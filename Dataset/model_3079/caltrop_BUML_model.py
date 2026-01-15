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
ChannelSelectorKeyword: Enumeration = Enumeration(
    name="ChannelSelectorKeyword",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="ANY")
    }
)

# Classes
caltrop_Schedule = Class(name="caltrop::Schedule")
caltrop_ActorParameter = Class(name="caltrop::ActorParameter")
Parameter_ = Class(name="Parameter")
caltrop_TypedInputPort = Class(name="caltrop::TypedInputPort")
AbstractTypedIOPort = Class(name="AbstractTypedIOPort")
caltrop_TypedOutputPort = Class(name="caltrop::TypedOutputPort")
Variable = Class(name="Variable")
caltrop_XExpression = Class(name="caltrop::XExpression")
caltrop_Realm = Class(name="caltrop::Realm")
caltrop_CaltropActorImpl = Class(name="caltrop::CaltropActorImpl")
caltrop_StateVariable = Class(name="caltrop::StateVariable")
caltrop_ReAction = Class(name="caltrop::ReAction")
caltrop_OutputAction = Class(name="caltrop::OutputAction")
caltrop_FunctionDeclaration = Class(name="caltrop::FunctionDeclaration")
caltrop_OutputPattern = Class(name="caltrop::OutputPattern")
caltrop_PortPattern = Class(name="caltrop::PortPattern", is_abstract=True)
caltrop_FireAction = Class(name="caltrop::FireAction")
ReAction = Class(name="ReAction")
caltrop_InputPattern = Class(name="caltrop::InputPattern")
OutputAction = Class(name="OutputAction")
NamedObj = Class(name="NamedObj")
ActionPattern = Class(name="ActionPattern")
caltrop_ExpressionChannelSelector = Class(name="caltrop::ExpressionChannelSelector")
ChannelSelector = Class(name="ChannelSelector")
caltrop_KeywordChannelSelector = Class(name="caltrop::KeywordChannelSelector")
caltrop_ChannelSelector = Class(name="caltrop::ChannelSelector", is_abstract=True)
caltrop_Port = Class(name="caltrop::Port")
caltrop_ActionPattern = Class(name="caltrop::ActionPattern")
PortPattern = Class(name="PortPattern")
caltrop_JvmTypeReference = Class(name="caltrop::JvmTypeReference")
caltrop_State = Class(name="caltrop::State")
caltrop_Transition = Class(name="caltrop::Transition")
JvmTypedObj = Class(name="JvmTypedObj")
caltrop_JvmTypedObj = Class(name="caltrop::JvmTypedObj")
caltrop_EventPattern = Class(name="caltrop::EventPattern")
caltrop_EventAction = Class(name="caltrop::EventAction")
caltrop_ConversionRelation = Class(name="caltrop::ConversionRelation")
Relation = Class(name="Relation")

# caltrop_Schedule class attributes and methods

# caltrop_ActorParameter class attributes and methods

# Parameter class attributes and methods

# caltrop_TypedInputPort class attributes and methods

# AbstractTypedIOPort class attributes and methods

# caltrop_TypedOutputPort class attributes and methods

# Variable class attributes and methods

# caltrop_XExpression class attributes and methods

# caltrop_Realm class attributes and methods
caltrop_Realm_key: Property = Property(name="key", type=StringType)
caltrop_Realm.attributes={caltrop_Realm_key}

# caltrop_CaltropActorImpl class attributes and methods

# caltrop_StateVariable class attributes and methods
caltrop_StateVariable_constant: Property = Property(name="constant", type=BooleanType)
caltrop_StateVariable_binding: Property = Property(name="binding", type=BooleanType)
caltrop_StateVariable.attributes={caltrop_StateVariable_constant, caltrop_StateVariable_binding}

# caltrop_ReAction class attributes and methods

# caltrop_OutputAction class attributes and methods
caltrop_OutputAction_m_getInputPatterns: Method = Method(name="getInputPatterns", parameters={}, type=StringType)
caltrop_OutputAction.methods={caltrop_OutputAction_m_getInputPatterns}

# caltrop_FunctionDeclaration class attributes and methods

# caltrop_OutputPattern class attributes and methods

# caltrop_PortPattern class attributes and methods
caltrop_PortPattern_m_size: Method = Method(name="size", parameters={}, type=IntegerType)
caltrop_PortPattern.methods={caltrop_PortPattern_m_size}

# caltrop_FireAction class attributes and methods

# ReAction class attributes and methods

# caltrop_InputPattern class attributes and methods
caltrop_InputPattern_variables: Property = Property(name="variables", type=StringType)
caltrop_InputPattern.attributes={caltrop_InputPattern_variables}

# OutputAction class attributes and methods

# NamedObj class attributes and methods

# ActionPattern class attributes and methods

# caltrop_ExpressionChannelSelector class attributes and methods
caltrop_ExpressionChannelSelector_many: Property = Property(name="many", type=BooleanType)
caltrop_ExpressionChannelSelector.attributes={caltrop_ExpressionChannelSelector_many}

# ChannelSelector class attributes and methods

# caltrop_KeywordChannelSelector class attributes and methods
caltrop_KeywordChannelSelector_keyword: Property = Property(name="keyword", type=StringType)
caltrop_KeywordChannelSelector.attributes={caltrop_KeywordChannelSelector_keyword}

# caltrop_ChannelSelector class attributes and methods

# caltrop_Port class attributes and methods

# caltrop_ActionPattern class attributes and methods
caltrop_ActionPattern_m_getPatternVariables: Method = Method(name="getPatternVariables", parameters={}, type=StringType)
caltrop_ActionPattern_m_getGuardExpression: Method = Method(name="getGuardExpression", parameters={}, type=StringType)
caltrop_ActionPattern.methods={caltrop_ActionPattern_m_getGuardExpression, caltrop_ActionPattern_m_getPatternVariables}

# PortPattern class attributes and methods

# caltrop_JvmTypeReference class attributes and methods

# caltrop_State class attributes and methods

# caltrop_Transition class attributes and methods

# JvmTypedObj class attributes and methods

# caltrop_JvmTypedObj class attributes and methods

# caltrop_EventPattern class attributes and methods
caltrop_EventPattern_name: Property = Property(name="name", type=StringType)
caltrop_EventPattern_qualifier: Property = Property(name="qualifier", type=StringType)
caltrop_EventPattern_variables: Property = Property(name="variables", type=StringType)
caltrop_EventPattern_property: Property = Property(name="property", type=BooleanType)
caltrop_EventPattern.attributes={caltrop_EventPattern_variables, caltrop_EventPattern_property, caltrop_EventPattern_qualifier, caltrop_EventPattern_name}

# caltrop_EventAction class attributes and methods

# caltrop_ConversionRelation class attributes and methods
caltrop_ConversionRelation_valueVar: Property = Property(name="valueVar", type=StringType)
caltrop_ConversionRelation.attributes={caltrop_ConversionRelation_valueVar}

# Relation class attributes and methods

# Relationships
schedule7: BinaryAssociation = BinaryAssociation(
    name="schedule7",
    ends={
        Property(name="caltrop_Schedule", type=caltrop_CaltropActorImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_CaltropActorImpl8", type=caltrop_Schedule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateExpression9: BinaryAssociation = BinaryAssociation(
    name="updateExpression9",
    ends={
        Property(name="caltrop_XExpression", type=caltrop_StateVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_StateVariable10", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="caltrop_StateVariable", type=caltrop_CaltropActorImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_CaltropActorImpl", type=caltrop_StateVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions1: BinaryAssociation = BinaryAssociation(
    name="actions1",
    ends={
        Property(name="caltrop_ReAction", type=caltrop_CaltropActorImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_CaltropActorImpl2", type=caltrop_ReAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initActions3: BinaryAssociation = BinaryAssociation(
    name="initActions3",
    ends={
        Property(name="caltrop_OutputAction", type=caltrop_CaltropActorImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_CaltropActorImpl4", type=caltrop_OutputAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions5: BinaryAssociation = BinaryAssociation(
    name="functions5",
    ends={
        Property(name="caltrop_FunctionDeclaration", type=caltrop_CaltropActorImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_CaltropActorImpl6", type=caltrop_FunctionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardExpression14: BinaryAssociation = BinaryAssociation(
    name="guardExpression14",
    ends={
        Property(name="caltrop_XExpression16", type=caltrop_OutputAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputAction15", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputPatterns17: BinaryAssociation = BinaryAssociation(
    name="outputPatterns17",
    ends={
        Property(name="caltrop_OutputPattern", type=caltrop_OutputAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputAction18", type=caltrop_OutputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression19: BinaryAssociation = BinaryAssociation(
    name="bodyExpression19",
    ends={
        Property(name="caltrop_XExpression21", type=caltrop_OutputAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputAction20", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateExpression22: BinaryAssociation = BinaryAssociation(
    name="updateExpression22",
    ends={
        Property(name="caltrop_XExpression24", type=caltrop_OutputAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputAction23", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delayExpression25: BinaryAssociation = BinaryAssociation(
    name="delayExpression25",
    ends={
        Property(name="caltrop_XExpression27", type=caltrop_OutputAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputAction26", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeatExpression28: BinaryAssociation = BinaryAssociation(
    name="repeatExpression28",
    ends={
        Property(name="caltrop_XExpression29", type=caltrop_PortPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_PortPattern", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
realm11: BinaryAssociation = BinaryAssociation(
    name="realm11",
    ends={
        Property(name="caltrop_Realm", type=caltrop_StateVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_StateVariable12", type=caltrop_Realm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputPatterns13: BinaryAssociation = BinaryAssociation(
    name="inputPatterns13",
    ends={
        Property(name="caltrop_InputPattern", type=caltrop_FireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_FireAction", type=caltrop_InputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueExpressions37: BinaryAssociation = BinaryAssociation(
    name="valueExpressions37",
    ends={
        Property(name="caltrop_XExpression39", type=caltrop_OutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_OutputPattern38", type=caltrop_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyExpressions40: BinaryAssociation = BinaryAssociation(
    name="keyExpressions40",
    ends={
        Property(name="caltrop_XExpression41", type=caltrop_ExpressionChannelSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_ExpressionChannelSelector", type=caltrop_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channels30: BinaryAssociation = BinaryAssociation(
    name="channels30",
    ends={
        Property(name="caltrop_ChannelSelector", type=caltrop_PortPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_PortPattern31", type=caltrop_ChannelSelector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portRef32: BinaryAssociation = BinaryAssociation(
    name="portRef32",
    ends={
        Property(name="caltrop_Port", type=caltrop_PortPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_PortPattern33", type=caltrop_Port, multiplicity=Multiplicity(0, 1))
    }
)
guardExpression34: BinaryAssociation = BinaryAssociation(
    name="guardExpression34",
    ends={
        Property(name="caltrop_XExpression36", type=caltrop_PortPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_PortPattern35", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwables47: BinaryAssociation = BinaryAssociation(
    name="throwables47",
    ends={
        Property(name="caltrop_JvmTypeReference", type=caltrop_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_FunctionDeclaration48", type=caltrop_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial49: BinaryAssociation = BinaryAssociation(
    name="initial49",
    ends={
        Property(name="caltrop_State", type=caltrop_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_Schedule50", type=caltrop_State, multiplicity=Multiplicity(0, 1))
    }
)
states51: BinaryAssociation = BinaryAssociation(
    name="states51",
    ends={
        Property(name="State", type=caltrop_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="schedule", type=caltrop_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions52: BinaryAssociation = BinaryAssociation(
    name="transitions52",
    ends={
        Property(name="Transition", type=caltrop_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=caltrop_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedule53: BinaryAssociation = BinaryAssociation(
    name="schedule53",
    ends={
        Property(name="Schedule", type=caltrop_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=caltrop_Schedule, multiplicity=Multiplicity(0, 1))
    }
)
parameters42: BinaryAssociation = BinaryAssociation(
    name="parameters42",
    ends={
        Property(name="caltrop_JvmTypedObj", type=caltrop_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_FunctionDeclaration43", type=caltrop_JvmTypedObj, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression44: BinaryAssociation = BinaryAssociation(
    name="bodyExpression44",
    ends={
        Property(name="caltrop_XExpression46", type=caltrop_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_FunctionDeclaration45", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventPatterns61: BinaryAssociation = BinaryAssociation(
    name="eventPatterns61",
    ends={
        Property(name="caltrop_EventPattern", type=caltrop_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_EventAction", type=caltrop_EventPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varRef62: BinaryAssociation = BinaryAssociation(
    name="varRef62",
    ends={
        Property(name="caltrop_StateVariable64", type=caltrop_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_EventPattern63", type=caltrop_StateVariable, multiplicity=Multiplicity(0, 1))
    }
)
timeExpression65: BinaryAssociation = BinaryAssociation(
    name="timeExpression65",
    ends={
        Property(name="caltrop_XExpression67", type=caltrop_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_EventPattern66", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source54: BinaryAssociation = BinaryAssociation(
    name="source54",
    ends={
        Property(name="State55", type=caltrop_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=caltrop_State, multiplicity=Multiplicity(0, 1))
    }
)
target56: BinaryAssociation = BinaryAssociation(
    name="target56",
    ends={
        Property(name="caltrop_State57", type=caltrop_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_Transition", type=caltrop_State, multiplicity=Multiplicity(0, 1))
    }
)
actions58: BinaryAssociation = BinaryAssociation(
    name="actions58",
    ends={
        Property(name="caltrop_OutputAction60", type=caltrop_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_Transition59", type=caltrop_OutputAction, multiplicity=Multiplicity(0, 9999))
    }
)
guardExpression68: BinaryAssociation = BinaryAssociation(
    name="guardExpression68",
    ends={
        Property(name="caltrop_XExpression70", type=caltrop_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_EventPattern69", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conversionExpression71: BinaryAssociation = BinaryAssociation(
    name="conversionExpression71",
    ends={
        Property(name="caltrop_XExpression72", type=caltrop_ConversionRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_ConversionRelation", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guardExpression73: BinaryAssociation = BinaryAssociation(
    name="guardExpression73",
    ends={
        Property(name="caltrop_XExpression75", type=caltrop_ConversionRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="caltrop_ConversionRelation74", type=caltrop_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_caltrop_ActorParameter_Parameter = Generalization(general=Parameter_, specific=caltrop_ActorParameter)
gen_caltrop_TypedInputPort_AbstractTypedIOPort = Generalization(general=AbstractTypedIOPort, specific=caltrop_TypedInputPort)
gen_caltrop_TypedOutputPort_AbstractTypedIOPort = Generalization(general=AbstractTypedIOPort, specific=caltrop_TypedOutputPort)
gen_caltrop_StateVariable_Variable = Generalization(general=Variable, specific=caltrop_StateVariable)
gen_caltrop_FireAction_ReAction = Generalization(general=ReAction, specific=caltrop_FireAction)
gen_caltrop_ReAction_OutputAction = Generalization(general=OutputAction, specific=caltrop_ReAction)
gen_caltrop_OutputAction_NamedObj = Generalization(general=NamedObj, specific=caltrop_OutputAction)
gen_caltrop_InputPattern_PortPattern = Generalization(general=PortPattern, specific=caltrop_InputPattern)
gen_caltrop_InputPattern_ActionPattern = Generalization(general=ActionPattern, specific=caltrop_InputPattern)
gen_caltrop_OutputPattern_PortPattern = Generalization(general=PortPattern, specific=caltrop_OutputPattern)
gen_caltrop_ExpressionChannelSelector_ChannelSelector = Generalization(general=ChannelSelector, specific=caltrop_ExpressionChannelSelector)
gen_caltrop_State_NamedObj = Generalization(general=NamedObj, specific=caltrop_State)
gen_caltrop_KeywordChannelSelector_ChannelSelector = Generalization(general=ChannelSelector, specific=caltrop_KeywordChannelSelector)
gen_caltrop_FunctionDeclaration_JvmTypedObj = Generalization(general=JvmTypedObj, specific=caltrop_FunctionDeclaration)
gen_caltrop_EventPattern_ActionPattern = Generalization(general=ActionPattern, specific=caltrop_EventPattern)
gen_caltrop_EventAction_ReAction = Generalization(general=ReAction, specific=caltrop_EventAction)
gen_caltrop_ConversionRelation_Relation = Generalization(general=Relation, specific=caltrop_ConversionRelation)

# Domain Model
domain_model = DomainModel(
    name="caltrop",
    types={caltrop_Schedule, caltrop_ActorParameter, Parameter_, caltrop_TypedInputPort, AbstractTypedIOPort, caltrop_TypedOutputPort, Variable, caltrop_XExpression, caltrop_Realm, caltrop_CaltropActorImpl, caltrop_StateVariable, caltrop_ReAction, caltrop_OutputAction, caltrop_FunctionDeclaration, caltrop_OutputPattern, caltrop_PortPattern, caltrop_FireAction, ReAction, caltrop_InputPattern, OutputAction, NamedObj, ActionPattern, caltrop_ExpressionChannelSelector, ChannelSelector, caltrop_KeywordChannelSelector, caltrop_ChannelSelector, caltrop_Port, caltrop_ActionPattern, PortPattern, caltrop_JvmTypeReference, caltrop_State, caltrop_Transition, JvmTypedObj, caltrop_JvmTypedObj, caltrop_EventPattern, caltrop_EventAction, caltrop_ConversionRelation, Relation, ChannelSelectorKeyword},
    associations={schedule7, updateExpression9, declarations0, actions1, initActions3, functions5, guardExpression14, outputPatterns17, bodyExpression19, updateExpression22, delayExpression25, repeatExpression28, realm11, inputPatterns13, valueExpressions37, keyExpressions40, channels30, portRef32, guardExpression34, throwables47, initial49, states51, transitions52, schedule53, parameters42, bodyExpression44, eventPatterns61, varRef62, timeExpression65, source54, target56, actions58, guardExpression68, conversionExpression71, guardExpression73},
    generalizations={gen_caltrop_ActorParameter_Parameter, gen_caltrop_TypedInputPort_AbstractTypedIOPort, gen_caltrop_TypedOutputPort_AbstractTypedIOPort, gen_caltrop_StateVariable_Variable, gen_caltrop_FireAction_ReAction, gen_caltrop_ReAction_OutputAction, gen_caltrop_OutputAction_NamedObj, gen_caltrop_InputPattern_PortPattern, gen_caltrop_InputPattern_ActionPattern, gen_caltrop_OutputPattern_PortPattern, gen_caltrop_ExpressionChannelSelector_ChannelSelector, gen_caltrop_State_NamedObj, gen_caltrop_KeywordChannelSelector_ChannelSelector, gen_caltrop_FunctionDeclaration_JvmTypedObj, gen_caltrop_EventPattern_ActionPattern, gen_caltrop_EventAction_ReAction, gen_caltrop_ConversionRelation_Relation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)