
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Are you there, world? It's me, Ducky!"

@app.route("/penguins")
def penguins():
    return "Penguins are cute!"

@app.route("/monkeys")
def monkeys():
    return "Monkeys are the best!"

@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    return f"The {adjective} {noun} looked in the mirror and saw quite the {adjective} {noun}."

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1)*int(number2)}."
    return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route("/sayntimes/<word>/<n>")
def say_n_times(word, n):
    if n.isdigit():
        return " ".join([word] * int(n))
    return "Invalid inputs. Please try again by entering a word and a number!"

@app.route("/reverse/<word>")
def reverse(word):
    return word[::-1]

@app.route("/strangecaps/<word>")
def strangecaps(word):
    new_word = ""
    for i, c in enumerate(word.lower()):
        new_word += c if i % 2 == 0 else c.upper()
    return new_word

@app.route("/dicegame")
def dicegame():
    roll = randint(0,6)
    result = "won" if roll == 6 else "lost"
    return f"You rolled a {roll}. You {result}!"

if __name__ == "__main__":
    app.run(debug=True)