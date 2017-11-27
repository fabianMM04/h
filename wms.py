import subprocess
import json


class Wms:
    def status(self):
        cmd = ["condor_status"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def job_Q(self):
        cmd = ["condor_q"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def log(self, log):
        file = open(log, "r")
        file_r = file.read()
        return file_r

    def output(self, output):
        file = open(output, "r")
        file_r = file.read()
        return file_r

    def submit(self, submit):
        cmd = ["condor_submit", submit]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def version(self):
        v = "8.0.5"
        return v

# obj2 = Wms()
# print(obj2.version())
