from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Accounts import Accounts
 
engine = create_engine('sqlite:///Accounts.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
 
# 削除処理
row = session.query(Accounts).filter_by(Id=1).one()
session.delete(row)
session.commit()
