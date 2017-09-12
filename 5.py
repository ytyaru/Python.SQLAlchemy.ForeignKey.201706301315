from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Accounts import Accounts
 
engine = create_engine('sqlite:///Accounts.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
 
for row in session.query(Accounts).all():
    print(row.Id, row.Username, row.MailAddress, row.Password, row.CreatedAt, row.UpdatedAt)
