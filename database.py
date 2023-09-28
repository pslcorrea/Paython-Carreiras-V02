from sqlalchemy import create_engine, text

string_conexao = "mysql+pymysql://laab3kezwc5s25pq2at5:pscale_pw_YMDbVWmngmKmPp8R0DtQxlG1z5cdvkLAzbbZyOblwp@aws.connect.psdb.cloud/carreira-python?charset=utf8mb4"

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

def carrega_vaga_db(id):
  with engine.connect() as conn:
    resultado = conn.execute(text(
      f"select * from vagas where id = :val;"
    ),
      {"val": id}
    )
    vaga = resultado.mappings().all()
    if len(vaga) == 0:
      return None
    else:
      return dict(vaga[0])