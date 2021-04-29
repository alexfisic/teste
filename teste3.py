from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

   

@app.route("/<mensagem>")
def repetir_mensagem(mensagem):
     return mensagem

if __name__ == '__main__':
    app.run(debug=True)    

