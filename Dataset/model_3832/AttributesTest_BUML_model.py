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
attributeTest_Root = Class(name="attributeTest::Root")

# attributeTest_Root class attributes and methods
attributeTest_Root_shortPrimitive: Property = Property(name="shortPrimitive", type=StringType)
attributeTest_Root_bigDecimal: Property = Property(name="bigDecimal", type=StringType)
attributeTest_Root_bigInteger: Property = Property(name="bigInteger", type=StringType)
attributeTest_Root_boolPrimitive: Property = Property(name="boolPrimitive", type=BooleanType)
attributeTest_Root_boolObj: Property = Property(name="boolObj", type=StringType)
attributeTest_Root_bytePrimitive: Property = Property(name="bytePrimitive", type=StringType)
attributeTest_Root_byteObj: Property = Property(name="byteObj", type=StringType)
attributeTest_Root_byteArray: Property = Property(name="byteArray", type=StringType)
attributeTest_Root_charPrimitive: Property = Property(name="charPrimitive", type=StringType)
attributeTest_Root_charObj: Property = Property(name="charObj", type=StringType)
attributeTest_Root_doublePrimitive: Property = Property(name="doublePrimitive", type=FloatType)
attributeTest_Root_doubleObj: Property = Property(name="doubleObj", type=StringType)
attributeTest_Root_floatPrimitive: Property = Property(name="floatPrimitive", type=FloatType)
attributeTest_Root_floatObj: Property = Property(name="floatObj", type=StringType)
attributeTest_Root_intPrimitive: Property = Property(name="intPrimitive", type=IntegerType)
attributeTest_Root_intObj: Property = Property(name="intObj", type=StringType)
attributeTest_Root_javaObject: Property = Property(name="javaObject", type=StringType)
attributeTest_Root_longPrimitive: Property = Property(name="longPrimitive", type=StringType)
attributeTest_Root_longObj: Property = Property(name="longObj", type=StringType)
attributeTest_Root_shortObj: Property = Property(name="shortObj", type=StringType)
attributeTest_Root_eList: Property = Property(name="eList", type=StringType)
attributeTest_Root_date: Property = Property(name="date", type=DateType)
attributeTest_Root_stringObj: Property = Property(name="stringObj", type=StringType)
attributeTest_Root_listString: Property = Property(name="listString", type=StringType)
attributeTest_Root_listInt: Property = Property(name="listInt", type=IntegerType)
attributeTest_Root_listShort: Property = Property(name="listShort", type=StringType)
attributeTest_Root_listInt1: Property = Property(name="listInt1", type=IntegerType)
attributeTest_Root_listInt2: Property = Property(name="listInt2", type=IntegerType)
attributeTest_Root_map: Property = Property(name="map", type=StringType)
attributeTest_Root.attributes={attributeTest_Root_longPrimitive, attributeTest_Root_listInt1, attributeTest_Root_byteObj, attributeTest_Root_bigInteger, attributeTest_Root_javaObject, attributeTest_Root_stringObj, attributeTest_Root_listString, attributeTest_Root_doubleObj, attributeTest_Root_charPrimitive, attributeTest_Root_shortObj, attributeTest_Root_listShort, attributeTest_Root_map, attributeTest_Root_floatPrimitive, attributeTest_Root_intObj, attributeTest_Root_listInt, attributeTest_Root_longObj, attributeTest_Root_date, attributeTest_Root_boolPrimitive, attributeTest_Root_boolObj, attributeTest_Root_shortPrimitive, attributeTest_Root_intPrimitive, attributeTest_Root_eList, attributeTest_Root_floatObj, attributeTest_Root_bytePrimitive, attributeTest_Root_bigDecimal, attributeTest_Root_listInt2, attributeTest_Root_byteArray, attributeTest_Root_charObj, attributeTest_Root_doublePrimitive}

# Domain Model
domain_model = DomainModel(
    name="attributeTest",
    types={attributeTest_Root},
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