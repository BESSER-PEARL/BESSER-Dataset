from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataType:

    pass
class cassandra_CounterColumnType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_DoubleType(DataType):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class cassandra_BytesType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_DecimalType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_UTF8Type(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_DateType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_AsciiType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_IntegerType(DataType):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class cassandra_DataType:

    pass
class cassandra_UUIDType(DataType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class cassandra_BooleanType(DataType):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class cassandra_FloatType(DataType):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class cassandra_Column:

    def __init__(self, key: str, timestamp: str, cassandra_Column: "cassandra_Row" = None, cassandra_Column8: "cassandra_DataType" = None, cassandra_Column11: "cassandra_SuperColumn" = None):
        self.key = key
        self.timestamp = timestamp
        self.cassandra_Column = cassandra_Column
        self.cassandra_Column8 = cassandra_Column8
        self.cassandra_Column11 = cassandra_Column11
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp


    @property
    def cassandra_Column11(self):
        return self.__cassandra_Column11

    @cassandra_Column11.setter
    def cassandra_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Column__cassandra_Column11", None)
        self.__cassandra_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_SuperColumn10"):
                opp_val = getattr(old_value, "cassandra_SuperColumn10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_SuperColumn10"):
                opp_val = getattr(value, "cassandra_SuperColumn10", None)
                if opp_val is None:
                    setattr(value, "cassandra_SuperColumn10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cassandra_Column8(self):
        return self.__cassandra_Column8

    @cassandra_Column8.setter
    def cassandra_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Column__cassandra_Column8", None)
        self.__cassandra_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_DataType"):
                opp_val = getattr(old_value, "cassandra_DataType", None)
                if opp_val == self:
                    setattr(old_value, "cassandra_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_DataType"):
                opp_val = getattr(value, "cassandra_DataType", None)
                setattr(value, "cassandra_DataType", self)

    @property
    def cassandra_Column(self):
        return self.__cassandra_Column

    @cassandra_Column.setter
    def cassandra_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Column__cassandra_Column", None)
        self.__cassandra_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_Row4"):
                opp_val = getattr(old_value, "cassandra_Row4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_Row4"):
                opp_val = getattr(value, "cassandra_Row4", None)
                if opp_val is None:
                    setattr(value, "cassandra_Row4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cassandra_Row:

    def __init__(self, key: str, cassandra_Row6: set["cassandra_SuperColumn"] = None, cassandra_Row: "cassandra_ColumnFamily" = None, cassandra_Row4: set["cassandra_Column"] = None):
        self.key = key
        self.cassandra_Row6 = cassandra_Row6 if cassandra_Row6 is not None else set()
        self.cassandra_Row = cassandra_Row
        self.cassandra_Row4 = cassandra_Row4 if cassandra_Row4 is not None else set()
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def cassandra_Row(self):
        return self.__cassandra_Row

    @cassandra_Row.setter
    def cassandra_Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Row__cassandra_Row", None)
        self.__cassandra_Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_ColumnFamily2"):
                opp_val = getattr(old_value, "cassandra_ColumnFamily2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_ColumnFamily2"):
                opp_val = getattr(value, "cassandra_ColumnFamily2", None)
                if opp_val is None:
                    setattr(value, "cassandra_ColumnFamily2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cassandra_Row6(self):
        return self.__cassandra_Row6

    @cassandra_Row6.setter
    def cassandra_Row6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Row__cassandra_Row6", None)
        self.__cassandra_Row6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cassandra_SuperColumn"):
                    opp_val = getattr(item, "cassandra_SuperColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "cassandra_SuperColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cassandra_SuperColumn"):
                    opp_val = getattr(item, "cassandra_SuperColumn", None)
                    
                    setattr(item, "cassandra_SuperColumn", self)
                    

    @property
    def cassandra_Row4(self):
        return self.__cassandra_Row4

    @cassandra_Row4.setter
    def cassandra_Row4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Row__cassandra_Row4", None)
        self.__cassandra_Row4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cassandra_Column"):
                    opp_val = getattr(item, "cassandra_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "cassandra_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cassandra_Column"):
                    opp_val = getattr(item, "cassandra_Column", None)
                    
                    setattr(item, "cassandra_Column", self)
                    

class cassandra_ColumnFamily:

    def __init__(self, name: str, cassandra_ColumnFamily: "cassandra_Keyspace" = None, cassandra_ColumnFamily2: set["cassandra_Row"] = None):
        self.name = name
        self.cassandra_ColumnFamily = cassandra_ColumnFamily
        self.cassandra_ColumnFamily2 = cassandra_ColumnFamily2 if cassandra_ColumnFamily2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def cassandra_ColumnFamily(self):
        return self.__cassandra_ColumnFamily

    @cassandra_ColumnFamily.setter
    def cassandra_ColumnFamily(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_ColumnFamily__cassandra_ColumnFamily", None)
        self.__cassandra_ColumnFamily = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_Keyspace"):
                opp_val = getattr(old_value, "cassandra_Keyspace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_Keyspace"):
                opp_val = getattr(value, "cassandra_Keyspace", None)
                if opp_val is None:
                    setattr(value, "cassandra_Keyspace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cassandra_ColumnFamily2(self):
        return self.__cassandra_ColumnFamily2

    @cassandra_ColumnFamily2.setter
    def cassandra_ColumnFamily2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_ColumnFamily__cassandra_ColumnFamily2", None)
        self.__cassandra_ColumnFamily2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cassandra_Row"):
                    opp_val = getattr(item, "cassandra_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "cassandra_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cassandra_Row"):
                    opp_val = getattr(item, "cassandra_Row", None)
                    
                    setattr(item, "cassandra_Row", self)
                    

class cassandra_SuperColumn:

    def __init__(self, key: str, cassandra_SuperColumn: "cassandra_Row" = None, cassandra_SuperColumn10: set["cassandra_Column"] = None):
        self.key = key
        self.cassandra_SuperColumn = cassandra_SuperColumn
        self.cassandra_SuperColumn10 = cassandra_SuperColumn10 if cassandra_SuperColumn10 is not None else set()
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def cassandra_SuperColumn(self):
        return self.__cassandra_SuperColumn

    @cassandra_SuperColumn.setter
    def cassandra_SuperColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_SuperColumn__cassandra_SuperColumn", None)
        self.__cassandra_SuperColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cassandra_Row6"):
                opp_val = getattr(old_value, "cassandra_Row6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cassandra_Row6"):
                opp_val = getattr(value, "cassandra_Row6", None)
                if opp_val is None:
                    setattr(value, "cassandra_Row6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cassandra_SuperColumn10(self):
        return self.__cassandra_SuperColumn10

    @cassandra_SuperColumn10.setter
    def cassandra_SuperColumn10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_SuperColumn__cassandra_SuperColumn10", None)
        self.__cassandra_SuperColumn10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cassandra_Column11"):
                    opp_val = getattr(item, "cassandra_Column11", None)
                    
                    if opp_val == self:
                        setattr(item, "cassandra_Column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cassandra_Column11"):
                    opp_val = getattr(item, "cassandra_Column11", None)
                    
                    setattr(item, "cassandra_Column11", self)
                    

class cassandra_Keyspace:

    def __init__(self, name: str, cassandra_Keyspace: set["cassandra_ColumnFamily"] = None):
        self.name = name
        self.cassandra_Keyspace = cassandra_Keyspace if cassandra_Keyspace is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def cassandra_Keyspace(self):
        return self.__cassandra_Keyspace

    @cassandra_Keyspace.setter
    def cassandra_Keyspace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cassandra_Keyspace__cassandra_Keyspace", None)
        self.__cassandra_Keyspace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cassandra_ColumnFamily"):
                    opp_val = getattr(item, "cassandra_ColumnFamily", None)
                    
                    if opp_val == self:
                        setattr(item, "cassandra_ColumnFamily", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cassandra_ColumnFamily"):
                    opp_val = getattr(item, "cassandra_ColumnFamily", None)
                    
                    setattr(item, "cassandra_ColumnFamily", self)
                    
