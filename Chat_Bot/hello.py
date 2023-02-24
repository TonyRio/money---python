from flask import Flask, request, render_template


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


### rodar o FLASK ##
app  = Flask(__name__)

portuguese_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer =ListTrainer(portuguese_bot)

trainer.train([
    "Olá",
    "Olá, estou bem e como voce esta"
])

### Rota do FLask

@app.route("/")
def home():
    return render_template("index.htmldir")

@app.route("/get")
def get_bot_response():
    userText = request.arqs.get("msg")
    return str(portuguese_bot.get_response(userText))

@app.route("/hello")
def hello():
    return "Boa Tarde !!"

if __name__ == "__main__":
    app.run()