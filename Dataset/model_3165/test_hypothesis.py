import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MyNode,
    softwaretraces::Feature,
    softwaretraces::Trace,
    softwaretraces::Model,
    softwaretraces::MyNode,
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



def test_softwaretraces::feature_is_not_abstract():
    assert not inspect.isabstract(softwaretraces::Feature)


def test_softwaretraces::feature_constructor_exists():
    assert callable(softwaretraces::Feature.__init__)


def test_softwaretraces::feature_constructor_args():
    sig = inspect.signature(softwaretraces::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softwaretraces::feature_has_name():
    assert hasattr(softwaretraces::Feature, "name")
    descriptor = None
    for klass in softwaretraces::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces::trace_is_not_abstract():
    assert not inspect.isabstract(softwaretraces::Trace)


def test_softwaretraces::trace_constructor_exists():
    assert callable(softwaretraces::Trace.__init__)


def test_softwaretraces::trace_constructor_args():
    sig = inspect.signature(softwaretraces::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_softwaretraces::trace_has_lineNumber():
    assert hasattr(softwaretraces::Trace, "lineNumber")
    descriptor = None
    for klass in softwaretraces::Trace.__mro__:
        if "lineNumber" in klass.__dict__:
            descriptor = klass.__dict__["lineNumber"]
            break
    assert isinstance(descriptor, property)

def test_softwaretraces::trace_has_projectName():
    assert hasattr(softwaretraces::Trace, "projectName")
    descriptor = None
    for klass in softwaretraces::Trace.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_softwaretraces::trace_has_fileName():
    assert hasattr(softwaretraces::Trace, "fileName")
    descriptor = None
    for klass in softwaretraces::Trace.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces::model_is_not_abstract():
    assert not inspect.isabstract(softwaretraces::Model)


def test_softwaretraces::model_constructor_exists():
    assert callable(softwaretraces::Model.__init__)


def test_softwaretraces::model_constructor_args():
    sig = inspect.signature(softwaretraces::Model.__init__)
    params = list(sig.parameters.keys())
    assert "resourceFileName" in params, "Missing parameter 'resourceFileName'"

def test_softwaretraces::model_has_resourceFileName():
    assert hasattr(softwaretraces::Model, "resourceFileName")
    descriptor = None
    for klass in softwaretraces::Model.__mro__:
        if "resourceFileName" in klass.__dict__:
            descriptor = klass.__dict__["resourceFileName"]
            break
    assert isinstance(descriptor, property)



def test_softwaretraces::mynode_is_not_abstract():
    assert not inspect.isabstract(softwaretraces::MyNode)


def test_softwaretraces::mynode_constructor_exists():
    assert callable(softwaretraces::MyNode.__init__)


def test_softwaretraces::mynode_constructor_args():
    sig = inspect.signature(softwaretraces::MyNode.__init__)
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
softwaretraces::Feature_strategy = st.builds(
    softwaretraces::Feature,
    name=
        safe_text
)
softwaretraces::Trace_strategy = st.builds(
    softwaretraces::Trace,
    lineNumber=
        st.integers(),
    projectName=
        safe_text,
    fileName=
        safe_text
)
softwaretraces::Model_strategy = st.builds(
    softwaretraces::Model,
    resourceFileName=
        safe_text
)
softwaretraces::MyNode_strategy = st.builds(
    softwaretraces::MyNode,
)

@given(instance=MyNode_strategy)
@settings(max_examples=50)
def test_mynode_instantiation(instance):
    assert isinstance(instance, MyNode)

@given(instance=softwaretraces::Feature_strategy)
@settings(max_examples=50)
def test_softwaretraces::feature_instantiation(instance):
    assert isinstance(instance, softwaretraces::Feature)

@given(instance=softwaretraces::Feature_strategy)
def test_softwaretraces::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softwaretraces::Feature_strategy)
def test_softwaretraces::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softwaretraces::Trace_strategy)
@settings(max_examples=50)
def test_softwaretraces::trace_instantiation(instance):
    assert isinstance(instance, softwaretraces::Trace)

@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_lineNumber_type(instance):
    assert isinstance(instance.lineNumber, int)


@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original

@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_projectName_type(instance):
    assert isinstance(instance.projectName, str)


@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original

@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=softwaretraces::Trace_strategy)
def test_softwaretraces::trace_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=softwaretraces::Model_strategy)
@settings(max_examples=50)
def test_softwaretraces::model_instantiation(instance):
    assert isinstance(instance, softwaretraces::Model)

@given(instance=softwaretraces::Model_strategy)
def test_softwaretraces::model_resourceFileName_type(instance):
    assert isinstance(instance.resourceFileName, str)


@given(instance=softwaretraces::Model_strategy)
def test_softwaretraces::model_resourceFileName_setter(instance):
    original = instance.resourceFileName
    instance.resourceFileName = original
    assert instance.resourceFileName == original

@given(instance=softwaretraces::MyNode_strategy)
@settings(max_examples=50)
def test_softwaretraces::mynode_instantiation(instance):
    assert isinstance(instance, softwaretraces::MyNode)
