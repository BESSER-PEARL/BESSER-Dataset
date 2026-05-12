import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    WriteVariableAction,
    UML2_AddVariableValueAction,
    UML2_RemoveVariableValueAction,
    StateMachine,
    UML2_ProtocolStateMachine,
    EncapsulatedClassifier,
    BehavioredClassifier,
    UML2_Class,
    LiteralSpecification,
    UML2_LiteralNull,
    WriteLinkAction,
    UML2_DestroyLinkAction,
    UML2_CreateLinkAction,
    DataType,
    UML2_Enumeration,
    UML2_PrimitiveType,
    TypedElement,
    UML2_ValueSpecification,
    UML2_Operation,
    UML2_Variable,
    UML2_StructuralFeature,
    CallAction,
    UML2_CallOperationAction,
    Interval,
    UML2_TimeInterval,
    Behavior,
    UML2_Activity,
    UML2_StateMachine,
    Class,
    UML2_Behavior,
    LinkAction,
    UML2_ReadLinkAction,
    Association,
    UML2_AssociationClass,
    UML2_Extension,
    Property,
    UML2_Port,
    VariableAction,
    UML2_ReadVariableAction,
    ObjectNode,
    UML2_Pin,
    UML2_ActivityParameterNode,
    InvocationAction,
    UML2_CallAction,
    UML2_SendSignalAction,
    UML2_BroadcastSignalAction,
    StructuredClassifier,
    UML2_EncapsulatedClassifier,
    Pin,
    UML2_InputPin,
    ValueSpecification,
    UML2_LiteralSpecification,
    UML2_Interval,
    CentralBufferNode,
    UML2_DataStoreNode,
    UML2_OutputPin,
    WriteStructuralFeatureAction,
    UML2_AddStructuralFeatureValueAction,
    UML2_DurationObservationAction,
    UML2_RemoveStructuralFeatureValueAction,
    UML2_TimeObservationAction,
    Action,
    UML2_AcceptEventAction,
    UML2_DestroyObjectAction,
    UML2_ReadLinkObjectEndQualifierAction,
    UML2_LinkAction,
    UML2_VariableAction,
    UML2_CreateObjectAction,
    UML2_RaiseExceptionAction,
    UML2_ReadIsClassifiedObjectAction,
    UML2_StartOwnedBehaviorAction,
    UML2_ReclassifyObjectAction,
    UML2_ReadSelfAction,
    UML2_StructuralFeatureAction,
    UML2_StructuredActivityNode,
    Classifier,
    UML2_TemplateableClassifier,
    UML2_Actor,
    UML2_DataType,
    StructuralFeatureAction,
    UML2_ReadStructuralFeatureAction,
    AcceptEventAction,
    UML2_AcceptCallAction,
    Node,
    UML2_Device,
    UML2_TimeExpression,
    UML2_StructuredClassifier,
    UML2_Action,
    UML2_SendObjectAction,
    UML2_InstanceValue,
    UML2_Node,
    UML2_CommunicationPath,
    UML2_LiteralBoolean,
    UML2_ReplyAction,
    OpaqueExpression,
    UML2_Expression,
    InputPin,
    UML2_ValuePin,
    UML2_ExpansionNode,
    UML2_Interaction,
    UML2_WriteLinkAction,
    UML2_LiteralUnlimitedNatural,
    UML2_InformationItem,
    UML2_ClearVariableAction,
    CreateLinkAction,
    UML2_CreateLinkObjectAction,
    UML2_TestIdentityAction,
    UML2_UseCase,
    UML2_Association,
    UML2_LiteralInteger,
    UML2_WriteStructuralFeatureAction,
    UML2_ExecutionEnvironment,
    UML2_Type,
    UML2_TypedElement,
    UML2_ObjectNode,
    UML2_InvocationAction,
    UML2_WriteVariableAction,
    UML2_OpaqueExpression,
    UML2_DurationInterval,
    UML2_ParameterableClassifier,
    UML2_CallBehaviorAction,
    UML2_Duration,
    StructuralFeature,
    UML2_Property,
    UML2_Parameter,
    UML2_ClearStructuralFeatureAction,
    UML2_Artifact,
    UML2_Collaboration,
    UML2_ExtensionEnd,
    UML2_Stereotype,
    UML2_Interface,
    UML2_Component,
    Artifact,
    UML2_DeploymentSpecification,
    UML2_CentralBufferNode,
    UML2_Signal,
    UML2_BehavioredClassifier,
    UML2_LiteralString,
    StructuredActivityNode,
    UML2_ExpansionRegion,
    UML2_LoopNode,
    UML2_ConditionalNode,
    UML2_ApplyFunctionAction,
    UML2_ClearAssociationAction,
    UML2_ReadExtentAction,
    Type,
    UML2_Classifier,
    UML2_ReadLinkObjectEndAction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AddVariableValueAction)


def test_uml2_addvariablevalueaction_constructor_exists():
    assert callable(UML2_AddVariableValueAction.__init__)


def test_uml2_addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RemoveVariableValueAction)


def test_uml2_removevariablevalueaction_constructor_exists():
    assert callable(UML2_RemoveVariableValueAction.__init__)


def test_uml2_removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolStateMachine)


def test_uml2_protocolstatemachine_constructor_exists():
    assert callable(UML2_ProtocolStateMachine.__init__)


def test_uml2_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_class_is_not_abstract():
    assert not inspect.isabstract(UML2_Class)


def test_uml2_class_constructor_exists():
    assert callable(UML2_Class.__init__)


def test_uml2_class_constructor_args():
    sig = inspect.signature(UML2_Class.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralNull)


def test_uml2_literalnull_constructor_exists():
    assert callable(UML2_LiteralNull.__init__)


def test_uml2_literalnull_constructor_args():
    sig = inspect.signature(UML2_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DestroyLinkAction)


def test_uml2_destroylinkaction_constructor_exists():
    assert callable(UML2_DestroyLinkAction.__init__)


def test_uml2_destroylinkaction_constructor_args():
    sig = inspect.signature(UML2_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateLinkAction)


def test_uml2_createlinkaction_constructor_exists():
    assert callable(UML2_CreateLinkAction.__init__)


def test_uml2_createlinkaction_constructor_args():
    sig = inspect.signature(UML2_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2_Enumeration)


def test_uml2_enumeration_constructor_exists():
    assert callable(UML2_Enumeration.__init__)


def test_uml2_enumeration_constructor_args():
    sig = inspect.signature(UML2_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2_PrimitiveType)


def test_uml2_primitivetype_constructor_exists():
    assert callable(UML2_PrimitiveType.__init__)


def test_uml2_primitivetype_constructor_args():
    sig = inspect.signature(UML2_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2_ValueSpecification)


def test_uml2_valuespecification_constructor_exists():
    assert callable(UML2_ValueSpecification.__init__)


def test_uml2_valuespecification_constructor_args():
    sig = inspect.signature(UML2_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operation_is_not_abstract():
    assert not inspect.isabstract(UML2_Operation)


def test_uml2_operation_constructor_exists():
    assert callable(UML2_Operation.__init__)


def test_uml2_operation_constructor_args():
    sig = inspect.signature(UML2_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2_variable_is_not_abstract():
    assert not inspect.isabstract(UML2_Variable)


def test_uml2_variable_constructor_exists():
    assert callable(UML2_Variable.__init__)


def test_uml2_variable_constructor_args():
    sig = inspect.signature(UML2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeature)


def test_uml2_structuralfeature_constructor_exists():
    assert callable(UML2_StructuralFeature.__init__)


def test_uml2_structuralfeature_constructor_args():
    sig = inspect.signature(UML2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallOperationAction)


def test_uml2_calloperationaction_constructor_exists():
    assert callable(UML2_CallOperationAction.__init__)


def test_uml2_calloperationaction_constructor_args():
    sig = inspect.signature(UML2_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeInterval)


def test_uml2_timeinterval_constructor_exists():
    assert callable(UML2_TimeInterval.__init__)


def test_uml2_timeinterval_constructor_args():
    sig = inspect.signature(UML2_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activity_is_not_abstract():
    assert not inspect.isabstract(UML2_Activity)


def test_uml2_activity_constructor_exists():
    assert callable(UML2_Activity.__init__)


def test_uml2_activity_constructor_args():
    sig = inspect.signature(UML2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_StateMachine)


def test_uml2_statemachine_constructor_exists():
    assert callable(UML2_StateMachine.__init__)


def test_uml2_statemachine_constructor_args():
    sig = inspect.signature(UML2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2_Behavior)


def test_uml2_behavior_constructor_exists():
    assert callable(UML2_Behavior.__init__)


def test_uml2_behavior_constructor_args():
    sig = inspect.signature(UML2_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkAction)


def test_uml2_readlinkaction_constructor_exists():
    assert callable(UML2_ReadLinkAction.__init__)


def test_uml2_readlinkaction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2_AssociationClass)


def test_uml2_associationclass_constructor_exists():
    assert callable(UML2_AssociationClass.__init__)


def test_uml2_associationclass_constructor_args():
    sig = inspect.signature(UML2_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extension_is_not_abstract():
    assert not inspect.isabstract(UML2_Extension)


def test_uml2_extension_constructor_exists():
    assert callable(UML2_Extension.__init__)


def test_uml2_extension_constructor_args():
    sig = inspect.signature(UML2_Extension.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadVariableAction)


def test_uml2_readvariableaction_constructor_exists():
    assert callable(UML2_ReadVariableAction.__init__)


def test_uml2_readvariableaction_constructor_args():
    sig = inspect.signature(UML2_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_pin_is_not_abstract():
    assert not inspect.isabstract(UML2_Pin)


def test_uml2_pin_constructor_exists():
    assert callable(UML2_Pin.__init__)


def test_uml2_pin_constructor_args():
    sig = inspect.signature(UML2_Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityParameterNode)


def test_uml2_activityparameternode_constructor_exists():
    assert callable(UML2_ActivityParameterNode.__init__)


def test_uml2_activityparameternode_constructor_args():
    sig = inspect.signature(UML2_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_callaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallAction)


def test_uml2_callaction_constructor_exists():
    assert callable(UML2_CallAction.__init__)


def test_uml2_callaction_constructor_args():
    sig = inspect.signature(UML2_CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2_SendSignalAction)


def test_uml2_sendsignalaction_constructor_exists():
    assert callable(UML2_SendSignalAction.__init__)


def test_uml2_sendsignalaction_constructor_args():
    sig = inspect.signature(UML2_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2_BroadcastSignalAction)


def test_uml2_broadcastsignalaction_constructor_exists():
    assert callable(UML2_BroadcastSignalAction.__init__)


def test_uml2_broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_EncapsulatedClassifier)


def test_uml2_encapsulatedclassifier_constructor_exists():
    assert callable(UML2_EncapsulatedClassifier.__init__)


def test_uml2_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_InputPin)


def test_uml2_inputpin_constructor_exists():
    assert callable(UML2_InputPin.__init__)


def test_uml2_inputpin_constructor_args():
    sig = inspect.signature(UML2_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralSpecification)


def test_uml2_literalspecification_constructor_exists():
    assert callable(UML2_LiteralSpecification.__init__)


def test_uml2_literalspecification_constructor_args():
    sig = inspect.signature(UML2_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interval_is_not_abstract():
    assert not inspect.isabstract(UML2_Interval)


def test_uml2_interval_constructor_exists():
    assert callable(UML2_Interval.__init__)


def test_uml2_interval_constructor_args():
    sig = inspect.signature(UML2_Interval.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2_DataStoreNode)


def test_uml2_datastorenode_constructor_exists():
    assert callable(UML2_DataStoreNode.__init__)


def test_uml2_datastorenode_constructor_args():
    sig = inspect.signature(UML2_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_OutputPin)


def test_uml2_outputpin_constructor_exists():
    assert callable(UML2_OutputPin.__init__)


def test_uml2_outputpin_constructor_args():
    sig = inspect.signature(UML2_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AddStructuralFeatureValueAction)


def test_uml2_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2_AddStructuralFeatureValueAction.__init__)


def test_uml2_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationObservationAction)


def test_uml2_durationobservationaction_constructor_exists():
    assert callable(UML2_DurationObservationAction.__init__)


def test_uml2_durationobservationaction_constructor_args():
    sig = inspect.signature(UML2_DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RemoveStructuralFeatureValueAction)


def test_uml2_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2_RemoveStructuralFeatureValueAction.__init__)


def test_uml2_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeObservationAction)


def test_uml2_timeobservationaction_constructor_exists():
    assert callable(UML2_TimeObservationAction.__init__)


def test_uml2_timeobservationaction_constructor_args():
    sig = inspect.signature(UML2_TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AcceptEventAction)


def test_uml2_accepteventaction_constructor_exists():
    assert callable(UML2_AcceptEventAction.__init__)


def test_uml2_accepteventaction_constructor_args():
    sig = inspect.signature(UML2_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DestroyObjectAction)


def test_uml2_destroyobjectaction_constructor_exists():
    assert callable(UML2_DestroyObjectAction.__init__)


def test_uml2_destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkObjectEndQualifierAction)


def test_uml2_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2_ReadLinkObjectEndQualifierAction.__init__)


def test_uml2_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkAction)


def test_uml2_linkaction_constructor_exists():
    assert callable(UML2_LinkAction.__init__)


def test_uml2_linkaction_constructor_args():
    sig = inspect.signature(UML2_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_VariableAction)


def test_uml2_variableaction_constructor_exists():
    assert callable(UML2_VariableAction.__init__)


def test_uml2_variableaction_constructor_args():
    sig = inspect.signature(UML2_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateObjectAction)


def test_uml2_createobjectaction_constructor_exists():
    assert callable(UML2_CreateObjectAction.__init__)


def test_uml2_createobjectaction_constructor_args():
    sig = inspect.signature(UML2_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RaiseExceptionAction)


def test_uml2_raiseexceptionaction_constructor_exists():
    assert callable(UML2_RaiseExceptionAction.__init__)


def test_uml2_raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadIsClassifiedObjectAction)


def test_uml2_readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2_ReadIsClassifiedObjectAction.__init__)


def test_uml2_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2_StartOwnedBehaviorAction)


def test_uml2_startownedbehavioraction_constructor_exists():
    assert callable(UML2_StartOwnedBehaviorAction.__init__)


def test_uml2_startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2_StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReclassifyObjectAction)


def test_uml2_reclassifyobjectaction_constructor_exists():
    assert callable(UML2_ReclassifyObjectAction.__init__)


def test_uml2_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadSelfAction)


def test_uml2_readselfaction_constructor_exists():
    assert callable(UML2_ReadSelfAction.__init__)


def test_uml2_readselfaction_constructor_args():
    sig = inspect.signature(UML2_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeatureAction)


def test_uml2_structuralfeatureaction_constructor_exists():
    assert callable(UML2_StructuralFeatureAction.__init__)


def test_uml2_structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuredActivityNode)


def test_uml2_structuredactivitynode_constructor_exists():
    assert callable(UML2_StructuredActivityNode.__init__)


def test_uml2_structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateableClassifier)


def test_uml2_templateableclassifier_constructor_exists():
    assert callable(UML2_TemplateableClassifier.__init__)


def test_uml2_templateableclassifier_constructor_args():
    sig = inspect.signature(UML2_TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_actor_is_not_abstract():
    assert not inspect.isabstract(UML2_Actor)


def test_uml2_actor_constructor_exists():
    assert callable(UML2_Actor.__init__)


def test_uml2_actor_constructor_args():
    sig = inspect.signature(UML2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datatype_is_not_abstract():
    assert not inspect.isabstract(UML2_DataType)


def test_uml2_datatype_constructor_exists():
    assert callable(UML2_DataType.__init__)


def test_uml2_datatype_constructor_args():
    sig = inspect.signature(UML2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadStructuralFeatureAction)


def test_uml2_readstructuralfeatureaction_constructor_exists():
    assert callable(UML2_ReadStructuralFeatureAction.__init__)


def test_uml2_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AcceptCallAction)


def test_uml2_acceptcallaction_constructor_exists():
    assert callable(UML2_AcceptCallAction.__init__)


def test_uml2_acceptcallaction_constructor_args():
    sig = inspect.signature(UML2_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_device_is_not_abstract():
    assert not inspect.isabstract(UML2_Device)


def test_uml2_device_constructor_exists():
    assert callable(UML2_Device.__init__)


def test_uml2_device_constructor_args():
    sig = inspect.signature(UML2_Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeExpression)


def test_uml2_timeexpression_constructor_exists():
    assert callable(UML2_TimeExpression.__init__)


def test_uml2_timeexpression_constructor_args():
    sig = inspect.signature(UML2_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuredClassifier)


def test_uml2_structuredclassifier_constructor_exists():
    assert callable(UML2_StructuredClassifier.__init__)


def test_uml2_structuredclassifier_constructor_args():
    sig = inspect.signature(UML2_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_action_is_not_abstract():
    assert not inspect.isabstract(UML2_Action)


def test_uml2_action_constructor_exists():
    assert callable(UML2_Action.__init__)


def test_uml2_action_constructor_args():
    sig = inspect.signature(UML2_Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_SendObjectAction)


def test_uml2_sendobjectaction_constructor_exists():
    assert callable(UML2_SendObjectAction.__init__)


def test_uml2_sendobjectaction_constructor_args():
    sig = inspect.signature(UML2_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2_InstanceValue)


def test_uml2_instancevalue_constructor_exists():
    assert callable(UML2_InstanceValue.__init__)


def test_uml2_instancevalue_constructor_args():
    sig = inspect.signature(UML2_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2_node_is_not_abstract():
    assert not inspect.isabstract(UML2_Node)


def test_uml2_node_constructor_exists():
    assert callable(UML2_Node.__init__)


def test_uml2_node_constructor_args():
    sig = inspect.signature(UML2_Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2_CommunicationPath)


def test_uml2_communicationpath_constructor_exists():
    assert callable(UML2_CommunicationPath.__init__)


def test_uml2_communicationpath_constructor_args():
    sig = inspect.signature(UML2_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralBoolean)


def test_uml2_literalboolean_constructor_exists():
    assert callable(UML2_LiteralBoolean.__init__)


def test_uml2_literalboolean_constructor_args():
    sig = inspect.signature(UML2_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2_replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReplyAction)


def test_uml2_replyaction_constructor_exists():
    assert callable(UML2_ReplyAction.__init__)


def test_uml2_replyaction_constructor_args():
    sig = inspect.signature(UML2_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expression_is_not_abstract():
    assert not inspect.isabstract(UML2_Expression)


def test_uml2_expression_constructor_exists():
    assert callable(UML2_Expression.__init__)


def test_uml2_expression_constructor_args():
    sig = inspect.signature(UML2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2_ValuePin)


def test_uml2_valuepin_constructor_exists():
    assert callable(UML2_ValuePin.__init__)


def test_uml2_valuepin_constructor_args():
    sig = inspect.signature(UML2_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ExpansionNode)


def test_uml2_expansionnode_constructor_exists():
    assert callable(UML2_ExpansionNode.__init__)


def test_uml2_expansionnode_constructor_args():
    sig = inspect.signature(UML2_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2_Interaction)


def test_uml2_interaction_constructor_exists():
    assert callable(UML2_Interaction.__init__)


def test_uml2_interaction_constructor_args():
    sig = inspect.signature(UML2_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteLinkAction)


def test_uml2_writelinkaction_constructor_exists():
    assert callable(UML2_WriteLinkAction.__init__)


def test_uml2_writelinkaction_constructor_args():
    sig = inspect.signature(UML2_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralUnlimitedNatural)


def test_uml2_literalunlimitednatural_constructor_exists():
    assert callable(UML2_LiteralUnlimitedNatural.__init__)


def test_uml2_literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2_informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2_InformationItem)


def test_uml2_informationitem_constructor_exists():
    assert callable(UML2_InformationItem.__init__)


def test_uml2_informationitem_constructor_args():
    sig = inspect.signature(UML2_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearVariableAction)


def test_uml2_clearvariableaction_constructor_exists():
    assert callable(UML2_ClearVariableAction.__init__)


def test_uml2_clearvariableaction_constructor_args():
    sig = inspect.signature(UML2_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateLinkObjectAction)


def test_uml2_createlinkobjectaction_constructor_exists():
    assert callable(UML2_CreateLinkObjectAction.__init__)


def test_uml2_createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2_TestIdentityAction)


def test_uml2_testidentityaction_constructor_exists():
    assert callable(UML2_TestIdentityAction.__init__)


def test_uml2_testidentityaction_constructor_args():
    sig = inspect.signature(UML2_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_usecase_is_not_abstract():
    assert not inspect.isabstract(UML2_UseCase)


def test_uml2_usecase_constructor_exists():
    assert callable(UML2_UseCase.__init__)


def test_uml2_usecase_constructor_args():
    sig = inspect.signature(UML2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2_association_is_not_abstract():
    assert not inspect.isabstract(UML2_Association)


def test_uml2_association_constructor_exists():
    assert callable(UML2_Association.__init__)


def test_uml2_association_constructor_args():
    sig = inspect.signature(UML2_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralInteger)


def test_uml2_literalinteger_constructor_exists():
    assert callable(UML2_LiteralInteger.__init__)


def test_uml2_literalinteger_constructor_args():
    sig = inspect.signature(UML2_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteStructuralFeatureAction)


def test_uml2_writestructuralfeatureaction_constructor_exists():
    assert callable(UML2_WriteStructuralFeatureAction.__init__)


def test_uml2_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutionEnvironment)


def test_uml2_executionenvironment_constructor_exists():
    assert callable(UML2_ExecutionEnvironment.__init__)


def test_uml2_executionenvironment_constructor_args():
    sig = inspect.signature(UML2_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_type_is_not_abstract():
    assert not inspect.isabstract(UML2_Type)


def test_uml2_type_constructor_exists():
    assert callable(UML2_Type.__init__)


def test_uml2_type_constructor_args():
    sig = inspect.signature(UML2_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2_typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2_TypedElement)


def test_uml2_typedelement_constructor_exists():
    assert callable(UML2_TypedElement.__init__)


def test_uml2_typedelement_constructor_args():
    sig = inspect.signature(UML2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ObjectNode)


def test_uml2_objectnode_constructor_exists():
    assert callable(UML2_ObjectNode.__init__)


def test_uml2_objectnode_constructor_args():
    sig = inspect.signature(UML2_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_InvocationAction)


def test_uml2_invocationaction_constructor_exists():
    assert callable(UML2_InvocationAction.__init__)


def test_uml2_invocationaction_constructor_args():
    sig = inspect.signature(UML2_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteVariableAction)


def test_uml2_writevariableaction_constructor_exists():
    assert callable(UML2_WriteVariableAction.__init__)


def test_uml2_writevariableaction_constructor_args():
    sig = inspect.signature(UML2_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_OpaqueExpression)


def test_uml2_opaqueexpression_constructor_exists():
    assert callable(UML2_OpaqueExpression.__init__)


def test_uml2_opaqueexpression_constructor_args():
    sig = inspect.signature(UML2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationInterval)


def test_uml2_durationinterval_constructor_exists():
    assert callable(UML2_DurationInterval.__init__)


def test_uml2_durationinterval_constructor_args():
    sig = inspect.signature(UML2_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterableClassifier)


def test_uml2_parameterableclassifier_constructor_exists():
    assert callable(UML2_ParameterableClassifier.__init__)


def test_uml2_parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2_ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallBehaviorAction)


def test_uml2_callbehavioraction_constructor_exists():
    assert callable(UML2_CallBehaviorAction.__init__)


def test_uml2_callbehavioraction_constructor_args():
    sig = inspect.signature(UML2_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_duration_is_not_abstract():
    assert not inspect.isabstract(UML2_Duration)


def test_uml2_duration_constructor_exists():
    assert callable(UML2_Duration.__init__)


def test_uml2_duration_constructor_args():
    sig = inspect.signature(UML2_Duration.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2_Parameter)


def test_uml2_parameter_constructor_exists():
    assert callable(UML2_Parameter.__init__)


def test_uml2_parameter_constructor_args():
    sig = inspect.signature(UML2_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearStructuralFeatureAction)


def test_uml2_clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2_ClearStructuralFeatureAction.__init__)


def test_uml2_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_artifact_is_not_abstract():
    assert not inspect.isabstract(UML2_Artifact)


def test_uml2_artifact_constructor_exists():
    assert callable(UML2_Artifact.__init__)


def test_uml2_artifact_constructor_args():
    sig = inspect.signature(UML2_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2_Collaboration)


def test_uml2_collaboration_constructor_exists():
    assert callable(UML2_Collaboration.__init__)


def test_uml2_collaboration_constructor_args():
    sig = inspect.signature(UML2_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2_Stereotype)


def test_uml2_stereotype_constructor_exists():
    assert callable(UML2_Stereotype.__init__)


def test_uml2_stereotype_constructor_args():
    sig = inspect.signature(UML2_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interface_is_not_abstract():
    assert not inspect.isabstract(UML2_Interface)


def test_uml2_interface_constructor_exists():
    assert callable(UML2_Interface.__init__)


def test_uml2_interface_constructor_args():
    sig = inspect.signature(UML2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2_component_is_not_abstract():
    assert not inspect.isabstract(UML2_Component)


def test_uml2_component_constructor_exists():
    assert callable(UML2_Component.__init__)


def test_uml2_component_constructor_args():
    sig = inspect.signature(UML2_Component.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_DeploymentSpecification)


def test_uml2_deploymentspecification_constructor_exists():
    assert callable(UML2_DeploymentSpecification.__init__)


def test_uml2_deploymentspecification_constructor_args():
    sig = inspect.signature(UML2_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2_CentralBufferNode)


def test_uml2_centralbuffernode_constructor_exists():
    assert callable(UML2_CentralBufferNode.__init__)


def test_uml2_centralbuffernode_constructor_args():
    sig = inspect.signature(UML2_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_signal_is_not_abstract():
    assert not inspect.isabstract(UML2_Signal)


def test_uml2_signal_constructor_exists():
    assert callable(UML2_Signal.__init__)


def test_uml2_signal_constructor_args():
    sig = inspect.signature(UML2_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_BehavioredClassifier)


def test_uml2_behavioredclassifier_constructor_exists():
    assert callable(UML2_BehavioredClassifier.__init__)


def test_uml2_behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralString)


def test_uml2_literalstring_constructor_exists():
    assert callable(UML2_LiteralString.__init__)


def test_uml2_literalstring_constructor_args():
    sig = inspect.signature(UML2_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2_ExpansionRegion)


def test_uml2_expansionregion_constructor_exists():
    assert callable(UML2_ExpansionRegion.__init__)


def test_uml2_expansionregion_constructor_args():
    sig = inspect.signature(UML2_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2_loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2_LoopNode)


def test_uml2_loopnode_constructor_exists():
    assert callable(UML2_LoopNode.__init__)


def test_uml2_loopnode_constructor_args():
    sig = inspect.signature(UML2_LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ConditionalNode)


def test_uml2_conditionalnode_constructor_exists():
    assert callable(UML2_ConditionalNode.__init__)


def test_uml2_conditionalnode_constructor_args():
    sig = inspect.signature(UML2_ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ApplyFunctionAction)


def test_uml2_applyfunctionaction_constructor_exists():
    assert callable(UML2_ApplyFunctionAction.__init__)


def test_uml2_applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2_ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearAssociationAction)


def test_uml2_clearassociationaction_constructor_exists():
    assert callable(UML2_ClearAssociationAction.__init__)


def test_uml2_clearassociationaction_constructor_args():
    sig = inspect.signature(UML2_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadExtentAction)


def test_uml2_readextentaction_constructor_exists():
    assert callable(UML2_ReadExtentAction.__init__)


def test_uml2_readextentaction_constructor_args():
    sig = inspect.signature(UML2_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2_classifier_is_not_abstract():
    assert not inspect.isabstract(UML2_Classifier)


def test_uml2_classifier_constructor_exists():
    assert callable(UML2_Classifier.__init__)


def test_uml2_classifier_constructor_args():
    sig = inspect.signature(UML2_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkObjectEndAction)


def test_uml2_readlinkobjectendaction_constructor_exists():
    assert callable(UML2_ReadLinkObjectEndAction.__init__)


def test_uml2_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2_AddVariableValueAction_strategy = st.builds(
    UML2_AddVariableValueAction,
)
UML2_RemoveVariableValueAction_strategy = st.builds(
    UML2_RemoveVariableValueAction,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2_ProtocolStateMachine_strategy = st.builds(
    UML2_ProtocolStateMachine,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2_Class_strategy = st.builds(
    UML2_Class,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2_LiteralNull_strategy = st.builds(
    UML2_LiteralNull,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UML2_DestroyLinkAction_strategy = st.builds(
    UML2_DestroyLinkAction,
)
UML2_CreateLinkAction_strategy = st.builds(
    UML2_CreateLinkAction,
)
DataType_strategy = st.builds(
    DataType,
)
UML2_Enumeration_strategy = st.builds(
    UML2_Enumeration,
)
UML2_PrimitiveType_strategy = st.builds(
    UML2_PrimitiveType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
UML2_ValueSpecification_strategy = st.builds(
    UML2_ValueSpecification,
)
UML2_Operation_strategy = st.builds(
    UML2_Operation,
)
UML2_Variable_strategy = st.builds(
    UML2_Variable,
)
UML2_StructuralFeature_strategy = st.builds(
    UML2_StructuralFeature,
)
CallAction_strategy = st.builds(
    CallAction,
)
UML2_CallOperationAction_strategy = st.builds(
    UML2_CallOperationAction,
)
Interval_strategy = st.builds(
    Interval,
)
UML2_TimeInterval_strategy = st.builds(
    UML2_TimeInterval,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2_Activity_strategy = st.builds(
    UML2_Activity,
)
UML2_StateMachine_strategy = st.builds(
    UML2_StateMachine,
)
Class_strategy = st.builds(
    Class,
)
UML2_Behavior_strategy = st.builds(
    UML2_Behavior,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2_ReadLinkAction_strategy = st.builds(
    UML2_ReadLinkAction,
)
Association_strategy = st.builds(
    Association,
)
UML2_AssociationClass_strategy = st.builds(
    UML2_AssociationClass,
)
UML2_Extension_strategy = st.builds(
    UML2_Extension,
)
Property_strategy = st.builds(
    Property,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UML2_ReadVariableAction_strategy = st.builds(
    UML2_ReadVariableAction,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2_Pin_strategy = st.builds(
    UML2_Pin,
)
UML2_ActivityParameterNode_strategy = st.builds(
    UML2_ActivityParameterNode,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UML2_CallAction_strategy = st.builds(
    UML2_CallAction,
)
UML2_SendSignalAction_strategy = st.builds(
    UML2_SendSignalAction,
)
UML2_BroadcastSignalAction_strategy = st.builds(
    UML2_BroadcastSignalAction,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2_EncapsulatedClassifier_strategy = st.builds(
    UML2_EncapsulatedClassifier,
)
Pin_strategy = st.builds(
    Pin,
)
UML2_InputPin_strategy = st.builds(
    UML2_InputPin,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2_LiteralSpecification_strategy = st.builds(
    UML2_LiteralSpecification,
)
UML2_Interval_strategy = st.builds(
    UML2_Interval,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2_DataStoreNode_strategy = st.builds(
    UML2_DataStoreNode,
)
UML2_OutputPin_strategy = st.builds(
    UML2_OutputPin,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2_AddStructuralFeatureValueAction_strategy = st.builds(
    UML2_AddStructuralFeatureValueAction,
)
UML2_DurationObservationAction_strategy = st.builds(
    UML2_DurationObservationAction,
)
UML2_RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2_RemoveStructuralFeatureValueAction,
)
UML2_TimeObservationAction_strategy = st.builds(
    UML2_TimeObservationAction,
)
Action_strategy = st.builds(
    Action,
)
UML2_AcceptEventAction_strategy = st.builds(
    UML2_AcceptEventAction,
)
UML2_DestroyObjectAction_strategy = st.builds(
    UML2_DestroyObjectAction,
)
UML2_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2_ReadLinkObjectEndQualifierAction,
)
UML2_LinkAction_strategy = st.builds(
    UML2_LinkAction,
)
UML2_VariableAction_strategy = st.builds(
    UML2_VariableAction,
)
UML2_CreateObjectAction_strategy = st.builds(
    UML2_CreateObjectAction,
)
UML2_RaiseExceptionAction_strategy = st.builds(
    UML2_RaiseExceptionAction,
)
UML2_ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2_ReadIsClassifiedObjectAction,
)
UML2_StartOwnedBehaviorAction_strategy = st.builds(
    UML2_StartOwnedBehaviorAction,
)
UML2_ReclassifyObjectAction_strategy = st.builds(
    UML2_ReclassifyObjectAction,
)
UML2_ReadSelfAction_strategy = st.builds(
    UML2_ReadSelfAction,
)
UML2_StructuralFeatureAction_strategy = st.builds(
    UML2_StructuralFeatureAction,
)
UML2_StructuredActivityNode_strategy = st.builds(
    UML2_StructuredActivityNode,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2_TemplateableClassifier_strategy = st.builds(
    UML2_TemplateableClassifier,
)
UML2_Actor_strategy = st.builds(
    UML2_Actor,
)
UML2_DataType_strategy = st.builds(
    UML2_DataType,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2_ReadStructuralFeatureAction_strategy = st.builds(
    UML2_ReadStructuralFeatureAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UML2_AcceptCallAction_strategy = st.builds(
    UML2_AcceptCallAction,
)
Node_strategy = st.builds(
    Node,
)
UML2_Device_strategy = st.builds(
    UML2_Device,
)
UML2_TimeExpression_strategy = st.builds(
    UML2_TimeExpression,
)
UML2_StructuredClassifier_strategy = st.builds(
    UML2_StructuredClassifier,
)
UML2_Action_strategy = st.builds(
    UML2_Action,
)
UML2_SendObjectAction_strategy = st.builds(
    UML2_SendObjectAction,
)
UML2_InstanceValue_strategy = st.builds(
    UML2_InstanceValue,
)
UML2_Node_strategy = st.builds(
    UML2_Node,
)
UML2_CommunicationPath_strategy = st.builds(
    UML2_CommunicationPath,
)
UML2_LiteralBoolean_strategy = st.builds(
    UML2_LiteralBoolean,
)
UML2_ReplyAction_strategy = st.builds(
    UML2_ReplyAction,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2_Expression_strategy = st.builds(
    UML2_Expression,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2_ValuePin_strategy = st.builds(
    UML2_ValuePin,
)
UML2_ExpansionNode_strategy = st.builds(
    UML2_ExpansionNode,
)
UML2_Interaction_strategy = st.builds(
    UML2_Interaction,
)
UML2_WriteLinkAction_strategy = st.builds(
    UML2_WriteLinkAction,
)
UML2_LiteralUnlimitedNatural_strategy = st.builds(
    UML2_LiteralUnlimitedNatural,
)
UML2_InformationItem_strategy = st.builds(
    UML2_InformationItem,
)
UML2_ClearVariableAction_strategy = st.builds(
    UML2_ClearVariableAction,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UML2_CreateLinkObjectAction_strategy = st.builds(
    UML2_CreateLinkObjectAction,
)
UML2_TestIdentityAction_strategy = st.builds(
    UML2_TestIdentityAction,
)
UML2_UseCase_strategy = st.builds(
    UML2_UseCase,
)
UML2_Association_strategy = st.builds(
    UML2_Association,
)
UML2_LiteralInteger_strategy = st.builds(
    UML2_LiteralInteger,
)
UML2_WriteStructuralFeatureAction_strategy = st.builds(
    UML2_WriteStructuralFeatureAction,
)
UML2_ExecutionEnvironment_strategy = st.builds(
    UML2_ExecutionEnvironment,
)
UML2_Type_strategy = st.builds(
    UML2_Type,
)
UML2_TypedElement_strategy = st.builds(
    UML2_TypedElement,
)
UML2_ObjectNode_strategy = st.builds(
    UML2_ObjectNode,
)
UML2_InvocationAction_strategy = st.builds(
    UML2_InvocationAction,
)
UML2_WriteVariableAction_strategy = st.builds(
    UML2_WriteVariableAction,
)
UML2_OpaqueExpression_strategy = st.builds(
    UML2_OpaqueExpression,
)
UML2_DurationInterval_strategy = st.builds(
    UML2_DurationInterval,
)
UML2_ParameterableClassifier_strategy = st.builds(
    UML2_ParameterableClassifier,
)
UML2_CallBehaviorAction_strategy = st.builds(
    UML2_CallBehaviorAction,
)
UML2_Duration_strategy = st.builds(
    UML2_Duration,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
)
UML2_Parameter_strategy = st.builds(
    UML2_Parameter,
)
UML2_ClearStructuralFeatureAction_strategy = st.builds(
    UML2_ClearStructuralFeatureAction,
)
UML2_Artifact_strategy = st.builds(
    UML2_Artifact,
)
UML2_Collaboration_strategy = st.builds(
    UML2_Collaboration,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
UML2_Stereotype_strategy = st.builds(
    UML2_Stereotype,
)
UML2_Interface_strategy = st.builds(
    UML2_Interface,
)
UML2_Component_strategy = st.builds(
    UML2_Component,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2_DeploymentSpecification_strategy = st.builds(
    UML2_DeploymentSpecification,
)
UML2_CentralBufferNode_strategy = st.builds(
    UML2_CentralBufferNode,
)
UML2_Signal_strategy = st.builds(
    UML2_Signal,
)
UML2_BehavioredClassifier_strategy = st.builds(
    UML2_BehavioredClassifier,
)
UML2_LiteralString_strategy = st.builds(
    UML2_LiteralString,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UML2_ExpansionRegion_strategy = st.builds(
    UML2_ExpansionRegion,
)
UML2_LoopNode_strategy = st.builds(
    UML2_LoopNode,
)
UML2_ConditionalNode_strategy = st.builds(
    UML2_ConditionalNode,
)
UML2_ApplyFunctionAction_strategy = st.builds(
    UML2_ApplyFunctionAction,
)
UML2_ClearAssociationAction_strategy = st.builds(
    UML2_ClearAssociationAction,
)
UML2_ReadExtentAction_strategy = st.builds(
    UML2_ReadExtentAction,
)
Type_strategy = st.builds(
    Type,
)
UML2_Classifier_strategy = st.builds(
    UML2_Classifier,
)
UML2_ReadLinkObjectEndAction_strategy = st.builds(
    UML2_ReadLinkObjectEndAction,
)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_AddVariableValueAction)

@given(instance=UML2_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_RemoveVariableValueAction)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2_Class_strategy)
@settings(max_examples=50)
def test_uml2_class_instantiation(instance):
    assert isinstance(instance, UML2_Class)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2_literalnull_instantiation(instance):
    assert isinstance(instance, UML2_LiteralNull)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UML2_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2_DestroyLinkAction)

@given(instance=UML2_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateLinkAction)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2_Enumeration_strategy)
@settings(max_examples=50)
def test_uml2_enumeration_instantiation(instance):
    assert isinstance(instance, UML2_Enumeration)

@given(instance=UML2_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2_primitivetype_instantiation(instance):
    assert isinstance(instance, UML2_PrimitiveType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=UML2_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2_valuespecification_instantiation(instance):
    assert isinstance(instance, UML2_ValueSpecification)

@given(instance=UML2_Operation_strategy)
@settings(max_examples=50)
def test_uml2_operation_instantiation(instance):
    assert isinstance(instance, UML2_Operation)

@given(instance=UML2_Variable_strategy)
@settings(max_examples=50)
def test_uml2_variable_instantiation(instance):
    assert isinstance(instance, UML2_Variable)

@given(instance=UML2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeature)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UML2_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2_calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2_CallOperationAction)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2_timeinterval_instantiation(instance):
    assert isinstance(instance, UML2_TimeInterval)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2_Activity_strategy)
@settings(max_examples=50)
def test_uml2_activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)

@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2_statemachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2_Behavior_strategy)
@settings(max_examples=50)
def test_uml2_behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkAction)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2_associationclass_instantiation(instance):
    assert isinstance(instance, UML2_AssociationClass)

@given(instance=UML2_Extension_strategy)
@settings(max_examples=50)
def test_uml2_extension_instantiation(instance):
    assert isinstance(instance, UML2_Extension)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UML2_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadVariableAction)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2_Pin_strategy)
@settings(max_examples=50)
def test_uml2_pin_instantiation(instance):
    assert isinstance(instance, UML2_Pin)

@given(instance=UML2_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2_activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2_ActivityParameterNode)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UML2_CallAction_strategy)
@settings(max_examples=50)
def test_uml2_callaction_instantiation(instance):
    assert isinstance(instance, UML2_CallAction)

@given(instance=UML2_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2_sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2_SendSignalAction)

@given(instance=UML2_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2_BroadcastSignalAction)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2_EncapsulatedClassifier)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2_InputPin_strategy)
@settings(max_examples=50)
def test_uml2_inputpin_instantiation(instance):
    assert isinstance(instance, UML2_InputPin)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2_literalspecification_instantiation(instance):
    assert isinstance(instance, UML2_LiteralSpecification)

@given(instance=UML2_Interval_strategy)
@settings(max_examples=50)
def test_uml2_interval_instantiation(instance):
    assert isinstance(instance, UML2_Interval)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2_datastorenode_instantiation(instance):
    assert isinstance(instance, UML2_DataStoreNode)

@given(instance=UML2_OutputPin_strategy)
@settings(max_examples=50)
def test_uml2_outputpin_instantiation(instance):
    assert isinstance(instance, UML2_OutputPin)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_AddStructuralFeatureValueAction)

@given(instance=UML2_DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2_durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2_DurationObservationAction)

@given(instance=UML2_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_RemoveStructuralFeatureValueAction)

@given(instance=UML2_TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2_timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2_TimeObservationAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2_accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2_AcceptEventAction)

@given(instance=UML2_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_DestroyObjectAction)

@given(instance=UML2_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkObjectEndQualifierAction)

@given(instance=UML2_LinkAction_strategy)
@settings(max_examples=50)
def test_uml2_linkaction_instantiation(instance):
    assert isinstance(instance, UML2_LinkAction)

@given(instance=UML2_VariableAction_strategy)
@settings(max_examples=50)
def test_uml2_variableaction_instantiation(instance):
    assert isinstance(instance, UML2_VariableAction)

@given(instance=UML2_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateObjectAction)

@given(instance=UML2_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2_RaiseExceptionAction)

@given(instance=UML2_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadIsClassifiedObjectAction)

@given(instance=UML2_StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2_startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2_StartOwnedBehaviorAction)

@given(instance=UML2_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_ReclassifyObjectAction)

@given(instance=UML2_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2_readselfaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadSelfAction)

@given(instance=UML2_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeatureAction)

@given(instance=UML2_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2_StructuredActivityNode)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2_TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_TemplateableClassifier)

@given(instance=UML2_Actor_strategy)
@settings(max_examples=50)
def test_uml2_actor_instantiation(instance):
    assert isinstance(instance, UML2_Actor)

@given(instance=UML2_DataType_strategy)
@settings(max_examples=50)
def test_uml2_datatype_instantiation(instance):
    assert isinstance(instance, UML2_DataType)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadStructuralFeatureAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UML2_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2_acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2_AcceptCallAction)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2_Device_strategy)
@settings(max_examples=50)
def test_uml2_device_instantiation(instance):
    assert isinstance(instance, UML2_Device)

@given(instance=UML2_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2_timeexpression_instantiation(instance):
    assert isinstance(instance, UML2_TimeExpression)

@given(instance=UML2_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_StructuredClassifier)

@given(instance=UML2_Action_strategy)
@settings(max_examples=50)
def test_uml2_action_instantiation(instance):
    assert isinstance(instance, UML2_Action)

@given(instance=UML2_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_SendObjectAction)

@given(instance=UML2_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2_instancevalue_instantiation(instance):
    assert isinstance(instance, UML2_InstanceValue)

@given(instance=UML2_Node_strategy)
@settings(max_examples=50)
def test_uml2_node_instantiation(instance):
    assert isinstance(instance, UML2_Node)

@given(instance=UML2_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2_CommunicationPath)

@given(instance=UML2_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2_literalboolean_instantiation(instance):
    assert isinstance(instance, UML2_LiteralBoolean)

@given(instance=UML2_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2_replyaction_instantiation(instance):
    assert isinstance(instance, UML2_ReplyAction)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2_Expression_strategy)
@settings(max_examples=50)
def test_uml2_expression_instantiation(instance):
    assert isinstance(instance, UML2_Expression)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2_ValuePin_strategy)
@settings(max_examples=50)
def test_uml2_valuepin_instantiation(instance):
    assert isinstance(instance, UML2_ValuePin)

@given(instance=UML2_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2_expansionnode_instantiation(instance):
    assert isinstance(instance, UML2_ExpansionNode)

@given(instance=UML2_Interaction_strategy)
@settings(max_examples=50)
def test_uml2_interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)

@given(instance=UML2_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteLinkAction)

@given(instance=UML2_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2_LiteralUnlimitedNatural)

@given(instance=UML2_InformationItem_strategy)
@settings(max_examples=50)
def test_uml2_informationitem_instantiation(instance):
    assert isinstance(instance, UML2_InformationItem)

@given(instance=UML2_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearVariableAction)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UML2_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateLinkObjectAction)

@given(instance=UML2_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2_testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2_TestIdentityAction)

@given(instance=UML2_UseCase_strategy)
@settings(max_examples=50)
def test_uml2_usecase_instantiation(instance):
    assert isinstance(instance, UML2_UseCase)

@given(instance=UML2_Association_strategy)
@settings(max_examples=50)
def test_uml2_association_instantiation(instance):
    assert isinstance(instance, UML2_Association)

@given(instance=UML2_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2_literalinteger_instantiation(instance):
    assert isinstance(instance, UML2_LiteralInteger)

@given(instance=UML2_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteStructuralFeatureAction)

@given(instance=UML2_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2_executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2_ExecutionEnvironment)

@given(instance=UML2_Type_strategy)
@settings(max_examples=50)
def test_uml2_type_instantiation(instance):
    assert isinstance(instance, UML2_Type)

@given(instance=UML2_TypedElement_strategy)
@settings(max_examples=50)
def test_uml2_typedelement_instantiation(instance):
    assert isinstance(instance, UML2_TypedElement)

@given(instance=UML2_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2_objectnode_instantiation(instance):
    assert isinstance(instance, UML2_ObjectNode)

@given(instance=UML2_InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2_invocationaction_instantiation(instance):
    assert isinstance(instance, UML2_InvocationAction)

@given(instance=UML2_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteVariableAction)

@given(instance=UML2_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2_OpaqueExpression)

@given(instance=UML2_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2_durationinterval_instantiation(instance):
    assert isinstance(instance, UML2_DurationInterval)

@given(instance=UML2_ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_ParameterableClassifier)

@given(instance=UML2_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2_callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2_CallBehaviorAction)

@given(instance=UML2_Duration_strategy)
@settings(max_examples=50)
def test_uml2_duration_instantiation(instance):
    assert isinstance(instance, UML2_Duration)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)

@given(instance=UML2_Parameter_strategy)
@settings(max_examples=50)
def test_uml2_parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)

@given(instance=UML2_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearStructuralFeatureAction)

@given(instance=UML2_Artifact_strategy)
@settings(max_examples=50)
def test_uml2_artifact_instantiation(instance):
    assert isinstance(instance, UML2_Artifact)

@given(instance=UML2_Collaboration_strategy)
@settings(max_examples=50)
def test_uml2_collaboration_instantiation(instance):
    assert isinstance(instance, UML2_Collaboration)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)

@given(instance=UML2_Stereotype_strategy)
@settings(max_examples=50)
def test_uml2_stereotype_instantiation(instance):
    assert isinstance(instance, UML2_Stereotype)

@given(instance=UML2_Interface_strategy)
@settings(max_examples=50)
def test_uml2_interface_instantiation(instance):
    assert isinstance(instance, UML2_Interface)

@given(instance=UML2_Component_strategy)
@settings(max_examples=50)
def test_uml2_component_instantiation(instance):
    assert isinstance(instance, UML2_Component)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2_deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2_DeploymentSpecification)

@given(instance=UML2_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2_centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2_CentralBufferNode)

@given(instance=UML2_Signal_strategy)
@settings(max_examples=50)
def test_uml2_signal_instantiation(instance):
    assert isinstance(instance, UML2_Signal)

@given(instance=UML2_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_BehavioredClassifier)

@given(instance=UML2_LiteralString_strategy)
@settings(max_examples=50)
def test_uml2_literalstring_instantiation(instance):
    assert isinstance(instance, UML2_LiteralString)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UML2_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2_expansionregion_instantiation(instance):
    assert isinstance(instance, UML2_ExpansionRegion)

@given(instance=UML2_LoopNode_strategy)
@settings(max_examples=50)
def test_uml2_loopnode_instantiation(instance):
    assert isinstance(instance, UML2_LoopNode)

@given(instance=UML2_ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2_conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2_ConditionalNode)

@given(instance=UML2_ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2_applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2_ApplyFunctionAction)

@given(instance=UML2_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2_clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearAssociationAction)

@given(instance=UML2_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2_readextentaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadExtentAction)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UML2_Classifier_strategy)
@settings(max_examples=50)
def test_uml2_classifier_instantiation(instance):
    assert isinstance(instance, UML2_Classifier)

@given(instance=UML2_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkObjectEndAction)
