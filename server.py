import os
import platform
from flask import Flask
from cfenv import AppEnv


app = Flask(__name__)
env = AppEnv()

@app.route('/')
def hello():
    
    return platform.system()+ platform.version()

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
