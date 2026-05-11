import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AccessControl,
    smc::Covered,
    smc::BellLapadula,
    Expression,
    smc::Dict,
    smc::Not,
    smc::IntLiteral,
    smc::StringLiteral,
    smc::MulOrDiv,
    smc::DoubleLiteral,
    smc::DateLiteral,
    smc::Equality,
    smc::PlusOrMinus,
    smc::And,
    smc::Or,
    smc::Comparison,
    smc::BooleanLiteral,
    smc::List,
    smc::TimeLiteral,
    smc::VariableRef,
    smc::Tuple,
    Download,
    smc::Client,
    smc::Database,
    AbstractAssignment,
    smc::Download,
    Computation,
    smc::Median,
    smc::Count,
    smc::WeightedAvg,
    smc::Average,
    smc::Multiplication,
    Functions,
    smc::AddValues,
    smc::BloomFilter,
    smc::Search,
    smc::CreateTable,
    smc::AccessControl,
    smc::CheckTable,
    smc::Computation,
    smc::Functions,
    smc::Expression,
    smc::Invocation,
    Command,
    smc::IfThenElse,
    smc::Return,
    smc::While,
    smc::InvocationVoid,
    smc::Block,
    smc::Print,
    smc::ParamDecl,
    smc::VariableAssignment,
    smc::AbstractAssignment,
    smc::VariableDecl,
    smc::Smc,
    smc::Command,
    smc::MainSMC,
    smc::BlockSMC,
    SecType,
    BlockType,
    BasicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(AccessControl)


def test_accesscontrol_constructor_exists():
    assert callable(AccessControl.__init__)


def test_accesscontrol_constructor_args():
    sig = inspect.signature(AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_smc::covered_is_not_abstract():
    assert not inspect.isabstract(smc::Covered)


def test_smc::covered_constructor_exists():
    assert callable(smc::Covered.__init__)


def test_smc::covered_constructor_args():
    sig = inspect.signature(smc::Covered.__init__)
    params = list(sig.parameters.keys())



def test_smc::belllapadula_is_not_abstract():
    assert not inspect.isabstract(smc::BellLapadula)


def test_smc::belllapadula_constructor_exists():
    assert callable(smc::BellLapadula.__init__)


def test_smc::belllapadula_constructor_args():
    sig = inspect.signature(smc::BellLapadula.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_smc::belllapadula_has_mode():
    assert hasattr(smc::BellLapadula, "mode")
    descriptor = None
    for klass in smc::BellLapadula.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_smc::dict_is_not_abstract():
    assert not inspect.isabstract(smc::Dict)


def test_smc::dict_constructor_exists():
    assert callable(smc::Dict.__init__)


def test_smc::dict_constructor_args():
    sig = inspect.signature(smc::Dict.__init__)
    params = list(sig.parameters.keys())



def test_smc::not_is_not_abstract():
    assert not inspect.isabstract(smc::Not)


def test_smc::not_constructor_exists():
    assert callable(smc::Not.__init__)


def test_smc::not_constructor_args():
    sig = inspect.signature(smc::Not.__init__)
    params = list(sig.parameters.keys())



def test_smc::intliteral_is_not_abstract():
    assert not inspect.isabstract(smc::IntLiteral)


def test_smc::intliteral_constructor_exists():
    assert callable(smc::IntLiteral.__init__)


def test_smc::intliteral_constructor_args():
    sig = inspect.signature(smc::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::intliteral_has_value():
    assert hasattr(smc::IntLiteral, "value")
    descriptor = None
    for klass in smc::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::stringliteral_is_not_abstract():
    assert not inspect.isabstract(smc::StringLiteral)


def test_smc::stringliteral_constructor_exists():
    assert callable(smc::StringLiteral.__init__)


def test_smc::stringliteral_constructor_args():
    sig = inspect.signature(smc::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::stringliteral_has_value():
    assert hasattr(smc::StringLiteral, "value")
    descriptor = None
    for klass in smc::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::mulordiv_is_not_abstract():
    assert not inspect.isabstract(smc::MulOrDiv)


def test_smc::mulordiv_constructor_exists():
    assert callable(smc::MulOrDiv.__init__)


def test_smc::mulordiv_constructor_args():
    sig = inspect.signature(smc::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc::mulordiv_has_op():
    assert hasattr(smc::MulOrDiv, "op")
    descriptor = None
    for klass in smc::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(smc::DoubleLiteral)


def test_smc::doubleliteral_constructor_exists():
    assert callable(smc::DoubleLiteral.__init__)


def test_smc::doubleliteral_constructor_args():
    sig = inspect.signature(smc::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::doubleliteral_has_value():
    assert hasattr(smc::DoubleLiteral, "value")
    descriptor = None
    for klass in smc::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::dateliteral_is_not_abstract():
    assert not inspect.isabstract(smc::DateLiteral)


def test_smc::dateliteral_constructor_exists():
    assert callable(smc::DateLiteral.__init__)


def test_smc::dateliteral_constructor_args():
    sig = inspect.signature(smc::DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::dateliteral_has_value():
    assert hasattr(smc::DateLiteral, "value")
    descriptor = None
    for klass in smc::DateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::equality_is_not_abstract():
    assert not inspect.isabstract(smc::Equality)


def test_smc::equality_constructor_exists():
    assert callable(smc::Equality.__init__)


def test_smc::equality_constructor_args():
    sig = inspect.signature(smc::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc::equality_has_op():
    assert hasattr(smc::Equality, "op")
    descriptor = None
    for klass in smc::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc::plusorminus_is_not_abstract():
    assert not inspect.isabstract(smc::PlusOrMinus)


def test_smc::plusorminus_constructor_exists():
    assert callable(smc::PlusOrMinus.__init__)


def test_smc::plusorminus_constructor_args():
    sig = inspect.signature(smc::PlusOrMinus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc::plusorminus_has_op():
    assert hasattr(smc::PlusOrMinus, "op")
    descriptor = None
    for klass in smc::PlusOrMinus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc::and_is_not_abstract():
    assert not inspect.isabstract(smc::And)


def test_smc::and_constructor_exists():
    assert callable(smc::And.__init__)


def test_smc::and_constructor_args():
    sig = inspect.signature(smc::And.__init__)
    params = list(sig.parameters.keys())



def test_smc::or_is_not_abstract():
    assert not inspect.isabstract(smc::Or)


def test_smc::or_constructor_exists():
    assert callable(smc::Or.__init__)


def test_smc::or_constructor_args():
    sig = inspect.signature(smc::Or.__init__)
    params = list(sig.parameters.keys())



def test_smc::comparison_is_not_abstract():
    assert not inspect.isabstract(smc::Comparison)


def test_smc::comparison_constructor_exists():
    assert callable(smc::Comparison.__init__)


def test_smc::comparison_constructor_args():
    sig = inspect.signature(smc::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc::comparison_has_op():
    assert hasattr(smc::Comparison, "op")
    descriptor = None
    for klass in smc::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(smc::BooleanLiteral)


def test_smc::booleanliteral_constructor_exists():
    assert callable(smc::BooleanLiteral.__init__)


def test_smc::booleanliteral_constructor_args():
    sig = inspect.signature(smc::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::booleanliteral_has_value():
    assert hasattr(smc::BooleanLiteral, "value")
    descriptor = None
    for klass in smc::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::list_is_not_abstract():
    assert not inspect.isabstract(smc::List)


def test_smc::list_constructor_exists():
    assert callable(smc::List.__init__)


def test_smc::list_constructor_args():
    sig = inspect.signature(smc::List.__init__)
    params = list(sig.parameters.keys())



def test_smc::timeliteral_is_not_abstract():
    assert not inspect.isabstract(smc::TimeLiteral)


def test_smc::timeliteral_constructor_exists():
    assert callable(smc::TimeLiteral.__init__)


def test_smc::timeliteral_constructor_args():
    sig = inspect.signature(smc::TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc::timeliteral_has_value():
    assert hasattr(smc::TimeLiteral, "value")
    descriptor = None
    for klass in smc::TimeLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc::variableref_is_not_abstract():
    assert not inspect.isabstract(smc::VariableRef)


def test_smc::variableref_constructor_exists():
    assert callable(smc::VariableRef.__init__)


def test_smc::variableref_constructor_args():
    sig = inspect.signature(smc::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_smc::tuple_is_not_abstract():
    assert not inspect.isabstract(smc::Tuple)


def test_smc::tuple_constructor_exists():
    assert callable(smc::Tuple.__init__)


def test_smc::tuple_constructor_args():
    sig = inspect.signature(smc::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_download_is_not_abstract():
    assert not inspect.isabstract(Download)


def test_download_constructor_exists():
    assert callable(Download.__init__)


def test_download_constructor_args():
    sig = inspect.signature(Download.__init__)
    params = list(sig.parameters.keys())



def test_smc::client_is_not_abstract():
    assert not inspect.isabstract(smc::Client)


def test_smc::client_constructor_exists():
    assert callable(smc::Client.__init__)


def test_smc::client_constructor_args():
    sig = inspect.signature(smc::Client.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"

def test_smc::client_has_arg():
    assert hasattr(smc::Client, "arg")
    descriptor = None
    for klass in smc::Client.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)



def test_smc::database_is_not_abstract():
    assert not inspect.isabstract(smc::Database)


def test_smc::database_constructor_exists():
    assert callable(smc::Database.__init__)


def test_smc::database_constructor_args():
    sig = inspect.signature(smc::Database.__init__)
    params = list(sig.parameters.keys())
    assert "clm" in params, "Missing parameter 'clm'"

def test_smc::database_has_clm():
    assert hasattr(smc::Database, "clm")
    descriptor = None
    for klass in smc::Database.__mro__:
        if "clm" in klass.__dict__:
            descriptor = klass.__dict__["clm"]
            break
    assert isinstance(descriptor, property)



def test_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc::download_is_not_abstract():
    assert not inspect.isabstract(smc::Download)


def test_smc::download_constructor_exists():
    assert callable(smc::Download.__init__)


def test_smc::download_constructor_args():
    sig = inspect.signature(smc::Download.__init__)
    params = list(sig.parameters.keys())



def test_computation_is_not_abstract():
    assert not inspect.isabstract(Computation)


def test_computation_constructor_exists():
    assert callable(Computation.__init__)


def test_computation_constructor_args():
    sig = inspect.signature(Computation.__init__)
    params = list(sig.parameters.keys())



def test_smc::median_is_not_abstract():
    assert not inspect.isabstract(smc::Median)


def test_smc::median_constructor_exists():
    assert callable(smc::Median.__init__)


def test_smc::median_constructor_args():
    sig = inspect.signature(smc::Median.__init__)
    params = list(sig.parameters.keys())



def test_smc::count_is_not_abstract():
    assert not inspect.isabstract(smc::Count)


def test_smc::count_constructor_exists():
    assert callable(smc::Count.__init__)


def test_smc::count_constructor_args():
    sig = inspect.signature(smc::Count.__init__)
    params = list(sig.parameters.keys())



def test_smc::weightedavg_is_not_abstract():
    assert not inspect.isabstract(smc::WeightedAvg)


def test_smc::weightedavg_constructor_exists():
    assert callable(smc::WeightedAvg.__init__)


def test_smc::weightedavg_constructor_args():
    sig = inspect.signature(smc::WeightedAvg.__init__)
    params = list(sig.parameters.keys())



def test_smc::average_is_not_abstract():
    assert not inspect.isabstract(smc::Average)


def test_smc::average_constructor_exists():
    assert callable(smc::Average.__init__)


def test_smc::average_constructor_args():
    sig = inspect.signature(smc::Average.__init__)
    params = list(sig.parameters.keys())



def test_smc::multiplication_is_not_abstract():
    assert not inspect.isabstract(smc::Multiplication)


def test_smc::multiplication_constructor_exists():
    assert callable(smc::Multiplication.__init__)


def test_smc::multiplication_constructor_args():
    sig = inspect.signature(smc::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_functions_is_not_abstract():
    assert not inspect.isabstract(Functions)


def test_functions_constructor_exists():
    assert callable(Functions.__init__)


def test_functions_constructor_args():
    sig = inspect.signature(Functions.__init__)
    params = list(sig.parameters.keys())



def test_smc::addvalues_is_not_abstract():
    assert not inspect.isabstract(smc::AddValues)


def test_smc::addvalues_constructor_exists():
    assert callable(smc::AddValues.__init__)


def test_smc::addvalues_constructor_args():
    sig = inspect.signature(smc::AddValues.__init__)
    params = list(sig.parameters.keys())



def test_smc::bloomfilter_is_not_abstract():
    assert not inspect.isabstract(smc::BloomFilter)


def test_smc::bloomfilter_constructor_exists():
    assert callable(smc::BloomFilter.__init__)


def test_smc::bloomfilter_constructor_args():
    sig = inspect.signature(smc::BloomFilter.__init__)
    params = list(sig.parameters.keys())



def test_smc::search_is_not_abstract():
    assert not inspect.isabstract(smc::Search)


def test_smc::search_constructor_exists():
    assert callable(smc::Search.__init__)


def test_smc::search_constructor_args():
    sig = inspect.signature(smc::Search.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_smc::search_has_column():
    assert hasattr(smc::Search, "column")
    descriptor = None
    for klass in smc::Search.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_smc::createtable_is_not_abstract():
    assert not inspect.isabstract(smc::CreateTable)


def test_smc::createtable_constructor_exists():
    assert callable(smc::CreateTable.__init__)


def test_smc::createtable_constructor_args():
    sig = inspect.signature(smc::CreateTable.__init__)
    params = list(sig.parameters.keys())



def test_smc::accesscontrol_is_not_abstract():
    assert not inspect.isabstract(smc::AccessControl)


def test_smc::accesscontrol_constructor_exists():
    assert callable(smc::AccessControl.__init__)


def test_smc::accesscontrol_constructor_args():
    sig = inspect.signature(smc::AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_smc::checktable_is_not_abstract():
    assert not inspect.isabstract(smc::CheckTable)


def test_smc::checktable_constructor_exists():
    assert callable(smc::CheckTable.__init__)


def test_smc::checktable_constructor_args():
    sig = inspect.signature(smc::CheckTable.__init__)
    params = list(sig.parameters.keys())



def test_smc::computation_is_not_abstract():
    assert not inspect.isabstract(smc::Computation)


def test_smc::computation_constructor_exists():
    assert callable(smc::Computation.__init__)


def test_smc::computation_constructor_args():
    sig = inspect.signature(smc::Computation.__init__)
    params = list(sig.parameters.keys())



def test_smc::functions_is_not_abstract():
    assert not inspect.isabstract(smc::Functions)


def test_smc::functions_constructor_exists():
    assert callable(smc::Functions.__init__)


def test_smc::functions_constructor_args():
    sig = inspect.signature(smc::Functions.__init__)
    params = list(sig.parameters.keys())



def test_smc::expression_is_not_abstract():
    assert not inspect.isabstract(smc::Expression)


def test_smc::expression_constructor_exists():
    assert callable(smc::Expression.__init__)


def test_smc::expression_constructor_args():
    sig = inspect.signature(smc::Expression.__init__)
    params = list(sig.parameters.keys())



def test_smc::invocation_is_not_abstract():
    assert not inspect.isabstract(smc::Invocation)


def test_smc::invocation_constructor_exists():
    assert callable(smc::Invocation.__init__)


def test_smc::invocation_constructor_args():
    sig = inspect.signature(smc::Invocation.__init__)
    params = list(sig.parameters.keys())



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_smc::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(smc::IfThenElse)


def test_smc::ifthenelse_constructor_exists():
    assert callable(smc::IfThenElse.__init__)


def test_smc::ifthenelse_constructor_args():
    sig = inspect.signature(smc::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_smc::return_is_not_abstract():
    assert not inspect.isabstract(smc::Return)


def test_smc::return_constructor_exists():
    assert callable(smc::Return.__init__)


def test_smc::return_constructor_args():
    sig = inspect.signature(smc::Return.__init__)
    params = list(sig.parameters.keys())



def test_smc::while_is_not_abstract():
    assert not inspect.isabstract(smc::While)


def test_smc::while_constructor_exists():
    assert callable(smc::While.__init__)


def test_smc::while_constructor_args():
    sig = inspect.signature(smc::While.__init__)
    params = list(sig.parameters.keys())



def test_smc::invocationvoid_is_not_abstract():
    assert not inspect.isabstract(smc::InvocationVoid)


def test_smc::invocationvoid_constructor_exists():
    assert callable(smc::InvocationVoid.__init__)


def test_smc::invocationvoid_constructor_args():
    sig = inspect.signature(smc::InvocationVoid.__init__)
    params = list(sig.parameters.keys())



def test_smc::block_is_not_abstract():
    assert not inspect.isabstract(smc::Block)


def test_smc::block_constructor_exists():
    assert callable(smc::Block.__init__)


def test_smc::block_constructor_args():
    sig = inspect.signature(smc::Block.__init__)
    params = list(sig.parameters.keys())



def test_smc::print_is_not_abstract():
    assert not inspect.isabstract(smc::Print)


def test_smc::print_constructor_exists():
    assert callable(smc::Print.__init__)


def test_smc::print_constructor_args():
    sig = inspect.signature(smc::Print.__init__)
    params = list(sig.parameters.keys())



def test_smc::paramdecl_is_not_abstract():
    assert not inspect.isabstract(smc::ParamDecl)


def test_smc::paramdecl_constructor_exists():
    assert callable(smc::ParamDecl.__init__)


def test_smc::paramdecl_constructor_args():
    sig = inspect.signature(smc::ParamDecl.__init__)
    params = list(sig.parameters.keys())
    assert "stype" in params, "Missing parameter 'stype'"
    assert "parName" in params, "Missing parameter 'parName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "btype" in params, "Missing parameter 'btype'"

def test_smc::paramdecl_has_stype():
    assert hasattr(smc::ParamDecl, "stype")
    descriptor = None
    for klass in smc::ParamDecl.__mro__:
        if "stype" in klass.__dict__:
            descriptor = klass.__dict__["stype"]
            break
    assert isinstance(descriptor, property)

def test_smc::paramdecl_has_parName():
    assert hasattr(smc::ParamDecl, "parName")
    descriptor = None
    for klass in smc::ParamDecl.__mro__:
        if "parName" in klass.__dict__:
            descriptor = klass.__dict__["parName"]
            break
    assert isinstance(descriptor, property)

def test_smc::paramdecl_has_name():
    assert hasattr(smc::ParamDecl, "name")
    descriptor = None
    for klass in smc::ParamDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc::paramdecl_has_btype():
    assert hasattr(smc::ParamDecl, "btype")
    descriptor = None
    for klass in smc::ParamDecl.__mro__:
        if "btype" in klass.__dict__:
            descriptor = klass.__dict__["btype"]
            break
    assert isinstance(descriptor, property)



def test_smc::variableassignment_is_not_abstract():
    assert not inspect.isabstract(smc::VariableAssignment)


def test_smc::variableassignment_constructor_exists():
    assert callable(smc::VariableAssignment.__init__)


def test_smc::variableassignment_constructor_args():
    sig = inspect.signature(smc::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc::abstractassignment_is_not_abstract():
    assert not inspect.isabstract(smc::AbstractAssignment)


def test_smc::abstractassignment_constructor_exists():
    assert callable(smc::AbstractAssignment.__init__)


def test_smc::abstractassignment_constructor_args():
    sig = inspect.signature(smc::AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc::variabledecl_is_not_abstract():
    assert not inspect.isabstract(smc::VariableDecl)


def test_smc::variabledecl_constructor_exists():
    assert callable(smc::VariableDecl.__init__)


def test_smc::variabledecl_constructor_args():
    sig = inspect.signature(smc::VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "type" in params, "Missing parameter 'type'"
    assert "array" in params, "Missing parameter 'array'"
    assert "length" in params, "Missing parameter 'length'"

def test_smc::variabledecl_has_name():
    assert hasattr(smc::VariableDecl, "name")
    descriptor = None
    for klass in smc::VariableDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc::variabledecl_has_visibility():
    assert hasattr(smc::VariableDecl, "visibility")
    descriptor = None
    for klass in smc::VariableDecl.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_smc::variabledecl_has_type():
    assert hasattr(smc::VariableDecl, "type")
    descriptor = None
    for klass in smc::VariableDecl.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_smc::variabledecl_has_array():
    assert hasattr(smc::VariableDecl, "array")
    descriptor = None
    for klass in smc::VariableDecl.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_smc::variabledecl_has_length():
    assert hasattr(smc::VariableDecl, "length")
    descriptor = None
    for klass in smc::VariableDecl.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_smc::smc_is_not_abstract():
    assert not inspect.isabstract(smc::Smc)


def test_smc::smc_constructor_exists():
    assert callable(smc::Smc.__init__)


def test_smc::smc_constructor_args():
    sig = inspect.signature(smc::Smc.__init__)
    params = list(sig.parameters.keys())



def test_smc::command_is_not_abstract():
    assert not inspect.isabstract(smc::Command)


def test_smc::command_constructor_exists():
    assert callable(smc::Command.__init__)


def test_smc::command_constructor_args():
    sig = inspect.signature(smc::Command.__init__)
    params = list(sig.parameters.keys())



def test_smc::mainsmc_is_not_abstract():
    assert not inspect.isabstract(smc::MainSMC)


def test_smc::mainsmc_constructor_exists():
    assert callable(smc::MainSMC.__init__)


def test_smc::mainsmc_constructor_args():
    sig = inspect.signature(smc::MainSMC.__init__)
    params = list(sig.parameters.keys())



def test_smc::blocksmc_is_not_abstract():
    assert not inspect.isabstract(smc::BlockSMC)


def test_smc::blocksmc_constructor_exists():
    assert callable(smc::BlockSMC.__init__)


def test_smc::blocksmc_constructor_args():
    sig = inspect.signature(smc::BlockSMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_smc::blocksmc_has_name():
    assert hasattr(smc::BlockSMC, "name")
    descriptor = None
    for klass in smc::BlockSMC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc::blocksmc_has_type():
    assert hasattr(smc::BlockSMC, "type")
    descriptor = None
    for klass in smc::BlockSMC.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sectype_exists():
    # Check that the Enumeration exists
    assert SecType is not None

def test_sectype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SecType]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SecType"

def test_blocktype_exists():
    # Check that the Enumeration exists
    assert BlockType is not None

def test_blocktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockType]
    expected_literals = [
        "COMP",
        "ANONYMIZATION",
        "INSERT",
        "ACCESS",
        "PERMISSION",
        "SEARCH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockType"

def test_basictype_exists():
    # Check that the Enumeration exists
    assert BasicType is not None

def test_basictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicType]
    expected_literals = [
        "STRING",
        "BOOLEAN",
        "ENCRYPTED",
        "DOUBLE",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicType"


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
AccessControl_strategy = st.builds(
    AccessControl,
)
smc::Covered_strategy = st.builds(
    smc::Covered,
)
smc::BellLapadula_strategy = st.builds(
    smc::BellLapadula,
    mode=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
smc::Dict_strategy = st.builds(
    smc::Dict,
)
smc::Not_strategy = st.builds(
    smc::Not,
)
smc::IntLiteral_strategy = st.builds(
    smc::IntLiteral,
    value=
        st.integers()
)
smc::StringLiteral_strategy = st.builds(
    smc::StringLiteral,
    value=
        safe_text
)
smc::MulOrDiv_strategy = st.builds(
    smc::MulOrDiv,
    op=
        safe_text
)
smc::DoubleLiteral_strategy = st.builds(
    smc::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smc::DateLiteral_strategy = st.builds(
    smc::DateLiteral,
    value=
        safe_text
)
smc::Equality_strategy = st.builds(
    smc::Equality,
    op=
        safe_text
)
smc::PlusOrMinus_strategy = st.builds(
    smc::PlusOrMinus,
    op=
        safe_text
)
smc::And_strategy = st.builds(
    smc::And,
)
smc::Or_strategy = st.builds(
    smc::Or,
)
smc::Comparison_strategy = st.builds(
    smc::Comparison,
    op=
        safe_text
)
smc::BooleanLiteral_strategy = st.builds(
    smc::BooleanLiteral,
    value=
        st.booleans()
)
smc::List_strategy = st.builds(
    smc::List,
)
smc::TimeLiteral_strategy = st.builds(
    smc::TimeLiteral,
    value=
        safe_text
)
smc::VariableRef_strategy = st.builds(
    smc::VariableRef,
)
smc::Tuple_strategy = st.builds(
    smc::Tuple,
)
Download_strategy = st.builds(
    Download,
)
smc::Client_strategy = st.builds(
    smc::Client,
    arg=
        safe_text
)
smc::Database_strategy = st.builds(
    smc::Database,
    clm=
        safe_text
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
smc::Download_strategy = st.builds(
    smc::Download,
)
Computation_strategy = st.builds(
    Computation,
)
smc::Median_strategy = st.builds(
    smc::Median,
)
smc::Count_strategy = st.builds(
    smc::Count,
)
smc::WeightedAvg_strategy = st.builds(
    smc::WeightedAvg,
)
smc::Average_strategy = st.builds(
    smc::Average,
)
smc::Multiplication_strategy = st.builds(
    smc::Multiplication,
)
Functions_strategy = st.builds(
    Functions,
)
smc::AddValues_strategy = st.builds(
    smc::AddValues,
)
smc::BloomFilter_strategy = st.builds(
    smc::BloomFilter,
)
smc::Search_strategy = st.builds(
    smc::Search,
    column=
        safe_text
)
smc::CreateTable_strategy = st.builds(
    smc::CreateTable,
)
smc::AccessControl_strategy = st.builds(
    smc::AccessControl,
)
smc::CheckTable_strategy = st.builds(
    smc::CheckTable,
)
smc::Computation_strategy = st.builds(
    smc::Computation,
)
smc::Functions_strategy = st.builds(
    smc::Functions,
)
smc::Expression_strategy = st.builds(
    smc::Expression,
)
smc::Invocation_strategy = st.builds(
    smc::Invocation,
)
Command_strategy = st.builds(
    Command,
)
smc::IfThenElse_strategy = st.builds(
    smc::IfThenElse,
)
smc::Return_strategy = st.builds(
    smc::Return,
)
smc::While_strategy = st.builds(
    smc::While,
)
smc::InvocationVoid_strategy = st.builds(
    smc::InvocationVoid,
)
smc::Block_strategy = st.builds(
    smc::Block,
)
smc::Print_strategy = st.builds(
    smc::Print,
)
smc::ParamDecl_strategy = st.builds(
    smc::ParamDecl,
    stype=
        safe_text,
    parName=
        safe_text,
    name=
        safe_text,
    btype=
        safe_text
)
smc::VariableAssignment_strategy = st.builds(
    smc::VariableAssignment,
)
smc::AbstractAssignment_strategy = st.builds(
    smc::AbstractAssignment,
)
smc::VariableDecl_strategy = st.builds(
    smc::VariableDecl,
    name=
        safe_text,
    visibility=
        safe_text,
    type=
        safe_text,
    array=
        st.booleans(),
    length=
        st.integers()
)
smc::Smc_strategy = st.builds(
    smc::Smc,
)
smc::Command_strategy = st.builds(
    smc::Command,
)
smc::MainSMC_strategy = st.builds(
    smc::MainSMC,
)
smc::BlockSMC_strategy = st.builds(
    smc::BlockSMC,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=AccessControl_strategy)
@settings(max_examples=50)
def test_accesscontrol_instantiation(instance):
    assert isinstance(instance, AccessControl)

@given(instance=smc::Covered_strategy)
@settings(max_examples=50)
def test_smc::covered_instantiation(instance):
    assert isinstance(instance, smc::Covered)

@given(instance=smc::BellLapadula_strategy)
@settings(max_examples=50)
def test_smc::belllapadula_instantiation(instance):
    assert isinstance(instance, smc::BellLapadula)

@given(instance=smc::BellLapadula_strategy)
def test_smc::belllapadula_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=smc::BellLapadula_strategy)
def test_smc::belllapadula_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=smc::Dict_strategy)
@settings(max_examples=50)
def test_smc::dict_instantiation(instance):
    assert isinstance(instance, smc::Dict)

@given(instance=smc::Not_strategy)
@settings(max_examples=50)
def test_smc::not_instantiation(instance):
    assert isinstance(instance, smc::Not)

@given(instance=smc::IntLiteral_strategy)
@settings(max_examples=50)
def test_smc::intliteral_instantiation(instance):
    assert isinstance(instance, smc::IntLiteral)

@given(instance=smc::IntLiteral_strategy)
def test_smc::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=smc::IntLiteral_strategy)
def test_smc::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::StringLiteral_strategy)
@settings(max_examples=50)
def test_smc::stringliteral_instantiation(instance):
    assert isinstance(instance, smc::StringLiteral)

@given(instance=smc::StringLiteral_strategy)
def test_smc::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smc::StringLiteral_strategy)
def test_smc::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::MulOrDiv_strategy)
@settings(max_examples=50)
def test_smc::mulordiv_instantiation(instance):
    assert isinstance(instance, smc::MulOrDiv)

@given(instance=smc::MulOrDiv_strategy)
def test_smc::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=smc::MulOrDiv_strategy)
def test_smc::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_smc::doubleliteral_instantiation(instance):
    assert isinstance(instance, smc::DoubleLiteral)

@given(instance=smc::DoubleLiteral_strategy)
def test_smc::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=smc::DoubleLiteral_strategy)
def test_smc::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::DateLiteral_strategy)
@settings(max_examples=50)
def test_smc::dateliteral_instantiation(instance):
    assert isinstance(instance, smc::DateLiteral)

@given(instance=smc::DateLiteral_strategy)
def test_smc::dateliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smc::DateLiteral_strategy)
def test_smc::dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::Equality_strategy)
@settings(max_examples=50)
def test_smc::equality_instantiation(instance):
    assert isinstance(instance, smc::Equality)

@given(instance=smc::Equality_strategy)
def test_smc::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=smc::Equality_strategy)
def test_smc::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc::PlusOrMinus_strategy)
@settings(max_examples=50)
def test_smc::plusorminus_instantiation(instance):
    assert isinstance(instance, smc::PlusOrMinus)

@given(instance=smc::PlusOrMinus_strategy)
def test_smc::plusorminus_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=smc::PlusOrMinus_strategy)
def test_smc::plusorminus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc::And_strategy)
@settings(max_examples=50)
def test_smc::and_instantiation(instance):
    assert isinstance(instance, smc::And)

@given(instance=smc::Or_strategy)
@settings(max_examples=50)
def test_smc::or_instantiation(instance):
    assert isinstance(instance, smc::Or)

@given(instance=smc::Comparison_strategy)
@settings(max_examples=50)
def test_smc::comparison_instantiation(instance):
    assert isinstance(instance, smc::Comparison)

@given(instance=smc::Comparison_strategy)
def test_smc::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=smc::Comparison_strategy)
def test_smc::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_smc::booleanliteral_instantiation(instance):
    assert isinstance(instance, smc::BooleanLiteral)

@given(instance=smc::BooleanLiteral_strategy)
def test_smc::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=smc::BooleanLiteral_strategy)
def test_smc::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::List_strategy)
@settings(max_examples=50)
def test_smc::list_instantiation(instance):
    assert isinstance(instance, smc::List)

@given(instance=smc::TimeLiteral_strategy)
@settings(max_examples=50)
def test_smc::timeliteral_instantiation(instance):
    assert isinstance(instance, smc::TimeLiteral)

@given(instance=smc::TimeLiteral_strategy)
def test_smc::timeliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smc::TimeLiteral_strategy)
def test_smc::timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc::VariableRef_strategy)
@settings(max_examples=50)
def test_smc::variableref_instantiation(instance):
    assert isinstance(instance, smc::VariableRef)

@given(instance=smc::Tuple_strategy)
@settings(max_examples=50)
def test_smc::tuple_instantiation(instance):
    assert isinstance(instance, smc::Tuple)

@given(instance=Download_strategy)
@settings(max_examples=50)
def test_download_instantiation(instance):
    assert isinstance(instance, Download)

@given(instance=smc::Client_strategy)
@settings(max_examples=50)
def test_smc::client_instantiation(instance):
    assert isinstance(instance, smc::Client)

@given(instance=smc::Client_strategy)
def test_smc::client_arg_type(instance):
    assert isinstance(instance.arg, str)


@given(instance=smc::Client_strategy)
def test_smc::client_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original

@given(instance=smc::Database_strategy)
@settings(max_examples=50)
def test_smc::database_instantiation(instance):
    assert isinstance(instance, smc::Database)

@given(instance=smc::Database_strategy)
def test_smc::database_clm_type(instance):
    assert isinstance(instance.clm, str)


@given(instance=smc::Database_strategy)
def test_smc::database_clm_setter(instance):
    original = instance.clm
    instance.clm = original
    assert instance.clm == original

@given(instance=AbstractAssignment_strategy)
@settings(max_examples=50)
def test_abstractassignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)

@given(instance=smc::Download_strategy)
@settings(max_examples=50)
def test_smc::download_instantiation(instance):
    assert isinstance(instance, smc::Download)

@given(instance=Computation_strategy)
@settings(max_examples=50)
def test_computation_instantiation(instance):
    assert isinstance(instance, Computation)

@given(instance=smc::Median_strategy)
@settings(max_examples=50)
def test_smc::median_instantiation(instance):
    assert isinstance(instance, smc::Median)

@given(instance=smc::Count_strategy)
@settings(max_examples=50)
def test_smc::count_instantiation(instance):
    assert isinstance(instance, smc::Count)

@given(instance=smc::WeightedAvg_strategy)
@settings(max_examples=50)
def test_smc::weightedavg_instantiation(instance):
    assert isinstance(instance, smc::WeightedAvg)

@given(instance=smc::Average_strategy)
@settings(max_examples=50)
def test_smc::average_instantiation(instance):
    assert isinstance(instance, smc::Average)

@given(instance=smc::Multiplication_strategy)
@settings(max_examples=50)
def test_smc::multiplication_instantiation(instance):
    assert isinstance(instance, smc::Multiplication)

@given(instance=Functions_strategy)
@settings(max_examples=50)
def test_functions_instantiation(instance):
    assert isinstance(instance, Functions)

@given(instance=smc::AddValues_strategy)
@settings(max_examples=50)
def test_smc::addvalues_instantiation(instance):
    assert isinstance(instance, smc::AddValues)

@given(instance=smc::BloomFilter_strategy)
@settings(max_examples=50)
def test_smc::bloomfilter_instantiation(instance):
    assert isinstance(instance, smc::BloomFilter)

@given(instance=smc::Search_strategy)
@settings(max_examples=50)
def test_smc::search_instantiation(instance):
    assert isinstance(instance, smc::Search)

@given(instance=smc::Search_strategy)
def test_smc::search_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=smc::Search_strategy)
def test_smc::search_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=smc::CreateTable_strategy)
@settings(max_examples=50)
def test_smc::createtable_instantiation(instance):
    assert isinstance(instance, smc::CreateTable)

@given(instance=smc::AccessControl_strategy)
@settings(max_examples=50)
def test_smc::accesscontrol_instantiation(instance):
    assert isinstance(instance, smc::AccessControl)

@given(instance=smc::CheckTable_strategy)
@settings(max_examples=50)
def test_smc::checktable_instantiation(instance):
    assert isinstance(instance, smc::CheckTable)

@given(instance=smc::Computation_strategy)
@settings(max_examples=50)
def test_smc::computation_instantiation(instance):
    assert isinstance(instance, smc::Computation)

@given(instance=smc::Functions_strategy)
@settings(max_examples=50)
def test_smc::functions_instantiation(instance):
    assert isinstance(instance, smc::Functions)

@given(instance=smc::Expression_strategy)
@settings(max_examples=50)
def test_smc::expression_instantiation(instance):
    assert isinstance(instance, smc::Expression)

@given(instance=smc::Invocation_strategy)
@settings(max_examples=50)
def test_smc::invocation_instantiation(instance):
    assert isinstance(instance, smc::Invocation)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=smc::IfThenElse_strategy)
@settings(max_examples=50)
def test_smc::ifthenelse_instantiation(instance):
    assert isinstance(instance, smc::IfThenElse)

@given(instance=smc::Return_strategy)
@settings(max_examples=50)
def test_smc::return_instantiation(instance):
    assert isinstance(instance, smc::Return)

@given(instance=smc::While_strategy)
@settings(max_examples=50)
def test_smc::while_instantiation(instance):
    assert isinstance(instance, smc::While)

@given(instance=smc::InvocationVoid_strategy)
@settings(max_examples=50)
def test_smc::invocationvoid_instantiation(instance):
    assert isinstance(instance, smc::InvocationVoid)

@given(instance=smc::Block_strategy)
@settings(max_examples=50)
def test_smc::block_instantiation(instance):
    assert isinstance(instance, smc::Block)

@given(instance=smc::Print_strategy)
@settings(max_examples=50)
def test_smc::print_instantiation(instance):
    assert isinstance(instance, smc::Print)

@given(instance=smc::ParamDecl_strategy)
@settings(max_examples=50)
def test_smc::paramdecl_instantiation(instance):
    assert isinstance(instance, smc::ParamDecl)

@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_stype_type(instance):
    assert isinstance(instance.stype, str)


@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_stype_setter(instance):
    original = instance.stype
    instance.stype = original
    assert instance.stype == original

@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_parName_type(instance):
    assert isinstance(instance.parName, str)


@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_parName_setter(instance):
    original = instance.parName
    instance.parName = original
    assert instance.parName == original

@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_btype_type(instance):
    assert isinstance(instance.btype, str)


@given(instance=smc::ParamDecl_strategy)
def test_smc::paramdecl_btype_setter(instance):
    original = instance.btype
    instance.btype = original
    assert instance.btype == original

@given(instance=smc::VariableAssignment_strategy)
@settings(max_examples=50)
def test_smc::variableassignment_instantiation(instance):
    assert isinstance(instance, smc::VariableAssignment)

@given(instance=smc::AbstractAssignment_strategy)
@settings(max_examples=50)
def test_smc::abstractassignment_instantiation(instance):
    assert isinstance(instance, smc::AbstractAssignment)

@given(instance=smc::VariableDecl_strategy)
@settings(max_examples=50)
def test_smc::variabledecl_instantiation(instance):
    assert isinstance(instance, smc::VariableDecl)

@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=smc::VariableDecl_strategy)
def test_smc::variabledecl_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=smc::Smc_strategy)
@settings(max_examples=50)
def test_smc::smc_instantiation(instance):
    assert isinstance(instance, smc::Smc)

@given(instance=smc::Command_strategy)
@settings(max_examples=50)
def test_smc::command_instantiation(instance):
    assert isinstance(instance, smc::Command)

@given(instance=smc::MainSMC_strategy)
@settings(max_examples=50)
def test_smc::mainsmc_instantiation(instance):
    assert isinstance(instance, smc::MainSMC)

@given(instance=smc::BlockSMC_strategy)
@settings(max_examples=50)
def test_smc::blocksmc_instantiation(instance):
    assert isinstance(instance, smc::BlockSMC)

@given(instance=smc::BlockSMC_strategy)
def test_smc::blocksmc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smc::BlockSMC_strategy)
def test_smc::blocksmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smc::BlockSMC_strategy)
def test_smc::blocksmc_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=smc::BlockSMC_strategy)
def test_smc::blocksmc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
