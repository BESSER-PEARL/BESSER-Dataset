import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclModelElement,
    Parameter,
    OclFeatureDefinition,
    OclFeature,
    OCL::Attribute,
    OCL::Operation,
    OclModel,
    TupleType,
    NumericType,
    OCL::RealType,
    OCL::IntegerType,
    Primitive,
    OCL::BooleanType,
    OCL::NumericType,
    OCL::StringType,
    TupleTypeAttribute,
    CollectionType,
    OCL::OrderedSetType,
    OCL::SequenceType,
    OCL::BagType,
    OCL::SetType,
    MapType,
    OclContextDefinition,
    VariableExp,
    IterateExp,
    Iterator,
    MapExp,
    MapElement,
    TupleExp,
    TuplePart,
    NumericExp,
    OCL::IntegerExp,
    OCL::RealExp,
    PrimitiveExp,
    OCL::NumericExp,
    OCL::BooleanExp,
    OCL::StringExp,
    Attribute,
    Operation,
    OperationCallExp,
    OCL::OperatorCallExp,
    OCL::CollectionOperationCallExp,
    LoopExp,
    OCL::IterateExp,
    OCL::IteratorExp,
    LetExp,
    CollectionExp,
    OCL::SequenceExp,
    OCL::OrderedSetExp,
    OCL::BagExp,
    OCL::SetExp,
    PropertyCallExp,
    OCL::NavigationOrAttributeCallExp,
    OCL::LoopExp,
    OCL::OperationCallExp,
    IfExp,
    OclType,
    OCL::CollectionType,
    OCL::Primitive,
    OCL::MapType,
    OCL::OclModelElement,
    OCL::OclAnyType,
    OCL::TupleType,
    ocl::constraints::LocatedElement,
    OclExpression,
    OCL::PropertyCallExp,
    OCL::MapExp,
    OCL::LetExp,
    OCL::OclType,
    OCL::EnumLiteralExp,
    OCL::TupleExp,
    OCL::CollectionExp,
    OCL::PrimitiveExp,
    OCL::SuperExp,
    OCL::VariableExp,
    OCL::OclUndefinedExp,
    OCL::IfExp,
    OclPrecondition,
    OclInvariant,
    OclConstraintsModel,
    Metaclass,
    ocl::constraints::UMLClass,
    VariableDeclaration,
    OCL::Iterator,
    OCL::TuplePart,
    OCL::Parameter,
    Context,
    LocatedElement,
    OCL::MapElement,
    OCL::OclModel,
    OCL::TupleTypeAttribute,
    OCL::OclFeatureDefinition,
    OCL::OclExpression,
    ocl::constraints::Context,
    ocl::constraints::OclPrecondition,
    OCL::OclContextDefinition,
    ocl::constraints::Metaclass,
    ocl::constraints::OclInvariant,
    OCL::OclFeature,
    OCL::VariableDeclaration,
    ocl::constraints::OclConstraintsModel,
    UMLClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(OCL::Attribute)


def test_ocl::attribute_constructor_exists():
    assert callable(OCL::Attribute.__init__)


def test_ocl::attribute_constructor_args():
    sig = inspect.signature(OCL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::attribute_has_name():
    assert hasattr(OCL::Attribute, "name")
    descriptor = None
    for klass in OCL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::operation_is_not_abstract():
    assert not inspect.isabstract(OCL::Operation)


def test_ocl::operation_constructor_exists():
    assert callable(OCL::Operation.__init__)


def test_ocl::operation_constructor_args():
    sig = inspect.signature(OCL::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::operation_has_name():
    assert hasattr(OCL::Operation, "name")
    descriptor = None
    for klass in OCL::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
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



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL::BooleanType)


def test_ocl::booleantype_constructor_exists():
    assert callable(OCL::BooleanType.__init__)


def test_ocl::booleantype_constructor_args():
    sig = inspect.signature(OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(OCL::NumericType)


def test_ocl::numerictype_constructor_exists():
    assert callable(OCL::NumericType.__init__)


def test_ocl::numerictype_constructor_args():
    sig = inspect.signature(OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(OCL::StringType)


def test_ocl::stringtype_constructor_exists():
    assert callable(OCL::StringType.__init__)


def test_ocl::stringtype_constructor_args():
    sig = inspect.signature(OCL::StringType.__init__)
    params = list(sig.parameters.keys())



def test_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(TupleTypeAttribute)


def test_tupletypeattribute_constructor_exists():
    assert callable(TupleTypeAttribute.__init__)


def test_tupletypeattribute_constructor_args():
    sig = inspect.signature(TupleTypeAttribute.__init__)
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



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_iterateexp_is_not_abstract():
    assert not inspect.isabstract(IterateExp)


def test_iterateexp_constructor_exists():
    assert callable(IterateExp.__init__)


def test_iterateexp_constructor_args():
    sig = inspect.signature(IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IntegerExp)


def test_ocl::integerexp_constructor_exists():
    assert callable(OCL::IntegerExp.__init__)


def test_ocl::integerexp_constructor_args():
    sig = inspect.signature(OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl::integerexp_has_integerSymbol():
    assert hasattr(OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(OCL::RealExp)


def test_ocl::realexp_constructor_exists():
    assert callable(OCL::RealExp.__init__)


def test_ocl::realexp_constructor_args():
    sig = inspect.signature(OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl::realexp_has_realSymbol():
    assert hasattr(OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in OCL::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(OCL::NumericExp)


def test_ocl::numericexp_constructor_exists():
    assert callable(OCL::NumericExp.__init__)


def test_ocl::numericexp_constructor_args():
    sig = inspect.signature(OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(OCL::BooleanExp)


def test_ocl::booleanexp_constructor_exists():
    assert callable(OCL::BooleanExp.__init__)


def test_ocl::booleanexp_constructor_args():
    sig = inspect.signature(OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl::booleanexp_has_booleanSymbol():
    assert hasattr(OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(OCL::StringExp)


def test_ocl::stringexp_constructor_exists():
    assert callable(OCL::StringExp.__init__)


def test_ocl::stringexp_constructor_args():
    sig = inspect.signature(OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl::stringexp_has_stringSymbol():
    assert hasattr(OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in OCL::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



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



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IterateExp)


def test_ocl::iterateexp_constructor_exists():
    assert callable(OCL::IterateExp.__init__)


def test_ocl::iterateexp_constructor_args():
    sig = inspect.signature(OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IteratorExp)


def test_ocl::iteratorexp_constructor_exists():
    assert callable(OCL::IteratorExp.__init__)


def test_ocl::iteratorexp_constructor_args():
    sig = inspect.signature(OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::iteratorexp_has_name():
    assert hasattr(OCL::IteratorExp, "name")
    descriptor = None
    for klass in OCL::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SequenceExp)


def test_ocl::sequenceexp_constructor_exists():
    assert callable(OCL::SequenceExp.__init__)


def test_ocl::sequenceexp_constructor_args():
    sig = inspect.signature(OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OrderedSetExp)


def test_ocl::orderedsetexp_constructor_exists():
    assert callable(OCL::OrderedSetExp.__init__)


def test_ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(OCL::BagExp)


def test_ocl::bagexp_constructor_exists():
    assert callable(OCL::BagExp.__init__)


def test_ocl::bagexp_constructor_args():
    sig = inspect.signature(OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SetExp)


def test_ocl::setexp_constructor_exists():
    assert callable(OCL::SetExp.__init__)


def test_ocl::setexp_constructor_args():
    sig = inspect.signature(OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::NavigationOrAttributeCallExp)


def test_ocl::navigationorattributecallexp_constructor_exists():
    assert callable(OCL::NavigationOrAttributeCallExp.__init__)


def test_ocl::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(OCL::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::navigationorattributecallexp_has_name():
    assert hasattr(OCL::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in OCL::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LoopExp)


def test_ocl::loopexp_constructor_exists():
    assert callable(OCL::LoopExp.__init__)


def test_ocl::loopexp_constructor_args():
    sig = inspect.signature(OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OperationCallExp)


def test_ocl::operationcallexp_constructor_exists():
    assert callable(OCL::OperationCallExp.__init__)


def test_ocl::operationcallexp_constructor_args():
    sig = inspect.signature(OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_ocl::operationcallexp_has_operationName():
    assert hasattr(OCL::OperationCallExp, "operationName")
    descriptor = None
    for klass in OCL::OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_ifexp_is_not_abstract():
    assert not inspect.isabstract(IfExp)


def test_ifexp_constructor_exists():
    assert callable(IfExp.__init__)


def test_ifexp_constructor_args():
    sig = inspect.signature(IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionType)


def test_ocl::collectiontype_constructor_exists():
    assert callable(OCL::CollectionType.__init__)


def test_ocl::collectiontype_constructor_args():
    sig = inspect.signature(OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(OCL::Primitive)


def test_ocl::primitive_constructor_exists():
    assert callable(OCL::Primitive.__init__)


def test_ocl::primitive_constructor_args():
    sig = inspect.signature(OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(OCL::MapType)


def test_ocl::maptype_constructor_exists():
    assert callable(OCL::MapType.__init__)


def test_ocl::maptype_constructor_args():
    sig = inspect.signature(OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OCL::OclModelElement)


def test_ocl::oclmodelelement_constructor_exists():
    assert callable(OCL::OclModelElement.__init__)


def test_ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(OCL::OclAnyType)


def test_ocl::oclanytype_constructor_exists():
    assert callable(OCL::OclAnyType.__init__)


def test_ocl::oclanytype_constructor_args():
    sig = inspect.signature(OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleType)


def test_ocl::tupletype_constructor_exists():
    assert callable(OCL::TupleType.__init__)


def test_ocl::tupletype_constructor_args():
    sig = inspect.signature(OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::constraints::locatedelement_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::LocatedElement)


def test_ocl::constraints::locatedelement_constructor_exists():
    assert callable(ocl::constraints::LocatedElement.__init__)


def test_ocl::constraints::locatedelement_constructor_args():
    sig = inspect.signature(ocl::constraints::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_ocl::constraints::locatedelement_has_commentsAfter():
    assert hasattr(ocl::constraints::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in ocl::constraints::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_ocl::constraints::locatedelement_has_commentsBefore():
    assert hasattr(ocl::constraints::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in ocl::constraints::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_ocl::constraints::locatedelement_has_location():
    assert hasattr(ocl::constraints::LocatedElement, "location")
    descriptor = None
    for klass in ocl::constraints::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::PropertyCallExp)


def test_ocl::propertycallexp_constructor_exists():
    assert callable(OCL::PropertyCallExp.__init__)


def test_ocl::propertycallexp_constructor_args():
    sig = inspect.signature(OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(OCL::MapExp)


def test_ocl::mapexp_constructor_exists():
    assert callable(OCL::MapExp.__init__)


def test_ocl::mapexp_constructor_args():
    sig = inspect.signature(OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LetExp)


def test_ocl::letexp_constructor_exists():
    assert callable(OCL::LetExp.__init__)


def test_ocl::letexp_constructor_args():
    sig = inspect.signature(OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(OCL::OclType)


def test_ocl::ocltype_constructor_exists():
    assert callable(OCL::OclType.__init__)


def test_ocl::ocltype_constructor_args():
    sig = inspect.signature(OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::ocltype_has_name():
    assert hasattr(OCL::OclType, "name")
    descriptor = None
    for klass in OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL::EnumLiteralExp)


def test_ocl::enumliteralexp_constructor_exists():
    assert callable(OCL::EnumLiteralExp.__init__)


def test_ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::enumliteralexp_has_name():
    assert hasattr(OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleExp)


def test_ocl::tupleexp_constructor_exists():
    assert callable(OCL::TupleExp.__init__)


def test_ocl::tupleexp_constructor_args():
    sig = inspect.signature(OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionExp)


def test_ocl::collectionexp_constructor_exists():
    assert callable(OCL::CollectionExp.__init__)


def test_ocl::collectionexp_constructor_args():
    sig = inspect.signature(OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(OCL::PrimitiveExp)


def test_ocl::primitiveexp_constructor_exists():
    assert callable(OCL::PrimitiveExp.__init__)


def test_ocl::primitiveexp_constructor_args():
    sig = inspect.signature(OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SuperExp)


def test_ocl::superexp_constructor_exists():
    assert callable(OCL::SuperExp.__init__)


def test_ocl::superexp_constructor_args():
    sig = inspect.signature(OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(OCL::VariableExp)


def test_ocl::variableexp_constructor_exists():
    assert callable(OCL::VariableExp.__init__)


def test_ocl::variableexp_constructor_args():
    sig = inspect.signature(OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OclUndefinedExp)


def test_ocl::oclundefinedexp_constructor_exists():
    assert callable(OCL::OclUndefinedExp.__init__)


def test_ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IfExp)


def test_ocl::ifexp_constructor_exists():
    assert callable(OCL::IfExp.__init__)


def test_ocl::ifexp_constructor_args():
    sig = inspect.signature(OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_oclprecondition_is_not_abstract():
    assert not inspect.isabstract(OclPrecondition)


def test_oclprecondition_constructor_exists():
    assert callable(OclPrecondition.__init__)


def test_oclprecondition_constructor_args():
    sig = inspect.signature(OclPrecondition.__init__)
    params = list(sig.parameters.keys())



def test_oclinvariant_is_not_abstract():
    assert not inspect.isabstract(OclInvariant)


def test_oclinvariant_constructor_exists():
    assert callable(OclInvariant.__init__)


def test_oclinvariant_constructor_args():
    sig = inspect.signature(OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_oclconstraintsmodel_is_not_abstract():
    assert not inspect.isabstract(OclConstraintsModel)


def test_oclconstraintsmodel_constructor_exists():
    assert callable(OclConstraintsModel.__init__)


def test_oclconstraintsmodel_constructor_args():
    sig = inspect.signature(OclConstraintsModel.__init__)
    params = list(sig.parameters.keys())



def test_metaclass_is_not_abstract():
    assert not inspect.isabstract(Metaclass)


def test_metaclass_constructor_exists():
    assert callable(Metaclass.__init__)


def test_metaclass_constructor_args():
    sig = inspect.signature(Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::constraints::umlclass_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::UMLClass)


def test_ocl::constraints::umlclass_constructor_exists():
    assert callable(ocl::constraints::UMLClass.__init__)


def test_ocl::constraints::umlclass_constructor_args():
    sig = inspect.signature(ocl::constraints::UMLClass.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(OCL::Iterator)


def test_ocl::iterator_constructor_exists():
    assert callable(OCL::Iterator.__init__)


def test_ocl::iterator_constructor_args():
    sig = inspect.signature(OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(OCL::TuplePart)


def test_ocl::tuplepart_constructor_exists():
    assert callable(OCL::TuplePart.__init__)


def test_ocl::tuplepart_constructor_args():
    sig = inspect.signature(OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(OCL::Parameter)


def test_ocl::parameter_constructor_exists():
    assert callable(OCL::Parameter.__init__)


def test_ocl::parameter_constructor_args():
    sig = inspect.signature(OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(OCL::MapElement)


def test_ocl::mapelement_constructor_exists():
    assert callable(OCL::MapElement.__init__)


def test_ocl::mapelement_constructor_args():
    sig = inspect.signature(OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(OCL::OclModel)


def test_ocl::oclmodel_constructor_exists():
    assert callable(OCL::OclModel.__init__)


def test_ocl::oclmodel_constructor_args():
    sig = inspect.signature(OCL::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::oclmodel_has_name():
    assert hasattr(OCL::OclModel, "name")
    descriptor = None
    for klass in OCL::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleTypeAttribute)


def test_ocl::tupletypeattribute_constructor_exists():
    assert callable(OCL::TupleTypeAttribute.__init__)


def test_ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::tupletypeattribute_has_name():
    assert hasattr(OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OCL::OclFeatureDefinition)


def test_ocl::oclfeaturedefinition_constructor_exists():
    assert callable(OCL::OclFeatureDefinition.__init__)


def test_ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL::OclExpression)


def test_ocl::oclexpression_constructor_exists():
    assert callable(OCL::OclExpression.__init__)


def test_ocl::oclexpression_constructor_args():
    sig = inspect.signature(OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::constraints::context_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::Context)


def test_ocl::constraints::context_constructor_exists():
    assert callable(ocl::constraints::Context.__init__)


def test_ocl::constraints::context_constructor_args():
    sig = inspect.signature(ocl::constraints::Context.__init__)
    params = list(sig.parameters.keys())



def test_ocl::constraints::oclprecondition_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::OclPrecondition)


def test_ocl::constraints::oclprecondition_constructor_exists():
    assert callable(ocl::constraints::OclPrecondition.__init__)


def test_ocl::constraints::oclprecondition_constructor_args():
    sig = inspect.signature(ocl::constraints::OclPrecondition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::constraints::oclprecondition_has_description():
    assert hasattr(ocl::constraints::OclPrecondition, "description")
    descriptor = None
    for klass in ocl::constraints::OclPrecondition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ocl::constraints::oclprecondition_has_name():
    assert hasattr(ocl::constraints::OclPrecondition, "name")
    descriptor = None
    for klass in ocl::constraints::OclPrecondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL::OclContextDefinition)


def test_ocl::oclcontextdefinition_constructor_exists():
    assert callable(OCL::OclContextDefinition.__init__)


def test_ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl::constraints::metaclass_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::Metaclass)


def test_ocl::constraints::metaclass_constructor_exists():
    assert callable(ocl::constraints::Metaclass.__init__)


def test_ocl::constraints::metaclass_constructor_args():
    sig = inspect.signature(ocl::constraints::Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl::constraints::metaclass_has_name():
    assert hasattr(ocl::constraints::Metaclass, "name")
    descriptor = None
    for klass in ocl::constraints::Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl::constraints::oclinvariant_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::OclInvariant)


def test_ocl::constraints::oclinvariant_constructor_exists():
    assert callable(ocl::constraints::OclInvariant.__init__)


def test_ocl::constraints::oclinvariant_constructor_args():
    sig = inspect.signature(ocl::constraints::OclInvariant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_ocl::constraints::oclinvariant_has_name():
    assert hasattr(ocl::constraints::OclInvariant, "name")
    descriptor = None
    for klass in ocl::constraints::OclInvariant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocl::constraints::oclinvariant_has_description():
    assert hasattr(ocl::constraints::OclInvariant, "description")
    descriptor = None
    for klass in ocl::constraints::OclInvariant.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL::OclFeature)


def test_ocl::oclfeature_constructor_exists():
    assert callable(OCL::OclFeature.__init__)


def test_ocl::oclfeature_constructor_args():
    sig = inspect.signature(OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(OCL::VariableDeclaration)


def test_ocl::variabledeclaration_constructor_exists():
    assert callable(OCL::VariableDeclaration.__init__)


def test_ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_ocl::variabledeclaration_has_id():
    assert hasattr(OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ocl::variabledeclaration_has_varName():
    assert hasattr(OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_ocl::constraints::oclconstraintsmodel_is_not_abstract():
    assert not inspect.isabstract(ocl::constraints::OclConstraintsModel)


def test_ocl::constraints::oclconstraintsmodel_constructor_exists():
    assert callable(ocl::constraints::OclConstraintsModel.__init__)


def test_ocl::constraints::oclconstraintsmodel_constructor_args():
    sig = inspect.signature(ocl::constraints::OclConstraintsModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_ocl::constraints::oclconstraintsmodel_has_name():
    assert hasattr(ocl::constraints::OclConstraintsModel, "name")
    descriptor = None
    for klass in ocl::constraints::OclConstraintsModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocl::constraints::oclconstraintsmodel_has_metamodel():
    assert hasattr(ocl::constraints::OclConstraintsModel, "metamodel")
    descriptor = None
    for klass in ocl::constraints::OclConstraintsModel.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_umlclass_is_not_abstract():
    assert not inspect.isabstract(UMLClass)


def test_umlclass_constructor_exists():
    assert callable(UMLClass.__init__)


def test_umlclass_constructor_args():
    sig = inspect.signature(UMLClass.__init__)
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
OclModelElement_strategy = st.builds(
    OclModelElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL::Attribute_strategy = st.builds(
    OCL::Attribute,
    name=
        safe_text
)
OCL::Operation_strategy = st.builds(
    OCL::Operation,
    name=
        safe_text
)
OclModel_strategy = st.builds(
    OclModel,
)
TupleType_strategy = st.builds(
    TupleType,
)
NumericType_strategy = st.builds(
    NumericType,
)
OCL::RealType_strategy = st.builds(
    OCL::RealType,
)
OCL::IntegerType_strategy = st.builds(
    OCL::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
OCL::BooleanType_strategy = st.builds(
    OCL::BooleanType,
)
OCL::NumericType_strategy = st.builds(
    OCL::NumericType,
)
OCL::StringType_strategy = st.builds(
    OCL::StringType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
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
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
OCL::IntegerExp_strategy = st.builds(
    OCL::IntegerExp,
    integerSymbol=
        safe_text
)
OCL::RealExp_strategy = st.builds(
    OCL::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
OCL::NumericExp_strategy = st.builds(
    OCL::NumericExp,
)
OCL::BooleanExp_strategy = st.builds(
    OCL::BooleanExp,
    booleanSymbol=
        safe_text
)
OCL::StringExp_strategy = st.builds(
    OCL::StringExp,
    stringSymbol=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
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
LoopExp_strategy = st.builds(
    LoopExp,
)
OCL::IterateExp_strategy = st.builds(
    OCL::IterateExp,
)
OCL::IteratorExp_strategy = st.builds(
    OCL::IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
OCL::SequenceExp_strategy = st.builds(
    OCL::SequenceExp,
)
OCL::OrderedSetExp_strategy = st.builds(
    OCL::OrderedSetExp,
)
OCL::BagExp_strategy = st.builds(
    OCL::BagExp,
)
OCL::SetExp_strategy = st.builds(
    OCL::SetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
)
OCL::LoopExp_strategy = st.builds(
    OCL::LoopExp,
)
OCL::OperationCallExp_strategy = st.builds(
    OCL::OperationCallExp,
    operationName=
        safe_text
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
OCL::CollectionType_strategy = st.builds(
    OCL::CollectionType,
)
OCL::Primitive_strategy = st.builds(
    OCL::Primitive,
)
OCL::MapType_strategy = st.builds(
    OCL::MapType,
)
OCL::OclModelElement_strategy = st.builds(
    OCL::OclModelElement,
)
OCL::OclAnyType_strategy = st.builds(
    OCL::OclAnyType,
)
OCL::TupleType_strategy = st.builds(
    OCL::TupleType,
)
ocl::constraints::LocatedElement_strategy = st.builds(
    ocl::constraints::LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL::PropertyCallExp_strategy = st.builds(
    OCL::PropertyCallExp,
)
OCL::MapExp_strategy = st.builds(
    OCL::MapExp,
)
OCL::LetExp_strategy = st.builds(
    OCL::LetExp,
)
OCL::OclType_strategy = st.builds(
    OCL::OclType,
    name=
        safe_text
)
OCL::EnumLiteralExp_strategy = st.builds(
    OCL::EnumLiteralExp,
    name=
        safe_text
)
OCL::TupleExp_strategy = st.builds(
    OCL::TupleExp,
)
OCL::CollectionExp_strategy = st.builds(
    OCL::CollectionExp,
)
OCL::PrimitiveExp_strategy = st.builds(
    OCL::PrimitiveExp,
)
OCL::SuperExp_strategy = st.builds(
    OCL::SuperExp,
)
OCL::VariableExp_strategy = st.builds(
    OCL::VariableExp,
)
OCL::OclUndefinedExp_strategy = st.builds(
    OCL::OclUndefinedExp,
)
OCL::IfExp_strategy = st.builds(
    OCL::IfExp,
)
OclPrecondition_strategy = st.builds(
    OclPrecondition,
)
OclInvariant_strategy = st.builds(
    OclInvariant,
)
OclConstraintsModel_strategy = st.builds(
    OclConstraintsModel,
)
Metaclass_strategy = st.builds(
    Metaclass,
)
ocl::constraints::UMLClass_strategy = st.builds(
    ocl::constraints::UMLClass,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
OCL::Iterator_strategy = st.builds(
    OCL::Iterator,
)
OCL::TuplePart_strategy = st.builds(
    OCL::TuplePart,
)
OCL::Parameter_strategy = st.builds(
    OCL::Parameter,
)
Context_strategy = st.builds(
    Context,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
OCL::MapElement_strategy = st.builds(
    OCL::MapElement,
)
OCL::OclModel_strategy = st.builds(
    OCL::OclModel,
    name=
        safe_text
)
OCL::TupleTypeAttribute_strategy = st.builds(
    OCL::TupleTypeAttribute,
    name=
        safe_text
)
OCL::OclFeatureDefinition_strategy = st.builds(
    OCL::OclFeatureDefinition,
)
OCL::OclExpression_strategy = st.builds(
    OCL::OclExpression,
)
ocl::constraints::Context_strategy = st.builds(
    ocl::constraints::Context,
)
ocl::constraints::OclPrecondition_strategy = st.builds(
    ocl::constraints::OclPrecondition,
    description=
        safe_text,
    name=
        safe_text
)
OCL::OclContextDefinition_strategy = st.builds(
    OCL::OclContextDefinition,
)
ocl::constraints::Metaclass_strategy = st.builds(
    ocl::constraints::Metaclass,
    name=
        safe_text
)
ocl::constraints::OclInvariant_strategy = st.builds(
    ocl::constraints::OclInvariant,
    name=
        safe_text,
    description=
        safe_text
)
OCL::OclFeature_strategy = st.builds(
    OCL::OclFeature,
)
OCL::VariableDeclaration_strategy = st.builds(
    OCL::VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
ocl::constraints::OclConstraintsModel_strategy = st.builds(
    ocl::constraints::OclConstraintsModel,
    name=
        safe_text,
    metamodel=
        safe_text
)
UMLClass_strategy = st.builds(
    UMLClass,
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OCL::Attribute_strategy)
@settings(max_examples=50)
def test_ocl::attribute_instantiation(instance):
    assert isinstance(instance, OCL::Attribute)

@given(instance=OCL::Attribute_strategy)
def test_ocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::Attribute_strategy)
def test_ocl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::Operation_strategy)
@settings(max_examples=50)
def test_ocl::operation_instantiation(instance):
    assert isinstance(instance, OCL::Operation)

@given(instance=OCL::Operation_strategy)
def test_ocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::Operation_strategy)
def test_ocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OCL::RealType_strategy)
@settings(max_examples=50)
def test_ocl::realtype_instantiation(instance):
    assert isinstance(instance, OCL::RealType)

@given(instance=OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_ocl::integertype_instantiation(instance):
    assert isinstance(instance, OCL::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_ocl::booleantype_instantiation(instance):
    assert isinstance(instance, OCL::BooleanType)

@given(instance=OCL::NumericType_strategy)
@settings(max_examples=50)
def test_ocl::numerictype_instantiation(instance):
    assert isinstance(instance, OCL::NumericType)

@given(instance=OCL::StringType_strategy)
@settings(max_examples=50)
def test_ocl::stringtype_instantiation(instance):
    assert isinstance(instance, OCL::StringType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

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

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_ocl::integerexp_instantiation(instance):
    assert isinstance(instance, OCL::IntegerExp)

@given(instance=OCL::IntegerExp_strategy)
def test_ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=OCL::IntegerExp_strategy)
def test_ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OCL::RealExp_strategy)
@settings(max_examples=50)
def test_ocl::realexp_instantiation(instance):
    assert isinstance(instance, OCL::RealExp)

@given(instance=OCL::RealExp_strategy)
def test_ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=OCL::RealExp_strategy)
def test_ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_ocl::numericexp_instantiation(instance):
    assert isinstance(instance, OCL::NumericExp)

@given(instance=OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, OCL::BooleanExp)

@given(instance=OCL::BooleanExp_strategy)
def test_ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=OCL::BooleanExp_strategy)
def test_ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OCL::StringExp_strategy)
@settings(max_examples=50)
def test_ocl::stringexp_instantiation(instance):
    assert isinstance(instance, OCL::StringExp)

@given(instance=OCL::StringExp_strategy)
def test_ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=OCL::StringExp_strategy)
def test_ocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

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

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, OCL::IterateExp)

@given(instance=OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, OCL::IteratorExp)

@given(instance=OCL::IteratorExp_strategy)
def test_ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::IteratorExp_strategy)
def test_ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, OCL::SequenceExp)

@given(instance=OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, OCL::OrderedSetExp)

@given(instance=OCL::BagExp_strategy)
@settings(max_examples=50)
def test_ocl::bagexp_instantiation(instance):
    assert isinstance(instance, OCL::BagExp)

@given(instance=OCL::SetExp_strategy)
@settings(max_examples=50)
def test_ocl::setexp_instantiation(instance):
    assert isinstance(instance, OCL::SetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=OCL::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_ocl::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, OCL::NavigationOrAttributeCallExp)

@given(instance=OCL::NavigationOrAttributeCallExp_strategy)
def test_ocl::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::NavigationOrAttributeCallExp_strategy)
def test_ocl::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::loopexp_instantiation(instance):
    assert isinstance(instance, OCL::LoopExp)

@given(instance=OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, OCL::OperationCallExp)

@given(instance=OCL::OperationCallExp_strategy)
def test_ocl::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=OCL::OperationCallExp_strategy)
def test_ocl::operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, OCL::CollectionType)

@given(instance=OCL::Primitive_strategy)
@settings(max_examples=50)
def test_ocl::primitive_instantiation(instance):
    assert isinstance(instance, OCL::Primitive)

@given(instance=OCL::MapType_strategy)
@settings(max_examples=50)
def test_ocl::maptype_instantiation(instance):
    assert isinstance(instance, OCL::MapType)

@given(instance=OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, OCL::OclModelElement)

@given(instance=OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, OCL::OclAnyType)

@given(instance=OCL::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::tupletype_instantiation(instance):
    assert isinstance(instance, OCL::TupleType)

@given(instance=ocl::constraints::LocatedElement_strategy)
@settings(max_examples=50)
def test_ocl::constraints::locatedelement_instantiation(instance):
    assert isinstance(instance, ocl::constraints::LocatedElement)

@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=ocl::constraints::LocatedElement_strategy)
def test_ocl::constraints::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, OCL::PropertyCallExp)

@given(instance=OCL::MapExp_strategy)
@settings(max_examples=50)
def test_ocl::mapexp_instantiation(instance):
    assert isinstance(instance, OCL::MapExp)

@given(instance=OCL::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::letexp_instantiation(instance):
    assert isinstance(instance, OCL::LetExp)

@given(instance=OCL::OclType_strategy)
@settings(max_examples=50)
def test_ocl::ocltype_instantiation(instance):
    assert isinstance(instance, OCL::OclType)

@given(instance=OCL::OclType_strategy)
def test_ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::OclType_strategy)
def test_ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCL::EnumLiteralExp)

@given(instance=OCL::EnumLiteralExp_strategy)
def test_ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::EnumLiteralExp_strategy)
def test_ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, OCL::TupleExp)

@given(instance=OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, OCL::CollectionExp)

@given(instance=OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, OCL::PrimitiveExp)

@given(instance=OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_ocl::superexp_instantiation(instance):
    assert isinstance(instance, OCL::SuperExp)

@given(instance=OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::variableexp_instantiation(instance):
    assert isinstance(instance, OCL::VariableExp)

@given(instance=OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OCL::OclUndefinedExp)

@given(instance=OCL::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::ifexp_instantiation(instance):
    assert isinstance(instance, OCL::IfExp)

@given(instance=OclPrecondition_strategy)
@settings(max_examples=50)
def test_oclprecondition_instantiation(instance):
    assert isinstance(instance, OclPrecondition)

@given(instance=OclInvariant_strategy)
@settings(max_examples=50)
def test_oclinvariant_instantiation(instance):
    assert isinstance(instance, OclInvariant)

@given(instance=OclConstraintsModel_strategy)
@settings(max_examples=50)
def test_oclconstraintsmodel_instantiation(instance):
    assert isinstance(instance, OclConstraintsModel)

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=ocl::constraints::UMLClass_strategy)
@settings(max_examples=50)
def test_ocl::constraints::umlclass_instantiation(instance):
    assert isinstance(instance, ocl::constraints::UMLClass)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=OCL::Iterator_strategy)
@settings(max_examples=50)
def test_ocl::iterator_instantiation(instance):
    assert isinstance(instance, OCL::Iterator)

@given(instance=OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, OCL::TuplePart)

@given(instance=OCL::Parameter_strategy)
@settings(max_examples=50)
def test_ocl::parameter_instantiation(instance):
    assert isinstance(instance, OCL::Parameter)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=OCL::MapElement_strategy)
@settings(max_examples=50)
def test_ocl::mapelement_instantiation(instance):
    assert isinstance(instance, OCL::MapElement)

@given(instance=OCL::OclModel_strategy)
@settings(max_examples=50)
def test_ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, OCL::OclModel)

@given(instance=OCL::OclModel_strategy)
def test_ocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::OclModel_strategy)
def test_ocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, OCL::TupleTypeAttribute)

@given(instance=OCL::TupleTypeAttribute_strategy)
def test_ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OCL::TupleTypeAttribute_strategy)
def test_ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OCL::OclFeatureDefinition)

@given(instance=OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, OCL::OclExpression)

@given(instance=ocl::constraints::Context_strategy)
@settings(max_examples=50)
def test_ocl::constraints::context_instantiation(instance):
    assert isinstance(instance, ocl::constraints::Context)

@given(instance=ocl::constraints::OclPrecondition_strategy)
@settings(max_examples=50)
def test_ocl::constraints::oclprecondition_instantiation(instance):
    assert isinstance(instance, ocl::constraints::OclPrecondition)

@given(instance=ocl::constraints::OclPrecondition_strategy)
def test_ocl::constraints::oclprecondition_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ocl::constraints::OclPrecondition_strategy)
def test_ocl::constraints::oclprecondition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ocl::constraints::OclPrecondition_strategy)
def test_ocl::constraints::oclprecondition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::constraints::OclPrecondition_strategy)
def test_ocl::constraints::oclprecondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCL::OclContextDefinition)

@given(instance=ocl::constraints::Metaclass_strategy)
@settings(max_examples=50)
def test_ocl::constraints::metaclass_instantiation(instance):
    assert isinstance(instance, ocl::constraints::Metaclass)

@given(instance=ocl::constraints::Metaclass_strategy)
def test_ocl::constraints::metaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::constraints::Metaclass_strategy)
def test_ocl::constraints::metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl::constraints::OclInvariant_strategy)
@settings(max_examples=50)
def test_ocl::constraints::oclinvariant_instantiation(instance):
    assert isinstance(instance, ocl::constraints::OclInvariant)

@given(instance=ocl::constraints::OclInvariant_strategy)
def test_ocl::constraints::oclinvariant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::constraints::OclInvariant_strategy)
def test_ocl::constraints::oclinvariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl::constraints::OclInvariant_strategy)
def test_ocl::constraints::oclinvariant_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ocl::constraints::OclInvariant_strategy)
def test_ocl::constraints::oclinvariant_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, OCL::OclFeature)

@given(instance=OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, OCL::VariableDeclaration)

@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=ocl::constraints::OclConstraintsModel_strategy)
@settings(max_examples=50)
def test_ocl::constraints::oclconstraintsmodel_instantiation(instance):
    assert isinstance(instance, ocl::constraints::OclConstraintsModel)

@given(instance=ocl::constraints::OclConstraintsModel_strategy)
def test_ocl::constraints::oclconstraintsmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocl::constraints::OclConstraintsModel_strategy)
def test_ocl::constraints::oclconstraintsmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl::constraints::OclConstraintsModel_strategy)
def test_ocl::constraints::oclconstraintsmodel_metamodel_type(instance):
    assert isinstance(instance.metamodel, str)


@given(instance=ocl::constraints::OclConstraintsModel_strategy)
def test_ocl::constraints::oclconstraintsmodel_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=UMLClass_strategy)
@settings(max_examples=50)
def test_umlclass_instantiation(instance):
    assert isinstance(instance, UMLClass)
