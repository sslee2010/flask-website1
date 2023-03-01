from sqlalchemy import create_engine, text

db_conn_str = "mysql+pymysql://4hhc0b1t4qqxw0qd0g97:pscale_pw_SwQxiMlwILxQXYBOmU7oPNnamiKKwzkO4T0VDGLtyaK@aws-ap-southeast-2.connect.psdb.cloud/flask1?charset=utf8mb4"

engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select 'hello world'"))
  print(result.all())