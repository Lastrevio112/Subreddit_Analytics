import pandas as pd
def read_data(subreddit):
    df = pd.read_excel("ExcelFiles/" + subreddit + ".xlsx", index_col=0)
    return df

def convertColumnsOf_DF_to_Int(dataFrame, listOfColumns):
    for col in listOfColumns:
        dataFrame[col] = dataFrame[col].astype(int)
    return dataFrame

