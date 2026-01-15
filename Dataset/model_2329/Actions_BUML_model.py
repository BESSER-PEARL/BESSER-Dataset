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
Actions_BasicActions_Action = Class(name="Actions::BasicActions::Action", is_abstract=True)
NamedElement = Class(name="NamedElement")
Classifier = Class(name="Classifier")
InputPin = Class(name="InputPin")
Actions_BasicActions_Classifier = Class(name="Actions::BasicActions::Classifier", is_abstract=True)
Actions_BasicActions_OpaqueAction = Class(name="Actions::BasicActions::OpaqueAction")
Action = Class(name="Action")
Actions_BasicActions_InputPin = Class(name="Actions::BasicActions::InputPin")
Pin = Class(name="Pin")
Actions_BasicActions_OutputPin = Class(name="Actions::BasicActions::OutputPin")
Actions_BasicActions_Pin = Class(name="Actions::BasicActions::Pin", is_abstract=True)
BasicActions_TypedElement = Class(name="BasicActions::TypedElement")
BasicActions_MultiplicityElement = Class(name="BasicActions::MultiplicityElement")
Actions_BasicActions_MultiplicityElement = Class(name="Actions::BasicActions::MultiplicityElement", is_abstract=True)
Actions_BasicActions_TypedElement = Class(name="Actions::BasicActions::TypedElement", is_abstract=True)
Actions_BasicActions_ValuePin = Class(name="Actions::BasicActions::ValuePin")
OutputPin = Class(name="OutputPin")
Actions_BasicActions_NamedElement = Class(name="Actions::BasicActions::NamedElement", is_abstract=True)
Actions_BasicActions_ValueSpecification = Class(name="Actions::BasicActions::ValueSpecification", is_abstract=True)
Actions_BasicActions_InvocationAction = Class(name="Actions::BasicActions::InvocationAction", is_abstract=True)
Actions_BasicActions_CallAction = Class(name="Actions::BasicActions::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
Actions_BasicActions_CallBehaviorAction = Class(name="Actions::BasicActions::CallBehaviorAction")
CallAction = Class(name="CallAction")
Behavior = Class(name="Behavior")
Actions_BasicActions_Behavior = Class(name="Actions::BasicActions::Behavior", is_abstract=True)
Actions_BasicActions_CallOperationAction = Class(name="Actions::BasicActions::CallOperationAction")
Operation = Class(name="Operation")
ValueSpecification = Class(name="ValueSpecification")
Actions_BasicActions_SendSignalAction = Class(name="Actions::BasicActions::SendSignalAction")
Signal = Class(name="Signal")
Actions_BasicActions_Signal = Class(name="Actions::BasicActions::Signal")
Actions_IntermediateActions_BroadcastSignalAction = Class(name="Actions::IntermediateActions::BroadcastSignalAction")
Actions_IntermediateActions_SendObjectAction = Class(name="Actions::IntermediateActions::SendObjectAction")
Actions_IntermediateActions_CreateObjectAction = Class(name="Actions::IntermediateActions::CreateObjectAction")
Actions_BasicActions_Operation = Class(name="Actions::BasicActions::Operation")
Actions_IntermediateActions_TestIdentityAction = Class(name="Actions::IntermediateActions::TestIdentityAction")
Actions_IntermediateActions_ReadSelfAction = Class(name="Actions::IntermediateActions::ReadSelfAction")
Actions_IntermediateActions_ValueSpecificationAction = Class(name="Actions::IntermediateActions::ValueSpecificationAction")
Actions_IntermediateActions_DestroyObjectAction = Class(name="Actions::IntermediateActions::DestroyObjectAction")
Actions_IntermediateActions_StructuralFeature = Class(name="Actions::IntermediateActions::StructuralFeature", is_abstract=True)
Actions_IntermediateActions_ReadStructuralFeatureAction = Class(name="Actions::IntermediateActions::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
Actions_IntermediateActions_WriteStructuralFeatureAction = Class(name="Actions::IntermediateActions::WriteStructuralFeatureAction", is_abstract=True)
Actions_IntermediateActions_AddStructuralFeatureValueAction = Class(name="Actions::IntermediateActions::AddStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
Actions_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="Actions::IntermediateActions::RemoveStructuralFeatureValueAction")
Actions_IntermediateActions_StructuralFeatureAction = Class(name="Actions::IntermediateActions::StructuralFeatureAction", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
Actions_IntermediateActions_LinkAction = Class(name="Actions::IntermediateActions::LinkAction")
LinkEndData = Class(name="LinkEndData")
Actions_IntermediateActions_LinkEndData = Class(name="Actions::IntermediateActions::LinkEndData", is_abstract=True)
Element = Class(name="Element")
Property_ = Class(name="Property")
QualifierValue = Class(name="QualifierValue")
Actions_IntermediateActions_Property = Class(name="Actions::IntermediateActions::Property")
Actions_IntermediateActions_ReadLinkAction = Class(name="Actions::IntermediateActions::ReadLinkAction")
LinkAction = Class(name="LinkAction")
Actions_IntermediateActions_ClearStructuralFeatureAction = Class(name="Actions::IntermediateActions::ClearStructuralFeatureAction")
Actions_IntermediateActions_LinkEndCreationData = Class(name="Actions::IntermediateActions::LinkEndCreationData")
Actions_IntermediateActions_Element = Class(name="Actions::IntermediateActions::Element", is_abstract=True)
Actions_IntermediateActions_DestroyLinkAction = Class(name="Actions::IntermediateActions::DestroyLinkAction")
Actions_IntermediateActions_LinkEndDestructionData = Class(name="Actions::IntermediateActions::LinkEndDestructionData")
Actions_CompleteActions_ReplyAction = Class(name="Actions::CompleteActions::ReplyAction")
Trigger = Class(name="Trigger")
Actions_CompleteActions_UnmarshallAction = Class(name="Actions::CompleteActions::UnmarshallAction")
Actions_IntermediateActions_WriteLinkAction = Class(name="Actions::IntermediateActions::WriteLinkAction", is_abstract=True)
Actions_IntermediateActions_CreateLinkAction = Class(name="Actions::IntermediateActions::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
Actions_CompleteActions_AcceptEventAction = Class(name="Actions::CompleteActions::AcceptEventAction")
Actions_CompleteActions_AcceptCallAction = Class(name="Actions::CompleteActions::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
Actions_CompleteActions_Trigger = Class(name="Actions::CompleteActions::Trigger")
Actions_CompleteActions_ReadExtendAction = Class(name="Actions::CompleteActions::ReadExtendAction")
Actions_CompleteActions_ReadlsClassifiedObjectAction = Class(name="Actions::CompleteActions::ReadlsClassifiedObjectAction")
Actions_CompleteActions_StartClassifierBehaviorAction = Class(name="Actions::CompleteActions::StartClassifierBehaviorAction")
Actions_CompleteActions_ReclassifyObjectAction = Class(name="Actions::CompleteActions::ReclassifyObjectAction")
Actions_CompleteActions_QualifierValue = Class(name="Actions::CompleteActions::QualifierValue")
Actions_CompleteActions_ReadLinkObjectEndAction = Class(name="Actions::CompleteActions::ReadLinkObjectEndAction")
Actions_CompleteActions_ReadLinkObjectEndQualifierAction = Class(name="Actions::CompleteActions::ReadLinkObjectEndQualifierAction")
Actions_CompleteActions_StartObjectBehaviorAction = Class(name="Actions::CompleteActions::StartObjectBehaviorAction")
Actions_CompleteActions_CreateLinkObjectAction = Class(name="Actions::CompleteActions::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
Actions_CompleteActions_ReduceAction = Class(name="Actions::CompleteActions::ReduceAction")
Actions_StructuredActions_VariableAction = Class(name="Actions::StructuredActions::VariableAction", is_abstract=True)
Variable = Class(name="Variable")
Actions_StructuredActions_WriteVariableAction = Class(name="Actions::StructuredActions::WriteVariableAction")
Actions_StructuredActions_AddVariableValueAction = Class(name="Actions::StructuredActions::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
Actions_StructuredActions_RemoveVariableValueAction = Class(name="Actions::StructuredActions::RemoveVariableValueAction")
Actions_StructuredActions_ClearVariableAction = Class(name="Actions::StructuredActions::ClearVariableAction")
Actions_StructuredActions_RaiseExceptionAction = Class(name="Actions::StructuredActions::RaiseExceptionAction")
Actions_StructuredActions_Variable = Class(name="Actions::StructuredActions::Variable")
Actions_StructuredActions_ReadVariableAction = Class(name="Actions::StructuredActions::ReadVariableAction")
VariableAction = Class(name="VariableAction")
Actions_StructuredActions_ActionInputPin = Class(name="Actions::StructuredActions::ActionInputPin")

# Actions_BasicActions_Action class attributes and methods

# NamedElement class attributes and methods

# Classifier class attributes and methods

# InputPin class attributes and methods

# Actions_BasicActions_Classifier class attributes and methods

# Actions_BasicActions_OpaqueAction class attributes and methods
Actions_BasicActions_OpaqueAction_body: Property = Property(name="body", type=StringType)
Actions_BasicActions_OpaqueAction_language: Property = Property(name="language", type=StringType)
Actions_BasicActions_OpaqueAction.attributes={Actions_BasicActions_OpaqueAction_language, Actions_BasicActions_OpaqueAction_body}

# Action class attributes and methods

# Actions_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# Actions_BasicActions_OutputPin class attributes and methods

# Actions_BasicActions_Pin class attributes and methods

# BasicActions_TypedElement class attributes and methods

# BasicActions_MultiplicityElement class attributes and methods

# Actions_BasicActions_MultiplicityElement class attributes and methods

# Actions_BasicActions_TypedElement class attributes and methods

# Actions_BasicActions_ValuePin class attributes and methods

# OutputPin class attributes and methods

# Actions_BasicActions_NamedElement class attributes and methods

# Actions_BasicActions_ValueSpecification class attributes and methods

# Actions_BasicActions_InvocationAction class attributes and methods

# Actions_BasicActions_CallAction class attributes and methods
Actions_BasicActions_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=BooleanType)
Actions_BasicActions_CallAction.attributes={Actions_BasicActions_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# Actions_BasicActions_CallBehaviorAction class attributes and methods

# CallAction class attributes and methods

# Behavior class attributes and methods

# Actions_BasicActions_Behavior class attributes and methods

# Actions_BasicActions_CallOperationAction class attributes and methods

# Operation class attributes and methods

# ValueSpecification class attributes and methods

# Actions_BasicActions_SendSignalAction class attributes and methods

# Signal class attributes and methods

# Actions_BasicActions_Signal class attributes and methods

# Actions_IntermediateActions_BroadcastSignalAction class attributes and methods

# Actions_IntermediateActions_SendObjectAction class attributes and methods

# Actions_IntermediateActions_CreateObjectAction class attributes and methods

# Actions_BasicActions_Operation class attributes and methods

# Actions_IntermediateActions_TestIdentityAction class attributes and methods

# Actions_IntermediateActions_ReadSelfAction class attributes and methods

# Actions_IntermediateActions_ValueSpecificationAction class attributes and methods

# Actions_IntermediateActions_DestroyObjectAction class attributes and methods

# Actions_IntermediateActions_StructuralFeature class attributes and methods

# Actions_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# Actions_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# Actions_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# Actions_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods

# Actions_IntermediateActions_StructuralFeatureAction class attributes and methods

# StructuralFeature class attributes and methods

# Actions_IntermediateActions_LinkAction class attributes and methods

# LinkEndData class attributes and methods

# Actions_IntermediateActions_LinkEndData class attributes and methods

# Element class attributes and methods

# Property class attributes and methods

# QualifierValue class attributes and methods

# Actions_IntermediateActions_Property class attributes and methods

# Actions_IntermediateActions_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# Actions_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# Actions_IntermediateActions_LinkEndCreationData class attributes and methods
Actions_IntermediateActions_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
Actions_IntermediateActions_LinkEndCreationData.attributes={Actions_IntermediateActions_LinkEndCreationData_isReplaceAll}

# Actions_IntermediateActions_Element class attributes and methods

# Actions_IntermediateActions_DestroyLinkAction class attributes and methods

# Actions_IntermediateActions_LinkEndDestructionData class attributes and methods
Actions_IntermediateActions_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=BooleanType)
Actions_IntermediateActions_LinkEndDestructionData.attributes={Actions_IntermediateActions_LinkEndDestructionData_isDestroyDuplicates}

# Actions_CompleteActions_ReplyAction class attributes and methods

# Trigger class attributes and methods

# Actions_CompleteActions_UnmarshallAction class attributes and methods

# Actions_IntermediateActions_WriteLinkAction class attributes and methods

# Actions_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# Actions_CompleteActions_AcceptEventAction class attributes and methods
Actions_CompleteActions_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=BooleanType)
Actions_CompleteActions_AcceptEventAction.attributes={Actions_CompleteActions_AcceptEventAction_isUnmarshall}

# Actions_CompleteActions_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# Actions_CompleteActions_Trigger class attributes and methods

# Actions_CompleteActions_ReadExtendAction class attributes and methods

# Actions_CompleteActions_ReadlsClassifiedObjectAction class attributes and methods

# Actions_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# Actions_CompleteActions_ReclassifyObjectAction class attributes and methods
Actions_CompleteActions_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
Actions_CompleteActions_ReclassifyObjectAction.attributes={Actions_CompleteActions_ReclassifyObjectAction_isReplaceAll}

# Actions_CompleteActions_QualifierValue class attributes and methods

# Actions_CompleteActions_ReadLinkObjectEndAction class attributes and methods

# Actions_CompleteActions_ReadLinkObjectEndQualifierAction class attributes and methods

# Actions_CompleteActions_StartObjectBehaviorAction class attributes and methods

# Actions_CompleteActions_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# Actions_CompleteActions_ReduceAction class attributes and methods
Actions_CompleteActions_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
Actions_CompleteActions_ReduceAction.attributes={Actions_CompleteActions_ReduceAction_isOrdered}

# Actions_StructuredActions_VariableAction class attributes and methods

# Variable class attributes and methods

# Actions_StructuredActions_WriteVariableAction class attributes and methods

# Actions_StructuredActions_AddVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# Actions_StructuredActions_RemoveVariableValueAction class attributes and methods

# Actions_StructuredActions_ClearVariableAction class attributes and methods

# Actions_StructuredActions_RaiseExceptionAction class attributes and methods

# Actions_StructuredActions_Variable class attributes and methods

# Actions_StructuredActions_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# Actions_StructuredActions_ActionInputPin class attributes and methods

# Relationships
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="Classifier", type=Actions_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_Action", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
input1: BinaryAssociation = BinaryAssociation(
    name="input1",
    ends={
        Property(name="InputPin", type=Actions_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_Action2", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputValue5: BinaryAssociation = BinaryAssociation(
    name="inputValue5",
    ends={
        Property(name="InputPin6", type=Actions_BasicActions_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_OpaqueAction", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputValue7: BinaryAssociation = BinaryAssociation(
    name="outputValue7",
    ends={
        Property(name="OutputPin9", type=Actions_BasicActions_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_OpaqueAction8", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output3: BinaryAssociation = BinaryAssociation(
    name="output3",
    ends={
        Property(name="OutputPin", type=Actions_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_Action4", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument11: BinaryAssociation = BinaryAssociation(
    name="argument11",
    ends={
        Property(name="InputPin12", type=Actions_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_InvocationAction", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result13: BinaryAssociation = BinaryAssociation(
    name="result13",
    ends={
        Property(name="OutputPin14", type=Actions_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_CallAction", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior15: BinaryAssociation = BinaryAssociation(
    name="behavior15",
    ends={
        Property(name="Behavior", type=Actions_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_CallBehaviorAction", type=Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation16: BinaryAssociation = BinaryAssociation(
    name="operation16",
    ends={
        Property(name="Operation", type=Actions_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_CallOperationAction", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="ValueSpecification", type=Actions_BasicActions_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_ValuePin", type=ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="InputPin21", type=Actions_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_SendSignalAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal22: BinaryAssociation = BinaryAssociation(
    name="signal22",
    ends={
        Property(name="Signal", type=Actions_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_SendSignalAction23", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal24: BinaryAssociation = BinaryAssociation(
    name="signal24",
    ends={
        Property(name="Signal25", type=Actions_IntermediateActions_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_BroadcastSignalAction", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="InputPin27", type=Actions_IntermediateActions_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_SendObjectAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request28: BinaryAssociation = BinaryAssociation(
    name="request28",
    ends={
        Property(name="InputPin30", type=Actions_IntermediateActions_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_SendObjectAction29", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier31: BinaryAssociation = BinaryAssociation(
    name="classifier31",
    ends={
        Property(name="Classifier32", type=Actions_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_CreateObjectAction", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="InputPin19", type=Actions_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_BasicActions_CallOperationAction18", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target36: BinaryAssociation = BinaryAssociation(
    name="target36",
    ends={
        Property(name="InputPin37", type=Actions_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_DestroyObjectAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result38: BinaryAssociation = BinaryAssociation(
    name="result38",
    ends={
        Property(name="OutputPin39", type=Actions_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_TestIdentityAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first40: BinaryAssociation = BinaryAssociation(
    name="first40",
    ends={
        Property(name="InputPin42", type=Actions_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_TestIdentityAction41", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second43: BinaryAssociation = BinaryAssociation(
    name="second43",
    ends={
        Property(name="InputPin45", type=Actions_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_TestIdentityAction44", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result46: BinaryAssociation = BinaryAssociation(
    name="result46",
    ends={
        Property(name="OutputPin47", type=Actions_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ReadSelfAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result48: BinaryAssociation = BinaryAssociation(
    name="result48",
    ends={
        Property(name="OutputPin49", type=Actions_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ValueSpecificationAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="ValueSpecification52", type=Actions_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ValueSpecificationAction51", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result33: BinaryAssociation = BinaryAssociation(
    name="result33",
    ends={
        Property(name="OutputPin35", type=Actions_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_CreateObjectAction34", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object54: BinaryAssociation = BinaryAssociation(
    name="object54",
    ends={
        Property(name="InputPin56", type=Actions_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_StructuralFeatureAction55", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result57: BinaryAssociation = BinaryAssociation(
    name="result57",
    ends={
        Property(name="OutputPin58", type=Actions_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ReadStructuralFeatureAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="InputPin60", type=Actions_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_WriteStructuralFeatureAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result61: BinaryAssociation = BinaryAssociation(
    name="result61",
    ends={
        Property(name="OutputPin63", type=Actions_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_WriteStructuralFeatureAction62", type=OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt64: BinaryAssociation = BinaryAssociation(
    name="insertAt64",
    ends={
        Property(name="InputPin65", type=Actions_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_AddStructuralFeatureValueAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt66: BinaryAssociation = BinaryAssociation(
    name="removeAt66",
    ends={
        Property(name="InputPin67", type=Actions_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_RemoveStructuralFeatureValueAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralFeature53: BinaryAssociation = BinaryAssociation(
    name="structuralFeature53",
    ends={
        Property(name="StructuralFeature", type=Actions_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_StructuralFeatureAction", type=StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
inputValue70: BinaryAssociation = BinaryAssociation(
    name="inputValue70",
    ends={
        Property(name="InputPin71", type=Actions_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkAction", type=InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
endData72: BinaryAssociation = BinaryAssociation(
    name="endData72",
    ends={
        Property(name="LinkEndData", type=Actions_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkAction73", type=LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="InputPin75", type=Actions_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkEndData", type=InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end76: BinaryAssociation = BinaryAssociation(
    name="end76",
    ends={
        Property(name="Property", type=Actions_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkEndData77", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
qualifier78: BinaryAssociation = BinaryAssociation(
    name="qualifier78",
    ends={
        Property(name="QualifierValue", type=Actions_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkEndData79", type=QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result80: BinaryAssociation = BinaryAssociation(
    name="result80",
    ends={
        Property(name="OutputPin81", type=Actions_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ReadLinkAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result68: BinaryAssociation = BinaryAssociation(
    name="result68",
    ends={
        Property(name="OutputPin69", type=Actions_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_ClearStructuralFeatureAction", type=OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt82: BinaryAssociation = BinaryAssociation(
    name="insertAt82",
    ends={
        Property(name="InputPin83", type=Actions_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkEndCreationData", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destroyAt84: BinaryAssociation = BinaryAssociation(
    name="destroyAt84",
    ends={
        Property(name="InputPin85", type=Actions_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_IntermediateActions_LinkEndDestructionData", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnInformation86: BinaryAssociation = BinaryAssociation(
    name="returnInformation86",
    ends={
        Property(name="InputPin87", type=Actions_CompleteActions_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReplyAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue88: BinaryAssociation = BinaryAssociation(
    name="replyValue88",
    ends={
        Property(name="InputPin90", type=Actions_CompleteActions_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReplyAction89", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replyToCall91: BinaryAssociation = BinaryAssociation(
    name="replyToCall91",
    ends={
        Property(name="Trigger", type=Actions_CompleteActions_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReplyAction92", type=Trigger, multiplicity=Multiplicity(1, 1))
    }
)
object93: BinaryAssociation = BinaryAssociation(
    name="object93",
    ends={
        Property(name="InputPin94", type=Actions_CompleteActions_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_UnmarshallAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result98: BinaryAssociation = BinaryAssociation(
    name="result98",
    ends={
        Property(name="OutputPin100", type=Actions_CompleteActions_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_UnmarshallAction99", type=OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result101: BinaryAssociation = BinaryAssociation(
    name="result101",
    ends={
        Property(name="OutputPin102", type=Actions_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_AcceptEventAction", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger103: BinaryAssociation = BinaryAssociation(
    name="trigger103",
    ends={
        Property(name="Trigger105", type=Actions_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_AcceptEventAction104", type=Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnInformation106: BinaryAssociation = BinaryAssociation(
    name="returnInformation106",
    ends={
        Property(name="OutputPin107", type=Actions_CompleteActions_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_AcceptCallAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result108: BinaryAssociation = BinaryAssociation(
    name="result108",
    ends={
        Property(name="OutputPin109", type=Actions_CompleteActions_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadExtendAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unmarshallType95: BinaryAssociation = BinaryAssociation(
    name="unmarshallType95",
    ends={
        Property(name="Classifier97", type=Actions_CompleteActions_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_UnmarshallAction96", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
object113: BinaryAssociation = BinaryAssociation(
    name="object113",
    ends={
        Property(name="InputPin114", type=Actions_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReclassifyObjectAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier115: BinaryAssociation = BinaryAssociation(
    name="oldClassifier115",
    ends={
        Property(name="Classifier117", type=Actions_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReclassifyObjectAction116", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier118: BinaryAssociation = BinaryAssociation(
    name="newClassifier118",
    ends={
        Property(name="Classifier120", type=Actions_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReclassifyObjectAction119", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
result121: BinaryAssociation = BinaryAssociation(
    name="result121",
    ends={
        Property(name="OutputPin122", type=Actions_CompleteActions_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadlsClassifiedObjectAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object123: BinaryAssociation = BinaryAssociation(
    name="object123",
    ends={
        Property(name="InputPin125", type=Actions_CompleteActions_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadlsClassifiedObjectAction124", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object126: BinaryAssociation = BinaryAssociation(
    name="object126",
    ends={
        Property(name="InputPin127", type=Actions_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_StartClassifierBehaviorAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier110: BinaryAssociation = BinaryAssociation(
    name="classifier110",
    ends={
        Property(name="Classifier112", type=Actions_CompleteActions_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadExtendAction111", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
qualifier130: BinaryAssociation = BinaryAssociation(
    name="qualifier130",
    ends={
        Property(name="Property131", type=Actions_CompleteActions_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_QualifierValue", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
value132: BinaryAssociation = BinaryAssociation(
    name="value132",
    ends={
        Property(name="InputPin134", type=Actions_CompleteActions_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_QualifierValue133", type=InputPin, multiplicity=Multiplicity(1, 1))
    }
)
end135: BinaryAssociation = BinaryAssociation(
    name="end135",
    ends={
        Property(name="Property136", type=Actions_CompleteActions_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndAction", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
object137: BinaryAssociation = BinaryAssociation(
    name="object137",
    ends={
        Property(name="InputPin139", type=Actions_CompleteActions_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndAction138", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result140: BinaryAssociation = BinaryAssociation(
    name="result140",
    ends={
        Property(name="OutputPin142", type=Actions_CompleteActions_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndAction141", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object143: BinaryAssociation = BinaryAssociation(
    name="object143",
    ends={
        Property(name="InputPin144", type=Actions_CompleteActions_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndQualifierAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object128: BinaryAssociation = BinaryAssociation(
    name="object128",
    ends={
        Property(name="InputPin129", type=Actions_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_StartObjectBehaviorAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result151: BinaryAssociation = BinaryAssociation(
    name="result151",
    ends={
        Property(name="OutputPin152", type=Actions_CompleteActions_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_CreateLinkObjectAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result153: BinaryAssociation = BinaryAssociation(
    name="result153",
    ends={
        Property(name="OutputPin154", type=Actions_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReduceAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection155: BinaryAssociation = BinaryAssociation(
    name="collection155",
    ends={
        Property(name="InputPin157", type=Actions_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReduceAction156", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer158: BinaryAssociation = BinaryAssociation(
    name="reducer158",
    ends={
        Property(name="Behavior160", type=Actions_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReduceAction159", type=Behavior, multiplicity=Multiplicity(1, 1))
    }
)
variable161: BinaryAssociation = BinaryAssociation(
    name="variable161",
    ends={
        Property(name="Variable", type=Actions_StructuredActions_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_VariableAction", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
result145: BinaryAssociation = BinaryAssociation(
    name="result145",
    ends={
        Property(name="OutputPin147", type=Actions_CompleteActions_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndQualifierAction146", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier148: BinaryAssociation = BinaryAssociation(
    name="qualifier148",
    ends={
        Property(name="Property150", type=Actions_CompleteActions_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_CompleteActions_ReadLinkObjectEndQualifierAction149", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
result162: BinaryAssociation = BinaryAssociation(
    name="result162",
    ends={
        Property(name="Actions_StructuredActions_ReadVariableAction", type=OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OutputPin163", type=Actions_StructuredActions_ReadVariableAction, multiplicity=Multiplicity(1, 1))
    }
)
value164: BinaryAssociation = BinaryAssociation(
    name="value164",
    ends={
        Property(name="InputPin165", type=Actions_StructuredActions_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_WriteVariableAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt166: BinaryAssociation = BinaryAssociation(
    name="insertAt166",
    ends={
        Property(name="InputPin167", type=Actions_StructuredActions_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_AddVariableValueAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt168: BinaryAssociation = BinaryAssociation(
    name="removeAt168",
    ends={
        Property(name="InputPin169", type=Actions_StructuredActions_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_RemoveVariableValueAction", type=InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception170: BinaryAssociation = BinaryAssociation(
    name="exception170",
    ends={
        Property(name="InputPin171", type=Actions_StructuredActions_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_RaiseExceptionAction", type=InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromAction172: BinaryAssociation = BinaryAssociation(
    name="fromAction172",
    ends={
        Property(name="Action", type=Actions_StructuredActions_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions_StructuredActions_ActionInputPin", type=Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Actions_BasicActions_Action_NamedElement = Generalization(general=NamedElement, specific=Actions_BasicActions_Action)
gen_Actions_BasicActions_OpaqueAction_Action = Generalization(general=Action, specific=Actions_BasicActions_OpaqueAction)
gen_Actions_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=Actions_BasicActions_InputPin)
gen_Actions_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=Actions_BasicActions_OutputPin)
gen_Actions_BasicActions_Pin_BasicActions_TypedElement = Generalization(general=BasicActions_TypedElement, specific=Actions_BasicActions_Pin)
gen_Actions_BasicActions_Pin_BasicActions_MultiplicityElement = Generalization(general=BasicActions_MultiplicityElement, specific=Actions_BasicActions_Pin)
gen_Actions_BasicActions_ValuePin_InputPin = Generalization(general=InputPin, specific=Actions_BasicActions_ValuePin)
gen_Actions_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=Actions_BasicActions_InvocationAction)
gen_Actions_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=Actions_BasicActions_CallAction)
gen_Actions_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=Actions_BasicActions_CallBehaviorAction)
gen_Actions_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=Actions_BasicActions_SendSignalAction)
gen_Actions_IntermediateActions_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=Actions_IntermediateActions_BroadcastSignalAction)
gen_Actions_IntermediateActions_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=Actions_IntermediateActions_SendObjectAction)
gen_Actions_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_CreateObjectAction)
gen_Actions_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_TestIdentityAction)
gen_Actions_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_ReadSelfAction)
gen_Actions_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_ValueSpecificationAction)
gen_Actions_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_DestroyObjectAction)
gen_Actions_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=Actions_IntermediateActions_ReadStructuralFeatureAction)
gen_Actions_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=Actions_IntermediateActions_WriteStructuralFeatureAction)
gen_Actions_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=Actions_IntermediateActions_AddStructuralFeatureValueAction)
gen_Actions_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=Actions_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_Actions_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_StructuralFeatureAction)
gen_Actions_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=Actions_IntermediateActions_LinkAction)
gen_Actions_IntermediateActions_LinkEndData_Element = Generalization(general=Element, specific=Actions_IntermediateActions_LinkEndData)
gen_Actions_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=Actions_IntermediateActions_ReadLinkAction)
gen_Actions_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=Actions_IntermediateActions_ClearStructuralFeatureAction)
gen_Actions_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=Actions_IntermediateActions_LinkEndCreationData)
gen_Actions_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=Actions_IntermediateActions_DestroyLinkAction)
gen_Actions_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=Actions_IntermediateActions_LinkEndDestructionData)
gen_Actions_CompleteActions_ReplyAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReplyAction)
gen_Actions_CompleteActions_UnmarshallAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_UnmarshallAction)
gen_Actions_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=Actions_IntermediateActions_WriteLinkAction)
gen_Actions_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=Actions_IntermediateActions_CreateLinkAction)
gen_Actions_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_AcceptEventAction)
gen_Actions_CompleteActions_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=Actions_CompleteActions_AcceptCallAction)
gen_Actions_CompleteActions_ReadExtendAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReadExtendAction)
gen_Actions_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_StartClassifierBehaviorAction)
gen_Actions_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReclassifyObjectAction)
gen_Actions_CompleteActions_QualifierValue_Element = Generalization(general=Element, specific=Actions_CompleteActions_QualifierValue)
gen_Actions_CompleteActions_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReadLinkObjectEndAction)
gen_Actions_CompleteActions_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReadLinkObjectEndQualifierAction)
gen_Actions_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=Actions_CompleteActions_StartObjectBehaviorAction)
gen_Actions_CompleteActions_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=Actions_CompleteActions_CreateLinkObjectAction)
gen_Actions_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=Actions_CompleteActions_ReduceAction)
gen_Actions_StructuredActions_VariableAction_Action = Generalization(general=Action, specific=Actions_StructuredActions_VariableAction)
gen_Actions_StructuredActions_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=Actions_StructuredActions_WriteVariableAction)
gen_Actions_StructuredActions_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=Actions_StructuredActions_AddVariableValueAction)
gen_Actions_StructuredActions_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=Actions_StructuredActions_RemoveVariableValueAction)
gen_Actions_StructuredActions_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=Actions_StructuredActions_ClearVariableAction)
gen_Actions_StructuredActions_RaiseExceptionAction_Action = Generalization(general=Action, specific=Actions_StructuredActions_RaiseExceptionAction)
gen_Actions_StructuredActions_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=Actions_StructuredActions_ReadVariableAction)
gen_Actions_StructuredActions_ActionInputPin_InputPin = Generalization(general=InputPin, specific=Actions_StructuredActions_ActionInputPin)

# Domain Model
domain_model = DomainModel(
    name="Actions",
    types={Actions_BasicActions_Action, NamedElement, Classifier, InputPin, Actions_BasicActions_Classifier, Actions_BasicActions_OpaqueAction, Action, Actions_BasicActions_InputPin, Pin, Actions_BasicActions_OutputPin, Actions_BasicActions_Pin, BasicActions_TypedElement, BasicActions_MultiplicityElement, Actions_BasicActions_MultiplicityElement, Actions_BasicActions_TypedElement, Actions_BasicActions_ValuePin, OutputPin, Actions_BasicActions_NamedElement, Actions_BasicActions_ValueSpecification, Actions_BasicActions_InvocationAction, Actions_BasicActions_CallAction, InvocationAction, Actions_BasicActions_CallBehaviorAction, CallAction, Behavior, Actions_BasicActions_Behavior, Actions_BasicActions_CallOperationAction, Operation, ValueSpecification, Actions_BasicActions_SendSignalAction, Signal, Actions_BasicActions_Signal, Actions_IntermediateActions_BroadcastSignalAction, Actions_IntermediateActions_SendObjectAction, Actions_IntermediateActions_CreateObjectAction, Actions_BasicActions_Operation, Actions_IntermediateActions_TestIdentityAction, Actions_IntermediateActions_ReadSelfAction, Actions_IntermediateActions_ValueSpecificationAction, Actions_IntermediateActions_DestroyObjectAction, Actions_IntermediateActions_StructuralFeature, Actions_IntermediateActions_ReadStructuralFeatureAction, StructuralFeatureAction, Actions_IntermediateActions_WriteStructuralFeatureAction, Actions_IntermediateActions_AddStructuralFeatureValueAction, WriteStructuralFeatureAction, Actions_IntermediateActions_RemoveStructuralFeatureValueAction, Actions_IntermediateActions_StructuralFeatureAction, StructuralFeature, Actions_IntermediateActions_LinkAction, LinkEndData, Actions_IntermediateActions_LinkEndData, Element, Property_, QualifierValue, Actions_IntermediateActions_Property, Actions_IntermediateActions_ReadLinkAction, LinkAction, Actions_IntermediateActions_ClearStructuralFeatureAction, Actions_IntermediateActions_LinkEndCreationData, Actions_IntermediateActions_Element, Actions_IntermediateActions_DestroyLinkAction, Actions_IntermediateActions_LinkEndDestructionData, Actions_CompleteActions_ReplyAction, Trigger, Actions_CompleteActions_UnmarshallAction, Actions_IntermediateActions_WriteLinkAction, Actions_IntermediateActions_CreateLinkAction, WriteLinkAction, Actions_CompleteActions_AcceptEventAction, Actions_CompleteActions_AcceptCallAction, AcceptEventAction, Actions_CompleteActions_Trigger, Actions_CompleteActions_ReadExtendAction, Actions_CompleteActions_ReadlsClassifiedObjectAction, Actions_CompleteActions_StartClassifierBehaviorAction, Actions_CompleteActions_ReclassifyObjectAction, Actions_CompleteActions_QualifierValue, Actions_CompleteActions_ReadLinkObjectEndAction, Actions_CompleteActions_ReadLinkObjectEndQualifierAction, Actions_CompleteActions_StartObjectBehaviorAction, Actions_CompleteActions_CreateLinkObjectAction, CreateLinkAction, Actions_CompleteActions_ReduceAction, Actions_StructuredActions_VariableAction, Variable, Actions_StructuredActions_WriteVariableAction, Actions_StructuredActions_AddVariableValueAction, WriteVariableAction, Actions_StructuredActions_RemoveVariableValueAction, Actions_StructuredActions_ClearVariableAction, Actions_StructuredActions_RaiseExceptionAction, Actions_StructuredActions_Variable, Actions_StructuredActions_ReadVariableAction, VariableAction, Actions_StructuredActions_ActionInputPin},
    associations={context0, input1, inputValue5, outputValue7, output3, argument11, result13, behavior15, operation16, value10, target20, signal22, signal24, target26, request28, classifier31, target17, target36, result38, first40, second43, result46, result48, value50, result33, object54, result57, value59, result61, insertAt64, removeAt66, structuralFeature53, inputValue70, endData72, value74, end76, qualifier78, result80, result68, insertAt82, destroyAt84, returnInformation86, replyValue88, replyToCall91, object93, result98, result101, trigger103, returnInformation106, result108, unmarshallType95, object113, oldClassifier115, newClassifier118, result121, object123, object126, classifier110, qualifier130, value132, end135, object137, result140, object143, object128, result151, result153, collection155, reducer158, variable161, result145, qualifier148, result162, value164, insertAt166, removeAt168, exception170, fromAction172},
    generalizations={gen_Actions_BasicActions_Action_NamedElement, gen_Actions_BasicActions_OpaqueAction_Action, gen_Actions_BasicActions_InputPin_Pin, gen_Actions_BasicActions_OutputPin_Pin, gen_Actions_BasicActions_Pin_BasicActions_TypedElement, gen_Actions_BasicActions_Pin_BasicActions_MultiplicityElement, gen_Actions_BasicActions_ValuePin_InputPin, gen_Actions_BasicActions_InvocationAction_Action, gen_Actions_BasicActions_CallAction_InvocationAction, gen_Actions_BasicActions_CallBehaviorAction_CallAction, gen_Actions_BasicActions_SendSignalAction_InvocationAction, gen_Actions_IntermediateActions_BroadcastSignalAction_InvocationAction, gen_Actions_IntermediateActions_SendObjectAction_InvocationAction, gen_Actions_IntermediateActions_CreateObjectAction_Action, gen_Actions_IntermediateActions_TestIdentityAction_Action, gen_Actions_IntermediateActions_ReadSelfAction_Action, gen_Actions_IntermediateActions_ValueSpecificationAction_Action, gen_Actions_IntermediateActions_DestroyObjectAction_Action, gen_Actions_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_Actions_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_Actions_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_Actions_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_Actions_IntermediateActions_StructuralFeatureAction_Action, gen_Actions_IntermediateActions_LinkAction_Action, gen_Actions_IntermediateActions_LinkEndData_Element, gen_Actions_IntermediateActions_ReadLinkAction_LinkAction, gen_Actions_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_Actions_IntermediateActions_LinkEndCreationData_LinkEndData, gen_Actions_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_Actions_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_Actions_CompleteActions_ReplyAction_Action, gen_Actions_CompleteActions_UnmarshallAction_Action, gen_Actions_IntermediateActions_WriteLinkAction_LinkAction, gen_Actions_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_Actions_CompleteActions_AcceptEventAction_Action, gen_Actions_CompleteActions_AcceptCallAction_AcceptEventAction, gen_Actions_CompleteActions_ReadExtendAction_Action, gen_Actions_CompleteActions_StartClassifierBehaviorAction_Action, gen_Actions_CompleteActions_ReclassifyObjectAction_Action, gen_Actions_CompleteActions_QualifierValue_Element, gen_Actions_CompleteActions_ReadLinkObjectEndAction_Action, gen_Actions_CompleteActions_ReadLinkObjectEndQualifierAction_Action, gen_Actions_CompleteActions_StartObjectBehaviorAction_CallAction, gen_Actions_CompleteActions_CreateLinkObjectAction_CreateLinkAction, gen_Actions_CompleteActions_ReduceAction_Action, gen_Actions_StructuredActions_VariableAction_Action, gen_Actions_StructuredActions_WriteVariableAction_VariableAction, gen_Actions_StructuredActions_AddVariableValueAction_WriteVariableAction, gen_Actions_StructuredActions_RemoveVariableValueAction_WriteVariableAction, gen_Actions_StructuredActions_ClearVariableAction_VariableAction, gen_Actions_StructuredActions_RaiseExceptionAction_Action, gen_Actions_StructuredActions_ReadVariableAction_VariableAction, gen_Actions_StructuredActions_ActionInputPin_InputPin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)