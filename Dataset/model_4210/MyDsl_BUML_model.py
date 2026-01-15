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
myDsl_Element = Class(name="myDsl::Element")
myDsl_Person = Class(name="myDsl::Person")
Element = Class(name="Element")
myDsl_Greeting = Class(name="myDsl::Greeting")

# myDsl_Model class attributes and methods

# myDsl_Element class attributes and methods

# myDsl_Person class attributes and methods
myDsl_Person_name: Property = Property(name="name", type=StringType)
myDsl_Person.attributes={myDsl_Person_name}

# Element class attributes and methods

# myDsl_Greeting class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_Element", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person1: BinaryAssociation = BinaryAssociation(
    name="person1",
    ends={
        Property(name="myDsl_Person", type=myDsl_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Greeting", type=myDsl_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_Person_Element = Generalization(general=Element, specific=myDsl_Person)
gen_myDsl_Greeting_Element = Generalization(general=Element, specific=myDsl_Greeting)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Element, myDsl_Person, Element, myDsl_Greeting},
    associations={elements0, person1},
    generalizations={gen_myDsl_Person_Element, gen_myDsl_Greeting_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)