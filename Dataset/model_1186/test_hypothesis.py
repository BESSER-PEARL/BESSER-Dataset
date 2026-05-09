import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclModelElement,
    TupleType,
    OclFeature,
    OCL::Operation,
    OCL::Attribute,
    Primitive,
    OCL::StringType,
    TupleTypeAttribute,
    CollectionType,
    OCL::SetType,
    OCL::SequenceType,
    OCL::OrderedSetType,
    OCL::BagType,
    NumericType,
    OCL::RealType,
    OCL::IntegerType,
    OCL::NumericType,
    OCL::BooleanType,
    VariableExp,
    IterateExp,
    MapType,
    OclContextDefinition,
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
    OCL::CollectionOperationCallExp,
    OCL::OperatorCallExp,
    LoopExp,
    OCL::IterateExp,
    OCL::IteratorExp,
    LetExp,
    CollectionExp,
    OCL::SetExp,
    OCL::OrderedSetExp,
    OCL::SequenceExp,
    OCL::BagExp,
    PropertyCallExp,
    OCL::LoopExp,
    OCL::NavigationOrAttributeCallExp,
    OCL::OperationCallExp,
    IfExp,
    OclType,
    OCL::OclAnyType,
    OCL::OclModelElement,
    OCL::MapType,
    OCL::CollectionType,
    OCL::TupleType,
    OCL::Primitive,
    Statement,
    ATL::BindingStat,
    ATL::ForStat,
    ATL::IfStat,
    ATL::ExpressionStat,
    Iterator,
    Binding,
    PatternElement,
    ATL::OutPatternElement,
    ATL::InPatternElement,
    VariableDeclaration,
    ATL::RuleVariableDeclaration,
    OCL::TuplePart,
    OCL::Parameter,
    OCL::Iterator,
    ATL::PatternElement,
    OutPatternElement,
    ATL::SimpleOutPatternElement,
    ATL::ForEachOutPatternElement,
    DropPattern,
    InPatternElement,
    ATL::SimpleInPatternElement,
    Parameter,
    MatchedRule,
    ATL::LazyMatchedRule,
    InPattern,
    Rule,
    ATL::CalledRule,
    ATL::MatchedRule,
    RuleVariableDeclaration,
    ActionBlock,
    OutPattern,
    OclFeatureDefinition,
    Library,
    Query,
    Module,
    ModuleElement,
    ATL::Rule,
    ATL::Helper,
    OclModel,
    OclExpression,
    OCL::PropertyCallExp,
    OCL::TupleExp,
    OCL::IfExp,
    OCL::LetExp,
    OCL::OclUndefinedExp,
    OCL::VariableExp,
    OCL::MapExp,
    OCL::OclType,
    OCL::SuperExp,
    OCL::PrimitiveExp,
    OCL::EnumLiteralExp,
    OCL::CollectionExp,
    Helper,
    Unit,
    ATL::Query,
    ATL::Module,
    ATL::Library,
    LibraryRef,
    LocatedElement,
    OCL::VariableDeclaration,
    ATL::Binding,
    ATL::Statement,
    ATL::ModuleElement,
    OCL::OclModel,
    OCL::OclExpression,
    OCL::OclContextDefinition,
    OCL::MapElement,
    ATL::DropPattern,
    OCL::TupleTypeAttribute,
    OCL::OclFeature,
    ATL::InPattern,
    ATL::ActionBlock,
    ATL::OutPattern,
    ATL::LibraryRef,
    OCL::OclFeatureDefinition,
    ATL::Unit,
    ATL::LocatedElement,
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



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



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



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
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



def test_ocl::settype_is_not_abstract():
    assert not inspect.isabstract(OCL::SetType)


def test_ocl::settype_constructor_exists():
    assert callable(OCL::SetType.__init__)


def test_ocl::settype_constructor_args():
    sig = inspect.signature(OCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCL::SequenceType)


def test_ocl::sequencetype_constructor_exists():
    assert callable(OCL::SequenceType.__init__)


def test_ocl::sequencetype_constructor_args():
    sig = inspect.signature(OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCL::OrderedSetType)


def test_ocl::orderedsettype_constructor_exists():
    assert callable(OCL::OrderedSetType.__init__)


def test_ocl::orderedsettype_constructor_args():
    sig = inspect.signature(OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(OCL::BagType)


def test_ocl::bagtype_constructor_exists():
    assert callable(OCL::BagType.__init__)


def test_ocl::bagtype_constructor_args():
    sig = inspect.signature(OCL::BagType.__init__)
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



def test_ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(OCL::NumericType)


def test_ocl::numerictype_constructor_exists():
    assert callable(OCL::NumericType.__init__)


def test_ocl::numerictype_constructor_args():
    sig = inspect.signature(OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL::BooleanType)


def test_ocl::booleantype_constructor_exists():
    assert callable(OCL::BooleanType.__init__)


def test_ocl::booleantype_constructor_args():
    sig = inspect.signature(OCL::BooleanType.__init__)
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



def test_ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionOperationCallExp)


def test_ocl::collectionoperationcallexp_constructor_exists():
    assert callable(OCL::CollectionOperationCallExp.__init__)


def test_ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OperatorCallExp)


def test_ocl::operatorcallexp_constructor_exists():
    assert callable(OCL::OperatorCallExp.__init__)


def test_ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(OCL::OperatorCallExp.__init__)
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



def test_ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SetExp)


def test_ocl::setexp_constructor_exists():
    assert callable(OCL::SetExp.__init__)


def test_ocl::setexp_constructor_args():
    sig = inspect.signature(OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OrderedSetExp)


def test_ocl::orderedsetexp_constructor_exists():
    assert callable(OCL::OrderedSetExp.__init__)


def test_ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SequenceExp)


def test_ocl::sequenceexp_constructor_exists():
    assert callable(OCL::SequenceExp.__init__)


def test_ocl::sequenceexp_constructor_args():
    sig = inspect.signature(OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(OCL::BagExp)


def test_ocl::bagexp_constructor_exists():
    assert callable(OCL::BagExp.__init__)


def test_ocl::bagexp_constructor_args():
    sig = inspect.signature(OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LoopExp)


def test_ocl::loopexp_constructor_exists():
    assert callable(OCL::LoopExp.__init__)


def test_ocl::loopexp_constructor_args():
    sig = inspect.signature(OCL::LoopExp.__init__)
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



def test_ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(OCL::OclAnyType)


def test_ocl::oclanytype_constructor_exists():
    assert callable(OCL::OclAnyType.__init__)


def test_ocl::oclanytype_constructor_args():
    sig = inspect.signature(OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OCL::OclModelElement)


def test_ocl::oclmodelelement_constructor_exists():
    assert callable(OCL::OclModelElement.__init__)


def test_ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(OCL::MapType)


def test_ocl::maptype_constructor_exists():
    assert callable(OCL::MapType.__init__)


def test_ocl::maptype_constructor_args():
    sig = inspect.signature(OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionType)


def test_ocl::collectiontype_constructor_exists():
    assert callable(OCL::CollectionType.__init__)


def test_ocl::collectiontype_constructor_args():
    sig = inspect.signature(OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleType)


def test_ocl::tupletype_constructor_exists():
    assert callable(OCL::TupleType.__init__)


def test_ocl::tupletype_constructor_args():
    sig = inspect.signature(OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(OCL::Primitive)


def test_ocl::primitive_constructor_exists():
    assert callable(OCL::Primitive.__init__)


def test_ocl::primitive_constructor_args():
    sig = inspect.signature(OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_atl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(ATL::BindingStat)


def test_atl::bindingstat_constructor_exists():
    assert callable(ATL::BindingStat.__init__)


def test_atl::bindingstat_constructor_args():
    sig = inspect.signature(ATL::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atl::bindingstat_has_propertyName():
    assert hasattr(ATL::BindingStat, "propertyName")
    descriptor = None
    for klass in ATL::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atl::bindingstat_has_isAssignment():
    assert hasattr(ATL::BindingStat, "isAssignment")
    descriptor = None
    for klass in ATL::BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atl::forstat_is_not_abstract():
    assert not inspect.isabstract(ATL::ForStat)


def test_atl::forstat_constructor_exists():
    assert callable(ATL::ForStat.__init__)


def test_atl::forstat_constructor_args():
    sig = inspect.signature(ATL::ForStat.__init__)
    params = list(sig.parameters.keys())



def test_atl::ifstat_is_not_abstract():
    assert not inspect.isabstract(ATL::IfStat)


def test_atl::ifstat_constructor_exists():
    assert callable(ATL::IfStat.__init__)


def test_atl::ifstat_constructor_args():
    sig = inspect.signature(ATL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_atl::expressionstat_is_not_abstract():
    assert not inspect.isabstract(ATL::ExpressionStat)


def test_atl::expressionstat_constructor_exists():
    assert callable(ATL::ExpressionStat.__init__)


def test_atl::expressionstat_constructor_args():
    sig = inspect.signature(ATL::ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_patternelement_is_not_abstract():
    assert not inspect.isabstract(PatternElement)


def test_patternelement_constructor_exists():
    assert callable(PatternElement.__init__)


def test_patternelement_constructor_args():
    sig = inspect.signature(PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::OutPatternElement)


def test_atl::outpatternelement_constructor_exists():
    assert callable(ATL::OutPatternElement.__init__)


def test_atl::outpatternelement_constructor_args():
    sig = inspect.signature(ATL::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::InPatternElement)


def test_atl::inpatternelement_constructor_exists():
    assert callable(ATL::InPatternElement.__init__)


def test_atl::inpatternelement_constructor_args():
    sig = inspect.signature(ATL::InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ATL::RuleVariableDeclaration)


def test_atl::rulevariabledeclaration_constructor_exists():
    assert callable(ATL::RuleVariableDeclaration.__init__)


def test_atl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(ATL::RuleVariableDeclaration.__init__)
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



def test_ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(OCL::Iterator)


def test_ocl::iterator_constructor_exists():
    assert callable(OCL::Iterator.__init__)


def test_ocl::iterator_constructor_args():
    sig = inspect.signature(OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atl::patternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::PatternElement)


def test_atl::patternelement_constructor_exists():
    assert callable(ATL::PatternElement.__init__)


def test_atl::patternelement_constructor_args():
    sig = inspect.signature(ATL::PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::SimpleOutPatternElement)


def test_atl::simpleoutpatternelement_constructor_exists():
    assert callable(ATL::SimpleOutPatternElement.__init__)


def test_atl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(ATL::SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::ForEachOutPatternElement)


def test_atl::foreachoutpatternelement_constructor_exists():
    assert callable(ATL::ForEachOutPatternElement.__init__)


def test_atl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(ATL::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_droppattern_is_not_abstract():
    assert not inspect.isabstract(DropPattern)


def test_droppattern_constructor_exists():
    assert callable(DropPattern.__init__)


def test_droppattern_constructor_args():
    sig = inspect.signature(DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_inpatternelement_is_not_abstract():
    assert not inspect.isabstract(InPatternElement)


def test_inpatternelement_constructor_exists():
    assert callable(InPatternElement.__init__)


def test_inpatternelement_constructor_args():
    sig = inspect.signature(InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(ATL::SimpleInPatternElement)


def test_atl::simpleinpatternelement_constructor_exists():
    assert callable(ATL::SimpleInPatternElement.__init__)


def test_atl::simpleinpatternelement_constructor_args():
    sig = inspect.signature(ATL::SimpleInPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_matchedrule_is_not_abstract():
    assert not inspect.isabstract(MatchedRule)


def test_matchedrule_constructor_exists():
    assert callable(MatchedRule.__init__)


def test_matchedrule_constructor_args():
    sig = inspect.signature(MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atl::lazymatchedrule_is_not_abstract():
    assert not inspect.isabstract(ATL::LazyMatchedRule)


def test_atl::lazymatchedrule_constructor_exists():
    assert callable(ATL::LazyMatchedRule.__init__)


def test_atl::lazymatchedrule_constructor_args():
    sig = inspect.signature(ATL::LazyMatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_atl::lazymatchedrule_has_isUnique():
    assert hasattr(ATL::LazyMatchedRule, "isUnique")
    descriptor = None
    for klass in ATL::LazyMatchedRule.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_inpattern_is_not_abstract():
    assert not inspect.isabstract(InPattern)


def test_inpattern_constructor_exists():
    assert callable(InPattern.__init__)


def test_inpattern_constructor_args():
    sig = inspect.signature(InPattern.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_atl::calledrule_is_not_abstract():
    assert not inspect.isabstract(ATL::CalledRule)


def test_atl::calledrule_constructor_exists():
    assert callable(ATL::CalledRule.__init__)


def test_atl::calledrule_constructor_args():
    sig = inspect.signature(ATL::CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"

def test_atl::calledrule_has_isEntrypoint():
    assert hasattr(ATL::CalledRule, "isEntrypoint")
    descriptor = None
    for klass in ATL::CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)

def test_atl::calledrule_has_isEndpoint():
    assert hasattr(ATL::CalledRule, "isEndpoint")
    descriptor = None
    for klass in ATL::CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
            break
    assert isinstance(descriptor, property)



def test_atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(ATL::MatchedRule)


def test_atl::matchedrule_constructor_exists():
    assert callable(ATL::MatchedRule.__init__)


def test_atl::matchedrule_constructor_args():
    sig = inspect.signature(ATL::MatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atl::matchedrule_has_isAbstract():
    assert hasattr(ATL::MatchedRule, "isAbstract")
    descriptor = None
    for klass in ATL::MatchedRule.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_atl::matchedrule_has_isNoDefault():
    assert hasattr(ATL::MatchedRule, "isNoDefault")
    descriptor = None
    for klass in ATL::MatchedRule.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)

def test_atl::matchedrule_has_isRefining():
    assert hasattr(ATL::MatchedRule, "isRefining")
    descriptor = None
    for klass in ATL::MatchedRule.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(RuleVariableDeclaration)


def test_rulevariabledeclaration_constructor_exists():
    assert callable(RuleVariableDeclaration.__init__)


def test_rulevariabledeclaration_constructor_args():
    sig = inspect.signature(RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_actionblock_is_not_abstract():
    assert not inspect.isabstract(ActionBlock)


def test_actionblock_constructor_exists():
    assert callable(ActionBlock.__init__)


def test_actionblock_constructor_args():
    sig = inspect.signature(ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_outpattern_is_not_abstract():
    assert not inspect.isabstract(OutPattern)


def test_outpattern_constructor_exists():
    assert callable(OutPattern.__init__)


def test_outpattern_constructor_args():
    sig = inspect.signature(OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::rule_is_not_abstract():
    assert not inspect.isabstract(ATL::Rule)


def test_atl::rule_constructor_exists():
    assert callable(ATL::Rule.__init__)


def test_atl::rule_constructor_args():
    sig = inspect.signature(ATL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::rule_has_name():
    assert hasattr(ATL::Rule, "name")
    descriptor = None
    for klass in ATL::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::helper_is_not_abstract():
    assert not inspect.isabstract(ATL::Helper)


def test_atl::helper_constructor_exists():
    assert callable(ATL::Helper.__init__)


def test_atl::helper_constructor_args():
    sig = inspect.signature(ATL::Helper.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



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



def test_ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(OCL::TupleExp)


def test_ocl::tupleexp_constructor_exists():
    assert callable(OCL::TupleExp.__init__)


def test_ocl::tupleexp_constructor_args():
    sig = inspect.signature(OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL::IfExp)


def test_ocl::ifexp_constructor_exists():
    assert callable(OCL::IfExp.__init__)


def test_ocl::ifexp_constructor_args():
    sig = inspect.signature(OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(OCL::LetExp)


def test_ocl::letexp_constructor_exists():
    assert callable(OCL::LetExp.__init__)


def test_ocl::letexp_constructor_args():
    sig = inspect.signature(OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OCL::OclUndefinedExp)


def test_ocl::oclundefinedexp_constructor_exists():
    assert callable(OCL::OclUndefinedExp.__init__)


def test_ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(OCL::VariableExp)


def test_ocl::variableexp_constructor_exists():
    assert callable(OCL::VariableExp.__init__)


def test_ocl::variableexp_constructor_args():
    sig = inspect.signature(OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(OCL::MapExp)


def test_ocl::mapexp_constructor_exists():
    assert callable(OCL::MapExp.__init__)


def test_ocl::mapexp_constructor_args():
    sig = inspect.signature(OCL::MapExp.__init__)
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



def test_ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(OCL::SuperExp)


def test_ocl::superexp_constructor_exists():
    assert callable(OCL::SuperExp.__init__)


def test_ocl::superexp_constructor_args():
    sig = inspect.signature(OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(OCL::PrimitiveExp)


def test_ocl::primitiveexp_constructor_exists():
    assert callable(OCL::PrimitiveExp.__init__)


def test_ocl::primitiveexp_constructor_args():
    sig = inspect.signature(OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



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



def test_ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(OCL::CollectionExp)


def test_ocl::collectionexp_constructor_exists():
    assert callable(OCL::CollectionExp.__init__)


def test_ocl::collectionexp_constructor_args():
    sig = inspect.signature(OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_helper_is_not_abstract():
    assert not inspect.isabstract(Helper)


def test_helper_constructor_exists():
    assert callable(Helper.__init__)


def test_helper_constructor_args():
    sig = inspect.signature(Helper.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_atl::query_is_not_abstract():
    assert not inspect.isabstract(ATL::Query)


def test_atl::query_constructor_exists():
    assert callable(ATL::Query.__init__)


def test_atl::query_constructor_args():
    sig = inspect.signature(ATL::Query.__init__)
    params = list(sig.parameters.keys())



def test_atl::module_is_not_abstract():
    assert not inspect.isabstract(ATL::Module)


def test_atl::module_constructor_exists():
    assert callable(ATL::Module.__init__)


def test_atl::module_constructor_args():
    sig = inspect.signature(ATL::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atl::module_has_isRefining():
    assert hasattr(ATL::Module, "isRefining")
    descriptor = None
    for klass in ATL::Module.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_atl::library_is_not_abstract():
    assert not inspect.isabstract(ATL::Library)


def test_atl::library_constructor_exists():
    assert callable(ATL::Library.__init__)


def test_atl::library_constructor_args():
    sig = inspect.signature(ATL::Library.__init__)
    params = list(sig.parameters.keys())



def test_libraryref_is_not_abstract():
    assert not inspect.isabstract(LibraryRef)


def test_libraryref_constructor_exists():
    assert callable(LibraryRef.__init__)


def test_libraryref_constructor_args():
    sig = inspect.signature(LibraryRef.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(OCL::VariableDeclaration)


def test_ocl::variabledeclaration_constructor_exists():
    assert callable(OCL::VariableDeclaration.__init__)


def test_ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "id" in params, "Missing parameter 'id'"

def test_ocl::variabledeclaration_has_varName():
    assert hasattr(OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_ocl::variabledeclaration_has_id():
    assert hasattr(OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_atl::binding_is_not_abstract():
    assert not inspect.isabstract(ATL::Binding)


def test_atl::binding_constructor_exists():
    assert callable(ATL::Binding.__init__)


def test_atl::binding_constructor_args():
    sig = inspect.signature(ATL::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_atl::binding_has_isAssignment():
    assert hasattr(ATL::Binding, "isAssignment")
    descriptor = None
    for klass in ATL::Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_atl::binding_has_propertyName():
    assert hasattr(ATL::Binding, "propertyName")
    descriptor = None
    for klass in ATL::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_atl::statement_is_not_abstract():
    assert not inspect.isabstract(ATL::Statement)


def test_atl::statement_constructor_exists():
    assert callable(ATL::Statement.__init__)


def test_atl::statement_constructor_args():
    sig = inspect.signature(ATL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(ATL::ModuleElement)


def test_atl::moduleelement_constructor_exists():
    assert callable(ATL::ModuleElement.__init__)


def test_atl::moduleelement_constructor_args():
    sig = inspect.signature(ATL::ModuleElement.__init__)
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



def test_ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL::OclExpression)


def test_ocl::oclexpression_constructor_exists():
    assert callable(OCL::OclExpression.__init__)


def test_ocl::oclexpression_constructor_args():
    sig = inspect.signature(OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL::OclContextDefinition)


def test_ocl::oclcontextdefinition_constructor_exists():
    assert callable(OCL::OclContextDefinition.__init__)


def test_ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(OCL::MapElement)


def test_ocl::mapelement_constructor_exists():
    assert callable(OCL::MapElement.__init__)


def test_ocl::mapelement_constructor_args():
    sig = inspect.signature(OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::droppattern_is_not_abstract():
    assert not inspect.isabstract(ATL::DropPattern)


def test_atl::droppattern_constructor_exists():
    assert callable(ATL::DropPattern.__init__)


def test_atl::droppattern_constructor_args():
    sig = inspect.signature(ATL::DropPattern.__init__)
    params = list(sig.parameters.keys())



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



def test_ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL::OclFeature)


def test_ocl::oclfeature_constructor_exists():
    assert callable(OCL::OclFeature.__init__)


def test_ocl::oclfeature_constructor_args():
    sig = inspect.signature(OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atl::inpattern_is_not_abstract():
    assert not inspect.isabstract(ATL::InPattern)


def test_atl::inpattern_constructor_exists():
    assert callable(ATL::InPattern.__init__)


def test_atl::inpattern_constructor_args():
    sig = inspect.signature(ATL::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_atl::actionblock_is_not_abstract():
    assert not inspect.isabstract(ATL::ActionBlock)


def test_atl::actionblock_constructor_exists():
    assert callable(ATL::ActionBlock.__init__)


def test_atl::actionblock_constructor_args():
    sig = inspect.signature(ATL::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_atl::outpattern_is_not_abstract():
    assert not inspect.isabstract(ATL::OutPattern)


def test_atl::outpattern_constructor_exists():
    assert callable(ATL::OutPattern.__init__)


def test_atl::outpattern_constructor_args():
    sig = inspect.signature(ATL::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_atl::libraryref_is_not_abstract():
    assert not inspect.isabstract(ATL::LibraryRef)


def test_atl::libraryref_constructor_exists():
    assert callable(ATL::LibraryRef.__init__)


def test_atl::libraryref_constructor_args():
    sig = inspect.signature(ATL::LibraryRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::libraryref_has_name():
    assert hasattr(ATL::LibraryRef, "name")
    descriptor = None
    for klass in ATL::LibraryRef.__mro__:
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



def test_atl::unit_is_not_abstract():
    assert not inspect.isabstract(ATL::Unit)


def test_atl::unit_constructor_exists():
    assert callable(ATL::Unit.__init__)


def test_atl::unit_constructor_args():
    sig = inspect.signature(ATL::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::unit_has_name():
    assert hasattr(ATL::Unit, "name")
    descriptor = None
    for klass in ATL::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(ATL::LocatedElement)


def test_atl::locatedelement_constructor_exists():
    assert callable(ATL::LocatedElement.__init__)


def test_atl::locatedelement_constructor_args():
    sig = inspect.signature(ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_atl::locatedelement_has_location():
    assert hasattr(ATL::LocatedElement, "location")
    descriptor = None
    for klass in ATL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_atl::locatedelement_has_commentsBefore():
    assert hasattr(ATL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in ATL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_atl::locatedelement_has_commentsAfter():
    assert hasattr(ATL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in ATL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
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
OclModelElement_strategy = st.builds(
    OclModelElement,
)
TupleType_strategy = st.builds(
    TupleType,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL::Operation_strategy = st.builds(
    OCL::Operation,
    name=
        safe_text
)
OCL::Attribute_strategy = st.builds(
    OCL::Attribute,
    name=
        safe_text
)
Primitive_strategy = st.builds(
    Primitive,
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
OCL::SetType_strategy = st.builds(
    OCL::SetType,
)
OCL::SequenceType_strategy = st.builds(
    OCL::SequenceType,
)
OCL::OrderedSetType_strategy = st.builds(
    OCL::OrderedSetType,
)
OCL::BagType_strategy = st.builds(
    OCL::BagType,
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
OCL::NumericType_strategy = st.builds(
    OCL::NumericType,
)
OCL::BooleanType_strategy = st.builds(
    OCL::BooleanType,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
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
OCL::CollectionOperationCallExp_strategy = st.builds(
    OCL::CollectionOperationCallExp,
)
OCL::OperatorCallExp_strategy = st.builds(
    OCL::OperatorCallExp,
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
OCL::SetExp_strategy = st.builds(
    OCL::SetExp,
)
OCL::OrderedSetExp_strategy = st.builds(
    OCL::OrderedSetExp,
)
OCL::SequenceExp_strategy = st.builds(
    OCL::SequenceExp,
)
OCL::BagExp_strategy = st.builds(
    OCL::BagExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
OCL::LoopExp_strategy = st.builds(
    OCL::LoopExp,
)
OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
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
OCL::OclAnyType_strategy = st.builds(
    OCL::OclAnyType,
)
OCL::OclModelElement_strategy = st.builds(
    OCL::OclModelElement,
)
OCL::MapType_strategy = st.builds(
    OCL::MapType,
)
OCL::CollectionType_strategy = st.builds(
    OCL::CollectionType,
)
OCL::TupleType_strategy = st.builds(
    OCL::TupleType,
)
OCL::Primitive_strategy = st.builds(
    OCL::Primitive,
)
Statement_strategy = st.builds(
    Statement,
)
ATL::BindingStat_strategy = st.builds(
    ATL::BindingStat,
    propertyName=
        safe_text,
    isAssignment=
        safe_text
)
ATL::ForStat_strategy = st.builds(
    ATL::ForStat,
)
ATL::IfStat_strategy = st.builds(
    ATL::IfStat,
)
ATL::ExpressionStat_strategy = st.builds(
    ATL::ExpressionStat,
)
Iterator_strategy = st.builds(
    Iterator,
)
Binding_strategy = st.builds(
    Binding,
)
PatternElement_strategy = st.builds(
    PatternElement,
)
ATL::OutPatternElement_strategy = st.builds(
    ATL::OutPatternElement,
)
ATL::InPatternElement_strategy = st.builds(
    ATL::InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ATL::RuleVariableDeclaration_strategy = st.builds(
    ATL::RuleVariableDeclaration,
)
OCL::TuplePart_strategy = st.builds(
    OCL::TuplePart,
)
OCL::Parameter_strategy = st.builds(
    OCL::Parameter,
)
OCL::Iterator_strategy = st.builds(
    OCL::Iterator,
)
ATL::PatternElement_strategy = st.builds(
    ATL::PatternElement,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
ATL::SimpleOutPatternElement_strategy = st.builds(
    ATL::SimpleOutPatternElement,
)
ATL::ForEachOutPatternElement_strategy = st.builds(
    ATL::ForEachOutPatternElement,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
ATL::SimpleInPatternElement_strategy = st.builds(
    ATL::SimpleInPatternElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
ATL::LazyMatchedRule_strategy = st.builds(
    ATL::LazyMatchedRule,
    isUnique=
        safe_text
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
ATL::CalledRule_strategy = st.builds(
    ATL::CalledRule,
    isEntrypoint=
        safe_text,
    isEndpoint=
        safe_text
)
ATL::MatchedRule_strategy = st.builds(
    ATL::MatchedRule,
    isAbstract=
        safe_text,
    isNoDefault=
        safe_text,
    isRefining=
        safe_text
)
RuleVariableDeclaration_strategy = st.builds(
    RuleVariableDeclaration,
)
ActionBlock_strategy = st.builds(
    ActionBlock,
)
OutPattern_strategy = st.builds(
    OutPattern,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
Library_strategy = st.builds(
    Library,
)
Query_strategy = st.builds(
    Query,
)
Module_strategy = st.builds(
    Module,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
ATL::Rule_strategy = st.builds(
    ATL::Rule,
    name=
        safe_text
)
ATL::Helper_strategy = st.builds(
    ATL::Helper,
)
OclModel_strategy = st.builds(
    OclModel,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL::PropertyCallExp_strategy = st.builds(
    OCL::PropertyCallExp,
)
OCL::TupleExp_strategy = st.builds(
    OCL::TupleExp,
)
OCL::IfExp_strategy = st.builds(
    OCL::IfExp,
)
OCL::LetExp_strategy = st.builds(
    OCL::LetExp,
)
OCL::OclUndefinedExp_strategy = st.builds(
    OCL::OclUndefinedExp,
)
OCL::VariableExp_strategy = st.builds(
    OCL::VariableExp,
)
OCL::MapExp_strategy = st.builds(
    OCL::MapExp,
)
OCL::OclType_strategy = st.builds(
    OCL::OclType,
    name=
        safe_text
)
OCL::SuperExp_strategy = st.builds(
    OCL::SuperExp,
)
OCL::PrimitiveExp_strategy = st.builds(
    OCL::PrimitiveExp,
)
OCL::EnumLiteralExp_strategy = st.builds(
    OCL::EnumLiteralExp,
    name=
        safe_text
)
OCL::CollectionExp_strategy = st.builds(
    OCL::CollectionExp,
)
Helper_strategy = st.builds(
    Helper,
)
Unit_strategy = st.builds(
    Unit,
)
ATL::Query_strategy = st.builds(
    ATL::Query,
)
ATL::Module_strategy = st.builds(
    ATL::Module,
    isRefining=
        safe_text
)
ATL::Library_strategy = st.builds(
    ATL::Library,
)
LibraryRef_strategy = st.builds(
    LibraryRef,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
OCL::VariableDeclaration_strategy = st.builds(
    OCL::VariableDeclaration,
    varName=
        safe_text,
    id=
        safe_text
)
ATL::Binding_strategy = st.builds(
    ATL::Binding,
    isAssignment=
        safe_text,
    propertyName=
        safe_text
)
ATL::Statement_strategy = st.builds(
    ATL::Statement,
)
ATL::ModuleElement_strategy = st.builds(
    ATL::ModuleElement,
)
OCL::OclModel_strategy = st.builds(
    OCL::OclModel,
    name=
        safe_text
)
OCL::OclExpression_strategy = st.builds(
    OCL::OclExpression,
)
OCL::OclContextDefinition_strategy = st.builds(
    OCL::OclContextDefinition,
)
OCL::MapElement_strategy = st.builds(
    OCL::MapElement,
)
ATL::DropPattern_strategy = st.builds(
    ATL::DropPattern,
)
OCL::TupleTypeAttribute_strategy = st.builds(
    OCL::TupleTypeAttribute,
    name=
        safe_text
)
OCL::OclFeature_strategy = st.builds(
    OCL::OclFeature,
)
ATL::InPattern_strategy = st.builds(
    ATL::InPattern,
)
ATL::ActionBlock_strategy = st.builds(
    ATL::ActionBlock,
)
ATL::OutPattern_strategy = st.builds(
    ATL::OutPattern,
)
ATL::LibraryRef_strategy = st.builds(
    ATL::LibraryRef,
    name=
        safe_text
)
OCL::OclFeatureDefinition_strategy = st.builds(
    OCL::OclFeatureDefinition,
)
ATL::Unit_strategy = st.builds(
    ATL::Unit,
    name=
        safe_text
)
ATL::LocatedElement_strategy = st.builds(
    ATL::LocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

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

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

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

@given(instance=OCL::SetType_strategy)
@settings(max_examples=50)
def test_ocl::settype_instantiation(instance):
    assert isinstance(instance, OCL::SetType)

@given(instance=OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, OCL::SequenceType)

@given(instance=OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, OCL::OrderedSetType)

@given(instance=OCL::BagType_strategy)
@settings(max_examples=50)
def test_ocl::bagtype_instantiation(instance):
    assert isinstance(instance, OCL::BagType)

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

@given(instance=OCL::NumericType_strategy)
@settings(max_examples=50)
def test_ocl::numerictype_instantiation(instance):
    assert isinstance(instance, OCL::NumericType)

@given(instance=OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_ocl::booleantype_instantiation(instance):
    assert isinstance(instance, OCL::BooleanType)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

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

@given(instance=OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCL::CollectionOperationCallExp)

@given(instance=OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCL::OperatorCallExp)

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

@given(instance=OCL::SetExp_strategy)
@settings(max_examples=50)
def test_ocl::setexp_instantiation(instance):
    assert isinstance(instance, OCL::SetExp)

@given(instance=OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, OCL::OrderedSetExp)

@given(instance=OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, OCL::SequenceExp)

@given(instance=OCL::BagExp_strategy)
@settings(max_examples=50)
def test_ocl::bagexp_instantiation(instance):
    assert isinstance(instance, OCL::BagExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::loopexp_instantiation(instance):
    assert isinstance(instance, OCL::LoopExp)

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

@given(instance=OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, OCL::OclAnyType)

@given(instance=OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, OCL::OclModelElement)

@given(instance=OCL::MapType_strategy)
@settings(max_examples=50)
def test_ocl::maptype_instantiation(instance):
    assert isinstance(instance, OCL::MapType)

@given(instance=OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, OCL::CollectionType)

@given(instance=OCL::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::tupletype_instantiation(instance):
    assert isinstance(instance, OCL::TupleType)

@given(instance=OCL::Primitive_strategy)
@settings(max_examples=50)
def test_ocl::primitive_instantiation(instance):
    assert isinstance(instance, OCL::Primitive)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ATL::BindingStat_strategy)
@settings(max_examples=50)
def test_atl::bindingstat_instantiation(instance):
    assert isinstance(instance, ATL::BindingStat)

@given(instance=ATL::BindingStat_strategy)
def test_atl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=ATL::BindingStat_strategy)
def test_atl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=ATL::BindingStat_strategy)
def test_atl::bindingstat_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=ATL::BindingStat_strategy)
def test_atl::bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=ATL::ForStat_strategy)
@settings(max_examples=50)
def test_atl::forstat_instantiation(instance):
    assert isinstance(instance, ATL::ForStat)

@given(instance=ATL::IfStat_strategy)
@settings(max_examples=50)
def test_atl::ifstat_instantiation(instance):
    assert isinstance(instance, ATL::IfStat)

@given(instance=ATL::ExpressionStat_strategy)
@settings(max_examples=50)
def test_atl::expressionstat_instantiation(instance):
    assert isinstance(instance, ATL::ExpressionStat)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=PatternElement_strategy)
@settings(max_examples=50)
def test_patternelement_instantiation(instance):
    assert isinstance(instance, PatternElement)

@given(instance=ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, ATL::OutPatternElement)

@given(instance=ATL::InPatternElement_strategy)
@settings(max_examples=50)
def test_atl::inpatternelement_instantiation(instance):
    assert isinstance(instance, ATL::InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ATL::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_atl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, ATL::RuleVariableDeclaration)

@given(instance=OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, OCL::TuplePart)

@given(instance=OCL::Parameter_strategy)
@settings(max_examples=50)
def test_ocl::parameter_instantiation(instance):
    assert isinstance(instance, OCL::Parameter)

@given(instance=OCL::Iterator_strategy)
@settings(max_examples=50)
def test_ocl::iterator_instantiation(instance):
    assert isinstance(instance, OCL::Iterator)

@given(instance=ATL::PatternElement_strategy)
@settings(max_examples=50)
def test_atl::patternelement_instantiation(instance):
    assert isinstance(instance, ATL::PatternElement)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=ATL::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, ATL::SimpleOutPatternElement)

@given(instance=ATL::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, ATL::ForEachOutPatternElement)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=ATL::SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_atl::simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, ATL::SimpleInPatternElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=ATL::LazyMatchedRule_strategy)
@settings(max_examples=50)
def test_atl::lazymatchedrule_instantiation(instance):
    assert isinstance(instance, ATL::LazyMatchedRule)

@given(instance=ATL::LazyMatchedRule_strategy)
def test_atl::lazymatchedrule_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=ATL::LazyMatchedRule_strategy)
def test_atl::lazymatchedrule_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=InPattern_strategy)
@settings(max_examples=50)
def test_inpattern_instantiation(instance):
    assert isinstance(instance, InPattern)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=ATL::CalledRule_strategy)
@settings(max_examples=50)
def test_atl::calledrule_instantiation(instance):
    assert isinstance(instance, ATL::CalledRule)

@given(instance=ATL::CalledRule_strategy)
def test_atl::calledrule_isEntrypoint_type(instance):
    assert isinstance(instance.isEntrypoint, str)


@given(instance=ATL::CalledRule_strategy)
def test_atl::calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=ATL::CalledRule_strategy)
def test_atl::calledrule_isEndpoint_type(instance):
    assert isinstance(instance.isEndpoint, str)


@given(instance=ATL::CalledRule_strategy)
def test_atl::calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original

@given(instance=ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_atl::matchedrule_instantiation(instance):
    assert isinstance(instance, ATL::MatchedRule)

@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isNoDefault_type(instance):
    assert isinstance(instance.isNoDefault, str)


@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original

@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=ATL::MatchedRule_strategy)
def test_atl::matchedrule_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, RuleVariableDeclaration)

@given(instance=ActionBlock_strategy)
@settings(max_examples=50)
def test_actionblock_instantiation(instance):
    assert isinstance(instance, ActionBlock)

@given(instance=OutPattern_strategy)
@settings(max_examples=50)
def test_outpattern_instantiation(instance):
    assert isinstance(instance, OutPattern)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=ATL::Rule_strategy)
@settings(max_examples=50)
def test_atl::rule_instantiation(instance):
    assert isinstance(instance, ATL::Rule)

@given(instance=ATL::Rule_strategy)
def test_atl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ATL::Rule_strategy)
def test_atl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ATL::Helper_strategy)
@settings(max_examples=50)
def test_atl::helper_instantiation(instance):
    assert isinstance(instance, ATL::Helper)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, OCL::PropertyCallExp)

@given(instance=OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, OCL::TupleExp)

@given(instance=OCL::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::ifexp_instantiation(instance):
    assert isinstance(instance, OCL::IfExp)

@given(instance=OCL::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::letexp_instantiation(instance):
    assert isinstance(instance, OCL::LetExp)

@given(instance=OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OCL::OclUndefinedExp)

@given(instance=OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::variableexp_instantiation(instance):
    assert isinstance(instance, OCL::VariableExp)

@given(instance=OCL::MapExp_strategy)
@settings(max_examples=50)
def test_ocl::mapexp_instantiation(instance):
    assert isinstance(instance, OCL::MapExp)

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

@given(instance=OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_ocl::superexp_instantiation(instance):
    assert isinstance(instance, OCL::SuperExp)

@given(instance=OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, OCL::PrimitiveExp)

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

@given(instance=OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, OCL::CollectionExp)

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=ATL::Query_strategy)
@settings(max_examples=50)
def test_atl::query_instantiation(instance):
    assert isinstance(instance, ATL::Query)

@given(instance=ATL::Module_strategy)
@settings(max_examples=50)
def test_atl::module_instantiation(instance):
    assert isinstance(instance, ATL::Module)

@given(instance=ATL::Module_strategy)
def test_atl::module_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=ATL::Module_strategy)
def test_atl::module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=ATL::Library_strategy)
@settings(max_examples=50)
def test_atl::library_instantiation(instance):
    assert isinstance(instance, ATL::Library)

@given(instance=LibraryRef_strategy)
@settings(max_examples=50)
def test_libraryref_instantiation(instance):
    assert isinstance(instance, LibraryRef)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, OCL::VariableDeclaration)

@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=OCL::VariableDeclaration_strategy)
def test_ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ATL::Binding_strategy)
@settings(max_examples=50)
def test_atl::binding_instantiation(instance):
    assert isinstance(instance, ATL::Binding)

@given(instance=ATL::Binding_strategy)
def test_atl::binding_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=ATL::Binding_strategy)
def test_atl::binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=ATL::Binding_strategy)
def test_atl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=ATL::Binding_strategy)
def test_atl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=ATL::Statement_strategy)
@settings(max_examples=50)
def test_atl::statement_instantiation(instance):
    assert isinstance(instance, ATL::Statement)

@given(instance=ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_atl::moduleelement_instantiation(instance):
    assert isinstance(instance, ATL::ModuleElement)

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

@given(instance=OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, OCL::OclExpression)

@given(instance=OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCL::OclContextDefinition)

@given(instance=OCL::MapElement_strategy)
@settings(max_examples=50)
def test_ocl::mapelement_instantiation(instance):
    assert isinstance(instance, OCL::MapElement)

@given(instance=ATL::DropPattern_strategy)
@settings(max_examples=50)
def test_atl::droppattern_instantiation(instance):
    assert isinstance(instance, ATL::DropPattern)

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

@given(instance=OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, OCL::OclFeature)

@given(instance=ATL::InPattern_strategy)
@settings(max_examples=50)
def test_atl::inpattern_instantiation(instance):
    assert isinstance(instance, ATL::InPattern)

@given(instance=ATL::ActionBlock_strategy)
@settings(max_examples=50)
def test_atl::actionblock_instantiation(instance):
    assert isinstance(instance, ATL::ActionBlock)

@given(instance=ATL::OutPattern_strategy)
@settings(max_examples=50)
def test_atl::outpattern_instantiation(instance):
    assert isinstance(instance, ATL::OutPattern)

@given(instance=ATL::LibraryRef_strategy)
@settings(max_examples=50)
def test_atl::libraryref_instantiation(instance):
    assert isinstance(instance, ATL::LibraryRef)

@given(instance=ATL::LibraryRef_strategy)
def test_atl::libraryref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ATL::LibraryRef_strategy)
def test_atl::libraryref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OCL::OclFeatureDefinition)

@given(instance=ATL::Unit_strategy)
@settings(max_examples=50)
def test_atl::unit_instantiation(instance):
    assert isinstance(instance, ATL::Unit)

@given(instance=ATL::Unit_strategy)
def test_atl::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ATL::Unit_strategy)
def test_atl::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_atl::locatedelement_instantiation(instance):
    assert isinstance(instance, ATL::LocatedElement)

@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=ATL::LocatedElement_strategy)
def test_atl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original
