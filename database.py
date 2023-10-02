import os

from sqlalchemy import create_engine, text

string_conexao = os.environ["DB_CONEXAO_STRING"]
engine = create_engine(string_conexao,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def carrega_vagas_db():
  with engine.connect() as conn:
    resultado = conn.execute(text('select * from vagas;'))
    vagas = []
    for vaga in resultado.all():
      vagas.append(vaga._asdict())
    return vagas


def carrega_vaga_db(id):
  with engine.connect() as conn:
    resultado = conn.execute(text(f"select * from vagas where id = :val;"),
                             {"val": id})
    vaga = resultado.mappings().all()
    if len(vaga) == 0:
      return None
    else:
      return dict(vaga[0])


def adiciona_inscricao(id_vaga, dados):
  with engine.connect() as conn:
    query = text(
        f"INSERT INTO inscricoes(vaga_id,nome,email,linkedin,experiencia) VALUES(:vaga_id,:nome,:email,:linkedin,:experiencia)"
    )
    conn.execute(
        query, {
            'vaga_id': id_vaga,
            'nome': dados['nome'],
            'email': dados['email'],
            'linkedin': dados['linkedin'],
            'experiencia': dados['experiencia']
        })
