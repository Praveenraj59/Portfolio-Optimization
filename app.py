from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from models.portfolio_analysis import analyze_portfolio, train_model
#from quantum.quantum_optimizer import quantum_optimize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        # Get file paths for training
        stock_data = request.files['stock_data']
        mutual_fund_data = request.files['mutual_fund_data']
        
        # Train the model
        train_model(stock_data, mutual_fund_data)
        
        return "Training Complete!"
    
    return render_template('train.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get user input
    stock_data = request.files['stock_data']
    mutual_fund_data = request.files['mutual_fund_data']

    # Parse and process the data
    portfolio_df = pd.read_csv(stock_data)
    mutual_funds_df = pd.read_csv(mutual_fund_data)

    # Run classical analysis
    analysis_results = analyze_portfolio(portfolio_df, mutual_funds_df)

    # Quantum optimization
    optimal_strategy = quantum_optimize(analysis_results)

    return render_template('results.html', analysis=analysis_results, strategy=optimal_strategy)

if __name__ == '__main__':
    app.run(debug=True)
