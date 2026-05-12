import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplePDL_WorkProduct,
    WorkDefinition,
    simplePDL_Activity,
    simplePDL_SubProcess,
    simplePDL_WorkDefinitionParameter,
    simplePDL_WorkSequence,
    simplePDL_WorkDefinition,
    simplePDL_Process,
    WorkSequenceType,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplepdl_workproduct_is_not_abstract():
    assert not inspect.isabstract(simplePDL_WorkProduct)


def test_simplepdl_workproduct_constructor_exists():
    assert callable(simplePDL_WorkProduct.__init__)


def test_simplepdl_workproduct_constructor_args():
    sig = inspect.signature(simplePDL_WorkProduct.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_workproduct_has_name():
    assert hasattr(simplePDL_WorkProduct, "name")
    descriptor = None
    for klass in simplePDL_WorkProduct.__mro__:
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



def test_simplepdl_activity_is_not_abstract():
    assert not inspect.isabstract(simplePDL_Activity)


def test_simplepdl_activity_constructor_exists():
    assert callable(simplePDL_Activity.__init__)


def test_simplepdl_activity_constructor_args():
    sig = inspect.signature(simplePDL_Activity.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_subprocess_is_not_abstract():
    assert not inspect.isabstract(simplePDL_SubProcess)


def test_simplepdl_subprocess_constructor_exists():
    assert callable(simplePDL_SubProcess.__init__)


def test_simplepdl_subprocess_constructor_args():
    sig = inspect.signature(simplePDL_SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_simplepdl_workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(simplePDL_WorkDefinitionParameter)


def test_simplepdl_workdefinitionparameter_constructor_exists():
    assert callable(simplePDL_WorkDefinitionParameter.__init__)


def test_simplepdl_workdefinitionparameter_constructor_args():
    sig = inspect.signature(simplePDL_WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterKind" in params, "Missing parameter 'parameterKind'"

def test_simplepdl_workdefinitionparameter_has_parameterKind():
    assert hasattr(simplePDL_WorkDefinitionParameter, "parameterKind")
    descriptor = None
    for klass in simplePDL_WorkDefinitionParameter.__mro__:
        if "parameterKind" in klass.__dict__:
            descriptor = klass.__dict__["parameterKind"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_worksequence_is_not_abstract():
    assert not inspect.isabstract(simplePDL_WorkSequence)


def test_simplepdl_worksequence_constructor_exists():
    assert callable(simplePDL_WorkSequence.__init__)


def test_simplepdl_worksequence_constructor_args():
    sig = inspect.signature(simplePDL_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_simplepdl_worksequence_has_linkType():
    assert hasattr(simplePDL_WorkSequence, "linkType")
    descriptor = None
    for klass in simplePDL_WorkSequence.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_workdefinition_is_not_abstract():
    assert not inspect.isabstract(simplePDL_WorkDefinition)


def test_simplepdl_workdefinition_constructor_exists():
    assert callable(simplePDL_WorkDefinition.__init__)


def test_simplepdl_workdefinition_constructor_args():
    sig = inspect.signature(simplePDL_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_workdefinition_has_name():
    assert hasattr(simplePDL_WorkDefinition, "name")
    descriptor = None
    for klass in simplePDL_WorkDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplepdl_process_is_not_abstract():
    assert not inspect.isabstract(simplePDL_Process)


def test_simplepdl_process_constructor_exists():
    assert callable(simplePDL_Process.__init__)


def test_simplepdl_process_constructor_args():
    sig = inspect.signature(simplePDL_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplepdl_process_has_name():
    assert hasattr(simplePDL_Process, "name")
    descriptor = None
    for klass in simplePDL_Process.__mro__:
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
        "finishTofinish",
        "finishToStart",
        "startToStart",
        "startToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceType"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
simplePDL_WorkProduct_strategy = st.builds(
    simplePDL_WorkProduct,
    name=
        safe_text
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
simplePDL_Activity_strategy = st.builds(
    simplePDL_Activity,
)
simplePDL_SubProcess_strategy = st.builds(
    simplePDL_SubProcess,
)
simplePDL_WorkDefinitionParameter_strategy = st.builds(
    simplePDL_WorkDefinitionParameter,
    parameterKind=
        safe_text
)
simplePDL_WorkSequence_strategy = st.builds(
    simplePDL_WorkSequence,
    linkType=
        safe_text
)
simplePDL_WorkDefinition_strategy = st.builds(
    simplePDL_WorkDefinition,
    name=
        safe_text
)
simplePDL_Process_strategy = st.builds(
    simplePDL_Process,
    name=
        safe_text
)

@given(instance=simplePDL_WorkProduct_strategy)
@settings(max_examples=50)
def test_simplepdl_workproduct_instantiation(instance):
    assert isinstance(instance, simplePDL_WorkProduct)



@given(instance=simplePDL_WorkProduct_strategy)
def test_simplepdl_workproduct_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=simplePDL_Activity_strategy)
@settings(max_examples=50)
def test_simplepdl_activity_instantiation(instance):
    assert isinstance(instance, simplePDL_Activity)

@given(instance=simplePDL_SubProcess_strategy)
@settings(max_examples=50)
def test_simplepdl_subprocess_instantiation(instance):
    assert isinstance(instance, simplePDL_SubProcess)

@given(instance=simplePDL_WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_simplepdl_workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, simplePDL_WorkDefinitionParameter)



@given(instance=simplePDL_WorkDefinitionParameter_strategy)
def test_simplepdl_workdefinitionparameter_parameterKind_setter(instance):
    original = instance.parameterKind
    instance.parameterKind = original
    assert instance.parameterKind == original

@given(instance=simplePDL_WorkSequence_strategy)
@settings(max_examples=50)
def test_simplepdl_worksequence_instantiation(instance):
    assert isinstance(instance, simplePDL_WorkSequence)



@given(instance=simplePDL_WorkSequence_strategy)
def test_simplepdl_worksequence_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=simplePDL_WorkDefinition_strategy)
@settings(max_examples=50)
def test_simplepdl_workdefinition_instantiation(instance):
    assert isinstance(instance, simplePDL_WorkDefinition)



@given(instance=simplePDL_WorkDefinition_strategy)
def test_simplepdl_workdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplePDL_Process_strategy)
@settings(max_examples=50)
def test_simplepdl_process_instantiation(instance):
    assert isinstance(instance, simplePDL_Process)



@given(instance=simplePDL_Process_strategy)
def test_simplepdl_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
