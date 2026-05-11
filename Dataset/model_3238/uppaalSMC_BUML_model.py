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
uppaalSMC_NSTA = Class(name="uppaalSMC_NSTA")
NTA = Class(name="NTA")
uppaalSMC_DoubleType = Class(name="uppaalSMC_DoubleType")
Type = Class(name="Type")
uppaalSMC_ChanceNode = Class(name="uppaalSMC_ChanceNode")
Location = Class(name="Location")
uppaalSMC_ChanceEdge = Class(name="uppaalSMC_ChanceEdge")
Edge = Class(name="Edge")
uppaalSMC_ExponentialLocation = Class(name="uppaalSMC_ExponentialLocation")
Expression = Class(name="Expression")

# uppaalSMC_NSTA class attributes and methods

# NTA class attributes and methods

# uppaalSMC_DoubleType class attributes and methods

# Type class attributes and methods

# uppaalSMC_ChanceNode class attributes and methods

# Location class attributes and methods

# uppaalSMC_ChanceEdge class attributes and methods
uppaalSMC_ChanceEdge_weight: Property = Property(name="weight", type=IntegerType)
uppaalSMC_ChanceEdge.attributes={uppaalSMC_ChanceEdge_weight}

# Edge class attributes and methods

# uppaalSMC_ExponentialLocation class attributes and methods

# Expression class attributes and methods

# Relationships
double0: BinaryAssociation = BinaryAssociation(
    name="double0",
    ends={
        Property(name="uppaalSMC_DoubleType", type=uppaalSMC_NSTA, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaalSMC_NSTA", type=uppaalSMC_DoubleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exitRate1: BinaryAssociation = BinaryAssociation(
    name="exitRate1",
    ends={
        Property(name="Expression", type=uppaalSMC_ExponentialLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaalSMC_ExponentialLocation", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_uppaalSMC_NSTA_NTA = Generalization(general=NTA, specific=uppaalSMC_NSTA)
gen_uppaalSMC_DoubleType_Type = Generalization(general=Type, specific=uppaalSMC_DoubleType)
gen_uppaalSMC_ChanceNode_Location = Generalization(general=Location, specific=uppaalSMC_ChanceNode)
gen_uppaalSMC_ChanceEdge_Edge = Generalization(general=Edge, specific=uppaalSMC_ChanceEdge)
gen_uppaalSMC_ExponentialLocation_Location = Generalization(general=Location, specific=uppaalSMC_ExponentialLocation)

# Domain Model
domain_model = DomainModel(
    name="uppaalSMC",
    types={uppaalSMC_NSTA, NTA, uppaalSMC_DoubleType, Type, uppaalSMC_ChanceNode, Location, uppaalSMC_ChanceEdge, Edge, uppaalSMC_ExponentialLocation, Expression},
    associations={double0, exitRate1},
    generalizations={gen_uppaalSMC_NSTA_NTA, gen_uppaalSMC_DoubleType_Type, gen_uppaalSMC_ChanceNode_Location, gen_uppaalSMC_ChanceEdge_Edge, gen_uppaalSMC_ExponentialLocation_Location},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)