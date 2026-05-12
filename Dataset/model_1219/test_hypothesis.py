import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryOperatorExpression,
    eol_ComparisonOperatorExpression,
    eol_ArithmeticOperatorExpression,
    eol_LogicalOperatorExpression,
    PseudoType,
    eol_OperationArgType,
    eol_SelfInnermostType,
    eol_SelfContentType,
    eol_SelfType,
    AssignmentStatement,
    eol_SpecialAssignmentStatement,
    CollectionInitValue,
    eol_ExpRange,
    eol_ExprList,
    VariableDeclarationExpression,
    eol_EClassifier,
    NameExpression,
    eol_SpecialNameExpression,
    Annotation,
    eol_SimpleAnnotation,
    eol_ExecutableAnnotation,
    OrderedCollectionType,
    eol_SequenceType,
    CollectionType,
    eol_UniqueCollectionType,
    eol_OrderedCollectionType,
    eol_BagType,
    UniqueCollectionType,
    eol_OrderedSetType,
    eol_SetType,
    PrimitiveType,
    eol_StringType,
    eol_RealType,
    eol_IntegerType,
    eol_BooleanType,
    Type,
    eol_NativeType,
    eol_EType,
    eol_ModelElementType,
    eol_CollectionType,
    eol_PseudoType,
    eol_VoidType,
    eol_MapType,
    eol_ModelType,
    eol_PrimitiveType,
    eol_AnyType,
    CollectionExpression,
    eol_OrderedSetExpression,
    eol_BagExpression,
    eol_SequenceExpression,
    eol_SetExpression,
    LiteralExpression,
    eol_CollectionExpression,
    eol_NativeExpression,
    eol_MapExpression,
    eol_PrimitiveExpression,
    SwitchCaseStatement,
    eol_EPackage,
    eol_SwitchCaseDefaultStatement,
    eol_SwitchCaseExpressionStatement,
    Statement,
    eol_ExpressionStatement,
    eol_DeleteStatement,
    eol_ThrowStatement,
    eol_ModelDeclarationStatement,
    eol_WhileStatement,
    eol_BreakAllStatement,
    eol_ReturnStatement,
    eol_ContinueStatement,
    eol_SwitchCaseStatement,
    eol_AbortStatement,
    eol_ForStatement,
    eol_IfStatement,
    eol_BreakStatement,
    eol_SwitchStatement,
    eol_TransactionStatement,
    eol_AssignmentStatement,
    eol_FormalParameterExpression,
    UnaryOperatorExpression,
    eol_NotOperatorExpression,
    eol_NegativeOperatorExpression,
    eol_EObject,
    FeatureCallExpression,
    eol_FOLMethodCallExpression,
    eol_PropertyCallExpression,
    eol_MethodCallExpression,
    Expression,
    eol_ModelDeclarationParameter,
    eol_CollectionInitValue,
    eol_KeyValue,
    eol_VariableDeclarationExpression,
    eol_NewExpression,
    eol_OperatorExpression,
    EolElement,
    eol_AnnotationBlock,
    eol_Statement,
    eol_Annotation,
    eol_Type,
    eol_OperationDefinition,
    eol_EolLibraryModule,
    eol_Expression,
    eol_ExpressionOrStatementBlock,
    eol_Import,
    eol_Block,
    EolLibraryModule,
    eol_EolProgram,
    eol_TextPosition,
    eol_TextRegion,
    eol_EolElement,
    eol_FeatureCallExpression,
    ComparisonOperatorExpression,
    eol_LessThanOrEqualToOperatorExpression,
    eol_GreaterThanOrEqualToOperatorExpression,
    eol_LessThanOperatorExpression,
    eol_NotEqualsOperatorExpression,
    eol_GreaterThanOperatorExpression,
    eol_EqualsOperatorExpression,
    eol_ModelExpression,
    eol_NameExpression,
    eol_EnumerationLiteralExpression,
    ArithmeticOperatorExpression,
    eol_MultiplyOperatorExpression,
    eol_MinusOperatorExpression,
    eol_PlusOperatorExpression,
    eol_DivideOperatorExpression,
    PrimitiveExpression,
    eol_RealExpression,
    eol_IntegerExpression,
    eol_StringExpression,
    eol_BooleanExpression,
    eol_LiteralExpression,
    LogicalOperatorExpression,
    eol_OrOperatorExpression,
    eol_XorOperatorExpression,
    eol_ImpliesOperatorExpression,
    eol_AndOperatorExpression,
    OperatorExpression,
    eol_BinaryOperatorExpression,
    eol_UnaryOperatorExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ComparisonOperatorExpression)


def test_eol_comparisonoperatorexpression_constructor_exists():
    assert callable(eol_ComparisonOperatorExpression.__init__)


def test_eol_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ArithmeticOperatorExpression)


def test_eol_arithmeticoperatorexpression_constructor_exists():
    assert callable(eol_ArithmeticOperatorExpression.__init__)


def test_eol_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol_ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LogicalOperatorExpression)


def test_eol_logicaloperatorexpression_constructor_exists():
    assert callable(eol_LogicalOperatorExpression.__init__)


def test_eol_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol_LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pseudotype_is_not_abstract():
    assert not inspect.isabstract(PseudoType)


def test_pseudotype_constructor_exists():
    assert callable(PseudoType.__init__)


def test_pseudotype_constructor_args():
    sig = inspect.signature(PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol_operationargtype_is_not_abstract():
    assert not inspect.isabstract(eol_OperationArgType)


def test_eol_operationargtype_constructor_exists():
    assert callable(eol_OperationArgType.__init__)


def test_eol_operationargtype_constructor_args():
    sig = inspect.signature(eol_OperationArgType.__init__)
    params = list(sig.parameters.keys())



def test_eol_selfinnermosttype_is_not_abstract():
    assert not inspect.isabstract(eol_SelfInnermostType)


def test_eol_selfinnermosttype_constructor_exists():
    assert callable(eol_SelfInnermostType.__init__)


def test_eol_selfinnermosttype_constructor_args():
    sig = inspect.signature(eol_SelfInnermostType.__init__)
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



def test_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(CollectionInitValue)


def test_collectioninitvalue_constructor_exists():
    assert callable(CollectionInitValue.__init__)


def test_collectioninitvalue_constructor_args():
    sig = inspect.signature(CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_eol_exprange_is_not_abstract():
    assert not inspect.isabstract(eol_ExpRange)


def test_eol_exprange_constructor_exists():
    assert callable(eol_ExpRange.__init__)


def test_eol_exprange_constructor_args():
    sig = inspect.signature(eol_ExpRange.__init__)
    params = list(sig.parameters.keys())



def test_eol_exprlist_is_not_abstract():
    assert not inspect.isabstract(eol_ExprList)


def test_eol_exprlist_constructor_exists():
    assert callable(eol_ExprList.__init__)


def test_eol_exprlist_constructor_args():
    sig = inspect.signature(eol_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_eclassifier_is_not_abstract():
    assert not inspect.isabstract(eol_EClassifier)


def test_eol_eclassifier_constructor_exists():
    assert callable(eol_EClassifier.__init__)


def test_eol_eclassifier_constructor_args():
    sig = inspect.signature(eol_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_nameexpression_is_not_abstract():
    assert not inspect.isabstract(NameExpression)


def test_nameexpression_constructor_exists():
    assert callable(NameExpression.__init__)


def test_nameexpression_constructor_args():
    sig = inspect.signature(NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_specialnameexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SpecialNameExpression)


def test_eol_specialnameexpression_constructor_exists():
    assert callable(eol_SpecialNameExpression.__init__)


def test_eol_specialnameexpression_constructor_args():
    sig = inspect.signature(eol_SpecialNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_eol_simpleannotation_is_not_abstract():
    assert not inspect.isabstract(eol_SimpleAnnotation)


def test_eol_simpleannotation_constructor_exists():
    assert callable(eol_SimpleAnnotation.__init__)


def test_eol_simpleannotation_constructor_args():
    sig = inspect.signature(eol_SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_eol_executableannotation_is_not_abstract():
    assert not inspect.isabstract(eol_ExecutableAnnotation)


def test_eol_executableannotation_constructor_exists():
    assert callable(eol_ExecutableAnnotation.__init__)


def test_eol_executableannotation_constructor_args():
    sig = inspect.signature(eol_ExecutableAnnotation.__init__)
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



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_UniqueCollectionType)


def test_eol_uniquecollectiontype_constructor_exists():
    assert callable(eol_UniqueCollectionType.__init__)


def test_eol_uniquecollectiontype_constructor_args():
    sig = inspect.signature(eol_UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedCollectionType)


def test_eol_orderedcollectiontype_constructor_exists():
    assert callable(eol_OrderedCollectionType.__init__)


def test_eol_orderedcollectiontype_constructor_args():
    sig = inspect.signature(eol_OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol_bagtype_is_not_abstract():
    assert not inspect.isabstract(eol_BagType)


def test_eol_bagtype_constructor_exists():
    assert callable(eol_BagType.__init__)


def test_eol_bagtype_constructor_args():
    sig = inspect.signature(eol_BagType.__init__)
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



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
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



def test_eol_integertype_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerType)


def test_eol_integertype_constructor_exists():
    assert callable(eol_IntegerType.__init__)


def test_eol_integertype_constructor_args():
    sig = inspect.signature(eol_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_eol_booleantype_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanType)


def test_eol_booleantype_constructor_exists():
    assert callable(eol_BooleanType.__init__)


def test_eol_booleantype_constructor_args():
    sig = inspect.signature(eol_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_eol_nativetype_is_not_abstract():
    assert not inspect.isabstract(eol_NativeType)


def test_eol_nativetype_constructor_exists():
    assert callable(eol_NativeType.__init__)


def test_eol_nativetype_constructor_args():
    sig = inspect.signature(eol_NativeType.__init__)
    params = list(sig.parameters.keys())



def test_eol_etype_is_not_abstract():
    assert not inspect.isabstract(eol_EType)


def test_eol_etype_constructor_exists():
    assert callable(eol_EType.__init__)


def test_eol_etype_constructor_args():
    sig = inspect.signature(eol_EType.__init__)
    params = list(sig.parameters.keys())



def test_eol_modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelElementType)


def test_eol_modelelementtype_constructor_exists():
    assert callable(eol_ModelElementType.__init__)


def test_eol_modelelementtype_constructor_args():
    sig = inspect.signature(eol_ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_eol_modelelementtype_has_elementName():
    assert hasattr(eol_ModelElementType, "elementName")
    descriptor = None
    for klass in eol_ModelElementType.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
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



def test_eol_voidtype_is_not_abstract():
    assert not inspect.isabstract(eol_VoidType)


def test_eol_voidtype_constructor_exists():
    assert callable(eol_VoidType.__init__)


def test_eol_voidtype_constructor_args():
    sig = inspect.signature(eol_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_eol_maptype_is_not_abstract():
    assert not inspect.isabstract(eol_MapType)


def test_eol_maptype_constructor_exists():
    assert callable(eol_MapType.__init__)


def test_eol_maptype_constructor_args():
    sig = inspect.signature(eol_MapType.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeltype_is_not_abstract():
    assert not inspect.isabstract(eol_ModelType)


def test_eol_modeltype_constructor_exists():
    assert callable(eol_ModelType.__init__)


def test_eol_modeltype_constructor_args():
    sig = inspect.signature(eol_ModelType.__init__)
    params = list(sig.parameters.keys())



def test_eol_primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveType)


def test_eol_primitivetype_constructor_exists():
    assert callable(eol_PrimitiveType.__init__)


def test_eol_primitivetype_constructor_args():
    sig = inspect.signature(eol_PrimitiveType.__init__)
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



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrderedSetExpression)


def test_eol_orderedsetexpression_constructor_exists():
    assert callable(eol_OrderedSetExpression.__init__)


def test_eol_orderedsetexpression_constructor_args():
    sig = inspect.signature(eol_OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BagExpression)


def test_eol_bagexpression_constructor_exists():
    assert callable(eol_BagExpression.__init__)


def test_eol_bagexpression_constructor_args():
    sig = inspect.signature(eol_BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SequenceExpression)


def test_eol_sequenceexpression_constructor_exists():
    assert callable(eol_SequenceExpression.__init__)


def test_eol_sequenceexpression_constructor_args():
    sig = inspect.signature(eol_SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_setexpression_is_not_abstract():
    assert not inspect.isabstract(eol_SetExpression)


def test_eol_setexpression_constructor_exists():
    assert callable(eol_SetExpression.__init__)


def test_eol_setexpression_constructor_args():
    sig = inspect.signature(eol_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionExpression)


def test_eol_collectionexpression_constructor_exists():
    assert callable(eol_CollectionExpression.__init__)


def test_eol_collectionexpression_constructor_args():
    sig = inspect.signature(eol_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_nativeexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NativeExpression)


def test_eol_nativeexpression_constructor_exists():
    assert callable(eol_NativeExpression.__init__)


def test_eol_nativeexpression_constructor_args():
    sig = inspect.signature(eol_NativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MapExpression)


def test_eol_mapexpression_constructor_exists():
    assert callable(eol_MapExpression.__init__)


def test_eol_mapexpression_constructor_args():
    sig = inspect.signature(eol_MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PrimitiveExpression)


def test_eol_primitiveexpression_constructor_exists():
    assert callable(eol_PrimitiveExpression.__init__)


def test_eol_primitiveexpression_constructor_args():
    sig = inspect.signature(eol_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_epackage_is_not_abstract():
    assert not inspect.isabstract(eol_EPackage)


def test_eol_epackage_constructor_exists():
    assert callable(eol_EPackage.__init__)


def test_eol_epackage_constructor_args():
    sig = inspect.signature(eol_EPackage.__init__)
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



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionStatement)


def test_eol_expressionstatement_constructor_exists():
    assert callable(eol_ExpressionStatement.__init__)


def test_eol_expressionstatement_constructor_args():
    sig = inspect.signature(eol_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol_DeleteStatement)


def test_eol_deletestatement_constructor_exists():
    assert callable(eol_DeleteStatement.__init__)


def test_eol_deletestatement_constructor_args():
    sig = inspect.signature(eol_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_throwstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ThrowStatement)


def test_eol_throwstatement_constructor_exists():
    assert callable(eol_ThrowStatement.__init__)


def test_eol_throwstatement_constructor_args():
    sig = inspect.signature(eol_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationStatement)


def test_eol_modeldeclarationstatement_constructor_exists():
    assert callable(eol_ModelDeclarationStatement.__init__)


def test_eol_modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationStatement.__init__)
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



def test_eol_returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ReturnStatement)


def test_eol_returnstatement_constructor_exists():
    assert callable(eol_ReturnStatement.__init__)


def test_eol_returnstatement_constructor_args():
    sig = inspect.signature(eol_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol_ContinueStatement)


def test_eol_continuestatement_constructor_exists():
    assert callable(eol_ContinueStatement.__init__)


def test_eol_continuestatement_constructor_args():
    sig = inspect.signature(eol_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchCaseStatement)


def test_eol_switchcasestatement_constructor_exists():
    assert callable(eol_SwitchCaseStatement.__init__)


def test_eol_switchcasestatement_constructor_args():
    sig = inspect.signature(eol_SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_abortstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AbortStatement)


def test_eol_abortstatement_constructor_exists():
    assert callable(eol_AbortStatement.__init__)


def test_eol_abortstatement_constructor_args():
    sig = inspect.signature(eol_AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_forstatement_is_not_abstract():
    assert not inspect.isabstract(eol_ForStatement)


def test_eol_forstatement_constructor_exists():
    assert callable(eol_ForStatement.__init__)


def test_eol_forstatement_constructor_args():
    sig = inspect.signature(eol_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol_IfStatement)


def test_eol_ifstatement_constructor_exists():
    assert callable(eol_IfStatement.__init__)


def test_eol_ifstatement_constructor_args():
    sig = inspect.signature(eol_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol_BreakStatement)


def test_eol_breakstatement_constructor_exists():
    assert callable(eol_BreakStatement.__init__)


def test_eol_breakstatement_constructor_args():
    sig = inspect.signature(eol_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol_SwitchStatement)


def test_eol_switchstatement_constructor_exists():
    assert callable(eol_SwitchStatement.__init__)


def test_eol_switchstatement_constructor_args():
    sig = inspect.signature(eol_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_transactionstatement_is_not_abstract():
    assert not inspect.isabstract(eol_TransactionStatement)


def test_eol_transactionstatement_constructor_exists():
    assert callable(eol_TransactionStatement.__init__)


def test_eol_transactionstatement_constructor_args():
    sig = inspect.signature(eol_TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol_AssignmentStatement)


def test_eol_assignmentstatement_constructor_exists():
    assert callable(eol_AssignmentStatement.__init__)


def test_eol_assignmentstatement_constructor_args():
    sig = inspect.signature(eol_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol_formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FormalParameterExpression)


def test_eol_formalparameterexpression_constructor_exists():
    assert callable(eol_FormalParameterExpression.__init__)


def test_eol_formalparameterexpression_constructor_args():
    sig = inspect.signature(eol_FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NotOperatorExpression)


def test_eol_notoperatorexpression_constructor_exists():
    assert callable(eol_NotOperatorExpression.__init__)


def test_eol_notoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NegativeOperatorExpression)


def test_eol_negativeoperatorexpression_constructor_exists():
    assert callable(eol_NegativeOperatorExpression.__init__)


def test_eol_negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol_NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_eobject_is_not_abstract():
    assert not inspect.isabstract(eol_EObject)


def test_eol_eobject_constructor_exists():
    assert callable(eol_EObject.__init__)


def test_eol_eobject_constructor_args():
    sig = inspect.signature(eol_EObject.__init__)
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



def test_eol_propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_PropertyCallExpression)


def test_eol_propertycallexpression_constructor_exists():
    assert callable(eol_PropertyCallExpression.__init__)


def test_eol_propertycallexpression_constructor_args():
    sig = inspect.signature(eol_PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MethodCallExpression)


def test_eol_methodcallexpression_constructor_exists():
    assert callable(eol_MethodCallExpression.__init__)


def test_eol_methodcallexpression_constructor_args():
    sig = inspect.signature(eol_MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol_modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol_ModelDeclarationParameter)


def test_eol_modeldeclarationparameter_constructor_exists():
    assert callable(eol_ModelDeclarationParameter.__init__)


def test_eol_modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol_ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_eol_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(eol_CollectionInitValue)


def test_eol_collectioninitvalue_constructor_exists():
    assert callable(eol_CollectionInitValue.__init__)


def test_eol_collectioninitvalue_constructor_args():
    sig = inspect.signature(eol_CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_eol_keyvalue_is_not_abstract():
    assert not inspect.isabstract(eol_KeyValue)


def test_eol_keyvalue_constructor_exists():
    assert callable(eol_KeyValue.__init__)


def test_eol_keyvalue_constructor_args():
    sig = inspect.signature(eol_KeyValue.__init__)
    params = list(sig.parameters.keys())



def test_eol_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol_VariableDeclarationExpression)


def test_eol_variabledeclarationexpression_constructor_exists():
    assert callable(eol_VariableDeclarationExpression.__init__)


def test_eol_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "definitionPoints" in params, "Missing parameter 'definitionPoints'"

def test_eol_variabledeclarationexpression_has_definitionPoints():
    assert hasattr(eol_VariableDeclarationExpression, "definitionPoints")
    descriptor = None
    for klass in eol_VariableDeclarationExpression.__mro__:
        if "definitionPoints" in klass.__dict__:
            descriptor = klass.__dict__["definitionPoints"]
            break
    assert isinstance(descriptor, property)



def test_eol_newexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NewExpression)


def test_eol_newexpression_constructor_exists():
    assert callable(eol_NewExpression.__init__)


def test_eol_newexpression_constructor_args():
    sig = inspect.signature(eol_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OperatorExpression)


def test_eol_operatorexpression_constructor_exists():
    assert callable(eol_OperatorExpression.__init__)


def test_eol_operatorexpression_constructor_args():
    sig = inspect.signature(eol_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eolelement_is_not_abstract():
    assert not inspect.isabstract(EolElement)


def test_eolelement_constructor_exists():
    assert callable(EolElement.__init__)


def test_eolelement_constructor_args():
    sig = inspect.signature(EolElement.__init__)
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



def test_eol_annotation_is_not_abstract():
    assert not inspect.isabstract(eol_Annotation)


def test_eol_annotation_constructor_exists():
    assert callable(eol_Annotation.__init__)


def test_eol_annotation_constructor_args():
    sig = inspect.signature(eol_Annotation.__init__)
    params = list(sig.parameters.keys())



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



def test_eol_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol_EolLibraryModule)


def test_eol_eollibrarymodule_constructor_exists():
    assert callable(eol_EolLibraryModule.__init__)


def test_eol_eollibrarymodule_constructor_args():
    sig = inspect.signature(eol_EolLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol_expression_is_not_abstract():
    assert not inspect.isabstract(eol_Expression)


def test_eol_expression_constructor_exists():
    assert callable(eol_Expression.__init__)


def test_eol_expression_constructor_args():
    sig = inspect.signature(eol_Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol_expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol_ExpressionOrStatementBlock)


def test_eol_expressionorstatementblock_constructor_exists():
    assert callable(eol_ExpressionOrStatementBlock.__init__)


def test_eol_expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol_ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol_import_is_not_abstract():
    assert not inspect.isabstract(eol_Import)


def test_eol_import_constructor_exists():
    assert callable(eol_Import.__init__)


def test_eol_import_constructor_args():
    sig = inspect.signature(eol_Import.__init__)
    params = list(sig.parameters.keys())



def test_eol_block_is_not_abstract():
    assert not inspect.isabstract(eol_Block)


def test_eol_block_constructor_exists():
    assert callable(eol_Block.__init__)


def test_eol_block_constructor_args():
    sig = inspect.signature(eol_Block.__init__)
    params = list(sig.parameters.keys())



def test_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EolLibraryModule)


def test_eollibrarymodule_constructor_exists():
    assert callable(EolLibraryModule.__init__)


def test_eollibrarymodule_constructor_args():
    sig = inspect.signature(EolLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol_eolprogram_is_not_abstract():
    assert not inspect.isabstract(eol_EolProgram)


def test_eol_eolprogram_constructor_exists():
    assert callable(eol_EolProgram.__init__)


def test_eol_eolprogram_constructor_args():
    sig = inspect.signature(eol_EolProgram.__init__)
    params = list(sig.parameters.keys())



def test_eol_textposition_is_not_abstract():
    assert not inspect.isabstract(eol_TextPosition)


def test_eol_textposition_constructor_exists():
    assert callable(eol_TextPosition.__init__)


def test_eol_textposition_constructor_args():
    sig = inspect.signature(eol_TextPosition.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_eol_textposition_has_column():
    assert hasattr(eol_TextPosition, "column")
    descriptor = None
    for klass in eol_TextPosition.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_eol_textposition_has_line():
    assert hasattr(eol_TextPosition, "line")
    descriptor = None
    for klass in eol_TextPosition.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_eol_textregion_is_not_abstract():
    assert not inspect.isabstract(eol_TextRegion)


def test_eol_textregion_constructor_exists():
    assert callable(eol_TextRegion.__init__)


def test_eol_textregion_constructor_args():
    sig = inspect.signature(eol_TextRegion.__init__)
    params = list(sig.parameters.keys())



def test_eol_eolelement_is_not_abstract():
    assert not inspect.isabstract(eol_EolElement)


def test_eol_eolelement_constructor_exists():
    assert callable(eol_EolElement.__init__)


def test_eol_eolelement_constructor_args():
    sig = inspect.signature(eol_EolElement.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "uri" in params, "Missing parameter 'uri'"
    assert "line" in params, "Missing parameter 'line'"

def test_eol_eolelement_has_column():
    assert hasattr(eol_EolElement, "column")
    descriptor = None
    for klass in eol_EolElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_eol_eolelement_has_uri():
    assert hasattr(eol_EolElement, "uri")
    descriptor = None
    for klass in eol_EolElement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_eol_eolelement_has_line():
    assert hasattr(eol_EolElement, "line")
    descriptor = None
    for klass in eol_EolElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_eol_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol_FeatureCallExpression)


def test_eol_featurecallexpression_constructor_exists():
    assert callable(eol_FeatureCallExpression.__init__)


def test_eol_featurecallexpression_constructor_args():
    sig = inspect.signature(eol_FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LessThanOrEqualToOperatorExpression)


def test_eol_lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_LessThanOrEqualToOperatorExpression.__init__)


def test_eol_lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOrEqualToOperatorExpression)


def test_eol_greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol_greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOrEqualToOperatorExpression.__init__)
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



def test_eol_greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_GreaterThanOperatorExpression)


def test_eol_greaterthanoperatorexpression_constructor_exists():
    assert callable(eol_GreaterThanOperatorExpression.__init__)


def test_eol_greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol_GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EqualsOperatorExpression)


def test_eol_equalsoperatorexpression_constructor_exists():
    assert callable(eol_EqualsOperatorExpression.__init__)


def test_eol_equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol_EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_modelexpression_is_not_abstract():
    assert not inspect.isabstract(eol_ModelExpression)


def test_eol_modelexpression_constructor_exists():
    assert callable(eol_ModelExpression.__init__)


def test_eol_modelexpression_constructor_args():
    sig = inspect.signature(eol_ModelExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol_NameExpression)


def test_eol_nameexpression_constructor_exists():
    assert callable(eol_NameExpression.__init__)


def test_eol_nameexpression_constructor_args():
    sig = inspect.signature(eol_NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedContent" in params, "Missing parameter 'resolvedContent'"
    assert "name" in params, "Missing parameter 'name'"

def test_eol_nameexpression_has_resolvedContent():
    assert hasattr(eol_NameExpression, "resolvedContent")
    descriptor = None
    for klass in eol_NameExpression.__mro__:
        if "resolvedContent" in klass.__dict__:
            descriptor = klass.__dict__["resolvedContent"]
            break
    assert isinstance(descriptor, property)

def test_eol_nameexpression_has_name():
    assert hasattr(eol_NameExpression, "name")
    descriptor = None
    for klass in eol_NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eol_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol_EnumerationLiteralExpression)


def test_eol_enumerationliteralexpression_constructor_exists():
    assert callable(eol_EnumerationLiteralExpression.__init__)


def test_eol_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_MultiplyOperatorExpression)


def test_eol_multiplyoperatorexpression_constructor_exists():
    assert callable(eol_MultiplyOperatorExpression.__init__)


def test_eol_multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol_MultiplyOperatorExpression.__init__)
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



def test_eol_divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_DivideOperatorExpression)


def test_eol_divideoperatorexpression_constructor_exists():
    assert callable(eol_DivideOperatorExpression.__init__)


def test_eol_divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol_DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_realexpression_is_not_abstract():
    assert not inspect.isabstract(eol_RealExpression)


def test_eol_realexpression_constructor_exists():
    assert callable(eol_RealExpression.__init__)


def test_eol_realexpression_constructor_args():
    sig = inspect.signature(eol_RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol_realexpression_has_val():
    assert hasattr(eol_RealExpression, "val")
    descriptor = None
    for klass in eol_RealExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol_integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol_IntegerExpression)


def test_eol_integerexpression_constructor_exists():
    assert callable(eol_IntegerExpression.__init__)


def test_eol_integerexpression_constructor_args():
    sig = inspect.signature(eol_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol_integerexpression_has_val():
    assert hasattr(eol_IntegerExpression, "val")
    descriptor = None
    for klass in eol_IntegerExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol_stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol_StringExpression)


def test_eol_stringexpression_constructor_exists():
    assert callable(eol_StringExpression.__init__)


def test_eol_stringexpression_constructor_args():
    sig = inspect.signature(eol_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol_stringexpression_has_val():
    assert hasattr(eol_StringExpression, "val")
    descriptor = None
    for klass in eol_StringExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol_BooleanExpression)


def test_eol_booleanexpression_constructor_exists():
    assert callable(eol_BooleanExpression.__init__)


def test_eol_booleanexpression_constructor_args():
    sig = inspect.signature(eol_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol_booleanexpression_has_val():
    assert hasattr(eol_BooleanExpression, "val")
    descriptor = None
    for klass in eol_BooleanExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol_literalexpression_is_not_abstract():
    assert not inspect.isabstract(eol_LiteralExpression)


def test_eol_literalexpression_constructor_exists():
    assert callable(eol_LiteralExpression.__init__)


def test_eol_literalexpression_constructor_args():
    sig = inspect.signature(eol_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol_oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_OrOperatorExpression)


def test_eol_oroperatorexpression_constructor_exists():
    assert callable(eol_OrOperatorExpression.__init__)


def test_eol_oroperatorexpression_constructor_args():
    sig = inspect.signature(eol_OrOperatorExpression.__init__)
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



def test_eol_andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol_AndOperatorExpression)


def test_eol_andoperatorexpression_constructor_exists():
    assert callable(eol_AndOperatorExpression.__init__)


def test_eol_andoperatorexpression_constructor_args():
    sig = inspect.signature(eol_AndOperatorExpression.__init__)
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
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol_ComparisonOperatorExpression_strategy = st.builds(
    eol_ComparisonOperatorExpression,
)
eol_ArithmeticOperatorExpression_strategy = st.builds(
    eol_ArithmeticOperatorExpression,
)
eol_LogicalOperatorExpression_strategy = st.builds(
    eol_LogicalOperatorExpression,
)
PseudoType_strategy = st.builds(
    PseudoType,
)
eol_OperationArgType_strategy = st.builds(
    eol_OperationArgType,
)
eol_SelfInnermostType_strategy = st.builds(
    eol_SelfInnermostType,
)
eol_SelfContentType_strategy = st.builds(
    eol_SelfContentType,
)
eol_SelfType_strategy = st.builds(
    eol_SelfType,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol_SpecialAssignmentStatement_strategy = st.builds(
    eol_SpecialAssignmentStatement,
)
CollectionInitValue_strategy = st.builds(
    CollectionInitValue,
)
eol_ExpRange_strategy = st.builds(
    eol_ExpRange,
)
eol_ExprList_strategy = st.builds(
    eol_ExprList,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
eol_EClassifier_strategy = st.builds(
    eol_EClassifier,
)
NameExpression_strategy = st.builds(
    NameExpression,
)
eol_SpecialNameExpression_strategy = st.builds(
    eol_SpecialNameExpression,
)
Annotation_strategy = st.builds(
    Annotation,
)
eol_SimpleAnnotation_strategy = st.builds(
    eol_SimpleAnnotation,
)
eol_ExecutableAnnotation_strategy = st.builds(
    eol_ExecutableAnnotation,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol_SequenceType_strategy = st.builds(
    eol_SequenceType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
eol_UniqueCollectionType_strategy = st.builds(
    eol_UniqueCollectionType,
)
eol_OrderedCollectionType_strategy = st.builds(
    eol_OrderedCollectionType,
)
eol_BagType_strategy = st.builds(
    eol_BagType,
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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol_StringType_strategy = st.builds(
    eol_StringType,
)
eol_RealType_strategy = st.builds(
    eol_RealType,
)
eol_IntegerType_strategy = st.builds(
    eol_IntegerType,
)
eol_BooleanType_strategy = st.builds(
    eol_BooleanType,
)
Type_strategy = st.builds(
    Type,
)
eol_NativeType_strategy = st.builds(
    eol_NativeType,
)
eol_EType_strategy = st.builds(
    eol_EType,
)
eol_ModelElementType_strategy = st.builds(
    eol_ModelElementType,
    elementName=
        safe_text,
    modelName=
        safe_text
)
eol_CollectionType_strategy = st.builds(
    eol_CollectionType,
)
eol_PseudoType_strategy = st.builds(
    eol_PseudoType,
)
eol_VoidType_strategy = st.builds(
    eol_VoidType,
)
eol_MapType_strategy = st.builds(
    eol_MapType,
)
eol_ModelType_strategy = st.builds(
    eol_ModelType,
)
eol_PrimitiveType_strategy = st.builds(
    eol_PrimitiveType,
)
eol_AnyType_strategy = st.builds(
    eol_AnyType,
    declared=
        st.booleans()
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol_OrderedSetExpression_strategy = st.builds(
    eol_OrderedSetExpression,
)
eol_BagExpression_strategy = st.builds(
    eol_BagExpression,
)
eol_SequenceExpression_strategy = st.builds(
    eol_SequenceExpression,
)
eol_SetExpression_strategy = st.builds(
    eol_SetExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
eol_CollectionExpression_strategy = st.builds(
    eol_CollectionExpression,
)
eol_NativeExpression_strategy = st.builds(
    eol_NativeExpression,
)
eol_MapExpression_strategy = st.builds(
    eol_MapExpression,
)
eol_PrimitiveExpression_strategy = st.builds(
    eol_PrimitiveExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
eol_EPackage_strategy = st.builds(
    eol_EPackage,
)
eol_SwitchCaseDefaultStatement_strategy = st.builds(
    eol_SwitchCaseDefaultStatement,
)
eol_SwitchCaseExpressionStatement_strategy = st.builds(
    eol_SwitchCaseExpressionStatement,
)
Statement_strategy = st.builds(
    Statement,
)
eol_ExpressionStatement_strategy = st.builds(
    eol_ExpressionStatement,
)
eol_DeleteStatement_strategy = st.builds(
    eol_DeleteStatement,
)
eol_ThrowStatement_strategy = st.builds(
    eol_ThrowStatement,
)
eol_ModelDeclarationStatement_strategy = st.builds(
    eol_ModelDeclarationStatement,
)
eol_WhileStatement_strategy = st.builds(
    eol_WhileStatement,
)
eol_BreakAllStatement_strategy = st.builds(
    eol_BreakAllStatement,
)
eol_ReturnStatement_strategy = st.builds(
    eol_ReturnStatement,
)
eol_ContinueStatement_strategy = st.builds(
    eol_ContinueStatement,
)
eol_SwitchCaseStatement_strategy = st.builds(
    eol_SwitchCaseStatement,
)
eol_AbortStatement_strategy = st.builds(
    eol_AbortStatement,
)
eol_ForStatement_strategy = st.builds(
    eol_ForStatement,
)
eol_IfStatement_strategy = st.builds(
    eol_IfStatement,
)
eol_BreakStatement_strategy = st.builds(
    eol_BreakStatement,
)
eol_SwitchStatement_strategy = st.builds(
    eol_SwitchStatement,
)
eol_TransactionStatement_strategy = st.builds(
    eol_TransactionStatement,
)
eol_AssignmentStatement_strategy = st.builds(
    eol_AssignmentStatement,
)
eol_FormalParameterExpression_strategy = st.builds(
    eol_FormalParameterExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol_NotOperatorExpression_strategy = st.builds(
    eol_NotOperatorExpression,
)
eol_NegativeOperatorExpression_strategy = st.builds(
    eol_NegativeOperatorExpression,
)
eol_EObject_strategy = st.builds(
    eol_EObject,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol_FOLMethodCallExpression_strategy = st.builds(
    eol_FOLMethodCallExpression,
)
eol_PropertyCallExpression_strategy = st.builds(
    eol_PropertyCallExpression,
)
eol_MethodCallExpression_strategy = st.builds(
    eol_MethodCallExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol_ModelDeclarationParameter_strategy = st.builds(
    eol_ModelDeclarationParameter,
)
eol_CollectionInitValue_strategy = st.builds(
    eol_CollectionInitValue,
)
eol_KeyValue_strategy = st.builds(
    eol_KeyValue,
)
eol_VariableDeclarationExpression_strategy = st.builds(
    eol_VariableDeclarationExpression,
    definitionPoints=
        safe_text
)
eol_NewExpression_strategy = st.builds(
    eol_NewExpression,
)
eol_OperatorExpression_strategy = st.builds(
    eol_OperatorExpression,
)
EolElement_strategy = st.builds(
    EolElement,
)
eol_AnnotationBlock_strategy = st.builds(
    eol_AnnotationBlock,
)
eol_Statement_strategy = st.builds(
    eol_Statement,
)
eol_Annotation_strategy = st.builds(
    eol_Annotation,
)
eol_Type_strategy = st.builds(
    eol_Type,
)
eol_OperationDefinition_strategy = st.builds(
    eol_OperationDefinition,
)
eol_EolLibraryModule_strategy = st.builds(
    eol_EolLibraryModule,
)
eol_Expression_strategy = st.builds(
    eol_Expression,
)
eol_ExpressionOrStatementBlock_strategy = st.builds(
    eol_ExpressionOrStatementBlock,
)
eol_Import_strategy = st.builds(
    eol_Import,
)
eol_Block_strategy = st.builds(
    eol_Block,
)
EolLibraryModule_strategy = st.builds(
    EolLibraryModule,
)
eol_EolProgram_strategy = st.builds(
    eol_EolProgram,
)
eol_TextPosition_strategy = st.builds(
    eol_TextPosition,
    column=
        st.integers(),
    line=
        st.integers()
)
eol_TextRegion_strategy = st.builds(
    eol_TextRegion,
)
eol_EolElement_strategy = st.builds(
    eol_EolElement,
    column=
        st.integers(),
    uri=
        safe_text,
    line=
        st.integers()
)
eol_FeatureCallExpression_strategy = st.builds(
    eol_FeatureCallExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol_LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_LessThanOrEqualToOperatorExpression,
)
eol_GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol_GreaterThanOrEqualToOperatorExpression,
)
eol_LessThanOperatorExpression_strategy = st.builds(
    eol_LessThanOperatorExpression,
)
eol_NotEqualsOperatorExpression_strategy = st.builds(
    eol_NotEqualsOperatorExpression,
)
eol_GreaterThanOperatorExpression_strategy = st.builds(
    eol_GreaterThanOperatorExpression,
)
eol_EqualsOperatorExpression_strategy = st.builds(
    eol_EqualsOperatorExpression,
)
eol_ModelExpression_strategy = st.builds(
    eol_ModelExpression,
)
eol_NameExpression_strategy = st.builds(
    eol_NameExpression,
    resolvedContent=
        safe_text,
    name=
        safe_text
)
eol_EnumerationLiteralExpression_strategy = st.builds(
    eol_EnumerationLiteralExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol_MultiplyOperatorExpression_strategy = st.builds(
    eol_MultiplyOperatorExpression,
)
eol_MinusOperatorExpression_strategy = st.builds(
    eol_MinusOperatorExpression,
)
eol_PlusOperatorExpression_strategy = st.builds(
    eol_PlusOperatorExpression,
)
eol_DivideOperatorExpression_strategy = st.builds(
    eol_DivideOperatorExpression,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol_RealExpression_strategy = st.builds(
    eol_RealExpression,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol_IntegerExpression_strategy = st.builds(
    eol_IntegerExpression,
    val=
        st.integers()
)
eol_StringExpression_strategy = st.builds(
    eol_StringExpression,
    val=
        safe_text
)
eol_BooleanExpression_strategy = st.builds(
    eol_BooleanExpression,
    val=
        st.booleans()
)
eol_LiteralExpression_strategy = st.builds(
    eol_LiteralExpression,
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol_OrOperatorExpression_strategy = st.builds(
    eol_OrOperatorExpression,
)
eol_XorOperatorExpression_strategy = st.builds(
    eol_XorOperatorExpression,
)
eol_ImpliesOperatorExpression_strategy = st.builds(
    eol_ImpliesOperatorExpression,
)
eol_AndOperatorExpression_strategy = st.builds(
    eol_AndOperatorExpression,
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

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol_ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ComparisonOperatorExpression)

@given(instance=eol_ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ArithmeticOperatorExpression)

@given(instance=eol_LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LogicalOperatorExpression)

@given(instance=PseudoType_strategy)
@settings(max_examples=50)
def test_pseudotype_instantiation(instance):
    assert isinstance(instance, PseudoType)

@given(instance=eol_OperationArgType_strategy)
@settings(max_examples=50)
def test_eol_operationargtype_instantiation(instance):
    assert isinstance(instance, eol_OperationArgType)

@given(instance=eol_SelfInnermostType_strategy)
@settings(max_examples=50)
def test_eol_selfinnermosttype_instantiation(instance):
    assert isinstance(instance, eol_SelfInnermostType)

@given(instance=eol_SelfContentType_strategy)
@settings(max_examples=50)
def test_eol_selfcontenttype_instantiation(instance):
    assert isinstance(instance, eol_SelfContentType)

@given(instance=eol_SelfType_strategy)
@settings(max_examples=50)
def test_eol_selftype_instantiation(instance):
    assert isinstance(instance, eol_SelfType)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=eol_SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol_specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, eol_SpecialAssignmentStatement)

@given(instance=CollectionInitValue_strategy)
@settings(max_examples=50)
def test_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, CollectionInitValue)

@given(instance=eol_ExpRange_strategy)
@settings(max_examples=50)
def test_eol_exprange_instantiation(instance):
    assert isinstance(instance, eol_ExpRange)

@given(instance=eol_ExprList_strategy)
@settings(max_examples=50)
def test_eol_exprlist_instantiation(instance):
    assert isinstance(instance, eol_ExprList)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=eol_EClassifier_strategy)
@settings(max_examples=50)
def test_eol_eclassifier_instantiation(instance):
    assert isinstance(instance, eol_EClassifier)

@given(instance=NameExpression_strategy)
@settings(max_examples=50)
def test_nameexpression_instantiation(instance):
    assert isinstance(instance, NameExpression)

@given(instance=eol_SpecialNameExpression_strategy)
@settings(max_examples=50)
def test_eol_specialnameexpression_instantiation(instance):
    assert isinstance(instance, eol_SpecialNameExpression)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=eol_SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_eol_simpleannotation_instantiation(instance):
    assert isinstance(instance, eol_SimpleAnnotation)

@given(instance=eol_ExecutableAnnotation_strategy)
@settings(max_examples=50)
def test_eol_executableannotation_instantiation(instance):
    assert isinstance(instance, eol_ExecutableAnnotation)

@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)

@given(instance=eol_SequenceType_strategy)
@settings(max_examples=50)
def test_eol_sequencetype_instantiation(instance):
    assert isinstance(instance, eol_SequenceType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=eol_UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_eol_uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, eol_UniqueCollectionType)

@given(instance=eol_OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_eol_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, eol_OrderedCollectionType)

@given(instance=eol_BagType_strategy)
@settings(max_examples=50)
def test_eol_bagtype_instantiation(instance):
    assert isinstance(instance, eol_BagType)

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

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=eol_StringType_strategy)
@settings(max_examples=50)
def test_eol_stringtype_instantiation(instance):
    assert isinstance(instance, eol_StringType)

@given(instance=eol_RealType_strategy)
@settings(max_examples=50)
def test_eol_realtype_instantiation(instance):
    assert isinstance(instance, eol_RealType)

@given(instance=eol_IntegerType_strategy)
@settings(max_examples=50)
def test_eol_integertype_instantiation(instance):
    assert isinstance(instance, eol_IntegerType)

@given(instance=eol_BooleanType_strategy)
@settings(max_examples=50)
def test_eol_booleantype_instantiation(instance):
    assert isinstance(instance, eol_BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eol_NativeType_strategy)
@settings(max_examples=50)
def test_eol_nativetype_instantiation(instance):
    assert isinstance(instance, eol_NativeType)

@given(instance=eol_EType_strategy)
@settings(max_examples=50)
def test_eol_etype_instantiation(instance):
    assert isinstance(instance, eol_EType)

@given(instance=eol_ModelElementType_strategy)
@settings(max_examples=50)
def test_eol_modelelementtype_instantiation(instance):
    assert isinstance(instance, eol_ModelElementType)



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original



@given(instance=eol_ModelElementType_strategy)
def test_eol_modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=eol_CollectionType_strategy)
@settings(max_examples=50)
def test_eol_collectiontype_instantiation(instance):
    assert isinstance(instance, eol_CollectionType)

@given(instance=eol_PseudoType_strategy)
@settings(max_examples=50)
def test_eol_pseudotype_instantiation(instance):
    assert isinstance(instance, eol_PseudoType)

@given(instance=eol_VoidType_strategy)
@settings(max_examples=50)
def test_eol_voidtype_instantiation(instance):
    assert isinstance(instance, eol_VoidType)

@given(instance=eol_MapType_strategy)
@settings(max_examples=50)
def test_eol_maptype_instantiation(instance):
    assert isinstance(instance, eol_MapType)

@given(instance=eol_ModelType_strategy)
@settings(max_examples=50)
def test_eol_modeltype_instantiation(instance):
    assert isinstance(instance, eol_ModelType)

@given(instance=eol_PrimitiveType_strategy)
@settings(max_examples=50)
def test_eol_primitivetype_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveType)

@given(instance=eol_AnyType_strategy)
@settings(max_examples=50)
def test_eol_anytype_instantiation(instance):
    assert isinstance(instance, eol_AnyType)



@given(instance=eol_AnyType_strategy)
def test_eol_anytype_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol_OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol_orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol_OrderedSetExpression)

@given(instance=eol_BagExpression_strategy)
@settings(max_examples=50)
def test_eol_bagexpression_instantiation(instance):
    assert isinstance(instance, eol_BagExpression)

@given(instance=eol_SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol_sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol_SequenceExpression)

@given(instance=eol_SetExpression_strategy)
@settings(max_examples=50)
def test_eol_setexpression_instantiation(instance):
    assert isinstance(instance, eol_SetExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=eol_CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol_collectionexpression_instantiation(instance):
    assert isinstance(instance, eol_CollectionExpression)

@given(instance=eol_NativeExpression_strategy)
@settings(max_examples=50)
def test_eol_nativeexpression_instantiation(instance):
    assert isinstance(instance, eol_NativeExpression)

@given(instance=eol_MapExpression_strategy)
@settings(max_examples=50)
def test_eol_mapexpression_instantiation(instance):
    assert isinstance(instance, eol_MapExpression)

@given(instance=eol_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol_primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol_PrimitiveExpression)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=eol_EPackage_strategy)
@settings(max_examples=50)
def test_eol_epackage_instantiation(instance):
    assert isinstance(instance, eol_EPackage)

@given(instance=eol_SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseDefaultStatement)

@given(instance=eol_SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseExpressionStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=eol_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol_expressionstatement_instantiation(instance):
    assert isinstance(instance, eol_ExpressionStatement)

@given(instance=eol_DeleteStatement_strategy)
@settings(max_examples=50)
def test_eol_deletestatement_instantiation(instance):
    assert isinstance(instance, eol_DeleteStatement)

@given(instance=eol_ThrowStatement_strategy)
@settings(max_examples=50)
def test_eol_throwstatement_instantiation(instance):
    assert isinstance(instance, eol_ThrowStatement)

@given(instance=eol_ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol_modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationStatement)

@given(instance=eol_WhileStatement_strategy)
@settings(max_examples=50)
def test_eol_whilestatement_instantiation(instance):
    assert isinstance(instance, eol_WhileStatement)

@given(instance=eol_BreakAllStatement_strategy)
@settings(max_examples=50)
def test_eol_breakallstatement_instantiation(instance):
    assert isinstance(instance, eol_BreakAllStatement)

@given(instance=eol_ReturnStatement_strategy)
@settings(max_examples=50)
def test_eol_returnstatement_instantiation(instance):
    assert isinstance(instance, eol_ReturnStatement)

@given(instance=eol_ContinueStatement_strategy)
@settings(max_examples=50)
def test_eol_continuestatement_instantiation(instance):
    assert isinstance(instance, eol_ContinueStatement)

@given(instance=eol_SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_eol_switchcasestatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchCaseStatement)

@given(instance=eol_AbortStatement_strategy)
@settings(max_examples=50)
def test_eol_abortstatement_instantiation(instance):
    assert isinstance(instance, eol_AbortStatement)

@given(instance=eol_ForStatement_strategy)
@settings(max_examples=50)
def test_eol_forstatement_instantiation(instance):
    assert isinstance(instance, eol_ForStatement)

@given(instance=eol_IfStatement_strategy)
@settings(max_examples=50)
def test_eol_ifstatement_instantiation(instance):
    assert isinstance(instance, eol_IfStatement)

@given(instance=eol_BreakStatement_strategy)
@settings(max_examples=50)
def test_eol_breakstatement_instantiation(instance):
    assert isinstance(instance, eol_BreakStatement)

@given(instance=eol_SwitchStatement_strategy)
@settings(max_examples=50)
def test_eol_switchstatement_instantiation(instance):
    assert isinstance(instance, eol_SwitchStatement)

@given(instance=eol_TransactionStatement_strategy)
@settings(max_examples=50)
def test_eol_transactionstatement_instantiation(instance):
    assert isinstance(instance, eol_TransactionStatement)

@given(instance=eol_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol_assignmentstatement_instantiation(instance):
    assert isinstance(instance, eol_AssignmentStatement)

@given(instance=eol_FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol_formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol_FormalParameterExpression)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol_NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NotOperatorExpression)

@given(instance=eol_NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NegativeOperatorExpression)

@given(instance=eol_EObject_strategy)
@settings(max_examples=50)
def test_eol_eobject_instantiation(instance):
    assert isinstance(instance, eol_EObject)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol_FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_FOLMethodCallExpression)

@given(instance=eol_PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol_propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol_PropertyCallExpression)

@given(instance=eol_MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol_methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol_MethodCallExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol_ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_eol_modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, eol_ModelDeclarationParameter)

@given(instance=eol_CollectionInitValue_strategy)
@settings(max_examples=50)
def test_eol_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, eol_CollectionInitValue)

@given(instance=eol_KeyValue_strategy)
@settings(max_examples=50)
def test_eol_keyvalue_instantiation(instance):
    assert isinstance(instance, eol_KeyValue)

@given(instance=eol_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol_VariableDeclarationExpression)



@given(instance=eol_VariableDeclarationExpression_strategy)
def test_eol_variabledeclarationexpression_definitionPoints_setter(instance):
    original = instance.definitionPoints
    instance.definitionPoints = original
    assert instance.definitionPoints == original

@given(instance=eol_NewExpression_strategy)
@settings(max_examples=50)
def test_eol_newexpression_instantiation(instance):
    assert isinstance(instance, eol_NewExpression)

@given(instance=eol_OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_operatorexpression_instantiation(instance):
    assert isinstance(instance, eol_OperatorExpression)

@given(instance=EolElement_strategy)
@settings(max_examples=50)
def test_eolelement_instantiation(instance):
    assert isinstance(instance, EolElement)

@given(instance=eol_AnnotationBlock_strategy)
@settings(max_examples=50)
def test_eol_annotationblock_instantiation(instance):
    assert isinstance(instance, eol_AnnotationBlock)

@given(instance=eol_Statement_strategy)
@settings(max_examples=50)
def test_eol_statement_instantiation(instance):
    assert isinstance(instance, eol_Statement)

@given(instance=eol_Annotation_strategy)
@settings(max_examples=50)
def test_eol_annotation_instantiation(instance):
    assert isinstance(instance, eol_Annotation)

@given(instance=eol_Type_strategy)
@settings(max_examples=50)
def test_eol_type_instantiation(instance):
    assert isinstance(instance, eol_Type)

@given(instance=eol_OperationDefinition_strategy)
@settings(max_examples=50)
def test_eol_operationdefinition_instantiation(instance):
    assert isinstance(instance, eol_OperationDefinition)

@given(instance=eol_EolLibraryModule_strategy)
@settings(max_examples=50)
def test_eol_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, eol_EolLibraryModule)

@given(instance=eol_Expression_strategy)
@settings(max_examples=50)
def test_eol_expression_instantiation(instance):
    assert isinstance(instance, eol_Expression)

@given(instance=eol_ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol_expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol_ExpressionOrStatementBlock)

@given(instance=eol_Import_strategy)
@settings(max_examples=50)
def test_eol_import_instantiation(instance):
    assert isinstance(instance, eol_Import)

@given(instance=eol_Block_strategy)
@settings(max_examples=50)
def test_eol_block_instantiation(instance):
    assert isinstance(instance, eol_Block)

@given(instance=EolLibraryModule_strategy)
@settings(max_examples=50)
def test_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, EolLibraryModule)

@given(instance=eol_EolProgram_strategy)
@settings(max_examples=50)
def test_eol_eolprogram_instantiation(instance):
    assert isinstance(instance, eol_EolProgram)

@given(instance=eol_TextPosition_strategy)
@settings(max_examples=50)
def test_eol_textposition_instantiation(instance):
    assert isinstance(instance, eol_TextPosition)



@given(instance=eol_TextPosition_strategy)
def test_eol_textposition_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=eol_TextPosition_strategy)
def test_eol_textposition_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=eol_TextRegion_strategy)
@settings(max_examples=50)
def test_eol_textregion_instantiation(instance):
    assert isinstance(instance, eol_TextRegion)

@given(instance=eol_EolElement_strategy)
@settings(max_examples=50)
def test_eol_eolelement_instantiation(instance):
    assert isinstance(instance, eol_EolElement)



@given(instance=eol_EolElement_strategy)
def test_eol_eolelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=eol_EolElement_strategy)
def test_eol_eolelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=eol_EolElement_strategy)
def test_eol_eolelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=eol_FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol_featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol_FeatureCallExpression)

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol_LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOrEqualToOperatorExpression)

@given(instance=eol_GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOrEqualToOperatorExpression)

@given(instance=eol_LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_LessThanOperatorExpression)

@given(instance=eol_NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_NotEqualsOperatorExpression)

@given(instance=eol_GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_GreaterThanOperatorExpression)

@given(instance=eol_EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_EqualsOperatorExpression)

@given(instance=eol_ModelExpression_strategy)
@settings(max_examples=50)
def test_eol_modelexpression_instantiation(instance):
    assert isinstance(instance, eol_ModelExpression)

@given(instance=eol_NameExpression_strategy)
@settings(max_examples=50)
def test_eol_nameexpression_instantiation(instance):
    assert isinstance(instance, eol_NameExpression)



@given(instance=eol_NameExpression_strategy)
def test_eol_nameexpression_resolvedContent_setter(instance):
    original = instance.resolvedContent
    instance.resolvedContent = original
    assert instance.resolvedContent == original



@given(instance=eol_NameExpression_strategy)
def test_eol_nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol_EnumerationLiteralExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol_MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_MultiplyOperatorExpression)

@given(instance=eol_MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_MinusOperatorExpression)

@given(instance=eol_PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_PlusOperatorExpression)

@given(instance=eol_DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_DivideOperatorExpression)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol_RealExpression_strategy)
@settings(max_examples=50)
def test_eol_realexpression_instantiation(instance):
    assert isinstance(instance, eol_RealExpression)



@given(instance=eol_RealExpression_strategy)
def test_eol_realexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol_IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol_integerexpression_instantiation(instance):
    assert isinstance(instance, eol_IntegerExpression)



@given(instance=eol_IntegerExpression_strategy)
def test_eol_integerexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol_StringExpression_strategy)
@settings(max_examples=50)
def test_eol_stringexpression_instantiation(instance):
    assert isinstance(instance, eol_StringExpression)



@given(instance=eol_StringExpression_strategy)
def test_eol_stringexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol_BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol_booleanexpression_instantiation(instance):
    assert isinstance(instance, eol_BooleanExpression)



@given(instance=eol_BooleanExpression_strategy)
def test_eol_booleanexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol_LiteralExpression_strategy)
@settings(max_examples=50)
def test_eol_literalexpression_instantiation(instance):
    assert isinstance(instance, eol_LiteralExpression)

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol_OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_OrOperatorExpression)

@given(instance=eol_XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_XorOperatorExpression)

@given(instance=eol_ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_ImpliesOperatorExpression)

@given(instance=eol_AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol_andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol_AndOperatorExpression)

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
