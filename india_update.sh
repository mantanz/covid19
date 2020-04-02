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

cp ./data_csv/india_data.json ./data_csv/india_data_yesterday.json
cp ../api/data.json ./data_csv/india_data.json

git add -A
git commit -m "india data updated" -a
git push

python3 push.py india_data_yesterday.json
python3 push.py india_data.json