from flask import Flask, request

app = Flask(__name__)







@app.route("/", methods=["POST", "GET"])
def guess():
    start = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>I will guess your number</title>
    </head>
    <body>
    <h1>Imagine number between 0 and 1000</h1>
    <form action="" method="POST">
        <input type="hidden" name="min" value="{}"></input>
        <input type="hidden" name="max" value="{}"></input>
        To start press button
        <input type="submit" value="OK">
    </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
