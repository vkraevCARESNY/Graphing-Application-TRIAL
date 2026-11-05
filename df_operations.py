import pandas as pd

def merge_df(dupe_key, keys, df_list):
    return_df = pd.DataFrame()

    for i in range(len(df_list)):
        if dupe_key in df_list[i][1].columns.values.tolist():

            return_df[dupe_key] = df_list[i][1][[dupe_key]]
            break
    for i in range(len(keys)):
        for j in range(len(df_list)):
            if keys[i][0] == df_list[j][0]:
                print(keys[i][1])
                return_df[keys[i][1]] = df_list[j][1][[keys[i][1]]]

    return return_df
