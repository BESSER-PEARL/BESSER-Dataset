import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iritpdl_Resource,
    iritpdl_ResourceConf,
    ProcessElement,
    iritpdl_WorkSequence,
    iritpdl_WorkDefinition,
    iritpdl_ResourceType,
    iritpdl_Guidance,
    iritpdl_ProcessElement,
    iritpdl_Process,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iritpdl_resource_is_not_abstract():
    assert not inspect.isabstract(iritpdl_Resource)


def test_iritpdl_resource_constructor_exists():
    assert callable(iritpdl_Resource.__init__)


def test_iritpdl_resource_constructor_args():
    sig = inspect.signature(iritpdl_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"

def test_iritpdl_resource_has_occurrences():
    assert hasattr(iritpdl_Resource, "occurrences")
    descriptor = None
    for klass in iritpdl_Resource.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl_resourceconf_is_not_abstract():
    assert not inspect.isabstract(iritpdl_ResourceConf)


def test_iritpdl_resourceconf_constructor_exists():
    assert callable(iritpdl_ResourceConf.__init__)


def test_iritpdl_resourceconf_constructor_args():
    sig = inspect.signature(iritpdl_ResourceConf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iritpdl_resourceconf_has_name():
    assert hasattr(iritpdl_ResourceConf, "name")
    descriptor = None
    for klass in iritpdl_ResourceConf.__mro__:
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



def test_iritpdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(iritpdl_WorkSequence)


def test_iritpdl_worksequence_constructor_exists():
    assert callable(iritpdl_WorkSequence.__init__)


def test_iritpdl_worksequence_constructor_args():
    sig = inspect.signature(iritpdl_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_iritpdl_worksequence_has_linkType():
    assert hasattr(iritpdl_WorkSequence, "linkType")
    descriptor = None
    for klass in iritpdl_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(iritpdl_WorkDefinition)


def test_iritpdl_workdefinition_constructor_exists():
    assert callable(iritpdl_WorkDefinition.__init__)


def test_iritpdl_workdefinition_constructor_args():
    sig = inspect.signature(iritpdl_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_iritpdl_workdefinition_has_minTime():
    assert hasattr(iritpdl_WorkDefinition, "minTime")
    descriptor = None
    for klass in iritpdl_WorkDefinition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl_workdefinition_has_name():
    assert hasattr(iritpdl_WorkDefinition, "name")
    descriptor = None
    for klass in iritpdl_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl_workdefinition_has_maxTime():
    assert hasattr(iritpdl_WorkDefinition, "maxTime")
    descriptor = None
    for klass in iritpdl_WorkDefinition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl_resourcetype_is_not_abstract():
    assert not inspect.isabstract(iritpdl_ResourceType)


def test_iritpdl_resourcetype_constructor_exists():
    assert callable(iritpdl_ResourceType.__init__)


def test_iritpdl_resourcetype_constructor_args():
    sig = inspect.signature(iritpdl_ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "occurrences" in params, "Missing parameter 'occurrences'"
    assert "name" in params, "Missing parameter 'name'"

def test_iritpdl_resourcetype_has_occurrences():
    assert hasattr(iritpdl_ResourceType, "occurrences")
    descriptor = None
    for klass in iritpdl_ResourceType.__mro__:
        if "occurrences" in klass.__dict__:
            descriptor = klass.__dict__["occurrences"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl_resourcetype_has_name():
    assert hasattr(iritpdl_ResourceType, "name")
    descriptor = None
    for klass in iritpdl_ResourceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl_guidance_is_not_abstract():
    assert not inspect.isabstract(iritpdl_Guidance)


def test_iritpdl_guidance_constructor_exists():
    assert callable(iritpdl_Guidance.__init__)


def test_iritpdl_guidance_constructor_args():
    sig = inspect.signature(iritpdl_Guidance.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_iritpdl_guidance_has_text():
    assert hasattr(iritpdl_Guidance, "text")
    descriptor = None
    for klass in iritpdl_Guidance.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_iritpdl_processelement_is_not_abstract():
    assert not inspect.isabstract(iritpdl_ProcessElement)


def test_iritpdl_processelement_constructor_exists():
    assert callable(iritpdl_ProcessElement.__init__)


def test_iritpdl_processelement_constructor_args():
    sig = inspect.signature(iritpdl_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_iritpdl_process_is_not_abstract():
    assert not inspect.isabstract(iritpdl_Process)


def test_iritpdl_process_constructor_exists():
    assert callable(iritpdl_Process.__init__)


def test_iritpdl_process_constructor_args():
    sig = inspect.signature(iritpdl_Process.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_iritpdl_process_has_maxTime():
    assert hasattr(iritpdl_Process, "maxTime")
    descriptor = None
    for klass in iritpdl_Process.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl_process_has_minTime():
    assert hasattr(iritpdl_Process, "minTime")
    descriptor = None
    for klass in iritpdl_Process.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_iritpdl_process_has_name():
    assert hasattr(iritpdl_Process, "name")
    descriptor = None
    for klass in iritpdl_Process.__mro__:
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
        "startToFinish",
        "finishToFinish",
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
iritpdl_Resource_strategy = st.builds(
    iritpdl_Resource,
    occurrences=
        st.integers()
)
iritpdl_ResourceConf_strategy = st.builds(
    iritpdl_ResourceConf,
    name=
        safe_text
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
iritpdl_WorkSequence_strategy = st.builds(
    iritpdl_WorkSequence,
    linkType=
        safe_text
)
iritpdl_WorkDefinition_strategy = st.builds(
    iritpdl_WorkDefinition,
    minTime=
        st.integers(),
    name=
        safe_text,
    maxTime=
        st.integers()
)
iritpdl_ResourceType_strategy = st.builds(
    iritpdl_ResourceType,
    occurrences=
        st.integers(),
    name=
        safe_text
)
iritpdl_Guidance_strategy = st.builds(
    iritpdl_Guidance,
    text=
        safe_text
)
iritpdl_ProcessElement_strategy = st.builds(
    iritpdl_ProcessElement,
)
iritpdl_Process_strategy = st.builds(
    iritpdl_Process,
    maxTime=
        st.integers(),
    minTime=
        st.integers(),
    name=
        safe_text
)

@given(instance=iritpdl_Resource_strategy)
@settings(max_examples=50)
def test_iritpdl_resource_instantiation(instance):
    assert isinstance(instance, iritpdl_Resource)



@given(instance=iritpdl_Resource_strategy)
def test_iritpdl_resource_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original

@given(instance=iritpdl_ResourceConf_strategy)
@settings(max_examples=50)
def test_iritpdl_resourceconf_instantiation(instance):
    assert isinstance(instance, iritpdl_ResourceConf)



@given(instance=iritpdl_ResourceConf_strategy)
def test_iritpdl_resourceconf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=iritpdl_WorkSequence_strategy)
@settings(max_examples=50)
def test_iritpdl_worksequence_instantiation(instance):
    assert isinstance(instance, iritpdl_WorkSequence)



@given(instance=iritpdl_WorkSequence_strategy)
def test_iritpdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=iritpdl_WorkDefinition_strategy)
@settings(max_examples=50)
def test_iritpdl_workdefinition_instantiation(instance):
    assert isinstance(instance, iritpdl_WorkDefinition)



@given(instance=iritpdl_WorkDefinition_strategy)
def test_iritpdl_workdefinition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=iritpdl_WorkDefinition_strategy)
def test_iritpdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iritpdl_WorkDefinition_strategy)
def test_iritpdl_workdefinition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=iritpdl_ResourceType_strategy)
@settings(max_examples=50)
def test_iritpdl_resourcetype_instantiation(instance):
    assert isinstance(instance, iritpdl_ResourceType)



@given(instance=iritpdl_ResourceType_strategy)
def test_iritpdl_resourcetype_occurrences_setter(instance):
    original = instance.occurrences
    instance.occurrences = original
    assert instance.occurrences == original



@given(instance=iritpdl_ResourceType_strategy)
def test_iritpdl_resourcetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iritpdl_Guidance_strategy)
@settings(max_examples=50)
def test_iritpdl_guidance_instantiation(instance):
    assert isinstance(instance, iritpdl_Guidance)



@given(instance=iritpdl_Guidance_strategy)
def test_iritpdl_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=iritpdl_ProcessElement_strategy)
@settings(max_examples=50)
def test_iritpdl_processelement_instantiation(instance):
    assert isinstance(instance, iritpdl_ProcessElement)

@given(instance=iritpdl_Process_strategy)
@settings(max_examples=50)
def test_iritpdl_process_instantiation(instance):
    assert isinstance(instance, iritpdl_Process)



@given(instance=iritpdl_Process_strategy)
def test_iritpdl_process_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=iritpdl_Process_strategy)
def test_iritpdl_process_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=iritpdl_Process_strategy)
def test_iritpdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
