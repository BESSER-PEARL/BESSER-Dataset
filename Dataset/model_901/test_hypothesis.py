import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iritpdl::Resource,
    iritpdl::ResourceConf,
    ProcessElement,
    iritpdl::WorkSequence,
    iritpdl::WorkDefinition,
    iritpdl::ResourceType,
    iritpdl::Guidance,
    iritpdl::ProcessElement,
    iritpdl::Process,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iritpdl::resource_is_not_abstract():
    assert not inspect.isabstract(iritpdl::Resource)


def test_iritpdl::resource_constructor_exists():
    assert callable(iritpdl::Resource.__init__)


def test_iritpdl::resource_constructor_args():
    sig = inspect.signature(iritpdl::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_iritpdl::resource_has_occurrences():
    assert hasattr(iritpdl::Resource, "occurrences")
    descriptor = None
    for klass in iritpdl::Resource.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl::resourceconf_is_not_abstract():
    assert not inspect.isabstract(iritpdl::ResourceConf)


def test_iritpdl::resourceconf_constructor_exists():
    assert callable(iritpdl::ResourceConf.__init__)


def test_iritpdl::resourceconf_constructor_args():
    sig = inspect.signature(iritpdl::ResourceConf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritpdl::resourceconf_has_name():
    assert hasattr(iritpdl::ResourceConf, "name")
    descriptor = None
    for klass in iritpdl::ResourceConf.__mro__:
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



def test_iritpdl::worksequence_is_not_abstract():
    assert not inspect.isabstract(iritpdl::WorkSequence)


def test_iritpdl::worksequence_constructor_exists():
    assert callable(iritpdl::WorkSequence.__init__)


def test_iritpdl::worksequence_constructor_args():
    sig = inspect.signature(iritpdl::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_iritpdl::worksequence_has_linkType():
    assert hasattr(iritpdl::WorkSequence, "linkType")
    descriptor = None
    for klass in iritpdl::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(iritpdl::WorkDefinition)


def test_iritpdl::workdefinition_constructor_exists():
    assert callable(iritpdl::WorkDefinition.__init__)


def test_iritpdl::workdefinition_constructor_args():
    sig = inspect.signature(iritpdl::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_iritpdl::workdefinition_has_maxTime():
    assert hasattr(iritpdl::WorkDefinition, "maxTime")
    descriptor = None
    for klass in iritpdl::WorkDefinition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl::workdefinition_has_minTime():
    assert hasattr(iritpdl::WorkDefinition, "minTime")
    descriptor = None
    for klass in iritpdl::WorkDefinition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl::workdefinition_has_name():
    assert hasattr(iritpdl::WorkDefinition, "name")
    descriptor = None
    for klass in iritpdl::WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl::resourcetype_is_not_abstract():
    assert not inspect.isabstract(iritpdl::ResourceType)


def test_iritpdl::resourcetype_constructor_exists():
    assert callable(iritpdl::ResourceType.__init__)


def test_iritpdl::resourcetype_constructor_args():
    sig = inspect.signature(iritpdl::ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_iritpdl::resourcetype_has_name():
    assert hasattr(iritpdl::ResourceType, "name")
    descriptor = None
    for klass in iritpdl::ResourceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl::resourcetype_has_occurrences():
    assert hasattr(iritpdl::ResourceType, "occurrences")
    descriptor = None
    for klass in iritpdl::ResourceType.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl::guidance_is_not_abstract():
    assert not inspect.isabstract(iritpdl::Guidance)


def test_iritpdl::guidance_constructor_exists():
    assert callable(iritpdl::Guidance.__init__)


def test_iritpdl::guidance_constructor_args():
    sig = inspect.signature(iritpdl::Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_iritpdl::guidance_has_text():
    assert hasattr(iritpdl::Guidance, "text")
    descriptor = None
    for klass in iritpdl::Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl::processelement_is_not_abstract():
    assert not inspect.isabstract(iritpdl::ProcessElement)


def test_iritpdl::processelement_constructor_exists():
    assert callable(iritpdl::ProcessElement.__init__)


def test_iritpdl::processelement_constructor_args():
    sig = inspect.signature(iritpdl::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_iritpdl::process_is_not_abstract():
    assert not inspect.isabstract(iritpdl::Process)


def test_iritpdl::process_constructor_exists():
    assert callable(iritpdl::Process.__init__)


def test_iritpdl::process_constructor_args():
    sig = inspect.signature(iritpdl::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_iritpdl::process_has_name():
    assert hasattr(iritpdl::Process, "name")
    descriptor = None
    for klass in iritpdl::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl::process_has_minTime():
    assert hasattr(iritpdl::Process, "minTime")
    descriptor = None
    for klass in iritpdl::Process.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl::process_has_maxTime():
    assert hasattr(iritpdl::Process, "maxTime")
    descriptor = None
    for klass in iritpdl::Process.__mro__:
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
iritpdl::Resource_strategy = st.builds(
    iritpdl::Resource,
    occurrences=
        st.integers()
)
iritpdl::ResourceConf_strategy = st.builds(
    iritpdl::ResourceConf,
    name=
        safe_text
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
iritpdl::WorkSequence_strategy = st.builds(
    iritpdl::WorkSequence,
    linkType=
        safe_text
)
iritpdl::WorkDefinition_strategy = st.builds(
    iritpdl::WorkDefinition,
    maxTime=
        st.integers(),
    minTime=
        st.integers(),
    name=
        safe_text
)
iritpdl::ResourceType_strategy = st.builds(
    iritpdl::ResourceType,
    name=
        safe_text,
    occurrences=
        st.integers()
)
iritpdl::Guidance_strategy = st.builds(
    iritpdl::Guidance,
    text=
        safe_text
)
iritpdl::ProcessElement_strategy = st.builds(
    iritpdl::ProcessElement,
)
iritpdl::Process_strategy = st.builds(
    iritpdl::Process,
    name=
        safe_text,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)

@given(instance=iritpdl::Resource_strategy)
@settings(max_examples=50)
def test_iritpdl::resource_instantiation(instance):
    assert isinstance(instance, iritpdl::Resource)

@given(instance=iritpdl::Resource_strategy)
def test_iritpdl::resource_occurrences_type(instance):
    assert isinstance(instance.occurrences, int)


@given(instance=iritpdl::Resource_strategy)
def test_iritpdl::resource_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=iritpdl::ResourceConf_strategy)
@settings(max_examples=50)
def test_iritpdl::resourceconf_instantiation(instance):
    assert isinstance(instance, iritpdl::ResourceConf)

@given(instance=iritpdl::ResourceConf_strategy)
def test_iritpdl::resourceconf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritpdl::ResourceConf_strategy)
def test_iritpdl::resourceconf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=iritpdl::WorkSequence_strategy)
@settings(max_examples=50)
def test_iritpdl::worksequence_instantiation(instance):
    assert isinstance(instance, iritpdl::WorkSequence)

@given(instance=iritpdl::WorkSequence_strategy)
def test_iritpdl::worksequence_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=iritpdl::WorkSequence_strategy)
def test_iritpdl::worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=iritpdl::WorkDefinition_strategy)
@settings(max_examples=50)
def test_iritpdl::workdefinition_instantiation(instance):
    assert isinstance(instance, iritpdl::WorkDefinition)

@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritpdl::WorkDefinition_strategy)
def test_iritpdl::workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritpdl::ResourceType_strategy)
@settings(max_examples=50)
def test_iritpdl::resourcetype_instantiation(instance):
    assert isinstance(instance, iritpdl::ResourceType)

@given(instance=iritpdl::ResourceType_strategy)
def test_iritpdl::resourcetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritpdl::ResourceType_strategy)
def test_iritpdl::resourcetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritpdl::ResourceType_strategy)
def test_iritpdl::resourcetype_occurrences_type(instance):
    assert isinstance(instance.occurrences, int)


@given(instance=iritpdl::ResourceType_strategy)
def test_iritpdl::resourcetype_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=iritpdl::Guidance_strategy)
@settings(max_examples=50)
def test_iritpdl::guidance_instantiation(instance):
    assert isinstance(instance, iritpdl::Guidance)

@given(instance=iritpdl::Guidance_strategy)
def test_iritpdl::guidance_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=iritpdl::Guidance_strategy)
def test_iritpdl::guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=iritpdl::ProcessElement_strategy)
@settings(max_examples=50)
def test_iritpdl::processelement_instantiation(instance):
    assert isinstance(instance, iritpdl::ProcessElement)

@given(instance=iritpdl::Process_strategy)
@settings(max_examples=50)
def test_iritpdl::process_instantiation(instance):
    assert isinstance(instance, iritpdl::Process)

@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=iritpdl::Process_strategy)
def test_iritpdl::process_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
