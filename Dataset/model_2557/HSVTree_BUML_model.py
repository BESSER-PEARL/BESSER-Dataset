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
HSVTree_HSVNode = Class(name="HSVTree::HSVNode")

# HSVTree_HSVNode class attributes and methods
HSVTree_HSVNode_hsv: Property = Property(name="hsv", type=StringType)
HSVTree_HSVNode_name: Property = Property(name="name", type=StringType)
HSVTree_HSVNode.attributes={HSVTree_HSVNode_name, HSVTree_HSVNode_hsv}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="HSVNode", type=HSVTree_HSVNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=HSVTree_HSVNode, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="HSVNode4", type=HSVTree_HSVNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=HSVTree_HSVNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="HSVTree",
    types={HSVTree_HSVNode},
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