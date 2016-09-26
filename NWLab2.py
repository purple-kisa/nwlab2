
# coding: utf-8

# In[ ]:

from flask import Flask, render_template, request
from random import randint
import requests

app = Flask(__name__) 

@app.route('/')
def index(): 
    stuffsaid = request.args.get('stuffsaid')
    if stuffsaid!=None:
        return render_template('stuffsaid.html', stuffsaid=stuffsaid)
    else:
        return render_template('htmltemplate.html')

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
