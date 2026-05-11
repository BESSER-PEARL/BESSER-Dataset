import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProtoLink,
    Component,
    testgramgen1::DerivedComponent,
    testgramgen1::ProtoLink,
    CNamedElement,
    testgramgen1::DerivedLink,
    Node,
    testgramgen1::A,
    testgramgen1::Node,
    testgramgen1::Component,
    testgramgen1::System,
    testgramgen1::B,
    testgramgen1::D,
    testgramgen1::CNamedElement,
    testgramgen1::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_protolink_is_not_abstract():
    assert not inspect.isabstract(ProtoLink)


def test_protolink_constructor_exists():
    assert callable(ProtoLink.__init__)


def test_protolink_constructor_args():
    sig = inspect.signature(ProtoLink.__init__)
    params = list(sig.parameters.keys())



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::derivedcomponent_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::DerivedComponent)


def test_testgramgen1::derivedcomponent_constructor_exists():
    assert callable(testgramgen1::DerivedComponent.__init__)


def test_testgramgen1::derivedcomponent_constructor_args():
    sig = inspect.signature(testgramgen1::DerivedComponent.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::protolink_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::ProtoLink)


def test_testgramgen1::protolink_constructor_exists():
    assert callable(testgramgen1::ProtoLink.__init__)


def test_testgramgen1::protolink_constructor_args():
    sig = inspect.signature(testgramgen1::ProtoLink.__init__)
    params = list(sig.parameters.keys())



def test_cnamedelement_is_not_abstract():
    assert not inspect.isabstract(CNamedElement)


def test_cnamedelement_constructor_exists():
    assert callable(CNamedElement.__init__)


def test_cnamedelement_constructor_args():
    sig = inspect.signature(CNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::derivedlink_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::DerivedLink)


def test_testgramgen1::derivedlink_constructor_exists():
    assert callable(testgramgen1::DerivedLink.__init__)


def test_testgramgen1::derivedlink_constructor_args():
    sig = inspect.signature(testgramgen1::DerivedLink.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::a_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::A)


def test_testgramgen1::a_constructor_exists():
    assert callable(testgramgen1::A.__init__)


def test_testgramgen1::a_constructor_args():
    sig = inspect.signature(testgramgen1::A.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::node_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::Node)


def test_testgramgen1::node_constructor_exists():
    assert callable(testgramgen1::Node.__init__)


def test_testgramgen1::node_constructor_args():
    sig = inspect.signature(testgramgen1::Node.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::component_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::Component)


def test_testgramgen1::component_constructor_exists():
    assert callable(testgramgen1::Component.__init__)


def test_testgramgen1::component_constructor_args():
    sig = inspect.signature(testgramgen1::Component.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::system_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::System)


def test_testgramgen1::system_constructor_exists():
    assert callable(testgramgen1::System.__init__)


def test_testgramgen1::system_constructor_args():
    sig = inspect.signature(testgramgen1::System.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::b_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::B)


def test_testgramgen1::b_constructor_exists():
    assert callable(testgramgen1::B.__init__)


def test_testgramgen1::b_constructor_args():
    sig = inspect.signature(testgramgen1::B.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::d_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::D)


def test_testgramgen1::d_constructor_exists():
    assert callable(testgramgen1::D.__init__)


def test_testgramgen1::d_constructor_args():
    sig = inspect.signature(testgramgen1::D.__init__)
    params = list(sig.parameters.keys())



def test_testgramgen1::cnamedelement_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::CNamedElement)


def test_testgramgen1::cnamedelement_constructor_exists():
    assert callable(testgramgen1::CNamedElement.__init__)


def test_testgramgen1::cnamedelement_constructor_args():
    sig = inspect.signature(testgramgen1::CNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testgramgen1::cnamedelement_has_name():
    assert hasattr(testgramgen1::CNamedElement, "name")
    descriptor = None
    for klass in testgramgen1::CNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testgramgen1::c_is_not_abstract():
    assert not inspect.isabstract(testgramgen1::C)


def test_testgramgen1::c_constructor_exists():
    assert callable(testgramgen1::C.__init__)


def test_testgramgen1::c_constructor_args():
    sig = inspect.signature(testgramgen1::C.__init__)
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
ProtoLink_strategy = st.builds(
    ProtoLink,
)
Component_strategy = st.builds(
    Component,
)
testgramgen1::DerivedComponent_strategy = st.builds(
    testgramgen1::DerivedComponent,
)
testgramgen1::ProtoLink_strategy = st.builds(
    testgramgen1::ProtoLink,
)
CNamedElement_strategy = st.builds(
    CNamedElement,
)
testgramgen1::DerivedLink_strategy = st.builds(
    testgramgen1::DerivedLink,
)
Node_strategy = st.builds(
    Node,
)
testgramgen1::A_strategy = st.builds(
    testgramgen1::A,
)
testgramgen1::Node_strategy = st.builds(
    testgramgen1::Node,
)
testgramgen1::Component_strategy = st.builds(
    testgramgen1::Component,
)
testgramgen1::System_strategy = st.builds(
    testgramgen1::System,
)
testgramgen1::B_strategy = st.builds(
    testgramgen1::B,
)
testgramgen1::D_strategy = st.builds(
    testgramgen1::D,
)
testgramgen1::CNamedElement_strategy = st.builds(
    testgramgen1::CNamedElement,
    name=
        safe_text
)
testgramgen1::C_strategy = st.builds(
    testgramgen1::C,
)

@given(instance=ProtoLink_strategy)
@settings(max_examples=50)
def test_protolink_instantiation(instance):
    assert isinstance(instance, ProtoLink)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=testgramgen1::DerivedComponent_strategy)
@settings(max_examples=50)
def test_testgramgen1::derivedcomponent_instantiation(instance):
    assert isinstance(instance, testgramgen1::DerivedComponent)

@given(instance=testgramgen1::ProtoLink_strategy)
@settings(max_examples=50)
def test_testgramgen1::protolink_instantiation(instance):
    assert isinstance(instance, testgramgen1::ProtoLink)

@given(instance=CNamedElement_strategy)
@settings(max_examples=50)
def test_cnamedelement_instantiation(instance):
    assert isinstance(instance, CNamedElement)

@given(instance=testgramgen1::DerivedLink_strategy)
@settings(max_examples=50)
def test_testgramgen1::derivedlink_instantiation(instance):
    assert isinstance(instance, testgramgen1::DerivedLink)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=testgramgen1::A_strategy)
@settings(max_examples=50)
def test_testgramgen1::a_instantiation(instance):
    assert isinstance(instance, testgramgen1::A)

@given(instance=testgramgen1::Node_strategy)
@settings(max_examples=50)
def test_testgramgen1::node_instantiation(instance):
    assert isinstance(instance, testgramgen1::Node)

@given(instance=testgramgen1::Component_strategy)
@settings(max_examples=50)
def test_testgramgen1::component_instantiation(instance):
    assert isinstance(instance, testgramgen1::Component)

@given(instance=testgramgen1::System_strategy)
@settings(max_examples=50)
def test_testgramgen1::system_instantiation(instance):
    assert isinstance(instance, testgramgen1::System)

@given(instance=testgramgen1::B_strategy)
@settings(max_examples=50)
def test_testgramgen1::b_instantiation(instance):
    assert isinstance(instance, testgramgen1::B)

@given(instance=testgramgen1::D_strategy)
@settings(max_examples=50)
def test_testgramgen1::d_instantiation(instance):
    assert isinstance(instance, testgramgen1::D)

@given(instance=testgramgen1::CNamedElement_strategy)
@settings(max_examples=50)
def test_testgramgen1::cnamedelement_instantiation(instance):
    assert isinstance(instance, testgramgen1::CNamedElement)

@given(instance=testgramgen1::CNamedElement_strategy)
def test_testgramgen1::cnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testgramgen1::CNamedElement_strategy)
def test_testgramgen1::cnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testgramgen1::C_strategy)
@settings(max_examples=50)
def test_testgramgen1::c_instantiation(instance):
    assert isinstance(instance, testgramgen1::C)
