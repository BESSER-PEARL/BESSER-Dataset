import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    beans_NamedElement,
    NamedElement,
    beans_BeanProperty,
    beans_Bean,
    beans_BeanLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_beans_namedelement_is_not_abstract():
    assert not inspect.isabstract(beans_NamedElement)


def test_beans_namedelement_constructor_exists():
    assert callable(beans_NamedElement.__init__)


def test_beans_namedelement_constructor_args():
    sig = inspect.signature(beans_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_beans_namedelement_has_name():
    assert hasattr(beans_NamedElement, "name")
    descriptor = None
    for klass in beans_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_beans_beanproperty_is_not_abstract():
    assert not inspect.isabstract(beans_BeanProperty)


def test_beans_beanproperty_constructor_exists():
    assert callable(beans_BeanProperty.__init__)


def test_beans_beanproperty_constructor_args():
    sig = inspect.signature(beans_BeanProperty.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_beans_beanproperty_has_typeName():
    assert hasattr(beans_BeanProperty, "typeName")
    descriptor = None
    for klass in beans_BeanProperty.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_beans_beanproperty_has_changeable():
    assert hasattr(beans_BeanProperty, "changeable")
    descriptor = None
    for klass in beans_BeanProperty.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_beans_bean_is_not_abstract():
    assert not inspect.isabstract(beans_Bean)


def test_beans_bean_constructor_exists():
    assert callable(beans_Bean.__init__)


def test_beans_bean_constructor_args():
    sig = inspect.signature(beans_Bean.__init__)
    params = list(sig.parameters.keys())



def test_beans_beanlibrary_is_not_abstract():
    assert not inspect.isabstract(beans_BeanLibrary)


def test_beans_beanlibrary_constructor_exists():
    assert callable(beans_BeanLibrary.__init__)


def test_beans_beanlibrary_constructor_args():
    sig = inspect.signature(beans_BeanLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_beans_beanlibrary_has_packageName():
    assert hasattr(beans_BeanLibrary, "packageName")
    descriptor = None
    for klass in beans_BeanLibrary.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
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
beans_NamedElement_strategy = st.builds(
    beans_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
beans_BeanProperty_strategy = st.builds(
    beans_BeanProperty,
    typeName=
        safe_text,
    changeable=
        st.booleans()
)
beans_Bean_strategy = st.builds(
    beans_Bean,
)
beans_BeanLibrary_strategy = st.builds(
    beans_BeanLibrary,
    packageName=
        safe_text
)

@given(instance=beans_NamedElement_strategy)
@settings(max_examples=50)
def test_beans_namedelement_instantiation(instance):
    assert isinstance(instance, beans_NamedElement)



@given(instance=beans_NamedElement_strategy)
def test_beans_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=beans_BeanProperty_strategy)
@settings(max_examples=50)
def test_beans_beanproperty_instantiation(instance):
    assert isinstance(instance, beans_BeanProperty)



@given(instance=beans_BeanProperty_strategy)
def test_beans_beanproperty_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=beans_BeanProperty_strategy)
def test_beans_beanproperty_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=beans_Bean_strategy)
@settings(max_examples=50)
def test_beans_bean_instantiation(instance):
    assert isinstance(instance, beans_Bean)

@given(instance=beans_BeanLibrary_strategy)
@settings(max_examples=50)
def test_beans_beanlibrary_instantiation(instance):
    assert isinstance(instance, beans_BeanLibrary)



@given(instance=beans_BeanLibrary_strategy)
def test_beans_beanlibrary_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original
