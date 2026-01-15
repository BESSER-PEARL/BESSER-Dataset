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
HLSTree_HLSNode = Class(name="HLSTree::HLSNode")

# HLSTree_HLSNode class attributes and methods
HLSTree_HLSNode_hls: Property = Property(name="hls", type=StringType)
HLSTree_HLSNode_name: Property = Property(name="name", type=StringType)
HLSTree_HLSNode.attributes={HLSTree_HLSNode_name, HLSTree_HLSNode_hls}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="HLSNode", type=HLSTree_HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=HLSTree_HLSNode, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="HLSNode4", type=HLSTree_HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=HLSTree_HLSNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="HLSTree",
    types={HLSTree_HLSNode},
    associations={parent1, children3},
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