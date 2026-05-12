import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VariableAction,
    Actions_StructuredActions_ReadVariableAction,
    Actions_StructuredActions_Variable,
    Variable,
    CreateLinkAction,
    Actions_CompleteActions_CreateLinkObjectAction,
    Actions_StructuredActions_ClearVariableAction,
    WriteVariableAction,
    Actions_StructuredActions_RemoveVariableValueAction,
    Actions_StructuredActions_AddVariableValueAction,
    Actions_StructuredActions_WriteVariableAction,
    Actions_CompleteActions_ReadlsClassifiedObjectAction,
    Trigger,
    Actions_CompleteActions_Trigger,
    AcceptEventAction,
    Actions_CompleteActions_AcceptCallAction,
    Actions_IntermediateActions_Property,
    QualifierValue,
    Property,
    Element,
    Actions_CompleteActions_QualifierValue,
    Actions_IntermediateActions_LinkEndData,
    LinkEndData,
    Actions_IntermediateActions_LinkEndDestructionData,
    WriteStructuralFeatureAction,
    Actions_IntermediateActions_RemoveStructuralFeatureValueAction,
    Actions_IntermediateActions_AddStructuralFeatureValueAction,
    Actions_IntermediateActions_Element,
    Actions_IntermediateActions_LinkEndCreationData,
    WriteLinkAction,
    Actions_IntermediateActions_DestroyLinkAction,
    Actions_IntermediateActions_CreateLinkAction,
    LinkAction,
    Actions_IntermediateActions_WriteLinkAction,
    Actions_IntermediateActions_ReadLinkAction,
    StructuralFeature,
    StructuralFeatureAction,
    Actions_IntermediateActions_WriteStructuralFeatureAction,
    Actions_IntermediateActions_ClearStructuralFeatureAction,
    Actions_IntermediateActions_ReadStructuralFeatureAction,
    Actions_IntermediateActions_StructuralFeature,
    Signal,
    Actions_BasicActions_Operation,
    Operation,
    Actions_BasicActions_CallOperationAction,
    Actions_BasicActions_Behavior,
    Behavior,
    CallAction,
    Actions_CompleteActions_StartObjectBehaviorAction,
    Actions_BasicActions_CallBehaviorAction,
    InvocationAction,
    Actions_BasicActions_SendSignalAction,
    Actions_BasicActions_CallAction,
    Actions_IntermediateActions_SendObjectAction,
    Actions_IntermediateActions_BroadcastSignalAction,
    Actions_BasicActions_Signal,
    Pin,
    Actions_BasicActions_InputPin,
    Action,
    Actions_IntermediateActions_LinkAction,
    Actions_CompleteActions_ReadLinkObjectEndQualifierAction,
    Actions_CompleteActions_ReplyAction,
    Actions_CompleteActions_ReclassifyObjectAction,
    Actions_CompleteActions_ReduceAction,
    Actions_IntermediateActions_StructuralFeatureAction,
    Actions_CompleteActions_ReadExtendAction,
    Actions_CompleteActions_UnmarshallAction,
    Actions_IntermediateActions_CreateObjectAction,
    Actions_IntermediateActions_TestIdentityAction,
    Actions_CompleteActions_AcceptEventAction,
    Actions_StructuredActions_RaiseExceptionAction,
    Actions_CompleteActions_ReadLinkObjectEndAction,
    Actions_CompleteActions_StartClassifierBehaviorAction,
    Actions_IntermediateActions_DestroyObjectAction,
    Actions_StructuredActions_VariableAction,
    Actions_IntermediateActions_ValueSpecificationAction,
    Actions_IntermediateActions_ReadSelfAction,
    Actions_BasicActions_OpaqueAction,
    Actions_BasicActions_Classifier,
    Actions_BasicActions_NamedElement,
    OutputPin,
    InputPin,
    Actions_StructuredActions_ActionInputPin,
    Classifier,
    NamedElement,
    Actions_BasicActions_Action,
    Actions_BasicActions_InvocationAction,
    Actions_BasicActions_ValueSpecification,
    ValueSpecification,
    Actions_BasicActions_ValuePin,
    Actions_BasicActions_TypedElement,
    Actions_BasicActions_MultiplicityElement,
    BasicActions_MultiplicityElement,
    BasicActions_TypedElement,
    Actions_BasicActions_Pin,
    Actions_BasicActions_OutputPin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_ReadVariableAction)


def test_actions_structuredactions_readvariableaction_constructor_exists():
    assert callable(Actions_StructuredActions_ReadVariableAction.__init__)


def test_actions_structuredactions_readvariableaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_variable_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_Variable)


def test_actions_structuredactions_variable_constructor_exists():
    assert callable(Actions_StructuredActions_Variable.__init__)


def test_actions_structuredactions_variable_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_Variable.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_CreateLinkObjectAction)


def test_actions_completeactions_createlinkobjectaction_constructor_exists():
    assert callable(Actions_CompleteActions_CreateLinkObjectAction.__init__)


def test_actions_completeactions_createlinkobjectaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_ClearVariableAction)


def test_actions_structuredactions_clearvariableaction_constructor_exists():
    assert callable(Actions_StructuredActions_ClearVariableAction.__init__)


def test_actions_structuredactions_clearvariableaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_RemoveVariableValueAction)


def test_actions_structuredactions_removevariablevalueaction_constructor_exists():
    assert callable(Actions_StructuredActions_RemoveVariableValueAction.__init__)


def test_actions_structuredactions_removevariablevalueaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_AddVariableValueAction)


def test_actions_structuredactions_addvariablevalueaction_constructor_exists():
    assert callable(Actions_StructuredActions_AddVariableValueAction.__init__)


def test_actions_structuredactions_addvariablevalueaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_WriteVariableAction)


def test_actions_structuredactions_writevariableaction_constructor_exists():
    assert callable(Actions_StructuredActions_WriteVariableAction.__init__)


def test_actions_structuredactions_writevariableaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReadlsClassifiedObjectAction)


def test_actions_completeactions_readlsclassifiedobjectaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReadlsClassifiedObjectAction.__init__)


def test_actions_completeactions_readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_trigger_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_Trigger)


def test_actions_completeactions_trigger_constructor_exists():
    assert callable(Actions_CompleteActions_Trigger.__init__)


def test_actions_completeactions_trigger_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_AcceptCallAction)


def test_actions_completeactions_acceptcallaction_constructor_exists():
    assert callable(Actions_CompleteActions_AcceptCallAction.__init__)


def test_actions_completeactions_acceptcallaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_property_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_Property)


def test_actions_intermediateactions_property_constructor_exists():
    assert callable(Actions_IntermediateActions_Property.__init__)


def test_actions_intermediateactions_property_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_Property.__init__)
    params = list(sig.parameters.keys())



def test_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(QualifierValue)


def test_qualifiervalue_constructor_exists():
    assert callable(QualifierValue.__init__)


def test_qualifiervalue_constructor_args():
    sig = inspect.signature(QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_QualifierValue)


def test_actions_completeactions_qualifiervalue_constructor_exists():
    assert callable(Actions_CompleteActions_QualifierValue.__init__)


def test_actions_completeactions_qualifiervalue_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_LinkEndData)


def test_actions_intermediateactions_linkenddata_constructor_exists():
    assert callable(Actions_IntermediateActions_LinkEndData.__init__)


def test_actions_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_LinkEndDestructionData)


def test_actions_intermediateactions_linkenddestructiondata_constructor_exists():
    assert callable(Actions_IntermediateActions_LinkEndDestructionData.__init__)


def test_actions_intermediateactions_linkenddestructiondata_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_actions_intermediateactions_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(Actions_IntermediateActions_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in Actions_IntermediateActions_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_RemoveStructuralFeatureValueAction)


def test_actions_intermediateactions_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(Actions_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)


def test_actions_intermediateactions_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_AddStructuralFeatureValueAction)


def test_actions_intermediateactions_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(Actions_IntermediateActions_AddStructuralFeatureValueAction.__init__)


def test_actions_intermediateactions_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_element_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_Element)


def test_actions_intermediateactions_element_constructor_exists():
    assert callable(Actions_IntermediateActions_Element.__init__)


def test_actions_intermediateactions_element_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_Element.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_LinkEndCreationData)


def test_actions_intermediateactions_linkendcreationdata_constructor_exists():
    assert callable(Actions_IntermediateActions_LinkEndCreationData.__init__)


def test_actions_intermediateactions_linkendcreationdata_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actions_intermediateactions_linkendcreationdata_has_isReplaceAll():
    assert hasattr(Actions_IntermediateActions_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in Actions_IntermediateActions_LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_DestroyLinkAction)


def test_actions_intermediateactions_destroylinkaction_constructor_exists():
    assert callable(Actions_IntermediateActions_DestroyLinkAction.__init__)


def test_actions_intermediateactions_destroylinkaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_CreateLinkAction)


def test_actions_intermediateactions_createlinkaction_constructor_exists():
    assert callable(Actions_IntermediateActions_CreateLinkAction.__init__)


def test_actions_intermediateactions_createlinkaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_WriteLinkAction)


def test_actions_intermediateactions_writelinkaction_constructor_exists():
    assert callable(Actions_IntermediateActions_WriteLinkAction.__init__)


def test_actions_intermediateactions_writelinkaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_ReadLinkAction)


def test_actions_intermediateactions_readlinkaction_constructor_exists():
    assert callable(Actions_IntermediateActions_ReadLinkAction.__init__)


def test_actions_intermediateactions_readlinkaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_WriteStructuralFeatureAction)


def test_actions_intermediateactions_writestructuralfeatureaction_constructor_exists():
    assert callable(Actions_IntermediateActions_WriteStructuralFeatureAction.__init__)


def test_actions_intermediateactions_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_ClearStructuralFeatureAction)


def test_actions_intermediateactions_clearstructuralfeatureaction_constructor_exists():
    assert callable(Actions_IntermediateActions_ClearStructuralFeatureAction.__init__)


def test_actions_intermediateactions_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_ReadStructuralFeatureAction)


def test_actions_intermediateactions_readstructuralfeatureaction_constructor_exists():
    assert callable(Actions_IntermediateActions_ReadStructuralFeatureAction.__init__)


def test_actions_intermediateactions_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_StructuralFeature)


def test_actions_intermediateactions_structuralfeature_constructor_exists():
    assert callable(Actions_IntermediateActions_StructuralFeature.__init__)


def test_actions_intermediateactions_structuralfeature_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_operation_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Operation)


def test_actions_basicactions_operation_constructor_exists():
    assert callable(Actions_BasicActions_Operation.__init__)


def test_actions_basicactions_operation_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Operation.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_CallOperationAction)


def test_actions_basicactions_calloperationaction_constructor_exists():
    assert callable(Actions_BasicActions_CallOperationAction.__init__)


def test_actions_basicactions_calloperationaction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_behavior_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Behavior)


def test_actions_basicactions_behavior_constructor_exists():
    assert callable(Actions_BasicActions_Behavior.__init__)


def test_actions_basicactions_behavior_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_StartObjectBehaviorAction)


def test_actions_completeactions_startobjectbehavioraction_constructor_exists():
    assert callable(Actions_CompleteActions_StartObjectBehaviorAction.__init__)


def test_actions_completeactions_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_CallBehaviorAction)


def test_actions_basicactions_callbehavioraction_constructor_exists():
    assert callable(Actions_BasicActions_CallBehaviorAction.__init__)


def test_actions_basicactions_callbehavioraction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_SendSignalAction)


def test_actions_basicactions_sendsignalaction_constructor_exists():
    assert callable(Actions_BasicActions_SendSignalAction.__init__)


def test_actions_basicactions_sendsignalaction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_callaction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_CallAction)


def test_actions_basicactions_callaction_constructor_exists():
    assert callable(Actions_BasicActions_CallAction.__init__)


def test_actions_basicactions_callaction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_actions_basicactions_callaction_has_isSynchronous():
    assert hasattr(Actions_BasicActions_CallAction, "isSynchronous")
    descriptor = None
    for klass in Actions_BasicActions_CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_actions_intermediateactions_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_SendObjectAction)


def test_actions_intermediateactions_sendobjectaction_constructor_exists():
    assert callable(Actions_IntermediateActions_SendObjectAction.__init__)


def test_actions_intermediateactions_sendobjectaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_BroadcastSignalAction)


def test_actions_intermediateactions_broadcastsignalaction_constructor_exists():
    assert callable(Actions_IntermediateActions_BroadcastSignalAction.__init__)


def test_actions_intermediateactions_broadcastsignalaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_signal_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Signal)


def test_actions_basicactions_signal_constructor_exists():
    assert callable(Actions_BasicActions_Signal.__init__)


def test_actions_basicactions_signal_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Signal.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_InputPin)


def test_actions_basicactions_inputpin_constructor_exists():
    assert callable(Actions_BasicActions_InputPin.__init__)


def test_actions_basicactions_inputpin_constructor_args():
    sig = inspect.signature(Actions_BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_linkaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_LinkAction)


def test_actions_intermediateactions_linkaction_constructor_exists():
    assert callable(Actions_IntermediateActions_LinkAction.__init__)


def test_actions_intermediateactions_linkaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReadLinkObjectEndQualifierAction)


def test_actions_completeactions_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(Actions_CompleteActions_ReadLinkObjectEndQualifierAction.__init__)


def test_actions_completeactions_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_replyaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReplyAction)


def test_actions_completeactions_replyaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReplyAction.__init__)


def test_actions_completeactions_replyaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReclassifyObjectAction)


def test_actions_completeactions_reclassifyobjectaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReclassifyObjectAction.__init__)


def test_actions_completeactions_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actions_completeactions_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(Actions_CompleteActions_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in Actions_CompleteActions_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_actions_completeactions_reduceaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReduceAction)


def test_actions_completeactions_reduceaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReduceAction.__init__)


def test_actions_completeactions_reduceaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_actions_completeactions_reduceaction_has_isOrdered():
    assert hasattr(Actions_CompleteActions_ReduceAction, "isOrdered")
    descriptor = None
    for klass in Actions_CompleteActions_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_actions_intermediateactions_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_StructuralFeatureAction)


def test_actions_intermediateactions_structuralfeatureaction_constructor_exists():
    assert callable(Actions_IntermediateActions_StructuralFeatureAction.__init__)


def test_actions_intermediateactions_structuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_readextendaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReadExtendAction)


def test_actions_completeactions_readextendaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReadExtendAction.__init__)


def test_actions_completeactions_readextendaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_UnmarshallAction)


def test_actions_completeactions_unmarshallaction_constructor_exists():
    assert callable(Actions_CompleteActions_UnmarshallAction.__init__)


def test_actions_completeactions_unmarshallaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_CreateObjectAction)


def test_actions_intermediateactions_createobjectaction_constructor_exists():
    assert callable(Actions_IntermediateActions_CreateObjectAction.__init__)


def test_actions_intermediateactions_createobjectaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_TestIdentityAction)


def test_actions_intermediateactions_testidentityaction_constructor_exists():
    assert callable(Actions_IntermediateActions_TestIdentityAction.__init__)


def test_actions_intermediateactions_testidentityaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_AcceptEventAction)


def test_actions_completeactions_accepteventaction_constructor_exists():
    assert callable(Actions_CompleteActions_AcceptEventAction.__init__)


def test_actions_completeactions_accepteventaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_actions_completeactions_accepteventaction_has_isUnmarshall():
    assert hasattr(Actions_CompleteActions_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in Actions_CompleteActions_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_actions_structuredactions_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_RaiseExceptionAction)


def test_actions_structuredactions_raiseexceptionaction_constructor_exists():
    assert callable(Actions_StructuredActions_RaiseExceptionAction.__init__)


def test_actions_structuredactions_raiseexceptionaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_ReadLinkObjectEndAction)


def test_actions_completeactions_readlinkobjectendaction_constructor_exists():
    assert callable(Actions_CompleteActions_ReadLinkObjectEndAction.__init__)


def test_actions_completeactions_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_completeactions_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions_CompleteActions_StartClassifierBehaviorAction)


def test_actions_completeactions_startclassifierbehavioraction_constructor_exists():
    assert callable(Actions_CompleteActions_StartClassifierBehaviorAction.__init__)


def test_actions_completeactions_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(Actions_CompleteActions_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_DestroyObjectAction)


def test_actions_intermediateactions_destroyobjectaction_constructor_exists():
    assert callable(Actions_IntermediateActions_DestroyObjectAction.__init__)


def test_actions_intermediateactions_destroyobjectaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_variableaction_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_VariableAction)


def test_actions_structuredactions_variableaction_constructor_exists():
    assert callable(Actions_StructuredActions_VariableAction.__init__)


def test_actions_structuredactions_variableaction_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_ValueSpecificationAction)


def test_actions_intermediateactions_valuespecificationaction_constructor_exists():
    assert callable(Actions_IntermediateActions_ValueSpecificationAction.__init__)


def test_actions_intermediateactions_valuespecificationaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_intermediateactions_readselfaction_is_not_abstract():
    assert not inspect.isabstract(Actions_IntermediateActions_ReadSelfAction)


def test_actions_intermediateactions_readselfaction_constructor_exists():
    assert callable(Actions_IntermediateActions_ReadSelfAction.__init__)


def test_actions_intermediateactions_readselfaction_constructor_args():
    sig = inspect.signature(Actions_IntermediateActions_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_OpaqueAction)


def test_actions_basicactions_opaqueaction_constructor_exists():
    assert callable(Actions_BasicActions_OpaqueAction.__init__)


def test_actions_basicactions_opaqueaction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_actions_basicactions_opaqueaction_has_body():
    assert hasattr(Actions_BasicActions_OpaqueAction, "body")
    descriptor = None
    for klass in Actions_BasicActions_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_actions_basicactions_opaqueaction_has_language():
    assert hasattr(Actions_BasicActions_OpaqueAction, "language")
    descriptor = None
    for klass in Actions_BasicActions_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_actions_basicactions_classifier_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Classifier)


def test_actions_basicactions_classifier_constructor_exists():
    assert callable(Actions_BasicActions_Classifier.__init__)


def test_actions_basicactions_classifier_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_namedelement_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_NamedElement)


def test_actions_basicactions_namedelement_constructor_exists():
    assert callable(Actions_BasicActions_NamedElement.__init__)


def test_actions_basicactions_namedelement_constructor_args():
    sig = inspect.signature(Actions_BasicActions_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_outputpin_is_not_abstract():
    assert not inspect.isabstract(OutputPin)


def test_outputpin_constructor_exists():
    assert callable(OutputPin.__init__)


def test_outputpin_constructor_args():
    sig = inspect.signature(OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_actions_structuredactions_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(Actions_StructuredActions_ActionInputPin)


def test_actions_structuredactions_actioninputpin_constructor_exists():
    assert callable(Actions_StructuredActions_ActionInputPin.__init__)


def test_actions_structuredactions_actioninputpin_constructor_args():
    sig = inspect.signature(Actions_StructuredActions_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_action_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Action)


def test_actions_basicactions_action_constructor_exists():
    assert callable(Actions_BasicActions_Action.__init__)


def test_actions_basicactions_action_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Action.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_invocationaction_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_InvocationAction)


def test_actions_basicactions_invocationaction_constructor_exists():
    assert callable(Actions_BasicActions_InvocationAction.__init__)


def test_actions_basicactions_invocationaction_constructor_args():
    sig = inspect.signature(Actions_BasicActions_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_ValueSpecification)


def test_actions_basicactions_valuespecification_constructor_exists():
    assert callable(Actions_BasicActions_ValueSpecification.__init__)


def test_actions_basicactions_valuespecification_constructor_args():
    sig = inspect.signature(Actions_BasicActions_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_valuepin_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_ValuePin)


def test_actions_basicactions_valuepin_constructor_exists():
    assert callable(Actions_BasicActions_ValuePin.__init__)


def test_actions_basicactions_valuepin_constructor_args():
    sig = inspect.signature(Actions_BasicActions_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_typedelement_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_TypedElement)


def test_actions_basicactions_typedelement_constructor_exists():
    assert callable(Actions_BasicActions_TypedElement.__init__)


def test_actions_basicactions_typedelement_constructor_args():
    sig = inspect.signature(Actions_BasicActions_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_MultiplicityElement)


def test_actions_basicactions_multiplicityelement_constructor_exists():
    assert callable(Actions_BasicActions_MultiplicityElement.__init__)


def test_actions_basicactions_multiplicityelement_constructor_args():
    sig = inspect.signature(Actions_BasicActions_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(BasicActions_MultiplicityElement)


def test_basicactions_multiplicityelement_constructor_exists():
    assert callable(BasicActions_MultiplicityElement.__init__)


def test_basicactions_multiplicityelement_constructor_args():
    sig = inspect.signature(BasicActions_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_typedelement_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TypedElement)


def test_basicactions_typedelement_constructor_exists():
    assert callable(BasicActions_TypedElement.__init__)


def test_basicactions_typedelement_constructor_args():
    sig = inspect.signature(BasicActions_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_pin_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_Pin)


def test_actions_basicactions_pin_constructor_exists():
    assert callable(Actions_BasicActions_Pin.__init__)


def test_actions_basicactions_pin_constructor_args():
    sig = inspect.signature(Actions_BasicActions_Pin.__init__)
    params = list(sig.parameters.keys())



def test_actions_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(Actions_BasicActions_OutputPin)


def test_actions_basicactions_outputpin_constructor_exists():
    assert callable(Actions_BasicActions_OutputPin.__init__)


def test_actions_basicactions_outputpin_constructor_args():
    sig = inspect.signature(Actions_BasicActions_OutputPin.__init__)
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
VariableAction_strategy = st.builds(
    VariableAction,
)
Actions_StructuredActions_ReadVariableAction_strategy = st.builds(
    Actions_StructuredActions_ReadVariableAction,
)
Actions_StructuredActions_Variable_strategy = st.builds(
    Actions_StructuredActions_Variable,
)
Variable_strategy = st.builds(
    Variable,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
Actions_CompleteActions_CreateLinkObjectAction_strategy = st.builds(
    Actions_CompleteActions_CreateLinkObjectAction,
)
Actions_StructuredActions_ClearVariableAction_strategy = st.builds(
    Actions_StructuredActions_ClearVariableAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
Actions_StructuredActions_RemoveVariableValueAction_strategy = st.builds(
    Actions_StructuredActions_RemoveVariableValueAction,
)
Actions_StructuredActions_AddVariableValueAction_strategy = st.builds(
    Actions_StructuredActions_AddVariableValueAction,
)
Actions_StructuredActions_WriteVariableAction_strategy = st.builds(
    Actions_StructuredActions_WriteVariableAction,
)
Actions_CompleteActions_ReadlsClassifiedObjectAction_strategy = st.builds(
    Actions_CompleteActions_ReadlsClassifiedObjectAction,
)
Trigger_strategy = st.builds(
    Trigger,
)
Actions_CompleteActions_Trigger_strategy = st.builds(
    Actions_CompleteActions_Trigger,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
Actions_CompleteActions_AcceptCallAction_strategy = st.builds(
    Actions_CompleteActions_AcceptCallAction,
)
Actions_IntermediateActions_Property_strategy = st.builds(
    Actions_IntermediateActions_Property,
)
QualifierValue_strategy = st.builds(
    QualifierValue,
)
Property_strategy = st.builds(
    Property,
)
Element_strategy = st.builds(
    Element,
)
Actions_CompleteActions_QualifierValue_strategy = st.builds(
    Actions_CompleteActions_QualifierValue,
)
Actions_IntermediateActions_LinkEndData_strategy = st.builds(
    Actions_IntermediateActions_LinkEndData,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
Actions_IntermediateActions_LinkEndDestructionData_strategy = st.builds(
    Actions_IntermediateActions_LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
Actions_IntermediateActions_RemoveStructuralFeatureValueAction_strategy = st.builds(
    Actions_IntermediateActions_RemoveStructuralFeatureValueAction,
)
Actions_IntermediateActions_AddStructuralFeatureValueAction_strategy = st.builds(
    Actions_IntermediateActions_AddStructuralFeatureValueAction,
)
Actions_IntermediateActions_Element_strategy = st.builds(
    Actions_IntermediateActions_Element,
)
Actions_IntermediateActions_LinkEndCreationData_strategy = st.builds(
    Actions_IntermediateActions_LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
Actions_IntermediateActions_DestroyLinkAction_strategy = st.builds(
    Actions_IntermediateActions_DestroyLinkAction,
)
Actions_IntermediateActions_CreateLinkAction_strategy = st.builds(
    Actions_IntermediateActions_CreateLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
Actions_IntermediateActions_WriteLinkAction_strategy = st.builds(
    Actions_IntermediateActions_WriteLinkAction,
)
Actions_IntermediateActions_ReadLinkAction_strategy = st.builds(
    Actions_IntermediateActions_ReadLinkAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
Actions_IntermediateActions_WriteStructuralFeatureAction_strategy = st.builds(
    Actions_IntermediateActions_WriteStructuralFeatureAction,
)
Actions_IntermediateActions_ClearStructuralFeatureAction_strategy = st.builds(
    Actions_IntermediateActions_ClearStructuralFeatureAction,
)
Actions_IntermediateActions_ReadStructuralFeatureAction_strategy = st.builds(
    Actions_IntermediateActions_ReadStructuralFeatureAction,
)
Actions_IntermediateActions_StructuralFeature_strategy = st.builds(
    Actions_IntermediateActions_StructuralFeature,
)
Signal_strategy = st.builds(
    Signal,
)
Actions_BasicActions_Operation_strategy = st.builds(
    Actions_BasicActions_Operation,
)
Operation_strategy = st.builds(
    Operation,
)
Actions_BasicActions_CallOperationAction_strategy = st.builds(
    Actions_BasicActions_CallOperationAction,
)
Actions_BasicActions_Behavior_strategy = st.builds(
    Actions_BasicActions_Behavior,
)
Behavior_strategy = st.builds(
    Behavior,
)
CallAction_strategy = st.builds(
    CallAction,
)
Actions_CompleteActions_StartObjectBehaviorAction_strategy = st.builds(
    Actions_CompleteActions_StartObjectBehaviorAction,
)
Actions_BasicActions_CallBehaviorAction_strategy = st.builds(
    Actions_BasicActions_CallBehaviorAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
Actions_BasicActions_SendSignalAction_strategy = st.builds(
    Actions_BasicActions_SendSignalAction,
)
Actions_BasicActions_CallAction_strategy = st.builds(
    Actions_BasicActions_CallAction,
    isSynchronous=
        st.booleans()
)
Actions_IntermediateActions_SendObjectAction_strategy = st.builds(
    Actions_IntermediateActions_SendObjectAction,
)
Actions_IntermediateActions_BroadcastSignalAction_strategy = st.builds(
    Actions_IntermediateActions_BroadcastSignalAction,
)
Actions_BasicActions_Signal_strategy = st.builds(
    Actions_BasicActions_Signal,
)
Pin_strategy = st.builds(
    Pin,
)
Actions_BasicActions_InputPin_strategy = st.builds(
    Actions_BasicActions_InputPin,
)
Action_strategy = st.builds(
    Action,
)
Actions_IntermediateActions_LinkAction_strategy = st.builds(
    Actions_IntermediateActions_LinkAction,
)
Actions_CompleteActions_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    Actions_CompleteActions_ReadLinkObjectEndQualifierAction,
)
Actions_CompleteActions_ReplyAction_strategy = st.builds(
    Actions_CompleteActions_ReplyAction,
)
Actions_CompleteActions_ReclassifyObjectAction_strategy = st.builds(
    Actions_CompleteActions_ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
Actions_CompleteActions_ReduceAction_strategy = st.builds(
    Actions_CompleteActions_ReduceAction,
    isOrdered=
        st.booleans()
)
Actions_IntermediateActions_StructuralFeatureAction_strategy = st.builds(
    Actions_IntermediateActions_StructuralFeatureAction,
)
Actions_CompleteActions_ReadExtendAction_strategy = st.builds(
    Actions_CompleteActions_ReadExtendAction,
)
Actions_CompleteActions_UnmarshallAction_strategy = st.builds(
    Actions_CompleteActions_UnmarshallAction,
)
Actions_IntermediateActions_CreateObjectAction_strategy = st.builds(
    Actions_IntermediateActions_CreateObjectAction,
)
Actions_IntermediateActions_TestIdentityAction_strategy = st.builds(
    Actions_IntermediateActions_TestIdentityAction,
)
Actions_CompleteActions_AcceptEventAction_strategy = st.builds(
    Actions_CompleteActions_AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
Actions_StructuredActions_RaiseExceptionAction_strategy = st.builds(
    Actions_StructuredActions_RaiseExceptionAction,
)
Actions_CompleteActions_ReadLinkObjectEndAction_strategy = st.builds(
    Actions_CompleteActions_ReadLinkObjectEndAction,
)
Actions_CompleteActions_StartClassifierBehaviorAction_strategy = st.builds(
    Actions_CompleteActions_StartClassifierBehaviorAction,
)
Actions_IntermediateActions_DestroyObjectAction_strategy = st.builds(
    Actions_IntermediateActions_DestroyObjectAction,
)
Actions_StructuredActions_VariableAction_strategy = st.builds(
    Actions_StructuredActions_VariableAction,
)
Actions_IntermediateActions_ValueSpecificationAction_strategy = st.builds(
    Actions_IntermediateActions_ValueSpecificationAction,
)
Actions_IntermediateActions_ReadSelfAction_strategy = st.builds(
    Actions_IntermediateActions_ReadSelfAction,
)
Actions_BasicActions_OpaqueAction_strategy = st.builds(
    Actions_BasicActions_OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
Actions_BasicActions_Classifier_strategy = st.builds(
    Actions_BasicActions_Classifier,
)
Actions_BasicActions_NamedElement_strategy = st.builds(
    Actions_BasicActions_NamedElement,
)
OutputPin_strategy = st.builds(
    OutputPin,
)
InputPin_strategy = st.builds(
    InputPin,
)
Actions_StructuredActions_ActionInputPin_strategy = st.builds(
    Actions_StructuredActions_ActionInputPin,
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Actions_BasicActions_Action_strategy = st.builds(
    Actions_BasicActions_Action,
)
Actions_BasicActions_InvocationAction_strategy = st.builds(
    Actions_BasicActions_InvocationAction,
)
Actions_BasicActions_ValueSpecification_strategy = st.builds(
    Actions_BasicActions_ValueSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
Actions_BasicActions_ValuePin_strategy = st.builds(
    Actions_BasicActions_ValuePin,
)
Actions_BasicActions_TypedElement_strategy = st.builds(
    Actions_BasicActions_TypedElement,
)
Actions_BasicActions_MultiplicityElement_strategy = st.builds(
    Actions_BasicActions_MultiplicityElement,
)
BasicActions_MultiplicityElement_strategy = st.builds(
    BasicActions_MultiplicityElement,
)
BasicActions_TypedElement_strategy = st.builds(
    BasicActions_TypedElement,
)
Actions_BasicActions_Pin_strategy = st.builds(
    Actions_BasicActions_Pin,
)
Actions_BasicActions_OutputPin_strategy = st.builds(
    Actions_BasicActions_OutputPin,
)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=Actions_StructuredActions_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_readvariableaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_ReadVariableAction)

@given(instance=Actions_StructuredActions_Variable_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_variable_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_Variable)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=Actions_CompleteActions_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_CreateLinkObjectAction)

@given(instance=Actions_StructuredActions_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_clearvariableaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_ClearVariableAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=Actions_StructuredActions_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_RemoveVariableValueAction)

@given(instance=Actions_StructuredActions_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_AddVariableValueAction)

@given(instance=Actions_StructuredActions_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_writevariableaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_WriteVariableAction)

@given(instance=Actions_CompleteActions_ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReadlsClassifiedObjectAction)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=Actions_CompleteActions_Trigger_strategy)
@settings(max_examples=50)
def test_actions_completeactions_trigger_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_Trigger)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=Actions_CompleteActions_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_acceptcallaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_AcceptCallAction)

@given(instance=Actions_IntermediateActions_Property_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_property_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_Property)

@given(instance=QualifierValue_strategy)
@settings(max_examples=50)
def test_qualifiervalue_instantiation(instance):
    assert isinstance(instance, QualifierValue)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Actions_CompleteActions_QualifierValue_strategy)
@settings(max_examples=50)
def test_actions_completeactions_qualifiervalue_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_QualifierValue)

@given(instance=Actions_IntermediateActions_LinkEndData_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_linkenddata_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_LinkEndData)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=Actions_IntermediateActions_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_LinkEndDestructionData)



@given(instance=Actions_IntermediateActions_LinkEndDestructionData_strategy)
def test_actions_intermediateactions_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=Actions_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_RemoveStructuralFeatureValueAction)

@given(instance=Actions_IntermediateActions_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_AddStructuralFeatureValueAction)

@given(instance=Actions_IntermediateActions_Element_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_element_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_Element)

@given(instance=Actions_IntermediateActions_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_LinkEndCreationData)



@given(instance=Actions_IntermediateActions_LinkEndCreationData_strategy)
def test_actions_intermediateactions_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=Actions_IntermediateActions_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_destroylinkaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_DestroyLinkAction)

@given(instance=Actions_IntermediateActions_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_createlinkaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_CreateLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=Actions_IntermediateActions_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_writelinkaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_WriteLinkAction)

@given(instance=Actions_IntermediateActions_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_readlinkaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_ReadLinkAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=Actions_IntermediateActions_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_WriteStructuralFeatureAction)

@given(instance=Actions_IntermediateActions_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_ClearStructuralFeatureAction)

@given(instance=Actions_IntermediateActions_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_ReadStructuralFeatureAction)

@given(instance=Actions_IntermediateActions_StructuralFeature_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_structuralfeature_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_StructuralFeature)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=Actions_BasicActions_Operation_strategy)
@settings(max_examples=50)
def test_actions_basicactions_operation_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Actions_BasicActions_CallOperationAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_calloperationaction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_CallOperationAction)

@given(instance=Actions_BasicActions_Behavior_strategy)
@settings(max_examples=50)
def test_actions_basicactions_behavior_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Behavior)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=Actions_CompleteActions_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_StartObjectBehaviorAction)

@given(instance=Actions_BasicActions_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_callbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_CallBehaviorAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=Actions_BasicActions_SendSignalAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_sendsignalaction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_SendSignalAction)

@given(instance=Actions_BasicActions_CallAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_callaction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_CallAction)



@given(instance=Actions_BasicActions_CallAction_strategy)
def test_actions_basicactions_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=Actions_IntermediateActions_SendObjectAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_sendobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_SendObjectAction)

@given(instance=Actions_IntermediateActions_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_BroadcastSignalAction)

@given(instance=Actions_BasicActions_Signal_strategy)
@settings(max_examples=50)
def test_actions_basicactions_signal_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Signal)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=Actions_BasicActions_InputPin_strategy)
@settings(max_examples=50)
def test_actions_basicactions_inputpin_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=Actions_IntermediateActions_LinkAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_linkaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_LinkAction)

@given(instance=Actions_CompleteActions_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReadLinkObjectEndQualifierAction)

@given(instance=Actions_CompleteActions_ReplyAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_replyaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReplyAction)

@given(instance=Actions_CompleteActions_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReclassifyObjectAction)



@given(instance=Actions_CompleteActions_ReclassifyObjectAction_strategy)
def test_actions_completeactions_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=Actions_CompleteActions_ReduceAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_reduceaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReduceAction)



@given(instance=Actions_CompleteActions_ReduceAction_strategy)
def test_actions_completeactions_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Actions_IntermediateActions_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_StructuralFeatureAction)

@given(instance=Actions_CompleteActions_ReadExtendAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_readextendaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReadExtendAction)

@given(instance=Actions_CompleteActions_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_unmarshallaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_UnmarshallAction)

@given(instance=Actions_IntermediateActions_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_createobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_CreateObjectAction)

@given(instance=Actions_IntermediateActions_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_testidentityaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_TestIdentityAction)

@given(instance=Actions_CompleteActions_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_accepteventaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_AcceptEventAction)



@given(instance=Actions_CompleteActions_AcceptEventAction_strategy)
def test_actions_completeactions_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=Actions_StructuredActions_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_RaiseExceptionAction)

@given(instance=Actions_CompleteActions_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_ReadLinkObjectEndAction)

@given(instance=Actions_CompleteActions_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions_completeactions_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions_CompleteActions_StartClassifierBehaviorAction)

@given(instance=Actions_IntermediateActions_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_DestroyObjectAction)

@given(instance=Actions_StructuredActions_VariableAction_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_variableaction_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_VariableAction)

@given(instance=Actions_IntermediateActions_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_ValueSpecificationAction)

@given(instance=Actions_IntermediateActions_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_actions_intermediateactions_readselfaction_instantiation(instance):
    assert isinstance(instance, Actions_IntermediateActions_ReadSelfAction)

@given(instance=Actions_BasicActions_OpaqueAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_opaqueaction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_OpaqueAction)



@given(instance=Actions_BasicActions_OpaqueAction_strategy)
def test_actions_basicactions_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=Actions_BasicActions_OpaqueAction_strategy)
def test_actions_basicactions_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Actions_BasicActions_Classifier_strategy)
@settings(max_examples=50)
def test_actions_basicactions_classifier_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Classifier)

@given(instance=Actions_BasicActions_NamedElement_strategy)
@settings(max_examples=50)
def test_actions_basicactions_namedelement_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_NamedElement)

@given(instance=OutputPin_strategy)
@settings(max_examples=50)
def test_outputpin_instantiation(instance):
    assert isinstance(instance, OutputPin)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=Actions_StructuredActions_ActionInputPin_strategy)
@settings(max_examples=50)
def test_actions_structuredactions_actioninputpin_instantiation(instance):
    assert isinstance(instance, Actions_StructuredActions_ActionInputPin)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Actions_BasicActions_Action_strategy)
@settings(max_examples=50)
def test_actions_basicactions_action_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Action)

@given(instance=Actions_BasicActions_InvocationAction_strategy)
@settings(max_examples=50)
def test_actions_basicactions_invocationaction_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_InvocationAction)

@given(instance=Actions_BasicActions_ValueSpecification_strategy)
@settings(max_examples=50)
def test_actions_basicactions_valuespecification_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_ValueSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=Actions_BasicActions_ValuePin_strategy)
@settings(max_examples=50)
def test_actions_basicactions_valuepin_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_ValuePin)

@given(instance=Actions_BasicActions_TypedElement_strategy)
@settings(max_examples=50)
def test_actions_basicactions_typedelement_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_TypedElement)

@given(instance=Actions_BasicActions_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_actions_basicactions_multiplicityelement_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_MultiplicityElement)

@given(instance=BasicActions_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_basicactions_multiplicityelement_instantiation(instance):
    assert isinstance(instance, BasicActions_MultiplicityElement)

@given(instance=BasicActions_TypedElement_strategy)
@settings(max_examples=50)
def test_basicactions_typedelement_instantiation(instance):
    assert isinstance(instance, BasicActions_TypedElement)

@given(instance=Actions_BasicActions_Pin_strategy)
@settings(max_examples=50)
def test_actions_basicactions_pin_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_Pin)

@given(instance=Actions_BasicActions_OutputPin_strategy)
@settings(max_examples=50)
def test_actions_basicactions_outputpin_instantiation(instance):
    assert isinstance(instance, Actions_BasicActions_OutputPin)
