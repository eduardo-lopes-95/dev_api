from flask import Flask, json, jsonify, request, response
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Eduardo',
        'linguagens': '[Python, Java]',
        'frameworks': '[Django, Flask, SpringBoot]'
    },
    {
        'nome': 'Lopes',
        'linguagens': '[Java]',
        'frameworks': '[SpringBoot]'
    }
]


@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não exite'
            response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)
        except Exception:
            mensagem = f'Error desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro deletado'})


app.route('/dev/', methods=['POST', 'GET'])


def lista_desenvolvedores():
    pass


if __name__ == "__main__":
    app.run(debug=True)
