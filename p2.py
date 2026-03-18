import pandas as pd


data = {
    "Name": ["Priyanshu", "Amit", "Rohit"],
    "Age": [22, 25, 27],
    "City": ["Bangalore", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("sample.csv", index=False)