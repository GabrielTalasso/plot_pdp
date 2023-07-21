import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay
from sklearn.inspection import  partial_dependence

from preprocessing import preprocessing
from plot_pdp_dash import plot_pdp_dash

class PDP():

    def __init__(self, data, clf):
        self.data = data
        self.clf  = clf
        
    def calcule_pdp(self,features):
        self.pdp = partial_dependence(self.clf, self.data, features=features,
                   kind = 'average')
        return self.pdp

    def plot_pdp(self, feature):
        features = [list(self.data.columns).index(feature)]
        PartialDependenceDisplay.from_estimator(self.clf, self.data, features = features)
        plt.show()

    def plot_pdp_iterativo(self, pdp_results, feature):
        plot_pdp_dash(self.data, pdp_results, feature)
    