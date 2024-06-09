# Import packages
import pandas as pd
from sqlalchemy import create_engine

# Create an engine that connects to the database file
engine = create_engine("sqlite:///data.db")

# Read one of the CSV files into a pandas dataframe
df_train1 = pd.read_csv("train.csv")

# Write the dataframe to the train_table in the database, appending it if it already exists
df_train1.to_sql("train_table", engine, if_exists="append", index=False)
