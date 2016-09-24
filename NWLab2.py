
# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request
from random import randint
import requests

app = Flask(__name__) 

@app.route('/')
def index(): 
    stuffsaid = request.args.get('stuffsaid')
    helloname = request.args.get('helloname') 
    if helloname!=None: 
        return hello(helloname)
    if stuffsaid!=None:
        return render_template('stuffsaid.html', stuffsaid=stuffsaid)
    else:
        return render_template('htmltemplate.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/contact')
def contact(): 
    return render_template('contact.html')

@app.route('/hello/<name>')
def hello(name): 
    if name=="shaun": 
        name = "shaun the uncool"
    return render_template('namepage.html', name=name)

@app.route('/gifsandimgs')
def gifsandimgs(): 
    apilink = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=meow&rating=pg-13"

    r = requests.get(apilink) 
        
    imgurl = r.json()['data']['image_url']
    return render_template('gifsandimgs.html', imgurl=imgurl)



if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0') 
