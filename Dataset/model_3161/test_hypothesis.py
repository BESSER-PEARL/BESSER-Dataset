import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    altarica::EBoolean,
    altarica::Equal,
    altarica::EString,
    altarica::Division,
    altarica::Imply,
    altarica::EInteger,
    altarica::Minus,
    altarica::Multiplication,
    altarica::Addition,
    altarica::NotEqual,
    altarica::Upper,
    altarica::VariableRef,
    altarica::NavigableVariable,
    altarica::Or,
    altarica::And,
    altarica::CaseExpression,
    AbstractBooleanExpression,
    AbstractExpression,
    altarica::Switch,
    altarica::Transition,
    altarica::EventRef,
    altarica::Cardinality,
    altarica::VectorParameter,
    altarica::Vector,
    altarica::EObject,
    altarica::IfThenElse,
    altarica::NodeInstanceDeclaration,
    altarica::StateDeclaration,
    altarica::AbstractExpression,
    altarica::Priority,
    NavigableVariable,
    altarica::NonNavigableVariable,
    altarica::Event,
    altarica::EventDeclaration,
    altarica::AbstractTypeRef,
    altarica::AbstractBooleanExpression,
    altarica::Assert,
    altarica::NodeInstance,
    altarica::Affectation,
    altarica::InitStatement,
    AbstractSpecification,
    altarica::StateSpecification,
    altarica::VectorSpecification,
    altarica::EventSpecification,
    altarica::NodeInstanceSpecification,
    altarica::AssertSpecification,
    altarica::TransitionSpecification,
    altarica::InitSpecification,
    altarica::VariableAttribute,
    altarica::AbstractSpecification,
    AbstractDomain,
    altarica::PrimitiveType,
    altarica::Enumeration,
    altarica::Range,
    AbstractTypeRef,
    altarica::DomainRef,
    altarica::AbstractDomain,
    AbstractDefinitionConstant,
    altarica::DomainConstant,
    altarica::ExpressionConstant,
    altarica::Expression,
    altarica::FlowDeclaration,
    altarica::FlowSpecification,
    altarica::ExternalDirective,
    altarica::ExternalSpecification,
    altarica::System,
    NonNavigableVariable,
    altarica::State,
    altarica::Flow,
    altarica::Literal,
    altarica::AbstractDefinitionConstant,
    altarica::Constant,
    AbstractDeclaration,
    altarica::Node,
    altarica::Domain,
    altarica::ConstantDefinition,
    altarica::AbstractDeclaration,
    VariableRef,
    altarica::NestedQualifiedVariableRef,
    EventRef,
    altarica::NestedQualifiedEventRef,
    altarica::StrictUpper,
    altarica::Lower,
    altarica::StrictLower,
    FlowKind,
    PrimitiveTypeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eboolean_is_not_abstract():
    assert not inspect.isabstract(altarica::EBoolean)


def test_altarica::eboolean_constructor_exists():
    assert callable(altarica::EBoolean.__init__)


def test_altarica::eboolean_constructor_args():
    sig = inspect.signature(altarica::EBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::eboolean_has_value():
    assert hasattr(altarica::EBoolean, "value")
    descriptor = None
    for klass in altarica::EBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::equal_is_not_abstract():
    assert not inspect.isabstract(altarica::Equal)


def test_altarica::equal_constructor_exists():
    assert callable(altarica::Equal.__init__)


def test_altarica::equal_constructor_args():
    sig = inspect.signature(altarica::Equal.__init__)
    params = list(sig.parameters.keys())



def test_altarica::estring_is_not_abstract():
    assert not inspect.isabstract(altarica::EString)


def test_altarica::estring_constructor_exists():
    assert callable(altarica::EString.__init__)


def test_altarica::estring_constructor_args():
    sig = inspect.signature(altarica::EString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::estring_has_value():
    assert hasattr(altarica::EString, "value")
    descriptor = None
    for klass in altarica::EString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::division_is_not_abstract():
    assert not inspect.isabstract(altarica::Division)


def test_altarica::division_constructor_exists():
    assert callable(altarica::Division.__init__)


def test_altarica::division_constructor_args():
    sig = inspect.signature(altarica::Division.__init__)
    params = list(sig.parameters.keys())



def test_altarica::imply_is_not_abstract():
    assert not inspect.isabstract(altarica::Imply)


def test_altarica::imply_constructor_exists():
    assert callable(altarica::Imply.__init__)


def test_altarica::imply_constructor_args():
    sig = inspect.signature(altarica::Imply.__init__)
    params = list(sig.parameters.keys())



def test_altarica::einteger_is_not_abstract():
    assert not inspect.isabstract(altarica::EInteger)


def test_altarica::einteger_constructor_exists():
    assert callable(altarica::EInteger.__init__)


def test_altarica::einteger_constructor_args():
    sig = inspect.signature(altarica::EInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_altarica::einteger_has_value():
    assert hasattr(altarica::EInteger, "value")
    descriptor = None
    for klass in altarica::EInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_altarica::minus_is_not_abstract():
    assert not inspect.isabstract(altarica::Minus)


def test_altarica::minus_constructor_exists():
    assert callable(altarica::Minus.__init__)


def test_altarica::minus_constructor_args():
    sig = inspect.signature(altarica::Minus.__init__)
    params = list(sig.parameters.keys())



def test_altarica::multiplication_is_not_abstract():
    assert not inspect.isabstract(altarica::Multiplication)


def test_altarica::multiplication_constructor_exists():
    assert callable(altarica::Multiplication.__init__)


def test_altarica::multiplication_constructor_args():
    sig = inspect.signature(altarica::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_altarica::addition_is_not_abstract():
    assert not inspect.isabstract(altarica::Addition)


def test_altarica::addition_constructor_exists():
    assert callable(altarica::Addition.__init__)


def test_altarica::addition_constructor_args():
    sig = inspect.signature(altarica::Addition.__init__)
    params = list(sig.parameters.keys())



def test_altarica::notequal_is_not_abstract():
    assert not inspect.isabstract(altarica::NotEqual)


def test_altarica::notequal_constructor_exists():
    assert callable(altarica::NotEqual.__init__)


def test_altarica::notequal_constructor_args():
    sig = inspect.signature(altarica::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_altarica::upper_is_not_abstract():
    assert not inspect.isabstract(altarica::Upper)


def test_altarica::upper_constructor_exists():
    assert callable(altarica::Upper.__init__)


def test_altarica::upper_constructor_args():
    sig = inspect.signature(altarica::Upper.__init__)
    params = list(sig.parameters.keys())



def test_altarica::variableref_is_not_abstract():
    assert not inspect.isabstract(altarica::VariableRef)


def test_altarica::variableref_constructor_exists():
    assert callable(altarica::VariableRef.__init__)


def test_altarica::variableref_constructor_args():
    sig = inspect.signature(altarica::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::navigablevariable_is_not_abstract():
    assert not inspect.isabstract(altarica::NavigableVariable)


def test_altarica::navigablevariable_constructor_exists():
    assert callable(altarica::NavigableVariable.__init__)


def test_altarica::navigablevariable_constructor_args():
    sig = inspect.signature(altarica::NavigableVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::navigablevariable_has_name():
    assert hasattr(altarica::NavigableVariable, "name")
    descriptor = None
    for klass in altarica::NavigableVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::or_is_not_abstract():
    assert not inspect.isabstract(altarica::Or)


def test_altarica::or_constructor_exists():
    assert callable(altarica::Or.__init__)


def test_altarica::or_constructor_args():
    sig = inspect.signature(altarica::Or.__init__)
    params = list(sig.parameters.keys())



def test_altarica::and_is_not_abstract():
    assert not inspect.isabstract(altarica::And)


def test_altarica::and_constructor_exists():
    assert callable(altarica::And.__init__)


def test_altarica::and_constructor_args():
    sig = inspect.signature(altarica::And.__init__)
    params = list(sig.parameters.keys())



def test_altarica::caseexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::CaseExpression)


def test_altarica::caseexpression_constructor_exists():
    assert callable(altarica::CaseExpression.__init__)


def test_altarica::caseexpression_constructor_args():
    sig = inspect.signature(altarica::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractBooleanExpression)


def test_abstractbooleanexpression_constructor_exists():
    assert callable(AbstractBooleanExpression.__init__)


def test_abstractbooleanexpression_constructor_args():
    sig = inspect.signature(AbstractBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractExpression)


def test_abstractexpression_constructor_exists():
    assert callable(AbstractExpression.__init__)


def test_abstractexpression_constructor_args():
    sig = inspect.signature(AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::switch_is_not_abstract():
    assert not inspect.isabstract(altarica::Switch)


def test_altarica::switch_constructor_exists():
    assert callable(altarica::Switch.__init__)


def test_altarica::switch_constructor_args():
    sig = inspect.signature(altarica::Switch.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transition_is_not_abstract():
    assert not inspect.isabstract(altarica::Transition)


def test_altarica::transition_constructor_exists():
    assert callable(altarica::Transition.__init__)


def test_altarica::transition_constructor_args():
    sig = inspect.signature(altarica::Transition.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eventref_is_not_abstract():
    assert not inspect.isabstract(altarica::EventRef)


def test_altarica::eventref_constructor_exists():
    assert callable(altarica::EventRef.__init__)


def test_altarica::eventref_constructor_args():
    sig = inspect.signature(altarica::EventRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::cardinality_is_not_abstract():
    assert not inspect.isabstract(altarica::Cardinality)


def test_altarica::cardinality_constructor_exists():
    assert callable(altarica::Cardinality.__init__)


def test_altarica::cardinality_constructor_args():
    sig = inspect.signature(altarica::Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_altarica::vectorparameter_is_not_abstract():
    assert not inspect.isabstract(altarica::VectorParameter)


def test_altarica::vectorparameter_constructor_exists():
    assert callable(altarica::VectorParameter.__init__)


def test_altarica::vectorparameter_constructor_args():
    sig = inspect.signature(altarica::VectorParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_altarica::vectorparameter_has_isRequired():
    assert hasattr(altarica::VectorParameter, "isRequired")
    descriptor = None
    for klass in altarica::VectorParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_altarica::vector_is_not_abstract():
    assert not inspect.isabstract(altarica::Vector)


def test_altarica::vector_constructor_exists():
    assert callable(altarica::Vector.__init__)


def test_altarica::vector_constructor_args():
    sig = inspect.signature(altarica::Vector.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eobject_is_not_abstract():
    assert not inspect.isabstract(altarica::EObject)


def test_altarica::eobject_constructor_exists():
    assert callable(altarica::EObject.__init__)


def test_altarica::eobject_constructor_args():
    sig = inspect.signature(altarica::EObject.__init__)
    params = list(sig.parameters.keys())



def test_altarica::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(altarica::IfThenElse)


def test_altarica::ifthenelse_constructor_exists():
    assert callable(altarica::IfThenElse.__init__)


def test_altarica::ifthenelse_constructor_args():
    sig = inspect.signature(altarica::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nodeinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::NodeInstanceDeclaration)


def test_altarica::nodeinstancedeclaration_constructor_exists():
    assert callable(altarica::NodeInstanceDeclaration.__init__)


def test_altarica::nodeinstancedeclaration_constructor_args():
    sig = inspect.signature(altarica::NodeInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::statedeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::StateDeclaration)


def test_altarica::statedeclaration_constructor_exists():
    assert callable(altarica::StateDeclaration.__init__)


def test_altarica::statedeclaration_constructor_args():
    sig = inspect.signature(altarica::StateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractExpression)


def test_altarica::abstractexpression_constructor_exists():
    assert callable(altarica::AbstractExpression.__init__)


def test_altarica::abstractexpression_constructor_args():
    sig = inspect.signature(altarica::AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::priority_is_not_abstract():
    assert not inspect.isabstract(altarica::Priority)


def test_altarica::priority_constructor_exists():
    assert callable(altarica::Priority.__init__)


def test_altarica::priority_constructor_args():
    sig = inspect.signature(altarica::Priority.__init__)
    params = list(sig.parameters.keys())



def test_navigablevariable_is_not_abstract():
    assert not inspect.isabstract(NavigableVariable)


def test_navigablevariable_constructor_exists():
    assert callable(NavigableVariable.__init__)


def test_navigablevariable_constructor_args():
    sig = inspect.signature(NavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nonnavigablevariable_is_not_abstract():
    assert not inspect.isabstract(altarica::NonNavigableVariable)


def test_altarica::nonnavigablevariable_constructor_exists():
    assert callable(altarica::NonNavigableVariable.__init__)


def test_altarica::nonnavigablevariable_constructor_args():
    sig = inspect.signature(altarica::NonNavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica::event_is_not_abstract():
    assert not inspect.isabstract(altarica::Event)


def test_altarica::event_constructor_exists():
    assert callable(altarica::Event.__init__)


def test_altarica::event_constructor_args():
    sig = inspect.signature(altarica::Event.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::EventDeclaration)


def test_altarica::eventdeclaration_constructor_exists():
    assert callable(altarica::EventDeclaration.__init__)


def test_altarica::eventdeclaration_constructor_args():
    sig = inspect.signature(altarica::EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstracttyperef_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractTypeRef)


def test_altarica::abstracttyperef_constructor_exists():
    assert callable(altarica::AbstractTypeRef.__init__)


def test_altarica::abstracttyperef_constructor_args():
    sig = inspect.signature(altarica::AbstractTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractBooleanExpression)


def test_altarica::abstractbooleanexpression_constructor_exists():
    assert callable(altarica::AbstractBooleanExpression.__init__)


def test_altarica::abstractbooleanexpression_constructor_args():
    sig = inspect.signature(altarica::AbstractBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::assert_is_not_abstract():
    assert not inspect.isabstract(altarica::Assert)


def test_altarica::assert_constructor_exists():
    assert callable(altarica::Assert.__init__)


def test_altarica::assert_constructor_args():
    sig = inspect.signature(altarica::Assert.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nodeinstance_is_not_abstract():
    assert not inspect.isabstract(altarica::NodeInstance)


def test_altarica::nodeinstance_constructor_exists():
    assert callable(altarica::NodeInstance.__init__)


def test_altarica::nodeinstance_constructor_args():
    sig = inspect.signature(altarica::NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_altarica::affectation_is_not_abstract():
    assert not inspect.isabstract(altarica::Affectation)


def test_altarica::affectation_constructor_exists():
    assert callable(altarica::Affectation.__init__)


def test_altarica::affectation_constructor_args():
    sig = inspect.signature(altarica::Affectation.__init__)
    params = list(sig.parameters.keys())



def test_altarica::initstatement_is_not_abstract():
    assert not inspect.isabstract(altarica::InitStatement)


def test_altarica::initstatement_constructor_exists():
    assert callable(altarica::InitStatement.__init__)


def test_altarica::initstatement_constructor_args():
    sig = inspect.signature(altarica::InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractspecification_is_not_abstract():
    assert not inspect.isabstract(AbstractSpecification)


def test_abstractspecification_constructor_exists():
    assert callable(AbstractSpecification.__init__)


def test_abstractspecification_constructor_args():
    sig = inspect.signature(AbstractSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::statespecification_is_not_abstract():
    assert not inspect.isabstract(altarica::StateSpecification)


def test_altarica::statespecification_constructor_exists():
    assert callable(altarica::StateSpecification.__init__)


def test_altarica::statespecification_constructor_args():
    sig = inspect.signature(altarica::StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::vectorspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::VectorSpecification)


def test_altarica::vectorspecification_constructor_exists():
    assert callable(altarica::VectorSpecification.__init__)


def test_altarica::vectorspecification_constructor_args():
    sig = inspect.signature(altarica::VectorSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::eventspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::EventSpecification)


def test_altarica::eventspecification_constructor_exists():
    assert callable(altarica::EventSpecification.__init__)


def test_altarica::eventspecification_constructor_args():
    sig = inspect.signature(altarica::EventSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nodeinstancespecification_is_not_abstract():
    assert not inspect.isabstract(altarica::NodeInstanceSpecification)


def test_altarica::nodeinstancespecification_constructor_exists():
    assert callable(altarica::NodeInstanceSpecification.__init__)


def test_altarica::nodeinstancespecification_constructor_args():
    sig = inspect.signature(altarica::NodeInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::assertspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::AssertSpecification)


def test_altarica::assertspecification_constructor_exists():
    assert callable(altarica::AssertSpecification.__init__)


def test_altarica::assertspecification_constructor_args():
    sig = inspect.signature(altarica::AssertSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::transitionspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::TransitionSpecification)


def test_altarica::transitionspecification_constructor_exists():
    assert callable(altarica::TransitionSpecification.__init__)


def test_altarica::transitionspecification_constructor_args():
    sig = inspect.signature(altarica::TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::initspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::InitSpecification)


def test_altarica::initspecification_constructor_exists():
    assert callable(altarica::InitSpecification.__init__)


def test_altarica::initspecification_constructor_args():
    sig = inspect.signature(altarica::InitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::variableattribute_is_not_abstract():
    assert not inspect.isabstract(altarica::VariableAttribute)


def test_altarica::variableattribute_constructor_exists():
    assert callable(altarica::VariableAttribute.__init__)


def test_altarica::variableattribute_constructor_args():
    sig = inspect.signature(altarica::VariableAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::variableattribute_has_name():
    assert hasattr(altarica::VariableAttribute, "name")
    descriptor = None
    for klass in altarica::VariableAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::abstractspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractSpecification)


def test_altarica::abstractspecification_constructor_exists():
    assert callable(altarica::AbstractSpecification.__init__)


def test_altarica::abstractspecification_constructor_args():
    sig = inspect.signature(altarica::AbstractSpecification.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomain_is_not_abstract():
    assert not inspect.isabstract(AbstractDomain)


def test_abstractdomain_constructor_exists():
    assert callable(AbstractDomain.__init__)


def test_abstractdomain_constructor_args():
    sig = inspect.signature(AbstractDomain.__init__)
    params = list(sig.parameters.keys())



def test_altarica::primitivetype_is_not_abstract():
    assert not inspect.isabstract(altarica::PrimitiveType)


def test_altarica::primitivetype_constructor_exists():
    assert callable(altarica::PrimitiveType.__init__)


def test_altarica::primitivetype_constructor_args():
    sig = inspect.signature(altarica::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::primitivetype_has_name():
    assert hasattr(altarica::PrimitiveType, "name")
    descriptor = None
    for klass in altarica::PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::enumeration_is_not_abstract():
    assert not inspect.isabstract(altarica::Enumeration)


def test_altarica::enumeration_constructor_exists():
    assert callable(altarica::Enumeration.__init__)


def test_altarica::enumeration_constructor_args():
    sig = inspect.signature(altarica::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::range_is_not_abstract():
    assert not inspect.isabstract(altarica::Range)


def test_altarica::range_constructor_exists():
    assert callable(altarica::Range.__init__)


def test_altarica::range_constructor_args():
    sig = inspect.signature(altarica::Range.__init__)
    params = list(sig.parameters.keys())



def test_abstracttyperef_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeRef)


def test_abstracttyperef_constructor_exists():
    assert callable(AbstractTypeRef.__init__)


def test_abstracttyperef_constructor_args():
    sig = inspect.signature(AbstractTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::domainref_is_not_abstract():
    assert not inspect.isabstract(altarica::DomainRef)


def test_altarica::domainref_constructor_exists():
    assert callable(altarica::DomainRef.__init__)


def test_altarica::domainref_constructor_args():
    sig = inspect.signature(altarica::DomainRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractdomain_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractDomain)


def test_altarica::abstractdomain_constructor_exists():
    assert callable(altarica::AbstractDomain.__init__)


def test_altarica::abstractdomain_constructor_args():
    sig = inspect.signature(altarica::AbstractDomain.__init__)
    params = list(sig.parameters.keys())



def test_abstractdefinitionconstant_is_not_abstract():
    assert not inspect.isabstract(AbstractDefinitionConstant)


def test_abstractdefinitionconstant_constructor_exists():
    assert callable(AbstractDefinitionConstant.__init__)


def test_abstractdefinitionconstant_constructor_args():
    sig = inspect.signature(AbstractDefinitionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica::domainconstant_is_not_abstract():
    assert not inspect.isabstract(altarica::DomainConstant)


def test_altarica::domainconstant_constructor_exists():
    assert callable(altarica::DomainConstant.__init__)


def test_altarica::domainconstant_constructor_args():
    sig = inspect.signature(altarica::DomainConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica::expressionconstant_is_not_abstract():
    assert not inspect.isabstract(altarica::ExpressionConstant)


def test_altarica::expressionconstant_constructor_exists():
    assert callable(altarica::ExpressionConstant.__init__)


def test_altarica::expressionconstant_constructor_args():
    sig = inspect.signature(altarica::ExpressionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica::expression_is_not_abstract():
    assert not inspect.isabstract(altarica::Expression)


def test_altarica::expression_constructor_exists():
    assert callable(altarica::Expression.__init__)


def test_altarica::expression_constructor_args():
    sig = inspect.signature(altarica::Expression.__init__)
    params = list(sig.parameters.keys())



def test_altarica::flowdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::FlowDeclaration)


def test_altarica::flowdeclaration_constructor_exists():
    assert callable(altarica::FlowDeclaration.__init__)


def test_altarica::flowdeclaration_constructor_args():
    sig = inspect.signature(altarica::FlowDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_altarica::flowdeclaration_has_kind():
    assert hasattr(altarica::FlowDeclaration, "kind")
    descriptor = None
    for klass in altarica::FlowDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_altarica::flowspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::FlowSpecification)


def test_altarica::flowspecification_constructor_exists():
    assert callable(altarica::FlowSpecification.__init__)


def test_altarica::flowspecification_constructor_args():
    sig = inspect.signature(altarica::FlowSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::externaldirective_is_not_abstract():
    assert not inspect.isabstract(altarica::ExternalDirective)


def test_altarica::externaldirective_constructor_exists():
    assert callable(altarica::ExternalDirective.__init__)


def test_altarica::externaldirective_constructor_args():
    sig = inspect.signature(altarica::ExternalDirective.__init__)
    params = list(sig.parameters.keys())
    assert "directive" in params, "Missing parameter 'directive'"

def test_altarica::externaldirective_has_directive():
    assert hasattr(altarica::ExternalDirective, "directive")
    descriptor = None
    for klass in altarica::ExternalDirective.__mro__:
        if "directive" in klass.__dict__:
            descriptor = klass.__dict__["directive"]
            break
    assert isinstance(descriptor, property)



def test_altarica::externalspecification_is_not_abstract():
    assert not inspect.isabstract(altarica::ExternalSpecification)


def test_altarica::externalspecification_constructor_exists():
    assert callable(altarica::ExternalSpecification.__init__)


def test_altarica::externalspecification_constructor_args():
    sig = inspect.signature(altarica::ExternalSpecification.__init__)
    params = list(sig.parameters.keys())



def test_altarica::system_is_not_abstract():
    assert not inspect.isabstract(altarica::System)


def test_altarica::system_constructor_exists():
    assert callable(altarica::System.__init__)


def test_altarica::system_constructor_args():
    sig = inspect.signature(altarica::System.__init__)
    params = list(sig.parameters.keys())



def test_nonnavigablevariable_is_not_abstract():
    assert not inspect.isabstract(NonNavigableVariable)


def test_nonnavigablevariable_constructor_exists():
    assert callable(NonNavigableVariable.__init__)


def test_nonnavigablevariable_constructor_args():
    sig = inspect.signature(NonNavigableVariable.__init__)
    params = list(sig.parameters.keys())



def test_altarica::state_is_not_abstract():
    assert not inspect.isabstract(altarica::State)


def test_altarica::state_constructor_exists():
    assert callable(altarica::State.__init__)


def test_altarica::state_constructor_args():
    sig = inspect.signature(altarica::State.__init__)
    params = list(sig.parameters.keys())



def test_altarica::flow_is_not_abstract():
    assert not inspect.isabstract(altarica::Flow)


def test_altarica::flow_constructor_exists():
    assert callable(altarica::Flow.__init__)


def test_altarica::flow_constructor_args():
    sig = inspect.signature(altarica::Flow.__init__)
    params = list(sig.parameters.keys())



def test_altarica::literal_is_not_abstract():
    assert not inspect.isabstract(altarica::Literal)


def test_altarica::literal_constructor_exists():
    assert callable(altarica::Literal.__init__)


def test_altarica::literal_constructor_args():
    sig = inspect.signature(altarica::Literal.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractdefinitionconstant_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractDefinitionConstant)


def test_altarica::abstractdefinitionconstant_constructor_exists():
    assert callable(altarica::AbstractDefinitionConstant.__init__)


def test_altarica::abstractdefinitionconstant_constructor_args():
    sig = inspect.signature(altarica::AbstractDefinitionConstant.__init__)
    params = list(sig.parameters.keys())



def test_altarica::constant_is_not_abstract():
    assert not inspect.isabstract(altarica::Constant)


def test_altarica::constant_constructor_exists():
    assert callable(altarica::Constant.__init__)


def test_altarica::constant_constructor_args():
    sig = inspect.signature(altarica::Constant.__init__)
    params = list(sig.parameters.keys())



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_altarica::node_is_not_abstract():
    assert not inspect.isabstract(altarica::Node)


def test_altarica::node_constructor_exists():
    assert callable(altarica::Node.__init__)


def test_altarica::node_constructor_args():
    sig = inspect.signature(altarica::Node.__init__)
    params = list(sig.parameters.keys())
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::node_has_isMain():
    assert hasattr(altarica::Node, "isMain")
    descriptor = None
    for klass in altarica::Node.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)

def test_altarica::node_has_name():
    assert hasattr(altarica::Node, "name")
    descriptor = None
    for klass in altarica::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::domain_is_not_abstract():
    assert not inspect.isabstract(altarica::Domain)


def test_altarica::domain_constructor_exists():
    assert callable(altarica::Domain.__init__)


def test_altarica::domain_constructor_args():
    sig = inspect.signature(altarica::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_altarica::domain_has_name():
    assert hasattr(altarica::Domain, "name")
    descriptor = None
    for klass in altarica::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_altarica::constantdefinition_is_not_abstract():
    assert not inspect.isabstract(altarica::ConstantDefinition)


def test_altarica::constantdefinition_constructor_exists():
    assert callable(altarica::ConstantDefinition.__init__)


def test_altarica::constantdefinition_constructor_args():
    sig = inspect.signature(altarica::ConstantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_altarica::abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(altarica::AbstractDeclaration)


def test_altarica::abstractdeclaration_constructor_exists():
    assert callable(altarica::AbstractDeclaration.__init__)


def test_altarica::abstractdeclaration_constructor_args():
    sig = inspect.signature(altarica::AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nestedqualifiedvariableref_is_not_abstract():
    assert not inspect.isabstract(altarica::NestedQualifiedVariableRef)


def test_altarica::nestedqualifiedvariableref_constructor_exists():
    assert callable(altarica::NestedQualifiedVariableRef.__init__)


def test_altarica::nestedqualifiedvariableref_constructor_args():
    sig = inspect.signature(altarica::NestedQualifiedVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_eventref_is_not_abstract():
    assert not inspect.isabstract(EventRef)


def test_eventref_constructor_exists():
    assert callable(EventRef.__init__)


def test_eventref_constructor_args():
    sig = inspect.signature(EventRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::nestedqualifiedeventref_is_not_abstract():
    assert not inspect.isabstract(altarica::NestedQualifiedEventRef)


def test_altarica::nestedqualifiedeventref_constructor_exists():
    assert callable(altarica::NestedQualifiedEventRef.__init__)


def test_altarica::nestedqualifiedeventref_constructor_args():
    sig = inspect.signature(altarica::NestedQualifiedEventRef.__init__)
    params = list(sig.parameters.keys())



def test_altarica::strictupper_is_not_abstract():
    assert not inspect.isabstract(altarica::StrictUpper)


def test_altarica::strictupper_constructor_exists():
    assert callable(altarica::StrictUpper.__init__)


def test_altarica::strictupper_constructor_args():
    sig = inspect.signature(altarica::StrictUpper.__init__)
    params = list(sig.parameters.keys())



def test_altarica::lower_is_not_abstract():
    assert not inspect.isabstract(altarica::Lower)


def test_altarica::lower_constructor_exists():
    assert callable(altarica::Lower.__init__)


def test_altarica::lower_constructor_args():
    sig = inspect.signature(altarica::Lower.__init__)
    params = list(sig.parameters.keys())



def test_altarica::strictlower_is_not_abstract():
    assert not inspect.isabstract(altarica::StrictLower)


def test_altarica::strictlower_constructor_exists():
    assert callable(altarica::StrictLower.__init__)


def test_altarica::strictlower_constructor_args():
    sig = inspect.signature(altarica::StrictLower.__init__)
    params = list(sig.parameters.keys())

def test_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowKind"

def test_primitivetypekind_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeKind is not None

def test_primitivetypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeKind]
    expected_literals = [
        "INTEGER",
        "BOOLEAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeKind"


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
Expression_strategy = st.builds(
    Expression,
)
altarica::EBoolean_strategy = st.builds(
    altarica::EBoolean,
    value=
        safe_text
)
altarica::Equal_strategy = st.builds(
    altarica::Equal,
)
altarica::EString_strategy = st.builds(
    altarica::EString,
    value=
        safe_text
)
altarica::Division_strategy = st.builds(
    altarica::Division,
)
altarica::Imply_strategy = st.builds(
    altarica::Imply,
)
altarica::EInteger_strategy = st.builds(
    altarica::EInteger,
    value=
        st.integers()
)
altarica::Minus_strategy = st.builds(
    altarica::Minus,
)
altarica::Multiplication_strategy = st.builds(
    altarica::Multiplication,
)
altarica::Addition_strategy = st.builds(
    altarica::Addition,
)
altarica::NotEqual_strategy = st.builds(
    altarica::NotEqual,
)
altarica::Upper_strategy = st.builds(
    altarica::Upper,
)
altarica::VariableRef_strategy = st.builds(
    altarica::VariableRef,
)
altarica::NavigableVariable_strategy = st.builds(
    altarica::NavigableVariable,
    name=
        safe_text
)
altarica::Or_strategy = st.builds(
    altarica::Or,
)
altarica::And_strategy = st.builds(
    altarica::And,
)
altarica::CaseExpression_strategy = st.builds(
    altarica::CaseExpression,
)
AbstractBooleanExpression_strategy = st.builds(
    AbstractBooleanExpression,
)
AbstractExpression_strategy = st.builds(
    AbstractExpression,
)
altarica::Switch_strategy = st.builds(
    altarica::Switch,
)
altarica::Transition_strategy = st.builds(
    altarica::Transition,
)
altarica::EventRef_strategy = st.builds(
    altarica::EventRef,
)
altarica::Cardinality_strategy = st.builds(
    altarica::Cardinality,
)
altarica::VectorParameter_strategy = st.builds(
    altarica::VectorParameter,
    isRequired=
        st.booleans()
)
altarica::Vector_strategy = st.builds(
    altarica::Vector,
)
altarica::EObject_strategy = st.builds(
    altarica::EObject,
)
altarica::IfThenElse_strategy = st.builds(
    altarica::IfThenElse,
)
altarica::NodeInstanceDeclaration_strategy = st.builds(
    altarica::NodeInstanceDeclaration,
)
altarica::StateDeclaration_strategy = st.builds(
    altarica::StateDeclaration,
)
altarica::AbstractExpression_strategy = st.builds(
    altarica::AbstractExpression,
)
altarica::Priority_strategy = st.builds(
    altarica::Priority,
)
NavigableVariable_strategy = st.builds(
    NavigableVariable,
)
altarica::NonNavigableVariable_strategy = st.builds(
    altarica::NonNavigableVariable,
)
altarica::Event_strategy = st.builds(
    altarica::Event,
)
altarica::EventDeclaration_strategy = st.builds(
    altarica::EventDeclaration,
)
altarica::AbstractTypeRef_strategy = st.builds(
    altarica::AbstractTypeRef,
)
altarica::AbstractBooleanExpression_strategy = st.builds(
    altarica::AbstractBooleanExpression,
)
altarica::Assert_strategy = st.builds(
    altarica::Assert,
)
altarica::NodeInstance_strategy = st.builds(
    altarica::NodeInstance,
)
altarica::Affectation_strategy = st.builds(
    altarica::Affectation,
)
altarica::InitStatement_strategy = st.builds(
    altarica::InitStatement,
)
AbstractSpecification_strategy = st.builds(
    AbstractSpecification,
)
altarica::StateSpecification_strategy = st.builds(
    altarica::StateSpecification,
)
altarica::VectorSpecification_strategy = st.builds(
    altarica::VectorSpecification,
)
altarica::EventSpecification_strategy = st.builds(
    altarica::EventSpecification,
)
altarica::NodeInstanceSpecification_strategy = st.builds(
    altarica::NodeInstanceSpecification,
)
altarica::AssertSpecification_strategy = st.builds(
    altarica::AssertSpecification,
)
altarica::TransitionSpecification_strategy = st.builds(
    altarica::TransitionSpecification,
)
altarica::InitSpecification_strategy = st.builds(
    altarica::InitSpecification,
)
altarica::VariableAttribute_strategy = st.builds(
    altarica::VariableAttribute,
    name=
        safe_text
)
altarica::AbstractSpecification_strategy = st.builds(
    altarica::AbstractSpecification,
)
AbstractDomain_strategy = st.builds(
    AbstractDomain,
)
altarica::PrimitiveType_strategy = st.builds(
    altarica::PrimitiveType,
    name=
        safe_text
)
altarica::Enumeration_strategy = st.builds(
    altarica::Enumeration,
)
altarica::Range_strategy = st.builds(
    altarica::Range,
)
AbstractTypeRef_strategy = st.builds(
    AbstractTypeRef,
)
altarica::DomainRef_strategy = st.builds(
    altarica::DomainRef,
)
altarica::AbstractDomain_strategy = st.builds(
    altarica::AbstractDomain,
)
AbstractDefinitionConstant_strategy = st.builds(
    AbstractDefinitionConstant,
)
altarica::DomainConstant_strategy = st.builds(
    altarica::DomainConstant,
)
altarica::ExpressionConstant_strategy = st.builds(
    altarica::ExpressionConstant,
)
altarica::Expression_strategy = st.builds(
    altarica::Expression,
)
altarica::FlowDeclaration_strategy = st.builds(
    altarica::FlowDeclaration,
    kind=
        safe_text
)
altarica::FlowSpecification_strategy = st.builds(
    altarica::FlowSpecification,
)
altarica::ExternalDirective_strategy = st.builds(
    altarica::ExternalDirective,
    directive=
        safe_text
)
altarica::ExternalSpecification_strategy = st.builds(
    altarica::ExternalSpecification,
)
altarica::System_strategy = st.builds(
    altarica::System,
)
NonNavigableVariable_strategy = st.builds(
    NonNavigableVariable,
)
altarica::State_strategy = st.builds(
    altarica::State,
)
altarica::Flow_strategy = st.builds(
    altarica::Flow,
)
altarica::Literal_strategy = st.builds(
    altarica::Literal,
)
altarica::AbstractDefinitionConstant_strategy = st.builds(
    altarica::AbstractDefinitionConstant,
)
altarica::Constant_strategy = st.builds(
    altarica::Constant,
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
altarica::Node_strategy = st.builds(
    altarica::Node,
    isMain=
        st.booleans(),
    name=
        safe_text
)
altarica::Domain_strategy = st.builds(
    altarica::Domain,
    name=
        safe_text
)
altarica::ConstantDefinition_strategy = st.builds(
    altarica::ConstantDefinition,
)
altarica::AbstractDeclaration_strategy = st.builds(
    altarica::AbstractDeclaration,
)
VariableRef_strategy = st.builds(
    VariableRef,
)
altarica::NestedQualifiedVariableRef_strategy = st.builds(
    altarica::NestedQualifiedVariableRef,
)
EventRef_strategy = st.builds(
    EventRef,
)
altarica::NestedQualifiedEventRef_strategy = st.builds(
    altarica::NestedQualifiedEventRef,
)
altarica::StrictUpper_strategy = st.builds(
    altarica::StrictUpper,
)
altarica::Lower_strategy = st.builds(
    altarica::Lower,
)
altarica::StrictLower_strategy = st.builds(
    altarica::StrictLower,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=altarica::EBoolean_strategy)
@settings(max_examples=50)
def test_altarica::eboolean_instantiation(instance):
    assert isinstance(instance, altarica::EBoolean)

@given(instance=altarica::EBoolean_strategy)
def test_altarica::eboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=altarica::EBoolean_strategy)
def test_altarica::eboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Equal_strategy)
@settings(max_examples=50)
def test_altarica::equal_instantiation(instance):
    assert isinstance(instance, altarica::Equal)

@given(instance=altarica::EString_strategy)
@settings(max_examples=50)
def test_altarica::estring_instantiation(instance):
    assert isinstance(instance, altarica::EString)

@given(instance=altarica::EString_strategy)
def test_altarica::estring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=altarica::EString_strategy)
def test_altarica::estring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Division_strategy)
@settings(max_examples=50)
def test_altarica::division_instantiation(instance):
    assert isinstance(instance, altarica::Division)

@given(instance=altarica::Imply_strategy)
@settings(max_examples=50)
def test_altarica::imply_instantiation(instance):
    assert isinstance(instance, altarica::Imply)

@given(instance=altarica::EInteger_strategy)
@settings(max_examples=50)
def test_altarica::einteger_instantiation(instance):
    assert isinstance(instance, altarica::EInteger)

@given(instance=altarica::EInteger_strategy)
def test_altarica::einteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=altarica::EInteger_strategy)
def test_altarica::einteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=altarica::Minus_strategy)
@settings(max_examples=50)
def test_altarica::minus_instantiation(instance):
    assert isinstance(instance, altarica::Minus)

@given(instance=altarica::Multiplication_strategy)
@settings(max_examples=50)
def test_altarica::multiplication_instantiation(instance):
    assert isinstance(instance, altarica::Multiplication)

@given(instance=altarica::Addition_strategy)
@settings(max_examples=50)
def test_altarica::addition_instantiation(instance):
    assert isinstance(instance, altarica::Addition)

@given(instance=altarica::NotEqual_strategy)
@settings(max_examples=50)
def test_altarica::notequal_instantiation(instance):
    assert isinstance(instance, altarica::NotEqual)

@given(instance=altarica::Upper_strategy)
@settings(max_examples=50)
def test_altarica::upper_instantiation(instance):
    assert isinstance(instance, altarica::Upper)

@given(instance=altarica::VariableRef_strategy)
@settings(max_examples=50)
def test_altarica::variableref_instantiation(instance):
    assert isinstance(instance, altarica::VariableRef)

@given(instance=altarica::NavigableVariable_strategy)
@settings(max_examples=50)
def test_altarica::navigablevariable_instantiation(instance):
    assert isinstance(instance, altarica::NavigableVariable)

@given(instance=altarica::NavigableVariable_strategy)
def test_altarica::navigablevariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::NavigableVariable_strategy)
def test_altarica::navigablevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::Or_strategy)
@settings(max_examples=50)
def test_altarica::or_instantiation(instance):
    assert isinstance(instance, altarica::Or)

@given(instance=altarica::And_strategy)
@settings(max_examples=50)
def test_altarica::and_instantiation(instance):
    assert isinstance(instance, altarica::And)

@given(instance=altarica::CaseExpression_strategy)
@settings(max_examples=50)
def test_altarica::caseexpression_instantiation(instance):
    assert isinstance(instance, altarica::CaseExpression)

@given(instance=AbstractBooleanExpression_strategy)
@settings(max_examples=50)
def test_abstractbooleanexpression_instantiation(instance):
    assert isinstance(instance, AbstractBooleanExpression)

@given(instance=AbstractExpression_strategy)
@settings(max_examples=50)
def test_abstractexpression_instantiation(instance):
    assert isinstance(instance, AbstractExpression)

@given(instance=altarica::Switch_strategy)
@settings(max_examples=50)
def test_altarica::switch_instantiation(instance):
    assert isinstance(instance, altarica::Switch)

@given(instance=altarica::Transition_strategy)
@settings(max_examples=50)
def test_altarica::transition_instantiation(instance):
    assert isinstance(instance, altarica::Transition)

@given(instance=altarica::EventRef_strategy)
@settings(max_examples=50)
def test_altarica::eventref_instantiation(instance):
    assert isinstance(instance, altarica::EventRef)

@given(instance=altarica::Cardinality_strategy)
@settings(max_examples=50)
def test_altarica::cardinality_instantiation(instance):
    assert isinstance(instance, altarica::Cardinality)

@given(instance=altarica::VectorParameter_strategy)
@settings(max_examples=50)
def test_altarica::vectorparameter_instantiation(instance):
    assert isinstance(instance, altarica::VectorParameter)

@given(instance=altarica::VectorParameter_strategy)
def test_altarica::vectorparameter_isRequired_type(instance):
    assert isinstance(instance.isRequired, bool)


@given(instance=altarica::VectorParameter_strategy)
def test_altarica::vectorparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=altarica::Vector_strategy)
@settings(max_examples=50)
def test_altarica::vector_instantiation(instance):
    assert isinstance(instance, altarica::Vector)

@given(instance=altarica::EObject_strategy)
@settings(max_examples=50)
def test_altarica::eobject_instantiation(instance):
    assert isinstance(instance, altarica::EObject)

@given(instance=altarica::IfThenElse_strategy)
@settings(max_examples=50)
def test_altarica::ifthenelse_instantiation(instance):
    assert isinstance(instance, altarica::IfThenElse)

@given(instance=altarica::NodeInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::nodeinstancedeclaration_instantiation(instance):
    assert isinstance(instance, altarica::NodeInstanceDeclaration)

@given(instance=altarica::StateDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::statedeclaration_instantiation(instance):
    assert isinstance(instance, altarica::StateDeclaration)

@given(instance=altarica::AbstractExpression_strategy)
@settings(max_examples=50)
def test_altarica::abstractexpression_instantiation(instance):
    assert isinstance(instance, altarica::AbstractExpression)

@given(instance=altarica::Priority_strategy)
@settings(max_examples=50)
def test_altarica::priority_instantiation(instance):
    assert isinstance(instance, altarica::Priority)

@given(instance=NavigableVariable_strategy)
@settings(max_examples=50)
def test_navigablevariable_instantiation(instance):
    assert isinstance(instance, NavigableVariable)

@given(instance=altarica::NonNavigableVariable_strategy)
@settings(max_examples=50)
def test_altarica::nonnavigablevariable_instantiation(instance):
    assert isinstance(instance, altarica::NonNavigableVariable)

@given(instance=altarica::Event_strategy)
@settings(max_examples=50)
def test_altarica::event_instantiation(instance):
    assert isinstance(instance, altarica::Event)

@given(instance=altarica::EventDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::eventdeclaration_instantiation(instance):
    assert isinstance(instance, altarica::EventDeclaration)

@given(instance=altarica::AbstractTypeRef_strategy)
@settings(max_examples=50)
def test_altarica::abstracttyperef_instantiation(instance):
    assert isinstance(instance, altarica::AbstractTypeRef)

@given(instance=altarica::AbstractBooleanExpression_strategy)
@settings(max_examples=50)
def test_altarica::abstractbooleanexpression_instantiation(instance):
    assert isinstance(instance, altarica::AbstractBooleanExpression)

@given(instance=altarica::Assert_strategy)
@settings(max_examples=50)
def test_altarica::assert_instantiation(instance):
    assert isinstance(instance, altarica::Assert)

@given(instance=altarica::NodeInstance_strategy)
@settings(max_examples=50)
def test_altarica::nodeinstance_instantiation(instance):
    assert isinstance(instance, altarica::NodeInstance)

@given(instance=altarica::Affectation_strategy)
@settings(max_examples=50)
def test_altarica::affectation_instantiation(instance):
    assert isinstance(instance, altarica::Affectation)

@given(instance=altarica::InitStatement_strategy)
@settings(max_examples=50)
def test_altarica::initstatement_instantiation(instance):
    assert isinstance(instance, altarica::InitStatement)

@given(instance=AbstractSpecification_strategy)
@settings(max_examples=50)
def test_abstractspecification_instantiation(instance):
    assert isinstance(instance, AbstractSpecification)

@given(instance=altarica::StateSpecification_strategy)
@settings(max_examples=50)
def test_altarica::statespecification_instantiation(instance):
    assert isinstance(instance, altarica::StateSpecification)

@given(instance=altarica::VectorSpecification_strategy)
@settings(max_examples=50)
def test_altarica::vectorspecification_instantiation(instance):
    assert isinstance(instance, altarica::VectorSpecification)

@given(instance=altarica::EventSpecification_strategy)
@settings(max_examples=50)
def test_altarica::eventspecification_instantiation(instance):
    assert isinstance(instance, altarica::EventSpecification)

@given(instance=altarica::NodeInstanceSpecification_strategy)
@settings(max_examples=50)
def test_altarica::nodeinstancespecification_instantiation(instance):
    assert isinstance(instance, altarica::NodeInstanceSpecification)

@given(instance=altarica::AssertSpecification_strategy)
@settings(max_examples=50)
def test_altarica::assertspecification_instantiation(instance):
    assert isinstance(instance, altarica::AssertSpecification)

@given(instance=altarica::TransitionSpecification_strategy)
@settings(max_examples=50)
def test_altarica::transitionspecification_instantiation(instance):
    assert isinstance(instance, altarica::TransitionSpecification)

@given(instance=altarica::InitSpecification_strategy)
@settings(max_examples=50)
def test_altarica::initspecification_instantiation(instance):
    assert isinstance(instance, altarica::InitSpecification)

@given(instance=altarica::VariableAttribute_strategy)
@settings(max_examples=50)
def test_altarica::variableattribute_instantiation(instance):
    assert isinstance(instance, altarica::VariableAttribute)

@given(instance=altarica::VariableAttribute_strategy)
def test_altarica::variableattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::VariableAttribute_strategy)
def test_altarica::variableattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::AbstractSpecification_strategy)
@settings(max_examples=50)
def test_altarica::abstractspecification_instantiation(instance):
    assert isinstance(instance, altarica::AbstractSpecification)

@given(instance=AbstractDomain_strategy)
@settings(max_examples=50)
def test_abstractdomain_instantiation(instance):
    assert isinstance(instance, AbstractDomain)

@given(instance=altarica::PrimitiveType_strategy)
@settings(max_examples=50)
def test_altarica::primitivetype_instantiation(instance):
    assert isinstance(instance, altarica::PrimitiveType)

@given(instance=altarica::PrimitiveType_strategy)
def test_altarica::primitivetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::PrimitiveType_strategy)
def test_altarica::primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::Enumeration_strategy)
@settings(max_examples=50)
def test_altarica::enumeration_instantiation(instance):
    assert isinstance(instance, altarica::Enumeration)

@given(instance=altarica::Range_strategy)
@settings(max_examples=50)
def test_altarica::range_instantiation(instance):
    assert isinstance(instance, altarica::Range)

@given(instance=AbstractTypeRef_strategy)
@settings(max_examples=50)
def test_abstracttyperef_instantiation(instance):
    assert isinstance(instance, AbstractTypeRef)

@given(instance=altarica::DomainRef_strategy)
@settings(max_examples=50)
def test_altarica::domainref_instantiation(instance):
    assert isinstance(instance, altarica::DomainRef)

@given(instance=altarica::AbstractDomain_strategy)
@settings(max_examples=50)
def test_altarica::abstractdomain_instantiation(instance):
    assert isinstance(instance, altarica::AbstractDomain)

@given(instance=AbstractDefinitionConstant_strategy)
@settings(max_examples=50)
def test_abstractdefinitionconstant_instantiation(instance):
    assert isinstance(instance, AbstractDefinitionConstant)

@given(instance=altarica::DomainConstant_strategy)
@settings(max_examples=50)
def test_altarica::domainconstant_instantiation(instance):
    assert isinstance(instance, altarica::DomainConstant)

@given(instance=altarica::ExpressionConstant_strategy)
@settings(max_examples=50)
def test_altarica::expressionconstant_instantiation(instance):
    assert isinstance(instance, altarica::ExpressionConstant)

@given(instance=altarica::Expression_strategy)
@settings(max_examples=50)
def test_altarica::expression_instantiation(instance):
    assert isinstance(instance, altarica::Expression)

@given(instance=altarica::FlowDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::flowdeclaration_instantiation(instance):
    assert isinstance(instance, altarica::FlowDeclaration)

@given(instance=altarica::FlowDeclaration_strategy)
def test_altarica::flowdeclaration_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=altarica::FlowDeclaration_strategy)
def test_altarica::flowdeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=altarica::FlowSpecification_strategy)
@settings(max_examples=50)
def test_altarica::flowspecification_instantiation(instance):
    assert isinstance(instance, altarica::FlowSpecification)

@given(instance=altarica::ExternalDirective_strategy)
@settings(max_examples=50)
def test_altarica::externaldirective_instantiation(instance):
    assert isinstance(instance, altarica::ExternalDirective)

@given(instance=altarica::ExternalDirective_strategy)
def test_altarica::externaldirective_directive_type(instance):
    assert isinstance(instance.directive, str)


@given(instance=altarica::ExternalDirective_strategy)
def test_altarica::externaldirective_directive_setter(instance):
    original = instance.directive
    instance.directive = original
    assert instance.directive == original

@given(instance=altarica::ExternalSpecification_strategy)
@settings(max_examples=50)
def test_altarica::externalspecification_instantiation(instance):
    assert isinstance(instance, altarica::ExternalSpecification)

@given(instance=altarica::System_strategy)
@settings(max_examples=50)
def test_altarica::system_instantiation(instance):
    assert isinstance(instance, altarica::System)

@given(instance=NonNavigableVariable_strategy)
@settings(max_examples=50)
def test_nonnavigablevariable_instantiation(instance):
    assert isinstance(instance, NonNavigableVariable)

@given(instance=altarica::State_strategy)
@settings(max_examples=50)
def test_altarica::state_instantiation(instance):
    assert isinstance(instance, altarica::State)

@given(instance=altarica::Flow_strategy)
@settings(max_examples=50)
def test_altarica::flow_instantiation(instance):
    assert isinstance(instance, altarica::Flow)

@given(instance=altarica::Literal_strategy)
@settings(max_examples=50)
def test_altarica::literal_instantiation(instance):
    assert isinstance(instance, altarica::Literal)

@given(instance=altarica::AbstractDefinitionConstant_strategy)
@settings(max_examples=50)
def test_altarica::abstractdefinitionconstant_instantiation(instance):
    assert isinstance(instance, altarica::AbstractDefinitionConstant)

@given(instance=altarica::Constant_strategy)
@settings(max_examples=50)
def test_altarica::constant_instantiation(instance):
    assert isinstance(instance, altarica::Constant)

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=altarica::Node_strategy)
@settings(max_examples=50)
def test_altarica::node_instantiation(instance):
    assert isinstance(instance, altarica::Node)

@given(instance=altarica::Node_strategy)
def test_altarica::node_isMain_type(instance):
    assert isinstance(instance.isMain, bool)


@given(instance=altarica::Node_strategy)
def test_altarica::node_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original

@given(instance=altarica::Node_strategy)
def test_altarica::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::Node_strategy)
def test_altarica::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::Domain_strategy)
@settings(max_examples=50)
def test_altarica::domain_instantiation(instance):
    assert isinstance(instance, altarica::Domain)

@given(instance=altarica::Domain_strategy)
def test_altarica::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=altarica::Domain_strategy)
def test_altarica::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=altarica::ConstantDefinition_strategy)
@settings(max_examples=50)
def test_altarica::constantdefinition_instantiation(instance):
    assert isinstance(instance, altarica::ConstantDefinition)

@given(instance=altarica::AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_altarica::abstractdeclaration_instantiation(instance):
    assert isinstance(instance, altarica::AbstractDeclaration)

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=altarica::NestedQualifiedVariableRef_strategy)
@settings(max_examples=50)
def test_altarica::nestedqualifiedvariableref_instantiation(instance):
    assert isinstance(instance, altarica::NestedQualifiedVariableRef)

@given(instance=EventRef_strategy)
@settings(max_examples=50)
def test_eventref_instantiation(instance):
    assert isinstance(instance, EventRef)

@given(instance=altarica::NestedQualifiedEventRef_strategy)
@settings(max_examples=50)
def test_altarica::nestedqualifiedeventref_instantiation(instance):
    assert isinstance(instance, altarica::NestedQualifiedEventRef)

@given(instance=altarica::StrictUpper_strategy)
@settings(max_examples=50)
def test_altarica::strictupper_instantiation(instance):
    assert isinstance(instance, altarica::StrictUpper)

@given(instance=altarica::Lower_strategy)
@settings(max_examples=50)
def test_altarica::lower_instantiation(instance):
    assert isinstance(instance, altarica::Lower)

@given(instance=altarica::StrictLower_strategy)
@settings(max_examples=50)
def test_altarica::strictlower_instantiation(instance):
    assert isinstance(instance, altarica::StrictLower)
