from scipy import stats
import numpy as np
from cohortfunctions import *


class CohortLinearRegression():
    """
    Streamlined object using cohort functions
    """
    def __init__(self, df=None):
        self.df = df

    def fit(self, X=None, y=None):

        iterations = 2500
        alpha = 0.01
        beta = np.zeros((len(X.columns)+1,1))
        beta, J_storage = gradient_descent_linreg(X, y, beta, alpha, iterations)
        self.beta = beta
        self.J_storage = J_storage

        return self

    def predict(self, X):
        return predict_linreg(X, self.beta)
