import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuralFeature,
    UML2::Property,
    BehavioralFeature,
    UML2::Operation,
    UML2::Reception,
    WriteStructuralFeatureAction,
    UML2::RemoveStructuralFeatureValueAction,
    UML2::AddStructuralFeatureValueAction,
    UML2::DurationObservationAction,
    UML2::TimeObservationAction,
    DataType,
    UML2::PrimitiveType,
    UML2::Enumeration,
    Association,
    UML2::Extension,
    UML2::CommunicationPath,
    StructuredClassifier,
    EncapsulatedClassifier,
    BehavioredClassifier,
    UML2::Collaboration,
    UML2::Class,
    StateMachine,
    UML2::ProtocolStateMachine,
    UML2::StructuralFeatureAction,
    Feature,
    UML2::BehavioralFeature,
    UML2::Connector,
    UML2::StructuralFeature,
    UML2::Classifier,
    UML2::Feature,
    Behavior,
    UML2::Activity,
    UML2::StateMachine,
    UML2::Interaction,
    Class,
    UML2::AssociationClass,
    UML2::Behavior,
    UML2::Stereotype,
    UML2::Component,
    UML2::Node,
    Property,
    UML2::Port,
    UML2::ExtensionEnd,
    Classifier,
    UML2::Interface,
    UML2::InformationItem,
    UML2::Artifact,
    UML2::Signal,
    UML2::Association,
    UML2::StructuredClassifier,
    UML2::ParameterableClassifier,
    UML2::Actor,
    Node,
    UML2::Device,
    StructuralFeatureAction,
    UML2::ClearStructuralFeatureAction,
    UML2::WriteStructuralFeatureAction,
    UML2::ReadStructuralFeatureAction,
    UML2::EncapsulatedClassifier,
    Artifact,
    UML2::DeploymentSpecification,
    UML2::DataType,
    UML2::BehavioredClassifier,
    UML2::ExecutionEnvironment,
    UML2::TemplateableClassifier,
    UML2::UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveStructuralFeatureValueAction)


def test_uml2::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::RemoveStructuralFeatureValueAction.__init__)


def test_uml2::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddStructuralFeatureValueAction)


def test_uml2::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::AddStructuralFeatureValueAction.__init__)


def test_uml2::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationObservationAction)


def test_uml2::durationobservationaction_constructor_exists():
    assert callable(UML2::DurationObservationAction.__init__)


def test_uml2::durationobservationaction_constructor_args():
    sig = inspect.signature(UML2::DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeObservationAction)


def test_uml2::timeobservationaction_constructor_exists():
    assert callable(UML2::TimeObservationAction.__init__)


def test_uml2::timeobservationaction_constructor_args():
    sig = inspect.signature(UML2::TimeObservationAction.__init__)
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



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
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



def test_uml2::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2::Collaboration)


def test_uml2::collaboration_constructor_exists():
    assert callable(UML2::Collaboration.__init__)


def test_uml2::collaboration_constructor_args():
    sig = inspect.signature(UML2::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::class_is_not_abstract():
    assert not inspect.isabstract(UML2::Class)


def test_uml2::class_constructor_exists():
    assert callable(UML2::Class.__init__)


def test_uml2::class_constructor_args():
    sig = inspect.signature(UML2::Class.__init__)
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



def test_uml2::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeatureAction)


def test_uml2::structuralfeatureaction_constructor_exists():
    assert callable(UML2::StructuralFeatureAction.__init__)


def test_uml2::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioralFeature)


def test_uml2::behavioralfeature_constructor_exists():
    assert callable(UML2::BehavioralFeature.__init__)


def test_uml2::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connector_is_not_abstract():
    assert not inspect.isabstract(UML2::Connector)


def test_uml2::connector_constructor_exists():
    assert callable(UML2::Connector.__init__)


def test_uml2::connector_constructor_args():
    sig = inspect.signature(UML2::Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2::Classifier)


def test_uml2::classifier_constructor_exists():
    assert callable(UML2::Classifier.__init__)


def test_uml2::classifier_constructor_args():
    sig = inspect.signature(UML2::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::feature_is_not_abstract():
    assert not inspect.isabstract(UML2::Feature)


def test_uml2::feature_constructor_exists():
    assert callable(UML2::Feature.__init__)


def test_uml2::feature_constructor_args():
    sig = inspect.signature(UML2::Feature.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
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



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2::component_is_not_abstract():
    assert not inspect.isabstract(UML2::Component)


def test_uml2::component_constructor_exists():
    assert callable(UML2::Component.__init__)


def test_uml2::component_constructor_args():
    sig = inspect.signature(UML2::Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::port_is_not_abstract():
    assert not inspect.isabstract(UML2::Port)


def test_uml2::port_constructor_exists():
    assert callable(UML2::Port.__init__)


def test_uml2::port_constructor_args():
    sig = inspect.signature(UML2::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interface_is_not_abstract():
    assert not inspect.isabstract(UML2::Interface)


def test_uml2::interface_constructor_exists():
    assert callable(UML2::Interface.__init__)


def test_uml2::interface_constructor_args():
    sig = inspect.signature(UML2::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationItem)


def test_uml2::informationitem_constructor_exists():
    assert callable(UML2::InformationItem.__init__)


def test_uml2::informationitem_constructor_args():
    sig = inspect.signature(UML2::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2::Artifact)


def test_uml2::artifact_constructor_exists():
    assert callable(UML2::Artifact.__init__)


def test_uml2::artifact_constructor_args():
    sig = inspect.signature(UML2::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signal_is_not_abstract():
    assert not inspect.isabstract(UML2::Signal)


def test_uml2::signal_constructor_exists():
    assert callable(UML2::Signal.__init__)


def test_uml2::signal_constructor_args():
    sig = inspect.signature(UML2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2::association_is_not_abstract():
    assert not inspect.isabstract(UML2::Association)


def test_uml2::association_constructor_exists():
    assert callable(UML2::Association.__init__)


def test_uml2::association_constructor_args():
    sig = inspect.signature(UML2::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredClassifier)


def test_uml2::structuredclassifier_constructor_exists():
    assert callable(UML2::StructuredClassifier.__init__)


def test_uml2::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterableClassifier)


def test_uml2::parameterableclassifier_constructor_exists():
    assert callable(UML2::ParameterableClassifier.__init__)


def test_uml2::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::actor_is_not_abstract():
    assert not inspect.isabstract(UML2::Actor)


def test_uml2::actor_constructor_exists():
    assert callable(UML2::Actor.__init__)


def test_uml2::actor_constructor_args():
    sig = inspect.signature(UML2::Actor.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::device_is_not_abstract():
    assert not inspect.isabstract(UML2::Device)


def test_uml2::device_constructor_exists():
    assert callable(UML2::Device.__init__)


def test_uml2::device_constructor_args():
    sig = inspect.signature(UML2::Device.__init__)
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



def test_uml2::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteStructuralFeatureAction)


def test_uml2::writestructuralfeatureaction_constructor_exists():
    assert callable(UML2::WriteStructuralFeatureAction.__init__)


def test_uml2::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadStructuralFeatureAction)


def test_uml2::readstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ReadStructuralFeatureAction.__init__)


def test_uml2::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::EncapsulatedClassifier)


def test_uml2::encapsulatedclassifier_constructor_exists():
    assert callable(UML2::EncapsulatedClassifier.__init__)


def test_uml2::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2::EncapsulatedClassifier.__init__)
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



def test_uml2::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2::DataType)


def test_uml2::datatype_constructor_exists():
    assert callable(UML2::DataType.__init__)


def test_uml2::datatype_constructor_args():
    sig = inspect.signature(UML2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioredClassifier)


def test_uml2::behavioredclassifier_constructor_exists():
    assert callable(UML2::BehavioredClassifier.__init__)


def test_uml2::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionEnvironment)


def test_uml2::executionenvironment_constructor_exists():
    assert callable(UML2::ExecutionEnvironment.__init__)


def test_uml2::executionenvironment_constructor_args():
    sig = inspect.signature(UML2::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableClassifier)


def test_uml2::templateableclassifier_constructor_exists():
    assert callable(UML2::TemplateableClassifier.__init__)


def test_uml2::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2::UseCase)


def test_uml2::usecase_constructor_exists():
    assert callable(UML2::UseCase.__init__)


def test_uml2::usecase_constructor_args():
    sig = inspect.signature(UML2::UseCase.__init__)
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
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
)
UML2::Reception_strategy = st.builds(
    UML2::Reception,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2::RemoveStructuralFeatureValueAction,
)
UML2::AddStructuralFeatureValueAction_strategy = st.builds(
    UML2::AddStructuralFeatureValueAction,
)
UML2::DurationObservationAction_strategy = st.builds(
    UML2::DurationObservationAction,
)
UML2::TimeObservationAction_strategy = st.builds(
    UML2::TimeObservationAction,
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
Association_strategy = st.builds(
    Association,
)
UML2::Extension_strategy = st.builds(
    UML2::Extension,
)
UML2::CommunicationPath_strategy = st.builds(
    UML2::CommunicationPath,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2::Collaboration_strategy = st.builds(
    UML2::Collaboration,
)
UML2::Class_strategy = st.builds(
    UML2::Class,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
UML2::StructuralFeatureAction_strategy = st.builds(
    UML2::StructuralFeatureAction,
)
Feature_strategy = st.builds(
    Feature,
)
UML2::BehavioralFeature_strategy = st.builds(
    UML2::BehavioralFeature,
)
UML2::Connector_strategy = st.builds(
    UML2::Connector,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
)
UML2::Classifier_strategy = st.builds(
    UML2::Classifier,
)
UML2::Feature_strategy = st.builds(
    UML2::Feature,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
)
UML2::StateMachine_strategy = st.builds(
    UML2::StateMachine,
)
UML2::Interaction_strategy = st.builds(
    UML2::Interaction,
)
Class_strategy = st.builds(
    Class,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
UML2::Component_strategy = st.builds(
    UML2::Component,
)
UML2::Node_strategy = st.builds(
    UML2::Node,
)
Property_strategy = st.builds(
    Property,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2::Interface_strategy = st.builds(
    UML2::Interface,
)
UML2::InformationItem_strategy = st.builds(
    UML2::InformationItem,
)
UML2::Artifact_strategy = st.builds(
    UML2::Artifact,
)
UML2::Signal_strategy = st.builds(
    UML2::Signal,
)
UML2::Association_strategy = st.builds(
    UML2::Association,
)
UML2::StructuredClassifier_strategy = st.builds(
    UML2::StructuredClassifier,
)
UML2::ParameterableClassifier_strategy = st.builds(
    UML2::ParameterableClassifier,
)
UML2::Actor_strategy = st.builds(
    UML2::Actor,
)
Node_strategy = st.builds(
    Node,
)
UML2::Device_strategy = st.builds(
    UML2::Device,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2::ClearStructuralFeatureAction_strategy = st.builds(
    UML2::ClearStructuralFeatureAction,
)
UML2::WriteStructuralFeatureAction_strategy = st.builds(
    UML2::WriteStructuralFeatureAction,
)
UML2::ReadStructuralFeatureAction_strategy = st.builds(
    UML2::ReadStructuralFeatureAction,
)
UML2::EncapsulatedClassifier_strategy = st.builds(
    UML2::EncapsulatedClassifier,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2::DeploymentSpecification_strategy = st.builds(
    UML2::DeploymentSpecification,
)
UML2::DataType_strategy = st.builds(
    UML2::DataType,
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::ExecutionEnvironment_strategy = st.builds(
    UML2::ExecutionEnvironment,
)
UML2::TemplateableClassifier_strategy = st.builds(
    UML2::TemplateableClassifier,
)
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveStructuralFeatureValueAction)

@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddStructuralFeatureValueAction)

@given(instance=UML2::DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::DurationObservationAction)

@given(instance=UML2::TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::TimeObservationAction)

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

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2::collaboration_instantiation(instance):
    assert isinstance(instance, UML2::Collaboration)

@given(instance=UML2::Class_strategy)
@settings(max_examples=50)
def test_uml2::class_instantiation(instance):
    assert isinstance(instance, UML2::Class)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=UML2::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeatureAction)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UML2::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2::BehavioralFeature)

@given(instance=UML2::Connector_strategy)
@settings(max_examples=50)
def test_uml2::connector_instantiation(instance):
    assert isinstance(instance, UML2::Connector)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::Classifier_strategy)
@settings(max_examples=50)
def test_uml2::classifier_instantiation(instance):
    assert isinstance(instance, UML2::Classifier)

@given(instance=UML2::Feature_strategy)
@settings(max_examples=50)
def test_uml2::feature_instantiation(instance):
    assert isinstance(instance, UML2::Feature)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

@given(instance=UML2::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2::statemachine_instantiation(instance):
    assert isinstance(instance, UML2::StateMachine)

@given(instance=UML2::Interaction_strategy)
@settings(max_examples=50)
def test_uml2::interaction_instantiation(instance):
    assert isinstance(instance, UML2::Interaction)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=UML2::Component_strategy)
@settings(max_examples=50)
def test_uml2::component_instantiation(instance):
    assert isinstance(instance, UML2::Component)

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2::Interface_strategy)
@settings(max_examples=50)
def test_uml2::interface_instantiation(instance):
    assert isinstance(instance, UML2::Interface)

@given(instance=UML2::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2::informationitem_instantiation(instance):
    assert isinstance(instance, UML2::InformationItem)

@given(instance=UML2::Artifact_strategy)
@settings(max_examples=50)
def test_uml2::artifact_instantiation(instance):
    assert isinstance(instance, UML2::Artifact)

@given(instance=UML2::Signal_strategy)
@settings(max_examples=50)
def test_uml2::signal_instantiation(instance):
    assert isinstance(instance, UML2::Signal)

@given(instance=UML2::Association_strategy)
@settings(max_examples=50)
def test_uml2::association_instantiation(instance):
    assert isinstance(instance, UML2::Association)

@given(instance=UML2::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::StructuredClassifier)

@given(instance=UML2::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableClassifier)

@given(instance=UML2::Actor_strategy)
@settings(max_examples=50)
def test_uml2::actor_instantiation(instance):
    assert isinstance(instance, UML2::Actor)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2::Device_strategy)
@settings(max_examples=50)
def test_uml2::device_instantiation(instance):
    assert isinstance(instance, UML2::Device)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearStructuralFeatureAction)

@given(instance=UML2::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteStructuralFeatureAction)

@given(instance=UML2::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadStructuralFeatureAction)

@given(instance=UML2::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2::EncapsulatedClassifier)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentSpecification)

@given(instance=UML2::DataType_strategy)
@settings(max_examples=50)
def test_uml2::datatype_instantiation(instance):
    assert isinstance(instance, UML2::DataType)

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionEnvironment)

@given(instance=UML2::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableClassifier)

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)
