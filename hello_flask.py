from flask import Flask, render_template, request, url_for

def log_request(log_message, req) -> None:
    with open("logs.txt", "a") as logs:
        print(f"{log_message}: {req}", file=logs) 
        

app = Flask(__name__, static_folder='static') 
app.debug = True

@app.route('/')  
@app.route('/home', methods=["POST", "GET"]) 
def all() -> 'html':
    return render_template('index.html', the_title="ГЛАВНАЯ СТРАНЦА")

@app.route("/code_result", methods=["POST"])
def code_result() -> 'html':
    #input_code = request.form["input_secret_code"]

    log_request("User enter code:", 0) #, input_code
    return render_template("code_result.html", the_title="МОИ ПИНЫ") #, the_code=input_code

@app.route("/films", methods=["POST"])
def films() -> "html":
    return render_template("films.html", the_title="МОИ ЛЮБИМЫЕ ФИЛЬМЫ")

@app.route("/viewlog")
def viewlog() -> str:
    with open("logs.txt") as log:
        contents = log.read()   

    return contents


if __name__ == "__main__":
    app.run(debug=True)
   



