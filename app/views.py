"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
"""
import os
from flask import Blueprint, render_template, request, jsonify, send_from_directory, current_app
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from .forms import MovieForm
from .models import Movie
from . import db

# Create Blueprint
main = Blueprint('main', __name__)

###
# Routing for your application.
###

@main.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@main.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@main.route('/api/v1/posters/<filename>', methods=['GET'])
def get_poster(filename):
    # Using absolute path from current_app.root_path
    upload_folder = os.path.join(current_app.root_path, 'uploads')
    return send_from_directory(upload_folder, filename)

@main.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    movies_list = []
    for movie in movies:
        movies_list.append({
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'poster': f'/api/v1/posters/{movie.poster}'
        })
    return jsonify({'movies': movies_list})

@main.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        # 1. Secure filename
        filename = secure_filename(poster.filename)

        # 2. Define absolute path to uploads folder
        upload_folder = os.path.join(current_app.root_path, 'uploads')

        # 3. Create directory if it doesn't exist
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # 4. Save file
        filepath = os.path.join(upload_folder, filename)
        poster.save(filepath)

        # 5. Save movie to database
        movie = Movie(
            title=title,
            description=description,
            poster=filename
        )

        db.session.add(movie)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201

    # If validation fails
    errors = form_errors(form)
    return jsonify({"errors": errors}), 400


###
# Helper Functions
###

def form_errors(form):
    """Collects form errors"""
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            )
            error_messages.append(message)
    return error_messages

@main.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return send_from_directory('static', file_dot_text)

@main.after_request
def add_header(response):
    """
    Add headers to force latest IE rendering engine or Chrome Frame
    and prevent caching.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@main.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404