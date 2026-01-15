from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dDL_Key:

    pass
class Key:

    pass
class dDL_Unique_key(Key):

    pass
class dDL_Foreign_key(Key):

    pass
class dDL_Primary_key(Key):

    pass
class dDL_Colname:

    def __init__(self, id: str, dDL_Colname: "dDL_Comment" = None, dDL_Colname21: "dDL_Key" = None):
        self.id = id
        self.dDL_Colname = dDL_Colname
        self.dDL_Colname21 = dDL_Colname21
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_Colname(self):
        return self.__dDL_Colname

    @dDL_Colname.setter
    def dDL_Colname(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Colname__dDL_Colname", None)
        self.__dDL_Colname = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Comment15"):
                opp_val = getattr(old_value, "dDL_Comment15", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Comment15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Comment15"):
                opp_val = getattr(value, "dDL_Comment15", None)
                setattr(value, "dDL_Comment15", self)

    @property
    def dDL_Colname21(self):
        return self.__dDL_Colname21

    @dDL_Colname21.setter
    def dDL_Colname21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Colname__dDL_Colname21", None)
        self.__dDL_Colname21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Key20"):
                opp_val = getattr(old_value, "dDL_Key20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Key20"):
                opp_val = getattr(value, "dDL_Key20", None)
                if opp_val is None:
                    setattr(value, "dDL_Key20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dDL_Sequence_options:

    def __init__(self, increment: str, start: str, maxvalue: str, nomaxvalue: str, minvalue: str, nominvalue: str, cycle: str, nocycle: str, cache: str, nocache: str, order: str, noorder: str, dDL_Sequence_options: "dDL_Create_sequence" = None):
        self.increment = increment
        self.start = start
        self.maxvalue = maxvalue
        self.nomaxvalue = nomaxvalue
        self.minvalue = minvalue
        self.nominvalue = nominvalue
        self.cycle = cycle
        self.nocycle = nocycle
        self.cache = cache
        self.nocache = nocache
        self.order = order
        self.noorder = noorder
        self.dDL_Sequence_options = dDL_Sequence_options
        
    @property
    def nominvalue(self) -> str:
        return self.__nominvalue

    @nominvalue.setter
    def nominvalue(self, nominvalue: str):
        self.__nominvalue = nominvalue

    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def nomaxvalue(self) -> str:
        return self.__nomaxvalue

    @nomaxvalue.setter
    def nomaxvalue(self, nomaxvalue: str):
        self.__nomaxvalue = nomaxvalue

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def nocache(self) -> str:
        return self.__nocache

    @nocache.setter
    def nocache(self, nocache: str):
        self.__nocache = nocache

    @property
    def nocycle(self) -> str:
        return self.__nocycle

    @nocycle.setter
    def nocycle(self, nocycle: str):
        self.__nocycle = nocycle

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def noorder(self) -> str:
        return self.__noorder

    @noorder.setter
    def noorder(self, noorder: str):
        self.__noorder = noorder

    @property
    def maxvalue(self) -> str:
        return self.__maxvalue

    @maxvalue.setter
    def maxvalue(self, maxvalue: str):
        self.__maxvalue = maxvalue

    @property
    def cache(self) -> str:
        return self.__cache

    @cache.setter
    def cache(self, cache: str):
        self.__cache = cache

    @property
    def minvalue(self) -> str:
        return self.__minvalue

    @minvalue.setter
    def minvalue(self, minvalue: str):
        self.__minvalue = minvalue

    @property
    def cycle(self) -> str:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: str):
        self.__cycle = cycle

    @property
    def dDL_Sequence_options(self):
        return self.__dDL_Sequence_options

    @dDL_Sequence_options.setter
    def dDL_Sequence_options(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Sequence_options__dDL_Sequence_options", None)
        self.__dDL_Sequence_options = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Create_sequence"):
                opp_val = getattr(old_value, "dDL_Create_sequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Create_sequence"):
                opp_val = getattr(value, "dDL_Create_sequence", None)
                if opp_val is None:
                    setattr(value, "dDL_Create_sequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dDL_Constraint:

    def __init__(self, id: str, dDL_Constraint11: "dDL_Alter_table" = None, dDL_Constraint: "dDL_Create_table" = None, dDL_Constraint18: "dDL_Key" = None):
        self.id = id
        self.dDL_Constraint11 = dDL_Constraint11
        self.dDL_Constraint = dDL_Constraint
        self.dDL_Constraint18 = dDL_Constraint18
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_Constraint18(self):
        return self.__dDL_Constraint18

    @dDL_Constraint18.setter
    def dDL_Constraint18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Constraint__dDL_Constraint18", None)
        self.__dDL_Constraint18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Key"):
                opp_val = getattr(old_value, "dDL_Key", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Key"):
                opp_val = getattr(value, "dDL_Key", None)
                setattr(value, "dDL_Key", self)

    @property
    def dDL_Constraint(self):
        return self.__dDL_Constraint

    @dDL_Constraint.setter
    def dDL_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Constraint__dDL_Constraint", None)
        self.__dDL_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Create_table3"):
                opp_val = getattr(old_value, "dDL_Create_table3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Create_table3"):
                opp_val = getattr(value, "dDL_Create_table3", None)
                if opp_val is None:
                    setattr(value, "dDL_Create_table3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dDL_Constraint11(self):
        return self.__dDL_Constraint11

    @dDL_Constraint11.setter
    def dDL_Constraint11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Constraint__dDL_Constraint11", None)
        self.__dDL_Constraint11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Alter_table10"):
                opp_val = getattr(old_value, "dDL_Alter_table10", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Alter_table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Alter_table10"):
                opp_val = getattr(value, "dDL_Alter_table10", None)
                setattr(value, "dDL_Alter_table10", self)

class dDL_Tabname:

    def __init__(self, id: str, basename: str, dDL_Tabname: "dDL_Alter_table" = None, dDL_Tabname13: "dDL_Comment" = None, dDL_Tabname23: "dDL_Foreign_key" = None):
        self.id = id
        self.basename = basename
        self.dDL_Tabname = dDL_Tabname
        self.dDL_Tabname13 = dDL_Tabname13
        self.dDL_Tabname23 = dDL_Tabname23
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def basename(self) -> str:
        return self.__basename

    @basename.setter
    def basename(self, basename: str):
        self.__basename = basename

    @property
    def dDL_Tabname(self):
        return self.__dDL_Tabname

    @dDL_Tabname.setter
    def dDL_Tabname(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Tabname__dDL_Tabname", None)
        self.__dDL_Tabname = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Alter_table"):
                opp_val = getattr(old_value, "dDL_Alter_table", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Alter_table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Alter_table"):
                opp_val = getattr(value, "dDL_Alter_table", None)
                setattr(value, "dDL_Alter_table", self)

    @property
    def dDL_Tabname13(self):
        return self.__dDL_Tabname13

    @dDL_Tabname13.setter
    def dDL_Tabname13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Tabname__dDL_Tabname13", None)
        self.__dDL_Tabname13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Comment"):
                opp_val = getattr(old_value, "dDL_Comment", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Comment"):
                opp_val = getattr(value, "dDL_Comment", None)
                setattr(value, "dDL_Comment", self)

    @property
    def dDL_Tabname23(self):
        return self.__dDL_Tabname23

    @dDL_Tabname23.setter
    def dDL_Tabname23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Tabname__dDL_Tabname23", None)
        self.__dDL_Tabname23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Foreign_key"):
                opp_val = getattr(old_value, "dDL_Foreign_key", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Foreign_key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Foreign_key"):
                opp_val = getattr(value, "dDL_Foreign_key", None)
                setattr(value, "dDL_Foreign_key", self)

class dDL_ISNULL:

    def __init__(self, null: bool, nonNull: bool, dDL_ISNULL: "dDL_Column" = None):
        self.null = null
        self.nonNull = nonNull
        self.dDL_ISNULL = dDL_ISNULL
        
    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

    @property
    def nonNull(self) -> bool:
        return self.__nonNull

    @nonNull.setter
    def nonNull(self, nonNull: bool):
        self.__nonNull = nonNull

    @property
    def dDL_ISNULL(self):
        return self.__dDL_ISNULL

    @dDL_ISNULL.setter
    def dDL_ISNULL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_ISNULL__dDL_ISNULL", None)
        self.__dDL_ISNULL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Column7"):
                opp_val = getattr(old_value, "dDL_Column7", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Column7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Column7"):
                opp_val = getattr(value, "dDL_Column7", None)
                setattr(value, "dDL_Column7", self)

class dDL_TYPE:

    def __init__(self, id: str, dDL_TYPE: "dDL_Column" = None):
        self.id = id
        self.dDL_TYPE = dDL_TYPE
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_TYPE(self):
        return self.__dDL_TYPE

    @dDL_TYPE.setter
    def dDL_TYPE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_TYPE__dDL_TYPE", None)
        self.__dDL_TYPE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Column5"):
                opp_val = getattr(old_value, "dDL_Column5", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Column5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Column5"):
                opp_val = getattr(value, "dDL_Column5", None)
                setattr(value, "dDL_Column5", self)

class dDL_Column:

    def __init__(self, number: int, id: str, dDL_Column: "dDL_Create_table" = None, dDL_Column5: "dDL_TYPE" = None, dDL_Column7: "dDL_ISNULL" = None):
        self.number = number
        self.id = id
        self.dDL_Column = dDL_Column
        self.dDL_Column5 = dDL_Column5
        self.dDL_Column7 = dDL_Column7
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def dDL_Column7(self):
        return self.__dDL_Column7

    @dDL_Column7.setter
    def dDL_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Column__dDL_Column7", None)
        self.__dDL_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_ISNULL"):
                opp_val = getattr(old_value, "dDL_ISNULL", None)
                if opp_val == self:
                    setattr(old_value, "dDL_ISNULL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_ISNULL"):
                opp_val = getattr(value, "dDL_ISNULL", None)
                setattr(value, "dDL_ISNULL", self)

    @property
    def dDL_Column(self):
        return self.__dDL_Column

    @dDL_Column.setter
    def dDL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Column__dDL_Column", None)
        self.__dDL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Create_table"):
                opp_val = getattr(old_value, "dDL_Create_table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Create_table"):
                opp_val = getattr(value, "dDL_Create_table", None)
                if opp_val is None:
                    setattr(value, "dDL_Create_table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dDL_Column5(self):
        return self.__dDL_Column5

    @dDL_Column5.setter
    def dDL_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Column__dDL_Column5", None)
        self.__dDL_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_TYPE"):
                opp_val = getattr(old_value, "dDL_TYPE", None)
                if opp_val == self:
                    setattr(old_value, "dDL_TYPE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_TYPE"):
                opp_val = getattr(value, "dDL_TYPE", None)
                setattr(value, "dDL_TYPE", self)

class Definition:

    pass
class dDL_Create_sequence(Definition):

    def __init__(self, id: str, dDL_Create_sequence: set["dDL_Sequence_options"] = None):
        self.id = id
        self.dDL_Create_sequence = dDL_Create_sequence if dDL_Create_sequence is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_Create_sequence(self):
        return self.__dDL_Create_sequence

    @dDL_Create_sequence.setter
    def dDL_Create_sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Create_sequence__dDL_Create_sequence", None)
        self.__dDL_Create_sequence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dDL_Sequence_options"):
                    opp_val = getattr(item, "dDL_Sequence_options", None)
                    
                    if opp_val == self:
                        setattr(item, "dDL_Sequence_options", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dDL_Sequence_options"):
                    opp_val = getattr(item, "dDL_Sequence_options", None)
                    
                    setattr(item, "dDL_Sequence_options", self)
                    

class dDL_Comment(Definition):

    def __init__(self, columnId: str, string: str, dDL_Comment: "dDL_Tabname" = None, dDL_Comment15: "dDL_Colname" = None):
        self.columnId = columnId
        self.string = string
        self.dDL_Comment = dDL_Comment
        self.dDL_Comment15 = dDL_Comment15
        
    @property
    def columnId(self) -> str:
        return self.__columnId

    @columnId.setter
    def columnId(self, columnId: str):
        self.__columnId = columnId

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def dDL_Comment15(self):
        return self.__dDL_Comment15

    @dDL_Comment15.setter
    def dDL_Comment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Comment__dDL_Comment15", None)
        self.__dDL_Comment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Colname"):
                opp_val = getattr(old_value, "dDL_Colname", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Colname", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Colname"):
                opp_val = getattr(value, "dDL_Colname", None)
                setattr(value, "dDL_Colname", self)

    @property
    def dDL_Comment(self):
        return self.__dDL_Comment

    @dDL_Comment.setter
    def dDL_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Comment__dDL_Comment", None)
        self.__dDL_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Tabname13"):
                opp_val = getattr(old_value, "dDL_Tabname13", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Tabname13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Tabname13"):
                opp_val = getattr(value, "dDL_Tabname13", None)
                setattr(value, "dDL_Tabname13", self)

class dDL_Alter_table(Definition):

    def __init__(self, add: str, enable: str, id: str, dDL_Alter_table: "dDL_Tabname" = None, dDL_Alter_table10: "dDL_Constraint" = None):
        self.add = add
        self.enable = enable
        self.id = id
        self.dDL_Alter_table = dDL_Alter_table
        self.dDL_Alter_table10 = dDL_Alter_table10
        
    @property
    def add(self) -> str:
        return self.__add

    @add.setter
    def add(self, add: str):
        self.__add = add

    @property
    def enable(self) -> str:
        return self.__enable

    @enable.setter
    def enable(self, enable: str):
        self.__enable = enable

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_Alter_table(self):
        return self.__dDL_Alter_table

    @dDL_Alter_table.setter
    def dDL_Alter_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Alter_table__dDL_Alter_table", None)
        self.__dDL_Alter_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Tabname"):
                opp_val = getattr(old_value, "dDL_Tabname", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Tabname", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Tabname"):
                opp_val = getattr(value, "dDL_Tabname", None)
                setattr(value, "dDL_Tabname", self)

    @property
    def dDL_Alter_table10(self):
        return self.__dDL_Alter_table10

    @dDL_Alter_table10.setter
    def dDL_Alter_table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Alter_table__dDL_Alter_table10", None)
        self.__dDL_Alter_table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dDL_Constraint11"):
                opp_val = getattr(old_value, "dDL_Constraint11", None)
                if opp_val == self:
                    setattr(old_value, "dDL_Constraint11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dDL_Constraint11"):
                opp_val = getattr(value, "dDL_Constraint11", None)
                setattr(value, "dDL_Constraint11", self)

class dDL_Create_table(Definition):

    def __init__(self, id: str, dDL_Create_table: set["dDL_Column"] = None, dDL_Create_table3: set["dDL_Constraint"] = None):
        self.id = id
        self.dDL_Create_table = dDL_Create_table if dDL_Create_table is not None else set()
        self.dDL_Create_table3 = dDL_Create_table3 if dDL_Create_table3 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dDL_Create_table(self):
        return self.__dDL_Create_table

    @dDL_Create_table.setter
    def dDL_Create_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Create_table__dDL_Create_table", None)
        self.__dDL_Create_table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dDL_Column"):
                    opp_val = getattr(item, "dDL_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "dDL_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dDL_Column"):
                    opp_val = getattr(item, "dDL_Column", None)
                    
                    setattr(item, "dDL_Column", self)
                    

    @property
    def dDL_Create_table3(self):
        return self.__dDL_Create_table3

    @dDL_Create_table3.setter
    def dDL_Create_table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dDL_Create_table__dDL_Create_table3", None)
        self.__dDL_Create_table3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dDL_Constraint"):
                    opp_val = getattr(item, "dDL_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "dDL_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dDL_Constraint"):
                    opp_val = getattr(item, "dDL_Constraint", None)
                    
                    setattr(item, "dDL_Constraint", self)
                    

class dDL_Definition:

    pass
class dDL_Data_definition:

    pass