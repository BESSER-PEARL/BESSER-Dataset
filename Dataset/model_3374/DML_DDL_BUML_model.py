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
DML_DDL_Statement = Class(name="DML::DDL::Statement")
DML_DDL_DataDefinition = Class(name="DML::DDL::DataDefinition")
Statement = Class(name="Statement")
DML_DDL_DataType = Class(name="DML::DDL::DataType")
DML_DDL_Type = Class(name="DML::DDL::Type")
DML_DDL_DDLDefinition = Class(name="DML::DDL::DDLDefinition")
DML_DDL_Pk = Class(name="DML::DDL::Pk")
DML_DDL_Fk = Class(name="DML::DDL::Fk")
DML_DDL_Table = Class(name="DML::DDL::Table")
DML_DDL_Ck = Class(name="DML::DDL::Ck")
DML_DDL_Database = Class(name="DML::DDL::Database")
DataDefinition = Class(name="DataDefinition")
DML_DDL_Registry = Class(name="DML::DDL::Registry")
DML_DDL_Value = Class(name="DML::DDL::Value")
DML_DDL_CommentTable = Class(name="DML::DDL::CommentTable")
DML_DDL_CommentColumn = Class(name="DML::DDL::CommentColumn")
DML_DDL_Exacto = Class(name="DML::DDL::Exacto")
Type = Class(name="Type")
DML_DDL_Integer = Class(name="DML::DDL::Integer")
Exacto = Class(name="Exacto")
DML_DDL_SmallInteger = Class(name="DML::DDL::SmallInteger")
DML_DDL_Int = Class(name="DML::DDL::Int")
DML_DDL_SmallInt = Class(name="DML::DDL::SmallInt")
DML_DDL_Number = Class(name="DML::DDL::Number")
DML_DDL_Numeric = Class(name="DML::DDL::Numeric")
DML_DDL_Decimal = Class(name="DML::DDL::Decimal")
DML_DDL_ValuesCk = Class(name="DML::DDL::ValuesCk")
DML_DDL_Column = Class(name="DML::DDL::Column")
DML_DDL_Character = Class(name="DML::DDL::Character")
Characters = Class(name="Characters")
DML_DDL_CharacterVarying = Class(name="DML::DDL::CharacterVarying")
DML_DDL_Char = Class(name="DML::DDL::Char")
DML_DDL_VarChar = Class(name="DML::DDL::VarChar")
DML_DDL_VarChar2 = Class(name="DML::DDL::VarChar2")
DML_DDL_NVarChar2 = Class(name="DML::DDL::NVarChar2")
DML_DDL_NChar = Class(name="DML::DDL::NChar")
DML_DDL_CharVarying = Class(name="DML::DDL::CharVarying")
DML_DDL_NationalChar = Class(name="DML::DDL::NationalChar")
DML_DDL_NationalCharVarying = Class(name="DML::DDL::NationalCharVarying")
DML_DDL_NationalCharacter = Class(name="DML::DDL::NationalCharacter")
DML_DDL_NationalCharacterVarying = Class(name="DML::DDL::NationalCharacterVarying")
DML_DDL_NCharVarying = Class(name="DML::DDL::NCharVarying")
DML_DDL_Clob = Class(name="DML::DDL::Clob")
DML_DDL_NClob = Class(name="DML::DDL::NClob")
DML_DDL_Bits = Class(name="DML::DDL::Bits")
DML_DDL_Bit = Class(name="DML::DDL::Bit")
Bits = Class(name="Bits")
DML_DDL_BitVarying = Class(name="DML::DDL::BitVarying")
Bit = Class(name="Bit")
DML_DDL_Times = Class(name="DML::DDL::Times")
DML_DDL_Date = Class(name="DML::DDL::Date")
Times = Class(name="Times")
DML_DDL_Time = Class(name="DML::DDL::Time")
DML_DDL_Timestamp = Class(name="DML::DDL::Timestamp")
DML_DDL_Intervals = Class(name="DML::DDL::Intervals")
DML_DDL_YearMonth = Class(name="DML::DDL::YearMonth")
Intervals = Class(name="Intervals")
DML_DDL_DayTime = Class(name="DML::DDL::DayTime")
DML_DDL_Binaries = Class(name="DML::DDL::Binaries")
DML_DDL_BinaryDouble = Class(name="DML::DDL::BinaryDouble")
Binaries = Class(name="Binaries")
DML_DDL_BinaryFloat = Class(name="DML::DDL::BinaryFloat")
DML_DDL_BFile = Class(name="DML::DDL::BFile")
DML_DDL_Blob = Class(name="DML::DDL::Blob")
DML_DDL_Aproximado = Class(name="DML::DDL::Aproximado")
DML_DDL_Real = Class(name="DML::DDL::Real")
Aproximado = Class(name="Aproximado")
DML_DDL_DoublePrecision = Class(name="DML::DDL::DoublePrecision")
DML_DDL_Float = Class(name="DML::DDL::Float")
DML_DDL_Long = Class(name="DML::DDL::Long")
DML_DDL_LongRaw = Class(name="DML::DDL::LongRaw")
DML_DDL_Characters = Class(name="DML::DDL::Characters")

# DML_DDL_Statement class attributes and methods

# DML_DDL_DataDefinition class attributes and methods

# Statement class attributes and methods

# DML_DDL_DataType class attributes and methods

# DML_DDL_Type class attributes and methods
DML_DDL_Type_name: Property = Property(name="name", type=StringType)
DML_DDL_Type.attributes={DML_DDL_Type_name}

# DML_DDL_DDLDefinition class attributes and methods

# DML_DDL_Pk class attributes and methods
DML_DDL_Pk_namePk: Property = Property(name="namePk", type=StringType)
DML_DDL_Pk_columnName: Property = Property(name="columnName", type=StringType)
DML_DDL_Pk.attributes={DML_DDL_Pk_columnName, DML_DDL_Pk_namePk}

# DML_DDL_Fk class attributes and methods
DML_DDL_Fk_nameFk: Property = Property(name="nameFk", type=StringType)
DML_DDL_Fk_columnName: Property = Property(name="columnName", type=StringType)
DML_DDL_Fk_columnReference: Property = Property(name="columnReference", type=StringType)
DML_DDL_Fk_status: Property = Property(name="status", type=StringType)
DML_DDL_Fk.attributes={DML_DDL_Fk_columnName, DML_DDL_Fk_columnReference, DML_DDL_Fk_status, DML_DDL_Fk_nameFk}

# DML_DDL_Table class attributes and methods
DML_DDL_Table_tableName: Property = Property(name="tableName", type=StringType)
DML_DDL_Table_commentTable: Property = Property(name="commentTable", type=StringType)
DML_DDL_Table.attributes={DML_DDL_Table_commentTable, DML_DDL_Table_tableName}

# DML_DDL_Ck class attributes and methods
DML_DDL_Ck_nameCk: Property = Property(name="nameCk", type=StringType)
DML_DDL_Ck_status: Property = Property(name="status", type=StringType)
DML_DDL_Ck.attributes={DML_DDL_Ck_status, DML_DDL_Ck_nameCk}

# DML_DDL_Database class attributes and methods
DML_DDL_Database_databaseName: Property = Property(name="databaseName", type=StringType)
DML_DDL_Database.attributes={DML_DDL_Database_databaseName}

# DataDefinition class attributes and methods

# DML_DDL_Registry class attributes and methods

# DML_DDL_Value class attributes and methods
DML_DDL_Value_value: Property = Property(name="value", type=StringType)
DML_DDL_Value.attributes={DML_DDL_Value_value}

# DML_DDL_CommentTable class attributes and methods
DML_DDL_CommentTable_tableName: Property = Property(name="tableName", type=StringType)
DML_DDL_CommentTable_tableComment: Property = Property(name="tableComment", type=StringType)
DML_DDL_CommentTable.attributes={DML_DDL_CommentTable_tableName, DML_DDL_CommentTable_tableComment}

# DML_DDL_CommentColumn class attributes and methods
DML_DDL_CommentColumn_tableName: Property = Property(name="tableName", type=StringType)
DML_DDL_CommentColumn_columnName: Property = Property(name="columnName", type=StringType)
DML_DDL_CommentColumn_columnComment: Property = Property(name="columnComment", type=StringType)
DML_DDL_CommentColumn.attributes={DML_DDL_CommentColumn_columnComment, DML_DDL_CommentColumn_columnName, DML_DDL_CommentColumn_tableName}

# DML_DDL_Exacto class attributes and methods

# Type class attributes and methods

# DML_DDL_Integer class attributes and methods

# Exacto class attributes and methods

# DML_DDL_SmallInteger class attributes and methods

# DML_DDL_Int class attributes and methods

# DML_DDL_SmallInt class attributes and methods

# DML_DDL_Number class attributes and methods

# DML_DDL_Numeric class attributes and methods

# DML_DDL_Decimal class attributes and methods

# DML_DDL_ValuesCk class attributes and methods
DML_DDL_ValuesCk_value: Property = Property(name="value", type=StringType)
DML_DDL_ValuesCk_comparator: Property = Property(name="comparator", type=StringType)
DML_DDL_ValuesCk_columnName: Property = Property(name="columnName", type=StringType)
DML_DDL_ValuesCk_logConjuntion: Property = Property(name="logConjuntion", type=StringType)
DML_DDL_ValuesCk.attributes={DML_DDL_ValuesCk_logConjuntion, DML_DDL_ValuesCk_comparator, DML_DDL_ValuesCk_columnName, DML_DDL_ValuesCk_value}

# DML_DDL_Column class attributes and methods
DML_DDL_Column_columnNull: Property = Property(name="columnNull", type=BooleanType)
DML_DDL_Column_columnName: Property = Property(name="columnName", type=StringType)
DML_DDL_Column_commentColumn: Property = Property(name="commentColumn", type=StringType)
DML_DDL_Column.attributes={DML_DDL_Column_columnNull, DML_DDL_Column_commentColumn, DML_DDL_Column_columnName}

# DML_DDL_Character class attributes and methods

# Characters class attributes and methods

# DML_DDL_CharacterVarying class attributes and methods

# DML_DDL_Char class attributes and methods

# DML_DDL_VarChar class attributes and methods

# DML_DDL_VarChar2 class attributes and methods

# DML_DDL_NVarChar2 class attributes and methods

# DML_DDL_NChar class attributes and methods

# DML_DDL_CharVarying class attributes and methods

# DML_DDL_NationalChar class attributes and methods

# DML_DDL_NationalCharVarying class attributes and methods

# DML_DDL_NationalCharacter class attributes and methods

# DML_DDL_NationalCharacterVarying class attributes and methods

# DML_DDL_NCharVarying class attributes and methods

# DML_DDL_Clob class attributes and methods

# DML_DDL_NClob class attributes and methods

# DML_DDL_Bits class attributes and methods
DML_DDL_Bits_n: Property = Property(name="n", type=StringType)
DML_DDL_Bits.attributes={DML_DDL_Bits_n}

# DML_DDL_Bit class attributes and methods

# Bits class attributes and methods

# DML_DDL_BitVarying class attributes and methods

# Bit class attributes and methods

# DML_DDL_Times class attributes and methods

# DML_DDL_Date class attributes and methods

# Times class attributes and methods

# DML_DDL_Time class attributes and methods

# DML_DDL_Timestamp class attributes and methods

# DML_DDL_Intervals class attributes and methods

# DML_DDL_YearMonth class attributes and methods

# Intervals class attributes and methods

# DML_DDL_DayTime class attributes and methods

# DML_DDL_Binaries class attributes and methods

# DML_DDL_BinaryDouble class attributes and methods

# Binaries class attributes and methods

# DML_DDL_BinaryFloat class attributes and methods

# DML_DDL_BFile class attributes and methods

# DML_DDL_Blob class attributes and methods

# DML_DDL_Aproximado class attributes and methods

# DML_DDL_Real class attributes and methods

# Aproximado class attributes and methods

# DML_DDL_DoublePrecision class attributes and methods

# DML_DDL_Float class attributes and methods

# DML_DDL_Long class attributes and methods

# DML_DDL_LongRaw class attributes and methods

# DML_DDL_Characters class attributes and methods
DML_DDL_Characters_n: Property = Property(name="n", type=StringType)
DML_DDL_Characters.attributes={DML_DDL_Characters_n}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="DML_DDL_Type", type=DML_DDL_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_DataType", type=DML_DDL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="DML_DDL_Statement", type=DML_DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_DDLDefinition", type=DML_DDL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType2: BinaryAssociation = BinaryAssociation(
    name="dataType2",
    ends={
        Property(name="DML_DDL_DataType4", type=DML_DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_DDLDefinition3", type=DML_DDL_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="DML_DDL_Table", type=DML_DDL_Fk, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Fk", type=DML_DDL_Table, multiplicity=Multiplicity(0, 1))
    }
)
columnType7: BinaryAssociation = BinaryAssociation(
    name="columnType7",
    ends={
        Property(name="DML_DDL_Type8", type=DML_DDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Column", type=DML_DDL_Type, multiplicity=Multiplicity(1, 1))
    }
)
columns9: BinaryAssociation = BinaryAssociation(
    name="columns9",
    ends={
        Property(name="DML_DDL_Column11", type=DML_DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Table10", type=DML_DDL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnsPk12: BinaryAssociation = BinaryAssociation(
    name="columnsPk12",
    ends={
        Property(name="DML_DDL_Pk", type=DML_DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Table13", type=DML_DDL_Pk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnsFk14: BinaryAssociation = BinaryAssociation(
    name="columnsFk14",
    ends={
        Property(name="DML_DDL_Fk16", type=DML_DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Table15", type=DML_DDL_Fk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks17: BinaryAssociation = BinaryAssociation(
    name="checks17",
    ends={
        Property(name="DML_DDL_Ck19", type=DML_DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Table18", type=DML_DDL_Ck, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registries20: BinaryAssociation = BinaryAssociation(
    name="registries20",
    ends={
        Property(name="DML_DDL_Registry", type=DML_DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Table21", type=DML_DDL_Registry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registryValues22: BinaryAssociation = BinaryAssociation(
    name="registryValues22",
    ends={
        Property(name="DML_DDL_Value", type=DML_DDL_Registry, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Registry23", type=DML_DDL_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column24: BinaryAssociation = BinaryAssociation(
    name="column24",
    ends={
        Property(name="DML_DDL_Column26", type=DML_DDL_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Value25", type=DML_DDL_Column, multiplicity=Multiplicity(1, 1))
    }
)
valuesCk6: BinaryAssociation = BinaryAssociation(
    name="valuesCk6",
    ends={
        Property(name="DML_DDL_ValuesCk", type=DML_DDL_Ck, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_DDL_Ck", type=DML_DDL_ValuesCk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_DML_DDL_DataDefinition_Statement = Generalization(general=Statement, specific=DML_DDL_DataDefinition)
gen_DML_DDL_Database_DataDefinition = Generalization(general=DataDefinition, specific=DML_DDL_Database)
gen_DML_DDL_Table_DataDefinition = Generalization(general=DataDefinition, specific=DML_DDL_Table)
gen_DML_DDL_CommentTable_DataDefinition = Generalization(general=DataDefinition, specific=DML_DDL_CommentTable)
gen_DML_DDL_CommentColumn_DataDefinition = Generalization(general=DataDefinition, specific=DML_DDL_CommentColumn)
gen_DML_DDL_Exacto_Type = Generalization(general=Type, specific=DML_DDL_Exacto)
gen_DML_DDL_Integer_Exacto = Generalization(general=Exacto, specific=DML_DDL_Integer)
gen_DML_DDL_SmallInteger_Exacto = Generalization(general=Exacto, specific=DML_DDL_SmallInteger)
gen_DML_DDL_Int_Exacto = Generalization(general=Exacto, specific=DML_DDL_Int)
gen_DML_DDL_SmallInt_Exacto = Generalization(general=Exacto, specific=DML_DDL_SmallInt)
gen_DML_DDL_Number_Exacto = Generalization(general=Exacto, specific=DML_DDL_Number)
gen_DML_DDL_Numeric_Exacto = Generalization(general=Exacto, specific=DML_DDL_Numeric)
gen_DML_DDL_Character_Characters = Generalization(general=Characters, specific=DML_DDL_Character)
gen_DML_DDL_CharacterVarying_Characters = Generalization(general=Characters, specific=DML_DDL_CharacterVarying)
gen_DML_DDL_Char_Characters = Generalization(general=Characters, specific=DML_DDL_Char)
gen_DML_DDL_VarChar_Characters = Generalization(general=Characters, specific=DML_DDL_VarChar)
gen_DML_DDL_VarChar2_Characters = Generalization(general=Characters, specific=DML_DDL_VarChar2)
gen_DML_DDL_NVarChar2_Characters = Generalization(general=Characters, specific=DML_DDL_NVarChar2)
gen_DML_DDL_NChar_Characters = Generalization(general=Characters, specific=DML_DDL_NChar)
gen_DML_DDL_CharVarying_Characters = Generalization(general=Characters, specific=DML_DDL_CharVarying)
gen_DML_DDL_NationalChar_Characters = Generalization(general=Characters, specific=DML_DDL_NationalChar)
gen_DML_DDL_NationalCharVarying_Characters = Generalization(general=Characters, specific=DML_DDL_NationalCharVarying)
gen_DML_DDL_NationalCharacter_Characters = Generalization(general=Characters, specific=DML_DDL_NationalCharacter)
gen_DML_DDL_NationalCharacterVarying_Characters = Generalization(general=Characters, specific=DML_DDL_NationalCharacterVarying)
gen_DML_DDL_NCharVarying_Characters = Generalization(general=Characters, specific=DML_DDL_NCharVarying)
gen_DML_DDL_Clob_Characters = Generalization(general=Characters, specific=DML_DDL_Clob)
gen_DML_DDL_NClob_Characters = Generalization(general=Characters, specific=DML_DDL_NClob)
gen_DML_DDL_Bits_Type = Generalization(general=Type, specific=DML_DDL_Bits)
gen_DML_DDL_Bit_Bits = Generalization(general=Bits, specific=DML_DDL_Bit)
gen_DML_DDL_BitVarying_Bit = Generalization(general=Bit, specific=DML_DDL_BitVarying)
gen_DML_DDL_Times_Type = Generalization(general=Type, specific=DML_DDL_Times)
gen_DML_DDL_Date_Times = Generalization(general=Times, specific=DML_DDL_Date)
gen_DML_DDL_Time_Times = Generalization(general=Times, specific=DML_DDL_Time)
gen_DML_DDL_Timestamp_Times = Generalization(general=Times, specific=DML_DDL_Timestamp)
gen_DML_DDL_Intervals_Type = Generalization(general=Type, specific=DML_DDL_Intervals)
gen_DML_DDL_YearMonth_Intervals = Generalization(general=Intervals, specific=DML_DDL_YearMonth)
gen_DML_DDL_DayTime_Intervals = Generalization(general=Intervals, specific=DML_DDL_DayTime)
gen_DML_DDL_Binaries_Type = Generalization(general=Type, specific=DML_DDL_Binaries)
gen_DML_DDL_BinaryDouble_Binaries = Generalization(general=Binaries, specific=DML_DDL_BinaryDouble)
gen_DML_DDL_BinaryFloat_Binaries = Generalization(general=Binaries, specific=DML_DDL_BinaryFloat)
gen_DML_DDL_BFile_Binaries = Generalization(general=Binaries, specific=DML_DDL_BFile)
gen_DML_DDL_Blob_Binaries = Generalization(general=Binaries, specific=DML_DDL_Blob)
gen_DML_DDL_Decimal_Exacto = Generalization(general=Exacto, specific=DML_DDL_Decimal)
gen_DML_DDL_Aproximado_Type = Generalization(general=Type, specific=DML_DDL_Aproximado)
gen_DML_DDL_Real_Aproximado = Generalization(general=Aproximado, specific=DML_DDL_Real)
gen_DML_DDL_DoublePrecision_Aproximado = Generalization(general=Aproximado, specific=DML_DDL_DoublePrecision)
gen_DML_DDL_Float_Aproximado = Generalization(general=Aproximado, specific=DML_DDL_Float)
gen_DML_DDL_Long_Aproximado = Generalization(general=Aproximado, specific=DML_DDL_Long)
gen_DML_DDL_LongRaw_Aproximado = Generalization(general=Aproximado, specific=DML_DDL_LongRaw)
gen_DML_DDL_Characters_Type = Generalization(general=Type, specific=DML_DDL_Characters)

# Domain Model
domain_model = DomainModel(
    name="DML_DDL",
    types={DML_DDL_Statement, DML_DDL_DataDefinition, Statement, DML_DDL_DataType, DML_DDL_Type, DML_DDL_DDLDefinition, DML_DDL_Pk, DML_DDL_Fk, DML_DDL_Table, DML_DDL_Ck, DML_DDL_Database, DataDefinition, DML_DDL_Registry, DML_DDL_Value, DML_DDL_CommentTable, DML_DDL_CommentColumn, DML_DDL_Exacto, Type, DML_DDL_Integer, Exacto, DML_DDL_SmallInteger, DML_DDL_Int, DML_DDL_SmallInt, DML_DDL_Number, DML_DDL_Numeric, DML_DDL_Decimal, DML_DDL_ValuesCk, DML_DDL_Column, DML_DDL_Character, Characters, DML_DDL_CharacterVarying, DML_DDL_Char, DML_DDL_VarChar, DML_DDL_VarChar2, DML_DDL_NVarChar2, DML_DDL_NChar, DML_DDL_CharVarying, DML_DDL_NationalChar, DML_DDL_NationalCharVarying, DML_DDL_NationalCharacter, DML_DDL_NationalCharacterVarying, DML_DDL_NCharVarying, DML_DDL_Clob, DML_DDL_NClob, DML_DDL_Bits, DML_DDL_Bit, Bits, DML_DDL_BitVarying, Bit, DML_DDL_Times, DML_DDL_Date, Times, DML_DDL_Time, DML_DDL_Timestamp, DML_DDL_Intervals, DML_DDL_YearMonth, Intervals, DML_DDL_DayTime, DML_DDL_Binaries, DML_DDL_BinaryDouble, Binaries, DML_DDL_BinaryFloat, DML_DDL_BFile, DML_DDL_Blob, DML_DDL_Aproximado, DML_DDL_Real, Aproximado, DML_DDL_DoublePrecision, DML_DDL_Float, DML_DDL_Long, DML_DDL_LongRaw, DML_DDL_Characters},
    associations={types0, statements1, dataType2, references5, columnType7, columns9, columnsPk12, columnsFk14, checks17, registries20, registryValues22, column24, valuesCk6},
    generalizations={gen_DML_DDL_DataDefinition_Statement, gen_DML_DDL_Database_DataDefinition, gen_DML_DDL_Table_DataDefinition, gen_DML_DDL_CommentTable_DataDefinition, gen_DML_DDL_CommentColumn_DataDefinition, gen_DML_DDL_Exacto_Type, gen_DML_DDL_Integer_Exacto, gen_DML_DDL_SmallInteger_Exacto, gen_DML_DDL_Int_Exacto, gen_DML_DDL_SmallInt_Exacto, gen_DML_DDL_Number_Exacto, gen_DML_DDL_Numeric_Exacto, gen_DML_DDL_Character_Characters, gen_DML_DDL_CharacterVarying_Characters, gen_DML_DDL_Char_Characters, gen_DML_DDL_VarChar_Characters, gen_DML_DDL_VarChar2_Characters, gen_DML_DDL_NVarChar2_Characters, gen_DML_DDL_NChar_Characters, gen_DML_DDL_CharVarying_Characters, gen_DML_DDL_NationalChar_Characters, gen_DML_DDL_NationalCharVarying_Characters, gen_DML_DDL_NationalCharacter_Characters, gen_DML_DDL_NationalCharacterVarying_Characters, gen_DML_DDL_NCharVarying_Characters, gen_DML_DDL_Clob_Characters, gen_DML_DDL_NClob_Characters, gen_DML_DDL_Bits_Type, gen_DML_DDL_Bit_Bits, gen_DML_DDL_BitVarying_Bit, gen_DML_DDL_Times_Type, gen_DML_DDL_Date_Times, gen_DML_DDL_Time_Times, gen_DML_DDL_Timestamp_Times, gen_DML_DDL_Intervals_Type, gen_DML_DDL_YearMonth_Intervals, gen_DML_DDL_DayTime_Intervals, gen_DML_DDL_Binaries_Type, gen_DML_DDL_BinaryDouble_Binaries, gen_DML_DDL_BinaryFloat_Binaries, gen_DML_DDL_BFile_Binaries, gen_DML_DDL_Blob_Binaries, gen_DML_DDL_Decimal_Exacto, gen_DML_DDL_Aproximado_Type, gen_DML_DDL_Real_Aproximado, gen_DML_DDL_DoublePrecision_Aproximado, gen_DML_DDL_Float_Aproximado, gen_DML_DDL_Long_Aproximado, gen_DML_DDL_LongRaw_Aproximado, gen_DML_DDL_Characters_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)