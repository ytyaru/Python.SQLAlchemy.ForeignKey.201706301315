from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Accounts import Accounts
 
engine = create_engine('sqlite:///Accounts.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
 
#ed_user = Accounts(Username='ed', MailAddress='Ed Jones', Password='edspassword', CreatedAt='', UpdatedAt='')
user0 = Accounts(Username='user0', MailAddress='mail0', Password='pass0')
session.add(user0)
 
session.add_all([
    Accounts(Username='user1', MailAddress='mail1', Password='pass1'),
    Accounts(Username='user2', MailAddress='mail2', Password='pass2'),
    Accounts(Username='user3', MailAddress='mail3', Password='pass3')])
 
session.commit()
