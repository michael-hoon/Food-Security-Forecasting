from sklearn.linear_model import LinearRegression
import pandas as pd
import os

class Model():
    def __init__(self):
        data = pd.read_excel()
        self.model = LinearRegression()
        
    def predict(self, population, infant_mortality, temperature, gini_index, human_development_index):
        xTest = [population, infant_mortality, temperature, gini_index, human_development_index]
        return self.model.predict(xTest)
