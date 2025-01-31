#%%
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False , host="0.0.0.0", port=8000)


# @app.route("/")
# def hello_world():
#     return "<p>Home Page</p>"
# app.run (host="0.0.0.0", port=8000)