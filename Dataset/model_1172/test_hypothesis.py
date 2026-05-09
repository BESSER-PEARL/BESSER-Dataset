import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JavaBody,
    atlext::OCL::GetAppliedStereotypesBody,
    atlext::OCL::TypedElement,
    OclModelElement,
    OclFeature,
    atlext::OCL::Operation,
    atlext::OCL::Attribute,
    TupleType,
    NumericType,
    atlext::OCL::RealType,
    atlext::OCL::IntegerType,
    Primitive,
    atlext::OCL::NumericType,
    atlext::OCL::BooleanType,
    atlext::OCL::StringType,
    TupleTypeAttribute,
    CollectionType,
    atlext::OCL::BagType,
    atlext::OCL::SequenceType,
    atlext::OCL::OrderedSetType,
    atlext::OCL::SetType,
    MapType,
    OclContextDefinition,
    VariableExp,
    IterateExp,
    ResolveTempResolution,
    ContextHelper,
    PrimitiveExp,
    MapExp,
    MapElement,
    TupleExp,
    TuplePart,
    NumericExp,
    atlext::OCL::IntegerExp,
    atlext::OCL::RealExp,
    atlext::OCL::NumericExp,
    atlext::OCL::BooleanExp,
    atlext::OCL::StringExp,
    Attribute,
    Operation,
    OperationCallExp,
    atlext::OCL::CollectionOperationCallExp,
    atlext::OCL::OperatorCallExp,
    LoopExp,
    atlext::OCL::IterateExp,
    atlext::OCL::IteratorExp,
    LetExp,
    CollectionExp,
    atlext::OCL::BagExp,
    atlext::OCL::OrderedSetExp,
    atlext::OCL::SetExp,
    atlext::OCL::SequenceExp,
    IfExp,
    OclType,
    atlext::OCL::MapType,
    atlext::OCL::OclAnyType,
    atlext::OCL::Primitive,
    atlext::OCL::OclModelElement,
    atlext::OCL::TupleType,
    atlext::OCL::CollectionType,
    OCL::TypedElement,
    ATL::LocatedElement,
    atlext::OCL::VariableDeclaration,
    atlext::OCL::OclExpression,
    MatchedRule,
    atlext::ATL::RuleResolutionInfo,
    atlext::ATL::CallableParameter,
    atlext::ATL::StringToStringMap,
    Statement,
    atlext::ATL::ForStat,
    atlext::ATL::BindingStat,
    atlext::ATL::IfStat,
    atlext::ATL::ExpressionStat,
    OutPatternElement,
    RuleResolutionInfo,
    atlext::OCL::ResolveTempResolution,
    Iterator,
    atlext::ATL::ForEachOutPatternElement,
    atlext::ATL::SimpleOutPatternElement,
    Binding,
    PatternElement,
    atlext::ATL::OutPatternElement,
    atlext::ATL::InPatternElement,
    VariableDeclaration,
    atlext::ATL::RuleVariableDeclaration,
    atlext::OCL::Parameter,
    atlext::OCL::Iterator,
    atlext::OCL::TuplePart,
    atlext::ATL::PatternElement,
    RuleVariableDeclaration,
    ActionBlock,
    DropPattern,
    InPatternElement,
    atlext::ATL::SimpleInPatternElement,
    Parameter,
    StaticRule,
    atlext::ATL::CalledRule,
    ATL::StaticRule,
    ATL::RuleWithPattern,
    atlext::ATL::LazyRule,
    RuleWithPattern,
    atlext::ATL::MatchedRule,
    InPattern,
    Rule,
    atlext::ATL::RuleWithPattern,
    CallableParameter,
    atlext::ATL::Callable,
    Callable,
    atlext::ATL::ModuleCallable,
    ATL::Rule,
    Unit,
    atlext::ATL::Library,
    LibraryRef,
    OutPattern,
    PropertyCallExp,
    atlext::OCL::LoopExp,
    atlext::OCL::OperationCallExp,
    atlext::OCL::NavigationOrAttributeCallExp,
    ATL::ModuleCallable,
    atlext::ATL::StaticRule,
    ATL::Helper,
    atlext::ATL::StaticHelper,
    OclFeatureDefinition,
    Library,
    Query,
    ATL::Callable,
    ATL::ModuleElement,
    atlext::ATL::Helper,
    ModuleElement,
    atlext::ATL::Rule,
    OclModel,
    atlext::ATL::Module,
    OclExpression,
    atlext::OCL::PrimitiveExp,
    atlext::OCL::JavaBody,
    atlext::OCL::MapExp,
    atlext::OCL::PropertyCallExp,
    atlext::OCL::VariableExp,
    atlext::OCL::IfExp,
    atlext::OCL::EnumLiteralExp,
    atlext::OCL::OclUndefinedExp,
    atlext::OCL::OclType,
    atlext::OCL::LetExp,
    atlext::OCL::SuperExp,
    atlext::OCL::CollectionExp,
    atlext::OCL::TupleExp,
    atlext::ATL::Query,
    Helper,
    atlext::ATL::ContextHelper,
    LocatedElement,
    atlext::ATL::ActionBlock,
    atlext::ATL::ModuleElement,
    atlext::OCL::OclModel,
    atlext::ATL::DropPattern,
    atlext::OCL::OclFeatureDefinition,
    atlext::ATL::LibraryRef,
    atlext::OCL::OclContextDefinition,
    atlext::ATL::OutPattern,
    atlext::OCL::TupleTypeAttribute,
    atlext::ATL::Statement,
    atlext::OCL::OclFeature,
    atlext::ATL::Binding,
    atlext::ATL::InPattern,
    atlext::OCL::MapElement,
    atlext::ATL::Unit,
    StringToStringMap,
    atlext::ATL::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javabody_is_not_abstract():
    assert not inspect.isabstract(JavaBody)


def test_javabody_constructor_exists():
    assert callable(JavaBody.__init__)


def test_javabody_constructor_args():
    sig = inspect.signature(JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::getappliedstereotypesbody_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::GetAppliedStereotypesBody)


def test_atlext::ocl::getappliedstereotypesbody_constructor_exists():
    assert callable(atlext::OCL::GetAppliedStereotypesBody.__init__)


def test_atlext::ocl::getappliedstereotypesbody_constructor_args():
    sig = inspect.signature(atlext::OCL::GetAppliedStereotypesBody.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::typedelement_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TypedElement)


def test_atlext::ocl::typedelement_constructor_exists():
    assert callable(atlext::OCL::TypedElement.__init__)


def test_atlext::ocl::typedelement_constructor_args():
    sig = inspect.signature(atlext::OCL::TypedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_atlext::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::Operation)


def test_atlext::ocl::operation_constructor_exists():
    assert callable(atlext::OCL::Operation.__init__)


def test_atlext::ocl::operation_constructor_args():
    sig = inspect.signature(atlext::OCL::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::operation_has_name():
    assert hasattr(atlext::OCL::Operation, "name")
    descriptor = None
    for klass in atlext::OCL::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::Attribute)


def test_atlext::ocl::attribute_constructor_exists():
    assert callable(atlext::OCL::Attribute.__init__)


def test_atlext::ocl::attribute_constructor_args():
    sig = inspect.signature(atlext::OCL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::attribute_has_name():
    assert hasattr(atlext::OCL::Attribute, "name")
    descriptor = None
    for klass in atlext::OCL::Attribute.__mro__:
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



def test_atlext::ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::RealType)


def test_atlext::ocl::realtype_constructor_exists():
    assert callable(atlext::OCL::RealType.__init__)


def test_atlext::ocl::realtype_constructor_args():
    sig = inspect.signature(atlext::OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::IntegerType)


def test_atlext::ocl::integertype_constructor_exists():
    assert callable(atlext::OCL::IntegerType.__init__)


def test_atlext::ocl::integertype_constructor_args():
    sig = inspect.signature(atlext::OCL::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::NumericType)


def test_atlext::ocl::numerictype_constructor_exists():
    assert callable(atlext::OCL::NumericType.__init__)


def test_atlext::ocl::numerictype_constructor_args():
    sig = inspect.signature(atlext::OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::BooleanType)


def test_atlext::ocl::booleantype_constructor_exists():
    assert callable(atlext::OCL::BooleanType.__init__)


def test_atlext::ocl::booleantype_constructor_args():
    sig = inspect.signature(atlext::OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::StringType)


def test_atlext::ocl::stringtype_constructor_exists():
    assert callable(atlext::OCL::StringType.__init__)


def test_atlext::ocl::stringtype_constructor_args():
    sig = inspect.signature(atlext::OCL::StringType.__init__)
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



def test_atlext::ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::BagType)


def test_atlext::ocl::bagtype_constructor_exists():
    assert callable(atlext::OCL::BagType.__init__)


def test_atlext::ocl::bagtype_constructor_args():
    sig = inspect.signature(atlext::OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::SequenceType)


def test_atlext::ocl::sequencetype_constructor_exists():
    assert callable(atlext::OCL::SequenceType.__init__)


def test_atlext::ocl::sequencetype_constructor_args():
    sig = inspect.signature(atlext::OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OrderedSetType)


def test_atlext::ocl::orderedsettype_constructor_exists():
    assert callable(atlext::OCL::OrderedSetType.__init__)


def test_atlext::ocl::orderedsettype_constructor_args():
    sig = inspect.signature(atlext::OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::settype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::SetType)


def test_atlext::ocl::settype_constructor_exists():
    assert callable(atlext::OCL::SetType.__init__)


def test_atlext::ocl::settype_constructor_args():
    sig = inspect.signature(atlext::OCL::SetType.__init__)
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



def test_resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(ResolveTempResolution)


def test_resolvetempresolution_constructor_exists():
    assert callable(ResolveTempResolution.__init__)


def test_resolvetempresolution_constructor_args():
    sig = inspect.signature(ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_contexthelper_is_not_abstract():
    assert not inspect.isabstract(ContextHelper)


def test_contexthelper_constructor_exists():
    assert callable(ContextHelper.__init__)


def test_contexthelper_constructor_args():
    sig = inspect.signature(ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
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



def test_atlext::ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::IntegerExp)


def test_atlext::ocl::integerexp_constructor_exists():
    assert callable(atlext::OCL::IntegerExp.__init__)


def test_atlext::ocl::integerexp_constructor_args():
    sig = inspect.signature(atlext::OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_atlext::ocl::integerexp_has_integerSymbol():
    assert hasattr(atlext::OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in atlext::OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::RealExp)


def test_atlext::ocl::realexp_constructor_exists():
    assert callable(atlext::OCL::RealExp.__init__)


def test_atlext::ocl::realexp_constructor_args():
    sig = inspect.signature(atlext::OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_atlext::ocl::realexp_has_realSymbol():
    assert hasattr(atlext::OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in atlext::OCL::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::NumericExp)


def test_atlext::ocl::numericexp_constructor_exists():
    assert callable(atlext::OCL::NumericExp.__init__)


def test_atlext::ocl::numericexp_constructor_args():
    sig = inspect.signature(atlext::OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::BooleanExp)


def test_atlext::ocl::booleanexp_constructor_exists():
    assert callable(atlext::OCL::BooleanExp.__init__)


def test_atlext::ocl::booleanexp_constructor_args():
    sig = inspect.signature(atlext::OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_atlext::ocl::booleanexp_has_booleanSymbol():
    assert hasattr(atlext::OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in atlext::OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::StringExp)


def test_atlext::ocl::stringexp_constructor_exists():
    assert callable(atlext::OCL::StringExp.__init__)


def test_atlext::ocl::stringexp_constructor_args():
    sig = inspect.signature(atlext::OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_atlext::ocl::stringexp_has_stringSymbol():
    assert hasattr(atlext::OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in atlext::OCL::StringExp.__mro__:
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



def test_atlext::ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::CollectionOperationCallExp)


def test_atlext::ocl::collectionoperationcallexp_constructor_exists():
    assert callable(atlext::OCL::CollectionOperationCallExp.__init__)


def test_atlext::ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OperatorCallExp)


def test_atlext::ocl::operatorcallexp_constructor_exists():
    assert callable(atlext::OCL::OperatorCallExp.__init__)


def test_atlext::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::IterateExp)


def test_atlext::ocl::iterateexp_constructor_exists():
    assert callable(atlext::OCL::IterateExp.__init__)


def test_atlext::ocl::iterateexp_constructor_args():
    sig = inspect.signature(atlext::OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::IteratorExp)


def test_atlext::ocl::iteratorexp_constructor_exists():
    assert callable(atlext::OCL::IteratorExp.__init__)


def test_atlext::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(atlext::OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::iteratorexp_has_name():
    assert hasattr(atlext::OCL::IteratorExp, "name")
    descriptor = None
    for klass in atlext::OCL::IteratorExp.__mro__:
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



def test_atlext::ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::BagExp)


def test_atlext::ocl::bagexp_constructor_exists():
    assert callable(atlext::OCL::BagExp.__init__)


def test_atlext::ocl::bagexp_constructor_args():
    sig = inspect.signature(atlext::OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OrderedSetExp)


def test_atlext::ocl::orderedsetexp_constructor_exists():
    assert callable(atlext::OCL::OrderedSetExp.__init__)


def test_atlext::ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(atlext::OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::SetExp)


def test_atlext::ocl::setexp_constructor_exists():
    assert callable(atlext::OCL::SetExp.__init__)


def test_atlext::ocl::setexp_constructor_args():
    sig = inspect.signature(atlext::OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::SequenceExp)


def test_atlext::ocl::sequenceexp_constructor_exists():
    assert callable(atlext::OCL::SequenceExp.__init__)


def test_atlext::ocl::sequenceexp_constructor_args():
    sig = inspect.signature(atlext::OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



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



def test_atlext::ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::MapType)


def test_atlext::ocl::maptype_constructor_exists():
    assert callable(atlext::OCL::MapType.__init__)


def test_atlext::ocl::maptype_constructor_args():
    sig = inspect.signature(atlext::OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclAnyType)


def test_atlext::ocl::oclanytype_constructor_exists():
    assert callable(atlext::OCL::OclAnyType.__init__)


def test_atlext::ocl::oclanytype_constructor_args():
    sig = inspect.signature(atlext::OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::Primitive)


def test_atlext::ocl::primitive_constructor_exists():
    assert callable(atlext::OCL::Primitive.__init__)


def test_atlext::ocl::primitive_constructor_args():
    sig = inspect.signature(atlext::OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclModelElement)


def test_atlext::ocl::oclmodelelement_constructor_exists():
    assert callable(atlext::OCL::OclModelElement.__init__)


def test_atlext::ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(atlext::OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TupleType)


def test_atlext::ocl::tupletype_constructor_exists():
    assert callable(atlext::OCL::TupleType.__init__)


def test_atlext::ocl::tupletype_constructor_args():
    sig = inspect.signature(atlext::OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::CollectionType)


def test_atlext::ocl::collectiontype_constructor_exists():
    assert callable(atlext::OCL::CollectionType.__init__)


def test_atlext::ocl::collectiontype_constructor_args():
    sig = inspect.signature(atlext::OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::typedelement_is_not_abstract():
    assert not inspect.isabstract(OCL::TypedElement)


def test_ocl::typedelement_constructor_exists():
    assert callable(OCL::TypedElement.__init__)


def test_ocl::typedelement_constructor_args():
    sig = inspect.signature(OCL::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(ATL::LocatedElement)


def test_atl::locatedelement_constructor_exists():
    assert callable(ATL::LocatedElement.__init__)


def test_atl::locatedelement_constructor_args():
    sig = inspect.signature(ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::VariableDeclaration)


def test_atlext::ocl::variabledeclaration_constructor_exists():
    assert callable(atlext::OCL::VariableDeclaration.__init__)


def test_atlext::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(atlext::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "id" in params, "Missing parameter 'id'"

def test_atlext::ocl::variabledeclaration_has_varName():
    assert hasattr(atlext::OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in atlext::OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_atlext::ocl::variabledeclaration_has_id():
    assert hasattr(atlext::OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in atlext::OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclExpression)


def test_atlext::ocl::oclexpression_constructor_exists():
    assert callable(atlext::OCL::OclExpression.__init__)


def test_atlext::ocl::oclexpression_constructor_args():
    sig = inspect.signature(atlext::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "implicitlyCasted" in params, "Missing parameter 'implicitlyCasted'"

def test_atlext::ocl::oclexpression_has_implicitlyCasted():
    assert hasattr(atlext::OCL::OclExpression, "implicitlyCasted")
    descriptor = None
    for klass in atlext::OCL::OclExpression.__mro__:
        if "implicitlyCasted" in klass.__dict__:
            descriptor = klass.__dict__["implicitlyCasted"]
            break
    assert isinstance(descriptor, property)



def test_matchedrule_is_not_abstract():
    assert not inspect.isabstract(MatchedRule)


def test_matchedrule_constructor_exists():
    assert callable(MatchedRule.__init__)


def test_matchedrule_constructor_args():
    sig = inspect.signature(MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::RuleResolutionInfo)


def test_atlext::atl::ruleresolutioninfo_constructor_exists():
    assert callable(atlext::ATL::RuleResolutionInfo.__init__)


def test_atlext::atl::ruleresolutioninfo_constructor_args():
    sig = inspect.signature(atlext::ATL::RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::callableparameter_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::CallableParameter)


def test_atlext::atl::callableparameter_constructor_exists():
    assert callable(atlext::ATL::CallableParameter.__init__)


def test_atlext::atl::callableparameter_constructor_args():
    sig = inspect.signature(atlext::ATL::CallableParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::atl::callableparameter_has_name():
    assert hasattr(atlext::ATL::CallableParameter, "name")
    descriptor = None
    for klass in atlext::ATL::CallableParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::StringToStringMap)


def test_atlext::atl::stringtostringmap_constructor_exists():
    assert callable(atlext::ATL::StringToStringMap.__init__)


def test_atlext::atl::stringtostringmap_constructor_args():
    sig = inspect.signature(atlext::ATL::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_atlext::atl::stringtostringmap_has_value():
    assert hasattr(atlext::ATL::StringToStringMap, "value")
    descriptor = None
    for klass in atlext::ATL::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::stringtostringmap_has_key():
    assert hasattr(atlext::ATL::StringToStringMap, "key")
    descriptor = None
    for klass in atlext::ATL::StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::forstat_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ForStat)


def test_atlext::atl::forstat_constructor_exists():
    assert callable(atlext::ATL::ForStat.__init__)


def test_atlext::atl::forstat_constructor_args():
    sig = inspect.signature(atlext::ATL::ForStat.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::BindingStat)


def test_atlext::atl::bindingstat_constructor_exists():
    assert callable(atlext::ATL::BindingStat.__init__)


def test_atlext::atl::bindingstat_constructor_args():
    sig = inspect.signature(atlext::ATL::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atlext::atl::bindingstat_has_propertyName():
    assert hasattr(atlext::ATL::BindingStat, "propertyName")
    descriptor = None
    for klass in atlext::ATL::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::bindingstat_has_isAssignment():
    assert hasattr(atlext::ATL::BindingStat, "isAssignment")
    descriptor = None
    for klass in atlext::ATL::BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::ifstat_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::IfStat)


def test_atlext::atl::ifstat_constructor_exists():
    assert callable(atlext::ATL::IfStat.__init__)


def test_atlext::atl::ifstat_constructor_args():
    sig = inspect.signature(atlext::ATL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::expressionstat_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ExpressionStat)


def test_atlext::atl::expressionstat_constructor_exists():
    assert callable(atlext::ATL::ExpressionStat.__init__)


def test_atlext::atl::expressionstat_constructor_args():
    sig = inspect.signature(atlext::ATL::ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(RuleResolutionInfo)


def test_ruleresolutioninfo_constructor_exists():
    assert callable(RuleResolutionInfo.__init__)


def test_ruleresolutioninfo_constructor_args():
    sig = inspect.signature(RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::ResolveTempResolution)


def test_atlext::ocl::resolvetempresolution_constructor_exists():
    assert callable(atlext::OCL::ResolveTempResolution.__init__)


def test_atlext::ocl::resolvetempresolution_constructor_args():
    sig = inspect.signature(atlext::OCL::ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ForEachOutPatternElement)


def test_atlext::atl::foreachoutpatternelement_constructor_exists():
    assert callable(atlext::ATL::ForEachOutPatternElement.__init__)


def test_atlext::atl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::SimpleOutPatternElement)


def test_atlext::atl::simpleoutpatternelement_constructor_exists():
    assert callable(atlext::ATL::SimpleOutPatternElement.__init__)


def test_atlext::atl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::SimpleOutPatternElement.__init__)
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



def test_atlext::atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::OutPatternElement)


def test_atlext::atl::outpatternelement_constructor_exists():
    assert callable(atlext::ATL::OutPatternElement.__init__)


def test_atlext::atl::outpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::InPatternElement)


def test_atlext::atl::inpatternelement_constructor_exists():
    assert callable(atlext::ATL::InPatternElement.__init__)


def test_atlext::atl::inpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::RuleVariableDeclaration)


def test_atlext::atl::rulevariabledeclaration_constructor_exists():
    assert callable(atlext::ATL::RuleVariableDeclaration.__init__)


def test_atlext::atl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(atlext::ATL::RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::Parameter)


def test_atlext::ocl::parameter_constructor_exists():
    assert callable(atlext::OCL::Parameter.__init__)


def test_atlext::ocl::parameter_constructor_args():
    sig = inspect.signature(atlext::OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::Iterator)


def test_atlext::ocl::iterator_constructor_exists():
    assert callable(atlext::OCL::Iterator.__init__)


def test_atlext::ocl::iterator_constructor_args():
    sig = inspect.signature(atlext::OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TuplePart)


def test_atlext::ocl::tuplepart_constructor_exists():
    assert callable(atlext::OCL::TuplePart.__init__)


def test_atlext::ocl::tuplepart_constructor_args():
    sig = inspect.signature(atlext::OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::patternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::PatternElement)


def test_atlext::atl::patternelement_constructor_exists():
    assert callable(atlext::ATL::PatternElement.__init__)


def test_atlext::atl::patternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::PatternElement.__init__)
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



def test_atlext::atl::simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::SimpleInPatternElement)


def test_atlext::atl::simpleinpatternelement_constructor_exists():
    assert callable(atlext::ATL::SimpleInPatternElement.__init__)


def test_atlext::atl::simpleinpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::SimpleInPatternElement.__init__)
    params = list(sig.parameters.keys())



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



def test_atlext::atl::calledrule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::CalledRule)


def test_atlext::atl::calledrule_constructor_exists():
    assert callable(atlext::ATL::CalledRule.__init__)


def test_atlext::atl::calledrule_constructor_args():
    sig = inspect.signature(atlext::ATL::CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"

def test_atlext::atl::calledrule_has_isEntrypoint():
    assert hasattr(atlext::ATL::CalledRule, "isEntrypoint")
    descriptor = None
    for klass in atlext::ATL::CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::calledrule_has_isEndpoint():
    assert hasattr(atlext::ATL::CalledRule, "isEndpoint")
    descriptor = None
    for klass in atlext::ATL::CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
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



def test_atlext::atl::lazyrule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::LazyRule)


def test_atlext::atl::lazyrule_constructor_exists():
    assert callable(atlext::ATL::LazyRule.__init__)


def test_atlext::atl::lazyrule_constructor_args():
    sig = inspect.signature(atlext::ATL::LazyRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_atlext::atl::lazyrule_has_isUnique():
    assert hasattr(atlext::ATL::LazyRule, "isUnique")
    descriptor = None
    for klass in atlext::ATL::LazyRule.__mro__:
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



def test_atlext::atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::MatchedRule)


def test_atlext::atl::matchedrule_constructor_exists():
    assert callable(atlext::ATL::MatchedRule.__init__)


def test_atlext::atl::matchedrule_constructor_args():
    sig = inspect.signature(atlext::ATL::MatchedRule.__init__)
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



def test_atlext::atl::rulewithpattern_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::RuleWithPattern)


def test_atlext::atl::rulewithpattern_constructor_exists():
    assert callable(atlext::ATL::RuleWithPattern.__init__)


def test_atlext::atl::rulewithpattern_constructor_args():
    sig = inspect.signature(atlext::ATL::RuleWithPattern.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"

def test_atlext::atl::rulewithpattern_has_isRefining():
    assert hasattr(atlext::ATL::RuleWithPattern, "isRefining")
    descriptor = None
    for klass in atlext::ATL::RuleWithPattern.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::rulewithpattern_has_isAbstract():
    assert hasattr(atlext::ATL::RuleWithPattern, "isAbstract")
    descriptor = None
    for klass in atlext::ATL::RuleWithPattern.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::rulewithpattern_has_isNoDefault():
    assert hasattr(atlext::ATL::RuleWithPattern, "isNoDefault")
    descriptor = None
    for klass in atlext::ATL::RuleWithPattern.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)



def test_callableparameter_is_not_abstract():
    assert not inspect.isabstract(CallableParameter)


def test_callableparameter_constructor_exists():
    assert callable(CallableParameter.__init__)


def test_callableparameter_constructor_args():
    sig = inspect.signature(CallableParameter.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::callable_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Callable)


def test_atlext::atl::callable_constructor_exists():
    assert callable(atlext::ATL::Callable.__init__)


def test_atlext::atl::callable_constructor_args():
    sig = inspect.signature(atlext::ATL::Callable.__init__)
    params = list(sig.parameters.keys())



def test_callable_is_not_abstract():
    assert not inspect.isabstract(Callable)


def test_callable_constructor_exists():
    assert callable(Callable.__init__)


def test_callable_constructor_args():
    sig = inspect.signature(Callable.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::modulecallable_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ModuleCallable)


def test_atlext::atl::modulecallable_constructor_exists():
    assert callable(atlext::ATL::ModuleCallable.__init__)


def test_atlext::atl::modulecallable_constructor_args():
    sig = inspect.signature(atlext::ATL::ModuleCallable.__init__)
    params = list(sig.parameters.keys())



def test_atl::rule_is_not_abstract():
    assert not inspect.isabstract(ATL::Rule)


def test_atl::rule_constructor_exists():
    assert callable(ATL::Rule.__init__)


def test_atl::rule_constructor_args():
    sig = inspect.signature(ATL::Rule.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::library_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Library)


def test_atlext::atl::library_constructor_exists():
    assert callable(atlext::ATL::Library.__init__)


def test_atlext::atl::library_constructor_args():
    sig = inspect.signature(atlext::ATL::Library.__init__)
    params = list(sig.parameters.keys())



def test_libraryref_is_not_abstract():
    assert not inspect.isabstract(LibraryRef)


def test_libraryref_constructor_exists():
    assert callable(LibraryRef.__init__)


def test_libraryref_constructor_args():
    sig = inspect.signature(LibraryRef.__init__)
    params = list(sig.parameters.keys())



def test_outpattern_is_not_abstract():
    assert not inspect.isabstract(OutPattern)


def test_outpattern_constructor_exists():
    assert callable(OutPattern.__init__)


def test_outpattern_constructor_args():
    sig = inspect.signature(OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::LoopExp)


def test_atlext::ocl::loopexp_constructor_exists():
    assert callable(atlext::OCL::LoopExp.__init__)


def test_atlext::ocl::loopexp_constructor_args():
    sig = inspect.signature(atlext::OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OperationCallExp)


def test_atlext::ocl::operationcallexp_constructor_exists():
    assert callable(atlext::OCL::OperationCallExp.__init__)


def test_atlext::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_atlext::ocl::operationcallexp_has_operationName():
    assert hasattr(atlext::OCL::OperationCallExp, "operationName")
    descriptor = None
    for klass in atlext::OCL::OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::NavigationOrAttributeCallExp)


def test_atlext::ocl::navigationorattributecallexp_constructor_exists():
    assert callable(atlext::OCL::NavigationOrAttributeCallExp.__init__)


def test_atlext::ocl::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::navigationorattributecallexp_has_name():
    assert hasattr(atlext::OCL::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in atlext::OCL::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::modulecallable_is_not_abstract():
    assert not inspect.isabstract(ATL::ModuleCallable)


def test_atl::modulecallable_constructor_exists():
    assert callable(ATL::ModuleCallable.__init__)


def test_atl::modulecallable_constructor_args():
    sig = inspect.signature(ATL::ModuleCallable.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::staticrule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::StaticRule)


def test_atlext::atl::staticrule_constructor_exists():
    assert callable(atlext::ATL::StaticRule.__init__)


def test_atlext::atl::staticrule_constructor_args():
    sig = inspect.signature(atlext::ATL::StaticRule.__init__)
    params = list(sig.parameters.keys())



def test_atl::helper_is_not_abstract():
    assert not inspect.isabstract(ATL::Helper)


def test_atl::helper_constructor_exists():
    assert callable(ATL::Helper.__init__)


def test_atl::helper_constructor_args():
    sig = inspect.signature(ATL::Helper.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::statichelper_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::StaticHelper)


def test_atlext::atl::statichelper_constructor_exists():
    assert callable(atlext::ATL::StaticHelper.__init__)


def test_atlext::atl::statichelper_constructor_args():
    sig = inspect.signature(atlext::ATL::StaticHelper.__init__)
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



def test_atlext::atl::helper_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Helper)


def test_atlext::atl::helper_constructor_exists():
    assert callable(atlext::ATL::Helper.__init__)


def test_atlext::atl::helper_constructor_args():
    sig = inspect.signature(atlext::ATL::Helper.__init__)
    params = list(sig.parameters.keys())
    assert "hasContext" in params, "Missing parameter 'hasContext'"
    assert "isAttribute" in params, "Missing parameter 'isAttribute'"

def test_atlext::atl::helper_has_hasContext():
    assert hasattr(atlext::ATL::Helper, "hasContext")
    descriptor = None
    for klass in atlext::ATL::Helper.__mro__:
        if "hasContext" in klass.__dict__:
            descriptor = klass.__dict__["hasContext"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::helper_has_isAttribute():
    assert hasattr(atlext::ATL::Helper, "isAttribute")
    descriptor = None
    for klass in atlext::ATL::Helper.__mro__:
        if "isAttribute" in klass.__dict__:
            descriptor = klass.__dict__["isAttribute"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::rule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Rule)


def test_atlext::atl::rule_constructor_exists():
    assert callable(atlext::ATL::Rule.__init__)


def test_atlext::atl::rule_constructor_args():
    sig = inspect.signature(atlext::ATL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::atl::rule_has_name():
    assert hasattr(atlext::ATL::Rule, "name")
    descriptor = None
    for klass in atlext::ATL::Rule.__mro__:
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



def test_atlext::atl::module_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Module)


def test_atlext::atl::module_constructor_exists():
    assert callable(atlext::ATL::Module.__init__)


def test_atlext::atl::module_constructor_args():
    sig = inspect.signature(atlext::ATL::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atlext::atl::module_has_isRefining():
    assert hasattr(atlext::ATL::Module, "isRefining")
    descriptor = None
    for klass in atlext::ATL::Module.__mro__:
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



def test_atlext::ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::PrimitiveExp)


def test_atlext::ocl::primitiveexp_constructor_exists():
    assert callable(atlext::OCL::PrimitiveExp.__init__)


def test_atlext::ocl::primitiveexp_constructor_args():
    sig = inspect.signature(atlext::OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::javabody_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::JavaBody)


def test_atlext::ocl::javabody_constructor_exists():
    assert callable(atlext::OCL::JavaBody.__init__)


def test_atlext::ocl::javabody_constructor_args():
    sig = inspect.signature(atlext::OCL::JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::MapExp)


def test_atlext::ocl::mapexp_constructor_exists():
    assert callable(atlext::OCL::MapExp.__init__)


def test_atlext::ocl::mapexp_constructor_args():
    sig = inspect.signature(atlext::OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::PropertyCallExp)


def test_atlext::ocl::propertycallexp_constructor_exists():
    assert callable(atlext::OCL::PropertyCallExp.__init__)


def test_atlext::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStaticCall" in params, "Missing parameter 'isStaticCall'"

def test_atlext::ocl::propertycallexp_has_isStaticCall():
    assert hasattr(atlext::OCL::PropertyCallExp, "isStaticCall")
    descriptor = None
    for klass in atlext::OCL::PropertyCallExp.__mro__:
        if "isStaticCall" in klass.__dict__:
            descriptor = klass.__dict__["isStaticCall"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::VariableExp)


def test_atlext::ocl::variableexp_constructor_exists():
    assert callable(atlext::OCL::VariableExp.__init__)


def test_atlext::ocl::variableexp_constructor_args():
    sig = inspect.signature(atlext::OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::IfExp)


def test_atlext::ocl::ifexp_constructor_exists():
    assert callable(atlext::OCL::IfExp.__init__)


def test_atlext::ocl::ifexp_constructor_args():
    sig = inspect.signature(atlext::OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::EnumLiteralExp)


def test_atlext::ocl::enumliteralexp_constructor_exists():
    assert callable(atlext::OCL::EnumLiteralExp.__init__)


def test_atlext::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(atlext::OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::enumliteralexp_has_name():
    assert hasattr(atlext::OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in atlext::OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclUndefinedExp)


def test_atlext::ocl::oclundefinedexp_constructor_exists():
    assert callable(atlext::OCL::OclUndefinedExp.__init__)


def test_atlext::ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(atlext::OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclType)


def test_atlext::ocl::ocltype_constructor_exists():
    assert callable(atlext::OCL::OclType.__init__)


def test_atlext::ocl::ocltype_constructor_args():
    sig = inspect.signature(atlext::OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::ocltype_has_name():
    assert hasattr(atlext::OCL::OclType, "name")
    descriptor = None
    for klass in atlext::OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::LetExp)


def test_atlext::ocl::letexp_constructor_exists():
    assert callable(atlext::OCL::LetExp.__init__)


def test_atlext::ocl::letexp_constructor_args():
    sig = inspect.signature(atlext::OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::SuperExp)


def test_atlext::ocl::superexp_constructor_exists():
    assert callable(atlext::OCL::SuperExp.__init__)


def test_atlext::ocl::superexp_constructor_args():
    sig = inspect.signature(atlext::OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::CollectionExp)


def test_atlext::ocl::collectionexp_constructor_exists():
    assert callable(atlext::OCL::CollectionExp.__init__)


def test_atlext::ocl::collectionexp_constructor_args():
    sig = inspect.signature(atlext::OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TupleExp)


def test_atlext::ocl::tupleexp_constructor_exists():
    assert callable(atlext::OCL::TupleExp.__init__)


def test_atlext::ocl::tupleexp_constructor_args():
    sig = inspect.signature(atlext::OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::query_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Query)


def test_atlext::atl::query_constructor_exists():
    assert callable(atlext::ATL::Query.__init__)


def test_atlext::atl::query_constructor_args():
    sig = inspect.signature(atlext::ATL::Query.__init__)
    params = list(sig.parameters.keys())



def test_helper_is_not_abstract():
    assert not inspect.isabstract(Helper)


def test_helper_constructor_exists():
    assert callable(Helper.__init__)


def test_helper_constructor_args():
    sig = inspect.signature(Helper.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::contexthelper_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ContextHelper)


def test_atlext::atl::contexthelper_constructor_exists():
    assert callable(atlext::ATL::ContextHelper.__init__)


def test_atlext::atl::contexthelper_constructor_args():
    sig = inspect.signature(atlext::ATL::ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::actionblock_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ActionBlock)


def test_atlext::atl::actionblock_constructor_exists():
    assert callable(atlext::ATL::ActionBlock.__init__)


def test_atlext::atl::actionblock_constructor_args():
    sig = inspect.signature(atlext::ATL::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ModuleElement)


def test_atlext::atl::moduleelement_constructor_exists():
    assert callable(atlext::ATL::ModuleElement.__init__)


def test_atlext::atl::moduleelement_constructor_args():
    sig = inspect.signature(atlext::ATL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclModel)


def test_atlext::ocl::oclmodel_constructor_exists():
    assert callable(atlext::OCL::OclModel.__init__)


def test_atlext::ocl::oclmodel_constructor_args():
    sig = inspect.signature(atlext::OCL::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::oclmodel_has_name():
    assert hasattr(atlext::OCL::OclModel, "name")
    descriptor = None
    for klass in atlext::OCL::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::droppattern_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::DropPattern)


def test_atlext::atl::droppattern_constructor_exists():
    assert callable(atlext::ATL::DropPattern.__init__)


def test_atlext::atl::droppattern_constructor_args():
    sig = inspect.signature(atlext::ATL::DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclFeatureDefinition)


def test_atlext::ocl::oclfeaturedefinition_constructor_exists():
    assert callable(atlext::OCL::OclFeatureDefinition.__init__)


def test_atlext::ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(atlext::OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::libraryref_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::LibraryRef)


def test_atlext::atl::libraryref_constructor_exists():
    assert callable(atlext::ATL::LibraryRef.__init__)


def test_atlext::atl::libraryref_constructor_args():
    sig = inspect.signature(atlext::ATL::LibraryRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::atl::libraryref_has_name():
    assert hasattr(atlext::ATL::LibraryRef, "name")
    descriptor = None
    for klass in atlext::ATL::LibraryRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclContextDefinition)


def test_atlext::ocl::oclcontextdefinition_constructor_exists():
    assert callable(atlext::OCL::OclContextDefinition.__init__)


def test_atlext::ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(atlext::OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::outpattern_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::OutPattern)


def test_atlext::atl::outpattern_constructor_exists():
    assert callable(atlext::ATL::OutPattern.__init__)


def test_atlext::atl::outpattern_constructor_args():
    sig = inspect.signature(atlext::ATL::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TupleTypeAttribute)


def test_atlext::ocl::tupletypeattribute_constructor_exists():
    assert callable(atlext::OCL::TupleTypeAttribute.__init__)


def test_atlext::ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(atlext::OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::ocl::tupletypeattribute_has_name():
    assert hasattr(atlext::OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in atlext::OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::statement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Statement)


def test_atlext::atl::statement_constructor_exists():
    assert callable(atlext::ATL::Statement.__init__)


def test_atlext::atl::statement_constructor_args():
    sig = inspect.signature(atlext::ATL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclFeature)


def test_atlext::ocl::oclfeature_constructor_exists():
    assert callable(atlext::OCL::OclFeature.__init__)


def test_atlext::ocl::oclfeature_constructor_args():
    sig = inspect.signature(atlext::OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::binding_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Binding)


def test_atlext::atl::binding_constructor_exists():
    assert callable(atlext::ATL::Binding.__init__)


def test_atlext::atl::binding_constructor_args():
    sig = inspect.signature(atlext::ATL::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atlext::atl::binding_has_propertyName():
    assert hasattr(atlext::ATL::Binding, "propertyName")
    descriptor = None
    for klass in atlext::ATL::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::binding_has_isAssignment():
    assert hasattr(atlext::ATL::Binding, "isAssignment")
    descriptor = None
    for klass in atlext::ATL::Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::inpattern_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::InPattern)


def test_atlext::atl::inpattern_constructor_exists():
    assert callable(atlext::ATL::InPattern.__init__)


def test_atlext::atl::inpattern_constructor_args():
    sig = inspect.signature(atlext::ATL::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::MapElement)


def test_atlext::ocl::mapelement_constructor_exists():
    assert callable(atlext::OCL::MapElement.__init__)


def test_atlext::ocl::mapelement_constructor_args():
    sig = inspect.signature(atlext::OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::unit_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Unit)


def test_atlext::atl::unit_constructor_exists():
    assert callable(atlext::ATL::Unit.__init__)


def test_atlext::atl::unit_constructor_args():
    sig = inspect.signature(atlext::ATL::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::atl::unit_has_name():
    assert hasattr(atlext::ATL::Unit, "name")
    descriptor = None
    for klass in atlext::ATL::Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(StringToStringMap)


def test_stringtostringmap_constructor_exists():
    assert callable(StringToStringMap.__init__)


def test_stringtostringmap_constructor_args():
    sig = inspect.signature(StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::LocatedElement)


def test_atlext::atl::locatedelement_constructor_exists():
    assert callable(atlext::ATL::LocatedElement.__init__)


def test_atlext::atl::locatedelement_constructor_args():
    sig = inspect.signature(atlext::ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "fileLocation" in params, "Missing parameter 'fileLocation'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "fileObject" in params, "Missing parameter 'fileObject'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_atlext::atl::locatedelement_has_fileLocation():
    assert hasattr(atlext::ATL::LocatedElement, "fileLocation")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "fileLocation" in klass.__dict__:
            descriptor = klass.__dict__["fileLocation"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::locatedelement_has_commentsAfter():
    assert hasattr(atlext::ATL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::locatedelement_has_fileObject():
    assert hasattr(atlext::ATL::LocatedElement, "fileObject")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "fileObject" in klass.__dict__:
            descriptor = klass.__dict__["fileObject"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::locatedelement_has_commentsBefore():
    assert hasattr(atlext::ATL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::locatedelement_has_location():
    assert hasattr(atlext::ATL::LocatedElement, "location")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
JavaBody_strategy = st.builds(
    JavaBody,
)
atlext::OCL::GetAppliedStereotypesBody_strategy = st.builds(
    atlext::OCL::GetAppliedStereotypesBody,
)
atlext::OCL::TypedElement_strategy = st.builds(
    atlext::OCL::TypedElement,
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
atlext::OCL::Operation_strategy = st.builds(
    atlext::OCL::Operation,
    name=
        safe_text
)
atlext::OCL::Attribute_strategy = st.builds(
    atlext::OCL::Attribute,
    name=
        safe_text
)
TupleType_strategy = st.builds(
    TupleType,
)
NumericType_strategy = st.builds(
    NumericType,
)
atlext::OCL::RealType_strategy = st.builds(
    atlext::OCL::RealType,
)
atlext::OCL::IntegerType_strategy = st.builds(
    atlext::OCL::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
atlext::OCL::NumericType_strategy = st.builds(
    atlext::OCL::NumericType,
)
atlext::OCL::BooleanType_strategy = st.builds(
    atlext::OCL::BooleanType,
)
atlext::OCL::StringType_strategy = st.builds(
    atlext::OCL::StringType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
atlext::OCL::BagType_strategy = st.builds(
    atlext::OCL::BagType,
)
atlext::OCL::SequenceType_strategy = st.builds(
    atlext::OCL::SequenceType,
)
atlext::OCL::OrderedSetType_strategy = st.builds(
    atlext::OCL::OrderedSetType,
)
atlext::OCL::SetType_strategy = st.builds(
    atlext::OCL::SetType,
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
ResolveTempResolution_strategy = st.builds(
    ResolveTempResolution,
)
ContextHelper_strategy = st.builds(
    ContextHelper,
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
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
atlext::OCL::IntegerExp_strategy = st.builds(
    atlext::OCL::IntegerExp,
    integerSymbol=
        safe_text
)
atlext::OCL::RealExp_strategy = st.builds(
    atlext::OCL::RealExp,
    realSymbol=
        safe_text
)
atlext::OCL::NumericExp_strategy = st.builds(
    atlext::OCL::NumericExp,
)
atlext::OCL::BooleanExp_strategy = st.builds(
    atlext::OCL::BooleanExp,
    booleanSymbol=
        safe_text
)
atlext::OCL::StringExp_strategy = st.builds(
    atlext::OCL::StringExp,
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
atlext::OCL::CollectionOperationCallExp_strategy = st.builds(
    atlext::OCL::CollectionOperationCallExp,
)
atlext::OCL::OperatorCallExp_strategy = st.builds(
    atlext::OCL::OperatorCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
atlext::OCL::IterateExp_strategy = st.builds(
    atlext::OCL::IterateExp,
)
atlext::OCL::IteratorExp_strategy = st.builds(
    atlext::OCL::IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
atlext::OCL::BagExp_strategy = st.builds(
    atlext::OCL::BagExp,
)
atlext::OCL::OrderedSetExp_strategy = st.builds(
    atlext::OCL::OrderedSetExp,
)
atlext::OCL::SetExp_strategy = st.builds(
    atlext::OCL::SetExp,
)
atlext::OCL::SequenceExp_strategy = st.builds(
    atlext::OCL::SequenceExp,
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
atlext::OCL::MapType_strategy = st.builds(
    atlext::OCL::MapType,
)
atlext::OCL::OclAnyType_strategy = st.builds(
    atlext::OCL::OclAnyType,
)
atlext::OCL::Primitive_strategy = st.builds(
    atlext::OCL::Primitive,
)
atlext::OCL::OclModelElement_strategy = st.builds(
    atlext::OCL::OclModelElement,
)
atlext::OCL::TupleType_strategy = st.builds(
    atlext::OCL::TupleType,
)
atlext::OCL::CollectionType_strategy = st.builds(
    atlext::OCL::CollectionType,
)
OCL::TypedElement_strategy = st.builds(
    OCL::TypedElement,
)
ATL::LocatedElement_strategy = st.builds(
    ATL::LocatedElement,
)
atlext::OCL::VariableDeclaration_strategy = st.builds(
    atlext::OCL::VariableDeclaration,
    varName=
        safe_text,
    id=
        safe_text
)
atlext::OCL::OclExpression_strategy = st.builds(
    atlext::OCL::OclExpression,
    implicitlyCasted=
        safe_text
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
atlext::ATL::RuleResolutionInfo_strategy = st.builds(
    atlext::ATL::RuleResolutionInfo,
)
atlext::ATL::CallableParameter_strategy = st.builds(
    atlext::ATL::CallableParameter,
    name=
        safe_text
)
atlext::ATL::StringToStringMap_strategy = st.builds(
    atlext::ATL::StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
atlext::ATL::ForStat_strategy = st.builds(
    atlext::ATL::ForStat,
)
atlext::ATL::BindingStat_strategy = st.builds(
    atlext::ATL::BindingStat,
    propertyName=
        safe_text,
    isAssignment=
        safe_text
)
atlext::ATL::IfStat_strategy = st.builds(
    atlext::ATL::IfStat,
)
atlext::ATL::ExpressionStat_strategy = st.builds(
    atlext::ATL::ExpressionStat,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
RuleResolutionInfo_strategy = st.builds(
    RuleResolutionInfo,
)
atlext::OCL::ResolveTempResolution_strategy = st.builds(
    atlext::OCL::ResolveTempResolution,
)
Iterator_strategy = st.builds(
    Iterator,
)
atlext::ATL::ForEachOutPatternElement_strategy = st.builds(
    atlext::ATL::ForEachOutPatternElement,
)
atlext::ATL::SimpleOutPatternElement_strategy = st.builds(
    atlext::ATL::SimpleOutPatternElement,
)
Binding_strategy = st.builds(
    Binding,
)
PatternElement_strategy = st.builds(
    PatternElement,
)
atlext::ATL::OutPatternElement_strategy = st.builds(
    atlext::ATL::OutPatternElement,
)
atlext::ATL::InPatternElement_strategy = st.builds(
    atlext::ATL::InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
atlext::ATL::RuleVariableDeclaration_strategy = st.builds(
    atlext::ATL::RuleVariableDeclaration,
)
atlext::OCL::Parameter_strategy = st.builds(
    atlext::OCL::Parameter,
)
atlext::OCL::Iterator_strategy = st.builds(
    atlext::OCL::Iterator,
)
atlext::OCL::TuplePart_strategy = st.builds(
    atlext::OCL::TuplePart,
)
atlext::ATL::PatternElement_strategy = st.builds(
    atlext::ATL::PatternElement,
)
RuleVariableDeclaration_strategy = st.builds(
    RuleVariableDeclaration,
)
ActionBlock_strategy = st.builds(
    ActionBlock,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
atlext::ATL::SimpleInPatternElement_strategy = st.builds(
    atlext::ATL::SimpleInPatternElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
StaticRule_strategy = st.builds(
    StaticRule,
)
atlext::ATL::CalledRule_strategy = st.builds(
    atlext::ATL::CalledRule,
    isEntrypoint=
        safe_text,
    isEndpoint=
        safe_text
)
ATL::StaticRule_strategy = st.builds(
    ATL::StaticRule,
)
ATL::RuleWithPattern_strategy = st.builds(
    ATL::RuleWithPattern,
)
atlext::ATL::LazyRule_strategy = st.builds(
    atlext::ATL::LazyRule,
    isUnique=
        safe_text
)
RuleWithPattern_strategy = st.builds(
    RuleWithPattern,
)
atlext::ATL::MatchedRule_strategy = st.builds(
    atlext::ATL::MatchedRule,
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
atlext::ATL::RuleWithPattern_strategy = st.builds(
    atlext::ATL::RuleWithPattern,
    isRefining=
        safe_text,
    isAbstract=
        safe_text,
    isNoDefault=
        safe_text
)
CallableParameter_strategy = st.builds(
    CallableParameter,
)
atlext::ATL::Callable_strategy = st.builds(
    atlext::ATL::Callable,
)
Callable_strategy = st.builds(
    Callable,
)
atlext::ATL::ModuleCallable_strategy = st.builds(
    atlext::ATL::ModuleCallable,
)
ATL::Rule_strategy = st.builds(
    ATL::Rule,
)
Unit_strategy = st.builds(
    Unit,
)
atlext::ATL::Library_strategy = st.builds(
    atlext::ATL::Library,
)
LibraryRef_strategy = st.builds(
    LibraryRef,
)
OutPattern_strategy = st.builds(
    OutPattern,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
atlext::OCL::LoopExp_strategy = st.builds(
    atlext::OCL::LoopExp,
)
atlext::OCL::OperationCallExp_strategy = st.builds(
    atlext::OCL::OperationCallExp,
    operationName=
        safe_text
)
atlext::OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    atlext::OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
)
ATL::ModuleCallable_strategy = st.builds(
    ATL::ModuleCallable,
)
atlext::ATL::StaticRule_strategy = st.builds(
    atlext::ATL::StaticRule,
)
ATL::Helper_strategy = st.builds(
    ATL::Helper,
)
atlext::ATL::StaticHelper_strategy = st.builds(
    atlext::ATL::StaticHelper,
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
atlext::ATL::Helper_strategy = st.builds(
    atlext::ATL::Helper,
    hasContext=
        st.booleans(),
    isAttribute=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
atlext::ATL::Rule_strategy = st.builds(
    atlext::ATL::Rule,
    name=
        safe_text
)
OclModel_strategy = st.builds(
    OclModel,
)
atlext::ATL::Module_strategy = st.builds(
    atlext::ATL::Module,
    isRefining=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atlext::OCL::PrimitiveExp_strategy = st.builds(
    atlext::OCL::PrimitiveExp,
)
atlext::OCL::JavaBody_strategy = st.builds(
    atlext::OCL::JavaBody,
)
atlext::OCL::MapExp_strategy = st.builds(
    atlext::OCL::MapExp,
)
atlext::OCL::PropertyCallExp_strategy = st.builds(
    atlext::OCL::PropertyCallExp,
    isStaticCall=
        st.booleans()
)
atlext::OCL::VariableExp_strategy = st.builds(
    atlext::OCL::VariableExp,
)
atlext::OCL::IfExp_strategy = st.builds(
    atlext::OCL::IfExp,
)
atlext::OCL::EnumLiteralExp_strategy = st.builds(
    atlext::OCL::EnumLiteralExp,
    name=
        safe_text
)
atlext::OCL::OclUndefinedExp_strategy = st.builds(
    atlext::OCL::OclUndefinedExp,
)
atlext::OCL::OclType_strategy = st.builds(
    atlext::OCL::OclType,
    name=
        safe_text
)
atlext::OCL::LetExp_strategy = st.builds(
    atlext::OCL::LetExp,
)
atlext::OCL::SuperExp_strategy = st.builds(
    atlext::OCL::SuperExp,
)
atlext::OCL::CollectionExp_strategy = st.builds(
    atlext::OCL::CollectionExp,
)
atlext::OCL::TupleExp_strategy = st.builds(
    atlext::OCL::TupleExp,
)
atlext::ATL::Query_strategy = st.builds(
    atlext::ATL::Query,
)
Helper_strategy = st.builds(
    Helper,
)
atlext::ATL::ContextHelper_strategy = st.builds(
    atlext::ATL::ContextHelper,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
atlext::ATL::ActionBlock_strategy = st.builds(
    atlext::ATL::ActionBlock,
)
atlext::ATL::ModuleElement_strategy = st.builds(
    atlext::ATL::ModuleElement,
)
atlext::OCL::OclModel_strategy = st.builds(
    atlext::OCL::OclModel,
    name=
        safe_text
)
atlext::ATL::DropPattern_strategy = st.builds(
    atlext::ATL::DropPattern,
)
atlext::OCL::OclFeatureDefinition_strategy = st.builds(
    atlext::OCL::OclFeatureDefinition,
)
atlext::ATL::LibraryRef_strategy = st.builds(
    atlext::ATL::LibraryRef,
    name=
        safe_text
)
atlext::OCL::OclContextDefinition_strategy = st.builds(
    atlext::OCL::OclContextDefinition,
)
atlext::ATL::OutPattern_strategy = st.builds(
    atlext::ATL::OutPattern,
)
atlext::OCL::TupleTypeAttribute_strategy = st.builds(
    atlext::OCL::TupleTypeAttribute,
    name=
        safe_text
)
atlext::ATL::Statement_strategy = st.builds(
    atlext::ATL::Statement,
)
atlext::OCL::OclFeature_strategy = st.builds(
    atlext::OCL::OclFeature,
)
atlext::ATL::Binding_strategy = st.builds(
    atlext::ATL::Binding,
    propertyName=
        safe_text,
    isAssignment=
        safe_text
)
atlext::ATL::InPattern_strategy = st.builds(
    atlext::ATL::InPattern,
)
atlext::OCL::MapElement_strategy = st.builds(
    atlext::OCL::MapElement,
)
atlext::ATL::Unit_strategy = st.builds(
    atlext::ATL::Unit,
    name=
        safe_text
)
StringToStringMap_strategy = st.builds(
    StringToStringMap,
)
atlext::ATL::LocatedElement_strategy = st.builds(
    atlext::ATL::LocatedElement,
    fileLocation=
        safe_text,
    commentsAfter=
        safe_text,
    fileObject=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)

@given(instance=JavaBody_strategy)
@settings(max_examples=50)
def test_javabody_instantiation(instance):
    assert isinstance(instance, JavaBody)

@given(instance=atlext::OCL::GetAppliedStereotypesBody_strategy)
@settings(max_examples=50)
def test_atlext::ocl::getappliedstereotypesbody_instantiation(instance):
    assert isinstance(instance, atlext::OCL::GetAppliedStereotypesBody)

@given(instance=atlext::OCL::TypedElement_strategy)
@settings(max_examples=50)
def test_atlext::ocl::typedelement_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TypedElement)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=atlext::OCL::Operation_strategy)
@settings(max_examples=50)
def test_atlext::ocl::operation_instantiation(instance):
    assert isinstance(instance, atlext::OCL::Operation)

@given(instance=atlext::OCL::Operation_strategy)
def test_atlext::ocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::Operation_strategy)
def test_atlext::ocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::OCL::Attribute_strategy)
@settings(max_examples=50)
def test_atlext::ocl::attribute_instantiation(instance):
    assert isinstance(instance, atlext::OCL::Attribute)

@given(instance=atlext::OCL::Attribute_strategy)
def test_atlext::ocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::Attribute_strategy)
def test_atlext::ocl::attribute_name_setter(instance):
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

@given(instance=atlext::OCL::RealType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::realtype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::RealType)

@given(instance=atlext::OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::integertype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=atlext::OCL::NumericType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::numerictype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::NumericType)

@given(instance=atlext::OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::booleantype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::BooleanType)

@given(instance=atlext::OCL::StringType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::stringtype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::StringType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=atlext::OCL::BagType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::bagtype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::BagType)

@given(instance=atlext::OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::SequenceType)

@given(instance=atlext::OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OrderedSetType)

@given(instance=atlext::OCL::SetType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::settype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::SetType)

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

@given(instance=ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_resolvetempresolution_instantiation(instance):
    assert isinstance(instance, ResolveTempResolution)

@given(instance=ContextHelper_strategy)
@settings(max_examples=50)
def test_contexthelper_instantiation(instance):
    assert isinstance(instance, ContextHelper)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

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

@given(instance=atlext::OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::integerexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::IntegerExp)

@given(instance=atlext::OCL::IntegerExp_strategy)
def test_atlext::ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=atlext::OCL::IntegerExp_strategy)
def test_atlext::ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=atlext::OCL::RealExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::realexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::RealExp)

@given(instance=atlext::OCL::RealExp_strategy)
def test_atlext::ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=atlext::OCL::RealExp_strategy)
def test_atlext::ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=atlext::OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::numericexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::NumericExp)

@given(instance=atlext::OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::BooleanExp)

@given(instance=atlext::OCL::BooleanExp_strategy)
def test_atlext::ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=atlext::OCL::BooleanExp_strategy)
def test_atlext::ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=atlext::OCL::StringExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::stringexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::StringExp)

@given(instance=atlext::OCL::StringExp_strategy)
def test_atlext::ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=atlext::OCL::StringExp_strategy)
def test_atlext::ocl::stringexp_stringSymbol_setter(instance):
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

@given(instance=atlext::OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::CollectionOperationCallExp)

@given(instance=atlext::OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OperatorCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=atlext::OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::IterateExp)

@given(instance=atlext::OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::IteratorExp)

@given(instance=atlext::OCL::IteratorExp_strategy)
def test_atlext::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::IteratorExp_strategy)
def test_atlext::ocl::iteratorexp_name_setter(instance):
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

@given(instance=atlext::OCL::BagExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::bagexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::BagExp)

@given(instance=atlext::OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OrderedSetExp)

@given(instance=atlext::OCL::SetExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::setexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::SetExp)

@given(instance=atlext::OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::SequenceExp)

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=atlext::OCL::MapType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::maptype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::MapType)

@given(instance=atlext::OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclAnyType)

@given(instance=atlext::OCL::Primitive_strategy)
@settings(max_examples=50)
def test_atlext::ocl::primitive_instantiation(instance):
    assert isinstance(instance, atlext::OCL::Primitive)

@given(instance=atlext::OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclModelElement)

@given(instance=atlext::OCL::TupleType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::tupletype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TupleType)

@given(instance=atlext::OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::CollectionType)

@given(instance=OCL::TypedElement_strategy)
@settings(max_examples=50)
def test_ocl::typedelement_instantiation(instance):
    assert isinstance(instance, OCL::TypedElement)

@given(instance=ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_atl::locatedelement_instantiation(instance):
    assert isinstance(instance, ATL::LocatedElement)

@given(instance=atlext::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlext::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, atlext::OCL::VariableDeclaration)

@given(instance=atlext::OCL::VariableDeclaration_strategy)
def test_atlext::ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=atlext::OCL::VariableDeclaration_strategy)
def test_atlext::ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=atlext::OCL::VariableDeclaration_strategy)
def test_atlext::ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=atlext::OCL::VariableDeclaration_strategy)
def test_atlext::ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=atlext::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclExpression)

@given(instance=atlext::OCL::OclExpression_strategy)
def test_atlext::ocl::oclexpression_implicitlyCasted_type(instance):
    assert isinstance(instance.implicitlyCasted, str)


@given(instance=atlext::OCL::OclExpression_strategy)
def test_atlext::ocl::oclexpression_implicitlyCasted_setter(instance):
    original = instance.implicitlyCasted
    instance.implicitlyCasted = original
    assert instance.implicitlyCasted == original

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=atlext::ATL::RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_atlext::atl::ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, atlext::ATL::RuleResolutionInfo)

@given(instance=atlext::ATL::CallableParameter_strategy)
@settings(max_examples=50)
def test_atlext::atl::callableparameter_instantiation(instance):
    assert isinstance(instance, atlext::ATL::CallableParameter)

@given(instance=atlext::ATL::CallableParameter_strategy)
def test_atlext::atl::callableparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::ATL::CallableParameter_strategy)
def test_atlext::atl::callableparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::ATL::StringToStringMap_strategy)
@settings(max_examples=50)
def test_atlext::atl::stringtostringmap_instantiation(instance):
    assert isinstance(instance, atlext::ATL::StringToStringMap)

@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=atlext::ATL::ForStat_strategy)
@settings(max_examples=50)
def test_atlext::atl::forstat_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ForStat)

@given(instance=atlext::ATL::BindingStat_strategy)
@settings(max_examples=50)
def test_atlext::atl::bindingstat_instantiation(instance):
    assert isinstance(instance, atlext::ATL::BindingStat)

@given(instance=atlext::ATL::BindingStat_strategy)
def test_atlext::atl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atlext::ATL::BindingStat_strategy)
def test_atlext::atl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atlext::ATL::BindingStat_strategy)
def test_atlext::atl::bindingstat_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=atlext::ATL::BindingStat_strategy)
def test_atlext::atl::bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atlext::ATL::IfStat_strategy)
@settings(max_examples=50)
def test_atlext::atl::ifstat_instantiation(instance):
    assert isinstance(instance, atlext::ATL::IfStat)

@given(instance=atlext::ATL::ExpressionStat_strategy)
@settings(max_examples=50)
def test_atlext::atl::expressionstat_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ExpressionStat)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, RuleResolutionInfo)

@given(instance=atlext::OCL::ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_atlext::ocl::resolvetempresolution_instantiation(instance):
    assert isinstance(instance, atlext::OCL::ResolveTempResolution)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=atlext::ATL::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ForEachOutPatternElement)

@given(instance=atlext::ATL::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::SimpleOutPatternElement)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=PatternElement_strategy)
@settings(max_examples=50)
def test_patternelement_instantiation(instance):
    assert isinstance(instance, PatternElement)

@given(instance=atlext::ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::OutPatternElement)

@given(instance=atlext::ATL::InPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::inpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=atlext::ATL::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlext::atl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, atlext::ATL::RuleVariableDeclaration)

@given(instance=atlext::OCL::Parameter_strategy)
@settings(max_examples=50)
def test_atlext::ocl::parameter_instantiation(instance):
    assert isinstance(instance, atlext::OCL::Parameter)

@given(instance=atlext::OCL::Iterator_strategy)
@settings(max_examples=50)
def test_atlext::ocl::iterator_instantiation(instance):
    assert isinstance(instance, atlext::OCL::Iterator)

@given(instance=atlext::OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_atlext::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TuplePart)

@given(instance=atlext::ATL::PatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::patternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::PatternElement)

@given(instance=RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, RuleVariableDeclaration)

@given(instance=ActionBlock_strategy)
@settings(max_examples=50)
def test_actionblock_instantiation(instance):
    assert isinstance(instance, ActionBlock)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=atlext::ATL::SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::SimpleInPatternElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=StaticRule_strategy)
@settings(max_examples=50)
def test_staticrule_instantiation(instance):
    assert isinstance(instance, StaticRule)

@given(instance=atlext::ATL::CalledRule_strategy)
@settings(max_examples=50)
def test_atlext::atl::calledrule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::CalledRule)

@given(instance=atlext::ATL::CalledRule_strategy)
def test_atlext::atl::calledrule_isEntrypoint_type(instance):
    assert isinstance(instance.isEntrypoint, str)


@given(instance=atlext::ATL::CalledRule_strategy)
def test_atlext::atl::calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=atlext::ATL::CalledRule_strategy)
def test_atlext::atl::calledrule_isEndpoint_type(instance):
    assert isinstance(instance.isEndpoint, str)


@given(instance=atlext::ATL::CalledRule_strategy)
def test_atlext::atl::calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original

@given(instance=ATL::StaticRule_strategy)
@settings(max_examples=50)
def test_atl::staticrule_instantiation(instance):
    assert isinstance(instance, ATL::StaticRule)

@given(instance=ATL::RuleWithPattern_strategy)
@settings(max_examples=50)
def test_atl::rulewithpattern_instantiation(instance):
    assert isinstance(instance, ATL::RuleWithPattern)

@given(instance=atlext::ATL::LazyRule_strategy)
@settings(max_examples=50)
def test_atlext::atl::lazyrule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::LazyRule)

@given(instance=atlext::ATL::LazyRule_strategy)
def test_atlext::atl::lazyrule_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=atlext::ATL::LazyRule_strategy)
def test_atlext::atl::lazyrule_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=RuleWithPattern_strategy)
@settings(max_examples=50)
def test_rulewithpattern_instantiation(instance):
    assert isinstance(instance, RuleWithPattern)

@given(instance=atlext::ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_atlext::atl::matchedrule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::MatchedRule)

@given(instance=InPattern_strategy)
@settings(max_examples=50)
def test_inpattern_instantiation(instance):
    assert isinstance(instance, InPattern)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=atlext::ATL::RuleWithPattern_strategy)
@settings(max_examples=50)
def test_atlext::atl::rulewithpattern_instantiation(instance):
    assert isinstance(instance, atlext::ATL::RuleWithPattern)

@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isNoDefault_type(instance):
    assert isinstance(instance.isNoDefault, str)


@given(instance=atlext::ATL::RuleWithPattern_strategy)
def test_atlext::atl::rulewithpattern_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original

@given(instance=CallableParameter_strategy)
@settings(max_examples=50)
def test_callableparameter_instantiation(instance):
    assert isinstance(instance, CallableParameter)

@given(instance=atlext::ATL::Callable_strategy)
@settings(max_examples=50)
def test_atlext::atl::callable_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Callable)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=atlext::ATL::ModuleCallable_strategy)
@settings(max_examples=50)
def test_atlext::atl::modulecallable_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ModuleCallable)

@given(instance=ATL::Rule_strategy)
@settings(max_examples=50)
def test_atl::rule_instantiation(instance):
    assert isinstance(instance, ATL::Rule)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=atlext::ATL::Library_strategy)
@settings(max_examples=50)
def test_atlext::atl::library_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Library)

@given(instance=LibraryRef_strategy)
@settings(max_examples=50)
def test_libraryref_instantiation(instance):
    assert isinstance(instance, LibraryRef)

@given(instance=OutPattern_strategy)
@settings(max_examples=50)
def test_outpattern_instantiation(instance):
    assert isinstance(instance, OutPattern)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=atlext::OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::LoopExp)

@given(instance=atlext::OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OperationCallExp)

@given(instance=atlext::OCL::OperationCallExp_strategy)
def test_atlext::ocl::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=atlext::OCL::OperationCallExp_strategy)
def test_atlext::ocl::operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=atlext::OCL::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::NavigationOrAttributeCallExp)

@given(instance=atlext::OCL::NavigationOrAttributeCallExp_strategy)
def test_atlext::ocl::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::NavigationOrAttributeCallExp_strategy)
def test_atlext::ocl::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ATL::ModuleCallable_strategy)
@settings(max_examples=50)
def test_atl::modulecallable_instantiation(instance):
    assert isinstance(instance, ATL::ModuleCallable)

@given(instance=atlext::ATL::StaticRule_strategy)
@settings(max_examples=50)
def test_atlext::atl::staticrule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::StaticRule)

@given(instance=ATL::Helper_strategy)
@settings(max_examples=50)
def test_atl::helper_instantiation(instance):
    assert isinstance(instance, ATL::Helper)

@given(instance=atlext::ATL::StaticHelper_strategy)
@settings(max_examples=50)
def test_atlext::atl::statichelper_instantiation(instance):
    assert isinstance(instance, atlext::ATL::StaticHelper)

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

@given(instance=atlext::ATL::Helper_strategy)
@settings(max_examples=50)
def test_atlext::atl::helper_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Helper)

@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_hasContext_type(instance):
    assert isinstance(instance.hasContext, bool)


@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_hasContext_setter(instance):
    original = instance.hasContext
    instance.hasContext = original
    assert instance.hasContext == original

@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_isAttribute_type(instance):
    assert isinstance(instance.isAttribute, str)


@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_isAttribute_setter(instance):
    original = instance.isAttribute
    instance.isAttribute = original
    assert instance.isAttribute == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=atlext::ATL::Rule_strategy)
@settings(max_examples=50)
def test_atlext::atl::rule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Rule)

@given(instance=atlext::ATL::Rule_strategy)
def test_atlext::atl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::ATL::Rule_strategy)
def test_atlext::atl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=atlext::ATL::Module_strategy)
@settings(max_examples=50)
def test_atlext::atl::module_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Module)

@given(instance=atlext::ATL::Module_strategy)
def test_atlext::atl::module_isRefining_type(instance):
    assert isinstance(instance.isRefining, str)


@given(instance=atlext::ATL::Module_strategy)
def test_atlext::atl::module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atlext::OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::PrimitiveExp)

@given(instance=atlext::OCL::JavaBody_strategy)
@settings(max_examples=50)
def test_atlext::ocl::javabody_instantiation(instance):
    assert isinstance(instance, atlext::OCL::JavaBody)

@given(instance=atlext::OCL::MapExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::mapexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::MapExp)

@given(instance=atlext::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::PropertyCallExp)

@given(instance=atlext::OCL::PropertyCallExp_strategy)
def test_atlext::ocl::propertycallexp_isStaticCall_type(instance):
    assert isinstance(instance.isStaticCall, bool)


@given(instance=atlext::OCL::PropertyCallExp_strategy)
def test_atlext::ocl::propertycallexp_isStaticCall_setter(instance):
    original = instance.isStaticCall
    instance.isStaticCall = original
    assert instance.isStaticCall == original

@given(instance=atlext::OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::variableexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::VariableExp)

@given(instance=atlext::OCL::IfExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::IfExp)

@given(instance=atlext::OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::EnumLiteralExp)

@given(instance=atlext::OCL::EnumLiteralExp_strategy)
def test_atlext::ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::EnumLiteralExp_strategy)
def test_atlext::ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclUndefinedExp)

@given(instance=atlext::OCL::OclType_strategy)
@settings(max_examples=50)
def test_atlext::ocl::ocltype_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclType)

@given(instance=atlext::OCL::OclType_strategy)
def test_atlext::ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::OclType_strategy)
def test_atlext::ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::OCL::LetExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::letexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::LetExp)

@given(instance=atlext::OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::superexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::SuperExp)

@given(instance=atlext::OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::CollectionExp)

@given(instance=atlext::OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TupleExp)

@given(instance=atlext::ATL::Query_strategy)
@settings(max_examples=50)
def test_atlext::atl::query_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Query)

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=atlext::ATL::ContextHelper_strategy)
@settings(max_examples=50)
def test_atlext::atl::contexthelper_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ContextHelper)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=atlext::ATL::ActionBlock_strategy)
@settings(max_examples=50)
def test_atlext::atl::actionblock_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ActionBlock)

@given(instance=atlext::ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::moduleelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ModuleElement)

@given(instance=atlext::OCL::OclModel_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclModel)

@given(instance=atlext::OCL::OclModel_strategy)
def test_atlext::ocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::OclModel_strategy)
def test_atlext::ocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::ATL::DropPattern_strategy)
@settings(max_examples=50)
def test_atlext::atl::droppattern_instantiation(instance):
    assert isinstance(instance, atlext::ATL::DropPattern)

@given(instance=atlext::OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclFeatureDefinition)

@given(instance=atlext::ATL::LibraryRef_strategy)
@settings(max_examples=50)
def test_atlext::atl::libraryref_instantiation(instance):
    assert isinstance(instance, atlext::ATL::LibraryRef)

@given(instance=atlext::ATL::LibraryRef_strategy)
def test_atlext::atl::libraryref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::ATL::LibraryRef_strategy)
def test_atlext::atl::libraryref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclContextDefinition)

@given(instance=atlext::ATL::OutPattern_strategy)
@settings(max_examples=50)
def test_atlext::atl::outpattern_instantiation(instance):
    assert isinstance(instance, atlext::ATL::OutPattern)

@given(instance=atlext::OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_atlext::ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TupleTypeAttribute)

@given(instance=atlext::OCL::TupleTypeAttribute_strategy)
def test_atlext::ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::OCL::TupleTypeAttribute_strategy)
def test_atlext::ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlext::ATL::Statement_strategy)
@settings(max_examples=50)
def test_atlext::atl::statement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Statement)

@given(instance=atlext::OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclFeature)

@given(instance=atlext::ATL::Binding_strategy)
@settings(max_examples=50)
def test_atlext::atl::binding_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Binding)

@given(instance=atlext::ATL::Binding_strategy)
def test_atlext::atl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atlext::ATL::Binding_strategy)
def test_atlext::atl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atlext::ATL::Binding_strategy)
def test_atlext::atl::binding_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, str)


@given(instance=atlext::ATL::Binding_strategy)
def test_atlext::atl::binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atlext::ATL::InPattern_strategy)
@settings(max_examples=50)
def test_atlext::atl::inpattern_instantiation(instance):
    assert isinstance(instance, atlext::ATL::InPattern)

@given(instance=atlext::OCL::MapElement_strategy)
@settings(max_examples=50)
def test_atlext::ocl::mapelement_instantiation(instance):
    assert isinstance(instance, atlext::OCL::MapElement)

@given(instance=atlext::ATL::Unit_strategy)
@settings(max_examples=50)
def test_atlext::atl::unit_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Unit)

@given(instance=atlext::ATL::Unit_strategy)
def test_atlext::atl::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::ATL::Unit_strategy)
def test_atlext::atl::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StringToStringMap_strategy)
@settings(max_examples=50)
def test_stringtostringmap_instantiation(instance):
    assert isinstance(instance, StringToStringMap)

@given(instance=atlext::ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::locatedelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::LocatedElement)

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileLocation_type(instance):
    assert isinstance(instance.fileLocation, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileLocation_setter(instance):
    original = instance.fileLocation
    instance.fileLocation = original
    assert instance.fileLocation == original

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileObject_type(instance):
    assert isinstance(instance.fileObject, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileObject_setter(instance):
    original = instance.fileObject
    instance.fileObject = original
    assert instance.fileObject == original

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
