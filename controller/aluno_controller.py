from flask import Flask, request, jsonify, Blueprint
from models.aluno import Aluno


aluno_controller = Blueprint('aluno_controller', __name__)

alunos = [
    {'id': 1, 'nome': 'João', 'idade': 22},
    {'id': 2, 'nome': 'Jhonny', 'idade': 20}
]

@aluno_controller.route('/criar/alunos', methods=['POST'])
def criar_alunos():
    data = request.json
    novo_aluno = Aluno(id=len(alunos)+1, nome=data['nome'],idade=data['idade'])

    alunos.append(novo_aluno)
    return jsonify({'message': 'Aluno criado com sucesso!', 'aluno': novo_aluno.to_dict()}), 201