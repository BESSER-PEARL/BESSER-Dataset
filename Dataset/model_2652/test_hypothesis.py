import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2WithID::Element,
    StateMachine,
    BehavioralFeature,
    BehavioredClassifier,
    Element,
    UML2WithID::Class,
    UML2WithID::BehavioralFeature,
    UML2WithID::UseCase,
    UML2WithID::Reception,
    UML2WithID::Operation,
    UML2WithID::Collaboration,
    UML2WithID::ProtocolStateMachine,
    Class,
    UML2WithID::AssociationClass,
    UML2WithID::Component,
    UML2WithID::Stereotype,
    UML2WithID::Node,
    Behavior,
    UML2WithID::Interaction,
    UML2WithID::StateMachine,
    UML2WithID::Activity,
    UML2WithID::Behavior,
    UML2WithID::BehavioredClassifier,
    Node,
    UML2WithID::ExecutionEnvironment,
    UML2WithID::Device,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::class_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Class)


def test_uml2withid::class_constructor_exists():
    assert callable(UML2WithID::Class.__init__)


def test_uml2withid::class_constructor_args():
    sig = inspect.signature(UML2WithID::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BehavioralFeature)


def test_uml2withid::behavioralfeature_constructor_exists():
    assert callable(UML2WithID::BehavioralFeature.__init__)


def test_uml2withid::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2WithID::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::UseCase)


def test_uml2withid::usecase_constructor_exists():
    assert callable(UML2WithID::UseCase.__init__)


def test_uml2withid::usecase_constructor_args():
    sig = inspect.signature(UML2WithID::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::reception_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Reception)


def test_uml2withid::reception_constructor_exists():
    assert callable(UML2WithID::Reception.__init__)


def test_uml2withid::reception_constructor_args():
    sig = inspect.signature(UML2WithID::Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::operation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Operation)


def test_uml2withid::operation_constructor_exists():
    assert callable(UML2WithID::Operation.__init__)


def test_uml2withid::operation_constructor_args():
    sig = inspect.signature(UML2WithID::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Collaboration)


def test_uml2withid::collaboration_constructor_exists():
    assert callable(UML2WithID::Collaboration.__init__)


def test_uml2withid::collaboration_constructor_args():
    sig = inspect.signature(UML2WithID::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ProtocolStateMachine)


def test_uml2withid::protocolstatemachine_constructor_exists():
    assert callable(UML2WithID::ProtocolStateMachine.__init__)


def test_uml2withid::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2WithID::ProtocolStateMachine.__init__)
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



def test_uml2withid::component_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Component)


def test_uml2withid::component_constructor_exists():
    assert callable(UML2WithID::Component.__init__)


def test_uml2withid::component_constructor_args():
    sig = inspect.signature(UML2WithID::Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Stereotype)


def test_uml2withid::stereotype_constructor_exists():
    assert callable(UML2WithID::Stereotype.__init__)


def test_uml2withid::stereotype_constructor_args():
    sig = inspect.signature(UML2WithID::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::node_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Node)


def test_uml2withid::node_constructor_exists():
    assert callable(UML2WithID::Node.__init__)


def test_uml2withid::node_constructor_args():
    sig = inspect.signature(UML2WithID::Node.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interaction)


def test_uml2withid::interaction_constructor_exists():
    assert callable(UML2WithID::Interaction.__init__)


def test_uml2withid::interaction_constructor_args():
    sig = inspect.signature(UML2WithID::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StateMachine)


def test_uml2withid::statemachine_constructor_exists():
    assert callable(UML2WithID::StateMachine.__init__)


def test_uml2withid::statemachine_constructor_args():
    sig = inspect.signature(UML2WithID::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activity_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Activity)


def test_uml2withid::activity_constructor_exists():
    assert callable(UML2WithID::Activity.__init__)


def test_uml2withid::activity_constructor_args():
    sig = inspect.signature(UML2WithID::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Behavior)


def test_uml2withid::behavior_constructor_exists():
    assert callable(UML2WithID::Behavior.__init__)


def test_uml2withid::behavior_constructor_args():
    sig = inspect.signature(UML2WithID::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BehavioredClassifier)


def test_uml2withid::behavioredclassifier_constructor_exists():
    assert callable(UML2WithID::BehavioredClassifier.__init__)


def test_uml2withid::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExecutionEnvironment)


def test_uml2withid::executionenvironment_constructor_exists():
    assert callable(UML2WithID::ExecutionEnvironment.__init__)


def test_uml2withid::executionenvironment_constructor_args():
    sig = inspect.signature(UML2WithID::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::device_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Device)


def test_uml2withid::device_constructor_exists():
    assert callable(UML2WithID::Device.__init__)


def test_uml2withid::device_constructor_args():
    sig = inspect.signature(UML2WithID::Device.__init__)
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
UML2WithID::Element_strategy = st.builds(
    UML2WithID::Element,
    ID=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID::Class_strategy = st.builds(
    UML2WithID::Class,
)
UML2WithID::BehavioralFeature_strategy = st.builds(
    UML2WithID::BehavioralFeature,
)
UML2WithID::UseCase_strategy = st.builds(
    UML2WithID::UseCase,
)
UML2WithID::Reception_strategy = st.builds(
    UML2WithID::Reception,
)
UML2WithID::Operation_strategy = st.builds(
    UML2WithID::Operation,
)
UML2WithID::Collaboration_strategy = st.builds(
    UML2WithID::Collaboration,
)
UML2WithID::ProtocolStateMachine_strategy = st.builds(
    UML2WithID::ProtocolStateMachine,
)
Class_strategy = st.builds(
    Class,
)
UML2WithID::AssociationClass_strategy = st.builds(
    UML2WithID::AssociationClass,
)
UML2WithID::Component_strategy = st.builds(
    UML2WithID::Component,
)
UML2WithID::Stereotype_strategy = st.builds(
    UML2WithID::Stereotype,
)
UML2WithID::Node_strategy = st.builds(
    UML2WithID::Node,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2WithID::Interaction_strategy = st.builds(
    UML2WithID::Interaction,
)
UML2WithID::StateMachine_strategy = st.builds(
    UML2WithID::StateMachine,
)
UML2WithID::Activity_strategy = st.builds(
    UML2WithID::Activity,
)
UML2WithID::Behavior_strategy = st.builds(
    UML2WithID::Behavior,
)
UML2WithID::BehavioredClassifier_strategy = st.builds(
    UML2WithID::BehavioredClassifier,
)
Node_strategy = st.builds(
    Node,
)
UML2WithID::ExecutionEnvironment_strategy = st.builds(
    UML2WithID::ExecutionEnvironment,
)
UML2WithID::Device_strategy = st.builds(
    UML2WithID::Device,
)

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

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID::Class_strategy)
@settings(max_examples=50)
def test_uml2withid::class_instantiation(instance):
    assert isinstance(instance, UML2WithID::Class)

@given(instance=UML2WithID::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2withid::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2WithID::BehavioralFeature)

@given(instance=UML2WithID::UseCase_strategy)
@settings(max_examples=50)
def test_uml2withid::usecase_instantiation(instance):
    assert isinstance(instance, UML2WithID::UseCase)

@given(instance=UML2WithID::Reception_strategy)
@settings(max_examples=50)
def test_uml2withid::reception_instantiation(instance):
    assert isinstance(instance, UML2WithID::Reception)

@given(instance=UML2WithID::Operation_strategy)
@settings(max_examples=50)
def test_uml2withid::operation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Operation)

@given(instance=UML2WithID::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2withid::collaboration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Collaboration)

@given(instance=UML2WithID::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::ProtocolStateMachine)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2WithID::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid::associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID::AssociationClass)

@given(instance=UML2WithID::Component_strategy)
@settings(max_examples=50)
def test_uml2withid::component_instantiation(instance):
    assert isinstance(instance, UML2WithID::Component)

@given(instance=UML2WithID::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2withid::stereotype_instantiation(instance):
    assert isinstance(instance, UML2WithID::Stereotype)

@given(instance=UML2WithID::Node_strategy)
@settings(max_examples=50)
def test_uml2withid::node_instantiation(instance):
    assert isinstance(instance, UML2WithID::Node)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2WithID::Interaction_strategy)
@settings(max_examples=50)
def test_uml2withid::interaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interaction)

@given(instance=UML2WithID::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::statemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::StateMachine)

@given(instance=UML2WithID::Activity_strategy)
@settings(max_examples=50)
def test_uml2withid::activity_instantiation(instance):
    assert isinstance(instance, UML2WithID::Activity)

@given(instance=UML2WithID::Behavior_strategy)
@settings(max_examples=50)
def test_uml2withid::behavior_instantiation(instance):
    assert isinstance(instance, UML2WithID::Behavior)

@given(instance=UML2WithID::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::BehavioredClassifier)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2WithID::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2withid::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExecutionEnvironment)

@given(instance=UML2WithID::Device_strategy)
@settings(max_examples=50)
def test_uml2withid::device_instantiation(instance):
    assert isinstance(instance, UML2WithID::Device)
