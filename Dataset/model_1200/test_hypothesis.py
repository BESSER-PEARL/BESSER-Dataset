import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitiveExp,
    oCLlite::UnlimitedNaturalLiteralExp,
    oCLlite::StringLiteralExp,
    oCLlite::BooleanLiteralExp,
    oCLlite::NumberLiteralExp,
    oCLlite::TuplePart,
    oCLlite::MapElement,
    CollectionExp,
    oCLlite::SequenceExp,
    oCLlite::OrderedSetExp,
    oCLlite::SetExp,
    oCLlite::BagExp,
    OclLExpression,
    oCLlite::PrimitiveExp,
    oCLlite::MapExp,
    oCLlite::CollectionExp,
    OclLType,
    oCLlite::OclLModelElementExp,
    oCLlite::IfExp,
    oCLlite::NullLiteralExp,
    oCLlite::OclLExpression,
    ModuleElement,
    oCLlite::Query,
    oCLlite::URI::,
    oCLlite::ModuleElement,
    oCLlite::Import,
    oCLlite::OclLModel,
    oCLlite::Module,
    oCLlite::OclLType,
    oCLlite::Iterator,
    oCLlite::LocalVariable,
    oCLlite::NestedExp,
    oCLlite::SelfExp,
    oCLlite::NavigationOrAttributeCall,
    oCLlite::IteratorExp,
    oCLlite::IterateExp,
    oCLlite::CollectionOpCallExp,
    oCLlite::NavigationExp,
    oCLlite::MulOpCallExp,
    oCLlite::AddOpCallExp,
    oCLlite::ComOpCallExp,
    oCLlite::EqOpCallExp,
    oCLlite::ElseIfThenExp,
    oCLlite::TupleExp,
    oCLlite::LambdaExp,
    oCLlite::OperationCall,
    oCLlite::BagType,
    oCLlite::OrderedSetType,
    oCLlite::SequenceType,
    oCLlite::SetType,
    oCLlite::OclLAnyType,
    oCLlite::TupleType,
    oCLlite::MapType,
    oCLlite::LambdaType,
    oCLlite::EnvType,
    oCLlite::BoolOpCallExp,
    oCLlite::StringType,
    oCLlite::BooleanType,
    oCLlite::IntegerType,
    oCLlite::RealType,
    oCLlite::InvalidLiteralExp,
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



def test_ocllite::unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::UnlimitedNaturalLiteralExp)


def test_ocllite::unlimitednaturalliteralexp_constructor_exists():
    assert callable(oCLlite::UnlimitedNaturalLiteralExp.__init__)


def test_ocllite::unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::StringLiteralExp)


def test_ocllite::stringliteralexp_constructor_exists():
    assert callable(oCLlite::StringLiteralExp.__init__)


def test_ocllite::stringliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_ocllite::stringliteralexp_has_segments():
    assert hasattr(oCLlite::StringLiteralExp, "segments")
    descriptor = None
    for klass in oCLlite::StringLiteralExp.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::BooleanLiteralExp)


def test_ocllite::booleanliteralexp_constructor_exists():
    assert callable(oCLlite::BooleanLiteralExp.__init__)


def test_ocllite::booleanliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocllite::booleanliteralexp_has_symbol():
    assert hasattr(oCLlite::BooleanLiteralExp, "symbol")
    descriptor = None
    for klass in oCLlite::BooleanLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::NumberLiteralExp)


def test_ocllite::numberliteralexp_constructor_exists():
    assert callable(oCLlite::NumberLiteralExp.__init__)


def test_ocllite::numberliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocllite::numberliteralexp_has_symbol():
    assert hasattr(oCLlite::NumberLiteralExp, "symbol")
    descriptor = None
    for klass in oCLlite::NumberLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::tuplepart_is_not_abstract():
    assert not inspect.isabstract(oCLlite::TuplePart)


def test_ocllite::tuplepart_constructor_exists():
    assert callable(oCLlite::TuplePart.__init__)


def test_ocllite::tuplepart_constructor_args():
    sig = inspect.signature(oCLlite::TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::tuplepart_has_name():
    assert hasattr(oCLlite::TuplePart, "name")
    descriptor = None
    for klass in oCLlite::TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::mapelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite::MapElement)


def test_ocllite::mapelement_constructor_exists():
    assert callable(oCLlite::MapElement.__init__)


def test_ocllite::mapelement_constructor_args():
    sig = inspect.signature(oCLlite::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::SequenceExp)


def test_ocllite::sequenceexp_constructor_exists():
    assert callable(oCLlite::SequenceExp.__init__)


def test_ocllite::sequenceexp_constructor_args():
    sig = inspect.signature(oCLlite::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OrderedSetExp)


def test_ocllite::orderedsetexp_constructor_exists():
    assert callable(oCLlite::OrderedSetExp.__init__)


def test_ocllite::orderedsetexp_constructor_args():
    sig = inspect.signature(oCLlite::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::setexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::SetExp)


def test_ocllite::setexp_constructor_exists():
    assert callable(oCLlite::SetExp.__init__)


def test_ocllite::setexp_constructor_args():
    sig = inspect.signature(oCLlite::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::bagexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::BagExp)


def test_ocllite::bagexp_constructor_exists():
    assert callable(oCLlite::BagExp.__init__)


def test_ocllite::bagexp_constructor_args():
    sig = inspect.signature(oCLlite::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllexpression_is_not_abstract():
    assert not inspect.isabstract(OclLExpression)


def test_ocllexpression_constructor_exists():
    assert callable(OclLExpression.__init__)


def test_ocllexpression_constructor_args():
    sig = inspect.signature(OclLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::PrimitiveExp)


def test_ocllite::primitiveexp_constructor_exists():
    assert callable(oCLlite::PrimitiveExp.__init__)


def test_ocllite::primitiveexp_constructor_args():
    sig = inspect.signature(oCLlite::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::mapexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::MapExp)


def test_ocllite::mapexp_constructor_exists():
    assert callable(oCLlite::MapExp.__init__)


def test_ocllite::mapexp_constructor_args():
    sig = inspect.signature(oCLlite::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::collectionexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::CollectionExp)


def test_ocllite::collectionexp_constructor_exists():
    assert callable(oCLlite::CollectionExp.__init__)


def test_ocllite::collectionexp_constructor_args():
    sig = inspect.signature(oCLlite::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclltype_is_not_abstract():
    assert not inspect.isabstract(OclLType)


def test_oclltype_constructor_exists():
    assert callable(OclLType.__init__)


def test_oclltype_constructor_args():
    sig = inspect.signature(OclLType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::ocllmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OclLModelElementExp)


def test_ocllite::ocllmodelelementexp_constructor_exists():
    assert callable(oCLlite::OclLModelElementExp.__init__)


def test_ocllite::ocllmodelelementexp_constructor_args():
    sig = inspect.signature(oCLlite::OclLModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::ocllmodelelementexp_has_name():
    assert hasattr(oCLlite::OclLModelElementExp, "name")
    descriptor = None
    for klass in oCLlite::OclLModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::ifexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::IfExp)


def test_ocllite::ifexp_constructor_exists():
    assert callable(oCLlite::IfExp.__init__)


def test_ocllite::ifexp_constructor_args():
    sig = inspect.signature(oCLlite::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::NullLiteralExp)


def test_ocllite::nullliteralexp_constructor_exists():
    assert callable(oCLlite::NullLiteralExp.__init__)


def test_ocllite::nullliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::ocllexpression_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OclLExpression)


def test_ocllite::ocllexpression_constructor_exists():
    assert callable(oCLlite::OclLExpression.__init__)


def test_ocllite::ocllexpression_constructor_args():
    sig = inspect.signature(oCLlite::OclLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::ocllexpression_has_elements():
    assert hasattr(oCLlite::OclLExpression, "elements")
    descriptor = None
    for klass in oCLlite::OclLExpression.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_ocllite::ocllexpression_has_name():
    assert hasattr(oCLlite::OclLExpression, "name")
    descriptor = None
    for klass in oCLlite::OclLExpression.__mro__:
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



def test_ocllite::query_is_not_abstract():
    assert not inspect.isabstract(oCLlite::Query)


def test_ocllite::query_constructor_exists():
    assert callable(oCLlite::Query.__init__)


def test_ocllite::query_constructor_args():
    sig = inspect.signature(oCLlite::Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::query_has_name():
    assert hasattr(oCLlite::Query, "name")
    descriptor = None
    for klass in oCLlite::Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::uri::_is_not_abstract():
    assert not inspect.isabstract(oCLlite::URI::)


def test_ocllite::uri::_constructor_exists():
    assert callable(oCLlite::URI::.__init__)


def test_ocllite::uri::_constructor_args():
    sig = inspect.signature(oCLlite::URI::.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "authority" in params, "Missing parameter 'authority'"
    assert "fragment_" in params, "Missing parameter 'fragment_'"

def test_ocllite::uri::_has_scheme():
    assert hasattr(oCLlite::URI::, "scheme")
    descriptor = None
    for klass in oCLlite::URI::.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_ocllite::uri::_has_authority():
    assert hasattr(oCLlite::URI::, "authority")
    descriptor = None
    for klass in oCLlite::URI::.__mro__:
        if "authority" in klass.__dict__:
            descriptor = klass.__dict__["authority"]
            break
    assert isinstance(descriptor, property)

def test_ocllite::uri::_has_fragment_():
    assert hasattr(oCLlite::URI::, "fragment_")
    descriptor = None
    for klass in oCLlite::URI::.__mro__:
        if "fragment_" in klass.__dict__:
            descriptor = klass.__dict__["fragment_"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::moduleelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite::ModuleElement)


def test_ocllite::moduleelement_constructor_exists():
    assert callable(oCLlite::ModuleElement.__init__)


def test_ocllite::moduleelement_constructor_args():
    sig = inspect.signature(oCLlite::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::import_is_not_abstract():
    assert not inspect.isabstract(oCLlite::Import)


def test_ocllite::import_constructor_exists():
    assert callable(oCLlite::Import.__init__)


def test_ocllite::import_constructor_args():
    sig = inspect.signature(oCLlite::Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::import_has_name():
    assert hasattr(oCLlite::Import, "name")
    descriptor = None
    for klass in oCLlite::Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::ocllmodel_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OclLModel)


def test_ocllite::ocllmodel_constructor_exists():
    assert callable(oCLlite::OclLModel.__init__)


def test_ocllite::ocllmodel_constructor_args():
    sig = inspect.signature(oCLlite::OclLModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::ocllmodel_has_name():
    assert hasattr(oCLlite::OclLModel, "name")
    descriptor = None
    for klass in oCLlite::OclLModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::module_is_not_abstract():
    assert not inspect.isabstract(oCLlite::Module)


def test_ocllite::module_constructor_exists():
    assert callable(oCLlite::Module.__init__)


def test_ocllite::module_constructor_args():
    sig = inspect.signature(oCLlite::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::module_has_name():
    assert hasattr(oCLlite::Module, "name")
    descriptor = None
    for klass in oCLlite::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::oclltype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OclLType)


def test_ocllite::oclltype_constructor_exists():
    assert callable(oCLlite::OclLType.__init__)


def test_ocllite::oclltype_constructor_args():
    sig = inspect.signature(oCLlite::OclLType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::iterator_is_not_abstract():
    assert not inspect.isabstract(oCLlite::Iterator)


def test_ocllite::iterator_constructor_exists():
    assert callable(oCLlite::Iterator.__init__)


def test_ocllite::iterator_constructor_args():
    sig = inspect.signature(oCLlite::Iterator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::iterator_has_name():
    assert hasattr(oCLlite::Iterator, "name")
    descriptor = None
    for klass in oCLlite::Iterator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::localvariable_is_not_abstract():
    assert not inspect.isabstract(oCLlite::LocalVariable)


def test_ocllite::localvariable_constructor_exists():
    assert callable(oCLlite::LocalVariable.__init__)


def test_ocllite::localvariable_constructor_args():
    sig = inspect.signature(oCLlite::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::localvariable_has_name():
    assert hasattr(oCLlite::LocalVariable, "name")
    descriptor = None
    for klass in oCLlite::LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::nestedexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::NestedExp)


def test_ocllite::nestedexp_constructor_exists():
    assert callable(oCLlite::NestedExp.__init__)


def test_ocllite::nestedexp_constructor_args():
    sig = inspect.signature(oCLlite::NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::selfexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::SelfExp)


def test_ocllite::selfexp_constructor_exists():
    assert callable(oCLlite::SelfExp.__init__)


def test_ocllite::selfexp_constructor_args():
    sig = inspect.signature(oCLlite::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(oCLlite::NavigationOrAttributeCall)


def test_ocllite::navigationorattributecall_constructor_exists():
    assert callable(oCLlite::NavigationOrAttributeCall.__init__)


def test_ocllite::navigationorattributecall_constructor_args():
    sig = inspect.signature(oCLlite::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_ocllite::navigationorattributecall_has_feature():
    assert hasattr(oCLlite::NavigationOrAttributeCall, "feature")
    descriptor = None
    for klass in oCLlite::NavigationOrAttributeCall.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::IteratorExp)


def test_ocllite::iteratorexp_constructor_exists():
    assert callable(oCLlite::IteratorExp.__init__)


def test_ocllite::iteratorexp_constructor_args():
    sig = inspect.signature(oCLlite::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::iterateexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::IterateExp)


def test_ocllite::iterateexp_constructor_exists():
    assert callable(oCLlite::IterateExp.__init__)


def test_ocllite::iterateexp_constructor_args():
    sig = inspect.signature(oCLlite::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::collectionopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::CollectionOpCallExp)


def test_ocllite::collectionopcallexp_constructor_exists():
    assert callable(oCLlite::CollectionOpCallExp.__init__)


def test_ocllite::collectionopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::CollectionOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::navigationexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::NavigationExp)


def test_ocllite::navigationexp_constructor_exists():
    assert callable(oCLlite::NavigationExp.__init__)


def test_ocllite::navigationexp_constructor_args():
    sig = inspect.signature(oCLlite::NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::MulOpCallExp)


def test_ocllite::mulopcallexp_constructor_exists():
    assert callable(oCLlite::MulOpCallExp.__init__)


def test_ocllite::mulopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::AddOpCallExp)


def test_ocllite::addopcallexp_constructor_exists():
    assert callable(oCLlite::AddOpCallExp.__init__)


def test_ocllite::addopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::comopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::ComOpCallExp)


def test_ocllite::comopcallexp_constructor_exists():
    assert callable(oCLlite::ComOpCallExp.__init__)


def test_ocllite::comopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::ComOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::EqOpCallExp)


def test_ocllite::eqopcallexp_constructor_exists():
    assert callable(oCLlite::EqOpCallExp.__init__)


def test_ocllite::eqopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::elseifthenexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::ElseIfThenExp)


def test_ocllite::elseifthenexp_constructor_exists():
    assert callable(oCLlite::ElseIfThenExp.__init__)


def test_ocllite::elseifthenexp_constructor_args():
    sig = inspect.signature(oCLlite::ElseIfThenExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::tupleexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::TupleExp)


def test_ocllite::tupleexp_constructor_exists():
    assert callable(oCLlite::TupleExp.__init__)


def test_ocllite::tupleexp_constructor_args():
    sig = inspect.signature(oCLlite::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::lambdaexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::LambdaExp)


def test_ocllite::lambdaexp_constructor_exists():
    assert callable(oCLlite::LambdaExp.__init__)


def test_ocllite::lambdaexp_constructor_args():
    sig = inspect.signature(oCLlite::LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::operationcall_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OperationCall)


def test_ocllite::operationcall_constructor_exists():
    assert callable(oCLlite::OperationCall.__init__)


def test_ocllite::operationcall_constructor_args():
    sig = inspect.signature(oCLlite::OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::bagtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::BagType)


def test_ocllite::bagtype_constructor_exists():
    assert callable(oCLlite::BagType.__init__)


def test_ocllite::bagtype_constructor_args():
    sig = inspect.signature(oCLlite::BagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::bagtype_has_name():
    assert hasattr(oCLlite::BagType, "name")
    descriptor = None
    for klass in oCLlite::BagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OrderedSetType)


def test_ocllite::orderedsettype_constructor_exists():
    assert callable(oCLlite::OrderedSetType.__init__)


def test_ocllite::orderedsettype_constructor_args():
    sig = inspect.signature(oCLlite::OrderedSetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::orderedsettype_has_name():
    assert hasattr(oCLlite::OrderedSetType, "name")
    descriptor = None
    for klass in oCLlite::OrderedSetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::sequencetype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::SequenceType)


def test_ocllite::sequencetype_constructor_exists():
    assert callable(oCLlite::SequenceType.__init__)


def test_ocllite::sequencetype_constructor_args():
    sig = inspect.signature(oCLlite::SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::sequencetype_has_name():
    assert hasattr(oCLlite::SequenceType, "name")
    descriptor = None
    for klass in oCLlite::SequenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::settype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::SetType)


def test_ocllite::settype_constructor_exists():
    assert callable(oCLlite::SetType.__init__)


def test_ocllite::settype_constructor_args():
    sig = inspect.signature(oCLlite::SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::settype_has_name():
    assert hasattr(oCLlite::SetType, "name")
    descriptor = None
    for klass in oCLlite::SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::ocllanytype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::OclLAnyType)


def test_ocllite::ocllanytype_constructor_exists():
    assert callable(oCLlite::OclLAnyType.__init__)


def test_ocllite::ocllanytype_constructor_args():
    sig = inspect.signature(oCLlite::OclLAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::ocllanytype_has_name():
    assert hasattr(oCLlite::OclLAnyType, "name")
    descriptor = None
    for klass in oCLlite::OclLAnyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::tupletype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::TupleType)


def test_ocllite::tupletype_constructor_exists():
    assert callable(oCLlite::TupleType.__init__)


def test_ocllite::tupletype_constructor_args():
    sig = inspect.signature(oCLlite::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::maptype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::MapType)


def test_ocllite::maptype_constructor_exists():
    assert callable(oCLlite::MapType.__init__)


def test_ocllite::maptype_constructor_args():
    sig = inspect.signature(oCLlite::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::maptype_has_name():
    assert hasattr(oCLlite::MapType, "name")
    descriptor = None
    for klass in oCLlite::MapType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::lambdatype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::LambdaType)


def test_ocllite::lambdatype_constructor_exists():
    assert callable(oCLlite::LambdaType.__init__)


def test_ocllite::lambdatype_constructor_args():
    sig = inspect.signature(oCLlite::LambdaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::lambdatype_has_name():
    assert hasattr(oCLlite::LambdaType, "name")
    descriptor = None
    for klass in oCLlite::LambdaType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::envtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::EnvType)


def test_ocllite::envtype_constructor_exists():
    assert callable(oCLlite::EnvType.__init__)


def test_ocllite::envtype_constructor_args():
    sig = inspect.signature(oCLlite::EnvType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::envtype_has_name():
    assert hasattr(oCLlite::EnvType, "name")
    descriptor = None
    for klass in oCLlite::EnvType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::boolopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::BoolOpCallExp)


def test_ocllite::boolopcallexp_constructor_exists():
    assert callable(oCLlite::BoolOpCallExp.__init__)


def test_ocllite::boolopcallexp_constructor_args():
    sig = inspect.signature(oCLlite::BoolOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite::stringtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::StringType)


def test_ocllite::stringtype_constructor_exists():
    assert callable(oCLlite::StringType.__init__)


def test_ocllite::stringtype_constructor_args():
    sig = inspect.signature(oCLlite::StringType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::stringtype_has_name():
    assert hasattr(oCLlite::StringType, "name")
    descriptor = None
    for klass in oCLlite::StringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::booleantype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::BooleanType)


def test_ocllite::booleantype_constructor_exists():
    assert callable(oCLlite::BooleanType.__init__)


def test_ocllite::booleantype_constructor_args():
    sig = inspect.signature(oCLlite::BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::booleantype_has_name():
    assert hasattr(oCLlite::BooleanType, "name")
    descriptor = None
    for klass in oCLlite::BooleanType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::integertype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::IntegerType)


def test_ocllite::integertype_constructor_exists():
    assert callable(oCLlite::IntegerType.__init__)


def test_ocllite::integertype_constructor_args():
    sig = inspect.signature(oCLlite::IntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::integertype_has_name():
    assert hasattr(oCLlite::IntegerType, "name")
    descriptor = None
    for klass in oCLlite::IntegerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::realtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite::RealType)


def test_ocllite::realtype_constructor_exists():
    assert callable(oCLlite::RealType.__init__)


def test_ocllite::realtype_constructor_args():
    sig = inspect.signature(oCLlite::RealType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite::realtype_has_name():
    assert hasattr(oCLlite::RealType, "name")
    descriptor = None
    for klass in oCLlite::RealType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite::InvalidLiteralExp)


def test_ocllite::invalidliteralexp_constructor_exists():
    assert callable(oCLlite::InvalidLiteralExp.__init__)


def test_ocllite::invalidliteralexp_constructor_args():
    sig = inspect.signature(oCLlite::InvalidLiteralExp.__init__)
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
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
oCLlite::UnlimitedNaturalLiteralExp_strategy = st.builds(
    oCLlite::UnlimitedNaturalLiteralExp,
)
oCLlite::StringLiteralExp_strategy = st.builds(
    oCLlite::StringLiteralExp,
    segments=
        safe_text
)
oCLlite::BooleanLiteralExp_strategy = st.builds(
    oCLlite::BooleanLiteralExp,
    symbol=
        safe_text
)
oCLlite::NumberLiteralExp_strategy = st.builds(
    oCLlite::NumberLiteralExp,
    symbol=
        st.integers()
)
oCLlite::TuplePart_strategy = st.builds(
    oCLlite::TuplePart,
    name=
        safe_text
)
oCLlite::MapElement_strategy = st.builds(
    oCLlite::MapElement,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
oCLlite::SequenceExp_strategy = st.builds(
    oCLlite::SequenceExp,
)
oCLlite::OrderedSetExp_strategy = st.builds(
    oCLlite::OrderedSetExp,
)
oCLlite::SetExp_strategy = st.builds(
    oCLlite::SetExp,
)
oCLlite::BagExp_strategy = st.builds(
    oCLlite::BagExp,
)
OclLExpression_strategy = st.builds(
    OclLExpression,
)
oCLlite::PrimitiveExp_strategy = st.builds(
    oCLlite::PrimitiveExp,
)
oCLlite::MapExp_strategy = st.builds(
    oCLlite::MapExp,
)
oCLlite::CollectionExp_strategy = st.builds(
    oCLlite::CollectionExp,
)
OclLType_strategy = st.builds(
    OclLType,
)
oCLlite::OclLModelElementExp_strategy = st.builds(
    oCLlite::OclLModelElementExp,
    name=
        safe_text
)
oCLlite::IfExp_strategy = st.builds(
    oCLlite::IfExp,
)
oCLlite::NullLiteralExp_strategy = st.builds(
    oCLlite::NullLiteralExp,
)
oCLlite::OclLExpression_strategy = st.builds(
    oCLlite::OclLExpression,
    elements=
        safe_text,
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
oCLlite::Query_strategy = st.builds(
    oCLlite::Query,
    name=
        safe_text
)
oCLlite::URI::_strategy = st.builds(
    oCLlite::URI::,
    scheme=
        safe_text,
    authority=
        safe_text,
    fragment_=
        safe_text
)
oCLlite::ModuleElement_strategy = st.builds(
    oCLlite::ModuleElement,
)
oCLlite::Import_strategy = st.builds(
    oCLlite::Import,
    name=
        safe_text
)
oCLlite::OclLModel_strategy = st.builds(
    oCLlite::OclLModel,
    name=
        safe_text
)
oCLlite::Module_strategy = st.builds(
    oCLlite::Module,
    name=
        safe_text
)
oCLlite::OclLType_strategy = st.builds(
    oCLlite::OclLType,
)
oCLlite::Iterator_strategy = st.builds(
    oCLlite::Iterator,
    name=
        safe_text
)
oCLlite::LocalVariable_strategy = st.builds(
    oCLlite::LocalVariable,
    name=
        safe_text
)
oCLlite::NestedExp_strategy = st.builds(
    oCLlite::NestedExp,
)
oCLlite::SelfExp_strategy = st.builds(
    oCLlite::SelfExp,
)
oCLlite::NavigationOrAttributeCall_strategy = st.builds(
    oCLlite::NavigationOrAttributeCall,
    feature=
        safe_text
)
oCLlite::IteratorExp_strategy = st.builds(
    oCLlite::IteratorExp,
)
oCLlite::IterateExp_strategy = st.builds(
    oCLlite::IterateExp,
)
oCLlite::CollectionOpCallExp_strategy = st.builds(
    oCLlite::CollectionOpCallExp,
)
oCLlite::NavigationExp_strategy = st.builds(
    oCLlite::NavigationExp,
)
oCLlite::MulOpCallExp_strategy = st.builds(
    oCLlite::MulOpCallExp,
)
oCLlite::AddOpCallExp_strategy = st.builds(
    oCLlite::AddOpCallExp,
)
oCLlite::ComOpCallExp_strategy = st.builds(
    oCLlite::ComOpCallExp,
)
oCLlite::EqOpCallExp_strategy = st.builds(
    oCLlite::EqOpCallExp,
)
oCLlite::ElseIfThenExp_strategy = st.builds(
    oCLlite::ElseIfThenExp,
)
oCLlite::TupleExp_strategy = st.builds(
    oCLlite::TupleExp,
)
oCLlite::LambdaExp_strategy = st.builds(
    oCLlite::LambdaExp,
)
oCLlite::OperationCall_strategy = st.builds(
    oCLlite::OperationCall,
)
oCLlite::BagType_strategy = st.builds(
    oCLlite::BagType,
    name=
        safe_text
)
oCLlite::OrderedSetType_strategy = st.builds(
    oCLlite::OrderedSetType,
    name=
        safe_text
)
oCLlite::SequenceType_strategy = st.builds(
    oCLlite::SequenceType,
    name=
        safe_text
)
oCLlite::SetType_strategy = st.builds(
    oCLlite::SetType,
    name=
        safe_text
)
oCLlite::OclLAnyType_strategy = st.builds(
    oCLlite::OclLAnyType,
    name=
        safe_text
)
oCLlite::TupleType_strategy = st.builds(
    oCLlite::TupleType,
)
oCLlite::MapType_strategy = st.builds(
    oCLlite::MapType,
    name=
        safe_text
)
oCLlite::LambdaType_strategy = st.builds(
    oCLlite::LambdaType,
    name=
        safe_text
)
oCLlite::EnvType_strategy = st.builds(
    oCLlite::EnvType,
    name=
        safe_text
)
oCLlite::BoolOpCallExp_strategy = st.builds(
    oCLlite::BoolOpCallExp,
)
oCLlite::StringType_strategy = st.builds(
    oCLlite::StringType,
    name=
        safe_text
)
oCLlite::BooleanType_strategy = st.builds(
    oCLlite::BooleanType,
    name=
        safe_text
)
oCLlite::IntegerType_strategy = st.builds(
    oCLlite::IntegerType,
    name=
        safe_text
)
oCLlite::RealType_strategy = st.builds(
    oCLlite::RealType,
    name=
        safe_text
)
oCLlite::InvalidLiteralExp_strategy = st.builds(
    oCLlite::InvalidLiteralExp,
)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=oCLlite::UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::UnlimitedNaturalLiteralExp)

@given(instance=oCLlite::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::stringliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::StringLiteralExp)

@given(instance=oCLlite::StringLiteralExp_strategy)
def test_ocllite::stringliteralexp_segments_type(instance):
    assert isinstance(instance.segments, str)


@given(instance=oCLlite::StringLiteralExp_strategy)
def test_ocllite::stringliteralexp_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=oCLlite::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::BooleanLiteralExp)

@given(instance=oCLlite::BooleanLiteralExp_strategy)
def test_ocllite::booleanliteralexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=oCLlite::BooleanLiteralExp_strategy)
def test_ocllite::booleanliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=oCLlite::NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::numberliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::NumberLiteralExp)

@given(instance=oCLlite::NumberLiteralExp_strategy)
def test_ocllite::numberliteralexp_symbol_type(instance):
    assert isinstance(instance.symbol, int)


@given(instance=oCLlite::NumberLiteralExp_strategy)
def test_ocllite::numberliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=oCLlite::TuplePart_strategy)
@settings(max_examples=50)
def test_ocllite::tuplepart_instantiation(instance):
    assert isinstance(instance, oCLlite::TuplePart)

@given(instance=oCLlite::TuplePart_strategy)
def test_ocllite::tuplepart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::TuplePart_strategy)
def test_ocllite::tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::MapElement_strategy)
@settings(max_examples=50)
def test_ocllite::mapelement_instantiation(instance):
    assert isinstance(instance, oCLlite::MapElement)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=oCLlite::SequenceExp_strategy)
@settings(max_examples=50)
def test_ocllite::sequenceexp_instantiation(instance):
    assert isinstance(instance, oCLlite::SequenceExp)

@given(instance=oCLlite::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_ocllite::orderedsetexp_instantiation(instance):
    assert isinstance(instance, oCLlite::OrderedSetExp)

@given(instance=oCLlite::SetExp_strategy)
@settings(max_examples=50)
def test_ocllite::setexp_instantiation(instance):
    assert isinstance(instance, oCLlite::SetExp)

@given(instance=oCLlite::BagExp_strategy)
@settings(max_examples=50)
def test_ocllite::bagexp_instantiation(instance):
    assert isinstance(instance, oCLlite::BagExp)

@given(instance=OclLExpression_strategy)
@settings(max_examples=50)
def test_ocllexpression_instantiation(instance):
    assert isinstance(instance, OclLExpression)

@given(instance=oCLlite::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_ocllite::primitiveexp_instantiation(instance):
    assert isinstance(instance, oCLlite::PrimitiveExp)

@given(instance=oCLlite::MapExp_strategy)
@settings(max_examples=50)
def test_ocllite::mapexp_instantiation(instance):
    assert isinstance(instance, oCLlite::MapExp)

@given(instance=oCLlite::CollectionExp_strategy)
@settings(max_examples=50)
def test_ocllite::collectionexp_instantiation(instance):
    assert isinstance(instance, oCLlite::CollectionExp)

@given(instance=OclLType_strategy)
@settings(max_examples=50)
def test_oclltype_instantiation(instance):
    assert isinstance(instance, OclLType)

@given(instance=oCLlite::OclLModelElementExp_strategy)
@settings(max_examples=50)
def test_ocllite::ocllmodelelementexp_instantiation(instance):
    assert isinstance(instance, oCLlite::OclLModelElementExp)

@given(instance=oCLlite::OclLModelElementExp_strategy)
def test_ocllite::ocllmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::OclLModelElementExp_strategy)
def test_ocllite::ocllmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::IfExp_strategy)
@settings(max_examples=50)
def test_ocllite::ifexp_instantiation(instance):
    assert isinstance(instance, oCLlite::IfExp)

@given(instance=oCLlite::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::nullliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::NullLiteralExp)

@given(instance=oCLlite::OclLExpression_strategy)
@settings(max_examples=50)
def test_ocllite::ocllexpression_instantiation(instance):
    assert isinstance(instance, oCLlite::OclLExpression)

@given(instance=oCLlite::OclLExpression_strategy)
def test_ocllite::ocllexpression_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=oCLlite::OclLExpression_strategy)
def test_ocllite::ocllexpression_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=oCLlite::OclLExpression_strategy)
def test_ocllite::ocllexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::OclLExpression_strategy)
def test_ocllite::ocllexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=oCLlite::Query_strategy)
@settings(max_examples=50)
def test_ocllite::query_instantiation(instance):
    assert isinstance(instance, oCLlite::Query)

@given(instance=oCLlite::Query_strategy)
def test_ocllite::query_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::Query_strategy)
def test_ocllite::query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::URI::_strategy)
@settings(max_examples=50)
def test_ocllite::uri::_instantiation(instance):
    assert isinstance(instance, oCLlite::URI::)

@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_authority_type(instance):
    assert isinstance(instance.authority, str)


@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_authority_setter(instance):
    original = instance.authority
    instance.authority = original
    assert instance.authority == original

@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_fragment__type(instance):
    assert isinstance(instance.fragment_, str)


@given(instance=oCLlite::URI::_strategy)
def test_ocllite::uri::_fragment__setter(instance):
    original = instance.fragment_
    instance.fragment_ = original
    assert instance.fragment_ == original

@given(instance=oCLlite::ModuleElement_strategy)
@settings(max_examples=50)
def test_ocllite::moduleelement_instantiation(instance):
    assert isinstance(instance, oCLlite::ModuleElement)

@given(instance=oCLlite::Import_strategy)
@settings(max_examples=50)
def test_ocllite::import_instantiation(instance):
    assert isinstance(instance, oCLlite::Import)

@given(instance=oCLlite::Import_strategy)
def test_ocllite::import_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::Import_strategy)
def test_ocllite::import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::OclLModel_strategy)
@settings(max_examples=50)
def test_ocllite::ocllmodel_instantiation(instance):
    assert isinstance(instance, oCLlite::OclLModel)

@given(instance=oCLlite::OclLModel_strategy)
def test_ocllite::ocllmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::OclLModel_strategy)
def test_ocllite::ocllmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::Module_strategy)
@settings(max_examples=50)
def test_ocllite::module_instantiation(instance):
    assert isinstance(instance, oCLlite::Module)

@given(instance=oCLlite::Module_strategy)
def test_ocllite::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::Module_strategy)
def test_ocllite::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::OclLType_strategy)
@settings(max_examples=50)
def test_ocllite::oclltype_instantiation(instance):
    assert isinstance(instance, oCLlite::OclLType)

@given(instance=oCLlite::Iterator_strategy)
@settings(max_examples=50)
def test_ocllite::iterator_instantiation(instance):
    assert isinstance(instance, oCLlite::Iterator)

@given(instance=oCLlite::Iterator_strategy)
def test_ocllite::iterator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::Iterator_strategy)
def test_ocllite::iterator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::LocalVariable_strategy)
@settings(max_examples=50)
def test_ocllite::localvariable_instantiation(instance):
    assert isinstance(instance, oCLlite::LocalVariable)

@given(instance=oCLlite::LocalVariable_strategy)
def test_ocllite::localvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::LocalVariable_strategy)
def test_ocllite::localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::NestedExp_strategy)
@settings(max_examples=50)
def test_ocllite::nestedexp_instantiation(instance):
    assert isinstance(instance, oCLlite::NestedExp)

@given(instance=oCLlite::SelfExp_strategy)
@settings(max_examples=50)
def test_ocllite::selfexp_instantiation(instance):
    assert isinstance(instance, oCLlite::SelfExp)

@given(instance=oCLlite::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_ocllite::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, oCLlite::NavigationOrAttributeCall)

@given(instance=oCLlite::NavigationOrAttributeCall_strategy)
def test_ocllite::navigationorattributecall_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=oCLlite::NavigationOrAttributeCall_strategy)
def test_ocllite::navigationorattributecall_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=oCLlite::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocllite::iteratorexp_instantiation(instance):
    assert isinstance(instance, oCLlite::IteratorExp)

@given(instance=oCLlite::IterateExp_strategy)
@settings(max_examples=50)
def test_ocllite::iterateexp_instantiation(instance):
    assert isinstance(instance, oCLlite::IterateExp)

@given(instance=oCLlite::CollectionOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::collectionopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::CollectionOpCallExp)

@given(instance=oCLlite::NavigationExp_strategy)
@settings(max_examples=50)
def test_ocllite::navigationexp_instantiation(instance):
    assert isinstance(instance, oCLlite::NavigationExp)

@given(instance=oCLlite::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::mulopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::MulOpCallExp)

@given(instance=oCLlite::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::addopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::AddOpCallExp)

@given(instance=oCLlite::ComOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::comopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::ComOpCallExp)

@given(instance=oCLlite::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::eqopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::EqOpCallExp)

@given(instance=oCLlite::ElseIfThenExp_strategy)
@settings(max_examples=50)
def test_ocllite::elseifthenexp_instantiation(instance):
    assert isinstance(instance, oCLlite::ElseIfThenExp)

@given(instance=oCLlite::TupleExp_strategy)
@settings(max_examples=50)
def test_ocllite::tupleexp_instantiation(instance):
    assert isinstance(instance, oCLlite::TupleExp)

@given(instance=oCLlite::LambdaExp_strategy)
@settings(max_examples=50)
def test_ocllite::lambdaexp_instantiation(instance):
    assert isinstance(instance, oCLlite::LambdaExp)

@given(instance=oCLlite::OperationCall_strategy)
@settings(max_examples=50)
def test_ocllite::operationcall_instantiation(instance):
    assert isinstance(instance, oCLlite::OperationCall)

@given(instance=oCLlite::BagType_strategy)
@settings(max_examples=50)
def test_ocllite::bagtype_instantiation(instance):
    assert isinstance(instance, oCLlite::BagType)

@given(instance=oCLlite::BagType_strategy)
def test_ocllite::bagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::BagType_strategy)
def test_ocllite::bagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocllite::orderedsettype_instantiation(instance):
    assert isinstance(instance, oCLlite::OrderedSetType)

@given(instance=oCLlite::OrderedSetType_strategy)
def test_ocllite::orderedsettype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::OrderedSetType_strategy)
def test_ocllite::orderedsettype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::SequenceType_strategy)
@settings(max_examples=50)
def test_ocllite::sequencetype_instantiation(instance):
    assert isinstance(instance, oCLlite::SequenceType)

@given(instance=oCLlite::SequenceType_strategy)
def test_ocllite::sequencetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::SequenceType_strategy)
def test_ocllite::sequencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::SetType_strategy)
@settings(max_examples=50)
def test_ocllite::settype_instantiation(instance):
    assert isinstance(instance, oCLlite::SetType)

@given(instance=oCLlite::SetType_strategy)
def test_ocllite::settype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::SetType_strategy)
def test_ocllite::settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::OclLAnyType_strategy)
@settings(max_examples=50)
def test_ocllite::ocllanytype_instantiation(instance):
    assert isinstance(instance, oCLlite::OclLAnyType)

@given(instance=oCLlite::OclLAnyType_strategy)
def test_ocllite::ocllanytype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::OclLAnyType_strategy)
def test_ocllite::ocllanytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::TupleType_strategy)
@settings(max_examples=50)
def test_ocllite::tupletype_instantiation(instance):
    assert isinstance(instance, oCLlite::TupleType)

@given(instance=oCLlite::MapType_strategy)
@settings(max_examples=50)
def test_ocllite::maptype_instantiation(instance):
    assert isinstance(instance, oCLlite::MapType)

@given(instance=oCLlite::MapType_strategy)
def test_ocllite::maptype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::MapType_strategy)
def test_ocllite::maptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::LambdaType_strategy)
@settings(max_examples=50)
def test_ocllite::lambdatype_instantiation(instance):
    assert isinstance(instance, oCLlite::LambdaType)

@given(instance=oCLlite::LambdaType_strategy)
def test_ocllite::lambdatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::LambdaType_strategy)
def test_ocllite::lambdatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::EnvType_strategy)
@settings(max_examples=50)
def test_ocllite::envtype_instantiation(instance):
    assert isinstance(instance, oCLlite::EnvType)

@given(instance=oCLlite::EnvType_strategy)
def test_ocllite::envtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::EnvType_strategy)
def test_ocllite::envtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::BoolOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite::boolopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite::BoolOpCallExp)

@given(instance=oCLlite::StringType_strategy)
@settings(max_examples=50)
def test_ocllite::stringtype_instantiation(instance):
    assert isinstance(instance, oCLlite::StringType)

@given(instance=oCLlite::StringType_strategy)
def test_ocllite::stringtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::StringType_strategy)
def test_ocllite::stringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::BooleanType_strategy)
@settings(max_examples=50)
def test_ocllite::booleantype_instantiation(instance):
    assert isinstance(instance, oCLlite::BooleanType)

@given(instance=oCLlite::BooleanType_strategy)
def test_ocllite::booleantype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::BooleanType_strategy)
def test_ocllite::booleantype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::IntegerType_strategy)
@settings(max_examples=50)
def test_ocllite::integertype_instantiation(instance):
    assert isinstance(instance, oCLlite::IntegerType)

@given(instance=oCLlite::IntegerType_strategy)
def test_ocllite::integertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::IntegerType_strategy)
def test_ocllite::integertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::RealType_strategy)
@settings(max_examples=50)
def test_ocllite::realtype_instantiation(instance):
    assert isinstance(instance, oCLlite::RealType)

@given(instance=oCLlite::RealType_strategy)
def test_ocllite::realtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oCLlite::RealType_strategy)
def test_ocllite::realtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite::InvalidLiteralExp)
