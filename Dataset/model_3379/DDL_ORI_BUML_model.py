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
DDL_Database = Class(name="DDL::Database")
Statement = Class(name="Statement")
NamedElement = Class(name="NamedElement")
DDL_Table = Class(name="DDL::Table")
DDL_Column = Class(name="DDL::Column")
DDL_Pk = Class(name="DDL::Pk")
DDL_Ck = Class(name="DDL::Ck")
DDL_Fk = Class(name="DDL::Fk")
DDL_DDLDefinition = Class(name="DDL::DDLDefinition")
DDL_Statement = Class(name="DDL::Statement", is_abstract=True)
DDL_NamedElement = Class(name="DDL::NamedElement", is_abstract=True)
DDL_ValuesCheck = Class(name="DDL::ValuesCheck")
DDL_Check = Class(name="DDL::Check")
DDL_Type = Class(name="DDL::Type", is_abstract=True)
DDL_NationalCharacterStringType = Class(name="DDL::NationalCharacterStringType", is_abstract=True)
DDL_NationalCharacter = Class(name="DDL::NationalCharacter")
NationalCharacterStringType = Class(name="NationalCharacterStringType")
DDL_NationalChar = Class(name="DDL::NationalChar")
DDL_NChar = Class(name="DDL::NChar")
DDL_NationalCharacterVarying = Class(name="DDL::NationalCharacterVarying")
DDL_NationalCharVarying = Class(name="DDL::NationalCharVarying")
DDL_NCharVarying = Class(name="DDL::NCharVarying")
DDL_BitStringType = Class(name="DDL::BitStringType", is_abstract=True)
DDL_CharacterStringType = Class(name="DDL::CharacterStringType", is_abstract=True)
Type = Class(name="Type")
DDL_Character = Class(name="DDL::Character")
CharacterStringType = Class(name="CharacterStringType")
DDL_Char = Class(name="DDL::Char")
DDL_CharacterVarying = Class(name="DDL::CharacterVarying")
DDL_CharVarying = Class(name="DDL::CharVarying")
DDL_Varchar = Class(name="DDL::Varchar")
DDL_Dec = Class(name="DDL::Dec")
DDL_Integer = Class(name="DDL::Integer")
DDL_Int = Class(name="DDL::Int")
DDL_Small = Class(name="DDL::Small")
DDL_ApproximateNumericType = Class(name="DDL::ApproximateNumericType", is_abstract=True)
DDL_Float = Class(name="DDL::Float")
ApproximateNumericType = Class(name="ApproximateNumericType")
DDL_Real = Class(name="DDL::Real")
DDL_Bit = Class(name="DDL::Bit")
BitStringType = Class(name="BitStringType")
DDL_BitVarying = Class(name="DDL::BitVarying")
DDL_NumericType = Class(name="DDL::NumericType", is_abstract=True)
DDL_ExactNumericType = Class(name="DDL::ExactNumericType", is_abstract=True)
NumericType = Class(name="NumericType")
DDL_Numeric = Class(name="DDL::Numeric")
ExactNumericType = Class(name="ExactNumericType")
DDL_Decimal = Class(name="DDL::Decimal")
DDL_DoublePrecision = Class(name="DDL::DoublePrecision")
DDL_DatetimeType = Class(name="DDL::DatetimeType", is_abstract=True)
DDL_Date = Class(name="DDL::Date")
DatetimeType = Class(name="DatetimeType")
DDL_Time = Class(name="DDL::Time")
DDL_TimeStamp = Class(name="DDL::TimeStamp")
DDL_Interval = Class(name="DDL::Interval")

# DDL_Database class attributes and methods

# Statement class attributes and methods

# NamedElement class attributes and methods

# DDL_Table class attributes and methods

# DDL_Column class attributes and methods
DDL_Column_columnNull: Property = Property(name="columnNull", type=BooleanType)
DDL_Column.attributes={DDL_Column_columnNull}

# DDL_Pk class attributes and methods
DDL_Pk_columnName: Property = Property(name="columnName", type=StringType)
DDL_Pk.attributes={DDL_Pk_columnName}

# DDL_Ck class attributes and methods
DDL_Ck_columnName: Property = Property(name="columnName", type=StringType)
DDL_Ck.attributes={DDL_Ck_columnName}

# DDL_Fk class attributes and methods
DDL_Fk_columnName: Property = Property(name="columnName", type=StringType)
DDL_Fk_columnReference: Property = Property(name="columnReference", type=StringType)
DDL_Fk.attributes={DDL_Fk_columnName, DDL_Fk_columnReference}

# DDL_DDLDefinition class attributes and methods

# DDL_Statement class attributes and methods

# DDL_NamedElement class attributes and methods
DDL_NamedElement_name: Property = Property(name="name", type=StringType)
DDL_NamedElement.attributes={DDL_NamedElement_name}

# DDL_ValuesCheck class attributes and methods
DDL_ValuesCheck_value: Property = Property(name="value", type=StringType)
DDL_ValuesCheck_comparator: Property = Property(name="comparator", type=StringType)
DDL_ValuesCheck_columnName: Property = Property(name="columnName", type=StringType)
DDL_ValuesCheck_logConjuntion: Property = Property(name="logConjuntion", type=StringType)
DDL_ValuesCheck.attributes={DDL_ValuesCheck_comparator, DDL_ValuesCheck_value, DDL_ValuesCheck_columnName, DDL_ValuesCheck_logConjuntion}

# DDL_Check class attributes and methods

# DDL_Type class attributes and methods

# DDL_NationalCharacterStringType class attributes and methods
DDL_NationalCharacterStringType_length: Property = Property(name="length", type=IntegerType)
DDL_NationalCharacterStringType.attributes={DDL_NationalCharacterStringType_length}

# DDL_NationalCharacter class attributes and methods

# NationalCharacterStringType class attributes and methods

# DDL_NationalChar class attributes and methods

# DDL_NChar class attributes and methods

# DDL_NationalCharacterVarying class attributes and methods

# DDL_NationalCharVarying class attributes and methods

# DDL_NCharVarying class attributes and methods

# DDL_BitStringType class attributes and methods
DDL_BitStringType_length: Property = Property(name="length", type=IntegerType)
DDL_BitStringType.attributes={DDL_BitStringType_length}

# DDL_CharacterStringType class attributes and methods
DDL_CharacterStringType_length: Property = Property(name="length", type=IntegerType)
DDL_CharacterStringType.attributes={DDL_CharacterStringType_length}

# Type class attributes and methods

# DDL_Character class attributes and methods

# CharacterStringType class attributes and methods

# DDL_Char class attributes and methods

# DDL_CharacterVarying class attributes and methods

# DDL_CharVarying class attributes and methods

# DDL_Varchar class attributes and methods

# DDL_Dec class attributes and methods
DDL_Dec_precision: Property = Property(name="precision", type=IntegerType)
DDL_Dec_scale: Property = Property(name="scale", type=IntegerType)
DDL_Dec.attributes={DDL_Dec_scale, DDL_Dec_precision}

# DDL_Integer class attributes and methods

# DDL_Int class attributes and methods

# DDL_Small class attributes and methods

# DDL_ApproximateNumericType class attributes and methods

# DDL_Float class attributes and methods
DDL_Float_precision: Property = Property(name="precision", type=IntegerType)
DDL_Float.attributes={DDL_Float_precision}

# ApproximateNumericType class attributes and methods

# DDL_Real class attributes and methods

# DDL_Bit class attributes and methods

# BitStringType class attributes and methods

# DDL_BitVarying class attributes and methods

# DDL_NumericType class attributes and methods

# DDL_ExactNumericType class attributes and methods

# NumericType class attributes and methods

# DDL_Numeric class attributes and methods
DDL_Numeric_precision: Property = Property(name="precision", type=IntegerType)
DDL_Numeric_scale: Property = Property(name="scale", type=IntegerType)
DDL_Numeric.attributes={DDL_Numeric_scale, DDL_Numeric_precision}

# ExactNumericType class attributes and methods

# DDL_Decimal class attributes and methods
DDL_Decimal_precision: Property = Property(name="precision", type=IntegerType)
DDL_Decimal_scale: Property = Property(name="scale", type=IntegerType)
DDL_Decimal.attributes={DDL_Decimal_scale, DDL_Decimal_precision}

# DDL_DoublePrecision class attributes and methods

# DDL_DatetimeType class attributes and methods

# DDL_Date class attributes and methods

# DatetimeType class attributes and methods

# DDL_Time class attributes and methods
DDL_Time_precision: Property = Property(name="precision", type=IntegerType)
DDL_Time_withTimeZone: Property = Property(name="withTimeZone", type=BooleanType)
DDL_Time.attributes={DDL_Time_withTimeZone, DDL_Time_precision}

# DDL_TimeStamp class attributes and methods
DDL_TimeStamp_precision: Property = Property(name="precision", type=IntegerType)
DDL_TimeStamp_withTimeZone: Property = Property(name="withTimeZone", type=BooleanType)
DDL_TimeStamp.attributes={DDL_TimeStamp_precision, DDL_TimeStamp_withTimeZone}

# DDL_Interval class attributes and methods
DDL_Interval_field2: Property = Property(name="field2", type=StringType)
DDL_Interval_precision1: Property = Property(name="precision1", type=IntegerType)
DDL_Interval_precision2: Property = Property(name="precision2", type=IntegerType)
DDL_Interval_field1: Property = Property(name="field1", type=StringType)
DDL_Interval.attributes={DDL_Interval_field2, DDL_Interval_precision2, DDL_Interval_precision1, DDL_Interval_field1}

# Relationships
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="DDL_Column", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table", type=DDL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pks2: BinaryAssociation = BinaryAssociation(
    name="pks2",
    ends={
        Property(name="DDL_Pk", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table3", type=DDL_Pk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cks4: BinaryAssociation = BinaryAssociation(
    name="cks4",
    ends={
        Property(name="DDL_Ck", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table5", type=DDL_Ck, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="DDL_Statement", type=DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_DDLDefinition", type=DDL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references12: BinaryAssociation = BinaryAssociation(
    name="references12",
    ends={
        Property(name="DDL_Table14", type=DDL_Fk, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Fk13", type=DDL_Table, multiplicity=Multiplicity(0, 1))
    }
)
valuesCheck15: BinaryAssociation = BinaryAssociation(
    name="valuesCheck15",
    ends={
        Property(name="DDL_ValuesCheck", type=DDL_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Check16", type=DDL_ValuesCheck, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fks6: BinaryAssociation = BinaryAssociation(
    name="fks6",
    ends={
        Property(name="DDL_Fk", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table7", type=DDL_Fk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks8: BinaryAssociation = BinaryAssociation(
    name="checks8",
    ends={
        Property(name="DDL_Check", type=DDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Table9", type=DDL_Check, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="DDL_Type", type=DDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_Column11", type=DDL_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_DDL_Database_Statement = Generalization(general=Statement, specific=DDL_Database)
gen_DDL_Database_NamedElement = Generalization(general=NamedElement, specific=DDL_Database)
gen_DDL_Table_Statement = Generalization(general=Statement, specific=DDL_Table)
gen_DDL_Table_NamedElement = Generalization(general=NamedElement, specific=DDL_Table)
gen_DDL_Fk_NamedElement = Generalization(general=NamedElement, specific=DDL_Fk)
gen_DDL_Check_NamedElement = Generalization(general=NamedElement, specific=DDL_Check)
gen_DDL_Column_NamedElement = Generalization(general=NamedElement, specific=DDL_Column)
gen_DDL_Pk_NamedElement = Generalization(general=NamedElement, specific=DDL_Pk)
gen_DDL_Ck_NamedElement = Generalization(general=NamedElement, specific=DDL_Ck)
gen_DDL_NationalCharacterStringType_Type = Generalization(general=Type, specific=DDL_NationalCharacterStringType)
gen_DDL_NationalCharacter_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NationalCharacter)
gen_DDL_NationalChar_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NationalChar)
gen_DDL_NChar_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NChar)
gen_DDL_NationalCharacterVarying_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NationalCharacterVarying)
gen_DDL_NationalCharVarying_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NationalCharVarying)
gen_DDL_NCharVarying_NationalCharacterStringType = Generalization(general=NationalCharacterStringType, specific=DDL_NCharVarying)
gen_DDL_BitStringType_Type = Generalization(general=Type, specific=DDL_BitStringType)
gen_DDL_CharacterStringType_Type = Generalization(general=Type, specific=DDL_CharacterStringType)
gen_DDL_Character_CharacterStringType = Generalization(general=CharacterStringType, specific=DDL_Character)
gen_DDL_Char_CharacterStringType = Generalization(general=CharacterStringType, specific=DDL_Char)
gen_DDL_CharacterVarying_CharacterStringType = Generalization(general=CharacterStringType, specific=DDL_CharacterVarying)
gen_DDL_CharVarying_CharacterStringType = Generalization(general=CharacterStringType, specific=DDL_CharVarying)
gen_DDL_Varchar_CharacterStringType = Generalization(general=CharacterStringType, specific=DDL_Varchar)
gen_DDL_Dec_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Dec)
gen_DDL_Integer_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Integer)
gen_DDL_Int_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Int)
gen_DDL_Small_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Small)
gen_DDL_ApproximateNumericType_NumericType = Generalization(general=NumericType, specific=DDL_ApproximateNumericType)
gen_DDL_Float_ApproximateNumericType = Generalization(general=ApproximateNumericType, specific=DDL_Float)
gen_DDL_Real_ApproximateNumericType = Generalization(general=ApproximateNumericType, specific=DDL_Real)
gen_DDL_Bit_BitStringType = Generalization(general=BitStringType, specific=DDL_Bit)
gen_DDL_BitVarying_BitStringType = Generalization(general=BitStringType, specific=DDL_BitVarying)
gen_DDL_NumericType_Type = Generalization(general=Type, specific=DDL_NumericType)
gen_DDL_ExactNumericType_NumericType = Generalization(general=NumericType, specific=DDL_ExactNumericType)
gen_DDL_Numeric_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Numeric)
gen_DDL_Decimal_ExactNumericType = Generalization(general=ExactNumericType, specific=DDL_Decimal)
gen_DDL_DoublePrecision_ApproximateNumericType = Generalization(general=ApproximateNumericType, specific=DDL_DoublePrecision)
gen_DDL_DatetimeType_Type = Generalization(general=Type, specific=DDL_DatetimeType)
gen_DDL_Date_DatetimeType = Generalization(general=DatetimeType, specific=DDL_Date)
gen_DDL_Time_DatetimeType = Generalization(general=DatetimeType, specific=DDL_Time)
gen_DDL_TimeStamp_DatetimeType = Generalization(general=DatetimeType, specific=DDL_TimeStamp)
gen_DDL_Interval_Type = Generalization(general=Type, specific=DDL_Interval)

# Domain Model
domain_model = DomainModel(
    name="DDL",
    types={DDL_Database, Statement, NamedElement, DDL_Table, DDL_Column, DDL_Pk, DDL_Ck, DDL_Fk, DDL_DDLDefinition, DDL_Statement, DDL_NamedElement, DDL_ValuesCheck, DDL_Check, DDL_Type, DDL_NationalCharacterStringType, DDL_NationalCharacter, NationalCharacterStringType, DDL_NationalChar, DDL_NChar, DDL_NationalCharacterVarying, DDL_NationalCharVarying, DDL_NCharVarying, DDL_BitStringType, DDL_CharacterStringType, Type, DDL_Character, CharacterStringType, DDL_Char, DDL_CharacterVarying, DDL_CharVarying, DDL_Varchar, DDL_Dec, DDL_Integer, DDL_Int, DDL_Small, DDL_ApproximateNumericType, DDL_Float, ApproximateNumericType, DDL_Real, DDL_Bit, BitStringType, DDL_BitVarying, DDL_NumericType, DDL_ExactNumericType, NumericType, DDL_Numeric, ExactNumericType, DDL_Decimal, DDL_DoublePrecision, DDL_DatetimeType, DDL_Date, DatetimeType, DDL_Time, DDL_TimeStamp, DDL_Interval},
    associations={columns1, pks2, cks4, statements0, references12, valuesCheck15, fks6, checks8, type10},
    generalizations={gen_DDL_Database_Statement, gen_DDL_Database_NamedElement, gen_DDL_Table_Statement, gen_DDL_Table_NamedElement, gen_DDL_Fk_NamedElement, gen_DDL_Check_NamedElement, gen_DDL_Column_NamedElement, gen_DDL_Pk_NamedElement, gen_DDL_Ck_NamedElement, gen_DDL_NationalCharacterStringType_Type, gen_DDL_NationalCharacter_NationalCharacterStringType, gen_DDL_NationalChar_NationalCharacterStringType, gen_DDL_NChar_NationalCharacterStringType, gen_DDL_NationalCharacterVarying_NationalCharacterStringType, gen_DDL_NationalCharVarying_NationalCharacterStringType, gen_DDL_NCharVarying_NationalCharacterStringType, gen_DDL_BitStringType_Type, gen_DDL_CharacterStringType_Type, gen_DDL_Character_CharacterStringType, gen_DDL_Char_CharacterStringType, gen_DDL_CharacterVarying_CharacterStringType, gen_DDL_CharVarying_CharacterStringType, gen_DDL_Varchar_CharacterStringType, gen_DDL_Dec_ExactNumericType, gen_DDL_Integer_ExactNumericType, gen_DDL_Int_ExactNumericType, gen_DDL_Small_ExactNumericType, gen_DDL_ApproximateNumericType_NumericType, gen_DDL_Float_ApproximateNumericType, gen_DDL_Real_ApproximateNumericType, gen_DDL_Bit_BitStringType, gen_DDL_BitVarying_BitStringType, gen_DDL_NumericType_Type, gen_DDL_ExactNumericType_NumericType, gen_DDL_Numeric_ExactNumericType, gen_DDL_Decimal_ExactNumericType, gen_DDL_DoublePrecision_ApproximateNumericType, gen_DDL_DatetimeType_Type, gen_DDL_Date_DatetimeType, gen_DDL_Time_DatetimeType, gen_DDL_TimeStamp_DatetimeType, gen_DDL_Interval_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)