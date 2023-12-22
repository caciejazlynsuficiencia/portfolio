from flask import Flask, render_template


app = Flask(Cacie Suficiencia)

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

if Cacie Suficiencia == "__main__":
	app.run(debug=True, port="8080", host="0.0.0.0")