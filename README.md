virtualenv flask
cd flask
source bin/activate
pip install flask
cd -
python run.py

Another method
pip install virtualenv
virtualenv env2  # create a new env
pip install flask
cd -
python run.py


<!-- couchdb -->
sudo chown -R $(whoami) /usr/local/bin /usr/local/lib /usr/local/include /usr/local/share <!-- might need this -->

npm install -g couchimport

curl -u admin:admin -X GET http://172.26.130.73:5984/employment/_all_docs\?include_docs\=true > /Users/clairezhang/Documents/2022S1/CCC/app_couchdb/data/employment.json

curl -u admin:admin -X GET http://172.26.130.73:5984/health/_all_docs\?include_docs\=true > /Users/clairezhang/Documents/2022S1/CCC/app_couchdb/data/health.json

curl -u admin:admin -X GET http://172.26.130.73:5984/diversity/_all_docs\?include_docs\=true > /Users/clairezhang/Documents/2022S1/CCC/app_couchdb/data/diversity.json