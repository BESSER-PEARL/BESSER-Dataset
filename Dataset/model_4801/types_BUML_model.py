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
TestEnum: Enumeration = Enumeration(
    name="TestEnum",
    literals={
            EnumerationLiteral(name="Enum0"),
			EnumerationLiteral(name="Enum1"),
			EnumerationLiteral(name="Enum2")
    }
)

TestNextEnum: Enumeration = Enumeration(
    name="TestNextEnum",
    literals={
            EnumerationLiteral(name="Enum1"),
			EnumerationLiteral(name="Enum2")
    }
)

# Classes
types_SingleTypes = Class(name="types::SingleTypes")
types_ManyTypes = Class(name="types::ManyTypes")

# types_SingleTypes class attributes and methods
types_SingleTypes_date: Property = Property(name="date", type=DateType)
types_SingleTypes_stringArray: Property = Property(name="stringArray", type=StringType)
types_SingleTypes_longArray: Property = Property(name="longArray", type=StringType)
types_SingleTypes_string: Property = Property(name="string", type=StringType)
types_SingleTypes_integer: Property = Property(name="integer", type=IntegerType)
types_SingleTypes_integerObject: Property = Property(name="integerObject", type=StringType)
types_SingleTypes_long: Property = Property(name="long", type=StringType)
types_SingleTypes_longObject: Property = Property(name="longObject", type=StringType)
types_SingleTypes_double: Property = Property(name="double", type=FloatType)
types_SingleTypes_doubleObject: Property = Property(name="doubleObject", type=StringType)
types_SingleTypes_float: Property = Property(name="float", type=FloatType)
types_SingleTypes_floatObject: Property = Property(name="floatObject", type=StringType)
types_SingleTypes_clazz: Property = Property(name="clazz", type=StringType)
types_SingleTypes_char: Property = Property(name="char", type=StringType)
types_SingleTypes_charObject: Property = Property(name="charObject", type=StringType)
types_SingleTypes_byte: Property = Property(name="byte", type=StringType)
types_SingleTypes_byteObject: Property = Property(name="byteObject", type=StringType)
types_SingleTypes_byteArray: Property = Property(name="byteArray", type=StringType)
types_SingleTypes_bigDecimal: Property = Property(name="bigDecimal", type=StringType)
types_SingleTypes_bigInteger: Property = Property(name="bigInteger", type=StringType)
types_SingleTypes_enum: Property = Property(name="enum", type=StringType)
types_SingleTypes_nextEnum: Property = Property(name="nextEnum", type=StringType)
types_SingleTypes.attributes={types_SingleTypes_date, types_SingleTypes_byte, types_SingleTypes_bigInteger, types_SingleTypes_integer, types_SingleTypes_nextEnum, types_SingleTypes_char, types_SingleTypes_clazz, types_SingleTypes_bigDecimal, types_SingleTypes_longArray, types_SingleTypes_charObject, types_SingleTypes_enum, types_SingleTypes_string, types_SingleTypes_float, types_SingleTypes_integerObject, types_SingleTypes_double, types_SingleTypes_longObject, types_SingleTypes_floatObject, types_SingleTypes_long, types_SingleTypes_byteArray, types_SingleTypes_byteObject, types_SingleTypes_stringArray, types_SingleTypes_doubleObject}

# types_ManyTypes class attributes and methods
types_ManyTypes_string: Property = Property(name="string", type=StringType)
types_ManyTypes_integerObject: Property = Property(name="integerObject", type=StringType)
types_ManyTypes_long: Property = Property(name="long", type=StringType)
types_ManyTypes_doubleObject: Property = Property(name="doubleObject", type=StringType)
types_ManyTypes_floatObject: Property = Property(name="floatObject", type=StringType)
types_ManyTypes_clazz: Property = Property(name="clazz", type=StringType)
types_ManyTypes_charObject: Property = Property(name="charObject", type=StringType)
types_ManyTypes_byteObject: Property = Property(name="byteObject", type=StringType)
types_ManyTypes_byteArray: Property = Property(name="byteArray", type=StringType)
types_ManyTypes_bigDecimal: Property = Property(name="bigDecimal", type=StringType)
types_ManyTypes_bigInteger: Property = Property(name="bigInteger", type=StringType)
types_ManyTypes_enum: Property = Property(name="enum", type=StringType)
types_ManyTypes_date: Property = Property(name="date", type=DateType)
types_ManyTypes_stringArray: Property = Property(name="stringArray", type=StringType)
types_ManyTypes_longArray: Property = Property(name="longArray", type=StringType)
types_ManyTypes.attributes={types_ManyTypes_stringArray, types_ManyTypes_floatObject, types_ManyTypes_integerObject, types_ManyTypes_byteObject, types_ManyTypes_string, types_ManyTypes_date, types_ManyTypes_longArray, types_ManyTypes_bigDecimal, types_ManyTypes_byteArray, types_ManyTypes_doubleObject, types_ManyTypes_clazz, types_ManyTypes_bigInteger, types_ManyTypes_long, types_ManyTypes_charObject, types_ManyTypes_enum}

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_SingleTypes, types_ManyTypes, TestEnum, TestNextEnum},
    associations={},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)