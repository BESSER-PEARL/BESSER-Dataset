import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProcessElement,
    simplepdl::RessourceLink,
    simplepdl::WorkDefinition,
    simplepdl::ProcessElement,
    simplepdl::Process,
    simplepdl::Ressource,
    simplepdl::Guidance,
    simplepdl::WorkSequence,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::ressourcelink_is_not_abstract():
    assert not inspect.isabstract(simplepdl::RessourceLink)


def test_simplepdl::ressourcelink_constructor_exists():
    assert callable(simplepdl::RessourceLink.__init__)


def test_simplepdl::ressourcelink_constructor_args():
    sig = inspect.signature(simplepdl::RessourceLink.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_simplepdl::ressourcelink_has_weight():
    assert hasattr(simplepdl::RessourceLink, "weight")
    descriptor = None
    for klass in simplepdl::RessourceLink.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(simplepdl::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(simplepdl::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::workdefinition_has_min_time():
    assert hasattr(simplepdl::WorkDefinition, "min_time")
    descriptor = None
    for klass in simplepdl::WorkDefinition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::workdefinition_has_max_time():
    assert hasattr(simplepdl::WorkDefinition, "max_time")
    descriptor = None
    for klass in simplepdl::WorkDefinition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::workdefinition_has_name():
    assert hasattr(simplepdl::WorkDefinition, "name")
    descriptor = None
    for klass in simplepdl::WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::processelement_is_not_abstract():
    assert not inspect.isabstract(simplepdl::ProcessElement)


def test_simplepdl::processelement_constructor_exists():
    assert callable(simplepdl::ProcessElement.__init__)


def test_simplepdl::processelement_constructor_args():
    sig = inspect.signature(simplepdl::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::process_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Process)


def test_simplepdl::process_constructor_exists():
    assert callable(simplepdl::Process.__init__)


def test_simplepdl::process_constructor_args():
    sig = inspect.signature(simplepdl::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_simplepdl::process_has_name():
    assert hasattr(simplepdl::Process, "name")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_max_time():
    assert hasattr(simplepdl::Process, "max_time")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_min_time():
    assert hasattr(simplepdl::Process, "min_time")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::ressource_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Ressource)


def test_simplepdl::ressource_constructor_exists():
    assert callable(simplepdl::Ressource.__init__)


def test_simplepdl::ressource_constructor_args():
    sig = inspect.signature(simplepdl::Ressource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_simplepdl::ressource_has_name():
    assert hasattr(simplepdl::Ressource, "name")
    descriptor = None
    for klass in simplepdl::Ressource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::ressource_has_quantity():
    assert hasattr(simplepdl::Ressource, "quantity")
    descriptor = None
    for klass in simplepdl::Ressource.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::guidance_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Guidance)


def test_simplepdl::guidance_constructor_exists():
    assert callable(simplepdl::Guidance.__init__)


def test_simplepdl::guidance_constructor_args():
    sig = inspect.signature(simplepdl::Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_simplepdl::guidance_has_text():
    assert hasattr(simplepdl::Guidance, "text")
    descriptor = None
    for klass in simplepdl::Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::worksequence_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkSequence)


def test_simplepdl::worksequence_constructor_exists():
    assert callable(simplepdl::WorkSequence.__init__)


def test_simplepdl::worksequence_constructor_args():
    sig = inspect.signature(simplepdl::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl::worksequence_has_linkType():
    assert hasattr(simplepdl::WorkSequence, "linkType")
    descriptor = None
    for klass in simplepdl::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "startToStart",
        "startToFinish",
        "finishToStart",
        "finishToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceType"


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
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl::RessourceLink_strategy = st.builds(
    simplepdl::RessourceLink,
    weight=
        st.integers()
)
simplepdl::WorkDefinition_strategy = st.builds(
    simplepdl::WorkDefinition,
    min_time=
        st.integers(),
    max_time=
        st.integers(),
    name=
        safe_text
)
simplepdl::ProcessElement_strategy = st.builds(
    simplepdl::ProcessElement,
)
simplepdl::Process_strategy = st.builds(
    simplepdl::Process,
    name=
        safe_text,
    max_time=
        st.integers(),
    min_time=
        st.integers()
)
simplepdl::Ressource_strategy = st.builds(
    simplepdl::Ressource,
    name=
        safe_text,
    quantity=
        st.integers()
)
simplepdl::Guidance_strategy = st.builds(
    simplepdl::Guidance,
    text=
        safe_text
)
simplepdl::WorkSequence_strategy = st.builds(
    simplepdl::WorkSequence,
    linkType=
        safe_text
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl::RessourceLink_strategy)
@settings(max_examples=50)
def test_simplepdl::ressourcelink_instantiation(instance):
    assert isinstance(instance, simplepdl::RessourceLink)

@given(instance=simplepdl::RessourceLink_strategy)
def test_simplepdl::ressourcelink_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=simplepdl::RessourceLink_strategy)
def test_simplepdl::ressourcelink_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=simplepdl::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::WorkDefinition)

@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl::processelement_instantiation(instance):
    assert isinstance(instance, simplepdl::ProcessElement)

@given(instance=simplepdl::Process_strategy)
@settings(max_examples=50)
def test_simplepdl::process_instantiation(instance):
    assert isinstance(instance, simplepdl::Process)

@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=simplepdl::Ressource_strategy)
@settings(max_examples=50)
def test_simplepdl::ressource_instantiation(instance):
    assert isinstance(instance, simplepdl::Ressource)

@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=simplepdl::Guidance_strategy)
@settings(max_examples=50)
def test_simplepdl::guidance_instantiation(instance):
    assert isinstance(instance, simplepdl::Guidance)

@given(instance=simplepdl::Guidance_strategy)
def test_simplepdl::guidance_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=simplepdl::Guidance_strategy)
def test_simplepdl::guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=simplepdl::WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl::worksequence_instantiation(instance):
    assert isinstance(instance, simplepdl::WorkSequence)

@given(instance=simplepdl::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=simplepdl::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original
