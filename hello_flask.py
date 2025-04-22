from flask import Flask, render_template

app = Flask(__name__) 
app.debug = True

@app.route('/') 
def hello() -> str: 
    return 'Hello world from Flask!' 

@app.route('/all') 
def all() -> 'html':
    return render_template('index.html', the_title="MAIN PAGE")

@app.route("/code_result", methods=["POST"])
def code_result() -> 'html':
    return render_template("code_result.html", the_code="swag")



app.run(debug=True)




