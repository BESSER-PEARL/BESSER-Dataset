import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    WriteVariableAction,
    ActionsProv::RemoveVariableValueAction,
    ActionsProv::AddVariableValueAction,
    VariableAction,
    ActionsProv::ClearVariableAction,
    ActionsProv::WriteVariableAction,
    ActionsProv::ReadVariableAction,
    CreateLinkAction,
    ActionsProv::CreateLinkObjectAction,
    ActionsProv::ReadlsClassifiedObjectAction,
    AcceptEventAction,
    ActionsProv::AcceptCallAction,
    ActionsProv::QualifierValue,
    LinkEndData,
    ActionsProv::LinkEndDestructionData,
    ActionsProv::LinkEndCreationData,
    WriteLinkAction,
    ActionsProv::DestroyLinkAction,
    ActionsProv::CreateLinkAction,
    LinkAction,
    ActionsProv::WriteLinkAction,
    ActionsProv::ReadLinkAction,
    ActionsProv::LinkEndData,
    WriteStructuralFeatureAction,
    ActionsProv::AddStructuralFeatureValueAction,
    ActionsProv::RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    ActionsProv::WriteStructuralFeatureAction,
    ActionsProv::ClearStructuralFeatureAction,
    ActionsProv::ReadStructuralFeatureAction,
    ActionsProv::CallOperationAction,
    CallAction,
    ActionsProv::StartObjectBehaviorAction,
    ActionsProv::CallBehaviorAction,
    ActionsProv::Action,
    InvocationAction,
    ActionsProv::BroadcastSignalAction,
    ActionsProv::SendSignalAction,
    ActionsProv::SendObjectAction,
    ActionsProv::CallAction,
    InputPin,
    ActionsProv::ActionInputPin,
    ActionsProv::ValuePin,
    ActionsProv::Pin,
    Pin,
    ActionsProv::InputPin,
    Action,
    ActionsProv::StartClassifierBehaviorAction,
    ActionsProv::LinkAction,
    ActionsProv::UnmarshallAction,
    ActionsProv::ReadLinkObjectEndAction,
    ActionsProv::AcceptEventAction,
    ActionsProv::VariableAction,
    ActionsProv::CreateObjectAction,
    ActionsProv::RaiseExceptionAction,
    ActionsProv::ReduceAction,
    ActionsProv::ReadLinkObjectEndQualifierAction,
    ActionsProv::StructuralFeatureAction,
    ActionsProv::ReplyAction,
    ActionsProv::InvocationAction,
    ActionsProv::ReadExtendAction,
    ActionsProv::TestIdentityAction,
    ActionsProv::DestroyObjectAction,
    ActionsProv::ReadSelfAction,
    ActionsProv::ValueSpecificationAction,
    ActionsProv::ReclassifyObjectAction,
    ActionsProv::OpaqueAction,
    ActionsProv::OutputPin,
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



def test_actionsprov::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::RemoveVariableValueAction)


def test_actionsprov::removevariablevalueaction_constructor_exists():
    assert callable(ActionsProv::RemoveVariableValueAction.__init__)


def test_actionsprov::removevariablevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::AddVariableValueAction)


def test_actionsprov::addvariablevalueaction_constructor_exists():
    assert callable(ActionsProv::AddVariableValueAction.__init__)


def test_actionsprov::addvariablevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ClearVariableAction)


def test_actionsprov::clearvariableaction_constructor_exists():
    assert callable(ActionsProv::ClearVariableAction.__init__)


def test_actionsprov::clearvariableaction_constructor_args():
    sig = inspect.signature(ActionsProv::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::WriteVariableAction)


def test_actionsprov::writevariableaction_constructor_exists():
    assert callable(ActionsProv::WriteVariableAction.__init__)


def test_actionsprov::writevariableaction_constructor_args():
    sig = inspect.signature(ActionsProv::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadVariableAction)


def test_actionsprov::readvariableaction_constructor_exists():
    assert callable(ActionsProv::ReadVariableAction.__init__)


def test_actionsprov::readvariableaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CreateLinkObjectAction)


def test_actionsprov::createlinkobjectaction_constructor_exists():
    assert callable(ActionsProv::CreateLinkObjectAction.__init__)


def test_actionsprov::createlinkobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadlsClassifiedObjectAction)


def test_actionsprov::readlsclassifiedobjectaction_constructor_exists():
    assert callable(ActionsProv::ReadlsClassifiedObjectAction.__init__)


def test_actionsprov::readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::AcceptCallAction)


def test_actionsprov::acceptcallaction_constructor_exists():
    assert callable(ActionsProv::AcceptCallAction.__init__)


def test_actionsprov::acceptcallaction_constructor_args():
    sig = inspect.signature(ActionsProv::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::QualifierValue)


def test_actionsprov::qualifiervalue_constructor_exists():
    assert callable(ActionsProv::QualifierValue.__init__)


def test_actionsprov::qualifiervalue_constructor_args():
    sig = inspect.signature(ActionsProv::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::LinkEndDestructionData)


def test_actionsprov::linkenddestructiondata_constructor_exists():
    assert callable(ActionsProv::LinkEndDestructionData.__init__)


def test_actionsprov::linkenddestructiondata_constructor_args():
    sig = inspect.signature(ActionsProv::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_actionsprov::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(ActionsProv::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in ActionsProv::LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::LinkEndCreationData)


def test_actionsprov::linkendcreationdata_constructor_exists():
    assert callable(ActionsProv::LinkEndCreationData.__init__)


def test_actionsprov::linkendcreationdata_constructor_args():
    sig = inspect.signature(ActionsProv::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actionsprov::linkendcreationdata_has_isReplaceAll():
    assert hasattr(ActionsProv::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in ActionsProv::LinkEndCreationData.__mro__:
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



def test_actionsprov::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::DestroyLinkAction)


def test_actionsprov::destroylinkaction_constructor_exists():
    assert callable(ActionsProv::DestroyLinkAction.__init__)


def test_actionsprov::destroylinkaction_constructor_args():
    sig = inspect.signature(ActionsProv::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CreateLinkAction)


def test_actionsprov::createlinkaction_constructor_exists():
    assert callable(ActionsProv::CreateLinkAction.__init__)


def test_actionsprov::createlinkaction_constructor_args():
    sig = inspect.signature(ActionsProv::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::WriteLinkAction)


def test_actionsprov::writelinkaction_constructor_exists():
    assert callable(ActionsProv::WriteLinkAction.__init__)


def test_actionsprov::writelinkaction_constructor_args():
    sig = inspect.signature(ActionsProv::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadLinkAction)


def test_actionsprov::readlinkaction_constructor_exists():
    assert callable(ActionsProv::ReadLinkAction.__init__)


def test_actionsprov::readlinkaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::linkenddata_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::LinkEndData)


def test_actionsprov::linkenddata_constructor_exists():
    assert callable(ActionsProv::LinkEndData.__init__)


def test_actionsprov::linkenddata_constructor_args():
    sig = inspect.signature(ActionsProv::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::AddStructuralFeatureValueAction)


def test_actionsprov::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(ActionsProv::AddStructuralFeatureValueAction.__init__)


def test_actionsprov::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::RemoveStructuralFeatureValueAction)


def test_actionsprov::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(ActionsProv::RemoveStructuralFeatureValueAction.__init__)


def test_actionsprov::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(ActionsProv::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::WriteStructuralFeatureAction)


def test_actionsprov::writestructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv::WriteStructuralFeatureAction.__init__)


def test_actionsprov::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ClearStructuralFeatureAction)


def test_actionsprov::clearstructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv::ClearStructuralFeatureAction.__init__)


def test_actionsprov::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadStructuralFeatureAction)


def test_actionsprov::readstructuralfeatureaction_constructor_exists():
    assert callable(ActionsProv::ReadStructuralFeatureAction.__init__)


def test_actionsprov::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CallOperationAction)


def test_actionsprov::calloperationaction_constructor_exists():
    assert callable(ActionsProv::CallOperationAction.__init__)


def test_actionsprov::calloperationaction_constructor_args():
    sig = inspect.signature(ActionsProv::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::StartObjectBehaviorAction)


def test_actionsprov::startobjectbehavioraction_constructor_exists():
    assert callable(ActionsProv::StartObjectBehaviorAction.__init__)


def test_actionsprov::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CallBehaviorAction)


def test_actionsprov::callbehavioraction_constructor_exists():
    assert callable(ActionsProv::CallBehaviorAction.__init__)


def test_actionsprov::callbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::action_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::Action)


def test_actionsprov::action_constructor_exists():
    assert callable(ActionsProv::Action.__init__)


def test_actionsprov::action_constructor_args():
    sig = inspect.signature(ActionsProv::Action.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::BroadcastSignalAction)


def test_actionsprov::broadcastsignalaction_constructor_exists():
    assert callable(ActionsProv::BroadcastSignalAction.__init__)


def test_actionsprov::broadcastsignalaction_constructor_args():
    sig = inspect.signature(ActionsProv::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::SendSignalAction)


def test_actionsprov::sendsignalaction_constructor_exists():
    assert callable(ActionsProv::SendSignalAction.__init__)


def test_actionsprov::sendsignalaction_constructor_args():
    sig = inspect.signature(ActionsProv::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::SendObjectAction)


def test_actionsprov::sendobjectaction_constructor_exists():
    assert callable(ActionsProv::SendObjectAction.__init__)


def test_actionsprov::sendobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::callaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CallAction)


def test_actionsprov::callaction_constructor_exists():
    assert callable(ActionsProv::CallAction.__init__)


def test_actionsprov::callaction_constructor_args():
    sig = inspect.signature(ActionsProv::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_actionsprov::callaction_has_isSynchronous():
    assert hasattr(ActionsProv::CallAction, "isSynchronous")
    descriptor = None
    for klass in ActionsProv::CallAction.__mro__:
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



def test_actionsprov::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ActionInputPin)


def test_actionsprov::actioninputpin_constructor_exists():
    assert callable(ActionsProv::ActionInputPin.__init__)


def test_actionsprov::actioninputpin_constructor_args():
    sig = inspect.signature(ActionsProv::ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::valuepin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ValuePin)


def test_actionsprov::valuepin_constructor_exists():
    assert callable(ActionsProv::ValuePin.__init__)


def test_actionsprov::valuepin_constructor_args():
    sig = inspect.signature(ActionsProv::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::pin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::Pin)


def test_actionsprov::pin_constructor_exists():
    assert callable(ActionsProv::Pin.__init__)


def test_actionsprov::pin_constructor_args():
    sig = inspect.signature(ActionsProv::Pin.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::inputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::InputPin)


def test_actionsprov::inputpin_constructor_exists():
    assert callable(ActionsProv::InputPin.__init__)


def test_actionsprov::inputpin_constructor_args():
    sig = inspect.signature(ActionsProv::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::StartClassifierBehaviorAction)


def test_actionsprov::startclassifierbehavioraction_constructor_exists():
    assert callable(ActionsProv::StartClassifierBehaviorAction.__init__)


def test_actionsprov::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(ActionsProv::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::linkaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::LinkAction)


def test_actionsprov::linkaction_constructor_exists():
    assert callable(ActionsProv::LinkAction.__init__)


def test_actionsprov::linkaction_constructor_args():
    sig = inspect.signature(ActionsProv::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::UnmarshallAction)


def test_actionsprov::unmarshallaction_constructor_exists():
    assert callable(ActionsProv::UnmarshallAction.__init__)


def test_actionsprov::unmarshallaction_constructor_args():
    sig = inspect.signature(ActionsProv::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadLinkObjectEndAction)


def test_actionsprov::readlinkobjectendaction_constructor_exists():
    assert callable(ActionsProv::ReadLinkObjectEndAction.__init__)


def test_actionsprov::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::AcceptEventAction)


def test_actionsprov::accepteventaction_constructor_exists():
    assert callable(ActionsProv::AcceptEventAction.__init__)


def test_actionsprov::accepteventaction_constructor_args():
    sig = inspect.signature(ActionsProv::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_actionsprov::accepteventaction_has_isUnmarshall():
    assert hasattr(ActionsProv::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in ActionsProv::AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov::variableaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::VariableAction)


def test_actionsprov::variableaction_constructor_exists():
    assert callable(ActionsProv::VariableAction.__init__)


def test_actionsprov::variableaction_constructor_args():
    sig = inspect.signature(ActionsProv::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::CreateObjectAction)


def test_actionsprov::createobjectaction_constructor_exists():
    assert callable(ActionsProv::CreateObjectAction.__init__)


def test_actionsprov::createobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::RaiseExceptionAction)


def test_actionsprov::raiseexceptionaction_constructor_exists():
    assert callable(ActionsProv::RaiseExceptionAction.__init__)


def test_actionsprov::raiseexceptionaction_constructor_args():
    sig = inspect.signature(ActionsProv::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::reduceaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReduceAction)


def test_actionsprov::reduceaction_constructor_exists():
    assert callable(ActionsProv::ReduceAction.__init__)


def test_actionsprov::reduceaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_actionsprov::reduceaction_has_isOrdered():
    assert hasattr(ActionsProv::ReduceAction, "isOrdered")
    descriptor = None
    for klass in ActionsProv::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadLinkObjectEndQualifierAction)


def test_actionsprov::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(ActionsProv::ReadLinkObjectEndQualifierAction.__init__)


def test_actionsprov::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::StructuralFeatureAction)


def test_actionsprov::structuralfeatureaction_constructor_exists():
    assert callable(ActionsProv::StructuralFeatureAction.__init__)


def test_actionsprov::structuralfeatureaction_constructor_args():
    sig = inspect.signature(ActionsProv::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::replyaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReplyAction)


def test_actionsprov::replyaction_constructor_exists():
    assert callable(ActionsProv::ReplyAction.__init__)


def test_actionsprov::replyaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::invocationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::InvocationAction)


def test_actionsprov::invocationaction_constructor_exists():
    assert callable(ActionsProv::InvocationAction.__init__)


def test_actionsprov::invocationaction_constructor_args():
    sig = inspect.signature(ActionsProv::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readextendaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadExtendAction)


def test_actionsprov::readextendaction_constructor_exists():
    assert callable(ActionsProv::ReadExtendAction.__init__)


def test_actionsprov::readextendaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::TestIdentityAction)


def test_actionsprov::testidentityaction_constructor_exists():
    assert callable(ActionsProv::TestIdentityAction.__init__)


def test_actionsprov::testidentityaction_constructor_args():
    sig = inspect.signature(ActionsProv::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::DestroyObjectAction)


def test_actionsprov::destroyobjectaction_constructor_exists():
    assert callable(ActionsProv::DestroyObjectAction.__init__)


def test_actionsprov::destroyobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::readselfaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReadSelfAction)


def test_actionsprov::readselfaction_constructor_exists():
    assert callable(ActionsProv::ReadSelfAction.__init__)


def test_actionsprov::readselfaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ValueSpecificationAction)


def test_actionsprov::valuespecificationaction_constructor_exists():
    assert callable(ActionsProv::ValueSpecificationAction.__init__)


def test_actionsprov::valuespecificationaction_constructor_args():
    sig = inspect.signature(ActionsProv::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_actionsprov::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::ReclassifyObjectAction)


def test_actionsprov::reclassifyobjectaction_constructor_exists():
    assert callable(ActionsProv::ReclassifyObjectAction.__init__)


def test_actionsprov::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(ActionsProv::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actionsprov::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(ActionsProv::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in ActionsProv::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::OpaqueAction)


def test_actionsprov::opaqueaction_constructor_exists():
    assert callable(ActionsProv::OpaqueAction.__init__)


def test_actionsprov::opaqueaction_constructor_args():
    sig = inspect.signature(ActionsProv::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_actionsprov::opaqueaction_has_language():
    assert hasattr(ActionsProv::OpaqueAction, "language")
    descriptor = None
    for klass in ActionsProv::OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_actionsprov::opaqueaction_has_body():
    assert hasattr(ActionsProv::OpaqueAction, "body")
    descriptor = None
    for klass in ActionsProv::OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_actionsprov::outputpin_is_not_abstract():
    assert not inspect.isabstract(ActionsProv::OutputPin)


def test_actionsprov::outputpin_constructor_exists():
    assert callable(ActionsProv::OutputPin.__init__)


def test_actionsprov::outputpin_constructor_args():
    sig = inspect.signature(ActionsProv::OutputPin.__init__)
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
ActionsProv::RemoveVariableValueAction_strategy = st.builds(
    ActionsProv::RemoveVariableValueAction,
)
ActionsProv::AddVariableValueAction_strategy = st.builds(
    ActionsProv::AddVariableValueAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
ActionsProv::ClearVariableAction_strategy = st.builds(
    ActionsProv::ClearVariableAction,
)
ActionsProv::WriteVariableAction_strategy = st.builds(
    ActionsProv::WriteVariableAction,
)
ActionsProv::ReadVariableAction_strategy = st.builds(
    ActionsProv::ReadVariableAction,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
ActionsProv::CreateLinkObjectAction_strategy = st.builds(
    ActionsProv::CreateLinkObjectAction,
)
ActionsProv::ReadlsClassifiedObjectAction_strategy = st.builds(
    ActionsProv::ReadlsClassifiedObjectAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
ActionsProv::AcceptCallAction_strategy = st.builds(
    ActionsProv::AcceptCallAction,
)
ActionsProv::QualifierValue_strategy = st.builds(
    ActionsProv::QualifierValue,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
ActionsProv::LinkEndDestructionData_strategy = st.builds(
    ActionsProv::LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
ActionsProv::LinkEndCreationData_strategy = st.builds(
    ActionsProv::LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
ActionsProv::DestroyLinkAction_strategy = st.builds(
    ActionsProv::DestroyLinkAction,
)
ActionsProv::CreateLinkAction_strategy = st.builds(
    ActionsProv::CreateLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
ActionsProv::WriteLinkAction_strategy = st.builds(
    ActionsProv::WriteLinkAction,
)
ActionsProv::ReadLinkAction_strategy = st.builds(
    ActionsProv::ReadLinkAction,
)
ActionsProv::LinkEndData_strategy = st.builds(
    ActionsProv::LinkEndData,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
ActionsProv::AddStructuralFeatureValueAction_strategy = st.builds(
    ActionsProv::AddStructuralFeatureValueAction,
)
ActionsProv::RemoveStructuralFeatureValueAction_strategy = st.builds(
    ActionsProv::RemoveStructuralFeatureValueAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
ActionsProv::WriteStructuralFeatureAction_strategy = st.builds(
    ActionsProv::WriteStructuralFeatureAction,
)
ActionsProv::ClearStructuralFeatureAction_strategy = st.builds(
    ActionsProv::ClearStructuralFeatureAction,
)
ActionsProv::ReadStructuralFeatureAction_strategy = st.builds(
    ActionsProv::ReadStructuralFeatureAction,
)
ActionsProv::CallOperationAction_strategy = st.builds(
    ActionsProv::CallOperationAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
ActionsProv::StartObjectBehaviorAction_strategy = st.builds(
    ActionsProv::StartObjectBehaviorAction,
)
ActionsProv::CallBehaviorAction_strategy = st.builds(
    ActionsProv::CallBehaviorAction,
)
ActionsProv::Action_strategy = st.builds(
    ActionsProv::Action,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
ActionsProv::BroadcastSignalAction_strategy = st.builds(
    ActionsProv::BroadcastSignalAction,
)
ActionsProv::SendSignalAction_strategy = st.builds(
    ActionsProv::SendSignalAction,
)
ActionsProv::SendObjectAction_strategy = st.builds(
    ActionsProv::SendObjectAction,
)
ActionsProv::CallAction_strategy = st.builds(
    ActionsProv::CallAction,
    isSynchronous=
        st.booleans()
)
InputPin_strategy = st.builds(
    InputPin,
)
ActionsProv::ActionInputPin_strategy = st.builds(
    ActionsProv::ActionInputPin,
)
ActionsProv::ValuePin_strategy = st.builds(
    ActionsProv::ValuePin,
)
ActionsProv::Pin_strategy = st.builds(
    ActionsProv::Pin,
)
Pin_strategy = st.builds(
    Pin,
)
ActionsProv::InputPin_strategy = st.builds(
    ActionsProv::InputPin,
)
Action_strategy = st.builds(
    Action,
)
ActionsProv::StartClassifierBehaviorAction_strategy = st.builds(
    ActionsProv::StartClassifierBehaviorAction,
)
ActionsProv::LinkAction_strategy = st.builds(
    ActionsProv::LinkAction,
)
ActionsProv::UnmarshallAction_strategy = st.builds(
    ActionsProv::UnmarshallAction,
)
ActionsProv::ReadLinkObjectEndAction_strategy = st.builds(
    ActionsProv::ReadLinkObjectEndAction,
)
ActionsProv::AcceptEventAction_strategy = st.builds(
    ActionsProv::AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
ActionsProv::VariableAction_strategy = st.builds(
    ActionsProv::VariableAction,
)
ActionsProv::CreateObjectAction_strategy = st.builds(
    ActionsProv::CreateObjectAction,
)
ActionsProv::RaiseExceptionAction_strategy = st.builds(
    ActionsProv::RaiseExceptionAction,
)
ActionsProv::ReduceAction_strategy = st.builds(
    ActionsProv::ReduceAction,
    isOrdered=
        st.booleans()
)
ActionsProv::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    ActionsProv::ReadLinkObjectEndQualifierAction,
)
ActionsProv::StructuralFeatureAction_strategy = st.builds(
    ActionsProv::StructuralFeatureAction,
)
ActionsProv::ReplyAction_strategy = st.builds(
    ActionsProv::ReplyAction,
)
ActionsProv::InvocationAction_strategy = st.builds(
    ActionsProv::InvocationAction,
)
ActionsProv::ReadExtendAction_strategy = st.builds(
    ActionsProv::ReadExtendAction,
)
ActionsProv::TestIdentityAction_strategy = st.builds(
    ActionsProv::TestIdentityAction,
)
ActionsProv::DestroyObjectAction_strategy = st.builds(
    ActionsProv::DestroyObjectAction,
)
ActionsProv::ReadSelfAction_strategy = st.builds(
    ActionsProv::ReadSelfAction,
)
ActionsProv::ValueSpecificationAction_strategy = st.builds(
    ActionsProv::ValueSpecificationAction,
)
ActionsProv::ReclassifyObjectAction_strategy = st.builds(
    ActionsProv::ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
ActionsProv::OpaqueAction_strategy = st.builds(
    ActionsProv::OpaqueAction,
    language=
        safe_text,
    body=
        safe_text
)
ActionsProv::OutputPin_strategy = st.builds(
    ActionsProv::OutputPin,
)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=ActionsProv::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::RemoveVariableValueAction)

@given(instance=ActionsProv::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::AddVariableValueAction)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=ActionsProv::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov::clearvariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ClearVariableAction)

@given(instance=ActionsProv::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov::writevariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::WriteVariableAction)

@given(instance=ActionsProv::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readvariableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadVariableAction)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=ActionsProv::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CreateLinkObjectAction)

@given(instance=ActionsProv::ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadlsClassifiedObjectAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=ActionsProv::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_actionsprov::acceptcallaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::AcceptCallAction)

@given(instance=ActionsProv::QualifierValue_strategy)
@settings(max_examples=50)
def test_actionsprov::qualifiervalue_instantiation(instance):
    assert isinstance(instance, ActionsProv::QualifierValue)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=ActionsProv::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_actionsprov::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, ActionsProv::LinkEndDestructionData)

@given(instance=ActionsProv::LinkEndDestructionData_strategy)
def test_actionsprov::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, bool)


@given(instance=ActionsProv::LinkEndDestructionData_strategy)
def test_actionsprov::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=ActionsProv::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_actionsprov::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, ActionsProv::LinkEndCreationData)

@given(instance=ActionsProv::LinkEndCreationData_strategy)
def test_actionsprov::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=ActionsProv::LinkEndCreationData_strategy)
def test_actionsprov::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=ActionsProv::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov::destroylinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::DestroyLinkAction)

@given(instance=ActionsProv::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov::createlinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CreateLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=ActionsProv::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov::writelinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::WriteLinkAction)

@given(instance=ActionsProv::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readlinkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadLinkAction)

@given(instance=ActionsProv::LinkEndData_strategy)
@settings(max_examples=50)
def test_actionsprov::linkenddata_instantiation(instance):
    assert isinstance(instance, ActionsProv::LinkEndData)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=ActionsProv::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::AddStructuralFeatureValueAction)

@given(instance=ActionsProv::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actionsprov::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::RemoveStructuralFeatureValueAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=ActionsProv::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::WriteStructuralFeatureAction)

@given(instance=ActionsProv::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ClearStructuralFeatureAction)

@given(instance=ActionsProv::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadStructuralFeatureAction)

@given(instance=ActionsProv::CallOperationAction_strategy)
@settings(max_examples=50)
def test_actionsprov::calloperationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CallOperationAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=ActionsProv::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv::StartObjectBehaviorAction)

@given(instance=ActionsProv::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov::callbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CallBehaviorAction)

@given(instance=ActionsProv::Action_strategy)
@settings(max_examples=50)
def test_actionsprov::action_instantiation(instance):
    assert isinstance(instance, ActionsProv::Action)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=ActionsProv::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_actionsprov::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::BroadcastSignalAction)

@given(instance=ActionsProv::SendSignalAction_strategy)
@settings(max_examples=50)
def test_actionsprov::sendsignalaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::SendSignalAction)

@given(instance=ActionsProv::SendObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::sendobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::SendObjectAction)

@given(instance=ActionsProv::CallAction_strategy)
@settings(max_examples=50)
def test_actionsprov::callaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CallAction)

@given(instance=ActionsProv::CallAction_strategy)
def test_actionsprov::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, bool)


@given(instance=ActionsProv::CallAction_strategy)
def test_actionsprov::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=ActionsProv::ActionInputPin_strategy)
@settings(max_examples=50)
def test_actionsprov::actioninputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv::ActionInputPin)

@given(instance=ActionsProv::ValuePin_strategy)
@settings(max_examples=50)
def test_actionsprov::valuepin_instantiation(instance):
    assert isinstance(instance, ActionsProv::ValuePin)

@given(instance=ActionsProv::Pin_strategy)
@settings(max_examples=50)
def test_actionsprov::pin_instantiation(instance):
    assert isinstance(instance, ActionsProv::Pin)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ActionsProv::InputPin_strategy)
@settings(max_examples=50)
def test_actionsprov::inputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv::InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=ActionsProv::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_actionsprov::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, ActionsProv::StartClassifierBehaviorAction)

@given(instance=ActionsProv::LinkAction_strategy)
@settings(max_examples=50)
def test_actionsprov::linkaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::LinkAction)

@given(instance=ActionsProv::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_actionsprov::unmarshallaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::UnmarshallAction)

@given(instance=ActionsProv::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadLinkObjectEndAction)

@given(instance=ActionsProv::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_actionsprov::accepteventaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::AcceptEventAction)

@given(instance=ActionsProv::AcceptEventAction_strategy)
def test_actionsprov::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, bool)


@given(instance=ActionsProv::AcceptEventAction_strategy)
def test_actionsprov::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=ActionsProv::VariableAction_strategy)
@settings(max_examples=50)
def test_actionsprov::variableaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::VariableAction)

@given(instance=ActionsProv::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::createobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::CreateObjectAction)

@given(instance=ActionsProv::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_actionsprov::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::RaiseExceptionAction)

@given(instance=ActionsProv::ReduceAction_strategy)
@settings(max_examples=50)
def test_actionsprov::reduceaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReduceAction)

@given(instance=ActionsProv::ReduceAction_strategy)
def test_actionsprov::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=ActionsProv::ReduceAction_strategy)
def test_actionsprov::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=ActionsProv::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadLinkObjectEndQualifierAction)

@given(instance=ActionsProv::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actionsprov::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::StructuralFeatureAction)

@given(instance=ActionsProv::ReplyAction_strategy)
@settings(max_examples=50)
def test_actionsprov::replyaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReplyAction)

@given(instance=ActionsProv::InvocationAction_strategy)
@settings(max_examples=50)
def test_actionsprov::invocationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::InvocationAction)

@given(instance=ActionsProv::ReadExtendAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readextendaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadExtendAction)

@given(instance=ActionsProv::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_actionsprov::testidentityaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::TestIdentityAction)

@given(instance=ActionsProv::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::DestroyObjectAction)

@given(instance=ActionsProv::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_actionsprov::readselfaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReadSelfAction)

@given(instance=ActionsProv::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_actionsprov::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ValueSpecificationAction)

@given(instance=ActionsProv::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_actionsprov::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::ReclassifyObjectAction)

@given(instance=ActionsProv::ReclassifyObjectAction_strategy)
def test_actionsprov::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=ActionsProv::ReclassifyObjectAction_strategy)
def test_actionsprov::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=ActionsProv::OpaqueAction_strategy)
@settings(max_examples=50)
def test_actionsprov::opaqueaction_instantiation(instance):
    assert isinstance(instance, ActionsProv::OpaqueAction)

@given(instance=ActionsProv::OpaqueAction_strategy)
def test_actionsprov::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=ActionsProv::OpaqueAction_strategy)
def test_actionsprov::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=ActionsProv::OpaqueAction_strategy)
def test_actionsprov::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=ActionsProv::OpaqueAction_strategy)
def test_actionsprov::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ActionsProv::OutputPin_strategy)
@settings(max_examples=50)
def test_actionsprov::outputpin_instantiation(instance):
    assert isinstance(instance, ActionsProv::OutputPin)
