import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Parameter,
    LetExp,
    Class,
    TupleLiteralPart,
    Property,
    NavigationCallExp,
    EssentialOCL_PropertyCallExp,
    Operation,
    TupleLiteralExp,
    LoopExp,
    EssentialOCL_IteratorExp,
    EssentialOCL_IterateExp,
    FeatureCallExp,
    EssentialOCL_OperationCallExp,
    EssentialOCL_NavigationCallExp,
    CallExp,
    EssentialOCL_FeatureCallExp,
    NumericLiteralExp,
    EssentialOCL_RealLiteralExp,
    EssentialOCL_UnlimitedNaturalExp,
    EssentialOCL_IntegerLiteralExp,
    DataType,
    EssentialOCL_TupleType,
    EssentialOCL_CollectionType,
    CollectionLiteralExp,
    TypedElement,
    EssentialOCL_Variable,
    EssentialOCL_OclExpression,
    EssentialOCL_TupleLiteralPart,
    EssentialOCL_CollectionLiteralPart,
    LiteralExp,
    EssentialOCL_InvalidLiteralExp,
    EssentialOCL_TupleLiteralExp,
    EssentialOCL_PrimitiveLiteralExp,
    EssentialOCL_NullLiteralExp,
    EssentialOCL_CollectionLiteralExp,
    CollectionLiteralPart,
    EssentialOCL_CollectionRange,
    EssentialOCL_CollectionItem,
    Variable,
    EssentialOCL_ExpressionInOcl,
    EnumerationLiteral,
    EssentialOCL_EnumLiteralExp,
    OclExpression,
    EssentialOCL_LiteralExp,
    EssentialOCL_LoopExp,
    EssentialOCL_LetExp,
    EssentialOCL_IfExp,
    EssentialOCL_TypeExp,
    EssentialOCL_VariableExp,
    EssentialOCL_CallExp,
    PrimitiveLiteralExp,
    EssentialOCL_StringLiteralExp,
    EssentialOCL_NumericLiteralExp,
    EssentialOCL_BooleanLiteralExp,
    CollectionType,
    EssentialOCL_SequenceType,
    EssentialOCL_SetType,
    EssentialOCL_OrderedSetType,
    EssentialOCL_BagType,
    Type,
    EssentialOCL_InvalidType,
    EssentialOCL_VoidType,
    EssentialOCL_AnyType,
    EssentialOCL_TemplateParameterType,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_PropertyCallExp)


def test_essentialocl_propertycallexp_constructor_exists():
    assert callable(EssentialOCL_PropertyCallExp.__init__)


def test_essentialocl_propertycallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IteratorExp)


def test_essentialocl_iteratorexp_constructor_exists():
    assert callable(EssentialOCL_IteratorExp.__init__)


def test_essentialocl_iteratorexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IterateExp)


def test_essentialocl_iterateexp_constructor_exists():
    assert callable(EssentialOCL_IterateExp.__init__)


def test_essentialocl_iterateexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OperationCallExp)


def test_essentialocl_operationcallexp_constructor_exists():
    assert callable(EssentialOCL_OperationCallExp.__init__)


def test_essentialocl_operationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NavigationCallExp)


def test_essentialocl_navigationcallexp_constructor_exists():
    assert callable(EssentialOCL_NavigationCallExp.__init__)


def test_essentialocl_navigationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_FeatureCallExp)


def test_essentialocl_featurecallexp_constructor_exists():
    assert callable(EssentialOCL_FeatureCallExp.__init__)


def test_essentialocl_featurecallexp_constructor_args():
    sig = inspect.signature(EssentialOCL_FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_RealLiteralExp)


def test_essentialocl_realliteralexp_constructor_exists():
    assert callable(EssentialOCL_RealLiteralExp.__init__)


def test_essentialocl_realliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl_realliteralexp_has_realSymbol():
    assert hasattr(EssentialOCL_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in EssentialOCL_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_UnlimitedNaturalExp)


def test_essentialocl_unlimitednaturalexp_constructor_exists():
    assert callable(EssentialOCL_UnlimitedNaturalExp.__init__)


def test_essentialocl_unlimitednaturalexp_constructor_args():
    sig = inspect.signature(EssentialOCL_UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl_unlimitednaturalexp_has_symbol():
    assert hasattr(EssentialOCL_UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in EssentialOCL_UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IntegerLiteralExp)


def test_essentialocl_integerliteralexp_constructor_exists():
    assert callable(EssentialOCL_IntegerLiteralExp.__init__)


def test_essentialocl_integerliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl_integerliteralexp_has_integerSymbol():
    assert hasattr(EssentialOCL_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in EssentialOCL_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleType)


def test_essentialocl_tupletype_constructor_exists():
    assert callable(EssentialOCL_TupleType.__init__)


def test_essentialocl_tupletype_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionType)


def test_essentialocl_collectiontype_constructor_exists():
    assert callable(EssentialOCL_CollectionType.__init__)


def test_essentialocl_collectiontype_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variable_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_Variable)


def test_essentialocl_variable_constructor_exists():
    assert callable(EssentialOCL_Variable.__init__)


def test_essentialocl_variable_constructor_args():
    sig = inspect.signature(EssentialOCL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OclExpression)


def test_essentialocl_oclexpression_constructor_exists():
    assert callable(EssentialOCL_OclExpression.__init__)


def test_essentialocl_oclexpression_constructor_args():
    sig = inspect.signature(EssentialOCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleLiteralPart)


def test_essentialocl_tupleliteralpart_constructor_exists():
    assert callable(EssentialOCL_TupleLiteralPart.__init__)


def test_essentialocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionLiteralPart)


def test_essentialocl_collectionliteralpart_constructor_exists():
    assert callable(EssentialOCL_CollectionLiteralPart.__init__)


def test_essentialocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_InvalidLiteralExp)


def test_essentialocl_invalidliteralexp_constructor_exists():
    assert callable(EssentialOCL_InvalidLiteralExp.__init__)


def test_essentialocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TupleLiteralExp)


def test_essentialocl_tupleliteralexp_constructor_exists():
    assert callable(EssentialOCL_TupleLiteralExp.__init__)


def test_essentialocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_PrimitiveLiteralExp)


def test_essentialocl_primitiveliteralexp_constructor_exists():
    assert callable(EssentialOCL_PrimitiveLiteralExp.__init__)


def test_essentialocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NullLiteralExp)


def test_essentialocl_nullliteralexp_constructor_exists():
    assert callable(EssentialOCL_NullLiteralExp.__init__)


def test_essentialocl_nullliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionLiteralExp)


def test_essentialocl_collectionliteralexp_constructor_exists():
    assert callable(EssentialOCL_CollectionLiteralExp.__init__)


def test_essentialocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl_collectionliteralexp_has_kind():
    assert hasattr(EssentialOCL_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in EssentialOCL_CollectionLiteralExp.__mro__:
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



def test_essentialocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionRange)


def test_essentialocl_collectionrange_constructor_exists():
    assert callable(EssentialOCL_CollectionRange.__init__)


def test_essentialocl_collectionrange_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CollectionItem)


def test_essentialocl_collectionitem_constructor_exists():
    assert callable(EssentialOCL_CollectionItem.__init__)


def test_essentialocl_collectionitem_constructor_args():
    sig = inspect.signature(EssentialOCL_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_expressioninocl_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_ExpressionInOcl)


def test_essentialocl_expressioninocl_constructor_exists():
    assert callable(EssentialOCL_ExpressionInOcl.__init__)


def test_essentialocl_expressioninocl_constructor_args():
    sig = inspect.signature(EssentialOCL_ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_EnumLiteralExp)


def test_essentialocl_enumliteralexp_constructor_exists():
    assert callable(EssentialOCL_EnumLiteralExp.__init__)


def test_essentialocl_enumliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LiteralExp)


def test_essentialocl_literalexp_constructor_exists():
    assert callable(EssentialOCL_LiteralExp.__init__)


def test_essentialocl_literalexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LoopExp)


def test_essentialocl_loopexp_constructor_exists():
    assert callable(EssentialOCL_LoopExp.__init__)


def test_essentialocl_loopexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_letexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_LetExp)


def test_essentialocl_letexp_constructor_exists():
    assert callable(EssentialOCL_LetExp.__init__)


def test_essentialocl_letexp_constructor_args():
    sig = inspect.signature(EssentialOCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_IfExp)


def test_essentialocl_ifexp_constructor_exists():
    assert callable(EssentialOCL_IfExp.__init__)


def test_essentialocl_ifexp_constructor_args():
    sig = inspect.signature(EssentialOCL_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_typeexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TypeExp)


def test_essentialocl_typeexp_constructor_exists():
    assert callable(EssentialOCL_TypeExp.__init__)


def test_essentialocl_typeexp_constructor_args():
    sig = inspect.signature(EssentialOCL_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_VariableExp)


def test_essentialocl_variableexp_constructor_exists():
    assert callable(EssentialOCL_VariableExp.__init__)


def test_essentialocl_variableexp_constructor_args():
    sig = inspect.signature(EssentialOCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_callexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_CallExp)


def test_essentialocl_callexp_constructor_exists():
    assert callable(EssentialOCL_CallExp.__init__)


def test_essentialocl_callexp_constructor_args():
    sig = inspect.signature(EssentialOCL_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_StringLiteralExp)


def test_essentialocl_stringliteralexp_constructor_exists():
    assert callable(EssentialOCL_StringLiteralExp.__init__)


def test_essentialocl_stringliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl_stringliteralexp_has_stringSymbol():
    assert hasattr(EssentialOCL_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in EssentialOCL_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_NumericLiteralExp)


def test_essentialocl_numericliteralexp_constructor_exists():
    assert callable(EssentialOCL_NumericLiteralExp.__init__)


def test_essentialocl_numericliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_BooleanLiteralExp)


def test_essentialocl_booleanliteralexp_constructor_exists():
    assert callable(EssentialOCL_BooleanLiteralExp.__init__)


def test_essentialocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl_booleanliteralexp_has_booleanSymbol():
    assert hasattr(EssentialOCL_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in EssentialOCL_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_SequenceType)


def test_essentialocl_sequencetype_constructor_exists():
    assert callable(EssentialOCL_SequenceType.__init__)


def test_essentialocl_sequencetype_constructor_args():
    sig = inspect.signature(EssentialOCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_settype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_SetType)


def test_essentialocl_settype_constructor_exists():
    assert callable(EssentialOCL_SetType.__init__)


def test_essentialocl_settype_constructor_args():
    sig = inspect.signature(EssentialOCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_OrderedSetType)


def test_essentialocl_orderedsettype_constructor_exists():
    assert callable(EssentialOCL_OrderedSetType.__init__)


def test_essentialocl_orderedsettype_constructor_args():
    sig = inspect.signature(EssentialOCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_BagType)


def test_essentialocl_bagtype_constructor_exists():
    assert callable(EssentialOCL_BagType.__init__)


def test_essentialocl_bagtype_constructor_args():
    sig = inspect.signature(EssentialOCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_InvalidType)


def test_essentialocl_invalidtype_constructor_exists():
    assert callable(EssentialOCL_InvalidType.__init__)


def test_essentialocl_invalidtype_constructor_args():
    sig = inspect.signature(EssentialOCL_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_VoidType)


def test_essentialocl_voidtype_constructor_exists():
    assert callable(EssentialOCL_VoidType.__init__)


def test_essentialocl_voidtype_constructor_args():
    sig = inspect.signature(EssentialOCL_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_anytype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_AnyType)


def test_essentialocl_anytype_constructor_exists():
    assert callable(EssentialOCL_AnyType.__init__)


def test_essentialocl_anytype_constructor_args():
    sig = inspect.signature(EssentialOCL_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL_TemplateParameterType)


def test_essentialocl_templateparametertype_constructor_exists():
    assert callable(EssentialOCL_TemplateParameterType.__init__)


def test_essentialocl_templateparametertype_constructor_args():
    sig = inspect.signature(EssentialOCL_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_essentialocl_templateparametertype_has_specification():
    assert hasattr(EssentialOCL_TemplateParameterType, "specification")
    descriptor = None
    for klass in EssentialOCL_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Set",
        "Sequence",
        "OrderedSet",
        "Bag",
        "Collection",
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
Parameter_strategy = st.builds(
    Parameter,
)
LetExp_strategy = st.builds(
    LetExp,
)
Class_strategy = st.builds(
    Class,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
Property_strategy = st.builds(
    Property,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
EssentialOCL_PropertyCallExp_strategy = st.builds(
    EssentialOCL_PropertyCallExp,
)
Operation_strategy = st.builds(
    Operation,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EssentialOCL_IteratorExp_strategy = st.builds(
    EssentialOCL_IteratorExp,
)
EssentialOCL_IterateExp_strategy = st.builds(
    EssentialOCL_IterateExp,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
EssentialOCL_OperationCallExp_strategy = st.builds(
    EssentialOCL_OperationCallExp,
)
EssentialOCL_NavigationCallExp_strategy = st.builds(
    EssentialOCL_NavigationCallExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
EssentialOCL_FeatureCallExp_strategy = st.builds(
    EssentialOCL_FeatureCallExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
EssentialOCL_RealLiteralExp_strategy = st.builds(
    EssentialOCL_RealLiteralExp,
    realSymbol=
        safe_text
)
EssentialOCL_UnlimitedNaturalExp_strategy = st.builds(
    EssentialOCL_UnlimitedNaturalExp,
    symbol=
        safe_text
)
EssentialOCL_IntegerLiteralExp_strategy = st.builds(
    EssentialOCL_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
EssentialOCL_TupleType_strategy = st.builds(
    EssentialOCL_TupleType,
)
EssentialOCL_CollectionType_strategy = st.builds(
    EssentialOCL_CollectionType,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
EssentialOCL_Variable_strategy = st.builds(
    EssentialOCL_Variable,
)
EssentialOCL_OclExpression_strategy = st.builds(
    EssentialOCL_OclExpression,
)
EssentialOCL_TupleLiteralPart_strategy = st.builds(
    EssentialOCL_TupleLiteralPart,
)
EssentialOCL_CollectionLiteralPart_strategy = st.builds(
    EssentialOCL_CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
EssentialOCL_InvalidLiteralExp_strategy = st.builds(
    EssentialOCL_InvalidLiteralExp,
)
EssentialOCL_TupleLiteralExp_strategy = st.builds(
    EssentialOCL_TupleLiteralExp,
)
EssentialOCL_PrimitiveLiteralExp_strategy = st.builds(
    EssentialOCL_PrimitiveLiteralExp,
)
EssentialOCL_NullLiteralExp_strategy = st.builds(
    EssentialOCL_NullLiteralExp,
)
EssentialOCL_CollectionLiteralExp_strategy = st.builds(
    EssentialOCL_CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
EssentialOCL_CollectionRange_strategy = st.builds(
    EssentialOCL_CollectionRange,
)
EssentialOCL_CollectionItem_strategy = st.builds(
    EssentialOCL_CollectionItem,
)
Variable_strategy = st.builds(
    Variable,
)
EssentialOCL_ExpressionInOcl_strategy = st.builds(
    EssentialOCL_ExpressionInOcl,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
EssentialOCL_EnumLiteralExp_strategy = st.builds(
    EssentialOCL_EnumLiteralExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EssentialOCL_LiteralExp_strategy = st.builds(
    EssentialOCL_LiteralExp,
)
EssentialOCL_LoopExp_strategy = st.builds(
    EssentialOCL_LoopExp,
)
EssentialOCL_LetExp_strategy = st.builds(
    EssentialOCL_LetExp,
)
EssentialOCL_IfExp_strategy = st.builds(
    EssentialOCL_IfExp,
)
EssentialOCL_TypeExp_strategy = st.builds(
    EssentialOCL_TypeExp,
)
EssentialOCL_VariableExp_strategy = st.builds(
    EssentialOCL_VariableExp,
)
EssentialOCL_CallExp_strategy = st.builds(
    EssentialOCL_CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
EssentialOCL_StringLiteralExp_strategy = st.builds(
    EssentialOCL_StringLiteralExp,
    stringSymbol=
        safe_text
)
EssentialOCL_NumericLiteralExp_strategy = st.builds(
    EssentialOCL_NumericLiteralExp,
)
EssentialOCL_BooleanLiteralExp_strategy = st.builds(
    EssentialOCL_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EssentialOCL_SequenceType_strategy = st.builds(
    EssentialOCL_SequenceType,
)
EssentialOCL_SetType_strategy = st.builds(
    EssentialOCL_SetType,
)
EssentialOCL_OrderedSetType_strategy = st.builds(
    EssentialOCL_OrderedSetType,
)
EssentialOCL_BagType_strategy = st.builds(
    EssentialOCL_BagType,
)
Type_strategy = st.builds(
    Type,
)
EssentialOCL_InvalidType_strategy = st.builds(
    EssentialOCL_InvalidType,
)
EssentialOCL_VoidType_strategy = st.builds(
    EssentialOCL_VoidType,
)
EssentialOCL_AnyType_strategy = st.builds(
    EssentialOCL_AnyType,
)
EssentialOCL_TemplateParameterType_strategy = st.builds(
    EssentialOCL_TemplateParameterType,
    specification=
        safe_text
)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=EssentialOCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_PropertyCallExp)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EssentialOCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IteratorExp)

@given(instance=EssentialOCL_IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl_iterateexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IterateExp)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=EssentialOCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OperationCallExp)

@given(instance=EssentialOCL_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_navigationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NavigationCallExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=EssentialOCL_FeatureCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_featurecallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_FeatureCallExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=EssentialOCL_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_RealLiteralExp)



@given(instance=EssentialOCL_RealLiteralExp_strategy)
def test_essentialocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=EssentialOCL_UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl_unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_UnlimitedNaturalExp)



@given(instance=EssentialOCL_UnlimitedNaturalExp_strategy)
def test_essentialocl_unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=EssentialOCL_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IntegerLiteralExp)



@given(instance=EssentialOCL_IntegerLiteralExp_strategy)
def test_essentialocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=EssentialOCL_TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl_tupletype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleType)

@given(instance=EssentialOCL_CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl_collectiontype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionType)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=EssentialOCL_Variable_strategy)
@settings(max_examples=50)
def test_essentialocl_variable_instantiation(instance):
    assert isinstance(instance, EssentialOCL_Variable)

@given(instance=EssentialOCL_OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl_oclexpression_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OclExpression)

@given(instance=EssentialOCL_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleLiteralPart)

@given(instance=EssentialOCL_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=EssentialOCL_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_InvalidLiteralExp)

@given(instance=EssentialOCL_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TupleLiteralExp)

@given(instance=EssentialOCL_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_PrimitiveLiteralExp)

@given(instance=EssentialOCL_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NullLiteralExp)

@given(instance=EssentialOCL_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionLiteralExp)



@given(instance=EssentialOCL_CollectionLiteralExp_strategy)
def test_essentialocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=EssentialOCL_CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionrange_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionRange)

@given(instance=EssentialOCL_CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl_collectionitem_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CollectionItem)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=EssentialOCL_ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl_expressioninocl_instantiation(instance):
    assert isinstance(instance, EssentialOCL_ExpressionInOcl)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=EssentialOCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_EnumLiteralExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EssentialOCL_LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_literalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LiteralExp)

@given(instance=EssentialOCL_LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl_loopexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LoopExp)

@given(instance=EssentialOCL_LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl_letexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_LetExp)

@given(instance=EssentialOCL_IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl_ifexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_IfExp)

@given(instance=EssentialOCL_TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl_typeexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TypeExp)

@given(instance=EssentialOCL_VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl_variableexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_VariableExp)

@given(instance=EssentialOCL_CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl_callexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=EssentialOCL_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_StringLiteralExp)



@given(instance=EssentialOCL_StringLiteralExp_strategy)
def test_essentialocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=EssentialOCL_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_numericliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_NumericLiteralExp)

@given(instance=EssentialOCL_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL_BooleanLiteralExp)



@given(instance=EssentialOCL_BooleanLiteralExp_strategy)
def test_essentialocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EssentialOCL_SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl_sequencetype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_SequenceType)

@given(instance=EssentialOCL_SetType_strategy)
@settings(max_examples=50)
def test_essentialocl_settype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_SetType)

@given(instance=EssentialOCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_OrderedSetType)

@given(instance=EssentialOCL_BagType_strategy)
@settings(max_examples=50)
def test_essentialocl_bagtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_BagType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=EssentialOCL_InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl_invalidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_InvalidType)

@given(instance=EssentialOCL_VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl_voidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_VoidType)

@given(instance=EssentialOCL_AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl_anytype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_AnyType)

@given(instance=EssentialOCL_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_essentialocl_templateparametertype_instantiation(instance):
    assert isinstance(instance, EssentialOCL_TemplateParameterType)



@given(instance=EssentialOCL_TemplateParameterType_strategy)
def test_essentialocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original
