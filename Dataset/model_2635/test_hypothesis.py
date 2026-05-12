import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DSimpleEdge,
    diagraph_DNavigationEdge,
    diagraph_DLineEdge,
    diagraph_EAttribute,
    DNode,
    DNestedEdge,
    diagraph_DAffixedEdge,
    diagraph_DCompartmentEdge,
    DEdge,
    diagraph_DSimpleEdge,
    DLineEdge,
    diagraph_DReference,
    DOwnedEdge,
    diagraph_DNestedEdge,
    diagraph_DContainment,
    diagraph_DViewNavigation,
    DOwnedElement,
    diagraph_DOwnedEdge,
    DLabeledElement,
    diagraph_DGeneric,
    diagraph_DLabeledEdge,
    diagraph_DGraph,
    diagraph_ENamedElement,
    diagraph_DGraphElement,
    diagraph_EReference,
    diagraph_DNode,
    diagraph_DOwnedElement,
    diagraph_DLabel,
    diagraph_EClass,
    diagraph_DPointOfView,
    DGraphElement,
    diagraph_DLabeledElement,
    diagraph_DEdge,
    DShape,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsimpleedge_is_not_abstract():
    assert not inspect.isabstract(DSimpleEdge)


def test_dsimpleedge_constructor_exists():
    assert callable(DSimpleEdge.__init__)


def test_dsimpleedge_constructor_args():
    sig = inspect.signature(DSimpleEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dnavigationedge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DNavigationEdge)


def test_diagraph_dnavigationedge_constructor_exists():
    assert callable(diagraph_DNavigationEdge.__init__)


def test_diagraph_dnavigationedge_constructor_args():
    sig = inspect.signature(diagraph_DNavigationEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dlineedge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DLineEdge)


def test_diagraph_dlineedge_constructor_exists():
    assert callable(diagraph_DLineEdge.__init__)


def test_diagraph_dlineedge_constructor_args():
    sig = inspect.signature(diagraph_DLineEdge.__init__)
    params = list(sig.parameters.keys())
    assert "arrows" in params, "Missing parameter 'arrows'"

def test_diagraph_dlineedge_has_arrows():
    assert hasattr(diagraph_DLineEdge, "arrows")
    descriptor = None
    for klass in diagraph_DLineEdge.__mro__:
        if "arrows" in klass.__dict__:
            descriptor = klass.__dict__["arrows"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_eattribute_is_not_abstract():
    assert not inspect.isabstract(diagraph_EAttribute)


def test_diagraph_eattribute_constructor_exists():
    assert callable(diagraph_EAttribute.__init__)


def test_diagraph_eattribute_constructor_args():
    sig = inspect.signature(diagraph_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_dnode_is_not_abstract():
    assert not inspect.isabstract(DNode)


def test_dnode_constructor_exists():
    assert callable(DNode.__init__)


def test_dnode_constructor_args():
    sig = inspect.signature(DNode.__init__)
    params = list(sig.parameters.keys())



def test_dnestededge_is_not_abstract():
    assert not inspect.isabstract(DNestedEdge)


def test_dnestededge_constructor_exists():
    assert callable(DNestedEdge.__init__)


def test_dnestededge_constructor_args():
    sig = inspect.signature(DNestedEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_daffixededge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DAffixedEdge)


def test_diagraph_daffixededge_constructor_exists():
    assert callable(diagraph_DAffixedEdge.__init__)


def test_diagraph_daffixededge_constructor_args():
    sig = inspect.signature(diagraph_DAffixedEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dcompartmentedge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DCompartmentEdge)


def test_diagraph_dcompartmentedge_constructor_exists():
    assert callable(diagraph_DCompartmentEdge.__init__)


def test_diagraph_dcompartmentedge_constructor_args():
    sig = inspect.signature(diagraph_DCompartmentEdge.__init__)
    params = list(sig.parameters.keys())
    assert "partitionName" in params, "Missing parameter 'partitionName'"
    assert "depth" in params, "Missing parameter 'depth'"

def test_diagraph_dcompartmentedge_has_partitionName():
    assert hasattr(diagraph_DCompartmentEdge, "partitionName")
    descriptor = None
    for klass in diagraph_DCompartmentEdge.__mro__:
        if "partitionName" in klass.__dict__:
            descriptor = klass.__dict__["partitionName"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dcompartmentedge_has_depth():
    assert hasattr(diagraph_DCompartmentEdge, "depth")
    descriptor = None
    for klass in diagraph_DCompartmentEdge.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)



def test_dedge_is_not_abstract():
    assert not inspect.isabstract(DEdge)


def test_dedge_constructor_exists():
    assert callable(DEdge.__init__)


def test_dedge_constructor_args():
    sig = inspect.signature(DEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dsimpleedge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DSimpleEdge)


def test_diagraph_dsimpleedge_constructor_exists():
    assert callable(diagraph_DSimpleEdge.__init__)


def test_diagraph_dsimpleedge_constructor_args():
    sig = inspect.signature(diagraph_DSimpleEdge.__init__)
    params = list(sig.parameters.keys())



def test_dlineedge_is_not_abstract():
    assert not inspect.isabstract(DLineEdge)


def test_dlineedge_constructor_exists():
    assert callable(DLineEdge.__init__)


def test_dlineedge_constructor_args():
    sig = inspect.signature(DLineEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dreference_is_not_abstract():
    assert not inspect.isabstract(diagraph_DReference)


def test_diagraph_dreference_constructor_exists():
    assert callable(diagraph_DReference.__init__)


def test_diagraph_dreference_constructor_args():
    sig = inspect.signature(diagraph_DReference.__init__)
    params = list(sig.parameters.keys())



def test_downededge_is_not_abstract():
    assert not inspect.isabstract(DOwnedEdge)


def test_downededge_constructor_exists():
    assert callable(DOwnedEdge.__init__)


def test_downededge_constructor_args():
    sig = inspect.signature(DOwnedEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dnestededge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DNestedEdge)


def test_diagraph_dnestededge_constructor_exists():
    assert callable(diagraph_DNestedEdge.__init__)


def test_diagraph_dnestededge_constructor_args():
    sig = inspect.signature(diagraph_DNestedEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dcontainment_is_not_abstract():
    assert not inspect.isabstract(diagraph_DContainment)


def test_diagraph_dcontainment_constructor_exists():
    assert callable(diagraph_DContainment.__init__)


def test_diagraph_dcontainment_constructor_args():
    sig = inspect.signature(diagraph_DContainment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_diagraph_dcontainment_has_name():
    assert hasattr(diagraph_DContainment, "name")
    descriptor = None
    for klass in diagraph_DContainment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_dviewnavigation_is_not_abstract():
    assert not inspect.isabstract(diagraph_DViewNavigation)


def test_diagraph_dviewnavigation_constructor_exists():
    assert callable(diagraph_DViewNavigation.__init__)


def test_diagraph_dviewnavigation_constructor_args():
    sig = inspect.signature(diagraph_DViewNavigation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagraph_dviewnavigation_has_id():
    assert hasattr(diagraph_DViewNavigation, "id")
    descriptor = None
    for klass in diagraph_DViewNavigation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_downedelement_is_not_abstract():
    assert not inspect.isabstract(DOwnedElement)


def test_downedelement_constructor_exists():
    assert callable(DOwnedElement.__init__)


def test_downedelement_constructor_args():
    sig = inspect.signature(DOwnedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_downededge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DOwnedEdge)


def test_diagraph_downededge_constructor_exists():
    assert callable(diagraph_DOwnedEdge.__init__)


def test_diagraph_downededge_constructor_args():
    sig = inspect.signature(diagraph_DOwnedEdge.__init__)
    params = list(sig.parameters.keys())



def test_dlabeledelement_is_not_abstract():
    assert not inspect.isabstract(DLabeledElement)


def test_dlabeledelement_constructor_exists():
    assert callable(DLabeledElement.__init__)


def test_dlabeledelement_constructor_args():
    sig = inspect.signature(DLabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dgeneric_is_not_abstract():
    assert not inspect.isabstract(diagraph_DGeneric)


def test_diagraph_dgeneric_constructor_exists():
    assert callable(diagraph_DGeneric.__init__)


def test_diagraph_dgeneric_constructor_args():
    sig = inspect.signature(diagraph_DGeneric.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dlabelededge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DLabeledEdge)


def test_diagraph_dlabelededge_constructor_exists():
    assert callable(diagraph_DLabeledEdge.__init__)


def test_diagraph_dlabelededge_constructor_args():
    sig = inspect.signature(diagraph_DLabeledEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dgraph_is_not_abstract():
    assert not inspect.isabstract(diagraph_DGraph)


def test_diagraph_dgraph_constructor_exists():
    assert callable(diagraph_DGraph.__init__)


def test_diagraph_dgraph_constructor_args():
    sig = inspect.signature(diagraph_DGraph.__init__)
    params = list(sig.parameters.keys())
    assert "viewName" in params, "Missing parameter 'viewName'"
    assert "facade2" in params, "Missing parameter 'facade2'"
    assert "facade1" in params, "Missing parameter 'facade1'"

def test_diagraph_dgraph_has_viewName():
    assert hasattr(diagraph_DGraph, "viewName")
    descriptor = None
    for klass in diagraph_DGraph.__mro__:
        if "viewName" in klass.__dict__:
            descriptor = klass.__dict__["viewName"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dgraph_has_facade2():
    assert hasattr(diagraph_DGraph, "facade2")
    descriptor = None
    for klass in diagraph_DGraph.__mro__:
        if "facade2" in klass.__dict__:
            descriptor = klass.__dict__["facade2"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dgraph_has_facade1():
    assert hasattr(diagraph_DGraph, "facade1")
    descriptor = None
    for klass in diagraph_DGraph.__mro__:
        if "facade1" in klass.__dict__:
            descriptor = klass.__dict__["facade1"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_enamedelement_is_not_abstract():
    assert not inspect.isabstract(diagraph_ENamedElement)


def test_diagraph_enamedelement_constructor_exists():
    assert callable(diagraph_ENamedElement.__init__)


def test_diagraph_enamedelement_constructor_args():
    sig = inspect.signature(diagraph_ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dgraphelement_is_not_abstract():
    assert not inspect.isabstract(diagraph_DGraphElement)


def test_diagraph_dgraphelement_constructor_exists():
    assert callable(diagraph_DGraphElement.__init__)


def test_diagraph_dgraphelement_constructor_args():
    sig = inspect.signature(diagraph_DGraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "abztract" in params, "Missing parameter 'abztract'"

def test_diagraph_dgraphelement_has_name():
    assert hasattr(diagraph_DGraphElement, "name")
    descriptor = None
    for klass in diagraph_DGraphElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dgraphelement_has_icon():
    assert hasattr(diagraph_DGraphElement, "icon")
    descriptor = None
    for klass in diagraph_DGraphElement.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dgraphelement_has_abztract():
    assert hasattr(diagraph_DGraphElement, "abztract")
    descriptor = None
    for klass in diagraph_DGraphElement.__mro__:
        if "abztract" in klass.__dict__:
            descriptor = klass.__dict__["abztract"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_ereference_is_not_abstract():
    assert not inspect.isabstract(diagraph_EReference)


def test_diagraph_ereference_constructor_exists():
    assert callable(diagraph_EReference.__init__)


def test_diagraph_ereference_constructor_args():
    sig = inspect.signature(diagraph_EReference.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dnode_is_not_abstract():
    assert not inspect.isabstract(diagraph_DNode)


def test_diagraph_dnode_constructor_exists():
    assert callable(diagraph_DNode.__init__)


def test_diagraph_dnode_constructor_args():
    sig = inspect.signature(diagraph_DNode.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"
    assert "navigationLink" in params, "Missing parameter 'navigationLink'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagraph_dnode_has_layout():
    assert hasattr(diagraph_DNode, "layout")
    descriptor = None
    for klass in diagraph_DNode.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dnode_has_navigationLink():
    assert hasattr(diagraph_DNode, "navigationLink")
    descriptor = None
    for klass in diagraph_DNode.__mro__:
        if "navigationLink" in klass.__dict__:
            descriptor = klass.__dict__["navigationLink"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dnode_has_shape():
    assert hasattr(diagraph_DNode, "shape")
    descriptor = None
    for klass in diagraph_DNode.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_downedelement_is_not_abstract():
    assert not inspect.isabstract(diagraph_DOwnedElement)


def test_diagraph_downedelement_constructor_exists():
    assert callable(diagraph_DOwnedElement.__init__)


def test_diagraph_downedelement_constructor_args():
    sig = inspect.signature(diagraph_DOwnedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dlabel_is_not_abstract():
    assert not inspect.isabstract(diagraph_DLabel)


def test_diagraph_dlabel_constructor_exists():
    assert callable(diagraph_DLabel.__init__)


def test_diagraph_dlabel_constructor_args():
    sig = inspect.signature(diagraph_DLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inferred" in params, "Missing parameter 'inferred'"
    assert "propagated" in params, "Missing parameter 'propagated'"
    assert "abztract" in params, "Missing parameter 'abztract'"

def test_diagraph_dlabel_has_inferred():
    assert hasattr(diagraph_DLabel, "inferred")
    descriptor = None
    for klass in diagraph_DLabel.__mro__:
        if "inferred" in klass.__dict__:
            descriptor = klass.__dict__["inferred"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dlabel_has_propagated():
    assert hasattr(diagraph_DLabel, "propagated")
    descriptor = None
    for klass in diagraph_DLabel.__mro__:
        if "propagated" in klass.__dict__:
            descriptor = klass.__dict__["propagated"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dlabel_has_abztract():
    assert hasattr(diagraph_DLabel, "abztract")
    descriptor = None
    for klass in diagraph_DLabel.__mro__:
        if "abztract" in klass.__dict__:
            descriptor = klass.__dict__["abztract"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_eclass_is_not_abstract():
    assert not inspect.isabstract(diagraph_EClass)


def test_diagraph_eclass_constructor_exists():
    assert callable(diagraph_EClass.__init__)


def test_diagraph_eclass_constructor_args():
    sig = inspect.signature(diagraph_EClass.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dpointofview_is_not_abstract():
    assert not inspect.isabstract(diagraph_DPointOfView)


def test_diagraph_dpointofview_constructor_exists():
    assert callable(diagraph_DPointOfView.__init__)


def test_diagraph_dpointofview_constructor_args():
    sig = inspect.signature(diagraph_DPointOfView.__init__)
    params = list(sig.parameters.keys())



def test_dgraphelement_is_not_abstract():
    assert not inspect.isabstract(DGraphElement)


def test_dgraphelement_constructor_exists():
    assert callable(DGraphElement.__init__)


def test_dgraphelement_constructor_args():
    sig = inspect.signature(DGraphElement.__init__)
    params = list(sig.parameters.keys())



def test_diagraph_dlabeledelement_is_not_abstract():
    assert not inspect.isabstract(diagraph_DLabeledElement)


def test_diagraph_dlabeledelement_constructor_exists():
    assert callable(diagraph_DLabeledElement.__init__)


def test_diagraph_dlabeledelement_constructor_args():
    sig = inspect.signature(diagraph_DLabeledElement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "labls" in params, "Missing parameter 'labls'"

def test_diagraph_dlabeledelement_has_expression():
    assert hasattr(diagraph_DLabeledElement, "expression")
    descriptor = None
    for klass in diagraph_DLabeledElement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_diagraph_dlabeledelement_has_labls():
    assert hasattr(diagraph_DLabeledElement, "labls")
    descriptor = None
    for klass in diagraph_DLabeledElement.__mro__:
        if "labls" in klass.__dict__:
            descriptor = klass.__dict__["labls"]
            break
    assert isinstance(descriptor, property)



def test_diagraph_dedge_is_not_abstract():
    assert not inspect.isabstract(diagraph_DEdge)


def test_diagraph_dedge_constructor_exists():
    assert callable(diagraph_DEdge.__init__)


def test_diagraph_dedge_constructor_args():
    sig = inspect.signature(diagraph_DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "propagated" in params, "Missing parameter 'propagated'"

def test_diagraph_dedge_has_propagated():
    assert hasattr(diagraph_DEdge, "propagated")
    descriptor = None
    for klass in diagraph_DEdge.__mro__:
        if "propagated" in klass.__dict__:
            descriptor = klass.__dict__["propagated"]
            break
    assert isinstance(descriptor, property)

def test_dshape_exists():
    # Check that the Enumeration exists
    assert DShape is not None

def test_dshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DShape]
    expected_literals = [
        "rectangle",
        "vee",
        "roundedRect",
        "triangle",
        "circle",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DShape"


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
DSimpleEdge_strategy = st.builds(
    DSimpleEdge,
)
diagraph_DNavigationEdge_strategy = st.builds(
    diagraph_DNavigationEdge,
)
diagraph_DLineEdge_strategy = st.builds(
    diagraph_DLineEdge,
    arrows=
        safe_text
)
diagraph_EAttribute_strategy = st.builds(
    diagraph_EAttribute,
)
DNode_strategy = st.builds(
    DNode,
)
DNestedEdge_strategy = st.builds(
    DNestedEdge,
)
diagraph_DAffixedEdge_strategy = st.builds(
    diagraph_DAffixedEdge,
)
diagraph_DCompartmentEdge_strategy = st.builds(
    diagraph_DCompartmentEdge,
    partitionName=
        safe_text,
    depth=
        st.integers()
)
DEdge_strategy = st.builds(
    DEdge,
)
diagraph_DSimpleEdge_strategy = st.builds(
    diagraph_DSimpleEdge,
)
DLineEdge_strategy = st.builds(
    DLineEdge,
)
diagraph_DReference_strategy = st.builds(
    diagraph_DReference,
)
DOwnedEdge_strategy = st.builds(
    DOwnedEdge,
)
diagraph_DNestedEdge_strategy = st.builds(
    diagraph_DNestedEdge,
)
diagraph_DContainment_strategy = st.builds(
    diagraph_DContainment,
    name=
        safe_text
)
diagraph_DViewNavigation_strategy = st.builds(
    diagraph_DViewNavigation,
    id=
        safe_text
)
DOwnedElement_strategy = st.builds(
    DOwnedElement,
)
diagraph_DOwnedEdge_strategy = st.builds(
    diagraph_DOwnedEdge,
)
DLabeledElement_strategy = st.builds(
    DLabeledElement,
)
diagraph_DGeneric_strategy = st.builds(
    diagraph_DGeneric,
)
diagraph_DLabeledEdge_strategy = st.builds(
    diagraph_DLabeledEdge,
)
diagraph_DGraph_strategy = st.builds(
    diagraph_DGraph,
    viewName=
        safe_text,
    facade2=
        safe_text,
    facade1=
        safe_text
)
diagraph_ENamedElement_strategy = st.builds(
    diagraph_ENamedElement,
)
diagraph_DGraphElement_strategy = st.builds(
    diagraph_DGraphElement,
    name=
        safe_text,
    icon=
        safe_text,
    abztract=
        st.booleans()
)
diagraph_EReference_strategy = st.builds(
    diagraph_EReference,
)
diagraph_DNode_strategy = st.builds(
    diagraph_DNode,
    layout=
        st.booleans(),
    navigationLink=
        safe_text,
    shape=
        safe_text
)
diagraph_DOwnedElement_strategy = st.builds(
    diagraph_DOwnedElement,
)
diagraph_DLabel_strategy = st.builds(
    diagraph_DLabel,
    inferred=
        st.booleans(),
    propagated=
        st.booleans(),
    abztract=
        st.booleans()
)
diagraph_EClass_strategy = st.builds(
    diagraph_EClass,
)
diagraph_DPointOfView_strategy = st.builds(
    diagraph_DPointOfView,
)
DGraphElement_strategy = st.builds(
    DGraphElement,
)
diagraph_DLabeledElement_strategy = st.builds(
    diagraph_DLabeledElement,
    expression=
        safe_text,
    labls=
        safe_text
)
diagraph_DEdge_strategy = st.builds(
    diagraph_DEdge,
    propagated=
        st.booleans()
)

@given(instance=DSimpleEdge_strategy)
@settings(max_examples=50)
def test_dsimpleedge_instantiation(instance):
    assert isinstance(instance, DSimpleEdge)

@given(instance=diagraph_DNavigationEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dnavigationedge_instantiation(instance):
    assert isinstance(instance, diagraph_DNavigationEdge)

@given(instance=diagraph_DLineEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dlineedge_instantiation(instance):
    assert isinstance(instance, diagraph_DLineEdge)



@given(instance=diagraph_DLineEdge_strategy)
def test_diagraph_dlineedge_arrows_setter(instance):
    original = instance.arrows
    instance.arrows = original
    assert instance.arrows == original

@given(instance=diagraph_EAttribute_strategy)
@settings(max_examples=50)
def test_diagraph_eattribute_instantiation(instance):
    assert isinstance(instance, diagraph_EAttribute)

@given(instance=DNode_strategy)
@settings(max_examples=50)
def test_dnode_instantiation(instance):
    assert isinstance(instance, DNode)

@given(instance=DNestedEdge_strategy)
@settings(max_examples=50)
def test_dnestededge_instantiation(instance):
    assert isinstance(instance, DNestedEdge)

@given(instance=diagraph_DAffixedEdge_strategy)
@settings(max_examples=50)
def test_diagraph_daffixededge_instantiation(instance):
    assert isinstance(instance, diagraph_DAffixedEdge)

@given(instance=diagraph_DCompartmentEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dcompartmentedge_instantiation(instance):
    assert isinstance(instance, diagraph_DCompartmentEdge)



@given(instance=diagraph_DCompartmentEdge_strategy)
def test_diagraph_dcompartmentedge_partitionName_setter(instance):
    original = instance.partitionName
    instance.partitionName = original
    assert instance.partitionName == original



@given(instance=diagraph_DCompartmentEdge_strategy)
def test_diagraph_dcompartmentedge_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=DEdge_strategy)
@settings(max_examples=50)
def test_dedge_instantiation(instance):
    assert isinstance(instance, DEdge)

@given(instance=diagraph_DSimpleEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dsimpleedge_instantiation(instance):
    assert isinstance(instance, diagraph_DSimpleEdge)

@given(instance=DLineEdge_strategy)
@settings(max_examples=50)
def test_dlineedge_instantiation(instance):
    assert isinstance(instance, DLineEdge)

@given(instance=diagraph_DReference_strategy)
@settings(max_examples=50)
def test_diagraph_dreference_instantiation(instance):
    assert isinstance(instance, diagraph_DReference)

@given(instance=DOwnedEdge_strategy)
@settings(max_examples=50)
def test_downededge_instantiation(instance):
    assert isinstance(instance, DOwnedEdge)

@given(instance=diagraph_DNestedEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dnestededge_instantiation(instance):
    assert isinstance(instance, diagraph_DNestedEdge)

@given(instance=diagraph_DContainment_strategy)
@settings(max_examples=50)
def test_diagraph_dcontainment_instantiation(instance):
    assert isinstance(instance, diagraph_DContainment)



@given(instance=diagraph_DContainment_strategy)
def test_diagraph_dcontainment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=diagraph_DViewNavigation_strategy)
@settings(max_examples=50)
def test_diagraph_dviewnavigation_instantiation(instance):
    assert isinstance(instance, diagraph_DViewNavigation)



@given(instance=diagraph_DViewNavigation_strategy)
def test_diagraph_dviewnavigation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=DOwnedElement_strategy)
@settings(max_examples=50)
def test_downedelement_instantiation(instance):
    assert isinstance(instance, DOwnedElement)

@given(instance=diagraph_DOwnedEdge_strategy)
@settings(max_examples=50)
def test_diagraph_downededge_instantiation(instance):
    assert isinstance(instance, diagraph_DOwnedEdge)

@given(instance=DLabeledElement_strategy)
@settings(max_examples=50)
def test_dlabeledelement_instantiation(instance):
    assert isinstance(instance, DLabeledElement)

@given(instance=diagraph_DGeneric_strategy)
@settings(max_examples=50)
def test_diagraph_dgeneric_instantiation(instance):
    assert isinstance(instance, diagraph_DGeneric)

@given(instance=diagraph_DLabeledEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dlabelededge_instantiation(instance):
    assert isinstance(instance, diagraph_DLabeledEdge)

@given(instance=diagraph_DGraph_strategy)
@settings(max_examples=50)
def test_diagraph_dgraph_instantiation(instance):
    assert isinstance(instance, diagraph_DGraph)



@given(instance=diagraph_DGraph_strategy)
def test_diagraph_dgraph_viewName_setter(instance):
    original = instance.viewName
    instance.viewName = original
    assert instance.viewName == original



@given(instance=diagraph_DGraph_strategy)
def test_diagraph_dgraph_facade2_setter(instance):
    original = instance.facade2
    instance.facade2 = original
    assert instance.facade2 == original



@given(instance=diagraph_DGraph_strategy)
def test_diagraph_dgraph_facade1_setter(instance):
    original = instance.facade1
    instance.facade1 = original
    assert instance.facade1 == original

@given(instance=diagraph_ENamedElement_strategy)
@settings(max_examples=50)
def test_diagraph_enamedelement_instantiation(instance):
    assert isinstance(instance, diagraph_ENamedElement)

@given(instance=diagraph_DGraphElement_strategy)
@settings(max_examples=50)
def test_diagraph_dgraphelement_instantiation(instance):
    assert isinstance(instance, diagraph_DGraphElement)



@given(instance=diagraph_DGraphElement_strategy)
def test_diagraph_dgraphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=diagraph_DGraphElement_strategy)
def test_diagraph_dgraphelement_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=diagraph_DGraphElement_strategy)
def test_diagraph_dgraphelement_abztract_setter(instance):
    original = instance.abztract
    instance.abztract = original
    assert instance.abztract == original

@given(instance=diagraph_EReference_strategy)
@settings(max_examples=50)
def test_diagraph_ereference_instantiation(instance):
    assert isinstance(instance, diagraph_EReference)

@given(instance=diagraph_DNode_strategy)
@settings(max_examples=50)
def test_diagraph_dnode_instantiation(instance):
    assert isinstance(instance, diagraph_DNode)



@given(instance=diagraph_DNode_strategy)
def test_diagraph_dnode_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original



@given(instance=diagraph_DNode_strategy)
def test_diagraph_dnode_navigationLink_setter(instance):
    original = instance.navigationLink
    instance.navigationLink = original
    assert instance.navigationLink == original



@given(instance=diagraph_DNode_strategy)
def test_diagraph_dnode_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagraph_DOwnedElement_strategy)
@settings(max_examples=50)
def test_diagraph_downedelement_instantiation(instance):
    assert isinstance(instance, diagraph_DOwnedElement)

@given(instance=diagraph_DLabel_strategy)
@settings(max_examples=50)
def test_diagraph_dlabel_instantiation(instance):
    assert isinstance(instance, diagraph_DLabel)



@given(instance=diagraph_DLabel_strategy)
def test_diagraph_dlabel_inferred_setter(instance):
    original = instance.inferred
    instance.inferred = original
    assert instance.inferred == original



@given(instance=diagraph_DLabel_strategy)
def test_diagraph_dlabel_propagated_setter(instance):
    original = instance.propagated
    instance.propagated = original
    assert instance.propagated == original



@given(instance=diagraph_DLabel_strategy)
def test_diagraph_dlabel_abztract_setter(instance):
    original = instance.abztract
    instance.abztract = original
    assert instance.abztract == original

@given(instance=diagraph_EClass_strategy)
@settings(max_examples=50)
def test_diagraph_eclass_instantiation(instance):
    assert isinstance(instance, diagraph_EClass)

@given(instance=diagraph_DPointOfView_strategy)
@settings(max_examples=50)
def test_diagraph_dpointofview_instantiation(instance):
    assert isinstance(instance, diagraph_DPointOfView)

@given(instance=DGraphElement_strategy)
@settings(max_examples=50)
def test_dgraphelement_instantiation(instance):
    assert isinstance(instance, DGraphElement)

@given(instance=diagraph_DLabeledElement_strategy)
@settings(max_examples=50)
def test_diagraph_dlabeledelement_instantiation(instance):
    assert isinstance(instance, diagraph_DLabeledElement)



@given(instance=diagraph_DLabeledElement_strategy)
def test_diagraph_dlabeledelement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=diagraph_DLabeledElement_strategy)
def test_diagraph_dlabeledelement_labls_setter(instance):
    original = instance.labls
    instance.labls = original
    assert instance.labls == original

@given(instance=diagraph_DEdge_strategy)
@settings(max_examples=50)
def test_diagraph_dedge_instantiation(instance):
    assert isinstance(instance, diagraph_DEdge)



@given(instance=diagraph_DEdge_strategy)
def test_diagraph_dedge_propagated_setter(instance):
    original = instance.propagated
    instance.propagated = original
    assert instance.propagated == original
