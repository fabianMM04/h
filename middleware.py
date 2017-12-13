from flask import Flask, jsonify,  render_template, request, redirect, url_for, send_from_directory, redirect, g, abort
from werkzeug import secure_filename
import subprocess
import os
from factory import Factory

app = Flask(__name__)

@app.route('/condor/version/<string:version>')
def version(version):
    a = Factory.get_vesion(Factory,version)
    if a != None:
        version = a.version()
        out = version
    else:
        out = "version does not exist"
    return jsonify({"version": out})

@app.route('/condor/<string:version>/status')
def condor_status(version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.status()).decode()
    else:
        out = "version does not exist"
    return jsonify({"status": out})

@app.route('/condor/<string:version>/q')
def condor_q(version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.job_Q()).decode()
    else:
        out = "version does not exist"
    return jsonify({"queue": out})


@app.route('/condor/<string:version>/ejecucion/<string:submit>')
def condor_submit(submit, version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.submit(submit)).decode()
    else:
        out = "version does not exist"
    return jsonify({"version": out})


@app.route('/condor/<string:version>/out/<string:out>')
def out(out, version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.output(out))
    else:
        out = "version does not exist"
    return jsonify({"version": out})


@app.route('/condor/<string:version>/log/<string:log>')
def log(log, version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.log(log))
    else:
        out = "version does not exist"
    return jsonify({"version": out})

app.config['UPLOAD_FOLDER'] = ''
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'xlsx', 'xls', 'csv', 'py','cpp', 'h', 'jar'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
    # Get the name of the uploaded file
        file = request.files['file']
        print("paso y el nombre es: ", file)
    # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
            return jsonify({"file": filename})
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
