from flask import Flask, request

app = Flask(__name__)







@app.route("/", methods=["POST", "GET"])
def guess():
    #main page that you will see using method get
    main_page = """
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
    gues = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Guess The Number</title>
        </head>
        <body>
         <form action="/" method="POST">
            <label>
            <h1>Is it {guess}?</h1>

            <INPUT TYPE="submit" name="choice" Value="small">
            <INPUT TYPE="submit" name="choice" Value="big">
            <INPUT TYPE="submit" name="choice" Value="win">
            <input type="hidden" name="min" value="{min}">
            <input type="hidden" name="max" value="{max}">
            <input type="hidden" name="guess" value="{guess}">
            </label>
        </form>
        </body>
        </html>
        """
    if request.method == "GET":
        return main_page.format(0, 1000)
    else:
        return gues

if __name__ == "__main__":
    app.run(debug=True)