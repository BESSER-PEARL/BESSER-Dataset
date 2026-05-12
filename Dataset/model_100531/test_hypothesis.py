import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    USECASEUML::Condition,
    USECASEUML::ScenarioDescription,
    USECASEUML::Resource,
    Resource,
    USECASEUML::Role,
    NonFunctionnelRequirement,
    FunctionnelRequirement,
    Role,
    USECASEUML::HumanRole,
    USECASEUML::EventRole,
    USECASEUML::SystemRole,
    Condition,
    USECASEUML::Pre,
    USECASEUML::Post,
    ScenarioDescription,
    USECASEUML::UseCase,
    USECASEUML::Goal,
    Goal,
    USECASEUML::Requirement,
    UseCase,
    USECASEUML::Manage,
    Requirement,
    USECASEUML::FunctionnelRequirement,
    USECASEUML::NonFunctionnelRequirement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecaseuml::condition_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Condition)


def test_usecaseuml::condition_constructor_exists():
    assert callable(USECASEUML::Condition.__init__)


def test_usecaseuml::condition_constructor_args():
    sig = inspect.signature(USECASEUML::Condition.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::scenariodescription_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::ScenarioDescription)


def test_usecaseuml::scenariodescription_constructor_exists():
    assert callable(USECASEUML::ScenarioDescription.__init__)


def test_usecaseuml::scenariodescription_constructor_args():
    sig = inspect.signature(USECASEUML::ScenarioDescription.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::resource_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Resource)


def test_usecaseuml::resource_constructor_exists():
    assert callable(USECASEUML::Resource.__init__)


def test_usecaseuml::resource_constructor_args():
    sig = inspect.signature(USECASEUML::Resource.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::role_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Role)


def test_usecaseuml::role_constructor_exists():
    assert callable(USECASEUML::Role.__init__)


def test_usecaseuml::role_constructor_args():
    sig = inspect.signature(USECASEUML::Role.__init__)
    params = list(sig.parameters.keys())



def test_nonfunctionnelrequirement_is_not_abstract():
    assert not inspect.isabstract(NonFunctionnelRequirement)


def test_nonfunctionnelrequirement_constructor_exists():
    assert callable(NonFunctionnelRequirement.__init__)


def test_nonfunctionnelrequirement_constructor_args():
    sig = inspect.signature(NonFunctionnelRequirement.__init__)
    params = list(sig.parameters.keys())



def test_functionnelrequirement_is_not_abstract():
    assert not inspect.isabstract(FunctionnelRequirement)


def test_functionnelrequirement_constructor_exists():
    assert callable(FunctionnelRequirement.__init__)


def test_functionnelrequirement_constructor_args():
    sig = inspect.signature(FunctionnelRequirement.__init__)
    params = list(sig.parameters.keys())



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::humanrole_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::HumanRole)


def test_usecaseuml::humanrole_constructor_exists():
    assert callable(USECASEUML::HumanRole.__init__)


def test_usecaseuml::humanrole_constructor_args():
    sig = inspect.signature(USECASEUML::HumanRole.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::eventrole_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::EventRole)


def test_usecaseuml::eventrole_constructor_exists():
    assert callable(USECASEUML::EventRole.__init__)


def test_usecaseuml::eventrole_constructor_args():
    sig = inspect.signature(USECASEUML::EventRole.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::systemrole_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::SystemRole)


def test_usecaseuml::systemrole_constructor_exists():
    assert callable(USECASEUML::SystemRole.__init__)


def test_usecaseuml::systemrole_constructor_args():
    sig = inspect.signature(USECASEUML::SystemRole.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::pre_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Pre)


def test_usecaseuml::pre_constructor_exists():
    assert callable(USECASEUML::Pre.__init__)


def test_usecaseuml::pre_constructor_args():
    sig = inspect.signature(USECASEUML::Pre.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::post_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Post)


def test_usecaseuml::post_constructor_exists():
    assert callable(USECASEUML::Post.__init__)


def test_usecaseuml::post_constructor_args():
    sig = inspect.signature(USECASEUML::Post.__init__)
    params = list(sig.parameters.keys())



def test_scenariodescription_is_not_abstract():
    assert not inspect.isabstract(ScenarioDescription)


def test_scenariodescription_constructor_exists():
    assert callable(ScenarioDescription.__init__)


def test_scenariodescription_constructor_args():
    sig = inspect.signature(ScenarioDescription.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::usecase_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::UseCase)


def test_usecaseuml::usecase_constructor_exists():
    assert callable(USECASEUML::UseCase.__init__)


def test_usecaseuml::usecase_constructor_args():
    sig = inspect.signature(USECASEUML::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::goal_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Goal)


def test_usecaseuml::goal_constructor_exists():
    assert callable(USECASEUML::Goal.__init__)


def test_usecaseuml::goal_constructor_args():
    sig = inspect.signature(USECASEUML::Goal.__init__)
    params = list(sig.parameters.keys())



def test_goal_is_not_abstract():
    assert not inspect.isabstract(Goal)


def test_goal_constructor_exists():
    assert callable(Goal.__init__)


def test_goal_constructor_args():
    sig = inspect.signature(Goal.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::requirement_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Requirement)


def test_usecaseuml::requirement_constructor_exists():
    assert callable(USECASEUML::Requirement.__init__)


def test_usecaseuml::requirement_constructor_args():
    sig = inspect.signature(USECASEUML::Requirement.__init__)
    params = list(sig.parameters.keys())



def test_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase)


def test_usecase_constructor_exists():
    assert callable(UseCase.__init__)


def test_usecase_constructor_args():
    sig = inspect.signature(UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::manage_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::Manage)


def test_usecaseuml::manage_constructor_exists():
    assert callable(USECASEUML::Manage.__init__)


def test_usecaseuml::manage_constructor_args():
    sig = inspect.signature(USECASEUML::Manage.__init__)
    params = list(sig.parameters.keys())



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::functionnelrequirement_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::FunctionnelRequirement)


def test_usecaseuml::functionnelrequirement_constructor_exists():
    assert callable(USECASEUML::FunctionnelRequirement.__init__)


def test_usecaseuml::functionnelrequirement_constructor_args():
    sig = inspect.signature(USECASEUML::FunctionnelRequirement.__init__)
    params = list(sig.parameters.keys())



def test_usecaseuml::nonfunctionnelrequirement_is_not_abstract():
    assert not inspect.isabstract(USECASEUML::NonFunctionnelRequirement)


def test_usecaseuml::nonfunctionnelrequirement_constructor_exists():
    assert callable(USECASEUML::NonFunctionnelRequirement.__init__)


def test_usecaseuml::nonfunctionnelrequirement_constructor_args():
    sig = inspect.signature(USECASEUML::NonFunctionnelRequirement.__init__)
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
USECASEUML::Condition_strategy = st.builds(
    USECASEUML::Condition,
)
USECASEUML::ScenarioDescription_strategy = st.builds(
    USECASEUML::ScenarioDescription,
)
USECASEUML::Resource_strategy = st.builds(
    USECASEUML::Resource,
)
Resource_strategy = st.builds(
    Resource,
)
USECASEUML::Role_strategy = st.builds(
    USECASEUML::Role,
)
NonFunctionnelRequirement_strategy = st.builds(
    NonFunctionnelRequirement,
)
FunctionnelRequirement_strategy = st.builds(
    FunctionnelRequirement,
)
Role_strategy = st.builds(
    Role,
)
USECASEUML::HumanRole_strategy = st.builds(
    USECASEUML::HumanRole,
)
USECASEUML::EventRole_strategy = st.builds(
    USECASEUML::EventRole,
)
USECASEUML::SystemRole_strategy = st.builds(
    USECASEUML::SystemRole,
)
Condition_strategy = st.builds(
    Condition,
)
USECASEUML::Pre_strategy = st.builds(
    USECASEUML::Pre,
)
USECASEUML::Post_strategy = st.builds(
    USECASEUML::Post,
)
ScenarioDescription_strategy = st.builds(
    ScenarioDescription,
)
USECASEUML::UseCase_strategy = st.builds(
    USECASEUML::UseCase,
)
USECASEUML::Goal_strategy = st.builds(
    USECASEUML::Goal,
)
Goal_strategy = st.builds(
    Goal,
)
USECASEUML::Requirement_strategy = st.builds(
    USECASEUML::Requirement,
)
UseCase_strategy = st.builds(
    UseCase,
)
USECASEUML::Manage_strategy = st.builds(
    USECASEUML::Manage,
)
Requirement_strategy = st.builds(
    Requirement,
)
USECASEUML::FunctionnelRequirement_strategy = st.builds(
    USECASEUML::FunctionnelRequirement,
)
USECASEUML::NonFunctionnelRequirement_strategy = st.builds(
    USECASEUML::NonFunctionnelRequirement,
)

@given(instance=USECASEUML::Condition_strategy)
@settings(max_examples=50)
def test_usecaseuml::condition_instantiation(instance):
    assert isinstance(instance, USECASEUML::Condition)

@given(instance=USECASEUML::ScenarioDescription_strategy)
@settings(max_examples=50)
def test_usecaseuml::scenariodescription_instantiation(instance):
    assert isinstance(instance, USECASEUML::ScenarioDescription)

@given(instance=USECASEUML::Resource_strategy)
@settings(max_examples=50)
def test_usecaseuml::resource_instantiation(instance):
    assert isinstance(instance, USECASEUML::Resource)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=USECASEUML::Role_strategy)
@settings(max_examples=50)
def test_usecaseuml::role_instantiation(instance):
    assert isinstance(instance, USECASEUML::Role)

@given(instance=NonFunctionnelRequirement_strategy)
@settings(max_examples=50)
def test_nonfunctionnelrequirement_instantiation(instance):
    assert isinstance(instance, NonFunctionnelRequirement)

@given(instance=FunctionnelRequirement_strategy)
@settings(max_examples=50)
def test_functionnelrequirement_instantiation(instance):
    assert isinstance(instance, FunctionnelRequirement)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=USECASEUML::HumanRole_strategy)
@settings(max_examples=50)
def test_usecaseuml::humanrole_instantiation(instance):
    assert isinstance(instance, USECASEUML::HumanRole)

@given(instance=USECASEUML::EventRole_strategy)
@settings(max_examples=50)
def test_usecaseuml::eventrole_instantiation(instance):
    assert isinstance(instance, USECASEUML::EventRole)

@given(instance=USECASEUML::SystemRole_strategy)
@settings(max_examples=50)
def test_usecaseuml::systemrole_instantiation(instance):
    assert isinstance(instance, USECASEUML::SystemRole)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=USECASEUML::Pre_strategy)
@settings(max_examples=50)
def test_usecaseuml::pre_instantiation(instance):
    assert isinstance(instance, USECASEUML::Pre)

@given(instance=USECASEUML::Post_strategy)
@settings(max_examples=50)
def test_usecaseuml::post_instantiation(instance):
    assert isinstance(instance, USECASEUML::Post)

@given(instance=ScenarioDescription_strategy)
@settings(max_examples=50)
def test_scenariodescription_instantiation(instance):
    assert isinstance(instance, ScenarioDescription)

@given(instance=USECASEUML::UseCase_strategy)
@settings(max_examples=50)
def test_usecaseuml::usecase_instantiation(instance):
    assert isinstance(instance, USECASEUML::UseCase)

@given(instance=USECASEUML::Goal_strategy)
@settings(max_examples=50)
def test_usecaseuml::goal_instantiation(instance):
    assert isinstance(instance, USECASEUML::Goal)

@given(instance=Goal_strategy)
@settings(max_examples=50)
def test_goal_instantiation(instance):
    assert isinstance(instance, Goal)

@given(instance=USECASEUML::Requirement_strategy)
@settings(max_examples=50)
def test_usecaseuml::requirement_instantiation(instance):
    assert isinstance(instance, USECASEUML::Requirement)

@given(instance=UseCase_strategy)
@settings(max_examples=50)
def test_usecase_instantiation(instance):
    assert isinstance(instance, UseCase)

@given(instance=USECASEUML::Manage_strategy)
@settings(max_examples=50)
def test_usecaseuml::manage_instantiation(instance):
    assert isinstance(instance, USECASEUML::Manage)

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)

@given(instance=USECASEUML::FunctionnelRequirement_strategy)
@settings(max_examples=50)
def test_usecaseuml::functionnelrequirement_instantiation(instance):
    assert isinstance(instance, USECASEUML::FunctionnelRequirement)

@given(instance=USECASEUML::NonFunctionnelRequirement_strategy)
@settings(max_examples=50)
def test_usecaseuml::nonfunctionnelrequirement_instantiation(instance):
    assert isinstance(instance, USECASEUML::NonFunctionnelRequirement)
