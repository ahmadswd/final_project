import pandas as pd

def say_hello():
    print("Hello, Ahmad.")

class DataFrameColumnAdder:
    def __init__(self, dataframe):
        self.df = dataframe

    def add_column(self, column_name, values):
        self.df[column_name] = values

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
column_adder = DataFrameColumnAdder(df)
column_adder.add_column('C', [7, 8, 9])
print(df)

df = pd.read_csv("Resources/diabetes.csv")