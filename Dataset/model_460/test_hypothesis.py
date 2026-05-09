import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CentralBufferNode,
    UML2::DataStoreNode,
    OpaqueExpression,
    UML2::Expression,
    StructuralFeature,
    UML2::Property,
    StateMachine,
    UML2::ProtocolStateMachine,
    Interval,
    UML2::DurationInterval,
    UML2::TimeInterval,
    StructuredClassifier,
    UML2::EncapsulatedClassifier,
    InputPin,
    UML2::ValuePin,
    Pin,
    UML2::InputPin,
    UML2::OutputPin,
    Class,
    UML2::Component,
    UML2::Behavior,
    UML2::Node,
    UML2::Stereotype,
    UML2::Type,
    UML2::TypedElement,
    UML2::Feature,
    EncapsulatedClassifier,
    Artifact,
    UML2::DeploymentSpecification,
    Feature,
    UML2::BehavioralFeature,
    UML2::Connector,
    UML2::StructuralFeatureAction,
    BehavioralFeature,
    UML2::Reception,
    DataType,
    UML2::PrimitiveType,
    UML2::Enumeration,
    LiteralSpecification,
    UML2::LiteralUnlimitedNatural,
    UML2::LiteralBoolean,
    UML2::LiteralString,
    UML2::LiteralNull,
    UML2::LiteralInteger,
    BehavioredClassifier,
    UML2::Collaboration,
    UML2::Class,
    UML2::UseCase,
    Property,
    UML2::ExtensionEnd,
    UML2::Port,
    ValueSpecification,
    UML2::InstanceValue,
    UML2::LiteralSpecification,
    UML2::TimeExpression,
    UML2::Interval,
    UML2::OpaqueExpression,
    UML2::Duration,
    Classifier,
    UML2::Association,
    UML2::Actor,
    UML2::InformationItem,
    UML2::Signal,
    UML2::TemplateableClassifier,
    UML2::Interface,
    UML2::BehavioredClassifier,
    UML2::ParameterableClassifier,
    UML2::DataType,
    UML2::Artifact,
    UML2::StructuredClassifier,
    ObjectNode,
    UML2::CentralBufferNode,
    UML2::ActivityParameterNode,
    UML2::ExpansionNode,
    UML2::Pin,
    Node,
    UML2::Device,
    UML2::ExecutionEnvironment,
    TypedElement,
    UML2::Operation,
    UML2::ObjectNode,
    UML2::Parameter,
    UML2::Variable,
    UML2::StructuralFeature,
    UML2::ValueSpecification,
    WriteStructuralFeatureAction,
    UML2::RemoveStructuralFeatureValueAction,
    UML2::AddStructuralFeatureValueAction,
    UML2::DurationObservationAction,
    UML2::TimeObservationAction,
    Behavior,
    UML2::Activity,
    UML2::StateMachine,
    UML2::Interaction,
    StructuralFeatureAction,
    UML2::ReadStructuralFeatureAction,
    UML2::WriteStructuralFeatureAction,
    UML2::ClearStructuralFeatureAction,
    Type,
    UML2::Classifier,
    Association,
    UML2::Extension,
    UML2::AssociationClass,
    UML2::CommunicationPath,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2::DataStoreNode)


def test_uml2::datastorenode_constructor_exists():
    assert callable(UML2::DataStoreNode.__init__)


def test_uml2::datastorenode_constructor_args():
    sig = inspect.signature(UML2::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expression_is_not_abstract():
    assert not inspect.isabstract(UML2::Expression)


def test_uml2::expression_constructor_exists():
    assert callable(UML2::Expression.__init__)


def test_uml2::expression_constructor_args():
    sig = inspect.signature(UML2::Expression.__init__)
    params = list(sig.parameters.keys())



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



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationInterval)


def test_uml2::durationinterval_constructor_exists():
    assert callable(UML2::DurationInterval.__init__)


def test_uml2::durationinterval_constructor_args():
    sig = inspect.signature(UML2::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeInterval)


def test_uml2::timeinterval_constructor_exists():
    assert callable(UML2::TimeInterval.__init__)


def test_uml2::timeinterval_constructor_args():
    sig = inspect.signature(UML2::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::EncapsulatedClassifier)


def test_uml2::encapsulatedclassifier_constructor_exists():
    assert callable(UML2::EncapsulatedClassifier.__init__)


def test_uml2::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2::ValuePin)


def test_uml2::valuepin_constructor_exists():
    assert callable(UML2::ValuePin.__init__)


def test_uml2::valuepin_constructor_args():
    sig = inspect.signature(UML2::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::InputPin)


def test_uml2::inputpin_constructor_exists():
    assert callable(UML2::InputPin.__init__)


def test_uml2::inputpin_constructor_args():
    sig = inspect.signature(UML2::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::OutputPin)


def test_uml2::outputpin_constructor_exists():
    assert callable(UML2::OutputPin.__init__)


def test_uml2::outputpin_constructor_args():
    sig = inspect.signature(UML2::OutputPin.__init__)
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



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2::type_is_not_abstract():
    assert not inspect.isabstract(UML2::Type)


def test_uml2::type_constructor_exists():
    assert callable(UML2::Type.__init__)


def test_uml2::type_constructor_args():
    sig = inspect.signature(UML2::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2::typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2::TypedElement)


def test_uml2::typedelement_constructor_exists():
    assert callable(UML2::TypedElement.__init__)


def test_uml2::typedelement_constructor_args():
    sig = inspect.signature(UML2::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::feature_is_not_abstract():
    assert not inspect.isabstract(UML2::Feature)


def test_uml2::feature_constructor_exists():
    assert callable(UML2::Feature.__init__)


def test_uml2::feature_constructor_args():
    sig = inspect.signature(UML2::Feature.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
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



def test_uml2::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeatureAction)


def test_uml2::structuralfeatureaction_constructor_exists():
    assert callable(UML2::StructuralFeatureAction.__init__)


def test_uml2::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
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



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralUnlimitedNatural)


def test_uml2::literalunlimitednatural_constructor_exists():
    assert callable(UML2::LiteralUnlimitedNatural.__init__)


def test_uml2::literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralBoolean)


def test_uml2::literalboolean_constructor_exists():
    assert callable(UML2::LiteralBoolean.__init__)


def test_uml2::literalboolean_constructor_args():
    sig = inspect.signature(UML2::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralString)


def test_uml2::literalstring_constructor_exists():
    assert callable(UML2::LiteralString.__init__)


def test_uml2::literalstring_constructor_args():
    sig = inspect.signature(UML2::LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralNull)


def test_uml2::literalnull_constructor_exists():
    assert callable(UML2::LiteralNull.__init__)


def test_uml2::literalnull_constructor_args():
    sig = inspect.signature(UML2::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralInteger)


def test_uml2::literalinteger_constructor_exists():
    assert callable(UML2::LiteralInteger.__init__)


def test_uml2::literalinteger_constructor_args():
    sig = inspect.signature(UML2::LiteralInteger.__init__)
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



def test_uml2::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2::UseCase)


def test_uml2::usecase_constructor_exists():
    assert callable(UML2::UseCase.__init__)


def test_uml2::usecase_constructor_args():
    sig = inspect.signature(UML2::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::port_is_not_abstract():
    assert not inspect.isabstract(UML2::Port)


def test_uml2::port_constructor_exists():
    assert callable(UML2::Port.__init__)


def test_uml2::port_constructor_args():
    sig = inspect.signature(UML2::Port.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2::InstanceValue)


def test_uml2::instancevalue_constructor_exists():
    assert callable(UML2::InstanceValue.__init__)


def test_uml2::instancevalue_constructor_args():
    sig = inspect.signature(UML2::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralSpecification)


def test_uml2::literalspecification_constructor_exists():
    assert callable(UML2::LiteralSpecification.__init__)


def test_uml2::literalspecification_constructor_args():
    sig = inspect.signature(UML2::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeExpression)


def test_uml2::timeexpression_constructor_exists():
    assert callable(UML2::TimeExpression.__init__)


def test_uml2::timeexpression_constructor_args():
    sig = inspect.signature(UML2::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interval_is_not_abstract():
    assert not inspect.isabstract(UML2::Interval)


def test_uml2::interval_constructor_exists():
    assert callable(UML2::Interval.__init__)


def test_uml2::interval_constructor_args():
    sig = inspect.signature(UML2::Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::OpaqueExpression)


def test_uml2::opaqueexpression_constructor_exists():
    assert callable(UML2::OpaqueExpression.__init__)


def test_uml2::opaqueexpression_constructor_args():
    sig = inspect.signature(UML2::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::duration_is_not_abstract():
    assert not inspect.isabstract(UML2::Duration)


def test_uml2::duration_constructor_exists():
    assert callable(UML2::Duration.__init__)


def test_uml2::duration_constructor_args():
    sig = inspect.signature(UML2::Duration.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::association_is_not_abstract():
    assert not inspect.isabstract(UML2::Association)


def test_uml2::association_constructor_exists():
    assert callable(UML2::Association.__init__)


def test_uml2::association_constructor_args():
    sig = inspect.signature(UML2::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2::actor_is_not_abstract():
    assert not inspect.isabstract(UML2::Actor)


def test_uml2::actor_constructor_exists():
    assert callable(UML2::Actor.__init__)


def test_uml2::actor_constructor_args():
    sig = inspect.signature(UML2::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationItem)


def test_uml2::informationitem_constructor_exists():
    assert callable(UML2::InformationItem.__init__)


def test_uml2::informationitem_constructor_args():
    sig = inspect.signature(UML2::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signal_is_not_abstract():
    assert not inspect.isabstract(UML2::Signal)


def test_uml2::signal_constructor_exists():
    assert callable(UML2::Signal.__init__)


def test_uml2::signal_constructor_args():
    sig = inspect.signature(UML2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableClassifier)


def test_uml2::templateableclassifier_constructor_exists():
    assert callable(UML2::TemplateableClassifier.__init__)


def test_uml2::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interface_is_not_abstract():
    assert not inspect.isabstract(UML2::Interface)


def test_uml2::interface_constructor_exists():
    assert callable(UML2::Interface.__init__)


def test_uml2::interface_constructor_args():
    sig = inspect.signature(UML2::Interface.__init__)
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



def test_uml2::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2::DataType)


def test_uml2::datatype_constructor_exists():
    assert callable(UML2::DataType.__init__)


def test_uml2::datatype_constructor_args():
    sig = inspect.signature(UML2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2::Artifact)


def test_uml2::artifact_constructor_exists():
    assert callable(UML2::Artifact.__init__)


def test_uml2::artifact_constructor_args():
    sig = inspect.signature(UML2::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredClassifier)


def test_uml2::structuredclassifier_constructor_exists():
    assert callable(UML2::StructuredClassifier.__init__)


def test_uml2::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2::CentralBufferNode)


def test_uml2::centralbuffernode_constructor_exists():
    assert callable(UML2::CentralBufferNode.__init__)


def test_uml2::centralbuffernode_constructor_args():
    sig = inspect.signature(UML2::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityParameterNode)


def test_uml2::activityparameternode_constructor_exists():
    assert callable(UML2::ActivityParameterNode.__init__)


def test_uml2::activityparameternode_constructor_args():
    sig = inspect.signature(UML2::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ExpansionNode)


def test_uml2::expansionnode_constructor_exists():
    assert callable(UML2::ExpansionNode.__init__)


def test_uml2::expansionnode_constructor_args():
    sig = inspect.signature(UML2::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pin_is_not_abstract():
    assert not inspect.isabstract(UML2::Pin)


def test_uml2::pin_constructor_exists():
    assert callable(UML2::Pin.__init__)


def test_uml2::pin_constructor_args():
    sig = inspect.signature(UML2::Pin.__init__)
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



def test_uml2::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionEnvironment)


def test_uml2::executionenvironment_constructor_exists():
    assert callable(UML2::ExecutionEnvironment.__init__)


def test_uml2::executionenvironment_constructor_args():
    sig = inspect.signature(UML2::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ObjectNode)


def test_uml2::objectnode_constructor_exists():
    assert callable(UML2::ObjectNode.__init__)


def test_uml2::objectnode_constructor_args():
    sig = inspect.signature(UML2::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2::Parameter)


def test_uml2::parameter_constructor_exists():
    assert callable(UML2::Parameter.__init__)


def test_uml2::parameter_constructor_args():
    sig = inspect.signature(UML2::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variable_is_not_abstract():
    assert not inspect.isabstract(UML2::Variable)


def test_uml2::variable_constructor_exists():
    assert callable(UML2::Variable.__init__)


def test_uml2::variable_constructor_args():
    sig = inspect.signature(UML2::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2::ValueSpecification)


def test_uml2::valuespecification_constructor_exists():
    assert callable(UML2::ValueSpecification.__init__)


def test_uml2::valuespecification_constructor_args():
    sig = inspect.signature(UML2::ValueSpecification.__init__)
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



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
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



def test_uml2::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearStructuralFeatureAction)


def test_uml2::clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ClearStructuralFeatureAction.__init__)


def test_uml2::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2::Classifier)


def test_uml2::classifier_constructor_exists():
    assert callable(UML2::Classifier.__init__)


def test_uml2::classifier_constructor_args():
    sig = inspect.signature(UML2::Classifier.__init__)
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



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2::CommunicationPath)


def test_uml2::communicationpath_constructor_exists():
    assert callable(UML2::CommunicationPath.__init__)


def test_uml2::communicationpath_constructor_args():
    sig = inspect.signature(UML2::CommunicationPath.__init__)
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
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2::DataStoreNode_strategy = st.builds(
    UML2::DataStoreNode,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2::Expression_strategy = st.builds(
    UML2::Expression,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
Interval_strategy = st.builds(
    Interval,
)
UML2::DurationInterval_strategy = st.builds(
    UML2::DurationInterval,
)
UML2::TimeInterval_strategy = st.builds(
    UML2::TimeInterval,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2::EncapsulatedClassifier_strategy = st.builds(
    UML2::EncapsulatedClassifier,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2::ValuePin_strategy = st.builds(
    UML2::ValuePin,
)
Pin_strategy = st.builds(
    Pin,
)
UML2::InputPin_strategy = st.builds(
    UML2::InputPin,
)
UML2::OutputPin_strategy = st.builds(
    UML2::OutputPin,
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
UML2::Node_strategy = st.builds(
    UML2::Node,
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
UML2::Type_strategy = st.builds(
    UML2::Type,
)
UML2::TypedElement_strategy = st.builds(
    UML2::TypedElement,
)
UML2::Feature_strategy = st.builds(
    UML2::Feature,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2::DeploymentSpecification_strategy = st.builds(
    UML2::DeploymentSpecification,
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
UML2::StructuralFeatureAction_strategy = st.builds(
    UML2::StructuralFeatureAction,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2::Reception_strategy = st.builds(
    UML2::Reception,
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
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2::LiteralUnlimitedNatural_strategy = st.builds(
    UML2::LiteralUnlimitedNatural,
)
UML2::LiteralBoolean_strategy = st.builds(
    UML2::LiteralBoolean,
)
UML2::LiteralString_strategy = st.builds(
    UML2::LiteralString,
)
UML2::LiteralNull_strategy = st.builds(
    UML2::LiteralNull,
)
UML2::LiteralInteger_strategy = st.builds(
    UML2::LiteralInteger,
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
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)
Property_strategy = st.builds(
    Property,
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2::InstanceValue_strategy = st.builds(
    UML2::InstanceValue,
)
UML2::LiteralSpecification_strategy = st.builds(
    UML2::LiteralSpecification,
)
UML2::TimeExpression_strategy = st.builds(
    UML2::TimeExpression,
)
UML2::Interval_strategy = st.builds(
    UML2::Interval,
)
UML2::OpaqueExpression_strategy = st.builds(
    UML2::OpaqueExpression,
)
UML2::Duration_strategy = st.builds(
    UML2::Duration,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2::Association_strategy = st.builds(
    UML2::Association,
)
UML2::Actor_strategy = st.builds(
    UML2::Actor,
)
UML2::InformationItem_strategy = st.builds(
    UML2::InformationItem,
)
UML2::Signal_strategy = st.builds(
    UML2::Signal,
)
UML2::TemplateableClassifier_strategy = st.builds(
    UML2::TemplateableClassifier,
)
UML2::Interface_strategy = st.builds(
    UML2::Interface,
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::ParameterableClassifier_strategy = st.builds(
    UML2::ParameterableClassifier,
)
UML2::DataType_strategy = st.builds(
    UML2::DataType,
)
UML2::Artifact_strategy = st.builds(
    UML2::Artifact,
)
UML2::StructuredClassifier_strategy = st.builds(
    UML2::StructuredClassifier,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2::CentralBufferNode_strategy = st.builds(
    UML2::CentralBufferNode,
)
UML2::ActivityParameterNode_strategy = st.builds(
    UML2::ActivityParameterNode,
)
UML2::ExpansionNode_strategy = st.builds(
    UML2::ExpansionNode,
)
UML2::Pin_strategy = st.builds(
    UML2::Pin,
)
Node_strategy = st.builds(
    Node,
)
UML2::Device_strategy = st.builds(
    UML2::Device,
)
UML2::ExecutionEnvironment_strategy = st.builds(
    UML2::ExecutionEnvironment,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
)
UML2::ObjectNode_strategy = st.builds(
    UML2::ObjectNode,
)
UML2::Parameter_strategy = st.builds(
    UML2::Parameter,
)
UML2::Variable_strategy = st.builds(
    UML2::Variable,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
)
UML2::ValueSpecification_strategy = st.builds(
    UML2::ValueSpecification,
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
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2::ReadStructuralFeatureAction_strategy = st.builds(
    UML2::ReadStructuralFeatureAction,
)
UML2::WriteStructuralFeatureAction_strategy = st.builds(
    UML2::WriteStructuralFeatureAction,
)
UML2::ClearStructuralFeatureAction_strategy = st.builds(
    UML2::ClearStructuralFeatureAction,
)
Type_strategy = st.builds(
    Type,
)
UML2::Classifier_strategy = st.builds(
    UML2::Classifier,
)
Association_strategy = st.builds(
    Association,
)
UML2::Extension_strategy = st.builds(
    UML2::Extension,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
)
UML2::CommunicationPath_strategy = st.builds(
    UML2::CommunicationPath,
)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2::datastorenode_instantiation(instance):
    assert isinstance(instance, UML2::DataStoreNode)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2::Expression_strategy)
@settings(max_examples=50)
def test_uml2::expression_instantiation(instance):
    assert isinstance(instance, UML2::Expression)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2::durationinterval_instantiation(instance):
    assert isinstance(instance, UML2::DurationInterval)

@given(instance=UML2::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2::timeinterval_instantiation(instance):
    assert isinstance(instance, UML2::TimeInterval)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2::EncapsulatedClassifier)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2::ValuePin_strategy)
@settings(max_examples=50)
def test_uml2::valuepin_instantiation(instance):
    assert isinstance(instance, UML2::ValuePin)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2::InputPin_strategy)
@settings(max_examples=50)
def test_uml2::inputpin_instantiation(instance):
    assert isinstance(instance, UML2::InputPin)

@given(instance=UML2::OutputPin_strategy)
@settings(max_examples=50)
def test_uml2::outputpin_instantiation(instance):
    assert isinstance(instance, UML2::OutputPin)

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

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=UML2::Type_strategy)
@settings(max_examples=50)
def test_uml2::type_instantiation(instance):
    assert isinstance(instance, UML2::Type)

@given(instance=UML2::TypedElement_strategy)
@settings(max_examples=50)
def test_uml2::typedelement_instantiation(instance):
    assert isinstance(instance, UML2::TypedElement)

@given(instance=UML2::Feature_strategy)
@settings(max_examples=50)
def test_uml2::feature_instantiation(instance):
    assert isinstance(instance, UML2::Feature)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentSpecification)

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

@given(instance=UML2::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeatureAction)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)

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

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2::LiteralUnlimitedNatural)

@given(instance=UML2::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2::literalboolean_instantiation(instance):
    assert isinstance(instance, UML2::LiteralBoolean)

@given(instance=UML2::LiteralString_strategy)
@settings(max_examples=50)
def test_uml2::literalstring_instantiation(instance):
    assert isinstance(instance, UML2::LiteralString)

@given(instance=UML2::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2::literalnull_instantiation(instance):
    assert isinstance(instance, UML2::LiteralNull)

@given(instance=UML2::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2::literalinteger_instantiation(instance):
    assert isinstance(instance, UML2::LiteralInteger)

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

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2::instancevalue_instantiation(instance):
    assert isinstance(instance, UML2::InstanceValue)

@given(instance=UML2::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2::literalspecification_instantiation(instance):
    assert isinstance(instance, UML2::LiteralSpecification)

@given(instance=UML2::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2::timeexpression_instantiation(instance):
    assert isinstance(instance, UML2::TimeExpression)

@given(instance=UML2::Interval_strategy)
@settings(max_examples=50)
def test_uml2::interval_instantiation(instance):
    assert isinstance(instance, UML2::Interval)

@given(instance=UML2::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2::OpaqueExpression)

@given(instance=UML2::Duration_strategy)
@settings(max_examples=50)
def test_uml2::duration_instantiation(instance):
    assert isinstance(instance, UML2::Duration)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2::Association_strategy)
@settings(max_examples=50)
def test_uml2::association_instantiation(instance):
    assert isinstance(instance, UML2::Association)

@given(instance=UML2::Actor_strategy)
@settings(max_examples=50)
def test_uml2::actor_instantiation(instance):
    assert isinstance(instance, UML2::Actor)

@given(instance=UML2::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2::informationitem_instantiation(instance):
    assert isinstance(instance, UML2::InformationItem)

@given(instance=UML2::Signal_strategy)
@settings(max_examples=50)
def test_uml2::signal_instantiation(instance):
    assert isinstance(instance, UML2::Signal)

@given(instance=UML2::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableClassifier)

@given(instance=UML2::Interface_strategy)
@settings(max_examples=50)
def test_uml2::interface_instantiation(instance):
    assert isinstance(instance, UML2::Interface)

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableClassifier)

@given(instance=UML2::DataType_strategy)
@settings(max_examples=50)
def test_uml2::datatype_instantiation(instance):
    assert isinstance(instance, UML2::DataType)

@given(instance=UML2::Artifact_strategy)
@settings(max_examples=50)
def test_uml2::artifact_instantiation(instance):
    assert isinstance(instance, UML2::Artifact)

@given(instance=UML2::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::StructuredClassifier)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2::centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2::CentralBufferNode)

@given(instance=UML2::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2::activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityParameterNode)

@given(instance=UML2::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2::expansionnode_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionNode)

@given(instance=UML2::Pin_strategy)
@settings(max_examples=50)
def test_uml2::pin_instantiation(instance):
    assert isinstance(instance, UML2::Pin)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2::Device_strategy)
@settings(max_examples=50)
def test_uml2::device_instantiation(instance):
    assert isinstance(instance, UML2::Device)

@given(instance=UML2::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionEnvironment)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=UML2::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2::objectnode_instantiation(instance):
    assert isinstance(instance, UML2::ObjectNode)

@given(instance=UML2::Parameter_strategy)
@settings(max_examples=50)
def test_uml2::parameter_instantiation(instance):
    assert isinstance(instance, UML2::Parameter)

@given(instance=UML2::Variable_strategy)
@settings(max_examples=50)
def test_uml2::variable_instantiation(instance):
    assert isinstance(instance, UML2::Variable)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2::valuespecification_instantiation(instance):
    assert isinstance(instance, UML2::ValueSpecification)

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

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadStructuralFeatureAction)

@given(instance=UML2::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteStructuralFeatureAction)

@given(instance=UML2::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearStructuralFeatureAction)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UML2::Classifier_strategy)
@settings(max_examples=50)
def test_uml2::classifier_instantiation(instance):
    assert isinstance(instance, UML2::Classifier)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2::Extension_strategy)
@settings(max_examples=50)
def test_uml2::extension_instantiation(instance):
    assert isinstance(instance, UML2::Extension)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

@given(instance=UML2::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2::CommunicationPath)
