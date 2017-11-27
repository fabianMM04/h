from wms import Wms

class Htcondor:
    def status(self):
        interface = Wms()
        condorStatus = interface.status()
        return condorStatus

    def job_Q(self):
        interface = Wms()
        condorQ = interface.job_Q()
        return condorQ

    def log(self, log):
        interface = Wms()
        condorLog = interface.log(log)
        return condorLog

    def output(self, output):
        interface = Wms()
        condorOutput = interface.output(output)
        return condorOutput

    def submit(self, submit):
        interface = Wms()
        condorSubmit = interface.submit(submit)
        return condorSubmit

    def version(self):
        interface = Wms()
        condorVersion = interface.version()
        return condorVersion


#print(Htcondor.version(Htcondor))

