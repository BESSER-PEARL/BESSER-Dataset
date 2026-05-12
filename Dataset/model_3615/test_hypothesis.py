import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    r1_InstanceElement,
    ExpressionDef,
    r1_FunctionDef,
    ExpressionRef,
    r1_FunctionRef,
    r1_EObject,
    r1_Element,
    NaryExpression,
    r1_Concatenate,
    r1_Coalesce,
    AggregateExpression,
    r1_Count,
    r1_AnyTrue,
    r1_Avg,
    r1_AllTrue,
    SortByItem,
    r1_ByDirection,
    r1_ByExpression,
    r1_ByColumn,
    Element,
    r1_DefineClause,
    r1_CodeSystemDef,
    r1_OperandDef,
    r1_ExpressionDef,
    r1_CaseItem,
    r1_TypeSpecifier,
    r1_AliasedQuerySource,
    r1_Expression,
    Expression,
    r1_If,
    r1_Current,
    r1_InCodeSystem,
    r1_Concept,
    r1_Case,
    r1_AliasRef,
    r1_Instance,
    r1_IdentifierRef,
    r1_Interval,
    r1_ForEach,
    r1_Filter,
    r1_First,
    r1_Code,
    r1_ExpressionRef,
    r1_DateTime,
    r1_CodeSystemRef,
    r1_BinaryExpression,
    r1_Combine,
    r1_IndexOf,
    r1_AggregateExpression,
    BinaryExpression,
    r1_Divide,
    r1_After,
    r1_Indexer,
    r1_GreaterOrEqual,
    r1_Contains,
    r1_Before,
    r1_And,
    r1_DifferenceBetween,
    r1_Except,
    r1_DurationBetween,
    r1_Includes,
    r1_IncludedIn,
    r1_CalculateAgeAt,
    r1_In,
    r1_Equal,
    r1_Ends,
    r1_Intersect,
    r1_Greater,
    r1_Add,
    UnaryExpression,
    r1_CalculateAge,
    r1_Floor,
    r1_Convert,
    r1_End,
    r1_DateTimeComponentFrom,
    r1_Distinct,
    r1_Collapse,
    r1_As,
    r1_Expand,
    r1_Ceiling,
    r1_Exists,
    r1_DateFrom,
    r1_Abs,
    r1_Xor,
    RelationshipClause,
    r1_Without,
    r1_With,
    r1_Width,
    r1_Variance,
    r1_Upper,
    r1_Union,
    r1_UnaryExpression,
    r1_TupleElementDefinition,
    r1_ValueSetDef,
    r1_TupleElement,
    r1_Tuple,
    r1_TruncatedDivide,
    r1_Truncate,
    r1_Today,
    r1_TimezoneFrom,
    r1_Times,
    r1_TimeOfDay,
    r1_TimeFrom,
    r1_Time,
    r1_TernaryExpression,
    r1_Sum,
    r1_Successor,
    r1_Subtract,
    r1_StdDev,
    r1_Starts,
    r1_Start,
    r1_Split,
    r1_Substring,
    r1_SortByItem,
    r1_Sort,
    r1_SingletonFrom,
    r1_SameOrBefore,
    r1_SameOrAfter,
    r1_SameAs,
    r1_Round,
    r1_Retrieve,
    AliasedQuerySource,
    r1_QueryDefineRef,
    r1_SortClause,
    r1_ReturnClause,
    r1_RelationshipClause,
    r1_Query,
    r1_Quantity,
    r1_Property,
    r1_ProperIncludes,
    r1_ProperIncludedIn,
    r1_ProperContains,
    r1_Predecessor,
    r1_Power,
    r1_PositionOf,
    r1_PopulationVariance,
    r1_PopulationStdDev,
    r1_ProperIn,
    r1_ParameterDef,
    r1_OverlapsBefore,
    r1_OverlapsAfter,
    r1_Overlaps,
    r1_Or,
    r1_ParameterRef,
    r1_Null,
    r1_Now,
    r1_NotEqual,
    r1_Not,
    r1_Negate,
    r1_OperandRef,
    r1_Multiply,
    r1_Modulo,
    r1_Mode,
    r1_MinValue,
    r1_Min,
    r1_MeetsBefore,
    r1_MeetsAfter,
    r1_NaryExpression,
    r1_MaxValue,
    r1_Max,
    r1_Matches,
    r1_Lower,
    r1_Log,
    r1_Ln,
    r1_Literal,
    r1_Meets,
    r1_Median,
    r1_List,
    r1_LessOrEqual,
    r1_Less,
    r1_Length,
    r1_Last,
    r1_IsTrue,
    r1_IsNull,
    r1_Is,
    r1_ValueSetRef,
    r1_InValueSet,
    TypeSpecifier,
    r1_NamedTypeSpecifier,
    r1_TupleTypeSpecifier,
    r1_ListTypeSpecifier,
    r1_IntervalTypeSpecifier,
    r1_IsFalse,
    AccessModifier,
    DateTimePrecision,
    SortDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_r1_instanceelement_is_not_abstract():
    assert not inspect.isabstract(r1_InstanceElement)


def test_r1_instanceelement_constructor_exists():
    assert callable(r1_InstanceElement.__init__)


def test_r1_instanceelement_constructor_args():
    sig = inspect.signature(r1_InstanceElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_instanceelement_has_name():
    assert hasattr(r1_InstanceElement, "name")
    descriptor = None
    for klass in r1_InstanceElement.__mro__:
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



def test_r1_functiondef_is_not_abstract():
    assert not inspect.isabstract(r1_FunctionDef)


def test_r1_functiondef_constructor_exists():
    assert callable(r1_FunctionDef.__init__)


def test_r1_functiondef_constructor_args():
    sig = inspect.signature(r1_FunctionDef.__init__)
    params = list(sig.parameters.keys())



def test_expressionref_is_not_abstract():
    assert not inspect.isabstract(ExpressionRef)


def test_expressionref_constructor_exists():
    assert callable(ExpressionRef.__init__)


def test_expressionref_constructor_args():
    sig = inspect.signature(ExpressionRef.__init__)
    params = list(sig.parameters.keys())



def test_r1_functionref_is_not_abstract():
    assert not inspect.isabstract(r1_FunctionRef)


def test_r1_functionref_constructor_exists():
    assert callable(r1_FunctionRef.__init__)


def test_r1_functionref_constructor_args():
    sig = inspect.signature(r1_FunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_r1_eobject_is_not_abstract():
    assert not inspect.isabstract(r1_EObject)


def test_r1_eobject_constructor_exists():
    assert callable(r1_EObject.__init__)


def test_r1_eobject_constructor_args():
    sig = inspect.signature(r1_EObject.__init__)
    params = list(sig.parameters.keys())



def test_r1_element_is_not_abstract():
    assert not inspect.isabstract(r1_Element)


def test_r1_element_constructor_exists():
    assert callable(r1_Element.__init__)


def test_r1_element_constructor_args():
    sig = inspect.signature(r1_Element.__init__)
    params = list(sig.parameters.keys())
    assert "localId" in params, "Missing parameter 'localId'"

def test_r1_element_has_localId():
    assert hasattr(r1_Element, "localId")
    descriptor = None
    for klass in r1_Element.__mro__:
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



def test_r1_concatenate_is_not_abstract():
    assert not inspect.isabstract(r1_Concatenate)


def test_r1_concatenate_constructor_exists():
    assert callable(r1_Concatenate.__init__)


def test_r1_concatenate_constructor_args():
    sig = inspect.signature(r1_Concatenate.__init__)
    params = list(sig.parameters.keys())



def test_r1_coalesce_is_not_abstract():
    assert not inspect.isabstract(r1_Coalesce)


def test_r1_coalesce_constructor_exists():
    assert callable(r1_Coalesce.__init__)


def test_r1_coalesce_constructor_args():
    sig = inspect.signature(r1_Coalesce.__init__)
    params = list(sig.parameters.keys())



def test_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(AggregateExpression)


def test_aggregateexpression_constructor_exists():
    assert callable(AggregateExpression.__init__)


def test_aggregateexpression_constructor_args():
    sig = inspect.signature(AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_count_is_not_abstract():
    assert not inspect.isabstract(r1_Count)


def test_r1_count_constructor_exists():
    assert callable(r1_Count.__init__)


def test_r1_count_constructor_args():
    sig = inspect.signature(r1_Count.__init__)
    params = list(sig.parameters.keys())



def test_r1_anytrue_is_not_abstract():
    assert not inspect.isabstract(r1_AnyTrue)


def test_r1_anytrue_constructor_exists():
    assert callable(r1_AnyTrue.__init__)


def test_r1_anytrue_constructor_args():
    sig = inspect.signature(r1_AnyTrue.__init__)
    params = list(sig.parameters.keys())



def test_r1_avg_is_not_abstract():
    assert not inspect.isabstract(r1_Avg)


def test_r1_avg_constructor_exists():
    assert callable(r1_Avg.__init__)


def test_r1_avg_constructor_args():
    sig = inspect.signature(r1_Avg.__init__)
    params = list(sig.parameters.keys())



def test_r1_alltrue_is_not_abstract():
    assert not inspect.isabstract(r1_AllTrue)


def test_r1_alltrue_constructor_exists():
    assert callable(r1_AllTrue.__init__)


def test_r1_alltrue_constructor_args():
    sig = inspect.signature(r1_AllTrue.__init__)
    params = list(sig.parameters.keys())



def test_sortbyitem_is_not_abstract():
    assert not inspect.isabstract(SortByItem)


def test_sortbyitem_constructor_exists():
    assert callable(SortByItem.__init__)


def test_sortbyitem_constructor_args():
    sig = inspect.signature(SortByItem.__init__)
    params = list(sig.parameters.keys())



def test_r1_bydirection_is_not_abstract():
    assert not inspect.isabstract(r1_ByDirection)


def test_r1_bydirection_constructor_exists():
    assert callable(r1_ByDirection.__init__)


def test_r1_bydirection_constructor_args():
    sig = inspect.signature(r1_ByDirection.__init__)
    params = list(sig.parameters.keys())



def test_r1_byexpression_is_not_abstract():
    assert not inspect.isabstract(r1_ByExpression)


def test_r1_byexpression_constructor_exists():
    assert callable(r1_ByExpression.__init__)


def test_r1_byexpression_constructor_args():
    sig = inspect.signature(r1_ByExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_bycolumn_is_not_abstract():
    assert not inspect.isabstract(r1_ByColumn)


def test_r1_bycolumn_constructor_exists():
    assert callable(r1_ByColumn.__init__)


def test_r1_bycolumn_constructor_args():
    sig = inspect.signature(r1_ByColumn.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_r1_bycolumn_has_path():
    assert hasattr(r1_ByColumn, "path")
    descriptor = None
    for klass in r1_ByColumn.__mro__:
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



def test_r1_defineclause_is_not_abstract():
    assert not inspect.isabstract(r1_DefineClause)


def test_r1_defineclause_constructor_exists():
    assert callable(r1_DefineClause.__init__)


def test_r1_defineclause_constructor_args():
    sig = inspect.signature(r1_DefineClause.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_r1_defineclause_has_identifier():
    assert hasattr(r1_DefineClause, "identifier")
    descriptor = None
    for klass in r1_DefineClause.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_r1_codesystemdef_is_not_abstract():
    assert not inspect.isabstract(r1_CodeSystemDef)


def test_r1_codesystemdef_constructor_exists():
    assert callable(r1_CodeSystemDef.__init__)


def test_r1_codesystemdef_constructor_args():
    sig = inspect.signature(r1_CodeSystemDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_r1_codesystemdef_has_name():
    assert hasattr(r1_CodeSystemDef, "name")
    descriptor = None
    for klass in r1_CodeSystemDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1_codesystemdef_has_accessLevel():
    assert hasattr(r1_CodeSystemDef, "accessLevel")
    descriptor = None
    for klass in r1_CodeSystemDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1_codesystemdef_has_version():
    assert hasattr(r1_CodeSystemDef, "version")
    descriptor = None
    for klass in r1_CodeSystemDef.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_r1_codesystemdef_has_id():
    assert hasattr(r1_CodeSystemDef, "id")
    descriptor = None
    for klass in r1_CodeSystemDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_r1_operanddef_is_not_abstract():
    assert not inspect.isabstract(r1_OperandDef)


def test_r1_operanddef_constructor_exists():
    assert callable(r1_OperandDef.__init__)


def test_r1_operanddef_constructor_args():
    sig = inspect.signature(r1_OperandDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "operandType" in params, "Missing parameter 'operandType'"

def test_r1_operanddef_has_name():
    assert hasattr(r1_OperandDef, "name")
    descriptor = None
    for klass in r1_OperandDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1_operanddef_has_operandType():
    assert hasattr(r1_OperandDef, "operandType")
    descriptor = None
    for klass in r1_OperandDef.__mro__:
        if "operandType" in klass.__dict__:
            descriptor = klass.__dict__["operandType"]
            break
    assert isinstance(descriptor, property)



def test_r1_expressiondef_is_not_abstract():
    assert not inspect.isabstract(r1_ExpressionDef)


def test_r1_expressiondef_constructor_exists():
    assert callable(r1_ExpressionDef.__init__)


def test_r1_expressiondef_constructor_args():
    sig = inspect.signature(r1_ExpressionDef.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_expressiondef_has_context():
    assert hasattr(r1_ExpressionDef, "context")
    descriptor = None
    for klass in r1_ExpressionDef.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_r1_expressiondef_has_accessLevel():
    assert hasattr(r1_ExpressionDef, "accessLevel")
    descriptor = None
    for klass in r1_ExpressionDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1_expressiondef_has_name():
    assert hasattr(r1_ExpressionDef, "name")
    descriptor = None
    for klass in r1_ExpressionDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_caseitem_is_not_abstract():
    assert not inspect.isabstract(r1_CaseItem)


def test_r1_caseitem_constructor_exists():
    assert callable(r1_CaseItem.__init__)


def test_r1_caseitem_constructor_args():
    sig = inspect.signature(r1_CaseItem.__init__)
    params = list(sig.parameters.keys())



def test_r1_typespecifier_is_not_abstract():
    assert not inspect.isabstract(r1_TypeSpecifier)


def test_r1_typespecifier_constructor_exists():
    assert callable(r1_TypeSpecifier.__init__)


def test_r1_typespecifier_constructor_args():
    sig = inspect.signature(r1_TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1_aliasedquerysource_is_not_abstract():
    assert not inspect.isabstract(r1_AliasedQuerySource)


def test_r1_aliasedquerysource_constructor_exists():
    assert callable(r1_AliasedQuerySource.__init__)


def test_r1_aliasedquerysource_constructor_args():
    sig = inspect.signature(r1_AliasedQuerySource.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_r1_aliasedquerysource_has_alias():
    assert hasattr(r1_AliasedQuerySource, "alias")
    descriptor = None
    for klass in r1_AliasedQuerySource.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_r1_expression_is_not_abstract():
    assert not inspect.isabstract(r1_Expression)


def test_r1_expression_constructor_exists():
    assert callable(r1_Expression.__init__)


def test_r1_expression_constructor_args():
    sig = inspect.signature(r1_Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_r1_if_is_not_abstract():
    assert not inspect.isabstract(r1_If)


def test_r1_if_constructor_exists():
    assert callable(r1_If.__init__)


def test_r1_if_constructor_args():
    sig = inspect.signature(r1_If.__init__)
    params = list(sig.parameters.keys())



def test_r1_current_is_not_abstract():
    assert not inspect.isabstract(r1_Current)


def test_r1_current_constructor_exists():
    assert callable(r1_Current.__init__)


def test_r1_current_constructor_args():
    sig = inspect.signature(r1_Current.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1_current_has_scope():
    assert hasattr(r1_Current, "scope")
    descriptor = None
    for klass in r1_Current.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1_incodesystem_is_not_abstract():
    assert not inspect.isabstract(r1_InCodeSystem)


def test_r1_incodesystem_constructor_exists():
    assert callable(r1_InCodeSystem.__init__)


def test_r1_incodesystem_constructor_args():
    sig = inspect.signature(r1_InCodeSystem.__init__)
    params = list(sig.parameters.keys())



def test_r1_concept_is_not_abstract():
    assert not inspect.isabstract(r1_Concept)


def test_r1_concept_constructor_exists():
    assert callable(r1_Concept.__init__)


def test_r1_concept_constructor_args():
    sig = inspect.signature(r1_Concept.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"

def test_r1_concept_has_display():
    assert hasattr(r1_Concept, "display")
    descriptor = None
    for klass in r1_Concept.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)



def test_r1_case_is_not_abstract():
    assert not inspect.isabstract(r1_Case)


def test_r1_case_constructor_exists():
    assert callable(r1_Case.__init__)


def test_r1_case_constructor_args():
    sig = inspect.signature(r1_Case.__init__)
    params = list(sig.parameters.keys())



def test_r1_aliasref_is_not_abstract():
    assert not inspect.isabstract(r1_AliasRef)


def test_r1_aliasref_constructor_exists():
    assert callable(r1_AliasRef.__init__)


def test_r1_aliasref_constructor_args():
    sig = inspect.signature(r1_AliasRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_aliasref_has_name():
    assert hasattr(r1_AliasRef, "name")
    descriptor = None
    for klass in r1_AliasRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_instance_is_not_abstract():
    assert not inspect.isabstract(r1_Instance)


def test_r1_instance_constructor_exists():
    assert callable(r1_Instance.__init__)


def test_r1_instance_constructor_args():
    sig = inspect.signature(r1_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "classType" in params, "Missing parameter 'classType'"

def test_r1_instance_has_classType():
    assert hasattr(r1_Instance, "classType")
    descriptor = None
    for klass in r1_Instance.__mro__:
        if "classType" in klass.__dict__:
            descriptor = klass.__dict__["classType"]
            break
    assert isinstance(descriptor, property)



def test_r1_identifierref_is_not_abstract():
    assert not inspect.isabstract(r1_IdentifierRef)


def test_r1_identifierref_constructor_exists():
    assert callable(r1_IdentifierRef.__init__)


def test_r1_identifierref_constructor_args():
    sig = inspect.signature(r1_IdentifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_identifierref_has_libraryName():
    assert hasattr(r1_IdentifierRef, "libraryName")
    descriptor = None
    for klass in r1_IdentifierRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1_identifierref_has_name():
    assert hasattr(r1_IdentifierRef, "name")
    descriptor = None
    for klass in r1_IdentifierRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_interval_is_not_abstract():
    assert not inspect.isabstract(r1_Interval)


def test_r1_interval_constructor_exists():
    assert callable(r1_Interval.__init__)


def test_r1_interval_constructor_args():
    sig = inspect.signature(r1_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r1_interval_has_lowClosed():
    assert hasattr(r1_Interval, "lowClosed")
    descriptor = None
    for klass in r1_Interval.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r1_interval_has_highClosed():
    assert hasattr(r1_Interval, "highClosed")
    descriptor = None
    for klass in r1_Interval.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r1_foreach_is_not_abstract():
    assert not inspect.isabstract(r1_ForEach)


def test_r1_foreach_constructor_exists():
    assert callable(r1_ForEach.__init__)


def test_r1_foreach_constructor_args():
    sig = inspect.signature(r1_ForEach.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1_foreach_has_scope():
    assert hasattr(r1_ForEach, "scope")
    descriptor = None
    for klass in r1_ForEach.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1_filter_is_not_abstract():
    assert not inspect.isabstract(r1_Filter)


def test_r1_filter_constructor_exists():
    assert callable(r1_Filter.__init__)


def test_r1_filter_constructor_args():
    sig = inspect.signature(r1_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1_filter_has_scope():
    assert hasattr(r1_Filter, "scope")
    descriptor = None
    for klass in r1_Filter.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_r1_first_is_not_abstract():
    assert not inspect.isabstract(r1_First)


def test_r1_first_constructor_exists():
    assert callable(r1_First.__init__)


def test_r1_first_constructor_args():
    sig = inspect.signature(r1_First.__init__)
    params = list(sig.parameters.keys())
    assert "orderBy" in params, "Missing parameter 'orderBy'"

def test_r1_first_has_orderBy():
    assert hasattr(r1_First, "orderBy")
    descriptor = None
    for klass in r1_First.__mro__:
        if "orderBy" in klass.__dict__:
            descriptor = klass.__dict__["orderBy"]
            break
    assert isinstance(descriptor, property)



def test_r1_code_is_not_abstract():
    assert not inspect.isabstract(r1_Code)


def test_r1_code_constructor_exists():
    assert callable(r1_Code.__init__)


def test_r1_code_constructor_args():
    sig = inspect.signature(r1_Code.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"
    assert "code" in params, "Missing parameter 'code'"

def test_r1_code_has_display():
    assert hasattr(r1_Code, "display")
    descriptor = None
    for klass in r1_Code.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)

def test_r1_code_has_code():
    assert hasattr(r1_Code, "code")
    descriptor = None
    for klass in r1_Code.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_r1_expressionref_is_not_abstract():
    assert not inspect.isabstract(r1_ExpressionRef)


def test_r1_expressionref_constructor_exists():
    assert callable(r1_ExpressionRef.__init__)


def test_r1_expressionref_constructor_args():
    sig = inspect.signature(r1_ExpressionRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "libraryName" in params, "Missing parameter 'libraryName'"

def test_r1_expressionref_has_name():
    assert hasattr(r1_ExpressionRef, "name")
    descriptor = None
    for klass in r1_ExpressionRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1_expressionref_has_libraryName():
    assert hasattr(r1_ExpressionRef, "libraryName")
    descriptor = None
    for klass in r1_ExpressionRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)



def test_r1_datetime_is_not_abstract():
    assert not inspect.isabstract(r1_DateTime)


def test_r1_datetime_constructor_exists():
    assert callable(r1_DateTime.__init__)


def test_r1_datetime_constructor_args():
    sig = inspect.signature(r1_DateTime.__init__)
    params = list(sig.parameters.keys())



def test_r1_codesystemref_is_not_abstract():
    assert not inspect.isabstract(r1_CodeSystemRef)


def test_r1_codesystemref_constructor_exists():
    assert callable(r1_CodeSystemRef.__init__)


def test_r1_codesystemref_constructor_args():
    sig = inspect.signature(r1_CodeSystemRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "libraryName" in params, "Missing parameter 'libraryName'"

def test_r1_codesystemref_has_name():
    assert hasattr(r1_CodeSystemRef, "name")
    descriptor = None
    for klass in r1_CodeSystemRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_r1_codesystemref_has_libraryName():
    assert hasattr(r1_CodeSystemRef, "libraryName")
    descriptor = None
    for klass in r1_CodeSystemRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)



def test_r1_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1_BinaryExpression)


def test_r1_binaryexpression_constructor_exists():
    assert callable(r1_BinaryExpression.__init__)


def test_r1_binaryexpression_constructor_args():
    sig = inspect.signature(r1_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_combine_is_not_abstract():
    assert not inspect.isabstract(r1_Combine)


def test_r1_combine_constructor_exists():
    assert callable(r1_Combine.__init__)


def test_r1_combine_constructor_args():
    sig = inspect.signature(r1_Combine.__init__)
    params = list(sig.parameters.keys())



def test_r1_indexof_is_not_abstract():
    assert not inspect.isabstract(r1_IndexOf)


def test_r1_indexof_constructor_exists():
    assert callable(r1_IndexOf.__init__)


def test_r1_indexof_constructor_args():
    sig = inspect.signature(r1_IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_r1_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(r1_AggregateExpression)


def test_r1_aggregateexpression_constructor_exists():
    assert callable(r1_AggregateExpression.__init__)


def test_r1_aggregateexpression_constructor_args():
    sig = inspect.signature(r1_AggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_r1_aggregateexpression_has_path():
    assert hasattr(r1_AggregateExpression, "path")
    descriptor = None
    for klass in r1_AggregateExpression.__mro__:
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



def test_r1_divide_is_not_abstract():
    assert not inspect.isabstract(r1_Divide)


def test_r1_divide_constructor_exists():
    assert callable(r1_Divide.__init__)


def test_r1_divide_constructor_args():
    sig = inspect.signature(r1_Divide.__init__)
    params = list(sig.parameters.keys())



def test_r1_after_is_not_abstract():
    assert not inspect.isabstract(r1_After)


def test_r1_after_constructor_exists():
    assert callable(r1_After.__init__)


def test_r1_after_constructor_args():
    sig = inspect.signature(r1_After.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_after_has_precision():
    assert hasattr(r1_After, "precision")
    descriptor = None
    for klass in r1_After.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_indexer_is_not_abstract():
    assert not inspect.isabstract(r1_Indexer)


def test_r1_indexer_constructor_exists():
    assert callable(r1_Indexer.__init__)


def test_r1_indexer_constructor_args():
    sig = inspect.signature(r1_Indexer.__init__)
    params = list(sig.parameters.keys())



def test_r1_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(r1_GreaterOrEqual)


def test_r1_greaterorequal_constructor_exists():
    assert callable(r1_GreaterOrEqual.__init__)


def test_r1_greaterorequal_constructor_args():
    sig = inspect.signature(r1_GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1_contains_is_not_abstract():
    assert not inspect.isabstract(r1_Contains)


def test_r1_contains_constructor_exists():
    assert callable(r1_Contains.__init__)


def test_r1_contains_constructor_args():
    sig = inspect.signature(r1_Contains.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_contains_has_precision():
    assert hasattr(r1_Contains, "precision")
    descriptor = None
    for klass in r1_Contains.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_before_is_not_abstract():
    assert not inspect.isabstract(r1_Before)


def test_r1_before_constructor_exists():
    assert callable(r1_Before.__init__)


def test_r1_before_constructor_args():
    sig = inspect.signature(r1_Before.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_before_has_precision():
    assert hasattr(r1_Before, "precision")
    descriptor = None
    for klass in r1_Before.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_and_is_not_abstract():
    assert not inspect.isabstract(r1_And)


def test_r1_and_constructor_exists():
    assert callable(r1_And.__init__)


def test_r1_and_constructor_args():
    sig = inspect.signature(r1_And.__init__)
    params = list(sig.parameters.keys())



def test_r1_differencebetween_is_not_abstract():
    assert not inspect.isabstract(r1_DifferenceBetween)


def test_r1_differencebetween_constructor_exists():
    assert callable(r1_DifferenceBetween.__init__)


def test_r1_differencebetween_constructor_args():
    sig = inspect.signature(r1_DifferenceBetween.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_differencebetween_has_precision():
    assert hasattr(r1_DifferenceBetween, "precision")
    descriptor = None
    for klass in r1_DifferenceBetween.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_except_is_not_abstract():
    assert not inspect.isabstract(r1_Except)


def test_r1_except_constructor_exists():
    assert callable(r1_Except.__init__)


def test_r1_except_constructor_args():
    sig = inspect.signature(r1_Except.__init__)
    params = list(sig.parameters.keys())



def test_r1_durationbetween_is_not_abstract():
    assert not inspect.isabstract(r1_DurationBetween)


def test_r1_durationbetween_constructor_exists():
    assert callable(r1_DurationBetween.__init__)


def test_r1_durationbetween_constructor_args():
    sig = inspect.signature(r1_DurationBetween.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_durationbetween_has_precision():
    assert hasattr(r1_DurationBetween, "precision")
    descriptor = None
    for klass in r1_DurationBetween.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_includes_is_not_abstract():
    assert not inspect.isabstract(r1_Includes)


def test_r1_includes_constructor_exists():
    assert callable(r1_Includes.__init__)


def test_r1_includes_constructor_args():
    sig = inspect.signature(r1_Includes.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_includes_has_precision():
    assert hasattr(r1_Includes, "precision")
    descriptor = None
    for klass in r1_Includes.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_includedin_is_not_abstract():
    assert not inspect.isabstract(r1_IncludedIn)


def test_r1_includedin_constructor_exists():
    assert callable(r1_IncludedIn.__init__)


def test_r1_includedin_constructor_args():
    sig = inspect.signature(r1_IncludedIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_includedin_has_precision():
    assert hasattr(r1_IncludedIn, "precision")
    descriptor = None
    for klass in r1_IncludedIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_calculateageat_is_not_abstract():
    assert not inspect.isabstract(r1_CalculateAgeAt)


def test_r1_calculateageat_constructor_exists():
    assert callable(r1_CalculateAgeAt.__init__)


def test_r1_calculateageat_constructor_args():
    sig = inspect.signature(r1_CalculateAgeAt.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_calculateageat_has_precision():
    assert hasattr(r1_CalculateAgeAt, "precision")
    descriptor = None
    for klass in r1_CalculateAgeAt.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_in_is_not_abstract():
    assert not inspect.isabstract(r1_In)


def test_r1_in_constructor_exists():
    assert callable(r1_In.__init__)


def test_r1_in_constructor_args():
    sig = inspect.signature(r1_In.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_in_has_precision():
    assert hasattr(r1_In, "precision")
    descriptor = None
    for klass in r1_In.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_equal_is_not_abstract():
    assert not inspect.isabstract(r1_Equal)


def test_r1_equal_constructor_exists():
    assert callable(r1_Equal.__init__)


def test_r1_equal_constructor_args():
    sig = inspect.signature(r1_Equal.__init__)
    params = list(sig.parameters.keys())



def test_r1_ends_is_not_abstract():
    assert not inspect.isabstract(r1_Ends)


def test_r1_ends_constructor_exists():
    assert callable(r1_Ends.__init__)


def test_r1_ends_constructor_args():
    sig = inspect.signature(r1_Ends.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_ends_has_precision():
    assert hasattr(r1_Ends, "precision")
    descriptor = None
    for klass in r1_Ends.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_intersect_is_not_abstract():
    assert not inspect.isabstract(r1_Intersect)


def test_r1_intersect_constructor_exists():
    assert callable(r1_Intersect.__init__)


def test_r1_intersect_constructor_args():
    sig = inspect.signature(r1_Intersect.__init__)
    params = list(sig.parameters.keys())



def test_r1_greater_is_not_abstract():
    assert not inspect.isabstract(r1_Greater)


def test_r1_greater_constructor_exists():
    assert callable(r1_Greater.__init__)


def test_r1_greater_constructor_args():
    sig = inspect.signature(r1_Greater.__init__)
    params = list(sig.parameters.keys())



def test_r1_add_is_not_abstract():
    assert not inspect.isabstract(r1_Add)


def test_r1_add_constructor_exists():
    assert callable(r1_Add.__init__)


def test_r1_add_constructor_args():
    sig = inspect.signature(r1_Add.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_calculateage_is_not_abstract():
    assert not inspect.isabstract(r1_CalculateAge)


def test_r1_calculateage_constructor_exists():
    assert callable(r1_CalculateAge.__init__)


def test_r1_calculateage_constructor_args():
    sig = inspect.signature(r1_CalculateAge.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_calculateage_has_precision():
    assert hasattr(r1_CalculateAge, "precision")
    descriptor = None
    for klass in r1_CalculateAge.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_floor_is_not_abstract():
    assert not inspect.isabstract(r1_Floor)


def test_r1_floor_constructor_exists():
    assert callable(r1_Floor.__init__)


def test_r1_floor_constructor_args():
    sig = inspect.signature(r1_Floor.__init__)
    params = list(sig.parameters.keys())



def test_r1_convert_is_not_abstract():
    assert not inspect.isabstract(r1_Convert)


def test_r1_convert_constructor_exists():
    assert callable(r1_Convert.__init__)


def test_r1_convert_constructor_args():
    sig = inspect.signature(r1_Convert.__init__)
    params = list(sig.parameters.keys())
    assert "toType" in params, "Missing parameter 'toType'"

def test_r1_convert_has_toType():
    assert hasattr(r1_Convert, "toType")
    descriptor = None
    for klass in r1_Convert.__mro__:
        if "toType" in klass.__dict__:
            descriptor = klass.__dict__["toType"]
            break
    assert isinstance(descriptor, property)



def test_r1_end_is_not_abstract():
    assert not inspect.isabstract(r1_End)


def test_r1_end_constructor_exists():
    assert callable(r1_End.__init__)


def test_r1_end_constructor_args():
    sig = inspect.signature(r1_End.__init__)
    params = list(sig.parameters.keys())



def test_r1_datetimecomponentfrom_is_not_abstract():
    assert not inspect.isabstract(r1_DateTimeComponentFrom)


def test_r1_datetimecomponentfrom_constructor_exists():
    assert callable(r1_DateTimeComponentFrom.__init__)


def test_r1_datetimecomponentfrom_constructor_args():
    sig = inspect.signature(r1_DateTimeComponentFrom.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_datetimecomponentfrom_has_precision():
    assert hasattr(r1_DateTimeComponentFrom, "precision")
    descriptor = None
    for klass in r1_DateTimeComponentFrom.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_distinct_is_not_abstract():
    assert not inspect.isabstract(r1_Distinct)


def test_r1_distinct_constructor_exists():
    assert callable(r1_Distinct.__init__)


def test_r1_distinct_constructor_args():
    sig = inspect.signature(r1_Distinct.__init__)
    params = list(sig.parameters.keys())



def test_r1_collapse_is_not_abstract():
    assert not inspect.isabstract(r1_Collapse)


def test_r1_collapse_constructor_exists():
    assert callable(r1_Collapse.__init__)


def test_r1_collapse_constructor_args():
    sig = inspect.signature(r1_Collapse.__init__)
    params = list(sig.parameters.keys())



def test_r1_as_is_not_abstract():
    assert not inspect.isabstract(r1_As)


def test_r1_as_constructor_exists():
    assert callable(r1_As.__init__)


def test_r1_as_constructor_args():
    sig = inspect.signature(r1_As.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "asType" in params, "Missing parameter 'asType'"

def test_r1_as_has_strict():
    assert hasattr(r1_As, "strict")
    descriptor = None
    for klass in r1_As.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_r1_as_has_asType():
    assert hasattr(r1_As, "asType")
    descriptor = None
    for klass in r1_As.__mro__:
        if "asType" in klass.__dict__:
            descriptor = klass.__dict__["asType"]
            break
    assert isinstance(descriptor, property)



def test_r1_expand_is_not_abstract():
    assert not inspect.isabstract(r1_Expand)


def test_r1_expand_constructor_exists():
    assert callable(r1_Expand.__init__)


def test_r1_expand_constructor_args():
    sig = inspect.signature(r1_Expand.__init__)
    params = list(sig.parameters.keys())



def test_r1_ceiling_is_not_abstract():
    assert not inspect.isabstract(r1_Ceiling)


def test_r1_ceiling_constructor_exists():
    assert callable(r1_Ceiling.__init__)


def test_r1_ceiling_constructor_args():
    sig = inspect.signature(r1_Ceiling.__init__)
    params = list(sig.parameters.keys())



def test_r1_exists_is_not_abstract():
    assert not inspect.isabstract(r1_Exists)


def test_r1_exists_constructor_exists():
    assert callable(r1_Exists.__init__)


def test_r1_exists_constructor_args():
    sig = inspect.signature(r1_Exists.__init__)
    params = list(sig.parameters.keys())



def test_r1_datefrom_is_not_abstract():
    assert not inspect.isabstract(r1_DateFrom)


def test_r1_datefrom_constructor_exists():
    assert callable(r1_DateFrom.__init__)


def test_r1_datefrom_constructor_args():
    sig = inspect.signature(r1_DateFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1_abs_is_not_abstract():
    assert not inspect.isabstract(r1_Abs)


def test_r1_abs_constructor_exists():
    assert callable(r1_Abs.__init__)


def test_r1_abs_constructor_args():
    sig = inspect.signature(r1_Abs.__init__)
    params = list(sig.parameters.keys())



def test_r1_xor_is_not_abstract():
    assert not inspect.isabstract(r1_Xor)


def test_r1_xor_constructor_exists():
    assert callable(r1_Xor.__init__)


def test_r1_xor_constructor_args():
    sig = inspect.signature(r1_Xor.__init__)
    params = list(sig.parameters.keys())



def test_relationshipclause_is_not_abstract():
    assert not inspect.isabstract(RelationshipClause)


def test_relationshipclause_constructor_exists():
    assert callable(RelationshipClause.__init__)


def test_relationshipclause_constructor_args():
    sig = inspect.signature(RelationshipClause.__init__)
    params = list(sig.parameters.keys())



def test_r1_without_is_not_abstract():
    assert not inspect.isabstract(r1_Without)


def test_r1_without_constructor_exists():
    assert callable(r1_Without.__init__)


def test_r1_without_constructor_args():
    sig = inspect.signature(r1_Without.__init__)
    params = list(sig.parameters.keys())



def test_r1_with_is_not_abstract():
    assert not inspect.isabstract(r1_With)


def test_r1_with_constructor_exists():
    assert callable(r1_With.__init__)


def test_r1_with_constructor_args():
    sig = inspect.signature(r1_With.__init__)
    params = list(sig.parameters.keys())



def test_r1_width_is_not_abstract():
    assert not inspect.isabstract(r1_Width)


def test_r1_width_constructor_exists():
    assert callable(r1_Width.__init__)


def test_r1_width_constructor_args():
    sig = inspect.signature(r1_Width.__init__)
    params = list(sig.parameters.keys())



def test_r1_variance_is_not_abstract():
    assert not inspect.isabstract(r1_Variance)


def test_r1_variance_constructor_exists():
    assert callable(r1_Variance.__init__)


def test_r1_variance_constructor_args():
    sig = inspect.signature(r1_Variance.__init__)
    params = list(sig.parameters.keys())



def test_r1_upper_is_not_abstract():
    assert not inspect.isabstract(r1_Upper)


def test_r1_upper_constructor_exists():
    assert callable(r1_Upper.__init__)


def test_r1_upper_constructor_args():
    sig = inspect.signature(r1_Upper.__init__)
    params = list(sig.parameters.keys())



def test_r1_union_is_not_abstract():
    assert not inspect.isabstract(r1_Union)


def test_r1_union_constructor_exists():
    assert callable(r1_Union.__init__)


def test_r1_union_constructor_args():
    sig = inspect.signature(r1_Union.__init__)
    params = list(sig.parameters.keys())



def test_r1_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1_UnaryExpression)


def test_r1_unaryexpression_constructor_exists():
    assert callable(r1_UnaryExpression.__init__)


def test_r1_unaryexpression_constructor_args():
    sig = inspect.signature(r1_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_tupleelementdefinition_is_not_abstract():
    assert not inspect.isabstract(r1_TupleElementDefinition)


def test_r1_tupleelementdefinition_constructor_exists():
    assert callable(r1_TupleElementDefinition.__init__)


def test_r1_tupleelementdefinition_constructor_args():
    sig = inspect.signature(r1_TupleElementDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_tupleelementdefinition_has_name():
    assert hasattr(r1_TupleElementDefinition, "name")
    descriptor = None
    for klass in r1_TupleElementDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_valuesetdef_is_not_abstract():
    assert not inspect.isabstract(r1_ValueSetDef)


def test_r1_valuesetdef_constructor_exists():
    assert callable(r1_ValueSetDef.__init__)


def test_r1_valuesetdef_constructor_args():
    sig = inspect.signature(r1_ValueSetDef.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_valuesetdef_has_accessLevel():
    assert hasattr(r1_ValueSetDef, "accessLevel")
    descriptor = None
    for klass in r1_ValueSetDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1_valuesetdef_has_id():
    assert hasattr(r1_ValueSetDef, "id")
    descriptor = None
    for klass in r1_ValueSetDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_r1_valuesetdef_has_version():
    assert hasattr(r1_ValueSetDef, "version")
    descriptor = None
    for klass in r1_ValueSetDef.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_r1_valuesetdef_has_name():
    assert hasattr(r1_ValueSetDef, "name")
    descriptor = None
    for klass in r1_ValueSetDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_tupleelement_is_not_abstract():
    assert not inspect.isabstract(r1_TupleElement)


def test_r1_tupleelement_constructor_exists():
    assert callable(r1_TupleElement.__init__)


def test_r1_tupleelement_constructor_args():
    sig = inspect.signature(r1_TupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_tupleelement_has_name():
    assert hasattr(r1_TupleElement, "name")
    descriptor = None
    for klass in r1_TupleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_tuple_is_not_abstract():
    assert not inspect.isabstract(r1_Tuple)


def test_r1_tuple_constructor_exists():
    assert callable(r1_Tuple.__init__)


def test_r1_tuple_constructor_args():
    sig = inspect.signature(r1_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_r1_truncateddivide_is_not_abstract():
    assert not inspect.isabstract(r1_TruncatedDivide)


def test_r1_truncateddivide_constructor_exists():
    assert callable(r1_TruncatedDivide.__init__)


def test_r1_truncateddivide_constructor_args():
    sig = inspect.signature(r1_TruncatedDivide.__init__)
    params = list(sig.parameters.keys())



def test_r1_truncate_is_not_abstract():
    assert not inspect.isabstract(r1_Truncate)


def test_r1_truncate_constructor_exists():
    assert callable(r1_Truncate.__init__)


def test_r1_truncate_constructor_args():
    sig = inspect.signature(r1_Truncate.__init__)
    params = list(sig.parameters.keys())



def test_r1_today_is_not_abstract():
    assert not inspect.isabstract(r1_Today)


def test_r1_today_constructor_exists():
    assert callable(r1_Today.__init__)


def test_r1_today_constructor_args():
    sig = inspect.signature(r1_Today.__init__)
    params = list(sig.parameters.keys())



def test_r1_timezonefrom_is_not_abstract():
    assert not inspect.isabstract(r1_TimezoneFrom)


def test_r1_timezonefrom_constructor_exists():
    assert callable(r1_TimezoneFrom.__init__)


def test_r1_timezonefrom_constructor_args():
    sig = inspect.signature(r1_TimezoneFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1_times_is_not_abstract():
    assert not inspect.isabstract(r1_Times)


def test_r1_times_constructor_exists():
    assert callable(r1_Times.__init__)


def test_r1_times_constructor_args():
    sig = inspect.signature(r1_Times.__init__)
    params = list(sig.parameters.keys())



def test_r1_timeofday_is_not_abstract():
    assert not inspect.isabstract(r1_TimeOfDay)


def test_r1_timeofday_constructor_exists():
    assert callable(r1_TimeOfDay.__init__)


def test_r1_timeofday_constructor_args():
    sig = inspect.signature(r1_TimeOfDay.__init__)
    params = list(sig.parameters.keys())



def test_r1_timefrom_is_not_abstract():
    assert not inspect.isabstract(r1_TimeFrom)


def test_r1_timefrom_constructor_exists():
    assert callable(r1_TimeFrom.__init__)


def test_r1_timefrom_constructor_args():
    sig = inspect.signature(r1_TimeFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1_time_is_not_abstract():
    assert not inspect.isabstract(r1_Time)


def test_r1_time_constructor_exists():
    assert callable(r1_Time.__init__)


def test_r1_time_constructor_args():
    sig = inspect.signature(r1_Time.__init__)
    params = list(sig.parameters.keys())



def test_r1_ternaryexpression_is_not_abstract():
    assert not inspect.isabstract(r1_TernaryExpression)


def test_r1_ternaryexpression_constructor_exists():
    assert callable(r1_TernaryExpression.__init__)


def test_r1_ternaryexpression_constructor_args():
    sig = inspect.signature(r1_TernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_sum_is_not_abstract():
    assert not inspect.isabstract(r1_Sum)


def test_r1_sum_constructor_exists():
    assert callable(r1_Sum.__init__)


def test_r1_sum_constructor_args():
    sig = inspect.signature(r1_Sum.__init__)
    params = list(sig.parameters.keys())



def test_r1_successor_is_not_abstract():
    assert not inspect.isabstract(r1_Successor)


def test_r1_successor_constructor_exists():
    assert callable(r1_Successor.__init__)


def test_r1_successor_constructor_args():
    sig = inspect.signature(r1_Successor.__init__)
    params = list(sig.parameters.keys())



def test_r1_subtract_is_not_abstract():
    assert not inspect.isabstract(r1_Subtract)


def test_r1_subtract_constructor_exists():
    assert callable(r1_Subtract.__init__)


def test_r1_subtract_constructor_args():
    sig = inspect.signature(r1_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_r1_stddev_is_not_abstract():
    assert not inspect.isabstract(r1_StdDev)


def test_r1_stddev_constructor_exists():
    assert callable(r1_StdDev.__init__)


def test_r1_stddev_constructor_args():
    sig = inspect.signature(r1_StdDev.__init__)
    params = list(sig.parameters.keys())



def test_r1_starts_is_not_abstract():
    assert not inspect.isabstract(r1_Starts)


def test_r1_starts_constructor_exists():
    assert callable(r1_Starts.__init__)


def test_r1_starts_constructor_args():
    sig = inspect.signature(r1_Starts.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_starts_has_precision():
    assert hasattr(r1_Starts, "precision")
    descriptor = None
    for klass in r1_Starts.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_start_is_not_abstract():
    assert not inspect.isabstract(r1_Start)


def test_r1_start_constructor_exists():
    assert callable(r1_Start.__init__)


def test_r1_start_constructor_args():
    sig = inspect.signature(r1_Start.__init__)
    params = list(sig.parameters.keys())



def test_r1_split_is_not_abstract():
    assert not inspect.isabstract(r1_Split)


def test_r1_split_constructor_exists():
    assert callable(r1_Split.__init__)


def test_r1_split_constructor_args():
    sig = inspect.signature(r1_Split.__init__)
    params = list(sig.parameters.keys())



def test_r1_substring_is_not_abstract():
    assert not inspect.isabstract(r1_Substring)


def test_r1_substring_constructor_exists():
    assert callable(r1_Substring.__init__)


def test_r1_substring_constructor_args():
    sig = inspect.signature(r1_Substring.__init__)
    params = list(sig.parameters.keys())



def test_r1_sortbyitem_is_not_abstract():
    assert not inspect.isabstract(r1_SortByItem)


def test_r1_sortbyitem_constructor_exists():
    assert callable(r1_SortByItem.__init__)


def test_r1_sortbyitem_constructor_args():
    sig = inspect.signature(r1_SortByItem.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_r1_sortbyitem_has_direction():
    assert hasattr(r1_SortByItem, "direction")
    descriptor = None
    for klass in r1_SortByItem.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_r1_sort_is_not_abstract():
    assert not inspect.isabstract(r1_Sort)


def test_r1_sort_constructor_exists():
    assert callable(r1_Sort.__init__)


def test_r1_sort_constructor_args():
    sig = inspect.signature(r1_Sort.__init__)
    params = list(sig.parameters.keys())



def test_r1_singletonfrom_is_not_abstract():
    assert not inspect.isabstract(r1_SingletonFrom)


def test_r1_singletonfrom_constructor_exists():
    assert callable(r1_SingletonFrom.__init__)


def test_r1_singletonfrom_constructor_args():
    sig = inspect.signature(r1_SingletonFrom.__init__)
    params = list(sig.parameters.keys())



def test_r1_sameorbefore_is_not_abstract():
    assert not inspect.isabstract(r1_SameOrBefore)


def test_r1_sameorbefore_constructor_exists():
    assert callable(r1_SameOrBefore.__init__)


def test_r1_sameorbefore_constructor_args():
    sig = inspect.signature(r1_SameOrBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_sameorbefore_has_precision():
    assert hasattr(r1_SameOrBefore, "precision")
    descriptor = None
    for klass in r1_SameOrBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_sameorafter_is_not_abstract():
    assert not inspect.isabstract(r1_SameOrAfter)


def test_r1_sameorafter_constructor_exists():
    assert callable(r1_SameOrAfter.__init__)


def test_r1_sameorafter_constructor_args():
    sig = inspect.signature(r1_SameOrAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_sameorafter_has_precision():
    assert hasattr(r1_SameOrAfter, "precision")
    descriptor = None
    for klass in r1_SameOrAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_sameas_is_not_abstract():
    assert not inspect.isabstract(r1_SameAs)


def test_r1_sameas_constructor_exists():
    assert callable(r1_SameAs.__init__)


def test_r1_sameas_constructor_args():
    sig = inspect.signature(r1_SameAs.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_sameas_has_precision():
    assert hasattr(r1_SameAs, "precision")
    descriptor = None
    for klass in r1_SameAs.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_round_is_not_abstract():
    assert not inspect.isabstract(r1_Round)


def test_r1_round_constructor_exists():
    assert callable(r1_Round.__init__)


def test_r1_round_constructor_args():
    sig = inspect.signature(r1_Round.__init__)
    params = list(sig.parameters.keys())



def test_r1_retrieve_is_not_abstract():
    assert not inspect.isabstract(r1_Retrieve)


def test_r1_retrieve_constructor_exists():
    assert callable(r1_Retrieve.__init__)


def test_r1_retrieve_constructor_args():
    sig = inspect.signature(r1_Retrieve.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "idProperty" in params, "Missing parameter 'idProperty'"
    assert "dateProperty" in params, "Missing parameter 'dateProperty'"
    assert "dateHighProperty" in params, "Missing parameter 'dateHighProperty'"
    assert "codeProperty" in params, "Missing parameter 'codeProperty'"
    assert "dateLowProperty" in params, "Missing parameter 'dateLowProperty'"
    assert "templateId" in params, "Missing parameter 'templateId'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_r1_retrieve_has_dataType():
    assert hasattr(r1_Retrieve, "dataType")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_idProperty():
    assert hasattr(r1_Retrieve, "idProperty")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "idProperty" in klass.__dict__:
            descriptor = klass.__dict__["idProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_dateProperty():
    assert hasattr(r1_Retrieve, "dateProperty")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "dateProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_dateHighProperty():
    assert hasattr(r1_Retrieve, "dateHighProperty")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "dateHighProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateHighProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_codeProperty():
    assert hasattr(r1_Retrieve, "codeProperty")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "codeProperty" in klass.__dict__:
            descriptor = klass.__dict__["codeProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_dateLowProperty():
    assert hasattr(r1_Retrieve, "dateLowProperty")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "dateLowProperty" in klass.__dict__:
            descriptor = klass.__dict__["dateLowProperty"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_templateId():
    assert hasattr(r1_Retrieve, "templateId")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "templateId" in klass.__dict__:
            descriptor = klass.__dict__["templateId"]
            break
    assert isinstance(descriptor, property)

def test_r1_retrieve_has_scope():
    assert hasattr(r1_Retrieve, "scope")
    descriptor = None
    for klass in r1_Retrieve.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_aliasedquerysource_is_not_abstract():
    assert not inspect.isabstract(AliasedQuerySource)


def test_aliasedquerysource_constructor_exists():
    assert callable(AliasedQuerySource.__init__)


def test_aliasedquerysource_constructor_args():
    sig = inspect.signature(AliasedQuerySource.__init__)
    params = list(sig.parameters.keys())



def test_r1_querydefineref_is_not_abstract():
    assert not inspect.isabstract(r1_QueryDefineRef)


def test_r1_querydefineref_constructor_exists():
    assert callable(r1_QueryDefineRef.__init__)


def test_r1_querydefineref_constructor_args():
    sig = inspect.signature(r1_QueryDefineRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_querydefineref_has_name():
    assert hasattr(r1_QueryDefineRef, "name")
    descriptor = None
    for klass in r1_QueryDefineRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_sortclause_is_not_abstract():
    assert not inspect.isabstract(r1_SortClause)


def test_r1_sortclause_constructor_exists():
    assert callable(r1_SortClause.__init__)


def test_r1_sortclause_constructor_args():
    sig = inspect.signature(r1_SortClause.__init__)
    params = list(sig.parameters.keys())



def test_r1_returnclause_is_not_abstract():
    assert not inspect.isabstract(r1_ReturnClause)


def test_r1_returnclause_constructor_exists():
    assert callable(r1_ReturnClause.__init__)


def test_r1_returnclause_constructor_args():
    sig = inspect.signature(r1_ReturnClause.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_r1_returnclause_has_distinct():
    assert hasattr(r1_ReturnClause, "distinct")
    descriptor = None
    for klass in r1_ReturnClause.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_r1_relationshipclause_is_not_abstract():
    assert not inspect.isabstract(r1_RelationshipClause)


def test_r1_relationshipclause_constructor_exists():
    assert callable(r1_RelationshipClause.__init__)


def test_r1_relationshipclause_constructor_args():
    sig = inspect.signature(r1_RelationshipClause.__init__)
    params = list(sig.parameters.keys())



def test_r1_query_is_not_abstract():
    assert not inspect.isabstract(r1_Query)


def test_r1_query_constructor_exists():
    assert callable(r1_Query.__init__)


def test_r1_query_constructor_args():
    sig = inspect.signature(r1_Query.__init__)
    params = list(sig.parameters.keys())



def test_r1_quantity_is_not_abstract():
    assert not inspect.isabstract(r1_Quantity)


def test_r1_quantity_constructor_exists():
    assert callable(r1_Quantity.__init__)


def test_r1_quantity_constructor_args():
    sig = inspect.signature(r1_Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_r1_quantity_has_value():
    assert hasattr(r1_Quantity, "value")
    descriptor = None
    for klass in r1_Quantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_r1_quantity_has_unit():
    assert hasattr(r1_Quantity, "unit")
    descriptor = None
    for klass in r1_Quantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_r1_property_is_not_abstract():
    assert not inspect.isabstract(r1_Property)


def test_r1_property_constructor_exists():
    assert callable(r1_Property.__init__)


def test_r1_property_constructor_args():
    sig = inspect.signature(r1_Property.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "path" in params, "Missing parameter 'path'"

def test_r1_property_has_scope():
    assert hasattr(r1_Property, "scope")
    descriptor = None
    for klass in r1_Property.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_r1_property_has_path():
    assert hasattr(r1_Property, "path")
    descriptor = None
    for klass in r1_Property.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_r1_properincludes_is_not_abstract():
    assert not inspect.isabstract(r1_ProperIncludes)


def test_r1_properincludes_constructor_exists():
    assert callable(r1_ProperIncludes.__init__)


def test_r1_properincludes_constructor_args():
    sig = inspect.signature(r1_ProperIncludes.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_properincludes_has_precision():
    assert hasattr(r1_ProperIncludes, "precision")
    descriptor = None
    for klass in r1_ProperIncludes.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_properincludedin_is_not_abstract():
    assert not inspect.isabstract(r1_ProperIncludedIn)


def test_r1_properincludedin_constructor_exists():
    assert callable(r1_ProperIncludedIn.__init__)


def test_r1_properincludedin_constructor_args():
    sig = inspect.signature(r1_ProperIncludedIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_properincludedin_has_precision():
    assert hasattr(r1_ProperIncludedIn, "precision")
    descriptor = None
    for klass in r1_ProperIncludedIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_propercontains_is_not_abstract():
    assert not inspect.isabstract(r1_ProperContains)


def test_r1_propercontains_constructor_exists():
    assert callable(r1_ProperContains.__init__)


def test_r1_propercontains_constructor_args():
    sig = inspect.signature(r1_ProperContains.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_propercontains_has_precision():
    assert hasattr(r1_ProperContains, "precision")
    descriptor = None
    for klass in r1_ProperContains.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_predecessor_is_not_abstract():
    assert not inspect.isabstract(r1_Predecessor)


def test_r1_predecessor_constructor_exists():
    assert callable(r1_Predecessor.__init__)


def test_r1_predecessor_constructor_args():
    sig = inspect.signature(r1_Predecessor.__init__)
    params = list(sig.parameters.keys())



def test_r1_power_is_not_abstract():
    assert not inspect.isabstract(r1_Power)


def test_r1_power_constructor_exists():
    assert callable(r1_Power.__init__)


def test_r1_power_constructor_args():
    sig = inspect.signature(r1_Power.__init__)
    params = list(sig.parameters.keys())



def test_r1_positionof_is_not_abstract():
    assert not inspect.isabstract(r1_PositionOf)


def test_r1_positionof_constructor_exists():
    assert callable(r1_PositionOf.__init__)


def test_r1_positionof_constructor_args():
    sig = inspect.signature(r1_PositionOf.__init__)
    params = list(sig.parameters.keys())



def test_r1_populationvariance_is_not_abstract():
    assert not inspect.isabstract(r1_PopulationVariance)


def test_r1_populationvariance_constructor_exists():
    assert callable(r1_PopulationVariance.__init__)


def test_r1_populationvariance_constructor_args():
    sig = inspect.signature(r1_PopulationVariance.__init__)
    params = list(sig.parameters.keys())



def test_r1_populationstddev_is_not_abstract():
    assert not inspect.isabstract(r1_PopulationStdDev)


def test_r1_populationstddev_constructor_exists():
    assert callable(r1_PopulationStdDev.__init__)


def test_r1_populationstddev_constructor_args():
    sig = inspect.signature(r1_PopulationStdDev.__init__)
    params = list(sig.parameters.keys())



def test_r1_properin_is_not_abstract():
    assert not inspect.isabstract(r1_ProperIn)


def test_r1_properin_constructor_exists():
    assert callable(r1_ProperIn.__init__)


def test_r1_properin_constructor_args():
    sig = inspect.signature(r1_ProperIn.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_properin_has_precision():
    assert hasattr(r1_ProperIn, "precision")
    descriptor = None
    for klass in r1_ProperIn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_parameterdef_is_not_abstract():
    assert not inspect.isabstract(r1_ParameterDef)


def test_r1_parameterdef_constructor_exists():
    assert callable(r1_ParameterDef.__init__)


def test_r1_parameterdef_constructor_args():
    sig = inspect.signature(r1_ParameterDef.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "parameterType" in params, "Missing parameter 'parameterType'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_parameterdef_has_accessLevel():
    assert hasattr(r1_ParameterDef, "accessLevel")
    descriptor = None
    for klass in r1_ParameterDef.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_r1_parameterdef_has_parameterType():
    assert hasattr(r1_ParameterDef, "parameterType")
    descriptor = None
    for klass in r1_ParameterDef.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)

def test_r1_parameterdef_has_name():
    assert hasattr(r1_ParameterDef, "name")
    descriptor = None
    for klass in r1_ParameterDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_overlapsbefore_is_not_abstract():
    assert not inspect.isabstract(r1_OverlapsBefore)


def test_r1_overlapsbefore_constructor_exists():
    assert callable(r1_OverlapsBefore.__init__)


def test_r1_overlapsbefore_constructor_args():
    sig = inspect.signature(r1_OverlapsBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_overlapsbefore_has_precision():
    assert hasattr(r1_OverlapsBefore, "precision")
    descriptor = None
    for klass in r1_OverlapsBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_overlapsafter_is_not_abstract():
    assert not inspect.isabstract(r1_OverlapsAfter)


def test_r1_overlapsafter_constructor_exists():
    assert callable(r1_OverlapsAfter.__init__)


def test_r1_overlapsafter_constructor_args():
    sig = inspect.signature(r1_OverlapsAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_overlapsafter_has_precision():
    assert hasattr(r1_OverlapsAfter, "precision")
    descriptor = None
    for klass in r1_OverlapsAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_overlaps_is_not_abstract():
    assert not inspect.isabstract(r1_Overlaps)


def test_r1_overlaps_constructor_exists():
    assert callable(r1_Overlaps.__init__)


def test_r1_overlaps_constructor_args():
    sig = inspect.signature(r1_Overlaps.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_overlaps_has_precision():
    assert hasattr(r1_Overlaps, "precision")
    descriptor = None
    for klass in r1_Overlaps.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_or_is_not_abstract():
    assert not inspect.isabstract(r1_Or)


def test_r1_or_constructor_exists():
    assert callable(r1_Or.__init__)


def test_r1_or_constructor_args():
    sig = inspect.signature(r1_Or.__init__)
    params = list(sig.parameters.keys())



def test_r1_parameterref_is_not_abstract():
    assert not inspect.isabstract(r1_ParameterRef)


def test_r1_parameterref_constructor_exists():
    assert callable(r1_ParameterRef.__init__)


def test_r1_parameterref_constructor_args():
    sig = inspect.signature(r1_ParameterRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_parameterref_has_libraryName():
    assert hasattr(r1_ParameterRef, "libraryName")
    descriptor = None
    for klass in r1_ParameterRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1_parameterref_has_name():
    assert hasattr(r1_ParameterRef, "name")
    descriptor = None
    for klass in r1_ParameterRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_null_is_not_abstract():
    assert not inspect.isabstract(r1_Null)


def test_r1_null_constructor_exists():
    assert callable(r1_Null.__init__)


def test_r1_null_constructor_args():
    sig = inspect.signature(r1_Null.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1_null_has_valueType():
    assert hasattr(r1_Null, "valueType")
    descriptor = None
    for klass in r1_Null.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1_now_is_not_abstract():
    assert not inspect.isabstract(r1_Now)


def test_r1_now_constructor_exists():
    assert callable(r1_Now.__init__)


def test_r1_now_constructor_args():
    sig = inspect.signature(r1_Now.__init__)
    params = list(sig.parameters.keys())



def test_r1_notequal_is_not_abstract():
    assert not inspect.isabstract(r1_NotEqual)


def test_r1_notequal_constructor_exists():
    assert callable(r1_NotEqual.__init__)


def test_r1_notequal_constructor_args():
    sig = inspect.signature(r1_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1_not_is_not_abstract():
    assert not inspect.isabstract(r1_Not)


def test_r1_not_constructor_exists():
    assert callable(r1_Not.__init__)


def test_r1_not_constructor_args():
    sig = inspect.signature(r1_Not.__init__)
    params = list(sig.parameters.keys())



def test_r1_negate_is_not_abstract():
    assert not inspect.isabstract(r1_Negate)


def test_r1_negate_constructor_exists():
    assert callable(r1_Negate.__init__)


def test_r1_negate_constructor_args():
    sig = inspect.signature(r1_Negate.__init__)
    params = list(sig.parameters.keys())



def test_r1_operandref_is_not_abstract():
    assert not inspect.isabstract(r1_OperandRef)


def test_r1_operandref_constructor_exists():
    assert callable(r1_OperandRef.__init__)


def test_r1_operandref_constructor_args():
    sig = inspect.signature(r1_OperandRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_operandref_has_name():
    assert hasattr(r1_OperandRef, "name")
    descriptor = None
    for klass in r1_OperandRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_multiply_is_not_abstract():
    assert not inspect.isabstract(r1_Multiply)


def test_r1_multiply_constructor_exists():
    assert callable(r1_Multiply.__init__)


def test_r1_multiply_constructor_args():
    sig = inspect.signature(r1_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_r1_modulo_is_not_abstract():
    assert not inspect.isabstract(r1_Modulo)


def test_r1_modulo_constructor_exists():
    assert callable(r1_Modulo.__init__)


def test_r1_modulo_constructor_args():
    sig = inspect.signature(r1_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_r1_mode_is_not_abstract():
    assert not inspect.isabstract(r1_Mode)


def test_r1_mode_constructor_exists():
    assert callable(r1_Mode.__init__)


def test_r1_mode_constructor_args():
    sig = inspect.signature(r1_Mode.__init__)
    params = list(sig.parameters.keys())



def test_r1_minvalue_is_not_abstract():
    assert not inspect.isabstract(r1_MinValue)


def test_r1_minvalue_constructor_exists():
    assert callable(r1_MinValue.__init__)


def test_r1_minvalue_constructor_args():
    sig = inspect.signature(r1_MinValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1_minvalue_has_valueType():
    assert hasattr(r1_MinValue, "valueType")
    descriptor = None
    for klass in r1_MinValue.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1_min_is_not_abstract():
    assert not inspect.isabstract(r1_Min)


def test_r1_min_constructor_exists():
    assert callable(r1_Min.__init__)


def test_r1_min_constructor_args():
    sig = inspect.signature(r1_Min.__init__)
    params = list(sig.parameters.keys())



def test_r1_meetsbefore_is_not_abstract():
    assert not inspect.isabstract(r1_MeetsBefore)


def test_r1_meetsbefore_constructor_exists():
    assert callable(r1_MeetsBefore.__init__)


def test_r1_meetsbefore_constructor_args():
    sig = inspect.signature(r1_MeetsBefore.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_meetsbefore_has_precision():
    assert hasattr(r1_MeetsBefore, "precision")
    descriptor = None
    for klass in r1_MeetsBefore.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_meetsafter_is_not_abstract():
    assert not inspect.isabstract(r1_MeetsAfter)


def test_r1_meetsafter_constructor_exists():
    assert callable(r1_MeetsAfter.__init__)


def test_r1_meetsafter_constructor_args():
    sig = inspect.signature(r1_MeetsAfter.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_meetsafter_has_precision():
    assert hasattr(r1_MeetsAfter, "precision")
    descriptor = None
    for klass in r1_MeetsAfter.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_naryexpression_is_not_abstract():
    assert not inspect.isabstract(r1_NaryExpression)


def test_r1_naryexpression_constructor_exists():
    assert callable(r1_NaryExpression.__init__)


def test_r1_naryexpression_constructor_args():
    sig = inspect.signature(r1_NaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_r1_maxvalue_is_not_abstract():
    assert not inspect.isabstract(r1_MaxValue)


def test_r1_maxvalue_constructor_exists():
    assert callable(r1_MaxValue.__init__)


def test_r1_maxvalue_constructor_args():
    sig = inspect.signature(r1_MaxValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_r1_maxvalue_has_valueType():
    assert hasattr(r1_MaxValue, "valueType")
    descriptor = None
    for klass in r1_MaxValue.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)



def test_r1_max_is_not_abstract():
    assert not inspect.isabstract(r1_Max)


def test_r1_max_constructor_exists():
    assert callable(r1_Max.__init__)


def test_r1_max_constructor_args():
    sig = inspect.signature(r1_Max.__init__)
    params = list(sig.parameters.keys())



def test_r1_matches_is_not_abstract():
    assert not inspect.isabstract(r1_Matches)


def test_r1_matches_constructor_exists():
    assert callable(r1_Matches.__init__)


def test_r1_matches_constructor_args():
    sig = inspect.signature(r1_Matches.__init__)
    params = list(sig.parameters.keys())



def test_r1_lower_is_not_abstract():
    assert not inspect.isabstract(r1_Lower)


def test_r1_lower_constructor_exists():
    assert callable(r1_Lower.__init__)


def test_r1_lower_constructor_args():
    sig = inspect.signature(r1_Lower.__init__)
    params = list(sig.parameters.keys())



def test_r1_log_is_not_abstract():
    assert not inspect.isabstract(r1_Log)


def test_r1_log_constructor_exists():
    assert callable(r1_Log.__init__)


def test_r1_log_constructor_args():
    sig = inspect.signature(r1_Log.__init__)
    params = list(sig.parameters.keys())



def test_r1_ln_is_not_abstract():
    assert not inspect.isabstract(r1_Ln)


def test_r1_ln_constructor_exists():
    assert callable(r1_Ln.__init__)


def test_r1_ln_constructor_args():
    sig = inspect.signature(r1_Ln.__init__)
    params = list(sig.parameters.keys())



def test_r1_literal_is_not_abstract():
    assert not inspect.isabstract(r1_Literal)


def test_r1_literal_constructor_exists():
    assert callable(r1_Literal.__init__)


def test_r1_literal_constructor_args():
    sig = inspect.signature(r1_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "value" in params, "Missing parameter 'value'"

def test_r1_literal_has_valueType():
    assert hasattr(r1_Literal, "valueType")
    descriptor = None
    for klass in r1_Literal.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_r1_literal_has_value():
    assert hasattr(r1_Literal, "value")
    descriptor = None
    for klass in r1_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r1_meets_is_not_abstract():
    assert not inspect.isabstract(r1_Meets)


def test_r1_meets_constructor_exists():
    assert callable(r1_Meets.__init__)


def test_r1_meets_constructor_args():
    sig = inspect.signature(r1_Meets.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_r1_meets_has_precision():
    assert hasattr(r1_Meets, "precision")
    descriptor = None
    for klass in r1_Meets.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_r1_median_is_not_abstract():
    assert not inspect.isabstract(r1_Median)


def test_r1_median_constructor_exists():
    assert callable(r1_Median.__init__)


def test_r1_median_constructor_args():
    sig = inspect.signature(r1_Median.__init__)
    params = list(sig.parameters.keys())



def test_r1_list_is_not_abstract():
    assert not inspect.isabstract(r1_List)


def test_r1_list_constructor_exists():
    assert callable(r1_List.__init__)


def test_r1_list_constructor_args():
    sig = inspect.signature(r1_List.__init__)
    params = list(sig.parameters.keys())



def test_r1_lessorequal_is_not_abstract():
    assert not inspect.isabstract(r1_LessOrEqual)


def test_r1_lessorequal_constructor_exists():
    assert callable(r1_LessOrEqual.__init__)


def test_r1_lessorequal_constructor_args():
    sig = inspect.signature(r1_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_r1_less_is_not_abstract():
    assert not inspect.isabstract(r1_Less)


def test_r1_less_constructor_exists():
    assert callable(r1_Less.__init__)


def test_r1_less_constructor_args():
    sig = inspect.signature(r1_Less.__init__)
    params = list(sig.parameters.keys())



def test_r1_length_is_not_abstract():
    assert not inspect.isabstract(r1_Length)


def test_r1_length_constructor_exists():
    assert callable(r1_Length.__init__)


def test_r1_length_constructor_args():
    sig = inspect.signature(r1_Length.__init__)
    params = list(sig.parameters.keys())



def test_r1_last_is_not_abstract():
    assert not inspect.isabstract(r1_Last)


def test_r1_last_constructor_exists():
    assert callable(r1_Last.__init__)


def test_r1_last_constructor_args():
    sig = inspect.signature(r1_Last.__init__)
    params = list(sig.parameters.keys())
    assert "orderBy" in params, "Missing parameter 'orderBy'"

def test_r1_last_has_orderBy():
    assert hasattr(r1_Last, "orderBy")
    descriptor = None
    for klass in r1_Last.__mro__:
        if "orderBy" in klass.__dict__:
            descriptor = klass.__dict__["orderBy"]
            break
    assert isinstance(descriptor, property)



def test_r1_istrue_is_not_abstract():
    assert not inspect.isabstract(r1_IsTrue)


def test_r1_istrue_constructor_exists():
    assert callable(r1_IsTrue.__init__)


def test_r1_istrue_constructor_args():
    sig = inspect.signature(r1_IsTrue.__init__)
    params = list(sig.parameters.keys())



def test_r1_isnull_is_not_abstract():
    assert not inspect.isabstract(r1_IsNull)


def test_r1_isnull_constructor_exists():
    assert callable(r1_IsNull.__init__)


def test_r1_isnull_constructor_args():
    sig = inspect.signature(r1_IsNull.__init__)
    params = list(sig.parameters.keys())



def test_r1_is_is_not_abstract():
    assert not inspect.isabstract(r1_Is)


def test_r1_is_constructor_exists():
    assert callable(r1_Is.__init__)


def test_r1_is_constructor_args():
    sig = inspect.signature(r1_Is.__init__)
    params = list(sig.parameters.keys())
    assert "isType" in params, "Missing parameter 'isType'"

def test_r1_is_has_isType():
    assert hasattr(r1_Is, "isType")
    descriptor = None
    for klass in r1_Is.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)



def test_r1_valuesetref_is_not_abstract():
    assert not inspect.isabstract(r1_ValueSetRef)


def test_r1_valuesetref_constructor_exists():
    assert callable(r1_ValueSetRef.__init__)


def test_r1_valuesetref_constructor_args():
    sig = inspect.signature(r1_ValueSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "name" in params, "Missing parameter 'name'"

def test_r1_valuesetref_has_libraryName():
    assert hasattr(r1_ValueSetRef, "libraryName")
    descriptor = None
    for klass in r1_ValueSetRef.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_r1_valuesetref_has_name():
    assert hasattr(r1_ValueSetRef, "name")
    descriptor = None
    for klass in r1_ValueSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_invalueset_is_not_abstract():
    assert not inspect.isabstract(r1_InValueSet)


def test_r1_invalueset_constructor_exists():
    assert callable(r1_InValueSet.__init__)


def test_r1_invalueset_constructor_args():
    sig = inspect.signature(r1_InValueSet.__init__)
    params = list(sig.parameters.keys())



def test_typespecifier_is_not_abstract():
    assert not inspect.isabstract(TypeSpecifier)


def test_typespecifier_constructor_exists():
    assert callable(TypeSpecifier.__init__)


def test_typespecifier_constructor_args():
    sig = inspect.signature(TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1_namedtypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1_NamedTypeSpecifier)


def test_r1_namedtypespecifier_constructor_exists():
    assert callable(r1_NamedTypeSpecifier.__init__)


def test_r1_namedtypespecifier_constructor_args():
    sig = inspect.signature(r1_NamedTypeSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_r1_namedtypespecifier_has_name():
    assert hasattr(r1_NamedTypeSpecifier, "name")
    descriptor = None
    for klass in r1_NamedTypeSpecifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_r1_tupletypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1_TupleTypeSpecifier)


def test_r1_tupletypespecifier_constructor_exists():
    assert callable(r1_TupleTypeSpecifier.__init__)


def test_r1_tupletypespecifier_constructor_args():
    sig = inspect.signature(r1_TupleTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1_listtypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1_ListTypeSpecifier)


def test_r1_listtypespecifier_constructor_exists():
    assert callable(r1_ListTypeSpecifier.__init__)


def test_r1_listtypespecifier_constructor_args():
    sig = inspect.signature(r1_ListTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1_intervaltypespecifier_is_not_abstract():
    assert not inspect.isabstract(r1_IntervalTypeSpecifier)


def test_r1_intervaltypespecifier_constructor_exists():
    assert callable(r1_IntervalTypeSpecifier.__init__)


def test_r1_intervaltypespecifier_constructor_args():
    sig = inspect.signature(r1_IntervalTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_r1_isfalse_is_not_abstract():
    assert not inspect.isabstract(r1_IsFalse)


def test_r1_isfalse_constructor_exists():
    assert callable(r1_IsFalse.__init__)


def test_r1_isfalse_constructor_args():
    sig = inspect.signature(r1_IsFalse.__init__)
    params = list(sig.parameters.keys())

def test_accessmodifier_exists():
    # Check that the Enumeration exists
    assert AccessModifier is not None

def test_accessmodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifier]
    expected_literals = [
        "Public",
        "Private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifier"

def test_datetimeprecision_exists():
    # Check that the Enumeration exists
    assert DateTimePrecision is not None

def test_datetimeprecision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateTimePrecision]
    expected_literals = [
        "Day",
        "Hour",
        "Year",
        "Second",
        "Month",
        "Minute",
        "Week",
        "Millisecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateTimePrecision"

def test_sortdirection_exists():
    # Check that the Enumeration exists
    assert SortDirection is not None

def test_sortdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortDirection]
    expected_literals = [
        "desc",
        "ascending",
        "asc",
        "descending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortDirection"


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
r1_InstanceElement_strategy = st.builds(
    r1_InstanceElement,
    name=
        safe_text
)
ExpressionDef_strategy = st.builds(
    ExpressionDef,
)
r1_FunctionDef_strategy = st.builds(
    r1_FunctionDef,
)
ExpressionRef_strategy = st.builds(
    ExpressionRef,
)
r1_FunctionRef_strategy = st.builds(
    r1_FunctionRef,
)
r1_EObject_strategy = st.builds(
    r1_EObject,
)
r1_Element_strategy = st.builds(
    r1_Element,
    localId=
        safe_text
)
NaryExpression_strategy = st.builds(
    NaryExpression,
)
r1_Concatenate_strategy = st.builds(
    r1_Concatenate,
)
r1_Coalesce_strategy = st.builds(
    r1_Coalesce,
)
AggregateExpression_strategy = st.builds(
    AggregateExpression,
)
r1_Count_strategy = st.builds(
    r1_Count,
)
r1_AnyTrue_strategy = st.builds(
    r1_AnyTrue,
)
r1_Avg_strategy = st.builds(
    r1_Avg,
)
r1_AllTrue_strategy = st.builds(
    r1_AllTrue,
)
SortByItem_strategy = st.builds(
    SortByItem,
)
r1_ByDirection_strategy = st.builds(
    r1_ByDirection,
)
r1_ByExpression_strategy = st.builds(
    r1_ByExpression,
)
r1_ByColumn_strategy = st.builds(
    r1_ByColumn,
    path=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
r1_DefineClause_strategy = st.builds(
    r1_DefineClause,
    identifier=
        safe_text
)
r1_CodeSystemDef_strategy = st.builds(
    r1_CodeSystemDef,
    name=
        safe_text,
    accessLevel=
        safe_text,
    version=
        safe_text,
    id=
        safe_text
)
r1_OperandDef_strategy = st.builds(
    r1_OperandDef,
    name=
        safe_text,
    operandType=
        safe_text
)
r1_ExpressionDef_strategy = st.builds(
    r1_ExpressionDef,
    context=
        safe_text,
    accessLevel=
        safe_text,
    name=
        safe_text
)
r1_CaseItem_strategy = st.builds(
    r1_CaseItem,
)
r1_TypeSpecifier_strategy = st.builds(
    r1_TypeSpecifier,
)
r1_AliasedQuerySource_strategy = st.builds(
    r1_AliasedQuerySource,
    alias=
        safe_text
)
r1_Expression_strategy = st.builds(
    r1_Expression,
)
Expression_strategy = st.builds(
    Expression,
)
r1_If_strategy = st.builds(
    r1_If,
)
r1_Current_strategy = st.builds(
    r1_Current,
    scope=
        safe_text
)
r1_InCodeSystem_strategy = st.builds(
    r1_InCodeSystem,
)
r1_Concept_strategy = st.builds(
    r1_Concept,
    display=
        safe_text
)
r1_Case_strategy = st.builds(
    r1_Case,
)
r1_AliasRef_strategy = st.builds(
    r1_AliasRef,
    name=
        safe_text
)
r1_Instance_strategy = st.builds(
    r1_Instance,
    classType=
        safe_text
)
r1_IdentifierRef_strategy = st.builds(
    r1_IdentifierRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1_Interval_strategy = st.builds(
    r1_Interval,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r1_ForEach_strategy = st.builds(
    r1_ForEach,
    scope=
        safe_text
)
r1_Filter_strategy = st.builds(
    r1_Filter,
    scope=
        safe_text
)
r1_First_strategy = st.builds(
    r1_First,
    orderBy=
        safe_text
)
r1_Code_strategy = st.builds(
    r1_Code,
    display=
        safe_text,
    code=
        safe_text
)
r1_ExpressionRef_strategy = st.builds(
    r1_ExpressionRef,
    name=
        safe_text,
    libraryName=
        safe_text
)
r1_DateTime_strategy = st.builds(
    r1_DateTime,
)
r1_CodeSystemRef_strategy = st.builds(
    r1_CodeSystemRef,
    name=
        safe_text,
    libraryName=
        safe_text
)
r1_BinaryExpression_strategy = st.builds(
    r1_BinaryExpression,
)
r1_Combine_strategy = st.builds(
    r1_Combine,
)
r1_IndexOf_strategy = st.builds(
    r1_IndexOf,
)
r1_AggregateExpression_strategy = st.builds(
    r1_AggregateExpression,
    path=
        safe_text
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
r1_Divide_strategy = st.builds(
    r1_Divide,
)
r1_After_strategy = st.builds(
    r1_After,
    precision=
        safe_text
)
r1_Indexer_strategy = st.builds(
    r1_Indexer,
)
r1_GreaterOrEqual_strategy = st.builds(
    r1_GreaterOrEqual,
)
r1_Contains_strategy = st.builds(
    r1_Contains,
    precision=
        safe_text
)
r1_Before_strategy = st.builds(
    r1_Before,
    precision=
        safe_text
)
r1_And_strategy = st.builds(
    r1_And,
)
r1_DifferenceBetween_strategy = st.builds(
    r1_DifferenceBetween,
    precision=
        safe_text
)
r1_Except_strategy = st.builds(
    r1_Except,
)
r1_DurationBetween_strategy = st.builds(
    r1_DurationBetween,
    precision=
        safe_text
)
r1_Includes_strategy = st.builds(
    r1_Includes,
    precision=
        safe_text
)
r1_IncludedIn_strategy = st.builds(
    r1_IncludedIn,
    precision=
        safe_text
)
r1_CalculateAgeAt_strategy = st.builds(
    r1_CalculateAgeAt,
    precision=
        safe_text
)
r1_In_strategy = st.builds(
    r1_In,
    precision=
        safe_text
)
r1_Equal_strategy = st.builds(
    r1_Equal,
)
r1_Ends_strategy = st.builds(
    r1_Ends,
    precision=
        safe_text
)
r1_Intersect_strategy = st.builds(
    r1_Intersect,
)
r1_Greater_strategy = st.builds(
    r1_Greater,
)
r1_Add_strategy = st.builds(
    r1_Add,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
r1_CalculateAge_strategy = st.builds(
    r1_CalculateAge,
    precision=
        safe_text
)
r1_Floor_strategy = st.builds(
    r1_Floor,
)
r1_Convert_strategy = st.builds(
    r1_Convert,
    toType=
        safe_text
)
r1_End_strategy = st.builds(
    r1_End,
)
r1_DateTimeComponentFrom_strategy = st.builds(
    r1_DateTimeComponentFrom,
    precision=
        safe_text
)
r1_Distinct_strategy = st.builds(
    r1_Distinct,
)
r1_Collapse_strategy = st.builds(
    r1_Collapse,
)
r1_As_strategy = st.builds(
    r1_As,
    strict=
        safe_text,
    asType=
        safe_text
)
r1_Expand_strategy = st.builds(
    r1_Expand,
)
r1_Ceiling_strategy = st.builds(
    r1_Ceiling,
)
r1_Exists_strategy = st.builds(
    r1_Exists,
)
r1_DateFrom_strategy = st.builds(
    r1_DateFrom,
)
r1_Abs_strategy = st.builds(
    r1_Abs,
)
r1_Xor_strategy = st.builds(
    r1_Xor,
)
RelationshipClause_strategy = st.builds(
    RelationshipClause,
)
r1_Without_strategy = st.builds(
    r1_Without,
)
r1_With_strategy = st.builds(
    r1_With,
)
r1_Width_strategy = st.builds(
    r1_Width,
)
r1_Variance_strategy = st.builds(
    r1_Variance,
)
r1_Upper_strategy = st.builds(
    r1_Upper,
)
r1_Union_strategy = st.builds(
    r1_Union,
)
r1_UnaryExpression_strategy = st.builds(
    r1_UnaryExpression,
)
r1_TupleElementDefinition_strategy = st.builds(
    r1_TupleElementDefinition,
    name=
        safe_text
)
r1_ValueSetDef_strategy = st.builds(
    r1_ValueSetDef,
    accessLevel=
        safe_text,
    id=
        safe_text,
    version=
        safe_text,
    name=
        safe_text
)
r1_TupleElement_strategy = st.builds(
    r1_TupleElement,
    name=
        safe_text
)
r1_Tuple_strategy = st.builds(
    r1_Tuple,
)
r1_TruncatedDivide_strategy = st.builds(
    r1_TruncatedDivide,
)
r1_Truncate_strategy = st.builds(
    r1_Truncate,
)
r1_Today_strategy = st.builds(
    r1_Today,
)
r1_TimezoneFrom_strategy = st.builds(
    r1_TimezoneFrom,
)
r1_Times_strategy = st.builds(
    r1_Times,
)
r1_TimeOfDay_strategy = st.builds(
    r1_TimeOfDay,
)
r1_TimeFrom_strategy = st.builds(
    r1_TimeFrom,
)
r1_Time_strategy = st.builds(
    r1_Time,
)
r1_TernaryExpression_strategy = st.builds(
    r1_TernaryExpression,
)
r1_Sum_strategy = st.builds(
    r1_Sum,
)
r1_Successor_strategy = st.builds(
    r1_Successor,
)
r1_Subtract_strategy = st.builds(
    r1_Subtract,
)
r1_StdDev_strategy = st.builds(
    r1_StdDev,
)
r1_Starts_strategy = st.builds(
    r1_Starts,
    precision=
        safe_text
)
r1_Start_strategy = st.builds(
    r1_Start,
)
r1_Split_strategy = st.builds(
    r1_Split,
)
r1_Substring_strategy = st.builds(
    r1_Substring,
)
r1_SortByItem_strategy = st.builds(
    r1_SortByItem,
    direction=
        safe_text
)
r1_Sort_strategy = st.builds(
    r1_Sort,
)
r1_SingletonFrom_strategy = st.builds(
    r1_SingletonFrom,
)
r1_SameOrBefore_strategy = st.builds(
    r1_SameOrBefore,
    precision=
        safe_text
)
r1_SameOrAfter_strategy = st.builds(
    r1_SameOrAfter,
    precision=
        safe_text
)
r1_SameAs_strategy = st.builds(
    r1_SameAs,
    precision=
        safe_text
)
r1_Round_strategy = st.builds(
    r1_Round,
)
r1_Retrieve_strategy = st.builds(
    r1_Retrieve,
    dataType=
        safe_text,
    idProperty=
        safe_text,
    dateProperty=
        safe_text,
    dateHighProperty=
        safe_text,
    codeProperty=
        safe_text,
    dateLowProperty=
        safe_text,
    templateId=
        safe_text,
    scope=
        safe_text
)
AliasedQuerySource_strategy = st.builds(
    AliasedQuerySource,
)
r1_QueryDefineRef_strategy = st.builds(
    r1_QueryDefineRef,
    name=
        safe_text
)
r1_SortClause_strategy = st.builds(
    r1_SortClause,
)
r1_ReturnClause_strategy = st.builds(
    r1_ReturnClause,
    distinct=
        safe_text
)
r1_RelationshipClause_strategy = st.builds(
    r1_RelationshipClause,
)
r1_Query_strategy = st.builds(
    r1_Query,
)
r1_Quantity_strategy = st.builds(
    r1_Quantity,
    value=
        safe_text,
    unit=
        safe_text
)
r1_Property_strategy = st.builds(
    r1_Property,
    scope=
        safe_text,
    path=
        safe_text
)
r1_ProperIncludes_strategy = st.builds(
    r1_ProperIncludes,
    precision=
        safe_text
)
r1_ProperIncludedIn_strategy = st.builds(
    r1_ProperIncludedIn,
    precision=
        safe_text
)
r1_ProperContains_strategy = st.builds(
    r1_ProperContains,
    precision=
        safe_text
)
r1_Predecessor_strategy = st.builds(
    r1_Predecessor,
)
r1_Power_strategy = st.builds(
    r1_Power,
)
r1_PositionOf_strategy = st.builds(
    r1_PositionOf,
)
r1_PopulationVariance_strategy = st.builds(
    r1_PopulationVariance,
)
r1_PopulationStdDev_strategy = st.builds(
    r1_PopulationStdDev,
)
r1_ProperIn_strategy = st.builds(
    r1_ProperIn,
    precision=
        safe_text
)
r1_ParameterDef_strategy = st.builds(
    r1_ParameterDef,
    accessLevel=
        safe_text,
    parameterType=
        safe_text,
    name=
        safe_text
)
r1_OverlapsBefore_strategy = st.builds(
    r1_OverlapsBefore,
    precision=
        safe_text
)
r1_OverlapsAfter_strategy = st.builds(
    r1_OverlapsAfter,
    precision=
        safe_text
)
r1_Overlaps_strategy = st.builds(
    r1_Overlaps,
    precision=
        safe_text
)
r1_Or_strategy = st.builds(
    r1_Or,
)
r1_ParameterRef_strategy = st.builds(
    r1_ParameterRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1_Null_strategy = st.builds(
    r1_Null,
    valueType=
        safe_text
)
r1_Now_strategy = st.builds(
    r1_Now,
)
r1_NotEqual_strategy = st.builds(
    r1_NotEqual,
)
r1_Not_strategy = st.builds(
    r1_Not,
)
r1_Negate_strategy = st.builds(
    r1_Negate,
)
r1_OperandRef_strategy = st.builds(
    r1_OperandRef,
    name=
        safe_text
)
r1_Multiply_strategy = st.builds(
    r1_Multiply,
)
r1_Modulo_strategy = st.builds(
    r1_Modulo,
)
r1_Mode_strategy = st.builds(
    r1_Mode,
)
r1_MinValue_strategy = st.builds(
    r1_MinValue,
    valueType=
        safe_text
)
r1_Min_strategy = st.builds(
    r1_Min,
)
r1_MeetsBefore_strategy = st.builds(
    r1_MeetsBefore,
    precision=
        safe_text
)
r1_MeetsAfter_strategy = st.builds(
    r1_MeetsAfter,
    precision=
        safe_text
)
r1_NaryExpression_strategy = st.builds(
    r1_NaryExpression,
)
r1_MaxValue_strategy = st.builds(
    r1_MaxValue,
    valueType=
        safe_text
)
r1_Max_strategy = st.builds(
    r1_Max,
)
r1_Matches_strategy = st.builds(
    r1_Matches,
)
r1_Lower_strategy = st.builds(
    r1_Lower,
)
r1_Log_strategy = st.builds(
    r1_Log,
)
r1_Ln_strategy = st.builds(
    r1_Ln,
)
r1_Literal_strategy = st.builds(
    r1_Literal,
    valueType=
        safe_text,
    value=
        safe_text
)
r1_Meets_strategy = st.builds(
    r1_Meets,
    precision=
        safe_text
)
r1_Median_strategy = st.builds(
    r1_Median,
)
r1_List_strategy = st.builds(
    r1_List,
)
r1_LessOrEqual_strategy = st.builds(
    r1_LessOrEqual,
)
r1_Less_strategy = st.builds(
    r1_Less,
)
r1_Length_strategy = st.builds(
    r1_Length,
)
r1_Last_strategy = st.builds(
    r1_Last,
    orderBy=
        safe_text
)
r1_IsTrue_strategy = st.builds(
    r1_IsTrue,
)
r1_IsNull_strategy = st.builds(
    r1_IsNull,
)
r1_Is_strategy = st.builds(
    r1_Is,
    isType=
        safe_text
)
r1_ValueSetRef_strategy = st.builds(
    r1_ValueSetRef,
    libraryName=
        safe_text,
    name=
        safe_text
)
r1_InValueSet_strategy = st.builds(
    r1_InValueSet,
)
TypeSpecifier_strategy = st.builds(
    TypeSpecifier,
)
r1_NamedTypeSpecifier_strategy = st.builds(
    r1_NamedTypeSpecifier,
    name=
        safe_text
)
r1_TupleTypeSpecifier_strategy = st.builds(
    r1_TupleTypeSpecifier,
)
r1_ListTypeSpecifier_strategy = st.builds(
    r1_ListTypeSpecifier,
)
r1_IntervalTypeSpecifier_strategy = st.builds(
    r1_IntervalTypeSpecifier,
)
r1_IsFalse_strategy = st.builds(
    r1_IsFalse,
)

@given(instance=r1_InstanceElement_strategy)
@settings(max_examples=50)
def test_r1_instanceelement_instantiation(instance):
    assert isinstance(instance, r1_InstanceElement)



@given(instance=r1_InstanceElement_strategy)
def test_r1_instanceelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpressionDef_strategy)
@settings(max_examples=50)
def test_expressiondef_instantiation(instance):
    assert isinstance(instance, ExpressionDef)

@given(instance=r1_FunctionDef_strategy)
@settings(max_examples=50)
def test_r1_functiondef_instantiation(instance):
    assert isinstance(instance, r1_FunctionDef)

@given(instance=ExpressionRef_strategy)
@settings(max_examples=50)
def test_expressionref_instantiation(instance):
    assert isinstance(instance, ExpressionRef)

@given(instance=r1_FunctionRef_strategy)
@settings(max_examples=50)
def test_r1_functionref_instantiation(instance):
    assert isinstance(instance, r1_FunctionRef)

@given(instance=r1_EObject_strategy)
@settings(max_examples=50)
def test_r1_eobject_instantiation(instance):
    assert isinstance(instance, r1_EObject)

@given(instance=r1_Element_strategy)
@settings(max_examples=50)
def test_r1_element_instantiation(instance):
    assert isinstance(instance, r1_Element)



@given(instance=r1_Element_strategy)
def test_r1_element_localId_setter(instance):
    original = instance.localId
    instance.localId = original
    assert instance.localId == original

@given(instance=NaryExpression_strategy)
@settings(max_examples=50)
def test_naryexpression_instantiation(instance):
    assert isinstance(instance, NaryExpression)

@given(instance=r1_Concatenate_strategy)
@settings(max_examples=50)
def test_r1_concatenate_instantiation(instance):
    assert isinstance(instance, r1_Concatenate)

@given(instance=r1_Coalesce_strategy)
@settings(max_examples=50)
def test_r1_coalesce_instantiation(instance):
    assert isinstance(instance, r1_Coalesce)

@given(instance=AggregateExpression_strategy)
@settings(max_examples=50)
def test_aggregateexpression_instantiation(instance):
    assert isinstance(instance, AggregateExpression)

@given(instance=r1_Count_strategy)
@settings(max_examples=50)
def test_r1_count_instantiation(instance):
    assert isinstance(instance, r1_Count)

@given(instance=r1_AnyTrue_strategy)
@settings(max_examples=50)
def test_r1_anytrue_instantiation(instance):
    assert isinstance(instance, r1_AnyTrue)

@given(instance=r1_Avg_strategy)
@settings(max_examples=50)
def test_r1_avg_instantiation(instance):
    assert isinstance(instance, r1_Avg)

@given(instance=r1_AllTrue_strategy)
@settings(max_examples=50)
def test_r1_alltrue_instantiation(instance):
    assert isinstance(instance, r1_AllTrue)

@given(instance=SortByItem_strategy)
@settings(max_examples=50)
def test_sortbyitem_instantiation(instance):
    assert isinstance(instance, SortByItem)

@given(instance=r1_ByDirection_strategy)
@settings(max_examples=50)
def test_r1_bydirection_instantiation(instance):
    assert isinstance(instance, r1_ByDirection)

@given(instance=r1_ByExpression_strategy)
@settings(max_examples=50)
def test_r1_byexpression_instantiation(instance):
    assert isinstance(instance, r1_ByExpression)

@given(instance=r1_ByColumn_strategy)
@settings(max_examples=50)
def test_r1_bycolumn_instantiation(instance):
    assert isinstance(instance, r1_ByColumn)



@given(instance=r1_ByColumn_strategy)
def test_r1_bycolumn_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=r1_DefineClause_strategy)
@settings(max_examples=50)
def test_r1_defineclause_instantiation(instance):
    assert isinstance(instance, r1_DefineClause)



@given(instance=r1_DefineClause_strategy)
def test_r1_defineclause_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=r1_CodeSystemDef_strategy)
@settings(max_examples=50)
def test_r1_codesystemdef_instantiation(instance):
    assert isinstance(instance, r1_CodeSystemDef)



@given(instance=r1_CodeSystemDef_strategy)
def test_r1_codesystemdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=r1_CodeSystemDef_strategy)
def test_r1_codesystemdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original



@given(instance=r1_CodeSystemDef_strategy)
def test_r1_codesystemdef_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=r1_CodeSystemDef_strategy)
def test_r1_codesystemdef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=r1_OperandDef_strategy)
@settings(max_examples=50)
def test_r1_operanddef_instantiation(instance):
    assert isinstance(instance, r1_OperandDef)



@given(instance=r1_OperandDef_strategy)
def test_r1_operanddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=r1_OperandDef_strategy)
def test_r1_operanddef_operandType_setter(instance):
    original = instance.operandType
    instance.operandType = original
    assert instance.operandType == original

@given(instance=r1_ExpressionDef_strategy)
@settings(max_examples=50)
def test_r1_expressiondef_instantiation(instance):
    assert isinstance(instance, r1_ExpressionDef)



@given(instance=r1_ExpressionDef_strategy)
def test_r1_expressiondef_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=r1_ExpressionDef_strategy)
def test_r1_expressiondef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original



@given(instance=r1_ExpressionDef_strategy)
def test_r1_expressiondef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_CaseItem_strategy)
@settings(max_examples=50)
def test_r1_caseitem_instantiation(instance):
    assert isinstance(instance, r1_CaseItem)

@given(instance=r1_TypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1_typespecifier_instantiation(instance):
    assert isinstance(instance, r1_TypeSpecifier)

@given(instance=r1_AliasedQuerySource_strategy)
@settings(max_examples=50)
def test_r1_aliasedquerysource_instantiation(instance):
    assert isinstance(instance, r1_AliasedQuerySource)



@given(instance=r1_AliasedQuerySource_strategy)
def test_r1_aliasedquerysource_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=r1_Expression_strategy)
@settings(max_examples=50)
def test_r1_expression_instantiation(instance):
    assert isinstance(instance, r1_Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=r1_If_strategy)
@settings(max_examples=50)
def test_r1_if_instantiation(instance):
    assert isinstance(instance, r1_If)

@given(instance=r1_Current_strategy)
@settings(max_examples=50)
def test_r1_current_instantiation(instance):
    assert isinstance(instance, r1_Current)



@given(instance=r1_Current_strategy)
def test_r1_current_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1_InCodeSystem_strategy)
@settings(max_examples=50)
def test_r1_incodesystem_instantiation(instance):
    assert isinstance(instance, r1_InCodeSystem)

@given(instance=r1_Concept_strategy)
@settings(max_examples=50)
def test_r1_concept_instantiation(instance):
    assert isinstance(instance, r1_Concept)



@given(instance=r1_Concept_strategy)
def test_r1_concept_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original

@given(instance=r1_Case_strategy)
@settings(max_examples=50)
def test_r1_case_instantiation(instance):
    assert isinstance(instance, r1_Case)

@given(instance=r1_AliasRef_strategy)
@settings(max_examples=50)
def test_r1_aliasref_instantiation(instance):
    assert isinstance(instance, r1_AliasRef)



@given(instance=r1_AliasRef_strategy)
def test_r1_aliasref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_Instance_strategy)
@settings(max_examples=50)
def test_r1_instance_instantiation(instance):
    assert isinstance(instance, r1_Instance)



@given(instance=r1_Instance_strategy)
def test_r1_instance_classType_setter(instance):
    original = instance.classType
    instance.classType = original
    assert instance.classType == original

@given(instance=r1_IdentifierRef_strategy)
@settings(max_examples=50)
def test_r1_identifierref_instantiation(instance):
    assert isinstance(instance, r1_IdentifierRef)



@given(instance=r1_IdentifierRef_strategy)
def test_r1_identifierref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original



@given(instance=r1_IdentifierRef_strategy)
def test_r1_identifierref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_Interval_strategy)
@settings(max_examples=50)
def test_r1_interval_instantiation(instance):
    assert isinstance(instance, r1_Interval)



@given(instance=r1_Interval_strategy)
def test_r1_interval_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original



@given(instance=r1_Interval_strategy)
def test_r1_interval_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r1_ForEach_strategy)
@settings(max_examples=50)
def test_r1_foreach_instantiation(instance):
    assert isinstance(instance, r1_ForEach)



@given(instance=r1_ForEach_strategy)
def test_r1_foreach_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1_Filter_strategy)
@settings(max_examples=50)
def test_r1_filter_instantiation(instance):
    assert isinstance(instance, r1_Filter)



@given(instance=r1_Filter_strategy)
def test_r1_filter_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=r1_First_strategy)
@settings(max_examples=50)
def test_r1_first_instantiation(instance):
    assert isinstance(instance, r1_First)



@given(instance=r1_First_strategy)
def test_r1_first_orderBy_setter(instance):
    original = instance.orderBy
    instance.orderBy = original
    assert instance.orderBy == original

@given(instance=r1_Code_strategy)
@settings(max_examples=50)
def test_r1_code_instantiation(instance):
    assert isinstance(instance, r1_Code)



@given(instance=r1_Code_strategy)
def test_r1_code_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original



@given(instance=r1_Code_strategy)
def test_r1_code_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=r1_ExpressionRef_strategy)
@settings(max_examples=50)
def test_r1_expressionref_instantiation(instance):
    assert isinstance(instance, r1_ExpressionRef)



@given(instance=r1_ExpressionRef_strategy)
def test_r1_expressionref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=r1_ExpressionRef_strategy)
def test_r1_expressionref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1_DateTime_strategy)
@settings(max_examples=50)
def test_r1_datetime_instantiation(instance):
    assert isinstance(instance, r1_DateTime)

@given(instance=r1_CodeSystemRef_strategy)
@settings(max_examples=50)
def test_r1_codesystemref_instantiation(instance):
    assert isinstance(instance, r1_CodeSystemRef)



@given(instance=r1_CodeSystemRef_strategy)
def test_r1_codesystemref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=r1_CodeSystemRef_strategy)
def test_r1_codesystemref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=r1_BinaryExpression_strategy)
@settings(max_examples=50)
def test_r1_binaryexpression_instantiation(instance):
    assert isinstance(instance, r1_BinaryExpression)

@given(instance=r1_Combine_strategy)
@settings(max_examples=50)
def test_r1_combine_instantiation(instance):
    assert isinstance(instance, r1_Combine)

@given(instance=r1_IndexOf_strategy)
@settings(max_examples=50)
def test_r1_indexof_instantiation(instance):
    assert isinstance(instance, r1_IndexOf)

@given(instance=r1_AggregateExpression_strategy)
@settings(max_examples=50)
def test_r1_aggregateexpression_instantiation(instance):
    assert isinstance(instance, r1_AggregateExpression)



@given(instance=r1_AggregateExpression_strategy)
def test_r1_aggregateexpression_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=r1_Divide_strategy)
@settings(max_examples=50)
def test_r1_divide_instantiation(instance):
    assert isinstance(instance, r1_Divide)

@given(instance=r1_After_strategy)
@settings(max_examples=50)
def test_r1_after_instantiation(instance):
    assert isinstance(instance, r1_After)



@given(instance=r1_After_strategy)
def test_r1_after_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Indexer_strategy)
@settings(max_examples=50)
def test_r1_indexer_instantiation(instance):
    assert isinstance(instance, r1_Indexer)

@given(instance=r1_GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_r1_greaterorequal_instantiation(instance):
    assert isinstance(instance, r1_GreaterOrEqual)

@given(instance=r1_Contains_strategy)
@settings(max_examples=50)
def test_r1_contains_instantiation(instance):
    assert isinstance(instance, r1_Contains)



@given(instance=r1_Contains_strategy)
def test_r1_contains_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Before_strategy)
@settings(max_examples=50)
def test_r1_before_instantiation(instance):
    assert isinstance(instance, r1_Before)



@given(instance=r1_Before_strategy)
def test_r1_before_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_And_strategy)
@settings(max_examples=50)
def test_r1_and_instantiation(instance):
    assert isinstance(instance, r1_And)

@given(instance=r1_DifferenceBetween_strategy)
@settings(max_examples=50)
def test_r1_differencebetween_instantiation(instance):
    assert isinstance(instance, r1_DifferenceBetween)



@given(instance=r1_DifferenceBetween_strategy)
def test_r1_differencebetween_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Except_strategy)
@settings(max_examples=50)
def test_r1_except_instantiation(instance):
    assert isinstance(instance, r1_Except)

@given(instance=r1_DurationBetween_strategy)
@settings(max_examples=50)
def test_r1_durationbetween_instantiation(instance):
    assert isinstance(instance, r1_DurationBetween)



@given(instance=r1_DurationBetween_strategy)
def test_r1_durationbetween_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Includes_strategy)
@settings(max_examples=50)
def test_r1_includes_instantiation(instance):
    assert isinstance(instance, r1_Includes)



@given(instance=r1_Includes_strategy)
def test_r1_includes_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_IncludedIn_strategy)
@settings(max_examples=50)
def test_r1_includedin_instantiation(instance):
    assert isinstance(instance, r1_IncludedIn)



@given(instance=r1_IncludedIn_strategy)
def test_r1_includedin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_CalculateAgeAt_strategy)
@settings(max_examples=50)
def test_r1_calculateageat_instantiation(instance):
    assert isinstance(instance, r1_CalculateAgeAt)



@given(instance=r1_CalculateAgeAt_strategy)
def test_r1_calculateageat_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_In_strategy)
@settings(max_examples=50)
def test_r1_in_instantiation(instance):
    assert isinstance(instance, r1_In)



@given(instance=r1_In_strategy)
def test_r1_in_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Equal_strategy)
@settings(max_examples=50)
def test_r1_equal_instantiation(instance):
    assert isinstance(instance, r1_Equal)

@given(instance=r1_Ends_strategy)
@settings(max_examples=50)
def test_r1_ends_instantiation(instance):
    assert isinstance(instance, r1_Ends)



@given(instance=r1_Ends_strategy)
def test_r1_ends_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Intersect_strategy)
@settings(max_examples=50)
def test_r1_intersect_instantiation(instance):
    assert isinstance(instance, r1_Intersect)

@given(instance=r1_Greater_strategy)
@settings(max_examples=50)
def test_r1_greater_instantiation(instance):
    assert isinstance(instance, r1_Greater)

@given(instance=r1_Add_strategy)
@settings(max_examples=50)
def test_r1_add_instantiation(instance):
    assert isinstance(instance, r1_Add)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=r1_CalculateAge_strategy)
@settings(max_examples=50)
def test_r1_calculateage_instantiation(instance):
    assert isinstance(instance, r1_CalculateAge)



@given(instance=r1_CalculateAge_strategy)
def test_r1_calculateage_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Floor_strategy)
@settings(max_examples=50)
def test_r1_floor_instantiation(instance):
    assert isinstance(instance, r1_Floor)

@given(instance=r1_Convert_strategy)
@settings(max_examples=50)
def test_r1_convert_instantiation(instance):
    assert isinstance(instance, r1_Convert)



@given(instance=r1_Convert_strategy)
def test_r1_convert_toType_setter(instance):
    original = instance.toType
    instance.toType = original
    assert instance.toType == original

@given(instance=r1_End_strategy)
@settings(max_examples=50)
def test_r1_end_instantiation(instance):
    assert isinstance(instance, r1_End)

@given(instance=r1_DateTimeComponentFrom_strategy)
@settings(max_examples=50)
def test_r1_datetimecomponentfrom_instantiation(instance):
    assert isinstance(instance, r1_DateTimeComponentFrom)



@given(instance=r1_DateTimeComponentFrom_strategy)
def test_r1_datetimecomponentfrom_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Distinct_strategy)
@settings(max_examples=50)
def test_r1_distinct_instantiation(instance):
    assert isinstance(instance, r1_Distinct)

@given(instance=r1_Collapse_strategy)
@settings(max_examples=50)
def test_r1_collapse_instantiation(instance):
    assert isinstance(instance, r1_Collapse)

@given(instance=r1_As_strategy)
@settings(max_examples=50)
def test_r1_as_instantiation(instance):
    assert isinstance(instance, r1_As)



@given(instance=r1_As_strategy)
def test_r1_as_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original



@given(instance=r1_As_strategy)
def test_r1_as_asType_setter(instance):
    original = instance.asType
    instance.asType = original
    assert instance.asType == original

@given(instance=r1_Expand_strategy)
@settings(max_examples=50)
def test_r1_expand_instantiation(instance):
    assert isinstance(instance, r1_Expand)

@given(instance=r1_Ceiling_strategy)
@settings(max_examples=50)
def test_r1_ceiling_instantiation(instance):
    assert isinstance(instance, r1_Ceiling)

@given(instance=r1_Exists_strategy)
@settings(max_examples=50)
def test_r1_exists_instantiation(instance):
    assert isinstance(instance, r1_Exists)

@given(instance=r1_DateFrom_strategy)
@settings(max_examples=50)
def test_r1_datefrom_instantiation(instance):
    assert isinstance(instance, r1_DateFrom)

@given(instance=r1_Abs_strategy)
@settings(max_examples=50)
def test_r1_abs_instantiation(instance):
    assert isinstance(instance, r1_Abs)

@given(instance=r1_Xor_strategy)
@settings(max_examples=50)
def test_r1_xor_instantiation(instance):
    assert isinstance(instance, r1_Xor)

@given(instance=RelationshipClause_strategy)
@settings(max_examples=50)
def test_relationshipclause_instantiation(instance):
    assert isinstance(instance, RelationshipClause)

@given(instance=r1_Without_strategy)
@settings(max_examples=50)
def test_r1_without_instantiation(instance):
    assert isinstance(instance, r1_Without)

@given(instance=r1_With_strategy)
@settings(max_examples=50)
def test_r1_with_instantiation(instance):
    assert isinstance(instance, r1_With)

@given(instance=r1_Width_strategy)
@settings(max_examples=50)
def test_r1_width_instantiation(instance):
    assert isinstance(instance, r1_Width)

@given(instance=r1_Variance_strategy)
@settings(max_examples=50)
def test_r1_variance_instantiation(instance):
    assert isinstance(instance, r1_Variance)

@given(instance=r1_Upper_strategy)
@settings(max_examples=50)
def test_r1_upper_instantiation(instance):
    assert isinstance(instance, r1_Upper)

@given(instance=r1_Union_strategy)
@settings(max_examples=50)
def test_r1_union_instantiation(instance):
    assert isinstance(instance, r1_Union)

@given(instance=r1_UnaryExpression_strategy)
@settings(max_examples=50)
def test_r1_unaryexpression_instantiation(instance):
    assert isinstance(instance, r1_UnaryExpression)

@given(instance=r1_TupleElementDefinition_strategy)
@settings(max_examples=50)
def test_r1_tupleelementdefinition_instantiation(instance):
    assert isinstance(instance, r1_TupleElementDefinition)



@given(instance=r1_TupleElementDefinition_strategy)
def test_r1_tupleelementdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_ValueSetDef_strategy)
@settings(max_examples=50)
def test_r1_valuesetdef_instantiation(instance):
    assert isinstance(instance, r1_ValueSetDef)



@given(instance=r1_ValueSetDef_strategy)
def test_r1_valuesetdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original



@given(instance=r1_ValueSetDef_strategy)
def test_r1_valuesetdef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=r1_ValueSetDef_strategy)
def test_r1_valuesetdef_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=r1_ValueSetDef_strategy)
def test_r1_valuesetdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_TupleElement_strategy)
@settings(max_examples=50)
def test_r1_tupleelement_instantiation(instance):
    assert isinstance(instance, r1_TupleElement)



@given(instance=r1_TupleElement_strategy)
def test_r1_tupleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_Tuple_strategy)
@settings(max_examples=50)
def test_r1_tuple_instantiation(instance):
    assert isinstance(instance, r1_Tuple)

@given(instance=r1_TruncatedDivide_strategy)
@settings(max_examples=50)
def test_r1_truncateddivide_instantiation(instance):
    assert isinstance(instance, r1_TruncatedDivide)

@given(instance=r1_Truncate_strategy)
@settings(max_examples=50)
def test_r1_truncate_instantiation(instance):
    assert isinstance(instance, r1_Truncate)

@given(instance=r1_Today_strategy)
@settings(max_examples=50)
def test_r1_today_instantiation(instance):
    assert isinstance(instance, r1_Today)

@given(instance=r1_TimezoneFrom_strategy)
@settings(max_examples=50)
def test_r1_timezonefrom_instantiation(instance):
    assert isinstance(instance, r1_TimezoneFrom)

@given(instance=r1_Times_strategy)
@settings(max_examples=50)
def test_r1_times_instantiation(instance):
    assert isinstance(instance, r1_Times)

@given(instance=r1_TimeOfDay_strategy)
@settings(max_examples=50)
def test_r1_timeofday_instantiation(instance):
    assert isinstance(instance, r1_TimeOfDay)

@given(instance=r1_TimeFrom_strategy)
@settings(max_examples=50)
def test_r1_timefrom_instantiation(instance):
    assert isinstance(instance, r1_TimeFrom)

@given(instance=r1_Time_strategy)
@settings(max_examples=50)
def test_r1_time_instantiation(instance):
    assert isinstance(instance, r1_Time)

@given(instance=r1_TernaryExpression_strategy)
@settings(max_examples=50)
def test_r1_ternaryexpression_instantiation(instance):
    assert isinstance(instance, r1_TernaryExpression)

@given(instance=r1_Sum_strategy)
@settings(max_examples=50)
def test_r1_sum_instantiation(instance):
    assert isinstance(instance, r1_Sum)

@given(instance=r1_Successor_strategy)
@settings(max_examples=50)
def test_r1_successor_instantiation(instance):
    assert isinstance(instance, r1_Successor)

@given(instance=r1_Subtract_strategy)
@settings(max_examples=50)
def test_r1_subtract_instantiation(instance):
    assert isinstance(instance, r1_Subtract)

@given(instance=r1_StdDev_strategy)
@settings(max_examples=50)
def test_r1_stddev_instantiation(instance):
    assert isinstance(instance, r1_StdDev)

@given(instance=r1_Starts_strategy)
@settings(max_examples=50)
def test_r1_starts_instantiation(instance):
    assert isinstance(instance, r1_Starts)



@given(instance=r1_Starts_strategy)
def test_r1_starts_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Start_strategy)
@settings(max_examples=50)
def test_r1_start_instantiation(instance):
    assert isinstance(instance, r1_Start)

@given(instance=r1_Split_strategy)
@settings(max_examples=50)
def test_r1_split_instantiation(instance):
    assert isinstance(instance, r1_Split)

@given(instance=r1_Substring_strategy)
@settings(max_examples=50)
def test_r1_substring_instantiation(instance):
    assert isinstance(instance, r1_Substring)

@given(instance=r1_SortByItem_strategy)
@settings(max_examples=50)
def test_r1_sortbyitem_instantiation(instance):
    assert isinstance(instance, r1_SortByItem)



@given(instance=r1_SortByItem_strategy)
def test_r1_sortbyitem_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=r1_Sort_strategy)
@settings(max_examples=50)
def test_r1_sort_instantiation(instance):
    assert isinstance(instance, r1_Sort)

@given(instance=r1_SingletonFrom_strategy)
@settings(max_examples=50)
def test_r1_singletonfrom_instantiation(instance):
    assert isinstance(instance, r1_SingletonFrom)

@given(instance=r1_SameOrBefore_strategy)
@settings(max_examples=50)
def test_r1_sameorbefore_instantiation(instance):
    assert isinstance(instance, r1_SameOrBefore)



@given(instance=r1_SameOrBefore_strategy)
def test_r1_sameorbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_SameOrAfter_strategy)
@settings(max_examples=50)
def test_r1_sameorafter_instantiation(instance):
    assert isinstance(instance, r1_SameOrAfter)



@given(instance=r1_SameOrAfter_strategy)
def test_r1_sameorafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_SameAs_strategy)
@settings(max_examples=50)
def test_r1_sameas_instantiation(instance):
    assert isinstance(instance, r1_SameAs)



@given(instance=r1_SameAs_strategy)
def test_r1_sameas_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Round_strategy)
@settings(max_examples=50)
def test_r1_round_instantiation(instance):
    assert isinstance(instance, r1_Round)

@given(instance=r1_Retrieve_strategy)
@settings(max_examples=50)
def test_r1_retrieve_instantiation(instance):
    assert isinstance(instance, r1_Retrieve)



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_idProperty_setter(instance):
    original = instance.idProperty
    instance.idProperty = original
    assert instance.idProperty == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_dateProperty_setter(instance):
    original = instance.dateProperty
    instance.dateProperty = original
    assert instance.dateProperty == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_dateHighProperty_setter(instance):
    original = instance.dateHighProperty
    instance.dateHighProperty = original
    assert instance.dateHighProperty == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_codeProperty_setter(instance):
    original = instance.codeProperty
    instance.codeProperty = original
    assert instance.codeProperty == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_dateLowProperty_setter(instance):
    original = instance.dateLowProperty
    instance.dateLowProperty = original
    assert instance.dateLowProperty == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_templateId_setter(instance):
    original = instance.templateId
    instance.templateId = original
    assert instance.templateId == original



@given(instance=r1_Retrieve_strategy)
def test_r1_retrieve_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=AliasedQuerySource_strategy)
@settings(max_examples=50)
def test_aliasedquerysource_instantiation(instance):
    assert isinstance(instance, AliasedQuerySource)

@given(instance=r1_QueryDefineRef_strategy)
@settings(max_examples=50)
def test_r1_querydefineref_instantiation(instance):
    assert isinstance(instance, r1_QueryDefineRef)



@given(instance=r1_QueryDefineRef_strategy)
def test_r1_querydefineref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_SortClause_strategy)
@settings(max_examples=50)
def test_r1_sortclause_instantiation(instance):
    assert isinstance(instance, r1_SortClause)

@given(instance=r1_ReturnClause_strategy)
@settings(max_examples=50)
def test_r1_returnclause_instantiation(instance):
    assert isinstance(instance, r1_ReturnClause)



@given(instance=r1_ReturnClause_strategy)
def test_r1_returnclause_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=r1_RelationshipClause_strategy)
@settings(max_examples=50)
def test_r1_relationshipclause_instantiation(instance):
    assert isinstance(instance, r1_RelationshipClause)

@given(instance=r1_Query_strategy)
@settings(max_examples=50)
def test_r1_query_instantiation(instance):
    assert isinstance(instance, r1_Query)

@given(instance=r1_Quantity_strategy)
@settings(max_examples=50)
def test_r1_quantity_instantiation(instance):
    assert isinstance(instance, r1_Quantity)



@given(instance=r1_Quantity_strategy)
def test_r1_quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=r1_Quantity_strategy)
def test_r1_quantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=r1_Property_strategy)
@settings(max_examples=50)
def test_r1_property_instantiation(instance):
    assert isinstance(instance, r1_Property)



@given(instance=r1_Property_strategy)
def test_r1_property_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=r1_Property_strategy)
def test_r1_property_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=r1_ProperIncludes_strategy)
@settings(max_examples=50)
def test_r1_properincludes_instantiation(instance):
    assert isinstance(instance, r1_ProperIncludes)



@given(instance=r1_ProperIncludes_strategy)
def test_r1_properincludes_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_ProperIncludedIn_strategy)
@settings(max_examples=50)
def test_r1_properincludedin_instantiation(instance):
    assert isinstance(instance, r1_ProperIncludedIn)



@given(instance=r1_ProperIncludedIn_strategy)
def test_r1_properincludedin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_ProperContains_strategy)
@settings(max_examples=50)
def test_r1_propercontains_instantiation(instance):
    assert isinstance(instance, r1_ProperContains)



@given(instance=r1_ProperContains_strategy)
def test_r1_propercontains_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Predecessor_strategy)
@settings(max_examples=50)
def test_r1_predecessor_instantiation(instance):
    assert isinstance(instance, r1_Predecessor)

@given(instance=r1_Power_strategy)
@settings(max_examples=50)
def test_r1_power_instantiation(instance):
    assert isinstance(instance, r1_Power)

@given(instance=r1_PositionOf_strategy)
@settings(max_examples=50)
def test_r1_positionof_instantiation(instance):
    assert isinstance(instance, r1_PositionOf)

@given(instance=r1_PopulationVariance_strategy)
@settings(max_examples=50)
def test_r1_populationvariance_instantiation(instance):
    assert isinstance(instance, r1_PopulationVariance)

@given(instance=r1_PopulationStdDev_strategy)
@settings(max_examples=50)
def test_r1_populationstddev_instantiation(instance):
    assert isinstance(instance, r1_PopulationStdDev)

@given(instance=r1_ProperIn_strategy)
@settings(max_examples=50)
def test_r1_properin_instantiation(instance):
    assert isinstance(instance, r1_ProperIn)



@given(instance=r1_ProperIn_strategy)
def test_r1_properin_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_ParameterDef_strategy)
@settings(max_examples=50)
def test_r1_parameterdef_instantiation(instance):
    assert isinstance(instance, r1_ParameterDef)



@given(instance=r1_ParameterDef_strategy)
def test_r1_parameterdef_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original



@given(instance=r1_ParameterDef_strategy)
def test_r1_parameterdef_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original



@given(instance=r1_ParameterDef_strategy)
def test_r1_parameterdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_OverlapsBefore_strategy)
@settings(max_examples=50)
def test_r1_overlapsbefore_instantiation(instance):
    assert isinstance(instance, r1_OverlapsBefore)



@given(instance=r1_OverlapsBefore_strategy)
def test_r1_overlapsbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_OverlapsAfter_strategy)
@settings(max_examples=50)
def test_r1_overlapsafter_instantiation(instance):
    assert isinstance(instance, r1_OverlapsAfter)



@given(instance=r1_OverlapsAfter_strategy)
def test_r1_overlapsafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Overlaps_strategy)
@settings(max_examples=50)
def test_r1_overlaps_instantiation(instance):
    assert isinstance(instance, r1_Overlaps)



@given(instance=r1_Overlaps_strategy)
def test_r1_overlaps_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Or_strategy)
@settings(max_examples=50)
def test_r1_or_instantiation(instance):
    assert isinstance(instance, r1_Or)

@given(instance=r1_ParameterRef_strategy)
@settings(max_examples=50)
def test_r1_parameterref_instantiation(instance):
    assert isinstance(instance, r1_ParameterRef)



@given(instance=r1_ParameterRef_strategy)
def test_r1_parameterref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original



@given(instance=r1_ParameterRef_strategy)
def test_r1_parameterref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_Null_strategy)
@settings(max_examples=50)
def test_r1_null_instantiation(instance):
    assert isinstance(instance, r1_Null)



@given(instance=r1_Null_strategy)
def test_r1_null_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1_Now_strategy)
@settings(max_examples=50)
def test_r1_now_instantiation(instance):
    assert isinstance(instance, r1_Now)

@given(instance=r1_NotEqual_strategy)
@settings(max_examples=50)
def test_r1_notequal_instantiation(instance):
    assert isinstance(instance, r1_NotEqual)

@given(instance=r1_Not_strategy)
@settings(max_examples=50)
def test_r1_not_instantiation(instance):
    assert isinstance(instance, r1_Not)

@given(instance=r1_Negate_strategy)
@settings(max_examples=50)
def test_r1_negate_instantiation(instance):
    assert isinstance(instance, r1_Negate)

@given(instance=r1_OperandRef_strategy)
@settings(max_examples=50)
def test_r1_operandref_instantiation(instance):
    assert isinstance(instance, r1_OperandRef)



@given(instance=r1_OperandRef_strategy)
def test_r1_operandref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_Multiply_strategy)
@settings(max_examples=50)
def test_r1_multiply_instantiation(instance):
    assert isinstance(instance, r1_Multiply)

@given(instance=r1_Modulo_strategy)
@settings(max_examples=50)
def test_r1_modulo_instantiation(instance):
    assert isinstance(instance, r1_Modulo)

@given(instance=r1_Mode_strategy)
@settings(max_examples=50)
def test_r1_mode_instantiation(instance):
    assert isinstance(instance, r1_Mode)

@given(instance=r1_MinValue_strategy)
@settings(max_examples=50)
def test_r1_minvalue_instantiation(instance):
    assert isinstance(instance, r1_MinValue)



@given(instance=r1_MinValue_strategy)
def test_r1_minvalue_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1_Min_strategy)
@settings(max_examples=50)
def test_r1_min_instantiation(instance):
    assert isinstance(instance, r1_Min)

@given(instance=r1_MeetsBefore_strategy)
@settings(max_examples=50)
def test_r1_meetsbefore_instantiation(instance):
    assert isinstance(instance, r1_MeetsBefore)



@given(instance=r1_MeetsBefore_strategy)
def test_r1_meetsbefore_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_MeetsAfter_strategy)
@settings(max_examples=50)
def test_r1_meetsafter_instantiation(instance):
    assert isinstance(instance, r1_MeetsAfter)



@given(instance=r1_MeetsAfter_strategy)
def test_r1_meetsafter_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_NaryExpression_strategy)
@settings(max_examples=50)
def test_r1_naryexpression_instantiation(instance):
    assert isinstance(instance, r1_NaryExpression)

@given(instance=r1_MaxValue_strategy)
@settings(max_examples=50)
def test_r1_maxvalue_instantiation(instance):
    assert isinstance(instance, r1_MaxValue)



@given(instance=r1_MaxValue_strategy)
def test_r1_maxvalue_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=r1_Max_strategy)
@settings(max_examples=50)
def test_r1_max_instantiation(instance):
    assert isinstance(instance, r1_Max)

@given(instance=r1_Matches_strategy)
@settings(max_examples=50)
def test_r1_matches_instantiation(instance):
    assert isinstance(instance, r1_Matches)

@given(instance=r1_Lower_strategy)
@settings(max_examples=50)
def test_r1_lower_instantiation(instance):
    assert isinstance(instance, r1_Lower)

@given(instance=r1_Log_strategy)
@settings(max_examples=50)
def test_r1_log_instantiation(instance):
    assert isinstance(instance, r1_Log)

@given(instance=r1_Ln_strategy)
@settings(max_examples=50)
def test_r1_ln_instantiation(instance):
    assert isinstance(instance, r1_Ln)

@given(instance=r1_Literal_strategy)
@settings(max_examples=50)
def test_r1_literal_instantiation(instance):
    assert isinstance(instance, r1_Literal)



@given(instance=r1_Literal_strategy)
def test_r1_literal_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original



@given(instance=r1_Literal_strategy)
def test_r1_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r1_Meets_strategy)
@settings(max_examples=50)
def test_r1_meets_instantiation(instance):
    assert isinstance(instance, r1_Meets)



@given(instance=r1_Meets_strategy)
def test_r1_meets_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=r1_Median_strategy)
@settings(max_examples=50)
def test_r1_median_instantiation(instance):
    assert isinstance(instance, r1_Median)

@given(instance=r1_List_strategy)
@settings(max_examples=50)
def test_r1_list_instantiation(instance):
    assert isinstance(instance, r1_List)

@given(instance=r1_LessOrEqual_strategy)
@settings(max_examples=50)
def test_r1_lessorequal_instantiation(instance):
    assert isinstance(instance, r1_LessOrEqual)

@given(instance=r1_Less_strategy)
@settings(max_examples=50)
def test_r1_less_instantiation(instance):
    assert isinstance(instance, r1_Less)

@given(instance=r1_Length_strategy)
@settings(max_examples=50)
def test_r1_length_instantiation(instance):
    assert isinstance(instance, r1_Length)

@given(instance=r1_Last_strategy)
@settings(max_examples=50)
def test_r1_last_instantiation(instance):
    assert isinstance(instance, r1_Last)



@given(instance=r1_Last_strategy)
def test_r1_last_orderBy_setter(instance):
    original = instance.orderBy
    instance.orderBy = original
    assert instance.orderBy == original

@given(instance=r1_IsTrue_strategy)
@settings(max_examples=50)
def test_r1_istrue_instantiation(instance):
    assert isinstance(instance, r1_IsTrue)

@given(instance=r1_IsNull_strategy)
@settings(max_examples=50)
def test_r1_isnull_instantiation(instance):
    assert isinstance(instance, r1_IsNull)

@given(instance=r1_Is_strategy)
@settings(max_examples=50)
def test_r1_is_instantiation(instance):
    assert isinstance(instance, r1_Is)



@given(instance=r1_Is_strategy)
def test_r1_is_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original

@given(instance=r1_ValueSetRef_strategy)
@settings(max_examples=50)
def test_r1_valuesetref_instantiation(instance):
    assert isinstance(instance, r1_ValueSetRef)



@given(instance=r1_ValueSetRef_strategy)
def test_r1_valuesetref_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original



@given(instance=r1_ValueSetRef_strategy)
def test_r1_valuesetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_InValueSet_strategy)
@settings(max_examples=50)
def test_r1_invalueset_instantiation(instance):
    assert isinstance(instance, r1_InValueSet)

@given(instance=TypeSpecifier_strategy)
@settings(max_examples=50)
def test_typespecifier_instantiation(instance):
    assert isinstance(instance, TypeSpecifier)

@given(instance=r1_NamedTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1_namedtypespecifier_instantiation(instance):
    assert isinstance(instance, r1_NamedTypeSpecifier)



@given(instance=r1_NamedTypeSpecifier_strategy)
def test_r1_namedtypespecifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=r1_TupleTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1_tupletypespecifier_instantiation(instance):
    assert isinstance(instance, r1_TupleTypeSpecifier)

@given(instance=r1_ListTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1_listtypespecifier_instantiation(instance):
    assert isinstance(instance, r1_ListTypeSpecifier)

@given(instance=r1_IntervalTypeSpecifier_strategy)
@settings(max_examples=50)
def test_r1_intervaltypespecifier_instantiation(instance):
    assert isinstance(instance, r1_IntervalTypeSpecifier)

@given(instance=r1_IsFalse_strategy)
@settings(max_examples=50)
def test_r1_isfalse_instantiation(instance):
    assert isinstance(instance, r1_IsFalse)
