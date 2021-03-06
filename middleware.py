from flask import Flask, jsonify,  render_template, request, redirect, url_for, send_from_directory, send_file, redirect, g, abort
from werkzeug import secure_filename
import subprocess
import os, shutil
import wget
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


@app.route('/condor/<string:version>/ejecucion/<string:path>/<string:path2>/<string:submit>')
def condor_submit(submit, version, path, path2):
    os.chdir('/opt/env/h/'+path+"/"+path2)
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
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'xlsx', 'xls', 'csv', 'py','cpp', 'h', 'jar', 'jpg', 'jpeg', 'submit'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Route that will process the file upload
@app.route('/upload/<string:path1>/<string:path2>', methods=['POST'])
def upload(path1, path2):
  # Get the name of the uploaded files
  path = path1+'/'+path2
  uploaded_files = request.files.getlist("file[]")
  print("nombre upload: ", uploaded_files)
  filenames = []
  for file in uploaded_files:
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
      # Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)
      # Move the file form the temporal folder to the upload
      # folder we setup
      if not os.path.exists('/opt/env/h/'+path):
        os.makedirs('/opt/env/h/'+path)
        print("crea carpeta", flush=True)
      file.save(os.path.join('/opt/env/h/'+path,filename))
      # Save the filename into a list, we'll use it later
      filenames.append(filename)
      # Redirect the user to the uploaded_file route, which
      # will basicaly show on the browser the uploaded file
  # Load an html page with a link to each uploaded file
  return jsonify({"file": filenames, "path": path})

@app.route('/showFile/<string:path>/<string:path2>')
def uploaded_file(path, path2):
    print(path,"/", path2)
    if not os.path.exists('/opt/env/h/'+path+"/"+path2):
        return jsonify({"files": "File not found"})
    else:
        return jsonify({"files": os.listdir('/opt/env/h/'+path+"/"+path2)})

@app.route('/delete/<string:path>/<string:path2>')
def delete_dir(path, path2):
    print(path,"/", path2)
    if os.path.isdir('/opt/env/h/'+path+"/"+path2):
        shutil.rmtree('/opt/env/h/'+path+"/"+path2)
        return jsonify({"directory": "Directory deleted "})
    else:
        return jsonify({"directory": "Directory not found"})

@app.route('/delete/<string:path>/<string:path2>/<string:filename>')
def delete_file(path, path2, filename):
    print(path,"/", path2,"/", filename)
    if os.path.exists('/opt/env/h/'+path+"/"+path2+"/"+filename):
        os.remove('/opt/env/h/'+path+"/"+path2+"/"+filename)
        return jsonify({"file": "File deleted "})
    else:
        return jsonify({"file": "File not found"})


@app.route('/download/<string:path>/<string:path2>/<string:filename>', methods=['GET', 'POST'])
def hola(path, path2, filename):
    if request.method == 'POST':
        print('/opt/env/h/'+path+"/"+path2+"/"+filename)
        uploads = '/opt/env/h/'+path+"/"+path2+"/"+filename
        print("upload:", uploads)
        return send_file(uploads, as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
