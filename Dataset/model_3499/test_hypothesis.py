import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FeatureModel::Feature,
    ConfigConstraint,
    FeatureModel::Or,
    FeatureModel::Xor,
    FeatureModel::And,
    FeatureModel::RootFeature,
    FeatureModel::FeatureModel,
    Constraint,
    FeatureModel::Constraint,
    FeatureModel::ConfigConstraint,
    FeatureModel::FeatureConstraint,
    kind,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(FeatureModel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(FeatureModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel::feature_has_id():
    assert hasattr(FeatureModel::Feature, "id")
    descriptor = None
    for klass in FeatureModel::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_name():
    assert hasattr(FeatureModel::Feature, "name")
    descriptor = None
    for klass in FeatureModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_configconstraint_is_not_abstract():
    assert not inspect.isabstract(ConfigConstraint)


def test_configconstraint_constructor_exists():
    assert callable(ConfigConstraint.__init__)


def test_configconstraint_constructor_args():
    sig = inspect.signature(ConfigConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::or_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::Or)


def test_featuremodel::or_constructor_exists():
    assert callable(FeatureModel::Or.__init__)


def test_featuremodel::or_constructor_args():
    sig = inspect.signature(FeatureModel::Or.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::xor_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::Xor)


def test_featuremodel::xor_constructor_exists():
    assert callable(FeatureModel::Xor.__init__)


def test_featuremodel::xor_constructor_args():
    sig = inspect.signature(FeatureModel::Xor.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::and_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::And)


def test_featuremodel::and_constructor_exists():
    assert callable(FeatureModel::And.__init__)


def test_featuremodel::and_constructor_args():
    sig = inspect.signature(FeatureModel::And.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::rootfeature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::RootFeature)


def test_featuremodel::rootfeature_constructor_exists():
    assert callable(FeatureModel::RootFeature.__init__)


def test_featuremodel::rootfeature_constructor_args():
    sig = inspect.signature(FeatureModel::RootFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::featuremodel_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::FeatureModel)


def test_featuremodel::featuremodel_constructor_exists():
    assert callable(FeatureModel::FeatureModel.__init__)


def test_featuremodel::featuremodel_constructor_args():
    sig = inspect.signature(FeatureModel::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::constraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::Constraint)


def test_featuremodel::constraint_constructor_exists():
    assert callable(FeatureModel::Constraint.__init__)


def test_featuremodel::constraint_constructor_args():
    sig = inspect.signature(FeatureModel::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::configconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::ConfigConstraint)


def test_featuremodel::configconstraint_constructor_exists():
    assert callable(FeatureModel::ConfigConstraint.__init__)


def test_featuremodel::configconstraint_constructor_args():
    sig = inspect.signature(FeatureModel::ConfigConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_featuremodel::configconstraint_has_kind():
    assert hasattr(FeatureModel::ConfigConstraint, "kind")
    descriptor = None
    for klass in FeatureModel::ConfigConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel::FeatureConstraint)


def test_featuremodel::featureconstraint_constructor_exists():
    assert callable(FeatureModel::FeatureConstraint.__init__)


def test_featuremodel::featureconstraint_constructor_args():
    sig = inspect.signature(FeatureModel::FeatureConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::featureconstraint_has_type():
    assert hasattr(FeatureModel::FeatureConstraint, "type")
    descriptor = None
    for klass in FeatureModel::FeatureConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_kind_exists():
    # Check that the Enumeration exists
    assert kind is not None

def test_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in kind]
    expected_literals = [
        "mandatory",
        "optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in kind"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "require",
        "exclude",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
FeatureModel::Feature_strategy = st.builds(
    FeatureModel::Feature,
    id=
        st.integers(),
    name=
        safe_text
)
ConfigConstraint_strategy = st.builds(
    ConfigConstraint,
)
FeatureModel::Or_strategy = st.builds(
    FeatureModel::Or,
)
FeatureModel::Xor_strategy = st.builds(
    FeatureModel::Xor,
)
FeatureModel::And_strategy = st.builds(
    FeatureModel::And,
)
FeatureModel::RootFeature_strategy = st.builds(
    FeatureModel::RootFeature,
)
FeatureModel::FeatureModel_strategy = st.builds(
    FeatureModel::FeatureModel,
)
Constraint_strategy = st.builds(
    Constraint,
)
FeatureModel::Constraint_strategy = st.builds(
    FeatureModel::Constraint,
)
FeatureModel::ConfigConstraint_strategy = st.builds(
    FeatureModel::ConfigConstraint,
    kind=
        safe_text
)
FeatureModel::FeatureConstraint_strategy = st.builds(
    FeatureModel::FeatureConstraint,
    type=
        safe_text
)

@given(instance=FeatureModel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, FeatureModel::Feature)

@given(instance=FeatureModel::Feature_strategy)
def test_featuremodel::feature_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=FeatureModel::Feature_strategy)
def test_featuremodel::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=FeatureModel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FeatureModel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConfigConstraint_strategy)
@settings(max_examples=50)
def test_configconstraint_instantiation(instance):
    assert isinstance(instance, ConfigConstraint)

@given(instance=FeatureModel::Or_strategy)
@settings(max_examples=50)
def test_featuremodel::or_instantiation(instance):
    assert isinstance(instance, FeatureModel::Or)

@given(instance=FeatureModel::Xor_strategy)
@settings(max_examples=50)
def test_featuremodel::xor_instantiation(instance):
    assert isinstance(instance, FeatureModel::Xor)

@given(instance=FeatureModel::And_strategy)
@settings(max_examples=50)
def test_featuremodel::and_instantiation(instance):
    assert isinstance(instance, FeatureModel::And)

@given(instance=FeatureModel::RootFeature_strategy)
@settings(max_examples=50)
def test_featuremodel::rootfeature_instantiation(instance):
    assert isinstance(instance, FeatureModel::RootFeature)

@given(instance=FeatureModel::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel::featuremodel_instantiation(instance):
    assert isinstance(instance, FeatureModel::FeatureModel)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=FeatureModel::Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel::constraint_instantiation(instance):
    assert isinstance(instance, FeatureModel::Constraint)

@given(instance=FeatureModel::ConfigConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::configconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel::ConfigConstraint)

@given(instance=FeatureModel::ConfigConstraint_strategy)
def test_featuremodel::configconstraint_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=FeatureModel::ConfigConstraint_strategy)
def test_featuremodel::configconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FeatureModel::FeatureConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::featureconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel::FeatureConstraint)

@given(instance=FeatureModel::FeatureConstraint_strategy)
def test_featuremodel::featureconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=FeatureModel::FeatureConstraint_strategy)
def test_featuremodel::featureconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
