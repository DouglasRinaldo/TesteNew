from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "RUNNING"


@app.route("/<cpf>")
def get_cpf(cpf):
    arquivo = open("blacklist.txt", "r")
    retorno = "FREE"
    for x in arquivo:
        x = x.replace(".", "").replace("-", "").replace("\n", "")
        if x == cpf:
            retorno = "BLOCK"
            return retorno
    return retorno


if __name__ == "__main__":
    app.run(port=5000, host='localhost')
