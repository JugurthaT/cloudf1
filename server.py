import os
import platform
from flask import Flask
from cfenv import AppEnv
from hdbcli import dbapi

app = Flask(__name__)
env = AppEnv()

hana_service = 'hanatrial'
hana = env.get_service(label=hana_service)
print("********************************************")
print(hana,flush=True)
@app.route('/')
def allo():
    
    #return platform.system()+ platform.version()
    print(platform.system())
    text_file = open("test.txt", "r") 
    #read whole file to a string
    data = text_file.read() 
    #close file
    text_file.close()
    return data
@app.route('/db')
def  hello():
    conn = dbapi.connect(address=hana.credentials['host'],
                         port=int(hana.credentials['port']),
                         user=hana.credentials['user'],
                         password=hana.credentials['password'],
                         encrypt='true',
                         sslTrustStore=hana.credentials['certificate'])

    cursor = conn.cursor()
    cursor.execute("select * from DUMMY")
    ro = cursor.fetchone()
    cursor.close()
    conn.close()
    return "Current version is: " + str(ro)
@app.route('/info')
def info():    
   return platform.system()+ platform.version()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
