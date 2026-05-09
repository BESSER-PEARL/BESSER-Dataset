import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclFeature,
    CollectionType,
    EmigOcl::SequenceType,
    EmigOcl::OrderedSetType,
    EmigOcl::SetType,
    EmigOcl::BagType,
    NumericType,
    EmigOcl::RealType,
    EmigOcl::IntegerType,
    Primitive,
    EmigOcl::NumericType,
    EmigOcl::BooleanType,
    EmigOcl::StringType,
    OclType,
    EmigOcl::MapType,
    EmigOcl::Primitive,
    EmigOcl::OclModelElement,
    EmigOcl::TupleType,
    EmigOcl::LambdaType,
    EmigOcl::OclAnyType,
    EmigOcl::CollectionType,
    VariableDeclaration,
    EmigOcl::Parameter,
    LoopExp,
    EmigOcl::IteratorExp,
    EmigOcl::Iterator,
    EmigOcl::IterateExp,
    OperationCall,
    EmigOcl::CollectionOperationCall,
    VariableExp,
    EmigOcl::LambdaCallExp,
    OperatorCallExp,
    EmigOcl::RelOpCallExp,
    EmigOcl::MulOpCallExp,
    EmigOcl::AddOpCallExp,
    EmigOcl::EqOpCallExp,
    EmigOcl::IntOpCallExp,
    EmigOcl::NotOpCallExp,
    PropertyCallExp,
    EmigOcl::OperatorCallExp,
    PropertyCall,
    EmigOcl::NavigationOrAttributeCall,
    EmigOcl::PropertyCall,
    StaticPropertyCall,
    EmigOcl::StaticOperationCall,
    EmigOcl::StaticNavigationOrAttributeCall,
    EmigOcl::StaticPropertyCall,
    LocalVariable,
    EmigOcl::TuplePart,
    NumericExp,
    EmigOcl::IntegerExp,
    EmigOcl::RealExp,
    PrimitiveExp,
    EmigOcl::BooleanExp,
    EmigOcl::NumericExp,
    EmigOcl::StringExp,
    OclExpression,
    EmigOcl::BraceExp,
    EmigOcl::SuperExp,
    EmigOcl::MapExp,
    EmigOcl::OclUndefinedExp,
    EmigOcl::OclModelElementExp,
    EmigOcl::EnumLiteralExp,
    EmigOcl::TupleExp,
    EmigOcl::PrimitiveExp,
    EmigOcl::SelfExp,
    EmigOcl::StaticPropertyCallExp,
    EmigOcl::VariableExp,
    EmigOcl::Attribute,
    EmigOcl::Operation,
    EmigOcl::LocalVariable,
    EmigOcl::OperationCall,
    EmigOcl::LoopExp,
    CollectionExp,
    EmigOcl::BagExp,
    EmigOcl::SequenceExp,
    EmigOcl::OrderedSetExp,
    EmigOcl::SetExp,
    EmigOcl::CollectionExp,
    EmigOcl::PropertyCallExp,
    EmigOcl::IfExp,
    LocatedElement,
    EmigOcl::OclFeature,
    EmigOcl::OclType,
    EmigOcl::VariableDeclaration,
    EmigOcl::OclModel,
    EmigOcl::OclContextDefinition,
    EmigOcl::TupleTypeAttribute,
    EmigOcl::OclExpression,
    EmigOcl::MapElement,
    EmigOcl::OclFeatureDefinition,
    EmigOcl::Module,
    EmigOcl::LocatedElement,
    EmigOcl::LetExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_emigocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SequenceType)


def test_emigocl::sequencetype_constructor_exists():
    assert callable(EmigOcl::SequenceType.__init__)


def test_emigocl::sequencetype_constructor_args():
    sig = inspect.signature(EmigOcl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OrderedSetType)


def test_emigocl::orderedsettype_constructor_exists():
    assert callable(EmigOcl::OrderedSetType.__init__)


def test_emigocl::orderedsettype_constructor_args():
    sig = inspect.signature(EmigOcl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::settype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SetType)


def test_emigocl::settype_constructor_exists():
    assert callable(EmigOcl::SetType.__init__)


def test_emigocl::settype_constructor_args():
    sig = inspect.signature(EmigOcl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::BagType)


def test_emigocl::bagtype_constructor_exists():
    assert callable(EmigOcl::BagType.__init__)


def test_emigocl::bagtype_constructor_args():
    sig = inspect.signature(EmigOcl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::realtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::RealType)


def test_emigocl::realtype_constructor_exists():
    assert callable(EmigOcl::RealType.__init__)


def test_emigocl::realtype_constructor_args():
    sig = inspect.signature(EmigOcl::RealType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::integertype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IntegerType)


def test_emigocl::integertype_constructor_exists():
    assert callable(EmigOcl::IntegerType.__init__)


def test_emigocl::integertype_constructor_args():
    sig = inspect.signature(EmigOcl::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::NumericType)


def test_emigocl::numerictype_constructor_exists():
    assert callable(EmigOcl::NumericType.__init__)


def test_emigocl::numerictype_constructor_args():
    sig = inspect.signature(EmigOcl::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::BooleanType)


def test_emigocl::booleantype_constructor_exists():
    assert callable(EmigOcl::BooleanType.__init__)


def test_emigocl::booleantype_constructor_args():
    sig = inspect.signature(EmigOcl::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StringType)


def test_emigocl::stringtype_constructor_exists():
    assert callable(EmigOcl::StringType.__init__)


def test_emigocl::stringtype_constructor_args():
    sig = inspect.signature(EmigOcl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::maptype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::MapType)


def test_emigocl::maptype_constructor_exists():
    assert callable(EmigOcl::MapType.__init__)


def test_emigocl::maptype_constructor_args():
    sig = inspect.signature(EmigOcl::MapType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::primitive_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Primitive)


def test_emigocl::primitive_constructor_exists():
    assert callable(EmigOcl::Primitive.__init__)


def test_emigocl::primitive_constructor_args():
    sig = inspect.signature(EmigOcl::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclModelElement)


def test_emigocl::oclmodelelement_constructor_exists():
    assert callable(EmigOcl::OclModelElement.__init__)


def test_emigocl::oclmodelelement_constructor_args():
    sig = inspect.signature(EmigOcl::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::TupleType)


def test_emigocl::tupletype_constructor_exists():
    assert callable(EmigOcl::TupleType.__init__)


def test_emigocl::tupletype_constructor_args():
    sig = inspect.signature(EmigOcl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::lambdatype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LambdaType)


def test_emigocl::lambdatype_constructor_exists():
    assert callable(EmigOcl::LambdaType.__init__)


def test_emigocl::lambdatype_constructor_args():
    sig = inspect.signature(EmigOcl::LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclAnyType)


def test_emigocl::oclanytype_constructor_exists():
    assert callable(EmigOcl::OclAnyType.__init__)


def test_emigocl::oclanytype_constructor_args():
    sig = inspect.signature(EmigOcl::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::CollectionType)


def test_emigocl::collectiontype_constructor_exists():
    assert callable(EmigOcl::CollectionType.__init__)


def test_emigocl::collectiontype_constructor_args():
    sig = inspect.signature(EmigOcl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::parameter_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Parameter)


def test_emigocl::parameter_constructor_exists():
    assert callable(EmigOcl::Parameter.__init__)


def test_emigocl::parameter_constructor_args():
    sig = inspect.signature(EmigOcl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IteratorExp)


def test_emigocl::iteratorexp_constructor_exists():
    assert callable(EmigOcl::IteratorExp.__init__)


def test_emigocl::iteratorexp_constructor_args():
    sig = inspect.signature(EmigOcl::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::iteratorexp_has_name():
    assert hasattr(EmigOcl::IteratorExp, "name")
    descriptor = None
    for klass in EmigOcl::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::iterator_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Iterator)


def test_emigocl::iterator_constructor_exists():
    assert callable(EmigOcl::Iterator.__init__)


def test_emigocl::iterator_constructor_args():
    sig = inspect.signature(EmigOcl::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IterateExp)


def test_emigocl::iterateexp_constructor_exists():
    assert callable(EmigOcl::IterateExp.__init__)


def test_emigocl::iterateexp_constructor_args():
    sig = inspect.signature(EmigOcl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::CollectionOperationCall)


def test_emigocl::collectionoperationcall_constructor_exists():
    assert callable(EmigOcl::CollectionOperationCall.__init__)


def test_emigocl::collectionoperationcall_constructor_args():
    sig = inspect.signature(EmigOcl::CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LambdaCallExp)


def test_emigocl::lambdacallexp_constructor_exists():
    assert callable(EmigOcl::LambdaCallExp.__init__)


def test_emigocl::lambdacallexp_constructor_args():
    sig = inspect.signature(EmigOcl::LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::relopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::RelOpCallExp)


def test_emigocl::relopcallexp_constructor_exists():
    assert callable(EmigOcl::RelOpCallExp.__init__)


def test_emigocl::relopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::MulOpCallExp)


def test_emigocl::mulopcallexp_constructor_exists():
    assert callable(EmigOcl::MulOpCallExp.__init__)


def test_emigocl::mulopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::AddOpCallExp)


def test_emigocl::addopcallexp_constructor_exists():
    assert callable(EmigOcl::AddOpCallExp.__init__)


def test_emigocl::addopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::EqOpCallExp)


def test_emigocl::eqopcallexp_constructor_exists():
    assert callable(EmigOcl::EqOpCallExp.__init__)


def test_emigocl::eqopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::intopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IntOpCallExp)


def test_emigocl::intopcallexp_constructor_exists():
    assert callable(EmigOcl::IntOpCallExp.__init__)


def test_emigocl::intopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::notopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::NotOpCallExp)


def test_emigocl::notopcallexp_constructor_exists():
    assert callable(EmigOcl::NotOpCallExp.__init__)


def test_emigocl::notopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OperatorCallExp)


def test_emigocl::operatorcallexp_constructor_exists():
    assert callable(EmigOcl::OperatorCallExp.__init__)


def test_emigocl::operatorcallexp_constructor_args():
    sig = inspect.signature(EmigOcl::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl::operatorcallexp_has_operationName():
    assert hasattr(EmigOcl::OperatorCallExp, "operationName")
    descriptor = None
    for klass in EmigOcl::OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::NavigationOrAttributeCall)


def test_emigocl::navigationorattributecall_constructor_exists():
    assert callable(EmigOcl::NavigationOrAttributeCall.__init__)


def test_emigocl::navigationorattributecall_constructor_args():
    sig = inspect.signature(EmigOcl::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::navigationorattributecall_has_name():
    assert hasattr(EmigOcl::NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in EmigOcl::NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::propertycall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::PropertyCall)


def test_emigocl::propertycall_constructor_exists():
    assert callable(EmigOcl::PropertyCall.__init__)


def test_emigocl::propertycall_constructor_args():
    sig = inspect.signature(EmigOcl::PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StaticOperationCall)


def test_emigocl::staticoperationcall_constructor_exists():
    assert callable(EmigOcl::StaticOperationCall.__init__)


def test_emigocl::staticoperationcall_constructor_args():
    sig = inspect.signature(EmigOcl::StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl::staticoperationcall_has_operationName():
    assert hasattr(EmigOcl::StaticOperationCall, "operationName")
    descriptor = None
    for klass in EmigOcl::StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StaticNavigationOrAttributeCall)


def test_emigocl::staticnavigationorattributecall_constructor_exists():
    assert callable(EmigOcl::StaticNavigationOrAttributeCall.__init__)


def test_emigocl::staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(EmigOcl::StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::staticnavigationorattributecall_has_name():
    assert hasattr(EmigOcl::StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in EmigOcl::StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StaticPropertyCall)


def test_emigocl::staticpropertycall_constructor_exists():
    assert callable(EmigOcl::StaticPropertyCall.__init__)


def test_emigocl::staticpropertycall_constructor_args():
    sig = inspect.signature(EmigOcl::StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::TuplePart)


def test_emigocl::tuplepart_constructor_exists():
    assert callable(EmigOcl::TuplePart.__init__)


def test_emigocl::tuplepart_constructor_args():
    sig = inspect.signature(EmigOcl::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IntegerExp)


def test_emigocl::integerexp_constructor_exists():
    assert callable(EmigOcl::IntegerExp.__init__)


def test_emigocl::integerexp_constructor_args():
    sig = inspect.signature(EmigOcl::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_emigocl::integerexp_has_integerSymbol():
    assert hasattr(EmigOcl::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in EmigOcl::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::realexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::RealExp)


def test_emigocl::realexp_constructor_exists():
    assert callable(EmigOcl::RealExp.__init__)


def test_emigocl::realexp_constructor_args():
    sig = inspect.signature(EmigOcl::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_emigocl::realexp_has_realSymbol():
    assert hasattr(EmigOcl::RealExp, "realSymbol")
    descriptor = None
    for klass in EmigOcl::RealExp.__mro__:
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



def test_emigocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::BooleanExp)


def test_emigocl::booleanexp_constructor_exists():
    assert callable(EmigOcl::BooleanExp.__init__)


def test_emigocl::booleanexp_constructor_args():
    sig = inspect.signature(EmigOcl::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_emigocl::booleanexp_has_booleanSymbol():
    assert hasattr(EmigOcl::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in EmigOcl::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::NumericExp)


def test_emigocl::numericexp_constructor_exists():
    assert callable(EmigOcl::NumericExp.__init__)


def test_emigocl::numericexp_constructor_args():
    sig = inspect.signature(EmigOcl::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StringExp)


def test_emigocl::stringexp_constructor_exists():
    assert callable(EmigOcl::StringExp.__init__)


def test_emigocl::stringexp_constructor_args():
    sig = inspect.signature(EmigOcl::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_emigocl::stringexp_has_stringSymbol():
    assert hasattr(EmigOcl::StringExp, "stringSymbol")
    descriptor = None
    for klass in EmigOcl::StringExp.__mro__:
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



def test_emigocl::braceexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::BraceExp)


def test_emigocl::braceexp_constructor_exists():
    assert callable(EmigOcl::BraceExp.__init__)


def test_emigocl::braceexp_constructor_args():
    sig = inspect.signature(EmigOcl::BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::superexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SuperExp)


def test_emigocl::superexp_constructor_exists():
    assert callable(EmigOcl::SuperExp.__init__)


def test_emigocl::superexp_constructor_args():
    sig = inspect.signature(EmigOcl::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::MapExp)


def test_emigocl::mapexp_constructor_exists():
    assert callable(EmigOcl::MapExp.__init__)


def test_emigocl::mapexp_constructor_args():
    sig = inspect.signature(EmigOcl::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclUndefinedExp)


def test_emigocl::oclundefinedexp_constructor_exists():
    assert callable(EmigOcl::OclUndefinedExp.__init__)


def test_emigocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(EmigOcl::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclModelElementExp)


def test_emigocl::oclmodelelementexp_constructor_exists():
    assert callable(EmigOcl::OclModelElementExp.__init__)


def test_emigocl::oclmodelelementexp_constructor_args():
    sig = inspect.signature(EmigOcl::OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::oclmodelelementexp_has_name():
    assert hasattr(EmigOcl::OclModelElementExp, "name")
    descriptor = None
    for klass in EmigOcl::OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::EnumLiteralExp)


def test_emigocl::enumliteralexp_constructor_exists():
    assert callable(EmigOcl::EnumLiteralExp.__init__)


def test_emigocl::enumliteralexp_constructor_args():
    sig = inspect.signature(EmigOcl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::enumliteralexp_has_name():
    assert hasattr(EmigOcl::EnumLiteralExp, "name")
    descriptor = None
    for klass in EmigOcl::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::TupleExp)


def test_emigocl::tupleexp_constructor_exists():
    assert callable(EmigOcl::TupleExp.__init__)


def test_emigocl::tupleexp_constructor_args():
    sig = inspect.signature(EmigOcl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::PrimitiveExp)


def test_emigocl::primitiveexp_constructor_exists():
    assert callable(EmigOcl::PrimitiveExp.__init__)


def test_emigocl::primitiveexp_constructor_args():
    sig = inspect.signature(EmigOcl::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::selfexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SelfExp)


def test_emigocl::selfexp_constructor_exists():
    assert callable(EmigOcl::SelfExp.__init__)


def test_emigocl::selfexp_constructor_args():
    sig = inspect.signature(EmigOcl::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::StaticPropertyCallExp)


def test_emigocl::staticpropertycallexp_constructor_exists():
    assert callable(EmigOcl::StaticPropertyCallExp.__init__)


def test_emigocl::staticpropertycallexp_constructor_args():
    sig = inspect.signature(EmigOcl::StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::VariableExp)


def test_emigocl::variableexp_constructor_exists():
    assert callable(EmigOcl::VariableExp.__init__)


def test_emigocl::variableexp_constructor_args():
    sig = inspect.signature(EmigOcl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::attribute_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Attribute)


def test_emigocl::attribute_constructor_exists():
    assert callable(EmigOcl::Attribute.__init__)


def test_emigocl::attribute_constructor_args():
    sig = inspect.signature(EmigOcl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::attribute_has_name():
    assert hasattr(EmigOcl::Attribute, "name")
    descriptor = None
    for klass in EmigOcl::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::operation_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Operation)


def test_emigocl::operation_constructor_exists():
    assert callable(EmigOcl::Operation.__init__)


def test_emigocl::operation_constructor_args():
    sig = inspect.signature(EmigOcl::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::operation_has_name():
    assert hasattr(EmigOcl::Operation, "name")
    descriptor = None
    for klass in EmigOcl::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::localvariable_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LocalVariable)


def test_emigocl::localvariable_constructor_exists():
    assert callable(EmigOcl::LocalVariable.__init__)


def test_emigocl::localvariable_constructor_args():
    sig = inspect.signature(EmigOcl::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_emigocl::localvariable_has_eq():
    assert hasattr(EmigOcl::LocalVariable, "eq")
    descriptor = None
    for klass in EmigOcl::LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::operationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OperationCall)


def test_emigocl::operationcall_constructor_exists():
    assert callable(EmigOcl::OperationCall.__init__)


def test_emigocl::operationcall_constructor_args():
    sig = inspect.signature(EmigOcl::OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl::operationcall_has_operationName():
    assert hasattr(EmigOcl::OperationCall, "operationName")
    descriptor = None
    for klass in EmigOcl::OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LoopExp)


def test_emigocl::loopexp_constructor_exists():
    assert callable(EmigOcl::LoopExp.__init__)


def test_emigocl::loopexp_constructor_args():
    sig = inspect.signature(EmigOcl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::BagExp)


def test_emigocl::bagexp_constructor_exists():
    assert callable(EmigOcl::BagExp.__init__)


def test_emigocl::bagexp_constructor_args():
    sig = inspect.signature(EmigOcl::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SequenceExp)


def test_emigocl::sequenceexp_constructor_exists():
    assert callable(EmigOcl::SequenceExp.__init__)


def test_emigocl::sequenceexp_constructor_args():
    sig = inspect.signature(EmigOcl::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OrderedSetExp)


def test_emigocl::orderedsetexp_constructor_exists():
    assert callable(EmigOcl::OrderedSetExp.__init__)


def test_emigocl::orderedsetexp_constructor_args():
    sig = inspect.signature(EmigOcl::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::setexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::SetExp)


def test_emigocl::setexp_constructor_exists():
    assert callable(EmigOcl::SetExp.__init__)


def test_emigocl::setexp_constructor_args():
    sig = inspect.signature(EmigOcl::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::CollectionExp)


def test_emigocl::collectionexp_constructor_exists():
    assert callable(EmigOcl::CollectionExp.__init__)


def test_emigocl::collectionexp_constructor_args():
    sig = inspect.signature(EmigOcl::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::PropertyCallExp)


def test_emigocl::propertycallexp_constructor_exists():
    assert callable(EmigOcl::PropertyCallExp.__init__)


def test_emigocl::propertycallexp_constructor_args():
    sig = inspect.signature(EmigOcl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::IfExp)


def test_emigocl::ifexp_constructor_exists():
    assert callable(EmigOcl::IfExp.__init__)


def test_emigocl::ifexp_constructor_args():
    sig = inspect.signature(EmigOcl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclFeature)


def test_emigocl::oclfeature_constructor_exists():
    assert callable(EmigOcl::OclFeature.__init__)


def test_emigocl::oclfeature_constructor_args():
    sig = inspect.signature(EmigOcl::OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_emigocl::oclfeature_has_eq():
    assert hasattr(EmigOcl::OclFeature, "eq")
    descriptor = None
    for klass in EmigOcl::OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclType)


def test_emigocl::ocltype_constructor_exists():
    assert callable(EmigOcl::OclType.__init__)


def test_emigocl::ocltype_constructor_args():
    sig = inspect.signature(EmigOcl::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::ocltype_has_name():
    assert hasattr(EmigOcl::OclType, "name")
    descriptor = None
    for klass in EmigOcl::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::VariableDeclaration)


def test_emigocl::variabledeclaration_constructor_exists():
    assert callable(EmigOcl::VariableDeclaration.__init__)


def test_emigocl::variabledeclaration_constructor_args():
    sig = inspect.signature(EmigOcl::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_emigocl::variabledeclaration_has_varName():
    assert hasattr(EmigOcl::VariableDeclaration, "varName")
    descriptor = None
    for klass in EmigOcl::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclModel)


def test_emigocl::oclmodel_constructor_exists():
    assert callable(EmigOcl::OclModel.__init__)


def test_emigocl::oclmodel_constructor_args():
    sig = inspect.signature(EmigOcl::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::oclmodel_has_name():
    assert hasattr(EmigOcl::OclModel, "name")
    descriptor = None
    for klass in EmigOcl::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclContextDefinition)


def test_emigocl::oclcontextdefinition_constructor_exists():
    assert callable(EmigOcl::OclContextDefinition.__init__)


def test_emigocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(EmigOcl::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::TupleTypeAttribute)


def test_emigocl::tupletypeattribute_constructor_exists():
    assert callable(EmigOcl::TupleTypeAttribute.__init__)


def test_emigocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(EmigOcl::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::tupletypeattribute_has_name():
    assert hasattr(EmigOcl::TupleTypeAttribute, "name")
    descriptor = None
    for klass in EmigOcl::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclExpression)


def test_emigocl::oclexpression_constructor_exists():
    assert callable(EmigOcl::OclExpression.__init__)


def test_emigocl::oclexpression_constructor_args():
    sig = inspect.signature(EmigOcl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::MapElement)


def test_emigocl::mapelement_constructor_exists():
    assert callable(EmigOcl::MapElement.__init__)


def test_emigocl::mapelement_constructor_args():
    sig = inspect.signature(EmigOcl::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::OclFeatureDefinition)


def test_emigocl::oclfeaturedefinition_constructor_exists():
    assert callable(EmigOcl::OclFeatureDefinition.__init__)


def test_emigocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(EmigOcl::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_emigocl::oclfeaturedefinition_has_static():
    assert hasattr(EmigOcl::OclFeatureDefinition, "static")
    descriptor = None
    for klass in EmigOcl::OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::module_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::Module)


def test_emigocl::module_constructor_exists():
    assert callable(EmigOcl::Module.__init__)


def test_emigocl::module_constructor_args():
    sig = inspect.signature(EmigOcl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl::module_has_name():
    assert hasattr(EmigOcl::Module, "name")
    descriptor = None
    for klass in EmigOcl::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LocatedElement)


def test_emigocl::locatedelement_constructor_exists():
    assert callable(EmigOcl::LocatedElement.__init__)


def test_emigocl::locatedelement_constructor_args():
    sig = inspect.signature(EmigOcl::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"

def test_emigocl::locatedelement_has_charEnd():
    assert hasattr(EmigOcl::LocatedElement, "charEnd")
    descriptor = None
    for klass in EmigOcl::LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_emigocl::locatedelement_has_charStart():
    assert hasattr(EmigOcl::LocatedElement, "charStart")
    descriptor = None
    for klass in EmigOcl::LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_emigocl::locatedelement_has_line():
    assert hasattr(EmigOcl::LocatedElement, "line")
    descriptor = None
    for klass in EmigOcl::LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_emigocl::locatedelement_has_column():
    assert hasattr(EmigOcl::LocatedElement, "column")
    descriptor = None
    for klass in EmigOcl::LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_emigocl::letexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl::LetExp)


def test_emigocl::letexp_constructor_exists():
    assert callable(EmigOcl::LetExp.__init__)


def test_emigocl::letexp_constructor_args():
    sig = inspect.signature(EmigOcl::LetExp.__init__)
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
OclFeature_strategy = st.builds(
    OclFeature,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EmigOcl::SequenceType_strategy = st.builds(
    EmigOcl::SequenceType,
)
EmigOcl::OrderedSetType_strategy = st.builds(
    EmigOcl::OrderedSetType,
)
EmigOcl::SetType_strategy = st.builds(
    EmigOcl::SetType,
)
EmigOcl::BagType_strategy = st.builds(
    EmigOcl::BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
EmigOcl::RealType_strategy = st.builds(
    EmigOcl::RealType,
)
EmigOcl::IntegerType_strategy = st.builds(
    EmigOcl::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
EmigOcl::NumericType_strategy = st.builds(
    EmigOcl::NumericType,
)
EmigOcl::BooleanType_strategy = st.builds(
    EmigOcl::BooleanType,
)
EmigOcl::StringType_strategy = st.builds(
    EmigOcl::StringType,
)
OclType_strategy = st.builds(
    OclType,
)
EmigOcl::MapType_strategy = st.builds(
    EmigOcl::MapType,
)
EmigOcl::Primitive_strategy = st.builds(
    EmigOcl::Primitive,
)
EmigOcl::OclModelElement_strategy = st.builds(
    EmigOcl::OclModelElement,
)
EmigOcl::TupleType_strategy = st.builds(
    EmigOcl::TupleType,
)
EmigOcl::LambdaType_strategy = st.builds(
    EmigOcl::LambdaType,
)
EmigOcl::OclAnyType_strategy = st.builds(
    EmigOcl::OclAnyType,
)
EmigOcl::CollectionType_strategy = st.builds(
    EmigOcl::CollectionType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
EmigOcl::Parameter_strategy = st.builds(
    EmigOcl::Parameter,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EmigOcl::IteratorExp_strategy = st.builds(
    EmigOcl::IteratorExp,
    name=
        safe_text
)
EmigOcl::Iterator_strategy = st.builds(
    EmigOcl::Iterator,
)
EmigOcl::IterateExp_strategy = st.builds(
    EmigOcl::IterateExp,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
EmigOcl::CollectionOperationCall_strategy = st.builds(
    EmigOcl::CollectionOperationCall,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
EmigOcl::LambdaCallExp_strategy = st.builds(
    EmigOcl::LambdaCallExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
EmigOcl::RelOpCallExp_strategy = st.builds(
    EmigOcl::RelOpCallExp,
)
EmigOcl::MulOpCallExp_strategy = st.builds(
    EmigOcl::MulOpCallExp,
)
EmigOcl::AddOpCallExp_strategy = st.builds(
    EmigOcl::AddOpCallExp,
)
EmigOcl::EqOpCallExp_strategy = st.builds(
    EmigOcl::EqOpCallExp,
)
EmigOcl::IntOpCallExp_strategy = st.builds(
    EmigOcl::IntOpCallExp,
)
EmigOcl::NotOpCallExp_strategy = st.builds(
    EmigOcl::NotOpCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
EmigOcl::OperatorCallExp_strategy = st.builds(
    EmigOcl::OperatorCallExp,
    operationName=
        safe_text
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
EmigOcl::NavigationOrAttributeCall_strategy = st.builds(
    EmigOcl::NavigationOrAttributeCall,
    name=
        safe_text
)
EmigOcl::PropertyCall_strategy = st.builds(
    EmigOcl::PropertyCall,
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
EmigOcl::StaticOperationCall_strategy = st.builds(
    EmigOcl::StaticOperationCall,
    operationName=
        safe_text
)
EmigOcl::StaticNavigationOrAttributeCall_strategy = st.builds(
    EmigOcl::StaticNavigationOrAttributeCall,
    name=
        safe_text
)
EmigOcl::StaticPropertyCall_strategy = st.builds(
    EmigOcl::StaticPropertyCall,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
EmigOcl::TuplePart_strategy = st.builds(
    EmigOcl::TuplePart,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
EmigOcl::IntegerExp_strategy = st.builds(
    EmigOcl::IntegerExp,
    integerSymbol=
        safe_text
)
EmigOcl::RealExp_strategy = st.builds(
    EmigOcl::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
EmigOcl::BooleanExp_strategy = st.builds(
    EmigOcl::BooleanExp,
    booleanSymbol=
        safe_text
)
EmigOcl::NumericExp_strategy = st.builds(
    EmigOcl::NumericExp,
)
EmigOcl::StringExp_strategy = st.builds(
    EmigOcl::StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EmigOcl::BraceExp_strategy = st.builds(
    EmigOcl::BraceExp,
)
EmigOcl::SuperExp_strategy = st.builds(
    EmigOcl::SuperExp,
)
EmigOcl::MapExp_strategy = st.builds(
    EmigOcl::MapExp,
)
EmigOcl::OclUndefinedExp_strategy = st.builds(
    EmigOcl::OclUndefinedExp,
)
EmigOcl::OclModelElementExp_strategy = st.builds(
    EmigOcl::OclModelElementExp,
    name=
        safe_text
)
EmigOcl::EnumLiteralExp_strategy = st.builds(
    EmigOcl::EnumLiteralExp,
    name=
        safe_text
)
EmigOcl::TupleExp_strategy = st.builds(
    EmigOcl::TupleExp,
)
EmigOcl::PrimitiveExp_strategy = st.builds(
    EmigOcl::PrimitiveExp,
)
EmigOcl::SelfExp_strategy = st.builds(
    EmigOcl::SelfExp,
)
EmigOcl::StaticPropertyCallExp_strategy = st.builds(
    EmigOcl::StaticPropertyCallExp,
)
EmigOcl::VariableExp_strategy = st.builds(
    EmigOcl::VariableExp,
)
EmigOcl::Attribute_strategy = st.builds(
    EmigOcl::Attribute,
    name=
        safe_text
)
EmigOcl::Operation_strategy = st.builds(
    EmigOcl::Operation,
    name=
        safe_text
)
EmigOcl::LocalVariable_strategy = st.builds(
    EmigOcl::LocalVariable,
    eq=
        safe_text
)
EmigOcl::OperationCall_strategy = st.builds(
    EmigOcl::OperationCall,
    operationName=
        safe_text
)
EmigOcl::LoopExp_strategy = st.builds(
    EmigOcl::LoopExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
EmigOcl::BagExp_strategy = st.builds(
    EmigOcl::BagExp,
)
EmigOcl::SequenceExp_strategy = st.builds(
    EmigOcl::SequenceExp,
)
EmigOcl::OrderedSetExp_strategy = st.builds(
    EmigOcl::OrderedSetExp,
)
EmigOcl::SetExp_strategy = st.builds(
    EmigOcl::SetExp,
)
EmigOcl::CollectionExp_strategy = st.builds(
    EmigOcl::CollectionExp,
)
EmigOcl::PropertyCallExp_strategy = st.builds(
    EmigOcl::PropertyCallExp,
)
EmigOcl::IfExp_strategy = st.builds(
    EmigOcl::IfExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
EmigOcl::OclFeature_strategy = st.builds(
    EmigOcl::OclFeature,
    eq=
        safe_text
)
EmigOcl::OclType_strategy = st.builds(
    EmigOcl::OclType,
    name=
        safe_text
)
EmigOcl::VariableDeclaration_strategy = st.builds(
    EmigOcl::VariableDeclaration,
    varName=
        safe_text
)
EmigOcl::OclModel_strategy = st.builds(
    EmigOcl::OclModel,
    name=
        safe_text
)
EmigOcl::OclContextDefinition_strategy = st.builds(
    EmigOcl::OclContextDefinition,
)
EmigOcl::TupleTypeAttribute_strategy = st.builds(
    EmigOcl::TupleTypeAttribute,
    name=
        safe_text
)
EmigOcl::OclExpression_strategy = st.builds(
    EmigOcl::OclExpression,
)
EmigOcl::MapElement_strategy = st.builds(
    EmigOcl::MapElement,
)
EmigOcl::OclFeatureDefinition_strategy = st.builds(
    EmigOcl::OclFeatureDefinition,
    static=
        safe_text
)
EmigOcl::Module_strategy = st.builds(
    EmigOcl::Module,
    name=
        safe_text
)
EmigOcl::LocatedElement_strategy = st.builds(
    EmigOcl::LocatedElement,
    charEnd=
        safe_text,
    charStart=
        safe_text,
    line=
        safe_text,
    column=
        safe_text
)
EmigOcl::LetExp_strategy = st.builds(
    EmigOcl::LetExp,
)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EmigOcl::SequenceType_strategy)
@settings(max_examples=50)
def test_emigocl::sequencetype_instantiation(instance):
    assert isinstance(instance, EmigOcl::SequenceType)

@given(instance=EmigOcl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_emigocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, EmigOcl::OrderedSetType)

@given(instance=EmigOcl::SetType_strategy)
@settings(max_examples=50)
def test_emigocl::settype_instantiation(instance):
    assert isinstance(instance, EmigOcl::SetType)

@given(instance=EmigOcl::BagType_strategy)
@settings(max_examples=50)
def test_emigocl::bagtype_instantiation(instance):
    assert isinstance(instance, EmigOcl::BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=EmigOcl::RealType_strategy)
@settings(max_examples=50)
def test_emigocl::realtype_instantiation(instance):
    assert isinstance(instance, EmigOcl::RealType)

@given(instance=EmigOcl::IntegerType_strategy)
@settings(max_examples=50)
def test_emigocl::integertype_instantiation(instance):
    assert isinstance(instance, EmigOcl::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=EmigOcl::NumericType_strategy)
@settings(max_examples=50)
def test_emigocl::numerictype_instantiation(instance):
    assert isinstance(instance, EmigOcl::NumericType)

@given(instance=EmigOcl::BooleanType_strategy)
@settings(max_examples=50)
def test_emigocl::booleantype_instantiation(instance):
    assert isinstance(instance, EmigOcl::BooleanType)

@given(instance=EmigOcl::StringType_strategy)
@settings(max_examples=50)
def test_emigocl::stringtype_instantiation(instance):
    assert isinstance(instance, EmigOcl::StringType)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=EmigOcl::MapType_strategy)
@settings(max_examples=50)
def test_emigocl::maptype_instantiation(instance):
    assert isinstance(instance, EmigOcl::MapType)

@given(instance=EmigOcl::Primitive_strategy)
@settings(max_examples=50)
def test_emigocl::primitive_instantiation(instance):
    assert isinstance(instance, EmigOcl::Primitive)

@given(instance=EmigOcl::OclModelElement_strategy)
@settings(max_examples=50)
def test_emigocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclModelElement)

@given(instance=EmigOcl::TupleType_strategy)
@settings(max_examples=50)
def test_emigocl::tupletype_instantiation(instance):
    assert isinstance(instance, EmigOcl::TupleType)

@given(instance=EmigOcl::LambdaType_strategy)
@settings(max_examples=50)
def test_emigocl::lambdatype_instantiation(instance):
    assert isinstance(instance, EmigOcl::LambdaType)

@given(instance=EmigOcl::OclAnyType_strategy)
@settings(max_examples=50)
def test_emigocl::oclanytype_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclAnyType)

@given(instance=EmigOcl::CollectionType_strategy)
@settings(max_examples=50)
def test_emigocl::collectiontype_instantiation(instance):
    assert isinstance(instance, EmigOcl::CollectionType)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=EmigOcl::Parameter_strategy)
@settings(max_examples=50)
def test_emigocl::parameter_instantiation(instance):
    assert isinstance(instance, EmigOcl::Parameter)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EmigOcl::IteratorExp_strategy)
@settings(max_examples=50)
def test_emigocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::IteratorExp)

@given(instance=EmigOcl::IteratorExp_strategy)
def test_emigocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::IteratorExp_strategy)
def test_emigocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::Iterator_strategy)
@settings(max_examples=50)
def test_emigocl::iterator_instantiation(instance):
    assert isinstance(instance, EmigOcl::Iterator)

@given(instance=EmigOcl::IterateExp_strategy)
@settings(max_examples=50)
def test_emigocl::iterateexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::IterateExp)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=EmigOcl::CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_emigocl::collectionoperationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl::CollectionOperationCall)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=EmigOcl::LambdaCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::lambdacallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::LambdaCallExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=EmigOcl::RelOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::relopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::RelOpCallExp)

@given(instance=EmigOcl::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::mulopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::MulOpCallExp)

@given(instance=EmigOcl::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::addopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::AddOpCallExp)

@given(instance=EmigOcl::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::eqopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::EqOpCallExp)

@given(instance=EmigOcl::IntOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::intopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::IntOpCallExp)

@given(instance=EmigOcl::NotOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::notopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::NotOpCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=EmigOcl::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::OperatorCallExp)

@given(instance=EmigOcl::OperatorCallExp_strategy)
def test_emigocl::operatorcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=EmigOcl::OperatorCallExp_strategy)
def test_emigocl::operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=EmigOcl::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_emigocl::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, EmigOcl::NavigationOrAttributeCall)

@given(instance=EmigOcl::NavigationOrAttributeCall_strategy)
def test_emigocl::navigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::NavigationOrAttributeCall_strategy)
def test_emigocl::navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::PropertyCall_strategy)
@settings(max_examples=50)
def test_emigocl::propertycall_instantiation(instance):
    assert isinstance(instance, EmigOcl::PropertyCall)

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=EmigOcl::StaticOperationCall_strategy)
@settings(max_examples=50)
def test_emigocl::staticoperationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl::StaticOperationCall)

@given(instance=EmigOcl::StaticOperationCall_strategy)
def test_emigocl::staticoperationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=EmigOcl::StaticOperationCall_strategy)
def test_emigocl::staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=EmigOcl::StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_emigocl::staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, EmigOcl::StaticNavigationOrAttributeCall)

@given(instance=EmigOcl::StaticNavigationOrAttributeCall_strategy)
def test_emigocl::staticnavigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::StaticNavigationOrAttributeCall_strategy)
def test_emigocl::staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_emigocl::staticpropertycall_instantiation(instance):
    assert isinstance(instance, EmigOcl::StaticPropertyCall)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=EmigOcl::TuplePart_strategy)
@settings(max_examples=50)
def test_emigocl::tuplepart_instantiation(instance):
    assert isinstance(instance, EmigOcl::TuplePart)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=EmigOcl::IntegerExp_strategy)
@settings(max_examples=50)
def test_emigocl::integerexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::IntegerExp)

@given(instance=EmigOcl::IntegerExp_strategy)
def test_emigocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=EmigOcl::IntegerExp_strategy)
def test_emigocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=EmigOcl::RealExp_strategy)
@settings(max_examples=50)
def test_emigocl::realexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::RealExp)

@given(instance=EmigOcl::RealExp_strategy)
def test_emigocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=EmigOcl::RealExp_strategy)
def test_emigocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=EmigOcl::BooleanExp_strategy)
@settings(max_examples=50)
def test_emigocl::booleanexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::BooleanExp)

@given(instance=EmigOcl::BooleanExp_strategy)
def test_emigocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=EmigOcl::BooleanExp_strategy)
def test_emigocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=EmigOcl::NumericExp_strategy)
@settings(max_examples=50)
def test_emigocl::numericexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::NumericExp)

@given(instance=EmigOcl::StringExp_strategy)
@settings(max_examples=50)
def test_emigocl::stringexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::StringExp)

@given(instance=EmigOcl::StringExp_strategy)
def test_emigocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=EmigOcl::StringExp_strategy)
def test_emigocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EmigOcl::BraceExp_strategy)
@settings(max_examples=50)
def test_emigocl::braceexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::BraceExp)

@given(instance=EmigOcl::SuperExp_strategy)
@settings(max_examples=50)
def test_emigocl::superexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::SuperExp)

@given(instance=EmigOcl::MapExp_strategy)
@settings(max_examples=50)
def test_emigocl::mapexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::MapExp)

@given(instance=EmigOcl::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_emigocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclUndefinedExp)

@given(instance=EmigOcl::OclModelElementExp_strategy)
@settings(max_examples=50)
def test_emigocl::oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclModelElementExp)

@given(instance=EmigOcl::OclModelElementExp_strategy)
def test_emigocl::oclmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::OclModelElementExp_strategy)
def test_emigocl::oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_emigocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::EnumLiteralExp)

@given(instance=EmigOcl::EnumLiteralExp_strategy)
def test_emigocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::EnumLiteralExp_strategy)
def test_emigocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::TupleExp_strategy)
@settings(max_examples=50)
def test_emigocl::tupleexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::TupleExp)

@given(instance=EmigOcl::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_emigocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::PrimitiveExp)

@given(instance=EmigOcl::SelfExp_strategy)
@settings(max_examples=50)
def test_emigocl::selfexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::SelfExp)

@given(instance=EmigOcl::StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::StaticPropertyCallExp)

@given(instance=EmigOcl::VariableExp_strategy)
@settings(max_examples=50)
def test_emigocl::variableexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::VariableExp)

@given(instance=EmigOcl::Attribute_strategy)
@settings(max_examples=50)
def test_emigocl::attribute_instantiation(instance):
    assert isinstance(instance, EmigOcl::Attribute)

@given(instance=EmigOcl::Attribute_strategy)
def test_emigocl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::Attribute_strategy)
def test_emigocl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::Operation_strategy)
@settings(max_examples=50)
def test_emigocl::operation_instantiation(instance):
    assert isinstance(instance, EmigOcl::Operation)

@given(instance=EmigOcl::Operation_strategy)
def test_emigocl::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::Operation_strategy)
def test_emigocl::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::LocalVariable_strategy)
@settings(max_examples=50)
def test_emigocl::localvariable_instantiation(instance):
    assert isinstance(instance, EmigOcl::LocalVariable)

@given(instance=EmigOcl::LocalVariable_strategy)
def test_emigocl::localvariable_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=EmigOcl::LocalVariable_strategy)
def test_emigocl::localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=EmigOcl::OperationCall_strategy)
@settings(max_examples=50)
def test_emigocl::operationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl::OperationCall)

@given(instance=EmigOcl::OperationCall_strategy)
def test_emigocl::operationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=EmigOcl::OperationCall_strategy)
def test_emigocl::operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=EmigOcl::LoopExp_strategy)
@settings(max_examples=50)
def test_emigocl::loopexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::LoopExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=EmigOcl::BagExp_strategy)
@settings(max_examples=50)
def test_emigocl::bagexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::BagExp)

@given(instance=EmigOcl::SequenceExp_strategy)
@settings(max_examples=50)
def test_emigocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::SequenceExp)

@given(instance=EmigOcl::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_emigocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::OrderedSetExp)

@given(instance=EmigOcl::SetExp_strategy)
@settings(max_examples=50)
def test_emigocl::setexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::SetExp)

@given(instance=EmigOcl::CollectionExp_strategy)
@settings(max_examples=50)
def test_emigocl::collectionexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::CollectionExp)

@given(instance=EmigOcl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_emigocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::PropertyCallExp)

@given(instance=EmigOcl::IfExp_strategy)
@settings(max_examples=50)
def test_emigocl::ifexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::IfExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=EmigOcl::OclFeature_strategy)
@settings(max_examples=50)
def test_emigocl::oclfeature_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclFeature)

@given(instance=EmigOcl::OclFeature_strategy)
def test_emigocl::oclfeature_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=EmigOcl::OclFeature_strategy)
def test_emigocl::oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=EmigOcl::OclType_strategy)
@settings(max_examples=50)
def test_emigocl::ocltype_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclType)

@given(instance=EmigOcl::OclType_strategy)
def test_emigocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::OclType_strategy)
def test_emigocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_emigocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, EmigOcl::VariableDeclaration)

@given(instance=EmigOcl::VariableDeclaration_strategy)
def test_emigocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=EmigOcl::VariableDeclaration_strategy)
def test_emigocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=EmigOcl::OclModel_strategy)
@settings(max_examples=50)
def test_emigocl::oclmodel_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclModel)

@given(instance=EmigOcl::OclModel_strategy)
def test_emigocl::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::OclModel_strategy)
def test_emigocl::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_emigocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclContextDefinition)

@given(instance=EmigOcl::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_emigocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, EmigOcl::TupleTypeAttribute)

@given(instance=EmigOcl::TupleTypeAttribute_strategy)
def test_emigocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::TupleTypeAttribute_strategy)
def test_emigocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::OclExpression_strategy)
@settings(max_examples=50)
def test_emigocl::oclexpression_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclExpression)

@given(instance=EmigOcl::MapElement_strategy)
@settings(max_examples=50)
def test_emigocl::mapelement_instantiation(instance):
    assert isinstance(instance, EmigOcl::MapElement)

@given(instance=EmigOcl::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_emigocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, EmigOcl::OclFeatureDefinition)

@given(instance=EmigOcl::OclFeatureDefinition_strategy)
def test_emigocl::oclfeaturedefinition_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=EmigOcl::OclFeatureDefinition_strategy)
def test_emigocl::oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=EmigOcl::Module_strategy)
@settings(max_examples=50)
def test_emigocl::module_instantiation(instance):
    assert isinstance(instance, EmigOcl::Module)

@given(instance=EmigOcl::Module_strategy)
def test_emigocl::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EmigOcl::Module_strategy)
def test_emigocl::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl::LocatedElement_strategy)
@settings(max_examples=50)
def test_emigocl::locatedelement_instantiation(instance):
    assert isinstance(instance, EmigOcl::LocatedElement)

@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_charEnd_type(instance):
    assert isinstance(instance.charEnd, str)


@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original

@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_charStart_type(instance):
    assert isinstance(instance.charStart, str)


@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original

@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=EmigOcl::LocatedElement_strategy)
def test_emigocl::locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=EmigOcl::LetExp_strategy)
@settings(max_examples=50)
def test_emigocl::letexp_instantiation(instance):
    assert isinstance(instance, EmigOcl::LetExp)
