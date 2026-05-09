import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataType,
    Association,
    Artifact,
    Node,
    UML2WithID::Element,
    Behavior,
    EncapsulatedClassifier,
    BehavioredClassifier,
    StructuredClassifier,
    Property,
    Element,
    UML2WithID::PrimitiveType,
    UML2WithID::Enumeration,
    UML2WithID::ExecutionEnvironment,
    UML2WithID::Activity,
    UML2WithID::Device,
    UML2WithID::CommunicationPath,
    UML2WithID::UseCase,
    UML2WithID::Interaction,
    UML2WithID::ExtensionEnd,
    UML2WithID::Port,
    UML2WithID::Extension,
    UML2WithID::StateMachine,
    UML2WithID::Classifier,
    UML2WithID::Generalization,
    UML2WithID::Property,
    UML2WithID::Class,
    UML2WithID::DeploymentSpecification,
    UML2WithID::EncapsulatedClassifier,
    Classifier,
    UML2WithID::Artifact,
    UML2WithID::BehavioredClassifier,
    UML2WithID::Signal,
    UML2WithID::Interface,
    UML2WithID::Association,
    UML2WithID::TemplateableClassifier,
    UML2WithID::Actor,
    UML2WithID::StructuredClassifier,
    UML2WithID::DataType,
    UML2WithID::InformationItem,
    UML2WithID::ParameterableClassifier,
    UML2WithID::Collaboration,
    Class,
    UML2WithID::AssociationClass,
    UML2WithID::Node,
    UML2WithID::Behavior,
    UML2WithID::Stereotype,
    UML2WithID::Component,
    StateMachine,
    UML2WithID::ProtocolStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::element_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Element)


def test_uml2withid::element_constructor_exists():
    assert callable(UML2WithID::Element.__init__)


def test_uml2withid::element_constructor_args():
    sig = inspect.signature(UML2WithID::Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_uml2withid::element_has_ID():
    assert hasattr(UML2WithID::Element, "ID")
    descriptor = None
    for klass in UML2WithID::Element.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
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



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
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



def test_uml2withid::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::PrimitiveType)


def test_uml2withid::primitivetype_constructor_exists():
    assert callable(UML2WithID::PrimitiveType.__init__)


def test_uml2withid::primitivetype_constructor_args():
    sig = inspect.signature(UML2WithID::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Enumeration)


def test_uml2withid::enumeration_constructor_exists():
    assert callable(UML2WithID::Enumeration.__init__)


def test_uml2withid::enumeration_constructor_args():
    sig = inspect.signature(UML2WithID::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExecutionEnvironment)


def test_uml2withid::executionenvironment_constructor_exists():
    assert callable(UML2WithID::ExecutionEnvironment.__init__)


def test_uml2withid::executionenvironment_constructor_args():
    sig = inspect.signature(UML2WithID::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activity_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Activity)


def test_uml2withid::activity_constructor_exists():
    assert callable(UML2WithID::Activity.__init__)


def test_uml2withid::activity_constructor_args():
    sig = inspect.signature(UML2WithID::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::device_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Device)


def test_uml2withid::device_constructor_exists():
    assert callable(UML2WithID::Device.__init__)


def test_uml2withid::device_constructor_args():
    sig = inspect.signature(UML2WithID::Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CommunicationPath)


def test_uml2withid::communicationpath_constructor_exists():
    assert callable(UML2WithID::CommunicationPath.__init__)


def test_uml2withid::communicationpath_constructor_args():
    sig = inspect.signature(UML2WithID::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::UseCase)


def test_uml2withid::usecase_constructor_exists():
    assert callable(UML2WithID::UseCase.__init__)


def test_uml2withid::usecase_constructor_args():
    sig = inspect.signature(UML2WithID::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interaction)


def test_uml2withid::interaction_constructor_exists():
    assert callable(UML2WithID::Interaction.__init__)


def test_uml2withid::interaction_constructor_args():
    sig = inspect.signature(UML2WithID::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExtensionEnd)


def test_uml2withid::extensionend_constructor_exists():
    assert callable(UML2WithID::ExtensionEnd.__init__)


def test_uml2withid::extensionend_constructor_args():
    sig = inspect.signature(UML2WithID::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::port_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Port)


def test_uml2withid::port_constructor_exists():
    assert callable(UML2WithID::Port.__init__)


def test_uml2withid::port_constructor_args():
    sig = inspect.signature(UML2WithID::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extension_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Extension)


def test_uml2withid::extension_constructor_exists():
    assert callable(UML2WithID::Extension.__init__)


def test_uml2withid::extension_constructor_args():
    sig = inspect.signature(UML2WithID::Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StateMachine)


def test_uml2withid::statemachine_constructor_exists():
    assert callable(UML2WithID::StateMachine.__init__)


def test_uml2withid::statemachine_constructor_args():
    sig = inspect.signature(UML2WithID::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Classifier)


def test_uml2withid::classifier_constructor_exists():
    assert callable(UML2WithID::Classifier.__init__)


def test_uml2withid::classifier_constructor_args():
    sig = inspect.signature(UML2WithID::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::generalization_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Generalization)


def test_uml2withid::generalization_constructor_exists():
    assert callable(UML2WithID::Generalization.__init__)


def test_uml2withid::generalization_constructor_args():
    sig = inspect.signature(UML2WithID::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::property_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Property)


def test_uml2withid::property_constructor_exists():
    assert callable(UML2WithID::Property.__init__)


def test_uml2withid::property_constructor_args():
    sig = inspect.signature(UML2WithID::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::class_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Class)


def test_uml2withid::class_constructor_exists():
    assert callable(UML2WithID::Class.__init__)


def test_uml2withid::class_constructor_args():
    sig = inspect.signature(UML2WithID::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DeploymentSpecification)


def test_uml2withid::deploymentspecification_constructor_exists():
    assert callable(UML2WithID::DeploymentSpecification.__init__)


def test_uml2withid::deploymentspecification_constructor_args():
    sig = inspect.signature(UML2WithID::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::EncapsulatedClassifier)


def test_uml2withid::encapsulatedclassifier_constructor_exists():
    assert callable(UML2WithID::EncapsulatedClassifier.__init__)


def test_uml2withid::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Artifact)


def test_uml2withid::artifact_constructor_exists():
    assert callable(UML2WithID::Artifact.__init__)


def test_uml2withid::artifact_constructor_args():
    sig = inspect.signature(UML2WithID::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BehavioredClassifier)


def test_uml2withid::behavioredclassifier_constructor_exists():
    assert callable(UML2WithID::BehavioredClassifier.__init__)


def test_uml2withid::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::signal_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Signal)


def test_uml2withid::signal_constructor_exists():
    assert callable(UML2WithID::Signal.__init__)


def test_uml2withid::signal_constructor_args():
    sig = inspect.signature(UML2WithID::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interface_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interface)


def test_uml2withid::interface_constructor_exists():
    assert callable(UML2WithID::Interface.__init__)


def test_uml2withid::interface_constructor_args():
    sig = inspect.signature(UML2WithID::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::association_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Association)


def test_uml2withid::association_constructor_exists():
    assert callable(UML2WithID::Association.__init__)


def test_uml2withid::association_constructor_args():
    sig = inspect.signature(UML2WithID::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TemplateableClassifier)


def test_uml2withid::templateableclassifier_constructor_exists():
    assert callable(UML2WithID::TemplateableClassifier.__init__)


def test_uml2withid::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::actor_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Actor)


def test_uml2withid::actor_constructor_exists():
    assert callable(UML2WithID::Actor.__init__)


def test_uml2withid::actor_constructor_args():
    sig = inspect.signature(UML2WithID::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StructuredClassifier)


def test_uml2withid::structuredclassifier_constructor_exists():
    assert callable(UML2WithID::StructuredClassifier.__init__)


def test_uml2withid::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DataType)


def test_uml2withid::datatype_constructor_exists():
    assert callable(UML2WithID::DataType.__init__)


def test_uml2withid::datatype_constructor_args():
    sig = inspect.signature(UML2WithID::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InformationItem)


def test_uml2withid::informationitem_constructor_exists():
    assert callable(UML2WithID::InformationItem.__init__)


def test_uml2withid::informationitem_constructor_args():
    sig = inspect.signature(UML2WithID::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ParameterableClassifier)


def test_uml2withid::parameterableclassifier_constructor_exists():
    assert callable(UML2WithID::ParameterableClassifier.__init__)


def test_uml2withid::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Collaboration)


def test_uml2withid::collaboration_constructor_exists():
    assert callable(UML2WithID::Collaboration.__init__)


def test_uml2withid::collaboration_constructor_args():
    sig = inspect.signature(UML2WithID::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AssociationClass)


def test_uml2withid::associationclass_constructor_exists():
    assert callable(UML2WithID::AssociationClass.__init__)


def test_uml2withid::associationclass_constructor_args():
    sig = inspect.signature(UML2WithID::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::node_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Node)


def test_uml2withid::node_constructor_exists():
    assert callable(UML2WithID::Node.__init__)


def test_uml2withid::node_constructor_args():
    sig = inspect.signature(UML2WithID::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Behavior)


def test_uml2withid::behavior_constructor_exists():
    assert callable(UML2WithID::Behavior.__init__)


def test_uml2withid::behavior_constructor_args():
    sig = inspect.signature(UML2WithID::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Stereotype)


def test_uml2withid::stereotype_constructor_exists():
    assert callable(UML2WithID::Stereotype.__init__)


def test_uml2withid::stereotype_constructor_args():
    sig = inspect.signature(UML2WithID::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::component_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Component)


def test_uml2withid::component_constructor_exists():
    assert callable(UML2WithID::Component.__init__)


def test_uml2withid::component_constructor_args():
    sig = inspect.signature(UML2WithID::Component.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ProtocolStateMachine)


def test_uml2withid::protocolstatemachine_constructor_exists():
    assert callable(UML2WithID::ProtocolStateMachine.__init__)


def test_uml2withid::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2WithID::ProtocolStateMachine.__init__)
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
DataType_strategy = st.builds(
    DataType,
)
Association_strategy = st.builds(
    Association,
)
Artifact_strategy = st.builds(
    Artifact,
)
Node_strategy = st.builds(
    Node,
)
UML2WithID::Element_strategy = st.builds(
    UML2WithID::Element,
    ID=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
Property_strategy = st.builds(
    Property,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID::PrimitiveType_strategy = st.builds(
    UML2WithID::PrimitiveType,
)
UML2WithID::Enumeration_strategy = st.builds(
    UML2WithID::Enumeration,
)
UML2WithID::ExecutionEnvironment_strategy = st.builds(
    UML2WithID::ExecutionEnvironment,
)
UML2WithID::Activity_strategy = st.builds(
    UML2WithID::Activity,
)
UML2WithID::Device_strategy = st.builds(
    UML2WithID::Device,
)
UML2WithID::CommunicationPath_strategy = st.builds(
    UML2WithID::CommunicationPath,
)
UML2WithID::UseCase_strategy = st.builds(
    UML2WithID::UseCase,
)
UML2WithID::Interaction_strategy = st.builds(
    UML2WithID::Interaction,
)
UML2WithID::ExtensionEnd_strategy = st.builds(
    UML2WithID::ExtensionEnd,
)
UML2WithID::Port_strategy = st.builds(
    UML2WithID::Port,
)
UML2WithID::Extension_strategy = st.builds(
    UML2WithID::Extension,
)
UML2WithID::StateMachine_strategy = st.builds(
    UML2WithID::StateMachine,
)
UML2WithID::Classifier_strategy = st.builds(
    UML2WithID::Classifier,
)
UML2WithID::Generalization_strategy = st.builds(
    UML2WithID::Generalization,
)
UML2WithID::Property_strategy = st.builds(
    UML2WithID::Property,
)
UML2WithID::Class_strategy = st.builds(
    UML2WithID::Class,
)
UML2WithID::DeploymentSpecification_strategy = st.builds(
    UML2WithID::DeploymentSpecification,
)
UML2WithID::EncapsulatedClassifier_strategy = st.builds(
    UML2WithID::EncapsulatedClassifier,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2WithID::Artifact_strategy = st.builds(
    UML2WithID::Artifact,
)
UML2WithID::BehavioredClassifier_strategy = st.builds(
    UML2WithID::BehavioredClassifier,
)
UML2WithID::Signal_strategy = st.builds(
    UML2WithID::Signal,
)
UML2WithID::Interface_strategy = st.builds(
    UML2WithID::Interface,
)
UML2WithID::Association_strategy = st.builds(
    UML2WithID::Association,
)
UML2WithID::TemplateableClassifier_strategy = st.builds(
    UML2WithID::TemplateableClassifier,
)
UML2WithID::Actor_strategy = st.builds(
    UML2WithID::Actor,
)
UML2WithID::StructuredClassifier_strategy = st.builds(
    UML2WithID::StructuredClassifier,
)
UML2WithID::DataType_strategy = st.builds(
    UML2WithID::DataType,
)
UML2WithID::InformationItem_strategy = st.builds(
    UML2WithID::InformationItem,
)
UML2WithID::ParameterableClassifier_strategy = st.builds(
    UML2WithID::ParameterableClassifier,
)
UML2WithID::Collaboration_strategy = st.builds(
    UML2WithID::Collaboration,
)
Class_strategy = st.builds(
    Class,
)
UML2WithID::AssociationClass_strategy = st.builds(
    UML2WithID::AssociationClass,
)
UML2WithID::Node_strategy = st.builds(
    UML2WithID::Node,
)
UML2WithID::Behavior_strategy = st.builds(
    UML2WithID::Behavior,
)
UML2WithID::Stereotype_strategy = st.builds(
    UML2WithID::Stereotype,
)
UML2WithID::Component_strategy = st.builds(
    UML2WithID::Component,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2WithID::ProtocolStateMachine_strategy = st.builds(
    UML2WithID::ProtocolStateMachine,
)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2WithID::Element_strategy)
@settings(max_examples=50)
def test_uml2withid::element_instantiation(instance):
    assert isinstance(instance, UML2WithID::Element)

@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2withid::primitivetype_instantiation(instance):
    assert isinstance(instance, UML2WithID::PrimitiveType)

@given(instance=UML2WithID::Enumeration_strategy)
@settings(max_examples=50)
def test_uml2withid::enumeration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Enumeration)

@given(instance=UML2WithID::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2withid::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExecutionEnvironment)

@given(instance=UML2WithID::Activity_strategy)
@settings(max_examples=50)
def test_uml2withid::activity_instantiation(instance):
    assert isinstance(instance, UML2WithID::Activity)

@given(instance=UML2WithID::Device_strategy)
@settings(max_examples=50)
def test_uml2withid::device_instantiation(instance):
    assert isinstance(instance, UML2WithID::Device)

@given(instance=UML2WithID::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2withid::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2WithID::CommunicationPath)

@given(instance=UML2WithID::UseCase_strategy)
@settings(max_examples=50)
def test_uml2withid::usecase_instantiation(instance):
    assert isinstance(instance, UML2WithID::UseCase)

@given(instance=UML2WithID::Interaction_strategy)
@settings(max_examples=50)
def test_uml2withid::interaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interaction)

@given(instance=UML2WithID::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2withid::extensionend_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExtensionEnd)

@given(instance=UML2WithID::Port_strategy)
@settings(max_examples=50)
def test_uml2withid::port_instantiation(instance):
    assert isinstance(instance, UML2WithID::Port)

@given(instance=UML2WithID::Extension_strategy)
@settings(max_examples=50)
def test_uml2withid::extension_instantiation(instance):
    assert isinstance(instance, UML2WithID::Extension)

@given(instance=UML2WithID::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::statemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::StateMachine)

@given(instance=UML2WithID::Classifier_strategy)
@settings(max_examples=50)
def test_uml2withid::classifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::Classifier)

@given(instance=UML2WithID::Generalization_strategy)
@settings(max_examples=50)
def test_uml2withid::generalization_instantiation(instance):
    assert isinstance(instance, UML2WithID::Generalization)

@given(instance=UML2WithID::Property_strategy)
@settings(max_examples=50)
def test_uml2withid::property_instantiation(instance):
    assert isinstance(instance, UML2WithID::Property)

@given(instance=UML2WithID::Class_strategy)
@settings(max_examples=50)
def test_uml2withid::class_instantiation(instance):
    assert isinstance(instance, UML2WithID::Class)

@given(instance=UML2WithID::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2WithID::DeploymentSpecification)

@given(instance=UML2WithID::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::EncapsulatedClassifier)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2WithID::Artifact_strategy)
@settings(max_examples=50)
def test_uml2withid::artifact_instantiation(instance):
    assert isinstance(instance, UML2WithID::Artifact)

@given(instance=UML2WithID::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::BehavioredClassifier)

@given(instance=UML2WithID::Signal_strategy)
@settings(max_examples=50)
def test_uml2withid::signal_instantiation(instance):
    assert isinstance(instance, UML2WithID::Signal)

@given(instance=UML2WithID::Interface_strategy)
@settings(max_examples=50)
def test_uml2withid::interface_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interface)

@given(instance=UML2WithID::Association_strategy)
@settings(max_examples=50)
def test_uml2withid::association_instantiation(instance):
    assert isinstance(instance, UML2WithID::Association)

@given(instance=UML2WithID::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::TemplateableClassifier)

@given(instance=UML2WithID::Actor_strategy)
@settings(max_examples=50)
def test_uml2withid::actor_instantiation(instance):
    assert isinstance(instance, UML2WithID::Actor)

@given(instance=UML2WithID::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::StructuredClassifier)

@given(instance=UML2WithID::DataType_strategy)
@settings(max_examples=50)
def test_uml2withid::datatype_instantiation(instance):
    assert isinstance(instance, UML2WithID::DataType)

@given(instance=UML2WithID::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2withid::informationitem_instantiation(instance):
    assert isinstance(instance, UML2WithID::InformationItem)

@given(instance=UML2WithID::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::ParameterableClassifier)

@given(instance=UML2WithID::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2withid::collaboration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Collaboration)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2WithID::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid::associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID::AssociationClass)

@given(instance=UML2WithID::Node_strategy)
@settings(max_examples=50)
def test_uml2withid::node_instantiation(instance):
    assert isinstance(instance, UML2WithID::Node)

@given(instance=UML2WithID::Behavior_strategy)
@settings(max_examples=50)
def test_uml2withid::behavior_instantiation(instance):
    assert isinstance(instance, UML2WithID::Behavior)

@given(instance=UML2WithID::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2withid::stereotype_instantiation(instance):
    assert isinstance(instance, UML2WithID::Stereotype)

@given(instance=UML2WithID::Component_strategy)
@settings(max_examples=50)
def test_uml2withid::component_instantiation(instance):
    assert isinstance(instance, UML2WithID::Component)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2WithID::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::ProtocolStateMachine)
