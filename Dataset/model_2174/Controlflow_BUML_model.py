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
controlflow_Node = Class(name="controlflow::Node", is_abstract=True)
controlflow_Graph = Class(name="controlflow::Graph")
controlflow_Command = Class(name="controlflow::Command")
Node = Class(name="Node")
controlflow_Branch = Class(name="controlflow::Branch")

# controlflow_Node class attributes and methods

# controlflow_Graph class attributes and methods

# controlflow_Command class attributes and methods

# Node class attributes and methods

# controlflow_Branch class attributes and methods

# Relationships
next1: BinaryAssociation = BinaryAssociation(
    name="next1",
    ends={
        Property(name="controlflow_Node", type=controlflow_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="controlflow_Node0", type=controlflow_Node, multiplicity=Multiplicity(0, 1))
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="controlflow_Node3", type=controlflow_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="controlflow_Graph", type=controlflow_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root4: BinaryAssociation = BinaryAssociation(
    name="root4",
    ends={
        Property(name="controlflow_Node6", type=controlflow_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="controlflow_Graph5", type=controlflow_Node, multiplicity=Multiplicity(0, 1))
    }
)
positive7: BinaryAssociation = BinaryAssociation(
    name="positive7",
    ends={
        Property(name="controlflow_Node8", type=controlflow_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="controlflow_Branch", type=controlflow_Node, multiplicity=Multiplicity(0, 1))
    }
)
negative9: BinaryAssociation = BinaryAssociation(
    name="negative9",
    ends={
        Property(name="controlflow_Node11", type=controlflow_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="controlflow_Branch10", type=controlflow_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_controlflow_Command_Node = Generalization(general=Node, specific=controlflow_Command)
gen_controlflow_Branch_Node = Generalization(general=Node, specific=controlflow_Branch)

# Domain Model
domain_model = DomainModel(
    name="controlflow",
    types={controlflow_Node, controlflow_Graph, controlflow_Command, Node, controlflow_Branch},
    associations={next1, nodes2, root4, positive7, negative9},
    generalizations={gen_controlflow_Command_Node, gen_controlflow_Branch_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)