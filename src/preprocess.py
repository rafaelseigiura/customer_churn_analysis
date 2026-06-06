from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.config import FEATURES, FEATURES_CAT, FEATURES_NUM, TARGET, MODELS_PARAMETERS
import pandas as pd

def total_charges(df):
     
    total_charges = pd.to_numeric(df['TotalCharges'], errors='coerce')
    total_charges = total_charges.fillna(total_charges.median())
    return total_charges

def churn_mapped(df,target):
    return df[target].map(
        {
            "Yes":1,
            "No":0
        }
    )
    
def train_test(X,y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    return X_train, X_test, y_train, y_test 

def create_preprocessor(features_num,features_cat):
    return ColumnTransformer(
        transformers=[
            ('num',StandardScaler(), features_num),
            ('cat', OneHotEncoder(handle_unknown='ignore'), features_cat)
        ]
    )
    
def build_pipeline(model):
    return Pipeline(steps=[
        ('preprocessor',create_preprocessor()),
        ('model', model)
    ])
