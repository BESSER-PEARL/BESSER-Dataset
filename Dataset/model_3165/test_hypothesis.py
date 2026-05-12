import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyNode,
    softwaretraces_Trace,
    softwaretraces_Feature,
    softwaretraces_Model,
    softwaretraces_MyNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mynode_is_not_abstract():
    assert not inspect.isabstract(MyNode)


def test_mynode_constructor_exists():
    assert callable(MyNode.__init__)


def test_mynode_constructor_args():
    sig = inspect.signature(MyNode.__init__)
    params = list(sig.parameters.keys())



def test_softwaretraces_trace_is_not_abstract():
    assert not inspect.isabstract(softwaretraces_Trace)


def test_softwaretraces_trace_constructor_exists():
    assert callable(softwaretraces_Trace.__init__)


def test_softwaretraces_trace_constructor_args():
    sig = inspect.signature(softwaretraces_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"

def test_softwaretraces_trace_has_projectName():
    assert hasattr(softwaretraces_Trace, "projectName")
    descriptor = None
    for klass in softwaretraces_Trace.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_softwaretraces_trace_has_fileName():
    assert hasattr(softwaretraces_Trace, "fileName")
    descriptor = None
    for klass in softwaretraces_Trace.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_softwaretraces_trace_has_lineNumber():
    assert hasattr(softwaretraces_Trace, "lineNumber")
    descriptor = None
    for klass in softwaretraces_Trace.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces_feature_is_not_abstract():
    assert not inspect.isabstract(softwaretraces_Feature)


def test_softwaretraces_feature_constructor_exists():
    assert callable(softwaretraces_Feature.__init__)


def test_softwaretraces_feature_constructor_args():
    sig = inspect.signature(softwaretraces_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softwaretraces_feature_has_name():
    assert hasattr(softwaretraces_Feature, "name")
    descriptor = None
    for klass in softwaretraces_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces_model_is_not_abstract():
    assert not inspect.isabstract(softwaretraces_Model)


def test_softwaretraces_model_constructor_exists():
    assert callable(softwaretraces_Model.__init__)


def test_softwaretraces_model_constructor_args():
    sig = inspect.signature(softwaretraces_Model.__init__)
    params = list(sig.parameters.keys())
    assert "resourceFileName" in params, "Missing parameter 'resourceFileName'"

def test_softwaretraces_model_has_resourceFileName():
    assert hasattr(softwaretraces_Model, "resourceFileName")
    descriptor = None
    for klass in softwaretraces_Model.__mro__:
        if "resourceFileName" in klass.__dict__:
            descriptor = klass.__dict__["resourceFileName"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces_mynode_is_not_abstract():
    assert not inspect.isabstract(softwaretraces_MyNode)


def test_softwaretraces_mynode_constructor_exists():
    assert callable(softwaretraces_MyNode.__init__)


def test_softwaretraces_mynode_constructor_args():
    sig = inspect.signature(softwaretraces_MyNode.__init__)
    params = list(sig.parameters.keys())


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
MyNode_strategy = st.builds(
    MyNode,
)
softwaretraces_Trace_strategy = st.builds(
    softwaretraces_Trace,
    projectName=
        safe_text,
    fileName=
        safe_text,
    lineNumber=
        st.integers()
)
softwaretraces_Feature_strategy = st.builds(
    softwaretraces_Feature,
    name=
        safe_text
)
softwaretraces_Model_strategy = st.builds(
    softwaretraces_Model,
    resourceFileName=
        safe_text
)
softwaretraces_MyNode_strategy = st.builds(
    softwaretraces_MyNode,
)

@given(instance=MyNode_strategy)
@settings(max_examples=50)
def test_mynode_instantiation(instance):
    assert isinstance(instance, MyNode)

@given(instance=softwaretraces_Trace_strategy)
@settings(max_examples=50)
def test_softwaretraces_trace_instantiation(instance):
    assert isinstance(instance, softwaretraces_Trace)



@given(instance=softwaretraces_Trace_strategy)
def test_softwaretraces_trace_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original



@given(instance=softwaretraces_Trace_strategy)
def test_softwaretraces_trace_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=softwaretraces_Trace_strategy)
def test_softwaretraces_trace_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original

@given(instance=softwaretraces_Feature_strategy)
@settings(max_examples=50)
def test_softwaretraces_feature_instantiation(instance):
    assert isinstance(instance, softwaretraces_Feature)



@given(instance=softwaretraces_Feature_strategy)
def test_softwaretraces_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softwaretraces_Model_strategy)
@settings(max_examples=50)
def test_softwaretraces_model_instantiation(instance):
    assert isinstance(instance, softwaretraces_Model)



@given(instance=softwaretraces_Model_strategy)
def test_softwaretraces_model_resourceFileName_setter(instance):
    original = instance.resourceFileName
    instance.resourceFileName = original
    assert instance.resourceFileName == original

@given(instance=softwaretraces_MyNode_strategy)
@settings(max_examples=50)
def test_softwaretraces_mynode_instantiation(instance):
    assert isinstance(instance, softwaretraces_MyNode)
