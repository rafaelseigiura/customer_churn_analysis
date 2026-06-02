from src.preprocess import churn_mapped, train_test, create_preprocessor
from src.data.load_data import import_dataset
from src.config import features, features_cat, features_num, target

df = import_dataset(r"data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv")

X = df[features]
y = churn_mapped(df,target)


X_train, X_test, y_train, y_test = train_test(X,y)

preprocessor = create_preprocessor(features_num,features_cat)

