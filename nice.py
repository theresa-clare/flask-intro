from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """ 
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <a href='/hello'>Hi! This is the home page.</a>
            <a href='/practice'>Link to HTML practice</a>
        </body>
    </html>
    """
# route to display a simple web page
@app.route("/practice")
def practice():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>HTML practice</title>
        </head>
        <body>
            <p>This is practice!</p>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Favorite Food</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Jane</td>
                        <td>Pizza</td>
                    </tr>
                    <tr>
                        <td>Emily</td>
                        <td>Ice cream</td>
                    </tr>
                    <tr>
                        <td>Theresa</td>
                        <td>Cookies</td>
                    </tr>
                </tbody>
            </table>
        </body>

    </html>
    """


@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                <label>Select a compliment <select name="compliment">
                    <option value="awesome">awesome</option>
                    <option value="terrific">terrific</option>
                    <option value="fantastic">fantastic</option>
                </label>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("compliment")
    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
