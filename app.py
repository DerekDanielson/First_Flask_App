from flask import Flask, request

app = Flask(__name__)

@app.route('/') #HOMEPAGE(ROOT)
def home_page():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the Home page</p>
            <a href='/hello'>Go to hello page</a>
            <br>
            <a href='/goodbye'>Go to goodbye page</a>
        </body>
    </html>
    """
    return html

@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the Hello page</p>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_bye():
    return "GOODBYE!!!"

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>"
# 127.0.0.1:5000/searc?term=Dogs&sort=New


#POST Requests
@app.route("/post", methods=["POST"])
def post_demo():
    return "YOU MADE A POST REQUEST!"


@app.route("/add-comment")
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method="POST">
            <input type='text' placeholder='comment' name='comment'/>
            <input type='text' placeholder='username' name='username'/>
            <button>Submit</button>
        </form>
    """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment=request.form["comment"]
    username = request.form["username"]
    print(request.form)
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</ul>
    </ul>
    """


# PATH VARIABLES
@app.route('/r/<subreddit>')
def show_subreddit():
    return "THIS IS A SUBREDDIT"




































