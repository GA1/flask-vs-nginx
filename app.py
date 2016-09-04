from flask import Flask
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def getMainPage():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
