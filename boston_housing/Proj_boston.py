import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.cross_validation import ShuffleSplit
from sklearn.linear_model import LinearRegression

import sklearn.metrics
# Import supplementary visualizations code visuals.py
#import visuals as vs

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

