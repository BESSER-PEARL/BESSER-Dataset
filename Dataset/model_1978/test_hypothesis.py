import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeGraphTrace::MethodSignatureTrace,
    TypeGraphTrace::TypeGraph,
    TypeGraphTrace::Trace,
    TypeGraphTrace::TClass,
    TypeGraphTrace::TMethodSignature,
    TypeGraphTrace::ClassListTrace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typegraphtrace::methodsignaturetrace_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::MethodSignatureTrace)


def test_typegraphtrace::methodsignaturetrace_constructor_exists():
    assert callable(TypeGraphTrace::MethodSignatureTrace.__init__)


def test_typegraphtrace::methodsignaturetrace_constructor_args():
    sig = inspect.signature(TypeGraphTrace::MethodSignatureTrace.__init__)
    params = list(sig.parameters.keys())
    assert "signatureString" in params, "Missing parameter 'signatureString'"

def test_typegraphtrace::methodsignaturetrace_has_signatureString():
    assert hasattr(TypeGraphTrace::MethodSignatureTrace, "signatureString")
    descriptor = None
    for klass in TypeGraphTrace::MethodSignatureTrace.__mro__:
        if "signatureString" in klass.__dict__:
            descriptor = klass.__dict__["signatureString"]
            break
    assert isinstance(descriptor, property)



def test_typegraphtrace::typegraph_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::TypeGraph)


def test_typegraphtrace::typegraph_constructor_exists():
    assert callable(TypeGraphTrace::TypeGraph.__init__)


def test_typegraphtrace::typegraph_constructor_args():
    sig = inspect.signature(TypeGraphTrace::TypeGraph.__init__)
    params = list(sig.parameters.keys())



def test_typegraphtrace::trace_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::Trace)


def test_typegraphtrace::trace_constructor_exists():
    assert callable(TypeGraphTrace::Trace.__init__)


def test_typegraphtrace::trace_constructor_args():
    sig = inspect.signature(TypeGraphTrace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_typegraphtrace::tclass_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::TClass)


def test_typegraphtrace::tclass_constructor_exists():
    assert callable(TypeGraphTrace::TClass.__init__)


def test_typegraphtrace::tclass_constructor_args():
    sig = inspect.signature(TypeGraphTrace::TClass.__init__)
    params = list(sig.parameters.keys())



def test_typegraphtrace::tmethodsignature_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::TMethodSignature)


def test_typegraphtrace::tmethodsignature_constructor_exists():
    assert callable(TypeGraphTrace::TMethodSignature.__init__)


def test_typegraphtrace::tmethodsignature_constructor_args():
    sig = inspect.signature(TypeGraphTrace::TMethodSignature.__init__)
    params = list(sig.parameters.keys())



def test_typegraphtrace::classlisttrace_is_not_abstract():
    assert not inspect.isabstract(TypeGraphTrace::ClassListTrace)


def test_typegraphtrace::classlisttrace_constructor_exists():
    assert callable(TypeGraphTrace::ClassListTrace.__init__)


def test_typegraphtrace::classlisttrace_constructor_args():
    sig = inspect.signature(TypeGraphTrace::ClassListTrace.__init__)
    params = list(sig.parameters.keys())
    assert "concatSignature" in params, "Missing parameter 'concatSignature'"

def test_typegraphtrace::classlisttrace_has_concatSignature():
    assert hasattr(TypeGraphTrace::ClassListTrace, "concatSignature")
    descriptor = None
    for klass in TypeGraphTrace::ClassListTrace.__mro__:
        if "concatSignature" in klass.__dict__:
            descriptor = klass.__dict__["concatSignature"]
            break
    assert isinstance(descriptor, property)


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
TypeGraphTrace::MethodSignatureTrace_strategy = st.builds(
    TypeGraphTrace::MethodSignatureTrace,
    signatureString=
        safe_text
)
TypeGraphTrace::TypeGraph_strategy = st.builds(
    TypeGraphTrace::TypeGraph,
)
TypeGraphTrace::Trace_strategy = st.builds(
    TypeGraphTrace::Trace,
)
TypeGraphTrace::TClass_strategy = st.builds(
    TypeGraphTrace::TClass,
)
TypeGraphTrace::TMethodSignature_strategy = st.builds(
    TypeGraphTrace::TMethodSignature,
)
TypeGraphTrace::ClassListTrace_strategy = st.builds(
    TypeGraphTrace::ClassListTrace,
    concatSignature=
        safe_text
)

@given(instance=TypeGraphTrace::MethodSignatureTrace_strategy)
@settings(max_examples=50)
def test_typegraphtrace::methodsignaturetrace_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::MethodSignatureTrace)

@given(instance=TypeGraphTrace::MethodSignatureTrace_strategy)
def test_typegraphtrace::methodsignaturetrace_signatureString_type(instance):
    assert isinstance(instance.signatureString, str)


@given(instance=TypeGraphTrace::MethodSignatureTrace_strategy)
def test_typegraphtrace::methodsignaturetrace_signatureString_setter(instance):
    original = instance.signatureString
    instance.signatureString = original
    assert instance.signatureString == original

@given(instance=TypeGraphTrace::TypeGraph_strategy)
@settings(max_examples=50)
def test_typegraphtrace::typegraph_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::TypeGraph)

@given(instance=TypeGraphTrace::Trace_strategy)
@settings(max_examples=50)
def test_typegraphtrace::trace_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::Trace)

@given(instance=TypeGraphTrace::TClass_strategy)
@settings(max_examples=50)
def test_typegraphtrace::tclass_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::TClass)

@given(instance=TypeGraphTrace::TMethodSignature_strategy)
@settings(max_examples=50)
def test_typegraphtrace::tmethodsignature_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::TMethodSignature)

@given(instance=TypeGraphTrace::ClassListTrace_strategy)
@settings(max_examples=50)
def test_typegraphtrace::classlisttrace_instantiation(instance):
    assert isinstance(instance, TypeGraphTrace::ClassListTrace)

@given(instance=TypeGraphTrace::ClassListTrace_strategy)
def test_typegraphtrace::classlisttrace_concatSignature_type(instance):
    assert isinstance(instance.concatSignature, str)


@given(instance=TypeGraphTrace::ClassListTrace_strategy)
def test_typegraphtrace::classlisttrace_concatSignature_setter(instance):
    original = instance.concatSignature
    instance.concatSignature = original
    assert instance.concatSignature == original
