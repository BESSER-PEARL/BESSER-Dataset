import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Activities,
    simplepdl_WorkDefinition,
    simplepdl_SubWorkDefinition,
    Parameter,
    simplepdl_ParameterWD,
    simplepdl_ParameterSWD,
    ProcessElement,
    simplepdl_Activities,
    simplepdl_WorkSequence,
    simplepdl_Parameter,
    simplepdl_Guidance,
    simplepdl_Resource,
    simplepdl_ProcessElement,
    simplepdl_Process,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activities_is_not_abstract():
    assert not inspect.isabstract(Activities)


def test_activities_constructor_exists():
    assert callable(Activities.__init__)


def test_activities_constructor_args():
    sig = inspect.signature(Activities.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl_WorkDefinition)


def test_simplepdl_workdefinition_constructor_exists():
    assert callable(simplepdl_WorkDefinition.__init__)


def test_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(simplepdl_WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_subworkdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl_SubWorkDefinition)


def test_simplepdl_subworkdefinition_constructor_exists():
    assert callable(simplepdl_SubWorkDefinition.__init__)


def test_simplepdl_subworkdefinition_constructor_args():
    sig = inspect.signature(simplepdl_SubWorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_parameterwd_is_not_abstract():
    assert not inspect.isabstract(simplepdl_ParameterWD)


def test_simplepdl_parameterwd_constructor_exists():
    assert callable(simplepdl_ParameterWD.__init__)


def test_simplepdl_parameterwd_constructor_args():
    sig = inspect.signature(simplepdl_ParameterWD.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_parameterswd_is_not_abstract():
    assert not inspect.isabstract(simplepdl_ParameterSWD)


def test_simplepdl_parameterswd_constructor_exists():
    assert callable(simplepdl_ParameterSWD.__init__)


def test_simplepdl_parameterswd_constructor_args():
    sig = inspect.signature(simplepdl_ParameterSWD.__init__)
    params = list(sig.parameters.keys())



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_activities_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Activities)


def test_simplepdl_activities_constructor_exists():
    assert callable(simplepdl_Activities.__init__)


def test_simplepdl_activities_constructor_args():
    sig = inspect.signature(simplepdl_Activities.__init__)
    params = list(sig.parameters.keys())
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_simplepdl_activities_has_max_time():
    assert hasattr(simplepdl_Activities, "max_time")
    descriptor = None
    for klass in simplepdl_Activities.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_activities_has_name():
    assert hasattr(simplepdl_Activities, "name")
    descriptor = None
    for klass in simplepdl_Activities.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_activities_has_min_time():
    assert hasattr(simplepdl_Activities, "min_time")
    descriptor = None
    for klass in simplepdl_Activities.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
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
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_worksequence_has_linkType():
    assert hasattr(simplepdl_WorkSequence, "linkType")
    descriptor = None
    for klass in simplepdl_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_worksequence_has_name():
    assert hasattr(simplepdl_WorkSequence, "name")
    descriptor = None
    for klass in simplepdl_WorkSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_parameter_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Parameter)


def test_simplepdl_parameter_constructor_exists():
    assert callable(simplepdl_Parameter.__init__)


def test_simplepdl_parameter_constructor_args():
    sig = inspect.signature(simplepdl_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "nbNeeds" in params, "Missing parameter 'nbNeeds'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_parameter_has_nbNeeds():
    assert hasattr(simplepdl_Parameter, "nbNeeds")
    descriptor = None
    for klass in simplepdl_Parameter.__mro__:
        if "nbNeeds" in klass.__dict__:
            descriptor = klass.__dict__["nbNeeds"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_parameter_has_name():
    assert hasattr(simplepdl_Parameter, "name")
    descriptor = None
    for klass in simplepdl_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_simplepdl_resource_is_not_abstract():
    assert not inspect.isabstract(simplepdl_Resource)


def test_simplepdl_resource_constructor_exists():
    assert callable(simplepdl_Resource.__init__)


def test_simplepdl_resource_constructor_args():
    sig = inspect.signature(simplepdl_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_resource_has_marking():
    assert hasattr(simplepdl_Resource, "marking")
    descriptor = None
    for klass in simplepdl_Resource.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl_resource_has_name():
    assert hasattr(simplepdl_Resource, "name")
    descriptor = None
    for klass in simplepdl_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min_time" in params, "Missing parameter 'min_time'"

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

def test_simplepdl_process_has_min_time():
    assert hasattr(simplepdl_Process, "min_time")
    descriptor = None
    for klass in simplepdl_Process.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
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
Activities_strategy = st.builds(
    Activities,
)
simplepdl_WorkDefinition_strategy = st.builds(
    simplepdl_WorkDefinition,
)
simplepdl_SubWorkDefinition_strategy = st.builds(
    simplepdl_SubWorkDefinition,
)
Parameter_strategy = st.builds(
    Parameter,
)
simplepdl_ParameterWD_strategy = st.builds(
    simplepdl_ParameterWD,
)
simplepdl_ParameterSWD_strategy = st.builds(
    simplepdl_ParameterSWD,
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl_Activities_strategy = st.builds(
    simplepdl_Activities,
    max_time=
        st.integers(),
    name=
        safe_text,
    min_time=
        st.integers()
)
simplepdl_WorkSequence_strategy = st.builds(
    simplepdl_WorkSequence,
    linkType=
        safe_text,
    name=
        safe_text
)
simplepdl_Parameter_strategy = st.builds(
    simplepdl_Parameter,
    nbNeeds=
        st.integers(),
    name=
        safe_text
)
simplepdl_Guidance_strategy = st.builds(
    simplepdl_Guidance,
    text=
        safe_text
)
simplepdl_Resource_strategy = st.builds(
    simplepdl_Resource,
    marking=
        st.integers(),
    name=
        safe_text
)
simplepdl_ProcessElement_strategy = st.builds(
    simplepdl_ProcessElement,
)
simplepdl_Process_strategy = st.builds(
    simplepdl_Process,
    max_time=
        st.integers(),
    name=
        safe_text,
    min_time=
        st.integers()
)

@given(instance=Activities_strategy)
@settings(max_examples=50)
def test_activities_instantiation(instance):
    assert isinstance(instance, Activities)

@given(instance=simplepdl_WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkDefinition)

@given(instance=simplepdl_SubWorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_subworkdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl_SubWorkDefinition)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=simplepdl_ParameterWD_strategy)
@settings(max_examples=50)
def test_simplepdl_parameterwd_instantiation(instance):
    assert isinstance(instance, simplepdl_ParameterWD)

@given(instance=simplepdl_ParameterSWD_strategy)
@settings(max_examples=50)
def test_simplepdl_parameterswd_instantiation(instance):
    assert isinstance(instance, simplepdl_ParameterSWD)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl_Activities_strategy)
@settings(max_examples=50)
def test_simplepdl_activities_instantiation(instance):
    assert isinstance(instance, simplepdl_Activities)



@given(instance=simplepdl_Activities_strategy)
def test_simplepdl_activities_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original



@given(instance=simplepdl_Activities_strategy)
def test_simplepdl_activities_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simplepdl_Activities_strategy)
def test_simplepdl_activities_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=simplepdl_WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl_worksequence_instantiation(instance):
    assert isinstance(instance, simplepdl_WorkSequence)



@given(instance=simplepdl_WorkSequence_strategy)
def test_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original



@given(instance=simplepdl_WorkSequence_strategy)
def test_simplepdl_worksequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl_Parameter_strategy)
@settings(max_examples=50)
def test_simplepdl_parameter_instantiation(instance):
    assert isinstance(instance, simplepdl_Parameter)



@given(instance=simplepdl_Parameter_strategy)
def test_simplepdl_parameter_nbNeeds_setter(instance):
    original = instance.nbNeeds
    instance.nbNeeds = original
    assert instance.nbNeeds == original



@given(instance=simplepdl_Parameter_strategy)
def test_simplepdl_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl_Guidance_strategy)
@settings(max_examples=50)
def test_simplepdl_guidance_instantiation(instance):
    assert isinstance(instance, simplepdl_Guidance)



@given(instance=simplepdl_Guidance_strategy)
def test_simplepdl_guidance_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=simplepdl_Resource_strategy)
@settings(max_examples=50)
def test_simplepdl_resource_instantiation(instance):
    assert isinstance(instance, simplepdl_Resource)



@given(instance=simplepdl_Resource_strategy)
def test_simplepdl_resource_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original



@given(instance=simplepdl_Resource_strategy)
def test_simplepdl_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl_ProcessElement_strategy)
@settings(max_examples=50)
def test_simplepdl_processelement_instantiation(instance):
    assert isinstance(instance, simplepdl_ProcessElement)

@given(instance=simplepdl_Process_strategy)
@settings(max_examples=50)
def test_simplepdl_process_instantiation(instance):
    assert isinstance(instance, simplepdl_Process)



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



@given(instance=simplepdl_Process_strategy)
def test_simplepdl_process_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original
