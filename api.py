### Building an API

from flask import Flask, render_template

app = Flask(__name__)

## Using the following...
## https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html

def factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def testing():
    return 'test'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'

@app.route('/square/<int:num>')
def f(num):
    # No conversion of x needed.
    return str(num**2)

## This one returns HTML
@app.route('/factors_raw/<int:n>')
def factors_display_raw_html(n):
    factors_list = factors(int(n))

    # First we put the stuff at the top, adding "n" in there
    html = "<h1>The factors of "+ str(n) +" are</h1>"+"\n"+"<ul>"

    # for each factor, we make a <li> item for it
    for f in factors_list:
        html += "<li>" + str(f) + "</li>"+"\n"
    html += "</ul> </body>" # the close tags at the bottom
    return html

@app.route('/factors/<int:n>')
def factors_display(n):
    return render_template("factors.html", number = n, factors = factors(n))

if __name__ == '__main__':
    app.run(host='0.0.0.0')