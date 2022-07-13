import os
import platform
from flask import Flask
from cfenv import AppEnv


app = Flask(__name__)
env = AppEnv()

@app.route('/')
def hello():
    
    #return platform.system()+ platform.version()
    print(platform.system())
    text_file = open("test.txt", "r") 
    #read whole file to a string
    data = text_file.read() 
    #close file
    text_file.close()
    return data
@app.route('/info')
def info():    
   #return platform.system()+ platform.version()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
