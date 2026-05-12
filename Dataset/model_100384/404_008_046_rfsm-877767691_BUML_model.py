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
rfsm_State = Class(name="rfsm_State")
Node = Class(name="Node")
rfsm_Node = Class(name="rfsm_Node")
rfsm_Connector = Class(name="rfsm_Connector")
rfsm_History = Class(name="rfsm_History")
rfsm_Transition = Class(name="rfsm_Transition")
rfsm_Function = Class(name="rfsm_Function")
rfsm_Event = Class(name="rfsm_Event")

# rfsm_State class attributes and methods

# Node class attributes and methods

# rfsm_Node class attributes and methods
rfsm_Node_name: Property = Property(name="name", type=StringType)
rfsm_Node.attributes={rfsm_Node_name}

# rfsm_Connector class attributes and methods
rfsm_Connector_public: Property = Property(name="public", type=BooleanType)
rfsm_Connector.attributes={rfsm_Connector_public}

# rfsm_History class attributes and methods
rfsm_History_depth: Property = Property(name="depth", type=IntegerType)
rfsm_History_hot: Property = Property(name="hot", type=BooleanType)
rfsm_History.attributes={rfsm_History_depth, rfsm_History_hot}

# rfsm_Transition class attributes and methods
rfsm_Transition_priority_number: Property = Property(name="priority_number", type=IntegerType)
rfsm_Transition_m_isAncestor: Method = Method(name="isAncestor", parameters={Parameter(name='rfsm_one', type=StringType), Parameter(name='rfsm_two', type=StringType)}, type=StringType)
rfsm_Transition_m_LCA: Method = Method(name="LCA", parameters={Parameter(name='rfsm_one', type=StringType), Parameter(name='rfsm_two', type=StringType)}, type=StringType)
rfsm_Transition.attributes={rfsm_Transition_priority_number}
rfsm_Transition.methods={rfsm_Transition_m_LCA, rfsm_Transition_m_isAncestor}

# rfsm_Function class attributes and methods
rfsm_Function_sourcecode: Property = Property(name="sourcecode", type=StringType)
rfsm_Function.attributes={rfsm_Function_sourcecode}

# rfsm_Event class attributes and methods
rfsm_Event_eventliteral: Property = Property(name="eventliteral", type=StringType)
rfsm_Event.attributes={rfsm_Event_eventliteral}

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="State", type=rfsm_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="subnodes", type=rfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
exit7: BinaryAssociation = BinaryAssociation(
    name="exit7",
    ends={
        Property(name="rfsm_Function9", type=rfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_State8", type=rfsm_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=rfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subnodes2: BinaryAssociation = BinaryAssociation(
    name="subnodes2",
    ends={
        Property(name="Node", type=rfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=rfsm_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry3: BinaryAssociation = BinaryAssociation(
    name="entry3",
    ends={
        Property(name="rfsm_Function", type=rfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_State", type=rfsm_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doo4: BinaryAssociation = BinaryAssociation(
    name="doo4",
    ends={
        Property(name="rfsm_Function6", type=rfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_State5", type=rfsm_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner11: BinaryAssociation = BinaryAssociation(
    name="owner11",
    ends={
        Property(name="State12", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=rfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="rfsm_Node", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_Transition", type=rfsm_Node, multiplicity=Multiplicity(1, 1))
    }
)
history10: BinaryAssociation = BinaryAssociation(
    name="history10",
    ends={
        Property(name="rfsm_History", type=rfsm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_Connector", type=rfsm_History, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner25: BinaryAssociation = BinaryAssociation(
    name="owner25",
    ends={
        Property(name="Transition26", type=rfsm_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=rfsm_Transition, multiplicity=Multiplicity(0, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="rfsm_Node16", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_Transition15", type=rfsm_Node, multiplicity=Multiplicity(1, 1))
    }
)
events17: BinaryAssociation = BinaryAssociation(
    name="events17",
    ends={
        Property(name="Event", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="owner18", type=rfsm_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard19: BinaryAssociation = BinaryAssociation(
    name="guard19",
    ends={
        Property(name="rfsm_Function21", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_Transition20", type=rfsm_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect22: BinaryAssociation = BinaryAssociation(
    name="effect22",
    ends={
        Property(name="rfsm_Function24", type=rfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rfsm_Transition23", type=rfsm_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_rfsm_State_Node = Generalization(general=Node, specific=rfsm_State)
gen_rfsm_Connector_Node = Generalization(general=Node, specific=rfsm_Connector)

# Domain Model
domain_model = DomainModel(
    name="rfsm",
    types={rfsm_State, Node, rfsm_Node, rfsm_Connector, rfsm_History, rfsm_Transition, rfsm_Function, rfsm_Event},
    associations={parent0, exit7, transitions1, subnodes2, entry3, doo4, owner11, source13, history10, owner25, target14, events17, guard19, effect22},
    generalizations={gen_rfsm_State_Node, gen_rfsm_Connector_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)