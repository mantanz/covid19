pwd=`pwd`
echo $pwd
cd ../COVID-19
git pull
sleep 20
cd $pwd
echo $pwd 

git stash
git pull --rebase
git stash apply

python3 ./worldtotal.py ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv ./data_csv/cntry_timeseries_confirmed.csv

python3 push.py cntry_timeseries_confirmed.csv

python3 ./worldtotal.py ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv ./data_csv/cntry_timeseries_recovered.csv

python3 push.py cntry_timeseries_recovered.csv

python3 ./worldtotal.py ../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv ./data_csv/cntry_timeseries_deaths.csv

python3 push.py cntry_timeseries_deaths.csv

git add -A
git commit -m "global data updated" -a
git push
