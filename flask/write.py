from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my_form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    data=request.form['text']
    with open("/data/abc.txt","a") as f:
        f.write("{}<br>".format(data))
    return data+" written into text file"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
