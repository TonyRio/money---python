from hello import app
from flask import Flask
def teste_hello():
    response = app.test_client().get("/hello")

    assert response.status_code == 200
    assert response.data == b"Hi There"

