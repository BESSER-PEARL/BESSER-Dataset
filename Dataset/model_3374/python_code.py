from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Characters:

    pass
class DDL_NChar(Characters):

    pass
class DDL_VarChar(Characters):

    pass
class DDL_CharVarying(Characters):

    pass
class DDL_VarChar2(Characters):

    pass
class DDL_Char(Characters):

    pass
class DDL_CharacterVarying(Characters):

    pass
class DDL_NVarChar2(Characters):

    pass
class DDL_Character(Characters):

    pass
class DDL_ValuesCk:

    def __init__(self, columnName: str, logConjuntion: str, value: str, comparator: str, DDL_ValuesCk: "DDL_Ck" = None):
        self.columnName = columnName
        self.logConjuntion = logConjuntion
        self.value = value
        self.comparator = comparator
        self.DDL_ValuesCk = DDL_ValuesCk
        
        pass
    @property
    def logConjuntion(self):
        return self.__logConjuntion

    @logConjuntion.setter
    def logConjuntion(self, logConjuntion: str):
        self.__logConjuntion = logConjuntion


    @property
    def comparator(self):
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def DDL_ValuesCk(self):
        return self.__DDL_ValuesCk

    @DDL_ValuesCk.setter
    def DDL_ValuesCk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_ValuesCk__DDL_ValuesCk", None)
        self.__DDL_ValuesCk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Ck"):
                opp_val = getattr(old_value, "DDL_Ck", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Ck"):
                opp_val = getattr(value, "DDL_Ck", None)
                if opp_val is None:
                    setattr(value, "DDL_Ck", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_Ck:

    def __init__(self, nameCk: str, status: str, DDL_Ck19: "DDL_Table" = None, DDL_Ck: set["DDL_ValuesCk"] = None):
        self.nameCk = nameCk
        self.status = status
        self.DDL_Ck19 = DDL_Ck19
        self.DDL_Ck = DDL_Ck if DDL_Ck is not None else set()
        
        pass
    @property
    def nameCk(self):
        return self.__nameCk

    @nameCk.setter
    def nameCk(self, nameCk: str):
        self.__nameCk = nameCk


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def DDL_Ck(self):
        return self.__DDL_Ck

    @DDL_Ck.setter
    def DDL_Ck(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Ck__DDL_Ck", None)
        self.__DDL_Ck = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_ValuesCk"):
                    opp_val = getattr(item, "DDL_ValuesCk", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_ValuesCk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_ValuesCk"):
                    opp_val = getattr(item, "DDL_ValuesCk", None)
                    
                    setattr(item, "DDL_ValuesCk", self)
                    

    @property
    def DDL_Ck19(self):
        return self.__DDL_Ck19

    @DDL_Ck19.setter
    def DDL_Ck19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Ck__DDL_Ck19", None)
        self.__DDL_Ck19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table18"):
                opp_val = getattr(old_value, "DDL_Table18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table18"):
                opp_val = getattr(value, "DDL_Table18", None)
                if opp_val is None:
                    setattr(value, "DDL_Table18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_Fk:

    def __init__(self, nameFk: str, columnName: str, columnReference: str, status: str, DDL_Fk16: "DDL_Table" = None, DDL_Fk: "DDL_Table" = None):
        self.nameFk = nameFk
        self.columnName = columnName
        self.columnReference = columnReference
        self.status = status
        self.DDL_Fk16 = DDL_Fk16
        self.DDL_Fk = DDL_Fk
        
        pass
    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def columnReference(self):
        return self.__columnReference

    @columnReference.setter
    def columnReference(self, columnReference: str):
        self.__columnReference = columnReference


    @property
    def nameFk(self):
        return self.__nameFk

    @nameFk.setter
    def nameFk(self, nameFk: str):
        self.__nameFk = nameFk


    @property
    def DDL_Fk(self):
        return self.__DDL_Fk

    @DDL_Fk.setter
    def DDL_Fk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Fk__DDL_Fk", None)
        self.__DDL_Fk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table"):
                opp_val = getattr(old_value, "DDL_Table", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table"):
                opp_val = getattr(value, "DDL_Table", None)
                setattr(value, "DDL_Table", self)

    @property
    def DDL_Fk16(self):
        return self.__DDL_Fk16

    @DDL_Fk16.setter
    def DDL_Fk16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Fk__DDL_Fk16", None)
        self.__DDL_Fk16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table15"):
                opp_val = getattr(old_value, "DDL_Table15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table15"):
                opp_val = getattr(value, "DDL_Table15", None)
                if opp_val is None:
                    setattr(value, "DDL_Table15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_Pk:

    def __init__(self, namePk: str, columnName: str, DDL_Pk: "DDL_Table" = None):
        self.namePk = namePk
        self.columnName = columnName
        self.DDL_Pk = DDL_Pk
        
        pass
    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def namePk(self):
        return self.__namePk

    @namePk.setter
    def namePk(self, namePk: str):
        self.__namePk = namePk


    @property
    def DDL_Pk(self):
        return self.__DDL_Pk

    @DDL_Pk.setter
    def DDL_Pk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Pk__DDL_Pk", None)
        self.__DDL_Pk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table13"):
                opp_val = getattr(old_value, "DDL_Table13", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Table13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table13"):
                opp_val = getattr(value, "DDL_Table13", None)
                setattr(value, "DDL_Table13", self)

class DDL_DDLDefinition:

    pass
class DataDefinition:

    pass
class DDL_Table(DataDefinition):

    def __init__(self, tableName: str, commentTable: str, DDL_Table10: set["DDL_Column"] = None, DDL_Table13: "DDL_Pk" = None, DDL_Table15: set["DDL_Fk"] = None, DDL_Table18: set["DDL_Ck"] = None, DDL_Table: "DDL_Fk" = None):
        self.tableName = tableName
        self.commentTable = commentTable
        self.DDL_Table10 = DDL_Table10 if DDL_Table10 is not None else set()
        self.DDL_Table13 = DDL_Table13
        self.DDL_Table15 = DDL_Table15 if DDL_Table15 is not None else set()
        self.DDL_Table18 = DDL_Table18 if DDL_Table18 is not None else set()
        self.DDL_Table = DDL_Table
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def commentTable(self):
        return self.__commentTable

    @commentTable.setter
    def commentTable(self, commentTable: str):
        self.__commentTable = commentTable


    @property
    def DDL_Table18(self):
        return self.__DDL_Table18

    @DDL_Table18.setter
    def DDL_Table18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Table__DDL_Table18", None)
        self.__DDL_Table18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_Ck19"):
                    opp_val = getattr(item, "DDL_Ck19", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_Ck19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_Ck19"):
                    opp_val = getattr(item, "DDL_Ck19", None)
                    
                    setattr(item, "DDL_Ck19", self)
                    

    @property
    def DDL_Table(self):
        return self.__DDL_Table

    @DDL_Table.setter
    def DDL_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Table__DDL_Table", None)
        self.__DDL_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Fk"):
                opp_val = getattr(old_value, "DDL_Fk", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Fk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Fk"):
                opp_val = getattr(value, "DDL_Fk", None)
                setattr(value, "DDL_Fk", self)

    @property
    def DDL_Table10(self):
        return self.__DDL_Table10

    @DDL_Table10.setter
    def DDL_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Table__DDL_Table10", None)
        self.__DDL_Table10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_Column11"):
                    opp_val = getattr(item, "DDL_Column11", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_Column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_Column11"):
                    opp_val = getattr(item, "DDL_Column11", None)
                    
                    setattr(item, "DDL_Column11", self)
                    

    @property
    def DDL_Table13(self):
        return self.__DDL_Table13

    @DDL_Table13.setter
    def DDL_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Table__DDL_Table13", None)
        self.__DDL_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Pk"):
                opp_val = getattr(old_value, "DDL_Pk", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Pk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Pk"):
                opp_val = getattr(value, "DDL_Pk", None)
                setattr(value, "DDL_Pk", self)

    @property
    def DDL_Table15(self):
        return self.__DDL_Table15

    @DDL_Table15.setter
    def DDL_Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Table__DDL_Table15", None)
        self.__DDL_Table15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_Fk16"):
                    opp_val = getattr(item, "DDL_Fk16", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_Fk16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_Fk16"):
                    opp_val = getattr(item, "DDL_Fk16", None)
                    
                    setattr(item, "DDL_Fk16", self)
                    

class DDL_CommentTable(DataDefinition):

    def __init__(self, tableName: str, tableComment: str):
        self.tableName = tableName
        self.tableComment = tableComment
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def tableComment(self):
        return self.__tableComment

    @tableComment.setter
    def tableComment(self, tableComment: str):
        self.__tableComment = tableComment


class DDL_CommentColumn(DataDefinition):

    def __init__(self, tableName: str, columnName: str, columnComment: str):
        self.tableName = tableName
        self.columnName = columnName
        self.columnComment = columnComment
        
        pass
    @property
    def columnComment(self):
        return self.__columnComment

    @columnComment.setter
    def columnComment(self, columnComment: str):
        self.__columnComment = columnComment


    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


class DDL_Database(DataDefinition):

    def __init__(self, databaseName: str):
        self.databaseName = databaseName
        
        pass
    @property
    def databaseName(self):
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName


class DDL_Column:

    def __init__(self, columnName: str, commentColumn: str, columnNull: bool, DDL_Column: "DDL_Type" = None, DDL_Column11: "DDL_Table" = None):
        self.columnName = columnName
        self.commentColumn = commentColumn
        self.columnNull = columnNull
        self.DDL_Column = DDL_Column
        self.DDL_Column11 = DDL_Column11
        
        pass
    @property
    def columnNull(self):
        return self.__columnNull

    @columnNull.setter
    def columnNull(self, columnNull: bool):
        self.__columnNull = columnNull


    @property
    def commentColumn(self):
        return self.__commentColumn

    @commentColumn.setter
    def commentColumn(self, commentColumn: str):
        self.__commentColumn = commentColumn


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def DDL_Column11(self):
        return self.__DDL_Column11

    @DDL_Column11.setter
    def DDL_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Column__DDL_Column11", None)
        self.__DDL_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table10"):
                opp_val = getattr(old_value, "DDL_Table10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table10"):
                opp_val = getattr(value, "DDL_Table10", None)
                if opp_val is None:
                    setattr(value, "DDL_Table10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DDL_Column(self):
        return self.__DDL_Column

    @DDL_Column.setter
    def DDL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Column__DDL_Column", None)
        self.__DDL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Type8"):
                opp_val = getattr(old_value, "DDL_Type8", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Type8"):
                opp_val = getattr(value, "DDL_Type8", None)
                setattr(value, "DDL_Type8", self)

class DDL_Type:

    def __init__(self, name: str, DDL_Type8: "DDL_Column" = None, DDL_Type: "DDL_DataType" = None):
        self.name = name
        self.DDL_Type8 = DDL_Type8
        self.DDL_Type = DDL_Type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def DDL_Type8(self):
        return self.__DDL_Type8

    @DDL_Type8.setter
    def DDL_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Type__DDL_Type8", None)
        self.__DDL_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Column"):
                opp_val = getattr(old_value, "DDL_Column", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Column"):
                opp_val = getattr(value, "DDL_Column", None)
                setattr(value, "DDL_Column", self)

    @property
    def DDL_Type(self):
        return self.__DDL_Type

    @DDL_Type.setter
    def DDL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Type__DDL_Type", None)
        self.__DDL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_DataType"):
                opp_val = getattr(old_value, "DDL_DataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_DataType"):
                opp_val = getattr(value, "DDL_DataType", None)
                if opp_val is None:
                    setattr(value, "DDL_DataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_DataType:

    pass
class Statement:

    pass
class DDL_DataDefinition(Statement):

    pass
class DDL_Statement:

    pass
class Binaries:

    pass
class DDL_Blob(Binaries):

    pass
class DDL_BFile(Binaries):

    pass
class DDL_BinaryFloat(Binaries):

    pass
class DDL_BinaryDouble(Binaries):

    pass
class Intervals:

    pass
class DDL_DayTime(Intervals):

    pass
class DDL_YearMonth(Intervals):

    pass
class Aproximado:

    pass
class DDL_DoublePrecision(Aproximado):

    pass
class DDL_LongRaw(Aproximado):

    pass
class DDL_Float(Aproximado):

    def __init__(self, precision: int):
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


class DDL_Long(Aproximado):

    pass
class DDL_Real(Aproximado):

    pass
class Exacto:

    pass
class DDL_Decimal(Exacto):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


class DDL_SmallInteger(Exacto):

    pass
class DDL_Int(Exacto):

    pass
class DDL_SmallInt(Exacto):

    pass
class DDL_Numeric(Exacto):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


class DDL_Number(Exacto):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


class DDL_Integer(Exacto):

    pass
class Type:

    pass
class DDL_Intervals(Type):

    pass
class DDL_Aproximado(Type):

    pass
class DDL_Binaries(Type):

    pass
class DDL_Characters(Type):

    def __init__(self, n: str):
        self.n = n
        
        pass
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n


class DDL_Exacto(Type):

    pass
class Times:

    pass
class DDL_Timestamp(Times):

    def __init__(self, precision: int):
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


class DDL_Time(Times):

    pass
class DDL_Date(Times):

    pass
class DDL_Times(Type):

    pass
class Bit:

    pass
class DDL_BitVarying(Bit):

    pass
class Bits:

    pass
class DDL_Bit(Bits):

    pass
class DDL_Bits(Type):

    def __init__(self, n: str):
        self.n = n
        
        pass
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n


class DDL_NClob(Characters):

    pass
class DDL_Clob(Characters):

    pass
class DDL_NCharVarying(Characters):

    pass
class DDL_NationalCharacterVarying(Characters):

    pass
class DDL_NationalCharacter(Characters):

    pass
class DDL_NationalCharVarying(Characters):

    pass
class DDL_NationalChar(Characters):

    pass