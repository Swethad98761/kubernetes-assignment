#import redis
from flask import Flask, request, render_template
import os.path
app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)


'''def my_form():
    return render_template('my_form.html')'''

#@app.route('/', methods=['POST'])
@app.route('/')
def log():
    #data=request.form['text']
    if os.path.isfile("/data/abc.txt")==False:
       return "sorry"    
    with open("/data/abc.txt","r") as f:
        content=f.read()
    return render_template("template.html", content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500, debug=True)
