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
myDsl_Model = Class(name="myDsl::Model")
myDsl_Greeting = Class(name="myDsl::Greeting")
myDsl_TypeA = Class(name="myDsl::TypeA")
myDsl_TypeB = Class(name="myDsl::TypeB")
TypeA = Class(name="TypeA")

# myDsl_Model class attributes and methods

# myDsl_Greeting class attributes and methods
myDsl_Greeting_name: Property = Property(name="name", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_name}

# myDsl_TypeA class attributes and methods
myDsl_TypeA_name: Property = Property(name="name", type=StringType)
myDsl_TypeA.attributes={myDsl_TypeA_name}

# myDsl_TypeB class attributes and methods
myDsl_TypeB_fullname: Property = Property(name="fullname", type=StringType)
myDsl_TypeB.attributes={myDsl_TypeB_fullname}

# TypeA class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_TypeB_TypeA = Generalization(general=TypeA, specific=myDsl_TypeB)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Greeting, myDsl_TypeA, myDsl_TypeB, TypeA},
    associations={greetings0},
    generalizations={gen_myDsl_TypeB_TypeA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)