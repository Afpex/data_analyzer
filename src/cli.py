from analyzer import DataAnalyzerAgent
import argparse

def main():
    parser = argparse.ArgumentParser(description='Financial Data Analyzer CLI')
    parser.add_argument('--data', type=str, default='data/financial_data.csv', help='Path to CSV file')
    parser.add_argument('--query', type=str, help='Natural language query')
    
    args = parser.parse_args()
    agent = DataAnalyzerAgent()
    agent.load_data(args.data)
    
    if args.query:
        print(agent.query(args.query))
    else:
        print(agent.analyze())

if __name__ == "__main__":
    main()