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

# Enumerations
ANSICharacterTypes: Enumeration = Enumeration(
    name="ANSICharacterTypes",
    literals={
            EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="CHARACTERVARYING"),
			EnumerationLiteral(name="CHARVARYING"),
			EnumerationLiteral(name="NCHARVARYING"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="NATIONALCHARACTER"),
			EnumerationLiteral(name="NATIONALCHAR"),
			EnumerationLiteral(name="NATIONALCHARACTERVARYING"),
			EnumerationLiteral(name="NATIONALCHARVARYING")
    }
)

ANSINumberTypes: Enumeration = Enumeration(
    name="ANSINumberTypes",
    literals={
            EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="DEC"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="DOUBLEPRECISION"),
			EnumerationLiteral(name="REAL")
    }
)

BuiltInCharacterSemantics: Enumeration = Enumeration(
    name="BuiltInCharacterSemantics",
    literals={
            EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="CHAR")
    }
)

BuiltInCharacterTypes: Enumeration = Enumeration(
    name="BuiltInCharacterTypes",
    literals={
            EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="VARCHAR2"),
			EnumerationLiteral(name="NCHAR"),
			EnumerationLiteral(name="NVARCHAR2")
    }
)

BuiltInDatetimeTypes: Enumeration = Enumeration(
    name="BuiltInDatetimeTypes",
    literals={
            EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="TIMESTAMPWITHTIMEZONE"),
			EnumerationLiteral(name="TIMESTAMPWITHLOCALTIMEZONE"),
			EnumerationLiteral(name="INTERVALYEARTOMONTH"),
			EnumerationLiteral(name="INTERVALDAYTOSECOND")
    }
)

BuiltInLOBType: Enumeration = Enumeration(
    name="BuiltInLOBType",
    literals={
            EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="CLOB"),
			EnumerationLiteral(name="NLOB"),
			EnumerationLiteral(name="BFILE")
    }
)

BuiltInLongAndRawTypes: Enumeration = Enumeration(
    name="BuiltInLongAndRawTypes",
    literals={
            EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="LONGRAW"),
			EnumerationLiteral(name="RAW")
    }
)

BuiltInROWIDType: Enumeration = Enumeration(
    name="BuiltInROWIDType",
    literals={
            EnumerationLiteral(name="ROWID"),
			EnumerationLiteral(name="UROWID")
    }
)

BuiltNumberTypes: Enumeration = Enumeration(
    name="BuiltNumberTypes",
    literals={
            EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="BINARY_FLOAT"),
			EnumerationLiteral(name="BINARY_DOUBLE")
    }
)

CharacterFeatures: Enumeration = Enumeration(
    name="CharacterFeatures",
    literals={
            EnumerationLiteral(name="size"),
			EnumerationLiteral(name="semantic")
    }
)

DatetimeFeatures: Enumeration = Enumeration(
    name="DatetimeFeatures",
    literals={
            EnumerationLiteral(name="precision")
    }
)

IntervalFeatures: Enumeration = Enumeration(
    name="IntervalFeatures",
    literals={
            EnumerationLiteral(name="day_precision"),
			EnumerationLiteral(name="second_precision"),
			EnumerationLiteral(name="year_precision")
    }
)

NumberFeatures: Enumeration = Enumeration(
    name="NumberFeatures",
    literals={
            EnumerationLiteral(name="size"),
			EnumerationLiteral(name="precision"),
			EnumerationLiteral(name="scale")
    }
)

ONDELETEActions: Enumeration = Enumeration(
    name="ONDELETEActions",
    literals={
            EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SETNULL")
    }
)

ParameterMode: Enumeration = Enumeration(
    name="ParameterMode",
    literals={
            EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT")
    }
)

RawFeatures: Enumeration = Enumeration(
    name="RawFeatures",
    literals={
            EnumerationLiteral(name="size")
    }
)

RowFeatures: Enumeration = Enumeration(
    name="RowFeatures",
    literals={
            EnumerationLiteral(name="size")
    }
)

SuppliedAnyTypes: Enumeration = Enumeration(
    name="SuppliedAnyTypes",
    literals={
            EnumerationLiteral(name="SYSANYDATA"),
			EnumerationLiteral(name="SYSANYTYPE"),
			EnumerationLiteral(name="SYSANYDATASET")
    }
)

SuppliedMediaTypes: Enumeration = Enumeration(
    name="SuppliedMediaTypes",
    literals={
            EnumerationLiteral(name="ORDImageSignature"),
			EnumerationLiteral(name="SI_STILLIMAGE"),
			EnumerationLiteral(name="SI_AVERAGECOLOR"),
			EnumerationLiteral(name="ORDAudio"),
			EnumerationLiteral(name="ORDImage"),
			EnumerationLiteral(name="ORDVideo"),
			EnumerationLiteral(name="ORDDoc"),
			EnumerationLiteral(name="SI_POSITIONALCOLOR"),
			EnumerationLiteral(name="SI_COLORHISTOGRAM"),
			EnumerationLiteral(name="SI_TEXTURE"),
			EnumerationLiteral(name="SI_FEATURELIST"),
			EnumerationLiteral(name="SI_COLOR")
    }
)

SuppliedSpacialTypes: Enumeration = Enumeration(
    name="SuppliedSpacialTypes",
    literals={
            EnumerationLiteral(name="SDO_GEOMETRY"),
			EnumerationLiteral(name="SDO_TOPO_GEOMETRY"),
			EnumerationLiteral(name="SDO_RASTER")
    }
)

SuppliedXMLTypes: Enumeration = Enumeration(
    name="SuppliedXMLTypes",
    literals={
            EnumerationLiteral(name="XMLTYPE"),
			EnumerationLiteral(name="URITYPE")
    }
)

TriggerActionTime: Enumeration = Enumeration(
    name="TriggerActionTime",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="INSTEADOF")
    }
)

TriggerEvent: Enumeration = Enumeration(
    name="TriggerEvent",
    literals={
            EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="INSERT"),
			EnumerationLiteral(name="UPDATE")
    }
)

# Classes
ORDB4ORA_ANSICharacterType = Class(name="ORDB4ORA::ANSICharacterType")
ANSIType = Class(name="ANSIType")
ORDB4ORA_ANSINumberType = Class(name="ORDB4ORA::ANSINumberType")
ORDB4ORA_ANSIType = Class(name="ORDB4ORA::ANSIType", is_abstract=True)
BasicDataType = Class(name="BasicDataType")
ORDB4ORA_AnyType = Class(name="ORDB4ORA::AnyType")
SuppliedType = Class(name="SuppliedType")
ORDB4ORA_Attribute = Class(name="ORDB4ORA::Attribute")
StructuralComponent = Class(name="StructuralComponent")
ORDB4ORA_StructuredType = Class(name="ORDB4ORA::StructuredType")
ORDB4ORA_BasicDataType = Class(name="ORDB4ORA::BasicDataType", is_abstract=True)
Datatype = Class(name="Datatype")
ORDB4ORA_BuiltInCharacterType = Class(name="ORDB4ORA::BuiltInCharacterType")
BuiltInType = Class(name="BuiltInType")
ORDB4ORA_BuiltInNumberType = Class(name="ORDB4ORA::BuiltInNumberType")
ORDB4ORA_BuiltInType = Class(name="ORDB4ORA::BuiltInType", is_abstract=True)
ORDB4ORA_CharacterFeature = Class(name="ORDB4ORA::CharacterFeature")
Feature = Class(name="Feature")
ORDB4ORA_Check = Class(name="ORDB4ORA::Check")
Restriction = Class(name="Restriction")
ORDB4ORA_Column = Class(name="ORDB4ORA::Column")
ORDB4ORA_Table = Class(name="ORDB4ORA::Table")
ORDB4ORA_Datatype = Class(name="ORDB4ORA::Datatype", is_abstract=True)
ORDB4ORA_Model = Class(name="ORDB4ORA::Model")
ORDB4ORA_DatetimeFeature = Class(name="ORDB4ORA::DatetimeFeature")
ORDB4ORA_DatetimeType = Class(name="ORDB4ORA::DatetimeType")
ORDB4ORA_Feature = Class(name="ORDB4ORA::Feature", is_abstract=True)
ORDB4ORA_ForeignKey = Class(name="ORDB4ORA::ForeignKey")
ORDB4ORA_Function = Class(name="ORDB4ORA::Function")
Operation = Class(name="Operation")
ORDB4ORA_IntervalFeature = Class(name="ORDB4ORA::IntervalFeature")
ORDB4ORA_LOBType = Class(name="ORDB4ORA::LOBType")
ORDB4ORA_LongAndRawType = Class(name="ORDB4ORA::LongAndRawType")
ORDB4ORA_MediaType = Class(name="ORDB4ORA::MediaType")
ORDB4ORA_Method = Class(name="ORDB4ORA::Method")
ORDB4ORA_MethodParameter = Class(name="ORDB4ORA::MethodParameter")
Parameter_ = Class(name="Parameter")
ORDB4ORA_Operation = Class(name="ORDB4ORA::Operation", is_abstract=True)
ORDB4ORA_OperationParameter = Class(name="ORDB4ORA::OperationParameter")
ORDB4ORA_Package = Class(name="ORDB4ORA::Package")
ORDB4ORA_NestedTableType = Class(name="ORDB4ORA::NestedTableType")
ORDB4ORA_NotNull = Class(name="ORDB4ORA::NotNull")
ORDB4ORA_NumberFeature = Class(name="ORDB4ORA::NumberFeature")
ORDB4ORA_PrimaryKey = Class(name="ORDB4ORA::PrimaryKey")
ORDB4ORA_Parameter = Class(name="ORDB4ORA::Parameter")
ORDB4ORA_Procedure = Class(name="ORDB4ORA::Procedure")
ORDB4ORA_ROWIDType = Class(name="ORDB4ORA::ROWIDType")
ORDB4ORA_RawFeature = Class(name="ORDB4ORA::RawFeature")
ORDB4ORA_ReferenceType = Class(name="ORDB4ORA::ReferenceType")
ORDB4ORA_Restriction = Class(name="ORDB4ORA::Restriction", is_abstract=True)
ORDB4ORA_StructuralComponent = Class(name="ORDB4ORA::StructuralComponent")
ORDB4ORA_RowFeature = Class(name="ORDB4ORA::RowFeature")
ORDB4ORA_SpacialType = Class(name="ORDB4ORA::SpacialType")
ORDB4ORA_StoredNestedTable = Class(name="ORDB4ORA::StoredNestedTable")
ORDB4ORA_TypedTable = Class(name="ORDB4ORA::TypedTable")
ORDB4ORA_SuppliedType = Class(name="ORDB4ORA::SuppliedType", is_abstract=True)
ORDB4ORA_Trigger = Class(name="ORDB4ORA::Trigger")
ORDB4ORA_Unique = Class(name="ORDB4ORA::Unique")
Table = Class(name="Table")
ORDB4ORA_Varray = Class(name="ORDB4ORA::Varray")
ORDB4ORA_XMLType = Class(name="ORDB4ORA::XMLType")
ORDB4ORA_DerivedTable = Class(name="ORDB4ORA::DerivedTable")
ORDB4ORA_View = Class(name="ORDB4ORA::View")
DerivedTable = Class(name="DerivedTable")

# ORDB4ORA_ANSICharacterType class attributes and methods
ORDB4ORA_ANSICharacterType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_ANSICharacterType.attributes={ORDB4ORA_ANSICharacterType_Descriptor}

# ANSIType class attributes and methods

# ORDB4ORA_ANSINumberType class attributes and methods
ORDB4ORA_ANSINumberType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_ANSINumberType.attributes={ORDB4ORA_ANSINumberType_Descriptor}

# ORDB4ORA_ANSIType class attributes and methods

# BasicDataType class attributes and methods

# ORDB4ORA_AnyType class attributes and methods
ORDB4ORA_AnyType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_AnyType.attributes={ORDB4ORA_AnyType_Descriptor}

# SuppliedType class attributes and methods

# ORDB4ORA_Attribute class attributes and methods
ORDB4ORA_Attribute_Default: Property = Property(name="Default", type=StringType)
ORDB4ORA_Attribute.attributes={ORDB4ORA_Attribute_Default}

# StructuralComponent class attributes and methods

# ORDB4ORA_StructuredType class attributes and methods
ORDB4ORA_StructuredType_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_StructuredType_is_instantiable: Property = Property(name="is_instantiable", type=BooleanType)
ORDB4ORA_StructuredType_is_final: Property = Property(name="is_final", type=BooleanType)
ORDB4ORA_StructuredType.attributes={ORDB4ORA_StructuredType_is_final, ORDB4ORA_StructuredType_is_instantiable, ORDB4ORA_StructuredType_Name}

# ORDB4ORA_BasicDataType class attributes and methods

# Datatype class attributes and methods

# ORDB4ORA_BuiltInCharacterType class attributes and methods
ORDB4ORA_BuiltInCharacterType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_BuiltInCharacterType_Semantic: Property = Property(name="Semantic", type=StringType)
ORDB4ORA_BuiltInCharacterType_Size_Min: Property = Property(name="Size_Min", type=IntegerType)
ORDB4ORA_BuiltInCharacterType_Size_Max: Property = Property(name="Size_Max", type=IntegerType)
ORDB4ORA_BuiltInCharacterType_Size_Def: Property = Property(name="Size_Def", type=IntegerType)
ORDB4ORA_BuiltInCharacterType.attributes={ORDB4ORA_BuiltInCharacterType_Descriptor, ORDB4ORA_BuiltInCharacterType_Semantic, ORDB4ORA_BuiltInCharacterType_Size_Def, ORDB4ORA_BuiltInCharacterType_Size_Min, ORDB4ORA_BuiltInCharacterType_Size_Max}

# BuiltInType class attributes and methods

# ORDB4ORA_BuiltInNumberType class attributes and methods
ORDB4ORA_BuiltInNumberType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_BuiltInNumberType_Precision_Mn: Property = Property(name="Precision_Mn", type=IntegerType)
ORDB4ORA_BuiltInNumberType_Precision_Max: Property = Property(name="Precision_Max", type=IntegerType)
ORDB4ORA_BuiltInNumberType_Scale_Min: Property = Property(name="Scale_Min", type=IntegerType)
ORDB4ORA_BuiltInNumberType_Scale_Max: Property = Property(name="Scale_Max", type=IntegerType)
ORDB4ORA_BuiltInNumberType.attributes={ORDB4ORA_BuiltInNumberType_Precision_Mn, ORDB4ORA_BuiltInNumberType_Scale_Min, ORDB4ORA_BuiltInNumberType_Scale_Max, ORDB4ORA_BuiltInNumberType_Descriptor, ORDB4ORA_BuiltInNumberType_Precision_Max}

# ORDB4ORA_BuiltInType class attributes and methods

# ORDB4ORA_CharacterFeature class attributes and methods
ORDB4ORA_CharacterFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_CharacterFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_CharacterFeature.attributes={ORDB4ORA_CharacterFeature_value, ORDB4ORA_CharacterFeature_key}

# Feature class attributes and methods

# ORDB4ORA_Check class attributes and methods
ORDB4ORA_Check_Condition: Property = Property(name="Condition", type=StringType)
ORDB4ORA_Check_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Check.attributes={ORDB4ORA_Check_Condition, ORDB4ORA_Check_Name}

# Restriction class attributes and methods

# ORDB4ORA_Column class attributes and methods

# ORDB4ORA_Table class attributes and methods
ORDB4ORA_Table_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Table.attributes={ORDB4ORA_Table_Name}

# ORDB4ORA_Datatype class attributes and methods

# ORDB4ORA_Model class attributes and methods
ORDB4ORA_Model_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Model.attributes={ORDB4ORA_Model_Name}

# ORDB4ORA_DatetimeFeature class attributes and methods
ORDB4ORA_DatetimeFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_DatetimeFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_DatetimeFeature.attributes={ORDB4ORA_DatetimeFeature_value, ORDB4ORA_DatetimeFeature_key}

# ORDB4ORA_DatetimeType class attributes and methods
ORDB4ORA_DatetimeType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_DatetimeType_SecondPrecision_Min: Property = Property(name="SecondPrecision_Min", type=IntegerType)
ORDB4ORA_DatetimeType_SecondPrecision_Max: Property = Property(name="SecondPrecision_Max", type=IntegerType)
ORDB4ORA_DatetimeType_SecondPrecision_Def: Property = Property(name="SecondPrecision_Def", type=IntegerType)
ORDB4ORA_DatetimeType_DayPrecision_Min: Property = Property(name="DayPrecision_Min", type=IntegerType)
ORDB4ORA_DatetimeType_DayPrecision_Max: Property = Property(name="DayPrecision_Max", type=IntegerType)
ORDB4ORA_DatetimeType_DayPrecision_Def: Property = Property(name="DayPrecision_Def", type=IntegerType)
ORDB4ORA_DatetimeType_YearPrecision_Min: Property = Property(name="YearPrecision_Min", type=IntegerType)
ORDB4ORA_DatetimeType_YearPrecision_Max: Property = Property(name="YearPrecision_Max", type=IntegerType)
ORDB4ORA_DatetimeType_YearPrecision_Def: Property = Property(name="YearPrecision_Def", type=IntegerType)
ORDB4ORA_DatetimeType.attributes={ORDB4ORA_DatetimeType_SecondPrecision_Max, ORDB4ORA_DatetimeType_YearPrecision_Max, ORDB4ORA_DatetimeType_YearPrecision_Min, ORDB4ORA_DatetimeType_SecondPrecision_Def, ORDB4ORA_DatetimeType_YearPrecision_Def, ORDB4ORA_DatetimeType_DayPrecision_Min, ORDB4ORA_DatetimeType_DayPrecision_Max, ORDB4ORA_DatetimeType_Descriptor, ORDB4ORA_DatetimeType_DayPrecision_Def, ORDB4ORA_DatetimeType_SecondPrecision_Min}

# ORDB4ORA_Feature class attributes and methods

# ORDB4ORA_ForeignKey class attributes and methods
ORDB4ORA_ForeignKey_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_ForeignKey_OnDelete: Property = Property(name="OnDelete", type=StringType)
ORDB4ORA_ForeignKey.attributes={ORDB4ORA_ForeignKey_Name, ORDB4ORA_ForeignKey_OnDelete}

# ORDB4ORA_Function class attributes and methods

# Operation class attributes and methods

# ORDB4ORA_IntervalFeature class attributes and methods
ORDB4ORA_IntervalFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_IntervalFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_IntervalFeature.attributes={ORDB4ORA_IntervalFeature_key, ORDB4ORA_IntervalFeature_value}

# ORDB4ORA_LOBType class attributes and methods
ORDB4ORA_LOBType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_LOBType.attributes={ORDB4ORA_LOBType_Descriptor}

# ORDB4ORA_LongAndRawType class attributes and methods
ORDB4ORA_LongAndRawType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_LongAndRawType_Size_Min: Property = Property(name="Size_Min", type=IntegerType)
ORDB4ORA_LongAndRawType_Size_Max: Property = Property(name="Size_Max", type=IntegerType)
ORDB4ORA_LongAndRawType.attributes={ORDB4ORA_LongAndRawType_Size_Min, ORDB4ORA_LongAndRawType_Descriptor, ORDB4ORA_LongAndRawType_Size_Max}

# ORDB4ORA_MediaType class attributes and methods
ORDB4ORA_MediaType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_MediaType.attributes={ORDB4ORA_MediaType_Descriptor}

# ORDB4ORA_Method class attributes and methods
ORDB4ORA_Method_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Method_Body: Property = Property(name="Body", type=StringType)
ORDB4ORA_Method.attributes={ORDB4ORA_Method_Body, ORDB4ORA_Method_Name}

# ORDB4ORA_MethodParameter class attributes and methods

# Parameter class attributes and methods

# ORDB4ORA_Operation class attributes and methods
ORDB4ORA_Operation_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Operation_Body: Property = Property(name="Body", type=StringType)
ORDB4ORA_Operation.attributes={ORDB4ORA_Operation_Name, ORDB4ORA_Operation_Body}

# ORDB4ORA_OperationParameter class attributes and methods
ORDB4ORA_OperationParameter_Mode: Property = Property(name="Mode", type=StringType)
ORDB4ORA_OperationParameter.attributes={ORDB4ORA_OperationParameter_Mode}

# ORDB4ORA_Package class attributes and methods
ORDB4ORA_Package_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Package.attributes={ORDB4ORA_Package_Name}

# ORDB4ORA_NestedTableType class attributes and methods
ORDB4ORA_NestedTableType_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_NestedTableType.attributes={ORDB4ORA_NestedTableType_Name}

# ORDB4ORA_NotNull class attributes and methods
ORDB4ORA_NotNull_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_NotNull.attributes={ORDB4ORA_NotNull_Name}

# ORDB4ORA_NumberFeature class attributes and methods
ORDB4ORA_NumberFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_NumberFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_NumberFeature.attributes={ORDB4ORA_NumberFeature_value, ORDB4ORA_NumberFeature_key}

# ORDB4ORA_PrimaryKey class attributes and methods
ORDB4ORA_PrimaryKey_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_PrimaryKey.attributes={ORDB4ORA_PrimaryKey_Name}

# ORDB4ORA_Parameter class attributes and methods
ORDB4ORA_Parameter_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Parameter.attributes={ORDB4ORA_Parameter_Name}

# ORDB4ORA_Procedure class attributes and methods

# ORDB4ORA_ROWIDType class attributes and methods
ORDB4ORA_ROWIDType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_ROWIDType_Size_Min: Property = Property(name="Size_Min", type=IntegerType)
ORDB4ORA_ROWIDType_Size_Max: Property = Property(name="Size_Max", type=IntegerType)
ORDB4ORA_ROWIDType.attributes={ORDB4ORA_ROWIDType_Descriptor, ORDB4ORA_ROWIDType_Size_Max, ORDB4ORA_ROWIDType_Size_Min}

# ORDB4ORA_RawFeature class attributes and methods
ORDB4ORA_RawFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_RawFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_RawFeature.attributes={ORDB4ORA_RawFeature_value, ORDB4ORA_RawFeature_key}

# ORDB4ORA_ReferenceType class attributes and methods
ORDB4ORA_ReferenceType_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_ReferenceType.attributes={ORDB4ORA_ReferenceType_Name}

# ORDB4ORA_Restriction class attributes and methods

# ORDB4ORA_StructuralComponent class attributes and methods
ORDB4ORA_StructuralComponent_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_StructuralComponent.attributes={ORDB4ORA_StructuralComponent_Name}

# ORDB4ORA_RowFeature class attributes and methods
ORDB4ORA_RowFeature_key: Property = Property(name="key", type=StringType)
ORDB4ORA_RowFeature_value: Property = Property(name="value", type=StringType)
ORDB4ORA_RowFeature.attributes={ORDB4ORA_RowFeature_value, ORDB4ORA_RowFeature_key}

# ORDB4ORA_SpacialType class attributes and methods
ORDB4ORA_SpacialType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_SpacialType.attributes={ORDB4ORA_SpacialType_Descriptor}

# ORDB4ORA_StoredNestedTable class attributes and methods
ORDB4ORA_StoredNestedTable_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_StoredNestedTable.attributes={ORDB4ORA_StoredNestedTable_Name}

# ORDB4ORA_TypedTable class attributes and methods

# ORDB4ORA_SuppliedType class attributes and methods

# ORDB4ORA_Trigger class attributes and methods
ORDB4ORA_Trigger_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Trigger_Body: Property = Property(name="Body", type=StringType)
ORDB4ORA_Trigger_Event: Property = Property(name="Event", type=StringType)
ORDB4ORA_Trigger_Action: Property = Property(name="Action", type=StringType)
ORDB4ORA_Trigger.attributes={ORDB4ORA_Trigger_Name, ORDB4ORA_Trigger_Event, ORDB4ORA_Trigger_Body, ORDB4ORA_Trigger_Action}

# ORDB4ORA_Unique class attributes and methods
ORDB4ORA_Unique_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Unique.attributes={ORDB4ORA_Unique_Name}

# Table class attributes and methods

# ORDB4ORA_Varray class attributes and methods
ORDB4ORA_Varray_Name: Property = Property(name="Name", type=StringType)
ORDB4ORA_Varray_NumElements: Property = Property(name="NumElements", type=IntegerType)
ORDB4ORA_Varray.attributes={ORDB4ORA_Varray_Name, ORDB4ORA_Varray_NumElements}

# ORDB4ORA_XMLType class attributes and methods
ORDB4ORA_XMLType_Descriptor: Property = Property(name="Descriptor", type=StringType)
ORDB4ORA_XMLType.attributes={ORDB4ORA_XMLType_Descriptor}

# ORDB4ORA_DerivedTable class attributes and methods
ORDB4ORA_DerivedTable_query_expression: Property = Property(name="query_expression", type=StringType)
ORDB4ORA_DerivedTable.attributes={ORDB4ORA_DerivedTable_query_expression}

# ORDB4ORA_View class attributes and methods

# DerivedTable class attributes and methods

# Relationships
structured0: BinaryAssociation = BinaryAssociation(
    name="structured0",
    ends={
        Property(name="StructuredType", type=ORDB4ORA_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
table1: BinaryAssociation = BinaryAssociation(
    name="table1",
    ends={
        Property(name="Table", type=ORDB4ORA_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1))
    }
)
model2: BinaryAssociation = BinaryAssociation(
    name="model2",
    ends={
        Property(name="Model", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1))
    }
)
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="ORDB4ORA_Table", type=ORDB4ORA_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_ForeignKey", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1))
    }
)
Return4: BinaryAssociation = BinaryAssociation(
    name="Return4",
    ends={
        Property(name="ORDB4ORA_Function", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Datatype", type=ORDB4ORA_Function, multiplicity=Multiplicity(1, 1))
    }
)
override6: BinaryAssociation = BinaryAssociation(
    name="override6",
    ends={
        Property(name="ORDB4ORA_Method", type=ORDB4ORA_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Method5", type=ORDB4ORA_Method, multiplicity=Multiplicity(0, 1))
    }
)
structured7: BinaryAssociation = BinaryAssociation(
    name="structured7",
    ends={
        Property(name="StructuredType8", type=ORDB4ORA_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="MethodParameter", type=ORDB4ORA_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method10", type=ORDB4ORA_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType11: BinaryAssociation = BinaryAssociation(
    name="returnType11",
    ends={
        Property(name="ORDB4ORA_Datatype13", type=ORDB4ORA_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Method12", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1))
    }
)
method14: BinaryAssociation = BinaryAssociation(
    name="method14",
    ends={
        Property(name="Method", type=ORDB4ORA_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=ORDB4ORA_Method, multiplicity=Multiplicity(0, 1))
    }
)
datatype15: BinaryAssociation = BinaryAssociation(
    name="datatype15",
    ends={
        Property(name="Datatype", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
table16: BinaryAssociation = BinaryAssociation(
    name="table16",
    ends={
        Property(name="Table18", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model17", type=ORDB4ORA_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation19: BinaryAssociation = BinaryAssociation(
    name="operation19",
    ends={
        Property(name="Operation", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model20", type=ORDB4ORA_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationParameters25: BinaryAssociation = BinaryAssociation(
    name="operationParameters25",
    ends={
        Property(name="OperationParameter", type=ORDB4ORA_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=ORDB4ORA_OperationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package21: BinaryAssociation = BinaryAssociation(
    name="package21",
    ends={
        Property(name="Package", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model22", type=ORDB4ORA_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type23: BinaryAssociation = BinaryAssociation(
    name="Type23",
    ends={
        Property(name="ORDB4ORA_Datatype24", type=ORDB4ORA_NestedTableType, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_NestedTableType", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1))
    }
)
model26: BinaryAssociation = BinaryAssociation(
    name="model26",
    ends={
        Property(name="Model28", type=ORDB4ORA_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation27", type=ORDB4ORA_Model, multiplicity=Multiplicity(0, 1))
    }
)
package29: BinaryAssociation = BinaryAssociation(
    name="package29",
    ends={
        Property(name="Package30", type=ORDB4ORA_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=ORDB4ORA_Package, multiplicity=Multiplicity(0, 1))
    }
)
operation31: BinaryAssociation = BinaryAssociation(
    name="operation31",
    ends={
        Property(name="Operation32", type=ORDB4ORA_OperationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="operationParameters", type=ORDB4ORA_Operation, multiplicity=Multiplicity(0, 1))
    }
)
operations33: BinaryAssociation = BinaryAssociation(
    name="operations33",
    ends={
        Property(name="Operation34", type=ORDB4ORA_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=ORDB4ORA_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model35: BinaryAssociation = BinaryAssociation(
    name="model35",
    ends={
        Property(name="Model37", type=ORDB4ORA_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package36", type=ORDB4ORA_Model, multiplicity=Multiplicity(1, 1))
    }
)
Type38: BinaryAssociation = BinaryAssociation(
    name="Type38",
    ends={
        Property(name="ORDB4ORA_Datatype39", type=ORDB4ORA_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Parameter", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1))
    }
)
table42: BinaryAssociation = BinaryAssociation(
    name="table42",
    ends={
        Property(name="Table43", type=ORDB4ORA_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restriction", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1))
    }
)
Type40: BinaryAssociation = BinaryAssociation(
    name="Type40",
    ends={
        Property(name="ORDB4ORA_StructuredType", type=ORDB4ORA_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_ReferenceType", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
attributes41: BinaryAssociation = BinaryAssociation(
    name="attributes41",
    ends={
        Property(name="StructuralComponent", type=ORDB4ORA_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)
restrictions50: BinaryAssociation = BinaryAssociation(
    name="restrictions50",
    ends={
        Property(name="Restriction", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=ORDB4ORA_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
attribute44: BinaryAssociation = BinaryAssociation(
    name="attribute44",
    ends={
        Property(name="ORDB4ORA_Attribute", type=ORDB4ORA_StoredNestedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_StoredNestedTable", type=ORDB4ORA_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
typed45: BinaryAssociation = BinaryAssociation(
    name="typed45",
    ends={
        Property(name="TypedTable", type=ORDB4ORA_StoredNestedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="storedNested", type=ORDB4ORA_TypedTable, multiplicity=Multiplicity(0, 1))
    }
)
Type46: BinaryAssociation = BinaryAssociation(
    name="Type46",
    ends={
        Property(name="ORDB4ORA_Datatype47", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_StructuralComponent", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1))
    }
)
features48: BinaryAssociation = BinaryAssociation(
    name="features48",
    ends={
        Property(name="ORDB4ORA_Feature", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_StructuralComponent49", type=ORDB4ORA_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute51: BinaryAssociation = BinaryAssociation(
    name="attribute51",
    ends={
        Property(name="Attribute", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured", type=ORDB4ORA_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method52: BinaryAssociation = BinaryAssociation(
    name="method52",
    ends={
        Property(name="Method54", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured53", type=ORDB4ORA_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typed55: BinaryAssociation = BinaryAssociation(
    name="typed55",
    ends={
        Property(name="TypedTable56", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structuredType", type=ORDB4ORA_TypedTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertype58: BinaryAssociation = BinaryAssociation(
    name="supertype58",
    ends={
        Property(name="ORDB4ORA_StructuredType59", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_StructuredType57", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
triggers67: BinaryAssociation = BinaryAssociation(
    name="triggers67",
    ends={
        Property(name="table68", type=ORDB4ORA_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Trigger", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1))
    }
)
restriction60: BinaryAssociation = BinaryAssociation(
    name="restriction60",
    ends={
        Property(name="Restriction61", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=ORDB4ORA_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns62: BinaryAssociation = BinaryAssociation(
    name="columns62",
    ends={
        Property(name="Column", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table63", type=ORDB4ORA_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model64: BinaryAssociation = BinaryAssociation(
    name="model64",
    ends={
        Property(name="Model66", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table65", type=ORDB4ORA_Model, multiplicity=Multiplicity(0, 1))
    }
)
updateColumns69: BinaryAssociation = BinaryAssociation(
    name="updateColumns69",
    ends={
        Property(name="ORDB4ORA_StructuralComponent70", type=ORDB4ORA_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Trigger", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)
table71: BinaryAssociation = BinaryAssociation(
    name="table71",
    ends={
        Property(name="Table72", type=ORDB4ORA_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 1))
    }
)
storedNested73: BinaryAssociation = BinaryAssociation(
    name="storedNested73",
    ends={
        Property(name="StoredNestedTable", type=ORDB4ORA_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed", type=ORDB4ORA_StoredNestedTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredType74: BinaryAssociation = BinaryAssociation(
    name="structuredType74",
    ends={
        Property(name="StructuredType76", type=ORDB4ORA_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed75", type=ORDB4ORA_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
Type77: BinaryAssociation = BinaryAssociation(
    name="Type77",
    ends={
        Property(name="ORDB4ORA_Datatype78", type=ORDB4ORA_Varray, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_Varray", type=ORDB4ORA_Datatype, multiplicity=Multiplicity(1, 1))
    }
)
tables79: BinaryAssociation = BinaryAssociation(
    name="tables79",
    ends={
        Property(name="ORDB4ORA_Table80", type=ORDB4ORA_View, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_View", type=ORDB4ORA_Table, multiplicity=Multiplicity(1, 9999))
    }
)
components81: BinaryAssociation = BinaryAssociation(
    name="components81",
    ends={
        Property(name="ORDB4ORA_StructuralComponent83", type=ORDB4ORA_View, multiplicity=Multiplicity(1, 1)),
        Property(name="ORDB4ORA_View82", type=ORDB4ORA_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_ORDB4ORA_ANSICharacterType_ANSIType = Generalization(general=ANSIType, specific=ORDB4ORA_ANSICharacterType)
gen_ORDB4ORA_ANSINumberType_ANSIType = Generalization(general=ANSIType, specific=ORDB4ORA_ANSINumberType)
gen_ORDB4ORA_ANSIType_BasicDataType = Generalization(general=BasicDataType, specific=ORDB4ORA_ANSIType)
gen_ORDB4ORA_AnyType_SuppliedType = Generalization(general=SuppliedType, specific=ORDB4ORA_AnyType)
gen_ORDB4ORA_Attribute_StructuralComponent = Generalization(general=StructuralComponent, specific=ORDB4ORA_Attribute)
gen_ORDB4ORA_BasicDataType_Datatype = Generalization(general=Datatype, specific=ORDB4ORA_BasicDataType)
gen_ORDB4ORA_BuiltInCharacterType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_BuiltInCharacterType)
gen_ORDB4ORA_BuiltInNumberType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_BuiltInNumberType)
gen_ORDB4ORA_BuiltInType_BasicDataType = Generalization(general=BasicDataType, specific=ORDB4ORA_BuiltInType)
gen_ORDB4ORA_CharacterFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_CharacterFeature)
gen_ORDB4ORA_Check_Restriction = Generalization(general=Restriction, specific=ORDB4ORA_Check)
gen_ORDB4ORA_Column_StructuralComponent = Generalization(general=StructuralComponent, specific=ORDB4ORA_Column)
gen_ORDB4ORA_DatetimeFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_DatetimeFeature)
gen_ORDB4ORA_DatetimeType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_DatetimeType)
gen_ORDB4ORA_ForeignKey_Restriction = Generalization(general=Restriction, specific=ORDB4ORA_ForeignKey)
gen_ORDB4ORA_Function_Operation = Generalization(general=Operation, specific=ORDB4ORA_Function)
gen_ORDB4ORA_IntervalFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_IntervalFeature)
gen_ORDB4ORA_LOBType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_LOBType)
gen_ORDB4ORA_LongAndRawType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_LongAndRawType)
gen_ORDB4ORA_MediaType_SuppliedType = Generalization(general=SuppliedType, specific=ORDB4ORA_MediaType)
gen_ORDB4ORA_MethodParameter_Parameter = Generalization(general=Parameter_, specific=ORDB4ORA_MethodParameter)
gen_ORDB4ORA_NestedTableType_Datatype = Generalization(general=Datatype, specific=ORDB4ORA_NestedTableType)
gen_ORDB4ORA_NotNull_Restriction = Generalization(general=Restriction, specific=ORDB4ORA_NotNull)
gen_ORDB4ORA_NumberFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_NumberFeature)
gen_ORDB4ORA_PrimaryKey_Restriction = Generalization(general=Restriction, specific=ORDB4ORA_PrimaryKey)
gen_ORDB4ORA_OperationParameter_Parameter = Generalization(general=Parameter_, specific=ORDB4ORA_OperationParameter)
gen_ORDB4ORA_Procedure_Operation = Generalization(general=Operation, specific=ORDB4ORA_Procedure)
gen_ORDB4ORA_ROWIDType_BuiltInType = Generalization(general=BuiltInType, specific=ORDB4ORA_ROWIDType)
gen_ORDB4ORA_RawFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_RawFeature)
gen_ORDB4ORA_ReferenceType_Datatype = Generalization(general=Datatype, specific=ORDB4ORA_ReferenceType)
gen_ORDB4ORA_StructuredType_Datatype = Generalization(general=Datatype, specific=ORDB4ORA_StructuredType)
gen_ORDB4ORA_RowFeature_Feature = Generalization(general=Feature, specific=ORDB4ORA_RowFeature)
gen_ORDB4ORA_SpacialType_SuppliedType = Generalization(general=SuppliedType, specific=ORDB4ORA_SpacialType)
gen_ORDB4ORA_SuppliedType_BasicDataType = Generalization(general=BasicDataType, specific=ORDB4ORA_SuppliedType)
gen_ORDB4ORA_Unique_Restriction = Generalization(general=Restriction, specific=ORDB4ORA_Unique)
gen_ORDB4ORA_TypedTable_Table = Generalization(general=Table, specific=ORDB4ORA_TypedTable)
gen_ORDB4ORA_Varray_Datatype = Generalization(general=Datatype, specific=ORDB4ORA_Varray)
gen_ORDB4ORA_XMLType_SuppliedType = Generalization(general=SuppliedType, specific=ORDB4ORA_XMLType)
gen_ORDB4ORA_DerivedTable_Table = Generalization(general=Table, specific=ORDB4ORA_DerivedTable)
gen_ORDB4ORA_View_DerivedTable = Generalization(general=DerivedTable, specific=ORDB4ORA_View)

# Domain Model
domain_model = DomainModel(
    name="ORDB4ORA",
    types={ORDB4ORA_ANSICharacterType, ANSIType, ORDB4ORA_ANSINumberType, ORDB4ORA_ANSIType, BasicDataType, ORDB4ORA_AnyType, SuppliedType, ORDB4ORA_Attribute, StructuralComponent, ORDB4ORA_StructuredType, ORDB4ORA_BasicDataType, Datatype, ORDB4ORA_BuiltInCharacterType, BuiltInType, ORDB4ORA_BuiltInNumberType, ORDB4ORA_BuiltInType, ORDB4ORA_CharacterFeature, Feature, ORDB4ORA_Check, Restriction, ORDB4ORA_Column, ORDB4ORA_Table, ORDB4ORA_Datatype, ORDB4ORA_Model, ORDB4ORA_DatetimeFeature, ORDB4ORA_DatetimeType, ORDB4ORA_Feature, ORDB4ORA_ForeignKey, ORDB4ORA_Function, Operation, ORDB4ORA_IntervalFeature, ORDB4ORA_LOBType, ORDB4ORA_LongAndRawType, ORDB4ORA_MediaType, ORDB4ORA_Method, ORDB4ORA_MethodParameter, Parameter_, ORDB4ORA_Operation, ORDB4ORA_OperationParameter, ORDB4ORA_Package, ORDB4ORA_NestedTableType, ORDB4ORA_NotNull, ORDB4ORA_NumberFeature, ORDB4ORA_PrimaryKey, ORDB4ORA_Parameter, ORDB4ORA_Procedure, ORDB4ORA_ROWIDType, ORDB4ORA_RawFeature, ORDB4ORA_ReferenceType, ORDB4ORA_Restriction, ORDB4ORA_StructuralComponent, ORDB4ORA_RowFeature, ORDB4ORA_SpacialType, ORDB4ORA_StoredNestedTable, ORDB4ORA_TypedTable, ORDB4ORA_SuppliedType, ORDB4ORA_Trigger, ORDB4ORA_Unique, Table, ORDB4ORA_Varray, ORDB4ORA_XMLType, ORDB4ORA_DerivedTable, ORDB4ORA_View, DerivedTable, ANSICharacterTypes, ANSINumberTypes, BuiltInCharacterSemantics, BuiltInCharacterTypes, BuiltInDatetimeTypes, BuiltInLOBType, BuiltInLongAndRawTypes, BuiltInROWIDType, BuiltNumberTypes, CharacterFeatures, DatetimeFeatures, IntervalFeatures, NumberFeatures, ONDELETEActions, ParameterMode, RawFeatures, RowFeatures, SuppliedAnyTypes, SuppliedMediaTypes, SuppliedSpacialTypes, SuppliedXMLTypes, TriggerActionTime, TriggerEvent},
    associations={structured0, table1, model2, reference3, Return4, override6, structured7, parameters9, returnType11, method14, datatype15, table16, operation19, operationParameters25, package21, Type23, model26, package29, operation31, operations33, model35, Type38, table42, Type40, attributes41, restrictions50, attribute44, typed45, Type46, features48, attribute51, method52, typed55, supertype58, triggers67, restriction60, columns62, model64, updateColumns69, table71, storedNested73, structuredType74, Type77, tables79, components81},
    generalizations={gen_ORDB4ORA_ANSICharacterType_ANSIType, gen_ORDB4ORA_ANSINumberType_ANSIType, gen_ORDB4ORA_ANSIType_BasicDataType, gen_ORDB4ORA_AnyType_SuppliedType, gen_ORDB4ORA_Attribute_StructuralComponent, gen_ORDB4ORA_BasicDataType_Datatype, gen_ORDB4ORA_BuiltInCharacterType_BuiltInType, gen_ORDB4ORA_BuiltInNumberType_BuiltInType, gen_ORDB4ORA_BuiltInType_BasicDataType, gen_ORDB4ORA_CharacterFeature_Feature, gen_ORDB4ORA_Check_Restriction, gen_ORDB4ORA_Column_StructuralComponent, gen_ORDB4ORA_DatetimeFeature_Feature, gen_ORDB4ORA_DatetimeType_BuiltInType, gen_ORDB4ORA_ForeignKey_Restriction, gen_ORDB4ORA_Function_Operation, gen_ORDB4ORA_IntervalFeature_Feature, gen_ORDB4ORA_LOBType_BuiltInType, gen_ORDB4ORA_LongAndRawType_BuiltInType, gen_ORDB4ORA_MediaType_SuppliedType, gen_ORDB4ORA_MethodParameter_Parameter, gen_ORDB4ORA_NestedTableType_Datatype, gen_ORDB4ORA_NotNull_Restriction, gen_ORDB4ORA_NumberFeature_Feature, gen_ORDB4ORA_PrimaryKey_Restriction, gen_ORDB4ORA_OperationParameter_Parameter, gen_ORDB4ORA_Procedure_Operation, gen_ORDB4ORA_ROWIDType_BuiltInType, gen_ORDB4ORA_RawFeature_Feature, gen_ORDB4ORA_ReferenceType_Datatype, gen_ORDB4ORA_StructuredType_Datatype, gen_ORDB4ORA_RowFeature_Feature, gen_ORDB4ORA_SpacialType_SuppliedType, gen_ORDB4ORA_SuppliedType_BasicDataType, gen_ORDB4ORA_Unique_Restriction, gen_ORDB4ORA_TypedTable_Table, gen_ORDB4ORA_Varray_Datatype, gen_ORDB4ORA_XMLType_SuppliedType, gen_ORDB4ORA_DerivedTable_Table, gen_ORDB4ORA_View_DerivedTable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)