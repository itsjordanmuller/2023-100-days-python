from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<h1>Hello, World Heading!</h1>"
        "<p>Paragraph Text!</p>"
        "<img src='https://media3.giphy.com/media/ivCe7QYFpZcWY/giphy.gif?cid=ecf05e47ux215wc0ah5vqb2zt0ngcl5054y3j6di2l71kz76&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=300>"
    )


@app.route("/bye")
def bye():
    return "<p>Bye!</p>"


@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"<p>Hello there {name}! You are {age} years old!</p>"


if __name__ == "__main__":
    app.run(debug=True)
