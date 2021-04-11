from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from src.helperfunctions.fixUnbalance import getBalanced
from src.helperfunctions.getOneHotEncodings import getOneHotEncodings
import pandas as pd

def getData(churned_y_valyes, X_values,categorical_features, numerical_features):
    """

    :param churned_y_valyes: DF - user_id, churn_ind
    :param X_values: Raw X features
    :param categorical_features
    :param numerical_features
    :return: (Train,Test,Validation) Data set
    """

    # add y to X correctly - they should all match
    full_df = pd.merge(X_values,churned_y_valyes,on=["user_id"],how="inner")

    X = full_df[numerical_features+categorical_features+["user_id"]]
    # users = full_df["user_id"].values.tolist()
    y = full_df["churn_ind"].values.tolist()
    # get 1 hot encodings
    X_tmp,cat_dummy_variables = getOneHotEncodings(feature_list=categorical_features,X=X)
    # correct the imbalance the data
    X_full = X_tmp[cat_dummy_variables+numerical_features]

    X_new,y_new = getBalanced(X_full,y,"over")

    # split model into train, test and validation
    # 0.6 train, 0.2 #test, 0.2 #val
    X_train, X_test, y_train, y_test= train_test_split(X_new, y_new, test_size=0.2, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

    return X_train, X_val, X_test,y_train, y_val, y_test


def runModel(X_train, X_val, X_test,y_train, y_val, y_test):
    """
    :param X_train,
    :param X_val,
    :param X_test
    :param y_train
    :param y_val
    :param y_test
    :return: model
    """

    # get model
    model = XGBClassifier()
    # model = GaussianProcessClassifier(random_state=0)
    # fit the model
    # print("X_train data")
    # print(X_train.head())
    feature_cols = X_train.loc[:,X_train.columns!="user_id"].columns
    print(feature_cols)
    model.fit(X_train.loc[:,feature_cols],y_train)

    # predict on test
    y_test_pred = model.predict(X_test.loc[:,feature_cols])
    y_val_pred = model.predict(X_val.loc[:,feature_cols])

    # return metrics values
    target_names=["not_churned","churned"]
    print("Classification Report for validation")
    print(classification_report(y_val, y_val_pred, target_names=target_names))

    print("Classification Report for test")
    print(classification_report(y_test, y_test_pred, target_names=target_names))

    importance = model.feature_importances_
    # summarize feature importance
    features_importance = pd.DataFrame()
    features_importance["feature"] = feature_cols.tolist()
    features_importance["importance"] = importance
    features_importance = features_importance.sort_values("importance",ascending=False)
    return model,features_importance