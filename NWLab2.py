# 50.012 NETWORKS LAB 3 
# Done by: 
# Hazel Lau (1001150)
# Samuel Lim (1000971) 

# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request, url_for, Response, json, jsonify
from random import randint
import requests
from functools import wraps 

app = Flask(__name__) 

fb = {}
fb['Kisa'] = ['55 05-31', '+6591234567', 'kisa@meow.com', '6th February']
fb['Samsam'] = ['55 08-35', '+6591234567', 'samsam@meow.com', '25th January']
fb['Shonz'] = ['59 09-smth', '+6591234567', 'shonz@meow.com', '26th October']
fb['Js'] = ['Punggol', '+6591234567', 'js@meow.com', '26th January']
fb['Junqi'] = ['Bedok', '+6591234567', 'junqi@meow.com', 'March']

favegifs = []

def check_auth(username, password): 
    return username == 'admin' and password == 'secret'

def authenticate(): 
    message = {'message': 'Authenticate.'}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers[ 'WWW-Authenticate'] = 'Basic realm = "Example"'
    return resp 

def requires_auth(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        auth = request.authorization 
        if not auth: 
            return authenticate() 
        elif not check_auth(auth.username, auth.password): 
            return authenticate() 
        return f(*args, **kwargs) 
    return decorated

@app.route('/secrets') 
@requires_auth 
def api_hello(): 
    return "Shh this is my top secret spy stuff!!!!!"

@app.route('/')
def index(): 
    stuffsaid = request.args.get('stuffsaid')
    giftag = request.args.get('giftag')
    if stuffsaid!=None:
        return render_template('stuffsaid.html', stuffsaid=stuffsaid)
    elif giftag!=None: 
        favegifs.append(giftag)
        return gifsandimgs(giftag) 
    else:
        return render_template('htmltemplate.html')

@app.route('/friendbook', methods = ['POST', 'GET', 'PUT', 'PATCH'])
@requires_auth
def friendbook(): 
    if request.method == 'POST': 
        if request.headers['Content-Type'] == 'application/json':
            req_json = request.get_json()
            name = req_json["name"]
            add = req_json["add"]
            phone = req_json["phoneno"]
            email = req_json["email"]
            birthday = req_json["birthday"]
        else:            
            name = request.form.get('submitname')
            add = request.form.get('address')
            phone = request.form.get('phoneno')
            email = request.form.get('email')
            birthday = request.form.get('birthday')
        if name!=None: 
            fb[name] = [add, phone, email, birthday]  
    elif request.method == 'GET': 
        deletename =  request.args.get('deletename') 
        api_deletename(deletename)
    elif request.method == 'PUT': 
        if request.headers['Content-Type'] == 'application/json': 
            req_json = request.get_json()
            name = req_json["name"]
            add = req_json["add"]
            phone = req_json["phoneno"]
            email = req_json["email"]
            birthday = req_json["birthday"]
        else:
            name = request.args.get('name')
            add = request.args.get('add')
            phone = request.args.get('phoneno')
            email = request.args.get('email')
            birthday = request.args.get('birthday')
        if name!=None: 
            fb[name]=[add, phone, email, birthday]

    elif request.method == 'PATCH': 
        name = request.args.get('name') 
        add = request.args.get('add')
        phone = request.args.get('phoneno')
        email = request.args.get('email')
        birthday = request.args.get('birthday')
        if name!=None: 
            if add!=None:
                fb[name][0] = add
            if phone!=None: 
                fb[name][1] = phone 
            if email!=None: 
                fb[name][2] = email 
            if birthday!=None: 
                fb[name][3] = birthday
    return render_template('friendbook.html', fb = fb)

@app.route('/friendbook/<name>')
def api_getname(name):
    param = fb.get(name, None)
    if param!=None:
        data = {
            'Name' : name, 
            'Address' : param[0],
            'Phone Number' : param[1],
            'Email Address' : param[2],
            'Birthday' : param[3]
        }
    else: 
        data = {
            'Name' : "Does not Exist"
        }
    js = json.dumps(data)
    resp = Response(js, status = 200, mimetype='application/json')
    return resp

@app.route('/deletefriend/<name>', methods = ['DELETE'])
@requires_auth
def api_deletename(name): 
    param = fb.get(name,None) 
    if param!=None: 
        fb.pop(name, None)
        resp = Response(status = 200)
    else: 
        resp = Response(status = 404)
    return resp


@app.route('/contact')
def contact(): 
    return render_template('contact.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        submitname = request.form.get('submitname')
        if submitname!=None:
            return render_template('submitname.html', submitname=submitname)
        else:
            return render_template('htmltemplate.html')

@app.route('/gifsandimgs')
def gifsandimgs(giftag): 
    apilink = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=" + giftag + "&rating=pg-13"

    r = requests.get(apilink) 
    
    imgurl = r.json()['data']['image_url']
    print(favegifs)
    return render_template('gifsandimgs.html', imgurl=imgurl, giflist=favegifs)



if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0') 
