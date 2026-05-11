import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BasicType,
    fiacre::NatType,
    fiacre::IntType,
    fiacre::BoolType,
    Type,
    fiacre::BasicType,
    InlineCollection,
    fiacre::InlineQueue,
    fiacre::Variable,
    fiacre::MaxBound,
    fiacre::MinBound,
    Exp,
    fiacre::ArrayElem,
    fiacre::BinExp,
    fiacre::RecordElem,
    fiacre::UnExp,
    fiacre::Pattern,
    fiacre::SingleAssignment,
    Assignment,
    fiacre::NonDeterministicAssignment,
    fiacre::DeterministicAssignment,
    fiacre::InterfacedComp,
    Composition,
    fiacre::Instance,
    fiacre::Par,
    Statement,
    fiacre::To,
    fiacre::Select,
    fiacre::Assignment,
    fiacre::Wait,
    fiacre::Communication,
    fiacre::WhileStmt,
    fiacre::IfStmt,
    fiacre::NullStmt,
    Arg,
    fiacre::Exp,
    fiacre::Arg,
    Declaration,
    fiacre::NodeDecl,
    fiacre::Declaration,
    Variable,
    fiacre::ArgumentVariable,
    fiacre::PortDecl,
    fiacre::Transition,
    fiacre::State,
    fiacre::Priority,
    fiacre::Composition,
    NodeDecl,
    fiacre::ProcessDecl,
    fiacre::ComponentDecl,
    fiacre::Channel,
    fiacre::ChannelDecl,
    fiacre::Type,
    fiacre::TypeDecl,
    fiacre::Statement,
    fiacre::LocalVariable,
    fiacre::Program,
    fiacre::InlineCollection,
    fiacre::Foreach,
    fiacre::CondExp,
    MaxBound,
    fiacre::InfiniteBound,
    MinBound,
    fiacre::FiniteBound,
    fiacre::LabeledType,
    fiacre::Union,
    fiacre::ConstrExp,
    fiacre::ConstantDecl,
    fiacre::RefArg,
    fiacre::Rule,
    fiacre::CaseStmt,
    Channel,
    fiacre::Profile,
    fiacre::TypeId,
    PortDecl,
    fiacre::ParamPortDecl,
    fiacre::LocalPortDecl,
    fiacre::Seq,
    Communication,
    fiacre::Emission,
    fiacre::Reception,
    fiacre::Synchronization,
    fiacre::ValuedField,
    fiacre::InlineRecord,
    fiacre::InlineArray,
    Pattern,
    fiacre::Literal,
    fiacre::ConstrPattern,
    fiacre::AnyPattern,
    fiacre::ConstantRef,
    fiacre::ArrayPattern,
    fiacre::FieldPattern,
    fiacre::VarRef,
    Literal,
    fiacre::BoolLiteral,
    fiacre::NatLiteral,
    fiacre::Queue,
    fiacre::Array,
    LabeledType,
    fiacre::Constr,
    fiacre::Field,
    fiacre::Record,
    fiacre::Interval,
    BinOp,
    UnOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basictype_is_not_abstract():
    assert not inspect.isabstract(BasicType)


def test_basictype_constructor_exists():
    assert callable(BasicType.__init__)


def test_basictype_constructor_args():
    sig = inspect.signature(BasicType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::nattype_is_not_abstract():
    assert not inspect.isabstract(fiacre::NatType)


def test_fiacre::nattype_constructor_exists():
    assert callable(fiacre::NatType.__init__)


def test_fiacre::nattype_constructor_args():
    sig = inspect.signature(fiacre::NatType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::inttype_is_not_abstract():
    assert not inspect.isabstract(fiacre::IntType)


def test_fiacre::inttype_constructor_exists():
    assert callable(fiacre::IntType.__init__)


def test_fiacre::inttype_constructor_args():
    sig = inspect.signature(fiacre::IntType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::booltype_is_not_abstract():
    assert not inspect.isabstract(fiacre::BoolType)


def test_fiacre::booltype_constructor_exists():
    assert callable(fiacre::BoolType.__init__)


def test_fiacre::booltype_constructor_args():
    sig = inspect.signature(fiacre::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::basictype_is_not_abstract():
    assert not inspect.isabstract(fiacre::BasicType)


def test_fiacre::basictype_constructor_exists():
    assert callable(fiacre::BasicType.__init__)


def test_fiacre::basictype_constructor_args():
    sig = inspect.signature(fiacre::BasicType.__init__)
    params = list(sig.parameters.keys())



def test_inlinecollection_is_not_abstract():
    assert not inspect.isabstract(InlineCollection)


def test_inlinecollection_constructor_exists():
    assert callable(InlineCollection.__init__)


def test_inlinecollection_constructor_args():
    sig = inspect.signature(InlineCollection.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::inlinequeue_is_not_abstract():
    assert not inspect.isabstract(fiacre::InlineQueue)


def test_fiacre::inlinequeue_constructor_exists():
    assert callable(fiacre::InlineQueue.__init__)


def test_fiacre::inlinequeue_constructor_args():
    sig = inspect.signature(fiacre::InlineQueue.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::variable_is_not_abstract():
    assert not inspect.isabstract(fiacre::Variable)


def test_fiacre::variable_constructor_exists():
    assert callable(fiacre::Variable.__init__)


def test_fiacre::variable_constructor_args():
    sig = inspect.signature(fiacre::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::variable_has_name():
    assert hasattr(fiacre::Variable, "name")
    descriptor = None
    for klass in fiacre::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::maxbound_is_not_abstract():
    assert not inspect.isabstract(fiacre::MaxBound)


def test_fiacre::maxbound_constructor_exists():
    assert callable(fiacre::MaxBound.__init__)


def test_fiacre::maxbound_constructor_args():
    sig = inspect.signature(fiacre::MaxBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::minbound_is_not_abstract():
    assert not inspect.isabstract(fiacre::MinBound)


def test_fiacre::minbound_constructor_exists():
    assert callable(fiacre::MinBound.__init__)


def test_fiacre::minbound_constructor_args():
    sig = inspect.signature(fiacre::MinBound.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::arrayelem_is_not_abstract():
    assert not inspect.isabstract(fiacre::ArrayElem)


def test_fiacre::arrayelem_constructor_exists():
    assert callable(fiacre::ArrayElem.__init__)


def test_fiacre::arrayelem_constructor_args():
    sig = inspect.signature(fiacre::ArrayElem.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::binexp_is_not_abstract():
    assert not inspect.isabstract(fiacre::BinExp)


def test_fiacre::binexp_constructor_exists():
    assert callable(fiacre::BinExp.__init__)


def test_fiacre::binexp_constructor_args():
    sig = inspect.signature(fiacre::BinExp.__init__)
    params = list(sig.parameters.keys())
    assert "binOp" in params, "Missing parameter 'binOp'"

def test_fiacre::binexp_has_binOp():
    assert hasattr(fiacre::BinExp, "binOp")
    descriptor = None
    for klass in fiacre::BinExp.__mro__:
        if "binOp" in klass.__dict__:
            descriptor = klass.__dict__["binOp"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::recordelem_is_not_abstract():
    assert not inspect.isabstract(fiacre::RecordElem)


def test_fiacre::recordelem_constructor_exists():
    assert callable(fiacre::RecordElem.__init__)


def test_fiacre::recordelem_constructor_args():
    sig = inspect.signature(fiacre::RecordElem.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre::recordelem_has_field():
    assert hasattr(fiacre::RecordElem, "field")
    descriptor = None
    for klass in fiacre::RecordElem.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::unexp_is_not_abstract():
    assert not inspect.isabstract(fiacre::UnExp)


def test_fiacre::unexp_constructor_exists():
    assert callable(fiacre::UnExp.__init__)


def test_fiacre::unexp_constructor_args():
    sig = inspect.signature(fiacre::UnExp.__init__)
    params = list(sig.parameters.keys())
    assert "unop" in params, "Missing parameter 'unop'"

def test_fiacre::unexp_has_unop():
    assert hasattr(fiacre::UnExp, "unop")
    descriptor = None
    for klass in fiacre::UnExp.__mro__:
        if "unop" in klass.__dict__:
            descriptor = klass.__dict__["unop"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::pattern_is_not_abstract():
    assert not inspect.isabstract(fiacre::Pattern)


def test_fiacre::pattern_constructor_exists():
    assert callable(fiacre::Pattern.__init__)


def test_fiacre::pattern_constructor_args():
    sig = inspect.signature(fiacre::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::singleassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre::SingleAssignment)


def test_fiacre::singleassignment_constructor_exists():
    assert callable(fiacre::SingleAssignment.__init__)


def test_fiacre::singleassignment_constructor_args():
    sig = inspect.signature(fiacre::SingleAssignment.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::nondeterministicassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre::NonDeterministicAssignment)


def test_fiacre::nondeterministicassignment_constructor_exists():
    assert callable(fiacre::NonDeterministicAssignment.__init__)


def test_fiacre::nondeterministicassignment_constructor_args():
    sig = inspect.signature(fiacre::NonDeterministicAssignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::deterministicassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre::DeterministicAssignment)


def test_fiacre::deterministicassignment_constructor_exists():
    assert callable(fiacre::DeterministicAssignment.__init__)


def test_fiacre::deterministicassignment_constructor_args():
    sig = inspect.signature(fiacre::DeterministicAssignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::interfacedcomp_is_not_abstract():
    assert not inspect.isabstract(fiacre::InterfacedComp)


def test_fiacre::interfacedcomp_constructor_exists():
    assert callable(fiacre::InterfacedComp.__init__)


def test_fiacre::interfacedcomp_constructor_args():
    sig = inspect.signature(fiacre::InterfacedComp.__init__)
    params = list(sig.parameters.keys())



def test_composition_is_not_abstract():
    assert not inspect.isabstract(Composition)


def test_composition_constructor_exists():
    assert callable(Composition.__init__)


def test_composition_constructor_args():
    sig = inspect.signature(Composition.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::instance_is_not_abstract():
    assert not inspect.isabstract(fiacre::Instance)


def test_fiacre::instance_constructor_exists():
    assert callable(fiacre::Instance.__init__)


def test_fiacre::instance_constructor_args():
    sig = inspect.signature(fiacre::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::instance_has_name():
    assert hasattr(fiacre::Instance, "name")
    descriptor = None
    for klass in fiacre::Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::par_is_not_abstract():
    assert not inspect.isabstract(fiacre::Par)


def test_fiacre::par_constructor_exists():
    assert callable(fiacre::Par.__init__)


def test_fiacre::par_constructor_args():
    sig = inspect.signature(fiacre::Par.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::to_is_not_abstract():
    assert not inspect.isabstract(fiacre::To)


def test_fiacre::to_constructor_exists():
    assert callable(fiacre::To.__init__)


def test_fiacre::to_constructor_args():
    sig = inspect.signature(fiacre::To.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::select_is_not_abstract():
    assert not inspect.isabstract(fiacre::Select)


def test_fiacre::select_constructor_exists():
    assert callable(fiacre::Select.__init__)


def test_fiacre::select_constructor_args():
    sig = inspect.signature(fiacre::Select.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::assignment_is_not_abstract():
    assert not inspect.isabstract(fiacre::Assignment)


def test_fiacre::assignment_constructor_exists():
    assert callable(fiacre::Assignment.__init__)


def test_fiacre::assignment_constructor_args():
    sig = inspect.signature(fiacre::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::wait_is_not_abstract():
    assert not inspect.isabstract(fiacre::Wait)


def test_fiacre::wait_constructor_exists():
    assert callable(fiacre::Wait.__init__)


def test_fiacre::wait_constructor_args():
    sig = inspect.signature(fiacre::Wait.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::communication_is_not_abstract():
    assert not inspect.isabstract(fiacre::Communication)


def test_fiacre::communication_constructor_exists():
    assert callable(fiacre::Communication.__init__)


def test_fiacre::communication_constructor_args():
    sig = inspect.signature(fiacre::Communication.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::whilestmt_is_not_abstract():
    assert not inspect.isabstract(fiacre::WhileStmt)


def test_fiacre::whilestmt_constructor_exists():
    assert callable(fiacre::WhileStmt.__init__)


def test_fiacre::whilestmt_constructor_args():
    sig = inspect.signature(fiacre::WhileStmt.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::ifstmt_is_not_abstract():
    assert not inspect.isabstract(fiacre::IfStmt)


def test_fiacre::ifstmt_constructor_exists():
    assert callable(fiacre::IfStmt.__init__)


def test_fiacre::ifstmt_constructor_args():
    sig = inspect.signature(fiacre::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::nullstmt_is_not_abstract():
    assert not inspect.isabstract(fiacre::NullStmt)


def test_fiacre::nullstmt_constructor_exists():
    assert callable(fiacre::NullStmt.__init__)


def test_fiacre::nullstmt_constructor_args():
    sig = inspect.signature(fiacre::NullStmt.__init__)
    params = list(sig.parameters.keys())



def test_arg_is_not_abstract():
    assert not inspect.isabstract(Arg)


def test_arg_constructor_exists():
    assert callable(Arg.__init__)


def test_arg_constructor_args():
    sig = inspect.signature(Arg.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::exp_is_not_abstract():
    assert not inspect.isabstract(fiacre::Exp)


def test_fiacre::exp_constructor_exists():
    assert callable(fiacre::Exp.__init__)


def test_fiacre::exp_constructor_args():
    sig = inspect.signature(fiacre::Exp.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::arg_is_not_abstract():
    assert not inspect.isabstract(fiacre::Arg)


def test_fiacre::arg_constructor_exists():
    assert callable(fiacre::Arg.__init__)


def test_fiacre::arg_constructor_args():
    sig = inspect.signature(fiacre::Arg.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::nodedecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::NodeDecl)


def test_fiacre::nodedecl_constructor_exists():
    assert callable(fiacre::NodeDecl.__init__)


def test_fiacre::nodedecl_constructor_args():
    sig = inspect.signature(fiacre::NodeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::declaration_is_not_abstract():
    assert not inspect.isabstract(fiacre::Declaration)


def test_fiacre::declaration_constructor_exists():
    assert callable(fiacre::Declaration.__init__)


def test_fiacre::declaration_constructor_args():
    sig = inspect.signature(fiacre::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::declaration_has_name():
    assert hasattr(fiacre::Declaration, "name")
    descriptor = None
    for klass in fiacre::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::argumentvariable_is_not_abstract():
    assert not inspect.isabstract(fiacre::ArgumentVariable)


def test_fiacre::argumentvariable_constructor_exists():
    assert callable(fiacre::ArgumentVariable.__init__)


def test_fiacre::argumentvariable_constructor_args():
    sig = inspect.signature(fiacre::ArgumentVariable.__init__)
    params = list(sig.parameters.keys())
    assert "read" in params, "Missing parameter 'read'"
    assert "write" in params, "Missing parameter 'write'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_fiacre::argumentvariable_has_read():
    assert hasattr(fiacre::ArgumentVariable, "read")
    descriptor = None
    for klass in fiacre::ArgumentVariable.__mro__:
        if "read" in klass.__dict__:
            descriptor = klass.__dict__["read"]
            break
    assert isinstance(descriptor, property)

def test_fiacre::argumentvariable_has_write():
    assert hasattr(fiacre::ArgumentVariable, "write")
    descriptor = None
    for klass in fiacre::ArgumentVariable.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)

def test_fiacre::argumentvariable_has_ref():
    assert hasattr(fiacre::ArgumentVariable, "ref")
    descriptor = None
    for klass in fiacre::ArgumentVariable.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::portdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::PortDecl)


def test_fiacre::portdecl_constructor_exists():
    assert callable(fiacre::PortDecl.__init__)


def test_fiacre::portdecl_constructor_args():
    sig = inspect.signature(fiacre::PortDecl.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "name" in params, "Missing parameter 'name'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_fiacre::portdecl_has_out():
    assert hasattr(fiacre::PortDecl, "out")
    descriptor = None
    for klass in fiacre::PortDecl.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_fiacre::portdecl_has_name():
    assert hasattr(fiacre::PortDecl, "name")
    descriptor = None
    for klass in fiacre::PortDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fiacre::portdecl_has_in_():
    assert hasattr(fiacre::PortDecl, "in_")
    descriptor = None
    for klass in fiacre::PortDecl.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::transition_is_not_abstract():
    assert not inspect.isabstract(fiacre::Transition)


def test_fiacre::transition_constructor_exists():
    assert callable(fiacre::Transition.__init__)


def test_fiacre::transition_constructor_args():
    sig = inspect.signature(fiacre::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::transition_has_name():
    assert hasattr(fiacre::Transition, "name")
    descriptor = None
    for klass in fiacre::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::state_is_not_abstract():
    assert not inspect.isabstract(fiacre::State)


def test_fiacre::state_constructor_exists():
    assert callable(fiacre::State.__init__)


def test_fiacre::state_constructor_args():
    sig = inspect.signature(fiacre::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::state_has_name():
    assert hasattr(fiacre::State, "name")
    descriptor = None
    for klass in fiacre::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::priority_is_not_abstract():
    assert not inspect.isabstract(fiacre::Priority)


def test_fiacre::priority_constructor_exists():
    assert callable(fiacre::Priority.__init__)


def test_fiacre::priority_constructor_args():
    sig = inspect.signature(fiacre::Priority.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::composition_is_not_abstract():
    assert not inspect.isabstract(fiacre::Composition)


def test_fiacre::composition_constructor_exists():
    assert callable(fiacre::Composition.__init__)


def test_fiacre::composition_constructor_args():
    sig = inspect.signature(fiacre::Composition.__init__)
    params = list(sig.parameters.keys())



def test_nodedecl_is_not_abstract():
    assert not inspect.isabstract(NodeDecl)


def test_nodedecl_constructor_exists():
    assert callable(NodeDecl.__init__)


def test_nodedecl_constructor_args():
    sig = inspect.signature(NodeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::processdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::ProcessDecl)


def test_fiacre::processdecl_constructor_exists():
    assert callable(fiacre::ProcessDecl.__init__)


def test_fiacre::processdecl_constructor_args():
    sig = inspect.signature(fiacre::ProcessDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::componentdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::ComponentDecl)


def test_fiacre::componentdecl_constructor_exists():
    assert callable(fiacre::ComponentDecl.__init__)


def test_fiacre::componentdecl_constructor_args():
    sig = inspect.signature(fiacre::ComponentDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::channel_is_not_abstract():
    assert not inspect.isabstract(fiacre::Channel)


def test_fiacre::channel_constructor_exists():
    assert callable(fiacre::Channel.__init__)


def test_fiacre::channel_constructor_args():
    sig = inspect.signature(fiacre::Channel.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::channeldecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::ChannelDecl)


def test_fiacre::channeldecl_constructor_exists():
    assert callable(fiacre::ChannelDecl.__init__)


def test_fiacre::channeldecl_constructor_args():
    sig = inspect.signature(fiacre::ChannelDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::type_is_not_abstract():
    assert not inspect.isabstract(fiacre::Type)


def test_fiacre::type_constructor_exists():
    assert callable(fiacre::Type.__init__)


def test_fiacre::type_constructor_args():
    sig = inspect.signature(fiacre::Type.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::typedecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::TypeDecl)


def test_fiacre::typedecl_constructor_exists():
    assert callable(fiacre::TypeDecl.__init__)


def test_fiacre::typedecl_constructor_args():
    sig = inspect.signature(fiacre::TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::statement_is_not_abstract():
    assert not inspect.isabstract(fiacre::Statement)


def test_fiacre::statement_constructor_exists():
    assert callable(fiacre::Statement.__init__)


def test_fiacre::statement_constructor_args():
    sig = inspect.signature(fiacre::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_fiacre::statement_has_comment():
    assert hasattr(fiacre::Statement, "comment")
    descriptor = None
    for klass in fiacre::Statement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::localvariable_is_not_abstract():
    assert not inspect.isabstract(fiacre::LocalVariable)


def test_fiacre::localvariable_constructor_exists():
    assert callable(fiacre::LocalVariable.__init__)


def test_fiacre::localvariable_constructor_args():
    sig = inspect.signature(fiacre::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_fiacre::localvariable_has_constant():
    assert hasattr(fiacre::LocalVariable, "constant")
    descriptor = None
    for klass in fiacre::LocalVariable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::program_is_not_abstract():
    assert not inspect.isabstract(fiacre::Program)


def test_fiacre::program_constructor_exists():
    assert callable(fiacre::Program.__init__)


def test_fiacre::program_constructor_args():
    sig = inspect.signature(fiacre::Program.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::inlinecollection_is_not_abstract():
    assert not inspect.isabstract(fiacre::InlineCollection)


def test_fiacre::inlinecollection_constructor_exists():
    assert callable(fiacre::InlineCollection.__init__)


def test_fiacre::inlinecollection_constructor_args():
    sig = inspect.signature(fiacre::InlineCollection.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::foreach_is_not_abstract():
    assert not inspect.isabstract(fiacre::Foreach)


def test_fiacre::foreach_constructor_exists():
    assert callable(fiacre::Foreach.__init__)


def test_fiacre::foreach_constructor_args():
    sig = inspect.signature(fiacre::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::condexp_is_not_abstract():
    assert not inspect.isabstract(fiacre::CondExp)


def test_fiacre::condexp_constructor_exists():
    assert callable(fiacre::CondExp.__init__)


def test_fiacre::condexp_constructor_args():
    sig = inspect.signature(fiacre::CondExp.__init__)
    params = list(sig.parameters.keys())



def test_maxbound_is_not_abstract():
    assert not inspect.isabstract(MaxBound)


def test_maxbound_constructor_exists():
    assert callable(MaxBound.__init__)


def test_maxbound_constructor_args():
    sig = inspect.signature(MaxBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::infinitebound_is_not_abstract():
    assert not inspect.isabstract(fiacre::InfiniteBound)


def test_fiacre::infinitebound_constructor_exists():
    assert callable(fiacre::InfiniteBound.__init__)


def test_fiacre::infinitebound_constructor_args():
    sig = inspect.signature(fiacre::InfiniteBound.__init__)
    params = list(sig.parameters.keys())



def test_minbound_is_not_abstract():
    assert not inspect.isabstract(MinBound)


def test_minbound_constructor_exists():
    assert callable(MinBound.__init__)


def test_minbound_constructor_args():
    sig = inspect.signature(MinBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::finitebound_is_not_abstract():
    assert not inspect.isabstract(fiacre::FiniteBound)


def test_fiacre::finitebound_constructor_exists():
    assert callable(fiacre::FiniteBound.__init__)


def test_fiacre::finitebound_constructor_args():
    sig = inspect.signature(fiacre::FiniteBound.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "val" in params, "Missing parameter 'val'"

def test_fiacre::finitebound_has_strict():
    assert hasattr(fiacre::FiniteBound, "strict")
    descriptor = None
    for klass in fiacre::FiniteBound.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_fiacre::finitebound_has_val():
    assert hasattr(fiacre::FiniteBound, "val")
    descriptor = None
    for klass in fiacre::FiniteBound.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::labeledtype_is_not_abstract():
    assert not inspect.isabstract(fiacre::LabeledType)


def test_fiacre::labeledtype_constructor_exists():
    assert callable(fiacre::LabeledType.__init__)


def test_fiacre::labeledtype_constructor_args():
    sig = inspect.signature(fiacre::LabeledType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::labeledtype_has_name():
    assert hasattr(fiacre::LabeledType, "name")
    descriptor = None
    for klass in fiacre::LabeledType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::union_is_not_abstract():
    assert not inspect.isabstract(fiacre::Union)


def test_fiacre::union_constructor_exists():
    assert callable(fiacre::Union.__init__)


def test_fiacre::union_constructor_args():
    sig = inspect.signature(fiacre::Union.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::constrexp_is_not_abstract():
    assert not inspect.isabstract(fiacre::ConstrExp)


def test_fiacre::constrexp_constructor_exists():
    assert callable(fiacre::ConstrExp.__init__)


def test_fiacre::constrexp_constructor_args():
    sig = inspect.signature(fiacre::ConstrExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::constrexp_has_name():
    assert hasattr(fiacre::ConstrExp, "name")
    descriptor = None
    for klass in fiacre::ConstrExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::constantdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::ConstantDecl)


def test_fiacre::constantdecl_constructor_exists():
    assert callable(fiacre::ConstantDecl.__init__)


def test_fiacre::constantdecl_constructor_args():
    sig = inspect.signature(fiacre::ConstantDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::refarg_is_not_abstract():
    assert not inspect.isabstract(fiacre::RefArg)


def test_fiacre::refarg_constructor_exists():
    assert callable(fiacre::RefArg.__init__)


def test_fiacre::refarg_constructor_args():
    sig = inspect.signature(fiacre::RefArg.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::rule_is_not_abstract():
    assert not inspect.isabstract(fiacre::Rule)


def test_fiacre::rule_constructor_exists():
    assert callable(fiacre::Rule.__init__)


def test_fiacre::rule_constructor_args():
    sig = inspect.signature(fiacre::Rule.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::casestmt_is_not_abstract():
    assert not inspect.isabstract(fiacre::CaseStmt)


def test_fiacre::casestmt_constructor_exists():
    assert callable(fiacre::CaseStmt.__init__)


def test_fiacre::casestmt_constructor_args():
    sig = inspect.signature(fiacre::CaseStmt.__init__)
    params = list(sig.parameters.keys())



def test_channel_is_not_abstract():
    assert not inspect.isabstract(Channel)


def test_channel_constructor_exists():
    assert callable(Channel.__init__)


def test_channel_constructor_args():
    sig = inspect.signature(Channel.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::profile_is_not_abstract():
    assert not inspect.isabstract(fiacre::Profile)


def test_fiacre::profile_constructor_exists():
    assert callable(fiacre::Profile.__init__)


def test_fiacre::profile_constructor_args():
    sig = inspect.signature(fiacre::Profile.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::typeid_is_not_abstract():
    assert not inspect.isabstract(fiacre::TypeId)


def test_fiacre::typeid_constructor_exists():
    assert callable(fiacre::TypeId.__init__)


def test_fiacre::typeid_constructor_args():
    sig = inspect.signature(fiacre::TypeId.__init__)
    params = list(sig.parameters.keys())



def test_portdecl_is_not_abstract():
    assert not inspect.isabstract(PortDecl)


def test_portdecl_constructor_exists():
    assert callable(PortDecl.__init__)


def test_portdecl_constructor_args():
    sig = inspect.signature(PortDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::paramportdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::ParamPortDecl)


def test_fiacre::paramportdecl_constructor_exists():
    assert callable(fiacre::ParamPortDecl.__init__)


def test_fiacre::paramportdecl_constructor_args():
    sig = inspect.signature(fiacre::ParamPortDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::localportdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre::LocalPortDecl)


def test_fiacre::localportdecl_constructor_exists():
    assert callable(fiacre::LocalPortDecl.__init__)


def test_fiacre::localportdecl_constructor_args():
    sig = inspect.signature(fiacre::LocalPortDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::seq_is_not_abstract():
    assert not inspect.isabstract(fiacre::Seq)


def test_fiacre::seq_constructor_exists():
    assert callable(fiacre::Seq.__init__)


def test_fiacre::seq_constructor_args():
    sig = inspect.signature(fiacre::Seq.__init__)
    params = list(sig.parameters.keys())



def test_communication_is_not_abstract():
    assert not inspect.isabstract(Communication)


def test_communication_constructor_exists():
    assert callable(Communication.__init__)


def test_communication_constructor_args():
    sig = inspect.signature(Communication.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::emission_is_not_abstract():
    assert not inspect.isabstract(fiacre::Emission)


def test_fiacre::emission_constructor_exists():
    assert callable(fiacre::Emission.__init__)


def test_fiacre::emission_constructor_args():
    sig = inspect.signature(fiacre::Emission.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::reception_is_not_abstract():
    assert not inspect.isabstract(fiacre::Reception)


def test_fiacre::reception_constructor_exists():
    assert callable(fiacre::Reception.__init__)


def test_fiacre::reception_constructor_args():
    sig = inspect.signature(fiacre::Reception.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::synchronization_is_not_abstract():
    assert not inspect.isabstract(fiacre::Synchronization)


def test_fiacre::synchronization_constructor_exists():
    assert callable(fiacre::Synchronization.__init__)


def test_fiacre::synchronization_constructor_args():
    sig = inspect.signature(fiacre::Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::valuedfield_is_not_abstract():
    assert not inspect.isabstract(fiacre::ValuedField)


def test_fiacre::valuedfield_constructor_exists():
    assert callable(fiacre::ValuedField.__init__)


def test_fiacre::valuedfield_constructor_args():
    sig = inspect.signature(fiacre::ValuedField.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre::valuedfield_has_field():
    assert hasattr(fiacre::ValuedField, "field")
    descriptor = None
    for klass in fiacre::ValuedField.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::inlinerecord_is_not_abstract():
    assert not inspect.isabstract(fiacre::InlineRecord)


def test_fiacre::inlinerecord_constructor_exists():
    assert callable(fiacre::InlineRecord.__init__)


def test_fiacre::inlinerecord_constructor_args():
    sig = inspect.signature(fiacre::InlineRecord.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::inlinearray_is_not_abstract():
    assert not inspect.isabstract(fiacre::InlineArray)


def test_fiacre::inlinearray_constructor_exists():
    assert callable(fiacre::InlineArray.__init__)


def test_fiacre::inlinearray_constructor_args():
    sig = inspect.signature(fiacre::InlineArray.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::literal_is_not_abstract():
    assert not inspect.isabstract(fiacre::Literal)


def test_fiacre::literal_constructor_exists():
    assert callable(fiacre::Literal.__init__)


def test_fiacre::literal_constructor_args():
    sig = inspect.signature(fiacre::Literal.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::constrpattern_is_not_abstract():
    assert not inspect.isabstract(fiacre::ConstrPattern)


def test_fiacre::constrpattern_constructor_exists():
    assert callable(fiacre::ConstrPattern.__init__)


def test_fiacre::constrpattern_constructor_args():
    sig = inspect.signature(fiacre::ConstrPattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre::constrpattern_has_name():
    assert hasattr(fiacre::ConstrPattern, "name")
    descriptor = None
    for klass in fiacre::ConstrPattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::anypattern_is_not_abstract():
    assert not inspect.isabstract(fiacre::AnyPattern)


def test_fiacre::anypattern_constructor_exists():
    assert callable(fiacre::AnyPattern.__init__)


def test_fiacre::anypattern_constructor_args():
    sig = inspect.signature(fiacre::AnyPattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::constantref_is_not_abstract():
    assert not inspect.isabstract(fiacre::ConstantRef)


def test_fiacre::constantref_constructor_exists():
    assert callable(fiacre::ConstantRef.__init__)


def test_fiacre::constantref_constructor_args():
    sig = inspect.signature(fiacre::ConstantRef.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::arraypattern_is_not_abstract():
    assert not inspect.isabstract(fiacre::ArrayPattern)


def test_fiacre::arraypattern_constructor_exists():
    assert callable(fiacre::ArrayPattern.__init__)


def test_fiacre::arraypattern_constructor_args():
    sig = inspect.signature(fiacre::ArrayPattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::fieldpattern_is_not_abstract():
    assert not inspect.isabstract(fiacre::FieldPattern)


def test_fiacre::fieldpattern_constructor_exists():
    assert callable(fiacre::FieldPattern.__init__)


def test_fiacre::fieldpattern_constructor_args():
    sig = inspect.signature(fiacre::FieldPattern.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre::fieldpattern_has_field():
    assert hasattr(fiacre::FieldPattern, "field")
    descriptor = None
    for klass in fiacre::FieldPattern.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::varref_is_not_abstract():
    assert not inspect.isabstract(fiacre::VarRef)


def test_fiacre::varref_constructor_exists():
    assert callable(fiacre::VarRef.__init__)


def test_fiacre::varref_constructor_args():
    sig = inspect.signature(fiacre::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::boolliteral_is_not_abstract():
    assert not inspect.isabstract(fiacre::BoolLiteral)


def test_fiacre::boolliteral_constructor_exists():
    assert callable(fiacre::BoolLiteral.__init__)


def test_fiacre::boolliteral_constructor_args():
    sig = inspect.signature(fiacre::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fiacre::boolliteral_has_value():
    assert hasattr(fiacre::BoolLiteral, "value")
    descriptor = None
    for klass in fiacre::BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::natliteral_is_not_abstract():
    assert not inspect.isabstract(fiacre::NatLiteral)


def test_fiacre::natliteral_constructor_exists():
    assert callable(fiacre::NatLiteral.__init__)


def test_fiacre::natliteral_constructor_args():
    sig = inspect.signature(fiacre::NatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fiacre::natliteral_has_value():
    assert hasattr(fiacre::NatLiteral, "value")
    descriptor = None
    for klass in fiacre::NatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fiacre::queue_is_not_abstract():
    assert not inspect.isabstract(fiacre::Queue)


def test_fiacre::queue_constructor_exists():
    assert callable(fiacre::Queue.__init__)


def test_fiacre::queue_constructor_args():
    sig = inspect.signature(fiacre::Queue.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::array_is_not_abstract():
    assert not inspect.isabstract(fiacre::Array)


def test_fiacre::array_constructor_exists():
    assert callable(fiacre::Array.__init__)


def test_fiacre::array_constructor_args():
    sig = inspect.signature(fiacre::Array.__init__)
    params = list(sig.parameters.keys())



def test_labeledtype_is_not_abstract():
    assert not inspect.isabstract(LabeledType)


def test_labeledtype_constructor_exists():
    assert callable(LabeledType.__init__)


def test_labeledtype_constructor_args():
    sig = inspect.signature(LabeledType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::constr_is_not_abstract():
    assert not inspect.isabstract(fiacre::Constr)


def test_fiacre::constr_constructor_exists():
    assert callable(fiacre::Constr.__init__)


def test_fiacre::constr_constructor_args():
    sig = inspect.signature(fiacre::Constr.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::field_is_not_abstract():
    assert not inspect.isabstract(fiacre::Field)


def test_fiacre::field_constructor_exists():
    assert callable(fiacre::Field.__init__)


def test_fiacre::field_constructor_args():
    sig = inspect.signature(fiacre::Field.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::record_is_not_abstract():
    assert not inspect.isabstract(fiacre::Record)


def test_fiacre::record_constructor_exists():
    assert callable(fiacre::Record.__init__)


def test_fiacre::record_constructor_args():
    sig = inspect.signature(fiacre::Record.__init__)
    params = list(sig.parameters.keys())



def test_fiacre::interval_is_not_abstract():
    assert not inspect.isabstract(fiacre::Interval)


def test_fiacre::interval_constructor_exists():
    assert callable(fiacre::Interval.__init__)


def test_fiacre::interval_constructor_args():
    sig = inspect.signature(fiacre::Interval.__init__)
    params = list(sig.parameters.keys())

def test_binop_exists():
    # Check that the Enumeration exists
    assert BinOp is not None

def test_binop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinOp]
    expected_literals = [
        "BADD",
        "BGT",
        "BMOD",
        "BMINUS",
        "BEQ",
        "BLT",
        "ENQUEUE",
        "BOR",
        "BGE",
        "BDIV",
        "APPEND",
        "BMUL",
        "BLE",
        "BNE",
        "BAND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinOp"

def test_unop_exists():
    # Check that the Enumeration exists
    assert UnOp is not None

def test_unop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnOp]
    expected_literals = [
        "UNOT",
        "UEMPTY",
        "UFULL",
        "UMINUS",
        "UDOLLAR",
        "FIRST",
        "DEQUEUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnOp"


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
BasicType_strategy = st.builds(
    BasicType,
)
fiacre::NatType_strategy = st.builds(
    fiacre::NatType,
)
fiacre::IntType_strategy = st.builds(
    fiacre::IntType,
)
fiacre::BoolType_strategy = st.builds(
    fiacre::BoolType,
)
Type_strategy = st.builds(
    Type,
)
fiacre::BasicType_strategy = st.builds(
    fiacre::BasicType,
)
InlineCollection_strategy = st.builds(
    InlineCollection,
)
fiacre::InlineQueue_strategy = st.builds(
    fiacre::InlineQueue,
)
fiacre::Variable_strategy = st.builds(
    fiacre::Variable,
    name=
        safe_text
)
fiacre::MaxBound_strategy = st.builds(
    fiacre::MaxBound,
)
fiacre::MinBound_strategy = st.builds(
    fiacre::MinBound,
)
Exp_strategy = st.builds(
    Exp,
)
fiacre::ArrayElem_strategy = st.builds(
    fiacre::ArrayElem,
)
fiacre::BinExp_strategy = st.builds(
    fiacre::BinExp,
    binOp=
        safe_text
)
fiacre::RecordElem_strategy = st.builds(
    fiacre::RecordElem,
    field=
        safe_text
)
fiacre::UnExp_strategy = st.builds(
    fiacre::UnExp,
    unop=
        safe_text
)
fiacre::Pattern_strategy = st.builds(
    fiacre::Pattern,
)
fiacre::SingleAssignment_strategy = st.builds(
    fiacre::SingleAssignment,
)
Assignment_strategy = st.builds(
    Assignment,
)
fiacre::NonDeterministicAssignment_strategy = st.builds(
    fiacre::NonDeterministicAssignment,
)
fiacre::DeterministicAssignment_strategy = st.builds(
    fiacre::DeterministicAssignment,
)
fiacre::InterfacedComp_strategy = st.builds(
    fiacre::InterfacedComp,
)
Composition_strategy = st.builds(
    Composition,
)
fiacre::Instance_strategy = st.builds(
    fiacre::Instance,
    name=
        safe_text
)
fiacre::Par_strategy = st.builds(
    fiacre::Par,
)
Statement_strategy = st.builds(
    Statement,
)
fiacre::To_strategy = st.builds(
    fiacre::To,
)
fiacre::Select_strategy = st.builds(
    fiacre::Select,
)
fiacre::Assignment_strategy = st.builds(
    fiacre::Assignment,
)
fiacre::Wait_strategy = st.builds(
    fiacre::Wait,
)
fiacre::Communication_strategy = st.builds(
    fiacre::Communication,
)
fiacre::WhileStmt_strategy = st.builds(
    fiacre::WhileStmt,
)
fiacre::IfStmt_strategy = st.builds(
    fiacre::IfStmt,
)
fiacre::NullStmt_strategy = st.builds(
    fiacre::NullStmt,
)
Arg_strategy = st.builds(
    Arg,
)
fiacre::Exp_strategy = st.builds(
    fiacre::Exp,
)
fiacre::Arg_strategy = st.builds(
    fiacre::Arg,
)
Declaration_strategy = st.builds(
    Declaration,
)
fiacre::NodeDecl_strategy = st.builds(
    fiacre::NodeDecl,
)
fiacre::Declaration_strategy = st.builds(
    fiacre::Declaration,
    name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
fiacre::ArgumentVariable_strategy = st.builds(
    fiacre::ArgumentVariable,
    read=
        st.booleans(),
    write=
        st.booleans(),
    ref=
        st.booleans()
)
fiacre::PortDecl_strategy = st.builds(
    fiacre::PortDecl,
    out=
        st.booleans(),
    name=
        safe_text,
    in_=
        st.booleans()
)
fiacre::Transition_strategy = st.builds(
    fiacre::Transition,
    name=
        safe_text
)
fiacre::State_strategy = st.builds(
    fiacre::State,
    name=
        safe_text
)
fiacre::Priority_strategy = st.builds(
    fiacre::Priority,
)
fiacre::Composition_strategy = st.builds(
    fiacre::Composition,
)
NodeDecl_strategy = st.builds(
    NodeDecl,
)
fiacre::ProcessDecl_strategy = st.builds(
    fiacre::ProcessDecl,
)
fiacre::ComponentDecl_strategy = st.builds(
    fiacre::ComponentDecl,
)
fiacre::Channel_strategy = st.builds(
    fiacre::Channel,
)
fiacre::ChannelDecl_strategy = st.builds(
    fiacre::ChannelDecl,
)
fiacre::Type_strategy = st.builds(
    fiacre::Type,
)
fiacre::TypeDecl_strategy = st.builds(
    fiacre::TypeDecl,
)
fiacre::Statement_strategy = st.builds(
    fiacre::Statement,
    comment=
        safe_text
)
fiacre::LocalVariable_strategy = st.builds(
    fiacre::LocalVariable,
    constant=
        st.booleans()
)
fiacre::Program_strategy = st.builds(
    fiacre::Program,
)
fiacre::InlineCollection_strategy = st.builds(
    fiacre::InlineCollection,
)
fiacre::Foreach_strategy = st.builds(
    fiacre::Foreach,
)
fiacre::CondExp_strategy = st.builds(
    fiacre::CondExp,
)
MaxBound_strategy = st.builds(
    MaxBound,
)
fiacre::InfiniteBound_strategy = st.builds(
    fiacre::InfiniteBound,
)
MinBound_strategy = st.builds(
    MinBound,
)
fiacre::FiniteBound_strategy = st.builds(
    fiacre::FiniteBound,
    strict=
        st.booleans(),
    val=
        st.integers()
)
fiacre::LabeledType_strategy = st.builds(
    fiacre::LabeledType,
    name=
        safe_text
)
fiacre::Union_strategy = st.builds(
    fiacre::Union,
)
fiacre::ConstrExp_strategy = st.builds(
    fiacre::ConstrExp,
    name=
        safe_text
)
fiacre::ConstantDecl_strategy = st.builds(
    fiacre::ConstantDecl,
)
fiacre::RefArg_strategy = st.builds(
    fiacre::RefArg,
)
fiacre::Rule_strategy = st.builds(
    fiacre::Rule,
)
fiacre::CaseStmt_strategy = st.builds(
    fiacre::CaseStmt,
)
Channel_strategy = st.builds(
    Channel,
)
fiacre::Profile_strategy = st.builds(
    fiacre::Profile,
)
fiacre::TypeId_strategy = st.builds(
    fiacre::TypeId,
)
PortDecl_strategy = st.builds(
    PortDecl,
)
fiacre::ParamPortDecl_strategy = st.builds(
    fiacre::ParamPortDecl,
)
fiacre::LocalPortDecl_strategy = st.builds(
    fiacre::LocalPortDecl,
)
fiacre::Seq_strategy = st.builds(
    fiacre::Seq,
)
Communication_strategy = st.builds(
    Communication,
)
fiacre::Emission_strategy = st.builds(
    fiacre::Emission,
)
fiacre::Reception_strategy = st.builds(
    fiacre::Reception,
)
fiacre::Synchronization_strategy = st.builds(
    fiacre::Synchronization,
)
fiacre::ValuedField_strategy = st.builds(
    fiacre::ValuedField,
    field=
        safe_text
)
fiacre::InlineRecord_strategy = st.builds(
    fiacre::InlineRecord,
)
fiacre::InlineArray_strategy = st.builds(
    fiacre::InlineArray,
)
Pattern_strategy = st.builds(
    Pattern,
)
fiacre::Literal_strategy = st.builds(
    fiacre::Literal,
)
fiacre::ConstrPattern_strategy = st.builds(
    fiacre::ConstrPattern,
    name=
        safe_text
)
fiacre::AnyPattern_strategy = st.builds(
    fiacre::AnyPattern,
)
fiacre::ConstantRef_strategy = st.builds(
    fiacre::ConstantRef,
)
fiacre::ArrayPattern_strategy = st.builds(
    fiacre::ArrayPattern,
)
fiacre::FieldPattern_strategy = st.builds(
    fiacre::FieldPattern,
    field=
        safe_text
)
fiacre::VarRef_strategy = st.builds(
    fiacre::VarRef,
)
Literal_strategy = st.builds(
    Literal,
)
fiacre::BoolLiteral_strategy = st.builds(
    fiacre::BoolLiteral,
    value=
        st.booleans()
)
fiacre::NatLiteral_strategy = st.builds(
    fiacre::NatLiteral,
    value=
        st.integers()
)
fiacre::Queue_strategy = st.builds(
    fiacre::Queue,
)
fiacre::Array_strategy = st.builds(
    fiacre::Array,
)
LabeledType_strategy = st.builds(
    LabeledType,
)
fiacre::Constr_strategy = st.builds(
    fiacre::Constr,
)
fiacre::Field_strategy = st.builds(
    fiacre::Field,
)
fiacre::Record_strategy = st.builds(
    fiacre::Record,
)
fiacre::Interval_strategy = st.builds(
    fiacre::Interval,
)

@given(instance=BasicType_strategy)
@settings(max_examples=50)
def test_basictype_instantiation(instance):
    assert isinstance(instance, BasicType)

@given(instance=fiacre::NatType_strategy)
@settings(max_examples=50)
def test_fiacre::nattype_instantiation(instance):
    assert isinstance(instance, fiacre::NatType)

@given(instance=fiacre::IntType_strategy)
@settings(max_examples=50)
def test_fiacre::inttype_instantiation(instance):
    assert isinstance(instance, fiacre::IntType)

@given(instance=fiacre::BoolType_strategy)
@settings(max_examples=50)
def test_fiacre::booltype_instantiation(instance):
    assert isinstance(instance, fiacre::BoolType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=fiacre::BasicType_strategy)
@settings(max_examples=50)
def test_fiacre::basictype_instantiation(instance):
    assert isinstance(instance, fiacre::BasicType)

@given(instance=InlineCollection_strategy)
@settings(max_examples=50)
def test_inlinecollection_instantiation(instance):
    assert isinstance(instance, InlineCollection)

@given(instance=fiacre::InlineQueue_strategy)
@settings(max_examples=50)
def test_fiacre::inlinequeue_instantiation(instance):
    assert isinstance(instance, fiacre::InlineQueue)

@given(instance=fiacre::Variable_strategy)
@settings(max_examples=50)
def test_fiacre::variable_instantiation(instance):
    assert isinstance(instance, fiacre::Variable)

@given(instance=fiacre::Variable_strategy)
def test_fiacre::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::Variable_strategy)
def test_fiacre::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::MaxBound_strategy)
@settings(max_examples=50)
def test_fiacre::maxbound_instantiation(instance):
    assert isinstance(instance, fiacre::MaxBound)

@given(instance=fiacre::MinBound_strategy)
@settings(max_examples=50)
def test_fiacre::minbound_instantiation(instance):
    assert isinstance(instance, fiacre::MinBound)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=fiacre::ArrayElem_strategy)
@settings(max_examples=50)
def test_fiacre::arrayelem_instantiation(instance):
    assert isinstance(instance, fiacre::ArrayElem)

@given(instance=fiacre::BinExp_strategy)
@settings(max_examples=50)
def test_fiacre::binexp_instantiation(instance):
    assert isinstance(instance, fiacre::BinExp)

@given(instance=fiacre::BinExp_strategy)
def test_fiacre::binexp_binOp_type(instance):
    assert isinstance(instance.binOp, str)


@given(instance=fiacre::BinExp_strategy)
def test_fiacre::binexp_binOp_setter(instance):
    original = instance.binOp
    instance.binOp = original
    assert instance.binOp == original

@given(instance=fiacre::RecordElem_strategy)
@settings(max_examples=50)
def test_fiacre::recordelem_instantiation(instance):
    assert isinstance(instance, fiacre::RecordElem)

@given(instance=fiacre::RecordElem_strategy)
def test_fiacre::recordelem_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=fiacre::RecordElem_strategy)
def test_fiacre::recordelem_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre::UnExp_strategy)
@settings(max_examples=50)
def test_fiacre::unexp_instantiation(instance):
    assert isinstance(instance, fiacre::UnExp)

@given(instance=fiacre::UnExp_strategy)
def test_fiacre::unexp_unop_type(instance):
    assert isinstance(instance.unop, str)


@given(instance=fiacre::UnExp_strategy)
def test_fiacre::unexp_unop_setter(instance):
    original = instance.unop
    instance.unop = original
    assert instance.unop == original

@given(instance=fiacre::Pattern_strategy)
@settings(max_examples=50)
def test_fiacre::pattern_instantiation(instance):
    assert isinstance(instance, fiacre::Pattern)

@given(instance=fiacre::SingleAssignment_strategy)
@settings(max_examples=50)
def test_fiacre::singleassignment_instantiation(instance):
    assert isinstance(instance, fiacre::SingleAssignment)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=fiacre::NonDeterministicAssignment_strategy)
@settings(max_examples=50)
def test_fiacre::nondeterministicassignment_instantiation(instance):
    assert isinstance(instance, fiacre::NonDeterministicAssignment)

@given(instance=fiacre::DeterministicAssignment_strategy)
@settings(max_examples=50)
def test_fiacre::deterministicassignment_instantiation(instance):
    assert isinstance(instance, fiacre::DeterministicAssignment)

@given(instance=fiacre::InterfacedComp_strategy)
@settings(max_examples=50)
def test_fiacre::interfacedcomp_instantiation(instance):
    assert isinstance(instance, fiacre::InterfacedComp)

@given(instance=Composition_strategy)
@settings(max_examples=50)
def test_composition_instantiation(instance):
    assert isinstance(instance, Composition)

@given(instance=fiacre::Instance_strategy)
@settings(max_examples=50)
def test_fiacre::instance_instantiation(instance):
    assert isinstance(instance, fiacre::Instance)

@given(instance=fiacre::Instance_strategy)
def test_fiacre::instance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::Instance_strategy)
def test_fiacre::instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::Par_strategy)
@settings(max_examples=50)
def test_fiacre::par_instantiation(instance):
    assert isinstance(instance, fiacre::Par)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fiacre::To_strategy)
@settings(max_examples=50)
def test_fiacre::to_instantiation(instance):
    assert isinstance(instance, fiacre::To)

@given(instance=fiacre::Select_strategy)
@settings(max_examples=50)
def test_fiacre::select_instantiation(instance):
    assert isinstance(instance, fiacre::Select)

@given(instance=fiacre::Assignment_strategy)
@settings(max_examples=50)
def test_fiacre::assignment_instantiation(instance):
    assert isinstance(instance, fiacre::Assignment)

@given(instance=fiacre::Wait_strategy)
@settings(max_examples=50)
def test_fiacre::wait_instantiation(instance):
    assert isinstance(instance, fiacre::Wait)

@given(instance=fiacre::Communication_strategy)
@settings(max_examples=50)
def test_fiacre::communication_instantiation(instance):
    assert isinstance(instance, fiacre::Communication)

@given(instance=fiacre::WhileStmt_strategy)
@settings(max_examples=50)
def test_fiacre::whilestmt_instantiation(instance):
    assert isinstance(instance, fiacre::WhileStmt)

@given(instance=fiacre::IfStmt_strategy)
@settings(max_examples=50)
def test_fiacre::ifstmt_instantiation(instance):
    assert isinstance(instance, fiacre::IfStmt)

@given(instance=fiacre::NullStmt_strategy)
@settings(max_examples=50)
def test_fiacre::nullstmt_instantiation(instance):
    assert isinstance(instance, fiacre::NullStmt)

@given(instance=Arg_strategy)
@settings(max_examples=50)
def test_arg_instantiation(instance):
    assert isinstance(instance, Arg)

@given(instance=fiacre::Exp_strategy)
@settings(max_examples=50)
def test_fiacre::exp_instantiation(instance):
    assert isinstance(instance, fiacre::Exp)

@given(instance=fiacre::Arg_strategy)
@settings(max_examples=50)
def test_fiacre::arg_instantiation(instance):
    assert isinstance(instance, fiacre::Arg)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=fiacre::NodeDecl_strategy)
@settings(max_examples=50)
def test_fiacre::nodedecl_instantiation(instance):
    assert isinstance(instance, fiacre::NodeDecl)

@given(instance=fiacre::Declaration_strategy)
@settings(max_examples=50)
def test_fiacre::declaration_instantiation(instance):
    assert isinstance(instance, fiacre::Declaration)

@given(instance=fiacre::Declaration_strategy)
def test_fiacre::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::Declaration_strategy)
def test_fiacre::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=fiacre::ArgumentVariable_strategy)
@settings(max_examples=50)
def test_fiacre::argumentvariable_instantiation(instance):
    assert isinstance(instance, fiacre::ArgumentVariable)

@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_read_type(instance):
    assert isinstance(instance.read, bool)


@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_read_setter(instance):
    original = instance.read
    instance.read = original
    assert instance.read == original

@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_write_type(instance):
    assert isinstance(instance.write, bool)


@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_ref_type(instance):
    assert isinstance(instance.ref, bool)


@given(instance=fiacre::ArgumentVariable_strategy)
def test_fiacre::argumentvariable_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=fiacre::PortDecl_strategy)
@settings(max_examples=50)
def test_fiacre::portdecl_instantiation(instance):
    assert isinstance(instance, fiacre::PortDecl)

@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_out_type(instance):
    assert isinstance(instance.out, bool)


@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_in__type(instance):
    assert isinstance(instance.in_, bool)


@given(instance=fiacre::PortDecl_strategy)
def test_fiacre::portdecl_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=fiacre::Transition_strategy)
@settings(max_examples=50)
def test_fiacre::transition_instantiation(instance):
    assert isinstance(instance, fiacre::Transition)

@given(instance=fiacre::Transition_strategy)
def test_fiacre::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::Transition_strategy)
def test_fiacre::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::State_strategy)
@settings(max_examples=50)
def test_fiacre::state_instantiation(instance):
    assert isinstance(instance, fiacre::State)

@given(instance=fiacre::State_strategy)
def test_fiacre::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::State_strategy)
def test_fiacre::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::Priority_strategy)
@settings(max_examples=50)
def test_fiacre::priority_instantiation(instance):
    assert isinstance(instance, fiacre::Priority)

@given(instance=fiacre::Composition_strategy)
@settings(max_examples=50)
def test_fiacre::composition_instantiation(instance):
    assert isinstance(instance, fiacre::Composition)

@given(instance=NodeDecl_strategy)
@settings(max_examples=50)
def test_nodedecl_instantiation(instance):
    assert isinstance(instance, NodeDecl)

@given(instance=fiacre::ProcessDecl_strategy)
@settings(max_examples=50)
def test_fiacre::processdecl_instantiation(instance):
    assert isinstance(instance, fiacre::ProcessDecl)

@given(instance=fiacre::ComponentDecl_strategy)
@settings(max_examples=50)
def test_fiacre::componentdecl_instantiation(instance):
    assert isinstance(instance, fiacre::ComponentDecl)

@given(instance=fiacre::Channel_strategy)
@settings(max_examples=50)
def test_fiacre::channel_instantiation(instance):
    assert isinstance(instance, fiacre::Channel)

@given(instance=fiacre::ChannelDecl_strategy)
@settings(max_examples=50)
def test_fiacre::channeldecl_instantiation(instance):
    assert isinstance(instance, fiacre::ChannelDecl)

@given(instance=fiacre::Type_strategy)
@settings(max_examples=50)
def test_fiacre::type_instantiation(instance):
    assert isinstance(instance, fiacre::Type)

@given(instance=fiacre::TypeDecl_strategy)
@settings(max_examples=50)
def test_fiacre::typedecl_instantiation(instance):
    assert isinstance(instance, fiacre::TypeDecl)

@given(instance=fiacre::Statement_strategy)
@settings(max_examples=50)
def test_fiacre::statement_instantiation(instance):
    assert isinstance(instance, fiacre::Statement)

@given(instance=fiacre::Statement_strategy)
def test_fiacre::statement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=fiacre::Statement_strategy)
def test_fiacre::statement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fiacre::LocalVariable_strategy)
@settings(max_examples=50)
def test_fiacre::localvariable_instantiation(instance):
    assert isinstance(instance, fiacre::LocalVariable)

@given(instance=fiacre::LocalVariable_strategy)
def test_fiacre::localvariable_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=fiacre::LocalVariable_strategy)
def test_fiacre::localvariable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=fiacre::Program_strategy)
@settings(max_examples=50)
def test_fiacre::program_instantiation(instance):
    assert isinstance(instance, fiacre::Program)

@given(instance=fiacre::InlineCollection_strategy)
@settings(max_examples=50)
def test_fiacre::inlinecollection_instantiation(instance):
    assert isinstance(instance, fiacre::InlineCollection)

@given(instance=fiacre::Foreach_strategy)
@settings(max_examples=50)
def test_fiacre::foreach_instantiation(instance):
    assert isinstance(instance, fiacre::Foreach)

@given(instance=fiacre::CondExp_strategy)
@settings(max_examples=50)
def test_fiacre::condexp_instantiation(instance):
    assert isinstance(instance, fiacre::CondExp)

@given(instance=MaxBound_strategy)
@settings(max_examples=50)
def test_maxbound_instantiation(instance):
    assert isinstance(instance, MaxBound)

@given(instance=fiacre::InfiniteBound_strategy)
@settings(max_examples=50)
def test_fiacre::infinitebound_instantiation(instance):
    assert isinstance(instance, fiacre::InfiniteBound)

@given(instance=MinBound_strategy)
@settings(max_examples=50)
def test_minbound_instantiation(instance):
    assert isinstance(instance, MinBound)

@given(instance=fiacre::FiniteBound_strategy)
@settings(max_examples=50)
def test_fiacre::finitebound_instantiation(instance):
    assert isinstance(instance, fiacre::FiniteBound)

@given(instance=fiacre::FiniteBound_strategy)
def test_fiacre::finitebound_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=fiacre::FiniteBound_strategy)
def test_fiacre::finitebound_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=fiacre::FiniteBound_strategy)
def test_fiacre::finitebound_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=fiacre::FiniteBound_strategy)
def test_fiacre::finitebound_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=fiacre::LabeledType_strategy)
@settings(max_examples=50)
def test_fiacre::labeledtype_instantiation(instance):
    assert isinstance(instance, fiacre::LabeledType)

@given(instance=fiacre::LabeledType_strategy)
def test_fiacre::labeledtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::LabeledType_strategy)
def test_fiacre::labeledtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::Union_strategy)
@settings(max_examples=50)
def test_fiacre::union_instantiation(instance):
    assert isinstance(instance, fiacre::Union)

@given(instance=fiacre::ConstrExp_strategy)
@settings(max_examples=50)
def test_fiacre::constrexp_instantiation(instance):
    assert isinstance(instance, fiacre::ConstrExp)

@given(instance=fiacre::ConstrExp_strategy)
def test_fiacre::constrexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::ConstrExp_strategy)
def test_fiacre::constrexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::ConstantDecl_strategy)
@settings(max_examples=50)
def test_fiacre::constantdecl_instantiation(instance):
    assert isinstance(instance, fiacre::ConstantDecl)

@given(instance=fiacre::RefArg_strategy)
@settings(max_examples=50)
def test_fiacre::refarg_instantiation(instance):
    assert isinstance(instance, fiacre::RefArg)

@given(instance=fiacre::Rule_strategy)
@settings(max_examples=50)
def test_fiacre::rule_instantiation(instance):
    assert isinstance(instance, fiacre::Rule)

@given(instance=fiacre::CaseStmt_strategy)
@settings(max_examples=50)
def test_fiacre::casestmt_instantiation(instance):
    assert isinstance(instance, fiacre::CaseStmt)

@given(instance=Channel_strategy)
@settings(max_examples=50)
def test_channel_instantiation(instance):
    assert isinstance(instance, Channel)

@given(instance=fiacre::Profile_strategy)
@settings(max_examples=50)
def test_fiacre::profile_instantiation(instance):
    assert isinstance(instance, fiacre::Profile)

@given(instance=fiacre::TypeId_strategy)
@settings(max_examples=50)
def test_fiacre::typeid_instantiation(instance):
    assert isinstance(instance, fiacre::TypeId)

@given(instance=PortDecl_strategy)
@settings(max_examples=50)
def test_portdecl_instantiation(instance):
    assert isinstance(instance, PortDecl)

@given(instance=fiacre::ParamPortDecl_strategy)
@settings(max_examples=50)
def test_fiacre::paramportdecl_instantiation(instance):
    assert isinstance(instance, fiacre::ParamPortDecl)

@given(instance=fiacre::LocalPortDecl_strategy)
@settings(max_examples=50)
def test_fiacre::localportdecl_instantiation(instance):
    assert isinstance(instance, fiacre::LocalPortDecl)

@given(instance=fiacre::Seq_strategy)
@settings(max_examples=50)
def test_fiacre::seq_instantiation(instance):
    assert isinstance(instance, fiacre::Seq)

@given(instance=Communication_strategy)
@settings(max_examples=50)
def test_communication_instantiation(instance):
    assert isinstance(instance, Communication)

@given(instance=fiacre::Emission_strategy)
@settings(max_examples=50)
def test_fiacre::emission_instantiation(instance):
    assert isinstance(instance, fiacre::Emission)

@given(instance=fiacre::Reception_strategy)
@settings(max_examples=50)
def test_fiacre::reception_instantiation(instance):
    assert isinstance(instance, fiacre::Reception)

@given(instance=fiacre::Synchronization_strategy)
@settings(max_examples=50)
def test_fiacre::synchronization_instantiation(instance):
    assert isinstance(instance, fiacre::Synchronization)

@given(instance=fiacre::ValuedField_strategy)
@settings(max_examples=50)
def test_fiacre::valuedfield_instantiation(instance):
    assert isinstance(instance, fiacre::ValuedField)

@given(instance=fiacre::ValuedField_strategy)
def test_fiacre::valuedfield_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=fiacre::ValuedField_strategy)
def test_fiacre::valuedfield_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre::InlineRecord_strategy)
@settings(max_examples=50)
def test_fiacre::inlinerecord_instantiation(instance):
    assert isinstance(instance, fiacre::InlineRecord)

@given(instance=fiacre::InlineArray_strategy)
@settings(max_examples=50)
def test_fiacre::inlinearray_instantiation(instance):
    assert isinstance(instance, fiacre::InlineArray)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=fiacre::Literal_strategy)
@settings(max_examples=50)
def test_fiacre::literal_instantiation(instance):
    assert isinstance(instance, fiacre::Literal)

@given(instance=fiacre::ConstrPattern_strategy)
@settings(max_examples=50)
def test_fiacre::constrpattern_instantiation(instance):
    assert isinstance(instance, fiacre::ConstrPattern)

@given(instance=fiacre::ConstrPattern_strategy)
def test_fiacre::constrpattern_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fiacre::ConstrPattern_strategy)
def test_fiacre::constrpattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre::AnyPattern_strategy)
@settings(max_examples=50)
def test_fiacre::anypattern_instantiation(instance):
    assert isinstance(instance, fiacre::AnyPattern)

@given(instance=fiacre::ConstantRef_strategy)
@settings(max_examples=50)
def test_fiacre::constantref_instantiation(instance):
    assert isinstance(instance, fiacre::ConstantRef)

@given(instance=fiacre::ArrayPattern_strategy)
@settings(max_examples=50)
def test_fiacre::arraypattern_instantiation(instance):
    assert isinstance(instance, fiacre::ArrayPattern)

@given(instance=fiacre::FieldPattern_strategy)
@settings(max_examples=50)
def test_fiacre::fieldpattern_instantiation(instance):
    assert isinstance(instance, fiacre::FieldPattern)

@given(instance=fiacre::FieldPattern_strategy)
def test_fiacre::fieldpattern_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=fiacre::FieldPattern_strategy)
def test_fiacre::fieldpattern_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre::VarRef_strategy)
@settings(max_examples=50)
def test_fiacre::varref_instantiation(instance):
    assert isinstance(instance, fiacre::VarRef)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fiacre::BoolLiteral_strategy)
@settings(max_examples=50)
def test_fiacre::boolliteral_instantiation(instance):
    assert isinstance(instance, fiacre::BoolLiteral)

@given(instance=fiacre::BoolLiteral_strategy)
def test_fiacre::boolliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fiacre::BoolLiteral_strategy)
def test_fiacre::boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fiacre::NatLiteral_strategy)
@settings(max_examples=50)
def test_fiacre::natliteral_instantiation(instance):
    assert isinstance(instance, fiacre::NatLiteral)

@given(instance=fiacre::NatLiteral_strategy)
def test_fiacre::natliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fiacre::NatLiteral_strategy)
def test_fiacre::natliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fiacre::Queue_strategy)
@settings(max_examples=50)
def test_fiacre::queue_instantiation(instance):
    assert isinstance(instance, fiacre::Queue)

@given(instance=fiacre::Array_strategy)
@settings(max_examples=50)
def test_fiacre::array_instantiation(instance):
    assert isinstance(instance, fiacre::Array)

@given(instance=LabeledType_strategy)
@settings(max_examples=50)
def test_labeledtype_instantiation(instance):
    assert isinstance(instance, LabeledType)

@given(instance=fiacre::Constr_strategy)
@settings(max_examples=50)
def test_fiacre::constr_instantiation(instance):
    assert isinstance(instance, fiacre::Constr)

@given(instance=fiacre::Field_strategy)
@settings(max_examples=50)
def test_fiacre::field_instantiation(instance):
    assert isinstance(instance, fiacre::Field)

@given(instance=fiacre::Record_strategy)
@settings(max_examples=50)
def test_fiacre::record_instantiation(instance):
    assert isinstance(instance, fiacre::Record)

@given(instance=fiacre::Interval_strategy)
@settings(max_examples=50)
def test_fiacre::interval_instantiation(instance):
    assert isinstance(instance, fiacre::Interval)
