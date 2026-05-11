import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pascal::repetitive::arit::expression,
    expression,
    pascal::rel::expression,
    pascal::arit::expression,
    pascal::expression,
    pascal::atrib,
    pascal::statement,
    pascal::block,
    pascal::var::block,
    pascal::program,
    pascal::Pascal,
    pascal::var::list,
    pascal::var::decl,
    pascal::EObject,
    type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal::repetitive::arit::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::repetitive::arit::expression)


def test_pascal::repetitive::arit::expression_constructor_exists():
    assert callable(pascal::repetitive::arit::expression.__init__)


def test_pascal::repetitive::arit::expression_constructor_args():
    sig = inspect.signature(pascal::repetitive::arit::expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_pascal::repetitive::arit::expression_has_value():
    assert hasattr(pascal::repetitive::arit::expression, "value")
    descriptor = None
    for klass in pascal::repetitive::arit::expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_pascal::repetitive::arit::expression_has_op():
    assert hasattr(pascal::repetitive::arit::expression, "op")
    descriptor = None
    for klass in pascal::repetitive::arit::expression.__mro__:
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



def test_pascal::rel::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::rel::expression)


def test_pascal::rel::expression_constructor_exists():
    assert callable(pascal::rel::expression.__init__)


def test_pascal::rel::expression_constructor_args():
    sig = inspect.signature(pascal::rel::expression.__init__)
    params = list(sig.parameters.keys())
    assert "close" in params, "Missing parameter 'close'"
    assert "first" in params, "Missing parameter 'first'"
    assert "second" in params, "Missing parameter 'second'"
    assert "open" in params, "Missing parameter 'open'"
    assert "op" in params, "Missing parameter 'op'"

def test_pascal::rel::expression_has_close():
    assert hasattr(pascal::rel::expression, "close")
    descriptor = None
    for klass in pascal::rel::expression.__mro__:
        if "close" in klass.__dict__:
            descriptor = klass.__dict__["close"]
            break
    assert isinstance(descriptor, property)

def test_pascal::rel::expression_has_first():
    assert hasattr(pascal::rel::expression, "first")
    descriptor = None
    for klass in pascal::rel::expression.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_pascal::rel::expression_has_second():
    assert hasattr(pascal::rel::expression, "second")
    descriptor = None
    for klass in pascal::rel::expression.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_pascal::rel::expression_has_open():
    assert hasattr(pascal::rel::expression, "open")
    descriptor = None
    for klass in pascal::rel::expression.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_pascal::rel::expression_has_op():
    assert hasattr(pascal::rel::expression, "op")
    descriptor = None
    for klass in pascal::rel::expression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pascal::arit::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::arit::expression)


def test_pascal::arit::expression_constructor_exists():
    assert callable(pascal::arit::expression.__init__)


def test_pascal::arit::expression_constructor_args():
    sig = inspect.signature(pascal::arit::expression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pascal::arit::expression_has_value():
    assert hasattr(pascal::arit::expression, "value")
    descriptor = None
    for klass in pascal::arit::expression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pascal::expression_is_not_abstract():
    assert not inspect.isabstract(pascal::expression)


def test_pascal::expression_constructor_exists():
    assert callable(pascal::expression.__init__)


def test_pascal::expression_constructor_args():
    sig = inspect.signature(pascal::expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal::atrib_is_not_abstract():
    assert not inspect.isabstract(pascal::atrib)


def test_pascal::atrib_constructor_exists():
    assert callable(pascal::atrib.__init__)


def test_pascal::atrib_constructor_args():
    sig = inspect.signature(pascal::atrib.__init__)
    params = list(sig.parameters.keys())
    assert "var_id" in params, "Missing parameter 'var_id'"

def test_pascal::atrib_has_var_id():
    assert hasattr(pascal::atrib, "var_id")
    descriptor = None
    for klass in pascal::atrib.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)



def test_pascal::statement_is_not_abstract():
    assert not inspect.isabstract(pascal::statement)


def test_pascal::statement_constructor_exists():
    assert callable(pascal::statement.__init__)


def test_pascal::statement_constructor_args():
    sig = inspect.signature(pascal::statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal::block_is_not_abstract():
    assert not inspect.isabstract(pascal::block)


def test_pascal::block_constructor_exists():
    assert callable(pascal::block.__init__)


def test_pascal::block_constructor_args():
    sig = inspect.signature(pascal::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::var::block_is_not_abstract():
    assert not inspect.isabstract(pascal::var::block)


def test_pascal::var::block_constructor_exists():
    assert callable(pascal::var::block.__init__)


def test_pascal::var::block_constructor_args():
    sig = inspect.signature(pascal::var::block.__init__)
    params = list(sig.parameters.keys())



def test_pascal::program_is_not_abstract():
    assert not inspect.isabstract(pascal::program)


def test_pascal::program_constructor_exists():
    assert callable(pascal::program.__init__)


def test_pascal::program_constructor_args():
    sig = inspect.signature(pascal::program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::program_has_name():
    assert hasattr(pascal::program, "name")
    descriptor = None
    for klass in pascal::program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::pascal_is_not_abstract():
    assert not inspect.isabstract(pascal::Pascal)


def test_pascal::pascal_constructor_exists():
    assert callable(pascal::Pascal.__init__)


def test_pascal::pascal_constructor_args():
    sig = inspect.signature(pascal::Pascal.__init__)
    params = list(sig.parameters.keys())



def test_pascal::var::list_is_not_abstract():
    assert not inspect.isabstract(pascal::var::list)


def test_pascal::var::list_constructor_exists():
    assert callable(pascal::var::list.__init__)


def test_pascal::var::list_constructor_args():
    sig = inspect.signature(pascal::var::list.__init__)
    params = list(sig.parameters.keys())
    assert "var_type" in params, "Missing parameter 'var_type'"
    assert "var_id" in params, "Missing parameter 'var_id'"
    assert "var_ids" in params, "Missing parameter 'var_ids'"

def test_pascal::var::list_has_var_type():
    assert hasattr(pascal::var::list, "var_type")
    descriptor = None
    for klass in pascal::var::list.__mro__:
        if "var_type" in klass.__dict__:
            descriptor = klass.__dict__["var_type"]
            break
    assert isinstance(descriptor, property)

def test_pascal::var::list_has_var_id():
    assert hasattr(pascal::var::list, "var_id")
    descriptor = None
    for klass in pascal::var::list.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)

def test_pascal::var::list_has_var_ids():
    assert hasattr(pascal::var::list, "var_ids")
    descriptor = None
    for klass in pascal::var::list.__mro__:
        if "var_ids" in klass.__dict__:
            descriptor = klass.__dict__["var_ids"]
            break
    assert isinstance(descriptor, property)



def test_pascal::var::decl_is_not_abstract():
    assert not inspect.isabstract(pascal::var::decl)


def test_pascal::var::decl_constructor_exists():
    assert callable(pascal::var::decl.__init__)


def test_pascal::var::decl_constructor_args():
    sig = inspect.signature(pascal::var::decl.__init__)
    params = list(sig.parameters.keys())
    assert "var_type" in params, "Missing parameter 'var_type'"
    assert "value" in params, "Missing parameter 'value'"
    assert "var_id" in params, "Missing parameter 'var_id'"

def test_pascal::var::decl_has_var_type():
    assert hasattr(pascal::var::decl, "var_type")
    descriptor = None
    for klass in pascal::var::decl.__mro__:
        if "var_type" in klass.__dict__:
            descriptor = klass.__dict__["var_type"]
            break
    assert isinstance(descriptor, property)

def test_pascal::var::decl_has_value():
    assert hasattr(pascal::var::decl, "value")
    descriptor = None
    for klass in pascal::var::decl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_pascal::var::decl_has_var_id():
    assert hasattr(pascal::var::decl, "var_id")
    descriptor = None
    for klass in pascal::var::decl.__mro__:
        if "var_id" in klass.__dict__:
            descriptor = klass.__dict__["var_id"]
            break
    assert isinstance(descriptor, property)



def test_pascal::eobject_is_not_abstract():
    assert not inspect.isabstract(pascal::EObject)


def test_pascal::eobject_constructor_exists():
    assert callable(pascal::EObject.__init__)


def test_pascal::eobject_constructor_args():
    sig = inspect.signature(pascal::EObject.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in type]
    expected_literals = [
        "BOOLEAN",
        "INTEGER",
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
pascal::repetitive::arit::expression_strategy = st.builds(
    pascal::repetitive::arit::expression,
    value=
        safe_text,
    op=
        safe_text
)
expression_strategy = st.builds(
    expression,
)
pascal::rel::expression_strategy = st.builds(
    pascal::rel::expression,
    close=
        safe_text,
    first=
        safe_text,
    second=
        safe_text,
    open=
        safe_text,
    op=
        safe_text
)
pascal::arit::expression_strategy = st.builds(
    pascal::arit::expression,
    value=
        safe_text
)
pascal::expression_strategy = st.builds(
    pascal::expression,
)
pascal::atrib_strategy = st.builds(
    pascal::atrib,
    var_id=
        safe_text
)
pascal::statement_strategy = st.builds(
    pascal::statement,
)
pascal::block_strategy = st.builds(
    pascal::block,
)
pascal::var::block_strategy = st.builds(
    pascal::var::block,
)
pascal::program_strategy = st.builds(
    pascal::program,
    name=
        safe_text
)
pascal::Pascal_strategy = st.builds(
    pascal::Pascal,
)
pascal::var::list_strategy = st.builds(
    pascal::var::list,
    var_type=
        safe_text,
    var_id=
        safe_text,
    var_ids=
        safe_text
)
pascal::var::decl_strategy = st.builds(
    pascal::var::decl,
    var_type=
        safe_text,
    value=
        safe_text,
    var_id=
        safe_text
)
pascal::EObject_strategy = st.builds(
    pascal::EObject,
)

@given(instance=pascal::repetitive::arit::expression_strategy)
@settings(max_examples=50)
def test_pascal::repetitive::arit::expression_instantiation(instance):
    assert isinstance(instance, pascal::repetitive::arit::expression)

@given(instance=pascal::repetitive::arit::expression_strategy)
def test_pascal::repetitive::arit::expression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pascal::repetitive::arit::expression_strategy)
def test_pascal::repetitive::arit::expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pascal::repetitive::arit::expression_strategy)
def test_pascal::repetitive::arit::expression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pascal::repetitive::arit::expression_strategy)
def test_pascal::repetitive::arit::expression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=pascal::rel::expression_strategy)
@settings(max_examples=50)
def test_pascal::rel::expression_instantiation(instance):
    assert isinstance(instance, pascal::rel::expression)

@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_close_type(instance):
    assert isinstance(instance.close, str)


@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_close_setter(instance):
    original = instance.close
    instance.close = original
    assert instance.close == original

@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_first_type(instance):
    assert isinstance(instance.first, str)


@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_open_type(instance):
    assert isinstance(instance.open, str)


@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pascal::rel::expression_strategy)
def test_pascal::rel::expression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pascal::arit::expression_strategy)
@settings(max_examples=50)
def test_pascal::arit::expression_instantiation(instance):
    assert isinstance(instance, pascal::arit::expression)

@given(instance=pascal::arit::expression_strategy)
def test_pascal::arit::expression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pascal::arit::expression_strategy)
def test_pascal::arit::expression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pascal::expression_strategy)
@settings(max_examples=50)
def test_pascal::expression_instantiation(instance):
    assert isinstance(instance, pascal::expression)

@given(instance=pascal::atrib_strategy)
@settings(max_examples=50)
def test_pascal::atrib_instantiation(instance):
    assert isinstance(instance, pascal::atrib)

@given(instance=pascal::atrib_strategy)
def test_pascal::atrib_var_id_type(instance):
    assert isinstance(instance.var_id, str)


@given(instance=pascal::atrib_strategy)
def test_pascal::atrib_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original

@given(instance=pascal::statement_strategy)
@settings(max_examples=50)
def test_pascal::statement_instantiation(instance):
    assert isinstance(instance, pascal::statement)

@given(instance=pascal::block_strategy)
@settings(max_examples=50)
def test_pascal::block_instantiation(instance):
    assert isinstance(instance, pascal::block)

@given(instance=pascal::var::block_strategy)
@settings(max_examples=50)
def test_pascal::var::block_instantiation(instance):
    assert isinstance(instance, pascal::var::block)

@given(instance=pascal::program_strategy)
@settings(max_examples=50)
def test_pascal::program_instantiation(instance):
    assert isinstance(instance, pascal::program)

@given(instance=pascal::program_strategy)
def test_pascal::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::program_strategy)
def test_pascal::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::Pascal_strategy)
@settings(max_examples=50)
def test_pascal::pascal_instantiation(instance):
    assert isinstance(instance, pascal::Pascal)

@given(instance=pascal::var::list_strategy)
@settings(max_examples=50)
def test_pascal::var::list_instantiation(instance):
    assert isinstance(instance, pascal::var::list)

@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_type_type(instance):
    assert isinstance(instance.var_type, str)


@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_type_setter(instance):
    original = instance.var_type
    instance.var_type = original
    assert instance.var_type == original

@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_id_type(instance):
    assert isinstance(instance.var_id, str)


@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original

@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_ids_type(instance):
    assert isinstance(instance.var_ids, str)


@given(instance=pascal::var::list_strategy)
def test_pascal::var::list_var_ids_setter(instance):
    original = instance.var_ids
    instance.var_ids = original
    assert instance.var_ids == original

@given(instance=pascal::var::decl_strategy)
@settings(max_examples=50)
def test_pascal::var::decl_instantiation(instance):
    assert isinstance(instance, pascal::var::decl)

@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_var_type_type(instance):
    assert isinstance(instance.var_type, str)


@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_var_type_setter(instance):
    original = instance.var_type
    instance.var_type = original
    assert instance.var_type == original

@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_var_id_type(instance):
    assert isinstance(instance.var_id, str)


@given(instance=pascal::var::decl_strategy)
def test_pascal::var::decl_var_id_setter(instance):
    original = instance.var_id
    instance.var_id = original
    assert instance.var_id == original

@given(instance=pascal::EObject_strategy)
@settings(max_examples=50)
def test_pascal::eobject_instantiation(instance):
    assert isinstance(instance, pascal::EObject)
