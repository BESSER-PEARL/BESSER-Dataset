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
NewEnum1: Enumeration = Enumeration(
    name="NewEnum1",
    literals={
            EnumerationLiteral(name="LITERAL0"),
			EnumerationLiteral(name="LITERAL1"),
			EnumerationLiteral(name="LITERAL2")
    }
)

# Classes
statesml_Events = Class(name="statesml_Events")
statesml_NewEClass3 = Class(name="statesml_NewEClass3")
statesml_NewEClass4 = Class(name="statesml_NewEClass4")
statesml_Transition = Class(name="statesml_Transition")
Node = Class(name="Node")
statesml_Trigger = Class(name="statesml_Trigger")
statesml_State = Class(name="statesml_State", is_abstract=True)
statesml_StatesMLModel = Class(name="statesml_StatesMLModel")
statesml_Node = Class(name="statesml_Node", is_abstract=True)
statesml_SystemUnit = Class(name="statesml_SystemUnit", is_abstract=True)
statesml_Edge = Class(name="statesml_Edge")
statesml_Attribute = Class(name="statesml_Attribute")
statesml_Function = Class(name="statesml_Function")
statesml_Constant = Class(name="statesml_Constant")
statesml_NewEClass21 = Class(name="statesml_NewEClass21")
statesml_NewEClass22 = Class(name="statesml_NewEClass22")
statesml_ChangeEvent = Class(name="statesml_ChangeEvent")
Event = Class(name="Event")
statesml_Attributes = Class(name="statesml_Attributes")
statesml_InitialState = Class(name="statesml_InitialState")
State = Class(name="State")
statesml_TerminalState = Class(name="statesml_TerminalState")
statesml_Event = Class(name="statesml_Event", is_abstract=True)
statesml_SelectionDivergence = Class(name="statesml_SelectionDivergence")
statesml_SelectionConvergence = Class(name="statesml_SelectionConvergence")
statesml_RegularState = Class(name="statesml_RegularState")
KeyValuePair = Class(name="KeyValuePair")
statesml_Parameter = Class(name="statesml_Parameter")
statesml_DataType = Class(name="statesml_DataType", is_abstract=True)
statesml_KeyValuePair = Class(name="statesml_KeyValuePair", is_abstract=True)
statesml_SystemUnitLibrary = Class(name="statesml_SystemUnitLibrary", is_abstract=True)
statesml_DataTypeLibrary = Class(name="statesml_DataTypeLibrary", is_abstract=True)

# statesml_Events class attributes and methods

# statesml_NewEClass3 class attributes and methods

# statesml_NewEClass4 class attributes and methods

# statesml_Transition class attributes and methods

# Node class attributes and methods

# statesml_Trigger class attributes and methods
statesml_Trigger_m_fire: Method = Method(name="fire", parameters={Parameter(name='statesml_event', type=StringType)})
statesml_Trigger.methods={statesml_Trigger_m_fire}

# statesml_State class attributes and methods

# statesml_StatesMLModel class attributes and methods

# statesml_Node class attributes and methods
statesml_Node_name: Property = Property(name="name", type=StringType)
statesml_Node.attributes={statesml_Node_name}

# statesml_SystemUnit class attributes and methods
statesml_SystemUnit_name: Property = Property(name="name", type=StringType)
statesml_SystemUnit.attributes={statesml_SystemUnit_name}

# statesml_Edge class attributes and methods
statesml_Edge_name: Property = Property(name="name", type=StringType)
statesml_Edge.attributes={statesml_Edge_name}

# statesml_Attribute class attributes and methods

# statesml_Function class attributes and methods
statesml_Function_name: Property = Property(name="name", type=StringType)
statesml_Function.attributes={statesml_Function_name}

# statesml_Constant class attributes and methods

# statesml_NewEClass21 class attributes and methods

# statesml_NewEClass22 class attributes and methods

# statesml_ChangeEvent class attributes and methods

# Event class attributes and methods

# statesml_Attributes class attributes and methods

# statesml_InitialState class attributes and methods

# State class attributes and methods

# statesml_TerminalState class attributes and methods

# statesml_Event class attributes and methods
statesml_Event_name: Property = Property(name="name", type=StringType)
statesml_Event_m_eventOccured: Method = Method(name="eventOccured", parameters={})
statesml_Event.attributes={statesml_Event_name}
statesml_Event.methods={statesml_Event_m_eventOccured}

# statesml_SelectionDivergence class attributes and methods

# statesml_SelectionConvergence class attributes and methods

# statesml_RegularState class attributes and methods

# KeyValuePair class attributes and methods

# statesml_Parameter class attributes and methods

# statesml_DataType class attributes and methods
statesml_DataType_name: Property = Property(name="name", type=StringType)
statesml_DataType.attributes={statesml_DataType_name}

# statesml_KeyValuePair class attributes and methods
statesml_KeyValuePair_name: Property = Property(name="name", type=StringType)
statesml_KeyValuePair.attributes={statesml_KeyValuePair_name}

# statesml_SystemUnitLibrary class attributes and methods
statesml_SystemUnitLibrary_name: Property = Property(name="name", type=StringType)
statesml_SystemUnitLibrary.attributes={statesml_SystemUnitLibrary_name}

# statesml_DataTypeLibrary class attributes and methods
statesml_DataTypeLibrary_name: Property = Property(name="name", type=StringType)
statesml_DataTypeLibrary.attributes={statesml_DataTypeLibrary_name}

# Relationships
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="statesml_Attribute", type=statesml_StatesMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesMLModel6", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node7: BinaryAssociation = BinaryAssociation(
    name="node7",
    ends={
        Property(name="Node", type=statesml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=statesml_Node, multiplicity=Multiplicity(0, 9999))
    }
)
trigger8: BinaryAssociation = BinaryAssociation(
    name="trigger8",
    ends={
        Property(name="statesml_Trigger", type=statesml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Transition", type=statesml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition9: BinaryAssociation = BinaryAssociation(
    name="transition9",
    ends={
        Property(name="Transition", type=statesml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=statesml_Transition, multiplicity=Multiplicity(2, 2))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="statesml_Node", type=statesml_StatesMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesMLModel", type=statesml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunits1: BinaryAssociation = BinaryAssociation(
    name="systemunits1",
    ends={
        Property(name="statesml_SystemUnit", type=statesml_StatesMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesMLModel2", type=statesml_SystemUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="statesml_Edge", type=statesml_StatesMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesMLModel4", type=statesml_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls22: BinaryAssociation = BinaryAssociation(
    name="calls22",
    ends={
        Property(name="statesml_Function", type=statesml_RegularState, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_RegularState", type=statesml_Function, multiplicity=Multiplicity(0, 9999))
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="statesml_Attribute25", type=statesml_SystemUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnit24", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions26: BinaryAssociation = BinaryAssociation(
    name="functions26",
    ends={
        Property(name="statesml_Function28", type=statesml_SystemUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnit27", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger10: BinaryAssociation = BinaryAssociation(
    name="trigger10",
    ends={
        Property(name="statesml_Trigger11", type=statesml_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Event", type=statesml_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
diverges12: BinaryAssociation = BinaryAssociation(
    name="diverges12",
    ends={
        Property(name="statesml_Transition13", type=statesml_SelectionDivergence, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SelectionDivergence", type=statesml_Transition, multiplicity=Multiplicity(2, 9999))
    }
)
converges14: BinaryAssociation = BinaryAssociation(
    name="converges14",
    ends={
        Property(name="statesml_Transition15", type=statesml_SelectionConvergence, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SelectionConvergence", type=statesml_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
preceedingNode16: BinaryAssociation = BinaryAssociation(
    name="preceedingNode16",
    ends={
        Property(name="statesml_Node18", type=statesml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Edge17", type=statesml_Node, multiplicity=Multiplicity(1, 1))
    }
)
succeedingNode19: BinaryAssociation = BinaryAssociation(
    name="succeedingNode19",
    ends={
        Property(name="statesml_Node21", type=statesml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Edge20", type=statesml_Node, multiplicity=Multiplicity(1, 1))
    }
)
inputParams29: BinaryAssociation = BinaryAssociation(
    name="inputParams29",
    ends={
        Property(name="statesml_Parameter", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function30", type=statesml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParams31: BinaryAssociation = BinaryAssociation(
    name="outputParams31",
    ends={
        Property(name="statesml_Parameter33", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function32", type=statesml_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defines34: BinaryAssociation = BinaryAssociation(
    name="defines34",
    ends={
        Property(name="statesml_Function35", type=statesml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataType", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasType36: BinaryAssociation = BinaryAssociation(
    name="hasType36",
    ends={
        Property(name="statesml_DataType37", type=statesml_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_KeyValuePair", type=statesml_DataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unitCollection38: BinaryAssociation = BinaryAssociation(
    name="unitCollection38",
    ends={
        Property(name="statesml_SystemUnit39", type=statesml_SystemUnitLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnitLibrary", type=statesml_SystemUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types40: BinaryAssociation = BinaryAssociation(
    name="types40",
    ends={
        Property(name="statesml_DataType41", type=statesml_DataTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataTypeLibrary", type=statesml_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statesml_Transition_Node = Generalization(general=Node, specific=statesml_Transition)
gen_statesml_State_Node = Generalization(general=Node, specific=statesml_State)
gen_statesml_ChangeEvent_Event = Generalization(general=Event, specific=statesml_ChangeEvent)
gen_statesml_InitialState_State = Generalization(general=State, specific=statesml_InitialState)
gen_statesml_TerminalState_State = Generalization(general=State, specific=statesml_TerminalState)
gen_statesml_SelectionDivergence_Node = Generalization(general=Node, specific=statesml_SelectionDivergence)
gen_statesml_SelectionConvergence_Node = Generalization(general=Node, specific=statesml_SelectionConvergence)
gen_statesml_RegularState_State = Generalization(general=State, specific=statesml_RegularState)
gen_statesml_Attribute_KeyValuePair = Generalization(general=KeyValuePair, specific=statesml_Attribute)
gen_statesml_Parameter_KeyValuePair = Generalization(general=KeyValuePair, specific=statesml_Parameter)

# Domain Model
domain_model = DomainModel(
    name="statesml",
    types={statesml_Events, statesml_NewEClass3, statesml_NewEClass4, statesml_Transition, Node, statesml_Trigger, statesml_State, statesml_StatesMLModel, statesml_Node, statesml_SystemUnit, statesml_Edge, statesml_Attribute, statesml_Function, statesml_Constant, statesml_NewEClass21, statesml_NewEClass22, statesml_ChangeEvent, Event, statesml_Attributes, statesml_InitialState, State, statesml_TerminalState, statesml_Event, statesml_SelectionDivergence, statesml_SelectionConvergence, statesml_RegularState, KeyValuePair, statesml_Parameter, statesml_DataType, statesml_KeyValuePair, statesml_SystemUnitLibrary, statesml_DataTypeLibrary, NewEnum1},
    associations={attributes5, node7, trigger8, transition9, nodes0, systemunits1, edges3, calls22, attributes23, functions26, trigger10, diverges12, converges14, preceedingNode16, succeedingNode19, inputParams29, outputParams31, defines34, hasType36, unitCollection38, types40},
    generalizations={gen_statesml_Transition_Node, gen_statesml_State_Node, gen_statesml_ChangeEvent_Event, gen_statesml_InitialState_State, gen_statesml_TerminalState_State, gen_statesml_SelectionDivergence_Node, gen_statesml_SelectionConvergence_Node, gen_statesml_RegularState_State, gen_statesml_Attribute_KeyValuePair, gen_statesml_Parameter_KeyValuePair},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)