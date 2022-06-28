

from werkzeug.middleware.dispatcher import DispatcherMiddleware 
from flask import Flask
from vpc.vpc import app as VPC
from securitygroup.sec import app as SEC
from publicip.publicip import app as IP
from NIC.networkinterface import app as Nic
from vmec2.vmec2 import app as VM
from werkzeug.serving import run_simple 
app =Flask(__name__)
application = DispatcherMiddleware(VPC, {
    '/sg': SEC,
    '/publicip': IP,
    '/nic':Nic,
    '/vm': VM
})

if __name__ == '__main__':
    # run_simple(hostname='localhost', port=1400, application=application, use_debugger=True, use_evalex=True, threaded=True)
    run_simple(port=1400, hostname='0.0.0.0', application=application)
   
    