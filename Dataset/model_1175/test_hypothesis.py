import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OCLinEmig::Module,
    OCLinEmig::LocatedElement,
    OclFeature,
    CollectionType,
    OCLinEmig::OrderedSetType,
    OCLinEmig::SetType,
    OCLinEmig::SequenceType,
    OCLinEmig::BagType,
    NumericType,
    OCLinEmig::RealType,
    OCLinEmig::IntegerType,
    Primitive,
    OCLinEmig::NumericType,
    OCLinEmig::BooleanType,
    OCLinEmig::StringType,
    OclType,
    OCLinEmig::Primitive,
    OCLinEmig::OclAnyType,
    OCLinEmig::TupleType,
    OCLinEmig::OclModelElement,
    OCLinEmig::CollectionType,
    OCLinEmig::MapType,
    LoopExp,
    OCLinEmig::IteratorExp,
    OCLinEmig::IterateExp,
    OperationCallExp,
    OCLinEmig::CollectionOperationCallExp,
    OCLinEmig::OperatorCallExp,
    VariableDeclaration,
    OCLinEmig::Iterator,
    OCLinEmig::Parameter,
    OCLinEmig::TuplePart,
    CollectionExp,
    OCLinEmig::OrderedSetExp,
    OCLinEmig::SequenceExp,
    OCLinEmig::SetExp,
    OCLinEmig::BagExp,
    PropertyCallExp,
    OCLinEmig::NavigationOrAttributeCallExp,
    PrimitiveExp,
    OCLinEmig::StringExp,
    OclExpression,
    OCLinEmig::OclUndefinedExp,
    OCLinEmig::EnumLiteralExp,
    OCLinEmig::SuperExp,
    OCLinEmig::TupleExp,
    OCLinEmig::PrimitiveExp,
    OCLinEmig::MapExp,
    OCLinEmig::VariableExp,
    OCLinEmig::Attribute,
    OCLinEmig::Operation,
    OCLinEmig::OperationCallExp,
    OCLinEmig::LoopExp,
    OCLinEmig::LetExp,
    NumericExp,
    OCLinEmig::IntegerExp,
    OCLinEmig::RealExp,
    OCLinEmig::NumericExp,
    OCLinEmig::BooleanExp,
    LocatedElement,
    OCLinEmig::VariableDeclaration,
    OCLinEmig::OclFeature,
    OCLinEmig::OclModel,
    OCLinEmig::MapElement,
    OCLinEmig::OclFeatureDefinition,
    OCLinEmig::TupleTypeAttribute,
    OCLinEmig::OclContextDefinition,
    OCLinEmig::OclExpression,
    OCLinEmig::CollectionExp,
    OCLinEmig::PropertyCallExp,
    OCLinEmig::IfExp,
    OCLinEmig::OclType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclinemig::module_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Module)


def test_oclinemig::module_constructor_exists():
    assert callable(OCLinEmig::Module.__init__)


def test_oclinemig::module_constructor_args():
    sig = inspect.signature(OCLinEmig::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::module_has_name():
    assert hasattr(OCLinEmig::Module, "name")
    descriptor = None
    for klass in OCLinEmig::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::locatedelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::LocatedElement)


def test_oclinemig::locatedelement_constructor_exists():
    assert callable(OCLinEmig::LocatedElement.__init__)


def test_oclinemig::locatedelement_constructor_args():
    sig = inspect.signature(OCLinEmig::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_oclinemig::locatedelement_has_location():
    assert hasattr(OCLinEmig::LocatedElement, "location")
    descriptor = None
    for klass in OCLinEmig::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig::locatedelement_has_commentsAfter():
    assert hasattr(OCLinEmig::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in OCLinEmig::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig::locatedelement_has_commentsBefore():
    assert hasattr(OCLinEmig::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in OCLinEmig::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OrderedSetType)


def test_oclinemig::orderedsettype_constructor_exists():
    assert callable(OCLinEmig::OrderedSetType.__init__)


def test_oclinemig::orderedsettype_constructor_args():
    sig = inspect.signature(OCLinEmig::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::settype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::SetType)


def test_oclinemig::settype_constructor_exists():
    assert callable(OCLinEmig::SetType.__init__)


def test_oclinemig::settype_constructor_args():
    sig = inspect.signature(OCLinEmig::SetType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::SequenceType)


def test_oclinemig::sequencetype_constructor_exists():
    assert callable(OCLinEmig::SequenceType.__init__)


def test_oclinemig::sequencetype_constructor_args():
    sig = inspect.signature(OCLinEmig::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::bagtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::BagType)


def test_oclinemig::bagtype_constructor_exists():
    assert callable(OCLinEmig::BagType.__init__)


def test_oclinemig::bagtype_constructor_args():
    sig = inspect.signature(OCLinEmig::BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::realtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::RealType)


def test_oclinemig::realtype_constructor_exists():
    assert callable(OCLinEmig::RealType.__init__)


def test_oclinemig::realtype_constructor_args():
    sig = inspect.signature(OCLinEmig::RealType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::integertype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::IntegerType)


def test_oclinemig::integertype_constructor_exists():
    assert callable(OCLinEmig::IntegerType.__init__)


def test_oclinemig::integertype_constructor_args():
    sig = inspect.signature(OCLinEmig::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::numerictype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::NumericType)


def test_oclinemig::numerictype_constructor_exists():
    assert callable(OCLinEmig::NumericType.__init__)


def test_oclinemig::numerictype_constructor_args():
    sig = inspect.signature(OCLinEmig::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::booleantype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::BooleanType)


def test_oclinemig::booleantype_constructor_exists():
    assert callable(OCLinEmig::BooleanType.__init__)


def test_oclinemig::booleantype_constructor_args():
    sig = inspect.signature(OCLinEmig::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::stringtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::StringType)


def test_oclinemig::stringtype_constructor_exists():
    assert callable(OCLinEmig::StringType.__init__)


def test_oclinemig::stringtype_constructor_args():
    sig = inspect.signature(OCLinEmig::StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::primitive_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Primitive)


def test_oclinemig::primitive_constructor_exists():
    assert callable(OCLinEmig::Primitive.__init__)


def test_oclinemig::primitive_constructor_args():
    sig = inspect.signature(OCLinEmig::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclanytype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclAnyType)


def test_oclinemig::oclanytype_constructor_exists():
    assert callable(OCLinEmig::OclAnyType.__init__)


def test_oclinemig::oclanytype_constructor_args():
    sig = inspect.signature(OCLinEmig::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::tupletype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::TupleType)


def test_oclinemig::tupletype_constructor_exists():
    assert callable(OCLinEmig::TupleType.__init__)


def test_oclinemig::tupletype_constructor_args():
    sig = inspect.signature(OCLinEmig::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclModelElement)


def test_oclinemig::oclmodelelement_constructor_exists():
    assert callable(OCLinEmig::OclModelElement.__init__)


def test_oclinemig::oclmodelelement_constructor_args():
    sig = inspect.signature(OCLinEmig::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::CollectionType)


def test_oclinemig::collectiontype_constructor_exists():
    assert callable(OCLinEmig::CollectionType.__init__)


def test_oclinemig::collectiontype_constructor_args():
    sig = inspect.signature(OCLinEmig::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::maptype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::MapType)


def test_oclinemig::maptype_constructor_exists():
    assert callable(OCLinEmig::MapType.__init__)


def test_oclinemig::maptype_constructor_args():
    sig = inspect.signature(OCLinEmig::MapType.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::IteratorExp)


def test_oclinemig::iteratorexp_constructor_exists():
    assert callable(OCLinEmig::IteratorExp.__init__)


def test_oclinemig::iteratorexp_constructor_args():
    sig = inspect.signature(OCLinEmig::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::iteratorexp_has_name():
    assert hasattr(OCLinEmig::IteratorExp, "name")
    descriptor = None
    for klass in OCLinEmig::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::IterateExp)


def test_oclinemig::iterateexp_constructor_exists():
    assert callable(OCLinEmig::IterateExp.__init__)


def test_oclinemig::iterateexp_constructor_args():
    sig = inspect.signature(OCLinEmig::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::CollectionOperationCallExp)


def test_oclinemig::collectionoperationcallexp_constructor_exists():
    assert callable(OCLinEmig::CollectionOperationCallExp.__init__)


def test_oclinemig::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OperatorCallExp)


def test_oclinemig::operatorcallexp_constructor_exists():
    assert callable(OCLinEmig::OperatorCallExp.__init__)


def test_oclinemig::operatorcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::iterator_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Iterator)


def test_oclinemig::iterator_constructor_exists():
    assert callable(OCLinEmig::Iterator.__init__)


def test_oclinemig::iterator_constructor_args():
    sig = inspect.signature(OCLinEmig::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::parameter_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Parameter)


def test_oclinemig::parameter_constructor_exists():
    assert callable(OCLinEmig::Parameter.__init__)


def test_oclinemig::parameter_constructor_args():
    sig = inspect.signature(OCLinEmig::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::tuplepart_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::TuplePart)


def test_oclinemig::tuplepart_constructor_exists():
    assert callable(OCLinEmig::TuplePart.__init__)


def test_oclinemig::tuplepart_constructor_args():
    sig = inspect.signature(OCLinEmig::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OrderedSetExp)


def test_oclinemig::orderedsetexp_constructor_exists():
    assert callable(OCLinEmig::OrderedSetExp.__init__)


def test_oclinemig::orderedsetexp_constructor_args():
    sig = inspect.signature(OCLinEmig::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::SequenceExp)


def test_oclinemig::sequenceexp_constructor_exists():
    assert callable(OCLinEmig::SequenceExp.__init__)


def test_oclinemig::sequenceexp_constructor_args():
    sig = inspect.signature(OCLinEmig::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::setexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::SetExp)


def test_oclinemig::setexp_constructor_exists():
    assert callable(OCLinEmig::SetExp.__init__)


def test_oclinemig::setexp_constructor_args():
    sig = inspect.signature(OCLinEmig::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::bagexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::BagExp)


def test_oclinemig::bagexp_constructor_exists():
    assert callable(OCLinEmig::BagExp.__init__)


def test_oclinemig::bagexp_constructor_args():
    sig = inspect.signature(OCLinEmig::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::NavigationOrAttributeCallExp)


def test_oclinemig::navigationorattributecallexp_constructor_exists():
    assert callable(OCLinEmig::NavigationOrAttributeCallExp.__init__)


def test_oclinemig::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(OCLinEmig::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::navigationorattributecallexp_has_name():
    assert hasattr(OCLinEmig::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in OCLinEmig::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::stringexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::StringExp)


def test_oclinemig::stringexp_constructor_exists():
    assert callable(OCLinEmig::StringExp.__init__)


def test_oclinemig::stringexp_constructor_args():
    sig = inspect.signature(OCLinEmig::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_oclinemig::stringexp_has_stringSymbol():
    assert hasattr(OCLinEmig::StringExp, "stringSymbol")
    descriptor = None
    for klass in OCLinEmig::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclUndefinedExp)


def test_oclinemig::oclundefinedexp_constructor_exists():
    assert callable(OCLinEmig::OclUndefinedExp.__init__)


def test_oclinemig::oclundefinedexp_constructor_args():
    sig = inspect.signature(OCLinEmig::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::EnumLiteralExp)


def test_oclinemig::enumliteralexp_constructor_exists():
    assert callable(OCLinEmig::EnumLiteralExp.__init__)


def test_oclinemig::enumliteralexp_constructor_args():
    sig = inspect.signature(OCLinEmig::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::enumliteralexp_has_name():
    assert hasattr(OCLinEmig::EnumLiteralExp, "name")
    descriptor = None
    for klass in OCLinEmig::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::superexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::SuperExp)


def test_oclinemig::superexp_constructor_exists():
    assert callable(OCLinEmig::SuperExp.__init__)


def test_oclinemig::superexp_constructor_args():
    sig = inspect.signature(OCLinEmig::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::tupleexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::TupleExp)


def test_oclinemig::tupleexp_constructor_exists():
    assert callable(OCLinEmig::TupleExp.__init__)


def test_oclinemig::tupleexp_constructor_args():
    sig = inspect.signature(OCLinEmig::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::PrimitiveExp)


def test_oclinemig::primitiveexp_constructor_exists():
    assert callable(OCLinEmig::PrimitiveExp.__init__)


def test_oclinemig::primitiveexp_constructor_args():
    sig = inspect.signature(OCLinEmig::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::mapexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::MapExp)


def test_oclinemig::mapexp_constructor_exists():
    assert callable(OCLinEmig::MapExp.__init__)


def test_oclinemig::mapexp_constructor_args():
    sig = inspect.signature(OCLinEmig::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::variableexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::VariableExp)


def test_oclinemig::variableexp_constructor_exists():
    assert callable(OCLinEmig::VariableExp.__init__)


def test_oclinemig::variableexp_constructor_args():
    sig = inspect.signature(OCLinEmig::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::attribute_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Attribute)


def test_oclinemig::attribute_constructor_exists():
    assert callable(OCLinEmig::Attribute.__init__)


def test_oclinemig::attribute_constructor_args():
    sig = inspect.signature(OCLinEmig::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::attribute_has_name():
    assert hasattr(OCLinEmig::Attribute, "name")
    descriptor = None
    for klass in OCLinEmig::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::operation_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::Operation)


def test_oclinemig::operation_constructor_exists():
    assert callable(OCLinEmig::Operation.__init__)


def test_oclinemig::operation_constructor_args():
    sig = inspect.signature(OCLinEmig::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::operation_has_name():
    assert hasattr(OCLinEmig::Operation, "name")
    descriptor = None
    for klass in OCLinEmig::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OperationCallExp)


def test_oclinemig::operationcallexp_constructor_exists():
    assert callable(OCLinEmig::OperationCallExp.__init__)


def test_oclinemig::operationcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_oclinemig::operationcallexp_has_operationName():
    assert hasattr(OCLinEmig::OperationCallExp, "operationName")
    descriptor = None
    for klass in OCLinEmig::OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::loopexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::LoopExp)


def test_oclinemig::loopexp_constructor_exists():
    assert callable(OCLinEmig::LoopExp.__init__)


def test_oclinemig::loopexp_constructor_args():
    sig = inspect.signature(OCLinEmig::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::letexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::LetExp)


def test_oclinemig::letexp_constructor_exists():
    assert callable(OCLinEmig::LetExp.__init__)


def test_oclinemig::letexp_constructor_args():
    sig = inspect.signature(OCLinEmig::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::integerexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::IntegerExp)


def test_oclinemig::integerexp_constructor_exists():
    assert callable(OCLinEmig::IntegerExp.__init__)


def test_oclinemig::integerexp_constructor_args():
    sig = inspect.signature(OCLinEmig::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_oclinemig::integerexp_has_integerSymbol():
    assert hasattr(OCLinEmig::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in OCLinEmig::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::realexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::RealExp)


def test_oclinemig::realexp_constructor_exists():
    assert callable(OCLinEmig::RealExp.__init__)


def test_oclinemig::realexp_constructor_args():
    sig = inspect.signature(OCLinEmig::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_oclinemig::realexp_has_realSymbol():
    assert hasattr(OCLinEmig::RealExp, "realSymbol")
    descriptor = None
    for klass in OCLinEmig::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::numericexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::NumericExp)


def test_oclinemig::numericexp_constructor_exists():
    assert callable(OCLinEmig::NumericExp.__init__)


def test_oclinemig::numericexp_constructor_args():
    sig = inspect.signature(OCLinEmig::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::booleanexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::BooleanExp)


def test_oclinemig::booleanexp_constructor_exists():
    assert callable(OCLinEmig::BooleanExp.__init__)


def test_oclinemig::booleanexp_constructor_args():
    sig = inspect.signature(OCLinEmig::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_oclinemig::booleanexp_has_booleanSymbol():
    assert hasattr(OCLinEmig::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in OCLinEmig::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::VariableDeclaration)


def test_oclinemig::variabledeclaration_constructor_exists():
    assert callable(OCLinEmig::VariableDeclaration.__init__)


def test_oclinemig::variabledeclaration_constructor_args():
    sig = inspect.signature(OCLinEmig::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_oclinemig::variabledeclaration_has_id():
    assert hasattr(OCLinEmig::VariableDeclaration, "id")
    descriptor = None
    for klass in OCLinEmig::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig::variabledeclaration_has_varName():
    assert hasattr(OCLinEmig::VariableDeclaration, "varName")
    descriptor = None
    for klass in OCLinEmig::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclFeature)


def test_oclinemig::oclfeature_constructor_exists():
    assert callable(OCLinEmig::OclFeature.__init__)


def test_oclinemig::oclfeature_constructor_args():
    sig = inspect.signature(OCLinEmig::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclmodel_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclModel)


def test_oclinemig::oclmodel_constructor_exists():
    assert callable(OCLinEmig::OclModel.__init__)


def test_oclinemig::oclmodel_constructor_args():
    sig = inspect.signature(OCLinEmig::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::oclmodel_has_name():
    assert hasattr(OCLinEmig::OclModel, "name")
    descriptor = None
    for klass in OCLinEmig::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::mapelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::MapElement)


def test_oclinemig::mapelement_constructor_exists():
    assert callable(OCLinEmig::MapElement.__init__)


def test_oclinemig::mapelement_constructor_args():
    sig = inspect.signature(OCLinEmig::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclFeatureDefinition)


def test_oclinemig::oclfeaturedefinition_constructor_exists():
    assert callable(OCLinEmig::OclFeatureDefinition.__init__)


def test_oclinemig::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OCLinEmig::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::TupleTypeAttribute)


def test_oclinemig::tupletypeattribute_constructor_exists():
    assert callable(OCLinEmig::TupleTypeAttribute.__init__)


def test_oclinemig::tupletypeattribute_constructor_args():
    sig = inspect.signature(OCLinEmig::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::tupletypeattribute_has_name():
    assert hasattr(OCLinEmig::TupleTypeAttribute, "name")
    descriptor = None
    for klass in OCLinEmig::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclContextDefinition)


def test_oclinemig::oclcontextdefinition_constructor_exists():
    assert callable(OCLinEmig::OclContextDefinition.__init__)


def test_oclinemig::oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCLinEmig::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclExpression)


def test_oclinemig::oclexpression_constructor_exists():
    assert callable(OCLinEmig::OclExpression.__init__)


def test_oclinemig::oclexpression_constructor_args():
    sig = inspect.signature(OCLinEmig::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::collectionexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::CollectionExp)


def test_oclinemig::collectionexp_constructor_exists():
    assert callable(OCLinEmig::CollectionExp.__init__)


def test_oclinemig::collectionexp_constructor_args():
    sig = inspect.signature(OCLinEmig::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::PropertyCallExp)


def test_oclinemig::propertycallexp_constructor_exists():
    assert callable(OCLinEmig::PropertyCallExp.__init__)


def test_oclinemig::propertycallexp_constructor_args():
    sig = inspect.signature(OCLinEmig::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::ifexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::IfExp)


def test_oclinemig::ifexp_constructor_exists():
    assert callable(OCLinEmig::IfExp.__init__)


def test_oclinemig::ifexp_constructor_args():
    sig = inspect.signature(OCLinEmig::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig::ocltype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig::OclType)


def test_oclinemig::ocltype_constructor_exists():
    assert callable(OCLinEmig::OclType.__init__)


def test_oclinemig::ocltype_constructor_args():
    sig = inspect.signature(OCLinEmig::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig::ocltype_has_name():
    assert hasattr(OCLinEmig::OclType, "name")
    descriptor = None
    for klass in OCLinEmig::OclType.__mro__:
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
OCLinEmig::Module_strategy = st.builds(
    OCLinEmig::Module,
    name=
        safe_text
)
OCLinEmig::LocatedElement_strategy = st.builds(
    OCLinEmig::LocatedElement,
    location=
        safe_text,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text
)
OclFeature_strategy = st.builds(
    OclFeature,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCLinEmig::OrderedSetType_strategy = st.builds(
    OCLinEmig::OrderedSetType,
)
OCLinEmig::SetType_strategy = st.builds(
    OCLinEmig::SetType,
)
OCLinEmig::SequenceType_strategy = st.builds(
    OCLinEmig::SequenceType,
)
OCLinEmig::BagType_strategy = st.builds(
    OCLinEmig::BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
OCLinEmig::RealType_strategy = st.builds(
    OCLinEmig::RealType,
)
OCLinEmig::IntegerType_strategy = st.builds(
    OCLinEmig::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
OCLinEmig::NumericType_strategy = st.builds(
    OCLinEmig::NumericType,
)
OCLinEmig::BooleanType_strategy = st.builds(
    OCLinEmig::BooleanType,
)
OCLinEmig::StringType_strategy = st.builds(
    OCLinEmig::StringType,
)
OclType_strategy = st.builds(
    OclType,
)
OCLinEmig::Primitive_strategy = st.builds(
    OCLinEmig::Primitive,
)
OCLinEmig::OclAnyType_strategy = st.builds(
    OCLinEmig::OclAnyType,
)
OCLinEmig::TupleType_strategy = st.builds(
    OCLinEmig::TupleType,
)
OCLinEmig::OclModelElement_strategy = st.builds(
    OCLinEmig::OclModelElement,
)
OCLinEmig::CollectionType_strategy = st.builds(
    OCLinEmig::CollectionType,
)
OCLinEmig::MapType_strategy = st.builds(
    OCLinEmig::MapType,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OCLinEmig::IteratorExp_strategy = st.builds(
    OCLinEmig::IteratorExp,
    name=
        safe_text
)
OCLinEmig::IterateExp_strategy = st.builds(
    OCLinEmig::IterateExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
OCLinEmig::CollectionOperationCallExp_strategy = st.builds(
    OCLinEmig::CollectionOperationCallExp,
)
OCLinEmig::OperatorCallExp_strategy = st.builds(
    OCLinEmig::OperatorCallExp,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
OCLinEmig::Iterator_strategy = st.builds(
    OCLinEmig::Iterator,
)
OCLinEmig::Parameter_strategy = st.builds(
    OCLinEmig::Parameter,
)
OCLinEmig::TuplePart_strategy = st.builds(
    OCLinEmig::TuplePart,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
OCLinEmig::OrderedSetExp_strategy = st.builds(
    OCLinEmig::OrderedSetExp,
)
OCLinEmig::SequenceExp_strategy = st.builds(
    OCLinEmig::SequenceExp,
)
OCLinEmig::SetExp_strategy = st.builds(
    OCLinEmig::SetExp,
)
OCLinEmig::BagExp_strategy = st.builds(
    OCLinEmig::BagExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
OCLinEmig::NavigationOrAttributeCallExp_strategy = st.builds(
    OCLinEmig::NavigationOrAttributeCallExp,
    name=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
OCLinEmig::StringExp_strategy = st.builds(
    OCLinEmig::StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCLinEmig::OclUndefinedExp_strategy = st.builds(
    OCLinEmig::OclUndefinedExp,
)
OCLinEmig::EnumLiteralExp_strategy = st.builds(
    OCLinEmig::EnumLiteralExp,
    name=
        safe_text
)
OCLinEmig::SuperExp_strategy = st.builds(
    OCLinEmig::SuperExp,
)
OCLinEmig::TupleExp_strategy = st.builds(
    OCLinEmig::TupleExp,
)
OCLinEmig::PrimitiveExp_strategy = st.builds(
    OCLinEmig::PrimitiveExp,
)
OCLinEmig::MapExp_strategy = st.builds(
    OCLinEmig::MapExp,
)
OCLinEmig::VariableExp_strategy = st.builds(
    OCLinEmig::VariableExp,
)
OCLinEmig::Attribute_strategy = st.builds(
    OCLinEmig::Attribute,
    name=
        safe_text
)
OCLinEmig::Operation_strategy = st.builds(
    OCLinEmig::Operation,
    name=
        safe_text
)
OCLinEmig::OperationCallExp_strategy = st.builds(
    OCLinEmig::OperationCallExp,
    operationName=
        safe_text
)
OCLinEmig::LoopExp_strategy = st.builds(
    OCLinEmig::LoopExp,
)
OCLinEmig::LetExp_strategy = st.builds(
    OCLinEmig::LetExp,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
OCLinEmig::IntegerExp_strategy = st.builds(
    OCLinEmig::IntegerExp,
    integerSymbol=
        safe_text
)
OCLinEmig::RealExp_strategy = st.builds(
    OCLinEmig::RealExp,
    realSymbol=
        safe_text
)
OCLinEmig::NumericExp_strategy = st.builds(
    OCLinEmig::NumericExp,
)
OCLinEmig::BooleanExp_strategy = st.builds(
    OCLinEmig::BooleanExp,
    booleanSymbol=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
OCLinEmig::VariableDeclaration_strategy = st.builds(
    OCLinEmig::VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
OCLinEmig::OclFeature_strategy = st.builds(
    OCLinEmig::OclFeature,
)
OCLinEmig::OclModel_strategy = st.builds(
    OCLinEmig::OclModel,
    name=
        safe_text
)
OCLinEmig::MapElement_strategy = st.builds(
    OCLinEmig::MapElement,
)
OCLinEmig::OclFeatureDefinition_strategy = st.builds(
    OCLinEmig::OclFeatureDefinition,
)
OCLinEmig::TupleTypeAttribute_strategy = st.builds(
    OCLinEmig::TupleTypeAttribute,
    name=
        safe_text
)
OCLinEmig::OclContextDefinition_strategy = st.builds(
    OCLinEmig::OclContextDefinition,
)
OCLinEmig::OclExpression_strategy = st.builds(
    OCLinEmig::OclExpression,
)
OCLinEmig::CollectionExp_strategy = st.builds(
    OCLinEmig::CollectionExp,
)
OCLinEmig::PropertyCallExp_strategy = st.builds(
    OCLinEmig::PropertyCallExp,
)
OCLinEmig::IfExp_strategy = st.builds(
    OCLinEmig::IfExp,
)
OCLinEmig::OclType_strategy = st.builds(
    OCLinEmig::OclType,
    name=
        safe_text
)

@given(instance=OCLinEmig::Module_strategy)
@settings(max_examples=50)
def test_oclinemig::module_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Module)

@given(instance=OCLinEmig::Module_strategy)
def test_oclinemig::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::Module_strategy)
def test_oclinemig::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::LocatedElement_strategy)
@settings(max_examples=50)
def test_oclinemig::locatedelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig::LocatedElement)

@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=OCLinEmig::LocatedElement_strategy)
def test_oclinemig::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=OCLinEmig::OrderedSetType_strategy)
@settings(max_examples=50)
def test_oclinemig::orderedsettype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OrderedSetType)

@given(instance=OCLinEmig::SetType_strategy)
@settings(max_examples=50)
def test_oclinemig::settype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::SetType)

@given(instance=OCLinEmig::SequenceType_strategy)
@settings(max_examples=50)
def test_oclinemig::sequencetype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::SequenceType)

@given(instance=OCLinEmig::BagType_strategy)
@settings(max_examples=50)
def test_oclinemig::bagtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OCLinEmig::RealType_strategy)
@settings(max_examples=50)
def test_oclinemig::realtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::RealType)

@given(instance=OCLinEmig::IntegerType_strategy)
@settings(max_examples=50)
def test_oclinemig::integertype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=OCLinEmig::NumericType_strategy)
@settings(max_examples=50)
def test_oclinemig::numerictype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::NumericType)

@given(instance=OCLinEmig::BooleanType_strategy)
@settings(max_examples=50)
def test_oclinemig::booleantype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::BooleanType)

@given(instance=OCLinEmig::StringType_strategy)
@settings(max_examples=50)
def test_oclinemig::stringtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::StringType)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=OCLinEmig::Primitive_strategy)
@settings(max_examples=50)
def test_oclinemig::primitive_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Primitive)

@given(instance=OCLinEmig::OclAnyType_strategy)
@settings(max_examples=50)
def test_oclinemig::oclanytype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclAnyType)

@given(instance=OCLinEmig::TupleType_strategy)
@settings(max_examples=50)
def test_oclinemig::tupletype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::TupleType)

@given(instance=OCLinEmig::OclModelElement_strategy)
@settings(max_examples=50)
def test_oclinemig::oclmodelelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclModelElement)

@given(instance=OCLinEmig::CollectionType_strategy)
@settings(max_examples=50)
def test_oclinemig::collectiontype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::CollectionType)

@given(instance=OCLinEmig::MapType_strategy)
@settings(max_examples=50)
def test_oclinemig::maptype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::MapType)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OCLinEmig::IteratorExp_strategy)
@settings(max_examples=50)
def test_oclinemig::iteratorexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::IteratorExp)

@given(instance=OCLinEmig::IteratorExp_strategy)
def test_oclinemig::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::IteratorExp_strategy)
def test_oclinemig::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::IterateExp_strategy)
@settings(max_examples=50)
def test_oclinemig::iterateexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::IterateExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=OCLinEmig::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::CollectionOperationCallExp)

@given(instance=OCLinEmig::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig::operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OperatorCallExp)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=OCLinEmig::Iterator_strategy)
@settings(max_examples=50)
def test_oclinemig::iterator_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Iterator)

@given(instance=OCLinEmig::Parameter_strategy)
@settings(max_examples=50)
def test_oclinemig::parameter_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Parameter)

@given(instance=OCLinEmig::TuplePart_strategy)
@settings(max_examples=50)
def test_oclinemig::tuplepart_instantiation(instance):
    assert isinstance(instance, OCLinEmig::TuplePart)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=OCLinEmig::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_oclinemig::orderedsetexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OrderedSetExp)

@given(instance=OCLinEmig::SequenceExp_strategy)
@settings(max_examples=50)
def test_oclinemig::sequenceexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::SequenceExp)

@given(instance=OCLinEmig::SetExp_strategy)
@settings(max_examples=50)
def test_oclinemig::setexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::SetExp)

@given(instance=OCLinEmig::BagExp_strategy)
@settings(max_examples=50)
def test_oclinemig::bagexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::BagExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=OCLinEmig::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::NavigationOrAttributeCallExp)

@given(instance=OCLinEmig::NavigationOrAttributeCallExp_strategy)
def test_oclinemig::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::NavigationOrAttributeCallExp_strategy)
def test_oclinemig::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=OCLinEmig::StringExp_strategy)
@settings(max_examples=50)
def test_oclinemig::stringexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::StringExp)

@given(instance=OCLinEmig::StringExp_strategy)
def test_oclinemig::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=OCLinEmig::StringExp_strategy)
def test_oclinemig::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCLinEmig::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_oclinemig::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclUndefinedExp)

@given(instance=OCLinEmig::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_oclinemig::enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::EnumLiteralExp)

@given(instance=OCLinEmig::EnumLiteralExp_strategy)
def test_oclinemig::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::EnumLiteralExp_strategy)
def test_oclinemig::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::SuperExp_strategy)
@settings(max_examples=50)
def test_oclinemig::superexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::SuperExp)

@given(instance=OCLinEmig::TupleExp_strategy)
@settings(max_examples=50)
def test_oclinemig::tupleexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::TupleExp)

@given(instance=OCLinEmig::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_oclinemig::primitiveexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::PrimitiveExp)

@given(instance=OCLinEmig::MapExp_strategy)
@settings(max_examples=50)
def test_oclinemig::mapexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::MapExp)

@given(instance=OCLinEmig::VariableExp_strategy)
@settings(max_examples=50)
def test_oclinemig::variableexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::VariableExp)

@given(instance=OCLinEmig::Attribute_strategy)
@settings(max_examples=50)
def test_oclinemig::attribute_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Attribute)

@given(instance=OCLinEmig::Attribute_strategy)
def test_oclinemig::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::Attribute_strategy)
def test_oclinemig::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::Operation_strategy)
@settings(max_examples=50)
def test_oclinemig::operation_instantiation(instance):
    assert isinstance(instance, OCLinEmig::Operation)

@given(instance=OCLinEmig::Operation_strategy)
def test_oclinemig::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::Operation_strategy)
def test_oclinemig::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::OperationCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig::operationcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OperationCallExp)

@given(instance=OCLinEmig::OperationCallExp_strategy)
def test_oclinemig::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=OCLinEmig::OperationCallExp_strategy)
def test_oclinemig::operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=OCLinEmig::LoopExp_strategy)
@settings(max_examples=50)
def test_oclinemig::loopexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::LoopExp)

@given(instance=OCLinEmig::LetExp_strategy)
@settings(max_examples=50)
def test_oclinemig::letexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::LetExp)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=OCLinEmig::IntegerExp_strategy)
@settings(max_examples=50)
def test_oclinemig::integerexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::IntegerExp)

@given(instance=OCLinEmig::IntegerExp_strategy)
def test_oclinemig::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=OCLinEmig::IntegerExp_strategy)
def test_oclinemig::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OCLinEmig::RealExp_strategy)
@settings(max_examples=50)
def test_oclinemig::realexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::RealExp)

@given(instance=OCLinEmig::RealExp_strategy)
def test_oclinemig::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=OCLinEmig::RealExp_strategy)
def test_oclinemig::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=OCLinEmig::NumericExp_strategy)
@settings(max_examples=50)
def test_oclinemig::numericexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::NumericExp)

@given(instance=OCLinEmig::BooleanExp_strategy)
@settings(max_examples=50)
def test_oclinemig::booleanexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::BooleanExp)

@given(instance=OCLinEmig::BooleanExp_strategy)
def test_oclinemig::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=OCLinEmig::BooleanExp_strategy)
def test_oclinemig::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=OCLinEmig::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_oclinemig::variabledeclaration_instantiation(instance):
    assert isinstance(instance, OCLinEmig::VariableDeclaration)

@given(instance=OCLinEmig::VariableDeclaration_strategy)
def test_oclinemig::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=OCLinEmig::VariableDeclaration_strategy)
def test_oclinemig::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=OCLinEmig::VariableDeclaration_strategy)
def test_oclinemig::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=OCLinEmig::VariableDeclaration_strategy)
def test_oclinemig::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=OCLinEmig::OclFeature_strategy)
@settings(max_examples=50)
def test_oclinemig::oclfeature_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclFeature)

@given(instance=OCLinEmig::OclModel_strategy)
@settings(max_examples=50)
def test_oclinemig::oclmodel_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclModel)

@given(instance=OCLinEmig::OclModel_strategy)
def test_oclinemig::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::OclModel_strategy)
def test_oclinemig::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::MapElement_strategy)
@settings(max_examples=50)
def test_oclinemig::mapelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig::MapElement)

@given(instance=OCLinEmig::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclinemig::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclFeatureDefinition)

@given(instance=OCLinEmig::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_oclinemig::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, OCLinEmig::TupleTypeAttribute)

@given(instance=OCLinEmig::TupleTypeAttribute_strategy)
def test_oclinemig::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::TupleTypeAttribute_strategy)
def test_oclinemig::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclinemig::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclContextDefinition)

@given(instance=OCLinEmig::OclExpression_strategy)
@settings(max_examples=50)
def test_oclinemig::oclexpression_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclExpression)

@given(instance=OCLinEmig::CollectionExp_strategy)
@settings(max_examples=50)
def test_oclinemig::collectionexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::CollectionExp)

@given(instance=OCLinEmig::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig::propertycallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::PropertyCallExp)

@given(instance=OCLinEmig::IfExp_strategy)
@settings(max_examples=50)
def test_oclinemig::ifexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig::IfExp)

@given(instance=OCLinEmig::OclType_strategy)
@settings(max_examples=50)
def test_oclinemig::ocltype_instantiation(instance):
    assert isinstance(instance, OCLinEmig::OclType)

@given(instance=OCLinEmig::OclType_strategy)
def test_oclinemig::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCLinEmig::OclType_strategy)
def test_oclinemig::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
