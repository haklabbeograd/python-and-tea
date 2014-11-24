from flask import Flask
app = Flask(__name__)

from datetime import datetime

params = {
    'jacina': 0.4,
    'vreme': 11*3600 + 8*60 + 25,
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

def alarm_is_on():
    d = datetime.now()
    t = d.time()
    return t.hour*3600 + t.minute*60 + t.second >= params['vreme']

if __name__ == "__main__":
    app.run()
