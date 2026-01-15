from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class C:

    pass
class b_B(C):

    def __init__(self, to_enum: str, custom_datatype: str):
        self.to_enum = to_enum
        self.custom_datatype = custom_datatype
        
    @property
    def custom_datatype(self) -> str:
        return self.__custom_datatype

    @custom_datatype.setter
    def custom_datatype(self, custom_datatype: str):
        self.__custom_datatype = custom_datatype

    @property
    def to_enum(self) -> str:
        return self.__to_enum

    @to_enum.setter
    def to_enum(self, to_enum: str):
        self.__to_enum = to_enum
