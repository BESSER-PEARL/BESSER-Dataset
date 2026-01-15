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
myDsl_Reponse = Class(name="myDsl::Reponse")
myDsl_ReponseT = Class(name="myDsl::ReponseT")
Reponse = Class(name="Reponse")
myDsl_ReponseF = Class(name="myDsl::ReponseF")

# myDsl_Model class attributes and methods

# myDsl_Greeting class attributes and methods
myDsl_Greeting_question: Property = Property(name="question", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_question}

# myDsl_Reponse class attributes and methods
myDsl_Reponse_name: Property = Property(name="name", type=StringType)
myDsl_Reponse.attributes={myDsl_Reponse_name}

# myDsl_ReponseT class attributes and methods

# Reponse class attributes and methods

# myDsl_ReponseF class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reponses1: BinaryAssociation = BinaryAssociation(
    name="reponses1",
    ends={
        Property(name="myDsl_Reponse", type=myDsl_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Greeting2", type=myDsl_Reponse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_ReponseT_Reponse = Generalization(general=Reponse, specific=myDsl_ReponseT)
gen_myDsl_ReponseF_Reponse = Generalization(general=Reponse, specific=myDsl_ReponseF)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Greeting, myDsl_Reponse, myDsl_ReponseT, Reponse, myDsl_ReponseF},
    associations={greetings0, reponses1},
    generalizations={gen_myDsl_ReponseT_Reponse, gen_myDsl_ReponseF_Reponse},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)