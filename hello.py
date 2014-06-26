# This runs on
# http://port-10080.q4ldrk5f967jh5migdgvy2380crw9udis9nzpuzfg1yeewmi.box.codeanywhere.com/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)