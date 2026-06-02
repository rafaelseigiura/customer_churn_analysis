import pandas as pd

def import_dataset(path:str):
  
    df = pd.read_csv(path)
    return df
