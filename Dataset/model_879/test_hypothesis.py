import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Activities,
    simplepdl::WorkDefinition,
    simplepdl::SubWorkDefinition,
    Parameter,
    simplepdl::ParameterWD,
    simplepdl::ParameterSWD,
    ProcessElement,
    simplepdl::Activities,
    simplepdl::WorkSequence,
    simplepdl::Parameter,
    simplepdl::Guidance,
    simplepdl::Resource,
    simplepdl::ProcessElement,
    simplepdl::Process,
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



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(simplepdl::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(simplepdl::WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::subworkdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::SubWorkDefinition)


def test_simplepdl::subworkdefinition_constructor_exists():
    assert callable(simplepdl::SubWorkDefinition.__init__)


def test_simplepdl::subworkdefinition_constructor_args():
    sig = inspect.signature(simplepdl::SubWorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::parameterwd_is_not_abstract():
    assert not inspect.isabstract(simplepdl::ParameterWD)


def test_simplepdl::parameterwd_constructor_exists():
    assert callable(simplepdl::ParameterWD.__init__)


def test_simplepdl::parameterwd_constructor_args():
    sig = inspect.signature(simplepdl::ParameterWD.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::parameterswd_is_not_abstract():
    assert not inspect.isabstract(simplepdl::ParameterSWD)


def test_simplepdl::parameterswd_constructor_exists():
    assert callable(simplepdl::ParameterSWD.__init__)


def test_simplepdl::parameterswd_constructor_args():
    sig = inspect.signature(simplepdl::ParameterSWD.__init__)
    params = list(sig.parameters.keys())



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::activities_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Activities)


def test_simplepdl::activities_constructor_exists():
    assert callable(simplepdl::Activities.__init__)


def test_simplepdl::activities_constructor_args():
    sig = inspect.signature(simplepdl::Activities.__init__)
    params = list(sig.parameters.keys())
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_simplepdl::activities_has_max_time():
    assert hasattr(simplepdl::Activities, "max_time")
    descriptor = None
    for klass in simplepdl::Activities.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::activities_has_name():
    assert hasattr(simplepdl::Activities, "name")
    descriptor = None
    for klass in simplepdl::Activities.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::activities_has_min_time():
    assert hasattr(simplepdl::Activities, "min_time")
    descriptor = None
    for klass in simplepdl::Activities.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::worksequence_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkSequence)


def test_simplepdl::worksequence_constructor_exists():
    assert callable(simplepdl::WorkSequence.__init__)


def test_simplepdl::worksequence_constructor_args():
    sig = inspect.signature(simplepdl::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::worksequence_has_linkType():
    assert hasattr(simplepdl::WorkSequence, "linkType")
    descriptor = None
    for klass in simplepdl::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::worksequence_has_name():
    assert hasattr(simplepdl::WorkSequence, "name")
    descriptor = None
    for klass in simplepdl::WorkSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::parameter_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Parameter)


def test_simplepdl::parameter_constructor_exists():
    assert callable(simplepdl::Parameter.__init__)


def test_simplepdl::parameter_constructor_args():
    sig = inspect.signature(simplepdl::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "nbNeeds" in params, "Missing parameter 'nbNeeds'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::parameter_has_nbNeeds():
    assert hasattr(simplepdl::Parameter, "nbNeeds")
    descriptor = None
    for klass in simplepdl::Parameter.__mro__:
        if "nbNeeds" in klass.__dict__:
            descriptor = klass.__dict__["nbNeeds"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::parameter_has_name():
    assert hasattr(simplepdl::Parameter, "name")
    descriptor = None
    for klass in simplepdl::Parameter.__mro__:
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



def test_simplepdl::resource_is_not_abstract():
    assert not inspect.isabstract(simplepdl::Resource)


def test_simplepdl::resource_constructor_exists():
    assert callable(simplepdl::Resource.__init__)


def test_simplepdl::resource_constructor_args():
    sig = inspect.signature(simplepdl::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "marking" in params, "Missing parameter 'marking'"

def test_simplepdl::resource_has_name():
    assert hasattr(simplepdl::Resource, "name")
    descriptor = None
    for klass in simplepdl::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::resource_has_marking():
    assert hasattr(simplepdl::Resource, "marking")
    descriptor = None
    for klass in simplepdl::Resource.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
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
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_simplepdl::process_has_name():
    assert hasattr(simplepdl::Process, "name")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_max_time():
    assert hasattr(simplepdl::Process, "max_time")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::process_has_min_time():
    assert hasattr(simplepdl::Process, "min_time")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
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
        "finishToStart",
        "startToFinish",
        "finishToFinish",
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
Activities_strategy = st.builds(
    Activities,
)
simplepdl::WorkDefinition_strategy = st.builds(
    simplepdl::WorkDefinition,
)
simplepdl::SubWorkDefinition_strategy = st.builds(
    simplepdl::SubWorkDefinition,
)
Parameter_strategy = st.builds(
    Parameter,
)
simplepdl::ParameterWD_strategy = st.builds(
    simplepdl::ParameterWD,
)
simplepdl::ParameterSWD_strategy = st.builds(
    simplepdl::ParameterSWD,
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
simplepdl::Activities_strategy = st.builds(
    simplepdl::Activities,
    max_time=
        st.integers(),
    name=
        safe_text,
    min_time=
        st.integers()
)
simplepdl::WorkSequence_strategy = st.builds(
    simplepdl::WorkSequence,
    linkType=
        safe_text,
    name=
        safe_text
)
simplepdl::Parameter_strategy = st.builds(
    simplepdl::Parameter,
    nbNeeds=
        st.integers(),
    name=
        safe_text
)
simplepdl::Guidance_strategy = st.builds(
    simplepdl::Guidance,
    text=
        safe_text
)
simplepdl::Resource_strategy = st.builds(
    simplepdl::Resource,
    name=
        safe_text,
    marking=
        st.integers()
)
simplepdl::ProcessElement_strategy = st.builds(
    simplepdl::ProcessElement,
)
simplepdl::Process_strategy = st.builds(
    simplepdl::Process,
    name=
        safe_text,
    max_time=
        st.integers(),
    min_time=
        st.integers()
)

@given(instance=Activities_strategy)
@settings(max_examples=50)
def test_activities_instantiation(instance):
    assert isinstance(instance, Activities)

@given(instance=simplepdl::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::WorkDefinition)

@given(instance=simplepdl::SubWorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::subworkdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::SubWorkDefinition)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=simplepdl::ParameterWD_strategy)
@settings(max_examples=50)
def test_simplepdl::parameterwd_instantiation(instance):
    assert isinstance(instance, simplepdl::ParameterWD)

@given(instance=simplepdl::ParameterSWD_strategy)
@settings(max_examples=50)
def test_simplepdl::parameterswd_instantiation(instance):
    assert isinstance(instance, simplepdl::ParameterSWD)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=simplepdl::Activities_strategy)
@settings(max_examples=50)
def test_simplepdl::activities_instantiation(instance):
    assert isinstance(instance, simplepdl::Activities)

@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::Activities_strategy)
def test_simplepdl::activities_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

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

@given(instance=simplepdl::WorkSequence_strategy)
def test_simplepdl::worksequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::WorkSequence_strategy)
def test_simplepdl::worksequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::Parameter_strategy)
@settings(max_examples=50)
def test_simplepdl::parameter_instantiation(instance):
    assert isinstance(instance, simplepdl::Parameter)

@given(instance=simplepdl::Parameter_strategy)
def test_simplepdl::parameter_nbNeeds_type(instance):
    assert isinstance(instance.nbNeeds, int)


@given(instance=simplepdl::Parameter_strategy)
def test_simplepdl::parameter_nbNeeds_setter(instance):
    original = instance.nbNeeds
    instance.nbNeeds = original
    assert instance.nbNeeds == original

@given(instance=simplepdl::Parameter_strategy)
def test_simplepdl::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Parameter_strategy)
def test_simplepdl::parameter_name_setter(instance):
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

@given(instance=simplepdl::Resource_strategy)
@settings(max_examples=50)
def test_simplepdl::resource_instantiation(instance):
    assert isinstance(instance, simplepdl::Resource)

@given(instance=simplepdl::Resource_strategy)
def test_simplepdl::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::Resource_strategy)
def test_simplepdl::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::Resource_strategy)
def test_simplepdl::resource_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=simplepdl::Resource_strategy)
def test_simplepdl::resource_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

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

@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original
