# https://torina.top/detail/214/
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

Base = declarative_base()

class Accounts(Base):
    __tablename__ = 'Accounts'
    Id = Column(Integer, primary_key=True)
    Username = Column(String, nullable=False) 
    MailAddress = Column(String, unique=True, nullable=False)
    Password = Column(String, nullable=False)
    CreatedAt = Column(String)
    UpdatedAt = Column(String)

    AccessTokens = relationship("AccessTokens", backref="Accounts")
    SshKeys = relationship("SshKeys", backref="Accounts")
    SshConfigures = relationship("SshConfigures", backref="Accounts")
    TwoFactors = relationship("TwoFactors", backref="Accounts")
    Users = relationship("Users", backref="Accounts")
    
class AccessTokens(Base):
    __tablename__ = 'AccessTokens'
    Id = Column(Integer, primary_key=True)
    AccountId = Column(Integer, ForeignKey('Accounts.Id'), nullable=False)
    IdOnGitHub = Column(Integer, ForeignKey('SshKeys.IdOnGitHub'), unique=True, nullable=False)
    Note = Column(String)
    AccessToken = Column(String, nullable=False)
    Scopes = Column(String)
    SshKeyId = Column(Integer) # GitHubAPIでSSH鍵を設定した場合、その鍵idを保存する
    CreatedAt = Column(String)
    UpdatedAt = Column(String)

#    AccountId = relationship("Accounts", foreign_keys=[AccountId])
#    IdOnGitHub = relationship("SshKeys", foreign_keys=[IdOnGitHub])

class SshKeys(Base):
    __tablename__ = 'SshKeys'
    Id = Column(Integer, primary_key=True)
    AccountId = Column(Integer, ForeignKey('Accounts.Id'), unique=True, nullable=False)
    IdOnGitHub = Column(Integer, nullable=False)
    Title = Column(String)
    Key = Column(String)
    Verified = Column(Integer, CheckConstraint('Verified=0 or Verified=1'))
    ReadOnly = Column(Integer, CheckConstraint('ReadOnly=0 or ReadOnly=1'))
    CreatedAt = Column(String)
    
#    AccountId = relationship("Accounts", foreign_keys=[AccountId])
    AccessTokens = relationship("AccessTokens", backref="SshKeys")

class SshConfigures(Base):
    __tablename__ = 'SshConfigures'
    Id = Column(Integer, primary_key=True)
    AccountId = Column(Integer, ForeignKey('Accounts.Id'), unique=True, nullable=False)
    HostName = Column(String)
    PrivateKeyFilePath = Column(String)
    PublicKeyFilePath = Column(String)
    Type = Column(String)
    Bits = Column(Integer)
    Passphrase = Column(String)
    
#    AccountId = relationship("Accounts", foreign_keys=[AccountId])

class TwoFactors(Base):
    __tablename__ = 'TwoFactors'
    Id = Column(Integer, primary_key=True)
    AccountId = Column(Integer, ForeignKey('Accounts.Id'), nullable=False)
    Secret = Column(String, nullable=False)
    RecoveryCodes = Column(String)
    RecoveryCodesExpirationDate = Column(String)
    
#    AccountId = relationship("Accounts", foreign_keys=[AccountId])

class Users(Base):
    __tablename__ = 'Users'
    Id = Column(Integer, primary_key=True)
    AccountId = Column(Integer, ForeignKey('Accounts.Id'), unique=True, nullable=False)
    Blog = Column(String)
    Company = Column(String)
    Location = Column(String)
    Hireable = Column(Integer, CheckConstraint('Hireable=0 or Hireable=1'))
    Bio = Column(String)
    
#    AccountId = relationship("Accounts", foreign_keys=[AccountId])

 
if __name__ == "__main__":
    engine = create_engine('sqlite:///Accounts.sqlite3', echo=True)
    Base.metadata.create_all(engine)  # テーブル作成
