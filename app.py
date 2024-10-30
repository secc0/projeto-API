from flask import Flask, request, jsonify
from controller.aluno_controller import aluno_controller


app = Flask(__name__)

app.register_blueprint(aluno_controller)

@app.route('/', methods=['GET'])
def home():
    return 'Servidor ligado!'

if __name__ == '__main__':
    app.run(debug=True)
