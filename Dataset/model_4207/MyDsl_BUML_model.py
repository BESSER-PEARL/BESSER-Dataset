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
myDsl_Model = Class(name="myDsl::Model")
myDsl_Define = Class(name="myDsl::Define")
Greeting = Class(name="Greeting")
myDsl_Lambda = Class(name="myDsl::Lambda")
myDsl_Square = Class(name="myDsl::Square")
myDsl_Conditional = Class(name="myDsl::Conditional")
myDsl_Operation = Class(name="myDsl::Operation")

# myDsl_Greeting class attributes and methods
myDsl_Greeting_value: Property = Property(name="value", type=IntegerType)
myDsl_Greeting_name: Property = Property(name="name", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_value, myDsl_Greeting_name}

# myDsl_Model class attributes and methods

# myDsl_Define class attributes and methods

# Greeting class attributes and methods

# myDsl_Lambda class attributes and methods

# myDsl_Square class attributes and methods

# myDsl_Conditional class attributes and methods
myDsl_Conditional_value2: Property = Property(name="value2", type=IntegerType)
myDsl_Conditional_value3: Property = Property(name="value3", type=IntegerType)
myDsl_Conditional.attributes={myDsl_Conditional_value3, myDsl_Conditional_value2}

# myDsl_Operation class attributes and methods
myDsl_Operation_op: Property = Property(name="op", type=StringType)
myDsl_Operation_value2: Property = Property(name="value2", type=IntegerType)
myDsl_Operation.attributes={myDsl_Operation_op, myDsl_Operation_value2}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Define_Greeting = Generalization(general=Greeting, specific=myDsl_Define)
gen_myDsl_Lambda_Greeting = Generalization(general=Greeting, specific=myDsl_Lambda)
gen_myDsl_Square_Greeting = Generalization(general=Greeting, specific=myDsl_Square)
gen_myDsl_Conditional_Greeting = Generalization(general=Greeting, specific=myDsl_Conditional)
gen_myDsl_Operation_Greeting = Generalization(general=Greeting, specific=myDsl_Operation)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Greeting, myDsl_Model, myDsl_Define, Greeting, myDsl_Lambda, myDsl_Square, myDsl_Conditional, myDsl_Operation},
    associations={greetings0},
    generalizations={gen_myDsl_Define_Greeting, gen_myDsl_Lambda_Greeting, gen_myDsl_Square_Greeting, gen_myDsl_Conditional_Greeting, gen_myDsl_Operation_Greeting},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)