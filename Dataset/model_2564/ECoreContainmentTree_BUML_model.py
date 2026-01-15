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
eCoreContainemntTree_Node = Class(name="eCoreContainemntTree::Node")
eCoreContainemntTree_EObject = Class(name="eCoreContainemntTree::EObject")

# eCoreContainemntTree_Node class attributes and methods
eCoreContainemntTree_Node_name: Property = Property(name="name", type=StringType)
eCoreContainemntTree_Node.attributes={eCoreContainemntTree_Node_name}

# eCoreContainemntTree_EObject class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="Node", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(0, 9999))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Node4", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(0, 9999))
    }
)
element5: BinaryAssociation = BinaryAssociation(
    name="element5",
    ends={
        Property(name="eCoreContainemntTree_EObject", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="eCoreContainemntTree_Node", type=eCoreContainemntTree_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subTypes7: BinaryAssociation = BinaryAssociation(
    name="subTypes7",
    ends={
        Property(name="Node8", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="superTypes", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(0, 9999))
    }
)
superTypes10: BinaryAssociation = BinaryAssociation(
    name="superTypes10",
    ends={
        Property(name="Node11", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="subTypes", type=eCoreContainemntTree_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="eCoreContainemntTree",
    types={eCoreContainemntTree_Node, eCoreContainemntTree_EObject},
    associations={parent1, children3, element5, subTypes7, superTypes10},
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