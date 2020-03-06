from flask import Flask, render_template, url_for, request, redirect
import json
import requests

# this init the app
TEMPLATE_DIR='./templates'
STATIC_DIR='./static'
app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


def requisitar( page ):
    # this make the requisition from the backend 
    response = []
    __URL = 'http://localhost:3001/api/products?page='+ str(page)
    request = requests.get(url=__URL)
    pages = request.json()['pages']
    data = request.json()['docs']
    response.append(pages)
    response.append(data)
    return response

def enabled_disabled(truFals):
    # this return disabled or enabled for the button based in a codition, what
    # means if it's the last page disable the button
    if(truFals):
        return("disabled")
    else:
        return("enabled")

def requisitar_1produto(_id):
    __URL = 'http://localhost:3001/api/products/' + str(_id)
    # print(__URL)
    request = requests.get(url=__URL)
    return request.json()

# obj with the name of the functions I want use in the template
funcs = {
    "en_dis": enabled_disabled
}

@app.route("/")
@app.route("/home")
def home_page():
    # this take the var from the query with indicate what page is needed from the
    # requisition
    page = int(request.args.get('page', '1'))

    # go to the home template, passing the data, the actual page of the requisition
    # the max number of pages, and the obj with the functions.
    return render_template('home.html', data=requisitar(page)[1], 
    page=page, pages=requisitar(page)[0], functions=funcs)


@app.route("/products/<id>")
def product_page(id):
    # this make a requisition with the ID of the product, wicth return the response
    # for only one of the products

    res = requisitar_1produto(id)
    return render_template('about.html', product = res )

# run 
if __name__ == '__main__':
    app.run(debug=1)
