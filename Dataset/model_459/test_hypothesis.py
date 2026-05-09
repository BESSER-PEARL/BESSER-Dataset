import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EncapsulatedClassifier,
    CreateLinkAction,
    UML2::CreateLinkObjectAction,
    AcceptEventAction,
    UML2::AcceptCallAction,
    Association,
    UML2::Extension,
    UML2::CommunicationPath,
    LinkAction,
    UML2::WriteLinkAction,
    UML2::ReadLinkAction,
    StructuralFeatureAction,
    UML2::ClearStructuralFeatureAction,
    UML2::ReadStructuralFeatureAction,
    UML2::WriteStructuralFeatureAction,
    StateMachine,
    UML2::ProtocolStateMachine,
    BehavioredClassifier,
    UML2::Class,
    UML2::UseCase,
    VariableAction,
    UML2::WriteVariableAction,
    UML2::ReadVariableAction,
    UML2::ClearVariableAction,
    Behavior,
    UML2::StateMachine,
    UML2::Interaction,
    WriteStructuralFeatureAction,
    UML2::AddStructuralFeatureValueAction,
    UML2::TimeObservationAction,
    UML2::DurationObservationAction,
    UML2::RemoveStructuralFeatureValueAction,
    WriteLinkAction,
    UML2::DestroyLinkAction,
    UML2::CreateLinkAction,
    UML2::Activity,
    Artifact,
    UML2::DeploymentSpecification,
    WriteVariableAction,
    UML2::AddVariableValueAction,
    UML2::RemoveVariableValueAction,
    UML2::Classifier,
    UML2::Action,
    StructuredClassifier,
    UML2::Collaboration,
    UML2::EncapsulatedClassifier,
    InvocationAction,
    UML2::CallAction,
    UML2::SendSignalAction,
    UML2::SendObjectAction,
    UML2::BroadcastSignalAction,
    StructuredActivityNode,
    UML2::ExpansionRegion,
    UML2::ConditionalNode,
    UML2::LoopNode,
    Node,
    UML2::ExecutionEnvironment,
    UML2::Device,
    CallAction,
    UML2::CallOperationAction,
    UML2::CallBehaviorAction,
    Class,
    UML2::Component,
    UML2::Behavior,
    UML2::AssociationClass,
    UML2::Stereotype,
    UML2::Node,
    DataType,
    UML2::PrimitiveType,
    UML2::Enumeration,
    Classifier,
    UML2::Actor,
    UML2::BehavioredClassifier,
    UML2::ParameterableClassifier,
    UML2::StructuredClassifier,
    UML2::DataType,
    UML2::Signal,
    UML2::InformationItem,
    UML2::TemplateableClassifier,
    UML2::Artifact,
    UML2::Interface,
    UML2::Association,
    Action,
    UML2::InvocationAction,
    UML2::ClearAssociationAction,
    UML2::ReadLinkObjectEndAction,
    UML2::CreateObjectAction,
    UML2::ReadExtentAction,
    UML2::ReclassifyObjectAction,
    UML2::StructuredActivityNode,
    UML2::DestroyObjectAction,
    UML2::ReadSelfAction,
    UML2::ReplyAction,
    UML2::ApplyFunctionAction,
    UML2::RaiseExceptionAction,
    UML2::VariableAction,
    UML2::TestIdentityAction,
    UML2::AcceptEventAction,
    UML2::ReadLinkObjectEndQualifierAction,
    UML2::StructuralFeatureAction,
    UML2::StartOwnedBehaviorAction,
    UML2::LinkAction,
    UML2::ReadIsClassifiedObjectAction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateLinkObjectAction)


def test_uml2::createlinkobjectaction_constructor_exists():
    assert callable(UML2::CreateLinkObjectAction.__init__)


def test_uml2::createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptCallAction)


def test_uml2::acceptcallaction_constructor_exists():
    assert callable(UML2::AcceptCallAction.__init__)


def test_uml2::acceptcallaction_constructor_args():
    sig = inspect.signature(UML2::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extension_is_not_abstract():
    assert not inspect.isabstract(UML2::Extension)


def test_uml2::extension_constructor_exists():
    assert callable(UML2::Extension.__init__)


def test_uml2::extension_constructor_args():
    sig = inspect.signature(UML2::Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2::CommunicationPath)


def test_uml2::communicationpath_constructor_exists():
    assert callable(UML2::CommunicationPath.__init__)


def test_uml2::communicationpath_constructor_args():
    sig = inspect.signature(UML2::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteLinkAction)


def test_uml2::writelinkaction_constructor_exists():
    assert callable(UML2::WriteLinkAction.__init__)


def test_uml2::writelinkaction_constructor_args():
    sig = inspect.signature(UML2::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkAction)


def test_uml2::readlinkaction_constructor_exists():
    assert callable(UML2::ReadLinkAction.__init__)


def test_uml2::readlinkaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearStructuralFeatureAction)


def test_uml2::clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ClearStructuralFeatureAction.__init__)


def test_uml2::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadStructuralFeatureAction)


def test_uml2::readstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ReadStructuralFeatureAction.__init__)


def test_uml2::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteStructuralFeatureAction)


def test_uml2::writestructuralfeatureaction_constructor_exists():
    assert callable(UML2::WriteStructuralFeatureAction.__init__)


def test_uml2::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::ProtocolStateMachine)


def test_uml2::protocolstatemachine_constructor_exists():
    assert callable(UML2::ProtocolStateMachine.__init__)


def test_uml2::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::class_is_not_abstract():
    assert not inspect.isabstract(UML2::Class)


def test_uml2::class_constructor_exists():
    assert callable(UML2::Class.__init__)


def test_uml2::class_constructor_args():
    sig = inspect.signature(UML2::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2::UseCase)


def test_uml2::usecase_constructor_exists():
    assert callable(UML2::UseCase.__init__)


def test_uml2::usecase_constructor_args():
    sig = inspect.signature(UML2::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteVariableAction)


def test_uml2::writevariableaction_constructor_exists():
    assert callable(UML2::WriteVariableAction.__init__)


def test_uml2::writevariableaction_constructor_args():
    sig = inspect.signature(UML2::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadVariableAction)


def test_uml2::readvariableaction_constructor_exists():
    assert callable(UML2::ReadVariableAction.__init__)


def test_uml2::readvariableaction_constructor_args():
    sig = inspect.signature(UML2::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearVariableAction)


def test_uml2::clearvariableaction_constructor_exists():
    assert callable(UML2::ClearVariableAction.__init__)


def test_uml2::clearvariableaction_constructor_args():
    sig = inspect.signature(UML2::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::StateMachine)


def test_uml2::statemachine_constructor_exists():
    assert callable(UML2::StateMachine.__init__)


def test_uml2::statemachine_constructor_args():
    sig = inspect.signature(UML2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2::Interaction)


def test_uml2::interaction_constructor_exists():
    assert callable(UML2::Interaction.__init__)


def test_uml2::interaction_constructor_args():
    sig = inspect.signature(UML2::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddStructuralFeatureValueAction)


def test_uml2::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::AddStructuralFeatureValueAction.__init__)


def test_uml2::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeObservationAction)


def test_uml2::timeobservationaction_constructor_exists():
    assert callable(UML2::TimeObservationAction.__init__)


def test_uml2::timeobservationaction_constructor_args():
    sig = inspect.signature(UML2::TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationObservationAction)


def test_uml2::durationobservationaction_constructor_exists():
    assert callable(UML2::DurationObservationAction.__init__)


def test_uml2::durationobservationaction_constructor_args():
    sig = inspect.signature(UML2::DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveStructuralFeatureValueAction)


def test_uml2::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::RemoveStructuralFeatureValueAction.__init__)


def test_uml2::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DestroyLinkAction)


def test_uml2::destroylinkaction_constructor_exists():
    assert callable(UML2::DestroyLinkAction.__init__)


def test_uml2::destroylinkaction_constructor_args():
    sig = inspect.signature(UML2::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateLinkAction)


def test_uml2::createlinkaction_constructor_exists():
    assert callable(UML2::CreateLinkAction.__init__)


def test_uml2::createlinkaction_constructor_args():
    sig = inspect.signature(UML2::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::DeploymentSpecification)


def test_uml2::deploymentspecification_constructor_exists():
    assert callable(UML2::DeploymentSpecification.__init__)


def test_uml2::deploymentspecification_constructor_args():
    sig = inspect.signature(UML2::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddVariableValueAction)


def test_uml2::addvariablevalueaction_constructor_exists():
    assert callable(UML2::AddVariableValueAction.__init__)


def test_uml2::addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveVariableValueAction)


def test_uml2::removevariablevalueaction_constructor_exists():
    assert callable(UML2::RemoveVariableValueAction.__init__)


def test_uml2::removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2::Classifier)


def test_uml2::classifier_constructor_exists():
    assert callable(UML2::Classifier.__init__)


def test_uml2::classifier_constructor_args():
    sig = inspect.signature(UML2::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::action_is_not_abstract():
    assert not inspect.isabstract(UML2::Action)


def test_uml2::action_constructor_exists():
    assert callable(UML2::Action.__init__)


def test_uml2::action_constructor_args():
    sig = inspect.signature(UML2::Action.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2::Collaboration)


def test_uml2::collaboration_constructor_exists():
    assert callable(UML2::Collaboration.__init__)


def test_uml2::collaboration_constructor_args():
    sig = inspect.signature(UML2::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::EncapsulatedClassifier)


def test_uml2::encapsulatedclassifier_constructor_exists():
    assert callable(UML2::EncapsulatedClassifier.__init__)


def test_uml2::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::callaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallAction)


def test_uml2::callaction_constructor_exists():
    assert callable(UML2::CallAction.__init__)


def test_uml2::callaction_constructor_args():
    sig = inspect.signature(UML2::CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendSignalAction)


def test_uml2::sendsignalaction_constructor_exists():
    assert callable(UML2::SendSignalAction.__init__)


def test_uml2::sendsignalaction_constructor_args():
    sig = inspect.signature(UML2::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendObjectAction)


def test_uml2::sendobjectaction_constructor_exists():
    assert callable(UML2::SendObjectAction.__init__)


def test_uml2::sendobjectaction_constructor_args():
    sig = inspect.signature(UML2::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::BroadcastSignalAction)


def test_uml2::broadcastsignalaction_constructor_exists():
    assert callable(UML2::BroadcastSignalAction.__init__)


def test_uml2::broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2::ExpansionRegion)


def test_uml2::expansionregion_constructor_exists():
    assert callable(UML2::ExpansionRegion.__init__)


def test_uml2::expansionregion_constructor_args():
    sig = inspect.signature(UML2::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ConditionalNode)


def test_uml2::conditionalnode_constructor_exists():
    assert callable(UML2::ConditionalNode.__init__)


def test_uml2::conditionalnode_constructor_args():
    sig = inspect.signature(UML2::ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2::LoopNode)


def test_uml2::loopnode_constructor_exists():
    assert callable(UML2::LoopNode.__init__)


def test_uml2::loopnode_constructor_args():
    sig = inspect.signature(UML2::LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionEnvironment)


def test_uml2::executionenvironment_constructor_exists():
    assert callable(UML2::ExecutionEnvironment.__init__)


def test_uml2::executionenvironment_constructor_args():
    sig = inspect.signature(UML2::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::device_is_not_abstract():
    assert not inspect.isabstract(UML2::Device)


def test_uml2::device_constructor_exists():
    assert callable(UML2::Device.__init__)


def test_uml2::device_constructor_args():
    sig = inspect.signature(UML2::Device.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallOperationAction)


def test_uml2::calloperationaction_constructor_exists():
    assert callable(UML2::CallOperationAction.__init__)


def test_uml2::calloperationaction_constructor_args():
    sig = inspect.signature(UML2::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallBehaviorAction)


def test_uml2::callbehavioraction_constructor_exists():
    assert callable(UML2::CallBehaviorAction.__init__)


def test_uml2::callbehavioraction_constructor_args():
    sig = inspect.signature(UML2::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::component_is_not_abstract():
    assert not inspect.isabstract(UML2::Component)


def test_uml2::component_constructor_exists():
    assert callable(UML2::Component.__init__)


def test_uml2::component_constructor_args():
    sig = inspect.signature(UML2::Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2::PrimitiveType)


def test_uml2::primitivetype_constructor_exists():
    assert callable(UML2::PrimitiveType.__init__)


def test_uml2::primitivetype_constructor_args():
    sig = inspect.signature(UML2::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2::Enumeration)


def test_uml2::enumeration_constructor_exists():
    assert callable(UML2::Enumeration.__init__)


def test_uml2::enumeration_constructor_args():
    sig = inspect.signature(UML2::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::actor_is_not_abstract():
    assert not inspect.isabstract(UML2::Actor)


def test_uml2::actor_constructor_exists():
    assert callable(UML2::Actor.__init__)


def test_uml2::actor_constructor_args():
    sig = inspect.signature(UML2::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioredClassifier)


def test_uml2::behavioredclassifier_constructor_exists():
    assert callable(UML2::BehavioredClassifier.__init__)


def test_uml2::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterableClassifier)


def test_uml2::parameterableclassifier_constructor_exists():
    assert callable(UML2::ParameterableClassifier.__init__)


def test_uml2::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredClassifier)


def test_uml2::structuredclassifier_constructor_exists():
    assert callable(UML2::StructuredClassifier.__init__)


def test_uml2::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2::DataType)


def test_uml2::datatype_constructor_exists():
    assert callable(UML2::DataType.__init__)


def test_uml2::datatype_constructor_args():
    sig = inspect.signature(UML2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signal_is_not_abstract():
    assert not inspect.isabstract(UML2::Signal)


def test_uml2::signal_constructor_exists():
    assert callable(UML2::Signal.__init__)


def test_uml2::signal_constructor_args():
    sig = inspect.signature(UML2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationItem)


def test_uml2::informationitem_constructor_exists():
    assert callable(UML2::InformationItem.__init__)


def test_uml2::informationitem_constructor_args():
    sig = inspect.signature(UML2::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableClassifier)


def test_uml2::templateableclassifier_constructor_exists():
    assert callable(UML2::TemplateableClassifier.__init__)


def test_uml2::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2::Artifact)


def test_uml2::artifact_constructor_exists():
    assert callable(UML2::Artifact.__init__)


def test_uml2::artifact_constructor_args():
    sig = inspect.signature(UML2::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interface_is_not_abstract():
    assert not inspect.isabstract(UML2::Interface)


def test_uml2::interface_constructor_exists():
    assert callable(UML2::Interface.__init__)


def test_uml2::interface_constructor_args():
    sig = inspect.signature(UML2::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2::association_is_not_abstract():
    assert not inspect.isabstract(UML2::Association)


def test_uml2::association_constructor_exists():
    assert callable(UML2::Association.__init__)


def test_uml2::association_constructor_args():
    sig = inspect.signature(UML2::Association.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2::invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::InvocationAction)


def test_uml2::invocationaction_constructor_exists():
    assert callable(UML2::InvocationAction.__init__)


def test_uml2::invocationaction_constructor_args():
    sig = inspect.signature(UML2::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearAssociationAction)


def test_uml2::clearassociationaction_constructor_exists():
    assert callable(UML2::ClearAssociationAction.__init__)


def test_uml2::clearassociationaction_constructor_args():
    sig = inspect.signature(UML2::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndAction)


def test_uml2::readlinkobjectendaction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndAction.__init__)


def test_uml2::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateObjectAction)


def test_uml2::createobjectaction_constructor_exists():
    assert callable(UML2::CreateObjectAction.__init__)


def test_uml2::createobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadExtentAction)


def test_uml2::readextentaction_constructor_exists():
    assert callable(UML2::ReadExtentAction.__init__)


def test_uml2::readextentaction_constructor_args():
    sig = inspect.signature(UML2::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReclassifyObjectAction)


def test_uml2::reclassifyobjectaction_constructor_exists():
    assert callable(UML2::ReclassifyObjectAction.__init__)


def test_uml2::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredActivityNode)


def test_uml2::structuredactivitynode_constructor_exists():
    assert callable(UML2::StructuredActivityNode.__init__)


def test_uml2::structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DestroyObjectAction)


def test_uml2::destroyobjectaction_constructor_exists():
    assert callable(UML2::DestroyObjectAction.__init__)


def test_uml2::destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadSelfAction)


def test_uml2::readselfaction_constructor_exists():
    assert callable(UML2::ReadSelfAction.__init__)


def test_uml2::readselfaction_constructor_args():
    sig = inspect.signature(UML2::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReplyAction)


def test_uml2::replyaction_constructor_exists():
    assert callable(UML2::ReplyAction.__init__)


def test_uml2::replyaction_constructor_args():
    sig = inspect.signature(UML2::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ApplyFunctionAction)


def test_uml2::applyfunctionaction_constructor_exists():
    assert callable(UML2::ApplyFunctionAction.__init__)


def test_uml2::applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2::ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RaiseExceptionAction)


def test_uml2::raiseexceptionaction_constructor_exists():
    assert callable(UML2::RaiseExceptionAction.__init__)


def test_uml2::raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::VariableAction)


def test_uml2::variableaction_constructor_exists():
    assert callable(UML2::VariableAction.__init__)


def test_uml2::variableaction_constructor_args():
    sig = inspect.signature(UML2::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TestIdentityAction)


def test_uml2::testidentityaction_constructor_exists():
    assert callable(UML2::TestIdentityAction.__init__)


def test_uml2::testidentityaction_constructor_args():
    sig = inspect.signature(UML2::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptEventAction)


def test_uml2::accepteventaction_constructor_exists():
    assert callable(UML2::AcceptEventAction.__init__)


def test_uml2::accepteventaction_constructor_args():
    sig = inspect.signature(UML2::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndQualifierAction)


def test_uml2::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndQualifierAction.__init__)


def test_uml2::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeatureAction)


def test_uml2::structuralfeatureaction_constructor_exists():
    assert callable(UML2::StructuralFeatureAction.__init__)


def test_uml2::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::StartOwnedBehaviorAction)


def test_uml2::startownedbehavioraction_constructor_exists():
    assert callable(UML2::StartOwnedBehaviorAction.__init__)


def test_uml2::startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2::StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkAction)


def test_uml2::linkaction_constructor_exists():
    assert callable(UML2::LinkAction.__init__)


def test_uml2::linkaction_constructor_args():
    sig = inspect.signature(UML2::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadIsClassifiedObjectAction)


def test_uml2::readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2::ReadIsClassifiedObjectAction.__init__)


def test_uml2::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReadIsClassifiedObjectAction.__init__)
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
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UML2::CreateLinkObjectAction_strategy = st.builds(
    UML2::CreateLinkObjectAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UML2::AcceptCallAction_strategy = st.builds(
    UML2::AcceptCallAction,
)
Association_strategy = st.builds(
    Association,
)
UML2::Extension_strategy = st.builds(
    UML2::Extension,
)
UML2::CommunicationPath_strategy = st.builds(
    UML2::CommunicationPath,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2::WriteLinkAction_strategy = st.builds(
    UML2::WriteLinkAction,
)
UML2::ReadLinkAction_strategy = st.builds(
    UML2::ReadLinkAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2::ClearStructuralFeatureAction_strategy = st.builds(
    UML2::ClearStructuralFeatureAction,
)
UML2::ReadStructuralFeatureAction_strategy = st.builds(
    UML2::ReadStructuralFeatureAction,
)
UML2::WriteStructuralFeatureAction_strategy = st.builds(
    UML2::WriteStructuralFeatureAction,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2::Class_strategy = st.builds(
    UML2::Class,
)
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UML2::WriteVariableAction_strategy = st.builds(
    UML2::WriteVariableAction,
)
UML2::ReadVariableAction_strategy = st.builds(
    UML2::ReadVariableAction,
)
UML2::ClearVariableAction_strategy = st.builds(
    UML2::ClearVariableAction,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2::StateMachine_strategy = st.builds(
    UML2::StateMachine,
)
UML2::Interaction_strategy = st.builds(
    UML2::Interaction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2::AddStructuralFeatureValueAction_strategy = st.builds(
    UML2::AddStructuralFeatureValueAction,
)
UML2::TimeObservationAction_strategy = st.builds(
    UML2::TimeObservationAction,
)
UML2::DurationObservationAction_strategy = st.builds(
    UML2::DurationObservationAction,
)
UML2::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2::RemoveStructuralFeatureValueAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UML2::DestroyLinkAction_strategy = st.builds(
    UML2::DestroyLinkAction,
)
UML2::CreateLinkAction_strategy = st.builds(
    UML2::CreateLinkAction,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2::DeploymentSpecification_strategy = st.builds(
    UML2::DeploymentSpecification,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2::AddVariableValueAction_strategy = st.builds(
    UML2::AddVariableValueAction,
)
UML2::RemoveVariableValueAction_strategy = st.builds(
    UML2::RemoveVariableValueAction,
)
UML2::Classifier_strategy = st.builds(
    UML2::Classifier,
)
UML2::Action_strategy = st.builds(
    UML2::Action,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2::Collaboration_strategy = st.builds(
    UML2::Collaboration,
)
UML2::EncapsulatedClassifier_strategy = st.builds(
    UML2::EncapsulatedClassifier,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UML2::CallAction_strategy = st.builds(
    UML2::CallAction,
)
UML2::SendSignalAction_strategy = st.builds(
    UML2::SendSignalAction,
)
UML2::SendObjectAction_strategy = st.builds(
    UML2::SendObjectAction,
)
UML2::BroadcastSignalAction_strategy = st.builds(
    UML2::BroadcastSignalAction,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UML2::ExpansionRegion_strategy = st.builds(
    UML2::ExpansionRegion,
)
UML2::ConditionalNode_strategy = st.builds(
    UML2::ConditionalNode,
)
UML2::LoopNode_strategy = st.builds(
    UML2::LoopNode,
)
Node_strategy = st.builds(
    Node,
)
UML2::ExecutionEnvironment_strategy = st.builds(
    UML2::ExecutionEnvironment,
)
UML2::Device_strategy = st.builds(
    UML2::Device,
)
CallAction_strategy = st.builds(
    CallAction,
)
UML2::CallOperationAction_strategy = st.builds(
    UML2::CallOperationAction,
)
UML2::CallBehaviorAction_strategy = st.builds(
    UML2::CallBehaviorAction,
)
Class_strategy = st.builds(
    Class,
)
UML2::Component_strategy = st.builds(
    UML2::Component,
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
UML2::Node_strategy = st.builds(
    UML2::Node,
)
DataType_strategy = st.builds(
    DataType,
)
UML2::PrimitiveType_strategy = st.builds(
    UML2::PrimitiveType,
)
UML2::Enumeration_strategy = st.builds(
    UML2::Enumeration,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2::Actor_strategy = st.builds(
    UML2::Actor,
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::ParameterableClassifier_strategy = st.builds(
    UML2::ParameterableClassifier,
)
UML2::StructuredClassifier_strategy = st.builds(
    UML2::StructuredClassifier,
)
UML2::DataType_strategy = st.builds(
    UML2::DataType,
)
UML2::Signal_strategy = st.builds(
    UML2::Signal,
)
UML2::InformationItem_strategy = st.builds(
    UML2::InformationItem,
)
UML2::TemplateableClassifier_strategy = st.builds(
    UML2::TemplateableClassifier,
)
UML2::Artifact_strategy = st.builds(
    UML2::Artifact,
)
UML2::Interface_strategy = st.builds(
    UML2::Interface,
)
UML2::Association_strategy = st.builds(
    UML2::Association,
)
Action_strategy = st.builds(
    Action,
)
UML2::InvocationAction_strategy = st.builds(
    UML2::InvocationAction,
)
UML2::ClearAssociationAction_strategy = st.builds(
    UML2::ClearAssociationAction,
)
UML2::ReadLinkObjectEndAction_strategy = st.builds(
    UML2::ReadLinkObjectEndAction,
)
UML2::CreateObjectAction_strategy = st.builds(
    UML2::CreateObjectAction,
)
UML2::ReadExtentAction_strategy = st.builds(
    UML2::ReadExtentAction,
)
UML2::ReclassifyObjectAction_strategy = st.builds(
    UML2::ReclassifyObjectAction,
)
UML2::StructuredActivityNode_strategy = st.builds(
    UML2::StructuredActivityNode,
)
UML2::DestroyObjectAction_strategy = st.builds(
    UML2::DestroyObjectAction,
)
UML2::ReadSelfAction_strategy = st.builds(
    UML2::ReadSelfAction,
)
UML2::ReplyAction_strategy = st.builds(
    UML2::ReplyAction,
)
UML2::ApplyFunctionAction_strategy = st.builds(
    UML2::ApplyFunctionAction,
)
UML2::RaiseExceptionAction_strategy = st.builds(
    UML2::RaiseExceptionAction,
)
UML2::VariableAction_strategy = st.builds(
    UML2::VariableAction,
)
UML2::TestIdentityAction_strategy = st.builds(
    UML2::TestIdentityAction,
)
UML2::AcceptEventAction_strategy = st.builds(
    UML2::AcceptEventAction,
)
UML2::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2::ReadLinkObjectEndQualifierAction,
)
UML2::StructuralFeatureAction_strategy = st.builds(
    UML2::StructuralFeatureAction,
)
UML2::StartOwnedBehaviorAction_strategy = st.builds(
    UML2::StartOwnedBehaviorAction,
)
UML2::LinkAction_strategy = st.builds(
    UML2::LinkAction,
)
UML2::ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2::ReadIsClassifiedObjectAction,
)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UML2::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateLinkObjectAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UML2::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2::acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptCallAction)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2::Extension_strategy)
@settings(max_examples=50)
def test_uml2::extension_instantiation(instance):
    assert isinstance(instance, UML2::Extension)

@given(instance=UML2::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2::CommunicationPath)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteLinkAction)

@given(instance=UML2::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearStructuralFeatureAction)

@given(instance=UML2::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadStructuralFeatureAction)

@given(instance=UML2::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteStructuralFeatureAction)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2::Class_strategy)
@settings(max_examples=50)
def test_uml2::class_instantiation(instance):
    assert isinstance(instance, UML2::Class)

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UML2::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteVariableAction)

@given(instance=UML2::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadVariableAction)

@given(instance=UML2::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearVariableAction)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2::statemachine_instantiation(instance):
    assert isinstance(instance, UML2::StateMachine)

@given(instance=UML2::Interaction_strategy)
@settings(max_examples=50)
def test_uml2::interaction_instantiation(instance):
    assert isinstance(instance, UML2::Interaction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddStructuralFeatureValueAction)

@given(instance=UML2::TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::TimeObservationAction)

@given(instance=UML2::DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::DurationObservationAction)

@given(instance=UML2::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveStructuralFeatureValueAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UML2::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2::DestroyLinkAction)

@given(instance=UML2::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateLinkAction)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentSpecification)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddVariableValueAction)

@given(instance=UML2::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveVariableValueAction)

@given(instance=UML2::Classifier_strategy)
@settings(max_examples=50)
def test_uml2::classifier_instantiation(instance):
    assert isinstance(instance, UML2::Classifier)

@given(instance=UML2::Action_strategy)
@settings(max_examples=50)
def test_uml2::action_instantiation(instance):
    assert isinstance(instance, UML2::Action)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2::collaboration_instantiation(instance):
    assert isinstance(instance, UML2::Collaboration)

@given(instance=UML2::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2::EncapsulatedClassifier)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UML2::CallAction_strategy)
@settings(max_examples=50)
def test_uml2::callaction_instantiation(instance):
    assert isinstance(instance, UML2::CallAction)

@given(instance=UML2::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::SendSignalAction)

@given(instance=UML2::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::SendObjectAction)

@given(instance=UML2::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::BroadcastSignalAction)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UML2::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2::expansionregion_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionRegion)

@given(instance=UML2::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2::conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2::ConditionalNode)

@given(instance=UML2::LoopNode_strategy)
@settings(max_examples=50)
def test_uml2::loopnode_instantiation(instance):
    assert isinstance(instance, UML2::LoopNode)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionEnvironment)

@given(instance=UML2::Device_strategy)
@settings(max_examples=50)
def test_uml2::device_instantiation(instance):
    assert isinstance(instance, UML2::Device)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UML2::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2::calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2::CallOperationAction)

@given(instance=UML2::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::CallBehaviorAction)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2::Component_strategy)
@settings(max_examples=50)
def test_uml2::component_instantiation(instance):
    assert isinstance(instance, UML2::Component)

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2::primitivetype_instantiation(instance):
    assert isinstance(instance, UML2::PrimitiveType)

@given(instance=UML2::Enumeration_strategy)
@settings(max_examples=50)
def test_uml2::enumeration_instantiation(instance):
    assert isinstance(instance, UML2::Enumeration)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2::Actor_strategy)
@settings(max_examples=50)
def test_uml2::actor_instantiation(instance):
    assert isinstance(instance, UML2::Actor)

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableClassifier)

@given(instance=UML2::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::StructuredClassifier)

@given(instance=UML2::DataType_strategy)
@settings(max_examples=50)
def test_uml2::datatype_instantiation(instance):
    assert isinstance(instance, UML2::DataType)

@given(instance=UML2::Signal_strategy)
@settings(max_examples=50)
def test_uml2::signal_instantiation(instance):
    assert isinstance(instance, UML2::Signal)

@given(instance=UML2::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2::informationitem_instantiation(instance):
    assert isinstance(instance, UML2::InformationItem)

@given(instance=UML2::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableClassifier)

@given(instance=UML2::Artifact_strategy)
@settings(max_examples=50)
def test_uml2::artifact_instantiation(instance):
    assert isinstance(instance, UML2::Artifact)

@given(instance=UML2::Interface_strategy)
@settings(max_examples=50)
def test_uml2::interface_instantiation(instance):
    assert isinstance(instance, UML2::Interface)

@given(instance=UML2::Association_strategy)
@settings(max_examples=50)
def test_uml2::association_instantiation(instance):
    assert isinstance(instance, UML2::Association)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2::invocationaction_instantiation(instance):
    assert isinstance(instance, UML2::InvocationAction)

@given(instance=UML2::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2::clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearAssociationAction)

@given(instance=UML2::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndAction)

@given(instance=UML2::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateObjectAction)

@given(instance=UML2::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2::readextentaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadExtentAction)

@given(instance=UML2::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReclassifyObjectAction)

@given(instance=UML2::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2::StructuredActivityNode)

@given(instance=UML2::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::DestroyObjectAction)

@given(instance=UML2::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2::readselfaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadSelfAction)

@given(instance=UML2::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2::replyaction_instantiation(instance):
    assert isinstance(instance, UML2::ReplyAction)

@given(instance=UML2::ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2::applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2::ApplyFunctionAction)

@given(instance=UML2::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2::RaiseExceptionAction)

@given(instance=UML2::VariableAction_strategy)
@settings(max_examples=50)
def test_uml2::variableaction_instantiation(instance):
    assert isinstance(instance, UML2::VariableAction)

@given(instance=UML2::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2::testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2::TestIdentityAction)

@given(instance=UML2::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2::accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptEventAction)

@given(instance=UML2::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndQualifierAction)

@given(instance=UML2::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeatureAction)

@given(instance=UML2::StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::StartOwnedBehaviorAction)

@given(instance=UML2::LinkAction_strategy)
@settings(max_examples=50)
def test_uml2::linkaction_instantiation(instance):
    assert isinstance(instance, UML2::LinkAction)

@given(instance=UML2::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadIsClassifiedObjectAction)
