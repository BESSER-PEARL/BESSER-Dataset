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
tree_Node = Class(name="tree::Node")
tree_Data = Class(name="tree::Data")

# tree_Node class attributes and methods
tree_Node_name: Property = Property(name="name", type=StringType)
tree_Node.attributes={tree_Node_name}

# tree_Data class attributes and methods
tree_Data_name: Property = Property(name="name", type=StringType)
tree_Data.attributes={tree_Data_name}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="Node", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=tree_Node, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Node4", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data5: BinaryAssociation = BinaryAssociation(
    name="data5",
    ends={
        Property(name="Data", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=tree_Data, multiplicity=Multiplicity(0, 1))
    }
)
relatedNodes7: BinaryAssociation = BinaryAssociation(
    name="relatedNodes7",
    ends={
        Property(name="tree_Node6", type=tree_Node, multiplicity=Multiplicity(0, 9999)),
        Property(name="tree_Node", type=tree_Node, multiplicity=Multiplicity(1, 1))
    }
)
node8: BinaryAssociation = BinaryAssociation(
    name="node8",
    ends={
        Property(name="Node9", type=tree_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=tree_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Node, tree_Data},
    associations={parent1, children3, data5, relatedNodes7, node8},
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