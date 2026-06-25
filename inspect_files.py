import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".xlsx"):
        df = pd.read_excel(os.path.join(folder, file))

        print("\n" + "="*60)
        print(file)
        print("="*60)
        print("Shape:", df.shape)
        print("Columns:")
        print(df.columns.tolist())
        