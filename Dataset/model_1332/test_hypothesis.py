import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElementCS,
    classescs_OperationCS,
    classescs_PathElementCS,
    classescs_ClassCS,
    classescs_PropertyCS,
    classescs_PackageCS,
    classescs_ArgumentCS,
    classescs_ElementCS,
    ElementCS,
    classescs_NameExpCS,
    classescs_RootCS,
    classescs_RoundedBracketClause,
    classescs_PathNameCS,
    classescs_NamedElementCS,
    classescs_EObject,
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



def test_classescs_operationcs_is_not_abstract():
    assert not inspect.isabstract(classescs_OperationCS)


def test_classescs_operationcs_constructor_exists():
    assert callable(classescs_OperationCS.__init__)


def test_classescs_operationcs_constructor_args():
    sig = inspect.signature(classescs_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_classescs_operationcs_has_params():
    assert hasattr(classescs_OperationCS, "params")
    descriptor = None
    for klass in classescs_OperationCS.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_classescs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathElementCS)


def test_classescs_pathelementcs_constructor_exists():
    assert callable(classescs_PathElementCS.__init__)


def test_classescs_pathelementcs_constructor_args():
    sig = inspect.signature(classescs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_classcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ClassCS)


def test_classescs_classcs_constructor_exists():
    assert callable(classescs_ClassCS.__init__)


def test_classescs_classcs_constructor_args():
    sig = inspect.signature(classescs_ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_propertycs_is_not_abstract():
    assert not inspect.isabstract(classescs_PropertyCS)


def test_classescs_propertycs_constructor_exists():
    assert callable(classescs_PropertyCS.__init__)


def test_classescs_propertycs_constructor_args():
    sig = inspect.signature(classescs_PropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_packagecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PackageCS)


def test_classescs_packagecs_constructor_exists():
    assert callable(classescs_PackageCS.__init__)


def test_classescs_packagecs_constructor_args():
    sig = inspect.signature(classescs_PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_argumentcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ArgumentCS)


def test_classescs_argumentcs_constructor_exists():
    assert callable(classescs_ArgumentCS.__init__)


def test_classescs_argumentcs_constructor_args():
    sig = inspect.signature(classescs_ArgumentCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_elementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ElementCS)


def test_classescs_elementcs_constructor_exists():
    assert callable(classescs_ElementCS.__init__)


def test_classescs_elementcs_constructor_args():
    sig = inspect.signature(classescs_ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(classescs_NameExpCS)


def test_classescs_nameexpcs_constructor_exists():
    assert callable(classescs_NameExpCS.__init__)


def test_classescs_nameexpcs_constructor_args():
    sig = inspect.signature(classescs_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_rootcs_is_not_abstract():
    assert not inspect.isabstract(classescs_RootCS)


def test_classescs_rootcs_constructor_exists():
    assert callable(classescs_RootCS.__init__)


def test_classescs_rootcs_constructor_args():
    sig = inspect.signature(classescs_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_roundedbracketclause_is_not_abstract():
    assert not inspect.isabstract(classescs_RoundedBracketClause)


def test_classescs_roundedbracketclause_constructor_exists():
    assert callable(classescs_RoundedBracketClause.__init__)


def test_classescs_roundedbracketclause_constructor_args():
    sig = inspect.signature(classescs_RoundedBracketClause.__init__)
    params = list(sig.parameters.keys())



def test_classescs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathNameCS)


def test_classescs_pathnamecs_constructor_exists():
    assert callable(classescs_PathNameCS.__init__)


def test_classescs_pathnamecs_constructor_args():
    sig = inspect.signature(classescs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_NamedElementCS)


def test_classescs_namedelementcs_constructor_exists():
    assert callable(classescs_NamedElementCS.__init__)


def test_classescs_namedelementcs_constructor_args():
    sig = inspect.signature(classescs_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classescs_namedelementcs_has_name():
    assert hasattr(classescs_NamedElementCS, "name")
    descriptor = None
    for klass in classescs_NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classescs_eobject_is_not_abstract():
    assert not inspect.isabstract(classescs_EObject)


def test_classescs_eobject_constructor_exists():
    assert callable(classescs_EObject.__init__)


def test_classescs_eobject_constructor_args():
    sig = inspect.signature(classescs_EObject.__init__)
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
classescs_OperationCS_strategy = st.builds(
    classescs_OperationCS,
    params=
        safe_text
)
classescs_PathElementCS_strategy = st.builds(
    classescs_PathElementCS,
)
classescs_ClassCS_strategy = st.builds(
    classescs_ClassCS,
)
classescs_PropertyCS_strategy = st.builds(
    classescs_PropertyCS,
)
classescs_PackageCS_strategy = st.builds(
    classescs_PackageCS,
)
classescs_ArgumentCS_strategy = st.builds(
    classescs_ArgumentCS,
)
classescs_ElementCS_strategy = st.builds(
    classescs_ElementCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
classescs_NameExpCS_strategy = st.builds(
    classescs_NameExpCS,
)
classescs_RootCS_strategy = st.builds(
    classescs_RootCS,
)
classescs_RoundedBracketClause_strategy = st.builds(
    classescs_RoundedBracketClause,
)
classescs_PathNameCS_strategy = st.builds(
    classescs_PathNameCS,
)
classescs_NamedElementCS_strategy = st.builds(
    classescs_NamedElementCS,
    name=
        safe_text
)
classescs_EObject_strategy = st.builds(
    classescs_EObject,
)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=classescs_OperationCS_strategy)
@settings(max_examples=50)
def test_classescs_operationcs_instantiation(instance):
    assert isinstance(instance, classescs_OperationCS)



@given(instance=classescs_OperationCS_strategy)
def test_classescs_operationcs_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=classescs_PathElementCS_strategy)
@settings(max_examples=50)
def test_classescs_pathelementcs_instantiation(instance):
    assert isinstance(instance, classescs_PathElementCS)

@given(instance=classescs_ClassCS_strategy)
@settings(max_examples=50)
def test_classescs_classcs_instantiation(instance):
    assert isinstance(instance, classescs_ClassCS)

@given(instance=classescs_PropertyCS_strategy)
@settings(max_examples=50)
def test_classescs_propertycs_instantiation(instance):
    assert isinstance(instance, classescs_PropertyCS)

@given(instance=classescs_PackageCS_strategy)
@settings(max_examples=50)
def test_classescs_packagecs_instantiation(instance):
    assert isinstance(instance, classescs_PackageCS)

@given(instance=classescs_ArgumentCS_strategy)
@settings(max_examples=50)
def test_classescs_argumentcs_instantiation(instance):
    assert isinstance(instance, classescs_ArgumentCS)

@given(instance=classescs_ElementCS_strategy)
@settings(max_examples=50)
def test_classescs_elementcs_instantiation(instance):
    assert isinstance(instance, classescs_ElementCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=classescs_NameExpCS_strategy)
@settings(max_examples=50)
def test_classescs_nameexpcs_instantiation(instance):
    assert isinstance(instance, classescs_NameExpCS)

@given(instance=classescs_RootCS_strategy)
@settings(max_examples=50)
def test_classescs_rootcs_instantiation(instance):
    assert isinstance(instance, classescs_RootCS)

@given(instance=classescs_RoundedBracketClause_strategy)
@settings(max_examples=50)
def test_classescs_roundedbracketclause_instantiation(instance):
    assert isinstance(instance, classescs_RoundedBracketClause)

@given(instance=classescs_PathNameCS_strategy)
@settings(max_examples=50)
def test_classescs_pathnamecs_instantiation(instance):
    assert isinstance(instance, classescs_PathNameCS)

@given(instance=classescs_NamedElementCS_strategy)
@settings(max_examples=50)
def test_classescs_namedelementcs_instantiation(instance):
    assert isinstance(instance, classescs_NamedElementCS)



@given(instance=classescs_NamedElementCS_strategy)
def test_classescs_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classescs_EObject_strategy)
@settings(max_examples=50)
def test_classescs_eobject_instantiation(instance):
    assert isinstance(instance, classescs_EObject)
