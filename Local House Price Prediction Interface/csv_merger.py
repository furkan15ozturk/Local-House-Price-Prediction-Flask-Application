import modules
import os
import glob
import pandas as pd


# List all csv files only

csv_files = glob.glob('*.{}'.format('csv'))


df_append = pd.DataFrame()

# for file in csv_files:
#             df_temp = pd.read_csv(file, encoding='latin1')
#             df_append = df_append.append(df_temp, ignore_index=True)

df_concat = pd.concat([pd.read_csv(f, encoding='latin1') for f in csv_files], ignore_index=True)

# (df_concat.tail())
df_concat.to_csv(r'C:\Users\furka\OneDrive\Masaüstü\GPII Project\Local House Price Prediction Interface\CSV Files\house_price_istanbul.csv')

