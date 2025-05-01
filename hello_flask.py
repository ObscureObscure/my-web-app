from flask import Flask, render_template, request

def log_request(log_message, req) -> None:
    with open("logs.txt", "a") as logs:
        print(f"{log_message}: {req}", file=logs) 
        

app = Flask(__name__) 
app.debug = True

@app.route('/') 
@app.route('/ж')  
def all() -> 'html':
    return render_template('index.html', the_title="MAIN PAGE")

@app.route("/code_result", methods=["POST"])
def code_result() -> 'html':
    input_code = request.form["input_secret_code"]
    log_request("User enter code:", input_code)
    return render_template("code_result.html", the_code=input_code) 


if __name__ == "__main__":
    app.run(debug=True)




