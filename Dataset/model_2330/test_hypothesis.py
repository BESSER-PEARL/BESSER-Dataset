import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VariableAction,
    Actions::StructuredActions::ReadVariableAction,
    Actions::StructuredActions::Variable,
    Variable,
    CreateLinkAction,
    Actions::CompleteActions::CreateLinkObjectAction,
    Actions::StructuredActions::ClearVariableAction,
    WriteVariableAction,
    Actions::StructuredActions::RemoveVariableValueAction,
    Actions::StructuredActions::AddVariableValueAction,
    Actions::StructuredActions::WriteVariableAction,
    Actions::CompleteActions::ReadlsClassifiedObjectAction,
    Trigger,
    Actions::CompleteActions::Trigger,
    AcceptEventAction,
    Actions::CompleteActions::AcceptCallAction,
    Actions::IntermediateActions::Property,
    QualifierValue,
    Property,
    Element,
    Actions::CompleteActions::QualifierValue,
    Actions::IntermediateActions::LinkEndData,
    LinkEndData,
    Actions::IntermediateActions::LinkEndDestructionData,
    WriteStructuralFeatureAction,
    Actions::IntermediateActions::RemoveStructuralFeatureValueAction,
    Actions::IntermediateActions::AddStructuralFeatureValueAction,
    Actions::IntermediateActions::Element,
    Actions::IntermediateActions::LinkEndCreationData,
    WriteLinkAction,
    Actions::IntermediateActions::DestroyLinkAction,
    Actions::IntermediateActions::CreateLinkAction,
    LinkAction,
    Actions::IntermediateActions::WriteLinkAction,
    Actions::IntermediateActions::ReadLinkAction,
    StructuralFeature,
    StructuralFeatureAction,
    Actions::IntermediateActions::WriteStructuralFeatureAction,
    Actions::IntermediateActions::ClearStructuralFeatureAction,
    Actions::IntermediateActions::ReadStructuralFeatureAction,
    Actions::IntermediateActions::StructuralFeature,
    Signal,
    Actions::BasicActions::Operation,
    Operation,
    Actions::BasicActions::CallOperationAction,
    Actions::BasicActions::Behavior,
    Behavior,
    CallAction,
    Actions::CompleteActions::StartObjectBehaviorAction,
    Actions::BasicActions::CallBehaviorAction,
    InvocationAction,
    Actions::BasicActions::SendSignalAction,
    Actions::BasicActions::CallAction,
    Actions::IntermediateActions::SendObjectAction,
    Actions::IntermediateActions::BroadcastSignalAction,
    Actions::BasicActions::Signal,
    Pin,
    Actions::BasicActions::InputPin,
    Action,
    Actions::IntermediateActions::DestroyObjectAction,
    Actions::IntermediateActions::TestIdentityAction,
    Actions::CompleteActions::AcceptEventAction,
    Actions::CompleteActions::ReadLinkObjectEndQualifierAction,
    Actions::IntermediateActions::LinkAction,
    Actions::IntermediateActions::ValueSpecificationAction,
    Actions::CompleteActions::ReadLinkObjectEndAction,
    Actions::CompleteActions::ReadExtendAction,
    Actions::IntermediateActions::StructuralFeatureAction,
    Actions::StructuredActions::VariableAction,
    Actions::CompleteActions::UnmarshallAction,
    Actions::CompleteActions::ReclassifyObjectAction,
    Actions::IntermediateActions::ReadSelfAction,
    Actions::CompleteActions::ReplyAction,
    Actions::IntermediateActions::CreateObjectAction,
    Actions::StructuredActions::RaiseExceptionAction,
    Actions::CompleteActions::ReduceAction,
    Actions::CompleteActions::StartClassifierBehaviorAction,
    Actions::BasicActions::OpaqueAction,
    Actions::BasicActions::Classifier,
    Actions::BasicActions::NamedElement,
    OutputPin,
    InputPin,
    Actions::StructuredActions::ActionInputPin,
    Classifier,
    NamedElement,
    Actions::BasicActions::Action,
    Actions::BasicActions::InvocationAction,
    Actions::BasicActions::ValueSpecification,
    ValueSpecification,
    Actions::BasicActions::ValuePin,
    Actions::BasicActions::TypedElement,
    Actions::BasicActions::MultiplicityElement,
    BasicActions::MultiplicityElement,
    BasicActions::TypedElement,
    Actions::BasicActions::Pin,
    Actions::BasicActions::OutputPin,
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



def test_actions::structuredactions::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::ReadVariableAction)


def test_actions::structuredactions::readvariableaction_constructor_exists():
    assert callable(Actions::StructuredActions::ReadVariableAction.__init__)


def test_actions::structuredactions::readvariableaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::variable_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::Variable)


def test_actions::structuredactions::variable_constructor_exists():
    assert callable(Actions::StructuredActions::Variable.__init__)


def test_actions::structuredactions::variable_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::Variable.__init__)
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



def test_actions::completeactions::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::CreateLinkObjectAction)


def test_actions::completeactions::createlinkobjectaction_constructor_exists():
    assert callable(Actions::CompleteActions::CreateLinkObjectAction.__init__)


def test_actions::completeactions::createlinkobjectaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::ClearVariableAction)


def test_actions::structuredactions::clearvariableaction_constructor_exists():
    assert callable(Actions::StructuredActions::ClearVariableAction.__init__)


def test_actions::structuredactions::clearvariableaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::RemoveVariableValueAction)


def test_actions::structuredactions::removevariablevalueaction_constructor_exists():
    assert callable(Actions::StructuredActions::RemoveVariableValueAction.__init__)


def test_actions::structuredactions::removevariablevalueaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::AddVariableValueAction)


def test_actions::structuredactions::addvariablevalueaction_constructor_exists():
    assert callable(Actions::StructuredActions::AddVariableValueAction.__init__)


def test_actions::structuredactions::addvariablevalueaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::WriteVariableAction)


def test_actions::structuredactions::writevariableaction_constructor_exists():
    assert callable(Actions::StructuredActions::WriteVariableAction.__init__)


def test_actions::structuredactions::writevariableaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReadlsClassifiedObjectAction)


def test_actions::completeactions::readlsclassifiedobjectaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReadlsClassifiedObjectAction.__init__)


def test_actions::completeactions::readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::trigger_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::Trigger)


def test_actions::completeactions::trigger_constructor_exists():
    assert callable(Actions::CompleteActions::Trigger.__init__)


def test_actions::completeactions::trigger_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::AcceptCallAction)


def test_actions::completeactions::acceptcallaction_constructor_exists():
    assert callable(Actions::CompleteActions::AcceptCallAction.__init__)


def test_actions::completeactions::acceptcallaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::property_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::Property)


def test_actions::intermediateactions::property_constructor_exists():
    assert callable(Actions::IntermediateActions::Property.__init__)


def test_actions::intermediateactions::property_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::Property.__init__)
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



def test_actions::completeactions::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::QualifierValue)


def test_actions::completeactions::qualifiervalue_constructor_exists():
    assert callable(Actions::CompleteActions::QualifierValue.__init__)


def test_actions::completeactions::qualifiervalue_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::LinkEndData)


def test_actions::intermediateactions::linkenddata_constructor_exists():
    assert callable(Actions::IntermediateActions::LinkEndData.__init__)


def test_actions::intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::LinkEndDestructionData)


def test_actions::intermediateactions::linkenddestructiondata_constructor_exists():
    assert callable(Actions::IntermediateActions::LinkEndDestructionData.__init__)


def test_actions::intermediateactions::linkenddestructiondata_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_actions::intermediateactions::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(Actions::IntermediateActions::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in Actions::IntermediateActions::LinkEndDestructionData.__mro__:
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



def test_actions::intermediateactions::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::RemoveStructuralFeatureValueAction)


def test_actions::intermediateactions::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(Actions::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)


def test_actions::intermediateactions::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::AddStructuralFeatureValueAction)


def test_actions::intermediateactions::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(Actions::IntermediateActions::AddStructuralFeatureValueAction.__init__)


def test_actions::intermediateactions::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::element_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::Element)


def test_actions::intermediateactions::element_constructor_exists():
    assert callable(Actions::IntermediateActions::Element.__init__)


def test_actions::intermediateactions::element_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::Element.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::LinkEndCreationData)


def test_actions::intermediateactions::linkendcreationdata_constructor_exists():
    assert callable(Actions::IntermediateActions::LinkEndCreationData.__init__)


def test_actions::intermediateactions::linkendcreationdata_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actions::intermediateactions::linkendcreationdata_has_isReplaceAll():
    assert hasattr(Actions::IntermediateActions::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in Actions::IntermediateActions::LinkEndCreationData.__mro__:
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



def test_actions::intermediateactions::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::DestroyLinkAction)


def test_actions::intermediateactions::destroylinkaction_constructor_exists():
    assert callable(Actions::IntermediateActions::DestroyLinkAction.__init__)


def test_actions::intermediateactions::destroylinkaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::CreateLinkAction)


def test_actions::intermediateactions::createlinkaction_constructor_exists():
    assert callable(Actions::IntermediateActions::CreateLinkAction.__init__)


def test_actions::intermediateactions::createlinkaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::WriteLinkAction)


def test_actions::intermediateactions::writelinkaction_constructor_exists():
    assert callable(Actions::IntermediateActions::WriteLinkAction.__init__)


def test_actions::intermediateactions::writelinkaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::ReadLinkAction)


def test_actions::intermediateactions::readlinkaction_constructor_exists():
    assert callable(Actions::IntermediateActions::ReadLinkAction.__init__)


def test_actions::intermediateactions::readlinkaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::ReadLinkAction.__init__)
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



def test_actions::intermediateactions::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::WriteStructuralFeatureAction)


def test_actions::intermediateactions::writestructuralfeatureaction_constructor_exists():
    assert callable(Actions::IntermediateActions::WriteStructuralFeatureAction.__init__)


def test_actions::intermediateactions::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::ClearStructuralFeatureAction)


def test_actions::intermediateactions::clearstructuralfeatureaction_constructor_exists():
    assert callable(Actions::IntermediateActions::ClearStructuralFeatureAction.__init__)


def test_actions::intermediateactions::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::ReadStructuralFeatureAction)


def test_actions::intermediateactions::readstructuralfeatureaction_constructor_exists():
    assert callable(Actions::IntermediateActions::ReadStructuralFeatureAction.__init__)


def test_actions::intermediateactions::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::StructuralFeature)


def test_actions::intermediateactions::structuralfeature_constructor_exists():
    assert callable(Actions::IntermediateActions::StructuralFeature.__init__)


def test_actions::intermediateactions::structuralfeature_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::operation_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Operation)


def test_actions::basicactions::operation_constructor_exists():
    assert callable(Actions::BasicActions::Operation.__init__)


def test_actions::basicactions::operation_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Operation.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::CallOperationAction)


def test_actions::basicactions::calloperationaction_constructor_exists():
    assert callable(Actions::BasicActions::CallOperationAction.__init__)


def test_actions::basicactions::calloperationaction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::behavior_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Behavior)


def test_actions::basicactions::behavior_constructor_exists():
    assert callable(Actions::BasicActions::Behavior.__init__)


def test_actions::basicactions::behavior_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Behavior.__init__)
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



def test_actions::completeactions::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::StartObjectBehaviorAction)


def test_actions::completeactions::startobjectbehavioraction_constructor_exists():
    assert callable(Actions::CompleteActions::StartObjectBehaviorAction.__init__)


def test_actions::completeactions::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::CallBehaviorAction)


def test_actions::basicactions::callbehavioraction_constructor_exists():
    assert callable(Actions::BasicActions::CallBehaviorAction.__init__)


def test_actions::basicactions::callbehavioraction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::SendSignalAction)


def test_actions::basicactions::sendsignalaction_constructor_exists():
    assert callable(Actions::BasicActions::SendSignalAction.__init__)


def test_actions::basicactions::sendsignalaction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::callaction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::CallAction)


def test_actions::basicactions::callaction_constructor_exists():
    assert callable(Actions::BasicActions::CallAction.__init__)


def test_actions::basicactions::callaction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_actions::basicactions::callaction_has_isSynchronous():
    assert hasattr(Actions::BasicActions::CallAction, "isSynchronous")
    descriptor = None
    for klass in Actions::BasicActions::CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_actions::intermediateactions::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::SendObjectAction)


def test_actions::intermediateactions::sendobjectaction_constructor_exists():
    assert callable(Actions::IntermediateActions::SendObjectAction.__init__)


def test_actions::intermediateactions::sendobjectaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::BroadcastSignalAction)


def test_actions::intermediateactions::broadcastsignalaction_constructor_exists():
    assert callable(Actions::IntermediateActions::BroadcastSignalAction.__init__)


def test_actions::intermediateactions::broadcastsignalaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::signal_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Signal)


def test_actions::basicactions::signal_constructor_exists():
    assert callable(Actions::BasicActions::Signal.__init__)


def test_actions::basicactions::signal_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Signal.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::inputpin_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::InputPin)


def test_actions::basicactions::inputpin_constructor_exists():
    assert callable(Actions::BasicActions::InputPin.__init__)


def test_actions::basicactions::inputpin_constructor_args():
    sig = inspect.signature(Actions::BasicActions::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::DestroyObjectAction)


def test_actions::intermediateactions::destroyobjectaction_constructor_exists():
    assert callable(Actions::IntermediateActions::DestroyObjectAction.__init__)


def test_actions::intermediateactions::destroyobjectaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::TestIdentityAction)


def test_actions::intermediateactions::testidentityaction_constructor_exists():
    assert callable(Actions::IntermediateActions::TestIdentityAction.__init__)


def test_actions::intermediateactions::testidentityaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::AcceptEventAction)


def test_actions::completeactions::accepteventaction_constructor_exists():
    assert callable(Actions::CompleteActions::AcceptEventAction.__init__)


def test_actions::completeactions::accepteventaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_actions::completeactions::accepteventaction_has_isUnmarshall():
    assert hasattr(Actions::CompleteActions::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in Actions::CompleteActions::AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_actions::completeactions::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReadLinkObjectEndQualifierAction)


def test_actions::completeactions::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(Actions::CompleteActions::ReadLinkObjectEndQualifierAction.__init__)


def test_actions::completeactions::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::linkaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::LinkAction)


def test_actions::intermediateactions::linkaction_constructor_exists():
    assert callable(Actions::IntermediateActions::LinkAction.__init__)


def test_actions::intermediateactions::linkaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::ValueSpecificationAction)


def test_actions::intermediateactions::valuespecificationaction_constructor_exists():
    assert callable(Actions::IntermediateActions::ValueSpecificationAction.__init__)


def test_actions::intermediateactions::valuespecificationaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReadLinkObjectEndAction)


def test_actions::completeactions::readlinkobjectendaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReadLinkObjectEndAction.__init__)


def test_actions::completeactions::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::readextendaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReadExtendAction)


def test_actions::completeactions::readextendaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReadExtendAction.__init__)


def test_actions::completeactions::readextendaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::StructuralFeatureAction)


def test_actions::intermediateactions::structuralfeatureaction_constructor_exists():
    assert callable(Actions::IntermediateActions::StructuralFeatureAction.__init__)


def test_actions::intermediateactions::structuralfeatureaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::variableaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::VariableAction)


def test_actions::structuredactions::variableaction_constructor_exists():
    assert callable(Actions::StructuredActions::VariableAction.__init__)


def test_actions::structuredactions::variableaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::UnmarshallAction)


def test_actions::completeactions::unmarshallaction_constructor_exists():
    assert callable(Actions::CompleteActions::UnmarshallAction.__init__)


def test_actions::completeactions::unmarshallaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReclassifyObjectAction)


def test_actions::completeactions::reclassifyobjectaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReclassifyObjectAction.__init__)


def test_actions::completeactions::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_actions::completeactions::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(Actions::CompleteActions::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in Actions::CompleteActions::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_actions::intermediateactions::readselfaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::ReadSelfAction)


def test_actions::intermediateactions::readselfaction_constructor_exists():
    assert callable(Actions::IntermediateActions::ReadSelfAction.__init__)


def test_actions::intermediateactions::readselfaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::replyaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReplyAction)


def test_actions::completeactions::replyaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReplyAction.__init__)


def test_actions::completeactions::replyaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::intermediateactions::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(Actions::IntermediateActions::CreateObjectAction)


def test_actions::intermediateactions::createobjectaction_constructor_exists():
    assert callable(Actions::IntermediateActions::CreateObjectAction.__init__)


def test_actions::intermediateactions::createobjectaction_constructor_args():
    sig = inspect.signature(Actions::IntermediateActions::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::structuredactions::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::RaiseExceptionAction)


def test_actions::structuredactions::raiseexceptionaction_constructor_exists():
    assert callable(Actions::StructuredActions::RaiseExceptionAction.__init__)


def test_actions::structuredactions::raiseexceptionaction_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::completeactions::reduceaction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::ReduceAction)


def test_actions::completeactions::reduceaction_constructor_exists():
    assert callable(Actions::CompleteActions::ReduceAction.__init__)


def test_actions::completeactions::reduceaction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_actions::completeactions::reduceaction_has_isOrdered():
    assert hasattr(Actions::CompleteActions::ReduceAction, "isOrdered")
    descriptor = None
    for klass in Actions::CompleteActions::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_actions::completeactions::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(Actions::CompleteActions::StartClassifierBehaviorAction)


def test_actions::completeactions::startclassifierbehavioraction_constructor_exists():
    assert callable(Actions::CompleteActions::StartClassifierBehaviorAction.__init__)


def test_actions::completeactions::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(Actions::CompleteActions::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::OpaqueAction)


def test_actions::basicactions::opaqueaction_constructor_exists():
    assert callable(Actions::BasicActions::OpaqueAction.__init__)


def test_actions::basicactions::opaqueaction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_actions::basicactions::opaqueaction_has_body():
    assert hasattr(Actions::BasicActions::OpaqueAction, "body")
    descriptor = None
    for klass in Actions::BasicActions::OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_actions::basicactions::opaqueaction_has_language():
    assert hasattr(Actions::BasicActions::OpaqueAction, "language")
    descriptor = None
    for klass in Actions::BasicActions::OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_actions::basicactions::classifier_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Classifier)


def test_actions::basicactions::classifier_constructor_exists():
    assert callable(Actions::BasicActions::Classifier.__init__)


def test_actions::basicactions::classifier_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::namedelement_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::NamedElement)


def test_actions::basicactions::namedelement_constructor_exists():
    assert callable(Actions::BasicActions::NamedElement.__init__)


def test_actions::basicactions::namedelement_constructor_args():
    sig = inspect.signature(Actions::BasicActions::NamedElement.__init__)
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



def test_actions::structuredactions::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(Actions::StructuredActions::ActionInputPin)


def test_actions::structuredactions::actioninputpin_constructor_exists():
    assert callable(Actions::StructuredActions::ActionInputPin.__init__)


def test_actions::structuredactions::actioninputpin_constructor_args():
    sig = inspect.signature(Actions::StructuredActions::ActionInputPin.__init__)
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



def test_actions::basicactions::action_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Action)


def test_actions::basicactions::action_constructor_exists():
    assert callable(Actions::BasicActions::Action.__init__)


def test_actions::basicactions::action_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Action.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::invocationaction_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::InvocationAction)


def test_actions::basicactions::invocationaction_constructor_exists():
    assert callable(Actions::BasicActions::InvocationAction.__init__)


def test_actions::basicactions::invocationaction_constructor_args():
    sig = inspect.signature(Actions::BasicActions::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::valuespecification_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::ValueSpecification)


def test_actions::basicactions::valuespecification_constructor_exists():
    assert callable(Actions::BasicActions::ValueSpecification.__init__)


def test_actions::basicactions::valuespecification_constructor_args():
    sig = inspect.signature(Actions::BasicActions::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::valuepin_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::ValuePin)


def test_actions::basicactions::valuepin_constructor_exists():
    assert callable(Actions::BasicActions::ValuePin.__init__)


def test_actions::basicactions::valuepin_constructor_args():
    sig = inspect.signature(Actions::BasicActions::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::typedelement_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::TypedElement)


def test_actions::basicactions::typedelement_constructor_exists():
    assert callable(Actions::BasicActions::TypedElement.__init__)


def test_actions::basicactions::typedelement_constructor_args():
    sig = inspect.signature(Actions::BasicActions::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::MultiplicityElement)


def test_actions::basicactions::multiplicityelement_constructor_exists():
    assert callable(Actions::BasicActions::MultiplicityElement.__init__)


def test_actions::basicactions::multiplicityelement_constructor_args():
    sig = inspect.signature(Actions::BasicActions::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(BasicActions::MultiplicityElement)


def test_basicactions::multiplicityelement_constructor_exists():
    assert callable(BasicActions::MultiplicityElement.__init__)


def test_basicactions::multiplicityelement_constructor_args():
    sig = inspect.signature(BasicActions::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::typedelement_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TypedElement)


def test_basicactions::typedelement_constructor_exists():
    assert callable(BasicActions::TypedElement.__init__)


def test_basicactions::typedelement_constructor_args():
    sig = inspect.signature(BasicActions::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::pin_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::Pin)


def test_actions::basicactions::pin_constructor_exists():
    assert callable(Actions::BasicActions::Pin.__init__)


def test_actions::basicactions::pin_constructor_args():
    sig = inspect.signature(Actions::BasicActions::Pin.__init__)
    params = list(sig.parameters.keys())



def test_actions::basicactions::outputpin_is_not_abstract():
    assert not inspect.isabstract(Actions::BasicActions::OutputPin)


def test_actions::basicactions::outputpin_constructor_exists():
    assert callable(Actions::BasicActions::OutputPin.__init__)


def test_actions::basicactions::outputpin_constructor_args():
    sig = inspect.signature(Actions::BasicActions::OutputPin.__init__)
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
Actions::StructuredActions::ReadVariableAction_strategy = st.builds(
    Actions::StructuredActions::ReadVariableAction,
)
Actions::StructuredActions::Variable_strategy = st.builds(
    Actions::StructuredActions::Variable,
)
Variable_strategy = st.builds(
    Variable,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
Actions::CompleteActions::CreateLinkObjectAction_strategy = st.builds(
    Actions::CompleteActions::CreateLinkObjectAction,
)
Actions::StructuredActions::ClearVariableAction_strategy = st.builds(
    Actions::StructuredActions::ClearVariableAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
Actions::StructuredActions::RemoveVariableValueAction_strategy = st.builds(
    Actions::StructuredActions::RemoveVariableValueAction,
)
Actions::StructuredActions::AddVariableValueAction_strategy = st.builds(
    Actions::StructuredActions::AddVariableValueAction,
)
Actions::StructuredActions::WriteVariableAction_strategy = st.builds(
    Actions::StructuredActions::WriteVariableAction,
)
Actions::CompleteActions::ReadlsClassifiedObjectAction_strategy = st.builds(
    Actions::CompleteActions::ReadlsClassifiedObjectAction,
)
Trigger_strategy = st.builds(
    Trigger,
)
Actions::CompleteActions::Trigger_strategy = st.builds(
    Actions::CompleteActions::Trigger,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
Actions::CompleteActions::AcceptCallAction_strategy = st.builds(
    Actions::CompleteActions::AcceptCallAction,
)
Actions::IntermediateActions::Property_strategy = st.builds(
    Actions::IntermediateActions::Property,
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
Actions::CompleteActions::QualifierValue_strategy = st.builds(
    Actions::CompleteActions::QualifierValue,
)
Actions::IntermediateActions::LinkEndData_strategy = st.builds(
    Actions::IntermediateActions::LinkEndData,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
Actions::IntermediateActions::LinkEndDestructionData_strategy = st.builds(
    Actions::IntermediateActions::LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
Actions::IntermediateActions::RemoveStructuralFeatureValueAction_strategy = st.builds(
    Actions::IntermediateActions::RemoveStructuralFeatureValueAction,
)
Actions::IntermediateActions::AddStructuralFeatureValueAction_strategy = st.builds(
    Actions::IntermediateActions::AddStructuralFeatureValueAction,
)
Actions::IntermediateActions::Element_strategy = st.builds(
    Actions::IntermediateActions::Element,
)
Actions::IntermediateActions::LinkEndCreationData_strategy = st.builds(
    Actions::IntermediateActions::LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
Actions::IntermediateActions::DestroyLinkAction_strategy = st.builds(
    Actions::IntermediateActions::DestroyLinkAction,
)
Actions::IntermediateActions::CreateLinkAction_strategy = st.builds(
    Actions::IntermediateActions::CreateLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
Actions::IntermediateActions::WriteLinkAction_strategy = st.builds(
    Actions::IntermediateActions::WriteLinkAction,
)
Actions::IntermediateActions::ReadLinkAction_strategy = st.builds(
    Actions::IntermediateActions::ReadLinkAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
Actions::IntermediateActions::WriteStructuralFeatureAction_strategy = st.builds(
    Actions::IntermediateActions::WriteStructuralFeatureAction,
)
Actions::IntermediateActions::ClearStructuralFeatureAction_strategy = st.builds(
    Actions::IntermediateActions::ClearStructuralFeatureAction,
)
Actions::IntermediateActions::ReadStructuralFeatureAction_strategy = st.builds(
    Actions::IntermediateActions::ReadStructuralFeatureAction,
)
Actions::IntermediateActions::StructuralFeature_strategy = st.builds(
    Actions::IntermediateActions::StructuralFeature,
)
Signal_strategy = st.builds(
    Signal,
)
Actions::BasicActions::Operation_strategy = st.builds(
    Actions::BasicActions::Operation,
)
Operation_strategy = st.builds(
    Operation,
)
Actions::BasicActions::CallOperationAction_strategy = st.builds(
    Actions::BasicActions::CallOperationAction,
)
Actions::BasicActions::Behavior_strategy = st.builds(
    Actions::BasicActions::Behavior,
)
Behavior_strategy = st.builds(
    Behavior,
)
CallAction_strategy = st.builds(
    CallAction,
)
Actions::CompleteActions::StartObjectBehaviorAction_strategy = st.builds(
    Actions::CompleteActions::StartObjectBehaviorAction,
)
Actions::BasicActions::CallBehaviorAction_strategy = st.builds(
    Actions::BasicActions::CallBehaviorAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
Actions::BasicActions::SendSignalAction_strategy = st.builds(
    Actions::BasicActions::SendSignalAction,
)
Actions::BasicActions::CallAction_strategy = st.builds(
    Actions::BasicActions::CallAction,
    isSynchronous=
        st.booleans()
)
Actions::IntermediateActions::SendObjectAction_strategy = st.builds(
    Actions::IntermediateActions::SendObjectAction,
)
Actions::IntermediateActions::BroadcastSignalAction_strategy = st.builds(
    Actions::IntermediateActions::BroadcastSignalAction,
)
Actions::BasicActions::Signal_strategy = st.builds(
    Actions::BasicActions::Signal,
)
Pin_strategy = st.builds(
    Pin,
)
Actions::BasicActions::InputPin_strategy = st.builds(
    Actions::BasicActions::InputPin,
)
Action_strategy = st.builds(
    Action,
)
Actions::IntermediateActions::DestroyObjectAction_strategy = st.builds(
    Actions::IntermediateActions::DestroyObjectAction,
)
Actions::IntermediateActions::TestIdentityAction_strategy = st.builds(
    Actions::IntermediateActions::TestIdentityAction,
)
Actions::CompleteActions::AcceptEventAction_strategy = st.builds(
    Actions::CompleteActions::AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
Actions::CompleteActions::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    Actions::CompleteActions::ReadLinkObjectEndQualifierAction,
)
Actions::IntermediateActions::LinkAction_strategy = st.builds(
    Actions::IntermediateActions::LinkAction,
)
Actions::IntermediateActions::ValueSpecificationAction_strategy = st.builds(
    Actions::IntermediateActions::ValueSpecificationAction,
)
Actions::CompleteActions::ReadLinkObjectEndAction_strategy = st.builds(
    Actions::CompleteActions::ReadLinkObjectEndAction,
)
Actions::CompleteActions::ReadExtendAction_strategy = st.builds(
    Actions::CompleteActions::ReadExtendAction,
)
Actions::IntermediateActions::StructuralFeatureAction_strategy = st.builds(
    Actions::IntermediateActions::StructuralFeatureAction,
)
Actions::StructuredActions::VariableAction_strategy = st.builds(
    Actions::StructuredActions::VariableAction,
)
Actions::CompleteActions::UnmarshallAction_strategy = st.builds(
    Actions::CompleteActions::UnmarshallAction,
)
Actions::CompleteActions::ReclassifyObjectAction_strategy = st.builds(
    Actions::CompleteActions::ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
Actions::IntermediateActions::ReadSelfAction_strategy = st.builds(
    Actions::IntermediateActions::ReadSelfAction,
)
Actions::CompleteActions::ReplyAction_strategy = st.builds(
    Actions::CompleteActions::ReplyAction,
)
Actions::IntermediateActions::CreateObjectAction_strategy = st.builds(
    Actions::IntermediateActions::CreateObjectAction,
)
Actions::StructuredActions::RaiseExceptionAction_strategy = st.builds(
    Actions::StructuredActions::RaiseExceptionAction,
)
Actions::CompleteActions::ReduceAction_strategy = st.builds(
    Actions::CompleteActions::ReduceAction,
    isOrdered=
        st.booleans()
)
Actions::CompleteActions::StartClassifierBehaviorAction_strategy = st.builds(
    Actions::CompleteActions::StartClassifierBehaviorAction,
)
Actions::BasicActions::OpaqueAction_strategy = st.builds(
    Actions::BasicActions::OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
Actions::BasicActions::Classifier_strategy = st.builds(
    Actions::BasicActions::Classifier,
)
Actions::BasicActions::NamedElement_strategy = st.builds(
    Actions::BasicActions::NamedElement,
)
OutputPin_strategy = st.builds(
    OutputPin,
)
InputPin_strategy = st.builds(
    InputPin,
)
Actions::StructuredActions::ActionInputPin_strategy = st.builds(
    Actions::StructuredActions::ActionInputPin,
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Actions::BasicActions::Action_strategy = st.builds(
    Actions::BasicActions::Action,
)
Actions::BasicActions::InvocationAction_strategy = st.builds(
    Actions::BasicActions::InvocationAction,
)
Actions::BasicActions::ValueSpecification_strategy = st.builds(
    Actions::BasicActions::ValueSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
Actions::BasicActions::ValuePin_strategy = st.builds(
    Actions::BasicActions::ValuePin,
)
Actions::BasicActions::TypedElement_strategy = st.builds(
    Actions::BasicActions::TypedElement,
)
Actions::BasicActions::MultiplicityElement_strategy = st.builds(
    Actions::BasicActions::MultiplicityElement,
)
BasicActions::MultiplicityElement_strategy = st.builds(
    BasicActions::MultiplicityElement,
)
BasicActions::TypedElement_strategy = st.builds(
    BasicActions::TypedElement,
)
Actions::BasicActions::Pin_strategy = st.builds(
    Actions::BasicActions::Pin,
)
Actions::BasicActions::OutputPin_strategy = st.builds(
    Actions::BasicActions::OutputPin,
)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=Actions::StructuredActions::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::readvariableaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::ReadVariableAction)

@given(instance=Actions::StructuredActions::Variable_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::variable_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::Variable)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=Actions::CompleteActions::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::CreateLinkObjectAction)

@given(instance=Actions::StructuredActions::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::clearvariableaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::ClearVariableAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=Actions::StructuredActions::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::RemoveVariableValueAction)

@given(instance=Actions::StructuredActions::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::AddVariableValueAction)

@given(instance=Actions::StructuredActions::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::writevariableaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::WriteVariableAction)

@given(instance=Actions::CompleteActions::ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReadlsClassifiedObjectAction)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=Actions::CompleteActions::Trigger_strategy)
@settings(max_examples=50)
def test_actions::completeactions::trigger_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::Trigger)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=Actions::CompleteActions::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::acceptcallaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::AcceptCallAction)

@given(instance=Actions::IntermediateActions::Property_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::property_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::Property)

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

@given(instance=Actions::CompleteActions::QualifierValue_strategy)
@settings(max_examples=50)
def test_actions::completeactions::qualifiervalue_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::QualifierValue)

@given(instance=Actions::IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::LinkEndData)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=Actions::IntermediateActions::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::LinkEndDestructionData)

@given(instance=Actions::IntermediateActions::LinkEndDestructionData_strategy)
def test_actions::intermediateactions::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, bool)


@given(instance=Actions::IntermediateActions::LinkEndDestructionData_strategy)
def test_actions::intermediateactions::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=Actions::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::RemoveStructuralFeatureValueAction)

@given(instance=Actions::IntermediateActions::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::AddStructuralFeatureValueAction)

@given(instance=Actions::IntermediateActions::Element_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::element_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::Element)

@given(instance=Actions::IntermediateActions::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::LinkEndCreationData)

@given(instance=Actions::IntermediateActions::LinkEndCreationData_strategy)
def test_actions::intermediateactions::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=Actions::IntermediateActions::LinkEndCreationData_strategy)
def test_actions::intermediateactions::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=Actions::IntermediateActions::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::destroylinkaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::DestroyLinkAction)

@given(instance=Actions::IntermediateActions::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::createlinkaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::CreateLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=Actions::IntermediateActions::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::writelinkaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::WriteLinkAction)

@given(instance=Actions::IntermediateActions::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::readlinkaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::ReadLinkAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=Actions::IntermediateActions::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::WriteStructuralFeatureAction)

@given(instance=Actions::IntermediateActions::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::ClearStructuralFeatureAction)

@given(instance=Actions::IntermediateActions::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::ReadStructuralFeatureAction)

@given(instance=Actions::IntermediateActions::StructuralFeature_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::structuralfeature_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::StructuralFeature)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=Actions::BasicActions::Operation_strategy)
@settings(max_examples=50)
def test_actions::basicactions::operation_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Actions::BasicActions::CallOperationAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::calloperationaction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::CallOperationAction)

@given(instance=Actions::BasicActions::Behavior_strategy)
@settings(max_examples=50)
def test_actions::basicactions::behavior_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Behavior)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=Actions::CompleteActions::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::StartObjectBehaviorAction)

@given(instance=Actions::BasicActions::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::callbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::CallBehaviorAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=Actions::BasicActions::SendSignalAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::sendsignalaction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::SendSignalAction)

@given(instance=Actions::BasicActions::CallAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::callaction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::CallAction)

@given(instance=Actions::BasicActions::CallAction_strategy)
def test_actions::basicactions::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, bool)


@given(instance=Actions::BasicActions::CallAction_strategy)
def test_actions::basicactions::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=Actions::IntermediateActions::SendObjectAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::sendobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::SendObjectAction)

@given(instance=Actions::IntermediateActions::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::BroadcastSignalAction)

@given(instance=Actions::BasicActions::Signal_strategy)
@settings(max_examples=50)
def test_actions::basicactions::signal_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Signal)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=Actions::BasicActions::InputPin_strategy)
@settings(max_examples=50)
def test_actions::basicactions::inputpin_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=Actions::IntermediateActions::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::DestroyObjectAction)

@given(instance=Actions::IntermediateActions::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::testidentityaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::TestIdentityAction)

@given(instance=Actions::CompleteActions::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::accepteventaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::AcceptEventAction)

@given(instance=Actions::CompleteActions::AcceptEventAction_strategy)
def test_actions::completeactions::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, bool)


@given(instance=Actions::CompleteActions::AcceptEventAction_strategy)
def test_actions::completeactions::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=Actions::CompleteActions::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReadLinkObjectEndQualifierAction)

@given(instance=Actions::IntermediateActions::LinkAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::linkaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::LinkAction)

@given(instance=Actions::IntermediateActions::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::ValueSpecificationAction)

@given(instance=Actions::CompleteActions::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReadLinkObjectEndAction)

@given(instance=Actions::CompleteActions::ReadExtendAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::readextendaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReadExtendAction)

@given(instance=Actions::IntermediateActions::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::StructuralFeatureAction)

@given(instance=Actions::StructuredActions::VariableAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::variableaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::VariableAction)

@given(instance=Actions::CompleteActions::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::unmarshallaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::UnmarshallAction)

@given(instance=Actions::CompleteActions::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReclassifyObjectAction)

@given(instance=Actions::CompleteActions::ReclassifyObjectAction_strategy)
def test_actions::completeactions::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=Actions::CompleteActions::ReclassifyObjectAction_strategy)
def test_actions::completeactions::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=Actions::IntermediateActions::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::readselfaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::ReadSelfAction)

@given(instance=Actions::CompleteActions::ReplyAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::replyaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReplyAction)

@given(instance=Actions::IntermediateActions::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_actions::intermediateactions::createobjectaction_instantiation(instance):
    assert isinstance(instance, Actions::IntermediateActions::CreateObjectAction)

@given(instance=Actions::StructuredActions::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::RaiseExceptionAction)

@given(instance=Actions::CompleteActions::ReduceAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::reduceaction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::ReduceAction)

@given(instance=Actions::CompleteActions::ReduceAction_strategy)
def test_actions::completeactions::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=Actions::CompleteActions::ReduceAction_strategy)
def test_actions::completeactions::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Actions::CompleteActions::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_actions::completeactions::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, Actions::CompleteActions::StartClassifierBehaviorAction)

@given(instance=Actions::BasicActions::OpaqueAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::opaqueaction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::OpaqueAction)

@given(instance=Actions::BasicActions::OpaqueAction_strategy)
def test_actions::basicactions::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=Actions::BasicActions::OpaqueAction_strategy)
def test_actions::basicactions::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Actions::BasicActions::OpaqueAction_strategy)
def test_actions::basicactions::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=Actions::BasicActions::OpaqueAction_strategy)
def test_actions::basicactions::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Actions::BasicActions::Classifier_strategy)
@settings(max_examples=50)
def test_actions::basicactions::classifier_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Classifier)

@given(instance=Actions::BasicActions::NamedElement_strategy)
@settings(max_examples=50)
def test_actions::basicactions::namedelement_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::NamedElement)

@given(instance=OutputPin_strategy)
@settings(max_examples=50)
def test_outputpin_instantiation(instance):
    assert isinstance(instance, OutputPin)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=Actions::StructuredActions::ActionInputPin_strategy)
@settings(max_examples=50)
def test_actions::structuredactions::actioninputpin_instantiation(instance):
    assert isinstance(instance, Actions::StructuredActions::ActionInputPin)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Actions::BasicActions::Action_strategy)
@settings(max_examples=50)
def test_actions::basicactions::action_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Action)

@given(instance=Actions::BasicActions::InvocationAction_strategy)
@settings(max_examples=50)
def test_actions::basicactions::invocationaction_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::InvocationAction)

@given(instance=Actions::BasicActions::ValueSpecification_strategy)
@settings(max_examples=50)
def test_actions::basicactions::valuespecification_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::ValueSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=Actions::BasicActions::ValuePin_strategy)
@settings(max_examples=50)
def test_actions::basicactions::valuepin_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::ValuePin)

@given(instance=Actions::BasicActions::TypedElement_strategy)
@settings(max_examples=50)
def test_actions::basicactions::typedelement_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::TypedElement)

@given(instance=Actions::BasicActions::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_actions::basicactions::multiplicityelement_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::MultiplicityElement)

@given(instance=BasicActions::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_basicactions::multiplicityelement_instantiation(instance):
    assert isinstance(instance, BasicActions::MultiplicityElement)

@given(instance=BasicActions::TypedElement_strategy)
@settings(max_examples=50)
def test_basicactions::typedelement_instantiation(instance):
    assert isinstance(instance, BasicActions::TypedElement)

@given(instance=Actions::BasicActions::Pin_strategy)
@settings(max_examples=50)
def test_actions::basicactions::pin_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::Pin)

@given(instance=Actions::BasicActions::OutputPin_strategy)
@settings(max_examples=50)
def test_actions::basicactions::outputpin_instantiation(instance):
    assert isinstance(instance, Actions::BasicActions::OutputPin)
