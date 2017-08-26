from db_admin.db_helper import DB_helper
from models.db_tables import Divisions, Staff, QuitSheets, Signs, Roles
from datetime import datetime as dt

db = DB_helper()

if __name__ == "__main__":
    db.db_connect()

# session = db.get_session()
# set_records_U = []
# # for a in range(0, 10):
# U = User('Иванов', 'Иван', '555','Иванович')
# set_records_U.append(U)
# for a in range(0,5):
#     U.properties.append(User_property(dt.now(),'Мелитополь'))
# session.add_all(set_records_U)
#
# session.commit()
#
# session = db.get_session()
#
#
# res = session.query(User_property).filter(User_property.location.like('%Мел%')).all()
# print(res[0].location)


# for a in session.query(User):
#     print(a.surname)