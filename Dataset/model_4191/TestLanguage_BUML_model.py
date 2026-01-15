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
testLanguage_Model = Class(name="testLanguage::Model")
testLanguage_Greeting = Class(name="testLanguage::Greeting")

# testLanguage_Model class attributes and methods

# testLanguage_Greeting class attributes and methods
testLanguage_Greeting_name: Property = Property(name="name", type=StringType)
testLanguage_Greeting.attributes={testLanguage_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="testLanguage_Greeting", type=testLanguage_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="testLanguage_Model", type=testLanguage_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testLanguage",
    types={testLanguage_Model, testLanguage_Greeting},
    associations={greetings0},
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