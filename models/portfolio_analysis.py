import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Function to train the model
def train_model(stock_data, mutual_fund_data):
    # Load and preprocess data
    stocks_df = pd.read_csv(stock_data)
    mutual_funds_df = pd.read_csv(mutual_fund_data)
    
    # Example: Using only investment amount and NAV for a simple regression
    X = stocks_df[['investment_amount', 'NAV']].values
    y = stocks_df['returns'].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model
    with open('models/linear_regression_model.pkl', 'wb') as f:
        pickle.dump(model, f)

def analyze_portfolio(stocks_df, mutual_funds_df):
    # Load the trained model
    with open('models/linear_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Perform predictions
    X = stocks_df[['investment_amount', 'NAV']].values
    predicted_returns = model.predict(X)

    analysis_results = {
        "predicted_returns": predicted_returns.tolist(),
        "suggestions": "Consider diversifying your portfolio with low-risk mutual funds."
    }

    return analysis_results
