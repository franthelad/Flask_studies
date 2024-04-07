from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'The current method is %s' % request.method

@app.route('/bacon', methods= ['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'

if __name__ == '__main__':
    app.run(debug= True)
