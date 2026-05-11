import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    imp::Member,
    Member,
    imp::AttributeDecl,
    NamedElement,
    imp::Symbol,
    imp::NamedElement,
    imp::Class,
    imp::MethodDecl,
    imp::Program,
    Value,
    imp::BoolValue,
    imp::ArrayValue,
    imp::StringValue,
    imp::IntValue,
    imp::Value,
    imp::StringToValueMap,
    imp::Store,
    Symbol,
    imp::ParamDecl,
    Stmt,
    imp::Return,
    imp::Expr,
    imp::Print,
    imp::Assignment,
    imp::Block,
    imp::Declaration,
    Expr,
    imp::Unary,
    imp::NewClass,
    imp::ArrayDecl,
    imp::This,
    imp::StringConst,
    imp::Binary,
    imp::VarRef,
    imp::BoolConst,
    imp::Project,
    imp::IntConst,
    imp::While,
    imp::If,
    imp::Stmt,
    BinaryOp,
    UnaryOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imp::member_is_not_abstract():
    assert not inspect.isabstract(imp::Member)


def test_imp::member_constructor_exists():
    assert callable(imp::Member.__init__)


def test_imp::member_constructor_args():
    sig = inspect.signature(imp::Member.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_imp::attributedecl_is_not_abstract():
    assert not inspect.isabstract(imp::AttributeDecl)


def test_imp::attributedecl_constructor_exists():
    assert callable(imp::AttributeDecl.__init__)


def test_imp::attributedecl_constructor_args():
    sig = inspect.signature(imp::AttributeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::attributedecl_has_name():
    assert hasattr(imp::AttributeDecl, "name")
    descriptor = None
    for klass in imp::AttributeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_imp::symbol_is_not_abstract():
    assert not inspect.isabstract(imp::Symbol)


def test_imp::symbol_constructor_exists():
    assert callable(imp::Symbol.__init__)


def test_imp::symbol_constructor_args():
    sig = inspect.signature(imp::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_imp::namedelement_is_not_abstract():
    assert not inspect.isabstract(imp::NamedElement)


def test_imp::namedelement_constructor_exists():
    assert callable(imp::NamedElement.__init__)


def test_imp::namedelement_constructor_args():
    sig = inspect.signature(imp::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_imp::class_is_not_abstract():
    assert not inspect.isabstract(imp::Class)


def test_imp::class_constructor_exists():
    assert callable(imp::Class.__init__)


def test_imp::class_constructor_args():
    sig = inspect.signature(imp::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::class_has_name():
    assert hasattr(imp::Class, "name")
    descriptor = None
    for klass in imp::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp::methoddecl_is_not_abstract():
    assert not inspect.isabstract(imp::MethodDecl)


def test_imp::methoddecl_constructor_exists():
    assert callable(imp::MethodDecl.__init__)


def test_imp::methoddecl_constructor_args():
    sig = inspect.signature(imp::MethodDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::methoddecl_has_name():
    assert hasattr(imp::MethodDecl, "name")
    descriptor = None
    for klass in imp::MethodDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp::program_is_not_abstract():
    assert not inspect.isabstract(imp::Program)


def test_imp::program_constructor_exists():
    assert callable(imp::Program.__init__)


def test_imp::program_constructor_args():
    sig = inspect.signature(imp::Program.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_imp::boolvalue_is_not_abstract():
    assert not inspect.isabstract(imp::BoolValue)


def test_imp::boolvalue_constructor_exists():
    assert callable(imp::BoolValue.__init__)


def test_imp::boolvalue_constructor_args():
    sig = inspect.signature(imp::BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::boolvalue_has_value():
    assert hasattr(imp::BoolValue, "value")
    descriptor = None
    for klass in imp::BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::arrayvalue_is_not_abstract():
    assert not inspect.isabstract(imp::ArrayValue)


def test_imp::arrayvalue_constructor_exists():
    assert callable(imp::ArrayValue.__init__)


def test_imp::arrayvalue_constructor_args():
    sig = inspect.signature(imp::ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_imp::stringvalue_is_not_abstract():
    assert not inspect.isabstract(imp::StringValue)


def test_imp::stringvalue_constructor_exists():
    assert callable(imp::StringValue.__init__)


def test_imp::stringvalue_constructor_args():
    sig = inspect.signature(imp::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::stringvalue_has_value():
    assert hasattr(imp::StringValue, "value")
    descriptor = None
    for klass in imp::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::intvalue_is_not_abstract():
    assert not inspect.isabstract(imp::IntValue)


def test_imp::intvalue_constructor_exists():
    assert callable(imp::IntValue.__init__)


def test_imp::intvalue_constructor_args():
    sig = inspect.signature(imp::IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::intvalue_has_value():
    assert hasattr(imp::IntValue, "value")
    descriptor = None
    for klass in imp::IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::value_is_not_abstract():
    assert not inspect.isabstract(imp::Value)


def test_imp::value_constructor_exists():
    assert callable(imp::Value.__init__)


def test_imp::value_constructor_args():
    sig = inspect.signature(imp::Value.__init__)
    params = list(sig.parameters.keys())



def test_imp::stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(imp::StringToValueMap)


def test_imp::stringtovaluemap_constructor_exists():
    assert callable(imp::StringToValueMap.__init__)


def test_imp::stringtovaluemap_constructor_args():
    sig = inspect.signature(imp::StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_imp::stringtovaluemap_has_key():
    assert hasattr(imp::StringToValueMap, "key")
    descriptor = None
    for klass in imp::StringToValueMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_imp::store_is_not_abstract():
    assert not inspect.isabstract(imp::Store)


def test_imp::store_constructor_exists():
    assert callable(imp::Store.__init__)


def test_imp::store_constructor_args():
    sig = inspect.signature(imp::Store.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_imp::paramdecl_is_not_abstract():
    assert not inspect.isabstract(imp::ParamDecl)


def test_imp::paramdecl_constructor_exists():
    assert callable(imp::ParamDecl.__init__)


def test_imp::paramdecl_constructor_args():
    sig = inspect.signature(imp::ParamDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::paramdecl_has_name():
    assert hasattr(imp::ParamDecl, "name")
    descriptor = None
    for klass in imp::ParamDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp::return_is_not_abstract():
    assert not inspect.isabstract(imp::Return)


def test_imp::return_constructor_exists():
    assert callable(imp::Return.__init__)


def test_imp::return_constructor_args():
    sig = inspect.signature(imp::Return.__init__)
    params = list(sig.parameters.keys())



def test_imp::expr_is_not_abstract():
    assert not inspect.isabstract(imp::Expr)


def test_imp::expr_constructor_exists():
    assert callable(imp::Expr.__init__)


def test_imp::expr_constructor_args():
    sig = inspect.signature(imp::Expr.__init__)
    params = list(sig.parameters.keys())



def test_imp::print_is_not_abstract():
    assert not inspect.isabstract(imp::Print)


def test_imp::print_constructor_exists():
    assert callable(imp::Print.__init__)


def test_imp::print_constructor_args():
    sig = inspect.signature(imp::Print.__init__)
    params = list(sig.parameters.keys())



def test_imp::assignment_is_not_abstract():
    assert not inspect.isabstract(imp::Assignment)


def test_imp::assignment_constructor_exists():
    assert callable(imp::Assignment.__init__)


def test_imp::assignment_constructor_args():
    sig = inspect.signature(imp::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_imp::block_is_not_abstract():
    assert not inspect.isabstract(imp::Block)


def test_imp::block_constructor_exists():
    assert callable(imp::Block.__init__)


def test_imp::block_constructor_args():
    sig = inspect.signature(imp::Block.__init__)
    params = list(sig.parameters.keys())



def test_imp::declaration_is_not_abstract():
    assert not inspect.isabstract(imp::Declaration)


def test_imp::declaration_constructor_exists():
    assert callable(imp::Declaration.__init__)


def test_imp::declaration_constructor_args():
    sig = inspect.signature(imp::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp::declaration_has_name():
    assert hasattr(imp::Declaration, "name")
    descriptor = None
    for klass in imp::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_imp::unary_is_not_abstract():
    assert not inspect.isabstract(imp::Unary)


def test_imp::unary_constructor_exists():
    assert callable(imp::Unary.__init__)


def test_imp::unary_constructor_args():
    sig = inspect.signature(imp::Unary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp::unary_has_op():
    assert hasattr(imp::Unary, "op")
    descriptor = None
    for klass in imp::Unary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp::newclass_is_not_abstract():
    assert not inspect.isabstract(imp::NewClass)


def test_imp::newclass_constructor_exists():
    assert callable(imp::NewClass.__init__)


def test_imp::newclass_constructor_args():
    sig = inspect.signature(imp::NewClass.__init__)
    params = list(sig.parameters.keys())



def test_imp::arraydecl_is_not_abstract():
    assert not inspect.isabstract(imp::ArrayDecl)


def test_imp::arraydecl_constructor_exists():
    assert callable(imp::ArrayDecl.__init__)


def test_imp::arraydecl_constructor_args():
    sig = inspect.signature(imp::ArrayDecl.__init__)
    params = list(sig.parameters.keys())



def test_imp::this_is_not_abstract():
    assert not inspect.isabstract(imp::This)


def test_imp::this_constructor_exists():
    assert callable(imp::This.__init__)


def test_imp::this_constructor_args():
    sig = inspect.signature(imp::This.__init__)
    params = list(sig.parameters.keys())



def test_imp::stringconst_is_not_abstract():
    assert not inspect.isabstract(imp::StringConst)


def test_imp::stringconst_constructor_exists():
    assert callable(imp::StringConst.__init__)


def test_imp::stringconst_constructor_args():
    sig = inspect.signature(imp::StringConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::stringconst_has_value():
    assert hasattr(imp::StringConst, "value")
    descriptor = None
    for klass in imp::StringConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::binary_is_not_abstract():
    assert not inspect.isabstract(imp::Binary)


def test_imp::binary_constructor_exists():
    assert callable(imp::Binary.__init__)


def test_imp::binary_constructor_args():
    sig = inspect.signature(imp::Binary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp::binary_has_op():
    assert hasattr(imp::Binary, "op")
    descriptor = None
    for klass in imp::Binary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp::varref_is_not_abstract():
    assert not inspect.isabstract(imp::VarRef)


def test_imp::varref_constructor_exists():
    assert callable(imp::VarRef.__init__)


def test_imp::varref_constructor_args():
    sig = inspect.signature(imp::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_imp::boolconst_is_not_abstract():
    assert not inspect.isabstract(imp::BoolConst)


def test_imp::boolconst_constructor_exists():
    assert callable(imp::BoolConst.__init__)


def test_imp::boolconst_constructor_args():
    sig = inspect.signature(imp::BoolConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::boolconst_has_value():
    assert hasattr(imp::BoolConst, "value")
    descriptor = None
    for klass in imp::BoolConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::project_is_not_abstract():
    assert not inspect.isabstract(imp::Project)


def test_imp::project_constructor_exists():
    assert callable(imp::Project.__init__)


def test_imp::project_constructor_args():
    sig = inspect.signature(imp::Project.__init__)
    params = list(sig.parameters.keys())
    assert "ismethodcall" in params, "Missing parameter 'ismethodcall'"

def test_imp::project_has_ismethodcall():
    assert hasattr(imp::Project, "ismethodcall")
    descriptor = None
    for klass in imp::Project.__mro__:
        if "ismethodcall" in klass.__dict__:
            descriptor = klass.__dict__["ismethodcall"]
            break
    assert isinstance(descriptor, property)



def test_imp::intconst_is_not_abstract():
    assert not inspect.isabstract(imp::IntConst)


def test_imp::intconst_constructor_exists():
    assert callable(imp::IntConst.__init__)


def test_imp::intconst_constructor_args():
    sig = inspect.signature(imp::IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp::intconst_has_value():
    assert hasattr(imp::IntConst, "value")
    descriptor = None
    for klass in imp::IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp::while_is_not_abstract():
    assert not inspect.isabstract(imp::While)


def test_imp::while_constructor_exists():
    assert callable(imp::While.__init__)


def test_imp::while_constructor_args():
    sig = inspect.signature(imp::While.__init__)
    params = list(sig.parameters.keys())



def test_imp::if_is_not_abstract():
    assert not inspect.isabstract(imp::If)


def test_imp::if_constructor_exists():
    assert callable(imp::If.__init__)


def test_imp::if_constructor_args():
    sig = inspect.signature(imp::If.__init__)
    params = list(sig.parameters.keys())



def test_imp::stmt_is_not_abstract():
    assert not inspect.isabstract(imp::Stmt)


def test_imp::stmt_constructor_exists():
    assert callable(imp::Stmt.__init__)


def test_imp::stmt_constructor_args():
    sig = inspect.signature(imp::Stmt.__init__)
    params = list(sig.parameters.keys())

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "LT",
        "GEQ",
        "ADD",
        "OR",
        "LEQ",
        "SUB",
        "MUL",
        "GT",
        "EQ",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "NOT",
        "NEGATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"


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
imp::Member_strategy = st.builds(
    imp::Member,
)
Member_strategy = st.builds(
    Member,
)
imp::AttributeDecl_strategy = st.builds(
    imp::AttributeDecl,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
imp::Symbol_strategy = st.builds(
    imp::Symbol,
)
imp::NamedElement_strategy = st.builds(
    imp::NamedElement,
)
imp::Class_strategy = st.builds(
    imp::Class,
    name=
        safe_text
)
imp::MethodDecl_strategy = st.builds(
    imp::MethodDecl,
    name=
        safe_text
)
imp::Program_strategy = st.builds(
    imp::Program,
)
Value_strategy = st.builds(
    Value,
)
imp::BoolValue_strategy = st.builds(
    imp::BoolValue,
    value=
        st.booleans()
)
imp::ArrayValue_strategy = st.builds(
    imp::ArrayValue,
)
imp::StringValue_strategy = st.builds(
    imp::StringValue,
    value=
        safe_text
)
imp::IntValue_strategy = st.builds(
    imp::IntValue,
    value=
        st.integers()
)
imp::Value_strategy = st.builds(
    imp::Value,
)
imp::StringToValueMap_strategy = st.builds(
    imp::StringToValueMap,
    key=
        safe_text
)
imp::Store_strategy = st.builds(
    imp::Store,
)
Symbol_strategy = st.builds(
    Symbol,
)
imp::ParamDecl_strategy = st.builds(
    imp::ParamDecl,
    name=
        safe_text
)
Stmt_strategy = st.builds(
    Stmt,
)
imp::Return_strategy = st.builds(
    imp::Return,
)
imp::Expr_strategy = st.builds(
    imp::Expr,
)
imp::Print_strategy = st.builds(
    imp::Print,
)
imp::Assignment_strategy = st.builds(
    imp::Assignment,
)
imp::Block_strategy = st.builds(
    imp::Block,
)
imp::Declaration_strategy = st.builds(
    imp::Declaration,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
imp::Unary_strategy = st.builds(
    imp::Unary,
    op=
        safe_text
)
imp::NewClass_strategy = st.builds(
    imp::NewClass,
)
imp::ArrayDecl_strategy = st.builds(
    imp::ArrayDecl,
)
imp::This_strategy = st.builds(
    imp::This,
)
imp::StringConst_strategy = st.builds(
    imp::StringConst,
    value=
        safe_text
)
imp::Binary_strategy = st.builds(
    imp::Binary,
    op=
        safe_text
)
imp::VarRef_strategy = st.builds(
    imp::VarRef,
)
imp::BoolConst_strategy = st.builds(
    imp::BoolConst,
    value=
        st.booleans()
)
imp::Project_strategy = st.builds(
    imp::Project,
    ismethodcall=
        st.booleans()
)
imp::IntConst_strategy = st.builds(
    imp::IntConst,
    value=
        st.integers()
)
imp::While_strategy = st.builds(
    imp::While,
)
imp::If_strategy = st.builds(
    imp::If,
)
imp::Stmt_strategy = st.builds(
    imp::Stmt,
)

@given(instance=imp::Member_strategy)
@settings(max_examples=50)
def test_imp::member_instantiation(instance):
    assert isinstance(instance, imp::Member)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=imp::AttributeDecl_strategy)
@settings(max_examples=50)
def test_imp::attributedecl_instantiation(instance):
    assert isinstance(instance, imp::AttributeDecl)

@given(instance=imp::AttributeDecl_strategy)
def test_imp::attributedecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::AttributeDecl_strategy)
def test_imp::attributedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=imp::Symbol_strategy)
@settings(max_examples=50)
def test_imp::symbol_instantiation(instance):
    assert isinstance(instance, imp::Symbol)

@given(instance=imp::NamedElement_strategy)
@settings(max_examples=50)
def test_imp::namedelement_instantiation(instance):
    assert isinstance(instance, imp::NamedElement)

@given(instance=imp::Class_strategy)
@settings(max_examples=50)
def test_imp::class_instantiation(instance):
    assert isinstance(instance, imp::Class)

@given(instance=imp::Class_strategy)
def test_imp::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::Class_strategy)
def test_imp::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp::MethodDecl_strategy)
@settings(max_examples=50)
def test_imp::methoddecl_instantiation(instance):
    assert isinstance(instance, imp::MethodDecl)

@given(instance=imp::MethodDecl_strategy)
def test_imp::methoddecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::MethodDecl_strategy)
def test_imp::methoddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp::Program_strategy)
@settings(max_examples=50)
def test_imp::program_instantiation(instance):
    assert isinstance(instance, imp::Program)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=imp::BoolValue_strategy)
@settings(max_examples=50)
def test_imp::boolvalue_instantiation(instance):
    assert isinstance(instance, imp::BoolValue)

@given(instance=imp::BoolValue_strategy)
def test_imp::boolvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=imp::BoolValue_strategy)
def test_imp::boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::ArrayValue_strategy)
@settings(max_examples=50)
def test_imp::arrayvalue_instantiation(instance):
    assert isinstance(instance, imp::ArrayValue)

@given(instance=imp::StringValue_strategy)
@settings(max_examples=50)
def test_imp::stringvalue_instantiation(instance):
    assert isinstance(instance, imp::StringValue)

@given(instance=imp::StringValue_strategy)
def test_imp::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=imp::StringValue_strategy)
def test_imp::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::IntValue_strategy)
@settings(max_examples=50)
def test_imp::intvalue_instantiation(instance):
    assert isinstance(instance, imp::IntValue)

@given(instance=imp::IntValue_strategy)
def test_imp::intvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=imp::IntValue_strategy)
def test_imp::intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::Value_strategy)
@settings(max_examples=50)
def test_imp::value_instantiation(instance):
    assert isinstance(instance, imp::Value)

@given(instance=imp::StringToValueMap_strategy)
@settings(max_examples=50)
def test_imp::stringtovaluemap_instantiation(instance):
    assert isinstance(instance, imp::StringToValueMap)

@given(instance=imp::StringToValueMap_strategy)
def test_imp::stringtovaluemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=imp::StringToValueMap_strategy)
def test_imp::stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=imp::Store_strategy)
@settings(max_examples=50)
def test_imp::store_instantiation(instance):
    assert isinstance(instance, imp::Store)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=imp::ParamDecl_strategy)
@settings(max_examples=50)
def test_imp::paramdecl_instantiation(instance):
    assert isinstance(instance, imp::ParamDecl)

@given(instance=imp::ParamDecl_strategy)
def test_imp::paramdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::ParamDecl_strategy)
def test_imp::paramdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=imp::Return_strategy)
@settings(max_examples=50)
def test_imp::return_instantiation(instance):
    assert isinstance(instance, imp::Return)

@given(instance=imp::Expr_strategy)
@settings(max_examples=50)
def test_imp::expr_instantiation(instance):
    assert isinstance(instance, imp::Expr)

@given(instance=imp::Print_strategy)
@settings(max_examples=50)
def test_imp::print_instantiation(instance):
    assert isinstance(instance, imp::Print)

@given(instance=imp::Assignment_strategy)
@settings(max_examples=50)
def test_imp::assignment_instantiation(instance):
    assert isinstance(instance, imp::Assignment)

@given(instance=imp::Block_strategy)
@settings(max_examples=50)
def test_imp::block_instantiation(instance):
    assert isinstance(instance, imp::Block)

@given(instance=imp::Declaration_strategy)
@settings(max_examples=50)
def test_imp::declaration_instantiation(instance):
    assert isinstance(instance, imp::Declaration)

@given(instance=imp::Declaration_strategy)
def test_imp::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=imp::Declaration_strategy)
def test_imp::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=imp::Unary_strategy)
@settings(max_examples=50)
def test_imp::unary_instantiation(instance):
    assert isinstance(instance, imp::Unary)

@given(instance=imp::Unary_strategy)
def test_imp::unary_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=imp::Unary_strategy)
def test_imp::unary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp::NewClass_strategy)
@settings(max_examples=50)
def test_imp::newclass_instantiation(instance):
    assert isinstance(instance, imp::NewClass)

@given(instance=imp::ArrayDecl_strategy)
@settings(max_examples=50)
def test_imp::arraydecl_instantiation(instance):
    assert isinstance(instance, imp::ArrayDecl)

@given(instance=imp::This_strategy)
@settings(max_examples=50)
def test_imp::this_instantiation(instance):
    assert isinstance(instance, imp::This)

@given(instance=imp::StringConst_strategy)
@settings(max_examples=50)
def test_imp::stringconst_instantiation(instance):
    assert isinstance(instance, imp::StringConst)

@given(instance=imp::StringConst_strategy)
def test_imp::stringconst_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=imp::StringConst_strategy)
def test_imp::stringconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::Binary_strategy)
@settings(max_examples=50)
def test_imp::binary_instantiation(instance):
    assert isinstance(instance, imp::Binary)

@given(instance=imp::Binary_strategy)
def test_imp::binary_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=imp::Binary_strategy)
def test_imp::binary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp::VarRef_strategy)
@settings(max_examples=50)
def test_imp::varref_instantiation(instance):
    assert isinstance(instance, imp::VarRef)

@given(instance=imp::BoolConst_strategy)
@settings(max_examples=50)
def test_imp::boolconst_instantiation(instance):
    assert isinstance(instance, imp::BoolConst)

@given(instance=imp::BoolConst_strategy)
def test_imp::boolconst_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=imp::BoolConst_strategy)
def test_imp::boolconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::Project_strategy)
@settings(max_examples=50)
def test_imp::project_instantiation(instance):
    assert isinstance(instance, imp::Project)

@given(instance=imp::Project_strategy)
def test_imp::project_ismethodcall_type(instance):
    assert isinstance(instance.ismethodcall, bool)


@given(instance=imp::Project_strategy)
def test_imp::project_ismethodcall_setter(instance):
    original = instance.ismethodcall
    instance.ismethodcall = original
    assert instance.ismethodcall == original

@given(instance=imp::IntConst_strategy)
@settings(max_examples=50)
def test_imp::intconst_instantiation(instance):
    assert isinstance(instance, imp::IntConst)

@given(instance=imp::IntConst_strategy)
def test_imp::intconst_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=imp::IntConst_strategy)
def test_imp::intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp::While_strategy)
@settings(max_examples=50)
def test_imp::while_instantiation(instance):
    assert isinstance(instance, imp::While)

@given(instance=imp::If_strategy)
@settings(max_examples=50)
def test_imp::if_instantiation(instance):
    assert isinstance(instance, imp::If)

@given(instance=imp::Stmt_strategy)
@settings(max_examples=50)
def test_imp::stmt_instantiation(instance):
    assert isinstance(instance, imp::Stmt)
