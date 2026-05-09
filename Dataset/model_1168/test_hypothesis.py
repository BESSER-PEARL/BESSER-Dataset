import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclModelElement,
    OclFeature,
    top::OCL::Attribute,
    top::OCL::Operation,
    TupleType,
    NumericType,
    top::OCL::RealType,
    top::OCL::IntegerType,
    TupleTypeAttribute,
    CollectionType,
    top::OCL::BagType,
    top::OCL::SequenceType,
    top::OCL::OrderedSetType,
    top::OCL::SetType,
    MapType,
    OclContextDefinition,
    VariableExp,
    IterateExp,
    Primitive,
    top::OCL::NumericType,
    top::OCL::BooleanType,
    top::OCL::StringType,
    MapExp,
    MapElement,
    TuplePart,
    NumericExp,
    top::OCL::IntegerExp,
    top::OCL::RealExp,
    PrimitiveExp,
    top::OCL::NumericExp,
    top::OCL::BooleanExp,
    top::OCL::StringExp,
    TupleExp,
    Attribute,
    Operation,
    OperationCallExp,
    top::OCL::CollectionOperationCallExp,
    top::OCL::OperatorCallExp,
    LoopExp,
    top::OCL::IteratorExp,
    top::OCL::IterateExp,
    LetExp,
    CollectionExp,
    top::OCL::BagExp,
    top::OCL::SequenceExp,
    top::OCL::OrderedSetExp,
    top::OCL::SetExp,
    PropertyCallExp,
    top::OCL::NavigationOrAttributeCallExp,
    top::OCL::LoopExp,
    top::OCL::OperationCallExp,
    IfExp,
    OclType,
    top::OCL::CollectionType,
    top::OCL::Primitive,
    top::OCL::TupleType,
    top::OCL::OclAnyType,
    top::OCL::MapType,
    top::OCL::OclModelElement,
    Statement,
    top::ATL::ExpressionStat,
    top::ATL::BindingStat,
    top::ATL::IfStat,
    top::ATL::ForStat,
    Iterator,
    Binding,
    PatternElement,
    top::ATL::OutPatternElement,
    top::ATL::InPatternElement,
    VariableDeclaration,
    top::OCL::TuplePart,
    top::OCL::Parameter,
    top::OCL::Iterator,
    top::ATL::RuleVariableDeclaration,
    top::ATL::PatternElement,
    OutPatternElement,
    top::ATL::ForEachOutPatternElement,
    top::ATL::SimpleOutPatternElement,
    DropPattern,
    InPatternElement,
    top::ATL::SimpleInPatternElement,
    Parameter,
    MatchedRule,
    top::ATL::LazyMatchedRule,
    InPattern,
    Rule,
    top::ATL::CalledRule,
    top::ATL::MatchedRule,
    RuleVariableDeclaration,
    ActionBlock,
    OutPattern,
    OclFeatureDefinition,
    Library,
    Query,
    Module,
    ModuleElement,
    top::ATL::Rule,
    top::ATL::Helper,
    OclModel,
    OclExpression,
    top::OCL::EnumLiteralExp,
    top::OCL::IfExp,
    top::OCL::CollectionExp,
    top::OCL::OclType,
    top::OCL::SuperExp,
    top::OCL::LetExp,
    top::OCL::VariableExp,
    top::OCL::TupleExp,
    top::OCL::PropertyCallExp,
    top::OCL::MapExp,
    top::OCL::PrimitiveExp,
    top::OCL::OclUndefinedExp,
    Helper,
    Unit,
    top::ATL::Module,
    top::ATL::Query,
    top::ATL::Library,
    LibraryRef,
    top::ATL::LocatedElement,
    LocatedElement,
    top::ATL::Binding,
    top::ATL::InPattern,
    top::OCL::OclExpression,
    top::ATL::DropPattern,
    top::OCL::TupleTypeAttribute,
    top::OCL::OclFeature,
    top::OCL::OclFeatureDefinition,
    top::OCL::OclModel,
    top::OCL::MapElement,
    top::OCL::VariableDeclaration,
    top::OCL::OclContextDefinition,
    top::ATL::ModuleElement,
    top::ATL::ActionBlock,
    top::ATL::Statement,
    top::ATL::LibraryRef,
    top::ATL::OutPattern,
    top::ATL::Unit,
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



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(top::OCL::Attribute)


def test_top::ocl::attribute_constructor_exists():
    assert callable(top::OCL::Attribute.__init__)


def test_top::ocl::attribute_constructor_args():
    sig = inspect.signature(top::OCL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::attribute_has_name():
    assert hasattr(top::OCL::Attribute, "name")
    descriptor = None
    for klass in top::OCL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(top::OCL::Operation)


def test_top::ocl::operation_constructor_exists():
    assert callable(top::OCL::Operation.__init__)


def test_top::ocl::operation_constructor_args():
    sig = inspect.signature(top::OCL::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::operation_has_name():
    assert hasattr(top::OCL::Operation, "name")
    descriptor = None
    for klass in top::OCL::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_top::ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::RealType)


def test_top::ocl::realtype_constructor_exists():
    assert callable(top::OCL::RealType.__init__)


def test_top::ocl::realtype_constructor_args():
    sig = inspect.signature(top::OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::IntegerType)


def test_top::ocl::integertype_constructor_exists():
    assert callable(top::OCL::IntegerType.__init__)


def test_top::ocl::integertype_constructor_args():
    sig = inspect.signature(top::OCL::IntegerType.__init__)
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



def test_top::ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::BagType)


def test_top::ocl::bagtype_constructor_exists():
    assert callable(top::OCL::BagType.__init__)


def test_top::ocl::bagtype_constructor_args():
    sig = inspect.signature(top::OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::SequenceType)


def test_top::ocl::sequencetype_constructor_exists():
    assert callable(top::OCL::SequenceType.__init__)


def test_top::ocl::sequencetype_constructor_args():
    sig = inspect.signature(top::OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OrderedSetType)


def test_top::ocl::orderedsettype_constructor_exists():
    assert callable(top::OCL::OrderedSetType.__init__)


def test_top::ocl::orderedsettype_constructor_args():
    sig = inspect.signature(top::OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::settype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::SetType)


def test_top::ocl::settype_constructor_exists():
    assert callable(top::OCL::SetType.__init__)


def test_top::ocl::settype_constructor_args():
    sig = inspect.signature(top::OCL::SetType.__init__)
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



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::NumericType)


def test_top::ocl::numerictype_constructor_exists():
    assert callable(top::OCL::NumericType.__init__)


def test_top::ocl::numerictype_constructor_args():
    sig = inspect.signature(top::OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::BooleanType)


def test_top::ocl::booleantype_constructor_exists():
    assert callable(top::OCL::BooleanType.__init__)


def test_top::ocl::booleantype_constructor_args():
    sig = inspect.signature(top::OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::StringType)


def test_top::ocl::stringtype_constructor_exists():
    assert callable(top::OCL::StringType.__init__)


def test_top::ocl::stringtype_constructor_args():
    sig = inspect.signature(top::OCL::StringType.__init__)
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



def test_top::ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::IntegerExp)


def test_top::ocl::integerexp_constructor_exists():
    assert callable(top::OCL::IntegerExp.__init__)


def test_top::ocl::integerexp_constructor_args():
    sig = inspect.signature(top::OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_top::ocl::integerexp_has_integerSymbol():
    assert hasattr(top::OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in top::OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::RealExp)


def test_top::ocl::realexp_constructor_exists():
    assert callable(top::OCL::RealExp.__init__)


def test_top::ocl::realexp_constructor_args():
    sig = inspect.signature(top::OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_top::ocl::realexp_has_realSymbol():
    assert hasattr(top::OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in top::OCL::RealExp.__mro__:
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



def test_top::ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::NumericExp)


def test_top::ocl::numericexp_constructor_exists():
    assert callable(top::OCL::NumericExp.__init__)


def test_top::ocl::numericexp_constructor_args():
    sig = inspect.signature(top::OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::BooleanExp)


def test_top::ocl::booleanexp_constructor_exists():
    assert callable(top::OCL::BooleanExp.__init__)


def test_top::ocl::booleanexp_constructor_args():
    sig = inspect.signature(top::OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_top::ocl::booleanexp_has_booleanSymbol():
    assert hasattr(top::OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in top::OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::StringExp)


def test_top::ocl::stringexp_constructor_exists():
    assert callable(top::OCL::StringExp.__init__)


def test_top::ocl::stringexp_constructor_args():
    sig = inspect.signature(top::OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_top::ocl::stringexp_has_stringSymbol():
    assert hasattr(top::OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in top::OCL::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



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



def test_top::ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::CollectionOperationCallExp)


def test_top::ocl::collectionoperationcallexp_constructor_exists():
    assert callable(top::OCL::CollectionOperationCallExp.__init__)


def test_top::ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(top::OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OperatorCallExp)


def test_top::ocl::operatorcallexp_constructor_exists():
    assert callable(top::OCL::OperatorCallExp.__init__)


def test_top::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(top::OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::IteratorExp)


def test_top::ocl::iteratorexp_constructor_exists():
    assert callable(top::OCL::IteratorExp.__init__)


def test_top::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(top::OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::iteratorexp_has_name():
    assert hasattr(top::OCL::IteratorExp, "name")
    descriptor = None
    for klass in top::OCL::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::IterateExp)


def test_top::ocl::iterateexp_constructor_exists():
    assert callable(top::OCL::IterateExp.__init__)


def test_top::ocl::iterateexp_constructor_args():
    sig = inspect.signature(top::OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



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



def test_top::ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::BagExp)


def test_top::ocl::bagexp_constructor_exists():
    assert callable(top::OCL::BagExp.__init__)


def test_top::ocl::bagexp_constructor_args():
    sig = inspect.signature(top::OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::SequenceExp)


def test_top::ocl::sequenceexp_constructor_exists():
    assert callable(top::OCL::SequenceExp.__init__)


def test_top::ocl::sequenceexp_constructor_args():
    sig = inspect.signature(top::OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OrderedSetExp)


def test_top::ocl::orderedsetexp_constructor_exists():
    assert callable(top::OCL::OrderedSetExp.__init__)


def test_top::ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(top::OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::SetExp)


def test_top::ocl::setexp_constructor_exists():
    assert callable(top::OCL::SetExp.__init__)


def test_top::ocl::setexp_constructor_args():
    sig = inspect.signature(top::OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::NavigationOrAttributeCallExp)


def test_top::ocl::navigationorattributecallexp_constructor_exists():
    assert callable(top::OCL::NavigationOrAttributeCallExp.__init__)


def test_top::ocl::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(top::OCL::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::navigationorattributecallexp_has_name():
    assert hasattr(top::OCL::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in top::OCL::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::LoopExp)


def test_top::ocl::loopexp_constructor_exists():
    assert callable(top::OCL::LoopExp.__init__)


def test_top::ocl::loopexp_constructor_args():
    sig = inspect.signature(top::OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OperationCallExp)


def test_top::ocl::operationcallexp_constructor_exists():
    assert callable(top::OCL::OperationCallExp.__init__)


def test_top::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(top::OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_top::ocl::operationcallexp_has_operationName():
    assert hasattr(top::OCL::OperationCallExp, "operationName")
    descriptor = None
    for klass in top::OCL::OperationCallExp.__mro__:
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



def test_top::ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::CollectionType)


def test_top::ocl::collectiontype_constructor_exists():
    assert callable(top::OCL::CollectionType.__init__)


def test_top::ocl::collectiontype_constructor_args():
    sig = inspect.signature(top::OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(top::OCL::Primitive)


def test_top::ocl::primitive_constructor_exists():
    assert callable(top::OCL::Primitive.__init__)


def test_top::ocl::primitive_constructor_args():
    sig = inspect.signature(top::OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::TupleType)


def test_top::ocl::tupletype_constructor_exists():
    assert callable(top::OCL::TupleType.__init__)


def test_top::ocl::tupletype_constructor_args():
    sig = inspect.signature(top::OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclAnyType)


def test_top::ocl::oclanytype_constructor_exists():
    assert callable(top::OCL::OclAnyType.__init__)


def test_top::ocl::oclanytype_constructor_args():
    sig = inspect.signature(top::OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::MapType)


def test_top::ocl::maptype_constructor_exists():
    assert callable(top::OCL::MapType.__init__)


def test_top::ocl::maptype_constructor_args():
    sig = inspect.signature(top::OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclModelElement)


def test_top::ocl::oclmodelelement_constructor_exists():
    assert callable(top::OCL::OclModelElement.__init__)


def test_top::ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(top::OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::expressionstat_is_not_abstract():
    assert not inspect.isabstract(top::ATL::ExpressionStat)


def test_top::atl::expressionstat_constructor_exists():
    assert callable(top::ATL::ExpressionStat.__init__)


def test_top::atl::expressionstat_constructor_args():
    sig = inspect.signature(top::ATL::ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(top::ATL::BindingStat)


def test_top::atl::bindingstat_constructor_exists():
    assert callable(top::ATL::BindingStat.__init__)


def test_top::atl::bindingstat_constructor_args():
    sig = inspect.signature(top::ATL::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_top::atl::bindingstat_has_isAssignment():
    assert hasattr(top::ATL::BindingStat, "isAssignment")
    descriptor = None
    for klass in top::ATL::BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::bindingstat_has_propertyName():
    assert hasattr(top::ATL::BindingStat, "propertyName")
    descriptor = None
    for klass in top::ATL::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::ifstat_is_not_abstract():
    assert not inspect.isabstract(top::ATL::IfStat)


def test_top::atl::ifstat_constructor_exists():
    assert callable(top::ATL::IfStat.__init__)


def test_top::atl::ifstat_constructor_args():
    sig = inspect.signature(top::ATL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::forstat_is_not_abstract():
    assert not inspect.isabstract(top::ATL::ForStat)


def test_top::atl::forstat_constructor_exists():
    assert callable(top::ATL::ForStat.__init__)


def test_top::atl::forstat_constructor_args():
    sig = inspect.signature(top::ATL::ForStat.__init__)
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



def test_top::atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::OutPatternElement)


def test_top::atl::outpatternelement_constructor_exists():
    assert callable(top::ATL::OutPatternElement.__init__)


def test_top::atl::outpatternelement_constructor_args():
    sig = inspect.signature(top::ATL::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::InPatternElement)


def test_top::atl::inpatternelement_constructor_exists():
    assert callable(top::ATL::InPatternElement.__init__)


def test_top::atl::inpatternelement_constructor_args():
    sig = inspect.signature(top::ATL::InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(top::OCL::TuplePart)


def test_top::ocl::tuplepart_constructor_exists():
    assert callable(top::OCL::TuplePart.__init__)


def test_top::ocl::tuplepart_constructor_args():
    sig = inspect.signature(top::OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(top::OCL::Parameter)


def test_top::ocl::parameter_constructor_exists():
    assert callable(top::OCL::Parameter.__init__)


def test_top::ocl::parameter_constructor_args():
    sig = inspect.signature(top::OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(top::OCL::Iterator)


def test_top::ocl::iterator_constructor_exists():
    assert callable(top::OCL::Iterator.__init__)


def test_top::ocl::iterator_constructor_args():
    sig = inspect.signature(top::OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(top::ATL::RuleVariableDeclaration)


def test_top::atl::rulevariabledeclaration_constructor_exists():
    assert callable(top::ATL::RuleVariableDeclaration.__init__)


def test_top::atl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(top::ATL::RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::patternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::PatternElement)


def test_top::atl::patternelement_constructor_exists():
    assert callable(top::ATL::PatternElement.__init__)


def test_top::atl::patternelement_constructor_args():
    sig = inspect.signature(top::ATL::PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::ForEachOutPatternElement)


def test_top::atl::foreachoutpatternelement_constructor_exists():
    assert callable(top::ATL::ForEachOutPatternElement.__init__)


def test_top::atl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(top::ATL::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::SimpleOutPatternElement)


def test_top::atl::simpleoutpatternelement_constructor_exists():
    assert callable(top::ATL::SimpleOutPatternElement.__init__)


def test_top::atl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(top::ATL::SimpleOutPatternElement.__init__)
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



def test_top::atl::simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::SimpleInPatternElement)


def test_top::atl::simpleinpatternelement_constructor_exists():
    assert callable(top::ATL::SimpleInPatternElement.__init__)


def test_top::atl::simpleinpatternelement_constructor_args():
    sig = inspect.signature(top::ATL::SimpleInPatternElement.__init__)
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



def test_top::atl::lazymatchedrule_is_not_abstract():
    assert not inspect.isabstract(top::ATL::LazyMatchedRule)


def test_top::atl::lazymatchedrule_constructor_exists():
    assert callable(top::ATL::LazyMatchedRule.__init__)


def test_top::atl::lazymatchedrule_constructor_args():
    sig = inspect.signature(top::ATL::LazyMatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_top::atl::lazymatchedrule_has_isUnique():
    assert hasattr(top::ATL::LazyMatchedRule, "isUnique")
    descriptor = None
    for klass in top::ATL::LazyMatchedRule.__mro__:
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



def test_top::atl::calledrule_is_not_abstract():
    assert not inspect.isabstract(top::ATL::CalledRule)


def test_top::atl::calledrule_constructor_exists():
    assert callable(top::ATL::CalledRule.__init__)


def test_top::atl::calledrule_constructor_args():
    sig = inspect.signature(top::ATL::CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"

def test_top::atl::calledrule_has_isEndpoint():
    assert hasattr(top::ATL::CalledRule, "isEndpoint")
    descriptor = None
    for klass in top::ATL::CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::calledrule_has_isEntrypoint():
    assert hasattr(top::ATL::CalledRule, "isEntrypoint")
    descriptor = None
    for klass in top::ATL::CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(top::ATL::MatchedRule)


def test_top::atl::matchedrule_constructor_exists():
    assert callable(top::ATL::MatchedRule.__init__)


def test_top::atl::matchedrule_constructor_args():
    sig = inspect.signature(top::ATL::MatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"
    assert "isRefining" in params, "Missing parameter 'isRefining'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_top::atl::matchedrule_has_isNoDefault():
    assert hasattr(top::ATL::MatchedRule, "isNoDefault")
    descriptor = None
    for klass in top::ATL::MatchedRule.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::matchedrule_has_isRefining():
    assert hasattr(top::ATL::MatchedRule, "isRefining")
    descriptor = None
    for klass in top::ATL::MatchedRule.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::matchedrule_has_isAbstract():
    assert hasattr(top::ATL::MatchedRule, "isAbstract")
    descriptor = None
    for klass in top::ATL::MatchedRule.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
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



def test_top::atl::rule_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Rule)


def test_top::atl::rule_constructor_exists():
    assert callable(top::ATL::Rule.__init__)


def test_top::atl::rule_constructor_args():
    sig = inspect.signature(top::ATL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::atl::rule_has_name():
    assert hasattr(top::ATL::Rule, "name")
    descriptor = None
    for klass in top::ATL::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::helper_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Helper)


def test_top::atl::helper_constructor_exists():
    assert callable(top::ATL::Helper.__init__)


def test_top::atl::helper_constructor_args():
    sig = inspect.signature(top::ATL::Helper.__init__)
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



def test_top::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::EnumLiteralExp)


def test_top::ocl::enumliteralexp_constructor_exists():
    assert callable(top::OCL::EnumLiteralExp.__init__)


def test_top::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(top::OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::enumliteralexp_has_name():
    assert hasattr(top::OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in top::OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::IfExp)


def test_top::ocl::ifexp_constructor_exists():
    assert callable(top::OCL::IfExp.__init__)


def test_top::ocl::ifexp_constructor_args():
    sig = inspect.signature(top::OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::CollectionExp)


def test_top::ocl::collectionexp_constructor_exists():
    assert callable(top::OCL::CollectionExp.__init__)


def test_top::ocl::collectionexp_constructor_args():
    sig = inspect.signature(top::OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclType)


def test_top::ocl::ocltype_constructor_exists():
    assert callable(top::OCL::OclType.__init__)


def test_top::ocl::ocltype_constructor_args():
    sig = inspect.signature(top::OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::ocltype_has_name():
    assert hasattr(top::OCL::OclType, "name")
    descriptor = None
    for klass in top::OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::SuperExp)


def test_top::ocl::superexp_constructor_exists():
    assert callable(top::OCL::SuperExp.__init__)


def test_top::ocl::superexp_constructor_args():
    sig = inspect.signature(top::OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::LetExp)


def test_top::ocl::letexp_constructor_exists():
    assert callable(top::OCL::LetExp.__init__)


def test_top::ocl::letexp_constructor_args():
    sig = inspect.signature(top::OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::VariableExp)


def test_top::ocl::variableexp_constructor_exists():
    assert callable(top::OCL::VariableExp.__init__)


def test_top::ocl::variableexp_constructor_args():
    sig = inspect.signature(top::OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::TupleExp)


def test_top::ocl::tupleexp_constructor_exists():
    assert callable(top::OCL::TupleExp.__init__)


def test_top::ocl::tupleexp_constructor_args():
    sig = inspect.signature(top::OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::PropertyCallExp)


def test_top::ocl::propertycallexp_constructor_exists():
    assert callable(top::OCL::PropertyCallExp.__init__)


def test_top::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(top::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::MapExp)


def test_top::ocl::mapexp_constructor_exists():
    assert callable(top::OCL::MapExp.__init__)


def test_top::ocl::mapexp_constructor_args():
    sig = inspect.signature(top::OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::PrimitiveExp)


def test_top::ocl::primitiveexp_constructor_exists():
    assert callable(top::OCL::PrimitiveExp.__init__)


def test_top::ocl::primitiveexp_constructor_args():
    sig = inspect.signature(top::OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclUndefinedExp)


def test_top::ocl::oclundefinedexp_constructor_exists():
    assert callable(top::OCL::OclUndefinedExp.__init__)


def test_top::ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(top::OCL::OclUndefinedExp.__init__)
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



def test_top::atl::module_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Module)


def test_top::atl::module_constructor_exists():
    assert callable(top::ATL::Module.__init__)


def test_top::atl::module_constructor_args():
    sig = inspect.signature(top::ATL::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_top::atl::module_has_isRefining():
    assert hasattr(top::ATL::Module, "isRefining")
    descriptor = None
    for klass in top::ATL::Module.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::query_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Query)


def test_top::atl::query_constructor_exists():
    assert callable(top::ATL::Query.__init__)


def test_top::atl::query_constructor_args():
    sig = inspect.signature(top::ATL::Query.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::library_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Library)


def test_top::atl::library_constructor_exists():
    assert callable(top::ATL::Library.__init__)


def test_top::atl::library_constructor_args():
    sig = inspect.signature(top::ATL::Library.__init__)
    params = list(sig.parameters.keys())



def test_libraryref_is_not_abstract():
    assert not inspect.isabstract(LibraryRef)


def test_libraryref_constructor_exists():
    assert callable(LibraryRef.__init__)


def test_libraryref_constructor_args():
    sig = inspect.signature(LibraryRef.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::LocatedElement)


def test_top::atl::locatedelement_constructor_exists():
    assert callable(top::ATL::LocatedElement.__init__)


def test_top::atl::locatedelement_constructor_args():
    sig = inspect.signature(top::ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_top::atl::locatedelement_has_commentsAfter():
    assert hasattr(top::ATL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in top::ATL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::locatedelement_has_commentsBefore():
    assert hasattr(top::ATL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in top::ATL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::locatedelement_has_location():
    assert hasattr(top::ATL::LocatedElement, "location")
    descriptor = None
    for klass in top::ATL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::binding_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Binding)


def test_top::atl::binding_constructor_exists():
    assert callable(top::ATL::Binding.__init__)


def test_top::atl::binding_constructor_args():
    sig = inspect.signature(top::ATL::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_top::atl::binding_has_isAssignment():
    assert hasattr(top::ATL::Binding, "isAssignment")
    descriptor = None
    for klass in top::ATL::Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_top::atl::binding_has_propertyName():
    assert hasattr(top::ATL::Binding, "propertyName")
    descriptor = None
    for klass in top::ATL::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::inpattern_is_not_abstract():
    assert not inspect.isabstract(top::ATL::InPattern)


def test_top::atl::inpattern_constructor_exists():
    assert callable(top::ATL::InPattern.__init__)


def test_top::atl::inpattern_constructor_args():
    sig = inspect.signature(top::ATL::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclExpression)


def test_top::ocl::oclexpression_constructor_exists():
    assert callable(top::OCL::OclExpression.__init__)


def test_top::ocl::oclexpression_constructor_args():
    sig = inspect.signature(top::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::droppattern_is_not_abstract():
    assert not inspect.isabstract(top::ATL::DropPattern)


def test_top::atl::droppattern_constructor_exists():
    assert callable(top::ATL::DropPattern.__init__)


def test_top::atl::droppattern_constructor_args():
    sig = inspect.signature(top::ATL::DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(top::OCL::TupleTypeAttribute)


def test_top::ocl::tupletypeattribute_constructor_exists():
    assert callable(top::OCL::TupleTypeAttribute.__init__)


def test_top::ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(top::OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::tupletypeattribute_has_name():
    assert hasattr(top::OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in top::OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclFeature)


def test_top::ocl::oclfeature_constructor_exists():
    assert callable(top::OCL::OclFeature.__init__)


def test_top::ocl::oclfeature_constructor_args():
    sig = inspect.signature(top::OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclFeatureDefinition)


def test_top::ocl::oclfeaturedefinition_constructor_exists():
    assert callable(top::OCL::OclFeatureDefinition.__init__)


def test_top::ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(top::OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclModel)


def test_top::ocl::oclmodel_constructor_exists():
    assert callable(top::OCL::OclModel.__init__)


def test_top::ocl::oclmodel_constructor_args():
    sig = inspect.signature(top::OCL::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::ocl::oclmodel_has_name():
    assert hasattr(top::OCL::OclModel, "name")
    descriptor = None
    for klass in top::OCL::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(top::OCL::MapElement)


def test_top::ocl::mapelement_constructor_exists():
    assert callable(top::OCL::MapElement.__init__)


def test_top::ocl::mapelement_constructor_args():
    sig = inspect.signature(top::OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_top::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(top::OCL::VariableDeclaration)


def test_top::ocl::variabledeclaration_constructor_exists():
    assert callable(top::OCL::VariableDeclaration.__init__)


def test_top::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(top::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "id" in params, "Missing parameter 'id'"

def test_top::ocl::variabledeclaration_has_varName():
    assert hasattr(top::OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in top::OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_top::ocl::variabledeclaration_has_id():
    assert hasattr(top::OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in top::OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_top::ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(top::OCL::OclContextDefinition)


def test_top::ocl::oclcontextdefinition_constructor_exists():
    assert callable(top::OCL::OclContextDefinition.__init__)


def test_top::ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(top::OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::ModuleElement)


def test_top::atl::moduleelement_constructor_exists():
    assert callable(top::ATL::ModuleElement.__init__)


def test_top::atl::moduleelement_constructor_args():
    sig = inspect.signature(top::ATL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::actionblock_is_not_abstract():
    assert not inspect.isabstract(top::ATL::ActionBlock)


def test_top::atl::actionblock_constructor_exists():
    assert callable(top::ATL::ActionBlock.__init__)


def test_top::atl::actionblock_constructor_args():
    sig = inspect.signature(top::ATL::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::statement_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Statement)


def test_top::atl::statement_constructor_exists():
    assert callable(top::ATL::Statement.__init__)


def test_top::atl::statement_constructor_args():
    sig = inspect.signature(top::ATL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::libraryref_is_not_abstract():
    assert not inspect.isabstract(top::ATL::LibraryRef)


def test_top::atl::libraryref_constructor_exists():
    assert callable(top::ATL::LibraryRef.__init__)


def test_top::atl::libraryref_constructor_args():
    sig = inspect.signature(top::ATL::LibraryRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::atl::libraryref_has_name():
    assert hasattr(top::ATL::LibraryRef, "name")
    descriptor = None
    for klass in top::ATL::LibraryRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_top::atl::outpattern_is_not_abstract():
    assert not inspect.isabstract(top::ATL::OutPattern)


def test_top::atl::outpattern_constructor_exists():
    assert callable(top::ATL::OutPattern.__init__)


def test_top::atl::outpattern_constructor_args():
    sig = inspect.signature(top::ATL::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_top::atl::unit_is_not_abstract():
    assert not inspect.isabstract(top::ATL::Unit)


def test_top::atl::unit_constructor_exists():
    assert callable(top::ATL::Unit.__init__)


def test_top::atl::unit_constructor_args():
    sig = inspect.signature(top::ATL::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_top::atl::unit_has_name():
    assert hasattr(top::ATL::Unit, "name")
    descriptor = None
    for klass in top::ATL::Unit.__mro__:
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
OclModelElement_strategy = st.builds(
    OclModelElement,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
top::OCL::Attribute_strategy = st.builds(
    top::OCL::Attribute,
    name=
        safe_text
)
top::OCL::Operation_strategy = st.builds(
    top::OCL::Operation,
    name=
        safe_text
)
TupleType_strategy = st.builds(
    TupleType,
)
NumericType_strategy = st.builds(
    NumericType,
)
top::OCL::RealType_strategy = st.builds(
    top::OCL::RealType,
)
top::OCL::IntegerType_strategy = st.builds(
    top::OCL::IntegerType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
top::OCL::BagType_strategy = st.builds(
    top::OCL::BagType,
)
top::OCL::SequenceType_strategy = st.builds(
    top::OCL::SequenceType,
)
top::OCL::OrderedSetType_strategy = st.builds(
    top::OCL::OrderedSetType,
)
top::OCL::SetType_strategy = st.builds(
    top::OCL::SetType,
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
Primitive_strategy = st.builds(
    Primitive,
)
top::OCL::NumericType_strategy = st.builds(
    top::OCL::NumericType,
)
top::OCL::BooleanType_strategy = st.builds(
    top::OCL::BooleanType,
)
top::OCL::StringType_strategy = st.builds(
    top::OCL::StringType,
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
top::OCL::IntegerExp_strategy = st.builds(
    top::OCL::IntegerExp,
    integerSymbol=
        safe_text
)
top::OCL::RealExp_strategy = st.builds(
    top::OCL::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
top::OCL::NumericExp_strategy = st.builds(
    top::OCL::NumericExp,
)
top::OCL::BooleanExp_strategy = st.builds(
    top::OCL::BooleanExp,
    booleanSymbol=
        safe_text
)
top::OCL::StringExp_strategy = st.builds(
    top::OCL::StringExp,
    stringSymbol=
        safe_text
)
TupleExp_strategy = st.builds(
    TupleExp,
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
top::OCL::CollectionOperationCallExp_strategy = st.builds(
    top::OCL::CollectionOperationCallExp,
)
top::OCL::OperatorCallExp_strategy = st.builds(
    top::OCL::OperatorCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
top::OCL::IteratorExp_strategy = st.builds(
    top::OCL::IteratorExp,
    name=
        safe_text
)
top::OCL::IterateExp_strategy = st.builds(
    top::OCL::IterateExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
top::OCL::BagExp_strategy = st.builds(
    top::OCL::BagExp,
)
top::OCL::SequenceExp_strategy = st.builds(
    top::OCL::SequenceExp,
)
top::OCL::OrderedSetExp_strategy = st.builds(
    top::OCL::OrderedSetExp,
)
top::OCL::SetExp_strategy = st.builds(
    top::OCL::SetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
top::OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    top::OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
)
top::OCL::LoopExp_strategy = st.builds(
    top::OCL::LoopExp,
)
top::OCL::OperationCallExp_strategy = st.builds(
    top::OCL::OperationCallExp,
    operationName=
        safe_text
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
top::OCL::CollectionType_strategy = st.builds(
    top::OCL::CollectionType,
)
top::OCL::Primitive_strategy = st.builds(
    top::OCL::Primitive,
)
top::OCL::TupleType_strategy = st.builds(
    top::OCL::TupleType,
)
top::OCL::OclAnyType_strategy = st.builds(
    top::OCL::OclAnyType,
)
top::OCL::MapType_strategy = st.builds(
    top::OCL::MapType,
)
top::OCL::OclModelElement_strategy = st.builds(
    top::OCL::OclModelElement,
)
Statement_strategy = st.builds(
    Statement,
)
top::ATL::ExpressionStat_strategy = st.builds(
    top::ATL::ExpressionStat,
)
top::ATL::BindingStat_strategy = st.builds(
    top::ATL::BindingStat,
    isAssignment=
        safe_text,
    propertyName=
        safe_text
)
top::ATL::IfStat_strategy = st.builds(
    top::ATL::IfStat,
)
top::ATL::ForStat_strategy = st.builds(
    top::ATL::ForStat,
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
top::ATL::OutPatternElement_strategy = st.builds(
    top::ATL::OutPatternElement,
)
top::ATL::InPatternElement_strategy = st.builds(
    top::ATL::InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
top::OCL::TuplePart_strategy = st.builds(
    top::OCL::TuplePart,
)
top::OCL::Parameter_strategy = st.builds(
    top::OCL::Parameter,
)
top::OCL::Iterator_strategy = st.builds(
    top::OCL::Iterator,
)
top::ATL::RuleVariableDeclaration_strategy = st.builds(
    top::ATL::RuleVariableDeclaration,
)
top::ATL::PatternElement_strategy = st.builds(
    top::ATL::PatternElement,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
top::ATL::ForEachOutPatternElement_strategy = st.builds(
    top::ATL::ForEachOutPatternElement,
)
top::ATL::SimpleOutPatternElement_strategy = st.builds(
    top::ATL::SimpleOutPatternElement,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
top::ATL::SimpleInPatternElement_strategy = st.builds(
    top::ATL::SimpleInPatternElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
top::ATL::LazyMatchedRule_strategy = st.builds(
    top::ATL::LazyMatchedRule,
    isUnique=
        safe_text
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
top::ATL::CalledRule_strategy = st.builds(
    top::ATL::CalledRule,
    isEndpoint=
        safe_text,
    isEntrypoint=
        safe_text
)
top::ATL::MatchedRule_strategy = st.builds(
    top::ATL::MatchedRule,
    isNoDefault=
        safe_text,
    isRefining=
        safe_text,
    isAbstract=
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
top::ATL::Rule_strategy = st.builds(
    top::ATL::Rule,
    name=
        safe_text
)
top::ATL::Helper_strategy = st.builds(
    top::ATL::Helper,
)
OclModel_strategy = st.builds(
    OclModel,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
top::OCL::EnumLiteralExp_strategy = st.builds(
    top::OCL::EnumLiteralExp,
    name=
        safe_text
)
top::OCL::IfExp_strategy = st.builds(
    top::OCL::IfExp,
)
top::OCL::CollectionExp_strategy = st.builds(
    top::OCL::CollectionExp,
)
top::OCL::OclType_strategy = st.builds(
    top::OCL::OclType,
    name=
        safe_text
)
top::OCL::SuperExp_strategy = st.builds(
    top::OCL::SuperExp,
)
top::OCL::LetExp_strategy = st.builds(
    top::OCL::LetExp,
)
top::OCL::VariableExp_strategy = st.builds(
    top::OCL::VariableExp,
)
top::OCL::TupleExp_strategy = st.builds(
    top::OCL::TupleExp,
)
top::OCL::PropertyCallExp_strategy = st.builds(
    top::OCL::PropertyCallExp,
)
top::OCL::MapExp_strategy = st.builds(
    top::OCL::MapExp,
)
top::OCL::PrimitiveExp_strategy = st.builds(
    top::OCL::PrimitiveExp,
)
top::OCL::OclUndefinedExp_strategy = st.builds(
    top::OCL::OclUndefinedExp,
)
Helper_strategy = st.builds(
    Helper,
)
Unit_strategy = st.builds(
    Unit,
)
top::ATL::Module_strategy = st.builds(
    top::ATL::Module,
    isRefining=
        safe_text
)
top::ATL::Query_strategy = st.builds(
    top::ATL::Query,
)
top::ATL::Library_strategy = st.builds(
    top::ATL::Library,
)
LibraryRef_strategy = st.builds(
    LibraryRef,
)
top::ATL::LocatedElement_strategy = st.builds(
    top::ATL::LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
top::ATL::Binding_strategy = st.builds(
    top::ATL::Binding,
    isAssignment=
        safe_text,
    propertyName=
        safe_text
)
top::ATL::InPattern_strategy = st.builds(
    top::ATL::InPattern,
)
top::OCL::OclExpression_strategy = st.builds(
    top::OCL::OclExpression,
)
top::ATL::DropPattern_strategy = st.builds(
    top::ATL::DropPattern,
)
top::OCL::TupleTypeAttribute_strategy = st.builds(
    top::OCL::TupleTypeAttribute,
    name=
        safe_text
)
top::OCL::OclFeature_strategy = st.builds(
    top::OCL::OclFeature,
)
top::OCL::OclFeatureDefinition_strategy = st.builds(
    top::OCL::OclFeatureDefinition,
)
top::OCL::OclModel_strategy = st.builds(
    top::OCL::OclModel,
    name=
        safe_text
)
top::OCL::MapElement_strategy = st.builds(
    top::OCL::MapElement,
)
top::OCL::VariableDeclaration_strategy = st.builds(
    top::OCL::VariableDeclaration,
    varName=
        safe_text,
    id=
        safe_text
)
top::OCL::OclContextDefinition_strategy = st.builds(
    top::OCL::OclContextDefinition,
)
top::ATL::ModuleElement_strategy = st.builds(
    top::ATL::ModuleElement,
)
top::ATL::ActionBlock_strategy = st.builds(
    top::ATL::ActionBlock,
)
top::ATL::Statement_strategy = st.builds(
    top::ATL::Statement,
)
top::ATL::LibraryRef_strategy = st.builds(
    top::ATL::LibraryRef,
    name=
        safe_text
)
top::ATL::OutPattern_strategy = st.builds(
    top::ATL::OutPattern,
)
top::ATL::Unit_strategy = st.builds(
    top::ATL::Unit,
    name=
        safe_text
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=top::OCL::Attribute_strategy)
@settings(max_examples=50)
def test_top::ocl::attribute_instantiation(instance):
    assert isinstance(instance, top::OCL::Attribute)

@given(instance=top::OCL::Attribute_strategy)
def test_top::ocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::Attribute_strategy)
def test_top::ocl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::Operation_strategy)
@settings(max_examples=50)
def test_top::ocl::operation_instantiation(instance):
    assert isinstance(instance, top::OCL::Operation)

@given(instance=top::OCL::Operation_strategy)
def test_top::ocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::Operation_strategy)
def test_top::ocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=top::OCL::RealType_strategy)
@settings(max_examples=50)
def test_top::ocl::realtype_instantiation(instance):
    assert isinstance(instance, top::OCL::RealType)

@given(instance=top::OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_top::ocl::integertype_instantiation(instance):
    assert isinstance(instance, top::OCL::IntegerType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=top::OCL::BagType_strategy)
@settings(max_examples=50)
def test_top::ocl::bagtype_instantiation(instance):
    assert isinstance(instance, top::OCL::BagType)

@given(instance=top::OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_top::ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, top::OCL::SequenceType)

@given(instance=top::OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_top::ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, top::OCL::OrderedSetType)

@given(instance=top::OCL::SetType_strategy)
@settings(max_examples=50)
def test_top::ocl::settype_instantiation(instance):
    assert isinstance(instance, top::OCL::SetType)

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

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=top::OCL::NumericType_strategy)
@settings(max_examples=50)
def test_top::ocl::numerictype_instantiation(instance):
    assert isinstance(instance, top::OCL::NumericType)

@given(instance=top::OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_top::ocl::booleantype_instantiation(instance):
    assert isinstance(instance, top::OCL::BooleanType)

@given(instance=top::OCL::StringType_strategy)
@settings(max_examples=50)
def test_top::ocl::stringtype_instantiation(instance):
    assert isinstance(instance, top::OCL::StringType)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=top::OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_top::ocl::integerexp_instantiation(instance):
    assert isinstance(instance, top::OCL::IntegerExp)

@given(instance=top::OCL::IntegerExp_strategy)
def test_top::ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=top::OCL::IntegerExp_strategy)
def test_top::ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=top::OCL::RealExp_strategy)
@settings(max_examples=50)
def test_top::ocl::realexp_instantiation(instance):
    assert isinstance(instance, top::OCL::RealExp)

@given(instance=top::OCL::RealExp_strategy)
def test_top::ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=top::OCL::RealExp_strategy)
def test_top::ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=top::OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_top::ocl::numericexp_instantiation(instance):
    assert isinstance(instance, top::OCL::NumericExp)

@given(instance=top::OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_top::ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, top::OCL::BooleanExp)

@given(instance=top::OCL::BooleanExp_strategy)
def test_top::ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=top::OCL::BooleanExp_strategy)
def test_top::ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=top::OCL::StringExp_strategy)
@settings(max_examples=50)
def test_top::ocl::stringexp_instantiation(instance):
    assert isinstance(instance, top::OCL::StringExp)

@given(instance=top::OCL::StringExp_strategy)
def test_top::ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=top::OCL::StringExp_strategy)
def test_top::ocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

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

@given(instance=top::OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_top::ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, top::OCL::CollectionOperationCallExp)

@given(instance=top::OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_top::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, top::OCL::OperatorCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=top::OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_top::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, top::OCL::IteratorExp)

@given(instance=top::OCL::IteratorExp_strategy)
def test_top::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::IteratorExp_strategy)
def test_top::ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_top::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, top::OCL::IterateExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=top::OCL::BagExp_strategy)
@settings(max_examples=50)
def test_top::ocl::bagexp_instantiation(instance):
    assert isinstance(instance, top::OCL::BagExp)

@given(instance=top::OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_top::ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, top::OCL::SequenceExp)

@given(instance=top::OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_top::ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, top::OCL::OrderedSetExp)

@given(instance=top::OCL::SetExp_strategy)
@settings(max_examples=50)
def test_top::ocl::setexp_instantiation(instance):
    assert isinstance(instance, top::OCL::SetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=top::OCL::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_top::ocl::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, top::OCL::NavigationOrAttributeCallExp)

@given(instance=top::OCL::NavigationOrAttributeCallExp_strategy)
def test_top::ocl::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::NavigationOrAttributeCallExp_strategy)
def test_top::ocl::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_top::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, top::OCL::LoopExp)

@given(instance=top::OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_top::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, top::OCL::OperationCallExp)

@given(instance=top::OCL::OperationCallExp_strategy)
def test_top::ocl::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=top::OCL::OperationCallExp_strategy)
def test_top::ocl::operationcallexp_operationName_setter(instance):
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

@given(instance=top::OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_top::ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, top::OCL::CollectionType)

@given(instance=top::OCL::Primitive_strategy)
@settings(max_examples=50)
def test_top::ocl::primitive_instantiation(instance):
    assert isinstance(instance, top::OCL::Primitive)

@given(instance=top::OCL::TupleType_strategy)
@settings(max_examples=50)
def test_top::ocl::tupletype_instantiation(instance):
    assert isinstance(instance, top::OCL::TupleType)

@given(instance=top::OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_top::ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, top::OCL::OclAnyType)

@given(instance=top::OCL::MapType_strategy)
@settings(max_examples=50)
def test_top::ocl::maptype_instantiation(instance):
    assert isinstance(instance, top::OCL::MapType)

@given(instance=top::OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_top::ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, top::OCL::OclModelElement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=top::ATL::ExpressionStat_strategy)
@settings(max_examples=50)
def test_top::atl::expressionstat_instantiation(instance):
    assert isinstance(instance, top::ATL::ExpressionStat)

@given(instance=top::ATL::BindingStat_strategy)
@settings(max_examples=50)
def test_top::atl::bindingstat_instantiation(instance):
    assert isinstance(instance, top::ATL::BindingStat)

@given(instance=top::ATL::BindingStat_strategy)
def test_top::atl::bindingstat_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=top::ATL::BindingStat_strategy)
def test_top::atl::bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=top::ATL::BindingStat_strategy)
def test_top::atl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=top::ATL::BindingStat_strategy)
def test_top::atl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=top::ATL::IfStat_strategy)
@settings(max_examples=50)
def test_top::atl::ifstat_instantiation(instance):
    assert isinstance(instance, top::ATL::IfStat)

@given(instance=top::ATL::ForStat_strategy)
@settings(max_examples=50)
def test_top::atl::forstat_instantiation(instance):
    assert isinstance(instance, top::ATL::ForStat)

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

@given(instance=top::ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::OutPatternElement)

@given(instance=top::ATL::InPatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::inpatternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=top::OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_top::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, top::OCL::TuplePart)

@given(instance=top::OCL::Parameter_strategy)
@settings(max_examples=50)
def test_top::ocl::parameter_instantiation(instance):
    assert isinstance(instance, top::OCL::Parameter)

@given(instance=top::OCL::Iterator_strategy)
@settings(max_examples=50)
def test_top::ocl::iterator_instantiation(instance):
    assert isinstance(instance, top::OCL::Iterator)

@given(instance=top::ATL::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_top::atl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, top::ATL::RuleVariableDeclaration)

@given(instance=top::ATL::PatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::patternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::PatternElement)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=top::ATL::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::ForEachOutPatternElement)

@given(instance=top::ATL::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::SimpleOutPatternElement)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=top::ATL::SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_top::atl::simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, top::ATL::SimpleInPatternElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=top::ATL::LazyMatchedRule_strategy)
@settings(max_examples=50)
def test_top::atl::lazymatchedrule_instantiation(instance):
    assert isinstance(instance, top::ATL::LazyMatchedRule)

@given(instance=top::ATL::LazyMatchedRule_strategy)
def test_top::atl::lazymatchedrule_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=top::ATL::LazyMatchedRule_strategy)
def test_top::atl::lazymatchedrule_isUnique_setter(instance):
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

@given(instance=top::ATL::CalledRule_strategy)
@settings(max_examples=50)
def test_top::atl::calledrule_instantiation(instance):
    assert isinstance(instance, top::ATL::CalledRule)

@given(instance=top::ATL::CalledRule_strategy)
def test_top::atl::calledrule_isEndpoint_type(instance):
    assert isinstance(instance.isEndpoint, str)


@given(instance=top::ATL::CalledRule_strategy)
def test_top::atl::calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original

@given(instance=top::ATL::CalledRule_strategy)
def test_top::atl::calledrule_isEntrypoint_type(instance):
    assert isinstance(instance.isEntrypoint, str)


@given(instance=top::ATL::CalledRule_strategy)
def test_top::atl::calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=top::ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_top::atl::matchedrule_instantiation(instance):
    assert isinstance(instance, top::ATL::MatchedRule)

@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isNoDefault_type(instance):
    assert isinstance(instance.isNoDefault, str)


@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original

@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=top::ATL::MatchedRule_strategy)
def test_top::atl::matchedrule_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

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

@given(instance=top::ATL::Rule_strategy)
@settings(max_examples=50)
def test_top::atl::rule_instantiation(instance):
    assert isinstance(instance, top::ATL::Rule)

@given(instance=top::ATL::Rule_strategy)
def test_top::atl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::ATL::Rule_strategy)
def test_top::atl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::ATL::Helper_strategy)
@settings(max_examples=50)
def test_top::atl::helper_instantiation(instance):
    assert isinstance(instance, top::ATL::Helper)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=top::OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_top::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, top::OCL::EnumLiteralExp)

@given(instance=top::OCL::EnumLiteralExp_strategy)
def test_top::ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::EnumLiteralExp_strategy)
def test_top::ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::IfExp_strategy)
@settings(max_examples=50)
def test_top::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, top::OCL::IfExp)

@given(instance=top::OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_top::ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, top::OCL::CollectionExp)

@given(instance=top::OCL::OclType_strategy)
@settings(max_examples=50)
def test_top::ocl::ocltype_instantiation(instance):
    assert isinstance(instance, top::OCL::OclType)

@given(instance=top::OCL::OclType_strategy)
def test_top::ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::OclType_strategy)
def test_top::ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_top::ocl::superexp_instantiation(instance):
    assert isinstance(instance, top::OCL::SuperExp)

@given(instance=top::OCL::LetExp_strategy)
@settings(max_examples=50)
def test_top::ocl::letexp_instantiation(instance):
    assert isinstance(instance, top::OCL::LetExp)

@given(instance=top::OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_top::ocl::variableexp_instantiation(instance):
    assert isinstance(instance, top::OCL::VariableExp)

@given(instance=top::OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_top::ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, top::OCL::TupleExp)

@given(instance=top::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_top::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, top::OCL::PropertyCallExp)

@given(instance=top::OCL::MapExp_strategy)
@settings(max_examples=50)
def test_top::ocl::mapexp_instantiation(instance):
    assert isinstance(instance, top::OCL::MapExp)

@given(instance=top::OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_top::ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, top::OCL::PrimitiveExp)

@given(instance=top::OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_top::ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, top::OCL::OclUndefinedExp)

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=top::ATL::Module_strategy)
@settings(max_examples=50)
def test_top::atl::module_instantiation(instance):
    assert isinstance(instance, top::ATL::Module)

@given(instance=top::ATL::Module_strategy)
def test_top::atl::module_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=top::ATL::Module_strategy)
def test_top::atl::module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=top::ATL::Query_strategy)
@settings(max_examples=50)
def test_top::atl::query_instantiation(instance):
    assert isinstance(instance, top::ATL::Query)

@given(instance=top::ATL::Library_strategy)
@settings(max_examples=50)
def test_top::atl::library_instantiation(instance):
    assert isinstance(instance, top::ATL::Library)

@given(instance=LibraryRef_strategy)
@settings(max_examples=50)
def test_libraryref_instantiation(instance):
    assert isinstance(instance, LibraryRef)

@given(instance=top::ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_top::atl::locatedelement_instantiation(instance):
    assert isinstance(instance, top::ATL::LocatedElement)

@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=top::ATL::LocatedElement_strategy)
def test_top::atl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=top::ATL::Binding_strategy)
@settings(max_examples=50)
def test_top::atl::binding_instantiation(instance):
    assert isinstance(instance, top::ATL::Binding)

@given(instance=top::ATL::Binding_strategy)
def test_top::atl::binding_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=top::ATL::Binding_strategy)
def test_top::atl::binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=top::ATL::Binding_strategy)
def test_top::atl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=top::ATL::Binding_strategy)
def test_top::atl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=top::ATL::InPattern_strategy)
@settings(max_examples=50)
def test_top::atl::inpattern_instantiation(instance):
    assert isinstance(instance, top::ATL::InPattern)

@given(instance=top::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_top::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, top::OCL::OclExpression)

@given(instance=top::ATL::DropPattern_strategy)
@settings(max_examples=50)
def test_top::atl::droppattern_instantiation(instance):
    assert isinstance(instance, top::ATL::DropPattern)

@given(instance=top::OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_top::ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, top::OCL::TupleTypeAttribute)

@given(instance=top::OCL::TupleTypeAttribute_strategy)
def test_top::ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::TupleTypeAttribute_strategy)
def test_top::ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_top::ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, top::OCL::OclFeature)

@given(instance=top::OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_top::ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, top::OCL::OclFeatureDefinition)

@given(instance=top::OCL::OclModel_strategy)
@settings(max_examples=50)
def test_top::ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, top::OCL::OclModel)

@given(instance=top::OCL::OclModel_strategy)
def test_top::ocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::OCL::OclModel_strategy)
def test_top::ocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::OCL::MapElement_strategy)
@settings(max_examples=50)
def test_top::ocl::mapelement_instantiation(instance):
    assert isinstance(instance, top::OCL::MapElement)

@given(instance=top::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_top::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, top::OCL::VariableDeclaration)

@given(instance=top::OCL::VariableDeclaration_strategy)
def test_top::ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=top::OCL::VariableDeclaration_strategy)
def test_top::ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=top::OCL::VariableDeclaration_strategy)
def test_top::ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=top::OCL::VariableDeclaration_strategy)
def test_top::ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=top::OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_top::ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, top::OCL::OclContextDefinition)

@given(instance=top::ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_top::atl::moduleelement_instantiation(instance):
    assert isinstance(instance, top::ATL::ModuleElement)

@given(instance=top::ATL::ActionBlock_strategy)
@settings(max_examples=50)
def test_top::atl::actionblock_instantiation(instance):
    assert isinstance(instance, top::ATL::ActionBlock)

@given(instance=top::ATL::Statement_strategy)
@settings(max_examples=50)
def test_top::atl::statement_instantiation(instance):
    assert isinstance(instance, top::ATL::Statement)

@given(instance=top::ATL::LibraryRef_strategy)
@settings(max_examples=50)
def test_top::atl::libraryref_instantiation(instance):
    assert isinstance(instance, top::ATL::LibraryRef)

@given(instance=top::ATL::LibraryRef_strategy)
def test_top::atl::libraryref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::ATL::LibraryRef_strategy)
def test_top::atl::libraryref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=top::ATL::OutPattern_strategy)
@settings(max_examples=50)
def test_top::atl::outpattern_instantiation(instance):
    assert isinstance(instance, top::ATL::OutPattern)

@given(instance=top::ATL::Unit_strategy)
@settings(max_examples=50)
def test_top::atl::unit_instantiation(instance):
    assert isinstance(instance, top::ATL::Unit)

@given(instance=top::ATL::Unit_strategy)
def test_top::atl::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=top::ATL::Unit_strategy)
def test_top::atl::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
