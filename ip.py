
from flask import render_template
from flask import Flask,redirect,session,url_for
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not 'username' in session:
        return redirect(url_for('logon'))

    lines = []
    try:
        file = open('ipset.ruls','r')
        lines = file.readlines()
    except:
        pass

    lines = [ x.split(' ')[2].strip() for x in lines]
    return render_template( 'index.html',ips ='\n'.join( lines) )
    #return 'Hello World!'

@app.route('/save', methods=['POST'])
@app.route('/save/<ips>', methods=['POST'])
def save(ips=None):
    if not 'username' in session:
        return redirect(url_for('logon')) 

    ips = request.form['ips'].split('\n')
    #ips = [ 'add banthis ' + x for x in ips if len(x)>0]
    ips = [x for x in sorted( set( ips ) ) if len(x)>0]
    ipsToSave = ['add banthis ' + x for x in ips ]
    #txtToSave = [ 'add banthis ' + x for x in ips if len(x)>0 ]
    txt = '\n'.join( ipsToSave )
    
    f = open('ipset.ruls','w') 
    f.write( txt )
    f.close()
    os.system('ipset flush')
    os.system('ipset restore -f ipset.ruls')
    return render_template( 'index.html',ips ='\n'.join( ips))

@app.route('/logon',methods=['POST','GET'])
def logon():
    if request.method == 'POST':
        if request.form['name']=='admin' and request.form['password']=='xlz2015':
            session['username'] = 'admin'
            return redirect(url_for('index'))

    return render_template( 'logon.html')


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RTdfsd'
if __name__ == '__main__':
    app.run( host='0.0.0.0',debug=True )
