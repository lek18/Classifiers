import pandas as pd
import numpy as np

def getchurnedDf(timelimit,user_id,equity_value_data):
    """
    :param timelimit: the number of days required for user to have churned
    :param user_id: string representing the user id
    :param equity_value_data: pandas data frame - ur equity value data
    :return: pandas dataframe with cols user id, churn times, churned
    """
    # filtering user data
    user_data = equity_value_data.loc[equity_value_data["user_id"] == user_id][["date", "close_equity"]]
    # obtain the full lenght of the time series
    # min_date = min(user_data["date"])
    # full_year = pd.DataFrame(pd.date_range(start=min_date,end="2017-08-18",freq="d"),columns = ["date"])
    # i like to use date instead of timestamp ;)
    # full_year["date"] = full_year["date"].dt.date
    # do left join on the table full year
    # user_id_ts = pd.merge(full_year,user_data, how="left").sort_values(["date"])
    # fill missing days with 1 ie <$10
    # user_id_ts["close_equity"] = user_id_ts["close_equity"].fillna(1)
    # user_id_ts.plot()
    equity =  user_id_ts["close_equity"]
    # count = 0
    all_windows = []
    window_size = 0

    for i in equity:
        if i ==1:
            window_size+=1
        else:
            all_windows.append(window_size)
            window_size=0

    output_df = pd.DataFrame()
    output_df["less_10_windows"] = all_windows
    output_df["user_id"] = user_id
    output_df["churned_ind"] = np.where(output_df["less_10_windows"]>=timelimit,1,0)

    return output_df
