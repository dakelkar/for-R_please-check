from flask import Flask
from flask import Flask, render_template
import os
#working = "D:\python36\Lib\site-packages\flask\FlaskApp\app.py"
#app = Flask(__name__, template_folder = working)
app = Flask(__name__)
@app.route("/")
def main():
	return "Welcome"
	#return render_template('index.html')
if __name__ == "__main__":
    app.run(host = 'localhost')
