import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitiveExp,
    docl::StringLiteralExp,
    docl::BooleanLiteralExp,
    docl::NullLiteralExp,
    docl::InvalidLiteralExp,
    docl::UnlimitedNaturalLiteralExp,
    docl::NumberLiteralExp,
    OclExpression,
    docl::IterateExp,
    docl::ComOpCallExp,
    docl::LambdaExp,
    docl::BoolOpCallExp,
    docl::IfExp,
    docl::NavigationExp,
    docl::ElseIfThenExp,
    docl::AddOpCallExp,
    docl::NestedExp,
    docl::SelfExp,
    docl::MulOpCallExp,
    docl::EqOpCallExp,
    docl::CollectionOpCallExp,
    docl::TupleExp,
    docl::OperationCall,
    docl::NavigationOrAttributeCall,
    docl::IteratorExp,
    docl::PrimitiveExp,
    docl::TuplePart,
    docl::OclType,
    docl::Iterator,
    docl::LocalVariable,
    OclType,
    docl::LambdaType,
    docl::StringType,
    docl::BagType,
    docl::OrderedSetType,
    docl::EnvType,
    docl::RealType,
    docl::TupleType,
    docl::IntegerType,
    docl::BooleanType,
    docl::SetType,
    docl::SequenceType,
    docl::OclAnyType,
    docl::MapType,
    docl::OclModelElementExp,
    ModuleElement,
    docl::Query,
    docl::URI::,
    docl::ModuleElement,
    docl::Import,
    docl::OclExpression,
    docl::OclModel,
    docl::Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::StringLiteralExp)


def test_docl::stringliteralexp_constructor_exists():
    assert callable(docl::StringLiteralExp.__init__)


def test_docl::stringliteralexp_constructor_args():
    sig = inspect.signature(docl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_docl::stringliteralexp_has_segments():
    assert hasattr(docl::StringLiteralExp, "segments")
    descriptor = None
    for klass in docl::StringLiteralExp.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_docl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::BooleanLiteralExp)


def test_docl::booleanliteralexp_constructor_exists():
    assert callable(docl::BooleanLiteralExp.__init__)


def test_docl::booleanliteralexp_constructor_args():
    sig = inspect.signature(docl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_docl::booleanliteralexp_has_symbol():
    assert hasattr(docl::BooleanLiteralExp, "symbol")
    descriptor = None
    for klass in docl::BooleanLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_docl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::NullLiteralExp)


def test_docl::nullliteralexp_constructor_exists():
    assert callable(docl::NullLiteralExp.__init__)


def test_docl::nullliteralexp_constructor_args():
    sig = inspect.signature(docl::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::InvalidLiteralExp)


def test_docl::invalidliteralexp_constructor_exists():
    assert callable(docl::InvalidLiteralExp.__init__)


def test_docl::invalidliteralexp_constructor_args():
    sig = inspect.signature(docl::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::UnlimitedNaturalLiteralExp)


def test_docl::unlimitednaturalliteralexp_constructor_exists():
    assert callable(docl::UnlimitedNaturalLiteralExp.__init__)


def test_docl::unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(docl::UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl::NumberLiteralExp)


def test_docl::numberliteralexp_constructor_exists():
    assert callable(docl::NumberLiteralExp.__init__)


def test_docl::numberliteralexp_constructor_args():
    sig = inspect.signature(docl::NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_docl::numberliteralexp_has_symbol():
    assert hasattr(docl::NumberLiteralExp, "symbol")
    descriptor = None
    for klass in docl::NumberLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_docl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(docl::IterateExp)


def test_docl::iterateexp_constructor_exists():
    assert callable(docl::IterateExp.__init__)


def test_docl::iterateexp_constructor_args():
    sig = inspect.signature(docl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::comopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::ComOpCallExp)


def test_docl::comopcallexp_constructor_exists():
    assert callable(docl::ComOpCallExp.__init__)


def test_docl::comopcallexp_constructor_args():
    sig = inspect.signature(docl::ComOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::lambdaexp_is_not_abstract():
    assert not inspect.isabstract(docl::LambdaExp)


def test_docl::lambdaexp_constructor_exists():
    assert callable(docl::LambdaExp.__init__)


def test_docl::lambdaexp_constructor_args():
    sig = inspect.signature(docl::LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::boolopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::BoolOpCallExp)


def test_docl::boolopcallexp_constructor_exists():
    assert callable(docl::BoolOpCallExp.__init__)


def test_docl::boolopcallexp_constructor_args():
    sig = inspect.signature(docl::BoolOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::ifexp_is_not_abstract():
    assert not inspect.isabstract(docl::IfExp)


def test_docl::ifexp_constructor_exists():
    assert callable(docl::IfExp.__init__)


def test_docl::ifexp_constructor_args():
    sig = inspect.signature(docl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::navigationexp_is_not_abstract():
    assert not inspect.isabstract(docl::NavigationExp)


def test_docl::navigationexp_constructor_exists():
    assert callable(docl::NavigationExp.__init__)


def test_docl::navigationexp_constructor_args():
    sig = inspect.signature(docl::NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::elseifthenexp_is_not_abstract():
    assert not inspect.isabstract(docl::ElseIfThenExp)


def test_docl::elseifthenexp_constructor_exists():
    assert callable(docl::ElseIfThenExp.__init__)


def test_docl::elseifthenexp_constructor_args():
    sig = inspect.signature(docl::ElseIfThenExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::AddOpCallExp)


def test_docl::addopcallexp_constructor_exists():
    assert callable(docl::AddOpCallExp.__init__)


def test_docl::addopcallexp_constructor_args():
    sig = inspect.signature(docl::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::nestedexp_is_not_abstract():
    assert not inspect.isabstract(docl::NestedExp)


def test_docl::nestedexp_constructor_exists():
    assert callable(docl::NestedExp.__init__)


def test_docl::nestedexp_constructor_args():
    sig = inspect.signature(docl::NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::selfexp_is_not_abstract():
    assert not inspect.isabstract(docl::SelfExp)


def test_docl::selfexp_constructor_exists():
    assert callable(docl::SelfExp.__init__)


def test_docl::selfexp_constructor_args():
    sig = inspect.signature(docl::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::MulOpCallExp)


def test_docl::mulopcallexp_constructor_exists():
    assert callable(docl::MulOpCallExp.__init__)


def test_docl::mulopcallexp_constructor_args():
    sig = inspect.signature(docl::MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::EqOpCallExp)


def test_docl::eqopcallexp_constructor_exists():
    assert callable(docl::EqOpCallExp.__init__)


def test_docl::eqopcallexp_constructor_args():
    sig = inspect.signature(docl::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::collectionopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl::CollectionOpCallExp)


def test_docl::collectionopcallexp_constructor_exists():
    assert callable(docl::CollectionOpCallExp.__init__)


def test_docl::collectionopcallexp_constructor_args():
    sig = inspect.signature(docl::CollectionOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(docl::TupleExp)


def test_docl::tupleexp_constructor_exists():
    assert callable(docl::TupleExp.__init__)


def test_docl::tupleexp_constructor_args():
    sig = inspect.signature(docl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::operationcall_is_not_abstract():
    assert not inspect.isabstract(docl::OperationCall)


def test_docl::operationcall_constructor_exists():
    assert callable(docl::OperationCall.__init__)


def test_docl::operationcall_constructor_args():
    sig = inspect.signature(docl::OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_docl::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(docl::NavigationOrAttributeCall)


def test_docl::navigationorattributecall_constructor_exists():
    assert callable(docl::NavigationOrAttributeCall.__init__)


def test_docl::navigationorattributecall_constructor_args():
    sig = inspect.signature(docl::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_docl::navigationorattributecall_has_feature():
    assert hasattr(docl::NavigationOrAttributeCall, "feature")
    descriptor = None
    for klass in docl::NavigationOrAttributeCall.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_docl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(docl::IteratorExp)


def test_docl::iteratorexp_constructor_exists():
    assert callable(docl::IteratorExp.__init__)


def test_docl::iteratorexp_constructor_args():
    sig = inspect.signature(docl::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(docl::PrimitiveExp)


def test_docl::primitiveexp_constructor_exists():
    assert callable(docl::PrimitiveExp.__init__)


def test_docl::primitiveexp_constructor_args():
    sig = inspect.signature(docl::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_docl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(docl::TuplePart)


def test_docl::tuplepart_constructor_exists():
    assert callable(docl::TuplePart.__init__)


def test_docl::tuplepart_constructor_args():
    sig = inspect.signature(docl::TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::tuplepart_has_name():
    assert hasattr(docl::TuplePart, "name")
    descriptor = None
    for klass in docl::TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::ocltype_is_not_abstract():
    assert not inspect.isabstract(docl::OclType)


def test_docl::ocltype_constructor_exists():
    assert callable(docl::OclType.__init__)


def test_docl::ocltype_constructor_args():
    sig = inspect.signature(docl::OclType.__init__)
    params = list(sig.parameters.keys())



def test_docl::iterator_is_not_abstract():
    assert not inspect.isabstract(docl::Iterator)


def test_docl::iterator_constructor_exists():
    assert callable(docl::Iterator.__init__)


def test_docl::iterator_constructor_args():
    sig = inspect.signature(docl::Iterator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::iterator_has_name():
    assert hasattr(docl::Iterator, "name")
    descriptor = None
    for klass in docl::Iterator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::localvariable_is_not_abstract():
    assert not inspect.isabstract(docl::LocalVariable)


def test_docl::localvariable_constructor_exists():
    assert callable(docl::LocalVariable.__init__)


def test_docl::localvariable_constructor_args():
    sig = inspect.signature(docl::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::localvariable_has_name():
    assert hasattr(docl::LocalVariable, "name")
    descriptor = None
    for klass in docl::LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_docl::lambdatype_is_not_abstract():
    assert not inspect.isabstract(docl::LambdaType)


def test_docl::lambdatype_constructor_exists():
    assert callable(docl::LambdaType.__init__)


def test_docl::lambdatype_constructor_args():
    sig = inspect.signature(docl::LambdaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::lambdatype_has_name():
    assert hasattr(docl::LambdaType, "name")
    descriptor = None
    for klass in docl::LambdaType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::stringtype_is_not_abstract():
    assert not inspect.isabstract(docl::StringType)


def test_docl::stringtype_constructor_exists():
    assert callable(docl::StringType.__init__)


def test_docl::stringtype_constructor_args():
    sig = inspect.signature(docl::StringType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::stringtype_has_name():
    assert hasattr(docl::StringType, "name")
    descriptor = None
    for klass in docl::StringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::bagtype_is_not_abstract():
    assert not inspect.isabstract(docl::BagType)


def test_docl::bagtype_constructor_exists():
    assert callable(docl::BagType.__init__)


def test_docl::bagtype_constructor_args():
    sig = inspect.signature(docl::BagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::bagtype_has_name():
    assert hasattr(docl::BagType, "name")
    descriptor = None
    for klass in docl::BagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(docl::OrderedSetType)


def test_docl::orderedsettype_constructor_exists():
    assert callable(docl::OrderedSetType.__init__)


def test_docl::orderedsettype_constructor_args():
    sig = inspect.signature(docl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::orderedsettype_has_name():
    assert hasattr(docl::OrderedSetType, "name")
    descriptor = None
    for klass in docl::OrderedSetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::envtype_is_not_abstract():
    assert not inspect.isabstract(docl::EnvType)


def test_docl::envtype_constructor_exists():
    assert callable(docl::EnvType.__init__)


def test_docl::envtype_constructor_args():
    sig = inspect.signature(docl::EnvType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::envtype_has_name():
    assert hasattr(docl::EnvType, "name")
    descriptor = None
    for klass in docl::EnvType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::realtype_is_not_abstract():
    assert not inspect.isabstract(docl::RealType)


def test_docl::realtype_constructor_exists():
    assert callable(docl::RealType.__init__)


def test_docl::realtype_constructor_args():
    sig = inspect.signature(docl::RealType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::realtype_has_name():
    assert hasattr(docl::RealType, "name")
    descriptor = None
    for klass in docl::RealType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::tupletype_is_not_abstract():
    assert not inspect.isabstract(docl::TupleType)


def test_docl::tupletype_constructor_exists():
    assert callable(docl::TupleType.__init__)


def test_docl::tupletype_constructor_args():
    sig = inspect.signature(docl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_docl::integertype_is_not_abstract():
    assert not inspect.isabstract(docl::IntegerType)


def test_docl::integertype_constructor_exists():
    assert callable(docl::IntegerType.__init__)


def test_docl::integertype_constructor_args():
    sig = inspect.signature(docl::IntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::integertype_has_name():
    assert hasattr(docl::IntegerType, "name")
    descriptor = None
    for klass in docl::IntegerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::booleantype_is_not_abstract():
    assert not inspect.isabstract(docl::BooleanType)


def test_docl::booleantype_constructor_exists():
    assert callable(docl::BooleanType.__init__)


def test_docl::booleantype_constructor_args():
    sig = inspect.signature(docl::BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::booleantype_has_name():
    assert hasattr(docl::BooleanType, "name")
    descriptor = None
    for klass in docl::BooleanType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::settype_is_not_abstract():
    assert not inspect.isabstract(docl::SetType)


def test_docl::settype_constructor_exists():
    assert callable(docl::SetType.__init__)


def test_docl::settype_constructor_args():
    sig = inspect.signature(docl::SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::settype_has_name():
    assert hasattr(docl::SetType, "name")
    descriptor = None
    for klass in docl::SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(docl::SequenceType)


def test_docl::sequencetype_constructor_exists():
    assert callable(docl::SequenceType.__init__)


def test_docl::sequencetype_constructor_args():
    sig = inspect.signature(docl::SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::sequencetype_has_name():
    assert hasattr(docl::SequenceType, "name")
    descriptor = None
    for klass in docl::SequenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(docl::OclAnyType)


def test_docl::oclanytype_constructor_exists():
    assert callable(docl::OclAnyType.__init__)


def test_docl::oclanytype_constructor_args():
    sig = inspect.signature(docl::OclAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::oclanytype_has_name():
    assert hasattr(docl::OclAnyType, "name")
    descriptor = None
    for klass in docl::OclAnyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::maptype_is_not_abstract():
    assert not inspect.isabstract(docl::MapType)


def test_docl::maptype_constructor_exists():
    assert callable(docl::MapType.__init__)


def test_docl::maptype_constructor_args():
    sig = inspect.signature(docl::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::maptype_has_name():
    assert hasattr(docl::MapType, "name")
    descriptor = None
    for klass in docl::MapType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(docl::OclModelElementExp)


def test_docl::oclmodelelementexp_constructor_exists():
    assert callable(docl::OclModelElementExp.__init__)


def test_docl::oclmodelelementexp_constructor_args():
    sig = inspect.signature(docl::OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::oclmodelelementexp_has_name():
    assert hasattr(docl::OclModelElementExp, "name")
    descriptor = None
    for klass in docl::OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_docl::query_is_not_abstract():
    assert not inspect.isabstract(docl::Query)


def test_docl::query_constructor_exists():
    assert callable(docl::Query.__init__)


def test_docl::query_constructor_args():
    sig = inspect.signature(docl::Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::query_has_name():
    assert hasattr(docl::Query, "name")
    descriptor = None
    for klass in docl::Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::uri::_is_not_abstract():
    assert not inspect.isabstract(docl::URI::)


def test_docl::uri::_constructor_exists():
    assert callable(docl::URI::.__init__)


def test_docl::uri::_constructor_args():
    sig = inspect.signature(docl::URI::.__init__)
    params = list(sig.parameters.keys())
    assert "fragment_" in params, "Missing parameter 'fragment_'"
    assert "authority" in params, "Missing parameter 'authority'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_docl::uri::_has_fragment_():
    assert hasattr(docl::URI::, "fragment_")
    descriptor = None
    for klass in docl::URI::.__mro__:
        if "fragment_" in klass.__dict__:
            descriptor = klass.__dict__["fragment_"]
            break
    assert isinstance(descriptor, property)

def test_docl::uri::_has_authority():
    assert hasattr(docl::URI::, "authority")
    descriptor = None
    for klass in docl::URI::.__mro__:
        if "authority" in klass.__dict__:
            descriptor = klass.__dict__["authority"]
            break
    assert isinstance(descriptor, property)

def test_docl::uri::_has_scheme():
    assert hasattr(docl::URI::, "scheme")
    descriptor = None
    for klass in docl::URI::.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_docl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(docl::ModuleElement)


def test_docl::moduleelement_constructor_exists():
    assert callable(docl::ModuleElement.__init__)


def test_docl::moduleelement_constructor_args():
    sig = inspect.signature(docl::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_docl::import_is_not_abstract():
    assert not inspect.isabstract(docl::Import)


def test_docl::import_constructor_exists():
    assert callable(docl::Import.__init__)


def test_docl::import_constructor_args():
    sig = inspect.signature(docl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::import_has_name():
    assert hasattr(docl::Import, "name")
    descriptor = None
    for klass in docl::Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(docl::OclExpression)


def test_docl::oclexpression_constructor_exists():
    assert callable(docl::OclExpression.__init__)


def test_docl::oclexpression_constructor_args():
    sig = inspect.signature(docl::OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_docl::oclexpression_has_elements():
    assert hasattr(docl::OclExpression, "elements")
    descriptor = None
    for klass in docl::OclExpression.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_docl::oclexpression_has_name():
    assert hasattr(docl::OclExpression, "name")
    descriptor = None
    for klass in docl::OclExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(docl::OclModel)


def test_docl::oclmodel_constructor_exists():
    assert callable(docl::OclModel.__init__)


def test_docl::oclmodel_constructor_args():
    sig = inspect.signature(docl::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::oclmodel_has_name():
    assert hasattr(docl::OclModel, "name")
    descriptor = None
    for klass in docl::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::module_is_not_abstract():
    assert not inspect.isabstract(docl::Module)


def test_docl::module_constructor_exists():
    assert callable(docl::Module.__init__)


def test_docl::module_constructor_args():
    sig = inspect.signature(docl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::module_has_name():
    assert hasattr(docl::Module, "name")
    descriptor = None
    for klass in docl::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
docl::StringLiteralExp_strategy = st.builds(
    docl::StringLiteralExp,
    segments=
        safe_text
)
docl::BooleanLiteralExp_strategy = st.builds(
    docl::BooleanLiteralExp,
    symbol=
        safe_text
)
docl::NullLiteralExp_strategy = st.builds(
    docl::NullLiteralExp,
)
docl::InvalidLiteralExp_strategy = st.builds(
    docl::InvalidLiteralExp,
)
docl::UnlimitedNaturalLiteralExp_strategy = st.builds(
    docl::UnlimitedNaturalLiteralExp,
)
docl::NumberLiteralExp_strategy = st.builds(
    docl::NumberLiteralExp,
    symbol=
        st.integers()
)
OclExpression_strategy = st.builds(
    OclExpression,
)
docl::IterateExp_strategy = st.builds(
    docl::IterateExp,
)
docl::ComOpCallExp_strategy = st.builds(
    docl::ComOpCallExp,
)
docl::LambdaExp_strategy = st.builds(
    docl::LambdaExp,
)
docl::BoolOpCallExp_strategy = st.builds(
    docl::BoolOpCallExp,
)
docl::IfExp_strategy = st.builds(
    docl::IfExp,
)
docl::NavigationExp_strategy = st.builds(
    docl::NavigationExp,
)
docl::ElseIfThenExp_strategy = st.builds(
    docl::ElseIfThenExp,
)
docl::AddOpCallExp_strategy = st.builds(
    docl::AddOpCallExp,
)
docl::NestedExp_strategy = st.builds(
    docl::NestedExp,
)
docl::SelfExp_strategy = st.builds(
    docl::SelfExp,
)
docl::MulOpCallExp_strategy = st.builds(
    docl::MulOpCallExp,
)
docl::EqOpCallExp_strategy = st.builds(
    docl::EqOpCallExp,
)
docl::CollectionOpCallExp_strategy = st.builds(
    docl::CollectionOpCallExp,
)
docl::TupleExp_strategy = st.builds(
    docl::TupleExp,
)
docl::OperationCall_strategy = st.builds(
    docl::OperationCall,
)
docl::NavigationOrAttributeCall_strategy = st.builds(
    docl::NavigationOrAttributeCall,
    feature=
        safe_text
)
docl::IteratorExp_strategy = st.builds(
    docl::IteratorExp,
)
docl::PrimitiveExp_strategy = st.builds(
    docl::PrimitiveExp,
)
docl::TuplePart_strategy = st.builds(
    docl::TuplePart,
    name=
        safe_text
)
docl::OclType_strategy = st.builds(
    docl::OclType,
)
docl::Iterator_strategy = st.builds(
    docl::Iterator,
    name=
        safe_text
)
docl::LocalVariable_strategy = st.builds(
    docl::LocalVariable,
    name=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
docl::LambdaType_strategy = st.builds(
    docl::LambdaType,
    name=
        safe_text
)
docl::StringType_strategy = st.builds(
    docl::StringType,
    name=
        safe_text
)
docl::BagType_strategy = st.builds(
    docl::BagType,
    name=
        safe_text
)
docl::OrderedSetType_strategy = st.builds(
    docl::OrderedSetType,
    name=
        safe_text
)
docl::EnvType_strategy = st.builds(
    docl::EnvType,
    name=
        safe_text
)
docl::RealType_strategy = st.builds(
    docl::RealType,
    name=
        safe_text
)
docl::TupleType_strategy = st.builds(
    docl::TupleType,
)
docl::IntegerType_strategy = st.builds(
    docl::IntegerType,
    name=
        safe_text
)
docl::BooleanType_strategy = st.builds(
    docl::BooleanType,
    name=
        safe_text
)
docl::SetType_strategy = st.builds(
    docl::SetType,
    name=
        safe_text
)
docl::SequenceType_strategy = st.builds(
    docl::SequenceType,
    name=
        safe_text
)
docl::OclAnyType_strategy = st.builds(
    docl::OclAnyType,
    name=
        safe_text
)
docl::MapType_strategy = st.builds(
    docl::MapType,
    name=
        safe_text
)
docl::OclModelElementExp_strategy = st.builds(
    docl::OclModelElementExp,
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
docl::Query_strategy = st.builds(
    docl::Query,
    name=
        safe_text
)
docl::URI::_strategy = st.builds(
    docl::URI::,
    fragment_=
        safe_text,
    authority=
        safe_text,
    scheme=
        safe_text
)
docl::ModuleElement_strategy = st.builds(
    docl::ModuleElement,
)
docl::Import_strategy = st.builds(
    docl::Import,
    name=
        safe_text
)
docl::OclExpression_strategy = st.builds(
    docl::OclExpression,
    elements=
        safe_text,
    name=
        safe_text
)
docl::OclModel_strategy = st.builds(
    docl::OclModel,
    name=
        safe_text
)
docl::Module_strategy = st.builds(
    docl::Module,
    name=
        safe_text
)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=docl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, docl::StringLiteralExp)

@given(instance=docl::StringLiteralExp_strategy)
def test_docl::stringliteralexp_segments_type(instance):
    assert isinstance(instance.segments, str)


@given(instance=docl::StringLiteralExp_strategy)
def test_docl::stringliteralexp_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=docl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, docl::BooleanLiteralExp)

@given(instance=docl::BooleanLiteralExp_strategy)
def test_docl::booleanliteralexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=docl::BooleanLiteralExp_strategy)
def test_docl::booleanliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=docl::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, docl::NullLiteralExp)

@given(instance=docl::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, docl::InvalidLiteralExp)

@given(instance=docl::UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, docl::UnlimitedNaturalLiteralExp)

@given(instance=docl::NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_docl::numberliteralexp_instantiation(instance):
    assert isinstance(instance, docl::NumberLiteralExp)

@given(instance=docl::NumberLiteralExp_strategy)
def test_docl::numberliteralexp_symbol_type(instance):
    assert isinstance(instance.symbol, int)


@given(instance=docl::NumberLiteralExp_strategy)
def test_docl::numberliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=docl::IterateExp_strategy)
@settings(max_examples=50)
def test_docl::iterateexp_instantiation(instance):
    assert isinstance(instance, docl::IterateExp)

@given(instance=docl::ComOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::comopcallexp_instantiation(instance):
    assert isinstance(instance, docl::ComOpCallExp)

@given(instance=docl::LambdaExp_strategy)
@settings(max_examples=50)
def test_docl::lambdaexp_instantiation(instance):
    assert isinstance(instance, docl::LambdaExp)

@given(instance=docl::BoolOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::boolopcallexp_instantiation(instance):
    assert isinstance(instance, docl::BoolOpCallExp)

@given(instance=docl::IfExp_strategy)
@settings(max_examples=50)
def test_docl::ifexp_instantiation(instance):
    assert isinstance(instance, docl::IfExp)

@given(instance=docl::NavigationExp_strategy)
@settings(max_examples=50)
def test_docl::navigationexp_instantiation(instance):
    assert isinstance(instance, docl::NavigationExp)

@given(instance=docl::ElseIfThenExp_strategy)
@settings(max_examples=50)
def test_docl::elseifthenexp_instantiation(instance):
    assert isinstance(instance, docl::ElseIfThenExp)

@given(instance=docl::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::addopcallexp_instantiation(instance):
    assert isinstance(instance, docl::AddOpCallExp)

@given(instance=docl::NestedExp_strategy)
@settings(max_examples=50)
def test_docl::nestedexp_instantiation(instance):
    assert isinstance(instance, docl::NestedExp)

@given(instance=docl::SelfExp_strategy)
@settings(max_examples=50)
def test_docl::selfexp_instantiation(instance):
    assert isinstance(instance, docl::SelfExp)

@given(instance=docl::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::mulopcallexp_instantiation(instance):
    assert isinstance(instance, docl::MulOpCallExp)

@given(instance=docl::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::eqopcallexp_instantiation(instance):
    assert isinstance(instance, docl::EqOpCallExp)

@given(instance=docl::CollectionOpCallExp_strategy)
@settings(max_examples=50)
def test_docl::collectionopcallexp_instantiation(instance):
    assert isinstance(instance, docl::CollectionOpCallExp)

@given(instance=docl::TupleExp_strategy)
@settings(max_examples=50)
def test_docl::tupleexp_instantiation(instance):
    assert isinstance(instance, docl::TupleExp)

@given(instance=docl::OperationCall_strategy)
@settings(max_examples=50)
def test_docl::operationcall_instantiation(instance):
    assert isinstance(instance, docl::OperationCall)

@given(instance=docl::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_docl::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, docl::NavigationOrAttributeCall)

@given(instance=docl::NavigationOrAttributeCall_strategy)
def test_docl::navigationorattributecall_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=docl::NavigationOrAttributeCall_strategy)
def test_docl::navigationorattributecall_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=docl::IteratorExp_strategy)
@settings(max_examples=50)
def test_docl::iteratorexp_instantiation(instance):
    assert isinstance(instance, docl::IteratorExp)

@given(instance=docl::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_docl::primitiveexp_instantiation(instance):
    assert isinstance(instance, docl::PrimitiveExp)

@given(instance=docl::TuplePart_strategy)
@settings(max_examples=50)
def test_docl::tuplepart_instantiation(instance):
    assert isinstance(instance, docl::TuplePart)

@given(instance=docl::TuplePart_strategy)
def test_docl::tuplepart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::TuplePart_strategy)
def test_docl::tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OclType_strategy)
@settings(max_examples=50)
def test_docl::ocltype_instantiation(instance):
    assert isinstance(instance, docl::OclType)

@given(instance=docl::Iterator_strategy)
@settings(max_examples=50)
def test_docl::iterator_instantiation(instance):
    assert isinstance(instance, docl::Iterator)

@given(instance=docl::Iterator_strategy)
def test_docl::iterator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::Iterator_strategy)
def test_docl::iterator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::LocalVariable_strategy)
@settings(max_examples=50)
def test_docl::localvariable_instantiation(instance):
    assert isinstance(instance, docl::LocalVariable)

@given(instance=docl::LocalVariable_strategy)
def test_docl::localvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::LocalVariable_strategy)
def test_docl::localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=docl::LambdaType_strategy)
@settings(max_examples=50)
def test_docl::lambdatype_instantiation(instance):
    assert isinstance(instance, docl::LambdaType)

@given(instance=docl::LambdaType_strategy)
def test_docl::lambdatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::LambdaType_strategy)
def test_docl::lambdatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::StringType_strategy)
@settings(max_examples=50)
def test_docl::stringtype_instantiation(instance):
    assert isinstance(instance, docl::StringType)

@given(instance=docl::StringType_strategy)
def test_docl::stringtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::StringType_strategy)
def test_docl::stringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::BagType_strategy)
@settings(max_examples=50)
def test_docl::bagtype_instantiation(instance):
    assert isinstance(instance, docl::BagType)

@given(instance=docl::BagType_strategy)
def test_docl::bagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::BagType_strategy)
def test_docl::bagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_docl::orderedsettype_instantiation(instance):
    assert isinstance(instance, docl::OrderedSetType)

@given(instance=docl::OrderedSetType_strategy)
def test_docl::orderedsettype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::OrderedSetType_strategy)
def test_docl::orderedsettype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::EnvType_strategy)
@settings(max_examples=50)
def test_docl::envtype_instantiation(instance):
    assert isinstance(instance, docl::EnvType)

@given(instance=docl::EnvType_strategy)
def test_docl::envtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::EnvType_strategy)
def test_docl::envtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::RealType_strategy)
@settings(max_examples=50)
def test_docl::realtype_instantiation(instance):
    assert isinstance(instance, docl::RealType)

@given(instance=docl::RealType_strategy)
def test_docl::realtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::RealType_strategy)
def test_docl::realtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::TupleType_strategy)
@settings(max_examples=50)
def test_docl::tupletype_instantiation(instance):
    assert isinstance(instance, docl::TupleType)

@given(instance=docl::IntegerType_strategy)
@settings(max_examples=50)
def test_docl::integertype_instantiation(instance):
    assert isinstance(instance, docl::IntegerType)

@given(instance=docl::IntegerType_strategy)
def test_docl::integertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::IntegerType_strategy)
def test_docl::integertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::BooleanType_strategy)
@settings(max_examples=50)
def test_docl::booleantype_instantiation(instance):
    assert isinstance(instance, docl::BooleanType)

@given(instance=docl::BooleanType_strategy)
def test_docl::booleantype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::BooleanType_strategy)
def test_docl::booleantype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::SetType_strategy)
@settings(max_examples=50)
def test_docl::settype_instantiation(instance):
    assert isinstance(instance, docl::SetType)

@given(instance=docl::SetType_strategy)
def test_docl::settype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::SetType_strategy)
def test_docl::settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::SequenceType_strategy)
@settings(max_examples=50)
def test_docl::sequencetype_instantiation(instance):
    assert isinstance(instance, docl::SequenceType)

@given(instance=docl::SequenceType_strategy)
def test_docl::sequencetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::SequenceType_strategy)
def test_docl::sequencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OclAnyType_strategy)
@settings(max_examples=50)
def test_docl::oclanytype_instantiation(instance):
    assert isinstance(instance, docl::OclAnyType)

@given(instance=docl::OclAnyType_strategy)
def test_docl::oclanytype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::OclAnyType_strategy)
def test_docl::oclanytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::MapType_strategy)
@settings(max_examples=50)
def test_docl::maptype_instantiation(instance):
    assert isinstance(instance, docl::MapType)

@given(instance=docl::MapType_strategy)
def test_docl::maptype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::MapType_strategy)
def test_docl::maptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OclModelElementExp_strategy)
@settings(max_examples=50)
def test_docl::oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, docl::OclModelElementExp)

@given(instance=docl::OclModelElementExp_strategy)
def test_docl::oclmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::OclModelElementExp_strategy)
def test_docl::oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=docl::Query_strategy)
@settings(max_examples=50)
def test_docl::query_instantiation(instance):
    assert isinstance(instance, docl::Query)

@given(instance=docl::Query_strategy)
def test_docl::query_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::Query_strategy)
def test_docl::query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::URI::_strategy)
@settings(max_examples=50)
def test_docl::uri::_instantiation(instance):
    assert isinstance(instance, docl::URI::)

@given(instance=docl::URI::_strategy)
def test_docl::uri::_fragment__type(instance):
    assert isinstance(instance.fragment_, str)


@given(instance=docl::URI::_strategy)
def test_docl::uri::_fragment__setter(instance):
    original = instance.fragment_
    instance.fragment_ = original
    assert instance.fragment_ == original

@given(instance=docl::URI::_strategy)
def test_docl::uri::_authority_type(instance):
    assert isinstance(instance.authority, str)


@given(instance=docl::URI::_strategy)
def test_docl::uri::_authority_setter(instance):
    original = instance.authority
    instance.authority = original
    assert instance.authority == original

@given(instance=docl::URI::_strategy)
def test_docl::uri::_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=docl::URI::_strategy)
def test_docl::uri::_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=docl::ModuleElement_strategy)
@settings(max_examples=50)
def test_docl::moduleelement_instantiation(instance):
    assert isinstance(instance, docl::ModuleElement)

@given(instance=docl::Import_strategy)
@settings(max_examples=50)
def test_docl::import_instantiation(instance):
    assert isinstance(instance, docl::Import)

@given(instance=docl::Import_strategy)
def test_docl::import_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::Import_strategy)
def test_docl::import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OclExpression_strategy)
@settings(max_examples=50)
def test_docl::oclexpression_instantiation(instance):
    assert isinstance(instance, docl::OclExpression)

@given(instance=docl::OclExpression_strategy)
def test_docl::oclexpression_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=docl::OclExpression_strategy)
def test_docl::oclexpression_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=docl::OclExpression_strategy)
def test_docl::oclexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::OclExpression_strategy)
def test_docl::oclexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::OclModel_strategy)
@settings(max_examples=50)
def test_docl::oclmodel_instantiation(instance):
    assert isinstance(instance, docl::OclModel)

@given(instance=docl::OclModel_strategy)
def test_docl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::OclModel_strategy)
def test_docl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::Module_strategy)
@settings(max_examples=50)
def test_docl::module_instantiation(instance):
    assert isinstance(instance, docl::Module)

@given(instance=docl::Module_strategy)
def test_docl::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::Module_strategy)
def test_docl::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
