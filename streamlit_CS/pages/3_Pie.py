# 3_Pie.py  (or a Jupyter Notebook cell)

import pandas as pd
import plotly.express as px
from pathlib import Path

# Define path to CSV file
data_path = Path("data/pie_demo.csv")

# Read the CSV file
df = pd.read_csv(data_path)

# Check that the file loaded correctly
print("Data loaded successfully:")
print(df)

# Create an interactive pie chart
fig = px.pie(
    df,
    names='Category',
    values='Value',
    title='Interactive Pie Chart from pie_demo.csv',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Optional: pull slices slightly outward for emphasis
fig.update_traces(textinfo='percent+label', pull=[0.05]*len(df))

# Show interactive plot
fig.show()
