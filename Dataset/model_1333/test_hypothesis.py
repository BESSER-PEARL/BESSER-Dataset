import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElementCS,
    classescs::PackageCS,
    ElementCS,
    classescs::RootCS,
    classescs::NamedElementCS,
    classescs::Element,
    classescs::ElementCS,
    classescs::PathElementCS,
    classescs::PathNameCS,
    classescs::ClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::packagecs_is_not_abstract():
    assert not inspect.isabstract(classescs::PackageCS)


def test_classescs::packagecs_constructor_exists():
    assert callable(classescs::PackageCS.__init__)


def test_classescs::packagecs_constructor_args():
    sig = inspect.signature(classescs::PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::rootcs_is_not_abstract():
    assert not inspect.isabstract(classescs::RootCS)


def test_classescs::rootcs_constructor_exists():
    assert callable(classescs::RootCS.__init__)


def test_classescs::rootcs_constructor_args():
    sig = inspect.signature(classescs::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::namedelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs::NamedElementCS)


def test_classescs::namedelementcs_constructor_exists():
    assert callable(classescs::NamedElementCS.__init__)


def test_classescs::namedelementcs_constructor_args():
    sig = inspect.signature(classescs::NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classescs::namedelementcs_has_name():
    assert hasattr(classescs::NamedElementCS, "name")
    descriptor = None
    for klass in classescs::NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classescs::element_is_not_abstract():
    assert not inspect.isabstract(classescs::Element)


def test_classescs::element_constructor_exists():
    assert callable(classescs::Element.__init__)


def test_classescs::element_constructor_args():
    sig = inspect.signature(classescs::Element.__init__)
    params = list(sig.parameters.keys())



def test_classescs::elementcs_is_not_abstract():
    assert not inspect.isabstract(classescs::ElementCS)


def test_classescs::elementcs_constructor_exists():
    assert callable(classescs::ElementCS.__init__)


def test_classescs::elementcs_constructor_args():
    sig = inspect.signature(classescs::ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs::PathElementCS)


def test_classescs::pathelementcs_constructor_exists():
    assert callable(classescs::PathElementCS.__init__)


def test_classescs::pathelementcs_constructor_args():
    sig = inspect.signature(classescs::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(classescs::PathNameCS)


def test_classescs::pathnamecs_constructor_exists():
    assert callable(classescs::PathNameCS.__init__)


def test_classescs::pathnamecs_constructor_args():
    sig = inspect.signature(classescs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::classcs_is_not_abstract():
    assert not inspect.isabstract(classescs::ClassCS)


def test_classescs::classcs_constructor_exists():
    assert callable(classescs::ClassCS.__init__)


def test_classescs::classcs_constructor_args():
    sig = inspect.signature(classescs::ClassCS.__init__)
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
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
classescs::PackageCS_strategy = st.builds(
    classescs::PackageCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
classescs::RootCS_strategy = st.builds(
    classescs::RootCS,
)
classescs::NamedElementCS_strategy = st.builds(
    classescs::NamedElementCS,
    name=
        safe_text
)
classescs::Element_strategy = st.builds(
    classescs::Element,
)
classescs::ElementCS_strategy = st.builds(
    classescs::ElementCS,
)
classescs::PathElementCS_strategy = st.builds(
    classescs::PathElementCS,
)
classescs::PathNameCS_strategy = st.builds(
    classescs::PathNameCS,
)
classescs::ClassCS_strategy = st.builds(
    classescs::ClassCS,
)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=classescs::PackageCS_strategy)
@settings(max_examples=50)
def test_classescs::packagecs_instantiation(instance):
    assert isinstance(instance, classescs::PackageCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=classescs::RootCS_strategy)
@settings(max_examples=50)
def test_classescs::rootcs_instantiation(instance):
    assert isinstance(instance, classescs::RootCS)

@given(instance=classescs::NamedElementCS_strategy)
@settings(max_examples=50)
def test_classescs::namedelementcs_instantiation(instance):
    assert isinstance(instance, classescs::NamedElementCS)

@given(instance=classescs::NamedElementCS_strategy)
def test_classescs::namedelementcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classescs::NamedElementCS_strategy)
def test_classescs::namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classescs::Element_strategy)
@settings(max_examples=50)
def test_classescs::element_instantiation(instance):
    assert isinstance(instance, classescs::Element)

@given(instance=classescs::ElementCS_strategy)
@settings(max_examples=50)
def test_classescs::elementcs_instantiation(instance):
    assert isinstance(instance, classescs::ElementCS)

@given(instance=classescs::PathElementCS_strategy)
@settings(max_examples=50)
def test_classescs::pathelementcs_instantiation(instance):
    assert isinstance(instance, classescs::PathElementCS)

@given(instance=classescs::PathNameCS_strategy)
@settings(max_examples=50)
def test_classescs::pathnamecs_instantiation(instance):
    assert isinstance(instance, classescs::PathNameCS)

@given(instance=classescs::ClassCS_strategy)
@settings(max_examples=50)
def test_classescs::classcs_instantiation(instance):
    assert isinstance(instance, classescs::ClassCS)
