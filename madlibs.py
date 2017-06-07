"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Determine if the user wants to play a game."""

    player = request.args.get("person")
    wants_to_play = request.args.get("playgamebool")

    if wants_to_play == "True":
        return render_template("game.html",
                            user=player)

    else:
        return render_template("goodbye.html",
                            person=player)


@app.route('/madlib')
def show_madlib():
    """Show resulting madlib based on user input."""

    player = request.args.get("user")
    person = request.args.get("chooseperson")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adj")

    return render_template("madlib.html",
                        user=player,
                        person=person,
                        color=color,
                        noun=noun,
                        adj=adj)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
