from flask import Flask

app = Flask(__name__)

# signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return 'This is the homepage'

if __name__ == '__main__':
    app.run(debug= True)
