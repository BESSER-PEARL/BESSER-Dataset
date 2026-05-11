import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Behavior,
    UML2::StateMachine,
    UML2::Interaction,
    Class,
    UML2::Component,
    BehavioralFeature,
    UML2::Operation,
    BehavioredClassifier,
    UML2::Collaboration,
    UML2::Class,
    UML2::BehavioralFeature,
    StateMachine,
    UML2::ProtocolStateMachine,
    UML2::Behavior,
    UML2::BehavioredClassifier,
    UML2::Node,
    UML2::Activity,
    UML2::AssociationClass,
    Node,
    UML2::ExecutionEnvironment,
    UML2::Device,
    UML2::Reception,
    UML2::Stereotype,
    UML2::UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_uml2::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioralFeature)


def test_uml2::behavioralfeature_constructor_exists():
    assert callable(UML2::BehavioralFeature.__init__)


def test_uml2::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2::BehavioralFeature.__init__)
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



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioredClassifier)


def test_uml2::behavioredclassifier_constructor_exists():
    assert callable(UML2::BehavioredClassifier.__init__)


def test_uml2::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
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



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
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
Behavior_strategy = st.builds(
    Behavior,
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
UML2::Component_strategy = st.builds(
    UML2::Component,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
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
UML2::BehavioralFeature_strategy = st.builds(
    UML2::BehavioralFeature,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::Node_strategy = st.builds(
    UML2::Node,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
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
UML2::Reception_strategy = st.builds(
    UML2::Reception,
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)

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

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2::Component_strategy)
@settings(max_examples=50)
def test_uml2::component_instantiation(instance):
    assert isinstance(instance, UML2::Component)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

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

@given(instance=UML2::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2::BehavioralFeature)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

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

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)
