import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplepdl::Allocation,
    ProcessElement,
    simplepdl::WorkSequence,
    simplepdl::WorkDefinition,
    simplepdl::ProcessElement,
    simplepdl::Process,
    simplepdl::Ressource,
    simplepdl::Guidance,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplepdl::allocation_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Allocation)


def test_simplepdl::allocation_constructor_exists():
    assert callable(simplepdl::Allocation.__init__)


def test_simplepdl::allocation_constructor_args():
    sig = inspect.signature(simplepdl::Allocation.__init__)
    params = list(sig.parameters.keys())
    assert "needed" in params, "Missing parameter 'needed'"

def test_simplepdl::allocation_has_needed():
    assert hasattr(simplepdl::Allocation, "needed")
    descriptor = None
    for klass in simplepdl::Allocation.__mro__:
        if "needed" in klass.__dict__:
            descriptor = klass.__dict__["needed"]
            break
    assert isinstance(descriptor, property)



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



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



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(simplepdl::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(simplepdl::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

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

def test_simplepdl::process_has_name():
    assert hasattr(simplepdl::Process, "name")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::ressource_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Ressource)


def test_simplepdl::ressource_constructor_exists():
    assert callable(simplepdl::Ressource.__init__)


def test_simplepdl::ressource_constructor_args():
    sig = inspect.signature(simplepdl::Ressource.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::ressource_has_count():
    assert hasattr(simplepdl::Ressource, "count")
    descriptor = None
    for klass in simplepdl::Ressource.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::ressource_has_name():
    assert hasattr(simplepdl::Ressource, "name")
    descriptor = None
    for klass in simplepdl::Ressource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "startToStart",
        "finishToFinish",
        "startToFinish",
        "finishToStart",
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
simplepdl::Allocation_strategy = st.builds(
    simplepdl::Allocation,
    needed=
        st.integers()
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl::WorkSequence_strategy = st.builds(
    simplepdl::WorkSequence,
    linkType=
        safe_text
)
simplepdl::WorkDefinition_strategy = st.builds(
    simplepdl::WorkDefinition,
    name=
        safe_text
)
simplepdl::ProcessElement_strategy = st.builds(
    simplepdl::ProcessElement,
)
simplepdl::Process_strategy = st.builds(
    simplepdl::Process,
    name=
        safe_text
)
simplepdl::Ressource_strategy = st.builds(
    simplepdl::Ressource,
    count=
        st.integers(),
    name=
        safe_text
)
simplepdl::Guidance_strategy = st.builds(
    simplepdl::Guidance,
    text=
        safe_text
)

@given(instance=simplepdl::Allocation_strategy)
@settings(max_examples=50)
def test_simplepdl::allocation_instantiation(instance):
    assert isinstance(instance, simplepdl::Allocation)

@given(instance=simplepdl::Allocation_strategy)
def test_simplepdl::allocation_needed_type(instance):
    assert isinstance(instance.needed, int)


@given(instance=simplepdl::Allocation_strategy)
def test_simplepdl::allocation_needed_setter(instance):
    original = instance.needed
    instance.needed = original
    assert instance.needed == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

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

@given(instance=simplepdl::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::WorkDefinition)

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

@given(instance=simplepdl::Ressource_strategy)
@settings(max_examples=50)
def test_simplepdl::ressource_instantiation(instance):
    assert isinstance(instance, simplepdl::Ressource)

@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Ressource_strategy)
def test_simplepdl::ressource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
