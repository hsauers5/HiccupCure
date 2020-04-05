from flask import Flask, render_template

# Create the application instance
app = Flask(__name__, static_folder='.', static_url_path='', template_folder='')


# Create a URL route in our Flask application for "/"
@app.route('/')
def home():
    return render_template("/index.html")


# runs on port 5000 by default.
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
