import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JoinEntity,
    FromRange,
    dom_InCollection,
    dom_InClass,
    dom_FromClass,
    Expression,
    dom_CollectionFunction,
    dom_AggregateFunction,
    dom_FunctionCall,
    dom_CastFunction,
    dom_JoinEntity,
    dom_InCollectionElements,
    dom_PropertyValue,
    dom_PropertyAssignment,
    SelectStatement,
    dom_SelectObject,
    dom_SelectClass,
    dom_SelectProperties,
    dom_SortOrderElement,
    dom_Join,
    dom_FromRange,
    dom_CallOutputParameter,
    dom_CallInputParameter,
    QlStatement,
    dom_InsertStatement,
    dom_UpdateStatement,
    dom_DeleteStatement,
    dom_SelectStatement,
    dom_CallableStatement,
    dom_Function,
    DaoFeature,
    dom_SqlType,
    dom_OneToOne,
    dom_ManyToOne,
    dom_Column,
    dom_DataBaseConstraint,
    dom_QlStatement,
    dom_QueryParameter,
    dom_ManyToMany,
    dom_OneToMany,
    dom_DaoFeature,
    dom_AttributeSortOrder,
    dom_ValidatorReference,
    dom_Constraint,
    dom_BoolLiteral,
    ExpressionFlag,
    dom_ReadOnlyFlag,
    dom_AvailableFlag,
    dom_RequiredFlag,
    dom_EqualityExpr,
    AttributeFlag,
    dom_TransientFlag,
    dom_DerivedFlag,
    dom_ExpressionFlag,
    AttributeProperty,
    dom_AttributeTextProperty,
    dom_AttributeValidationProperty,
    dom_BetweenExpression,
    dom_UnaryExpression,
    dom_MemberOfExpression,
    dom_LikeExpression,
    dom_InExpression,
    dom_NotExpression,
    dom_BinaryExpression,
    dom_AliasedExpression,
    dom_PresentableFeature,
    dom_WhenClause,
    LiteralValue,
    dom_RealLiteralValue,
    dom_IntegerLiteralValue,
    dom_EmptyLiteralValue,
    dom_NullLiteralValue,
    dom_BooleanLiteralValue,
    dom_LiteralValue,
    dom_ParenthesizedExpression,
    dom_SubQuery,
    dom_AltWhenClause,
    dom_StringLiteralValue,
    dom_TrimFunction,
    dom_CaseExpression,
    dom_QuantifiedExpression,
    dom_QueryParameterValue,
    dom_QueryParameterReference,
    dom_AttributeFlag,
    dom_IncrementerReference,
    dom_DataTypeAndTypeParameter,
    dom_PropertyMapping,
    dom_ConditionsBlock,
    PresentableFeature,
    ComplexType,
    dom_ValueObject,
    dom_AttributeProperty,
    dom_DataView,
    dom_Type,
    QueryParameterReference,
    QueryParameter,
    dom_Expression,
    dom_DaoOperation,
    dom_Dependant,
    Dependant,
    dom_Entity,
    dom_Parameter,
    DaoOperation,
    dom_SimpleType,
    IDocumentable,
    dom_FeatureReference,
    dom_AttributeGroup,
    dom_Operation,
    dom_QueryOperation,
    dom_DelegateOperation,
    ReferenceableByXmadslVariable,
    dom_IElementWithNoName,
    dom_Property,
    dom_Attribute,
    Type,
    ModelElement,
    dom_ApplicationSession,
    dom_Mapper,
    dom_Dao,
    dom_Service,
    dom_ComplexType,
    DataBaseConstraintType,
    CrudOperationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_dom_incollection_is_not_abstract():
    assert not inspect.isabstract(dom_InCollection)


def test_dom_incollection_constructor_exists():
    assert callable(dom_InCollection.__init__)


def test_dom_incollection_constructor_args():
    sig = inspect.signature(dom_InCollection.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "path" in params, "Missing parameter 'path'"

def test_dom_incollection_has_alias():
    assert hasattr(dom_InCollection, "alias")
    descriptor = None
    for klass in dom_InCollection.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_dom_incollection_has_path():
    assert hasattr(dom_InCollection, "path")
    descriptor = None
    for klass in dom_InCollection.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_dom_inclass_is_not_abstract():
    assert not inspect.isabstract(dom_InClass)


def test_dom_inclass_constructor_exists():
    assert callable(dom_InClass.__init__)


def test_dom_inclass_constructor_args():
    sig = inspect.signature(dom_InClass.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_inclass_has_class_():
    assert hasattr(dom_InClass, "class_")
    descriptor = None
    for klass in dom_InClass.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_dom_inclass_has_name():
    assert hasattr(dom_InClass, "name")
    descriptor = None
    for klass in dom_InClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_fromclass_is_not_abstract():
    assert not inspect.isabstract(dom_FromClass)


def test_dom_fromclass_constructor_exists():
    assert callable(dom_FromClass.__init__)


def test_dom_fromclass_constructor_args():
    sig = inspect.signature(dom_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "popertyFetch" in params, "Missing parameter 'popertyFetch'"

def test_dom_fromclass_has_popertyFetch():
    assert hasattr(dom_FromClass, "popertyFetch")
    descriptor = None
    for klass in dom_FromClass.__mro__:
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



def test_dom_collectionfunction_is_not_abstract():
    assert not inspect.isabstract(dom_CollectionFunction)


def test_dom_collectionfunction_constructor_exists():
    assert callable(dom_CollectionFunction.__init__)


def test_dom_collectionfunction_constructor_args():
    sig = inspect.signature(dom_CollectionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_dom_collectionfunction_has_function():
    assert hasattr(dom_CollectionFunction, "function")
    descriptor = None
    for klass in dom_CollectionFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom_aggregatefunction_is_not_abstract():
    assert not inspect.isabstract(dom_AggregateFunction)


def test_dom_aggregatefunction_constructor_exists():
    assert callable(dom_AggregateFunction.__init__)


def test_dom_aggregatefunction_constructor_args():
    sig = inspect.signature(dom_AggregateFunction.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "function" in params, "Missing parameter 'function'"
    assert "all" in params, "Missing parameter 'all'"

def test_dom_aggregatefunction_has_from_():
    assert hasattr(dom_AggregateFunction, "from_")
    descriptor = None
    for klass in dom_AggregateFunction.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_dom_aggregatefunction_has_distinct():
    assert hasattr(dom_AggregateFunction, "distinct")
    descriptor = None
    for klass in dom_AggregateFunction.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_dom_aggregatefunction_has_function():
    assert hasattr(dom_AggregateFunction, "function")
    descriptor = None
    for klass in dom_AggregateFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_dom_aggregatefunction_has_all():
    assert hasattr(dom_AggregateFunction, "all")
    descriptor = None
    for klass in dom_AggregateFunction.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_dom_functioncall_is_not_abstract():
    assert not inspect.isabstract(dom_FunctionCall)


def test_dom_functioncall_constructor_exists():
    assert callable(dom_FunctionCall.__init__)


def test_dom_functioncall_constructor_args():
    sig = inspect.signature(dom_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_dom_functioncall_has_function():
    assert hasattr(dom_FunctionCall, "function")
    descriptor = None
    for klass in dom_FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_dom_castfunction_is_not_abstract():
    assert not inspect.isabstract(dom_CastFunction)


def test_dom_castfunction_constructor_exists():
    assert callable(dom_CastFunction.__init__)


def test_dom_castfunction_constructor_args():
    sig = inspect.signature(dom_CastFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_castfunction_has_function():
    assert hasattr(dom_CastFunction, "function")
    descriptor = None
    for klass in dom_CastFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_dom_castfunction_has_name():
    assert hasattr(dom_CastFunction, "name")
    descriptor = None
    for klass in dom_CastFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_joinentity_is_not_abstract():
    assert not inspect.isabstract(dom_JoinEntity)


def test_dom_joinentity_constructor_exists():
    assert callable(dom_JoinEntity.__init__)


def test_dom_joinentity_constructor_args():
    sig = inspect.signature(dom_JoinEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_joinentity_has_name():
    assert hasattr(dom_JoinEntity, "name")
    descriptor = None
    for klass in dom_JoinEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_incollectionelements_is_not_abstract():
    assert not inspect.isabstract(dom_InCollectionElements)


def test_dom_incollectionelements_constructor_exists():
    assert callable(dom_InCollectionElements.__init__)


def test_dom_incollectionelements_constructor_args():
    sig = inspect.signature(dom_InCollectionElements.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_incollectionelements_has_reference():
    assert hasattr(dom_InCollectionElements, "reference")
    descriptor = None
    for klass in dom_InCollectionElements.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_dom_incollectionelements_has_name():
    assert hasattr(dom_InCollectionElements, "name")
    descriptor = None
    for klass in dom_InCollectionElements.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyValue)


def test_dom_propertyvalue_constructor_exists():
    assert callable(dom_PropertyValue.__init__)


def test_dom_propertyvalue_constructor_args():
    sig = inspect.signature(dom_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "classProperty" in params, "Missing parameter 'classProperty'"
    assert "segments" in params, "Missing parameter 'segments'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_propertyvalue_has_classProperty():
    assert hasattr(dom_PropertyValue, "classProperty")
    descriptor = None
    for klass in dom_PropertyValue.__mro__:
        if "classProperty" in klass.__dict__:
            descriptor = klass.__dict__["classProperty"]
            break
    assert isinstance(descriptor, property)

def test_dom_propertyvalue_has_segments():
    assert hasattr(dom_PropertyValue, "segments")
    descriptor = None
    for klass in dom_PropertyValue.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)

def test_dom_propertyvalue_has_name():
    assert hasattr(dom_PropertyValue, "name")
    descriptor = None
    for klass in dom_PropertyValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyAssignment)


def test_dom_propertyassignment_constructor_exists():
    assert callable(dom_PropertyAssignment.__init__)


def test_dom_propertyassignment_constructor_args():
    sig = inspect.signature(dom_PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_selectobject_is_not_abstract():
    assert not inspect.isabstract(dom_SelectObject)


def test_dom_selectobject_constructor_exists():
    assert callable(dom_SelectObject.__init__)


def test_dom_selectobject_constructor_args():
    sig = inspect.signature(dom_SelectObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_selectobject_has_name():
    assert hasattr(dom_SelectObject, "name")
    descriptor = None
    for klass in dom_SelectObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_selectclass_is_not_abstract():
    assert not inspect.isabstract(dom_SelectClass)


def test_dom_selectclass_constructor_exists():
    assert callable(dom_SelectClass.__init__)


def test_dom_selectclass_constructor_args():
    sig = inspect.signature(dom_SelectClass.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_dom_selectclass_has_class_():
    assert hasattr(dom_SelectClass, "class_")
    descriptor = None
    for klass in dom_SelectClass.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dom_selectproperties_is_not_abstract():
    assert not inspect.isabstract(dom_SelectProperties)


def test_dom_selectproperties_constructor_exists():
    assert callable(dom_SelectProperties.__init__)


def test_dom_selectproperties_constructor_args():
    sig = inspect.signature(dom_SelectProperties.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_dom_selectproperties_has_distinct():
    assert hasattr(dom_SelectProperties, "distinct")
    descriptor = None
    for klass in dom_SelectProperties.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_dom_sortorderelement_is_not_abstract():
    assert not inspect.isabstract(dom_SortOrderElement)


def test_dom_sortorderelement_constructor_exists():
    assert callable(dom_SortOrderElement.__init__)


def test_dom_sortorderelement_constructor_args():
    sig = inspect.signature(dom_SortOrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "sortOrder" in params, "Missing parameter 'sortOrder'"

def test_dom_sortorderelement_has_sortOrder():
    assert hasattr(dom_SortOrderElement, "sortOrder")
    descriptor = None
    for klass in dom_SortOrderElement.__mro__:
        if "sortOrder" in klass.__dict__:
            descriptor = klass.__dict__["sortOrder"]
            break
    assert isinstance(descriptor, property)



def test_dom_join_is_not_abstract():
    assert not inspect.isabstract(dom_Join)


def test_dom_join_constructor_exists():
    assert callable(dom_Join.__init__)


def test_dom_join_constructor_args():
    sig = inspect.signature(dom_Join.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "propertyFetch" in params, "Missing parameter 'propertyFetch'"

def test_dom_join_has_type():
    assert hasattr(dom_Join, "type")
    descriptor = None
    for klass in dom_Join.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dom_join_has_fetch():
    assert hasattr(dom_Join, "fetch")
    descriptor = None
    for klass in dom_Join.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_dom_join_has_propertyFetch():
    assert hasattr(dom_Join, "propertyFetch")
    descriptor = None
    for klass in dom_Join.__mro__:
        if "propertyFetch" in klass.__dict__:
            descriptor = klass.__dict__["propertyFetch"]
            break
    assert isinstance(descriptor, property)



def test_dom_fromrange_is_not_abstract():
    assert not inspect.isabstract(dom_FromRange)


def test_dom_fromrange_constructor_exists():
    assert callable(dom_FromRange.__init__)


def test_dom_fromrange_constructor_args():
    sig = inspect.signature(dom_FromRange.__init__)
    params = list(sig.parameters.keys())



def test_dom_calloutputparameter_is_not_abstract():
    assert not inspect.isabstract(dom_CallOutputParameter)


def test_dom_calloutputparameter_constructor_exists():
    assert callable(dom_CallOutputParameter.__init__)


def test_dom_calloutputparameter_constructor_args():
    sig = inspect.signature(dom_CallOutputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_calloutputparameter_has_name():
    assert hasattr(dom_CallOutputParameter, "name")
    descriptor = None
    for klass in dom_CallOutputParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_callinputparameter_is_not_abstract():
    assert not inspect.isabstract(dom_CallInputParameter)


def test_dom_callinputparameter_constructor_exists():
    assert callable(dom_CallInputParameter.__init__)


def test_dom_callinputparameter_constructor_args():
    sig = inspect.signature(dom_CallInputParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_callinputparameter_has_name():
    assert hasattr(dom_CallInputParameter, "name")
    descriptor = None
    for klass in dom_CallInputParameter.__mro__:
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



def test_dom_insertstatement_is_not_abstract():
    assert not inspect.isabstract(dom_InsertStatement)


def test_dom_insertstatement_constructor_exists():
    assert callable(dom_InsertStatement.__init__)


def test_dom_insertstatement_constructor_args():
    sig = inspect.signature(dom_InsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_updatestatement_is_not_abstract():
    assert not inspect.isabstract(dom_UpdateStatement)


def test_dom_updatestatement_constructor_exists():
    assert callable(dom_UpdateStatement.__init__)


def test_dom_updatestatement_constructor_args():
    sig = inspect.signature(dom_UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "versioned" in params, "Missing parameter 'versioned'"

def test_dom_updatestatement_has_name():
    assert hasattr(dom_UpdateStatement, "name")
    descriptor = None
    for klass in dom_UpdateStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_updatestatement_has_versioned():
    assert hasattr(dom_UpdateStatement, "versioned")
    descriptor = None
    for klass in dom_UpdateStatement.__mro__:
        if "versioned" in klass.__dict__:
            descriptor = klass.__dict__["versioned"]
            break
    assert isinstance(descriptor, property)



def test_dom_deletestatement_is_not_abstract():
    assert not inspect.isabstract(dom_DeleteStatement)


def test_dom_deletestatement_constructor_exists():
    assert callable(dom_DeleteStatement.__init__)


def test_dom_deletestatement_constructor_args():
    sig = inspect.signature(dom_DeleteStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_deletestatement_has_name():
    assert hasattr(dom_DeleteStatement, "name")
    descriptor = None
    for klass in dom_DeleteStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_selectstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SelectStatement)


def test_dom_selectstatement_constructor_exists():
    assert callable(dom_SelectStatement.__init__)


def test_dom_selectstatement_constructor_args():
    sig = inspect.signature(dom_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_callablestatement_is_not_abstract():
    assert not inspect.isabstract(dom_CallableStatement)


def test_dom_callablestatement_constructor_exists():
    assert callable(dom_CallableStatement.__init__)


def test_dom_callablestatement_constructor_args():
    sig = inspect.signature(dom_CallableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "functionCall" in params, "Missing parameter 'functionCall'"

def test_dom_callablestatement_has_name():
    assert hasattr(dom_CallableStatement, "name")
    descriptor = None
    for klass in dom_CallableStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_callablestatement_has_functionCall():
    assert hasattr(dom_CallableStatement, "functionCall")
    descriptor = None
    for klass in dom_CallableStatement.__mro__:
        if "functionCall" in klass.__dict__:
            descriptor = klass.__dict__["functionCall"]
            break
    assert isinstance(descriptor, property)



def test_dom_function_is_not_abstract():
    assert not inspect.isabstract(dom_Function)


def test_dom_function_constructor_exists():
    assert callable(dom_Function.__init__)


def test_dom_function_constructor_args():
    sig = inspect.signature(dom_Function.__init__)
    params = list(sig.parameters.keys())



def test_daofeature_is_not_abstract():
    assert not inspect.isabstract(DaoFeature)


def test_daofeature_constructor_exists():
    assert callable(DaoFeature.__init__)


def test_daofeature_constructor_args():
    sig = inspect.signature(DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_dom_sqltype_is_not_abstract():
    assert not inspect.isabstract(dom_SqlType)


def test_dom_sqltype_constructor_exists():
    assert callable(dom_SqlType.__init__)


def test_dom_sqltype_constructor_args():
    sig = inspect.signature(dom_SqlType.__init__)
    params = list(sig.parameters.keys())



def test_dom_onetoone_is_not_abstract():
    assert not inspect.isabstract(dom_OneToOne)


def test_dom_onetoone_constructor_exists():
    assert callable(dom_OneToOne.__init__)


def test_dom_onetoone_constructor_args():
    sig = inspect.signature(dom_OneToOne.__init__)
    params = list(sig.parameters.keys())



def test_dom_manytoone_is_not_abstract():
    assert not inspect.isabstract(dom_ManyToOne)


def test_dom_manytoone_constructor_exists():
    assert callable(dom_ManyToOne.__init__)


def test_dom_manytoone_constructor_args():
    sig = inspect.signature(dom_ManyToOne.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_dom_manytoone_has_columnName():
    assert hasattr(dom_ManyToOne, "columnName")
    descriptor = None
    for klass in dom_ManyToOne.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dom_manytoone_has_derived():
    assert hasattr(dom_ManyToOne, "derived")
    descriptor = None
    for klass in dom_ManyToOne.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_dom_column_is_not_abstract():
    assert not inspect.isabstract(dom_Column)


def test_dom_column_constructor_exists():
    assert callable(dom_Column.__init__)


def test_dom_column_constructor_args():
    sig = inspect.signature(dom_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dom_column_has_columnName():
    assert hasattr(dom_Column, "columnName")
    descriptor = None
    for klass in dom_Column.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dom_databaseconstraint_is_not_abstract():
    assert not inspect.isabstract(dom_DataBaseConstraint)


def test_dom_databaseconstraint_constructor_exists():
    assert callable(dom_DataBaseConstraint.__init__)


def test_dom_databaseconstraint_constructor_args():
    sig = inspect.signature(dom_DataBaseConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_dom_databaseconstraint_has_name():
    assert hasattr(dom_DataBaseConstraint, "name")
    descriptor = None
    for klass in dom_DataBaseConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_databaseconstraint_has_type():
    assert hasattr(dom_DataBaseConstraint, "type")
    descriptor = None
    for klass in dom_DataBaseConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dom_qlstatement_is_not_abstract():
    assert not inspect.isabstract(dom_QlStatement)


def test_dom_qlstatement_constructor_exists():
    assert callable(dom_QlStatement.__init__)


def test_dom_qlstatement_constructor_args():
    sig = inspect.signature(dom_QlStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_queryparameter_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameter)


def test_dom_queryparameter_constructor_exists():
    assert callable(dom_QueryParameter.__init__)


def test_dom_queryparameter_constructor_args():
    sig = inspect.signature(dom_QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom_manytomany_is_not_abstract():
    assert not inspect.isabstract(dom_ManyToMany)


def test_dom_manytomany_constructor_exists():
    assert callable(dom_ManyToMany.__init__)


def test_dom_manytomany_constructor_args():
    sig = inspect.signature(dom_ManyToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "inverse" in params, "Missing parameter 'inverse'"

def test_dom_manytomany_has_columnName():
    assert hasattr(dom_ManyToMany, "columnName")
    descriptor = None
    for klass in dom_ManyToMany.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_dom_manytomany_has_tableName():
    assert hasattr(dom_ManyToMany, "tableName")
    descriptor = None
    for klass in dom_ManyToMany.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_dom_manytomany_has_inverse():
    assert hasattr(dom_ManyToMany, "inverse")
    descriptor = None
    for klass in dom_ManyToMany.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)



def test_dom_onetomany_is_not_abstract():
    assert not inspect.isabstract(dom_OneToMany)


def test_dom_onetomany_constructor_exists():
    assert callable(dom_OneToMany.__init__)


def test_dom_onetomany_constructor_args():
    sig = inspect.signature(dom_OneToMany.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_dom_onetomany_has_columnName():
    assert hasattr(dom_OneToMany, "columnName")
    descriptor = None
    for klass in dom_OneToMany.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_dom_daofeature_is_not_abstract():
    assert not inspect.isabstract(dom_DaoFeature)


def test_dom_daofeature_constructor_exists():
    assert callable(dom_DaoFeature.__init__)


def test_dom_daofeature_constructor_args():
    sig = inspect.signature(dom_DaoFeature.__init__)
    params = list(sig.parameters.keys())



def test_dom_attributesortorder_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeSortOrder)


def test_dom_attributesortorder_constructor_exists():
    assert callable(dom_AttributeSortOrder.__init__)


def test_dom_attributesortorder_constructor_args():
    sig = inspect.signature(dom_AttributeSortOrder.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"

def test_dom_attributesortorder_has_desc():
    assert hasattr(dom_AttributeSortOrder, "desc")
    descriptor = None
    for klass in dom_AttributeSortOrder.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributesortorder_has_asc():
    assert hasattr(dom_AttributeSortOrder, "asc")
    descriptor = None
    for klass in dom_AttributeSortOrder.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)



def test_dom_validatorreference_is_not_abstract():
    assert not inspect.isabstract(dom_ValidatorReference)


def test_dom_validatorreference_constructor_exists():
    assert callable(dom_ValidatorReference.__init__)


def test_dom_validatorreference_constructor_args():
    sig = inspect.signature(dom_ValidatorReference.__init__)
    params = list(sig.parameters.keys())



def test_dom_constraint_is_not_abstract():
    assert not inspect.isabstract(dom_Constraint)


def test_dom_constraint_constructor_exists():
    assert callable(dom_Constraint.__init__)


def test_dom_constraint_constructor_args():
    sig = inspect.signature(dom_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_dom_boolliteral_is_not_abstract():
    assert not inspect.isabstract(dom_BoolLiteral)


def test_dom_boolliteral_constructor_exists():
    assert callable(dom_BoolLiteral.__init__)


def test_dom_boolliteral_constructor_args():
    sig = inspect.signature(dom_BoolLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expressionflag_is_not_abstract():
    assert not inspect.isabstract(ExpressionFlag)


def test_expressionflag_constructor_exists():
    assert callable(ExpressionFlag.__init__)


def test_expressionflag_constructor_args():
    sig = inspect.signature(ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_readonlyflag_is_not_abstract():
    assert not inspect.isabstract(dom_ReadOnlyFlag)


def test_dom_readonlyflag_constructor_exists():
    assert callable(dom_ReadOnlyFlag.__init__)


def test_dom_readonlyflag_constructor_args():
    sig = inspect.signature(dom_ReadOnlyFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_availableflag_is_not_abstract():
    assert not inspect.isabstract(dom_AvailableFlag)


def test_dom_availableflag_constructor_exists():
    assert callable(dom_AvailableFlag.__init__)


def test_dom_availableflag_constructor_args():
    sig = inspect.signature(dom_AvailableFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_requiredflag_is_not_abstract():
    assert not inspect.isabstract(dom_RequiredFlag)


def test_dom_requiredflag_constructor_exists():
    assert callable(dom_RequiredFlag.__init__)


def test_dom_requiredflag_constructor_args():
    sig = inspect.signature(dom_RequiredFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_equalityexpr_is_not_abstract():
    assert not inspect.isabstract(dom_EqualityExpr)


def test_dom_equalityexpr_constructor_exists():
    assert callable(dom_EqualityExpr.__init__)


def test_dom_equalityexpr_constructor_args():
    sig = inspect.signature(dom_EqualityExpr.__init__)
    params = list(sig.parameters.keys())



def test_attributeflag_is_not_abstract():
    assert not inspect.isabstract(AttributeFlag)


def test_attributeflag_constructor_exists():
    assert callable(AttributeFlag.__init__)


def test_attributeflag_constructor_args():
    sig = inspect.signature(AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_transientflag_is_not_abstract():
    assert not inspect.isabstract(dom_TransientFlag)


def test_dom_transientflag_constructor_exists():
    assert callable(dom_TransientFlag.__init__)


def test_dom_transientflag_constructor_args():
    sig = inspect.signature(dom_TransientFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_derivedflag_is_not_abstract():
    assert not inspect.isabstract(dom_DerivedFlag)


def test_dom_derivedflag_constructor_exists():
    assert callable(dom_DerivedFlag.__init__)


def test_dom_derivedflag_constructor_args():
    sig = inspect.signature(dom_DerivedFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_expressionflag_is_not_abstract():
    assert not inspect.isabstract(dom_ExpressionFlag)


def test_dom_expressionflag_constructor_exists():
    assert callable(dom_ExpressionFlag.__init__)


def test_dom_expressionflag_constructor_args():
    sig = inspect.signature(dom_ExpressionFlag.__init__)
    params = list(sig.parameters.keys())



def test_attributeproperty_is_not_abstract():
    assert not inspect.isabstract(AttributeProperty)


def test_attributeproperty_constructor_exists():
    assert callable(AttributeProperty.__init__)


def test_attributeproperty_constructor_args():
    sig = inspect.signature(AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom_attributetextproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeTextProperty)


def test_dom_attributetextproperty_constructor_exists():
    assert callable(dom_AttributeTextProperty.__init__)


def test_dom_attributetextproperty_constructor_args():
    sig = inspect.signature(dom_AttributeTextProperty.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "hstoreColumn" in params, "Missing parameter 'hstoreColumn'"
    assert "unitText" in params, "Missing parameter 'unitText'"

def test_dom_attributetextproperty_has_labelText():
    assert hasattr(dom_AttributeTextProperty, "labelText")
    descriptor = None
    for klass in dom_AttributeTextProperty.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributetextproperty_has_tooltipText():
    assert hasattr(dom_AttributeTextProperty, "tooltipText")
    descriptor = None
    for klass in dom_AttributeTextProperty.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributetextproperty_has_hstoreColumn():
    assert hasattr(dom_AttributeTextProperty, "hstoreColumn")
    descriptor = None
    for klass in dom_AttributeTextProperty.__mro__:
        if "hstoreColumn" in klass.__dict__:
            descriptor = klass.__dict__["hstoreColumn"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributetextproperty_has_unitText():
    assert hasattr(dom_AttributeTextProperty, "unitText")
    descriptor = None
    for klass in dom_AttributeTextProperty.__mro__:
        if "unitText" in klass.__dict__:
            descriptor = klass.__dict__["unitText"]
            break
    assert isinstance(descriptor, property)



def test_dom_attributevalidationproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeValidationProperty)


def test_dom_attributevalidationproperty_constructor_exists():
    assert callable(dom_AttributeValidationProperty.__init__)


def test_dom_attributevalidationproperty_constructor_args():
    sig = inspect.signature(dom_AttributeValidationProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom_betweenexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BetweenExpression)


def test_dom_betweenexpression_constructor_exists():
    assert callable(dom_BetweenExpression.__init__)


def test_dom_betweenexpression_constructor_args():
    sig = inspect.signature(dom_BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_dom_betweenexpression_has_operator():
    assert hasattr(dom_BetweenExpression, "operator")
    descriptor = None
    for klass in dom_BetweenExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_dom_betweenexpression_has_not_():
    assert hasattr(dom_BetweenExpression, "not_")
    descriptor = None
    for klass in dom_BetweenExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_dom_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_UnaryExpression)


def test_dom_unaryexpression_constructor_exists():
    assert callable(dom_UnaryExpression.__init__)


def test_dom_unaryexpression_constructor_args():
    sig = inspect.signature(dom_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_unaryexpression_has_operator():
    assert hasattr(dom_UnaryExpression, "operator")
    descriptor = None
    for klass in dom_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_memberofexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MemberOfExpression)


def test_dom_memberofexpression_constructor_exists():
    assert callable(dom_MemberOfExpression.__init__)


def test_dom_memberofexpression_constructor_args():
    sig = inspect.signature(dom_MemberOfExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "memberOf" in params, "Missing parameter 'memberOf'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_memberofexpression_has_not_():
    assert hasattr(dom_MemberOfExpression, "not_")
    descriptor = None
    for klass in dom_MemberOfExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom_memberofexpression_has_memberOf():
    assert hasattr(dom_MemberOfExpression, "memberOf")
    descriptor = None
    for klass in dom_MemberOfExpression.__mro__:
        if "memberOf" in klass.__dict__:
            descriptor = klass.__dict__["memberOf"]
            break
    assert isinstance(descriptor, property)

def test_dom_memberofexpression_has_operator():
    assert hasattr(dom_MemberOfExpression, "operator")
    descriptor = None
    for klass in dom_MemberOfExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_likeexpression_is_not_abstract():
    assert not inspect.isabstract(dom_LikeExpression)


def test_dom_likeexpression_constructor_exists():
    assert callable(dom_LikeExpression.__init__)


def test_dom_likeexpression_constructor_args():
    sig = inspect.signature(dom_LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_likeexpression_has_not_():
    assert hasattr(dom_LikeExpression, "not_")
    descriptor = None
    for klass in dom_LikeExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom_likeexpression_has_operator():
    assert hasattr(dom_LikeExpression, "operator")
    descriptor = None
    for klass in dom_LikeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_inexpression_is_not_abstract():
    assert not inspect.isabstract(dom_InExpression)


def test_dom_inexpression_constructor_exists():
    assert callable(dom_InExpression.__init__)


def test_dom_inexpression_constructor_args():
    sig = inspect.signature(dom_InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_inexpression_has_not_():
    assert hasattr(dom_InExpression, "not_")
    descriptor = None
    for klass in dom_InExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dom_inexpression_has_operator():
    assert hasattr(dom_InExpression, "operator")
    descriptor = None
    for klass in dom_InExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_notexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NotExpression)


def test_dom_notexpression_constructor_exists():
    assert callable(dom_NotExpression.__init__)


def test_dom_notexpression_constructor_args():
    sig = inspect.signature(dom_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BinaryExpression)


def test_dom_binaryexpression_constructor_exists():
    assert callable(dom_BinaryExpression.__init__)


def test_dom_binaryexpression_constructor_args():
    sig = inspect.signature(dom_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dom_binaryexpression_has_operator():
    assert hasattr(dom_BinaryExpression, "operator")
    descriptor = None
    for klass in dom_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dom_aliasedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_AliasedExpression)


def test_dom_aliasedexpression_constructor_exists():
    assert callable(dom_AliasedExpression.__init__)


def test_dom_aliasedexpression_constructor_args():
    sig = inspect.signature(dom_AliasedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_aliasedexpression_has_name():
    assert hasattr(dom_AliasedExpression, "name")
    descriptor = None
    for klass in dom_AliasedExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_presentablefeature_is_not_abstract():
    assert not inspect.isabstract(dom_PresentableFeature)


def test_dom_presentablefeature_constructor_exists():
    assert callable(dom_PresentableFeature.__init__)


def test_dom_presentablefeature_constructor_args():
    sig = inspect.signature(dom_PresentableFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_presentablefeature_has_name():
    assert hasattr(dom_PresentableFeature, "name")
    descriptor = None
    for klass in dom_PresentableFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_whenclause_is_not_abstract():
    assert not inspect.isabstract(dom_WhenClause)


def test_dom_whenclause_constructor_exists():
    assert callable(dom_WhenClause.__init__)


def test_dom_whenclause_constructor_args():
    sig = inspect.signature(dom_WhenClause.__init__)
    params = list(sig.parameters.keys())



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_realliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_RealLiteralValue)


def test_dom_realliteralvalue_constructor_exists():
    assert callable(dom_RealLiteralValue.__init__)


def test_dom_realliteralvalue_constructor_args():
    sig = inspect.signature(dom_RealLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom_realliteralvalue_has_value():
    assert hasattr(dom_RealLiteralValue, "value")
    descriptor = None
    for klass in dom_RealLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom_integerliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_IntegerLiteralValue)


def test_dom_integerliteralvalue_constructor_exists():
    assert callable(dom_IntegerLiteralValue.__init__)


def test_dom_integerliteralvalue_constructor_args():
    sig = inspect.signature(dom_IntegerLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom_integerliteralvalue_has_value():
    assert hasattr(dom_IntegerLiteralValue, "value")
    descriptor = None
    for klass in dom_IntegerLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom_emptyliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_EmptyLiteralValue)


def test_dom_emptyliteralvalue_constructor_exists():
    assert callable(dom_EmptyLiteralValue.__init__)


def test_dom_emptyliteralvalue_constructor_args():
    sig = inspect.signature(dom_EmptyLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_nullliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_NullLiteralValue)


def test_dom_nullliteralvalue_constructor_exists():
    assert callable(dom_NullLiteralValue.__init__)


def test_dom_nullliteralvalue_constructor_args():
    sig = inspect.signature(dom_NullLiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_booleanliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_BooleanLiteralValue)


def test_dom_booleanliteralvalue_constructor_exists():
    assert callable(dom_BooleanLiteralValue.__init__)


def test_dom_booleanliteralvalue_constructor_args():
    sig = inspect.signature(dom_BooleanLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_dom_booleanliteralvalue_has_isTrue():
    assert hasattr(dom_BooleanLiteralValue, "isTrue")
    descriptor = None
    for klass in dom_BooleanLiteralValue.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_dom_literalvalue_is_not_abstract():
    assert not inspect.isabstract(dom_LiteralValue)


def test_dom_literalvalue_constructor_exists():
    assert callable(dom_LiteralValue.__init__)


def test_dom_literalvalue_constructor_args():
    sig = inspect.signature(dom_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ParenthesizedExpression)


def test_dom_parenthesizedexpression_constructor_exists():
    assert callable(dom_ParenthesizedExpression.__init__)


def test_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(dom_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_subquery_is_not_abstract():
    assert not inspect.isabstract(dom_SubQuery)


def test_dom_subquery_constructor_exists():
    assert callable(dom_SubQuery.__init__)


def test_dom_subquery_constructor_args():
    sig = inspect.signature(dom_SubQuery.__init__)
    params = list(sig.parameters.keys())



def test_dom_altwhenclause_is_not_abstract():
    assert not inspect.isabstract(dom_AltWhenClause)


def test_dom_altwhenclause_constructor_exists():
    assert callable(dom_AltWhenClause.__init__)


def test_dom_altwhenclause_constructor_args():
    sig = inspect.signature(dom_AltWhenClause.__init__)
    params = list(sig.parameters.keys())



def test_dom_stringliteralvalue_is_not_abstract():
    assert not inspect.isabstract(dom_StringLiteralValue)


def test_dom_stringliteralvalue_constructor_exists():
    assert callable(dom_StringLiteralValue.__init__)


def test_dom_stringliteralvalue_constructor_args():
    sig = inspect.signature(dom_StringLiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dom_stringliteralvalue_has_value():
    assert hasattr(dom_StringLiteralValue, "value")
    descriptor = None
    for klass in dom_StringLiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dom_trimfunction_is_not_abstract():
    assert not inspect.isabstract(dom_TrimFunction)


def test_dom_trimfunction_constructor_exists():
    assert callable(dom_TrimFunction.__init__)


def test_dom_trimfunction_constructor_args():
    sig = inspect.signature(dom_TrimFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_dom_trimfunction_has_function():
    assert hasattr(dom_TrimFunction, "function")
    descriptor = None
    for klass in dom_TrimFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_dom_trimfunction_has_mode():
    assert hasattr(dom_TrimFunction, "mode")
    descriptor = None
    for klass in dom_TrimFunction.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_dom_caseexpression_is_not_abstract():
    assert not inspect.isabstract(dom_CaseExpression)


def test_dom_caseexpression_constructor_exists():
    assert callable(dom_CaseExpression.__init__)


def test_dom_caseexpression_constructor_args():
    sig = inspect.signature(dom_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_QuantifiedExpression)


def test_dom_quantifiedexpression_constructor_exists():
    assert callable(dom_QuantifiedExpression.__init__)


def test_dom_quantifiedexpression_constructor_args():
    sig = inspect.signature(dom_QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_quantifiedexpression_has_quantifier():
    assert hasattr(dom_QuantifiedExpression, "quantifier")
    descriptor = None
    for klass in dom_QuantifiedExpression.__mro__:
        if "quantifier" in klass.__dict__:
            descriptor = klass.__dict__["quantifier"]
            break
    assert isinstance(descriptor, property)

def test_dom_quantifiedexpression_has_name():
    assert hasattr(dom_QuantifiedExpression, "name")
    descriptor = None
    for klass in dom_QuantifiedExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dom_queryparametervalue_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameterValue)


def test_dom_queryparametervalue_constructor_exists():
    assert callable(dom_QueryParameterValue.__init__)


def test_dom_queryparametervalue_constructor_args():
    sig = inspect.signature(dom_QueryParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(dom_QueryParameterReference)


def test_dom_queryparameterreference_constructor_exists():
    assert callable(dom_QueryParameterReference.__init__)


def test_dom_queryparameterreference_constructor_args():
    sig = inspect.signature(dom_QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_dom_attributeflag_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeFlag)


def test_dom_attributeflag_constructor_exists():
    assert callable(dom_AttributeFlag.__init__)


def test_dom_attributeflag_constructor_args():
    sig = inspect.signature(dom_AttributeFlag.__init__)
    params = list(sig.parameters.keys())



def test_dom_incrementerreference_is_not_abstract():
    assert not inspect.isabstract(dom_IncrementerReference)


def test_dom_incrementerreference_constructor_exists():
    assert callable(dom_IncrementerReference.__init__)


def test_dom_incrementerreference_constructor_args():
    sig = inspect.signature(dom_IncrementerReference.__init__)
    params = list(sig.parameters.keys())



def test_dom_datatypeandtypeparameter_is_not_abstract():
    assert not inspect.isabstract(dom_DataTypeAndTypeParameter)


def test_dom_datatypeandtypeparameter_constructor_exists():
    assert callable(dom_DataTypeAndTypeParameter.__init__)


def test_dom_datatypeandtypeparameter_constructor_args():
    sig = inspect.signature(dom_DataTypeAndTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom_propertymapping_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyMapping)


def test_dom_propertymapping_constructor_exists():
    assert callable(dom_PropertyMapping.__init__)


def test_dom_propertymapping_constructor_args():
    sig = inspect.signature(dom_PropertyMapping.__init__)
    params = list(sig.parameters.keys())
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "toLeft" in params, "Missing parameter 'toLeft'"

def test_dom_propertymapping_has_biDirectional():
    assert hasattr(dom_PropertyMapping, "biDirectional")
    descriptor = None
    for klass in dom_PropertyMapping.__mro__:
        if "biDirectional" in klass.__dict__:
            descriptor = klass.__dict__["biDirectional"]
            break
    assert isinstance(descriptor, property)

def test_dom_propertymapping_has_toRight():
    assert hasattr(dom_PropertyMapping, "toRight")
    descriptor = None
    for klass in dom_PropertyMapping.__mro__:
        if "toRight" in klass.__dict__:
            descriptor = klass.__dict__["toRight"]
            break
    assert isinstance(descriptor, property)

def test_dom_propertymapping_has_toLeft():
    assert hasattr(dom_PropertyMapping, "toLeft")
    descriptor = None
    for klass in dom_PropertyMapping.__mro__:
        if "toLeft" in klass.__dict__:
            descriptor = klass.__dict__["toLeft"]
            break
    assert isinstance(descriptor, property)



def test_dom_conditionsblock_is_not_abstract():
    assert not inspect.isabstract(dom_ConditionsBlock)


def test_dom_conditionsblock_constructor_exists():
    assert callable(dom_ConditionsBlock.__init__)


def test_dom_conditionsblock_constructor_args():
    sig = inspect.signature(dom_ConditionsBlock.__init__)
    params = list(sig.parameters.keys())



def test_presentablefeature_is_not_abstract():
    assert not inspect.isabstract(PresentableFeature)


def test_presentablefeature_constructor_exists():
    assert callable(PresentableFeature.__init__)


def test_presentablefeature_constructor_args():
    sig = inspect.signature(PresentableFeature.__init__)
    params = list(sig.parameters.keys())



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_dom_valueobject_is_not_abstract():
    assert not inspect.isabstract(dom_ValueObject)


def test_dom_valueobject_constructor_exists():
    assert callable(dom_ValueObject.__init__)


def test_dom_valueobject_constructor_args():
    sig = inspect.signature(dom_ValueObject.__init__)
    params = list(sig.parameters.keys())



def test_dom_attributeproperty_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeProperty)


def test_dom_attributeproperty_constructor_exists():
    assert callable(dom_AttributeProperty.__init__)


def test_dom_attributeproperty_constructor_args():
    sig = inspect.signature(dom_AttributeProperty.__init__)
    params = list(sig.parameters.keys())



def test_dom_dataview_is_not_abstract():
    assert not inspect.isabstract(dom_DataView)


def test_dom_dataview_constructor_exists():
    assert callable(dom_DataView.__init__)


def test_dom_dataview_constructor_args():
    sig = inspect.signature(dom_DataView.__init__)
    params = list(sig.parameters.keys())



def test_dom_type_is_not_abstract():
    assert not inspect.isabstract(dom_Type)


def test_dom_type_constructor_exists():
    assert callable(dom_Type.__init__)


def test_dom_type_constructor_args():
    sig = inspect.signature(dom_Type.__init__)
    params = list(sig.parameters.keys())



def test_queryparameterreference_is_not_abstract():
    assert not inspect.isabstract(QueryParameterReference)


def test_queryparameterreference_constructor_exists():
    assert callable(QueryParameterReference.__init__)


def test_queryparameterreference_constructor_args():
    sig = inspect.signature(QueryParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_queryparameter_is_not_abstract():
    assert not inspect.isabstract(QueryParameter)


def test_queryparameter_constructor_exists():
    assert callable(QueryParameter.__init__)


def test_queryparameter_constructor_args():
    sig = inspect.signature(QueryParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom_expression_is_not_abstract():
    assert not inspect.isabstract(dom_Expression)


def test_dom_expression_constructor_exists():
    assert callable(dom_Expression.__init__)


def test_dom_expression_constructor_args():
    sig = inspect.signature(dom_Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom_daooperation_is_not_abstract():
    assert not inspect.isabstract(dom_DaoOperation)


def test_dom_daooperation_constructor_exists():
    assert callable(dom_DaoOperation.__init__)


def test_dom_daooperation_constructor_args():
    sig = inspect.signature(dom_DaoOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_dom_daooperation_has_name():
    assert hasattr(dom_DaoOperation, "name")
    descriptor = None
    for klass in dom_DaoOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_daooperation_has_many():
    assert hasattr(dom_DaoOperation, "many")
    descriptor = None
    for klass in dom_DaoOperation.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_dom_dependant_is_not_abstract():
    assert not inspect.isabstract(dom_Dependant)


def test_dom_dependant_constructor_exists():
    assert callable(dom_Dependant.__init__)


def test_dom_dependant_constructor_args():
    sig = inspect.signature(dom_Dependant.__init__)
    params = list(sig.parameters.keys())



def test_dependant_is_not_abstract():
    assert not inspect.isabstract(Dependant)


def test_dependant_constructor_exists():
    assert callable(Dependant.__init__)


def test_dependant_constructor_args():
    sig = inspect.signature(Dependant.__init__)
    params = list(sig.parameters.keys())



def test_dom_entity_is_not_abstract():
    assert not inspect.isabstract(dom_Entity)


def test_dom_entity_constructor_exists():
    assert callable(dom_Entity.__init__)


def test_dom_entity_constructor_args():
    sig = inspect.signature(dom_Entity.__init__)
    params = list(sig.parameters.keys())



def test_dom_parameter_is_not_abstract():
    assert not inspect.isabstract(dom_Parameter)


def test_dom_parameter_constructor_exists():
    assert callable(dom_Parameter.__init__)


def test_dom_parameter_constructor_args():
    sig = inspect.signature(dom_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_dom_parameter_has_name():
    assert hasattr(dom_Parameter, "name")
    descriptor = None
    for klass in dom_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_parameter_has_many():
    assert hasattr(dom_Parameter, "many")
    descriptor = None
    for klass in dom_Parameter.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_daooperation_is_not_abstract():
    assert not inspect.isabstract(DaoOperation)


def test_daooperation_constructor_exists():
    assert callable(DaoOperation.__init__)


def test_daooperation_constructor_args():
    sig = inspect.signature(DaoOperation.__init__)
    params = list(sig.parameters.keys())



def test_dom_simpletype_is_not_abstract():
    assert not inspect.isabstract(dom_SimpleType)


def test_dom_simpletype_constructor_exists():
    assert callable(dom_SimpleType.__init__)


def test_dom_simpletype_constructor_args():
    sig = inspect.signature(dom_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_idocumentable_is_not_abstract():
    assert not inspect.isabstract(IDocumentable)


def test_idocumentable_constructor_exists():
    assert callable(IDocumentable.__init__)


def test_idocumentable_constructor_args():
    sig = inspect.signature(IDocumentable.__init__)
    params = list(sig.parameters.keys())



def test_dom_featurereference_is_not_abstract():
    assert not inspect.isabstract(dom_FeatureReference)


def test_dom_featurereference_constructor_exists():
    assert callable(dom_FeatureReference.__init__)


def test_dom_featurereference_constructor_args():
    sig = inspect.signature(dom_FeatureReference.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_dom_featurereference_has_all():
    assert hasattr(dom_FeatureReference, "all")
    descriptor = None
    for klass in dom_FeatureReference.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_dom_attributegroup_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeGroup)


def test_dom_attributegroup_constructor_exists():
    assert callable(dom_AttributeGroup.__init__)


def test_dom_attributegroup_constructor_args():
    sig = inspect.signature(dom_AttributeGroup.__init__)
    params = list(sig.parameters.keys())
    assert "sortorder" in params, "Missing parameter 'sortorder'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "name" in params, "Missing parameter 'name'"
    assert "key" in params, "Missing parameter 'key'"
    assert "filter" in params, "Missing parameter 'filter'"

def test_dom_attributegroup_has_sortorder():
    assert hasattr(dom_AttributeGroup, "sortorder")
    descriptor = None
    for klass in dom_AttributeGroup.__mro__:
        if "sortorder" in klass.__dict__:
            descriptor = klass.__dict__["sortorder"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributegroup_has_unique():
    assert hasattr(dom_AttributeGroup, "unique")
    descriptor = None
    for klass in dom_AttributeGroup.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributegroup_has_name():
    assert hasattr(dom_AttributeGroup, "name")
    descriptor = None
    for klass in dom_AttributeGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributegroup_has_key():
    assert hasattr(dom_AttributeGroup, "key")
    descriptor = None
    for klass in dom_AttributeGroup.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_dom_attributegroup_has_filter():
    assert hasattr(dom_AttributeGroup, "filter")
    descriptor = None
    for klass in dom_AttributeGroup.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_dom_operation_is_not_abstract():
    assert not inspect.isabstract(dom_Operation)


def test_dom_operation_constructor_exists():
    assert callable(dom_Operation.__init__)


def test_dom_operation_constructor_args():
    sig = inspect.signature(dom_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_dom_operation_has_expression():
    assert hasattr(dom_Operation, "expression")
    descriptor = None
    for klass in dom_Operation.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_dom_queryoperation_is_not_abstract():
    assert not inspect.isabstract(dom_QueryOperation)


def test_dom_queryoperation_constructor_exists():
    assert callable(dom_QueryOperation.__init__)


def test_dom_queryoperation_constructor_args():
    sig = inspect.signature(dom_QueryOperation.__init__)
    params = list(sig.parameters.keys())



def test_dom_delegateoperation_is_not_abstract():
    assert not inspect.isabstract(dom_DelegateOperation)


def test_dom_delegateoperation_constructor_exists():
    assert callable(dom_DelegateOperation.__init__)


def test_dom_delegateoperation_constructor_args():
    sig = inspect.signature(dom_DelegateOperation.__init__)
    params = list(sig.parameters.keys())
    assert "crudOperationType" in params, "Missing parameter 'crudOperationType'"
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_dom_delegateoperation_has_crudOperationType():
    assert hasattr(dom_DelegateOperation, "crudOperationType")
    descriptor = None
    for klass in dom_DelegateOperation.__mro__:
        if "crudOperationType" in klass.__dict__:
            descriptor = klass.__dict__["crudOperationType"]
            break
    assert isinstance(descriptor, property)

def test_dom_delegateoperation_has_many():
    assert hasattr(dom_DelegateOperation, "many")
    descriptor = None
    for klass in dom_DelegateOperation.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_dom_delegateoperation_has_name():
    assert hasattr(dom_DelegateOperation, "name")
    descriptor = None
    for klass in dom_DelegateOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_referenceablebyxmadslvariable_is_not_abstract():
    assert not inspect.isabstract(ReferenceableByXmadslVariable)


def test_referenceablebyxmadslvariable_constructor_exists():
    assert callable(ReferenceableByXmadslVariable.__init__)


def test_referenceablebyxmadslvariable_constructor_args():
    sig = inspect.signature(ReferenceableByXmadslVariable.__init__)
    params = list(sig.parameters.keys())



def test_dom_ielementwithnoname_is_not_abstract():
    assert not inspect.isabstract(dom_IElementWithNoName)


def test_dom_ielementwithnoname_constructor_exists():
    assert callable(dom_IElementWithNoName.__init__)


def test_dom_ielementwithnoname_constructor_args():
    sig = inspect.signature(dom_IElementWithNoName.__init__)
    params = list(sig.parameters.keys())
    assert "noName" in params, "Missing parameter 'noName'"

def test_dom_ielementwithnoname_has_noName():
    assert hasattr(dom_IElementWithNoName, "noName")
    descriptor = None
    for klass in dom_IElementWithNoName.__mro__:
        if "noName" in klass.__dict__:
            descriptor = klass.__dict__["noName"]
            break
    assert isinstance(descriptor, property)



def test_dom_property_is_not_abstract():
    assert not inspect.isabstract(dom_Property)


def test_dom_property_constructor_exists():
    assert callable(dom_Property.__init__)


def test_dom_property_constructor_args():
    sig = inspect.signature(dom_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_dom_property_has_name():
    assert hasattr(dom_Property, "name")
    descriptor = None
    for klass in dom_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dom_property_has_defaultValue():
    assert hasattr(dom_Property, "defaultValue")
    descriptor = None
    for klass in dom_Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_dom_attribute_is_not_abstract():
    assert not inspect.isabstract(dom_Attribute)


def test_dom_attribute_constructor_exists():
    assert callable(dom_Attribute.__init__)


def test_dom_attribute_constructor_args():
    sig = inspect.signature(dom_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "version" in params, "Missing parameter 'version'"
    assert "composition" in params, "Missing parameter 'composition'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "required" in params, "Missing parameter 'required'"
    assert "dataTypeName" in params, "Missing parameter 'dataTypeName'"

def test_dom_attribute_has_many():
    assert hasattr(dom_Attribute, "many")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_readOnly():
    assert hasattr(dom_Attribute, "readOnly")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_version():
    assert hasattr(dom_Attribute, "version")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_composition():
    assert hasattr(dom_Attribute, "composition")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "composition" in klass.__dict__:
            descriptor = klass.__dict__["composition"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_reference():
    assert hasattr(dom_Attribute, "reference")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_defaultValue():
    assert hasattr(dom_Attribute, "defaultValue")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_derived():
    assert hasattr(dom_Attribute, "derived")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_identifier():
    assert hasattr(dom_Attribute, "identifier")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_transient():
    assert hasattr(dom_Attribute, "transient")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_required():
    assert hasattr(dom_Attribute, "required")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_dom_attribute_has_dataTypeName():
    assert hasattr(dom_Attribute, "dataTypeName")
    descriptor = None
    for klass in dom_Attribute.__mro__:
        if "dataTypeName" in klass.__dict__:
            descriptor = klass.__dict__["dataTypeName"]
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



def test_dom_applicationsession_is_not_abstract():
    assert not inspect.isabstract(dom_ApplicationSession)


def test_dom_applicationsession_constructor_exists():
    assert callable(dom_ApplicationSession.__init__)


def test_dom_applicationsession_constructor_args():
    sig = inspect.signature(dom_ApplicationSession.__init__)
    params = list(sig.parameters.keys())



def test_dom_mapper_is_not_abstract():
    assert not inspect.isabstract(dom_Mapper)


def test_dom_mapper_constructor_exists():
    assert callable(dom_Mapper.__init__)


def test_dom_mapper_constructor_args():
    sig = inspect.signature(dom_Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "toLeft" in params, "Missing parameter 'toLeft'"
    assert "toRight" in params, "Missing parameter 'toRight'"
    assert "biDirectional" in params, "Missing parameter 'biDirectional'"

def test_dom_mapper_has_toLeft():
    assert hasattr(dom_Mapper, "toLeft")
    descriptor = None
    for klass in dom_Mapper.__mro__:
        if "toLeft" in klass.__dict__:
            descriptor = klass.__dict__["toLeft"]
            break
    assert isinstance(descriptor, property)

def test_dom_mapper_has_toRight():
    assert hasattr(dom_Mapper, "toRight")
    descriptor = None
    for klass in dom_Mapper.__mro__:
        if "toRight" in klass.__dict__:
            descriptor = klass.__dict__["toRight"]
            break
    assert isinstance(descriptor, property)

def test_dom_mapper_has_biDirectional():
    assert hasattr(dom_Mapper, "biDirectional")
    descriptor = None
    for klass in dom_Mapper.__mro__:
        if "biDirectional" in klass.__dict__:
            descriptor = klass.__dict__["biDirectional"]
            break
    assert isinstance(descriptor, property)



def test_dom_dao_is_not_abstract():
    assert not inspect.isabstract(dom_Dao)


def test_dom_dao_constructor_exists():
    assert callable(dom_Dao.__init__)


def test_dom_dao_constructor_args():
    sig = inspect.signature(dom_Dao.__init__)
    params = list(sig.parameters.keys())
    assert "discriminator" in params, "Missing parameter 'discriminator'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dom_dao_has_discriminator():
    assert hasattr(dom_Dao, "discriminator")
    descriptor = None
    for klass in dom_Dao.__mro__:
        if "discriminator" in klass.__dict__:
            descriptor = klass.__dict__["discriminator"]
            break
    assert isinstance(descriptor, property)

def test_dom_dao_has_qualifier():
    assert hasattr(dom_Dao, "qualifier")
    descriptor = None
    for klass in dom_Dao.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_dom_dao_has_tableName():
    assert hasattr(dom_Dao, "tableName")
    descriptor = None
    for klass in dom_Dao.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dom_service_is_not_abstract():
    assert not inspect.isabstract(dom_Service)


def test_dom_service_constructor_exists():
    assert callable(dom_Service.__init__)


def test_dom_service_constructor_args():
    sig = inspect.signature(dom_Service.__init__)
    params = list(sig.parameters.keys())



def test_dom_complextype_is_not_abstract():
    assert not inspect.isabstract(dom_ComplexType)


def test_dom_complextype_constructor_exists():
    assert callable(dom_ComplexType.__init__)


def test_dom_complextype_constructor_args():
    sig = inspect.signature(dom_ComplexType.__init__)
    params = list(sig.parameters.keys())

def test_databaseconstrainttype_exists():
    # Check that the Enumeration exists
    assert DataBaseConstraintType is not None

def test_databaseconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataBaseConstraintType]
    expected_literals = [
        "NULL",
        "PRIMARY",
        "NATURAL",
        "UNIQUE",
        "INDEX",
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
        "READ",
        "DELETE",
        "CREATE",
        "ALL",
        "NULL",
        "UPDATE",
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
JoinEntity_strategy = st.builds(
    JoinEntity,
)
FromRange_strategy = st.builds(
    FromRange,
)
dom_InCollection_strategy = st.builds(
    dom_InCollection,
    alias=
        safe_text,
    path=
        safe_text
)
dom_InClass_strategy = st.builds(
    dom_InClass,
    class_=
        safe_text,
    name=
        safe_text
)
dom_FromClass_strategy = st.builds(
    dom_FromClass,
    popertyFetch=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
dom_CollectionFunction_strategy = st.builds(
    dom_CollectionFunction,
    function=
        safe_text
)
dom_AggregateFunction_strategy = st.builds(
    dom_AggregateFunction,
    from_=
        safe_text,
    distinct=
        st.booleans(),
    function=
        safe_text,
    all=
        st.booleans()
)
dom_FunctionCall_strategy = st.builds(
    dom_FunctionCall,
    function=
        safe_text
)
dom_CastFunction_strategy = st.builds(
    dom_CastFunction,
    function=
        safe_text,
    name=
        safe_text
)
dom_JoinEntity_strategy = st.builds(
    dom_JoinEntity,
    name=
        safe_text
)
dom_InCollectionElements_strategy = st.builds(
    dom_InCollectionElements,
    reference=
        safe_text,
    name=
        safe_text
)
dom_PropertyValue_strategy = st.builds(
    dom_PropertyValue,
    classProperty=
        st.booleans(),
    segments=
        safe_text,
    name=
        safe_text
)
dom_PropertyAssignment_strategy = st.builds(
    dom_PropertyAssignment,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
dom_SelectObject_strategy = st.builds(
    dom_SelectObject,
    name=
        safe_text
)
dom_SelectClass_strategy = st.builds(
    dom_SelectClass,
    class_=
        safe_text
)
dom_SelectProperties_strategy = st.builds(
    dom_SelectProperties,
    distinct=
        st.booleans()
)
dom_SortOrderElement_strategy = st.builds(
    dom_SortOrderElement,
    sortOrder=
        safe_text
)
dom_Join_strategy = st.builds(
    dom_Join,
    type=
        safe_text,
    fetch=
        st.booleans(),
    propertyFetch=
        st.booleans()
)
dom_FromRange_strategy = st.builds(
    dom_FromRange,
)
dom_CallOutputParameter_strategy = st.builds(
    dom_CallOutputParameter,
    name=
        safe_text
)
dom_CallInputParameter_strategy = st.builds(
    dom_CallInputParameter,
    name=
        safe_text
)
QlStatement_strategy = st.builds(
    QlStatement,
)
dom_InsertStatement_strategy = st.builds(
    dom_InsertStatement,
)
dom_UpdateStatement_strategy = st.builds(
    dom_UpdateStatement,
    name=
        safe_text,
    versioned=
        st.booleans()
)
dom_DeleteStatement_strategy = st.builds(
    dom_DeleteStatement,
    name=
        safe_text
)
dom_SelectStatement_strategy = st.builds(
    dom_SelectStatement,
)
dom_CallableStatement_strategy = st.builds(
    dom_CallableStatement,
    name=
        safe_text,
    functionCall=
        st.booleans()
)
dom_Function_strategy = st.builds(
    dom_Function,
)
DaoFeature_strategy = st.builds(
    DaoFeature,
)
dom_SqlType_strategy = st.builds(
    dom_SqlType,
)
dom_OneToOne_strategy = st.builds(
    dom_OneToOne,
)
dom_ManyToOne_strategy = st.builds(
    dom_ManyToOne,
    columnName=
        safe_text,
    derived=
        st.booleans()
)
dom_Column_strategy = st.builds(
    dom_Column,
    columnName=
        safe_text
)
dom_DataBaseConstraint_strategy = st.builds(
    dom_DataBaseConstraint,
    name=
        safe_text,
    type=
        safe_text
)
dom_QlStatement_strategy = st.builds(
    dom_QlStatement,
)
dom_QueryParameter_strategy = st.builds(
    dom_QueryParameter,
)
dom_ManyToMany_strategy = st.builds(
    dom_ManyToMany,
    columnName=
        safe_text,
    tableName=
        safe_text,
    inverse=
        st.booleans()
)
dom_OneToMany_strategy = st.builds(
    dom_OneToMany,
    columnName=
        safe_text
)
dom_DaoFeature_strategy = st.builds(
    dom_DaoFeature,
)
dom_AttributeSortOrder_strategy = st.builds(
    dom_AttributeSortOrder,
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
dom_ValidatorReference_strategy = st.builds(
    dom_ValidatorReference,
)
dom_Constraint_strategy = st.builds(
    dom_Constraint,
)
dom_BoolLiteral_strategy = st.builds(
    dom_BoolLiteral,
)
ExpressionFlag_strategy = st.builds(
    ExpressionFlag,
)
dom_ReadOnlyFlag_strategy = st.builds(
    dom_ReadOnlyFlag,
)
dom_AvailableFlag_strategy = st.builds(
    dom_AvailableFlag,
)
dom_RequiredFlag_strategy = st.builds(
    dom_RequiredFlag,
)
dom_EqualityExpr_strategy = st.builds(
    dom_EqualityExpr,
)
AttributeFlag_strategy = st.builds(
    AttributeFlag,
)
dom_TransientFlag_strategy = st.builds(
    dom_TransientFlag,
)
dom_DerivedFlag_strategy = st.builds(
    dom_DerivedFlag,
)
dom_ExpressionFlag_strategy = st.builds(
    dom_ExpressionFlag,
)
AttributeProperty_strategy = st.builds(
    AttributeProperty,
)
dom_AttributeTextProperty_strategy = st.builds(
    dom_AttributeTextProperty,
    labelText=
        safe_text,
    tooltipText=
        safe_text,
    hstoreColumn=
        safe_text,
    unitText=
        safe_text
)
dom_AttributeValidationProperty_strategy = st.builds(
    dom_AttributeValidationProperty,
)
dom_BetweenExpression_strategy = st.builds(
    dom_BetweenExpression,
    operator=
        safe_text,
    not_=
        st.booleans()
)
dom_UnaryExpression_strategy = st.builds(
    dom_UnaryExpression,
    operator=
        safe_text
)
dom_MemberOfExpression_strategy = st.builds(
    dom_MemberOfExpression,
    not_=
        st.booleans(),
    memberOf=
        safe_text,
    operator=
        safe_text
)
dom_LikeExpression_strategy = st.builds(
    dom_LikeExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom_InExpression_strategy = st.builds(
    dom_InExpression,
    not_=
        st.booleans(),
    operator=
        safe_text
)
dom_NotExpression_strategy = st.builds(
    dom_NotExpression,
)
dom_BinaryExpression_strategy = st.builds(
    dom_BinaryExpression,
    operator=
        safe_text
)
dom_AliasedExpression_strategy = st.builds(
    dom_AliasedExpression,
    name=
        safe_text
)
dom_PresentableFeature_strategy = st.builds(
    dom_PresentableFeature,
    name=
        safe_text
)
dom_WhenClause_strategy = st.builds(
    dom_WhenClause,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
dom_RealLiteralValue_strategy = st.builds(
    dom_RealLiteralValue,
    value=
        safe_text
)
dom_IntegerLiteralValue_strategy = st.builds(
    dom_IntegerLiteralValue,
    value=
        safe_text
)
dom_EmptyLiteralValue_strategy = st.builds(
    dom_EmptyLiteralValue,
)
dom_NullLiteralValue_strategy = st.builds(
    dom_NullLiteralValue,
)
dom_BooleanLiteralValue_strategy = st.builds(
    dom_BooleanLiteralValue,
    isTrue=
        st.booleans()
)
dom_LiteralValue_strategy = st.builds(
    dom_LiteralValue,
)
dom_ParenthesizedExpression_strategy = st.builds(
    dom_ParenthesizedExpression,
)
dom_SubQuery_strategy = st.builds(
    dom_SubQuery,
)
dom_AltWhenClause_strategy = st.builds(
    dom_AltWhenClause,
)
dom_StringLiteralValue_strategy = st.builds(
    dom_StringLiteralValue,
    value=
        safe_text
)
dom_TrimFunction_strategy = st.builds(
    dom_TrimFunction,
    function=
        safe_text,
    mode=
        safe_text
)
dom_CaseExpression_strategy = st.builds(
    dom_CaseExpression,
)
dom_QuantifiedExpression_strategy = st.builds(
    dom_QuantifiedExpression,
    quantifier=
        safe_text,
    name=
        safe_text
)
dom_QueryParameterValue_strategy = st.builds(
    dom_QueryParameterValue,
)
dom_QueryParameterReference_strategy = st.builds(
    dom_QueryParameterReference,
)
dom_AttributeFlag_strategy = st.builds(
    dom_AttributeFlag,
)
dom_IncrementerReference_strategy = st.builds(
    dom_IncrementerReference,
)
dom_DataTypeAndTypeParameter_strategy = st.builds(
    dom_DataTypeAndTypeParameter,
)
dom_PropertyMapping_strategy = st.builds(
    dom_PropertyMapping,
    biDirectional=
        st.booleans(),
    toRight=
        st.booleans(),
    toLeft=
        st.booleans()
)
dom_ConditionsBlock_strategy = st.builds(
    dom_ConditionsBlock,
)
PresentableFeature_strategy = st.builds(
    PresentableFeature,
)
ComplexType_strategy = st.builds(
    ComplexType,
)
dom_ValueObject_strategy = st.builds(
    dom_ValueObject,
)
dom_AttributeProperty_strategy = st.builds(
    dom_AttributeProperty,
)
dom_DataView_strategy = st.builds(
    dom_DataView,
)
dom_Type_strategy = st.builds(
    dom_Type,
)
QueryParameterReference_strategy = st.builds(
    QueryParameterReference,
)
QueryParameter_strategy = st.builds(
    QueryParameter,
)
dom_Expression_strategy = st.builds(
    dom_Expression,
)
dom_DaoOperation_strategy = st.builds(
    dom_DaoOperation,
    name=
        safe_text,
    many=
        st.booleans()
)
dom_Dependant_strategy = st.builds(
    dom_Dependant,
)
Dependant_strategy = st.builds(
    Dependant,
)
dom_Entity_strategy = st.builds(
    dom_Entity,
)
dom_Parameter_strategy = st.builds(
    dom_Parameter,
    name=
        safe_text,
    many=
        st.booleans()
)
DaoOperation_strategy = st.builds(
    DaoOperation,
)
dom_SimpleType_strategy = st.builds(
    dom_SimpleType,
)
IDocumentable_strategy = st.builds(
    IDocumentable,
)
dom_FeatureReference_strategy = st.builds(
    dom_FeatureReference,
    all=
        st.booleans()
)
dom_AttributeGroup_strategy = st.builds(
    dom_AttributeGroup,
    sortorder=
        st.booleans(),
    unique=
        st.booleans(),
    name=
        safe_text,
    key=
        st.booleans(),
    filter=
        st.booleans()
)
dom_Operation_strategy = st.builds(
    dom_Operation,
    expression=
        safe_text
)
dom_QueryOperation_strategy = st.builds(
    dom_QueryOperation,
)
dom_DelegateOperation_strategy = st.builds(
    dom_DelegateOperation,
    crudOperationType=
        safe_text,
    many=
        st.booleans(),
    name=
        safe_text
)
ReferenceableByXmadslVariable_strategy = st.builds(
    ReferenceableByXmadslVariable,
)
dom_IElementWithNoName_strategy = st.builds(
    dom_IElementWithNoName,
    noName=
        safe_text
)
dom_Property_strategy = st.builds(
    dom_Property,
    name=
        safe_text,
    defaultValue=
        safe_text
)
dom_Attribute_strategy = st.builds(
    dom_Attribute,
    many=
        st.booleans(),
    readOnly=
        st.booleans(),
    version=
        st.booleans(),
    composition=
        st.booleans(),
    reference=
        st.booleans(),
    defaultValue=
        safe_text,
    derived=
        st.booleans(),
    identifier=
        st.booleans(),
    transient=
        st.booleans(),
    required=
        st.booleans(),
    dataTypeName=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
dom_ApplicationSession_strategy = st.builds(
    dom_ApplicationSession,
)
dom_Mapper_strategy = st.builds(
    dom_Mapper,
    toLeft=
        st.booleans(),
    toRight=
        st.booleans(),
    biDirectional=
        st.booleans()
)
dom_Dao_strategy = st.builds(
    dom_Dao,
    discriminator=
        safe_text,
    qualifier=
        safe_text,
    tableName=
        safe_text
)
dom_Service_strategy = st.builds(
    dom_Service,
)
dom_ComplexType_strategy = st.builds(
    dom_ComplexType,
)

@given(instance=JoinEntity_strategy)
@settings(max_examples=50)
def test_joinentity_instantiation(instance):
    assert isinstance(instance, JoinEntity)

@given(instance=FromRange_strategy)
@settings(max_examples=50)
def test_fromrange_instantiation(instance):
    assert isinstance(instance, FromRange)

@given(instance=dom_InCollection_strategy)
@settings(max_examples=50)
def test_dom_incollection_instantiation(instance):
    assert isinstance(instance, dom_InCollection)



@given(instance=dom_InCollection_strategy)
def test_dom_incollection_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=dom_InCollection_strategy)
def test_dom_incollection_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=dom_InClass_strategy)
@settings(max_examples=50)
def test_dom_inclass_instantiation(instance):
    assert isinstance(instance, dom_InClass)



@given(instance=dom_InClass_strategy)
def test_dom_inclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=dom_InClass_strategy)
def test_dom_inclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_FromClass_strategy)
@settings(max_examples=50)
def test_dom_fromclass_instantiation(instance):
    assert isinstance(instance, dom_FromClass)



@given(instance=dom_FromClass_strategy)
def test_dom_fromclass_popertyFetch_setter(instance):
    original = instance.popertyFetch
    instance.popertyFetch = original
    assert instance.popertyFetch == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dom_CollectionFunction_strategy)
@settings(max_examples=50)
def test_dom_collectionfunction_instantiation(instance):
    assert isinstance(instance, dom_CollectionFunction)



@given(instance=dom_CollectionFunction_strategy)
def test_dom_collectionfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom_AggregateFunction_strategy)
@settings(max_examples=50)
def test_dom_aggregatefunction_instantiation(instance):
    assert isinstance(instance, dom_AggregateFunction)



@given(instance=dom_AggregateFunction_strategy)
def test_dom_aggregatefunction_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=dom_AggregateFunction_strategy)
def test_dom_aggregatefunction_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=dom_AggregateFunction_strategy)
def test_dom_aggregatefunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_AggregateFunction_strategy)
def test_dom_aggregatefunction_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=dom_FunctionCall_strategy)
@settings(max_examples=50)
def test_dom_functioncall_instantiation(instance):
    assert isinstance(instance, dom_FunctionCall)



@given(instance=dom_FunctionCall_strategy)
def test_dom_functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=dom_CastFunction_strategy)
@settings(max_examples=50)
def test_dom_castfunction_instantiation(instance):
    assert isinstance(instance, dom_CastFunction)



@given(instance=dom_CastFunction_strategy)
def test_dom_castfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_CastFunction_strategy)
def test_dom_castfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_JoinEntity_strategy)
@settings(max_examples=50)
def test_dom_joinentity_instantiation(instance):
    assert isinstance(instance, dom_JoinEntity)



@given(instance=dom_JoinEntity_strategy)
def test_dom_joinentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_InCollectionElements_strategy)
@settings(max_examples=50)
def test_dom_incollectionelements_instantiation(instance):
    assert isinstance(instance, dom_InCollectionElements)



@given(instance=dom_InCollectionElements_strategy)
def test_dom_incollectionelements_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=dom_InCollectionElements_strategy)
def test_dom_incollectionelements_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_PropertyValue_strategy)
@settings(max_examples=50)
def test_dom_propertyvalue_instantiation(instance):
    assert isinstance(instance, dom_PropertyValue)



@given(instance=dom_PropertyValue_strategy)
def test_dom_propertyvalue_classProperty_setter(instance):
    original = instance.classProperty
    instance.classProperty = original
    assert instance.classProperty == original



@given(instance=dom_PropertyValue_strategy)
def test_dom_propertyvalue_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original



@given(instance=dom_PropertyValue_strategy)
def test_dom_propertyvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_PropertyAssignment_strategy)
@settings(max_examples=50)
def test_dom_propertyassignment_instantiation(instance):
    assert isinstance(instance, dom_PropertyAssignment)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=dom_SelectObject_strategy)
@settings(max_examples=50)
def test_dom_selectobject_instantiation(instance):
    assert isinstance(instance, dom_SelectObject)



@given(instance=dom_SelectObject_strategy)
def test_dom_selectobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_SelectClass_strategy)
@settings(max_examples=50)
def test_dom_selectclass_instantiation(instance):
    assert isinstance(instance, dom_SelectClass)



@given(instance=dom_SelectClass_strategy)
def test_dom_selectclass_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dom_SelectProperties_strategy)
@settings(max_examples=50)
def test_dom_selectproperties_instantiation(instance):
    assert isinstance(instance, dom_SelectProperties)



@given(instance=dom_SelectProperties_strategy)
def test_dom_selectproperties_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=dom_SortOrderElement_strategy)
@settings(max_examples=50)
def test_dom_sortorderelement_instantiation(instance):
    assert isinstance(instance, dom_SortOrderElement)



@given(instance=dom_SortOrderElement_strategy)
def test_dom_sortorderelement_sortOrder_setter(instance):
    original = instance.sortOrder
    instance.sortOrder = original
    assert instance.sortOrder == original

@given(instance=dom_Join_strategy)
@settings(max_examples=50)
def test_dom_join_instantiation(instance):
    assert isinstance(instance, dom_Join)



@given(instance=dom_Join_strategy)
def test_dom_join_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=dom_Join_strategy)
def test_dom_join_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original



@given(instance=dom_Join_strategy)
def test_dom_join_propertyFetch_setter(instance):
    original = instance.propertyFetch
    instance.propertyFetch = original
    assert instance.propertyFetch == original

@given(instance=dom_FromRange_strategy)
@settings(max_examples=50)
def test_dom_fromrange_instantiation(instance):
    assert isinstance(instance, dom_FromRange)

@given(instance=dom_CallOutputParameter_strategy)
@settings(max_examples=50)
def test_dom_calloutputparameter_instantiation(instance):
    assert isinstance(instance, dom_CallOutputParameter)



@given(instance=dom_CallOutputParameter_strategy)
def test_dom_calloutputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_CallInputParameter_strategy)
@settings(max_examples=50)
def test_dom_callinputparameter_instantiation(instance):
    assert isinstance(instance, dom_CallInputParameter)



@given(instance=dom_CallInputParameter_strategy)
def test_dom_callinputparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QlStatement_strategy)
@settings(max_examples=50)
def test_qlstatement_instantiation(instance):
    assert isinstance(instance, QlStatement)

@given(instance=dom_InsertStatement_strategy)
@settings(max_examples=50)
def test_dom_insertstatement_instantiation(instance):
    assert isinstance(instance, dom_InsertStatement)

@given(instance=dom_UpdateStatement_strategy)
@settings(max_examples=50)
def test_dom_updatestatement_instantiation(instance):
    assert isinstance(instance, dom_UpdateStatement)



@given(instance=dom_UpdateStatement_strategy)
def test_dom_updatestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_UpdateStatement_strategy)
def test_dom_updatestatement_versioned_setter(instance):
    original = instance.versioned
    instance.versioned = original
    assert instance.versioned == original

@given(instance=dom_DeleteStatement_strategy)
@settings(max_examples=50)
def test_dom_deletestatement_instantiation(instance):
    assert isinstance(instance, dom_DeleteStatement)



@given(instance=dom_DeleteStatement_strategy)
def test_dom_deletestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_SelectStatement_strategy)
@settings(max_examples=50)
def test_dom_selectstatement_instantiation(instance):
    assert isinstance(instance, dom_SelectStatement)

@given(instance=dom_CallableStatement_strategy)
@settings(max_examples=50)
def test_dom_callablestatement_instantiation(instance):
    assert isinstance(instance, dom_CallableStatement)



@given(instance=dom_CallableStatement_strategy)
def test_dom_callablestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_CallableStatement_strategy)
def test_dom_callablestatement_functionCall_setter(instance):
    original = instance.functionCall
    instance.functionCall = original
    assert instance.functionCall == original

@given(instance=dom_Function_strategy)
@settings(max_examples=50)
def test_dom_function_instantiation(instance):
    assert isinstance(instance, dom_Function)

@given(instance=DaoFeature_strategy)
@settings(max_examples=50)
def test_daofeature_instantiation(instance):
    assert isinstance(instance, DaoFeature)

@given(instance=dom_SqlType_strategy)
@settings(max_examples=50)
def test_dom_sqltype_instantiation(instance):
    assert isinstance(instance, dom_SqlType)

@given(instance=dom_OneToOne_strategy)
@settings(max_examples=50)
def test_dom_onetoone_instantiation(instance):
    assert isinstance(instance, dom_OneToOne)

@given(instance=dom_ManyToOne_strategy)
@settings(max_examples=50)
def test_dom_manytoone_instantiation(instance):
    assert isinstance(instance, dom_ManyToOne)



@given(instance=dom_ManyToOne_strategy)
def test_dom_manytoone_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=dom_ManyToOne_strategy)
def test_dom_manytoone_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=dom_Column_strategy)
@settings(max_examples=50)
def test_dom_column_instantiation(instance):
    assert isinstance(instance, dom_Column)



@given(instance=dom_Column_strategy)
def test_dom_column_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom_DataBaseConstraint_strategy)
@settings(max_examples=50)
def test_dom_databaseconstraint_instantiation(instance):
    assert isinstance(instance, dom_DataBaseConstraint)



@given(instance=dom_DataBaseConstraint_strategy)
def test_dom_databaseconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_DataBaseConstraint_strategy)
def test_dom_databaseconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dom_QlStatement_strategy)
@settings(max_examples=50)
def test_dom_qlstatement_instantiation(instance):
    assert isinstance(instance, dom_QlStatement)

@given(instance=dom_QueryParameter_strategy)
@settings(max_examples=50)
def test_dom_queryparameter_instantiation(instance):
    assert isinstance(instance, dom_QueryParameter)

@given(instance=dom_ManyToMany_strategy)
@settings(max_examples=50)
def test_dom_manytomany_instantiation(instance):
    assert isinstance(instance, dom_ManyToMany)



@given(instance=dom_ManyToMany_strategy)
def test_dom_manytomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=dom_ManyToMany_strategy)
def test_dom_manytomany_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=dom_ManyToMany_strategy)
def test_dom_manytomany_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=dom_OneToMany_strategy)
@settings(max_examples=50)
def test_dom_onetomany_instantiation(instance):
    assert isinstance(instance, dom_OneToMany)



@given(instance=dom_OneToMany_strategy)
def test_dom_onetomany_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=dom_DaoFeature_strategy)
@settings(max_examples=50)
def test_dom_daofeature_instantiation(instance):
    assert isinstance(instance, dom_DaoFeature)

@given(instance=dom_AttributeSortOrder_strategy)
@settings(max_examples=50)
def test_dom_attributesortorder_instantiation(instance):
    assert isinstance(instance, dom_AttributeSortOrder)



@given(instance=dom_AttributeSortOrder_strategy)
def test_dom_attributesortorder_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=dom_AttributeSortOrder_strategy)
def test_dom_attributesortorder_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=dom_ValidatorReference_strategy)
@settings(max_examples=50)
def test_dom_validatorreference_instantiation(instance):
    assert isinstance(instance, dom_ValidatorReference)

@given(instance=dom_Constraint_strategy)
@settings(max_examples=50)
def test_dom_constraint_instantiation(instance):
    assert isinstance(instance, dom_Constraint)

@given(instance=dom_BoolLiteral_strategy)
@settings(max_examples=50)
def test_dom_boolliteral_instantiation(instance):
    assert isinstance(instance, dom_BoolLiteral)

@given(instance=ExpressionFlag_strategy)
@settings(max_examples=50)
def test_expressionflag_instantiation(instance):
    assert isinstance(instance, ExpressionFlag)

@given(instance=dom_ReadOnlyFlag_strategy)
@settings(max_examples=50)
def test_dom_readonlyflag_instantiation(instance):
    assert isinstance(instance, dom_ReadOnlyFlag)

@given(instance=dom_AvailableFlag_strategy)
@settings(max_examples=50)
def test_dom_availableflag_instantiation(instance):
    assert isinstance(instance, dom_AvailableFlag)

@given(instance=dom_RequiredFlag_strategy)
@settings(max_examples=50)
def test_dom_requiredflag_instantiation(instance):
    assert isinstance(instance, dom_RequiredFlag)

@given(instance=dom_EqualityExpr_strategy)
@settings(max_examples=50)
def test_dom_equalityexpr_instantiation(instance):
    assert isinstance(instance, dom_EqualityExpr)

@given(instance=AttributeFlag_strategy)
@settings(max_examples=50)
def test_attributeflag_instantiation(instance):
    assert isinstance(instance, AttributeFlag)

@given(instance=dom_TransientFlag_strategy)
@settings(max_examples=50)
def test_dom_transientflag_instantiation(instance):
    assert isinstance(instance, dom_TransientFlag)

@given(instance=dom_DerivedFlag_strategy)
@settings(max_examples=50)
def test_dom_derivedflag_instantiation(instance):
    assert isinstance(instance, dom_DerivedFlag)

@given(instance=dom_ExpressionFlag_strategy)
@settings(max_examples=50)
def test_dom_expressionflag_instantiation(instance):
    assert isinstance(instance, dom_ExpressionFlag)

@given(instance=AttributeProperty_strategy)
@settings(max_examples=50)
def test_attributeproperty_instantiation(instance):
    assert isinstance(instance, AttributeProperty)

@given(instance=dom_AttributeTextProperty_strategy)
@settings(max_examples=50)
def test_dom_attributetextproperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeTextProperty)



@given(instance=dom_AttributeTextProperty_strategy)
def test_dom_attributetextproperty_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_dom_attributetextproperty_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_dom_attributetextproperty_hstoreColumn_setter(instance):
    original = instance.hstoreColumn
    instance.hstoreColumn = original
    assert instance.hstoreColumn == original



@given(instance=dom_AttributeTextProperty_strategy)
def test_dom_attributetextproperty_unitText_setter(instance):
    original = instance.unitText
    instance.unitText = original
    assert instance.unitText == original

@given(instance=dom_AttributeValidationProperty_strategy)
@settings(max_examples=50)
def test_dom_attributevalidationproperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeValidationProperty)

@given(instance=dom_BetweenExpression_strategy)
@settings(max_examples=50)
def test_dom_betweenexpression_instantiation(instance):
    assert isinstance(instance, dom_BetweenExpression)



@given(instance=dom_BetweenExpression_strategy)
def test_dom_betweenexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=dom_BetweenExpression_strategy)
def test_dom_betweenexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dom_UnaryExpression_strategy)
@settings(max_examples=50)
def test_dom_unaryexpression_instantiation(instance):
    assert isinstance(instance, dom_UnaryExpression)



@given(instance=dom_UnaryExpression_strategy)
def test_dom_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom_MemberOfExpression_strategy)
@settings(max_examples=50)
def test_dom_memberofexpression_instantiation(instance):
    assert isinstance(instance, dom_MemberOfExpression)



@given(instance=dom_MemberOfExpression_strategy)
def test_dom_memberofexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_MemberOfExpression_strategy)
def test_dom_memberofexpression_memberOf_setter(instance):
    original = instance.memberOf
    instance.memberOf = original
    assert instance.memberOf == original



@given(instance=dom_MemberOfExpression_strategy)
def test_dom_memberofexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom_LikeExpression_strategy)
@settings(max_examples=50)
def test_dom_likeexpression_instantiation(instance):
    assert isinstance(instance, dom_LikeExpression)



@given(instance=dom_LikeExpression_strategy)
def test_dom_likeexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_LikeExpression_strategy)
def test_dom_likeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom_InExpression_strategy)
@settings(max_examples=50)
def test_dom_inexpression_instantiation(instance):
    assert isinstance(instance, dom_InExpression)



@given(instance=dom_InExpression_strategy)
def test_dom_inexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dom_InExpression_strategy)
def test_dom_inexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom_NotExpression_strategy)
@settings(max_examples=50)
def test_dom_notexpression_instantiation(instance):
    assert isinstance(instance, dom_NotExpression)

@given(instance=dom_BinaryExpression_strategy)
@settings(max_examples=50)
def test_dom_binaryexpression_instantiation(instance):
    assert isinstance(instance, dom_BinaryExpression)



@given(instance=dom_BinaryExpression_strategy)
def test_dom_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dom_AliasedExpression_strategy)
@settings(max_examples=50)
def test_dom_aliasedexpression_instantiation(instance):
    assert isinstance(instance, dom_AliasedExpression)



@given(instance=dom_AliasedExpression_strategy)
def test_dom_aliasedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_PresentableFeature_strategy)
@settings(max_examples=50)
def test_dom_presentablefeature_instantiation(instance):
    assert isinstance(instance, dom_PresentableFeature)



@given(instance=dom_PresentableFeature_strategy)
def test_dom_presentablefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_WhenClause_strategy)
@settings(max_examples=50)
def test_dom_whenclause_instantiation(instance):
    assert isinstance(instance, dom_WhenClause)

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=dom_RealLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_realliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_RealLiteralValue)



@given(instance=dom_RealLiteralValue_strategy)
def test_dom_realliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom_IntegerLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_integerliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_IntegerLiteralValue)



@given(instance=dom_IntegerLiteralValue_strategy)
def test_dom_integerliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom_EmptyLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_emptyliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_EmptyLiteralValue)

@given(instance=dom_NullLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_nullliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_NullLiteralValue)

@given(instance=dom_BooleanLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_booleanliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_BooleanLiteralValue)



@given(instance=dom_BooleanLiteralValue_strategy)
def test_dom_booleanliteralvalue_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=dom_LiteralValue_strategy)
@settings(max_examples=50)
def test_dom_literalvalue_instantiation(instance):
    assert isinstance(instance, dom_LiteralValue)

@given(instance=dom_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_dom_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, dom_ParenthesizedExpression)

@given(instance=dom_SubQuery_strategy)
@settings(max_examples=50)
def test_dom_subquery_instantiation(instance):
    assert isinstance(instance, dom_SubQuery)

@given(instance=dom_AltWhenClause_strategy)
@settings(max_examples=50)
def test_dom_altwhenclause_instantiation(instance):
    assert isinstance(instance, dom_AltWhenClause)

@given(instance=dom_StringLiteralValue_strategy)
@settings(max_examples=50)
def test_dom_stringliteralvalue_instantiation(instance):
    assert isinstance(instance, dom_StringLiteralValue)



@given(instance=dom_StringLiteralValue_strategy)
def test_dom_stringliteralvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dom_TrimFunction_strategy)
@settings(max_examples=50)
def test_dom_trimfunction_instantiation(instance):
    assert isinstance(instance, dom_TrimFunction)



@given(instance=dom_TrimFunction_strategy)
def test_dom_trimfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=dom_TrimFunction_strategy)
def test_dom_trimfunction_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=dom_CaseExpression_strategy)
@settings(max_examples=50)
def test_dom_caseexpression_instantiation(instance):
    assert isinstance(instance, dom_CaseExpression)

@given(instance=dom_QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_dom_quantifiedexpression_instantiation(instance):
    assert isinstance(instance, dom_QuantifiedExpression)



@given(instance=dom_QuantifiedExpression_strategy)
def test_dom_quantifiedexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original



@given(instance=dom_QuantifiedExpression_strategy)
def test_dom_quantifiedexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dom_QueryParameterValue_strategy)
@settings(max_examples=50)
def test_dom_queryparametervalue_instantiation(instance):
    assert isinstance(instance, dom_QueryParameterValue)

@given(instance=dom_QueryParameterReference_strategy)
@settings(max_examples=50)
def test_dom_queryparameterreference_instantiation(instance):
    assert isinstance(instance, dom_QueryParameterReference)

@given(instance=dom_AttributeFlag_strategy)
@settings(max_examples=50)
def test_dom_attributeflag_instantiation(instance):
    assert isinstance(instance, dom_AttributeFlag)

@given(instance=dom_IncrementerReference_strategy)
@settings(max_examples=50)
def test_dom_incrementerreference_instantiation(instance):
    assert isinstance(instance, dom_IncrementerReference)

@given(instance=dom_DataTypeAndTypeParameter_strategy)
@settings(max_examples=50)
def test_dom_datatypeandtypeparameter_instantiation(instance):
    assert isinstance(instance, dom_DataTypeAndTypeParameter)

@given(instance=dom_PropertyMapping_strategy)
@settings(max_examples=50)
def test_dom_propertymapping_instantiation(instance):
    assert isinstance(instance, dom_PropertyMapping)



@given(instance=dom_PropertyMapping_strategy)
def test_dom_propertymapping_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original



@given(instance=dom_PropertyMapping_strategy)
def test_dom_propertymapping_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original



@given(instance=dom_PropertyMapping_strategy)
def test_dom_propertymapping_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original

@given(instance=dom_ConditionsBlock_strategy)
@settings(max_examples=50)
def test_dom_conditionsblock_instantiation(instance):
    assert isinstance(instance, dom_ConditionsBlock)

@given(instance=PresentableFeature_strategy)
@settings(max_examples=50)
def test_presentablefeature_instantiation(instance):
    assert isinstance(instance, PresentableFeature)

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=dom_ValueObject_strategy)
@settings(max_examples=50)
def test_dom_valueobject_instantiation(instance):
    assert isinstance(instance, dom_ValueObject)

@given(instance=dom_AttributeProperty_strategy)
@settings(max_examples=50)
def test_dom_attributeproperty_instantiation(instance):
    assert isinstance(instance, dom_AttributeProperty)

@given(instance=dom_DataView_strategy)
@settings(max_examples=50)
def test_dom_dataview_instantiation(instance):
    assert isinstance(instance, dom_DataView)

@given(instance=dom_Type_strategy)
@settings(max_examples=50)
def test_dom_type_instantiation(instance):
    assert isinstance(instance, dom_Type)

@given(instance=QueryParameterReference_strategy)
@settings(max_examples=50)
def test_queryparameterreference_instantiation(instance):
    assert isinstance(instance, QueryParameterReference)

@given(instance=QueryParameter_strategy)
@settings(max_examples=50)
def test_queryparameter_instantiation(instance):
    assert isinstance(instance, QueryParameter)

@given(instance=dom_Expression_strategy)
@settings(max_examples=50)
def test_dom_expression_instantiation(instance):
    assert isinstance(instance, dom_Expression)

@given(instance=dom_DaoOperation_strategy)
@settings(max_examples=50)
def test_dom_daooperation_instantiation(instance):
    assert isinstance(instance, dom_DaoOperation)



@given(instance=dom_DaoOperation_strategy)
def test_dom_daooperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_DaoOperation_strategy)
def test_dom_daooperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=dom_Dependant_strategy)
@settings(max_examples=50)
def test_dom_dependant_instantiation(instance):
    assert isinstance(instance, dom_Dependant)

@given(instance=Dependant_strategy)
@settings(max_examples=50)
def test_dependant_instantiation(instance):
    assert isinstance(instance, Dependant)

@given(instance=dom_Entity_strategy)
@settings(max_examples=50)
def test_dom_entity_instantiation(instance):
    assert isinstance(instance, dom_Entity)

@given(instance=dom_Parameter_strategy)
@settings(max_examples=50)
def test_dom_parameter_instantiation(instance):
    assert isinstance(instance, dom_Parameter)



@given(instance=dom_Parameter_strategy)
def test_dom_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_Parameter_strategy)
def test_dom_parameter_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=DaoOperation_strategy)
@settings(max_examples=50)
def test_daooperation_instantiation(instance):
    assert isinstance(instance, DaoOperation)

@given(instance=dom_SimpleType_strategy)
@settings(max_examples=50)
def test_dom_simpletype_instantiation(instance):
    assert isinstance(instance, dom_SimpleType)

@given(instance=IDocumentable_strategy)
@settings(max_examples=50)
def test_idocumentable_instantiation(instance):
    assert isinstance(instance, IDocumentable)

@given(instance=dom_FeatureReference_strategy)
@settings(max_examples=50)
def test_dom_featurereference_instantiation(instance):
    assert isinstance(instance, dom_FeatureReference)



@given(instance=dom_FeatureReference_strategy)
def test_dom_featurereference_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=dom_AttributeGroup_strategy)
@settings(max_examples=50)
def test_dom_attributegroup_instantiation(instance):
    assert isinstance(instance, dom_AttributeGroup)



@given(instance=dom_AttributeGroup_strategy)
def test_dom_attributegroup_sortorder_setter(instance):
    original = instance.sortorder
    instance.sortorder = original
    assert instance.sortorder == original



@given(instance=dom_AttributeGroup_strategy)
def test_dom_attributegroup_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=dom_AttributeGroup_strategy)
def test_dom_attributegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_AttributeGroup_strategy)
def test_dom_attributegroup_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=dom_AttributeGroup_strategy)
def test_dom_attributegroup_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=dom_Operation_strategy)
@settings(max_examples=50)
def test_dom_operation_instantiation(instance):
    assert isinstance(instance, dom_Operation)



@given(instance=dom_Operation_strategy)
def test_dom_operation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=dom_QueryOperation_strategy)
@settings(max_examples=50)
def test_dom_queryoperation_instantiation(instance):
    assert isinstance(instance, dom_QueryOperation)

@given(instance=dom_DelegateOperation_strategy)
@settings(max_examples=50)
def test_dom_delegateoperation_instantiation(instance):
    assert isinstance(instance, dom_DelegateOperation)



@given(instance=dom_DelegateOperation_strategy)
def test_dom_delegateoperation_crudOperationType_setter(instance):
    original = instance.crudOperationType
    instance.crudOperationType = original
    assert instance.crudOperationType == original



@given(instance=dom_DelegateOperation_strategy)
def test_dom_delegateoperation_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=dom_DelegateOperation_strategy)
def test_dom_delegateoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ReferenceableByXmadslVariable_strategy)
@settings(max_examples=50)
def test_referenceablebyxmadslvariable_instantiation(instance):
    assert isinstance(instance, ReferenceableByXmadslVariable)

@given(instance=dom_IElementWithNoName_strategy)
@settings(max_examples=50)
def test_dom_ielementwithnoname_instantiation(instance):
    assert isinstance(instance, dom_IElementWithNoName)



@given(instance=dom_IElementWithNoName_strategy)
def test_dom_ielementwithnoname_noName_setter(instance):
    original = instance.noName
    instance.noName = original
    assert instance.noName == original

@given(instance=dom_Property_strategy)
@settings(max_examples=50)
def test_dom_property_instantiation(instance):
    assert isinstance(instance, dom_Property)



@given(instance=dom_Property_strategy)
def test_dom_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dom_Property_strategy)
def test_dom_property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=dom_Attribute_strategy)
@settings(max_examples=50)
def test_dom_attribute_instantiation(instance):
    assert isinstance(instance, dom_Attribute)



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=dom_Attribute_strategy)
def test_dom_attribute_dataTypeName_setter(instance):
    original = instance.dataTypeName
    instance.dataTypeName = original
    assert instance.dataTypeName == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=dom_ApplicationSession_strategy)
@settings(max_examples=50)
def test_dom_applicationsession_instantiation(instance):
    assert isinstance(instance, dom_ApplicationSession)

@given(instance=dom_Mapper_strategy)
@settings(max_examples=50)
def test_dom_mapper_instantiation(instance):
    assert isinstance(instance, dom_Mapper)



@given(instance=dom_Mapper_strategy)
def test_dom_mapper_toLeft_setter(instance):
    original = instance.toLeft
    instance.toLeft = original
    assert instance.toLeft == original



@given(instance=dom_Mapper_strategy)
def test_dom_mapper_toRight_setter(instance):
    original = instance.toRight
    instance.toRight = original
    assert instance.toRight == original



@given(instance=dom_Mapper_strategy)
def test_dom_mapper_biDirectional_setter(instance):
    original = instance.biDirectional
    instance.biDirectional = original
    assert instance.biDirectional == original

@given(instance=dom_Dao_strategy)
@settings(max_examples=50)
def test_dom_dao_instantiation(instance):
    assert isinstance(instance, dom_Dao)



@given(instance=dom_Dao_strategy)
def test_dom_dao_discriminator_setter(instance):
    original = instance.discriminator
    instance.discriminator = original
    assert instance.discriminator == original



@given(instance=dom_Dao_strategy)
def test_dom_dao_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=dom_Dao_strategy)
def test_dom_dao_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=dom_Service_strategy)
@settings(max_examples=50)
def test_dom_service_instantiation(instance):
    assert isinstance(instance, dom_Service)

@given(instance=dom_ComplexType_strategy)
@settings(max_examples=50)
def test_dom_complextype_instantiation(instance):
    assert isinstance(instance, dom_ComplexType)
