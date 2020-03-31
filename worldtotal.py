import pandas as pd
import sys
df = pd.read_csv(sys.argv[1])
total = df.sum()
df.append((total.replace(total[0],'World')), ignore_index=True).to_csv(sys.argv[2])