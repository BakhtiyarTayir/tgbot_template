from collections import UserList
from tkinter import CASCADE
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from tgbot.models.product import Products
from tgbot.models.database import Base


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)

    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        CASCADE=True))
    
    def __str__(self):
        return f"{self.quantity} {self.data}"