import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    imp_NamedElement,
    imp_Class,
    imp_Program,
    Value,
    imp_BoolValue,
    imp_StringValue,
    imp_ArrayValue,
    imp_IntValue,
    imp_Value,
    imp_StringToValueMap,
    imp_Store,
    Symbol,
    Stmt,
    imp_Expr,
    imp_Block,
    imp_Declaration,
    Expr,
    imp_Binary,
    imp_ArrayDecl,
    imp_BoolConst,
    imp_StringConst,
    imp_Unary,
    imp_IntConst,
    imp_While,
    imp_If,
    imp_Stmt,
    imp_VarRef,
    imp_Symbol,
    imp_Member,
    imp_Project,
    imp_Print,
    imp_Return,
    imp_ParamDecl,
    Member,
    imp_MethodDecl,
    imp_AttributeDecl,
    imp_Assignment,
    imp_NewClass,
    imp_This,
    UnaryOp,
    BinaryOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_imp_namedelement_is_not_abstract():
    assert not inspect.isabstract(imp_NamedElement)


def test_imp_namedelement_constructor_exists():
    assert callable(imp_NamedElement.__init__)


def test_imp_namedelement_constructor_args():
    sig = inspect.signature(imp_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_imp_class_is_not_abstract():
    assert not inspect.isabstract(imp_Class)


def test_imp_class_constructor_exists():
    assert callable(imp_Class.__init__)


def test_imp_class_constructor_args():
    sig = inspect.signature(imp_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_class_has_name():
    assert hasattr(imp_Class, "name")
    descriptor = None
    for klass in imp_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp_program_is_not_abstract():
    assert not inspect.isabstract(imp_Program)


def test_imp_program_constructor_exists():
    assert callable(imp_Program.__init__)


def test_imp_program_constructor_args():
    sig = inspect.signature(imp_Program.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_imp_boolvalue_is_not_abstract():
    assert not inspect.isabstract(imp_BoolValue)


def test_imp_boolvalue_constructor_exists():
    assert callable(imp_BoolValue.__init__)


def test_imp_boolvalue_constructor_args():
    sig = inspect.signature(imp_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_boolvalue_has_value():
    assert hasattr(imp_BoolValue, "value")
    descriptor = None
    for klass in imp_BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_stringvalue_is_not_abstract():
    assert not inspect.isabstract(imp_StringValue)


def test_imp_stringvalue_constructor_exists():
    assert callable(imp_StringValue.__init__)


def test_imp_stringvalue_constructor_args():
    sig = inspect.signature(imp_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_stringvalue_has_value():
    assert hasattr(imp_StringValue, "value")
    descriptor = None
    for klass in imp_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(imp_ArrayValue)


def test_imp_arrayvalue_constructor_exists():
    assert callable(imp_ArrayValue.__init__)


def test_imp_arrayvalue_constructor_args():
    sig = inspect.signature(imp_ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_imp_intvalue_is_not_abstract():
    assert not inspect.isabstract(imp_IntValue)


def test_imp_intvalue_constructor_exists():
    assert callable(imp_IntValue.__init__)


def test_imp_intvalue_constructor_args():
    sig = inspect.signature(imp_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_intvalue_has_value():
    assert hasattr(imp_IntValue, "value")
    descriptor = None
    for klass in imp_IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_value_is_not_abstract():
    assert not inspect.isabstract(imp_Value)


def test_imp_value_constructor_exists():
    assert callable(imp_Value.__init__)


def test_imp_value_constructor_args():
    sig = inspect.signature(imp_Value.__init__)
    params = list(sig.parameters.keys())



def test_imp_stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(imp_StringToValueMap)


def test_imp_stringtovaluemap_constructor_exists():
    assert callable(imp_StringToValueMap.__init__)


def test_imp_stringtovaluemap_constructor_args():
    sig = inspect.signature(imp_StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_imp_stringtovaluemap_has_key():
    assert hasattr(imp_StringToValueMap, "key")
    descriptor = None
    for klass in imp_StringToValueMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_imp_store_is_not_abstract():
    assert not inspect.isabstract(imp_Store)


def test_imp_store_constructor_exists():
    assert callable(imp_Store.__init__)


def test_imp_store_constructor_args():
    sig = inspect.signature(imp_Store.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp_expr_is_not_abstract():
    assert not inspect.isabstract(imp_Expr)


def test_imp_expr_constructor_exists():
    assert callable(imp_Expr.__init__)


def test_imp_expr_constructor_args():
    sig = inspect.signature(imp_Expr.__init__)
    params = list(sig.parameters.keys())



def test_imp_block_is_not_abstract():
    assert not inspect.isabstract(imp_Block)


def test_imp_block_constructor_exists():
    assert callable(imp_Block.__init__)


def test_imp_block_constructor_args():
    sig = inspect.signature(imp_Block.__init__)
    params = list(sig.parameters.keys())



def test_imp_declaration_is_not_abstract():
    assert not inspect.isabstract(imp_Declaration)


def test_imp_declaration_constructor_exists():
    assert callable(imp_Declaration.__init__)


def test_imp_declaration_constructor_args():
    sig = inspect.signature(imp_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_declaration_has_name():
    assert hasattr(imp_Declaration, "name")
    descriptor = None
    for klass in imp_Declaration.__mro__:
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



def test_imp_binary_is_not_abstract():
    assert not inspect.isabstract(imp_Binary)


def test_imp_binary_constructor_exists():
    assert callable(imp_Binary.__init__)


def test_imp_binary_constructor_args():
    sig = inspect.signature(imp_Binary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp_binary_has_op():
    assert hasattr(imp_Binary, "op")
    descriptor = None
    for klass in imp_Binary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp_arraydecl_is_not_abstract():
    assert not inspect.isabstract(imp_ArrayDecl)


def test_imp_arraydecl_constructor_exists():
    assert callable(imp_ArrayDecl.__init__)


def test_imp_arraydecl_constructor_args():
    sig = inspect.signature(imp_ArrayDecl.__init__)
    params = list(sig.parameters.keys())



def test_imp_boolconst_is_not_abstract():
    assert not inspect.isabstract(imp_BoolConst)


def test_imp_boolconst_constructor_exists():
    assert callable(imp_BoolConst.__init__)


def test_imp_boolconst_constructor_args():
    sig = inspect.signature(imp_BoolConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_boolconst_has_value():
    assert hasattr(imp_BoolConst, "value")
    descriptor = None
    for klass in imp_BoolConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_stringconst_is_not_abstract():
    assert not inspect.isabstract(imp_StringConst)


def test_imp_stringconst_constructor_exists():
    assert callable(imp_StringConst.__init__)


def test_imp_stringconst_constructor_args():
    sig = inspect.signature(imp_StringConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_stringconst_has_value():
    assert hasattr(imp_StringConst, "value")
    descriptor = None
    for klass in imp_StringConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_unary_is_not_abstract():
    assert not inspect.isabstract(imp_Unary)


def test_imp_unary_constructor_exists():
    assert callable(imp_Unary.__init__)


def test_imp_unary_constructor_args():
    sig = inspect.signature(imp_Unary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_imp_unary_has_op():
    assert hasattr(imp_Unary, "op")
    descriptor = None
    for klass in imp_Unary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_imp_intconst_is_not_abstract():
    assert not inspect.isabstract(imp_IntConst)


def test_imp_intconst_constructor_exists():
    assert callable(imp_IntConst.__init__)


def test_imp_intconst_constructor_args():
    sig = inspect.signature(imp_IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_imp_intconst_has_value():
    assert hasattr(imp_IntConst, "value")
    descriptor = None
    for klass in imp_IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imp_while_is_not_abstract():
    assert not inspect.isabstract(imp_While)


def test_imp_while_constructor_exists():
    assert callable(imp_While.__init__)


def test_imp_while_constructor_args():
    sig = inspect.signature(imp_While.__init__)
    params = list(sig.parameters.keys())



def test_imp_if_is_not_abstract():
    assert not inspect.isabstract(imp_If)


def test_imp_if_constructor_exists():
    assert callable(imp_If.__init__)


def test_imp_if_constructor_args():
    sig = inspect.signature(imp_If.__init__)
    params = list(sig.parameters.keys())



def test_imp_stmt_is_not_abstract():
    assert not inspect.isabstract(imp_Stmt)


def test_imp_stmt_constructor_exists():
    assert callable(imp_Stmt.__init__)


def test_imp_stmt_constructor_args():
    sig = inspect.signature(imp_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_imp_varref_is_not_abstract():
    assert not inspect.isabstract(imp_VarRef)


def test_imp_varref_constructor_exists():
    assert callable(imp_VarRef.__init__)


def test_imp_varref_constructor_args():
    sig = inspect.signature(imp_VarRef.__init__)
    params = list(sig.parameters.keys())



def test_imp_symbol_is_not_abstract():
    assert not inspect.isabstract(imp_Symbol)


def test_imp_symbol_constructor_exists():
    assert callable(imp_Symbol.__init__)


def test_imp_symbol_constructor_args():
    sig = inspect.signature(imp_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_imp_member_is_not_abstract():
    assert not inspect.isabstract(imp_Member)


def test_imp_member_constructor_exists():
    assert callable(imp_Member.__init__)


def test_imp_member_constructor_args():
    sig = inspect.signature(imp_Member.__init__)
    params = list(sig.parameters.keys())



def test_imp_project_is_not_abstract():
    assert not inspect.isabstract(imp_Project)


def test_imp_project_constructor_exists():
    assert callable(imp_Project.__init__)


def test_imp_project_constructor_args():
    sig = inspect.signature(imp_Project.__init__)
    params = list(sig.parameters.keys())
    assert "ismethodcall" in params, "Missing parameter 'ismethodcall'"

def test_imp_project_has_ismethodcall():
    assert hasattr(imp_Project, "ismethodcall")
    descriptor = None
    for klass in imp_Project.__mro__:
        if "ismethodcall" in klass.__dict__:
            descriptor = klass.__dict__["ismethodcall"]
            break
    assert isinstance(descriptor, property)



def test_imp_print_is_not_abstract():
    assert not inspect.isabstract(imp_Print)


def test_imp_print_constructor_exists():
    assert callable(imp_Print.__init__)


def test_imp_print_constructor_args():
    sig = inspect.signature(imp_Print.__init__)
    params = list(sig.parameters.keys())



def test_imp_return_is_not_abstract():
    assert not inspect.isabstract(imp_Return)


def test_imp_return_constructor_exists():
    assert callable(imp_Return.__init__)


def test_imp_return_constructor_args():
    sig = inspect.signature(imp_Return.__init__)
    params = list(sig.parameters.keys())



def test_imp_paramdecl_is_not_abstract():
    assert not inspect.isabstract(imp_ParamDecl)


def test_imp_paramdecl_constructor_exists():
    assert callable(imp_ParamDecl.__init__)


def test_imp_paramdecl_constructor_args():
    sig = inspect.signature(imp_ParamDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_paramdecl_has_name():
    assert hasattr(imp_ParamDecl, "name")
    descriptor = None
    for klass in imp_ParamDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_imp_methoddecl_is_not_abstract():
    assert not inspect.isabstract(imp_MethodDecl)


def test_imp_methoddecl_constructor_exists():
    assert callable(imp_MethodDecl.__init__)


def test_imp_methoddecl_constructor_args():
    sig = inspect.signature(imp_MethodDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_methoddecl_has_name():
    assert hasattr(imp_MethodDecl, "name")
    descriptor = None
    for klass in imp_MethodDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp_attributedecl_is_not_abstract():
    assert not inspect.isabstract(imp_AttributeDecl)


def test_imp_attributedecl_constructor_exists():
    assert callable(imp_AttributeDecl.__init__)


def test_imp_attributedecl_constructor_args():
    sig = inspect.signature(imp_AttributeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_imp_attributedecl_has_name():
    assert hasattr(imp_AttributeDecl, "name")
    descriptor = None
    for klass in imp_AttributeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_imp_assignment_is_not_abstract():
    assert not inspect.isabstract(imp_Assignment)


def test_imp_assignment_constructor_exists():
    assert callable(imp_Assignment.__init__)


def test_imp_assignment_constructor_args():
    sig = inspect.signature(imp_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_imp_newclass_is_not_abstract():
    assert not inspect.isabstract(imp_NewClass)


def test_imp_newclass_constructor_exists():
    assert callable(imp_NewClass.__init__)


def test_imp_newclass_constructor_args():
    sig = inspect.signature(imp_NewClass.__init__)
    params = list(sig.parameters.keys())



def test_imp_this_is_not_abstract():
    assert not inspect.isabstract(imp_This)


def test_imp_this_constructor_exists():
    assert callable(imp_This.__init__)


def test_imp_this_constructor_args():
    sig = inspect.signature(imp_This.__init__)
    params = list(sig.parameters.keys())

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "NEGATE",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "GEQ",
        "ADD",
        "LEQ",
        "EQ",
        "MUL",
        "GT",
        "OR",
        "SUB",
        "AND",
        "LT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"


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
NamedElement_strategy = st.builds(
    NamedElement,
)
imp_NamedElement_strategy = st.builds(
    imp_NamedElement,
)
imp_Class_strategy = st.builds(
    imp_Class,
    name=
        safe_text
)
imp_Program_strategy = st.builds(
    imp_Program,
)
Value_strategy = st.builds(
    Value,
)
imp_BoolValue_strategy = st.builds(
    imp_BoolValue,
    value=
        st.booleans()
)
imp_StringValue_strategy = st.builds(
    imp_StringValue,
    value=
        safe_text
)
imp_ArrayValue_strategy = st.builds(
    imp_ArrayValue,
)
imp_IntValue_strategy = st.builds(
    imp_IntValue,
    value=
        st.integers()
)
imp_Value_strategy = st.builds(
    imp_Value,
)
imp_StringToValueMap_strategy = st.builds(
    imp_StringToValueMap,
    key=
        safe_text
)
imp_Store_strategy = st.builds(
    imp_Store,
)
Symbol_strategy = st.builds(
    Symbol,
)
Stmt_strategy = st.builds(
    Stmt,
)
imp_Expr_strategy = st.builds(
    imp_Expr,
)
imp_Block_strategy = st.builds(
    imp_Block,
)
imp_Declaration_strategy = st.builds(
    imp_Declaration,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
imp_Binary_strategy = st.builds(
    imp_Binary,
    op=
        safe_text
)
imp_ArrayDecl_strategy = st.builds(
    imp_ArrayDecl,
)
imp_BoolConst_strategy = st.builds(
    imp_BoolConst,
    value=
        st.booleans()
)
imp_StringConst_strategy = st.builds(
    imp_StringConst,
    value=
        safe_text
)
imp_Unary_strategy = st.builds(
    imp_Unary,
    op=
        safe_text
)
imp_IntConst_strategy = st.builds(
    imp_IntConst,
    value=
        st.integers()
)
imp_While_strategy = st.builds(
    imp_While,
)
imp_If_strategy = st.builds(
    imp_If,
)
imp_Stmt_strategy = st.builds(
    imp_Stmt,
)
imp_VarRef_strategy = st.builds(
    imp_VarRef,
)
imp_Symbol_strategy = st.builds(
    imp_Symbol,
)
imp_Member_strategy = st.builds(
    imp_Member,
)
imp_Project_strategy = st.builds(
    imp_Project,
    ismethodcall=
        st.booleans()
)
imp_Print_strategy = st.builds(
    imp_Print,
)
imp_Return_strategy = st.builds(
    imp_Return,
)
imp_ParamDecl_strategy = st.builds(
    imp_ParamDecl,
    name=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
imp_MethodDecl_strategy = st.builds(
    imp_MethodDecl,
    name=
        safe_text
)
imp_AttributeDecl_strategy = st.builds(
    imp_AttributeDecl,
    name=
        safe_text
)
imp_Assignment_strategy = st.builds(
    imp_Assignment,
)
imp_NewClass_strategy = st.builds(
    imp_NewClass,
)
imp_This_strategy = st.builds(
    imp_This,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=imp_NamedElement_strategy)
@settings(max_examples=50)
def test_imp_namedelement_instantiation(instance):
    assert isinstance(instance, imp_NamedElement)

@given(instance=imp_Class_strategy)
@settings(max_examples=50)
def test_imp_class_instantiation(instance):
    assert isinstance(instance, imp_Class)



@given(instance=imp_Class_strategy)
def test_imp_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp_Program_strategy)
@settings(max_examples=50)
def test_imp_program_instantiation(instance):
    assert isinstance(instance, imp_Program)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=imp_BoolValue_strategy)
@settings(max_examples=50)
def test_imp_boolvalue_instantiation(instance):
    assert isinstance(instance, imp_BoolValue)



@given(instance=imp_BoolValue_strategy)
def test_imp_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_StringValue_strategy)
@settings(max_examples=50)
def test_imp_stringvalue_instantiation(instance):
    assert isinstance(instance, imp_StringValue)



@given(instance=imp_StringValue_strategy)
def test_imp_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_ArrayValue_strategy)
@settings(max_examples=50)
def test_imp_arrayvalue_instantiation(instance):
    assert isinstance(instance, imp_ArrayValue)

@given(instance=imp_IntValue_strategy)
@settings(max_examples=50)
def test_imp_intvalue_instantiation(instance):
    assert isinstance(instance, imp_IntValue)



@given(instance=imp_IntValue_strategy)
def test_imp_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_Value_strategy)
@settings(max_examples=50)
def test_imp_value_instantiation(instance):
    assert isinstance(instance, imp_Value)

@given(instance=imp_StringToValueMap_strategy)
@settings(max_examples=50)
def test_imp_stringtovaluemap_instantiation(instance):
    assert isinstance(instance, imp_StringToValueMap)



@given(instance=imp_StringToValueMap_strategy)
def test_imp_stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=imp_Store_strategy)
@settings(max_examples=50)
def test_imp_store_instantiation(instance):
    assert isinstance(instance, imp_Store)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=imp_Expr_strategy)
@settings(max_examples=50)
def test_imp_expr_instantiation(instance):
    assert isinstance(instance, imp_Expr)

@given(instance=imp_Block_strategy)
@settings(max_examples=50)
def test_imp_block_instantiation(instance):
    assert isinstance(instance, imp_Block)

@given(instance=imp_Declaration_strategy)
@settings(max_examples=50)
def test_imp_declaration_instantiation(instance):
    assert isinstance(instance, imp_Declaration)



@given(instance=imp_Declaration_strategy)
def test_imp_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=imp_Binary_strategy)
@settings(max_examples=50)
def test_imp_binary_instantiation(instance):
    assert isinstance(instance, imp_Binary)



@given(instance=imp_Binary_strategy)
def test_imp_binary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp_ArrayDecl_strategy)
@settings(max_examples=50)
def test_imp_arraydecl_instantiation(instance):
    assert isinstance(instance, imp_ArrayDecl)

@given(instance=imp_BoolConst_strategy)
@settings(max_examples=50)
def test_imp_boolconst_instantiation(instance):
    assert isinstance(instance, imp_BoolConst)



@given(instance=imp_BoolConst_strategy)
def test_imp_boolconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_StringConst_strategy)
@settings(max_examples=50)
def test_imp_stringconst_instantiation(instance):
    assert isinstance(instance, imp_StringConst)



@given(instance=imp_StringConst_strategy)
def test_imp_stringconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_Unary_strategy)
@settings(max_examples=50)
def test_imp_unary_instantiation(instance):
    assert isinstance(instance, imp_Unary)



@given(instance=imp_Unary_strategy)
def test_imp_unary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=imp_IntConst_strategy)
@settings(max_examples=50)
def test_imp_intconst_instantiation(instance):
    assert isinstance(instance, imp_IntConst)



@given(instance=imp_IntConst_strategy)
def test_imp_intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=imp_While_strategy)
@settings(max_examples=50)
def test_imp_while_instantiation(instance):
    assert isinstance(instance, imp_While)

@given(instance=imp_If_strategy)
@settings(max_examples=50)
def test_imp_if_instantiation(instance):
    assert isinstance(instance, imp_If)

@given(instance=imp_Stmt_strategy)
@settings(max_examples=50)
def test_imp_stmt_instantiation(instance):
    assert isinstance(instance, imp_Stmt)

@given(instance=imp_VarRef_strategy)
@settings(max_examples=50)
def test_imp_varref_instantiation(instance):
    assert isinstance(instance, imp_VarRef)

@given(instance=imp_Symbol_strategy)
@settings(max_examples=50)
def test_imp_symbol_instantiation(instance):
    assert isinstance(instance, imp_Symbol)

@given(instance=imp_Member_strategy)
@settings(max_examples=50)
def test_imp_member_instantiation(instance):
    assert isinstance(instance, imp_Member)

@given(instance=imp_Project_strategy)
@settings(max_examples=50)
def test_imp_project_instantiation(instance):
    assert isinstance(instance, imp_Project)



@given(instance=imp_Project_strategy)
def test_imp_project_ismethodcall_setter(instance):
    original = instance.ismethodcall
    instance.ismethodcall = original
    assert instance.ismethodcall == original

@given(instance=imp_Print_strategy)
@settings(max_examples=50)
def test_imp_print_instantiation(instance):
    assert isinstance(instance, imp_Print)

@given(instance=imp_Return_strategy)
@settings(max_examples=50)
def test_imp_return_instantiation(instance):
    assert isinstance(instance, imp_Return)

@given(instance=imp_ParamDecl_strategy)
@settings(max_examples=50)
def test_imp_paramdecl_instantiation(instance):
    assert isinstance(instance, imp_ParamDecl)



@given(instance=imp_ParamDecl_strategy)
def test_imp_paramdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=imp_MethodDecl_strategy)
@settings(max_examples=50)
def test_imp_methoddecl_instantiation(instance):
    assert isinstance(instance, imp_MethodDecl)



@given(instance=imp_MethodDecl_strategy)
def test_imp_methoddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp_AttributeDecl_strategy)
@settings(max_examples=50)
def test_imp_attributedecl_instantiation(instance):
    assert isinstance(instance, imp_AttributeDecl)



@given(instance=imp_AttributeDecl_strategy)
def test_imp_attributedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=imp_Assignment_strategy)
@settings(max_examples=50)
def test_imp_assignment_instantiation(instance):
    assert isinstance(instance, imp_Assignment)

@given(instance=imp_NewClass_strategy)
@settings(max_examples=50)
def test_imp_newclass_instantiation(instance):
    assert isinstance(instance, imp_NewClass)

@given(instance=imp_This_strategy)
@settings(max_examples=50)
def test_imp_this_instantiation(instance):
    assert isinstance(instance, imp_This)
