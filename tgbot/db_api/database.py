import imp
from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import MYSQLURI

db = Gino()


async def create_db():
    await db.set_bind(MYSQLURI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()