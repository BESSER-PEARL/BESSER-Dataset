import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclModelElement,
    OclFeature,
    atlstatic::OCL::Operation,
    atlstatic::OCL::Attribute,
    MapType,
    TupleType,
    NumericType,
    atlstatic::OCL::RealType,
    atlstatic::OCL::IntegerType,
    Primitive,
    atlstatic::OCL::NumericType,
    atlstatic::OCL::BooleanType,
    atlstatic::OCL::StringType,
    TupleTypeAttribute,
    CollectionType,
    atlstatic::OCL::OrderedSetType,
    atlstatic::OCL::BagType,
    atlstatic::OCL::SequenceType,
    atlstatic::OCL::SetType,
    OclContextDefinition,
    VariableExp,
    IterateExp,
    TupleExp,
    TuplePart,
    MapExp,
    MapElement,
    OperationCallExp,
    atlstatic::OCL::OperatorCallExp,
    atlstatic::OCL::CollectionOperationCallExp,
    LoopExp,
    atlstatic::OCL::IteratorExp,
    atlstatic::OCL::IterateExp,
    LetExp,
    CollectionExp,
    atlstatic::OCL::OrderedSetExp,
    atlstatic::OCL::BagExp,
    atlstatic::OCL::SequenceExp,
    atlstatic::OCL::SetExp,
    PropertyCallExp,
    atlstatic::OCL::LoopExp,
    atlstatic::OCL::OperationCallExp,
    atlstatic::OCL::NavigationOrAttributeCallExp,
    IfExp,
    OclType,
    atlstatic::OCL::MapType,
    atlstatic::OCL::OclModelElement,
    atlstatic::OCL::CollectionType,
    atlstatic::OCL::TupleType,
    atlstatic::OCL::OclAnyType,
    atlstatic::OCL::Primitive,
    NumericExp,
    atlstatic::OCL::IntegerExp,
    atlstatic::OCL::RealExp,
    PrimitiveExp,
    atlstatic::OCL::BooleanExp,
    atlstatic::OCL::NumericExp,
    atlstatic::OCL::StringExp,
    Attribute,
    Operation,
    Statement,
    atlstatic::ATL::ForStat,
    atlstatic::ATL::IfStat,
    atlstatic::ATL::BindingStat,
    atlstatic::ATL::ExpressionStat,
    PatternElement,
    atlstatic::ATL::InPatternElement,
    VariableDeclaration,
    atlstatic::OCL::TuplePart,
    atlstatic::OCL::Parameter,
    atlstatic::ATL::RuleVariableDeclaration,
    atlstatic::OCL::Iterator,
    atlstatic::ATL::PatternElement,
    OutPatternElement,
    DropPattern,
    InPatternElement,
    Iterator,
    atlstatic::ATL::ForEachOutPatternElement,
    atlstatic::ATL::SimpleOutPatternElement,
    Binding,
    atlstatic::ATL::OutPatternElement,
    Helper,
    Unit,
    atlstatic::ATL::Library,
    LibraryRef,
    LocatedElement,
    atlstatic::ATL::DropPattern,
    atlstatic::OCL::VariableDeclaration,
    atlstatic::OCL::OclModel,
    atlstatic::ATL::Binding,
    atlstatic::OCL::OclExpression,
    atlstatic::OCL::OclFeature,
    atlstatic::ATL::LibraryRef,
    atlstatic::OCL::TupleTypeAttribute,
    atlstatic::ATL::ActionBlock,
    atlstatic::OCL::MapElement,
    atlstatic::OCL::OclContextDefinition,
    atlstatic::OCL::OclFeatureDefinition,
    atlstatic::ATL::InPattern,
    atlstatic::ATL::Statement,
    atlstatic::ATL::OutPattern,
    atlstatic::ATL::Unit,
    atlstatic::ATL::SimpleInPatternElement,
    RuleVariableDeclaration,
    ActionBlock,
    OutPattern,
    atlstatic::ATL::ContextHelper,
    ATL::ModuleCallable,
    ATL::Helper,
    atlstatic::ATL::StaticHelper,
    OclFeatureDefinition,
    Library,
    Query,
    ATL::Callable,
    ATL::ModuleElement,
    atlstatic::ATL::Helper,
    atlstatic::ATL::ModuleElement,
    ModuleElement,
    atlstatic::ATL::Rule,
    Parameter,
    StaticRule,
    atlstatic::ATL::CalledRule,
    ATL::StaticRule,
    ATL::RuleWithPattern,
    atlstatic::ATL::LazyRule,
    RuleWithPattern,
    atlstatic::ATL::MatchedRule,
    InPattern,
    Rule,
    atlstatic::ATL::RuleWithPattern,
    atlstatic::ATL::Callable,
    Callable,
    atlstatic::ATL::ModuleCallable,
    ATL::Rule,
    atlstatic::ATL::StaticRule,
    atlstatic::ATL::LocatedElement,
    OclModel,
    atlstatic::ATL::Module,
    OclExpression,
    atlstatic::OCL::PrimitiveExp,
    atlstatic::OCL::MapExp,
    atlstatic::OCL::CollectionExp,
    atlstatic::OCL::EnumLiteralExp,
    atlstatic::OCL::OclType,
    atlstatic::OCL::LetExp,
    atlstatic::OCL::TupleExp,
    atlstatic::OCL::PropertyCallExp,
    atlstatic::OCL::OclUndefinedExp,
    atlstatic::OCL::VariableExp,
    atlstatic::OCL::SuperExp,
    atlstatic::OCL::IfExp,
    atlstatic::ATL::Query,
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



def test_atlstatic::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::Operation)


def test_atlstatic::ocl::operation_constructor_exists():
    assert callable(atlstatic::OCL::Operation.__init__)


def test_atlstatic::ocl::operation_constructor_args():
    sig = inspect.signature(atlstatic::OCL::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::operation_has_name():
    assert hasattr(atlstatic::OCL::Operation, "name")
    descriptor = None
    for klass in atlstatic::OCL::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::Attribute)


def test_atlstatic::ocl::attribute_constructor_exists():
    assert callable(atlstatic::OCL::Attribute.__init__)


def test_atlstatic::ocl::attribute_constructor_args():
    sig = inspect.signature(atlstatic::OCL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::attribute_has_name():
    assert hasattr(atlstatic::OCL::Attribute, "name")
    descriptor = None
    for klass in atlstatic::OCL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
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



def test_atlstatic::ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::RealType)


def test_atlstatic::ocl::realtype_constructor_exists():
    assert callable(atlstatic::OCL::RealType.__init__)


def test_atlstatic::ocl::realtype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::IntegerType)


def test_atlstatic::ocl::integertype_constructor_exists():
    assert callable(atlstatic::OCL::IntegerType.__init__)


def test_atlstatic::ocl::integertype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::NumericType)


def test_atlstatic::ocl::numerictype_constructor_exists():
    assert callable(atlstatic::OCL::NumericType.__init__)


def test_atlstatic::ocl::numerictype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::BooleanType)


def test_atlstatic::ocl::booleantype_constructor_exists():
    assert callable(atlstatic::OCL::BooleanType.__init__)


def test_atlstatic::ocl::booleantype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::StringType)


def test_atlstatic::ocl::stringtype_constructor_exists():
    assert callable(atlstatic::OCL::StringType.__init__)


def test_atlstatic::ocl::stringtype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::StringType.__init__)
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



def test_atlstatic::ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OrderedSetType)


def test_atlstatic::ocl::orderedsettype_constructor_exists():
    assert callable(atlstatic::OCL::OrderedSetType.__init__)


def test_atlstatic::ocl::orderedsettype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::BagType)


def test_atlstatic::ocl::bagtype_constructor_exists():
    assert callable(atlstatic::OCL::BagType.__init__)


def test_atlstatic::ocl::bagtype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::SequenceType)


def test_atlstatic::ocl::sequencetype_constructor_exists():
    assert callable(atlstatic::OCL::SequenceType.__init__)


def test_atlstatic::ocl::sequencetype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::settype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::SetType)


def test_atlstatic::ocl::settype_constructor_exists():
    assert callable(atlstatic::OCL::SetType.__init__)


def test_atlstatic::ocl::settype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::SetType.__init__)
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



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OperatorCallExp)


def test_atlstatic::ocl::operatorcallexp_constructor_exists():
    assert callable(atlstatic::OCL::OperatorCallExp.__init__)


def test_atlstatic::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::CollectionOperationCallExp)


def test_atlstatic::ocl::collectionoperationcallexp_constructor_exists():
    assert callable(atlstatic::OCL::CollectionOperationCallExp.__init__)


def test_atlstatic::ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::IteratorExp)


def test_atlstatic::ocl::iteratorexp_constructor_exists():
    assert callable(atlstatic::OCL::IteratorExp.__init__)


def test_atlstatic::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::iteratorexp_has_name():
    assert hasattr(atlstatic::OCL::IteratorExp, "name")
    descriptor = None
    for klass in atlstatic::OCL::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::IterateExp)


def test_atlstatic::ocl::iterateexp_constructor_exists():
    assert callable(atlstatic::OCL::IterateExp.__init__)


def test_atlstatic::ocl::iterateexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::IterateExp.__init__)
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



def test_atlstatic::ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OrderedSetExp)


def test_atlstatic::ocl::orderedsetexp_constructor_exists():
    assert callable(atlstatic::OCL::OrderedSetExp.__init__)


def test_atlstatic::ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::BagExp)


def test_atlstatic::ocl::bagexp_constructor_exists():
    assert callable(atlstatic::OCL::BagExp.__init__)


def test_atlstatic::ocl::bagexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::SequenceExp)


def test_atlstatic::ocl::sequenceexp_constructor_exists():
    assert callable(atlstatic::OCL::SequenceExp.__init__)


def test_atlstatic::ocl::sequenceexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::SetExp)


def test_atlstatic::ocl::setexp_constructor_exists():
    assert callable(atlstatic::OCL::SetExp.__init__)


def test_atlstatic::ocl::setexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::LoopExp)


def test_atlstatic::ocl::loopexp_constructor_exists():
    assert callable(atlstatic::OCL::LoopExp.__init__)


def test_atlstatic::ocl::loopexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OperationCallExp)


def test_atlstatic::ocl::operationcallexp_constructor_exists():
    assert callable(atlstatic::OCL::OperationCallExp.__init__)


def test_atlstatic::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_atlstatic::ocl::operationcallexp_has_operationName():
    assert hasattr(atlstatic::OCL::OperationCallExp, "operationName")
    descriptor = None
    for klass in atlstatic::OCL::OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::NavigationOrAttributeCallExp)


def test_atlstatic::ocl::navigationorattributecallexp_constructor_exists():
    assert callable(atlstatic::OCL::NavigationOrAttributeCallExp.__init__)


def test_atlstatic::ocl::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::navigationorattributecallexp_has_name():
    assert hasattr(atlstatic::OCL::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in atlstatic::OCL::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_atlstatic::ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::MapType)


def test_atlstatic::ocl::maptype_constructor_exists():
    assert callable(atlstatic::OCL::MapType.__init__)


def test_atlstatic::ocl::maptype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclModelElement)


def test_atlstatic::ocl::oclmodelelement_constructor_exists():
    assert callable(atlstatic::OCL::OclModelElement.__init__)


def test_atlstatic::ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::CollectionType)


def test_atlstatic::ocl::collectiontype_constructor_exists():
    assert callable(atlstatic::OCL::CollectionType.__init__)


def test_atlstatic::ocl::collectiontype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::TupleType)


def test_atlstatic::ocl::tupletype_constructor_exists():
    assert callable(atlstatic::OCL::TupleType.__init__)


def test_atlstatic::ocl::tupletype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclAnyType)


def test_atlstatic::ocl::oclanytype_constructor_exists():
    assert callable(atlstatic::OCL::OclAnyType.__init__)


def test_atlstatic::ocl::oclanytype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::Primitive)


def test_atlstatic::ocl::primitive_constructor_exists():
    assert callable(atlstatic::OCL::Primitive.__init__)


def test_atlstatic::ocl::primitive_constructor_args():
    sig = inspect.signature(atlstatic::OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::IntegerExp)


def test_atlstatic::ocl::integerexp_constructor_exists():
    assert callable(atlstatic::OCL::IntegerExp.__init__)


def test_atlstatic::ocl::integerexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_atlstatic::ocl::integerexp_has_integerSymbol():
    assert hasattr(atlstatic::OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in atlstatic::OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::RealExp)


def test_atlstatic::ocl::realexp_constructor_exists():
    assert callable(atlstatic::OCL::RealExp.__init__)


def test_atlstatic::ocl::realexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_atlstatic::ocl::realexp_has_realSymbol():
    assert hasattr(atlstatic::OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in atlstatic::OCL::RealExp.__mro__:
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



def test_atlstatic::ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::BooleanExp)


def test_atlstatic::ocl::booleanexp_constructor_exists():
    assert callable(atlstatic::OCL::BooleanExp.__init__)


def test_atlstatic::ocl::booleanexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_atlstatic::ocl::booleanexp_has_booleanSymbol():
    assert hasattr(atlstatic::OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in atlstatic::OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::NumericExp)


def test_atlstatic::ocl::numericexp_constructor_exists():
    assert callable(atlstatic::OCL::NumericExp.__init__)


def test_atlstatic::ocl::numericexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::StringExp)


def test_atlstatic::ocl::stringexp_constructor_exists():
    assert callable(atlstatic::OCL::StringExp.__init__)


def test_atlstatic::ocl::stringexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_atlstatic::ocl::stringexp_has_stringSymbol():
    assert hasattr(atlstatic::OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in atlstatic::OCL::StringExp.__mro__:
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



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::forstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ForStat)


def test_atlstatic::atl::forstat_constructor_exists():
    assert callable(atlstatic::ATL::ForStat.__init__)


def test_atlstatic::atl::forstat_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ForStat.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::ifstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::IfStat)


def test_atlstatic::atl::ifstat_constructor_exists():
    assert callable(atlstatic::ATL::IfStat.__init__)


def test_atlstatic::atl::ifstat_constructor_args():
    sig = inspect.signature(atlstatic::ATL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::BindingStat)


def test_atlstatic::atl::bindingstat_constructor_exists():
    assert callable(atlstatic::ATL::BindingStat.__init__)


def test_atlstatic::atl::bindingstat_constructor_args():
    sig = inspect.signature(atlstatic::ATL::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_atlstatic::atl::bindingstat_has_isAssignment():
    assert hasattr(atlstatic::ATL::BindingStat, "isAssignment")
    descriptor = None
    for klass in atlstatic::ATL::BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::bindingstat_has_propertyName():
    assert hasattr(atlstatic::ATL::BindingStat, "propertyName")
    descriptor = None
    for klass in atlstatic::ATL::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::atl::expressionstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ExpressionStat)


def test_atlstatic::atl::expressionstat_constructor_exists():
    assert callable(atlstatic::ATL::ExpressionStat.__init__)


def test_atlstatic::atl::expressionstat_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_patternelement_is_not_abstract():
    assert not inspect.isabstract(PatternElement)


def test_patternelement_constructor_exists():
    assert callable(PatternElement.__init__)


def test_patternelement_constructor_args():
    sig = inspect.signature(PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::InPatternElement)


def test_atlstatic::atl::inpatternelement_constructor_exists():
    assert callable(atlstatic::ATL::InPatternElement.__init__)


def test_atlstatic::atl::inpatternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::TuplePart)


def test_atlstatic::ocl::tuplepart_constructor_exists():
    assert callable(atlstatic::OCL::TuplePart.__init__)


def test_atlstatic::ocl::tuplepart_constructor_args():
    sig = inspect.signature(atlstatic::OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::Parameter)


def test_atlstatic::ocl::parameter_constructor_exists():
    assert callable(atlstatic::OCL::Parameter.__init__)


def test_atlstatic::ocl::parameter_constructor_args():
    sig = inspect.signature(atlstatic::OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::RuleVariableDeclaration)


def test_atlstatic::atl::rulevariabledeclaration_constructor_exists():
    assert callable(atlstatic::ATL::RuleVariableDeclaration.__init__)


def test_atlstatic::atl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(atlstatic::ATL::RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::Iterator)


def test_atlstatic::ocl::iterator_constructor_exists():
    assert callable(atlstatic::OCL::Iterator.__init__)


def test_atlstatic::ocl::iterator_constructor_args():
    sig = inspect.signature(atlstatic::OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::patternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::PatternElement)


def test_atlstatic::atl::patternelement_constructor_exists():
    assert callable(atlstatic::ATL::PatternElement.__init__)


def test_atlstatic::atl::patternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
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



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ForEachOutPatternElement)


def test_atlstatic::atl::foreachoutpatternelement_constructor_exists():
    assert callable(atlstatic::ATL::ForEachOutPatternElement.__init__)


def test_atlstatic::atl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::SimpleOutPatternElement)


def test_atlstatic::atl::simpleoutpatternelement_constructor_exists():
    assert callable(atlstatic::ATL::SimpleOutPatternElement.__init__)


def test_atlstatic::atl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::OutPatternElement)


def test_atlstatic::atl::outpatternelement_constructor_exists():
    assert callable(atlstatic::ATL::OutPatternElement.__init__)


def test_atlstatic::atl::outpatternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::OutPatternElement.__init__)
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



def test_atlstatic::atl::library_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Library)


def test_atlstatic::atl::library_constructor_exists():
    assert callable(atlstatic::ATL::Library.__init__)


def test_atlstatic::atl::library_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Library.__init__)
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



def test_atlstatic::atl::droppattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::DropPattern)


def test_atlstatic::atl::droppattern_constructor_exists():
    assert callable(atlstatic::ATL::DropPattern.__init__)


def test_atlstatic::atl::droppattern_constructor_args():
    sig = inspect.signature(atlstatic::ATL::DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::VariableDeclaration)


def test_atlstatic::ocl::variabledeclaration_constructor_exists():
    assert callable(atlstatic::OCL::VariableDeclaration.__init__)


def test_atlstatic::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(atlstatic::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_atlstatic::ocl::variabledeclaration_has_id():
    assert hasattr(atlstatic::OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in atlstatic::OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::ocl::variabledeclaration_has_varName():
    assert hasattr(atlstatic::OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in atlstatic::OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclModel)


def test_atlstatic::ocl::oclmodel_constructor_exists():
    assert callable(atlstatic::OCL::OclModel.__init__)


def test_atlstatic::ocl::oclmodel_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::oclmodel_has_name():
    assert hasattr(atlstatic::OCL::OclModel, "name")
    descriptor = None
    for klass in atlstatic::OCL::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::atl::binding_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Binding)


def test_atlstatic::atl::binding_constructor_exists():
    assert callable(atlstatic::ATL::Binding.__init__)


def test_atlstatic::atl::binding_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atlstatic::atl::binding_has_propertyName():
    assert hasattr(atlstatic::ATL::Binding, "propertyName")
    descriptor = None
    for klass in atlstatic::ATL::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::binding_has_isAssignment():
    assert hasattr(atlstatic::ATL::Binding, "isAssignment")
    descriptor = None
    for klass in atlstatic::ATL::Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclExpression)


def test_atlstatic::ocl::oclexpression_constructor_exists():
    assert callable(atlstatic::OCL::OclExpression.__init__)


def test_atlstatic::ocl::oclexpression_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclFeature)


def test_atlstatic::ocl::oclfeature_constructor_exists():
    assert callable(atlstatic::OCL::OclFeature.__init__)


def test_atlstatic::ocl::oclfeature_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::libraryref_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::LibraryRef)


def test_atlstatic::atl::libraryref_constructor_exists():
    assert callable(atlstatic::ATL::LibraryRef.__init__)


def test_atlstatic::atl::libraryref_constructor_args():
    sig = inspect.signature(atlstatic::ATL::LibraryRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::atl::libraryref_has_name():
    assert hasattr(atlstatic::ATL::LibraryRef, "name")
    descriptor = None
    for klass in atlstatic::ATL::LibraryRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::TupleTypeAttribute)


def test_atlstatic::ocl::tupletypeattribute_constructor_exists():
    assert callable(atlstatic::OCL::TupleTypeAttribute.__init__)


def test_atlstatic::ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(atlstatic::OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::tupletypeattribute_has_name():
    assert hasattr(atlstatic::OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in atlstatic::OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::atl::actionblock_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ActionBlock)


def test_atlstatic::atl::actionblock_constructor_exists():
    assert callable(atlstatic::ATL::ActionBlock.__init__)


def test_atlstatic::atl::actionblock_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::MapElement)


def test_atlstatic::ocl::mapelement_constructor_exists():
    assert callable(atlstatic::OCL::MapElement.__init__)


def test_atlstatic::ocl::mapelement_constructor_args():
    sig = inspect.signature(atlstatic::OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclContextDefinition)


def test_atlstatic::ocl::oclcontextdefinition_constructor_exists():
    assert callable(atlstatic::OCL::OclContextDefinition.__init__)


def test_atlstatic::ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclFeatureDefinition)


def test_atlstatic::ocl::oclfeaturedefinition_constructor_exists():
    assert callable(atlstatic::OCL::OclFeatureDefinition.__init__)


def test_atlstatic::ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::inpattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::InPattern)


def test_atlstatic::atl::inpattern_constructor_exists():
    assert callable(atlstatic::ATL::InPattern.__init__)


def test_atlstatic::atl::inpattern_constructor_args():
    sig = inspect.signature(atlstatic::ATL::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::statement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Statement)


def test_atlstatic::atl::statement_constructor_exists():
    assert callable(atlstatic::ATL::Statement.__init__)


def test_atlstatic::atl::statement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::outpattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::OutPattern)


def test_atlstatic::atl::outpattern_constructor_exists():
    assert callable(atlstatic::ATL::OutPattern.__init__)


def test_atlstatic::atl::outpattern_constructor_args():
    sig = inspect.signature(atlstatic::ATL::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::unit_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Unit)


def test_atlstatic::atl::unit_constructor_exists():
    assert callable(atlstatic::ATL::Unit.__init__)


def test_atlstatic::atl::unit_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::atl::unit_has_name():
    assert hasattr(atlstatic::ATL::Unit, "name")
    descriptor = None
    for klass in atlstatic::ATL::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::atl::simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::SimpleInPatternElement)


def test_atlstatic::atl::simpleinpatternelement_constructor_exists():
    assert callable(atlstatic::ATL::SimpleInPatternElement.__init__)


def test_atlstatic::atl::simpleinpatternelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::SimpleInPatternElement.__init__)
    params = list(sig.parameters.keys())



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



def test_atlstatic::atl::contexthelper_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ContextHelper)


def test_atlstatic::atl::contexthelper_constructor_exists():
    assert callable(atlstatic::ATL::ContextHelper.__init__)


def test_atlstatic::atl::contexthelper_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_atl::modulecallable_is_not_abstract():
    assert not inspect.isabstract(ATL::ModuleCallable)


def test_atl::modulecallable_constructor_exists():
    assert callable(ATL::ModuleCallable.__init__)


def test_atl::modulecallable_constructor_args():
    sig = inspect.signature(ATL::ModuleCallable.__init__)
    params = list(sig.parameters.keys())



def test_atl::helper_is_not_abstract():
    assert not inspect.isabstract(ATL::Helper)


def test_atl::helper_constructor_exists():
    assert callable(ATL::Helper.__init__)


def test_atl::helper_constructor_args():
    sig = inspect.signature(ATL::Helper.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::statichelper_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::StaticHelper)


def test_atlstatic::atl::statichelper_constructor_exists():
    assert callable(atlstatic::ATL::StaticHelper.__init__)


def test_atlstatic::atl::statichelper_constructor_args():
    sig = inspect.signature(atlstatic::ATL::StaticHelper.__init__)
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



def test_atl::callable_is_not_abstract():
    assert not inspect.isabstract(ATL::Callable)


def test_atl::callable_constructor_exists():
    assert callable(ATL::Callable.__init__)


def test_atl::callable_constructor_args():
    sig = inspect.signature(ATL::Callable.__init__)
    params = list(sig.parameters.keys())



def test_atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(ATL::ModuleElement)


def test_atl::moduleelement_constructor_exists():
    assert callable(ATL::ModuleElement.__init__)


def test_atl::moduleelement_constructor_args():
    sig = inspect.signature(ATL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::helper_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Helper)


def test_atlstatic::atl::helper_constructor_exists():
    assert callable(atlstatic::ATL::Helper.__init__)


def test_atlstatic::atl::helper_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Helper.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ModuleElement)


def test_atlstatic::atl::moduleelement_constructor_exists():
    assert callable(atlstatic::ATL::ModuleElement.__init__)


def test_atlstatic::atl::moduleelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::rule_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Rule)


def test_atlstatic::atl::rule_constructor_exists():
    assert callable(atlstatic::ATL::Rule.__init__)


def test_atlstatic::atl::rule_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::atl::rule_has_name():
    assert hasattr(atlstatic::ATL::Rule, "name")
    descriptor = None
    for klass in atlstatic::ATL::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_staticrule_is_not_abstract():
    assert not inspect.isabstract(StaticRule)


def test_staticrule_constructor_exists():
    assert callable(StaticRule.__init__)


def test_staticrule_constructor_args():
    sig = inspect.signature(StaticRule.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::calledrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::CalledRule)


def test_atlstatic::atl::calledrule_constructor_exists():
    assert callable(atlstatic::ATL::CalledRule.__init__)


def test_atlstatic::atl::calledrule_constructor_args():
    sig = inspect.signature(atlstatic::ATL::CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"

def test_atlstatic::atl::calledrule_has_isEndpoint():
    assert hasattr(atlstatic::ATL::CalledRule, "isEndpoint")
    descriptor = None
    for klass in atlstatic::ATL::CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::calledrule_has_isEntrypoint():
    assert hasattr(atlstatic::ATL::CalledRule, "isEntrypoint")
    descriptor = None
    for klass in atlstatic::ATL::CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)



def test_atl::staticrule_is_not_abstract():
    assert not inspect.isabstract(ATL::StaticRule)


def test_atl::staticrule_constructor_exists():
    assert callable(ATL::StaticRule.__init__)


def test_atl::staticrule_constructor_args():
    sig = inspect.signature(ATL::StaticRule.__init__)
    params = list(sig.parameters.keys())



def test_atl::rulewithpattern_is_not_abstract():
    assert not inspect.isabstract(ATL::RuleWithPattern)


def test_atl::rulewithpattern_constructor_exists():
    assert callable(ATL::RuleWithPattern.__init__)


def test_atl::rulewithpattern_constructor_args():
    sig = inspect.signature(ATL::RuleWithPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::lazyrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::LazyRule)


def test_atlstatic::atl::lazyrule_constructor_exists():
    assert callable(atlstatic::ATL::LazyRule.__init__)


def test_atlstatic::atl::lazyrule_constructor_args():
    sig = inspect.signature(atlstatic::ATL::LazyRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_atlstatic::atl::lazyrule_has_isUnique():
    assert hasattr(atlstatic::ATL::LazyRule, "isUnique")
    descriptor = None
    for klass in atlstatic::ATL::LazyRule.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_rulewithpattern_is_not_abstract():
    assert not inspect.isabstract(RuleWithPattern)


def test_rulewithpattern_constructor_exists():
    assert callable(RuleWithPattern.__init__)


def test_rulewithpattern_constructor_args():
    sig = inspect.signature(RuleWithPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::MatchedRule)


def test_atlstatic::atl::matchedrule_constructor_exists():
    assert callable(atlstatic::ATL::MatchedRule.__init__)


def test_atlstatic::atl::matchedrule_constructor_args():
    sig = inspect.signature(atlstatic::ATL::MatchedRule.__init__)
    params = list(sig.parameters.keys())



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



def test_atlstatic::atl::rulewithpattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::RuleWithPattern)


def test_atlstatic::atl::rulewithpattern_constructor_exists():
    assert callable(atlstatic::ATL::RuleWithPattern.__init__)


def test_atlstatic::atl::rulewithpattern_constructor_args():
    sig = inspect.signature(atlstatic::ATL::RuleWithPattern.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isRefining" in params, "Missing parameter 'isRefining'"
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"

def test_atlstatic::atl::rulewithpattern_has_isAbstract():
    assert hasattr(atlstatic::ATL::RuleWithPattern, "isAbstract")
    descriptor = None
    for klass in atlstatic::ATL::RuleWithPattern.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::rulewithpattern_has_isRefining():
    assert hasattr(atlstatic::ATL::RuleWithPattern, "isRefining")
    descriptor = None
    for klass in atlstatic::ATL::RuleWithPattern.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::rulewithpattern_has_isNoDefault():
    assert hasattr(atlstatic::ATL::RuleWithPattern, "isNoDefault")
    descriptor = None
    for klass in atlstatic::ATL::RuleWithPattern.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::atl::callable_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Callable)


def test_atlstatic::atl::callable_constructor_exists():
    assert callable(atlstatic::ATL::Callable.__init__)


def test_atlstatic::atl::callable_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Callable.__init__)
    params = list(sig.parameters.keys())



def test_callable_is_not_abstract():
    assert not inspect.isabstract(Callable)


def test_callable_constructor_exists():
    assert callable(Callable.__init__)


def test_callable_constructor_args():
    sig = inspect.signature(Callable.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::modulecallable_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::ModuleCallable)


def test_atlstatic::atl::modulecallable_constructor_exists():
    assert callable(atlstatic::ATL::ModuleCallable.__init__)


def test_atlstatic::atl::modulecallable_constructor_args():
    sig = inspect.signature(atlstatic::ATL::ModuleCallable.__init__)
    params = list(sig.parameters.keys())



def test_atl::rule_is_not_abstract():
    assert not inspect.isabstract(ATL::Rule)


def test_atl::rule_constructor_exists():
    assert callable(ATL::Rule.__init__)


def test_atl::rule_constructor_args():
    sig = inspect.signature(ATL::Rule.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::staticrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::StaticRule)


def test_atlstatic::atl::staticrule_constructor_exists():
    assert callable(atlstatic::ATL::StaticRule.__init__)


def test_atlstatic::atl::staticrule_constructor_args():
    sig = inspect.signature(atlstatic::ATL::StaticRule.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::LocatedElement)


def test_atlstatic::atl::locatedelement_constructor_exists():
    assert callable(atlstatic::ATL::LocatedElement.__init__)


def test_atlstatic::atl::locatedelement_constructor_args():
    sig = inspect.signature(atlstatic::ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_atlstatic::atl::locatedelement_has_commentsBefore():
    assert hasattr(atlstatic::ATL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in atlstatic::ATL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::locatedelement_has_location():
    assert hasattr(atlstatic::ATL::LocatedElement, "location")
    descriptor = None
    for klass in atlstatic::ATL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic::atl::locatedelement_has_commentsAfter():
    assert hasattr(atlstatic::ATL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in atlstatic::ATL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::module_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Module)


def test_atlstatic::atl::module_constructor_exists():
    assert callable(atlstatic::ATL::Module.__init__)


def test_atlstatic::atl::module_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atlstatic::atl::module_has_isRefining():
    assert hasattr(atlstatic::ATL::Module, "isRefining")
    descriptor = None
    for klass in atlstatic::ATL::Module.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::PrimitiveExp)


def test_atlstatic::ocl::primitiveexp_constructor_exists():
    assert callable(atlstatic::OCL::PrimitiveExp.__init__)


def test_atlstatic::ocl::primitiveexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::MapExp)


def test_atlstatic::ocl::mapexp_constructor_exists():
    assert callable(atlstatic::OCL::MapExp.__init__)


def test_atlstatic::ocl::mapexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::CollectionExp)


def test_atlstatic::ocl::collectionexp_constructor_exists():
    assert callable(atlstatic::OCL::CollectionExp.__init__)


def test_atlstatic::ocl::collectionexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::EnumLiteralExp)


def test_atlstatic::ocl::enumliteralexp_constructor_exists():
    assert callable(atlstatic::OCL::EnumLiteralExp.__init__)


def test_atlstatic::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::enumliteralexp_has_name():
    assert hasattr(atlstatic::OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in atlstatic::OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclType)


def test_atlstatic::ocl::ocltype_constructor_exists():
    assert callable(atlstatic::OCL::OclType.__init__)


def test_atlstatic::ocl::ocltype_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic::ocl::ocltype_has_name():
    assert hasattr(atlstatic::OCL::OclType, "name")
    descriptor = None
    for klass in atlstatic::OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::LetExp)


def test_atlstatic::ocl::letexp_constructor_exists():
    assert callable(atlstatic::OCL::LetExp.__init__)


def test_atlstatic::ocl::letexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::TupleExp)


def test_atlstatic::ocl::tupleexp_constructor_exists():
    assert callable(atlstatic::OCL::TupleExp.__init__)


def test_atlstatic::ocl::tupleexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::PropertyCallExp)


def test_atlstatic::ocl::propertycallexp_constructor_exists():
    assert callable(atlstatic::OCL::PropertyCallExp.__init__)


def test_atlstatic::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::OclUndefinedExp)


def test_atlstatic::ocl::oclundefinedexp_constructor_exists():
    assert callable(atlstatic::OCL::OclUndefinedExp.__init__)


def test_atlstatic::ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::VariableExp)


def test_atlstatic::ocl::variableexp_constructor_exists():
    assert callable(atlstatic::OCL::VariableExp.__init__)


def test_atlstatic::ocl::variableexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::SuperExp)


def test_atlstatic::ocl::superexp_constructor_exists():
    assert callable(atlstatic::OCL::SuperExp.__init__)


def test_atlstatic::ocl::superexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic::OCL::IfExp)


def test_atlstatic::ocl::ifexp_constructor_exists():
    assert callable(atlstatic::OCL::IfExp.__init__)


def test_atlstatic::ocl::ifexp_constructor_args():
    sig = inspect.signature(atlstatic::OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic::atl::query_is_not_abstract():
    assert not inspect.isabstract(atlstatic::ATL::Query)


def test_atlstatic::atl::query_constructor_exists():
    assert callable(atlstatic::ATL::Query.__init__)


def test_atlstatic::atl::query_constructor_args():
    sig = inspect.signature(atlstatic::ATL::Query.__init__)
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
OclFeature_strategy = st.builds(
    OclFeature,
)
atlstatic::OCL::Operation_strategy = st.builds(
    atlstatic::OCL::Operation,
    name=
        safe_text
)
atlstatic::OCL::Attribute_strategy = st.builds(
    atlstatic::OCL::Attribute,
    name=
        safe_text
)
MapType_strategy = st.builds(
    MapType,
)
TupleType_strategy = st.builds(
    TupleType,
)
NumericType_strategy = st.builds(
    NumericType,
)
atlstatic::OCL::RealType_strategy = st.builds(
    atlstatic::OCL::RealType,
)
atlstatic::OCL::IntegerType_strategy = st.builds(
    atlstatic::OCL::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
atlstatic::OCL::NumericType_strategy = st.builds(
    atlstatic::OCL::NumericType,
)
atlstatic::OCL::BooleanType_strategy = st.builds(
    atlstatic::OCL::BooleanType,
)
atlstatic::OCL::StringType_strategy = st.builds(
    atlstatic::OCL::StringType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
atlstatic::OCL::OrderedSetType_strategy = st.builds(
    atlstatic::OCL::OrderedSetType,
)
atlstatic::OCL::BagType_strategy = st.builds(
    atlstatic::OCL::BagType,
)
atlstatic::OCL::SequenceType_strategy = st.builds(
    atlstatic::OCL::SequenceType,
)
atlstatic::OCL::SetType_strategy = st.builds(
    atlstatic::OCL::SetType,
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
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
atlstatic::OCL::OperatorCallExp_strategy = st.builds(
    atlstatic::OCL::OperatorCallExp,
)
atlstatic::OCL::CollectionOperationCallExp_strategy = st.builds(
    atlstatic::OCL::CollectionOperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
atlstatic::OCL::IteratorExp_strategy = st.builds(
    atlstatic::OCL::IteratorExp,
    name=
        safe_text
)
atlstatic::OCL::IterateExp_strategy = st.builds(
    atlstatic::OCL::IterateExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
atlstatic::OCL::OrderedSetExp_strategy = st.builds(
    atlstatic::OCL::OrderedSetExp,
)
atlstatic::OCL::BagExp_strategy = st.builds(
    atlstatic::OCL::BagExp,
)
atlstatic::OCL::SequenceExp_strategy = st.builds(
    atlstatic::OCL::SequenceExp,
)
atlstatic::OCL::SetExp_strategy = st.builds(
    atlstatic::OCL::SetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
atlstatic::OCL::LoopExp_strategy = st.builds(
    atlstatic::OCL::LoopExp,
)
atlstatic::OCL::OperationCallExp_strategy = st.builds(
    atlstatic::OCL::OperationCallExp,
    operationName=
        safe_text
)
atlstatic::OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    atlstatic::OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
atlstatic::OCL::MapType_strategy = st.builds(
    atlstatic::OCL::MapType,
)
atlstatic::OCL::OclModelElement_strategy = st.builds(
    atlstatic::OCL::OclModelElement,
)
atlstatic::OCL::CollectionType_strategy = st.builds(
    atlstatic::OCL::CollectionType,
)
atlstatic::OCL::TupleType_strategy = st.builds(
    atlstatic::OCL::TupleType,
)
atlstatic::OCL::OclAnyType_strategy = st.builds(
    atlstatic::OCL::OclAnyType,
)
atlstatic::OCL::Primitive_strategy = st.builds(
    atlstatic::OCL::Primitive,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
atlstatic::OCL::IntegerExp_strategy = st.builds(
    atlstatic::OCL::IntegerExp,
    integerSymbol=
        safe_text
)
atlstatic::OCL::RealExp_strategy = st.builds(
    atlstatic::OCL::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
atlstatic::OCL::BooleanExp_strategy = st.builds(
    atlstatic::OCL::BooleanExp,
    booleanSymbol=
        safe_text
)
atlstatic::OCL::NumericExp_strategy = st.builds(
    atlstatic::OCL::NumericExp,
)
atlstatic::OCL::StringExp_strategy = st.builds(
    atlstatic::OCL::StringExp,
    stringSymbol=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
Statement_strategy = st.builds(
    Statement,
)
atlstatic::ATL::ForStat_strategy = st.builds(
    atlstatic::ATL::ForStat,
)
atlstatic::ATL::IfStat_strategy = st.builds(
    atlstatic::ATL::IfStat,
)
atlstatic::ATL::BindingStat_strategy = st.builds(
    atlstatic::ATL::BindingStat,
    isAssignment=
        safe_text,
    propertyName=
        safe_text
)
atlstatic::ATL::ExpressionStat_strategy = st.builds(
    atlstatic::ATL::ExpressionStat,
)
PatternElement_strategy = st.builds(
    PatternElement,
)
atlstatic::ATL::InPatternElement_strategy = st.builds(
    atlstatic::ATL::InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
atlstatic::OCL::TuplePart_strategy = st.builds(
    atlstatic::OCL::TuplePart,
)
atlstatic::OCL::Parameter_strategy = st.builds(
    atlstatic::OCL::Parameter,
)
atlstatic::ATL::RuleVariableDeclaration_strategy = st.builds(
    atlstatic::ATL::RuleVariableDeclaration,
)
atlstatic::OCL::Iterator_strategy = st.builds(
    atlstatic::OCL::Iterator,
)
atlstatic::ATL::PatternElement_strategy = st.builds(
    atlstatic::ATL::PatternElement,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
Iterator_strategy = st.builds(
    Iterator,
)
atlstatic::ATL::ForEachOutPatternElement_strategy = st.builds(
    atlstatic::ATL::ForEachOutPatternElement,
)
atlstatic::ATL::SimpleOutPatternElement_strategy = st.builds(
    atlstatic::ATL::SimpleOutPatternElement,
)
Binding_strategy = st.builds(
    Binding,
)
atlstatic::ATL::OutPatternElement_strategy = st.builds(
    atlstatic::ATL::OutPatternElement,
)
Helper_strategy = st.builds(
    Helper,
)
Unit_strategy = st.builds(
    Unit,
)
atlstatic::ATL::Library_strategy = st.builds(
    atlstatic::ATL::Library,
)
LibraryRef_strategy = st.builds(
    LibraryRef,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
atlstatic::ATL::DropPattern_strategy = st.builds(
    atlstatic::ATL::DropPattern,
)
atlstatic::OCL::VariableDeclaration_strategy = st.builds(
    atlstatic::OCL::VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
atlstatic::OCL::OclModel_strategy = st.builds(
    atlstatic::OCL::OclModel,
    name=
        safe_text
)
atlstatic::ATL::Binding_strategy = st.builds(
    atlstatic::ATL::Binding,
    propertyName=
        safe_text,
    isAssignment=
        safe_text
)
atlstatic::OCL::OclExpression_strategy = st.builds(
    atlstatic::OCL::OclExpression,
)
atlstatic::OCL::OclFeature_strategy = st.builds(
    atlstatic::OCL::OclFeature,
)
atlstatic::ATL::LibraryRef_strategy = st.builds(
    atlstatic::ATL::LibraryRef,
    name=
        safe_text
)
atlstatic::OCL::TupleTypeAttribute_strategy = st.builds(
    atlstatic::OCL::TupleTypeAttribute,
    name=
        safe_text
)
atlstatic::ATL::ActionBlock_strategy = st.builds(
    atlstatic::ATL::ActionBlock,
)
atlstatic::OCL::MapElement_strategy = st.builds(
    atlstatic::OCL::MapElement,
)
atlstatic::OCL::OclContextDefinition_strategy = st.builds(
    atlstatic::OCL::OclContextDefinition,
)
atlstatic::OCL::OclFeatureDefinition_strategy = st.builds(
    atlstatic::OCL::OclFeatureDefinition,
)
atlstatic::ATL::InPattern_strategy = st.builds(
    atlstatic::ATL::InPattern,
)
atlstatic::ATL::Statement_strategy = st.builds(
    atlstatic::ATL::Statement,
)
atlstatic::ATL::OutPattern_strategy = st.builds(
    atlstatic::ATL::OutPattern,
)
atlstatic::ATL::Unit_strategy = st.builds(
    atlstatic::ATL::Unit,
    name=
        safe_text
)
atlstatic::ATL::SimpleInPatternElement_strategy = st.builds(
    atlstatic::ATL::SimpleInPatternElement,
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
atlstatic::ATL::ContextHelper_strategy = st.builds(
    atlstatic::ATL::ContextHelper,
)
ATL::ModuleCallable_strategy = st.builds(
    ATL::ModuleCallable,
)
ATL::Helper_strategy = st.builds(
    ATL::Helper,
)
atlstatic::ATL::StaticHelper_strategy = st.builds(
    atlstatic::ATL::StaticHelper,
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
ATL::Callable_strategy = st.builds(
    ATL::Callable,
)
ATL::ModuleElement_strategy = st.builds(
    ATL::ModuleElement,
)
atlstatic::ATL::Helper_strategy = st.builds(
    atlstatic::ATL::Helper,
)
atlstatic::ATL::ModuleElement_strategy = st.builds(
    atlstatic::ATL::ModuleElement,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
atlstatic::ATL::Rule_strategy = st.builds(
    atlstatic::ATL::Rule,
    name=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
StaticRule_strategy = st.builds(
    StaticRule,
)
atlstatic::ATL::CalledRule_strategy = st.builds(
    atlstatic::ATL::CalledRule,
    isEndpoint=
        safe_text,
    isEntrypoint=
        safe_text
)
ATL::StaticRule_strategy = st.builds(
    ATL::StaticRule,
)
ATL::RuleWithPattern_strategy = st.builds(
    ATL::RuleWithPattern,
)
atlstatic::ATL::LazyRule_strategy = st.builds(
    atlstatic::ATL::LazyRule,
    isUnique=
        safe_text
)
RuleWithPattern_strategy = st.builds(
    RuleWithPattern,
)
atlstatic::ATL::MatchedRule_strategy = st.builds(
    atlstatic::ATL::MatchedRule,
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
atlstatic::ATL::RuleWithPattern_strategy = st.builds(
    atlstatic::ATL::RuleWithPattern,
    isAbstract=
        safe_text,
    isRefining=
        safe_text,
    isNoDefault=
        safe_text
)
atlstatic::ATL::Callable_strategy = st.builds(
    atlstatic::ATL::Callable,
)
Callable_strategy = st.builds(
    Callable,
)
atlstatic::ATL::ModuleCallable_strategy = st.builds(
    atlstatic::ATL::ModuleCallable,
)
ATL::Rule_strategy = st.builds(
    ATL::Rule,
)
atlstatic::ATL::StaticRule_strategy = st.builds(
    atlstatic::ATL::StaticRule,
)
atlstatic::ATL::LocatedElement_strategy = st.builds(
    atlstatic::ATL::LocatedElement,
    commentsBefore=
        safe_text,
    location=
        safe_text,
    commentsAfter=
        safe_text
)
OclModel_strategy = st.builds(
    OclModel,
)
atlstatic::ATL::Module_strategy = st.builds(
    atlstatic::ATL::Module,
    isRefining=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atlstatic::OCL::PrimitiveExp_strategy = st.builds(
    atlstatic::OCL::PrimitiveExp,
)
atlstatic::OCL::MapExp_strategy = st.builds(
    atlstatic::OCL::MapExp,
)
atlstatic::OCL::CollectionExp_strategy = st.builds(
    atlstatic::OCL::CollectionExp,
)
atlstatic::OCL::EnumLiteralExp_strategy = st.builds(
    atlstatic::OCL::EnumLiteralExp,
    name=
        safe_text
)
atlstatic::OCL::OclType_strategy = st.builds(
    atlstatic::OCL::OclType,
    name=
        safe_text
)
atlstatic::OCL::LetExp_strategy = st.builds(
    atlstatic::OCL::LetExp,
)
atlstatic::OCL::TupleExp_strategy = st.builds(
    atlstatic::OCL::TupleExp,
)
atlstatic::OCL::PropertyCallExp_strategy = st.builds(
    atlstatic::OCL::PropertyCallExp,
)
atlstatic::OCL::OclUndefinedExp_strategy = st.builds(
    atlstatic::OCL::OclUndefinedExp,
)
atlstatic::OCL::VariableExp_strategy = st.builds(
    atlstatic::OCL::VariableExp,
)
atlstatic::OCL::SuperExp_strategy = st.builds(
    atlstatic::OCL::SuperExp,
)
atlstatic::OCL::IfExp_strategy = st.builds(
    atlstatic::OCL::IfExp,
)
atlstatic::ATL::Query_strategy = st.builds(
    atlstatic::ATL::Query,
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=atlstatic::OCL::Operation_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::operation_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::Operation)

@given(instance=atlstatic::OCL::Operation_strategy)
def test_atlstatic::ocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::Operation_strategy)
def test_atlstatic::ocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::OCL::Attribute_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::attribute_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::Attribute)

@given(instance=atlstatic::OCL::Attribute_strategy)
def test_atlstatic::ocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::Attribute_strategy)
def test_atlstatic::ocl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=atlstatic::OCL::RealType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::realtype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::RealType)

@given(instance=atlstatic::OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::integertype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=atlstatic::OCL::NumericType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::numerictype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::NumericType)

@given(instance=atlstatic::OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::booleantype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::BooleanType)

@given(instance=atlstatic::OCL::StringType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::stringtype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::StringType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=atlstatic::OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OrderedSetType)

@given(instance=atlstatic::OCL::BagType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::bagtype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::BagType)

@given(instance=atlstatic::OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::SequenceType)

@given(instance=atlstatic::OCL::SetType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::settype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::SetType)

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

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=atlstatic::OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OperatorCallExp)

@given(instance=atlstatic::OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::CollectionOperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=atlstatic::OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::IteratorExp)

@given(instance=atlstatic::OCL::IteratorExp_strategy)
def test_atlstatic::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::IteratorExp_strategy)
def test_atlstatic::ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::IterateExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=atlstatic::OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OrderedSetExp)

@given(instance=atlstatic::OCL::BagExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::bagexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::BagExp)

@given(instance=atlstatic::OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::SequenceExp)

@given(instance=atlstatic::OCL::SetExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::setexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::SetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=atlstatic::OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::LoopExp)

@given(instance=atlstatic::OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OperationCallExp)

@given(instance=atlstatic::OCL::OperationCallExp_strategy)
def test_atlstatic::ocl::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=atlstatic::OCL::OperationCallExp_strategy)
def test_atlstatic::ocl::operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=atlstatic::OCL::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::NavigationOrAttributeCallExp)

@given(instance=atlstatic::OCL::NavigationOrAttributeCallExp_strategy)
def test_atlstatic::ocl::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::NavigationOrAttributeCallExp_strategy)
def test_atlstatic::ocl::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=atlstatic::OCL::MapType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::maptype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::MapType)

@given(instance=atlstatic::OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclModelElement)

@given(instance=atlstatic::OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::CollectionType)

@given(instance=atlstatic::OCL::TupleType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::tupletype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::TupleType)

@given(instance=atlstatic::OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclAnyType)

@given(instance=atlstatic::OCL::Primitive_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::primitive_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::Primitive)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=atlstatic::OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::integerexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::IntegerExp)

@given(instance=atlstatic::OCL::IntegerExp_strategy)
def test_atlstatic::ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=atlstatic::OCL::IntegerExp_strategy)
def test_atlstatic::ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=atlstatic::OCL::RealExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::realexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::RealExp)

@given(instance=atlstatic::OCL::RealExp_strategy)
def test_atlstatic::ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=atlstatic::OCL::RealExp_strategy)
def test_atlstatic::ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=atlstatic::OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::BooleanExp)

@given(instance=atlstatic::OCL::BooleanExp_strategy)
def test_atlstatic::ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=atlstatic::OCL::BooleanExp_strategy)
def test_atlstatic::ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=atlstatic::OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::numericexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::NumericExp)

@given(instance=atlstatic::OCL::StringExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::stringexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::StringExp)

@given(instance=atlstatic::OCL::StringExp_strategy)
def test_atlstatic::ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=atlstatic::OCL::StringExp_strategy)
def test_atlstatic::ocl::stringexp_stringSymbol_setter(instance):
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

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=atlstatic::ATL::ForStat_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::forstat_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ForStat)

@given(instance=atlstatic::ATL::IfStat_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::ifstat_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::IfStat)

@given(instance=atlstatic::ATL::BindingStat_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::bindingstat_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::BindingStat)

@given(instance=atlstatic::ATL::BindingStat_strategy)
def test_atlstatic::atl::bindingstat_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=atlstatic::ATL::BindingStat_strategy)
def test_atlstatic::atl::bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atlstatic::ATL::BindingStat_strategy)
def test_atlstatic::atl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atlstatic::ATL::BindingStat_strategy)
def test_atlstatic::atl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atlstatic::ATL::ExpressionStat_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::expressionstat_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ExpressionStat)

@given(instance=PatternElement_strategy)
@settings(max_examples=50)
def test_patternelement_instantiation(instance):
    assert isinstance(instance, PatternElement)

@given(instance=atlstatic::ATL::InPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::inpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=atlstatic::OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::TuplePart)

@given(instance=atlstatic::OCL::Parameter_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::parameter_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::Parameter)

@given(instance=atlstatic::ATL::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::RuleVariableDeclaration)

@given(instance=atlstatic::OCL::Iterator_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::iterator_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::Iterator)

@given(instance=atlstatic::ATL::PatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::patternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::PatternElement)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=atlstatic::ATL::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ForEachOutPatternElement)

@given(instance=atlstatic::ATL::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::SimpleOutPatternElement)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=atlstatic::ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::OutPatternElement)

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=atlstatic::ATL::Library_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::library_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Library)

@given(instance=LibraryRef_strategy)
@settings(max_examples=50)
def test_libraryref_instantiation(instance):
    assert isinstance(instance, LibraryRef)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=atlstatic::ATL::DropPattern_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::droppattern_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::DropPattern)

@given(instance=atlstatic::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::VariableDeclaration)

@given(instance=atlstatic::OCL::VariableDeclaration_strategy)
def test_atlstatic::ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=atlstatic::OCL::VariableDeclaration_strategy)
def test_atlstatic::ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=atlstatic::OCL::VariableDeclaration_strategy)
def test_atlstatic::ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=atlstatic::OCL::VariableDeclaration_strategy)
def test_atlstatic::ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=atlstatic::OCL::OclModel_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclModel)

@given(instance=atlstatic::OCL::OclModel_strategy)
def test_atlstatic::ocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::OclModel_strategy)
def test_atlstatic::ocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::ATL::Binding_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::binding_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Binding)

@given(instance=atlstatic::ATL::Binding_strategy)
def test_atlstatic::atl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atlstatic::ATL::Binding_strategy)
def test_atlstatic::atl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atlstatic::ATL::Binding_strategy)
def test_atlstatic::atl::binding_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=atlstatic::ATL::Binding_strategy)
def test_atlstatic::atl::binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atlstatic::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclExpression)

@given(instance=atlstatic::OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclFeature)

@given(instance=atlstatic::ATL::LibraryRef_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::libraryref_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::LibraryRef)

@given(instance=atlstatic::ATL::LibraryRef_strategy)
def test_atlstatic::atl::libraryref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::ATL::LibraryRef_strategy)
def test_atlstatic::atl::libraryref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::TupleTypeAttribute)

@given(instance=atlstatic::OCL::TupleTypeAttribute_strategy)
def test_atlstatic::ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::TupleTypeAttribute_strategy)
def test_atlstatic::ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::ATL::ActionBlock_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::actionblock_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ActionBlock)

@given(instance=atlstatic::OCL::MapElement_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::mapelement_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::MapElement)

@given(instance=atlstatic::OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclContextDefinition)

@given(instance=atlstatic::OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclFeatureDefinition)

@given(instance=atlstatic::ATL::InPattern_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::inpattern_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::InPattern)

@given(instance=atlstatic::ATL::Statement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::statement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Statement)

@given(instance=atlstatic::ATL::OutPattern_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::outpattern_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::OutPattern)

@given(instance=atlstatic::ATL::Unit_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::unit_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Unit)

@given(instance=atlstatic::ATL::Unit_strategy)
def test_atlstatic::atl::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::ATL::Unit_strategy)
def test_atlstatic::atl::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::ATL::SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::SimpleInPatternElement)

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

@given(instance=atlstatic::ATL::ContextHelper_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::contexthelper_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ContextHelper)

@given(instance=ATL::ModuleCallable_strategy)
@settings(max_examples=50)
def test_atl::modulecallable_instantiation(instance):
    assert isinstance(instance, ATL::ModuleCallable)

@given(instance=ATL::Helper_strategy)
@settings(max_examples=50)
def test_atl::helper_instantiation(instance):
    assert isinstance(instance, ATL::Helper)

@given(instance=atlstatic::ATL::StaticHelper_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::statichelper_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::StaticHelper)

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

@given(instance=ATL::Callable_strategy)
@settings(max_examples=50)
def test_atl::callable_instantiation(instance):
    assert isinstance(instance, ATL::Callable)

@given(instance=ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_atl::moduleelement_instantiation(instance):
    assert isinstance(instance, ATL::ModuleElement)

@given(instance=atlstatic::ATL::Helper_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::helper_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Helper)

@given(instance=atlstatic::ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::moduleelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ModuleElement)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=atlstatic::ATL::Rule_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::rule_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Rule)

@given(instance=atlstatic::ATL::Rule_strategy)
def test_atlstatic::atl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::ATL::Rule_strategy)
def test_atlstatic::atl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=StaticRule_strategy)
@settings(max_examples=50)
def test_staticrule_instantiation(instance):
    assert isinstance(instance, StaticRule)

@given(instance=atlstatic::ATL::CalledRule_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::calledrule_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::CalledRule)

@given(instance=atlstatic::ATL::CalledRule_strategy)
def test_atlstatic::atl::calledrule_isEndpoint_type(instance):
    assert isinstance(instance.isEndpoint, str)


@given(instance=atlstatic::ATL::CalledRule_strategy)
def test_atlstatic::atl::calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original

@given(instance=atlstatic::ATL::CalledRule_strategy)
def test_atlstatic::atl::calledrule_isEntrypoint_type(instance):
    assert isinstance(instance.isEntrypoint, str)


@given(instance=atlstatic::ATL::CalledRule_strategy)
def test_atlstatic::atl::calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=ATL::StaticRule_strategy)
@settings(max_examples=50)
def test_atl::staticrule_instantiation(instance):
    assert isinstance(instance, ATL::StaticRule)

@given(instance=ATL::RuleWithPattern_strategy)
@settings(max_examples=50)
def test_atl::rulewithpattern_instantiation(instance):
    assert isinstance(instance, ATL::RuleWithPattern)

@given(instance=atlstatic::ATL::LazyRule_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::lazyrule_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::LazyRule)

@given(instance=atlstatic::ATL::LazyRule_strategy)
def test_atlstatic::atl::lazyrule_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=atlstatic::ATL::LazyRule_strategy)
def test_atlstatic::atl::lazyrule_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=RuleWithPattern_strategy)
@settings(max_examples=50)
def test_rulewithpattern_instantiation(instance):
    assert isinstance(instance, RuleWithPattern)

@given(instance=atlstatic::ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::matchedrule_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::MatchedRule)

@given(instance=InPattern_strategy)
@settings(max_examples=50)
def test_inpattern_instantiation(instance):
    assert isinstance(instance, InPattern)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::rulewithpattern_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::RuleWithPattern)

@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isNoDefault_type(instance):
    assert isinstance(instance.isNoDefault, str)


@given(instance=atlstatic::ATL::RuleWithPattern_strategy)
def test_atlstatic::atl::rulewithpattern_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original

@given(instance=atlstatic::ATL::Callable_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::callable_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Callable)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=atlstatic::ATL::ModuleCallable_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::modulecallable_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::ModuleCallable)

@given(instance=ATL::Rule_strategy)
@settings(max_examples=50)
def test_atl::rule_instantiation(instance):
    assert isinstance(instance, ATL::Rule)

@given(instance=atlstatic::ATL::StaticRule_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::staticrule_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::StaticRule)

@given(instance=atlstatic::ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::locatedelement_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::LocatedElement)

@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=atlstatic::ATL::LocatedElement_strategy)
def test_atlstatic::atl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=atlstatic::ATL::Module_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::module_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Module)

@given(instance=atlstatic::ATL::Module_strategy)
def test_atlstatic::atl::module_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=atlstatic::ATL::Module_strategy)
def test_atlstatic::atl::module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atlstatic::OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::PrimitiveExp)

@given(instance=atlstatic::OCL::MapExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::mapexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::MapExp)

@given(instance=atlstatic::OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::CollectionExp)

@given(instance=atlstatic::OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::EnumLiteralExp)

@given(instance=atlstatic::OCL::EnumLiteralExp_strategy)
def test_atlstatic::ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::EnumLiteralExp_strategy)
def test_atlstatic::ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::OCL::OclType_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::ocltype_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclType)

@given(instance=atlstatic::OCL::OclType_strategy)
def test_atlstatic::ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlstatic::OCL::OclType_strategy)
def test_atlstatic::ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic::OCL::LetExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::letexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::LetExp)

@given(instance=atlstatic::OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::TupleExp)

@given(instance=atlstatic::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::PropertyCallExp)

@given(instance=atlstatic::OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::OclUndefinedExp)

@given(instance=atlstatic::OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::variableexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::VariableExp)

@given(instance=atlstatic::OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::superexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::SuperExp)

@given(instance=atlstatic::OCL::IfExp_strategy)
@settings(max_examples=50)
def test_atlstatic::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, atlstatic::OCL::IfExp)

@given(instance=atlstatic::ATL::Query_strategy)
@settings(max_examples=50)
def test_atlstatic::atl::query_instantiation(instance):
    assert isinstance(instance, atlstatic::ATL::Query)
