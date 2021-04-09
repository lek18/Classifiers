import pandas as pd
import sys
import os

from questions.churn_users import getchurnedDf


def main():

    path = os.getcwd()
    feature_data = pd.read_csv(path+"/data/features_data.csv",header=0)
    equity_value_data = pd.read_csv(path+"/data/equity_value_data.csv",header =0)
    equity_value_data["date"] = pd.to_datetime(equity_value_data["timestamp"].astype(str)).dt.date

    # Basic EDA
    # print("features",feature_data.head)
    # print(feature_data.columns)
    # print("timeseries",equity_value_data.head)
    # number of users are the same across all the data
    # print('number of unique user in df1 , df2 respectively is {0} and {1}'.format(len(feature_data["user_id"].unique().tolist()),len(equity_value_data["user_id"].unique().tolist())))
    # feature_Desc = feature_data.astype("object").describe()

    # Question 1 - determining the number of churn users.
    # plan is to fill the missing dates in our time series and check how many times a user churned, and if it did at least once, classify it as a churner
    # unique users
    unique_users = equity_value_data["user_id"].unique().tolist()
    print(len(unique_users))
    output = []
    for users in unique_users[0:100]:
        df = getchurnedDf(user_id=users,timelimit=28,equity_value_data=equity_value_data)
        output.append(1 if sum(df["churned_ind"])>=1 else 0)
    print(sum(output)/len(output))


    # unique users number of dates of data
    user_date_count = equity_value_data.groupby(["user_id"],as_index=False).count().sort_values("timestamp",ascending=False)
    print("Number of unique dates is {0} vs 365 days".format(len(user_date_count["close_equity"].unique())))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
