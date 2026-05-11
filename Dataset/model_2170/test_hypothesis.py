import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DVertex,
    dgf::DReference,
    DContainedVertex,
    dgf::DTypedElement,
    dgf::Graph,
    dgf::DContainment,
    DContainedElement,
    dgf::DContainedVertex,
    DTypedElement,
    dgf::DLink,
    dgf::DGraphElement,
    DGraphElement,
    dgf::DNode,
    dgf::DContainedElement,
    dgf::DVertex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dvertex_is_not_abstract():
    assert not inspect.isabstract(DVertex)


def test_dvertex_constructor_exists():
    assert callable(DVertex.__init__)


def test_dvertex_constructor_args():
    sig = inspect.signature(DVertex.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dreference_is_not_abstract():
    assert not inspect.isabstract(dgf::DReference)


def test_dgf::dreference_constructor_exists():
    assert callable(dgf::DReference.__init__)


def test_dgf::dreference_constructor_args():
    sig = inspect.signature(dgf::DReference.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"

def test_dgf::dreference_has__property():
    assert hasattr(dgf::DReference, "_property")
    descriptor = None
    for klass in dgf::DReference.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)



def test_dcontainedvertex_is_not_abstract():
    assert not inspect.isabstract(DContainedVertex)


def test_dcontainedvertex_constructor_exists():
    assert callable(DContainedVertex.__init__)


def test_dcontainedvertex_constructor_args():
    sig = inspect.signature(DContainedVertex.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dtypedelement_is_not_abstract():
    assert not inspect.isabstract(dgf::DTypedElement)


def test_dgf::dtypedelement_constructor_exists():
    assert callable(dgf::DTypedElement.__init__)


def test_dgf::dtypedelement_constructor_args():
    sig = inspect.signature(dgf::DTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dgf::graph_is_not_abstract():
    assert not inspect.isabstract(dgf::Graph)


def test_dgf::graph_constructor_exists():
    assert callable(dgf::Graph.__init__)


def test_dgf::graph_constructor_args():
    sig = inspect.signature(dgf::Graph.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dcontainment_is_not_abstract():
    assert not inspect.isabstract(dgf::DContainment)


def test_dgf::dcontainment_constructor_exists():
    assert callable(dgf::DContainment.__init__)


def test_dgf::dcontainment_constructor_args():
    sig = inspect.signature(dgf::DContainment.__init__)
    params = list(sig.parameters.keys())
    assert "compartment" in params, "Missing parameter 'compartment'"

def test_dgf::dcontainment_has_compartment():
    assert hasattr(dgf::DContainment, "compartment")
    descriptor = None
    for klass in dgf::DContainment.__mro__:
        if "compartment" in klass.__dict__:
            descriptor = klass.__dict__["compartment"]
            break
    assert isinstance(descriptor, property)



def test_dcontainedelement_is_not_abstract():
    assert not inspect.isabstract(DContainedElement)


def test_dcontainedelement_constructor_exists():
    assert callable(DContainedElement.__init__)


def test_dcontainedelement_constructor_args():
    sig = inspect.signature(DContainedElement.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dcontainedvertex_is_not_abstract():
    assert not inspect.isabstract(dgf::DContainedVertex)


def test_dgf::dcontainedvertex_constructor_exists():
    assert callable(dgf::DContainedVertex.__init__)


def test_dgf::dcontainedvertex_constructor_args():
    sig = inspect.signature(dgf::DContainedVertex.__init__)
    params = list(sig.parameters.keys())



def test_dtypedelement_is_not_abstract():
    assert not inspect.isabstract(DTypedElement)


def test_dtypedelement_constructor_exists():
    assert callable(DTypedElement.__init__)


def test_dtypedelement_constructor_args():
    sig = inspect.signature(DTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dlink_is_not_abstract():
    assert not inspect.isabstract(dgf::DLink)


def test_dgf::dlink_constructor_exists():
    assert callable(dgf::DLink.__init__)


def test_dgf::dlink_constructor_args():
    sig = inspect.signature(dgf::DLink.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dgraphelement_is_not_abstract():
    assert not inspect.isabstract(dgf::DGraphElement)


def test_dgf::dgraphelement_constructor_exists():
    assert callable(dgf::DGraphElement.__init__)


def test_dgf::dgraphelement_constructor_args():
    sig = inspect.signature(dgf::DGraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dgf::dgraphelement_has_name():
    assert hasattr(dgf::DGraphElement, "name")
    descriptor = None
    for klass in dgf::DGraphElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dgraphelement_is_not_abstract():
    assert not inspect.isabstract(DGraphElement)


def test_dgraphelement_constructor_exists():
    assert callable(DGraphElement.__init__)


def test_dgraphelement_constructor_args():
    sig = inspect.signature(DGraphElement.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dnode_is_not_abstract():
    assert not inspect.isabstract(dgf::DNode)


def test_dgf::dnode_constructor_exists():
    assert callable(dgf::DNode.__init__)


def test_dgf::dnode_constructor_args():
    sig = inspect.signature(dgf::DNode.__init__)
    params = list(sig.parameters.keys())
    assert "pointOfView" in params, "Missing parameter 'pointOfView'"

def test_dgf::dnode_has_pointOfView():
    assert hasattr(dgf::DNode, "pointOfView")
    descriptor = None
    for klass in dgf::DNode.__mro__:
        if "pointOfView" in klass.__dict__:
            descriptor = klass.__dict__["pointOfView"]
            break
    assert isinstance(descriptor, property)



def test_dgf::dcontainedelement_is_not_abstract():
    assert not inspect.isabstract(dgf::DContainedElement)


def test_dgf::dcontainedelement_constructor_exists():
    assert callable(dgf::DContainedElement.__init__)


def test_dgf::dcontainedelement_constructor_args():
    sig = inspect.signature(dgf::DContainedElement.__init__)
    params = list(sig.parameters.keys())



def test_dgf::dvertex_is_not_abstract():
    assert not inspect.isabstract(dgf::DVertex)


def test_dgf::dvertex_constructor_exists():
    assert callable(dgf::DVertex.__init__)


def test_dgf::dvertex_constructor_args():
    sig = inspect.signature(dgf::DVertex.__init__)
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
DVertex_strategy = st.builds(
    DVertex,
)
dgf::DReference_strategy = st.builds(
    dgf::DReference,
    _property=
        st.booleans()
)
DContainedVertex_strategy = st.builds(
    DContainedVertex,
)
dgf::DTypedElement_strategy = st.builds(
    dgf::DTypedElement,
)
dgf::Graph_strategy = st.builds(
    dgf::Graph,
)
dgf::DContainment_strategy = st.builds(
    dgf::DContainment,
    compartment=
        safe_text
)
DContainedElement_strategy = st.builds(
    DContainedElement,
)
dgf::DContainedVertex_strategy = st.builds(
    dgf::DContainedVertex,
)
DTypedElement_strategy = st.builds(
    DTypedElement,
)
dgf::DLink_strategy = st.builds(
    dgf::DLink,
)
dgf::DGraphElement_strategy = st.builds(
    dgf::DGraphElement,
    name=
        safe_text
)
DGraphElement_strategy = st.builds(
    DGraphElement,
)
dgf::DNode_strategy = st.builds(
    dgf::DNode,
    pointOfView=
        safe_text
)
dgf::DContainedElement_strategy = st.builds(
    dgf::DContainedElement,
)
dgf::DVertex_strategy = st.builds(
    dgf::DVertex,
)

@given(instance=DVertex_strategy)
@settings(max_examples=50)
def test_dvertex_instantiation(instance):
    assert isinstance(instance, DVertex)

@given(instance=dgf::DReference_strategy)
@settings(max_examples=50)
def test_dgf::dreference_instantiation(instance):
    assert isinstance(instance, dgf::DReference)

@given(instance=dgf::DReference_strategy)
def test_dgf::dreference__property_type(instance):
    assert isinstance(instance._property, bool)


@given(instance=dgf::DReference_strategy)
def test_dgf::dreference__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=DContainedVertex_strategy)
@settings(max_examples=50)
def test_dcontainedvertex_instantiation(instance):
    assert isinstance(instance, DContainedVertex)

@given(instance=dgf::DTypedElement_strategy)
@settings(max_examples=50)
def test_dgf::dtypedelement_instantiation(instance):
    assert isinstance(instance, dgf::DTypedElement)

@given(instance=dgf::Graph_strategy)
@settings(max_examples=50)
def test_dgf::graph_instantiation(instance):
    assert isinstance(instance, dgf::Graph)

@given(instance=dgf::DContainment_strategy)
@settings(max_examples=50)
def test_dgf::dcontainment_instantiation(instance):
    assert isinstance(instance, dgf::DContainment)

@given(instance=dgf::DContainment_strategy)
def test_dgf::dcontainment_compartment_type(instance):
    assert isinstance(instance.compartment, str)


@given(instance=dgf::DContainment_strategy)
def test_dgf::dcontainment_compartment_setter(instance):
    original = instance.compartment
    instance.compartment = original
    assert instance.compartment == original

@given(instance=DContainedElement_strategy)
@settings(max_examples=50)
def test_dcontainedelement_instantiation(instance):
    assert isinstance(instance, DContainedElement)

@given(instance=dgf::DContainedVertex_strategy)
@settings(max_examples=50)
def test_dgf::dcontainedvertex_instantiation(instance):
    assert isinstance(instance, dgf::DContainedVertex)

@given(instance=DTypedElement_strategy)
@settings(max_examples=50)
def test_dtypedelement_instantiation(instance):
    assert isinstance(instance, DTypedElement)

@given(instance=dgf::DLink_strategy)
@settings(max_examples=50)
def test_dgf::dlink_instantiation(instance):
    assert isinstance(instance, dgf::DLink)

@given(instance=dgf::DGraphElement_strategy)
@settings(max_examples=50)
def test_dgf::dgraphelement_instantiation(instance):
    assert isinstance(instance, dgf::DGraphElement)

@given(instance=dgf::DGraphElement_strategy)
def test_dgf::dgraphelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dgf::DGraphElement_strategy)
def test_dgf::dgraphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DGraphElement_strategy)
@settings(max_examples=50)
def test_dgraphelement_instantiation(instance):
    assert isinstance(instance, DGraphElement)

@given(instance=dgf::DNode_strategy)
@settings(max_examples=50)
def test_dgf::dnode_instantiation(instance):
    assert isinstance(instance, dgf::DNode)

@given(instance=dgf::DNode_strategy)
def test_dgf::dnode_pointOfView_type(instance):
    assert isinstance(instance.pointOfView, str)


@given(instance=dgf::DNode_strategy)
def test_dgf::dnode_pointOfView_setter(instance):
    original = instance.pointOfView
    instance.pointOfView = original
    assert instance.pointOfView == original

@given(instance=dgf::DContainedElement_strategy)
@settings(max_examples=50)
def test_dgf::dcontainedelement_instantiation(instance):
    assert isinstance(instance, dgf::DContainedElement)

@given(instance=dgf::DVertex_strategy)
@settings(max_examples=50)
def test_dgf::dvertex_instantiation(instance):
    assert isinstance(instance, dgf::DVertex)
