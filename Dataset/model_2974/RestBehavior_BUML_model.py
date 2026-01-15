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
restbehavior_BehaviorSpecification = Class(name="restbehavior::BehaviorSpecification")
restbehavior_Action = Class(name="restbehavior::Action", is_abstract=True)
restbehavior_Creator = Class(name="restbehavior::Creator")
restbehavior_MediaType = Class(name="restbehavior::MediaType")
restbehavior_Parameter = Class(name="restbehavior::Parameter")
restbehavior_Method = Class(name="restbehavior::Method")
restbehavior_Trigger = Class(name="restbehavior::Trigger", is_abstract=True)
restbehavior_State = Class(name="restbehavior::State")
restbehavior_Transition = Class(name="restbehavior::Transition")
Trigger = Class(name="Trigger")
restbehavior_MessageAction = Class(name="restbehavior::MessageAction")
Action = Class(name="Action")
restbehavior_Condition = Class(name="restbehavior::Condition")
restbehavior_Value = Class(name="restbehavior::Value", is_abstract=True)
restbehavior_InternalMessage = Class(name="restbehavior::InternalMessage")
restbehavior_ListAddAction = Class(name="restbehavior::ListAddAction")
restbehavior_ListRemoveAction = Class(name="restbehavior::ListRemoveAction")
restbehavior_ActionSequence = Class(name="restbehavior::ActionSequence")
restbehavior_ConditionalAction = Class(name="restbehavior::ConditionalAction")
restbehavior_CreateAction = Class(name="restbehavior::CreateAction")
restbehavior_Metadata = Class(name="restbehavior::Metadata")
restbehavior_Representation = Class(name="restbehavior::Representation")
restbehavior_UpdateAction = Class(name="restbehavior::UpdateAction")
restbehavior_WritableReference = Class(name="restbehavior::WritableReference", is_abstract=True)
restbehavior_ReturnAction = Class(name="restbehavior::ReturnAction")
restbehavior_StatusCode = Class(name="restbehavior::StatusCode")
restbehavior_BinOpType = Class(name="restbehavior::BinOpType")
restbehavior_Constant = Class(name="restbehavior::Constant")
Value = Class(name="Value")
restbehavior_DataType = Class(name="restbehavior::DataType")
restbehavior_Reference = Class(name="restbehavior::Reference", is_abstract=True)
restbehavior_Operation = Class(name="restbehavior::Operation", is_abstract=True)
restbehavior_BinaryOperation = Class(name="restbehavior::BinaryOperation")
Operation = Class(name="Operation")
restbehavior_AttributeReference = Class(name="restbehavior::AttributeReference")
WritableReference = Class(name="WritableReference")
restbehavior_Attribute = Class(name="restbehavior::Attribute")
restbehavior_InternalLinkReference = Class(name="restbehavior::InternalLinkReference")
restbehavior_InternalLink = Class(name="restbehavior::InternalLink")
restbehavior_OpType = Class(name="restbehavior::OpType", is_abstract=True)
OpType = Class(name="OpType")
restbehavior_MediaTypeElement = Class(name="restbehavior::MediaTypeElement")
restbehavior_DeletedState = Class(name="restbehavior::DeletedState")
State = Class(name="State")
restbehavior_ExternalLinkReference = Class(name="restbehavior::ExternalLinkReference")
Reference = Class(name="Reference")
restbehavior_MTReference = Class(name="restbehavior::MTReference", is_abstract=True)
restbehavior_MTLinkReference = Class(name="restbehavior::MTLinkReference")
MTReference = Class(name="MTReference")
restbehavior_MediaTypeLink = Class(name="restbehavior::MediaTypeLink")
restbehavior_MtElementReference = Class(name="restbehavior::MtElementReference")
restbehavior_ExternalLink = Class(name="restbehavior::ExternalLink")

# restbehavior_BehaviorSpecification class attributes and methods

# restbehavior_Action class attributes and methods

# restbehavior_Creator class attributes and methods

# restbehavior_MediaType class attributes and methods

# restbehavior_Parameter class attributes and methods

# restbehavior_Method class attributes and methods

# restbehavior_Trigger class attributes and methods

# restbehavior_State class attributes and methods
restbehavior_State_name: Property = Property(name="name", type=StringType)
restbehavior_State.attributes={restbehavior_State_name}

# restbehavior_Transition class attributes and methods

# Trigger class attributes and methods

# restbehavior_MessageAction class attributes and methods

# Action class attributes and methods

# restbehavior_Condition class attributes and methods

# restbehavior_Value class attributes and methods

# restbehavior_InternalMessage class attributes and methods
restbehavior_InternalMessage_name: Property = Property(name="name", type=StringType)
restbehavior_InternalMessage.attributes={restbehavior_InternalMessage_name}

# restbehavior_ListAddAction class attributes and methods

# restbehavior_ListRemoveAction class attributes and methods

# restbehavior_ActionSequence class attributes and methods

# restbehavior_ConditionalAction class attributes and methods

# restbehavior_CreateAction class attributes and methods

# restbehavior_Metadata class attributes and methods

# restbehavior_Representation class attributes and methods

# restbehavior_UpdateAction class attributes and methods

# restbehavior_WritableReference class attributes and methods

# restbehavior_ReturnAction class attributes and methods

# restbehavior_StatusCode class attributes and methods
restbehavior_StatusCode_number: Property = Property(name="number", type=IntegerType)
restbehavior_StatusCode.attributes={restbehavior_StatusCode_number}

# restbehavior_BinOpType class attributes and methods

# restbehavior_Constant class attributes and methods
restbehavior_Constant_stringRepresentation: Property = Property(name="stringRepresentation", type=StringType)
restbehavior_Constant.attributes={restbehavior_Constant_stringRepresentation}

# Value class attributes and methods

# restbehavior_DataType class attributes and methods

# restbehavior_Reference class attributes and methods

# restbehavior_Operation class attributes and methods

# restbehavior_BinaryOperation class attributes and methods

# Operation class attributes and methods

# restbehavior_AttributeReference class attributes and methods

# WritableReference class attributes and methods

# restbehavior_Attribute class attributes and methods

# restbehavior_InternalLinkReference class attributes and methods

# restbehavior_InternalLink class attributes and methods

# restbehavior_OpType class attributes and methods
restbehavior_OpType_name: Property = Property(name="name", type=StringType)
restbehavior_OpType.attributes={restbehavior_OpType_name}

# OpType class attributes and methods

# restbehavior_MediaTypeElement class attributes and methods

# restbehavior_DeletedState class attributes and methods

# State class attributes and methods

# restbehavior_ExternalLinkReference class attributes and methods

# Reference class attributes and methods

# restbehavior_MTReference class attributes and methods

# restbehavior_MTLinkReference class attributes and methods

# MTReference class attributes and methods

# restbehavior_MediaTypeLink class attributes and methods

# restbehavior_MtElementReference class attributes and methods

# restbehavior_ExternalLink class attributes and methods

# Relationships
createbehavior3: BinaryAssociation = BinaryAssociation(
    name="createbehavior3",
    ends={
        Property(name="restbehavior_BehaviorSpecification", type=restbehavior_Creator, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Creator4", type=restbehavior_BehaviorSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action5: BinaryAssociation = BinaryAssociation(
    name="action5",
    ends={
        Property(name="restbehavior_Action", type=restbehavior_BehaviorSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BehaviorSpecification6", type=restbehavior_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consumedMT0: BinaryAssociation = BinaryAssociation(
    name="consumedMT0",
    ends={
        Property(name="restbehavior_MediaType", type=restbehavior_Creator, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Creator", type=restbehavior_MediaType, multiplicity=Multiplicity(1, 9999))
    }
)
creatorParams1: BinaryAssociation = BinaryAssociation(
    name="creatorParams1",
    ends={
        Property(name="restbehavior_Parameter", type=restbehavior_Creator, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Creator2", type=restbehavior_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportedMethods14: BinaryAssociation = BinaryAssociation(
    name="supportedMethods14",
    ends={
        Property(name="restbehavior_Method", type=restbehavior_State, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_State15", type=restbehavior_Method, multiplicity=Multiplicity(0, 9999))
    }
)
trigger16: BinaryAssociation = BinaryAssociation(
    name="trigger16",
    ends={
        Property(name="restbehavior_Trigger", type=restbehavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Transition17", type=restbehavior_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entering7: BinaryAssociation = BinaryAssociation(
    name="entering7",
    ends={
        Property(name="restbehavior_BehaviorSpecification8", type=restbehavior_State, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_State", type=restbehavior_BehaviorSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leaving9: BinaryAssociation = BinaryAssociation(
    name="leaving9",
    ends={
        Property(name="restbehavior_BehaviorSpecification11", type=restbehavior_State, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_State10", type=restbehavior_BehaviorSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions12: BinaryAssociation = BinaryAssociation(
    name="transitions12",
    ends={
        Property(name="restbehavior_Transition", type=restbehavior_State, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_State13", type=restbehavior_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message28: BinaryAssociation = BinaryAssociation(
    name="message28",
    ends={
        Property(name="restbehavior_InternalMessage", type=restbehavior_MessageAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_MessageAction", type=restbehavior_InternalMessage, multiplicity=Multiplicity(1, 1))
    }
)
targetState18: BinaryAssociation = BinaryAssociation(
    name="targetState18",
    ends={
        Property(name="restbehavior_State20", type=restbehavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Transition19", type=restbehavior_State, multiplicity=Multiplicity(1, 1))
    }
)
condition21: BinaryAssociation = BinaryAssociation(
    name="condition21",
    ends={
        Property(name="restbehavior_Condition", type=restbehavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Transition22", type=restbehavior_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect23: BinaryAssociation = BinaryAssociation(
    name="effect23",
    ends={
        Property(name="restbehavior_BehaviorSpecification25", type=restbehavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Transition24", type=restbehavior_BehaviorSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionExpr26: BinaryAssociation = BinaryAssociation(
    name="conditionExpr26",
    ends={
        Property(name="restbehavior_Value", type=restbehavior_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Condition27", type=restbehavior_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actionelements39: BinaryAssociation = BinaryAssociation(
    name="actionelements39",
    ends={
        Property(name="restbehavior_Action40", type=restbehavior_ActionSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ActionSequence", type=restbehavior_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actionCondition29: BinaryAssociation = BinaryAssociation(
    name="actionCondition29",
    ends={
        Property(name="restbehavior_Condition30", type=restbehavior_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ConditionalAction", type=restbehavior_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actionIfTrue31: BinaryAssociation = BinaryAssociation(
    name="actionIfTrue31",
    ends={
        Property(name="restbehavior_Action33", type=restbehavior_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ConditionalAction32", type=restbehavior_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionIfFalse34: BinaryAssociation = BinaryAssociation(
    name="actionIfFalse34",
    ends={
        Property(name="restbehavior_Action36", type=restbehavior_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ConditionalAction35", type=restbehavior_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creator37: BinaryAssociation = BinaryAssociation(
    name="creator37",
    ends={
        Property(name="restbehavior_Creator38", type=restbehavior_CreateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_CreateAction", type=restbehavior_Creator, multiplicity=Multiplicity(0, 1))
    }
)
metadata46: BinaryAssociation = BinaryAssociation(
    name="metadata46",
    ends={
        Property(name="restbehavior_Metadata", type=restbehavior_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ReturnAction47", type=restbehavior_Metadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representation48: BinaryAssociation = BinaryAssociation(
    name="representation48",
    ends={
        Property(name="restbehavior_Representation", type=restbehavior_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ReturnAction49", type=restbehavior_Representation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementForUpdate41: BinaryAssociation = BinaryAssociation(
    name="elementForUpdate41",
    ends={
        Property(name="restbehavior_WritableReference", type=restbehavior_UpdateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_UpdateAction", type=restbehavior_WritableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newValue42: BinaryAssociation = BinaryAssociation(
    name="newValue42",
    ends={
        Property(name="restbehavior_Value44", type=restbehavior_UpdateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_UpdateAction43", type=restbehavior_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
status45: BinaryAssociation = BinaryAssociation(
    name="status45",
    ends={
        Property(name="restbehavior_StatusCode", type=restbehavior_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ReturnAction", type=restbehavior_StatusCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstOp51: BinaryAssociation = BinaryAssociation(
    name="firstOp51",
    ends={
        Property(name="restbehavior_Value52", type=restbehavior_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BinaryOperation", type=restbehavior_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
secondOp53: BinaryAssociation = BinaryAssociation(
    name="secondOp53",
    ends={
        Property(name="restbehavior_Value55", type=restbehavior_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BinaryOperation54", type=restbehavior_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="restbehavior_DataType", type=restbehavior_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_Constant", type=restbehavior_DataType, multiplicity=Multiplicity(1, 1))
    }
)
referencedAttribute66: BinaryAssociation = BinaryAssociation(
    name="referencedAttribute66",
    ends={
        Property(name="restbehavior_Attribute", type=restbehavior_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_AttributeReference", type=restbehavior_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
optype56: BinaryAssociation = BinaryAssociation(
    name="optype56",
    ends={
        Property(name="restbehavior_BinOpType", type=restbehavior_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BinaryOperation57", type=restbehavior_BinOpType, multiplicity=Multiplicity(1, 1))
    }
)
resultType58: BinaryAssociation = BinaryAssociation(
    name="resultType58",
    ends={
        Property(name="restbehavior_DataType59", type=restbehavior_OpType, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_OpType", type=restbehavior_DataType, multiplicity=Multiplicity(1, 1))
    }
)
firstOpType60: BinaryAssociation = BinaryAssociation(
    name="firstOpType60",
    ends={
        Property(name="restbehavior_DataType62", type=restbehavior_BinOpType, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BinOpType61", type=restbehavior_DataType, multiplicity=Multiplicity(1, 1))
    }
)
secondOpType63: BinaryAssociation = BinaryAssociation(
    name="secondOpType63",
    ends={
        Property(name="restbehavior_DataType65", type=restbehavior_BinOpType, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_BinOpType64", type=restbehavior_DataType, multiplicity=Multiplicity(1, 1))
    }
)
referencedMTElement72: BinaryAssociation = BinaryAssociation(
    name="referencedMTElement72",
    ends={
        Property(name="restbehavior_MediaTypeElement", type=restbehavior_MtElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_MtElementReference", type=restbehavior_MediaTypeElement, multiplicity=Multiplicity(1, 1))
    }
)
referencedLink67: BinaryAssociation = BinaryAssociation(
    name="referencedLink67",
    ends={
        Property(name="restbehavior_InternalLink", type=restbehavior_InternalLinkReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_InternalLinkReference", type=restbehavior_InternalLink, multiplicity=Multiplicity(1, 1))
    }
)
referencedReference68: BinaryAssociation = BinaryAssociation(
    name="referencedReference68",
    ends={
        Property(name="restbehavior_WritableReference70", type=restbehavior_InternalLinkReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_InternalLinkReference69", type=restbehavior_WritableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedMTLink71: BinaryAssociation = BinaryAssociation(
    name="referencedMTLink71",
    ends={
        Property(name="restbehavior_MediaTypeLink", type=restbehavior_MTLinkReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_MTLinkReference", type=restbehavior_MediaTypeLink, multiplicity=Multiplicity(1, 1))
    }
)
referencedExternalLink73: BinaryAssociation = BinaryAssociation(
    name="referencedExternalLink73",
    ends={
        Property(name="restbehavior_ExternalLink", type=restbehavior_ExternalLinkReference, multiplicity=Multiplicity(1, 1)),
        Property(name="restbehavior_ExternalLinkReference", type=restbehavior_ExternalLink, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_restbehavior_InternalMessage_Trigger = Generalization(general=Trigger, specific=restbehavior_InternalMessage)
gen_restbehavior_MessageAction_Action = Generalization(general=Action, specific=restbehavior_MessageAction)
gen_restbehavior_ListAddAction_Action = Generalization(general=Action, specific=restbehavior_ListAddAction)
gen_restbehavior_ListRemoveAction_Action = Generalization(general=Action, specific=restbehavior_ListRemoveAction)
gen_restbehavior_ActionSequence_Action = Generalization(general=Action, specific=restbehavior_ActionSequence)
gen_restbehavior_ConditionalAction_Action = Generalization(general=Action, specific=restbehavior_ConditionalAction)
gen_restbehavior_CreateAction_Action = Generalization(general=Action, specific=restbehavior_CreateAction)
gen_restbehavior_UpdateAction_Action = Generalization(general=Action, specific=restbehavior_UpdateAction)
gen_restbehavior_ReturnAction_Action = Generalization(general=Action, specific=restbehavior_ReturnAction)
gen_restbehavior_Constant_Value = Generalization(general=Value, specific=restbehavior_Constant)
gen_restbehavior_Reference_Value = Generalization(general=Value, specific=restbehavior_Reference)
gen_restbehavior_Operation_Value = Generalization(general=Value, specific=restbehavior_Operation)
gen_restbehavior_BinaryOperation_Operation = Generalization(general=Operation, specific=restbehavior_BinaryOperation)
gen_restbehavior_AttributeReference_WritableReference = Generalization(general=WritableReference, specific=restbehavior_AttributeReference)
gen_restbehavior_InternalLinkReference_WritableReference = Generalization(general=WritableReference, specific=restbehavior_InternalLinkReference)
gen_restbehavior_BinOpType_OpType = Generalization(general=OpType, specific=restbehavior_BinOpType)
gen_restbehavior_DeletedState_State = Generalization(general=State, specific=restbehavior_DeletedState)
gen_restbehavior_ExternalLinkReference_WritableReference = Generalization(general=WritableReference, specific=restbehavior_ExternalLinkReference)
gen_restbehavior_WritableReference_Reference = Generalization(general=Reference, specific=restbehavior_WritableReference)
gen_restbehavior_MTReference_Reference = Generalization(general=Reference, specific=restbehavior_MTReference)
gen_restbehavior_MTLinkReference_MTReference = Generalization(general=MTReference, specific=restbehavior_MTLinkReference)
gen_restbehavior_MtElementReference_MTReference = Generalization(general=MTReference, specific=restbehavior_MtElementReference)

# Domain Model
domain_model = DomainModel(
    name="restbehavior",
    types={restbehavior_BehaviorSpecification, restbehavior_Action, restbehavior_Creator, restbehavior_MediaType, restbehavior_Parameter, restbehavior_Method, restbehavior_Trigger, restbehavior_State, restbehavior_Transition, Trigger, restbehavior_MessageAction, Action, restbehavior_Condition, restbehavior_Value, restbehavior_InternalMessage, restbehavior_ListAddAction, restbehavior_ListRemoveAction, restbehavior_ActionSequence, restbehavior_ConditionalAction, restbehavior_CreateAction, restbehavior_Metadata, restbehavior_Representation, restbehavior_UpdateAction, restbehavior_WritableReference, restbehavior_ReturnAction, restbehavior_StatusCode, restbehavior_BinOpType, restbehavior_Constant, Value, restbehavior_DataType, restbehavior_Reference, restbehavior_Operation, restbehavior_BinaryOperation, Operation, restbehavior_AttributeReference, WritableReference, restbehavior_Attribute, restbehavior_InternalLinkReference, restbehavior_InternalLink, restbehavior_OpType, OpType, restbehavior_MediaTypeElement, restbehavior_DeletedState, State, restbehavior_ExternalLinkReference, Reference, restbehavior_MTReference, restbehavior_MTLinkReference, MTReference, restbehavior_MediaTypeLink, restbehavior_MtElementReference, restbehavior_ExternalLink},
    associations={createbehavior3, action5, consumedMT0, creatorParams1, supportedMethods14, trigger16, entering7, leaving9, transitions12, message28, targetState18, condition21, effect23, conditionExpr26, actionelements39, actionCondition29, actionIfTrue31, actionIfFalse34, creator37, metadata46, representation48, elementForUpdate41, newValue42, status45, firstOp51, secondOp53, type50, referencedAttribute66, optype56, resultType58, firstOpType60, secondOpType63, referencedMTElement72, referencedLink67, referencedReference68, referencedMTLink71, referencedExternalLink73},
    generalizations={gen_restbehavior_InternalMessage_Trigger, gen_restbehavior_MessageAction_Action, gen_restbehavior_ListAddAction_Action, gen_restbehavior_ListRemoveAction_Action, gen_restbehavior_ActionSequence_Action, gen_restbehavior_ConditionalAction_Action, gen_restbehavior_CreateAction_Action, gen_restbehavior_UpdateAction_Action, gen_restbehavior_ReturnAction_Action, gen_restbehavior_Constant_Value, gen_restbehavior_Reference_Value, gen_restbehavior_Operation_Value, gen_restbehavior_BinaryOperation_Operation, gen_restbehavior_AttributeReference_WritableReference, gen_restbehavior_InternalLinkReference_WritableReference, gen_restbehavior_BinOpType_OpType, gen_restbehavior_DeletedState_State, gen_restbehavior_ExternalLinkReference_WritableReference, gen_restbehavior_WritableReference_Reference, gen_restbehavior_MTReference_Reference, gen_restbehavior_MTLinkReference_MTReference, gen_restbehavior_MtElementReference_MTReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)