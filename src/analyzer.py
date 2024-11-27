import pandas as pd
from typing import Dict, List, Any
import json

class DataAnalyzerAgent:
    """
    A financial data analysis agent that processes CSV data and provides insights.
    
    The agent can:
    - Load and validate financial data
    - Perform statistical analysis
    - Answer natural language queries about the data
    """

    def __init__(self):
        """Initialize the agent with an empty data store."""
        self.data = None
        
    def load_data(self, csv_path: str) -> None:
        """
        Load financial data from a CSV file into pandas DataFrame.
        
        Args:
            csv_path (str): Path to the CSV file containing financial data
        """
        self.data = pd.read_csv(csv_path)
        
    def analyze(self) -> Dict[str, Any]:
        """
        Perform comprehensive financial analysis on loaded data.
        
        Returns:
            Dict containing:
            - summary_stats: Basic statistical measures for numerical columns
            - correlations: Correlation matrix between numerical columns
            - missing_values: Count of missing values in each column
            
        Raises:
            Returns error dict if no data is loaded
        """
        if self.data is None:
            return {"error": "No data loaded"}
            
        analysis = {
            "summary_stats": {
                col: {
                    "mean": float(self.data[col].mean()),
                    "median": float(self.data[col].median()),
                    "std": float(self.data[col].std())
                }
                for col in self.data.select_dtypes(include=['float64', 'int64']).columns
            },
            "correlations": self.data.corr().to_dict(),
            "missing_values": self.data.isnull().sum().to_dict()
        }
        
        return analysis
        
    def query(self, question: str) -> str:
        """
        Natural language interface for data queries.
        
        Args:
            question (str): Natural language question about the data
            
        Returns:
            str: Answer to the question or error message if question not understood
            
        Example:
            >>> agent.query("What is the mean revenue?")
            "The mean of revenue is 1234.56"
        """
        if "mean" in question.lower():
            col = next((col for col in self.data.columns if col.lower() in question.lower()), None)
            if col:
                return f"The mean of {col} is {self.data[col].mean():.2f}"
        return "I couldn't understand that question."

def main():
    """
    Example usage of the DataAnalyzerAgent.
    
    Creates an agent instance, loads sample data, and prints analysis results.
    """
    agent = DataAnalyzerAgent()
    agent.load_data("data/financial_data.csv")
    results = agent.analyze()
    print(json.dumps(results, indent=2))
    
if __name__ == "__main__":
    main()