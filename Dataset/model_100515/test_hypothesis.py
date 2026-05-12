import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rqsDsl::RAnnotation,
    rqsDsl::EObject,
    rqsDsl::Requirement,
    rqsDsl::TAnnotation,
    rqsDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rqsdsl::rannotation_is_not_abstract():
    assert not inspect.isabstract(rqsDsl::RAnnotation)


def test_rqsdsl::rannotation_constructor_exists():
    assert callable(rqsDsl::RAnnotation.__init__)


def test_rqsdsl::rannotation_constructor_args():
    sig = inspect.signature(rqsDsl::RAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "ba" in params, "Missing parameter 'ba'"
    assert "id" in params, "Missing parameter 'id'"
    assert "ab" in params, "Missing parameter 'ab'"
    assert "type" in params, "Missing parameter 'type'"
    assert "bb" in params, "Missing parameter 'bb'"
    assert "aa" in params, "Missing parameter 'aa'"
    assert "num" in params, "Missing parameter 'num'"

def test_rqsdsl::rannotation_has_ba():
    assert hasattr(rqsDsl::RAnnotation, "ba")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "ba" in klass.__dict__:
            descriptor = klass.__dict__["ba"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_id():
    assert hasattr(rqsDsl::RAnnotation, "id")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_ab():
    assert hasattr(rqsDsl::RAnnotation, "ab")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "ab" in klass.__dict__:
            descriptor = klass.__dict__["ab"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_type():
    assert hasattr(rqsDsl::RAnnotation, "type")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_bb():
    assert hasattr(rqsDsl::RAnnotation, "bb")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "bb" in klass.__dict__:
            descriptor = klass.__dict__["bb"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_aa():
    assert hasattr(rqsDsl::RAnnotation, "aa")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "aa" in klass.__dict__:
            descriptor = klass.__dict__["aa"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::rannotation_has_num():
    assert hasattr(rqsDsl::RAnnotation, "num")
    descriptor = None
    for klass in rqsDsl::RAnnotation.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl::eobject_is_not_abstract():
    assert not inspect.isabstract(rqsDsl::EObject)


def test_rqsdsl::eobject_constructor_exists():
    assert callable(rqsDsl::EObject.__init__)


def test_rqsdsl::eobject_constructor_args():
    sig = inspect.signature(rqsDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_rqsdsl::requirement_is_not_abstract():
    assert not inspect.isabstract(rqsDsl::Requirement)


def test_rqsdsl::requirement_constructor_exists():
    assert callable(rqsDsl::Requirement.__init__)


def test_rqsdsl::requirement_constructor_args():
    sig = inspect.signature(rqsDsl::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_rqsdsl::requirement_has_text():
    assert hasattr(rqsDsl::Requirement, "text")
    descriptor = None
    for klass in rqsDsl::Requirement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl::tannotation_is_not_abstract():
    assert not inspect.isabstract(rqsDsl::TAnnotation)


def test_rqsdsl::tannotation_constructor_exists():
    assert callable(rqsDsl::TAnnotation.__init__)


def test_rqsdsl::tannotation_constructor_args():
    sig = inspect.signature(rqsDsl::TAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "num" in params, "Missing parameter 'num'"
    assert "text" in params, "Missing parameter 'text'"
    assert "b" in params, "Missing parameter 'b'"

def test_rqsdsl::tannotation_has_a():
    assert hasattr(rqsDsl::TAnnotation, "a")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::tannotation_has_type():
    assert hasattr(rqsDsl::TAnnotation, "type")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::tannotation_has_id():
    assert hasattr(rqsDsl::TAnnotation, "id")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::tannotation_has_num():
    assert hasattr(rqsDsl::TAnnotation, "num")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::tannotation_has_text():
    assert hasattr(rqsDsl::TAnnotation, "text")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_rqsdsl::tannotation_has_b():
    assert hasattr(rqsDsl::TAnnotation, "b")
    descriptor = None
    for klass in rqsDsl::TAnnotation.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_rqsdsl::model_is_not_abstract():
    assert not inspect.isabstract(rqsDsl::Model)


def test_rqsdsl::model_constructor_exists():
    assert callable(rqsDsl::Model.__init__)


def test_rqsdsl::model_constructor_args():
    sig = inspect.signature(rqsDsl::Model.__init__)
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
rqsDsl::RAnnotation_strategy = st.builds(
    rqsDsl::RAnnotation,
    ba=
        st.integers(),
    id=
        st.integers(),
    ab=
        st.integers(),
    type=
        safe_text,
    bb=
        st.integers(),
    aa=
        st.integers(),
    num=
        st.integers()
)
rqsDsl::EObject_strategy = st.builds(
    rqsDsl::EObject,
)
rqsDsl::Requirement_strategy = st.builds(
    rqsDsl::Requirement,
    text=
        safe_text
)
rqsDsl::TAnnotation_strategy = st.builds(
    rqsDsl::TAnnotation,
    a=
        st.integers(),
    type=
        safe_text,
    id=
        st.integers(),
    num=
        st.integers(),
    text=
        safe_text,
    b=
        st.integers()
)
rqsDsl::Model_strategy = st.builds(
    rqsDsl::Model,
)

@given(instance=rqsDsl::RAnnotation_strategy)
@settings(max_examples=50)
def test_rqsdsl::rannotation_instantiation(instance):
    assert isinstance(instance, rqsDsl::RAnnotation)

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_ba_type(instance):
    assert isinstance(instance.ba, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_ba_setter(instance):
    original = instance.ba
    instance.ba = original
    assert instance.ba == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_ab_type(instance):
    assert isinstance(instance.ab, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_ab_setter(instance):
    original = instance.ab
    instance.ab = original
    assert instance.ab == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_bb_type(instance):
    assert isinstance(instance.bb, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_bb_setter(instance):
    original = instance.bb
    instance.bb = original
    assert instance.bb == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_aa_type(instance):
    assert isinstance(instance.aa, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_aa_setter(instance):
    original = instance.aa
    instance.aa = original
    assert instance.aa == original

@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=rqsDsl::RAnnotation_strategy)
def test_rqsdsl::rannotation_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=rqsDsl::EObject_strategy)
@settings(max_examples=50)
def test_rqsdsl::eobject_instantiation(instance):
    assert isinstance(instance, rqsDsl::EObject)

@given(instance=rqsDsl::Requirement_strategy)
@settings(max_examples=50)
def test_rqsdsl::requirement_instantiation(instance):
    assert isinstance(instance, rqsDsl::Requirement)

@given(instance=rqsDsl::Requirement_strategy)
def test_rqsdsl::requirement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=rqsDsl::Requirement_strategy)
def test_rqsdsl::requirement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rqsDsl::TAnnotation_strategy)
@settings(max_examples=50)
def test_rqsdsl::tannotation_instantiation(instance):
    assert isinstance(instance, rqsDsl::TAnnotation)

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=rqsDsl::TAnnotation_strategy)
def test_rqsdsl::tannotation_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=rqsDsl::Model_strategy)
@settings(max_examples=50)
def test_rqsdsl::model_instantiation(instance):
    assert isinstance(instance, rqsDsl::Model)
