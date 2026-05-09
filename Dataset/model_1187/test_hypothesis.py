import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclContextDefinition,
    Iterator,
    NumericLiteralExp,
    OCL::RealLiteralExp,
    OCL::IntegerLiteralExp,
    OperationCallExp,
    OCL::OperatorCallExp,
    OCL::CollectionOperationCallExp,
    FeaturePropertyCall,
    OCL::PropertyCallExp,
    OCL::OperationCallExp,
    LoopExp,
    OCL::IteratorExp,
    OCL::IterateExp,
    PrimitiveLiteralExp,
    OCL::BooleanLiteralExp,
    OCL::StringLiteralExp,
    OCL::NumericLiteralExp,
    CollectionLiteralPart,
    OCL::CollectionItem,
    OCL::CollectionRange,
    TupleLiteralPart,
    CallExp,
    OCL::LoopExp,
    OCL::FeaturePropertyCall,
    LiteralExp,
    OCL::TupleLiteralExp,
    OCL::PrimitiveLiteralExp,
    OCL::NullLiteralExp,
    OCL::CollectionLiteralExp,
    OCL::InvalidLiteralExp,
    OCL::EnumLiteralExp,
    CollectionType,
    OCL::OrderedSetType,
    OCL::SequenceType,
    OCL::BagType,
    OCL::SetType,
    Type,
    OCL::VoidType,
    OCL::Class,
    OCL::InvalidType,
    PrimitiveType,
    OCL::StringType,
    OCL::BooleanType,
    OCL::RealType,
    OCL::IntegerType,
    DataType,
    OCL::TupleType,
    OCL::CollectionType,
    OCL::PrimitiveType,
    Extent,
    OCL::URIExtent,
    NamedElement,
    OCL::EnumerationLiteral,
    OCL::TypedElement,
    EnumerationLiteral,
    OCL::Enumeration,
    Object,
    OCL::Element,
    OCL::Extent,
    OCL::Object,
    OCL::MultiplicityElement,
    OCL::Package,
    OCL::Type,
    OCL::DataType,
    MultiplicityElement,
    TypedElement,
    OCL::OclExpression,
    OCL::Operation,
    OCL::Variable,
    OCL::Parameter,
    OCL::CollectionLiteralPart,
    OCL::TupleLiteralPart,
    OCL::Property,
    OCL::OclModuleElement,
    OCL::OclFeature,
    Property,
    OclExpression,
    OCL::CallExp,
    OCL::VariableExp,
    OCL::LiteralExp,
    OCL::LetExp,
    OCL::IfExp,
    Variable,
    OCL::Iterator,
    OclFeature,
    OCL::OclProperty,
    Operation,
    OCL::OclOperation,
    Package,
    OCL::OclModule,
    Class,
    OCL::AnyType,
    Element,
    OCL::Tag,
    OCL::NamedElement,
    OCL::Comment,
    OCL::OclContextDefinition,
    Parameter,
    OclModuleElement,
    OCL::Invariant,
    OCL::DefOclModuleElement,
    OCL::DeriveOclModuleElement,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::RealLiteralExp)


def test_ocl::realliteralexp_constructor_exists():
    assert callable(OCL::RealLiteralExp.__init__)


def test_ocl::realliteralexp_constructor_args():
    sig = inspect.signature(OCL::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl::realliteralexp_has_realSymbol():
    assert hasattr(OCL::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in OCL::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IntegerLiteralExp)


def test_ocl::integerliteralexp_constructor_exists():
    assert callable(OCL::IntegerLiteralExp.__init__)


def test_ocl::integerliteralexp_constructor_args():
    sig = inspect.signature(OCL::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl::integerliteralexp_has_integerSymbol():
    assert hasattr(OCL::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in OCL::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OperatorCallExp)


def test_ocl::operatorcallexp_constructor_exists():
    assert callable(OCL::OperatorCallExp.__init__)


def test_ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionOperationCallExp)


def test_ocl::collectionoperationcallexp_constructor_exists():
    assert callable(OCL::CollectionOperationCallExp.__init__)


def test_ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::PropertyCallExp)


def test_ocl::propertycallexp_constructor_exists():
    assert callable(OCL::PropertyCallExp.__init__)


def test_ocl::propertycallexp_constructor_args():
    sig = inspect.signature(OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OperationCallExp)


def test_ocl::operationcallexp_constructor_exists():
    assert callable(OCL::OperationCallExp.__init__)


def test_ocl::operationcallexp_constructor_args():
    sig = inspect.signature(OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IteratorExp)


def test_ocl::iteratorexp_constructor_exists():
    assert callable(OCL::IteratorExp.__init__)


def test_ocl::iteratorexp_constructor_args():
    sig = inspect.signature(OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IterateExp)


def test_ocl::iterateexp_constructor_exists():
    assert callable(OCL::IterateExp.__init__)


def test_ocl::iterateexp_constructor_args():
    sig = inspect.signature(OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::BooleanLiteralExp)


def test_ocl::booleanliteralexp_constructor_exists():
    assert callable(OCL::BooleanLiteralExp.__init__)


def test_ocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(OCL::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(OCL::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in OCL::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::StringLiteralExp)


def test_ocl::stringliteralexp_constructor_exists():
    assert callable(OCL::StringLiteralExp.__init__)


def test_ocl::stringliteralexp_constructor_args():
    sig = inspect.signature(OCL::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl::stringliteralexp_has_stringSymbol():
    assert hasattr(OCL::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in OCL::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::NumericLiteralExp)


def test_ocl::numericliteralexp_constructor_exists():
    assert callable(OCL::NumericLiteralExp.__init__)


def test_ocl::numericliteralexp_constructor_args():
    sig = inspect.signature(OCL::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionItem)


def test_ocl::collectionitem_constructor_exists():
    assert callable(OCL::CollectionItem.__init__)


def test_ocl::collectionitem_constructor_args():
    sig = inspect.signature(OCL::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionRange)


def test_ocl::collectionrange_constructor_exists():
    assert callable(OCL::CollectionRange.__init__)


def test_ocl::collectionrange_constructor_args():
    sig = inspect.signature(OCL::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LoopExp)


def test_ocl::loopexp_constructor_exists():
    assert callable(OCL::LoopExp.__init__)


def test_ocl::loopexp_constructor_args():
    sig = inspect.signature(OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(OCL::FeaturePropertyCall)


def test_ocl::featurepropertycall_constructor_exists():
    assert callable(OCL::FeaturePropertyCall.__init__)


def test_ocl::featurepropertycall_constructor_args():
    sig = inspect.signature(OCL::FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleLiteralExp)


def test_ocl::tupleliteralexp_constructor_exists():
    assert callable(OCL::TupleLiteralExp.__init__)


def test_ocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(OCL::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::PrimitiveLiteralExp)


def test_ocl::primitiveliteralexp_constructor_exists():
    assert callable(OCL::PrimitiveLiteralExp.__init__)


def test_ocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(OCL::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::NullLiteralExp)


def test_ocl::nullliteralexp_constructor_exists():
    assert callable(OCL::NullLiteralExp.__init__)


def test_ocl::nullliteralexp_constructor_args():
    sig = inspect.signature(OCL::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionLiteralExp)


def test_ocl::collectionliteralexp_constructor_exists():
    assert callable(OCL::CollectionLiteralExp.__init__)


def test_ocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(OCL::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::collectionliteralexp_has_kind():
    assert hasattr(OCL::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in OCL::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::InvalidLiteralExp)


def test_ocl::invalidliteralexp_constructor_exists():
    assert callable(OCL::InvalidLiteralExp.__init__)


def test_ocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(OCL::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::EnumLiteralExp)


def test_ocl::enumliteralexp_constructor_exists():
    assert callable(OCL::EnumLiteralExp.__init__)


def test_ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCL::OrderedSetType)


def test_ocl::orderedsettype_constructor_exists():
    assert callable(OCL::OrderedSetType.__init__)


def test_ocl::orderedsettype_constructor_args():
    sig = inspect.signature(OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCL::SequenceType)


def test_ocl::sequencetype_constructor_exists():
    assert callable(OCL::SequenceType.__init__)


def test_ocl::sequencetype_constructor_args():
    sig = inspect.signature(OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(OCL::BagType)


def test_ocl::bagtype_constructor_exists():
    assert callable(OCL::BagType.__init__)


def test_ocl::bagtype_constructor_args():
    sig = inspect.signature(OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::settype_is_not_abstract():
    assert not inspect.isabstract(OCL::SetType)


def test_ocl::settype_constructor_exists():
    assert callable(OCL::SetType.__init__)


def test_ocl::settype_constructor_args():
    sig = inspect.signature(OCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(OCL::VoidType)


def test_ocl::voidtype_constructor_exists():
    assert callable(OCL::VoidType.__init__)


def test_ocl::voidtype_constructor_args():
    sig = inspect.signature(OCL::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::class_is_not_abstract():
    assert not inspect.isabstract(OCL::Class)


def test_ocl::class_constructor_exists():
    assert callable(OCL::Class.__init__)


def test_ocl::class_constructor_args():
    sig = inspect.signature(OCL::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_ocl::class_has_isAbstract():
    assert hasattr(OCL::Class, "isAbstract")
    descriptor = None
    for klass in OCL::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_ocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(OCL::InvalidType)


def test_ocl::invalidtype_constructor_exists():
    assert callable(OCL::InvalidType.__init__)


def test_ocl::invalidtype_constructor_args():
    sig = inspect.signature(OCL::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(OCL::StringType)


def test_ocl::stringtype_constructor_exists():
    assert callable(OCL::StringType.__init__)


def test_ocl::stringtype_constructor_args():
    sig = inspect.signature(OCL::StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL::BooleanType)


def test_ocl::booleantype_constructor_exists():
    assert callable(OCL::BooleanType.__init__)


def test_ocl::booleantype_constructor_args():
    sig = inspect.signature(OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(OCL::RealType)


def test_ocl::realtype_constructor_exists():
    assert callable(OCL::RealType.__init__)


def test_ocl::realtype_constructor_args():
    sig = inspect.signature(OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(OCL::IntegerType)


def test_ocl::integertype_constructor_exists():
    assert callable(OCL::IntegerType.__init__)


def test_ocl::integertype_constructor_args():
    sig = inspect.signature(OCL::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleType)


def test_ocl::tupletype_constructor_exists():
    assert callable(OCL::TupleType.__init__)


def test_ocl::tupletype_constructor_args():
    sig = inspect.signature(OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionType)


def test_ocl::collectiontype_constructor_exists():
    assert callable(OCL::CollectionType.__init__)


def test_ocl::collectiontype_constructor_args():
    sig = inspect.signature(OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitivetype_is_not_abstract():
    assert not inspect.isabstract(OCL::PrimitiveType)


def test_ocl::primitivetype_constructor_exists():
    assert callable(OCL::PrimitiveType.__init__)


def test_ocl::primitivetype_constructor_args():
    sig = inspect.signature(OCL::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uriextent_is_not_abstract():
    assert not inspect.isabstract(OCL::URIExtent)


def test_ocl::uriextent_constructor_exists():
    assert callable(OCL::URIExtent.__init__)


def test_ocl::uriextent_constructor_args():
    sig = inspect.signature(OCL::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(OCL::EnumerationLiteral)


def test_ocl::enumerationliteral_constructor_exists():
    assert callable(OCL::EnumerationLiteral.__init__)


def test_ocl::enumerationliteral_constructor_args():
    sig = inspect.signature(OCL::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl::typedelement_is_not_abstract():
    assert not inspect.isabstract(OCL::TypedElement)


def test_ocl::typedelement_constructor_exists():
    assert callable(OCL::TypedElement.__init__)


def test_ocl::typedelement_constructor_args():
    sig = inspect.signature(OCL::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl::enumeration_is_not_abstract():
    assert not inspect.isabstract(OCL::Enumeration)


def test_ocl::enumeration_constructor_exists():
    assert callable(OCL::Enumeration.__init__)


def test_ocl::enumeration_constructor_args():
    sig = inspect.signature(OCL::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_ocl::element_is_not_abstract():
    assert not inspect.isabstract(OCL::Element)


def test_ocl::element_constructor_exists():
    assert callable(OCL::Element.__init__)


def test_ocl::element_constructor_args():
    sig = inspect.signature(OCL::Element.__init__)
    params = list(sig.parameters.keys())



def test_ocl::extent_is_not_abstract():
    assert not inspect.isabstract(OCL::Extent)


def test_ocl::extent_constructor_exists():
    assert callable(OCL::Extent.__init__)


def test_ocl::extent_constructor_args():
    sig = inspect.signature(OCL::Extent.__init__)
    params = list(sig.parameters.keys())



def test_ocl::object_is_not_abstract():
    assert not inspect.isabstract(OCL::Object)


def test_ocl::object_constructor_exists():
    assert callable(OCL::Object.__init__)


def test_ocl::object_constructor_args():
    sig = inspect.signature(OCL::Object.__init__)
    params = list(sig.parameters.keys())



def test_ocl::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(OCL::MultiplicityElement)


def test_ocl::multiplicityelement_constructor_exists():
    assert callable(OCL::MultiplicityElement.__init__)


def test_ocl::multiplicityelement_constructor_args():
    sig = inspect.signature(OCL::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_ocl::multiplicityelement_has_upper():
    assert hasattr(OCL::MultiplicityElement, "upper")
    descriptor = None
    for klass in OCL::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_ocl::multiplicityelement_has_isUnique():
    assert hasattr(OCL::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in OCL::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_ocl::multiplicityelement_has_lower():
    assert hasattr(OCL::MultiplicityElement, "lower")
    descriptor = None
    for klass in OCL::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_ocl::multiplicityelement_has_isOrdered():
    assert hasattr(OCL::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in OCL::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_ocl::package_is_not_abstract():
    assert not inspect.isabstract(OCL::Package)


def test_ocl::package_constructor_exists():
    assert callable(OCL::Package.__init__)


def test_ocl::package_constructor_args():
    sig = inspect.signature(OCL::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_ocl::package_has_uri():
    assert hasattr(OCL::Package, "uri")
    descriptor = None
    for klass in OCL::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_ocl::type_is_not_abstract():
    assert not inspect.isabstract(OCL::Type)


def test_ocl::type_constructor_exists():
    assert callable(OCL::Type.__init__)


def test_ocl::type_constructor_args():
    sig = inspect.signature(OCL::Type.__init__)
    params = list(sig.parameters.keys())



def test_ocl::datatype_is_not_abstract():
    assert not inspect.isabstract(OCL::DataType)


def test_ocl::datatype_constructor_exists():
    assert callable(OCL::DataType.__init__)


def test_ocl::datatype_constructor_args():
    sig = inspect.signature(OCL::DataType.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL::OclExpression)


def test_ocl::oclexpression_constructor_exists():
    assert callable(OCL::OclExpression.__init__)


def test_ocl::oclexpression_constructor_args():
    sig = inspect.signature(OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::operation_is_not_abstract():
    assert not inspect.isabstract(OCL::Operation)


def test_ocl::operation_constructor_exists():
    assert callable(OCL::Operation.__init__)


def test_ocl::operation_constructor_args():
    sig = inspect.signature(OCL::Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variable_is_not_abstract():
    assert not inspect.isabstract(OCL::Variable)


def test_ocl::variable_constructor_exists():
    assert callable(OCL::Variable.__init__)


def test_ocl::variable_constructor_args():
    sig = inspect.signature(OCL::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(OCL::Parameter)


def test_ocl::parameter_constructor_exists():
    assert callable(OCL::Parameter.__init__)


def test_ocl::parameter_constructor_args():
    sig = inspect.signature(OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionLiteralPart)


def test_ocl::collectionliteralpart_constructor_exists():
    assert callable(OCL::CollectionLiteralPart.__init__)


def test_ocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(OCL::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleLiteralPart)


def test_ocl::tupleliteralpart_constructor_exists():
    assert callable(OCL::TupleLiteralPart.__init__)


def test_ocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(OCL::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::property_is_not_abstract():
    assert not inspect.isabstract(OCL::Property)


def test_ocl::property_constructor_exists():
    assert callable(OCL::Property.__init__)


def test_ocl::property_constructor_args():
    sig = inspect.signature(OCL::Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isId" in params, "Missing parameter 'isId'"

def test_ocl::property_has_default():
    assert hasattr(OCL::Property, "default")
    descriptor = None
    for klass in OCL::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_ocl::property_has_isDerived():
    assert hasattr(OCL::Property, "isDerived")
    descriptor = None
    for klass in OCL::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_ocl::property_has_isComposite():
    assert hasattr(OCL::Property, "isComposite")
    descriptor = None
    for klass in OCL::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_ocl::property_has_isReadOnly():
    assert hasattr(OCL::Property, "isReadOnly")
    descriptor = None
    for klass in OCL::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_ocl::property_has_isId():
    assert hasattr(OCL::Property, "isId")
    descriptor = None
    for klass in OCL::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)



def test_ocl::oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL::OclModuleElement)


def test_ocl::oclmoduleelement_constructor_exists():
    assert callable(OCL::OclModuleElement.__init__)


def test_ocl::oclmoduleelement_constructor_args():
    sig = inspect.signature(OCL::OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL::OclFeature)


def test_ocl::oclfeature_constructor_exists():
    assert callable(OCL::OclFeature.__init__)


def test_ocl::oclfeature_constructor_args():
    sig = inspect.signature(OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::callexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CallExp)


def test_ocl::callexp_constructor_exists():
    assert callable(OCL::CallExp.__init__)


def test_ocl::callexp_constructor_args():
    sig = inspect.signature(OCL::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(OCL::VariableExp)


def test_ocl::variableexp_constructor_exists():
    assert callable(OCL::VariableExp.__init__)


def test_ocl::variableexp_constructor_args():
    sig = inspect.signature(OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LiteralExp)


def test_ocl::literalexp_constructor_exists():
    assert callable(OCL::LiteralExp.__init__)


def test_ocl::literalexp_constructor_args():
    sig = inspect.signature(OCL::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LetExp)


def test_ocl::letexp_constructor_exists():
    assert callable(OCL::LetExp.__init__)


def test_ocl::letexp_constructor_args():
    sig = inspect.signature(OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IfExp)


def test_ocl::ifexp_constructor_exists():
    assert callable(OCL::IfExp.__init__)


def test_ocl::ifexp_constructor_args():
    sig = inspect.signature(OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(OCL::Iterator)


def test_ocl::iterator_constructor_exists():
    assert callable(OCL::Iterator.__init__)


def test_ocl::iterator_constructor_args():
    sig = inspect.signature(OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclproperty_is_not_abstract():
    assert not inspect.isabstract(OCL::OclProperty)


def test_ocl::oclproperty_constructor_exists():
    assert callable(OCL::OclProperty.__init__)


def test_ocl::oclproperty_constructor_args():
    sig = inspect.signature(OCL::OclProperty.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ocloperation_is_not_abstract():
    assert not inspect.isabstract(OCL::OclOperation)


def test_ocl::ocloperation_constructor_exists():
    assert callable(OCL::OclOperation.__init__)


def test_ocl::ocloperation_constructor_args():
    sig = inspect.signature(OCL::OclOperation.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclmodule_is_not_abstract():
    assert not inspect.isabstract(OCL::OclModule)


def test_ocl::oclmodule_constructor_exists():
    assert callable(OCL::OclModule.__init__)


def test_ocl::oclmodule_constructor_args():
    sig = inspect.signature(OCL::OclModule.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_ocl::anytype_is_not_abstract():
    assert not inspect.isabstract(OCL::AnyType)


def test_ocl::anytype_constructor_exists():
    assert callable(OCL::AnyType.__init__)


def test_ocl::anytype_constructor_args():
    sig = inspect.signature(OCL::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tag_is_not_abstract():
    assert not inspect.isabstract(OCL::Tag)


def test_ocl::tag_constructor_exists():
    assert callable(OCL::Tag.__init__)


def test_ocl::tag_constructor_args():
    sig = inspect.signature(OCL::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::tag_has_value():
    assert hasattr(OCL::Tag, "value")
    descriptor = None
    for klass in OCL::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ocl::tag_has_name():
    assert hasattr(OCL::Tag, "name")
    descriptor = None
    for klass in OCL::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::namedelement_is_not_abstract():
    assert not inspect.isabstract(OCL::NamedElement)


def test_ocl::namedelement_constructor_exists():
    assert callable(OCL::NamedElement.__init__)


def test_ocl::namedelement_constructor_args():
    sig = inspect.signature(OCL::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::namedelement_has_name():
    assert hasattr(OCL::NamedElement, "name")
    descriptor = None
    for klass in OCL::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::comment_is_not_abstract():
    assert not inspect.isabstract(OCL::Comment)


def test_ocl::comment_constructor_exists():
    assert callable(OCL::Comment.__init__)


def test_ocl::comment_constructor_args():
    sig = inspect.signature(OCL::Comment.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL::OclContextDefinition)


def test_ocl::oclcontextdefinition_constructor_exists():
    assert callable(OCL::OclContextDefinition.__init__)


def test_ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OclModuleElement)


def test_oclmoduleelement_constructor_exists():
    assert callable(OclModuleElement.__init__)


def test_oclmoduleelement_constructor_args():
    sig = inspect.signature(OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::invariant_is_not_abstract():
    assert not inspect.isabstract(OCL::Invariant)


def test_ocl::invariant_constructor_exists():
    assert callable(OCL::Invariant.__init__)


def test_ocl::invariant_constructor_args():
    sig = inspect.signature(OCL::Invariant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::invariant_has_name():
    assert hasattr(OCL::Invariant, "name")
    descriptor = None
    for klass in OCL::Invariant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::defoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL::DefOclModuleElement)


def test_ocl::defoclmoduleelement_constructor_exists():
    assert callable(OCL::DefOclModuleElement.__init__)


def test_ocl::defoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL::DefOclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::deriveoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL::DeriveOclModuleElement)


def test_ocl::deriveoclmoduleelement_constructor_exists():
    assert callable(OCL::DeriveOclModuleElement.__init__)


def test_ocl::deriveoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL::DeriveOclModuleElement.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Set",
        "Bag",
        "Sequence",
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
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
Iterator_strategy = st.builds(
    Iterator,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
OCL::RealLiteralExp_strategy = st.builds(
    OCL::RealLiteralExp,
    realSymbol=
        safe_text
)
OCL::IntegerLiteralExp_strategy = st.builds(
    OCL::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
OCL::OperatorCallExp_strategy = st.builds(
    OCL::OperatorCallExp,
)
OCL::CollectionOperationCallExp_strategy = st.builds(
    OCL::CollectionOperationCallExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
OCL::PropertyCallExp_strategy = st.builds(
    OCL::PropertyCallExp,
)
OCL::OperationCallExp_strategy = st.builds(
    OCL::OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OCL::IteratorExp_strategy = st.builds(
    OCL::IteratorExp,
)
OCL::IterateExp_strategy = st.builds(
    OCL::IterateExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
OCL::BooleanLiteralExp_strategy = st.builds(
    OCL::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
OCL::StringLiteralExp_strategy = st.builds(
    OCL::StringLiteralExp,
    stringSymbol=
        safe_text
)
OCL::NumericLiteralExp_strategy = st.builds(
    OCL::NumericLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
OCL::CollectionItem_strategy = st.builds(
    OCL::CollectionItem,
)
OCL::CollectionRange_strategy = st.builds(
    OCL::CollectionRange,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
OCL::LoopExp_strategy = st.builds(
    OCL::LoopExp,
)
OCL::FeaturePropertyCall_strategy = st.builds(
    OCL::FeaturePropertyCall,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
OCL::TupleLiteralExp_strategy = st.builds(
    OCL::TupleLiteralExp,
)
OCL::PrimitiveLiteralExp_strategy = st.builds(
    OCL::PrimitiveLiteralExp,
)
OCL::NullLiteralExp_strategy = st.builds(
    OCL::NullLiteralExp,
)
OCL::CollectionLiteralExp_strategy = st.builds(
    OCL::CollectionLiteralExp,
    kind=
        safe_text
)
OCL::InvalidLiteralExp_strategy = st.builds(
    OCL::InvalidLiteralExp,
)
OCL::EnumLiteralExp_strategy = st.builds(
    OCL::EnumLiteralExp,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCL::OrderedSetType_strategy = st.builds(
    OCL::OrderedSetType,
)
OCL::SequenceType_strategy = st.builds(
    OCL::SequenceType,
)
OCL::BagType_strategy = st.builds(
    OCL::BagType,
)
OCL::SetType_strategy = st.builds(
    OCL::SetType,
)
Type_strategy = st.builds(
    Type,
)
OCL::VoidType_strategy = st.builds(
    OCL::VoidType,
)
OCL::Class_strategy = st.builds(
    OCL::Class,
    isAbstract=
        safe_text
)
OCL::InvalidType_strategy = st.builds(
    OCL::InvalidType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OCL::StringType_strategy = st.builds(
    OCL::StringType,
)
OCL::BooleanType_strategy = st.builds(
    OCL::BooleanType,
)
OCL::RealType_strategy = st.builds(
    OCL::RealType,
)
OCL::IntegerType_strategy = st.builds(
    OCL::IntegerType,
)
DataType_strategy = st.builds(
    DataType,
)
OCL::TupleType_strategy = st.builds(
    OCL::TupleType,
)
OCL::CollectionType_strategy = st.builds(
    OCL::CollectionType,
)
OCL::PrimitiveType_strategy = st.builds(
    OCL::PrimitiveType,
)
Extent_strategy = st.builds(
    Extent,
)
OCL::URIExtent_strategy = st.builds(
    OCL::URIExtent,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OCL::EnumerationLiteral_strategy = st.builds(
    OCL::EnumerationLiteral,
)
OCL::TypedElement_strategy = st.builds(
    OCL::TypedElement,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
OCL::Enumeration_strategy = st.builds(
    OCL::Enumeration,
)
Object_strategy = st.builds(
    Object,
)
OCL::Element_strategy = st.builds(
    OCL::Element,
)
OCL::Extent_strategy = st.builds(
    OCL::Extent,
)
OCL::Object_strategy = st.builds(
    OCL::Object,
)
OCL::MultiplicityElement_strategy = st.builds(
    OCL::MultiplicityElement,
    upper=
        safe_text,
    isUnique=
        safe_text,
    lower=
        safe_text,
    isOrdered=
        safe_text
)
OCL::Package_strategy = st.builds(
    OCL::Package,
    uri=
        safe_text
)
OCL::Type_strategy = st.builds(
    OCL::Type,
)
OCL::DataType_strategy = st.builds(
    OCL::DataType,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
OCL::OclExpression_strategy = st.builds(
    OCL::OclExpression,
)
OCL::Operation_strategy = st.builds(
    OCL::Operation,
)
OCL::Variable_strategy = st.builds(
    OCL::Variable,
)
OCL::Parameter_strategy = st.builds(
    OCL::Parameter,
)
OCL::CollectionLiteralPart_strategy = st.builds(
    OCL::CollectionLiteralPart,
)
OCL::TupleLiteralPart_strategy = st.builds(
    OCL::TupleLiteralPart,
)
OCL::Property_strategy = st.builds(
    OCL::Property,
    default=
        safe_text,
    isDerived=
        safe_text,
    isComposite=
        safe_text,
    isReadOnly=
        safe_text,
    isId=
        safe_text
)
OCL::OclModuleElement_strategy = st.builds(
    OCL::OclModuleElement,
)
OCL::OclFeature_strategy = st.builds(
    OCL::OclFeature,
)
Property_strategy = st.builds(
    Property,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL::CallExp_strategy = st.builds(
    OCL::CallExp,
)
OCL::VariableExp_strategy = st.builds(
    OCL::VariableExp,
)
OCL::LiteralExp_strategy = st.builds(
    OCL::LiteralExp,
)
OCL::LetExp_strategy = st.builds(
    OCL::LetExp,
)
OCL::IfExp_strategy = st.builds(
    OCL::IfExp,
)
Variable_strategy = st.builds(
    Variable,
)
OCL::Iterator_strategy = st.builds(
    OCL::Iterator,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL::OclProperty_strategy = st.builds(
    OCL::OclProperty,
)
Operation_strategy = st.builds(
    Operation,
)
OCL::OclOperation_strategy = st.builds(
    OCL::OclOperation,
)
Package_strategy = st.builds(
    Package,
)
OCL::OclModule_strategy = st.builds(
    OCL::OclModule,
)
Class_strategy = st.builds(
    Class,
)
OCL::AnyType_strategy = st.builds(
    OCL::AnyType,
)
Element_strategy = st.builds(
    Element,
)
OCL::Tag_strategy = st.builds(
    OCL::Tag,
    value=
        safe_text,
    name=
        safe_text
)
OCL::NamedElement_strategy = st.builds(
    OCL::NamedElement,
    name=
        safe_text
)
OCL::Comment_strategy = st.builds(
    OCL::Comment,
)
OCL::OclContextDefinition_strategy = st.builds(
    OCL::OclContextDefinition,
)
Parameter_strategy = st.builds(
    Parameter,
)
OclModuleElement_strategy = st.builds(
    OclModuleElement,
)
OCL::Invariant_strategy = st.builds(
    OCL::Invariant,
    name=
        safe_text
)
OCL::DefOclModuleElement_strategy = st.builds(
    OCL::DefOclModuleElement,
)
OCL::DeriveOclModuleElement_strategy = st.builds(
    OCL::DeriveOclModuleElement,
)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=OCL::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::RealLiteralExp)

@given(instance=OCL::RealLiteralExp_strategy)
def test_ocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=OCL::RealLiteralExp_strategy)
def test_ocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=OCL::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::IntegerLiteralExp)

@given(instance=OCL::IntegerLiteralExp_strategy)
def test_ocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=OCL::IntegerLiteralExp_strategy)
def test_ocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCL::OperatorCallExp)

@given(instance=OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCL::CollectionOperationCallExp)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, OCL::PropertyCallExp)

@given(instance=OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, OCL::OperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, OCL::IteratorExp)

@given(instance=OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, OCL::IterateExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=OCL::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::BooleanLiteralExp)

@given(instance=OCL::BooleanLiteralExp_strategy)
def test_ocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=OCL::BooleanLiteralExp_strategy)
def test_ocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OCL::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::StringLiteralExp)

@given(instance=OCL::StringLiteralExp_strategy)
def test_ocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=OCL::StringLiteralExp_strategy)
def test_ocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OCL::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::NumericLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=OCL::CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl::collectionitem_instantiation(instance):
    assert isinstance(instance, OCL::CollectionItem)

@given(instance=OCL::CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl::collectionrange_instantiation(instance):
    assert isinstance(instance, OCL::CollectionRange)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::loopexp_instantiation(instance):
    assert isinstance(instance, OCL::LoopExp)

@given(instance=OCL::FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_ocl::featurepropertycall_instantiation(instance):
    assert isinstance(instance, OCL::FeaturePropertyCall)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=OCL::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::TupleLiteralExp)

@given(instance=OCL::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::PrimitiveLiteralExp)

@given(instance=OCL::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::NullLiteralExp)

@given(instance=OCL::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::CollectionLiteralExp)

@given(instance=OCL::CollectionLiteralExp_strategy)
def test_ocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=OCL::CollectionLiteralExp_strategy)
def test_ocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=OCL::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::InvalidLiteralExp)

@given(instance=OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::EnumLiteralExp)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, OCL::OrderedSetType)

@given(instance=OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, OCL::SequenceType)

@given(instance=OCL::BagType_strategy)
@settings(max_examples=50)
def test_ocl::bagtype_instantiation(instance):
    assert isinstance(instance, OCL::BagType)

@given(instance=OCL::SetType_strategy)
@settings(max_examples=50)
def test_ocl::settype_instantiation(instance):
    assert isinstance(instance, OCL::SetType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=OCL::VoidType_strategy)
@settings(max_examples=50)
def test_ocl::voidtype_instantiation(instance):
    assert isinstance(instance, OCL::VoidType)

@given(instance=OCL::Class_strategy)
@settings(max_examples=50)
def test_ocl::class_instantiation(instance):
    assert isinstance(instance, OCL::Class)

@given(instance=OCL::Class_strategy)
def test_ocl::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=OCL::Class_strategy)
def test_ocl::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=OCL::InvalidType_strategy)
@settings(max_examples=50)
def test_ocl::invalidtype_instantiation(instance):
    assert isinstance(instance, OCL::InvalidType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=OCL::StringType_strategy)
@settings(max_examples=50)
def test_ocl::stringtype_instantiation(instance):
    assert isinstance(instance, OCL::StringType)

@given(instance=OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_ocl::booleantype_instantiation(instance):
    assert isinstance(instance, OCL::BooleanType)

@given(instance=OCL::RealType_strategy)
@settings(max_examples=50)
def test_ocl::realtype_instantiation(instance):
    assert isinstance(instance, OCL::RealType)

@given(instance=OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_ocl::integertype_instantiation(instance):
    assert isinstance(instance, OCL::IntegerType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=OCL::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::tupletype_instantiation(instance):
    assert isinstance(instance, OCL::TupleType)

@given(instance=OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, OCL::CollectionType)

@given(instance=OCL::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::primitivetype_instantiation(instance):
    assert isinstance(instance, OCL::PrimitiveType)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=OCL::URIExtent_strategy)
@settings(max_examples=50)
def test_ocl::uriextent_instantiation(instance):
    assert isinstance(instance, OCL::URIExtent)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=OCL::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_ocl::enumerationliteral_instantiation(instance):
    assert isinstance(instance, OCL::EnumerationLiteral)

@given(instance=OCL::TypedElement_strategy)
@settings(max_examples=50)
def test_ocl::typedelement_instantiation(instance):
    assert isinstance(instance, OCL::TypedElement)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=OCL::Enumeration_strategy)
@settings(max_examples=50)
def test_ocl::enumeration_instantiation(instance):
    assert isinstance(instance, OCL::Enumeration)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=OCL::Element_strategy)
@settings(max_examples=50)
def test_ocl::element_instantiation(instance):
    assert isinstance(instance, OCL::Element)

@given(instance=OCL::Extent_strategy)
@settings(max_examples=50)
def test_ocl::extent_instantiation(instance):
    assert isinstance(instance, OCL::Extent)

@given(instance=OCL::Object_strategy)
@settings(max_examples=50)
def test_ocl::object_instantiation(instance):
    assert isinstance(instance, OCL::Object)

@given(instance=OCL::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_ocl::multiplicityelement_instantiation(instance):
    assert isinstance(instance, OCL::MultiplicityElement)

@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=OCL::MultiplicityElement_strategy)
def test_ocl::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=OCL::Package_strategy)
@settings(max_examples=50)
def test_ocl::package_instantiation(instance):
    assert isinstance(instance, OCL::Package)

@given(instance=OCL::Package_strategy)
def test_ocl::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=OCL::Package_strategy)
def test_ocl::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=OCL::Type_strategy)
@settings(max_examples=50)
def test_ocl::type_instantiation(instance):
    assert isinstance(instance, OCL::Type)

@given(instance=OCL::DataType_strategy)
@settings(max_examples=50)
def test_ocl::datatype_instantiation(instance):
    assert isinstance(instance, OCL::DataType)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, OCL::OclExpression)

@given(instance=OCL::Operation_strategy)
@settings(max_examples=50)
def test_ocl::operation_instantiation(instance):
    assert isinstance(instance, OCL::Operation)

@given(instance=OCL::Variable_strategy)
@settings(max_examples=50)
def test_ocl::variable_instantiation(instance):
    assert isinstance(instance, OCL::Variable)

@given(instance=OCL::Parameter_strategy)
@settings(max_examples=50)
def test_ocl::parameter_instantiation(instance):
    assert isinstance(instance, OCL::Parameter)

@given(instance=OCL::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, OCL::CollectionLiteralPart)

@given(instance=OCL::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, OCL::TupleLiteralPart)

@given(instance=OCL::Property_strategy)
@settings(max_examples=50)
def test_ocl::property_instantiation(instance):
    assert isinstance(instance, OCL::Property)

@given(instance=OCL::Property_strategy)
def test_ocl::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=OCL::Property_strategy)
def test_ocl::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=OCL::Property_strategy)
def test_ocl::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=OCL::Property_strategy)
def test_ocl::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=OCL::Property_strategy)
def test_ocl::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=OCL::Property_strategy)
def test_ocl::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=OCL::Property_strategy)
def test_ocl::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=OCL::Property_strategy)
def test_ocl::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=OCL::Property_strategy)
def test_ocl::property_isId_type(instance):
    assert isinstance(instance.isId, str)


@given(instance=OCL::Property_strategy)
def test_ocl::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=OCL::OclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl::oclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL::OclModuleElement)

@given(instance=OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, OCL::OclFeature)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCL::CallExp_strategy)
@settings(max_examples=50)
def test_ocl::callexp_instantiation(instance):
    assert isinstance(instance, OCL::CallExp)

@given(instance=OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::variableexp_instantiation(instance):
    assert isinstance(instance, OCL::VariableExp)

@given(instance=OCL::LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::literalexp_instantiation(instance):
    assert isinstance(instance, OCL::LiteralExp)

@given(instance=OCL::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::letexp_instantiation(instance):
    assert isinstance(instance, OCL::LetExp)

@given(instance=OCL::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::ifexp_instantiation(instance):
    assert isinstance(instance, OCL::IfExp)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=OCL::Iterator_strategy)
@settings(max_examples=50)
def test_ocl::iterator_instantiation(instance):
    assert isinstance(instance, OCL::Iterator)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OCL::OclProperty_strategy)
@settings(max_examples=50)
def test_ocl::oclproperty_instantiation(instance):
    assert isinstance(instance, OCL::OclProperty)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=OCL::OclOperation_strategy)
@settings(max_examples=50)
def test_ocl::ocloperation_instantiation(instance):
    assert isinstance(instance, OCL::OclOperation)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=OCL::OclModule_strategy)
@settings(max_examples=50)
def test_ocl::oclmodule_instantiation(instance):
    assert isinstance(instance, OCL::OclModule)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OCL::AnyType_strategy)
@settings(max_examples=50)
def test_ocl::anytype_instantiation(instance):
    assert isinstance(instance, OCL::AnyType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=OCL::Tag_strategy)
@settings(max_examples=50)
def test_ocl::tag_instantiation(instance):
    assert isinstance(instance, OCL::Tag)

@given(instance=OCL::Tag_strategy)
def test_ocl::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=OCL::Tag_strategy)
def test_ocl::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OCL::Tag_strategy)
def test_ocl::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::Tag_strategy)
def test_ocl::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::NamedElement_strategy)
@settings(max_examples=50)
def test_ocl::namedelement_instantiation(instance):
    assert isinstance(instance, OCL::NamedElement)

@given(instance=OCL::NamedElement_strategy)
def test_ocl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::NamedElement_strategy)
def test_ocl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::Comment_strategy)
@settings(max_examples=50)
def test_ocl::comment_instantiation(instance):
    assert isinstance(instance, OCL::Comment)

@given(instance=OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCL::OclContextDefinition)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=OclModuleElement_strategy)
@settings(max_examples=50)
def test_oclmoduleelement_instantiation(instance):
    assert isinstance(instance, OclModuleElement)

@given(instance=OCL::Invariant_strategy)
@settings(max_examples=50)
def test_ocl::invariant_instantiation(instance):
    assert isinstance(instance, OCL::Invariant)

@given(instance=OCL::Invariant_strategy)
def test_ocl::invariant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::Invariant_strategy)
def test_ocl::invariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::DefOclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl::defoclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL::DefOclModuleElement)

@given(instance=OCL::DeriveOclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl::deriveoclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL::DeriveOclModuleElement)
