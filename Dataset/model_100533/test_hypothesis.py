import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UseCaseDSL::UseCasesModel,
    UseCaseDSL::StepAlternative,
    UseCaseDSL::PackageDeclaration,
    UseCaseDSL::UseCase,
    UseCaseDSL::Step,
    Step,
    UseCaseDSL::ParallelStep,
    UseCaseDSL::NormalStep,
    UseCaseDSL::Actor,
    UseCaseDSL::Flow,
    Flow,
    UseCaseDSL::BasicFlow,
    UseCaseDSL::NamedFlow,
    StepAlternative,
    UseCaseDSL::Condition,
    UseCaseDSL::LocalAlternative,
    UseCaseDSL::AlternativeFlowAlternative,
    NamedFlow,
    UseCaseDSL::ParallelFlow,
    UseCaseDSL::ExceptionFlow,
    UseCaseDSL::AlternativeFlow,
    ActorType,
    CustomStepType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecasedsl::usecasesmodel_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::UseCasesModel)


def test_usecasedsl::usecasesmodel_constructor_exists():
    assert callable(UseCaseDSL::UseCasesModel.__init__)


def test_usecasedsl::usecasesmodel_constructor_args():
    sig = inspect.signature(UseCaseDSL::UseCasesModel.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::stepalternative_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::StepAlternative)


def test_usecasedsl::stepalternative_constructor_exists():
    assert callable(UseCaseDSL::StepAlternative.__init__)


def test_usecasedsl::stepalternative_constructor_args():
    sig = inspect.signature(UseCaseDSL::StepAlternative.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_usecasedsl::stepalternative_has_condition():
    assert hasattr(UseCaseDSL::StepAlternative, "condition")
    descriptor = None
    for klass in UseCaseDSL::StepAlternative.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::PackageDeclaration)


def test_usecasedsl::packagedeclaration_constructor_exists():
    assert callable(UseCaseDSL::PackageDeclaration.__init__)


def test_usecasedsl::packagedeclaration_constructor_args():
    sig = inspect.signature(UseCaseDSL::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_usecasedsl::packagedeclaration_has_name():
    assert hasattr(UseCaseDSL::PackageDeclaration, "name")
    descriptor = None
    for klass in UseCaseDSL::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::packagedeclaration_has_description():
    assert hasattr(UseCaseDSL::PackageDeclaration, "description")
    descriptor = None
    for klass in UseCaseDSL::PackageDeclaration.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::usecase_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::UseCase)


def test_usecasedsl::usecase_constructor_exists():
    assert callable(UseCaseDSL::UseCase.__init__)


def test_usecasedsl::usecase_constructor_args():
    sig = inspect.signature(UseCaseDSL::UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "preConditions" in params, "Missing parameter 'preConditions'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_usecasedsl::usecase_has_preConditions():
    assert hasattr(UseCaseDSL::UseCase, "preConditions")
    descriptor = None
    for klass in UseCaseDSL::UseCase.__mro__:
        if "preConditions" in klass.__dict__:
            descriptor = klass.__dict__["preConditions"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::usecase_has_postcondition():
    assert hasattr(UseCaseDSL::UseCase, "postcondition")
    descriptor = None
    for klass in UseCaseDSL::UseCase.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::usecase_has_name():
    assert hasattr(UseCaseDSL::UseCase, "name")
    descriptor = None
    for klass in UseCaseDSL::UseCase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::usecase_has_description():
    assert hasattr(UseCaseDSL::UseCase, "description")
    descriptor = None
    for klass in UseCaseDSL::UseCase.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::step_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::Step)


def test_usecasedsl::step_constructor_exists():
    assert callable(UseCaseDSL::Step.__init__)


def test_usecasedsl::step_constructor_args():
    sig = inspect.signature(UseCaseDSL::Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_usecasedsl::step_has_name():
    assert hasattr(UseCaseDSL::Step, "name")
    descriptor = None
    for klass in UseCaseDSL::Step.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::step_has_label():
    assert hasattr(UseCaseDSL::Step, "label")
    descriptor = None
    for klass in UseCaseDSL::Step.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::parallelstep_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::ParallelStep)


def test_usecasedsl::parallelstep_constructor_exists():
    assert callable(UseCaseDSL::ParallelStep.__init__)


def test_usecasedsl::parallelstep_constructor_args():
    sig = inspect.signature(UseCaseDSL::ParallelStep.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::normalstep_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::NormalStep)


def test_usecasedsl::normalstep_constructor_exists():
    assert callable(UseCaseDSL::NormalStep.__init__)


def test_usecasedsl::normalstep_constructor_args():
    sig = inspect.signature(UseCaseDSL::NormalStep.__init__)
    params = list(sig.parameters.keys())
    assert "customStepType" in params, "Missing parameter 'customStepType'"

def test_usecasedsl::normalstep_has_customStepType():
    assert hasattr(UseCaseDSL::NormalStep, "customStepType")
    descriptor = None
    for klass in UseCaseDSL::NormalStep.__mro__:
        if "customStepType" in klass.__dict__:
            descriptor = klass.__dict__["customStepType"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::actor_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::Actor)


def test_usecasedsl::actor_constructor_exists():
    assert callable(UseCaseDSL::Actor.__init__)


def test_usecasedsl::actor_constructor_args():
    sig = inspect.signature(UseCaseDSL::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"

def test_usecasedsl::actor_has_name():
    assert hasattr(UseCaseDSL::Actor, "name")
    descriptor = None
    for klass in UseCaseDSL::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::actor_has_description():
    assert hasattr(UseCaseDSL::Actor, "description")
    descriptor = None
    for klass in UseCaseDSL::Actor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_usecasedsl::actor_has_type():
    assert hasattr(UseCaseDSL::Actor, "type")
    descriptor = None
    for klass in UseCaseDSL::Actor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::flow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::Flow)


def test_usecasedsl::flow_constructor_exists():
    assert callable(UseCaseDSL::Flow.__init__)


def test_usecasedsl::flow_constructor_args():
    sig = inspect.signature(UseCaseDSL::Flow.__init__)
    params = list(sig.parameters.keys())
    assert "finalState" in params, "Missing parameter 'finalState'"

def test_usecasedsl::flow_has_finalState():
    assert hasattr(UseCaseDSL::Flow, "finalState")
    descriptor = None
    for klass in UseCaseDSL::Flow.__mro__:
        if "finalState" in klass.__dict__:
            descriptor = klass.__dict__["finalState"]
            break
    assert isinstance(descriptor, property)



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::basicflow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::BasicFlow)


def test_usecasedsl::basicflow_constructor_exists():
    assert callable(UseCaseDSL::BasicFlow.__init__)


def test_usecasedsl::basicflow_constructor_args():
    sig = inspect.signature(UseCaseDSL::BasicFlow.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::namedflow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::NamedFlow)


def test_usecasedsl::namedflow_constructor_exists():
    assert callable(UseCaseDSL::NamedFlow.__init__)


def test_usecasedsl::namedflow_constructor_args():
    sig = inspect.signature(UseCaseDSL::NamedFlow.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecasedsl::namedflow_has_name():
    assert hasattr(UseCaseDSL::NamedFlow, "name")
    descriptor = None
    for klass in UseCaseDSL::NamedFlow.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stepalternative_is_not_abstract():
    assert not inspect.isabstract(StepAlternative)


def test_stepalternative_constructor_exists():
    assert callable(StepAlternative.__init__)


def test_stepalternative_constructor_args():
    sig = inspect.signature(StepAlternative.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::condition_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::Condition)


def test_usecasedsl::condition_constructor_exists():
    assert callable(UseCaseDSL::Condition.__init__)


def test_usecasedsl::condition_constructor_args():
    sig = inspect.signature(UseCaseDSL::Condition.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::localalternative_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::LocalAlternative)


def test_usecasedsl::localalternative_constructor_exists():
    assert callable(UseCaseDSL::LocalAlternative.__init__)


def test_usecasedsl::localalternative_constructor_args():
    sig = inspect.signature(UseCaseDSL::LocalAlternative.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_usecasedsl::localalternative_has_description():
    assert hasattr(UseCaseDSL::LocalAlternative, "description")
    descriptor = None
    for klass in UseCaseDSL::LocalAlternative.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::alternativeflowalternative_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::AlternativeFlowAlternative)


def test_usecasedsl::alternativeflowalternative_constructor_exists():
    assert callable(UseCaseDSL::AlternativeFlowAlternative.__init__)


def test_usecasedsl::alternativeflowalternative_constructor_args():
    sig = inspect.signature(UseCaseDSL::AlternativeFlowAlternative.__init__)
    params = list(sig.parameters.keys())



def test_namedflow_is_not_abstract():
    assert not inspect.isabstract(NamedFlow)


def test_namedflow_constructor_exists():
    assert callable(NamedFlow.__init__)


def test_namedflow_constructor_args():
    sig = inspect.signature(NamedFlow.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::parallelflow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::ParallelFlow)


def test_usecasedsl::parallelflow_constructor_exists():
    assert callable(UseCaseDSL::ParallelFlow.__init__)


def test_usecasedsl::parallelflow_constructor_args():
    sig = inspect.signature(UseCaseDSL::ParallelFlow.__init__)
    params = list(sig.parameters.keys())



def test_usecasedsl::exceptionflow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::ExceptionFlow)


def test_usecasedsl::exceptionflow_constructor_exists():
    assert callable(UseCaseDSL::ExceptionFlow.__init__)


def test_usecasedsl::exceptionflow_constructor_args():
    sig = inspect.signature(UseCaseDSL::ExceptionFlow.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_usecasedsl::exceptionflow_has_condition():
    assert hasattr(UseCaseDSL::ExceptionFlow, "condition")
    descriptor = None
    for klass in UseCaseDSL::ExceptionFlow.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_usecasedsl::alternativeflow_is_not_abstract():
    assert not inspect.isabstract(UseCaseDSL::AlternativeFlow)


def test_usecasedsl::alternativeflow_constructor_exists():
    assert callable(UseCaseDSL::AlternativeFlow.__init__)


def test_usecasedsl::alternativeflow_constructor_args():
    sig = inspect.signature(UseCaseDSL::AlternativeFlow.__init__)
    params = list(sig.parameters.keys())

def test_actortype_exists():
    # Check that the Enumeration exists
    assert ActorType is not None

def test_actortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActorType]
    expected_literals = [
        "ORGANIZATION",
        "PERSON",
        "SYSTEM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActorType"

def test_customsteptype_exists():
    # Check that the Enumeration exists
    assert CustomStepType is not None

def test_customsteptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomStepType]
    expected_literals = [
        "PROCESS",
        "MIX",
        "OUTPUT",
        "INPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomStepType"


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
UseCaseDSL::UseCasesModel_strategy = st.builds(
    UseCaseDSL::UseCasesModel,
)
UseCaseDSL::StepAlternative_strategy = st.builds(
    UseCaseDSL::StepAlternative,
    condition=
        safe_text
)
UseCaseDSL::PackageDeclaration_strategy = st.builds(
    UseCaseDSL::PackageDeclaration,
    name=
        safe_text,
    description=
        safe_text
)
UseCaseDSL::UseCase_strategy = st.builds(
    UseCaseDSL::UseCase,
    preConditions=
        safe_text,
    postcondition=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
UseCaseDSL::Step_strategy = st.builds(
    UseCaseDSL::Step,
    name=
        safe_text,
    label=
        safe_text
)
Step_strategy = st.builds(
    Step,
)
UseCaseDSL::ParallelStep_strategy = st.builds(
    UseCaseDSL::ParallelStep,
)
UseCaseDSL::NormalStep_strategy = st.builds(
    UseCaseDSL::NormalStep,
    customStepType=
        safe_text
)
UseCaseDSL::Actor_strategy = st.builds(
    UseCaseDSL::Actor,
    name=
        safe_text,
    description=
        safe_text,
    type=
        safe_text
)
UseCaseDSL::Flow_strategy = st.builds(
    UseCaseDSL::Flow,
    finalState=
        safe_text
)
Flow_strategy = st.builds(
    Flow,
)
UseCaseDSL::BasicFlow_strategy = st.builds(
    UseCaseDSL::BasicFlow,
)
UseCaseDSL::NamedFlow_strategy = st.builds(
    UseCaseDSL::NamedFlow,
    name=
        safe_text
)
StepAlternative_strategy = st.builds(
    StepAlternative,
)
UseCaseDSL::Condition_strategy = st.builds(
    UseCaseDSL::Condition,
)
UseCaseDSL::LocalAlternative_strategy = st.builds(
    UseCaseDSL::LocalAlternative,
    description=
        safe_text
)
UseCaseDSL::AlternativeFlowAlternative_strategy = st.builds(
    UseCaseDSL::AlternativeFlowAlternative,
)
NamedFlow_strategy = st.builds(
    NamedFlow,
)
UseCaseDSL::ParallelFlow_strategy = st.builds(
    UseCaseDSL::ParallelFlow,
)
UseCaseDSL::ExceptionFlow_strategy = st.builds(
    UseCaseDSL::ExceptionFlow,
    condition=
        safe_text
)
UseCaseDSL::AlternativeFlow_strategy = st.builds(
    UseCaseDSL::AlternativeFlow,
)

@given(instance=UseCaseDSL::UseCasesModel_strategy)
@settings(max_examples=50)
def test_usecasedsl::usecasesmodel_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::UseCasesModel)

@given(instance=UseCaseDSL::StepAlternative_strategy)
@settings(max_examples=50)
def test_usecasedsl::stepalternative_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::StepAlternative)

@given(instance=UseCaseDSL::StepAlternative_strategy)
def test_usecasedsl::stepalternative_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=UseCaseDSL::StepAlternative_strategy)
def test_usecasedsl::stepalternative_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=UseCaseDSL::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_usecasedsl::packagedeclaration_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::PackageDeclaration)

@given(instance=UseCaseDSL::PackageDeclaration_strategy)
def test_usecasedsl::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCaseDSL::PackageDeclaration_strategy)
def test_usecasedsl::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCaseDSL::PackageDeclaration_strategy)
def test_usecasedsl::packagedeclaration_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=UseCaseDSL::PackageDeclaration_strategy)
def test_usecasedsl::packagedeclaration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=UseCaseDSL::UseCase_strategy)
@settings(max_examples=50)
def test_usecasedsl::usecase_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::UseCase)

@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_preConditions_type(instance):
    assert isinstance(instance.preConditions, str)


@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_preConditions_setter(instance):
    original = instance.preConditions
    instance.preConditions = original
    assert instance.preConditions == original

@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=UseCaseDSL::UseCase_strategy)
def test_usecasedsl::usecase_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=UseCaseDSL::Step_strategy)
@settings(max_examples=50)
def test_usecasedsl::step_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::Step)

@given(instance=UseCaseDSL::Step_strategy)
def test_usecasedsl::step_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCaseDSL::Step_strategy)
def test_usecasedsl::step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCaseDSL::Step_strategy)
def test_usecasedsl::step_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=UseCaseDSL::Step_strategy)
def test_usecasedsl::step_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=UseCaseDSL::ParallelStep_strategy)
@settings(max_examples=50)
def test_usecasedsl::parallelstep_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::ParallelStep)

@given(instance=UseCaseDSL::NormalStep_strategy)
@settings(max_examples=50)
def test_usecasedsl::normalstep_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::NormalStep)

@given(instance=UseCaseDSL::NormalStep_strategy)
def test_usecasedsl::normalstep_customStepType_type(instance):
    assert isinstance(instance.customStepType, str)


@given(instance=UseCaseDSL::NormalStep_strategy)
def test_usecasedsl::normalstep_customStepType_setter(instance):
    original = instance.customStepType
    instance.customStepType = original
    assert instance.customStepType == original

@given(instance=UseCaseDSL::Actor_strategy)
@settings(max_examples=50)
def test_usecasedsl::actor_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::Actor)

@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=UseCaseDSL::Actor_strategy)
def test_usecasedsl::actor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UseCaseDSL::Flow_strategy)
@settings(max_examples=50)
def test_usecasedsl::flow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::Flow)

@given(instance=UseCaseDSL::Flow_strategy)
def test_usecasedsl::flow_finalState_type(instance):
    assert isinstance(instance.finalState, str)


@given(instance=UseCaseDSL::Flow_strategy)
def test_usecasedsl::flow_finalState_setter(instance):
    original = instance.finalState
    instance.finalState = original
    assert instance.finalState == original

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=UseCaseDSL::BasicFlow_strategy)
@settings(max_examples=50)
def test_usecasedsl::basicflow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::BasicFlow)

@given(instance=UseCaseDSL::NamedFlow_strategy)
@settings(max_examples=50)
def test_usecasedsl::namedflow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::NamedFlow)

@given(instance=UseCaseDSL::NamedFlow_strategy)
def test_usecasedsl::namedflow_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCaseDSL::NamedFlow_strategy)
def test_usecasedsl::namedflow_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StepAlternative_strategy)
@settings(max_examples=50)
def test_stepalternative_instantiation(instance):
    assert isinstance(instance, StepAlternative)

@given(instance=UseCaseDSL::Condition_strategy)
@settings(max_examples=50)
def test_usecasedsl::condition_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::Condition)

@given(instance=UseCaseDSL::LocalAlternative_strategy)
@settings(max_examples=50)
def test_usecasedsl::localalternative_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::LocalAlternative)

@given(instance=UseCaseDSL::LocalAlternative_strategy)
def test_usecasedsl::localalternative_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=UseCaseDSL::LocalAlternative_strategy)
def test_usecasedsl::localalternative_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=UseCaseDSL::AlternativeFlowAlternative_strategy)
@settings(max_examples=50)
def test_usecasedsl::alternativeflowalternative_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::AlternativeFlowAlternative)

@given(instance=NamedFlow_strategy)
@settings(max_examples=50)
def test_namedflow_instantiation(instance):
    assert isinstance(instance, NamedFlow)

@given(instance=UseCaseDSL::ParallelFlow_strategy)
@settings(max_examples=50)
def test_usecasedsl::parallelflow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::ParallelFlow)

@given(instance=UseCaseDSL::ExceptionFlow_strategy)
@settings(max_examples=50)
def test_usecasedsl::exceptionflow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::ExceptionFlow)

@given(instance=UseCaseDSL::ExceptionFlow_strategy)
def test_usecasedsl::exceptionflow_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=UseCaseDSL::ExceptionFlow_strategy)
def test_usecasedsl::exceptionflow_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=UseCaseDSL::AlternativeFlow_strategy)
@settings(max_examples=50)
def test_usecasedsl::alternativeflow_instantiation(instance):
    assert isinstance(instance, UseCaseDSL::AlternativeFlow)
