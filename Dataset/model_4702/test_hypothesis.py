import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expr,
    paplj::Neq,
    paplj::Cast,
    paplj::Bool,
    paplj::New,
    paplj::Num,
    paplj::MemberRef,
    paplj::Div,
    paplj::Let,
    paplj::Eq,
    paplj::Mul,
    paplj::Null,
    paplj::Not,
    paplj::Sub,
    paplj::Min,
    paplj::If,
    paplj::Add,
    paplj::Lt,
    paplj::Var,
    paplj::This,
    paplj::And,
    paplj::Assignment,
    paplj::Or,
    paplj::Symbol,
    Symbol,
    paplj::Binding,
    paplj::Member,
    paplj::Expr,
    paplj::Type,
    paplj::Import,
    paplj::Program,
    paplj::Block2,
    paplj::Param,
    Member,
    paplj::Method,
    paplj::Field,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_paplj::neq_is_not_abstract():
    assert not inspect.isabstract(paplj::Neq)


def test_paplj::neq_constructor_exists():
    assert callable(paplj::Neq.__init__)


def test_paplj::neq_constructor_args():
    sig = inspect.signature(paplj::Neq.__init__)
    params = list(sig.parameters.keys())



def test_paplj::cast_is_not_abstract():
    assert not inspect.isabstract(paplj::Cast)


def test_paplj::cast_constructor_exists():
    assert callable(paplj::Cast.__init__)


def test_paplj::cast_constructor_args():
    sig = inspect.signature(paplj::Cast.__init__)
    params = list(sig.parameters.keys())



def test_paplj::bool_is_not_abstract():
    assert not inspect.isabstract(paplj::Bool)


def test_paplj::bool_constructor_exists():
    assert callable(paplj::Bool.__init__)


def test_paplj::bool_constructor_args():
    sig = inspect.signature(paplj::Bool.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"

def test_paplj::bool_has_true():
    assert hasattr(paplj::Bool, "true")
    descriptor = None
    for klass in paplj::Bool.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_paplj::new_is_not_abstract():
    assert not inspect.isabstract(paplj::New)


def test_paplj::new_constructor_exists():
    assert callable(paplj::New.__init__)


def test_paplj::new_constructor_args():
    sig = inspect.signature(paplj::New.__init__)
    params = list(sig.parameters.keys())



def test_paplj::num_is_not_abstract():
    assert not inspect.isabstract(paplj::Num)


def test_paplj::num_constructor_exists():
    assert callable(paplj::Num.__init__)


def test_paplj::num_constructor_args():
    sig = inspect.signature(paplj::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_paplj::num_has_value():
    assert hasattr(paplj::Num, "value")
    descriptor = None
    for klass in paplj::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_paplj::memberref_is_not_abstract():
    assert not inspect.isabstract(paplj::MemberRef)


def test_paplj::memberref_constructor_exists():
    assert callable(paplj::MemberRef.__init__)


def test_paplj::memberref_constructor_args():
    sig = inspect.signature(paplj::MemberRef.__init__)
    params = list(sig.parameters.keys())
    assert "methodInvocation" in params, "Missing parameter 'methodInvocation'"

def test_paplj::memberref_has_methodInvocation():
    assert hasattr(paplj::MemberRef, "methodInvocation")
    descriptor = None
    for klass in paplj::MemberRef.__mro__:
        if "methodInvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodInvocation"]
            break
    assert isinstance(descriptor, property)



def test_paplj::div_is_not_abstract():
    assert not inspect.isabstract(paplj::Div)


def test_paplj::div_constructor_exists():
    assert callable(paplj::Div.__init__)


def test_paplj::div_constructor_args():
    sig = inspect.signature(paplj::Div.__init__)
    params = list(sig.parameters.keys())



def test_paplj::let_is_not_abstract():
    assert not inspect.isabstract(paplj::Let)


def test_paplj::let_constructor_exists():
    assert callable(paplj::Let.__init__)


def test_paplj::let_constructor_args():
    sig = inspect.signature(paplj::Let.__init__)
    params = list(sig.parameters.keys())



def test_paplj::eq_is_not_abstract():
    assert not inspect.isabstract(paplj::Eq)


def test_paplj::eq_constructor_exists():
    assert callable(paplj::Eq.__init__)


def test_paplj::eq_constructor_args():
    sig = inspect.signature(paplj::Eq.__init__)
    params = list(sig.parameters.keys())



def test_paplj::mul_is_not_abstract():
    assert not inspect.isabstract(paplj::Mul)


def test_paplj::mul_constructor_exists():
    assert callable(paplj::Mul.__init__)


def test_paplj::mul_constructor_args():
    sig = inspect.signature(paplj::Mul.__init__)
    params = list(sig.parameters.keys())



def test_paplj::null_is_not_abstract():
    assert not inspect.isabstract(paplj::Null)


def test_paplj::null_constructor_exists():
    assert callable(paplj::Null.__init__)


def test_paplj::null_constructor_args():
    sig = inspect.signature(paplj::Null.__init__)
    params = list(sig.parameters.keys())



def test_paplj::not_is_not_abstract():
    assert not inspect.isabstract(paplj::Not)


def test_paplj::not_constructor_exists():
    assert callable(paplj::Not.__init__)


def test_paplj::not_constructor_args():
    sig = inspect.signature(paplj::Not.__init__)
    params = list(sig.parameters.keys())



def test_paplj::sub_is_not_abstract():
    assert not inspect.isabstract(paplj::Sub)


def test_paplj::sub_constructor_exists():
    assert callable(paplj::Sub.__init__)


def test_paplj::sub_constructor_args():
    sig = inspect.signature(paplj::Sub.__init__)
    params = list(sig.parameters.keys())



def test_paplj::min_is_not_abstract():
    assert not inspect.isabstract(paplj::Min)


def test_paplj::min_constructor_exists():
    assert callable(paplj::Min.__init__)


def test_paplj::min_constructor_args():
    sig = inspect.signature(paplj::Min.__init__)
    params = list(sig.parameters.keys())



def test_paplj::if_is_not_abstract():
    assert not inspect.isabstract(paplj::If)


def test_paplj::if_constructor_exists():
    assert callable(paplj::If.__init__)


def test_paplj::if_constructor_args():
    sig = inspect.signature(paplj::If.__init__)
    params = list(sig.parameters.keys())



def test_paplj::add_is_not_abstract():
    assert not inspect.isabstract(paplj::Add)


def test_paplj::add_constructor_exists():
    assert callable(paplj::Add.__init__)


def test_paplj::add_constructor_args():
    sig = inspect.signature(paplj::Add.__init__)
    params = list(sig.parameters.keys())



def test_paplj::lt_is_not_abstract():
    assert not inspect.isabstract(paplj::Lt)


def test_paplj::lt_constructor_exists():
    assert callable(paplj::Lt.__init__)


def test_paplj::lt_constructor_args():
    sig = inspect.signature(paplj::Lt.__init__)
    params = list(sig.parameters.keys())



def test_paplj::var_is_not_abstract():
    assert not inspect.isabstract(paplj::Var)


def test_paplj::var_constructor_exists():
    assert callable(paplj::Var.__init__)


def test_paplj::var_constructor_args():
    sig = inspect.signature(paplj::Var.__init__)
    params = list(sig.parameters.keys())
    assert "methodInvocation" in params, "Missing parameter 'methodInvocation'"

def test_paplj::var_has_methodInvocation():
    assert hasattr(paplj::Var, "methodInvocation")
    descriptor = None
    for klass in paplj::Var.__mro__:
        if "methodInvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodInvocation"]
            break
    assert isinstance(descriptor, property)



def test_paplj::this_is_not_abstract():
    assert not inspect.isabstract(paplj::This)


def test_paplj::this_constructor_exists():
    assert callable(paplj::This.__init__)


def test_paplj::this_constructor_args():
    sig = inspect.signature(paplj::This.__init__)
    params = list(sig.parameters.keys())



def test_paplj::and_is_not_abstract():
    assert not inspect.isabstract(paplj::And)


def test_paplj::and_constructor_exists():
    assert callable(paplj::And.__init__)


def test_paplj::and_constructor_args():
    sig = inspect.signature(paplj::And.__init__)
    params = list(sig.parameters.keys())



def test_paplj::assignment_is_not_abstract():
    assert not inspect.isabstract(paplj::Assignment)


def test_paplj::assignment_constructor_exists():
    assert callable(paplj::Assignment.__init__)


def test_paplj::assignment_constructor_args():
    sig = inspect.signature(paplj::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_paplj::or_is_not_abstract():
    assert not inspect.isabstract(paplj::Or)


def test_paplj::or_constructor_exists():
    assert callable(paplj::Or.__init__)


def test_paplj::or_constructor_args():
    sig = inspect.signature(paplj::Or.__init__)
    params = list(sig.parameters.keys())



def test_paplj::symbol_is_not_abstract():
    assert not inspect.isabstract(paplj::Symbol)


def test_paplj::symbol_constructor_exists():
    assert callable(paplj::Symbol.__init__)


def test_paplj::symbol_constructor_args():
    sig = inspect.signature(paplj::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_paplj::symbol_has_name():
    assert hasattr(paplj::Symbol, "name")
    descriptor = None
    for klass in paplj::Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_paplj::binding_is_not_abstract():
    assert not inspect.isabstract(paplj::Binding)


def test_paplj::binding_constructor_exists():
    assert callable(paplj::Binding.__init__)


def test_paplj::binding_constructor_args():
    sig = inspect.signature(paplj::Binding.__init__)
    params = list(sig.parameters.keys())



def test_paplj::member_is_not_abstract():
    assert not inspect.isabstract(paplj::Member)


def test_paplj::member_constructor_exists():
    assert callable(paplj::Member.__init__)


def test_paplj::member_constructor_args():
    sig = inspect.signature(paplj::Member.__init__)
    params = list(sig.parameters.keys())



def test_paplj::expr_is_not_abstract():
    assert not inspect.isabstract(paplj::Expr)


def test_paplj::expr_constructor_exists():
    assert callable(paplj::Expr.__init__)


def test_paplj::expr_constructor_args():
    sig = inspect.signature(paplj::Expr.__init__)
    params = list(sig.parameters.keys())



def test_paplj::type_is_not_abstract():
    assert not inspect.isabstract(paplj::Type)


def test_paplj::type_constructor_exists():
    assert callable(paplj::Type.__init__)


def test_paplj::type_constructor_args():
    sig = inspect.signature(paplj::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_paplj::type_has_name():
    assert hasattr(paplj::Type, "name")
    descriptor = None
    for klass in paplj::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_paplj::import_is_not_abstract():
    assert not inspect.isabstract(paplj::Import)


def test_paplj::import_constructor_exists():
    assert callable(paplj::Import.__init__)


def test_paplj::import_constructor_args():
    sig = inspect.signature(paplj::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_paplj::import_has_importedNamespace():
    assert hasattr(paplj::Import, "importedNamespace")
    descriptor = None
    for klass in paplj::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_paplj::program_is_not_abstract():
    assert not inspect.isabstract(paplj::Program)


def test_paplj::program_constructor_exists():
    assert callable(paplj::Program.__init__)


def test_paplj::program_constructor_args():
    sig = inspect.signature(paplj::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_paplj::program_has_name():
    assert hasattr(paplj::Program, "name")
    descriptor = None
    for klass in paplj::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_paplj::block2_is_not_abstract():
    assert not inspect.isabstract(paplj::Block2)


def test_paplj::block2_constructor_exists():
    assert callable(paplj::Block2.__init__)


def test_paplj::block2_constructor_args():
    sig = inspect.signature(paplj::Block2.__init__)
    params = list(sig.parameters.keys())



def test_paplj::param_is_not_abstract():
    assert not inspect.isabstract(paplj::Param)


def test_paplj::param_constructor_exists():
    assert callable(paplj::Param.__init__)


def test_paplj::param_constructor_args():
    sig = inspect.signature(paplj::Param.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_paplj::method_is_not_abstract():
    assert not inspect.isabstract(paplj::Method)


def test_paplj::method_constructor_exists():
    assert callable(paplj::Method.__init__)


def test_paplj::method_constructor_args():
    sig = inspect.signature(paplj::Method.__init__)
    params = list(sig.parameters.keys())



def test_paplj::field_is_not_abstract():
    assert not inspect.isabstract(paplj::Field)


def test_paplj::field_constructor_exists():
    assert callable(paplj::Field.__init__)


def test_paplj::field_constructor_args():
    sig = inspect.signature(paplj::Field.__init__)
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
Expr_strategy = st.builds(
    Expr,
)
paplj::Neq_strategy = st.builds(
    paplj::Neq,
)
paplj::Cast_strategy = st.builds(
    paplj::Cast,
)
paplj::Bool_strategy = st.builds(
    paplj::Bool,
    true=
        st.booleans()
)
paplj::New_strategy = st.builds(
    paplj::New,
)
paplj::Num_strategy = st.builds(
    paplj::Num,
    value=
        st.integers()
)
paplj::MemberRef_strategy = st.builds(
    paplj::MemberRef,
    methodInvocation=
        st.booleans()
)
paplj::Div_strategy = st.builds(
    paplj::Div,
)
paplj::Let_strategy = st.builds(
    paplj::Let,
)
paplj::Eq_strategy = st.builds(
    paplj::Eq,
)
paplj::Mul_strategy = st.builds(
    paplj::Mul,
)
paplj::Null_strategy = st.builds(
    paplj::Null,
)
paplj::Not_strategy = st.builds(
    paplj::Not,
)
paplj::Sub_strategy = st.builds(
    paplj::Sub,
)
paplj::Min_strategy = st.builds(
    paplj::Min,
)
paplj::If_strategy = st.builds(
    paplj::If,
)
paplj::Add_strategy = st.builds(
    paplj::Add,
)
paplj::Lt_strategy = st.builds(
    paplj::Lt,
)
paplj::Var_strategy = st.builds(
    paplj::Var,
    methodInvocation=
        st.booleans()
)
paplj::This_strategy = st.builds(
    paplj::This,
)
paplj::And_strategy = st.builds(
    paplj::And,
)
paplj::Assignment_strategy = st.builds(
    paplj::Assignment,
)
paplj::Or_strategy = st.builds(
    paplj::Or,
)
paplj::Symbol_strategy = st.builds(
    paplj::Symbol,
    name=
        safe_text
)
Symbol_strategy = st.builds(
    Symbol,
)
paplj::Binding_strategy = st.builds(
    paplj::Binding,
)
paplj::Member_strategy = st.builds(
    paplj::Member,
)
paplj::Expr_strategy = st.builds(
    paplj::Expr,
)
paplj::Type_strategy = st.builds(
    paplj::Type,
    name=
        safe_text
)
paplj::Import_strategy = st.builds(
    paplj::Import,
    importedNamespace=
        safe_text
)
paplj::Program_strategy = st.builds(
    paplj::Program,
    name=
        safe_text
)
paplj::Block2_strategy = st.builds(
    paplj::Block2,
)
paplj::Param_strategy = st.builds(
    paplj::Param,
)
Member_strategy = st.builds(
    Member,
)
paplj::Method_strategy = st.builds(
    paplj::Method,
)
paplj::Field_strategy = st.builds(
    paplj::Field,
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=paplj::Neq_strategy)
@settings(max_examples=50)
def test_paplj::neq_instantiation(instance):
    assert isinstance(instance, paplj::Neq)

@given(instance=paplj::Cast_strategy)
@settings(max_examples=50)
def test_paplj::cast_instantiation(instance):
    assert isinstance(instance, paplj::Cast)

@given(instance=paplj::Bool_strategy)
@settings(max_examples=50)
def test_paplj::bool_instantiation(instance):
    assert isinstance(instance, paplj::Bool)

@given(instance=paplj::Bool_strategy)
def test_paplj::bool_true_type(instance):
    assert isinstance(instance.true, bool)


@given(instance=paplj::Bool_strategy)
def test_paplj::bool_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=paplj::New_strategy)
@settings(max_examples=50)
def test_paplj::new_instantiation(instance):
    assert isinstance(instance, paplj::New)

@given(instance=paplj::Num_strategy)
@settings(max_examples=50)
def test_paplj::num_instantiation(instance):
    assert isinstance(instance, paplj::Num)

@given(instance=paplj::Num_strategy)
def test_paplj::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=paplj::Num_strategy)
def test_paplj::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=paplj::MemberRef_strategy)
@settings(max_examples=50)
def test_paplj::memberref_instantiation(instance):
    assert isinstance(instance, paplj::MemberRef)

@given(instance=paplj::MemberRef_strategy)
def test_paplj::memberref_methodInvocation_type(instance):
    assert isinstance(instance.methodInvocation, bool)


@given(instance=paplj::MemberRef_strategy)
def test_paplj::memberref_methodInvocation_setter(instance):
    original = instance.methodInvocation
    instance.methodInvocation = original
    assert instance.methodInvocation == original

@given(instance=paplj::Div_strategy)
@settings(max_examples=50)
def test_paplj::div_instantiation(instance):
    assert isinstance(instance, paplj::Div)

@given(instance=paplj::Let_strategy)
@settings(max_examples=50)
def test_paplj::let_instantiation(instance):
    assert isinstance(instance, paplj::Let)

@given(instance=paplj::Eq_strategy)
@settings(max_examples=50)
def test_paplj::eq_instantiation(instance):
    assert isinstance(instance, paplj::Eq)

@given(instance=paplj::Mul_strategy)
@settings(max_examples=50)
def test_paplj::mul_instantiation(instance):
    assert isinstance(instance, paplj::Mul)

@given(instance=paplj::Null_strategy)
@settings(max_examples=50)
def test_paplj::null_instantiation(instance):
    assert isinstance(instance, paplj::Null)

@given(instance=paplj::Not_strategy)
@settings(max_examples=50)
def test_paplj::not_instantiation(instance):
    assert isinstance(instance, paplj::Not)

@given(instance=paplj::Sub_strategy)
@settings(max_examples=50)
def test_paplj::sub_instantiation(instance):
    assert isinstance(instance, paplj::Sub)

@given(instance=paplj::Min_strategy)
@settings(max_examples=50)
def test_paplj::min_instantiation(instance):
    assert isinstance(instance, paplj::Min)

@given(instance=paplj::If_strategy)
@settings(max_examples=50)
def test_paplj::if_instantiation(instance):
    assert isinstance(instance, paplj::If)

@given(instance=paplj::Add_strategy)
@settings(max_examples=50)
def test_paplj::add_instantiation(instance):
    assert isinstance(instance, paplj::Add)

@given(instance=paplj::Lt_strategy)
@settings(max_examples=50)
def test_paplj::lt_instantiation(instance):
    assert isinstance(instance, paplj::Lt)

@given(instance=paplj::Var_strategy)
@settings(max_examples=50)
def test_paplj::var_instantiation(instance):
    assert isinstance(instance, paplj::Var)

@given(instance=paplj::Var_strategy)
def test_paplj::var_methodInvocation_type(instance):
    assert isinstance(instance.methodInvocation, bool)


@given(instance=paplj::Var_strategy)
def test_paplj::var_methodInvocation_setter(instance):
    original = instance.methodInvocation
    instance.methodInvocation = original
    assert instance.methodInvocation == original

@given(instance=paplj::This_strategy)
@settings(max_examples=50)
def test_paplj::this_instantiation(instance):
    assert isinstance(instance, paplj::This)

@given(instance=paplj::And_strategy)
@settings(max_examples=50)
def test_paplj::and_instantiation(instance):
    assert isinstance(instance, paplj::And)

@given(instance=paplj::Assignment_strategy)
@settings(max_examples=50)
def test_paplj::assignment_instantiation(instance):
    assert isinstance(instance, paplj::Assignment)

@given(instance=paplj::Or_strategy)
@settings(max_examples=50)
def test_paplj::or_instantiation(instance):
    assert isinstance(instance, paplj::Or)

@given(instance=paplj::Symbol_strategy)
@settings(max_examples=50)
def test_paplj::symbol_instantiation(instance):
    assert isinstance(instance, paplj::Symbol)

@given(instance=paplj::Symbol_strategy)
def test_paplj::symbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=paplj::Symbol_strategy)
def test_paplj::symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=paplj::Binding_strategy)
@settings(max_examples=50)
def test_paplj::binding_instantiation(instance):
    assert isinstance(instance, paplj::Binding)

@given(instance=paplj::Member_strategy)
@settings(max_examples=50)
def test_paplj::member_instantiation(instance):
    assert isinstance(instance, paplj::Member)

@given(instance=paplj::Expr_strategy)
@settings(max_examples=50)
def test_paplj::expr_instantiation(instance):
    assert isinstance(instance, paplj::Expr)

@given(instance=paplj::Type_strategy)
@settings(max_examples=50)
def test_paplj::type_instantiation(instance):
    assert isinstance(instance, paplj::Type)

@given(instance=paplj::Type_strategy)
def test_paplj::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=paplj::Type_strategy)
def test_paplj::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=paplj::Import_strategy)
@settings(max_examples=50)
def test_paplj::import_instantiation(instance):
    assert isinstance(instance, paplj::Import)

@given(instance=paplj::Import_strategy)
def test_paplj::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=paplj::Import_strategy)
def test_paplj::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=paplj::Program_strategy)
@settings(max_examples=50)
def test_paplj::program_instantiation(instance):
    assert isinstance(instance, paplj::Program)

@given(instance=paplj::Program_strategy)
def test_paplj::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=paplj::Program_strategy)
def test_paplj::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=paplj::Block2_strategy)
@settings(max_examples=50)
def test_paplj::block2_instantiation(instance):
    assert isinstance(instance, paplj::Block2)

@given(instance=paplj::Param_strategy)
@settings(max_examples=50)
def test_paplj::param_instantiation(instance):
    assert isinstance(instance, paplj::Param)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=paplj::Method_strategy)
@settings(max_examples=50)
def test_paplj::method_instantiation(instance):
    assert isinstance(instance, paplj::Method)

@given(instance=paplj::Field_strategy)
@settings(max_examples=50)
def test_paplj::field_instantiation(instance):
    assert isinstance(instance, paplj::Field)
