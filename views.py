#%%
from flask      import Blueprint, render_template
from templates  import *

views    =   Blueprint(__name__, "views")


@views.route("/",endpoint='one')
def home():
    return render_template("index.html")

# %%