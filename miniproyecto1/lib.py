import numpy as np


def load_data(sub_sample=True):
    """CArga los datos y convierte al sistema adecuado"""
    path = "altura_peso.csv"
    data = np.genfromtxt(path, delimiter=",", skip_header=1, usecols=[1, 2])
    height = data[:, 0]
    weight = data[:, 1]
    gender = np.genfromtxt(
        path,
        delimiter=",",
        skip_header=1,
        usecols=[0],
        converters={0: lambda x: 1 if b"Female" in x else 0},
    )

    height *= 0.025
    weight *= 0.454

    # sub-muestreo
    if sub_sample:
        height = height[::50]
        weight = weight[::50]
 
    return height, weight, gender


def standarizer(X):
    """Estandariza el conjutno de datos original"""
    mu, sigma = np.mean(X), np.std(X)
    X = (X - mu)/sigma
    
    return X, mu, sigma


def build_model_data(height, weight):
    """A partir de (y,tX) obtiene los datos de la regresion en forma matricial"""
    y = weight
    X = height
    num_samples = len(y)
    X_ = np.c_[np.ones(num_samples), X]
    return y, X_


