from flask import Flask, render_template, url_for
lagoa = Flask(__name__)


@lagoa.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
    lagoa.run(host='0.0.0.0')
