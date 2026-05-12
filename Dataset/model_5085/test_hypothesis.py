import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractComponent,
    adl199_AtomicComponent,
    adl199_Component,
    Interface,
    adl199_Binding,
    adl199_Interface,
    adl199_Delegation,
    adl199_Provided,
    adl199_Required,
    adl199_Content,
    adl199_AbstractComponent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl199_atomiccomponent_is_not_abstract():
    assert not inspect.isabstract(adl199_AtomicComponent)


def test_adl199_atomiccomponent_constructor_exists():
    assert callable(adl199_AtomicComponent.__init__)


def test_adl199_atomiccomponent_constructor_args():
    sig = inspect.signature(adl199_AtomicComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl199_component_is_not_abstract():
    assert not inspect.isabstract(adl199_Component)


def test_adl199_component_constructor_exists():
    assert callable(adl199_Component.__init__)


def test_adl199_component_constructor_args():
    sig = inspect.signature(adl199_Component.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl199_binding_is_not_abstract():
    assert not inspect.isabstract(adl199_Binding)


def test_adl199_binding_constructor_exists():
    assert callable(adl199_Binding.__init__)


def test_adl199_binding_constructor_args():
    sig = inspect.signature(adl199_Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl199_interface_is_not_abstract():
    assert not inspect.isabstract(adl199_Interface)


def test_adl199_interface_constructor_exists():
    assert callable(adl199_Interface.__init__)


def test_adl199_interface_constructor_args():
    sig = inspect.signature(adl199_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl199_interface_has_signature():
    assert hasattr(adl199_Interface, "signature")
    descriptor = None
    for klass in adl199_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl199_interface_has_name():
    assert hasattr(adl199_Interface, "name")
    descriptor = None
    for klass in adl199_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl199_delegation_is_not_abstract():
    assert not inspect.isabstract(adl199_Delegation)


def test_adl199_delegation_constructor_exists():
    assert callable(adl199_Delegation.__init__)


def test_adl199_delegation_constructor_args():
    sig = inspect.signature(adl199_Delegation.__init__)
    params = list(sig.parameters.keys())



def test_adl199_provided_is_not_abstract():
    assert not inspect.isabstract(adl199_Provided)


def test_adl199_provided_constructor_exists():
    assert callable(adl199_Provided.__init__)


def test_adl199_provided_constructor_args():
    sig = inspect.signature(adl199_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl199_required_is_not_abstract():
    assert not inspect.isabstract(adl199_Required)


def test_adl199_required_constructor_exists():
    assert callable(adl199_Required.__init__)


def test_adl199_required_constructor_args():
    sig = inspect.signature(adl199_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl199_content_is_not_abstract():
    assert not inspect.isabstract(adl199_Content)


def test_adl199_content_constructor_exists():
    assert callable(adl199_Content.__init__)


def test_adl199_content_constructor_args():
    sig = inspect.signature(adl199_Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl199_content_has_language():
    assert hasattr(adl199_Content, "language")
    descriptor = None
    for klass in adl199_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl199_content_has_expression():
    assert hasattr(adl199_Content, "expression")
    descriptor = None
    for klass in adl199_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adl199_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl199_AbstractComponent)


def test_adl199_abstractcomponent_constructor_exists():
    assert callable(adl199_AbstractComponent.__init__)


def test_adl199_abstractcomponent_constructor_args():
    sig = inspect.signature(adl199_AbstractComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl199_abstractcomponent_has_name():
    assert hasattr(adl199_AbstractComponent, "name")
    descriptor = None
    for klass in adl199_AbstractComponent.__mro__:
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
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adl199_AtomicComponent_strategy = st.builds(
    adl199_AtomicComponent,
)
adl199_Component_strategy = st.builds(
    adl199_Component,
)
Interface_strategy = st.builds(
    Interface,
)
adl199_Binding_strategy = st.builds(
    adl199_Binding,
)
adl199_Interface_strategy = st.builds(
    adl199_Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adl199_Delegation_strategy = st.builds(
    adl199_Delegation,
)
adl199_Provided_strategy = st.builds(
    adl199_Provided,
)
adl199_Required_strategy = st.builds(
    adl199_Required,
)
adl199_Content_strategy = st.builds(
    adl199_Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl199_AbstractComponent_strategy = st.builds(
    adl199_AbstractComponent,
    name=
        safe_text
)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adl199_AtomicComponent_strategy)
@settings(max_examples=50)
def test_adl199_atomiccomponent_instantiation(instance):
    assert isinstance(instance, adl199_AtomicComponent)

@given(instance=adl199_Component_strategy)
@settings(max_examples=50)
def test_adl199_component_instantiation(instance):
    assert isinstance(instance, adl199_Component)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl199_Binding_strategy)
@settings(max_examples=50)
def test_adl199_binding_instantiation(instance):
    assert isinstance(instance, adl199_Binding)

@given(instance=adl199_Interface_strategy)
@settings(max_examples=50)
def test_adl199_interface_instantiation(instance):
    assert isinstance(instance, adl199_Interface)



@given(instance=adl199_Interface_strategy)
def test_adl199_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=adl199_Interface_strategy)
def test_adl199_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl199_Delegation_strategy)
@settings(max_examples=50)
def test_adl199_delegation_instantiation(instance):
    assert isinstance(instance, adl199_Delegation)

@given(instance=adl199_Provided_strategy)
@settings(max_examples=50)
def test_adl199_provided_instantiation(instance):
    assert isinstance(instance, adl199_Provided)

@given(instance=adl199_Required_strategy)
@settings(max_examples=50)
def test_adl199_required_instantiation(instance):
    assert isinstance(instance, adl199_Required)

@given(instance=adl199_Content_strategy)
@settings(max_examples=50)
def test_adl199_content_instantiation(instance):
    assert isinstance(instance, adl199_Content)



@given(instance=adl199_Content_strategy)
def test_adl199_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=adl199_Content_strategy)
def test_adl199_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl199_AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl199_abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl199_AbstractComponent)



@given(instance=adl199_AbstractComponent_strategy)
def test_adl199_abstractcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
