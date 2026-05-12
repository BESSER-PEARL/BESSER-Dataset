import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProcessElement,
    pDL1_WorkSequence,
    pDL1_Guidance,
    pDL1_WorkDefinition,
    pDL1_ProcessElement,
    pDL1_Process,
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



def test_pdl1_worksequence_is_not_abstract():
    assert not inspect.isabstract(pDL1_WorkSequence)


def test_pdl1_worksequence_constructor_exists():
    assert callable(pDL1_WorkSequence.__init__)


def test_pdl1_worksequence_constructor_args():
    sig = inspect.signature(pDL1_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_pdl1_worksequence_has_linkType():
    assert hasattr(pDL1_WorkSequence, "linkType")
    descriptor = None
    for klass in pDL1_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_pdl1_guidance_is_not_abstract():
    assert not inspect.isabstract(pDL1_Guidance)


def test_pdl1_guidance_constructor_exists():
    assert callable(pDL1_Guidance.__init__)


def test_pdl1_guidance_constructor_args():
    sig = inspect.signature(pDL1_Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pdl1_guidance_has_text():
    assert hasattr(pDL1_Guidance, "text")
    descriptor = None
    for klass in pDL1_Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pdl1_workdefinition_is_not_abstract():
    assert not inspect.isabstract(pDL1_WorkDefinition)


def test_pdl1_workdefinition_constructor_exists():
    assert callable(pDL1_WorkDefinition.__init__)


def test_pdl1_workdefinition_constructor_args():
    sig = inspect.signature(pDL1_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdl1_workdefinition_has_name():
    assert hasattr(pDL1_WorkDefinition, "name")
    descriptor = None
    for klass in pDL1_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pdl1_processelement_is_not_abstract():
    assert not inspect.isabstract(pDL1_ProcessElement)


def test_pdl1_processelement_constructor_exists():
    assert callable(pDL1_ProcessElement.__init__)


def test_pdl1_processelement_constructor_args():
    sig = inspect.signature(pDL1_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_pdl1_process_is_not_abstract():
    assert not inspect.isabstract(pDL1_Process)


def test_pdl1_process_constructor_exists():
    assert callable(pDL1_Process.__init__)


def test_pdl1_process_constructor_args():
    sig = inspect.signature(pDL1_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdl1_process_has_name():
    assert hasattr(pDL1_Process, "name")
    descriptor = None
    for klass in pDL1_Process.__mro__:
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
        "start2finish",
        "finish2finish",
        "finish2start",
        "start2start",
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
pDL1_WorkSequence_strategy = st.builds(
    pDL1_WorkSequence,
    linkType=
        safe_text
)
pDL1_Guidance_strategy = st.builds(
    pDL1_Guidance,
    text=
        safe_text
)
pDL1_WorkDefinition_strategy = st.builds(
    pDL1_WorkDefinition,
    name=
        safe_text
)
pDL1_ProcessElement_strategy = st.builds(
    pDL1_ProcessElement,
)
pDL1_Process_strategy = st.builds(
    pDL1_Process,
    name=
        safe_text
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=pDL1_WorkSequence_strategy)
@settings(max_examples=50)
def test_pdl1_worksequence_instantiation(instance):
    assert isinstance(instance, pDL1_WorkSequence)



@given(instance=pDL1_WorkSequence_strategy)
def test_pdl1_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=pDL1_Guidance_strategy)
@settings(max_examples=50)
def test_pdl1_guidance_instantiation(instance):
    assert isinstance(instance, pDL1_Guidance)



@given(instance=pDL1_Guidance_strategy)
def test_pdl1_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pDL1_WorkDefinition_strategy)
@settings(max_examples=50)
def test_pdl1_workdefinition_instantiation(instance):
    assert isinstance(instance, pDL1_WorkDefinition)



@given(instance=pDL1_WorkDefinition_strategy)
def test_pdl1_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pDL1_ProcessElement_strategy)
@settings(max_examples=50)
def test_pdl1_processelement_instantiation(instance):
    assert isinstance(instance, pDL1_ProcessElement)

@given(instance=pDL1_Process_strategy)
@settings(max_examples=50)
def test_pdl1_process_instantiation(instance):
    assert isinstance(instance, pDL1_Process)



@given(instance=pDL1_Process_strategy)
def test_pdl1_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
