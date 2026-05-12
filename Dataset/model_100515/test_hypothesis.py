import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rqsDsl_RAnnotation,
    rqsDsl_EObject,
    rqsDsl_Requirement,
    rqsDsl_TAnnotation,
    rqsDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rqsdsl_rannotation_is_not_abstract():
    assert not inspect.isabstract(rqsDsl_RAnnotation)


def test_rqsdsl_rannotation_constructor_exists():
    assert callable(rqsDsl_RAnnotation.__init__)


def test_rqsdsl_rannotation_constructor_args():
    sig = inspect.signature(rqsDsl_RAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "ab" in params, "Missing parameter 'ab'"
    assert "id" in params, "Missing parameter 'id'"
    assert "ba" in params, "Missing parameter 'ba'"
    assert "aa" in params, "Missing parameter 'aa'"
    assert "bb" in params, "Missing parameter 'bb'"
    assert "num" in params, "Missing parameter 'num'"
    assert "type" in params, "Missing parameter 'type'"

def test_rqsdsl_rannotation_has_ab():
    assert hasattr(rqsDsl_RAnnotation, "ab")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "ab" in klass.__dict__:
            descriptor = klass.__dict__["ab"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_id():
    assert hasattr(rqsDsl_RAnnotation, "id")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_ba():
    assert hasattr(rqsDsl_RAnnotation, "ba")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "ba" in klass.__dict__:
            descriptor = klass.__dict__["ba"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_aa():
    assert hasattr(rqsDsl_RAnnotation, "aa")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "aa" in klass.__dict__:
            descriptor = klass.__dict__["aa"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_bb():
    assert hasattr(rqsDsl_RAnnotation, "bb")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "bb" in klass.__dict__:
            descriptor = klass.__dict__["bb"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_num():
    assert hasattr(rqsDsl_RAnnotation, "num")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_rannotation_has_type():
    assert hasattr(rqsDsl_RAnnotation, "type")
    descriptor = None
    for klass in rqsDsl_RAnnotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl_eobject_is_not_abstract():
    assert not inspect.isabstract(rqsDsl_EObject)


def test_rqsdsl_eobject_constructor_exists():
    assert callable(rqsDsl_EObject.__init__)


def test_rqsdsl_eobject_constructor_args():
    sig = inspect.signature(rqsDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_rqsdsl_requirement_is_not_abstract():
    assert not inspect.isabstract(rqsDsl_Requirement)


def test_rqsdsl_requirement_constructor_exists():
    assert callable(rqsDsl_Requirement.__init__)


def test_rqsdsl_requirement_constructor_args():
    sig = inspect.signature(rqsDsl_Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_rqsdsl_requirement_has_text():
    assert hasattr(rqsDsl_Requirement, "text")
    descriptor = None
    for klass in rqsDsl_Requirement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl_tannotation_is_not_abstract():
    assert not inspect.isabstract(rqsDsl_TAnnotation)


def test_rqsdsl_tannotation_constructor_exists():
    assert callable(rqsDsl_TAnnotation.__init__)


def test_rqsdsl_tannotation_constructor_args():
    sig = inspect.signature(rqsDsl_TAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "b" in params, "Missing parameter 'b'"
    assert "id" in params, "Missing parameter 'id'"
    assert "a" in params, "Missing parameter 'a'"
    assert "type" in params, "Missing parameter 'type'"
    assert "text" in params, "Missing parameter 'text'"

def test_rqsdsl_tannotation_has_num():
    assert hasattr(rqsDsl_TAnnotation, "num")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_tannotation_has_b():
    assert hasattr(rqsDsl_TAnnotation, "b")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_tannotation_has_id():
    assert hasattr(rqsDsl_TAnnotation, "id")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_tannotation_has_a():
    assert hasattr(rqsDsl_TAnnotation, "a")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_tannotation_has_type():
    assert hasattr(rqsDsl_TAnnotation, "type")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl_tannotation_has_text():
    assert hasattr(rqsDsl_TAnnotation, "text")
    descriptor = None
    for klass in rqsDsl_TAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl_model_is_not_abstract():
    assert not inspect.isabstract(rqsDsl_Model)


def test_rqsdsl_model_constructor_exists():
    assert callable(rqsDsl_Model.__init__)


def test_rqsdsl_model_constructor_args():
    sig = inspect.signature(rqsDsl_Model.__init__)
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
rqsDsl_RAnnotation_strategy = st.builds(
    rqsDsl_RAnnotation,
    ab=
        st.integers(),
    id=
        st.integers(),
    ba=
        st.integers(),
    aa=
        st.integers(),
    bb=
        st.integers(),
    num=
        st.integers(),
    type=
        safe_text
)
rqsDsl_EObject_strategy = st.builds(
    rqsDsl_EObject,
)
rqsDsl_Requirement_strategy = st.builds(
    rqsDsl_Requirement,
    text=
        safe_text
)
rqsDsl_TAnnotation_strategy = st.builds(
    rqsDsl_TAnnotation,
    num=
        st.integers(),
    b=
        st.integers(),
    id=
        st.integers(),
    a=
        st.integers(),
    type=
        safe_text,
    text=
        safe_text
)
rqsDsl_Model_strategy = st.builds(
    rqsDsl_Model,
)

@given(instance=rqsDsl_RAnnotation_strategy)
@settings(max_examples=50)
def test_rqsdsl_rannotation_instantiation(instance):
    assert isinstance(instance, rqsDsl_RAnnotation)



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_ab_setter(instance):
    original = instance.ab
    instance.ab = original
    assert instance.ab == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_ba_setter(instance):
    original = instance.ba
    instance.ba = original
    assert instance.ba == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_aa_setter(instance):
    original = instance.aa
    instance.aa = original
    assert instance.aa == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_bb_setter(instance):
    original = instance.bb
    instance.bb = original
    assert instance.bb == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=rqsDsl_RAnnotation_strategy)
def test_rqsdsl_rannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rqsDsl_EObject_strategy)
@settings(max_examples=50)
def test_rqsdsl_eobject_instantiation(instance):
    assert isinstance(instance, rqsDsl_EObject)

@given(instance=rqsDsl_Requirement_strategy)
@settings(max_examples=50)
def test_rqsdsl_requirement_instantiation(instance):
    assert isinstance(instance, rqsDsl_Requirement)



@given(instance=rqsDsl_Requirement_strategy)
def test_rqsdsl_requirement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rqsDsl_TAnnotation_strategy)
@settings(max_examples=50)
def test_rqsdsl_tannotation_instantiation(instance):
    assert isinstance(instance, rqsDsl_TAnnotation)



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rqsDsl_TAnnotation_strategy)
def test_rqsdsl_tannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rqsDsl_Model_strategy)
@settings(max_examples=50)
def test_rqsdsl_model_instantiation(instance):
    assert isinstance(instance, rqsDsl_Model)
