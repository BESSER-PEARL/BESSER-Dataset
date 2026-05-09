import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProcessElement,
    simplepdl::RequeteDeRessource,
    simplepdl::GuidanceLink,
    simplepdl::WorkSequence,
    simplepdl::WorkDefinition,
    simplepdl::ProcessElement,
    simplepdl::Process,
    simplepdl::Resources,
    simplepdl::Guidance,
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



def test_simplepdl::requetederessource_is_not_abstract():
    assert not inspect.isabstract(simplepdl::RequeteDeRessource)


def test_simplepdl::requetederessource_constructor_exists():
    assert callable(simplepdl::RequeteDeRessource.__init__)


def test_simplepdl::requetederessource_constructor_args():
    sig = inspect.signature(simplepdl::RequeteDeRessource.__init__)
    params = list(sig.parameters.keys())
    assert "quantite" in params, "Missing parameter 'quantite'"

def test_simplepdl::requetederessource_has_quantite():
    assert hasattr(simplepdl::RequeteDeRessource, "quantite")
    descriptor = None
    for klass in simplepdl::RequeteDeRessource.__mro__:
        if "quantite" in klass.__dict__:
            descriptor = klass.__dict__["quantite"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::guidancelink_is_not_abstract():
    assert not inspect.isabstract(simplepdl::GuidanceLink)


def test_simplepdl::guidancelink_constructor_exists():
    assert callable(simplepdl::GuidanceLink.__init__)


def test_simplepdl::guidancelink_constructor_args():
    sig = inspect.signature(simplepdl::GuidanceLink.__init__)
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



def test_simplepdl::resources_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Resources)


def test_simplepdl::resources_constructor_exists():
    assert callable(simplepdl::Resources.__init__)


def test_simplepdl::resources_constructor_args():
    sig = inspect.signature(simplepdl::Resources.__init__)
    params = list(sig.parameters.keys())
    assert "quantite" in params, "Missing parameter 'quantite'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::resources_has_quantite():
    assert hasattr(simplepdl::Resources, "quantite")
    descriptor = None
    for klass in simplepdl::Resources.__mro__:
        if "quantite" in klass.__dict__:
            descriptor = klass.__dict__["quantite"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::resources_has_name():
    assert hasattr(simplepdl::Resources, "name")
    descriptor = None
    for klass in simplepdl::Resources.__mro__:
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
        "finishToFinish",
        "startToStart",
        "finishToStart",
        "startToFinish",
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
simplepdl::RequeteDeRessource_strategy = st.builds(
    simplepdl::RequeteDeRessource,
    quantite=
        st.integers()
)
simplepdl::GuidanceLink_strategy = st.builds(
    simplepdl::GuidanceLink,
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
simplepdl::Resources_strategy = st.builds(
    simplepdl::Resources,
    quantite=
        st.integers(),
    name=
        safe_text
)
simplepdl::Guidance_strategy = st.builds(
    simplepdl::Guidance,
    text=
        safe_text
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl::RequeteDeRessource_strategy)
@settings(max_examples=50)
def test_simplepdl::requetederessource_instantiation(instance):
    assert isinstance(instance, simplepdl::RequeteDeRessource)

@given(instance=simplepdl::RequeteDeRessource_strategy)
def test_simplepdl::requetederessource_quantite_type(instance):
    assert isinstance(instance.quantite, int)


@given(instance=simplepdl::RequeteDeRessource_strategy)
def test_simplepdl::requetederessource_quantite_setter(instance):
    original = instance.quantite
    instance.quantite = original
    assert instance.quantite == original

@given(instance=simplepdl::GuidanceLink_strategy)
@settings(max_examples=50)
def test_simplepdl::guidancelink_instantiation(instance):
    assert isinstance(instance, simplepdl::GuidanceLink)

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

@given(instance=simplepdl::Resources_strategy)
@settings(max_examples=50)
def test_simplepdl::resources_instantiation(instance):
    assert isinstance(instance, simplepdl::Resources)

@given(instance=simplepdl::Resources_strategy)
def test_simplepdl::resources_quantite_type(instance):
    assert isinstance(instance.quantite, int)


@given(instance=simplepdl::Resources_strategy)
def test_simplepdl::resources_quantite_setter(instance):
    original = instance.quantite
    instance.quantite = original
    assert instance.quantite == original

@given(instance=simplepdl::Resources_strategy)
def test_simplepdl::resources_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Resources_strategy)
def test_simplepdl::resources_name_setter(instance):
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
