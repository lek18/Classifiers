import pandas as pd
import numpy as np
import datetime
def getchurnedDf(timelimit,equity_value_data):
    """
    :param timelimit: the number of days required for user to have churned
    :param user_id: string representing the user id
    :param equity_value_data: pandas data frame - ur equity value data
    :return: pandas dataframe with cols user id, churn times, churned
    """
    # sort the data
    user_data = equity_value_data[["user_id","close_equity","date"]].sort_values(["user_id","date"],ascending=True)
    # Shift the close equity value
    user_data["prev_date"] = user_data.groupby(["user_id"])["date"].shift()
    # drop the NAS
    user_data = user_data.dropna()
    # date difference btw consecuitve days
    user_data["day_diff"] = (user_data["date"] - user_data["prev_date"]).astype('timedelta64[D]').astype(int)

    # if day_diff >= timelimit then 1 for churned else 0 for NOT churned
    user_data["churn_ind"] = np.where(user_data["day_diff"]>=timelimit,1,0)
    # print(user_data[user_data["user_id"]=="0012db34aa7b083f5714e7831195e54d"])
    rolled_user_data = user_data[["user_id", "churn_ind"]].groupby(["user_id"], as_index=False).sum()
    # print(rolled_user_data.columns)
    rolled_user_data.columns = ["user_id","no_churn_times"]
    rolled_user_data["churn_ind"] = np.where(rolled_user_data["no_churn_times"]>=1,1,0)
    # print(rolled_user_data.head())
    return rolled_user_data
