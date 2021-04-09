import pandas as pd
def getOneHotEncodings(feature_list, X):
    """

    :param feature_list: feature list that are considered categorical features
    :param X: our entire feature data set
    :return: tuple of X but with added one hote feature list, one hot feature list
    """

    # create dummy table :
    dummy_table = pd.get_dummies(X[feature_list].astype("category"),prefix_sep="_",prefix=feature_list)

    # add dummy table columns to our X data
    tmp  = pd.concat([X,dummy_table],axis=1)

    return tmp,dummy_table.columns.tolist()
