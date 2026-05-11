import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    features::modeling::NOT,
    features::modeling::AND,
    features::modeling::PropositionOR,
    features::modeling::PropFormulaCNF,
    features::modeling::Constraints,
    features::modeling::Group,
    features::modeling::Constraint,
    Constraint,
    features::modeling::EX,
    features::modeling::I,
    Group,
    features::modeling::GOR,
    features::modeling::GXOR,
    E,
    features::modeling::EMAND,
    features::modeling::E,
    features::modeling::Edge,
    features::modeling::F,
    features::modeling::Feature,
    Feature,
    features::modeling::R,
    features::modeling::G,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_features::modeling::not_is_not_abstract():
    assert not inspect.isabstract(features::modeling::NOT)


def test_features::modeling::not_constructor_exists():
    assert callable(features::modeling::NOT.__init__)


def test_features::modeling::not_constructor_args():
    sig = inspect.signature(features::modeling::NOT.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::and_is_not_abstract():
    assert not inspect.isabstract(features::modeling::AND)


def test_features::modeling::and_constructor_exists():
    assert callable(features::modeling::AND.__init__)


def test_features::modeling::and_constructor_args():
    sig = inspect.signature(features::modeling::AND.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::propositionor_is_not_abstract():
    assert not inspect.isabstract(features::modeling::PropositionOR)


def test_features::modeling::propositionor_constructor_exists():
    assert callable(features::modeling::PropositionOR.__init__)


def test_features::modeling::propositionor_constructor_args():
    sig = inspect.signature(features::modeling::PropositionOR.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::propformulacnf_is_not_abstract():
    assert not inspect.isabstract(features::modeling::PropFormulaCNF)


def test_features::modeling::propformulacnf_constructor_exists():
    assert callable(features::modeling::PropFormulaCNF.__init__)


def test_features::modeling::propformulacnf_constructor_args():
    sig = inspect.signature(features::modeling::PropFormulaCNF.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::constraints_is_not_abstract():
    assert not inspect.isabstract(features::modeling::Constraints)


def test_features::modeling::constraints_constructor_exists():
    assert callable(features::modeling::Constraints.__init__)


def test_features::modeling::constraints_constructor_args():
    sig = inspect.signature(features::modeling::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::group_is_not_abstract():
    assert not inspect.isabstract(features::modeling::Group)


def test_features::modeling::group_constructor_exists():
    assert callable(features::modeling::Group.__init__)


def test_features::modeling::group_constructor_args():
    sig = inspect.signature(features::modeling::Group.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::constraint_is_not_abstract():
    assert not inspect.isabstract(features::modeling::Constraint)


def test_features::modeling::constraint_constructor_exists():
    assert callable(features::modeling::Constraint.__init__)


def test_features::modeling::constraint_constructor_args():
    sig = inspect.signature(features::modeling::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::ex_is_not_abstract():
    assert not inspect.isabstract(features::modeling::EX)


def test_features::modeling::ex_constructor_exists():
    assert callable(features::modeling::EX.__init__)


def test_features::modeling::ex_constructor_args():
    sig = inspect.signature(features::modeling::EX.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::i_is_not_abstract():
    assert not inspect.isabstract(features::modeling::I)


def test_features::modeling::i_constructor_exists():
    assert callable(features::modeling::I.__init__)


def test_features::modeling::i_constructor_args():
    sig = inspect.signature(features::modeling::I.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::gor_is_not_abstract():
    assert not inspect.isabstract(features::modeling::GOR)


def test_features::modeling::gor_constructor_exists():
    assert callable(features::modeling::GOR.__init__)


def test_features::modeling::gor_constructor_args():
    sig = inspect.signature(features::modeling::GOR.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::gxor_is_not_abstract():
    assert not inspect.isabstract(features::modeling::GXOR)


def test_features::modeling::gxor_constructor_exists():
    assert callable(features::modeling::GXOR.__init__)


def test_features::modeling::gxor_constructor_args():
    sig = inspect.signature(features::modeling::GXOR.__init__)
    params = list(sig.parameters.keys())



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::emand_is_not_abstract():
    assert not inspect.isabstract(features::modeling::EMAND)


def test_features::modeling::emand_constructor_exists():
    assert callable(features::modeling::EMAND.__init__)


def test_features::modeling::emand_constructor_args():
    sig = inspect.signature(features::modeling::EMAND.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::e_is_not_abstract():
    assert not inspect.isabstract(features::modeling::E)


def test_features::modeling::e_constructor_exists():
    assert callable(features::modeling::E.__init__)


def test_features::modeling::e_constructor_args():
    sig = inspect.signature(features::modeling::E.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::edge_is_not_abstract():
    assert not inspect.isabstract(features::modeling::Edge)


def test_features::modeling::edge_constructor_exists():
    assert callable(features::modeling::Edge.__init__)


def test_features::modeling::edge_constructor_args():
    sig = inspect.signature(features::modeling::Edge.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::f_is_not_abstract():
    assert not inspect.isabstract(features::modeling::F)


def test_features::modeling::f_constructor_exists():
    assert callable(features::modeling::F.__init__)


def test_features::modeling::f_constructor_args():
    sig = inspect.signature(features::modeling::F.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::feature_is_not_abstract():
    assert not inspect.isabstract(features::modeling::Feature)


def test_features::modeling::feature_constructor_exists():
    assert callable(features::modeling::Feature.__init__)


def test_features::modeling::feature_constructor_args():
    sig = inspect.signature(features::modeling::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_features::modeling::feature_has_ID():
    assert hasattr(features::modeling::Feature, "ID")
    descriptor = None
    for klass in features::modeling::Feature.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::r_is_not_abstract():
    assert not inspect.isabstract(features::modeling::R)


def test_features::modeling::r_constructor_exists():
    assert callable(features::modeling::R.__init__)


def test_features::modeling::r_constructor_args():
    sig = inspect.signature(features::modeling::R.__init__)
    params = list(sig.parameters.keys())



def test_features::modeling::g_is_not_abstract():
    assert not inspect.isabstract(features::modeling::G)


def test_features::modeling::g_constructor_exists():
    assert callable(features::modeling::G.__init__)


def test_features::modeling::g_constructor_args():
    sig = inspect.signature(features::modeling::G.__init__)
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
features::modeling::NOT_strategy = st.builds(
    features::modeling::NOT,
)
features::modeling::AND_strategy = st.builds(
    features::modeling::AND,
)
features::modeling::PropositionOR_strategy = st.builds(
    features::modeling::PropositionOR,
)
features::modeling::PropFormulaCNF_strategy = st.builds(
    features::modeling::PropFormulaCNF,
)
features::modeling::Constraints_strategy = st.builds(
    features::modeling::Constraints,
)
features::modeling::Group_strategy = st.builds(
    features::modeling::Group,
)
features::modeling::Constraint_strategy = st.builds(
    features::modeling::Constraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
features::modeling::EX_strategy = st.builds(
    features::modeling::EX,
)
features::modeling::I_strategy = st.builds(
    features::modeling::I,
)
Group_strategy = st.builds(
    Group,
)
features::modeling::GOR_strategy = st.builds(
    features::modeling::GOR,
)
features::modeling::GXOR_strategy = st.builds(
    features::modeling::GXOR,
)
E_strategy = st.builds(
    E,
)
features::modeling::EMAND_strategy = st.builds(
    features::modeling::EMAND,
)
features::modeling::E_strategy = st.builds(
    features::modeling::E,
)
features::modeling::Edge_strategy = st.builds(
    features::modeling::Edge,
)
features::modeling::F_strategy = st.builds(
    features::modeling::F,
)
features::modeling::Feature_strategy = st.builds(
    features::modeling::Feature,
    ID=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
features::modeling::R_strategy = st.builds(
    features::modeling::R,
)
features::modeling::G_strategy = st.builds(
    features::modeling::G,
)

@given(instance=features::modeling::NOT_strategy)
@settings(max_examples=50)
def test_features::modeling::not_instantiation(instance):
    assert isinstance(instance, features::modeling::NOT)

@given(instance=features::modeling::AND_strategy)
@settings(max_examples=50)
def test_features::modeling::and_instantiation(instance):
    assert isinstance(instance, features::modeling::AND)

@given(instance=features::modeling::PropositionOR_strategy)
@settings(max_examples=50)
def test_features::modeling::propositionor_instantiation(instance):
    assert isinstance(instance, features::modeling::PropositionOR)

@given(instance=features::modeling::PropFormulaCNF_strategy)
@settings(max_examples=50)
def test_features::modeling::propformulacnf_instantiation(instance):
    assert isinstance(instance, features::modeling::PropFormulaCNF)

@given(instance=features::modeling::Constraints_strategy)
@settings(max_examples=50)
def test_features::modeling::constraints_instantiation(instance):
    assert isinstance(instance, features::modeling::Constraints)

@given(instance=features::modeling::Group_strategy)
@settings(max_examples=50)
def test_features::modeling::group_instantiation(instance):
    assert isinstance(instance, features::modeling::Group)

@given(instance=features::modeling::Constraint_strategy)
@settings(max_examples=50)
def test_features::modeling::constraint_instantiation(instance):
    assert isinstance(instance, features::modeling::Constraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=features::modeling::EX_strategy)
@settings(max_examples=50)
def test_features::modeling::ex_instantiation(instance):
    assert isinstance(instance, features::modeling::EX)

@given(instance=features::modeling::I_strategy)
@settings(max_examples=50)
def test_features::modeling::i_instantiation(instance):
    assert isinstance(instance, features::modeling::I)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=features::modeling::GOR_strategy)
@settings(max_examples=50)
def test_features::modeling::gor_instantiation(instance):
    assert isinstance(instance, features::modeling::GOR)

@given(instance=features::modeling::GXOR_strategy)
@settings(max_examples=50)
def test_features::modeling::gxor_instantiation(instance):
    assert isinstance(instance, features::modeling::GXOR)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=features::modeling::EMAND_strategy)
@settings(max_examples=50)
def test_features::modeling::emand_instantiation(instance):
    assert isinstance(instance, features::modeling::EMAND)

@given(instance=features::modeling::E_strategy)
@settings(max_examples=50)
def test_features::modeling::e_instantiation(instance):
    assert isinstance(instance, features::modeling::E)

@given(instance=features::modeling::Edge_strategy)
@settings(max_examples=50)
def test_features::modeling::edge_instantiation(instance):
    assert isinstance(instance, features::modeling::Edge)

@given(instance=features::modeling::F_strategy)
@settings(max_examples=50)
def test_features::modeling::f_instantiation(instance):
    assert isinstance(instance, features::modeling::F)

@given(instance=features::modeling::Feature_strategy)
@settings(max_examples=50)
def test_features::modeling::feature_instantiation(instance):
    assert isinstance(instance, features::modeling::Feature)

@given(instance=features::modeling::Feature_strategy)
def test_features::modeling::feature_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=features::modeling::Feature_strategy)
def test_features::modeling::feature_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=features::modeling::R_strategy)
@settings(max_examples=50)
def test_features::modeling::r_instantiation(instance):
    assert isinstance(instance, features::modeling::R)

@given(instance=features::modeling::G_strategy)
@settings(max_examples=50)
def test_features::modeling::g_instantiation(instance):
    assert isinstance(instance, features::modeling::G)
