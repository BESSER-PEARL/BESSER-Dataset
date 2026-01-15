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
anytype_B = Class(name="anytype::B")
anytype_C = Class(name="anytype::C")
anytype_TestAny = Class(name="anytype::TestAny")
anytype_EObject = Class(name="anytype::EObject")
anytype_A = Class(name="anytype::A")

# anytype_B class attributes and methods
anytype_B_name: Property = Property(name="name", type=StringType)
anytype_B.attributes={anytype_B_name}

# anytype_C class attributes and methods

# anytype_TestAny class attributes and methods
anytype_TestAny_name: Property = Property(name="name", type=StringType)
anytype_TestAny_any: Property = Property(name="any", type=StringType)
anytype_TestAny_a: Property = Property(name="a", type=StringType)
anytype_TestAny_myAny: Property = Property(name="myAny", type=StringType)
anytype_TestAny.attributes={anytype_TestAny_name, anytype_TestAny_myAny, anytype_TestAny_a, anytype_TestAny_any}

# anytype_EObject class attributes and methods

# anytype_A class attributes and methods
anytype_A_name: Property = Property(name="name", type=StringType)
anytype_A_doub: Property = Property(name="doub", type=StringType)
anytype_A_lon: Property = Property(name="lon", type=StringType)
anytype_A.attributes={anytype_A_lon, anytype_A_doub, anytype_A_name}

# Relationships
myB0: BinaryAssociation = BinaryAssociation(
    name="myB0",
    ends={
        Property(name="anytype_B", type=anytype_A, multiplicity=Multiplicity(1, 1)),
        Property(name="anytype_A", type=anytype_B, multiplicity=Multiplicity(1, 1))
    }
)
singleAnyType1: BinaryAssociation = BinaryAssociation(
    name="singleAnyType1",
    ends={
        Property(name="anytype_EObject", type=anytype_TestAny, multiplicity=Multiplicity(1, 1)),
        Property(name="anytype_TestAny", type=anytype_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiAnyType2: BinaryAssociation = BinaryAssociation(
    name="multiAnyType2",
    ends={
        Property(name="anytype_EObject4", type=anytype_TestAny, multiplicity=Multiplicity(1, 1)),
        Property(name="anytype_TestAny3", type=anytype_EObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="anytype",
    types={anytype_B, anytype_C, anytype_TestAny, anytype_EObject, anytype_A},
    associations={myB0, singleAnyType1, multiAnyType2},
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