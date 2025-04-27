from flask import Flask, render_template, request

app = Flask(__name__) 
app.debug = True

@app.route('/') 
@app.route('/ж')  
def all() -> 'html':
    return render_template('index.html', the_title="MAIN PAGE")

@app.route("/code_result", methods=["POST"])
def code_result() -> 'html':
    input_code = request.form["input_secret_code"]
    return render_template("code_result.html", the_code=input_code) 


if __name__ == "__main__":
    app.run(debug=True)




