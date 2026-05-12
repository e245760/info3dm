import numpy as np
import pandas as pd

def true_function(x):
    x = np.asarray(x)
    return np.sin(np.pi * x * 0.8) * 10


def generate_observation_points(n=20, seed=0):
    np.random.seed(seed)
    return np.random.uniform(-1, 1, size=n)


def generate_true_values(x_obs):
    x_obs = np.asarray(x_obs)
    return true_function(x_obs)


def generate_noise(n=20, seed=0, mean=0.0, variance=2.0):
    np.random.seed(seed)
    std = np.sqrt(variance)
    noise = np.random.normal(loc=mean, scale=std, size=n)
    return noise / 2.0


def create_sample_dataframe(n=20, seed=0):
    x_obs = generate_observation_points(n=n, seed=seed)
    y_true = generate_true_values(x_obs)

    noise = generate_noise(
        n=n,
        seed=seed,
        mean=0.0,
        variance=2.0
    )

    y_obs = y_true + noise

    return pd.DataFrame({
        "観測点": x_obs,
        "真値": y_true,
        "観測値": y_obs
    })


df = create_sample_dataframe()

df.to_csv(
    "ex1.tsv",
    sep="\t",
    index=False
)