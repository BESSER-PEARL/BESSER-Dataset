import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplepdl_ProcessElement,
    simplepdl_Process,
    ProcessElement,
    simplepdl_WorkSequence,
    simplepdl_Guidance,
    simplepdl_WorkDefinition,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplepdl_processelement_is_not_abstract():
    assert not inspect.isabstract(simplepdl_ProcessElement)


def test_simplepdl_processelement_constructor_exists():
    assert callable(simplepdl_ProcessElement.__init__)


def test_simplepdl_processelement_constructor_args():
    sig = inspect.signature(simplepdl_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_process_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Process)


def test_simplepdl_process_constructor_exists():
    assert callable(simplepdl_Process.__init__)


def test_simplepdl_process_constructor_args():
    sig = inspect.signature(simplepdl_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_process_has_name():
    assert hasattr(simplepdl_Process, "name")
    descriptor = None
    for klass in simplepdl_Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(simplepdl_WorkSequence)


def test_simplepdl_worksequence_constructor_exists():
    assert callable(simplepdl_WorkSequence.__init__)


def test_simplepdl_worksequence_constructor_args():
    sig = inspect.signature(simplepdl_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl_worksequence_has_linkType():
    assert hasattr(simplepdl_WorkSequence, "linkType")
    descriptor = None
    for klass in simplepdl_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_guidance_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Guidance)


def test_simplepdl_guidance_constructor_exists():
    assert callable(simplepdl_Guidance.__init__)


def test_simplepdl_guidance_constructor_args():
    sig = inspect.signature(simplepdl_Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_simplepdl_guidance_has_text():
    assert hasattr(simplepdl_Guidance, "text")
    descriptor = None
    for klass in simplepdl_Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl_WorkDefinition)


def test_simplepdl_workdefinition_constructor_exists():
    assert callable(simplepdl_WorkDefinition.__init__)


def test_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(simplepdl_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_workdefinition_has_name():
    assert hasattr(simplepdl_WorkDefinition, "name")
    descriptor = None
    for klass in simplepdl_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "finishToFinish",
        "startToFinish",
        "startToStart",
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
simplepdl_ProcessElement_strategy = st.builds(
    simplepdl_ProcessElement,
)
simplepdl_Process_strategy = st.builds(
    simplepdl_Process,
    name=
        safe_text
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl_WorkSequence_strategy = st.builds(
    simplepdl_WorkSequence,
    linkType=
        safe_text
)
simplepdl_Guidance_strategy = st.builds(
    simplepdl_Guidance,
    text=
        safe_text
)
simplepdl_WorkDefinition_strategy = st.builds(
    simplepdl_WorkDefinition,
    name=
        safe_text
)

@given(instance=simplepdl_ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl_processelement_instantiation(instance):
    assert isinstance(instance, simplepdl_ProcessElement)

@given(instance=simplepdl_Process_strategy)
@settings(max_examples=50)
def test_simplepdl_process_instantiation(instance):
    assert isinstance(instance, simplepdl_Process)



@given(instance=simplepdl_Process_strategy)
def test_simplepdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl_WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl_worksequence_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkSequence)



@given(instance=simplepdl_WorkSequence_strategy)
def test_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=simplepdl_Guidance_strategy)
@settings(max_examples=50)
def test_simplepdl_guidance_instantiation(instance):
    assert isinstance(instance, simplepdl_Guidance)



@given(instance=simplepdl_Guidance_strategy)
def test_simplepdl_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=simplepdl_WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkDefinition)



@given(instance=simplepdl_WorkDefinition_strategy)
def test_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
