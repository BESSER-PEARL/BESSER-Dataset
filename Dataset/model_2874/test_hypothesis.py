import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CollectionInitValue,
    dom_ExpRange,
    dom_ExprList,
    AssignmentStatement,
    dom_SpecialAssignmentStatement,
    NameExpression,
    dom_SpecialNameExpression,
    Annotation,
    dom_SimpleAnnotation,
    dom_ModelExpression,
    dom_ShortModelDeclarationExpression,
    SwitchCaseStatement,
    dom_ExecutableAnnotation,
    CollectionType,
    dom_SequenceType,
    dom_OrderedSetType,
    dom_BagType,
    dom_SetType,
    PrimitiveType,
    dom_StringType,
    dom_IntegerType,
    dom_RealType,
    dom_BooleanType,
    Type,
    dom_ModelElementType,
    dom_CollectionType,
    dom_NativeType,
    dom_MapType,
    dom_PrimitiveType,
    dom_AnyType,
    CollectionExpression,
    dom_OrderedSetExpression,
    dom_BagExpression,
    dom_SequenceExpression,
    dom_SetExpression,
    LiteralExpression,
    dom_MapExpression,
    dom_CollectionExpression,
    dom_PrimitiveExpression,
    dom_SwitchCaseDefaultStatement,
    dom_SwitchCaseExpressionStatement,
    UnaryOperatorExpression,
    dom_NotOperatorExpression,
    dom_NegativeOperatorExpression,
    Statement,
    dom_ExpressionStatement,
    dom_DeleteStatement,
    dom_AbortStatement,
    dom_BreakAllStatement,
    dom_ContinueStatement,
    dom_BreakStatement,
    dom_TransactionStatement,
    dom_WhileStatement,
    dom_SwitchCaseStatement,
    dom_ThrowStatement,
    dom_SwitchStatement,
    dom_IfStatement,
    dom_ReturnStatement,
    dom_ForStatement,
    dom_AssignmentStatement,
    PrimitiveExpression,
    dom_RealExpression,
    dom_BooleanExpression,
    BinaryOperatorExpression,
    dom_NotEqualsOperatorExpression,
    dom_OrOperatorExpression,
    dom_PlusOperatorExpression,
    dom_XorOperatorExpression,
    dom_DivideOperatorExpression,
    dom_AndOperatorExpression,
    OperatorExpression,
    dom_UnaryOperatorExpression,
    dom_BinaryOperatorExpression,
    Expression,
    dom_VariableDeclarationExpression,
    dom_FormalParameterExpression,
    dom_EnumerationLiteralExpression,
    dom_ModelElementTypeExpression,
    dom_NewExpression,
    dom_LiteralExpression,
    dom_OperatorExpression,
    dom_MultiplyOperatorExpression,
    dom_MinusOperatorExpression,
    FeatureCallExpression,
    dom_FOLMethodCallExpression,
    dom_PropertyCallExpression,
    dom_MethodCallExpression,
    dom_LessThanOrEqualToOperatorExpression,
    dom_LessThanOperatorExpression,
    dom_IntegerExpression,
    dom_ImpliesOperatorExpression,
    dom_GreaterThanOrEqualToOperatorExpression,
    dom_GreaterThanOperatorExpression,
    dom_FeatureCallExpression,
    dom_EqualsOperatorExpression,
    dom_DomElement,
    dom_StringExpression,
    dom_ModelDeclarationStatement,
    dom_NameExpression,
    DomElement,
    dom_KeyValue,
    dom_Annotation,
    dom_Block,
    dom_OperationDefinition,
    dom_Expression,
    dom_Type,
    dom_CollectionInitValue,
    dom_AnnotationBlock,
    dom_Import,
    dom_ModelDeclarationParameter,
    dom_Statement,
    dom_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(CollectionInitValue)


def test_collectioninitvalue_constructor_exists():
    assert callable(CollectionInitValue.__init__)


def test_collectioninitvalue_constructor_args():
    sig = inspect.signature(CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_exprange_is_not_abstract():
    assert not inspect.isabstract(dom_ExpRange)


def test_dom_exprange_constructor_exists():
    assert callable(dom_ExpRange.__init__)


def test_dom_exprange_constructor_args():
    sig = inspect.signature(dom_ExpRange.__init__)
    params = list(sig.parameters.keys())



def test_dom_exprlist_is_not_abstract():
    assert not inspect.isabstract(dom_ExprList)


def test_dom_exprlist_constructor_exists():
    assert callable(dom_ExprList.__init__)


def test_dom_exprlist_constructor_args():
    sig = inspect.signature(dom_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SpecialAssignmentStatement)


def test_dom_specialassignmentstatement_constructor_exists():
    assert callable(dom_SpecialAssignmentStatement.__init__)


def test_dom_specialassignmentstatement_constructor_args():
    sig = inspect.signature(dom_SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_nameexpression_is_not_abstract():
    assert not inspect.isabstract(NameExpression)


def test_nameexpression_constructor_exists():
    assert callable(NameExpression.__init__)


def test_nameexpression_constructor_args():
    sig = inspect.signature(NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_specialnameexpression_is_not_abstract():
    assert not inspect.isabstract(dom_SpecialNameExpression)


def test_dom_specialnameexpression_constructor_exists():
    assert callable(dom_SpecialNameExpression.__init__)


def test_dom_specialnameexpression_constructor_args():
    sig = inspect.signature(dom_SpecialNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_simpleannotation_is_not_abstract():
    assert not inspect.isabstract(dom_SimpleAnnotation)


def test_dom_simpleannotation_constructor_exists():
    assert callable(dom_SimpleAnnotation.__init__)


def test_dom_simpleannotation_constructor_args():
    sig = inspect.signature(dom_SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_modelexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ModelExpression)


def test_dom_modelexpression_constructor_exists():
    assert callable(dom_ModelExpression.__init__)


def test_dom_modelexpression_constructor_args():
    sig = inspect.signature(dom_ModelExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_shortmodeldeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ShortModelDeclarationExpression)


def test_dom_shortmodeldeclarationexpression_constructor_exists():
    assert callable(dom_ShortModelDeclarationExpression.__init__)


def test_dom_shortmodeldeclarationexpression_constructor_args():
    sig = inspect.signature(dom_ShortModelDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_executableannotation_is_not_abstract():
    assert not inspect.isabstract(dom_ExecutableAnnotation)


def test_dom_executableannotation_constructor_exists():
    assert callable(dom_ExecutableAnnotation.__init__)


def test_dom_executableannotation_constructor_args():
    sig = inspect.signature(dom_ExecutableAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_dom_sequencetype_is_not_abstract():
    assert not inspect.isabstract(dom_SequenceType)


def test_dom_sequencetype_constructor_exists():
    assert callable(dom_SequenceType.__init__)


def test_dom_sequencetype_constructor_args():
    sig = inspect.signature(dom_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_dom_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(dom_OrderedSetType)


def test_dom_orderedsettype_constructor_exists():
    assert callable(dom_OrderedSetType.__init__)


def test_dom_orderedsettype_constructor_args():
    sig = inspect.signature(dom_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_dom_bagtype_is_not_abstract():
    assert not inspect.isabstract(dom_BagType)


def test_dom_bagtype_constructor_exists():
    assert callable(dom_BagType.__init__)


def test_dom_bagtype_constructor_args():
    sig = inspect.signature(dom_BagType.__init__)
    params = list(sig.parameters.keys())



def test_dom_settype_is_not_abstract():
    assert not inspect.isabstract(dom_SetType)


def test_dom_settype_constructor_exists():
    assert callable(dom_SetType.__init__)


def test_dom_settype_constructor_args():
    sig = inspect.signature(dom_SetType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dom_stringtype_is_not_abstract():
    assert not inspect.isabstract(dom_StringType)


def test_dom_stringtype_constructor_exists():
    assert callable(dom_StringType.__init__)


def test_dom_stringtype_constructor_args():
    sig = inspect.signature(dom_StringType.__init__)
    params = list(sig.parameters.keys())



def test_dom_integertype_is_not_abstract():
    assert not inspect.isabstract(dom_IntegerType)


def test_dom_integertype_constructor_exists():
    assert callable(dom_IntegerType.__init__)


def test_dom_integertype_constructor_args():
    sig = inspect.signature(dom_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_dom_realtype_is_not_abstract():
    assert not inspect.isabstract(dom_RealType)


def test_dom_realtype_constructor_exists():
    assert callable(dom_RealType.__init__)


def test_dom_realtype_constructor_args():
    sig = inspect.signature(dom_RealType.__init__)
    params = list(sig.parameters.keys())



def test_dom_booleantype_is_not_abstract():
    assert not inspect.isabstract(dom_BooleanType)


def test_dom_booleantype_constructor_exists():
    assert callable(dom_BooleanType.__init__)


def test_dom_booleantype_constructor_args():
    sig = inspect.signature(dom_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dom_modelelementtype_is_not_abstract():
    assert not inspect.isabstract(dom_ModelElementType)


def test_dom_modelelementtype_constructor_exists():
    assert callable(dom_ModelElementType.__init__)


def test_dom_modelelementtype_constructor_args():
    sig = inspect.signature(dom_ModelElementType.__init__)
    params = list(sig.parameters.keys())



def test_dom_collectiontype_is_not_abstract():
    assert not inspect.isabstract(dom_CollectionType)


def test_dom_collectiontype_constructor_exists():
    assert callable(dom_CollectionType.__init__)


def test_dom_collectiontype_constructor_args():
    sig = inspect.signature(dom_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_dom_nativetype_is_not_abstract():
    assert not inspect.isabstract(dom_NativeType)


def test_dom_nativetype_constructor_exists():
    assert callable(dom_NativeType.__init__)


def test_dom_nativetype_constructor_args():
    sig = inspect.signature(dom_NativeType.__init__)
    params = list(sig.parameters.keys())



def test_dom_maptype_is_not_abstract():
    assert not inspect.isabstract(dom_MapType)


def test_dom_maptype_constructor_exists():
    assert callable(dom_MapType.__init__)


def test_dom_maptype_constructor_args():
    sig = inspect.signature(dom_MapType.__init__)
    params = list(sig.parameters.keys())



def test_dom_primitivetype_is_not_abstract():
    assert not inspect.isabstract(dom_PrimitiveType)


def test_dom_primitivetype_constructor_exists():
    assert callable(dom_PrimitiveType.__init__)


def test_dom_primitivetype_constructor_args():
    sig = inspect.signature(dom_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dom_anytype_is_not_abstract():
    assert not inspect.isabstract(dom_AnyType)


def test_dom_anytype_constructor_exists():
    assert callable(dom_AnyType.__init__)


def test_dom_anytype_constructor_args():
    sig = inspect.signature(dom_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(dom_OrderedSetExpression)


def test_dom_orderedsetexpression_constructor_exists():
    assert callable(dom_OrderedSetExpression.__init__)


def test_dom_orderedsetexpression_constructor_args():
    sig = inspect.signature(dom_OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_bagexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BagExpression)


def test_dom_bagexpression_constructor_exists():
    assert callable(dom_BagExpression.__init__)


def test_dom_bagexpression_constructor_args():
    sig = inspect.signature(dom_BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(dom_SequenceExpression)


def test_dom_sequenceexpression_constructor_exists():
    assert callable(dom_SequenceExpression.__init__)


def test_dom_sequenceexpression_constructor_args():
    sig = inspect.signature(dom_SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_setexpression_is_not_abstract():
    assert not inspect.isabstract(dom_SetExpression)


def test_dom_setexpression_constructor_exists():
    assert callable(dom_SetExpression.__init__)


def test_dom_setexpression_constructor_args():
    sig = inspect.signature(dom_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_mapexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MapExpression)


def test_dom_mapexpression_constructor_exists():
    assert callable(dom_MapExpression.__init__)


def test_dom_mapexpression_constructor_args():
    sig = inspect.signature(dom_MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(dom_CollectionExpression)


def test_dom_collectionexpression_constructor_exists():
    assert callable(dom_CollectionExpression.__init__)


def test_dom_collectionexpression_constructor_args():
    sig = inspect.signature(dom_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(dom_PrimitiveExpression)


def test_dom_primitiveexpression_constructor_exists():
    assert callable(dom_PrimitiveExpression.__init__)


def test_dom_primitiveexpression_constructor_args():
    sig = inspect.signature(dom_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchCaseDefaultStatement)


def test_dom_switchcasedefaultstatement_constructor_exists():
    assert callable(dom_SwitchCaseDefaultStatement.__init__)


def test_dom_switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(dom_SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchCaseExpressionStatement)


def test_dom_switchcaseexpressionstatement_constructor_exists():
    assert callable(dom_SwitchCaseExpressionStatement.__init__)


def test_dom_switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(dom_SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NotOperatorExpression)


def test_dom_notoperatorexpression_constructor_exists():
    assert callable(dom_NotOperatorExpression.__init__)


def test_dom_notoperatorexpression_constructor_args():
    sig = inspect.signature(dom_NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NegativeOperatorExpression)


def test_dom_negativeoperatorexpression_constructor_exists():
    assert callable(dom_NegativeOperatorExpression.__init__)


def test_dom_negativeoperatorexpression_constructor_args():
    sig = inspect.signature(dom_NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ExpressionStatement)


def test_dom_expressionstatement_constructor_exists():
    assert callable(dom_ExpressionStatement.__init__)


def test_dom_expressionstatement_constructor_args():
    sig = inspect.signature(dom_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_deletestatement_is_not_abstract():
    assert not inspect.isabstract(dom_DeleteStatement)


def test_dom_deletestatement_constructor_exists():
    assert callable(dom_DeleteStatement.__init__)


def test_dom_deletestatement_constructor_args():
    sig = inspect.signature(dom_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_abortstatement_is_not_abstract():
    assert not inspect.isabstract(dom_AbortStatement)


def test_dom_abortstatement_constructor_exists():
    assert callable(dom_AbortStatement.__init__)


def test_dom_abortstatement_constructor_args():
    sig = inspect.signature(dom_AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_breakallstatement_is_not_abstract():
    assert not inspect.isabstract(dom_BreakAllStatement)


def test_dom_breakallstatement_constructor_exists():
    assert callable(dom_BreakAllStatement.__init__)


def test_dom_breakallstatement_constructor_args():
    sig = inspect.signature(dom_BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(dom_ContinueStatement)


def test_dom_continuestatement_constructor_exists():
    assert callable(dom_ContinueStatement.__init__)


def test_dom_continuestatement_constructor_args():
    sig = inspect.signature(dom_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(dom_BreakStatement)


def test_dom_breakstatement_constructor_exists():
    assert callable(dom_BreakStatement.__init__)


def test_dom_breakstatement_constructor_args():
    sig = inspect.signature(dom_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_transactionstatement_is_not_abstract():
    assert not inspect.isabstract(dom_TransactionStatement)


def test_dom_transactionstatement_constructor_exists():
    assert callable(dom_TransactionStatement.__init__)


def test_dom_transactionstatement_constructor_args():
    sig = inspect.signature(dom_TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(dom_WhileStatement)


def test_dom_whilestatement_constructor_exists():
    assert callable(dom_WhileStatement.__init__)


def test_dom_whilestatement_constructor_args():
    sig = inspect.signature(dom_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchCaseStatement)


def test_dom_switchcasestatement_constructor_exists():
    assert callable(dom_SwitchCaseStatement.__init__)


def test_dom_switchcasestatement_constructor_args():
    sig = inspect.signature(dom_SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_throwstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ThrowStatement)


def test_dom_throwstatement_constructor_exists():
    assert callable(dom_ThrowStatement.__init__)


def test_dom_throwstatement_constructor_args():
    sig = inspect.signature(dom_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_switchstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchStatement)


def test_dom_switchstatement_constructor_exists():
    assert callable(dom_SwitchStatement.__init__)


def test_dom_switchstatement_constructor_args():
    sig = inspect.signature(dom_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(dom_IfStatement)


def test_dom_ifstatement_constructor_exists():
    assert callable(dom_IfStatement.__init__)


def test_dom_ifstatement_constructor_args():
    sig = inspect.signature(dom_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_returnstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ReturnStatement)


def test_dom_returnstatement_constructor_exists():
    assert callable(dom_ReturnStatement.__init__)


def test_dom_returnstatement_constructor_args():
    sig = inspect.signature(dom_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_forstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ForStatement)


def test_dom_forstatement_constructor_exists():
    assert callable(dom_ForStatement.__init__)


def test_dom_forstatement_constructor_args():
    sig = inspect.signature(dom_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(dom_AssignmentStatement)


def test_dom_assignmentstatement_constructor_exists():
    assert callable(dom_AssignmentStatement.__init__)


def test_dom_assignmentstatement_constructor_args():
    sig = inspect.signature(dom_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_realexpression_is_not_abstract():
    assert not inspect.isabstract(dom_RealExpression)


def test_dom_realexpression_constructor_exists():
    assert callable(dom_RealExpression.__init__)


def test_dom_realexpression_constructor_args():
    sig = inspect.signature(dom_RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom_realexpression_has_val():
    assert hasattr(dom_RealExpression, "val")
    descriptor = None
    for klass in dom_RealExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BooleanExpression)


def test_dom_booleanexpression_constructor_exists():
    assert callable(dom_BooleanExpression.__init__)


def test_dom_booleanexpression_constructor_args():
    sig = inspect.signature(dom_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom_booleanexpression_has_val():
    assert hasattr(dom_BooleanExpression, "val")
    descriptor = None
    for klass in dom_BooleanExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NotEqualsOperatorExpression)


def test_dom_notequalsoperatorexpression_constructor_exists():
    assert callable(dom_NotEqualsOperatorExpression.__init__)


def test_dom_notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(dom_NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_OrOperatorExpression)


def test_dom_oroperatorexpression_constructor_exists():
    assert callable(dom_OrOperatorExpression.__init__)


def test_dom_oroperatorexpression_constructor_args():
    sig = inspect.signature(dom_OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_PlusOperatorExpression)


def test_dom_plusoperatorexpression_constructor_exists():
    assert callable(dom_PlusOperatorExpression.__init__)


def test_dom_plusoperatorexpression_constructor_args():
    sig = inspect.signature(dom_PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_XorOperatorExpression)


def test_dom_xoroperatorexpression_constructor_exists():
    assert callable(dom_XorOperatorExpression.__init__)


def test_dom_xoroperatorexpression_constructor_args():
    sig = inspect.signature(dom_XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_DivideOperatorExpression)


def test_dom_divideoperatorexpression_constructor_exists():
    assert callable(dom_DivideOperatorExpression.__init__)


def test_dom_divideoperatorexpression_constructor_args():
    sig = inspect.signature(dom_DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_AndOperatorExpression)


def test_dom_andoperatorexpression_constructor_exists():
    assert callable(dom_AndOperatorExpression.__init__)


def test_dom_andoperatorexpression_constructor_args():
    sig = inspect.signature(dom_AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_UnaryOperatorExpression)


def test_dom_unaryoperatorexpression_constructor_exists():
    assert callable(dom_UnaryOperatorExpression.__init__)


def test_dom_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(dom_UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BinaryOperatorExpression)


def test_dom_binaryoperatorexpression_constructor_exists():
    assert callable(dom_BinaryOperatorExpression.__init__)


def test_dom_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(dom_BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(dom_VariableDeclarationExpression)


def test_dom_variabledeclarationexpression_constructor_exists():
    assert callable(dom_VariableDeclarationExpression.__init__)


def test_dom_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(dom_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(dom_FormalParameterExpression)


def test_dom_formalparameterexpression_constructor_exists():
    assert callable(dom_FormalParameterExpression.__init__)


def test_dom_formalparameterexpression_constructor_args():
    sig = inspect.signature(dom_FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(dom_EnumerationLiteralExpression)


def test_dom_enumerationliteralexpression_constructor_exists():
    assert callable(dom_EnumerationLiteralExpression.__init__)


def test_dom_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(dom_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_modelelementtypeexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ModelElementTypeExpression)


def test_dom_modelelementtypeexpression_constructor_exists():
    assert callable(dom_ModelElementTypeExpression.__init__)


def test_dom_modelelementtypeexpression_constructor_args():
    sig = inspect.signature(dom_ModelElementTypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_newexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NewExpression)


def test_dom_newexpression_constructor_exists():
    assert callable(dom_NewExpression.__init__)


def test_dom_newexpression_constructor_args():
    sig = inspect.signature(dom_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_literalexpression_is_not_abstract():
    assert not inspect.isabstract(dom_LiteralExpression)


def test_dom_literalexpression_constructor_exists():
    assert callable(dom_LiteralExpression.__init__)


def test_dom_literalexpression_constructor_args():
    sig = inspect.signature(dom_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_OperatorExpression)


def test_dom_operatorexpression_constructor_exists():
    assert callable(dom_OperatorExpression.__init__)


def test_dom_operatorexpression_constructor_args():
    sig = inspect.signature(dom_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MultiplyOperatorExpression)


def test_dom_multiplyoperatorexpression_constructor_exists():
    assert callable(dom_MultiplyOperatorExpression.__init__)


def test_dom_multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(dom_MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MinusOperatorExpression)


def test_dom_minusoperatorexpression_constructor_exists():
    assert callable(dom_MinusOperatorExpression.__init__)


def test_dom_minusoperatorexpression_constructor_args():
    sig = inspect.signature(dom_MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(dom_FOLMethodCallExpression)


def test_dom_folmethodcallexpression_constructor_exists():
    assert callable(dom_FOLMethodCallExpression.__init__)


def test_dom_folmethodcallexpression_constructor_args():
    sig = inspect.signature(dom_FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyCallExpression)


def test_dom_propertycallexpression_constructor_exists():
    assert callable(dom_PropertyCallExpression.__init__)


def test_dom_propertycallexpression_constructor_args():
    sig = inspect.signature(dom_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(dom_MethodCallExpression)


def test_dom_methodcallexpression_constructor_exists():
    assert callable(dom_MethodCallExpression.__init__)


def test_dom_methodcallexpression_constructor_args():
    sig = inspect.signature(dom_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_LessThanOrEqualToOperatorExpression)


def test_dom_lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(dom_LessThanOrEqualToOperatorExpression.__init__)


def test_dom_lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(dom_LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_LessThanOperatorExpression)


def test_dom_lessthanoperatorexpression_constructor_exists():
    assert callable(dom_LessThanOperatorExpression.__init__)


def test_dom_lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(dom_LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_integerexpression_is_not_abstract():
    assert not inspect.isabstract(dom_IntegerExpression)


def test_dom_integerexpression_constructor_exists():
    assert callable(dom_IntegerExpression.__init__)


def test_dom_integerexpression_constructor_args():
    sig = inspect.signature(dom_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom_integerexpression_has_val():
    assert hasattr(dom_IntegerExpression, "val")
    descriptor = None
    for klass in dom_IntegerExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom_impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ImpliesOperatorExpression)


def test_dom_impliesoperatorexpression_constructor_exists():
    assert callable(dom_ImpliesOperatorExpression.__init__)


def test_dom_impliesoperatorexpression_constructor_args():
    sig = inspect.signature(dom_ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_GreaterThanOrEqualToOperatorExpression)


def test_dom_greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(dom_GreaterThanOrEqualToOperatorExpression.__init__)


def test_dom_greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(dom_GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_GreaterThanOperatorExpression)


def test_dom_greaterthanoperatorexpression_constructor_exists():
    assert callable(dom_GreaterThanOperatorExpression.__init__)


def test_dom_greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(dom_GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(dom_FeatureCallExpression)


def test_dom_featurecallexpression_constructor_exists():
    assert callable(dom_FeatureCallExpression.__init__)


def test_dom_featurecallexpression_constructor_args():
    sig = inspect.signature(dom_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom_EqualsOperatorExpression)


def test_dom_equalsoperatorexpression_constructor_exists():
    assert callable(dom_EqualsOperatorExpression.__init__)


def test_dom_equalsoperatorexpression_constructor_args():
    sig = inspect.signature(dom_EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom_domelement_is_not_abstract():
    assert not inspect.isabstract(dom_DomElement)


def test_dom_domelement_constructor_exists():
    assert callable(dom_DomElement.__init__)


def test_dom_domelement_constructor_args():
    sig = inspect.signature(dom_DomElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"

def test_dom_domelement_has_line():
    assert hasattr(dom_DomElement, "line")
    descriptor = None
    for klass in dom_DomElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_dom_domelement_has_column():
    assert hasattr(dom_DomElement, "column")
    descriptor = None
    for klass in dom_DomElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_dom_stringexpression_is_not_abstract():
    assert not inspect.isabstract(dom_StringExpression)


def test_dom_stringexpression_constructor_exists():
    assert callable(dom_StringExpression.__init__)


def test_dom_stringexpression_constructor_args():
    sig = inspect.signature(dom_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom_stringexpression_has_val():
    assert hasattr(dom_StringExpression, "val")
    descriptor = None
    for klass in dom_StringExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom_modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ModelDeclarationStatement)


def test_dom_modeldeclarationstatement_constructor_exists():
    assert callable(dom_ModelDeclarationStatement.__init__)


def test_dom_modeldeclarationstatement_constructor_args():
    sig = inspect.signature(dom_ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom_nameexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NameExpression)


def test_dom_nameexpression_constructor_exists():
    assert callable(dom_NameExpression.__init__)


def test_dom_nameexpression_constructor_args():
    sig = inspect.signature(dom_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom_nameexpression_has_name():
    assert hasattr(dom_NameExpression, "name")
    descriptor = None
    for klass in dom_NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domelement_is_not_abstract():
    assert not inspect.isabstract(DomElement)


def test_domelement_constructor_exists():
    assert callable(DomElement.__init__)


def test_domelement_constructor_args():
    sig = inspect.signature(DomElement.__init__)
    params = list(sig.parameters.keys())



def test_dom_keyvalue_is_not_abstract():
    assert not inspect.isabstract(dom_KeyValue)


def test_dom_keyvalue_constructor_exists():
    assert callable(dom_KeyValue.__init__)


def test_dom_keyvalue_constructor_args():
    sig = inspect.signature(dom_KeyValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_annotation_is_not_abstract():
    assert not inspect.isabstract(dom_Annotation)


def test_dom_annotation_constructor_exists():
    assert callable(dom_Annotation.__init__)


def test_dom_annotation_constructor_args():
    sig = inspect.signature(dom_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom_block_is_not_abstract():
    assert not inspect.isabstract(dom_Block)


def test_dom_block_constructor_exists():
    assert callable(dom_Block.__init__)


def test_dom_block_constructor_args():
    sig = inspect.signature(dom_Block.__init__)
    params = list(sig.parameters.keys())



def test_dom_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(dom_OperationDefinition)


def test_dom_operationdefinition_constructor_exists():
    assert callable(dom_OperationDefinition.__init__)


def test_dom_operationdefinition_constructor_args():
    sig = inspect.signature(dom_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dom_expression_is_not_abstract():
    assert not inspect.isabstract(dom_Expression)


def test_dom_expression_constructor_exists():
    assert callable(dom_Expression.__init__)


def test_dom_expression_constructor_args():
    sig = inspect.signature(dom_Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom_type_is_not_abstract():
    assert not inspect.isabstract(dom_Type)


def test_dom_type_constructor_exists():
    assert callable(dom_Type.__init__)


def test_dom_type_constructor_args():
    sig = inspect.signature(dom_Type.__init__)
    params = list(sig.parameters.keys())



def test_dom_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(dom_CollectionInitValue)


def test_dom_collectioninitvalue_constructor_exists():
    assert callable(dom_CollectionInitValue.__init__)


def test_dom_collectioninitvalue_constructor_args():
    sig = inspect.signature(dom_CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_dom_annotationblock_is_not_abstract():
    assert not inspect.isabstract(dom_AnnotationBlock)


def test_dom_annotationblock_constructor_exists():
    assert callable(dom_AnnotationBlock.__init__)


def test_dom_annotationblock_constructor_args():
    sig = inspect.signature(dom_AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_dom_import_is_not_abstract():
    assert not inspect.isabstract(dom_Import)


def test_dom_import_constructor_exists():
    assert callable(dom_Import.__init__)


def test_dom_import_constructor_args():
    sig = inspect.signature(dom_Import.__init__)
    params = list(sig.parameters.keys())



def test_dom_modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(dom_ModelDeclarationParameter)


def test_dom_modeldeclarationparameter_constructor_exists():
    assert callable(dom_ModelDeclarationParameter.__init__)


def test_dom_modeldeclarationparameter_constructor_args():
    sig = inspect.signature(dom_ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom_statement_is_not_abstract():
    assert not inspect.isabstract(dom_Statement)


def test_dom_statement_constructor_exists():
    assert callable(dom_Statement.__init__)


def test_dom_statement_constructor_args():
    sig = inspect.signature(dom_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom_program_is_not_abstract():
    assert not inspect.isabstract(dom_Program)


def test_dom_program_constructor_exists():
    assert callable(dom_Program.__init__)


def test_dom_program_constructor_args():
    sig = inspect.signature(dom_Program.__init__)
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
CollectionInitValue_strategy = st.builds(
    CollectionInitValue,
)
dom_ExpRange_strategy = st.builds(
    dom_ExpRange,
)
dom_ExprList_strategy = st.builds(
    dom_ExprList,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
dom_SpecialAssignmentStatement_strategy = st.builds(
    dom_SpecialAssignmentStatement,
)
NameExpression_strategy = st.builds(
    NameExpression,
)
dom_SpecialNameExpression_strategy = st.builds(
    dom_SpecialNameExpression,
)
Annotation_strategy = st.builds(
    Annotation,
)
dom_SimpleAnnotation_strategy = st.builds(
    dom_SimpleAnnotation,
)
dom_ModelExpression_strategy = st.builds(
    dom_ModelExpression,
)
dom_ShortModelDeclarationExpression_strategy = st.builds(
    dom_ShortModelDeclarationExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
dom_ExecutableAnnotation_strategy = st.builds(
    dom_ExecutableAnnotation,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
dom_SequenceType_strategy = st.builds(
    dom_SequenceType,
)
dom_OrderedSetType_strategy = st.builds(
    dom_OrderedSetType,
)
dom_BagType_strategy = st.builds(
    dom_BagType,
)
dom_SetType_strategy = st.builds(
    dom_SetType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dom_StringType_strategy = st.builds(
    dom_StringType,
)
dom_IntegerType_strategy = st.builds(
    dom_IntegerType,
)
dom_RealType_strategy = st.builds(
    dom_RealType,
)
dom_BooleanType_strategy = st.builds(
    dom_BooleanType,
)
Type_strategy = st.builds(
    Type,
)
dom_ModelElementType_strategy = st.builds(
    dom_ModelElementType,
)
dom_CollectionType_strategy = st.builds(
    dom_CollectionType,
)
dom_NativeType_strategy = st.builds(
    dom_NativeType,
)
dom_MapType_strategy = st.builds(
    dom_MapType,
)
dom_PrimitiveType_strategy = st.builds(
    dom_PrimitiveType,
)
dom_AnyType_strategy = st.builds(
    dom_AnyType,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
dom_OrderedSetExpression_strategy = st.builds(
    dom_OrderedSetExpression,
)
dom_BagExpression_strategy = st.builds(
    dom_BagExpression,
)
dom_SequenceExpression_strategy = st.builds(
    dom_SequenceExpression,
)
dom_SetExpression_strategy = st.builds(
    dom_SetExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
dom_MapExpression_strategy = st.builds(
    dom_MapExpression,
)
dom_CollectionExpression_strategy = st.builds(
    dom_CollectionExpression,
)
dom_PrimitiveExpression_strategy = st.builds(
    dom_PrimitiveExpression,
)
dom_SwitchCaseDefaultStatement_strategy = st.builds(
    dom_SwitchCaseDefaultStatement,
)
dom_SwitchCaseExpressionStatement_strategy = st.builds(
    dom_SwitchCaseExpressionStatement,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
dom_NotOperatorExpression_strategy = st.builds(
    dom_NotOperatorExpression,
)
dom_NegativeOperatorExpression_strategy = st.builds(
    dom_NegativeOperatorExpression,
)
Statement_strategy = st.builds(
    Statement,
)
dom_ExpressionStatement_strategy = st.builds(
    dom_ExpressionStatement,
)
dom_DeleteStatement_strategy = st.builds(
    dom_DeleteStatement,
)
dom_AbortStatement_strategy = st.builds(
    dom_AbortStatement,
)
dom_BreakAllStatement_strategy = st.builds(
    dom_BreakAllStatement,
)
dom_ContinueStatement_strategy = st.builds(
    dom_ContinueStatement,
)
dom_BreakStatement_strategy = st.builds(
    dom_BreakStatement,
)
dom_TransactionStatement_strategy = st.builds(
    dom_TransactionStatement,
)
dom_WhileStatement_strategy = st.builds(
    dom_WhileStatement,
)
dom_SwitchCaseStatement_strategy = st.builds(
    dom_SwitchCaseStatement,
)
dom_ThrowStatement_strategy = st.builds(
    dom_ThrowStatement,
)
dom_SwitchStatement_strategy = st.builds(
    dom_SwitchStatement,
)
dom_IfStatement_strategy = st.builds(
    dom_IfStatement,
)
dom_ReturnStatement_strategy = st.builds(
    dom_ReturnStatement,
)
dom_ForStatement_strategy = st.builds(
    dom_ForStatement,
)
dom_AssignmentStatement_strategy = st.builds(
    dom_AssignmentStatement,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
dom_RealExpression_strategy = st.builds(
    dom_RealExpression,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dom_BooleanExpression_strategy = st.builds(
    dom_BooleanExpression,
    val=
        st.booleans()
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
dom_NotEqualsOperatorExpression_strategy = st.builds(
    dom_NotEqualsOperatorExpression,
)
dom_OrOperatorExpression_strategy = st.builds(
    dom_OrOperatorExpression,
)
dom_PlusOperatorExpression_strategy = st.builds(
    dom_PlusOperatorExpression,
)
dom_XorOperatorExpression_strategy = st.builds(
    dom_XorOperatorExpression,
)
dom_DivideOperatorExpression_strategy = st.builds(
    dom_DivideOperatorExpression,
)
dom_AndOperatorExpression_strategy = st.builds(
    dom_AndOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
dom_UnaryOperatorExpression_strategy = st.builds(
    dom_UnaryOperatorExpression,
)
dom_BinaryOperatorExpression_strategy = st.builds(
    dom_BinaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
dom_VariableDeclarationExpression_strategy = st.builds(
    dom_VariableDeclarationExpression,
)
dom_FormalParameterExpression_strategy = st.builds(
    dom_FormalParameterExpression,
)
dom_EnumerationLiteralExpression_strategy = st.builds(
    dom_EnumerationLiteralExpression,
)
dom_ModelElementTypeExpression_strategy = st.builds(
    dom_ModelElementTypeExpression,
)
dom_NewExpression_strategy = st.builds(
    dom_NewExpression,
)
dom_LiteralExpression_strategy = st.builds(
    dom_LiteralExpression,
)
dom_OperatorExpression_strategy = st.builds(
    dom_OperatorExpression,
)
dom_MultiplyOperatorExpression_strategy = st.builds(
    dom_MultiplyOperatorExpression,
)
dom_MinusOperatorExpression_strategy = st.builds(
    dom_MinusOperatorExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
dom_FOLMethodCallExpression_strategy = st.builds(
    dom_FOLMethodCallExpression,
)
dom_PropertyCallExpression_strategy = st.builds(
    dom_PropertyCallExpression,
)
dom_MethodCallExpression_strategy = st.builds(
    dom_MethodCallExpression,
)
dom_LessThanOrEqualToOperatorExpression_strategy = st.builds(
    dom_LessThanOrEqualToOperatorExpression,
)
dom_LessThanOperatorExpression_strategy = st.builds(
    dom_LessThanOperatorExpression,
)
dom_IntegerExpression_strategy = st.builds(
    dom_IntegerExpression,
    val=
        st.integers()
)
dom_ImpliesOperatorExpression_strategy = st.builds(
    dom_ImpliesOperatorExpression,
)
dom_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    dom_GreaterThanOrEqualToOperatorExpression,
)
dom_GreaterThanOperatorExpression_strategy = st.builds(
    dom_GreaterThanOperatorExpression,
)
dom_FeatureCallExpression_strategy = st.builds(
    dom_FeatureCallExpression,
)
dom_EqualsOperatorExpression_strategy = st.builds(
    dom_EqualsOperatorExpression,
)
dom_DomElement_strategy = st.builds(
    dom_DomElement,
    line=
        st.integers(),
    column=
        st.integers()
)
dom_StringExpression_strategy = st.builds(
    dom_StringExpression,
    val=
        safe_text
)
dom_ModelDeclarationStatement_strategy = st.builds(
    dom_ModelDeclarationStatement,
)
dom_NameExpression_strategy = st.builds(
    dom_NameExpression,
    name=
        safe_text
)
DomElement_strategy = st.builds(
    DomElement,
)
dom_KeyValue_strategy = st.builds(
    dom_KeyValue,
)
dom_Annotation_strategy = st.builds(
    dom_Annotation,
)
dom_Block_strategy = st.builds(
    dom_Block,
)
dom_OperationDefinition_strategy = st.builds(
    dom_OperationDefinition,
)
dom_Expression_strategy = st.builds(
    dom_Expression,
)
dom_Type_strategy = st.builds(
    dom_Type,
)
dom_CollectionInitValue_strategy = st.builds(
    dom_CollectionInitValue,
)
dom_AnnotationBlock_strategy = st.builds(
    dom_AnnotationBlock,
)
dom_Import_strategy = st.builds(
    dom_Import,
)
dom_ModelDeclarationParameter_strategy = st.builds(
    dom_ModelDeclarationParameter,
)
dom_Statement_strategy = st.builds(
    dom_Statement,
)
dom_Program_strategy = st.builds(
    dom_Program,
)

@given(instance=CollectionInitValue_strategy)
@settings(max_examples=50)
def test_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, CollectionInitValue)

@given(instance=dom_ExpRange_strategy)
@settings(max_examples=50)
def test_dom_exprange_instantiation(instance):
    assert isinstance(instance, dom_ExpRange)

@given(instance=dom_ExprList_strategy)
@settings(max_examples=50)
def test_dom_exprlist_instantiation(instance):
    assert isinstance(instance, dom_ExprList)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=dom_SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_dom_specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, dom_SpecialAssignmentStatement)

@given(instance=NameExpression_strategy)
@settings(max_examples=50)
def test_nameexpression_instantiation(instance):
    assert isinstance(instance, NameExpression)

@given(instance=dom_SpecialNameExpression_strategy)
@settings(max_examples=50)
def test_dom_specialnameexpression_instantiation(instance):
    assert isinstance(instance, dom_SpecialNameExpression)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=dom_SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_dom_simpleannotation_instantiation(instance):
    assert isinstance(instance, dom_SimpleAnnotation)

@given(instance=dom_ModelExpression_strategy)
@settings(max_examples=50)
def test_dom_modelexpression_instantiation(instance):
    assert isinstance(instance, dom_ModelExpression)

@given(instance=dom_ShortModelDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom_shortmodeldeclarationexpression_instantiation(instance):
    assert isinstance(instance, dom_ShortModelDeclarationExpression)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=dom_ExecutableAnnotation_strategy)
@settings(max_examples=50)
def test_dom_executableannotation_instantiation(instance):
    assert isinstance(instance, dom_ExecutableAnnotation)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=dom_SequenceType_strategy)
@settings(max_examples=50)
def test_dom_sequencetype_instantiation(instance):
    assert isinstance(instance, dom_SequenceType)

@given(instance=dom_OrderedSetType_strategy)
@settings(max_examples=50)
def test_dom_orderedsettype_instantiation(instance):
    assert isinstance(instance, dom_OrderedSetType)

@given(instance=dom_BagType_strategy)
@settings(max_examples=50)
def test_dom_bagtype_instantiation(instance):
    assert isinstance(instance, dom_BagType)

@given(instance=dom_SetType_strategy)
@settings(max_examples=50)
def test_dom_settype_instantiation(instance):
    assert isinstance(instance, dom_SetType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dom_StringType_strategy)
@settings(max_examples=50)
def test_dom_stringtype_instantiation(instance):
    assert isinstance(instance, dom_StringType)

@given(instance=dom_IntegerType_strategy)
@settings(max_examples=50)
def test_dom_integertype_instantiation(instance):
    assert isinstance(instance, dom_IntegerType)

@given(instance=dom_RealType_strategy)
@settings(max_examples=50)
def test_dom_realtype_instantiation(instance):
    assert isinstance(instance, dom_RealType)

@given(instance=dom_BooleanType_strategy)
@settings(max_examples=50)
def test_dom_booleantype_instantiation(instance):
    assert isinstance(instance, dom_BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dom_ModelElementType_strategy)
@settings(max_examples=50)
def test_dom_modelelementtype_instantiation(instance):
    assert isinstance(instance, dom_ModelElementType)

@given(instance=dom_CollectionType_strategy)
@settings(max_examples=50)
def test_dom_collectiontype_instantiation(instance):
    assert isinstance(instance, dom_CollectionType)

@given(instance=dom_NativeType_strategy)
@settings(max_examples=50)
def test_dom_nativetype_instantiation(instance):
    assert isinstance(instance, dom_NativeType)

@given(instance=dom_MapType_strategy)
@settings(max_examples=50)
def test_dom_maptype_instantiation(instance):
    assert isinstance(instance, dom_MapType)

@given(instance=dom_PrimitiveType_strategy)
@settings(max_examples=50)
def test_dom_primitivetype_instantiation(instance):
    assert isinstance(instance, dom_PrimitiveType)

@given(instance=dom_AnyType_strategy)
@settings(max_examples=50)
def test_dom_anytype_instantiation(instance):
    assert isinstance(instance, dom_AnyType)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=dom_OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_dom_orderedsetexpression_instantiation(instance):
    assert isinstance(instance, dom_OrderedSetExpression)

@given(instance=dom_BagExpression_strategy)
@settings(max_examples=50)
def test_dom_bagexpression_instantiation(instance):
    assert isinstance(instance, dom_BagExpression)

@given(instance=dom_SequenceExpression_strategy)
@settings(max_examples=50)
def test_dom_sequenceexpression_instantiation(instance):
    assert isinstance(instance, dom_SequenceExpression)

@given(instance=dom_SetExpression_strategy)
@settings(max_examples=50)
def test_dom_setexpression_instantiation(instance):
    assert isinstance(instance, dom_SetExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=dom_MapExpression_strategy)
@settings(max_examples=50)
def test_dom_mapexpression_instantiation(instance):
    assert isinstance(instance, dom_MapExpression)

@given(instance=dom_CollectionExpression_strategy)
@settings(max_examples=50)
def test_dom_collectionexpression_instantiation(instance):
    assert isinstance(instance, dom_CollectionExpression)

@given(instance=dom_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_dom_primitiveexpression_instantiation(instance):
    assert isinstance(instance, dom_PrimitiveExpression)

@given(instance=dom_SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_dom_switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseDefaultStatement)

@given(instance=dom_SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom_switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseExpressionStatement)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=dom_NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_notoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_NotOperatorExpression)

@given(instance=dom_NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_NegativeOperatorExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dom_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom_expressionstatement_instantiation(instance):
    assert isinstance(instance, dom_ExpressionStatement)

@given(instance=dom_DeleteStatement_strategy)
@settings(max_examples=50)
def test_dom_deletestatement_instantiation(instance):
    assert isinstance(instance, dom_DeleteStatement)

@given(instance=dom_AbortStatement_strategy)
@settings(max_examples=50)
def test_dom_abortstatement_instantiation(instance):
    assert isinstance(instance, dom_AbortStatement)

@given(instance=dom_BreakAllStatement_strategy)
@settings(max_examples=50)
def test_dom_breakallstatement_instantiation(instance):
    assert isinstance(instance, dom_BreakAllStatement)

@given(instance=dom_ContinueStatement_strategy)
@settings(max_examples=50)
def test_dom_continuestatement_instantiation(instance):
    assert isinstance(instance, dom_ContinueStatement)

@given(instance=dom_BreakStatement_strategy)
@settings(max_examples=50)
def test_dom_breakstatement_instantiation(instance):
    assert isinstance(instance, dom_BreakStatement)

@given(instance=dom_TransactionStatement_strategy)
@settings(max_examples=50)
def test_dom_transactionstatement_instantiation(instance):
    assert isinstance(instance, dom_TransactionStatement)

@given(instance=dom_WhileStatement_strategy)
@settings(max_examples=50)
def test_dom_whilestatement_instantiation(instance):
    assert isinstance(instance, dom_WhileStatement)

@given(instance=dom_SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_dom_switchcasestatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchCaseStatement)

@given(instance=dom_ThrowStatement_strategy)
@settings(max_examples=50)
def test_dom_throwstatement_instantiation(instance):
    assert isinstance(instance, dom_ThrowStatement)

@given(instance=dom_SwitchStatement_strategy)
@settings(max_examples=50)
def test_dom_switchstatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchStatement)

@given(instance=dom_IfStatement_strategy)
@settings(max_examples=50)
def test_dom_ifstatement_instantiation(instance):
    assert isinstance(instance, dom_IfStatement)

@given(instance=dom_ReturnStatement_strategy)
@settings(max_examples=50)
def test_dom_returnstatement_instantiation(instance):
    assert isinstance(instance, dom_ReturnStatement)

@given(instance=dom_ForStatement_strategy)
@settings(max_examples=50)
def test_dom_forstatement_instantiation(instance):
    assert isinstance(instance, dom_ForStatement)

@given(instance=dom_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_dom_assignmentstatement_instantiation(instance):
    assert isinstance(instance, dom_AssignmentStatement)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=dom_RealExpression_strategy)
@settings(max_examples=50)
def test_dom_realexpression_instantiation(instance):
    assert isinstance(instance, dom_RealExpression)



@given(instance=dom_RealExpression_strategy)
def test_dom_realexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom_BooleanExpression_strategy)
@settings(max_examples=50)
def test_dom_booleanexpression_instantiation(instance):
    assert isinstance(instance, dom_BooleanExpression)



@given(instance=dom_BooleanExpression_strategy)
def test_dom_booleanexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=dom_NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_NotEqualsOperatorExpression)

@given(instance=dom_OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_oroperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_OrOperatorExpression)

@given(instance=dom_PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_PlusOperatorExpression)

@given(instance=dom_XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_XorOperatorExpression)

@given(instance=dom_DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_DivideOperatorExpression)

@given(instance=dom_AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_andoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_AndOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=dom_UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_UnaryOperatorExpression)

@given(instance=dom_BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_BinaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dom_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, dom_VariableDeclarationExpression)

@given(instance=dom_FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_dom_formalparameterexpression_instantiation(instance):
    assert isinstance(instance, dom_FormalParameterExpression)

@given(instance=dom_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_dom_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, dom_EnumerationLiteralExpression)

@given(instance=dom_ModelElementTypeExpression_strategy)
@settings(max_examples=50)
def test_dom_modelelementtypeexpression_instantiation(instance):
    assert isinstance(instance, dom_ModelElementTypeExpression)

@given(instance=dom_NewExpression_strategy)
@settings(max_examples=50)
def test_dom_newexpression_instantiation(instance):
    assert isinstance(instance, dom_NewExpression)

@given(instance=dom_LiteralExpression_strategy)
@settings(max_examples=50)
def test_dom_literalexpression_instantiation(instance):
    assert isinstance(instance, dom_LiteralExpression)

@given(instance=dom_OperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_operatorexpression_instantiation(instance):
    assert isinstance(instance, dom_OperatorExpression)

@given(instance=dom_MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_MultiplyOperatorExpression)

@given(instance=dom_MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_MinusOperatorExpression)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=dom_FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_dom_folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, dom_FOLMethodCallExpression)

@given(instance=dom_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_dom_propertycallexpression_instantiation(instance):
    assert isinstance(instance, dom_PropertyCallExpression)

@given(instance=dom_MethodCallExpression_strategy)
@settings(max_examples=50)
def test_dom_methodcallexpression_instantiation(instance):
    assert isinstance(instance, dom_MethodCallExpression)

@given(instance=dom_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_LessThanOrEqualToOperatorExpression)

@given(instance=dom_LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_LessThanOperatorExpression)

@given(instance=dom_IntegerExpression_strategy)
@settings(max_examples=50)
def test_dom_integerexpression_instantiation(instance):
    assert isinstance(instance, dom_IntegerExpression)



@given(instance=dom_IntegerExpression_strategy)
def test_dom_integerexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom_ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_ImpliesOperatorExpression)

@given(instance=dom_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_GreaterThanOrEqualToOperatorExpression)

@given(instance=dom_GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_GreaterThanOperatorExpression)

@given(instance=dom_FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_dom_featurecallexpression_instantiation(instance):
    assert isinstance(instance, dom_FeatureCallExpression)

@given(instance=dom_EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom_equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom_EqualsOperatorExpression)

@given(instance=dom_DomElement_strategy)
@settings(max_examples=50)
def test_dom_domelement_instantiation(instance):
    assert isinstance(instance, dom_DomElement)



@given(instance=dom_DomElement_strategy)
def test_dom_domelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=dom_DomElement_strategy)
def test_dom_domelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=dom_StringExpression_strategy)
@settings(max_examples=50)
def test_dom_stringexpression_instantiation(instance):
    assert isinstance(instance, dom_StringExpression)



@given(instance=dom_StringExpression_strategy)
def test_dom_stringexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom_ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom_modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, dom_ModelDeclarationStatement)

@given(instance=dom_NameExpression_strategy)
@settings(max_examples=50)
def test_dom_nameexpression_instantiation(instance):
    assert isinstance(instance, dom_NameExpression)



@given(instance=dom_NameExpression_strategy)
def test_dom_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomElement_strategy)
@settings(max_examples=50)
def test_domelement_instantiation(instance):
    assert isinstance(instance, DomElement)

@given(instance=dom_KeyValue_strategy)
@settings(max_examples=50)
def test_dom_keyvalue_instantiation(instance):
    assert isinstance(instance, dom_KeyValue)

@given(instance=dom_Annotation_strategy)
@settings(max_examples=50)
def test_dom_annotation_instantiation(instance):
    assert isinstance(instance, dom_Annotation)

@given(instance=dom_Block_strategy)
@settings(max_examples=50)
def test_dom_block_instantiation(instance):
    assert isinstance(instance, dom_Block)

@given(instance=dom_OperationDefinition_strategy)
@settings(max_examples=50)
def test_dom_operationdefinition_instantiation(instance):
    assert isinstance(instance, dom_OperationDefinition)

@given(instance=dom_Expression_strategy)
@settings(max_examples=50)
def test_dom_expression_instantiation(instance):
    assert isinstance(instance, dom_Expression)

@given(instance=dom_Type_strategy)
@settings(max_examples=50)
def test_dom_type_instantiation(instance):
    assert isinstance(instance, dom_Type)

@given(instance=dom_CollectionInitValue_strategy)
@settings(max_examples=50)
def test_dom_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, dom_CollectionInitValue)

@given(instance=dom_AnnotationBlock_strategy)
@settings(max_examples=50)
def test_dom_annotationblock_instantiation(instance):
    assert isinstance(instance, dom_AnnotationBlock)

@given(instance=dom_Import_strategy)
@settings(max_examples=50)
def test_dom_import_instantiation(instance):
    assert isinstance(instance, dom_Import)

@given(instance=dom_ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_dom_modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, dom_ModelDeclarationParameter)

@given(instance=dom_Statement_strategy)
@settings(max_examples=50)
def test_dom_statement_instantiation(instance):
    assert isinstance(instance, dom_Statement)

@given(instance=dom_Program_strategy)
@settings(max_examples=50)
def test_dom_program_instantiation(instance):
    assert isinstance(instance, dom_Program)
