from flask import Flask, render_template, jsonify
from database import carrega_vagas_db, carrega_vaga_db

app = Flask(__name__)


@app.route('/')
def home():
    vagas = carrega_vagas_db()
    return render_template('home.html', vagas=vagas)


@app.route('/vagas')
def lista_vagas():
    vagas = carrega_vagas_db()
    return jsonify(vagas)


@app.route('/vaga/<id>')
def mostra_vaga(id):
    vaga = carrega_vaga_db(id)
    if not vaga:
        return 'Not Found', 404
    return render_template('detalhe_vaga.html', vaga=vaga)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
