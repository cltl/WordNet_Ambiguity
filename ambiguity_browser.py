from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

from ambiguity import Ambiguity


@app.route('/',methods=['GET'])
def main_page():
    """
    Function to display the main page. This is the first thing you see when you
    load the website.
    """
    get_or_post = request.method
    return render_template('index.html')

@app.route('/search/', methods=['POST'])
def search():
    """
    Search function. Is called when the search form is submitted.
    """
    text = request.form['text']

    ambiguity_string = Ambiguity(text).the_polysemy_string

    return render_template('index.html',
                           text = ambiguity_string)

if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(host='130.37.53.15', port=5001)
