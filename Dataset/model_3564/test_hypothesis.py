import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pascal_repetitive_arit_expression,
    expression,
    pascal_rel_expression,
    pascal_arit_expression,
    pascal_expression,
    pascal_atrib,
    pascal_statement,
    pascal_block,
    pascal_var_block,
    pascal_program,
    pascal_Pascal,
    pascal_var_list,
    pascal_var_decl,
    pascal_EObject,
    type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal_repetitive_arit_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_repetitive_arit_expression)


def test_pascal_repetitive_arit_expression_constructor_exists():
    assert callable(pascal_repetitive_arit_expression.__init__)


def test_pascal_repetitive_arit_expression_constructor_args():
    sig = inspect.signature(pascal_repetitive_arit_expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_pascal_repetitive_arit_expression_has_value():
    assert hasattr(pascal_repetitive_arit_expression, "value")
    descriptor = None
    for klass in pascal_repetitive_arit_expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_pascal_repetitive_arit_expression_has_op():
    assert hasattr(pascal_repetitive_arit_expression, "op")
    descriptor = None
    for klass in pascal_repetitive_arit_expression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(expression)


def test_expression_constructor_exists():
    assert callable(expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal_rel_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_rel_expression)


def test_pascal_rel_expression_constructor_exists():
    assert callable(pascal_rel_expression.__init__)


def test_pascal_rel_expression_constructor_args():
    sig = inspect.signature(pascal_rel_expression.__init__)
    params = list(sig.parameters.keys())
    assert "close" in params, "Missing parameter 'close'"
    assert "second" in params, "Missing parameter 'second'"
    assert "first" in params, "Missing parameter 'first'"
    assert "op" in params, "Missing parameter 'op'"
    assert "open" in params, "Missing parameter 'open'"

def test_pascal_rel_expression_has_close():
    assert hasattr(pascal_rel_expression, "close")
    descriptor = None
    for klass in pascal_rel_expression.__mro__:
        if "close" in klass.__dict__:
            descriptor = klass.__dict__["close"]
            break
    assert isinstance(descriptor, property)

def test_pascal_rel_expression_has_second():
    assert hasattr(pascal_rel_expression, "second")
    descriptor = None
    for klass in pascal_rel_expression.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_pascal_rel_expression_has_first():
    assert hasattr(pascal_rel_expression, "first")
    descriptor = None
    for klass in pascal_rel_expression.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_pascal_rel_expression_has_op():
    assert hasattr(pascal_rel_expression, "op")
    descriptor = None
    for klass in pascal_rel_expression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_pascal_rel_expression_has_open():
    assert hasattr(pascal_rel_expression, "open")
    descriptor = None
    for klass in pascal_rel_expression.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)



def test_pascal_arit_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_arit_expression)


def test_pascal_arit_expression_constructor_exists():
    assert callable(pascal_arit_expression.__init__)


def test_pascal_arit_expression_constructor_args():
    sig = inspect.signature(pascal_arit_expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pascal_arit_expression_has_value():
    assert hasattr(pascal_arit_expression, "value")
    descriptor = None
    for klass in pascal_arit_expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal_atrib_is_not_abstract():
    assert not inspect.isabstract(pascal_atrib)


def test_pascal_atrib_constructor_exists():
    assert callable(pascal_atrib.__init__)


def test_pascal_atrib_constructor_args():
    sig = inspect.signature(pascal_atrib.__init__)
    params = list(sig.parameters.keys())
    assert "var_id" in params, "Missing parameter 'var_id'"

def test_pascal_atrib_has_var_id():
    assert hasattr(pascal_atrib, "var_id")
    descriptor = None
    for klass in pascal_atrib.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)



def test_pascal_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_statement)


def test_pascal_statement_constructor_exists():
    assert callable(pascal_statement.__init__)


def test_pascal_statement_constructor_args():
    sig = inspect.signature(pascal_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_block_is_not_abstract():
    assert not inspect.isabstract(pascal_block)


def test_pascal_block_constructor_exists():
    assert callable(pascal_block.__init__)


def test_pascal_block_constructor_args():
    sig = inspect.signature(pascal_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_var_block_is_not_abstract():
    assert not inspect.isabstract(pascal_var_block)


def test_pascal_var_block_constructor_exists():
    assert callable(pascal_var_block.__init__)


def test_pascal_var_block_constructor_args():
    sig = inspect.signature(pascal_var_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_program_has_name():
    assert hasattr(pascal_program, "name")
    descriptor = None
    for klass in pascal_program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_pascal_is_not_abstract():
    assert not inspect.isabstract(pascal_Pascal)


def test_pascal_pascal_constructor_exists():
    assert callable(pascal_Pascal.__init__)


def test_pascal_pascal_constructor_args():
    sig = inspect.signature(pascal_Pascal.__init__)
    params = list(sig.parameters.keys())



def test_pascal_var_list_is_not_abstract():
    assert not inspect.isabstract(pascal_var_list)


def test_pascal_var_list_constructor_exists():
    assert callable(pascal_var_list.__init__)


def test_pascal_var_list_constructor_args():
    sig = inspect.signature(pascal_var_list.__init__)
    params = list(sig.parameters.keys())
    assert "var_id" in params, "Missing parameter 'var_id'"
    assert "var_ids" in params, "Missing parameter 'var_ids'"
    assert "var_type" in params, "Missing parameter 'var_type'"

def test_pascal_var_list_has_var_id():
    assert hasattr(pascal_var_list, "var_id")
    descriptor = None
    for klass in pascal_var_list.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)

def test_pascal_var_list_has_var_ids():
    assert hasattr(pascal_var_list, "var_ids")
    descriptor = None
    for klass in pascal_var_list.__mro__:
        if "var_ids" in klass.__dict__:
            descriptor = klass.__dict__["var_ids"]
            break
    assert isinstance(descriptor, property)

def test_pascal_var_list_has_var_type():
    assert hasattr(pascal_var_list, "var_type")
    descriptor = None
    for klass in pascal_var_list.__mro__:
        if "var_type" in klass.__dict__:
            descriptor = klass.__dict__["var_type"]
            break
    assert isinstance(descriptor, property)



def test_pascal_var_decl_is_not_abstract():
    assert not inspect.isabstract(pascal_var_decl)


def test_pascal_var_decl_constructor_exists():
    assert callable(pascal_var_decl.__init__)


def test_pascal_var_decl_constructor_args():
    sig = inspect.signature(pascal_var_decl.__init__)
    params = list(sig.parameters.keys())
    assert "var_id" in params, "Missing parameter 'var_id'"
    assert "var_type" in params, "Missing parameter 'var_type'"
    assert "value" in params, "Missing parameter 'value'"

def test_pascal_var_decl_has_var_id():
    assert hasattr(pascal_var_decl, "var_id")
    descriptor = None
    for klass in pascal_var_decl.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)

def test_pascal_var_decl_has_var_type():
    assert hasattr(pascal_var_decl, "var_type")
    descriptor = None
    for klass in pascal_var_decl.__mro__:
        if "var_type" in klass.__dict__:
            descriptor = klass.__dict__["var_type"]
            break
    assert isinstance(descriptor, property)

def test_pascal_var_decl_has_value():
    assert hasattr(pascal_var_decl, "value")
    descriptor = None
    for klass in pascal_var_decl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pascal_eobject_is_not_abstract():
    assert not inspect.isabstract(pascal_EObject)


def test_pascal_eobject_constructor_exists():
    assert callable(pascal_EObject.__init__)


def test_pascal_eobject_constructor_args():
    sig = inspect.signature(pascal_EObject.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in type]
    expected_literals = [
        "INTEGER",
        "BOOLEAN",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in type"


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
pascal_repetitive_arit_expression_strategy = st.builds(
    pascal_repetitive_arit_expression,
    value=
        safe_text,
    op=
        safe_text
)
expression_strategy = st.builds(
    expression,
)
pascal_rel_expression_strategy = st.builds(
    pascal_rel_expression,
    close=
        safe_text,
    second=
        safe_text,
    first=
        safe_text,
    op=
        safe_text,
    open=
        safe_text
)
pascal_arit_expression_strategy = st.builds(
    pascal_arit_expression,
    value=
        safe_text
)
pascal_expression_strategy = st.builds(
    pascal_expression,
)
pascal_atrib_strategy = st.builds(
    pascal_atrib,
    var_id=
        safe_text
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_var_block_strategy = st.builds(
    pascal_var_block,
)
pascal_program_strategy = st.builds(
    pascal_program,
    name=
        safe_text
)
pascal_Pascal_strategy = st.builds(
    pascal_Pascal,
)
pascal_var_list_strategy = st.builds(
    pascal_var_list,
    var_id=
        safe_text,
    var_ids=
        safe_text,
    var_type=
        safe_text
)
pascal_var_decl_strategy = st.builds(
    pascal_var_decl,
    var_id=
        safe_text,
    var_type=
        safe_text,
    value=
        safe_text
)
pascal_EObject_strategy = st.builds(
    pascal_EObject,
)

@given(instance=pascal_repetitive_arit_expression_strategy)
@settings(max_examples=50)
def test_pascal_repetitive_arit_expression_instantiation(instance):
    assert isinstance(instance, pascal_repetitive_arit_expression)



@given(instance=pascal_repetitive_arit_expression_strategy)
def test_pascal_repetitive_arit_expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=pascal_repetitive_arit_expression_strategy)
def test_pascal_repetitive_arit_expression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=pascal_rel_expression_strategy)
@settings(max_examples=50)
def test_pascal_rel_expression_instantiation(instance):
    assert isinstance(instance, pascal_rel_expression)



@given(instance=pascal_rel_expression_strategy)
def test_pascal_rel_expression_close_setter(instance):
    original = instance.close
    instance.close = original
    assert instance.close == original



@given(instance=pascal_rel_expression_strategy)
def test_pascal_rel_expression_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=pascal_rel_expression_strategy)
def test_pascal_rel_expression_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original



@given(instance=pascal_rel_expression_strategy)
def test_pascal_rel_expression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=pascal_rel_expression_strategy)
def test_pascal_rel_expression_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=pascal_arit_expression_strategy)
@settings(max_examples=50)
def test_pascal_arit_expression_instantiation(instance):
    assert isinstance(instance, pascal_arit_expression)



@given(instance=pascal_arit_expression_strategy)
def test_pascal_arit_expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pascal_expression_strategy)
@settings(max_examples=50)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)

@given(instance=pascal_atrib_strategy)
@settings(max_examples=50)
def test_pascal_atrib_instantiation(instance):
    assert isinstance(instance, pascal_atrib)



@given(instance=pascal_atrib_strategy)
def test_pascal_atrib_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original

@given(instance=pascal_statement_strategy)
@settings(max_examples=50)
def test_pascal_statement_instantiation(instance):
    assert isinstance(instance, pascal_statement)

@given(instance=pascal_block_strategy)
@settings(max_examples=50)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)

@given(instance=pascal_var_block_strategy)
@settings(max_examples=50)
def test_pascal_var_block_instantiation(instance):
    assert isinstance(instance, pascal_var_block)

@given(instance=pascal_program_strategy)
@settings(max_examples=50)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)



@given(instance=pascal_program_strategy)
def test_pascal_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_Pascal_strategy)
@settings(max_examples=50)
def test_pascal_pascal_instantiation(instance):
    assert isinstance(instance, pascal_Pascal)

@given(instance=pascal_var_list_strategy)
@settings(max_examples=50)
def test_pascal_var_list_instantiation(instance):
    assert isinstance(instance, pascal_var_list)



@given(instance=pascal_var_list_strategy)
def test_pascal_var_list_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original



@given(instance=pascal_var_list_strategy)
def test_pascal_var_list_var_ids_setter(instance):
    original = instance.var_ids
    instance.var_ids = original
    assert instance.var_ids == original



@given(instance=pascal_var_list_strategy)
def test_pascal_var_list_var_type_setter(instance):
    original = instance.var_type
    instance.var_type = original
    assert instance.var_type == original

@given(instance=pascal_var_decl_strategy)
@settings(max_examples=50)
def test_pascal_var_decl_instantiation(instance):
    assert isinstance(instance, pascal_var_decl)



@given(instance=pascal_var_decl_strategy)
def test_pascal_var_decl_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original



@given(instance=pascal_var_decl_strategy)
def test_pascal_var_decl_var_type_setter(instance):
    original = instance.var_type
    instance.var_type = original
    assert instance.var_type == original



@given(instance=pascal_var_decl_strategy)
def test_pascal_var_decl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pascal_EObject_strategy)
@settings(max_examples=50)
def test_pascal_eobject_instantiation(instance):
    assert isinstance(instance, pascal_EObject)
