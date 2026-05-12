import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProcessElement,
    SimplePDL_Resource,
    SimplePDL_ResourceType,
    SimplePDL_WorkSequence,
    SimplePDL_WorkDefinition,
    SimplePDL_Guidance,
    SimplePDL_ProcessElement,
    SimplePDL_Process,
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



def test_simplepdl_resource_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Resource)


def test_simplepdl_resource_constructor_exists():
    assert callable(SimplePDL_Resource.__init__)


def test_simplepdl_resource_constructor_args():
    sig = inspect.signature(SimplePDL_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_simplepdl_resource_has_occurrences():
    assert hasattr(SimplePDL_Resource, "occurrences")
    descriptor = None
    for klass in SimplePDL_Resource.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_resourcetype_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_ResourceType)


def test_simplepdl_resourcetype_constructor_exists():
    assert callable(SimplePDL_ResourceType.__init__)


def test_simplepdl_resourcetype_constructor_args():
    sig = inspect.signature(SimplePDL_ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_resourcetype_has_occurrences():
    assert hasattr(SimplePDL_ResourceType, "occurrences")
    descriptor = None
    for klass in SimplePDL_ResourceType.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_resourcetype_has_name():
    assert hasattr(SimplePDL_ResourceType, "name")
    descriptor = None
    for klass in SimplePDL_ResourceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_WorkSequence)


def test_simplepdl_worksequence_constructor_exists():
    assert callable(SimplePDL_WorkSequence.__init__)


def test_simplepdl_worksequence_constructor_args():
    sig = inspect.signature(SimplePDL_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl_worksequence_has_linkType():
    assert hasattr(SimplePDL_WorkSequence, "linkType")
    descriptor = None
    for klass in SimplePDL_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_WorkDefinition)


def test_simplepdl_workdefinition_constructor_exists():
    assert callable(SimplePDL_WorkDefinition.__init__)


def test_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(SimplePDL_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_workdefinition_has_maxTime():
    assert hasattr(SimplePDL_WorkDefinition, "maxTime")
    descriptor = None
    for klass in SimplePDL_WorkDefinition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_workdefinition_has_minTime():
    assert hasattr(SimplePDL_WorkDefinition, "minTime")
    descriptor = None
    for klass in SimplePDL_WorkDefinition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_workdefinition_has_name():
    assert hasattr(SimplePDL_WorkDefinition, "name")
    descriptor = None
    for klass in SimplePDL_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_guidance_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Guidance)


def test_simplepdl_guidance_constructor_exists():
    assert callable(SimplePDL_Guidance.__init__)


def test_simplepdl_guidance_constructor_args():
    sig = inspect.signature(SimplePDL_Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_simplepdl_guidance_has_text():
    assert hasattr(SimplePDL_Guidance, "text")
    descriptor = None
    for klass in SimplePDL_Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_processelement_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_ProcessElement)


def test_simplepdl_processelement_constructor_exists():
    assert callable(SimplePDL_ProcessElement.__init__)


def test_simplepdl_processelement_constructor_args():
    sig = inspect.signature(SimplePDL_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_process_is_not_abstract():
    assert not inspect.isabstract(SimplePDL_Process)


def test_simplepdl_process_constructor_exists():
    assert callable(SimplePDL_Process.__init__)


def test_simplepdl_process_constructor_args():
    sig = inspect.signature(SimplePDL_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_simplepdl_process_has_name():
    assert hasattr(SimplePDL_Process, "name")
    descriptor = None
    for klass in SimplePDL_Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_process_has_minTime():
    assert hasattr(SimplePDL_Process, "minTime")
    descriptor = None
    for klass in SimplePDL_Process.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_process_has_maxTime():
    assert hasattr(SimplePDL_Process, "maxTime")
    descriptor = None
    for klass in SimplePDL_Process.__mro__:
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
        "finishToFinish",
        "finishToStart",
        "startToFinish",
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
SimplePDL_Resource_strategy = st.builds(
    SimplePDL_Resource,
    occurrences=
        st.integers()
)
SimplePDL_ResourceType_strategy = st.builds(
    SimplePDL_ResourceType,
    occurrences=
        st.integers(),
    name=
        safe_text
)
SimplePDL_WorkSequence_strategy = st.builds(
    SimplePDL_WorkSequence,
    linkType=
        safe_text
)
SimplePDL_WorkDefinition_strategy = st.builds(
    SimplePDL_WorkDefinition,
    maxTime=
        st.integers(),
    minTime=
        st.integers(),
    name=
        safe_text
)
SimplePDL_Guidance_strategy = st.builds(
    SimplePDL_Guidance,
    text=
        safe_text
)
SimplePDL_ProcessElement_strategy = st.builds(
    SimplePDL_ProcessElement,
)
SimplePDL_Process_strategy = st.builds(
    SimplePDL_Process,
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

@given(instance=SimplePDL_Resource_strategy)
@settings(max_examples=50)
def test_simplepdl_resource_instantiation(instance):
    assert isinstance(instance, SimplePDL_Resource)



@given(instance=SimplePDL_Resource_strategy)
def test_simplepdl_resource_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=SimplePDL_ResourceType_strategy)
@settings(max_examples=50)
def test_simplepdl_resourcetype_instantiation(instance):
    assert isinstance(instance, SimplePDL_ResourceType)



@given(instance=SimplePDL_ResourceType_strategy)
def test_simplepdl_resourcetype_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original



@given(instance=SimplePDL_ResourceType_strategy)
def test_simplepdl_resourcetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePDL_WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl_worksequence_instantiation(instance):
    assert isinstance(instance, SimplePDL_WorkSequence)



@given(instance=SimplePDL_WorkSequence_strategy)
def test_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=SimplePDL_WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_workdefinition_instantiation(instance):
    assert isinstance(instance, SimplePDL_WorkDefinition)



@given(instance=SimplePDL_WorkDefinition_strategy)
def test_simplepdl_workdefinition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=SimplePDL_WorkDefinition_strategy)
def test_simplepdl_workdefinition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=SimplePDL_WorkDefinition_strategy)
def test_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplePDL_Guidance_strategy)
@settings(max_examples=50)
def test_simplepdl_guidance_instantiation(instance):
    assert isinstance(instance, SimplePDL_Guidance)



@given(instance=SimplePDL_Guidance_strategy)
def test_simplepdl_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SimplePDL_ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl_processelement_instantiation(instance):
    assert isinstance(instance, SimplePDL_ProcessElement)

@given(instance=SimplePDL_Process_strategy)
@settings(max_examples=50)
def test_simplepdl_process_instantiation(instance):
    assert isinstance(instance, SimplePDL_Process)



@given(instance=SimplePDL_Process_strategy)
def test_simplepdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimplePDL_Process_strategy)
def test_simplepdl_process_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=SimplePDL_Process_strategy)
def test_simplepdl_process_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original
