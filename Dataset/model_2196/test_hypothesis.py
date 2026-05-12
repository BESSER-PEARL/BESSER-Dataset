import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ensemble,
    datamodel_ConcreteEnsemble,
    datamodel_EmptyEnsemble,
    datamodel_TreeNode,
    datamodel_SliceRepository,
    datamodel_Slice,
    datamodel_Constraint,
    TreeNode,
    datamodel_EnsembleRepository,
    datamodel_Ensemble,
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



def test_datamodel_concreteensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel_ConcreteEnsemble)


def test_datamodel_concreteensemble_constructor_exists():
    assert callable(datamodel_ConcreteEnsemble.__init__)


def test_datamodel_concreteensemble_constructor_args():
    sig = inspect.signature(datamodel_ConcreteEnsemble.__init__)
    params = list(sig.parameters.keys())



def test_datamodel_emptyensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel_EmptyEnsemble)


def test_datamodel_emptyensemble_constructor_exists():
    assert callable(datamodel_EmptyEnsemble.__init__)


def test_datamodel_emptyensemble_constructor_args():
    sig = inspect.signature(datamodel_EmptyEnsemble.__init__)
    params = list(sig.parameters.keys())



def test_datamodel_treenode_is_not_abstract():
    assert not inspect.isabstract(datamodel_TreeNode)


def test_datamodel_treenode_constructor_exists():
    assert callable(datamodel_TreeNode.__init__)


def test_datamodel_treenode_constructor_args():
    sig = inspect.signature(datamodel_TreeNode.__init__)
    params = list(sig.parameters.keys())



def test_datamodel_slicerepository_is_not_abstract():
    assert not inspect.isabstract(datamodel_SliceRepository)


def test_datamodel_slicerepository_constructor_exists():
    assert callable(datamodel_SliceRepository.__init__)


def test_datamodel_slicerepository_constructor_args():
    sig = inspect.signature(datamodel_SliceRepository.__init__)
    params = list(sig.parameters.keys())



def test_datamodel_slice_is_not_abstract():
    assert not inspect.isabstract(datamodel_Slice)


def test_datamodel_slice_constructor_exists():
    assert callable(datamodel_Slice.__init__)


def test_datamodel_slice_constructor_args():
    sig = inspect.signature(datamodel_Slice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "diagram" in params, "Missing parameter 'diagram'"

def test_datamodel_slice_has_name():
    assert hasattr(datamodel_Slice, "name")
    descriptor = None
    for klass in datamodel_Slice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datamodel_slice_has_diagram():
    assert hasattr(datamodel_Slice, "diagram")
    descriptor = None
    for klass in datamodel_Slice.__mro__:
        if "diagram" in klass.__dict__:
            descriptor = klass.__dict__["diagram"]
            break
    assert isinstance(descriptor, property)



def test_datamodel_constraint_is_not_abstract():
    assert not inspect.isabstract(datamodel_Constraint)


def test_datamodel_constraint_constructor_exists():
    assert callable(datamodel_Constraint.__init__)


def test_datamodel_constraint_constructor_args():
    sig = inspect.signature(datamodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "dependencyKind" in params, "Missing parameter 'dependencyKind'"
    assert "constraintType" in params, "Missing parameter 'constraintType'"

def test_datamodel_constraint_has_dependencyKind():
    assert hasattr(datamodel_Constraint, "dependencyKind")
    descriptor = None
    for klass in datamodel_Constraint.__mro__:
        if "dependencyKind" in klass.__dict__:
            descriptor = klass.__dict__["dependencyKind"]
            break
    assert isinstance(descriptor, property)

def test_datamodel_constraint_has_constraintType():
    assert hasattr(datamodel_Constraint, "constraintType")
    descriptor = None
    for klass in datamodel_Constraint.__mro__:
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



def test_datamodel_ensemblerepository_is_not_abstract():
    assert not inspect.isabstract(datamodel_EnsembleRepository)


def test_datamodel_ensemblerepository_constructor_exists():
    assert callable(datamodel_EnsembleRepository.__init__)


def test_datamodel_ensemblerepository_constructor_args():
    sig = inspect.signature(datamodel_EnsembleRepository.__init__)
    params = list(sig.parameters.keys())



def test_datamodel_ensemble_is_not_abstract():
    assert not inspect.isabstract(datamodel_Ensemble)


def test_datamodel_ensemble_constructor_exists():
    assert callable(datamodel_Ensemble.__init__)


def test_datamodel_ensemble_constructor_args():
    sig = inspect.signature(datamodel_Ensemble.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "query" in params, "Missing parameter 'query'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "name" in params, "Missing parameter 'name'"

def test_datamodel_ensemble_has_description():
    assert hasattr(datamodel_Ensemble, "description")
    descriptor = None
    for klass in datamodel_Ensemble.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datamodel_ensemble_has_query():
    assert hasattr(datamodel_Ensemble, "query")
    descriptor = None
    for klass in datamodel_Ensemble.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_datamodel_ensemble_has_derived():
    assert hasattr(datamodel_Ensemble, "derived")
    descriptor = None
    for klass in datamodel_Ensemble.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_datamodel_ensemble_has_name():
    assert hasattr(datamodel_Ensemble, "name")
    descriptor = None
    for klass in datamodel_Ensemble.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "LocalOutgoing",
        "GlobalIncoming",
        "Expected",
        "LocalIncoming",
        "Undefined",
        "NotAllowed",
        "GlobalOutgoing",
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
datamodel_ConcreteEnsemble_strategy = st.builds(
    datamodel_ConcreteEnsemble,
)
datamodel_EmptyEnsemble_strategy = st.builds(
    datamodel_EmptyEnsemble,
)
datamodel_TreeNode_strategy = st.builds(
    datamodel_TreeNode,
)
datamodel_SliceRepository_strategy = st.builds(
    datamodel_SliceRepository,
)
datamodel_Slice_strategy = st.builds(
    datamodel_Slice,
    name=
        safe_text,
    diagram=
        safe_text
)
datamodel_Constraint_strategy = st.builds(
    datamodel_Constraint,
    dependencyKind=
        safe_text,
    constraintType=
        safe_text
)
TreeNode_strategy = st.builds(
    TreeNode,
)
datamodel_EnsembleRepository_strategy = st.builds(
    datamodel_EnsembleRepository,
)
datamodel_Ensemble_strategy = st.builds(
    datamodel_Ensemble,
    description=
        safe_text,
    query=
        safe_text,
    derived=
        st.booleans(),
    name=
        safe_text
)

@given(instance=Ensemble_strategy)
@settings(max_examples=50)
def test_ensemble_instantiation(instance):
    assert isinstance(instance, Ensemble)

@given(instance=datamodel_ConcreteEnsemble_strategy)
@settings(max_examples=50)
def test_datamodel_concreteensemble_instantiation(instance):
    assert isinstance(instance, datamodel_ConcreteEnsemble)

@given(instance=datamodel_EmptyEnsemble_strategy)
@settings(max_examples=50)
def test_datamodel_emptyensemble_instantiation(instance):
    assert isinstance(instance, datamodel_EmptyEnsemble)

@given(instance=datamodel_TreeNode_strategy)
@settings(max_examples=50)
def test_datamodel_treenode_instantiation(instance):
    assert isinstance(instance, datamodel_TreeNode)

@given(instance=datamodel_SliceRepository_strategy)
@settings(max_examples=50)
def test_datamodel_slicerepository_instantiation(instance):
    assert isinstance(instance, datamodel_SliceRepository)

@given(instance=datamodel_Slice_strategy)
@settings(max_examples=50)
def test_datamodel_slice_instantiation(instance):
    assert isinstance(instance, datamodel_Slice)



@given(instance=datamodel_Slice_strategy)
def test_datamodel_slice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=datamodel_Slice_strategy)
def test_datamodel_slice_diagram_setter(instance):
    original = instance.diagram
    instance.diagram = original
    assert instance.diagram == original

@given(instance=datamodel_Constraint_strategy)
@settings(max_examples=50)
def test_datamodel_constraint_instantiation(instance):
    assert isinstance(instance, datamodel_Constraint)



@given(instance=datamodel_Constraint_strategy)
def test_datamodel_constraint_dependencyKind_setter(instance):
    original = instance.dependencyKind
    instance.dependencyKind = original
    assert instance.dependencyKind == original



@given(instance=datamodel_Constraint_strategy)
def test_datamodel_constraint_constraintType_setter(instance):
    original = instance.constraintType
    instance.constraintType = original
    assert instance.constraintType == original

@given(instance=TreeNode_strategy)
@settings(max_examples=50)
def test_treenode_instantiation(instance):
    assert isinstance(instance, TreeNode)

@given(instance=datamodel_EnsembleRepository_strategy)
@settings(max_examples=50)
def test_datamodel_ensemblerepository_instantiation(instance):
    assert isinstance(instance, datamodel_EnsembleRepository)

@given(instance=datamodel_Ensemble_strategy)
@settings(max_examples=50)
def test_datamodel_ensemble_instantiation(instance):
    assert isinstance(instance, datamodel_Ensemble)



@given(instance=datamodel_Ensemble_strategy)
def test_datamodel_ensemble_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=datamodel_Ensemble_strategy)
def test_datamodel_ensemble_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=datamodel_Ensemble_strategy)
def test_datamodel_ensemble_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=datamodel_Ensemble_strategy)
def test_datamodel_ensemble_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
