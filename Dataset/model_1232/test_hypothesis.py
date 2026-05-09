import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    qvt::cst::IHasName,
    cst::qvt::EObject,
    IdentifierCS,
    cst::IHasName,
    cst::CSTNode,
    qvt::cst::IdentifierCS,
    qvt::cst::IdentifiedCS,
    qvt::cst::ErrorNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvt::cst::ihasname_is_not_abstract():
    assert not inspect.isabstract(qvt::cst::IHasName)


def test_qvt::cst::ihasname_constructor_exists():
    assert callable(qvt::cst::IHasName.__init__)


def test_qvt::cst::ihasname_constructor_args():
    sig = inspect.signature(qvt::cst::IHasName.__init__)
    params = list(sig.parameters.keys())



def test_cst::qvt::eobject_is_not_abstract():
    assert not inspect.isabstract(cst::qvt::EObject)


def test_cst::qvt::eobject_constructor_exists():
    assert callable(cst::qvt::EObject.__init__)


def test_cst::qvt::eobject_constructor_args():
    sig = inspect.signature(cst::qvt::EObject.__init__)
    params = list(sig.parameters.keys())



def test_identifiercs_is_not_abstract():
    assert not inspect.isabstract(IdentifierCS)


def test_identifiercs_constructor_exists():
    assert callable(IdentifierCS.__init__)


def test_identifiercs_constructor_args():
    sig = inspect.signature(IdentifierCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::ihasname_is_not_abstract():
    assert not inspect.isabstract(cst::IHasName)


def test_cst::ihasname_constructor_exists():
    assert callable(cst::IHasName.__init__)


def test_cst::ihasname_constructor_args():
    sig = inspect.signature(cst::IHasName.__init__)
    params = list(sig.parameters.keys())



def test_cst::cstnode_is_not_abstract():
    assert not inspect.isabstract(cst::CSTNode)


def test_cst::cstnode_constructor_exists():
    assert callable(cst::CSTNode.__init__)


def test_cst::cstnode_constructor_args():
    sig = inspect.signature(cst::CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvt::cst::identifiercs_is_not_abstract():
    assert not inspect.isabstract(qvt::cst::IdentifierCS)


def test_qvt::cst::identifiercs_constructor_exists():
    assert callable(qvt::cst::IdentifierCS.__init__)


def test_qvt::cst::identifiercs_constructor_args():
    sig = inspect.signature(qvt::cst::IdentifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qvt::cst::identifiercs_has_value():
    assert hasattr(qvt::cst::IdentifierCS, "value")
    descriptor = None
    for klass in qvt::cst::IdentifierCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qvt::cst::identifiedcs_is_not_abstract():
    assert not inspect.isabstract(qvt::cst::IdentifiedCS)


def test_qvt::cst::identifiedcs_constructor_exists():
    assert callable(qvt::cst::IdentifiedCS.__init__)


def test_qvt::cst::identifiedcs_constructor_args():
    sig = inspect.signature(qvt::cst::IdentifiedCS.__init__)
    params = list(sig.parameters.keys())



def test_qvt::cst::errornode_is_not_abstract():
    assert not inspect.isabstract(qvt::cst::ErrorNode)


def test_qvt::cst::errornode_constructor_exists():
    assert callable(qvt::cst::ErrorNode.__init__)


def test_qvt::cst::errornode_constructor_args():
    sig = inspect.signature(qvt::cst::ErrorNode.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_qvt::cst::errornode_has_message():
    assert hasattr(qvt::cst::ErrorNode, "message")
    descriptor = None
    for klass in qvt::cst::ErrorNode.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)


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
qvt::cst::IHasName_strategy = st.builds(
    qvt::cst::IHasName,
)
cst::qvt::EObject_strategy = st.builds(
    cst::qvt::EObject,
)
IdentifierCS_strategy = st.builds(
    IdentifierCS,
)
cst::IHasName_strategy = st.builds(
    cst::IHasName,
)
cst::CSTNode_strategy = st.builds(
    cst::CSTNode,
)
qvt::cst::IdentifierCS_strategy = st.builds(
    qvt::cst::IdentifierCS,
    value=
        safe_text
)
qvt::cst::IdentifiedCS_strategy = st.builds(
    qvt::cst::IdentifiedCS,
)
qvt::cst::ErrorNode_strategy = st.builds(
    qvt::cst::ErrorNode,
    message=
        safe_text
)

@given(instance=qvt::cst::IHasName_strategy)
@settings(max_examples=50)
def test_qvt::cst::ihasname_instantiation(instance):
    assert isinstance(instance, qvt::cst::IHasName)

@given(instance=cst::qvt::EObject_strategy)
@settings(max_examples=50)
def test_cst::qvt::eobject_instantiation(instance):
    assert isinstance(instance, cst::qvt::EObject)

@given(instance=IdentifierCS_strategy)
@settings(max_examples=50)
def test_identifiercs_instantiation(instance):
    assert isinstance(instance, IdentifierCS)

@given(instance=cst::IHasName_strategy)
@settings(max_examples=50)
def test_cst::ihasname_instantiation(instance):
    assert isinstance(instance, cst::IHasName)

@given(instance=cst::CSTNode_strategy)
@settings(max_examples=50)
def test_cst::cstnode_instantiation(instance):
    assert isinstance(instance, cst::CSTNode)

@given(instance=qvt::cst::IdentifierCS_strategy)
@settings(max_examples=50)
def test_qvt::cst::identifiercs_instantiation(instance):
    assert isinstance(instance, qvt::cst::IdentifierCS)

@given(instance=qvt::cst::IdentifierCS_strategy)
def test_qvt::cst::identifiercs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=qvt::cst::IdentifierCS_strategy)
def test_qvt::cst::identifiercs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=qvt::cst::IdentifiedCS_strategy)
@settings(max_examples=50)
def test_qvt::cst::identifiedcs_instantiation(instance):
    assert isinstance(instance, qvt::cst::IdentifiedCS)

@given(instance=qvt::cst::ErrorNode_strategy)
@settings(max_examples=50)
def test_qvt::cst::errornode_instantiation(instance):
    assert isinstance(instance, qvt::cst::ErrorNode)

@given(instance=qvt::cst::ErrorNode_strategy)
def test_qvt::cst::errornode_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=qvt::cst::ErrorNode_strategy)
def test_qvt::cst::errornode_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original
