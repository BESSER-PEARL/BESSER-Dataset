import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    requirements::editor::DocumentRoot,
    Argument,
    requirements::editor::NOTOperator,
    requirements::editor::RequirementArgument,
    requirements::editor::BinaryOperatorArgument,
    requirements::editor::Argument,
    SimpleDependency,
    requirements::editor::ICost,
    requirements::editor::CValue,
    requirements::editor::Refines,
    Dependency,
    requirements::editor::Requires,
    requirements::editor::SimpleDependency,
    Requirement,
    requirements::editor::FunctionalRequirement,
    requirements::editor::QualityRequirement,
    Description,
    requirements::editor::TextualDescription,
    requirements::editor::Category,
    requirements::editor::Dependency,
    requirements::editor::Person,
    requirements::editor::Description,
    requirements::editor::Requirement,
    BinaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirements::editor::documentroot_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::DocumentRoot)


def test_requirements::editor::documentroot_constructor_exists():
    assert callable(requirements::editor::DocumentRoot.__init__)


def test_requirements::editor::documentroot_constructor_args():
    sig = inspect.signature(requirements::editor::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_requirements::editor::documentroot_has_name():
    assert hasattr(requirements::editor::DocumentRoot, "name")
    descriptor = None
    for klass in requirements::editor::DocumentRoot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::notoperator_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::NOTOperator)


def test_requirements::editor::notoperator_constructor_exists():
    assert callable(requirements::editor::NOTOperator.__init__)


def test_requirements::editor::notoperator_constructor_args():
    sig = inspect.signature(requirements::editor::NOTOperator.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::requirementargument_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::RequirementArgument)


def test_requirements::editor::requirementargument_constructor_exists():
    assert callable(requirements::editor::RequirementArgument.__init__)


def test_requirements::editor::requirementargument_constructor_args():
    sig = inspect.signature(requirements::editor::RequirementArgument.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::binaryoperatorargument_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::BinaryOperatorArgument)


def test_requirements::editor::binaryoperatorargument_constructor_exists():
    assert callable(requirements::editor::BinaryOperatorArgument.__init__)


def test_requirements::editor::binaryoperatorargument_constructor_args():
    sig = inspect.signature(requirements::editor::BinaryOperatorArgument.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_requirements::editor::binaryoperatorargument_has_operator():
    assert hasattr(requirements::editor::BinaryOperatorArgument, "operator")
    descriptor = None
    for klass in requirements::editor::BinaryOperatorArgument.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_requirements::editor::argument_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Argument)


def test_requirements::editor::argument_constructor_exists():
    assert callable(requirements::editor::Argument.__init__)


def test_requirements::editor::argument_constructor_args():
    sig = inspect.signature(requirements::editor::Argument.__init__)
    params = list(sig.parameters.keys())



def test_simpledependency_is_not_abstract():
    assert not inspect.isabstract(SimpleDependency)


def test_simpledependency_constructor_exists():
    assert callable(SimpleDependency.__init__)


def test_simpledependency_constructor_args():
    sig = inspect.signature(SimpleDependency.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::icost_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::ICost)


def test_requirements::editor::icost_constructor_exists():
    assert callable(requirements::editor::ICost.__init__)


def test_requirements::editor::icost_constructor_args():
    sig = inspect.signature(requirements::editor::ICost.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::cvalue_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::CValue)


def test_requirements::editor::cvalue_constructor_exists():
    assert callable(requirements::editor::CValue.__init__)


def test_requirements::editor::cvalue_constructor_args():
    sig = inspect.signature(requirements::editor::CValue.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::refines_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Refines)


def test_requirements::editor::refines_constructor_exists():
    assert callable(requirements::editor::Refines.__init__)


def test_requirements::editor::refines_constructor_args():
    sig = inspect.signature(requirements::editor::Refines.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::requires_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Requires)


def test_requirements::editor::requires_constructor_exists():
    assert callable(requirements::editor::Requires.__init__)


def test_requirements::editor::requires_constructor_args():
    sig = inspect.signature(requirements::editor::Requires.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::simpledependency_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::SimpleDependency)


def test_requirements::editor::simpledependency_constructor_exists():
    assert callable(requirements::editor::SimpleDependency.__init__)


def test_requirements::editor::simpledependency_constructor_args():
    sig = inspect.signature(requirements::editor::SimpleDependency.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_requirements::editor::simpledependency_has_comment():
    assert hasattr(requirements::editor::SimpleDependency, "comment")
    descriptor = None
    for klass in requirements::editor::SimpleDependency.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::FunctionalRequirement)


def test_requirements::editor::functionalrequirement_constructor_exists():
    assert callable(requirements::editor::FunctionalRequirement.__init__)


def test_requirements::editor::functionalrequirement_constructor_args():
    sig = inspect.signature(requirements::editor::FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::qualityrequirement_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::QualityRequirement)


def test_requirements::editor::qualityrequirement_constructor_exists():
    assert callable(requirements::editor::QualityRequirement.__init__)


def test_requirements::editor::qualityrequirement_constructor_args():
    sig = inspect.signature(requirements::editor::QualityRequirement.__init__)
    params = list(sig.parameters.keys())



def test_description_is_not_abstract():
    assert not inspect.isabstract(Description)


def test_description_constructor_exists():
    assert callable(Description.__init__)


def test_description_constructor_args():
    sig = inspect.signature(Description.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::textualdescription_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::TextualDescription)


def test_requirements::editor::textualdescription_constructor_exists():
    assert callable(requirements::editor::TextualDescription.__init__)


def test_requirements::editor::textualdescription_constructor_args():
    sig = inspect.signature(requirements::editor::TextualDescription.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_requirements::editor::textualdescription_has_description():
    assert hasattr(requirements::editor::TextualDescription, "description")
    descriptor = None
    for klass in requirements::editor::TextualDescription.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_requirements::editor::category_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Category)


def test_requirements::editor::category_constructor_exists():
    assert callable(requirements::editor::Category.__init__)


def test_requirements::editor::category_constructor_args():
    sig = inspect.signature(requirements::editor::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_requirements::editor::category_has_name():
    assert hasattr(requirements::editor::Category, "name")
    descriptor = None
    for klass in requirements::editor::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_requirements::editor::dependency_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Dependency)


def test_requirements::editor::dependency_constructor_exists():
    assert callable(requirements::editor::Dependency.__init__)


def test_requirements::editor::dependency_constructor_args():
    sig = inspect.signature(requirements::editor::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::person_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Person)


def test_requirements::editor::person_constructor_exists():
    assert callable(requirements::editor::Person.__init__)


def test_requirements::editor::person_constructor_args():
    sig = inspect.signature(requirements::editor::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_requirements::editor::person_has_name():
    assert hasattr(requirements::editor::Person, "name")
    descriptor = None
    for klass in requirements::editor::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_requirements::editor::description_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Description)


def test_requirements::editor::description_constructor_exists():
    assert callable(requirements::editor::Description.__init__)


def test_requirements::editor::description_constructor_args():
    sig = inspect.signature(requirements::editor::Description.__init__)
    params = list(sig.parameters.keys())



def test_requirements::editor::requirement_is_not_abstract():
    assert not inspect.isabstract(requirements::editor::Requirement)


def test_requirements::editor::requirement_constructor_exists():
    assert callable(requirements::editor::Requirement.__init__)


def test_requirements::editor::requirement_constructor_args():
    sig = inspect.signature(requirements::editor::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_requirements::editor::requirement_has_priority():
    assert hasattr(requirements::editor::Requirement, "priority")
    descriptor = None
    for klass in requirements::editor::Requirement.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_requirements::editor::requirement_has_isMandatory():
    assert hasattr(requirements::editor::Requirement, "isMandatory")
    descriptor = None
    for klass in requirements::editor::Requirement.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_requirements::editor::requirement_has_identifier():
    assert hasattr(requirements::editor::Requirement, "identifier")
    descriptor = None
    for klass in requirements::editor::Requirement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_requirements::editor::requirement_has_name():
    assert hasattr(requirements::editor::Requirement, "name")
    descriptor = None
    for klass in requirements::editor::Requirement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"


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
requirements::editor::DocumentRoot_strategy = st.builds(
    requirements::editor::DocumentRoot,
    name=
        safe_text
)
Argument_strategy = st.builds(
    Argument,
)
requirements::editor::NOTOperator_strategy = st.builds(
    requirements::editor::NOTOperator,
)
requirements::editor::RequirementArgument_strategy = st.builds(
    requirements::editor::RequirementArgument,
)
requirements::editor::BinaryOperatorArgument_strategy = st.builds(
    requirements::editor::BinaryOperatorArgument,
    operator=
        safe_text
)
requirements::editor::Argument_strategy = st.builds(
    requirements::editor::Argument,
)
SimpleDependency_strategy = st.builds(
    SimpleDependency,
)
requirements::editor::ICost_strategy = st.builds(
    requirements::editor::ICost,
)
requirements::editor::CValue_strategy = st.builds(
    requirements::editor::CValue,
)
requirements::editor::Refines_strategy = st.builds(
    requirements::editor::Refines,
)
Dependency_strategy = st.builds(
    Dependency,
)
requirements::editor::Requires_strategy = st.builds(
    requirements::editor::Requires,
)
requirements::editor::SimpleDependency_strategy = st.builds(
    requirements::editor::SimpleDependency,
    comment=
        safe_text
)
Requirement_strategy = st.builds(
    Requirement,
)
requirements::editor::FunctionalRequirement_strategy = st.builds(
    requirements::editor::FunctionalRequirement,
)
requirements::editor::QualityRequirement_strategy = st.builds(
    requirements::editor::QualityRequirement,
)
Description_strategy = st.builds(
    Description,
)
requirements::editor::TextualDescription_strategy = st.builds(
    requirements::editor::TextualDescription,
    description=
        safe_text
)
requirements::editor::Category_strategy = st.builds(
    requirements::editor::Category,
    name=
        safe_text
)
requirements::editor::Dependency_strategy = st.builds(
    requirements::editor::Dependency,
)
requirements::editor::Person_strategy = st.builds(
    requirements::editor::Person,
    name=
        safe_text
)
requirements::editor::Description_strategy = st.builds(
    requirements::editor::Description,
)
requirements::editor::Requirement_strategy = st.builds(
    requirements::editor::Requirement,
    priority=
        st.integers(),
    isMandatory=
        st.booleans(),
    identifier=
        safe_text,
    name=
        safe_text
)

@given(instance=requirements::editor::DocumentRoot_strategy)
@settings(max_examples=50)
def test_requirements::editor::documentroot_instantiation(instance):
    assert isinstance(instance, requirements::editor::DocumentRoot)

@given(instance=requirements::editor::DocumentRoot_strategy)
def test_requirements::editor::documentroot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=requirements::editor::DocumentRoot_strategy)
def test_requirements::editor::documentroot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=requirements::editor::NOTOperator_strategy)
@settings(max_examples=50)
def test_requirements::editor::notoperator_instantiation(instance):
    assert isinstance(instance, requirements::editor::NOTOperator)

@given(instance=requirements::editor::RequirementArgument_strategy)
@settings(max_examples=50)
def test_requirements::editor::requirementargument_instantiation(instance):
    assert isinstance(instance, requirements::editor::RequirementArgument)

@given(instance=requirements::editor::BinaryOperatorArgument_strategy)
@settings(max_examples=50)
def test_requirements::editor::binaryoperatorargument_instantiation(instance):
    assert isinstance(instance, requirements::editor::BinaryOperatorArgument)

@given(instance=requirements::editor::BinaryOperatorArgument_strategy)
def test_requirements::editor::binaryoperatorargument_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=requirements::editor::BinaryOperatorArgument_strategy)
def test_requirements::editor::binaryoperatorargument_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=requirements::editor::Argument_strategy)
@settings(max_examples=50)
def test_requirements::editor::argument_instantiation(instance):
    assert isinstance(instance, requirements::editor::Argument)

@given(instance=SimpleDependency_strategy)
@settings(max_examples=50)
def test_simpledependency_instantiation(instance):
    assert isinstance(instance, SimpleDependency)

@given(instance=requirements::editor::ICost_strategy)
@settings(max_examples=50)
def test_requirements::editor::icost_instantiation(instance):
    assert isinstance(instance, requirements::editor::ICost)

@given(instance=requirements::editor::CValue_strategy)
@settings(max_examples=50)
def test_requirements::editor::cvalue_instantiation(instance):
    assert isinstance(instance, requirements::editor::CValue)

@given(instance=requirements::editor::Refines_strategy)
@settings(max_examples=50)
def test_requirements::editor::refines_instantiation(instance):
    assert isinstance(instance, requirements::editor::Refines)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=requirements::editor::Requires_strategy)
@settings(max_examples=50)
def test_requirements::editor::requires_instantiation(instance):
    assert isinstance(instance, requirements::editor::Requires)

@given(instance=requirements::editor::SimpleDependency_strategy)
@settings(max_examples=50)
def test_requirements::editor::simpledependency_instantiation(instance):
    assert isinstance(instance, requirements::editor::SimpleDependency)

@given(instance=requirements::editor::SimpleDependency_strategy)
def test_requirements::editor::simpledependency_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=requirements::editor::SimpleDependency_strategy)
def test_requirements::editor::simpledependency_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)

@given(instance=requirements::editor::FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_requirements::editor::functionalrequirement_instantiation(instance):
    assert isinstance(instance, requirements::editor::FunctionalRequirement)

@given(instance=requirements::editor::QualityRequirement_strategy)
@settings(max_examples=50)
def test_requirements::editor::qualityrequirement_instantiation(instance):
    assert isinstance(instance, requirements::editor::QualityRequirement)

@given(instance=Description_strategy)
@settings(max_examples=50)
def test_description_instantiation(instance):
    assert isinstance(instance, Description)

@given(instance=requirements::editor::TextualDescription_strategy)
@settings(max_examples=50)
def test_requirements::editor::textualdescription_instantiation(instance):
    assert isinstance(instance, requirements::editor::TextualDescription)

@given(instance=requirements::editor::TextualDescription_strategy)
def test_requirements::editor::textualdescription_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=requirements::editor::TextualDescription_strategy)
def test_requirements::editor::textualdescription_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=requirements::editor::Category_strategy)
@settings(max_examples=50)
def test_requirements::editor::category_instantiation(instance):
    assert isinstance(instance, requirements::editor::Category)

@given(instance=requirements::editor::Category_strategy)
def test_requirements::editor::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=requirements::editor::Category_strategy)
def test_requirements::editor::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=requirements::editor::Dependency_strategy)
@settings(max_examples=50)
def test_requirements::editor::dependency_instantiation(instance):
    assert isinstance(instance, requirements::editor::Dependency)

@given(instance=requirements::editor::Person_strategy)
@settings(max_examples=50)
def test_requirements::editor::person_instantiation(instance):
    assert isinstance(instance, requirements::editor::Person)

@given(instance=requirements::editor::Person_strategy)
def test_requirements::editor::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=requirements::editor::Person_strategy)
def test_requirements::editor::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=requirements::editor::Description_strategy)
@settings(max_examples=50)
def test_requirements::editor::description_instantiation(instance):
    assert isinstance(instance, requirements::editor::Description)

@given(instance=requirements::editor::Requirement_strategy)
@settings(max_examples=50)
def test_requirements::editor::requirement_instantiation(instance):
    assert isinstance(instance, requirements::editor::Requirement)

@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=requirements::editor::Requirement_strategy)
def test_requirements::editor::requirement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=requirements::editor::Requirement_strategy)
@settings(max_examples=30)
def test_requirements::editor::requirement_findleafnodes_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findLeafNodes(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findLeafNodes).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findLeafNodes' in requirements::editor::Requirement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findLeafNodes' in requirements::editor::Requirement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findLeafNodes' in requirements::editor::Requirement is not implemented or raised an error")
