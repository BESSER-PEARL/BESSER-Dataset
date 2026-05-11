import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    featureModel::Constraint,
    featureModel::Group,
    Group,
    featureModel::PropFormula,
    featureModel::Constraints,
    featureModel::Feature,
    featureModel::FeatureModel,
    featureModel::Proposition,
    Constraint,
    featureModel::ExcludeConstraint,
    featureModel::ImplyConstraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featuremodel::constraint_is_not_abstract():
    assert not inspect.isabstract(featureModel::Constraint)


def test_featuremodel::constraint_constructor_exists():
    assert callable(featureModel::Constraint.__init__)


def test_featuremodel::constraint_constructor_args():
    sig = inspect.signature(featureModel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "nameA" in params, "Missing parameter 'nameA'"
    assert "nameB" in params, "Missing parameter 'nameB'"

def test_featuremodel::constraint_has_nameA():
    assert hasattr(featureModel::Constraint, "nameA")
    descriptor = None
    for klass in featureModel::Constraint.__mro__:
        if "nameA" in klass.__dict__:
            descriptor = klass.__dict__["nameA"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::constraint_has_nameB():
    assert hasattr(featureModel::Constraint, "nameB")
    descriptor = None
    for klass in featureModel::Constraint.__mro__:
        if "nameB" in klass.__dict__:
            descriptor = klass.__dict__["nameB"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::group_is_not_abstract():
    assert not inspect.isabstract(featureModel::Group)


def test_featuremodel::group_constructor_exists():
    assert callable(featureModel::Group.__init__)


def test_featuremodel::group_constructor_args():
    sig = inspect.signature(featureModel::Group.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::propformula_is_not_abstract():
    assert not inspect.isabstract(featureModel::PropFormula)


def test_featuremodel::propformula_constructor_exists():
    assert callable(featureModel::PropFormula.__init__)


def test_featuremodel::propformula_constructor_args():
    sig = inspect.signature(featureModel::PropFormula.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::constraints_is_not_abstract():
    assert not inspect.isabstract(featureModel::Constraints)


def test_featuremodel::constraints_constructor_exists():
    assert callable(featureModel::Constraints.__init__)


def test_featuremodel::constraints_constructor_args():
    sig = inspect.signature(featureModel::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(featureModel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(featureModel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(featureModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel::feature_has_name():
    assert hasattr(featureModel::Feature, "name")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::featuremodel_is_not_abstract():
    assert not inspect.isabstract(featureModel::FeatureModel)


def test_featuremodel::featuremodel_constructor_exists():
    assert callable(featureModel::FeatureModel.__init__)


def test_featuremodel::featuremodel_constructor_args():
    sig = inspect.signature(featureModel::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::proposition_is_not_abstract():
    assert not inspect.isabstract(featureModel::Proposition)


def test_featuremodel::proposition_constructor_exists():
    assert callable(featureModel::Proposition.__init__)


def test_featuremodel::proposition_constructor_args():
    sig = inspect.signature(featureModel::Proposition.__init__)
    params = list(sig.parameters.keys())
    assert "nameA" in params, "Missing parameter 'nameA'"
    assert "nameRest" in params, "Missing parameter 'nameRest'"

def test_featuremodel::proposition_has_nameA():
    assert hasattr(featureModel::Proposition, "nameA")
    descriptor = None
    for klass in featureModel::Proposition.__mro__:
        if "nameA" in klass.__dict__:
            descriptor = klass.__dict__["nameA"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::proposition_has_nameRest():
    assert hasattr(featureModel::Proposition, "nameRest")
    descriptor = None
    for klass in featureModel::Proposition.__mro__:
        if "nameRest" in klass.__dict__:
            descriptor = klass.__dict__["nameRest"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::excludeconstraint_is_not_abstract():
    assert not inspect.isabstract(featureModel::ExcludeConstraint)


def test_featuremodel::excludeconstraint_constructor_exists():
    assert callable(featureModel::ExcludeConstraint.__init__)


def test_featuremodel::excludeconstraint_constructor_args():
    sig = inspect.signature(featureModel::ExcludeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::implyconstraint_is_not_abstract():
    assert not inspect.isabstract(featureModel::ImplyConstraint)


def test_featuremodel::implyconstraint_constructor_exists():
    assert callable(featureModel::ImplyConstraint.__init__)


def test_featuremodel::implyconstraint_constructor_args():
    sig = inspect.signature(featureModel::ImplyConstraint.__init__)
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
featureModel::Constraint_strategy = st.builds(
    featureModel::Constraint,
    nameA=
        safe_text,
    nameB=
        safe_text
)
featureModel::Group_strategy = st.builds(
    featureModel::Group,
)
Group_strategy = st.builds(
    Group,
)
featureModel::PropFormula_strategy = st.builds(
    featureModel::PropFormula,
)
featureModel::Constraints_strategy = st.builds(
    featureModel::Constraints,
)
featureModel::Feature_strategy = st.builds(
    featureModel::Feature,
    name=
        safe_text
)
featureModel::FeatureModel_strategy = st.builds(
    featureModel::FeatureModel,
)
featureModel::Proposition_strategy = st.builds(
    featureModel::Proposition,
    nameA=
        safe_text,
    nameRest=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
featureModel::ExcludeConstraint_strategy = st.builds(
    featureModel::ExcludeConstraint,
)
featureModel::ImplyConstraint_strategy = st.builds(
    featureModel::ImplyConstraint,
)

@given(instance=featureModel::Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel::constraint_instantiation(instance):
    assert isinstance(instance, featureModel::Constraint)

@given(instance=featureModel::Constraint_strategy)
def test_featuremodel::constraint_nameA_type(instance):
    assert isinstance(instance.nameA, str)


@given(instance=featureModel::Constraint_strategy)
def test_featuremodel::constraint_nameA_setter(instance):
    original = instance.nameA
    instance.nameA = original
    assert instance.nameA == original

@given(instance=featureModel::Constraint_strategy)
def test_featuremodel::constraint_nameB_type(instance):
    assert isinstance(instance.nameB, str)


@given(instance=featureModel::Constraint_strategy)
def test_featuremodel::constraint_nameB_setter(instance):
    original = instance.nameB
    instance.nameB = original
    assert instance.nameB == original

@given(instance=featureModel::Group_strategy)
@settings(max_examples=50)
def test_featuremodel::group_instantiation(instance):
    assert isinstance(instance, featureModel::Group)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=featureModel::PropFormula_strategy)
@settings(max_examples=50)
def test_featuremodel::propformula_instantiation(instance):
    assert isinstance(instance, featureModel::PropFormula)

@given(instance=featureModel::Constraints_strategy)
@settings(max_examples=50)
def test_featuremodel::constraints_instantiation(instance):
    assert isinstance(instance, featureModel::Constraints)

@given(instance=featureModel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, featureModel::Feature)

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModel::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel::featuremodel_instantiation(instance):
    assert isinstance(instance, featureModel::FeatureModel)

@given(instance=featureModel::Proposition_strategy)
@settings(max_examples=50)
def test_featuremodel::proposition_instantiation(instance):
    assert isinstance(instance, featureModel::Proposition)

@given(instance=featureModel::Proposition_strategy)
def test_featuremodel::proposition_nameA_type(instance):
    assert isinstance(instance.nameA, str)


@given(instance=featureModel::Proposition_strategy)
def test_featuremodel::proposition_nameA_setter(instance):
    original = instance.nameA
    instance.nameA = original
    assert instance.nameA == original

@given(instance=featureModel::Proposition_strategy)
def test_featuremodel::proposition_nameRest_type(instance):
    assert isinstance(instance.nameRest, str)


@given(instance=featureModel::Proposition_strategy)
def test_featuremodel::proposition_nameRest_setter(instance):
    original = instance.nameRest
    instance.nameRest = original
    assert instance.nameRest == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=featureModel::ExcludeConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::excludeconstraint_instantiation(instance):
    assert isinstance(instance, featureModel::ExcludeConstraint)

@given(instance=featureModel::ImplyConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::implyconstraint_instantiation(instance):
    assert isinstance(instance, featureModel::ImplyConstraint)
