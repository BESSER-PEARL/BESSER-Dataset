import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    qvt_cst_IHasName,
    cst_qvt_EObject,
    IdentifierCS,
    cst_IHasName,
    cst_CSTNode,
    qvt_cst_IdentifierCS,
    qvt_cst_IdentifiedCS,
    qvt_cst_ErrorNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvt_cst_ihasname_is_not_abstract():
    assert not inspect.isabstract(qvt_cst_IHasName)


def test_qvt_cst_ihasname_constructor_exists():
    assert callable(qvt_cst_IHasName.__init__)


def test_qvt_cst_ihasname_constructor_args():
    sig = inspect.signature(qvt_cst_IHasName.__init__)
    params = list(sig.parameters.keys())



def test_cst_qvt_eobject_is_not_abstract():
    assert not inspect.isabstract(cst_qvt_EObject)


def test_cst_qvt_eobject_constructor_exists():
    assert callable(cst_qvt_EObject.__init__)


def test_cst_qvt_eobject_constructor_args():
    sig = inspect.signature(cst_qvt_EObject.__init__)
    params = list(sig.parameters.keys())



def test_identifiercs_is_not_abstract():
    assert not inspect.isabstract(IdentifierCS)


def test_identifiercs_constructor_exists():
    assert callable(IdentifierCS.__init__)


def test_identifiercs_constructor_args():
    sig = inspect.signature(IdentifierCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_ihasname_is_not_abstract():
    assert not inspect.isabstract(cst_IHasName)


def test_cst_ihasname_constructor_exists():
    assert callable(cst_IHasName.__init__)


def test_cst_ihasname_constructor_args():
    sig = inspect.signature(cst_IHasName.__init__)
    params = list(sig.parameters.keys())



def test_cst_cstnode_is_not_abstract():
    assert not inspect.isabstract(cst_CSTNode)


def test_cst_cstnode_constructor_exists():
    assert callable(cst_CSTNode.__init__)


def test_cst_cstnode_constructor_args():
    sig = inspect.signature(cst_CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvt_cst_identifiercs_is_not_abstract():
    assert not inspect.isabstract(qvt_cst_IdentifierCS)


def test_qvt_cst_identifiercs_constructor_exists():
    assert callable(qvt_cst_IdentifierCS.__init__)


def test_qvt_cst_identifiercs_constructor_args():
    sig = inspect.signature(qvt_cst_IdentifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qvt_cst_identifiercs_has_value():
    assert hasattr(qvt_cst_IdentifierCS, "value")
    descriptor = None
    for klass in qvt_cst_IdentifierCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qvt_cst_identifiedcs_is_not_abstract():
    assert not inspect.isabstract(qvt_cst_IdentifiedCS)


def test_qvt_cst_identifiedcs_constructor_exists():
    assert callable(qvt_cst_IdentifiedCS.__init__)


def test_qvt_cst_identifiedcs_constructor_args():
    sig = inspect.signature(qvt_cst_IdentifiedCS.__init__)
    params = list(sig.parameters.keys())



def test_qvt_cst_errornode_is_not_abstract():
    assert not inspect.isabstract(qvt_cst_ErrorNode)


def test_qvt_cst_errornode_constructor_exists():
    assert callable(qvt_cst_ErrorNode.__init__)


def test_qvt_cst_errornode_constructor_args():
    sig = inspect.signature(qvt_cst_ErrorNode.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_qvt_cst_errornode_has_message():
    assert hasattr(qvt_cst_ErrorNode, "message")
    descriptor = None
    for klass in qvt_cst_ErrorNode.__mro__:
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
qvt_cst_IHasName_strategy = st.builds(
    qvt_cst_IHasName,
)
cst_qvt_EObject_strategy = st.builds(
    cst_qvt_EObject,
)
IdentifierCS_strategy = st.builds(
    IdentifierCS,
)
cst_IHasName_strategy = st.builds(
    cst_IHasName,
)
cst_CSTNode_strategy = st.builds(
    cst_CSTNode,
)
qvt_cst_IdentifierCS_strategy = st.builds(
    qvt_cst_IdentifierCS,
    value=
        safe_text
)
qvt_cst_IdentifiedCS_strategy = st.builds(
    qvt_cst_IdentifiedCS,
)
qvt_cst_ErrorNode_strategy = st.builds(
    qvt_cst_ErrorNode,
    message=
        safe_text
)

@given(instance=qvt_cst_IHasName_strategy)
@settings(max_examples=50)
def test_qvt_cst_ihasname_instantiation(instance):
    assert isinstance(instance, qvt_cst_IHasName)

@given(instance=cst_qvt_EObject_strategy)
@settings(max_examples=50)
def test_cst_qvt_eobject_instantiation(instance):
    assert isinstance(instance, cst_qvt_EObject)

@given(instance=IdentifierCS_strategy)
@settings(max_examples=50)
def test_identifiercs_instantiation(instance):
    assert isinstance(instance, IdentifierCS)

@given(instance=cst_IHasName_strategy)
@settings(max_examples=50)
def test_cst_ihasname_instantiation(instance):
    assert isinstance(instance, cst_IHasName)

@given(instance=cst_CSTNode_strategy)
@settings(max_examples=50)
def test_cst_cstnode_instantiation(instance):
    assert isinstance(instance, cst_CSTNode)

@given(instance=qvt_cst_IdentifierCS_strategy)
@settings(max_examples=50)
def test_qvt_cst_identifiercs_instantiation(instance):
    assert isinstance(instance, qvt_cst_IdentifierCS)



@given(instance=qvt_cst_IdentifierCS_strategy)
def test_qvt_cst_identifiercs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=qvt_cst_IdentifiedCS_strategy)
@settings(max_examples=50)
def test_qvt_cst_identifiedcs_instantiation(instance):
    assert isinstance(instance, qvt_cst_IdentifiedCS)

@given(instance=qvt_cst_ErrorNode_strategy)
@settings(max_examples=50)
def test_qvt_cst_errornode_instantiation(instance):
    assert isinstance(instance, qvt_cst_ErrorNode)



@given(instance=qvt_cst_ErrorNode_strategy)
def test_qvt_cst_errornode_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original
