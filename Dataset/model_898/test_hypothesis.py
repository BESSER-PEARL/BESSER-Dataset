import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProcessElement,
    SimplePDL::ResourceType,
    SimplePDL::Resource,
    SimplePDL::WorkSequence,
    SimplePDL::WorkDefinition,
    SimplePDL::Guidance,
    SimplePDL::ProcessElement,
    SimplePDL::Process,
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



def test_simplepdl::resourcetype_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::ResourceType)


def test_simplepdl::resourcetype_constructor_exists():
    assert callable(SimplePDL::ResourceType.__init__)


def test_simplepdl::resourcetype_constructor_args():
    sig = inspect.signature(SimplePDL::ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_simplepdl::resourcetype_has_name():
    assert hasattr(SimplePDL::ResourceType, "name")
    descriptor = None
    for klass in SimplePDL::ResourceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::resourcetype_has_occurrences():
    assert hasattr(SimplePDL::ResourceType, "occurrences")
    descriptor = None
    for klass in SimplePDL::ResourceType.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::resource_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::Resource)


def test_simplepdl::resource_constructor_exists():
    assert callable(SimplePDL::Resource.__init__)


def test_simplepdl::resource_constructor_args():
    sig = inspect.signature(SimplePDL::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_simplepdl::resource_has_occurrences():
    assert hasattr(SimplePDL::Resource, "occurrences")
    descriptor = None
    for klass in SimplePDL::Resource.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::worksequence_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::WorkSequence)


def test_simplepdl::worksequence_constructor_exists():
    assert callable(SimplePDL::WorkSequence.__init__)


def test_simplepdl::worksequence_constructor_args():
    sig = inspect.signature(SimplePDL::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl::worksequence_has_linkType():
    assert hasattr(SimplePDL::WorkSequence, "linkType")
    descriptor = None
    for klass in SimplePDL::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(SimplePDL::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(SimplePDL::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_simplepdl::workdefinition_has_name():
    assert hasattr(SimplePDL::WorkDefinition, "name")
    descriptor = None
    for klass in SimplePDL::WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::workdefinition_has_maxTime():
    assert hasattr(SimplePDL::WorkDefinition, "maxTime")
    descriptor = None
    for klass in SimplePDL::WorkDefinition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::workdefinition_has_minTime():
    assert hasattr(SimplePDL::WorkDefinition, "minTime")
    descriptor = None
    for klass in SimplePDL::WorkDefinition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::guidance_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::Guidance)


def test_simplepdl::guidance_constructor_exists():
    assert callable(SimplePDL::Guidance.__init__)


def test_simplepdl::guidance_constructor_args():
    sig = inspect.signature(SimplePDL::Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_simplepdl::guidance_has_text():
    assert hasattr(SimplePDL::Guidance, "text")
    descriptor = None
    for klass in SimplePDL::Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::processelement_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::ProcessElement)


def test_simplepdl::processelement_constructor_exists():
    assert callable(SimplePDL::ProcessElement.__init__)


def test_simplepdl::processelement_constructor_args():
    sig = inspect.signature(SimplePDL::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::process_is_not_abstract():
    assert not inspect.isabstract(SimplePDL::Process)


def test_simplepdl::process_constructor_exists():
    assert callable(SimplePDL::Process.__init__)


def test_simplepdl::process_constructor_args():
    sig = inspect.signature(SimplePDL::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_simplepdl::process_has_name():
    assert hasattr(SimplePDL::Process, "name")
    descriptor = None
    for klass in SimplePDL::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_minTime():
    assert hasattr(SimplePDL::Process, "minTime")
    descriptor = None
    for klass in SimplePDL::Process.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_maxTime():
    assert hasattr(SimplePDL::Process, "maxTime")
    descriptor = None
    for klass in SimplePDL::Process.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "startToFinish",
        "finishToFinish",
        "finishToStart",
        "startToStart",
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
SimplePDL::ResourceType_strategy = st.builds(
    SimplePDL::ResourceType,
    name=
        safe_text,
    occurrences=
        st.integers()
)
SimplePDL::Resource_strategy = st.builds(
    SimplePDL::Resource,
    occurrences=
        st.integers()
)
SimplePDL::WorkSequence_strategy = st.builds(
    SimplePDL::WorkSequence,
    linkType=
        safe_text
)
SimplePDL::WorkDefinition_strategy = st.builds(
    SimplePDL::WorkDefinition,
    name=
        safe_text,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
SimplePDL::Guidance_strategy = st.builds(
    SimplePDL::Guidance,
    text=
        safe_text
)
SimplePDL::ProcessElement_strategy = st.builds(
    SimplePDL::ProcessElement,
)
SimplePDL::Process_strategy = st.builds(
    SimplePDL::Process,
    name=
        safe_text,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=SimplePDL::ResourceType_strategy)
@settings(max_examples=50)
def test_simplepdl::resourcetype_instantiation(instance):
    assert isinstance(instance, SimplePDL::ResourceType)

@given(instance=SimplePDL::ResourceType_strategy)
def test_simplepdl::resourcetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplePDL::ResourceType_strategy)
def test_simplepdl::resourcetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePDL::ResourceType_strategy)
def test_simplepdl::resourcetype_occurrences_type(instance):
    assert isinstance(instance.occurrences, int)


@given(instance=SimplePDL::ResourceType_strategy)
def test_simplepdl::resourcetype_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=SimplePDL::Resource_strategy)
@settings(max_examples=50)
def test_simplepdl::resource_instantiation(instance):
    assert isinstance(instance, SimplePDL::Resource)

@given(instance=SimplePDL::Resource_strategy)
def test_simplepdl::resource_occurrences_type(instance):
    assert isinstance(instance.occurrences, int)


@given(instance=SimplePDL::Resource_strategy)
def test_simplepdl::resource_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=SimplePDL::WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl::worksequence_instantiation(instance):
    assert isinstance(instance, SimplePDL::WorkSequence)

@given(instance=SimplePDL::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=SimplePDL::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=SimplePDL::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, SimplePDL::WorkDefinition)

@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=SimplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=SimplePDL::Guidance_strategy)
@settings(max_examples=50)
def test_simplepdl::guidance_instantiation(instance):
    assert isinstance(instance, SimplePDL::Guidance)

@given(instance=SimplePDL::Guidance_strategy)
def test_simplepdl::guidance_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=SimplePDL::Guidance_strategy)
def test_simplepdl::guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SimplePDL::ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl::processelement_instantiation(instance):
    assert isinstance(instance, SimplePDL::ProcessElement)

@given(instance=SimplePDL::Process_strategy)
@settings(max_examples=50)
def test_simplepdl::process_instantiation(instance):
    assert isinstance(instance, SimplePDL::Process)

@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=SimplePDL::Process_strategy)
def test_simplepdl::process_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
