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
CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="cck_sequential"),
			EnumerationLiteral(name="cck_guarded"),
			EnumerationLiteral(name="cck_concurrent")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="pdk_in"),
			EnumerationLiteral(name="pdk_inout"),
			EnumerationLiteral(name="pdk_out"),
			EnumerationLiteral(name="pdk_return")
    }
)

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="sk_instance"),
			EnumerationLiteral(name="sk_classifier")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="pk_choice"),
			EnumerationLiteral(name="pk_deepHistory"),
			EnumerationLiteral(name="pk_fork"),
			EnumerationLiteral(name="pk_initial"),
			EnumerationLiteral(name="pk_join"),
			EnumerationLiteral(name="pk_junction"),
			EnumerationLiteral(name="pk_shallowHistory")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="vk_public"),
			EnumerationLiteral(name="vk_protected"),
			EnumerationLiteral(name="vk_private"),
			EnumerationLiteral(name="vk_package")
    }
)

# Classes
Common_Behavior_Signal = Class(name="Common_Behavior_Signal")
Classifier = Class(name="Classifier")
Common_Behavior_Action = Class(name="Common_Behavior_Action", is_abstract=True)
ModelElement = Class(name="ModelElement")
Argument = Class(name="Argument")
ActionSequence = Class(name="ActionSequence")
IterationExpression = Class(name="IterationExpression")
ObjectSetExpression = Class(name="ObjectSetExpression")
Signal = Class(name="Signal")
Common_Behavior_ActionSequence = Class(name="Common_Behavior_ActionSequence")
Common_Behavior_Argument = Class(name="Common_Behavior_Argument")
Expression = Class(name="Expression")
Common_Behavior_Reception = Class(name="Common_Behavior_Reception")
BehavioralFeature = Class(name="BehavioralFeature")
Common_Behavior_ReturnAction = Class(name="Common_Behavior_ReturnAction")
Common_Behavior_TerminateAction = Class(name="Common_Behavior_TerminateAction")
Common_Behavior_Exception = Class(name="Common_Behavior_Exception")
ActionExpression = Class(name="ActionExpression")
Common_Behavior_CreateAction = Class(name="Common_Behavior_CreateAction")
Action = Class(name="Action")
Common_Behavior_DestroyAction = Class(name="Common_Behavior_DestroyAction")
Common_Behavior_UninterpretedAction = Class(name="Common_Behavior_UninterpretedAction")
Common_Behavior_CallAction = Class(name="Common_Behavior_CallAction")
Operation = Class(name="Operation")
Common_Behavior_SendAction = Class(name="Common_Behavior_SendAction")
Data_Types_BooleanExpression = Class(name="Data_Types_BooleanExpression")
Data_Types_ObjectSetExpression = Class(name="Data_Types_ObjectSetExpression")
Data_Types_ActionExpression = Class(name="Data_Types_ActionExpression")
Data_Types_IterationExpression = Class(name="Data_Types_IterationExpression")
Data_Types_TimeExpression = Class(name="Data_Types_TimeExpression")
State_Machines_StateMachine = Class(name="State_Machines_StateMachine")
SubmachineState = Class(name="SubmachineState")
State = Class(name="State")
Transition = Class(name="Transition")
State_Machines_Event = Class(name="State_Machines_Event", is_abstract=True)
Parameter_ = Class(name="Parameter")
State_Machines_StateVertex = Class(name="State_Machines_StateVertex", is_abstract=True)
CompositeState = Class(name="CompositeState")
Data_Types_Expression = Class(name="Data_Types_Expression")
StateMachine = Class(name="StateMachine")
State_Machines_TimeEvent = Class(name="State_Machines_TimeEvent")
TimeExpression = Class(name="TimeExpression")
State_Machines_CallEvent = Class(name="State_Machines_CallEvent")
State_Machines_SignalEvent = Class(name="State_Machines_SignalEvent")
State_Machines_Transition = Class(name="State_Machines_Transition")
State_Machines_State = Class(name="State_Machines_State", is_abstract=True)
StateVertex = Class(name="StateVertex")
Event = Class(name="Event")
State_Machines_Pseudostate = Class(name="State_Machines_Pseudostate")
State_Machines_SimpleState = Class(name="State_Machines_SimpleState")
State_Machines_SubmachineState = Class(name="State_Machines_SubmachineState")
State_Machines_SynchState = Class(name="State_Machines_SynchState")
State_Machines_StubState = Class(name="State_Machines_StubState")
State_Machines_FinalState = Class(name="State_Machines_FinalState")
Core_Element = Class(name="Core_Element", is_abstract=True)
Core_ModelElement = Class(name="Core_ModelElement", is_abstract=True)
Element = Class(name="Element")
Namespace = Class(name="Namespace")
Core_GeneralizableElement = Class(name="Core_GeneralizableElement", is_abstract=True)
Guard = Class(name="Guard")
Generalization_ = Class(name="Generalization_")
State_Machines_CompositeState = Class(name="State_Machines_CompositeState")
State_Machines_ChangeEvent = Class(name="State_Machines_ChangeEvent")
BooleanExpression = Class(name="BooleanExpression")
State_Machines_Guard = Class(name="State_Machines_Guard")
Core_Classifier = Class(name="Core_Classifier", is_abstract=True)
GeneralizableElement = Class(name="GeneralizableElement")
Feature = Class(name="Feature")
Core_Feature = Class(name="Core_Feature", is_abstract=True)
Core_Relationship = Class(name="Core_Relationship", is_abstract=True)
Core_BehavioralFeature = Class(name="Core_BehavioralFeature", is_abstract=True)
Core_Operation = Class(name="Core_Operation")
Core_Namespace = Class(name="Core_Namespace", is_abstract=True)
Core_Generalization = Class(name="Core_Generalization_")
Relationship = Class(name="Relationship")
Core_Parameter = Class(name="Core_Parameter")

# Common_Behavior_Signal class attributes and methods

# Classifier class attributes and methods

# Common_Behavior_Action class attributes and methods
Common_Behavior_Action_isAsynchronous: Property = Property(name="isAsynchronous", type=StringType)
Common_Behavior_Action.attributes={Common_Behavior_Action_isAsynchronous}

# ModelElement class attributes and methods

# Argument class attributes and methods

# ActionSequence class attributes and methods

# IterationExpression class attributes and methods

# ObjectSetExpression class attributes and methods

# Signal class attributes and methods

# Common_Behavior_ActionSequence class attributes and methods

# Common_Behavior_Argument class attributes and methods

# Expression class attributes and methods

# Common_Behavior_Reception class attributes and methods
Common_Behavior_Reception_specification: Property = Property(name="specification", type=StringType)
Common_Behavior_Reception_isRoot: Property = Property(name="isRoot", type=StringType)
Common_Behavior_Reception_isLeaf: Property = Property(name="isLeaf", type=StringType)
Common_Behavior_Reception_isAbstract: Property = Property(name="isAbstract", type=StringType)
Common_Behavior_Reception.attributes={Common_Behavior_Reception_isLeaf, Common_Behavior_Reception_specification, Common_Behavior_Reception_isAbstract, Common_Behavior_Reception_isRoot}

# BehavioralFeature class attributes and methods

# Common_Behavior_ReturnAction class attributes and methods

# Common_Behavior_TerminateAction class attributes and methods

# Common_Behavior_Exception class attributes and methods

# ActionExpression class attributes and methods

# Common_Behavior_CreateAction class attributes and methods

# Action class attributes and methods

# Common_Behavior_DestroyAction class attributes and methods

# Common_Behavior_UninterpretedAction class attributes and methods

# Common_Behavior_CallAction class attributes and methods

# Operation class attributes and methods

# Common_Behavior_SendAction class attributes and methods

# Data_Types_BooleanExpression class attributes and methods

# Data_Types_ObjectSetExpression class attributes and methods

# Data_Types_ActionExpression class attributes and methods

# Data_Types_IterationExpression class attributes and methods

# Data_Types_TimeExpression class attributes and methods

# State_Machines_StateMachine class attributes and methods

# SubmachineState class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# State_Machines_Event class attributes and methods

# Parameter class attributes and methods

# State_Machines_StateVertex class attributes and methods

# CompositeState class attributes and methods

# Data_Types_Expression class attributes and methods
Data_Types_Expression_language: Property = Property(name="language", type=StringType)
Data_Types_Expression_body: Property = Property(name="body", type=StringType)
Data_Types_Expression.attributes={Data_Types_Expression_language, Data_Types_Expression_body}

# StateMachine class attributes and methods

# State_Machines_TimeEvent class attributes and methods

# TimeExpression class attributes and methods

# State_Machines_CallEvent class attributes and methods

# State_Machines_SignalEvent class attributes and methods

# State_Machines_Transition class attributes and methods

# State_Machines_State class attributes and methods

# StateVertex class attributes and methods

# Event class attributes and methods

# State_Machines_Pseudostate class attributes and methods
State_Machines_Pseudostate_kind: Property = Property(name="kind", type=StringType)
State_Machines_Pseudostate.attributes={State_Machines_Pseudostate_kind}

# State_Machines_SimpleState class attributes and methods

# State_Machines_SubmachineState class attributes and methods

# State_Machines_SynchState class attributes and methods
State_Machines_SynchState_bound: Property = Property(name="bound", type=StringType)
State_Machines_SynchState.attributes={State_Machines_SynchState_bound}

# State_Machines_StubState class attributes and methods
State_Machines_StubState_referenceState: Property = Property(name="referenceState", type=StringType)
State_Machines_StubState.attributes={State_Machines_StubState_referenceState}

# State_Machines_FinalState class attributes and methods

# Core_Element class attributes and methods

# Core_ModelElement class attributes and methods
Core_ModelElement_name: Property = Property(name="name", type=StringType)
Core_ModelElement_visibility: Property = Property(name="visibility", type=StringType)
Core_ModelElement_isSpecification: Property = Property(name="isSpecification", type=StringType)
Core_ModelElement.attributes={Core_ModelElement_name, Core_ModelElement_isSpecification, Core_ModelElement_visibility}

# Element class attributes and methods

# Namespace class attributes and methods

# Core_GeneralizableElement class attributes and methods
Core_GeneralizableElement_isRoot: Property = Property(name="isRoot", type=StringType)
Core_GeneralizableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
Core_GeneralizableElement_isAbstract: Property = Property(name="isAbstract", type=StringType)
Core_GeneralizableElement.attributes={Core_GeneralizableElement_isLeaf, Core_GeneralizableElement_isAbstract, Core_GeneralizableElement_isRoot}

# Guard class attributes and methods

# Generalization_ class attributes and methods

# State_Machines_CompositeState class attributes and methods
State_Machines_CompositeState_isConcurrent: Property = Property(name="isConcurrent", type=StringType)
State_Machines_CompositeState.attributes={State_Machines_CompositeState_isConcurrent}

# State_Machines_ChangeEvent class attributes and methods

# BooleanExpression class attributes and methods

# State_Machines_Guard class attributes and methods

# Core_Classifier class attributes and methods

# GeneralizableElement class attributes and methods

# Feature class attributes and methods

# Core_Feature class attributes and methods
Core_Feature_ownerScope: Property = Property(name="ownerScope", type=StringType)
Core_Feature.attributes={Core_Feature_ownerScope}

# Core_Relationship class attributes and methods

# Core_BehavioralFeature class attributes and methods
Core_BehavioralFeature_isQuery: Property = Property(name="isQuery", type=StringType)
Core_BehavioralFeature.attributes={Core_BehavioralFeature_isQuery}

# Core_Operation class attributes and methods
Core_Operation_concurrency: Property = Property(name="concurrency", type=StringType)
Core_Operation_isRoot: Property = Property(name="isRoot", type=StringType)
Core_Operation_isLeaf: Property = Property(name="isLeaf", type=StringType)
Core_Operation_isAbstract: Property = Property(name="isAbstract", type=StringType)
Core_Operation_specification: Property = Property(name="specification", type=StringType)
Core_Operation.attributes={Core_Operation_concurrency, Core_Operation_isLeaf, Core_Operation_isRoot, Core_Operation_specification, Core_Operation_isAbstract}

# Core_Namespace class attributes and methods

# Core_Generalization class attributes and methods
Core_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
Core_Generalization.attributes={Core_Generalization_discriminator}

# Relationship class attributes and methods

# Core_Parameter class attributes and methods
Core_Parameter_kind: Property = Property(name="kind", type=StringType)
Core_Parameter.attributes={Core_Parameter_kind}

# Relationships
actualArgument0: BinaryAssociation = BinaryAssociation(
    name="actualArgument0",
    ends={
        Property(name="Argument", type=Common_Behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="action", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionSequence1: BinaryAssociation = BinaryAssociation(
    name="actionSequence1",
    ends={
        Property(name="ActionSequence", type=Common_Behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="action2", type=ActionSequence, multiplicity=Multiplicity(0, 1))
    }
)
recurrence3: BinaryAssociation = BinaryAssociation(
    name="recurrence3",
    ends={
        Property(name="IterationExpression", type=Common_Behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Action", type=IterationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signal10: BinaryAssociation = BinaryAssociation(
    name="signal10",
    ends={
        Property(name="Signal", type=Common_Behavior_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_SendAction", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
action11: BinaryAssociation = BinaryAssociation(
    name="action11",
    ends={
        Property(name="Action", type=Common_Behavior_ActionSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="actionSequence", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action12: BinaryAssociation = BinaryAssociation(
    name="action12",
    ends={
        Property(name="Action13", type=Common_Behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="actualArgument", type=Action, multiplicity=Multiplicity(0, 1))
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="Expression", type=Common_Behavior_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Argument", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal15: BinaryAssociation = BinaryAssociation(
    name="signal15",
    ends={
        Property(name="Signal16", type=Common_Behavior_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Reception", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="ObjectSetExpression", type=Common_Behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Action5", type=ObjectSetExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script6: BinaryAssociation = BinaryAssociation(
    name="script6",
    ends={
        Property(name="ActionExpression", type=Common_Behavior_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Action7", type=ActionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instantiation8: BinaryAssociation = BinaryAssociation(
    name="instantiation8",
    ends={
        Property(name="Classifier", type=Common_Behavior_CreateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_CreateAction", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operation9: BinaryAssociation = BinaryAssociation(
    name="operation9",
    ends={
        Property(name="Operation", type=Common_Behavior_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_CallAction", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
context17: BinaryAssociation = BinaryAssociation(
    name="context17",
    ends={
        Property(name="ModelElement", type=State_Machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_StateMachine", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
submachineState18: BinaryAssociation = BinaryAssociation(
    name="submachineState18",
    ends={
        Property(name="SubmachineState", type=State_Machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=SubmachineState, multiplicity=Multiplicity(0, 9999))
    }
)
top19: BinaryAssociation = BinaryAssociation(
    name="top19",
    ends={
        Property(name="State", type=State_Machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions20: BinaryAssociation = BinaryAssociation(
    name="transitions20",
    ends={
        Property(name="Transition", type=State_Machines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine21", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter22: BinaryAssociation = BinaryAssociation(
    name="parameter22",
    ends={
        Property(name="Parameter", type=State_Machines_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_Event", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container23: BinaryAssociation = BinaryAssociation(
    name="container23",
    ends={
        Property(name="CompositeState", type=State_Machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
incoming24: BinaryAssociation = BinaryAssociation(
    name="incoming24",
    ends={
        Property(name="Transition25", type=State_Machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing26: BinaryAssociation = BinaryAssociation(
    name="outgoing26",
    ends={
        Property(name="Transition27", type=State_Machines_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry38: BinaryAssociation = BinaryAssociation(
    name="entry38",
    ends={
        Property(name="Action40", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_State39", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine41: BinaryAssociation = BinaryAssociation(
    name="stateMachine41",
    ends={
        Property(name="StateMachine", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="top", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
when42: BinaryAssociation = BinaryAssociation(
    name="when42",
    ends={
        Property(name="TimeExpression", type=State_Machines_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_TimeEvent", type=TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation43: BinaryAssociation = BinaryAssociation(
    name="operation43",
    ends={
        Property(name="Operation44", type=State_Machines_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_CallEvent", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal45: BinaryAssociation = BinaryAssociation(
    name="signal45",
    ends={
        Property(name="Signal46", type=State_Machines_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_SignalEvent", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
target47: BinaryAssociation = BinaryAssociation(
    name="target47",
    ends={
        Property(name="StateVertex", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger48: BinaryAssociation = BinaryAssociation(
    name="trigger48",
    ends={
        Property(name="Event49", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_Transition", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine50: BinaryAssociation = BinaryAssociation(
    name="stateMachine50",
    ends={
        Property(name="StateMachine51", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source52: BinaryAssociation = BinaryAssociation(
    name="source52",
    ends={
        Property(name="StateVertex53", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
effect54: BinaryAssociation = BinaryAssociation(
    name="effect54",
    ends={
        Property(name="Action56", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_Transition55", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableEvent28: BinaryAssociation = BinaryAssociation(
    name="deferrableEvent28",
    ends={
        Property(name="Event", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_State", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
internalTransition29: BinaryAssociation = BinaryAssociation(
    name="internalTransition29",
    ends={
        Property(name="Transition31", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_State30", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit32: BinaryAssociation = BinaryAssociation(
    name="exit32",
    ends={
        Property(name="Action34", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_State33", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression63: BinaryAssociation = BinaryAssociation(
    name="expression63",
    ends={
        Property(name="BooleanExpression64", type=State_Machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_Guard", type=BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
doActivity35: BinaryAssociation = BinaryAssociation(
    name="doActivity35",
    ends={
        Property(name="Action37", type=State_Machines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_State36", type=Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachine65: BinaryAssociation = BinaryAssociation(
    name="submachine65",
    ends={
        Property(name="StateMachine66", type=State_Machines_SubmachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
namespace67: BinaryAssociation = BinaryAssociation(
    name="namespace67",
    ends={
        Property(name="Namespace", type=Core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
guard57: BinaryAssociation = BinaryAssociation(
    name="guard57",
    ends={
        Property(name="Guard", type=State_Machines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generalization68: BinaryAssociation = BinaryAssociation(
    name="generalization68",
    ends={
        Property(name="Generalization_", type=Core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex58: BinaryAssociation = BinaryAssociation(
    name="subvertex58",
    ends={
        Property(name="StateVertex59", type=State_Machines_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeExpression60: BinaryAssociation = BinaryAssociation(
    name="changeExpression60",
    ends={
        Property(name="BooleanExpression", type=State_Machines_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="State_Machines_ChangeEvent", type=BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transition61: BinaryAssociation = BinaryAssociation(
    name="transition61",
    ends={
        Property(name="Transition62", type=State_Machines_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
powertypeRange71: BinaryAssociation = BinaryAssociation(
    name="powertypeRange71",
    ends={
        Property(name="Generalization72", type=Core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
feature73: BinaryAssociation = BinaryAssociation(
    name="feature73",
    ends={
        Property(name="Feature", type=Core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner74: BinaryAssociation = BinaryAssociation(
    name="owner74",
    ends={
        Property(name="Classifier75", type=Core_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
parameter76: BinaryAssociation = BinaryAssociation(
    name="parameter76",
    ends={
        Property(name="Parameter77", type=Core_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioralFeature", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement69: BinaryAssociation = BinaryAssociation(
    name="ownedElement69",
    ends={
        Property(name="ModelElement70", type=Core_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent84: BinaryAssociation = BinaryAssociation(
    name="parent84",
    ends={
        Property(name="GeneralizableElement", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_Generalization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
powertype85: BinaryAssociation = BinaryAssociation(
    name="powertype85",
    ends={
        Property(name="Classifier86", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeRange", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
child87: BinaryAssociation = BinaryAssociation(
    name="child87",
    ends={
        Property(name="GeneralizableElement88", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="Classifier79", type=Core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_Parameter", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
behavioralFeature80: BinaryAssociation = BinaryAssociation(
    name="behavioralFeature80",
    ends={
        Property(name="BehavioralFeature", type=Core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue81: BinaryAssociation = BinaryAssociation(
    name="defaultValue81",
    ends={
        Property(name="Expression83", type=Core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_Parameter82", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Common_Behavior_Signal_Classifier = Generalization(general=Classifier, specific=Common_Behavior_Signal)
gen_Common_Behavior_Action_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_Action)
gen_Common_Behavior_ActionSequence_Action = Generalization(general=Action, specific=Common_Behavior_ActionSequence)
gen_Common_Behavior_Argument_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_Argument)
gen_Common_Behavior_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=Common_Behavior_Reception)
gen_Common_Behavior_ReturnAction_Action = Generalization(general=Action, specific=Common_Behavior_ReturnAction)
gen_Common_Behavior_TerminateAction_Action = Generalization(general=Action, specific=Common_Behavior_TerminateAction)
gen_Common_Behavior_Exception_Signal = Generalization(general=Signal, specific=Common_Behavior_Exception)
gen_Common_Behavior_CreateAction_Action = Generalization(general=Action, specific=Common_Behavior_CreateAction)
gen_Common_Behavior_DestroyAction_Action = Generalization(general=Action, specific=Common_Behavior_DestroyAction)
gen_Common_Behavior_UninterpretedAction_Action = Generalization(general=Action, specific=Common_Behavior_UninterpretedAction)
gen_Common_Behavior_CallAction_Action = Generalization(general=Action, specific=Common_Behavior_CallAction)
gen_Common_Behavior_SendAction_Action = Generalization(general=Action, specific=Common_Behavior_SendAction)
gen_Data_Types_BooleanExpression_Expression = Generalization(general=Expression, specific=Data_Types_BooleanExpression)
gen_Data_Types_ObjectSetExpression_Expression = Generalization(general=Expression, specific=Data_Types_ObjectSetExpression)
gen_Data_Types_ActionExpression_Expression = Generalization(general=Expression, specific=Data_Types_ActionExpression)
gen_Data_Types_IterationExpression_Expression = Generalization(general=Expression, specific=Data_Types_IterationExpression)
gen_Data_Types_TimeExpression_Expression = Generalization(general=Expression, specific=Data_Types_TimeExpression)
gen_State_Machines_StateMachine_ModelElement = Generalization(general=ModelElement, specific=State_Machines_StateMachine)
gen_State_Machines_Event_ModelElement = Generalization(general=ModelElement, specific=State_Machines_Event)
gen_State_Machines_StateVertex_ModelElement = Generalization(general=ModelElement, specific=State_Machines_StateVertex)
gen_State_Machines_TimeEvent_Event = Generalization(general=Event, specific=State_Machines_TimeEvent)
gen_State_Machines_CallEvent_Event = Generalization(general=Event, specific=State_Machines_CallEvent)
gen_State_Machines_SignalEvent_Event = Generalization(general=Event, specific=State_Machines_SignalEvent)
gen_State_Machines_Transition_ModelElement = Generalization(general=ModelElement, specific=State_Machines_Transition)
gen_State_Machines_State_StateVertex = Generalization(general=StateVertex, specific=State_Machines_State)
gen_State_Machines_Pseudostate_StateVertex = Generalization(general=StateVertex, specific=State_Machines_Pseudostate)
gen_State_Machines_SimpleState_State = Generalization(general=State, specific=State_Machines_SimpleState)
gen_State_Machines_SubmachineState_CompositeState = Generalization(general=CompositeState, specific=State_Machines_SubmachineState)
gen_State_Machines_SynchState_StateVertex = Generalization(general=StateVertex, specific=State_Machines_SynchState)
gen_State_Machines_StubState_StateVertex = Generalization(general=StateVertex, specific=State_Machines_StubState)
gen_State_Machines_FinalState_State = Generalization(general=State, specific=State_Machines_FinalState)
gen_Core_ModelElement_Element = Generalization(general=Element, specific=Core_ModelElement)
gen_Core_GeneralizableElement_ModelElement = Generalization(general=ModelElement, specific=Core_GeneralizableElement)
gen_State_Machines_CompositeState_State = Generalization(general=State, specific=State_Machines_CompositeState)
gen_State_Machines_ChangeEvent_Event = Generalization(general=Event, specific=State_Machines_ChangeEvent)
gen_State_Machines_Guard_ModelElement = Generalization(general=ModelElement, specific=State_Machines_Guard)
gen_Core_Classifier_GeneralizableElement = Generalization(general=GeneralizableElement, specific=Core_Classifier)
gen_Core_Classifier_Namespace = Generalization(general=Namespace, specific=Core_Classifier)
gen_Core_Feature_ModelElement = Generalization(general=ModelElement, specific=Core_Feature)
gen_Core_Relationship_ModelElement = Generalization(general=ModelElement, specific=Core_Relationship)
gen_Core_BehavioralFeature_Feature = Generalization(general=Feature, specific=Core_BehavioralFeature)
gen_Core_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=Core_Operation)
gen_Core_Namespace_ModelElement = Generalization(general=ModelElement, specific=Core_Namespace)
gen_Core_Generalization_Relationship = Generalization(general=Relationship, specific=Core_Generalization)
gen_Core_Parameter_ModelElement = Generalization(general=ModelElement, specific=Core_Parameter)

# Domain Model
domain_model = DomainModel(
    name="Core",
    types={Common_Behavior_Signal, Classifier, Common_Behavior_Action, ModelElement, Argument, ActionSequence, IterationExpression, ObjectSetExpression, Signal, Common_Behavior_ActionSequence, Common_Behavior_Argument, Expression, Common_Behavior_Reception, BehavioralFeature, Common_Behavior_ReturnAction, Common_Behavior_TerminateAction, Common_Behavior_Exception, ActionExpression, Common_Behavior_CreateAction, Action, Common_Behavior_DestroyAction, Common_Behavior_UninterpretedAction, Common_Behavior_CallAction, Operation, Common_Behavior_SendAction, Data_Types_BooleanExpression, Data_Types_ObjectSetExpression, Data_Types_ActionExpression, Data_Types_IterationExpression, Data_Types_TimeExpression, State_Machines_StateMachine, SubmachineState, State, Transition, State_Machines_Event, Parameter_, State_Machines_StateVertex, CompositeState, Data_Types_Expression, StateMachine, State_Machines_TimeEvent, TimeExpression, State_Machines_CallEvent, State_Machines_SignalEvent, State_Machines_Transition, State_Machines_State, StateVertex, Event, State_Machines_Pseudostate, State_Machines_SimpleState, State_Machines_SubmachineState, State_Machines_SynchState, State_Machines_StubState, State_Machines_FinalState, Core_Element, Core_ModelElement, Element, Namespace, Core_GeneralizableElement, Guard, Generalization_, State_Machines_CompositeState, State_Machines_ChangeEvent, BooleanExpression, State_Machines_Guard, Core_Classifier, GeneralizableElement, Feature, Core_Feature, Core_Relationship, Core_BehavioralFeature, Core_Operation, Core_Namespace, Core_Generalization, Relationship, Core_Parameter, CallConcurrencyKind, ParameterDirectionKind, ScopeKind, PseudostateKind, VisibilityKind},
    associations={actualArgument0, actionSequence1, recurrence3, signal10, action11, action12, value14, signal15, target4, script6, instantiation8, operation9, context17, submachineState18, top19, transitions20, parameter22, container23, incoming24, outgoing26, entry38, stateMachine41, when42, operation43, signal45, target47, trigger48, stateMachine50, source52, effect54, deferrableEvent28, internalTransition29, exit32, expression63, doActivity35, submachine65, namespace67, guard57, generalization68, subvertex58, changeExpression60, transition61, powertypeRange71, feature73, owner74, parameter76, ownedElement69, parent84, powertype85, child87, type78, behavioralFeature80, defaultValue81},
    generalizations={gen_Common_Behavior_Signal_Classifier, gen_Common_Behavior_Action_ModelElement, gen_Common_Behavior_ActionSequence_Action, gen_Common_Behavior_Argument_ModelElement, gen_Common_Behavior_Reception_BehavioralFeature, gen_Common_Behavior_ReturnAction_Action, gen_Common_Behavior_TerminateAction_Action, gen_Common_Behavior_Exception_Signal, gen_Common_Behavior_CreateAction_Action, gen_Common_Behavior_DestroyAction_Action, gen_Common_Behavior_UninterpretedAction_Action, gen_Common_Behavior_CallAction_Action, gen_Common_Behavior_SendAction_Action, gen_Data_Types_BooleanExpression_Expression, gen_Data_Types_ObjectSetExpression_Expression, gen_Data_Types_ActionExpression_Expression, gen_Data_Types_IterationExpression_Expression, gen_Data_Types_TimeExpression_Expression, gen_State_Machines_StateMachine_ModelElement, gen_State_Machines_Event_ModelElement, gen_State_Machines_StateVertex_ModelElement, gen_State_Machines_TimeEvent_Event, gen_State_Machines_CallEvent_Event, gen_State_Machines_SignalEvent_Event, gen_State_Machines_Transition_ModelElement, gen_State_Machines_State_StateVertex, gen_State_Machines_Pseudostate_StateVertex, gen_State_Machines_SimpleState_State, gen_State_Machines_SubmachineState_CompositeState, gen_State_Machines_SynchState_StateVertex, gen_State_Machines_StubState_StateVertex, gen_State_Machines_FinalState_State, gen_Core_ModelElement_Element, gen_Core_GeneralizableElement_ModelElement, gen_State_Machines_CompositeState_State, gen_State_Machines_ChangeEvent_Event, gen_State_Machines_Guard_ModelElement, gen_Core_Classifier_GeneralizableElement, gen_Core_Classifier_Namespace, gen_Core_Feature_ModelElement, gen_Core_Relationship_ModelElement, gen_Core_BehavioralFeature_Feature, gen_Core_Operation_BehavioralFeature, gen_Core_Namespace_ModelElement, gen_Core_Generalization_Relationship, gen_Core_Parameter_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)