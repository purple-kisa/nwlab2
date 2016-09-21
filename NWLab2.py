
# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request
from random import randint

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

@app.route('/hello/<name>')
def hello(name): 
    if name=="shaun": 
        name = "shaun the uncool"
    return render_template('namepage.html', name=name)

@app.route('/gifsandimgs')
def gifsandimgs(): 
    giflinks = ["https://myanimelist.cdn-dena.com/images/anime/11/79410.jpg", "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",                          "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",                          "https://media4.giphy.com/media/a34HjLEsKchWM/200w.gif",                          "https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif", "https://media.giphy.com/media/OmK8lulOMQ9XO/giphy.gif"]
    giflink = giflinks[randint(0, len(giflinks)-1)]
    return render_template('gifsandimgs.html', giflink=giflink)



if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0') 
