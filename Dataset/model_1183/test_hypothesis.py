import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VariableDeclaration,
    simpleocl::Parameter,
    OclType,
    simpleocl::MapType,
    simpleocl::CollectionType,
    LoopExp,
    simpleocl::IteratorExp,
    simpleocl::IterateExp,
    simpleocl::Iterator,
    OperationCall,
    simpleocl::CollectionOperationCall,
    VariableExp,
    simpleocl::LambdaCallExp,
    OperatorCallExp,
    simpleocl::AddOpCallExp,
    simpleocl::IntOpCallExp,
    simpleocl::EqOpCallExp,
    simpleocl::MulOpCallExp,
    simpleocl::RelOpCallExp,
    simpleocl::NotOpCallExp,
    PropertyCall,
    simpleocl::NavigationOrAttributeCall,
    StaticPropertyCall,
    simpleocl::StaticOperationCall,
    simpleocl::StaticNavigationOrAttributeCall,
    LocalVariable,
    simpleocl::TuplePart,
    OclModel,
    simpleocl::OclInstanceModel,
    OclFeature,
    ModuleElement,
    simpleocl::OclFeatureDefinition,
    simpleocl::EnvType,
    simpleocl::LambdaType,
    simpleocl::OclModelElement,
    simpleocl::TupleType,
    simpleocl::OclAnyType,
    CollectionType,
    simpleocl::OrderedSetType,
    simpleocl::SequenceType,
    simpleocl::SetType,
    simpleocl::BagType,
    NumericType,
    simpleocl::RealType,
    simpleocl::IntegerType,
    Primitive,
    simpleocl::BooleanType,
    simpleocl::NumericType,
    simpleocl::StringType,
    simpleocl::Primitive,
    CollectionExp,
    simpleocl::SetExp,
    simpleocl::OrderedSetExp,
    simpleocl::SequenceExp,
    simpleocl::BagExp,
    CollectionPart,
    simpleocl::CollectionItem,
    simpleocl::CollectionRange,
    PrimitiveExp,
    simpleocl::BooleanExp,
    simpleocl::StringExp,
    OclExpression,
    simpleocl::TupleExp,
    simpleocl::StaticPropertyCallExp,
    simpleocl::OclUndefinedExp,
    simpleocl::EnumLiteralExp,
    simpleocl::SuperExp,
    simpleocl::BraceExp,
    simpleocl::PrimitiveExp,
    simpleocl::MapExp,
    simpleocl::SelfExp,
    simpleocl::OclModelElementExp,
    simpleocl::CollectionExp,
    simpleocl::EnvExp,
    simpleocl::VariableExp,
    simpleocl::OperatorCallExp,
    simpleocl::Attribute,
    NumericExp,
    simpleocl::IntegerExp,
    simpleocl::RealExp,
    simpleocl::NumericExp,
    simpleocl::Operation,
    simpleocl::LocalVariable,
    simpleocl::OperationCall,
    simpleocl::LoopExp,
    simpleocl::LetExp,
    simpleocl::PropertyCallExp,
    simpleocl::IfExp,
    simpleocl::OclMetamodel,
    NamedElement,
    simpleocl::OclModel,
    simpleocl::OclFeature,
    simpleocl::Module,
    LocatedElement,
    simpleocl::ModuleElement,
    simpleocl::OclExpression,
    simpleocl::OclType,
    simpleocl::TupleTypeAttribute,
    simpleocl::MapElement,
    simpleocl::CollectionPart,
    simpleocl::PropertyCall,
    simpleocl::StaticPropertyCall,
    simpleocl::VariableDeclaration,
    simpleocl::OclContextDefinition,
    simpleocl::NamedElement,
    simpleocl::LocatedElement,
    simpleocl::Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::parameter_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Parameter)


def test_simpleocl::parameter_constructor_exists():
    assert callable(simpleocl::Parameter.__init__)


def test_simpleocl::parameter_constructor_args():
    sig = inspect.signature(simpleocl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::maptype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::MapType)


def test_simpleocl::maptype_constructor_exists():
    assert callable(simpleocl::MapType.__init__)


def test_simpleocl::maptype_constructor_args():
    sig = inspect.signature(simpleocl::MapType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionType)


def test_simpleocl::collectiontype_constructor_exists():
    assert callable(simpleocl::CollectionType.__init__)


def test_simpleocl::collectiontype_constructor_args():
    sig = inspect.signature(simpleocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IteratorExp)


def test_simpleocl::iteratorexp_constructor_exists():
    assert callable(simpleocl::IteratorExp.__init__)


def test_simpleocl::iteratorexp_constructor_args():
    sig = inspect.signature(simpleocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::iteratorexp_has_name():
    assert hasattr(simpleocl::IteratorExp, "name")
    descriptor = None
    for klass in simpleocl::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IterateExp)


def test_simpleocl::iterateexp_constructor_exists():
    assert callable(simpleocl::IterateExp.__init__)


def test_simpleocl::iterateexp_constructor_args():
    sig = inspect.signature(simpleocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::iterator_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Iterator)


def test_simpleocl::iterator_constructor_exists():
    assert callable(simpleocl::Iterator.__init__)


def test_simpleocl::iterator_constructor_args():
    sig = inspect.signature(simpleocl::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionOperationCall)


def test_simpleocl::collectionoperationcall_constructor_exists():
    assert callable(simpleocl::CollectionOperationCall.__init__)


def test_simpleocl::collectionoperationcall_constructor_args():
    sig = inspect.signature(simpleocl::CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LambdaCallExp)


def test_simpleocl::lambdacallexp_constructor_exists():
    assert callable(simpleocl::LambdaCallExp.__init__)


def test_simpleocl::lambdacallexp_constructor_args():
    sig = inspect.signature(simpleocl::LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::AddOpCallExp)


def test_simpleocl::addopcallexp_constructor_exists():
    assert callable(simpleocl::AddOpCallExp.__init__)


def test_simpleocl::addopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::intopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IntOpCallExp)


def test_simpleocl::intopcallexp_constructor_exists():
    assert callable(simpleocl::IntOpCallExp.__init__)


def test_simpleocl::intopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::EqOpCallExp)


def test_simpleocl::eqopcallexp_constructor_exists():
    assert callable(simpleocl::EqOpCallExp.__init__)


def test_simpleocl::eqopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::MulOpCallExp)


def test_simpleocl::mulopcallexp_constructor_exists():
    assert callable(simpleocl::MulOpCallExp.__init__)


def test_simpleocl::mulopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::relopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::RelOpCallExp)


def test_simpleocl::relopcallexp_constructor_exists():
    assert callable(simpleocl::RelOpCallExp.__init__)


def test_simpleocl::relopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::notopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::NotOpCallExp)


def test_simpleocl::notopcallexp_constructor_exists():
    assert callable(simpleocl::NotOpCallExp.__init__)


def test_simpleocl::notopcallexp_constructor_args():
    sig = inspect.signature(simpleocl::NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::NavigationOrAttributeCall)


def test_simpleocl::navigationorattributecall_constructor_exists():
    assert callable(simpleocl::NavigationOrAttributeCall.__init__)


def test_simpleocl::navigationorattributecall_constructor_args():
    sig = inspect.signature(simpleocl::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::navigationorattributecall_has_name():
    assert hasattr(simpleocl::NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in simpleocl::NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StaticOperationCall)


def test_simpleocl::staticoperationcall_constructor_exists():
    assert callable(simpleocl::StaticOperationCall.__init__)


def test_simpleocl::staticoperationcall_constructor_args():
    sig = inspect.signature(simpleocl::StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl::staticoperationcall_has_operationName():
    assert hasattr(simpleocl::StaticOperationCall, "operationName")
    descriptor = None
    for klass in simpleocl::StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StaticNavigationOrAttributeCall)


def test_simpleocl::staticnavigationorattributecall_constructor_exists():
    assert callable(simpleocl::StaticNavigationOrAttributeCall.__init__)


def test_simpleocl::staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(simpleocl::StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::staticnavigationorattributecall_has_name():
    assert hasattr(simpleocl::StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in simpleocl::StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(simpleocl::TuplePart)


def test_simpleocl::tuplepart_constructor_exists():
    assert callable(simpleocl::TuplePart.__init__)


def test_simpleocl::tuplepart_constructor_args():
    sig = inspect.signature(simpleocl::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclInstanceModel)


def test_simpleocl::oclinstancemodel_constructor_exists():
    assert callable(simpleocl::OclInstanceModel.__init__)


def test_simpleocl::oclinstancemodel_constructor_args():
    sig = inspect.signature(simpleocl::OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclFeatureDefinition)


def test_simpleocl::oclfeaturedefinition_constructor_exists():
    assert callable(simpleocl::OclFeatureDefinition.__init__)


def test_simpleocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(simpleocl::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_simpleocl::oclfeaturedefinition_has_static():
    assert hasattr(simpleocl::OclFeatureDefinition, "static")
    descriptor = None
    for klass in simpleocl::OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::envtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::EnvType)


def test_simpleocl::envtype_constructor_exists():
    assert callable(simpleocl::EnvType.__init__)


def test_simpleocl::envtype_constructor_args():
    sig = inspect.signature(simpleocl::EnvType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::lambdatype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LambdaType)


def test_simpleocl::lambdatype_constructor_exists():
    assert callable(simpleocl::LambdaType.__init__)


def test_simpleocl::lambdatype_constructor_args():
    sig = inspect.signature(simpleocl::LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclModelElement)


def test_simpleocl::oclmodelelement_constructor_exists():
    assert callable(simpleocl::OclModelElement.__init__)


def test_simpleocl::oclmodelelement_constructor_args():
    sig = inspect.signature(simpleocl::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::TupleType)


def test_simpleocl::tupletype_constructor_exists():
    assert callable(simpleocl::TupleType.__init__)


def test_simpleocl::tupletype_constructor_args():
    sig = inspect.signature(simpleocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclAnyType)


def test_simpleocl::oclanytype_constructor_exists():
    assert callable(simpleocl::OclAnyType.__init__)


def test_simpleocl::oclanytype_constructor_args():
    sig = inspect.signature(simpleocl::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OrderedSetType)


def test_simpleocl::orderedsettype_constructor_exists():
    assert callable(simpleocl::OrderedSetType.__init__)


def test_simpleocl::orderedsettype_constructor_args():
    sig = inspect.signature(simpleocl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SequenceType)


def test_simpleocl::sequencetype_constructor_exists():
    assert callable(simpleocl::SequenceType.__init__)


def test_simpleocl::sequencetype_constructor_args():
    sig = inspect.signature(simpleocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::settype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SetType)


def test_simpleocl::settype_constructor_exists():
    assert callable(simpleocl::SetType.__init__)


def test_simpleocl::settype_constructor_args():
    sig = inspect.signature(simpleocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::BagType)


def test_simpleocl::bagtype_constructor_exists():
    assert callable(simpleocl::BagType.__init__)


def test_simpleocl::bagtype_constructor_args():
    sig = inspect.signature(simpleocl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::realtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::RealType)


def test_simpleocl::realtype_constructor_exists():
    assert callable(simpleocl::RealType.__init__)


def test_simpleocl::realtype_constructor_args():
    sig = inspect.signature(simpleocl::RealType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::integertype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IntegerType)


def test_simpleocl::integertype_constructor_exists():
    assert callable(simpleocl::IntegerType.__init__)


def test_simpleocl::integertype_constructor_args():
    sig = inspect.signature(simpleocl::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::BooleanType)


def test_simpleocl::booleantype_constructor_exists():
    assert callable(simpleocl::BooleanType.__init__)


def test_simpleocl::booleantype_constructor_args():
    sig = inspect.signature(simpleocl::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::NumericType)


def test_simpleocl::numerictype_constructor_exists():
    assert callable(simpleocl::NumericType.__init__)


def test_simpleocl::numerictype_constructor_args():
    sig = inspect.signature(simpleocl::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StringType)


def test_simpleocl::stringtype_constructor_exists():
    assert callable(simpleocl::StringType.__init__)


def test_simpleocl::stringtype_constructor_args():
    sig = inspect.signature(simpleocl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::primitive_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Primitive)


def test_simpleocl::primitive_constructor_exists():
    assert callable(simpleocl::Primitive.__init__)


def test_simpleocl::primitive_constructor_args():
    sig = inspect.signature(simpleocl::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::setexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SetExp)


def test_simpleocl::setexp_constructor_exists():
    assert callable(simpleocl::SetExp.__init__)


def test_simpleocl::setexp_constructor_args():
    sig = inspect.signature(simpleocl::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OrderedSetExp)


def test_simpleocl::orderedsetexp_constructor_exists():
    assert callable(simpleocl::OrderedSetExp.__init__)


def test_simpleocl::orderedsetexp_constructor_args():
    sig = inspect.signature(simpleocl::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SequenceExp)


def test_simpleocl::sequenceexp_constructor_exists():
    assert callable(simpleocl::SequenceExp.__init__)


def test_simpleocl::sequenceexp_constructor_args():
    sig = inspect.signature(simpleocl::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::BagExp)


def test_simpleocl::bagexp_constructor_exists():
    assert callable(simpleocl::BagExp.__init__)


def test_simpleocl::bagexp_constructor_args():
    sig = inspect.signature(simpleocl::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionpart_is_not_abstract():
    assert not inspect.isabstract(CollectionPart)


def test_collectionpart_constructor_exists():
    assert callable(CollectionPart.__init__)


def test_collectionpart_constructor_args():
    sig = inspect.signature(CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionItem)


def test_simpleocl::collectionitem_constructor_exists():
    assert callable(simpleocl::CollectionItem.__init__)


def test_simpleocl::collectionitem_constructor_args():
    sig = inspect.signature(simpleocl::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionRange)


def test_simpleocl::collectionrange_constructor_exists():
    assert callable(simpleocl::CollectionRange.__init__)


def test_simpleocl::collectionrange_constructor_args():
    sig = inspect.signature(simpleocl::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::BooleanExp)


def test_simpleocl::booleanexp_constructor_exists():
    assert callable(simpleocl::BooleanExp.__init__)


def test_simpleocl::booleanexp_constructor_args():
    sig = inspect.signature(simpleocl::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_simpleocl::booleanexp_has_booleanSymbol():
    assert hasattr(simpleocl::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in simpleocl::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StringExp)


def test_simpleocl::stringexp_constructor_exists():
    assert callable(simpleocl::StringExp.__init__)


def test_simpleocl::stringexp_constructor_args():
    sig = inspect.signature(simpleocl::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_simpleocl::stringexp_has_stringSymbol():
    assert hasattr(simpleocl::StringExp, "stringSymbol")
    descriptor = None
    for klass in simpleocl::StringExp.__mro__:
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



def test_simpleocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::TupleExp)


def test_simpleocl::tupleexp_constructor_exists():
    assert callable(simpleocl::TupleExp.__init__)


def test_simpleocl::tupleexp_constructor_args():
    sig = inspect.signature(simpleocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StaticPropertyCallExp)


def test_simpleocl::staticpropertycallexp_constructor_exists():
    assert callable(simpleocl::StaticPropertyCallExp.__init__)


def test_simpleocl::staticpropertycallexp_constructor_args():
    sig = inspect.signature(simpleocl::StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclUndefinedExp)


def test_simpleocl::oclundefinedexp_constructor_exists():
    assert callable(simpleocl::OclUndefinedExp.__init__)


def test_simpleocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(simpleocl::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::EnumLiteralExp)


def test_simpleocl::enumliteralexp_constructor_exists():
    assert callable(simpleocl::EnumLiteralExp.__init__)


def test_simpleocl::enumliteralexp_constructor_args():
    sig = inspect.signature(simpleocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::enumliteralexp_has_name():
    assert hasattr(simpleocl::EnumLiteralExp, "name")
    descriptor = None
    for klass in simpleocl::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::superexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SuperExp)


def test_simpleocl::superexp_constructor_exists():
    assert callable(simpleocl::SuperExp.__init__)


def test_simpleocl::superexp_constructor_args():
    sig = inspect.signature(simpleocl::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::braceexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::BraceExp)


def test_simpleocl::braceexp_constructor_exists():
    assert callable(simpleocl::BraceExp.__init__)


def test_simpleocl::braceexp_constructor_args():
    sig = inspect.signature(simpleocl::BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::PrimitiveExp)


def test_simpleocl::primitiveexp_constructor_exists():
    assert callable(simpleocl::PrimitiveExp.__init__)


def test_simpleocl::primitiveexp_constructor_args():
    sig = inspect.signature(simpleocl::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::MapExp)


def test_simpleocl::mapexp_constructor_exists():
    assert callable(simpleocl::MapExp.__init__)


def test_simpleocl::mapexp_constructor_args():
    sig = inspect.signature(simpleocl::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::selfexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::SelfExp)


def test_simpleocl::selfexp_constructor_exists():
    assert callable(simpleocl::SelfExp.__init__)


def test_simpleocl::selfexp_constructor_args():
    sig = inspect.signature(simpleocl::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclModelElementExp)


def test_simpleocl::oclmodelelementexp_constructor_exists():
    assert callable(simpleocl::OclModelElementExp.__init__)


def test_simpleocl::oclmodelelementexp_constructor_args():
    sig = inspect.signature(simpleocl::OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::oclmodelelementexp_has_name():
    assert hasattr(simpleocl::OclModelElementExp, "name")
    descriptor = None
    for klass in simpleocl::OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionExp)


def test_simpleocl::collectionexp_constructor_exists():
    assert callable(simpleocl::CollectionExp.__init__)


def test_simpleocl::collectionexp_constructor_args():
    sig = inspect.signature(simpleocl::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::envexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::EnvExp)


def test_simpleocl::envexp_constructor_exists():
    assert callable(simpleocl::EnvExp.__init__)


def test_simpleocl::envexp_constructor_args():
    sig = inspect.signature(simpleocl::EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::VariableExp)


def test_simpleocl::variableexp_constructor_exists():
    assert callable(simpleocl::VariableExp.__init__)


def test_simpleocl::variableexp_constructor_args():
    sig = inspect.signature(simpleocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OperatorCallExp)


def test_simpleocl::operatorcallexp_constructor_exists():
    assert callable(simpleocl::OperatorCallExp.__init__)


def test_simpleocl::operatorcallexp_constructor_args():
    sig = inspect.signature(simpleocl::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl::operatorcallexp_has_operationName():
    assert hasattr(simpleocl::OperatorCallExp, "operationName")
    descriptor = None
    for klass in simpleocl::OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Attribute)


def test_simpleocl::attribute_constructor_exists():
    assert callable(simpleocl::Attribute.__init__)


def test_simpleocl::attribute_constructor_args():
    sig = inspect.signature(simpleocl::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IntegerExp)


def test_simpleocl::integerexp_constructor_exists():
    assert callable(simpleocl::IntegerExp.__init__)


def test_simpleocl::integerexp_constructor_args():
    sig = inspect.signature(simpleocl::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_simpleocl::integerexp_has_integerSymbol():
    assert hasattr(simpleocl::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in simpleocl::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::realexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::RealExp)


def test_simpleocl::realexp_constructor_exists():
    assert callable(simpleocl::RealExp.__init__)


def test_simpleocl::realexp_constructor_args():
    sig = inspect.signature(simpleocl::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_simpleocl::realexp_has_realSymbol():
    assert hasattr(simpleocl::RealExp, "realSymbol")
    descriptor = None
    for klass in simpleocl::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::NumericExp)


def test_simpleocl::numericexp_constructor_exists():
    assert callable(simpleocl::NumericExp.__init__)


def test_simpleocl::numericexp_constructor_args():
    sig = inspect.signature(simpleocl::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::operation_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Operation)


def test_simpleocl::operation_constructor_exists():
    assert callable(simpleocl::Operation.__init__)


def test_simpleocl::operation_constructor_args():
    sig = inspect.signature(simpleocl::Operation.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::localvariable_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LocalVariable)


def test_simpleocl::localvariable_constructor_exists():
    assert callable(simpleocl::LocalVariable.__init__)


def test_simpleocl::localvariable_constructor_args():
    sig = inspect.signature(simpleocl::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_simpleocl::localvariable_has_eq():
    assert hasattr(simpleocl::LocalVariable, "eq")
    descriptor = None
    for klass in simpleocl::LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::operationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OperationCall)


def test_simpleocl::operationcall_constructor_exists():
    assert callable(simpleocl::OperationCall.__init__)


def test_simpleocl::operationcall_constructor_args():
    sig = inspect.signature(simpleocl::OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl::operationcall_has_operationName():
    assert hasattr(simpleocl::OperationCall, "operationName")
    descriptor = None
    for klass in simpleocl::OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LoopExp)


def test_simpleocl::loopexp_constructor_exists():
    assert callable(simpleocl::LoopExp.__init__)


def test_simpleocl::loopexp_constructor_args():
    sig = inspect.signature(simpleocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::letexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LetExp)


def test_simpleocl::letexp_constructor_exists():
    assert callable(simpleocl::LetExp.__init__)


def test_simpleocl::letexp_constructor_args():
    sig = inspect.signature(simpleocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::PropertyCallExp)


def test_simpleocl::propertycallexp_constructor_exists():
    assert callable(simpleocl::PropertyCallExp.__init__)


def test_simpleocl::propertycallexp_constructor_args():
    sig = inspect.signature(simpleocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl::IfExp)


def test_simpleocl::ifexp_constructor_exists():
    assert callable(simpleocl::IfExp.__init__)


def test_simpleocl::ifexp_constructor_args():
    sig = inspect.signature(simpleocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclMetamodel)


def test_simpleocl::oclmetamodel_constructor_exists():
    assert callable(simpleocl::OclMetamodel.__init__)


def test_simpleocl::oclmetamodel_constructor_args():
    sig = inspect.signature(simpleocl::OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_simpleocl::oclmetamodel_has_uri():
    assert hasattr(simpleocl::OclMetamodel, "uri")
    descriptor = None
    for klass in simpleocl::OclMetamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclModel)


def test_simpleocl::oclmodel_constructor_exists():
    assert callable(simpleocl::OclModel.__init__)


def test_simpleocl::oclmodel_constructor_args():
    sig = inspect.signature(simpleocl::OclModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclFeature)


def test_simpleocl::oclfeature_constructor_exists():
    assert callable(simpleocl::OclFeature.__init__)


def test_simpleocl::oclfeature_constructor_args():
    sig = inspect.signature(simpleocl::OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_simpleocl::oclfeature_has_eq():
    assert hasattr(simpleocl::OclFeature, "eq")
    descriptor = None
    for klass in simpleocl::OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::module_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Module)


def test_simpleocl::module_constructor_exists():
    assert callable(simpleocl::Module.__init__)


def test_simpleocl::module_constructor_args():
    sig = inspect.signature(simpleocl::Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl::ModuleElement)


def test_simpleocl::moduleelement_constructor_exists():
    assert callable(simpleocl::ModuleElement.__init__)


def test_simpleocl::moduleelement_constructor_args():
    sig = inspect.signature(simpleocl::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclExpression)


def test_simpleocl::oclexpression_constructor_exists():
    assert callable(simpleocl::OclExpression.__init__)


def test_simpleocl::oclexpression_constructor_args():
    sig = inspect.signature(simpleocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclType)


def test_simpleocl::ocltype_constructor_exists():
    assert callable(simpleocl::OclType.__init__)


def test_simpleocl::ocltype_constructor_args():
    sig = inspect.signature(simpleocl::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::ocltype_has_name():
    assert hasattr(simpleocl::OclType, "name")
    descriptor = None
    for klass in simpleocl::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(simpleocl::TupleTypeAttribute)


def test_simpleocl::tupletypeattribute_constructor_exists():
    assert callable(simpleocl::TupleTypeAttribute.__init__)


def test_simpleocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(simpleocl::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::tupletypeattribute_has_name():
    assert hasattr(simpleocl::TupleTypeAttribute, "name")
    descriptor = None
    for klass in simpleocl::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl::MapElement)


def test_simpleocl::mapelement_constructor_exists():
    assert callable(simpleocl::MapElement.__init__)


def test_simpleocl::mapelement_constructor_args():
    sig = inspect.signature(simpleocl::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::collectionpart_is_not_abstract():
    assert not inspect.isabstract(simpleocl::CollectionPart)


def test_simpleocl::collectionpart_constructor_exists():
    assert callable(simpleocl::CollectionPart.__init__)


def test_simpleocl::collectionpart_constructor_args():
    sig = inspect.signature(simpleocl::CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::propertycall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::PropertyCall)


def test_simpleocl::propertycall_constructor_exists():
    assert callable(simpleocl::PropertyCall.__init__)


def test_simpleocl::propertycall_constructor_args():
    sig = inspect.signature(simpleocl::PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(simpleocl::StaticPropertyCall)


def test_simpleocl::staticpropertycall_constructor_exists():
    assert callable(simpleocl::StaticPropertyCall.__init__)


def test_simpleocl::staticpropertycall_constructor_args():
    sig = inspect.signature(simpleocl::StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simpleocl::VariableDeclaration)


def test_simpleocl::variabledeclaration_constructor_exists():
    assert callable(simpleocl::VariableDeclaration.__init__)


def test_simpleocl::variabledeclaration_constructor_args():
    sig = inspect.signature(simpleocl::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_simpleocl::variabledeclaration_has_varName():
    assert hasattr(simpleocl::VariableDeclaration, "varName")
    descriptor = None
    for klass in simpleocl::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(simpleocl::OclContextDefinition)


def test_simpleocl::oclcontextdefinition_constructor_exists():
    assert callable(simpleocl::OclContextDefinition.__init__)


def test_simpleocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(simpleocl::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl::NamedElement)


def test_simpleocl::namedelement_constructor_exists():
    assert callable(simpleocl::NamedElement.__init__)


def test_simpleocl::namedelement_constructor_args():
    sig = inspect.signature(simpleocl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl::namedelement_has_name():
    assert hasattr(simpleocl::NamedElement, "name")
    descriptor = None
    for klass in simpleocl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl::LocatedElement)


def test_simpleocl::locatedelement_constructor_exists():
    assert callable(simpleocl::LocatedElement.__init__)


def test_simpleocl::locatedelement_constructor_args():
    sig = inspect.signature(simpleocl::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"

def test_simpleocl::locatedelement_has_charEnd():
    assert hasattr(simpleocl::LocatedElement, "charEnd")
    descriptor = None
    for klass in simpleocl::LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl::locatedelement_has_charStart():
    assert hasattr(simpleocl::LocatedElement, "charStart")
    descriptor = None
    for klass in simpleocl::LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl::locatedelement_has_line():
    assert hasattr(simpleocl::LocatedElement, "line")
    descriptor = None
    for klass in simpleocl::LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl::locatedelement_has_column():
    assert hasattr(simpleocl::LocatedElement, "column")
    descriptor = None
    for klass in simpleocl::LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl::import_is_not_abstract():
    assert not inspect.isabstract(simpleocl::Import)


def test_simpleocl::import_constructor_exists():
    assert callable(simpleocl::Import.__init__)


def test_simpleocl::import_constructor_args():
    sig = inspect.signature(simpleocl::Import.__init__)
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
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
simpleocl::Parameter_strategy = st.builds(
    simpleocl::Parameter,
)
OclType_strategy = st.builds(
    OclType,
)
simpleocl::MapType_strategy = st.builds(
    simpleocl::MapType,
)
simpleocl::CollectionType_strategy = st.builds(
    simpleocl::CollectionType,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
simpleocl::IteratorExp_strategy = st.builds(
    simpleocl::IteratorExp,
    name=
        safe_text
)
simpleocl::IterateExp_strategy = st.builds(
    simpleocl::IterateExp,
)
simpleocl::Iterator_strategy = st.builds(
    simpleocl::Iterator,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
simpleocl::CollectionOperationCall_strategy = st.builds(
    simpleocl::CollectionOperationCall,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
simpleocl::LambdaCallExp_strategy = st.builds(
    simpleocl::LambdaCallExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
simpleocl::AddOpCallExp_strategy = st.builds(
    simpleocl::AddOpCallExp,
)
simpleocl::IntOpCallExp_strategy = st.builds(
    simpleocl::IntOpCallExp,
)
simpleocl::EqOpCallExp_strategy = st.builds(
    simpleocl::EqOpCallExp,
)
simpleocl::MulOpCallExp_strategy = st.builds(
    simpleocl::MulOpCallExp,
)
simpleocl::RelOpCallExp_strategy = st.builds(
    simpleocl::RelOpCallExp,
)
simpleocl::NotOpCallExp_strategy = st.builds(
    simpleocl::NotOpCallExp,
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
simpleocl::NavigationOrAttributeCall_strategy = st.builds(
    simpleocl::NavigationOrAttributeCall,
    name=
        safe_text
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
simpleocl::StaticOperationCall_strategy = st.builds(
    simpleocl::StaticOperationCall,
    operationName=
        safe_text
)
simpleocl::StaticNavigationOrAttributeCall_strategy = st.builds(
    simpleocl::StaticNavigationOrAttributeCall,
    name=
        safe_text
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
simpleocl::TuplePart_strategy = st.builds(
    simpleocl::TuplePart,
)
OclModel_strategy = st.builds(
    OclModel,
)
simpleocl::OclInstanceModel_strategy = st.builds(
    simpleocl::OclInstanceModel,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
simpleocl::OclFeatureDefinition_strategy = st.builds(
    simpleocl::OclFeatureDefinition,
    static=
        safe_text
)
simpleocl::EnvType_strategy = st.builds(
    simpleocl::EnvType,
)
simpleocl::LambdaType_strategy = st.builds(
    simpleocl::LambdaType,
)
simpleocl::OclModelElement_strategy = st.builds(
    simpleocl::OclModelElement,
)
simpleocl::TupleType_strategy = st.builds(
    simpleocl::TupleType,
)
simpleocl::OclAnyType_strategy = st.builds(
    simpleocl::OclAnyType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
simpleocl::OrderedSetType_strategy = st.builds(
    simpleocl::OrderedSetType,
)
simpleocl::SequenceType_strategy = st.builds(
    simpleocl::SequenceType,
)
simpleocl::SetType_strategy = st.builds(
    simpleocl::SetType,
)
simpleocl::BagType_strategy = st.builds(
    simpleocl::BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
simpleocl::RealType_strategy = st.builds(
    simpleocl::RealType,
)
simpleocl::IntegerType_strategy = st.builds(
    simpleocl::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
simpleocl::BooleanType_strategy = st.builds(
    simpleocl::BooleanType,
)
simpleocl::NumericType_strategy = st.builds(
    simpleocl::NumericType,
)
simpleocl::StringType_strategy = st.builds(
    simpleocl::StringType,
)
simpleocl::Primitive_strategy = st.builds(
    simpleocl::Primitive,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
simpleocl::SetExp_strategy = st.builds(
    simpleocl::SetExp,
)
simpleocl::OrderedSetExp_strategy = st.builds(
    simpleocl::OrderedSetExp,
)
simpleocl::SequenceExp_strategy = st.builds(
    simpleocl::SequenceExp,
)
simpleocl::BagExp_strategy = st.builds(
    simpleocl::BagExp,
)
CollectionPart_strategy = st.builds(
    CollectionPart,
)
simpleocl::CollectionItem_strategy = st.builds(
    simpleocl::CollectionItem,
)
simpleocl::CollectionRange_strategy = st.builds(
    simpleocl::CollectionRange,
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
simpleocl::BooleanExp_strategy = st.builds(
    simpleocl::BooleanExp,
    booleanSymbol=
        safe_text
)
simpleocl::StringExp_strategy = st.builds(
    simpleocl::StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
simpleocl::TupleExp_strategy = st.builds(
    simpleocl::TupleExp,
)
simpleocl::StaticPropertyCallExp_strategy = st.builds(
    simpleocl::StaticPropertyCallExp,
)
simpleocl::OclUndefinedExp_strategy = st.builds(
    simpleocl::OclUndefinedExp,
)
simpleocl::EnumLiteralExp_strategy = st.builds(
    simpleocl::EnumLiteralExp,
    name=
        safe_text
)
simpleocl::SuperExp_strategy = st.builds(
    simpleocl::SuperExp,
)
simpleocl::BraceExp_strategy = st.builds(
    simpleocl::BraceExp,
)
simpleocl::PrimitiveExp_strategy = st.builds(
    simpleocl::PrimitiveExp,
)
simpleocl::MapExp_strategy = st.builds(
    simpleocl::MapExp,
)
simpleocl::SelfExp_strategy = st.builds(
    simpleocl::SelfExp,
)
simpleocl::OclModelElementExp_strategy = st.builds(
    simpleocl::OclModelElementExp,
    name=
        safe_text
)
simpleocl::CollectionExp_strategy = st.builds(
    simpleocl::CollectionExp,
)
simpleocl::EnvExp_strategy = st.builds(
    simpleocl::EnvExp,
)
simpleocl::VariableExp_strategy = st.builds(
    simpleocl::VariableExp,
)
simpleocl::OperatorCallExp_strategy = st.builds(
    simpleocl::OperatorCallExp,
    operationName=
        safe_text
)
simpleocl::Attribute_strategy = st.builds(
    simpleocl::Attribute,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
simpleocl::IntegerExp_strategy = st.builds(
    simpleocl::IntegerExp,
    integerSymbol=
        safe_text
)
simpleocl::RealExp_strategy = st.builds(
    simpleocl::RealExp,
    realSymbol=
        safe_text
)
simpleocl::NumericExp_strategy = st.builds(
    simpleocl::NumericExp,
)
simpleocl::Operation_strategy = st.builds(
    simpleocl::Operation,
)
simpleocl::LocalVariable_strategy = st.builds(
    simpleocl::LocalVariable,
    eq=
        safe_text
)
simpleocl::OperationCall_strategy = st.builds(
    simpleocl::OperationCall,
    operationName=
        safe_text
)
simpleocl::LoopExp_strategy = st.builds(
    simpleocl::LoopExp,
)
simpleocl::LetExp_strategy = st.builds(
    simpleocl::LetExp,
)
simpleocl::PropertyCallExp_strategy = st.builds(
    simpleocl::PropertyCallExp,
)
simpleocl::IfExp_strategy = st.builds(
    simpleocl::IfExp,
)
simpleocl::OclMetamodel_strategy = st.builds(
    simpleocl::OclMetamodel,
    uri=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleocl::OclModel_strategy = st.builds(
    simpleocl::OclModel,
)
simpleocl::OclFeature_strategy = st.builds(
    simpleocl::OclFeature,
    eq=
        safe_text
)
simpleocl::Module_strategy = st.builds(
    simpleocl::Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
simpleocl::ModuleElement_strategy = st.builds(
    simpleocl::ModuleElement,
)
simpleocl::OclExpression_strategy = st.builds(
    simpleocl::OclExpression,
)
simpleocl::OclType_strategy = st.builds(
    simpleocl::OclType,
    name=
        safe_text
)
simpleocl::TupleTypeAttribute_strategy = st.builds(
    simpleocl::TupleTypeAttribute,
    name=
        safe_text
)
simpleocl::MapElement_strategy = st.builds(
    simpleocl::MapElement,
)
simpleocl::CollectionPart_strategy = st.builds(
    simpleocl::CollectionPart,
)
simpleocl::PropertyCall_strategy = st.builds(
    simpleocl::PropertyCall,
)
simpleocl::StaticPropertyCall_strategy = st.builds(
    simpleocl::StaticPropertyCall,
)
simpleocl::VariableDeclaration_strategy = st.builds(
    simpleocl::VariableDeclaration,
    varName=
        safe_text
)
simpleocl::OclContextDefinition_strategy = st.builds(
    simpleocl::OclContextDefinition,
)
simpleocl::NamedElement_strategy = st.builds(
    simpleocl::NamedElement,
    name=
        safe_text
)
simpleocl::LocatedElement_strategy = st.builds(
    simpleocl::LocatedElement,
    charEnd=
        safe_text,
    charStart=
        safe_text,
    line=
        safe_text,
    column=
        safe_text
)
simpleocl::Import_strategy = st.builds(
    simpleocl::Import,
)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=simpleocl::Parameter_strategy)
@settings(max_examples=50)
def test_simpleocl::parameter_instantiation(instance):
    assert isinstance(instance, simpleocl::Parameter)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=simpleocl::MapType_strategy)
@settings(max_examples=50)
def test_simpleocl::maptype_instantiation(instance):
    assert isinstance(instance, simpleocl::MapType)

@given(instance=simpleocl::CollectionType_strategy)
@settings(max_examples=50)
def test_simpleocl::collectiontype_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionType)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=simpleocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_simpleocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, simpleocl::IteratorExp)

@given(instance=simpleocl::IteratorExp_strategy)
def test_simpleocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::IteratorExp_strategy)
def test_simpleocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::IterateExp_strategy)
@settings(max_examples=50)
def test_simpleocl::iterateexp_instantiation(instance):
    assert isinstance(instance, simpleocl::IterateExp)

@given(instance=simpleocl::Iterator_strategy)
@settings(max_examples=50)
def test_simpleocl::iterator_instantiation(instance):
    assert isinstance(instance, simpleocl::Iterator)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=simpleocl::CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl::collectionoperationcall_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionOperationCall)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=simpleocl::LambdaCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::lambdacallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::LambdaCallExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=simpleocl::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::addopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::AddOpCallExp)

@given(instance=simpleocl::IntOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::intopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::IntOpCallExp)

@given(instance=simpleocl::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::eqopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::EqOpCallExp)

@given(instance=simpleocl::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::mulopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::MulOpCallExp)

@given(instance=simpleocl::RelOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::relopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::RelOpCallExp)

@given(instance=simpleocl::NotOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::notopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::NotOpCallExp)

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=simpleocl::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_simpleocl::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, simpleocl::NavigationOrAttributeCall)

@given(instance=simpleocl::NavigationOrAttributeCall_strategy)
def test_simpleocl::navigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::NavigationOrAttributeCall_strategy)
def test_simpleocl::navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=simpleocl::StaticOperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl::staticoperationcall_instantiation(instance):
    assert isinstance(instance, simpleocl::StaticOperationCall)

@given(instance=simpleocl::StaticOperationCall_strategy)
def test_simpleocl::staticoperationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=simpleocl::StaticOperationCall_strategy)
def test_simpleocl::staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl::StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_simpleocl::staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, simpleocl::StaticNavigationOrAttributeCall)

@given(instance=simpleocl::StaticNavigationOrAttributeCall_strategy)
def test_simpleocl::staticnavigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::StaticNavigationOrAttributeCall_strategy)
def test_simpleocl::staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=simpleocl::TuplePart_strategy)
@settings(max_examples=50)
def test_simpleocl::tuplepart_instantiation(instance):
    assert isinstance(instance, simpleocl::TuplePart)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=simpleocl::OclInstanceModel_strategy)
@settings(max_examples=50)
def test_simpleocl::oclinstancemodel_instantiation(instance):
    assert isinstance(instance, simpleocl::OclInstanceModel)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=simpleocl::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_simpleocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, simpleocl::OclFeatureDefinition)

@given(instance=simpleocl::OclFeatureDefinition_strategy)
def test_simpleocl::oclfeaturedefinition_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=simpleocl::OclFeatureDefinition_strategy)
def test_simpleocl::oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=simpleocl::EnvType_strategy)
@settings(max_examples=50)
def test_simpleocl::envtype_instantiation(instance):
    assert isinstance(instance, simpleocl::EnvType)

@given(instance=simpleocl::LambdaType_strategy)
@settings(max_examples=50)
def test_simpleocl::lambdatype_instantiation(instance):
    assert isinstance(instance, simpleocl::LambdaType)

@given(instance=simpleocl::OclModelElement_strategy)
@settings(max_examples=50)
def test_simpleocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, simpleocl::OclModelElement)

@given(instance=simpleocl::TupleType_strategy)
@settings(max_examples=50)
def test_simpleocl::tupletype_instantiation(instance):
    assert isinstance(instance, simpleocl::TupleType)

@given(instance=simpleocl::OclAnyType_strategy)
@settings(max_examples=50)
def test_simpleocl::oclanytype_instantiation(instance):
    assert isinstance(instance, simpleocl::OclAnyType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=simpleocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_simpleocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, simpleocl::OrderedSetType)

@given(instance=simpleocl::SequenceType_strategy)
@settings(max_examples=50)
def test_simpleocl::sequencetype_instantiation(instance):
    assert isinstance(instance, simpleocl::SequenceType)

@given(instance=simpleocl::SetType_strategy)
@settings(max_examples=50)
def test_simpleocl::settype_instantiation(instance):
    assert isinstance(instance, simpleocl::SetType)

@given(instance=simpleocl::BagType_strategy)
@settings(max_examples=50)
def test_simpleocl::bagtype_instantiation(instance):
    assert isinstance(instance, simpleocl::BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=simpleocl::RealType_strategy)
@settings(max_examples=50)
def test_simpleocl::realtype_instantiation(instance):
    assert isinstance(instance, simpleocl::RealType)

@given(instance=simpleocl::IntegerType_strategy)
@settings(max_examples=50)
def test_simpleocl::integertype_instantiation(instance):
    assert isinstance(instance, simpleocl::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=simpleocl::BooleanType_strategy)
@settings(max_examples=50)
def test_simpleocl::booleantype_instantiation(instance):
    assert isinstance(instance, simpleocl::BooleanType)

@given(instance=simpleocl::NumericType_strategy)
@settings(max_examples=50)
def test_simpleocl::numerictype_instantiation(instance):
    assert isinstance(instance, simpleocl::NumericType)

@given(instance=simpleocl::StringType_strategy)
@settings(max_examples=50)
def test_simpleocl::stringtype_instantiation(instance):
    assert isinstance(instance, simpleocl::StringType)

@given(instance=simpleocl::Primitive_strategy)
@settings(max_examples=50)
def test_simpleocl::primitive_instantiation(instance):
    assert isinstance(instance, simpleocl::Primitive)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=simpleocl::SetExp_strategy)
@settings(max_examples=50)
def test_simpleocl::setexp_instantiation(instance):
    assert isinstance(instance, simpleocl::SetExp)

@given(instance=simpleocl::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_simpleocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, simpleocl::OrderedSetExp)

@given(instance=simpleocl::SequenceExp_strategy)
@settings(max_examples=50)
def test_simpleocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, simpleocl::SequenceExp)

@given(instance=simpleocl::BagExp_strategy)
@settings(max_examples=50)
def test_simpleocl::bagexp_instantiation(instance):
    assert isinstance(instance, simpleocl::BagExp)

@given(instance=CollectionPart_strategy)
@settings(max_examples=50)
def test_collectionpart_instantiation(instance):
    assert isinstance(instance, CollectionPart)

@given(instance=simpleocl::CollectionItem_strategy)
@settings(max_examples=50)
def test_simpleocl::collectionitem_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionItem)

@given(instance=simpleocl::CollectionRange_strategy)
@settings(max_examples=50)
def test_simpleocl::collectionrange_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionRange)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=simpleocl::BooleanExp_strategy)
@settings(max_examples=50)
def test_simpleocl::booleanexp_instantiation(instance):
    assert isinstance(instance, simpleocl::BooleanExp)

@given(instance=simpleocl::BooleanExp_strategy)
def test_simpleocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=simpleocl::BooleanExp_strategy)
def test_simpleocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=simpleocl::StringExp_strategy)
@settings(max_examples=50)
def test_simpleocl::stringexp_instantiation(instance):
    assert isinstance(instance, simpleocl::StringExp)

@given(instance=simpleocl::StringExp_strategy)
def test_simpleocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=simpleocl::StringExp_strategy)
def test_simpleocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=simpleocl::TupleExp_strategy)
@settings(max_examples=50)
def test_simpleocl::tupleexp_instantiation(instance):
    assert isinstance(instance, simpleocl::TupleExp)

@given(instance=simpleocl::StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::StaticPropertyCallExp)

@given(instance=simpleocl::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_simpleocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, simpleocl::OclUndefinedExp)

@given(instance=simpleocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_simpleocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, simpleocl::EnumLiteralExp)

@given(instance=simpleocl::EnumLiteralExp_strategy)
def test_simpleocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::EnumLiteralExp_strategy)
def test_simpleocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::SuperExp_strategy)
@settings(max_examples=50)
def test_simpleocl::superexp_instantiation(instance):
    assert isinstance(instance, simpleocl::SuperExp)

@given(instance=simpleocl::BraceExp_strategy)
@settings(max_examples=50)
def test_simpleocl::braceexp_instantiation(instance):
    assert isinstance(instance, simpleocl::BraceExp)

@given(instance=simpleocl::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_simpleocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, simpleocl::PrimitiveExp)

@given(instance=simpleocl::MapExp_strategy)
@settings(max_examples=50)
def test_simpleocl::mapexp_instantiation(instance):
    assert isinstance(instance, simpleocl::MapExp)

@given(instance=simpleocl::SelfExp_strategy)
@settings(max_examples=50)
def test_simpleocl::selfexp_instantiation(instance):
    assert isinstance(instance, simpleocl::SelfExp)

@given(instance=simpleocl::OclModelElementExp_strategy)
@settings(max_examples=50)
def test_simpleocl::oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, simpleocl::OclModelElementExp)

@given(instance=simpleocl::OclModelElementExp_strategy)
def test_simpleocl::oclmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::OclModelElementExp_strategy)
def test_simpleocl::oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::CollectionExp_strategy)
@settings(max_examples=50)
def test_simpleocl::collectionexp_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionExp)

@given(instance=simpleocl::EnvExp_strategy)
@settings(max_examples=50)
def test_simpleocl::envexp_instantiation(instance):
    assert isinstance(instance, simpleocl::EnvExp)

@given(instance=simpleocl::VariableExp_strategy)
@settings(max_examples=50)
def test_simpleocl::variableexp_instantiation(instance):
    assert isinstance(instance, simpleocl::VariableExp)

@given(instance=simpleocl::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::OperatorCallExp)

@given(instance=simpleocl::OperatorCallExp_strategy)
def test_simpleocl::operatorcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=simpleocl::OperatorCallExp_strategy)
def test_simpleocl::operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl::Attribute_strategy)
@settings(max_examples=50)
def test_simpleocl::attribute_instantiation(instance):
    assert isinstance(instance, simpleocl::Attribute)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=simpleocl::IntegerExp_strategy)
@settings(max_examples=50)
def test_simpleocl::integerexp_instantiation(instance):
    assert isinstance(instance, simpleocl::IntegerExp)

@given(instance=simpleocl::IntegerExp_strategy)
def test_simpleocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=simpleocl::IntegerExp_strategy)
def test_simpleocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=simpleocl::RealExp_strategy)
@settings(max_examples=50)
def test_simpleocl::realexp_instantiation(instance):
    assert isinstance(instance, simpleocl::RealExp)

@given(instance=simpleocl::RealExp_strategy)
def test_simpleocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=simpleocl::RealExp_strategy)
def test_simpleocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=simpleocl::NumericExp_strategy)
@settings(max_examples=50)
def test_simpleocl::numericexp_instantiation(instance):
    assert isinstance(instance, simpleocl::NumericExp)

@given(instance=simpleocl::Operation_strategy)
@settings(max_examples=50)
def test_simpleocl::operation_instantiation(instance):
    assert isinstance(instance, simpleocl::Operation)

@given(instance=simpleocl::LocalVariable_strategy)
@settings(max_examples=50)
def test_simpleocl::localvariable_instantiation(instance):
    assert isinstance(instance, simpleocl::LocalVariable)

@given(instance=simpleocl::LocalVariable_strategy)
def test_simpleocl::localvariable_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=simpleocl::LocalVariable_strategy)
def test_simpleocl::localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=simpleocl::OperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl::operationcall_instantiation(instance):
    assert isinstance(instance, simpleocl::OperationCall)

@given(instance=simpleocl::OperationCall_strategy)
def test_simpleocl::operationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=simpleocl::OperationCall_strategy)
def test_simpleocl::operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl::LoopExp_strategy)
@settings(max_examples=50)
def test_simpleocl::loopexp_instantiation(instance):
    assert isinstance(instance, simpleocl::LoopExp)

@given(instance=simpleocl::LetExp_strategy)
@settings(max_examples=50)
def test_simpleocl::letexp_instantiation(instance):
    assert isinstance(instance, simpleocl::LetExp)

@given(instance=simpleocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, simpleocl::PropertyCallExp)

@given(instance=simpleocl::IfExp_strategy)
@settings(max_examples=50)
def test_simpleocl::ifexp_instantiation(instance):
    assert isinstance(instance, simpleocl::IfExp)

@given(instance=simpleocl::OclMetamodel_strategy)
@settings(max_examples=50)
def test_simpleocl::oclmetamodel_instantiation(instance):
    assert isinstance(instance, simpleocl::OclMetamodel)

@given(instance=simpleocl::OclMetamodel_strategy)
def test_simpleocl::oclmetamodel_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=simpleocl::OclMetamodel_strategy)
def test_simpleocl::oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleocl::OclModel_strategy)
@settings(max_examples=50)
def test_simpleocl::oclmodel_instantiation(instance):
    assert isinstance(instance, simpleocl::OclModel)

@given(instance=simpleocl::OclFeature_strategy)
@settings(max_examples=50)
def test_simpleocl::oclfeature_instantiation(instance):
    assert isinstance(instance, simpleocl::OclFeature)

@given(instance=simpleocl::OclFeature_strategy)
def test_simpleocl::oclfeature_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=simpleocl::OclFeature_strategy)
def test_simpleocl::oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=simpleocl::Module_strategy)
@settings(max_examples=50)
def test_simpleocl::module_instantiation(instance):
    assert isinstance(instance, simpleocl::Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=simpleocl::ModuleElement_strategy)
@settings(max_examples=50)
def test_simpleocl::moduleelement_instantiation(instance):
    assert isinstance(instance, simpleocl::ModuleElement)

@given(instance=simpleocl::OclExpression_strategy)
@settings(max_examples=50)
def test_simpleocl::oclexpression_instantiation(instance):
    assert isinstance(instance, simpleocl::OclExpression)

@given(instance=simpleocl::OclType_strategy)
@settings(max_examples=50)
def test_simpleocl::ocltype_instantiation(instance):
    assert isinstance(instance, simpleocl::OclType)

@given(instance=simpleocl::OclType_strategy)
def test_simpleocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::OclType_strategy)
def test_simpleocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_simpleocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, simpleocl::TupleTypeAttribute)

@given(instance=simpleocl::TupleTypeAttribute_strategy)
def test_simpleocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::TupleTypeAttribute_strategy)
def test_simpleocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::MapElement_strategy)
@settings(max_examples=50)
def test_simpleocl::mapelement_instantiation(instance):
    assert isinstance(instance, simpleocl::MapElement)

@given(instance=simpleocl::CollectionPart_strategy)
@settings(max_examples=50)
def test_simpleocl::collectionpart_instantiation(instance):
    assert isinstance(instance, simpleocl::CollectionPart)

@given(instance=simpleocl::PropertyCall_strategy)
@settings(max_examples=50)
def test_simpleocl::propertycall_instantiation(instance):
    assert isinstance(instance, simpleocl::PropertyCall)

@given(instance=simpleocl::StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_simpleocl::staticpropertycall_instantiation(instance):
    assert isinstance(instance, simpleocl::StaticPropertyCall)

@given(instance=simpleocl::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_simpleocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, simpleocl::VariableDeclaration)

@given(instance=simpleocl::VariableDeclaration_strategy)
def test_simpleocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=simpleocl::VariableDeclaration_strategy)
def test_simpleocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=simpleocl::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_simpleocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, simpleocl::OclContextDefinition)

@given(instance=simpleocl::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleocl::namedelement_instantiation(instance):
    assert isinstance(instance, simpleocl::NamedElement)

@given(instance=simpleocl::NamedElement_strategy)
def test_simpleocl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleocl::NamedElement_strategy)
def test_simpleocl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl::LocatedElement_strategy)
@settings(max_examples=50)
def test_simpleocl::locatedelement_instantiation(instance):
    assert isinstance(instance, simpleocl::LocatedElement)

@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_charEnd_type(instance):
    assert isinstance(instance.charEnd, str)


@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original

@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_charStart_type(instance):
    assert isinstance(instance.charStart, str)


@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original

@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=simpleocl::LocatedElement_strategy)
def test_simpleocl::locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=simpleocl::Import_strategy)
@settings(max_examples=50)
def test_simpleocl::import_instantiation(instance):
    assert isinstance(instance, simpleocl::Import)
