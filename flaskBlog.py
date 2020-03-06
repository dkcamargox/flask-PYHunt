from flask import Flask, render_template, url_for, request, redirect
import json
import requests

# this init the app
TEMPLATE_DIR='./templates'
STATIC_DIR='./static'
app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


def requisistar( page ):
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
    print(funcs['en_dis'])
    # go to the home template, passing the data, the actual page of the requisition
    # the max number of pages, and the obj with the functions.
    return render_template('home.html', data=requisistar(page)[1], 
    page=page, pages=requisistar(page)[0], functions=funcs)


@app.route("/about")
def about_page():
    # not made yet
    return render_template('about.html')

# run 
if __name__ == '__main__':
    app.run(debug=1)
