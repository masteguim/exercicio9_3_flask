from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello World!</h1>
    <p>Exercicio 9.3 - Flask e Nuvem</p>
    <p>Aplicacao Flask funcionando!</p>
    """


if __name__ == "__main__":
    app.run(debug=True)