import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    World,
    testcompat103::EClass3,
    EClass0,
    testcompat103::EClass2,
    NamedElement,
    testcompat103::RelatedTo,
    testcompat103::Foo,
    testcompat103::Thing,
    testcompat103::EClass1,
    testcompat103::EClass0,
    testcompat103::World,
    testcompat103::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_world_is_not_abstract():
    assert not inspect.isabstract(World)


def test_world_constructor_exists():
    assert callable(World.__init__)


def test_world_constructor_args():
    sig = inspect.signature(World.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::eclass3_is_not_abstract():
    assert not inspect.isabstract(testcompat103::EClass3)


def test_testcompat103::eclass3_constructor_exists():
    assert callable(testcompat103::EClass3.__init__)


def test_testcompat103::eclass3_constructor_args():
    sig = inspect.signature(testcompat103::EClass3.__init__)
    params = list(sig.parameters.keys())



def test_eclass0_is_not_abstract():
    assert not inspect.isabstract(EClass0)


def test_eclass0_constructor_exists():
    assert callable(EClass0.__init__)


def test_eclass0_constructor_args():
    sig = inspect.signature(EClass0.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::eclass2_is_not_abstract():
    assert not inspect.isabstract(testcompat103::EClass2)


def test_testcompat103::eclass2_constructor_exists():
    assert callable(testcompat103::EClass2.__init__)


def test_testcompat103::eclass2_constructor_args():
    sig = inspect.signature(testcompat103::EClass2.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::relatedto_is_not_abstract():
    assert not inspect.isabstract(testcompat103::RelatedTo)


def test_testcompat103::relatedto_constructor_exists():
    assert callable(testcompat103::RelatedTo.__init__)


def test_testcompat103::relatedto_constructor_args():
    sig = inspect.signature(testcompat103::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_testcompat103::relatedto_has_since():
    assert hasattr(testcompat103::RelatedTo, "since")
    descriptor = None
    for klass in testcompat103::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_testcompat103::foo_is_not_abstract():
    assert not inspect.isabstract(testcompat103::Foo)


def test_testcompat103::foo_constructor_exists():
    assert callable(testcompat103::Foo.__init__)


def test_testcompat103::foo_constructor_args():
    sig = inspect.signature(testcompat103::Foo.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::thing_is_not_abstract():
    assert not inspect.isabstract(testcompat103::Thing)


def test_testcompat103::thing_constructor_exists():
    assert callable(testcompat103::Thing.__init__)


def test_testcompat103::thing_constructor_args():
    sig = inspect.signature(testcompat103::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_testcompat103::thing_has_id():
    assert hasattr(testcompat103::Thing, "id")
    descriptor = None
    for klass in testcompat103::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_testcompat103::eclass1_is_not_abstract():
    assert not inspect.isabstract(testcompat103::EClass1)


def test_testcompat103::eclass1_constructor_exists():
    assert callable(testcompat103::EClass1.__init__)


def test_testcompat103::eclass1_constructor_args():
    sig = inspect.signature(testcompat103::EClass1.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::eclass0_is_not_abstract():
    assert not inspect.isabstract(testcompat103::EClass0)


def test_testcompat103::eclass0_constructor_exists():
    assert callable(testcompat103::EClass0.__init__)


def test_testcompat103::eclass0_constructor_args():
    sig = inspect.signature(testcompat103::EClass0.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::world_is_not_abstract():
    assert not inspect.isabstract(testcompat103::World)


def test_testcompat103::world_constructor_exists():
    assert callable(testcompat103::World.__init__)


def test_testcompat103::world_constructor_args():
    sig = inspect.signature(testcompat103::World.__init__)
    params = list(sig.parameters.keys())



def test_testcompat103::namedelement_is_not_abstract():
    assert not inspect.isabstract(testcompat103::NamedElement)


def test_testcompat103::namedelement_constructor_exists():
    assert callable(testcompat103::NamedElement.__init__)


def test_testcompat103::namedelement_constructor_args():
    sig = inspect.signature(testcompat103::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testcompat103::namedelement_has_name():
    assert hasattr(testcompat103::NamedElement, "name")
    descriptor = None
    for klass in testcompat103::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
World_strategy = st.builds(
    World,
)
testcompat103::EClass3_strategy = st.builds(
    testcompat103::EClass3,
)
EClass0_strategy = st.builds(
    EClass0,
)
testcompat103::EClass2_strategy = st.builds(
    testcompat103::EClass2,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
testcompat103::RelatedTo_strategy = st.builds(
    testcompat103::RelatedTo,
    since=
        safe_text
)
testcompat103::Foo_strategy = st.builds(
    testcompat103::Foo,
)
testcompat103::Thing_strategy = st.builds(
    testcompat103::Thing,
    id=
        st.integers()
)
testcompat103::EClass1_strategy = st.builds(
    testcompat103::EClass1,
)
testcompat103::EClass0_strategy = st.builds(
    testcompat103::EClass0,
)
testcompat103::World_strategy = st.builds(
    testcompat103::World,
)
testcompat103::NamedElement_strategy = st.builds(
    testcompat103::NamedElement,
    name=
        safe_text
)

@given(instance=World_strategy)
@settings(max_examples=50)
def test_world_instantiation(instance):
    assert isinstance(instance, World)

@given(instance=testcompat103::EClass3_strategy)
@settings(max_examples=50)
def test_testcompat103::eclass3_instantiation(instance):
    assert isinstance(instance, testcompat103::EClass3)

@given(instance=EClass0_strategy)
@settings(max_examples=50)
def test_eclass0_instantiation(instance):
    assert isinstance(instance, EClass0)

@given(instance=testcompat103::EClass2_strategy)
@settings(max_examples=50)
def test_testcompat103::eclass2_instantiation(instance):
    assert isinstance(instance, testcompat103::EClass2)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=testcompat103::RelatedTo_strategy)
@settings(max_examples=50)
def test_testcompat103::relatedto_instantiation(instance):
    assert isinstance(instance, testcompat103::RelatedTo)

@given(instance=testcompat103::RelatedTo_strategy)
def test_testcompat103::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=testcompat103::RelatedTo_strategy)
def test_testcompat103::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=testcompat103::Foo_strategy)
@settings(max_examples=50)
def test_testcompat103::foo_instantiation(instance):
    assert isinstance(instance, testcompat103::Foo)

@given(instance=testcompat103::Thing_strategy)
@settings(max_examples=50)
def test_testcompat103::thing_instantiation(instance):
    assert isinstance(instance, testcompat103::Thing)

@given(instance=testcompat103::Thing_strategy)
def test_testcompat103::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=testcompat103::Thing_strategy)
def test_testcompat103::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=testcompat103::EClass1_strategy)
@settings(max_examples=50)
def test_testcompat103::eclass1_instantiation(instance):
    assert isinstance(instance, testcompat103::EClass1)

@given(instance=testcompat103::EClass0_strategy)
@settings(max_examples=50)
def test_testcompat103::eclass0_instantiation(instance):
    assert isinstance(instance, testcompat103::EClass0)

@given(instance=testcompat103::World_strategy)
@settings(max_examples=50)
def test_testcompat103::world_instantiation(instance):
    assert isinstance(instance, testcompat103::World)

@given(instance=testcompat103::NamedElement_strategy)
@settings(max_examples=50)
def test_testcompat103::namedelement_instantiation(instance):
    assert isinstance(instance, testcompat103::NamedElement)

@given(instance=testcompat103::NamedElement_strategy)
def test_testcompat103::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testcompat103::NamedElement_strategy)
def test_testcompat103::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
