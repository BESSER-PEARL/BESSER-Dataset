import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ocl_ecore_VariableExp,
    ocl_ecore_Variable,
    ocl_ecore_UnspecifiedValueExp,
    ocl_ecore_TypeExp,
    ocl_ecore_TupleLiteralPart,
    ocl_ecore_TupleLiteralExp,
    ocl_ecore_StringLiteralExp,
    ocl_ecore_StateExp,
    ocl_ecore_RealLiteralExp,
    ocl_ecore_PropertyCallExp,
    ocl_ecore_LoopExp,
    ocl_ecore_LiteralExp,
    ocl_ecore_LetExp,
    ocl_ecore_IteratorExp,
    ocl_ecore_IterateExp,
    ocl_ecore_InvalidLiteralExp,
    ocl_ecore_UnlimitedNaturalLiteralExp,
    ocl_ecore_IntegerLiteralExp,
    ocl_ecore_IfExp,
    ocl_ecore_FeatureCallExp,
    ocl_ecore_EnumLiteralExp,
    ocl_ecore_PrimitiveLiteralExp,
    ocl_ecore_OperationCallExp,
    ocl_ecore_OCLExpression,
    ocl_ecore_NumericLiteralExp,
    ocl_ecore_NullLiteralExp,
    ocl_ecore_NavigationCallExp,
    ocl_ecore_MessageExp,
    ecore_ocl_EClass,
    ocl_ecore_SendSignalAction,
    ecore_ocl_EModelElement,
    ENamedElement,
    ocl_ecore_Constraint,
    ecore_ocl_EOperation,
    ocl_ecore_CallOperationAction,
    ocl_ecore_VoidType,
    ocl_ecore_TypeType,
    ocl_ecore_CollectionRange,
    ocl_ecore_CollectionLiteralPart,
    ocl_ecore_CollectionLiteralExp,
    ocl_ecore_CollectionItem,
    ocl_ecore_CallExp,
    ocl_ecore_BooleanLiteralExp,
    ocl_ecore_AssociationClassCallExp,
    ocl_ecore_ExpressionInOCL,
    ocl_ecore_MessageType,
    ocl_ecore_InvalidType,
    types_ElementType,
    EClass,
    ocl_ecore_ElementType,
    ocl_ecore_CollectionType,
    ocl_ecore_BagType,
    ocl_ecore_AnyType,
    ocl_ecore_TupleType,
    ocl_ecore_TemplateParameterType,
    ocl_ecore_SetType,
    ocl_ecore_SequenceType,
    ocl_ecore_PrimitiveType,
    ocl_ecore_OrderedSetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl_ecore_variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_VariableExp)


def test_ocl_ecore_variableexp_constructor_exists():
    assert callable(ocl_ecore_VariableExp.__init__)


def test_ocl_ecore_variableexp_constructor_args():
    sig = inspect.signature(ocl_ecore_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_variable_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_Variable)


def test_ocl_ecore_variable_constructor_exists():
    assert callable(ocl_ecore_Variable.__init__)


def test_ocl_ecore_variable_constructor_args():
    sig = inspect.signature(ocl_ecore_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_UnspecifiedValueExp)


def test_ocl_ecore_unspecifiedvalueexp_constructor_exists():
    assert callable(ocl_ecore_UnspecifiedValueExp.__init__)


def test_ocl_ecore_unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl_ecore_UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TypeExp)


def test_ocl_ecore_typeexp_constructor_exists():
    assert callable(ocl_ecore_TypeExp.__init__)


def test_ocl_ecore_typeexp_constructor_args():
    sig = inspect.signature(ocl_ecore_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TupleLiteralPart)


def test_ocl_ecore_tupleliteralpart_constructor_exists():
    assert callable(ocl_ecore_TupleLiteralPart.__init__)


def test_ocl_ecore_tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl_ecore_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TupleLiteralExp)


def test_ocl_ecore_tupleliteralexp_constructor_exists():
    assert callable(ocl_ecore_TupleLiteralExp.__init__)


def test_ocl_ecore_tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_StringLiteralExp)


def test_ocl_ecore_stringliteralexp_constructor_exists():
    assert callable(ocl_ecore_StringLiteralExp.__init__)


def test_ocl_ecore_stringliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_StateExp)


def test_ocl_ecore_stateexp_constructor_exists():
    assert callable(ocl_ecore_StateExp.__init__)


def test_ocl_ecore_stateexp_constructor_args():
    sig = inspect.signature(ocl_ecore_StateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_RealLiteralExp)


def test_ocl_ecore_realliteralexp_constructor_exists():
    assert callable(ocl_ecore_RealLiteralExp.__init__)


def test_ocl_ecore_realliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_PropertyCallExp)


def test_ocl_ecore_propertycallexp_constructor_exists():
    assert callable(ocl_ecore_PropertyCallExp.__init__)


def test_ocl_ecore_propertycallexp_constructor_args():
    sig = inspect.signature(ocl_ecore_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_LoopExp)


def test_ocl_ecore_loopexp_constructor_exists():
    assert callable(ocl_ecore_LoopExp.__init__)


def test_ocl_ecore_loopexp_constructor_args():
    sig = inspect.signature(ocl_ecore_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_LiteralExp)


def test_ocl_ecore_literalexp_constructor_exists():
    assert callable(ocl_ecore_LiteralExp.__init__)


def test_ocl_ecore_literalexp_constructor_args():
    sig = inspect.signature(ocl_ecore_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_letexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_LetExp)


def test_ocl_ecore_letexp_constructor_exists():
    assert callable(ocl_ecore_LetExp.__init__)


def test_ocl_ecore_letexp_constructor_args():
    sig = inspect.signature(ocl_ecore_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_IteratorExp)


def test_ocl_ecore_iteratorexp_constructor_exists():
    assert callable(ocl_ecore_IteratorExp.__init__)


def test_ocl_ecore_iteratorexp_constructor_args():
    sig = inspect.signature(ocl_ecore_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_IterateExp)


def test_ocl_ecore_iterateexp_constructor_exists():
    assert callable(ocl_ecore_IterateExp.__init__)


def test_ocl_ecore_iterateexp_constructor_args():
    sig = inspect.signature(ocl_ecore_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_InvalidLiteralExp)


def test_ocl_ecore_invalidliteralexp_constructor_exists():
    assert callable(ocl_ecore_InvalidLiteralExp.__init__)


def test_ocl_ecore_invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_UnlimitedNaturalLiteralExp)


def test_ocl_ecore_unlimitednaturalliteralexp_constructor_exists():
    assert callable(ocl_ecore_UnlimitedNaturalLiteralExp.__init__)


def test_ocl_ecore_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_IntegerLiteralExp)


def test_ocl_ecore_integerliteralexp_constructor_exists():
    assert callable(ocl_ecore_IntegerLiteralExp.__init__)


def test_ocl_ecore_integerliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_IfExp)


def test_ocl_ecore_ifexp_constructor_exists():
    assert callable(ocl_ecore_IfExp.__init__)


def test_ocl_ecore_ifexp_constructor_args():
    sig = inspect.signature(ocl_ecore_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_FeatureCallExp)


def test_ocl_ecore_featurecallexp_constructor_exists():
    assert callable(ocl_ecore_FeatureCallExp.__init__)


def test_ocl_ecore_featurecallexp_constructor_args():
    sig = inspect.signature(ocl_ecore_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_EnumLiteralExp)


def test_ocl_ecore_enumliteralexp_constructor_exists():
    assert callable(ocl_ecore_EnumLiteralExp.__init__)


def test_ocl_ecore_enumliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_PrimitiveLiteralExp)


def test_ocl_ecore_primitiveliteralexp_constructor_exists():
    assert callable(ocl_ecore_PrimitiveLiteralExp.__init__)


def test_ocl_ecore_primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_OperationCallExp)


def test_ocl_ecore_operationcallexp_constructor_exists():
    assert callable(ocl_ecore_OperationCallExp.__init__)


def test_ocl_ecore_operationcallexp_constructor_args():
    sig = inspect.signature(ocl_ecore_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_OCLExpression)


def test_ocl_ecore_oclexpression_constructor_exists():
    assert callable(ocl_ecore_OCLExpression.__init__)


def test_ocl_ecore_oclexpression_constructor_args():
    sig = inspect.signature(ocl_ecore_OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_NumericLiteralExp)


def test_ocl_ecore_numericliteralexp_constructor_exists():
    assert callable(ocl_ecore_NumericLiteralExp.__init__)


def test_ocl_ecore_numericliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_NullLiteralExp)


def test_ocl_ecore_nullliteralexp_constructor_exists():
    assert callable(ocl_ecore_NullLiteralExp.__init__)


def test_ocl_ecore_nullliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_NavigationCallExp)


def test_ocl_ecore_navigationcallexp_constructor_exists():
    assert callable(ocl_ecore_NavigationCallExp.__init__)


def test_ocl_ecore_navigationcallexp_constructor_args():
    sig = inspect.signature(ocl_ecore_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_MessageExp)


def test_ocl_ecore_messageexp_constructor_exists():
    assert callable(ocl_ecore_MessageExp.__init__)


def test_ocl_ecore_messageexp_constructor_args():
    sig = inspect.signature(ocl_ecore_MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ecore_ocl_eclass_is_not_abstract():
    assert not inspect.isabstract(ecore_ocl_EClass)


def test_ecore_ocl_eclass_constructor_exists():
    assert callable(ecore_ocl_EClass.__init__)


def test_ecore_ocl_eclass_constructor_args():
    sig = inspect.signature(ecore_ocl_EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_SendSignalAction)


def test_ocl_ecore_sendsignalaction_constructor_exists():
    assert callable(ocl_ecore_SendSignalAction.__init__)


def test_ocl_ecore_sendsignalaction_constructor_args():
    sig = inspect.signature(ocl_ecore_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_ecore_ocl_emodelelement_is_not_abstract():
    assert not inspect.isabstract(ecore_ocl_EModelElement)


def test_ecore_ocl_emodelelement_constructor_exists():
    assert callable(ecore_ocl_EModelElement.__init__)


def test_ecore_ocl_emodelelement_constructor_args():
    sig = inspect.signature(ecore_ocl_EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_constraint_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_Constraint)


def test_ocl_ecore_constraint_constructor_exists():
    assert callable(ocl_ecore_Constraint.__init__)


def test_ocl_ecore_constraint_constructor_args():
    sig = inspect.signature(ocl_ecore_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_ocl_ecore_constraint_has_stereotype():
    assert hasattr(ocl_ecore_Constraint, "stereotype")
    descriptor = None
    for klass in ocl_ecore_Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_ecore_ocl_eoperation_is_not_abstract():
    assert not inspect.isabstract(ecore_ocl_EOperation)


def test_ecore_ocl_eoperation_constructor_exists():
    assert callable(ecore_ocl_EOperation.__init__)


def test_ecore_ocl_eoperation_constructor_args():
    sig = inspect.signature(ecore_ocl_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CallOperationAction)


def test_ocl_ecore_calloperationaction_constructor_exists():
    assert callable(ocl_ecore_CallOperationAction.__init__)


def test_ocl_ecore_calloperationaction_constructor_args():
    sig = inspect.signature(ocl_ecore_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_VoidType)


def test_ocl_ecore_voidtype_constructor_exists():
    assert callable(ocl_ecore_VoidType.__init__)


def test_ocl_ecore_voidtype_constructor_args():
    sig = inspect.signature(ocl_ecore_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_typetype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TypeType)


def test_ocl_ecore_typetype_constructor_exists():
    assert callable(ocl_ecore_TypeType.__init__)


def test_ocl_ecore_typetype_constructor_args():
    sig = inspect.signature(ocl_ecore_TypeType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CollectionRange)


def test_ocl_ecore_collectionrange_constructor_exists():
    assert callable(ocl_ecore_CollectionRange.__init__)


def test_ocl_ecore_collectionrange_constructor_args():
    sig = inspect.signature(ocl_ecore_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CollectionLiteralPart)


def test_ocl_ecore_collectionliteralpart_constructor_exists():
    assert callable(ocl_ecore_CollectionLiteralPart.__init__)


def test_ocl_ecore_collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl_ecore_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CollectionLiteralExp)


def test_ocl_ecore_collectionliteralexp_constructor_exists():
    assert callable(ocl_ecore_CollectionLiteralExp.__init__)


def test_ocl_ecore_collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CollectionItem)


def test_ocl_ecore_collectionitem_constructor_exists():
    assert callable(ocl_ecore_CollectionItem.__init__)


def test_ocl_ecore_collectionitem_constructor_args():
    sig = inspect.signature(ocl_ecore_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_callexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CallExp)


def test_ocl_ecore_callexp_constructor_exists():
    assert callable(ocl_ecore_CallExp.__init__)


def test_ocl_ecore_callexp_constructor_args():
    sig = inspect.signature(ocl_ecore_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_BooleanLiteralExp)


def test_ocl_ecore_booleanliteralexp_constructor_exists():
    assert callable(ocl_ecore_BooleanLiteralExp.__init__)


def test_ocl_ecore_booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl_ecore_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_AssociationClassCallExp)


def test_ocl_ecore_associationclasscallexp_constructor_exists():
    assert callable(ocl_ecore_AssociationClassCallExp.__init__)


def test_ocl_ecore_associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl_ecore_AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_ExpressionInOCL)


def test_ocl_ecore_expressioninocl_constructor_exists():
    assert callable(ocl_ecore_ExpressionInOCL.__init__)


def test_ocl_ecore_expressioninocl_constructor_args():
    sig = inspect.signature(ocl_ecore_ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_MessageType)


def test_ocl_ecore_messagetype_constructor_exists():
    assert callable(ocl_ecore_MessageType.__init__)


def test_ocl_ecore_messagetype_constructor_args():
    sig = inspect.signature(ocl_ecore_MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_InvalidType)


def test_ocl_ecore_invalidtype_constructor_exists():
    assert callable(ocl_ecore_InvalidType.__init__)


def test_ocl_ecore_invalidtype_constructor_args():
    sig = inspect.signature(ocl_ecore_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_types_elementtype_is_not_abstract():
    assert not inspect.isabstract(types_ElementType)


def test_types_elementtype_constructor_exists():
    assert callable(types_ElementType.__init__)


def test_types_elementtype_constructor_args():
    sig = inspect.signature(types_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_ElementType)


def test_ocl_ecore_elementtype_constructor_exists():
    assert callable(ocl_ecore_ElementType.__init__)


def test_ocl_ecore_elementtype_constructor_args():
    sig = inspect.signature(ocl_ecore_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_CollectionType)


def test_ocl_ecore_collectiontype_constructor_exists():
    assert callable(ocl_ecore_CollectionType.__init__)


def test_ocl_ecore_collectiontype_constructor_args():
    sig = inspect.signature(ocl_ecore_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_BagType)


def test_ocl_ecore_bagtype_constructor_exists():
    assert callable(ocl_ecore_BagType.__init__)


def test_ocl_ecore_bagtype_constructor_args():
    sig = inspect.signature(ocl_ecore_BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_anytype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_AnyType)


def test_ocl_ecore_anytype_constructor_exists():
    assert callable(ocl_ecore_AnyType.__init__)


def test_ocl_ecore_anytype_constructor_args():
    sig = inspect.signature(ocl_ecore_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TupleType)


def test_ocl_ecore_tupletype_constructor_exists():
    assert callable(ocl_ecore_TupleType.__init__)


def test_ocl_ecore_tupletype_constructor_args():
    sig = inspect.signature(ocl_ecore_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_TemplateParameterType)


def test_ocl_ecore_templateparametertype_constructor_exists():
    assert callable(ocl_ecore_TemplateParameterType.__init__)


def test_ocl_ecore_templateparametertype_constructor_args():
    sig = inspect.signature(ocl_ecore_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_settype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_SetType)


def test_ocl_ecore_settype_constructor_exists():
    assert callable(ocl_ecore_SetType.__init__)


def test_ocl_ecore_settype_constructor_args():
    sig = inspect.signature(ocl_ecore_SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_SequenceType)


def test_ocl_ecore_sequencetype_constructor_exists():
    assert callable(ocl_ecore_SequenceType.__init__)


def test_ocl_ecore_sequencetype_constructor_args():
    sig = inspect.signature(ocl_ecore_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_PrimitiveType)


def test_ocl_ecore_primitivetype_constructor_exists():
    assert callable(ocl_ecore_PrimitiveType.__init__)


def test_ocl_ecore_primitivetype_constructor_args():
    sig = inspect.signature(ocl_ecore_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ecore_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl_ecore_OrderedSetType)


def test_ocl_ecore_orderedsettype_constructor_exists():
    assert callable(ocl_ecore_OrderedSetType.__init__)


def test_ocl_ecore_orderedsettype_constructor_args():
    sig = inspect.signature(ocl_ecore_OrderedSetType.__init__)
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
ocl_ecore_VariableExp_strategy = st.builds(
    ocl_ecore_VariableExp,
)
ocl_ecore_Variable_strategy = st.builds(
    ocl_ecore_Variable,
)
ocl_ecore_UnspecifiedValueExp_strategy = st.builds(
    ocl_ecore_UnspecifiedValueExp,
)
ocl_ecore_TypeExp_strategy = st.builds(
    ocl_ecore_TypeExp,
)
ocl_ecore_TupleLiteralPart_strategy = st.builds(
    ocl_ecore_TupleLiteralPart,
)
ocl_ecore_TupleLiteralExp_strategy = st.builds(
    ocl_ecore_TupleLiteralExp,
)
ocl_ecore_StringLiteralExp_strategy = st.builds(
    ocl_ecore_StringLiteralExp,
)
ocl_ecore_StateExp_strategy = st.builds(
    ocl_ecore_StateExp,
)
ocl_ecore_RealLiteralExp_strategy = st.builds(
    ocl_ecore_RealLiteralExp,
)
ocl_ecore_PropertyCallExp_strategy = st.builds(
    ocl_ecore_PropertyCallExp,
)
ocl_ecore_LoopExp_strategy = st.builds(
    ocl_ecore_LoopExp,
)
ocl_ecore_LiteralExp_strategy = st.builds(
    ocl_ecore_LiteralExp,
)
ocl_ecore_LetExp_strategy = st.builds(
    ocl_ecore_LetExp,
)
ocl_ecore_IteratorExp_strategy = st.builds(
    ocl_ecore_IteratorExp,
)
ocl_ecore_IterateExp_strategy = st.builds(
    ocl_ecore_IterateExp,
)
ocl_ecore_InvalidLiteralExp_strategy = st.builds(
    ocl_ecore_InvalidLiteralExp,
)
ocl_ecore_UnlimitedNaturalLiteralExp_strategy = st.builds(
    ocl_ecore_UnlimitedNaturalLiteralExp,
)
ocl_ecore_IntegerLiteralExp_strategy = st.builds(
    ocl_ecore_IntegerLiteralExp,
)
ocl_ecore_IfExp_strategy = st.builds(
    ocl_ecore_IfExp,
)
ocl_ecore_FeatureCallExp_strategy = st.builds(
    ocl_ecore_FeatureCallExp,
)
ocl_ecore_EnumLiteralExp_strategy = st.builds(
    ocl_ecore_EnumLiteralExp,
)
ocl_ecore_PrimitiveLiteralExp_strategy = st.builds(
    ocl_ecore_PrimitiveLiteralExp,
)
ocl_ecore_OperationCallExp_strategy = st.builds(
    ocl_ecore_OperationCallExp,
)
ocl_ecore_OCLExpression_strategy = st.builds(
    ocl_ecore_OCLExpression,
)
ocl_ecore_NumericLiteralExp_strategy = st.builds(
    ocl_ecore_NumericLiteralExp,
)
ocl_ecore_NullLiteralExp_strategy = st.builds(
    ocl_ecore_NullLiteralExp,
)
ocl_ecore_NavigationCallExp_strategy = st.builds(
    ocl_ecore_NavigationCallExp,
)
ocl_ecore_MessageExp_strategy = st.builds(
    ocl_ecore_MessageExp,
)
ecore_ocl_EClass_strategy = st.builds(
    ecore_ocl_EClass,
)
ocl_ecore_SendSignalAction_strategy = st.builds(
    ocl_ecore_SendSignalAction,
)
ecore_ocl_EModelElement_strategy = st.builds(
    ecore_ocl_EModelElement,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ocl_ecore_Constraint_strategy = st.builds(
    ocl_ecore_Constraint,
    stereotype=
        safe_text
)
ecore_ocl_EOperation_strategy = st.builds(
    ecore_ocl_EOperation,
)
ocl_ecore_CallOperationAction_strategy = st.builds(
    ocl_ecore_CallOperationAction,
)
ocl_ecore_VoidType_strategy = st.builds(
    ocl_ecore_VoidType,
)
ocl_ecore_TypeType_strategy = st.builds(
    ocl_ecore_TypeType,
)
ocl_ecore_CollectionRange_strategy = st.builds(
    ocl_ecore_CollectionRange,
)
ocl_ecore_CollectionLiteralPart_strategy = st.builds(
    ocl_ecore_CollectionLiteralPart,
)
ocl_ecore_CollectionLiteralExp_strategy = st.builds(
    ocl_ecore_CollectionLiteralExp,
)
ocl_ecore_CollectionItem_strategy = st.builds(
    ocl_ecore_CollectionItem,
)
ocl_ecore_CallExp_strategy = st.builds(
    ocl_ecore_CallExp,
)
ocl_ecore_BooleanLiteralExp_strategy = st.builds(
    ocl_ecore_BooleanLiteralExp,
)
ocl_ecore_AssociationClassCallExp_strategy = st.builds(
    ocl_ecore_AssociationClassCallExp,
)
ocl_ecore_ExpressionInOCL_strategy = st.builds(
    ocl_ecore_ExpressionInOCL,
)
ocl_ecore_MessageType_strategy = st.builds(
    ocl_ecore_MessageType,
)
ocl_ecore_InvalidType_strategy = st.builds(
    ocl_ecore_InvalidType,
)
types_ElementType_strategy = st.builds(
    types_ElementType,
)
EClass_strategy = st.builds(
    EClass,
)
ocl_ecore_ElementType_strategy = st.builds(
    ocl_ecore_ElementType,
)
ocl_ecore_CollectionType_strategy = st.builds(
    ocl_ecore_CollectionType,
)
ocl_ecore_BagType_strategy = st.builds(
    ocl_ecore_BagType,
)
ocl_ecore_AnyType_strategy = st.builds(
    ocl_ecore_AnyType,
)
ocl_ecore_TupleType_strategy = st.builds(
    ocl_ecore_TupleType,
)
ocl_ecore_TemplateParameterType_strategy = st.builds(
    ocl_ecore_TemplateParameterType,
)
ocl_ecore_SetType_strategy = st.builds(
    ocl_ecore_SetType,
)
ocl_ecore_SequenceType_strategy = st.builds(
    ocl_ecore_SequenceType,
)
ocl_ecore_PrimitiveType_strategy = st.builds(
    ocl_ecore_PrimitiveType,
)
ocl_ecore_OrderedSetType_strategy = st.builds(
    ocl_ecore_OrderedSetType,
)

@given(instance=ocl_ecore_VariableExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_variableexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_VariableExp)

@given(instance=ocl_ecore_Variable_strategy)
@settings(max_examples=50)
def test_ocl_ecore_variable_instantiation(instance):
    assert isinstance(instance, ocl_ecore_Variable)

@given(instance=ocl_ecore_UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_UnspecifiedValueExp)

@given(instance=ocl_ecore_TypeExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_typeexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TypeExp)

@given(instance=ocl_ecore_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_ecore_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TupleLiteralPart)

@given(instance=ocl_ecore_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TupleLiteralExp)

@given(instance=ocl_ecore_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_StringLiteralExp)

@given(instance=ocl_ecore_StateExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_stateexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_StateExp)

@given(instance=ocl_ecore_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_RealLiteralExp)

@given(instance=ocl_ecore_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_PropertyCallExp)

@given(instance=ocl_ecore_LoopExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_loopexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_LoopExp)

@given(instance=ocl_ecore_LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_literalexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_LiteralExp)

@given(instance=ocl_ecore_LetExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_letexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_LetExp)

@given(instance=ocl_ecore_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_IteratorExp)

@given(instance=ocl_ecore_IterateExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_iterateexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_IterateExp)

@given(instance=ocl_ecore_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_InvalidLiteralExp)

@given(instance=ocl_ecore_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_UnlimitedNaturalLiteralExp)

@given(instance=ocl_ecore_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_IntegerLiteralExp)

@given(instance=ocl_ecore_IfExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_ifexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_IfExp)

@given(instance=ocl_ecore_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_FeatureCallExp)

@given(instance=ocl_ecore_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_EnumLiteralExp)

@given(instance=ocl_ecore_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_PrimitiveLiteralExp)

@given(instance=ocl_ecore_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_OperationCallExp)

@given(instance=ocl_ecore_OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl_ecore_oclexpression_instantiation(instance):
    assert isinstance(instance, ocl_ecore_OCLExpression)

@given(instance=ocl_ecore_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_NumericLiteralExp)

@given(instance=ocl_ecore_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_NullLiteralExp)

@given(instance=ocl_ecore_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_NavigationCallExp)

@given(instance=ocl_ecore_MessageExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_messageexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_MessageExp)

@given(instance=ecore_ocl_EClass_strategy)
@settings(max_examples=50)
def test_ecore_ocl_eclass_instantiation(instance):
    assert isinstance(instance, ecore_ocl_EClass)

@given(instance=ocl_ecore_SendSignalAction_strategy)
@settings(max_examples=50)
def test_ocl_ecore_sendsignalaction_instantiation(instance):
    assert isinstance(instance, ocl_ecore_SendSignalAction)

@given(instance=ecore_ocl_EModelElement_strategy)
@settings(max_examples=50)
def test_ecore_ocl_emodelelement_instantiation(instance):
    assert isinstance(instance, ecore_ocl_EModelElement)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ocl_ecore_Constraint_strategy)
@settings(max_examples=50)
def test_ocl_ecore_constraint_instantiation(instance):
    assert isinstance(instance, ocl_ecore_Constraint)



@given(instance=ocl_ecore_Constraint_strategy)
def test_ocl_ecore_constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=ecore_ocl_EOperation_strategy)
@settings(max_examples=50)
def test_ecore_ocl_eoperation_instantiation(instance):
    assert isinstance(instance, ecore_ocl_EOperation)

@given(instance=ocl_ecore_CallOperationAction_strategy)
@settings(max_examples=50)
def test_ocl_ecore_calloperationaction_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CallOperationAction)

@given(instance=ocl_ecore_VoidType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_voidtype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_VoidType)

@given(instance=ocl_ecore_TypeType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_typetype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TypeType)

@given(instance=ocl_ecore_CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl_ecore_collectionrange_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CollectionRange)

@given(instance=ocl_ecore_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_ecore_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CollectionLiteralPart)

@given(instance=ocl_ecore_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CollectionLiteralExp)

@given(instance=ocl_ecore_CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl_ecore_collectionitem_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CollectionItem)

@given(instance=ocl_ecore_CallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_callexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CallExp)

@given(instance=ocl_ecore_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_BooleanLiteralExp)

@given(instance=ocl_ecore_AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl_ecore_associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl_ecore_AssociationClassCallExp)

@given(instance=ocl_ecore_ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_ocl_ecore_expressioninocl_instantiation(instance):
    assert isinstance(instance, ocl_ecore_ExpressionInOCL)

@given(instance=ocl_ecore_MessageType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_messagetype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_MessageType)

@given(instance=ocl_ecore_InvalidType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_invalidtype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_InvalidType)

@given(instance=types_ElementType_strategy)
@settings(max_examples=50)
def test_types_elementtype_instantiation(instance):
    assert isinstance(instance, types_ElementType)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ocl_ecore_ElementType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_elementtype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_ElementType)

@given(instance=ocl_ecore_CollectionType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_collectiontype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_CollectionType)

@given(instance=ocl_ecore_BagType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_bagtype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_BagType)

@given(instance=ocl_ecore_AnyType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_anytype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_AnyType)

@given(instance=ocl_ecore_TupleType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_tupletype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TupleType)

@given(instance=ocl_ecore_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_templateparametertype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_TemplateParameterType)

@given(instance=ocl_ecore_SetType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_settype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_SetType)

@given(instance=ocl_ecore_SequenceType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_sequencetype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_SequenceType)

@given(instance=ocl_ecore_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_primitivetype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_PrimitiveType)

@given(instance=ocl_ecore_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_ecore_orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl_ecore_OrderedSetType)
