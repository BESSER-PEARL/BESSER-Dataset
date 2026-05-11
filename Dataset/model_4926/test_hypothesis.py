import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NotStructuredElement,
    becontent::RelationManager,
    becontent::Hidden,
    becontent::Position,
    becontent::Textarea,
    becontent::File,
    becontent::Link,
    becontent::Year,
    becontent::SelectFromReference,
    becontent::RadioFromReference,
    becontent::LongDate,
    becontent::Password,
    becontent::FileToFolder,
    becontent::HierarchicalPosition,
    becontent::Image,
    becontent::Date,
    becontent::Color,
    becontent::Editor,
    becontent::Select,
    becontent::Section,
    Form,
    becontent::ExtendedForm,
    becontent::Checkbox,
    becontent::RadioButton,
    becontent::Text,
    becontent::Validation,
    becontent::CustomPager,
    ApplyCommand,
    becontent::ApplyItem,
    becontent::ApplyIndexed,
    becontent::Apply,
    FormElement,
    becontent::NotStructuredElement,
    becontent::Form,
    becontent::FormElement,
    becontent::ConditionalTemplate,
    becontent::ContentCommand,
    becontent::JoinEntity,
    ContentCommand,
    becontent::UnsetParameter,
    becontent::Trigger,
    becontent::Copy,
    becontent::ApplyCommand,
    becontent::Propagate,
    becontent::Parameter,
    ViewItem,
    becontent::Template,
    becontent::Skin,
    becontent::ViewItem,
    becontent::Content,
    becontent::Skinlet,
    TypedSystemAttribute,
    becontent::SystemAttributePosition,
    becontent::SystemAttributeLongDate,
    becontent::SystemAttributeText,
    becontent::SystemAttributePassword,
    becontent::SystemAttributeDate,
    becontent::SystemAttributeColor,
    SystemEntityField,
    becontent::TypedSystemAttribute,
    becontent::SystemReference,
    becontent::SystemAttributeFileToFolder,
    becontent::SystemAttributeFile,
    becontent::SystemAttributeVarchar,
    becontent::SystemAttributeInteger,
    becontent::SystemAttributeImage,
    TypedAttribute,
    becontent::AttributeFileToFolder,
    becontent::AttributeColor,
    EntityField,
    becontent::TypedAttribute,
    becontent::Reference,
    becontent::AttributeFile,
    becontent::AttributeVarchar,
    becontent::AttributeInteger,
    becontent::AttributeImage,
    becontent::AttributePosition,
    becontent::AttributePassword,
    becontent::AttributeText,
    becontent::AttributeLongDate,
    becontent::AttributeDate,
    becontent::EntityField,
    DefinitionItem,
    becontent::Entity,
    BeContentElement,
    becontent::Channel,
    becontent::FileToFolderExtension,
    becontent::EntityManagerPage,
    becontent::DefinitionItem,
    becontent::BeContentElement,
    becontent::BeContentModel,
    Relation,
    becontent::SystemRelation,
    becontent::CustomRelation,
    becontent::Relation,
    becontent::SystemEntityField,
    Entity,
    becontent::SystemEntity,
    becontent::CustomEntity,
    becontent::Handler,
    FormMethodType,
    ContentStyle,
    ConditionalTemplateExpType,
    OrientationType,
    ConditionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_notstructuredelement_is_not_abstract():
    assert not inspect.isabstract(NotStructuredElement)


def test_notstructuredelement_constructor_exists():
    assert callable(NotStructuredElement.__init__)


def test_notstructuredelement_constructor_args():
    sig = inspect.signature(NotStructuredElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent::relationmanager_is_not_abstract():
    assert not inspect.isabstract(becontent::RelationManager)


def test_becontent::relationmanager_constructor_exists():
    assert callable(becontent::RelationManager.__init__)


def test_becontent::relationmanager_constructor_args():
    sig = inspect.signature(becontent::RelationManager.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"

def test_becontent::relationmanager_has_orientation():
    assert hasattr(becontent::RelationManager, "orientation")
    descriptor = None
    for klass in becontent::RelationManager.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_becontent::relationmanager_has_label():
    assert hasattr(becontent::RelationManager, "label")
    descriptor = None
    for klass in becontent::RelationManager.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::relationmanager_has_name():
    assert hasattr(becontent::RelationManager, "name")
    descriptor = None
    for klass in becontent::RelationManager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::relationmanager_has_restrictCondition():
    assert hasattr(becontent::RelationManager, "restrictCondition")
    descriptor = None
    for klass in becontent::RelationManager.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)



def test_becontent::hidden_is_not_abstract():
    assert not inspect.isabstract(becontent::Hidden)


def test_becontent::hidden_constructor_exists():
    assert callable(becontent::Hidden.__init__)


def test_becontent::hidden_constructor_args():
    sig = inspect.signature(becontent::Hidden.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "values" in params, "Missing parameter 'values'"

def test_becontent::hidden_has_name():
    assert hasattr(becontent::Hidden, "name")
    descriptor = None
    for klass in becontent::Hidden.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::hidden_has_values():
    assert hasattr(becontent::Hidden, "values")
    descriptor = None
    for klass in becontent::Hidden.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_becontent::position_is_not_abstract():
    assert not inspect.isabstract(becontent::Position)


def test_becontent::position_constructor_exists():
    assert callable(becontent::Position.__init__)


def test_becontent::position_constructor_args():
    sig = inspect.signature(becontent::Position.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "size" in params, "Missing parameter 'size'"
    assert "controlledField" in params, "Missing parameter 'controlledField'"

def test_becontent::position_has_name():
    assert hasattr(becontent::Position, "name")
    descriptor = None
    for klass in becontent::Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::position_has_label():
    assert hasattr(becontent::Position, "label")
    descriptor = None
    for klass in becontent::Position.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::position_has_isMandatory():
    assert hasattr(becontent::Position, "isMandatory")
    descriptor = None
    for klass in becontent::Position.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::position_has_size():
    assert hasattr(becontent::Position, "size")
    descriptor = None
    for klass in becontent::Position.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent::position_has_controlledField():
    assert hasattr(becontent::Position, "controlledField")
    descriptor = None
    for klass in becontent::Position.__mro__:
        if "controlledField" in klass.__dict__:
            descriptor = klass.__dict__["controlledField"]
            break
    assert isinstance(descriptor, property)



def test_becontent::textarea_is_not_abstract():
    assert not inspect.isabstract(becontent::Textarea)


def test_becontent::textarea_constructor_exists():
    assert callable(becontent::Textarea.__init__)


def test_becontent::textarea_constructor_args():
    sig = inspect.signature(becontent::Textarea.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent::textarea_has_rows():
    assert hasattr(becontent::Textarea, "rows")
    descriptor = None
    for klass in becontent::Textarea.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_becontent::textarea_has_name():
    assert hasattr(becontent::Textarea, "name")
    descriptor = None
    for klass in becontent::Textarea.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::textarea_has_isMandatory():
    assert hasattr(becontent::Textarea, "isMandatory")
    descriptor = None
    for klass in becontent::Textarea.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::textarea_has_columns():
    assert hasattr(becontent::Textarea, "columns")
    descriptor = None
    for klass in becontent::Textarea.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_becontent::textarea_has_label():
    assert hasattr(becontent::Textarea, "label")
    descriptor = None
    for klass in becontent::Textarea.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent::file_is_not_abstract():
    assert not inspect.isabstract(becontent::File)


def test_becontent::file_constructor_exists():
    assert callable(becontent::File.__init__)


def test_becontent::file_constructor_args():
    sig = inspect.signature(becontent::File.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "extensionMessage" in params, "Missing parameter 'extensionMessage'"
    assert "extension" in params, "Missing parameter 'extension'"

def test_becontent::file_has_name():
    assert hasattr(becontent::File, "name")
    descriptor = None
    for klass in becontent::File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::file_has_isMandatory():
    assert hasattr(becontent::File, "isMandatory")
    descriptor = None
    for klass in becontent::File.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::file_has_label():
    assert hasattr(becontent::File, "label")
    descriptor = None
    for klass in becontent::File.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::file_has_extensionMessage():
    assert hasattr(becontent::File, "extensionMessage")
    descriptor = None
    for klass in becontent::File.__mro__:
        if "extensionMessage" in klass.__dict__:
            descriptor = klass.__dict__["extensionMessage"]
            break
    assert isinstance(descriptor, property)

def test_becontent::file_has_extension():
    assert hasattr(becontent::File, "extension")
    descriptor = None
    for klass in becontent::File.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_becontent::link_is_not_abstract():
    assert not inspect.isabstract(becontent::Link)


def test_becontent::link_constructor_exists():
    assert callable(becontent::Link.__init__)


def test_becontent::link_constructor_args():
    sig = inspect.signature(becontent::Link.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "label" in params, "Missing parameter 'label'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent::link_has_size():
    assert hasattr(becontent::Link, "size")
    descriptor = None
    for klass in becontent::Link.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent::link_has_label():
    assert hasattr(becontent::Link, "label")
    descriptor = None
    for klass in becontent::Link.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::link_has_maxLength():
    assert hasattr(becontent::Link, "maxLength")
    descriptor = None
    for klass in becontent::Link.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent::link_has_name():
    assert hasattr(becontent::Link, "name")
    descriptor = None
    for klass in becontent::Link.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::link_has_isMandatory():
    assert hasattr(becontent::Link, "isMandatory")
    descriptor = None
    for klass in becontent::Link.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent::year_is_not_abstract():
    assert not inspect.isabstract(becontent::Year)


def test_becontent::year_constructor_exists():
    assert callable(becontent::Year.__init__)


def test_becontent::year_constructor_args():
    sig = inspect.signature(becontent::Year.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent::year_has_name():
    assert hasattr(becontent::Year, "name")
    descriptor = None
    for klass in becontent::Year.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::year_has_label():
    assert hasattr(becontent::Year, "label")
    descriptor = None
    for klass in becontent::Year.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::year_has_start():
    assert hasattr(becontent::Year, "start")
    descriptor = None
    for klass in becontent::Year.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_becontent::year_has_end():
    assert hasattr(becontent::Year, "end")
    descriptor = None
    for klass in becontent::Year.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_becontent::year_has_isMandatory():
    assert hasattr(becontent::Year, "isMandatory")
    descriptor = None
    for klass in becontent::Year.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent::selectfromreference_is_not_abstract():
    assert not inspect.isabstract(becontent::SelectFromReference)


def test_becontent::selectfromreference_constructor_exists():
    assert callable(becontent::SelectFromReference.__init__)


def test_becontent::selectfromreference_constructor_args():
    sig = inspect.signature(becontent::SelectFromReference.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent::selectfromreference_has_isMandatory():
    assert hasattr(becontent::SelectFromReference, "isMandatory")
    descriptor = None
    for klass in becontent::SelectFromReference.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::selectfromreference_has_restrictCondition():
    assert hasattr(becontent::SelectFromReference, "restrictCondition")
    descriptor = None
    for klass in becontent::SelectFromReference.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent::selectfromreference_has_name():
    assert hasattr(becontent::SelectFromReference, "name")
    descriptor = None
    for klass in becontent::SelectFromReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::selectfromreference_has_label():
    assert hasattr(becontent::SelectFromReference, "label")
    descriptor = None
    for klass in becontent::SelectFromReference.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent::radiofromreference_is_not_abstract():
    assert not inspect.isabstract(becontent::RadioFromReference)


def test_becontent::radiofromreference_constructor_exists():
    assert callable(becontent::RadioFromReference.__init__)


def test_becontent::radiofromreference_constructor_args():
    sig = inspect.signature(becontent::RadioFromReference.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"

def test_becontent::radiofromreference_has_isMandatory():
    assert hasattr(becontent::RadioFromReference, "isMandatory")
    descriptor = None
    for klass in becontent::RadioFromReference.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::radiofromreference_has_label():
    assert hasattr(becontent::RadioFromReference, "label")
    descriptor = None
    for klass in becontent::RadioFromReference.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::radiofromreference_has_name():
    assert hasattr(becontent::RadioFromReference, "name")
    descriptor = None
    for klass in becontent::RadioFromReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::radiofromreference_has_restrictCondition():
    assert hasattr(becontent::RadioFromReference, "restrictCondition")
    descriptor = None
    for klass in becontent::RadioFromReference.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)



def test_becontent::longdate_is_not_abstract():
    assert not inspect.isabstract(becontent::LongDate)


def test_becontent::longdate_constructor_exists():
    assert callable(becontent::LongDate.__init__)


def test_becontent::longdate_constructor_args():
    sig = inspect.signature(becontent::LongDate.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::longdate_has_label():
    assert hasattr(becontent::LongDate, "label")
    descriptor = None
    for klass in becontent::LongDate.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::longdate_has_isMandatory():
    assert hasattr(becontent::LongDate, "isMandatory")
    descriptor = None
    for klass in becontent::LongDate.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::longdate_has_name():
    assert hasattr(becontent::LongDate, "name")
    descriptor = None
    for klass in becontent::LongDate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::password_is_not_abstract():
    assert not inspect.isabstract(becontent::Password)


def test_becontent::password_constructor_exists():
    assert callable(becontent::Password.__init__)


def test_becontent::password_constructor_args():
    sig = inspect.signature(becontent::Password.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "size" in params, "Missing parameter 'size'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent::password_has_maxLength():
    assert hasattr(becontent::Password, "maxLength")
    descriptor = None
    for klass in becontent::Password.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent::password_has_name():
    assert hasattr(becontent::Password, "name")
    descriptor = None
    for klass in becontent::Password.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::password_has_label():
    assert hasattr(becontent::Password, "label")
    descriptor = None
    for klass in becontent::Password.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::password_has_size():
    assert hasattr(becontent::Password, "size")
    descriptor = None
    for klass in becontent::Password.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent::password_has_isMandatory():
    assert hasattr(becontent::Password, "isMandatory")
    descriptor = None
    for klass in becontent::Password.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent::filetofolder_is_not_abstract():
    assert not inspect.isabstract(becontent::FileToFolder)


def test_becontent::filetofolder_constructor_exists():
    assert callable(becontent::FileToFolder.__init__)


def test_becontent::filetofolder_constructor_args():
    sig = inspect.signature(becontent::FileToFolder.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "extensionMessage" in params, "Missing parameter 'extensionMessage'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::filetofolder_has_extension():
    assert hasattr(becontent::FileToFolder, "extension")
    descriptor = None
    for klass in becontent::FileToFolder.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolder_has_extensionMessage():
    assert hasattr(becontent::FileToFolder, "extensionMessage")
    descriptor = None
    for klass in becontent::FileToFolder.__mro__:
        if "extensionMessage" in klass.__dict__:
            descriptor = klass.__dict__["extensionMessage"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolder_has_isMandatory():
    assert hasattr(becontent::FileToFolder, "isMandatory")
    descriptor = None
    for klass in becontent::FileToFolder.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolder_has_label():
    assert hasattr(becontent::FileToFolder, "label")
    descriptor = None
    for klass in becontent::FileToFolder.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolder_has_name():
    assert hasattr(becontent::FileToFolder, "name")
    descriptor = None
    for klass in becontent::FileToFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::hierarchicalposition_is_not_abstract():
    assert not inspect.isabstract(becontent::HierarchicalPosition)


def test_becontent::hierarchicalposition_constructor_exists():
    assert callable(becontent::HierarchicalPosition.__init__)


def test_becontent::hierarchicalposition_constructor_args():
    sig = inspect.signature(becontent::HierarchicalPosition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "size" in params, "Missing parameter 'size'"
    assert "controlledField" in params, "Missing parameter 'controlledField'"
    assert "referenceField" in params, "Missing parameter 'referenceField'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::hierarchicalposition_has_label():
    assert hasattr(becontent::HierarchicalPosition, "label")
    descriptor = None
    for klass in becontent::HierarchicalPosition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::hierarchicalposition_has_size():
    assert hasattr(becontent::HierarchicalPosition, "size")
    descriptor = None
    for klass in becontent::HierarchicalPosition.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent::hierarchicalposition_has_controlledField():
    assert hasattr(becontent::HierarchicalPosition, "controlledField")
    descriptor = None
    for klass in becontent::HierarchicalPosition.__mro__:
        if "controlledField" in klass.__dict__:
            descriptor = klass.__dict__["controlledField"]
            break
    assert isinstance(descriptor, property)

def test_becontent::hierarchicalposition_has_referenceField():
    assert hasattr(becontent::HierarchicalPosition, "referenceField")
    descriptor = None
    for klass in becontent::HierarchicalPosition.__mro__:
        if "referenceField" in klass.__dict__:
            descriptor = klass.__dict__["referenceField"]
            break
    assert isinstance(descriptor, property)

def test_becontent::hierarchicalposition_has_name():
    assert hasattr(becontent::HierarchicalPosition, "name")
    descriptor = None
    for klass in becontent::HierarchicalPosition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::image_is_not_abstract():
    assert not inspect.isabstract(becontent::Image)


def test_becontent::image_constructor_exists():
    assert callable(becontent::Image.__init__)


def test_becontent::image_constructor_args():
    sig = inspect.signature(becontent::Image.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent::image_has_isMandatory():
    assert hasattr(becontent::Image, "isMandatory")
    descriptor = None
    for klass in becontent::Image.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::image_has_name():
    assert hasattr(becontent::Image, "name")
    descriptor = None
    for klass in becontent::Image.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::image_has_label():
    assert hasattr(becontent::Image, "label")
    descriptor = None
    for klass in becontent::Image.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent::date_is_not_abstract():
    assert not inspect.isabstract(becontent::Date)


def test_becontent::date_constructor_exists():
    assert callable(becontent::Date.__init__)


def test_becontent::date_constructor_args():
    sig = inspect.signature(becontent::Date.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent::date_has_name():
    assert hasattr(becontent::Date, "name")
    descriptor = None
    for klass in becontent::Date.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::date_has_label():
    assert hasattr(becontent::Date, "label")
    descriptor = None
    for klass in becontent::Date.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::date_has_isMandatory():
    assert hasattr(becontent::Date, "isMandatory")
    descriptor = None
    for klass in becontent::Date.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent::color_is_not_abstract():
    assert not inspect.isabstract(becontent::Color)


def test_becontent::color_constructor_exists():
    assert callable(becontent::Color.__init__)


def test_becontent::color_constructor_args():
    sig = inspect.signature(becontent::Color.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultColor" in params, "Missing parameter 'defaultColor'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent::color_has_name():
    assert hasattr(becontent::Color, "name")
    descriptor = None
    for klass in becontent::Color.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::color_has_defaultColor():
    assert hasattr(becontent::Color, "defaultColor")
    descriptor = None
    for klass in becontent::Color.__mro__:
        if "defaultColor" in klass.__dict__:
            descriptor = klass.__dict__["defaultColor"]
            break
    assert isinstance(descriptor, property)

def test_becontent::color_has_label():
    assert hasattr(becontent::Color, "label")
    descriptor = None
    for klass in becontent::Color.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent::editor_is_not_abstract():
    assert not inspect.isabstract(becontent::Editor)


def test_becontent::editor_constructor_exists():
    assert callable(becontent::Editor.__init__)


def test_becontent::editor_constructor_args():
    sig = inspect.signature(becontent::Editor.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::editor_has_rows():
    assert hasattr(becontent::Editor, "rows")
    descriptor = None
    for klass in becontent::Editor.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_becontent::editor_has_columns():
    assert hasattr(becontent::Editor, "columns")
    descriptor = None
    for klass in becontent::Editor.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_becontent::editor_has_label():
    assert hasattr(becontent::Editor, "label")
    descriptor = None
    for klass in becontent::Editor.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::editor_has_isMandatory():
    assert hasattr(becontent::Editor, "isMandatory")
    descriptor = None
    for klass in becontent::Editor.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::editor_has_name():
    assert hasattr(becontent::Editor, "name")
    descriptor = None
    for klass in becontent::Editor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::select_is_not_abstract():
    assert not inspect.isabstract(becontent::Select)


def test_becontent::select_constructor_exists():
    assert callable(becontent::Select.__init__)


def test_becontent::select_constructor_args():
    sig = inspect.signature(becontent::Select.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::select_has_values():
    assert hasattr(becontent::Select, "values")
    descriptor = None
    for klass in becontent::Select.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_becontent::select_has_isMandatory():
    assert hasattr(becontent::Select, "isMandatory")
    descriptor = None
    for klass in becontent::Select.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::select_has_label():
    assert hasattr(becontent::Select, "label")
    descriptor = None
    for klass in becontent::Select.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::select_has_name():
    assert hasattr(becontent::Select, "name")
    descriptor = None
    for klass in becontent::Select.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::section_is_not_abstract():
    assert not inspect.isabstract(becontent::Section)


def test_becontent::section_constructor_exists():
    assert callable(becontent::Section.__init__)


def test_becontent::section_constructor_args():
    sig = inspect.signature(becontent::Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "text" in params, "Missing parameter 'text'"

def test_becontent::section_has_name():
    assert hasattr(becontent::Section, "name")
    descriptor = None
    for klass in becontent::Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::section_has_text():
    assert hasattr(becontent::Section, "text")
    descriptor = None
    for klass in becontent::Section.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_form_is_not_abstract():
    assert not inspect.isabstract(Form)


def test_form_constructor_exists():
    assert callable(Form.__init__)


def test_form_constructor_args():
    sig = inspect.signature(Form.__init__)
    params = list(sig.parameters.keys())



def test_becontent::extendedform_is_not_abstract():
    assert not inspect.isabstract(becontent::ExtendedForm)


def test_becontent::extendedform_constructor_exists():
    assert callable(becontent::ExtendedForm.__init__)


def test_becontent::extendedform_constructor_args():
    sig = inspect.signature(becontent::ExtendedForm.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_becontent::extendedform_has_className():
    assert hasattr(becontent::ExtendedForm, "className")
    descriptor = None
    for klass in becontent::ExtendedForm.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_becontent::checkbox_is_not_abstract():
    assert not inspect.isabstract(becontent::Checkbox)


def test_becontent::checkbox_constructor_exists():
    assert callable(becontent::Checkbox.__init__)


def test_becontent::checkbox_constructor_args():
    sig = inspect.signature(becontent::Checkbox.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isChecked" in params, "Missing parameter 'isChecked'"
    assert "label" in params, "Missing parameter 'label'"
    assert "value" in params, "Missing parameter 'value'"

def test_becontent::checkbox_has_name():
    assert hasattr(becontent::Checkbox, "name")
    descriptor = None
    for klass in becontent::Checkbox.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::checkbox_has_isChecked():
    assert hasattr(becontent::Checkbox, "isChecked")
    descriptor = None
    for klass in becontent::Checkbox.__mro__:
        if "isChecked" in klass.__dict__:
            descriptor = klass.__dict__["isChecked"]
            break
    assert isinstance(descriptor, property)

def test_becontent::checkbox_has_label():
    assert hasattr(becontent::Checkbox, "label")
    descriptor = None
    for klass in becontent::Checkbox.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::checkbox_has_value():
    assert hasattr(becontent::Checkbox, "value")
    descriptor = None
    for klass in becontent::Checkbox.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_becontent::radiobutton_is_not_abstract():
    assert not inspect.isabstract(becontent::RadioButton)


def test_becontent::radiobutton_constructor_exists():
    assert callable(becontent::RadioButton.__init__)


def test_becontent::radiobutton_constructor_args():
    sig = inspect.signature(becontent::RadioButton.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::radiobutton_has_values():
    assert hasattr(becontent::RadioButton, "values")
    descriptor = None
    for klass in becontent::RadioButton.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_becontent::radiobutton_has_label():
    assert hasattr(becontent::RadioButton, "label")
    descriptor = None
    for klass in becontent::RadioButton.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::radiobutton_has_name():
    assert hasattr(becontent::RadioButton, "name")
    descriptor = None
    for klass in becontent::RadioButton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::text_is_not_abstract():
    assert not inspect.isabstract(becontent::Text)


def test_becontent::text_constructor_exists():
    assert callable(becontent::Text.__init__)


def test_becontent::text_constructor_args():
    sig = inspect.signature(becontent::Text.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_becontent::text_has_size():
    assert hasattr(becontent::Text, "size")
    descriptor = None
    for klass in becontent::Text.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent::text_has_name():
    assert hasattr(becontent::Text, "name")
    descriptor = None
    for klass in becontent::Text.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::text_has_label():
    assert hasattr(becontent::Text, "label")
    descriptor = None
    for klass in becontent::Text.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent::text_has_isMandatory():
    assert hasattr(becontent::Text, "isMandatory")
    descriptor = None
    for klass in becontent::Text.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::text_has_maxLength():
    assert hasattr(becontent::Text, "maxLength")
    descriptor = None
    for klass in becontent::Text.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_becontent::validation_is_not_abstract():
    assert not inspect.isabstract(becontent::Validation)


def test_becontent::validation_constructor_exists():
    assert callable(becontent::Validation.__init__)


def test_becontent::validation_constructor_args():
    sig = inspect.signature(becontent::Validation.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_becontent::validation_has_message():
    assert hasattr(becontent::Validation, "message")
    descriptor = None
    for klass in becontent::Validation.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_becontent::validation_has__id_model():
    assert hasattr(becontent::Validation, "_id_model")
    descriptor = None
    for klass in becontent::Validation.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::validation_has_condition():
    assert hasattr(becontent::Validation, "condition")
    descriptor = None
    for klass in becontent::Validation.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_becontent::custompager_is_not_abstract():
    assert not inspect.isabstract(becontent::CustomPager)


def test_becontent::custompager_constructor_exists():
    assert callable(becontent::CustomPager.__init__)


def test_becontent::custompager_constructor_args():
    sig = inspect.signature(becontent::CustomPager.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "template" in params, "Missing parameter 'template'"
    assert "className" in params, "Missing parameter 'className'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "query" in params, "Missing parameter 'query'"
    assert "length" in params, "Missing parameter 'length'"

def test_becontent::custompager_has_order():
    assert hasattr(becontent::CustomPager, "order")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has__id_model():
    assert hasattr(becontent::CustomPager, "_id_model")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has_template():
    assert hasattr(becontent::CustomPager, "template")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has_className():
    assert hasattr(becontent::CustomPager, "className")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has_filter():
    assert hasattr(becontent::CustomPager, "filter")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has_query():
    assert hasattr(becontent::CustomPager, "query")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_becontent::custompager_has_length():
    assert hasattr(becontent::CustomPager, "length")
    descriptor = None
    for klass in becontent::CustomPager.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_applycommand_is_not_abstract():
    assert not inspect.isabstract(ApplyCommand)


def test_applycommand_constructor_exists():
    assert callable(ApplyCommand.__init__)


def test_applycommand_constructor_args():
    sig = inspect.signature(ApplyCommand.__init__)
    params = list(sig.parameters.keys())



def test_becontent::applyitem_is_not_abstract():
    assert not inspect.isabstract(becontent::ApplyItem)


def test_becontent::applyitem_constructor_exists():
    assert callable(becontent::ApplyItem.__init__)


def test_becontent::applyitem_constructor_args():
    sig = inspect.signature(becontent::ApplyItem.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "key" in params, "Missing parameter 'key'"

def test_becontent::applyitem_has_prefix():
    assert hasattr(becontent::ApplyItem, "prefix")
    descriptor = None
    for klass in becontent::ApplyItem.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_becontent::applyitem_has_key():
    assert hasattr(becontent::ApplyItem, "key")
    descriptor = None
    for klass in becontent::ApplyItem.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_becontent::applyindexed_is_not_abstract():
    assert not inspect.isabstract(becontent::ApplyIndexed)


def test_becontent::applyindexed_constructor_exists():
    assert callable(becontent::ApplyIndexed.__init__)


def test_becontent::applyindexed_constructor_args():
    sig = inspect.signature(becontent::ApplyIndexed.__init__)
    params = list(sig.parameters.keys())



def test_becontent::apply_is_not_abstract():
    assert not inspect.isabstract(becontent::Apply)


def test_becontent::apply_constructor_exists():
    assert callable(becontent::Apply.__init__)


def test_becontent::apply_constructor_args():
    sig = inspect.signature(becontent::Apply.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_becontent::apply_has_prefix():
    assert hasattr(becontent::Apply, "prefix")
    descriptor = None
    for klass in becontent::Apply.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_formelement_is_not_abstract():
    assert not inspect.isabstract(FormElement)


def test_formelement_constructor_exists():
    assert callable(FormElement.__init__)


def test_formelement_constructor_args():
    sig = inspect.signature(FormElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent::notstructuredelement_is_not_abstract():
    assert not inspect.isabstract(becontent::NotStructuredElement)


def test_becontent::notstructuredelement_constructor_exists():
    assert callable(becontent::NotStructuredElement.__init__)


def test_becontent::notstructuredelement_constructor_args():
    sig = inspect.signature(becontent::NotStructuredElement.__init__)
    params = list(sig.parameters.keys())
    assert "helper" in params, "Missing parameter 'helper'"

def test_becontent::notstructuredelement_has_helper():
    assert hasattr(becontent::NotStructuredElement, "helper")
    descriptor = None
    for klass in becontent::NotStructuredElement.__mro__:
        if "helper" in klass.__dict__:
            descriptor = klass.__dict__["helper"]
            break
    assert isinstance(descriptor, property)



def test_becontent::form_is_not_abstract():
    assert not inspect.isabstract(becontent::Form)


def test_becontent::form_constructor_exists():
    assert callable(becontent::Form.__init__)


def test_becontent::form_constructor_args():
    sig = inspect.signature(becontent::Form.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"
    assert "description" in params, "Missing parameter 'description'"

def test_becontent::form_has_name():
    assert hasattr(becontent::Form, "name")
    descriptor = None
    for klass in becontent::Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::form_has_method():
    assert hasattr(becontent::Form, "method")
    descriptor = None
    for klass in becontent::Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_becontent::form_has_description():
    assert hasattr(becontent::Form, "description")
    descriptor = None
    for klass in becontent::Form.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_becontent::formelement_is_not_abstract():
    assert not inspect.isabstract(becontent::FormElement)


def test_becontent::formelement_constructor_exists():
    assert callable(becontent::FormElement.__init__)


def test_becontent::formelement_constructor_args():
    sig = inspect.signature(becontent::FormElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent::conditionaltemplate_is_not_abstract():
    assert not inspect.isabstract(becontent::ConditionalTemplate)


def test_becontent::conditionaltemplate_constructor_exists():
    assert callable(becontent::ConditionalTemplate.__init__)


def test_becontent::conditionaltemplate_constructor_args():
    sig = inspect.signature(becontent::ConditionalTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExp" in params, "Missing parameter 'conditionExp'"
    assert "falseTemplate" in params, "Missing parameter 'falseTemplate'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "trueTemplate" in params, "Missing parameter 'trueTemplate'"

def test_becontent::conditionaltemplate_has_conditionExp():
    assert hasattr(becontent::ConditionalTemplate, "conditionExp")
    descriptor = None
    for klass in becontent::ConditionalTemplate.__mro__:
        if "conditionExp" in klass.__dict__:
            descriptor = klass.__dict__["conditionExp"]
            break
    assert isinstance(descriptor, property)

def test_becontent::conditionaltemplate_has_falseTemplate():
    assert hasattr(becontent::ConditionalTemplate, "falseTemplate")
    descriptor = None
    for klass in becontent::ConditionalTemplate.__mro__:
        if "falseTemplate" in klass.__dict__:
            descriptor = klass.__dict__["falseTemplate"]
            break
    assert isinstance(descriptor, property)

def test_becontent::conditionaltemplate_has_fieldName():
    assert hasattr(becontent::ConditionalTemplate, "fieldName")
    descriptor = None
    for klass in becontent::ConditionalTemplate.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_becontent::conditionaltemplate_has__id_model():
    assert hasattr(becontent::ConditionalTemplate, "_id_model")
    descriptor = None
    for klass in becontent::ConditionalTemplate.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::conditionaltemplate_has_trueTemplate():
    assert hasattr(becontent::ConditionalTemplate, "trueTemplate")
    descriptor = None
    for klass in becontent::ConditionalTemplate.__mro__:
        if "trueTemplate" in klass.__dict__:
            descriptor = klass.__dict__["trueTemplate"]
            break
    assert isinstance(descriptor, property)



def test_becontent::contentcommand_is_not_abstract():
    assert not inspect.isabstract(becontent::ContentCommand)


def test_becontent::contentcommand_constructor_exists():
    assert callable(becontent::ContentCommand.__init__)


def test_becontent::contentcommand_constructor_args():
    sig = inspect.signature(becontent::ContentCommand.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent::contentcommand_has__id_model():
    assert hasattr(becontent::ContentCommand, "_id_model")
    descriptor = None
    for klass in becontent::ContentCommand.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_becontent::joinentity_is_not_abstract():
    assert not inspect.isabstract(becontent::JoinEntity)


def test_becontent::joinentity_constructor_exists():
    assert callable(becontent::JoinEntity.__init__)


def test_becontent::joinentity_constructor_args():
    sig = inspect.signature(becontent::JoinEntity.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent::joinentity_has__id_model():
    assert hasattr(becontent::JoinEntity, "_id_model")
    descriptor = None
    for klass in becontent::JoinEntity.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_contentcommand_is_not_abstract():
    assert not inspect.isabstract(ContentCommand)


def test_contentcommand_constructor_exists():
    assert callable(ContentCommand.__init__)


def test_contentcommand_constructor_args():
    sig = inspect.signature(ContentCommand.__init__)
    params = list(sig.parameters.keys())



def test_becontent::unsetparameter_is_not_abstract():
    assert not inspect.isabstract(becontent::UnsetParameter)


def test_becontent::unsetparameter_constructor_exists():
    assert callable(becontent::UnsetParameter.__init__)


def test_becontent::unsetparameter_constructor_args():
    sig = inspect.signature(becontent::UnsetParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::unsetparameter_has_name():
    assert hasattr(becontent::UnsetParameter, "name")
    descriptor = None
    for klass in becontent::UnsetParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::trigger_is_not_abstract():
    assert not inspect.isabstract(becontent::Trigger)


def test_becontent::trigger_constructor_exists():
    assert callable(becontent::Trigger.__init__)


def test_becontent::trigger_constructor_args():
    sig = inspect.signature(becontent::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::trigger_has_value():
    assert hasattr(becontent::Trigger, "value")
    descriptor = None
    for klass in becontent::Trigger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_becontent::trigger_has_name():
    assert hasattr(becontent::Trigger, "name")
    descriptor = None
    for klass in becontent::Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::copy_is_not_abstract():
    assert not inspect.isabstract(becontent::Copy)


def test_becontent::copy_constructor_exists():
    assert callable(becontent::Copy.__init__)


def test_becontent::copy_constructor_args():
    sig = inspect.signature(becontent::Copy.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName1" in params, "Missing parameter 'fieldName1'"
    assert "fieldName2" in params, "Missing parameter 'fieldName2'"

def test_becontent::copy_has_fieldName1():
    assert hasattr(becontent::Copy, "fieldName1")
    descriptor = None
    for klass in becontent::Copy.__mro__:
        if "fieldName1" in klass.__dict__:
            descriptor = klass.__dict__["fieldName1"]
            break
    assert isinstance(descriptor, property)

def test_becontent::copy_has_fieldName2():
    assert hasattr(becontent::Copy, "fieldName2")
    descriptor = None
    for klass in becontent::Copy.__mro__:
        if "fieldName2" in klass.__dict__:
            descriptor = klass.__dict__["fieldName2"]
            break
    assert isinstance(descriptor, property)



def test_becontent::applycommand_is_not_abstract():
    assert not inspect.isabstract(becontent::ApplyCommand)


def test_becontent::applycommand_constructor_exists():
    assert callable(becontent::ApplyCommand.__init__)


def test_becontent::applycommand_constructor_args():
    sig = inspect.signature(becontent::ApplyCommand.__init__)
    params = list(sig.parameters.keys())



def test_becontent::propagate_is_not_abstract():
    assert not inspect.isabstract(becontent::Propagate)


def test_becontent::propagate_constructor_exists():
    assert callable(becontent::Propagate.__init__)


def test_becontent::propagate_constructor_args():
    sig = inspect.signature(becontent::Propagate.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName2" in params, "Missing parameter 'fieldName2'"
    assert "fieldName1" in params, "Missing parameter 'fieldName1'"

def test_becontent::propagate_has_fieldName2():
    assert hasattr(becontent::Propagate, "fieldName2")
    descriptor = None
    for klass in becontent::Propagate.__mro__:
        if "fieldName2" in klass.__dict__:
            descriptor = klass.__dict__["fieldName2"]
            break
    assert isinstance(descriptor, property)

def test_becontent::propagate_has_fieldName1():
    assert hasattr(becontent::Propagate, "fieldName1")
    descriptor = None
    for klass in becontent::Propagate.__mro__:
        if "fieldName1" in klass.__dict__:
            descriptor = klass.__dict__["fieldName1"]
            break
    assert isinstance(descriptor, property)



def test_becontent::parameter_is_not_abstract():
    assert not inspect.isabstract(becontent::Parameter)


def test_becontent::parameter_constructor_exists():
    assert callable(becontent::Parameter.__init__)


def test_becontent::parameter_constructor_args():
    sig = inspect.signature(becontent::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_becontent::parameter_has_name():
    assert hasattr(becontent::Parameter, "name")
    descriptor = None
    for klass in becontent::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::parameter_has_value():
    assert hasattr(becontent::Parameter, "value")
    descriptor = None
    for klass in becontent::Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_viewitem_is_not_abstract():
    assert not inspect.isabstract(ViewItem)


def test_viewitem_constructor_exists():
    assert callable(ViewItem.__init__)


def test_viewitem_constructor_args():
    sig = inspect.signature(ViewItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent::template_is_not_abstract():
    assert not inspect.isabstract(becontent::Template)


def test_becontent::template_constructor_exists():
    assert callable(becontent::Template.__init__)


def test_becontent::template_constructor_args():
    sig = inspect.signature(becontent::Template.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "path" in params, "Missing parameter 'path'"

def test_becontent::template_has__id_model():
    assert hasattr(becontent::Template, "_id_model")
    descriptor = None
    for klass in becontent::Template.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::template_has_path():
    assert hasattr(becontent::Template, "path")
    descriptor = None
    for klass in becontent::Template.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_becontent::skin_is_not_abstract():
    assert not inspect.isabstract(becontent::Skin)


def test_becontent::skin_constructor_exists():
    assert callable(becontent::Skin.__init__)


def test_becontent::skin_constructor_args():
    sig = inspect.signature(becontent::Skin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::skin_has_name():
    assert hasattr(becontent::Skin, "name")
    descriptor = None
    for klass in becontent::Skin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::viewitem_is_not_abstract():
    assert not inspect.isabstract(becontent::ViewItem)


def test_becontent::viewitem_constructor_exists():
    assert callable(becontent::ViewItem.__init__)


def test_becontent::viewitem_constructor_args():
    sig = inspect.signature(becontent::ViewItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent::content_is_not_abstract():
    assert not inspect.isabstract(becontent::Content)


def test_becontent::content_constructor_exists():
    assert callable(becontent::Content.__init__)


def test_becontent::content_constructor_args():
    sig = inspect.signature(becontent::Content.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "presentationFields" in params, "Missing parameter 'presentationFields'"
    assert "template" in params, "Missing parameter 'template'"
    assert "orderFields" in params, "Missing parameter 'orderFields'"
    assert "joinCondition" in params, "Missing parameter 'joinCondition'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent::content_has_style():
    assert hasattr(becontent::Content, "style")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_limit():
    assert hasattr(becontent::Content, "limit")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_presentationFields():
    assert hasattr(becontent::Content, "presentationFields")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "presentationFields" in klass.__dict__:
            descriptor = klass.__dict__["presentationFields"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_template():
    assert hasattr(becontent::Content, "template")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_orderFields():
    assert hasattr(becontent::Content, "orderFields")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "orderFields" in klass.__dict__:
            descriptor = klass.__dict__["orderFields"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_joinCondition():
    assert hasattr(becontent::Content, "joinCondition")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "joinCondition" in klass.__dict__:
            descriptor = klass.__dict__["joinCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has_filter():
    assert hasattr(becontent::Content, "filter")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)

def test_becontent::content_has__id_model():
    assert hasattr(becontent::Content, "_id_model")
    descriptor = None
    for klass in becontent::Content.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_becontent::skinlet_is_not_abstract():
    assert not inspect.isabstract(becontent::Skinlet)


def test_becontent::skinlet_constructor_exists():
    assert callable(becontent::Skinlet.__init__)


def test_becontent::skinlet_constructor_args():
    sig = inspect.signature(becontent::Skinlet.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "template" in params, "Missing parameter 'template'"

def test_becontent::skinlet_has__id_model():
    assert hasattr(becontent::Skinlet, "_id_model")
    descriptor = None
    for klass in becontent::Skinlet.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::skinlet_has_template():
    assert hasattr(becontent::Skinlet, "template")
    descriptor = None
    for klass in becontent::Skinlet.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_typedsystemattribute_is_not_abstract():
    assert not inspect.isabstract(TypedSystemAttribute)


def test_typedsystemattribute_constructor_exists():
    assert callable(TypedSystemAttribute.__init__)


def test_typedsystemattribute_constructor_args():
    sig = inspect.signature(TypedSystemAttribute.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributeposition_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributePosition)


def test_becontent::systemattributeposition_constructor_exists():
    assert callable(becontent::SystemAttributePosition.__init__)


def test_becontent::systemattributeposition_constructor_args():
    sig = inspect.signature(becontent::SystemAttributePosition.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributelongdate_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeLongDate)


def test_becontent::systemattributelongdate_constructor_exists():
    assert callable(becontent::SystemAttributeLongDate.__init__)


def test_becontent::systemattributelongdate_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeLongDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributetext_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeText)


def test_becontent::systemattributetext_constructor_exists():
    assert callable(becontent::SystemAttributeText.__init__)


def test_becontent::systemattributetext_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeText.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributepassword_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributePassword)


def test_becontent::systemattributepassword_constructor_exists():
    assert callable(becontent::SystemAttributePassword.__init__)


def test_becontent::systemattributepassword_constructor_args():
    sig = inspect.signature(becontent::SystemAttributePassword.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributedate_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeDate)


def test_becontent::systemattributedate_constructor_exists():
    assert callable(becontent::SystemAttributeDate.__init__)


def test_becontent::systemattributedate_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributecolor_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeColor)


def test_becontent::systemattributecolor_constructor_exists():
    assert callable(becontent::SystemAttributeColor.__init__)


def test_becontent::systemattributecolor_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeColor.__init__)
    params = list(sig.parameters.keys())



def test_systementityfield_is_not_abstract():
    assert not inspect.isabstract(SystemEntityField)


def test_systementityfield_constructor_exists():
    assert callable(SystemEntityField.__init__)


def test_systementityfield_constructor_args():
    sig = inspect.signature(SystemEntityField.__init__)
    params = list(sig.parameters.keys())



def test_becontent::typedsystemattribute_is_not_abstract():
    assert not inspect.isabstract(becontent::TypedSystemAttribute)


def test_becontent::typedsystemattribute_constructor_exists():
    assert callable(becontent::TypedSystemAttribute.__init__)


def test_becontent::typedsystemattribute_constructor_args():
    sig = inspect.signature(becontent::TypedSystemAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::typedsystemattribute_has_isMandatory():
    assert hasattr(becontent::TypedSystemAttribute, "isMandatory")
    descriptor = None
    for klass in becontent::TypedSystemAttribute.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent::typedsystemattribute_has_name():
    assert hasattr(becontent::TypedSystemAttribute, "name")
    descriptor = None
    for klass in becontent::TypedSystemAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::systemreference_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemReference)


def test_becontent::systemreference_constructor_exists():
    assert callable(becontent::SystemReference.__init__)


def test_becontent::systemreference_constructor_args():
    sig = inspect.signature(becontent::SystemReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::systemreference_has_name():
    assert hasattr(becontent::SystemReference, "name")
    descriptor = None
    for klass in becontent::SystemReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::systemattributefiletofolder_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeFileToFolder)


def test_becontent::systemattributefiletofolder_constructor_exists():
    assert callable(becontent::SystemAttributeFileToFolder.__init__)


def test_becontent::systemattributefiletofolder_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeFileToFolder.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributefile_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeFile)


def test_becontent::systemattributefile_constructor_exists():
    assert callable(becontent::SystemAttributeFile.__init__)


def test_becontent::systemattributefile_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeFile.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemattributevarchar_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeVarchar)


def test_becontent::systemattributevarchar_constructor_exists():
    assert callable(becontent::SystemAttributeVarchar.__init__)


def test_becontent::systemattributevarchar_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeVarchar.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent::systemattributevarchar_has_length():
    assert hasattr(becontent::SystemAttributeVarchar, "length")
    descriptor = None
    for klass in becontent::SystemAttributeVarchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_becontent::systemattributevarchar_has_isPrimaryKey():
    assert hasattr(becontent::SystemAttributeVarchar, "isPrimaryKey")
    descriptor = None
    for klass in becontent::SystemAttributeVarchar.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent::systemattributeinteger_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeInteger)


def test_becontent::systemattributeinteger_constructor_exists():
    assert callable(becontent::SystemAttributeInteger.__init__)


def test_becontent::systemattributeinteger_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent::systemattributeinteger_has_isPrimaryKey():
    assert hasattr(becontent::SystemAttributeInteger, "isPrimaryKey")
    descriptor = None
    for klass in becontent::SystemAttributeInteger.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent::systemattributeimage_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemAttributeImage)


def test_becontent::systemattributeimage_constructor_exists():
    assert callable(becontent::SystemAttributeImage.__init__)


def test_becontent::systemattributeimage_constructor_args():
    sig = inspect.signature(becontent::SystemAttributeImage.__init__)
    params = list(sig.parameters.keys())



def test_typedattribute_is_not_abstract():
    assert not inspect.isabstract(TypedAttribute)


def test_typedattribute_constructor_exists():
    assert callable(TypedAttribute.__init__)


def test_typedattribute_constructor_args():
    sig = inspect.signature(TypedAttribute.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributefiletofolder_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeFileToFolder)


def test_becontent::attributefiletofolder_constructor_exists():
    assert callable(becontent::AttributeFileToFolder.__init__)


def test_becontent::attributefiletofolder_constructor_args():
    sig = inspect.signature(becontent::AttributeFileToFolder.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributecolor_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeColor)


def test_becontent::attributecolor_constructor_exists():
    assert callable(becontent::AttributeColor.__init__)


def test_becontent::attributecolor_constructor_args():
    sig = inspect.signature(becontent::AttributeColor.__init__)
    params = list(sig.parameters.keys())



def test_entityfield_is_not_abstract():
    assert not inspect.isabstract(EntityField)


def test_entityfield_constructor_exists():
    assert callable(EntityField.__init__)


def test_entityfield_constructor_args():
    sig = inspect.signature(EntityField.__init__)
    params = list(sig.parameters.keys())



def test_becontent::typedattribute_is_not_abstract():
    assert not inspect.isabstract(becontent::TypedAttribute)


def test_becontent::typedattribute_constructor_exists():
    assert callable(becontent::TypedAttribute.__init__)


def test_becontent::typedattribute_constructor_args():
    sig = inspect.signature(becontent::TypedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent::typedattribute_has_name():
    assert hasattr(becontent::TypedAttribute, "name")
    descriptor = None
    for klass in becontent::TypedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::typedattribute_has_isMandatory():
    assert hasattr(becontent::TypedAttribute, "isMandatory")
    descriptor = None
    for klass in becontent::TypedAttribute.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent::reference_is_not_abstract():
    assert not inspect.isabstract(becontent::Reference)


def test_becontent::reference_constructor_exists():
    assert callable(becontent::Reference.__init__)


def test_becontent::reference_constructor_args():
    sig = inspect.signature(becontent::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent::reference_has_name():
    assert hasattr(becontent::Reference, "name")
    descriptor = None
    for klass in becontent::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent::attributefile_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeFile)


def test_becontent::attributefile_constructor_exists():
    assert callable(becontent::AttributeFile.__init__)


def test_becontent::attributefile_constructor_args():
    sig = inspect.signature(becontent::AttributeFile.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributevarchar_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeVarchar)


def test_becontent::attributevarchar_constructor_exists():
    assert callable(becontent::AttributeVarchar.__init__)


def test_becontent::attributevarchar_constructor_args():
    sig = inspect.signature(becontent::AttributeVarchar.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent::attributevarchar_has_length():
    assert hasattr(becontent::AttributeVarchar, "length")
    descriptor = None
    for klass in becontent::AttributeVarchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_becontent::attributevarchar_has_isPrimaryKey():
    assert hasattr(becontent::AttributeVarchar, "isPrimaryKey")
    descriptor = None
    for klass in becontent::AttributeVarchar.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent::attributeinteger_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeInteger)


def test_becontent::attributeinteger_constructor_exists():
    assert callable(becontent::AttributeInteger.__init__)


def test_becontent::attributeinteger_constructor_args():
    sig = inspect.signature(becontent::AttributeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent::attributeinteger_has_isPrimaryKey():
    assert hasattr(becontent::AttributeInteger, "isPrimaryKey")
    descriptor = None
    for klass in becontent::AttributeInteger.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent::attributeimage_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeImage)


def test_becontent::attributeimage_constructor_exists():
    assert callable(becontent::AttributeImage.__init__)


def test_becontent::attributeimage_constructor_args():
    sig = inspect.signature(becontent::AttributeImage.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributeposition_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributePosition)


def test_becontent::attributeposition_constructor_exists():
    assert callable(becontent::AttributePosition.__init__)


def test_becontent::attributeposition_constructor_args():
    sig = inspect.signature(becontent::AttributePosition.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributepassword_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributePassword)


def test_becontent::attributepassword_constructor_exists():
    assert callable(becontent::AttributePassword.__init__)


def test_becontent::attributepassword_constructor_args():
    sig = inspect.signature(becontent::AttributePassword.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributetext_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeText)


def test_becontent::attributetext_constructor_exists():
    assert callable(becontent::AttributeText.__init__)


def test_becontent::attributetext_constructor_args():
    sig = inspect.signature(becontent::AttributeText.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributelongdate_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeLongDate)


def test_becontent::attributelongdate_constructor_exists():
    assert callable(becontent::AttributeLongDate.__init__)


def test_becontent::attributelongdate_constructor_args():
    sig = inspect.signature(becontent::AttributeLongDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent::attributedate_is_not_abstract():
    assert not inspect.isabstract(becontent::AttributeDate)


def test_becontent::attributedate_constructor_exists():
    assert callable(becontent::AttributeDate.__init__)


def test_becontent::attributedate_constructor_args():
    sig = inspect.signature(becontent::AttributeDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent::entityfield_is_not_abstract():
    assert not inspect.isabstract(becontent::EntityField)


def test_becontent::entityfield_constructor_exists():
    assert callable(becontent::EntityField.__init__)


def test_becontent::entityfield_constructor_args():
    sig = inspect.signature(becontent::EntityField.__init__)
    params = list(sig.parameters.keys())
    assert "isSearchPresentationHead" in params, "Missing parameter 'isSearchPresentationHead'"
    assert "isSearchPresentationBody" in params, "Missing parameter 'isSearchPresentationBody'"
    assert "isPresented" in params, "Missing parameter 'isPresented'"
    assert "isTextSearch" in params, "Missing parameter 'isTextSearch'"

def test_becontent::entityfield_has_isSearchPresentationHead():
    assert hasattr(becontent::EntityField, "isSearchPresentationHead")
    descriptor = None
    for klass in becontent::EntityField.__mro__:
        if "isSearchPresentationHead" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationHead"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entityfield_has_isSearchPresentationBody():
    assert hasattr(becontent::EntityField, "isSearchPresentationBody")
    descriptor = None
    for klass in becontent::EntityField.__mro__:
        if "isSearchPresentationBody" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationBody"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entityfield_has_isPresented():
    assert hasattr(becontent::EntityField, "isPresented")
    descriptor = None
    for klass in becontent::EntityField.__mro__:
        if "isPresented" in klass.__dict__:
            descriptor = klass.__dict__["isPresented"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entityfield_has_isTextSearch():
    assert hasattr(becontent::EntityField, "isTextSearch")
    descriptor = None
    for klass in becontent::EntityField.__mro__:
        if "isTextSearch" in klass.__dict__:
            descriptor = klass.__dict__["isTextSearch"]
            break
    assert isinstance(descriptor, property)



def test_definitionitem_is_not_abstract():
    assert not inspect.isabstract(DefinitionItem)


def test_definitionitem_constructor_exists():
    assert callable(DefinitionItem.__init__)


def test_definitionitem_constructor_args():
    sig = inspect.signature(DefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent::entity_is_not_abstract():
    assert not inspect.isabstract(becontent::Entity)


def test_becontent::entity_constructor_exists():
    assert callable(becontent::Entity.__init__)


def test_becontent::entity_constructor_args():
    sig = inspect.signature(becontent::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "presentationString" in params, "Missing parameter 'presentationString'"
    assert "rssFilter" in params, "Missing parameter 'rssFilter'"
    assert "isOwned" in params, "Missing parameter 'isOwned'"

def test_becontent::entity_has_variableName():
    assert hasattr(becontent::Entity, "variableName")
    descriptor = None
    for klass in becontent::Entity.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entity_has_name():
    assert hasattr(becontent::Entity, "name")
    descriptor = None
    for klass in becontent::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entity_has_presentationString():
    assert hasattr(becontent::Entity, "presentationString")
    descriptor = None
    for klass in becontent::Entity.__mro__:
        if "presentationString" in klass.__dict__:
            descriptor = klass.__dict__["presentationString"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entity_has_rssFilter():
    assert hasattr(becontent::Entity, "rssFilter")
    descriptor = None
    for klass in becontent::Entity.__mro__:
        if "rssFilter" in klass.__dict__:
            descriptor = klass.__dict__["rssFilter"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entity_has_isOwned():
    assert hasattr(becontent::Entity, "isOwned")
    descriptor = None
    for klass in becontent::Entity.__mro__:
        if "isOwned" in klass.__dict__:
            descriptor = klass.__dict__["isOwned"]
            break
    assert isinstance(descriptor, property)



def test_becontentelement_is_not_abstract():
    assert not inspect.isabstract(BeContentElement)


def test_becontentelement_constructor_exists():
    assert callable(BeContentElement.__init__)


def test_becontentelement_constructor_args():
    sig = inspect.signature(BeContentElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent::channel_is_not_abstract():
    assert not inspect.isabstract(becontent::Channel)


def test_becontent::channel_constructor_exists():
    assert callable(becontent::Channel.__init__)


def test_becontent::channel_constructor_args():
    sig = inspect.signature(becontent::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_becontent::channel_has__id_model():
    assert hasattr(becontent::Channel, "_id_model")
    descriptor = None
    for klass in becontent::Channel.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::channel_has_parameters():
    assert hasattr(becontent::Channel, "parameters")
    descriptor = None
    for klass in becontent::Channel.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_becontent::filetofolderextension_is_not_abstract():
    assert not inspect.isabstract(becontent::FileToFolderExtension)


def test_becontent::filetofolderextension_constructor_exists():
    assert callable(becontent::FileToFolderExtension.__init__)


def test_becontent::filetofolderextension_constructor_args():
    sig = inspect.signature(becontent::FileToFolderExtension.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "extensionValue" in params, "Missing parameter 'extensionValue'"
    assert "extensionKey" in params, "Missing parameter 'extensionKey'"

def test_becontent::filetofolderextension_has__id_model():
    assert hasattr(becontent::FileToFolderExtension, "_id_model")
    descriptor = None
    for klass in becontent::FileToFolderExtension.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolderextension_has_extensionValue():
    assert hasattr(becontent::FileToFolderExtension, "extensionValue")
    descriptor = None
    for klass in becontent::FileToFolderExtension.__mro__:
        if "extensionValue" in klass.__dict__:
            descriptor = klass.__dict__["extensionValue"]
            break
    assert isinstance(descriptor, property)

def test_becontent::filetofolderextension_has_extensionKey():
    assert hasattr(becontent::FileToFolderExtension, "extensionKey")
    descriptor = None
    for klass in becontent::FileToFolderExtension.__mro__:
        if "extensionKey" in klass.__dict__:
            descriptor = klass.__dict__["extensionKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent::entitymanagerpage_is_not_abstract():
    assert not inspect.isabstract(becontent::EntityManagerPage)


def test_becontent::entitymanagerpage_constructor_exists():
    assert callable(becontent::EntityManagerPage.__init__)


def test_becontent::entitymanagerpage_constructor_args():
    sig = inspect.signature(becontent::EntityManagerPage.__init__)
    params = list(sig.parameters.keys())
    assert "skin" in params, "Missing parameter 'skin'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_becontent::entitymanagerpage_has_skin():
    assert hasattr(becontent::EntityManagerPage, "skin")
    descriptor = None
    for klass in becontent::EntityManagerPage.__mro__:
        if "skin" in klass.__dict__:
            descriptor = klass.__dict__["skin"]
            break
    assert isinstance(descriptor, property)

def test_becontent::entitymanagerpage_has_fileName():
    assert hasattr(becontent::EntityManagerPage, "fileName")
    descriptor = None
    for klass in becontent::EntityManagerPage.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_becontent::definitionitem_is_not_abstract():
    assert not inspect.isabstract(becontent::DefinitionItem)


def test_becontent::definitionitem_constructor_exists():
    assert callable(becontent::DefinitionItem.__init__)


def test_becontent::definitionitem_constructor_args():
    sig = inspect.signature(becontent::DefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent::becontentelement_is_not_abstract():
    assert not inspect.isabstract(becontent::BeContentElement)


def test_becontent::becontentelement_constructor_exists():
    assert callable(becontent::BeContentElement.__init__)


def test_becontent::becontentelement_constructor_args():
    sig = inspect.signature(becontent::BeContentElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent::becontentmodel_is_not_abstract():
    assert not inspect.isabstract(becontent::BeContentModel)


def test_becontent::becontentmodel_constructor_exists():
    assert callable(becontent::BeContentModel.__init__)


def test_becontent::becontentmodel_constructor_args():
    sig = inspect.signature(becontent::BeContentModel.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systemrelation_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemRelation)


def test_becontent::systemrelation_constructor_exists():
    assert callable(becontent::SystemRelation.__init__)


def test_becontent::systemrelation_constructor_args():
    sig = inspect.signature(becontent::SystemRelation.__init__)
    params = list(sig.parameters.keys())



def test_becontent::customrelation_is_not_abstract():
    assert not inspect.isabstract(becontent::CustomRelation)


def test_becontent::customrelation_constructor_exists():
    assert callable(becontent::CustomRelation.__init__)


def test_becontent::customrelation_constructor_args():
    sig = inspect.signature(becontent::CustomRelation.__init__)
    params = list(sig.parameters.keys())



def test_becontent::relation_is_not_abstract():
    assert not inspect.isabstract(becontent::Relation)


def test_becontent::relation_constructor_exists():
    assert callable(becontent::Relation.__init__)


def test_becontent::relation_constructor_args():
    sig = inspect.signature(becontent::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_becontent::relation_has_name():
    assert hasattr(becontent::Relation, "name")
    descriptor = None
    for klass in becontent::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent::relation_has_variableName():
    assert hasattr(becontent::Relation, "variableName")
    descriptor = None
    for klass in becontent::Relation.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_becontent::systementityfield_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemEntityField)


def test_becontent::systementityfield_constructor_exists():
    assert callable(becontent::SystemEntityField.__init__)


def test_becontent::systementityfield_constructor_args():
    sig = inspect.signature(becontent::SystemEntityField.__init__)
    params = list(sig.parameters.keys())
    assert "isPresented" in params, "Missing parameter 'isPresented'"
    assert "isSearchPresentationBody" in params, "Missing parameter 'isSearchPresentationBody'"
    assert "isTextSearch" in params, "Missing parameter 'isTextSearch'"
    assert "isSearchPresentationHead" in params, "Missing parameter 'isSearchPresentationHead'"

def test_becontent::systementityfield_has_isPresented():
    assert hasattr(becontent::SystemEntityField, "isPresented")
    descriptor = None
    for klass in becontent::SystemEntityField.__mro__:
        if "isPresented" in klass.__dict__:
            descriptor = klass.__dict__["isPresented"]
            break
    assert isinstance(descriptor, property)

def test_becontent::systementityfield_has_isSearchPresentationBody():
    assert hasattr(becontent::SystemEntityField, "isSearchPresentationBody")
    descriptor = None
    for klass in becontent::SystemEntityField.__mro__:
        if "isSearchPresentationBody" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationBody"]
            break
    assert isinstance(descriptor, property)

def test_becontent::systementityfield_has_isTextSearch():
    assert hasattr(becontent::SystemEntityField, "isTextSearch")
    descriptor = None
    for klass in becontent::SystemEntityField.__mro__:
        if "isTextSearch" in klass.__dict__:
            descriptor = klass.__dict__["isTextSearch"]
            break
    assert isinstance(descriptor, property)

def test_becontent::systementityfield_has_isSearchPresentationHead():
    assert hasattr(becontent::SystemEntityField, "isSearchPresentationHead")
    descriptor = None
    for klass in becontent::SystemEntityField.__mro__:
        if "isSearchPresentationHead" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationHead"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_becontent::systementity_is_not_abstract():
    assert not inspect.isabstract(becontent::SystemEntity)


def test_becontent::systementity_constructor_exists():
    assert callable(becontent::SystemEntity.__init__)


def test_becontent::systementity_constructor_args():
    sig = inspect.signature(becontent::SystemEntity.__init__)
    params = list(sig.parameters.keys())



def test_becontent::customentity_is_not_abstract():
    assert not inspect.isabstract(becontent::CustomEntity)


def test_becontent::customentity_constructor_exists():
    assert callable(becontent::CustomEntity.__init__)


def test_becontent::customentity_constructor_args():
    sig = inspect.signature(becontent::CustomEntity.__init__)
    params = list(sig.parameters.keys())



def test_becontent::handler_is_not_abstract():
    assert not inspect.isabstract(becontent::Handler)


def test_becontent::handler_constructor_exists():
    assert callable(becontent::Handler.__init__)


def test_becontent::handler_constructor_args():
    sig = inspect.signature(becontent::Handler.__init__)
    params = list(sig.parameters.keys())
    assert "mainSkinPlaceholder" in params, "Missing parameter 'mainSkinPlaceholder'"
    assert "mainSkinWithPager" in params, "Missing parameter 'mainSkinWithPager'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "mainSkinPagerLength" in params, "Missing parameter 'mainSkinPagerLength'"

def test_becontent::handler_has_mainSkinPlaceholder():
    assert hasattr(becontent::Handler, "mainSkinPlaceholder")
    descriptor = None
    for klass in becontent::Handler.__mro__:
        if "mainSkinPlaceholder" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinPlaceholder"]
            break
    assert isinstance(descriptor, property)

def test_becontent::handler_has_mainSkinWithPager():
    assert hasattr(becontent::Handler, "mainSkinWithPager")
    descriptor = None
    for klass in becontent::Handler.__mro__:
        if "mainSkinWithPager" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinWithPager"]
            break
    assert isinstance(descriptor, property)

def test_becontent::handler_has_fileName():
    assert hasattr(becontent::Handler, "fileName")
    descriptor = None
    for klass in becontent::Handler.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_becontent::handler_has_mainSkinPagerLength():
    assert hasattr(becontent::Handler, "mainSkinPagerLength")
    descriptor = None
    for klass in becontent::Handler.__mro__:
        if "mainSkinPagerLength" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinPagerLength"]
            break
    assert isinstance(descriptor, property)

def test_formmethodtype_exists():
    # Check that the Enumeration exists
    assert FormMethodType is not None

def test_formmethodtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FormMethodType]
    expected_literals = [
        "post",
        "get",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FormMethodType"

def test_contentstyle_exists():
    # Check that the Enumeration exists
    assert ContentStyle is not None

def test_contentstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContentStyle]
    expected_literals = [
        "hierarchical",
        "normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContentStyle"

def test_conditionaltemplateexptype_exists():
    # Check that the Enumeration exists
    assert ConditionalTemplateExpType is not None

def test_conditionaltemplateexptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionalTemplateExpType]
    expected_literals = [
        "isNotEmpty",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionalTemplateExpType"

def test_orientationtype_exists():
    # Check that the Enumeration exists
    assert OrientationType is not None

def test_orientationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrientationType]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrientationType"

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "implies",
        "dateLessEqual",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"


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
NotStructuredElement_strategy = st.builds(
    NotStructuredElement,
)
becontent::RelationManager_strategy = st.builds(
    becontent::RelationManager,
    orientation=
        safe_text,
    label=
        safe_text,
    name=
        safe_text,
    restrictCondition=
        safe_text
)
becontent::Hidden_strategy = st.builds(
    becontent::Hidden,
    name=
        safe_text,
    values=
        safe_text
)
becontent::Position_strategy = st.builds(
    becontent::Position,
    name=
        safe_text,
    label=
        safe_text,
    isMandatory=
        st.booleans(),
    size=
        st.integers(),
    controlledField=
        safe_text
)
becontent::Textarea_strategy = st.builds(
    becontent::Textarea,
    rows=
        st.integers(),
    name=
        safe_text,
    isMandatory=
        st.booleans(),
    columns=
        st.integers(),
    label=
        safe_text
)
becontent::File_strategy = st.builds(
    becontent::File,
    name=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    extensionMessage=
        safe_text,
    extension=
        safe_text
)
becontent::Link_strategy = st.builds(
    becontent::Link,
    size=
        st.integers(),
    label=
        safe_text,
    maxLength=
        st.integers(),
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent::Year_strategy = st.builds(
    becontent::Year,
    name=
        safe_text,
    label=
        safe_text,
    start=
        st.integers(),
    end=
        st.integers(),
    isMandatory=
        st.booleans()
)
becontent::SelectFromReference_strategy = st.builds(
    becontent::SelectFromReference,
    isMandatory=
        st.booleans(),
    restrictCondition=
        safe_text,
    name=
        safe_text,
    label=
        safe_text
)
becontent::RadioFromReference_strategy = st.builds(
    becontent::RadioFromReference,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    name=
        safe_text,
    restrictCondition=
        safe_text
)
becontent::LongDate_strategy = st.builds(
    becontent::LongDate,
    label=
        safe_text,
    isMandatory=
        st.booleans(),
    name=
        safe_text
)
becontent::Password_strategy = st.builds(
    becontent::Password,
    maxLength=
        st.integers(),
    name=
        safe_text,
    label=
        safe_text,
    size=
        st.integers(),
    isMandatory=
        st.booleans()
)
becontent::FileToFolder_strategy = st.builds(
    becontent::FileToFolder,
    extension=
        safe_text,
    extensionMessage=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    name=
        safe_text
)
becontent::HierarchicalPosition_strategy = st.builds(
    becontent::HierarchicalPosition,
    label=
        safe_text,
    size=
        st.integers(),
    controlledField=
        safe_text,
    referenceField=
        safe_text,
    name=
        safe_text
)
becontent::Image_strategy = st.builds(
    becontent::Image,
    isMandatory=
        st.booleans(),
    name=
        safe_text,
    label=
        safe_text
)
becontent::Date_strategy = st.builds(
    becontent::Date,
    name=
        safe_text,
    label=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent::Color_strategy = st.builds(
    becontent::Color,
    name=
        safe_text,
    defaultColor=
        safe_text,
    label=
        safe_text
)
becontent::Editor_strategy = st.builds(
    becontent::Editor,
    rows=
        st.integers(),
    columns=
        st.integers(),
    label=
        safe_text,
    isMandatory=
        st.booleans(),
    name=
        safe_text
)
becontent::Select_strategy = st.builds(
    becontent::Select,
    values=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    name=
        safe_text
)
becontent::Section_strategy = st.builds(
    becontent::Section,
    name=
        safe_text,
    text=
        safe_text
)
Form_strategy = st.builds(
    Form,
)
becontent::ExtendedForm_strategy = st.builds(
    becontent::ExtendedForm,
    className=
        safe_text
)
becontent::Checkbox_strategy = st.builds(
    becontent::Checkbox,
    name=
        safe_text,
    isChecked=
        st.booleans(),
    label=
        safe_text,
    value=
        safe_text
)
becontent::RadioButton_strategy = st.builds(
    becontent::RadioButton,
    values=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
becontent::Text_strategy = st.builds(
    becontent::Text,
    size=
        st.integers(),
    name=
        safe_text,
    label=
        safe_text,
    isMandatory=
        st.booleans(),
    maxLength=
        st.integers()
)
becontent::Validation_strategy = st.builds(
    becontent::Validation,
    message=
        safe_text,
    _id_model=
        safe_text,
    condition=
        safe_text
)
becontent::CustomPager_strategy = st.builds(
    becontent::CustomPager,
    order=
        safe_text,
    _id_model=
        safe_text,
    template=
        safe_text,
    className=
        safe_text,
    filter=
        safe_text,
    query=
        safe_text,
    length=
        st.integers()
)
ApplyCommand_strategy = st.builds(
    ApplyCommand,
)
becontent::ApplyItem_strategy = st.builds(
    becontent::ApplyItem,
    prefix=
        safe_text,
    key=
        safe_text
)
becontent::ApplyIndexed_strategy = st.builds(
    becontent::ApplyIndexed,
)
becontent::Apply_strategy = st.builds(
    becontent::Apply,
    prefix=
        safe_text
)
FormElement_strategy = st.builds(
    FormElement,
)
becontent::NotStructuredElement_strategy = st.builds(
    becontent::NotStructuredElement,
    helper=
        safe_text
)
becontent::Form_strategy = st.builds(
    becontent::Form,
    name=
        safe_text,
    method=
        safe_text,
    description=
        safe_text
)
becontent::FormElement_strategy = st.builds(
    becontent::FormElement,
)
becontent::ConditionalTemplate_strategy = st.builds(
    becontent::ConditionalTemplate,
    conditionExp=
        safe_text,
    falseTemplate=
        safe_text,
    fieldName=
        safe_text,
    _id_model=
        safe_text,
    trueTemplate=
        safe_text
)
becontent::ContentCommand_strategy = st.builds(
    becontent::ContentCommand,
    _id_model=
        safe_text
)
becontent::JoinEntity_strategy = st.builds(
    becontent::JoinEntity,
    _id_model=
        safe_text
)
ContentCommand_strategy = st.builds(
    ContentCommand,
)
becontent::UnsetParameter_strategy = st.builds(
    becontent::UnsetParameter,
    name=
        safe_text
)
becontent::Trigger_strategy = st.builds(
    becontent::Trigger,
    value=
        safe_text,
    name=
        safe_text
)
becontent::Copy_strategy = st.builds(
    becontent::Copy,
    fieldName1=
        safe_text,
    fieldName2=
        safe_text
)
becontent::ApplyCommand_strategy = st.builds(
    becontent::ApplyCommand,
)
becontent::Propagate_strategy = st.builds(
    becontent::Propagate,
    fieldName2=
        safe_text,
    fieldName1=
        safe_text
)
becontent::Parameter_strategy = st.builds(
    becontent::Parameter,
    name=
        safe_text,
    value=
        safe_text
)
ViewItem_strategy = st.builds(
    ViewItem,
)
becontent::Template_strategy = st.builds(
    becontent::Template,
    _id_model=
        safe_text,
    path=
        safe_text
)
becontent::Skin_strategy = st.builds(
    becontent::Skin,
    name=
        safe_text
)
becontent::ViewItem_strategy = st.builds(
    becontent::ViewItem,
)
becontent::Content_strategy = st.builds(
    becontent::Content,
    style=
        safe_text,
    limit=
        st.integers(),
    presentationFields=
        safe_text,
    template=
        safe_text,
    orderFields=
        safe_text,
    joinCondition=
        safe_text,
    filter=
        safe_text,
    _id_model=
        safe_text
)
becontent::Skinlet_strategy = st.builds(
    becontent::Skinlet,
    _id_model=
        safe_text,
    template=
        safe_text
)
TypedSystemAttribute_strategy = st.builds(
    TypedSystemAttribute,
)
becontent::SystemAttributePosition_strategy = st.builds(
    becontent::SystemAttributePosition,
)
becontent::SystemAttributeLongDate_strategy = st.builds(
    becontent::SystemAttributeLongDate,
)
becontent::SystemAttributeText_strategy = st.builds(
    becontent::SystemAttributeText,
)
becontent::SystemAttributePassword_strategy = st.builds(
    becontent::SystemAttributePassword,
)
becontent::SystemAttributeDate_strategy = st.builds(
    becontent::SystemAttributeDate,
)
becontent::SystemAttributeColor_strategy = st.builds(
    becontent::SystemAttributeColor,
)
SystemEntityField_strategy = st.builds(
    SystemEntityField,
)
becontent::TypedSystemAttribute_strategy = st.builds(
    becontent::TypedSystemAttribute,
    isMandatory=
        st.booleans(),
    name=
        safe_text
)
becontent::SystemReference_strategy = st.builds(
    becontent::SystemReference,
    name=
        safe_text
)
becontent::SystemAttributeFileToFolder_strategy = st.builds(
    becontent::SystemAttributeFileToFolder,
)
becontent::SystemAttributeFile_strategy = st.builds(
    becontent::SystemAttributeFile,
)
becontent::SystemAttributeVarchar_strategy = st.builds(
    becontent::SystemAttributeVarchar,
    length=
        st.integers(),
    isPrimaryKey=
        st.booleans()
)
becontent::SystemAttributeInteger_strategy = st.builds(
    becontent::SystemAttributeInteger,
    isPrimaryKey=
        st.booleans()
)
becontent::SystemAttributeImage_strategy = st.builds(
    becontent::SystemAttributeImage,
)
TypedAttribute_strategy = st.builds(
    TypedAttribute,
)
becontent::AttributeFileToFolder_strategy = st.builds(
    becontent::AttributeFileToFolder,
)
becontent::AttributeColor_strategy = st.builds(
    becontent::AttributeColor,
)
EntityField_strategy = st.builds(
    EntityField,
)
becontent::TypedAttribute_strategy = st.builds(
    becontent::TypedAttribute,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent::Reference_strategy = st.builds(
    becontent::Reference,
    name=
        safe_text
)
becontent::AttributeFile_strategy = st.builds(
    becontent::AttributeFile,
)
becontent::AttributeVarchar_strategy = st.builds(
    becontent::AttributeVarchar,
    length=
        st.integers(),
    isPrimaryKey=
        st.booleans()
)
becontent::AttributeInteger_strategy = st.builds(
    becontent::AttributeInteger,
    isPrimaryKey=
        st.booleans()
)
becontent::AttributeImage_strategy = st.builds(
    becontent::AttributeImage,
)
becontent::AttributePosition_strategy = st.builds(
    becontent::AttributePosition,
)
becontent::AttributePassword_strategy = st.builds(
    becontent::AttributePassword,
)
becontent::AttributeText_strategy = st.builds(
    becontent::AttributeText,
)
becontent::AttributeLongDate_strategy = st.builds(
    becontent::AttributeLongDate,
)
becontent::AttributeDate_strategy = st.builds(
    becontent::AttributeDate,
)
becontent::EntityField_strategy = st.builds(
    becontent::EntityField,
    isSearchPresentationHead=
        st.booleans(),
    isSearchPresentationBody=
        st.booleans(),
    isPresented=
        st.booleans(),
    isTextSearch=
        st.booleans()
)
DefinitionItem_strategy = st.builds(
    DefinitionItem,
)
becontent::Entity_strategy = st.builds(
    becontent::Entity,
    variableName=
        safe_text,
    name=
        safe_text,
    presentationString=
        safe_text,
    rssFilter=
        safe_text,
    isOwned=
        st.booleans()
)
BeContentElement_strategy = st.builds(
    BeContentElement,
)
becontent::Channel_strategy = st.builds(
    becontent::Channel,
    _id_model=
        safe_text,
    parameters=
        safe_text
)
becontent::FileToFolderExtension_strategy = st.builds(
    becontent::FileToFolderExtension,
    _id_model=
        safe_text,
    extensionValue=
        safe_text,
    extensionKey=
        safe_text
)
becontent::EntityManagerPage_strategy = st.builds(
    becontent::EntityManagerPage,
    skin=
        safe_text,
    fileName=
        safe_text
)
becontent::DefinitionItem_strategy = st.builds(
    becontent::DefinitionItem,
)
becontent::BeContentElement_strategy = st.builds(
    becontent::BeContentElement,
)
becontent::BeContentModel_strategy = st.builds(
    becontent::BeContentModel,
)
Relation_strategy = st.builds(
    Relation,
)
becontent::SystemRelation_strategy = st.builds(
    becontent::SystemRelation,
)
becontent::CustomRelation_strategy = st.builds(
    becontent::CustomRelation,
)
becontent::Relation_strategy = st.builds(
    becontent::Relation,
    name=
        safe_text,
    variableName=
        safe_text
)
becontent::SystemEntityField_strategy = st.builds(
    becontent::SystemEntityField,
    isPresented=
        st.booleans(),
    isSearchPresentationBody=
        st.booleans(),
    isTextSearch=
        st.booleans(),
    isSearchPresentationHead=
        st.booleans()
)
Entity_strategy = st.builds(
    Entity,
)
becontent::SystemEntity_strategy = st.builds(
    becontent::SystemEntity,
)
becontent::CustomEntity_strategy = st.builds(
    becontent::CustomEntity,
)
becontent::Handler_strategy = st.builds(
    becontent::Handler,
    mainSkinPlaceholder=
        safe_text,
    mainSkinWithPager=
        st.booleans(),
    fileName=
        safe_text,
    mainSkinPagerLength=
        st.integers()
)

@given(instance=NotStructuredElement_strategy)
@settings(max_examples=50)
def test_notstructuredelement_instantiation(instance):
    assert isinstance(instance, NotStructuredElement)

@given(instance=becontent::RelationManager_strategy)
@settings(max_examples=50)
def test_becontent::relationmanager_instantiation(instance):
    assert isinstance(instance, becontent::RelationManager)

@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_restrictCondition_type(instance):
    assert isinstance(instance.restrictCondition, str)


@given(instance=becontent::RelationManager_strategy)
def test_becontent::relationmanager_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original

@given(instance=becontent::Hidden_strategy)
@settings(max_examples=50)
def test_becontent::hidden_instantiation(instance):
    assert isinstance(instance, becontent::Hidden)

@given(instance=becontent::Hidden_strategy)
def test_becontent::hidden_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Hidden_strategy)
def test_becontent::hidden_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Hidden_strategy)
def test_becontent::hidden_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=becontent::Hidden_strategy)
def test_becontent::hidden_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent::Position_strategy)
@settings(max_examples=50)
def test_becontent::position_instantiation(instance):
    assert isinstance(instance, becontent::Position)

@given(instance=becontent::Position_strategy)
def test_becontent::position_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Position_strategy)
def test_becontent::position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Position_strategy)
def test_becontent::position_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Position_strategy)
def test_becontent::position_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Position_strategy)
def test_becontent::position_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Position_strategy)
def test_becontent::position_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Position_strategy)
def test_becontent::position_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=becontent::Position_strategy)
def test_becontent::position_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=becontent::Position_strategy)
def test_becontent::position_controlledField_type(instance):
    assert isinstance(instance.controlledField, str)


@given(instance=becontent::Position_strategy)
def test_becontent::position_controlledField_setter(instance):
    original = instance.controlledField
    instance.controlledField = original
    assert instance.controlledField == original

@given(instance=becontent::Textarea_strategy)
@settings(max_examples=50)
def test_becontent::textarea_instantiation(instance):
    assert isinstance(instance, becontent::Textarea)

@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_rows_type(instance):
    assert isinstance(instance.rows, int)


@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Textarea_strategy)
def test_becontent::textarea_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::File_strategy)
@settings(max_examples=50)
def test_becontent::file_instantiation(instance):
    assert isinstance(instance, becontent::File)

@given(instance=becontent::File_strategy)
def test_becontent::file_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::File_strategy)
def test_becontent::file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::File_strategy)
def test_becontent::file_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::File_strategy)
def test_becontent::file_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::File_strategy)
def test_becontent::file_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::File_strategy)
def test_becontent::file_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::File_strategy)
def test_becontent::file_extensionMessage_type(instance):
    assert isinstance(instance.extensionMessage, str)


@given(instance=becontent::File_strategy)
def test_becontent::file_extensionMessage_setter(instance):
    original = instance.extensionMessage
    instance.extensionMessage = original
    assert instance.extensionMessage == original

@given(instance=becontent::File_strategy)
def test_becontent::file_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=becontent::File_strategy)
def test_becontent::file_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=becontent::Link_strategy)
@settings(max_examples=50)
def test_becontent::link_instantiation(instance):
    assert isinstance(instance, becontent::Link)

@given(instance=becontent::Link_strategy)
def test_becontent::link_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=becontent::Link_strategy)
def test_becontent::link_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=becontent::Link_strategy)
def test_becontent::link_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Link_strategy)
def test_becontent::link_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Link_strategy)
def test_becontent::link_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=becontent::Link_strategy)
def test_becontent::link_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=becontent::Link_strategy)
def test_becontent::link_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Link_strategy)
def test_becontent::link_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Link_strategy)
def test_becontent::link_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Link_strategy)
def test_becontent::link_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Year_strategy)
@settings(max_examples=50)
def test_becontent::year_instantiation(instance):
    assert isinstance(instance, becontent::Year)

@given(instance=becontent::Year_strategy)
def test_becontent::year_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Year_strategy)
def test_becontent::year_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Year_strategy)
def test_becontent::year_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Year_strategy)
def test_becontent::year_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Year_strategy)
def test_becontent::year_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=becontent::Year_strategy)
def test_becontent::year_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=becontent::Year_strategy)
def test_becontent::year_end_type(instance):
    assert isinstance(instance.end, int)


@given(instance=becontent::Year_strategy)
def test_becontent::year_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=becontent::Year_strategy)
def test_becontent::year_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Year_strategy)
def test_becontent::year_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::SelectFromReference_strategy)
@settings(max_examples=50)
def test_becontent::selectfromreference_instantiation(instance):
    assert isinstance(instance, becontent::SelectFromReference)

@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_restrictCondition_type(instance):
    assert isinstance(instance.restrictCondition, str)


@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original

@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::SelectFromReference_strategy)
def test_becontent::selectfromreference_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::RadioFromReference_strategy)
@settings(max_examples=50)
def test_becontent::radiofromreference_instantiation(instance):
    assert isinstance(instance, becontent::RadioFromReference)

@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_restrictCondition_type(instance):
    assert isinstance(instance.restrictCondition, str)


@given(instance=becontent::RadioFromReference_strategy)
def test_becontent::radiofromreference_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original

@given(instance=becontent::LongDate_strategy)
@settings(max_examples=50)
def test_becontent::longdate_instantiation(instance):
    assert isinstance(instance, becontent::LongDate)

@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::LongDate_strategy)
def test_becontent::longdate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Password_strategy)
@settings(max_examples=50)
def test_becontent::password_instantiation(instance):
    assert isinstance(instance, becontent::Password)

@given(instance=becontent::Password_strategy)
def test_becontent::password_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=becontent::Password_strategy)
def test_becontent::password_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=becontent::Password_strategy)
def test_becontent::password_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Password_strategy)
def test_becontent::password_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Password_strategy)
def test_becontent::password_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Password_strategy)
def test_becontent::password_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Password_strategy)
def test_becontent::password_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=becontent::Password_strategy)
def test_becontent::password_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=becontent::Password_strategy)
def test_becontent::password_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Password_strategy)
def test_becontent::password_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::FileToFolder_strategy)
@settings(max_examples=50)
def test_becontent::filetofolder_instantiation(instance):
    assert isinstance(instance, becontent::FileToFolder)

@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_extensionMessage_type(instance):
    assert isinstance(instance.extensionMessage, str)


@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_extensionMessage_setter(instance):
    original = instance.extensionMessage
    instance.extensionMessage = original
    assert instance.extensionMessage == original

@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::FileToFolder_strategy)
def test_becontent::filetofolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::HierarchicalPosition_strategy)
@settings(max_examples=50)
def test_becontent::hierarchicalposition_instantiation(instance):
    assert isinstance(instance, becontent::HierarchicalPosition)

@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_controlledField_type(instance):
    assert isinstance(instance.controlledField, str)


@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_controlledField_setter(instance):
    original = instance.controlledField
    instance.controlledField = original
    assert instance.controlledField == original

@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_referenceField_type(instance):
    assert isinstance(instance.referenceField, str)


@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_referenceField_setter(instance):
    original = instance.referenceField
    instance.referenceField = original
    assert instance.referenceField == original

@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::HierarchicalPosition_strategy)
def test_becontent::hierarchicalposition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Image_strategy)
@settings(max_examples=50)
def test_becontent::image_instantiation(instance):
    assert isinstance(instance, becontent::Image)

@given(instance=becontent::Image_strategy)
def test_becontent::image_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Image_strategy)
def test_becontent::image_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Image_strategy)
def test_becontent::image_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Image_strategy)
def test_becontent::image_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Image_strategy)
def test_becontent::image_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Image_strategy)
def test_becontent::image_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Date_strategy)
@settings(max_examples=50)
def test_becontent::date_instantiation(instance):
    assert isinstance(instance, becontent::Date)

@given(instance=becontent::Date_strategy)
def test_becontent::date_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Date_strategy)
def test_becontent::date_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Date_strategy)
def test_becontent::date_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Date_strategy)
def test_becontent::date_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Date_strategy)
def test_becontent::date_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Date_strategy)
def test_becontent::date_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Color_strategy)
@settings(max_examples=50)
def test_becontent::color_instantiation(instance):
    assert isinstance(instance, becontent::Color)

@given(instance=becontent::Color_strategy)
def test_becontent::color_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Color_strategy)
def test_becontent::color_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Color_strategy)
def test_becontent::color_defaultColor_type(instance):
    assert isinstance(instance.defaultColor, str)


@given(instance=becontent::Color_strategy)
def test_becontent::color_defaultColor_setter(instance):
    original = instance.defaultColor
    instance.defaultColor = original
    assert instance.defaultColor == original

@given(instance=becontent::Color_strategy)
def test_becontent::color_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Color_strategy)
def test_becontent::color_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Editor_strategy)
@settings(max_examples=50)
def test_becontent::editor_instantiation(instance):
    assert isinstance(instance, becontent::Editor)

@given(instance=becontent::Editor_strategy)
def test_becontent::editor_rows_type(instance):
    assert isinstance(instance.rows, int)


@given(instance=becontent::Editor_strategy)
def test_becontent::editor_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=becontent::Editor_strategy)
def test_becontent::editor_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=becontent::Editor_strategy)
def test_becontent::editor_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=becontent::Editor_strategy)
def test_becontent::editor_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Editor_strategy)
def test_becontent::editor_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Editor_strategy)
def test_becontent::editor_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Editor_strategy)
def test_becontent::editor_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Editor_strategy)
def test_becontent::editor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Editor_strategy)
def test_becontent::editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Select_strategy)
@settings(max_examples=50)
def test_becontent::select_instantiation(instance):
    assert isinstance(instance, becontent::Select)

@given(instance=becontent::Select_strategy)
def test_becontent::select_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=becontent::Select_strategy)
def test_becontent::select_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent::Select_strategy)
def test_becontent::select_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Select_strategy)
def test_becontent::select_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Select_strategy)
def test_becontent::select_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Select_strategy)
def test_becontent::select_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Select_strategy)
def test_becontent::select_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Select_strategy)
def test_becontent::select_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Section_strategy)
@settings(max_examples=50)
def test_becontent::section_instantiation(instance):
    assert isinstance(instance, becontent::Section)

@given(instance=becontent::Section_strategy)
def test_becontent::section_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Section_strategy)
def test_becontent::section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Section_strategy)
def test_becontent::section_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=becontent::Section_strategy)
def test_becontent::section_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Form_strategy)
@settings(max_examples=50)
def test_form_instantiation(instance):
    assert isinstance(instance, Form)

@given(instance=becontent::ExtendedForm_strategy)
@settings(max_examples=50)
def test_becontent::extendedform_instantiation(instance):
    assert isinstance(instance, becontent::ExtendedForm)

@given(instance=becontent::ExtendedForm_strategy)
def test_becontent::extendedform_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=becontent::ExtendedForm_strategy)
def test_becontent::extendedform_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=becontent::Checkbox_strategy)
@settings(max_examples=50)
def test_becontent::checkbox_instantiation(instance):
    assert isinstance(instance, becontent::Checkbox)

@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_isChecked_type(instance):
    assert isinstance(instance.isChecked, bool)


@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_isChecked_setter(instance):
    original = instance.isChecked
    instance.isChecked = original
    assert instance.isChecked == original

@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=becontent::Checkbox_strategy)
def test_becontent::checkbox_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=becontent::RadioButton_strategy)
@settings(max_examples=50)
def test_becontent::radiobutton_instantiation(instance):
    assert isinstance(instance, becontent::RadioButton)

@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::RadioButton_strategy)
def test_becontent::radiobutton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Text_strategy)
@settings(max_examples=50)
def test_becontent::text_instantiation(instance):
    assert isinstance(instance, becontent::Text)

@given(instance=becontent::Text_strategy)
def test_becontent::text_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=becontent::Text_strategy)
def test_becontent::text_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=becontent::Text_strategy)
def test_becontent::text_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Text_strategy)
def test_becontent::text_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Text_strategy)
def test_becontent::text_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=becontent::Text_strategy)
def test_becontent::text_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent::Text_strategy)
def test_becontent::text_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::Text_strategy)
def test_becontent::text_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Text_strategy)
def test_becontent::text_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=becontent::Text_strategy)
def test_becontent::text_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=becontent::Validation_strategy)
@settings(max_examples=50)
def test_becontent::validation_instantiation(instance):
    assert isinstance(instance, becontent::Validation)

@given(instance=becontent::Validation_strategy)
def test_becontent::validation_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=becontent::Validation_strategy)
def test_becontent::validation_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=becontent::Validation_strategy)
def test_becontent::validation__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::Validation_strategy)
def test_becontent::validation__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::Validation_strategy)
def test_becontent::validation_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=becontent::Validation_strategy)
def test_becontent::validation_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=becontent::CustomPager_strategy)
@settings(max_examples=50)
def test_becontent::custompager_instantiation(instance):
    assert isinstance(instance, becontent::CustomPager)

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_filter_type(instance):
    assert isinstance(instance.filter, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=becontent::CustomPager_strategy)
def test_becontent::custompager_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=ApplyCommand_strategy)
@settings(max_examples=50)
def test_applycommand_instantiation(instance):
    assert isinstance(instance, ApplyCommand)

@given(instance=becontent::ApplyItem_strategy)
@settings(max_examples=50)
def test_becontent::applyitem_instantiation(instance):
    assert isinstance(instance, becontent::ApplyItem)

@given(instance=becontent::ApplyItem_strategy)
def test_becontent::applyitem_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=becontent::ApplyItem_strategy)
def test_becontent::applyitem_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=becontent::ApplyItem_strategy)
def test_becontent::applyitem_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=becontent::ApplyItem_strategy)
def test_becontent::applyitem_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=becontent::ApplyIndexed_strategy)
@settings(max_examples=50)
def test_becontent::applyindexed_instantiation(instance):
    assert isinstance(instance, becontent::ApplyIndexed)

@given(instance=becontent::Apply_strategy)
@settings(max_examples=50)
def test_becontent::apply_instantiation(instance):
    assert isinstance(instance, becontent::Apply)

@given(instance=becontent::Apply_strategy)
def test_becontent::apply_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=becontent::Apply_strategy)
def test_becontent::apply_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=FormElement_strategy)
@settings(max_examples=50)
def test_formelement_instantiation(instance):
    assert isinstance(instance, FormElement)

@given(instance=becontent::NotStructuredElement_strategy)
@settings(max_examples=50)
def test_becontent::notstructuredelement_instantiation(instance):
    assert isinstance(instance, becontent::NotStructuredElement)

@given(instance=becontent::NotStructuredElement_strategy)
def test_becontent::notstructuredelement_helper_type(instance):
    assert isinstance(instance.helper, str)


@given(instance=becontent::NotStructuredElement_strategy)
def test_becontent::notstructuredelement_helper_setter(instance):
    original = instance.helper
    instance.helper = original
    assert instance.helper == original

@given(instance=becontent::Form_strategy)
@settings(max_examples=50)
def test_becontent::form_instantiation(instance):
    assert isinstance(instance, becontent::Form)

@given(instance=becontent::Form_strategy)
def test_becontent::form_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Form_strategy)
def test_becontent::form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Form_strategy)
def test_becontent::form_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=becontent::Form_strategy)
def test_becontent::form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=becontent::Form_strategy)
def test_becontent::form_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=becontent::Form_strategy)
def test_becontent::form_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=becontent::FormElement_strategy)
@settings(max_examples=50)
def test_becontent::formelement_instantiation(instance):
    assert isinstance(instance, becontent::FormElement)

@given(instance=becontent::ConditionalTemplate_strategy)
@settings(max_examples=50)
def test_becontent::conditionaltemplate_instantiation(instance):
    assert isinstance(instance, becontent::ConditionalTemplate)

@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_conditionExp_type(instance):
    assert isinstance(instance.conditionExp, str)


@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_conditionExp_setter(instance):
    original = instance.conditionExp
    instance.conditionExp = original
    assert instance.conditionExp == original

@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_falseTemplate_type(instance):
    assert isinstance(instance.falseTemplate, str)


@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_falseTemplate_setter(instance):
    original = instance.falseTemplate
    instance.falseTemplate = original
    assert instance.falseTemplate == original

@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_trueTemplate_type(instance):
    assert isinstance(instance.trueTemplate, str)


@given(instance=becontent::ConditionalTemplate_strategy)
def test_becontent::conditionaltemplate_trueTemplate_setter(instance):
    original = instance.trueTemplate
    instance.trueTemplate = original
    assert instance.trueTemplate == original

@given(instance=becontent::ContentCommand_strategy)
@settings(max_examples=50)
def test_becontent::contentcommand_instantiation(instance):
    assert isinstance(instance, becontent::ContentCommand)

@given(instance=becontent::ContentCommand_strategy)
def test_becontent::contentcommand__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::ContentCommand_strategy)
def test_becontent::contentcommand__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::JoinEntity_strategy)
@settings(max_examples=50)
def test_becontent::joinentity_instantiation(instance):
    assert isinstance(instance, becontent::JoinEntity)

@given(instance=becontent::JoinEntity_strategy)
def test_becontent::joinentity__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::JoinEntity_strategy)
def test_becontent::joinentity__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=ContentCommand_strategy)
@settings(max_examples=50)
def test_contentcommand_instantiation(instance):
    assert isinstance(instance, ContentCommand)

@given(instance=becontent::UnsetParameter_strategy)
@settings(max_examples=50)
def test_becontent::unsetparameter_instantiation(instance):
    assert isinstance(instance, becontent::UnsetParameter)

@given(instance=becontent::UnsetParameter_strategy)
def test_becontent::unsetparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::UnsetParameter_strategy)
def test_becontent::unsetparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Trigger_strategy)
@settings(max_examples=50)
def test_becontent::trigger_instantiation(instance):
    assert isinstance(instance, becontent::Trigger)

@given(instance=becontent::Trigger_strategy)
def test_becontent::trigger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=becontent::Trigger_strategy)
def test_becontent::trigger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=becontent::Trigger_strategy)
def test_becontent::trigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Trigger_strategy)
def test_becontent::trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Copy_strategy)
@settings(max_examples=50)
def test_becontent::copy_instantiation(instance):
    assert isinstance(instance, becontent::Copy)

@given(instance=becontent::Copy_strategy)
def test_becontent::copy_fieldName1_type(instance):
    assert isinstance(instance.fieldName1, str)


@given(instance=becontent::Copy_strategy)
def test_becontent::copy_fieldName1_setter(instance):
    original = instance.fieldName1
    instance.fieldName1 = original
    assert instance.fieldName1 == original

@given(instance=becontent::Copy_strategy)
def test_becontent::copy_fieldName2_type(instance):
    assert isinstance(instance.fieldName2, str)


@given(instance=becontent::Copy_strategy)
def test_becontent::copy_fieldName2_setter(instance):
    original = instance.fieldName2
    instance.fieldName2 = original
    assert instance.fieldName2 == original

@given(instance=becontent::ApplyCommand_strategy)
@settings(max_examples=50)
def test_becontent::applycommand_instantiation(instance):
    assert isinstance(instance, becontent::ApplyCommand)

@given(instance=becontent::Propagate_strategy)
@settings(max_examples=50)
def test_becontent::propagate_instantiation(instance):
    assert isinstance(instance, becontent::Propagate)

@given(instance=becontent::Propagate_strategy)
def test_becontent::propagate_fieldName2_type(instance):
    assert isinstance(instance.fieldName2, str)


@given(instance=becontent::Propagate_strategy)
def test_becontent::propagate_fieldName2_setter(instance):
    original = instance.fieldName2
    instance.fieldName2 = original
    assert instance.fieldName2 == original

@given(instance=becontent::Propagate_strategy)
def test_becontent::propagate_fieldName1_type(instance):
    assert isinstance(instance.fieldName1, str)


@given(instance=becontent::Propagate_strategy)
def test_becontent::propagate_fieldName1_setter(instance):
    original = instance.fieldName1
    instance.fieldName1 = original
    assert instance.fieldName1 == original

@given(instance=becontent::Parameter_strategy)
@settings(max_examples=50)
def test_becontent::parameter_instantiation(instance):
    assert isinstance(instance, becontent::Parameter)

@given(instance=becontent::Parameter_strategy)
def test_becontent::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Parameter_strategy)
def test_becontent::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Parameter_strategy)
def test_becontent::parameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=becontent::Parameter_strategy)
def test_becontent::parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ViewItem_strategy)
@settings(max_examples=50)
def test_viewitem_instantiation(instance):
    assert isinstance(instance, ViewItem)

@given(instance=becontent::Template_strategy)
@settings(max_examples=50)
def test_becontent::template_instantiation(instance):
    assert isinstance(instance, becontent::Template)

@given(instance=becontent::Template_strategy)
def test_becontent::template__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::Template_strategy)
def test_becontent::template__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::Template_strategy)
def test_becontent::template_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=becontent::Template_strategy)
def test_becontent::template_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=becontent::Skin_strategy)
@settings(max_examples=50)
def test_becontent::skin_instantiation(instance):
    assert isinstance(instance, becontent::Skin)

@given(instance=becontent::Skin_strategy)
def test_becontent::skin_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Skin_strategy)
def test_becontent::skin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::ViewItem_strategy)
@settings(max_examples=50)
def test_becontent::viewitem_instantiation(instance):
    assert isinstance(instance, becontent::ViewItem)

@given(instance=becontent::Content_strategy)
@settings(max_examples=50)
def test_becontent::content_instantiation(instance):
    assert isinstance(instance, becontent::Content)

@given(instance=becontent::Content_strategy)
def test_becontent::content_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_limit_type(instance):
    assert isinstance(instance.limit, int)


@given(instance=becontent::Content_strategy)
def test_becontent::content_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_presentationFields_type(instance):
    assert isinstance(instance.presentationFields, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_presentationFields_setter(instance):
    original = instance.presentationFields
    instance.presentationFields = original
    assert instance.presentationFields == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_orderFields_type(instance):
    assert isinstance(instance.orderFields, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_orderFields_setter(instance):
    original = instance.orderFields
    instance.orderFields = original
    assert instance.orderFields == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_joinCondition_type(instance):
    assert isinstance(instance.joinCondition, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_joinCondition_setter(instance):
    original = instance.joinCondition
    instance.joinCondition = original
    assert instance.joinCondition == original

@given(instance=becontent::Content_strategy)
def test_becontent::content_filter_type(instance):
    assert isinstance(instance.filter, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=becontent::Content_strategy)
def test_becontent::content__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::Content_strategy)
def test_becontent::content__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::Skinlet_strategy)
@settings(max_examples=50)
def test_becontent::skinlet_instantiation(instance):
    assert isinstance(instance, becontent::Skinlet)

@given(instance=becontent::Skinlet_strategy)
def test_becontent::skinlet__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::Skinlet_strategy)
def test_becontent::skinlet__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::Skinlet_strategy)
def test_becontent::skinlet_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=becontent::Skinlet_strategy)
def test_becontent::skinlet_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=TypedSystemAttribute_strategy)
@settings(max_examples=50)
def test_typedsystemattribute_instantiation(instance):
    assert isinstance(instance, TypedSystemAttribute)

@given(instance=becontent::SystemAttributePosition_strategy)
@settings(max_examples=50)
def test_becontent::systemattributeposition_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributePosition)

@given(instance=becontent::SystemAttributeLongDate_strategy)
@settings(max_examples=50)
def test_becontent::systemattributelongdate_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeLongDate)

@given(instance=becontent::SystemAttributeText_strategy)
@settings(max_examples=50)
def test_becontent::systemattributetext_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeText)

@given(instance=becontent::SystemAttributePassword_strategy)
@settings(max_examples=50)
def test_becontent::systemattributepassword_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributePassword)

@given(instance=becontent::SystemAttributeDate_strategy)
@settings(max_examples=50)
def test_becontent::systemattributedate_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeDate)

@given(instance=becontent::SystemAttributeColor_strategy)
@settings(max_examples=50)
def test_becontent::systemattributecolor_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeColor)

@given(instance=SystemEntityField_strategy)
@settings(max_examples=50)
def test_systementityfield_instantiation(instance):
    assert isinstance(instance, SystemEntityField)

@given(instance=becontent::TypedSystemAttribute_strategy)
@settings(max_examples=50)
def test_becontent::typedsystemattribute_instantiation(instance):
    assert isinstance(instance, becontent::TypedSystemAttribute)

@given(instance=becontent::TypedSystemAttribute_strategy)
def test_becontent::typedsystemattribute_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::TypedSystemAttribute_strategy)
def test_becontent::typedsystemattribute_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::TypedSystemAttribute_strategy)
def test_becontent::typedsystemattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::TypedSystemAttribute_strategy)
def test_becontent::typedsystemattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::SystemReference_strategy)
@settings(max_examples=50)
def test_becontent::systemreference_instantiation(instance):
    assert isinstance(instance, becontent::SystemReference)

@given(instance=becontent::SystemReference_strategy)
def test_becontent::systemreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::SystemReference_strategy)
def test_becontent::systemreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::SystemAttributeFileToFolder_strategy)
@settings(max_examples=50)
def test_becontent::systemattributefiletofolder_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeFileToFolder)

@given(instance=becontent::SystemAttributeFile_strategy)
@settings(max_examples=50)
def test_becontent::systemattributefile_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeFile)

@given(instance=becontent::SystemAttributeVarchar_strategy)
@settings(max_examples=50)
def test_becontent::systemattributevarchar_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeVarchar)

@given(instance=becontent::SystemAttributeVarchar_strategy)
def test_becontent::systemattributevarchar_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=becontent::SystemAttributeVarchar_strategy)
def test_becontent::systemattributevarchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=becontent::SystemAttributeVarchar_strategy)
def test_becontent::systemattributevarchar_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=becontent::SystemAttributeVarchar_strategy)
def test_becontent::systemattributevarchar_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent::SystemAttributeInteger_strategy)
@settings(max_examples=50)
def test_becontent::systemattributeinteger_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeInteger)

@given(instance=becontent::SystemAttributeInteger_strategy)
def test_becontent::systemattributeinteger_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=becontent::SystemAttributeInteger_strategy)
def test_becontent::systemattributeinteger_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent::SystemAttributeImage_strategy)
@settings(max_examples=50)
def test_becontent::systemattributeimage_instantiation(instance):
    assert isinstance(instance, becontent::SystemAttributeImage)

@given(instance=TypedAttribute_strategy)
@settings(max_examples=50)
def test_typedattribute_instantiation(instance):
    assert isinstance(instance, TypedAttribute)

@given(instance=becontent::AttributeFileToFolder_strategy)
@settings(max_examples=50)
def test_becontent::attributefiletofolder_instantiation(instance):
    assert isinstance(instance, becontent::AttributeFileToFolder)

@given(instance=becontent::AttributeColor_strategy)
@settings(max_examples=50)
def test_becontent::attributecolor_instantiation(instance):
    assert isinstance(instance, becontent::AttributeColor)

@given(instance=EntityField_strategy)
@settings(max_examples=50)
def test_entityfield_instantiation(instance):
    assert isinstance(instance, EntityField)

@given(instance=becontent::TypedAttribute_strategy)
@settings(max_examples=50)
def test_becontent::typedattribute_instantiation(instance):
    assert isinstance(instance, becontent::TypedAttribute)

@given(instance=becontent::TypedAttribute_strategy)
def test_becontent::typedattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::TypedAttribute_strategy)
def test_becontent::typedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::TypedAttribute_strategy)
def test_becontent::typedattribute_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=becontent::TypedAttribute_strategy)
def test_becontent::typedattribute_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent::Reference_strategy)
@settings(max_examples=50)
def test_becontent::reference_instantiation(instance):
    assert isinstance(instance, becontent::Reference)

@given(instance=becontent::Reference_strategy)
def test_becontent::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Reference_strategy)
def test_becontent::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::AttributeFile_strategy)
@settings(max_examples=50)
def test_becontent::attributefile_instantiation(instance):
    assert isinstance(instance, becontent::AttributeFile)

@given(instance=becontent::AttributeVarchar_strategy)
@settings(max_examples=50)
def test_becontent::attributevarchar_instantiation(instance):
    assert isinstance(instance, becontent::AttributeVarchar)

@given(instance=becontent::AttributeVarchar_strategy)
def test_becontent::attributevarchar_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=becontent::AttributeVarchar_strategy)
def test_becontent::attributevarchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=becontent::AttributeVarchar_strategy)
def test_becontent::attributevarchar_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=becontent::AttributeVarchar_strategy)
def test_becontent::attributevarchar_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent::AttributeInteger_strategy)
@settings(max_examples=50)
def test_becontent::attributeinteger_instantiation(instance):
    assert isinstance(instance, becontent::AttributeInteger)

@given(instance=becontent::AttributeInteger_strategy)
def test_becontent::attributeinteger_isPrimaryKey_type(instance):
    assert isinstance(instance.isPrimaryKey, bool)


@given(instance=becontent::AttributeInteger_strategy)
def test_becontent::attributeinteger_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent::AttributeImage_strategy)
@settings(max_examples=50)
def test_becontent::attributeimage_instantiation(instance):
    assert isinstance(instance, becontent::AttributeImage)

@given(instance=becontent::AttributePosition_strategy)
@settings(max_examples=50)
def test_becontent::attributeposition_instantiation(instance):
    assert isinstance(instance, becontent::AttributePosition)

@given(instance=becontent::AttributePassword_strategy)
@settings(max_examples=50)
def test_becontent::attributepassword_instantiation(instance):
    assert isinstance(instance, becontent::AttributePassword)

@given(instance=becontent::AttributeText_strategy)
@settings(max_examples=50)
def test_becontent::attributetext_instantiation(instance):
    assert isinstance(instance, becontent::AttributeText)

@given(instance=becontent::AttributeLongDate_strategy)
@settings(max_examples=50)
def test_becontent::attributelongdate_instantiation(instance):
    assert isinstance(instance, becontent::AttributeLongDate)

@given(instance=becontent::AttributeDate_strategy)
@settings(max_examples=50)
def test_becontent::attributedate_instantiation(instance):
    assert isinstance(instance, becontent::AttributeDate)

@given(instance=becontent::EntityField_strategy)
@settings(max_examples=50)
def test_becontent::entityfield_instantiation(instance):
    assert isinstance(instance, becontent::EntityField)

@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isSearchPresentationHead_type(instance):
    assert isinstance(instance.isSearchPresentationHead, bool)


@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isSearchPresentationHead_setter(instance):
    original = instance.isSearchPresentationHead
    instance.isSearchPresentationHead = original
    assert instance.isSearchPresentationHead == original

@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isSearchPresentationBody_type(instance):
    assert isinstance(instance.isSearchPresentationBody, bool)


@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isSearchPresentationBody_setter(instance):
    original = instance.isSearchPresentationBody
    instance.isSearchPresentationBody = original
    assert instance.isSearchPresentationBody == original

@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isPresented_type(instance):
    assert isinstance(instance.isPresented, bool)


@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isPresented_setter(instance):
    original = instance.isPresented
    instance.isPresented = original
    assert instance.isPresented == original

@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isTextSearch_type(instance):
    assert isinstance(instance.isTextSearch, bool)


@given(instance=becontent::EntityField_strategy)
def test_becontent::entityfield_isTextSearch_setter(instance):
    original = instance.isTextSearch
    instance.isTextSearch = original
    assert instance.isTextSearch == original

@given(instance=DefinitionItem_strategy)
@settings(max_examples=50)
def test_definitionitem_instantiation(instance):
    assert isinstance(instance, DefinitionItem)

@given(instance=becontent::Entity_strategy)
@settings(max_examples=50)
def test_becontent::entity_instantiation(instance):
    assert isinstance(instance, becontent::Entity)

@given(instance=becontent::Entity_strategy)
def test_becontent::entity_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=becontent::Entity_strategy)
def test_becontent::entity_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=becontent::Entity_strategy)
def test_becontent::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Entity_strategy)
def test_becontent::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Entity_strategy)
def test_becontent::entity_presentationString_type(instance):
    assert isinstance(instance.presentationString, str)


@given(instance=becontent::Entity_strategy)
def test_becontent::entity_presentationString_setter(instance):
    original = instance.presentationString
    instance.presentationString = original
    assert instance.presentationString == original

@given(instance=becontent::Entity_strategy)
def test_becontent::entity_rssFilter_type(instance):
    assert isinstance(instance.rssFilter, str)


@given(instance=becontent::Entity_strategy)
def test_becontent::entity_rssFilter_setter(instance):
    original = instance.rssFilter
    instance.rssFilter = original
    assert instance.rssFilter == original

@given(instance=becontent::Entity_strategy)
def test_becontent::entity_isOwned_type(instance):
    assert isinstance(instance.isOwned, bool)


@given(instance=becontent::Entity_strategy)
def test_becontent::entity_isOwned_setter(instance):
    original = instance.isOwned
    instance.isOwned = original
    assert instance.isOwned == original

@given(instance=BeContentElement_strategy)
@settings(max_examples=50)
def test_becontentelement_instantiation(instance):
    assert isinstance(instance, BeContentElement)

@given(instance=becontent::Channel_strategy)
@settings(max_examples=50)
def test_becontent::channel_instantiation(instance):
    assert isinstance(instance, becontent::Channel)

@given(instance=becontent::Channel_strategy)
def test_becontent::channel__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::Channel_strategy)
def test_becontent::channel__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::Channel_strategy)
def test_becontent::channel_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=becontent::Channel_strategy)
def test_becontent::channel_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=becontent::FileToFolderExtension_strategy)
@settings(max_examples=50)
def test_becontent::filetofolderextension_instantiation(instance):
    assert isinstance(instance, becontent::FileToFolderExtension)

@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension__id_model_type(instance):
    assert isinstance(instance._id_model, str)


@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension_extensionValue_type(instance):
    assert isinstance(instance.extensionValue, str)


@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension_extensionValue_setter(instance):
    original = instance.extensionValue
    instance.extensionValue = original
    assert instance.extensionValue == original

@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension_extensionKey_type(instance):
    assert isinstance(instance.extensionKey, str)


@given(instance=becontent::FileToFolderExtension_strategy)
def test_becontent::filetofolderextension_extensionKey_setter(instance):
    original = instance.extensionKey
    instance.extensionKey = original
    assert instance.extensionKey == original

@given(instance=becontent::EntityManagerPage_strategy)
@settings(max_examples=50)
def test_becontent::entitymanagerpage_instantiation(instance):
    assert isinstance(instance, becontent::EntityManagerPage)

@given(instance=becontent::EntityManagerPage_strategy)
def test_becontent::entitymanagerpage_skin_type(instance):
    assert isinstance(instance.skin, str)


@given(instance=becontent::EntityManagerPage_strategy)
def test_becontent::entitymanagerpage_skin_setter(instance):
    original = instance.skin
    instance.skin = original
    assert instance.skin == original

@given(instance=becontent::EntityManagerPage_strategy)
def test_becontent::entitymanagerpage_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=becontent::EntityManagerPage_strategy)
def test_becontent::entitymanagerpage_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=becontent::DefinitionItem_strategy)
@settings(max_examples=50)
def test_becontent::definitionitem_instantiation(instance):
    assert isinstance(instance, becontent::DefinitionItem)

@given(instance=becontent::BeContentElement_strategy)
@settings(max_examples=50)
def test_becontent::becontentelement_instantiation(instance):
    assert isinstance(instance, becontent::BeContentElement)

@given(instance=becontent::BeContentModel_strategy)
@settings(max_examples=50)
def test_becontent::becontentmodel_instantiation(instance):
    assert isinstance(instance, becontent::BeContentModel)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=becontent::SystemRelation_strategy)
@settings(max_examples=50)
def test_becontent::systemrelation_instantiation(instance):
    assert isinstance(instance, becontent::SystemRelation)

@given(instance=becontent::CustomRelation_strategy)
@settings(max_examples=50)
def test_becontent::customrelation_instantiation(instance):
    assert isinstance(instance, becontent::CustomRelation)

@given(instance=becontent::Relation_strategy)
@settings(max_examples=50)
def test_becontent::relation_instantiation(instance):
    assert isinstance(instance, becontent::Relation)

@given(instance=becontent::Relation_strategy)
def test_becontent::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=becontent::Relation_strategy)
def test_becontent::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent::Relation_strategy)
def test_becontent::relation_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=becontent::Relation_strategy)
def test_becontent::relation_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=becontent::SystemEntityField_strategy)
@settings(max_examples=50)
def test_becontent::systementityfield_instantiation(instance):
    assert isinstance(instance, becontent::SystemEntityField)

@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isPresented_type(instance):
    assert isinstance(instance.isPresented, bool)


@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isPresented_setter(instance):
    original = instance.isPresented
    instance.isPresented = original
    assert instance.isPresented == original

@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isSearchPresentationBody_type(instance):
    assert isinstance(instance.isSearchPresentationBody, bool)


@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isSearchPresentationBody_setter(instance):
    original = instance.isSearchPresentationBody
    instance.isSearchPresentationBody = original
    assert instance.isSearchPresentationBody == original

@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isTextSearch_type(instance):
    assert isinstance(instance.isTextSearch, bool)


@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isTextSearch_setter(instance):
    original = instance.isTextSearch
    instance.isTextSearch = original
    assert instance.isTextSearch == original

@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isSearchPresentationHead_type(instance):
    assert isinstance(instance.isSearchPresentationHead, bool)


@given(instance=becontent::SystemEntityField_strategy)
def test_becontent::systementityfield_isSearchPresentationHead_setter(instance):
    original = instance.isSearchPresentationHead
    instance.isSearchPresentationHead = original
    assert instance.isSearchPresentationHead == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=becontent::SystemEntity_strategy)
@settings(max_examples=50)
def test_becontent::systementity_instantiation(instance):
    assert isinstance(instance, becontent::SystemEntity)

@given(instance=becontent::CustomEntity_strategy)
@settings(max_examples=50)
def test_becontent::customentity_instantiation(instance):
    assert isinstance(instance, becontent::CustomEntity)

@given(instance=becontent::Handler_strategy)
@settings(max_examples=50)
def test_becontent::handler_instantiation(instance):
    assert isinstance(instance, becontent::Handler)

@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinPlaceholder_type(instance):
    assert isinstance(instance.mainSkinPlaceholder, str)


@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinPlaceholder_setter(instance):
    original = instance.mainSkinPlaceholder
    instance.mainSkinPlaceholder = original
    assert instance.mainSkinPlaceholder == original

@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinWithPager_type(instance):
    assert isinstance(instance.mainSkinWithPager, bool)


@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinWithPager_setter(instance):
    original = instance.mainSkinWithPager
    instance.mainSkinWithPager = original
    assert instance.mainSkinWithPager == original

@given(instance=becontent::Handler_strategy)
def test_becontent::handler_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=becontent::Handler_strategy)
def test_becontent::handler_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinPagerLength_type(instance):
    assert isinstance(instance.mainSkinPagerLength, int)


@given(instance=becontent::Handler_strategy)
def test_becontent::handler_mainSkinPagerLength_setter(instance):
    original = instance.mainSkinPagerLength
    instance.mainSkinPagerLength = original
    assert instance.mainSkinPagerLength == original
