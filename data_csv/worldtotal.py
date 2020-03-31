import pandas as pd
df = pd.read_csv('/Users/mantanz/Downloads/git_rep/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
total = df.sum()
df.append((total.replace(total[0],'World')), ignore_index=True).to_csv('/Users/mantanz/Desktop/covid19/cntry_timeseries_confirmed.csv')

df1 = pd.read_csv('/Users/mantanz/Downloads/git_rep/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
total = df1.sum()
df1.append((total.replace(total[0],'World')), ignore_index=True).to_csv('/Users/mantanz/Desktop/covid19/cntry_timeseries_recovered.csv')

df2 = pd.read_csv('/Users/mantanz/Downloads/git_rep/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
total = df2.sum()
df2.append((total.replace(total[0],'World')), ignore_index=True).to_csv('/Users/mantanz/Desktop/covid19/cntry_timeseries_deaths.csv')