
from flask import Flask, redirect, render_template, make_response, jsonify
import json

app = Flask(__name__, static_url_path='/static')
app.debug=True


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