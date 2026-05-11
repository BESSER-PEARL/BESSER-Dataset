import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Operation,
    Trmodel::Update,
    Trmodel::Delete,
    Trmodel::Add,
    Trmodel::Column,
    Trmodel::Table,
    Trmodel::LoadModel,
    Trmodel::Operation,
    Trmodel::loader,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_trmodel::update_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Update)


def test_trmodel::update_constructor_exists():
    assert callable(Trmodel::Update.__init__)


def test_trmodel::update_constructor_args():
    sig = inspect.signature(Trmodel::Update.__init__)
    params = list(sig.parameters.keys())
    assert "newName" in params, "Missing parameter 'newName'"

def test_trmodel::update_has_newName():
    assert hasattr(Trmodel::Update, "newName")
    descriptor = None
    for klass in Trmodel::Update.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)



def test_trmodel::delete_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Delete)


def test_trmodel::delete_constructor_exists():
    assert callable(Trmodel::Delete.__init__)


def test_trmodel::delete_constructor_args():
    sig = inspect.signature(Trmodel::Delete.__init__)
    params = list(sig.parameters.keys())



def test_trmodel::add_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Add)


def test_trmodel::add_constructor_exists():
    assert callable(Trmodel::Add.__init__)


def test_trmodel::add_constructor_args():
    sig = inspect.signature(Trmodel::Add.__init__)
    params = list(sig.parameters.keys())



def test_trmodel::column_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Column)


def test_trmodel::column_constructor_exists():
    assert callable(Trmodel::Column.__init__)


def test_trmodel::column_constructor_args():
    sig = inspect.signature(Trmodel::Column.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_trmodel::column_has_Name():
    assert hasattr(Trmodel::Column, "Name")
    descriptor = None
    for klass in Trmodel::Column.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_trmodel::column_has_tableName():
    assert hasattr(Trmodel::Column, "tableName")
    descriptor = None
    for klass in Trmodel::Column.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_trmodel::table_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Table)


def test_trmodel::table_constructor_exists():
    assert callable(Trmodel::Table.__init__)


def test_trmodel::table_constructor_args():
    sig = inspect.signature(Trmodel::Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_trmodel::table_has_Name():
    assert hasattr(Trmodel::Table, "Name")
    descriptor = None
    for klass in Trmodel::Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_trmodel::loadmodel_is_not_abstract():
    assert not inspect.isabstract(Trmodel::LoadModel)


def test_trmodel::loadmodel_constructor_exists():
    assert callable(Trmodel::LoadModel.__init__)


def test_trmodel::loadmodel_constructor_args():
    sig = inspect.signature(Trmodel::LoadModel.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_trmodel::loadmodel_has_url():
    assert hasattr(Trmodel::LoadModel, "url")
    descriptor = None
    for klass in Trmodel::LoadModel.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_trmodel::operation_is_not_abstract():
    assert not inspect.isabstract(Trmodel::Operation)


def test_trmodel::operation_constructor_exists():
    assert callable(Trmodel::Operation.__init__)


def test_trmodel::operation_constructor_args():
    sig = inspect.signature(Trmodel::Operation.__init__)
    params = list(sig.parameters.keys())



def test_trmodel::loader_is_not_abstract():
    assert not inspect.isabstract(Trmodel::loader)


def test_trmodel::loader_constructor_exists():
    assert callable(Trmodel::loader.__init__)


def test_trmodel::loader_constructor_args():
    sig = inspect.signature(Trmodel::loader.__init__)
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
Operation_strategy = st.builds(
    Operation,
)
Trmodel::Update_strategy = st.builds(
    Trmodel::Update,
    newName=
        safe_text
)
Trmodel::Delete_strategy = st.builds(
    Trmodel::Delete,
)
Trmodel::Add_strategy = st.builds(
    Trmodel::Add,
)
Trmodel::Column_strategy = st.builds(
    Trmodel::Column,
    Name=
        safe_text,
    tableName=
        safe_text
)
Trmodel::Table_strategy = st.builds(
    Trmodel::Table,
    Name=
        safe_text
)
Trmodel::LoadModel_strategy = st.builds(
    Trmodel::LoadModel,
    url=
        safe_text
)
Trmodel::Operation_strategy = st.builds(
    Trmodel::Operation,
)
Trmodel::loader_strategy = st.builds(
    Trmodel::loader,
)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Trmodel::Update_strategy)
@settings(max_examples=50)
def test_trmodel::update_instantiation(instance):
    assert isinstance(instance, Trmodel::Update)

@given(instance=Trmodel::Update_strategy)
def test_trmodel::update_newName_type(instance):
    assert isinstance(instance.newName, str)


@given(instance=Trmodel::Update_strategy)
def test_trmodel::update_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original

@given(instance=Trmodel::Delete_strategy)
@settings(max_examples=50)
def test_trmodel::delete_instantiation(instance):
    assert isinstance(instance, Trmodel::Delete)

@given(instance=Trmodel::Add_strategy)
@settings(max_examples=50)
def test_trmodel::add_instantiation(instance):
    assert isinstance(instance, Trmodel::Add)

@given(instance=Trmodel::Column_strategy)
@settings(max_examples=50)
def test_trmodel::column_instantiation(instance):
    assert isinstance(instance, Trmodel::Column)

@given(instance=Trmodel::Column_strategy)
def test_trmodel::column_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Trmodel::Column_strategy)
def test_trmodel::column_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Trmodel::Column_strategy)
def test_trmodel::column_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=Trmodel::Column_strategy)
def test_trmodel::column_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=Trmodel::Table_strategy)
@settings(max_examples=50)
def test_trmodel::table_instantiation(instance):
    assert isinstance(instance, Trmodel::Table)

@given(instance=Trmodel::Table_strategy)
def test_trmodel::table_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Trmodel::Table_strategy)
def test_trmodel::table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Trmodel::LoadModel_strategy)
@settings(max_examples=50)
def test_trmodel::loadmodel_instantiation(instance):
    assert isinstance(instance, Trmodel::LoadModel)

@given(instance=Trmodel::LoadModel_strategy)
def test_trmodel::loadmodel_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=Trmodel::LoadModel_strategy)
def test_trmodel::loadmodel_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=Trmodel::Operation_strategy)
@settings(max_examples=50)
def test_trmodel::operation_instantiation(instance):
    assert isinstance(instance, Trmodel::Operation)

@given(instance=Trmodel::loader_strategy)
@settings(max_examples=50)
def test_trmodel::loader_instantiation(instance):
    assert isinstance(instance, Trmodel::loader)
