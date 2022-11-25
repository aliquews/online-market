from typing import Union
from marketdb.tables import Base, User, Product, Bill
from config import DB_LOGIN

from sqlalchemy import create_engine, exists, select
from sqlalchemy.orm import Session

class DataBase:
    def __init__(self, db_login) -> None:
        '''
        create connection with db and if not exists create tables
        '''
        self.engine = create_engine(db_login)
        Base.metadata.create_all(self.engine)

    def append_user(self, telegram_id: int):
        '''
        appends user in database
        '''
        with Session(self.engine) as session:
            if session.query(exists().where(User.tg_id == telegram_id)).scalar() == False:
                user = User(
                    tg_id = telegram_id,
                )
                session.add_all([user])
                session.commit()

    def append_product(self, data: dict):
        '''
        !FOR ADMINS!
        '''
        with Session(self.engine) as session:
            prod = Product(
                description = data['title'],
                price = int(data['price']),
                content = data['content'],
            )
            session.add(prod)
            session.commit()

    def show_products(self):
        with Session(self.engine) as session:
            text = str()
            out_data = list()
            contents = select(Product)
            for row in session.execute(contents):
                out_data.append([row.Product.description, row.Product.price])
            for content in out_data:
                text += " | ".join(list(map(str,content)))
                text += "₽\n\n"
            return text

    def select_product_price(self, message: str):
        with Session(self.engine) as session:
            title = message.split(' | ')[0]
            product_price = session.scalar(select(Product.price).where(Product.description == title))
            return product_price

    def select_content(self, message: str):
        with Session(self.engine) as session:
            title = message.split(' | ')[0]
            content = session.scalar(select(Product.content).where(Product.description == title))
            return content

    def append_bill(self, telegram_id: int, bill: Union[str, int], content):
        with Session(self.engine) as session:
            billing = Bill(
                tg_id=telegram_id,
                bill=bill,
                content=content,
            )
            session.add(billing)
            session.commit()

    def show_bill(self, telegram_id: int):
        with Session(self.engine) as session:
            bill = session.scalar(select(Bill.bill).where(Bill.tg_id == telegram_id))
            return bill

    def show_content(self, bill: Union[int, str]):
        with Session(self.engine) as session:
            content = session.scalar(select(Bill.content).where(Bill.bill == bill))
            return content

    def del_bill(self, bill: Union[int, str]):
        with Session(self.engine) as session:
            table_string = session.get(Bill, session.scalar(select(Bill.id).where(Bill.bill == bill)))
            session.delete(table_string)
            session.commit()

    def get_title_list(self):
        titles = list()
        with Session(self.engine) as session:
            title = session.scalars(select(Product.description))
            for i in title:
                titles.append(i)
            return titles

    def del_product(self, title):
        with Session(self.engine) as session:
            stmt = session.get(Product, session.scalar(select(Product.id).where(Product.description == title)))
            session.delete(stmt)
            session.commit()



db = DataBase(DB_LOGIN)
