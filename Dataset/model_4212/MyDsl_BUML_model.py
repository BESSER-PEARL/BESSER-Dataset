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
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_Define = Class(name="myDsl::Define")
Expression = Class(name="Expression")
myDsl_Lambda = Class(name="myDsl::Lambda")
myDsl_Conditional = Class(name="myDsl::Conditional")
myDsl_Operation = Class(name="myDsl::Operation")

# myDsl_Model class attributes and methods

# myDsl_Expression class attributes and methods
myDsl_Expression_value: Property = Property(name="value", type=IntegerType)
myDsl_Expression.attributes={myDsl_Expression_value}

# myDsl_Define class attributes and methods
myDsl_Define_name: Property = Property(name="name", type=StringType)
myDsl_Define.attributes={myDsl_Define_name}

# Expression class attributes and methods

# myDsl_Lambda class attributes and methods
myDsl_Lambda_name: Property = Property(name="name", type=StringType)
myDsl_Lambda.attributes={myDsl_Lambda_name}

# myDsl_Conditional class attributes and methods
myDsl_Conditional_name: Property = Property(name="name", type=StringType)
myDsl_Conditional_value2: Property = Property(name="value2", type=IntegerType)
myDsl_Conditional_value3: Property = Property(name="value3", type=IntegerType)
myDsl_Conditional.attributes={myDsl_Conditional_value2, myDsl_Conditional_value3, myDsl_Conditional_name}

# myDsl_Operation class attributes and methods
myDsl_Operation_op: Property = Property(name="op", type=StringType)
myDsl_Operation_value2: Property = Property(name="value2", type=IntegerType)
myDsl_Operation.attributes={myDsl_Operation_value2, myDsl_Operation_op}

# Relationships
expressions0: BinaryAssociation = BinaryAssociation(
    name="expressions0",
    ends={
        Property(name="myDsl_Expression", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Define_Expression = Generalization(general=Expression, specific=myDsl_Define)
gen_myDsl_Lambda_Expression = Generalization(general=Expression, specific=myDsl_Lambda)
gen_myDsl_Conditional_Expression = Generalization(general=Expression, specific=myDsl_Conditional)
gen_myDsl_Operation_Expression = Generalization(general=Expression, specific=myDsl_Operation)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Expression, myDsl_Define, Expression, myDsl_Lambda, myDsl_Conditional, myDsl_Operation},
    associations={expressions0},
    generalizations={gen_myDsl_Define_Expression, gen_myDsl_Lambda_Expression, gen_myDsl_Conditional_Expression, gen_myDsl_Operation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)