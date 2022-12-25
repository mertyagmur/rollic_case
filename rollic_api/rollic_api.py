from flask import render_template 
from app import create_app, basedir, connex_app
from app.models import *

app = create_app()
connex_app.add_api(basedir / "swagger.yml")

@app.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)