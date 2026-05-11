import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classifierTypeRule,
    ale::ClassifierType,
    Expression,
    ale::VarRef,
    ale::Comp,
    ale::Lit,
    ale::Not,
    ale::Let,
    ale::Min,
    ale::Feature,
    ale::Or,
    ale::Add,
    ale::Xor,
    ale::Conditional,
    ale::Implie,
    ale::Apply,
    ale::And,
    ale::Mult,
    ale::Call,
    typeLiteral,
    ale::StringType,
    ale::SetType,
    ale::SeqType,
    ale::IntType,
    ale::ClassifierSetType,
    ale::RealType,
    ale::BoolType,
    ale::classifierTypeRule,
    rType,
    literal,
    ale::String,
    ale::Sequence,
    ale::False,
    ale::OrderedSet,
    ale::Null,
    ale::True,
    ale::Enum,
    ale::Int,
    ale::Real,
    ale::literal,
    ale::typeLiteral,
    ale::binding,
    ale::EObject,
    ale::rCase,
    ale::rSwitch,
    ale::Collection,
    ale::Expression,
    Statement,
    ale::If,
    ale::Assign,
    ale::While,
    ale::ForEach,
    ale::Remove,
    ale::Insert,
    ale::VarDecl,
    ale::Statement,
    ale::ExpressionStmt,
    ale::rOpposite,
    ale::Block,
    ale::Variable,
    ale::rType,
    ale::Tag,
    BehavioredClass,
    ale::RuntimeClass,
    ale::ExtendedClass,
    ale::Operation,
    ale::Attribute,
    ale::BehavioredClass,
    ale::Service,
    ale::Import,
    ale::Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifiertyperule_is_not_abstract():
    assert not inspect.isabstract(classifierTypeRule)


def test_classifiertyperule_constructor_exists():
    assert callable(classifierTypeRule.__init__)


def test_classifiertyperule_constructor_args():
    sig = inspect.signature(classifierTypeRule.__init__)
    params = list(sig.parameters.keys())



def test_ale::classifiertype_is_not_abstract():
    assert not inspect.isabstract(ale::ClassifierType)


def test_ale::classifiertype_constructor_exists():
    assert callable(ale::ClassifierType.__init__)


def test_ale::classifiertype_constructor_args():
    sig = inspect.signature(ale::ClassifierType.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_ale::classifiertype_has_className():
    assert hasattr(ale::ClassifierType, "className")
    descriptor = None
    for klass in ale::ClassifierType.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_ale::classifiertype_has_packageName():
    assert hasattr(ale::ClassifierType, "packageName")
    descriptor = None
    for klass in ale::ClassifierType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ale::varref_is_not_abstract():
    assert not inspect.isabstract(ale::VarRef)


def test_ale::varref_constructor_exists():
    assert callable(ale::VarRef.__init__)


def test_ale::varref_constructor_args():
    sig = inspect.signature(ale::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_ale::varref_has_ID():
    assert hasattr(ale::VarRef, "ID")
    descriptor = None
    for klass in ale::VarRef.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_ale::comp_is_not_abstract():
    assert not inspect.isabstract(ale::Comp)


def test_ale::comp_constructor_exists():
    assert callable(ale::Comp.__init__)


def test_ale::comp_constructor_args():
    sig = inspect.signature(ale::Comp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ale::comp_has_op():
    assert hasattr(ale::Comp, "op")
    descriptor = None
    for klass in ale::Comp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ale::lit_is_not_abstract():
    assert not inspect.isabstract(ale::Lit)


def test_ale::lit_constructor_exists():
    assert callable(ale::Lit.__init__)


def test_ale::lit_constructor_args():
    sig = inspect.signature(ale::Lit.__init__)
    params = list(sig.parameters.keys())



def test_ale::not_is_not_abstract():
    assert not inspect.isabstract(ale::Not)


def test_ale::not_constructor_exists():
    assert callable(ale::Not.__init__)


def test_ale::not_constructor_args():
    sig = inspect.signature(ale::Not.__init__)
    params = list(sig.parameters.keys())



def test_ale::let_is_not_abstract():
    assert not inspect.isabstract(ale::Let)


def test_ale::let_constructor_exists():
    assert callable(ale::Let.__init__)


def test_ale::let_constructor_args():
    sig = inspect.signature(ale::Let.__init__)
    params = list(sig.parameters.keys())



def test_ale::min_is_not_abstract():
    assert not inspect.isabstract(ale::Min)


def test_ale::min_constructor_exists():
    assert callable(ale::Min.__init__)


def test_ale::min_constructor_args():
    sig = inspect.signature(ale::Min.__init__)
    params = list(sig.parameters.keys())



def test_ale::feature_is_not_abstract():
    assert not inspect.isabstract(ale::Feature)


def test_ale::feature_constructor_exists():
    assert callable(ale::Feature.__init__)


def test_ale::feature_constructor_args():
    sig = inspect.signature(ale::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_ale::feature_has_feature():
    assert hasattr(ale::Feature, "feature")
    descriptor = None
    for klass in ale::Feature.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_ale::or_is_not_abstract():
    assert not inspect.isabstract(ale::Or)


def test_ale::or_constructor_exists():
    assert callable(ale::Or.__init__)


def test_ale::or_constructor_args():
    sig = inspect.signature(ale::Or.__init__)
    params = list(sig.parameters.keys())



def test_ale::add_is_not_abstract():
    assert not inspect.isabstract(ale::Add)


def test_ale::add_constructor_exists():
    assert callable(ale::Add.__init__)


def test_ale::add_constructor_args():
    sig = inspect.signature(ale::Add.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ale::add_has_op():
    assert hasattr(ale::Add, "op")
    descriptor = None
    for klass in ale::Add.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ale::xor_is_not_abstract():
    assert not inspect.isabstract(ale::Xor)


def test_ale::xor_constructor_exists():
    assert callable(ale::Xor.__init__)


def test_ale::xor_constructor_args():
    sig = inspect.signature(ale::Xor.__init__)
    params = list(sig.parameters.keys())



def test_ale::conditional_is_not_abstract():
    assert not inspect.isabstract(ale::Conditional)


def test_ale::conditional_constructor_exists():
    assert callable(ale::Conditional.__init__)


def test_ale::conditional_constructor_args():
    sig = inspect.signature(ale::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_ale::implie_is_not_abstract():
    assert not inspect.isabstract(ale::Implie)


def test_ale::implie_constructor_exists():
    assert callable(ale::Implie.__init__)


def test_ale::implie_constructor_args():
    sig = inspect.signature(ale::Implie.__init__)
    params = list(sig.parameters.keys())



def test_ale::apply_is_not_abstract():
    assert not inspect.isabstract(ale::Apply)


def test_ale::apply_constructor_exists():
    assert callable(ale::Apply.__init__)


def test_ale::apply_constructor_args():
    sig = inspect.signature(ale::Apply.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ale::apply_has_varName():
    assert hasattr(ale::Apply, "varName")
    descriptor = None
    for klass in ale::Apply.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_ale::apply_has_name():
    assert hasattr(ale::Apply, "name")
    descriptor = None
    for klass in ale::Apply.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::and_is_not_abstract():
    assert not inspect.isabstract(ale::And)


def test_ale::and_constructor_exists():
    assert callable(ale::And.__init__)


def test_ale::and_constructor_args():
    sig = inspect.signature(ale::And.__init__)
    params = list(sig.parameters.keys())



def test_ale::mult_is_not_abstract():
    assert not inspect.isabstract(ale::Mult)


def test_ale::mult_constructor_exists():
    assert callable(ale::Mult.__init__)


def test_ale::mult_constructor_args():
    sig = inspect.signature(ale::Mult.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ale::mult_has_op():
    assert hasattr(ale::Mult, "op")
    descriptor = None
    for klass in ale::Mult.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ale::call_is_not_abstract():
    assert not inspect.isabstract(ale::Call)


def test_ale::call_constructor_exists():
    assert callable(ale::Call.__init__)


def test_ale::call_constructor_args():
    sig = inspect.signature(ale::Call.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::call_has_name():
    assert hasattr(ale::Call, "name")
    descriptor = None
    for klass in ale::Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeliteral_is_not_abstract():
    assert not inspect.isabstract(typeLiteral)


def test_typeliteral_constructor_exists():
    assert callable(typeLiteral.__init__)


def test_typeliteral_constructor_args():
    sig = inspect.signature(typeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ale::stringtype_is_not_abstract():
    assert not inspect.isabstract(ale::StringType)


def test_ale::stringtype_constructor_exists():
    assert callable(ale::StringType.__init__)


def test_ale::stringtype_constructor_args():
    sig = inspect.signature(ale::StringType.__init__)
    params = list(sig.parameters.keys())



def test_ale::settype_is_not_abstract():
    assert not inspect.isabstract(ale::SetType)


def test_ale::settype_constructor_exists():
    assert callable(ale::SetType.__init__)


def test_ale::settype_constructor_args():
    sig = inspect.signature(ale::SetType.__init__)
    params = list(sig.parameters.keys())



def test_ale::seqtype_is_not_abstract():
    assert not inspect.isabstract(ale::SeqType)


def test_ale::seqtype_constructor_exists():
    assert callable(ale::SeqType.__init__)


def test_ale::seqtype_constructor_args():
    sig = inspect.signature(ale::SeqType.__init__)
    params = list(sig.parameters.keys())



def test_ale::inttype_is_not_abstract():
    assert not inspect.isabstract(ale::IntType)


def test_ale::inttype_constructor_exists():
    assert callable(ale::IntType.__init__)


def test_ale::inttype_constructor_args():
    sig = inspect.signature(ale::IntType.__init__)
    params = list(sig.parameters.keys())



def test_ale::classifiersettype_is_not_abstract():
    assert not inspect.isabstract(ale::ClassifierSetType)


def test_ale::classifiersettype_constructor_exists():
    assert callable(ale::ClassifierSetType.__init__)


def test_ale::classifiersettype_constructor_args():
    sig = inspect.signature(ale::ClassifierSetType.__init__)
    params = list(sig.parameters.keys())



def test_ale::realtype_is_not_abstract():
    assert not inspect.isabstract(ale::RealType)


def test_ale::realtype_constructor_exists():
    assert callable(ale::RealType.__init__)


def test_ale::realtype_constructor_args():
    sig = inspect.signature(ale::RealType.__init__)
    params = list(sig.parameters.keys())



def test_ale::booltype_is_not_abstract():
    assert not inspect.isabstract(ale::BoolType)


def test_ale::booltype_constructor_exists():
    assert callable(ale::BoolType.__init__)


def test_ale::booltype_constructor_args():
    sig = inspect.signature(ale::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_ale::classifiertyperule_is_not_abstract():
    assert not inspect.isabstract(ale::classifierTypeRule)


def test_ale::classifiertyperule_constructor_exists():
    assert callable(ale::classifierTypeRule.__init__)


def test_ale::classifiertyperule_constructor_args():
    sig = inspect.signature(ale::classifierTypeRule.__init__)
    params = list(sig.parameters.keys())



def test_rtype_is_not_abstract():
    assert not inspect.isabstract(rType)


def test_rtype_constructor_exists():
    assert callable(rType.__init__)


def test_rtype_constructor_args():
    sig = inspect.signature(rType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(literal)


def test_literal_constructor_exists():
    assert callable(literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(literal.__init__)
    params = list(sig.parameters.keys())



def test_ale::string_is_not_abstract():
    assert not inspect.isabstract(ale::String)


def test_ale::string_constructor_exists():
    assert callable(ale::String.__init__)


def test_ale::string_constructor_args():
    sig = inspect.signature(ale::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale::string_has_value():
    assert hasattr(ale::String, "value")
    descriptor = None
    for klass in ale::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale::sequence_is_not_abstract():
    assert not inspect.isabstract(ale::Sequence)


def test_ale::sequence_constructor_exists():
    assert callable(ale::Sequence.__init__)


def test_ale::sequence_constructor_args():
    sig = inspect.signature(ale::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_ale::false_is_not_abstract():
    assert not inspect.isabstract(ale::False)


def test_ale::false_constructor_exists():
    assert callable(ale::False.__init__)


def test_ale::false_constructor_args():
    sig = inspect.signature(ale::False.__init__)
    params = list(sig.parameters.keys())



def test_ale::orderedset_is_not_abstract():
    assert not inspect.isabstract(ale::OrderedSet)


def test_ale::orderedset_constructor_exists():
    assert callable(ale::OrderedSet.__init__)


def test_ale::orderedset_constructor_args():
    sig = inspect.signature(ale::OrderedSet.__init__)
    params = list(sig.parameters.keys())



def test_ale::null_is_not_abstract():
    assert not inspect.isabstract(ale::Null)


def test_ale::null_constructor_exists():
    assert callable(ale::Null.__init__)


def test_ale::null_constructor_args():
    sig = inspect.signature(ale::Null.__init__)
    params = list(sig.parameters.keys())



def test_ale::true_is_not_abstract():
    assert not inspect.isabstract(ale::True)


def test_ale::true_constructor_exists():
    assert callable(ale::True.__init__)


def test_ale::true_constructor_args():
    sig = inspect.signature(ale::True.__init__)
    params = list(sig.parameters.keys())



def test_ale::enum_is_not_abstract():
    assert not inspect.isabstract(ale::Enum)


def test_ale::enum_constructor_exists():
    assert callable(ale::Enum.__init__)


def test_ale::enum_constructor_args():
    sig = inspect.signature(ale::Enum.__init__)
    params = list(sig.parameters.keys())



def test_ale::int_is_not_abstract():
    assert not inspect.isabstract(ale::Int)


def test_ale::int_constructor_exists():
    assert callable(ale::Int.__init__)


def test_ale::int_constructor_args():
    sig = inspect.signature(ale::Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale::int_has_value():
    assert hasattr(ale::Int, "value")
    descriptor = None
    for klass in ale::Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale::real_is_not_abstract():
    assert not inspect.isabstract(ale::Real)


def test_ale::real_constructor_exists():
    assert callable(ale::Real.__init__)


def test_ale::real_constructor_args():
    sig = inspect.signature(ale::Real.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale::real_has_value():
    assert hasattr(ale::Real, "value")
    descriptor = None
    for klass in ale::Real.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale::literal_is_not_abstract():
    assert not inspect.isabstract(ale::literal)


def test_ale::literal_constructor_exists():
    assert callable(ale::literal.__init__)


def test_ale::literal_constructor_args():
    sig = inspect.signature(ale::literal.__init__)
    params = list(sig.parameters.keys())



def test_ale::typeliteral_is_not_abstract():
    assert not inspect.isabstract(ale::typeLiteral)


def test_ale::typeliteral_constructor_exists():
    assert callable(ale::typeLiteral.__init__)


def test_ale::typeliteral_constructor_args():
    sig = inspect.signature(ale::typeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ale::binding_is_not_abstract():
    assert not inspect.isabstract(ale::binding)


def test_ale::binding_constructor_exists():
    assert callable(ale::binding.__init__)


def test_ale::binding_constructor_args():
    sig = inspect.signature(ale::binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::binding_has_name():
    assert hasattr(ale::binding, "name")
    descriptor = None
    for klass in ale::binding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::eobject_is_not_abstract():
    assert not inspect.isabstract(ale::EObject)


def test_ale::eobject_constructor_exists():
    assert callable(ale::EObject.__init__)


def test_ale::eobject_constructor_args():
    sig = inspect.signature(ale::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ale::rcase_is_not_abstract():
    assert not inspect.isabstract(ale::rCase)


def test_ale::rcase_constructor_exists():
    assert callable(ale::rCase.__init__)


def test_ale::rcase_constructor_args():
    sig = inspect.signature(ale::rCase.__init__)
    params = list(sig.parameters.keys())



def test_ale::rswitch_is_not_abstract():
    assert not inspect.isabstract(ale::rSwitch)


def test_ale::rswitch_constructor_exists():
    assert callable(ale::rSwitch.__init__)


def test_ale::rswitch_constructor_args():
    sig = inspect.signature(ale::rSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "paramName" in params, "Missing parameter 'paramName'"

def test_ale::rswitch_has_paramName():
    assert hasattr(ale::rSwitch, "paramName")
    descriptor = None
    for klass in ale::rSwitch.__mro__:
        if "paramName" in klass.__dict__:
            descriptor = klass.__dict__["paramName"]
            break
    assert isinstance(descriptor, property)



def test_ale::collection_is_not_abstract():
    assert not inspect.isabstract(ale::Collection)


def test_ale::collection_constructor_exists():
    assert callable(ale::Collection.__init__)


def test_ale::collection_constructor_args():
    sig = inspect.signature(ale::Collection.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_ale::collection_has_min():
    assert hasattr(ale::Collection, "min")
    descriptor = None
    for klass in ale::Collection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ale::collection_has_max():
    assert hasattr(ale::Collection, "max")
    descriptor = None
    for klass in ale::Collection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_ale::expression_is_not_abstract():
    assert not inspect.isabstract(ale::Expression)


def test_ale::expression_constructor_exists():
    assert callable(ale::Expression.__init__)


def test_ale::expression_constructor_args():
    sig = inspect.signature(ale::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ale::if_is_not_abstract():
    assert not inspect.isabstract(ale::If)


def test_ale::if_constructor_exists():
    assert callable(ale::If.__init__)


def test_ale::if_constructor_args():
    sig = inspect.signature(ale::If.__init__)
    params = list(sig.parameters.keys())



def test_ale::assign_is_not_abstract():
    assert not inspect.isabstract(ale::Assign)


def test_ale::assign_constructor_exists():
    assert callable(ale::Assign.__init__)


def test_ale::assign_constructor_args():
    sig = inspect.signature(ale::Assign.__init__)
    params = list(sig.parameters.keys())



def test_ale::while_is_not_abstract():
    assert not inspect.isabstract(ale::While)


def test_ale::while_constructor_exists():
    assert callable(ale::While.__init__)


def test_ale::while_constructor_args():
    sig = inspect.signature(ale::While.__init__)
    params = list(sig.parameters.keys())



def test_ale::foreach_is_not_abstract():
    assert not inspect.isabstract(ale::ForEach)


def test_ale::foreach_constructor_exists():
    assert callable(ale::ForEach.__init__)


def test_ale::foreach_constructor_args():
    sig = inspect.signature(ale::ForEach.__init__)
    params = list(sig.parameters.keys())
    assert "iterator" in params, "Missing parameter 'iterator'"

def test_ale::foreach_has_iterator():
    assert hasattr(ale::ForEach, "iterator")
    descriptor = None
    for klass in ale::ForEach.__mro__:
        if "iterator" in klass.__dict__:
            descriptor = klass.__dict__["iterator"]
            break
    assert isinstance(descriptor, property)



def test_ale::remove_is_not_abstract():
    assert not inspect.isabstract(ale::Remove)


def test_ale::remove_constructor_exists():
    assert callable(ale::Remove.__init__)


def test_ale::remove_constructor_args():
    sig = inspect.signature(ale::Remove.__init__)
    params = list(sig.parameters.keys())



def test_ale::insert_is_not_abstract():
    assert not inspect.isabstract(ale::Insert)


def test_ale::insert_constructor_exists():
    assert callable(ale::Insert.__init__)


def test_ale::insert_constructor_args():
    sig = inspect.signature(ale::Insert.__init__)
    params = list(sig.parameters.keys())



def test_ale::vardecl_is_not_abstract():
    assert not inspect.isabstract(ale::VarDecl)


def test_ale::vardecl_constructor_exists():
    assert callable(ale::VarDecl.__init__)


def test_ale::vardecl_constructor_args():
    sig = inspect.signature(ale::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::vardecl_has_name():
    assert hasattr(ale::VarDecl, "name")
    descriptor = None
    for klass in ale::VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::statement_is_not_abstract():
    assert not inspect.isabstract(ale::Statement)


def test_ale::statement_constructor_exists():
    assert callable(ale::Statement.__init__)


def test_ale::statement_constructor_args():
    sig = inspect.signature(ale::Statement.__init__)
    params = list(sig.parameters.keys())



def test_ale::expressionstmt_is_not_abstract():
    assert not inspect.isabstract(ale::ExpressionStmt)


def test_ale::expressionstmt_constructor_exists():
    assert callable(ale::ExpressionStmt.__init__)


def test_ale::expressionstmt_constructor_args():
    sig = inspect.signature(ale::ExpressionStmt.__init__)
    params = list(sig.parameters.keys())



def test_ale::ropposite_is_not_abstract():
    assert not inspect.isabstract(ale::rOpposite)


def test_ale::ropposite_constructor_exists():
    assert callable(ale::rOpposite.__init__)


def test_ale::ropposite_constructor_args():
    sig = inspect.signature(ale::rOpposite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::ropposite_has_name():
    assert hasattr(ale::rOpposite, "name")
    descriptor = None
    for klass in ale::rOpposite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::block_is_not_abstract():
    assert not inspect.isabstract(ale::Block)


def test_ale::block_constructor_exists():
    assert callable(ale::Block.__init__)


def test_ale::block_constructor_args():
    sig = inspect.signature(ale::Block.__init__)
    params = list(sig.parameters.keys())



def test_ale::variable_is_not_abstract():
    assert not inspect.isabstract(ale::Variable)


def test_ale::variable_constructor_exists():
    assert callable(ale::Variable.__init__)


def test_ale::variable_constructor_args():
    sig = inspect.signature(ale::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::variable_has_name():
    assert hasattr(ale::Variable, "name")
    descriptor = None
    for klass in ale::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::rtype_is_not_abstract():
    assert not inspect.isabstract(ale::rType)


def test_ale::rtype_constructor_exists():
    assert callable(ale::rType.__init__)


def test_ale::rtype_constructor_args():
    sig = inspect.signature(ale::rType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::rtype_has_name():
    assert hasattr(ale::rType, "name")
    descriptor = None
    for klass in ale::rType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::tag_is_not_abstract():
    assert not inspect.isabstract(ale::Tag)


def test_ale::tag_constructor_exists():
    assert callable(ale::Tag.__init__)


def test_ale::tag_constructor_args():
    sig = inspect.signature(ale::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::tag_has_name():
    assert hasattr(ale::Tag, "name")
    descriptor = None
    for klass in ale::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behavioredclass_is_not_abstract():
    assert not inspect.isabstract(BehavioredClass)


def test_behavioredclass_constructor_exists():
    assert callable(BehavioredClass.__init__)


def test_behavioredclass_constructor_args():
    sig = inspect.signature(BehavioredClass.__init__)
    params = list(sig.parameters.keys())



def test_ale::runtimeclass_is_not_abstract():
    assert not inspect.isabstract(ale::RuntimeClass)


def test_ale::runtimeclass_constructor_exists():
    assert callable(ale::RuntimeClass.__init__)


def test_ale::runtimeclass_constructor_args():
    sig = inspect.signature(ale::RuntimeClass.__init__)
    params = list(sig.parameters.keys())



def test_ale::extendedclass_is_not_abstract():
    assert not inspect.isabstract(ale::ExtendedClass)


def test_ale::extendedclass_constructor_exists():
    assert callable(ale::ExtendedClass.__init__)


def test_ale::extendedclass_constructor_args():
    sig = inspect.signature(ale::ExtendedClass.__init__)
    params = list(sig.parameters.keys())
    assert "extends" in params, "Missing parameter 'extends'"

def test_ale::extendedclass_has_extends():
    assert hasattr(ale::ExtendedClass, "extends")
    descriptor = None
    for klass in ale::ExtendedClass.__mro__:
        if "extends" in klass.__dict__:
            descriptor = klass.__dict__["extends"]
            break
    assert isinstance(descriptor, property)



def test_ale::operation_is_not_abstract():
    assert not inspect.isabstract(ale::Operation)


def test_ale::operation_constructor_exists():
    assert callable(ale::Operation.__init__)


def test_ale::operation_constructor_args():
    sig = inspect.signature(ale::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::operation_has_name():
    assert hasattr(ale::Operation, "name")
    descriptor = None
    for klass in ale::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::attribute_is_not_abstract():
    assert not inspect.isabstract(ale::Attribute)


def test_ale::attribute_constructor_exists():
    assert callable(ale::Attribute.__init__)


def test_ale::attribute_constructor_args():
    sig = inspect.signature(ale::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_ale::attribute_has_name():
    assert hasattr(ale::Attribute, "name")
    descriptor = None
    for klass in ale::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ale::attribute_has_bounds():
    assert hasattr(ale::Attribute, "bounds")
    descriptor = None
    for klass in ale::Attribute.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_ale::attribute_has_modifier():
    assert hasattr(ale::Attribute, "modifier")
    descriptor = None
    for klass in ale::Attribute.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_ale::behavioredclass_is_not_abstract():
    assert not inspect.isabstract(ale::BehavioredClass)


def test_ale::behavioredclass_constructor_exists():
    assert callable(ale::BehavioredClass.__init__)


def test_ale::behavioredclass_constructor_args():
    sig = inspect.signature(ale::BehavioredClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::behavioredclass_has_name():
    assert hasattr(ale::BehavioredClass, "name")
    descriptor = None
    for klass in ale::BehavioredClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::service_is_not_abstract():
    assert not inspect.isabstract(ale::Service)


def test_ale::service_constructor_exists():
    assert callable(ale::Service.__init__)


def test_ale::service_constructor_args():
    sig = inspect.signature(ale::Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::service_has_name():
    assert hasattr(ale::Service, "name")
    descriptor = None
    for klass in ale::Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale::import_is_not_abstract():
    assert not inspect.isabstract(ale::Import)


def test_ale::import_constructor_exists():
    assert callable(ale::Import.__init__)


def test_ale::import_constructor_args():
    sig = inspect.signature(ale::Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_ale::import_has_name():
    assert hasattr(ale::Import, "name")
    descriptor = None
    for klass in ale::Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ale::import_has_alias():
    assert hasattr(ale::Import, "alias")
    descriptor = None
    for klass in ale::Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_ale::unit_is_not_abstract():
    assert not inspect.isabstract(ale::Unit)


def test_ale::unit_constructor_exists():
    assert callable(ale::Unit.__init__)


def test_ale::unit_constructor_args():
    sig = inspect.signature(ale::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale::unit_has_name():
    assert hasattr(ale::Unit, "name")
    descriptor = None
    for klass in ale::Unit.__mro__:
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
classifierTypeRule_strategy = st.builds(
    classifierTypeRule,
)
ale::ClassifierType_strategy = st.builds(
    ale::ClassifierType,
    className=
        safe_text,
    packageName=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ale::VarRef_strategy = st.builds(
    ale::VarRef,
    ID=
        safe_text
)
ale::Comp_strategy = st.builds(
    ale::Comp,
    op=
        safe_text
)
ale::Lit_strategy = st.builds(
    ale::Lit,
)
ale::Not_strategy = st.builds(
    ale::Not,
)
ale::Let_strategy = st.builds(
    ale::Let,
)
ale::Min_strategy = st.builds(
    ale::Min,
)
ale::Feature_strategy = st.builds(
    ale::Feature,
    feature=
        safe_text
)
ale::Or_strategy = st.builds(
    ale::Or,
)
ale::Add_strategy = st.builds(
    ale::Add,
    op=
        safe_text
)
ale::Xor_strategy = st.builds(
    ale::Xor,
)
ale::Conditional_strategy = st.builds(
    ale::Conditional,
)
ale::Implie_strategy = st.builds(
    ale::Implie,
)
ale::Apply_strategy = st.builds(
    ale::Apply,
    varName=
        safe_text,
    name=
        safe_text
)
ale::And_strategy = st.builds(
    ale::And,
)
ale::Mult_strategy = st.builds(
    ale::Mult,
    op=
        safe_text
)
ale::Call_strategy = st.builds(
    ale::Call,
    name=
        safe_text
)
typeLiteral_strategy = st.builds(
    typeLiteral,
)
ale::StringType_strategy = st.builds(
    ale::StringType,
)
ale::SetType_strategy = st.builds(
    ale::SetType,
)
ale::SeqType_strategy = st.builds(
    ale::SeqType,
)
ale::IntType_strategy = st.builds(
    ale::IntType,
)
ale::ClassifierSetType_strategy = st.builds(
    ale::ClassifierSetType,
)
ale::RealType_strategy = st.builds(
    ale::RealType,
)
ale::BoolType_strategy = st.builds(
    ale::BoolType,
)
ale::classifierTypeRule_strategy = st.builds(
    ale::classifierTypeRule,
)
rType_strategy = st.builds(
    rType,
)
literal_strategy = st.builds(
    literal,
)
ale::String_strategy = st.builds(
    ale::String,
    value=
        safe_text
)
ale::Sequence_strategy = st.builds(
    ale::Sequence,
)
ale::False_strategy = st.builds(
    ale::False,
)
ale::OrderedSet_strategy = st.builds(
    ale::OrderedSet,
)
ale::Null_strategy = st.builds(
    ale::Null,
)
ale::True_strategy = st.builds(
    ale::True,
)
ale::Enum_strategy = st.builds(
    ale::Enum,
)
ale::Int_strategy = st.builds(
    ale::Int,
    value=
        st.integers()
)
ale::Real_strategy = st.builds(
    ale::Real,
    value=
        safe_text
)
ale::literal_strategy = st.builds(
    ale::literal,
)
ale::typeLiteral_strategy = st.builds(
    ale::typeLiteral,
)
ale::binding_strategy = st.builds(
    ale::binding,
    name=
        safe_text
)
ale::EObject_strategy = st.builds(
    ale::EObject,
)
ale::rCase_strategy = st.builds(
    ale::rCase,
)
ale::rSwitch_strategy = st.builds(
    ale::rSwitch,
    paramName=
        safe_text
)
ale::Collection_strategy = st.builds(
    ale::Collection,
    min=
        st.integers(),
    max=
        st.integers()
)
ale::Expression_strategy = st.builds(
    ale::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
ale::If_strategy = st.builds(
    ale::If,
)
ale::Assign_strategy = st.builds(
    ale::Assign,
)
ale::While_strategy = st.builds(
    ale::While,
)
ale::ForEach_strategy = st.builds(
    ale::ForEach,
    iterator=
        safe_text
)
ale::Remove_strategy = st.builds(
    ale::Remove,
)
ale::Insert_strategy = st.builds(
    ale::Insert,
)
ale::VarDecl_strategy = st.builds(
    ale::VarDecl,
    name=
        safe_text
)
ale::Statement_strategy = st.builds(
    ale::Statement,
)
ale::ExpressionStmt_strategy = st.builds(
    ale::ExpressionStmt,
)
ale::rOpposite_strategy = st.builds(
    ale::rOpposite,
    name=
        safe_text
)
ale::Block_strategy = st.builds(
    ale::Block,
)
ale::Variable_strategy = st.builds(
    ale::Variable,
    name=
        safe_text
)
ale::rType_strategy = st.builds(
    ale::rType,
    name=
        safe_text
)
ale::Tag_strategy = st.builds(
    ale::Tag,
    name=
        safe_text
)
BehavioredClass_strategy = st.builds(
    BehavioredClass,
)
ale::RuntimeClass_strategy = st.builds(
    ale::RuntimeClass,
)
ale::ExtendedClass_strategy = st.builds(
    ale::ExtendedClass,
    extends=
        safe_text
)
ale::Operation_strategy = st.builds(
    ale::Operation,
    name=
        safe_text
)
ale::Attribute_strategy = st.builds(
    ale::Attribute,
    name=
        safe_text,
    bounds=
        safe_text,
    modifier=
        safe_text
)
ale::BehavioredClass_strategy = st.builds(
    ale::BehavioredClass,
    name=
        safe_text
)
ale::Service_strategy = st.builds(
    ale::Service,
    name=
        safe_text
)
ale::Import_strategy = st.builds(
    ale::Import,
    name=
        safe_text,
    alias=
        safe_text
)
ale::Unit_strategy = st.builds(
    ale::Unit,
    name=
        safe_text
)

@given(instance=classifierTypeRule_strategy)
@settings(max_examples=50)
def test_classifiertyperule_instantiation(instance):
    assert isinstance(instance, classifierTypeRule)

@given(instance=ale::ClassifierType_strategy)
@settings(max_examples=50)
def test_ale::classifiertype_instantiation(instance):
    assert isinstance(instance, ale::ClassifierType)

@given(instance=ale::ClassifierType_strategy)
def test_ale::classifiertype_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=ale::ClassifierType_strategy)
def test_ale::classifiertype_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=ale::ClassifierType_strategy)
def test_ale::classifiertype_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=ale::ClassifierType_strategy)
def test_ale::classifiertype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ale::VarRef_strategy)
@settings(max_examples=50)
def test_ale::varref_instantiation(instance):
    assert isinstance(instance, ale::VarRef)

@given(instance=ale::VarRef_strategy)
def test_ale::varref_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=ale::VarRef_strategy)
def test_ale::varref_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ale::Comp_strategy)
@settings(max_examples=50)
def test_ale::comp_instantiation(instance):
    assert isinstance(instance, ale::Comp)

@given(instance=ale::Comp_strategy)
def test_ale::comp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=ale::Comp_strategy)
def test_ale::comp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ale::Lit_strategy)
@settings(max_examples=50)
def test_ale::lit_instantiation(instance):
    assert isinstance(instance, ale::Lit)

@given(instance=ale::Not_strategy)
@settings(max_examples=50)
def test_ale::not_instantiation(instance):
    assert isinstance(instance, ale::Not)

@given(instance=ale::Let_strategy)
@settings(max_examples=50)
def test_ale::let_instantiation(instance):
    assert isinstance(instance, ale::Let)

@given(instance=ale::Min_strategy)
@settings(max_examples=50)
def test_ale::min_instantiation(instance):
    assert isinstance(instance, ale::Min)

@given(instance=ale::Feature_strategy)
@settings(max_examples=50)
def test_ale::feature_instantiation(instance):
    assert isinstance(instance, ale::Feature)

@given(instance=ale::Feature_strategy)
def test_ale::feature_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=ale::Feature_strategy)
def test_ale::feature_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=ale::Or_strategy)
@settings(max_examples=50)
def test_ale::or_instantiation(instance):
    assert isinstance(instance, ale::Or)

@given(instance=ale::Add_strategy)
@settings(max_examples=50)
def test_ale::add_instantiation(instance):
    assert isinstance(instance, ale::Add)

@given(instance=ale::Add_strategy)
def test_ale::add_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=ale::Add_strategy)
def test_ale::add_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ale::Xor_strategy)
@settings(max_examples=50)
def test_ale::xor_instantiation(instance):
    assert isinstance(instance, ale::Xor)

@given(instance=ale::Conditional_strategy)
@settings(max_examples=50)
def test_ale::conditional_instantiation(instance):
    assert isinstance(instance, ale::Conditional)

@given(instance=ale::Implie_strategy)
@settings(max_examples=50)
def test_ale::implie_instantiation(instance):
    assert isinstance(instance, ale::Implie)

@given(instance=ale::Apply_strategy)
@settings(max_examples=50)
def test_ale::apply_instantiation(instance):
    assert isinstance(instance, ale::Apply)

@given(instance=ale::Apply_strategy)
def test_ale::apply_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=ale::Apply_strategy)
def test_ale::apply_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=ale::Apply_strategy)
def test_ale::apply_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Apply_strategy)
def test_ale::apply_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::And_strategy)
@settings(max_examples=50)
def test_ale::and_instantiation(instance):
    assert isinstance(instance, ale::And)

@given(instance=ale::Mult_strategy)
@settings(max_examples=50)
def test_ale::mult_instantiation(instance):
    assert isinstance(instance, ale::Mult)

@given(instance=ale::Mult_strategy)
def test_ale::mult_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=ale::Mult_strategy)
def test_ale::mult_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ale::Call_strategy)
@settings(max_examples=50)
def test_ale::call_instantiation(instance):
    assert isinstance(instance, ale::Call)

@given(instance=ale::Call_strategy)
def test_ale::call_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Call_strategy)
def test_ale::call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeLiteral_strategy)
@settings(max_examples=50)
def test_typeliteral_instantiation(instance):
    assert isinstance(instance, typeLiteral)

@given(instance=ale::StringType_strategy)
@settings(max_examples=50)
def test_ale::stringtype_instantiation(instance):
    assert isinstance(instance, ale::StringType)

@given(instance=ale::SetType_strategy)
@settings(max_examples=50)
def test_ale::settype_instantiation(instance):
    assert isinstance(instance, ale::SetType)

@given(instance=ale::SeqType_strategy)
@settings(max_examples=50)
def test_ale::seqtype_instantiation(instance):
    assert isinstance(instance, ale::SeqType)

@given(instance=ale::IntType_strategy)
@settings(max_examples=50)
def test_ale::inttype_instantiation(instance):
    assert isinstance(instance, ale::IntType)

@given(instance=ale::ClassifierSetType_strategy)
@settings(max_examples=50)
def test_ale::classifiersettype_instantiation(instance):
    assert isinstance(instance, ale::ClassifierSetType)

@given(instance=ale::RealType_strategy)
@settings(max_examples=50)
def test_ale::realtype_instantiation(instance):
    assert isinstance(instance, ale::RealType)

@given(instance=ale::BoolType_strategy)
@settings(max_examples=50)
def test_ale::booltype_instantiation(instance):
    assert isinstance(instance, ale::BoolType)

@given(instance=ale::classifierTypeRule_strategy)
@settings(max_examples=50)
def test_ale::classifiertyperule_instantiation(instance):
    assert isinstance(instance, ale::classifierTypeRule)

@given(instance=rType_strategy)
@settings(max_examples=50)
def test_rtype_instantiation(instance):
    assert isinstance(instance, rType)

@given(instance=literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, literal)

@given(instance=ale::String_strategy)
@settings(max_examples=50)
def test_ale::string_instantiation(instance):
    assert isinstance(instance, ale::String)

@given(instance=ale::String_strategy)
def test_ale::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ale::String_strategy)
def test_ale::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale::Sequence_strategy)
@settings(max_examples=50)
def test_ale::sequence_instantiation(instance):
    assert isinstance(instance, ale::Sequence)

@given(instance=ale::False_strategy)
@settings(max_examples=50)
def test_ale::false_instantiation(instance):
    assert isinstance(instance, ale::False)

@given(instance=ale::OrderedSet_strategy)
@settings(max_examples=50)
def test_ale::orderedset_instantiation(instance):
    assert isinstance(instance, ale::OrderedSet)

@given(instance=ale::Null_strategy)
@settings(max_examples=50)
def test_ale::null_instantiation(instance):
    assert isinstance(instance, ale::Null)

@given(instance=ale::True_strategy)
@settings(max_examples=50)
def test_ale::true_instantiation(instance):
    assert isinstance(instance, ale::True)

@given(instance=ale::Enum_strategy)
@settings(max_examples=50)
def test_ale::enum_instantiation(instance):
    assert isinstance(instance, ale::Enum)

@given(instance=ale::Int_strategy)
@settings(max_examples=50)
def test_ale::int_instantiation(instance):
    assert isinstance(instance, ale::Int)

@given(instance=ale::Int_strategy)
def test_ale::int_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ale::Int_strategy)
def test_ale::int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale::Real_strategy)
@settings(max_examples=50)
def test_ale::real_instantiation(instance):
    assert isinstance(instance, ale::Real)

@given(instance=ale::Real_strategy)
def test_ale::real_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ale::Real_strategy)
def test_ale::real_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale::literal_strategy)
@settings(max_examples=50)
def test_ale::literal_instantiation(instance):
    assert isinstance(instance, ale::literal)

@given(instance=ale::typeLiteral_strategy)
@settings(max_examples=50)
def test_ale::typeliteral_instantiation(instance):
    assert isinstance(instance, ale::typeLiteral)

@given(instance=ale::binding_strategy)
@settings(max_examples=50)
def test_ale::binding_instantiation(instance):
    assert isinstance(instance, ale::binding)

@given(instance=ale::binding_strategy)
def test_ale::binding_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::binding_strategy)
def test_ale::binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::EObject_strategy)
@settings(max_examples=50)
def test_ale::eobject_instantiation(instance):
    assert isinstance(instance, ale::EObject)

@given(instance=ale::rCase_strategy)
@settings(max_examples=50)
def test_ale::rcase_instantiation(instance):
    assert isinstance(instance, ale::rCase)

@given(instance=ale::rSwitch_strategy)
@settings(max_examples=50)
def test_ale::rswitch_instantiation(instance):
    assert isinstance(instance, ale::rSwitch)

@given(instance=ale::rSwitch_strategy)
def test_ale::rswitch_paramName_type(instance):
    assert isinstance(instance.paramName, str)


@given(instance=ale::rSwitch_strategy)
def test_ale::rswitch_paramName_setter(instance):
    original = instance.paramName
    instance.paramName = original
    assert instance.paramName == original

@given(instance=ale::Collection_strategy)
@settings(max_examples=50)
def test_ale::collection_instantiation(instance):
    assert isinstance(instance, ale::Collection)

@given(instance=ale::Collection_strategy)
def test_ale::collection_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=ale::Collection_strategy)
def test_ale::collection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=ale::Collection_strategy)
def test_ale::collection_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=ale::Collection_strategy)
def test_ale::collection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ale::Expression_strategy)
@settings(max_examples=50)
def test_ale::expression_instantiation(instance):
    assert isinstance(instance, ale::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ale::If_strategy)
@settings(max_examples=50)
def test_ale::if_instantiation(instance):
    assert isinstance(instance, ale::If)

@given(instance=ale::Assign_strategy)
@settings(max_examples=50)
def test_ale::assign_instantiation(instance):
    assert isinstance(instance, ale::Assign)

@given(instance=ale::While_strategy)
@settings(max_examples=50)
def test_ale::while_instantiation(instance):
    assert isinstance(instance, ale::While)

@given(instance=ale::ForEach_strategy)
@settings(max_examples=50)
def test_ale::foreach_instantiation(instance):
    assert isinstance(instance, ale::ForEach)

@given(instance=ale::ForEach_strategy)
def test_ale::foreach_iterator_type(instance):
    assert isinstance(instance.iterator, str)


@given(instance=ale::ForEach_strategy)
def test_ale::foreach_iterator_setter(instance):
    original = instance.iterator
    instance.iterator = original
    assert instance.iterator == original

@given(instance=ale::Remove_strategy)
@settings(max_examples=50)
def test_ale::remove_instantiation(instance):
    assert isinstance(instance, ale::Remove)

@given(instance=ale::Insert_strategy)
@settings(max_examples=50)
def test_ale::insert_instantiation(instance):
    assert isinstance(instance, ale::Insert)

@given(instance=ale::VarDecl_strategy)
@settings(max_examples=50)
def test_ale::vardecl_instantiation(instance):
    assert isinstance(instance, ale::VarDecl)

@given(instance=ale::VarDecl_strategy)
def test_ale::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::VarDecl_strategy)
def test_ale::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Statement_strategy)
@settings(max_examples=50)
def test_ale::statement_instantiation(instance):
    assert isinstance(instance, ale::Statement)

@given(instance=ale::ExpressionStmt_strategy)
@settings(max_examples=50)
def test_ale::expressionstmt_instantiation(instance):
    assert isinstance(instance, ale::ExpressionStmt)

@given(instance=ale::rOpposite_strategy)
@settings(max_examples=50)
def test_ale::ropposite_instantiation(instance):
    assert isinstance(instance, ale::rOpposite)

@given(instance=ale::rOpposite_strategy)
def test_ale::ropposite_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::rOpposite_strategy)
def test_ale::ropposite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Block_strategy)
@settings(max_examples=50)
def test_ale::block_instantiation(instance):
    assert isinstance(instance, ale::Block)

@given(instance=ale::Variable_strategy)
@settings(max_examples=50)
def test_ale::variable_instantiation(instance):
    assert isinstance(instance, ale::Variable)

@given(instance=ale::Variable_strategy)
def test_ale::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Variable_strategy)
def test_ale::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::rType_strategy)
@settings(max_examples=50)
def test_ale::rtype_instantiation(instance):
    assert isinstance(instance, ale::rType)

@given(instance=ale::rType_strategy)
def test_ale::rtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::rType_strategy)
def test_ale::rtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Tag_strategy)
@settings(max_examples=50)
def test_ale::tag_instantiation(instance):
    assert isinstance(instance, ale::Tag)

@given(instance=ale::Tag_strategy)
def test_ale::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Tag_strategy)
def test_ale::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BehavioredClass_strategy)
@settings(max_examples=50)
def test_behavioredclass_instantiation(instance):
    assert isinstance(instance, BehavioredClass)

@given(instance=ale::RuntimeClass_strategy)
@settings(max_examples=50)
def test_ale::runtimeclass_instantiation(instance):
    assert isinstance(instance, ale::RuntimeClass)

@given(instance=ale::ExtendedClass_strategy)
@settings(max_examples=50)
def test_ale::extendedclass_instantiation(instance):
    assert isinstance(instance, ale::ExtendedClass)

@given(instance=ale::ExtendedClass_strategy)
def test_ale::extendedclass_extends_type(instance):
    assert isinstance(instance.extends, str)


@given(instance=ale::ExtendedClass_strategy)
def test_ale::extendedclass_extends_setter(instance):
    original = instance.extends
    instance.extends = original
    assert instance.extends == original

@given(instance=ale::Operation_strategy)
@settings(max_examples=50)
def test_ale::operation_instantiation(instance):
    assert isinstance(instance, ale::Operation)

@given(instance=ale::Operation_strategy)
def test_ale::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Operation_strategy)
def test_ale::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Attribute_strategy)
@settings(max_examples=50)
def test_ale::attribute_instantiation(instance):
    assert isinstance(instance, ale::Attribute)

@given(instance=ale::Attribute_strategy)
def test_ale::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Attribute_strategy)
def test_ale::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Attribute_strategy)
def test_ale::attribute_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=ale::Attribute_strategy)
def test_ale::attribute_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=ale::Attribute_strategy)
def test_ale::attribute_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=ale::Attribute_strategy)
def test_ale::attribute_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=ale::BehavioredClass_strategy)
@settings(max_examples=50)
def test_ale::behavioredclass_instantiation(instance):
    assert isinstance(instance, ale::BehavioredClass)

@given(instance=ale::BehavioredClass_strategy)
def test_ale::behavioredclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::BehavioredClass_strategy)
def test_ale::behavioredclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Service_strategy)
@settings(max_examples=50)
def test_ale::service_instantiation(instance):
    assert isinstance(instance, ale::Service)

@given(instance=ale::Service_strategy)
def test_ale::service_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Service_strategy)
def test_ale::service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Import_strategy)
@settings(max_examples=50)
def test_ale::import_instantiation(instance):
    assert isinstance(instance, ale::Import)

@given(instance=ale::Import_strategy)
def test_ale::import_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Import_strategy)
def test_ale::import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale::Import_strategy)
def test_ale::import_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=ale::Import_strategy)
def test_ale::import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=ale::Unit_strategy)
@settings(max_examples=50)
def test_ale::unit_instantiation(instance):
    assert isinstance(instance, ale::Unit)

@given(instance=ale::Unit_strategy)
def test_ale::unit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ale::Unit_strategy)
def test_ale::unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
