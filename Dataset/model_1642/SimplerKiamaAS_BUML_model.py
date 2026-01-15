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
kiamaas_Top = Class(name="kiamaas::Top")
kiamaas_Node = Class(name="kiamaas::Node", is_abstract=True)
kiamaas_Composite = Class(name="kiamaas::Composite")
Node = Class(name="Node")
kiamaas_Leaf = Class(name="kiamaas::Leaf")

# kiamaas_Top class attributes and methods

# kiamaas_Node class attributes and methods
kiamaas_Node_height: Property = Property(name="height", type=StringType)
kiamaas_Node_depth: Property = Property(name="depth", type=StringType)
kiamaas_Node.attributes={kiamaas_Node_depth, kiamaas_Node_height}

# kiamaas_Composite class attributes and methods

# Node class attributes and methods

# kiamaas_Leaf class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kiamaas_Node", type=kiamaas_Top, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamaas_Top", type=kiamaas_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="kiamaas_Node2", type=kiamaas_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamaas_Composite", type=kiamaas_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kiamaas_Composite_Node = Generalization(general=Node, specific=kiamaas_Composite)
gen_kiamaas_Leaf_Node = Generalization(general=Node, specific=kiamaas_Leaf)

# Domain Model
domain_model = DomainModel(
    name="kiamaas",
    types={kiamaas_Top, kiamaas_Node, kiamaas_Composite, Node, kiamaas_Leaf},
    associations={node0, child1},
    generalizations={gen_kiamaas_Composite_Node, gen_kiamaas_Leaf_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)