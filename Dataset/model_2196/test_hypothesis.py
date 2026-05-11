import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Ensemble,
    datamodel::ConcreteEnsemble,
    datamodel::EmptyEnsemble,
    datamodel::TreeNode,
    datamodel::SliceRepository,
    datamodel::Slice,
    datamodel::Constraint,
    TreeNode,
    datamodel::EnsembleRepository,
    datamodel::Ensemble,
    ConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ensemble_is_not_abstract():
    assert not inspect.isabstract(Ensemble)


def test_ensemble_constructor_exists():
    assert callable(Ensemble.__init__)


def test_ensemble_constructor_args():
    sig = inspect.signature(Ensemble.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::concreteensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel::ConcreteEnsemble)


def test_datamodel::concreteensemble_constructor_exists():
    assert callable(datamodel::ConcreteEnsemble.__init__)


def test_datamodel::concreteensemble_constructor_args():
    sig = inspect.signature(datamodel::ConcreteEnsemble.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::emptyensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel::EmptyEnsemble)


def test_datamodel::emptyensemble_constructor_exists():
    assert callable(datamodel::EmptyEnsemble.__init__)


def test_datamodel::emptyensemble_constructor_args():
    sig = inspect.signature(datamodel::EmptyEnsemble.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::treenode_is_not_abstract():
    assert not inspect.isabstract(datamodel::TreeNode)


def test_datamodel::treenode_constructor_exists():
    assert callable(datamodel::TreeNode.__init__)


def test_datamodel::treenode_constructor_args():
    sig = inspect.signature(datamodel::TreeNode.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::slicerepository_is_not_abstract():
    assert not inspect.isabstract(datamodel::SliceRepository)


def test_datamodel::slicerepository_constructor_exists():
    assert callable(datamodel::SliceRepository.__init__)


def test_datamodel::slicerepository_constructor_args():
    sig = inspect.signature(datamodel::SliceRepository.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::slice_is_not_abstract():
    assert not inspect.isabstract(datamodel::Slice)


def test_datamodel::slice_constructor_exists():
    assert callable(datamodel::Slice.__init__)


def test_datamodel::slice_constructor_args():
    sig = inspect.signature(datamodel::Slice.__init__)
    params = list(sig.parameters.keys())
    assert "diagram" in params, "Missing parameter 'diagram'"
    assert "name" in params, "Missing parameter 'name'"

def test_datamodel::slice_has_diagram():
    assert hasattr(datamodel::Slice, "diagram")
    descriptor = None
    for klass in datamodel::Slice.__mro__:
        if "diagram" in klass.__dict__:
            descriptor = klass.__dict__["diagram"]
            break
    assert isinstance(descriptor, property)

def test_datamodel::slice_has_name():
    assert hasattr(datamodel::Slice, "name")
    descriptor = None
    for klass in datamodel::Slice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datamodel::constraint_is_not_abstract():
    assert not inspect.isabstract(datamodel::Constraint)


def test_datamodel::constraint_constructor_exists():
    assert callable(datamodel::Constraint.__init__)


def test_datamodel::constraint_constructor_args():
    sig = inspect.signature(datamodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "dependencyKind" in params, "Missing parameter 'dependencyKind'"
    assert "constraintType" in params, "Missing parameter 'constraintType'"

def test_datamodel::constraint_has_dependencyKind():
    assert hasattr(datamodel::Constraint, "dependencyKind")
    descriptor = None
    for klass in datamodel::Constraint.__mro__:
        if "dependencyKind" in klass.__dict__:
            descriptor = klass.__dict__["dependencyKind"]
            break
    assert isinstance(descriptor, property)

def test_datamodel::constraint_has_constraintType():
    assert hasattr(datamodel::Constraint, "constraintType")
    descriptor = None
    for klass in datamodel::Constraint.__mro__:
        if "constraintType" in klass.__dict__:
            descriptor = klass.__dict__["constraintType"]
            break
    assert isinstance(descriptor, property)



def test_treenode_is_not_abstract():
    assert not inspect.isabstract(TreeNode)


def test_treenode_constructor_exists():
    assert callable(TreeNode.__init__)


def test_treenode_constructor_args():
    sig = inspect.signature(TreeNode.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::ensemblerepository_is_not_abstract():
    assert not inspect.isabstract(datamodel::EnsembleRepository)


def test_datamodel::ensemblerepository_constructor_exists():
    assert callable(datamodel::EnsembleRepository.__init__)


def test_datamodel::ensemblerepository_constructor_args():
    sig = inspect.signature(datamodel::EnsembleRepository.__init__)
    params = list(sig.parameters.keys())



def test_datamodel::ensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel::Ensemble)


def test_datamodel::ensemble_constructor_exists():
    assert callable(datamodel::Ensemble.__init__)


def test_datamodel::ensemble_constructor_args():
    sig = inspect.signature(datamodel::Ensemble.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "query" in params, "Missing parameter 'query'"

def test_datamodel::ensemble_has_derived():
    assert hasattr(datamodel::Ensemble, "derived")
    descriptor = None
    for klass in datamodel::Ensemble.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_datamodel::ensemble_has_description():
    assert hasattr(datamodel::Ensemble, "description")
    descriptor = None
    for klass in datamodel::Ensemble.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datamodel::ensemble_has_name():
    assert hasattr(datamodel::Ensemble, "name")
    descriptor = None
    for klass in datamodel::Ensemble.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datamodel::ensemble_has_query():
    assert hasattr(datamodel::Ensemble, "query")
    descriptor = None
    for klass in datamodel::Ensemble.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "Expected",
        "Undefined",
        "GlobalOutgoing",
        "LocalIncoming",
        "GlobalIncoming",
        "LocalOutgoing",
        "NotAllowed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"


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
Ensemble_strategy = st.builds(
    Ensemble,
)
datamodel::ConcreteEnsemble_strategy = st.builds(
    datamodel::ConcreteEnsemble,
)
datamodel::EmptyEnsemble_strategy = st.builds(
    datamodel::EmptyEnsemble,
)
datamodel::TreeNode_strategy = st.builds(
    datamodel::TreeNode,
)
datamodel::SliceRepository_strategy = st.builds(
    datamodel::SliceRepository,
)
datamodel::Slice_strategy = st.builds(
    datamodel::Slice,
    diagram=
        safe_text,
    name=
        safe_text
)
datamodel::Constraint_strategy = st.builds(
    datamodel::Constraint,
    dependencyKind=
        safe_text,
    constraintType=
        safe_text
)
TreeNode_strategy = st.builds(
    TreeNode,
)
datamodel::EnsembleRepository_strategy = st.builds(
    datamodel::EnsembleRepository,
)
datamodel::Ensemble_strategy = st.builds(
    datamodel::Ensemble,
    derived=
        st.booleans(),
    description=
        safe_text,
    name=
        safe_text,
    query=
        safe_text
)

@given(instance=Ensemble_strategy)
@settings(max_examples=50)
def test_ensemble_instantiation(instance):
    assert isinstance(instance, Ensemble)

@given(instance=datamodel::ConcreteEnsemble_strategy)
@settings(max_examples=50)
def test_datamodel::concreteensemble_instantiation(instance):
    assert isinstance(instance, datamodel::ConcreteEnsemble)

@given(instance=datamodel::EmptyEnsemble_strategy)
@settings(max_examples=50)
def test_datamodel::emptyensemble_instantiation(instance):
    assert isinstance(instance, datamodel::EmptyEnsemble)

@given(instance=datamodel::TreeNode_strategy)
@settings(max_examples=50)
def test_datamodel::treenode_instantiation(instance):
    assert isinstance(instance, datamodel::TreeNode)

@given(instance=datamodel::SliceRepository_strategy)
@settings(max_examples=50)
def test_datamodel::slicerepository_instantiation(instance):
    assert isinstance(instance, datamodel::SliceRepository)

@given(instance=datamodel::Slice_strategy)
@settings(max_examples=50)
def test_datamodel::slice_instantiation(instance):
    assert isinstance(instance, datamodel::Slice)

@given(instance=datamodel::Slice_strategy)
def test_datamodel::slice_diagram_type(instance):
    assert isinstance(instance.diagram, str)


@given(instance=datamodel::Slice_strategy)
def test_datamodel::slice_diagram_setter(instance):
    original = instance.diagram
    instance.diagram = original
    assert instance.diagram == original

@given(instance=datamodel::Slice_strategy)
def test_datamodel::slice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datamodel::Slice_strategy)
def test_datamodel::slice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datamodel::Constraint_strategy)
@settings(max_examples=50)
def test_datamodel::constraint_instantiation(instance):
    assert isinstance(instance, datamodel::Constraint)

@given(instance=datamodel::Constraint_strategy)
def test_datamodel::constraint_dependencyKind_type(instance):
    assert isinstance(instance.dependencyKind, str)


@given(instance=datamodel::Constraint_strategy)
def test_datamodel::constraint_dependencyKind_setter(instance):
    original = instance.dependencyKind
    instance.dependencyKind = original
    assert instance.dependencyKind == original

@given(instance=datamodel::Constraint_strategy)
def test_datamodel::constraint_constraintType_type(instance):
    assert isinstance(instance.constraintType, str)


@given(instance=datamodel::Constraint_strategy)
def test_datamodel::constraint_constraintType_setter(instance):
    original = instance.constraintType
    instance.constraintType = original
    assert instance.constraintType == original

@given(instance=TreeNode_strategy)
@settings(max_examples=50)
def test_treenode_instantiation(instance):
    assert isinstance(instance, TreeNode)

@given(instance=datamodel::EnsembleRepository_strategy)
@settings(max_examples=50)
def test_datamodel::ensemblerepository_instantiation(instance):
    assert isinstance(instance, datamodel::EnsembleRepository)

@given(instance=datamodel::Ensemble_strategy)
@settings(max_examples=50)
def test_datamodel::ensemble_instantiation(instance):
    assert isinstance(instance, datamodel::Ensemble)

@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=datamodel::Ensemble_strategy)
def test_datamodel::ensemble_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original
