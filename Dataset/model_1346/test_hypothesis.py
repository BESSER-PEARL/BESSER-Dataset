import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VariableExpCS,
    essentialOCLCST::CallArgumentsCS,
    PrimitiveLiteralExpCS,
    essentialOCLCST::StringLiteralExpCS,
    essentialOCLCST::UnlimitedNaturalLiteralExpCS,
    essentialOCLCST::RealLiteralExpCS,
    essentialOCLCST::NullLiteralExpCS,
    essentialOCLCST::BooleanLiteralExpCS,
    OclExpressionCS,
    essentialOCLCST::LiteralExpCS,
    essentialOCLCST::VariableExpCS,
    essentialOCLCST::UnaryExpressionCS,
    essentialOCLCST::LetExpCS,
    essentialOCLCST::InvalidLiteralExpCS,
    essentialOCLCST::IntegerLiteralExpCS,
    essentialOCLCST::IfExpCS,
    essentialOCLCST::TypeCS,
    TypeLiteralExpCS,
    CollectionLiteralExpCS,
    TypeCS,
    essentialOCLCST::TupleTypeCS,
    essentialOCLCST::SimpleNameCS,
    essentialOCLCST::PathNameCS,
    essentialOCLCST::CollectionTypeCS,
    essentialOCLCST::CollectionLiteralPartCS,
    LiteralExpCS,
    essentialOCLCST::TupleLiteralExpCS,
    essentialOCLCST::TypeLiteralExpCS,
    essentialOCLCST::PrimitiveLiteralExpCS,
    essentialOCLCST::CollectionLiteralExpCS,
    essentialOCLCST::CallExpCS,
    essentialOCLCST::BinaryExpressionCS,
    essentialOCLCST::OclExpressionCS,
    essentialOCLCST::VariableCS,
    CallArgumentsCS,
    essentialOCLCST::DotIndexArgumentsCS,
    essentialOCLCST::ArrowCallArgumentsCS,
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



def test_essentialoclcst::callargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::CallArgumentsCS)


def test_essentialoclcst::callargumentscs_constructor_exists():
    assert callable(essentialOCLCST::CallArgumentsCS.__init__)


def test_essentialoclcst::callargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST::CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::StringLiteralExpCS)


def test_essentialoclcst::stringliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::StringLiteralExpCS.__init__)


def test_essentialoclcst::stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialoclcst::stringliteralexpcs_has_stringSymbol():
    assert hasattr(essentialOCLCST::StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in essentialOCLCST::StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::UnlimitedNaturalLiteralExpCS)


def test_essentialoclcst::unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcst::unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::realliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::RealLiteralExpCS)


def test_essentialoclcst::realliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::RealLiteralExpCS.__init__)


def test_essentialoclcst::realliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::RealLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialoclcst::realliteralexpcs_has_realSymbol():
    assert hasattr(essentialOCLCST::RealLiteralExpCS, "realSymbol")
    descriptor = None
    for klass in essentialOCLCST::RealLiteralExpCS.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::NullLiteralExpCS)


def test_essentialoclcst::nullliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::NullLiteralExpCS.__init__)


def test_essentialoclcst::nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::BooleanLiteralExpCS)


def test_essentialoclcst::booleanliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::BooleanLiteralExpCS.__init__)


def test_essentialoclcst::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst::booleanliteralexpcs_has_value():
    assert hasattr(essentialOCLCST::BooleanLiteralExpCS, "value")
    descriptor = None
    for klass in essentialOCLCST::BooleanLiteralExpCS.__mro__:
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



def test_essentialoclcst::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::LiteralExpCS)


def test_essentialoclcst::literalexpcs_constructor_exists():
    assert callable(essentialOCLCST::LiteralExpCS.__init__)


def test_essentialoclcst::literalexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::VariableExpCS)


def test_essentialoclcst::variableexpcs_constructor_exists():
    assert callable(essentialOCLCST::VariableExpCS.__init__)


def test_essentialoclcst::variableexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::unaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::UnaryExpressionCS)


def test_essentialoclcst::unaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST::UnaryExpressionCS.__init__)


def test_essentialoclcst::unaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST::UnaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_essentialoclcst::unaryexpressioncs_has_op():
    assert hasattr(essentialOCLCST::UnaryExpressionCS, "op")
    descriptor = None
    for klass in essentialOCLCST::UnaryExpressionCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::LetExpCS)


def test_essentialoclcst::letexpcs_constructor_exists():
    assert callable(essentialOCLCST::LetExpCS.__init__)


def test_essentialoclcst::letexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::InvalidLiteralExpCS)


def test_essentialoclcst::invalidliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::InvalidLiteralExpCS.__init__)


def test_essentialoclcst::invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::integerliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::IntegerLiteralExpCS)


def test_essentialoclcst::integerliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::IntegerLiteralExpCS.__init__)


def test_essentialoclcst::integerliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::IntegerLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialoclcst::integerliteralexpcs_has_integerSymbol():
    assert hasattr(essentialOCLCST::IntegerLiteralExpCS, "integerSymbol")
    descriptor = None
    for klass in essentialOCLCST::IntegerLiteralExpCS.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::IfExpCS)


def test_essentialoclcst::ifexpcs_constructor_exists():
    assert callable(essentialOCLCST::IfExpCS.__init__)


def test_essentialoclcst::ifexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::typecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::TypeCS)


def test_essentialoclcst::typecs_constructor_exists():
    assert callable(essentialOCLCST::TypeCS.__init__)


def test_essentialoclcst::typecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::TypeCS.__init__)
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



def test_essentialoclcst::tupletypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::TupleTypeCS)


def test_essentialoclcst::tupletypecs_constructor_exists():
    assert callable(essentialOCLCST::TupleTypeCS.__init__)


def test_essentialoclcst::tupletypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst::tupletypecs_has_value():
    assert hasattr(essentialOCLCST::TupleTypeCS, "value")
    descriptor = None
    for klass in essentialOCLCST::TupleTypeCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::simplenamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::SimpleNameCS)


def test_essentialoclcst::simplenamecs_constructor_exists():
    assert callable(essentialOCLCST::SimpleNameCS.__init__)


def test_essentialoclcst::simplenamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::SimpleNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcst::simplenamecs_has_value():
    assert hasattr(essentialOCLCST::SimpleNameCS, "value")
    descriptor = None
    for klass in essentialOCLCST::SimpleNameCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::PathNameCS)


def test_essentialoclcst::pathnamecs_constructor_exists():
    assert callable(essentialOCLCST::PathNameCS.__init__)


def test_essentialoclcst::pathnamecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::CollectionTypeCS)


def test_essentialoclcst::collectiontypecs_constructor_exists():
    assert callable(essentialOCLCST::CollectionTypeCS.__init__)


def test_essentialoclcst::collectiontypecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::CollectionLiteralPartCS)


def test_essentialoclcst::collectionliteralpartcs_constructor_exists():
    assert callable(essentialOCLCST::CollectionLiteralPartCS.__init__)


def test_essentialoclcst::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::TupleLiteralExpCS)


def test_essentialoclcst::tupleliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::TupleLiteralExpCS.__init__)


def test_essentialoclcst::tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::TypeLiteralExpCS)


def test_essentialoclcst::typeliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::TypeLiteralExpCS.__init__)


def test_essentialoclcst::typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::PrimitiveLiteralExpCS)


def test_essentialoclcst::primitiveliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::PrimitiveLiteralExpCS.__init__)


def test_essentialoclcst::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::CollectionLiteralExpCS)


def test_essentialoclcst::collectionliteralexpcs_constructor_exists():
    assert callable(essentialOCLCST::CollectionLiteralExpCS.__init__)


def test_essentialoclcst::collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::CallExpCS)


def test_essentialoclcst::callexpcs_constructor_exists():
    assert callable(essentialOCLCST::CallExpCS.__init__)


def test_essentialoclcst::callexpcs_constructor_args():
    sig = inspect.signature(essentialOCLCST::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::binaryexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::BinaryExpressionCS)


def test_essentialoclcst::binaryexpressioncs_constructor_exists():
    assert callable(essentialOCLCST::BinaryExpressionCS.__init__)


def test_essentialoclcst::binaryexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST::BinaryExpressionCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_essentialoclcst::binaryexpressioncs_has_op():
    assert hasattr(essentialOCLCST::BinaryExpressionCS, "op")
    descriptor = None
    for klass in essentialOCLCST::BinaryExpressionCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::OclExpressionCS)


def test_essentialoclcst::oclexpressioncs_constructor_exists():
    assert callable(essentialOCLCST::OclExpressionCS.__init__)


def test_essentialoclcst::oclexpressioncs_constructor_args():
    sig = inspect.signature(essentialOCLCST::OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::VariableCS)


def test_essentialoclcst::variablecs_constructor_exists():
    assert callable(essentialOCLCST::VariableCS.__init__)


def test_essentialoclcst::variablecs_constructor_args():
    sig = inspect.signature(essentialOCLCST::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_callargumentscs_is_not_abstract():
    assert not inspect.isabstract(CallArgumentsCS)


def test_callargumentscs_constructor_exists():
    assert callable(CallArgumentsCS.__init__)


def test_callargumentscs_constructor_args():
    sig = inspect.signature(CallArgumentsCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcst::dotindexargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::DotIndexArgumentsCS)


def test_essentialoclcst::dotindexargumentscs_constructor_exists():
    assert callable(essentialOCLCST::DotIndexArgumentsCS.__init__)


def test_essentialoclcst::dotindexargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST::DotIndexArgumentsCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_essentialoclcst::dotindexargumentscs_has_isPre():
    assert hasattr(essentialOCLCST::DotIndexArgumentsCS, "isPre")
    descriptor = None
    for klass in essentialOCLCST::DotIndexArgumentsCS.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcst::arrowcallargumentscs_is_not_abstract():
    assert not inspect.isabstract(essentialOCLCST::ArrowCallArgumentsCS)


def test_essentialoclcst::arrowcallargumentscs_constructor_exists():
    assert callable(essentialOCLCST::ArrowCallArgumentsCS.__init__)


def test_essentialoclcst::arrowcallargumentscs_constructor_args():
    sig = inspect.signature(essentialOCLCST::ArrowCallArgumentsCS.__init__)
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
essentialOCLCST::CallArgumentsCS_strategy = st.builds(
    essentialOCLCST::CallArgumentsCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialOCLCST::StringLiteralExpCS_strategy = st.builds(
    essentialOCLCST::StringLiteralExpCS,
    stringSymbol=
        safe_text
)
essentialOCLCST::UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialOCLCST::UnlimitedNaturalLiteralExpCS,
)
essentialOCLCST::RealLiteralExpCS_strategy = st.builds(
    essentialOCLCST::RealLiteralExpCS,
    realSymbol=
        safe_text
)
essentialOCLCST::NullLiteralExpCS_strategy = st.builds(
    essentialOCLCST::NullLiteralExpCS,
)
essentialOCLCST::BooleanLiteralExpCS_strategy = st.builds(
    essentialOCLCST::BooleanLiteralExpCS,
    value=
        safe_text
)
OclExpressionCS_strategy = st.builds(
    OclExpressionCS,
)
essentialOCLCST::LiteralExpCS_strategy = st.builds(
    essentialOCLCST::LiteralExpCS,
)
essentialOCLCST::VariableExpCS_strategy = st.builds(
    essentialOCLCST::VariableExpCS,
)
essentialOCLCST::UnaryExpressionCS_strategy = st.builds(
    essentialOCLCST::UnaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST::LetExpCS_strategy = st.builds(
    essentialOCLCST::LetExpCS,
)
essentialOCLCST::InvalidLiteralExpCS_strategy = st.builds(
    essentialOCLCST::InvalidLiteralExpCS,
)
essentialOCLCST::IntegerLiteralExpCS_strategy = st.builds(
    essentialOCLCST::IntegerLiteralExpCS,
    integerSymbol=
        safe_text
)
essentialOCLCST::IfExpCS_strategy = st.builds(
    essentialOCLCST::IfExpCS,
)
essentialOCLCST::TypeCS_strategy = st.builds(
    essentialOCLCST::TypeCS,
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
essentialOCLCST::TupleTypeCS_strategy = st.builds(
    essentialOCLCST::TupleTypeCS,
    value=
        safe_text
)
essentialOCLCST::SimpleNameCS_strategy = st.builds(
    essentialOCLCST::SimpleNameCS,
    value=
        safe_text
)
essentialOCLCST::PathNameCS_strategy = st.builds(
    essentialOCLCST::PathNameCS,
)
essentialOCLCST::CollectionTypeCS_strategy = st.builds(
    essentialOCLCST::CollectionTypeCS,
)
essentialOCLCST::CollectionLiteralPartCS_strategy = st.builds(
    essentialOCLCST::CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialOCLCST::TupleLiteralExpCS_strategy = st.builds(
    essentialOCLCST::TupleLiteralExpCS,
)
essentialOCLCST::TypeLiteralExpCS_strategy = st.builds(
    essentialOCLCST::TypeLiteralExpCS,
)
essentialOCLCST::PrimitiveLiteralExpCS_strategy = st.builds(
    essentialOCLCST::PrimitiveLiteralExpCS,
)
essentialOCLCST::CollectionLiteralExpCS_strategy = st.builds(
    essentialOCLCST::CollectionLiteralExpCS,
)
essentialOCLCST::CallExpCS_strategy = st.builds(
    essentialOCLCST::CallExpCS,
)
essentialOCLCST::BinaryExpressionCS_strategy = st.builds(
    essentialOCLCST::BinaryExpressionCS,
    op=
        safe_text
)
essentialOCLCST::OclExpressionCS_strategy = st.builds(
    essentialOCLCST::OclExpressionCS,
)
essentialOCLCST::VariableCS_strategy = st.builds(
    essentialOCLCST::VariableCS,
)
CallArgumentsCS_strategy = st.builds(
    CallArgumentsCS,
)
essentialOCLCST::DotIndexArgumentsCS_strategy = st.builds(
    essentialOCLCST::DotIndexArgumentsCS,
    isPre=
        st.booleans()
)
essentialOCLCST::ArrowCallArgumentsCS_strategy = st.builds(
    essentialOCLCST::ArrowCallArgumentsCS,
)

@given(instance=VariableExpCS_strategy)
@settings(max_examples=50)
def test_variableexpcs_instantiation(instance):
    assert isinstance(instance, VariableExpCS)

@given(instance=essentialOCLCST::CallArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::callargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::CallArgumentsCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialOCLCST::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::StringLiteralExpCS)

@given(instance=essentialOCLCST::StringLiteralExpCS_strategy)
def test_essentialoclcst::stringliteralexpcs_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=essentialOCLCST::StringLiteralExpCS_strategy)
def test_essentialoclcst::stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=essentialOCLCST::UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::UnlimitedNaturalLiteralExpCS)

@given(instance=essentialOCLCST::RealLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::realliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::RealLiteralExpCS)

@given(instance=essentialOCLCST::RealLiteralExpCS_strategy)
def test_essentialoclcst::realliteralexpcs_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=essentialOCLCST::RealLiteralExpCS_strategy)
def test_essentialoclcst::realliteralexpcs_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=essentialOCLCST::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::NullLiteralExpCS)

@given(instance=essentialOCLCST::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::BooleanLiteralExpCS)

@given(instance=essentialOCLCST::BooleanLiteralExpCS_strategy)
def test_essentialoclcst::booleanliteralexpcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialOCLCST::BooleanLiteralExpCS_strategy)
def test_essentialoclcst::booleanliteralexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OclExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OclExpressionCS)

@given(instance=essentialOCLCST::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::LiteralExpCS)

@given(instance=essentialOCLCST::VariableExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::variableexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::VariableExpCS)

@given(instance=essentialOCLCST::UnaryExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::unaryexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::UnaryExpressionCS)

@given(instance=essentialOCLCST::UnaryExpressionCS_strategy)
def test_essentialoclcst::unaryexpressioncs_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=essentialOCLCST::UnaryExpressionCS_strategy)
def test_essentialoclcst::unaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=essentialOCLCST::LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::letexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::LetExpCS)

@given(instance=essentialOCLCST::InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::InvalidLiteralExpCS)

@given(instance=essentialOCLCST::IntegerLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::integerliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::IntegerLiteralExpCS)

@given(instance=essentialOCLCST::IntegerLiteralExpCS_strategy)
def test_essentialoclcst::integerliteralexpcs_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=essentialOCLCST::IntegerLiteralExpCS_strategy)
def test_essentialoclcst::integerliteralexpcs_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=essentialOCLCST::IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::IfExpCS)

@given(instance=essentialOCLCST::TypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::typecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::TypeCS)

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

@given(instance=essentialOCLCST::TupleTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::tupletypecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::TupleTypeCS)

@given(instance=essentialOCLCST::TupleTypeCS_strategy)
def test_essentialoclcst::tupletypecs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialOCLCST::TupleTypeCS_strategy)
def test_essentialoclcst::tupletypecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialOCLCST::SimpleNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::simplenamecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::SimpleNameCS)

@given(instance=essentialOCLCST::SimpleNameCS_strategy)
def test_essentialoclcst::simplenamecs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialOCLCST::SimpleNameCS_strategy)
def test_essentialoclcst::simplenamecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialOCLCST::PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::PathNameCS)

@given(instance=essentialOCLCST::CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::CollectionTypeCS)

@given(instance=essentialOCLCST::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::CollectionLiteralPartCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialOCLCST::TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::TupleLiteralExpCS)

@given(instance=essentialOCLCST::TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::TypeLiteralExpCS)

@given(instance=essentialOCLCST::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::PrimitiveLiteralExpCS)

@given(instance=essentialOCLCST::CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::CollectionLiteralExpCS)

@given(instance=essentialOCLCST::CallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::callexpcs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::CallExpCS)

@given(instance=essentialOCLCST::BinaryExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::binaryexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::BinaryExpressionCS)

@given(instance=essentialOCLCST::BinaryExpressionCS_strategy)
def test_essentialoclcst::binaryexpressioncs_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=essentialOCLCST::BinaryExpressionCS_strategy)
def test_essentialoclcst::binaryexpressioncs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=essentialOCLCST::OclExpressionCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::oclexpressioncs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::OclExpressionCS)

@given(instance=essentialOCLCST::VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::variablecs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::VariableCS)

@given(instance=CallArgumentsCS_strategy)
@settings(max_examples=50)
def test_callargumentscs_instantiation(instance):
    assert isinstance(instance, CallArgumentsCS)

@given(instance=essentialOCLCST::DotIndexArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::dotindexargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::DotIndexArgumentsCS)

@given(instance=essentialOCLCST::DotIndexArgumentsCS_strategy)
def test_essentialoclcst::dotindexargumentscs_isPre_type(instance):
    assert isinstance(instance.isPre, bool)


@given(instance=essentialOCLCST::DotIndexArgumentsCS_strategy)
def test_essentialoclcst::dotindexargumentscs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

@given(instance=essentialOCLCST::ArrowCallArgumentsCS_strategy)
@settings(max_examples=50)
def test_essentialoclcst::arrowcallargumentscs_instantiation(instance):
    assert isinstance(instance, essentialOCLCST::ArrowCallArgumentsCS)
