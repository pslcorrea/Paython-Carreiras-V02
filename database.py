from sqlalchemy import create_engine, text
import os

string_conexao = os.environ['db_conexao_string']
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
