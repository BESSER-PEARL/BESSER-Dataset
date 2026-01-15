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
Attribute_NodeIn = Class(name="Attribute::NodeIn")
Attribute_NodeOut = Class(name="Attribute::NodeOut")
Attribute_NodeInOut = Class(name="Attribute::NodeInOut")
Attribute_NodeVar = Class(name="Attribute::NodeVar")

# Attribute_NodeIn class attributes and methods
Attribute_NodeIn_Number: Property = Property(name="Number", type=IntegerType)
Attribute_NodeIn.attributes={Attribute_NodeIn_Number}

# Attribute_NodeOut class attributes and methods
Attribute_NodeOut_Number: Property = Property(name="Number", type=IntegerType)
Attribute_NodeOut.attributes={Attribute_NodeOut_Number}

# Attribute_NodeInOut class attributes and methods
Attribute_NodeInOut_Number: Property = Property(name="Number", type=IntegerType)
Attribute_NodeInOut.attributes={Attribute_NodeInOut_Number}

# Attribute_NodeVar class attributes and methods
Attribute_NodeVar_Number: Property = Property(name="Number", type=IntegerType)
Attribute_NodeVar.attributes={Attribute_NodeVar_Number}

# Domain Model
domain_model = DomainModel(
    name="Attribute",
    types={Attribute_NodeIn, Attribute_NodeOut, Attribute_NodeInOut, Attribute_NodeVar},
    associations={},
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