from flask import Flask, jsonify,  render_template, request, redirect, url_for, send_from_directory, redirect, g, abort
import subprocess
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


@app.route('/condor/<string:version/out/<string:out>')
def out(out, version):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.output(out)).decode()
    else:
        out = "version does not exist"
    return jsonify({"version": out})


@app.route('/condor/log/<string:log>')
def log(log):
    a = Factory.get_vesion(Factory, version)
    if a != None:
        out = (a.log(log)).decode()
    else:
        out = "version does not exist"
    return jsonify({"version": out})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)