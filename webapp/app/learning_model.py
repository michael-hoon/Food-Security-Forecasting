from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import os

parent = os.path.dirname(os.getcwd())

class Model():
    def __init__(self):
        self.target = ["Prevalence of moderate or severe food insecurity in the total population (percent) (2022)"]
        self.predictors = ['Population', 'Infant mortality', 'temperature', "Gini's index", 'Human Development Index (2021)']
        self.data = pd.read_csv(f"{parent}/webapp/data/imputated_data.csv")
        self.feature_df = self.data.loc[:, self.predictors]
        self.target_df = self.data.loc[:,self.target]
        self.model = LinearRegression()
        self.model.fit(self.feature_df, self.target_df)
        #self.model.coef_ = np.array([-0.44147326,  0.41232714, -0.26634369,  0.19499116,  0.11442385], dtype=float)
        #self.model.intercept_ = np.array([0.00549848],dtype=float)
        
    def prediction(self, population, infant_mortality, temperature, gini_index, human_development_index):
        xTest = pd.DataFrame({'Population': [population],
                             'Infant mortality': [infant_mortality],
                             'temperature': [temperature],
                             "Gini's index": [gini_index],
                             'Human Development Index (2021)': [human_development_index]})
        #x_means = np.array([3.98312385e+07, 2.12015847e+01, 2.02841042e+01, 3.68663743e+01, 7.19362621e-01],dtype=float)
        #x_std = np.array([1.48891995e+08, 1.94589607e+01, 8.72662921e+00, 7.06347916e+00,1.53609214e-01],dtype=float)
        #normalized_values = (np.array([population, infant_mortality, temperature, gini_index, human_development_index],dtype=float) - x_means) / x_std
        #prediction = self.model.predict([normalized_values]) * 26.384990583237517 + 35.72993197278912
        return self.model.predict(xTest)[0][0]

