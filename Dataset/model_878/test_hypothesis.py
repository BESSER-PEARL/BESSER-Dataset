import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ProcessElement,
    simplepdl::WorkSequence,
    simplepdl::RessourceDefinition,
    simplepdl::RessourceConfig,
    simplepdl::RessourceInstance,
    simplepdl::Guidance,
    simplepdl::WorkDefinition,
    simplepdl::ProcessElement,
    simplepdl::Process,
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



def test_simplepdl::ressourcedefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::RessourceDefinition)


def test_simplepdl::ressourcedefinition_constructor_exists():
    assert callable(simplepdl::RessourceDefinition.__init__)


def test_simplepdl::ressourcedefinition_constructor_args():
    sig = inspect.signature(simplepdl::RessourceDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::ressourcedefinition_has_number():
    assert hasattr(simplepdl::RessourceDefinition, "number")
    descriptor = None
    for klass in simplepdl::RessourceDefinition.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::ressourcedefinition_has_name():
    assert hasattr(simplepdl::RessourceDefinition, "name")
    descriptor = None
    for klass in simplepdl::RessourceDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::ressourceconfig_is_not_abstract():
    assert not inspect.isabstract(simplepdl::RessourceConfig)


def test_simplepdl::ressourceconfig_constructor_exists():
    assert callable(simplepdl::RessourceConfig.__init__)


def test_simplepdl::ressourceconfig_constructor_args():
    sig = inspect.signature(simplepdl::RessourceConfig.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::ressourceconfig_has_name():
    assert hasattr(simplepdl::RessourceConfig, "name")
    descriptor = None
    for klass in simplepdl::RessourceConfig.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::ressourceinstance_is_not_abstract():
    assert not inspect.isabstract(simplepdl::RessourceInstance)


def test_simplepdl::ressourceinstance_constructor_exists():
    assert callable(simplepdl::RessourceInstance.__init__)


def test_simplepdl::ressourceinstance_constructor_args():
    sig = inspect.signature(simplepdl::RessourceInstance.__init__)
    params = list(sig.parameters.keys())
    assert "instances" in params, "Missing parameter 'instances'"

def test_simplepdl::ressourceinstance_has_instances():
    assert hasattr(simplepdl::RessourceInstance, "instances")
    descriptor = None
    for klass in simplepdl::RessourceInstance.__mro__:
        if "instances" in klass.__dict__:
            descriptor = klass.__dict__["instances"]
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



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplepdl::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(simplepdl::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(simplepdl::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::workdefinition_has_min_time():
    assert hasattr(simplepdl::WorkDefinition, "min_time")
    descriptor = None
    for klass in simplepdl::WorkDefinition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

def test_simplepdl::workdefinition_has_max_time():
    assert hasattr(simplepdl::WorkDefinition, "max_time")
    descriptor = None
    for klass in simplepdl::WorkDefinition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

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
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "max_time" in params, "Missing parameter 'max_time'"

def test_simplepdl::process_has_min_time():
    assert hasattr(simplepdl::Process, "min_time")
    descriptor = None
    for klass in simplepdl::Process.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

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

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "finishToFinish",
        "startToFinish",
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
simplepdl::WorkSequence_strategy = st.builds(
    simplepdl::WorkSequence,
    linkType=
        safe_text
)
simplepdl::RessourceDefinition_strategy = st.builds(
    simplepdl::RessourceDefinition,
    number=
        st.integers(),
    name=
        safe_text
)
simplepdl::RessourceConfig_strategy = st.builds(
    simplepdl::RessourceConfig,
    name=
        safe_text
)
simplepdl::RessourceInstance_strategy = st.builds(
    simplepdl::RessourceInstance,
    instances=
        st.integers()
)
simplepdl::Guidance_strategy = st.builds(
    simplepdl::Guidance,
    text=
        safe_text
)
simplepdl::WorkDefinition_strategy = st.builds(
    simplepdl::WorkDefinition,
    min_time=
        st.integers(),
    max_time=
        st.integers(),
    name=
        safe_text
)
simplepdl::ProcessElement_strategy = st.builds(
    simplepdl::ProcessElement,
)
simplepdl::Process_strategy = st.builds(
    simplepdl::Process,
    min_time=
        st.integers(),
    name=
        safe_text,
    max_time=
        st.integers()
)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

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

@given(instance=simplepdl::RessourceDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::ressourcedefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::RessourceDefinition)

@given(instance=simplepdl::RessourceDefinition_strategy)
def test_simplepdl::ressourcedefinition_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=simplepdl::RessourceDefinition_strategy)
def test_simplepdl::ressourcedefinition_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=simplepdl::RessourceDefinition_strategy)
def test_simplepdl::ressourcedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::RessourceDefinition_strategy)
def test_simplepdl::ressourcedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::RessourceConfig_strategy)
@settings(max_examples=50)
def test_simplepdl::ressourceconfig_instantiation(instance):
    assert isinstance(instance, simplepdl::RessourceConfig)

@given(instance=simplepdl::RessourceConfig_strategy)
def test_simplepdl::ressourceconfig_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplepdl::RessourceConfig_strategy)
def test_simplepdl::ressourceconfig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplepdl::RessourceInstance_strategy)
@settings(max_examples=50)
def test_simplepdl::ressourceinstance_instantiation(instance):
    assert isinstance(instance, simplepdl::RessourceInstance)

@given(instance=simplepdl::RessourceInstance_strategy)
def test_simplepdl::ressourceinstance_instances_type(instance):
    assert isinstance(instance.instances, int)


@given(instance=simplepdl::RessourceInstance_strategy)
def test_simplepdl::ressourceinstance_instances_setter(instance):
    original = instance.instances
    instance.instances = original
    assert instance.instances == original

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

@given(instance=simplepdl::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, simplepdl::WorkDefinition)

@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=simplepdl::WorkDefinition_strategy)
def test_simplepdl::workdefinition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

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
def test_simplepdl::process_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=simplepdl::Process_strategy)
def test_simplepdl::process_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

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
