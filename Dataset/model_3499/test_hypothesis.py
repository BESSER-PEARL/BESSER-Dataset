import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FeatureModel_Feature,
    ConfigConstraint,
    FeatureModel_Or,
    FeatureModel_Xor,
    FeatureModel_And,
    FeatureModel_RootFeature,
    FeatureModel_FeatureModel,
    Constraint,
    FeatureModel_Constraint,
    FeatureModel_ConfigConstraint,
    FeatureModel_FeatureConstraint,
    Type,
    kind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Feature)


def test_featuremodel_feature_constructor_exists():
    assert callable(FeatureModel_Feature.__init__)


def test_featuremodel_feature_constructor_args():
    sig = inspect.signature(FeatureModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel_feature_has_id():
    assert hasattr(FeatureModel_Feature, "id")
    descriptor = None
    for klass in FeatureModel_Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_feature_has_name():
    assert hasattr(FeatureModel_Feature, "name")
    descriptor = None
    for klass in FeatureModel_Feature.__mro__:
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



def test_featuremodel_or_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Or)


def test_featuremodel_or_constructor_exists():
    assert callable(FeatureModel_Or.__init__)


def test_featuremodel_or_constructor_args():
    sig = inspect.signature(FeatureModel_Or.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_xor_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Xor)


def test_featuremodel_xor_constructor_exists():
    assert callable(FeatureModel_Xor.__init__)


def test_featuremodel_xor_constructor_args():
    sig = inspect.signature(FeatureModel_Xor.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_and_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_And)


def test_featuremodel_and_constructor_exists():
    assert callable(FeatureModel_And.__init__)


def test_featuremodel_and_constructor_args():
    sig = inspect.signature(FeatureModel_And.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_rootfeature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_RootFeature)


def test_featuremodel_rootfeature_constructor_exists():
    assert callable(FeatureModel_RootFeature.__init__)


def test_featuremodel_rootfeature_constructor_args():
    sig = inspect.signature(FeatureModel_RootFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_FeatureModel)


def test_featuremodel_featuremodel_constructor_exists():
    assert callable(FeatureModel_FeatureModel.__init__)


def test_featuremodel_featuremodel_constructor_args():
    sig = inspect.signature(FeatureModel_FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_constraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Constraint)


def test_featuremodel_constraint_constructor_exists():
    assert callable(FeatureModel_Constraint.__init__)


def test_featuremodel_constraint_constructor_args():
    sig = inspect.signature(FeatureModel_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_configconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_ConfigConstraint)


def test_featuremodel_configconstraint_constructor_exists():
    assert callable(FeatureModel_ConfigConstraint.__init__)


def test_featuremodel_configconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_ConfigConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_featuremodel_configconstraint_has_kind():
    assert hasattr(FeatureModel_ConfigConstraint, "kind")
    descriptor = None
    for klass in FeatureModel_ConfigConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_FeatureConstraint)


def test_featuremodel_featureconstraint_constructor_exists():
    assert callable(FeatureModel_FeatureConstraint.__init__)


def test_featuremodel_featureconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_FeatureConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel_featureconstraint_has_type():
    assert hasattr(FeatureModel_FeatureConstraint, "type")
    descriptor = None
    for klass in FeatureModel_FeatureConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

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

def test_kind_exists():
    # Check that the Enumeration exists
    assert kind is not None

def test_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in kind]
    expected_literals = [
        "optional",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in kind"


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
FeatureModel_Feature_strategy = st.builds(
    FeatureModel_Feature,
    id=
        st.integers(),
    name=
        safe_text
)
ConfigConstraint_strategy = st.builds(
    ConfigConstraint,
)
FeatureModel_Or_strategy = st.builds(
    FeatureModel_Or,
)
FeatureModel_Xor_strategy = st.builds(
    FeatureModel_Xor,
)
FeatureModel_And_strategy = st.builds(
    FeatureModel_And,
)
FeatureModel_RootFeature_strategy = st.builds(
    FeatureModel_RootFeature,
)
FeatureModel_FeatureModel_strategy = st.builds(
    FeatureModel_FeatureModel,
)
Constraint_strategy = st.builds(
    Constraint,
)
FeatureModel_Constraint_strategy = st.builds(
    FeatureModel_Constraint,
)
FeatureModel_ConfigConstraint_strategy = st.builds(
    FeatureModel_ConfigConstraint,
    kind=
        safe_text
)
FeatureModel_FeatureConstraint_strategy = st.builds(
    FeatureModel_FeatureConstraint,
    type=
        safe_text
)

@given(instance=FeatureModel_Feature_strategy)
@settings(max_examples=50)
def test_featuremodel_feature_instantiation(instance):
    assert isinstance(instance, FeatureModel_Feature)



@given(instance=FeatureModel_Feature_strategy)
def test_featuremodel_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=FeatureModel_Feature_strategy)
def test_featuremodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConfigConstraint_strategy)
@settings(max_examples=50)
def test_configconstraint_instantiation(instance):
    assert isinstance(instance, ConfigConstraint)

@given(instance=FeatureModel_Or_strategy)
@settings(max_examples=50)
def test_featuremodel_or_instantiation(instance):
    assert isinstance(instance, FeatureModel_Or)

@given(instance=FeatureModel_Xor_strategy)
@settings(max_examples=50)
def test_featuremodel_xor_instantiation(instance):
    assert isinstance(instance, FeatureModel_Xor)

@given(instance=FeatureModel_And_strategy)
@settings(max_examples=50)
def test_featuremodel_and_instantiation(instance):
    assert isinstance(instance, FeatureModel_And)

@given(instance=FeatureModel_RootFeature_strategy)
@settings(max_examples=50)
def test_featuremodel_rootfeature_instantiation(instance):
    assert isinstance(instance, FeatureModel_RootFeature)

@given(instance=FeatureModel_FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel_featuremodel_instantiation(instance):
    assert isinstance(instance, FeatureModel_FeatureModel)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=FeatureModel_Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel_constraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_Constraint)

@given(instance=FeatureModel_ConfigConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel_configconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_ConfigConstraint)



@given(instance=FeatureModel_ConfigConstraint_strategy)
def test_featuremodel_configconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FeatureModel_FeatureConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel_featureconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_FeatureConstraint)



@given(instance=FeatureModel_FeatureConstraint_strategy)
def test_featuremodel_featureconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
