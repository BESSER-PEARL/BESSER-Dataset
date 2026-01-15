from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SqlDataType(Enum):
    VARCHAR = "VARCHAR"
    CHAR = "CHAR"
    INTEGER = "INTEGER"
    DATE = "DATE"


############################################
# Definition of Classes
############################################

class Key:

    pass
class relational_PrimaryKey(Key):

    pass
class Table:

    pass
class relational_View(Table):

    pass
class relational_RelationalEntity(ABC):

    pass
class relational_ForeignKey(Key):

    pass
class RelationalEntity:

    pass
class relational_Schema(RelationalEntity):

    pass
class relational_Column(RelationalEntity):

    pass
class relational_Key(RelationalEntity):

    pass
class relational_Table(RelationalEntity):

    pass