from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "This is my first blog."

@app.route('/blog')
def get_blog():
    url_blog = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url_blog)
    all_blog = response.json()
    n = len(all_blog)
    return render_template('index.html', posts=all_blog, n=n)


@app.route('/post/<num>')
def get_post(num):
    url_blog = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url_blog)
    all_post = response.json()[int(num)-1]
    return render_template('post.html', posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
