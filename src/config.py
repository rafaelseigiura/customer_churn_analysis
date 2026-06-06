from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


FEATURES = ['tenure', 'TotalCharges','MonthlyCharges','gender','SeniorCitizen',
            'Partner','Dependents','PhoneService','MultipleLines','InternetService',
            'OnlineSecurity','OnlineBackup','DeviceProtection', 'TechSupport','StreamingTV', 
            'StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod']
FEATURES_NUM = ['tenure', 'TotalCharges','MonthlyCharges']

FEATURES_CAT = ['gender','SeniorCitizen','Partner','Dependents','PhoneService',
               'MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
               'DeviceProtection', 'TechSupport','StreamingTV','StreamingMovies', 
               'Contract', 'PaperlessBilling','PaymentMethod']
TARGET = "Churn"

MODELS_PARAMETERS = {
    
    "Logistic Regresison":LogisticRegression(
        class_weight='balanced', 
        random_state = 42,
        max_iter=1000
    ),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=10,
        min_samples_leaf=5,
        class_weight='balanced',
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        max_depth= 5,
        min_samples_split= 10,
        min_samples_leaf= 5,
        class_weight='balanced',
        random_state=42
    ),
    "XGBoost": XGBClassifier(
        max_depth=4,
        learning_rate=0.05,
        n_estimators=500,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=3
    )
    
}