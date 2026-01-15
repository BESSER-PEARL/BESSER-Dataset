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
talltree_TallNode = Class(name="talltree::TallNode")

# talltree_TallNode class attributes and methods
talltree_TallNode_height: Property = Property(name="height", type=IntegerType)
talltree_TallNode_name: Property = Property(name="name", type=StringType)
talltree_TallNode.attributes={talltree_TallNode_height, talltree_TallNode_name}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="TallNode", type=talltree_TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=talltree_TallNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="TallNode4", type=talltree_TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=talltree_TallNode, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="talltree",
    types={talltree_TallNode},
    associations={children1, parent3},
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