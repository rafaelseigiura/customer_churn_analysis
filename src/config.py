features = ['tenure', 'TotalCharges','MonthlyCharges','gender','SeniorCitizen',
            'Partner','Dependents','PhoneService','MultipleLines','InternetService',
            'OnlineSecurity','OnlineBackup','DeviceProtection', 'TechSupport','StreamingTV', 
            'StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod']
features_num = ['tenure', 'TotalCharges','MonthlyCharges']

features_cat = ['gender','SeniorCitizen','Partner','Dependents','PhoneService',
               'MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
               'DeviceProtection', 'TechSupport','StreamingTV','StreamingMovies', 
               'Contract', 'PaperlessBilling','PaymentMethod']
target = "Churn"