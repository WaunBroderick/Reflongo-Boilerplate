from flask import Flask
app = Flask(__name__,
 	static_folder = './public',
 	template_folder="./static")

from templates.reflongo.views import reflongo_blueprint
# register the blueprints
app.register_blueprint(reflongo_blueprint)
