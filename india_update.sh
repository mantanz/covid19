pwd=`pwd`
echo $pwd
cd ../api
git pull
sleep 60
cd $pwd
echo $pwd 

git stash
git pull --rebase
git stash apply

diff --brief ../api/data.json ./data_csv/india_data.json >/dev/null
comp_value=$?

if [ $comp_value -eq 1 ]
then
    cp ./data_csv/india_data.json ./data_csv/india_data_yesterday.json
    cp ../api/data.json ./data_csv/india_data.json
    
    python3 push.py india_data_yesterday.json
    python3 push.py india_data.json
else
    echo "do something because they're identical"
fi

git add -A
git commit -m "india data updated" -a
git push