import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VariableExpCS,
    essentialOCLCST_CallArgumentsCS,
    PrimitiveLiteralExpCS,
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
    essentialOCLCST_RealLiteralExpCS,
    essentialOCLCST_NullLiteralExpCS,
    essentialOCLCST_StringLiteralExpCS,
    essentialOCLCST_BooleanLiteralExpCS,
    OclExpressionCS,
    essentialOCLCST_LiteralExpCS,
    essentialOCLCST_VariableExpCS,
    essentialOCLCST_UnaryExpressionCS,
    essentialOCLCST_LetExpCS,
    essentialOCLCST_InvalidLiteralExpCS,
    essentialOCLCST_IntegerLiteralExpCS,
    essentialOCLCST_IfExpCS,
    essentialOCLCST_TypeCS,
    TypeLiteralExpCS,
    CollectionLiteralExpCS,
    TypeCS,
    essentialOCLCST_PathNameCS,
    essentialOCLCST_SimpleNameCS,
    essentialOCLCST_TupleTypeCS,
    essentialOCLCST_CollectionTypeCS,
    essentialOCLCST_CollectionLiteralPartCS,
    LiteralExpCS,
    essentialOCLCST_PrimitiveLiteralExpCS,
    essentialOCLCST_TupleLiteralExpCS,
    essentialOCLCST_TypeLiteralExpCS,
    essentialOCLCST_CollectionLiteralExpCS,
    essentialOCLCST_CallExpCS,
    essentialOCLCST_BinaryExpressionCS,
    essentialOCLCST_OclExpressionCS,
    essentialOCLCST_VariableCS,
    CallArgumentsCS,
    essentialOCLCST_DotIndexArgumentsCS,
    essentialOCLCST_ArrowCallArgumentsCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(VariableExpCS)


def test_variableexpcs_constructor_exists():
    assert callable(VariableExpCS.__init__)


def test_variableexpcs_constructor_args():
    sig = inspect.signature(VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_callargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CallArgumentsCS)


def test_essentialoclcst_callargumentscs_constructor_exists():
    assert callable(essentialOCLCST_CallArgumentsCS.__init__)


def test_essentialoclcst_callargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_UnlimitedNaturalLiteralExpCS)


def test_essentialoclcst_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcst_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_realliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_RealLiteralExpCS)


def test_essentialoclcst_realliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_RealLiteralExpCS.__init__)


def test_essentialoclcst_realliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_RealLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialoclcst_realliteralexpcs_has_realSymbol():
    assert hasattr(essentialOCLCST_RealLiteralExpCS, "realSymbol")
    descriptor = None
    for klass in essentialOCLCST_RealLiteralExpCS.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_NullLiteralExpCS)


def test_essentialoclcst_nullliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_NullLiteralExpCS.__init__)


def test_essentialoclcst_nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_StringLiteralExpCS)


def test_essentialoclcst_stringliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_StringLiteralExpCS.__init__)


def test_essentialoclcst_stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialoclcst_stringliteralexpcs_has_stringSymbol():
    assert hasattr(essentialOCLCST_StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in essentialOCLCST_StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_BooleanLiteralExpCS)


def test_essentialoclcst_booleanliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_BooleanLiteralExpCS.__init__)


def test_essentialoclcst_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst_booleanliteralexpcs_has_value():
    assert hasattr(essentialOCLCST_BooleanLiteralExpCS, "value")
    descriptor = None
    for klass in essentialOCLCST_BooleanLiteralExpCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OclExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OclExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_LiteralExpCS)


def test_essentialoclcst_literalexpcs_constructor_exists():
    assert callable(essentialOCLCST_LiteralExpCS.__init__)


def test_essentialoclcst_literalexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_VariableExpCS)


def test_essentialoclcst_variableexpcs_constructor_exists():
    assert callable(essentialOCLCST_VariableExpCS.__init__)


def test_essentialoclcst_variableexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_unaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_UnaryExpressionCS)


def test_essentialoclcst_unaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_UnaryExpressionCS.__init__)


def test_essentialoclcst_unaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_UnaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_essentialoclcst_unaryexpressioncs_has_op():
    assert hasattr(essentialOCLCST_UnaryExpressionCS, "op")
    descriptor = None
    for klass in essentialOCLCST_UnaryExpressionCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_LetExpCS)


def test_essentialoclcst_letexpcs_constructor_exists():
    assert callable(essentialOCLCST_LetExpCS.__init__)


def test_essentialoclcst_letexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_InvalidLiteralExpCS)


def test_essentialoclcst_invalidliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_InvalidLiteralExpCS.__init__)


def test_essentialoclcst_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_integerliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_IntegerLiteralExpCS)


def test_essentialoclcst_integerliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_IntegerLiteralExpCS.__init__)


def test_essentialoclcst_integerliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_IntegerLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialoclcst_integerliteralexpcs_has_integerSymbol():
    assert hasattr(essentialOCLCST_IntegerLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in essentialOCLCST_IntegerLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_IfExpCS)


def test_essentialoclcst_ifexpcs_constructor_exists():
    assert callable(essentialOCLCST_IfExpCS.__init__)


def test_essentialoclcst_ifexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_typecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TypeCS)


def test_essentialoclcst_typecs_constructor_exists():
    assert callable(essentialOCLCST_TypeCS.__init__)


def test_essentialoclcst_typecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(TypeLiteralExpCS)


def test_typeliteralexpcs_constructor_exists():
    assert callable(TypeLiteralExpCS.__init__)


def test_typeliteralexpcs_constructor_args():
    sig = inspect.signature(TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExpCS)


def test_collectionliteralexpcs_constructor_exists():
    assert callable(CollectionLiteralExpCS.__init__)


def test_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_PathNameCS)


def test_essentialoclcst_pathnamecs_constructor_exists():
    assert callable(essentialOCLCST_PathNameCS.__init__)


def test_essentialoclcst_pathnamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_SimpleNameCS)


def test_essentialoclcst_simplenamecs_constructor_exists():
    assert callable(essentialOCLCST_SimpleNameCS.__init__)


def test_essentialoclcst_simplenamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_SimpleNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst_simplenamecs_has_value():
    assert hasattr(essentialOCLCST_SimpleNameCS, "value")
    descriptor = None
    for klass in essentialOCLCST_SimpleNameCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TupleTypeCS)


def test_essentialoclcst_tupletypecs_constructor_exists():
    assert callable(essentialOCLCST_TupleTypeCS.__init__)


def test_essentialoclcst_tupletypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst_tupletypecs_has_value():
    assert hasattr(essentialOCLCST_TupleTypeCS, "value")
    descriptor = None
    for klass in essentialOCLCST_TupleTypeCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionTypeCS)


def test_essentialoclcst_collectiontypecs_constructor_exists():
    assert callable(essentialOCLCST_CollectionTypeCS.__init__)


def test_essentialoclcst_collectiontypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionLiteralPartCS)


def test_essentialoclcst_collectionliteralpartcs_constructor_exists():
    assert callable(essentialOCLCST_CollectionLiteralPartCS.__init__)


def test_essentialoclcst_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_PrimitiveLiteralExpCS)


def test_essentialoclcst_primitiveliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_PrimitiveLiteralExpCS.__init__)


def test_essentialoclcst_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TupleLiteralExpCS)


def test_essentialoclcst_tupleliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_TupleLiteralExpCS.__init__)


def test_essentialoclcst_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_TypeLiteralExpCS)


def test_essentialoclcst_typeliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_TypeLiteralExpCS.__init__)


def test_essentialoclcst_typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CollectionLiteralExpCS)


def test_essentialoclcst_collectionliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST_CollectionLiteralExpCS.__init__)


def test_essentialoclcst_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_CallExpCS)


def test_essentialoclcst_callexpcs_constructor_exists():
    assert callable(essentialOCLCST_CallExpCS.__init__)


def test_essentialoclcst_callexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_binaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_BinaryExpressionCS)


def test_essentialoclcst_binaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_BinaryExpressionCS.__init__)


def test_essentialoclcst_binaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_BinaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_essentialoclcst_binaryexpressioncs_has_op():
    assert hasattr(essentialOCLCST_BinaryExpressionCS, "op")
    descriptor = None
    for klass in essentialOCLCST_BinaryExpressionCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_OclExpressionCS)


def test_essentialoclcst_oclexpressioncs_constructor_exists():
    assert callable(essentialOCLCST_OclExpressionCS.__init__)


def test_essentialoclcst_oclexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST_OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_VariableCS)


def test_essentialoclcst_variablecs_constructor_exists():
    assert callable(essentialOCLCST_VariableCS.__init__)


def test_essentialoclcst_variablecs_constructor_args():
    sig = inspect.signature(essentialOCLCST_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_callargumentscs_is_not_abstract():
    assert not inspect.isabstract(CallArgumentsCS)


def test_callargumentscs_constructor_exists():
    assert callable(CallArgumentsCS.__init__)


def test_callargumentscs_constructor_args():
    sig = inspect.signature(CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst_dotindexargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_DotIndexArgumentsCS)


def test_essentialoclcst_dotindexargumentscs_constructor_exists():
    assert callable(essentialOCLCST_DotIndexArgumentsCS.__init__)


def test_essentialoclcst_dotindexargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_DotIndexArgumentsCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_essentialoclcst_dotindexargumentscs_has_isPre():
    assert hasattr(essentialOCLCST_DotIndexArgumentsCS, "isPre")
    descriptor = None
    for klass in essentialOCLCST_DotIndexArgumentsCS.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst_arrowcallargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST_ArrowCallArgumentsCS)


def test_essentialoclcst_arrowcallargumentscs_constructor_exists():
    assert callable(essentialOCLCST_ArrowCallArgumentsCS.__init__)


def test_essentialoclcst_arrowcallargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST_ArrowCallArgumentsCS.__init__)
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
VariableExpCS_strategy = st.builds(
    VariableExpCS,
)
essentialOCLCST_CallArgumentsCS_strategy = st.builds(
    essentialOCLCST_CallArgumentsCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialOCLCST_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
)
essentialOCLCST_RealLiteralExpCS_strategy = st.builds(
    essentialOCLCST_RealLiteralExpCS,
    realSymbol=
        safe_text
)
essentialOCLCST_NullLiteralExpCS_strategy = st.builds(
    essentialOCLCST_NullLiteralExpCS,
)
essentialOCLCST_StringLiteralExpCS_strategy = st.builds(
    essentialOCLCST_StringLiteralExpCS,
    stringSymbol=
        safe_text
)
essentialOCLCST_BooleanLiteralExpCS_strategy = st.builds(
    essentialOCLCST_BooleanLiteralExpCS,
    value=
        safe_text
)
OclExpressionCS_strategy = st.builds(
    OclExpressionCS,
)
essentialOCLCST_LiteralExpCS_strategy = st.builds(
    essentialOCLCST_LiteralExpCS,
)
essentialOCLCST_VariableExpCS_strategy = st.builds(
    essentialOCLCST_VariableExpCS,
)
essentialOCLCST_UnaryExpressionCS_strategy = st.builds(
    essentialOCLCST_UnaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST_LetExpCS_strategy = st.builds(
    essentialOCLCST_LetExpCS,
)
essentialOCLCST_InvalidLiteralExpCS_strategy = st.builds(
    essentialOCLCST_InvalidLiteralExpCS,
)
essentialOCLCST_IntegerLiteralExpCS_strategy = st.builds(
    essentialOCLCST_IntegerLiteralExpCS,
    integerSymbol=
        safe_text
)
essentialOCLCST_IfExpCS_strategy = st.builds(
    essentialOCLCST_IfExpCS,
)
essentialOCLCST_TypeCS_strategy = st.builds(
    essentialOCLCST_TypeCS,
)
TypeLiteralExpCS_strategy = st.builds(
    TypeLiteralExpCS,
)
CollectionLiteralExpCS_strategy = st.builds(
    CollectionLiteralExpCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
essentialOCLCST_PathNameCS_strategy = st.builds(
    essentialOCLCST_PathNameCS,
)
essentialOCLCST_SimpleNameCS_strategy = st.builds(
    essentialOCLCST_SimpleNameCS,
    value=
        safe_text
)
essentialOCLCST_TupleTypeCS_strategy = st.builds(
    essentialOCLCST_TupleTypeCS,
    value=
        safe_text
)
essentialOCLCST_CollectionTypeCS_strategy = st.builds(
    essentialOCLCST_CollectionTypeCS,
)
essentialOCLCST_CollectionLiteralPartCS_strategy = st.builds(
    essentialOCLCST_CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialOCLCST_PrimitiveLiteralExpCS_strategy = st.builds(
    essentialOCLCST_PrimitiveLiteralExpCS,
)
essentialOCLCST_TupleLiteralExpCS_strategy = st.builds(
    essentialOCLCST_TupleLiteralExpCS,
)
essentialOCLCST_TypeLiteralExpCS_strategy = st.builds(
    essentialOCLCST_TypeLiteralExpCS,
)
essentialOCLCST_CollectionLiteralExpCS_strategy = st.builds(
    essentialOCLCST_CollectionLiteralExpCS,
)
essentialOCLCST_CallExpCS_strategy = st.builds(
    essentialOCLCST_CallExpCS,
)
essentialOCLCST_BinaryExpressionCS_strategy = st.builds(
    essentialOCLCST_BinaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST_OclExpressionCS_strategy = st.builds(
    essentialOCLCST_OclExpressionCS,
)
essentialOCLCST_VariableCS_strategy = st.builds(
    essentialOCLCST_VariableCS,
)
CallArgumentsCS_strategy = st.builds(
    CallArgumentsCS,
)
essentialOCLCST_DotIndexArgumentsCS_strategy = st.builds(
    essentialOCLCST_DotIndexArgumentsCS,
    isPre=
        st.booleans()
)
essentialOCLCST_ArrowCallArgumentsCS_strategy = st.builds(
    essentialOCLCST_ArrowCallArgumentsCS,
)

@given(instance=VariableExpCS_strategy)
@settings(max_examples=50)
def test_variableexpcs_instantiation(instance):
    assert isinstance(instance, VariableExpCS)

@given(instance=essentialOCLCST_CallArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_callargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CallArgumentsCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialOCLCST_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_UnlimitedNaturalLiteralExpCS)

@given(instance=essentialOCLCST_RealLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_realliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_RealLiteralExpCS)



@given(instance=essentialOCLCST_RealLiteralExpCS_strategy)
def test_essentialoclcst_realliteralexpcs_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=essentialOCLCST_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_NullLiteralExpCS)

@given(instance=essentialOCLCST_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_StringLiteralExpCS)



@given(instance=essentialOCLCST_StringLiteralExpCS_strategy)
def test_essentialoclcst_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=essentialOCLCST_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_BooleanLiteralExpCS)



@given(instance=essentialOCLCST_BooleanLiteralExpCS_strategy)
def test_essentialoclcst_booleanliteralexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OclExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OclExpressionCS)

@given(instance=essentialOCLCST_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_LiteralExpCS)

@given(instance=essentialOCLCST_VariableExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_variableexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_VariableExpCS)

@given(instance=essentialOCLCST_UnaryExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_unaryexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_UnaryExpressionCS)



@given(instance=essentialOCLCST_UnaryExpressionCS_strategy)
def test_essentialoclcst_unaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=essentialOCLCST_LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_letexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_LetExpCS)

@given(instance=essentialOCLCST_InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_InvalidLiteralExpCS)

@given(instance=essentialOCLCST_IntegerLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_integerliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_IntegerLiteralExpCS)



@given(instance=essentialOCLCST_IntegerLiteralExpCS_strategy)
def test_essentialoclcst_integerliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=essentialOCLCST_IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_IfExpCS)

@given(instance=essentialOCLCST_TypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_typecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TypeCS)

@given(instance=TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, TypeLiteralExpCS)

@given(instance=CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExpCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=essentialOCLCST_PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_PathNameCS)

@given(instance=essentialOCLCST_SimpleNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_simplenamecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_SimpleNameCS)



@given(instance=essentialOCLCST_SimpleNameCS_strategy)
def test_essentialoclcst_simplenamecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialOCLCST_TupleTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_tupletypecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TupleTypeCS)



@given(instance=essentialOCLCST_TupleTypeCS_strategy)
def test_essentialoclcst_tupletypecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialOCLCST_CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionTypeCS)

@given(instance=essentialOCLCST_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionLiteralPartCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialOCLCST_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_PrimitiveLiteralExpCS)

@given(instance=essentialOCLCST_TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TupleLiteralExpCS)

@given(instance=essentialOCLCST_TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_TypeLiteralExpCS)

@given(instance=essentialOCLCST_CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CollectionLiteralExpCS)

@given(instance=essentialOCLCST_CallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_callexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_CallExpCS)

@given(instance=essentialOCLCST_BinaryExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_binaryexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_BinaryExpressionCS)



@given(instance=essentialOCLCST_BinaryExpressionCS_strategy)
def test_essentialoclcst_binaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=essentialOCLCST_OclExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_OclExpressionCS)

@given(instance=essentialOCLCST_VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_variablecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_VariableCS)

@given(instance=CallArgumentsCS_strategy)
@settings(max_examples=50)
def test_callargumentscs_instantiation(instance):
    assert isinstance(instance, CallArgumentsCS)

@given(instance=essentialOCLCST_DotIndexArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_dotindexargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_DotIndexArgumentsCS)



@given(instance=essentialOCLCST_DotIndexArgumentsCS_strategy)
def test_essentialoclcst_dotindexargumentscs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

@given(instance=essentialOCLCST_ArrowCallArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst_arrowcallargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST_ArrowCallArgumentsCS)
