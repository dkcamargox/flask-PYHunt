from flask import Flask, render_template, url_for, request, redirect
import json
import requests
TEMPLATE_DIR='./templates'
STATIC_DIR='./static'
app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


def requisistar( page ):
    response = []
    __URL = 'http://localhost:3001/api/products?page='+ str(page)
    request = requests.get(url=__URL)
    pages = request.json()['pages']
    data = request.json()['docs']
    response.append(pages)
    response.append(data)
    return response

def enabled_disabled(truFals):
    if(truFals):
        return("disabled")
    else:
        return("enabled")


#routes 
funcs = {
    "en_dis": enabled_disabled,
    "rd": redirect
}

@app.route("/")
@app.route("/home")
def home_page():
    page = int(request.args.get('page', '1'))
    print(funcs['en_dis'])
    # api retorna já paginado, a variavel page define a pagina
    return render_template('home.html', data=requisistar(page)[1], 
    page=page, pages=requisistar(page)[0], functions=funcs)


@app.route("/about")
def about_page():
    return render_template('about.html')

# run 

if __name__ == '__main__':
    app.run(debug=1)
