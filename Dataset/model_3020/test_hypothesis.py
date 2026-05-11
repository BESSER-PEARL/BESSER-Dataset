import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    nabla::MaxConstant,
    nabla::Minus,
    nabla::Or,
    nabla::BaseTypeConstant,
    nabla::Parenthesis,
    nabla::Equality,
    nabla::Cardinality,
    nabla::FunctionCall,
    nabla::Modulo,
    nabla::Not,
    nabla::And,
    nabla::MinConstant,
    nabla::VectorConstant,
    nabla::Comparison,
    nabla::UnaryMinus,
    nabla::Mul,
    nabla::BoolConstant,
    nabla::Plus,
    nabla::Div,
    nabla::ContractedIf,
    nabla::RealConstant,
    nabla::IntConstant,
    FunctionOrReduction,
    nabla::FunctionOrReduction,
    Var,
    nabla::ConnectivityVar,
    nabla::ArgOrVar,
    TimeIteratorRef,
    nabla::NextTimeIteratorRef,
    nabla::InitTimeIteratorRef,
    nabla::CurrentTimeIteratorRef,
    nabla::TimeIteratorRef,
    ArgOrVar,
    nabla::Arg,
    nabla::TimeIterator,
    ConnectivityCall,
    nabla::ItemRef,
    nabla::ConnectivityCall,
    nabla::Var,
    nabla::SingletonDefinition,
    IterationBlock,
    nabla::Interval,
    nabla::SpaceIterator,
    Container,
    nabla::SetRef,
    nabla::Container,
    nabla::MultipleConnectivityCall,
    nabla::SingleConnectivityCall,
    nabla::Item,
    nabla::ArgOrVarRef,
    Iterable,
    nabla::ReductionCall,
    nabla::Reduction,
    nabla::Connectivity,
    nabla::BaseType,
    Instruction,
    nabla::Return,
    nabla::ItemDefinition,
    nabla::InstructionBlock,
    nabla::If,
    nabla::Exit,
    nabla::Affectation,
    nabla::Loop,
    nabla::SetDefinition,
    nabla::IterationBlock,
    nabla::Iterable,
    nabla::Instruction,
    Connectivity,
    nabla::SingleConnectivity,
    nabla::MultipleConnectivity,
    nabla::Expression,
    nabla::SimpleVar,
    nabla::Job,
    nabla::TimeIteratorDefinition,
    nabla::VarGroupDeclaration,
    nabla::SimpleVarDefinition,
    nabla::OptDefinition,
    nabla::Function,
    nabla::ItemType,
    nabla::Import,
    nabla::NablaModule,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_nabla::maxconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::MaxConstant)


def test_nabla::maxconstant_constructor_exists():
    assert callable(nabla::MaxConstant.__init__)


def test_nabla::maxconstant_constructor_args():
    sig = inspect.signature(nabla::MaxConstant.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_nabla::maxconstant_has_type():
    assert hasattr(nabla::MaxConstant, "type")
    descriptor = None
    for klass in nabla::MaxConstant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nabla::minus_is_not_abstract():
    assert not inspect.isabstract(nabla::Minus)


def test_nabla::minus_constructor_exists():
    assert callable(nabla::Minus.__init__)


def test_nabla::minus_constructor_args():
    sig = inspect.signature(nabla::Minus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::minus_has_op():
    assert hasattr(nabla::Minus, "op")
    descriptor = None
    for klass in nabla::Minus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::or_is_not_abstract():
    assert not inspect.isabstract(nabla::Or)


def test_nabla::or_constructor_exists():
    assert callable(nabla::Or.__init__)


def test_nabla::or_constructor_args():
    sig = inspect.signature(nabla::Or.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::or_has_op():
    assert hasattr(nabla::Or, "op")
    descriptor = None
    for klass in nabla::Or.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::basetypeconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::BaseTypeConstant)


def test_nabla::basetypeconstant_constructor_exists():
    assert callable(nabla::BaseTypeConstant.__init__)


def test_nabla::basetypeconstant_constructor_args():
    sig = inspect.signature(nabla::BaseTypeConstant.__init__)
    params = list(sig.parameters.keys())



def test_nabla::parenthesis_is_not_abstract():
    assert not inspect.isabstract(nabla::Parenthesis)


def test_nabla::parenthesis_constructor_exists():
    assert callable(nabla::Parenthesis.__init__)


def test_nabla::parenthesis_constructor_args():
    sig = inspect.signature(nabla::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_nabla::equality_is_not_abstract():
    assert not inspect.isabstract(nabla::Equality)


def test_nabla::equality_constructor_exists():
    assert callable(nabla::Equality.__init__)


def test_nabla::equality_constructor_args():
    sig = inspect.signature(nabla::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::equality_has_op():
    assert hasattr(nabla::Equality, "op")
    descriptor = None
    for klass in nabla::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::cardinality_is_not_abstract():
    assert not inspect.isabstract(nabla::Cardinality)


def test_nabla::cardinality_constructor_exists():
    assert callable(nabla::Cardinality.__init__)


def test_nabla::cardinality_constructor_args():
    sig = inspect.signature(nabla::Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_nabla::functioncall_is_not_abstract():
    assert not inspect.isabstract(nabla::FunctionCall)


def test_nabla::functioncall_constructor_exists():
    assert callable(nabla::FunctionCall.__init__)


def test_nabla::functioncall_constructor_args():
    sig = inspect.signature(nabla::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::modulo_is_not_abstract():
    assert not inspect.isabstract(nabla::Modulo)


def test_nabla::modulo_constructor_exists():
    assert callable(nabla::Modulo.__init__)


def test_nabla::modulo_constructor_args():
    sig = inspect.signature(nabla::Modulo.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::modulo_has_op():
    assert hasattr(nabla::Modulo, "op")
    descriptor = None
    for klass in nabla::Modulo.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::not_is_not_abstract():
    assert not inspect.isabstract(nabla::Not)


def test_nabla::not_constructor_exists():
    assert callable(nabla::Not.__init__)


def test_nabla::not_constructor_args():
    sig = inspect.signature(nabla::Not.__init__)
    params = list(sig.parameters.keys())



def test_nabla::and_is_not_abstract():
    assert not inspect.isabstract(nabla::And)


def test_nabla::and_constructor_exists():
    assert callable(nabla::And.__init__)


def test_nabla::and_constructor_args():
    sig = inspect.signature(nabla::And.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::and_has_op():
    assert hasattr(nabla::And, "op")
    descriptor = None
    for klass in nabla::And.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::minconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::MinConstant)


def test_nabla::minconstant_constructor_exists():
    assert callable(nabla::MinConstant.__init__)


def test_nabla::minconstant_constructor_args():
    sig = inspect.signature(nabla::MinConstant.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_nabla::minconstant_has_type():
    assert hasattr(nabla::MinConstant, "type")
    descriptor = None
    for klass in nabla::MinConstant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nabla::vectorconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::VectorConstant)


def test_nabla::vectorconstant_constructor_exists():
    assert callable(nabla::VectorConstant.__init__)


def test_nabla::vectorconstant_constructor_args():
    sig = inspect.signature(nabla::VectorConstant.__init__)
    params = list(sig.parameters.keys())



def test_nabla::comparison_is_not_abstract():
    assert not inspect.isabstract(nabla::Comparison)


def test_nabla::comparison_constructor_exists():
    assert callable(nabla::Comparison.__init__)


def test_nabla::comparison_constructor_args():
    sig = inspect.signature(nabla::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::comparison_has_op():
    assert hasattr(nabla::Comparison, "op")
    descriptor = None
    for klass in nabla::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::unaryminus_is_not_abstract():
    assert not inspect.isabstract(nabla::UnaryMinus)


def test_nabla::unaryminus_constructor_exists():
    assert callable(nabla::UnaryMinus.__init__)


def test_nabla::unaryminus_constructor_args():
    sig = inspect.signature(nabla::UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_nabla::mul_is_not_abstract():
    assert not inspect.isabstract(nabla::Mul)


def test_nabla::mul_constructor_exists():
    assert callable(nabla::Mul.__init__)


def test_nabla::mul_constructor_args():
    sig = inspect.signature(nabla::Mul.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::mul_has_op():
    assert hasattr(nabla::Mul, "op")
    descriptor = None
    for klass in nabla::Mul.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::boolconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::BoolConstant)


def test_nabla::boolconstant_constructor_exists():
    assert callable(nabla::BoolConstant.__init__)


def test_nabla::boolconstant_constructor_args():
    sig = inspect.signature(nabla::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla::boolconstant_has_value():
    assert hasattr(nabla::BoolConstant, "value")
    descriptor = None
    for klass in nabla::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla::plus_is_not_abstract():
    assert not inspect.isabstract(nabla::Plus)


def test_nabla::plus_constructor_exists():
    assert callable(nabla::Plus.__init__)


def test_nabla::plus_constructor_args():
    sig = inspect.signature(nabla::Plus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::plus_has_op():
    assert hasattr(nabla::Plus, "op")
    descriptor = None
    for klass in nabla::Plus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::div_is_not_abstract():
    assert not inspect.isabstract(nabla::Div)


def test_nabla::div_constructor_exists():
    assert callable(nabla::Div.__init__)


def test_nabla::div_constructor_args():
    sig = inspect.signature(nabla::Div.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla::div_has_op():
    assert hasattr(nabla::Div, "op")
    descriptor = None
    for klass in nabla::Div.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla::contractedif_is_not_abstract():
    assert not inspect.isabstract(nabla::ContractedIf)


def test_nabla::contractedif_constructor_exists():
    assert callable(nabla::ContractedIf.__init__)


def test_nabla::contractedif_constructor_args():
    sig = inspect.signature(nabla::ContractedIf.__init__)
    params = list(sig.parameters.keys())



def test_nabla::realconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::RealConstant)


def test_nabla::realconstant_constructor_exists():
    assert callable(nabla::RealConstant.__init__)


def test_nabla::realconstant_constructor_args():
    sig = inspect.signature(nabla::RealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla::realconstant_has_value():
    assert hasattr(nabla::RealConstant, "value")
    descriptor = None
    for klass in nabla::RealConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla::intconstant_is_not_abstract():
    assert not inspect.isabstract(nabla::IntConstant)


def test_nabla::intconstant_constructor_exists():
    assert callable(nabla::IntConstant.__init__)


def test_nabla::intconstant_constructor_args():
    sig = inspect.signature(nabla::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla::intconstant_has_value():
    assert hasattr(nabla::IntConstant, "value")
    descriptor = None
    for klass in nabla::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_functionorreduction_is_not_abstract():
    assert not inspect.isabstract(FunctionOrReduction)


def test_functionorreduction_constructor_exists():
    assert callable(FunctionOrReduction.__init__)


def test_functionorreduction_constructor_args():
    sig = inspect.signature(FunctionOrReduction.__init__)
    params = list(sig.parameters.keys())



def test_nabla::functionorreduction_is_not_abstract():
    assert not inspect.isabstract(nabla::FunctionOrReduction)


def test_nabla::functionorreduction_constructor_exists():
    assert callable(nabla::FunctionOrReduction.__init__)


def test_nabla::functionorreduction_constructor_args():
    sig = inspect.signature(nabla::FunctionOrReduction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::functionorreduction_has_name():
    assert hasattr(nabla::FunctionOrReduction, "name")
    descriptor = None
    for klass in nabla::FunctionOrReduction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_var_constructor_exists():
    assert callable(Var.__init__)


def test_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_nabla::connectivityvar_is_not_abstract():
    assert not inspect.isabstract(nabla::ConnectivityVar)


def test_nabla::connectivityvar_constructor_exists():
    assert callable(nabla::ConnectivityVar.__init__)


def test_nabla::connectivityvar_constructor_args():
    sig = inspect.signature(nabla::ConnectivityVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla::argorvar_is_not_abstract():
    assert not inspect.isabstract(nabla::ArgOrVar)


def test_nabla::argorvar_constructor_exists():
    assert callable(nabla::ArgOrVar.__init__)


def test_nabla::argorvar_constructor_args():
    sig = inspect.signature(nabla::ArgOrVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::argorvar_has_name():
    assert hasattr(nabla::ArgOrVar, "name")
    descriptor = None
    for klass in nabla::ArgOrVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timeiteratorref_is_not_abstract():
    assert not inspect.isabstract(TimeIteratorRef)


def test_timeiteratorref_constructor_exists():
    assert callable(TimeIteratorRef.__init__)


def test_timeiteratorref_constructor_args():
    sig = inspect.signature(TimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla::nexttimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla::NextTimeIteratorRef)


def test_nabla::nexttimeiteratorref_constructor_exists():
    assert callable(nabla::NextTimeIteratorRef.__init__)


def test_nabla::nexttimeiteratorref_constructor_args():
    sig = inspect.signature(nabla::NextTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla::nexttimeiteratorref_has_value():
    assert hasattr(nabla::NextTimeIteratorRef, "value")
    descriptor = None
    for klass in nabla::NextTimeIteratorRef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla::inittimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla::InitTimeIteratorRef)


def test_nabla::inittimeiteratorref_constructor_exists():
    assert callable(nabla::InitTimeIteratorRef.__init__)


def test_nabla::inittimeiteratorref_constructor_args():
    sig = inspect.signature(nabla::InitTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla::inittimeiteratorref_has_value():
    assert hasattr(nabla::InitTimeIteratorRef, "value")
    descriptor = None
    for klass in nabla::InitTimeIteratorRef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla::currenttimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla::CurrentTimeIteratorRef)


def test_nabla::currenttimeiteratorref_constructor_exists():
    assert callable(nabla::CurrentTimeIteratorRef.__init__)


def test_nabla::currenttimeiteratorref_constructor_args():
    sig = inspect.signature(nabla::CurrentTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla::timeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla::TimeIteratorRef)


def test_nabla::timeiteratorref_constructor_exists():
    assert callable(nabla::TimeIteratorRef.__init__)


def test_nabla::timeiteratorref_constructor_args():
    sig = inspect.signature(nabla::TimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_argorvar_is_not_abstract():
    assert not inspect.isabstract(ArgOrVar)


def test_argorvar_constructor_exists():
    assert callable(ArgOrVar.__init__)


def test_argorvar_constructor_args():
    sig = inspect.signature(ArgOrVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla::arg_is_not_abstract():
    assert not inspect.isabstract(nabla::Arg)


def test_nabla::arg_constructor_exists():
    assert callable(nabla::Arg.__init__)


def test_nabla::arg_constructor_args():
    sig = inspect.signature(nabla::Arg.__init__)
    params = list(sig.parameters.keys())



def test_nabla::timeiterator_is_not_abstract():
    assert not inspect.isabstract(nabla::TimeIterator)


def test_nabla::timeiterator_constructor_exists():
    assert callable(nabla::TimeIterator.__init__)


def test_nabla::timeiterator_constructor_args():
    sig = inspect.signature(nabla::TimeIterator.__init__)
    params = list(sig.parameters.keys())



def test_connectivitycall_is_not_abstract():
    assert not inspect.isabstract(ConnectivityCall)


def test_connectivitycall_constructor_exists():
    assert callable(ConnectivityCall.__init__)


def test_connectivitycall_constructor_args():
    sig = inspect.signature(ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::itemref_is_not_abstract():
    assert not inspect.isabstract(nabla::ItemRef)


def test_nabla::itemref_constructor_exists():
    assert callable(nabla::ItemRef.__init__)


def test_nabla::itemref_constructor_args():
    sig = inspect.signature(nabla::ItemRef.__init__)
    params = list(sig.parameters.keys())
    assert "dec" in params, "Missing parameter 'dec'"
    assert "inc" in params, "Missing parameter 'inc'"

def test_nabla::itemref_has_dec():
    assert hasattr(nabla::ItemRef, "dec")
    descriptor = None
    for klass in nabla::ItemRef.__mro__:
        if "dec" in klass.__dict__:
            descriptor = klass.__dict__["dec"]
            break
    assert isinstance(descriptor, property)

def test_nabla::itemref_has_inc():
    assert hasattr(nabla::ItemRef, "inc")
    descriptor = None
    for klass in nabla::ItemRef.__mro__:
        if "inc" in klass.__dict__:
            descriptor = klass.__dict__["inc"]
            break
    assert isinstance(descriptor, property)



def test_nabla::connectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla::ConnectivityCall)


def test_nabla::connectivitycall_constructor_exists():
    assert callable(nabla::ConnectivityCall.__init__)


def test_nabla::connectivitycall_constructor_args():
    sig = inspect.signature(nabla::ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::var_is_not_abstract():
    assert not inspect.isabstract(nabla::Var)


def test_nabla::var_constructor_exists():
    assert callable(nabla::Var.__init__)


def test_nabla::var_constructor_args():
    sig = inspect.signature(nabla::Var.__init__)
    params = list(sig.parameters.keys())



def test_nabla::singletondefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::SingletonDefinition)


def test_nabla::singletondefinition_constructor_exists():
    assert callable(nabla::SingletonDefinition.__init__)


def test_nabla::singletondefinition_constructor_args():
    sig = inspect.signature(nabla::SingletonDefinition.__init__)
    params = list(sig.parameters.keys())



def test_iterationblock_is_not_abstract():
    assert not inspect.isabstract(IterationBlock)


def test_iterationblock_constructor_exists():
    assert callable(IterationBlock.__init__)


def test_iterationblock_constructor_args():
    sig = inspect.signature(IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla::interval_is_not_abstract():
    assert not inspect.isabstract(nabla::Interval)


def test_nabla::interval_constructor_exists():
    assert callable(nabla::Interval.__init__)


def test_nabla::interval_constructor_args():
    sig = inspect.signature(nabla::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"

def test_nabla::interval_has_from_():
    assert hasattr(nabla::Interval, "from_")
    descriptor = None
    for klass in nabla::Interval.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_nabla::spaceiterator_is_not_abstract():
    assert not inspect.isabstract(nabla::SpaceIterator)


def test_nabla::spaceiterator_constructor_exists():
    assert callable(nabla::SpaceIterator.__init__)


def test_nabla::spaceiterator_constructor_args():
    sig = inspect.signature(nabla::SpaceIterator.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_nabla::setref_is_not_abstract():
    assert not inspect.isabstract(nabla::SetRef)


def test_nabla::setref_constructor_exists():
    assert callable(nabla::SetRef.__init__)


def test_nabla::setref_constructor_args():
    sig = inspect.signature(nabla::SetRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla::container_is_not_abstract():
    assert not inspect.isabstract(nabla::Container)


def test_nabla::container_constructor_exists():
    assert callable(nabla::Container.__init__)


def test_nabla::container_constructor_args():
    sig = inspect.signature(nabla::Container.__init__)
    params = list(sig.parameters.keys())



def test_nabla::multipleconnectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla::MultipleConnectivityCall)


def test_nabla::multipleconnectivitycall_constructor_exists():
    assert callable(nabla::MultipleConnectivityCall.__init__)


def test_nabla::multipleconnectivitycall_constructor_args():
    sig = inspect.signature(nabla::MultipleConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::singleconnectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla::SingleConnectivityCall)


def test_nabla::singleconnectivitycall_constructor_exists():
    assert callable(nabla::SingleConnectivityCall.__init__)


def test_nabla::singleconnectivitycall_constructor_args():
    sig = inspect.signature(nabla::SingleConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::item_is_not_abstract():
    assert not inspect.isabstract(nabla::Item)


def test_nabla::item_constructor_exists():
    assert callable(nabla::Item.__init__)


def test_nabla::item_constructor_args():
    sig = inspect.signature(nabla::Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::item_has_name():
    assert hasattr(nabla::Item, "name")
    descriptor = None
    for klass in nabla::Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla::argorvarref_is_not_abstract():
    assert not inspect.isabstract(nabla::ArgOrVarRef)


def test_nabla::argorvarref_constructor_exists():
    assert callable(nabla::ArgOrVarRef.__init__)


def test_nabla::argorvarref_constructor_args():
    sig = inspect.signature(nabla::ArgOrVarRef.__init__)
    params = list(sig.parameters.keys())



def test_iterable_is_not_abstract():
    assert not inspect.isabstract(Iterable)


def test_iterable_constructor_exists():
    assert callable(Iterable.__init__)


def test_iterable_constructor_args():
    sig = inspect.signature(Iterable.__init__)
    params = list(sig.parameters.keys())



def test_nabla::reductioncall_is_not_abstract():
    assert not inspect.isabstract(nabla::ReductionCall)


def test_nabla::reductioncall_constructor_exists():
    assert callable(nabla::ReductionCall.__init__)


def test_nabla::reductioncall_constructor_args():
    sig = inspect.signature(nabla::ReductionCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla::reduction_is_not_abstract():
    assert not inspect.isabstract(nabla::Reduction)


def test_nabla::reduction_constructor_exists():
    assert callable(nabla::Reduction.__init__)


def test_nabla::reduction_constructor_args():
    sig = inspect.signature(nabla::Reduction.__init__)
    params = list(sig.parameters.keys())



def test_nabla::connectivity_is_not_abstract():
    assert not inspect.isabstract(nabla::Connectivity)


def test_nabla::connectivity_constructor_exists():
    assert callable(nabla::Connectivity.__init__)


def test_nabla::connectivity_constructor_args():
    sig = inspect.signature(nabla::Connectivity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::connectivity_has_name():
    assert hasattr(nabla::Connectivity, "name")
    descriptor = None
    for klass in nabla::Connectivity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla::basetype_is_not_abstract():
    assert not inspect.isabstract(nabla::BaseType)


def test_nabla::basetype_constructor_exists():
    assert callable(nabla::BaseType.__init__)


def test_nabla::basetype_constructor_args():
    sig = inspect.signature(nabla::BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_nabla::basetype_has_primitive():
    assert hasattr(nabla::BaseType, "primitive")
    descriptor = None
    for klass in nabla::BaseType.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_nabla::return_is_not_abstract():
    assert not inspect.isabstract(nabla::Return)


def test_nabla::return_constructor_exists():
    assert callable(nabla::Return.__init__)


def test_nabla::return_constructor_args():
    sig = inspect.signature(nabla::Return.__init__)
    params = list(sig.parameters.keys())



def test_nabla::itemdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::ItemDefinition)


def test_nabla::itemdefinition_constructor_exists():
    assert callable(nabla::ItemDefinition.__init__)


def test_nabla::itemdefinition_constructor_args():
    sig = inspect.signature(nabla::ItemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla::instructionblock_is_not_abstract():
    assert not inspect.isabstract(nabla::InstructionBlock)


def test_nabla::instructionblock_constructor_exists():
    assert callable(nabla::InstructionBlock.__init__)


def test_nabla::instructionblock_constructor_args():
    sig = inspect.signature(nabla::InstructionBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla::if_is_not_abstract():
    assert not inspect.isabstract(nabla::If)


def test_nabla::if_constructor_exists():
    assert callable(nabla::If.__init__)


def test_nabla::if_constructor_args():
    sig = inspect.signature(nabla::If.__init__)
    params = list(sig.parameters.keys())



def test_nabla::exit_is_not_abstract():
    assert not inspect.isabstract(nabla::Exit)


def test_nabla::exit_constructor_exists():
    assert callable(nabla::Exit.__init__)


def test_nabla::exit_constructor_args():
    sig = inspect.signature(nabla::Exit.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_nabla::exit_has_message():
    assert hasattr(nabla::Exit, "message")
    descriptor = None
    for klass in nabla::Exit.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_nabla::affectation_is_not_abstract():
    assert not inspect.isabstract(nabla::Affectation)


def test_nabla::affectation_constructor_exists():
    assert callable(nabla::Affectation.__init__)


def test_nabla::affectation_constructor_args():
    sig = inspect.signature(nabla::Affectation.__init__)
    params = list(sig.parameters.keys())



def test_nabla::loop_is_not_abstract():
    assert not inspect.isabstract(nabla::Loop)


def test_nabla::loop_constructor_exists():
    assert callable(nabla::Loop.__init__)


def test_nabla::loop_constructor_args():
    sig = inspect.signature(nabla::Loop.__init__)
    params = list(sig.parameters.keys())



def test_nabla::setdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::SetDefinition)


def test_nabla::setdefinition_constructor_exists():
    assert callable(nabla::SetDefinition.__init__)


def test_nabla::setdefinition_constructor_args():
    sig = inspect.signature(nabla::SetDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::setdefinition_has_name():
    assert hasattr(nabla::SetDefinition, "name")
    descriptor = None
    for klass in nabla::SetDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla::iterationblock_is_not_abstract():
    assert not inspect.isabstract(nabla::IterationBlock)


def test_nabla::iterationblock_constructor_exists():
    assert callable(nabla::IterationBlock.__init__)


def test_nabla::iterationblock_constructor_args():
    sig = inspect.signature(nabla::IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla::iterable_is_not_abstract():
    assert not inspect.isabstract(nabla::Iterable)


def test_nabla::iterable_constructor_exists():
    assert callable(nabla::Iterable.__init__)


def test_nabla::iterable_constructor_args():
    sig = inspect.signature(nabla::Iterable.__init__)
    params = list(sig.parameters.keys())



def test_nabla::instruction_is_not_abstract():
    assert not inspect.isabstract(nabla::Instruction)


def test_nabla::instruction_constructor_exists():
    assert callable(nabla::Instruction.__init__)


def test_nabla::instruction_constructor_args():
    sig = inspect.signature(nabla::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_connectivity_is_not_abstract():
    assert not inspect.isabstract(Connectivity)


def test_connectivity_constructor_exists():
    assert callable(Connectivity.__init__)


def test_connectivity_constructor_args():
    sig = inspect.signature(Connectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla::singleconnectivity_is_not_abstract():
    assert not inspect.isabstract(nabla::SingleConnectivity)


def test_nabla::singleconnectivity_constructor_exists():
    assert callable(nabla::SingleConnectivity.__init__)


def test_nabla::singleconnectivity_constructor_args():
    sig = inspect.signature(nabla::SingleConnectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla::multipleconnectivity_is_not_abstract():
    assert not inspect.isabstract(nabla::MultipleConnectivity)


def test_nabla::multipleconnectivity_constructor_exists():
    assert callable(nabla::MultipleConnectivity.__init__)


def test_nabla::multipleconnectivity_constructor_args():
    sig = inspect.signature(nabla::MultipleConnectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla::expression_is_not_abstract():
    assert not inspect.isabstract(nabla::Expression)


def test_nabla::expression_constructor_exists():
    assert callable(nabla::Expression.__init__)


def test_nabla::expression_constructor_args():
    sig = inspect.signature(nabla::Expression.__init__)
    params = list(sig.parameters.keys())



def test_nabla::simplevar_is_not_abstract():
    assert not inspect.isabstract(nabla::SimpleVar)


def test_nabla::simplevar_constructor_exists():
    assert callable(nabla::SimpleVar.__init__)


def test_nabla::simplevar_constructor_args():
    sig = inspect.signature(nabla::SimpleVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla::job_is_not_abstract():
    assert not inspect.isabstract(nabla::Job)


def test_nabla::job_constructor_exists():
    assert callable(nabla::Job.__init__)


def test_nabla::job_constructor_args():
    sig = inspect.signature(nabla::Job.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::job_has_name():
    assert hasattr(nabla::Job, "name")
    descriptor = None
    for klass in nabla::Job.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla::timeiteratordefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::TimeIteratorDefinition)


def test_nabla::timeiteratordefinition_constructor_exists():
    assert callable(nabla::TimeIteratorDefinition.__init__)


def test_nabla::timeiteratordefinition_constructor_args():
    sig = inspect.signature(nabla::TimeIteratorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla::vargroupdeclaration_is_not_abstract():
    assert not inspect.isabstract(nabla::VarGroupDeclaration)


def test_nabla::vargroupdeclaration_constructor_exists():
    assert callable(nabla::VarGroupDeclaration.__init__)


def test_nabla::vargroupdeclaration_constructor_args():
    sig = inspect.signature(nabla::VarGroupDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nabla::simplevardefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::SimpleVarDefinition)


def test_nabla::simplevardefinition_constructor_exists():
    assert callable(nabla::SimpleVarDefinition.__init__)


def test_nabla::simplevardefinition_constructor_args():
    sig = inspect.signature(nabla::SimpleVarDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla::optdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla::OptDefinition)


def test_nabla::optdefinition_constructor_exists():
    assert callable(nabla::OptDefinition.__init__)


def test_nabla::optdefinition_constructor_args():
    sig = inspect.signature(nabla::OptDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla::function_is_not_abstract():
    assert not inspect.isabstract(nabla::Function)


def test_nabla::function_constructor_exists():
    assert callable(nabla::Function.__init__)


def test_nabla::function_constructor_args():
    sig = inspect.signature(nabla::Function.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"

def test_nabla::function_has_external():
    assert hasattr(nabla::Function, "external")
    descriptor = None
    for klass in nabla::Function.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)



def test_nabla::itemtype_is_not_abstract():
    assert not inspect.isabstract(nabla::ItemType)


def test_nabla::itemtype_constructor_exists():
    assert callable(nabla::ItemType.__init__)


def test_nabla::itemtype_constructor_args():
    sig = inspect.signature(nabla::ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::itemtype_has_name():
    assert hasattr(nabla::ItemType, "name")
    descriptor = None
    for klass in nabla::ItemType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla::import_is_not_abstract():
    assert not inspect.isabstract(nabla::Import)


def test_nabla::import_constructor_exists():
    assert callable(nabla::Import.__init__)


def test_nabla::import_constructor_args():
    sig = inspect.signature(nabla::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_nabla::import_has_importedNamespace():
    assert hasattr(nabla::Import, "importedNamespace")
    descriptor = None
    for klass in nabla::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_nabla::nablamodule_is_not_abstract():
    assert not inspect.isabstract(nabla::NablaModule)


def test_nabla::nablamodule_constructor_exists():
    assert callable(nabla::NablaModule.__init__)


def test_nabla::nablamodule_constructor_args():
    sig = inspect.signature(nabla::NablaModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla::nablamodule_has_name():
    assert hasattr(nabla::NablaModule, "name")
    descriptor = None
    for klass in nabla::NablaModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "Bool",
        "Int",
        "Real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
Expression_strategy = st.builds(
    Expression,
)
nabla::MaxConstant_strategy = st.builds(
    nabla::MaxConstant,
    type=
        safe_text
)
nabla::Minus_strategy = st.builds(
    nabla::Minus,
    op=
        safe_text
)
nabla::Or_strategy = st.builds(
    nabla::Or,
    op=
        safe_text
)
nabla::BaseTypeConstant_strategy = st.builds(
    nabla::BaseTypeConstant,
)
nabla::Parenthesis_strategy = st.builds(
    nabla::Parenthesis,
)
nabla::Equality_strategy = st.builds(
    nabla::Equality,
    op=
        safe_text
)
nabla::Cardinality_strategy = st.builds(
    nabla::Cardinality,
)
nabla::FunctionCall_strategy = st.builds(
    nabla::FunctionCall,
)
nabla::Modulo_strategy = st.builds(
    nabla::Modulo,
    op=
        safe_text
)
nabla::Not_strategy = st.builds(
    nabla::Not,
)
nabla::And_strategy = st.builds(
    nabla::And,
    op=
        safe_text
)
nabla::MinConstant_strategy = st.builds(
    nabla::MinConstant,
    type=
        safe_text
)
nabla::VectorConstant_strategy = st.builds(
    nabla::VectorConstant,
)
nabla::Comparison_strategy = st.builds(
    nabla::Comparison,
    op=
        safe_text
)
nabla::UnaryMinus_strategy = st.builds(
    nabla::UnaryMinus,
)
nabla::Mul_strategy = st.builds(
    nabla::Mul,
    op=
        safe_text
)
nabla::BoolConstant_strategy = st.builds(
    nabla::BoolConstant,
    value=
        st.booleans()
)
nabla::Plus_strategy = st.builds(
    nabla::Plus,
    op=
        safe_text
)
nabla::Div_strategy = st.builds(
    nabla::Div,
    op=
        safe_text
)
nabla::ContractedIf_strategy = st.builds(
    nabla::ContractedIf,
)
nabla::RealConstant_strategy = st.builds(
    nabla::RealConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
nabla::IntConstant_strategy = st.builds(
    nabla::IntConstant,
    value=
        st.integers()
)
FunctionOrReduction_strategy = st.builds(
    FunctionOrReduction,
)
nabla::FunctionOrReduction_strategy = st.builds(
    nabla::FunctionOrReduction,
    name=
        safe_text
)
Var_strategy = st.builds(
    Var,
)
nabla::ConnectivityVar_strategy = st.builds(
    nabla::ConnectivityVar,
)
nabla::ArgOrVar_strategy = st.builds(
    nabla::ArgOrVar,
    name=
        safe_text
)
TimeIteratorRef_strategy = st.builds(
    TimeIteratorRef,
)
nabla::NextTimeIteratorRef_strategy = st.builds(
    nabla::NextTimeIteratorRef,
    value=
        st.integers()
)
nabla::InitTimeIteratorRef_strategy = st.builds(
    nabla::InitTimeIteratorRef,
    value=
        st.integers()
)
nabla::CurrentTimeIteratorRef_strategy = st.builds(
    nabla::CurrentTimeIteratorRef,
)
nabla::TimeIteratorRef_strategy = st.builds(
    nabla::TimeIteratorRef,
)
ArgOrVar_strategy = st.builds(
    ArgOrVar,
)
nabla::Arg_strategy = st.builds(
    nabla::Arg,
)
nabla::TimeIterator_strategy = st.builds(
    nabla::TimeIterator,
)
ConnectivityCall_strategy = st.builds(
    ConnectivityCall,
)
nabla::ItemRef_strategy = st.builds(
    nabla::ItemRef,
    dec=
        st.integers(),
    inc=
        st.integers()
)
nabla::ConnectivityCall_strategy = st.builds(
    nabla::ConnectivityCall,
)
nabla::Var_strategy = st.builds(
    nabla::Var,
)
nabla::SingletonDefinition_strategy = st.builds(
    nabla::SingletonDefinition,
)
IterationBlock_strategy = st.builds(
    IterationBlock,
)
nabla::Interval_strategy = st.builds(
    nabla::Interval,
    from_=
        st.integers()
)
nabla::SpaceIterator_strategy = st.builds(
    nabla::SpaceIterator,
)
Container_strategy = st.builds(
    Container,
)
nabla::SetRef_strategy = st.builds(
    nabla::SetRef,
)
nabla::Container_strategy = st.builds(
    nabla::Container,
)
nabla::MultipleConnectivityCall_strategy = st.builds(
    nabla::MultipleConnectivityCall,
)
nabla::SingleConnectivityCall_strategy = st.builds(
    nabla::SingleConnectivityCall,
)
nabla::Item_strategy = st.builds(
    nabla::Item,
    name=
        safe_text
)
nabla::ArgOrVarRef_strategy = st.builds(
    nabla::ArgOrVarRef,
)
Iterable_strategy = st.builds(
    Iterable,
)
nabla::ReductionCall_strategy = st.builds(
    nabla::ReductionCall,
)
nabla::Reduction_strategy = st.builds(
    nabla::Reduction,
)
nabla::Connectivity_strategy = st.builds(
    nabla::Connectivity,
    name=
        safe_text
)
nabla::BaseType_strategy = st.builds(
    nabla::BaseType,
    primitive=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
nabla::Return_strategy = st.builds(
    nabla::Return,
)
nabla::ItemDefinition_strategy = st.builds(
    nabla::ItemDefinition,
)
nabla::InstructionBlock_strategy = st.builds(
    nabla::InstructionBlock,
)
nabla::If_strategy = st.builds(
    nabla::If,
)
nabla::Exit_strategy = st.builds(
    nabla::Exit,
    message=
        safe_text
)
nabla::Affectation_strategy = st.builds(
    nabla::Affectation,
)
nabla::Loop_strategy = st.builds(
    nabla::Loop,
)
nabla::SetDefinition_strategy = st.builds(
    nabla::SetDefinition,
    name=
        safe_text
)
nabla::IterationBlock_strategy = st.builds(
    nabla::IterationBlock,
)
nabla::Iterable_strategy = st.builds(
    nabla::Iterable,
)
nabla::Instruction_strategy = st.builds(
    nabla::Instruction,
)
Connectivity_strategy = st.builds(
    Connectivity,
)
nabla::SingleConnectivity_strategy = st.builds(
    nabla::SingleConnectivity,
)
nabla::MultipleConnectivity_strategy = st.builds(
    nabla::MultipleConnectivity,
)
nabla::Expression_strategy = st.builds(
    nabla::Expression,
)
nabla::SimpleVar_strategy = st.builds(
    nabla::SimpleVar,
)
nabla::Job_strategy = st.builds(
    nabla::Job,
    name=
        safe_text
)
nabla::TimeIteratorDefinition_strategy = st.builds(
    nabla::TimeIteratorDefinition,
)
nabla::VarGroupDeclaration_strategy = st.builds(
    nabla::VarGroupDeclaration,
)
nabla::SimpleVarDefinition_strategy = st.builds(
    nabla::SimpleVarDefinition,
)
nabla::OptDefinition_strategy = st.builds(
    nabla::OptDefinition,
)
nabla::Function_strategy = st.builds(
    nabla::Function,
    external=
        st.booleans()
)
nabla::ItemType_strategy = st.builds(
    nabla::ItemType,
    name=
        safe_text
)
nabla::Import_strategy = st.builds(
    nabla::Import,
    importedNamespace=
        safe_text
)
nabla::NablaModule_strategy = st.builds(
    nabla::NablaModule,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=nabla::MaxConstant_strategy)
@settings(max_examples=50)
def test_nabla::maxconstant_instantiation(instance):
    assert isinstance(instance, nabla::MaxConstant)

@given(instance=nabla::MaxConstant_strategy)
def test_nabla::maxconstant_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=nabla::MaxConstant_strategy)
def test_nabla::maxconstant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=nabla::Minus_strategy)
@settings(max_examples=50)
def test_nabla::minus_instantiation(instance):
    assert isinstance(instance, nabla::Minus)

@given(instance=nabla::Minus_strategy)
def test_nabla::minus_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Minus_strategy)
def test_nabla::minus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::Or_strategy)
@settings(max_examples=50)
def test_nabla::or_instantiation(instance):
    assert isinstance(instance, nabla::Or)

@given(instance=nabla::Or_strategy)
def test_nabla::or_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Or_strategy)
def test_nabla::or_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::BaseTypeConstant_strategy)
@settings(max_examples=50)
def test_nabla::basetypeconstant_instantiation(instance):
    assert isinstance(instance, nabla::BaseTypeConstant)

@given(instance=nabla::Parenthesis_strategy)
@settings(max_examples=50)
def test_nabla::parenthesis_instantiation(instance):
    assert isinstance(instance, nabla::Parenthesis)

@given(instance=nabla::Equality_strategy)
@settings(max_examples=50)
def test_nabla::equality_instantiation(instance):
    assert isinstance(instance, nabla::Equality)

@given(instance=nabla::Equality_strategy)
def test_nabla::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Equality_strategy)
def test_nabla::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::Cardinality_strategy)
@settings(max_examples=50)
def test_nabla::cardinality_instantiation(instance):
    assert isinstance(instance, nabla::Cardinality)

@given(instance=nabla::FunctionCall_strategy)
@settings(max_examples=50)
def test_nabla::functioncall_instantiation(instance):
    assert isinstance(instance, nabla::FunctionCall)

@given(instance=nabla::Modulo_strategy)
@settings(max_examples=50)
def test_nabla::modulo_instantiation(instance):
    assert isinstance(instance, nabla::Modulo)

@given(instance=nabla::Modulo_strategy)
def test_nabla::modulo_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Modulo_strategy)
def test_nabla::modulo_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::Not_strategy)
@settings(max_examples=50)
def test_nabla::not_instantiation(instance):
    assert isinstance(instance, nabla::Not)

@given(instance=nabla::And_strategy)
@settings(max_examples=50)
def test_nabla::and_instantiation(instance):
    assert isinstance(instance, nabla::And)

@given(instance=nabla::And_strategy)
def test_nabla::and_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::And_strategy)
def test_nabla::and_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::MinConstant_strategy)
@settings(max_examples=50)
def test_nabla::minconstant_instantiation(instance):
    assert isinstance(instance, nabla::MinConstant)

@given(instance=nabla::MinConstant_strategy)
def test_nabla::minconstant_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=nabla::MinConstant_strategy)
def test_nabla::minconstant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=nabla::VectorConstant_strategy)
@settings(max_examples=50)
def test_nabla::vectorconstant_instantiation(instance):
    assert isinstance(instance, nabla::VectorConstant)

@given(instance=nabla::Comparison_strategy)
@settings(max_examples=50)
def test_nabla::comparison_instantiation(instance):
    assert isinstance(instance, nabla::Comparison)

@given(instance=nabla::Comparison_strategy)
def test_nabla::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Comparison_strategy)
def test_nabla::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::UnaryMinus_strategy)
@settings(max_examples=50)
def test_nabla::unaryminus_instantiation(instance):
    assert isinstance(instance, nabla::UnaryMinus)

@given(instance=nabla::Mul_strategy)
@settings(max_examples=50)
def test_nabla::mul_instantiation(instance):
    assert isinstance(instance, nabla::Mul)

@given(instance=nabla::Mul_strategy)
def test_nabla::mul_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Mul_strategy)
def test_nabla::mul_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::BoolConstant_strategy)
@settings(max_examples=50)
def test_nabla::boolconstant_instantiation(instance):
    assert isinstance(instance, nabla::BoolConstant)

@given(instance=nabla::BoolConstant_strategy)
def test_nabla::boolconstant_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=nabla::BoolConstant_strategy)
def test_nabla::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla::Plus_strategy)
@settings(max_examples=50)
def test_nabla::plus_instantiation(instance):
    assert isinstance(instance, nabla::Plus)

@given(instance=nabla::Plus_strategy)
def test_nabla::plus_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Plus_strategy)
def test_nabla::plus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::Div_strategy)
@settings(max_examples=50)
def test_nabla::div_instantiation(instance):
    assert isinstance(instance, nabla::Div)

@given(instance=nabla::Div_strategy)
def test_nabla::div_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nabla::Div_strategy)
def test_nabla::div_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla::ContractedIf_strategy)
@settings(max_examples=50)
def test_nabla::contractedif_instantiation(instance):
    assert isinstance(instance, nabla::ContractedIf)

@given(instance=nabla::RealConstant_strategy)
@settings(max_examples=50)
def test_nabla::realconstant_instantiation(instance):
    assert isinstance(instance, nabla::RealConstant)

@given(instance=nabla::RealConstant_strategy)
def test_nabla::realconstant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=nabla::RealConstant_strategy)
def test_nabla::realconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla::IntConstant_strategy)
@settings(max_examples=50)
def test_nabla::intconstant_instantiation(instance):
    assert isinstance(instance, nabla::IntConstant)

@given(instance=nabla::IntConstant_strategy)
def test_nabla::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=nabla::IntConstant_strategy)
def test_nabla::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FunctionOrReduction_strategy)
@settings(max_examples=50)
def test_functionorreduction_instantiation(instance):
    assert isinstance(instance, FunctionOrReduction)

@given(instance=nabla::FunctionOrReduction_strategy)
@settings(max_examples=50)
def test_nabla::functionorreduction_instantiation(instance):
    assert isinstance(instance, nabla::FunctionOrReduction)

@given(instance=nabla::FunctionOrReduction_strategy)
def test_nabla::functionorreduction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::FunctionOrReduction_strategy)
def test_nabla::functionorreduction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Var_strategy)
@settings(max_examples=50)
def test_var_instantiation(instance):
    assert isinstance(instance, Var)

@given(instance=nabla::ConnectivityVar_strategy)
@settings(max_examples=50)
def test_nabla::connectivityvar_instantiation(instance):
    assert isinstance(instance, nabla::ConnectivityVar)

@given(instance=nabla::ArgOrVar_strategy)
@settings(max_examples=50)
def test_nabla::argorvar_instantiation(instance):
    assert isinstance(instance, nabla::ArgOrVar)

@given(instance=nabla::ArgOrVar_strategy)
def test_nabla::argorvar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::ArgOrVar_strategy)
def test_nabla::argorvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TimeIteratorRef_strategy)
@settings(max_examples=50)
def test_timeiteratorref_instantiation(instance):
    assert isinstance(instance, TimeIteratorRef)

@given(instance=nabla::NextTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla::nexttimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla::NextTimeIteratorRef)

@given(instance=nabla::NextTimeIteratorRef_strategy)
def test_nabla::nexttimeiteratorref_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=nabla::NextTimeIteratorRef_strategy)
def test_nabla::nexttimeiteratorref_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla::InitTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla::inittimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla::InitTimeIteratorRef)

@given(instance=nabla::InitTimeIteratorRef_strategy)
def test_nabla::inittimeiteratorref_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=nabla::InitTimeIteratorRef_strategy)
def test_nabla::inittimeiteratorref_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla::CurrentTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla::currenttimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla::CurrentTimeIteratorRef)

@given(instance=nabla::TimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla::timeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla::TimeIteratorRef)

@given(instance=ArgOrVar_strategy)
@settings(max_examples=50)
def test_argorvar_instantiation(instance):
    assert isinstance(instance, ArgOrVar)

@given(instance=nabla::Arg_strategy)
@settings(max_examples=50)
def test_nabla::arg_instantiation(instance):
    assert isinstance(instance, nabla::Arg)

@given(instance=nabla::TimeIterator_strategy)
@settings(max_examples=50)
def test_nabla::timeiterator_instantiation(instance):
    assert isinstance(instance, nabla::TimeIterator)

@given(instance=ConnectivityCall_strategy)
@settings(max_examples=50)
def test_connectivitycall_instantiation(instance):
    assert isinstance(instance, ConnectivityCall)

@given(instance=nabla::ItemRef_strategy)
@settings(max_examples=50)
def test_nabla::itemref_instantiation(instance):
    assert isinstance(instance, nabla::ItemRef)

@given(instance=nabla::ItemRef_strategy)
def test_nabla::itemref_dec_type(instance):
    assert isinstance(instance.dec, int)


@given(instance=nabla::ItemRef_strategy)
def test_nabla::itemref_dec_setter(instance):
    original = instance.dec
    instance.dec = original
    assert instance.dec == original

@given(instance=nabla::ItemRef_strategy)
def test_nabla::itemref_inc_type(instance):
    assert isinstance(instance.inc, int)


@given(instance=nabla::ItemRef_strategy)
def test_nabla::itemref_inc_setter(instance):
    original = instance.inc
    instance.inc = original
    assert instance.inc == original

@given(instance=nabla::ConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla::connectivitycall_instantiation(instance):
    assert isinstance(instance, nabla::ConnectivityCall)

@given(instance=nabla::Var_strategy)
@settings(max_examples=50)
def test_nabla::var_instantiation(instance):
    assert isinstance(instance, nabla::Var)

@given(instance=nabla::SingletonDefinition_strategy)
@settings(max_examples=50)
def test_nabla::singletondefinition_instantiation(instance):
    assert isinstance(instance, nabla::SingletonDefinition)

@given(instance=IterationBlock_strategy)
@settings(max_examples=50)
def test_iterationblock_instantiation(instance):
    assert isinstance(instance, IterationBlock)

@given(instance=nabla::Interval_strategy)
@settings(max_examples=50)
def test_nabla::interval_instantiation(instance):
    assert isinstance(instance, nabla::Interval)

@given(instance=nabla::Interval_strategy)
def test_nabla::interval_from__type(instance):
    assert isinstance(instance.from_, int)


@given(instance=nabla::Interval_strategy)
def test_nabla::interval_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=nabla::SpaceIterator_strategy)
@settings(max_examples=50)
def test_nabla::spaceiterator_instantiation(instance):
    assert isinstance(instance, nabla::SpaceIterator)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=nabla::SetRef_strategy)
@settings(max_examples=50)
def test_nabla::setref_instantiation(instance):
    assert isinstance(instance, nabla::SetRef)

@given(instance=nabla::Container_strategy)
@settings(max_examples=50)
def test_nabla::container_instantiation(instance):
    assert isinstance(instance, nabla::Container)

@given(instance=nabla::MultipleConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla::multipleconnectivitycall_instantiation(instance):
    assert isinstance(instance, nabla::MultipleConnectivityCall)

@given(instance=nabla::SingleConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla::singleconnectivitycall_instantiation(instance):
    assert isinstance(instance, nabla::SingleConnectivityCall)

@given(instance=nabla::Item_strategy)
@settings(max_examples=50)
def test_nabla::item_instantiation(instance):
    assert isinstance(instance, nabla::Item)

@given(instance=nabla::Item_strategy)
def test_nabla::item_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::Item_strategy)
def test_nabla::item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla::ArgOrVarRef_strategy)
@settings(max_examples=50)
def test_nabla::argorvarref_instantiation(instance):
    assert isinstance(instance, nabla::ArgOrVarRef)

@given(instance=Iterable_strategy)
@settings(max_examples=50)
def test_iterable_instantiation(instance):
    assert isinstance(instance, Iterable)

@given(instance=nabla::ReductionCall_strategy)
@settings(max_examples=50)
def test_nabla::reductioncall_instantiation(instance):
    assert isinstance(instance, nabla::ReductionCall)

@given(instance=nabla::Reduction_strategy)
@settings(max_examples=50)
def test_nabla::reduction_instantiation(instance):
    assert isinstance(instance, nabla::Reduction)

@given(instance=nabla::Connectivity_strategy)
@settings(max_examples=50)
def test_nabla::connectivity_instantiation(instance):
    assert isinstance(instance, nabla::Connectivity)

@given(instance=nabla::Connectivity_strategy)
def test_nabla::connectivity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::Connectivity_strategy)
def test_nabla::connectivity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla::BaseType_strategy)
@settings(max_examples=50)
def test_nabla::basetype_instantiation(instance):
    assert isinstance(instance, nabla::BaseType)

@given(instance=nabla::BaseType_strategy)
def test_nabla::basetype_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=nabla::BaseType_strategy)
def test_nabla::basetype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=nabla::Return_strategy)
@settings(max_examples=50)
def test_nabla::return_instantiation(instance):
    assert isinstance(instance, nabla::Return)

@given(instance=nabla::ItemDefinition_strategy)
@settings(max_examples=50)
def test_nabla::itemdefinition_instantiation(instance):
    assert isinstance(instance, nabla::ItemDefinition)

@given(instance=nabla::InstructionBlock_strategy)
@settings(max_examples=50)
def test_nabla::instructionblock_instantiation(instance):
    assert isinstance(instance, nabla::InstructionBlock)

@given(instance=nabla::If_strategy)
@settings(max_examples=50)
def test_nabla::if_instantiation(instance):
    assert isinstance(instance, nabla::If)

@given(instance=nabla::Exit_strategy)
@settings(max_examples=50)
def test_nabla::exit_instantiation(instance):
    assert isinstance(instance, nabla::Exit)

@given(instance=nabla::Exit_strategy)
def test_nabla::exit_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=nabla::Exit_strategy)
def test_nabla::exit_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=nabla::Affectation_strategy)
@settings(max_examples=50)
def test_nabla::affectation_instantiation(instance):
    assert isinstance(instance, nabla::Affectation)

@given(instance=nabla::Loop_strategy)
@settings(max_examples=50)
def test_nabla::loop_instantiation(instance):
    assert isinstance(instance, nabla::Loop)

@given(instance=nabla::SetDefinition_strategy)
@settings(max_examples=50)
def test_nabla::setdefinition_instantiation(instance):
    assert isinstance(instance, nabla::SetDefinition)

@given(instance=nabla::SetDefinition_strategy)
def test_nabla::setdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::SetDefinition_strategy)
def test_nabla::setdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla::IterationBlock_strategy)
@settings(max_examples=50)
def test_nabla::iterationblock_instantiation(instance):
    assert isinstance(instance, nabla::IterationBlock)

@given(instance=nabla::Iterable_strategy)
@settings(max_examples=50)
def test_nabla::iterable_instantiation(instance):
    assert isinstance(instance, nabla::Iterable)

@given(instance=nabla::Instruction_strategy)
@settings(max_examples=50)
def test_nabla::instruction_instantiation(instance):
    assert isinstance(instance, nabla::Instruction)

@given(instance=Connectivity_strategy)
@settings(max_examples=50)
def test_connectivity_instantiation(instance):
    assert isinstance(instance, Connectivity)

@given(instance=nabla::SingleConnectivity_strategy)
@settings(max_examples=50)
def test_nabla::singleconnectivity_instantiation(instance):
    assert isinstance(instance, nabla::SingleConnectivity)

@given(instance=nabla::MultipleConnectivity_strategy)
@settings(max_examples=50)
def test_nabla::multipleconnectivity_instantiation(instance):
    assert isinstance(instance, nabla::MultipleConnectivity)

@given(instance=nabla::Expression_strategy)
@settings(max_examples=50)
def test_nabla::expression_instantiation(instance):
    assert isinstance(instance, nabla::Expression)

@given(instance=nabla::SimpleVar_strategy)
@settings(max_examples=50)
def test_nabla::simplevar_instantiation(instance):
    assert isinstance(instance, nabla::SimpleVar)

@given(instance=nabla::Job_strategy)
@settings(max_examples=50)
def test_nabla::job_instantiation(instance):
    assert isinstance(instance, nabla::Job)

@given(instance=nabla::Job_strategy)
def test_nabla::job_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::Job_strategy)
def test_nabla::job_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla::TimeIteratorDefinition_strategy)
@settings(max_examples=50)
def test_nabla::timeiteratordefinition_instantiation(instance):
    assert isinstance(instance, nabla::TimeIteratorDefinition)

@given(instance=nabla::VarGroupDeclaration_strategy)
@settings(max_examples=50)
def test_nabla::vargroupdeclaration_instantiation(instance):
    assert isinstance(instance, nabla::VarGroupDeclaration)

@given(instance=nabla::SimpleVarDefinition_strategy)
@settings(max_examples=50)
def test_nabla::simplevardefinition_instantiation(instance):
    assert isinstance(instance, nabla::SimpleVarDefinition)

@given(instance=nabla::OptDefinition_strategy)
@settings(max_examples=50)
def test_nabla::optdefinition_instantiation(instance):
    assert isinstance(instance, nabla::OptDefinition)

@given(instance=nabla::Function_strategy)
@settings(max_examples=50)
def test_nabla::function_instantiation(instance):
    assert isinstance(instance, nabla::Function)

@given(instance=nabla::Function_strategy)
def test_nabla::function_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=nabla::Function_strategy)
def test_nabla::function_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=nabla::ItemType_strategy)
@settings(max_examples=50)
def test_nabla::itemtype_instantiation(instance):
    assert isinstance(instance, nabla::ItemType)

@given(instance=nabla::ItemType_strategy)
def test_nabla::itemtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::ItemType_strategy)
def test_nabla::itemtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla::Import_strategy)
@settings(max_examples=50)
def test_nabla::import_instantiation(instance):
    assert isinstance(instance, nabla::Import)

@given(instance=nabla::Import_strategy)
def test_nabla::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=nabla::Import_strategy)
def test_nabla::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=nabla::NablaModule_strategy)
@settings(max_examples=50)
def test_nabla::nablamodule_instantiation(instance):
    assert isinstance(instance, nabla::NablaModule)

@given(instance=nabla::NablaModule_strategy)
def test_nabla::nablamodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nabla::NablaModule_strategy)
def test_nabla::nablamodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
