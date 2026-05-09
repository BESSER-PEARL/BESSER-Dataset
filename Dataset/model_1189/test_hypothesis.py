import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ir::ocl::OclAnyLibElement,
    CollectionLiteralExp,
    ir::ocl::SequenceLiteralExp,
    ir::ocl::OrderedSetLiteralExp,
    ir::ocl::BagLiteralExp,
    ir::ocl::SetLiteralExp,
    ocl::ir::EFEnumLiteral,
    ocl::ir::MetaTypeRef,
    ir::ocl::TuplePart,
    TuplePart,
    ocl::ir::EFTupleType,
    LiteralExp,
    ir::ocl::IntegerLiteralExp,
    ir::ocl::EnumLiteralExp,
    ir::ocl::StringLiteralExp,
    ir::ocl::OclInvalid,
    ir::ocl::RealLiteralExp,
    ir::ocl::OclUndefined,
    ir::ocl::CollectionLiteralExp,
    ir::ocl::TupleLiteralExp,
    ir::ocl::BooleanLiteralExp,
    LoopExp,
    ir::ocl::IterateExp,
    ir::ocl::IteratorExp,
    Iterator,
    ocl::ir::PropertyFeatureRef,
    ocl::ir::OperationFeatureRef,
    AbstractOperationCallExp,
    ir::ocl::CollectionCallExp,
    ir::ocl::OperationCallExp,
    CallExp,
    ir::ocl::OperatorCallExp,
    ir::ocl::LoopExp,
    ir::ocl::PropertyCallExp,
    ir::ocl::AbstractOperationCallExp,
    ocl::ir::TypeRef,
    ir::ocl::OclExpression,
    Operation,
    DerivedProperty,
    OclExpression,
    ir::ocl::UnsupportedExp,
    ir::ocl::CallExp,
    ir::ocl::LiteralExp,
    ir::ocl::LetExp,
    ir::ocl::ModelElement,
    ir::ocl::IfExp,
    ir::ocl::VarExp,
    ocl::ir::EFClass,
    ocl::WithContextVariable,
    ir::ocl::OclDerivedProperty,
    ir::ocl::OclOperation,
    Constraint,
    ir::ocl::OclInvariant,
    ocl::ir::VariableDeclaration,
    ir::ocl::WithContextVariable,
    CollectionTypeRef,
    ir::OrderedSetTypeRef,
    ir::SequenceTypeRef,
    ir::BagTypeRef,
    ir::SetTypeRef,
    TypeRef,
    ir::InvalidTypeRef,
    ir::CollectionTypeRef,
    ir::MetaTypeRef,
    ir::TupleTypeElement,
    ir::EFEnumLiteral,
    ir::EEnum,
    ir::EClass,
    EFType,
    ir::EFEnum,
    ir::EPackage,
    ir::EFPackage,
    VariableDeclaration,
    ir::ocl::Iterator,
    ir::VariableDeclaration,
    ir::EStructuralFeature,
    PropertyFeatureRef,
    ir::BuiltinPropertyRef,
    ir::DerivedPropertyRef,
    ir::MetamodelFeatureRef,
    ir::TupleFieldRef,
    OperationFeatureRef,
    ir::DefinedOperationRef,
    ir::BuiltinOperationRef,
    ir::EFClass,
    FeatureRef,
    ir::PropertyFeatureRef,
    ir::OperationFeatureRef,
    ir::FeatureRef,
    ir::Constraint,
    ir::Parameter,
    ir::EFMetamodel,
    AbstractFunction,
    ir::DerivedProperty,
    ir::Specification,
    ir::EFType,
    TypedElement,
    ir::AbstractFunction,
    ir::TypeRef,
    ir::TypedElement,
    ir::EFTupleType,
    ir::EFPrimitiveType,
    ir::Operation,
    OperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ir::ocl::oclanylibelement_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclAnyLibElement)


def test_ir::ocl::oclanylibelement_constructor_exists():
    assert callable(ir::ocl::OclAnyLibElement.__init__)


def test_ir::ocl::oclanylibelement_constructor_args():
    sig = inspect.signature(ir::ocl::OclAnyLibElement.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::sequenceliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::SequenceLiteralExp)


def test_ir::ocl::sequenceliteralexp_constructor_exists():
    assert callable(ir::ocl::SequenceLiteralExp.__init__)


def test_ir::ocl::sequenceliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::SequenceLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::orderedsetliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OrderedSetLiteralExp)


def test_ir::ocl::orderedsetliteralexp_constructor_exists():
    assert callable(ir::ocl::OrderedSetLiteralExp.__init__)


def test_ir::ocl::orderedsetliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::OrderedSetLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::bagliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::BagLiteralExp)


def test_ir::ocl::bagliteralexp_constructor_exists():
    assert callable(ir::ocl::BagLiteralExp.__init__)


def test_ir::ocl::bagliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::BagLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::setliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::SetLiteralExp)


def test_ir::ocl::setliteralexp_constructor_exists():
    assert callable(ir::ocl::SetLiteralExp.__init__)


def test_ir::ocl::setliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::SetLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::efenumliteral_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::EFEnumLiteral)


def test_ocl::ir::efenumliteral_constructor_exists():
    assert callable(ocl::ir::EFEnumLiteral.__init__)


def test_ocl::ir::efenumliteral_constructor_args():
    sig = inspect.signature(ocl::ir::EFEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::metatyperef_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::MetaTypeRef)


def test_ocl::ir::metatyperef_constructor_exists():
    assert callable(ocl::ir::MetaTypeRef.__init__)


def test_ocl::ir::metatyperef_constructor_args():
    sig = inspect.signature(ocl::ir::MetaTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::TuplePart)


def test_ir::ocl::tuplepart_constructor_exists():
    assert callable(ir::ocl::TuplePart.__init__)


def test_ir::ocl::tuplepart_constructor_args():
    sig = inspect.signature(ir::ocl::TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::ocl::tuplepart_has_name():
    assert hasattr(ir::ocl::TuplePart, "name")
    descriptor = None
    for klass in ir::ocl::TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::eftupletype_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::EFTupleType)


def test_ocl::ir::eftupletype_constructor_exists():
    assert callable(ocl::ir::EFTupleType.__init__)


def test_ocl::ir::eftupletype_constructor_args():
    sig = inspect.signature(ocl::ir::EFTupleType.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::IntegerLiteralExp)


def test_ir::ocl::integerliteralexp_constructor_exists():
    assert callable(ir::ocl::IntegerLiteralExp.__init__)


def test_ir::ocl::integerliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::ocl::integerliteralexp_has_value():
    assert hasattr(ir::ocl::IntegerLiteralExp, "value")
    descriptor = None
    for klass in ir::ocl::IntegerLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::EnumLiteralExp)


def test_ir::ocl::enumliteralexp_constructor_exists():
    assert callable(ir::ocl::EnumLiteralExp.__init__)


def test_ir::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::StringLiteralExp)


def test_ir::ocl::stringliteralexp_constructor_exists():
    assert callable(ir::ocl::StringLiteralExp.__init__)


def test_ir::ocl::stringliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::ocl::stringliteralexp_has_value():
    assert hasattr(ir::ocl::StringLiteralExp, "value")
    descriptor = None
    for klass in ir::ocl::StringLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::oclinvalid_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclInvalid)


def test_ir::ocl::oclinvalid_constructor_exists():
    assert callable(ir::ocl::OclInvalid.__init__)


def test_ir::ocl::oclinvalid_constructor_args():
    sig = inspect.signature(ir::ocl::OclInvalid.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::RealLiteralExp)


def test_ir::ocl::realliteralexp_constructor_exists():
    assert callable(ir::ocl::RealLiteralExp.__init__)


def test_ir::ocl::realliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::ocl::realliteralexp_has_value():
    assert hasattr(ir::ocl::RealLiteralExp, "value")
    descriptor = None
    for klass in ir::ocl::RealLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::oclundefined_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclUndefined)


def test_ir::ocl::oclundefined_constructor_exists():
    assert callable(ir::ocl::OclUndefined.__init__)


def test_ir::ocl::oclundefined_constructor_args():
    sig = inspect.signature(ir::ocl::OclUndefined.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::CollectionLiteralExp)


def test_ir::ocl::collectionliteralexp_constructor_exists():
    assert callable(ir::ocl::CollectionLiteralExp.__init__)


def test_ir::ocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::TupleLiteralExp)


def test_ir::ocl::tupleliteralexp_constructor_exists():
    assert callable(ir::ocl::TupleLiteralExp.__init__)


def test_ir::ocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::BooleanLiteralExp)


def test_ir::ocl::booleanliteralexp_constructor_exists():
    assert callable(ir::ocl::BooleanLiteralExp.__init__)


def test_ir::ocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(ir::ocl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::ocl::booleanliteralexp_has_value():
    assert hasattr(ir::ocl::BooleanLiteralExp, "value")
    descriptor = None
    for klass in ir::ocl::BooleanLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::IterateExp)


def test_ir::ocl::iterateexp_constructor_exists():
    assert callable(ir::ocl::IterateExp.__init__)


def test_ir::ocl::iterateexp_constructor_args():
    sig = inspect.signature(ir::ocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::IteratorExp)


def test_ir::ocl::iteratorexp_constructor_exists():
    assert callable(ir::ocl::IteratorExp.__init__)


def test_ir::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(ir::ocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::ocl::iteratorexp_has_name():
    assert hasattr(ir::ocl::IteratorExp, "name")
    descriptor = None
    for klass in ir::ocl::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::PropertyFeatureRef)


def test_ocl::ir::propertyfeatureref_constructor_exists():
    assert callable(ocl::ir::PropertyFeatureRef.__init__)


def test_ocl::ir::propertyfeatureref_constructor_args():
    sig = inspect.signature(ocl::ir::PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::OperationFeatureRef)


def test_ocl::ir::operationfeatureref_constructor_exists():
    assert callable(ocl::ir::OperationFeatureRef.__init__)


def test_ocl::ir::operationfeatureref_constructor_args():
    sig = inspect.signature(ocl::ir::OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_abstractoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(AbstractOperationCallExp)


def test_abstractoperationcallexp_constructor_exists():
    assert callable(AbstractOperationCallExp.__init__)


def test_abstractoperationcallexp_constructor_args():
    sig = inspect.signature(AbstractOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::collectioncallexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::CollectionCallExp)


def test_ir::ocl::collectioncallexp_constructor_exists():
    assert callable(ir::ocl::CollectionCallExp.__init__)


def test_ir::ocl::collectioncallexp_constructor_args():
    sig = inspect.signature(ir::ocl::CollectionCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::ocl::collectioncallexp_has_name():
    assert hasattr(ir::ocl::CollectionCallExp, "name")
    descriptor = None
    for klass in ir::ocl::CollectionCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OperationCallExp)


def test_ir::ocl::operationcallexp_constructor_exists():
    assert callable(ir::ocl::OperationCallExp.__init__)


def test_ir::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(ir::ocl::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::ocl::operationcallexp_has_name():
    assert hasattr(ir::ocl::OperationCallExp, "name")
    descriptor = None
    for klass in ir::ocl::OperationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OperatorCallExp)


def test_ir::ocl::operatorcallexp_constructor_exists():
    assert callable(ir::ocl::OperatorCallExp.__init__)


def test_ir::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(ir::ocl::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir::ocl::operatorcallexp_has_operator():
    assert hasattr(ir::ocl::OperatorCallExp, "operator")
    descriptor = None
    for klass in ir::ocl::OperatorCallExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::LoopExp)


def test_ir::ocl::loopexp_constructor_exists():
    assert callable(ir::ocl::LoopExp.__init__)


def test_ir::ocl::loopexp_constructor_args():
    sig = inspect.signature(ir::ocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::PropertyCallExp)


def test_ir::ocl::propertycallexp_constructor_exists():
    assert callable(ir::ocl::PropertyCallExp.__init__)


def test_ir::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(ir::ocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::ocl::propertycallexp_has_name():
    assert hasattr(ir::ocl::PropertyCallExp, "name")
    descriptor = None
    for klass in ir::ocl::PropertyCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::abstractoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::AbstractOperationCallExp)


def test_ir::ocl::abstractoperationcallexp_constructor_exists():
    assert callable(ir::ocl::AbstractOperationCallExp.__init__)


def test_ir::ocl::abstractoperationcallexp_constructor_args():
    sig = inspect.signature(ir::ocl::AbstractOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::typeref_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::TypeRef)


def test_ocl::ir::typeref_constructor_exists():
    assert callable(ocl::ir::TypeRef.__init__)


def test_ocl::ir::typeref_constructor_args():
    sig = inspect.signature(ocl::ir::TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclExpression)


def test_ir::ocl::oclexpression_constructor_exists():
    assert callable(ir::ocl::OclExpression.__init__)


def test_ir::ocl::oclexpression_constructor_args():
    sig = inspect.signature(ir::ocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_derivedproperty_is_not_abstract():
    assert not inspect.isabstract(DerivedProperty)


def test_derivedproperty_constructor_exists():
    assert callable(DerivedProperty.__init__)


def test_derivedproperty_constructor_args():
    sig = inspect.signature(DerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::unsupportedexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::UnsupportedExp)


def test_ir::ocl::unsupportedexp_constructor_exists():
    assert callable(ir::ocl::UnsupportedExp.__init__)


def test_ir::ocl::unsupportedexp_constructor_args():
    sig = inspect.signature(ir::ocl::UnsupportedExp.__init__)
    params = list(sig.parameters.keys())
    assert "reason" in params, "Missing parameter 'reason'"
    assert "description" in params, "Missing parameter 'description'"

def test_ir::ocl::unsupportedexp_has_reason():
    assert hasattr(ir::ocl::UnsupportedExp, "reason")
    descriptor = None
    for klass in ir::ocl::UnsupportedExp.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)

def test_ir::ocl::unsupportedexp_has_description():
    assert hasattr(ir::ocl::UnsupportedExp, "description")
    descriptor = None
    for klass in ir::ocl::UnsupportedExp.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ir::ocl::callexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::CallExp)


def test_ir::ocl::callexp_constructor_exists():
    assert callable(ir::ocl::CallExp.__init__)


def test_ir::ocl::callexp_constructor_args():
    sig = inspect.signature(ir::ocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::LiteralExp)


def test_ir::ocl::literalexp_constructor_exists():
    assert callable(ir::ocl::LiteralExp.__init__)


def test_ir::ocl::literalexp_constructor_args():
    sig = inspect.signature(ir::ocl::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::LetExp)


def test_ir::ocl::letexp_constructor_exists():
    assert callable(ir::ocl::LetExp.__init__)


def test_ir::ocl::letexp_constructor_args():
    sig = inspect.signature(ir::ocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::modelelement_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::ModelElement)


def test_ir::ocl::modelelement_constructor_exists():
    assert callable(ir::ocl::ModelElement.__init__)


def test_ir::ocl::modelelement_constructor_args():
    sig = inspect.signature(ir::ocl::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::IfExp)


def test_ir::ocl::ifexp_constructor_exists():
    assert callable(ir::ocl::IfExp.__init__)


def test_ir::ocl::ifexp_constructor_args():
    sig = inspect.signature(ir::ocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::varexp_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::VarExp)


def test_ir::ocl::varexp_constructor_exists():
    assert callable(ir::ocl::VarExp.__init__)


def test_ir::ocl::varexp_constructor_args():
    sig = inspect.signature(ir::ocl::VarExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::efclass_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::EFClass)


def test_ocl::ir::efclass_constructor_exists():
    assert callable(ocl::ir::EFClass.__init__)


def test_ocl::ir::efclass_constructor_args():
    sig = inspect.signature(ocl::ir::EFClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::withcontextvariable_is_not_abstract():
    assert not inspect.isabstract(ocl::WithContextVariable)


def test_ocl::withcontextvariable_constructor_exists():
    assert callable(ocl::WithContextVariable.__init__)


def test_ocl::withcontextvariable_constructor_args():
    sig = inspect.signature(ocl::WithContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::oclderivedproperty_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclDerivedProperty)


def test_ir::ocl::oclderivedproperty_constructor_exists():
    assert callable(ir::ocl::OclDerivedProperty.__init__)


def test_ir::ocl::oclderivedproperty_constructor_args():
    sig = inspect.signature(ir::ocl::OclDerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::ocloperation_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclOperation)


def test_ir::ocl::ocloperation_constructor_exists():
    assert callable(ir::ocl::OclOperation.__init__)


def test_ir::ocl::ocloperation_constructor_args():
    sig = inspect.signature(ir::ocl::OclOperation.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::oclinvariant_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::OclInvariant)


def test_ir::ocl::oclinvariant_constructor_exists():
    assert callable(ir::ocl::OclInvariant.__init__)


def test_ir::ocl::oclinvariant_constructor_args():
    sig = inspect.signature(ir::ocl::OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ir::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ocl::ir::VariableDeclaration)


def test_ocl::ir::variabledeclaration_constructor_exists():
    assert callable(ocl::ir::VariableDeclaration.__init__)


def test_ocl::ir::variabledeclaration_constructor_args():
    sig = inspect.signature(ocl::ir::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::withcontextvariable_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::WithContextVariable)


def test_ir::ocl::withcontextvariable_constructor_exists():
    assert callable(ir::ocl::WithContextVariable.__init__)


def test_ir::ocl::withcontextvariable_constructor_args():
    sig = inspect.signature(ir::ocl::WithContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_collectiontyperef_is_not_abstract():
    assert not inspect.isabstract(CollectionTypeRef)


def test_collectiontyperef_constructor_exists():
    assert callable(CollectionTypeRef.__init__)


def test_collectiontyperef_constructor_args():
    sig = inspect.signature(CollectionTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::orderedsettyperef_is_not_abstract():
    assert not inspect.isabstract(ir::OrderedSetTypeRef)


def test_ir::orderedsettyperef_constructor_exists():
    assert callable(ir::OrderedSetTypeRef.__init__)


def test_ir::orderedsettyperef_constructor_args():
    sig = inspect.signature(ir::OrderedSetTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::sequencetyperef_is_not_abstract():
    assert not inspect.isabstract(ir::SequenceTypeRef)


def test_ir::sequencetyperef_constructor_exists():
    assert callable(ir::SequenceTypeRef.__init__)


def test_ir::sequencetyperef_constructor_args():
    sig = inspect.signature(ir::SequenceTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::bagtyperef_is_not_abstract():
    assert not inspect.isabstract(ir::BagTypeRef)


def test_ir::bagtyperef_constructor_exists():
    assert callable(ir::BagTypeRef.__init__)


def test_ir::bagtyperef_constructor_args():
    sig = inspect.signature(ir::BagTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::settyperef_is_not_abstract():
    assert not inspect.isabstract(ir::SetTypeRef)


def test_ir::settyperef_constructor_exists():
    assert callable(ir::SetTypeRef.__init__)


def test_ir::settyperef_constructor_args():
    sig = inspect.signature(ir::SetTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_typeref_is_not_abstract():
    assert not inspect.isabstract(TypeRef)


def test_typeref_constructor_exists():
    assert callable(TypeRef.__init__)


def test_typeref_constructor_args():
    sig = inspect.signature(TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::invalidtyperef_is_not_abstract():
    assert not inspect.isabstract(ir::InvalidTypeRef)


def test_ir::invalidtyperef_constructor_exists():
    assert callable(ir::InvalidTypeRef.__init__)


def test_ir::invalidtyperef_constructor_args():
    sig = inspect.signature(ir::InvalidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::collectiontyperef_is_not_abstract():
    assert not inspect.isabstract(ir::CollectionTypeRef)


def test_ir::collectiontyperef_constructor_exists():
    assert callable(ir::CollectionTypeRef.__init__)


def test_ir::collectiontyperef_constructor_args():
    sig = inspect.signature(ir::CollectionTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::metatyperef_is_not_abstract():
    assert not inspect.isabstract(ir::MetaTypeRef)


def test_ir::metatyperef_constructor_exists():
    assert callable(ir::MetaTypeRef.__init__)


def test_ir::metatyperef_constructor_args():
    sig = inspect.signature(ir::MetaTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::tupletypeelement_is_not_abstract():
    assert not inspect.isabstract(ir::TupleTypeElement)


def test_ir::tupletypeelement_constructor_exists():
    assert callable(ir::TupleTypeElement.__init__)


def test_ir::tupletypeelement_constructor_args():
    sig = inspect.signature(ir::TupleTypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::tupletypeelement_has_name():
    assert hasattr(ir::TupleTypeElement, "name")
    descriptor = None
    for klass in ir::TupleTypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::efenumliteral_is_not_abstract():
    assert not inspect.isabstract(ir::EFEnumLiteral)


def test_ir::efenumliteral_constructor_exists():
    assert callable(ir::EFEnumLiteral.__init__)


def test_ir::efenumliteral_constructor_args():
    sig = inspect.signature(ir::EFEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::efenumliteral_has_name():
    assert hasattr(ir::EFEnumLiteral, "name")
    descriptor = None
    for klass in ir::EFEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::eenum_is_not_abstract():
    assert not inspect.isabstract(ir::EEnum)


def test_ir::eenum_constructor_exists():
    assert callable(ir::EEnum.__init__)


def test_ir::eenum_constructor_args():
    sig = inspect.signature(ir::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ir::eclass_is_not_abstract():
    assert not inspect.isabstract(ir::EClass)


def test_ir::eclass_constructor_exists():
    assert callable(ir::EClass.__init__)


def test_ir::eclass_constructor_args():
    sig = inspect.signature(ir::EClass.__init__)
    params = list(sig.parameters.keys())



def test_eftype_is_not_abstract():
    assert not inspect.isabstract(EFType)


def test_eftype_constructor_exists():
    assert callable(EFType.__init__)


def test_eftype_constructor_args():
    sig = inspect.signature(EFType.__init__)
    params = list(sig.parameters.keys())



def test_ir::efenum_is_not_abstract():
    assert not inspect.isabstract(ir::EFEnum)


def test_ir::efenum_constructor_exists():
    assert callable(ir::EFEnum.__init__)


def test_ir::efenum_constructor_args():
    sig = inspect.signature(ir::EFEnum.__init__)
    params = list(sig.parameters.keys())



def test_ir::epackage_is_not_abstract():
    assert not inspect.isabstract(ir::EPackage)


def test_ir::epackage_constructor_exists():
    assert callable(ir::EPackage.__init__)


def test_ir::epackage_constructor_args():
    sig = inspect.signature(ir::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ir::efpackage_is_not_abstract():
    assert not inspect.isabstract(ir::EFPackage)


def test_ir::efpackage_constructor_exists():
    assert callable(ir::EFPackage.__init__)


def test_ir::efpackage_constructor_args():
    sig = inspect.signature(ir::EFPackage.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(ir::ocl::Iterator)


def test_ir::ocl::iterator_constructor_exists():
    assert callable(ir::ocl::Iterator.__init__)


def test_ir::ocl::iterator_constructor_args():
    sig = inspect.signature(ir::ocl::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ir::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ir::VariableDeclaration)


def test_ir::variabledeclaration_constructor_exists():
    assert callable(ir::VariableDeclaration.__init__)


def test_ir::variabledeclaration_constructor_args():
    sig = inspect.signature(ir::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::variabledeclaration_has_name():
    assert hasattr(ir::VariableDeclaration, "name")
    descriptor = None
    for klass in ir::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ir::EStructuralFeature)


def test_ir::estructuralfeature_constructor_exists():
    assert callable(ir::EStructuralFeature.__init__)


def test_ir::estructuralfeature_constructor_args():
    sig = inspect.signature(ir::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(PropertyFeatureRef)


def test_propertyfeatureref_constructor_exists():
    assert callable(PropertyFeatureRef.__init__)


def test_propertyfeatureref_constructor_args():
    sig = inspect.signature(PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::builtinpropertyref_is_not_abstract():
    assert not inspect.isabstract(ir::BuiltinPropertyRef)


def test_ir::builtinpropertyref_constructor_exists():
    assert callable(ir::BuiltinPropertyRef.__init__)


def test_ir::builtinpropertyref_constructor_args():
    sig = inspect.signature(ir::BuiltinPropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::derivedpropertyref_is_not_abstract():
    assert not inspect.isabstract(ir::DerivedPropertyRef)


def test_ir::derivedpropertyref_constructor_exists():
    assert callable(ir::DerivedPropertyRef.__init__)


def test_ir::derivedpropertyref_constructor_args():
    sig = inspect.signature(ir::DerivedPropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::metamodelfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir::MetamodelFeatureRef)


def test_ir::metamodelfeatureref_constructor_exists():
    assert callable(ir::MetamodelFeatureRef.__init__)


def test_ir::metamodelfeatureref_constructor_args():
    sig = inspect.signature(ir::MetamodelFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::tuplefieldref_is_not_abstract():
    assert not inspect.isabstract(ir::TupleFieldRef)


def test_ir::tuplefieldref_constructor_exists():
    assert callable(ir::TupleFieldRef.__init__)


def test_ir::tuplefieldref_constructor_args():
    sig = inspect.signature(ir::TupleFieldRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::tuplefieldref_has_name():
    assert hasattr(ir::TupleFieldRef, "name")
    descriptor = None
    for klass in ir::TupleFieldRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(OperationFeatureRef)


def test_operationfeatureref_constructor_exists():
    assert callable(OperationFeatureRef.__init__)


def test_operationfeatureref_constructor_args():
    sig = inspect.signature(OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::definedoperationref_is_not_abstract():
    assert not inspect.isabstract(ir::DefinedOperationRef)


def test_ir::definedoperationref_constructor_exists():
    assert callable(ir::DefinedOperationRef.__init__)


def test_ir::definedoperationref_constructor_args():
    sig = inspect.signature(ir::DefinedOperationRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::builtinoperationref_is_not_abstract():
    assert not inspect.isabstract(ir::BuiltinOperationRef)


def test_ir::builtinoperationref_constructor_exists():
    assert callable(ir::BuiltinOperationRef.__init__)


def test_ir::builtinoperationref_constructor_args():
    sig = inspect.signature(ir::BuiltinOperationRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::efclass_is_not_abstract():
    assert not inspect.isabstract(ir::EFClass)


def test_ir::efclass_constructor_exists():
    assert callable(ir::EFClass.__init__)


def test_ir::efclass_constructor_args():
    sig = inspect.signature(ir::EFClass.__init__)
    params = list(sig.parameters.keys())



def test_featureref_is_not_abstract():
    assert not inspect.isabstract(FeatureRef)


def test_featureref_constructor_exists():
    assert callable(FeatureRef.__init__)


def test_featureref_constructor_args():
    sig = inspect.signature(FeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir::PropertyFeatureRef)


def test_ir::propertyfeatureref_constructor_exists():
    assert callable(ir::PropertyFeatureRef.__init__)


def test_ir::propertyfeatureref_constructor_args():
    sig = inspect.signature(ir::PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir::OperationFeatureRef)


def test_ir::operationfeatureref_constructor_exists():
    assert callable(ir::OperationFeatureRef.__init__)


def test_ir::operationfeatureref_constructor_args():
    sig = inspect.signature(ir::OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::featureref_is_not_abstract():
    assert not inspect.isabstract(ir::FeatureRef)


def test_ir::featureref_constructor_exists():
    assert callable(ir::FeatureRef.__init__)


def test_ir::featureref_constructor_args():
    sig = inspect.signature(ir::FeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::constraint_is_not_abstract():
    assert not inspect.isabstract(ir::Constraint)


def test_ir::constraint_constructor_exists():
    assert callable(ir::Constraint.__init__)


def test_ir::constraint_constructor_args():
    sig = inspect.signature(ir::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::constraint_has_name():
    assert hasattr(ir::Constraint, "name")
    descriptor = None
    for klass in ir::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::parameter_is_not_abstract():
    assert not inspect.isabstract(ir::Parameter)


def test_ir::parameter_constructor_exists():
    assert callable(ir::Parameter.__init__)


def test_ir::parameter_constructor_args():
    sig = inspect.signature(ir::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ir::efmetamodel_is_not_abstract():
    assert not inspect.isabstract(ir::EFMetamodel)


def test_ir::efmetamodel_constructor_exists():
    assert callable(ir::EFMetamodel.__init__)


def test_ir::efmetamodel_constructor_args():
    sig = inspect.signature(ir::EFMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_abstractfunction_is_not_abstract():
    assert not inspect.isabstract(AbstractFunction)


def test_abstractfunction_constructor_exists():
    assert callable(AbstractFunction.__init__)


def test_abstractfunction_constructor_args():
    sig = inspect.signature(AbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_ir::derivedproperty_is_not_abstract():
    assert not inspect.isabstract(ir::DerivedProperty)


def test_ir::derivedproperty_constructor_exists():
    assert callable(ir::DerivedProperty.__init__)


def test_ir::derivedproperty_constructor_args():
    sig = inspect.signature(ir::DerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_ir::specification_is_not_abstract():
    assert not inspect.isabstract(ir::Specification)


def test_ir::specification_constructor_exists():
    assert callable(ir::Specification.__init__)


def test_ir::specification_constructor_args():
    sig = inspect.signature(ir::Specification.__init__)
    params = list(sig.parameters.keys())



def test_ir::eftype_is_not_abstract():
    assert not inspect.isabstract(ir::EFType)


def test_ir::eftype_constructor_exists():
    assert callable(ir::EFType.__init__)


def test_ir::eftype_constructor_args():
    sig = inspect.signature(ir::EFType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ir::abstractfunction_is_not_abstract():
    assert not inspect.isabstract(ir::AbstractFunction)


def test_ir::abstractfunction_constructor_exists():
    assert callable(ir::AbstractFunction.__init__)


def test_ir::abstractfunction_constructor_args():
    sig = inspect.signature(ir::AbstractFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::abstractfunction_has_name():
    assert hasattr(ir::AbstractFunction, "name")
    descriptor = None
    for klass in ir::AbstractFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::typeref_is_not_abstract():
    assert not inspect.isabstract(ir::TypeRef)


def test_ir::typeref_constructor_exists():
    assert callable(ir::TypeRef.__init__)


def test_ir::typeref_constructor_args():
    sig = inspect.signature(ir::TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::typedelement_is_not_abstract():
    assert not inspect.isabstract(ir::TypedElement)


def test_ir::typedelement_constructor_exists():
    assert callable(ir::TypedElement.__init__)


def test_ir::typedelement_constructor_args():
    sig = inspect.signature(ir::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ir::eftupletype_is_not_abstract():
    assert not inspect.isabstract(ir::EFTupleType)


def test_ir::eftupletype_constructor_exists():
    assert callable(ir::EFTupleType.__init__)


def test_ir::eftupletype_constructor_args():
    sig = inspect.signature(ir::EFTupleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ir::eftupletype_has_id():
    assert hasattr(ir::EFTupleType, "id")
    descriptor = None
    for klass in ir::EFTupleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ir::efprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ir::EFPrimitiveType)


def test_ir::efprimitivetype_constructor_exists():
    assert callable(ir::EFPrimitiveType.__init__)


def test_ir::efprimitivetype_constructor_args():
    sig = inspect.signature(ir::EFPrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::efprimitivetype_has_name():
    assert hasattr(ir::EFPrimitiveType, "name")
    descriptor = None
    for klass in ir::EFPrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::operation_is_not_abstract():
    assert not inspect.isabstract(ir::Operation)


def test_ir::operation_constructor_exists():
    assert callable(ir::Operation.__init__)


def test_ir::operation_constructor_args():
    sig = inspect.signature(ir::Operation.__init__)
    params = list(sig.parameters.keys())

def test_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "GREATER",
        "DIV",
        "XOR",
        "NOT",
        "PLUS",
        "DISTINCT",
        "GREATER_OR_EQUAL",
        "MUL",
        "IMPLIES",
        "LESS",
        "LESS_OR_EQUAL",
        "OR",
        "AND",
        "MINUS",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"


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
ir::ocl::OclAnyLibElement_strategy = st.builds(
    ir::ocl::OclAnyLibElement,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
ir::ocl::SequenceLiteralExp_strategy = st.builds(
    ir::ocl::SequenceLiteralExp,
)
ir::ocl::OrderedSetLiteralExp_strategy = st.builds(
    ir::ocl::OrderedSetLiteralExp,
)
ir::ocl::BagLiteralExp_strategy = st.builds(
    ir::ocl::BagLiteralExp,
)
ir::ocl::SetLiteralExp_strategy = st.builds(
    ir::ocl::SetLiteralExp,
)
ocl::ir::EFEnumLiteral_strategy = st.builds(
    ocl::ir::EFEnumLiteral,
)
ocl::ir::MetaTypeRef_strategy = st.builds(
    ocl::ir::MetaTypeRef,
)
ir::ocl::TuplePart_strategy = st.builds(
    ir::ocl::TuplePart,
    name=
        safe_text
)
TuplePart_strategy = st.builds(
    TuplePart,
)
ocl::ir::EFTupleType_strategy = st.builds(
    ocl::ir::EFTupleType,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ir::ocl::IntegerLiteralExp_strategy = st.builds(
    ir::ocl::IntegerLiteralExp,
    value=
        safe_text
)
ir::ocl::EnumLiteralExp_strategy = st.builds(
    ir::ocl::EnumLiteralExp,
)
ir::ocl::StringLiteralExp_strategy = st.builds(
    ir::ocl::StringLiteralExp,
    value=
        safe_text
)
ir::ocl::OclInvalid_strategy = st.builds(
    ir::ocl::OclInvalid,
)
ir::ocl::RealLiteralExp_strategy = st.builds(
    ir::ocl::RealLiteralExp,
    value=
        safe_text
)
ir::ocl::OclUndefined_strategy = st.builds(
    ir::ocl::OclUndefined,
)
ir::ocl::CollectionLiteralExp_strategy = st.builds(
    ir::ocl::CollectionLiteralExp,
)
ir::ocl::TupleLiteralExp_strategy = st.builds(
    ir::ocl::TupleLiteralExp,
)
ir::ocl::BooleanLiteralExp_strategy = st.builds(
    ir::ocl::BooleanLiteralExp,
    value=
        st.booleans()
)
LoopExp_strategy = st.builds(
    LoopExp,
)
ir::ocl::IterateExp_strategy = st.builds(
    ir::ocl::IterateExp,
)
ir::ocl::IteratorExp_strategy = st.builds(
    ir::ocl::IteratorExp,
    name=
        safe_text
)
Iterator_strategy = st.builds(
    Iterator,
)
ocl::ir::PropertyFeatureRef_strategy = st.builds(
    ocl::ir::PropertyFeatureRef,
)
ocl::ir::OperationFeatureRef_strategy = st.builds(
    ocl::ir::OperationFeatureRef,
)
AbstractOperationCallExp_strategy = st.builds(
    AbstractOperationCallExp,
)
ir::ocl::CollectionCallExp_strategy = st.builds(
    ir::ocl::CollectionCallExp,
    name=
        safe_text
)
ir::ocl::OperationCallExp_strategy = st.builds(
    ir::ocl::OperationCallExp,
    name=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
ir::ocl::OperatorCallExp_strategy = st.builds(
    ir::ocl::OperatorCallExp,
    operator=
        safe_text
)
ir::ocl::LoopExp_strategy = st.builds(
    ir::ocl::LoopExp,
)
ir::ocl::PropertyCallExp_strategy = st.builds(
    ir::ocl::PropertyCallExp,
    name=
        safe_text
)
ir::ocl::AbstractOperationCallExp_strategy = st.builds(
    ir::ocl::AbstractOperationCallExp,
)
ocl::ir::TypeRef_strategy = st.builds(
    ocl::ir::TypeRef,
)
ir::ocl::OclExpression_strategy = st.builds(
    ir::ocl::OclExpression,
)
Operation_strategy = st.builds(
    Operation,
)
DerivedProperty_strategy = st.builds(
    DerivedProperty,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
ir::ocl::UnsupportedExp_strategy = st.builds(
    ir::ocl::UnsupportedExp,
    reason=
        safe_text,
    description=
        safe_text
)
ir::ocl::CallExp_strategy = st.builds(
    ir::ocl::CallExp,
)
ir::ocl::LiteralExp_strategy = st.builds(
    ir::ocl::LiteralExp,
)
ir::ocl::LetExp_strategy = st.builds(
    ir::ocl::LetExp,
)
ir::ocl::ModelElement_strategy = st.builds(
    ir::ocl::ModelElement,
)
ir::ocl::IfExp_strategy = st.builds(
    ir::ocl::IfExp,
)
ir::ocl::VarExp_strategy = st.builds(
    ir::ocl::VarExp,
)
ocl::ir::EFClass_strategy = st.builds(
    ocl::ir::EFClass,
)
ocl::WithContextVariable_strategy = st.builds(
    ocl::WithContextVariable,
)
ir::ocl::OclDerivedProperty_strategy = st.builds(
    ir::ocl::OclDerivedProperty,
)
ir::ocl::OclOperation_strategy = st.builds(
    ir::ocl::OclOperation,
)
Constraint_strategy = st.builds(
    Constraint,
)
ir::ocl::OclInvariant_strategy = st.builds(
    ir::ocl::OclInvariant,
)
ocl::ir::VariableDeclaration_strategy = st.builds(
    ocl::ir::VariableDeclaration,
)
ir::ocl::WithContextVariable_strategy = st.builds(
    ir::ocl::WithContextVariable,
)
CollectionTypeRef_strategy = st.builds(
    CollectionTypeRef,
)
ir::OrderedSetTypeRef_strategy = st.builds(
    ir::OrderedSetTypeRef,
)
ir::SequenceTypeRef_strategy = st.builds(
    ir::SequenceTypeRef,
)
ir::BagTypeRef_strategy = st.builds(
    ir::BagTypeRef,
)
ir::SetTypeRef_strategy = st.builds(
    ir::SetTypeRef,
)
TypeRef_strategy = st.builds(
    TypeRef,
)
ir::InvalidTypeRef_strategy = st.builds(
    ir::InvalidTypeRef,
)
ir::CollectionTypeRef_strategy = st.builds(
    ir::CollectionTypeRef,
)
ir::MetaTypeRef_strategy = st.builds(
    ir::MetaTypeRef,
)
ir::TupleTypeElement_strategy = st.builds(
    ir::TupleTypeElement,
    name=
        safe_text
)
ir::EFEnumLiteral_strategy = st.builds(
    ir::EFEnumLiteral,
    name=
        safe_text
)
ir::EEnum_strategy = st.builds(
    ir::EEnum,
)
ir::EClass_strategy = st.builds(
    ir::EClass,
)
EFType_strategy = st.builds(
    EFType,
)
ir::EFEnum_strategy = st.builds(
    ir::EFEnum,
)
ir::EPackage_strategy = st.builds(
    ir::EPackage,
)
ir::EFPackage_strategy = st.builds(
    ir::EFPackage,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ir::ocl::Iterator_strategy = st.builds(
    ir::ocl::Iterator,
)
ir::VariableDeclaration_strategy = st.builds(
    ir::VariableDeclaration,
    name=
        safe_text
)
ir::EStructuralFeature_strategy = st.builds(
    ir::EStructuralFeature,
)
PropertyFeatureRef_strategy = st.builds(
    PropertyFeatureRef,
)
ir::BuiltinPropertyRef_strategy = st.builds(
    ir::BuiltinPropertyRef,
)
ir::DerivedPropertyRef_strategy = st.builds(
    ir::DerivedPropertyRef,
)
ir::MetamodelFeatureRef_strategy = st.builds(
    ir::MetamodelFeatureRef,
)
ir::TupleFieldRef_strategy = st.builds(
    ir::TupleFieldRef,
    name=
        safe_text
)
OperationFeatureRef_strategy = st.builds(
    OperationFeatureRef,
)
ir::DefinedOperationRef_strategy = st.builds(
    ir::DefinedOperationRef,
)
ir::BuiltinOperationRef_strategy = st.builds(
    ir::BuiltinOperationRef,
)
ir::EFClass_strategy = st.builds(
    ir::EFClass,
)
FeatureRef_strategy = st.builds(
    FeatureRef,
)
ir::PropertyFeatureRef_strategy = st.builds(
    ir::PropertyFeatureRef,
)
ir::OperationFeatureRef_strategy = st.builds(
    ir::OperationFeatureRef,
)
ir::FeatureRef_strategy = st.builds(
    ir::FeatureRef,
)
ir::Constraint_strategy = st.builds(
    ir::Constraint,
    name=
        safe_text
)
ir::Parameter_strategy = st.builds(
    ir::Parameter,
)
ir::EFMetamodel_strategy = st.builds(
    ir::EFMetamodel,
)
AbstractFunction_strategy = st.builds(
    AbstractFunction,
)
ir::DerivedProperty_strategy = st.builds(
    ir::DerivedProperty,
)
ir::Specification_strategy = st.builds(
    ir::Specification,
)
ir::EFType_strategy = st.builds(
    ir::EFType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ir::AbstractFunction_strategy = st.builds(
    ir::AbstractFunction,
    name=
        safe_text
)
ir::TypeRef_strategy = st.builds(
    ir::TypeRef,
)
ir::TypedElement_strategy = st.builds(
    ir::TypedElement,
)
ir::EFTupleType_strategy = st.builds(
    ir::EFTupleType,
    id=
        safe_text
)
ir::EFPrimitiveType_strategy = st.builds(
    ir::EFPrimitiveType,
    name=
        safe_text
)
ir::Operation_strategy = st.builds(
    ir::Operation,
)

@given(instance=ir::ocl::OclAnyLibElement_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclanylibelement_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclAnyLibElement)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=ir::ocl::SequenceLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::sequenceliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::SequenceLiteralExp)

@given(instance=ir::ocl::OrderedSetLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::orderedsetliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::OrderedSetLiteralExp)

@given(instance=ir::ocl::BagLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::bagliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::BagLiteralExp)

@given(instance=ir::ocl::SetLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::setliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::SetLiteralExp)

@given(instance=ocl::ir::EFEnumLiteral_strategy)
@settings(max_examples=50)
def test_ocl::ir::efenumliteral_instantiation(instance):
    assert isinstance(instance, ocl::ir::EFEnumLiteral)

@given(instance=ocl::ir::MetaTypeRef_strategy)
@settings(max_examples=50)
def test_ocl::ir::metatyperef_instantiation(instance):
    assert isinstance(instance, ocl::ir::MetaTypeRef)

@given(instance=ir::ocl::TuplePart_strategy)
@settings(max_examples=50)
def test_ir::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, ir::ocl::TuplePart)

@given(instance=ir::ocl::TuplePart_strategy)
def test_ir::ocl::tuplepart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ocl::TuplePart_strategy)
def test_ir::ocl::tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=ocl::ir::EFTupleType_strategy)
@settings(max_examples=50)
def test_ocl::ir::eftupletype_instantiation(instance):
    assert isinstance(instance, ocl::ir::EFTupleType)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ir::ocl::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::IntegerLiteralExp)

@given(instance=ir::ocl::IntegerLiteralExp_strategy)
def test_ir::ocl::integerliteralexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::ocl::IntegerLiteralExp_strategy)
def test_ir::ocl::integerliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::ocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::EnumLiteralExp)

@given(instance=ir::ocl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::StringLiteralExp)

@given(instance=ir::ocl::StringLiteralExp_strategy)
def test_ir::ocl::stringliteralexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::ocl::StringLiteralExp_strategy)
def test_ir::ocl::stringliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::ocl::OclInvalid_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclinvalid_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclInvalid)

@given(instance=ir::ocl::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::RealLiteralExp)

@given(instance=ir::ocl::RealLiteralExp_strategy)
def test_ir::ocl::realliteralexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::ocl::RealLiteralExp_strategy)
def test_ir::ocl::realliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::ocl::OclUndefined_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclundefined_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclUndefined)

@given(instance=ir::ocl::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::CollectionLiteralExp)

@given(instance=ir::ocl::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::TupleLiteralExp)

@given(instance=ir::ocl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::BooleanLiteralExp)

@given(instance=ir::ocl::BooleanLiteralExp_strategy)
def test_ir::ocl::booleanliteralexp_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=ir::ocl::BooleanLiteralExp_strategy)
def test_ir::ocl::booleanliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=ir::ocl::IterateExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::IterateExp)

@given(instance=ir::ocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::IteratorExp)

@given(instance=ir::ocl::IteratorExp_strategy)
def test_ir::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ocl::IteratorExp_strategy)
def test_ir::ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=ocl::ir::PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_ocl::ir::propertyfeatureref_instantiation(instance):
    assert isinstance(instance, ocl::ir::PropertyFeatureRef)

@given(instance=ocl::ir::OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_ocl::ir::operationfeatureref_instantiation(instance):
    assert isinstance(instance, ocl::ir::OperationFeatureRef)

@given(instance=AbstractOperationCallExp_strategy)
@settings(max_examples=50)
def test_abstractoperationcallexp_instantiation(instance):
    assert isinstance(instance, AbstractOperationCallExp)

@given(instance=ir::ocl::CollectionCallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::collectioncallexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::CollectionCallExp)

@given(instance=ir::ocl::CollectionCallExp_strategy)
def test_ir::ocl::collectioncallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ocl::CollectionCallExp_strategy)
def test_ir::ocl::collectioncallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ocl::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::OperationCallExp)

@given(instance=ir::ocl::OperationCallExp_strategy)
def test_ir::ocl::operationcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ocl::OperationCallExp_strategy)
def test_ir::ocl::operationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=ir::ocl::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::OperatorCallExp)

@given(instance=ir::ocl::OperatorCallExp_strategy)
def test_ir::ocl::operatorcallexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ir::ocl::OperatorCallExp_strategy)
def test_ir::ocl::operatorcallexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir::ocl::LoopExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::LoopExp)

@given(instance=ir::ocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::PropertyCallExp)

@given(instance=ir::ocl::PropertyCallExp_strategy)
def test_ir::ocl::propertycallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ocl::PropertyCallExp_strategy)
def test_ir::ocl::propertycallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ocl::AbstractOperationCallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::abstractoperationcallexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::AbstractOperationCallExp)

@given(instance=ocl::ir::TypeRef_strategy)
@settings(max_examples=50)
def test_ocl::ir::typeref_instantiation(instance):
    assert isinstance(instance, ocl::ir::TypeRef)

@given(instance=ir::ocl::OclExpression_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclExpression)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=DerivedProperty_strategy)
@settings(max_examples=50)
def test_derivedproperty_instantiation(instance):
    assert isinstance(instance, DerivedProperty)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=ir::ocl::UnsupportedExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::unsupportedexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::UnsupportedExp)

@given(instance=ir::ocl::UnsupportedExp_strategy)
def test_ir::ocl::unsupportedexp_reason_type(instance):
    assert isinstance(instance.reason, str)


@given(instance=ir::ocl::UnsupportedExp_strategy)
def test_ir::ocl::unsupportedexp_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=ir::ocl::UnsupportedExp_strategy)
def test_ir::ocl::unsupportedexp_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ir::ocl::UnsupportedExp_strategy)
def test_ir::ocl::unsupportedexp_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ir::ocl::CallExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::callexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::CallExp)

@given(instance=ir::ocl::LiteralExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::literalexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::LiteralExp)

@given(instance=ir::ocl::LetExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::letexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::LetExp)

@given(instance=ir::ocl::ModelElement_strategy)
@settings(max_examples=50)
def test_ir::ocl::modelelement_instantiation(instance):
    assert isinstance(instance, ir::ocl::ModelElement)

@given(instance=ir::ocl::IfExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::IfExp)

@given(instance=ir::ocl::VarExp_strategy)
@settings(max_examples=50)
def test_ir::ocl::varexp_instantiation(instance):
    assert isinstance(instance, ir::ocl::VarExp)

@given(instance=ocl::ir::EFClass_strategy)
@settings(max_examples=50)
def test_ocl::ir::efclass_instantiation(instance):
    assert isinstance(instance, ocl::ir::EFClass)

@given(instance=ocl::WithContextVariable_strategy)
@settings(max_examples=50)
def test_ocl::withcontextvariable_instantiation(instance):
    assert isinstance(instance, ocl::WithContextVariable)

@given(instance=ir::ocl::OclDerivedProperty_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclderivedproperty_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclDerivedProperty)

@given(instance=ir::ocl::OclOperation_strategy)
@settings(max_examples=50)
def test_ir::ocl::ocloperation_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclOperation)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=ir::ocl::OclInvariant_strategy)
@settings(max_examples=50)
def test_ir::ocl::oclinvariant_instantiation(instance):
    assert isinstance(instance, ir::ocl::OclInvariant)

@given(instance=ocl::ir::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ocl::ir::variabledeclaration_instantiation(instance):
    assert isinstance(instance, ocl::ir::VariableDeclaration)

@given(instance=ir::ocl::WithContextVariable_strategy)
@settings(max_examples=50)
def test_ir::ocl::withcontextvariable_instantiation(instance):
    assert isinstance(instance, ir::ocl::WithContextVariable)

@given(instance=CollectionTypeRef_strategy)
@settings(max_examples=50)
def test_collectiontyperef_instantiation(instance):
    assert isinstance(instance, CollectionTypeRef)

@given(instance=ir::OrderedSetTypeRef_strategy)
@settings(max_examples=50)
def test_ir::orderedsettyperef_instantiation(instance):
    assert isinstance(instance, ir::OrderedSetTypeRef)

@given(instance=ir::SequenceTypeRef_strategy)
@settings(max_examples=50)
def test_ir::sequencetyperef_instantiation(instance):
    assert isinstance(instance, ir::SequenceTypeRef)

@given(instance=ir::BagTypeRef_strategy)
@settings(max_examples=50)
def test_ir::bagtyperef_instantiation(instance):
    assert isinstance(instance, ir::BagTypeRef)

@given(instance=ir::SetTypeRef_strategy)
@settings(max_examples=50)
def test_ir::settyperef_instantiation(instance):
    assert isinstance(instance, ir::SetTypeRef)

@given(instance=TypeRef_strategy)
@settings(max_examples=50)
def test_typeref_instantiation(instance):
    assert isinstance(instance, TypeRef)

@given(instance=ir::InvalidTypeRef_strategy)
@settings(max_examples=50)
def test_ir::invalidtyperef_instantiation(instance):
    assert isinstance(instance, ir::InvalidTypeRef)

@given(instance=ir::CollectionTypeRef_strategy)
@settings(max_examples=50)
def test_ir::collectiontyperef_instantiation(instance):
    assert isinstance(instance, ir::CollectionTypeRef)

@given(instance=ir::MetaTypeRef_strategy)
@settings(max_examples=50)
def test_ir::metatyperef_instantiation(instance):
    assert isinstance(instance, ir::MetaTypeRef)

@given(instance=ir::TupleTypeElement_strategy)
@settings(max_examples=50)
def test_ir::tupletypeelement_instantiation(instance):
    assert isinstance(instance, ir::TupleTypeElement)

@given(instance=ir::TupleTypeElement_strategy)
def test_ir::tupletypeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TupleTypeElement_strategy)
def test_ir::tupletypeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::EFEnumLiteral_strategy)
@settings(max_examples=50)
def test_ir::efenumliteral_instantiation(instance):
    assert isinstance(instance, ir::EFEnumLiteral)

@given(instance=ir::EFEnumLiteral_strategy)
def test_ir::efenumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::EFEnumLiteral_strategy)
def test_ir::efenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::EEnum_strategy)
@settings(max_examples=50)
def test_ir::eenum_instantiation(instance):
    assert isinstance(instance, ir::EEnum)

@given(instance=ir::EClass_strategy)
@settings(max_examples=50)
def test_ir::eclass_instantiation(instance):
    assert isinstance(instance, ir::EClass)

@given(instance=EFType_strategy)
@settings(max_examples=50)
def test_eftype_instantiation(instance):
    assert isinstance(instance, EFType)

@given(instance=ir::EFEnum_strategy)
@settings(max_examples=50)
def test_ir::efenum_instantiation(instance):
    assert isinstance(instance, ir::EFEnum)

@given(instance=ir::EPackage_strategy)
@settings(max_examples=50)
def test_ir::epackage_instantiation(instance):
    assert isinstance(instance, ir::EPackage)

@given(instance=ir::EFPackage_strategy)
@settings(max_examples=50)
def test_ir::efpackage_instantiation(instance):
    assert isinstance(instance, ir::EFPackage)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ir::ocl::Iterator_strategy)
@settings(max_examples=50)
def test_ir::ocl::iterator_instantiation(instance):
    assert isinstance(instance, ir::ocl::Iterator)

@given(instance=ir::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ir::variabledeclaration_instantiation(instance):
    assert isinstance(instance, ir::VariableDeclaration)

@given(instance=ir::VariableDeclaration_strategy)
def test_ir::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::VariableDeclaration_strategy)
def test_ir::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ir::estructuralfeature_instantiation(instance):
    assert isinstance(instance, ir::EStructuralFeature)

@given(instance=PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_propertyfeatureref_instantiation(instance):
    assert isinstance(instance, PropertyFeatureRef)

@given(instance=ir::BuiltinPropertyRef_strategy)
@settings(max_examples=50)
def test_ir::builtinpropertyref_instantiation(instance):
    assert isinstance(instance, ir::BuiltinPropertyRef)

@given(instance=ir::DerivedPropertyRef_strategy)
@settings(max_examples=50)
def test_ir::derivedpropertyref_instantiation(instance):
    assert isinstance(instance, ir::DerivedPropertyRef)

@given(instance=ir::MetamodelFeatureRef_strategy)
@settings(max_examples=50)
def test_ir::metamodelfeatureref_instantiation(instance):
    assert isinstance(instance, ir::MetamodelFeatureRef)

@given(instance=ir::TupleFieldRef_strategy)
@settings(max_examples=50)
def test_ir::tuplefieldref_instantiation(instance):
    assert isinstance(instance, ir::TupleFieldRef)

@given(instance=ir::TupleFieldRef_strategy)
def test_ir::tuplefieldref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TupleFieldRef_strategy)
def test_ir::tuplefieldref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_operationfeatureref_instantiation(instance):
    assert isinstance(instance, OperationFeatureRef)

@given(instance=ir::DefinedOperationRef_strategy)
@settings(max_examples=50)
def test_ir::definedoperationref_instantiation(instance):
    assert isinstance(instance, ir::DefinedOperationRef)

@given(instance=ir::BuiltinOperationRef_strategy)
@settings(max_examples=50)
def test_ir::builtinoperationref_instantiation(instance):
    assert isinstance(instance, ir::BuiltinOperationRef)

@given(instance=ir::EFClass_strategy)
@settings(max_examples=50)
def test_ir::efclass_instantiation(instance):
    assert isinstance(instance, ir::EFClass)

@given(instance=FeatureRef_strategy)
@settings(max_examples=50)
def test_featureref_instantiation(instance):
    assert isinstance(instance, FeatureRef)

@given(instance=ir::PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_ir::propertyfeatureref_instantiation(instance):
    assert isinstance(instance, ir::PropertyFeatureRef)

@given(instance=ir::OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_ir::operationfeatureref_instantiation(instance):
    assert isinstance(instance, ir::OperationFeatureRef)

@given(instance=ir::FeatureRef_strategy)
@settings(max_examples=50)
def test_ir::featureref_instantiation(instance):
    assert isinstance(instance, ir::FeatureRef)

@given(instance=ir::Constraint_strategy)
@settings(max_examples=50)
def test_ir::constraint_instantiation(instance):
    assert isinstance(instance, ir::Constraint)

@given(instance=ir::Constraint_strategy)
def test_ir::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Constraint_strategy)
def test_ir::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Parameter_strategy)
@settings(max_examples=50)
def test_ir::parameter_instantiation(instance):
    assert isinstance(instance, ir::Parameter)

@given(instance=ir::EFMetamodel_strategy)
@settings(max_examples=50)
def test_ir::efmetamodel_instantiation(instance):
    assert isinstance(instance, ir::EFMetamodel)

@given(instance=AbstractFunction_strategy)
@settings(max_examples=50)
def test_abstractfunction_instantiation(instance):
    assert isinstance(instance, AbstractFunction)

@given(instance=ir::DerivedProperty_strategy)
@settings(max_examples=50)
def test_ir::derivedproperty_instantiation(instance):
    assert isinstance(instance, ir::DerivedProperty)

@given(instance=ir::Specification_strategy)
@settings(max_examples=50)
def test_ir::specification_instantiation(instance):
    assert isinstance(instance, ir::Specification)

@given(instance=ir::EFType_strategy)
@settings(max_examples=50)
def test_ir::eftype_instantiation(instance):
    assert isinstance(instance, ir::EFType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ir::AbstractFunction_strategy)
@settings(max_examples=50)
def test_ir::abstractfunction_instantiation(instance):
    assert isinstance(instance, ir::AbstractFunction)

@given(instance=ir::AbstractFunction_strategy)
def test_ir::abstractfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::AbstractFunction_strategy)
def test_ir::abstractfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::TypeRef_strategy)
@settings(max_examples=50)
def test_ir::typeref_instantiation(instance):
    assert isinstance(instance, ir::TypeRef)

@given(instance=ir::TypedElement_strategy)
@settings(max_examples=50)
def test_ir::typedelement_instantiation(instance):
    assert isinstance(instance, ir::TypedElement)

@given(instance=ir::EFTupleType_strategy)
@settings(max_examples=50)
def test_ir::eftupletype_instantiation(instance):
    assert isinstance(instance, ir::EFTupleType)

@given(instance=ir::EFTupleType_strategy)
def test_ir::eftupletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ir::EFTupleType_strategy)
def test_ir::eftupletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ir::EFPrimitiveType_strategy)
@settings(max_examples=50)
def test_ir::efprimitivetype_instantiation(instance):
    assert isinstance(instance, ir::EFPrimitiveType)

@given(instance=ir::EFPrimitiveType_strategy)
def test_ir::efprimitivetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::EFPrimitiveType_strategy)
def test_ir::efprimitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Operation_strategy)
@settings(max_examples=50)
def test_ir::operation_instantiation(instance):
    assert isinstance(instance, ir::Operation)
