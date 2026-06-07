from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.config import FEATURES, FEATURES_CAT, FEATURES_NUM, TARGET, MODELS_PARAMETERS
from src.preprocess import total_charges, churn_mapped, train_test, create_preprocessor, build_pipeline, create_pipeline
import pandas as pd

    
def train_model(X_train, y_train):
    pipelines = create_pipeline()
    
    for nome, pipeline in pipelines.items():
        pipeline.fit(X_train, y_train)
        print(f"Modelo {nome} treinado")
    
    return pipelines