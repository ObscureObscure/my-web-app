from flask import Flask, render_template

app = Flask(__name__) 
app.debug = True

@app.route('/') 
def hello() -> str: 
    return 'Hello world from Flask!' 

@app.route('/all') 
def all() -> 'html':
    return render_template('index2.html', the_title="privet")#.encode("utf-8")

app.run(debug=True)



