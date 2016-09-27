# 50.012 NETWORKS LAB 2 
# Done by: 
# Hazel Lau (1001150)
# Samuel Lim (1000971) 

# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request, url_for, Response, json
from random import randint
import requests

app = Flask(__name__) 

fb = {}
fb['Kisa'] = ['55 05-31', '+6591234567', 'kisa@meow.com', '6th February']
fb['Samsam'] = ['55 08-35', '+6591234567', 'samsam@meow.com', '25th January']
fb['Shonz'] = ['59 09-smth', '+6591234567', 'shonz@meow.com', '26th October']
fb['Js'] = ['Punggol', '+6591234567', 'js@meow.com', '26th January']
fb['Junqi'] = ['Bedok', '+6591234567', 'junqi@meow.com', 'March']

@app.route('/')
def index(): 
    stuffsaid = request.args.get('stuffsaid')
    if stuffsaid!=None:
        return render_template('stuffsaid.html', stuffsaid=stuffsaid)
    else:
        return render_template('htmltemplate.html')

@app.route('/friendbook')
def friendbook(): 
    return render_template('friendbook.html', fb = fb)

@app.route('/friendbook/<name>')
def api_name(name):
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
def gifsandimgs(): 
    apilink = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=meow&rating=pg-13"

    r = requests.get(apilink) 
        
    imgurl = r.json()['data']['image_url']
    return render_template('gifsandimgs.html', imgurl=imgurl)



if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0') 
