from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'telegram_user'
    id = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)

    def __repr__(self) -> str:
        return f'User(id={self.id}, tg_id={self.tg_id})'

class Product(Base):
    '''
    description pack,
    price in roubles,
    content - link on pack
    '''
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    description = Column(Text)
    price = Column(BigInteger)
    content = Column(Text)

    def __repr__(self) -> str:
        return f'Product(id={self.id}, description={self.description}, price={self.price})'

class Bill(Base):
    '''
    table for check bill status
    '''
    __tablename__ = "bill"
    id = Column(BigInteger, primary_key=True)
    tg_id = Column(BigInteger)
    bill = Column(Text)
    content = Column(Text)

    def __repr__(self) -> str:
        return f'Bill(id={self.id}, tg_id={self.tg_id}, bill={self.bill})'
