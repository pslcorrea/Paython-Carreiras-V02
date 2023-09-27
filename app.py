from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [
    {
        'id': 1,
        'titulo': 'Analista de Dados',
        'localidade': 'SC, Brasil',
        'salario': 'R$ 5.000'
    },
    {
        'id': 2,
        'titulo': 'Analista de Segurança de Dados',
        'localidade': 'SP, Brasil',
        'salario': 'R$ 15.000'
    },
    {
        'id': 3,
        'titulo': 'Analista de BI',
        'localidade': 'RJ, Brasil',
        'salario': 'R$ 8.000'
    },
    {
        'id': 4,
        'titulo': 'Analista de Projetos',
        'localidade': 'MG, Brasil',
        'salario': 'R$ 9.000'
    },
    {
        'id': 5,
        'titulo': 'Analista de Storage NetApp',
        'localidade': 'SP, Brasil',
        'salario': 'R$ 18.000'
    },
]


@app.route('/')
def home():
  return render_template('home.html', vagas=VAGAS)


@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
