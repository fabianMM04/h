from htcondor8_0_5 import Htcondor

class Factory:

    def get_vesion(self,v):

        if v == "8.0.5":
            htc8_0_5 = Htcondor()
            return htc8_0_5

        else:
            print("Invalid version", flush=True)


a = Factory.get_vesion(Factory,"8.0.5")
d_a = a.submit("test.submit")
s = d_a.decode()
print((s))
