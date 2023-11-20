import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def normalize_z(dfin, columns_means=None, columns_stds=None):
    if columns_means == None:
        columns_means = dfin.mean()
    if columns_stds == None:
        columns_stds = dfin.std()
    dfout = (dfin-columns_means)/columns_stds
    return dfout, columns_means, columns_stds

def get_features_targets(df, feature_names, target_names):
    df_feature = df[feature_names]
    df_target = df[target_names]
    return df_feature, df_target

def prepare_feature(df_feature):
    x = df_feature.copy()
    if isinstance(df_feature, pd.DataFrame):
        x = x.to_numpy()
    else:
        x = x
    x.T
    x1 = np.insert(x, 0, 1, axis=1)
    return x1

def prepare_target(df_target):
    x = df_target.copy()
    if isinstance(df_target, pd.DataFrame):
        x = x.to_numpy()
    else:
        x = df_target
    x.T
    return x

def predict_linreg(df_feature, beta, means=None, stds=None):
    x = normalize_z(df_feature, means, stds)
    prepared_df = prepare_feature(x[0])
    return calc_linreg(prepared_df, beta)

def calc_linreg(X, beta):
    return np.matmul(X,beta)

def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    if random_state != None:
        np.random.seed(random_state)
    
    indices = df_feature.index
    testsz = int(test_size*len(indices))
    test_indices = sorted(np.random.choice(indices, testsz, replace = False))
    training_indices = list(set(indices) - set(test_indices))
    df_feature_train = df_feature.loc[training_indices]
    df_target_train = df_target.loc[training_indices]
    df_feature_test = df_feature.loc[test_indices]
    df_target_test = df_target.loc[test_indices]
    return df_feature_train, df_feature_test, df_target_train, df_target_test
  
def r2_score(y, ypred):
    return 1 - (np.sum((y - ypred)**2)/np.sum((y - np.mean(y))**2))

def mean_squared_error(target, pred):
    return np.mean((target - pred)**2)

def compute_cost_linreg(X, y, beta):
    J = 0
    m = X.shape[0]
    for i in range(m):
        J = J + 1/(2*m)*(calc_linreg(X[i],beta) - y[i])**2
    return J

def gradient_descent_linreg(X, y, beta, alpha, num_iters):
    m = y.shape[0]
    J_storage = np.zeros(num_iters)
    for i in range(num_iters):
        J_storage[i] = compute_cost_linreg(X, y, beta)
        beta = beta - (alpha/m)*np.matmul(X.T, calc_linreg(X,beta)-y) #np.matmul is derivative, divide by m to find average
    return beta, J_storage

def transform_features_quadratic(df_feature, colname, colname_transformed):
    df_copy = df_feature.copy(deep=True)
    df_copy[colname_transformed] = df_copy[colname]**2
    return df_copy

