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
reqLanguage_ReqID = Class(name="reqLanguage::ReqID")
reqLanguage_Prefix = Class(name="reqLanguage::Prefix")
reqLanguage_EObject = Class(name="reqLanguage::EObject")
reqLanguage_Model = Class(name="reqLanguage::Model")
reqLanguage_Requirement = Class(name="reqLanguage::Requirement")
reqLanguage_Operator = Class(name="reqLanguage::Operator")
reqLanguage_Value = Class(name="reqLanguage::Value")
reqLanguage_TimingConstraint = Class(name="reqLanguage::TimingConstraint")
reqLanguage_PrefixEvent = Class(name="reqLanguage::PrefixEvent")
reqLanguage_ParamEvent = Class(name="reqLanguage::ParamEvent")
reqLanguage_PrefixRightOperand = Class(name="reqLanguage::PrefixRightOperand")
reqLanguage_PrefixState = Class(name="reqLanguage::PrefixState")
reqLanguage_PrefixCondition = Class(name="reqLanguage::PrefixCondition")
reqLanguage_StateEvent = Class(name="reqLanguage::StateEvent")
reqLanguage_System = Class(name="reqLanguage::System")
reqLanguage_State = Class(name="reqLanguage::State")
reqLanguage_ParameterState = Class(name="reqLanguage::ParameterState")
reqLanguage_MainFunction = Class(name="reqLanguage::MainFunction")
reqLanguage_ActorEvent = Class(name="reqLanguage::ActorEvent")
reqLanguage_Parameter = Class(name="reqLanguage::Parameter")
reqLanguage_Action = Class(name="reqLanguage::Action")
reqLanguage_MainComposition = Class(name="reqLanguage::MainComposition")
reqLanguage_MainAttributes = Class(name="reqLanguage::MainAttributes")
reqLanguage_Attribute = Class(name="reqLanguage::Attribute")
reqLanguage_MainStateTransition = Class(name="reqLanguage::MainStateTransition")
reqLanguage_MainFunctions = Class(name="reqLanguage::MainFunctions")
reqLanguage_Function = Class(name="reqLanguage::Function")
reqLanguage_Transition = Class(name="reqLanguage::Transition")
reqLanguage_OutTransition = Class(name="reqLanguage::OutTransition")
reqLanguage_NoTransition = Class(name="reqLanguage::NoTransition")
reqLanguage_Actor = Class(name="reqLanguage::Actor")
reqLanguage_User = Class(name="reqLanguage::User")
reqLanguage_Time = Class(name="reqLanguage::Time")

# reqLanguage_ReqID class attributes and methods
reqLanguage_ReqID_reqID: Property = Property(name="reqID", type=StringType)
reqLanguage_ReqID_name: Property = Property(name="name", type=StringType)
reqLanguage_ReqID.attributes={reqLanguage_ReqID_reqID, reqLanguage_ReqID_name}

# reqLanguage_Prefix class attributes and methods

# reqLanguage_EObject class attributes and methods

# reqLanguage_Model class attributes and methods

# reqLanguage_Requirement class attributes and methods

# reqLanguage_Operator class attributes and methods
reqLanguage_Operator_operator: Property = Property(name="operator", type=StringType)
reqLanguage_Operator.attributes={reqLanguage_Operator_operator}

# reqLanguage_Value class attributes and methods
reqLanguage_Value_val: Property = Property(name="val", type=StringType)
reqLanguage_Value_value: Property = Property(name="value", type=IntegerType)
reqLanguage_Value.attributes={reqLanguage_Value_val, reqLanguage_Value_value}

# reqLanguage_TimingConstraint class attributes and methods
reqLanguage_TimingConstraint_timingConstraint: Property = Property(name="timingConstraint", type=StringType)
reqLanguage_TimingConstraint_minmax: Property = Property(name="minmax", type=StringType)
reqLanguage_TimingConstraint.attributes={reqLanguage_TimingConstraint_minmax, reqLanguage_TimingConstraint_timingConstraint}

# reqLanguage_PrefixEvent class attributes and methods
reqLanguage_PrefixEvent_prefixFixedSyntax: Property = Property(name="prefixFixedSyntax", type=StringType)
reqLanguage_PrefixEvent.attributes={reqLanguage_PrefixEvent_prefixFixedSyntax}

# reqLanguage_ParamEvent class attributes and methods
reqLanguage_ParamEvent_action: Property = Property(name="action", type=StringType)
reqLanguage_ParamEvent.attributes={reqLanguage_ParamEvent_action}

# reqLanguage_PrefixRightOperand class attributes and methods
reqLanguage_PrefixRightOperand_operator: Property = Property(name="operator", type=StringType)
reqLanguage_PrefixRightOperand.attributes={reqLanguage_PrefixRightOperand_operator}

# reqLanguage_PrefixState class attributes and methods
reqLanguage_PrefixState_prefixFixedSyntax: Property = Property(name="prefixFixedSyntax", type=StringType)
reqLanguage_PrefixState.attributes={reqLanguage_PrefixState_prefixFixedSyntax}

# reqLanguage_PrefixCondition class attributes and methods
reqLanguage_PrefixCondition_prefixFixedSyntax: Property = Property(name="prefixFixedSyntax", type=StringType)
reqLanguage_PrefixCondition.attributes={reqLanguage_PrefixCondition_prefixFixedSyntax}

# reqLanguage_StateEvent class attributes and methods

# reqLanguage_System class attributes and methods
reqLanguage_System_system: Property = Property(name="system", type=StringType)
reqLanguage_System_name: Property = Property(name="name", type=StringType)
reqLanguage_System.attributes={reqLanguage_System_system, reqLanguage_System_name}

# reqLanguage_State class attributes and methods
reqLanguage_State_state: Property = Property(name="state", type=StringType)
reqLanguage_State_name: Property = Property(name="name", type=StringType)
reqLanguage_State.attributes={reqLanguage_State_name, reqLanguage_State_state}

# reqLanguage_ParameterState class attributes and methods

# reqLanguage_MainFunction class attributes and methods

# reqLanguage_ActorEvent class attributes and methods
reqLanguage_ActorEvent_action: Property = Property(name="action", type=StringType)
reqLanguage_ActorEvent.attributes={reqLanguage_ActorEvent_action}

# reqLanguage_Parameter class attributes and methods
reqLanguage_Parameter_parameter: Property = Property(name="parameter", type=StringType)
reqLanguage_Parameter_name: Property = Property(name="name", type=StringType)
reqLanguage_Parameter.attributes={reqLanguage_Parameter_parameter, reqLanguage_Parameter_name}

# reqLanguage_Action class attributes and methods
reqLanguage_Action_action: Property = Property(name="action", type=StringType)
reqLanguage_Action_name: Property = Property(name="name", type=StringType)
reqLanguage_Action.attributes={reqLanguage_Action_action, reqLanguage_Action_name}

# reqLanguage_MainComposition class attributes and methods

# reqLanguage_MainAttributes class attributes and methods

# reqLanguage_Attribute class attributes and methods
reqLanguage_Attribute_attribute: Property = Property(name="attribute", type=StringType)
reqLanguage_Attribute_name: Property = Property(name="name", type=StringType)
reqLanguage_Attribute_type: Property = Property(name="type", type=StringType)
reqLanguage_Attribute.attributes={reqLanguage_Attribute_name, reqLanguage_Attribute_attribute, reqLanguage_Attribute_type}

# reqLanguage_MainStateTransition class attributes and methods

# reqLanguage_MainFunctions class attributes and methods

# reqLanguage_Function class attributes and methods
reqLanguage_Function_name: Property = Property(name="name", type=StringType)
reqLanguage_Function_type: Property = Property(name="type", type=StringType)
reqLanguage_Function_function: Property = Property(name="function", type=StringType)
reqLanguage_Function.attributes={reqLanguage_Function_type, reqLanguage_Function_name, reqLanguage_Function_function}

# reqLanguage_Transition class attributes and methods

# reqLanguage_OutTransition class attributes and methods

# reqLanguage_NoTransition class attributes and methods

# reqLanguage_Actor class attributes and methods
reqLanguage_Actor_actor: Property = Property(name="actor", type=StringType)
reqLanguage_Actor_name: Property = Property(name="name", type=StringType)
reqLanguage_Actor.attributes={reqLanguage_Actor_actor, reqLanguage_Actor_name}

# reqLanguage_User class attributes and methods
reqLanguage_User_user: Property = Property(name="user", type=StringType)
reqLanguage_User_name: Property = Property(name="name", type=StringType)
reqLanguage_User.attributes={reqLanguage_User_user, reqLanguage_User_name}

# reqLanguage_Time class attributes and methods
reqLanguage_Time_value: Property = Property(name="value", type=IntegerType)
reqLanguage_Time_timeUnit: Property = Property(name="timeUnit", type=StringType)
reqLanguage_Time.attributes={reqLanguage_Time_timeUnit, reqLanguage_Time_value}

# Relationships
reqID1: BinaryAssociation = BinaryAssociation(
    name="reqID1",
    ends={
        Property(name="reqLanguage_ReqID", type=reqLanguage_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Requirement2", type=reqLanguage_ReqID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prefix3: BinaryAssociation = BinaryAssociation(
    name="prefix3",
    ends={
        Property(name="reqLanguage_Prefix", type=reqLanguage_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Requirement4", type=reqLanguage_Prefix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainRequirement5: BinaryAssociation = BinaryAssociation(
    name="mainRequirement5",
    ends={
        Property(name="reqLanguage_EObject", type=reqLanguage_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Requirement6", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand7: BinaryAssociation = BinaryAssociation(
    name="leftOperand7",
    ends={
        Property(name="reqLanguage_EObject9", type=reqLanguage_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Prefix8", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requirements0: BinaryAssociation = BinaryAssociation(
    name="requirements0",
    ends={
        Property(name="reqLanguage_Requirement", type=reqLanguage_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Model", type=reqLanguage_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter17: BinaryAssociation = BinaryAssociation(
    name="parameter17",
    ends={
        Property(name="reqLanguage_EObject18", type=reqLanguage_PrefixCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixCondition", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator19: BinaryAssociation = BinaryAssociation(
    name="operator19",
    ends={
        Property(name="reqLanguage_Operator", type=reqLanguage_PrefixCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixCondition20", type=reqLanguage_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="reqLanguage_Value", type=reqLanguage_PrefixCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixCondition22", type=reqLanguage_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time23: BinaryAssociation = BinaryAssociation(
    name="time23",
    ends={
        Property(name="reqLanguage_TimingConstraint", type=reqLanguage_PrefixCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixCondition24", type=reqLanguage_TimingConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event_expression25: BinaryAssociation = BinaryAssociation(
    name="event_expression25",
    ends={
        Property(name="reqLanguage_EObject26", type=reqLanguage_PrefixEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixEvent", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prefixList10: BinaryAssociation = BinaryAssociation(
    name="prefixList10",
    ends={
        Property(name="reqLanguage_PrefixRightOperand", type=reqLanguage_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Prefix11", type=reqLanguage_PrefixRightOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prefixRightOperand12: BinaryAssociation = BinaryAssociation(
    name="prefixRightOperand12",
    ends={
        Property(name="reqLanguage_EObject14", type=reqLanguage_PrefixRightOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixRightOperand13", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateExpression15: BinaryAssociation = BinaryAssociation(
    name="stateExpression15",
    ends={
        Property(name="reqLanguage_EObject16", type=reqLanguage_PrefixState, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_PrefixState", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system36: BinaryAssociation = BinaryAssociation(
    name="system36",
    ends={
        Property(name="reqLanguage_System", type=reqLanguage_StateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_StateEvent", type=reqLanguage_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state37: BinaryAssociation = BinaryAssociation(
    name="state37",
    ends={
        Property(name="reqLanguage_State", type=reqLanguage_StateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_StateEvent38", type=reqLanguage_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter39: BinaryAssociation = BinaryAssociation(
    name="parameter39",
    ends={
        Property(name="reqLanguage_Parameter40", type=reqLanguage_ParameterState, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ParameterState", type=reqLanguage_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_value41: BinaryAssociation = BinaryAssociation(
    name="parameter_value41",
    ends={
        Property(name="reqLanguage_EObject43", type=reqLanguage_ParameterState, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ParameterState42", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system44: BinaryAssociation = BinaryAssociation(
    name="system44",
    ends={
        Property(name="reqLanguage_EObject45", type=reqLanguage_MainFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainFunction", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter27: BinaryAssociation = BinaryAssociation(
    name="parameter27",
    ends={
        Property(name="reqLanguage_EObject28", type=reqLanguage_ParamEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ParamEvent", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="reqLanguage_Value31", type=reqLanguage_ParamEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ParamEvent30", type=reqLanguage_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actor32: BinaryAssociation = BinaryAssociation(
    name="actor32",
    ends={
        Property(name="reqLanguage_EObject33", type=reqLanguage_ActorEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ActorEvent", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity34: BinaryAssociation = BinaryAssociation(
    name="entity34",
    ends={
        Property(name="reqLanguage_Parameter", type=reqLanguage_ActorEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_ActorEvent35", type=reqLanguage_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function58: BinaryAssociation = BinaryAssociation(
    name="function58",
    ends={
        Property(name="reqLanguage_Action60", type=reqLanguage_MainStateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainStateTransition59", type=reqLanguage_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function46: BinaryAssociation = BinaryAssociation(
    name="function46",
    ends={
        Property(name="reqLanguage_Action", type=reqLanguage_MainFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainFunction47", type=reqLanguage_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system48: BinaryAssociation = BinaryAssociation(
    name="system48",
    ends={
        Property(name="reqLanguage_System49", type=reqLanguage_MainComposition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainComposition", type=reqLanguage_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system61: BinaryAssociation = BinaryAssociation(
    name="system61",
    ends={
        Property(name="reqLanguage_System62", type=reqLanguage_MainAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainAttributes", type=reqLanguage_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subsystemList50: BinaryAssociation = BinaryAssociation(
    name="subsystemList50",
    ends={
        Property(name="reqLanguage_System52", type=reqLanguage_MainComposition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainComposition51", type=reqLanguage_System, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeList63: BinaryAssociation = BinaryAssociation(
    name="attributeList63",
    ends={
        Property(name="reqLanguage_Attribute", type=reqLanguage_MainAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainAttributes64", type=reqLanguage_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system53: BinaryAssociation = BinaryAssociation(
    name="system53",
    ends={
        Property(name="reqLanguage_System54", type=reqLanguage_MainStateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainStateTransition", type=reqLanguage_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system65: BinaryAssociation = BinaryAssociation(
    name="system65",
    ends={
        Property(name="reqLanguage_System66", type=reqLanguage_MainFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainFunctions", type=reqLanguage_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition55: BinaryAssociation = BinaryAssociation(
    name="transition55",
    ends={
        Property(name="reqLanguage_EObject57", type=reqLanguage_MainStateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainStateTransition56", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionList67: BinaryAssociation = BinaryAssociation(
    name="functionList67",
    ends={
        Property(name="reqLanguage_Function", type=reqLanguage_MainFunctions, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_MainFunctions68", type=reqLanguage_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source_state69: BinaryAssociation = BinaryAssociation(
    name="source_state69",
    ends={
        Property(name="reqLanguage_EObject70", type=reqLanguage_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Transition", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target_state71: BinaryAssociation = BinaryAssociation(
    name="target_state71",
    ends={
        Property(name="reqLanguage_EObject73", type=reqLanguage_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Transition72", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source_state74: BinaryAssociation = BinaryAssociation(
    name="source_state74",
    ends={
        Property(name="reqLanguage_EObject75", type=reqLanguage_OutTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_OutTransition", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state76: BinaryAssociation = BinaryAssociation(
    name="state76",
    ends={
        Property(name="reqLanguage_EObject77", type=reqLanguage_NoTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_NoTransition", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter78: BinaryAssociation = BinaryAssociation(
    name="parameter78",
    ends={
        Property(name="reqLanguage_Parameter80", type=reqLanguage_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Action79", type=reqLanguage_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="reqLanguage_Value83", type=reqLanguage_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Action82", type=reqLanguage_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subject84: BinaryAssociation = BinaryAssociation(
    name="subject84",
    ends={
        Property(name="reqLanguage_EObject86", type=reqLanguage_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_Action85", type=reqLanguage_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time87: BinaryAssociation = BinaryAssociation(
    name="time87",
    ends={
        Property(name="reqLanguage_Time", type=reqLanguage_TimingConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="reqLanguage_TimingConstraint88", type=reqLanguage_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="reqLanguage",
    types={reqLanguage_ReqID, reqLanguage_Prefix, reqLanguage_EObject, reqLanguage_Model, reqLanguage_Requirement, reqLanguage_Operator, reqLanguage_Value, reqLanguage_TimingConstraint, reqLanguage_PrefixEvent, reqLanguage_ParamEvent, reqLanguage_PrefixRightOperand, reqLanguage_PrefixState, reqLanguage_PrefixCondition, reqLanguage_StateEvent, reqLanguage_System, reqLanguage_State, reqLanguage_ParameterState, reqLanguage_MainFunction, reqLanguage_ActorEvent, reqLanguage_Parameter, reqLanguage_Action, reqLanguage_MainComposition, reqLanguage_MainAttributes, reqLanguage_Attribute, reqLanguage_MainStateTransition, reqLanguage_MainFunctions, reqLanguage_Function, reqLanguage_Transition, reqLanguage_OutTransition, reqLanguage_NoTransition, reqLanguage_Actor, reqLanguage_User, reqLanguage_Time},
    associations={reqID1, prefix3, mainRequirement5, leftOperand7, requirements0, parameter17, operator19, value21, time23, event_expression25, prefixList10, prefixRightOperand12, stateExpression15, system36, state37, parameter39, parameter_value41, system44, parameter27, value29, actor32, entity34, function58, function46, system48, system61, subsystemList50, attributeList63, system53, system65, transition55, functionList67, source_state69, target_state71, source_state74, state76, parameter78, value81, subject84, time87},
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