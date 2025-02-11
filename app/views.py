import os
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app # imported our created app

# decorated route index. 
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
			return render_template('index.html', filename=filename)
	return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOADS_FOLDER'], filename, as_attachment=True)


@app.route('/uploads', methods=['GET'])
def uploads():
	f = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		f.extend(filenames)

	return render_template('index.html', filelist=f)
