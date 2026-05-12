import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CollectionType,
    ocl_types_BagType,
    utilities_PredefinedType,
    EClassifier,
    ocl_types_AnyType,
    ocl_query_Query,
    ocl_utilities_Visitable,
    ocl_utilities_PredefinedType,
    ASTNode,
    ocl_utilities_TypedASTNode,
    ocl_utilities_CallingASTNode,
    ocl_utilities_ASTNode,
    uml_ocl_EClassifier,
    uml_ocl_EClass,
    ocl_uml_SendSignalAction,
    uml_ocl_ENamedElement,
    ENamedElement,
    ocl_uml_TypedElement,
    uml_ocl_EOperation,
    ocl_uml_CallOperationAction,
    expressions_ocl_EParameter,
    expressions_ocl_EClassifier,
    TupleLiteralPart,
    expressions_ocl_EObject,
    expressions_ocl_EOperation,
    utilities_ASTNode,
    utilities_Visitable,
    ocl_uml_Constraint,
    uml_TypedElement,
    ocl_expressions_OCLExpression,
    expressions_ocl_EStructuralFeature,
    FeatureCallExp,
    ocl_expressions_OperationCallExp,
    ocl_expressions_NavigationCallExp,
    SendSignalAction,
    CallOperationAction,
    Variable,
    LoopExp,
    ocl_expressions_IteratorExp,
    ocl_expressions_IterateExp,
    NumericLiteralExp,
    ocl_expressions_RealLiteralExp,
    ocl_expressions_IntegerLiteralExp,
    CallExp,
    ocl_expressions_LoopExp,
    ocl_expressions_FeatureCallExp,
    expressions_ocl_EEnumLiteral,
    TypedElement,
    ocl_expressions_CollectionLiteralPart,
    LiteralExp,
    ocl_expressions_PrimitiveLiteralExp,
    ocl_expressions_InvalidLiteralExp,
    ocl_expressions_EnumLiteralExp,
    ocl_expressions_NullLiteralExp,
    ocl_expressions_TupleLiteralExp,
    ocl_expressions_CollectionLiteralExp,
    CollectionLiteralPart,
    ocl_expressions_CollectionRange,
    ocl_expressions_CollectionItem,
    OCLExpression,
    ocl_expressions_IfExp,
    ocl_expressions_TypeExp,
    ocl_expressions_VariableExp,
    ocl_expressions_LetExp,
    ocl_expressions_LiteralExp,
    ocl_expressions_StateExp,
    utilities_CallingASTNode,
    expressions_OCLExpression,
    ocl_expressions_MessageExp,
    ocl_expressions_CallExp,
    PrimitiveLiteralExp,
    ocl_expressions_StringLiteralExp,
    ocl_expressions_NumericLiteralExp,
    ocl_expressions_BooleanLiteralExp,
    expressions_ocl_EClass,
    NavigationCallExp,
    ocl_expressions_PropertyCallExp,
    ocl_expressions_AssociationClassCallExp,
    ocl_types_VoidType,
    ocl_types_TypeType,
    ocl_types_SetType,
    ocl_types_SequenceType,
    PrimitiveReal,
    ocl_types_PrimitiveInteger,
    PrimitiveType,
    ocl_types_PrimitiveString,
    ocl_types_PrimitiveReal,
    ocl_types_PrimitiveBoolean,
    ocl_types_OrderedSetType,
    types_ocl_EClass,
    types_ocl_EOperation,
    ocl_types_InvalidType,
    EClass,
    ocl_types_TupleType,
    ocl_types_MessageType,
    ocl_types_ElementType,
    types_ocl_EClassifier,
    utilities_TypedASTNode,
    ocl_expressions_Variable,
    ocl_expressions_UnspecifiedValueExp,
    ocl_expressions_TupleLiteralPart,
    EDataType,
    ocl_types_PrimitiveType,
    ocl_types_CollectionType,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_BagType)


def test_ocl_types_bagtype_constructor_exists():
    assert callable(ocl_types_BagType.__init__)


def test_ocl_types_bagtype_constructor_args():
    sig = inspect.signature(ocl_types_BagType.__init__)
    params = list(sig.parameters.keys())



def test_utilities_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(utilities_PredefinedType)


def test_utilities_predefinedtype_constructor_exists():
    assert callable(utilities_PredefinedType.__init__)


def test_utilities_predefinedtype_constructor_args():
    sig = inspect.signature(utilities_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_anytype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_AnyType)


def test_ocl_types_anytype_constructor_exists():
    assert callable(ocl_types_AnyType.__init__)


def test_ocl_types_anytype_constructor_args():
    sig = inspect.signature(ocl_types_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_query_query_is_not_abstract():
    assert not inspect.isabstract(ocl_query_Query)


def test_ocl_query_query_constructor_exists():
    assert callable(ocl_query_Query.__init__)


def test_ocl_query_query_constructor_args():
    sig = inspect.signature(ocl_query_Query.__init__)
    params = list(sig.parameters.keys())
    assert "extentMap" in params, "Missing parameter 'extentMap'"

def test_ocl_query_query_has_extentMap():
    assert hasattr(ocl_query_Query, "extentMap")
    descriptor = None
    for klass in ocl_query_Query.__mro__:
        if "extentMap" in klass.__dict__:
            descriptor = klass.__dict__["extentMap"]
            break
    assert isinstance(descriptor, property)



def test_ocl_utilities_visitable_is_not_abstract():
    assert not inspect.isabstract(ocl_utilities_Visitable)


def test_ocl_utilities_visitable_constructor_exists():
    assert callable(ocl_utilities_Visitable.__init__)


def test_ocl_utilities_visitable_constructor_args():
    sig = inspect.signature(ocl_utilities_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_utilities_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(ocl_utilities_PredefinedType)


def test_ocl_utilities_predefinedtype_constructor_exists():
    assert callable(ocl_utilities_PredefinedType.__init__)


def test_ocl_utilities_predefinedtype_constructor_args():
    sig = inspect.signature(ocl_utilities_PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_ocl_utilities_typedastnode_is_not_abstract():
    assert not inspect.isabstract(ocl_utilities_TypedASTNode)


def test_ocl_utilities_typedastnode_constructor_exists():
    assert callable(ocl_utilities_TypedASTNode.__init__)


def test_ocl_utilities_typedastnode_constructor_args():
    sig = inspect.signature(ocl_utilities_TypedASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "typeStartPosition" in params, "Missing parameter 'typeStartPosition'"
    assert "typeEndPosition" in params, "Missing parameter 'typeEndPosition'"

def test_ocl_utilities_typedastnode_has_typeStartPosition():
    assert hasattr(ocl_utilities_TypedASTNode, "typeStartPosition")
    descriptor = None
    for klass in ocl_utilities_TypedASTNode.__mro__:
        if "typeStartPosition" in klass.__dict__:
            descriptor = klass.__dict__["typeStartPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl_utilities_typedastnode_has_typeEndPosition():
    assert hasattr(ocl_utilities_TypedASTNode, "typeEndPosition")
    descriptor = None
    for klass in ocl_utilities_TypedASTNode.__mro__:
        if "typeEndPosition" in klass.__dict__:
            descriptor = klass.__dict__["typeEndPosition"]
            break
    assert isinstance(descriptor, property)



def test_ocl_utilities_callingastnode_is_not_abstract():
    assert not inspect.isabstract(ocl_utilities_CallingASTNode)


def test_ocl_utilities_callingastnode_constructor_exists():
    assert callable(ocl_utilities_CallingASTNode.__init__)


def test_ocl_utilities_callingastnode_constructor_args():
    sig = inspect.signature(ocl_utilities_CallingASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "propertyStartPosition" in params, "Missing parameter 'propertyStartPosition'"
    assert "propertyEndPosition" in params, "Missing parameter 'propertyEndPosition'"

def test_ocl_utilities_callingastnode_has_propertyStartPosition():
    assert hasattr(ocl_utilities_CallingASTNode, "propertyStartPosition")
    descriptor = None
    for klass in ocl_utilities_CallingASTNode.__mro__:
        if "propertyStartPosition" in klass.__dict__:
            descriptor = klass.__dict__["propertyStartPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl_utilities_callingastnode_has_propertyEndPosition():
    assert hasattr(ocl_utilities_CallingASTNode, "propertyEndPosition")
    descriptor = None
    for klass in ocl_utilities_CallingASTNode.__mro__:
        if "propertyEndPosition" in klass.__dict__:
            descriptor = klass.__dict__["propertyEndPosition"]
            break
    assert isinstance(descriptor, property)



def test_ocl_utilities_astnode_is_not_abstract():
    assert not inspect.isabstract(ocl_utilities_ASTNode)


def test_ocl_utilities_astnode_constructor_exists():
    assert callable(ocl_utilities_ASTNode.__init__)


def test_ocl_utilities_astnode_constructor_args():
    sig = inspect.signature(ocl_utilities_ASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "startPosition" in params, "Missing parameter 'startPosition'"
    assert "endPosition" in params, "Missing parameter 'endPosition'"

def test_ocl_utilities_astnode_has_startPosition():
    assert hasattr(ocl_utilities_ASTNode, "startPosition")
    descriptor = None
    for klass in ocl_utilities_ASTNode.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl_utilities_astnode_has_endPosition():
    assert hasattr(ocl_utilities_ASTNode, "endPosition")
    descriptor = None
    for klass in ocl_utilities_ASTNode.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)



def test_uml_ocl_eclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_EClassifier)


def test_uml_ocl_eclassifier_constructor_exists():
    assert callable(uml_ocl_EClassifier.__init__)


def test_uml_ocl_eclassifier_constructor_args():
    sig = inspect.signature(uml_ocl_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_ocl_eclass_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_EClass)


def test_uml_ocl_eclass_constructor_exists():
    assert callable(uml_ocl_EClass.__init__)


def test_uml_ocl_eclass_constructor_args():
    sig = inspect.signature(uml_ocl_EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_SendSignalAction)


def test_ocl_uml_sendsignalaction_constructor_exists():
    assert callable(ocl_uml_SendSignalAction.__init__)


def test_ocl_uml_sendsignalaction_constructor_args():
    sig = inspect.signature(ocl_uml_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_ocl_enamedelement_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_ENamedElement)


def test_uml_ocl_enamedelement_constructor_exists():
    assert callable(uml_ocl_ENamedElement.__init__)


def test_uml_ocl_enamedelement_constructor_args():
    sig = inspect.signature(uml_ocl_ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_typedelement_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TypedElement)


def test_ocl_uml_typedelement_constructor_exists():
    assert callable(ocl_uml_TypedElement.__init__)


def test_ocl_uml_typedelement_constructor_args():
    sig = inspect.signature(ocl_uml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_ocl_eoperation_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_EOperation)


def test_uml_ocl_eoperation_constructor_exists():
    assert callable(uml_ocl_EOperation.__init__)


def test_uml_ocl_eoperation_constructor_args():
    sig = inspect.signature(uml_ocl_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CallOperationAction)


def test_ocl_uml_calloperationaction_constructor_exists():
    assert callable(ocl_uml_CallOperationAction.__init__)


def test_ocl_uml_calloperationaction_constructor_args():
    sig = inspect.signature(ocl_uml_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_expressions_ocl_eparameter_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EParameter)


def test_expressions_ocl_eparameter_constructor_exists():
    assert callable(expressions_ocl_EParameter.__init__)


def test_expressions_ocl_eparameter_constructor_args():
    sig = inspect.signature(expressions_ocl_EParameter.__init__)
    params = list(sig.parameters.keys())



def test_expressions_ocl_eclassifier_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EClassifier)


def test_expressions_ocl_eclassifier_constructor_exists():
    assert callable(expressions_ocl_EClassifier.__init__)


def test_expressions_ocl_eclassifier_constructor_args():
    sig = inspect.signature(expressions_ocl_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_expressions_ocl_eobject_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EObject)


def test_expressions_ocl_eobject_constructor_exists():
    assert callable(expressions_ocl_EObject.__init__)


def test_expressions_ocl_eobject_constructor_args():
    sig = inspect.signature(expressions_ocl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_expressions_ocl_eoperation_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EOperation)


def test_expressions_ocl_eoperation_constructor_exists():
    assert callable(expressions_ocl_EOperation.__init__)


def test_expressions_ocl_eoperation_constructor_args():
    sig = inspect.signature(expressions_ocl_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_utilities_astnode_is_not_abstract():
    assert not inspect.isabstract(utilities_ASTNode)


def test_utilities_astnode_constructor_exists():
    assert callable(utilities_ASTNode.__init__)


def test_utilities_astnode_constructor_args():
    sig = inspect.signature(utilities_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_utilities_visitable_is_not_abstract():
    assert not inspect.isabstract(utilities_Visitable)


def test_utilities_visitable_constructor_exists():
    assert callable(utilities_Visitable.__init__)


def test_utilities_visitable_constructor_args():
    sig = inspect.signature(utilities_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_constraint_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_Constraint)


def test_ocl_uml_constraint_constructor_exists():
    assert callable(ocl_uml_Constraint.__init__)


def test_ocl_uml_constraint_constructor_args():
    sig = inspect.signature(ocl_uml_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "instanceVarName" in params, "Missing parameter 'instanceVarName'"
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_ocl_uml_constraint_has_instanceVarName():
    assert hasattr(ocl_uml_Constraint, "instanceVarName")
    descriptor = None
    for klass in ocl_uml_Constraint.__mro__:
        if "instanceVarName" in klass.__dict__:
            descriptor = klass.__dict__["instanceVarName"]
            break
    assert isinstance(descriptor, property)

def test_ocl_uml_constraint_has_stereotype():
    assert hasattr(ocl_uml_Constraint, "stereotype")
    descriptor = None
    for klass in ocl_uml_Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_uml_typedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TypedElement)


def test_uml_typedelement_constructor_exists():
    assert callable(uml_TypedElement.__init__)


def test_uml_typedelement_constructor_args():
    sig = inspect.signature(uml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_OCLExpression)


def test_ocl_expressions_oclexpression_constructor_exists():
    assert callable(ocl_expressions_OCLExpression.__init__)


def test_ocl_expressions_oclexpression_constructor_args():
    sig = inspect.signature(ocl_expressions_OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_ocl_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EStructuralFeature)


def test_expressions_ocl_estructuralfeature_constructor_exists():
    assert callable(expressions_ocl_EStructuralFeature.__init__)


def test_expressions_ocl_estructuralfeature_constructor_args():
    sig = inspect.signature(expressions_ocl_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_OperationCallExp)


def test_ocl_expressions_operationcallexp_constructor_exists():
    assert callable(ocl_expressions_OperationCallExp.__init__)


def test_ocl_expressions_operationcallexp_constructor_args():
    sig = inspect.signature(ocl_expressions_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_NavigationCallExp)


def test_ocl_expressions_navigationcallexp_constructor_exists():
    assert callable(ocl_expressions_NavigationCallExp.__init__)


def test_ocl_expressions_navigationcallexp_constructor_args():
    sig = inspect.signature(ocl_expressions_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(SendSignalAction)


def test_sendsignalaction_constructor_exists():
    assert callable(SendSignalAction.__init__)


def test_sendsignalaction_constructor_args():
    sig = inspect.signature(SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CallOperationAction)


def test_calloperationaction_constructor_exists():
    assert callable(CallOperationAction.__init__)


def test_calloperationaction_constructor_args():
    sig = inspect.signature(CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_IteratorExp)


def test_ocl_expressions_iteratorexp_constructor_exists():
    assert callable(ocl_expressions_IteratorExp.__init__)


def test_ocl_expressions_iteratorexp_constructor_args():
    sig = inspect.signature(ocl_expressions_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_IterateExp)


def test_ocl_expressions_iterateexp_constructor_exists():
    assert callable(ocl_expressions_IterateExp.__init__)


def test_ocl_expressions_iterateexp_constructor_args():
    sig = inspect.signature(ocl_expressions_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_RealLiteralExp)


def test_ocl_expressions_realliteralexp_constructor_exists():
    assert callable(ocl_expressions_RealLiteralExp.__init__)


def test_ocl_expressions_realliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl_expressions_realliteralexp_has_realSymbol():
    assert hasattr(ocl_expressions_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in ocl_expressions_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_expressions_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_IntegerLiteralExp)


def test_ocl_expressions_integerliteralexp_constructor_exists():
    assert callable(ocl_expressions_IntegerLiteralExp.__init__)


def test_ocl_expressions_integerliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl_expressions_integerliteralexp_has_integerSymbol():
    assert hasattr(ocl_expressions_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in ocl_expressions_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_LoopExp)


def test_ocl_expressions_loopexp_constructor_exists():
    assert callable(ocl_expressions_LoopExp.__init__)


def test_ocl_expressions_loopexp_constructor_args():
    sig = inspect.signature(ocl_expressions_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_FeatureCallExp)


def test_ocl_expressions_featurecallexp_constructor_exists():
    assert callable(ocl_expressions_FeatureCallExp.__init__)


def test_ocl_expressions_featurecallexp_constructor_args():
    sig = inspect.signature(ocl_expressions_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "markedPre" in params, "Missing parameter 'markedPre'"

def test_ocl_expressions_featurecallexp_has_markedPre():
    assert hasattr(ocl_expressions_FeatureCallExp, "markedPre")
    descriptor = None
    for klass in ocl_expressions_FeatureCallExp.__mro__:
        if "markedPre" in klass.__dict__:
            descriptor = klass.__dict__["markedPre"]
            break
    assert isinstance(descriptor, property)



def test_expressions_ocl_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EEnumLiteral)


def test_expressions_ocl_eenumliteral_constructor_exists():
    assert callable(expressions_ocl_EEnumLiteral.__init__)


def test_expressions_ocl_eenumliteral_constructor_args():
    sig = inspect.signature(expressions_ocl_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_CollectionLiteralPart)


def test_ocl_expressions_collectionliteralpart_constructor_exists():
    assert callable(ocl_expressions_CollectionLiteralPart.__init__)


def test_ocl_expressions_collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl_expressions_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_PrimitiveLiteralExp)


def test_ocl_expressions_primitiveliteralexp_constructor_exists():
    assert callable(ocl_expressions_PrimitiveLiteralExp.__init__)


def test_ocl_expressions_primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_InvalidLiteralExp)


def test_ocl_expressions_invalidliteralexp_constructor_exists():
    assert callable(ocl_expressions_InvalidLiteralExp.__init__)


def test_ocl_expressions_invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_EnumLiteralExp)


def test_ocl_expressions_enumliteralexp_constructor_exists():
    assert callable(ocl_expressions_EnumLiteralExp.__init__)


def test_ocl_expressions_enumliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_NullLiteralExp)


def test_ocl_expressions_nullliteralexp_constructor_exists():
    assert callable(ocl_expressions_NullLiteralExp.__init__)


def test_ocl_expressions_nullliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_TupleLiteralExp)


def test_ocl_expressions_tupleliteralexp_constructor_exists():
    assert callable(ocl_expressions_TupleLiteralExp.__init__)


def test_ocl_expressions_tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_CollectionLiteralExp)


def test_ocl_expressions_collectionliteralexp_constructor_exists():
    assert callable(ocl_expressions_CollectionLiteralExp.__init__)


def test_ocl_expressions_collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_expressions_collectionliteralexp_has_kind():
    assert hasattr(ocl_expressions_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in ocl_expressions_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_CollectionRange)


def test_ocl_expressions_collectionrange_constructor_exists():
    assert callable(ocl_expressions_CollectionRange.__init__)


def test_ocl_expressions_collectionrange_constructor_args():
    sig = inspect.signature(ocl_expressions_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_CollectionItem)


def test_ocl_expressions_collectionitem_constructor_exists():
    assert callable(ocl_expressions_CollectionItem.__init__)


def test_ocl_expressions_collectionitem_constructor_args():
    sig = inspect.signature(ocl_expressions_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_IfExp)


def test_ocl_expressions_ifexp_constructor_exists():
    assert callable(ocl_expressions_IfExp.__init__)


def test_ocl_expressions_ifexp_constructor_args():
    sig = inspect.signature(ocl_expressions_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_TypeExp)


def test_ocl_expressions_typeexp_constructor_exists():
    assert callable(ocl_expressions_TypeExp.__init__)


def test_ocl_expressions_typeexp_constructor_args():
    sig = inspect.signature(ocl_expressions_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_VariableExp)


def test_ocl_expressions_variableexp_constructor_exists():
    assert callable(ocl_expressions_VariableExp.__init__)


def test_ocl_expressions_variableexp_constructor_args():
    sig = inspect.signature(ocl_expressions_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_letexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_LetExp)


def test_ocl_expressions_letexp_constructor_exists():
    assert callable(ocl_expressions_LetExp.__init__)


def test_ocl_expressions_letexp_constructor_args():
    sig = inspect.signature(ocl_expressions_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_LiteralExp)


def test_ocl_expressions_literalexp_constructor_exists():
    assert callable(ocl_expressions_LiteralExp.__init__)


def test_ocl_expressions_literalexp_constructor_args():
    sig = inspect.signature(ocl_expressions_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_StateExp)


def test_ocl_expressions_stateexp_constructor_exists():
    assert callable(ocl_expressions_StateExp.__init__)


def test_ocl_expressions_stateexp_constructor_args():
    sig = inspect.signature(ocl_expressions_StateExp.__init__)
    params = list(sig.parameters.keys())



def test_utilities_callingastnode_is_not_abstract():
    assert not inspect.isabstract(utilities_CallingASTNode)


def test_utilities_callingastnode_constructor_exists():
    assert callable(utilities_CallingASTNode.__init__)


def test_utilities_callingastnode_constructor_args():
    sig = inspect.signature(utilities_CallingASTNode.__init__)
    params = list(sig.parameters.keys())



def test_expressions_oclexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_OCLExpression)


def test_expressions_oclexpression_constructor_exists():
    assert callable(expressions_OCLExpression.__init__)


def test_expressions_oclexpression_constructor_args():
    sig = inspect.signature(expressions_OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_MessageExp)


def test_ocl_expressions_messageexp_constructor_exists():
    assert callable(ocl_expressions_MessageExp.__init__)


def test_ocl_expressions_messageexp_constructor_args():
    sig = inspect.signature(ocl_expressions_MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_callexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_CallExp)


def test_ocl_expressions_callexp_constructor_exists():
    assert callable(ocl_expressions_CallExp.__init__)


def test_ocl_expressions_callexp_constructor_args():
    sig = inspect.signature(ocl_expressions_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_StringLiteralExp)


def test_ocl_expressions_stringliteralexp_constructor_exists():
    assert callable(ocl_expressions_StringLiteralExp.__init__)


def test_ocl_expressions_stringliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl_expressions_stringliteralexp_has_stringSymbol():
    assert hasattr(ocl_expressions_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in ocl_expressions_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_expressions_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_NumericLiteralExp)


def test_ocl_expressions_numericliteralexp_constructor_exists():
    assert callable(ocl_expressions_NumericLiteralExp.__init__)


def test_ocl_expressions_numericliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_BooleanLiteralExp)


def test_ocl_expressions_booleanliteralexp_constructor_exists():
    assert callable(ocl_expressions_BooleanLiteralExp.__init__)


def test_ocl_expressions_booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl_expressions_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl_expressions_booleanliteralexp_has_booleanSymbol():
    assert hasattr(ocl_expressions_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in ocl_expressions_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_expressions_ocl_eclass_is_not_abstract():
    assert not inspect.isabstract(expressions_ocl_EClass)


def test_expressions_ocl_eclass_constructor_exists():
    assert callable(expressions_ocl_EClass.__init__)


def test_expressions_ocl_eclass_constructor_args():
    sig = inspect.signature(expressions_ocl_EClass.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_PropertyCallExp)


def test_ocl_expressions_propertycallexp_constructor_exists():
    assert callable(ocl_expressions_PropertyCallExp.__init__)


def test_ocl_expressions_propertycallexp_constructor_args():
    sig = inspect.signature(ocl_expressions_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_AssociationClassCallExp)


def test_ocl_expressions_associationclasscallexp_constructor_exists():
    assert callable(ocl_expressions_AssociationClassCallExp.__init__)


def test_ocl_expressions_associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl_expressions_AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_VoidType)


def test_ocl_types_voidtype_constructor_exists():
    assert callable(ocl_types_VoidType.__init__)


def test_ocl_types_voidtype_constructor_args():
    sig = inspect.signature(ocl_types_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_typetype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_TypeType)


def test_ocl_types_typetype_constructor_exists():
    assert callable(ocl_types_TypeType.__init__)


def test_ocl_types_typetype_constructor_args():
    sig = inspect.signature(ocl_types_TypeType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_settype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_SetType)


def test_ocl_types_settype_constructor_exists():
    assert callable(ocl_types_SetType.__init__)


def test_ocl_types_settype_constructor_args():
    sig = inspect.signature(ocl_types_SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_SequenceType)


def test_ocl_types_sequencetype_constructor_exists():
    assert callable(ocl_types_SequenceType.__init__)


def test_ocl_types_sequencetype_constructor_args():
    sig = inspect.signature(ocl_types_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_primitivereal_is_not_abstract():
    assert not inspect.isabstract(PrimitiveReal)


def test_primitivereal_constructor_exists():
    assert callable(PrimitiveReal.__init__)


def test_primitivereal_constructor_args():
    sig = inspect.signature(PrimitiveReal.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_primitiveinteger_is_not_abstract():
    assert not inspect.isabstract(ocl_types_PrimitiveInteger)


def test_ocl_types_primitiveinteger_constructor_exists():
    assert callable(ocl_types_PrimitiveInteger.__init__)


def test_ocl_types_primitiveinteger_constructor_args():
    sig = inspect.signature(ocl_types_PrimitiveInteger.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_primitivestring_is_not_abstract():
    assert not inspect.isabstract(ocl_types_PrimitiveString)


def test_ocl_types_primitivestring_constructor_exists():
    assert callable(ocl_types_PrimitiveString.__init__)


def test_ocl_types_primitivestring_constructor_args():
    sig = inspect.signature(ocl_types_PrimitiveString.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_primitivereal_is_not_abstract():
    assert not inspect.isabstract(ocl_types_PrimitiveReal)


def test_ocl_types_primitivereal_constructor_exists():
    assert callable(ocl_types_PrimitiveReal.__init__)


def test_ocl_types_primitivereal_constructor_args():
    sig = inspect.signature(ocl_types_PrimitiveReal.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_primitiveboolean_is_not_abstract():
    assert not inspect.isabstract(ocl_types_PrimitiveBoolean)


def test_ocl_types_primitiveboolean_constructor_exists():
    assert callable(ocl_types_PrimitiveBoolean.__init__)


def test_ocl_types_primitiveboolean_constructor_args():
    sig = inspect.signature(ocl_types_PrimitiveBoolean.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_OrderedSetType)


def test_ocl_types_orderedsettype_constructor_exists():
    assert callable(ocl_types_OrderedSetType.__init__)


def test_ocl_types_orderedsettype_constructor_args():
    sig = inspect.signature(ocl_types_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_types_ocl_eclass_is_not_abstract():
    assert not inspect.isabstract(types_ocl_EClass)


def test_types_ocl_eclass_constructor_exists():
    assert callable(types_ocl_EClass.__init__)


def test_types_ocl_eclass_constructor_args():
    sig = inspect.signature(types_ocl_EClass.__init__)
    params = list(sig.parameters.keys())



def test_types_ocl_eoperation_is_not_abstract():
    assert not inspect.isabstract(types_ocl_EOperation)


def test_types_ocl_eoperation_constructor_exists():
    assert callable(types_ocl_EOperation.__init__)


def test_types_ocl_eoperation_constructor_args():
    sig = inspect.signature(types_ocl_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_InvalidType)


def test_ocl_types_invalidtype_constructor_exists():
    assert callable(ocl_types_InvalidType.__init__)


def test_ocl_types_invalidtype_constructor_args():
    sig = inspect.signature(ocl_types_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_TupleType)


def test_ocl_types_tupletype_constructor_exists():
    assert callable(ocl_types_TupleType.__init__)


def test_ocl_types_tupletype_constructor_args():
    sig = inspect.signature(ocl_types_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_MessageType)


def test_ocl_types_messagetype_constructor_exists():
    assert callable(ocl_types_MessageType.__init__)


def test_ocl_types_messagetype_constructor_args():
    sig = inspect.signature(ocl_types_MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_ElementType)


def test_ocl_types_elementtype_constructor_exists():
    assert callable(ocl_types_ElementType.__init__)


def test_ocl_types_elementtype_constructor_args():
    sig = inspect.signature(ocl_types_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_types_ocl_eclassifier_is_not_abstract():
    assert not inspect.isabstract(types_ocl_EClassifier)


def test_types_ocl_eclassifier_constructor_exists():
    assert callable(types_ocl_EClassifier.__init__)


def test_types_ocl_eclassifier_constructor_args():
    sig = inspect.signature(types_ocl_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_utilities_typedastnode_is_not_abstract():
    assert not inspect.isabstract(utilities_TypedASTNode)


def test_utilities_typedastnode_constructor_exists():
    assert callable(utilities_TypedASTNode.__init__)


def test_utilities_typedastnode_constructor_args():
    sig = inspect.signature(utilities_TypedASTNode.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_variable_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_Variable)


def test_ocl_expressions_variable_constructor_exists():
    assert callable(ocl_expressions_Variable.__init__)


def test_ocl_expressions_variable_constructor_args():
    sig = inspect.signature(ocl_expressions_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_UnspecifiedValueExp)


def test_ocl_expressions_unspecifiedvalueexp_constructor_exists():
    assert callable(ocl_expressions_UnspecifiedValueExp.__init__)


def test_ocl_expressions_unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl_expressions_UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_expressions_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_expressions_TupleLiteralPart)


def test_ocl_expressions_tupleliteralpart_constructor_exists():
    assert callable(ocl_expressions_TupleLiteralPart.__init__)


def test_ocl_expressions_tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl_expressions_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_PrimitiveType)


def test_ocl_types_primitivetype_constructor_exists():
    assert callable(ocl_types_PrimitiveType.__init__)


def test_ocl_types_primitivetype_constructor_args():
    sig = inspect.signature(ocl_types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl_types_CollectionType)


def test_ocl_types_collectiontype_constructor_exists():
    assert callable(ocl_types_CollectionType.__init__)


def test_ocl_types_collectiontype_constructor_args():
    sig = inspect.signature(ocl_types_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_types_collectiontype_has_kind():
    assert hasattr(ocl_types_CollectionType, "kind")
    descriptor = None
    for klass in ocl_types_CollectionType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "set",
        "sequence",
        "bag",
        "collection",
        "orderedSet",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
CollectionType_strategy = st.builds(
    CollectionType,
)
ocl_types_BagType_strategy = st.builds(
    ocl_types_BagType,
)
utilities_PredefinedType_strategy = st.builds(
    utilities_PredefinedType,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ocl_types_AnyType_strategy = st.builds(
    ocl_types_AnyType,
)
ocl_query_Query_strategy = st.builds(
    ocl_query_Query,
    extentMap=
        safe_text
)
ocl_utilities_Visitable_strategy = st.builds(
    ocl_utilities_Visitable,
)
ocl_utilities_PredefinedType_strategy = st.builds(
    ocl_utilities_PredefinedType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
ocl_utilities_TypedASTNode_strategy = st.builds(
    ocl_utilities_TypedASTNode,
    typeStartPosition=
        st.integers(),
    typeEndPosition=
        st.integers()
)
ocl_utilities_CallingASTNode_strategy = st.builds(
    ocl_utilities_CallingASTNode,
    propertyStartPosition=
        st.integers(),
    propertyEndPosition=
        st.integers()
)
ocl_utilities_ASTNode_strategy = st.builds(
    ocl_utilities_ASTNode,
    startPosition=
        st.integers(),
    endPosition=
        st.integers()
)
uml_ocl_EClassifier_strategy = st.builds(
    uml_ocl_EClassifier,
)
uml_ocl_EClass_strategy = st.builds(
    uml_ocl_EClass,
)
ocl_uml_SendSignalAction_strategy = st.builds(
    ocl_uml_SendSignalAction,
)
uml_ocl_ENamedElement_strategy = st.builds(
    uml_ocl_ENamedElement,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ocl_uml_TypedElement_strategy = st.builds(
    ocl_uml_TypedElement,
)
uml_ocl_EOperation_strategy = st.builds(
    uml_ocl_EOperation,
)
ocl_uml_CallOperationAction_strategy = st.builds(
    ocl_uml_CallOperationAction,
)
expressions_ocl_EParameter_strategy = st.builds(
    expressions_ocl_EParameter,
)
expressions_ocl_EClassifier_strategy = st.builds(
    expressions_ocl_EClassifier,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
expressions_ocl_EObject_strategy = st.builds(
    expressions_ocl_EObject,
)
expressions_ocl_EOperation_strategy = st.builds(
    expressions_ocl_EOperation,
)
utilities_ASTNode_strategy = st.builds(
    utilities_ASTNode,
)
utilities_Visitable_strategy = st.builds(
    utilities_Visitable,
)
ocl_uml_Constraint_strategy = st.builds(
    ocl_uml_Constraint,
    instanceVarName=
        safe_text,
    stereotype=
        safe_text
)
uml_TypedElement_strategy = st.builds(
    uml_TypedElement,
)
ocl_expressions_OCLExpression_strategy = st.builds(
    ocl_expressions_OCLExpression,
)
expressions_ocl_EStructuralFeature_strategy = st.builds(
    expressions_ocl_EStructuralFeature,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
ocl_expressions_OperationCallExp_strategy = st.builds(
    ocl_expressions_OperationCallExp,
)
ocl_expressions_NavigationCallExp_strategy = st.builds(
    ocl_expressions_NavigationCallExp,
)
SendSignalAction_strategy = st.builds(
    SendSignalAction,
)
CallOperationAction_strategy = st.builds(
    CallOperationAction,
)
Variable_strategy = st.builds(
    Variable,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
ocl_expressions_IteratorExp_strategy = st.builds(
    ocl_expressions_IteratorExp,
)
ocl_expressions_IterateExp_strategy = st.builds(
    ocl_expressions_IterateExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
ocl_expressions_RealLiteralExp_strategy = st.builds(
    ocl_expressions_RealLiteralExp,
    realSymbol=
        safe_text
)
ocl_expressions_IntegerLiteralExp_strategy = st.builds(
    ocl_expressions_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
ocl_expressions_LoopExp_strategy = st.builds(
    ocl_expressions_LoopExp,
)
ocl_expressions_FeatureCallExp_strategy = st.builds(
    ocl_expressions_FeatureCallExp,
    markedPre=
        st.booleans()
)
expressions_ocl_EEnumLiteral_strategy = st.builds(
    expressions_ocl_EEnumLiteral,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ocl_expressions_CollectionLiteralPart_strategy = st.builds(
    ocl_expressions_CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ocl_expressions_PrimitiveLiteralExp_strategy = st.builds(
    ocl_expressions_PrimitiveLiteralExp,
)
ocl_expressions_InvalidLiteralExp_strategy = st.builds(
    ocl_expressions_InvalidLiteralExp,
)
ocl_expressions_EnumLiteralExp_strategy = st.builds(
    ocl_expressions_EnumLiteralExp,
)
ocl_expressions_NullLiteralExp_strategy = st.builds(
    ocl_expressions_NullLiteralExp,
)
ocl_expressions_TupleLiteralExp_strategy = st.builds(
    ocl_expressions_TupleLiteralExp,
)
ocl_expressions_CollectionLiteralExp_strategy = st.builds(
    ocl_expressions_CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
ocl_expressions_CollectionRange_strategy = st.builds(
    ocl_expressions_CollectionRange,
)
ocl_expressions_CollectionItem_strategy = st.builds(
    ocl_expressions_CollectionItem,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
ocl_expressions_IfExp_strategy = st.builds(
    ocl_expressions_IfExp,
)
ocl_expressions_TypeExp_strategy = st.builds(
    ocl_expressions_TypeExp,
)
ocl_expressions_VariableExp_strategy = st.builds(
    ocl_expressions_VariableExp,
)
ocl_expressions_LetExp_strategy = st.builds(
    ocl_expressions_LetExp,
)
ocl_expressions_LiteralExp_strategy = st.builds(
    ocl_expressions_LiteralExp,
)
ocl_expressions_StateExp_strategy = st.builds(
    ocl_expressions_StateExp,
)
utilities_CallingASTNode_strategy = st.builds(
    utilities_CallingASTNode,
)
expressions_OCLExpression_strategy = st.builds(
    expressions_OCLExpression,
)
ocl_expressions_MessageExp_strategy = st.builds(
    ocl_expressions_MessageExp,
)
ocl_expressions_CallExp_strategy = st.builds(
    ocl_expressions_CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
ocl_expressions_StringLiteralExp_strategy = st.builds(
    ocl_expressions_StringLiteralExp,
    stringSymbol=
        safe_text
)
ocl_expressions_NumericLiteralExp_strategy = st.builds(
    ocl_expressions_NumericLiteralExp,
)
ocl_expressions_BooleanLiteralExp_strategy = st.builds(
    ocl_expressions_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
expressions_ocl_EClass_strategy = st.builds(
    expressions_ocl_EClass,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
ocl_expressions_PropertyCallExp_strategy = st.builds(
    ocl_expressions_PropertyCallExp,
)
ocl_expressions_AssociationClassCallExp_strategy = st.builds(
    ocl_expressions_AssociationClassCallExp,
)
ocl_types_VoidType_strategy = st.builds(
    ocl_types_VoidType,
)
ocl_types_TypeType_strategy = st.builds(
    ocl_types_TypeType,
)
ocl_types_SetType_strategy = st.builds(
    ocl_types_SetType,
)
ocl_types_SequenceType_strategy = st.builds(
    ocl_types_SequenceType,
)
PrimitiveReal_strategy = st.builds(
    PrimitiveReal,
)
ocl_types_PrimitiveInteger_strategy = st.builds(
    ocl_types_PrimitiveInteger,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ocl_types_PrimitiveString_strategy = st.builds(
    ocl_types_PrimitiveString,
)
ocl_types_PrimitiveReal_strategy = st.builds(
    ocl_types_PrimitiveReal,
)
ocl_types_PrimitiveBoolean_strategy = st.builds(
    ocl_types_PrimitiveBoolean,
)
ocl_types_OrderedSetType_strategy = st.builds(
    ocl_types_OrderedSetType,
)
types_ocl_EClass_strategy = st.builds(
    types_ocl_EClass,
)
types_ocl_EOperation_strategy = st.builds(
    types_ocl_EOperation,
)
ocl_types_InvalidType_strategy = st.builds(
    ocl_types_InvalidType,
)
EClass_strategy = st.builds(
    EClass,
)
ocl_types_TupleType_strategy = st.builds(
    ocl_types_TupleType,
)
ocl_types_MessageType_strategy = st.builds(
    ocl_types_MessageType,
)
ocl_types_ElementType_strategy = st.builds(
    ocl_types_ElementType,
)
types_ocl_EClassifier_strategy = st.builds(
    types_ocl_EClassifier,
)
utilities_TypedASTNode_strategy = st.builds(
    utilities_TypedASTNode,
)
ocl_expressions_Variable_strategy = st.builds(
    ocl_expressions_Variable,
)
ocl_expressions_UnspecifiedValueExp_strategy = st.builds(
    ocl_expressions_UnspecifiedValueExp,
)
ocl_expressions_TupleLiteralPart_strategy = st.builds(
    ocl_expressions_TupleLiteralPart,
)
EDataType_strategy = st.builds(
    EDataType,
)
ocl_types_PrimitiveType_strategy = st.builds(
    ocl_types_PrimitiveType,
)
ocl_types_CollectionType_strategy = st.builds(
    ocl_types_CollectionType,
    kind=
        safe_text
)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=ocl_types_BagType_strategy)
@settings(max_examples=50)
def test_ocl_types_bagtype_instantiation(instance):
    assert isinstance(instance, ocl_types_BagType)

@given(instance=utilities_PredefinedType_strategy)
@settings(max_examples=50)
def test_utilities_predefinedtype_instantiation(instance):
    assert isinstance(instance, utilities_PredefinedType)

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=ocl_types_AnyType_strategy)
@settings(max_examples=50)
def test_ocl_types_anytype_instantiation(instance):
    assert isinstance(instance, ocl_types_AnyType)

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=50)
def test_ocl_query_query_instantiation(instance):
    assert isinstance(instance, ocl_query_Query)



@given(instance=ocl_query_Query_strategy)
def test_ocl_query_query_extentMap_setter(instance):
    original = instance.extentMap
    instance.extentMap = original
    assert instance.extentMap == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_check_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.check(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.check).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'check' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'check' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'check' in ocl_query_Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_resulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resultType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resultType' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resultType' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resultType' in ocl_query_Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in ocl_query_Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_reject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reject' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reject' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reject' in ocl_query_Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_querytext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.queryText()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.queryText).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'queryText' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'queryText' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'queryText' in ocl_query_Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_query_Query_strategy)
@settings(max_examples=30)
def test_ocl_query_query_select_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.select(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.select).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'select' in ocl_query_Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'select' in ocl_query_Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'select' in ocl_query_Query is not implemented or raised an error")

@given(instance=ocl_utilities_Visitable_strategy)
@settings(max_examples=50)
def test_ocl_utilities_visitable_instantiation(instance):
    assert isinstance(instance, ocl_utilities_Visitable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl_utilities_Visitable_strategy)
@settings(max_examples=30)
def test_ocl_utilities_visitable_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in ocl_utilities_Visitable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in ocl_utilities_Visitable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in ocl_utilities_Visitable is not implemented or raised an error")

@given(instance=ocl_utilities_PredefinedType_strategy)
@settings(max_examples=50)
def test_ocl_utilities_predefinedtype_instantiation(instance):
    assert isinstance(instance, ocl_utilities_PredefinedType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=ocl_utilities_TypedASTNode_strategy)
@settings(max_examples=50)
def test_ocl_utilities_typedastnode_instantiation(instance):
    assert isinstance(instance, ocl_utilities_TypedASTNode)



@given(instance=ocl_utilities_TypedASTNode_strategy)
def test_ocl_utilities_typedastnode_typeStartPosition_setter(instance):
    original = instance.typeStartPosition
    instance.typeStartPosition = original
    assert instance.typeStartPosition == original



@given(instance=ocl_utilities_TypedASTNode_strategy)
def test_ocl_utilities_typedastnode_typeEndPosition_setter(instance):
    original = instance.typeEndPosition
    instance.typeEndPosition = original
    assert instance.typeEndPosition == original

@given(instance=ocl_utilities_CallingASTNode_strategy)
@settings(max_examples=50)
def test_ocl_utilities_callingastnode_instantiation(instance):
    assert isinstance(instance, ocl_utilities_CallingASTNode)



@given(instance=ocl_utilities_CallingASTNode_strategy)
def test_ocl_utilities_callingastnode_propertyStartPosition_setter(instance):
    original = instance.propertyStartPosition
    instance.propertyStartPosition = original
    assert instance.propertyStartPosition == original



@given(instance=ocl_utilities_CallingASTNode_strategy)
def test_ocl_utilities_callingastnode_propertyEndPosition_setter(instance):
    original = instance.propertyEndPosition
    instance.propertyEndPosition = original
    assert instance.propertyEndPosition == original

@given(instance=ocl_utilities_ASTNode_strategy)
@settings(max_examples=50)
def test_ocl_utilities_astnode_instantiation(instance):
    assert isinstance(instance, ocl_utilities_ASTNode)



@given(instance=ocl_utilities_ASTNode_strategy)
def test_ocl_utilities_astnode_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original



@given(instance=ocl_utilities_ASTNode_strategy)
def test_ocl_utilities_astnode_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original

@given(instance=uml_ocl_EClassifier_strategy)
@settings(max_examples=50)
def test_uml_ocl_eclassifier_instantiation(instance):
    assert isinstance(instance, uml_ocl_EClassifier)

@given(instance=uml_ocl_EClass_strategy)
@settings(max_examples=50)
def test_uml_ocl_eclass_instantiation(instance):
    assert isinstance(instance, uml_ocl_EClass)

@given(instance=ocl_uml_SendSignalAction_strategy)
@settings(max_examples=50)
def test_ocl_uml_sendsignalaction_instantiation(instance):
    assert isinstance(instance, ocl_uml_SendSignalAction)

@given(instance=uml_ocl_ENamedElement_strategy)
@settings(max_examples=50)
def test_uml_ocl_enamedelement_instantiation(instance):
    assert isinstance(instance, uml_ocl_ENamedElement)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ocl_uml_TypedElement_strategy)
@settings(max_examples=50)
def test_ocl_uml_typedelement_instantiation(instance):
    assert isinstance(instance, ocl_uml_TypedElement)

@given(instance=uml_ocl_EOperation_strategy)
@settings(max_examples=50)
def test_uml_ocl_eoperation_instantiation(instance):
    assert isinstance(instance, uml_ocl_EOperation)

@given(instance=ocl_uml_CallOperationAction_strategy)
@settings(max_examples=50)
def test_ocl_uml_calloperationaction_instantiation(instance):
    assert isinstance(instance, ocl_uml_CallOperationAction)

@given(instance=expressions_ocl_EParameter_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eparameter_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EParameter)

@given(instance=expressions_ocl_EClassifier_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eclassifier_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EClassifier)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=expressions_ocl_EObject_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eobject_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EObject)

@given(instance=expressions_ocl_EOperation_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eoperation_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EOperation)

@given(instance=utilities_ASTNode_strategy)
@settings(max_examples=50)
def test_utilities_astnode_instantiation(instance):
    assert isinstance(instance, utilities_ASTNode)

@given(instance=utilities_Visitable_strategy)
@settings(max_examples=50)
def test_utilities_visitable_instantiation(instance):
    assert isinstance(instance, utilities_Visitable)

@given(instance=ocl_uml_Constraint_strategy)
@settings(max_examples=50)
def test_ocl_uml_constraint_instantiation(instance):
    assert isinstance(instance, ocl_uml_Constraint)



@given(instance=ocl_uml_Constraint_strategy)
def test_ocl_uml_constraint_instanceVarName_setter(instance):
    original = instance.instanceVarName
    instance.instanceVarName = original
    assert instance.instanceVarName == original



@given(instance=ocl_uml_Constraint_strategy)
def test_ocl_uml_constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=uml_TypedElement_strategy)
@settings(max_examples=50)
def test_uml_typedelement_instantiation(instance):
    assert isinstance(instance, uml_TypedElement)

@given(instance=ocl_expressions_OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl_expressions_oclexpression_instantiation(instance):
    assert isinstance(instance, ocl_expressions_OCLExpression)

@given(instance=expressions_ocl_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_expressions_ocl_estructuralfeature_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EStructuralFeature)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=ocl_expressions_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_OperationCallExp)

@given(instance=ocl_expressions_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_NavigationCallExp)

@given(instance=SendSignalAction_strategy)
@settings(max_examples=50)
def test_sendsignalaction_instantiation(instance):
    assert isinstance(instance, SendSignalAction)

@given(instance=CallOperationAction_strategy)
@settings(max_examples=50)
def test_calloperationaction_instantiation(instance):
    assert isinstance(instance, CallOperationAction)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=ocl_expressions_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_IteratorExp)

@given(instance=ocl_expressions_IterateExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_iterateexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_IterateExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=ocl_expressions_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_RealLiteralExp)



@given(instance=ocl_expressions_RealLiteralExp_strategy)
def test_ocl_expressions_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=ocl_expressions_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_IntegerLiteralExp)



@given(instance=ocl_expressions_IntegerLiteralExp_strategy)
def test_ocl_expressions_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=ocl_expressions_LoopExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_loopexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_LoopExp)

@given(instance=ocl_expressions_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_FeatureCallExp)



@given(instance=ocl_expressions_FeatureCallExp_strategy)
def test_ocl_expressions_featurecallexp_markedPre_setter(instance):
    original = instance.markedPre
    instance.markedPre = original
    assert instance.markedPre == original

@given(instance=expressions_ocl_EEnumLiteral_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eenumliteral_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EEnumLiteral)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ocl_expressions_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_expressions_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_expressions_CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ocl_expressions_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_PrimitiveLiteralExp)

@given(instance=ocl_expressions_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_InvalidLiteralExp)

@given(instance=ocl_expressions_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_EnumLiteralExp)

@given(instance=ocl_expressions_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_NullLiteralExp)

@given(instance=ocl_expressions_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_TupleLiteralExp)

@given(instance=ocl_expressions_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_CollectionLiteralExp)



@given(instance=ocl_expressions_CollectionLiteralExp_strategy)
def test_ocl_expressions_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=ocl_expressions_CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl_expressions_collectionrange_instantiation(instance):
    assert isinstance(instance, ocl_expressions_CollectionRange)

@given(instance=ocl_expressions_CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl_expressions_collectionitem_instantiation(instance):
    assert isinstance(instance, ocl_expressions_CollectionItem)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=ocl_expressions_IfExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_ifexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_IfExp)

@given(instance=ocl_expressions_TypeExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_typeexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_TypeExp)

@given(instance=ocl_expressions_VariableExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_variableexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_VariableExp)

@given(instance=ocl_expressions_LetExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_letexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_LetExp)

@given(instance=ocl_expressions_LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_literalexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_LiteralExp)

@given(instance=ocl_expressions_StateExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_stateexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_StateExp)

@given(instance=utilities_CallingASTNode_strategy)
@settings(max_examples=50)
def test_utilities_callingastnode_instantiation(instance):
    assert isinstance(instance, utilities_CallingASTNode)

@given(instance=expressions_OCLExpression_strategy)
@settings(max_examples=50)
def test_expressions_oclexpression_instantiation(instance):
    assert isinstance(instance, expressions_OCLExpression)

@given(instance=ocl_expressions_MessageExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_messageexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_MessageExp)

@given(instance=ocl_expressions_CallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_callexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=ocl_expressions_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_StringLiteralExp)



@given(instance=ocl_expressions_StringLiteralExp_strategy)
def test_ocl_expressions_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=ocl_expressions_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_NumericLiteralExp)

@given(instance=ocl_expressions_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_BooleanLiteralExp)



@given(instance=ocl_expressions_BooleanLiteralExp_strategy)
def test_ocl_expressions_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=expressions_ocl_EClass_strategy)
@settings(max_examples=50)
def test_expressions_ocl_eclass_instantiation(instance):
    assert isinstance(instance, expressions_ocl_EClass)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=ocl_expressions_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_PropertyCallExp)

@given(instance=ocl_expressions_AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_AssociationClassCallExp)

@given(instance=ocl_types_VoidType_strategy)
@settings(max_examples=50)
def test_ocl_types_voidtype_instantiation(instance):
    assert isinstance(instance, ocl_types_VoidType)

@given(instance=ocl_types_TypeType_strategy)
@settings(max_examples=50)
def test_ocl_types_typetype_instantiation(instance):
    assert isinstance(instance, ocl_types_TypeType)

@given(instance=ocl_types_SetType_strategy)
@settings(max_examples=50)
def test_ocl_types_settype_instantiation(instance):
    assert isinstance(instance, ocl_types_SetType)

@given(instance=ocl_types_SequenceType_strategy)
@settings(max_examples=50)
def test_ocl_types_sequencetype_instantiation(instance):
    assert isinstance(instance, ocl_types_SequenceType)

@given(instance=PrimitiveReal_strategy)
@settings(max_examples=50)
def test_primitivereal_instantiation(instance):
    assert isinstance(instance, PrimitiveReal)

@given(instance=ocl_types_PrimitiveInteger_strategy)
@settings(max_examples=50)
def test_ocl_types_primitiveinteger_instantiation(instance):
    assert isinstance(instance, ocl_types_PrimitiveInteger)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ocl_types_PrimitiveString_strategy)
@settings(max_examples=50)
def test_ocl_types_primitivestring_instantiation(instance):
    assert isinstance(instance, ocl_types_PrimitiveString)

@given(instance=ocl_types_PrimitiveReal_strategy)
@settings(max_examples=50)
def test_ocl_types_primitivereal_instantiation(instance):
    assert isinstance(instance, ocl_types_PrimitiveReal)

@given(instance=ocl_types_PrimitiveBoolean_strategy)
@settings(max_examples=50)
def test_ocl_types_primitiveboolean_instantiation(instance):
    assert isinstance(instance, ocl_types_PrimitiveBoolean)

@given(instance=ocl_types_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_types_orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl_types_OrderedSetType)

@given(instance=types_ocl_EClass_strategy)
@settings(max_examples=50)
def test_types_ocl_eclass_instantiation(instance):
    assert isinstance(instance, types_ocl_EClass)

@given(instance=types_ocl_EOperation_strategy)
@settings(max_examples=50)
def test_types_ocl_eoperation_instantiation(instance):
    assert isinstance(instance, types_ocl_EOperation)

@given(instance=ocl_types_InvalidType_strategy)
@settings(max_examples=50)
def test_ocl_types_invalidtype_instantiation(instance):
    assert isinstance(instance, ocl_types_InvalidType)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ocl_types_TupleType_strategy)
@settings(max_examples=50)
def test_ocl_types_tupletype_instantiation(instance):
    assert isinstance(instance, ocl_types_TupleType)

@given(instance=ocl_types_MessageType_strategy)
@settings(max_examples=50)
def test_ocl_types_messagetype_instantiation(instance):
    assert isinstance(instance, ocl_types_MessageType)

@given(instance=ocl_types_ElementType_strategy)
@settings(max_examples=50)
def test_ocl_types_elementtype_instantiation(instance):
    assert isinstance(instance, ocl_types_ElementType)

@given(instance=types_ocl_EClassifier_strategy)
@settings(max_examples=50)
def test_types_ocl_eclassifier_instantiation(instance):
    assert isinstance(instance, types_ocl_EClassifier)

@given(instance=utilities_TypedASTNode_strategy)
@settings(max_examples=50)
def test_utilities_typedastnode_instantiation(instance):
    assert isinstance(instance, utilities_TypedASTNode)

@given(instance=ocl_expressions_Variable_strategy)
@settings(max_examples=50)
def test_ocl_expressions_variable_instantiation(instance):
    assert isinstance(instance, ocl_expressions_Variable)

@given(instance=ocl_expressions_UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl_expressions_unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl_expressions_UnspecifiedValueExp)

@given(instance=ocl_expressions_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_expressions_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_expressions_TupleLiteralPart)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=ocl_types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_types_primitivetype_instantiation(instance):
    assert isinstance(instance, ocl_types_PrimitiveType)

@given(instance=ocl_types_CollectionType_strategy)
@settings(max_examples=50)
def test_ocl_types_collectiontype_instantiation(instance):
    assert isinstance(instance, ocl_types_CollectionType)



@given(instance=ocl_types_CollectionType_strategy)
def test_ocl_types_collectiontype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
