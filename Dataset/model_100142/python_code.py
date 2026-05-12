from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dSDL_Table:

    def __init__(self, name: str, dSDL_Table2: set["dSDL_Attribute"] = None, dSDL_Table: "dSDL_Database" = None):
        self.name = name
        self.dSDL_Table2 = dSDL_Table2 if dSDL_Table2 is not None else set()
        self.dSDL_Table = dSDL_Table
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dSDL_Table(self):
        return self.__dSDL_Table

    @dSDL_Table.setter
    def dSDL_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Table__dSDL_Table", None)
        self.__dSDL_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSDL_Database"):
                opp_val = getattr(old_value, "dSDL_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSDL_Database"):
                opp_val = getattr(value, "dSDL_Database", None)
                if opp_val is None:
                    setattr(value, "dSDL_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSDL_Table2(self):
        return self.__dSDL_Table2

    @dSDL_Table2.setter
    def dSDL_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Table__dSDL_Table2", None)
        self.__dSDL_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSDL_Attribute"):
                    opp_val = getattr(item, "dSDL_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "dSDL_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSDL_Attribute"):
                    opp_val = getattr(item, "dSDL_Attribute", None)
                    
                    setattr(item, "dSDL_Attribute", self)
                    

class dSDL_Database:

    def __init__(self, name: str, dSDL_Database: set["dSDL_Table"] = None):
        self.name = name
        self.dSDL_Database = dSDL_Database if dSDL_Database is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dSDL_Database(self):
        return self.__dSDL_Database

    @dSDL_Database.setter
    def dSDL_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Database__dSDL_Database", None)
        self.__dSDL_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSDL_Table"):
                    opp_val = getattr(item, "dSDL_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "dSDL_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSDL_Table"):
                    opp_val = getattr(item, "dSDL_Table", None)
                    
                    setattr(item, "dSDL_Table", self)
                    

class Property:

    pass
class dSDL_AutoIncrement(Property):

    def __init__(self, autoIncrement: bool):
        self.autoIncrement = autoIncrement
        
        pass
    @property
    def autoIncrement(self):
        return self.__autoIncrement

    @autoIncrement.setter
    def autoIncrement(self, autoIncrement: bool):
        self.__autoIncrement = autoIncrement


class dSDL_Nullable(Property):

    def __init__(self, nullable: bool):
        self.nullable = nullable
        
        pass
    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


class dSDL_ForeignKey(Property):

    def __init__(self, tableName: str, attributeName: str):
        self.tableName = tableName
        self.attributeName = attributeName
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def attributeName(self):
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName


class dSDL_PrimaryKey(Property):

    def __init__(self, primaryKey: bool):
        self.primaryKey = primaryKey
        
        pass
    @property
    def primaryKey(self):
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey


class Type:

    pass
class dSDL_Varchar(Type):

    def __init__(self, varchar: str, length: int):
        self.varchar = varchar
        self.length = length
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def varchar(self):
        return self.__varchar

    @varchar.setter
    def varchar(self, varchar: str):
        self.__varchar = varchar


class dSDL_DateTime(Type):

    def __init__(self, date: str):
        self.date = date
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


class dSDL_Text(Type):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class dSDL_Integer(Type):

    def __init__(self, integer: str, length: int):
        self.integer = integer
        self.length = length
        
        pass
    @property
    def integer(self):
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


class dSDL_Property:

    pass
class dSDL_Type:

    pass
class dSDL_Attribute:

    def __init__(self, attributeName: str, dSDL_Attribute: "dSDL_Table" = None, dSDL_Attribute4: "dSDL_Type" = None, dSDL_Attribute6: set["dSDL_Property"] = None):
        self.attributeName = attributeName
        self.dSDL_Attribute = dSDL_Attribute
        self.dSDL_Attribute4 = dSDL_Attribute4
        self.dSDL_Attribute6 = dSDL_Attribute6 if dSDL_Attribute6 is not None else set()
        
        pass
    @property
    def attributeName(self):
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName


    @property
    def dSDL_Attribute6(self):
        return self.__dSDL_Attribute6

    @dSDL_Attribute6.setter
    def dSDL_Attribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Attribute__dSDL_Attribute6", None)
        self.__dSDL_Attribute6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSDL_Property"):
                    opp_val = getattr(item, "dSDL_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "dSDL_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSDL_Property"):
                    opp_val = getattr(item, "dSDL_Property", None)
                    
                    setattr(item, "dSDL_Property", self)
                    

    @property
    def dSDL_Attribute4(self):
        return self.__dSDL_Attribute4

    @dSDL_Attribute4.setter
    def dSDL_Attribute4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Attribute__dSDL_Attribute4", None)
        self.__dSDL_Attribute4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSDL_Type"):
                opp_val = getattr(old_value, "dSDL_Type", None)
                if opp_val == self:
                    setattr(old_value, "dSDL_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSDL_Type"):
                opp_val = getattr(value, "dSDL_Type", None)
                setattr(value, "dSDL_Type", self)

    @property
    def dSDL_Attribute(self):
        return self.__dSDL_Attribute

    @dSDL_Attribute.setter
    def dSDL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSDL_Attribute__dSDL_Attribute", None)
        self.__dSDL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSDL_Table2"):
                opp_val = getattr(old_value, "dSDL_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSDL_Table2"):
                opp_val = getattr(value, "dSDL_Table2", None)
                if opp_val is None:
                    setattr(value, "dSDL_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
