from flask import Flask
app = Flask(__name__)

from datetime import datetime

import threading
import time
import subprocess

# from threading import Thread as Zeka

params = {
    'jacina': 0.4,
    'vreme': 11*3600 + 8*60 + 25, # sekunde
    'trajanje': 20, # sekunde
    'tip': 'zvuk',
    'sablon': 'beskonacno',
}

def calc_time():
    h = int(params['vreme']/3600)
    m = (params['vreme'] % 3600) / 60
    s = params['vreme'] % 60
    return (h, m, s)

@app.route("/")
def index():
    h, m, s = calc_time()
    return r'''
<pre>
jacina: %.0f%%
vreme : %d:%02d:%02d
tip   : %s
sablon: %s
</pre>
''' % (params['jacina']*100, h, m, s, 
       params['tip'], params['sablon'])

# @app.route("/page2/<param>")
# def page2tttt(param):
#     return 'ovo je test stranica 2: ' + param

def current_ts():
    d = datetime.now()
    t = d.time()
    ts = t.hour*3600 + t.minute*60 + t.second
    return ts

def alarm_should_be_on():
    ts = current_ts()
    return params['vreme'] <= ts < params['vreme'] + params['trajanje']

proc = None

def start_alarm():
    global proc
    proc = subprocess.Popen(['./play.sh'])

def stop_alarm():
    global proc
    proc.kill()
    proc = None

def alarm_activator():
    while True:
        should = alarm_should_be_on()
        active = proc != None

        print (should, active)
 
        # if   (should, active) == (False, False):
        #     pass
        # elif (should, active) == (False, True):
        #     # stop
        # elif (should, active) == (True,  False):
        #     # start
        # elif (should, active) == (True,  True):
        #     pass

        if not active and should:
            start_alarm()
        elif active and not should:
            stop_alarm()

        time.sleep(1.0)

if __name__ == "__main__":
    params['vreme'] = current_ts() + 10

    thr = threading.Thread(target=alarm_activator)
    thr.start()

    app.run(debug=False)
