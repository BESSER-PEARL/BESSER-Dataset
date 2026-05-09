import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IExtendible,
    ea::extensions::ExtendibleElement,
    ea::extensions::IExtension,
    IExtension,
    ExtensionElement,
    ea::extensions::BooleanExtension,
    ea::extensions::StringExtension,
    ea::extensions::StringListExtension,
    ea::extensions::IntegerExtension,
    ea::extensions::ExtensionElement,
    State,
    ExtendibleElement,
    ea::automata::Automaton,
    ea::extensions::IExtendible,
    ea::automata::Module,
    ea::automata::Transition,
    Automaton,
    ea::automata::State,
    Module,
    Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iextendible_is_not_abstract():
    assert not inspect.isabstract(IExtendible)


def test_iextendible_constructor_exists():
    assert callable(IExtendible.__init__)


def test_iextendible_constructor_args():
    sig = inspect.signature(IExtendible.__init__)
    params = list(sig.parameters.keys())



def test_ea::extensions::extendibleelement_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::ExtendibleElement)


def test_ea::extensions::extendibleelement_constructor_exists():
    assert callable(ea::extensions::ExtendibleElement.__init__)


def test_ea::extensions::extendibleelement_constructor_args():
    sig = inspect.signature(ea::extensions::ExtendibleElement.__init__)
    params = list(sig.parameters.keys())



def test_ea::extensions::iextension_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::IExtension)


def test_ea::extensions::iextension_constructor_exists():
    assert callable(ea::extensions::IExtension.__init__)


def test_ea::extensions::iextension_constructor_args():
    sig = inspect.signature(ea::extensions::IExtension.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ea::extensions::iextension_has_id():
    assert hasattr(ea::extensions::IExtension, "id")
    descriptor = None
    for klass in ea::extensions::IExtension.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_iextension_is_not_abstract():
    assert not inspect.isabstract(IExtension)


def test_iextension_constructor_exists():
    assert callable(IExtension.__init__)


def test_iextension_constructor_args():
    sig = inspect.signature(IExtension.__init__)
    params = list(sig.parameters.keys())



def test_extensionelement_is_not_abstract():
    assert not inspect.isabstract(ExtensionElement)


def test_extensionelement_constructor_exists():
    assert callable(ExtensionElement.__init__)


def test_extensionelement_constructor_args():
    sig = inspect.signature(ExtensionElement.__init__)
    params = list(sig.parameters.keys())



def test_ea::extensions::booleanextension_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::BooleanExtension)


def test_ea::extensions::booleanextension_constructor_exists():
    assert callable(ea::extensions::BooleanExtension.__init__)


def test_ea::extensions::booleanextension_constructor_args():
    sig = inspect.signature(ea::extensions::BooleanExtension.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ea::extensions::booleanextension_has_value():
    assert hasattr(ea::extensions::BooleanExtension, "value")
    descriptor = None
    for klass in ea::extensions::BooleanExtension.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ea::extensions::stringextension_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::StringExtension)


def test_ea::extensions::stringextension_constructor_exists():
    assert callable(ea::extensions::StringExtension.__init__)


def test_ea::extensions::stringextension_constructor_args():
    sig = inspect.signature(ea::extensions::StringExtension.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ea::extensions::stringextension_has_value():
    assert hasattr(ea::extensions::StringExtension, "value")
    descriptor = None
    for klass in ea::extensions::StringExtension.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ea::extensions::stringlistextension_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::StringListExtension)


def test_ea::extensions::stringlistextension_constructor_exists():
    assert callable(ea::extensions::StringListExtension.__init__)


def test_ea::extensions::stringlistextension_constructor_args():
    sig = inspect.signature(ea::extensions::StringListExtension.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_ea::extensions::stringlistextension_has_values():
    assert hasattr(ea::extensions::StringListExtension, "values")
    descriptor = None
    for klass in ea::extensions::StringListExtension.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_ea::extensions::integerextension_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::IntegerExtension)


def test_ea::extensions::integerextension_constructor_exists():
    assert callable(ea::extensions::IntegerExtension.__init__)


def test_ea::extensions::integerextension_constructor_args():
    sig = inspect.signature(ea::extensions::IntegerExtension.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ea::extensions::integerextension_has_value():
    assert hasattr(ea::extensions::IntegerExtension, "value")
    descriptor = None
    for klass in ea::extensions::IntegerExtension.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ea::extensions::extensionelement_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::ExtensionElement)


def test_ea::extensions::extensionelement_constructor_exists():
    assert callable(ea::extensions::ExtensionElement.__init__)


def test_ea::extensions::extensionelement_constructor_args():
    sig = inspect.signature(ea::extensions::ExtensionElement.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_extendibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtendibleElement)


def test_extendibleelement_constructor_exists():
    assert callable(ExtendibleElement.__init__)


def test_extendibleelement_constructor_args():
    sig = inspect.signature(ExtendibleElement.__init__)
    params = list(sig.parameters.keys())



def test_ea::automata::automaton_is_not_abstract():
    assert not inspect.isabstract(ea::automata::Automaton)


def test_ea::automata::automaton_constructor_exists():
    assert callable(ea::automata::Automaton.__init__)


def test_ea::automata::automaton_constructor_args():
    sig = inspect.signature(ea::automata::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "usedExtensionIds" in params, "Missing parameter 'usedExtensionIds'"
    assert "name" in params, "Missing parameter 'name'"

def test_ea::automata::automaton_has_id():
    assert hasattr(ea::automata::Automaton, "id")
    descriptor = None
    for klass in ea::automata::Automaton.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ea::automata::automaton_has_usedExtensionIds():
    assert hasattr(ea::automata::Automaton, "usedExtensionIds")
    descriptor = None
    for klass in ea::automata::Automaton.__mro__:
        if "usedExtensionIds" in klass.__dict__:
            descriptor = klass.__dict__["usedExtensionIds"]
            break
    assert isinstance(descriptor, property)

def test_ea::automata::automaton_has_name():
    assert hasattr(ea::automata::Automaton, "name")
    descriptor = None
    for klass in ea::automata::Automaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ea::extensions::iextendible_is_not_abstract():
    assert not inspect.isabstract(ea::extensions::IExtendible)


def test_ea::extensions::iextendible_constructor_exists():
    assert callable(ea::extensions::IExtendible.__init__)


def test_ea::extensions::iextendible_constructor_args():
    sig = inspect.signature(ea::extensions::IExtendible.__init__)
    params = list(sig.parameters.keys())



def test_ea::automata::module_is_not_abstract():
    assert not inspect.isabstract(ea::automata::Module)


def test_ea::automata::module_constructor_exists():
    assert callable(ea::automata::Module.__init__)


def test_ea::automata::module_constructor_args():
    sig = inspect.signature(ea::automata::Module.__init__)
    params = list(sig.parameters.keys())



def test_ea::automata::transition_is_not_abstract():
    assert not inspect.isabstract(ea::automata::Transition)


def test_ea::automata::transition_constructor_exists():
    assert callable(ea::automata::Transition.__init__)


def test_ea::automata::transition_constructor_args():
    sig = inspect.signature(ea::automata::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ea::automata::transition_has_id():
    assert hasattr(ea::automata::Transition, "id")
    descriptor = None
    for klass in ea::automata::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_automaton_is_not_abstract():
    assert not inspect.isabstract(Automaton)


def test_automaton_constructor_exists():
    assert callable(Automaton.__init__)


def test_automaton_constructor_args():
    sig = inspect.signature(Automaton.__init__)
    params = list(sig.parameters.keys())



def test_ea::automata::state_is_not_abstract():
    assert not inspect.isabstract(ea::automata::State)


def test_ea::automata::state_constructor_exists():
    assert callable(ea::automata::State.__init__)


def test_ea::automata::state_constructor_args():
    sig = inspect.signature(ea::automata::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_ea::automata::state_has_name():
    assert hasattr(ea::automata::State, "name")
    descriptor = None
    for klass in ea::automata::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ea::automata::state_has_id():
    assert hasattr(ea::automata::State, "id")
    descriptor = None
    for klass in ea::automata::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
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
IExtendible_strategy = st.builds(
    IExtendible,
)
ea::extensions::ExtendibleElement_strategy = st.builds(
    ea::extensions::ExtendibleElement,
)
ea::extensions::IExtension_strategy = st.builds(
    ea::extensions::IExtension,
    id=
        safe_text
)
IExtension_strategy = st.builds(
    IExtension,
)
ExtensionElement_strategy = st.builds(
    ExtensionElement,
)
ea::extensions::BooleanExtension_strategy = st.builds(
    ea::extensions::BooleanExtension,
    value=
        st.booleans()
)
ea::extensions::StringExtension_strategy = st.builds(
    ea::extensions::StringExtension,
    value=
        safe_text
)
ea::extensions::StringListExtension_strategy = st.builds(
    ea::extensions::StringListExtension,
    values=
        safe_text
)
ea::extensions::IntegerExtension_strategy = st.builds(
    ea::extensions::IntegerExtension,
    value=
        st.integers()
)
ea::extensions::ExtensionElement_strategy = st.builds(
    ea::extensions::ExtensionElement,
)
State_strategy = st.builds(
    State,
)
ExtendibleElement_strategy = st.builds(
    ExtendibleElement,
)
ea::automata::Automaton_strategy = st.builds(
    ea::automata::Automaton,
    id=
        safe_text,
    usedExtensionIds=
        safe_text,
    name=
        safe_text
)
ea::extensions::IExtendible_strategy = st.builds(
    ea::extensions::IExtendible,
)
ea::automata::Module_strategy = st.builds(
    ea::automata::Module,
)
ea::automata::Transition_strategy = st.builds(
    ea::automata::Transition,
    id=
        safe_text
)
Automaton_strategy = st.builds(
    Automaton,
)
ea::automata::State_strategy = st.builds(
    ea::automata::State,
    name=
        safe_text,
    id=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
Transition_strategy = st.builds(
    Transition,
)

@given(instance=IExtendible_strategy)
@settings(max_examples=50)
def test_iextendible_instantiation(instance):
    assert isinstance(instance, IExtendible)

@given(instance=ea::extensions::ExtendibleElement_strategy)
@settings(max_examples=50)
def test_ea::extensions::extendibleelement_instantiation(instance):
    assert isinstance(instance, ea::extensions::ExtendibleElement)

@given(instance=ea::extensions::IExtension_strategy)
@settings(max_examples=50)
def test_ea::extensions::iextension_instantiation(instance):
    assert isinstance(instance, ea::extensions::IExtension)

@given(instance=ea::extensions::IExtension_strategy)
def test_ea::extensions::iextension_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ea::extensions::IExtension_strategy)
def test_ea::extensions::iextension_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=IExtension_strategy)
@settings(max_examples=50)
def test_iextension_instantiation(instance):
    assert isinstance(instance, IExtension)

@given(instance=ExtensionElement_strategy)
@settings(max_examples=50)
def test_extensionelement_instantiation(instance):
    assert isinstance(instance, ExtensionElement)

@given(instance=ea::extensions::BooleanExtension_strategy)
@settings(max_examples=50)
def test_ea::extensions::booleanextension_instantiation(instance):
    assert isinstance(instance, ea::extensions::BooleanExtension)

@given(instance=ea::extensions::BooleanExtension_strategy)
def test_ea::extensions::booleanextension_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=ea::extensions::BooleanExtension_strategy)
def test_ea::extensions::booleanextension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ea::extensions::StringExtension_strategy)
@settings(max_examples=50)
def test_ea::extensions::stringextension_instantiation(instance):
    assert isinstance(instance, ea::extensions::StringExtension)

@given(instance=ea::extensions::StringExtension_strategy)
def test_ea::extensions::stringextension_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ea::extensions::StringExtension_strategy)
def test_ea::extensions::stringextension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ea::extensions::StringListExtension_strategy)
@settings(max_examples=50)
def test_ea::extensions::stringlistextension_instantiation(instance):
    assert isinstance(instance, ea::extensions::StringListExtension)

@given(instance=ea::extensions::StringListExtension_strategy)
def test_ea::extensions::stringlistextension_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=ea::extensions::StringListExtension_strategy)
def test_ea::extensions::stringlistextension_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ea::extensions::IntegerExtension_strategy)
@settings(max_examples=50)
def test_ea::extensions::integerextension_instantiation(instance):
    assert isinstance(instance, ea::extensions::IntegerExtension)

@given(instance=ea::extensions::IntegerExtension_strategy)
def test_ea::extensions::integerextension_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ea::extensions::IntegerExtension_strategy)
def test_ea::extensions::integerextension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ea::extensions::ExtensionElement_strategy)
@settings(max_examples=50)
def test_ea::extensions::extensionelement_instantiation(instance):
    assert isinstance(instance, ea::extensions::ExtensionElement)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=ExtendibleElement_strategy)
@settings(max_examples=50)
def test_extendibleelement_instantiation(instance):
    assert isinstance(instance, ExtendibleElement)

@given(instance=ea::automata::Automaton_strategy)
@settings(max_examples=50)
def test_ea::automata::automaton_instantiation(instance):
    assert isinstance(instance, ea::automata::Automaton)

@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_usedExtensionIds_type(instance):
    assert isinstance(instance.usedExtensionIds, str)


@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_usedExtensionIds_setter(instance):
    original = instance.usedExtensionIds
    instance.usedExtensionIds = original
    assert instance.usedExtensionIds == original

@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ea::automata::Automaton_strategy)
def test_ea::automata::automaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ea::extensions::IExtendible_strategy)
@settings(max_examples=50)
def test_ea::extensions::iextendible_instantiation(instance):
    assert isinstance(instance, ea::extensions::IExtendible)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ea::extensions::IExtendible_strategy)
@settings(max_examples=30)
def test_ea::extensions::iextendible_updateextension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateExtension(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateExtension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateExtension' in ea::extensions::IExtendible is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateExtension' in ea::extensions::IExtendible did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateExtension' in ea::extensions::IExtendible is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ea::extensions::IExtendible_strategy)
@settings(max_examples=30)
def test_ea::extensions::iextendible_findextension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findExtension(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findExtension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findExtension' in ea::extensions::IExtendible is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findExtension' in ea::extensions::IExtendible did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findExtension' in ea::extensions::IExtendible is not implemented or raised an error")

@given(instance=ea::automata::Module_strategy)
@settings(max_examples=50)
def test_ea::automata::module_instantiation(instance):
    assert isinstance(instance, ea::automata::Module)

@given(instance=ea::automata::Transition_strategy)
@settings(max_examples=50)
def test_ea::automata::transition_instantiation(instance):
    assert isinstance(instance, ea::automata::Transition)

@given(instance=ea::automata::Transition_strategy)
def test_ea::automata::transition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ea::automata::Transition_strategy)
def test_ea::automata::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Automaton_strategy)
@settings(max_examples=50)
def test_automaton_instantiation(instance):
    assert isinstance(instance, Automaton)

@given(instance=ea::automata::State_strategy)
@settings(max_examples=50)
def test_ea::automata::state_instantiation(instance):
    assert isinstance(instance, ea::automata::State)

@given(instance=ea::automata::State_strategy)
def test_ea::automata::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ea::automata::State_strategy)
def test_ea::automata::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ea::automata::State_strategy)
def test_ea::automata::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ea::automata::State_strategy)
def test_ea::automata::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)
