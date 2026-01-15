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
myDsl_Greeting = Class(name="myDsl::Greeting")
myDsl_Expressao = Class(name="myDsl::Expressao")
Greeting = Class(name="Greeting")
myDsl_Selecao = Class(name="myDsl::Selecao")
myDsl_Define = Class(name="myDsl::Define")
myDsl_Model = Class(name="myDsl::Model")

# myDsl_Greeting class attributes and methods
myDsl_Greeting_value: Property = Property(name="value", type=IntegerType)
myDsl_Greeting.attributes={myDsl_Greeting_value}

# myDsl_Expressao class attributes and methods
myDsl_Expressao_name: Property = Property(name="name", type=StringType)
myDsl_Expressao.attributes={myDsl_Expressao_name}

# Greeting class attributes and methods

# myDsl_Selecao class attributes and methods

# myDsl_Define class attributes and methods

# myDsl_Model class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Exp1: BinaryAssociation = BinaryAssociation(
    name="Exp1",
    ends={
        Property(name="myDsl_Expressao", type=myDsl_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Greeting2", type=myDsl_Expressao, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Sel3: BinaryAssociation = BinaryAssociation(
    name="Sel3",
    ends={
        Property(name="myDsl_Selecao", type=myDsl_Define, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Define", type=myDsl_Selecao, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Expressao_Greeting = Generalization(general=Greeting, specific=myDsl_Expressao)
gen_myDsl_Selecao_Greeting = Generalization(general=Greeting, specific=myDsl_Selecao)
gen_myDsl_Define_Greeting = Generalization(general=Greeting, specific=myDsl_Define)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Greeting, myDsl_Expressao, Greeting, myDsl_Selecao, myDsl_Define, myDsl_Model},
    associations={greetings0, Exp1, Sel3},
    generalizations={gen_myDsl_Expressao_Greeting, gen_myDsl_Selecao_Greeting, gen_myDsl_Define_Greeting},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)