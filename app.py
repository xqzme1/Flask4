from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/company')
def company():
    return render_template('company.html')


if __name__ == '__main__':
    app.run(debug=True)
