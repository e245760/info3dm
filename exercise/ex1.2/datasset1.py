import unittest
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

def true_function(x):
    x = np.array(x)
    return np.sin(np.pi * x * 0.8) * 10

def generate_observation_points(n=20, seed=0):
    np.random.seed(seed)
    return np.random.uniform(-1, 1, size=n)

def generate_true_values(x_obs):
    x_obs = np.array(x_obs)
    return true_function(x_obs)

def create_sample_dataframe(n=20, seed=0):
    x_obs = generate_observation_points(n=n, seed=seed)
    y_true = generate_true_values(x_obs)
    return pd.DataFrame({
        "観測点": x_obs,
        "真値": y_true
    })

df = create_sample_dataframe()

plt.scatter(df["観測点"], df["真値"], label="sample points")
plt.xlabel("観測点")
plt.ylabel("真値")
plt.legend()
plt.savefig("exercise/ex1.2/ex1.2.png")
plt.close()
