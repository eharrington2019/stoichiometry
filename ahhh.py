import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text



engine = create_engine('sqlite:///mydb.db', echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)

  def makeRecord(name, date):
      statement = text("INSERT INTO users (name, date)"
      " values ('" + name +  "', '" + date + "')")

  statement = text("INSERT INTO users (coefficient, element)"
  " values (4, 'He')")
  conn.execute(statement)

  statement = text("INSERT INTO users (coefficient, element)"
  " values (3, 'C')")
  conn.execute(statement)

#  statement = text("INSERT INTO pets (name, age, userid)"
 # " values ('Josie', 4, 1)")
  #conn.execute(statement)

  #statement = text("INSERT INTO pets (name, age, userid)"
  #" values ('Bobbi', 24, 2)")
  #conn.execute(statement)

  #statement = text("INSERT INTO pets (name, age, userid)"
  #" values ('Bubbles', 14, 2)")
  #conn.execute(statement)

  query = text("SELECT * from users")
  result = conn.execute(query).fetchall()
  print(result)






def createTables(metadata, conn):
  users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('coefficient', Integer),
    Column('element', String)
    #Column('age', Integer),
    #Column('fullname', String))


  #pets = Table('pets', metadata,
    #Column('id', Integer, primary_key=True),
    #Column('userId', Integer),
    #Column('name', String),
    #Column('age', Integer),
  )
  metadata.create_all(engine)

main()
