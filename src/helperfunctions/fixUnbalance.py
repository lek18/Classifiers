from collections import Counter

from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

def getBalanced(X,y,strategy):
    """

    :param X: X features
    :param y: y features
    :param strategy: str - "over" or "under"
    :return: X,y but without its imbalance
    """
    # check current data distribution
    print("Current Balance data overview", Counter(y))

    # define the strategy to sample
    if strategy=="over":
        sampling_technique = RandomOverSampler(sampling_strategy="minority")
    elif strategy=="under":
        sampling_technique = RandomUnderSampler(sampling_strategy="majority")
    else:
        return "NO VALID STRATEGY"

    # fit the sampling technique
    X_new,y_new = sampling_technique.fit_resample(X,y)
    print("New Balance data overview",Counter(y_new))

    return X_new,y_new