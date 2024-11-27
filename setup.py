import pandas as pd
import os

# Create data directory
os.makedirs('data', exist_ok=True)

# Create proper CSV structure
data = pd.DataFrame({
    'revenue': [100000, 120000, 95000, 140000],
    'costs': [80000, 90000, 85000, 100000],
    'profit': [20000, 30000, 10000, 40000]
})

# Save with proper formatting
data.to_csv('data/financial_data.csv', index=False)