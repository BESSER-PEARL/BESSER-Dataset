import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElementCS,
    classescs::PathElementCS,
    classescs::PropertyCS,
    classescs::ClassCS,
    classescs::OperationCS,
    classescs::PackageCS,
    classescs::ArgumentCS,
    classescs::ElementCS,
    ElementCS,
    classescs::RoundedBracketClause,
    classescs::RootCS,
    classescs::PathNameCS,
    classescs::NameExpCS,
    classescs::NamedElementCS,
    classescs::EObject,
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



def test_classescs::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs::PathElementCS)


def test_classescs::pathelementcs_constructor_exists():
    assert callable(classescs::PathElementCS.__init__)


def test_classescs::pathelementcs_constructor_args():
    sig = inspect.signature(classescs::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::propertycs_is_not_abstract():
    assert not inspect.isabstract(classescs::PropertyCS)


def test_classescs::propertycs_constructor_exists():
    assert callable(classescs::PropertyCS.__init__)


def test_classescs::propertycs_constructor_args():
    sig = inspect.signature(classescs::PropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::classcs_is_not_abstract():
    assert not inspect.isabstract(classescs::ClassCS)


def test_classescs::classcs_constructor_exists():
    assert callable(classescs::ClassCS.__init__)


def test_classescs::classcs_constructor_args():
    sig = inspect.signature(classescs::ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::operationcs_is_not_abstract():
    assert not inspect.isabstract(classescs::OperationCS)


def test_classescs::operationcs_constructor_exists():
    assert callable(classescs::OperationCS.__init__)


def test_classescs::operationcs_constructor_args():
    sig = inspect.signature(classescs::OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_classescs::operationcs_has_params():
    assert hasattr(classescs::OperationCS, "params")
    descriptor = None
    for klass in classescs::OperationCS.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_classescs::packagecs_is_not_abstract():
    assert not inspect.isabstract(classescs::PackageCS)


def test_classescs::packagecs_constructor_exists():
    assert callable(classescs::PackageCS.__init__)


def test_classescs::packagecs_constructor_args():
    sig = inspect.signature(classescs::PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::argumentcs_is_not_abstract():
    assert not inspect.isabstract(classescs::ArgumentCS)


def test_classescs::argumentcs_constructor_exists():
    assert callable(classescs::ArgumentCS.__init__)


def test_classescs::argumentcs_constructor_args():
    sig = inspect.signature(classescs::ArgumentCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::elementcs_is_not_abstract():
    assert not inspect.isabstract(classescs::ElementCS)


def test_classescs::elementcs_constructor_exists():
    assert callable(classescs::ElementCS.__init__)


def test_classescs::elementcs_constructor_args():
    sig = inspect.signature(classescs::ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::roundedbracketclause_is_not_abstract():
    assert not inspect.isabstract(classescs::RoundedBracketClause)


def test_classescs::roundedbracketclause_constructor_exists():
    assert callable(classescs::RoundedBracketClause.__init__)


def test_classescs::roundedbracketclause_constructor_args():
    sig = inspect.signature(classescs::RoundedBracketClause.__init__)
    params = list(sig.parameters.keys())



def test_classescs::rootcs_is_not_abstract():
    assert not inspect.isabstract(classescs::RootCS)


def test_classescs::rootcs_constructor_exists():
    assert callable(classescs::RootCS.__init__)


def test_classescs::rootcs_constructor_args():
    sig = inspect.signature(classescs::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(classescs::PathNameCS)


def test_classescs::pathnamecs_constructor_exists():
    assert callable(classescs::PathNameCS.__init__)


def test_classescs::pathnamecs_constructor_args():
    sig = inspect.signature(classescs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(classescs::NameExpCS)


def test_classescs::nameexpcs_constructor_exists():
    assert callable(classescs::NameExpCS.__init__)


def test_classescs::nameexpcs_constructor_args():
    sig = inspect.signature(classescs::NameExpCS.__init__)
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



def test_classescs::eobject_is_not_abstract():
    assert not inspect.isabstract(classescs::EObject)


def test_classescs::eobject_constructor_exists():
    assert callable(classescs::EObject.__init__)


def test_classescs::eobject_constructor_args():
    sig = inspect.signature(classescs::EObject.__init__)
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
classescs::PathElementCS_strategy = st.builds(
    classescs::PathElementCS,
)
classescs::PropertyCS_strategy = st.builds(
    classescs::PropertyCS,
)
classescs::ClassCS_strategy = st.builds(
    classescs::ClassCS,
)
classescs::OperationCS_strategy = st.builds(
    classescs::OperationCS,
    params=
        safe_text
)
classescs::PackageCS_strategy = st.builds(
    classescs::PackageCS,
)
classescs::ArgumentCS_strategy = st.builds(
    classescs::ArgumentCS,
)
classescs::ElementCS_strategy = st.builds(
    classescs::ElementCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
classescs::RoundedBracketClause_strategy = st.builds(
    classescs::RoundedBracketClause,
)
classescs::RootCS_strategy = st.builds(
    classescs::RootCS,
)
classescs::PathNameCS_strategy = st.builds(
    classescs::PathNameCS,
)
classescs::NameExpCS_strategy = st.builds(
    classescs::NameExpCS,
)
classescs::NamedElementCS_strategy = st.builds(
    classescs::NamedElementCS,
    name=
        safe_text
)
classescs::EObject_strategy = st.builds(
    classescs::EObject,
)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=classescs::PathElementCS_strategy)
@settings(max_examples=50)
def test_classescs::pathelementcs_instantiation(instance):
    assert isinstance(instance, classescs::PathElementCS)

@given(instance=classescs::PropertyCS_strategy)
@settings(max_examples=50)
def test_classescs::propertycs_instantiation(instance):
    assert isinstance(instance, classescs::PropertyCS)

@given(instance=classescs::ClassCS_strategy)
@settings(max_examples=50)
def test_classescs::classcs_instantiation(instance):
    assert isinstance(instance, classescs::ClassCS)

@given(instance=classescs::OperationCS_strategy)
@settings(max_examples=50)
def test_classescs::operationcs_instantiation(instance):
    assert isinstance(instance, classescs::OperationCS)

@given(instance=classescs::OperationCS_strategy)
def test_classescs::operationcs_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=classescs::OperationCS_strategy)
def test_classescs::operationcs_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=classescs::PackageCS_strategy)
@settings(max_examples=50)
def test_classescs::packagecs_instantiation(instance):
    assert isinstance(instance, classescs::PackageCS)

@given(instance=classescs::ArgumentCS_strategy)
@settings(max_examples=50)
def test_classescs::argumentcs_instantiation(instance):
    assert isinstance(instance, classescs::ArgumentCS)

@given(instance=classescs::ElementCS_strategy)
@settings(max_examples=50)
def test_classescs::elementcs_instantiation(instance):
    assert isinstance(instance, classescs::ElementCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=classescs::RoundedBracketClause_strategy)
@settings(max_examples=50)
def test_classescs::roundedbracketclause_instantiation(instance):
    assert isinstance(instance, classescs::RoundedBracketClause)

@given(instance=classescs::RootCS_strategy)
@settings(max_examples=50)
def test_classescs::rootcs_instantiation(instance):
    assert isinstance(instance, classescs::RootCS)

@given(instance=classescs::PathNameCS_strategy)
@settings(max_examples=50)
def test_classescs::pathnamecs_instantiation(instance):
    assert isinstance(instance, classescs::PathNameCS)

@given(instance=classescs::NameExpCS_strategy)
@settings(max_examples=50)
def test_classescs::nameexpcs_instantiation(instance):
    assert isinstance(instance, classescs::NameExpCS)

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

@given(instance=classescs::EObject_strategy)
@settings(max_examples=50)
def test_classescs::eobject_instantiation(instance):
    assert isinstance(instance, classescs::EObject)
