import numpy as np
import pandas as pd
import pymc as pm


def build_fast_switchpoint_model(data_series):
    n_obs = len(data_series)
    idx = np.arange(n_obs)
    obs_values = data_series.values
    
    mean_prior = np.nanmean(obs_values)
    std_prior = np.nanstd(obs_values) * 2.0

    with pm.Model() as model:
        # Continuous prior for tau over index range
        tau = pm.Uniform("tau", lower=0, upper=n_obs - 1)
        
        # Means before and after
        mu_1 = pm.Normal("mu_1", mu=mean_prior, sigma=std_prior)
        mu_2 = pm.Normal("mu_2", mu=mean_prior, sigma=std_prior)
        sigma = pm.HalfNormal("sigma", sigma=std_prior)
        
        # Smooth continuous transition (Sigmoid)
        # s controls transition sharpness; higher = sharper switch
        s = 50 
        weight = pm.math.sigmoid(s * (idx - tau) / n_obs)
        mu = (1 - weight) * mu_1 + weight * mu_2
        
        likelihood = pm.Normal("obs", mu=mu, sigma=sigma, observed=obs_values)
        
    return model