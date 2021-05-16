import pandas as pd
import lottodataframe
dataframe_lotto = lottodataframe.get_lotto_df()

last_two_list = []

for key,row in dataframe_lotto.iterrows():
    last_two = int(row['two'])
    last_two_list.append(last_two)
    
last_two_list = pd.Series(last_two_list)

print(last_two_list.value_counts().head(10))