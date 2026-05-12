import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    UML2_ExecutionEnvironment,
    UML2_Device,
    StateMachine,
    UML2_ProtocolStateMachine,
    Behavior,
    UML2_StateMachine,
    UML2_Interaction,
    UML2_Activity,
    Class,
    UML2_Behavior,
    UML2_Class,
    UML2_Reception,
    UML2_Component,
    UML2_Node,
    UML2_Stereotype,
    UML2_AssociationClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutionEnvironment)


def test_uml2_executionenvironment_constructor_exists():
    assert callable(UML2_ExecutionEnvironment.__init__)


def test_uml2_executionenvironment_constructor_args():
    sig = inspect.signature(UML2_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_device_is_not_abstract():
    assert not inspect.isabstract(UML2_Device)


def test_uml2_device_constructor_exists():
    assert callable(UML2_Device.__init__)


def test_uml2_device_constructor_args():
    sig = inspect.signature(UML2_Device.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolStateMachine)


def test_uml2_protocolstatemachine_constructor_exists():
    assert callable(UML2_ProtocolStateMachine.__init__)


def test_uml2_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_StateMachine)


def test_uml2_statemachine_constructor_exists():
    assert callable(UML2_StateMachine.__init__)


def test_uml2_statemachine_constructor_args():
    sig = inspect.signature(UML2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2_Interaction)


def test_uml2_interaction_constructor_exists():
    assert callable(UML2_Interaction.__init__)


def test_uml2_interaction_constructor_args():
    sig = inspect.signature(UML2_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activity_is_not_abstract():
    assert not inspect.isabstract(UML2_Activity)


def test_uml2_activity_constructor_exists():
    assert callable(UML2_Activity.__init__)


def test_uml2_activity_constructor_args():
    sig = inspect.signature(UML2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2_Behavior)


def test_uml2_behavior_constructor_exists():
    assert callable(UML2_Behavior.__init__)


def test_uml2_behavior_constructor_args():
    sig = inspect.signature(UML2_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_class_is_not_abstract():
    assert not inspect.isabstract(UML2_Class)


def test_uml2_class_constructor_exists():
    assert callable(UML2_Class.__init__)


def test_uml2_class_constructor_args():
    sig = inspect.signature(UML2_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml2_class_has_isActive():
    assert hasattr(UML2_Class, "isActive")
    descriptor = None
    for klass in UML2_Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_uml2_reception_is_not_abstract():
    assert not inspect.isabstract(UML2_Reception)


def test_uml2_reception_constructor_exists():
    assert callable(UML2_Reception.__init__)


def test_uml2_reception_constructor_args():
    sig = inspect.signature(UML2_Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2_component_is_not_abstract():
    assert not inspect.isabstract(UML2_Component)


def test_uml2_component_constructor_exists():
    assert callable(UML2_Component.__init__)


def test_uml2_component_constructor_args():
    sig = inspect.signature(UML2_Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2_node_is_not_abstract():
    assert not inspect.isabstract(UML2_Node)


def test_uml2_node_constructor_exists():
    assert callable(UML2_Node.__init__)


def test_uml2_node_constructor_args():
    sig = inspect.signature(UML2_Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2_Stereotype)


def test_uml2_stereotype_constructor_exists():
    assert callable(UML2_Stereotype.__init__)


def test_uml2_stereotype_constructor_args():
    sig = inspect.signature(UML2_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2_AssociationClass)


def test_uml2_associationclass_constructor_exists():
    assert callable(UML2_AssociationClass.__init__)


def test_uml2_associationclass_constructor_args():
    sig = inspect.signature(UML2_AssociationClass.__init__)
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
Node_strategy = st.builds(
    Node,
)
UML2_ExecutionEnvironment_strategy = st.builds(
    UML2_ExecutionEnvironment,
)
UML2_Device_strategy = st.builds(
    UML2_Device,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2_ProtocolStateMachine_strategy = st.builds(
    UML2_ProtocolStateMachine,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2_StateMachine_strategy = st.builds(
    UML2_StateMachine,
)
UML2_Interaction_strategy = st.builds(
    UML2_Interaction,
)
UML2_Activity_strategy = st.builds(
    UML2_Activity,
)
Class_strategy = st.builds(
    Class,
)
UML2_Behavior_strategy = st.builds(
    UML2_Behavior,
)
UML2_Class_strategy = st.builds(
    UML2_Class,
    isActive=
        st.booleans()
)
UML2_Reception_strategy = st.builds(
    UML2_Reception,
)
UML2_Component_strategy = st.builds(
    UML2_Component,
)
UML2_Node_strategy = st.builds(
    UML2_Node,
)
UML2_Stereotype_strategy = st.builds(
    UML2_Stereotype,
)
UML2_AssociationClass_strategy = st.builds(
    UML2_AssociationClass,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2_executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2_ExecutionEnvironment)

@given(instance=UML2_Device_strategy)
@settings(max_examples=50)
def test_uml2_device_instantiation(instance):
    assert isinstance(instance, UML2_Device)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2_statemachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)

@given(instance=UML2_Interaction_strategy)
@settings(max_examples=50)
def test_uml2_interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)

@given(instance=UML2_Activity_strategy)
@settings(max_examples=50)
def test_uml2_activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2_Behavior_strategy)
@settings(max_examples=50)
def test_uml2_behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)

@given(instance=UML2_Class_strategy)
@settings(max_examples=50)
def test_uml2_class_instantiation(instance):
    assert isinstance(instance, UML2_Class)



@given(instance=UML2_Class_strategy)
def test_uml2_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UML2_Reception_strategy)
@settings(max_examples=50)
def test_uml2_reception_instantiation(instance):
    assert isinstance(instance, UML2_Reception)

@given(instance=UML2_Component_strategy)
@settings(max_examples=50)
def test_uml2_component_instantiation(instance):
    assert isinstance(instance, UML2_Component)

@given(instance=UML2_Node_strategy)
@settings(max_examples=50)
def test_uml2_node_instantiation(instance):
    assert isinstance(instance, UML2_Node)

@given(instance=UML2_Stereotype_strategy)
@settings(max_examples=50)
def test_uml2_stereotype_instantiation(instance):
    assert isinstance(instance, UML2_Stereotype)

@given(instance=UML2_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2_associationclass_instantiation(instance):
    assert isinstance(instance, UML2_AssociationClass)
