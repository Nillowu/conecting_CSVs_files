import glob
import pandas
import os
from pathlib import Path


files = glob.glob(r"C:\Users\andrs\PycharmProjects\parsing\*.csv")
corrected_files = [str(Path(file)) for file in files]

combined = pandas.DataFrame()

for file in files:
    data = pandas.read_csv(file)
    data['filename'] = file
    combined = pandas.concat([combined, data])

combined.to_csv('combined.csv', index=False, encoding='utf-8-sig')
