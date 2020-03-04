from flask import Flask, render_template, url_for
import json
import requests
TEMPLATE_DIR='./templates'

STATIC_DIR='./static'
app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
URL = 'http://localhost:3001/api/products'
request = requests.get(url=URL)
data = request.json()['docs']
print(data)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', data=data)


@app.route("/about")
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=1)
