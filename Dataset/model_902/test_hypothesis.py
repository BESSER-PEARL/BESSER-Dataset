import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplePDL::WorkProduct,
    WorkDefinition,
    simplePDL::Activity,
    simplePDL::SubProcess,
    simplePDL::WorkDefinitionParameter,
    simplePDL::WorkSequence,
    simplePDL::WorkDefinition,
    simplePDL::Process,
    ParameterDirectionKind,
    WorkSequenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplepdl::workproduct_is_not_abstract():
    assert not inspect.isabstract(simplePDL::WorkProduct)


def test_simplepdl::workproduct_constructor_exists():
    assert callable(simplePDL::WorkProduct.__init__)


def test_simplepdl::workproduct_constructor_args():
    sig = inspect.signature(simplePDL::WorkProduct.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::workproduct_has_name():
    assert hasattr(simplePDL::WorkProduct, "name")
    descriptor = None
    for klass in simplePDL::WorkProduct.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::activity_is_not_abstract():
    assert not inspect.isabstract(simplePDL::Activity)


def test_simplepdl::activity_constructor_exists():
    assert callable(simplePDL::Activity.__init__)


def test_simplepdl::activity_constructor_args():
    sig = inspect.signature(simplePDL::Activity.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::subprocess_is_not_abstract():
    assert not inspect.isabstract(simplePDL::SubProcess)


def test_simplepdl::subprocess_constructor_exists():
    assert callable(simplePDL::SubProcess.__init__)


def test_simplepdl::subprocess_constructor_args():
    sig = inspect.signature(simplePDL::SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl::workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(simplePDL::WorkDefinitionParameter)


def test_simplepdl::workdefinitionparameter_constructor_exists():
    assert callable(simplePDL::WorkDefinitionParameter.__init__)


def test_simplepdl::workdefinitionparameter_constructor_args():
    sig = inspect.signature(simplePDL::WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterKind" in params, "Missing parameter 'parameterKind'"

def test_simplepdl::workdefinitionparameter_has_parameterKind():
    assert hasattr(simplePDL::WorkDefinitionParameter, "parameterKind")
    descriptor = None
    for klass in simplePDL::WorkDefinitionParameter.__mro__:
        if "parameterKind" in klass.__dict__:
            descriptor = klass.__dict__["parameterKind"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::worksequence_is_not_abstract():
    assert not inspect.isabstract(simplePDL::WorkSequence)


def test_simplepdl::worksequence_constructor_exists():
    assert callable(simplePDL::WorkSequence.__init__)


def test_simplepdl::worksequence_constructor_args():
    sig = inspect.signature(simplePDL::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl::worksequence_has_linkType():
    assert hasattr(simplePDL::WorkSequence, "linkType")
    descriptor = None
    for klass in simplePDL::WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplePDL::WorkDefinition)


def test_simplepdl::workdefinition_constructor_exists():
    assert callable(simplePDL::WorkDefinition.__init__)


def test_simplepdl::workdefinition_constructor_args():
    sig = inspect.signature(simplePDL::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::workdefinition_has_name():
    assert hasattr(simplePDL::WorkDefinition, "name")
    descriptor = None
    for klass in simplePDL::WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl::process_is_not_abstract():
    assert not inspect.isabstract(simplePDL::Process)


def test_simplepdl::process_constructor_exists():
    assert callable(simplePDL::Process.__init__)


def test_simplepdl::process_constructor_args():
    sig = inspect.signature(simplePDL::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl::process_has_name():
    assert hasattr(simplePDL::Process, "name")
    descriptor = None
    for klass in simplePDL::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "out",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_worksequencetype_exists():
    # Check that the Enumeration exists
    assert WorkSequenceType is not None

def test_worksequencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceType]
    expected_literals = [
        "finishToStart",
        "startToFinish",
        "finishTofinish",
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
simplePDL::WorkProduct_strategy = st.builds(
    simplePDL::WorkProduct,
    name=
        safe_text
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
simplePDL::Activity_strategy = st.builds(
    simplePDL::Activity,
)
simplePDL::SubProcess_strategy = st.builds(
    simplePDL::SubProcess,
)
simplePDL::WorkDefinitionParameter_strategy = st.builds(
    simplePDL::WorkDefinitionParameter,
    parameterKind=
        safe_text
)
simplePDL::WorkSequence_strategy = st.builds(
    simplePDL::WorkSequence,
    linkType=
        safe_text
)
simplePDL::WorkDefinition_strategy = st.builds(
    simplePDL::WorkDefinition,
    name=
        safe_text
)
simplePDL::Process_strategy = st.builds(
    simplePDL::Process,
    name=
        safe_text
)

@given(instance=simplePDL::WorkProduct_strategy)
@settings(max_examples=50)
def test_simplepdl::workproduct_instantiation(instance):
    assert isinstance(instance, simplePDL::WorkProduct)

@given(instance=simplePDL::WorkProduct_strategy)
def test_simplepdl::workproduct_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplePDL::WorkProduct_strategy)
def test_simplepdl::workproduct_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=simplePDL::Activity_strategy)
@settings(max_examples=50)
def test_simplepdl::activity_instantiation(instance):
    assert isinstance(instance, simplePDL::Activity)

@given(instance=simplePDL::SubProcess_strategy)
@settings(max_examples=50)
def test_simplepdl::subprocess_instantiation(instance):
    assert isinstance(instance, simplePDL::SubProcess)

@given(instance=simplePDL::WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, simplePDL::WorkDefinitionParameter)

@given(instance=simplePDL::WorkDefinitionParameter_strategy)
def test_simplepdl::workdefinitionparameter_parameterKind_type(instance):
    assert isinstance(instance.parameterKind, str)


@given(instance=simplePDL::WorkDefinitionParameter_strategy)
def test_simplepdl::workdefinitionparameter_parameterKind_setter(instance):
    original = instance.parameterKind
    instance.parameterKind = original
    assert instance.parameterKind == original

@given(instance=simplePDL::WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl::worksequence_instantiation(instance):
    assert isinstance(instance, simplePDL::WorkSequence)

@given(instance=simplePDL::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=simplePDL::WorkSequence_strategy)
def test_simplepdl::worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=simplePDL::WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl::workdefinition_instantiation(instance):
    assert isinstance(instance, simplePDL::WorkDefinition)

@given(instance=simplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplePDL::WorkDefinition_strategy)
def test_simplepdl::workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplePDL::Process_strategy)
@settings(max_examples=50)
def test_simplepdl::process_instantiation(instance):
    assert isinstance(instance, simplePDL::Process)

@given(instance=simplePDL::Process_strategy)
def test_simplepdl::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplePDL::Process_strategy)
def test_simplepdl::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
