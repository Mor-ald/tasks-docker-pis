import os
import socket
from flask import Flask

counter = 0

app = Flask(__name__)

@app.route('/about')
def hello():
    html = "<h3>Hello , I'm Alexey</h3>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/port/')
def port():
    return str(counter)

@app.route('/port/stat')
def stat():
    global counter
    counter += 1
    return str(counter)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
