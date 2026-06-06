from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.config import FEATURES, FEATURES_CAT, FEATURES_NUM, TARGET, MODELS_PARAMETERS
from preprocess import total_charges, churn_mapped, train_test, create_preprocessor, build_pipeline
import pandas as pd


def pipeline():

    return{
        nome: build_pipeline(modelo)
        for nome, modelo in MODELS_PARAMETERS.items()
    }
    
def train_model(X_train, y_train):
    pipeline = build_pipeline()
    
    for nome, pipeline in pipeline.items():
        pipeline.fit(X_train, y_train)
        print(f"Modelo {nome} treinado")
    
    return pipeline