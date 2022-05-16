<!-- flask environment setup -->
virtualenv flask
cd flask
source bin/activate
pip install flask
cd -

Another method
pip install virtualenv
virtualenv env2  # create a new env
pip install flask
cd -


<!-- retrieve couchdb database -->
curl -u admin:admin -X GET http://172.26.130.73:5984/output/_all_docs\?include_docs\=true > /Users/clairezhang/Documents/2022S1/COMP90024-project2/data/output.json

<!-- preprocess some data -->
<!-- python preprocess.py -->

<!-- render web -->
python run.py