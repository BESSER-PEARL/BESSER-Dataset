import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    afmmm::EClass0,
    afmmm::AttributedFeatureModel,
    Domain,
    afmmm::Real,
    afmmm::Integer,
    afmmm::Enum,
    afmmm::Boolean,
    afmmm::Domain,
    Relation,
    afmmm::Optional,
    afmmm::XOr,
    afmmm::Mutex,
    afmmm::Or,
    afmmm::Mandatory,
    afmmm::Attribute,
    afmmm::Relation,
    afmmm::CrossTreeConstraint,
    afmmm::Feature,
    afmmm::AttributedFeatureDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_afmmm::eclass0_is_not_abstract():
    assert not inspect.isabstract(afmmm::EClass0)


def test_afmmm::eclass0_constructor_exists():
    assert callable(afmmm::EClass0.__init__)


def test_afmmm::eclass0_constructor_args():
    sig = inspect.signature(afmmm::EClass0.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::attributedfeaturemodel_is_not_abstract():
    assert not inspect.isabstract(afmmm::AttributedFeatureModel)


def test_afmmm::attributedfeaturemodel_constructor_exists():
    assert callable(afmmm::AttributedFeatureModel.__init__)


def test_afmmm::attributedfeaturemodel_constructor_args():
    sig = inspect.signature(afmmm::AttributedFeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::real_is_not_abstract():
    assert not inspect.isabstract(afmmm::Real)


def test_afmmm::real_constructor_exists():
    assert callable(afmmm::Real.__init__)


def test_afmmm::real_constructor_args():
    sig = inspect.signature(afmmm::Real.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::integer_is_not_abstract():
    assert not inspect.isabstract(afmmm::Integer)


def test_afmmm::integer_constructor_exists():
    assert callable(afmmm::Integer.__init__)


def test_afmmm::integer_constructor_args():
    sig = inspect.signature(afmmm::Integer.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::enum_is_not_abstract():
    assert not inspect.isabstract(afmmm::Enum)


def test_afmmm::enum_constructor_exists():
    assert callable(afmmm::Enum.__init__)


def test_afmmm::enum_constructor_args():
    sig = inspect.signature(afmmm::Enum.__init__)
    params = list(sig.parameters.keys())
    assert "literals" in params, "Missing parameter 'literals'"

def test_afmmm::enum_has_literals():
    assert hasattr(afmmm::Enum, "literals")
    descriptor = None
    for klass in afmmm::Enum.__mro__:
        if "literals" in klass.__dict__:
            descriptor = klass.__dict__["literals"]
            break
    assert isinstance(descriptor, property)



def test_afmmm::boolean_is_not_abstract():
    assert not inspect.isabstract(afmmm::Boolean)


def test_afmmm::boolean_constructor_exists():
    assert callable(afmmm::Boolean.__init__)


def test_afmmm::boolean_constructor_args():
    sig = inspect.signature(afmmm::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::domain_is_not_abstract():
    assert not inspect.isabstract(afmmm::Domain)


def test_afmmm::domain_constructor_exists():
    assert callable(afmmm::Domain.__init__)


def test_afmmm::domain_constructor_args():
    sig = inspect.signature(afmmm::Domain.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::optional_is_not_abstract():
    assert not inspect.isabstract(afmmm::Optional)


def test_afmmm::optional_constructor_exists():
    assert callable(afmmm::Optional.__init__)


def test_afmmm::optional_constructor_args():
    sig = inspect.signature(afmmm::Optional.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::xor_is_not_abstract():
    assert not inspect.isabstract(afmmm::XOr)


def test_afmmm::xor_constructor_exists():
    assert callable(afmmm::XOr.__init__)


def test_afmmm::xor_constructor_args():
    sig = inspect.signature(afmmm::XOr.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::mutex_is_not_abstract():
    assert not inspect.isabstract(afmmm::Mutex)


def test_afmmm::mutex_constructor_exists():
    assert callable(afmmm::Mutex.__init__)


def test_afmmm::mutex_constructor_args():
    sig = inspect.signature(afmmm::Mutex.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::or_is_not_abstract():
    assert not inspect.isabstract(afmmm::Or)


def test_afmmm::or_constructor_exists():
    assert callable(afmmm::Or.__init__)


def test_afmmm::or_constructor_args():
    sig = inspect.signature(afmmm::Or.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::mandatory_is_not_abstract():
    assert not inspect.isabstract(afmmm::Mandatory)


def test_afmmm::mandatory_constructor_exists():
    assert callable(afmmm::Mandatory.__init__)


def test_afmmm::mandatory_constructor_args():
    sig = inspect.signature(afmmm::Mandatory.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::attribute_is_not_abstract():
    assert not inspect.isabstract(afmmm::Attribute)


def test_afmmm::attribute_constructor_exists():
    assert callable(afmmm::Attribute.__init__)


def test_afmmm::attribute_constructor_args():
    sig = inspect.signature(afmmm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_afmmm::attribute_has_name():
    assert hasattr(afmmm::Attribute, "name")
    descriptor = None
    for klass in afmmm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_afmmm::relation_is_not_abstract():
    assert not inspect.isabstract(afmmm::Relation)


def test_afmmm::relation_constructor_exists():
    assert callable(afmmm::Relation.__init__)


def test_afmmm::relation_constructor_args():
    sig = inspect.signature(afmmm::Relation.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(afmmm::CrossTreeConstraint)


def test_afmmm::crosstreeconstraint_constructor_exists():
    assert callable(afmmm::CrossTreeConstraint.__init__)


def test_afmmm::crosstreeconstraint_constructor_args():
    sig = inspect.signature(afmmm::CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_afmmm::feature_is_not_abstract():
    assert not inspect.isabstract(afmmm::Feature)


def test_afmmm::feature_constructor_exists():
    assert callable(afmmm::Feature.__init__)


def test_afmmm::feature_constructor_args():
    sig = inspect.signature(afmmm::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_afmmm::feature_has_name():
    assert hasattr(afmmm::Feature, "name")
    descriptor = None
    for klass in afmmm::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_afmmm::attributedfeaturediagram_is_not_abstract():
    assert not inspect.isabstract(afmmm::AttributedFeatureDiagram)


def test_afmmm::attributedfeaturediagram_constructor_exists():
    assert callable(afmmm::AttributedFeatureDiagram.__init__)


def test_afmmm::attributedfeaturediagram_constructor_args():
    sig = inspect.signature(afmmm::AttributedFeatureDiagram.__init__)
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
afmmm::EClass0_strategy = st.builds(
    afmmm::EClass0,
)
afmmm::AttributedFeatureModel_strategy = st.builds(
    afmmm::AttributedFeatureModel,
)
Domain_strategy = st.builds(
    Domain,
)
afmmm::Real_strategy = st.builds(
    afmmm::Real,
)
afmmm::Integer_strategy = st.builds(
    afmmm::Integer,
)
afmmm::Enum_strategy = st.builds(
    afmmm::Enum,
    literals=
        safe_text
)
afmmm::Boolean_strategy = st.builds(
    afmmm::Boolean,
)
afmmm::Domain_strategy = st.builds(
    afmmm::Domain,
)
Relation_strategy = st.builds(
    Relation,
)
afmmm::Optional_strategy = st.builds(
    afmmm::Optional,
)
afmmm::XOr_strategy = st.builds(
    afmmm::XOr,
)
afmmm::Mutex_strategy = st.builds(
    afmmm::Mutex,
)
afmmm::Or_strategy = st.builds(
    afmmm::Or,
)
afmmm::Mandatory_strategy = st.builds(
    afmmm::Mandatory,
)
afmmm::Attribute_strategy = st.builds(
    afmmm::Attribute,
    name=
        safe_text
)
afmmm::Relation_strategy = st.builds(
    afmmm::Relation,
)
afmmm::CrossTreeConstraint_strategy = st.builds(
    afmmm::CrossTreeConstraint,
)
afmmm::Feature_strategy = st.builds(
    afmmm::Feature,
    name=
        safe_text
)
afmmm::AttributedFeatureDiagram_strategy = st.builds(
    afmmm::AttributedFeatureDiagram,
)

@given(instance=afmmm::EClass0_strategy)
@settings(max_examples=50)
def test_afmmm::eclass0_instantiation(instance):
    assert isinstance(instance, afmmm::EClass0)

@given(instance=afmmm::AttributedFeatureModel_strategy)
@settings(max_examples=50)
def test_afmmm::attributedfeaturemodel_instantiation(instance):
    assert isinstance(instance, afmmm::AttributedFeatureModel)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=afmmm::Real_strategy)
@settings(max_examples=50)
def test_afmmm::real_instantiation(instance):
    assert isinstance(instance, afmmm::Real)

@given(instance=afmmm::Integer_strategy)
@settings(max_examples=50)
def test_afmmm::integer_instantiation(instance):
    assert isinstance(instance, afmmm::Integer)

@given(instance=afmmm::Enum_strategy)
@settings(max_examples=50)
def test_afmmm::enum_instantiation(instance):
    assert isinstance(instance, afmmm::Enum)

@given(instance=afmmm::Enum_strategy)
def test_afmmm::enum_literals_type(instance):
    assert isinstance(instance.literals, str)


@given(instance=afmmm::Enum_strategy)
def test_afmmm::enum_literals_setter(instance):
    original = instance.literals
    instance.literals = original
    assert instance.literals == original

@given(instance=afmmm::Boolean_strategy)
@settings(max_examples=50)
def test_afmmm::boolean_instantiation(instance):
    assert isinstance(instance, afmmm::Boolean)

@given(instance=afmmm::Domain_strategy)
@settings(max_examples=50)
def test_afmmm::domain_instantiation(instance):
    assert isinstance(instance, afmmm::Domain)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=afmmm::Optional_strategy)
@settings(max_examples=50)
def test_afmmm::optional_instantiation(instance):
    assert isinstance(instance, afmmm::Optional)

@given(instance=afmmm::XOr_strategy)
@settings(max_examples=50)
def test_afmmm::xor_instantiation(instance):
    assert isinstance(instance, afmmm::XOr)

@given(instance=afmmm::Mutex_strategy)
@settings(max_examples=50)
def test_afmmm::mutex_instantiation(instance):
    assert isinstance(instance, afmmm::Mutex)

@given(instance=afmmm::Or_strategy)
@settings(max_examples=50)
def test_afmmm::or_instantiation(instance):
    assert isinstance(instance, afmmm::Or)

@given(instance=afmmm::Mandatory_strategy)
@settings(max_examples=50)
def test_afmmm::mandatory_instantiation(instance):
    assert isinstance(instance, afmmm::Mandatory)

@given(instance=afmmm::Attribute_strategy)
@settings(max_examples=50)
def test_afmmm::attribute_instantiation(instance):
    assert isinstance(instance, afmmm::Attribute)

@given(instance=afmmm::Attribute_strategy)
def test_afmmm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=afmmm::Attribute_strategy)
def test_afmmm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=afmmm::Relation_strategy)
@settings(max_examples=50)
def test_afmmm::relation_instantiation(instance):
    assert isinstance(instance, afmmm::Relation)

@given(instance=afmmm::CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_afmmm::crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, afmmm::CrossTreeConstraint)

@given(instance=afmmm::Feature_strategy)
@settings(max_examples=50)
def test_afmmm::feature_instantiation(instance):
    assert isinstance(instance, afmmm::Feature)

@given(instance=afmmm::Feature_strategy)
def test_afmmm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=afmmm::Feature_strategy)
def test_afmmm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=afmmm::AttributedFeatureDiagram_strategy)
@settings(max_examples=50)
def test_afmmm::attributedfeaturediagram_instantiation(instance):
    assert isinstance(instance, afmmm::AttributedFeatureDiagram)
