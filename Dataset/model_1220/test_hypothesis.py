import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimitiveType,
    eol_BooleanType,
    eol_SummablePrimitiveType,
    eol_ComparablePrimitiveType,
    OrderedCollectionType,
    eol_SequenceType,
    UniqueCollectionType,
    eol_OrderedSetType,
    eol_SetType,
    CollectionType,
    eol_OrderedCollectionType,
    eol_UniqueCollectionType,
    eol_BagType,
    AssignmentStatement,
    eol_SpecialAssignmentStatement,
    Type,
    eol_AnyType,
    AnnotationStatement,
    eol_ExecutableAnnotationStatement,
    eol_SimpleAnnotationStatement,
    SwitchCaseStatement,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    OrderedCollection,
    eol_SequenceExpression,
    UniqueCollection,
    eol_OrderedSetExpression,
    eol_SetExpression,
    CollectionExpression,
    eol_OrderedCollection,
    eol_BagExpression,
    SummableExpression,
    ComparableExpression,
    eol_RealExpression,
    eol_IntegerExpression,
    eol_StringExpression,
    PrimitiveExpression,
    eol_SummableExpression,
    eol_BooleanExpression,
    eol_ComparableExpression,
    Statement,
    eol_ThrowStatement,
    eol_AnnotationStatement,
    eol_SwitchStatement,
    eol_BreakStatement,
    eol_SwitchCaseStatement,
    eol_ExpressionStatement,
    eol_ContinueStatement,
    eol_AssignmentStatement,
    eol_IfStatement,
    eol_DeleteStatement,
    eol_ReturnStatement,
    eol_ForStatement,
    eol_AbortStatement,
    eol_WhileStatement,
    eol_BreakAllStatement,
    eol_TransactionStatement,
    CollectionInitialisationExpression,
    eol_ExpressionList,
    eol_ExpressionRange,
    eol_UniqueCollection,
    KeyValueExpression,
    eol_ModelDeclarationParameter,
    FeatureCallExpression,
    eol_FOLMethodCallExpression,
    eol_MethodCallExpression,
    eol_PropertyCallExpression,
    LogicalOperatorExpression,
    eol_XorOperatorExpression,
    eol_ImpliesOperatorExpression,
    eol_OrOperatorExpression,
    eol_AndOperatorExpression,
    BinaryOperatorExpression,
    eol_LogicalOperatorExpression,
    UnaryOperatorExpression,
    eol_NegativeOperatorExpression,
    eol_NotOperatorExpression,
    OperatorExpression,
    eol_BinaryOperatorExpression,
    eol_UnaryOperatorExpression,
    Expression,
    eol_PrimitiveExpression,
    eol_EnumerationLiteralExpression,
    eol_CollectionExpression,
    eol_CollectionInitialisationExpression,
    eol_MapExpression,
    eol_NewExpression,
    eol_FeatureCallExpression,
    eol_KeyValueExpression,
    eol_OperatorExpression,
    VariableDeclarationExpression,
    ComparisonOperatorExpression,
    eol_GreaterThanOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_EqualsOperatorExpression,
    eol_LessThanOperatorExpression,
    eol_NotEqualsOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_ComparisonOperatorExpression,
    ArithmeticOperatorExpression,
    eol_MinusOperatorExpression,
    eol_PlusOperatorExpression,
    eol_MultiplyOperatorExpression,
    eol_DivideOperatorExpression,
    eol_ArithmeticOperatorExpression,
    eol_Expression,
    eol_ExpressionOrStatementBlock,
    Block,
    eol_AnnotationBlock,
    eol_Statement,
    eol_Block,
    EOLLibraryModule,
    eol_EOLModule,
    eol_VariableDeclarationExpression,
    eol_FormalParameterExpression,
    eol_NameExpression,
    eol_Type,
    eol_OperationDefinition,
    eol_ModelDeclarationStatement,
    eol_Import,
    eol_EOLLibraryModule,
    PseudoType,
    eol_SelfContentType,
    eol_SelfType,
    AnyType,
    eol_InvalidType,
    eol_ModelElementType,
    eol_MapType,
    eol_CollectionType,
    eol_PseudoType,
    eol_PrimitiveType,
    eol_NativeType,
    eol_VoidType,
    eol_ModelType,
    RealType,
    eol_IntegerType,
    SummablePrimitiveType,
    ComparablePrimitiveType,
    eol_StringType,
    eol_RealType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol_booleantype_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanType)


def test_eol_booleantype_constructor_exists():
    assert callable(eol_BooleanType.__init__)


def test_eol_booleantype_constructor_args():
    sig = inspect.signature(eol_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_eol_summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_SummablePrimitiveType)


def test_eol_summableprimitivetype_constructor_exists():
    assert callable(eol_SummablePrimitiveType.__init__)


def test_eol_summableprimitivetype_constructor_args():
    sig = inspect.signature(eol_SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol_comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_ComparablePrimitiveType)


def test_eol_comparableprimitivetype_constructor_exists():
    assert callable(eol_ComparablePrimitiveType.__init__)


def test_eol_comparableprimitivetype_constructor_args():
    sig = inspect.signature(eol_ComparablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(OrderedCollectionType)


def test_orderedcollectiontype_constructor_exists():
    assert callable(OrderedCollectionType.__init__)


def test_orderedcollectiontype_constructor_args():
    sig = inspect.signature(OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_sequencetype_is_not_abstract():
    assert not inspect.isabstract(eol_SequenceType)


def test_eol_sequencetype_constructor_exists():
    assert callable(eol_SequenceType.__init__)


def test_eol_sequencetype_constructor_args():
    sig = inspect.signature(eol_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(UniqueCollectionType)


def test_uniquecollectiontype_constructor_exists():
    assert callable(UniqueCollectionType.__init__)


def test_uniquecollectiontype_constructor_args():
    sig = inspect.signature(UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedSetType)


def test_eol_orderedsettype_constructor_exists():
    assert callable(eol_OrderedSetType.__init__)


def test_eol_orderedsettype_constructor_args():
    sig = inspect.signature(eol_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_eol_settype_is_not_abstract():
    assert not inspect.isabstract(eol_SetType)


def test_eol_settype_constructor_exists():
    assert callable(eol_SetType.__init__)


def test_eol_settype_constructor_args():
    sig = inspect.signature(eol_SetType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedCollectionType)


def test_eol_orderedcollectiontype_constructor_exists():
    assert callable(eol_OrderedCollectionType.__init__)


def test_eol_orderedcollectiontype_constructor_args():
    sig = inspect.signature(eol_OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_UniqueCollectionType)


def test_eol_uniquecollectiontype_constructor_exists():
    assert callable(eol_UniqueCollectionType.__init__)


def test_eol_uniquecollectiontype_constructor_args():
    sig = inspect.signature(eol_UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_bagtype_is_not_abstract():
    assert not inspect.isabstract(eol_BagType)


def test_eol_bagtype_constructor_exists():
    assert callable(eol_BagType.__init__)


def test_eol_bagtype_constructor_args():
    sig = inspect.signature(eol_BagType.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SpecialAssignmentStatement)


def test_eol_specialassignmentstatement_constructor_exists():
    assert callable(eol_SpecialAssignmentStatement.__init__)


def test_eol_specialassignmentstatement_constructor_args():
    sig = inspect.signature(eol_SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_eol_anytype_is_not_abstract():
    assert not inspect.isabstract(eol_AnyType)


def test_eol_anytype_constructor_exists():
    assert callable(eol_AnyType.__init__)


def test_eol_anytype_constructor_args():
    sig = inspect.signature(eol_AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "declared" in params, "Missing parameter 'declared'"

def test_eol_anytype_has_declared():
    assert hasattr(eol_AnyType, "declared")
    descriptor = None
    for klass in eol_AnyType.__mro__:
        if "declared" in klass.__dict__:
            descriptor = klass.__dict__["declared"]
            break
    assert isinstance(descriptor, property)



def test_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(AnnotationStatement)


def test_annotationstatement_constructor_exists():
    assert callable(AnnotationStatement.__init__)


def test_annotationstatement_constructor_args():
    sig = inspect.signature(AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_executableannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ExecutableAnnotationStatement)


def test_eol_executableannotationstatement_constructor_exists():
    assert callable(eol_ExecutableAnnotationStatement.__init__)


def test_eol_executableannotationstatement_constructor_args():
    sig = inspect.signature(eol_ExecutableAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_simpleannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SimpleAnnotationStatement)


def test_eol_simpleannotationstatement_constructor_exists():
    assert callable(eol_SimpleAnnotationStatement.__init__)


def test_eol_simpleannotationstatement_constructor_args():
    sig = inspect.signature(eol_SimpleAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseDefaultStatement)


def test_eol_switchcasedefaultstatement_constructor_exists():
    assert callable(eol_SwitchCaseDefaultStatement.__init__)


def test_eol_switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseExpressionStatement)


def test_eol_switchcaseexpressionstatement_constructor_exists():
    assert callable(eol_SwitchCaseExpressionStatement.__init__)


def test_eol_switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(OrderedCollection)


def test_orderedcollection_constructor_exists():
    assert callable(OrderedCollection.__init__)


def test_orderedcollection_constructor_args():
    sig = inspect.signature(OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SequenceExpression)


def test_eol_sequenceexpression_constructor_exists():
    assert callable(eol_SequenceExpression.__init__)


def test_eol_sequenceexpression_constructor_args():
    sig = inspect.signature(eol_SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(UniqueCollection)


def test_uniquecollection_constructor_exists():
    assert callable(UniqueCollection.__init__)


def test_uniquecollection_constructor_args():
    sig = inspect.signature(UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedSetExpression)


def test_eol_orderedsetexpression_constructor_exists():
    assert callable(eol_OrderedSetExpression.__init__)


def test_eol_orderedsetexpression_constructor_args():
    sig = inspect.signature(eol_OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_setexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SetExpression)


def test_eol_setexpression_constructor_exists():
    assert callable(eol_SetExpression.__init__)


def test_eol_setexpression_constructor_args():
    sig = inspect.signature(eol_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedCollection)


def test_eol_orderedcollection_constructor_exists():
    assert callable(eol_OrderedCollection.__init__)


def test_eol_orderedcollection_constructor_args():
    sig = inspect.signature(eol_OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol_bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BagExpression)


def test_eol_bagexpression_constructor_exists():
    assert callable(eol_BagExpression.__init__)


def test_eol_bagexpression_constructor_args():
    sig = inspect.signature(eol_BagExpression.__init__)
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



def test_eol_realexpression_is_not_abstract():
    assert not inspect.isabstract(eol_RealExpression)


def test_eol_realexpression_constructor_exists():
    assert callable(eol_RealExpression.__init__)


def test_eol_realexpression_constructor_args():
    sig = inspect.signature(eol_RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_realexpression_has_value():
    assert hasattr(eol_RealExpression, "value")
    descriptor = None
    for klass in eol_RealExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerExpression)


def test_eol_integerexpression_constructor_exists():
    assert callable(eol_IntegerExpression.__init__)


def test_eol_integerexpression_constructor_args():
    sig = inspect.signature(eol_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_integerexpression_has_value():
    assert hasattr(eol_IntegerExpression, "value")
    descriptor = None
    for klass in eol_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol_StringExpression)


def test_eol_stringexpression_constructor_exists():
    assert callable(eol_StringExpression.__init__)


def test_eol_stringexpression_constructor_args():
    sig = inspect.signature(eol_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_stringexpression_has_value():
    assert hasattr(eol_StringExpression, "value")
    descriptor = None
    for klass in eol_StringExpression.__mro__:
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



def test_eol_summableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SummableExpression)


def test_eol_summableexpression_constructor_exists():
    assert callable(eol_SummableExpression.__init__)


def test_eol_summableexpression_constructor_args():
    sig = inspect.signature(eol_SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanExpression)


def test_eol_booleanexpression_constructor_exists():
    assert callable(eol_BooleanExpression.__init__)


def test_eol_booleanexpression_constructor_args():
    sig = inspect.signature(eol_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol_booleanexpression_has_value():
    assert hasattr(eol_BooleanExpression, "value")
    descriptor = None
    for klass in eol_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ComparableExpression)


def test_eol_comparableexpression_constructor_exists():
    assert callable(eol_ComparableExpression.__init__)


def test_eol_comparableexpression_constructor_args():
    sig = inspect.signature(eol_ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol_throwstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ThrowStatement)


def test_eol_throwstatement_constructor_exists():
    assert callable(eol_ThrowStatement.__init__)


def test_eol_throwstatement_constructor_args():
    sig = inspect.signature(eol_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AnnotationStatement)


def test_eol_annotationstatement_constructor_exists():
    assert callable(eol_AnnotationStatement.__init__)


def test_eol_annotationstatement_constructor_args():
    sig = inspect.signature(eol_AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchStatement)


def test_eol_switchstatement_constructor_exists():
    assert callable(eol_SwitchStatement.__init__)


def test_eol_switchstatement_constructor_args():
    sig = inspect.signature(eol_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol_BreakStatement)


def test_eol_breakstatement_constructor_exists():
    assert callable(eol_BreakStatement.__init__)


def test_eol_breakstatement_constructor_args():
    sig = inspect.signature(eol_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseStatement)


def test_eol_switchcasestatement_constructor_exists():
    assert callable(eol_SwitchCaseStatement.__init__)


def test_eol_switchcasestatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionStatement)


def test_eol_expressionstatement_constructor_exists():
    assert callable(eol_ExpressionStatement.__init__)


def test_eol_expressionstatement_constructor_args():
    sig = inspect.signature(eol_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol_ContinueStatement)


def test_eol_continuestatement_constructor_exists():
    assert callable(eol_ContinueStatement.__init__)


def test_eol_continuestatement_constructor_args():
    sig = inspect.signature(eol_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AssignmentStatement)


def test_eol_assignmentstatement_constructor_exists():
    assert callable(eol_AssignmentStatement.__init__)


def test_eol_assignmentstatement_constructor_args():
    sig = inspect.signature(eol_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol_IfStatement)


def test_eol_ifstatement_constructor_exists():
    assert callable(eol_IfStatement.__init__)


def test_eol_ifstatement_constructor_args():
    sig = inspect.signature(eol_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol_DeleteStatement)


def test_eol_deletestatement_constructor_exists():
    assert callable(eol_DeleteStatement.__init__)


def test_eol_deletestatement_constructor_args():
    sig = inspect.signature(eol_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ReturnStatement)


def test_eol_returnstatement_constructor_exists():
    assert callable(eol_ReturnStatement.__init__)


def test_eol_returnstatement_constructor_args():
    sig = inspect.signature(eol_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_forstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ForStatement)


def test_eol_forstatement_constructor_exists():
    assert callable(eol_ForStatement.__init__)


def test_eol_forstatement_constructor_args():
    sig = inspect.signature(eol_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_abortstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AbortStatement)


def test_eol_abortstatement_constructor_exists():
    assert callable(eol_AbortStatement.__init__)


def test_eol_abortstatement_constructor_args():
    sig = inspect.signature(eol_AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_whilestatement_is_not_abstract():
    assert not inspect.isabstract(eol_WhileStatement)


def test_eol_whilestatement_constructor_exists():
    assert callable(eol_WhileStatement.__init__)


def test_eol_whilestatement_constructor_args():
    sig = inspect.signature(eol_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_breakallstatement_is_not_abstract():
    assert not inspect.isabstract(eol_BreakAllStatement)


def test_eol_breakallstatement_constructor_exists():
    assert callable(eol_BreakAllStatement.__init__)


def test_eol_breakallstatement_constructor_args():
    sig = inspect.signature(eol_BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_transactionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_TransactionStatement)


def test_eol_transactionstatement_constructor_exists():
    assert callable(eol_TransactionStatement.__init__)


def test_eol_transactionstatement_constructor_args():
    sig = inspect.signature(eol_TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionInitialisationExpression)


def test_collectioninitialisationexpression_constructor_exists():
    assert callable(CollectionInitialisationExpression.__init__)


def test_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expressionlist_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionList)


def test_eol_expressionlist_constructor_exists():
    assert callable(eol_ExpressionList.__init__)


def test_eol_expressionlist_constructor_args():
    sig = inspect.signature(eol_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_eol_expressionrange_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionRange)


def test_eol_expressionrange_constructor_exists():
    assert callable(eol_ExpressionRange.__init__)


def test_eol_expressionrange_constructor_args():
    sig = inspect.signature(eol_ExpressionRange.__init__)
    params = list(sig.parameters.keys())



def test_eol_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(eol_UniqueCollection)


def test_eol_uniquecollection_constructor_exists():
    assert callable(eol_UniqueCollection.__init__)


def test_eol_uniquecollection_constructor_args():
    sig = inspect.signature(eol_UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(KeyValueExpression)


def test_keyvalueexpression_constructor_exists():
    assert callable(KeyValueExpression.__init__)


def test_keyvalueexpression_constructor_args():
    sig = inspect.signature(KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationParameter)


def test_eol_modeldeclarationparameter_constructor_exists():
    assert callable(eol_ModelDeclarationParameter.__init__)


def test_eol_modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FOLMethodCallExpression)


def test_eol_folmethodcallexpression_constructor_exists():
    assert callable(eol_FOLMethodCallExpression.__init__)


def test_eol_folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol_FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MethodCallExpression)


def test_eol_methodcallexpression_constructor_exists():
    assert callable(eol_MethodCallExpression.__init__)


def test_eol_methodcallexpression_constructor_args():
    sig = inspect.signature(eol_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PropertyCallExpression)


def test_eol_propertycallexpression_constructor_exists():
    assert callable(eol_PropertyCallExpression.__init__)


def test_eol_propertycallexpression_constructor_args():
    sig = inspect.signature(eol_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "extended" in params, "Missing parameter 'extended'"

def test_eol_propertycallexpression_has_extended():
    assert hasattr(eol_PropertyCallExpression, "extended")
    descriptor = None
    for klass in eol_PropertyCallExpression.__mro__:
        if "extended" in klass.__dict__:
            descriptor = klass.__dict__["extended"]
            break
    assert isinstance(descriptor, property)



def test_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_XorOperatorExpression)


def test_eol_xoroperatorexpression_constructor_exists():
    assert callable(eol_XorOperatorExpression.__init__)


def test_eol_xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol_XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ImpliesOperatorExpression)


def test_eol_impliesoperatorexpression_constructor_exists():
    assert callable(eol_ImpliesOperatorExpression.__init__)


def test_eol_impliesoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrOperatorExpression)


def test_eol_oroperatorexpression_constructor_exists():
    assert callable(eol_OrOperatorExpression.__init__)


def test_eol_oroperatorexpression_constructor_args():
    sig = inspect.signature(eol_OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_AndOperatorExpression)


def test_eol_andoperatorexpression_constructor_exists():
    assert callable(eol_AndOperatorExpression.__init__)


def test_eol_andoperatorexpression_constructor_args():
    sig = inspect.signature(eol_AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LogicalOperatorExpression)


def test_eol_logicaloperatorexpression_constructor_exists():
    assert callable(eol_LogicalOperatorExpression.__init__)


def test_eol_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol_LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NegativeOperatorExpression)


def test_eol_negativeoperatorexpression_constructor_exists():
    assert callable(eol_NegativeOperatorExpression.__init__)


def test_eol_negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NotOperatorExpression)


def test_eol_notoperatorexpression_constructor_exists():
    assert callable(eol_NotOperatorExpression.__init__)


def test_eol_notoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BinaryOperatorExpression)


def test_eol_binaryoperatorexpression_constructor_exists():
    assert callable(eol_BinaryOperatorExpression.__init__)


def test_eol_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_UnaryOperatorExpression)


def test_eol_unaryoperatorexpression_constructor_exists():
    assert callable(eol_UnaryOperatorExpression.__init__)


def test_eol_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol_UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveExpression)


def test_eol_primitiveexpression_constructor_exists():
    assert callable(eol_PrimitiveExpression.__init__)


def test_eol_primitiveexpression_constructor_args():
    sig = inspect.signature(eol_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EnumerationLiteralExpression)


def test_eol_enumerationliteralexpression_constructor_exists():
    assert callable(eol_EnumerationLiteralExpression.__init__)


def test_eol_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionExpression)


def test_eol_collectionexpression_constructor_exists():
    assert callable(eol_CollectionExpression.__init__)


def test_eol_collectionexpression_constructor_args():
    sig = inspect.signature(eol_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionInitialisationExpression)


def test_eol_collectioninitialisationexpression_constructor_exists():
    assert callable(eol_CollectionInitialisationExpression.__init__)


def test_eol_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(eol_CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MapExpression)


def test_eol_mapexpression_constructor_exists():
    assert callable(eol_MapExpression.__init__)


def test_eol_mapexpression_constructor_args():
    sig = inspect.signature(eol_MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_newexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NewExpression)


def test_eol_newexpression_constructor_exists():
    assert callable(eol_NewExpression.__init__)


def test_eol_newexpression_constructor_args():
    sig = inspect.signature(eol_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FeatureCallExpression)


def test_eol_featurecallexpression_constructor_exists():
    assert callable(eol_FeatureCallExpression.__init__)


def test_eol_featurecallexpression_constructor_args():
    sig = inspect.signature(eol_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arrow" in params, "Missing parameter 'arrow'"

def test_eol_featurecallexpression_has_arrow():
    assert hasattr(eol_FeatureCallExpression, "arrow")
    descriptor = None
    for klass in eol_FeatureCallExpression.__mro__:
        if "arrow" in klass.__dict__:
            descriptor = klass.__dict__["arrow"]
            break
    assert isinstance(descriptor, property)



def test_eol_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(eol_KeyValueExpression)


def test_eol_keyvalueexpression_constructor_exists():
    assert callable(eol_KeyValueExpression.__init__)


def test_eol_keyvalueexpression_constructor_args():
    sig = inspect.signature(eol_KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OperatorExpression)


def test_eol_operatorexpression_constructor_exists():
    assert callable(eol_OperatorExpression.__init__)


def test_eol_operatorexpression_constructor_args():
    sig = inspect.signature(eol_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOperatorExpression)


def test_eol_greaterthanoperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOperatorExpression.__init__)


def test_eol_greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LessThanOrEqualToOperatorExpression)


def test_eol_lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_LessThanOrEqualToOperatorExpression.__init__)


def test_eol_lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EqualsOperatorExpression)


def test_eol_equalsoperatorexpression_constructor_exists():
    assert callable(eol_EqualsOperatorExpression.__init__)


def test_eol_equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LessThanOperatorExpression)


def test_eol_lessthanoperatorexpression_constructor_exists():
    assert callable(eol_LessThanOperatorExpression.__init__)


def test_eol_lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NotEqualsOperatorExpression)


def test_eol_notequalsoperatorexpression_constructor_exists():
    assert callable(eol_NotEqualsOperatorExpression.__init__)


def test_eol_notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOrEqualToOperatorExpression)


def test_eol_greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol_greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ComparisonOperatorExpression)


def test_eol_comparisonoperatorexpression_constructor_exists():
    assert callable(eol_ComparisonOperatorExpression.__init__)


def test_eol_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MinusOperatorExpression)


def test_eol_minusoperatorexpression_constructor_exists():
    assert callable(eol_MinusOperatorExpression.__init__)


def test_eol_minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PlusOperatorExpression)


def test_eol_plusoperatorexpression_constructor_exists():
    assert callable(eol_PlusOperatorExpression.__init__)


def test_eol_plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol_PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MultiplyOperatorExpression)


def test_eol_multiplyoperatorexpression_constructor_exists():
    assert callable(eol_MultiplyOperatorExpression.__init__)


def test_eol_multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol_MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_DivideOperatorExpression)


def test_eol_divideoperatorexpression_constructor_exists():
    assert callable(eol_DivideOperatorExpression.__init__)


def test_eol_divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol_DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ArithmeticOperatorExpression)


def test_eol_arithmeticoperatorexpression_constructor_exists():
    assert callable(eol_ArithmeticOperatorExpression.__init__)


def test_eol_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_is_not_abstract():
    assert not inspect.isabstract(eol_Expression)


def test_eol_expression_constructor_exists():
    assert callable(eol_Expression.__init__)


def test_eol_expression_constructor_args():
    sig = inspect.signature(eol_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "inBrackets" in params, "Missing parameter 'inBrackets'"

def test_eol_expression_has_inBrackets():
    assert hasattr(eol_Expression, "inBrackets")
    descriptor = None
    for klass in eol_Expression.__mro__:
        if "inBrackets" in klass.__dict__:
            descriptor = klass.__dict__["inBrackets"]
            break
    assert isinstance(descriptor, property)



def test_eol_expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionOrStatementBlock)


def test_eol_expressionorstatementblock_constructor_exists():
    assert callable(eol_ExpressionOrStatementBlock.__init__)


def test_eol_expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol_ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_eol_annotationblock_is_not_abstract():
    assert not inspect.isabstract(eol_AnnotationBlock)


def test_eol_annotationblock_constructor_exists():
    assert callable(eol_AnnotationBlock.__init__)


def test_eol_annotationblock_constructor_args():
    sig = inspect.signature(eol_AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol_statement_is_not_abstract():
    assert not inspect.isabstract(eol_Statement)


def test_eol_statement_constructor_exists():
    assert callable(eol_Statement.__init__)


def test_eol_statement_constructor_args():
    sig = inspect.signature(eol_Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol_block_is_not_abstract():
    assert not inspect.isabstract(eol_Block)


def test_eol_block_constructor_exists():
    assert callable(eol_Block.__init__)


def test_eol_block_constructor_args():
    sig = inspect.signature(eol_Block.__init__)
    params = list(sig.parameters.keys())



def test_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EOLLibraryModule)


def test_eollibrarymodule_constructor_exists():
    assert callable(EOLLibraryModule.__init__)


def test_eollibrarymodule_constructor_args():
    sig = inspect.signature(EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol_eolmodule_is_not_abstract():
    assert not inspect.isabstract(eol_EOLModule)


def test_eol_eolmodule_constructor_exists():
    assert callable(eol_EOLModule.__init__)


def test_eol_eolmodule_constructor_args():
    sig = inspect.signature(eol_EOLModule.__init__)
    params = list(sig.parameters.keys())



def test_eol_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_VariableDeclarationExpression)


def test_eol_variabledeclarationexpression_constructor_exists():
    assert callable(eol_VariableDeclarationExpression.__init__)


def test_eol_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "create" in params, "Missing parameter 'create'"

def test_eol_variabledeclarationexpression_has_create():
    assert hasattr(eol_VariableDeclarationExpression, "create")
    descriptor = None
    for klass in eol_VariableDeclarationExpression.__mro__:
        if "create" in klass.__dict__:
            descriptor = klass.__dict__["create"]
            break
    assert isinstance(descriptor, property)



def test_eol_formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FormalParameterExpression)


def test_eol_formalparameterexpression_constructor_exists():
    assert callable(eol_FormalParameterExpression.__init__)


def test_eol_formalparameterexpression_constructor_args():
    sig = inspect.signature(eol_FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NameExpression)


def test_eol_nameexpression_constructor_exists():
    assert callable(eol_NameExpression.__init__)


def test_eol_nameexpression_constructor_args():
    sig = inspect.signature(eol_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isType" in params, "Missing parameter 'isType'"
    assert "resolvedContent" in params, "Missing parameter 'resolvedContent'"

def test_eol_nameexpression_has_name():
    assert hasattr(eol_NameExpression, "name")
    descriptor = None
    for klass in eol_NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eol_nameexpression_has_isType():
    assert hasattr(eol_NameExpression, "isType")
    descriptor = None
    for klass in eol_NameExpression.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)

def test_eol_nameexpression_has_resolvedContent():
    assert hasattr(eol_NameExpression, "resolvedContent")
    descriptor = None
    for klass in eol_NameExpression.__mro__:
        if "resolvedContent" in klass.__dict__:
            descriptor = klass.__dict__["resolvedContent"]
            break
    assert isinstance(descriptor, property)



def test_eol_type_is_not_abstract():
    assert not inspect.isabstract(eol_Type)


def test_eol_type_constructor_exists():
    assert callable(eol_Type.__init__)


def test_eol_type_constructor_args():
    sig = inspect.signature(eol_Type.__init__)
    params = list(sig.parameters.keys())



def test_eol_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(eol_OperationDefinition)


def test_eol_operationdefinition_constructor_exists():
    assert callable(eol_OperationDefinition.__init__)


def test_eol_operationdefinition_constructor_args():
    sig = inspect.signature(eol_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationStatement)


def test_eol_modeldeclarationstatement_constructor_exists():
    assert callable(eol_ModelDeclarationStatement.__init__)


def test_eol_modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"

def test_eol_modeldeclarationstatement_has_resolvedIMetamodel():
    assert hasattr(eol_ModelDeclarationStatement, "resolvedIMetamodel")
    descriptor = None
    for klass in eol_ModelDeclarationStatement.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)



def test_eol_import_is_not_abstract():
    assert not inspect.isabstract(eol_Import)


def test_eol_import_constructor_exists():
    assert callable(eol_Import.__init__)


def test_eol_import_constructor_args():
    sig = inspect.signature(eol_Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"

def test_eol_import_has_imported():
    assert hasattr(eol_Import, "imported")
    descriptor = None
    for klass in eol_Import.__mro__:
        if "imported" in klass.__dict__:
            descriptor = klass.__dict__["imported"]
            break
    assert isinstance(descriptor, property)



def test_eol_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol_EOLLibraryModule)


def test_eol_eollibrarymodule_constructor_exists():
    assert callable(eol_EOLLibraryModule.__init__)


def test_eol_eollibrarymodule_constructor_args():
    sig = inspect.signature(eol_EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eol_eollibrarymodule_has_name():
    assert hasattr(eol_EOLLibraryModule, "name")
    descriptor = None
    for klass in eol_EOLLibraryModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pseudotype_is_not_abstract():
    assert not inspect.isabstract(PseudoType)


def test_pseudotype_constructor_exists():
    assert callable(PseudoType.__init__)


def test_pseudotype_constructor_args():
    sig = inspect.signature(PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol_selfcontenttype_is_not_abstract():
    assert not inspect.isabstract(eol_SelfContentType)


def test_eol_selfcontenttype_constructor_exists():
    assert callable(eol_SelfContentType.__init__)


def test_eol_selfcontenttype_constructor_args():
    sig = inspect.signature(eol_SelfContentType.__init__)
    params = list(sig.parameters.keys())



def test_eol_selftype_is_not_abstract():
    assert not inspect.isabstract(eol_SelfType)


def test_eol_selftype_constructor_exists():
    assert callable(eol_SelfType.__init__)


def test_eol_selftype_constructor_args():
    sig = inspect.signature(eol_SelfType.__init__)
    params = list(sig.parameters.keys())



def test_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_eol_invalidtype_is_not_abstract():
    assert not inspect.isabstract(eol_InvalidType)


def test_eol_invalidtype_constructor_exists():
    assert callable(eol_InvalidType.__init__)


def test_eol_invalidtype_constructor_args():
    sig = inspect.signature(eol_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_eol_modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelElementType)


def test_eol_modelelementtype_constructor_exists():
    assert callable(eol_ModelElementType.__init__)


def test_eol_modelelementtype_constructor_args():
    sig = inspect.signature(eol_ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"
    assert "modelElementType" in params, "Missing parameter 'modelElementType'"
    assert "modelName" in params, "Missing parameter 'modelName'"
    assert "resolvedIPackage" in params, "Missing parameter 'resolvedIPackage'"
    assert "elementName" in params, "Missing parameter 'elementName'"

def test_eol_modelelementtype_has_resolvedIMetamodel():
    assert hasattr(eol_ModelElementType, "resolvedIMetamodel")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)

def test_eol_modelelementtype_has_modelElementType():
    assert hasattr(eol_ModelElementType, "modelElementType")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "modelElementType" in klass.__dict__:
            descriptor = klass.__dict__["modelElementType"]
            break
    assert isinstance(descriptor, property)

def test_eol_modelelementtype_has_modelName():
    assert hasattr(eol_ModelElementType, "modelName")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)

def test_eol_modelelementtype_has_resolvedIPackage():
    assert hasattr(eol_ModelElementType, "resolvedIPackage")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "resolvedIPackage" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIPackage"]
            break
    assert isinstance(descriptor, property)

def test_eol_modelelementtype_has_elementName():
    assert hasattr(eol_ModelElementType, "elementName")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)



def test_eol_maptype_is_not_abstract():
    assert not inspect.isabstract(eol_MapType)


def test_eol_maptype_constructor_exists():
    assert callable(eol_MapType.__init__)


def test_eol_maptype_constructor_args():
    sig = inspect.signature(eol_MapType.__init__)
    params = list(sig.parameters.keys())



def test_eol_collectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionType)


def test_eol_collectiontype_constructor_exists():
    assert callable(eol_CollectionType.__init__)


def test_eol_collectiontype_constructor_args():
    sig = inspect.signature(eol_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_pseudotype_is_not_abstract():
    assert not inspect.isabstract(eol_PseudoType)


def test_eol_pseudotype_constructor_exists():
    assert callable(eol_PseudoType.__init__)


def test_eol_pseudotype_constructor_args():
    sig = inspect.signature(eol_PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol_primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveType)


def test_eol_primitivetype_constructor_exists():
    assert callable(eol_PrimitiveType.__init__)


def test_eol_primitivetype_constructor_args():
    sig = inspect.signature(eol_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol_nativetype_is_not_abstract():
    assert not inspect.isabstract(eol_NativeType)


def test_eol_nativetype_constructor_exists():
    assert callable(eol_NativeType.__init__)


def test_eol_nativetype_constructor_args():
    sig = inspect.signature(eol_NativeType.__init__)
    params = list(sig.parameters.keys())



def test_eol_voidtype_is_not_abstract():
    assert not inspect.isabstract(eol_VoidType)


def test_eol_voidtype_constructor_exists():
    assert callable(eol_VoidType.__init__)


def test_eol_voidtype_constructor_args():
    sig = inspect.signature(eol_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeltype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelType)


def test_eol_modeltype_constructor_exists():
    assert callable(eol_ModelType.__init__)


def test_eol_modeltype_constructor_args():
    sig = inspect.signature(eol_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_eol_modeltype_has_resolvedIMetamodel():
    assert hasattr(eol_ModelType, "resolvedIMetamodel")
    descriptor = None
    for klass in eol_ModelType.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)

def test_eol_modeltype_has_modelName():
    assert hasattr(eol_ModelType, "modelName")
    descriptor = None
    for klass in eol_ModelType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_eol_integertype_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerType)


def test_eol_integertype_constructor_exists():
    assert callable(eol_IntegerType.__init__)


def test_eol_integertype_constructor_args():
    sig = inspect.signature(eol_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(SummablePrimitiveType)


def test_summableprimitivetype_constructor_exists():
    assert callable(SummablePrimitiveType.__init__)


def test_summableprimitivetype_constructor_args():
    sig = inspect.signature(SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ComparablePrimitiveType)


def test_comparableprimitivetype_constructor_exists():
    assert callable(ComparablePrimitiveType.__init__)


def test_comparableprimitivetype_constructor_args():
    sig = inspect.signature(ComparablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol_stringtype_is_not_abstract():
    assert not inspect.isabstract(eol_StringType)


def test_eol_stringtype_constructor_exists():
    assert callable(eol_StringType.__init__)


def test_eol_stringtype_constructor_args():
    sig = inspect.signature(eol_StringType.__init__)
    params = list(sig.parameters.keys())



def test_eol_realtype_is_not_abstract():
    assert not inspect.isabstract(eol_RealType)


def test_eol_realtype_constructor_exists():
    assert callable(eol_RealType.__init__)


def test_eol_realtype_constructor_args():
    sig = inspect.signature(eol_RealType.__init__)
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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol_BooleanType_strategy = st.builds(
    eol_BooleanType,
)
eol_SummablePrimitiveType_strategy = st.builds(
    eol_SummablePrimitiveType,
)
eol_ComparablePrimitiveType_strategy = st.builds(
    eol_ComparablePrimitiveType,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol_SequenceType_strategy = st.builds(
    eol_SequenceType,
)
UniqueCollectionType_strategy = st.builds(
    UniqueCollectionType,
)
eol_OrderedSetType_strategy = st.builds(
    eol_OrderedSetType,
)
eol_SetType_strategy = st.builds(
    eol_SetType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
eol_OrderedCollectionType_strategy = st.builds(
    eol_OrderedCollectionType,
)
eol_UniqueCollectionType_strategy = st.builds(
    eol_UniqueCollectionType,
)
eol_BagType_strategy = st.builds(
    eol_BagType,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol_SpecialAssignmentStatement_strategy = st.builds(
    eol_SpecialAssignmentStatement,
)
Type_strategy = st.builds(
    Type,
)
eol_AnyType_strategy = st.builds(
    eol_AnyType,
    declared=
        st.booleans()
)
AnnotationStatement_strategy = st.builds(
    AnnotationStatement,
)
eol_ExecutableAnnotationStatement_strategy = st.builds(
    eol_ExecutableAnnotationStatement,
)
eol_SimpleAnnotationStatement_strategy = st.builds(
    eol_SimpleAnnotationStatement,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
eol_SwitchCaseDefaultStatement_strategy = st.builds(
    eol_SwitchCaseDefaultStatement,
)
eol_SwitchCaseExpressionStatement_strategy = st.builds(
    eol_SwitchCaseExpressionStatement,
)
OrderedCollection_strategy = st.builds(
    OrderedCollection,
)
eol_SequenceExpression_strategy = st.builds(
    eol_SequenceExpression,
)
UniqueCollection_strategy = st.builds(
    UniqueCollection,
)
eol_OrderedSetExpression_strategy = st.builds(
    eol_OrderedSetExpression,
)
eol_SetExpression_strategy = st.builds(
    eol_SetExpression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol_OrderedCollection_strategy = st.builds(
    eol_OrderedCollection,
)
eol_BagExpression_strategy = st.builds(
    eol_BagExpression,
)
SummableExpression_strategy = st.builds(
    SummableExpression,
)
ComparableExpression_strategy = st.builds(
    ComparableExpression,
)
eol_RealExpression_strategy = st.builds(
    eol_RealExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol_IntegerExpression_strategy = st.builds(
    eol_IntegerExpression,
    value=
        st.integers()
)
eol_StringExpression_strategy = st.builds(
    eol_StringExpression,
    value=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol_SummableExpression_strategy = st.builds(
    eol_SummableExpression,
)
eol_BooleanExpression_strategy = st.builds(
    eol_BooleanExpression,
    value=
        st.booleans()
)
eol_ComparableExpression_strategy = st.builds(
    eol_ComparableExpression,
)
Statement_strategy = st.builds(
    Statement,
)
eol_ThrowStatement_strategy = st.builds(
    eol_ThrowStatement,
)
eol_AnnotationStatement_strategy = st.builds(
    eol_AnnotationStatement,
)
eol_SwitchStatement_strategy = st.builds(
    eol_SwitchStatement,
)
eol_BreakStatement_strategy = st.builds(
    eol_BreakStatement,
)
eol_SwitchCaseStatement_strategy = st.builds(
    eol_SwitchCaseStatement,
)
eol_ExpressionStatement_strategy = st.builds(
    eol_ExpressionStatement,
)
eol_ContinueStatement_strategy = st.builds(
    eol_ContinueStatement,
)
eol_AssignmentStatement_strategy = st.builds(
    eol_AssignmentStatement,
)
eol_IfStatement_strategy = st.builds(
    eol_IfStatement,
)
eol_DeleteStatement_strategy = st.builds(
    eol_DeleteStatement,
)
eol_ReturnStatement_strategy = st.builds(
    eol_ReturnStatement,
)
eol_ForStatement_strategy = st.builds(
    eol_ForStatement,
)
eol_AbortStatement_strategy = st.builds(
    eol_AbortStatement,
)
eol_WhileStatement_strategy = st.builds(
    eol_WhileStatement,
)
eol_BreakAllStatement_strategy = st.builds(
    eol_BreakAllStatement,
)
eol_TransactionStatement_strategy = st.builds(
    eol_TransactionStatement,
)
CollectionInitialisationExpression_strategy = st.builds(
    CollectionInitialisationExpression,
)
eol_ExpressionList_strategy = st.builds(
    eol_ExpressionList,
)
eol_ExpressionRange_strategy = st.builds(
    eol_ExpressionRange,
)
eol_UniqueCollection_strategy = st.builds(
    eol_UniqueCollection,
)
KeyValueExpression_strategy = st.builds(
    KeyValueExpression,
)
eol_ModelDeclarationParameter_strategy = st.builds(
    eol_ModelDeclarationParameter,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol_FOLMethodCallExpression_strategy = st.builds(
    eol_FOLMethodCallExpression,
)
eol_MethodCallExpression_strategy = st.builds(
    eol_MethodCallExpression,
)
eol_PropertyCallExpression_strategy = st.builds(
    eol_PropertyCallExpression,
    extended=
        st.booleans()
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol_XorOperatorExpression_strategy = st.builds(
    eol_XorOperatorExpression,
)
eol_ImpliesOperatorExpression_strategy = st.builds(
    eol_ImpliesOperatorExpression,
)
eol_OrOperatorExpression_strategy = st.builds(
    eol_OrOperatorExpression,
)
eol_AndOperatorExpression_strategy = st.builds(
    eol_AndOperatorExpression,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol_LogicalOperatorExpression_strategy = st.builds(
    eol_LogicalOperatorExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol_NegativeOperatorExpression_strategy = st.builds(
    eol_NegativeOperatorExpression,
)
eol_NotOperatorExpression_strategy = st.builds(
    eol_NotOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol_BinaryOperatorExpression_strategy = st.builds(
    eol_BinaryOperatorExpression,
)
eol_UnaryOperatorExpression_strategy = st.builds(
    eol_UnaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol_PrimitiveExpression_strategy = st.builds(
    eol_PrimitiveExpression,
)
eol_EnumerationLiteralExpression_strategy = st.builds(
    eol_EnumerationLiteralExpression,
)
eol_CollectionExpression_strategy = st.builds(
    eol_CollectionExpression,
)
eol_CollectionInitialisationExpression_strategy = st.builds(
    eol_CollectionInitialisationExpression,
)
eol_MapExpression_strategy = st.builds(
    eol_MapExpression,
)
eol_NewExpression_strategy = st.builds(
    eol_NewExpression,
)
eol_FeatureCallExpression_strategy = st.builds(
    eol_FeatureCallExpression,
    arrow=
        st.booleans()
)
eol_KeyValueExpression_strategy = st.builds(
    eol_KeyValueExpression,
)
eol_OperatorExpression_strategy = st.builds(
    eol_OperatorExpression,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol_GreaterThanOperatorExpression_strategy = st.builds(
    eol_GreaterThanOperatorExpression,
)
eol_LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_LessThanOrEqualToOperatorExpression,
)
eol_EqualsOperatorExpression_strategy = st.builds(
    eol_EqualsOperatorExpression,
)
eol_LessThanOperatorExpression_strategy = st.builds(
    eol_LessThanOperatorExpression,
)
eol_NotEqualsOperatorExpression_strategy = st.builds(
    eol_NotEqualsOperatorExpression,
)
eol_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_GreaterThanOrEqualToOperatorExpression,
)
eol_ComparisonOperatorExpression_strategy = st.builds(
    eol_ComparisonOperatorExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol_MinusOperatorExpression_strategy = st.builds(
    eol_MinusOperatorExpression,
)
eol_PlusOperatorExpression_strategy = st.builds(
    eol_PlusOperatorExpression,
)
eol_MultiplyOperatorExpression_strategy = st.builds(
    eol_MultiplyOperatorExpression,
)
eol_DivideOperatorExpression_strategy = st.builds(
    eol_DivideOperatorExpression,
)
eol_ArithmeticOperatorExpression_strategy = st.builds(
    eol_ArithmeticOperatorExpression,
)
eol_Expression_strategy = st.builds(
    eol_Expression,
    inBrackets=
        st.booleans()
)
eol_ExpressionOrStatementBlock_strategy = st.builds(
    eol_ExpressionOrStatementBlock,
)
Block_strategy = st.builds(
    Block,
)
eol_AnnotationBlock_strategy = st.builds(
    eol_AnnotationBlock,
)
eol_Statement_strategy = st.builds(
    eol_Statement,
)
eol_Block_strategy = st.builds(
    eol_Block,
)
EOLLibraryModule_strategy = st.builds(
    EOLLibraryModule,
)
eol_EOLModule_strategy = st.builds(
    eol_EOLModule,
)
eol_VariableDeclarationExpression_strategy = st.builds(
    eol_VariableDeclarationExpression,
    create=
        st.booleans()
)
eol_FormalParameterExpression_strategy = st.builds(
    eol_FormalParameterExpression,
)
eol_NameExpression_strategy = st.builds(
    eol_NameExpression,
    name=
        safe_text,
    isType=
        st.booleans(),
    resolvedContent=
        safe_text
)
eol_Type_strategy = st.builds(
    eol_Type,
)
eol_OperationDefinition_strategy = st.builds(
    eol_OperationDefinition,
)
eol_ModelDeclarationStatement_strategy = st.builds(
    eol_ModelDeclarationStatement,
    resolvedIMetamodel=
        safe_text
)
eol_Import_strategy = st.builds(
    eol_Import,
    imported=
        safe_text
)
eol_EOLLibraryModule_strategy = st.builds(
    eol_EOLLibraryModule,
    name=
        safe_text
)
PseudoType_strategy = st.builds(
    PseudoType,
)
eol_SelfContentType_strategy = st.builds(
    eol_SelfContentType,
)
eol_SelfType_strategy = st.builds(
    eol_SelfType,
)
AnyType_strategy = st.builds(
    AnyType,
)
eol_InvalidType_strategy = st.builds(
    eol_InvalidType,
)
eol_ModelElementType_strategy = st.builds(
    eol_ModelElementType,
    resolvedIMetamodel=
        safe_text,
    modelElementType=
        safe_text,
    modelName=
        safe_text,
    resolvedIPackage=
        safe_text,
    elementName=
        safe_text
)
eol_MapType_strategy = st.builds(
    eol_MapType,
)
eol_CollectionType_strategy = st.builds(
    eol_CollectionType,
)
eol_PseudoType_strategy = st.builds(
    eol_PseudoType,
)
eol_PrimitiveType_strategy = st.builds(
    eol_PrimitiveType,
)
eol_NativeType_strategy = st.builds(
    eol_NativeType,
)
eol_VoidType_strategy = st.builds(
    eol_VoidType,
)
eol_ModelType_strategy = st.builds(
    eol_ModelType,
    resolvedIMetamodel=
        safe_text,
    modelName=
        safe_text
)
RealType_strategy = st.builds(
    RealType,
)
eol_IntegerType_strategy = st.builds(
    eol_IntegerType,
)
SummablePrimitiveType_strategy = st.builds(
    SummablePrimitiveType,
)
ComparablePrimitiveType_strategy = st.builds(
    ComparablePrimitiveType,
)
eol_StringType_strategy = st.builds(
    eol_StringType,
)
eol_RealType_strategy = st.builds(
    eol_RealType,
)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=eol_BooleanType_strategy)
@settings(max_examples=50)
def test_eol_booleantype_instantiation(instance):
    assert isinstance(instance, eol_BooleanType)

@given(instance=eol_SummablePrimitiveType_strategy)
@settings(max_examples=50)
def test_eol_summableprimitivetype_instantiation(instance):
    assert isinstance(instance, eol_SummablePrimitiveType)

@given(instance=eol_ComparablePrimitiveType_strategy)
@settings(max_examples=50)
def test_eol_comparableprimitivetype_instantiation(instance):
    assert isinstance(instance, eol_ComparablePrimitiveType)

@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)

@given(instance=eol_SequenceType_strategy)
@settings(max_examples=50)
def test_eol_sequencetype_instantiation(instance):
    assert isinstance(instance, eol_SequenceType)

@given(instance=UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, UniqueCollectionType)

@given(instance=eol_OrderedSetType_strategy)
@settings(max_examples=50)
def test_eol_orderedsettype_instantiation(instance):
    assert isinstance(instance, eol_OrderedSetType)

@given(instance=eol_SetType_strategy)
@settings(max_examples=50)
def test_eol_settype_instantiation(instance):
    assert isinstance(instance, eol_SetType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=eol_OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_eol_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, eol_OrderedCollectionType)

@given(instance=eol_UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_eol_uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, eol_UniqueCollectionType)

@given(instance=eol_BagType_strategy)
@settings(max_examples=50)
def test_eol_bagtype_instantiation(instance):
    assert isinstance(instance, eol_BagType)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=eol_SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol_specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, eol_SpecialAssignmentStatement)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eol_AnyType_strategy)
@settings(max_examples=50)
def test_eol_anytype_instantiation(instance):
    assert isinstance(instance, eol_AnyType)



@given(instance=eol_AnyType_strategy)
def test_eol_anytype_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original

@given(instance=AnnotationStatement_strategy)
@settings(max_examples=50)
def test_annotationstatement_instantiation(instance):
    assert isinstance(instance, AnnotationStatement)

@given(instance=eol_ExecutableAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol_executableannotationstatement_instantiation(instance):
    assert isinstance(instance, eol_ExecutableAnnotationStatement)

@given(instance=eol_SimpleAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol_simpleannotationstatement_instantiation(instance):
    assert isinstance(instance, eol_SimpleAnnotationStatement)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=eol_SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseDefaultStatement)

@given(instance=eol_SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseExpressionStatement)

@given(instance=OrderedCollection_strategy)
@settings(max_examples=50)
def test_orderedcollection_instantiation(instance):
    assert isinstance(instance, OrderedCollection)

@given(instance=eol_SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol_sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol_SequenceExpression)

@given(instance=UniqueCollection_strategy)
@settings(max_examples=50)
def test_uniquecollection_instantiation(instance):
    assert isinstance(instance, UniqueCollection)

@given(instance=eol_OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol_orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol_OrderedSetExpression)

@given(instance=eol_SetExpression_strategy)
@settings(max_examples=50)
def test_eol_setexpression_instantiation(instance):
    assert isinstance(instance, eol_SetExpression)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol_OrderedCollection_strategy)
@settings(max_examples=50)
def test_eol_orderedcollection_instantiation(instance):
    assert isinstance(instance, eol_OrderedCollection)

@given(instance=eol_BagExpression_strategy)
@settings(max_examples=50)
def test_eol_bagexpression_instantiation(instance):
    assert isinstance(instance, eol_BagExpression)

@given(instance=SummableExpression_strategy)
@settings(max_examples=50)
def test_summableexpression_instantiation(instance):
    assert isinstance(instance, SummableExpression)

@given(instance=ComparableExpression_strategy)
@settings(max_examples=50)
def test_comparableexpression_instantiation(instance):
    assert isinstance(instance, ComparableExpression)

@given(instance=eol_RealExpression_strategy)
@settings(max_examples=50)
def test_eol_realexpression_instantiation(instance):
    assert isinstance(instance, eol_RealExpression)



@given(instance=eol_RealExpression_strategy)
def test_eol_realexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol_integerexpression_instantiation(instance):
    assert isinstance(instance, eol_IntegerExpression)



@given(instance=eol_IntegerExpression_strategy)
def test_eol_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_StringExpression_strategy)
@settings(max_examples=50)
def test_eol_stringexpression_instantiation(instance):
    assert isinstance(instance, eol_StringExpression)



@given(instance=eol_StringExpression_strategy)
def test_eol_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol_SummableExpression_strategy)
@settings(max_examples=50)
def test_eol_summableexpression_instantiation(instance):
    assert isinstance(instance, eol_SummableExpression)

@given(instance=eol_BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol_booleanexpression_instantiation(instance):
    assert isinstance(instance, eol_BooleanExpression)



@given(instance=eol_BooleanExpression_strategy)
def test_eol_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol_ComparableExpression_strategy)
@settings(max_examples=50)
def test_eol_comparableexpression_instantiation(instance):
    assert isinstance(instance, eol_ComparableExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=eol_ThrowStatement_strategy)
@settings(max_examples=50)
def test_eol_throwstatement_instantiation(instance):
    assert isinstance(instance, eol_ThrowStatement)

@given(instance=eol_AnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol_annotationstatement_instantiation(instance):
    assert isinstance(instance, eol_AnnotationStatement)

@given(instance=eol_SwitchStatement_strategy)
@settings(max_examples=50)
def test_eol_switchstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchStatement)

@given(instance=eol_BreakStatement_strategy)
@settings(max_examples=50)
def test_eol_breakstatement_instantiation(instance):
    assert isinstance(instance, eol_BreakStatement)

@given(instance=eol_SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcasestatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseStatement)

@given(instance=eol_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol_expressionstatement_instantiation(instance):
    assert isinstance(instance, eol_ExpressionStatement)

@given(instance=eol_ContinueStatement_strategy)
@settings(max_examples=50)
def test_eol_continuestatement_instantiation(instance):
    assert isinstance(instance, eol_ContinueStatement)

@given(instance=eol_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol_assignmentstatement_instantiation(instance):
    assert isinstance(instance, eol_AssignmentStatement)

@given(instance=eol_IfStatement_strategy)
@settings(max_examples=50)
def test_eol_ifstatement_instantiation(instance):
    assert isinstance(instance, eol_IfStatement)

@given(instance=eol_DeleteStatement_strategy)
@settings(max_examples=50)
def test_eol_deletestatement_instantiation(instance):
    assert isinstance(instance, eol_DeleteStatement)

@given(instance=eol_ReturnStatement_strategy)
@settings(max_examples=50)
def test_eol_returnstatement_instantiation(instance):
    assert isinstance(instance, eol_ReturnStatement)

@given(instance=eol_ForStatement_strategy)
@settings(max_examples=50)
def test_eol_forstatement_instantiation(instance):
    assert isinstance(instance, eol_ForStatement)

@given(instance=eol_AbortStatement_strategy)
@settings(max_examples=50)
def test_eol_abortstatement_instantiation(instance):
    assert isinstance(instance, eol_AbortStatement)

@given(instance=eol_WhileStatement_strategy)
@settings(max_examples=50)
def test_eol_whilestatement_instantiation(instance):
    assert isinstance(instance, eol_WhileStatement)

@given(instance=eol_BreakAllStatement_strategy)
@settings(max_examples=50)
def test_eol_breakallstatement_instantiation(instance):
    assert isinstance(instance, eol_BreakAllStatement)

@given(instance=eol_TransactionStatement_strategy)
@settings(max_examples=50)
def test_eol_transactionstatement_instantiation(instance):
    assert isinstance(instance, eol_TransactionStatement)

@given(instance=CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, CollectionInitialisationExpression)

@given(instance=eol_ExpressionList_strategy)
@settings(max_examples=50)
def test_eol_expressionlist_instantiation(instance):
    assert isinstance(instance, eol_ExpressionList)

@given(instance=eol_ExpressionRange_strategy)
@settings(max_examples=50)
def test_eol_expressionrange_instantiation(instance):
    assert isinstance(instance, eol_ExpressionRange)

@given(instance=eol_UniqueCollection_strategy)
@settings(max_examples=50)
def test_eol_uniquecollection_instantiation(instance):
    assert isinstance(instance, eol_UniqueCollection)

@given(instance=KeyValueExpression_strategy)
@settings(max_examples=50)
def test_keyvalueexpression_instantiation(instance):
    assert isinstance(instance, KeyValueExpression)

@given(instance=eol_ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_eol_modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationParameter)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol_FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_FOLMethodCallExpression)

@given(instance=eol_MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_MethodCallExpression)

@given(instance=eol_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol_propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol_PropertyCallExpression)



@given(instance=eol_PropertyCallExpression_strategy)
def test_eol_propertycallexpression_extended_setter(instance):
    original = instance.extended
    instance.extended = original
    assert instance.extended == original

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol_XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_XorOperatorExpression)

@given(instance=eol_ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ImpliesOperatorExpression)

@given(instance=eol_OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_OrOperatorExpression)

@given(instance=eol_AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_AndOperatorExpression)

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol_LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LogicalOperatorExpression)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol_NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NegativeOperatorExpression)

@given(instance=eol_NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NotOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=eol_BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_BinaryOperatorExpression)

@given(instance=eol_UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_UnaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol_primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveExpression)

@given(instance=eol_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol_EnumerationLiteralExpression)

@given(instance=eol_CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol_collectionexpression_instantiation(instance):
    assert isinstance(instance, eol_CollectionExpression)

@given(instance=eol_CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_eol_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, eol_CollectionInitialisationExpression)

@given(instance=eol_MapExpression_strategy)
@settings(max_examples=50)
def test_eol_mapexpression_instantiation(instance):
    assert isinstance(instance, eol_MapExpression)

@given(instance=eol_NewExpression_strategy)
@settings(max_examples=50)
def test_eol_newexpression_instantiation(instance):
    assert isinstance(instance, eol_NewExpression)

@given(instance=eol_FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol_featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol_FeatureCallExpression)



@given(instance=eol_FeatureCallExpression_strategy)
def test_eol_featurecallexpression_arrow_setter(instance):
    original = instance.arrow
    instance.arrow = original
    assert instance.arrow == original

@given(instance=eol_KeyValueExpression_strategy)
@settings(max_examples=50)
def test_eol_keyvalueexpression_instantiation(instance):
    assert isinstance(instance, eol_KeyValueExpression)

@given(instance=eol_OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_operatorexpression_instantiation(instance):
    assert isinstance(instance, eol_OperatorExpression)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol_GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOperatorExpression)

@given(instance=eol_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOrEqualToOperatorExpression)

@given(instance=eol_EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_EqualsOperatorExpression)

@given(instance=eol_LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOperatorExpression)

@given(instance=eol_NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NotEqualsOperatorExpression)

@given(instance=eol_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOrEqualToOperatorExpression)

@given(instance=eol_ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ComparisonOperatorExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol_MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_MinusOperatorExpression)

@given(instance=eol_PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_PlusOperatorExpression)

@given(instance=eol_MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_MultiplyOperatorExpression)

@given(instance=eol_DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_DivideOperatorExpression)

@given(instance=eol_ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ArithmeticOperatorExpression)

@given(instance=eol_Expression_strategy)
@settings(max_examples=50)
def test_eol_expression_instantiation(instance):
    assert isinstance(instance, eol_Expression)



@given(instance=eol_Expression_strategy)
def test_eol_expression_inBrackets_setter(instance):
    original = instance.inBrackets
    instance.inBrackets = original
    assert instance.inBrackets == original

@given(instance=eol_ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol_expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol_ExpressionOrStatementBlock)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=eol_AnnotationBlock_strategy)
@settings(max_examples=50)
def test_eol_annotationblock_instantiation(instance):
    assert isinstance(instance, eol_AnnotationBlock)

@given(instance=eol_Statement_strategy)
@settings(max_examples=50)
def test_eol_statement_instantiation(instance):
    assert isinstance(instance, eol_Statement)

@given(instance=eol_Block_strategy)
@settings(max_examples=50)
def test_eol_block_instantiation(instance):
    assert isinstance(instance, eol_Block)

@given(instance=EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, EOLLibraryModule)

@given(instance=eol_EOLModule_strategy)
@settings(max_examples=50)
def test_eol_eolmodule_instantiation(instance):
    assert isinstance(instance, eol_EOLModule)

@given(instance=eol_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol_VariableDeclarationExpression)



@given(instance=eol_VariableDeclarationExpression_strategy)
def test_eol_variabledeclarationexpression_create_setter(instance):
    original = instance.create
    instance.create = original
    assert instance.create == original

@given(instance=eol_FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol_formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol_FormalParameterExpression)

@given(instance=eol_NameExpression_strategy)
@settings(max_examples=50)
def test_eol_nameexpression_instantiation(instance):
    assert isinstance(instance, eol_NameExpression)



@given(instance=eol_NameExpression_strategy)
def test_eol_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eol_NameExpression_strategy)
def test_eol_nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original



@given(instance=eol_NameExpression_strategy)
def test_eol_nameexpression_resolvedContent_setter(instance):
    original = instance.resolvedContent
    instance.resolvedContent = original
    assert instance.resolvedContent == original

@given(instance=eol_Type_strategy)
@settings(max_examples=50)
def test_eol_type_instantiation(instance):
    assert isinstance(instance, eol_Type)

@given(instance=eol_OperationDefinition_strategy)
@settings(max_examples=50)
def test_eol_operationdefinition_instantiation(instance):
    assert isinstance(instance, eol_OperationDefinition)

@given(instance=eol_ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol_modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationStatement)



@given(instance=eol_ModelDeclarationStatement_strategy)
def test_eol_modeldeclarationstatement_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original

@given(instance=eol_Import_strategy)
@settings(max_examples=50)
def test_eol_import_instantiation(instance):
    assert isinstance(instance, eol_Import)



@given(instance=eol_Import_strategy)
def test_eol_import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original

@given(instance=eol_EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eol_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, eol_EOLLibraryModule)



@given(instance=eol_EOLLibraryModule_strategy)
def test_eol_eollibrarymodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PseudoType_strategy)
@settings(max_examples=50)
def test_pseudotype_instantiation(instance):
    assert isinstance(instance, PseudoType)

@given(instance=eol_SelfContentType_strategy)
@settings(max_examples=50)
def test_eol_selfcontenttype_instantiation(instance):
    assert isinstance(instance, eol_SelfContentType)

@given(instance=eol_SelfType_strategy)
@settings(max_examples=50)
def test_eol_selftype_instantiation(instance):
    assert isinstance(instance, eol_SelfType)

@given(instance=AnyType_strategy)
@settings(max_examples=50)
def test_anytype_instantiation(instance):
    assert isinstance(instance, AnyType)

@given(instance=eol_InvalidType_strategy)
@settings(max_examples=50)
def test_eol_invalidtype_instantiation(instance):
    assert isinstance(instance, eol_InvalidType)

@given(instance=eol_ModelElementType_strategy)
@settings(max_examples=50)
def test_eol_modelelementtype_instantiation(instance):
    assert isinstance(instance, eol_ModelElementType)



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_modelElementType_setter(instance):
    original = instance.modelElementType
    instance.modelElementType = original
    assert instance.modelElementType == original



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_resolvedIPackage_setter(instance):
    original = instance.resolvedIPackage
    instance.resolvedIPackage = original
    assert instance.resolvedIPackage == original



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=eol_MapType_strategy)
@settings(max_examples=50)
def test_eol_maptype_instantiation(instance):
    assert isinstance(instance, eol_MapType)

@given(instance=eol_CollectionType_strategy)
@settings(max_examples=50)
def test_eol_collectiontype_instantiation(instance):
    assert isinstance(instance, eol_CollectionType)

@given(instance=eol_PseudoType_strategy)
@settings(max_examples=50)
def test_eol_pseudotype_instantiation(instance):
    assert isinstance(instance, eol_PseudoType)

@given(instance=eol_PrimitiveType_strategy)
@settings(max_examples=50)
def test_eol_primitivetype_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveType)

@given(instance=eol_NativeType_strategy)
@settings(max_examples=50)
def test_eol_nativetype_instantiation(instance):
    assert isinstance(instance, eol_NativeType)

@given(instance=eol_VoidType_strategy)
@settings(max_examples=50)
def test_eol_voidtype_instantiation(instance):
    assert isinstance(instance, eol_VoidType)

@given(instance=eol_ModelType_strategy)
@settings(max_examples=50)
def test_eol_modeltype_instantiation(instance):
    assert isinstance(instance, eol_ModelType)



@given(instance=eol_ModelType_strategy)
def test_eol_modeltype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original



@given(instance=eol_ModelType_strategy)
def test_eol_modeltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=RealType_strategy)
@settings(max_examples=50)
def test_realtype_instantiation(instance):
    assert isinstance(instance, RealType)

@given(instance=eol_IntegerType_strategy)
@settings(max_examples=50)
def test_eol_integertype_instantiation(instance):
    assert isinstance(instance, eol_IntegerType)

@given(instance=SummablePrimitiveType_strategy)
@settings(max_examples=50)
def test_summableprimitivetype_instantiation(instance):
    assert isinstance(instance, SummablePrimitiveType)

@given(instance=ComparablePrimitiveType_strategy)
@settings(max_examples=50)
def test_comparableprimitivetype_instantiation(instance):
    assert isinstance(instance, ComparablePrimitiveType)

@given(instance=eol_StringType_strategy)
@settings(max_examples=50)
def test_eol_stringtype_instantiation(instance):
    assert isinstance(instance, eol_StringType)

@given(instance=eol_RealType_strategy)
@settings(max_examples=50)
def test_eol_realtype_instantiation(instance):
    assert isinstance(instance, eol_RealType)
