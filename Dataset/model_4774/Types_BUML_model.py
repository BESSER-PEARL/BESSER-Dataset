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
types_Type = Class(name="types::Type", is_abstract=True)
types_Boolean = Class(name="types::Boolean")
Simple = Class(name="Simple")
types_Branch = Class(name="types::Branch")
Element = Class(name="Element")
types_Field = Class(name="types::Field")
types_Case = Class(name="types::Case")
types_Array = Class(name="types::Array")
Collection = Class(name="Collection")
types_Short = Class(name="types::Short")
types_SignedInt = Class(name="types::SignedInt", is_abstract=True)
Int = Class(name="Int")
types_Simple = Class(name="types::Simple", is_abstract=True)
types_String = Class(name="types::String")
types_Struct = Class(name="types::Struct")
types_Char = Class(name="types::Char")
types_Collection = Class(name="types::Collection", is_abstract=True)
Type = Class(name="Type")
types_Double = Class(name="types::Double")
FloatingPoint = Class(name="FloatingPoint")
types_Enum = Class(name="types::Enum")
types_Float = Class(name="types::Float")
types_FloatingPoint = Class(name="types::FloatingPoint", is_abstract=True)
types_Int = Class(name="types::Int", is_abstract=True)
types_Key = Class(name="types::Key")
types_Long = Class(name="types::Long")
SignedInt = Class(name="SignedInt")
types_LongDouble = Class(name="types::LongDouble")
types_LongLong = Class(name="types::LongLong")
types_Octet = Class(name="types::Octet")
types_Sequence = Class(name="types::Sequence")
types_Typedef = Class(name="types::Typedef")
types_ULong = Class(name="types::ULong")
UnsignedInt = Class(name="UnsignedInt")
types_ULongLong = Class(name="types::ULongLong")
types_UShort = Class(name="types::UShort")
types_Union = Class(name="types::Union")
types_UnsignedInt = Class(name="types::UnsignedInt", is_abstract=True)
types_WChar = Class(name="types::WChar")
types_WString = Class(name="types::WString")
types_DataLib = Class(name="types::DataLib")
OpenDDSLib = Class(name="OpenDDSLib")

# types_Type class attributes and methods

# types_Boolean class attributes and methods

# Simple class attributes and methods

# types_Branch class attributes and methods

# Element class attributes and methods

# types_Field class attributes and methods
types_Field_name: Property = Property(name="name", type=StringType)
types_Field.attributes={types_Field_name}

# types_Case class attributes and methods
types_Case_literal: Property = Property(name="literal", type=StringType)
types_Case.attributes={types_Case_literal}

# types_Array class attributes and methods

# Collection class attributes and methods

# types_Short class attributes and methods

# types_SignedInt class attributes and methods

# Int class attributes and methods

# types_Simple class attributes and methods

# types_String class attributes and methods

# types_Struct class attributes and methods
types_Struct_name: Property = Property(name="name", type=StringType)
types_Struct_isDcpsDataType: Property = Property(name="isDcpsDataType", type=BooleanType)
types_Struct.attributes={types_Struct_name, types_Struct_isDcpsDataType}

# types_Char class attributes and methods

# types_Collection class attributes and methods
types_Collection_length: Property = Property(name="length", type=StringType)
types_Collection.attributes={types_Collection_length}

# Type class attributes and methods

# types_Double class attributes and methods

# FloatingPoint class attributes and methods

# types_Enum class attributes and methods
types_Enum_name: Property = Property(name="name", type=StringType)
types_Enum_literals: Property = Property(name="literals", type=StringType)
types_Enum.attributes={types_Enum_name, types_Enum_literals}

# types_Float class attributes and methods

# types_FloatingPoint class attributes and methods

# types_Int class attributes and methods

# types_Key class attributes and methods

# types_Long class attributes and methods

# SignedInt class attributes and methods

# types_LongDouble class attributes and methods

# types_LongLong class attributes and methods

# types_Octet class attributes and methods

# types_Sequence class attributes and methods

# types_Typedef class attributes and methods
types_Typedef_name: Property = Property(name="name", type=StringType)
types_Typedef.attributes={types_Typedef_name}

# types_ULong class attributes and methods

# UnsignedInt class attributes and methods

# types_ULongLong class attributes and methods

# types_UShort class attributes and methods

# types_Union class attributes and methods
types_Union_name: Property = Property(name="name", type=StringType)
types_Union.attributes={types_Union_name}

# types_UnsignedInt class attributes and methods

# types_WChar class attributes and methods

# types_WString class attributes and methods

# types_DataLib class attributes and methods

# OpenDDSLib class attributes and methods

# Relationships
subtype0: BinaryAssociation = BinaryAssociation(
    name="subtype0",
    ends={
        Property(name="types_Type", type=types_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Array", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
field1: BinaryAssociation = BinaryAssociation(
    name="field1",
    ends={
        Property(name="types_Field", type=types_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Branch", type=types_Field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases2: BinaryAssociation = BinaryAssociation(
    name="cases2",
    ends={
        Property(name="types_Case", type=types_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Branch3", type=types_Case, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subtype9: BinaryAssociation = BinaryAssociation(
    name="subtype9",
    ends={
        Property(name="types_Type10", type=types_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Sequence", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
fields11: BinaryAssociation = BinaryAssociation(
    name="fields11",
    ends={
        Property(name="types_Field12", type=types_Struct, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Struct", type=types_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="types_Type6", type=types_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Field5", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
field7: BinaryAssociation = BinaryAssociation(
    name="field7",
    ends={
        Property(name="types_Field8", type=types_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Key", type=types_Field, multiplicity=Multiplicity(1, 1))
    }
)
keys13: BinaryAssociation = BinaryAssociation(
    name="keys13",
    ends={
        Property(name="types_Key15", type=types_Struct, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Struct14", type=types_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="types_Type17", type=types_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Typedef", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
branches18: BinaryAssociation = BinaryAssociation(
    name="branches18",
    ends={
        Property(name="types_Branch19", type=types_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Union", type=types_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
switch20: BinaryAssociation = BinaryAssociation(
    name="switch20",
    ends={
        Property(name="types_Type22", type=types_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Union21", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
default23: BinaryAssociation = BinaryAssociation(
    name="default23",
    ends={
        Property(name="types_Field25", type=types_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Union24", type=types_Field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types26: BinaryAssociation = BinaryAssociation(
    name="types26",
    ends={
        Property(name="types_Type27", type=types_DataLib, multiplicity=Multiplicity(1, 1)),
        Property(name="types_DataLib", type=types_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_types_Boolean_Simple = Generalization(general=Simple, specific=types_Boolean)
gen_types_Branch_Element = Generalization(general=Element, specific=types_Branch)
gen_types_Case_Element = Generalization(general=Element, specific=types_Case)
gen_types_Array_Collection = Generalization(general=Collection, specific=types_Array)
gen_types_Short_SignedInt = Generalization(general=SignedInt, specific=types_Short)
gen_types_SignedInt_Int = Generalization(general=Int, specific=types_SignedInt)
gen_types_Simple_Type = Generalization(general=Type, specific=types_Simple)
gen_types_String_Collection = Generalization(general=Collection, specific=types_String)
gen_types_Struct_Type = Generalization(general=Type, specific=types_Struct)
gen_types_Char_Simple = Generalization(general=Simple, specific=types_Char)
gen_types_Collection_Type = Generalization(general=Type, specific=types_Collection)
gen_types_Double_FloatingPoint = Generalization(general=FloatingPoint, specific=types_Double)
gen_types_Enum_Simple = Generalization(general=Simple, specific=types_Enum)
gen_types_Field_Element = Generalization(general=Element, specific=types_Field)
gen_types_Float_FloatingPoint = Generalization(general=FloatingPoint, specific=types_Float)
gen_types_FloatingPoint_Simple = Generalization(general=Simple, specific=types_FloatingPoint)
gen_types_Int_Simple = Generalization(general=Simple, specific=types_Int)
gen_types_Key_Element = Generalization(general=Element, specific=types_Key)
gen_types_Long_SignedInt = Generalization(general=SignedInt, specific=types_Long)
gen_types_LongDouble_FloatingPoint = Generalization(general=FloatingPoint, specific=types_LongDouble)
gen_types_LongLong_SignedInt = Generalization(general=SignedInt, specific=types_LongLong)
gen_types_Octet_Simple = Generalization(general=Simple, specific=types_Octet)
gen_types_Sequence_Collection = Generalization(general=Collection, specific=types_Sequence)
gen_types_Type_Element = Generalization(general=Element, specific=types_Type)
gen_types_Typedef_Type = Generalization(general=Type, specific=types_Typedef)
gen_types_ULong_UnsignedInt = Generalization(general=UnsignedInt, specific=types_ULong)
gen_types_ULongLong_UnsignedInt = Generalization(general=UnsignedInt, specific=types_ULongLong)
gen_types_UShort_UnsignedInt = Generalization(general=UnsignedInt, specific=types_UShort)
gen_types_Union_Type = Generalization(general=Type, specific=types_Union)
gen_types_UnsignedInt_Int = Generalization(general=Int, specific=types_UnsignedInt)
gen_types_WChar_Simple = Generalization(general=Simple, specific=types_WChar)
gen_types_WString_Collection = Generalization(general=Collection, specific=types_WString)
gen_types_DataLib_OpenDDSLib = Generalization(general=OpenDDSLib, specific=types_DataLib)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Type, types_Boolean, Simple, types_Branch, Element, types_Field, types_Case, types_Array, Collection, types_Short, types_SignedInt, Int, types_Simple, types_String, types_Struct, types_Char, types_Collection, Type, types_Double, FloatingPoint, types_Enum, types_Float, types_FloatingPoint, types_Int, types_Key, types_Long, SignedInt, types_LongDouble, types_LongLong, types_Octet, types_Sequence, types_Typedef, types_ULong, UnsignedInt, types_ULongLong, types_UShort, types_Union, types_UnsignedInt, types_WChar, types_WString, types_DataLib, OpenDDSLib},
    associations={subtype0, field1, cases2, subtype9, fields11, type4, field7, keys13, type16, branches18, switch20, default23, types26},
    generalizations={gen_types_Boolean_Simple, gen_types_Branch_Element, gen_types_Case_Element, gen_types_Array_Collection, gen_types_Short_SignedInt, gen_types_SignedInt_Int, gen_types_Simple_Type, gen_types_String_Collection, gen_types_Struct_Type, gen_types_Char_Simple, gen_types_Collection_Type, gen_types_Double_FloatingPoint, gen_types_Enum_Simple, gen_types_Field_Element, gen_types_Float_FloatingPoint, gen_types_FloatingPoint_Simple, gen_types_Int_Simple, gen_types_Key_Element, gen_types_Long_SignedInt, gen_types_LongDouble_FloatingPoint, gen_types_LongLong_SignedInt, gen_types_Octet_Simple, gen_types_Sequence_Collection, gen_types_Type_Element, gen_types_Typedef_Type, gen_types_ULong_UnsignedInt, gen_types_ULongLong_UnsignedInt, gen_types_UShort_UnsignedInt, gen_types_Union_Type, gen_types_UnsignedInt_Int, gen_types_WChar_Simple, gen_types_WString_Collection, gen_types_DataLib_OpenDDSLib},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)