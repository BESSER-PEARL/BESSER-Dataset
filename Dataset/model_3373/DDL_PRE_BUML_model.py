####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
DDL_Statement = Class(name="DDL::Statement")
DDL_DataDefinition = Class(name="DDL::DataDefinition")
Statement = Class(name="Statement")
DDL_DataType = Class(name="DDL::DataType")
DDL_Type = Class(name="DDL::Type")
DDL_DDLDefinition = Class(name="DDL::DDLDefinition")
DDL_Pk = Class(name="DDL::Pk")
DDL_Fk = Class(name="DDL::Fk")
DDL_Table = Class(name="DDL::Table")
DDL_Ck = Class(name="DDL::Ck")
DDL_ValuesCk = Class(name="DDL::ValuesCk")
DDL_Database = Class(name="DDL::Database")
DataDefinition = Class(name="DataDefinition")
DDL_CommentTable = Class(name="DDL::CommentTable")
DDL_Column = Class(name="DDL::Column")
DDL_Exacto = Class(name="DDL::Exacto")
Type = Class(name="Type")
DDL_Integer = Class(name="DDL::Integer")
Exacto = Class(name="Exacto")
DDL_SmallInteger = Class(name="DDL::SmallInteger")
DDL_Int = Class(name="DDL::Int")
DDL_SmallInt = Class(name="DDL::SmallInt")
DDL_Number = Class(name="DDL::Number")
DDL_Numeric = Class(name="DDL::Numeric")
DDL_Decimal = Class(name="DDL::Decimal")
DDL_CommentColumn = Class(name="DDL::CommentColumn")
DDL_Real = Class(name="DDL::Real")
Aproximado = Class(name="Aproximado")
DDL_DoublePrecision = Class(name="DDL::DoublePrecision")
DDL_Float = Class(name="DDL::Float")
DDL_Long = Class(name="DDL::Long")
DDL_LongRaw = Class(name="DDL::LongRaw")
DDL_Characters = Class(name="DDL::Characters")
DDL_Character = Class(name="DDL::Character")
Characters = Class(name="Characters")
DDL_CharacterVarying = Class(name="DDL::CharacterVarying")
DDL_Char = Class(name="DDL::Char")
DDL_VarChar = Class(name="DDL::VarChar")
DDL_VarChar2 = Class(name="DDL::VarChar2")
DDL_NVarChar2 = Class(name="DDL::NVarChar2")
DDL_NChar = Class(name="DDL::NChar")
DDL_Aproximado = Class(name="DDL::Aproximado")
DDL_NationalCharVarying = Class(name="DDL::NationalCharVarying")
DDL_NationalCharacter = Class(name="DDL::NationalCharacter")
DDL_NationalCharacterVarying = Class(name="DDL::NationalCharacterVarying")
DDL_NCharVarying = Class(name="DDL::NCharVarying")
DDL_Clob = Class(name="DDL::Clob")
DDL_NClob = Class(name="DDL::NClob")
DDL_Bits = Class(name="DDL::Bits")
DDL_Bit = Class(name="DDL::Bit")
Bits = Class(name="Bits")
DDL_BitVarying = Class(name="DDL::BitVarying")
Bit = Class(name="Bit")
DDL_Times = Class(name="DDL::Times")
DDL_Date = Class(name="DDL::Date")
Times = Class(name="Times")
DDL_Time = Class(name="DDL::Time")
DDL_Timestamp = Class(name="DDL::Timestamp")
DDL_CharVarying = Class(name="DDL::CharVarying")
DDL_NationalChar = Class(name="DDL::NationalChar")
DDL_YearMonth = Class(name="DDL::YearMonth")
Intervals = Class(name="Intervals")
DDL_DayTime = Class(name="DDL::DayTime")
DDL_Binaries = Class(name="DDL::Binaries")
DDL_BinaryDouble = Class(name="DDL::BinaryDouble")
Binaries = Class(name="Binaries")
DDL_BinaryFloat = Class(name="DDL::BinaryFloat")
DDL_BFile = Class(name="DDL::BFile")
DDL_Blob = Class(name="DDL::Blob")
DDL_Intervals = Class(name="DDL::Intervals")

# DDL_Statement class attributes and methods

# DDL_DataDefinition class attributes and methods

# Statement class attributes and methods

# DDL_DataType class attributes and methods

# DDL_Type class attributes and methods
DDL_Type_name: Property = Property(name="name", type=StringType)
DDL_Type.attributes={DDL_Type_name}

# DDL_DDLDefinition class attributes and methods

# DDL_Pk class attributes and methods
DDL_Pk_namePk: Property = Property(name="namePk", type=StringType)
DDL_Pk_columnName: Property = Property(name="columnName", type=StringType)
DDL_Pk.attributes={DDL_Pk_namePk, DDL_Pk_columnName}

# DDL_Fk class attributes and methods
DDL_Fk_nameFk: Property = Property(name="nameFk", type=StringType)
DDL_Fk_columnName: Property = Property(name="columnName", type=StringType)
DDL_Fk_columnReference: Property = Property(name="columnReference", type=StringType)
DDL_Fk_status: Property = Property(name="status", type=StringType)
DDL_Fk.attributes={DDL_Fk_columnReference, DDL_Fk_nameFk, DDL_Fk_status, DDL_Fk_columnName}

# DDL_Table class attributes and methods
DDL_Table_tableName: Property = Property(name="tableName", type=StringType)
DDL_Table_commentTable: Property = Property(name="commentTable", type=StringType)
DDL_Table.attributes={DDL_Table_commentTable, DDL_Table_tableName}

# DDL_Ck class attributes and methods
DDL_Ck_nameCk: Property = Property(name="nameCk", type=StringType)
DDL_Ck_status: Property = Property(name="status", type=StringType)
DDL_Ck.attributes={DDL_Ck_status, DDL_Ck_nameCk}

# DDL_ValuesCk class attributes and methods
DDL_ValuesCk_value: Property = Property(name="value", type=StringType)
DDL_ValuesCk_comparator: Property = Property(name="comparator", type=StringType)
DDL_ValuesCk_columnName: Property = Property(name="columnName", type=StringType)
DDL_ValuesCk_logConjuntion: Property = Property(name="logConjuntion", type=StringType)
DDL_ValuesCk.attributes={DDL_ValuesCk_comparator, DDL_ValuesCk_logConjuntion, DDL_ValuesCk_value, DDL_ValuesCk_columnName}

# DDL_Database class attributes and methods
DDL_Database_databaseName: Property = Property(name="databaseName", type=StringType)
DDL_Database.attributes={DDL_Database_databaseName}

# DataDefinition class attributes and methods

# DDL_CommentTable class attributes and methods
DDL_CommentTable_tableName: Property = Property(name="tableName", type=StringType)
DDL_CommentTable_tableComment: Property = Property(name="tableComment", type=StringType)
DDL_CommentTable.attributes={DDL_CommentTable_tableName, DDL_CommentTable_tableComment}

# DDL_Column class attributes and methods
DDL_Column_commentColumn: Property = Property(name="commentColumn", type=StringType)
DDL_Column_columnNull: Property = Property(name="columnNull", type=BooleanType)
DDL_Column_columnName: Property = Property(name="columnName", type=StringType)
DDL_Column.attributes={DDL_Column_commentColumn, DDL_Column_columnName, DDL_Column_columnNull}

# DDL_Exacto class attributes and methods

# Type class attributes and methods

# DDL_Integer class attributes and methods

# Exacto class attributes and methods

# DDL_SmallInteger class attributes and methods

# DDL_Int class attributes and methods

# DDL_SmallInt class attributes and methods

# DDL_Number class attributes and methods
DDL_Number_precision: Property = Property(name="precision", type=IntegerType)
DDL_Number_scale: Property = Property(name="scale", type=IntegerType)
DDL_Number.attributes={DDL_Number_precision, DDL_Number_scale}

# DDL_Numeric class attributes and methods
DDL_Numeric_precision: Property = Property(name="precision", type=IntegerType)
DDL_Numeric_scale: Property = Property(name="scale", type=IntegerType)
DDL_Numeric.attributes={DDL_Numeric_scale, DDL_Numeric_precision}

# DDL_Decimal class attributes and methods
DDL_Decimal_precision: Property = Property(name="precision", type=IntegerType)
DDL_Decimal_scale: Property = Property(name="scale", type=IntegerType)
DDL_Decimal.attributes={DDL_Decimal_scale, DDL_Decimal_precision}

# DDL_CommentColumn class attributes and methods
DDL_CommentColumn_tableName: Property = Property(name="tableName", type=StringType)
DDL_CommentColumn_columnName: Property = Property(name="columnName", type=StringType)
DDL_CommentColumn_columnComment: Property = Property(name="columnComment", type=StringType)
DDL_CommentColumn.attributes={DDL_CommentColumn_columnComment, DDL_CommentColumn_tableName, DDL_CommentColumn_columnName}

# DDL_Real class attributes and methods

# Aproximado class attributes and methods

# DDL_DoublePrecision class attributes and methods

# DDL_Float class attributes and methods
DDL_Float_precision: Property = Property(name="precision", type=IntegerType)
DDL_Float.attributes={DDL_Float_precision}

# DDL_Long class attributes and methods

# DDL_LongRaw class attributes and methods

# DDL_Characters class attributes and methods
DDL_Characters_n: Property = Property(name="n", type=StringType)
DDL_Characters.attributes={DDL_Characters_n}

# DDL_Character class attributes and methods

# Characters class attributes and methods

# DDL_CharacterVarying class attributes and methods

# DDL_Char class attributes and methods

# DDL_VarChar class attributes and methods

# DDL_VarChar2 class attributes and methods

# DDL_NVarChar2 class attributes and methods

# DDL_NChar class attributes and methods

# DDL_Aproximado class attributes and methods

# DDL_NationalCharVarying class attributes and methods

# DDL_NationalCharacter class attributes and methods

# DDL_NationalCharacterVarying class attributes and methods

# DDL_NCharVarying class attributes and methods

# DDL_Clob class attributes and methods

# DDL_NClob class attributes and methods

# DDL_Bits class attributes and methods
DDL_Bits_n: Property = Property(name="n", type=StringType)
DDL_Bits.attributes={DDL_Bits_n}

# DDL_Bit class attributes and methods

# Bits class attributes and methods

# DDL_BitVarying class attributes and methods

# Bit class attributes and methods

# DDL_Times class attributes and methods

# DDL_Date class attributes and methods

# Times class attributes and methods

# DDL_Time class attributes and methods

# DDL_Timestamp class attributes and methods
DDL_Timestamp_precision: Property = Property(name="precision", type=IntegerType)
DDL_Timestamp.attributes={DDL_Timestamp_precision}

# DDL_CharVarying class attributes and methods

# DDL_NationalChar class attributes and methods

# DDL_YearMonth class attributes and methods

# Intervals class attributes and methods

# DDL_DayTime class attributes and methods

# DDL_Binaries class attributes and methods

# DDL_BinaryDouble class attributes and methods

# Binaries class attributes and methods

# DDL_BinaryFloat class attributes and methods

# DDL_BFile class attributes and methods

# DDL_Blob class attributes and methods

# DDL_Intervals class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="DDL_Type", type=DDL_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_DataType", type=DDL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="DDL_Table", type=DDL_Fk, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Fk", type=DDL_Table, multiplicity=Multiplicity(0, 1))
    }
)
valuesCk6: BinaryAssociation = BinaryAssociation(
    name="valuesCk6",
    ends={
        Property(name="DDL_ValuesCk", type=DDL_Ck, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Ck", type=DDL_ValuesCk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="DDL_Statement", type=DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_DDLDefinition", type=DDL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType2: BinaryAssociation = BinaryAssociation(
    name="dataType2",
    ends={
        Property(name="DDL_DataType4", type=DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_DDLDefinition3", type=DDL_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnType7: BinaryAssociation = BinaryAssociation(
    name="columnType7",
    ends={
        Property(name="DDL_Type8", type=DDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Column", type=DDL_Type, multiplicity=Multiplicity(1, 1))
    }
)
columns9: BinaryAssociation = BinaryAssociation(
    name="columns9",
    ends={
        Property(name="DDL_Column11", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table10", type=DDL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnsPk12: BinaryAssociation = BinaryAssociation(
    name="columnsPk12",
    ends={
        Property(name="DDL_Pk", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table13", type=DDL_Pk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnsFk14: BinaryAssociation = BinaryAssociation(
    name="columnsFk14",
    ends={
        Property(name="DDL_Fk16", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table15", type=DDL_Fk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks17: BinaryAssociation = BinaryAssociation(
    name="checks17",
    ends={
        Property(name="DDL_Ck19", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table18", type=DDL_Ck, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_DDL_DataDefinition_Statement = Generalization(general=Statement, specific=DDL_DataDefinition)
gen_DDL_Database_DataDefinition = Generalization(general=DataDefinition, specific=DDL_Database)
gen_DDL_Table_DataDefinition = Generalization(general=DataDefinition, specific=DDL_Table)
gen_DDL_CommentTable_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CommentTable)
gen_DDL_Exacto_Type = Generalization(general=Type, specific=DDL_Exacto)
gen_DDL_Integer_Exacto = Generalization(general=Exacto, specific=DDL_Integer)
gen_DDL_SmallInteger_Exacto = Generalization(general=Exacto, specific=DDL_SmallInteger)
gen_DDL_Int_Exacto = Generalization(general=Exacto, specific=DDL_Int)
gen_DDL_SmallInt_Exacto = Generalization(general=Exacto, specific=DDL_SmallInt)
gen_DDL_Number_Exacto = Generalization(general=Exacto, specific=DDL_Number)
gen_DDL_Numeric_Exacto = Generalization(general=Exacto, specific=DDL_Numeric)
gen_DDL_Decimal_Exacto = Generalization(general=Exacto, specific=DDL_Decimal)
gen_DDL_CommentColumn_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CommentColumn)
gen_DDL_Real_Aproximado = Generalization(general=Aproximado, specific=DDL_Real)
gen_DDL_DoublePrecision_Aproximado = Generalization(general=Aproximado, specific=DDL_DoublePrecision)
gen_DDL_Float_Aproximado = Generalization(general=Aproximado, specific=DDL_Float)
gen_DDL_Long_Aproximado = Generalization(general=Aproximado, specific=DDL_Long)
gen_DDL_LongRaw_Aproximado = Generalization(general=Aproximado, specific=DDL_LongRaw)
gen_DDL_Characters_Type = Generalization(general=Type, specific=DDL_Characters)
gen_DDL_Character_Characters = Generalization(general=Characters, specific=DDL_Character)
gen_DDL_CharacterVarying_Characters = Generalization(general=Characters, specific=DDL_CharacterVarying)
gen_DDL_Char_Characters = Generalization(general=Characters, specific=DDL_Char)
gen_DDL_VarChar_Characters = Generalization(general=Characters, specific=DDL_VarChar)
gen_DDL_VarChar2_Characters = Generalization(general=Characters, specific=DDL_VarChar2)
gen_DDL_NVarChar2_Characters = Generalization(general=Characters, specific=DDL_NVarChar2)
gen_DDL_NChar_Characters = Generalization(general=Characters, specific=DDL_NChar)
gen_DDL_Aproximado_Type = Generalization(general=Type, specific=DDL_Aproximado)
gen_DDL_NationalCharVarying_Characters = Generalization(general=Characters, specific=DDL_NationalCharVarying)
gen_DDL_NationalCharacter_Characters = Generalization(general=Characters, specific=DDL_NationalCharacter)
gen_DDL_NationalCharacterVarying_Characters = Generalization(general=Characters, specific=DDL_NationalCharacterVarying)
gen_DDL_NCharVarying_Characters = Generalization(general=Characters, specific=DDL_NCharVarying)
gen_DDL_Clob_Characters = Generalization(general=Characters, specific=DDL_Clob)
gen_DDL_NClob_Characters = Generalization(general=Characters, specific=DDL_NClob)
gen_DDL_Bits_Type = Generalization(general=Type, specific=DDL_Bits)
gen_DDL_Bit_Bits = Generalization(general=Bits, specific=DDL_Bit)
gen_DDL_BitVarying_Bit = Generalization(general=Bit, specific=DDL_BitVarying)
gen_DDL_Times_Type = Generalization(general=Type, specific=DDL_Times)
gen_DDL_Date_Times = Generalization(general=Times, specific=DDL_Date)
gen_DDL_Time_Times = Generalization(general=Times, specific=DDL_Time)
gen_DDL_Timestamp_Times = Generalization(general=Times, specific=DDL_Timestamp)
gen_DDL_CharVarying_Characters = Generalization(general=Characters, specific=DDL_CharVarying)
gen_DDL_NationalChar_Characters = Generalization(general=Characters, specific=DDL_NationalChar)
gen_DDL_YearMonth_Intervals = Generalization(general=Intervals, specific=DDL_YearMonth)
gen_DDL_DayTime_Intervals = Generalization(general=Intervals, specific=DDL_DayTime)
gen_DDL_Binaries_Type = Generalization(general=Type, specific=DDL_Binaries)
gen_DDL_BinaryDouble_Binaries = Generalization(general=Binaries, specific=DDL_BinaryDouble)
gen_DDL_BinaryFloat_Binaries = Generalization(general=Binaries, specific=DDL_BinaryFloat)
gen_DDL_BFile_Binaries = Generalization(general=Binaries, specific=DDL_BFile)
gen_DDL_Blob_Binaries = Generalization(general=Binaries, specific=DDL_Blob)
gen_DDL_Intervals_Type = Generalization(general=Type, specific=DDL_Intervals)

# Domain Model
domain_model = DomainModel(
    name="DDL",
    types={DDL_Statement, DDL_DataDefinition, Statement, DDL_DataType, DDL_Type, DDL_DDLDefinition, DDL_Pk, DDL_Fk, DDL_Table, DDL_Ck, DDL_ValuesCk, DDL_Database, DataDefinition, DDL_CommentTable, DDL_Column, DDL_Exacto, Type, DDL_Integer, Exacto, DDL_SmallInteger, DDL_Int, DDL_SmallInt, DDL_Number, DDL_Numeric, DDL_Decimal, DDL_CommentColumn, DDL_Real, Aproximado, DDL_DoublePrecision, DDL_Float, DDL_Long, DDL_LongRaw, DDL_Characters, DDL_Character, Characters, DDL_CharacterVarying, DDL_Char, DDL_VarChar, DDL_VarChar2, DDL_NVarChar2, DDL_NChar, DDL_Aproximado, DDL_NationalCharVarying, DDL_NationalCharacter, DDL_NationalCharacterVarying, DDL_NCharVarying, DDL_Clob, DDL_NClob, DDL_Bits, DDL_Bit, Bits, DDL_BitVarying, Bit, DDL_Times, DDL_Date, Times, DDL_Time, DDL_Timestamp, DDL_CharVarying, DDL_NationalChar, DDL_YearMonth, Intervals, DDL_DayTime, DDL_Binaries, DDL_BinaryDouble, Binaries, DDL_BinaryFloat, DDL_BFile, DDL_Blob, DDL_Intervals},
    associations={types0, references5, valuesCk6, statements1, dataType2, columnType7, columns9, columnsPk12, columnsFk14, checks17},
    generalizations={gen_DDL_DataDefinition_Statement, gen_DDL_Database_DataDefinition, gen_DDL_Table_DataDefinition, gen_DDL_CommentTable_DataDefinition, gen_DDL_Exacto_Type, gen_DDL_Integer_Exacto, gen_DDL_SmallInteger_Exacto, gen_DDL_Int_Exacto, gen_DDL_SmallInt_Exacto, gen_DDL_Number_Exacto, gen_DDL_Numeric_Exacto, gen_DDL_Decimal_Exacto, gen_DDL_CommentColumn_DataDefinition, gen_DDL_Real_Aproximado, gen_DDL_DoublePrecision_Aproximado, gen_DDL_Float_Aproximado, gen_DDL_Long_Aproximado, gen_DDL_LongRaw_Aproximado, gen_DDL_Characters_Type, gen_DDL_Character_Characters, gen_DDL_CharacterVarying_Characters, gen_DDL_Char_Characters, gen_DDL_VarChar_Characters, gen_DDL_VarChar2_Characters, gen_DDL_NVarChar2_Characters, gen_DDL_NChar_Characters, gen_DDL_Aproximado_Type, gen_DDL_NationalCharVarying_Characters, gen_DDL_NationalCharacter_Characters, gen_DDL_NationalCharacterVarying_Characters, gen_DDL_NCharVarying_Characters, gen_DDL_Clob_Characters, gen_DDL_NClob_Characters, gen_DDL_Bits_Type, gen_DDL_Bit_Bits, gen_DDL_BitVarying_Bit, gen_DDL_Times_Type, gen_DDL_Date_Times, gen_DDL_Time_Times, gen_DDL_Timestamp_Times, gen_DDL_CharVarying_Characters, gen_DDL_NationalChar_Characters, gen_DDL_YearMonth_Intervals, gen_DDL_DayTime_Intervals, gen_DDL_Binaries_Type, gen_DDL_BinaryDouble_Binaries, gen_DDL_BinaryFloat_Binaries, gen_DDL_BFile_Binaries, gen_DDL_Blob_Binaries, gen_DDL_Intervals_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)