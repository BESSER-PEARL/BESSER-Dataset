import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OrderedCollection,
    eol_expression_SequenceExpression,
    eol_expression_Statement,
    CollectionInitialisationExpression,
    eol_expression_ExpressionList,
    eol_expression_ExpressionRange,
    UniqueCollection,
    eol_expression_OrderedSetExpression,
    eol_expression_SetExpression,
    CollectionExpression,
    eol_expression_UniqueCollection,
    eol_expression_OrderedCollection,
    eol_expression_BagExpression,
    SummableExpression,
    ComparableExpression,
    eol_expression_RealExpression,
    eol_expression_IntegerExpression,
    eol_expression_StringExpression,
    PrimitiveExpression,
    eol_expression_SummableExpression,
    eol_expression_BooleanExpression,
    eol_expression_ComparableExpression,
    ArithmeticOperatorExpression,
    eol_expression_MinusOperatorExpression,
    eol_expression_MultiplyOperatorExpression,
    eol_expression_DivideOperatorExpression,
    FeatureCallExpression,
    eol_expression_FOLMethodCallExpression,
    eol_expression_PropertyCallExpression,
    eol_expression_MethodCallExpression,
    VariableDeclarationExpression,
    eol_expression_FormalParameterExpression,
    ComparisonOperatorExpression,
    eol_expression_GreaterThanOperatorExpression,
    eol_expression_LessThanOrEqualToOperatorExpression,
    eol_expression_NotEqualsOperatorExpression,
    eol_expression_EqualsOperatorExpression,
    eol_expression_LessThanOperatorExpression,
    eol_expression_GreaterThanOrEqualToOperatorExpression,
    eol_expression_PlusOperatorExpression,
    LogicalOperatorExpression,
    eol_expression_XorOperatorExpression,
    eol_expression_OrOperatorExpression,
    eol_expression_ImpliesOperatorExpression,
    eol_expression_AndOperatorExpression,
    BinaryOperatorExpression,
    eol_expression_ComparisonOperatorExpression,
    eol_expression_ArithmeticOperatorExpression,
    eol_expression_LogicalOperatorExpression,
    UnaryOperatorExpression,
    eol_expression_NegativeOperatorExpression,
    eol_expression_NotOperatorExpression,
    OperatorExpression,
    eol_expression_BinaryOperatorExpression,
    eol_expression_UnaryOperatorExpression,
    Expression,
    eol_expression_EnumerationLiteralExpression,
    eol_expression_NameExpression,
    eol_expression_KeyValueExpression,
    eol_expression_NewExpression,
    eol_expression_VariableDeclarationExpression,
    eol_expression_CollectionInitialisationExpression,
    eol_expression_MapExpression,
    eol_expression_FeatureCallExpression,
    eol_expression_CollectionExpression,
    eol_expression_PrimitiveExpression,
    eol_expression_OperatorExpression,
    eol_expression_Type,
    eol_expression_Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(OrderedCollection)


def test_orderedcollection_constructor_exists():
    assert callable(OrderedCollection.__init__)


def test_orderedcollection_constructor_args():
    sig = inspect.signature(OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_SequenceExpression)


def test_eol_expression_sequenceexpression_constructor_exists():
    assert callable(eol_expression_SequenceExpression.__init__)


def test_eol_expression_sequenceexpression_constructor_args():
    sig = inspect.signature(eol_expression_SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_statement_is_not_abstract():
    assert not inspect.isabstract(eol_expression_Statement)


def test_eol_expression_statement_constructor_exists():
    assert callable(eol_expression_Statement.__init__)


def test_eol_expression_statement_constructor_args():
    sig = inspect.signature(eol_expression_Statement.__init__)
    params = list(sig.parameters.keys())



def test_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionInitialisationExpression)


def test_collectioninitialisationexpression_constructor_exists():
    assert callable(CollectionInitialisationExpression.__init__)


def test_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_expressionlist_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ExpressionList)


def test_eol_expression_expressionlist_constructor_exists():
    assert callable(eol_expression_ExpressionList.__init__)


def test_eol_expression_expressionlist_constructor_args():
    sig = inspect.signature(eol_expression_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_expressionrange_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ExpressionRange)


def test_eol_expression_expressionrange_constructor_exists():
    assert callable(eol_expression_ExpressionRange.__init__)


def test_eol_expression_expressionrange_constructor_args():
    sig = inspect.signature(eol_expression_ExpressionRange.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(UniqueCollection)


def test_uniquecollection_constructor_exists():
    assert callable(UniqueCollection.__init__)


def test_uniquecollection_constructor_args():
    sig = inspect.signature(UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_OrderedSetExpression)


def test_eol_expression_orderedsetexpression_constructor_exists():
    assert callable(eol_expression_OrderedSetExpression.__init__)


def test_eol_expression_orderedsetexpression_constructor_args():
    sig = inspect.signature(eol_expression_OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_setexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_SetExpression)


def test_eol_expression_setexpression_constructor_exists():
    assert callable(eol_expression_SetExpression.__init__)


def test_eol_expression_setexpression_constructor_args():
    sig = inspect.signature(eol_expression_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(eol_expression_UniqueCollection)


def test_eol_expression_uniquecollection_constructor_exists():
    assert callable(eol_expression_UniqueCollection.__init__)


def test_eol_expression_uniquecollection_constructor_args():
    sig = inspect.signature(eol_expression_UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(eol_expression_OrderedCollection)


def test_eol_expression_orderedcollection_constructor_exists():
    assert callable(eol_expression_OrderedCollection.__init__)


def test_eol_expression_orderedcollection_constructor_args():
    sig = inspect.signature(eol_expression_OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_BagExpression)


def test_eol_expression_bagexpression_constructor_exists():
    assert callable(eol_expression_BagExpression.__init__)


def test_eol_expression_bagexpression_constructor_args():
    sig = inspect.signature(eol_expression_BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_summableexpression_is_not_abstract():
    assert not inspect.isabstract(SummableExpression)


def test_summableexpression_constructor_exists():
    assert callable(SummableExpression.__init__)


def test_summableexpression_constructor_args():
    sig = inspect.signature(SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(ComparableExpression)


def test_comparableexpression_constructor_exists():
    assert callable(ComparableExpression.__init__)


def test_comparableexpression_constructor_args():
    sig = inspect.signature(ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_realexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_RealExpression)


def test_eol_expression_realexpression_constructor_exists():
    assert callable(eol_expression_RealExpression.__init__)


def test_eol_expression_realexpression_constructor_args():
    sig = inspect.signature(eol_expression_RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_expression_realexpression_has_value():
    assert hasattr(eol_expression_RealExpression, "value")
    descriptor = None
    for klass in eol_expression_RealExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_IntegerExpression)


def test_eol_expression_integerexpression_constructor_exists():
    assert callable(eol_expression_IntegerExpression.__init__)


def test_eol_expression_integerexpression_constructor_args():
    sig = inspect.signature(eol_expression_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_expression_integerexpression_has_value():
    assert hasattr(eol_expression_IntegerExpression, "value")
    descriptor = None
    for klass in eol_expression_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_StringExpression)


def test_eol_expression_stringexpression_constructor_exists():
    assert callable(eol_expression_StringExpression.__init__)


def test_eol_expression_stringexpression_constructor_args():
    sig = inspect.signature(eol_expression_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_expression_stringexpression_has_value():
    assert hasattr(eol_expression_StringExpression, "value")
    descriptor = None
    for klass in eol_expression_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_summableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_SummableExpression)


def test_eol_expression_summableexpression_constructor_exists():
    assert callable(eol_expression_SummableExpression.__init__)


def test_eol_expression_summableexpression_constructor_args():
    sig = inspect.signature(eol_expression_SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_BooleanExpression)


def test_eol_expression_booleanexpression_constructor_exists():
    assert callable(eol_expression_BooleanExpression.__init__)


def test_eol_expression_booleanexpression_constructor_args():
    sig = inspect.signature(eol_expression_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_expression_booleanexpression_has_value():
    assert hasattr(eol_expression_BooleanExpression, "value")
    descriptor = None
    for klass in eol_expression_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ComparableExpression)


def test_eol_expression_comparableexpression_constructor_exists():
    assert callable(eol_expression_ComparableExpression.__init__)


def test_eol_expression_comparableexpression_constructor_args():
    sig = inspect.signature(eol_expression_ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_MinusOperatorExpression)


def test_eol_expression_minusoperatorexpression_constructor_exists():
    assert callable(eol_expression_MinusOperatorExpression.__init__)


def test_eol_expression_minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_MultiplyOperatorExpression)


def test_eol_expression_multiplyoperatorexpression_constructor_exists():
    assert callable(eol_expression_MultiplyOperatorExpression.__init__)


def test_eol_expression_multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_DivideOperatorExpression)


def test_eol_expression_divideoperatorexpression_constructor_exists():
    assert callable(eol_expression_DivideOperatorExpression.__init__)


def test_eol_expression_divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_FOLMethodCallExpression)


def test_eol_expression_folmethodcallexpression_constructor_exists():
    assert callable(eol_expression_FOLMethodCallExpression.__init__)


def test_eol_expression_folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol_expression_FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_PropertyCallExpression)


def test_eol_expression_propertycallexpression_constructor_exists():
    assert callable(eol_expression_PropertyCallExpression.__init__)


def test_eol_expression_propertycallexpression_constructor_args():
    sig = inspect.signature(eol_expression_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "extended" in params, "Missing parameter 'extended'"

def test_eol_expression_propertycallexpression_has_extended():
    assert hasattr(eol_expression_PropertyCallExpression, "extended")
    descriptor = None
    for klass in eol_expression_PropertyCallExpression.__mro__:
        if "extended" in klass.__dict__:
            descriptor = klass.__dict__["extended"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_MethodCallExpression)


def test_eol_expression_methodcallexpression_constructor_exists():
    assert callable(eol_expression_MethodCallExpression.__init__)


def test_eol_expression_methodcallexpression_constructor_args():
    sig = inspect.signature(eol_expression_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_FormalParameterExpression)


def test_eol_expression_formalparameterexpression_constructor_exists():
    assert callable(eol_expression_FormalParameterExpression.__init__)


def test_eol_expression_formalparameterexpression_constructor_args():
    sig = inspect.signature(eol_expression_FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_GreaterThanOperatorExpression)


def test_eol_expression_greaterthanoperatorexpression_constructor_exists():
    assert callable(eol_expression_GreaterThanOperatorExpression.__init__)


def test_eol_expression_greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_LessThanOrEqualToOperatorExpression)


def test_eol_expression_lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_expression_LessThanOrEqualToOperatorExpression.__init__)


def test_eol_expression_lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_NotEqualsOperatorExpression)


def test_eol_expression_notequalsoperatorexpression_constructor_exists():
    assert callable(eol_expression_NotEqualsOperatorExpression.__init__)


def test_eol_expression_notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_EqualsOperatorExpression)


def test_eol_expression_equalsoperatorexpression_constructor_exists():
    assert callable(eol_expression_EqualsOperatorExpression.__init__)


def test_eol_expression_equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_LessThanOperatorExpression)


def test_eol_expression_lessthanoperatorexpression_constructor_exists():
    assert callable(eol_expression_LessThanOperatorExpression.__init__)


def test_eol_expression_lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_GreaterThanOrEqualToOperatorExpression)


def test_eol_expression_greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_expression_GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol_expression_greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_PlusOperatorExpression)


def test_eol_expression_plusoperatorexpression_constructor_exists():
    assert callable(eol_expression_PlusOperatorExpression.__init__)


def test_eol_expression_plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_XorOperatorExpression)


def test_eol_expression_xoroperatorexpression_constructor_exists():
    assert callable(eol_expression_XorOperatorExpression.__init__)


def test_eol_expression_xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_OrOperatorExpression)


def test_eol_expression_oroperatorexpression_constructor_exists():
    assert callable(eol_expression_OrOperatorExpression.__init__)


def test_eol_expression_oroperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ImpliesOperatorExpression)


def test_eol_expression_impliesoperatorexpression_constructor_exists():
    assert callable(eol_expression_ImpliesOperatorExpression.__init__)


def test_eol_expression_impliesoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_AndOperatorExpression)


def test_eol_expression_andoperatorexpression_constructor_exists():
    assert callable(eol_expression_AndOperatorExpression.__init__)


def test_eol_expression_andoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ComparisonOperatorExpression)


def test_eol_expression_comparisonoperatorexpression_constructor_exists():
    assert callable(eol_expression_ComparisonOperatorExpression.__init__)


def test_eol_expression_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_ArithmeticOperatorExpression)


def test_eol_expression_arithmeticoperatorexpression_constructor_exists():
    assert callable(eol_expression_ArithmeticOperatorExpression.__init__)


def test_eol_expression_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_LogicalOperatorExpression)


def test_eol_expression_logicaloperatorexpression_constructor_exists():
    assert callable(eol_expression_LogicalOperatorExpression.__init__)


def test_eol_expression_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_NegativeOperatorExpression)


def test_eol_expression_negativeoperatorexpression_constructor_exists():
    assert callable(eol_expression_NegativeOperatorExpression.__init__)


def test_eol_expression_negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_NotOperatorExpression)


def test_eol_expression_notoperatorexpression_constructor_exists():
    assert callable(eol_expression_NotOperatorExpression.__init__)


def test_eol_expression_notoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_BinaryOperatorExpression)


def test_eol_expression_binaryoperatorexpression_constructor_exists():
    assert callable(eol_expression_BinaryOperatorExpression.__init__)


def test_eol_expression_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_UnaryOperatorExpression)


def test_eol_expression_unaryoperatorexpression_constructor_exists():
    assert callable(eol_expression_UnaryOperatorExpression.__init__)


def test_eol_expression_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_EnumerationLiteralExpression)


def test_eol_expression_enumerationliteralexpression_constructor_exists():
    assert callable(eol_expression_EnumerationLiteralExpression.__init__)


def test_eol_expression_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol_expression_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_NameExpression)


def test_eol_expression_nameexpression_constructor_exists():
    assert callable(eol_expression_NameExpression.__init__)


def test_eol_expression_nameexpression_constructor_args():
    sig = inspect.signature(eol_expression_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isType" in params, "Missing parameter 'isType'"
    assert "name" in params, "Missing parameter 'name'"

def test_eol_expression_nameexpression_has_isType():
    assert hasattr(eol_expression_NameExpression, "isType")
    descriptor = None
    for klass in eol_expression_NameExpression.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)

def test_eol_expression_nameexpression_has_name():
    assert hasattr(eol_expression_NameExpression, "name")
    descriptor = None
    for klass in eol_expression_NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_KeyValueExpression)


def test_eol_expression_keyvalueexpression_constructor_exists():
    assert callable(eol_expression_KeyValueExpression.__init__)


def test_eol_expression_keyvalueexpression_constructor_args():
    sig = inspect.signature(eol_expression_KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_newexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_NewExpression)


def test_eol_expression_newexpression_constructor_exists():
    assert callable(eol_expression_NewExpression.__init__)


def test_eol_expression_newexpression_constructor_args():
    sig = inspect.signature(eol_expression_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_VariableDeclarationExpression)


def test_eol_expression_variabledeclarationexpression_constructor_exists():
    assert callable(eol_expression_VariableDeclarationExpression.__init__)


def test_eol_expression_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol_expression_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "create" in params, "Missing parameter 'create'"

def test_eol_expression_variabledeclarationexpression_has_create():
    assert hasattr(eol_expression_VariableDeclarationExpression, "create")
    descriptor = None
    for klass in eol_expression_VariableDeclarationExpression.__mro__:
        if "create" in klass.__dict__:
            descriptor = klass.__dict__["create"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_CollectionInitialisationExpression)


def test_eol_expression_collectioninitialisationexpression_constructor_exists():
    assert callable(eol_expression_CollectionInitialisationExpression.__init__)


def test_eol_expression_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(eol_expression_CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_MapExpression)


def test_eol_expression_mapexpression_constructor_exists():
    assert callable(eol_expression_MapExpression.__init__)


def test_eol_expression_mapexpression_constructor_args():
    sig = inspect.signature(eol_expression_MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_FeatureCallExpression)


def test_eol_expression_featurecallexpression_constructor_exists():
    assert callable(eol_expression_FeatureCallExpression.__init__)


def test_eol_expression_featurecallexpression_constructor_args():
    sig = inspect.signature(eol_expression_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arrow" in params, "Missing parameter 'arrow'"

def test_eol_expression_featurecallexpression_has_arrow():
    assert hasattr(eol_expression_FeatureCallExpression, "arrow")
    descriptor = None
    for klass in eol_expression_FeatureCallExpression.__mro__:
        if "arrow" in klass.__dict__:
            descriptor = klass.__dict__["arrow"]
            break
    assert isinstance(descriptor, property)



def test_eol_expression_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_CollectionExpression)


def test_eol_expression_collectionexpression_constructor_exists():
    assert callable(eol_expression_CollectionExpression.__init__)


def test_eol_expression_collectionexpression_constructor_args():
    sig = inspect.signature(eol_expression_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_PrimitiveExpression)


def test_eol_expression_primitiveexpression_constructor_exists():
    assert callable(eol_expression_PrimitiveExpression.__init__)


def test_eol_expression_primitiveexpression_constructor_args():
    sig = inspect.signature(eol_expression_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_OperatorExpression)


def test_eol_expression_operatorexpression_constructor_exists():
    assert callable(eol_expression_OperatorExpression.__init__)


def test_eol_expression_operatorexpression_constructor_args():
    sig = inspect.signature(eol_expression_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_type_is_not_abstract():
    assert not inspect.isabstract(eol_expression_Type)


def test_eol_expression_type_constructor_exists():
    assert callable(eol_expression_Type.__init__)


def test_eol_expression_type_constructor_args():
    sig = inspect.signature(eol_expression_Type.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_expression_is_not_abstract():
    assert not inspect.isabstract(eol_expression_Expression)


def test_eol_expression_expression_constructor_exists():
    assert callable(eol_expression_Expression.__init__)


def test_eol_expression_expression_constructor_args():
    sig = inspect.signature(eol_expression_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "inBrackets" in params, "Missing parameter 'inBrackets'"

def test_eol_expression_expression_has_inBrackets():
    assert hasattr(eol_expression_Expression, "inBrackets")
    descriptor = None
    for klass in eol_expression_Expression.__mro__:
        if "inBrackets" in klass.__dict__:
            descriptor = klass.__dict__["inBrackets"]
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
OrderedCollection_strategy = st.builds(
    OrderedCollection,
)
eol_expression_SequenceExpression_strategy = st.builds(
    eol_expression_SequenceExpression,
)
eol_expression_Statement_strategy = st.builds(
    eol_expression_Statement,
)
CollectionInitialisationExpression_strategy = st.builds(
    CollectionInitialisationExpression,
)
eol_expression_ExpressionList_strategy = st.builds(
    eol_expression_ExpressionList,
)
eol_expression_ExpressionRange_strategy = st.builds(
    eol_expression_ExpressionRange,
)
UniqueCollection_strategy = st.builds(
    UniqueCollection,
)
eol_expression_OrderedSetExpression_strategy = st.builds(
    eol_expression_OrderedSetExpression,
)
eol_expression_SetExpression_strategy = st.builds(
    eol_expression_SetExpression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol_expression_UniqueCollection_strategy = st.builds(
    eol_expression_UniqueCollection,
)
eol_expression_OrderedCollection_strategy = st.builds(
    eol_expression_OrderedCollection,
)
eol_expression_BagExpression_strategy = st.builds(
    eol_expression_BagExpression,
)
SummableExpression_strategy = st.builds(
    SummableExpression,
)
ComparableExpression_strategy = st.builds(
    ComparableExpression,
)
eol_expression_RealExpression_strategy = st.builds(
    eol_expression_RealExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol_expression_IntegerExpression_strategy = st.builds(
    eol_expression_IntegerExpression,
    value=
        st.integers()
)
eol_expression_StringExpression_strategy = st.builds(
    eol_expression_StringExpression,
    value=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol_expression_SummableExpression_strategy = st.builds(
    eol_expression_SummableExpression,
)
eol_expression_BooleanExpression_strategy = st.builds(
    eol_expression_BooleanExpression,
    value=
        st.booleans()
)
eol_expression_ComparableExpression_strategy = st.builds(
    eol_expression_ComparableExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol_expression_MinusOperatorExpression_strategy = st.builds(
    eol_expression_MinusOperatorExpression,
)
eol_expression_MultiplyOperatorExpression_strategy = st.builds(
    eol_expression_MultiplyOperatorExpression,
)
eol_expression_DivideOperatorExpression_strategy = st.builds(
    eol_expression_DivideOperatorExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol_expression_FOLMethodCallExpression_strategy = st.builds(
    eol_expression_FOLMethodCallExpression,
)
eol_expression_PropertyCallExpression_strategy = st.builds(
    eol_expression_PropertyCallExpression,
    extended=
        st.booleans()
)
eol_expression_MethodCallExpression_strategy = st.builds(
    eol_expression_MethodCallExpression,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
eol_expression_FormalParameterExpression_strategy = st.builds(
    eol_expression_FormalParameterExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol_expression_GreaterThanOperatorExpression_strategy = st.builds(
    eol_expression_GreaterThanOperatorExpression,
)
eol_expression_LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_expression_LessThanOrEqualToOperatorExpression,
)
eol_expression_NotEqualsOperatorExpression_strategy = st.builds(
    eol_expression_NotEqualsOperatorExpression,
)
eol_expression_EqualsOperatorExpression_strategy = st.builds(
    eol_expression_EqualsOperatorExpression,
)
eol_expression_LessThanOperatorExpression_strategy = st.builds(
    eol_expression_LessThanOperatorExpression,
)
eol_expression_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_expression_GreaterThanOrEqualToOperatorExpression,
)
eol_expression_PlusOperatorExpression_strategy = st.builds(
    eol_expression_PlusOperatorExpression,
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol_expression_XorOperatorExpression_strategy = st.builds(
    eol_expression_XorOperatorExpression,
)
eol_expression_OrOperatorExpression_strategy = st.builds(
    eol_expression_OrOperatorExpression,
)
eol_expression_ImpliesOperatorExpression_strategy = st.builds(
    eol_expression_ImpliesOperatorExpression,
)
eol_expression_AndOperatorExpression_strategy = st.builds(
    eol_expression_AndOperatorExpression,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol_expression_ComparisonOperatorExpression_strategy = st.builds(
    eol_expression_ComparisonOperatorExpression,
)
eol_expression_ArithmeticOperatorExpression_strategy = st.builds(
    eol_expression_ArithmeticOperatorExpression,
)
eol_expression_LogicalOperatorExpression_strategy = st.builds(
    eol_expression_LogicalOperatorExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol_expression_NegativeOperatorExpression_strategy = st.builds(
    eol_expression_NegativeOperatorExpression,
)
eol_expression_NotOperatorExpression_strategy = st.builds(
    eol_expression_NotOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol_expression_BinaryOperatorExpression_strategy = st.builds(
    eol_expression_BinaryOperatorExpression,
)
eol_expression_UnaryOperatorExpression_strategy = st.builds(
    eol_expression_UnaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol_expression_EnumerationLiteralExpression_strategy = st.builds(
    eol_expression_EnumerationLiteralExpression,
)
eol_expression_NameExpression_strategy = st.builds(
    eol_expression_NameExpression,
    isType=
        st.booleans(),
    name=
        safe_text
)
eol_expression_KeyValueExpression_strategy = st.builds(
    eol_expression_KeyValueExpression,
)
eol_expression_NewExpression_strategy = st.builds(
    eol_expression_NewExpression,
)
eol_expression_VariableDeclarationExpression_strategy = st.builds(
    eol_expression_VariableDeclarationExpression,
    create=
        st.booleans()
)
eol_expression_CollectionInitialisationExpression_strategy = st.builds(
    eol_expression_CollectionInitialisationExpression,
)
eol_expression_MapExpression_strategy = st.builds(
    eol_expression_MapExpression,
)
eol_expression_FeatureCallExpression_strategy = st.builds(
    eol_expression_FeatureCallExpression,
    arrow=
        st.booleans()
)
eol_expression_CollectionExpression_strategy = st.builds(
    eol_expression_CollectionExpression,
)
eol_expression_PrimitiveExpression_strategy = st.builds(
    eol_expression_PrimitiveExpression,
)
eol_expression_OperatorExpression_strategy = st.builds(
    eol_expression_OperatorExpression,
)
eol_expression_Type_strategy = st.builds(
    eol_expression_Type,
)
eol_expression_Expression_strategy = st.builds(
    eol_expression_Expression,
    inBrackets=
        st.booleans()
)

@given(instance=OrderedCollection_strategy)
@settings(max_examples=50)
def test_orderedcollection_instantiation(instance):
    assert isinstance(instance, OrderedCollection)

@given(instance=eol_expression_SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_SequenceExpression)

@given(instance=eol_expression_Statement_strategy)
@settings(max_examples=50)
def test_eol_expression_statement_instantiation(instance):
    assert isinstance(instance, eol_expression_Statement)

@given(instance=CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, CollectionInitialisationExpression)

@given(instance=eol_expression_ExpressionList_strategy)
@settings(max_examples=50)
def test_eol_expression_expressionlist_instantiation(instance):
    assert isinstance(instance, eol_expression_ExpressionList)

@given(instance=eol_expression_ExpressionRange_strategy)
@settings(max_examples=50)
def test_eol_expression_expressionrange_instantiation(instance):
    assert isinstance(instance, eol_expression_ExpressionRange)

@given(instance=UniqueCollection_strategy)
@settings(max_examples=50)
def test_uniquecollection_instantiation(instance):
    assert isinstance(instance, UniqueCollection)

@given(instance=eol_expression_OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_OrderedSetExpression)

@given(instance=eol_expression_SetExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_setexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_SetExpression)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol_expression_UniqueCollection_strategy)
@settings(max_examples=50)
def test_eol_expression_uniquecollection_instantiation(instance):
    assert isinstance(instance, eol_expression_UniqueCollection)

@given(instance=eol_expression_OrderedCollection_strategy)
@settings(max_examples=50)
def test_eol_expression_orderedcollection_instantiation(instance):
    assert isinstance(instance, eol_expression_OrderedCollection)

@given(instance=eol_expression_BagExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_bagexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_BagExpression)

@given(instance=SummableExpression_strategy)
@settings(max_examples=50)
def test_summableexpression_instantiation(instance):
    assert isinstance(instance, SummableExpression)

@given(instance=ComparableExpression_strategy)
@settings(max_examples=50)
def test_comparableexpression_instantiation(instance):
    assert isinstance(instance, ComparableExpression)

@given(instance=eol_expression_RealExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_realexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_RealExpression)



@given(instance=eol_expression_RealExpression_strategy)
def test_eol_expression_realexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_expression_IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_integerexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_IntegerExpression)



@given(instance=eol_expression_IntegerExpression_strategy)
def test_eol_expression_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_expression_StringExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_stringexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_StringExpression)



@given(instance=eol_expression_StringExpression_strategy)
def test_eol_expression_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol_expression_SummableExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_summableexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_SummableExpression)

@given(instance=eol_expression_BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_booleanexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_BooleanExpression)



@given(instance=eol_expression_BooleanExpression_strategy)
def test_eol_expression_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_expression_ComparableExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_comparableexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_ComparableExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol_expression_MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_MinusOperatorExpression)

@given(instance=eol_expression_MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_MultiplyOperatorExpression)

@given(instance=eol_expression_DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_DivideOperatorExpression)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol_expression_FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_FOLMethodCallExpression)

@given(instance=eol_expression_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_PropertyCallExpression)



@given(instance=eol_expression_PropertyCallExpression_strategy)
def test_eol_expression_propertycallexpression_extended_setter(instance):
    original = instance.extended
    instance.extended = original
    assert instance.extended == original

@given(instance=eol_expression_MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_MethodCallExpression)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=eol_expression_FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_FormalParameterExpression)

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol_expression_GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_GreaterThanOperatorExpression)

@given(instance=eol_expression_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_LessThanOrEqualToOperatorExpression)

@given(instance=eol_expression_NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_NotEqualsOperatorExpression)

@given(instance=eol_expression_EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_EqualsOperatorExpression)

@given(instance=eol_expression_LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_LessThanOperatorExpression)

@given(instance=eol_expression_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_GreaterThanOrEqualToOperatorExpression)

@given(instance=eol_expression_PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_PlusOperatorExpression)

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol_expression_XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_XorOperatorExpression)

@given(instance=eol_expression_OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_OrOperatorExpression)

@given(instance=eol_expression_ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_ImpliesOperatorExpression)

@given(instance=eol_expression_AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_AndOperatorExpression)

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol_expression_ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_ComparisonOperatorExpression)

@given(instance=eol_expression_ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_ArithmeticOperatorExpression)

@given(instance=eol_expression_LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_LogicalOperatorExpression)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol_expression_NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_NegativeOperatorExpression)

@given(instance=eol_expression_NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_NotOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=eol_expression_BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_BinaryOperatorExpression)

@given(instance=eol_expression_UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_UnaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol_expression_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_EnumerationLiteralExpression)

@given(instance=eol_expression_NameExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_nameexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_NameExpression)



@given(instance=eol_expression_NameExpression_strategy)
def test_eol_expression_nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original



@given(instance=eol_expression_NameExpression_strategy)
def test_eol_expression_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol_expression_KeyValueExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_keyvalueexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_KeyValueExpression)

@given(instance=eol_expression_NewExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_newexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_NewExpression)

@given(instance=eol_expression_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_VariableDeclarationExpression)



@given(instance=eol_expression_VariableDeclarationExpression_strategy)
def test_eol_expression_variabledeclarationexpression_create_setter(instance):
    original = instance.create
    instance.create = original
    assert instance.create == original

@given(instance=eol_expression_CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_CollectionInitialisationExpression)

@given(instance=eol_expression_MapExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_mapexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_MapExpression)

@given(instance=eol_expression_FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_FeatureCallExpression)



@given(instance=eol_expression_FeatureCallExpression_strategy)
def test_eol_expression_featurecallexpression_arrow_setter(instance):
    original = instance.arrow
    instance.arrow = original
    assert instance.arrow == original

@given(instance=eol_expression_CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_collectionexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_CollectionExpression)

@given(instance=eol_expression_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_PrimitiveExpression)

@given(instance=eol_expression_OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_expression_operatorexpression_instantiation(instance):
    assert isinstance(instance, eol_expression_OperatorExpression)

@given(instance=eol_expression_Type_strategy)
@settings(max_examples=50)
def test_eol_expression_type_instantiation(instance):
    assert isinstance(instance, eol_expression_Type)

@given(instance=eol_expression_Expression_strategy)
@settings(max_examples=50)
def test_eol_expression_expression_instantiation(instance):
    assert isinstance(instance, eol_expression_Expression)



@given(instance=eol_expression_Expression_strategy)
def test_eol_expression_expression_inBrackets_setter(instance):
    original = instance.inBrackets
    instance.inBrackets = original
    assert instance.inBrackets == original
