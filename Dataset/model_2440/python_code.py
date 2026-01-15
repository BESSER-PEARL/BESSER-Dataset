from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ddl_DataElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DataElement:

    pass
class ddl_Table(DataElement):

    pass
class ddl_Column(DataElement):

    pass
class ddl_DataType(DataElement):

    pass
class ddl_Schema(DataElement):

    pass