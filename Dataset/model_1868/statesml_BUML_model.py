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
statesml_StatesModel = Class(name="statesml::StatesModel")
statesml_SystemUnitModel = Class(name="statesml::SystemUnitModel")
statesml_DataTypeLibrary = Class(name="statesml::DataTypeLibrary")
statesml_SystemUnitLibrary = Class(name="statesml::SystemUnitLibrary")
statesml_Attribute = Class(name="statesml::Attribute")
statesml_DataType = Class(name="statesml::DataType", is_abstract=True)
statesml_StateSystemModel = Class(name="statesml::StateSystemModel")
statesml_Function = Class(name="statesml::Function")
statesml_SystemUnit = Class(name="statesml::SystemUnit")
statesml_ReturnParameter = Class(name="statesml::ReturnParameter")
statesml_IncomingParameter = Class(name="statesml::IncomingParameter")
statesml_Parameter = Class(name="statesml::Parameter", is_abstract=True)
statesml_Node = Class(name="statesml::Node", is_abstract=True)
statesml_Edge = Class(name="statesml::Edge")
statesml_Event = Class(name="statesml::Event", is_abstract=True)
statesml_StateSystem = Class(name="statesml::StateSystem")
statesml_State = Class(name="statesml::State", is_abstract=True)
Node = Class(name="Node")
statesml_FunctionCall = Class(name="statesml::FunctionCall")
statesml_Transition = Class(name="statesml::Transition")
statesml_Trigger = Class(name="statesml::Trigger")
statesml_SelectionDivergence = Class(name="statesml::SelectionDivergence")
statesml_SelectionConvergence = Class(name="statesml::SelectionConvergence")
statesml_ParameterValue = Class(name="statesml::ParameterValue")
statesml_String = Class(name="statesml::String")
DataType = Class(name="DataType")
statesml_Integer = Class(name="statesml::Integer")
statesml_Boolean = Class(name="statesml::Boolean")
statesml_InitialState = Class(name="statesml::InitialState")
State = Class(name="State")
Parameter_ = Class(name="Parameter")
statesml_ChangeEvent = Class(name="statesml::ChangeEvent")
Event = Class(name="Event")
statesml_ChangeExpression = Class(name="statesml::ChangeExpression")
statesml_TerminalState = Class(name="statesml::TerminalState")
statesml_MiddleState = Class(name="statesml::MiddleState")

# statesml_StatesModel class attributes and methods

# statesml_SystemUnitModel class attributes and methods
statesml_SystemUnitModel_name: Property = Property(name="name", type=StringType)
statesml_SystemUnitModel.attributes={statesml_SystemUnitModel_name}

# statesml_DataTypeLibrary class attributes and methods
statesml_DataTypeLibrary_name: Property = Property(name="name", type=StringType)
statesml_DataTypeLibrary.attributes={statesml_DataTypeLibrary_name}

# statesml_SystemUnitLibrary class attributes and methods
statesml_SystemUnitLibrary_name: Property = Property(name="name", type=StringType)
statesml_SystemUnitLibrary.attributes={statesml_SystemUnitLibrary_name}

# statesml_Attribute class attributes and methods
statesml_Attribute_name: Property = Property(name="name", type=StringType)
statesml_Attribute.attributes={statesml_Attribute_name}

# statesml_DataType class attributes and methods
statesml_DataType_name: Property = Property(name="name", type=StringType)
statesml_DataType.attributes={statesml_DataType_name}

# statesml_StateSystemModel class attributes and methods
statesml_StateSystemModel_name: Property = Property(name="name", type=StringType)
statesml_StateSystemModel.attributes={statesml_StateSystemModel_name}

# statesml_Function class attributes and methods
statesml_Function_name: Property = Property(name="name", type=StringType)
statesml_Function.attributes={statesml_Function_name}

# statesml_SystemUnit class attributes and methods
statesml_SystemUnit_name: Property = Property(name="name", type=StringType)
statesml_SystemUnit.attributes={statesml_SystemUnit_name}

# statesml_ReturnParameter class attributes and methods

# statesml_IncomingParameter class attributes and methods

# statesml_Parameter class attributes and methods
statesml_Parameter_name: Property = Property(name="name", type=StringType)
statesml_Parameter.attributes={statesml_Parameter_name}

# statesml_Node class attributes and methods
statesml_Node_name: Property = Property(name="name", type=StringType)
statesml_Node.attributes={statesml_Node_name}

# statesml_Edge class attributes and methods
statesml_Edge_name: Property = Property(name="name", type=StringType)
statesml_Edge.attributes={statesml_Edge_name}

# statesml_Event class attributes and methods
statesml_Event_name: Property = Property(name="name", type=StringType)
statesml_Event.attributes={statesml_Event_name}

# statesml_StateSystem class attributes and methods

# statesml_State class attributes and methods

# Node class attributes and methods

# statesml_FunctionCall class attributes and methods

# statesml_Transition class attributes and methods

# statesml_Trigger class attributes and methods

# statesml_SelectionDivergence class attributes and methods

# statesml_SelectionConvergence class attributes and methods

# statesml_ParameterValue class attributes and methods

# statesml_String class attributes and methods

# DataType class attributes and methods

# statesml_Integer class attributes and methods

# statesml_Boolean class attributes and methods

# statesml_InitialState class attributes and methods

# State class attributes and methods

# Parameter class attributes and methods

# statesml_ChangeEvent class attributes and methods

# Event class attributes and methods

# statesml_ChangeExpression class attributes and methods
statesml_ChangeExpression_fulfilled: Property = Property(name="fulfilled", type=BooleanType)
statesml_ChangeExpression.attributes={statesml_ChangeExpression_fulfilled}

# statesml_TerminalState class attributes and methods

# statesml_MiddleState class attributes and methods

# Relationships
datatype1: BinaryAssociation = BinaryAssociation(
    name="datatype1",
    ends={
        Property(name="statesml_Attribute", type=statesml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataType", type=statesml_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
datatypelibrary2: BinaryAssociation = BinaryAssociation(
    name="datatypelibrary2",
    ends={
        Property(name="statesml_DataTypeLibrary", type=statesml_SystemUnitModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnitModel3", type=statesml_DataTypeLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunitlibrary4: BinaryAssociation = BinaryAssociation(
    name="systemunitlibrary4",
    ends={
        Property(name="statesml_SystemUnitLibrary", type=statesml_SystemUnitModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnitModel5", type=statesml_SystemUnitLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunits0: BinaryAssociation = BinaryAssociation(
    name="systemunits0",
    ends={
        Property(name="statesml_SystemUnitModel", type=statesml_StatesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StatesModel", type=statesml_SystemUnitModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemunit8: BinaryAssociation = BinaryAssociation(
    name="systemunit8",
    ends={
        Property(name="statesml_SystemUnit", type=statesml_SystemUnitLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnitLibrary9", type=statesml_SystemUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statesystemmodel10: BinaryAssociation = BinaryAssociation(
    name="statesystemmodel10",
    ends={
        Property(name="statesml_StateSystemModel", type=statesml_SystemUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnit11", type=statesml_StateSystemModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute12: BinaryAssociation = BinaryAssociation(
    name="attribute12",
    ends={
        Property(name="statesml_Attribute14", type=statesml_SystemUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnit13", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function6: BinaryAssociation = BinaryAssociation(
    name="function6",
    ends={
        Property(name="statesml_Function", type=statesml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataType7", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnparameter21: BinaryAssociation = BinaryAssociation(
    name="returnparameter21",
    ends={
        Property(name="statesml_ReturnParameter", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function22", type=statesml_ReturnParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingparameter23: BinaryAssociation = BinaryAssociation(
    name="incomingparameter23",
    ends={
        Property(name="statesml_IncomingParameter", type=statesml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Function24", type=statesml_IncomingParameter, multiplicity=Multiplicity(0, 9999))
    }
)
function15: BinaryAssociation = BinaryAssociation(
    name="function15",
    ends={
        Property(name="statesml_Function17", type=statesml_SystemUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_SystemUnit16", type=statesml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype25: BinaryAssociation = BinaryAssociation(
    name="datatype25",
    ends={
        Property(name="statesml_DataType26", type=statesml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Parameter", type=statesml_DataType, multiplicity=Multiplicity(1, 1))
    }
)
datatype18: BinaryAssociation = BinaryAssociation(
    name="datatype18",
    ends={
        Property(name="statesml_DataType20", type=statesml_DataTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_DataTypeLibrary19", type=statesml_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node29: BinaryAssociation = BinaryAssociation(
    name="node29",
    ends={
        Property(name="statesml_Node", type=statesml_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StateSystem30", type=statesml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge31: BinaryAssociation = BinaryAssociation(
    name="edge31",
    ends={
        Property(name="statesml_Edge", type=statesml_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StateSystem32", type=statesml_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute33: BinaryAssociation = BinaryAssociation(
    name="attribute33",
    ends={
        Property(name="statesml_Attribute35", type=statesml_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StateSystem34", type=statesml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event36: BinaryAssociation = BinaryAssociation(
    name="event36",
    ends={
        Property(name="statesml_Event", type=statesml_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StateSystem37", type=statesml_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing38: BinaryAssociation = BinaryAssociation(
    name="outgoing38",
    ends={
        Property(name="Edge", type=statesml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statesml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
statesystem27: BinaryAssociation = BinaryAssociation(
    name="statesystem27",
    ends={
        Property(name="statesml_StateSystem", type=statesml_StateSystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_StateSystemModel28", type=statesml_StateSystem, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functioncall44: BinaryAssociation = BinaryAssociation(
    name="functioncall44",
    ends={
        Property(name="statesml_FunctionCall", type=statesml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_State", type=statesml_FunctionCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger45: BinaryAssociation = BinaryAssociation(
    name="trigger45",
    ends={
        Property(name="statesml_Trigger", type=statesml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Transition", type=statesml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming39: BinaryAssociation = BinaryAssociation(
    name="incoming39",
    ends={
        Property(name="Edge40", type=statesml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statesml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="Node", type=statesml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statesml_Node, multiplicity=Multiplicity(1, 1))
    }
)
target42: BinaryAssociation = BinaryAssociation(
    name="target42",
    ends={
        Property(name="Node43", type=statesml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statesml_Node, multiplicity=Multiplicity(1, 1))
    }
)
attribute49: BinaryAssociation = BinaryAssociation(
    name="attribute49",
    ends={
        Property(name="statesml_Attribute51", type=statesml_IncomingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_IncomingParameter50", type=statesml_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
function52: BinaryAssociation = BinaryAssociation(
    name="function52",
    ends={
        Property(name="statesml_Function54", type=statesml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_FunctionCall53", type=statesml_Function, multiplicity=Multiplicity(1, 1))
    }
)
parametervalue55: BinaryAssociation = BinaryAssociation(
    name="parametervalue55",
    ends={
        Property(name="statesml_ParameterValue", type=statesml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_FunctionCall56", type=statesml_ParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event46: BinaryAssociation = BinaryAssociation(
    name="event46",
    ends={
        Property(name="statesml_Event48", type=statesml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_Trigger47", type=statesml_Event, multiplicity=Multiplicity(1, 1))
    }
)
changeexpression57: BinaryAssociation = BinaryAssociation(
    name="changeexpression57",
    ends={
        Property(name="statesml_ChangeExpression", type=statesml_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_ChangeEvent", type=statesml_ChangeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function58: BinaryAssociation = BinaryAssociation(
    name="function58",
    ends={
        Property(name="statesml_Function60", type=statesml_ChangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_ChangeExpression59", type=statesml_Function, multiplicity=Multiplicity(1, 1))
    }
)
incomingparameter61: BinaryAssociation = BinaryAssociation(
    name="incomingparameter61",
    ends={
        Property(name="statesml_IncomingParameter63", type=statesml_ChangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_ChangeExpression62", type=statesml_IncomingParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingparameter64: BinaryAssociation = BinaryAssociation(
    name="incomingparameter64",
    ends={
        Property(name="statesml_IncomingParameter66", type=statesml_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="statesml_ParameterValue65", type=statesml_IncomingParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statesml_State_Node = Generalization(general=Node, specific=statesml_State)
gen_statesml_Transition_Node = Generalization(general=Node, specific=statesml_Transition)
gen_statesml_SelectionDivergence_Node = Generalization(general=Node, specific=statesml_SelectionDivergence)
gen_statesml_String_DataType = Generalization(general=DataType, specific=statesml_String)
gen_statesml_Integer_DataType = Generalization(general=DataType, specific=statesml_Integer)
gen_statesml_Boolean_DataType = Generalization(general=DataType, specific=statesml_Boolean)
gen_statesml_InitialState_State = Generalization(general=State, specific=statesml_InitialState)
gen_statesml_SelectionConvergence_Node = Generalization(general=Node, specific=statesml_SelectionConvergence)
gen_statesml_ReturnParameter_Parameter = Generalization(general=Parameter_, specific=statesml_ReturnParameter)
gen_statesml_IncomingParameter_Parameter = Generalization(general=Parameter_, specific=statesml_IncomingParameter)
gen_statesml_ChangeEvent_Event = Generalization(general=Event, specific=statesml_ChangeEvent)
gen_statesml_TerminalState_State = Generalization(general=State, specific=statesml_TerminalState)
gen_statesml_MiddleState_State = Generalization(general=State, specific=statesml_MiddleState)

# Domain Model
domain_model = DomainModel(
    name="statesml",
    types={statesml_StatesModel, statesml_SystemUnitModel, statesml_DataTypeLibrary, statesml_SystemUnitLibrary, statesml_Attribute, statesml_DataType, statesml_StateSystemModel, statesml_Function, statesml_SystemUnit, statesml_ReturnParameter, statesml_IncomingParameter, statesml_Parameter, statesml_Node, statesml_Edge, statesml_Event, statesml_StateSystem, statesml_State, Node, statesml_FunctionCall, statesml_Transition, statesml_Trigger, statesml_SelectionDivergence, statesml_SelectionConvergence, statesml_ParameterValue, statesml_String, DataType, statesml_Integer, statesml_Boolean, statesml_InitialState, State, Parameter_, statesml_ChangeEvent, Event, statesml_ChangeExpression, statesml_TerminalState, statesml_MiddleState},
    associations={datatype1, datatypelibrary2, systemunitlibrary4, systemunits0, systemunit8, statesystemmodel10, attribute12, function6, returnparameter21, incomingparameter23, function15, datatype25, datatype18, node29, edge31, attribute33, event36, outgoing38, statesystem27, functioncall44, trigger45, incoming39, source41, target42, attribute49, function52, parametervalue55, event46, changeexpression57, function58, incomingparameter61, incomingparameter64},
    generalizations={gen_statesml_State_Node, gen_statesml_Transition_Node, gen_statesml_SelectionDivergence_Node, gen_statesml_String_DataType, gen_statesml_Integer_DataType, gen_statesml_Boolean_DataType, gen_statesml_InitialState_State, gen_statesml_SelectionConvergence_Node, gen_statesml_ReturnParameter_Parameter, gen_statesml_IncomingParameter_Parameter, gen_statesml_ChangeEvent_Event, gen_statesml_TerminalState_State, gen_statesml_MiddleState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)