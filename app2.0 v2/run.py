# from app import app
# if __name__ == '__main__':
#     app.run(debug = True)

# couchdb -> http://localhost:5984/_utils/index.html 
from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify, abort
# from couchdb import Server
import couchdb
from flaskext.couchdb import Document
import json

app = Flask(__name__, static_url_path='/static')
app.debug=True


# Opening JSON file
# f = open('data/health.json')
# data = json.load(f)
# print(data)
# for i in data['id']:
#     print(i)
# f.close()

# import db
username = "admin"
password = "admin"
#employment = couchdb.Database("http://172.26.130.73:5984/_utils/#database/employment/_all_docs")
#employment.resource.credentials(username, password)
# http://172.26.130.73:5984/_utils/#/_all_dbs
#couch = couchdb.Server('http://172.26.130.73:5984/_utils/')
#income = couch["employment"]
username = "admin"
password = "admin"
diversity_search = couchdb.Database("http://172.26.130.73:5984/_utils/#database/diversity_search")
diversity_search.resource.credentials = (username, password)
diversity_search.view('_all_docs', include_docs=True)

# data1=dict()
# while(true):
# for item in employment.view('_all_docs', group=True, group_level=1):
#    print(item)
#    data1[item.key] = item.value
# print(data1)


# class User(Document):
#     doc_type = 'User'
# @app.route('/db', methods=['GET', 'POST'])
# def register():
# 	user = {
# 	"username":"media site", 
# 	"email":"justmail@gmail.com",
# 	"password":"encrypteddata"
# 	}
# 	db = server['muocouch'] #select the database
# 	doc_id, doc_rev = db.save(user) #store your data in th database
#       # Use the view function to fetch your data from CouchDB
#    map_func = '''function(doc) { emit(doc.doc_rev, doc); }'''
#    # Get all the data by running a query set
#    myQuery = User.query(db, map_func, reduce_fun=None, reverse=True)
#    q = [i['username'] for i in myQuery] # Loop out all the usernames from the database
#    q2 = [i['email'] for i in myQuery] # Loop out all the email addresses from the database
#    q3 = q+q2 # Merge both queries into a single list
#    print(q3)
# 	return "<h2>Your data should now be in the database</h2>"


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return redirect('/')

@app.route('/income', methods=['GET', 'POST'])
def topic1():
    return redirect('/')

@app.route('/test')
def test():
   return render_template('test.html')

@app.route('/analysis')
def analysis():
   return render_template('analysis.html')

@app.route('/youtube')
def youtube():
   return render_template('youtube.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/health')
def topic2():
   return render_template('map2.html')

@app.route('/language')
def topic3():
   return render_template('map3.html')

@app.route('/sentiment')
def topic4():
   return render_template('map4.html')

if __name__ == '__main__':
   app.run(debug = True)