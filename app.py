#%%
from flask import Flask, render_template
from views import views

#, template_folder='/templates', static_folder='/static'
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host="0.0.0.0", port=8000)

# %%