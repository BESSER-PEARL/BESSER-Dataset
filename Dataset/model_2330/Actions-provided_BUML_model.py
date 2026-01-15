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
ActionsProv_OutputPin = Class(name="ActionsProv::OutputPin")
ActionsProv_Action = Class(name="ActionsProv::Action", is_abstract=True)
ActionsProv_InputPin = Class(name="ActionsProv::InputPin")
ActionsProv_OpaqueAction = Class(name="ActionsProv::OpaqueAction")
Action = Class(name="Action")
Pin = Class(name="Pin")
ActionsProv_Pin = Class(name="ActionsProv::Pin", is_abstract=True)
ActionsProv_ValuePin = Class(name="ActionsProv::ValuePin")
InputPin = Class(name="InputPin")
ActionsProv_InvocationAction = Class(name="ActionsProv::InvocationAction", is_abstract=True)
ActionsProv_CallAction = Class(name="ActionsProv::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
ActionsProv_CallBehaviorAction = Class(name="ActionsProv::CallBehaviorAction")
CallAction = Class(name="CallAction")
ActionsProv_CallOperationAction = Class(name="ActionsProv::CallOperationAction")
ActionsProv_SendSignalAction = Class(name="ActionsProv::SendSignalAction")
ActionsProv_BroadcastSignalAction = Class(name="ActionsProv::BroadcastSignalAction")
ActionsProv_SendObjectAction = Class(name="ActionsProv::SendObjectAction")
ActionsProv_CreateObjectAction = Class(name="ActionsProv::CreateObjectAction")
ActionsProv_DestroyObjectAction = Class(name="ActionsProv::DestroyObjectAction")
ActionsProv_TestIdentityAction = Class(name="ActionsProv::TestIdentityAction")
ActionsProv_ReadSelfAction = Class(name="ActionsProv::ReadSelfAction")
ActionsProv_ValueSpecificationAction = Class(name="ActionsProv::ValueSpecificationAction")
ActionsProv_StructuralFeatureAction = Class(name="ActionsProv::StructuralFeatureAction", is_abstract=True)
ActionsProv_ReadStructuralFeatureAction = Class(name="ActionsProv::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
ActionsProv_WriteStructuralFeatureAction = Class(name="ActionsProv::WriteStructuralFeatureAction", is_abstract=True)
ActionsProv_AddStructuralFeatureValueAction = Class(name="ActionsProv::AddStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
ActionsProv_RemoveStructuralFeatureValueAction = Class(name="ActionsProv::RemoveStructuralFeatureValueAction")
ActionsProv_ClearStructuralFeatureAction = Class(name="ActionsProv::ClearStructuralFeatureAction")
ActionsProv_LinkAction = Class(name="ActionsProv::LinkAction")
ActionsProv_LinkEndData = Class(name="ActionsProv::LinkEndData", is_abstract=True)
ActionsProv_QualifierValue = Class(name="ActionsProv::QualifierValue")
ActionsProv_ReadLinkAction = Class(name="ActionsProv::ReadLinkAction")
LinkAction = Class(name="LinkAction")
ActionsProv_WriteLinkAction = Class(name="ActionsProv::WriteLinkAction", is_abstract=True)
ActionsProv_CreateLinkAction = Class(name="ActionsProv::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
ActionsProv_LinkEndCreationData = Class(name="ActionsProv::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
ActionsProv_DestroyLinkAction = Class(name="ActionsProv::DestroyLinkAction")
ActionsProv_LinkEndDestructionData = Class(name="ActionsProv::LinkEndDestructionData")
ActionsProv_ReplyAction = Class(name="ActionsProv::ReplyAction")
ActionsProv_UnmarshallAction = Class(name="ActionsProv::UnmarshallAction")
ActionsProv_AcceptEventAction = Class(name="ActionsProv::AcceptEventAction")
ActionsProv_AcceptCallAction = Class(name="ActionsProv::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
ActionsProv_ReadExtendAction = Class(name="ActionsProv::ReadExtendAction")
ActionsProv_ReclassifyObjectAction = Class(name="ActionsProv::ReclassifyObjectAction")
ActionsProv_ReadlsClassifiedObjectAction = Class(name="ActionsProv::ReadlsClassifiedObjectAction")
ActionsProv_StartClassifierBehaviorAction = Class(name="ActionsProv::StartClassifierBehaviorAction")
ActionsProv_StartObjectBehaviorAction = Class(name="ActionsProv::StartObjectBehaviorAction")
ActionsProv_ReadLinkObjectEndAction = Class(name="ActionsProv::ReadLinkObjectEndAction")
ActionsProv_ReadLinkObjectEndQualifierAction = Class(name="ActionsProv::ReadLinkObjectEndQualifierAction")
ActionsProv_CreateLinkObjectAction = Class(name="ActionsProv::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
ActionsProv_ReduceAction = Class(name="ActionsProv::ReduceAction")
ActionsProv_VariableAction = Class(name="ActionsProv::VariableAction", is_abstract=True)
ActionsProv_ReadVariableAction = Class(name="ActionsProv::ReadVariableAction")
VariableAction = Class(name="VariableAction")
ActionsProv_WriteVariableAction = Class(name="ActionsProv::WriteVariableAction")
ActionsProv_AddVariableValueAction = Class(name="ActionsProv::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
ActionsProv_RemoveVariableValueAction = Class(name="ActionsProv::RemoveVariableValueAction")
ActionsProv_ClearVariableAction = Class(name="ActionsProv::ClearVariableAction")
ActionsProv_RaiseExceptionAction = Class(name="ActionsProv::RaiseExceptionAction")
ActionsProv_ActionInputPin = Class(name="ActionsProv::ActionInputPin")

# ActionsProv_OutputPin class attributes and methods

# ActionsProv_Action class attributes and methods

# ActionsProv_InputPin class attributes and methods

# ActionsProv_OpaqueAction class attributes and methods
ActionsProv_OpaqueAction_body: Property = Property(name="body", type=StringType)
ActionsProv_OpaqueAction_language: Property = Property(name="language", type=StringType)
ActionsProv_OpaqueAction.attributes={ActionsProv_OpaqueAction_body, ActionsProv_OpaqueAction_language}

# Action class attributes and methods

# Pin class attributes and methods

# ActionsProv_Pin class attributes and methods

# ActionsProv_ValuePin class attributes and methods

# InputPin class attributes and methods

# ActionsProv_InvocationAction class attributes and methods

# ActionsProv_CallAction class attributes and methods
ActionsProv_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=BooleanType)
ActionsProv_CallAction.attributes={ActionsProv_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# ActionsProv_CallBehaviorAction class attributes and methods

# CallAction class attributes and methods

# ActionsProv_CallOperationAction class attributes and methods

# ActionsProv_SendSignalAction class attributes and methods

# ActionsProv_BroadcastSignalAction class attributes and methods

# ActionsProv_SendObjectAction class attributes and methods

# ActionsProv_CreateObjectAction class attributes and methods

# ActionsProv_DestroyObjectAction class attributes and methods

# ActionsProv_TestIdentityAction class attributes and methods

# ActionsProv_ReadSelfAction class attributes and methods

# ActionsProv_ValueSpecificationAction class attributes and methods

# ActionsProv_StructuralFeatureAction class attributes and methods

# ActionsProv_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# ActionsProv_WriteStructuralFeatureAction class attributes and methods

# ActionsProv_AddStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# ActionsProv_RemoveStructuralFeatureValueAction class attributes and methods

# ActionsProv_ClearStructuralFeatureAction class attributes and methods

# ActionsProv_LinkAction class attributes and methods

# ActionsProv_LinkEndData class attributes and methods

# ActionsProv_QualifierValue class attributes and methods

# ActionsProv_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# ActionsProv_WriteLinkAction class attributes and methods

# ActionsProv_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# ActionsProv_LinkEndCreationData class attributes and methods
ActionsProv_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
ActionsProv_LinkEndCreationData.attributes={ActionsProv_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# ActionsProv_DestroyLinkAction class attributes and methods

# ActionsProv_LinkEndDestructionData class attributes and methods
ActionsProv_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=BooleanType)
ActionsProv_LinkEndDestructionData.attributes={ActionsProv_LinkEndDestructionData_isDestroyDuplicates}

# ActionsProv_ReplyAction class attributes and methods

# ActionsProv_UnmarshallAction class attributes and methods

# ActionsProv_AcceptEventAction class attributes and methods
ActionsProv_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=BooleanType)
ActionsProv_AcceptEventAction.attributes={ActionsProv_AcceptEventAction_isUnmarshall}

# ActionsProv_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# ActionsProv_ReadExtendAction class attributes and methods

# ActionsProv_ReclassifyObjectAction class attributes and methods
ActionsProv_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
ActionsProv_ReclassifyObjectAction.attributes={ActionsProv_ReclassifyObjectAction_isReplaceAll}

# ActionsProv_ReadlsClassifiedObjectAction class attributes and methods

# ActionsProv_StartClassifierBehaviorAction class attributes and methods

# ActionsProv_StartObjectBehaviorAction class attributes and methods

# ActionsProv_ReadLinkObjectEndAction class attributes and methods

# ActionsProv_ReadLinkObjectEndQualifierAction class attributes and methods

# ActionsProv_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# ActionsProv_ReduceAction class attributes and methods
ActionsProv_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
ActionsProv_ReduceAction.attributes={ActionsProv_ReduceAction_isOrdered}

# ActionsProv_VariableAction class attributes and methods

# ActionsProv_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# ActionsProv_WriteVariableAction class attributes and methods

# ActionsProv_AddVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# ActionsProv_RemoveVariableValueAction class attributes and methods

# ActionsProv_ClearVariableAction class attributes and methods

# ActionsProv_RaiseExceptionAction class attributes and methods

# ActionsProv_ActionInputPin class attributes and methods

# Relationships
input0: BinaryAssociation = BinaryAssociation(
    name="input0",
    ends={
        Property(name="ActionsProv_InputPin", type=ActionsProv_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_Action", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="ActionsProv_InputPin13", type=ActionsProv_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_CallOperationAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
output1: BinaryAssociation = BinaryAssociation(
    name="output1",
    ends={
        Property(name="ActionsProv_OutputPin", type=ActionsProv_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_Action2", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputValue3: BinaryAssociation = BinaryAssociation(
    name="inputValue3",
    ends={
        Property(name="ActionsProv_InputPin4", type=ActionsProv_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_OpaqueAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputValue5: BinaryAssociation = BinaryAssociation(
    name="outputValue5",
    ends={
        Property(name="ActionsProv_OutputPin7", type=ActionsProv_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_OpaqueAction6", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument8: BinaryAssociation = BinaryAssociation(
    name="argument8",
    ends={
        Property(name="ActionsProv_InputPin9", type=ActionsProv_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_InvocationAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result10: BinaryAssociation = BinaryAssociation(
    name="result10",
    ends={
        Property(name="ActionsProv_OutputPin11", type=ActionsProv_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_CallAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="ActionsProv_InputPin15", type=ActionsProv_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_SendSignalAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="ActionsProv_InputPin17", type=ActionsProv_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_SendObjectAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request18: BinaryAssociation = BinaryAssociation(
    name="request18",
    ends={
        Property(name="ActionsProv_InputPin20", type=ActionsProv_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_SendObjectAction19", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result21: BinaryAssociation = BinaryAssociation(
    name="result21",
    ends={
        Property(name="ActionsProv_OutputPin22", type=ActionsProv_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_CreateObjectAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="ActionsProv_InputPin24", type=ActionsProv_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_DestroyObjectAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result25: BinaryAssociation = BinaryAssociation(
    name="result25",
    ends={
        Property(name="ActionsProv_OutputPin26", type=ActionsProv_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_TestIdentityAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first27: BinaryAssociation = BinaryAssociation(
    name="first27",
    ends={
        Property(name="ActionsProv_InputPin29", type=ActionsProv_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_TestIdentityAction28", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second30: BinaryAssociation = BinaryAssociation(
    name="second30",
    ends={
        Property(name="ActionsProv_InputPin32", type=ActionsProv_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_TestIdentityAction31", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result33: BinaryAssociation = BinaryAssociation(
    name="result33",
    ends={
        Property(name="ActionsProv_OutputPin34", type=ActionsProv_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadSelfAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result35: BinaryAssociation = BinaryAssociation(
    name="result35",
    ends={
        Property(name="ActionsProv_OutputPin36", type=ActionsProv_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ValueSpecificationAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object37: BinaryAssociation = BinaryAssociation(
    name="object37",
    ends={
        Property(name="ActionsProv_InputPin38", type=ActionsProv_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_StructuralFeatureAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result39: BinaryAssociation = BinaryAssociation(
    name="result39",
    ends={
        Property(name="ActionsProv_OutputPin40", type=ActionsProv_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadStructuralFeatureAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value41: BinaryAssociation = BinaryAssociation(
    name="value41",
    ends={
        Property(name="ActionsProv_InputPin42", type=ActionsProv_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_WriteStructuralFeatureAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result43: BinaryAssociation = BinaryAssociation(
    name="result43",
    ends={
        Property(name="ActionsProv_OutputPin45", type=ActionsProv_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_WriteStructuralFeatureAction44", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt46: BinaryAssociation = BinaryAssociation(
    name="insertAt46",
    ends={
        Property(name="ActionsProv_InputPin47", type=ActionsProv_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_AddStructuralFeatureValueAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt48: BinaryAssociation = BinaryAssociation(
    name="removeAt48",
    ends={
        Property(name="ActionsProv_InputPin49", type=ActionsProv_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_RemoveStructuralFeatureValueAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result50: BinaryAssociation = BinaryAssociation(
    name="result50",
    ends={
        Property(name="ActionsProv_OutputPin51", type=ActionsProv_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ClearStructuralFeatureAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValue52: BinaryAssociation = BinaryAssociation(
    name="inputValue52",
    ends={
        Property(name="ActionsProv_InputPin53", type=ActionsProv_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
endData54: BinaryAssociation = BinaryAssociation(
    name="endData54",
    ends={
        Property(name="ActionsProv_LinkEndData", type=ActionsProv_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkAction55", type=ActionsProv_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="ActionsProv_InputPin58", type=ActionsProv_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkEndData57", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
qualifier59: BinaryAssociation = BinaryAssociation(
    name="qualifier59",
    ends={
        Property(name="ActionsProv_QualifierValue", type=ActionsProv_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkEndData60", type=ActionsProv_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result61: BinaryAssociation = BinaryAssociation(
    name="result61",
    ends={
        Property(name="ActionsProv_OutputPin62", type=ActionsProv_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadLinkAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt63: BinaryAssociation = BinaryAssociation(
    name="insertAt63",
    ends={
        Property(name="ActionsProv_InputPin64", type=ActionsProv_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkEndCreationData", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destroyAt65: BinaryAssociation = BinaryAssociation(
    name="destroyAt65",
    ends={
        Property(name="ActionsProv_InputPin66", type=ActionsProv_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_LinkEndDestructionData", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnInformation67: BinaryAssociation = BinaryAssociation(
    name="returnInformation67",
    ends={
        Property(name="ActionsProv_InputPin68", type=ActionsProv_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReplyAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue69: BinaryAssociation = BinaryAssociation(
    name="replyValue69",
    ends={
        Property(name="ActionsProv_InputPin71", type=ActionsProv_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReplyAction70", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object72: BinaryAssociation = BinaryAssociation(
    name="object72",
    ends={
        Property(name="ActionsProv_InputPin73", type=ActionsProv_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_UnmarshallAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result74: BinaryAssociation = BinaryAssociation(
    name="result74",
    ends={
        Property(name="ActionsProv_OutputPin76", type=ActionsProv_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_UnmarshallAction75", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result77: BinaryAssociation = BinaryAssociation(
    name="result77",
    ends={
        Property(name="ActionsProv_OutputPin78", type=ActionsProv_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_AcceptEventAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnInformation79: BinaryAssociation = BinaryAssociation(
    name="returnInformation79",
    ends={
        Property(name="ActionsProv_OutputPin80", type=ActionsProv_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_AcceptCallAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result81: BinaryAssociation = BinaryAssociation(
    name="result81",
    ends={
        Property(name="ActionsProv_OutputPin82", type=ActionsProv_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadExtendAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object83: BinaryAssociation = BinaryAssociation(
    name="object83",
    ends={
        Property(name="ActionsProv_InputPin84", type=ActionsProv_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReclassifyObjectAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result85: BinaryAssociation = BinaryAssociation(
    name="result85",
    ends={
        Property(name="ActionsProv_OutputPin86", type=ActionsProv_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadlsClassifiedObjectAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object87: BinaryAssociation = BinaryAssociation(
    name="object87",
    ends={
        Property(name="ActionsProv_InputPin89", type=ActionsProv_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadlsClassifiedObjectAction88", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object90: BinaryAssociation = BinaryAssociation(
    name="object90",
    ends={
        Property(name="ActionsProv_InputPin91", type=ActionsProv_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_StartClassifierBehaviorAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object92: BinaryAssociation = BinaryAssociation(
    name="object92",
    ends={
        Property(name="ActionsProv_InputPin93", type=ActionsProv_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_StartObjectBehaviorAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value94: BinaryAssociation = BinaryAssociation(
    name="value94",
    ends={
        Property(name="ActionsProv_InputPin96", type=ActionsProv_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_QualifierValue95", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
object97: BinaryAssociation = BinaryAssociation(
    name="object97",
    ends={
        Property(name="ActionsProv_InputPin98", type=ActionsProv_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadLinkObjectEndAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result99: BinaryAssociation = BinaryAssociation(
    name="result99",
    ends={
        Property(name="ActionsProv_OutputPin101", type=ActionsProv_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadLinkObjectEndAction100", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result109: BinaryAssociation = BinaryAssociation(
    name="result109",
    ends={
        Property(name="ActionsProv_OutputPin110", type=ActionsProv_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReduceAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object102: BinaryAssociation = BinaryAssociation(
    name="object102",
    ends={
        Property(name="ActionsProv_InputPin103", type=ActionsProv_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadLinkObjectEndQualifierAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result104: BinaryAssociation = BinaryAssociation(
    name="result104",
    ends={
        Property(name="ActionsProv_OutputPin106", type=ActionsProv_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadLinkObjectEndQualifierAction105", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result107: BinaryAssociation = BinaryAssociation(
    name="result107",
    ends={
        Property(name="ActionsProv_OutputPin108", type=ActionsProv_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_CreateLinkObjectAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection111: BinaryAssociation = BinaryAssociation(
    name="collection111",
    ends={
        Property(name="ActionsProv_InputPin113", type=ActionsProv_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReduceAction112", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result114: BinaryAssociation = BinaryAssociation(
    name="result114",
    ends={
        Property(name="ActionsProv_OutputPin115", type=ActionsProv_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ReadVariableAction", type=ActionsProv_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value116: BinaryAssociation = BinaryAssociation(
    name="value116",
    ends={
        Property(name="ActionsProv_InputPin117", type=ActionsProv_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_WriteVariableAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt118: BinaryAssociation = BinaryAssociation(
    name="insertAt118",
    ends={
        Property(name="ActionsProv_InputPin119", type=ActionsProv_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_AddVariableValueAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt120: BinaryAssociation = BinaryAssociation(
    name="removeAt120",
    ends={
        Property(name="ActionsProv_InputPin121", type=ActionsProv_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_RemoveVariableValueAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception122: BinaryAssociation = BinaryAssociation(
    name="exception122",
    ends={
        Property(name="ActionsProv_InputPin123", type=ActionsProv_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_RaiseExceptionAction", type=ActionsProv_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromAction124: BinaryAssociation = BinaryAssociation(
    name="fromAction124",
    ends={
        Property(name="ActionsProv_Action125", type=ActionsProv_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionsProv_ActionInputPin", type=ActionsProv_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ActionsProv_OpaqueAction_Action = Generalization(general=Action, specific=ActionsProv_OpaqueAction)
gen_ActionsProv_InputPin_Pin = Generalization(general=Pin, specific=ActionsProv_InputPin)
gen_ActionsProv_OutputPin_Pin = Generalization(general=Pin, specific=ActionsProv_OutputPin)
gen_ActionsProv_ValuePin_InputPin = Generalization(general=InputPin, specific=ActionsProv_ValuePin)
gen_ActionsProv_InvocationAction_Action = Generalization(general=Action, specific=ActionsProv_InvocationAction)
gen_ActionsProv_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=ActionsProv_CallAction)
gen_ActionsProv_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=ActionsProv_CallBehaviorAction)
gen_ActionsProv_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=ActionsProv_SendSignalAction)
gen_ActionsProv_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=ActionsProv_BroadcastSignalAction)
gen_ActionsProv_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=ActionsProv_SendObjectAction)
gen_ActionsProv_CreateObjectAction_Action = Generalization(general=Action, specific=ActionsProv_CreateObjectAction)
gen_ActionsProv_DestroyObjectAction_Action = Generalization(general=Action, specific=ActionsProv_DestroyObjectAction)
gen_ActionsProv_TestIdentityAction_Action = Generalization(general=Action, specific=ActionsProv_TestIdentityAction)
gen_ActionsProv_ReadSelfAction_Action = Generalization(general=Action, specific=ActionsProv_ReadSelfAction)
gen_ActionsProv_LinkAction_Action = Generalization(general=Action, specific=ActionsProv_LinkAction)
gen_ActionsProv_ValueSpecificationAction_Action = Generalization(general=Action, specific=ActionsProv_ValueSpecificationAction)
gen_ActionsProv_StructuralFeatureAction_Action = Generalization(general=Action, specific=ActionsProv_StructuralFeatureAction)
gen_ActionsProv_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=ActionsProv_ReadStructuralFeatureAction)
gen_ActionsProv_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=ActionsProv_WriteStructuralFeatureAction)
gen_ActionsProv_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=ActionsProv_AddStructuralFeatureValueAction)
gen_ActionsProv_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=ActionsProv_RemoveStructuralFeatureValueAction)
gen_ActionsProv_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=ActionsProv_ClearStructuralFeatureAction)
gen_ActionsProv_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=ActionsProv_ReadLinkAction)
gen_ActionsProv_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=ActionsProv_WriteLinkAction)
gen_ActionsProv_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=ActionsProv_CreateLinkAction)
gen_ActionsProv_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=ActionsProv_LinkEndCreationData)
gen_ActionsProv_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=ActionsProv_DestroyLinkAction)
gen_ActionsProv_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=ActionsProv_LinkEndDestructionData)
gen_ActionsProv_ReplyAction_Action = Generalization(general=Action, specific=ActionsProv_ReplyAction)
gen_ActionsProv_UnmarshallAction_Action = Generalization(general=Action, specific=ActionsProv_UnmarshallAction)
gen_ActionsProv_AcceptEventAction_Action = Generalization(general=Action, specific=ActionsProv_AcceptEventAction)
gen_ActionsProv_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=ActionsProv_AcceptCallAction)
gen_ActionsProv_ReadExtendAction_Action = Generalization(general=Action, specific=ActionsProv_ReadExtendAction)
gen_ActionsProv_ReclassifyObjectAction_Action = Generalization(general=Action, specific=ActionsProv_ReclassifyObjectAction)
gen_ActionsProv_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=ActionsProv_ReadLinkObjectEndQualifierAction)
gen_ActionsProv_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=ActionsProv_StartClassifierBehaviorAction)
gen_ActionsProv_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=ActionsProv_StartObjectBehaviorAction)
gen_ActionsProv_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=ActionsProv_ReadLinkObjectEndAction)
gen_ActionsProv_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=ActionsProv_CreateLinkObjectAction)
gen_ActionsProv_ReduceAction_Action = Generalization(general=Action, specific=ActionsProv_ReduceAction)
gen_ActionsProv_VariableAction_Action = Generalization(general=Action, specific=ActionsProv_VariableAction)
gen_ActionsProv_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=ActionsProv_ReadVariableAction)
gen_ActionsProv_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=ActionsProv_WriteVariableAction)
gen_ActionsProv_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=ActionsProv_AddVariableValueAction)
gen_ActionsProv_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=ActionsProv_RemoveVariableValueAction)
gen_ActionsProv_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=ActionsProv_ClearVariableAction)
gen_ActionsProv_RaiseExceptionAction_Action = Generalization(general=Action, specific=ActionsProv_RaiseExceptionAction)
gen_ActionsProv_ActionInputPin_InputPin = Generalization(general=InputPin, specific=ActionsProv_ActionInputPin)

# Domain Model
domain_model = DomainModel(
    name="ActionsProv",
    types={ActionsProv_OutputPin, ActionsProv_Action, ActionsProv_InputPin, ActionsProv_OpaqueAction, Action, Pin, ActionsProv_Pin, ActionsProv_ValuePin, InputPin, ActionsProv_InvocationAction, ActionsProv_CallAction, InvocationAction, ActionsProv_CallBehaviorAction, CallAction, ActionsProv_CallOperationAction, ActionsProv_SendSignalAction, ActionsProv_BroadcastSignalAction, ActionsProv_SendObjectAction, ActionsProv_CreateObjectAction, ActionsProv_DestroyObjectAction, ActionsProv_TestIdentityAction, ActionsProv_ReadSelfAction, ActionsProv_ValueSpecificationAction, ActionsProv_StructuralFeatureAction, ActionsProv_ReadStructuralFeatureAction, StructuralFeatureAction, ActionsProv_WriteStructuralFeatureAction, ActionsProv_AddStructuralFeatureValueAction, WriteStructuralFeatureAction, ActionsProv_RemoveStructuralFeatureValueAction, ActionsProv_ClearStructuralFeatureAction, ActionsProv_LinkAction, ActionsProv_LinkEndData, ActionsProv_QualifierValue, ActionsProv_ReadLinkAction, LinkAction, ActionsProv_WriteLinkAction, ActionsProv_CreateLinkAction, WriteLinkAction, ActionsProv_LinkEndCreationData, LinkEndData, ActionsProv_DestroyLinkAction, ActionsProv_LinkEndDestructionData, ActionsProv_ReplyAction, ActionsProv_UnmarshallAction, ActionsProv_AcceptEventAction, ActionsProv_AcceptCallAction, AcceptEventAction, ActionsProv_ReadExtendAction, ActionsProv_ReclassifyObjectAction, ActionsProv_ReadlsClassifiedObjectAction, ActionsProv_StartClassifierBehaviorAction, ActionsProv_StartObjectBehaviorAction, ActionsProv_ReadLinkObjectEndAction, ActionsProv_ReadLinkObjectEndQualifierAction, ActionsProv_CreateLinkObjectAction, CreateLinkAction, ActionsProv_ReduceAction, ActionsProv_VariableAction, ActionsProv_ReadVariableAction, VariableAction, ActionsProv_WriteVariableAction, ActionsProv_AddVariableValueAction, WriteVariableAction, ActionsProv_RemoveVariableValueAction, ActionsProv_ClearVariableAction, ActionsProv_RaiseExceptionAction, ActionsProv_ActionInputPin},
    associations={input0, target12, output1, inputValue3, outputValue5, argument8, result10, target14, target16, request18, result21, target23, result25, first27, second30, result33, result35, object37, result39, value41, result43, insertAt46, removeAt48, result50, inputValue52, endData54, value56, qualifier59, result61, insertAt63, destroyAt65, returnInformation67, replyValue69, object72, result74, result77, returnInformation79, result81, object83, result85, object87, object90, object92, value94, object97, result99, result109, object102, result104, result107, collection111, result114, value116, insertAt118, removeAt120, exception122, fromAction124},
    generalizations={gen_ActionsProv_OpaqueAction_Action, gen_ActionsProv_InputPin_Pin, gen_ActionsProv_OutputPin_Pin, gen_ActionsProv_ValuePin_InputPin, gen_ActionsProv_InvocationAction_Action, gen_ActionsProv_CallAction_InvocationAction, gen_ActionsProv_CallBehaviorAction_CallAction, gen_ActionsProv_SendSignalAction_InvocationAction, gen_ActionsProv_BroadcastSignalAction_InvocationAction, gen_ActionsProv_SendObjectAction_InvocationAction, gen_ActionsProv_CreateObjectAction_Action, gen_ActionsProv_DestroyObjectAction_Action, gen_ActionsProv_TestIdentityAction_Action, gen_ActionsProv_ReadSelfAction_Action, gen_ActionsProv_LinkAction_Action, gen_ActionsProv_ValueSpecificationAction_Action, gen_ActionsProv_StructuralFeatureAction_Action, gen_ActionsProv_ReadStructuralFeatureAction_StructuralFeatureAction, gen_ActionsProv_WriteStructuralFeatureAction_StructuralFeatureAction, gen_ActionsProv_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_ActionsProv_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_ActionsProv_ClearStructuralFeatureAction_StructuralFeatureAction, gen_ActionsProv_ReadLinkAction_LinkAction, gen_ActionsProv_WriteLinkAction_LinkAction, gen_ActionsProv_CreateLinkAction_WriteLinkAction, gen_ActionsProv_LinkEndCreationData_LinkEndData, gen_ActionsProv_DestroyLinkAction_WriteLinkAction, gen_ActionsProv_LinkEndDestructionData_LinkEndData, gen_ActionsProv_ReplyAction_Action, gen_ActionsProv_UnmarshallAction_Action, gen_ActionsProv_AcceptEventAction_Action, gen_ActionsProv_AcceptCallAction_AcceptEventAction, gen_ActionsProv_ReadExtendAction_Action, gen_ActionsProv_ReclassifyObjectAction_Action, gen_ActionsProv_ReadLinkObjectEndQualifierAction_Action, gen_ActionsProv_StartClassifierBehaviorAction_Action, gen_ActionsProv_StartObjectBehaviorAction_CallAction, gen_ActionsProv_ReadLinkObjectEndAction_Action, gen_ActionsProv_CreateLinkObjectAction_CreateLinkAction, gen_ActionsProv_ReduceAction_Action, gen_ActionsProv_VariableAction_Action, gen_ActionsProv_ReadVariableAction_VariableAction, gen_ActionsProv_WriteVariableAction_VariableAction, gen_ActionsProv_AddVariableValueAction_WriteVariableAction, gen_ActionsProv_RemoveVariableValueAction_WriteVariableAction, gen_ActionsProv_ClearVariableAction_VariableAction, gen_ActionsProv_RaiseExceptionAction_Action, gen_ActionsProv_ActionInputPin_InputPin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)