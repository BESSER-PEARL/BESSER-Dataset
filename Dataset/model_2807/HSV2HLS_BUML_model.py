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
HSV2HLS_HLSNode = Class(name="HSV2HLS::HLSNode")
HSV2HLS_HSVNode2HLSNode = Class(name="HSV2HLS::HSVNode2HLSNode")
HSV2HLS_HSVNode = Class(name="HSV2HLS::HSVNode")

# HSV2HLS_HLSNode class attributes and methods

# HSV2HLS_HSVNode2HLSNode class attributes and methods
HSV2HLS_HSVNode2HLSNode_rgb: Property = Property(name="rgb", type=StringType)
HSV2HLS_HSVNode2HLSNode_name: Property = Property(name="name", type=StringType)
HSV2HLS_HSVNode2HLSNode.attributes={HSV2HLS_HSVNode2HLSNode_rgb, HSV2HLS_HSVNode2HLSNode_name}

# HSV2HLS_HSVNode class attributes and methods

# Relationships
hls6: BinaryAssociation = BinaryAssociation(
    name="hls6",
    ends={
        Property(name="HSV2HLS_HLSNode", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="HSV2HLS_HSVNode2HLSNode7", type=HSV2HLS_HLSNode, multiplicity=Multiplicity(1, 1))
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="HSVNode2HLSNode", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="HSVNode2HLSNode4", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hsv5: BinaryAssociation = BinaryAssociation(
    name="hsv5",
    ends={
        Property(name="HSV2HLS_HSVNode", type=HSV2HLS_HSVNode2HLSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="HSV2HLS_HSVNode2HLSNode", type=HSV2HLS_HSVNode, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="HSV2HLS",
    types={HSV2HLS_HLSNode, HSV2HLS_HSVNode2HLSNode, HSV2HLS_HSVNode},
    associations={hls6, parent1, children3, hsv5},
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