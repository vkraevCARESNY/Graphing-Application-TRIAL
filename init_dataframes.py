import pandas as pd

def get_dataframes(file_path_list,ID_vals):
    df_list = []
    missing_ID = 0
    for i in range(len(file_path_list)):

        temp_df = pd.read_csv(file_path_list[i])
        if ID_vals[i] is not "":
            temp_df["ID"] = ID_vals[i]
            ID = ID_vals[i]
        else:
            ID = "Missing ID " + str(missing_ID)
            missing_ID += 1

        df_list.append((ID,temp_df))

    return df_list