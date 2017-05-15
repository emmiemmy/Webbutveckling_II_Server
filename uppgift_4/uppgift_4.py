from flask import Flask, render_template, url_for

app = Flask(__name__)


# StartPage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Contacts page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Movies page
@app.route('/movies')
def movies():
    movies = \
        [
            {
                "Title": "The Revenant",
                "Plot": "A frontiersman on a fur trading expedition in the 1820s fights for "
                        "survival after being mauled by a bear and left for dead by members of "
                        "his own hunting team."
            },
            {
                "Title": "Everest",
                "Plot": "A climbing expedition on Mt. Everest is devastated by a severe snow storm."
            },
            {
                "Title": "Heat",
                "Plot": "A group of professional bank robbers start to feel the heat "
                        "from police when they unknowingly leave a clue at their latest heist."
            },
            {
                "Title": "The Wave",
                "Plot": "A high school teacher's experiment to demonstrate to his students what "
                        "life is like under a dictatorship spins horribly out of control when he "
                        "forms a social unit with a life of its own."
            }

        ]
    return render_template('movies.html', movies=movies)


# Greeting page
@app.route('/hello/<name>')
@app.route('/hello')
def greeting(name='user'):
    return render_template('greeting.html', name=name)


# Doesn't exist page
@app.errorhandler(404)
def doesntexist(error):
    return render_template("doesntexist.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
