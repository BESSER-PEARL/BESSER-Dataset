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
primitives_Primitive = Class(name="primitives::Primitive")
primitives_Bag = Class(name="primitives::Bag")

# primitives_Primitive class attributes and methods
primitives_Primitive_bigdecimal: Property = Property(name="bigdecimal", type=StringType)
primitives_Primitive_bigint: Property = Property(name="bigint", type=StringType)
primitives_Primitive_boolean: Property = Property(name="boolean", type=BooleanType)
primitives_Primitive_booleanObj: Property = Property(name="booleanObj", type=StringType)
primitives_Primitive_byte: Property = Property(name="byte", type=StringType)
primitives_Primitive_byteArray: Property = Property(name="byteArray", type=StringType)
primitives_Primitive_byteObj: Property = Property(name="byteObj", type=StringType)
primitives_Primitive_char: Property = Property(name="char", type=StringType)
primitives_Primitive_characterObj: Property = Property(name="characterObj", type=StringType)
primitives_Primitive_date: Property = Property(name="date", type=DateType)
primitives_Primitive_double: Property = Property(name="double", type=FloatType)
primitives_Primitive_doubleObj: Property = Property(name="doubleObj", type=StringType)
primitives_Primitive_float: Property = Property(name="float", type=FloatType)
primitives_Primitive_floatObj: Property = Property(name="floatObj", type=StringType)
primitives_Primitive_int: Property = Property(name="int", type=IntegerType)
primitives_Primitive_integerObj: Property = Property(name="integerObj", type=StringType)
primitives_Primitive_javaClass: Property = Property(name="javaClass", type=StringType)
primitives_Primitive_javaObj: Property = Property(name="javaObj", type=StringType)
primitives_Primitive_long: Property = Property(name="long", type=StringType)
primitives_Primitive_longObj: Property = Property(name="longObj", type=StringType)
primitives_Primitive_short: Property = Property(name="short", type=StringType)
primitives_Primitive_shortObj: Property = Property(name="shortObj", type=StringType)
primitives_Primitive_string: Property = Property(name="string", type=StringType)
primitives_Primitive.attributes={primitives_Primitive_integerObj, primitives_Primitive_string, primitives_Primitive_int, primitives_Primitive_long, primitives_Primitive_booleanObj, primitives_Primitive_byteArray, primitives_Primitive_double, primitives_Primitive_boolean, primitives_Primitive_floatObj, primitives_Primitive_bigint, primitives_Primitive_javaObj, primitives_Primitive_date, primitives_Primitive_byteObj, primitives_Primitive_bigdecimal, primitives_Primitive_doubleObj, primitives_Primitive_short, primitives_Primitive_float, primitives_Primitive_longObj, primitives_Primitive_char, primitives_Primitive_characterObj, primitives_Primitive_javaClass, primitives_Primitive_byte, primitives_Primitive_shortObj}

# primitives_Bag class attributes and methods
primitives_Bag_id: Property = Property(name="id", type=StringType)
primitives_Bag.attributes={primitives_Bag_id}

# Relationships
values0: BinaryAssociation = BinaryAssociation(
    name="values0",
    ends={
        Property(name="primitives_Primitive", type=primitives_Bag, multiplicity=Multiplicity(1, 1)),
        Property(name="primitives_Bag", type=primitives_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="primitives_Bag3", type=primitives_Bag, multiplicity=Multiplicity(1, 1)),
        Property(name="primitives_Bag1", type=primitives_Bag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="primitives",
    types={primitives_Primitive, primitives_Bag},
    associations={values0, children2},
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