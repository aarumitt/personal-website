import sys

# Check Python version
required_version = (3, 7)
if sys.version_info < required_version:
    sys.exit(f"This application requires Python {required_version[0]}.{required_version[1]} or higher. You are running Python {sys.version_info.major}.{sys.version_info.minor}.")

from flask import Flask, render_template, request, redirect, url_for, flash
from DAL import *
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Configuration for file uploads
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    # Get projects from database
    projectList = getAllProjects()
    return render_template('projects.html', projects=projectList)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
    if request.method == 'GET':
        # Display form and existing projects table
        projectList = getAllProjects()
        return render_template('addproject.html', projects=projectList)
    
    elif request.method == 'POST':
        # Get form data
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        
        # Validate required fields
        if not title or not description:
            flash('Title and description are required!', 'error')
            projectList = getAllProjects()
            return render_template('addproject.html', projects=projectList)
        
        # Handle file upload
        imageFileName = ''
        if 'imageFile' in request.files:
            file = request.files['imageFile']
            if file and file.filename and allowed_file(file.filename):
                # Secure the filename and save the file
                filename = secure_filename(file.filename)
                # Add timestamp to avoid filename conflicts
                import time
                timestamp = str(int(time.time()))
                name, ext = os.path.splitext(filename)
                filename = f"{name}_{timestamp}{ext}"
                
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                imageFileName = filename
                flash('Project added successfully!', 'success')
            elif file and file.filename:
                flash('Invalid file type. Please upload PNG, JPG, JPEG, GIF, or WebP images only.', 'error')
                projectList = getAllProjects()
                return render_template('addproject.html', projects=projectList)
            else:
                flash('No image file selected.', 'error')
                projectList = getAllProjects()
                return render_template('addproject.html', projects=projectList)
        else:
            flash('Please select an image file.', 'error')
            projectList = getAllProjects()
            return render_template('addproject.html', projects=projectList)
        
        # Save project to database
        saveProjectDB(title, description, imageFileName)
        
        # Get updated project list and display page
        projectList = getAllProjects()
        return render_template('addproject.html', projects=projectList)
    
    else:
        return render_template('addproject.html', projects=[])

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        # Handle form submission and redirect to thank you page
        return render_template('thankyou.html')
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)
