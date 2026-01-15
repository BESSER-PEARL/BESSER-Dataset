from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Bits:

    pass
class Binaries:

    pass
class DML_DDL_Blob(Binaries):

    pass
class DML_DDL_BinaryFloat(Binaries):

    pass
class DML_DDL_BFile(Binaries):

    pass
class DML_DDL_BinaryDouble(Binaries):

    pass
class Intervals:

    pass
class DML_DDL_DayTime(Intervals):

    pass
class DML_DDL_YearMonth(Intervals):

    pass
class Times:

    pass
class DML_DDL_Timestamp(Times):

    pass
class DML_DDL_Time(Times):

    pass
class DML_DDL_Date(Times):

    pass
class Bit:

    pass
class DML_DDL_BitVarying(Bit):

    pass
class DML_DDL_Bit(Bits):

    pass
class Characters:

    pass
class DML_DDL_Clob(Characters):

    pass
class DML_DDL_NVarChar2(Characters):

    pass
class DML_DDL_CharacterVarying(Characters):

    pass
class DML_DDL_NChar(Characters):

    pass
class DML_DDL_VarChar(Characters):

    pass
class DML_DDL_NClob(Characters):

    pass
class DML_DDL_NationalCharVarying(Characters):

    pass
class DML_DDL_NationalChar(Characters):

    pass
class DML_DDL_CharVarying(Characters):

    pass
class DML_DDL_Text(Characters):

    pass
class DML_DDL_NCharVarying(Characters):

    pass
class DML_DDL_NationalCharacterVarying(Characters):

    pass
class DML_DDL_Char(Characters):

    pass
class DML_DDL_VarChar2(Characters):

    pass
class DML_DDL_NationalCharacter(Characters):

    pass
class DML_DDL_Character(Characters):

    pass
class Aproximado:

    pass
class DML_DDL_DoublePrecision(Aproximado):

    pass
class DML_DDL_Long(Aproximado):

    pass
class DML_DDL_Float(Aproximado):

    pass
class DML_DDL_LongRaw(Aproximado):

    pass
class DML_DDL_Real(Aproximado):

    pass
class Exacto:

    pass
class DML_DDL_SmallInt(Exacto):

    pass
class DML_DDL_Decimal(Exacto):

    pass
class DML_DDL_SmallInteger(Exacto):

    pass
class DML_DDL_Int(Exacto):

    pass
class DML_DDL_Number(Exacto):

    pass
class DML_DDL_Numeric(Exacto):

    pass
class DML_DDL_Integer(Exacto):

    pass
class Type:

    pass
class DML_DDL_Binaries(Type):

    pass
class DML_DDL_Times(Type):

    pass
class DML_DDL_Aproximado(Type):

    pass
class DML_DDL_Bits(Type):

    def __init__(self, n: str):
        self.n = n
        
    @property
    def n(self) -> str:
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n

class DML_DDL_Exacto(Type):

    pass
class DML_DDL_Characters(Type):

    def __init__(self, n: str):
        self.n = n
        
    @property
    def n(self) -> str:
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n

class DML_DDL_Intervals(Type):

    pass
class DML_DDL_Value:

    def __init__(self, value: str, DML_DDL_Value: "DML_DDL_Registry" = None, DML_DDL_Value25: "DML_DDL_Column" = None):
        self.value = value
        self.DML_DDL_Value = DML_DDL_Value
        self.DML_DDL_Value25 = DML_DDL_Value25
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def DML_DDL_Value25(self):
        return self.__DML_DDL_Value25

    @DML_DDL_Value25.setter
    def DML_DDL_Value25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Value__DML_DDL_Value25", None)
        self.__DML_DDL_Value25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Column26"):
                opp_val = getattr(old_value, "DML_DDL_Column26", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Column26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Column26"):
                opp_val = getattr(value, "DML_DDL_Column26", None)
                setattr(value, "DML_DDL_Column26", self)

    @property
    def DML_DDL_Value(self):
        return self.__DML_DDL_Value

    @DML_DDL_Value.setter
    def DML_DDL_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Value__DML_DDL_Value", None)
        self.__DML_DDL_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Registry23"):
                opp_val = getattr(old_value, "DML_DDL_Registry23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Registry23"):
                opp_val = getattr(value, "DML_DDL_Registry23", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_Registry23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_DDL_Registry:

    pass
class DataDefinition:

    pass
class DML_DDL_CommentColumn(DataDefinition):

    def __init__(self, tableName: str, columnName: str, columnComment: str):
        self.tableName = tableName
        self.columnName = columnName
        self.columnComment = columnComment
        
    @property
    def columnComment(self) -> str:
        return self.__columnComment

    @columnComment.setter
    def columnComment(self, columnComment: str):
        self.__columnComment = columnComment

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

class DML_DDL_CommentTable(DataDefinition):

    def __init__(self, tableName: str, tableComment: str):
        self.tableName = tableName
        self.tableComment = tableComment
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def tableComment(self) -> str:
        return self.__tableComment

    @tableComment.setter
    def tableComment(self, tableComment: str):
        self.__tableComment = tableComment

class DML_DDL_Database(DataDefinition):

    def __init__(self, databaseName: str):
        self.databaseName = databaseName
        
    @property
    def databaseName(self) -> str:
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName

class DML_DDL_Column:

    def __init__(self, columnName: str, commentColumn: str, columnNull: bool, precision: int, scale: int, DML_DDL_Column: "DML_DDL_Type" = None, DML_DDL_Column11: "DML_DDL_Table" = None, DML_DDL_Column26: "DML_DDL_Value" = None):
        self.columnName = columnName
        self.commentColumn = commentColumn
        self.columnNull = columnNull
        self.precision = precision
        self.scale = scale
        self.DML_DDL_Column = DML_DDL_Column
        self.DML_DDL_Column11 = DML_DDL_Column11
        self.DML_DDL_Column26 = DML_DDL_Column26
        
    @property
    def columnNull(self) -> bool:
        return self.__columnNull

    @columnNull.setter
    def columnNull(self, columnNull: bool):
        self.__columnNull = columnNull

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def commentColumn(self) -> str:
        return self.__commentColumn

    @commentColumn.setter
    def commentColumn(self, commentColumn: str):
        self.__commentColumn = commentColumn

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def DML_DDL_Column26(self):
        return self.__DML_DDL_Column26

    @DML_DDL_Column26.setter
    def DML_DDL_Column26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Column__DML_DDL_Column26", None)
        self.__DML_DDL_Column26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Value25"):
                opp_val = getattr(old_value, "DML_DDL_Value25", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Value25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Value25"):
                opp_val = getattr(value, "DML_DDL_Value25", None)
                setattr(value, "DML_DDL_Value25", self)

    @property
    def DML_DDL_Column(self):
        return self.__DML_DDL_Column

    @DML_DDL_Column.setter
    def DML_DDL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Column__DML_DDL_Column", None)
        self.__DML_DDL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Type8"):
                opp_val = getattr(old_value, "DML_DDL_Type8", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Type8"):
                opp_val = getattr(value, "DML_DDL_Type8", None)
                setattr(value, "DML_DDL_Type8", self)

    @property
    def DML_DDL_Column11(self):
        return self.__DML_DDL_Column11

    @DML_DDL_Column11.setter
    def DML_DDL_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Column__DML_DDL_Column11", None)
        self.__DML_DDL_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Table10"):
                opp_val = getattr(old_value, "DML_DDL_Table10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Table10"):
                opp_val = getattr(value, "DML_DDL_Table10", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_Table10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_DDL_ValuesCk:

    def __init__(self, value: str, comparator: str, columnName: str, logConjuntion: str, DML_DDL_ValuesCk: "DML_DDL_Ck" = None):
        self.value = value
        self.comparator = comparator
        self.columnName = columnName
        self.logConjuntion = logConjuntion
        self.DML_DDL_ValuesCk = DML_DDL_ValuesCk
        
    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def logConjuntion(self) -> str:
        return self.__logConjuntion

    @logConjuntion.setter
    def logConjuntion(self, logConjuntion: str):
        self.__logConjuntion = logConjuntion

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def DML_DDL_ValuesCk(self):
        return self.__DML_DDL_ValuesCk

    @DML_DDL_ValuesCk.setter
    def DML_DDL_ValuesCk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_ValuesCk__DML_DDL_ValuesCk", None)
        self.__DML_DDL_ValuesCk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Ck"):
                opp_val = getattr(old_value, "DML_DDL_Ck", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Ck"):
                opp_val = getattr(value, "DML_DDL_Ck", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_Ck", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_DDL_Statement:

    pass
class DML_DDL_Ck:

    def __init__(self, nameCk: str, status: str, DML_DDL_Ck: set["DML_DDL_ValuesCk"] = None, DML_DDL_Ck19: "DML_DDL_Table" = None):
        self.nameCk = nameCk
        self.status = status
        self.DML_DDL_Ck = DML_DDL_Ck if DML_DDL_Ck is not None else set()
        self.DML_DDL_Ck19 = DML_DDL_Ck19
        
    @property
    def nameCk(self) -> str:
        return self.__nameCk

    @nameCk.setter
    def nameCk(self, nameCk: str):
        self.__nameCk = nameCk

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def DML_DDL_Ck19(self):
        return self.__DML_DDL_Ck19

    @DML_DDL_Ck19.setter
    def DML_DDL_Ck19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Ck__DML_DDL_Ck19", None)
        self.__DML_DDL_Ck19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Table18"):
                opp_val = getattr(old_value, "DML_DDL_Table18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Table18"):
                opp_val = getattr(value, "DML_DDL_Table18", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_Table18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DML_DDL_Ck(self):
        return self.__DML_DDL_Ck

    @DML_DDL_Ck.setter
    def DML_DDL_Ck(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Ck__DML_DDL_Ck", None)
        self.__DML_DDL_Ck = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_DDL_ValuesCk"):
                    opp_val = getattr(item, "DML_DDL_ValuesCk", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_DDL_ValuesCk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_DDL_ValuesCk"):
                    opp_val = getattr(item, "DML_DDL_ValuesCk", None)
                    
                    setattr(item, "DML_DDL_ValuesCk", self)
                    

class DML_DDL_Table(DataDefinition):

    def __init__(self, tableName: str, commentTable: str, DML_DDL_Table: "DML_DDL_Fk" = None, DML_DDL_Table10: set["DML_DDL_Column"] = None, DML_DDL_Table15: set["DML_DDL_Fk"] = None, DML_DDL_Table18: set["DML_DDL_Ck"] = None, DML_DDL_Table21: set["DML_DDL_Registry"] = None, DML_DDL_Table13: "DML_DDL_Pk" = None):
        self.tableName = tableName
        self.commentTable = commentTable
        self.DML_DDL_Table = DML_DDL_Table
        self.DML_DDL_Table10 = DML_DDL_Table10 if DML_DDL_Table10 is not None else set()
        self.DML_DDL_Table15 = DML_DDL_Table15 if DML_DDL_Table15 is not None else set()
        self.DML_DDL_Table18 = DML_DDL_Table18 if DML_DDL_Table18 is not None else set()
        self.DML_DDL_Table21 = DML_DDL_Table21 if DML_DDL_Table21 is not None else set()
        self.DML_DDL_Table13 = DML_DDL_Table13
        
    @property
    def commentTable(self) -> str:
        return self.__commentTable

    @commentTable.setter
    def commentTable(self, commentTable: str):
        self.__commentTable = commentTable

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def DML_DDL_Table10(self):
        return self.__DML_DDL_Table10

    @DML_DDL_Table10.setter
    def DML_DDL_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table10", None)
        self.__DML_DDL_Table10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_DDL_Column11"):
                    opp_val = getattr(item, "DML_DDL_Column11", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_DDL_Column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_DDL_Column11"):
                    opp_val = getattr(item, "DML_DDL_Column11", None)
                    
                    setattr(item, "DML_DDL_Column11", self)
                    

    @property
    def DML_DDL_Table13(self):
        return self.__DML_DDL_Table13

    @DML_DDL_Table13.setter
    def DML_DDL_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table13", None)
        self.__DML_DDL_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Pk"):
                opp_val = getattr(old_value, "DML_DDL_Pk", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Pk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Pk"):
                opp_val = getattr(value, "DML_DDL_Pk", None)
                setattr(value, "DML_DDL_Pk", self)

    @property
    def DML_DDL_Table15(self):
        return self.__DML_DDL_Table15

    @DML_DDL_Table15.setter
    def DML_DDL_Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table15", None)
        self.__DML_DDL_Table15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_DDL_Fk16"):
                    opp_val = getattr(item, "DML_DDL_Fk16", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_DDL_Fk16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_DDL_Fk16"):
                    opp_val = getattr(item, "DML_DDL_Fk16", None)
                    
                    setattr(item, "DML_DDL_Fk16", self)
                    

    @property
    def DML_DDL_Table(self):
        return self.__DML_DDL_Table

    @DML_DDL_Table.setter
    def DML_DDL_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table", None)
        self.__DML_DDL_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Fk"):
                opp_val = getattr(old_value, "DML_DDL_Fk", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Fk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Fk"):
                opp_val = getattr(value, "DML_DDL_Fk", None)
                setattr(value, "DML_DDL_Fk", self)

    @property
    def DML_DDL_Table21(self):
        return self.__DML_DDL_Table21

    @DML_DDL_Table21.setter
    def DML_DDL_Table21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table21", None)
        self.__DML_DDL_Table21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_DDL_Registry"):
                    opp_val = getattr(item, "DML_DDL_Registry", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_DDL_Registry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_DDL_Registry"):
                    opp_val = getattr(item, "DML_DDL_Registry", None)
                    
                    setattr(item, "DML_DDL_Registry", self)
                    

    @property
    def DML_DDL_Table18(self):
        return self.__DML_DDL_Table18

    @DML_DDL_Table18.setter
    def DML_DDL_Table18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Table__DML_DDL_Table18", None)
        self.__DML_DDL_Table18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_DDL_Ck19"):
                    opp_val = getattr(item, "DML_DDL_Ck19", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_DDL_Ck19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_DDL_Ck19"):
                    opp_val = getattr(item, "DML_DDL_Ck19", None)
                    
                    setattr(item, "DML_DDL_Ck19", self)
                    

class DML_DDL_Fk:

    def __init__(self, nameFk: str, columnName: str, columnReference: str, status: str, DML_DDL_Fk: "DML_DDL_Table" = None, DML_DDL_Fk16: "DML_DDL_Table" = None):
        self.nameFk = nameFk
        self.columnName = columnName
        self.columnReference = columnReference
        self.status = status
        self.DML_DDL_Fk = DML_DDL_Fk
        self.DML_DDL_Fk16 = DML_DDL_Fk16
        
    @property
    def nameFk(self) -> str:
        return self.__nameFk

    @nameFk.setter
    def nameFk(self, nameFk: str):
        self.__nameFk = nameFk

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def columnReference(self) -> str:
        return self.__columnReference

    @columnReference.setter
    def columnReference(self, columnReference: str):
        self.__columnReference = columnReference

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DML_DDL_Fk(self):
        return self.__DML_DDL_Fk

    @DML_DDL_Fk.setter
    def DML_DDL_Fk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Fk__DML_DDL_Fk", None)
        self.__DML_DDL_Fk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Table"):
                opp_val = getattr(old_value, "DML_DDL_Table", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Table"):
                opp_val = getattr(value, "DML_DDL_Table", None)
                setattr(value, "DML_DDL_Table", self)

    @property
    def DML_DDL_Fk16(self):
        return self.__DML_DDL_Fk16

    @DML_DDL_Fk16.setter
    def DML_DDL_Fk16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Fk__DML_DDL_Fk16", None)
        self.__DML_DDL_Fk16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Table15"):
                opp_val = getattr(old_value, "DML_DDL_Table15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Table15"):
                opp_val = getattr(value, "DML_DDL_Table15", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_Table15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_DDL_Pk:

    def __init__(self, namePk: str, columnName: str, DML_DDL_Pk: "DML_DDL_Table" = None):
        self.namePk = namePk
        self.columnName = columnName
        self.DML_DDL_Pk = DML_DDL_Pk
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def namePk(self) -> str:
        return self.__namePk

    @namePk.setter
    def namePk(self, namePk: str):
        self.__namePk = namePk

    @property
    def DML_DDL_Pk(self):
        return self.__DML_DDL_Pk

    @DML_DDL_Pk.setter
    def DML_DDL_Pk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Pk__DML_DDL_Pk", None)
        self.__DML_DDL_Pk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Table13"):
                opp_val = getattr(old_value, "DML_DDL_Table13", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Table13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Table13"):
                opp_val = getattr(value, "DML_DDL_Table13", None)
                setattr(value, "DML_DDL_Table13", self)

class DML_DDL_DDLDefinition:

    pass
class DML_DDL_Type:

    def __init__(self, name: str, DML_DDL_Type: "DML_DDL_DataType" = None, DML_DDL_Type8: "DML_DDL_Column" = None):
        self.name = name
        self.DML_DDL_Type = DML_DDL_Type
        self.DML_DDL_Type8 = DML_DDL_Type8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DML_DDL_Type8(self):
        return self.__DML_DDL_Type8

    @DML_DDL_Type8.setter
    def DML_DDL_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Type__DML_DDL_Type8", None)
        self.__DML_DDL_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_Column"):
                opp_val = getattr(old_value, "DML_DDL_Column", None)
                if opp_val == self:
                    setattr(old_value, "DML_DDL_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_Column"):
                opp_val = getattr(value, "DML_DDL_Column", None)
                setattr(value, "DML_DDL_Column", self)

    @property
    def DML_DDL_Type(self):
        return self.__DML_DDL_Type

    @DML_DDL_Type.setter
    def DML_DDL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_DDL_Type__DML_DDL_Type", None)
        self.__DML_DDL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_DDL_DataType"):
                opp_val = getattr(old_value, "DML_DDL_DataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_DDL_DataType"):
                opp_val = getattr(value, "DML_DDL_DataType", None)
                if opp_val is None:
                    setattr(value, "DML_DDL_DataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_DDL_DataType:

    pass
class Statement:

    pass
class DML_DDL_DataDefinition(Statement):

    pass