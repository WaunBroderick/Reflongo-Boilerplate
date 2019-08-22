from flask import render_template, Blueprint

reflongo_blueprint = Blueprint('reflongo',__name__)

@reflongo_blueprint.route('/')
@reflongo_blueprint.route('/reflongo')


def index():
	return render_template("index.html")


def mongo():
	return ("success")