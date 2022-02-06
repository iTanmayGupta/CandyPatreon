from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():	
	return render_template('index.html')

@app.route("/treat")
def treat():	
	return render_template('treat.html')

@app.route("/home")
def home():	
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)
