from flask import Flask, render_template, url_for
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def birthday_greeting():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the static/images directory exists
    os.makedirs('static/images', exist_ok=True)
    app.run(debug=True)
