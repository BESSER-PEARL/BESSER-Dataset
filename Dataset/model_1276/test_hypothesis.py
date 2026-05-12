import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ocl_uml_TemplateParameterType,
    ocl_uml_VariableExp,
    ocl_uml_Variable,
    ocl_uml_UnspecifiedValueExp,
    ocl_uml_TypeExp,
    ocl_uml_TupleLiteralPart,
    ocl_uml_UnlimitedNaturalLiteralExp,
    ocl_uml_NumericLiteralExp,
    ocl_uml_TupleLiteralExp,
    ocl_uml_StringLiteralExp,
    ocl_uml_StateExp,
    ocl_uml_RealLiteralExp,
    ocl_uml_PropertyCallExp,
    ocl_uml_OperationCallExp,
    ocl_uml_NullLiteralExp,
    ocl_uml_MessageExp,
    ocl_uml_LetExp,
    ocl_uml_IteratorExp,
    ocl_uml_LoopExp,
    ocl_uml_IterateExp,
    ocl_uml_InvalidLiteralExp,
    ocl_uml_NavigationCallExp,
    ocl_uml_AssociationClassCallExp,
    ocl_uml_ExpressionInOCL,
    ocl_uml_SequenceType,
    ocl_uml_IntegerLiteralExp,
    ocl_uml_IfExp,
    ocl_uml_EnumLiteralExp,
    ocl_uml_CollectionRange,
    ocl_uml_CollectionLiteralExp,
    ocl_uml_CollectionLiteralPart,
    ocl_uml_CollectionItem,
    ocl_uml_LiteralExp,
    ocl_uml_PrimitiveLiteralExp,
    ocl_uml_BooleanLiteralExp,
    ocl_uml_OCLExpression,
    ocl_uml_CallExp,
    ocl_uml_FeatureCallExp,
    ocl_uml_InvalidType,
    ocl_uml_VoidType,
    uml_ocl_Operation,
    ocl_uml_OrderedSetType,
    ocl_uml_SetType,
    ocl_uml_BagType,
    ocl_uml_TupleType,
    ocl_uml_CollectionType,
    ocl_uml_PrimitiveType,
    uml_ocl_Property,
    ocl_uml_MessageType,
    ocl_uml_TypeType,
    types_ElementType,
    Classifier,
    ocl_uml_ElementType,
    ocl_uml_AnyType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl_uml_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TemplateParameterType)


def test_ocl_uml_templateparametertype_constructor_exists():
    assert callable(ocl_uml_TemplateParameterType.__init__)


def test_ocl_uml_templateparametertype_constructor_args():
    sig = inspect.signature(ocl_uml_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_VariableExp)


def test_ocl_uml_variableexp_constructor_exists():
    assert callable(ocl_uml_VariableExp.__init__)


def test_ocl_uml_variableexp_constructor_args():
    sig = inspect.signature(ocl_uml_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_variable_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_Variable)


def test_ocl_uml_variable_constructor_exists():
    assert callable(ocl_uml_Variable.__init__)


def test_ocl_uml_variable_constructor_args():
    sig = inspect.signature(ocl_uml_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_UnspecifiedValueExp)


def test_ocl_uml_unspecifiedvalueexp_constructor_exists():
    assert callable(ocl_uml_UnspecifiedValueExp.__init__)


def test_ocl_uml_unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl_uml_UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TypeExp)


def test_ocl_uml_typeexp_constructor_exists():
    assert callable(ocl_uml_TypeExp.__init__)


def test_ocl_uml_typeexp_constructor_args():
    sig = inspect.signature(ocl_uml_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TupleLiteralPart)


def test_ocl_uml_tupleliteralpart_constructor_exists():
    assert callable(ocl_uml_TupleLiteralPart.__init__)


def test_ocl_uml_tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl_uml_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_UnlimitedNaturalLiteralExp)


def test_ocl_uml_unlimitednaturalliteralexp_constructor_exists():
    assert callable(ocl_uml_UnlimitedNaturalLiteralExp.__init__)


def test_ocl_uml_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_NumericLiteralExp)


def test_ocl_uml_numericliteralexp_constructor_exists():
    assert callable(ocl_uml_NumericLiteralExp.__init__)


def test_ocl_uml_numericliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TupleLiteralExp)


def test_ocl_uml_tupleliteralexp_constructor_exists():
    assert callable(ocl_uml_TupleLiteralExp.__init__)


def test_ocl_uml_tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_StringLiteralExp)


def test_ocl_uml_stringliteralexp_constructor_exists():
    assert callable(ocl_uml_StringLiteralExp.__init__)


def test_ocl_uml_stringliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_StateExp)


def test_ocl_uml_stateexp_constructor_exists():
    assert callable(ocl_uml_StateExp.__init__)


def test_ocl_uml_stateexp_constructor_args():
    sig = inspect.signature(ocl_uml_StateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_RealLiteralExp)


def test_ocl_uml_realliteralexp_constructor_exists():
    assert callable(ocl_uml_RealLiteralExp.__init__)


def test_ocl_uml_realliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_PropertyCallExp)


def test_ocl_uml_propertycallexp_constructor_exists():
    assert callable(ocl_uml_PropertyCallExp.__init__)


def test_ocl_uml_propertycallexp_constructor_args():
    sig = inspect.signature(ocl_uml_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_OperationCallExp)


def test_ocl_uml_operationcallexp_constructor_exists():
    assert callable(ocl_uml_OperationCallExp.__init__)


def test_ocl_uml_operationcallexp_constructor_args():
    sig = inspect.signature(ocl_uml_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_NullLiteralExp)


def test_ocl_uml_nullliteralexp_constructor_exists():
    assert callable(ocl_uml_NullLiteralExp.__init__)


def test_ocl_uml_nullliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_MessageExp)


def test_ocl_uml_messageexp_constructor_exists():
    assert callable(ocl_uml_MessageExp.__init__)


def test_ocl_uml_messageexp_constructor_args():
    sig = inspect.signature(ocl_uml_MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_letexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_LetExp)


def test_ocl_uml_letexp_constructor_exists():
    assert callable(ocl_uml_LetExp.__init__)


def test_ocl_uml_letexp_constructor_args():
    sig = inspect.signature(ocl_uml_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_IteratorExp)


def test_ocl_uml_iteratorexp_constructor_exists():
    assert callable(ocl_uml_IteratorExp.__init__)


def test_ocl_uml_iteratorexp_constructor_args():
    sig = inspect.signature(ocl_uml_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_LoopExp)


def test_ocl_uml_loopexp_constructor_exists():
    assert callable(ocl_uml_LoopExp.__init__)


def test_ocl_uml_loopexp_constructor_args():
    sig = inspect.signature(ocl_uml_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_IterateExp)


def test_ocl_uml_iterateexp_constructor_exists():
    assert callable(ocl_uml_IterateExp.__init__)


def test_ocl_uml_iterateexp_constructor_args():
    sig = inspect.signature(ocl_uml_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_InvalidLiteralExp)


def test_ocl_uml_invalidliteralexp_constructor_exists():
    assert callable(ocl_uml_InvalidLiteralExp.__init__)


def test_ocl_uml_invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_NavigationCallExp)


def test_ocl_uml_navigationcallexp_constructor_exists():
    assert callable(ocl_uml_NavigationCallExp.__init__)


def test_ocl_uml_navigationcallexp_constructor_args():
    sig = inspect.signature(ocl_uml_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_AssociationClassCallExp)


def test_ocl_uml_associationclasscallexp_constructor_exists():
    assert callable(ocl_uml_AssociationClassCallExp.__init__)


def test_ocl_uml_associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl_uml_AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_ExpressionInOCL)


def test_ocl_uml_expressioninocl_constructor_exists():
    assert callable(ocl_uml_ExpressionInOCL.__init__)


def test_ocl_uml_expressioninocl_constructor_args():
    sig = inspect.signature(ocl_uml_ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_SequenceType)


def test_ocl_uml_sequencetype_constructor_exists():
    assert callable(ocl_uml_SequenceType.__init__)


def test_ocl_uml_sequencetype_constructor_args():
    sig = inspect.signature(ocl_uml_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_IntegerLiteralExp)


def test_ocl_uml_integerliteralexp_constructor_exists():
    assert callable(ocl_uml_IntegerLiteralExp.__init__)


def test_ocl_uml_integerliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_IfExp)


def test_ocl_uml_ifexp_constructor_exists():
    assert callable(ocl_uml_IfExp.__init__)


def test_ocl_uml_ifexp_constructor_args():
    sig = inspect.signature(ocl_uml_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_EnumLiteralExp)


def test_ocl_uml_enumliteralexp_constructor_exists():
    assert callable(ocl_uml_EnumLiteralExp.__init__)


def test_ocl_uml_enumliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CollectionRange)


def test_ocl_uml_collectionrange_constructor_exists():
    assert callable(ocl_uml_CollectionRange.__init__)


def test_ocl_uml_collectionrange_constructor_args():
    sig = inspect.signature(ocl_uml_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CollectionLiteralExp)


def test_ocl_uml_collectionliteralexp_constructor_exists():
    assert callable(ocl_uml_CollectionLiteralExp.__init__)


def test_ocl_uml_collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CollectionLiteralPart)


def test_ocl_uml_collectionliteralpart_constructor_exists():
    assert callable(ocl_uml_CollectionLiteralPart.__init__)


def test_ocl_uml_collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl_uml_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CollectionItem)


def test_ocl_uml_collectionitem_constructor_exists():
    assert callable(ocl_uml_CollectionItem.__init__)


def test_ocl_uml_collectionitem_constructor_args():
    sig = inspect.signature(ocl_uml_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_LiteralExp)


def test_ocl_uml_literalexp_constructor_exists():
    assert callable(ocl_uml_LiteralExp.__init__)


def test_ocl_uml_literalexp_constructor_args():
    sig = inspect.signature(ocl_uml_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_PrimitiveLiteralExp)


def test_ocl_uml_primitiveliteralexp_constructor_exists():
    assert callable(ocl_uml_PrimitiveLiteralExp.__init__)


def test_ocl_uml_primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_BooleanLiteralExp)


def test_ocl_uml_booleanliteralexp_constructor_exists():
    assert callable(ocl_uml_BooleanLiteralExp.__init__)


def test_ocl_uml_booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl_uml_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_OCLExpression)


def test_ocl_uml_oclexpression_constructor_exists():
    assert callable(ocl_uml_OCLExpression.__init__)


def test_ocl_uml_oclexpression_constructor_args():
    sig = inspect.signature(ocl_uml_OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_callexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CallExp)


def test_ocl_uml_callexp_constructor_exists():
    assert callable(ocl_uml_CallExp.__init__)


def test_ocl_uml_callexp_constructor_args():
    sig = inspect.signature(ocl_uml_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_FeatureCallExp)


def test_ocl_uml_featurecallexp_constructor_exists():
    assert callable(ocl_uml_FeatureCallExp.__init__)


def test_ocl_uml_featurecallexp_constructor_args():
    sig = inspect.signature(ocl_uml_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_InvalidType)


def test_ocl_uml_invalidtype_constructor_exists():
    assert callable(ocl_uml_InvalidType.__init__)


def test_ocl_uml_invalidtype_constructor_args():
    sig = inspect.signature(ocl_uml_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_VoidType)


def test_ocl_uml_voidtype_constructor_exists():
    assert callable(ocl_uml_VoidType.__init__)


def test_ocl_uml_voidtype_constructor_args():
    sig = inspect.signature(ocl_uml_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_uml_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_Operation)


def test_uml_ocl_operation_constructor_exists():
    assert callable(uml_ocl_Operation.__init__)


def test_uml_ocl_operation_constructor_args():
    sig = inspect.signature(uml_ocl_Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_OrderedSetType)


def test_ocl_uml_orderedsettype_constructor_exists():
    assert callable(ocl_uml_OrderedSetType.__init__)


def test_ocl_uml_orderedsettype_constructor_args():
    sig = inspect.signature(ocl_uml_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_settype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_SetType)


def test_ocl_uml_settype_constructor_exists():
    assert callable(ocl_uml_SetType.__init__)


def test_ocl_uml_settype_constructor_args():
    sig = inspect.signature(ocl_uml_SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_BagType)


def test_ocl_uml_bagtype_constructor_exists():
    assert callable(ocl_uml_BagType.__init__)


def test_ocl_uml_bagtype_constructor_args():
    sig = inspect.signature(ocl_uml_BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TupleType)


def test_ocl_uml_tupletype_constructor_exists():
    assert callable(ocl_uml_TupleType.__init__)


def test_ocl_uml_tupletype_constructor_args():
    sig = inspect.signature(ocl_uml_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_CollectionType)


def test_ocl_uml_collectiontype_constructor_exists():
    assert callable(ocl_uml_CollectionType.__init__)


def test_ocl_uml_collectiontype_constructor_args():
    sig = inspect.signature(ocl_uml_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_PrimitiveType)


def test_ocl_uml_primitivetype_constructor_exists():
    assert callable(ocl_uml_PrimitiveType.__init__)


def test_ocl_uml_primitivetype_constructor_args():
    sig = inspect.signature(ocl_uml_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml_ocl_property_is_not_abstract():
    assert not inspect.isabstract(uml_ocl_Property)


def test_uml_ocl_property_constructor_exists():
    assert callable(uml_ocl_Property.__init__)


def test_uml_ocl_property_constructor_args():
    sig = inspect.signature(uml_ocl_Property.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_MessageType)


def test_ocl_uml_messagetype_constructor_exists():
    assert callable(ocl_uml_MessageType.__init__)


def test_ocl_uml_messagetype_constructor_args():
    sig = inspect.signature(ocl_uml_MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_typetype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_TypeType)


def test_ocl_uml_typetype_constructor_exists():
    assert callable(ocl_uml_TypeType.__init__)


def test_ocl_uml_typetype_constructor_args():
    sig = inspect.signature(ocl_uml_TypeType.__init__)
    params = list(sig.parameters.keys())



def test_types_elementtype_is_not_abstract():
    assert not inspect.isabstract(types_ElementType)


def test_types_elementtype_constructor_exists():
    assert callable(types_ElementType.__init__)


def test_types_elementtype_constructor_args():
    sig = inspect.signature(types_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_ElementType)


def test_ocl_uml_elementtype_constructor_exists():
    assert callable(ocl_uml_ElementType.__init__)


def test_ocl_uml_elementtype_constructor_args():
    sig = inspect.signature(ocl_uml_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uml_anytype_is_not_abstract():
    assert not inspect.isabstract(ocl_uml_AnyType)


def test_ocl_uml_anytype_constructor_exists():
    assert callable(ocl_uml_AnyType.__init__)


def test_ocl_uml_anytype_constructor_args():
    sig = inspect.signature(ocl_uml_AnyType.__init__)
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
ocl_uml_TemplateParameterType_strategy = st.builds(
    ocl_uml_TemplateParameterType,
)
ocl_uml_VariableExp_strategy = st.builds(
    ocl_uml_VariableExp,
)
ocl_uml_Variable_strategy = st.builds(
    ocl_uml_Variable,
)
ocl_uml_UnspecifiedValueExp_strategy = st.builds(
    ocl_uml_UnspecifiedValueExp,
)
ocl_uml_TypeExp_strategy = st.builds(
    ocl_uml_TypeExp,
)
ocl_uml_TupleLiteralPart_strategy = st.builds(
    ocl_uml_TupleLiteralPart,
)
ocl_uml_UnlimitedNaturalLiteralExp_strategy = st.builds(
    ocl_uml_UnlimitedNaturalLiteralExp,
)
ocl_uml_NumericLiteralExp_strategy = st.builds(
    ocl_uml_NumericLiteralExp,
)
ocl_uml_TupleLiteralExp_strategy = st.builds(
    ocl_uml_TupleLiteralExp,
)
ocl_uml_StringLiteralExp_strategy = st.builds(
    ocl_uml_StringLiteralExp,
)
ocl_uml_StateExp_strategy = st.builds(
    ocl_uml_StateExp,
)
ocl_uml_RealLiteralExp_strategy = st.builds(
    ocl_uml_RealLiteralExp,
)
ocl_uml_PropertyCallExp_strategy = st.builds(
    ocl_uml_PropertyCallExp,
)
ocl_uml_OperationCallExp_strategy = st.builds(
    ocl_uml_OperationCallExp,
)
ocl_uml_NullLiteralExp_strategy = st.builds(
    ocl_uml_NullLiteralExp,
)
ocl_uml_MessageExp_strategy = st.builds(
    ocl_uml_MessageExp,
)
ocl_uml_LetExp_strategy = st.builds(
    ocl_uml_LetExp,
)
ocl_uml_IteratorExp_strategy = st.builds(
    ocl_uml_IteratorExp,
)
ocl_uml_LoopExp_strategy = st.builds(
    ocl_uml_LoopExp,
)
ocl_uml_IterateExp_strategy = st.builds(
    ocl_uml_IterateExp,
)
ocl_uml_InvalidLiteralExp_strategy = st.builds(
    ocl_uml_InvalidLiteralExp,
)
ocl_uml_NavigationCallExp_strategy = st.builds(
    ocl_uml_NavigationCallExp,
)
ocl_uml_AssociationClassCallExp_strategy = st.builds(
    ocl_uml_AssociationClassCallExp,
)
ocl_uml_ExpressionInOCL_strategy = st.builds(
    ocl_uml_ExpressionInOCL,
)
ocl_uml_SequenceType_strategy = st.builds(
    ocl_uml_SequenceType,
)
ocl_uml_IntegerLiteralExp_strategy = st.builds(
    ocl_uml_IntegerLiteralExp,
)
ocl_uml_IfExp_strategy = st.builds(
    ocl_uml_IfExp,
)
ocl_uml_EnumLiteralExp_strategy = st.builds(
    ocl_uml_EnumLiteralExp,
)
ocl_uml_CollectionRange_strategy = st.builds(
    ocl_uml_CollectionRange,
)
ocl_uml_CollectionLiteralExp_strategy = st.builds(
    ocl_uml_CollectionLiteralExp,
)
ocl_uml_CollectionLiteralPart_strategy = st.builds(
    ocl_uml_CollectionLiteralPart,
)
ocl_uml_CollectionItem_strategy = st.builds(
    ocl_uml_CollectionItem,
)
ocl_uml_LiteralExp_strategy = st.builds(
    ocl_uml_LiteralExp,
)
ocl_uml_PrimitiveLiteralExp_strategy = st.builds(
    ocl_uml_PrimitiveLiteralExp,
)
ocl_uml_BooleanLiteralExp_strategy = st.builds(
    ocl_uml_BooleanLiteralExp,
)
ocl_uml_OCLExpression_strategy = st.builds(
    ocl_uml_OCLExpression,
)
ocl_uml_CallExp_strategy = st.builds(
    ocl_uml_CallExp,
)
ocl_uml_FeatureCallExp_strategy = st.builds(
    ocl_uml_FeatureCallExp,
)
ocl_uml_InvalidType_strategy = st.builds(
    ocl_uml_InvalidType,
)
ocl_uml_VoidType_strategy = st.builds(
    ocl_uml_VoidType,
)
uml_ocl_Operation_strategy = st.builds(
    uml_ocl_Operation,
)
ocl_uml_OrderedSetType_strategy = st.builds(
    ocl_uml_OrderedSetType,
)
ocl_uml_SetType_strategy = st.builds(
    ocl_uml_SetType,
)
ocl_uml_BagType_strategy = st.builds(
    ocl_uml_BagType,
)
ocl_uml_TupleType_strategy = st.builds(
    ocl_uml_TupleType,
)
ocl_uml_CollectionType_strategy = st.builds(
    ocl_uml_CollectionType,
)
ocl_uml_PrimitiveType_strategy = st.builds(
    ocl_uml_PrimitiveType,
)
uml_ocl_Property_strategy = st.builds(
    uml_ocl_Property,
)
ocl_uml_MessageType_strategy = st.builds(
    ocl_uml_MessageType,
)
ocl_uml_TypeType_strategy = st.builds(
    ocl_uml_TypeType,
)
types_ElementType_strategy = st.builds(
    types_ElementType,
)
Classifier_strategy = st.builds(
    Classifier,
)
ocl_uml_ElementType_strategy = st.builds(
    ocl_uml_ElementType,
)
ocl_uml_AnyType_strategy = st.builds(
    ocl_uml_AnyType,
)

@given(instance=ocl_uml_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_ocl_uml_templateparametertype_instantiation(instance):
    assert isinstance(instance, ocl_uml_TemplateParameterType)

@given(instance=ocl_uml_VariableExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_variableexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_VariableExp)

@given(instance=ocl_uml_Variable_strategy)
@settings(max_examples=50)
def test_ocl_uml_variable_instantiation(instance):
    assert isinstance(instance, ocl_uml_Variable)

@given(instance=ocl_uml_UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_UnspecifiedValueExp)

@given(instance=ocl_uml_TypeExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_typeexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_TypeExp)

@given(instance=ocl_uml_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_uml_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleLiteralPart)

@given(instance=ocl_uml_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_UnlimitedNaturalLiteralExp)

@given(instance=ocl_uml_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NumericLiteralExp)

@given(instance=ocl_uml_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleLiteralExp)

@given(instance=ocl_uml_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_StringLiteralExp)

@given(instance=ocl_uml_StateExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_stateexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_StateExp)

@given(instance=ocl_uml_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_RealLiteralExp)

@given(instance=ocl_uml_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_PropertyCallExp)

@given(instance=ocl_uml_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_OperationCallExp)

@given(instance=ocl_uml_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NullLiteralExp)

@given(instance=ocl_uml_MessageExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_messageexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_MessageExp)

@given(instance=ocl_uml_LetExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_letexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LetExp)

@given(instance=ocl_uml_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IteratorExp)

@given(instance=ocl_uml_LoopExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_loopexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LoopExp)

@given(instance=ocl_uml_IterateExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_iterateexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IterateExp)

@given(instance=ocl_uml_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_InvalidLiteralExp)

@given(instance=ocl_uml_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_NavigationCallExp)

@given(instance=ocl_uml_AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_AssociationClassCallExp)

@given(instance=ocl_uml_ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_ocl_uml_expressioninocl_instantiation(instance):
    assert isinstance(instance, ocl_uml_ExpressionInOCL)

@given(instance=ocl_uml_SequenceType_strategy)
@settings(max_examples=50)
def test_ocl_uml_sequencetype_instantiation(instance):
    assert isinstance(instance, ocl_uml_SequenceType)

@given(instance=ocl_uml_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IntegerLiteralExp)

@given(instance=ocl_uml_IfExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_ifexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_IfExp)

@given(instance=ocl_uml_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_EnumLiteralExp)

@given(instance=ocl_uml_CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl_uml_collectionrange_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionRange)

@given(instance=ocl_uml_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionLiteralExp)

@given(instance=ocl_uml_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_uml_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionLiteralPart)

@given(instance=ocl_uml_CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl_uml_collectionitem_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionItem)

@given(instance=ocl_uml_LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_literalexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_LiteralExp)

@given(instance=ocl_uml_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_PrimitiveLiteralExp)

@given(instance=ocl_uml_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_BooleanLiteralExp)

@given(instance=ocl_uml_OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl_uml_oclexpression_instantiation(instance):
    assert isinstance(instance, ocl_uml_OCLExpression)

@given(instance=ocl_uml_CallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_callexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_CallExp)

@given(instance=ocl_uml_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl_uml_featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl_uml_FeatureCallExp)

@given(instance=ocl_uml_InvalidType_strategy)
@settings(max_examples=50)
def test_ocl_uml_invalidtype_instantiation(instance):
    assert isinstance(instance, ocl_uml_InvalidType)

@given(instance=ocl_uml_VoidType_strategy)
@settings(max_examples=50)
def test_ocl_uml_voidtype_instantiation(instance):
    assert isinstance(instance, ocl_uml_VoidType)

@given(instance=uml_ocl_Operation_strategy)
@settings(max_examples=50)
def test_uml_ocl_operation_instantiation(instance):
    assert isinstance(instance, uml_ocl_Operation)

@given(instance=ocl_uml_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_uml_orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl_uml_OrderedSetType)

@given(instance=ocl_uml_SetType_strategy)
@settings(max_examples=50)
def test_ocl_uml_settype_instantiation(instance):
    assert isinstance(instance, ocl_uml_SetType)

@given(instance=ocl_uml_BagType_strategy)
@settings(max_examples=50)
def test_ocl_uml_bagtype_instantiation(instance):
    assert isinstance(instance, ocl_uml_BagType)

@given(instance=ocl_uml_TupleType_strategy)
@settings(max_examples=50)
def test_ocl_uml_tupletype_instantiation(instance):
    assert isinstance(instance, ocl_uml_TupleType)

@given(instance=ocl_uml_CollectionType_strategy)
@settings(max_examples=50)
def test_ocl_uml_collectiontype_instantiation(instance):
    assert isinstance(instance, ocl_uml_CollectionType)

@given(instance=ocl_uml_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_uml_primitivetype_instantiation(instance):
    assert isinstance(instance, ocl_uml_PrimitiveType)

@given(instance=uml_ocl_Property_strategy)
@settings(max_examples=50)
def test_uml_ocl_property_instantiation(instance):
    assert isinstance(instance, uml_ocl_Property)

@given(instance=ocl_uml_MessageType_strategy)
@settings(max_examples=50)
def test_ocl_uml_messagetype_instantiation(instance):
    assert isinstance(instance, ocl_uml_MessageType)

@given(instance=ocl_uml_TypeType_strategy)
@settings(max_examples=50)
def test_ocl_uml_typetype_instantiation(instance):
    assert isinstance(instance, ocl_uml_TypeType)

@given(instance=types_ElementType_strategy)
@settings(max_examples=50)
def test_types_elementtype_instantiation(instance):
    assert isinstance(instance, types_ElementType)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ocl_uml_ElementType_strategy)
@settings(max_examples=50)
def test_ocl_uml_elementtype_instantiation(instance):
    assert isinstance(instance, ocl_uml_ElementType)

@given(instance=ocl_uml_AnyType_strategy)
@settings(max_examples=50)
def test_ocl_uml_anytype_instantiation(instance):
    assert isinstance(instance, ocl_uml_AnyType)
