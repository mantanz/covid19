import pandas as pd
df = pd.read_csv('input.csv')
total = df.sum()
df.append((total.replace(total[0],'World')), ignore_index=True).to_csv('output.csv')