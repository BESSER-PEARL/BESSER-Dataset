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

# Enumerations
DataTypes: Enumeration = Enumeration(
    name="DataTypes",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="boolean")
    }
)

PseudoTypes: Enumeration = Enumeration(
    name="PseudoTypes",
    literals={
            EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory")
    }
)

IOTypes: Enumeration = Enumeration(
    name="IOTypes",
    literals={
            EnumerationLiteral(name="local"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="input")
    }
)

TriggerTypes: Enumeration = Enumeration(
    name="TriggerTypes",
    literals={
            EnumerationLiteral(name="either"),
			EnumerationLiteral(name="rising"),
			EnumerationLiteral(name="falling"),
			EnumerationLiteral(name="functionCall")
    }
)

# Classes
statemachine_Region = Class(name="statemachine::Region")
statemachine_Node = Class(name="statemachine::Node")
statemachine_State = Class(name="statemachine::State")
Node = Class(name="Node")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Variable = Class(name="statemachine::Variable")
DataElement = Class(name="DataElement")
statemachine_Event = Class(name="statemachine::Event")
statemachine_Pseudostate = Class(name="statemachine::Pseudostate")
statemachine_DataElement = Class(name="statemachine::DataElement")
statemachine_FinalState = Class(name="statemachine::FinalState")
State = Class(name="State")
statemachine_Statechart = Class(name="statemachine::Statechart")

# statemachine_Region class attributes and methods
statemachine_Region_priority: Property = Property(name="priority", type=IntegerType)
statemachine_Region.attributes={statemachine_Region_priority}

# statemachine_Node class attributes and methods
statemachine_Node_name: Property = Property(name="name", type=StringType)
statemachine_Node_id: Property = Property(name="id", type=IntegerType)
statemachine_Node.attributes={statemachine_Node_name, statemachine_Node_id}

# statemachine_State class attributes and methods
statemachine_State_entry: Property = Property(name="entry", type=StringType)
statemachine_State_do: Property = Property(name="do", type=StringType)
statemachine_State_exit: Property = Property(name="exit", type=StringType)
statemachine_State.attributes={statemachine_State_entry, statemachine_State_exit, statemachine_State_do}

# Node class attributes and methods

# statemachine_Transition class attributes and methods
statemachine_Transition_expression: Property = Property(name="expression", type=StringType)
statemachine_Transition_id: Property = Property(name="id", type=IntegerType)
statemachine_Transition_priority: Property = Property(name="priority", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_priority, statemachine_Transition_id, statemachine_Transition_expression}

# statemachine_Variable class attributes and methods
statemachine_Variable_dataType: Property = Property(name="dataType", type=StringType)
statemachine_Variable.attributes={statemachine_Variable_dataType}

# DataElement class attributes and methods

# statemachine_Event class attributes and methods
statemachine_Event_trigger: Property = Property(name="trigger", type=StringType)
statemachine_Event.attributes={statemachine_Event_trigger}

# statemachine_Pseudostate class attributes and methods
statemachine_Pseudostate_pseudoType: Property = Property(name="pseudoType", type=StringType)
statemachine_Pseudostate.attributes={statemachine_Pseudostate_pseudoType}

# statemachine_DataElement class attributes and methods
statemachine_DataElement_name: Property = Property(name="name", type=StringType)
statemachine_DataElement_ioType: Property = Property(name="ioType", type=StringType)
statemachine_DataElement_port: Property = Property(name="port", type=IntegerType)
statemachine_DataElement.attributes={statemachine_DataElement_port, statemachine_DataElement_name, statemachine_DataElement_ioType}

# statemachine_FinalState class attributes and methods

# State class attributes and methods

# statemachine_Statechart class attributes and methods
statemachine_Statechart_name: Property = Property(name="name", type=StringType)
statemachine_Statechart_UUID: Property = Property(name="UUID", type=StringType)
statemachine_Statechart.attributes={statemachine_Statechart_name, statemachine_Statechart_UUID}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="statemachine_Node", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Region", type=statemachine_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceNode3: BinaryAssociation = BinaryAssociation(
    name="sourceNode3",
    ends={
        Property(name="statemachine_Node5", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition4", type=statemachine_Node, multiplicity=Multiplicity(1, 1))
    }
)
region6: BinaryAssociation = BinaryAssociation(
    name="region6",
    ends={
        Property(name="statemachine_Region7", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State", type=statemachine_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetNode1: BinaryAssociation = BinaryAssociation(
    name="targetNode1",
    ends={
        Property(name="statemachine_Node2", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition", type=statemachine_Node, multiplicity=Multiplicity(1, 1))
    }
)
dataElement8: BinaryAssociation = BinaryAssociation(
    name="dataElement8",
    ends={
        Property(name="statemachine_DataElement", type=statemachine_Statechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statechart", type=statemachine_DataElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region9: BinaryAssociation = BinaryAssociation(
    name="region9",
    ends={
        Property(name="statemachine_Region11", type=statemachine_Statechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statechart10", type=statemachine_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition12: BinaryAssociation = BinaryAssociation(
    name="transition12",
    ends={
        Property(name="statemachine_Transition14", type=statemachine_Statechart, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statechart13", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine_State_Node = Generalization(general=Node, specific=statemachine_State)
gen_statemachine_Variable_DataElement = Generalization(general=DataElement, specific=statemachine_Variable)
gen_statemachine_Event_DataElement = Generalization(general=DataElement, specific=statemachine_Event)
gen_statemachine_Pseudostate_Node = Generalization(general=Node, specific=statemachine_Pseudostate)
gen_statemachine_FinalState_State = Generalization(general=State, specific=statemachine_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Region, statemachine_Node, statemachine_State, Node, statemachine_Transition, statemachine_Variable, DataElement, statemachine_Event, statemachine_Pseudostate, statemachine_DataElement, statemachine_FinalState, State, statemachine_Statechart, DataTypes, PseudoTypes, IOTypes, TriggerTypes},
    associations={state0, sourceNode3, region6, targetNode1, dataElement8, region9, transition12},
    generalizations={gen_statemachine_State_Node, gen_statemachine_Variable_DataElement, gen_statemachine_Event_DataElement, gen_statemachine_Pseudostate_Node, gen_statemachine_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)