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

# myDsl_Model class attributes and methods
myDsl_Model_name: Property = Property(name="name", type=StringType)
myDsl_Model.attributes={myDsl_Model_name}

# myDsl_Greeting class attributes and methods
myDsl_Greeting_name: Property = Property(name="name", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_name}

# Relationships
refModel1: BinaryAssociation = BinaryAssociation(
    name="refModel1",
    ends={
        Property(name="myDsl_Model", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model0", type=myDsl_Model, multiplicity=Multiplicity(0, 1))
    }
)
refModels3: BinaryAssociation = BinaryAssociation(
    name="refModels3",
    ends={
        Property(name="myDsl_Model4", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model2", type=myDsl_Model, multiplicity=Multiplicity(0, 9999))
    }
)
greetings5: BinaryAssociation = BinaryAssociation(
    name="greetings5",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model6", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Greeting},
    associations={refModel1, refModels3, greetings5},
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