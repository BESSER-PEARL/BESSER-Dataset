import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FeatureCallExpCS,
    ocl_cst_OperationCallExpCS,
    LoopExpCS,
    ocl_cst_IterateExpCS,
    ocl_cst_IteratorExpCS,
    CallExpCS,
    ocl_cst_FeatureCallExpCS,
    ocl_cst_LoopExpCS,
    CollectionLiteralPartCS,
    ocl_cst_CollectionRangeCS,
    LiteralExpCS,
    ocl_cst_PrimitiveLiteralExpCS,
    ocl_cst_TupleLiteralExpCS,
    ocl_cst_CollectionLiteralExpCS,
    cst_LiteralExpCS,
    cst_PrimitiveLiteralExpCS,
    PrimitiveLiteralExpCS,
    ocl_cst_UnlimitedNaturalLiteralExpCS,
    ocl_cst_StringLiteralExpCS,
    ocl_cst_RealLiteralExpCS,
    ocl_cst_IntegerLiteralExpCS,
    cst_TypeCS,
    cst_SimpleNameCS,
    ocl_cst_BooleanLiteralExpCS,
    ocl_cst_InvalidLiteralExpCS,
    ocl_cst_NullLiteralExpCS,
    ocl_cst_CollectionTypeCS,
    ocl_cst_PrimitiveTypeCS,
    IsMarkedPreCS,
    OCLMessageArgCS,
    VariableCS,
    PrePostOrBodyDeclCS,
    OperationCS,
    DefExpressionCS,
    OCLExpressionCS,
    ocl_cst_SimpleNameCS,
    ocl_cst_VariableExpCS,
    ocl_cst_LetExpCS,
    ocl_cst_LiteralExpCS,
    ocl_cst_CallExpCS,
    ocl_cst_IfExpCS,
    ocl_cst_MessageExpCS,
    ocl_cst_TypeCS,
    SimpleNameCS,
    TypeCS,
    ocl_cst_TupleTypeCS,
    ocl_cst_PathNameCS,
    PackageDeclarationCS,
    ContextDeclCS,
    ocl_cst_OperationContextDeclCS,
    PathNameCS,
    InvOrDefCS,
    ocl_cst_InvCS,
    ocl_cst_DefCS,
    ocl_cst_ClassifierContextDeclCS,
    InitOrDerValueCS,
    ocl_cst_DerValueCS,
    ocl_cst_InitValueCS,
    ocl_cst_PropertyContextCS,
    CSTNode,
    ocl_cst_PrePostOrBodyDeclCS,
    ocl_cst_OCLMessageArgCS,
    ocl_cst_IsMarkedPreCS,
    ocl_cst_InvOrDefCS,
    ocl_cst_OCLDocumentCS,
    ocl_cst_VariableCS,
    ocl_cst_OperationCS,
    ocl_cst_OCLExpressionCS,
    ocl_cst_DefExpressionCS,
    ocl_cst_ContextDeclCS,
    ocl_cst_InitOrDerValueCS,
    ocl_cst_CollectionLiteralPartCS,
    ocl_cst_PackageDeclarationCS,
    ocl_cst_CSTNode,
    MessageExpKind,
    DotOrArrowEnum,
    PrePostOrBodyEnum,
    SimpleTypeEnum,
    CollectionTypeIdentifierEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featurecallexpcs_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpCS)


def test_featurecallexpcs_constructor_exists():
    assert callable(FeatureCallExpCS.__init__)


def test_featurecallexpcs_constructor_args():
    sig = inspect.signature(FeatureCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OperationCallExpCS)


def test_ocl_cst_operationcallexpcs_constructor_exists():
    assert callable(ocl_cst_OperationCallExpCS.__init__)


def test_ocl_cst_operationcallexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_ocl_cst_operationcallexpcs_has_isAtomic():
    assert hasattr(ocl_cst_OperationCallExpCS, "isAtomic")
    descriptor = None
    for klass in ocl_cst_OperationCallExpCS.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_IterateExpCS)


def test_ocl_cst_iterateexpcs_constructor_exists():
    assert callable(ocl_cst_IterateExpCS.__init__)


def test_ocl_cst_iterateexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_iteratorexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_IteratorExpCS)


def test_ocl_cst_iteratorexpcs_constructor_exists():
    assert callable(ocl_cst_IteratorExpCS.__init__)


def test_ocl_cst_iteratorexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_IteratorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_featurecallexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_FeatureCallExpCS)


def test_ocl_cst_featurecallexpcs_constructor_exists():
    assert callable(ocl_cst_FeatureCallExpCS.__init__)


def test_ocl_cst_featurecallexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_FeatureCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_LoopExpCS)


def test_ocl_cst_loopexpcs_constructor_exists():
    assert callable(ocl_cst_LoopExpCS.__init__)


def test_ocl_cst_loopexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPartCS)


def test_collectionliteralpartcs_constructor_exists():
    assert callable(CollectionLiteralPartCS.__init__)


def test_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_collectionrangecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CollectionRangeCS)


def test_ocl_cst_collectionrangecs_constructor_exists():
    assert callable(ocl_cst_CollectionRangeCS.__init__)


def test_ocl_cst_collectionrangecs_constructor_args():
    sig = inspect.signature(ocl_cst_CollectionRangeCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PrimitiveLiteralExpCS)


def test_ocl_cst_primitiveliteralexpcs_constructor_exists():
    assert callable(ocl_cst_PrimitiveLiteralExpCS.__init__)


def test_ocl_cst_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocl_cst_primitiveliteralexpcs_has_symbol():
    assert hasattr(ocl_cst_PrimitiveLiteralExpCS, "symbol")
    descriptor = None
    for klass in ocl_cst_PrimitiveLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_TupleLiteralExpCS)


def test_ocl_cst_tupleliteralexpcs_constructor_exists():
    assert callable(ocl_cst_TupleLiteralExpCS.__init__)


def test_ocl_cst_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CollectionLiteralExpCS)


def test_ocl_cst_collectionliteralexpcs_constructor_exists():
    assert callable(ocl_cst_CollectionLiteralExpCS.__init__)


def test_ocl_cst_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "collectionType" in params, "Missing parameter 'collectionType'"

def test_ocl_cst_collectionliteralexpcs_has_collectionType():
    assert hasattr(ocl_cst_CollectionLiteralExpCS, "collectionType")
    descriptor = None
    for klass in ocl_cst_CollectionLiteralExpCS.__mro__:
        if "collectionType" in klass.__dict__:
            descriptor = klass.__dict__["collectionType"]
            break
    assert isinstance(descriptor, property)



def test_cst_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(cst_LiteralExpCS)


def test_cst_literalexpcs_constructor_exists():
    assert callable(cst_LiteralExpCS.__init__)


def test_cst_literalexpcs_constructor_args():
    sig = inspect.signature(cst_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(cst_PrimitiveLiteralExpCS)


def test_cst_primitiveliteralexpcs_constructor_exists():
    assert callable(cst_PrimitiveLiteralExpCS.__init__)


def test_cst_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(cst_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_UnlimitedNaturalLiteralExpCS)


def test_ocl_cst_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(ocl_cst_UnlimitedNaturalLiteralExpCS.__init__)


def test_ocl_cst_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"
    assert "extendedIntegerSymbol" in params, "Missing parameter 'extendedIntegerSymbol'"
    assert "longSymbol" in params, "Missing parameter 'longSymbol'"

def test_ocl_cst_unlimitednaturalliteralexpcs_has_integerSymbol():
    assert hasattr(ocl_cst_UnlimitedNaturalLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in ocl_cst_UnlimitedNaturalLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_unlimitednaturalliteralexpcs_has_extendedIntegerSymbol():
    assert hasattr(ocl_cst_UnlimitedNaturalLiteralExpCS, "extendedIntegerSymbol")
    descriptor = None
    for klass in ocl_cst_UnlimitedNaturalLiteralExpCS.__mro__:
        if "extendedIntegerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["extendedIntegerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_unlimitednaturalliteralexpcs_has_longSymbol():
    assert hasattr(ocl_cst_UnlimitedNaturalLiteralExpCS, "longSymbol")
    descriptor = None
    for klass in ocl_cst_UnlimitedNaturalLiteralExpCS.__mro__:
        if "longSymbol" in klass.__dict__:
            descriptor = klass.__dict__["longSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_StringLiteralExpCS)


def test_ocl_cst_stringliteralexpcs_constructor_exists():
    assert callable(ocl_cst_StringLiteralExpCS.__init__)


def test_ocl_cst_stringliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"
    assert "unescapedStringSymbol" in params, "Missing parameter 'unescapedStringSymbol'"

def test_ocl_cst_stringliteralexpcs_has_stringSymbol():
    assert hasattr(ocl_cst_StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in ocl_cst_StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_stringliteralexpcs_has_unescapedStringSymbol():
    assert hasattr(ocl_cst_StringLiteralExpCS, "unescapedStringSymbol")
    descriptor = None
    for klass in ocl_cst_StringLiteralExpCS.__mro__:
        if "unescapedStringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["unescapedStringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_realliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_RealLiteralExpCS)


def test_ocl_cst_realliteralexpcs_constructor_exists():
    assert callable(ocl_cst_RealLiteralExpCS.__init__)


def test_ocl_cst_realliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_RealLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl_cst_realliteralexpcs_has_realSymbol():
    assert hasattr(ocl_cst_RealLiteralExpCS, "realSymbol")
    descriptor = None
    for klass in ocl_cst_RealLiteralExpCS.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_integerliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_IntegerLiteralExpCS)


def test_ocl_cst_integerliteralexpcs_constructor_exists():
    assert callable(ocl_cst_IntegerLiteralExpCS.__init__)


def test_ocl_cst_integerliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_IntegerLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "extendedIntegerSymbol" in params, "Missing parameter 'extendedIntegerSymbol'"
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"
    assert "longSymbol" in params, "Missing parameter 'longSymbol'"

def test_ocl_cst_integerliteralexpcs_has_extendedIntegerSymbol():
    assert hasattr(ocl_cst_IntegerLiteralExpCS, "extendedIntegerSymbol")
    descriptor = None
    for klass in ocl_cst_IntegerLiteralExpCS.__mro__:
        if "extendedIntegerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["extendedIntegerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_integerliteralexpcs_has_integerSymbol():
    assert hasattr(ocl_cst_IntegerLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in ocl_cst_IntegerLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_integerliteralexpcs_has_longSymbol():
    assert hasattr(ocl_cst_IntegerLiteralExpCS, "longSymbol")
    descriptor = None
    for klass in ocl_cst_IntegerLiteralExpCS.__mro__:
        if "longSymbol" in klass.__dict__:
            descriptor = klass.__dict__["longSymbol"]
            break
    assert isinstance(descriptor, property)



def test_cst_typecs_is_not_abstract():
    assert not inspect.isabstract(cst_TypeCS)


def test_cst_typecs_constructor_exists():
    assert callable(cst_TypeCS.__init__)


def test_cst_typecs_constructor_args():
    sig = inspect.signature(cst_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(cst_SimpleNameCS)


def test_cst_simplenamecs_constructor_exists():
    assert callable(cst_SimpleNameCS.__init__)


def test_cst_simplenamecs_constructor_args():
    sig = inspect.signature(cst_SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_BooleanLiteralExpCS)


def test_ocl_cst_booleanliteralexpcs_constructor_exists():
    assert callable(ocl_cst_BooleanLiteralExpCS.__init__)


def test_ocl_cst_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl_cst_booleanliteralexpcs_has_booleanSymbol():
    assert hasattr(ocl_cst_BooleanLiteralExpCS, "booleanSymbol")
    descriptor = None
    for klass in ocl_cst_BooleanLiteralExpCS.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_InvalidLiteralExpCS)


def test_ocl_cst_invalidliteralexpcs_constructor_exists():
    assert callable(ocl_cst_InvalidLiteralExpCS.__init__)


def test_ocl_cst_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_NullLiteralExpCS)


def test_ocl_cst_nullliteralexpcs_constructor_exists():
    assert callable(ocl_cst_NullLiteralExpCS.__init__)


def test_ocl_cst_nullliteralexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CollectionTypeCS)


def test_ocl_cst_collectiontypecs_constructor_exists():
    assert callable(ocl_cst_CollectionTypeCS.__init__)


def test_ocl_cst_collectiontypecs_constructor_args():
    sig = inspect.signature(ocl_cst_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "collectionTypeIdentifier" in params, "Missing parameter 'collectionTypeIdentifier'"

def test_ocl_cst_collectiontypecs_has_collectionTypeIdentifier():
    assert hasattr(ocl_cst_CollectionTypeCS, "collectionTypeIdentifier")
    descriptor = None
    for klass in ocl_cst_CollectionTypeCS.__mro__:
        if "collectionTypeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["collectionTypeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_primitivetypecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PrimitiveTypeCS)


def test_ocl_cst_primitivetypecs_constructor_exists():
    assert callable(ocl_cst_PrimitiveTypeCS.__init__)


def test_ocl_cst_primitivetypecs_constructor_args():
    sig = inspect.signature(ocl_cst_PrimitiveTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ismarkedprecs_is_not_abstract():
    assert not inspect.isabstract(IsMarkedPreCS)


def test_ismarkedprecs_constructor_exists():
    assert callable(IsMarkedPreCS.__init__)


def test_ismarkedprecs_constructor_args():
    sig = inspect.signature(IsMarkedPreCS.__init__)
    params = list(sig.parameters.keys())



def test_oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(OCLMessageArgCS)


def test_oclmessageargcs_constructor_exists():
    assert callable(OCLMessageArgCS.__init__)


def test_oclmessageargcs_constructor_args():
    sig = inspect.signature(OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_prepostorbodydeclcs_is_not_abstract():
    assert not inspect.isabstract(PrePostOrBodyDeclCS)


def test_prepostorbodydeclcs_constructor_exists():
    assert callable(PrePostOrBodyDeclCS.__init__)


def test_prepostorbodydeclcs_constructor_args():
    sig = inspect.signature(PrePostOrBodyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_operationcs_is_not_abstract():
    assert not inspect.isabstract(OperationCS)


def test_operationcs_constructor_exists():
    assert callable(OperationCS.__init__)


def test_operationcs_constructor_args():
    sig = inspect.signature(OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_defexpressioncs_is_not_abstract():
    assert not inspect.isabstract(DefExpressionCS)


def test_defexpressioncs_constructor_exists():
    assert callable(DefExpressionCS.__init__)


def test_defexpressioncs_constructor_args():
    sig = inspect.signature(DefExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_SimpleNameCS)


def test_ocl_cst_simplenamecs_constructor_exists():
    assert callable(ocl_cst_SimpleNameCS.__init__)


def test_ocl_cst_simplenamecs_constructor_args():
    sig = inspect.signature(ocl_cst_SimpleNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_ocl_cst_simplenamecs_has_type():
    assert hasattr(ocl_cst_SimpleNameCS, "type")
    descriptor = None
    for klass in ocl_cst_SimpleNameCS.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_simplenamecs_has_value():
    assert hasattr(ocl_cst_SimpleNameCS, "value")
    descriptor = None
    for klass in ocl_cst_SimpleNameCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_VariableExpCS)


def test_ocl_cst_variableexpcs_constructor_exists():
    assert callable(ocl_cst_VariableExpCS.__init__)


def test_ocl_cst_variableexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_letexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_LetExpCS)


def test_ocl_cst_letexpcs_constructor_exists():
    assert callable(ocl_cst_LetExpCS.__init__)


def test_ocl_cst_letexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_LiteralExpCS)


def test_ocl_cst_literalexpcs_constructor_exists():
    assert callable(ocl_cst_LiteralExpCS.__init__)


def test_ocl_cst_literalexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_callexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CallExpCS)


def test_ocl_cst_callexpcs_constructor_exists():
    assert callable(ocl_cst_CallExpCS.__init__)


def test_ocl_cst_callexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_CallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_ocl_cst_callexpcs_has_accessor():
    assert hasattr(ocl_cst_CallExpCS, "accessor")
    descriptor = None
    for klass in ocl_cst_CallExpCS.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_IfExpCS)


def test_ocl_cst_ifexpcs_constructor_exists():
    assert callable(ocl_cst_IfExpCS.__init__)


def test_ocl_cst_ifexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_messageexpcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_MessageExpCS)


def test_ocl_cst_messageexpcs_constructor_exists():
    assert callable(ocl_cst_MessageExpCS.__init__)


def test_ocl_cst_messageexpcs_constructor_args():
    sig = inspect.signature(ocl_cst_MessageExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_cst_messageexpcs_has_kind():
    assert hasattr(ocl_cst_MessageExpCS, "kind")
    descriptor = None
    for klass in ocl_cst_MessageExpCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_typecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_TypeCS)


def test_ocl_cst_typecs_constructor_exists():
    assert callable(ocl_cst_TypeCS.__init__)


def test_ocl_cst_typecs_constructor_args():
    sig = inspect.signature(ocl_cst_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(SimpleNameCS)


def test_simplenamecs_constructor_exists():
    assert callable(SimpleNameCS.__init__)


def test_simplenamecs_constructor_args():
    sig = inspect.signature(SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_TupleTypeCS)


def test_ocl_cst_tupletypecs_constructor_exists():
    assert callable(ocl_cst_TupleTypeCS.__init__)


def test_ocl_cst_tupletypecs_constructor_args():
    sig = inspect.signature(ocl_cst_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PathNameCS)


def test_ocl_cst_pathnamecs_constructor_exists():
    assert callable(ocl_cst_PathNameCS.__init__)


def test_ocl_cst_pathnamecs_constructor_args():
    sig = inspect.signature(ocl_cst_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(PackageDeclarationCS)


def test_packagedeclarationcs_constructor_exists():
    assert callable(PackageDeclarationCS.__init__)


def test_packagedeclarationcs_constructor_args():
    sig = inspect.signature(PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ContextDeclCS)


def test_contextdeclcs_constructor_exists():
    assert callable(ContextDeclCS.__init__)


def test_contextdeclcs_constructor_args():
    sig = inspect.signature(ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_operationcontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OperationContextDeclCS)


def test_ocl_cst_operationcontextdeclcs_constructor_exists():
    assert callable(ocl_cst_OperationContextDeclCS.__init__)


def test_ocl_cst_operationcontextdeclcs_constructor_args():
    sig = inspect.signature(ocl_cst_OperationContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_invordefcs_is_not_abstract():
    assert not inspect.isabstract(InvOrDefCS)


def test_invordefcs_constructor_exists():
    assert callable(InvOrDefCS.__init__)


def test_invordefcs_constructor_args():
    sig = inspect.signature(InvOrDefCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_invcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_InvCS)


def test_ocl_cst_invcs_constructor_exists():
    assert callable(ocl_cst_InvCS.__init__)


def test_ocl_cst_invcs_constructor_args():
    sig = inspect.signature(ocl_cst_InvCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_defcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_DefCS)


def test_ocl_cst_defcs_constructor_exists():
    assert callable(ocl_cst_DefCS.__init__)


def test_ocl_cst_defcs_constructor_args():
    sig = inspect.signature(ocl_cst_DefCS.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ocl_cst_defcs_has_static():
    assert hasattr(ocl_cst_DefCS, "static")
    descriptor = None
    for klass in ocl_cst_DefCS.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_classifiercontextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_ClassifierContextDeclCS)


def test_ocl_cst_classifiercontextdeclcs_constructor_exists():
    assert callable(ocl_cst_ClassifierContextDeclCS.__init__)


def test_ocl_cst_classifiercontextdeclcs_constructor_args():
    sig = inspect.signature(ocl_cst_ClassifierContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_initordervaluecs_is_not_abstract():
    assert not inspect.isabstract(InitOrDerValueCS)


def test_initordervaluecs_constructor_exists():
    assert callable(InitOrDerValueCS.__init__)


def test_initordervaluecs_constructor_args():
    sig = inspect.signature(InitOrDerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_dervaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_DerValueCS)


def test_ocl_cst_dervaluecs_constructor_exists():
    assert callable(ocl_cst_DerValueCS.__init__)


def test_ocl_cst_dervaluecs_constructor_args():
    sig = inspect.signature(ocl_cst_DerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_initvaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_InitValueCS)


def test_ocl_cst_initvaluecs_constructor_exists():
    assert callable(ocl_cst_InitValueCS.__init__)


def test_ocl_cst_initvaluecs_constructor_args():
    sig = inspect.signature(ocl_cst_InitValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_propertycontextcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PropertyContextCS)


def test_ocl_cst_propertycontextcs_constructor_exists():
    assert callable(ocl_cst_PropertyContextCS.__init__)


def test_ocl_cst_propertycontextcs_constructor_args():
    sig = inspect.signature(ocl_cst_PropertyContextCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_prepostorbodydeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PrePostOrBodyDeclCS)


def test_ocl_cst_prepostorbodydeclcs_constructor_exists():
    assert callable(ocl_cst_PrePostOrBodyDeclCS.__init__)


def test_ocl_cst_prepostorbodydeclcs_constructor_args():
    sig = inspect.signature(ocl_cst_PrePostOrBodyDeclCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_cst_prepostorbodydeclcs_has_kind():
    assert hasattr(ocl_cst_PrePostOrBodyDeclCS, "kind")
    descriptor = None
    for klass in ocl_cst_PrePostOrBodyDeclCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_oclmessageargcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OCLMessageArgCS)


def test_ocl_cst_oclmessageargcs_constructor_exists():
    assert callable(ocl_cst_OCLMessageArgCS.__init__)


def test_ocl_cst_oclmessageargcs_constructor_args():
    sig = inspect.signature(ocl_cst_OCLMessageArgCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_ismarkedprecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_IsMarkedPreCS)


def test_ocl_cst_ismarkedprecs_constructor_exists():
    assert callable(ocl_cst_IsMarkedPreCS.__init__)


def test_ocl_cst_ismarkedprecs_constructor_args():
    sig = inspect.signature(ocl_cst_IsMarkedPreCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_invordefcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_InvOrDefCS)


def test_ocl_cst_invordefcs_constructor_exists():
    assert callable(ocl_cst_InvOrDefCS.__init__)


def test_ocl_cst_invordefcs_constructor_args():
    sig = inspect.signature(ocl_cst_InvOrDefCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_ocldocumentcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OCLDocumentCS)


def test_ocl_cst_ocldocumentcs_constructor_exists():
    assert callable(ocl_cst_OCLDocumentCS.__init__)


def test_ocl_cst_ocldocumentcs_constructor_args():
    sig = inspect.signature(ocl_cst_OCLDocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_variablecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_VariableCS)


def test_ocl_cst_variablecs_constructor_exists():
    assert callable(ocl_cst_VariableCS.__init__)


def test_ocl_cst_variablecs_constructor_args():
    sig = inspect.signature(ocl_cst_VariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_cst_variablecs_has_name():
    assert hasattr(ocl_cst_VariableCS, "name")
    descriptor = None
    for klass in ocl_cst_VariableCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_cst_operationcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OperationCS)


def test_ocl_cst_operationcs_constructor_exists():
    assert callable(ocl_cst_OperationCS.__init__)


def test_ocl_cst_operationcs_constructor_args():
    sig = inspect.signature(ocl_cst_OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_OCLExpressionCS)


def test_ocl_cst_oclexpressioncs_constructor_exists():
    assert callable(ocl_cst_OCLExpressionCS.__init__)


def test_ocl_cst_oclexpressioncs_constructor_args():
    sig = inspect.signature(ocl_cst_OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_defexpressioncs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_DefExpressionCS)


def test_ocl_cst_defexpressioncs_constructor_exists():
    assert callable(ocl_cst_DefExpressionCS.__init__)


def test_ocl_cst_defexpressioncs_constructor_args():
    sig = inspect.signature(ocl_cst_DefExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_contextdeclcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_ContextDeclCS)


def test_ocl_cst_contextdeclcs_constructor_exists():
    assert callable(ocl_cst_ContextDeclCS.__init__)


def test_ocl_cst_contextdeclcs_constructor_args():
    sig = inspect.signature(ocl_cst_ContextDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_initordervaluecs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_InitOrDerValueCS)


def test_ocl_cst_initordervaluecs_constructor_exists():
    assert callable(ocl_cst_InitOrDerValueCS.__init__)


def test_ocl_cst_initordervaluecs_constructor_args():
    sig = inspect.signature(ocl_cst_InitOrDerValueCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CollectionLiteralPartCS)


def test_ocl_cst_collectionliteralpartcs_constructor_exists():
    assert callable(ocl_cst_CollectionLiteralPartCS.__init__)


def test_ocl_cst_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(ocl_cst_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_packagedeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_PackageDeclarationCS)


def test_ocl_cst_packagedeclarationcs_constructor_exists():
    assert callable(ocl_cst_PackageDeclarationCS.__init__)


def test_ocl_cst_packagedeclarationcs_constructor_args():
    sig = inspect.signature(ocl_cst_PackageDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_ocl_cst_cstnode_is_not_abstract():
    assert not inspect.isabstract(ocl_cst_CSTNode)


def test_ocl_cst_cstnode_constructor_exists():
    assert callable(ocl_cst_CSTNode.__init__)


def test_ocl_cst_cstnode_constructor_args():
    sig = inspect.signature(ocl_cst_CSTNode.__init__)
    params = list(sig.parameters.keys())
    assert "ast" in params, "Missing parameter 'ast'"
    assert "endToken" in params, "Missing parameter 'endToken'"
    assert "endOffset" in params, "Missing parameter 'endOffset'"
    assert "startToken" in params, "Missing parameter 'startToken'"
    assert "startOffset" in params, "Missing parameter 'startOffset'"

def test_ocl_cst_cstnode_has_ast():
    assert hasattr(ocl_cst_CSTNode, "ast")
    descriptor = None
    for klass in ocl_cst_CSTNode.__mro__:
        if "ast" in klass.__dict__:
            descriptor = klass.__dict__["ast"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_cstnode_has_endToken():
    assert hasattr(ocl_cst_CSTNode, "endToken")
    descriptor = None
    for klass in ocl_cst_CSTNode.__mro__:
        if "endToken" in klass.__dict__:
            descriptor = klass.__dict__["endToken"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_cstnode_has_endOffset():
    assert hasattr(ocl_cst_CSTNode, "endOffset")
    descriptor = None
    for klass in ocl_cst_CSTNode.__mro__:
        if "endOffset" in klass.__dict__:
            descriptor = klass.__dict__["endOffset"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_cstnode_has_startToken():
    assert hasattr(ocl_cst_CSTNode, "startToken")
    descriptor = None
    for klass in ocl_cst_CSTNode.__mro__:
        if "startToken" in klass.__dict__:
            descriptor = klass.__dict__["startToken"]
            break
    assert isinstance(descriptor, property)

def test_ocl_cst_cstnode_has_startOffset():
    assert hasattr(ocl_cst_CSTNode, "startOffset")
    descriptor = None
    for klass in ocl_cst_CSTNode.__mro__:
        if "startOffset" in klass.__dict__:
            descriptor = klass.__dict__["startOffset"]
            break
    assert isinstance(descriptor, property)

def test_messageexpkind_exists():
    # Check that the Enumeration exists
    assert MessageExpKind is not None

def test_messageexpkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageExpKind]
    expected_literals = [
        "hasSent",
        "sent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageExpKind"

def test_dotorarrowenum_exists():
    # Check that the Enumeration exists
    assert DotOrArrowEnum is not None

def test_dotorarrowenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DotOrArrowEnum]
    expected_literals = [
        "dot",
        "none",
        "arrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DotOrArrowEnum"

def test_prepostorbodyenum_exists():
    # Check that the Enumeration exists
    assert PrePostOrBodyEnum is not None

def test_prepostorbodyenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrePostOrBodyEnum]
    expected_literals = [
        "post",
        "body",
        "pre",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrePostOrBodyEnum"

def test_simpletypeenum_exists():
    # Check that the Enumeration exists
    assert SimpleTypeEnum is not None

def test_simpletypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleTypeEnum]
    expected_literals = [
        "identifier",
        "Boolean",
        "OclVoid",
        "OclInvalid",
        "String",
        "Real",
        "OclAny",
        "keyword",
        "UnlimitedNatural",
        "OclMessage",
        "self",
        "Integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleTypeEnum"

def test_collectiontypeidentifierenum_exists():
    # Check that the Enumeration exists
    assert CollectionTypeIdentifierEnum is not None

def test_collectiontypeidentifierenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionTypeIdentifierEnum]
    expected_literals = [
        "Collection",
        "Set",
        "Bag",
        "OrderedSet",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionTypeIdentifierEnum"


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
FeatureCallExpCS_strategy = st.builds(
    FeatureCallExpCS,
)
ocl_cst_OperationCallExpCS_strategy = st.builds(
    ocl_cst_OperationCallExpCS,
    isAtomic=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
ocl_cst_IterateExpCS_strategy = st.builds(
    ocl_cst_IterateExpCS,
)
ocl_cst_IteratorExpCS_strategy = st.builds(
    ocl_cst_IteratorExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
ocl_cst_FeatureCallExpCS_strategy = st.builds(
    ocl_cst_FeatureCallExpCS,
)
ocl_cst_LoopExpCS_strategy = st.builds(
    ocl_cst_LoopExpCS,
)
CollectionLiteralPartCS_strategy = st.builds(
    CollectionLiteralPartCS,
)
ocl_cst_CollectionRangeCS_strategy = st.builds(
    ocl_cst_CollectionRangeCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
ocl_cst_PrimitiveLiteralExpCS_strategy = st.builds(
    ocl_cst_PrimitiveLiteralExpCS,
    symbol=
        safe_text
)
ocl_cst_TupleLiteralExpCS_strategy = st.builds(
    ocl_cst_TupleLiteralExpCS,
)
ocl_cst_CollectionLiteralExpCS_strategy = st.builds(
    ocl_cst_CollectionLiteralExpCS,
    collectionType=
        safe_text
)
cst_LiteralExpCS_strategy = st.builds(
    cst_LiteralExpCS,
)
cst_PrimitiveLiteralExpCS_strategy = st.builds(
    cst_PrimitiveLiteralExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
ocl_cst_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    ocl_cst_UnlimitedNaturalLiteralExpCS,
    integerSymbol=
        safe_text,
    extendedIntegerSymbol=
        safe_text,
    longSymbol=
        safe_text
)
ocl_cst_StringLiteralExpCS_strategy = st.builds(
    ocl_cst_StringLiteralExpCS,
    stringSymbol=
        safe_text,
    unescapedStringSymbol=
        safe_text
)
ocl_cst_RealLiteralExpCS_strategy = st.builds(
    ocl_cst_RealLiteralExpCS,
    realSymbol=
        safe_text
)
ocl_cst_IntegerLiteralExpCS_strategy = st.builds(
    ocl_cst_IntegerLiteralExpCS,
    extendedIntegerSymbol=
        safe_text,
    integerSymbol=
        safe_text,
    longSymbol=
        safe_text
)
cst_TypeCS_strategy = st.builds(
    cst_TypeCS,
)
cst_SimpleNameCS_strategy = st.builds(
    cst_SimpleNameCS,
)
ocl_cst_BooleanLiteralExpCS_strategy = st.builds(
    ocl_cst_BooleanLiteralExpCS,
    booleanSymbol=
        safe_text
)
ocl_cst_InvalidLiteralExpCS_strategy = st.builds(
    ocl_cst_InvalidLiteralExpCS,
)
ocl_cst_NullLiteralExpCS_strategy = st.builds(
    ocl_cst_NullLiteralExpCS,
)
ocl_cst_CollectionTypeCS_strategy = st.builds(
    ocl_cst_CollectionTypeCS,
    collectionTypeIdentifier=
        safe_text
)
ocl_cst_PrimitiveTypeCS_strategy = st.builds(
    ocl_cst_PrimitiveTypeCS,
)
IsMarkedPreCS_strategy = st.builds(
    IsMarkedPreCS,
)
OCLMessageArgCS_strategy = st.builds(
    OCLMessageArgCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
PrePostOrBodyDeclCS_strategy = st.builds(
    PrePostOrBodyDeclCS,
)
OperationCS_strategy = st.builds(
    OperationCS,
)
DefExpressionCS_strategy = st.builds(
    DefExpressionCS,
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
ocl_cst_SimpleNameCS_strategy = st.builds(
    ocl_cst_SimpleNameCS,
    type=
        safe_text,
    value=
        safe_text
)
ocl_cst_VariableExpCS_strategy = st.builds(
    ocl_cst_VariableExpCS,
)
ocl_cst_LetExpCS_strategy = st.builds(
    ocl_cst_LetExpCS,
)
ocl_cst_LiteralExpCS_strategy = st.builds(
    ocl_cst_LiteralExpCS,
)
ocl_cst_CallExpCS_strategy = st.builds(
    ocl_cst_CallExpCS,
    accessor=
        safe_text
)
ocl_cst_IfExpCS_strategy = st.builds(
    ocl_cst_IfExpCS,
)
ocl_cst_MessageExpCS_strategy = st.builds(
    ocl_cst_MessageExpCS,
    kind=
        safe_text
)
ocl_cst_TypeCS_strategy = st.builds(
    ocl_cst_TypeCS,
)
SimpleNameCS_strategy = st.builds(
    SimpleNameCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
ocl_cst_TupleTypeCS_strategy = st.builds(
    ocl_cst_TupleTypeCS,
)
ocl_cst_PathNameCS_strategy = st.builds(
    ocl_cst_PathNameCS,
)
PackageDeclarationCS_strategy = st.builds(
    PackageDeclarationCS,
)
ContextDeclCS_strategy = st.builds(
    ContextDeclCS,
)
ocl_cst_OperationContextDeclCS_strategy = st.builds(
    ocl_cst_OperationContextDeclCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
InvOrDefCS_strategy = st.builds(
    InvOrDefCS,
)
ocl_cst_InvCS_strategy = st.builds(
    ocl_cst_InvCS,
)
ocl_cst_DefCS_strategy = st.builds(
    ocl_cst_DefCS,
    static=
        st.booleans()
)
ocl_cst_ClassifierContextDeclCS_strategy = st.builds(
    ocl_cst_ClassifierContextDeclCS,
)
InitOrDerValueCS_strategy = st.builds(
    InitOrDerValueCS,
)
ocl_cst_DerValueCS_strategy = st.builds(
    ocl_cst_DerValueCS,
)
ocl_cst_InitValueCS_strategy = st.builds(
    ocl_cst_InitValueCS,
)
ocl_cst_PropertyContextCS_strategy = st.builds(
    ocl_cst_PropertyContextCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
ocl_cst_PrePostOrBodyDeclCS_strategy = st.builds(
    ocl_cst_PrePostOrBodyDeclCS,
    kind=
        safe_text
)
ocl_cst_OCLMessageArgCS_strategy = st.builds(
    ocl_cst_OCLMessageArgCS,
)
ocl_cst_IsMarkedPreCS_strategy = st.builds(
    ocl_cst_IsMarkedPreCS,
)
ocl_cst_InvOrDefCS_strategy = st.builds(
    ocl_cst_InvOrDefCS,
)
ocl_cst_OCLDocumentCS_strategy = st.builds(
    ocl_cst_OCLDocumentCS,
)
ocl_cst_VariableCS_strategy = st.builds(
    ocl_cst_VariableCS,
    name=
        safe_text
)
ocl_cst_OperationCS_strategy = st.builds(
    ocl_cst_OperationCS,
)
ocl_cst_OCLExpressionCS_strategy = st.builds(
    ocl_cst_OCLExpressionCS,
)
ocl_cst_DefExpressionCS_strategy = st.builds(
    ocl_cst_DefExpressionCS,
)
ocl_cst_ContextDeclCS_strategy = st.builds(
    ocl_cst_ContextDeclCS,
)
ocl_cst_InitOrDerValueCS_strategy = st.builds(
    ocl_cst_InitOrDerValueCS,
)
ocl_cst_CollectionLiteralPartCS_strategy = st.builds(
    ocl_cst_CollectionLiteralPartCS,
)
ocl_cst_PackageDeclarationCS_strategy = st.builds(
    ocl_cst_PackageDeclarationCS,
)
ocl_cst_CSTNode_strategy = st.builds(
    ocl_cst_CSTNode,
    ast=
        safe_text,
    endToken=
        safe_text,
    endOffset=
        st.integers(),
    startToken=
        safe_text,
    startOffset=
        st.integers()
)

@given(instance=FeatureCallExpCS_strategy)
@settings(max_examples=50)
def test_featurecallexpcs_instantiation(instance):
    assert isinstance(instance, FeatureCallExpCS)

@given(instance=ocl_cst_OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OperationCallExpCS)



@given(instance=ocl_cst_OperationCallExpCS_strategy)
def test_ocl_cst_operationcallexpcs_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=ocl_cst_IterateExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_iterateexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_IterateExpCS)

@given(instance=ocl_cst_IteratorExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_iteratorexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_IteratorExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=ocl_cst_FeatureCallExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_featurecallexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_FeatureCallExpCS)

@given(instance=ocl_cst_LoopExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_loopexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_LoopExpCS)

@given(instance=CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPartCS)

@given(instance=ocl_cst_CollectionRangeCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_collectionrangecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_CollectionRangeCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=ocl_cst_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PrimitiveLiteralExpCS)



@given(instance=ocl_cst_PrimitiveLiteralExpCS_strategy)
def test_ocl_cst_primitiveliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=ocl_cst_TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_TupleLiteralExpCS)

@given(instance=ocl_cst_CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_CollectionLiteralExpCS)



@given(instance=ocl_cst_CollectionLiteralExpCS_strategy)
def test_ocl_cst_collectionliteralexpcs_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original

@given(instance=cst_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_cst_literalexpcs_instantiation(instance):
    assert isinstance(instance, cst_LiteralExpCS)

@given(instance=cst_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_cst_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, cst_PrimitiveLiteralExpCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=ocl_cst_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_UnlimitedNaturalLiteralExpCS)



@given(instance=ocl_cst_UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl_cst_unlimitednaturalliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original



@given(instance=ocl_cst_UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl_cst_unlimitednaturalliteralexpcs_extendedIntegerSymbol_setter(instance):
    original = instance.extendedIntegerSymbol
    instance.extendedIntegerSymbol = original
    assert instance.extendedIntegerSymbol == original



@given(instance=ocl_cst_UnlimitedNaturalLiteralExpCS_strategy)
def test_ocl_cst_unlimitednaturalliteralexpcs_longSymbol_setter(instance):
    original = instance.longSymbol
    instance.longSymbol = original
    assert instance.longSymbol == original

@given(instance=ocl_cst_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_StringLiteralExpCS)



@given(instance=ocl_cst_StringLiteralExpCS_strategy)
def test_ocl_cst_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original



@given(instance=ocl_cst_StringLiteralExpCS_strategy)
def test_ocl_cst_stringliteralexpcs_unescapedStringSymbol_setter(instance):
    original = instance.unescapedStringSymbol
    instance.unescapedStringSymbol = original
    assert instance.unescapedStringSymbol == original

@given(instance=ocl_cst_RealLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_realliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_RealLiteralExpCS)



@given(instance=ocl_cst_RealLiteralExpCS_strategy)
def test_ocl_cst_realliteralexpcs_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=ocl_cst_IntegerLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_integerliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_IntegerLiteralExpCS)



@given(instance=ocl_cst_IntegerLiteralExpCS_strategy)
def test_ocl_cst_integerliteralexpcs_extendedIntegerSymbol_setter(instance):
    original = instance.extendedIntegerSymbol
    instance.extendedIntegerSymbol = original
    assert instance.extendedIntegerSymbol == original



@given(instance=ocl_cst_IntegerLiteralExpCS_strategy)
def test_ocl_cst_integerliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original



@given(instance=ocl_cst_IntegerLiteralExpCS_strategy)
def test_ocl_cst_integerliteralexpcs_longSymbol_setter(instance):
    original = instance.longSymbol
    instance.longSymbol = original
    assert instance.longSymbol == original

@given(instance=cst_TypeCS_strategy)
@settings(max_examples=50)
def test_cst_typecs_instantiation(instance):
    assert isinstance(instance, cst_TypeCS)

@given(instance=cst_SimpleNameCS_strategy)
@settings(max_examples=50)
def test_cst_simplenamecs_instantiation(instance):
    assert isinstance(instance, cst_SimpleNameCS)

@given(instance=ocl_cst_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_BooleanLiteralExpCS)



@given(instance=ocl_cst_BooleanLiteralExpCS_strategy)
def test_ocl_cst_booleanliteralexpcs_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=ocl_cst_InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_InvalidLiteralExpCS)

@given(instance=ocl_cst_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_NullLiteralExpCS)

@given(instance=ocl_cst_CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_collectiontypecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_CollectionTypeCS)



@given(instance=ocl_cst_CollectionTypeCS_strategy)
def test_ocl_cst_collectiontypecs_collectionTypeIdentifier_setter(instance):
    original = instance.collectionTypeIdentifier
    instance.collectionTypeIdentifier = original
    assert instance.collectionTypeIdentifier == original

@given(instance=ocl_cst_PrimitiveTypeCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_primitivetypecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PrimitiveTypeCS)

@given(instance=IsMarkedPreCS_strategy)
@settings(max_examples=50)
def test_ismarkedprecs_instantiation(instance):
    assert isinstance(instance, IsMarkedPreCS)

@given(instance=OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_oclmessageargcs_instantiation(instance):
    assert isinstance(instance, OCLMessageArgCS)

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=PrePostOrBodyDeclCS_strategy)
@settings(max_examples=50)
def test_prepostorbodydeclcs_instantiation(instance):
    assert isinstance(instance, PrePostOrBodyDeclCS)

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=DefExpressionCS_strategy)
@settings(max_examples=50)
def test_defexpressioncs_instantiation(instance):
    assert isinstance(instance, DefExpressionCS)

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=ocl_cst_SimpleNameCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_simplenamecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_SimpleNameCS)



@given(instance=ocl_cst_SimpleNameCS_strategy)
def test_ocl_cst_simplenamecs_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ocl_cst_SimpleNameCS_strategy)
def test_ocl_cst_simplenamecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ocl_cst_VariableExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_variableexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_VariableExpCS)

@given(instance=ocl_cst_LetExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_letexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_LetExpCS)

@given(instance=ocl_cst_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_literalexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_LiteralExpCS)

@given(instance=ocl_cst_CallExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_callexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_CallExpCS)



@given(instance=ocl_cst_CallExpCS_strategy)
def test_ocl_cst_callexpcs_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=ocl_cst_IfExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_ifexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_IfExpCS)

@given(instance=ocl_cst_MessageExpCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_messageexpcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_MessageExpCS)



@given(instance=ocl_cst_MessageExpCS_strategy)
def test_ocl_cst_messageexpcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl_cst_TypeCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_typecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_TypeCS)

@given(instance=SimpleNameCS_strategy)
@settings(max_examples=50)
def test_simplenamecs_instantiation(instance):
    assert isinstance(instance, SimpleNameCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=ocl_cst_TupleTypeCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_tupletypecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_TupleTypeCS)

@given(instance=ocl_cst_PathNameCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_pathnamecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PathNameCS)

@given(instance=PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, PackageDeclarationCS)

@given(instance=ContextDeclCS_strategy)
@settings(max_examples=50)
def test_contextdeclcs_instantiation(instance):
    assert isinstance(instance, ContextDeclCS)

@given(instance=ocl_cst_OperationContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_operationcontextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OperationContextDeclCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=InvOrDefCS_strategy)
@settings(max_examples=50)
def test_invordefcs_instantiation(instance):
    assert isinstance(instance, InvOrDefCS)

@given(instance=ocl_cst_InvCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_invcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_InvCS)

@given(instance=ocl_cst_DefCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_defcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_DefCS)



@given(instance=ocl_cst_DefCS_strategy)
def test_ocl_cst_defcs_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ocl_cst_ClassifierContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_classifiercontextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_ClassifierContextDeclCS)

@given(instance=InitOrDerValueCS_strategy)
@settings(max_examples=50)
def test_initordervaluecs_instantiation(instance):
    assert isinstance(instance, InitOrDerValueCS)

@given(instance=ocl_cst_DerValueCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_dervaluecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_DerValueCS)

@given(instance=ocl_cst_InitValueCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_initvaluecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_InitValueCS)

@given(instance=ocl_cst_PropertyContextCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_propertycontextcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PropertyContextCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=ocl_cst_PrePostOrBodyDeclCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_prepostorbodydeclcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PrePostOrBodyDeclCS)



@given(instance=ocl_cst_PrePostOrBodyDeclCS_strategy)
def test_ocl_cst_prepostorbodydeclcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ocl_cst_OCLMessageArgCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_oclmessageargcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OCLMessageArgCS)

@given(instance=ocl_cst_IsMarkedPreCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_ismarkedprecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_IsMarkedPreCS)

@given(instance=ocl_cst_InvOrDefCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_invordefcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_InvOrDefCS)

@given(instance=ocl_cst_OCLDocumentCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_ocldocumentcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OCLDocumentCS)

@given(instance=ocl_cst_VariableCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_variablecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_VariableCS)



@given(instance=ocl_cst_VariableCS_strategy)
def test_ocl_cst_variablecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl_cst_OperationCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_operationcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OperationCS)

@given(instance=ocl_cst_OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, ocl_cst_OCLExpressionCS)

@given(instance=ocl_cst_DefExpressionCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_defexpressioncs_instantiation(instance):
    assert isinstance(instance, ocl_cst_DefExpressionCS)

@given(instance=ocl_cst_ContextDeclCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_contextdeclcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_ContextDeclCS)

@given(instance=ocl_cst_InitOrDerValueCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_initordervaluecs_instantiation(instance):
    assert isinstance(instance, ocl_cst_InitOrDerValueCS)

@given(instance=ocl_cst_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_CollectionLiteralPartCS)

@given(instance=ocl_cst_PackageDeclarationCS_strategy)
@settings(max_examples=50)
def test_ocl_cst_packagedeclarationcs_instantiation(instance):
    assert isinstance(instance, ocl_cst_PackageDeclarationCS)

@given(instance=ocl_cst_CSTNode_strategy)
@settings(max_examples=50)
def test_ocl_cst_cstnode_instantiation(instance):
    assert isinstance(instance, ocl_cst_CSTNode)



@given(instance=ocl_cst_CSTNode_strategy)
def test_ocl_cst_cstnode_ast_setter(instance):
    original = instance.ast
    instance.ast = original
    assert instance.ast == original



@given(instance=ocl_cst_CSTNode_strategy)
def test_ocl_cst_cstnode_endToken_setter(instance):
    original = instance.endToken
    instance.endToken = original
    assert instance.endToken == original



@given(instance=ocl_cst_CSTNode_strategy)
def test_ocl_cst_cstnode_endOffset_setter(instance):
    original = instance.endOffset
    instance.endOffset = original
    assert instance.endOffset == original



@given(instance=ocl_cst_CSTNode_strategy)
def test_ocl_cst_cstnode_startToken_setter(instance):
    original = instance.startToken
    instance.startToken = original
    assert instance.startToken == original



@given(instance=ocl_cst_CSTNode_strategy)
def test_ocl_cst_cstnode_startOffset_setter(instance):
    original = instance.startOffset
    instance.startOffset = original
    assert instance.startOffset == original
