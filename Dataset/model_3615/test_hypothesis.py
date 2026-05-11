import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RelationshipClause,
    r1::Without,
    r1::With,
    r1::TupleElement,
    AliasedQuerySource,
    r1::RelationshipClause,
    TypeSpecifier,
    r1::ListTypeSpecifier,
    r1::NamedTypeSpecifier,
    r1::TupleTypeSpecifier,
    r1::IntervalTypeSpecifier,
    r1::InstanceElement,
    ExpressionDef,
    r1::FunctionDef,
    ExpressionRef,
    r1::FunctionRef,
    r1::EObject,
    r1::Element,
    NaryExpression,
    r1::Concatenate,
    r1::Coalesce,
    AggregateExpression,
    r1::PopulationStdDev,
    r1::Median,
    r1::StdDev,
    r1::Variance,
    r1::Mode,
    r1::Avg,
    r1::PopulationVariance,
    r1::Max,
    r1::Min,
    r1::Count,
    r1::AnyTrue,
    r1::Sum,
    r1::AllTrue,
    SortByItem,
    r1::ByDirection,
    r1::ByExpression,
    r1::ByColumn,
    Element,
    r1::DefineClause,
    r1::SortByItem,
    r1::CaseItem,
    r1::CodeSystemDef,
    r1::ValueSetDef,
    r1::ReturnClause,
    r1::ParameterDef,
    r1::SortClause,
    r1::OperandDef,
    r1::TypeSpecifier,
    r1::ExpressionDef,
    r1::TupleElementDefinition,
    r1::AliasedQuerySource,
    r1::Expression,
    Expression,
    r1::PositionOf,
    r1::ForEach,
    r1::Code,
    r1::DateTime,
    r1::Quantity,
    r1::AliasRef,
    r1::MinValue,
    r1::CodeSystemRef,
    r1::Interval,
    r1::Null,
    r1::First,
    r1::Case,
    r1::InValueSet,
    r1::Today,
    r1::Substring,
    r1::Current,
    r1::QueryDefineRef,
    r1::Query,
    r1::List,
    r1::TimeOfDay,
    r1::Combine,
    r1::Tuple,
    r1::ValueSetRef,
    r1::Time,
    r1::OperandRef,
    r1::Concept,
    r1::BinaryExpression,
    r1::IndexOf,
    r1::NaryExpression,
    r1::Filter,
    r1::Retrieve,
    r1::Last,
    r1::Property,
    r1::UnaryExpression,
    r1::MaxValue,
    r1::Sort,
    r1::Split,
    r1::Now,
    r1::InCodeSystem,
    r1::Round,
    r1::If,
    r1::ParameterRef,
    r1::IdentifierRef,
    r1::Literal,
    r1::TernaryExpression,
    r1::ExpressionRef,
    r1::Instance,
    r1::AggregateExpression,
    BinaryExpression,
    r1::ProperContains,
    r1::NotEqual,
    r1::Times,
    r1::MeetsAfter,
    r1::Before,
    r1::Overlaps,
    r1::Starts,
    r1::ProperIncludes,
    r1::OverlapsAfter,
    r1::After,
    r1::Multiply,
    r1::Equal,
    r1::Includes,
    r1::ProperIncludedIn,
    r1::Indexer,
    r1::IncludedIn,
    r1::Subtract,
    r1::Intersect,
    r1::SameAs,
    r1::Modulo,
    r1::LessOrEqual,
    r1::Xor,
    r1::SameOrBefore,
    r1::In,
    r1::Matches,
    r1::MeetsBefore,
    r1::GreaterOrEqual,
    r1::CalculateAgeAt,
    r1::OverlapsBefore,
    r1::Less,
    r1::SameOrAfter,
    r1::Greater,
    r1::Ends,
    r1::Meets,
    r1::TruncatedDivide,
    r1::Power,
    r1::Log,
    r1::Except,
    r1::Divide,
    r1::DifferenceBetween,
    r1::And,
    r1::DurationBetween,
    r1::Union,
    r1::Contains,
    r1::ProperIn,
    r1::Or,
    r1::Add,
    UnaryExpression,
    r1::DateFrom,
    r1::Ln,
    r1::IsTrue,
    r1::Exists,
    r1::IsFalse,
    r1::Length,
    r1::Floor,
    r1::TimezoneFrom,
    r1::Lower,
    r1::End,
    r1::Truncate,
    r1::Expand,
    r1::Successor,
    r1::Distinct,
    r1::Negate,
    r1::As,
    r1::Convert,
    r1::Not,
    r1::DateTimeComponentFrom,
    r1::Width,
    r1::Is,
    r1::CalculateAge,
    r1::Ceiling,
    r1::SingletonFrom,
    r1::TimeFrom,
    r1::Collapse,
    r1::Predecessor,
    r1::Upper,
    r1::Start,
    r1::IsNull,
    r1::Abs,
    SortDirection,
    DateTimePrecision,
    AccessModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relationshipclause_is_not_abstract():
    assert not inspect.isabstract(RelationshipClause)


def test_relationshipclause_constructor_exists():
    assert callable(RelationshipClause.__init__)


def test_relationshipclause_constructor_args():
    sig = inspect.signature(RelationshipClause.__init__)
    params = list(sig.parameters.keys())



def test_r1::without_is_not_abstract():
    assert not inspect.isabstract(r1::Without)


def test_r1::without_constructor_exists():
    assert callable(r1::Without.__init__)


def test_r1::without_constructor_args():
    sig = inspect.signature(r1::Without.__init__)
    params = list(sig.parameters.keys())



def test_r1::with_is_not_abstract():
    assert not inspect.isabstract(r1::With)


def test_r1::with_constructor_exists():
    assert callable(r1::With.__init__)


def test_r1::with_constructor_args():
    sig = inspect.signature(r1::With.__init__)
    params = list(sig.parameters.keys())



def test_r1::tupleelement_is_not_abstract():
    assert not inspect.isabstract(r1::TupleElement)


def test_r1::tupleelement_constructor_exists():
    assert callable(r1::TupleElement.__init__)


def test_r1::tupleelement_constructor_args():
    sig = inspect.signature(r1::TupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::tupleelement_has_name():
    assert hasattr(r1::TupleElement, "name")
    descriptor = None
    for klass in r1::TupleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aliasedquerysource_is_not_abstract():
    assert not inspect.isabstract(AliasedQuerySource)


def test_aliasedquerysource_constructor_exists():
    assert callable(AliasedQuerySource.__init__)


def test_aliasedquerysource_constructor_args():
    sig = inspect.signature(AliasedQuerySource.__init__)
    params = list(sig.parameters.keys())



def test_r1::relationshipclause_is_not_abstract():
    assert not inspect.isabstract(r1::RelationshipClause)


def test_r1::relationshipclause_constructor_exists():
    assert callable(r1::RelationshipClause.__init__)


def test_r1::relationshipclause_constructor_args():
    sig = inspect.signature(r1::RelationshipClause.__init__)
    params = list(sig.parameters.keys())



def test_typespecifier_is_not_abstract():
    assert not inspect.isabstract(TypeSpecifier)


def test_typespecifier_constructor_exists():
    assert callable(TypeSpecifier.__init__)


def test_typespecifier_constructor_args():
    sig = inspect.signature(TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1::listtypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1::ListTypeSpecifier)


def test_r1::listtypespecifier_constructor_exists():
    assert callable(r1::ListTypeSpecifier.__init__)


def test_r1::listtypespecifier_constructor_args():
    sig = inspect.signature(r1::ListTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1::namedtypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1::NamedTypeSpecifier)


def test_r1::namedtypespecifier_constructor_exists():
    assert callable(r1::NamedTypeSpecifier.__init__)


def test_r1::namedtypespecifier_constructor_args():
    sig = inspect.signature(r1::NamedTypeSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::namedtypespecifier_has_name():
    assert hasattr(r1::NamedTypeSpecifier, "name")
    descriptor = None
    for klass in r1::NamedTypeSpecifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::tupletypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1::TupleTypeSpecifier)


def test_r1::tupletypespecifier_constructor_exists():
    assert callable(r1::TupleTypeSpecifier.__init__)


def test_r1::tupletypespecifier_constructor_args():
    sig = inspect.signature(r1::TupleTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1::intervaltypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1::IntervalTypeSpecifier)


def test_r1::intervaltypespecifier_constructor_exists():
    assert callable(r1::IntervalTypeSpecifier.__init__)


def test_r1::intervaltypespecifier_constructor_args():
    sig = inspect.signature(r1::IntervalTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1::instanceelement_is_not_abstract():
    assert not inspect.isabstract(r1::InstanceElement)


def test_r1::instanceelement_constructor_exists():
    assert callable(r1::InstanceElement.__init__)


def test_r1::instanceelement_constructor_args():
    sig = inspect.signature(r1::InstanceElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::instanceelement_has_name():
    assert hasattr(r1::InstanceElement, "name")
    descriptor = None
    for klass in r1::InstanceElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressiondef_is_not_abstract():
    assert not inspect.isabstract(ExpressionDef)


def test_expressiondef_constructor_exists():
    assert callable(ExpressionDef.__init__)


def test_expressiondef_constructor_args():
    sig = inspect.signature(ExpressionDef.__init__)
    params = list(sig.parameters.keys())



def test_r1::functiondef_is_not_abstract():
    assert not inspect.isabstract(r1::FunctionDef)


def test_r1::functiondef_constructor_exists():
    assert callable(r1::FunctionDef.__init__)


def test_r1::functiondef_constructor_args():
    sig = inspect.signature(r1::FunctionDef.__init__)
    params = list(sig.parameters.keys())



def test_expressionref_is_not_abstract():
    assert not inspect.isabstract(ExpressionRef)


def test_expressionref_constructor_exists():
    assert callable(ExpressionRef.__init__)


def test_expressionref_constructor_args():
    sig = inspect.signature(ExpressionRef.__init__)
    params = list(sig.parameters.keys())



def test_r1::functionref_is_not_abstract():
    assert not inspect.isabstract(r1::FunctionRef)


def test_r1::functionref_constructor_exists():
    assert callable(r1::FunctionRef.__init__)


def test_r1::functionref_constructor_args():
    sig = inspect.signature(r1::FunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_r1::eobject_is_not_abstract():
    assert not inspect.isabstract(r1::EObject)


def test_r1::eobject_constructor_exists():
    assert callable(r1::EObject.__init__)


def test_r1::eobject_constructor_args():
    sig = inspect.signature(r1::EObject.__init__)
    params = list(sig.parameters.keys())



def test_r1::element_is_not_abstract():
    assert not inspect.isabstract(r1::Element)


def test_r1::element_constructor_exists():
    assert callable(r1::Element.__init__)


def test_r1::element_constructor_args():
    sig = inspect.signature(r1::Element.__init__)
    params = list(sig.parameters.keys())
    assert "localId" in params, "Missing parameter 'localId'"

def test_r1::element_has_localId():
    assert hasattr(r1::Element, "localId")
    descriptor = None
    for klass in r1::Element.__mro__:
        if "localId" in klass.__dict__:
            descriptor = klass.__dict__["localId"]
            break
    assert isinstance(descriptor, property)



def test_naryexpression_is_not_abstract():
    assert not inspect.isabstract(NaryExpression)


def test_naryexpression_constructor_exists():
    assert callable(NaryExpression.__init__)


def test_naryexpression_constructor_args():
    sig = inspect.signature(NaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::concatenate_is_not_abstract():
    assert not inspect.isabstract(r1::Concatenate)


def test_r1::concatenate_constructor_exists():
    assert callable(r1::Concatenate.__init__)


def test_r1::concatenate_constructor_args():
    sig = inspect.signature(r1::Concatenate.__init__)
    params = list(sig.parameters.keys())



def test_r1::coalesce_is_not_abstract():
    assert not inspect.isabstract(r1::Coalesce)


def test_r1::coalesce_constructor_exists():
    assert callable(r1::Coalesce.__init__)


def test_r1::coalesce_constructor_args():
    sig = inspect.signature(r1::Coalesce.__init__)
    params = list(sig.parameters.keys())



def test_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(AggregateExpression)


def test_aggregateexpression_constructor_exists():
    assert callable(AggregateExpression.__init__)


def test_aggregateexpression_constructor_args():
    sig = inspect.signature(AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::populationstddev_is_not_abstract():
    assert not inspect.isabstract(r1::PopulationStdDev)


def test_r1::populationstddev_constructor_exists():
    assert callable(r1::PopulationStdDev.__init__)


def test_r1::populationstddev_constructor_args():
    sig = inspect.signature(r1::PopulationStdDev.__init__)
    params = list(sig.parameters.keys())



def test_r1::median_is_not_abstract():
    assert not inspect.isabstract(r1::Median)


def test_r1::median_constructor_exists():
    assert callable(r1::Median.__init__)


def test_r1::median_constructor_args():
    sig = inspect.signature(r1::Median.__init__)
    params = list(sig.parameters.keys())



def test_r1::stddev_is_not_abstract():
    assert not inspect.isabstract(r1::StdDev)


def test_r1::stddev_constructor_exists():
    assert callable(r1::StdDev.__init__)


def test_r1::stddev_constructor_args():
    sig = inspect.signature(r1::StdDev.__init__)
    params = list(sig.parameters.keys())



def test_r1::variance_is_not_abstract():
    assert not inspect.isabstract(r1::Variance)


def test_r1::variance_constructor_exists():
    assert callable(r1::Variance.__init__)


def test_r1::variance_constructor_args():
    sig = inspect.signature(r1::Variance.__init__)
    params = list(sig.parameters.keys())



def test_r1::mode_is_not_abstract():
    assert not inspect.isabstract(r1::Mode)


def test_r1::mode_constructor_exists():
    assert callable(r1::Mode.__init__)


def test_r1::mode_constructor_args():
    sig = inspect.signature(r1::Mode.__init__)
    params = list(sig.parameters.keys())



def test_r1::avg_is_not_abstract():
    assert not inspect.isabstract(r1::Avg)


def test_r1::avg_constructor_exists():
    assert callable(r1::Avg.__init__)


def test_r1::avg_constructor_args():
    sig = inspect.signature(r1::Avg.__init__)
    params = list(sig.parameters.keys())



def test_r1::populationvariance_is_not_abstract():
    assert not inspect.isabstract(r1::PopulationVariance)


def test_r1::populationvariance_constructor_exists():
    assert callable(r1::PopulationVariance.__init__)


def test_r1::populationvariance_constructor_args():
    sig = inspect.signature(r1::PopulationVariance.__init__)
    params = list(sig.parameters.keys())



def test_r1::max_is_not_abstract():
    assert not inspect.isabstract(r1::Max)


def test_r1::max_constructor_exists():
    assert callable(r1::Max.__init__)


def test_r1::max_constructor_args():
    sig = inspect.signature(r1::Max.__init__)
    params = list(sig.parameters.keys())



def test_r1::min_is_not_abstract():
    assert not inspect.isabstract(r1::Min)


def test_r1::min_constructor_exists():
    assert callable(r1::Min.__init__)


def test_r1::min_constructor_args():
    sig = inspect.signature(r1::Min.__init__)
    params = list(sig.parameters.keys())



def test_r1::count_is_not_abstract():
    assert not inspect.isabstract(r1::Count)


def test_r1::count_constructor_exists():
    assert callable(r1::Count.__init__)


def test_r1::count_constructor_args():
    sig = inspect.signature(r1::Count.__init__)
    params = list(sig.parameters.keys())



def test_r1::anytrue_is_not_abstract():
    assert not inspect.isabstract(r1::AnyTrue)


def test_r1::anytrue_constructor_exists():
    assert callable(r1::AnyTrue.__init__)


def test_r1::anytrue_constructor_args():
    sig = inspect.signature(r1::AnyTrue.__init__)
    params = list(sig.parameters.keys())



def test_r1::sum_is_not_abstract():
    assert not inspect.isabstract(r1::Sum)


def test_r1::sum_constructor_exists():
    assert callable(r1::Sum.__init__)


def test_r1::sum_constructor_args():
    sig = inspect.signature(r1::Sum.__init__)
    params = list(sig.parameters.keys())



def test_r1::alltrue_is_not_abstract():
    assert not inspect.isabstract(r1::AllTrue)


def test_r1::alltrue_constructor_exists():
    assert callable(r1::AllTrue.__init__)


def test_r1::alltrue_constructor_args():
    sig = inspect.signature(r1::AllTrue.__init__)
    params = list(sig.parameters.keys())



def test_sortbyitem_is_not_abstract():
    assert not inspect.isabstract(SortByItem)


def test_sortbyitem_constructor_exists():
    assert callable(SortByItem.__init__)


def test_sortbyitem_constructor_args():
    sig = inspect.signature(SortByItem.__init__)
    params = list(sig.parameters.keys())



def test_r1::bydirection_is_not_abstract():
    assert not inspect.isabstract(r1::ByDirection)


def test_r1::bydirection_constructor_exists():
    assert callable(r1::ByDirection.__init__)


def test_r1::bydirection_constructor_args():
    sig = inspect.signature(r1::ByDirection.__init__)
    params = list(sig.parameters.keys())



def test_r1::byexpression_is_not_abstract():
    assert not inspect.isabstract(r1::ByExpression)


def test_r1::byexpression_constructor_exists():
    assert callable(r1::ByExpression.__init__)


def test_r1::byexpression_constructor_args():
    sig = inspect.signature(r1::ByExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::bycolumn_is_not_abstract():
    assert not inspect.isabstract(r1::ByColumn)


def test_r1::bycolumn_constructor_exists():
    assert callable(r1::ByColumn.__init__)


def test_r1::bycolumn_constructor_args():
    sig = inspect.signature(r1::ByColumn.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_r1::bycolumn_has_path():
    assert hasattr(r1::ByColumn, "path")
    descriptor = None
    for klass in r1::ByColumn.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_r1::defineclause_is_not_abstract():
    assert not inspect.isabstract(r1::DefineClause)


def test_r1::defineclause_constructor_exists():
    assert callable(r1::DefineClause.__init__)


def test_r1::defineclause_constructor_args():
    sig = inspect.signature(r1::DefineClause.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_r1::defineclause_has_identifier():
    assert hasattr(r1::DefineClause, "identifier")
    descriptor = None
    for klass in r1::DefineClause.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_r1::sortbyitem_is_not_abstract():
    assert not inspect.isabstract(r1::SortByItem)


def test_r1::sortbyitem_constructor_exists():
    assert callable(r1::SortByItem.__init__)


def test_r1::sortbyitem_constructor_args():
    sig = inspect.signature(r1::SortByItem.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_r1::sortbyitem_has_direction():
    assert hasattr(r1::SortByItem, "direction")
    descriptor = None
    for klass in r1::SortByItem.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_r1::caseitem_is_not_abstract():
    assert not inspect.isabstract(r1::CaseItem)


def test_r1::caseitem_constructor_exists():
    assert callable(r1::CaseItem.__init__)


def test_r1::caseitem_constructor_args():
    sig = inspect.signature(r1::CaseItem.__init__)
    params = list(sig.parameters.keys())



def test_r1::codesystemdef_is_not_abstract():
    assert not inspect.isabstract(r1::CodeSystemDef)


def test_r1::codesystemdef_constructor_exists():
    assert callable(r1::CodeSystemDef.__init__)


def test_r1::codesystemdef_constructor_args():
    sig = inspect.signature(r1::CodeSystemDef.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_r1::codesystemdef_has_accessLevel():
    assert hasattr(r1::CodeSystemDef, "accessLevel")
    descriptor = None
    for klass in r1::CodeSystemDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1::codesystemdef_has_version():
    assert hasattr(r1::CodeSystemDef, "version")
    descriptor = None
    for klass in r1::CodeSystemDef.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_r1::codesystemdef_has_name():
    assert hasattr(r1::CodeSystemDef, "name")
    descriptor = None
    for klass in r1::CodeSystemDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1::codesystemdef_has_id():
    assert hasattr(r1::CodeSystemDef, "id")
    descriptor = None
    for klass in r1::CodeSystemDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_r1::valuesetdef_is_not_abstract():
    assert not inspect.isabstract(r1::ValueSetDef)


def test_r1::valuesetdef_constructor_exists():
    assert callable(r1::ValueSetDef.__init__)


def test_r1::valuesetdef_constructor_args():
    sig = inspect.signature(r1::ValueSetDef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_r1::valuesetdef_has_id():
    assert hasattr(r1::ValueSetDef, "id")
    descriptor = None
    for klass in r1::ValueSetDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_r1::valuesetdef_has_accessLevel():
    assert hasattr(r1::ValueSetDef, "accessLevel")
    descriptor = None
    for klass in r1::ValueSetDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1::valuesetdef_has_name():
    assert hasattr(r1::ValueSetDef, "name")
    descriptor = None
    for klass in r1::ValueSetDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1::valuesetdef_has_version():
    assert hasattr(r1::ValueSetDef, "version")
    descriptor = None
    for klass in r1::ValueSetDef.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_r1::returnclause_is_not_abstract():
    assert not inspect.isabstract(r1::ReturnClause)


def test_r1::returnclause_constructor_exists():
    assert callable(r1::ReturnClause.__init__)


def test_r1::returnclause_constructor_args():
    sig = inspect.signature(r1::ReturnClause.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_r1::returnclause_has_distinct():
    assert hasattr(r1::ReturnClause, "distinct")
    descriptor = None
    for klass in r1::ReturnClause.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_r1::parameterdef_is_not_abstract():
    assert not inspect.isabstract(r1::ParameterDef)


def test_r1::parameterdef_constructor_exists():
    assert callable(r1::ParameterDef.__init__)


def test_r1::parameterdef_constructor_args():
    sig = inspect.signature(r1::ParameterDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "parameterType" in params, "Missing parameter 'parameterType'"

def test_r1::parameterdef_has_name():
    assert hasattr(r1::ParameterDef, "name")
    descriptor = None
    for klass in r1::ParameterDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1::parameterdef_has_accessLevel():
    assert hasattr(r1::ParameterDef, "accessLevel")
    descriptor = None
    for klass in r1::ParameterDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1::parameterdef_has_parameterType():
    assert hasattr(r1::ParameterDef, "parameterType")
    descriptor = None
    for klass in r1::ParameterDef.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)



def test_r1::sortclause_is_not_abstract():
    assert not inspect.isabstract(r1::SortClause)


def test_r1::sortclause_constructor_exists():
    assert callable(r1::SortClause.__init__)


def test_r1::sortclause_constructor_args():
    sig = inspect.signature(r1::SortClause.__init__)
    params = list(sig.parameters.keys())



def test_r1::operanddef_is_not_abstract():
    assert not inspect.isabstract(r1::OperandDef)


def test_r1::operanddef_constructor_exists():
    assert callable(r1::OperandDef.__init__)


def test_r1::operanddef_constructor_args():
    sig = inspect.signature(r1::OperandDef.__init__)
    params = list(sig.parameters.keys())
    assert "operandType" in params, "Missing parameter 'operandType'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::operanddef_has_operandType():
    assert hasattr(r1::OperandDef, "operandType")
    descriptor = None
    for klass in r1::OperandDef.__mro__:
        if "operandType" in klass.__dict__:
            descriptor = klass.__dict__["operandType"]
            break
    assert isinstance(descriptor, property)

def test_r1::operanddef_has_name():
    assert hasattr(r1::OperandDef, "name")
    descriptor = None
    for klass in r1::OperandDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::typespecifier_is_not_abstract():
    assert not inspect.isabstract(r1::TypeSpecifier)


def test_r1::typespecifier_constructor_exists():
    assert callable(r1::TypeSpecifier.__init__)


def test_r1::typespecifier_constructor_args():
    sig = inspect.signature(r1::TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1::expressiondef_is_not_abstract():
    assert not inspect.isabstract(r1::ExpressionDef)


def test_r1::expressiondef_constructor_exists():
    assert callable(r1::ExpressionDef.__init__)


def test_r1::expressiondef_constructor_args():
    sig = inspect.signature(r1::ExpressionDef.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "context" in params, "Missing parameter 'context'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::expressiondef_has_accessLevel():
    assert hasattr(r1::ExpressionDef, "accessLevel")
    descriptor = None
    for klass in r1::ExpressionDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1::expressiondef_has_context():
    assert hasattr(r1::ExpressionDef, "context")
    descriptor = None
    for klass in r1::ExpressionDef.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_r1::expressiondef_has_name():
    assert hasattr(r1::ExpressionDef, "name")
    descriptor = None
    for klass in r1::ExpressionDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::tupleelementdefinition_is_not_abstract():
    assert not inspect.isabstract(r1::TupleElementDefinition)


def test_r1::tupleelementdefinition_constructor_exists():
    assert callable(r1::TupleElementDefinition.__init__)


def test_r1::tupleelementdefinition_constructor_args():
    sig = inspect.signature(r1::TupleElementDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::tupleelementdefinition_has_name():
    assert hasattr(r1::TupleElementDefinition, "name")
    descriptor = None
    for klass in r1::TupleElementDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::aliasedquerysource_is_not_abstract():
    assert not inspect.isabstract(r1::AliasedQuerySource)


def test_r1::aliasedquerysource_constructor_exists():
    assert callable(r1::AliasedQuerySource.__init__)


def test_r1::aliasedquerysource_constructor_args():
    sig = inspect.signature(r1::AliasedQuerySource.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_r1::aliasedquerysource_has_alias():
    assert hasattr(r1::AliasedQuerySource, "alias")
    descriptor = None
    for klass in r1::AliasedQuerySource.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_r1::expression_is_not_abstract():
    assert not inspect.isabstract(r1::Expression)


def test_r1::expression_constructor_exists():
    assert callable(r1::Expression.__init__)


def test_r1::expression_constructor_args():
    sig = inspect.signature(r1::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_r1::positionof_is_not_abstract():
    assert not inspect.isabstract(r1::PositionOf)


def test_r1::positionof_constructor_exists():
    assert callable(r1::PositionOf.__init__)


def test_r1::positionof_constructor_args():
    sig = inspect.signature(r1::PositionOf.__init__)
    params = list(sig.parameters.keys())



def test_r1::foreach_is_not_abstract():
    assert not inspect.isabstract(r1::ForEach)


def test_r1::foreach_constructor_exists():
    assert callable(r1::ForEach.__init__)


def test_r1::foreach_constructor_args():
    sig = inspect.signature(r1::ForEach.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1::foreach_has_scope():
    assert hasattr(r1::ForEach, "scope")
    descriptor = None
    for klass in r1::ForEach.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1::code_is_not_abstract():
    assert not inspect.isabstract(r1::Code)


def test_r1::code_constructor_exists():
    assert callable(r1::Code.__init__)


def test_r1::code_constructor_args():
    sig = inspect.signature(r1::Code.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"
    assert "code" in params, "Missing parameter 'code'"

def test_r1::code_has_display():
    assert hasattr(r1::Code, "display")
    descriptor = None
    for klass in r1::Code.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)

def test_r1::code_has_code():
    assert hasattr(r1::Code, "code")
    descriptor = None
    for klass in r1::Code.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_r1::datetime_is_not_abstract():
    assert not inspect.isabstract(r1::DateTime)


def test_r1::datetime_constructor_exists():
    assert callable(r1::DateTime.__init__)


def test_r1::datetime_constructor_args():
    sig = inspect.signature(r1::DateTime.__init__)
    params = list(sig.parameters.keys())



def test_r1::quantity_is_not_abstract():
    assert not inspect.isabstract(r1::Quantity)


def test_r1::quantity_constructor_exists():
    assert callable(r1::Quantity.__init__)


def test_r1::quantity_constructor_args():
    sig = inspect.signature(r1::Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_r1::quantity_has_value():
    assert hasattr(r1::Quantity, "value")
    descriptor = None
    for klass in r1::Quantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_r1::quantity_has_unit():
    assert hasattr(r1::Quantity, "unit")
    descriptor = None
    for klass in r1::Quantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_r1::aliasref_is_not_abstract():
    assert not inspect.isabstract(r1::AliasRef)


def test_r1::aliasref_constructor_exists():
    assert callable(r1::AliasRef.__init__)


def test_r1::aliasref_constructor_args():
    sig = inspect.signature(r1::AliasRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::aliasref_has_name():
    assert hasattr(r1::AliasRef, "name")
    descriptor = None
    for klass in r1::AliasRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::minvalue_is_not_abstract():
    assert not inspect.isabstract(r1::MinValue)


def test_r1::minvalue_constructor_exists():
    assert callable(r1::MinValue.__init__)


def test_r1::minvalue_constructor_args():
    sig = inspect.signature(r1::MinValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1::minvalue_has_valueType():
    assert hasattr(r1::MinValue, "valueType")
    descriptor = None
    for klass in r1::MinValue.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1::codesystemref_is_not_abstract():
    assert not inspect.isabstract(r1::CodeSystemRef)


def test_r1::codesystemref_constructor_exists():
    assert callable(r1::CodeSystemRef.__init__)


def test_r1::codesystemref_constructor_args():
    sig = inspect.signature(r1::CodeSystemRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "libraryName" in params, "Missing parameter 'libraryName'"

def test_r1::codesystemref_has_name():
    assert hasattr(r1::CodeSystemRef, "name")
    descriptor = None
    for klass in r1::CodeSystemRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1::codesystemref_has_libraryName():
    assert hasattr(r1::CodeSystemRef, "libraryName")
    descriptor = None
    for klass in r1::CodeSystemRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)



def test_r1::interval_is_not_abstract():
    assert not inspect.isabstract(r1::Interval)


def test_r1::interval_constructor_exists():
    assert callable(r1::Interval.__init__)


def test_r1::interval_constructor_args():
    sig = inspect.signature(r1::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r1::interval_has_lowClosed():
    assert hasattr(r1::Interval, "lowClosed")
    descriptor = None
    for klass in r1::Interval.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r1::interval_has_highClosed():
    assert hasattr(r1::Interval, "highClosed")
    descriptor = None
    for klass in r1::Interval.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r1::null_is_not_abstract():
    assert not inspect.isabstract(r1::Null)


def test_r1::null_constructor_exists():
    assert callable(r1::Null.__init__)


def test_r1::null_constructor_args():
    sig = inspect.signature(r1::Null.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1::null_has_valueType():
    assert hasattr(r1::Null, "valueType")
    descriptor = None
    for klass in r1::Null.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1::first_is_not_abstract():
    assert not inspect.isabstract(r1::First)


def test_r1::first_constructor_exists():
    assert callable(r1::First.__init__)


def test_r1::first_constructor_args():
    sig = inspect.signature(r1::First.__init__)
    params = list(sig.parameters.keys())
    assert "orderBy" in params, "Missing parameter 'orderBy'"

def test_r1::first_has_orderBy():
    assert hasattr(r1::First, "orderBy")
    descriptor = None
    for klass in r1::First.__mro__:
        if "orderBy" in klass.__dict__:
            descriptor = klass.__dict__["orderBy"]
            break
    assert isinstance(descriptor, property)



def test_r1::case_is_not_abstract():
    assert not inspect.isabstract(r1::Case)


def test_r1::case_constructor_exists():
    assert callable(r1::Case.__init__)


def test_r1::case_constructor_args():
    sig = inspect.signature(r1::Case.__init__)
    params = list(sig.parameters.keys())



def test_r1::invalueset_is_not_abstract():
    assert not inspect.isabstract(r1::InValueSet)


def test_r1::invalueset_constructor_exists():
    assert callable(r1::InValueSet.__init__)


def test_r1::invalueset_constructor_args():
    sig = inspect.signature(r1::InValueSet.__init__)
    params = list(sig.parameters.keys())



def test_r1::today_is_not_abstract():
    assert not inspect.isabstract(r1::Today)


def test_r1::today_constructor_exists():
    assert callable(r1::Today.__init__)


def test_r1::today_constructor_args():
    sig = inspect.signature(r1::Today.__init__)
    params = list(sig.parameters.keys())



def test_r1::substring_is_not_abstract():
    assert not inspect.isabstract(r1::Substring)


def test_r1::substring_constructor_exists():
    assert callable(r1::Substring.__init__)


def test_r1::substring_constructor_args():
    sig = inspect.signature(r1::Substring.__init__)
    params = list(sig.parameters.keys())



def test_r1::current_is_not_abstract():
    assert not inspect.isabstract(r1::Current)


def test_r1::current_constructor_exists():
    assert callable(r1::Current.__init__)


def test_r1::current_constructor_args():
    sig = inspect.signature(r1::Current.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1::current_has_scope():
    assert hasattr(r1::Current, "scope")
    descriptor = None
    for klass in r1::Current.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1::querydefineref_is_not_abstract():
    assert not inspect.isabstract(r1::QueryDefineRef)


def test_r1::querydefineref_constructor_exists():
    assert callable(r1::QueryDefineRef.__init__)


def test_r1::querydefineref_constructor_args():
    sig = inspect.signature(r1::QueryDefineRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::querydefineref_has_name():
    assert hasattr(r1::QueryDefineRef, "name")
    descriptor = None
    for klass in r1::QueryDefineRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::query_is_not_abstract():
    assert not inspect.isabstract(r1::Query)


def test_r1::query_constructor_exists():
    assert callable(r1::Query.__init__)


def test_r1::query_constructor_args():
    sig = inspect.signature(r1::Query.__init__)
    params = list(sig.parameters.keys())



def test_r1::list_is_not_abstract():
    assert not inspect.isabstract(r1::List)


def test_r1::list_constructor_exists():
    assert callable(r1::List.__init__)


def test_r1::list_constructor_args():
    sig = inspect.signature(r1::List.__init__)
    params = list(sig.parameters.keys())



def test_r1::timeofday_is_not_abstract():
    assert not inspect.isabstract(r1::TimeOfDay)


def test_r1::timeofday_constructor_exists():
    assert callable(r1::TimeOfDay.__init__)


def test_r1::timeofday_constructor_args():
    sig = inspect.signature(r1::TimeOfDay.__init__)
    params = list(sig.parameters.keys())



def test_r1::combine_is_not_abstract():
    assert not inspect.isabstract(r1::Combine)


def test_r1::combine_constructor_exists():
    assert callable(r1::Combine.__init__)


def test_r1::combine_constructor_args():
    sig = inspect.signature(r1::Combine.__init__)
    params = list(sig.parameters.keys())



def test_r1::tuple_is_not_abstract():
    assert not inspect.isabstract(r1::Tuple)


def test_r1::tuple_constructor_exists():
    assert callable(r1::Tuple.__init__)


def test_r1::tuple_constructor_args():
    sig = inspect.signature(r1::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_r1::valuesetref_is_not_abstract():
    assert not inspect.isabstract(r1::ValueSetRef)


def test_r1::valuesetref_constructor_exists():
    assert callable(r1::ValueSetRef.__init__)


def test_r1::valuesetref_constructor_args():
    sig = inspect.signature(r1::ValueSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::valuesetref_has_libraryName():
    assert hasattr(r1::ValueSetRef, "libraryName")
    descriptor = None
    for klass in r1::ValueSetRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1::valuesetref_has_name():
    assert hasattr(r1::ValueSetRef, "name")
    descriptor = None
    for klass in r1::ValueSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::time_is_not_abstract():
    assert not inspect.isabstract(r1::Time)


def test_r1::time_constructor_exists():
    assert callable(r1::Time.__init__)


def test_r1::time_constructor_args():
    sig = inspect.signature(r1::Time.__init__)
    params = list(sig.parameters.keys())



def test_r1::operandref_is_not_abstract():
    assert not inspect.isabstract(r1::OperandRef)


def test_r1::operandref_constructor_exists():
    assert callable(r1::OperandRef.__init__)


def test_r1::operandref_constructor_args():
    sig = inspect.signature(r1::OperandRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1::operandref_has_name():
    assert hasattr(r1::OperandRef, "name")
    descriptor = None
    for klass in r1::OperandRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::concept_is_not_abstract():
    assert not inspect.isabstract(r1::Concept)


def test_r1::concept_constructor_exists():
    assert callable(r1::Concept.__init__)


def test_r1::concept_constructor_args():
    sig = inspect.signature(r1::Concept.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"

def test_r1::concept_has_display():
    assert hasattr(r1::Concept, "display")
    descriptor = None
    for klass in r1::Concept.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)



def test_r1::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1::BinaryExpression)


def test_r1::binaryexpression_constructor_exists():
    assert callable(r1::BinaryExpression.__init__)


def test_r1::binaryexpression_constructor_args():
    sig = inspect.signature(r1::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::indexof_is_not_abstract():
    assert not inspect.isabstract(r1::IndexOf)


def test_r1::indexof_constructor_exists():
    assert callable(r1::IndexOf.__init__)


def test_r1::indexof_constructor_args():
    sig = inspect.signature(r1::IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_r1::naryexpression_is_not_abstract():
    assert not inspect.isabstract(r1::NaryExpression)


def test_r1::naryexpression_constructor_exists():
    assert callable(r1::NaryExpression.__init__)


def test_r1::naryexpression_constructor_args():
    sig = inspect.signature(r1::NaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::filter_is_not_abstract():
    assert not inspect.isabstract(r1::Filter)


def test_r1::filter_constructor_exists():
    assert callable(r1::Filter.__init__)


def test_r1::filter_constructor_args():
    sig = inspect.signature(r1::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1::filter_has_scope():
    assert hasattr(r1::Filter, "scope")
    descriptor = None
    for klass in r1::Filter.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1::retrieve_is_not_abstract():
    assert not inspect.isabstract(r1::Retrieve)


def test_r1::retrieve_constructor_exists():
    assert callable(r1::Retrieve.__init__)


def test_r1::retrieve_constructor_args():
    sig = inspect.signature(r1::Retrieve.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "dateHighProperty" in params, "Missing parameter 'dateHighProperty'"
    assert "templateId" in params, "Missing parameter 'templateId'"
    assert "dateLowProperty" in params, "Missing parameter 'dateLowProperty'"
    assert "dateProperty" in params, "Missing parameter 'dateProperty'"
    assert "idProperty" in params, "Missing parameter 'idProperty'"
    assert "codeProperty" in params, "Missing parameter 'codeProperty'"

def test_r1::retrieve_has_dataType():
    assert hasattr(r1::Retrieve, "dataType")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_scope():
    assert hasattr(r1::Retrieve, "scope")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_dateHighProperty():
    assert hasattr(r1::Retrieve, "dateHighProperty")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "dateHighProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateHighProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_templateId():
    assert hasattr(r1::Retrieve, "templateId")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "templateId" in klass.__dict__:
            descriptor = klass.__dict__["templateId"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_dateLowProperty():
    assert hasattr(r1::Retrieve, "dateLowProperty")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "dateLowProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateLowProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_dateProperty():
    assert hasattr(r1::Retrieve, "dateProperty")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "dateProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_idProperty():
    assert hasattr(r1::Retrieve, "idProperty")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "idProperty" in klass.__dict__:
            descriptor = klass.__dict__["idProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1::retrieve_has_codeProperty():
    assert hasattr(r1::Retrieve, "codeProperty")
    descriptor = None
    for klass in r1::Retrieve.__mro__:
        if "codeProperty" in klass.__dict__:
            descriptor = klass.__dict__["codeProperty"]
            break
    assert isinstance(descriptor, property)



def test_r1::last_is_not_abstract():
    assert not inspect.isabstract(r1::Last)


def test_r1::last_constructor_exists():
    assert callable(r1::Last.__init__)


def test_r1::last_constructor_args():
    sig = inspect.signature(r1::Last.__init__)
    params = list(sig.parameters.keys())
    assert "orderBy" in params, "Missing parameter 'orderBy'"

def test_r1::last_has_orderBy():
    assert hasattr(r1::Last, "orderBy")
    descriptor = None
    for klass in r1::Last.__mro__:
        if "orderBy" in klass.__dict__:
            descriptor = klass.__dict__["orderBy"]
            break
    assert isinstance(descriptor, property)



def test_r1::property_is_not_abstract():
    assert not inspect.isabstract(r1::Property)


def test_r1::property_constructor_exists():
    assert callable(r1::Property.__init__)


def test_r1::property_constructor_args():
    sig = inspect.signature(r1::Property.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "path" in params, "Missing parameter 'path'"

def test_r1::property_has_scope():
    assert hasattr(r1::Property, "scope")
    descriptor = None
    for klass in r1::Property.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_r1::property_has_path():
    assert hasattr(r1::Property, "path")
    descriptor = None
    for klass in r1::Property.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_r1::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1::UnaryExpression)


def test_r1::unaryexpression_constructor_exists():
    assert callable(r1::UnaryExpression.__init__)


def test_r1::unaryexpression_constructor_args():
    sig = inspect.signature(r1::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::maxvalue_is_not_abstract():
    assert not inspect.isabstract(r1::MaxValue)


def test_r1::maxvalue_constructor_exists():
    assert callable(r1::MaxValue.__init__)


def test_r1::maxvalue_constructor_args():
    sig = inspect.signature(r1::MaxValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1::maxvalue_has_valueType():
    assert hasattr(r1::MaxValue, "valueType")
    descriptor = None
    for klass in r1::MaxValue.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1::sort_is_not_abstract():
    assert not inspect.isabstract(r1::Sort)


def test_r1::sort_constructor_exists():
    assert callable(r1::Sort.__init__)


def test_r1::sort_constructor_args():
    sig = inspect.signature(r1::Sort.__init__)
    params = list(sig.parameters.keys())



def test_r1::split_is_not_abstract():
    assert not inspect.isabstract(r1::Split)


def test_r1::split_constructor_exists():
    assert callable(r1::Split.__init__)


def test_r1::split_constructor_args():
    sig = inspect.signature(r1::Split.__init__)
    params = list(sig.parameters.keys())



def test_r1::now_is_not_abstract():
    assert not inspect.isabstract(r1::Now)


def test_r1::now_constructor_exists():
    assert callable(r1::Now.__init__)


def test_r1::now_constructor_args():
    sig = inspect.signature(r1::Now.__init__)
    params = list(sig.parameters.keys())



def test_r1::incodesystem_is_not_abstract():
    assert not inspect.isabstract(r1::InCodeSystem)


def test_r1::incodesystem_constructor_exists():
    assert callable(r1::InCodeSystem.__init__)


def test_r1::incodesystem_constructor_args():
    sig = inspect.signature(r1::InCodeSystem.__init__)
    params = list(sig.parameters.keys())



def test_r1::round_is_not_abstract():
    assert not inspect.isabstract(r1::Round)


def test_r1::round_constructor_exists():
    assert callable(r1::Round.__init__)


def test_r1::round_constructor_args():
    sig = inspect.signature(r1::Round.__init__)
    params = list(sig.parameters.keys())



def test_r1::if_is_not_abstract():
    assert not inspect.isabstract(r1::If)


def test_r1::if_constructor_exists():
    assert callable(r1::If.__init__)


def test_r1::if_constructor_args():
    sig = inspect.signature(r1::If.__init__)
    params = list(sig.parameters.keys())



def test_r1::parameterref_is_not_abstract():
    assert not inspect.isabstract(r1::ParameterRef)


def test_r1::parameterref_constructor_exists():
    assert callable(r1::ParameterRef.__init__)


def test_r1::parameterref_constructor_args():
    sig = inspect.signature(r1::ParameterRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::parameterref_has_libraryName():
    assert hasattr(r1::ParameterRef, "libraryName")
    descriptor = None
    for klass in r1::ParameterRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1::parameterref_has_name():
    assert hasattr(r1::ParameterRef, "name")
    descriptor = None
    for klass in r1::ParameterRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::identifierref_is_not_abstract():
    assert not inspect.isabstract(r1::IdentifierRef)


def test_r1::identifierref_constructor_exists():
    assert callable(r1::IdentifierRef.__init__)


def test_r1::identifierref_constructor_args():
    sig = inspect.signature(r1::IdentifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::identifierref_has_libraryName():
    assert hasattr(r1::IdentifierRef, "libraryName")
    descriptor = None
    for klass in r1::IdentifierRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1::identifierref_has_name():
    assert hasattr(r1::IdentifierRef, "name")
    descriptor = None
    for klass in r1::IdentifierRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::literal_is_not_abstract():
    assert not inspect.isabstract(r1::Literal)


def test_r1::literal_constructor_exists():
    assert callable(r1::Literal.__init__)


def test_r1::literal_constructor_args():
    sig = inspect.signature(r1::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "value" in params, "Missing parameter 'value'"

def test_r1::literal_has_valueType():
    assert hasattr(r1::Literal, "valueType")
    descriptor = None
    for klass in r1::Literal.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_r1::literal_has_value():
    assert hasattr(r1::Literal, "value")
    descriptor = None
    for klass in r1::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r1::ternaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1::TernaryExpression)


def test_r1::ternaryexpression_constructor_exists():
    assert callable(r1::TernaryExpression.__init__)


def test_r1::ternaryexpression_constructor_args():
    sig = inspect.signature(r1::TernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::expressionref_is_not_abstract():
    assert not inspect.isabstract(r1::ExpressionRef)


def test_r1::expressionref_constructor_exists():
    assert callable(r1::ExpressionRef.__init__)


def test_r1::expressionref_constructor_args():
    sig = inspect.signature(r1::ExpressionRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1::expressionref_has_libraryName():
    assert hasattr(r1::ExpressionRef, "libraryName")
    descriptor = None
    for klass in r1::ExpressionRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1::expressionref_has_name():
    assert hasattr(r1::ExpressionRef, "name")
    descriptor = None
    for klass in r1::ExpressionRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1::instance_is_not_abstract():
    assert not inspect.isabstract(r1::Instance)


def test_r1::instance_constructor_exists():
    assert callable(r1::Instance.__init__)


def test_r1::instance_constructor_args():
    sig = inspect.signature(r1::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "classType" in params, "Missing parameter 'classType'"

def test_r1::instance_has_classType():
    assert hasattr(r1::Instance, "classType")
    descriptor = None
    for klass in r1::Instance.__mro__:
        if "classType" in klass.__dict__:
            descriptor = klass.__dict__["classType"]
            break
    assert isinstance(descriptor, property)



def test_r1::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(r1::AggregateExpression)


def test_r1::aggregateexpression_constructor_exists():
    assert callable(r1::AggregateExpression.__init__)


def test_r1::aggregateexpression_constructor_args():
    sig = inspect.signature(r1::AggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_r1::aggregateexpression_has_path():
    assert hasattr(r1::AggregateExpression, "path")
    descriptor = None
    for klass in r1::AggregateExpression.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::propercontains_is_not_abstract():
    assert not inspect.isabstract(r1::ProperContains)


def test_r1::propercontains_constructor_exists():
    assert callable(r1::ProperContains.__init__)


def test_r1::propercontains_constructor_args():
    sig = inspect.signature(r1::ProperContains.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::propercontains_has_precision():
    assert hasattr(r1::ProperContains, "precision")
    descriptor = None
    for klass in r1::ProperContains.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::notequal_is_not_abstract():
    assert not inspect.isabstract(r1::NotEqual)


def test_r1::notequal_constructor_exists():
    assert callable(r1::NotEqual.__init__)


def test_r1::notequal_constructor_args():
    sig = inspect.signature(r1::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1::times_is_not_abstract():
    assert not inspect.isabstract(r1::Times)


def test_r1::times_constructor_exists():
    assert callable(r1::Times.__init__)


def test_r1::times_constructor_args():
    sig = inspect.signature(r1::Times.__init__)
    params = list(sig.parameters.keys())



def test_r1::meetsafter_is_not_abstract():
    assert not inspect.isabstract(r1::MeetsAfter)


def test_r1::meetsafter_constructor_exists():
    assert callable(r1::MeetsAfter.__init__)


def test_r1::meetsafter_constructor_args():
    sig = inspect.signature(r1::MeetsAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::meetsafter_has_precision():
    assert hasattr(r1::MeetsAfter, "precision")
    descriptor = None
    for klass in r1::MeetsAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::before_is_not_abstract():
    assert not inspect.isabstract(r1::Before)


def test_r1::before_constructor_exists():
    assert callable(r1::Before.__init__)


def test_r1::before_constructor_args():
    sig = inspect.signature(r1::Before.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::before_has_precision():
    assert hasattr(r1::Before, "precision")
    descriptor = None
    for klass in r1::Before.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::overlaps_is_not_abstract():
    assert not inspect.isabstract(r1::Overlaps)


def test_r1::overlaps_constructor_exists():
    assert callable(r1::Overlaps.__init__)


def test_r1::overlaps_constructor_args():
    sig = inspect.signature(r1::Overlaps.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::overlaps_has_precision():
    assert hasattr(r1::Overlaps, "precision")
    descriptor = None
    for klass in r1::Overlaps.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::starts_is_not_abstract():
    assert not inspect.isabstract(r1::Starts)


def test_r1::starts_constructor_exists():
    assert callable(r1::Starts.__init__)


def test_r1::starts_constructor_args():
    sig = inspect.signature(r1::Starts.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::starts_has_precision():
    assert hasattr(r1::Starts, "precision")
    descriptor = None
    for klass in r1::Starts.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::properincludes_is_not_abstract():
    assert not inspect.isabstract(r1::ProperIncludes)


def test_r1::properincludes_constructor_exists():
    assert callable(r1::ProperIncludes.__init__)


def test_r1::properincludes_constructor_args():
    sig = inspect.signature(r1::ProperIncludes.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::properincludes_has_precision():
    assert hasattr(r1::ProperIncludes, "precision")
    descriptor = None
    for klass in r1::ProperIncludes.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::overlapsafter_is_not_abstract():
    assert not inspect.isabstract(r1::OverlapsAfter)


def test_r1::overlapsafter_constructor_exists():
    assert callable(r1::OverlapsAfter.__init__)


def test_r1::overlapsafter_constructor_args():
    sig = inspect.signature(r1::OverlapsAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::overlapsafter_has_precision():
    assert hasattr(r1::OverlapsAfter, "precision")
    descriptor = None
    for klass in r1::OverlapsAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::after_is_not_abstract():
    assert not inspect.isabstract(r1::After)


def test_r1::after_constructor_exists():
    assert callable(r1::After.__init__)


def test_r1::after_constructor_args():
    sig = inspect.signature(r1::After.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::after_has_precision():
    assert hasattr(r1::After, "precision")
    descriptor = None
    for klass in r1::After.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::multiply_is_not_abstract():
    assert not inspect.isabstract(r1::Multiply)


def test_r1::multiply_constructor_exists():
    assert callable(r1::Multiply.__init__)


def test_r1::multiply_constructor_args():
    sig = inspect.signature(r1::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_r1::equal_is_not_abstract():
    assert not inspect.isabstract(r1::Equal)


def test_r1::equal_constructor_exists():
    assert callable(r1::Equal.__init__)


def test_r1::equal_constructor_args():
    sig = inspect.signature(r1::Equal.__init__)
    params = list(sig.parameters.keys())



def test_r1::includes_is_not_abstract():
    assert not inspect.isabstract(r1::Includes)


def test_r1::includes_constructor_exists():
    assert callable(r1::Includes.__init__)


def test_r1::includes_constructor_args():
    sig = inspect.signature(r1::Includes.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::includes_has_precision():
    assert hasattr(r1::Includes, "precision")
    descriptor = None
    for klass in r1::Includes.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::properincludedin_is_not_abstract():
    assert not inspect.isabstract(r1::ProperIncludedIn)


def test_r1::properincludedin_constructor_exists():
    assert callable(r1::ProperIncludedIn.__init__)


def test_r1::properincludedin_constructor_args():
    sig = inspect.signature(r1::ProperIncludedIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::properincludedin_has_precision():
    assert hasattr(r1::ProperIncludedIn, "precision")
    descriptor = None
    for klass in r1::ProperIncludedIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::indexer_is_not_abstract():
    assert not inspect.isabstract(r1::Indexer)


def test_r1::indexer_constructor_exists():
    assert callable(r1::Indexer.__init__)


def test_r1::indexer_constructor_args():
    sig = inspect.signature(r1::Indexer.__init__)
    params = list(sig.parameters.keys())



def test_r1::includedin_is_not_abstract():
    assert not inspect.isabstract(r1::IncludedIn)


def test_r1::includedin_constructor_exists():
    assert callable(r1::IncludedIn.__init__)


def test_r1::includedin_constructor_args():
    sig = inspect.signature(r1::IncludedIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::includedin_has_precision():
    assert hasattr(r1::IncludedIn, "precision")
    descriptor = None
    for klass in r1::IncludedIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::subtract_is_not_abstract():
    assert not inspect.isabstract(r1::Subtract)


def test_r1::subtract_constructor_exists():
    assert callable(r1::Subtract.__init__)


def test_r1::subtract_constructor_args():
    sig = inspect.signature(r1::Subtract.__init__)
    params = list(sig.parameters.keys())



def test_r1::intersect_is_not_abstract():
    assert not inspect.isabstract(r1::Intersect)


def test_r1::intersect_constructor_exists():
    assert callable(r1::Intersect.__init__)


def test_r1::intersect_constructor_args():
    sig = inspect.signature(r1::Intersect.__init__)
    params = list(sig.parameters.keys())



def test_r1::sameas_is_not_abstract():
    assert not inspect.isabstract(r1::SameAs)


def test_r1::sameas_constructor_exists():
    assert callable(r1::SameAs.__init__)


def test_r1::sameas_constructor_args():
    sig = inspect.signature(r1::SameAs.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::sameas_has_precision():
    assert hasattr(r1::SameAs, "precision")
    descriptor = None
    for klass in r1::SameAs.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::modulo_is_not_abstract():
    assert not inspect.isabstract(r1::Modulo)


def test_r1::modulo_constructor_exists():
    assert callable(r1::Modulo.__init__)


def test_r1::modulo_constructor_args():
    sig = inspect.signature(r1::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_r1::lessorequal_is_not_abstract():
    assert not inspect.isabstract(r1::LessOrEqual)


def test_r1::lessorequal_constructor_exists():
    assert callable(r1::LessOrEqual.__init__)


def test_r1::lessorequal_constructor_args():
    sig = inspect.signature(r1::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1::xor_is_not_abstract():
    assert not inspect.isabstract(r1::Xor)


def test_r1::xor_constructor_exists():
    assert callable(r1::Xor.__init__)


def test_r1::xor_constructor_args():
    sig = inspect.signature(r1::Xor.__init__)
    params = list(sig.parameters.keys())



def test_r1::sameorbefore_is_not_abstract():
    assert not inspect.isabstract(r1::SameOrBefore)


def test_r1::sameorbefore_constructor_exists():
    assert callable(r1::SameOrBefore.__init__)


def test_r1::sameorbefore_constructor_args():
    sig = inspect.signature(r1::SameOrBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::sameorbefore_has_precision():
    assert hasattr(r1::SameOrBefore, "precision")
    descriptor = None
    for klass in r1::SameOrBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::in_is_not_abstract():
    assert not inspect.isabstract(r1::In)


def test_r1::in_constructor_exists():
    assert callable(r1::In.__init__)


def test_r1::in_constructor_args():
    sig = inspect.signature(r1::In.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::in_has_precision():
    assert hasattr(r1::In, "precision")
    descriptor = None
    for klass in r1::In.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::matches_is_not_abstract():
    assert not inspect.isabstract(r1::Matches)


def test_r1::matches_constructor_exists():
    assert callable(r1::Matches.__init__)


def test_r1::matches_constructor_args():
    sig = inspect.signature(r1::Matches.__init__)
    params = list(sig.parameters.keys())



def test_r1::meetsbefore_is_not_abstract():
    assert not inspect.isabstract(r1::MeetsBefore)


def test_r1::meetsbefore_constructor_exists():
    assert callable(r1::MeetsBefore.__init__)


def test_r1::meetsbefore_constructor_args():
    sig = inspect.signature(r1::MeetsBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::meetsbefore_has_precision():
    assert hasattr(r1::MeetsBefore, "precision")
    descriptor = None
    for klass in r1::MeetsBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::greaterorequal_is_not_abstract():
    assert not inspect.isabstract(r1::GreaterOrEqual)


def test_r1::greaterorequal_constructor_exists():
    assert callable(r1::GreaterOrEqual.__init__)


def test_r1::greaterorequal_constructor_args():
    sig = inspect.signature(r1::GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1::calculateageat_is_not_abstract():
    assert not inspect.isabstract(r1::CalculateAgeAt)


def test_r1::calculateageat_constructor_exists():
    assert callable(r1::CalculateAgeAt.__init__)


def test_r1::calculateageat_constructor_args():
    sig = inspect.signature(r1::CalculateAgeAt.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::calculateageat_has_precision():
    assert hasattr(r1::CalculateAgeAt, "precision")
    descriptor = None
    for klass in r1::CalculateAgeAt.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::overlapsbefore_is_not_abstract():
    assert not inspect.isabstract(r1::OverlapsBefore)


def test_r1::overlapsbefore_constructor_exists():
    assert callable(r1::OverlapsBefore.__init__)


def test_r1::overlapsbefore_constructor_args():
    sig = inspect.signature(r1::OverlapsBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::overlapsbefore_has_precision():
    assert hasattr(r1::OverlapsBefore, "precision")
    descriptor = None
    for klass in r1::OverlapsBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::less_is_not_abstract():
    assert not inspect.isabstract(r1::Less)


def test_r1::less_constructor_exists():
    assert callable(r1::Less.__init__)


def test_r1::less_constructor_args():
    sig = inspect.signature(r1::Less.__init__)
    params = list(sig.parameters.keys())



def test_r1::sameorafter_is_not_abstract():
    assert not inspect.isabstract(r1::SameOrAfter)


def test_r1::sameorafter_constructor_exists():
    assert callable(r1::SameOrAfter.__init__)


def test_r1::sameorafter_constructor_args():
    sig = inspect.signature(r1::SameOrAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::sameorafter_has_precision():
    assert hasattr(r1::SameOrAfter, "precision")
    descriptor = None
    for klass in r1::SameOrAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::greater_is_not_abstract():
    assert not inspect.isabstract(r1::Greater)


def test_r1::greater_constructor_exists():
    assert callable(r1::Greater.__init__)


def test_r1::greater_constructor_args():
    sig = inspect.signature(r1::Greater.__init__)
    params = list(sig.parameters.keys())



def test_r1::ends_is_not_abstract():
    assert not inspect.isabstract(r1::Ends)


def test_r1::ends_constructor_exists():
    assert callable(r1::Ends.__init__)


def test_r1::ends_constructor_args():
    sig = inspect.signature(r1::Ends.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::ends_has_precision():
    assert hasattr(r1::Ends, "precision")
    descriptor = None
    for klass in r1::Ends.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::meets_is_not_abstract():
    assert not inspect.isabstract(r1::Meets)


def test_r1::meets_constructor_exists():
    assert callable(r1::Meets.__init__)


def test_r1::meets_constructor_args():
    sig = inspect.signature(r1::Meets.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::meets_has_precision():
    assert hasattr(r1::Meets, "precision")
    descriptor = None
    for klass in r1::Meets.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::truncateddivide_is_not_abstract():
    assert not inspect.isabstract(r1::TruncatedDivide)


def test_r1::truncateddivide_constructor_exists():
    assert callable(r1::TruncatedDivide.__init__)


def test_r1::truncateddivide_constructor_args():
    sig = inspect.signature(r1::TruncatedDivide.__init__)
    params = list(sig.parameters.keys())



def test_r1::power_is_not_abstract():
    assert not inspect.isabstract(r1::Power)


def test_r1::power_constructor_exists():
    assert callable(r1::Power.__init__)


def test_r1::power_constructor_args():
    sig = inspect.signature(r1::Power.__init__)
    params = list(sig.parameters.keys())



def test_r1::log_is_not_abstract():
    assert not inspect.isabstract(r1::Log)


def test_r1::log_constructor_exists():
    assert callable(r1::Log.__init__)


def test_r1::log_constructor_args():
    sig = inspect.signature(r1::Log.__init__)
    params = list(sig.parameters.keys())



def test_r1::except_is_not_abstract():
    assert not inspect.isabstract(r1::Except)


def test_r1::except_constructor_exists():
    assert callable(r1::Except.__init__)


def test_r1::except_constructor_args():
    sig = inspect.signature(r1::Except.__init__)
    params = list(sig.parameters.keys())



def test_r1::divide_is_not_abstract():
    assert not inspect.isabstract(r1::Divide)


def test_r1::divide_constructor_exists():
    assert callable(r1::Divide.__init__)


def test_r1::divide_constructor_args():
    sig = inspect.signature(r1::Divide.__init__)
    params = list(sig.parameters.keys())



def test_r1::differencebetween_is_not_abstract():
    assert not inspect.isabstract(r1::DifferenceBetween)


def test_r1::differencebetween_constructor_exists():
    assert callable(r1::DifferenceBetween.__init__)


def test_r1::differencebetween_constructor_args():
    sig = inspect.signature(r1::DifferenceBetween.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::differencebetween_has_precision():
    assert hasattr(r1::DifferenceBetween, "precision")
    descriptor = None
    for klass in r1::DifferenceBetween.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::and_is_not_abstract():
    assert not inspect.isabstract(r1::And)


def test_r1::and_constructor_exists():
    assert callable(r1::And.__init__)


def test_r1::and_constructor_args():
    sig = inspect.signature(r1::And.__init__)
    params = list(sig.parameters.keys())



def test_r1::durationbetween_is_not_abstract():
    assert not inspect.isabstract(r1::DurationBetween)


def test_r1::durationbetween_constructor_exists():
    assert callable(r1::DurationBetween.__init__)


def test_r1::durationbetween_constructor_args():
    sig = inspect.signature(r1::DurationBetween.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::durationbetween_has_precision():
    assert hasattr(r1::DurationBetween, "precision")
    descriptor = None
    for klass in r1::DurationBetween.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::union_is_not_abstract():
    assert not inspect.isabstract(r1::Union)


def test_r1::union_constructor_exists():
    assert callable(r1::Union.__init__)


def test_r1::union_constructor_args():
    sig = inspect.signature(r1::Union.__init__)
    params = list(sig.parameters.keys())



def test_r1::contains_is_not_abstract():
    assert not inspect.isabstract(r1::Contains)


def test_r1::contains_constructor_exists():
    assert callable(r1::Contains.__init__)


def test_r1::contains_constructor_args():
    sig = inspect.signature(r1::Contains.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::contains_has_precision():
    assert hasattr(r1::Contains, "precision")
    descriptor = None
    for klass in r1::Contains.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::properin_is_not_abstract():
    assert not inspect.isabstract(r1::ProperIn)


def test_r1::properin_constructor_exists():
    assert callable(r1::ProperIn.__init__)


def test_r1::properin_constructor_args():
    sig = inspect.signature(r1::ProperIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::properin_has_precision():
    assert hasattr(r1::ProperIn, "precision")
    descriptor = None
    for klass in r1::ProperIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::or_is_not_abstract():
    assert not inspect.isabstract(r1::Or)


def test_r1::or_constructor_exists():
    assert callable(r1::Or.__init__)


def test_r1::or_constructor_args():
    sig = inspect.signature(r1::Or.__init__)
    params = list(sig.parameters.keys())



def test_r1::add_is_not_abstract():
    assert not inspect.isabstract(r1::Add)


def test_r1::add_constructor_exists():
    assert callable(r1::Add.__init__)


def test_r1::add_constructor_args():
    sig = inspect.signature(r1::Add.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1::datefrom_is_not_abstract():
    assert not inspect.isabstract(r1::DateFrom)


def test_r1::datefrom_constructor_exists():
    assert callable(r1::DateFrom.__init__)


def test_r1::datefrom_constructor_args():
    sig = inspect.signature(r1::DateFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1::ln_is_not_abstract():
    assert not inspect.isabstract(r1::Ln)


def test_r1::ln_constructor_exists():
    assert callable(r1::Ln.__init__)


def test_r1::ln_constructor_args():
    sig = inspect.signature(r1::Ln.__init__)
    params = list(sig.parameters.keys())



def test_r1::istrue_is_not_abstract():
    assert not inspect.isabstract(r1::IsTrue)


def test_r1::istrue_constructor_exists():
    assert callable(r1::IsTrue.__init__)


def test_r1::istrue_constructor_args():
    sig = inspect.signature(r1::IsTrue.__init__)
    params = list(sig.parameters.keys())



def test_r1::exists_is_not_abstract():
    assert not inspect.isabstract(r1::Exists)


def test_r1::exists_constructor_exists():
    assert callable(r1::Exists.__init__)


def test_r1::exists_constructor_args():
    sig = inspect.signature(r1::Exists.__init__)
    params = list(sig.parameters.keys())



def test_r1::isfalse_is_not_abstract():
    assert not inspect.isabstract(r1::IsFalse)


def test_r1::isfalse_constructor_exists():
    assert callable(r1::IsFalse.__init__)


def test_r1::isfalse_constructor_args():
    sig = inspect.signature(r1::IsFalse.__init__)
    params = list(sig.parameters.keys())



def test_r1::length_is_not_abstract():
    assert not inspect.isabstract(r1::Length)


def test_r1::length_constructor_exists():
    assert callable(r1::Length.__init__)


def test_r1::length_constructor_args():
    sig = inspect.signature(r1::Length.__init__)
    params = list(sig.parameters.keys())



def test_r1::floor_is_not_abstract():
    assert not inspect.isabstract(r1::Floor)


def test_r1::floor_constructor_exists():
    assert callable(r1::Floor.__init__)


def test_r1::floor_constructor_args():
    sig = inspect.signature(r1::Floor.__init__)
    params = list(sig.parameters.keys())



def test_r1::timezonefrom_is_not_abstract():
    assert not inspect.isabstract(r1::TimezoneFrom)


def test_r1::timezonefrom_constructor_exists():
    assert callable(r1::TimezoneFrom.__init__)


def test_r1::timezonefrom_constructor_args():
    sig = inspect.signature(r1::TimezoneFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1::lower_is_not_abstract():
    assert not inspect.isabstract(r1::Lower)


def test_r1::lower_constructor_exists():
    assert callable(r1::Lower.__init__)


def test_r1::lower_constructor_args():
    sig = inspect.signature(r1::Lower.__init__)
    params = list(sig.parameters.keys())



def test_r1::end_is_not_abstract():
    assert not inspect.isabstract(r1::End)


def test_r1::end_constructor_exists():
    assert callable(r1::End.__init__)


def test_r1::end_constructor_args():
    sig = inspect.signature(r1::End.__init__)
    params = list(sig.parameters.keys())



def test_r1::truncate_is_not_abstract():
    assert not inspect.isabstract(r1::Truncate)


def test_r1::truncate_constructor_exists():
    assert callable(r1::Truncate.__init__)


def test_r1::truncate_constructor_args():
    sig = inspect.signature(r1::Truncate.__init__)
    params = list(sig.parameters.keys())



def test_r1::expand_is_not_abstract():
    assert not inspect.isabstract(r1::Expand)


def test_r1::expand_constructor_exists():
    assert callable(r1::Expand.__init__)


def test_r1::expand_constructor_args():
    sig = inspect.signature(r1::Expand.__init__)
    params = list(sig.parameters.keys())



def test_r1::successor_is_not_abstract():
    assert not inspect.isabstract(r1::Successor)


def test_r1::successor_constructor_exists():
    assert callable(r1::Successor.__init__)


def test_r1::successor_constructor_args():
    sig = inspect.signature(r1::Successor.__init__)
    params = list(sig.parameters.keys())



def test_r1::distinct_is_not_abstract():
    assert not inspect.isabstract(r1::Distinct)


def test_r1::distinct_constructor_exists():
    assert callable(r1::Distinct.__init__)


def test_r1::distinct_constructor_args():
    sig = inspect.signature(r1::Distinct.__init__)
    params = list(sig.parameters.keys())



def test_r1::negate_is_not_abstract():
    assert not inspect.isabstract(r1::Negate)


def test_r1::negate_constructor_exists():
    assert callable(r1::Negate.__init__)


def test_r1::negate_constructor_args():
    sig = inspect.signature(r1::Negate.__init__)
    params = list(sig.parameters.keys())



def test_r1::as_is_not_abstract():
    assert not inspect.isabstract(r1::As)


def test_r1::as_constructor_exists():
    assert callable(r1::As.__init__)


def test_r1::as_constructor_args():
    sig = inspect.signature(r1::As.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "asType" in params, "Missing parameter 'asType'"

def test_r1::as_has_strict():
    assert hasattr(r1::As, "strict")
    descriptor = None
    for klass in r1::As.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_r1::as_has_asType():
    assert hasattr(r1::As, "asType")
    descriptor = None
    for klass in r1::As.__mro__:
        if "asType" in klass.__dict__:
            descriptor = klass.__dict__["asType"]
            break
    assert isinstance(descriptor, property)



def test_r1::convert_is_not_abstract():
    assert not inspect.isabstract(r1::Convert)


def test_r1::convert_constructor_exists():
    assert callable(r1::Convert.__init__)


def test_r1::convert_constructor_args():
    sig = inspect.signature(r1::Convert.__init__)
    params = list(sig.parameters.keys())
    assert "toType" in params, "Missing parameter 'toType'"

def test_r1::convert_has_toType():
    assert hasattr(r1::Convert, "toType")
    descriptor = None
    for klass in r1::Convert.__mro__:
        if "toType" in klass.__dict__:
            descriptor = klass.__dict__["toType"]
            break
    assert isinstance(descriptor, property)



def test_r1::not_is_not_abstract():
    assert not inspect.isabstract(r1::Not)


def test_r1::not_constructor_exists():
    assert callable(r1::Not.__init__)


def test_r1::not_constructor_args():
    sig = inspect.signature(r1::Not.__init__)
    params = list(sig.parameters.keys())



def test_r1::datetimecomponentfrom_is_not_abstract():
    assert not inspect.isabstract(r1::DateTimeComponentFrom)


def test_r1::datetimecomponentfrom_constructor_exists():
    assert callable(r1::DateTimeComponentFrom.__init__)


def test_r1::datetimecomponentfrom_constructor_args():
    sig = inspect.signature(r1::DateTimeComponentFrom.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::datetimecomponentfrom_has_precision():
    assert hasattr(r1::DateTimeComponentFrom, "precision")
    descriptor = None
    for klass in r1::DateTimeComponentFrom.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::width_is_not_abstract():
    assert not inspect.isabstract(r1::Width)


def test_r1::width_constructor_exists():
    assert callable(r1::Width.__init__)


def test_r1::width_constructor_args():
    sig = inspect.signature(r1::Width.__init__)
    params = list(sig.parameters.keys())



def test_r1::is_is_not_abstract():
    assert not inspect.isabstract(r1::Is)


def test_r1::is_constructor_exists():
    assert callable(r1::Is.__init__)


def test_r1::is_constructor_args():
    sig = inspect.signature(r1::Is.__init__)
    params = list(sig.parameters.keys())
    assert "isType" in params, "Missing parameter 'isType'"

def test_r1::is_has_isType():
    assert hasattr(r1::Is, "isType")
    descriptor = None
    for klass in r1::Is.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)



def test_r1::calculateage_is_not_abstract():
    assert not inspect.isabstract(r1::CalculateAge)


def test_r1::calculateage_constructor_exists():
    assert callable(r1::CalculateAge.__init__)


def test_r1::calculateage_constructor_args():
    sig = inspect.signature(r1::CalculateAge.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1::calculateage_has_precision():
    assert hasattr(r1::CalculateAge, "precision")
    descriptor = None
    for klass in r1::CalculateAge.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1::ceiling_is_not_abstract():
    assert not inspect.isabstract(r1::Ceiling)


def test_r1::ceiling_constructor_exists():
    assert callable(r1::Ceiling.__init__)


def test_r1::ceiling_constructor_args():
    sig = inspect.signature(r1::Ceiling.__init__)
    params = list(sig.parameters.keys())



def test_r1::singletonfrom_is_not_abstract():
    assert not inspect.isabstract(r1::SingletonFrom)


def test_r1::singletonfrom_constructor_exists():
    assert callable(r1::SingletonFrom.__init__)


def test_r1::singletonfrom_constructor_args():
    sig = inspect.signature(r1::SingletonFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1::timefrom_is_not_abstract():
    assert not inspect.isabstract(r1::TimeFrom)


def test_r1::timefrom_constructor_exists():
    assert callable(r1::TimeFrom.__init__)


def test_r1::timefrom_constructor_args():
    sig = inspect.signature(r1::TimeFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1::collapse_is_not_abstract():
    assert not inspect.isabstract(r1::Collapse)


def test_r1::collapse_constructor_exists():
    assert callable(r1::Collapse.__init__)


def test_r1::collapse_constructor_args():
    sig = inspect.signature(r1::Collapse.__init__)
    params = list(sig.parameters.keys())



def test_r1::predecessor_is_not_abstract():
    assert not inspect.isabstract(r1::Predecessor)


def test_r1::predecessor_constructor_exists():
    assert callable(r1::Predecessor.__init__)


def test_r1::predecessor_constructor_args():
    sig = inspect.signature(r1::Predecessor.__init__)
    params = list(sig.parameters.keys())



def test_r1::upper_is_not_abstract():
    assert not inspect.isabstract(r1::Upper)


def test_r1::upper_constructor_exists():
    assert callable(r1::Upper.__init__)


def test_r1::upper_constructor_args():
    sig = inspect.signature(r1::Upper.__init__)
    params = list(sig.parameters.keys())



def test_r1::start_is_not_abstract():
    assert not inspect.isabstract(r1::Start)


def test_r1::start_constructor_exists():
    assert callable(r1::Start.__init__)


def test_r1::start_constructor_args():
    sig = inspect.signature(r1::Start.__init__)
    params = list(sig.parameters.keys())



def test_r1::isnull_is_not_abstract():
    assert not inspect.isabstract(r1::IsNull)


def test_r1::isnull_constructor_exists():
    assert callable(r1::IsNull.__init__)


def test_r1::isnull_constructor_args():
    sig = inspect.signature(r1::IsNull.__init__)
    params = list(sig.parameters.keys())



def test_r1::abs_is_not_abstract():
    assert not inspect.isabstract(r1::Abs)


def test_r1::abs_constructor_exists():
    assert callable(r1::Abs.__init__)


def test_r1::abs_constructor_args():
    sig = inspect.signature(r1::Abs.__init__)
    params = list(sig.parameters.keys())

def test_sortdirection_exists():
    # Check that the Enumeration exists
    assert SortDirection is not None

def test_sortdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortDirection]
    expected_literals = [
        "asc",
        "desc",
        "ascending",
        "descending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortDirection"

def test_datetimeprecision_exists():
    # Check that the Enumeration exists
    assert DateTimePrecision is not None

def test_datetimeprecision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateTimePrecision]
    expected_literals = [
        "Hour",
        "Year",
        "Day",
        "Second",
        "Month",
        "Week",
        "Millisecond",
        "Minute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateTimePrecision"

def test_accessmodifier_exists():
    # Check that the Enumeration exists
    assert AccessModifier is not None

def test_accessmodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifier]
    expected_literals = [
        "Private",
        "Public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifier"


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
RelationshipClause_strategy = st.builds(
    RelationshipClause,
)
r1::Without_strategy = st.builds(
    r1::Without,
)
r1::With_strategy = st.builds(
    r1::With,
)
r1::TupleElement_strategy = st.builds(
    r1::TupleElement,
    name=
        safe_text
)
AliasedQuerySource_strategy = st.builds(
    AliasedQuerySource,
)
r1::RelationshipClause_strategy = st.builds(
    r1::RelationshipClause,
)
TypeSpecifier_strategy = st.builds(
    TypeSpecifier,
)
r1::ListTypeSpecifier_strategy = st.builds(
    r1::ListTypeSpecifier,
)
r1::NamedTypeSpecifier_strategy = st.builds(
    r1::NamedTypeSpecifier,
    name=
        safe_text
)
r1::TupleTypeSpecifier_strategy = st.builds(
    r1::TupleTypeSpecifier,
)
r1::IntervalTypeSpecifier_strategy = st.builds(
    r1::IntervalTypeSpecifier,
)
r1::InstanceElement_strategy = st.builds(
    r1::InstanceElement,
    name=
        safe_text
)
ExpressionDef_strategy = st.builds(
    ExpressionDef,
)
r1::FunctionDef_strategy = st.builds(
    r1::FunctionDef,
)
ExpressionRef_strategy = st.builds(
    ExpressionRef,
)
r1::FunctionRef_strategy = st.builds(
    r1::FunctionRef,
)
r1::EObject_strategy = st.builds(
    r1::EObject,
)
r1::Element_strategy = st.builds(
    r1::Element,
    localId=
        safe_text
)
NaryExpression_strategy = st.builds(
    NaryExpression,
)
r1::Concatenate_strategy = st.builds(
    r1::Concatenate,
)
r1::Coalesce_strategy = st.builds(
    r1::Coalesce,
)
AggregateExpression_strategy = st.builds(
    AggregateExpression,
)
r1::PopulationStdDev_strategy = st.builds(
    r1::PopulationStdDev,
)
r1::Median_strategy = st.builds(
    r1::Median,
)
r1::StdDev_strategy = st.builds(
    r1::StdDev,
)
r1::Variance_strategy = st.builds(
    r1::Variance,
)
r1::Mode_strategy = st.builds(
    r1::Mode,
)
r1::Avg_strategy = st.builds(
    r1::Avg,
)
r1::PopulationVariance_strategy = st.builds(
    r1::PopulationVariance,
)
r1::Max_strategy = st.builds(
    r1::Max,
)
r1::Min_strategy = st.builds(
    r1::Min,
)
r1::Count_strategy = st.builds(
    r1::Count,
)
r1::AnyTrue_strategy = st.builds(
    r1::AnyTrue,
)
r1::Sum_strategy = st.builds(
    r1::Sum,
)
r1::AllTrue_strategy = st.builds(
    r1::AllTrue,
)
SortByItem_strategy = st.builds(
    SortByItem,
)
r1::ByDirection_strategy = st.builds(
    r1::ByDirection,
)
r1::ByExpression_strategy = st.builds(
    r1::ByExpression,
)
r1::ByColumn_strategy = st.builds(
    r1::ByColumn,
    path=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
r1::DefineClause_strategy = st.builds(
    r1::DefineClause,
    identifier=
        safe_text
)
r1::SortByItem_strategy = st.builds(
    r1::SortByItem,
    direction=
        safe_text
)
r1::CaseItem_strategy = st.builds(
    r1::CaseItem,
)
r1::CodeSystemDef_strategy = st.builds(
    r1::CodeSystemDef,
    accessLevel=
        safe_text,
    version=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
r1::ValueSetDef_strategy = st.builds(
    r1::ValueSetDef,
    id=
        safe_text,
    accessLevel=
        safe_text,
    name=
        safe_text,
    version=
        safe_text
)
r1::ReturnClause_strategy = st.builds(
    r1::ReturnClause,
    distinct=
        safe_text
)
r1::ParameterDef_strategy = st.builds(
    r1::ParameterDef,
    name=
        safe_text,
    accessLevel=
        safe_text,
    parameterType=
        safe_text
)
r1::SortClause_strategy = st.builds(
    r1::SortClause,
)
r1::OperandDef_strategy = st.builds(
    r1::OperandDef,
    operandType=
        safe_text,
    name=
        safe_text
)
r1::TypeSpecifier_strategy = st.builds(
    r1::TypeSpecifier,
)
r1::ExpressionDef_strategy = st.builds(
    r1::ExpressionDef,
    accessLevel=
        safe_text,
    context=
        safe_text,
    name=
        safe_text
)
r1::TupleElementDefinition_strategy = st.builds(
    r1::TupleElementDefinition,
    name=
        safe_text
)
r1::AliasedQuerySource_strategy = st.builds(
    r1::AliasedQuerySource,
    alias=
        safe_text
)
r1::Expression_strategy = st.builds(
    r1::Expression,
)
Expression_strategy = st.builds(
    Expression,
)
r1::PositionOf_strategy = st.builds(
    r1::PositionOf,
)
r1::ForEach_strategy = st.builds(
    r1::ForEach,
    scope=
        safe_text
)
r1::Code_strategy = st.builds(
    r1::Code,
    display=
        safe_text,
    code=
        safe_text
)
r1::DateTime_strategy = st.builds(
    r1::DateTime,
)
r1::Quantity_strategy = st.builds(
    r1::Quantity,
    value=
        safe_text,
    unit=
        safe_text
)
r1::AliasRef_strategy = st.builds(
    r1::AliasRef,
    name=
        safe_text
)
r1::MinValue_strategy = st.builds(
    r1::MinValue,
    valueType=
        safe_text
)
r1::CodeSystemRef_strategy = st.builds(
    r1::CodeSystemRef,
    name=
        safe_text,
    libraryName=
        safe_text
)
r1::Interval_strategy = st.builds(
    r1::Interval,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r1::Null_strategy = st.builds(
    r1::Null,
    valueType=
        safe_text
)
r1::First_strategy = st.builds(
    r1::First,
    orderBy=
        safe_text
)
r1::Case_strategy = st.builds(
    r1::Case,
)
r1::InValueSet_strategy = st.builds(
    r1::InValueSet,
)
r1::Today_strategy = st.builds(
    r1::Today,
)
r1::Substring_strategy = st.builds(
    r1::Substring,
)
r1::Current_strategy = st.builds(
    r1::Current,
    scope=
        safe_text
)
r1::QueryDefineRef_strategy = st.builds(
    r1::QueryDefineRef,
    name=
        safe_text
)
r1::Query_strategy = st.builds(
    r1::Query,
)
r1::List_strategy = st.builds(
    r1::List,
)
r1::TimeOfDay_strategy = st.builds(
    r1::TimeOfDay,
)
r1::Combine_strategy = st.builds(
    r1::Combine,
)
r1::Tuple_strategy = st.builds(
    r1::Tuple,
)
r1::ValueSetRef_strategy = st.builds(
    r1::ValueSetRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1::Time_strategy = st.builds(
    r1::Time,
)
r1::OperandRef_strategy = st.builds(
    r1::OperandRef,
    name=
        safe_text
)
r1::Concept_strategy = st.builds(
    r1::Concept,
    display=
        safe_text
)
r1::BinaryExpression_strategy = st.builds(
    r1::BinaryExpression,
)
r1::IndexOf_strategy = st.builds(
    r1::IndexOf,
)
r1::NaryExpression_strategy = st.builds(
    r1::NaryExpression,
)
r1::Filter_strategy = st.builds(
    r1::Filter,
    scope=
        safe_text
)
r1::Retrieve_strategy = st.builds(
    r1::Retrieve,
    dataType=
        safe_text,
    scope=
        safe_text,
    dateHighProperty=
        safe_text,
    templateId=
        safe_text,
    dateLowProperty=
        safe_text,
    dateProperty=
        safe_text,
    idProperty=
        safe_text,
    codeProperty=
        safe_text
)
r1::Last_strategy = st.builds(
    r1::Last,
    orderBy=
        safe_text
)
r1::Property_strategy = st.builds(
    r1::Property,
    scope=
        safe_text,
    path=
        safe_text
)
r1::UnaryExpression_strategy = st.builds(
    r1::UnaryExpression,
)
r1::MaxValue_strategy = st.builds(
    r1::MaxValue,
    valueType=
        safe_text
)
r1::Sort_strategy = st.builds(
    r1::Sort,
)
r1::Split_strategy = st.builds(
    r1::Split,
)
r1::Now_strategy = st.builds(
    r1::Now,
)
r1::InCodeSystem_strategy = st.builds(
    r1::InCodeSystem,
)
r1::Round_strategy = st.builds(
    r1::Round,
)
r1::If_strategy = st.builds(
    r1::If,
)
r1::ParameterRef_strategy = st.builds(
    r1::ParameterRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1::IdentifierRef_strategy = st.builds(
    r1::IdentifierRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1::Literal_strategy = st.builds(
    r1::Literal,
    valueType=
        safe_text,
    value=
        safe_text
)
r1::TernaryExpression_strategy = st.builds(
    r1::TernaryExpression,
)
r1::ExpressionRef_strategy = st.builds(
    r1::ExpressionRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1::Instance_strategy = st.builds(
    r1::Instance,
    classType=
        safe_text
)
r1::AggregateExpression_strategy = st.builds(
    r1::AggregateExpression,
    path=
        safe_text
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
r1::ProperContains_strategy = st.builds(
    r1::ProperContains,
    precision=
        safe_text
)
r1::NotEqual_strategy = st.builds(
    r1::NotEqual,
)
r1::Times_strategy = st.builds(
    r1::Times,
)
r1::MeetsAfter_strategy = st.builds(
    r1::MeetsAfter,
    precision=
        safe_text
)
r1::Before_strategy = st.builds(
    r1::Before,
    precision=
        safe_text
)
r1::Overlaps_strategy = st.builds(
    r1::Overlaps,
    precision=
        safe_text
)
r1::Starts_strategy = st.builds(
    r1::Starts,
    precision=
        safe_text
)
r1::ProperIncludes_strategy = st.builds(
    r1::ProperIncludes,
    precision=
        safe_text
)
r1::OverlapsAfter_strategy = st.builds(
    r1::OverlapsAfter,
    precision=
        safe_text
)
r1::After_strategy = st.builds(
    r1::After,
    precision=
        safe_text
)
r1::Multiply_strategy = st.builds(
    r1::Multiply,
)
r1::Equal_strategy = st.builds(
    r1::Equal,
)
r1::Includes_strategy = st.builds(
    r1::Includes,
    precision=
        safe_text
)
r1::ProperIncludedIn_strategy = st.builds(
    r1::ProperIncludedIn,
    precision=
        safe_text
)
r1::Indexer_strategy = st.builds(
    r1::Indexer,
)
r1::IncludedIn_strategy = st.builds(
    r1::IncludedIn,
    precision=
        safe_text
)
r1::Subtract_strategy = st.builds(
    r1::Subtract,
)
r1::Intersect_strategy = st.builds(
    r1::Intersect,
)
r1::SameAs_strategy = st.builds(
    r1::SameAs,
    precision=
        safe_text
)
r1::Modulo_strategy = st.builds(
    r1::Modulo,
)
r1::LessOrEqual_strategy = st.builds(
    r1::LessOrEqual,
)
r1::Xor_strategy = st.builds(
    r1::Xor,
)
r1::SameOrBefore_strategy = st.builds(
    r1::SameOrBefore,
    precision=
        safe_text
)
r1::In_strategy = st.builds(
    r1::In,
    precision=
        safe_text
)
r1::Matches_strategy = st.builds(
    r1::Matches,
)
r1::MeetsBefore_strategy = st.builds(
    r1::MeetsBefore,
    precision=
        safe_text
)
r1::GreaterOrEqual_strategy = st.builds(
    r1::GreaterOrEqual,
)
r1::CalculateAgeAt_strategy = st.builds(
    r1::CalculateAgeAt,
    precision=
        safe_text
)
r1::OverlapsBefore_strategy = st.builds(
    r1::OverlapsBefore,
    precision=
        safe_text
)
r1::Less_strategy = st.builds(
    r1::Less,
)
r1::SameOrAfter_strategy = st.builds(
    r1::SameOrAfter,
    precision=
        safe_text
)
r1::Greater_strategy = st.builds(
    r1::Greater,
)
r1::Ends_strategy = st.builds(
    r1::Ends,
    precision=
        safe_text
)
r1::Meets_strategy = st.builds(
    r1::Meets,
    precision=
        safe_text
)
r1::TruncatedDivide_strategy = st.builds(
    r1::TruncatedDivide,
)
r1::Power_strategy = st.builds(
    r1::Power,
)
r1::Log_strategy = st.builds(
    r1::Log,
)
r1::Except_strategy = st.builds(
    r1::Except,
)
r1::Divide_strategy = st.builds(
    r1::Divide,
)
r1::DifferenceBetween_strategy = st.builds(
    r1::DifferenceBetween,
    precision=
        safe_text
)
r1::And_strategy = st.builds(
    r1::And,
)
r1::DurationBetween_strategy = st.builds(
    r1::DurationBetween,
    precision=
        safe_text
)
r1::Union_strategy = st.builds(
    r1::Union,
)
r1::Contains_strategy = st.builds(
    r1::Contains,
    precision=
        safe_text
)
r1::ProperIn_strategy = st.builds(
    r1::ProperIn,
    precision=
        safe_text
)
r1::Or_strategy = st.builds(
    r1::Or,
)
r1::Add_strategy = st.builds(
    r1::Add,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
r1::DateFrom_strategy = st.builds(
    r1::DateFrom,
)
r1::Ln_strategy = st.builds(
    r1::Ln,
)
r1::IsTrue_strategy = st.builds(
    r1::IsTrue,
)
r1::Exists_strategy = st.builds(
    r1::Exists,
)
r1::IsFalse_strategy = st.builds(
    r1::IsFalse,
)
r1::Length_strategy = st.builds(
    r1::Length,
)
r1::Floor_strategy = st.builds(
    r1::Floor,
)
r1::TimezoneFrom_strategy = st.builds(
    r1::TimezoneFrom,
)
r1::Lower_strategy = st.builds(
    r1::Lower,
)
r1::End_strategy = st.builds(
    r1::End,
)
r1::Truncate_strategy = st.builds(
    r1::Truncate,
)
r1::Expand_strategy = st.builds(
    r1::Expand,
)
r1::Successor_strategy = st.builds(
    r1::Successor,
)
r1::Distinct_strategy = st.builds(
    r1::Distinct,
)
r1::Negate_strategy = st.builds(
    r1::Negate,
)
r1::As_strategy = st.builds(
    r1::As,
    strict=
        safe_text,
    asType=
        safe_text
)
r1::Convert_strategy = st.builds(
    r1::Convert,
    toType=
        safe_text
)
r1::Not_strategy = st.builds(
    r1::Not,
)
r1::DateTimeComponentFrom_strategy = st.builds(
    r1::DateTimeComponentFrom,
    precision=
        safe_text
)
r1::Width_strategy = st.builds(
    r1::Width,
)
r1::Is_strategy = st.builds(
    r1::Is,
    isType=
        safe_text
)
r1::CalculateAge_strategy = st.builds(
    r1::CalculateAge,
    precision=
        safe_text
)
r1::Ceiling_strategy = st.builds(
    r1::Ceiling,
)
r1::SingletonFrom_strategy = st.builds(
    r1::SingletonFrom,
)
r1::TimeFrom_strategy = st.builds(
    r1::TimeFrom,
)
r1::Collapse_strategy = st.builds(
    r1::Collapse,
)
r1::Predecessor_strategy = st.builds(
    r1::Predecessor,
)
r1::Upper_strategy = st.builds(
    r1::Upper,
)
r1::Start_strategy = st.builds(
    r1::Start,
)
r1::IsNull_strategy = st.builds(
    r1::IsNull,
)
r1::Abs_strategy = st.builds(
    r1::Abs,
)

@given(instance=RelationshipClause_strategy)
@settings(max_examples=50)
def test_relationshipclause_instantiation(instance):
    assert isinstance(instance, RelationshipClause)

@given(instance=r1::Without_strategy)
@settings(max_examples=50)
def test_r1::without_instantiation(instance):
    assert isinstance(instance, r1::Without)

@given(instance=r1::With_strategy)
@settings(max_examples=50)
def test_r1::with_instantiation(instance):
    assert isinstance(instance, r1::With)

@given(instance=r1::TupleElement_strategy)
@settings(max_examples=50)
def test_r1::tupleelement_instantiation(instance):
    assert isinstance(instance, r1::TupleElement)

@given(instance=r1::TupleElement_strategy)
def test_r1::tupleelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::TupleElement_strategy)
def test_r1::tupleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AliasedQuerySource_strategy)
@settings(max_examples=50)
def test_aliasedquerysource_instantiation(instance):
    assert isinstance(instance, AliasedQuerySource)

@given(instance=r1::RelationshipClause_strategy)
@settings(max_examples=50)
def test_r1::relationshipclause_instantiation(instance):
    assert isinstance(instance, r1::RelationshipClause)

@given(instance=TypeSpecifier_strategy)
@settings(max_examples=50)
def test_typespecifier_instantiation(instance):
    assert isinstance(instance, TypeSpecifier)

@given(instance=r1::ListTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1::listtypespecifier_instantiation(instance):
    assert isinstance(instance, r1::ListTypeSpecifier)

@given(instance=r1::NamedTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1::namedtypespecifier_instantiation(instance):
    assert isinstance(instance, r1::NamedTypeSpecifier)

@given(instance=r1::NamedTypeSpecifier_strategy)
def test_r1::namedtypespecifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::NamedTypeSpecifier_strategy)
def test_r1::namedtypespecifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::TupleTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1::tupletypespecifier_instantiation(instance):
    assert isinstance(instance, r1::TupleTypeSpecifier)

@given(instance=r1::IntervalTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1::intervaltypespecifier_instantiation(instance):
    assert isinstance(instance, r1::IntervalTypeSpecifier)

@given(instance=r1::InstanceElement_strategy)
@settings(max_examples=50)
def test_r1::instanceelement_instantiation(instance):
    assert isinstance(instance, r1::InstanceElement)

@given(instance=r1::InstanceElement_strategy)
def test_r1::instanceelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::InstanceElement_strategy)
def test_r1::instanceelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpressionDef_strategy)
@settings(max_examples=50)
def test_expressiondef_instantiation(instance):
    assert isinstance(instance, ExpressionDef)

@given(instance=r1::FunctionDef_strategy)
@settings(max_examples=50)
def test_r1::functiondef_instantiation(instance):
    assert isinstance(instance, r1::FunctionDef)

@given(instance=ExpressionRef_strategy)
@settings(max_examples=50)
def test_expressionref_instantiation(instance):
    assert isinstance(instance, ExpressionRef)

@given(instance=r1::FunctionRef_strategy)
@settings(max_examples=50)
def test_r1::functionref_instantiation(instance):
    assert isinstance(instance, r1::FunctionRef)

@given(instance=r1::EObject_strategy)
@settings(max_examples=50)
def test_r1::eobject_instantiation(instance):
    assert isinstance(instance, r1::EObject)

@given(instance=r1::Element_strategy)
@settings(max_examples=50)
def test_r1::element_instantiation(instance):
    assert isinstance(instance, r1::Element)

@given(instance=r1::Element_strategy)
def test_r1::element_localId_type(instance):
    assert isinstance(instance.localId, str)


@given(instance=r1::Element_strategy)
def test_r1::element_localId_setter(instance):
    original = instance.localId
    instance.localId = original
    assert instance.localId == original

@given(instance=NaryExpression_strategy)
@settings(max_examples=50)
def test_naryexpression_instantiation(instance):
    assert isinstance(instance, NaryExpression)

@given(instance=r1::Concatenate_strategy)
@settings(max_examples=50)
def test_r1::concatenate_instantiation(instance):
    assert isinstance(instance, r1::Concatenate)

@given(instance=r1::Coalesce_strategy)
@settings(max_examples=50)
def test_r1::coalesce_instantiation(instance):
    assert isinstance(instance, r1::Coalesce)

@given(instance=AggregateExpression_strategy)
@settings(max_examples=50)
def test_aggregateexpression_instantiation(instance):
    assert isinstance(instance, AggregateExpression)

@given(instance=r1::PopulationStdDev_strategy)
@settings(max_examples=50)
def test_r1::populationstddev_instantiation(instance):
    assert isinstance(instance, r1::PopulationStdDev)

@given(instance=r1::Median_strategy)
@settings(max_examples=50)
def test_r1::median_instantiation(instance):
    assert isinstance(instance, r1::Median)

@given(instance=r1::StdDev_strategy)
@settings(max_examples=50)
def test_r1::stddev_instantiation(instance):
    assert isinstance(instance, r1::StdDev)

@given(instance=r1::Variance_strategy)
@settings(max_examples=50)
def test_r1::variance_instantiation(instance):
    assert isinstance(instance, r1::Variance)

@given(instance=r1::Mode_strategy)
@settings(max_examples=50)
def test_r1::mode_instantiation(instance):
    assert isinstance(instance, r1::Mode)

@given(instance=r1::Avg_strategy)
@settings(max_examples=50)
def test_r1::avg_instantiation(instance):
    assert isinstance(instance, r1::Avg)

@given(instance=r1::PopulationVariance_strategy)
@settings(max_examples=50)
def test_r1::populationvariance_instantiation(instance):
    assert isinstance(instance, r1::PopulationVariance)

@given(instance=r1::Max_strategy)
@settings(max_examples=50)
def test_r1::max_instantiation(instance):
    assert isinstance(instance, r1::Max)

@given(instance=r1::Min_strategy)
@settings(max_examples=50)
def test_r1::min_instantiation(instance):
    assert isinstance(instance, r1::Min)

@given(instance=r1::Count_strategy)
@settings(max_examples=50)
def test_r1::count_instantiation(instance):
    assert isinstance(instance, r1::Count)

@given(instance=r1::AnyTrue_strategy)
@settings(max_examples=50)
def test_r1::anytrue_instantiation(instance):
    assert isinstance(instance, r1::AnyTrue)

@given(instance=r1::Sum_strategy)
@settings(max_examples=50)
def test_r1::sum_instantiation(instance):
    assert isinstance(instance, r1::Sum)

@given(instance=r1::AllTrue_strategy)
@settings(max_examples=50)
def test_r1::alltrue_instantiation(instance):
    assert isinstance(instance, r1::AllTrue)

@given(instance=SortByItem_strategy)
@settings(max_examples=50)
def test_sortbyitem_instantiation(instance):
    assert isinstance(instance, SortByItem)

@given(instance=r1::ByDirection_strategy)
@settings(max_examples=50)
def test_r1::bydirection_instantiation(instance):
    assert isinstance(instance, r1::ByDirection)

@given(instance=r1::ByExpression_strategy)
@settings(max_examples=50)
def test_r1::byexpression_instantiation(instance):
    assert isinstance(instance, r1::ByExpression)

@given(instance=r1::ByColumn_strategy)
@settings(max_examples=50)
def test_r1::bycolumn_instantiation(instance):
    assert isinstance(instance, r1::ByColumn)

@given(instance=r1::ByColumn_strategy)
def test_r1::bycolumn_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=r1::ByColumn_strategy)
def test_r1::bycolumn_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=r1::DefineClause_strategy)
@settings(max_examples=50)
def test_r1::defineclause_instantiation(instance):
    assert isinstance(instance, r1::DefineClause)

@given(instance=r1::DefineClause_strategy)
def test_r1::defineclause_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=r1::DefineClause_strategy)
def test_r1::defineclause_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=r1::SortByItem_strategy)
@settings(max_examples=50)
def test_r1::sortbyitem_instantiation(instance):
    assert isinstance(instance, r1::SortByItem)

@given(instance=r1::SortByItem_strategy)
def test_r1::sortbyitem_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=r1::SortByItem_strategy)
def test_r1::sortbyitem_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=r1::CaseItem_strategy)
@settings(max_examples=50)
def test_r1::caseitem_instantiation(instance):
    assert isinstance(instance, r1::CaseItem)

@given(instance=r1::CodeSystemDef_strategy)
@settings(max_examples=50)
def test_r1::codesystemdef_instantiation(instance):
    assert isinstance(instance, r1::CodeSystemDef)

@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=r1::CodeSystemDef_strategy)
def test_r1::codesystemdef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=r1::ValueSetDef_strategy)
@settings(max_examples=50)
def test_r1::valuesetdef_instantiation(instance):
    assert isinstance(instance, r1::ValueSetDef)

@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=r1::ValueSetDef_strategy)
def test_r1::valuesetdef_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=r1::ReturnClause_strategy)
@settings(max_examples=50)
def test_r1::returnclause_instantiation(instance):
    assert isinstance(instance, r1::ReturnClause)

@given(instance=r1::ReturnClause_strategy)
def test_r1::returnclause_distinct_type(instance):
    assert isinstance(instance.distinct, str)


@given(instance=r1::ReturnClause_strategy)
def test_r1::returnclause_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=r1::ParameterDef_strategy)
@settings(max_examples=50)
def test_r1::parameterdef_instantiation(instance):
    assert isinstance(instance, r1::ParameterDef)

@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_parameterType_type(instance):
    assert isinstance(instance.parameterType, str)


@given(instance=r1::ParameterDef_strategy)
def test_r1::parameterdef_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=r1::SortClause_strategy)
@settings(max_examples=50)
def test_r1::sortclause_instantiation(instance):
    assert isinstance(instance, r1::SortClause)

@given(instance=r1::OperandDef_strategy)
@settings(max_examples=50)
def test_r1::operanddef_instantiation(instance):
    assert isinstance(instance, r1::OperandDef)

@given(instance=r1::OperandDef_strategy)
def test_r1::operanddef_operandType_type(instance):
    assert isinstance(instance.operandType, str)


@given(instance=r1::OperandDef_strategy)
def test_r1::operanddef_operandType_setter(instance):
    original = instance.operandType
    instance.operandType = original
    assert instance.operandType == original

@given(instance=r1::OperandDef_strategy)
def test_r1::operanddef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::OperandDef_strategy)
def test_r1::operanddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::TypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1::typespecifier_instantiation(instance):
    assert isinstance(instance, r1::TypeSpecifier)

@given(instance=r1::ExpressionDef_strategy)
@settings(max_examples=50)
def test_r1::expressiondef_instantiation(instance):
    assert isinstance(instance, r1::ExpressionDef)

@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ExpressionDef_strategy)
def test_r1::expressiondef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::TupleElementDefinition_strategy)
@settings(max_examples=50)
def test_r1::tupleelementdefinition_instantiation(instance):
    assert isinstance(instance, r1::TupleElementDefinition)

@given(instance=r1::TupleElementDefinition_strategy)
def test_r1::tupleelementdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::TupleElementDefinition_strategy)
def test_r1::tupleelementdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::AliasedQuerySource_strategy)
@settings(max_examples=50)
def test_r1::aliasedquerysource_instantiation(instance):
    assert isinstance(instance, r1::AliasedQuerySource)

@given(instance=r1::AliasedQuerySource_strategy)
def test_r1::aliasedquerysource_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=r1::AliasedQuerySource_strategy)
def test_r1::aliasedquerysource_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=r1::Expression_strategy)
@settings(max_examples=50)
def test_r1::expression_instantiation(instance):
    assert isinstance(instance, r1::Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=r1::PositionOf_strategy)
@settings(max_examples=50)
def test_r1::positionof_instantiation(instance):
    assert isinstance(instance, r1::PositionOf)

@given(instance=r1::ForEach_strategy)
@settings(max_examples=50)
def test_r1::foreach_instantiation(instance):
    assert isinstance(instance, r1::ForEach)

@given(instance=r1::ForEach_strategy)
def test_r1::foreach_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=r1::ForEach_strategy)
def test_r1::foreach_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1::Code_strategy)
@settings(max_examples=50)
def test_r1::code_instantiation(instance):
    assert isinstance(instance, r1::Code)

@given(instance=r1::Code_strategy)
def test_r1::code_display_type(instance):
    assert isinstance(instance.display, str)


@given(instance=r1::Code_strategy)
def test_r1::code_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original

@given(instance=r1::Code_strategy)
def test_r1::code_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=r1::Code_strategy)
def test_r1::code_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=r1::DateTime_strategy)
@settings(max_examples=50)
def test_r1::datetime_instantiation(instance):
    assert isinstance(instance, r1::DateTime)

@given(instance=r1::Quantity_strategy)
@settings(max_examples=50)
def test_r1::quantity_instantiation(instance):
    assert isinstance(instance, r1::Quantity)

@given(instance=r1::Quantity_strategy)
def test_r1::quantity_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r1::Quantity_strategy)
def test_r1::quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r1::Quantity_strategy)
def test_r1::quantity_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=r1::Quantity_strategy)
def test_r1::quantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=r1::AliasRef_strategy)
@settings(max_examples=50)
def test_r1::aliasref_instantiation(instance):
    assert isinstance(instance, r1::AliasRef)

@given(instance=r1::AliasRef_strategy)
def test_r1::aliasref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::AliasRef_strategy)
def test_r1::aliasref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::MinValue_strategy)
@settings(max_examples=50)
def test_r1::minvalue_instantiation(instance):
    assert isinstance(instance, r1::MinValue)

@given(instance=r1::MinValue_strategy)
def test_r1::minvalue_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=r1::MinValue_strategy)
def test_r1::minvalue_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1::CodeSystemRef_strategy)
@settings(max_examples=50)
def test_r1::codesystemref_instantiation(instance):
    assert isinstance(instance, r1::CodeSystemRef)

@given(instance=r1::CodeSystemRef_strategy)
def test_r1::codesystemref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::CodeSystemRef_strategy)
def test_r1::codesystemref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::CodeSystemRef_strategy)
def test_r1::codesystemref_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=r1::CodeSystemRef_strategy)
def test_r1::codesystemref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1::Interval_strategy)
@settings(max_examples=50)
def test_r1::interval_instantiation(instance):
    assert isinstance(instance, r1::Interval)

@given(instance=r1::Interval_strategy)
def test_r1::interval_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r1::Interval_strategy)
def test_r1::interval_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r1::Interval_strategy)
def test_r1::interval_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r1::Interval_strategy)
def test_r1::interval_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r1::Null_strategy)
@settings(max_examples=50)
def test_r1::null_instantiation(instance):
    assert isinstance(instance, r1::Null)

@given(instance=r1::Null_strategy)
def test_r1::null_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=r1::Null_strategy)
def test_r1::null_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1::First_strategy)
@settings(max_examples=50)
def test_r1::first_instantiation(instance):
    assert isinstance(instance, r1::First)

@given(instance=r1::First_strategy)
def test_r1::first_orderBy_type(instance):
    assert isinstance(instance.orderBy, str)


@given(instance=r1::First_strategy)
def test_r1::first_orderBy_setter(instance):
    original = instance.orderBy
    instance.orderBy = original
    assert instance.orderBy == original

@given(instance=r1::Case_strategy)
@settings(max_examples=50)
def test_r1::case_instantiation(instance):
    assert isinstance(instance, r1::Case)

@given(instance=r1::InValueSet_strategy)
@settings(max_examples=50)
def test_r1::invalueset_instantiation(instance):
    assert isinstance(instance, r1::InValueSet)

@given(instance=r1::Today_strategy)
@settings(max_examples=50)
def test_r1::today_instantiation(instance):
    assert isinstance(instance, r1::Today)

@given(instance=r1::Substring_strategy)
@settings(max_examples=50)
def test_r1::substring_instantiation(instance):
    assert isinstance(instance, r1::Substring)

@given(instance=r1::Current_strategy)
@settings(max_examples=50)
def test_r1::current_instantiation(instance):
    assert isinstance(instance, r1::Current)

@given(instance=r1::Current_strategy)
def test_r1::current_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=r1::Current_strategy)
def test_r1::current_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1::QueryDefineRef_strategy)
@settings(max_examples=50)
def test_r1::querydefineref_instantiation(instance):
    assert isinstance(instance, r1::QueryDefineRef)

@given(instance=r1::QueryDefineRef_strategy)
def test_r1::querydefineref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::QueryDefineRef_strategy)
def test_r1::querydefineref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::Query_strategy)
@settings(max_examples=50)
def test_r1::query_instantiation(instance):
    assert isinstance(instance, r1::Query)

@given(instance=r1::List_strategy)
@settings(max_examples=50)
def test_r1::list_instantiation(instance):
    assert isinstance(instance, r1::List)

@given(instance=r1::TimeOfDay_strategy)
@settings(max_examples=50)
def test_r1::timeofday_instantiation(instance):
    assert isinstance(instance, r1::TimeOfDay)

@given(instance=r1::Combine_strategy)
@settings(max_examples=50)
def test_r1::combine_instantiation(instance):
    assert isinstance(instance, r1::Combine)

@given(instance=r1::Tuple_strategy)
@settings(max_examples=50)
def test_r1::tuple_instantiation(instance):
    assert isinstance(instance, r1::Tuple)

@given(instance=r1::ValueSetRef_strategy)
@settings(max_examples=50)
def test_r1::valuesetref_instantiation(instance):
    assert isinstance(instance, r1::ValueSetRef)

@given(instance=r1::ValueSetRef_strategy)
def test_r1::valuesetref_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=r1::ValueSetRef_strategy)
def test_r1::valuesetref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1::ValueSetRef_strategy)
def test_r1::valuesetref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ValueSetRef_strategy)
def test_r1::valuesetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::Time_strategy)
@settings(max_examples=50)
def test_r1::time_instantiation(instance):
    assert isinstance(instance, r1::Time)

@given(instance=r1::OperandRef_strategy)
@settings(max_examples=50)
def test_r1::operandref_instantiation(instance):
    assert isinstance(instance, r1::OperandRef)

@given(instance=r1::OperandRef_strategy)
def test_r1::operandref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::OperandRef_strategy)
def test_r1::operandref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::Concept_strategy)
@settings(max_examples=50)
def test_r1::concept_instantiation(instance):
    assert isinstance(instance, r1::Concept)

@given(instance=r1::Concept_strategy)
def test_r1::concept_display_type(instance):
    assert isinstance(instance.display, str)


@given(instance=r1::Concept_strategy)
def test_r1::concept_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original

@given(instance=r1::BinaryExpression_strategy)
@settings(max_examples=50)
def test_r1::binaryexpression_instantiation(instance):
    assert isinstance(instance, r1::BinaryExpression)

@given(instance=r1::IndexOf_strategy)
@settings(max_examples=50)
def test_r1::indexof_instantiation(instance):
    assert isinstance(instance, r1::IndexOf)

@given(instance=r1::NaryExpression_strategy)
@settings(max_examples=50)
def test_r1::naryexpression_instantiation(instance):
    assert isinstance(instance, r1::NaryExpression)

@given(instance=r1::Filter_strategy)
@settings(max_examples=50)
def test_r1::filter_instantiation(instance):
    assert isinstance(instance, r1::Filter)

@given(instance=r1::Filter_strategy)
def test_r1::filter_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=r1::Filter_strategy)
def test_r1::filter_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1::Retrieve_strategy)
@settings(max_examples=50)
def test_r1::retrieve_instantiation(instance):
    assert isinstance(instance, r1::Retrieve)

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateHighProperty_type(instance):
    assert isinstance(instance.dateHighProperty, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateHighProperty_setter(instance):
    original = instance.dateHighProperty
    instance.dateHighProperty = original
    assert instance.dateHighProperty == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_templateId_type(instance):
    assert isinstance(instance.templateId, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_templateId_setter(instance):
    original = instance.templateId
    instance.templateId = original
    assert instance.templateId == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateLowProperty_type(instance):
    assert isinstance(instance.dateLowProperty, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateLowProperty_setter(instance):
    original = instance.dateLowProperty
    instance.dateLowProperty = original
    assert instance.dateLowProperty == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateProperty_type(instance):
    assert isinstance(instance.dateProperty, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_dateProperty_setter(instance):
    original = instance.dateProperty
    instance.dateProperty = original
    assert instance.dateProperty == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_idProperty_type(instance):
    assert isinstance(instance.idProperty, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_idProperty_setter(instance):
    original = instance.idProperty
    instance.idProperty = original
    assert instance.idProperty == original

@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_codeProperty_type(instance):
    assert isinstance(instance.codeProperty, str)


@given(instance=r1::Retrieve_strategy)
def test_r1::retrieve_codeProperty_setter(instance):
    original = instance.codeProperty
    instance.codeProperty = original
    assert instance.codeProperty == original

@given(instance=r1::Last_strategy)
@settings(max_examples=50)
def test_r1::last_instantiation(instance):
    assert isinstance(instance, r1::Last)

@given(instance=r1::Last_strategy)
def test_r1::last_orderBy_type(instance):
    assert isinstance(instance.orderBy, str)


@given(instance=r1::Last_strategy)
def test_r1::last_orderBy_setter(instance):
    original = instance.orderBy
    instance.orderBy = original
    assert instance.orderBy == original

@given(instance=r1::Property_strategy)
@settings(max_examples=50)
def test_r1::property_instantiation(instance):
    assert isinstance(instance, r1::Property)

@given(instance=r1::Property_strategy)
def test_r1::property_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=r1::Property_strategy)
def test_r1::property_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1::Property_strategy)
def test_r1::property_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=r1::Property_strategy)
def test_r1::property_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=r1::UnaryExpression_strategy)
@settings(max_examples=50)
def test_r1::unaryexpression_instantiation(instance):
    assert isinstance(instance, r1::UnaryExpression)

@given(instance=r1::MaxValue_strategy)
@settings(max_examples=50)
def test_r1::maxvalue_instantiation(instance):
    assert isinstance(instance, r1::MaxValue)

@given(instance=r1::MaxValue_strategy)
def test_r1::maxvalue_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=r1::MaxValue_strategy)
def test_r1::maxvalue_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1::Sort_strategy)
@settings(max_examples=50)
def test_r1::sort_instantiation(instance):
    assert isinstance(instance, r1::Sort)

@given(instance=r1::Split_strategy)
@settings(max_examples=50)
def test_r1::split_instantiation(instance):
    assert isinstance(instance, r1::Split)

@given(instance=r1::Now_strategy)
@settings(max_examples=50)
def test_r1::now_instantiation(instance):
    assert isinstance(instance, r1::Now)

@given(instance=r1::InCodeSystem_strategy)
@settings(max_examples=50)
def test_r1::incodesystem_instantiation(instance):
    assert isinstance(instance, r1::InCodeSystem)

@given(instance=r1::Round_strategy)
@settings(max_examples=50)
def test_r1::round_instantiation(instance):
    assert isinstance(instance, r1::Round)

@given(instance=r1::If_strategy)
@settings(max_examples=50)
def test_r1::if_instantiation(instance):
    assert isinstance(instance, r1::If)

@given(instance=r1::ParameterRef_strategy)
@settings(max_examples=50)
def test_r1::parameterref_instantiation(instance):
    assert isinstance(instance, r1::ParameterRef)

@given(instance=r1::ParameterRef_strategy)
def test_r1::parameterref_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=r1::ParameterRef_strategy)
def test_r1::parameterref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1::ParameterRef_strategy)
def test_r1::parameterref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ParameterRef_strategy)
def test_r1::parameterref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::IdentifierRef_strategy)
@settings(max_examples=50)
def test_r1::identifierref_instantiation(instance):
    assert isinstance(instance, r1::IdentifierRef)

@given(instance=r1::IdentifierRef_strategy)
def test_r1::identifierref_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=r1::IdentifierRef_strategy)
def test_r1::identifierref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1::IdentifierRef_strategy)
def test_r1::identifierref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::IdentifierRef_strategy)
def test_r1::identifierref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::Literal_strategy)
@settings(max_examples=50)
def test_r1::literal_instantiation(instance):
    assert isinstance(instance, r1::Literal)

@given(instance=r1::Literal_strategy)
def test_r1::literal_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=r1::Literal_strategy)
def test_r1::literal_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1::Literal_strategy)
def test_r1::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r1::Literal_strategy)
def test_r1::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r1::TernaryExpression_strategy)
@settings(max_examples=50)
def test_r1::ternaryexpression_instantiation(instance):
    assert isinstance(instance, r1::TernaryExpression)

@given(instance=r1::ExpressionRef_strategy)
@settings(max_examples=50)
def test_r1::expressionref_instantiation(instance):
    assert isinstance(instance, r1::ExpressionRef)

@given(instance=r1::ExpressionRef_strategy)
def test_r1::expressionref_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=r1::ExpressionRef_strategy)
def test_r1::expressionref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1::ExpressionRef_strategy)
def test_r1::expressionref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=r1::ExpressionRef_strategy)
def test_r1::expressionref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1::Instance_strategy)
@settings(max_examples=50)
def test_r1::instance_instantiation(instance):
    assert isinstance(instance, r1::Instance)

@given(instance=r1::Instance_strategy)
def test_r1::instance_classType_type(instance):
    assert isinstance(instance.classType, str)


@given(instance=r1::Instance_strategy)
def test_r1::instance_classType_setter(instance):
    original = instance.classType
    instance.classType = original
    assert instance.classType == original

@given(instance=r1::AggregateExpression_strategy)
@settings(max_examples=50)
def test_r1::aggregateexpression_instantiation(instance):
    assert isinstance(instance, r1::AggregateExpression)

@given(instance=r1::AggregateExpression_strategy)
def test_r1::aggregateexpression_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=r1::AggregateExpression_strategy)
def test_r1::aggregateexpression_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=r1::ProperContains_strategy)
@settings(max_examples=50)
def test_r1::propercontains_instantiation(instance):
    assert isinstance(instance, r1::ProperContains)

@given(instance=r1::ProperContains_strategy)
def test_r1::propercontains_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::ProperContains_strategy)
def test_r1::propercontains_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::NotEqual_strategy)
@settings(max_examples=50)
def test_r1::notequal_instantiation(instance):
    assert isinstance(instance, r1::NotEqual)

@given(instance=r1::Times_strategy)
@settings(max_examples=50)
def test_r1::times_instantiation(instance):
    assert isinstance(instance, r1::Times)

@given(instance=r1::MeetsAfter_strategy)
@settings(max_examples=50)
def test_r1::meetsafter_instantiation(instance):
    assert isinstance(instance, r1::MeetsAfter)

@given(instance=r1::MeetsAfter_strategy)
def test_r1::meetsafter_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::MeetsAfter_strategy)
def test_r1::meetsafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Before_strategy)
@settings(max_examples=50)
def test_r1::before_instantiation(instance):
    assert isinstance(instance, r1::Before)

@given(instance=r1::Before_strategy)
def test_r1::before_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Before_strategy)
def test_r1::before_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Overlaps_strategy)
@settings(max_examples=50)
def test_r1::overlaps_instantiation(instance):
    assert isinstance(instance, r1::Overlaps)

@given(instance=r1::Overlaps_strategy)
def test_r1::overlaps_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Overlaps_strategy)
def test_r1::overlaps_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Starts_strategy)
@settings(max_examples=50)
def test_r1::starts_instantiation(instance):
    assert isinstance(instance, r1::Starts)

@given(instance=r1::Starts_strategy)
def test_r1::starts_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Starts_strategy)
def test_r1::starts_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::ProperIncludes_strategy)
@settings(max_examples=50)
def test_r1::properincludes_instantiation(instance):
    assert isinstance(instance, r1::ProperIncludes)

@given(instance=r1::ProperIncludes_strategy)
def test_r1::properincludes_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::ProperIncludes_strategy)
def test_r1::properincludes_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::OverlapsAfter_strategy)
@settings(max_examples=50)
def test_r1::overlapsafter_instantiation(instance):
    assert isinstance(instance, r1::OverlapsAfter)

@given(instance=r1::OverlapsAfter_strategy)
def test_r1::overlapsafter_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::OverlapsAfter_strategy)
def test_r1::overlapsafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::After_strategy)
@settings(max_examples=50)
def test_r1::after_instantiation(instance):
    assert isinstance(instance, r1::After)

@given(instance=r1::After_strategy)
def test_r1::after_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::After_strategy)
def test_r1::after_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Multiply_strategy)
@settings(max_examples=50)
def test_r1::multiply_instantiation(instance):
    assert isinstance(instance, r1::Multiply)

@given(instance=r1::Equal_strategy)
@settings(max_examples=50)
def test_r1::equal_instantiation(instance):
    assert isinstance(instance, r1::Equal)

@given(instance=r1::Includes_strategy)
@settings(max_examples=50)
def test_r1::includes_instantiation(instance):
    assert isinstance(instance, r1::Includes)

@given(instance=r1::Includes_strategy)
def test_r1::includes_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Includes_strategy)
def test_r1::includes_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::ProperIncludedIn_strategy)
@settings(max_examples=50)
def test_r1::properincludedin_instantiation(instance):
    assert isinstance(instance, r1::ProperIncludedIn)

@given(instance=r1::ProperIncludedIn_strategy)
def test_r1::properincludedin_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::ProperIncludedIn_strategy)
def test_r1::properincludedin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Indexer_strategy)
@settings(max_examples=50)
def test_r1::indexer_instantiation(instance):
    assert isinstance(instance, r1::Indexer)

@given(instance=r1::IncludedIn_strategy)
@settings(max_examples=50)
def test_r1::includedin_instantiation(instance):
    assert isinstance(instance, r1::IncludedIn)

@given(instance=r1::IncludedIn_strategy)
def test_r1::includedin_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::IncludedIn_strategy)
def test_r1::includedin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Subtract_strategy)
@settings(max_examples=50)
def test_r1::subtract_instantiation(instance):
    assert isinstance(instance, r1::Subtract)

@given(instance=r1::Intersect_strategy)
@settings(max_examples=50)
def test_r1::intersect_instantiation(instance):
    assert isinstance(instance, r1::Intersect)

@given(instance=r1::SameAs_strategy)
@settings(max_examples=50)
def test_r1::sameas_instantiation(instance):
    assert isinstance(instance, r1::SameAs)

@given(instance=r1::SameAs_strategy)
def test_r1::sameas_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::SameAs_strategy)
def test_r1::sameas_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Modulo_strategy)
@settings(max_examples=50)
def test_r1::modulo_instantiation(instance):
    assert isinstance(instance, r1::Modulo)

@given(instance=r1::LessOrEqual_strategy)
@settings(max_examples=50)
def test_r1::lessorequal_instantiation(instance):
    assert isinstance(instance, r1::LessOrEqual)

@given(instance=r1::Xor_strategy)
@settings(max_examples=50)
def test_r1::xor_instantiation(instance):
    assert isinstance(instance, r1::Xor)

@given(instance=r1::SameOrBefore_strategy)
@settings(max_examples=50)
def test_r1::sameorbefore_instantiation(instance):
    assert isinstance(instance, r1::SameOrBefore)

@given(instance=r1::SameOrBefore_strategy)
def test_r1::sameorbefore_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::SameOrBefore_strategy)
def test_r1::sameorbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::In_strategy)
@settings(max_examples=50)
def test_r1::in_instantiation(instance):
    assert isinstance(instance, r1::In)

@given(instance=r1::In_strategy)
def test_r1::in_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::In_strategy)
def test_r1::in_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Matches_strategy)
@settings(max_examples=50)
def test_r1::matches_instantiation(instance):
    assert isinstance(instance, r1::Matches)

@given(instance=r1::MeetsBefore_strategy)
@settings(max_examples=50)
def test_r1::meetsbefore_instantiation(instance):
    assert isinstance(instance, r1::MeetsBefore)

@given(instance=r1::MeetsBefore_strategy)
def test_r1::meetsbefore_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::MeetsBefore_strategy)
def test_r1::meetsbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_r1::greaterorequal_instantiation(instance):
    assert isinstance(instance, r1::GreaterOrEqual)

@given(instance=r1::CalculateAgeAt_strategy)
@settings(max_examples=50)
def test_r1::calculateageat_instantiation(instance):
    assert isinstance(instance, r1::CalculateAgeAt)

@given(instance=r1::CalculateAgeAt_strategy)
def test_r1::calculateageat_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::CalculateAgeAt_strategy)
def test_r1::calculateageat_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::OverlapsBefore_strategy)
@settings(max_examples=50)
def test_r1::overlapsbefore_instantiation(instance):
    assert isinstance(instance, r1::OverlapsBefore)

@given(instance=r1::OverlapsBefore_strategy)
def test_r1::overlapsbefore_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::OverlapsBefore_strategy)
def test_r1::overlapsbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Less_strategy)
@settings(max_examples=50)
def test_r1::less_instantiation(instance):
    assert isinstance(instance, r1::Less)

@given(instance=r1::SameOrAfter_strategy)
@settings(max_examples=50)
def test_r1::sameorafter_instantiation(instance):
    assert isinstance(instance, r1::SameOrAfter)

@given(instance=r1::SameOrAfter_strategy)
def test_r1::sameorafter_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::SameOrAfter_strategy)
def test_r1::sameorafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Greater_strategy)
@settings(max_examples=50)
def test_r1::greater_instantiation(instance):
    assert isinstance(instance, r1::Greater)

@given(instance=r1::Ends_strategy)
@settings(max_examples=50)
def test_r1::ends_instantiation(instance):
    assert isinstance(instance, r1::Ends)

@given(instance=r1::Ends_strategy)
def test_r1::ends_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Ends_strategy)
def test_r1::ends_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Meets_strategy)
@settings(max_examples=50)
def test_r1::meets_instantiation(instance):
    assert isinstance(instance, r1::Meets)

@given(instance=r1::Meets_strategy)
def test_r1::meets_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Meets_strategy)
def test_r1::meets_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::TruncatedDivide_strategy)
@settings(max_examples=50)
def test_r1::truncateddivide_instantiation(instance):
    assert isinstance(instance, r1::TruncatedDivide)

@given(instance=r1::Power_strategy)
@settings(max_examples=50)
def test_r1::power_instantiation(instance):
    assert isinstance(instance, r1::Power)

@given(instance=r1::Log_strategy)
@settings(max_examples=50)
def test_r1::log_instantiation(instance):
    assert isinstance(instance, r1::Log)

@given(instance=r1::Except_strategy)
@settings(max_examples=50)
def test_r1::except_instantiation(instance):
    assert isinstance(instance, r1::Except)

@given(instance=r1::Divide_strategy)
@settings(max_examples=50)
def test_r1::divide_instantiation(instance):
    assert isinstance(instance, r1::Divide)

@given(instance=r1::DifferenceBetween_strategy)
@settings(max_examples=50)
def test_r1::differencebetween_instantiation(instance):
    assert isinstance(instance, r1::DifferenceBetween)

@given(instance=r1::DifferenceBetween_strategy)
def test_r1::differencebetween_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::DifferenceBetween_strategy)
def test_r1::differencebetween_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::And_strategy)
@settings(max_examples=50)
def test_r1::and_instantiation(instance):
    assert isinstance(instance, r1::And)

@given(instance=r1::DurationBetween_strategy)
@settings(max_examples=50)
def test_r1::durationbetween_instantiation(instance):
    assert isinstance(instance, r1::DurationBetween)

@given(instance=r1::DurationBetween_strategy)
def test_r1::durationbetween_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::DurationBetween_strategy)
def test_r1::durationbetween_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Union_strategy)
@settings(max_examples=50)
def test_r1::union_instantiation(instance):
    assert isinstance(instance, r1::Union)

@given(instance=r1::Contains_strategy)
@settings(max_examples=50)
def test_r1::contains_instantiation(instance):
    assert isinstance(instance, r1::Contains)

@given(instance=r1::Contains_strategy)
def test_r1::contains_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::Contains_strategy)
def test_r1::contains_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::ProperIn_strategy)
@settings(max_examples=50)
def test_r1::properin_instantiation(instance):
    assert isinstance(instance, r1::ProperIn)

@given(instance=r1::ProperIn_strategy)
def test_r1::properin_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::ProperIn_strategy)
def test_r1::properin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Or_strategy)
@settings(max_examples=50)
def test_r1::or_instantiation(instance):
    assert isinstance(instance, r1::Or)

@given(instance=r1::Add_strategy)
@settings(max_examples=50)
def test_r1::add_instantiation(instance):
    assert isinstance(instance, r1::Add)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=r1::DateFrom_strategy)
@settings(max_examples=50)
def test_r1::datefrom_instantiation(instance):
    assert isinstance(instance, r1::DateFrom)

@given(instance=r1::Ln_strategy)
@settings(max_examples=50)
def test_r1::ln_instantiation(instance):
    assert isinstance(instance, r1::Ln)

@given(instance=r1::IsTrue_strategy)
@settings(max_examples=50)
def test_r1::istrue_instantiation(instance):
    assert isinstance(instance, r1::IsTrue)

@given(instance=r1::Exists_strategy)
@settings(max_examples=50)
def test_r1::exists_instantiation(instance):
    assert isinstance(instance, r1::Exists)

@given(instance=r1::IsFalse_strategy)
@settings(max_examples=50)
def test_r1::isfalse_instantiation(instance):
    assert isinstance(instance, r1::IsFalse)

@given(instance=r1::Length_strategy)
@settings(max_examples=50)
def test_r1::length_instantiation(instance):
    assert isinstance(instance, r1::Length)

@given(instance=r1::Floor_strategy)
@settings(max_examples=50)
def test_r1::floor_instantiation(instance):
    assert isinstance(instance, r1::Floor)

@given(instance=r1::TimezoneFrom_strategy)
@settings(max_examples=50)
def test_r1::timezonefrom_instantiation(instance):
    assert isinstance(instance, r1::TimezoneFrom)

@given(instance=r1::Lower_strategy)
@settings(max_examples=50)
def test_r1::lower_instantiation(instance):
    assert isinstance(instance, r1::Lower)

@given(instance=r1::End_strategy)
@settings(max_examples=50)
def test_r1::end_instantiation(instance):
    assert isinstance(instance, r1::End)

@given(instance=r1::Truncate_strategy)
@settings(max_examples=50)
def test_r1::truncate_instantiation(instance):
    assert isinstance(instance, r1::Truncate)

@given(instance=r1::Expand_strategy)
@settings(max_examples=50)
def test_r1::expand_instantiation(instance):
    assert isinstance(instance, r1::Expand)

@given(instance=r1::Successor_strategy)
@settings(max_examples=50)
def test_r1::successor_instantiation(instance):
    assert isinstance(instance, r1::Successor)

@given(instance=r1::Distinct_strategy)
@settings(max_examples=50)
def test_r1::distinct_instantiation(instance):
    assert isinstance(instance, r1::Distinct)

@given(instance=r1::Negate_strategy)
@settings(max_examples=50)
def test_r1::negate_instantiation(instance):
    assert isinstance(instance, r1::Negate)

@given(instance=r1::As_strategy)
@settings(max_examples=50)
def test_r1::as_instantiation(instance):
    assert isinstance(instance, r1::As)

@given(instance=r1::As_strategy)
def test_r1::as_strict_type(instance):
    assert isinstance(instance.strict, str)


@given(instance=r1::As_strategy)
def test_r1::as_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=r1::As_strategy)
def test_r1::as_asType_type(instance):
    assert isinstance(instance.asType, str)


@given(instance=r1::As_strategy)
def test_r1::as_asType_setter(instance):
    original = instance.asType
    instance.asType = original
    assert instance.asType == original

@given(instance=r1::Convert_strategy)
@settings(max_examples=50)
def test_r1::convert_instantiation(instance):
    assert isinstance(instance, r1::Convert)

@given(instance=r1::Convert_strategy)
def test_r1::convert_toType_type(instance):
    assert isinstance(instance.toType, str)


@given(instance=r1::Convert_strategy)
def test_r1::convert_toType_setter(instance):
    original = instance.toType
    instance.toType = original
    assert instance.toType == original

@given(instance=r1::Not_strategy)
@settings(max_examples=50)
def test_r1::not_instantiation(instance):
    assert isinstance(instance, r1::Not)

@given(instance=r1::DateTimeComponentFrom_strategy)
@settings(max_examples=50)
def test_r1::datetimecomponentfrom_instantiation(instance):
    assert isinstance(instance, r1::DateTimeComponentFrom)

@given(instance=r1::DateTimeComponentFrom_strategy)
def test_r1::datetimecomponentfrom_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::DateTimeComponentFrom_strategy)
def test_r1::datetimecomponentfrom_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Width_strategy)
@settings(max_examples=50)
def test_r1::width_instantiation(instance):
    assert isinstance(instance, r1::Width)

@given(instance=r1::Is_strategy)
@settings(max_examples=50)
def test_r1::is_instantiation(instance):
    assert isinstance(instance, r1::Is)

@given(instance=r1::Is_strategy)
def test_r1::is_isType_type(instance):
    assert isinstance(instance.isType, str)


@given(instance=r1::Is_strategy)
def test_r1::is_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original

@given(instance=r1::CalculateAge_strategy)
@settings(max_examples=50)
def test_r1::calculateage_instantiation(instance):
    assert isinstance(instance, r1::CalculateAge)

@given(instance=r1::CalculateAge_strategy)
def test_r1::calculateage_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=r1::CalculateAge_strategy)
def test_r1::calculateage_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1::Ceiling_strategy)
@settings(max_examples=50)
def test_r1::ceiling_instantiation(instance):
    assert isinstance(instance, r1::Ceiling)

@given(instance=r1::SingletonFrom_strategy)
@settings(max_examples=50)
def test_r1::singletonfrom_instantiation(instance):
    assert isinstance(instance, r1::SingletonFrom)

@given(instance=r1::TimeFrom_strategy)
@settings(max_examples=50)
def test_r1::timefrom_instantiation(instance):
    assert isinstance(instance, r1::TimeFrom)

@given(instance=r1::Collapse_strategy)
@settings(max_examples=50)
def test_r1::collapse_instantiation(instance):
    assert isinstance(instance, r1::Collapse)

@given(instance=r1::Predecessor_strategy)
@settings(max_examples=50)
def test_r1::predecessor_instantiation(instance):
    assert isinstance(instance, r1::Predecessor)

@given(instance=r1::Upper_strategy)
@settings(max_examples=50)
def test_r1::upper_instantiation(instance):
    assert isinstance(instance, r1::Upper)

@given(instance=r1::Start_strategy)
@settings(max_examples=50)
def test_r1::start_instantiation(instance):
    assert isinstance(instance, r1::Start)

@given(instance=r1::IsNull_strategy)
@settings(max_examples=50)
def test_r1::isnull_instantiation(instance):
    assert isinstance(instance, r1::IsNull)

@given(instance=r1::Abs_strategy)
@settings(max_examples=50)
def test_r1::abs_instantiation(instance):
    assert isinstance(instance, r1::Abs)
