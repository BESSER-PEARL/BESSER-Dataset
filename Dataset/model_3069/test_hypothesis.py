import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dom::PresentableFeature,
    dom::WhenClause,
    LiteralValue,
    dom::IntegerLiteralValue,
    dom::EmptyLiteralValue,
    dom::RealLiteralValue,
    dom::NullLiteralValue,
    dom::BooleanLiteralValue,
    dom::AltWhenClause,
    dom::StringLiteralValue,
    dom::QueryParameterReference,
    JoinEntity,
    FromRange,
    dom::InClass,
    dom::InCollection,
    dom::Dependant,
    Dependant,
    DaoOperation,
    dom::SimpleType,
    IDocumentable,
    dom::Operation,
    ReferenceableByXmadslVariable,
    dom::Property,
    Type,
    ModelElement,
    dom::Service,
    dom::ComplexType,
    dom::FromClass,
    Expression,
    dom::SubQuery,
    dom::LikeExpression,
    dom::AliasedExpression,
    dom::BinaryExpression,
    dom::CollectionFunction,
    dom::NotExpression,
    dom::CastFunction,
    dom::QueryParameterValue,
    dom::CaseExpression,
    dom::UnaryExpression,
    dom::ParenthesizedExpression,
    dom::TrimFunction,
    dom::MemberOfExpression,
    dom::FunctionCall,
    dom::InExpression,
    dom::AggregateFunction,
    dom::LiteralValue,
    dom::QuantifiedExpression,
    dom::BetweenExpression,
    dom::JoinEntity,
    dom::InCollectionElements,
    dom::PropertyValue,
    dom::PropertyAssignment,
    SelectStatement,
    dom::SelectClass,
    dom::SelectObject,
    dom::SelectProperties,
    dom::SortOrderElement,
    dom::Join,
    dom::FromRange,
    dom::CallOutputParameter,
    dom::CallInputParameter,
    QlStatement,
    dom::SelectStatement,
    dom::UpdateStatement,
    dom::InsertStatement,
    dom::DeleteStatement,
    dom::CallableStatement,
    dom::Function,
    dom::ApplicationSession,
    DaoFeature,
    dom::SqlType,
    dom::OneToOne,
    dom::ManyToOne,
    dom::Column,
    dom::DataBaseConstraint,
    dom::QlStatement,
    dom::QueryParameter,
    dom::ManyToMany,
    dom::OneToMany,
    dom::QueryOperation,
    dom::DaoFeature,
    dom::AttributeSortOrder,
    dom::ValidatorReference,
    dom::Constraint,
    dom::BoolLiteral,
    ExpressionFlag,
    dom::AvailableFlag,
    dom::ReadOnlyFlag,
    dom::RequiredFlag,
    dom::EqualityExpr,
    AttributeFlag,
    dom::TransientFlag,
    dom::DerivedFlag,
    dom::ExpressionFlag,
    AttributeProperty,
    dom::AttributeTextProperty,
    dom::AttributeValidationProperty,
    dom::AttributeFlag,
    dom::IncrementerReference,
    dom::DataTypeAndTypeParameter,
    dom::PropertyMapping,
    dom::ConditionsBlock,
    dom::AttributeGroup,
    PresentableFeature,
    dom::FeatureReference,
    ComplexType,
    dom::Entity,
    dom::ValueObject,
    dom::Mapper,
    dom::AttributeProperty,
    dom::DataView,
    dom::Type,
    QueryParameterReference,
    dom::IElementWithNoName,
    dom::Attribute,
    QueryParameter,
    dom::Parameter,
    dom::Expression,
    dom::DaoOperation,
    dom::Dao,
    dom::DelegateOperation,
    DataBaseConstraintType,
    CrudOperationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dom::presentablefeature_is_not_abstract():
    assert not inspect.isabstract(dom::PresentableFeature)


def test_dom::presentablefeature_constructor_exists():
    assert callable(dom::PresentableFeature.__init__)


def test_dom::presentablefeature_constructor_args():
    sig = inspect.signature(dom::PresentableFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::presentablefeature_has_name():
    assert hasattr(dom::PresentableFeature, "name")
    descriptor = None
    for klass in dom::PresentableFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::whenclause_is_not_abstract():
    assert not inspect.isabstract(dom::WhenClause)


def test_dom::whenclause_constructor_exists():
    assert callable(dom::WhenClause.__init__)


def test_dom::whenclause_constructor_args():
    sig = inspect.signature(dom::WhenClause.__init__)
    params = list(sig.parameters.keys())



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::integerliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::IntegerLiteralValue)


def test_dom::integerliteralvalue_constructor_exists():
    assert callable(dom::IntegerLiteralValue.__init__)


def test_dom::integerliteralvalue_constructor_args():
    sig = inspect.signature(dom::IntegerLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom::integerliteralvalue_has_value():
    assert hasattr(dom::IntegerLiteralValue, "value")
    descriptor = None
    for klass in dom::IntegerLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom::emptyliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::EmptyLiteralValue)


def test_dom::emptyliteralvalue_constructor_exists():
    assert callable(dom::EmptyLiteralValue.__init__)


def test_dom::emptyliteralvalue_constructor_args():
    sig = inspect.signature(dom::EmptyLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::realliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::RealLiteralValue)


def test_dom::realliteralvalue_constructor_exists():
    assert callable(dom::RealLiteralValue.__init__)


def test_dom::realliteralvalue_constructor_args():
    sig = inspect.signature(dom::RealLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom::realliteralvalue_has_value():
    assert hasattr(dom::RealLiteralValue, "value")
    descriptor = None
    for klass in dom::RealLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom::nullliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::NullLiteralValue)


def test_dom::nullliteralvalue_constructor_exists():
    assert callable(dom::NullLiteralValue.__init__)


def test_dom::nullliteralvalue_constructor_args():
    sig = inspect.signature(dom::NullLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::booleanliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::BooleanLiteralValue)


def test_dom::booleanliteralvalue_constructor_exists():
    assert callable(dom::BooleanLiteralValue.__init__)


def test_dom::booleanliteralvalue_constructor_args():
    sig = inspect.signature(dom::BooleanLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_dom::booleanliteralvalue_has_isTrue():
    assert hasattr(dom::BooleanLiteralValue, "isTrue")
    descriptor = None
    for klass in dom::BooleanLiteralValue.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_dom::altwhenclause_is_not_abstract():
    assert not inspect.isabstract(dom::AltWhenClause)


def test_dom::altwhenclause_constructor_exists():
    assert callable(dom::AltWhenClause.__init__)


def test_dom::altwhenclause_constructor_args():
    sig = inspect.signature(dom::AltWhenClause.__init__)
    params = list(sig.parameters.keys())



def test_dom::stringliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom::StringLiteralValue)


def test_dom::stringliteralvalue_constructor_exists():
    assert callable(dom::StringLiteralValue.__init__)


def test_dom::stringliteralvalue_constructor_args():
    sig = inspect.signature(dom::StringLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom::stringliteralvalue_has_value():
    assert hasattr(dom::StringLiteralValue, "value")
    descriptor = None
    for klass in dom::StringLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom::queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(dom::QueryParameterReference)


def test_dom::queryparameterreference_constructor_exists():
    assert callable(dom::QueryParameterReference.__init__)


def test_dom::queryparameterreference_constructor_args():
    sig = inspect.signature(dom::QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_joinentity_is_not_abstract():
    assert not inspect.isabstract(JoinEntity)


def test_joinentity_constructor_exists():
    assert callable(JoinEntity.__init__)


def test_joinentity_constructor_args():
    sig = inspect.signature(JoinEntity.__init__)
    params = list(sig.parameters.keys())



def test_fromrange_is_not_abstract():
    assert not inspect.isabstract(FromRange)


def test_fromrange_constructor_exists():
    assert callable(FromRange.__init__)


def test_fromrange_constructor_args():
    sig = inspect.signature(FromRange.__init__)
    params = list(sig.parameters.keys())



def test_dom::inclass_is_not_abstract():
    assert not inspect.isabstract(dom::InClass)


def test_dom::inclass_constructor_exists():
    assert callable(dom::InClass.__init__)


def test_dom::inclass_constructor_args():
    sig = inspect.signature(dom::InClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_dom::inclass_has_name():
    assert hasattr(dom::InClass, "name")
    descriptor = None
    for klass in dom::InClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::inclass_has_class_():
    assert hasattr(dom::InClass, "class_")
    descriptor = None
    for klass in dom::InClass.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dom::incollection_is_not_abstract():
    assert not inspect.isabstract(dom::InCollection)


def test_dom::incollection_constructor_exists():
    assert callable(dom::InCollection.__init__)


def test_dom::incollection_constructor_args():
    sig = inspect.signature(dom::InCollection.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "path" in params, "Missing parameter 'path'"

def test_dom::incollection_has_alias():
    assert hasattr(dom::InCollection, "alias")
    descriptor = None
    for klass in dom::InCollection.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_dom::incollection_has_path():
    assert hasattr(dom::InCollection, "path")
    descriptor = None
    for klass in dom::InCollection.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_dom::dependant_is_not_abstract():
    assert not inspect.isabstract(dom::Dependant)


def test_dom::dependant_constructor_exists():
    assert callable(dom::Dependant.__init__)


def test_dom::dependant_constructor_args():
    sig = inspect.signature(dom::Dependant.__init__)
    params = list(sig.parameters.keys())



def test_dependant_is_not_abstract():
    assert not inspect.isabstract(Dependant)


def test_dependant_constructor_exists():
    assert callable(Dependant.__init__)


def test_dependant_constructor_args():
    sig = inspect.signature(Dependant.__init__)
    params = list(sig.parameters.keys())



def test_daooperation_is_not_abstract():
    assert not inspect.isabstract(DaoOperation)


def test_daooperation_constructor_exists():
    assert callable(DaoOperation.__init__)


def test_daooperation_constructor_args():
    sig = inspect.signature(DaoOperation.__init__)
    params = list(sig.parameters.keys())



def test_dom::simpletype_is_not_abstract():
    assert not inspect.isabstract(dom::SimpleType)


def test_dom::simpletype_constructor_exists():
    assert callable(dom::SimpleType.__init__)


def test_dom::simpletype_constructor_args():
    sig = inspect.signature(dom::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_idocumentable_is_not_abstract():
    assert not inspect.isabstract(IDocumentable)


def test_idocumentable_constructor_exists():
    assert callable(IDocumentable.__init__)


def test_idocumentable_constructor_args():
    sig = inspect.signature(IDocumentable.__init__)
    params = list(sig.parameters.keys())



def test_dom::operation_is_not_abstract():
    assert not inspect.isabstract(dom::Operation)


def test_dom::operation_constructor_exists():
    assert callable(dom::Operation.__init__)


def test_dom::operation_constructor_args():
    sig = inspect.signature(dom::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_dom::operation_has_expression():
    assert hasattr(dom::Operation, "expression")
    descriptor = None
    for klass in dom::Operation.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_referenceablebyxmadslvariable_is_not_abstract():
    assert not inspect.isabstract(ReferenceableByXmadslVariable)


def test_referenceablebyxmadslvariable_constructor_exists():
    assert callable(ReferenceableByXmadslVariable.__init__)


def test_referenceablebyxmadslvariable_constructor_args():
    sig = inspect.signature(ReferenceableByXmadslVariable.__init__)
    params = list(sig.parameters.keys())



def test_dom::property_is_not_abstract():
    assert not inspect.isabstract(dom::Property)


def test_dom::property_constructor_exists():
    assert callable(dom::Property.__init__)


def test_dom::property_constructor_args():
    sig = inspect.signature(dom::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_dom::property_has_name():
    assert hasattr(dom::Property, "name")
    descriptor = None
    for klass in dom::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::property_has_defaultValue():
    assert hasattr(dom::Property, "defaultValue")
    descriptor = None
    for klass in dom::Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_dom::service_is_not_abstract():
    assert not inspect.isabstract(dom::Service)


def test_dom::service_constructor_exists():
    assert callable(dom::Service.__init__)


def test_dom::service_constructor_args():
    sig = inspect.signature(dom::Service.__init__)
    params = list(sig.parameters.keys())



def test_dom::complextype_is_not_abstract():
    assert not inspect.isabstract(dom::ComplexType)


def test_dom::complextype_constructor_exists():
    assert callable(dom::ComplexType.__init__)


def test_dom::complextype_constructor_args():
    sig = inspect.signature(dom::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_dom::fromclass_is_not_abstract():
    assert not inspect.isabstract(dom::FromClass)


def test_dom::fromclass_constructor_exists():
    assert callable(dom::FromClass.__init__)


def test_dom::fromclass_constructor_args():
    sig = inspect.signature(dom::FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "popertyFetch" in params, "Missing parameter 'popertyFetch'"

def test_dom::fromclass_has_popertyFetch():
    assert hasattr(dom::FromClass, "popertyFetch")
    descriptor = None
    for klass in dom::FromClass.__mro__:
        if "popertyFetch" in klass.__dict__:
            descriptor = klass.__dict__["popertyFetch"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::subquery_is_not_abstract():
    assert not inspect.isabstract(dom::SubQuery)


def test_dom::subquery_constructor_exists():
    assert callable(dom::SubQuery.__init__)


def test_dom::subquery_constructor_args():
    sig = inspect.signature(dom::SubQuery.__init__)
    params = list(sig.parameters.keys())



def test_dom::likeexpression_is_not_abstract():
    assert not inspect.isabstract(dom::LikeExpression)


def test_dom::likeexpression_constructor_exists():
    assert callable(dom::LikeExpression.__init__)


def test_dom::likeexpression_constructor_args():
    sig = inspect.signature(dom::LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_dom::likeexpression_has_operator():
    assert hasattr(dom::LikeExpression, "operator")
    descriptor = None
    for klass in dom::LikeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_dom::likeexpression_has_not_():
    assert hasattr(dom::LikeExpression, "not_")
    descriptor = None
    for klass in dom::LikeExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_dom::aliasedexpression_is_not_abstract():
    assert not inspect.isabstract(dom::AliasedExpression)


def test_dom::aliasedexpression_constructor_exists():
    assert callable(dom::AliasedExpression.__init__)


def test_dom::aliasedexpression_constructor_args():
    sig = inspect.signature(dom::AliasedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::aliasedexpression_has_name():
    assert hasattr(dom::AliasedExpression, "name")
    descriptor = None
    for klass in dom::AliasedExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom::BinaryExpression)


def test_dom::binaryexpression_constructor_exists():
    assert callable(dom::BinaryExpression.__init__)


def test_dom::binaryexpression_constructor_args():
    sig = inspect.signature(dom::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::binaryexpression_has_operator():
    assert hasattr(dom::BinaryExpression, "operator")
    descriptor = None
    for klass in dom::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::collectionfunction_is_not_abstract():
    assert not inspect.isabstract(dom::CollectionFunction)


def test_dom::collectionfunction_constructor_exists():
    assert callable(dom::CollectionFunction.__init__)


def test_dom::collectionfunction_constructor_args():
    sig = inspect.signature(dom::CollectionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_dom::collectionfunction_has_function():
    assert hasattr(dom::CollectionFunction, "function")
    descriptor = None
    for klass in dom::CollectionFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom::notexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NotExpression)


def test_dom::notexpression_constructor_exists():
    assert callable(dom::NotExpression.__init__)


def test_dom::notexpression_constructor_args():
    sig = inspect.signature(dom::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::castfunction_is_not_abstract():
    assert not inspect.isabstract(dom::CastFunction)


def test_dom::castfunction_constructor_exists():
    assert callable(dom::CastFunction.__init__)


def test_dom::castfunction_constructor_args():
    sig = inspect.signature(dom::CastFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "function" in params, "Missing parameter 'function'"

def test_dom::castfunction_has_name():
    assert hasattr(dom::CastFunction, "name")
    descriptor = None
    for klass in dom::CastFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::castfunction_has_function():
    assert hasattr(dom::CastFunction, "function")
    descriptor = None
    for klass in dom::CastFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom::queryparametervalue_is_not_abstract():
    assert not inspect.isabstract(dom::QueryParameterValue)


def test_dom::queryparametervalue_constructor_exists():
    assert callable(dom::QueryParameterValue.__init__)


def test_dom::queryparametervalue_constructor_args():
    sig = inspect.signature(dom::QueryParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::caseexpression_is_not_abstract():
    assert not inspect.isabstract(dom::CaseExpression)


def test_dom::caseexpression_constructor_exists():
    assert callable(dom::CaseExpression.__init__)


def test_dom::caseexpression_constructor_args():
    sig = inspect.signature(dom::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom::UnaryExpression)


def test_dom::unaryexpression_constructor_exists():
    assert callable(dom::UnaryExpression.__init__)


def test_dom::unaryexpression_constructor_args():
    sig = inspect.signature(dom::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::unaryexpression_has_operator():
    assert hasattr(dom::UnaryExpression, "operator")
    descriptor = None
    for klass in dom::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(dom::ParenthesizedExpression)


def test_dom::parenthesizedexpression_constructor_exists():
    assert callable(dom::ParenthesizedExpression.__init__)


def test_dom::parenthesizedexpression_constructor_args():
    sig = inspect.signature(dom::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::trimfunction_is_not_abstract():
    assert not inspect.isabstract(dom::TrimFunction)


def test_dom::trimfunction_constructor_exists():
    assert callable(dom::TrimFunction.__init__)


def test_dom::trimfunction_constructor_args():
    sig = inspect.signature(dom::TrimFunction.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "function" in params, "Missing parameter 'function'"

def test_dom::trimfunction_has_mode():
    assert hasattr(dom::TrimFunction, "mode")
    descriptor = None
    for klass in dom::TrimFunction.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_dom::trimfunction_has_function():
    assert hasattr(dom::TrimFunction, "function")
    descriptor = None
    for klass in dom::TrimFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom::memberofexpression_is_not_abstract():
    assert not inspect.isabstract(dom::MemberOfExpression)


def test_dom::memberofexpression_constructor_exists():
    assert callable(dom::MemberOfExpression.__init__)


def test_dom::memberofexpression_constructor_args():
    sig = inspect.signature(dom::MemberOfExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "memberOf" in params, "Missing parameter 'memberOf'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::memberofexpression_has_not_():
    assert hasattr(dom::MemberOfExpression, "not_")
    descriptor = None
    for klass in dom::MemberOfExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom::memberofexpression_has_memberOf():
    assert hasattr(dom::MemberOfExpression, "memberOf")
    descriptor = None
    for klass in dom::MemberOfExpression.__mro__:
        if "memberOf" in klass.__dict__:
            descriptor = klass.__dict__["memberOf"]
            break
    assert isinstance(descriptor, property)

def test_dom::memberofexpression_has_operator():
    assert hasattr(dom::MemberOfExpression, "operator")
    descriptor = None
    for klass in dom::MemberOfExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::functioncall_is_not_abstract():
    assert not inspect.isabstract(dom::FunctionCall)


def test_dom::functioncall_constructor_exists():
    assert callable(dom::FunctionCall.__init__)


def test_dom::functioncall_constructor_args():
    sig = inspect.signature(dom::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_dom::functioncall_has_function():
    assert hasattr(dom::FunctionCall, "function")
    descriptor = None
    for klass in dom::FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom::inexpression_is_not_abstract():
    assert not inspect.isabstract(dom::InExpression)


def test_dom::inexpression_constructor_exists():
    assert callable(dom::InExpression.__init__)


def test_dom::inexpression_constructor_args():
    sig = inspect.signature(dom::InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::inexpression_has_not_():
    assert hasattr(dom::InExpression, "not_")
    descriptor = None
    for klass in dom::InExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom::inexpression_has_operator():
    assert hasattr(dom::InExpression, "operator")
    descriptor = None
    for klass in dom::InExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::aggregatefunction_is_not_abstract():
    assert not inspect.isabstract(dom::AggregateFunction)


def test_dom::aggregatefunction_constructor_exists():
    assert callable(dom::AggregateFunction.__init__)


def test_dom::aggregatefunction_constructor_args():
    sig = inspect.signature(dom::AggregateFunction.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"
    assert "function" in params, "Missing parameter 'function'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_dom::aggregatefunction_has_all():
    assert hasattr(dom::AggregateFunction, "all")
    descriptor = None
    for klass in dom::AggregateFunction.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_dom::aggregatefunction_has_function():
    assert hasattr(dom::AggregateFunction, "function")
    descriptor = None
    for klass in dom::AggregateFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_dom::aggregatefunction_has_from_():
    assert hasattr(dom::AggregateFunction, "from_")
    descriptor = None
    for klass in dom::AggregateFunction.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_dom::aggregatefunction_has_distinct():
    assert hasattr(dom::AggregateFunction, "distinct")
    descriptor = None
    for klass in dom::AggregateFunction.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_dom::literalvalue_is_not_abstract():
    assert not inspect.isabstract(dom::LiteralValue)


def test_dom::literalvalue_constructor_exists():
    assert callable(dom::LiteralValue.__init__)


def test_dom::literalvalue_constructor_args():
    sig = inspect.signature(dom::LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(dom::QuantifiedExpression)


def test_dom::quantifiedexpression_constructor_exists():
    assert callable(dom::QuantifiedExpression.__init__)


def test_dom::quantifiedexpression_constructor_args():
    sig = inspect.signature(dom::QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::quantifiedexpression_has_quantifier():
    assert hasattr(dom::QuantifiedExpression, "quantifier")
    descriptor = None
    for klass in dom::QuantifiedExpression.__mro__:
        if "quantifier" in klass.__dict__:
            descriptor = klass.__dict__["quantifier"]
            break
    assert isinstance(descriptor, property)

def test_dom::quantifiedexpression_has_name():
    assert hasattr(dom::QuantifiedExpression, "name")
    descriptor = None
    for klass in dom::QuantifiedExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::betweenexpression_is_not_abstract():
    assert not inspect.isabstract(dom::BetweenExpression)


def test_dom::betweenexpression_constructor_exists():
    assert callable(dom::BetweenExpression.__init__)


def test_dom::betweenexpression_constructor_args():
    sig = inspect.signature(dom::BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom::betweenexpression_has_not_():
    assert hasattr(dom::BetweenExpression, "not_")
    descriptor = None
    for klass in dom::BetweenExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom::betweenexpression_has_operator():
    assert hasattr(dom::BetweenExpression, "operator")
    descriptor = None
    for klass in dom::BetweenExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom::joinentity_is_not_abstract():
    assert not inspect.isabstract(dom::JoinEntity)


def test_dom::joinentity_constructor_exists():
    assert callable(dom::JoinEntity.__init__)


def test_dom::joinentity_constructor_args():
    sig = inspect.signature(dom::JoinEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::joinentity_has_name():
    assert hasattr(dom::JoinEntity, "name")
    descriptor = None
    for klass in dom::JoinEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::incollectionelements_is_not_abstract():
    assert not inspect.isabstract(dom::InCollectionElements)


def test_dom::incollectionelements_constructor_exists():
    assert callable(dom::InCollectionElements.__init__)


def test_dom::incollectionelements_constructor_args():
    sig = inspect.signature(dom::InCollectionElements.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_dom::incollectionelements_has_name():
    assert hasattr(dom::InCollectionElements, "name")
    descriptor = None
    for klass in dom::InCollectionElements.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::incollectionelements_has_reference():
    assert hasattr(dom::InCollectionElements, "reference")
    descriptor = None
    for klass in dom::InCollectionElements.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_dom::propertyvalue_is_not_abstract():
    assert not inspect.isabstract(dom::PropertyValue)


def test_dom::propertyvalue_constructor_exists():
    assert callable(dom::PropertyValue.__init__)


def test_dom::propertyvalue_constructor_args():
    sig = inspect.signature(dom::PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"
    assert "classProperty" in params, "Missing parameter 'classProperty'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::propertyvalue_has_segments():
    assert hasattr(dom::PropertyValue, "segments")
    descriptor = None
    for klass in dom::PropertyValue.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)

def test_dom::propertyvalue_has_classProperty():
    assert hasattr(dom::PropertyValue, "classProperty")
    descriptor = None
    for klass in dom::PropertyValue.__mro__:
        if "classProperty" in klass.__dict__:
            descriptor = klass.__dict__["classProperty"]
            break
    assert isinstance(descriptor, property)

def test_dom::propertyvalue_has_name():
    assert hasattr(dom::PropertyValue, "name")
    descriptor = None
    for klass in dom::PropertyValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::propertyassignment_is_not_abstract():
    assert not inspect.isabstract(dom::PropertyAssignment)


def test_dom::propertyassignment_constructor_exists():
    assert callable(dom::PropertyAssignment.__init__)


def test_dom::propertyassignment_constructor_args():
    sig = inspect.signature(dom::PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::selectclass_is_not_abstract():
    assert not inspect.isabstract(dom::SelectClass)


def test_dom::selectclass_constructor_exists():
    assert callable(dom::SelectClass.__init__)


def test_dom::selectclass_constructor_args():
    sig = inspect.signature(dom::SelectClass.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_dom::selectclass_has_class_():
    assert hasattr(dom::SelectClass, "class_")
    descriptor = None
    for klass in dom::SelectClass.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dom::selectobject_is_not_abstract():
    assert not inspect.isabstract(dom::SelectObject)


def test_dom::selectobject_constructor_exists():
    assert callable(dom::SelectObject.__init__)


def test_dom::selectobject_constructor_args():
    sig = inspect.signature(dom::SelectObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::selectobject_has_name():
    assert hasattr(dom::SelectObject, "name")
    descriptor = None
    for klass in dom::SelectObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::selectproperties_is_not_abstract():
    assert not inspect.isabstract(dom::SelectProperties)


def test_dom::selectproperties_constructor_exists():
    assert callable(dom::SelectProperties.__init__)


def test_dom::selectproperties_constructor_args():
    sig = inspect.signature(dom::SelectProperties.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_dom::selectproperties_has_distinct():
    assert hasattr(dom::SelectProperties, "distinct")
    descriptor = None
    for klass in dom::SelectProperties.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_dom::sortorderelement_is_not_abstract():
    assert not inspect.isabstract(dom::SortOrderElement)


def test_dom::sortorderelement_constructor_exists():
    assert callable(dom::SortOrderElement.__init__)


def test_dom::sortorderelement_constructor_args():
    sig = inspect.signature(dom::SortOrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "sortOrder" in params, "Missing parameter 'sortOrder'"

def test_dom::sortorderelement_has_sortOrder():
    assert hasattr(dom::SortOrderElement, "sortOrder")
    descriptor = None
    for klass in dom::SortOrderElement.__mro__:
        if "sortOrder" in klass.__dict__:
            descriptor = klass.__dict__["sortOrder"]
            break
    assert isinstance(descriptor, property)



def test_dom::join_is_not_abstract():
    assert not inspect.isabstract(dom::Join)


def test_dom::join_constructor_exists():
    assert callable(dom::Join.__init__)


def test_dom::join_constructor_args():
    sig = inspect.signature(dom::Join.__init__)
    params = list(sig.parameters.keys())
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "type" in params, "Missing parameter 'type'"
    assert "propertyFetch" in params, "Missing parameter 'propertyFetch'"

def test_dom::join_has_fetch():
    assert hasattr(dom::Join, "fetch")
    descriptor = None
    for klass in dom::Join.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_dom::join_has_type():
    assert hasattr(dom::Join, "type")
    descriptor = None
    for klass in dom::Join.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dom::join_has_propertyFetch():
    assert hasattr(dom::Join, "propertyFetch")
    descriptor = None
    for klass in dom::Join.__mro__:
        if "propertyFetch" in klass.__dict__:
            descriptor = klass.__dict__["propertyFetch"]
            break
    assert isinstance(descriptor, property)



def test_dom::fromrange_is_not_abstract():
    assert not inspect.isabstract(dom::FromRange)


def test_dom::fromrange_constructor_exists():
    assert callable(dom::FromRange.__init__)


def test_dom::fromrange_constructor_args():
    sig = inspect.signature(dom::FromRange.__init__)
    params = list(sig.parameters.keys())



def test_dom::calloutputparameter_is_not_abstract():
    assert not inspect.isabstract(dom::CallOutputParameter)


def test_dom::calloutputparameter_constructor_exists():
    assert callable(dom::CallOutputParameter.__init__)


def test_dom::calloutputparameter_constructor_args():
    sig = inspect.signature(dom::CallOutputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::calloutputparameter_has_name():
    assert hasattr(dom::CallOutputParameter, "name")
    descriptor = None
    for klass in dom::CallOutputParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::callinputparameter_is_not_abstract():
    assert not inspect.isabstract(dom::CallInputParameter)


def test_dom::callinputparameter_constructor_exists():
    assert callable(dom::CallInputParameter.__init__)


def test_dom::callinputparameter_constructor_args():
    sig = inspect.signature(dom::CallInputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::callinputparameter_has_name():
    assert hasattr(dom::CallInputParameter, "name")
    descriptor = None
    for klass in dom::CallInputParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qlstatement_is_not_abstract():
    assert not inspect.isabstract(QlStatement)


def test_qlstatement_constructor_exists():
    assert callable(QlStatement.__init__)


def test_qlstatement_constructor_args():
    sig = inspect.signature(QlStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::selectstatement_is_not_abstract():
    assert not inspect.isabstract(dom::SelectStatement)


def test_dom::selectstatement_constructor_exists():
    assert callable(dom::SelectStatement.__init__)


def test_dom::selectstatement_constructor_args():
    sig = inspect.signature(dom::SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::updatestatement_is_not_abstract():
    assert not inspect.isabstract(dom::UpdateStatement)


def test_dom::updatestatement_constructor_exists():
    assert callable(dom::UpdateStatement.__init__)


def test_dom::updatestatement_constructor_args():
    sig = inspect.signature(dom::UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "versioned" in params, "Missing parameter 'versioned'"

def test_dom::updatestatement_has_name():
    assert hasattr(dom::UpdateStatement, "name")
    descriptor = None
    for klass in dom::UpdateStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::updatestatement_has_versioned():
    assert hasattr(dom::UpdateStatement, "versioned")
    descriptor = None
    for klass in dom::UpdateStatement.__mro__:
        if "versioned" in klass.__dict__:
            descriptor = klass.__dict__["versioned"]
            break
    assert isinstance(descriptor, property)



def test_dom::insertstatement_is_not_abstract():
    assert not inspect.isabstract(dom::InsertStatement)


def test_dom::insertstatement_constructor_exists():
    assert callable(dom::InsertStatement.__init__)


def test_dom::insertstatement_constructor_args():
    sig = inspect.signature(dom::InsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::deletestatement_is_not_abstract():
    assert not inspect.isabstract(dom::DeleteStatement)


def test_dom::deletestatement_constructor_exists():
    assert callable(dom::DeleteStatement.__init__)


def test_dom::deletestatement_constructor_args():
    sig = inspect.signature(dom::DeleteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::deletestatement_has_name():
    assert hasattr(dom::DeleteStatement, "name")
    descriptor = None
    for klass in dom::DeleteStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::callablestatement_is_not_abstract():
    assert not inspect.isabstract(dom::CallableStatement)


def test_dom::callablestatement_constructor_exists():
    assert callable(dom::CallableStatement.__init__)


def test_dom::callablestatement_constructor_args():
    sig = inspect.signature(dom::CallableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "functionCall" in params, "Missing parameter 'functionCall'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::callablestatement_has_functionCall():
    assert hasattr(dom::CallableStatement, "functionCall")
    descriptor = None
    for klass in dom::CallableStatement.__mro__:
        if "functionCall" in klass.__dict__:
            descriptor = klass.__dict__["functionCall"]
            break
    assert isinstance(descriptor, property)

def test_dom::callablestatement_has_name():
    assert hasattr(dom::CallableStatement, "name")
    descriptor = None
    for klass in dom::CallableStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::function_is_not_abstract():
    assert not inspect.isabstract(dom::Function)


def test_dom::function_constructor_exists():
    assert callable(dom::Function.__init__)


def test_dom::function_constructor_args():
    sig = inspect.signature(dom::Function.__init__)
    params = list(sig.parameters.keys())



def test_dom::applicationsession_is_not_abstract():
    assert not inspect.isabstract(dom::ApplicationSession)


def test_dom::applicationsession_constructor_exists():
    assert callable(dom::ApplicationSession.__init__)


def test_dom::applicationsession_constructor_args():
    sig = inspect.signature(dom::ApplicationSession.__init__)
    params = list(sig.parameters.keys())



def test_daofeature_is_not_abstract():
    assert not inspect.isabstract(DaoFeature)


def test_daofeature_constructor_exists():
    assert callable(DaoFeature.__init__)


def test_daofeature_constructor_args():
    sig = inspect.signature(DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_dom::sqltype_is_not_abstract():
    assert not inspect.isabstract(dom::SqlType)


def test_dom::sqltype_constructor_exists():
    assert callable(dom::SqlType.__init__)


def test_dom::sqltype_constructor_args():
    sig = inspect.signature(dom::SqlType.__init__)
    params = list(sig.parameters.keys())



def test_dom::onetoone_is_not_abstract():
    assert not inspect.isabstract(dom::OneToOne)


def test_dom::onetoone_constructor_exists():
    assert callable(dom::OneToOne.__init__)


def test_dom::onetoone_constructor_args():
    sig = inspect.signature(dom::OneToOne.__init__)
    params = list(sig.parameters.keys())



def test_dom::manytoone_is_not_abstract():
    assert not inspect.isabstract(dom::ManyToOne)


def test_dom::manytoone_constructor_exists():
    assert callable(dom::ManyToOne.__init__)


def test_dom::manytoone_constructor_args():
    sig = inspect.signature(dom::ManyToOne.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_dom::manytoone_has_columnName():
    assert hasattr(dom::ManyToOne, "columnName")
    descriptor = None
    for klass in dom::ManyToOne.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dom::manytoone_has_derived():
    assert hasattr(dom::ManyToOne, "derived")
    descriptor = None
    for klass in dom::ManyToOne.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_dom::column_is_not_abstract():
    assert not inspect.isabstract(dom::Column)


def test_dom::column_constructor_exists():
    assert callable(dom::Column.__init__)


def test_dom::column_constructor_args():
    sig = inspect.signature(dom::Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dom::column_has_columnName():
    assert hasattr(dom::Column, "columnName")
    descriptor = None
    for klass in dom::Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dom::databaseconstraint_is_not_abstract():
    assert not inspect.isabstract(dom::DataBaseConstraint)


def test_dom::databaseconstraint_constructor_exists():
    assert callable(dom::DataBaseConstraint.__init__)


def test_dom::databaseconstraint_constructor_args():
    sig = inspect.signature(dom::DataBaseConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::databaseconstraint_has_type():
    assert hasattr(dom::DataBaseConstraint, "type")
    descriptor = None
    for klass in dom::DataBaseConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dom::databaseconstraint_has_name():
    assert hasattr(dom::DataBaseConstraint, "name")
    descriptor = None
    for klass in dom::DataBaseConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::qlstatement_is_not_abstract():
    assert not inspect.isabstract(dom::QlStatement)


def test_dom::qlstatement_constructor_exists():
    assert callable(dom::QlStatement.__init__)


def test_dom::qlstatement_constructor_args():
    sig = inspect.signature(dom::QlStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::queryparameter_is_not_abstract():
    assert not inspect.isabstract(dom::QueryParameter)


def test_dom::queryparameter_constructor_exists():
    assert callable(dom::QueryParameter.__init__)


def test_dom::queryparameter_constructor_args():
    sig = inspect.signature(dom::QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::manytomany_is_not_abstract():
    assert not inspect.isabstract(dom::ManyToMany)


def test_dom::manytomany_constructor_exists():
    assert callable(dom::ManyToMany.__init__)


def test_dom::manytomany_constructor_args():
    sig = inspect.signature(dom::ManyToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "inverse" in params, "Missing parameter 'inverse'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dom::manytomany_has_columnName():
    assert hasattr(dom::ManyToMany, "columnName")
    descriptor = None
    for klass in dom::ManyToMany.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dom::manytomany_has_inverse():
    assert hasattr(dom::ManyToMany, "inverse")
    descriptor = None
    for klass in dom::ManyToMany.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)

def test_dom::manytomany_has_tableName():
    assert hasattr(dom::ManyToMany, "tableName")
    descriptor = None
    for klass in dom::ManyToMany.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dom::onetomany_is_not_abstract():
    assert not inspect.isabstract(dom::OneToMany)


def test_dom::onetomany_constructor_exists():
    assert callable(dom::OneToMany.__init__)


def test_dom::onetomany_constructor_args():
    sig = inspect.signature(dom::OneToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dom::onetomany_has_columnName():
    assert hasattr(dom::OneToMany, "columnName")
    descriptor = None
    for klass in dom::OneToMany.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dom::queryoperation_is_not_abstract():
    assert not inspect.isabstract(dom::QueryOperation)


def test_dom::queryoperation_constructor_exists():
    assert callable(dom::QueryOperation.__init__)


def test_dom::queryoperation_constructor_args():
    sig = inspect.signature(dom::QueryOperation.__init__)
    params = list(sig.parameters.keys())



def test_dom::daofeature_is_not_abstract():
    assert not inspect.isabstract(dom::DaoFeature)


def test_dom::daofeature_constructor_exists():
    assert callable(dom::DaoFeature.__init__)


def test_dom::daofeature_constructor_args():
    sig = inspect.signature(dom::DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_dom::attributesortorder_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeSortOrder)


def test_dom::attributesortorder_constructor_exists():
    assert callable(dom::AttributeSortOrder.__init__)


def test_dom::attributesortorder_constructor_args():
    sig = inspect.signature(dom::AttributeSortOrder.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"

def test_dom::attributesortorder_has_desc():
    assert hasattr(dom::AttributeSortOrder, "desc")
    descriptor = None
    for klass in dom::AttributeSortOrder.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributesortorder_has_asc():
    assert hasattr(dom::AttributeSortOrder, "asc")
    descriptor = None
    for klass in dom::AttributeSortOrder.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)



def test_dom::validatorreference_is_not_abstract():
    assert not inspect.isabstract(dom::ValidatorReference)


def test_dom::validatorreference_constructor_exists():
    assert callable(dom::ValidatorReference.__init__)


def test_dom::validatorreference_constructor_args():
    sig = inspect.signature(dom::ValidatorReference.__init__)
    params = list(sig.parameters.keys())



def test_dom::constraint_is_not_abstract():
    assert not inspect.isabstract(dom::Constraint)


def test_dom::constraint_constructor_exists():
    assert callable(dom::Constraint.__init__)


def test_dom::constraint_constructor_args():
    sig = inspect.signature(dom::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_dom::boolliteral_is_not_abstract():
    assert not inspect.isabstract(dom::BoolLiteral)


def test_dom::boolliteral_constructor_exists():
    assert callable(dom::BoolLiteral.__init__)


def test_dom::boolliteral_constructor_args():
    sig = inspect.signature(dom::BoolLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expressionflag_is_not_abstract():
    assert not inspect.isabstract(ExpressionFlag)


def test_expressionflag_constructor_exists():
    assert callable(ExpressionFlag.__init__)


def test_expressionflag_constructor_args():
    sig = inspect.signature(ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::availableflag_is_not_abstract():
    assert not inspect.isabstract(dom::AvailableFlag)


def test_dom::availableflag_constructor_exists():
    assert callable(dom::AvailableFlag.__init__)


def test_dom::availableflag_constructor_args():
    sig = inspect.signature(dom::AvailableFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::readonlyflag_is_not_abstract():
    assert not inspect.isabstract(dom::ReadOnlyFlag)


def test_dom::readonlyflag_constructor_exists():
    assert callable(dom::ReadOnlyFlag.__init__)


def test_dom::readonlyflag_constructor_args():
    sig = inspect.signature(dom::ReadOnlyFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::requiredflag_is_not_abstract():
    assert not inspect.isabstract(dom::RequiredFlag)


def test_dom::requiredflag_constructor_exists():
    assert callable(dom::RequiredFlag.__init__)


def test_dom::requiredflag_constructor_args():
    sig = inspect.signature(dom::RequiredFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::equalityexpr_is_not_abstract():
    assert not inspect.isabstract(dom::EqualityExpr)


def test_dom::equalityexpr_constructor_exists():
    assert callable(dom::EqualityExpr.__init__)


def test_dom::equalityexpr_constructor_args():
    sig = inspect.signature(dom::EqualityExpr.__init__)
    params = list(sig.parameters.keys())



def test_attributeflag_is_not_abstract():
    assert not inspect.isabstract(AttributeFlag)


def test_attributeflag_constructor_exists():
    assert callable(AttributeFlag.__init__)


def test_attributeflag_constructor_args():
    sig = inspect.signature(AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::transientflag_is_not_abstract():
    assert not inspect.isabstract(dom::TransientFlag)


def test_dom::transientflag_constructor_exists():
    assert callable(dom::TransientFlag.__init__)


def test_dom::transientflag_constructor_args():
    sig = inspect.signature(dom::TransientFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::derivedflag_is_not_abstract():
    assert not inspect.isabstract(dom::DerivedFlag)


def test_dom::derivedflag_constructor_exists():
    assert callable(dom::DerivedFlag.__init__)


def test_dom::derivedflag_constructor_args():
    sig = inspect.signature(dom::DerivedFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::expressionflag_is_not_abstract():
    assert not inspect.isabstract(dom::ExpressionFlag)


def test_dom::expressionflag_constructor_exists():
    assert callable(dom::ExpressionFlag.__init__)


def test_dom::expressionflag_constructor_args():
    sig = inspect.signature(dom::ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_attributeproperty_is_not_abstract():
    assert not inspect.isabstract(AttributeProperty)


def test_attributeproperty_constructor_exists():
    assert callable(AttributeProperty.__init__)


def test_attributeproperty_constructor_args():
    sig = inspect.signature(AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom::attributetextproperty_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeTextProperty)


def test_dom::attributetextproperty_constructor_exists():
    assert callable(dom::AttributeTextProperty.__init__)


def test_dom::attributetextproperty_constructor_args():
    sig = inspect.signature(dom::AttributeTextProperty.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "unitText" in params, "Missing parameter 'unitText'"
    assert "hstoreColumn" in params, "Missing parameter 'hstoreColumn'"

def test_dom::attributetextproperty_has_labelText():
    assert hasattr(dom::AttributeTextProperty, "labelText")
    descriptor = None
    for klass in dom::AttributeTextProperty.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributetextproperty_has_tooltipText():
    assert hasattr(dom::AttributeTextProperty, "tooltipText")
    descriptor = None
    for klass in dom::AttributeTextProperty.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributetextproperty_has_unitText():
    assert hasattr(dom::AttributeTextProperty, "unitText")
    descriptor = None
    for klass in dom::AttributeTextProperty.__mro__:
        if "unitText" in klass.__dict__:
            descriptor = klass.__dict__["unitText"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributetextproperty_has_hstoreColumn():
    assert hasattr(dom::AttributeTextProperty, "hstoreColumn")
    descriptor = None
    for klass in dom::AttributeTextProperty.__mro__:
        if "hstoreColumn" in klass.__dict__:
            descriptor = klass.__dict__["hstoreColumn"]
            break
    assert isinstance(descriptor, property)



def test_dom::attributevalidationproperty_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeValidationProperty)


def test_dom::attributevalidationproperty_constructor_exists():
    assert callable(dom::AttributeValidationProperty.__init__)


def test_dom::attributevalidationproperty_constructor_args():
    sig = inspect.signature(dom::AttributeValidationProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom::attributeflag_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeFlag)


def test_dom::attributeflag_constructor_exists():
    assert callable(dom::AttributeFlag.__init__)


def test_dom::attributeflag_constructor_args():
    sig = inspect.signature(dom::AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom::incrementerreference_is_not_abstract():
    assert not inspect.isabstract(dom::IncrementerReference)


def test_dom::incrementerreference_constructor_exists():
    assert callable(dom::IncrementerReference.__init__)


def test_dom::incrementerreference_constructor_args():
    sig = inspect.signature(dom::IncrementerReference.__init__)
    params = list(sig.parameters.keys())



def test_dom::datatypeandtypeparameter_is_not_abstract():
    assert not inspect.isabstract(dom::DataTypeAndTypeParameter)


def test_dom::datatypeandtypeparameter_constructor_exists():
    assert callable(dom::DataTypeAndTypeParameter.__init__)


def test_dom::datatypeandtypeparameter_constructor_args():
    sig = inspect.signature(dom::DataTypeAndTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::propertymapping_is_not_abstract():
    assert not inspect.isabstract(dom::PropertyMapping)


def test_dom::propertymapping_constructor_exists():
    assert callable(dom::PropertyMapping.__init__)


def test_dom::propertymapping_constructor_args():
    sig = inspect.signature(dom::PropertyMapping.__init__)
    params = list(sig.parameters.keys())
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "toLeft" in params, "Missing parameter 'toLeft'"
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"

def test_dom::propertymapping_has_toRight():
    assert hasattr(dom::PropertyMapping, "toRight")
    descriptor = None
    for klass in dom::PropertyMapping.__mro__:
        if "toRight" in klass.__dict__:
            descriptor = klass.__dict__["toRight"]
            break
    assert isinstance(descriptor, property)

def test_dom::propertymapping_has_toLeft():
    assert hasattr(dom::PropertyMapping, "toLeft")
    descriptor = None
    for klass in dom::PropertyMapping.__mro__:
        if "toLeft" in klass.__dict__:
            descriptor = klass.__dict__["toLeft"]
            break
    assert isinstance(descriptor, property)

def test_dom::propertymapping_has_biDirectional():
    assert hasattr(dom::PropertyMapping, "biDirectional")
    descriptor = None
    for klass in dom::PropertyMapping.__mro__:
        if "biDirectional" in klass.__dict__:
            descriptor = klass.__dict__["biDirectional"]
            break
    assert isinstance(descriptor, property)



def test_dom::conditionsblock_is_not_abstract():
    assert not inspect.isabstract(dom::ConditionsBlock)


def test_dom::conditionsblock_constructor_exists():
    assert callable(dom::ConditionsBlock.__init__)


def test_dom::conditionsblock_constructor_args():
    sig = inspect.signature(dom::ConditionsBlock.__init__)
    params = list(sig.parameters.keys())



def test_dom::attributegroup_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeGroup)


def test_dom::attributegroup_constructor_exists():
    assert callable(dom::AttributeGroup.__init__)


def test_dom::attributegroup_constructor_args():
    sig = inspect.signature(dom::AttributeGroup.__init__)
    params = list(sig.parameters.keys())
    assert "sortorder" in params, "Missing parameter 'sortorder'"
    assert "key" in params, "Missing parameter 'key'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::attributegroup_has_sortorder():
    assert hasattr(dom::AttributeGroup, "sortorder")
    descriptor = None
    for klass in dom::AttributeGroup.__mro__:
        if "sortorder" in klass.__dict__:
            descriptor = klass.__dict__["sortorder"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributegroup_has_key():
    assert hasattr(dom::AttributeGroup, "key")
    descriptor = None
    for klass in dom::AttributeGroup.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributegroup_has_unique():
    assert hasattr(dom::AttributeGroup, "unique")
    descriptor = None
    for klass in dom::AttributeGroup.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributegroup_has_filter():
    assert hasattr(dom::AttributeGroup, "filter")
    descriptor = None
    for klass in dom::AttributeGroup.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)

def test_dom::attributegroup_has_name():
    assert hasattr(dom::AttributeGroup, "name")
    descriptor = None
    for klass in dom::AttributeGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_presentablefeature_is_not_abstract():
    assert not inspect.isabstract(PresentableFeature)


def test_presentablefeature_constructor_exists():
    assert callable(PresentableFeature.__init__)


def test_presentablefeature_constructor_args():
    sig = inspect.signature(PresentableFeature.__init__)
    params = list(sig.parameters.keys())



def test_dom::featurereference_is_not_abstract():
    assert not inspect.isabstract(dom::FeatureReference)


def test_dom::featurereference_constructor_exists():
    assert callable(dom::FeatureReference.__init__)


def test_dom::featurereference_constructor_args():
    sig = inspect.signature(dom::FeatureReference.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_dom::featurereference_has_all():
    assert hasattr(dom::FeatureReference, "all")
    descriptor = None
    for klass in dom::FeatureReference.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_dom::entity_is_not_abstract():
    assert not inspect.isabstract(dom::Entity)


def test_dom::entity_constructor_exists():
    assert callable(dom::Entity.__init__)


def test_dom::entity_constructor_args():
    sig = inspect.signature(dom::Entity.__init__)
    params = list(sig.parameters.keys())



def test_dom::valueobject_is_not_abstract():
    assert not inspect.isabstract(dom::ValueObject)


def test_dom::valueobject_constructor_exists():
    assert callable(dom::ValueObject.__init__)


def test_dom::valueobject_constructor_args():
    sig = inspect.signature(dom::ValueObject.__init__)
    params = list(sig.parameters.keys())



def test_dom::mapper_is_not_abstract():
    assert not inspect.isabstract(dom::Mapper)


def test_dom::mapper_constructor_exists():
    assert callable(dom::Mapper.__init__)


def test_dom::mapper_constructor_args():
    sig = inspect.signature(dom::Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "toLeft" in params, "Missing parameter 'toLeft'"
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"

def test_dom::mapper_has_toLeft():
    assert hasattr(dom::Mapper, "toLeft")
    descriptor = None
    for klass in dom::Mapper.__mro__:
        if "toLeft" in klass.__dict__:
            descriptor = klass.__dict__["toLeft"]
            break
    assert isinstance(descriptor, property)

def test_dom::mapper_has_toRight():
    assert hasattr(dom::Mapper, "toRight")
    descriptor = None
    for klass in dom::Mapper.__mro__:
        if "toRight" in klass.__dict__:
            descriptor = klass.__dict__["toRight"]
            break
    assert isinstance(descriptor, property)

def test_dom::mapper_has_biDirectional():
    assert hasattr(dom::Mapper, "biDirectional")
    descriptor = None
    for klass in dom::Mapper.__mro__:
        if "biDirectional" in klass.__dict__:
            descriptor = klass.__dict__["biDirectional"]
            break
    assert isinstance(descriptor, property)



def test_dom::attributeproperty_is_not_abstract():
    assert not inspect.isabstract(dom::AttributeProperty)


def test_dom::attributeproperty_constructor_exists():
    assert callable(dom::AttributeProperty.__init__)


def test_dom::attributeproperty_constructor_args():
    sig = inspect.signature(dom::AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom::dataview_is_not_abstract():
    assert not inspect.isabstract(dom::DataView)


def test_dom::dataview_constructor_exists():
    assert callable(dom::DataView.__init__)


def test_dom::dataview_constructor_args():
    sig = inspect.signature(dom::DataView.__init__)
    params = list(sig.parameters.keys())



def test_dom::type_is_not_abstract():
    assert not inspect.isabstract(dom::Type)


def test_dom::type_constructor_exists():
    assert callable(dom::Type.__init__)


def test_dom::type_constructor_args():
    sig = inspect.signature(dom::Type.__init__)
    params = list(sig.parameters.keys())



def test_queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(QueryParameterReference)


def test_queryparameterreference_constructor_exists():
    assert callable(QueryParameterReference.__init__)


def test_queryparameterreference_constructor_args():
    sig = inspect.signature(QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_dom::ielementwithnoname_is_not_abstract():
    assert not inspect.isabstract(dom::IElementWithNoName)


def test_dom::ielementwithnoname_constructor_exists():
    assert callable(dom::IElementWithNoName.__init__)


def test_dom::ielementwithnoname_constructor_args():
    sig = inspect.signature(dom::IElementWithNoName.__init__)
    params = list(sig.parameters.keys())
    assert "noName" in params, "Missing parameter 'noName'"

def test_dom::ielementwithnoname_has_noName():
    assert hasattr(dom::IElementWithNoName, "noName")
    descriptor = None
    for klass in dom::IElementWithNoName.__mro__:
        if "noName" in klass.__dict__:
            descriptor = klass.__dict__["noName"]
            break
    assert isinstance(descriptor, property)



def test_dom::attribute_is_not_abstract():
    assert not inspect.isabstract(dom::Attribute)


def test_dom::attribute_constructor_exists():
    assert callable(dom::Attribute.__init__)


def test_dom::attribute_constructor_args():
    sig = inspect.signature(dom::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "composition" in params, "Missing parameter 'composition'"
    assert "required" in params, "Missing parameter 'required'"
    assert "version" in params, "Missing parameter 'version'"
    assert "dataTypeName" in params, "Missing parameter 'dataTypeName'"
    assert "many" in params, "Missing parameter 'many'"

def test_dom::attribute_has_identifier():
    assert hasattr(dom::Attribute, "identifier")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_derived():
    assert hasattr(dom::Attribute, "derived")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_readOnly():
    assert hasattr(dom::Attribute, "readOnly")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_transient():
    assert hasattr(dom::Attribute, "transient")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_reference():
    assert hasattr(dom::Attribute, "reference")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_defaultValue():
    assert hasattr(dom::Attribute, "defaultValue")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_composition():
    assert hasattr(dom::Attribute, "composition")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "composition" in klass.__dict__:
            descriptor = klass.__dict__["composition"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_required():
    assert hasattr(dom::Attribute, "required")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_version():
    assert hasattr(dom::Attribute, "version")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_dataTypeName():
    assert hasattr(dom::Attribute, "dataTypeName")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "dataTypeName" in klass.__dict__:
            descriptor = klass.__dict__["dataTypeName"]
            break
    assert isinstance(descriptor, property)

def test_dom::attribute_has_many():
    assert hasattr(dom::Attribute, "many")
    descriptor = None
    for klass in dom::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_queryparameter_is_not_abstract():
    assert not inspect.isabstract(QueryParameter)


def test_queryparameter_constructor_exists():
    assert callable(QueryParameter.__init__)


def test_queryparameter_constructor_args():
    sig = inspect.signature(QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::parameter_is_not_abstract():
    assert not inspect.isabstract(dom::Parameter)


def test_dom::parameter_constructor_exists():
    assert callable(dom::Parameter.__init__)


def test_dom::parameter_constructor_args():
    sig = inspect.signature(dom::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_dom::parameter_has_name():
    assert hasattr(dom::Parameter, "name")
    descriptor = None
    for klass in dom::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::parameter_has_many():
    assert hasattr(dom::Parameter, "many")
    descriptor = None
    for klass in dom::Parameter.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_dom::expression_is_not_abstract():
    assert not inspect.isabstract(dom::Expression)


def test_dom::expression_constructor_exists():
    assert callable(dom::Expression.__init__)


def test_dom::expression_constructor_args():
    sig = inspect.signature(dom::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::daooperation_is_not_abstract():
    assert not inspect.isabstract(dom::DaoOperation)


def test_dom::daooperation_constructor_exists():
    assert callable(dom::DaoOperation.__init__)


def test_dom::daooperation_constructor_args():
    sig = inspect.signature(dom::DaoOperation.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom::daooperation_has_many():
    assert hasattr(dom::DaoOperation, "many")
    descriptor = None
    for klass in dom::DaoOperation.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_dom::daooperation_has_name():
    assert hasattr(dom::DaoOperation, "name")
    descriptor = None
    for klass in dom::DaoOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom::dao_is_not_abstract():
    assert not inspect.isabstract(dom::Dao)


def test_dom::dao_constructor_exists():
    assert callable(dom::Dao.__init__)


def test_dom::dao_constructor_args():
    sig = inspect.signature(dom::Dao.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "discriminator" in params, "Missing parameter 'discriminator'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_dom::dao_has_tableName():
    assert hasattr(dom::Dao, "tableName")
    descriptor = None
    for klass in dom::Dao.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dom::dao_has_discriminator():
    assert hasattr(dom::Dao, "discriminator")
    descriptor = None
    for klass in dom::Dao.__mro__:
        if "discriminator" in klass.__dict__:
            descriptor = klass.__dict__["discriminator"]
            break
    assert isinstance(descriptor, property)

def test_dom::dao_has_qualifier():
    assert hasattr(dom::Dao, "qualifier")
    descriptor = None
    for klass in dom::Dao.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_dom::delegateoperation_is_not_abstract():
    assert not inspect.isabstract(dom::DelegateOperation)


def test_dom::delegateoperation_constructor_exists():
    assert callable(dom::DelegateOperation.__init__)


def test_dom::delegateoperation_constructor_args():
    sig = inspect.signature(dom::DelegateOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "crudOperationType" in params, "Missing parameter 'crudOperationType'"
    assert "many" in params, "Missing parameter 'many'"

def test_dom::delegateoperation_has_name():
    assert hasattr(dom::DelegateOperation, "name")
    descriptor = None
    for klass in dom::DelegateOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom::delegateoperation_has_crudOperationType():
    assert hasattr(dom::DelegateOperation, "crudOperationType")
    descriptor = None
    for klass in dom::DelegateOperation.__mro__:
        if "crudOperationType" in klass.__dict__:
            descriptor = klass.__dict__["crudOperationType"]
            break
    assert isinstance(descriptor, property)

def test_dom::delegateoperation_has_many():
    assert hasattr(dom::DelegateOperation, "many")
    descriptor = None
    for klass in dom::DelegateOperation.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_databaseconstrainttype_exists():
    # Check that the Enumeration exists
    assert DataBaseConstraintType is not None

def test_databaseconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataBaseConstraintType]
    expected_literals = [
        "INDEX",
        "NULL",
        "UNIQUE",
        "PRIMARY",
        "NATURAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataBaseConstraintType"

def test_crudoperationtype_exists():
    # Check that the Enumeration exists
    assert CrudOperationType is not None

def test_crudoperationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CrudOperationType]
    expected_literals = [
        "NULL",
        "UPDATE",
        "READ",
        "CREATE",
        "ALL",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CrudOperationType"


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
dom::PresentableFeature_strategy = st.builds(
    dom::PresentableFeature,
    name=
        safe_text
)
dom::WhenClause_strategy = st.builds(
    dom::WhenClause,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
dom::IntegerLiteralValue_strategy = st.builds(
    dom::IntegerLiteralValue,
    value=
        safe_text
)
dom::EmptyLiteralValue_strategy = st.builds(
    dom::EmptyLiteralValue,
)
dom::RealLiteralValue_strategy = st.builds(
    dom::RealLiteralValue,
    value=
        safe_text
)
dom::NullLiteralValue_strategy = st.builds(
    dom::NullLiteralValue,
)
dom::BooleanLiteralValue_strategy = st.builds(
    dom::BooleanLiteralValue,
    isTrue=
        st.booleans()
)
dom::AltWhenClause_strategy = st.builds(
    dom::AltWhenClause,
)
dom::StringLiteralValue_strategy = st.builds(
    dom::StringLiteralValue,
    value=
        safe_text
)
dom::QueryParameterReference_strategy = st.builds(
    dom::QueryParameterReference,
)
JoinEntity_strategy = st.builds(
    JoinEntity,
)
FromRange_strategy = st.builds(
    FromRange,
)
dom::InClass_strategy = st.builds(
    dom::InClass,
    name=
        safe_text,
    class_=
        safe_text
)
dom::InCollection_strategy = st.builds(
    dom::InCollection,
    alias=
        safe_text,
    path=
        safe_text
)
dom::Dependant_strategy = st.builds(
    dom::Dependant,
)
Dependant_strategy = st.builds(
    Dependant,
)
DaoOperation_strategy = st.builds(
    DaoOperation,
)
dom::SimpleType_strategy = st.builds(
    dom::SimpleType,
)
IDocumentable_strategy = st.builds(
    IDocumentable,
)
dom::Operation_strategy = st.builds(
    dom::Operation,
    expression=
        safe_text
)
ReferenceableByXmadslVariable_strategy = st.builds(
    ReferenceableByXmadslVariable,
)
dom::Property_strategy = st.builds(
    dom::Property,
    name=
        safe_text,
    defaultValue=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
dom::Service_strategy = st.builds(
    dom::Service,
)
dom::ComplexType_strategy = st.builds(
    dom::ComplexType,
)
dom::FromClass_strategy = st.builds(
    dom::FromClass,
    popertyFetch=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
dom::SubQuery_strategy = st.builds(
    dom::SubQuery,
)
dom::LikeExpression_strategy = st.builds(
    dom::LikeExpression,
    operator=
        safe_text,
    not_=
        st.booleans()
)
dom::AliasedExpression_strategy = st.builds(
    dom::AliasedExpression,
    name=
        safe_text
)
dom::BinaryExpression_strategy = st.builds(
    dom::BinaryExpression,
    operator=
        safe_text
)
dom::CollectionFunction_strategy = st.builds(
    dom::CollectionFunction,
    function=
        safe_text
)
dom::NotExpression_strategy = st.builds(
    dom::NotExpression,
)
dom::CastFunction_strategy = st.builds(
    dom::CastFunction,
    name=
        safe_text,
    function=
        safe_text
)
dom::QueryParameterValue_strategy = st.builds(
    dom::QueryParameterValue,
)
dom::CaseExpression_strategy = st.builds(
    dom::CaseExpression,
)
dom::UnaryExpression_strategy = st.builds(
    dom::UnaryExpression,
    operator=
        safe_text
)
dom::ParenthesizedExpression_strategy = st.builds(
    dom::ParenthesizedExpression,
)
dom::TrimFunction_strategy = st.builds(
    dom::TrimFunction,
    mode=
        safe_text,
    function=
        safe_text
)
dom::MemberOfExpression_strategy = st.builds(
    dom::MemberOfExpression,
    not_=
        st.booleans(),
    memberOf=
        safe_text,
    operator=
        safe_text
)
dom::FunctionCall_strategy = st.builds(
    dom::FunctionCall,
    function=
        safe_text
)
dom::InExpression_strategy = st.builds(
    dom::InExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom::AggregateFunction_strategy = st.builds(
    dom::AggregateFunction,
    all=
        st.booleans(),
    function=
        safe_text,
    from_=
        safe_text,
    distinct=
        st.booleans()
)
dom::LiteralValue_strategy = st.builds(
    dom::LiteralValue,
)
dom::QuantifiedExpression_strategy = st.builds(
    dom::QuantifiedExpression,
    quantifier=
        safe_text,
    name=
        safe_text
)
dom::BetweenExpression_strategy = st.builds(
    dom::BetweenExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom::JoinEntity_strategy = st.builds(
    dom::JoinEntity,
    name=
        safe_text
)
dom::InCollectionElements_strategy = st.builds(
    dom::InCollectionElements,
    name=
        safe_text,
    reference=
        safe_text
)
dom::PropertyValue_strategy = st.builds(
    dom::PropertyValue,
    segments=
        safe_text,
    classProperty=
        st.booleans(),
    name=
        safe_text
)
dom::PropertyAssignment_strategy = st.builds(
    dom::PropertyAssignment,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
dom::SelectClass_strategy = st.builds(
    dom::SelectClass,
    class_=
        safe_text
)
dom::SelectObject_strategy = st.builds(
    dom::SelectObject,
    name=
        safe_text
)
dom::SelectProperties_strategy = st.builds(
    dom::SelectProperties,
    distinct=
        st.booleans()
)
dom::SortOrderElement_strategy = st.builds(
    dom::SortOrderElement,
    sortOrder=
        safe_text
)
dom::Join_strategy = st.builds(
    dom::Join,
    fetch=
        st.booleans(),
    type=
        safe_text,
    propertyFetch=
        st.booleans()
)
dom::FromRange_strategy = st.builds(
    dom::FromRange,
)
dom::CallOutputParameter_strategy = st.builds(
    dom::CallOutputParameter,
    name=
        safe_text
)
dom::CallInputParameter_strategy = st.builds(
    dom::CallInputParameter,
    name=
        safe_text
)
QlStatement_strategy = st.builds(
    QlStatement,
)
dom::SelectStatement_strategy = st.builds(
    dom::SelectStatement,
)
dom::UpdateStatement_strategy = st.builds(
    dom::UpdateStatement,
    name=
        safe_text,
    versioned=
        st.booleans()
)
dom::InsertStatement_strategy = st.builds(
    dom::InsertStatement,
)
dom::DeleteStatement_strategy = st.builds(
    dom::DeleteStatement,
    name=
        safe_text
)
dom::CallableStatement_strategy = st.builds(
    dom::CallableStatement,
    functionCall=
        st.booleans(),
    name=
        safe_text
)
dom::Function_strategy = st.builds(
    dom::Function,
)
dom::ApplicationSession_strategy = st.builds(
    dom::ApplicationSession,
)
DaoFeature_strategy = st.builds(
    DaoFeature,
)
dom::SqlType_strategy = st.builds(
    dom::SqlType,
)
dom::OneToOne_strategy = st.builds(
    dom::OneToOne,
)
dom::ManyToOne_strategy = st.builds(
    dom::ManyToOne,
    columnName=
        safe_text,
    derived=
        st.booleans()
)
dom::Column_strategy = st.builds(
    dom::Column,
    columnName=
        safe_text
)
dom::DataBaseConstraint_strategy = st.builds(
    dom::DataBaseConstraint,
    type=
        safe_text,
    name=
        safe_text
)
dom::QlStatement_strategy = st.builds(
    dom::QlStatement,
)
dom::QueryParameter_strategy = st.builds(
    dom::QueryParameter,
)
dom::ManyToMany_strategy = st.builds(
    dom::ManyToMany,
    columnName=
        safe_text,
    inverse=
        st.booleans(),
    tableName=
        safe_text
)
dom::OneToMany_strategy = st.builds(
    dom::OneToMany,
    columnName=
        safe_text
)
dom::QueryOperation_strategy = st.builds(
    dom::QueryOperation,
)
dom::DaoFeature_strategy = st.builds(
    dom::DaoFeature,
)
dom::AttributeSortOrder_strategy = st.builds(
    dom::AttributeSortOrder,
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
dom::ValidatorReference_strategy = st.builds(
    dom::ValidatorReference,
)
dom::Constraint_strategy = st.builds(
    dom::Constraint,
)
dom::BoolLiteral_strategy = st.builds(
    dom::BoolLiteral,
)
ExpressionFlag_strategy = st.builds(
    ExpressionFlag,
)
dom::AvailableFlag_strategy = st.builds(
    dom::AvailableFlag,
)
dom::ReadOnlyFlag_strategy = st.builds(
    dom::ReadOnlyFlag,
)
dom::RequiredFlag_strategy = st.builds(
    dom::RequiredFlag,
)
dom::EqualityExpr_strategy = st.builds(
    dom::EqualityExpr,
)
AttributeFlag_strategy = st.builds(
    AttributeFlag,
)
dom::TransientFlag_strategy = st.builds(
    dom::TransientFlag,
)
dom::DerivedFlag_strategy = st.builds(
    dom::DerivedFlag,
)
dom::ExpressionFlag_strategy = st.builds(
    dom::ExpressionFlag,
)
AttributeProperty_strategy = st.builds(
    AttributeProperty,
)
dom::AttributeTextProperty_strategy = st.builds(
    dom::AttributeTextProperty,
    labelText=
        safe_text,
    tooltipText=
        safe_text,
    unitText=
        safe_text,
    hstoreColumn=
        safe_text
)
dom::AttributeValidationProperty_strategy = st.builds(
    dom::AttributeValidationProperty,
)
dom::AttributeFlag_strategy = st.builds(
    dom::AttributeFlag,
)
dom::IncrementerReference_strategy = st.builds(
    dom::IncrementerReference,
)
dom::DataTypeAndTypeParameter_strategy = st.builds(
    dom::DataTypeAndTypeParameter,
)
dom::PropertyMapping_strategy = st.builds(
    dom::PropertyMapping,
    toRight=
        st.booleans(),
    toLeft=
        st.booleans(),
    biDirectional=
        st.booleans()
)
dom::ConditionsBlock_strategy = st.builds(
    dom::ConditionsBlock,
)
dom::AttributeGroup_strategy = st.builds(
    dom::AttributeGroup,
    sortorder=
        st.booleans(),
    key=
        st.booleans(),
    unique=
        st.booleans(),
    filter=
        st.booleans(),
    name=
        safe_text
)
PresentableFeature_strategy = st.builds(
    PresentableFeature,
)
dom::FeatureReference_strategy = st.builds(
    dom::FeatureReference,
    all=
        st.booleans()
)
ComplexType_strategy = st.builds(
    ComplexType,
)
dom::Entity_strategy = st.builds(
    dom::Entity,
)
dom::ValueObject_strategy = st.builds(
    dom::ValueObject,
)
dom::Mapper_strategy = st.builds(
    dom::Mapper,
    toLeft=
        st.booleans(),
    toRight=
        st.booleans(),
    biDirectional=
        st.booleans()
)
dom::AttributeProperty_strategy = st.builds(
    dom::AttributeProperty,
)
dom::DataView_strategy = st.builds(
    dom::DataView,
)
dom::Type_strategy = st.builds(
    dom::Type,
)
QueryParameterReference_strategy = st.builds(
    QueryParameterReference,
)
dom::IElementWithNoName_strategy = st.builds(
    dom::IElementWithNoName,
    noName=
        safe_text
)
dom::Attribute_strategy = st.builds(
    dom::Attribute,
    identifier=
        st.booleans(),
    derived=
        st.booleans(),
    readOnly=
        st.booleans(),
    transient=
        st.booleans(),
    reference=
        st.booleans(),
    defaultValue=
        safe_text,
    composition=
        st.booleans(),
    required=
        st.booleans(),
    version=
        st.booleans(),
    dataTypeName=
        safe_text,
    many=
        st.booleans()
)
QueryParameter_strategy = st.builds(
    QueryParameter,
)
dom::Parameter_strategy = st.builds(
    dom::Parameter,
    name=
        safe_text,
    many=
        st.booleans()
)
dom::Expression_strategy = st.builds(
    dom::Expression,
)
dom::DaoOperation_strategy = st.builds(
    dom::DaoOperation,
    many=
        st.booleans(),
    name=
        safe_text
)
dom::Dao_strategy = st.builds(
    dom::Dao,
    tableName=
        safe_text,
    discriminator=
        safe_text,
    qualifier=
        safe_text
)
dom::DelegateOperation_strategy = st.builds(
    dom::DelegateOperation,
    name=
        safe_text,
    crudOperationType=
        safe_text,
    many=
        st.booleans()
)

@given(instance=dom::PresentableFeature_strategy)
@settings(max_examples=50)
def test_dom::presentablefeature_instantiation(instance):
    assert isinstance(instance, dom::PresentableFeature)

@given(instance=dom::PresentableFeature_strategy)
def test_dom::presentablefeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::PresentableFeature_strategy)
def test_dom::presentablefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::WhenClause_strategy)
@settings(max_examples=50)
def test_dom::whenclause_instantiation(instance):
    assert isinstance(instance, dom::WhenClause)

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=dom::IntegerLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::integerliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::IntegerLiteralValue)

@given(instance=dom::IntegerLiteralValue_strategy)
def test_dom::integerliteralvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dom::IntegerLiteralValue_strategy)
def test_dom::integerliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom::EmptyLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::emptyliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::EmptyLiteralValue)

@given(instance=dom::RealLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::realliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::RealLiteralValue)

@given(instance=dom::RealLiteralValue_strategy)
def test_dom::realliteralvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dom::RealLiteralValue_strategy)
def test_dom::realliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom::NullLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::nullliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::NullLiteralValue)

@given(instance=dom::BooleanLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::booleanliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::BooleanLiteralValue)

@given(instance=dom::BooleanLiteralValue_strategy)
def test_dom::booleanliteralvalue_isTrue_type(instance):
    assert isinstance(instance.isTrue, bool)


@given(instance=dom::BooleanLiteralValue_strategy)
def test_dom::booleanliteralvalue_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=dom::AltWhenClause_strategy)
@settings(max_examples=50)
def test_dom::altwhenclause_instantiation(instance):
    assert isinstance(instance, dom::AltWhenClause)

@given(instance=dom::StringLiteralValue_strategy)
@settings(max_examples=50)
def test_dom::stringliteralvalue_instantiation(instance):
    assert isinstance(instance, dom::StringLiteralValue)

@given(instance=dom::StringLiteralValue_strategy)
def test_dom::stringliteralvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dom::StringLiteralValue_strategy)
def test_dom::stringliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom::QueryParameterReference_strategy)
@settings(max_examples=50)
def test_dom::queryparameterreference_instantiation(instance):
    assert isinstance(instance, dom::QueryParameterReference)

@given(instance=JoinEntity_strategy)
@settings(max_examples=50)
def test_joinentity_instantiation(instance):
    assert isinstance(instance, JoinEntity)

@given(instance=FromRange_strategy)
@settings(max_examples=50)
def test_fromrange_instantiation(instance):
    assert isinstance(instance, FromRange)

@given(instance=dom::InClass_strategy)
@settings(max_examples=50)
def test_dom::inclass_instantiation(instance):
    assert isinstance(instance, dom::InClass)

@given(instance=dom::InClass_strategy)
def test_dom::inclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::InClass_strategy)
def test_dom::inclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::InClass_strategy)
def test_dom::inclass_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=dom::InClass_strategy)
def test_dom::inclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dom::InCollection_strategy)
@settings(max_examples=50)
def test_dom::incollection_instantiation(instance):
    assert isinstance(instance, dom::InCollection)

@given(instance=dom::InCollection_strategy)
def test_dom::incollection_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=dom::InCollection_strategy)
def test_dom::incollection_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=dom::InCollection_strategy)
def test_dom::incollection_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=dom::InCollection_strategy)
def test_dom::incollection_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=dom::Dependant_strategy)
@settings(max_examples=50)
def test_dom::dependant_instantiation(instance):
    assert isinstance(instance, dom::Dependant)

@given(instance=Dependant_strategy)
@settings(max_examples=50)
def test_dependant_instantiation(instance):
    assert isinstance(instance, Dependant)

@given(instance=DaoOperation_strategy)
@settings(max_examples=50)
def test_daooperation_instantiation(instance):
    assert isinstance(instance, DaoOperation)

@given(instance=dom::SimpleType_strategy)
@settings(max_examples=50)
def test_dom::simpletype_instantiation(instance):
    assert isinstance(instance, dom::SimpleType)

@given(instance=IDocumentable_strategy)
@settings(max_examples=50)
def test_idocumentable_instantiation(instance):
    assert isinstance(instance, IDocumentable)

@given(instance=dom::Operation_strategy)
@settings(max_examples=50)
def test_dom::operation_instantiation(instance):
    assert isinstance(instance, dom::Operation)

@given(instance=dom::Operation_strategy)
def test_dom::operation_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=dom::Operation_strategy)
def test_dom::operation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=ReferenceableByXmadslVariable_strategy)
@settings(max_examples=50)
def test_referenceablebyxmadslvariable_instantiation(instance):
    assert isinstance(instance, ReferenceableByXmadslVariable)

@given(instance=dom::Property_strategy)
@settings(max_examples=50)
def test_dom::property_instantiation(instance):
    assert isinstance(instance, dom::Property)

@given(instance=dom::Property_strategy)
def test_dom::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::Property_strategy)
def test_dom::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::Property_strategy)
def test_dom::property_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=dom::Property_strategy)
def test_dom::property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=dom::Service_strategy)
@settings(max_examples=50)
def test_dom::service_instantiation(instance):
    assert isinstance(instance, dom::Service)

@given(instance=dom::ComplexType_strategy)
@settings(max_examples=50)
def test_dom::complextype_instantiation(instance):
    assert isinstance(instance, dom::ComplexType)

@given(instance=dom::FromClass_strategy)
@settings(max_examples=50)
def test_dom::fromclass_instantiation(instance):
    assert isinstance(instance, dom::FromClass)

@given(instance=dom::FromClass_strategy)
def test_dom::fromclass_popertyFetch_type(instance):
    assert isinstance(instance.popertyFetch, bool)


@given(instance=dom::FromClass_strategy)
def test_dom::fromclass_popertyFetch_setter(instance):
    original = instance.popertyFetch
    instance.popertyFetch = original
    assert instance.popertyFetch == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dom::SubQuery_strategy)
@settings(max_examples=50)
def test_dom::subquery_instantiation(instance):
    assert isinstance(instance, dom::SubQuery)

@given(instance=dom::LikeExpression_strategy)
@settings(max_examples=50)
def test_dom::likeexpression_instantiation(instance):
    assert isinstance(instance, dom::LikeExpression)

@given(instance=dom::LikeExpression_strategy)
def test_dom::likeexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::LikeExpression_strategy)
def test_dom::likeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::LikeExpression_strategy)
def test_dom::likeexpression_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=dom::LikeExpression_strategy)
def test_dom::likeexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dom::AliasedExpression_strategy)
@settings(max_examples=50)
def test_dom::aliasedexpression_instantiation(instance):
    assert isinstance(instance, dom::AliasedExpression)

@given(instance=dom::AliasedExpression_strategy)
def test_dom::aliasedexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::AliasedExpression_strategy)
def test_dom::aliasedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::BinaryExpression_strategy)
@settings(max_examples=50)
def test_dom::binaryexpression_instantiation(instance):
    assert isinstance(instance, dom::BinaryExpression)

@given(instance=dom::BinaryExpression_strategy)
def test_dom::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::BinaryExpression_strategy)
def test_dom::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::CollectionFunction_strategy)
@settings(max_examples=50)
def test_dom::collectionfunction_instantiation(instance):
    assert isinstance(instance, dom::CollectionFunction)

@given(instance=dom::CollectionFunction_strategy)
def test_dom::collectionfunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=dom::CollectionFunction_strategy)
def test_dom::collectionfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom::NotExpression_strategy)
@settings(max_examples=50)
def test_dom::notexpression_instantiation(instance):
    assert isinstance(instance, dom::NotExpression)

@given(instance=dom::CastFunction_strategy)
@settings(max_examples=50)
def test_dom::castfunction_instantiation(instance):
    assert isinstance(instance, dom::CastFunction)

@given(instance=dom::CastFunction_strategy)
def test_dom::castfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::CastFunction_strategy)
def test_dom::castfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::CastFunction_strategy)
def test_dom::castfunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=dom::CastFunction_strategy)
def test_dom::castfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom::QueryParameterValue_strategy)
@settings(max_examples=50)
def test_dom::queryparametervalue_instantiation(instance):
    assert isinstance(instance, dom::QueryParameterValue)

@given(instance=dom::CaseExpression_strategy)
@settings(max_examples=50)
def test_dom::caseexpression_instantiation(instance):
    assert isinstance(instance, dom::CaseExpression)

@given(instance=dom::UnaryExpression_strategy)
@settings(max_examples=50)
def test_dom::unaryexpression_instantiation(instance):
    assert isinstance(instance, dom::UnaryExpression)

@given(instance=dom::UnaryExpression_strategy)
def test_dom::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::UnaryExpression_strategy)
def test_dom::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_dom::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, dom::ParenthesizedExpression)

@given(instance=dom::TrimFunction_strategy)
@settings(max_examples=50)
def test_dom::trimfunction_instantiation(instance):
    assert isinstance(instance, dom::TrimFunction)

@given(instance=dom::TrimFunction_strategy)
def test_dom::trimfunction_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=dom::TrimFunction_strategy)
def test_dom::trimfunction_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=dom::TrimFunction_strategy)
def test_dom::trimfunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=dom::TrimFunction_strategy)
def test_dom::trimfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom::MemberOfExpression_strategy)
@settings(max_examples=50)
def test_dom::memberofexpression_instantiation(instance):
    assert isinstance(instance, dom::MemberOfExpression)

@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_memberOf_type(instance):
    assert isinstance(instance.memberOf, str)


@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_memberOf_setter(instance):
    original = instance.memberOf
    instance.memberOf = original
    assert instance.memberOf == original

@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::MemberOfExpression_strategy)
def test_dom::memberofexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::FunctionCall_strategy)
@settings(max_examples=50)
def test_dom::functioncall_instantiation(instance):
    assert isinstance(instance, dom::FunctionCall)

@given(instance=dom::FunctionCall_strategy)
def test_dom::functioncall_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=dom::FunctionCall_strategy)
def test_dom::functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom::InExpression_strategy)
@settings(max_examples=50)
def test_dom::inexpression_instantiation(instance):
    assert isinstance(instance, dom::InExpression)

@given(instance=dom::InExpression_strategy)
def test_dom::inexpression_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=dom::InExpression_strategy)
def test_dom::inexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dom::InExpression_strategy)
def test_dom::inexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::InExpression_strategy)
def test_dom::inexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::AggregateFunction_strategy)
@settings(max_examples=50)
def test_dom::aggregatefunction_instantiation(instance):
    assert isinstance(instance, dom::AggregateFunction)

@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=dom::AggregateFunction_strategy)
def test_dom::aggregatefunction_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=dom::LiteralValue_strategy)
@settings(max_examples=50)
def test_dom::literalvalue_instantiation(instance):
    assert isinstance(instance, dom::LiteralValue)

@given(instance=dom::QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_dom::quantifiedexpression_instantiation(instance):
    assert isinstance(instance, dom::QuantifiedExpression)

@given(instance=dom::QuantifiedExpression_strategy)
def test_dom::quantifiedexpression_quantifier_type(instance):
    assert isinstance(instance.quantifier, str)


@given(instance=dom::QuantifiedExpression_strategy)
def test_dom::quantifiedexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original

@given(instance=dom::QuantifiedExpression_strategy)
def test_dom::quantifiedexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::QuantifiedExpression_strategy)
def test_dom::quantifiedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::BetweenExpression_strategy)
@settings(max_examples=50)
def test_dom::betweenexpression_instantiation(instance):
    assert isinstance(instance, dom::BetweenExpression)

@given(instance=dom::BetweenExpression_strategy)
def test_dom::betweenexpression_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=dom::BetweenExpression_strategy)
def test_dom::betweenexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dom::BetweenExpression_strategy)
def test_dom::betweenexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dom::BetweenExpression_strategy)
def test_dom::betweenexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom::JoinEntity_strategy)
@settings(max_examples=50)
def test_dom::joinentity_instantiation(instance):
    assert isinstance(instance, dom::JoinEntity)

@given(instance=dom::JoinEntity_strategy)
def test_dom::joinentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::JoinEntity_strategy)
def test_dom::joinentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::InCollectionElements_strategy)
@settings(max_examples=50)
def test_dom::incollectionelements_instantiation(instance):
    assert isinstance(instance, dom::InCollectionElements)

@given(instance=dom::InCollectionElements_strategy)
def test_dom::incollectionelements_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::InCollectionElements_strategy)
def test_dom::incollectionelements_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::InCollectionElements_strategy)
def test_dom::incollectionelements_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=dom::InCollectionElements_strategy)
def test_dom::incollectionelements_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=dom::PropertyValue_strategy)
@settings(max_examples=50)
def test_dom::propertyvalue_instantiation(instance):
    assert isinstance(instance, dom::PropertyValue)

@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_segments_type(instance):
    assert isinstance(instance.segments, str)


@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_classProperty_type(instance):
    assert isinstance(instance.classProperty, bool)


@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_classProperty_setter(instance):
    original = instance.classProperty
    instance.classProperty = original
    assert instance.classProperty == original

@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::PropertyValue_strategy)
def test_dom::propertyvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::PropertyAssignment_strategy)
@settings(max_examples=50)
def test_dom::propertyassignment_instantiation(instance):
    assert isinstance(instance, dom::PropertyAssignment)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=dom::SelectClass_strategy)
@settings(max_examples=50)
def test_dom::selectclass_instantiation(instance):
    assert isinstance(instance, dom::SelectClass)

@given(instance=dom::SelectClass_strategy)
def test_dom::selectclass_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=dom::SelectClass_strategy)
def test_dom::selectclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dom::SelectObject_strategy)
@settings(max_examples=50)
def test_dom::selectobject_instantiation(instance):
    assert isinstance(instance, dom::SelectObject)

@given(instance=dom::SelectObject_strategy)
def test_dom::selectobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::SelectObject_strategy)
def test_dom::selectobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::SelectProperties_strategy)
@settings(max_examples=50)
def test_dom::selectproperties_instantiation(instance):
    assert isinstance(instance, dom::SelectProperties)

@given(instance=dom::SelectProperties_strategy)
def test_dom::selectproperties_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=dom::SelectProperties_strategy)
def test_dom::selectproperties_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=dom::SortOrderElement_strategy)
@settings(max_examples=50)
def test_dom::sortorderelement_instantiation(instance):
    assert isinstance(instance, dom::SortOrderElement)

@given(instance=dom::SortOrderElement_strategy)
def test_dom::sortorderelement_sortOrder_type(instance):
    assert isinstance(instance.sortOrder, str)


@given(instance=dom::SortOrderElement_strategy)
def test_dom::sortorderelement_sortOrder_setter(instance):
    original = instance.sortOrder
    instance.sortOrder = original
    assert instance.sortOrder == original

@given(instance=dom::Join_strategy)
@settings(max_examples=50)
def test_dom::join_instantiation(instance):
    assert isinstance(instance, dom::Join)

@given(instance=dom::Join_strategy)
def test_dom::join_fetch_type(instance):
    assert isinstance(instance.fetch, bool)


@given(instance=dom::Join_strategy)
def test_dom::join_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original

@given(instance=dom::Join_strategy)
def test_dom::join_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dom::Join_strategy)
def test_dom::join_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dom::Join_strategy)
def test_dom::join_propertyFetch_type(instance):
    assert isinstance(instance.propertyFetch, bool)


@given(instance=dom::Join_strategy)
def test_dom::join_propertyFetch_setter(instance):
    original = instance.propertyFetch
    instance.propertyFetch = original
    assert instance.propertyFetch == original

@given(instance=dom::FromRange_strategy)
@settings(max_examples=50)
def test_dom::fromrange_instantiation(instance):
    assert isinstance(instance, dom::FromRange)

@given(instance=dom::CallOutputParameter_strategy)
@settings(max_examples=50)
def test_dom::calloutputparameter_instantiation(instance):
    assert isinstance(instance, dom::CallOutputParameter)

@given(instance=dom::CallOutputParameter_strategy)
def test_dom::calloutputparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::CallOutputParameter_strategy)
def test_dom::calloutputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::CallInputParameter_strategy)
@settings(max_examples=50)
def test_dom::callinputparameter_instantiation(instance):
    assert isinstance(instance, dom::CallInputParameter)

@given(instance=dom::CallInputParameter_strategy)
def test_dom::callinputparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::CallInputParameter_strategy)
def test_dom::callinputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QlStatement_strategy)
@settings(max_examples=50)
def test_qlstatement_instantiation(instance):
    assert isinstance(instance, QlStatement)

@given(instance=dom::SelectStatement_strategy)
@settings(max_examples=50)
def test_dom::selectstatement_instantiation(instance):
    assert isinstance(instance, dom::SelectStatement)

@given(instance=dom::UpdateStatement_strategy)
@settings(max_examples=50)
def test_dom::updatestatement_instantiation(instance):
    assert isinstance(instance, dom::UpdateStatement)

@given(instance=dom::UpdateStatement_strategy)
def test_dom::updatestatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::UpdateStatement_strategy)
def test_dom::updatestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::UpdateStatement_strategy)
def test_dom::updatestatement_versioned_type(instance):
    assert isinstance(instance.versioned, bool)


@given(instance=dom::UpdateStatement_strategy)
def test_dom::updatestatement_versioned_setter(instance):
    original = instance.versioned
    instance.versioned = original
    assert instance.versioned == original

@given(instance=dom::InsertStatement_strategy)
@settings(max_examples=50)
def test_dom::insertstatement_instantiation(instance):
    assert isinstance(instance, dom::InsertStatement)

@given(instance=dom::DeleteStatement_strategy)
@settings(max_examples=50)
def test_dom::deletestatement_instantiation(instance):
    assert isinstance(instance, dom::DeleteStatement)

@given(instance=dom::DeleteStatement_strategy)
def test_dom::deletestatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::DeleteStatement_strategy)
def test_dom::deletestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::CallableStatement_strategy)
@settings(max_examples=50)
def test_dom::callablestatement_instantiation(instance):
    assert isinstance(instance, dom::CallableStatement)

@given(instance=dom::CallableStatement_strategy)
def test_dom::callablestatement_functionCall_type(instance):
    assert isinstance(instance.functionCall, bool)


@given(instance=dom::CallableStatement_strategy)
def test_dom::callablestatement_functionCall_setter(instance):
    original = instance.functionCall
    instance.functionCall = original
    assert instance.functionCall == original

@given(instance=dom::CallableStatement_strategy)
def test_dom::callablestatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::CallableStatement_strategy)
def test_dom::callablestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::Function_strategy)
@settings(max_examples=50)
def test_dom::function_instantiation(instance):
    assert isinstance(instance, dom::Function)

@given(instance=dom::ApplicationSession_strategy)
@settings(max_examples=50)
def test_dom::applicationsession_instantiation(instance):
    assert isinstance(instance, dom::ApplicationSession)

@given(instance=DaoFeature_strategy)
@settings(max_examples=50)
def test_daofeature_instantiation(instance):
    assert isinstance(instance, DaoFeature)

@given(instance=dom::SqlType_strategy)
@settings(max_examples=50)
def test_dom::sqltype_instantiation(instance):
    assert isinstance(instance, dom::SqlType)

@given(instance=dom::OneToOne_strategy)
@settings(max_examples=50)
def test_dom::onetoone_instantiation(instance):
    assert isinstance(instance, dom::OneToOne)

@given(instance=dom::ManyToOne_strategy)
@settings(max_examples=50)
def test_dom::manytoone_instantiation(instance):
    assert isinstance(instance, dom::ManyToOne)

@given(instance=dom::ManyToOne_strategy)
def test_dom::manytoone_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=dom::ManyToOne_strategy)
def test_dom::manytoone_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom::ManyToOne_strategy)
def test_dom::manytoone_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=dom::ManyToOne_strategy)
def test_dom::manytoone_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=dom::Column_strategy)
@settings(max_examples=50)
def test_dom::column_instantiation(instance):
    assert isinstance(instance, dom::Column)

@given(instance=dom::Column_strategy)
def test_dom::column_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=dom::Column_strategy)
def test_dom::column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom::DataBaseConstraint_strategy)
@settings(max_examples=50)
def test_dom::databaseconstraint_instantiation(instance):
    assert isinstance(instance, dom::DataBaseConstraint)

@given(instance=dom::DataBaseConstraint_strategy)
def test_dom::databaseconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dom::DataBaseConstraint_strategy)
def test_dom::databaseconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dom::DataBaseConstraint_strategy)
def test_dom::databaseconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::DataBaseConstraint_strategy)
def test_dom::databaseconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::QlStatement_strategy)
@settings(max_examples=50)
def test_dom::qlstatement_instantiation(instance):
    assert isinstance(instance, dom::QlStatement)

@given(instance=dom::QueryParameter_strategy)
@settings(max_examples=50)
def test_dom::queryparameter_instantiation(instance):
    assert isinstance(instance, dom::QueryParameter)

@given(instance=dom::ManyToMany_strategy)
@settings(max_examples=50)
def test_dom::manytomany_instantiation(instance):
    assert isinstance(instance, dom::ManyToMany)

@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_inverse_type(instance):
    assert isinstance(instance.inverse, bool)


@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=dom::ManyToMany_strategy)
def test_dom::manytomany_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=dom::OneToMany_strategy)
@settings(max_examples=50)
def test_dom::onetomany_instantiation(instance):
    assert isinstance(instance, dom::OneToMany)

@given(instance=dom::OneToMany_strategy)
def test_dom::onetomany_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=dom::OneToMany_strategy)
def test_dom::onetomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom::QueryOperation_strategy)
@settings(max_examples=50)
def test_dom::queryoperation_instantiation(instance):
    assert isinstance(instance, dom::QueryOperation)

@given(instance=dom::DaoFeature_strategy)
@settings(max_examples=50)
def test_dom::daofeature_instantiation(instance):
    assert isinstance(instance, dom::DaoFeature)

@given(instance=dom::AttributeSortOrder_strategy)
@settings(max_examples=50)
def test_dom::attributesortorder_instantiation(instance):
    assert isinstance(instance, dom::AttributeSortOrder)

@given(instance=dom::AttributeSortOrder_strategy)
def test_dom::attributesortorder_desc_type(instance):
    assert isinstance(instance.desc, bool)


@given(instance=dom::AttributeSortOrder_strategy)
def test_dom::attributesortorder_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=dom::AttributeSortOrder_strategy)
def test_dom::attributesortorder_asc_type(instance):
    assert isinstance(instance.asc, bool)


@given(instance=dom::AttributeSortOrder_strategy)
def test_dom::attributesortorder_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=dom::ValidatorReference_strategy)
@settings(max_examples=50)
def test_dom::validatorreference_instantiation(instance):
    assert isinstance(instance, dom::ValidatorReference)

@given(instance=dom::Constraint_strategy)
@settings(max_examples=50)
def test_dom::constraint_instantiation(instance):
    assert isinstance(instance, dom::Constraint)

@given(instance=dom::BoolLiteral_strategy)
@settings(max_examples=50)
def test_dom::boolliteral_instantiation(instance):
    assert isinstance(instance, dom::BoolLiteral)

@given(instance=ExpressionFlag_strategy)
@settings(max_examples=50)
def test_expressionflag_instantiation(instance):
    assert isinstance(instance, ExpressionFlag)

@given(instance=dom::AvailableFlag_strategy)
@settings(max_examples=50)
def test_dom::availableflag_instantiation(instance):
    assert isinstance(instance, dom::AvailableFlag)

@given(instance=dom::ReadOnlyFlag_strategy)
@settings(max_examples=50)
def test_dom::readonlyflag_instantiation(instance):
    assert isinstance(instance, dom::ReadOnlyFlag)

@given(instance=dom::RequiredFlag_strategy)
@settings(max_examples=50)
def test_dom::requiredflag_instantiation(instance):
    assert isinstance(instance, dom::RequiredFlag)

@given(instance=dom::EqualityExpr_strategy)
@settings(max_examples=50)
def test_dom::equalityexpr_instantiation(instance):
    assert isinstance(instance, dom::EqualityExpr)

@given(instance=AttributeFlag_strategy)
@settings(max_examples=50)
def test_attributeflag_instantiation(instance):
    assert isinstance(instance, AttributeFlag)

@given(instance=dom::TransientFlag_strategy)
@settings(max_examples=50)
def test_dom::transientflag_instantiation(instance):
    assert isinstance(instance, dom::TransientFlag)

@given(instance=dom::DerivedFlag_strategy)
@settings(max_examples=50)
def test_dom::derivedflag_instantiation(instance):
    assert isinstance(instance, dom::DerivedFlag)

@given(instance=dom::ExpressionFlag_strategy)
@settings(max_examples=50)
def test_dom::expressionflag_instantiation(instance):
    assert isinstance(instance, dom::ExpressionFlag)

@given(instance=AttributeProperty_strategy)
@settings(max_examples=50)
def test_attributeproperty_instantiation(instance):
    assert isinstance(instance, AttributeProperty)

@given(instance=dom::AttributeTextProperty_strategy)
@settings(max_examples=50)
def test_dom::attributetextproperty_instantiation(instance):
    assert isinstance(instance, dom::AttributeTextProperty)

@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_labelText_type(instance):
    assert isinstance(instance.labelText, str)


@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original

@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_tooltipText_type(instance):
    assert isinstance(instance.tooltipText, str)


@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original

@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_unitText_type(instance):
    assert isinstance(instance.unitText, str)


@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_unitText_setter(instance):
    original = instance.unitText
    instance.unitText = original
    assert instance.unitText == original

@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_hstoreColumn_type(instance):
    assert isinstance(instance.hstoreColumn, str)


@given(instance=dom::AttributeTextProperty_strategy)
def test_dom::attributetextproperty_hstoreColumn_setter(instance):
    original = instance.hstoreColumn
    instance.hstoreColumn = original
    assert instance.hstoreColumn == original

@given(instance=dom::AttributeValidationProperty_strategy)
@settings(max_examples=50)
def test_dom::attributevalidationproperty_instantiation(instance):
    assert isinstance(instance, dom::AttributeValidationProperty)

@given(instance=dom::AttributeFlag_strategy)
@settings(max_examples=50)
def test_dom::attributeflag_instantiation(instance):
    assert isinstance(instance, dom::AttributeFlag)

@given(instance=dom::IncrementerReference_strategy)
@settings(max_examples=50)
def test_dom::incrementerreference_instantiation(instance):
    assert isinstance(instance, dom::IncrementerReference)

@given(instance=dom::DataTypeAndTypeParameter_strategy)
@settings(max_examples=50)
def test_dom::datatypeandtypeparameter_instantiation(instance):
    assert isinstance(instance, dom::DataTypeAndTypeParameter)

@given(instance=dom::PropertyMapping_strategy)
@settings(max_examples=50)
def test_dom::propertymapping_instantiation(instance):
    assert isinstance(instance, dom::PropertyMapping)

@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_toRight_type(instance):
    assert isinstance(instance.toRight, bool)


@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original

@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_toLeft_type(instance):
    assert isinstance(instance.toLeft, bool)


@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original

@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_biDirectional_type(instance):
    assert isinstance(instance.biDirectional, bool)


@given(instance=dom::PropertyMapping_strategy)
def test_dom::propertymapping_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original

@given(instance=dom::ConditionsBlock_strategy)
@settings(max_examples=50)
def test_dom::conditionsblock_instantiation(instance):
    assert isinstance(instance, dom::ConditionsBlock)

@given(instance=dom::AttributeGroup_strategy)
@settings(max_examples=50)
def test_dom::attributegroup_instantiation(instance):
    assert isinstance(instance, dom::AttributeGroup)

@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_sortorder_type(instance):
    assert isinstance(instance.sortorder, bool)


@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_sortorder_setter(instance):
    original = instance.sortorder
    instance.sortorder = original
    assert instance.sortorder == original

@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_key_type(instance):
    assert isinstance(instance.key, bool)


@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_filter_type(instance):
    assert isinstance(instance.filter, bool)


@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::AttributeGroup_strategy)
def test_dom::attributegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PresentableFeature_strategy)
@settings(max_examples=50)
def test_presentablefeature_instantiation(instance):
    assert isinstance(instance, PresentableFeature)

@given(instance=dom::FeatureReference_strategy)
@settings(max_examples=50)
def test_dom::featurereference_instantiation(instance):
    assert isinstance(instance, dom::FeatureReference)

@given(instance=dom::FeatureReference_strategy)
def test_dom::featurereference_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=dom::FeatureReference_strategy)
def test_dom::featurereference_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=dom::Entity_strategy)
@settings(max_examples=50)
def test_dom::entity_instantiation(instance):
    assert isinstance(instance, dom::Entity)

@given(instance=dom::ValueObject_strategy)
@settings(max_examples=50)
def test_dom::valueobject_instantiation(instance):
    assert isinstance(instance, dom::ValueObject)

@given(instance=dom::Mapper_strategy)
@settings(max_examples=50)
def test_dom::mapper_instantiation(instance):
    assert isinstance(instance, dom::Mapper)

@given(instance=dom::Mapper_strategy)
def test_dom::mapper_toLeft_type(instance):
    assert isinstance(instance.toLeft, bool)


@given(instance=dom::Mapper_strategy)
def test_dom::mapper_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original

@given(instance=dom::Mapper_strategy)
def test_dom::mapper_toRight_type(instance):
    assert isinstance(instance.toRight, bool)


@given(instance=dom::Mapper_strategy)
def test_dom::mapper_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original

@given(instance=dom::Mapper_strategy)
def test_dom::mapper_biDirectional_type(instance):
    assert isinstance(instance.biDirectional, bool)


@given(instance=dom::Mapper_strategy)
def test_dom::mapper_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original

@given(instance=dom::AttributeProperty_strategy)
@settings(max_examples=50)
def test_dom::attributeproperty_instantiation(instance):
    assert isinstance(instance, dom::AttributeProperty)

@given(instance=dom::DataView_strategy)
@settings(max_examples=50)
def test_dom::dataview_instantiation(instance):
    assert isinstance(instance, dom::DataView)

@given(instance=dom::Type_strategy)
@settings(max_examples=50)
def test_dom::type_instantiation(instance):
    assert isinstance(instance, dom::Type)

@given(instance=QueryParameterReference_strategy)
@settings(max_examples=50)
def test_queryparameterreference_instantiation(instance):
    assert isinstance(instance, QueryParameterReference)

@given(instance=dom::IElementWithNoName_strategy)
@settings(max_examples=50)
def test_dom::ielementwithnoname_instantiation(instance):
    assert isinstance(instance, dom::IElementWithNoName)

@given(instance=dom::IElementWithNoName_strategy)
def test_dom::ielementwithnoname_noName_type(instance):
    assert isinstance(instance.noName, str)


@given(instance=dom::IElementWithNoName_strategy)
def test_dom::ielementwithnoname_noName_setter(instance):
    original = instance.noName
    instance.noName = original
    assert instance.noName == original

@given(instance=dom::Attribute_strategy)
@settings(max_examples=50)
def test_dom::attribute_instantiation(instance):
    assert isinstance(instance, dom::Attribute)

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_identifier_type(instance):
    assert isinstance(instance.identifier, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_reference_type(instance):
    assert isinstance(instance.reference, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_composition_type(instance):
    assert isinstance(instance.composition, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_version_type(instance):
    assert isinstance(instance.version, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_dataTypeName_type(instance):
    assert isinstance(instance.dataTypeName, str)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_dataTypeName_setter(instance):
    original = instance.dataTypeName
    instance.dataTypeName = original
    assert instance.dataTypeName == original

@given(instance=dom::Attribute_strategy)
def test_dom::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=dom::Attribute_strategy)
def test_dom::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=QueryParameter_strategy)
@settings(max_examples=50)
def test_queryparameter_instantiation(instance):
    assert isinstance(instance, QueryParameter)

@given(instance=dom::Parameter_strategy)
@settings(max_examples=50)
def test_dom::parameter_instantiation(instance):
    assert isinstance(instance, dom::Parameter)

@given(instance=dom::Parameter_strategy)
def test_dom::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::Parameter_strategy)
def test_dom::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::Parameter_strategy)
def test_dom::parameter_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=dom::Parameter_strategy)
def test_dom::parameter_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=dom::Expression_strategy)
@settings(max_examples=50)
def test_dom::expression_instantiation(instance):
    assert isinstance(instance, dom::Expression)

@given(instance=dom::DaoOperation_strategy)
@settings(max_examples=50)
def test_dom::daooperation_instantiation(instance):
    assert isinstance(instance, dom::DaoOperation)

@given(instance=dom::DaoOperation_strategy)
def test_dom::daooperation_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=dom::DaoOperation_strategy)
def test_dom::daooperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=dom::DaoOperation_strategy)
def test_dom::daooperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::DaoOperation_strategy)
def test_dom::daooperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::Dao_strategy)
@settings(max_examples=50)
def test_dom::dao_instantiation(instance):
    assert isinstance(instance, dom::Dao)

@given(instance=dom::Dao_strategy)
def test_dom::dao_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=dom::Dao_strategy)
def test_dom::dao_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=dom::Dao_strategy)
def test_dom::dao_discriminator_type(instance):
    assert isinstance(instance.discriminator, str)


@given(instance=dom::Dao_strategy)
def test_dom::dao_discriminator_setter(instance):
    original = instance.discriminator
    instance.discriminator = original
    assert instance.discriminator == original

@given(instance=dom::Dao_strategy)
def test_dom::dao_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=dom::Dao_strategy)
def test_dom::dao_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=dom::DelegateOperation_strategy)
@settings(max_examples=50)
def test_dom::delegateoperation_instantiation(instance):
    assert isinstance(instance, dom::DelegateOperation)

@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_crudOperationType_type(instance):
    assert isinstance(instance.crudOperationType, str)


@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_crudOperationType_setter(instance):
    original = instance.crudOperationType
    instance.crudOperationType = original
    assert instance.crudOperationType == original

@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=dom::DelegateOperation_strategy)
def test_dom::delegateoperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original
