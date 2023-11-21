import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.feature_selection import f_regression
from cohortfunctions import *

def foodsecurity(predictors):
    # Reading the data
    print("Reading Data")
    cwd = os.getcwd()
    df = pd.read_excel(f"{cwd}/Datasets/2D dataset.xlsx")
    df = df.drop(["Country Code", "temperature change per country in 2022"], axis = 1)

    # Getting rid of the NaNs using imputation
    print("Imputing...")
    imp = IterativeImputer(max_iter=1000, random_state=0)
    df_imp = imp.fit_transform(df.iloc[:,1:])
    df_imp = pd.DataFrame(df_imp)
    print(df_imp.columns, df.columns)
    df_imp.columns = df.iloc[:,1:].columns
    df_imp["Country"] = df.loc[:, ["Country"]]
    print(df_imp)
    print("Imputed!")

    df_country_name = df_imp["Country"]
    df_without_country_name = df_imp.drop(["Country"], axis = 1)

    #Normalize
    print("Normalizing")
    df_norm,df_norm_means,df_norm_stds = normalize_z(df_without_country_name)
    df_norm.to_csv("geographical_processed_data.csv", mode = "w")
    print(df_norm.head())
    df_norm = df_norm.dropna()
    print("Normalized!")

    # Prepping the data
    print("Prepping data!")
    target = ["Prevalence of moderate or severe food insecurity in the total population (percent) (2022)"]
    df_features, df_target = get_features_targets(df_norm, predictors, target)
    df_features_train, df_features_test, df_target_train, df_target_test = split_data(df_features, df_target, test_size = 0.2)
    X = prepare_feature(df_features_train)
    target = prepare_target(df_target_train)

    # gradient descent time
    print("Gradient Descent Time")
    iterations = 1500
    alpha = 0.01
    beta = np.zeros((len(predictors)+1,1))

    beta, J_storage = gradient_descent_linreg(X, target, beta, alpha, iterations)

    # predicting
    print("Predicting")
    skpred = LinearRegression()
    skpred.fit(df_features, df_target)
    pred = predict_linreg(df_features_test, beta)
    print(pred)
    print("Predicted!")

    #calculate model evaluators
    target_test = prepare_target(df_target_test)
    feature_test = prepare_feature(df_features_test)

    #Mean squared error
    print("Calculating MSE")
    mse = mean_squared_error(target_test, pred)
    print(f"Mean Squared Error: {mse}")

    #f-stat 
    print("Calculating f-stat")
    stat_values = pd.DataFrame()
    stat_values["f-stat"],stat_values["p-values"] = f_regression(df_features, df_target.values.ravel())
    print(stat_values)

    # CV with scores
    metrics = ['r2', 'neg_mean_squared_error']
    cv_results = cross_validate(skpred, df_features, df_target, cv=10,
                                scoring=metrics, return_train_score=True)
    cv_df = pd.DataFrame(cv_results)
    print(cv_df) 
    EVAL = 'test_neg_mean_squared_error'
    print(f"Average {EVAL}: {np.mean(cv_df[EVAL])}")
