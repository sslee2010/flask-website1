import os
from sqlalchemy import create_engine, text

db_conn_str = os.environ['db_connection_string']

engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select 'hello world'"))
  print(result.all())



def get_tables_name_list_in_db():
  with engine.connect() as conn:
    result = conn.execute(text("SHOW TABLES;"))
  return(result.all())
  
print("Tables in the database: ",
     get_tables_name_list_in_db())




def create_table_in_db(table_name,sql_query_str_create_table):
  if table_name in get_tables_name_list_in_db():
    return("Table",table_name,"already exists.")
  else:
    with engine.connect() as conn:
      conn.execute(text(sql_query_str_create_table))

db_create_table_posts_str = '''
  CREATE TABLE IF NOT EXISTS posts (
    id INT NOT NULL AUTO-INCREMENT,
    title VARCHAR(100) NOT NULL DEFAULT '',
    author VARCHAR(25) NOT NULL DEFAULT '',
    content VARCHAR(20000) DEFAULT '',
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
  )ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
'''
try:
  create_table_in_db("posts", db_create_table_posts_str)
except SQLAlchemyError as e:
  error = str(e.__dict__['orig'])
  print(error)

print("Tables in the database: ",
     get_tables_name_list_in_db())