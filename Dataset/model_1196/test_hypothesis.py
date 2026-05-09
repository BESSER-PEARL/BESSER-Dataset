import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EssentialOCL::VoidType,
    LetExp,
    EssentialOCL::Variable,
    NavigationCallExp,
    EssentialOCL::PropertyCallExp,
    EssentialOCL::OclExpression,
    FeatureCallExp,
    EssentialOCL::OperationCallExp,
    EssentialOCL::NavigationCallExp,
    EssentialOCL::TupleType,
    TupleLiteralExp,
    EssentialOCL::TupleLiteralPart,
    TupleLiteralPart,
    EssentialOCL::TemplateParameterType,
    CallExp,
    EssentialOCL::FeatureCallExp,
    LoopExp,
    EssentialOCL::IteratorExp,
    EssentialOCL::IterateExp,
    EssentialOCL::InvalidType,
    NumericLiteralExp,
    EssentialOCL::UnlimitedNaturalExp,
    EssentialOCL::RealLiteralExp,
    EssentialOCL::IntegerLiteralExp,
    LiteralExp,
    EssentialOCL::TupleLiteralExp,
    EssentialOCL::InvalidLiteralExp,
    EssentialOCL::NullLiteralExp,
    EssentialOCL::PrimitiveLiteralExp,
    EssentialOCL::CollectionLiteralExp,
    CollectionLiteralPart,
    EssentialOCL::CollectionItem,
    OclExpression,
    EssentialOCL::TypeExp,
    EssentialOCL::VariableExp,
    EssentialOCL::LoopExp,
    EssentialOCL::IfExp,
    EssentialOCL::LiteralExp,
    EssentialOCL::LetExp,
    EssentialOCL::CallExp,
    PrimitiveLiteralExp,
    EssentialOCL::StringLiteralExp,
    EssentialOCL::NumericLiteralExp,
    EssentialOCL::BooleanLiteralExp,
    Variable,
    EssentialOCL::ExpressionInOcl,
    EssentialOCL::EnumLiteralExp,
    EssentialOCL::CollectionType,
    EssentialOCL::CollectionRange,
    CollectionLiteralExp,
    EssentialOCL::CollectionLiteralPart,
    CollectionType,
    EssentialOCL::SetType,
    EssentialOCL::OrderedSetType,
    EssentialOCL::SequenceType,
    EssentialOCL::BagType,
    EssentialOCL::AnyType,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::VoidType)


def test_essentialocl::voidtype_constructor_exists():
    assert callable(EssentialOCL::VoidType.__init__)


def test_essentialocl::voidtype_constructor_args():
    sig = inspect.signature(EssentialOCL::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::Variable)


def test_essentialocl::variable_constructor_exists():
    assert callable(EssentialOCL::Variable.__init__)


def test_essentialocl::variable_constructor_args():
    sig = inspect.signature(EssentialOCL::Variable.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::PropertyCallExp)


def test_essentialocl::propertycallexp_constructor_exists():
    assert callable(EssentialOCL::PropertyCallExp.__init__)


def test_essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OclExpression)


def test_essentialocl::oclexpression_constructor_exists():
    assert callable(EssentialOCL::OclExpression.__init__)


def test_essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(EssentialOCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OperationCallExp)


def test_essentialocl::operationcallexp_constructor_exists():
    assert callable(EssentialOCL::OperationCallExp.__init__)


def test_essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NavigationCallExp)


def test_essentialocl::navigationcallexp_constructor_exists():
    assert callable(EssentialOCL::NavigationCallExp.__init__)


def test_essentialocl::navigationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleType)


def test_essentialocl::tupletype_constructor_exists():
    assert callable(EssentialOCL::TupleType.__init__)


def test_essentialocl::tupletype_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleLiteralPart)


def test_essentialocl::tupleliteralpart_constructor_exists():
    assert callable(EssentialOCL::TupleLiteralPart.__init__)


def test_essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TemplateParameterType)


def test_essentialocl::templateparametertype_constructor_exists():
    assert callable(EssentialOCL::TemplateParameterType.__init__)


def test_essentialocl::templateparametertype_constructor_args():
    sig = inspect.signature(EssentialOCL::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_essentialocl::templateparametertype_has_specification():
    assert hasattr(EssentialOCL::TemplateParameterType, "specification")
    descriptor = None
    for klass in EssentialOCL::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::FeatureCallExp)


def test_essentialocl::featurecallexp_constructor_exists():
    assert callable(EssentialOCL::FeatureCallExp.__init__)


def test_essentialocl::featurecallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IteratorExp)


def test_essentialocl::iteratorexp_constructor_exists():
    assert callable(EssentialOCL::IteratorExp.__init__)


def test_essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IterateExp)


def test_essentialocl::iterateexp_constructor_exists():
    assert callable(EssentialOCL::IterateExp.__init__)


def test_essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::InvalidType)


def test_essentialocl::invalidtype_constructor_exists():
    assert callable(EssentialOCL::InvalidType.__init__)


def test_essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(EssentialOCL::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::UnlimitedNaturalExp)


def test_essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(EssentialOCL::UnlimitedNaturalExp.__init__)


def test_essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(EssentialOCL::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(EssentialOCL::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in EssentialOCL::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::RealLiteralExp)


def test_essentialocl::realliteralexp_constructor_exists():
    assert callable(EssentialOCL::RealLiteralExp.__init__)


def test_essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(EssentialOCL::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in EssentialOCL::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IntegerLiteralExp)


def test_essentialocl::integerliteralexp_constructor_exists():
    assert callable(EssentialOCL::IntegerLiteralExp.__init__)


def test_essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(EssentialOCL::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in EssentialOCL::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleLiteralExp)


def test_essentialocl::tupleliteralexp_constructor_exists():
    assert callable(EssentialOCL::TupleLiteralExp.__init__)


def test_essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::InvalidLiteralExp)


def test_essentialocl::invalidliteralexp_constructor_exists():
    assert callable(EssentialOCL::InvalidLiteralExp.__init__)


def test_essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NullLiteralExp)


def test_essentialocl::nullliteralexp_constructor_exists():
    assert callable(EssentialOCL::NullLiteralExp.__init__)


def test_essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::PrimitiveLiteralExp)


def test_essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(EssentialOCL::PrimitiveLiteralExp.__init__)


def test_essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionLiteralExp)


def test_essentialocl::collectionliteralexp_constructor_exists():
    assert callable(EssentialOCL::CollectionLiteralExp.__init__)


def test_essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl::collectionliteralexp_has_kind():
    assert hasattr(EssentialOCL::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in EssentialOCL::CollectionLiteralExp.__mro__:
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



def test_essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionItem)


def test_essentialocl::collectionitem_constructor_exists():
    assert callable(EssentialOCL::CollectionItem.__init__)


def test_essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TypeExp)


def test_essentialocl::typeexp_constructor_exists():
    assert callable(EssentialOCL::TypeExp.__init__)


def test_essentialocl::typeexp_constructor_args():
    sig = inspect.signature(EssentialOCL::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::VariableExp)


def test_essentialocl::variableexp_constructor_exists():
    assert callable(EssentialOCL::VariableExp.__init__)


def test_essentialocl::variableexp_constructor_args():
    sig = inspect.signature(EssentialOCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(EssentialOCL::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IfExp)


def test_essentialocl::ifexp_constructor_exists():
    assert callable(EssentialOCL::IfExp.__init__)


def test_essentialocl::ifexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LiteralExp)


def test_essentialocl::literalexp_constructor_exists():
    assert callable(EssentialOCL::LiteralExp.__init__)


def test_essentialocl::literalexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LetExp)


def test_essentialocl::letexp_constructor_exists():
    assert callable(EssentialOCL::LetExp.__init__)


def test_essentialocl::letexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CallExp)


def test_essentialocl::callexp_constructor_exists():
    assert callable(EssentialOCL::CallExp.__init__)


def test_essentialocl::callexp_constructor_args():
    sig = inspect.signature(EssentialOCL::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::StringLiteralExp)


def test_essentialocl::stringliteralexp_constructor_exists():
    assert callable(EssentialOCL::StringLiteralExp.__init__)


def test_essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(EssentialOCL::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in EssentialOCL::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NumericLiteralExp)


def test_essentialocl::numericliteralexp_constructor_exists():
    assert callable(EssentialOCL::NumericLiteralExp.__init__)


def test_essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::BooleanLiteralExp)


def test_essentialocl::booleanliteralexp_constructor_exists():
    assert callable(EssentialOCL::BooleanLiteralExp.__init__)


def test_essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(EssentialOCL::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in EssentialOCL::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::ExpressionInOcl)


def test_essentialocl::expressioninocl_constructor_exists():
    assert callable(EssentialOCL::ExpressionInOcl.__init__)


def test_essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(EssentialOCL::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::EnumLiteralExp)


def test_essentialocl::enumliteralexp_constructor_exists():
    assert callable(EssentialOCL::EnumLiteralExp.__init__)


def test_essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionType)


def test_essentialocl::collectiontype_constructor_exists():
    assert callable(EssentialOCL::CollectionType.__init__)


def test_essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionRange)


def test_essentialocl::collectionrange_constructor_exists():
    assert callable(EssentialOCL::CollectionRange.__init__)


def test_essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionLiteralPart)


def test_essentialocl::collectionliteralpart_constructor_exists():
    assert callable(EssentialOCL::CollectionLiteralPart.__init__)


def test_essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::SetType)


def test_essentialocl::settype_constructor_exists():
    assert callable(EssentialOCL::SetType.__init__)


def test_essentialocl::settype_constructor_args():
    sig = inspect.signature(EssentialOCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OrderedSetType)


def test_essentialocl::orderedsettype_constructor_exists():
    assert callable(EssentialOCL::OrderedSetType.__init__)


def test_essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(EssentialOCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::SequenceType)


def test_essentialocl::sequencetype_constructor_exists():
    assert callable(EssentialOCL::SequenceType.__init__)


def test_essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(EssentialOCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::BagType)


def test_essentialocl::bagtype_constructor_exists():
    assert callable(EssentialOCL::BagType.__init__)


def test_essentialocl::bagtype_constructor_args():
    sig = inspect.signature(EssentialOCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::AnyType)


def test_essentialocl::anytype_constructor_exists():
    assert callable(EssentialOCL::AnyType.__init__)


def test_essentialocl::anytype_constructor_args():
    sig = inspect.signature(EssentialOCL::AnyType.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Set",
        "Sequence",
        "Collection",
        "Bag",
        "OrderedSet",
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
EssentialOCL::VoidType_strategy = st.builds(
    EssentialOCL::VoidType,
)
LetExp_strategy = st.builds(
    LetExp,
)
EssentialOCL::Variable_strategy = st.builds(
    EssentialOCL::Variable,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
EssentialOCL::PropertyCallExp_strategy = st.builds(
    EssentialOCL::PropertyCallExp,
)
EssentialOCL::OclExpression_strategy = st.builds(
    EssentialOCL::OclExpression,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
EssentialOCL::OperationCallExp_strategy = st.builds(
    EssentialOCL::OperationCallExp,
)
EssentialOCL::NavigationCallExp_strategy = st.builds(
    EssentialOCL::NavigationCallExp,
)
EssentialOCL::TupleType_strategy = st.builds(
    EssentialOCL::TupleType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
EssentialOCL::TupleLiteralPart_strategy = st.builds(
    EssentialOCL::TupleLiteralPart,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
EssentialOCL::TemplateParameterType_strategy = st.builds(
    EssentialOCL::TemplateParameterType,
    specification=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
EssentialOCL::FeatureCallExp_strategy = st.builds(
    EssentialOCL::FeatureCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EssentialOCL::IteratorExp_strategy = st.builds(
    EssentialOCL::IteratorExp,
)
EssentialOCL::IterateExp_strategy = st.builds(
    EssentialOCL::IterateExp,
)
EssentialOCL::InvalidType_strategy = st.builds(
    EssentialOCL::InvalidType,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
EssentialOCL::UnlimitedNaturalExp_strategy = st.builds(
    EssentialOCL::UnlimitedNaturalExp,
    symbol=
        safe_text
)
EssentialOCL::RealLiteralExp_strategy = st.builds(
    EssentialOCL::RealLiteralExp,
    realSymbol=
        safe_text
)
EssentialOCL::IntegerLiteralExp_strategy = st.builds(
    EssentialOCL::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
EssentialOCL::TupleLiteralExp_strategy = st.builds(
    EssentialOCL::TupleLiteralExp,
)
EssentialOCL::InvalidLiteralExp_strategy = st.builds(
    EssentialOCL::InvalidLiteralExp,
)
EssentialOCL::NullLiteralExp_strategy = st.builds(
    EssentialOCL::NullLiteralExp,
)
EssentialOCL::PrimitiveLiteralExp_strategy = st.builds(
    EssentialOCL::PrimitiveLiteralExp,
)
EssentialOCL::CollectionLiteralExp_strategy = st.builds(
    EssentialOCL::CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
EssentialOCL::CollectionItem_strategy = st.builds(
    EssentialOCL::CollectionItem,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EssentialOCL::TypeExp_strategy = st.builds(
    EssentialOCL::TypeExp,
)
EssentialOCL::VariableExp_strategy = st.builds(
    EssentialOCL::VariableExp,
)
EssentialOCL::LoopExp_strategy = st.builds(
    EssentialOCL::LoopExp,
)
EssentialOCL::IfExp_strategy = st.builds(
    EssentialOCL::IfExp,
)
EssentialOCL::LiteralExp_strategy = st.builds(
    EssentialOCL::LiteralExp,
)
EssentialOCL::LetExp_strategy = st.builds(
    EssentialOCL::LetExp,
)
EssentialOCL::CallExp_strategy = st.builds(
    EssentialOCL::CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
EssentialOCL::StringLiteralExp_strategy = st.builds(
    EssentialOCL::StringLiteralExp,
    stringSymbol=
        safe_text
)
EssentialOCL::NumericLiteralExp_strategy = st.builds(
    EssentialOCL::NumericLiteralExp,
)
EssentialOCL::BooleanLiteralExp_strategy = st.builds(
    EssentialOCL::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
EssentialOCL::ExpressionInOcl_strategy = st.builds(
    EssentialOCL::ExpressionInOcl,
)
EssentialOCL::EnumLiteralExp_strategy = st.builds(
    EssentialOCL::EnumLiteralExp,
)
EssentialOCL::CollectionType_strategy = st.builds(
    EssentialOCL::CollectionType,
)
EssentialOCL::CollectionRange_strategy = st.builds(
    EssentialOCL::CollectionRange,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
EssentialOCL::CollectionLiteralPart_strategy = st.builds(
    EssentialOCL::CollectionLiteralPart,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EssentialOCL::SetType_strategy = st.builds(
    EssentialOCL::SetType,
)
EssentialOCL::OrderedSetType_strategy = st.builds(
    EssentialOCL::OrderedSetType,
)
EssentialOCL::SequenceType_strategy = st.builds(
    EssentialOCL::SequenceType,
)
EssentialOCL::BagType_strategy = st.builds(
    EssentialOCL::BagType,
)
EssentialOCL::AnyType_strategy = st.builds(
    EssentialOCL::AnyType,
)

@given(instance=EssentialOCL::VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::VoidType)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=EssentialOCL::Variable_strategy)
@settings(max_examples=50)
def test_essentialocl::variable_instantiation(instance):
    assert isinstance(instance, EssentialOCL::Variable)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=EssentialOCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::PropertyCallExp)

@given(instance=EssentialOCL::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OclExpression)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=EssentialOCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OperationCallExp)

@given(instance=EssentialOCL::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::navigationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NavigationCallExp)

@given(instance=EssentialOCL::TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=EssentialOCL::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleLiteralPart)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=EssentialOCL::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_essentialocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TemplateParameterType)

@given(instance=EssentialOCL::TemplateParameterType_strategy)
def test_essentialocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=EssentialOCL::TemplateParameterType_strategy)
def test_essentialocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=EssentialOCL::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::featurecallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::FeatureCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EssentialOCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IteratorExp)

@given(instance=EssentialOCL::IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IterateExp)

@given(instance=EssentialOCL::InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::InvalidType)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::UnlimitedNaturalExp)

@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=EssentialOCL::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::RealLiteralExp)

@given(instance=EssentialOCL::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=EssentialOCL::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IntegerLiteralExp)

@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=EssentialOCL::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleLiteralExp)

@given(instance=EssentialOCL::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::InvalidLiteralExp)

@given(instance=EssentialOCL::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NullLiteralExp)

@given(instance=EssentialOCL::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::PrimitiveLiteralExp)

@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionLiteralExp)

@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=EssentialOCL::CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionItem)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EssentialOCL::TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TypeExp)

@given(instance=EssentialOCL::VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::VariableExp)

@given(instance=EssentialOCL::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LoopExp)

@given(instance=EssentialOCL::IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IfExp)

@given(instance=EssentialOCL::LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LiteralExp)

@given(instance=EssentialOCL::LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LetExp)

@given(instance=EssentialOCL::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=EssentialOCL::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::StringLiteralExp)

@given(instance=EssentialOCL::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=EssentialOCL::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=EssentialOCL::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NumericLiteralExp)

@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::BooleanLiteralExp)

@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=EssentialOCL::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, EssentialOCL::ExpressionInOcl)

@given(instance=EssentialOCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::EnumLiteralExp)

@given(instance=EssentialOCL::CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionType)

@given(instance=EssentialOCL::CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionRange)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=EssentialOCL::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionLiteralPart)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EssentialOCL::SetType_strategy)
@settings(max_examples=50)
def test_essentialocl::settype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::SetType)

@given(instance=EssentialOCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OrderedSetType)

@given(instance=EssentialOCL::SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::SequenceType)

@given(instance=EssentialOCL::BagType_strategy)
@settings(max_examples=50)
def test_essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::BagType)

@given(instance=EssentialOCL::AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::AnyType)
