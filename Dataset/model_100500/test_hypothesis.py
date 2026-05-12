import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryOperator,
    newP::OrOperator,
    newP::AndOperartor,
    UnaryOperator,
    newP::BinaryOperator,
    newP::NotOperator,
    SimpleDependency,
    newP::ICost,
    newP::Refines,
    newP::CValue,
    newP::Person,
    newP::Specification,
    newP::Category,
    Description,
    newP::TextDescription,
    Requirement,
    newP::QualityRequirement,
    newP::FunctionalRequirement,
    Dependency,
    newP::SimpleDependency,
    newP::Requires,
    Term,
    newP::RequirementTerm,
    newP::UnaryOperator,
    newP::Term,
    newP::Dependency,
    newP::Description,
    newP::Requirement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_newp::oroperator_is_not_abstract():
    assert not inspect.isabstract(newP::OrOperator)


def test_newp::oroperator_constructor_exists():
    assert callable(newP::OrOperator.__init__)


def test_newp::oroperator_constructor_args():
    sig = inspect.signature(newP::OrOperator.__init__)
    params = list(sig.parameters.keys())



def test_newp::andoperartor_is_not_abstract():
    assert not inspect.isabstract(newP::AndOperartor)


def test_newp::andoperartor_constructor_exists():
    assert callable(newP::AndOperartor.__init__)


def test_newp::andoperartor_constructor_args():
    sig = inspect.signature(newP::AndOperartor.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_newp::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(newP::BinaryOperator)


def test_newp::binaryoperator_constructor_exists():
    assert callable(newP::BinaryOperator.__init__)


def test_newp::binaryoperator_constructor_args():
    sig = inspect.signature(newP::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_newp::notoperator_is_not_abstract():
    assert not inspect.isabstract(newP::NotOperator)


def test_newp::notoperator_constructor_exists():
    assert callable(newP::NotOperator.__init__)


def test_newp::notoperator_constructor_args():
    sig = inspect.signature(newP::NotOperator.__init__)
    params = list(sig.parameters.keys())



def test_simpledependency_is_not_abstract():
    assert not inspect.isabstract(SimpleDependency)


def test_simpledependency_constructor_exists():
    assert callable(SimpleDependency.__init__)


def test_simpledependency_constructor_args():
    sig = inspect.signature(SimpleDependency.__init__)
    params = list(sig.parameters.keys())



def test_newp::icost_is_not_abstract():
    assert not inspect.isabstract(newP::ICost)


def test_newp::icost_constructor_exists():
    assert callable(newP::ICost.__init__)


def test_newp::icost_constructor_args():
    sig = inspect.signature(newP::ICost.__init__)
    params = list(sig.parameters.keys())



def test_newp::refines_is_not_abstract():
    assert not inspect.isabstract(newP::Refines)


def test_newp::refines_constructor_exists():
    assert callable(newP::Refines.__init__)


def test_newp::refines_constructor_args():
    sig = inspect.signature(newP::Refines.__init__)
    params = list(sig.parameters.keys())



def test_newp::cvalue_is_not_abstract():
    assert not inspect.isabstract(newP::CValue)


def test_newp::cvalue_constructor_exists():
    assert callable(newP::CValue.__init__)


def test_newp::cvalue_constructor_args():
    sig = inspect.signature(newP::CValue.__init__)
    params = list(sig.parameters.keys())



def test_newp::person_is_not_abstract():
    assert not inspect.isabstract(newP::Person)


def test_newp::person_constructor_exists():
    assert callable(newP::Person.__init__)


def test_newp::person_constructor_args():
    sig = inspect.signature(newP::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_newp::person_has_firstName():
    assert hasattr(newP::Person, "firstName")
    descriptor = None
    for klass in newP::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_newp::person_has_lastName():
    assert hasattr(newP::Person, "lastName")
    descriptor = None
    for klass in newP::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_newp::specification_is_not_abstract():
    assert not inspect.isabstract(newP::Specification)


def test_newp::specification_constructor_exists():
    assert callable(newP::Specification.__init__)


def test_newp::specification_constructor_args():
    sig = inspect.signature(newP::Specification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_newp::specification_has_name():
    assert hasattr(newP::Specification, "name")
    descriptor = None
    for klass in newP::Specification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_newp::category_is_not_abstract():
    assert not inspect.isabstract(newP::Category)


def test_newp::category_constructor_exists():
    assert callable(newP::Category.__init__)


def test_newp::category_constructor_args():
    sig = inspect.signature(newP::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_newp::category_has_name():
    assert hasattr(newP::Category, "name")
    descriptor = None
    for klass in newP::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_description_is_not_abstract():
    assert not inspect.isabstract(Description)


def test_description_constructor_exists():
    assert callable(Description.__init__)


def test_description_constructor_args():
    sig = inspect.signature(Description.__init__)
    params = list(sig.parameters.keys())



def test_newp::textdescription_is_not_abstract():
    assert not inspect.isabstract(newP::TextDescription)


def test_newp::textdescription_constructor_exists():
    assert callable(newP::TextDescription.__init__)


def test_newp::textdescription_constructor_args():
    sig = inspect.signature(newP::TextDescription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_newp::textdescription_has_text():
    assert hasattr(newP::TextDescription, "text")
    descriptor = None
    for klass in newP::TextDescription.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_requirement_is_not_abstract():
    assert not inspect.isabstract(Requirement)


def test_requirement_constructor_exists():
    assert callable(Requirement.__init__)


def test_requirement_constructor_args():
    sig = inspect.signature(Requirement.__init__)
    params = list(sig.parameters.keys())



def test_newp::qualityrequirement_is_not_abstract():
    assert not inspect.isabstract(newP::QualityRequirement)


def test_newp::qualityrequirement_constructor_exists():
    assert callable(newP::QualityRequirement.__init__)


def test_newp::qualityrequirement_constructor_args():
    sig = inspect.signature(newP::QualityRequirement.__init__)
    params = list(sig.parameters.keys())



def test_newp::functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(newP::FunctionalRequirement)


def test_newp::functionalrequirement_constructor_exists():
    assert callable(newP::FunctionalRequirement.__init__)


def test_newp::functionalrequirement_constructor_args():
    sig = inspect.signature(newP::FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_newp::simpledependency_is_not_abstract():
    assert not inspect.isabstract(newP::SimpleDependency)


def test_newp::simpledependency_constructor_exists():
    assert callable(newP::SimpleDependency.__init__)


def test_newp::simpledependency_constructor_args():
    sig = inspect.signature(newP::SimpleDependency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_newp::simpledependency_has_name():
    assert hasattr(newP::SimpleDependency, "name")
    descriptor = None
    for klass in newP::SimpleDependency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_newp::requires_is_not_abstract():
    assert not inspect.isabstract(newP::Requires)


def test_newp::requires_constructor_exists():
    assert callable(newP::Requires.__init__)


def test_newp::requires_constructor_args():
    sig = inspect.signature(newP::Requires.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_newp::requires_has_name():
    assert hasattr(newP::Requires, "name")
    descriptor = None
    for klass in newP::Requires.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_newp::requirementterm_is_not_abstract():
    assert not inspect.isabstract(newP::RequirementTerm)


def test_newp::requirementterm_constructor_exists():
    assert callable(newP::RequirementTerm.__init__)


def test_newp::requirementterm_constructor_args():
    sig = inspect.signature(newP::RequirementTerm.__init__)
    params = list(sig.parameters.keys())



def test_newp::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(newP::UnaryOperator)


def test_newp::unaryoperator_constructor_exists():
    assert callable(newP::UnaryOperator.__init__)


def test_newp::unaryoperator_constructor_args():
    sig = inspect.signature(newP::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_newp::unaryoperator_has_name():
    assert hasattr(newP::UnaryOperator, "name")
    descriptor = None
    for klass in newP::UnaryOperator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_newp::term_is_not_abstract():
    assert not inspect.isabstract(newP::Term)


def test_newp::term_constructor_exists():
    assert callable(newP::Term.__init__)


def test_newp::term_constructor_args():
    sig = inspect.signature(newP::Term.__init__)
    params = list(sig.parameters.keys())



def test_newp::dependency_is_not_abstract():
    assert not inspect.isabstract(newP::Dependency)


def test_newp::dependency_constructor_exists():
    assert callable(newP::Dependency.__init__)


def test_newp::dependency_constructor_args():
    sig = inspect.signature(newP::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_newp::description_is_not_abstract():
    assert not inspect.isabstract(newP::Description)


def test_newp::description_constructor_exists():
    assert callable(newP::Description.__init__)


def test_newp::description_constructor_args():
    sig = inspect.signature(newP::Description.__init__)
    params = list(sig.parameters.keys())



def test_newp::requirement_is_not_abstract():
    assert not inspect.isabstract(newP::Requirement)


def test_newp::requirement_constructor_exists():
    assert callable(newP::Requirement.__init__)


def test_newp::requirement_constructor_args():
    sig = inspect.signature(newP::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_newp::requirement_has_mandatory():
    assert hasattr(newP::Requirement, "mandatory")
    descriptor = None
    for klass in newP::Requirement.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_newp::requirement_has_name():
    assert hasattr(newP::Requirement, "name")
    descriptor = None
    for klass in newP::Requirement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_newp::requirement_has_priority():
    assert hasattr(newP::Requirement, "priority")
    descriptor = None
    for klass in newP::Requirement.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_newp::requirement_has_identifier():
    assert hasattr(newP::Requirement, "identifier")
    descriptor = None
    for klass in newP::Requirement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)


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
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
newP::OrOperator_strategy = st.builds(
    newP::OrOperator,
)
newP::AndOperartor_strategy = st.builds(
    newP::AndOperartor,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
newP::BinaryOperator_strategy = st.builds(
    newP::BinaryOperator,
)
newP::NotOperator_strategy = st.builds(
    newP::NotOperator,
)
SimpleDependency_strategy = st.builds(
    SimpleDependency,
)
newP::ICost_strategy = st.builds(
    newP::ICost,
)
newP::Refines_strategy = st.builds(
    newP::Refines,
)
newP::CValue_strategy = st.builds(
    newP::CValue,
)
newP::Person_strategy = st.builds(
    newP::Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)
newP::Specification_strategy = st.builds(
    newP::Specification,
    name=
        safe_text
)
newP::Category_strategy = st.builds(
    newP::Category,
    name=
        safe_text
)
Description_strategy = st.builds(
    Description,
)
newP::TextDescription_strategy = st.builds(
    newP::TextDescription,
    text=
        safe_text
)
Requirement_strategy = st.builds(
    Requirement,
)
newP::QualityRequirement_strategy = st.builds(
    newP::QualityRequirement,
)
newP::FunctionalRequirement_strategy = st.builds(
    newP::FunctionalRequirement,
)
Dependency_strategy = st.builds(
    Dependency,
)
newP::SimpleDependency_strategy = st.builds(
    newP::SimpleDependency,
    name=
        safe_text
)
newP::Requires_strategy = st.builds(
    newP::Requires,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
newP::RequirementTerm_strategy = st.builds(
    newP::RequirementTerm,
)
newP::UnaryOperator_strategy = st.builds(
    newP::UnaryOperator,
    name=
        safe_text
)
newP::Term_strategy = st.builds(
    newP::Term,
)
newP::Dependency_strategy = st.builds(
    newP::Dependency,
)
newP::Description_strategy = st.builds(
    newP::Description,
)
newP::Requirement_strategy = st.builds(
    newP::Requirement,
    mandatory=
        st.booleans(),
    name=
        safe_text,
    priority=
        st.integers(),
    identifier=
        safe_text
)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=newP::OrOperator_strategy)
@settings(max_examples=50)
def test_newp::oroperator_instantiation(instance):
    assert isinstance(instance, newP::OrOperator)

@given(instance=newP::AndOperartor_strategy)
@settings(max_examples=50)
def test_newp::andoperartor_instantiation(instance):
    assert isinstance(instance, newP::AndOperartor)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=newP::BinaryOperator_strategy)
@settings(max_examples=50)
def test_newp::binaryoperator_instantiation(instance):
    assert isinstance(instance, newP::BinaryOperator)

@given(instance=newP::NotOperator_strategy)
@settings(max_examples=50)
def test_newp::notoperator_instantiation(instance):
    assert isinstance(instance, newP::NotOperator)

@given(instance=SimpleDependency_strategy)
@settings(max_examples=50)
def test_simpledependency_instantiation(instance):
    assert isinstance(instance, SimpleDependency)

@given(instance=newP::ICost_strategy)
@settings(max_examples=50)
def test_newp::icost_instantiation(instance):
    assert isinstance(instance, newP::ICost)

@given(instance=newP::Refines_strategy)
@settings(max_examples=50)
def test_newp::refines_instantiation(instance):
    assert isinstance(instance, newP::Refines)

@given(instance=newP::CValue_strategy)
@settings(max_examples=50)
def test_newp::cvalue_instantiation(instance):
    assert isinstance(instance, newP::CValue)

@given(instance=newP::Person_strategy)
@settings(max_examples=50)
def test_newp::person_instantiation(instance):
    assert isinstance(instance, newP::Person)

@given(instance=newP::Person_strategy)
def test_newp::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=newP::Person_strategy)
def test_newp::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=newP::Person_strategy)
def test_newp::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=newP::Person_strategy)
def test_newp::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=newP::Specification_strategy)
@settings(max_examples=50)
def test_newp::specification_instantiation(instance):
    assert isinstance(instance, newP::Specification)

@given(instance=newP::Specification_strategy)
def test_newp::specification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::Specification_strategy)
def test_newp::specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=newP::Category_strategy)
@settings(max_examples=50)
def test_newp::category_instantiation(instance):
    assert isinstance(instance, newP::Category)

@given(instance=newP::Category_strategy)
def test_newp::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::Category_strategy)
def test_newp::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Description_strategy)
@settings(max_examples=50)
def test_description_instantiation(instance):
    assert isinstance(instance, Description)

@given(instance=newP::TextDescription_strategy)
@settings(max_examples=50)
def test_newp::textdescription_instantiation(instance):
    assert isinstance(instance, newP::TextDescription)

@given(instance=newP::TextDescription_strategy)
def test_newp::textdescription_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=newP::TextDescription_strategy)
def test_newp::textdescription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Requirement_strategy)
@settings(max_examples=50)
def test_requirement_instantiation(instance):
    assert isinstance(instance, Requirement)

@given(instance=newP::QualityRequirement_strategy)
@settings(max_examples=50)
def test_newp::qualityrequirement_instantiation(instance):
    assert isinstance(instance, newP::QualityRequirement)

@given(instance=newP::FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_newp::functionalrequirement_instantiation(instance):
    assert isinstance(instance, newP::FunctionalRequirement)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=newP::SimpleDependency_strategy)
@settings(max_examples=50)
def test_newp::simpledependency_instantiation(instance):
    assert isinstance(instance, newP::SimpleDependency)

@given(instance=newP::SimpleDependency_strategy)
def test_newp::simpledependency_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::SimpleDependency_strategy)
def test_newp::simpledependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=newP::Requires_strategy)
@settings(max_examples=50)
def test_newp::requires_instantiation(instance):
    assert isinstance(instance, newP::Requires)

@given(instance=newP::Requires_strategy)
def test_newp::requires_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::Requires_strategy)
def test_newp::requires_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=newP::RequirementTerm_strategy)
@settings(max_examples=50)
def test_newp::requirementterm_instantiation(instance):
    assert isinstance(instance, newP::RequirementTerm)

@given(instance=newP::UnaryOperator_strategy)
@settings(max_examples=50)
def test_newp::unaryoperator_instantiation(instance):
    assert isinstance(instance, newP::UnaryOperator)

@given(instance=newP::UnaryOperator_strategy)
def test_newp::unaryoperator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::UnaryOperator_strategy)
def test_newp::unaryoperator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=newP::Term_strategy)
@settings(max_examples=50)
def test_newp::term_instantiation(instance):
    assert isinstance(instance, newP::Term)

@given(instance=newP::Dependency_strategy)
@settings(max_examples=50)
def test_newp::dependency_instantiation(instance):
    assert isinstance(instance, newP::Dependency)

@given(instance=newP::Description_strategy)
@settings(max_examples=50)
def test_newp::description_instantiation(instance):
    assert isinstance(instance, newP::Description)

@given(instance=newP::Requirement_strategy)
@settings(max_examples=50)
def test_newp::requirement_instantiation(instance):
    assert isinstance(instance, newP::Requirement)

@given(instance=newP::Requirement_strategy)
def test_newp::requirement_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=newP::Requirement_strategy)
def test_newp::requirement_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=newP::Requirement_strategy)
def test_newp::requirement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=newP::Requirement_strategy)
def test_newp::requirement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=newP::Requirement_strategy)
def test_newp::requirement_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=newP::Requirement_strategy)
def test_newp::requirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=newP::Requirement_strategy)
def test_newp::requirement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=newP::Requirement_strategy)
def test_newp::requirement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original
