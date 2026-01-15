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
helloBuck_Model = Class(name="helloBuck::Model")
helloBuck_Greeting = Class(name="helloBuck::Greeting")

# helloBuck_Model class attributes and methods

# helloBuck_Greeting class attributes and methods
helloBuck_Greeting_name: Property = Property(name="name", type=StringType)
helloBuck_Greeting.attributes={helloBuck_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="helloBuck_Greeting", type=helloBuck_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="helloBuck_Model", type=helloBuck_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloBuck",
    types={helloBuck_Model, helloBuck_Greeting},
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