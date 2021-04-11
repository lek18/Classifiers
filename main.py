import pandas as pd
import sys

from src.pipelines.xgboostmodel import getData, runModel

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from src.pipelines.obtain_minority_class import getchurnedDf


def main():
    path1 = sys.argv[1]
    feature_data = pd.read_csv(path1+"data/features_data.csv",header=0)
    equity_value_data = pd.read_csv(path1+"data/equity_value_data.csv",header =0)
    equity_value_data["date"] = pd.to_datetime(equity_value_data["timestamp"].astype(str)).dt.date

    # Basic EDA
    # print("features",feature_data.head())
    # print(feature_data.columns)
    categorical_features = ["risk_tolerance","investment_experience","liquidity_needs","platform","time_horizon"]
    numerical_features = ["time_spent","first_deposit_amount"]
    # print("timeseries",equity_value_data.head)
    # number of users are the same across all the data
    # print('number of unique user in df1 , df2 respectively is {0} and {1}'.format(len(feature_data["user_id"].unique().tolist()),len(equity_value_data["user_id"].unique().tolist())))
    # feature_Desc = feature_data.astype("object").describe()

    # Question 1 - determining the number of churn users.
    # plan is to fill the missing dates in our time series and check how many times a user churned, and if it did at least once, classify it as a churner
    # unique users
    # unique_users = equity_value_data["user_id"].unique().tolist()
    # print(len(unique_users))
    df = getchurnedDf(timelimit=28,equity_value_data=equity_value_data)
    # print(df.head())
    # print(df.sort_values("no_churn_times",ascending=False).head(20))
    # obtain percent of users that are churned
    # print("Number of Churned Users: {0}%".format(100*sum(df["churn_ind"])/len(df["churn_ind"])))

    ## Question 2

    # get the data
    X_train, X_val, X_test,y_train, y_val, y_test = getData(churned_y_valyes=df, X_values=feature_data, categorical_features=categorical_features, numerical_features=numerical_features)

    # train and get the model
    model,features_importance = runModel(X_train, X_val, X_test,y_train, y_val, y_test)

    print(features_importance.head(10))
    print(features_importance.tail(10))

    print(path1+"/data/feature_importance.csv")
    features_importance.to_csv("/data/feature_importance.csv",index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
