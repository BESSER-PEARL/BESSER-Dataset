import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Key,
    dDL::Primary::key,
    dDL::Key,
    dDL::Sequence::options,
    dDL::Colname,
    dDL::TYPE,
    dDL::Constraint,
    dDL::Column,
    Definition,
    dDL::Create::sequence,
    dDL::Create::table,
    dDL::Definition,
    dDL::Data::definition,
    dDL::Comment,
    dDL::Tabname,
    dDL::Alter::table,
    dDL::Foreign::key,
    dDL::Unique::key,
    dDL::ISNULL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_ddl::primary::key_is_not_abstract():
    assert not inspect.isabstract(dDL::Primary::key)


def test_ddl::primary::key_constructor_exists():
    assert callable(dDL::Primary::key.__init__)


def test_ddl::primary::key_constructor_args():
    sig = inspect.signature(dDL::Primary::key.__init__)
    params = list(sig.parameters.keys())



def test_ddl::key_is_not_abstract():
    assert not inspect.isabstract(dDL::Key)


def test_ddl::key_constructor_exists():
    assert callable(dDL::Key.__init__)


def test_ddl::key_constructor_args():
    sig = inspect.signature(dDL::Key.__init__)
    params = list(sig.parameters.keys())



def test_ddl::sequence::options_is_not_abstract():
    assert not inspect.isabstract(dDL::Sequence::options)


def test_ddl::sequence::options_constructor_exists():
    assert callable(dDL::Sequence::options.__init__)


def test_ddl::sequence::options_constructor_args():
    sig = inspect.signature(dDL::Sequence::options.__init__)
    params = list(sig.parameters.keys())
    assert "increment" in params, "Missing parameter 'increment'"
    assert "minvalue" in params, "Missing parameter 'minvalue'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "noorder" in params, "Missing parameter 'noorder'"
    assert "order" in params, "Missing parameter 'order'"
    assert "nomaxvalue" in params, "Missing parameter 'nomaxvalue'"
    assert "start" in params, "Missing parameter 'start'"
    assert "cache" in params, "Missing parameter 'cache'"
    assert "maxvalue" in params, "Missing parameter 'maxvalue'"
    assert "nocache" in params, "Missing parameter 'nocache'"
    assert "nominvalue" in params, "Missing parameter 'nominvalue'"
    assert "nocycle" in params, "Missing parameter 'nocycle'"

def test_ddl::sequence::options_has_increment():
    assert hasattr(dDL::Sequence::options, "increment")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_minvalue():
    assert hasattr(dDL::Sequence::options, "minvalue")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "minvalue" in klass.__dict__:
            descriptor = klass.__dict__["minvalue"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_cycle():
    assert hasattr(dDL::Sequence::options, "cycle")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_noorder():
    assert hasattr(dDL::Sequence::options, "noorder")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "noorder" in klass.__dict__:
            descriptor = klass.__dict__["noorder"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_order():
    assert hasattr(dDL::Sequence::options, "order")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_nomaxvalue():
    assert hasattr(dDL::Sequence::options, "nomaxvalue")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "nomaxvalue" in klass.__dict__:
            descriptor = klass.__dict__["nomaxvalue"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_start():
    assert hasattr(dDL::Sequence::options, "start")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_cache():
    assert hasattr(dDL::Sequence::options, "cache")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "cache" in klass.__dict__:
            descriptor = klass.__dict__["cache"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_maxvalue():
    assert hasattr(dDL::Sequence::options, "maxvalue")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "maxvalue" in klass.__dict__:
            descriptor = klass.__dict__["maxvalue"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_nocache():
    assert hasattr(dDL::Sequence::options, "nocache")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "nocache" in klass.__dict__:
            descriptor = klass.__dict__["nocache"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_nominvalue():
    assert hasattr(dDL::Sequence::options, "nominvalue")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "nominvalue" in klass.__dict__:
            descriptor = klass.__dict__["nominvalue"]
            break
    assert isinstance(descriptor, property)

def test_ddl::sequence::options_has_nocycle():
    assert hasattr(dDL::Sequence::options, "nocycle")
    descriptor = None
    for klass in dDL::Sequence::options.__mro__:
        if "nocycle" in klass.__dict__:
            descriptor = klass.__dict__["nocycle"]
            break
    assert isinstance(descriptor, property)



def test_ddl::colname_is_not_abstract():
    assert not inspect.isabstract(dDL::Colname)


def test_ddl::colname_constructor_exists():
    assert callable(dDL::Colname.__init__)


def test_ddl::colname_constructor_args():
    sig = inspect.signature(dDL::Colname.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::colname_has_id():
    assert hasattr(dDL::Colname, "id")
    descriptor = None
    for klass in dDL::Colname.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::type_is_not_abstract():
    assert not inspect.isabstract(dDL::TYPE)


def test_ddl::type_constructor_exists():
    assert callable(dDL::TYPE.__init__)


def test_ddl::type_constructor_args():
    sig = inspect.signature(dDL::TYPE.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::type_has_id():
    assert hasattr(dDL::TYPE, "id")
    descriptor = None
    for klass in dDL::TYPE.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::constraint_is_not_abstract():
    assert not inspect.isabstract(dDL::Constraint)


def test_ddl::constraint_constructor_exists():
    assert callable(dDL::Constraint.__init__)


def test_ddl::constraint_constructor_args():
    sig = inspect.signature(dDL::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::constraint_has_id():
    assert hasattr(dDL::Constraint, "id")
    descriptor = None
    for klass in dDL::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::column_is_not_abstract():
    assert not inspect.isabstract(dDL::Column)


def test_ddl::column_constructor_exists():
    assert callable(dDL::Column.__init__)


def test_ddl::column_constructor_args():
    sig = inspect.signature(dDL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::column_has_number():
    assert hasattr(dDL::Column, "number")
    descriptor = None
    for klass in dDL::Column.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_ddl::column_has_id():
    assert hasattr(dDL::Column, "id")
    descriptor = None
    for klass in dDL::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::create::sequence_is_not_abstract():
    assert not inspect.isabstract(dDL::Create::sequence)


def test_ddl::create::sequence_constructor_exists():
    assert callable(dDL::Create::sequence.__init__)


def test_ddl::create::sequence_constructor_args():
    sig = inspect.signature(dDL::Create::sequence.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::create::sequence_has_id():
    assert hasattr(dDL::Create::sequence, "id")
    descriptor = None
    for klass in dDL::Create::sequence.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::create::table_is_not_abstract():
    assert not inspect.isabstract(dDL::Create::table)


def test_ddl::create::table_constructor_exists():
    assert callable(dDL::Create::table.__init__)


def test_ddl::create::table_constructor_args():
    sig = inspect.signature(dDL::Create::table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::create::table_has_id():
    assert hasattr(dDL::Create::table, "id")
    descriptor = None
    for klass in dDL::Create::table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::definition_is_not_abstract():
    assert not inspect.isabstract(dDL::Definition)


def test_ddl::definition_constructor_exists():
    assert callable(dDL::Definition.__init__)


def test_ddl::definition_constructor_args():
    sig = inspect.signature(dDL::Definition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::data::definition_is_not_abstract():
    assert not inspect.isabstract(dDL::Data::definition)


def test_ddl::data::definition_constructor_exists():
    assert callable(dDL::Data::definition.__init__)


def test_ddl::data::definition_constructor_args():
    sig = inspect.signature(dDL::Data::definition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::comment_is_not_abstract():
    assert not inspect.isabstract(dDL::Comment)


def test_ddl::comment_constructor_exists():
    assert callable(dDL::Comment.__init__)


def test_ddl::comment_constructor_args():
    sig = inspect.signature(dDL::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "columnId" in params, "Missing parameter 'columnId'"

def test_ddl::comment_has_string():
    assert hasattr(dDL::Comment, "string")
    descriptor = None
    for klass in dDL::Comment.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_ddl::comment_has_columnId():
    assert hasattr(dDL::Comment, "columnId")
    descriptor = None
    for klass in dDL::Comment.__mro__:
        if "columnId" in klass.__dict__:
            descriptor = klass.__dict__["columnId"]
            break
    assert isinstance(descriptor, property)



def test_ddl::tabname_is_not_abstract():
    assert not inspect.isabstract(dDL::Tabname)


def test_ddl::tabname_constructor_exists():
    assert callable(dDL::Tabname.__init__)


def test_ddl::tabname_constructor_args():
    sig = inspect.signature(dDL::Tabname.__init__)
    params = list(sig.parameters.keys())
    assert "basename" in params, "Missing parameter 'basename'"
    assert "id" in params, "Missing parameter 'id'"

def test_ddl::tabname_has_basename():
    assert hasattr(dDL::Tabname, "basename")
    descriptor = None
    for klass in dDL::Tabname.__mro__:
        if "basename" in klass.__dict__:
            descriptor = klass.__dict__["basename"]
            break
    assert isinstance(descriptor, property)

def test_ddl::tabname_has_id():
    assert hasattr(dDL::Tabname, "id")
    descriptor = None
    for klass in dDL::Tabname.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ddl::alter::table_is_not_abstract():
    assert not inspect.isabstract(dDL::Alter::table)


def test_ddl::alter::table_constructor_exists():
    assert callable(dDL::Alter::table.__init__)


def test_ddl::alter::table_constructor_args():
    sig = inspect.signature(dDL::Alter::table.__init__)
    params = list(sig.parameters.keys())
    assert "enable" in params, "Missing parameter 'enable'"
    assert "id" in params, "Missing parameter 'id'"
    assert "add" in params, "Missing parameter 'add'"

def test_ddl::alter::table_has_enable():
    assert hasattr(dDL::Alter::table, "enable")
    descriptor = None
    for klass in dDL::Alter::table.__mro__:
        if "enable" in klass.__dict__:
            descriptor = klass.__dict__["enable"]
            break
    assert isinstance(descriptor, property)

def test_ddl::alter::table_has_id():
    assert hasattr(dDL::Alter::table, "id")
    descriptor = None
    for klass in dDL::Alter::table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ddl::alter::table_has_add():
    assert hasattr(dDL::Alter::table, "add")
    descriptor = None
    for klass in dDL::Alter::table.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)



def test_ddl::foreign::key_is_not_abstract():
    assert not inspect.isabstract(dDL::Foreign::key)


def test_ddl::foreign::key_constructor_exists():
    assert callable(dDL::Foreign::key.__init__)


def test_ddl::foreign::key_constructor_args():
    sig = inspect.signature(dDL::Foreign::key.__init__)
    params = list(sig.parameters.keys())



def test_ddl::unique::key_is_not_abstract():
    assert not inspect.isabstract(dDL::Unique::key)


def test_ddl::unique::key_constructor_exists():
    assert callable(dDL::Unique::key.__init__)


def test_ddl::unique::key_constructor_args():
    sig = inspect.signature(dDL::Unique::key.__init__)
    params = list(sig.parameters.keys())



def test_ddl::isnull_is_not_abstract():
    assert not inspect.isabstract(dDL::ISNULL)


def test_ddl::isnull_constructor_exists():
    assert callable(dDL::ISNULL.__init__)


def test_ddl::isnull_constructor_args():
    sig = inspect.signature(dDL::ISNULL.__init__)
    params = list(sig.parameters.keys())
    assert "nonNull" in params, "Missing parameter 'nonNull'"
    assert "null" in params, "Missing parameter 'null'"

def test_ddl::isnull_has_nonNull():
    assert hasattr(dDL::ISNULL, "nonNull")
    descriptor = None
    for klass in dDL::ISNULL.__mro__:
        if "nonNull" in klass.__dict__:
            descriptor = klass.__dict__["nonNull"]
            break
    assert isinstance(descriptor, property)

def test_ddl::isnull_has_null():
    assert hasattr(dDL::ISNULL, "null")
    descriptor = None
    for klass in dDL::ISNULL.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
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
Key_strategy = st.builds(
    Key,
)
dDL::Primary::key_strategy = st.builds(
    dDL::Primary::key,
)
dDL::Key_strategy = st.builds(
    dDL::Key,
)
dDL::Sequence::options_strategy = st.builds(
    dDL::Sequence::options,
    increment=
        safe_text,
    minvalue=
        safe_text,
    cycle=
        safe_text,
    noorder=
        safe_text,
    order=
        safe_text,
    nomaxvalue=
        safe_text,
    start=
        safe_text,
    cache=
        safe_text,
    maxvalue=
        safe_text,
    nocache=
        safe_text,
    nominvalue=
        safe_text,
    nocycle=
        safe_text
)
dDL::Colname_strategy = st.builds(
    dDL::Colname,
    id=
        safe_text
)
dDL::TYPE_strategy = st.builds(
    dDL::TYPE,
    id=
        safe_text
)
dDL::Constraint_strategy = st.builds(
    dDL::Constraint,
    id=
        safe_text
)
dDL::Column_strategy = st.builds(
    dDL::Column,
    number=
        st.integers(),
    id=
        safe_text
)
Definition_strategy = st.builds(
    Definition,
)
dDL::Create::sequence_strategy = st.builds(
    dDL::Create::sequence,
    id=
        safe_text
)
dDL::Create::table_strategy = st.builds(
    dDL::Create::table,
    id=
        safe_text
)
dDL::Definition_strategy = st.builds(
    dDL::Definition,
)
dDL::Data::definition_strategy = st.builds(
    dDL::Data::definition,
)
dDL::Comment_strategy = st.builds(
    dDL::Comment,
    string=
        safe_text,
    columnId=
        safe_text
)
dDL::Tabname_strategy = st.builds(
    dDL::Tabname,
    basename=
        safe_text,
    id=
        safe_text
)
dDL::Alter::table_strategy = st.builds(
    dDL::Alter::table,
    enable=
        safe_text,
    id=
        safe_text,
    add=
        safe_text
)
dDL::Foreign::key_strategy = st.builds(
    dDL::Foreign::key,
)
dDL::Unique::key_strategy = st.builds(
    dDL::Unique::key,
)
dDL::ISNULL_strategy = st.builds(
    dDL::ISNULL,
    nonNull=
        st.booleans(),
    null=
        st.booleans()
)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=dDL::Primary::key_strategy)
@settings(max_examples=50)
def test_ddl::primary::key_instantiation(instance):
    assert isinstance(instance, dDL::Primary::key)

@given(instance=dDL::Key_strategy)
@settings(max_examples=50)
def test_ddl::key_instantiation(instance):
    assert isinstance(instance, dDL::Key)

@given(instance=dDL::Sequence::options_strategy)
@settings(max_examples=50)
def test_ddl::sequence::options_instantiation(instance):
    assert isinstance(instance, dDL::Sequence::options)

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_minvalue_type(instance):
    assert isinstance(instance.minvalue, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_minvalue_setter(instance):
    original = instance.minvalue
    instance.minvalue = original
    assert instance.minvalue == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_cycle_type(instance):
    assert isinstance(instance.cycle, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_noorder_type(instance):
    assert isinstance(instance.noorder, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_noorder_setter(instance):
    original = instance.noorder
    instance.noorder = original
    assert instance.noorder == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nomaxvalue_type(instance):
    assert isinstance(instance.nomaxvalue, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nomaxvalue_setter(instance):
    original = instance.nomaxvalue
    instance.nomaxvalue = original
    assert instance.nomaxvalue == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_cache_type(instance):
    assert isinstance(instance.cache, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_cache_setter(instance):
    original = instance.cache
    instance.cache = original
    assert instance.cache == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_maxvalue_type(instance):
    assert isinstance(instance.maxvalue, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_maxvalue_setter(instance):
    original = instance.maxvalue
    instance.maxvalue = original
    assert instance.maxvalue == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nocache_type(instance):
    assert isinstance(instance.nocache, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nocache_setter(instance):
    original = instance.nocache
    instance.nocache = original
    assert instance.nocache == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nominvalue_type(instance):
    assert isinstance(instance.nominvalue, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nominvalue_setter(instance):
    original = instance.nominvalue
    instance.nominvalue = original
    assert instance.nominvalue == original

@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nocycle_type(instance):
    assert isinstance(instance.nocycle, str)


@given(instance=dDL::Sequence::options_strategy)
def test_ddl::sequence::options_nocycle_setter(instance):
    original = instance.nocycle
    instance.nocycle = original
    assert instance.nocycle == original

@given(instance=dDL::Colname_strategy)
@settings(max_examples=50)
def test_ddl::colname_instantiation(instance):
    assert isinstance(instance, dDL::Colname)

@given(instance=dDL::Colname_strategy)
def test_ddl::colname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Colname_strategy)
def test_ddl::colname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::TYPE_strategy)
@settings(max_examples=50)
def test_ddl::type_instantiation(instance):
    assert isinstance(instance, dDL::TYPE)

@given(instance=dDL::TYPE_strategy)
def test_ddl::type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::TYPE_strategy)
def test_ddl::type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Constraint_strategy)
@settings(max_examples=50)
def test_ddl::constraint_instantiation(instance):
    assert isinstance(instance, dDL::Constraint)

@given(instance=dDL::Constraint_strategy)
def test_ddl::constraint_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Constraint_strategy)
def test_ddl::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Column_strategy)
@settings(max_examples=50)
def test_ddl::column_instantiation(instance):
    assert isinstance(instance, dDL::Column)

@given(instance=dDL::Column_strategy)
def test_ddl::column_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=dDL::Column_strategy)
def test_ddl::column_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=dDL::Column_strategy)
def test_ddl::column_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Column_strategy)
def test_ddl::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=dDL::Create::sequence_strategy)
@settings(max_examples=50)
def test_ddl::create::sequence_instantiation(instance):
    assert isinstance(instance, dDL::Create::sequence)

@given(instance=dDL::Create::sequence_strategy)
def test_ddl::create::sequence_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Create::sequence_strategy)
def test_ddl::create::sequence_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Create::table_strategy)
@settings(max_examples=50)
def test_ddl::create::table_instantiation(instance):
    assert isinstance(instance, dDL::Create::table)

@given(instance=dDL::Create::table_strategy)
def test_ddl::create::table_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Create::table_strategy)
def test_ddl::create::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Definition_strategy)
@settings(max_examples=50)
def test_ddl::definition_instantiation(instance):
    assert isinstance(instance, dDL::Definition)

@given(instance=dDL::Data::definition_strategy)
@settings(max_examples=50)
def test_ddl::data::definition_instantiation(instance):
    assert isinstance(instance, dDL::Data::definition)

@given(instance=dDL::Comment_strategy)
@settings(max_examples=50)
def test_ddl::comment_instantiation(instance):
    assert isinstance(instance, dDL::Comment)

@given(instance=dDL::Comment_strategy)
def test_ddl::comment_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=dDL::Comment_strategy)
def test_ddl::comment_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=dDL::Comment_strategy)
def test_ddl::comment_columnId_type(instance):
    assert isinstance(instance.columnId, str)


@given(instance=dDL::Comment_strategy)
def test_ddl::comment_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original

@given(instance=dDL::Tabname_strategy)
@settings(max_examples=50)
def test_ddl::tabname_instantiation(instance):
    assert isinstance(instance, dDL::Tabname)

@given(instance=dDL::Tabname_strategy)
def test_ddl::tabname_basename_type(instance):
    assert isinstance(instance.basename, str)


@given(instance=dDL::Tabname_strategy)
def test_ddl::tabname_basename_setter(instance):
    original = instance.basename
    instance.basename = original
    assert instance.basename == original

@given(instance=dDL::Tabname_strategy)
def test_ddl::tabname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Tabname_strategy)
def test_ddl::tabname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Alter::table_strategy)
@settings(max_examples=50)
def test_ddl::alter::table_instantiation(instance):
    assert isinstance(instance, dDL::Alter::table)

@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_enable_type(instance):
    assert isinstance(instance.enable, str)


@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original

@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_add_type(instance):
    assert isinstance(instance.add, str)


@given(instance=dDL::Alter::table_strategy)
def test_ddl::alter::table_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=dDL::Foreign::key_strategy)
@settings(max_examples=50)
def test_ddl::foreign::key_instantiation(instance):
    assert isinstance(instance, dDL::Foreign::key)

@given(instance=dDL::Unique::key_strategy)
@settings(max_examples=50)
def test_ddl::unique::key_instantiation(instance):
    assert isinstance(instance, dDL::Unique::key)

@given(instance=dDL::ISNULL_strategy)
@settings(max_examples=50)
def test_ddl::isnull_instantiation(instance):
    assert isinstance(instance, dDL::ISNULL)

@given(instance=dDL::ISNULL_strategy)
def test_ddl::isnull_nonNull_type(instance):
    assert isinstance(instance.nonNull, bool)


@given(instance=dDL::ISNULL_strategy)
def test_ddl::isnull_nonNull_setter(instance):
    original = instance.nonNull
    instance.nonNull = original
    assert instance.nonNull == original

@given(instance=dDL::ISNULL_strategy)
def test_ddl::isnull_null_type(instance):
    assert isinstance(instance.null, bool)


@given(instance=dDL::ISNULL_strategy)
def test_ddl::isnull_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original
