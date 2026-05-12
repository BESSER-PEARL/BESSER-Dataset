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
TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="m"),
			EnumerationLiteral(name="h")
    }
)

# Classes
scxmlxt_StateMachine = Class(name="scxmlxt_StateMachine")
AbstractState = Class(name="AbstractState")
scxmlxt_ResourceImport = Class(name="scxmlxt_ResourceImport", is_abstract=True)
scxmlxt_State = Class(name="scxmlxt_State")
scxmlxt_InitialTransition = Class(name="scxmlxt_InitialTransition")
scxmlxt_Action = Class(name="scxmlxt_Action", is_abstract=True)
scxmlxt_AbstractState = Class(name="scxmlxt_AbstractState", is_abstract=True)
scxmlxt_AbstractTransition = Class(name="scxmlxt_AbstractTransition", is_abstract=True)
scxmlxt_VarDef = Class(name="scxmlxt_VarDef")
scxmlxt_Event = Class(name="scxmlxt_Event", is_abstract=True)
scxmlxt_Condition = Class(name="scxmlxt_Condition")
scxmlxt_Transition = Class(name="scxmlxt_Transition")
AbstractTransition = Class(name="AbstractTransition")
scxmlxt_InternalTransition = Class(name="scxmlxt_InternalTransition")
scxmlxt_SymbolicEvent = Class(name="scxmlxt_SymbolicEvent")
Event = Class(name="Event")
scxmlxt_AbstractTransitionEvent = Class(name="scxmlxt_AbstractTransitionEvent", is_abstract=True)
scxmlxt_TransitionEvent = Class(name="scxmlxt_TransitionEvent")
AbstractTransitionEvent = Class(name="AbstractTransitionEvent")
scxmlxt_EnterEvent = Class(name="scxmlxt_EnterEvent")
scxmlxt_ExitEvent = Class(name="scxmlxt_ExitEvent")
scxmlxt_ScriptEvent = Class(name="scxmlxt_ScriptEvent")
scxmlxt_TimerEvent = Class(name="scxmlxt_TimerEvent")
scxmlxt_Expression = Class(name="scxmlxt_Expression", is_abstract=True)
scxmlxt_SymbolicAction = Class(name="scxmlxt_SymbolicAction")
Action = Class(name="Action")
scxmlxt_ScriptAction = Class(name="scxmlxt_ScriptAction")
scxmlxt_Typed = Class(name="scxmlxt_Typed")
scxmlxt_EClassifier = Class(name="scxmlxt_EClassifier")
Typed = Class(name="Typed")
scxmlxt_AssignmentAction = Class(name="scxmlxt_AssignmentAction")
scxmlxt_EPath = Class(name="scxmlxt_EPath")
scxmlxt_EStep = Class(name="scxmlxt_EStep")
scxmlxt_EStepFilter = Class(name="scxmlxt_EStepFilter")
scxmlxt_ScriptExpression = Class(name="scxmlxt_ScriptExpression")
scxmlxt_Literal = Class(name="scxmlxt_Literal", is_abstract=True)
scxmlxt_BooleanLiteral = Class(name="scxmlxt_BooleanLiteral")
Literal = Class(name="Literal")
scxmlxt_IntLiteral = Class(name="scxmlxt_IntLiteral")
scxmlxt_FloatLiteral = Class(name="scxmlxt_FloatLiteral")
scxmlxt_StringLiteral = Class(name="scxmlxt_StringLiteral")
scxmlxt_VarRef = Class(name="scxmlxt_VarRef")
Expression = Class(name="Expression")
scxmlxt_AbstractUriLiteral = Class(name="scxmlxt_AbstractUriLiteral")
scxmlxt_UriLiteral = Class(name="scxmlxt_UriLiteral")
AbstractUriLiteral = Class(name="AbstractUriLiteral")
scxmlxt_ResourceUriLiteral = Class(name="scxmlxt_ResourceUriLiteral")
scxmlxt_EObjectUriLiteral = Class(name="scxmlxt_EObjectUriLiteral")
ResourceUriLiteral = Class(name="ResourceUriLiteral")
scxmlxt_EObjectReference = Class(name="scxmlxt_EObjectReference")
scxmlxt_EObject = Class(name="scxmlxt_EObject")
scxmlxt_DelayLiteral = Class(name="scxmlxt_DelayLiteral")
IntLiteral = Class(name="IntLiteral")
scxmlxt_DomainModelImport = Class(name="scxmlxt_DomainModelImport")
ResourceImport = Class(name="ResourceImport")
scxmlxt_DomainDataImport = Class(name="scxmlxt_DomainDataImport")

# scxmlxt_StateMachine class attributes and methods

# AbstractState class attributes and methods

# scxmlxt_ResourceImport class attributes and methods
scxmlxt_ResourceImport_importURI: Property = Property(name="importURI", type=StringType)
scxmlxt_ResourceImport.attributes={scxmlxt_ResourceImport_importURI}

# scxmlxt_State class attributes and methods
scxmlxt_State_name: Property = Property(name="name", type=StringType)
scxmlxt_State.attributes={scxmlxt_State_name}

# scxmlxt_InitialTransition class attributes and methods

# scxmlxt_Action class attributes and methods

# scxmlxt_AbstractState class attributes and methods

# scxmlxt_AbstractTransition class attributes and methods

# scxmlxt_VarDef class attributes and methods
scxmlxt_VarDef_name: Property = Property(name="name", type=StringType)
scxmlxt_VarDef.attributes={scxmlxt_VarDef_name}

# scxmlxt_Event class attributes and methods

# scxmlxt_Condition class attributes and methods
scxmlxt_Condition_script: Property = Property(name="script", type=StringType)
scxmlxt_Condition.attributes={scxmlxt_Condition_script}

# scxmlxt_Transition class attributes and methods

# AbstractTransition class attributes and methods

# scxmlxt_InternalTransition class attributes and methods

# scxmlxt_SymbolicEvent class attributes and methods
scxmlxt_SymbolicEvent_name: Property = Property(name="name", type=StringType)
scxmlxt_SymbolicEvent.attributes={scxmlxt_SymbolicEvent_name}

# Event class attributes and methods

# scxmlxt_AbstractTransitionEvent class attributes and methods
scxmlxt_AbstractTransitionEvent_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
scxmlxt_AbstractTransitionEvent_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
scxmlxt_AbstractTransitionEvent.methods={scxmlxt_AbstractTransitionEvent_m_getTarget, scxmlxt_AbstractTransitionEvent_m_getSource}

# scxmlxt_TransitionEvent class attributes and methods

# AbstractTransitionEvent class attributes and methods

# scxmlxt_EnterEvent class attributes and methods

# scxmlxt_ExitEvent class attributes and methods

# scxmlxt_ScriptEvent class attributes and methods
scxmlxt_ScriptEvent_script: Property = Property(name="script", type=StringType)
scxmlxt_ScriptEvent.attributes={scxmlxt_ScriptEvent_script}

# scxmlxt_TimerEvent class attributes and methods

# scxmlxt_Expression class attributes and methods

# scxmlxt_SymbolicAction class attributes and methods
scxmlxt_SymbolicAction_name: Property = Property(name="name", type=StringType)
scxmlxt_SymbolicAction.attributes={scxmlxt_SymbolicAction_name}

# Action class attributes and methods

# scxmlxt_ScriptAction class attributes and methods
scxmlxt_ScriptAction_script: Property = Property(name="script", type=StringType)
scxmlxt_ScriptAction.attributes={scxmlxt_ScriptAction_script}

# scxmlxt_Typed class attributes and methods
scxmlxt_Typed_many: Property = Property(name="many", type=BooleanType)
scxmlxt_Typed.attributes={scxmlxt_Typed_many}

# scxmlxt_EClassifier class attributes and methods

# Typed class attributes and methods

# scxmlxt_AssignmentAction class attributes and methods

# scxmlxt_EPath class attributes and methods

# scxmlxt_EStep class attributes and methods
scxmlxt_EStep_featureName: Property = Property(name="featureName", type=StringType)
scxmlxt_EStep.attributes={scxmlxt_EStep_featureName}

# scxmlxt_EStepFilter class attributes and methods
scxmlxt_EStepFilter_freeVarName: Property = Property(name="freeVarName", type=StringType)
scxmlxt_EStepFilter.attributes={scxmlxt_EStepFilter_freeVarName}

# scxmlxt_ScriptExpression class attributes and methods
scxmlxt_ScriptExpression_script: Property = Property(name="script", type=StringType)
scxmlxt_ScriptExpression.attributes={scxmlxt_ScriptExpression_script}

# scxmlxt_Literal class attributes and methods

# scxmlxt_BooleanLiteral class attributes and methods
scxmlxt_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
scxmlxt_BooleanLiteral.attributes={scxmlxt_BooleanLiteral_booleanValue}

# Literal class attributes and methods

# scxmlxt_IntLiteral class attributes and methods
scxmlxt_IntLiteral_intValue: Property = Property(name="intValue", type=IntegerType)
scxmlxt_IntLiteral.attributes={scxmlxt_IntLiteral_intValue}

# scxmlxt_FloatLiteral class attributes and methods
scxmlxt_FloatLiteral_floatValue: Property = Property(name="floatValue", type=FloatType)
scxmlxt_FloatLiteral.attributes={scxmlxt_FloatLiteral_floatValue}

# scxmlxt_StringLiteral class attributes and methods
scxmlxt_StringLiteral_stringValue: Property = Property(name="stringValue", type=StringType)
scxmlxt_StringLiteral.attributes={scxmlxt_StringLiteral_stringValue}

# scxmlxt_VarRef class attributes and methods

# Expression class attributes and methods

# scxmlxt_AbstractUriLiteral class attributes and methods
scxmlxt_AbstractUriLiteral_uri: Property = Property(name="uri", type=StringType)
scxmlxt_AbstractUriLiteral.attributes={scxmlxt_AbstractUriLiteral_uri}

# scxmlxt_UriLiteral class attributes and methods
scxmlxt_UriLiteral_uriValue: Property = Property(name="uriValue", type=StringType)
scxmlxt_UriLiteral.attributes={scxmlxt_UriLiteral_uriValue}

# AbstractUriLiteral class attributes and methods

# scxmlxt_ResourceUriLiteral class attributes and methods
scxmlxt_ResourceUriLiteral_resourceUri: Property = Property(name="resourceUri", type=StringType)
scxmlxt_ResourceUriLiteral.attributes={scxmlxt_ResourceUriLiteral_resourceUri}

# scxmlxt_EObjectUriLiteral class attributes and methods
scxmlxt_EObjectUriLiteral_uriFragment: Property = Property(name="uriFragment", type=StringType)
scxmlxt_EObjectUriLiteral.attributes={scxmlxt_EObjectUriLiteral_uriFragment}

# ResourceUriLiteral class attributes and methods

# scxmlxt_EObjectReference class attributes and methods

# scxmlxt_EObject class attributes and methods

# scxmlxt_DelayLiteral class attributes and methods
scxmlxt_DelayLiteral_timeUnit: Property = Property(name="timeUnit", type=StringType)
scxmlxt_DelayLiteral.attributes={scxmlxt_DelayLiteral_timeUnit}

# IntLiteral class attributes and methods

# scxmlxt_DomainModelImport class attributes and methods

# ResourceImport class attributes and methods

# scxmlxt_DomainDataImport class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="scxmlxt_ResourceImport", type=scxmlxt_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_StateMachine", type=scxmlxt_ResourceImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentStates1: BinaryAssociation = BinaryAssociation(
    name="currentStates1",
    ends={
        Property(name="scxmlxt_State", type=scxmlxt_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_StateMachine2", type=scxmlxt_State, multiplicity=Multiplicity(0, 9999))
    }
)
initialTransition3: BinaryAssociation = BinaryAssociation(
    name="initialTransition3",
    ends={
        Property(name="scxmlxt_InitialTransition", type=scxmlxt_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_State4", type=scxmlxt_InitialTransition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action5: BinaryAssociation = BinaryAssociation(
    name="action5",
    ends={
        Property(name="scxmlxt_Action", type=scxmlxt_InitialTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_InitialTransition6", type=scxmlxt_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="scxmlxt_State8", type=scxmlxt_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractState", type=scxmlxt_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="scxmlxt_AbstractTransition", type=scxmlxt_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractState10", type=scxmlxt_AbstractTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables11: BinaryAssociation = BinaryAssociation(
    name="variables11",
    ends={
        Property(name="scxmlxt_VarDef", type=scxmlxt_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractState12", type=scxmlxt_VarDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event13: BinaryAssociation = BinaryAssociation(
    name="event13",
    ends={
        Property(name="scxmlxt_Event", type=scxmlxt_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractTransition14", type=scxmlxt_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="scxmlxt_Condition", type=scxmlxt_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractTransition16", type=scxmlxt_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action17: BinaryAssociation = BinaryAssociation(
    name="action17",
    ends={
        Property(name="scxmlxt_Action19", type=scxmlxt_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AbstractTransition18", type=scxmlxt_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="scxmlxt_State21", type=scxmlxt_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_Transition", type=scxmlxt_State, multiplicity=Multiplicity(0, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="scxmlxt_State26", type=scxmlxt_TransitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_TransitionEvent25", type=scxmlxt_State, multiplicity=Multiplicity(0, 1))
    }
)
event27: BinaryAssociation = BinaryAssociation(
    name="event27",
    ends={
        Property(name="scxmlxt_Event28", type=scxmlxt_TimerEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_TimerEvent", type=scxmlxt_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delay29: BinaryAssociation = BinaryAssociation(
    name="delay29",
    ends={
        Property(name="scxmlxt_Expression", type=scxmlxt_TimerEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_TimerEvent30", type=scxmlxt_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="scxmlxt_State23", type=scxmlxt_TransitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_TransitionEvent", type=scxmlxt_State, multiplicity=Multiplicity(0, 1))
    }
)
delay31: BinaryAssociation = BinaryAssociation(
    name="delay31",
    ends={
        Property(name="scxmlxt_Expression32", type=scxmlxt_SymbolicAction, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_SymbolicAction", type=scxmlxt_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eType33: BinaryAssociation = BinaryAssociation(
    name="eType33",
    ends={
        Property(name="scxmlxt_EClassifier", type=scxmlxt_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_Typed", type=scxmlxt_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
init34: BinaryAssociation = BinaryAssociation(
    name="init34",
    ends={
        Property(name="scxmlxt_Expression36", type=scxmlxt_VarDef, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_VarDef35", type=scxmlxt_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var37: BinaryAssociation = BinaryAssociation(
    name="var37",
    ends={
        Property(name="scxmlxt_VarDef38", type=scxmlxt_AssignmentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AssignmentAction", type=scxmlxt_VarDef, multiplicity=Multiplicity(0, 1))
    }
)
value39: BinaryAssociation = BinaryAssociation(
    name="value39",
    ends={
        Property(name="scxmlxt_Expression41", type=scxmlxt_AssignmentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_AssignmentAction40", type=scxmlxt_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var42: BinaryAssociation = BinaryAssociation(
    name="var42",
    ends={
        Property(name="scxmlxt_VarDef43", type=scxmlxt_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_VarRef", type=scxmlxt_VarDef, multiplicity=Multiplicity(0, 1))
    }
)
var44: BinaryAssociation = BinaryAssociation(
    name="var44",
    ends={
        Property(name="scxmlxt_VarRef45", type=scxmlxt_EPath, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_EPath", type=scxmlxt_VarRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
steps46: BinaryAssociation = BinaryAssociation(
    name="steps46",
    ends={
        Property(name="scxmlxt_EStep", type=scxmlxt_EPath, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_EPath47", type=scxmlxt_EStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter48: BinaryAssociation = BinaryAssociation(
    name="filter48",
    ends={
        Property(name="scxmlxt_EStepFilter", type=scxmlxt_EStep, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_EStep49", type=scxmlxt_EStepFilter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script50: BinaryAssociation = BinaryAssociation(
    name="script50",
    ends={
        Property(name="scxmlxt_ScriptExpression", type=scxmlxt_EStepFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_EStepFilter51", type=scxmlxt_ScriptExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eObject52: BinaryAssociation = BinaryAssociation(
    name="eObject52",
    ends={
        Property(name="scxmlxt_EObject", type=scxmlxt_EObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="scxmlxt_EObjectReference", type=scxmlxt_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_scxmlxt_StateMachine_AbstractState = Generalization(general=AbstractState, specific=scxmlxt_StateMachine)
gen_scxmlxt_State_AbstractState = Generalization(general=AbstractState, specific=scxmlxt_State)
gen_scxmlxt_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=scxmlxt_Transition)
gen_scxmlxt_InternalTransition_AbstractTransition = Generalization(general=AbstractTransition, specific=scxmlxt_InternalTransition)
gen_scxmlxt_SymbolicEvent_Event = Generalization(general=Event, specific=scxmlxt_SymbolicEvent)
gen_scxmlxt_AbstractTransitionEvent_Event = Generalization(general=Event, specific=scxmlxt_AbstractTransitionEvent)
gen_scxmlxt_TransitionEvent_AbstractTransitionEvent = Generalization(general=AbstractTransitionEvent, specific=scxmlxt_TransitionEvent)
gen_scxmlxt_EnterEvent_AbstractTransitionEvent = Generalization(general=AbstractTransitionEvent, specific=scxmlxt_EnterEvent)
gen_scxmlxt_ExitEvent_AbstractTransitionEvent = Generalization(general=AbstractTransitionEvent, specific=scxmlxt_ExitEvent)
gen_scxmlxt_ScriptEvent_Event = Generalization(general=Event, specific=scxmlxt_ScriptEvent)
gen_scxmlxt_TimerEvent_Event = Generalization(general=Event, specific=scxmlxt_TimerEvent)
gen_scxmlxt_SymbolicAction_Action = Generalization(general=Action, specific=scxmlxt_SymbolicAction)
gen_scxmlxt_ScriptAction_Action = Generalization(general=Action, specific=scxmlxt_ScriptAction)
gen_scxmlxt_VarDef_Typed = Generalization(general=Typed, specific=scxmlxt_VarDef)
gen_scxmlxt_AssignmentAction_Action = Generalization(general=Action, specific=scxmlxt_AssignmentAction)
gen_scxmlxt_EPath_Expression = Generalization(general=Expression, specific=scxmlxt_EPath)
gen_scxmlxt_Literal_Expression = Generalization(general=Expression, specific=scxmlxt_Literal)
gen_scxmlxt_BooleanLiteral_Literal = Generalization(general=Literal, specific=scxmlxt_BooleanLiteral)
gen_scxmlxt_IntLiteral_Literal = Generalization(general=Literal, specific=scxmlxt_IntLiteral)
gen_scxmlxt_FloatLiteral_Literal = Generalization(general=Literal, specific=scxmlxt_FloatLiteral)
gen_scxmlxt_StringLiteral_Literal = Generalization(general=Literal, specific=scxmlxt_StringLiteral)
gen_scxmlxt_VarRef_Expression = Generalization(general=Expression, specific=scxmlxt_VarRef)
gen_scxmlxt_AbstractUriLiteral_Literal = Generalization(general=Literal, specific=scxmlxt_AbstractUriLiteral)
gen_scxmlxt_UriLiteral_AbstractUriLiteral = Generalization(general=AbstractUriLiteral, specific=scxmlxt_UriLiteral)
gen_scxmlxt_ResourceUriLiteral_AbstractUriLiteral = Generalization(general=AbstractUriLiteral, specific=scxmlxt_ResourceUriLiteral)
gen_scxmlxt_EObjectUriLiteral_ResourceUriLiteral = Generalization(general=ResourceUriLiteral, specific=scxmlxt_EObjectUriLiteral)
gen_scxmlxt_DelayLiteral_IntLiteral = Generalization(general=IntLiteral, specific=scxmlxt_DelayLiteral)
gen_scxmlxt_DomainModelImport_ResourceImport = Generalization(general=ResourceImport, specific=scxmlxt_DomainModelImport)
gen_scxmlxt_DomainDataImport_ResourceImport = Generalization(general=ResourceImport, specific=scxmlxt_DomainDataImport)
gen_scxmlxt_ScriptExpression_Expression = Generalization(general=Expression, specific=scxmlxt_ScriptExpression)

# Domain Model
domain_model = DomainModel(
    name="scxmlxt",
    types={scxmlxt_StateMachine, AbstractState, scxmlxt_ResourceImport, scxmlxt_State, scxmlxt_InitialTransition, scxmlxt_Action, scxmlxt_AbstractState, scxmlxt_AbstractTransition, scxmlxt_VarDef, scxmlxt_Event, scxmlxt_Condition, scxmlxt_Transition, AbstractTransition, scxmlxt_InternalTransition, scxmlxt_SymbolicEvent, Event, scxmlxt_AbstractTransitionEvent, scxmlxt_TransitionEvent, AbstractTransitionEvent, scxmlxt_EnterEvent, scxmlxt_ExitEvent, scxmlxt_ScriptEvent, scxmlxt_TimerEvent, scxmlxt_Expression, scxmlxt_SymbolicAction, Action, scxmlxt_ScriptAction, scxmlxt_Typed, scxmlxt_EClassifier, Typed, scxmlxt_AssignmentAction, scxmlxt_EPath, scxmlxt_EStep, scxmlxt_EStepFilter, scxmlxt_ScriptExpression, scxmlxt_Literal, scxmlxt_BooleanLiteral, Literal, scxmlxt_IntLiteral, scxmlxt_FloatLiteral, scxmlxt_StringLiteral, scxmlxt_VarRef, Expression, scxmlxt_AbstractUriLiteral, scxmlxt_UriLiteral, AbstractUriLiteral, scxmlxt_ResourceUriLiteral, scxmlxt_EObjectUriLiteral, ResourceUriLiteral, scxmlxt_EObjectReference, scxmlxt_EObject, scxmlxt_DelayLiteral, IntLiteral, scxmlxt_DomainModelImport, ResourceImport, scxmlxt_DomainDataImport, TimeUnit},
    associations={imports0, currentStates1, initialTransition3, action5, states7, transitions9, variables11, event13, condition15, action17, target20, target24, event27, delay29, source22, delay31, eType33, init34, var37, value39, var42, var44, steps46, filter48, script50, eObject52},
    generalizations={gen_scxmlxt_StateMachine_AbstractState, gen_scxmlxt_State_AbstractState, gen_scxmlxt_Transition_AbstractTransition, gen_scxmlxt_InternalTransition_AbstractTransition, gen_scxmlxt_SymbolicEvent_Event, gen_scxmlxt_AbstractTransitionEvent_Event, gen_scxmlxt_TransitionEvent_AbstractTransitionEvent, gen_scxmlxt_EnterEvent_AbstractTransitionEvent, gen_scxmlxt_ExitEvent_AbstractTransitionEvent, gen_scxmlxt_ScriptEvent_Event, gen_scxmlxt_TimerEvent_Event, gen_scxmlxt_SymbolicAction_Action, gen_scxmlxt_ScriptAction_Action, gen_scxmlxt_VarDef_Typed, gen_scxmlxt_AssignmentAction_Action, gen_scxmlxt_EPath_Expression, gen_scxmlxt_Literal_Expression, gen_scxmlxt_BooleanLiteral_Literal, gen_scxmlxt_IntLiteral_Literal, gen_scxmlxt_FloatLiteral_Literal, gen_scxmlxt_StringLiteral_Literal, gen_scxmlxt_VarRef_Expression, gen_scxmlxt_AbstractUriLiteral_Literal, gen_scxmlxt_UriLiteral_AbstractUriLiteral, gen_scxmlxt_ResourceUriLiteral_AbstractUriLiteral, gen_scxmlxt_EObjectUriLiteral_ResourceUriLiteral, gen_scxmlxt_DelayLiteral_IntLiteral, gen_scxmlxt_DomainModelImport_ResourceImport, gen_scxmlxt_DomainDataImport_ResourceImport, gen_scxmlxt_ScriptExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)