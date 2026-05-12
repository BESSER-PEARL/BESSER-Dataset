import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    WriteVariableAction,
    ActionsProv_RemoveVariableValueAction,
    ActionsProv_AddVariableValueAction,
    VariableAction,
    ActionsProv_ClearVariableAction,
    ActionsProv_WriteVariableAction,
    ActionsProv_ReadVariableAction,
    CreateLinkAction,
    ActionsProv_CreateLinkObjectAction,
    ActionsProv_ReadlsClassifiedObjectAction,
    AcceptEventAction,
    ActionsProv_AcceptCallAction,
    ActionsProv_QualifierValue,
    LinkEndData,
    ActionsProv_LinkEndDestructionData,
    ActionsProv_LinkEndCreationData,
    WriteLinkAction,
    ActionsProv_DestroyLinkAction,
    ActionsProv_CreateLinkAction,
    LinkAction,
    ActionsProv_ReadLinkAction,
    ActionsProv_WriteLinkAction,
    ActionsProv_LinkEndData,
    WriteStructuralFeatureAction,
    ActionsProv_AddStructuralFeatureValueAction,
    ActionsProv_RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    ActionsProv_WriteStructuralFeatureAction,
    ActionsProv_ClearStructuralFeatureAction,
    ActionsProv_ReadStructuralFeatureAction,
    ActionsProv_CallOperationAction,
    CallAction,
    ActionsProv_StartObjectBehaviorAction,
    ActionsProv_CallBehaviorAction,
    ActionsProv_Action,
    InvocationAction,
    ActionsProv_BroadcastSignalAction,
    ActionsProv_SendObjectAction,
    ActionsProv_SendSignalAction,
    ActionsProv_CallAction,
    InputPin,
    ActionsProv_ActionInputPin,
    ActionsProv_ValuePin,
    ActionsProv_Pin,
    Pin,
    ActionsProv_InputPin,
    Action,
    ActionsProv_ReclassifyObjectAction,
    ActionsProv_ValueSpecificationAction,
    ActionsProv_VariableAction,
    ActionsProv_LinkAction,
    ActionsProv_AcceptEventAction,
    ActionsProv_InvocationAction,
    ActionsProv_ReadLinkObjectEndQualifierAction,
    ActionsProv_StructuralFeatureAction,
    ActionsProv_RaiseExceptionAction,
    ActionsProv_CreateObjectAction,
    ActionsProv_ReadExtendAction,
    ActionsProv_ReplyAction,
    ActionsProv_UnmarshallAction,
    ActionsProv_StartClassifierBehaviorAction,
    ActionsProv_TestIdentityAction,
    ActionsProv_ReadLinkObjectEndAction,
    ActionsProv_ReadSelfAction,
    ActionsProv_ReduceAction,
    ActionsProv_DestroyObjectAction,
    ActionsProv_OpaqueAction,
    ActionsProv_OutputPin,
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



def test_actionsprov_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_RemoveVariableValueAction)


def test_actionsprov_removevariablevalueaction_constructor_exists():
    assert callable(ActionsProv_RemoveVariableValueAction.__init__)


def test_actionsprov_removevariablevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_AddVariableValueAction)


def test_actionsprov_addvariablevalueaction_constructor_exists():
    assert callable(ActionsProv_AddVariableValueAction.__init__)


def test_actionsprov_addvariablevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ClearVariableAction)


def test_actionsprov_clearvariableaction_constructor_exists():
    assert callable(ActionsProv_ClearVariableAction.__init__)


def test_actionsprov_clearvariableaction_constructor_args():
    sig = inspect.signature(ActionsProv_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_WriteVariableAction)


def test_actionsprov_writevariableaction_constructor_exists():
    assert callable(ActionsProv_WriteVariableAction.__init__)


def test_actionsprov_writevariableaction_constructor_args():
    sig = inspect.signature(ActionsProv_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadVariableAction)


def test_actionsprov_readvariableaction_constructor_exists():
    assert callable(ActionsProv_ReadVariableAction.__init__)


def test_actionsprov_readvariableaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CreateLinkObjectAction)


def test_actionsprov_createlinkobjectaction_constructor_exists():
    assert callable(ActionsProv_CreateLinkObjectAction.__init__)


def test_actionsprov_createlinkobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadlsClassifiedObjectAction)


def test_actionsprov_readlsclassifiedobjectaction_constructor_exists():
    assert callable(ActionsProv_ReadlsClassifiedObjectAction.__init__)


def test_actionsprov_readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_AcceptCallAction)


def test_actionsprov_acceptcallaction_constructor_exists():
    assert callable(ActionsProv_AcceptCallAction.__init__)


def test_actionsprov_acceptcallaction_constructor_args():
    sig = inspect.signature(ActionsProv_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_QualifierValue)


def test_actionsprov_qualifiervalue_constructor_exists():
    assert callable(ActionsProv_QualifierValue.__init__)


def test_actionsprov_qualifiervalue_constructor_args():
    sig = inspect.signature(ActionsProv_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_LinkEndDestructionData)


def test_actionsprov_linkenddestructiondata_constructor_exists():
    assert callable(ActionsProv_LinkEndDestructionData.__init__)


def test_actionsprov_linkenddestructiondata_constructor_args():
    sig = inspect.signature(ActionsProv_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_actionsprov_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(ActionsProv_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in ActionsProv_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_LinkEndCreationData)


def test_actionsprov_linkendcreationdata_constructor_exists():
    assert callable(ActionsProv_LinkEndCreationData.__init__)


def test_actionsprov_linkendcreationdata_constructor_args():
    sig = inspect.signature(ActionsProv_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actionsprov_linkendcreationdata_has_isReplaceAll():
    assert hasattr(ActionsProv_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in ActionsProv_LinkEndCreationData.__mro__:
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



def test_actionsprov_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_DestroyLinkAction)


def test_actionsprov_destroylinkaction_constructor_exists():
    assert callable(ActionsProv_DestroyLinkAction.__init__)


def test_actionsprov_destroylinkaction_constructor_args():
    sig = inspect.signature(ActionsProv_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CreateLinkAction)


def test_actionsprov_createlinkaction_constructor_exists():
    assert callable(ActionsProv_CreateLinkAction.__init__)


def test_actionsprov_createlinkaction_constructor_args():
    sig = inspect.signature(ActionsProv_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadLinkAction)


def test_actionsprov_readlinkaction_constructor_exists():
    assert callable(ActionsProv_ReadLinkAction.__init__)


def test_actionsprov_readlinkaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_WriteLinkAction)


def test_actionsprov_writelinkaction_constructor_exists():
    assert callable(ActionsProv_WriteLinkAction.__init__)


def test_actionsprov_writelinkaction_constructor_args():
    sig = inspect.signature(ActionsProv_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_linkenddata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_LinkEndData)


def test_actionsprov_linkenddata_constructor_exists():
    assert callable(ActionsProv_LinkEndData.__init__)


def test_actionsprov_linkenddata_constructor_args():
    sig = inspect.signature(ActionsProv_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_AddStructuralFeatureValueAction)


def test_actionsprov_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(ActionsProv_AddStructuralFeatureValueAction.__init__)


def test_actionsprov_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_RemoveStructuralFeatureValueAction)


def test_actionsprov_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(ActionsProv_RemoveStructuralFeatureValueAction.__init__)


def test_actionsprov_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_WriteStructuralFeatureAction)


def test_actionsprov_writestructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv_WriteStructuralFeatureAction.__init__)


def test_actionsprov_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ClearStructuralFeatureAction)


def test_actionsprov_clearstructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv_ClearStructuralFeatureAction.__init__)


def test_actionsprov_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadStructuralFeatureAction)


def test_actionsprov_readstructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv_ReadStructuralFeatureAction.__init__)


def test_actionsprov_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CallOperationAction)


def test_actionsprov_calloperationaction_constructor_exists():
    assert callable(ActionsProv_CallOperationAction.__init__)


def test_actionsprov_calloperationaction_constructor_args():
    sig = inspect.signature(ActionsProv_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_StartObjectBehaviorAction)


def test_actionsprov_startobjectbehavioraction_constructor_exists():
    assert callable(ActionsProv_StartObjectBehaviorAction.__init__)


def test_actionsprov_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CallBehaviorAction)


def test_actionsprov_callbehavioraction_constructor_exists():
    assert callable(ActionsProv_CallBehaviorAction.__init__)


def test_actionsprov_callbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_action_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_Action)


def test_actionsprov_action_constructor_exists():
    assert callable(ActionsProv_Action.__init__)


def test_actionsprov_action_constructor_args():
    sig = inspect.signature(ActionsProv_Action.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_BroadcastSignalAction)


def test_actionsprov_broadcastsignalaction_constructor_exists():
    assert callable(ActionsProv_BroadcastSignalAction.__init__)


def test_actionsprov_broadcastsignalaction_constructor_args():
    sig = inspect.signature(ActionsProv_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_SendObjectAction)


def test_actionsprov_sendobjectaction_constructor_exists():
    assert callable(ActionsProv_SendObjectAction.__init__)


def test_actionsprov_sendobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_SendSignalAction)


def test_actionsprov_sendsignalaction_constructor_exists():
    assert callable(ActionsProv_SendSignalAction.__init__)


def test_actionsprov_sendsignalaction_constructor_args():
    sig = inspect.signature(ActionsProv_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_callaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CallAction)


def test_actionsprov_callaction_constructor_exists():
    assert callable(ActionsProv_CallAction.__init__)


def test_actionsprov_callaction_constructor_args():
    sig = inspect.signature(ActionsProv_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_actionsprov_callaction_has_isSynchronous():
    assert hasattr(ActionsProv_CallAction, "isSynchronous")
    descriptor = None
    for klass in ActionsProv_CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ActionInputPin)


def test_actionsprov_actioninputpin_constructor_exists():
    assert callable(ActionsProv_ActionInputPin.__init__)


def test_actionsprov_actioninputpin_constructor_args():
    sig = inspect.signature(ActionsProv_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_valuepin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ValuePin)


def test_actionsprov_valuepin_constructor_exists():
    assert callable(ActionsProv_ValuePin.__init__)


def test_actionsprov_valuepin_constructor_args():
    sig = inspect.signature(ActionsProv_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_pin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_Pin)


def test_actionsprov_pin_constructor_exists():
    assert callable(ActionsProv_Pin.__init__)


def test_actionsprov_pin_constructor_args():
    sig = inspect.signature(ActionsProv_Pin.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_inputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_InputPin)


def test_actionsprov_inputpin_constructor_exists():
    assert callable(ActionsProv_InputPin.__init__)


def test_actionsprov_inputpin_constructor_args():
    sig = inspect.signature(ActionsProv_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReclassifyObjectAction)


def test_actionsprov_reclassifyobjectaction_constructor_exists():
    assert callable(ActionsProv_ReclassifyObjectAction.__init__)


def test_actionsprov_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actionsprov_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(ActionsProv_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in ActionsProv_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ValueSpecificationAction)


def test_actionsprov_valuespecificationaction_constructor_exists():
    assert callable(ActionsProv_ValueSpecificationAction.__init__)


def test_actionsprov_valuespecificationaction_constructor_args():
    sig = inspect.signature(ActionsProv_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_variableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_VariableAction)


def test_actionsprov_variableaction_constructor_exists():
    assert callable(ActionsProv_VariableAction.__init__)


def test_actionsprov_variableaction_constructor_args():
    sig = inspect.signature(ActionsProv_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_linkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_LinkAction)


def test_actionsprov_linkaction_constructor_exists():
    assert callable(ActionsProv_LinkAction.__init__)


def test_actionsprov_linkaction_constructor_args():
    sig = inspect.signature(ActionsProv_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_AcceptEventAction)


def test_actionsprov_accepteventaction_constructor_exists():
    assert callable(ActionsProv_AcceptEventAction.__init__)


def test_actionsprov_accepteventaction_constructor_args():
    sig = inspect.signature(ActionsProv_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_actionsprov_accepteventaction_has_isUnmarshall():
    assert hasattr(ActionsProv_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in ActionsProv_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov_invocationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_InvocationAction)


def test_actionsprov_invocationaction_constructor_exists():
    assert callable(ActionsProv_InvocationAction.__init__)


def test_actionsprov_invocationaction_constructor_args():
    sig = inspect.signature(ActionsProv_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadLinkObjectEndQualifierAction)


def test_actionsprov_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(ActionsProv_ReadLinkObjectEndQualifierAction.__init__)


def test_actionsprov_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_StructuralFeatureAction)


def test_actionsprov_structuralfeatureaction_constructor_exists():
    assert callable(ActionsProv_StructuralFeatureAction.__init__)


def test_actionsprov_structuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_RaiseExceptionAction)


def test_actionsprov_raiseexceptionaction_constructor_exists():
    assert callable(ActionsProv_RaiseExceptionAction.__init__)


def test_actionsprov_raiseexceptionaction_constructor_args():
    sig = inspect.signature(ActionsProv_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_CreateObjectAction)


def test_actionsprov_createobjectaction_constructor_exists():
    assert callable(ActionsProv_CreateObjectAction.__init__)


def test_actionsprov_createobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readextendaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadExtendAction)


def test_actionsprov_readextendaction_constructor_exists():
    assert callable(ActionsProv_ReadExtendAction.__init__)


def test_actionsprov_readextendaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_replyaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReplyAction)


def test_actionsprov_replyaction_constructor_exists():
    assert callable(ActionsProv_ReplyAction.__init__)


def test_actionsprov_replyaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_UnmarshallAction)


def test_actionsprov_unmarshallaction_constructor_exists():
    assert callable(ActionsProv_UnmarshallAction.__init__)


def test_actionsprov_unmarshallaction_constructor_args():
    sig = inspect.signature(ActionsProv_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_StartClassifierBehaviorAction)


def test_actionsprov_startclassifierbehavioraction_constructor_exists():
    assert callable(ActionsProv_StartClassifierBehaviorAction.__init__)


def test_actionsprov_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_TestIdentityAction)


def test_actionsprov_testidentityaction_constructor_exists():
    assert callable(ActionsProv_TestIdentityAction.__init__)


def test_actionsprov_testidentityaction_constructor_args():
    sig = inspect.signature(ActionsProv_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadLinkObjectEndAction)


def test_actionsprov_readlinkobjectendaction_constructor_exists():
    assert callable(ActionsProv_ReadLinkObjectEndAction.__init__)


def test_actionsprov_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_readselfaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReadSelfAction)


def test_actionsprov_readselfaction_constructor_exists():
    assert callable(ActionsProv_ReadSelfAction.__init__)


def test_actionsprov_readselfaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_reduceaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_ReduceAction)


def test_actionsprov_reduceaction_constructor_exists():
    assert callable(ActionsProv_ReduceAction.__init__)


def test_actionsprov_reduceaction_constructor_args():
    sig = inspect.signature(ActionsProv_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_actionsprov_reduceaction_has_isOrdered():
    assert hasattr(ActionsProv_ReduceAction, "isOrdered")
    descriptor = None
    for klass in ActionsProv_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_DestroyObjectAction)


def test_actionsprov_destroyobjectaction_constructor_exists():
    assert callable(ActionsProv_DestroyObjectAction.__init__)


def test_actionsprov_destroyobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_OpaqueAction)


def test_actionsprov_opaqueaction_constructor_exists():
    assert callable(ActionsProv_OpaqueAction.__init__)


def test_actionsprov_opaqueaction_constructor_args():
    sig = inspect.signature(ActionsProv_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_actionsprov_opaqueaction_has_language():
    assert hasattr(ActionsProv_OpaqueAction, "language")
    descriptor = None
    for klass in ActionsProv_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_actionsprov_opaqueaction_has_body():
    assert hasattr(ActionsProv_OpaqueAction, "body")
    descriptor = None
    for klass in ActionsProv_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov_outputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv_OutputPin)


def test_actionsprov_outputpin_constructor_exists():
    assert callable(ActionsProv_OutputPin.__init__)


def test_actionsprov_outputpin_constructor_args():
    sig = inspect.signature(ActionsProv_OutputPin.__init__)
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
ActionsProv_RemoveVariableValueAction_strategy = st.builds(
    ActionsProv_RemoveVariableValueAction,
)
ActionsProv_AddVariableValueAction_strategy = st.builds(
    ActionsProv_AddVariableValueAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
ActionsProv_ClearVariableAction_strategy = st.builds(
    ActionsProv_ClearVariableAction,
)
ActionsProv_WriteVariableAction_strategy = st.builds(
    ActionsProv_WriteVariableAction,
)
ActionsProv_ReadVariableAction_strategy = st.builds(
    ActionsProv_ReadVariableAction,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
ActionsProv_CreateLinkObjectAction_strategy = st.builds(
    ActionsProv_CreateLinkObjectAction,
)
ActionsProv_ReadlsClassifiedObjectAction_strategy = st.builds(
    ActionsProv_ReadlsClassifiedObjectAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
ActionsProv_AcceptCallAction_strategy = st.builds(
    ActionsProv_AcceptCallAction,
)
ActionsProv_QualifierValue_strategy = st.builds(
    ActionsProv_QualifierValue,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
ActionsProv_LinkEndDestructionData_strategy = st.builds(
    ActionsProv_LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
ActionsProv_LinkEndCreationData_strategy = st.builds(
    ActionsProv_LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
ActionsProv_DestroyLinkAction_strategy = st.builds(
    ActionsProv_DestroyLinkAction,
)
ActionsProv_CreateLinkAction_strategy = st.builds(
    ActionsProv_CreateLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
ActionsProv_ReadLinkAction_strategy = st.builds(
    ActionsProv_ReadLinkAction,
)
ActionsProv_WriteLinkAction_strategy = st.builds(
    ActionsProv_WriteLinkAction,
)
ActionsProv_LinkEndData_strategy = st.builds(
    ActionsProv_LinkEndData,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
ActionsProv_AddStructuralFeatureValueAction_strategy = st.builds(
    ActionsProv_AddStructuralFeatureValueAction,
)
ActionsProv_RemoveStructuralFeatureValueAction_strategy = st.builds(
    ActionsProv_RemoveStructuralFeatureValueAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
ActionsProv_WriteStructuralFeatureAction_strategy = st.builds(
    ActionsProv_WriteStructuralFeatureAction,
)
ActionsProv_ClearStructuralFeatureAction_strategy = st.builds(
    ActionsProv_ClearStructuralFeatureAction,
)
ActionsProv_ReadStructuralFeatureAction_strategy = st.builds(
    ActionsProv_ReadStructuralFeatureAction,
)
ActionsProv_CallOperationAction_strategy = st.builds(
    ActionsProv_CallOperationAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
ActionsProv_StartObjectBehaviorAction_strategy = st.builds(
    ActionsProv_StartObjectBehaviorAction,
)
ActionsProv_CallBehaviorAction_strategy = st.builds(
    ActionsProv_CallBehaviorAction,
)
ActionsProv_Action_strategy = st.builds(
    ActionsProv_Action,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
ActionsProv_BroadcastSignalAction_strategy = st.builds(
    ActionsProv_BroadcastSignalAction,
)
ActionsProv_SendObjectAction_strategy = st.builds(
    ActionsProv_SendObjectAction,
)
ActionsProv_SendSignalAction_strategy = st.builds(
    ActionsProv_SendSignalAction,
)
ActionsProv_CallAction_strategy = st.builds(
    ActionsProv_CallAction,
    isSynchronous=
        st.booleans()
)
InputPin_strategy = st.builds(
    InputPin,
)
ActionsProv_ActionInputPin_strategy = st.builds(
    ActionsProv_ActionInputPin,
)
ActionsProv_ValuePin_strategy = st.builds(
    ActionsProv_ValuePin,
)
ActionsProv_Pin_strategy = st.builds(
    ActionsProv_Pin,
)
Pin_strategy = st.builds(
    Pin,
)
ActionsProv_InputPin_strategy = st.builds(
    ActionsProv_InputPin,
)
Action_strategy = st.builds(
    Action,
)
ActionsProv_ReclassifyObjectAction_strategy = st.builds(
    ActionsProv_ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
ActionsProv_ValueSpecificationAction_strategy = st.builds(
    ActionsProv_ValueSpecificationAction,
)
ActionsProv_VariableAction_strategy = st.builds(
    ActionsProv_VariableAction,
)
ActionsProv_LinkAction_strategy = st.builds(
    ActionsProv_LinkAction,
)
ActionsProv_AcceptEventAction_strategy = st.builds(
    ActionsProv_AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
ActionsProv_InvocationAction_strategy = st.builds(
    ActionsProv_InvocationAction,
)
ActionsProv_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    ActionsProv_ReadLinkObjectEndQualifierAction,
)
ActionsProv_StructuralFeatureAction_strategy = st.builds(
    ActionsProv_StructuralFeatureAction,
)
ActionsProv_RaiseExceptionAction_strategy = st.builds(
    ActionsProv_RaiseExceptionAction,
)
ActionsProv_CreateObjectAction_strategy = st.builds(
    ActionsProv_CreateObjectAction,
)
ActionsProv_ReadExtendAction_strategy = st.builds(
    ActionsProv_ReadExtendAction,
)
ActionsProv_ReplyAction_strategy = st.builds(
    ActionsProv_ReplyAction,
)
ActionsProv_UnmarshallAction_strategy = st.builds(
    ActionsProv_UnmarshallAction,
)
ActionsProv_StartClassifierBehaviorAction_strategy = st.builds(
    ActionsProv_StartClassifierBehaviorAction,
)
ActionsProv_TestIdentityAction_strategy = st.builds(
    ActionsProv_TestIdentityAction,
)
ActionsProv_ReadLinkObjectEndAction_strategy = st.builds(
    ActionsProv_ReadLinkObjectEndAction,
)
ActionsProv_ReadSelfAction_strategy = st.builds(
    ActionsProv_ReadSelfAction,
)
ActionsProv_ReduceAction_strategy = st.builds(
    ActionsProv_ReduceAction,
    isOrdered=
        st.booleans()
)
ActionsProv_DestroyObjectAction_strategy = st.builds(
    ActionsProv_DestroyObjectAction,
)
ActionsProv_OpaqueAction_strategy = st.builds(
    ActionsProv_OpaqueAction,
    language=
        safe_text,
    body=
        safe_text
)
ActionsProv_OutputPin_strategy = st.builds(
    ActionsProv_OutputPin,
)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=ActionsProv_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_RemoveVariableValueAction)

@given(instance=ActionsProv_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_AddVariableValueAction)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=ActionsProv_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov_clearvariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ClearVariableAction)

@given(instance=ActionsProv_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov_writevariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_WriteVariableAction)

@given(instance=ActionsProv_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readvariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadVariableAction)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=ActionsProv_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CreateLinkObjectAction)

@given(instance=ActionsProv_ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadlsClassifiedObjectAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=ActionsProv_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_actionsprov_acceptcallaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_AcceptCallAction)

@given(instance=ActionsProv_QualifierValue_strategy)
@settings(max_examples=50)
def test_actionsprov_qualifiervalue_instantiation(instance):
    assert isinstance(instance, ActionsProv_QualifierValue)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=ActionsProv_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_actionsprov_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, ActionsProv_LinkEndDestructionData)



@given(instance=ActionsProv_LinkEndDestructionData_strategy)
def test_actionsprov_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=ActionsProv_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_actionsprov_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, ActionsProv_LinkEndCreationData)



@given(instance=ActionsProv_LinkEndCreationData_strategy)
def test_actionsprov_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=ActionsProv_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov_destroylinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_DestroyLinkAction)

@given(instance=ActionsProv_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov_createlinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CreateLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=ActionsProv_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readlinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadLinkAction)

@given(instance=ActionsProv_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov_writelinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_WriteLinkAction)

@given(instance=ActionsProv_LinkEndData_strategy)
@settings(max_examples=50)
def test_actionsprov_linkenddata_instantiation(instance):
    assert isinstance(instance, ActionsProv_LinkEndData)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=ActionsProv_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_AddStructuralFeatureValueAction)

@given(instance=ActionsProv_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_RemoveStructuralFeatureValueAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=ActionsProv_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_WriteStructuralFeatureAction)

@given(instance=ActionsProv_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ClearStructuralFeatureAction)

@given(instance=ActionsProv_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadStructuralFeatureAction)

@given(instance=ActionsProv_CallOperationAction_strategy)
@settings(max_examples=50)
def test_actionsprov_calloperationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CallOperationAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=ActionsProv_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv_StartObjectBehaviorAction)

@given(instance=ActionsProv_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov_callbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CallBehaviorAction)

@given(instance=ActionsProv_Action_strategy)
@settings(max_examples=50)
def test_actionsprov_action_instantiation(instance):
    assert isinstance(instance, ActionsProv_Action)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=ActionsProv_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_actionsprov_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_BroadcastSignalAction)

@given(instance=ActionsProv_SendObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_sendobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_SendObjectAction)

@given(instance=ActionsProv_SendSignalAction_strategy)
@settings(max_examples=50)
def test_actionsprov_sendsignalaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_SendSignalAction)

@given(instance=ActionsProv_CallAction_strategy)
@settings(max_examples=50)
def test_actionsprov_callaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CallAction)



@given(instance=ActionsProv_CallAction_strategy)
def test_actionsprov_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=ActionsProv_ActionInputPin_strategy)
@settings(max_examples=50)
def test_actionsprov_actioninputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv_ActionInputPin)

@given(instance=ActionsProv_ValuePin_strategy)
@settings(max_examples=50)
def test_actionsprov_valuepin_instantiation(instance):
    assert isinstance(instance, ActionsProv_ValuePin)

@given(instance=ActionsProv_Pin_strategy)
@settings(max_examples=50)
def test_actionsprov_pin_instantiation(instance):
    assert isinstance(instance, ActionsProv_Pin)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ActionsProv_InputPin_strategy)
@settings(max_examples=50)
def test_actionsprov_inputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv_InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=ActionsProv_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReclassifyObjectAction)



@given(instance=ActionsProv_ReclassifyObjectAction_strategy)
def test_actionsprov_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=ActionsProv_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_actionsprov_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ValueSpecificationAction)

@given(instance=ActionsProv_VariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov_variableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_VariableAction)

@given(instance=ActionsProv_LinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov_linkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_LinkAction)

@given(instance=ActionsProv_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_actionsprov_accepteventaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_AcceptEventAction)



@given(instance=ActionsProv_AcceptEventAction_strategy)
def test_actionsprov_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=ActionsProv_InvocationAction_strategy)
@settings(max_examples=50)
def test_actionsprov_invocationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_InvocationAction)

@given(instance=ActionsProv_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadLinkObjectEndQualifierAction)

@given(instance=ActionsProv_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_StructuralFeatureAction)

@given(instance=ActionsProv_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_actionsprov_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_RaiseExceptionAction)

@given(instance=ActionsProv_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_createobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_CreateObjectAction)

@given(instance=ActionsProv_ReadExtendAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readextendaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadExtendAction)

@given(instance=ActionsProv_ReplyAction_strategy)
@settings(max_examples=50)
def test_actionsprov_replyaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReplyAction)

@given(instance=ActionsProv_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_actionsprov_unmarshallaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_UnmarshallAction)

@given(instance=ActionsProv_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv_StartClassifierBehaviorAction)

@given(instance=ActionsProv_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_actionsprov_testidentityaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_TestIdentityAction)

@given(instance=ActionsProv_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadLinkObjectEndAction)

@given(instance=ActionsProv_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_actionsprov_readselfaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReadSelfAction)

@given(instance=ActionsProv_ReduceAction_strategy)
@settings(max_examples=50)
def test_actionsprov_reduceaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_ReduceAction)



@given(instance=ActionsProv_ReduceAction_strategy)
def test_actionsprov_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=ActionsProv_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_DestroyObjectAction)

@given(instance=ActionsProv_OpaqueAction_strategy)
@settings(max_examples=50)
def test_actionsprov_opaqueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv_OpaqueAction)



@given(instance=ActionsProv_OpaqueAction_strategy)
def test_actionsprov_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=ActionsProv_OpaqueAction_strategy)
def test_actionsprov_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ActionsProv_OutputPin_strategy)
@settings(max_examples=50)
def test_actionsprov_outputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv_OutputPin)
