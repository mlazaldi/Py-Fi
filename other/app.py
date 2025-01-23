#%%
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>you need to Drink WAAAAY more Coffee!</p>"


app.run (host="0.0.0.0", port=80)