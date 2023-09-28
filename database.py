from sqlalchemy import create_engine, text

string_conexao = "mysql+pymysql://1j8gv3lra0qbi3r6pmlu:pscale_pw_Djub0t1eJ75fxVPhCRA6RTqGu0UcHVa1NG9dLJuFibS@aws.connect.psdb.cloud/carreira-python?charset=utf8mb4"

engine = create_engine(
  string_conexao,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def carrega_vagas_db():
  with engine.connect() as conn:
    resultado = conn.execute(text('select * from vagas;'))
    vagas = []
    for vaga in resultado.all():
      vagas.append(vaga._asdict())
    return vagas
