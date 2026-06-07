
import pandas as pd
from sklearn.metrics import accuracy_score,recall_score, precision_score, f1_score

def threshold(model, X_test,y_test):
    y_proba = model.predict_proba(X_test)[:, 1]

    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    results = []

    for t in thresholds:
        y_pred = (y_proba >= t).astype(int)
        
        results.append({
            "threshold": t,
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred)
        })
    thresholds_df = pd.DataFrame(results)
    return thresholds_df.round(3)


def threshold_analysis(model, X_test, y_test, ltv_medio, taxa_conversao, custo_contrato):
    y_proba = model.predict_proba(X_test)[:,1]
    churn_real = sum(y_test)
    
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    results = []

    for t in thresholds:
        y_pred = (y_proba >= t).astype(int)
        
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        
        capturados = round(churn_real*rec)
        abordados = (capturados/prec) if prec > 0 else 0
        receita = capturados * ltv_medio * taxa_conversao
        receita_anual = capturados * (ltv_medio*12) * taxa_conversao
        custo = abordados * custo_contrato
        
        results.append({
            "Threshold": t,
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1": f1_score(y_test, y_pred),
            "Capturados": capturados,
            "Abordados": abordados,
            "Receita Mensal": round(receita, 0),
            "Receita Anual": round(receita_anual, 0),
            "Custo": round(custo, 0),
            "ROI": round(((receita - custo) / custo),3)*100 if custo > 0 else 0,
            
        })
    return pd.DataFrame(results)