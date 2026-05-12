import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProcessElement,
    simplepdl_RessourceConfig,
    simplepdl_RessourceInstance,
    simplepdl_RessourceDefinition,
    simplepdl_WorkSequence,
    simplepdl_Guidance,
    simplepdl_WorkDefinition,
    simplepdl_ProcessElement,
    simplepdl_Process,
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



def test_simplepdl_ressourceconfig_is_not_abstract():
    assert not inspect.isabstract(simplepdl_RessourceConfig)


def test_simplepdl_ressourceconfig_constructor_exists():
    assert callable(simplepdl_RessourceConfig.__init__)


def test_simplepdl_ressourceconfig_constructor_args():
    sig = inspect.signature(simplepdl_RessourceConfig.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_ressourceconfig_has_name():
    assert hasattr(simplepdl_RessourceConfig, "name")
    descriptor = None
    for klass in simplepdl_RessourceConfig.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_ressourceinstance_is_not_abstract():
    assert not inspect.isabstract(simplepdl_RessourceInstance)


def test_simplepdl_ressourceinstance_constructor_exists():
    assert callable(simplepdl_RessourceInstance.__init__)


def test_simplepdl_ressourceinstance_constructor_args():
    sig = inspect.signature(simplepdl_RessourceInstance.__init__)
    params = list(sig.parameters.keys())
    assert "instances" in params, "Missing parameter 'instances'"

def test_simplepdl_ressourceinstance_has_instances():
    assert hasattr(simplepdl_RessourceInstance, "instances")
    descriptor = None
    for klass in simplepdl_RessourceInstance.__mro__:
        if "instances" in klass.__dict__:
            descriptor = klass.__dict__["instances"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_ressourcedefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl_RessourceDefinition)


def test_simplepdl_ressourcedefinition_constructor_exists():
    assert callable(simplepdl_RessourceDefinition.__init__)


def test_simplepdl_ressourcedefinition_constructor_args():
    sig = inspect.signature(simplepdl_RessourceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_ressourcedefinition_has_number():
    assert hasattr(simplepdl_RessourceDefinition, "number")
    descriptor = None
    for klass in simplepdl_RessourceDefinition.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_ressourcedefinition_has_name():
    assert hasattr(simplepdl_RessourceDefinition, "name")
    descriptor = None
    for klass in simplepdl_RessourceDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_simplepdl_workdefinition_has_max_time():
    assert hasattr(simplepdl_WorkDefinition, "max_time")
    descriptor = None
    for klass in simplepdl_WorkDefinition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_workdefinition_has_name():
    assert hasattr(simplepdl_WorkDefinition, "name")
    descriptor = None
    for klass in simplepdl_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_workdefinition_has_min_time():
    assert hasattr(simplepdl_WorkDefinition, "min_time")
    descriptor = None
    for klass in simplepdl_WorkDefinition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



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
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_process_has_min_time():
    assert hasattr(simplepdl_Process, "min_time")
    descriptor = None
    for klass in simplepdl_Process.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_process_has_max_time():
    assert hasattr(simplepdl_Process, "max_time")
    descriptor = None
    for klass in simplepdl_Process.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_process_has_name():
    assert hasattr(simplepdl_Process, "name")
    descriptor = None
    for klass in simplepdl_Process.__mro__:
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
        "startToStart",
        "startToFinish",
        "finishToFinish",
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
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl_RessourceConfig_strategy = st.builds(
    simplepdl_RessourceConfig,
    name=
        safe_text
)
simplepdl_RessourceInstance_strategy = st.builds(
    simplepdl_RessourceInstance,
    instances=
        st.integers()
)
simplepdl_RessourceDefinition_strategy = st.builds(
    simplepdl_RessourceDefinition,
    number=
        st.integers(),
    name=
        safe_text
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
    max_time=
        st.integers(),
    name=
        safe_text,
    min_time=
        st.integers()
)
simplepdl_ProcessElement_strategy = st.builds(
    simplepdl_ProcessElement,
)
simplepdl_Process_strategy = st.builds(
    simplepdl_Process,
    min_time=
        st.integers(),
    max_time=
        st.integers(),
    name=
        safe_text
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl_RessourceConfig_strategy)
@settings(max_examples=50)
def test_simplepdl_ressourceconfig_instantiation(instance):
    assert isinstance(instance, simplepdl_RessourceConfig)



@given(instance=simplepdl_RessourceConfig_strategy)
def test_simplepdl_ressourceconfig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl_RessourceInstance_strategy)
@settings(max_examples=50)
def test_simplepdl_ressourceinstance_instantiation(instance):
    assert isinstance(instance, simplepdl_RessourceInstance)



@given(instance=simplepdl_RessourceInstance_strategy)
def test_simplepdl_ressourceinstance_instances_setter(instance):
    original = instance.instances
    instance.instances = original
    assert instance.instances == original

@given(instance=simplepdl_RessourceDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_ressourcedefinition_instantiation(instance):
    assert isinstance(instance, simplepdl_RessourceDefinition)



@given(instance=simplepdl_RessourceDefinition_strategy)
def test_simplepdl_ressourcedefinition_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=simplepdl_RessourceDefinition_strategy)
def test_simplepdl_ressourcedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_simplepdl_workdefinition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original



@given(instance=simplepdl_WorkDefinition_strategy)
def test_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simplepdl_WorkDefinition_strategy)
def test_simplepdl_workdefinition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=simplepdl_ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl_processelement_instantiation(instance):
    assert isinstance(instance, simplepdl_ProcessElement)

@given(instance=simplepdl_Process_strategy)
@settings(max_examples=50)
def test_simplepdl_process_instantiation(instance):
    assert isinstance(instance, simplepdl_Process)



@given(instance=simplepdl_Process_strategy)
def test_simplepdl_process_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original



@given(instance=simplepdl_Process_strategy)
def test_simplepdl_process_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original



@given(instance=simplepdl_Process_strategy)
def test_simplepdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
