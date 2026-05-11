import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Field,
    Form,
    webApplication::content::CRUDForm,
    Link,
    Content,
    webApplication::content::Menu,
    webApplication::content::MultipleContent,
    webApplication::content::SingleContent,
    RelatedEntity,
    Column,
    Page,
    DataSource,
    Entity,
    Named,
    webApplication::content::Field,
    webApplication::content::Form,
    webApplication::content::Link,
    webApplication::content::Content,
    webApplication::data::Entity,
    webApplication::data::Column,
    webApplication::data::RelatedEntity,
    webApplication::content::Page,
    webApplication::data::DataSource,
    webApplication::WebApplicationModel,
    webApplication::Named,
    ColumnType,
    FieldType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_form_is_not_abstract():
    assert not inspect.isabstract(Form)


def test_form_constructor_exists():
    assert callable(Form.__init__)


def test_form_constructor_args():
    sig = inspect.signature(Form.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::crudform_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::CRUDForm)


def test_webapplication::content::crudform_constructor_exists():
    assert callable(webApplication::content::CRUDForm.__init__)


def test_webapplication::content::crudform_constructor_args():
    sig = inspect.signature(webApplication::content::CRUDForm.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_content_constructor_exists():
    assert callable(Content.__init__)


def test_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::menu_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Menu)


def test_webapplication::content::menu_constructor_exists():
    assert callable(webApplication::content::Menu.__init__)


def test_webapplication::content::menu_constructor_args():
    sig = inspect.signature(webApplication::content::Menu.__init__)
    params = list(sig.parameters.keys())
    assert "itemName" in params, "Missing parameter 'itemName'"
    assert "order" in params, "Missing parameter 'order'"
    assert "url" in params, "Missing parameter 'url'"

def test_webapplication::content::menu_has_itemName():
    assert hasattr(webApplication::content::Menu, "itemName")
    descriptor = None
    for klass in webApplication::content::Menu.__mro__:
        if "itemName" in klass.__dict__:
            descriptor = klass.__dict__["itemName"]
            break
    assert isinstance(descriptor, property)

def test_webapplication::content::menu_has_order():
    assert hasattr(webApplication::content::Menu, "order")
    descriptor = None
    for klass in webApplication::content::Menu.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_webapplication::content::menu_has_url():
    assert hasattr(webApplication::content::Menu, "url")
    descriptor = None
    for klass in webApplication::content::Menu.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_webapplication::content::multiplecontent_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::MultipleContent)


def test_webapplication::content::multiplecontent_constructor_exists():
    assert callable(webApplication::content::MultipleContent.__init__)


def test_webapplication::content::multiplecontent_constructor_args():
    sig = inspect.signature(webApplication::content::MultipleContent.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "paginated" in params, "Missing parameter 'paginated'"

def test_webapplication::content::multiplecontent_has_size():
    assert hasattr(webApplication::content::MultipleContent, "size")
    descriptor = None
    for klass in webApplication::content::MultipleContent.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_webapplication::content::multiplecontent_has_paginated():
    assert hasattr(webApplication::content::MultipleContent, "paginated")
    descriptor = None
    for klass in webApplication::content::MultipleContent.__mro__:
        if "paginated" in klass.__dict__:
            descriptor = klass.__dict__["paginated"]
            break
    assert isinstance(descriptor, property)



def test_webapplication::content::singlecontent_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::SingleContent)


def test_webapplication::content::singlecontent_constructor_exists():
    assert callable(webApplication::content::SingleContent.__init__)


def test_webapplication::content::singlecontent_constructor_args():
    sig = inspect.signature(webApplication::content::SingleContent.__init__)
    params = list(sig.parameters.keys())



def test_relatedentity_is_not_abstract():
    assert not inspect.isabstract(RelatedEntity)


def test_relatedentity_constructor_exists():
    assert callable(RelatedEntity.__init__)


def test_relatedentity_constructor_args():
    sig = inspect.signature(RelatedEntity.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datasource_is_not_abstract():
    assert not inspect.isabstract(DataSource)


def test_datasource_constructor_exists():
    assert callable(DataSource.__init__)


def test_datasource_constructor_args():
    sig = inspect.signature(DataSource.__init__)
    params = list(sig.parameters.keys())



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::field_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Field)


def test_webapplication::content::field_constructor_exists():
    assert callable(webApplication::content::Field.__init__)


def test_webapplication::content::field_constructor_args():
    sig = inspect.signature(webApplication::content::Field.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_webapplication::content::field_has_type():
    assert hasattr(webApplication::content::Field, "type")
    descriptor = None
    for klass in webApplication::content::Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_webapplication::content::form_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Form)


def test_webapplication::content::form_constructor_exists():
    assert callable(webApplication::content::Form.__init__)


def test_webapplication::content::form_constructor_args():
    sig = inspect.signature(webApplication::content::Form.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::link_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Link)


def test_webapplication::content::link_constructor_exists():
    assert callable(webApplication::content::Link.__init__)


def test_webapplication::content::link_constructor_args():
    sig = inspect.signature(webApplication::content::Link.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::content_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Content)


def test_webapplication::content::content_constructor_exists():
    assert callable(webApplication::content::Content.__init__)


def test_webapplication::content::content_constructor_args():
    sig = inspect.signature(webApplication::content::Content.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::data::entity_is_not_abstract():
    assert not inspect.isabstract(webApplication::data::Entity)


def test_webapplication::data::entity_constructor_exists():
    assert callable(webApplication::data::Entity.__init__)


def test_webapplication::data::entity_constructor_args():
    sig = inspect.signature(webApplication::data::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfColumns" in params, "Missing parameter 'numberOfColumns'"

def test_webapplication::data::entity_has_numberOfColumns():
    assert hasattr(webApplication::data::Entity, "numberOfColumns")
    descriptor = None
    for klass in webApplication::data::Entity.__mro__:
        if "numberOfColumns" in klass.__dict__:
            descriptor = klass.__dict__["numberOfColumns"]
            break
    assert isinstance(descriptor, property)



def test_webapplication::data::column_is_not_abstract():
    assert not inspect.isabstract(webApplication::data::Column)


def test_webapplication::data::column_constructor_exists():
    assert callable(webApplication::data::Column.__init__)


def test_webapplication::data::column_constructor_args():
    sig = inspect.signature(webApplication::data::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "PK" in params, "Missing parameter 'PK'"
    assert "lenght" in params, "Missing parameter 'lenght'"

def test_webapplication::data::column_has_type():
    assert hasattr(webApplication::data::Column, "type")
    descriptor = None
    for klass in webApplication::data::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_webapplication::data::column_has_PK():
    assert hasattr(webApplication::data::Column, "PK")
    descriptor = None
    for klass in webApplication::data::Column.__mro__:
        if "PK" in klass.__dict__:
            descriptor = klass.__dict__["PK"]
            break
    assert isinstance(descriptor, property)

def test_webapplication::data::column_has_lenght():
    assert hasattr(webApplication::data::Column, "lenght")
    descriptor = None
    for klass in webApplication::data::Column.__mro__:
        if "lenght" in klass.__dict__:
            descriptor = klass.__dict__["lenght"]
            break
    assert isinstance(descriptor, property)



def test_webapplication::data::relatedentity_is_not_abstract():
    assert not inspect.isabstract(webApplication::data::RelatedEntity)


def test_webapplication::data::relatedentity_constructor_exists():
    assert callable(webApplication::data::RelatedEntity.__init__)


def test_webapplication::data::relatedentity_constructor_args():
    sig = inspect.signature(webApplication::data::RelatedEntity.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::content::page_is_not_abstract():
    assert not inspect.isabstract(webApplication::content::Page)


def test_webapplication::content::page_constructor_exists():
    assert callable(webApplication::content::Page.__init__)


def test_webapplication::content::page_constructor_args():
    sig = inspect.signature(webApplication::content::Page.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::data::datasource_is_not_abstract():
    assert not inspect.isabstract(webApplication::data::DataSource)


def test_webapplication::data::datasource_constructor_exists():
    assert callable(webApplication::data::DataSource.__init__)


def test_webapplication::data::datasource_constructor_args():
    sig = inspect.signature(webApplication::data::DataSource.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::webapplicationmodel_is_not_abstract():
    assert not inspect.isabstract(webApplication::WebApplicationModel)


def test_webapplication::webapplicationmodel_constructor_exists():
    assert callable(webApplication::WebApplicationModel.__init__)


def test_webapplication::webapplicationmodel_constructor_args():
    sig = inspect.signature(webApplication::WebApplicationModel.__init__)
    params = list(sig.parameters.keys())



def test_webapplication::named_is_not_abstract():
    assert not inspect.isabstract(webApplication::Named)


def test_webapplication::named_constructor_exists():
    assert callable(webApplication::Named.__init__)


def test_webapplication::named_constructor_args():
    sig = inspect.signature(webApplication::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_webapplication::named_has_name():
    assert hasattr(webApplication::Named, "name")
    descriptor = None
    for klass in webApplication::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "String",
        "Boolean",
        "Float",
        "Text",
        "Integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"

def test_fieldtype_exists():
    # Check that the Enumeration exists
    assert FieldType is not None

def test_fieldtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FieldType]
    expected_literals = [
        "CheckBox",
        "RadioButton",
        "TextBox",
        "SubmitButton",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FieldType"


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
Field_strategy = st.builds(
    Field,
)
Form_strategy = st.builds(
    Form,
)
webApplication::content::CRUDForm_strategy = st.builds(
    webApplication::content::CRUDForm,
)
Link_strategy = st.builds(
    Link,
)
Content_strategy = st.builds(
    Content,
)
webApplication::content::Menu_strategy = st.builds(
    webApplication::content::Menu,
    itemName=
        safe_text,
    order=
        st.integers(),
    url=
        safe_text
)
webApplication::content::MultipleContent_strategy = st.builds(
    webApplication::content::MultipleContent,
    size=
        st.integers(),
    paginated=
        st.booleans()
)
webApplication::content::SingleContent_strategy = st.builds(
    webApplication::content::SingleContent,
)
RelatedEntity_strategy = st.builds(
    RelatedEntity,
)
Column_strategy = st.builds(
    Column,
)
Page_strategy = st.builds(
    Page,
)
DataSource_strategy = st.builds(
    DataSource,
)
Entity_strategy = st.builds(
    Entity,
)
Named_strategy = st.builds(
    Named,
)
webApplication::content::Field_strategy = st.builds(
    webApplication::content::Field,
    type=
        safe_text
)
webApplication::content::Form_strategy = st.builds(
    webApplication::content::Form,
)
webApplication::content::Link_strategy = st.builds(
    webApplication::content::Link,
)
webApplication::content::Content_strategy = st.builds(
    webApplication::content::Content,
)
webApplication::data::Entity_strategy = st.builds(
    webApplication::data::Entity,
    numberOfColumns=
        safe_text
)
webApplication::data::Column_strategy = st.builds(
    webApplication::data::Column,
    type=
        safe_text,
    PK=
        st.booleans(),
    lenght=
        st.integers()
)
webApplication::data::RelatedEntity_strategy = st.builds(
    webApplication::data::RelatedEntity,
)
webApplication::content::Page_strategy = st.builds(
    webApplication::content::Page,
)
webApplication::data::DataSource_strategy = st.builds(
    webApplication::data::DataSource,
)
webApplication::WebApplicationModel_strategy = st.builds(
    webApplication::WebApplicationModel,
)
webApplication::Named_strategy = st.builds(
    webApplication::Named,
    name=
        safe_text
)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=Form_strategy)
@settings(max_examples=50)
def test_form_instantiation(instance):
    assert isinstance(instance, Form)

@given(instance=webApplication::content::CRUDForm_strategy)
@settings(max_examples=50)
def test_webapplication::content::crudform_instantiation(instance):
    assert isinstance(instance, webApplication::content::CRUDForm)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=Content_strategy)
@settings(max_examples=50)
def test_content_instantiation(instance):
    assert isinstance(instance, Content)

@given(instance=webApplication::content::Menu_strategy)
@settings(max_examples=50)
def test_webapplication::content::menu_instantiation(instance):
    assert isinstance(instance, webApplication::content::Menu)

@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_itemName_type(instance):
    assert isinstance(instance.itemName, str)


@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_itemName_setter(instance):
    original = instance.itemName
    instance.itemName = original
    assert instance.itemName == original

@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=webApplication::content::Menu_strategy)
def test_webapplication::content::menu_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=webApplication::content::MultipleContent_strategy)
@settings(max_examples=50)
def test_webapplication::content::multiplecontent_instantiation(instance):
    assert isinstance(instance, webApplication::content::MultipleContent)

@given(instance=webApplication::content::MultipleContent_strategy)
def test_webapplication::content::multiplecontent_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=webApplication::content::MultipleContent_strategy)
def test_webapplication::content::multiplecontent_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=webApplication::content::MultipleContent_strategy)
def test_webapplication::content::multiplecontent_paginated_type(instance):
    assert isinstance(instance.paginated, bool)


@given(instance=webApplication::content::MultipleContent_strategy)
def test_webapplication::content::multiplecontent_paginated_setter(instance):
    original = instance.paginated
    instance.paginated = original
    assert instance.paginated == original

@given(instance=webApplication::content::SingleContent_strategy)
@settings(max_examples=50)
def test_webapplication::content::singlecontent_instantiation(instance):
    assert isinstance(instance, webApplication::content::SingleContent)

@given(instance=RelatedEntity_strategy)
@settings(max_examples=50)
def test_relatedentity_instantiation(instance):
    assert isinstance(instance, RelatedEntity)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DataSource_strategy)
@settings(max_examples=50)
def test_datasource_instantiation(instance):
    assert isinstance(instance, DataSource)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=webApplication::content::Field_strategy)
@settings(max_examples=50)
def test_webapplication::content::field_instantiation(instance):
    assert isinstance(instance, webApplication::content::Field)

@given(instance=webApplication::content::Field_strategy)
def test_webapplication::content::field_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=webApplication::content::Field_strategy)
def test_webapplication::content::field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=webApplication::content::Form_strategy)
@settings(max_examples=50)
def test_webapplication::content::form_instantiation(instance):
    assert isinstance(instance, webApplication::content::Form)

@given(instance=webApplication::content::Link_strategy)
@settings(max_examples=50)
def test_webapplication::content::link_instantiation(instance):
    assert isinstance(instance, webApplication::content::Link)

@given(instance=webApplication::content::Content_strategy)
@settings(max_examples=50)
def test_webapplication::content::content_instantiation(instance):
    assert isinstance(instance, webApplication::content::Content)

@given(instance=webApplication::data::Entity_strategy)
@settings(max_examples=50)
def test_webapplication::data::entity_instantiation(instance):
    assert isinstance(instance, webApplication::data::Entity)

@given(instance=webApplication::data::Entity_strategy)
def test_webapplication::data::entity_numberOfColumns_type(instance):
    assert isinstance(instance.numberOfColumns, str)


@given(instance=webApplication::data::Entity_strategy)
def test_webapplication::data::entity_numberOfColumns_setter(instance):
    original = instance.numberOfColumns
    instance.numberOfColumns = original
    assert instance.numberOfColumns == original

@given(instance=webApplication::data::Column_strategy)
@settings(max_examples=50)
def test_webapplication::data::column_instantiation(instance):
    assert isinstance(instance, webApplication::data::Column)

@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_PK_type(instance):
    assert isinstance(instance.PK, bool)


@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_PK_setter(instance):
    original = instance.PK
    instance.PK = original
    assert instance.PK == original

@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_lenght_type(instance):
    assert isinstance(instance.lenght, int)


@given(instance=webApplication::data::Column_strategy)
def test_webapplication::data::column_lenght_setter(instance):
    original = instance.lenght
    instance.lenght = original
    assert instance.lenght == original

@given(instance=webApplication::data::RelatedEntity_strategy)
@settings(max_examples=50)
def test_webapplication::data::relatedentity_instantiation(instance):
    assert isinstance(instance, webApplication::data::RelatedEntity)

@given(instance=webApplication::content::Page_strategy)
@settings(max_examples=50)
def test_webapplication::content::page_instantiation(instance):
    assert isinstance(instance, webApplication::content::Page)

@given(instance=webApplication::data::DataSource_strategy)
@settings(max_examples=50)
def test_webapplication::data::datasource_instantiation(instance):
    assert isinstance(instance, webApplication::data::DataSource)

@given(instance=webApplication::WebApplicationModel_strategy)
@settings(max_examples=50)
def test_webapplication::webapplicationmodel_instantiation(instance):
    assert isinstance(instance, webApplication::WebApplicationModel)

@given(instance=webApplication::Named_strategy)
@settings(max_examples=50)
def test_webapplication::named_instantiation(instance):
    assert isinstance(instance, webApplication::Named)

@given(instance=webApplication::Named_strategy)
def test_webapplication::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=webApplication::Named_strategy)
def test_webapplication::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
