from flask import Flask

### rodar o FLASK ##
app  = Flask(__name__)


### Rota do FLask

@app.route("/hello")
def hello():
    return "Hello World !!"

if __name__ == "__main__":
    app.run()