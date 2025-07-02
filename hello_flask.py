from flask import Flask, render_template, request, url_for
import wiki
import badges
import database

def log_request(log_message, req) -> None:
    with open("logs.txt", "a") as logs:
        print(f"{log_message}: {req}", file=logs) 
        

app = Flask(__name__, static_folder='static') 
app.debug = True

@app.route('/')  
@app.route('/home', methods=["POST", "GET"]) 
def all() -> 'html':
    return render_template('main-page.html', the_title="Главная страница")

@app.route('/authorized', methods=["POST"]) 
def authorized() -> 'str':
    username = request.form["username"]
    user_password = request.form["password"]
    db_output = database.is_user_authorized(username, user_password)
    if db_output:
        return f"{username}, Вы авторизованы!!"
    else:
        return render_template('auth.html', the_title="Authorization")


@app.route("/pins", methods=["POST", "GET"])
def pins() -> 'html':
    log_request("User enter code:", 0) 
    return render_template("pins.html", the_title="Мои пины")


@app.route("/films", methods=["POST", "GET"])
def films() -> "html":
    return render_template("films.html", the_title="Мои любимые фильмы", links=wiki.parse_film_info() )


@app.route("/books", methods=["POST", "GET"])
def books() -> "html":
    return render_template("books.html", the_title="Книги которые я прочел")

@app.route("/graphics", methods=["POST", "GET"])
def graphics() -> "html":
    return render_template("graphics.html", the_title="Graphics", urls=badges.get_badges_url() )


@app.route("/viewlog", methods=["POST", "GET"])
def viewlog() -> str:
    with open("logs.txt") as log:
        contents = log.read()   
    return contents

if __name__ == "__main__":
    app.run(debug=True)
   



