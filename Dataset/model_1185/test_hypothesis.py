import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclModelElement,
    atl::n::ocl::OCL::OclModel,
    atl::n::ocl::OCL::TupleTypeAttribute,
    TupleTypeAttribute,
    CollectionType,
    atl::n::ocl::OCL::SetType,
    atl::n::ocl::OCL::SequenceType,
    atl::n::ocl::OCL::OrderedSetType,
    atl::n::ocl::OCL::BagType,
    NumericType,
    atl::n::ocl::OCL::RealType,
    atl::n::ocl::OCL::IntegerType,
    Primitive,
    atl::n::ocl::OCL::BooleanType,
    atl::n::ocl::OCL::NumericType,
    atl::n::ocl::OCL::OclFeature,
    atl::n::ocl::OCL::OclContextDefinition,
    OclContextDefinition,
    OclFeature,
    atl::n::ocl::OCL::Operation,
    atl::n::ocl::OCL::Attribute,
    atl::n::ocl::OCL::OclFeatureDefinition,
    LoopExp,
    atl::n::ocl::OCL::IteratorExp,
    atl::n::ocl::OCL::IterateExp,
    atl::n::ocl::OCL::StringType,
    atl::n::ocl::OCL::VariableDeclaration,
    atl::n::ocl::OCL::MapElement,
    MapElement,
    TupleExp,
    TuplePart,
    CollectionExp,
    atl::n::ocl::OCL::SequenceExp,
    atl::n::ocl::OCL::SetExp,
    atl::n::ocl::OCL::OrderedSetExp,
    atl::n::ocl::OCL::BagExp,
    OperationCallExp,
    atl::n::ocl::OCL::CollectionOperationCallExp,
    atl::n::ocl::OCL::OperatorCallExp,
    PropertyCallExp,
    atl::n::ocl::OCL::OperationCallExp,
    atl::n::ocl::OCL::LoopExp,
    atl::n::ocl::OCL::NavigationOrAttributeCallExp,
    NumericExp,
    atl::n::ocl::OCL::IntegerExp,
    atl::n::ocl::OCL::RealExp,
    PrimitiveExp,
    atl::n::ocl::OCL::NumericExp,
    atl::n::ocl::OCL::BooleanExp,
    atl::n::ocl::OCL::StringExp,
    OclType,
    atl::n::ocl::OCL::MapType,
    atl::n::ocl::OCL::OclModelElement,
    atl::n::ocl::OCL::CollectionType,
    atl::n::ocl::OCL::OclAnyType,
    atl::n::ocl::OCL::TupleType,
    atl::n::ocl::OCL::Primitive,
    atl::n::ocl::OCL::OclExpression,
    PatternElement,
    atl::n::ocl::ATL::OutPatternElement,
    atl::n::ocl::ATL::InPatternElement,
    VariableDeclaration,
    atl::n::ocl::OCL::TuplePart,
    atl::n::ocl::OCL::Parameter,
    atl::n::ocl::OCL::Iterator,
    atl::n::ocl::ATL::PatternElement,
    atl::n::ocl::ATL::DropPattern,
    OutPatternElement,
    DropPattern,
    atl::n::ocl::ATL::OutPattern,
    InPatternElement,
    atl::n::ocl::ATL::SimpleInPatternElement,
    atl::n::ocl::ATL::InPattern,
    atl::n::ocl::ATL::Statement,
    Statement,
    atl::n::ocl::ATL::IfStat,
    atl::n::ocl::ATL::ForStat,
    atl::n::ocl::ATL::BindingStat,
    atl::n::ocl::ATL::ExpressionStat,
    atl::n::ocl::ATL::ActionBlock,
    atl::n::ocl::ATL::RuleVariableDeclaration,
    atl::n::ocl::ATL::Binding,
    Iterator,
    atl::n::ocl::ATL::ForEachOutPatternElement,
    atl::n::ocl::ATL::SimpleOutPatternElement,
    Binding,
    atl::n::ocl::ATL::ModuleElement,
    ModuleElement,
    atl::n::ocl::ATL::Helper,
    OclModel,
    atl::n::ocl::ATL::Module,
    Helper,
    OclExpression,
    atl::n::ocl::OCL::OclUndefinedExp,
    atl::n::ocl::OCL::TupleExp,
    atl::n::ocl::OCL::IfExp,
    atl::n::ocl::OCL::PropertyCallExp,
    atl::n::ocl::OCL::LetExp,
    atl::n::ocl::OCL::VariableExp,
    atl::n::ocl::OCL::OclType,
    atl::n::ocl::OCL::CollectionExp,
    atl::n::ocl::OCL::MapExp,
    atl::n::ocl::OCL::EnumLiteralExp,
    atl::n::ocl::OCL::SuperExp,
    atl::n::ocl::OCL::PrimitiveExp,
    atl::n::ocl::ATL::Query,
    Parameter,
    MatchedRule,
    atl::n::ocl::ATL::LazyMatchedRule,
    InPattern,
    Rule,
    atl::n::ocl::ATL::CalledRule,
    atl::n::ocl::ATL::MatchedRule,
    RuleVariableDeclaration,
    ActionBlock,
    OutPattern,
    atl::n::ocl::ATL::Rule,
    OclFeatureDefinition,
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



def test_atl::n::ocl::ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclModel)


def test_atl::n::ocl::ocl::oclmodel_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclModel.__init__)


def test_atl::n::ocl::ocl::oclmodel_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::oclmodel_has_name():
    assert hasattr(atl::n::ocl::OCL::OclModel, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::TupleTypeAttribute)


def test_atl::n::ocl::ocl::tupletypeattribute_constructor_exists():
    assert callable(atl::n::ocl::OCL::TupleTypeAttribute.__init__)


def test_atl::n::ocl::ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::tupletypeattribute_has_name():
    assert hasattr(atl::n::ocl::OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_atl::n::ocl::ocl::settype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::SetType)


def test_atl::n::ocl::ocl::settype_constructor_exists():
    assert callable(atl::n::ocl::OCL::SetType.__init__)


def test_atl::n::ocl::ocl::settype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::SequenceType)


def test_atl::n::ocl::ocl::sequencetype_constructor_exists():
    assert callable(atl::n::ocl::OCL::SequenceType.__init__)


def test_atl::n::ocl::ocl::sequencetype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OrderedSetType)


def test_atl::n::ocl::ocl::orderedsettype_constructor_exists():
    assert callable(atl::n::ocl::OCL::OrderedSetType.__init__)


def test_atl::n::ocl::ocl::orderedsettype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::BagType)


def test_atl::n::ocl::ocl::bagtype_constructor_exists():
    assert callable(atl::n::ocl::OCL::BagType.__init__)


def test_atl::n::ocl::ocl::bagtype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::RealType)


def test_atl::n::ocl::ocl::realtype_constructor_exists():
    assert callable(atl::n::ocl::OCL::RealType.__init__)


def test_atl::n::ocl::ocl::realtype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::IntegerType)


def test_atl::n::ocl::ocl::integertype_constructor_exists():
    assert callable(atl::n::ocl::OCL::IntegerType.__init__)


def test_atl::n::ocl::ocl::integertype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::BooleanType)


def test_atl::n::ocl::ocl::booleantype_constructor_exists():
    assert callable(atl::n::ocl::OCL::BooleanType.__init__)


def test_atl::n::ocl::ocl::booleantype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::NumericType)


def test_atl::n::ocl::ocl::numerictype_constructor_exists():
    assert callable(atl::n::ocl::OCL::NumericType.__init__)


def test_atl::n::ocl::ocl::numerictype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclFeature)


def test_atl::n::ocl::ocl::oclfeature_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclFeature.__init__)


def test_atl::n::ocl::ocl::oclfeature_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclContextDefinition)


def test_atl::n::ocl::ocl::oclcontextdefinition_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclContextDefinition.__init__)


def test_atl::n::ocl::ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::Operation)


def test_atl::n::ocl::ocl::operation_constructor_exists():
    assert callable(atl::n::ocl::OCL::Operation.__init__)


def test_atl::n::ocl::ocl::operation_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::operation_has_name():
    assert hasattr(atl::n::ocl::OCL::Operation, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::Attribute)


def test_atl::n::ocl::ocl::attribute_constructor_exists():
    assert callable(atl::n::ocl::OCL::Attribute.__init__)


def test_atl::n::ocl::ocl::attribute_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::attribute_has_name():
    assert hasattr(atl::n::ocl::OCL::Attribute, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclFeatureDefinition)


def test_atl::n::ocl::ocl::oclfeaturedefinition_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclFeatureDefinition.__init__)


def test_atl::n::ocl::ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::IteratorExp)


def test_atl::n::ocl::ocl::iteratorexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::IteratorExp.__init__)


def test_atl::n::ocl::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::iteratorexp_has_name():
    assert hasattr(atl::n::ocl::OCL::IteratorExp, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::IterateExp)


def test_atl::n::ocl::ocl::iterateexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::IterateExp.__init__)


def test_atl::n::ocl::ocl::iterateexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::StringType)


def test_atl::n::ocl::ocl::stringtype_constructor_exists():
    assert callable(atl::n::ocl::OCL::StringType.__init__)


def test_atl::n::ocl::ocl::stringtype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::StringType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::VariableDeclaration)


def test_atl::n::ocl::ocl::variabledeclaration_constructor_exists():
    assert callable(atl::n::ocl::OCL::VariableDeclaration.__init__)


def test_atl::n::ocl::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "id" in params, "Missing parameter 'id'"

def test_atl::n::ocl::ocl::variabledeclaration_has_varName():
    assert hasattr(atl::n::ocl::OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in atl::n::ocl::OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::ocl::variabledeclaration_has_id():
    assert hasattr(atl::n::ocl::OCL::VariableDeclaration, "id")
    descriptor = None
    for klass in atl::n::ocl::OCL::VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::MapElement)


def test_atl::n::ocl::ocl::mapelement_constructor_exists():
    assert callable(atl::n::ocl::OCL::MapElement.__init__)


def test_atl::n::ocl::ocl::mapelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::MapElement.__init__)
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



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::SequenceExp)


def test_atl::n::ocl::ocl::sequenceexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::SequenceExp.__init__)


def test_atl::n::ocl::ocl::sequenceexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::SetExp)


def test_atl::n::ocl::ocl::setexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::SetExp.__init__)


def test_atl::n::ocl::ocl::setexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OrderedSetExp)


def test_atl::n::ocl::ocl::orderedsetexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::OrderedSetExp.__init__)


def test_atl::n::ocl::ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::BagExp)


def test_atl::n::ocl::ocl::bagexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::BagExp.__init__)


def test_atl::n::ocl::ocl::bagexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::CollectionOperationCallExp)


def test_atl::n::ocl::ocl::collectionoperationcallexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::CollectionOperationCallExp.__init__)


def test_atl::n::ocl::ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OperatorCallExp)


def test_atl::n::ocl::ocl::operatorcallexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::OperatorCallExp.__init__)


def test_atl::n::ocl::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OperationCallExp)


def test_atl::n::ocl::ocl::operationcallexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::OperationCallExp.__init__)


def test_atl::n::ocl::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_atl::n::ocl::ocl::operationcallexp_has_operationName():
    assert hasattr(atl::n::ocl::OCL::OperationCallExp, "operationName")
    descriptor = None
    for klass in atl::n::ocl::OCL::OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::LoopExp)


def test_atl::n::ocl::ocl::loopexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::LoopExp.__init__)


def test_atl::n::ocl::ocl::loopexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::NavigationOrAttributeCallExp)


def test_atl::n::ocl::ocl::navigationorattributecallexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::NavigationOrAttributeCallExp.__init__)


def test_atl::n::ocl::ocl::navigationorattributecallexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::navigationorattributecallexp_has_name():
    assert hasattr(atl::n::ocl::OCL::NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::IntegerExp)


def test_atl::n::ocl::ocl::integerexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::IntegerExp.__init__)


def test_atl::n::ocl::ocl::integerexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_atl::n::ocl::ocl::integerexp_has_integerSymbol():
    assert hasattr(atl::n::ocl::OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in atl::n::ocl::OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::RealExp)


def test_atl::n::ocl::ocl::realexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::RealExp.__init__)


def test_atl::n::ocl::ocl::realexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_atl::n::ocl::ocl::realexp_has_realSymbol():
    assert hasattr(atl::n::ocl::OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in atl::n::ocl::OCL::RealExp.__mro__:
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



def test_atl::n::ocl::ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::NumericExp)


def test_atl::n::ocl::ocl::numericexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::NumericExp.__init__)


def test_atl::n::ocl::ocl::numericexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::BooleanExp)


def test_atl::n::ocl::ocl::booleanexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::BooleanExp.__init__)


def test_atl::n::ocl::ocl::booleanexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_atl::n::ocl::ocl::booleanexp_has_booleanSymbol():
    assert hasattr(atl::n::ocl::OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in atl::n::ocl::OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::StringExp)


def test_atl::n::ocl::ocl::stringexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::StringExp.__init__)


def test_atl::n::ocl::ocl::stringexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_atl::n::ocl::ocl::stringexp_has_stringSymbol():
    assert hasattr(atl::n::ocl::OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in atl::n::ocl::OCL::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::MapType)


def test_atl::n::ocl::ocl::maptype_constructor_exists():
    assert callable(atl::n::ocl::OCL::MapType.__init__)


def test_atl::n::ocl::ocl::maptype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclModelElement)


def test_atl::n::ocl::ocl::oclmodelelement_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclModelElement.__init__)


def test_atl::n::ocl::ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::CollectionType)


def test_atl::n::ocl::ocl::collectiontype_constructor_exists():
    assert callable(atl::n::ocl::OCL::CollectionType.__init__)


def test_atl::n::ocl::ocl::collectiontype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclAnyType)


def test_atl::n::ocl::ocl::oclanytype_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclAnyType.__init__)


def test_atl::n::ocl::ocl::oclanytype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::TupleType)


def test_atl::n::ocl::ocl::tupletype_constructor_exists():
    assert callable(atl::n::ocl::OCL::TupleType.__init__)


def test_atl::n::ocl::ocl::tupletype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::Primitive)


def test_atl::n::ocl::ocl::primitive_constructor_exists():
    assert callable(atl::n::ocl::OCL::Primitive.__init__)


def test_atl::n::ocl::ocl::primitive_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclExpression)


def test_atl::n::ocl::ocl::oclexpression_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclExpression.__init__)


def test_atl::n::ocl::ocl::oclexpression_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_patternelement_is_not_abstract():
    assert not inspect.isabstract(PatternElement)


def test_patternelement_constructor_exists():
    assert callable(PatternElement.__init__)


def test_patternelement_constructor_args():
    sig = inspect.signature(PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::OutPatternElement)


def test_atl::n::ocl::atl::outpatternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::OutPatternElement.__init__)


def test_atl::n::ocl::atl::outpatternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::InPatternElement)


def test_atl::n::ocl::atl::inpatternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::InPatternElement.__init__)


def test_atl::n::ocl::atl::inpatternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::TuplePart)


def test_atl::n::ocl::ocl::tuplepart_constructor_exists():
    assert callable(atl::n::ocl::OCL::TuplePart.__init__)


def test_atl::n::ocl::ocl::tuplepart_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::Parameter)


def test_atl::n::ocl::ocl::parameter_constructor_exists():
    assert callable(atl::n::ocl::OCL::Parameter.__init__)


def test_atl::n::ocl::ocl::parameter_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::Iterator)


def test_atl::n::ocl::ocl::iterator_constructor_exists():
    assert callable(atl::n::ocl::OCL::Iterator.__init__)


def test_atl::n::ocl::ocl::iterator_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::patternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::PatternElement)


def test_atl::n::ocl::atl::patternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::PatternElement.__init__)


def test_atl::n::ocl::atl::patternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::droppattern_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::DropPattern)


def test_atl::n::ocl::atl::droppattern_constructor_exists():
    assert callable(atl::n::ocl::ATL::DropPattern.__init__)


def test_atl::n::ocl::atl::droppattern_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::DropPattern.__init__)
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



def test_atl::n::ocl::atl::outpattern_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::OutPattern)


def test_atl::n::ocl::atl::outpattern_constructor_exists():
    assert callable(atl::n::ocl::ATL::OutPattern.__init__)


def test_atl::n::ocl::atl::outpattern_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_inpatternelement_is_not_abstract():
    assert not inspect.isabstract(InPatternElement)


def test_inpatternelement_constructor_exists():
    assert callable(InPatternElement.__init__)


def test_inpatternelement_constructor_args():
    sig = inspect.signature(InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::SimpleInPatternElement)


def test_atl::n::ocl::atl::simpleinpatternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::SimpleInPatternElement.__init__)


def test_atl::n::ocl::atl::simpleinpatternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::SimpleInPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::inpattern_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::InPattern)


def test_atl::n::ocl::atl::inpattern_constructor_exists():
    assert callable(atl::n::ocl::ATL::InPattern.__init__)


def test_atl::n::ocl::atl::inpattern_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::statement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Statement)


def test_atl::n::ocl::atl::statement_constructor_exists():
    assert callable(atl::n::ocl::ATL::Statement.__init__)


def test_atl::n::ocl::atl::statement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::ifstat_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::IfStat)


def test_atl::n::ocl::atl::ifstat_constructor_exists():
    assert callable(atl::n::ocl::ATL::IfStat.__init__)


def test_atl::n::ocl::atl::ifstat_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::forstat_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::ForStat)


def test_atl::n::ocl::atl::forstat_constructor_exists():
    assert callable(atl::n::ocl::ATL::ForStat.__init__)


def test_atl::n::ocl::atl::forstat_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::ForStat.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::BindingStat)


def test_atl::n::ocl::atl::bindingstat_constructor_exists():
    assert callable(atl::n::ocl::ATL::BindingStat.__init__)


def test_atl::n::ocl::atl::bindingstat_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atl::n::ocl::atl::bindingstat_has_propertyName():
    assert hasattr(atl::n::ocl::ATL::BindingStat, "propertyName")
    descriptor = None
    for klass in atl::n::ocl::ATL::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::atl::bindingstat_has_isAssignment():
    assert hasattr(atl::n::ocl::ATL::BindingStat, "isAssignment")
    descriptor = None
    for klass in atl::n::ocl::ATL::BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::atl::expressionstat_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::ExpressionStat)


def test_atl::n::ocl::atl::expressionstat_constructor_exists():
    assert callable(atl::n::ocl::ATL::ExpressionStat.__init__)


def test_atl::n::ocl::atl::expressionstat_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::actionblock_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::ActionBlock)


def test_atl::n::ocl::atl::actionblock_constructor_exists():
    assert callable(atl::n::ocl::ATL::ActionBlock.__init__)


def test_atl::n::ocl::atl::actionblock_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::RuleVariableDeclaration)


def test_atl::n::ocl::atl::rulevariabledeclaration_constructor_exists():
    assert callable(atl::n::ocl::ATL::RuleVariableDeclaration.__init__)


def test_atl::n::ocl::atl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::binding_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Binding)


def test_atl::n::ocl::atl::binding_constructor_exists():
    assert callable(atl::n::ocl::ATL::Binding.__init__)


def test_atl::n::ocl::atl::binding_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_atl::n::ocl::atl::binding_has_isAssignment():
    assert hasattr(atl::n::ocl::ATL::Binding, "isAssignment")
    descriptor = None
    for klass in atl::n::ocl::ATL::Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::atl::binding_has_propertyName():
    assert hasattr(atl::n::ocl::ATL::Binding, "propertyName")
    descriptor = None
    for klass in atl::n::ocl::ATL::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::ForEachOutPatternElement)


def test_atl::n::ocl::atl::foreachoutpatternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::ForEachOutPatternElement.__init__)


def test_atl::n::ocl::atl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::SimpleOutPatternElement)


def test_atl::n::ocl::atl::simpleoutpatternelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::SimpleOutPatternElement.__init__)


def test_atl::n::ocl::atl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::ModuleElement)


def test_atl::n::ocl::atl::moduleelement_constructor_exists():
    assert callable(atl::n::ocl::ATL::ModuleElement.__init__)


def test_atl::n::ocl::atl::moduleelement_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::helper_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Helper)


def test_atl::n::ocl::atl::helper_constructor_exists():
    assert callable(atl::n::ocl::ATL::Helper.__init__)


def test_atl::n::ocl::atl::helper_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Helper.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::module_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Module)


def test_atl::n::ocl::atl::module_constructor_exists():
    assert callable(atl::n::ocl::ATL::Module.__init__)


def test_atl::n::ocl::atl::module_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atl::n::ocl::atl::module_has_isRefining():
    assert hasattr(atl::n::ocl::ATL::Module, "isRefining")
    descriptor = None
    for klass in atl::n::ocl::ATL::Module.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_helper_is_not_abstract():
    assert not inspect.isabstract(Helper)


def test_helper_constructor_exists():
    assert callable(Helper.__init__)


def test_helper_constructor_args():
    sig = inspect.signature(Helper.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclUndefinedExp)


def test_atl::n::ocl::ocl::oclundefinedexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclUndefinedExp.__init__)


def test_atl::n::ocl::ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::TupleExp)


def test_atl::n::ocl::ocl::tupleexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::TupleExp.__init__)


def test_atl::n::ocl::ocl::tupleexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::IfExp)


def test_atl::n::ocl::ocl::ifexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::IfExp.__init__)


def test_atl::n::ocl::ocl::ifexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::PropertyCallExp)


def test_atl::n::ocl::ocl::propertycallexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::PropertyCallExp.__init__)


def test_atl::n::ocl::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::LetExp)


def test_atl::n::ocl::ocl::letexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::LetExp.__init__)


def test_atl::n::ocl::ocl::letexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::VariableExp)


def test_atl::n::ocl::ocl::variableexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::VariableExp.__init__)


def test_atl::n::ocl::ocl::variableexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::OclType)


def test_atl::n::ocl::ocl::ocltype_constructor_exists():
    assert callable(atl::n::ocl::OCL::OclType.__init__)


def test_atl::n::ocl::ocl::ocltype_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::ocltype_has_name():
    assert hasattr(atl::n::ocl::OCL::OclType, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::CollectionExp)


def test_atl::n::ocl::ocl::collectionexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::CollectionExp.__init__)


def test_atl::n::ocl::ocl::collectionexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::MapExp)


def test_atl::n::ocl::ocl::mapexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::MapExp.__init__)


def test_atl::n::ocl::ocl::mapexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::EnumLiteralExp)


def test_atl::n::ocl::ocl::enumliteralexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::EnumLiteralExp.__init__)


def test_atl::n::ocl::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::ocl::enumliteralexp_has_name():
    assert hasattr(atl::n::ocl::OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in atl::n::ocl::OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::SuperExp)


def test_atl::n::ocl::ocl::superexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::SuperExp.__init__)


def test_atl::n::ocl::ocl::superexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::OCL::PrimitiveExp)


def test_atl::n::ocl::ocl::primitiveexp_constructor_exists():
    assert callable(atl::n::ocl::OCL::PrimitiveExp.__init__)


def test_atl::n::ocl::ocl::primitiveexp_constructor_args():
    sig = inspect.signature(atl::n::ocl::OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_atl::n::ocl::atl::query_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Query)


def test_atl::n::ocl::atl::query_constructor_exists():
    assert callable(atl::n::ocl::ATL::Query.__init__)


def test_atl::n::ocl::atl::query_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Query.__init__)
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



def test_atl::n::ocl::atl::lazymatchedrule_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::LazyMatchedRule)


def test_atl::n::ocl::atl::lazymatchedrule_constructor_exists():
    assert callable(atl::n::ocl::ATL::LazyMatchedRule.__init__)


def test_atl::n::ocl::atl::lazymatchedrule_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::LazyMatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_atl::n::ocl::atl::lazymatchedrule_has_isUnique():
    assert hasattr(atl::n::ocl::ATL::LazyMatchedRule, "isUnique")
    descriptor = None
    for klass in atl::n::ocl::ATL::LazyMatchedRule.__mro__:
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



def test_atl::n::ocl::atl::calledrule_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::CalledRule)


def test_atl::n::ocl::atl::calledrule_constructor_exists():
    assert callable(atl::n::ocl::ATL::CalledRule.__init__)


def test_atl::n::ocl::atl::calledrule_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"

def test_atl::n::ocl::atl::calledrule_has_isEndpoint():
    assert hasattr(atl::n::ocl::ATL::CalledRule, "isEndpoint")
    descriptor = None
    for klass in atl::n::ocl::ATL::CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::atl::calledrule_has_isEntrypoint():
    assert hasattr(atl::n::ocl::ATL::CalledRule, "isEntrypoint")
    descriptor = None
    for klass in atl::n::ocl::ATL::CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)



def test_atl::n::ocl::atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::MatchedRule)


def test_atl::n::ocl::atl::matchedrule_constructor_exists():
    assert callable(atl::n::ocl::ATL::MatchedRule.__init__)


def test_atl::n::ocl::atl::matchedrule_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::MatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_atl::n::ocl::atl::matchedrule_has_isRefining():
    assert hasattr(atl::n::ocl::ATL::MatchedRule, "isRefining")
    descriptor = None
    for klass in atl::n::ocl::ATL::MatchedRule.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::atl::matchedrule_has_isNoDefault():
    assert hasattr(atl::n::ocl::ATL::MatchedRule, "isNoDefault")
    descriptor = None
    for klass in atl::n::ocl::ATL::MatchedRule.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)

def test_atl::n::ocl::atl::matchedrule_has_isAbstract():
    assert hasattr(atl::n::ocl::ATL::MatchedRule, "isAbstract")
    descriptor = None
    for klass in atl::n::ocl::ATL::MatchedRule.__mro__:
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



def test_atl::n::ocl::atl::rule_is_not_abstract():
    assert not inspect.isabstract(atl::n::ocl::ATL::Rule)


def test_atl::n::ocl::atl::rule_constructor_exists():
    assert callable(atl::n::ocl::ATL::Rule.__init__)


def test_atl::n::ocl::atl::rule_constructor_args():
    sig = inspect.signature(atl::n::ocl::ATL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atl::n::ocl::atl::rule_has_name():
    assert hasattr(atl::n::ocl::ATL::Rule, "name")
    descriptor = None
    for klass in atl::n::ocl::ATL::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
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
atl::n::ocl::OCL::OclModel_strategy = st.builds(
    atl::n::ocl::OCL::OclModel,
    name=
        safe_text
)
atl::n::ocl::OCL::TupleTypeAttribute_strategy = st.builds(
    atl::n::ocl::OCL::TupleTypeAttribute,
    name=
        safe_text
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
atl::n::ocl::OCL::SetType_strategy = st.builds(
    atl::n::ocl::OCL::SetType,
)
atl::n::ocl::OCL::SequenceType_strategy = st.builds(
    atl::n::ocl::OCL::SequenceType,
)
atl::n::ocl::OCL::OrderedSetType_strategy = st.builds(
    atl::n::ocl::OCL::OrderedSetType,
)
atl::n::ocl::OCL::BagType_strategy = st.builds(
    atl::n::ocl::OCL::BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
atl::n::ocl::OCL::RealType_strategy = st.builds(
    atl::n::ocl::OCL::RealType,
)
atl::n::ocl::OCL::IntegerType_strategy = st.builds(
    atl::n::ocl::OCL::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
atl::n::ocl::OCL::BooleanType_strategy = st.builds(
    atl::n::ocl::OCL::BooleanType,
)
atl::n::ocl::OCL::NumericType_strategy = st.builds(
    atl::n::ocl::OCL::NumericType,
)
atl::n::ocl::OCL::OclFeature_strategy = st.builds(
    atl::n::ocl::OCL::OclFeature,
)
atl::n::ocl::OCL::OclContextDefinition_strategy = st.builds(
    atl::n::ocl::OCL::OclContextDefinition,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
atl::n::ocl::OCL::Operation_strategy = st.builds(
    atl::n::ocl::OCL::Operation,
    name=
        safe_text
)
atl::n::ocl::OCL::Attribute_strategy = st.builds(
    atl::n::ocl::OCL::Attribute,
    name=
        safe_text
)
atl::n::ocl::OCL::OclFeatureDefinition_strategy = st.builds(
    atl::n::ocl::OCL::OclFeatureDefinition,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
atl::n::ocl::OCL::IteratorExp_strategy = st.builds(
    atl::n::ocl::OCL::IteratorExp,
    name=
        safe_text
)
atl::n::ocl::OCL::IterateExp_strategy = st.builds(
    atl::n::ocl::OCL::IterateExp,
)
atl::n::ocl::OCL::StringType_strategy = st.builds(
    atl::n::ocl::OCL::StringType,
)
atl::n::ocl::OCL::VariableDeclaration_strategy = st.builds(
    atl::n::ocl::OCL::VariableDeclaration,
    varName=
        safe_text,
    id=
        safe_text
)
atl::n::ocl::OCL::MapElement_strategy = st.builds(
    atl::n::ocl::OCL::MapElement,
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
CollectionExp_strategy = st.builds(
    CollectionExp,
)
atl::n::ocl::OCL::SequenceExp_strategy = st.builds(
    atl::n::ocl::OCL::SequenceExp,
)
atl::n::ocl::OCL::SetExp_strategy = st.builds(
    atl::n::ocl::OCL::SetExp,
)
atl::n::ocl::OCL::OrderedSetExp_strategy = st.builds(
    atl::n::ocl::OCL::OrderedSetExp,
)
atl::n::ocl::OCL::BagExp_strategy = st.builds(
    atl::n::ocl::OCL::BagExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
atl::n::ocl::OCL::CollectionOperationCallExp_strategy = st.builds(
    atl::n::ocl::OCL::CollectionOperationCallExp,
)
atl::n::ocl::OCL::OperatorCallExp_strategy = st.builds(
    atl::n::ocl::OCL::OperatorCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
atl::n::ocl::OCL::OperationCallExp_strategy = st.builds(
    atl::n::ocl::OCL::OperationCallExp,
    operationName=
        safe_text
)
atl::n::ocl::OCL::LoopExp_strategy = st.builds(
    atl::n::ocl::OCL::LoopExp,
)
atl::n::ocl::OCL::NavigationOrAttributeCallExp_strategy = st.builds(
    atl::n::ocl::OCL::NavigationOrAttributeCallExp,
    name=
        safe_text
)
NumericExp_strategy = st.builds(
    NumericExp,
)
atl::n::ocl::OCL::IntegerExp_strategy = st.builds(
    atl::n::ocl::OCL::IntegerExp,
    integerSymbol=
        st.integers()
)
atl::n::ocl::OCL::RealExp_strategy = st.builds(
    atl::n::ocl::OCL::RealExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
atl::n::ocl::OCL::NumericExp_strategy = st.builds(
    atl::n::ocl::OCL::NumericExp,
)
atl::n::ocl::OCL::BooleanExp_strategy = st.builds(
    atl::n::ocl::OCL::BooleanExp,
    booleanSymbol=
        st.booleans()
)
atl::n::ocl::OCL::StringExp_strategy = st.builds(
    atl::n::ocl::OCL::StringExp,
    stringSymbol=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
atl::n::ocl::OCL::MapType_strategy = st.builds(
    atl::n::ocl::OCL::MapType,
)
atl::n::ocl::OCL::OclModelElement_strategy = st.builds(
    atl::n::ocl::OCL::OclModelElement,
)
atl::n::ocl::OCL::CollectionType_strategy = st.builds(
    atl::n::ocl::OCL::CollectionType,
)
atl::n::ocl::OCL::OclAnyType_strategy = st.builds(
    atl::n::ocl::OCL::OclAnyType,
)
atl::n::ocl::OCL::TupleType_strategy = st.builds(
    atl::n::ocl::OCL::TupleType,
)
atl::n::ocl::OCL::Primitive_strategy = st.builds(
    atl::n::ocl::OCL::Primitive,
)
atl::n::ocl::OCL::OclExpression_strategy = st.builds(
    atl::n::ocl::OCL::OclExpression,
)
PatternElement_strategy = st.builds(
    PatternElement,
)
atl::n::ocl::ATL::OutPatternElement_strategy = st.builds(
    atl::n::ocl::ATL::OutPatternElement,
)
atl::n::ocl::ATL::InPatternElement_strategy = st.builds(
    atl::n::ocl::ATL::InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
atl::n::ocl::OCL::TuplePart_strategy = st.builds(
    atl::n::ocl::OCL::TuplePart,
)
atl::n::ocl::OCL::Parameter_strategy = st.builds(
    atl::n::ocl::OCL::Parameter,
)
atl::n::ocl::OCL::Iterator_strategy = st.builds(
    atl::n::ocl::OCL::Iterator,
)
atl::n::ocl::ATL::PatternElement_strategy = st.builds(
    atl::n::ocl::ATL::PatternElement,
)
atl::n::ocl::ATL::DropPattern_strategy = st.builds(
    atl::n::ocl::ATL::DropPattern,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
atl::n::ocl::ATL::OutPattern_strategy = st.builds(
    atl::n::ocl::ATL::OutPattern,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
atl::n::ocl::ATL::SimpleInPatternElement_strategy = st.builds(
    atl::n::ocl::ATL::SimpleInPatternElement,
)
atl::n::ocl::ATL::InPattern_strategy = st.builds(
    atl::n::ocl::ATL::InPattern,
)
atl::n::ocl::ATL::Statement_strategy = st.builds(
    atl::n::ocl::ATL::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
atl::n::ocl::ATL::IfStat_strategy = st.builds(
    atl::n::ocl::ATL::IfStat,
)
atl::n::ocl::ATL::ForStat_strategy = st.builds(
    atl::n::ocl::ATL::ForStat,
)
atl::n::ocl::ATL::BindingStat_strategy = st.builds(
    atl::n::ocl::ATL::BindingStat,
    propertyName=
        safe_text,
    isAssignment=
        st.booleans()
)
atl::n::ocl::ATL::ExpressionStat_strategy = st.builds(
    atl::n::ocl::ATL::ExpressionStat,
)
atl::n::ocl::ATL::ActionBlock_strategy = st.builds(
    atl::n::ocl::ATL::ActionBlock,
)
atl::n::ocl::ATL::RuleVariableDeclaration_strategy = st.builds(
    atl::n::ocl::ATL::RuleVariableDeclaration,
)
atl::n::ocl::ATL::Binding_strategy = st.builds(
    atl::n::ocl::ATL::Binding,
    isAssignment=
        st.booleans(),
    propertyName=
        safe_text
)
Iterator_strategy = st.builds(
    Iterator,
)
atl::n::ocl::ATL::ForEachOutPatternElement_strategy = st.builds(
    atl::n::ocl::ATL::ForEachOutPatternElement,
)
atl::n::ocl::ATL::SimpleOutPatternElement_strategy = st.builds(
    atl::n::ocl::ATL::SimpleOutPatternElement,
)
Binding_strategy = st.builds(
    Binding,
)
atl::n::ocl::ATL::ModuleElement_strategy = st.builds(
    atl::n::ocl::ATL::ModuleElement,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
atl::n::ocl::ATL::Helper_strategy = st.builds(
    atl::n::ocl::ATL::Helper,
)
OclModel_strategy = st.builds(
    OclModel,
)
atl::n::ocl::ATL::Module_strategy = st.builds(
    atl::n::ocl::ATL::Module,
    isRefining=
        st.booleans()
)
Helper_strategy = st.builds(
    Helper,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atl::n::ocl::OCL::OclUndefinedExp_strategy = st.builds(
    atl::n::ocl::OCL::OclUndefinedExp,
)
atl::n::ocl::OCL::TupleExp_strategy = st.builds(
    atl::n::ocl::OCL::TupleExp,
)
atl::n::ocl::OCL::IfExp_strategy = st.builds(
    atl::n::ocl::OCL::IfExp,
)
atl::n::ocl::OCL::PropertyCallExp_strategy = st.builds(
    atl::n::ocl::OCL::PropertyCallExp,
)
atl::n::ocl::OCL::LetExp_strategy = st.builds(
    atl::n::ocl::OCL::LetExp,
)
atl::n::ocl::OCL::VariableExp_strategy = st.builds(
    atl::n::ocl::OCL::VariableExp,
)
atl::n::ocl::OCL::OclType_strategy = st.builds(
    atl::n::ocl::OCL::OclType,
    name=
        safe_text
)
atl::n::ocl::OCL::CollectionExp_strategy = st.builds(
    atl::n::ocl::OCL::CollectionExp,
)
atl::n::ocl::OCL::MapExp_strategy = st.builds(
    atl::n::ocl::OCL::MapExp,
)
atl::n::ocl::OCL::EnumLiteralExp_strategy = st.builds(
    atl::n::ocl::OCL::EnumLiteralExp,
    name=
        safe_text
)
atl::n::ocl::OCL::SuperExp_strategy = st.builds(
    atl::n::ocl::OCL::SuperExp,
)
atl::n::ocl::OCL::PrimitiveExp_strategy = st.builds(
    atl::n::ocl::OCL::PrimitiveExp,
)
atl::n::ocl::ATL::Query_strategy = st.builds(
    atl::n::ocl::ATL::Query,
)
Parameter_strategy = st.builds(
    Parameter,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
atl::n::ocl::ATL::LazyMatchedRule_strategy = st.builds(
    atl::n::ocl::ATL::LazyMatchedRule,
    isUnique=
        st.booleans()
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
atl::n::ocl::ATL::CalledRule_strategy = st.builds(
    atl::n::ocl::ATL::CalledRule,
    isEndpoint=
        st.booleans(),
    isEntrypoint=
        st.booleans()
)
atl::n::ocl::ATL::MatchedRule_strategy = st.builds(
    atl::n::ocl::ATL::MatchedRule,
    isRefining=
        st.booleans(),
    isNoDefault=
        st.booleans(),
    isAbstract=
        st.booleans()
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
atl::n::ocl::ATL::Rule_strategy = st.builds(
    atl::n::ocl::ATL::Rule,
    name=
        safe_text
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=atl::n::ocl::OCL::OclModel_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclModel)

@given(instance=atl::n::ocl::OCL::OclModel_strategy)
def test_atl::n::ocl::ocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::OclModel_strategy)
def test_atl::n::ocl::ocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::TupleTypeAttribute)

@given(instance=atl::n::ocl::OCL::TupleTypeAttribute_strategy)
def test_atl::n::ocl::ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::TupleTypeAttribute_strategy)
def test_atl::n::ocl::ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=atl::n::ocl::OCL::SetType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::settype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::SetType)

@given(instance=atl::n::ocl::OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::SequenceType)

@given(instance=atl::n::ocl::OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OrderedSetType)

@given(instance=atl::n::ocl::OCL::BagType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::bagtype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=atl::n::ocl::OCL::RealType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::realtype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::RealType)

@given(instance=atl::n::ocl::OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::integertype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=atl::n::ocl::OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::booleantype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::BooleanType)

@given(instance=atl::n::ocl::OCL::NumericType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::numerictype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::NumericType)

@given(instance=atl::n::ocl::OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclFeature)

@given(instance=atl::n::ocl::OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclContextDefinition)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=atl::n::ocl::OCL::Operation_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::operation_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::Operation)

@given(instance=atl::n::ocl::OCL::Operation_strategy)
def test_atl::n::ocl::ocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::Operation_strategy)
def test_atl::n::ocl::ocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::Attribute_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::attribute_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::Attribute)

@given(instance=atl::n::ocl::OCL::Attribute_strategy)
def test_atl::n::ocl::ocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::Attribute_strategy)
def test_atl::n::ocl::ocl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclFeatureDefinition)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=atl::n::ocl::OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::IteratorExp)

@given(instance=atl::n::ocl::OCL::IteratorExp_strategy)
def test_atl::n::ocl::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::IteratorExp_strategy)
def test_atl::n::ocl::ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::IterateExp)

@given(instance=atl::n::ocl::OCL::StringType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::stringtype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::StringType)

@given(instance=atl::n::ocl::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::VariableDeclaration)

@given(instance=atl::n::ocl::OCL::VariableDeclaration_strategy)
def test_atl::n::ocl::ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=atl::n::ocl::OCL::VariableDeclaration_strategy)
def test_atl::n::ocl::ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=atl::n::ocl::OCL::VariableDeclaration_strategy)
def test_atl::n::ocl::ocl::variabledeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=atl::n::ocl::OCL::VariableDeclaration_strategy)
def test_atl::n::ocl::ocl::variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=atl::n::ocl::OCL::MapElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::mapelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::MapElement)

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

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=atl::n::ocl::OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::SequenceExp)

@given(instance=atl::n::ocl::OCL::SetExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::setexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::SetExp)

@given(instance=atl::n::ocl::OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OrderedSetExp)

@given(instance=atl::n::ocl::OCL::BagExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::bagexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::BagExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=atl::n::ocl::OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::CollectionOperationCallExp)

@given(instance=atl::n::ocl::OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OperatorCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=atl::n::ocl::OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OperationCallExp)

@given(instance=atl::n::ocl::OCL::OperationCallExp_strategy)
def test_atl::n::ocl::ocl::operationcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=atl::n::ocl::OCL::OperationCallExp_strategy)
def test_atl::n::ocl::ocl::operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=atl::n::ocl::OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::LoopExp)

@given(instance=atl::n::ocl::OCL::NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::NavigationOrAttributeCallExp)

@given(instance=atl::n::ocl::OCL::NavigationOrAttributeCallExp_strategy)
def test_atl::n::ocl::ocl::navigationorattributecallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::NavigationOrAttributeCallExp_strategy)
def test_atl::n::ocl::ocl::navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=atl::n::ocl::OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::integerexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::IntegerExp)

@given(instance=atl::n::ocl::OCL::IntegerExp_strategy)
def test_atl::n::ocl::ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, int)


@given(instance=atl::n::ocl::OCL::IntegerExp_strategy)
def test_atl::n::ocl::ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=atl::n::ocl::OCL::RealExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::realexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::RealExp)

@given(instance=atl::n::ocl::OCL::RealExp_strategy)
def test_atl::n::ocl::ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, float)


@given(instance=atl::n::ocl::OCL::RealExp_strategy)
def test_atl::n::ocl::ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=atl::n::ocl::OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::numericexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::NumericExp)

@given(instance=atl::n::ocl::OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::BooleanExp)

@given(instance=atl::n::ocl::OCL::BooleanExp_strategy)
def test_atl::n::ocl::ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, bool)


@given(instance=atl::n::ocl::OCL::BooleanExp_strategy)
def test_atl::n::ocl::ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=atl::n::ocl::OCL::StringExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::stringexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::StringExp)

@given(instance=atl::n::ocl::OCL::StringExp_strategy)
def test_atl::n::ocl::ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=atl::n::ocl::OCL::StringExp_strategy)
def test_atl::n::ocl::ocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=atl::n::ocl::OCL::MapType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::maptype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::MapType)

@given(instance=atl::n::ocl::OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclModelElement)

@given(instance=atl::n::ocl::OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::CollectionType)

@given(instance=atl::n::ocl::OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclAnyType)

@given(instance=atl::n::ocl::OCL::TupleType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::tupletype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::TupleType)

@given(instance=atl::n::ocl::OCL::Primitive_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::primitive_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::Primitive)

@given(instance=atl::n::ocl::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclExpression)

@given(instance=PatternElement_strategy)
@settings(max_examples=50)
def test_patternelement_instantiation(instance):
    assert isinstance(instance, PatternElement)

@given(instance=atl::n::ocl::ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::OutPatternElement)

@given(instance=atl::n::ocl::ATL::InPatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::inpatternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=atl::n::ocl::OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::TuplePart)

@given(instance=atl::n::ocl::OCL::Parameter_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::parameter_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::Parameter)

@given(instance=atl::n::ocl::OCL::Iterator_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::iterator_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::Iterator)

@given(instance=atl::n::ocl::ATL::PatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::patternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::PatternElement)

@given(instance=atl::n::ocl::ATL::DropPattern_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::droppattern_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::DropPattern)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=atl::n::ocl::ATL::OutPattern_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::outpattern_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::OutPattern)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=atl::n::ocl::ATL::SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::SimpleInPatternElement)

@given(instance=atl::n::ocl::ATL::InPattern_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::inpattern_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::InPattern)

@given(instance=atl::n::ocl::ATL::Statement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::statement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=atl::n::ocl::ATL::IfStat_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::ifstat_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::IfStat)

@given(instance=atl::n::ocl::ATL::ForStat_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::forstat_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::ForStat)

@given(instance=atl::n::ocl::ATL::BindingStat_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::bindingstat_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::BindingStat)

@given(instance=atl::n::ocl::ATL::BindingStat_strategy)
def test_atl::n::ocl::atl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atl::n::ocl::ATL::BindingStat_strategy)
def test_atl::n::ocl::atl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atl::n::ocl::ATL::BindingStat_strategy)
def test_atl::n::ocl::atl::bindingstat_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, bool)


@given(instance=atl::n::ocl::ATL::BindingStat_strategy)
def test_atl::n::ocl::atl::bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atl::n::ocl::ATL::ExpressionStat_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::expressionstat_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::ExpressionStat)

@given(instance=atl::n::ocl::ATL::ActionBlock_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::actionblock_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::ActionBlock)

@given(instance=atl::n::ocl::ATL::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::RuleVariableDeclaration)

@given(instance=atl::n::ocl::ATL::Binding_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::binding_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Binding)

@given(instance=atl::n::ocl::ATL::Binding_strategy)
def test_atl::n::ocl::atl::binding_isAssignment_type(instance):
    assert isinstance(instance.isAssignment, bool)


@given(instance=atl::n::ocl::ATL::Binding_strategy)
def test_atl::n::ocl::atl::binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atl::n::ocl::ATL::Binding_strategy)
def test_atl::n::ocl::atl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=atl::n::ocl::ATL::Binding_strategy)
def test_atl::n::ocl::atl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=atl::n::ocl::ATL::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::ForEachOutPatternElement)

@given(instance=atl::n::ocl::ATL::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::SimpleOutPatternElement)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=atl::n::ocl::ATL::ModuleElement_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::moduleelement_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::ModuleElement)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=atl::n::ocl::ATL::Helper_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::helper_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Helper)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=atl::n::ocl::ATL::Module_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::module_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Module)

@given(instance=atl::n::ocl::ATL::Module_strategy)
def test_atl::n::ocl::atl::module_isRefining_type(instance):
    assert isinstance(instance.isRefining, bool)


@given(instance=atl::n::ocl::ATL::Module_strategy)
def test_atl::n::ocl::atl::module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atl::n::ocl::OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclUndefinedExp)

@given(instance=atl::n::ocl::OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::TupleExp)

@given(instance=atl::n::ocl::OCL::IfExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::IfExp)

@given(instance=atl::n::ocl::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::PropertyCallExp)

@given(instance=atl::n::ocl::OCL::LetExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::letexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::LetExp)

@given(instance=atl::n::ocl::OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::variableexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::VariableExp)

@given(instance=atl::n::ocl::OCL::OclType_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::ocltype_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::OclType)

@given(instance=atl::n::ocl::OCL::OclType_strategy)
def test_atl::n::ocl::ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::OclType_strategy)
def test_atl::n::ocl::ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::CollectionExp)

@given(instance=atl::n::ocl::OCL::MapExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::mapexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::MapExp)

@given(instance=atl::n::ocl::OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::EnumLiteralExp)

@given(instance=atl::n::ocl::OCL::EnumLiteralExp_strategy)
def test_atl::n::ocl::ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::OCL::EnumLiteralExp_strategy)
def test_atl::n::ocl::ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atl::n::ocl::OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::superexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::SuperExp)

@given(instance=atl::n::ocl::OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::OCL::PrimitiveExp)

@given(instance=atl::n::ocl::ATL::Query_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::query_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Query)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=atl::n::ocl::ATL::LazyMatchedRule_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::lazymatchedrule_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::LazyMatchedRule)

@given(instance=atl::n::ocl::ATL::LazyMatchedRule_strategy)
def test_atl::n::ocl::atl::lazymatchedrule_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=atl::n::ocl::ATL::LazyMatchedRule_strategy)
def test_atl::n::ocl::atl::lazymatchedrule_isUnique_setter(instance):
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

@given(instance=atl::n::ocl::ATL::CalledRule_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::calledrule_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::CalledRule)

@given(instance=atl::n::ocl::ATL::CalledRule_strategy)
def test_atl::n::ocl::atl::calledrule_isEndpoint_type(instance):
    assert isinstance(instance.isEndpoint, bool)


@given(instance=atl::n::ocl::ATL::CalledRule_strategy)
def test_atl::n::ocl::atl::calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original

@given(instance=atl::n::ocl::ATL::CalledRule_strategy)
def test_atl::n::ocl::atl::calledrule_isEntrypoint_type(instance):
    assert isinstance(instance.isEntrypoint, bool)


@given(instance=atl::n::ocl::ATL::CalledRule_strategy)
def test_atl::n::ocl::atl::calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::matchedrule_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::MatchedRule)

@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isRefining_type(instance):
    assert isinstance(instance.isRefining, bool)


@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isNoDefault_type(instance):
    assert isinstance(instance.isNoDefault, bool)


@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original

@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=atl::n::ocl::ATL::MatchedRule_strategy)
def test_atl::n::ocl::atl::matchedrule_isAbstract_setter(instance):
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

@given(instance=atl::n::ocl::ATL::Rule_strategy)
@settings(max_examples=50)
def test_atl::n::ocl::atl::rule_instantiation(instance):
    assert isinstance(instance, atl::n::ocl::ATL::Rule)

@given(instance=atl::n::ocl::ATL::Rule_strategy)
def test_atl::n::ocl::atl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atl::n::ocl::ATL::Rule_strategy)
def test_atl::n::ocl::atl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)
