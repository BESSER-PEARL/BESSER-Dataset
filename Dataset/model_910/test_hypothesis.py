import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProcessElement,
    pDL1::WorkSequence,
    pDL1::Guidance,
    pDL1::WorkDefinition,
    pDL1::ProcessElement,
    pDL1::Process,
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



def test_pdl1::worksequence_is_not_abstract():
    assert not inspect.isabstract(pDL1::WorkSequence)


def test_pdl1::worksequence_constructor_exists():
    assert callable(pDL1::WorkSequence.__init__)


def test_pdl1::worksequence_constructor_args():
    sig = inspect.signature(pDL1::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_pdl1::worksequence_has_linkType():
    assert hasattr(pDL1::WorkSequence, "linkType")
    descriptor = None
    for klass in pDL1::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_pdl1::guidance_is_not_abstract():
    assert not inspect.isabstract(pDL1::Guidance)


def test_pdl1::guidance_constructor_exists():
    assert callable(pDL1::Guidance.__init__)


def test_pdl1::guidance_constructor_args():
    sig = inspect.signature(pDL1::Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "texte" in params, "Missing parameter 'texte'"

def test_pdl1::guidance_has_texte():
    assert hasattr(pDL1::Guidance, "texte")
    descriptor = None
    for klass in pDL1::Guidance.__mro__:
        if "texte" in klass.__dict__:
            descriptor = klass.__dict__["texte"]
            break
    assert isinstance(descriptor, property)



def test_pdl1::workdefinition_is_not_abstract():
    assert not inspect.isabstract(pDL1::WorkDefinition)


def test_pdl1::workdefinition_constructor_exists():
    assert callable(pDL1::WorkDefinition.__init__)


def test_pdl1::workdefinition_constructor_args():
    sig = inspect.signature(pDL1::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdl1::workdefinition_has_name():
    assert hasattr(pDL1::WorkDefinition, "name")
    descriptor = None
    for klass in pDL1::WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pdl1::processelement_is_not_abstract():
    assert not inspect.isabstract(pDL1::ProcessElement)


def test_pdl1::processelement_constructor_exists():
    assert callable(pDL1::ProcessElement.__init__)


def test_pdl1::processelement_constructor_args():
    sig = inspect.signature(pDL1::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_pdl1::process_is_not_abstract():
    assert not inspect.isabstract(pDL1::Process)


def test_pdl1::process_constructor_exists():
    assert callable(pDL1::Process.__init__)


def test_pdl1::process_constructor_args():
    sig = inspect.signature(pDL1::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pdl1::process_has_name():
    assert hasattr(pDL1::Process, "name")
    descriptor = None
    for klass in pDL1::Process.__mro__:
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
        "start2start",
        "finish2finish",
        "finish2start",
        "start2finish",
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
pDL1::WorkSequence_strategy = st.builds(
    pDL1::WorkSequence,
    linkType=
        safe_text
)
pDL1::Guidance_strategy = st.builds(
    pDL1::Guidance,
    texte=
        safe_text
)
pDL1::WorkDefinition_strategy = st.builds(
    pDL1::WorkDefinition,
    name=
        safe_text
)
pDL1::ProcessElement_strategy = st.builds(
    pDL1::ProcessElement,
)
pDL1::Process_strategy = st.builds(
    pDL1::Process,
    name=
        safe_text
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=pDL1::WorkSequence_strategy)
@settings(max_examples=50)
def test_pdl1::worksequence_instantiation(instance):
    assert isinstance(instance, pDL1::WorkSequence)

@given(instance=pDL1::WorkSequence_strategy)
def test_pdl1::worksequence_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=pDL1::WorkSequence_strategy)
def test_pdl1::worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=pDL1::Guidance_strategy)
@settings(max_examples=50)
def test_pdl1::guidance_instantiation(instance):
    assert isinstance(instance, pDL1::Guidance)

@given(instance=pDL1::Guidance_strategy)
def test_pdl1::guidance_texte_type(instance):
    assert isinstance(instance.texte, str)


@given(instance=pDL1::Guidance_strategy)
def test_pdl1::guidance_texte_setter(instance):
    original = instance.texte
    instance.texte = original
    assert instance.texte == original

@given(instance=pDL1::WorkDefinition_strategy)
@settings(max_examples=50)
def test_pdl1::workdefinition_instantiation(instance):
    assert isinstance(instance, pDL1::WorkDefinition)

@given(instance=pDL1::WorkDefinition_strategy)
def test_pdl1::workdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pDL1::WorkDefinition_strategy)
def test_pdl1::workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pDL1::ProcessElement_strategy)
@settings(max_examples=50)
def test_pdl1::processelement_instantiation(instance):
    assert isinstance(instance, pDL1::ProcessElement)

@given(instance=pDL1::Process_strategy)
@settings(max_examples=50)
def test_pdl1::process_instantiation(instance):
    assert isinstance(instance, pDL1::Process)

@given(instance=pDL1::Process_strategy)
def test_pdl1::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pDL1::Process_strategy)
def test_pdl1::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
