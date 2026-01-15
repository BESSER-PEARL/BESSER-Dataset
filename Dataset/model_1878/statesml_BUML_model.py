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
statesml_SystemUnits = Class(name="statesml::SystemUnits")
statesml_Function = Class(name="statesml::Function")
statesml_Attribute = Class(name="statesml::Attribute")
statesml_Parameter = Class(name="statesml::Parameter")
statesml_DataType = Class(name="statesml::DataType")
statesml_SystemUnitLibrariy = Class(name="statesml::SystemUnitLibrariy")
statesml_DataTypeLibrary = Class(name="statesml::DataTypeLibrary")
statesml_State = Class(name="statesml::State")
Node = Class(name="Node")
statesml_Transition = Class(name="statesml::Transition")
statesml_SelectionDivergence = Class(name="statesml::SelectionDivergence")
statesml_SelectionConvergence = Class(name="statesml::SelectionConvergence")
statesml_StatesML = Class(name="statesml::StatesML")
statesml_Event = Class(name="statesml::Event", is_abstract=True)
statesml_ChangeEvent = Class(name="statesml::ChangeEvent")
statesml_Node = Class(name="statesml::Node", is_abstract=True)
statesml_Edge = Class(name="statesml::Edge")
Event = Class(name="Event")
statesml_Trigger = Class(name="statesml::Trigger")

# statesml_SystemUnits class attributes and methods
statesml_SystemUnits_name: Property = Property(name="name", type=StringType)
statesml_SystemUnits.attributes={statesml_SystemUnits_name}

# statesml_Function class attributes and methods
statesml_Function_name: Property = Property(name="name", type=StringType)
statesml_Function.attributes={statesml_Function_name}

# statesml_Attribute class attributes and methods
statesml_Attribute_name: Property = Property(name="name", type=StringType)
statesml_Attribute.attributes={statesml_Attribute_name}

# statesml_Parameter class attributes and methods
statesml_Parameter_name: Property = Property(name="name", type=StringType)
statesml_Parameter.attributes={statesml_Parameter_name}

# statesml_DataType class attributes and methods
statesml_DataType_name: Property = Property(name="name", type=StringType)
statesml_DataType.attributes={statesml_DataType_name}

# statesml_SystemUnitLibrariy class attributes and methods
statesml_SystemUnitLibrariy_name: Property = Property(name="name", type=StringType)
statesml_SystemUnitLibrariy.attributes={statesml_SystemUnitLibrariy_name}

# statesml_DataTypeLibrary class attributes and methods
statesml_DataTypeLibrary_name: Property = Property(name="name", type=StringType)
statesml_DataTypeLibrary.attributes={statesml_DataTypeLibrary_name}

# statesml_State class attributes and methods
statesml_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
statesml_State_isTerminal: Property = Property(name="isTerminal", type=BooleanType)
statesml_State.attributes={statesml_State_isTerminal, statesml_State_isInitial}

# Node class attributes and methods

# statesml_Transition class attributes and methods

# statesml_SelectionDivergence class attributes and methods

# statesml_SelectionConvergence class attributes and methods

# statesml_StatesML class attributes and methods

# statesml_Event class attributes and methods
statesml_Event_name: Property = Property(name="name", type=StringType)
statesml_Event.attributes={statesml_Event_name}

# statesml_ChangeEvent class attributes and methods
statesml_ChangeEvent_isFulfilled: Property = Property(name="isFulfilled", type=BooleanType)
statesml_ChangeEvent.attributes={statesml_ChangeEvent_isFulfilled}

# statesml_Node class attributes and methods
statesml_Node_name: Property = Property(name="name", type=StringType)
statesml_Node.attributes={statesml_Node_name}

# statesml_Edge class attributes and methods
statesml_Edge_name: Property = Property(name="name", type=StringType)
statesml_Edge.attributes={statesml_Edge_name}

# Event class attributes and methods

# statesml_Trigger class attributes and methods
statesml_Trigger_m_fire: Method = Method(name="fire", parameters={})
statesml_Trigger_m_isActivated: Method = Method(name="isActivated", parameters={}, type=BooleanType)
statesml_Trigger.methods={statesml_Trigger_m_fire, statesml_Trigger_m_isActivated}

# Relationships
function0: BinaryAssociation = BinaryAssociation(
    name="function0",
    ends={
        Property(name="statesml_Function", type=statesml_SystemUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnits", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="statesml_Attribute", type=statesml_SystemUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnits2", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inParameter3: BinaryAssociation = BinaryAssociation(
    name="inParameter3",
    ends={
        Property(name="statesml_Parameter", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function4", type=statesml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnParameter5: BinaryAssociation = BinaryAssociation(
    name="returnParameter5",
    ends={
        Property(name="statesml_Parameter7", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function6", type=statesml_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datatype8: BinaryAssociation = BinaryAssociation(
    name="datatype8",
    ends={
        Property(name="statesml_DataType", type=statesml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Attribute9", type=statesml_DataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
datatype10: BinaryAssociation = BinaryAssociation(
    name="datatype10",
    ends={
        Property(name="statesml_DataType12", type=statesml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Parameter11", type=statesml_DataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function13: BinaryAssociation = BinaryAssociation(
    name="function13",
    ends={
        Property(name="statesml_Function15", type=statesml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataType14", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunits16: BinaryAssociation = BinaryAssociation(
    name="systemunits16",
    ends={
        Property(name="statesml_SystemUnits17", type=statesml_SystemUnitLibrariy, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnitLibrariy", type=statesml_SystemUnits, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype18: BinaryAssociation = BinaryAssociation(
    name="datatype18",
    ends={
        Property(name="statesml_DataType19", type=statesml_DataTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataTypeLibrary", type=statesml_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition20: BinaryAssociation = BinaryAssociation(
    name="transition20",
    ends={
        Property(name="Transition", type=statesml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=statesml_Transition, multiplicity=Multiplicity(0, 1))
    }
)
selectiondivergence21: BinaryAssociation = BinaryAssociation(
    name="selectiondivergence21",
    ends={
        Property(name="statesml_SelectionDivergence", type=statesml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_State", type=statesml_SelectionDivergence, multiplicity=Multiplicity(0, 1))
    }
)
trigger22: BinaryAssociation = BinaryAssociation(
    name="trigger22",
    ends={
        Property(name="statesml_Transition", type=statesml_ChangeEvent, multiplicity=Multiplicity(0, 1)),
        Property(name="statesml_ChangeEvent", type=statesml_Transition, multiplicity=Multiplicity(1, 1))
    }
)
state23: BinaryAssociation = BinaryAssociation(
    name="state23",
    ends={
        Property(name="State", type=statesml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=statesml_State, multiplicity=Multiplicity(0, 1))
    }
)
selectionconvergence24: BinaryAssociation = BinaryAssociation(
    name="selectionconvergence24",
    ends={
        Property(name="statesml_SelectionConvergence", type=statesml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Transition25", type=statesml_SelectionConvergence, multiplicity=Multiplicity(0, 1))
    }
)
transition26: BinaryAssociation = BinaryAssociation(
    name="transition26",
    ends={
        Property(name="statesml_Transition28", type=statesml_SelectionDivergence, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SelectionDivergence27", type=statesml_Transition, multiplicity=Multiplicity(2, 9999))
    }
)
state29: BinaryAssociation = BinaryAssociation(
    name="state29",
    ends={
        Property(name="statesml_State31", type=statesml_SelectionConvergence, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SelectionConvergence30", type=statesml_State, multiplicity=Multiplicity(1, 1))
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="statesml_Event", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML", type=statesml_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypelibrary36: BinaryAssociation = BinaryAssociation(
    name="datatypelibrary36",
    ends={
        Property(name="statesml_DataTypeLibrary38", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML37", type=statesml_DataTypeLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunitlibrariy39: BinaryAssociation = BinaryAssociation(
    name="systemunitlibrariy39",
    ends={
        Property(name="statesml_SystemUnitLibrariy41", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML40", type=statesml_SystemUnitLibrariy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node42: BinaryAssociation = BinaryAssociation(
    name="node42",
    ends={
        Property(name="statesml_Node", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML43", type=statesml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge44: BinaryAssociation = BinaryAssociation(
    name="edge44",
    ends={
        Property(name="statesml_Edge", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML45", type=statesml_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute46: BinaryAssociation = BinaryAssociation(
    name="attribute46",
    ends={
        Property(name="statesml_Attribute48", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML47", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node49: BinaryAssociation = BinaryAssociation(
    name="node49",
    ends={
        Property(name="Node", type=statesml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=statesml_Node, multiplicity=Multiplicity(2, 2))
    }
)
edge50: BinaryAssociation = BinaryAssociation(
    name="edge50",
    ends={
        Property(name="Edge", type=statesml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=statesml_Edge, multiplicity=Multiplicity(1, 9999))
    }
)
systemunits33: BinaryAssociation = BinaryAssociation(
    name="systemunits33",
    ends={
        Property(name="statesml_SystemUnits35", type=statesml_StatesML, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesML34", type=statesml_SystemUnits, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function51: BinaryAssociation = BinaryAssociation(
    name="function51",
    ends={
        Property(name="statesml_Function53", type=statesml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Node52", type=statesml_Function, multiplicity=Multiplicity(0, 9999))
    }
)
changeevent54: BinaryAssociation = BinaryAssociation(
    name="changeevent54",
    ends={
        Property(name="statesml_ChangeEvent55", type=statesml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Trigger", type=statesml_ChangeEvent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_statesml_State_Node = Generalization(general=Node, specific=statesml_State)
gen_statesml_Transition_Node = Generalization(general=Node, specific=statesml_Transition)
gen_statesml_SelectionDivergence_Node = Generalization(general=Node, specific=statesml_SelectionDivergence)
gen_statesml_SelectionConvergence_Node = Generalization(general=Node, specific=statesml_SelectionConvergence)
gen_statesml_ChangeEvent_Event = Generalization(general=Event, specific=statesml_ChangeEvent)

# Domain Model
domain_model = DomainModel(
    name="statesml",
    types={statesml_SystemUnits, statesml_Function, statesml_Attribute, statesml_Parameter, statesml_DataType, statesml_SystemUnitLibrariy, statesml_DataTypeLibrary, statesml_State, Node, statesml_Transition, statesml_SelectionDivergence, statesml_SelectionConvergence, statesml_StatesML, statesml_Event, statesml_ChangeEvent, statesml_Node, statesml_Edge, Event, statesml_Trigger},
    associations={function0, attribute1, inParameter3, returnParameter5, datatype8, datatype10, function13, systemunits16, datatype18, transition20, selectiondivergence21, trigger22, state23, selectionconvergence24, transition26, state29, event32, datatypelibrary36, systemunitlibrariy39, node42, edge44, attribute46, node49, edge50, systemunits33, function51, changeevent54},
    generalizations={gen_statesml_State_Node, gen_statesml_Transition_Node, gen_statesml_SelectionDivergence_Node, gen_statesml_SelectionConvergence_Node, gen_statesml_ChangeEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)