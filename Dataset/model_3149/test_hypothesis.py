import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RuntimeItemType,
    ccore::DBObject,
    ccore::View,
    ccore::ComposerLink,
    ccore::MenuGroup,
    ccore::MenuAction,
    ccore::ViewModel,
    ccore::ExtItem,
    ccore::ComputedString,
    ccore::EEnum,
    EEnum,
    ccore::GroupExtItem,
    EReference,
    ccore::EnumType,
    RuntimeItem,
    ccore::ModelController,
    ccore::InteractionController,
    ccore::Display,
    ccore::ExportedContent,
    BindingDesc,
    ccore::BindExt,
    ccore::UnresolvedAttributeType,
    LongAttribute,
    ccore::TimeAttribute,
    Attribute,
    ccore::DateAttribute,
    ccore::Enum,
    ccore::LinkType,
    ccore::DoubleAttribute,
    ccore::LongAttribute,
    ccore::UUIDAttribute,
    ccore::IntegerAttribute,
    ccore::BooleanAttribute,
    ccore::StringAttribute,
    ccore::ViewDescription,
    ccore::ViewLinkType,
    ccore::ViewItemType,
    ccore::GenInformation,
    ItemType,
    ccore::RuntimeItemType,
    ccore::MenuAbstract,
    ccore::Menu,
    ccore::ActionExtItemType,
    ccore::DynamicActions,
    EAttribute,
    ccore::Composer,
    ccore::Exporter,
    ccore::ContentItem,
    ccore::EStructuralFeature,
    EPackage,
    ccore::ComposerType,
    ccore::ExporterType,
    ccore::ContentItemType,
    DBObject,
    ENamedElement,
    ccore::Item,
    ccore::BindingDesc,
    ccore::EPackage,
    ccore::WCListener,
    TypeDefinition,
    ccore::ItemType,
    ccore::ExtentedType,
    ccore::EClass,
    ccore::GroupOfAttributes,
    ccore::UIValidator,
    ccore::Page,
    EClass,
    Item,
    ccore::RuntimeItem,
    ccore::Attribute,
    ccore::KeyDefinition,
    ccore::Field,
    ccore::Cadse,
    ccore::TypeDefinition,
    TWCommitKind,
    TWEvol,
    TWDestEvol,
    TWUpdateKind,
    PositionEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(RuntimeItemType)


def test_runtimeitemtype_constructor_exists():
    assert callable(RuntimeItemType.__init__)


def test_runtimeitemtype_constructor_args():
    sig = inspect.signature(RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::dbobject_is_not_abstract():
    assert not inspect.isabstract(ccore::DBObject)


def test_ccore::dbobject_constructor_exists():
    assert callable(ccore::DBObject.__init__)


def test_ccore::dbobject_constructor_args():
    sig = inspect.signature(ccore::DBObject.__init__)
    params = list(sig.parameters.keys())
    assert "uuid_lsb" in params, "Missing parameter 'uuid_lsb'"
    assert "objectId" in params, "Missing parameter 'objectId'"
    assert "uuid_msb" in params, "Missing parameter 'uuid_msb'"

def test_ccore::dbobject_has_uuid_lsb():
    assert hasattr(ccore::DBObject, "uuid_lsb")
    descriptor = None
    for klass in ccore::DBObject.__mro__:
        if "uuid_lsb" in klass.__dict__:
            descriptor = klass.__dict__["uuid_lsb"]
            break
    assert isinstance(descriptor, property)

def test_ccore::dbobject_has_objectId():
    assert hasattr(ccore::DBObject, "objectId")
    descriptor = None
    for klass in ccore::DBObject.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)

def test_ccore::dbobject_has_uuid_msb():
    assert hasattr(ccore::DBObject, "uuid_msb")
    descriptor = None
    for klass in ccore::DBObject.__mro__:
        if "uuid_msb" in klass.__dict__:
            descriptor = klass.__dict__["uuid_msb"]
            break
    assert isinstance(descriptor, property)



def test_ccore::view_is_not_abstract():
    assert not inspect.isabstract(ccore::View)


def test_ccore::view_constructor_exists():
    assert callable(ccore::View.__init__)


def test_ccore::view_constructor_args():
    sig = inspect.signature(ccore::View.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_ccore::view_has_icon():
    assert hasattr(ccore::View, "icon")
    descriptor = None
    for klass in ccore::View.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_ccore::composerlink_is_not_abstract():
    assert not inspect.isabstract(ccore::ComposerLink)


def test_ccore::composerlink_constructor_exists():
    assert callable(ccore::ComposerLink.__init__)


def test_ccore::composerlink_constructor_args():
    sig = inspect.signature(ccore::ComposerLink.__init__)
    params = list(sig.parameters.keys())



def test_ccore::menugroup_is_not_abstract():
    assert not inspect.isabstract(ccore::MenuGroup)


def test_ccore::menugroup_constructor_exists():
    assert callable(ccore::MenuGroup.__init__)


def test_ccore::menugroup_constructor_args():
    sig = inspect.signature(ccore::MenuGroup.__init__)
    params = list(sig.parameters.keys())



def test_ccore::menuaction_is_not_abstract():
    assert not inspect.isabstract(ccore::MenuAction)


def test_ccore::menuaction_constructor_exists():
    assert callable(ccore::MenuAction.__init__)


def test_ccore::menuaction_constructor_args():
    sig = inspect.signature(ccore::MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_ccore::viewmodel_is_not_abstract():
    assert not inspect.isabstract(ccore::ViewModel)


def test_ccore::viewmodel_constructor_exists():
    assert callable(ccore::ViewModel.__init__)


def test_ccore::viewmodel_constructor_args():
    sig = inspect.signature(ccore::ViewModel.__init__)
    params = list(sig.parameters.keys())



def test_ccore::extitem_is_not_abstract():
    assert not inspect.isabstract(ccore::ExtItem)


def test_ccore::extitem_constructor_exists():
    assert callable(ccore::ExtItem.__init__)


def test_ccore::extitem_constructor_args():
    sig = inspect.signature(ccore::ExtItem.__init__)
    params = list(sig.parameters.keys())



def test_ccore::computedstring_is_not_abstract():
    assert not inspect.isabstract(ccore::ComputedString)


def test_ccore::computedstring_constructor_exists():
    assert callable(ccore::ComputedString.__init__)


def test_ccore::computedstring_constructor_args():
    sig = inspect.signature(ccore::ComputedString.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_ccore::computedstring_has_expression():
    assert hasattr(ccore::ComputedString, "expression")
    descriptor = None
    for klass in ccore::ComputedString.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_ccore::eenum_is_not_abstract():
    assert not inspect.isabstract(ccore::EEnum)


def test_ccore::eenum_constructor_exists():
    assert callable(ccore::EEnum.__init__)


def test_ccore::eenum_constructor_args():
    sig = inspect.signature(ccore::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_eenum_is_not_abstract():
    assert not inspect.isabstract(EEnum)


def test_eenum_constructor_exists():
    assert callable(EEnum.__init__)


def test_eenum_constructor_args():
    sig = inspect.signature(EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ccore::groupextitem_is_not_abstract():
    assert not inspect.isabstract(ccore::GroupExtItem)


def test_ccore::groupextitem_constructor_exists():
    assert callable(ccore::GroupExtItem.__init__)


def test_ccore::groupextitem_constructor_args():
    sig = inspect.signature(ccore::GroupExtItem.__init__)
    params = list(sig.parameters.keys())



def test_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_ccore::enumtype_is_not_abstract():
    assert not inspect.isabstract(ccore::EnumType)


def test_ccore::enumtype_constructor_exists():
    assert callable(ccore::EnumType.__init__)


def test_ccore::enumtype_constructor_args():
    sig = inspect.signature(ccore::EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "javaClass" in params, "Missing parameter 'javaClass'"
    assert "mustBeGenerated" in params, "Missing parameter 'mustBeGenerated'"

def test_ccore::enumtype_has_values():
    assert hasattr(ccore::EnumType, "values")
    descriptor = None
    for klass in ccore::EnumType.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_ccore::enumtype_has_javaClass():
    assert hasattr(ccore::EnumType, "javaClass")
    descriptor = None
    for klass in ccore::EnumType.__mro__:
        if "javaClass" in klass.__dict__:
            descriptor = klass.__dict__["javaClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore::enumtype_has_mustBeGenerated():
    assert hasattr(ccore::EnumType, "mustBeGenerated")
    descriptor = None
    for klass in ccore::EnumType.__mro__:
        if "mustBeGenerated" in klass.__dict__:
            descriptor = klass.__dict__["mustBeGenerated"]
            break
    assert isinstance(descriptor, property)



def test_runtimeitem_is_not_abstract():
    assert not inspect.isabstract(RuntimeItem)


def test_runtimeitem_constructor_exists():
    assert callable(RuntimeItem.__init__)


def test_runtimeitem_constructor_args():
    sig = inspect.signature(RuntimeItem.__init__)
    params = list(sig.parameters.keys())



def test_ccore::modelcontroller_is_not_abstract():
    assert not inspect.isabstract(ccore::ModelController)


def test_ccore::modelcontroller_constructor_exists():
    assert callable(ccore::ModelController.__init__)


def test_ccore::modelcontroller_constructor_args():
    sig = inspect.signature(ccore::ModelController.__init__)
    params = list(sig.parameters.keys())



def test_ccore::interactioncontroller_is_not_abstract():
    assert not inspect.isabstract(ccore::InteractionController)


def test_ccore::interactioncontroller_constructor_exists():
    assert callable(ccore::InteractionController.__init__)


def test_ccore::interactioncontroller_constructor_args():
    sig = inspect.signature(ccore::InteractionController.__init__)
    params = list(sig.parameters.keys())



def test_ccore::display_is_not_abstract():
    assert not inspect.isabstract(ccore::Display)


def test_ccore::display_constructor_exists():
    assert callable(ccore::Display.__init__)


def test_ccore::display_constructor_args():
    sig = inspect.signature(ccore::Display.__init__)
    params = list(sig.parameters.keys())
    assert "extendsIC" in params, "Missing parameter 'extendsIC'"
    assert "extendsUI" in params, "Missing parameter 'extendsUI'"
    assert "extendsMC" in params, "Missing parameter 'extendsMC'"

def test_ccore::display_has_extendsIC():
    assert hasattr(ccore::Display, "extendsIC")
    descriptor = None
    for klass in ccore::Display.__mro__:
        if "extendsIC" in klass.__dict__:
            descriptor = klass.__dict__["extendsIC"]
            break
    assert isinstance(descriptor, property)

def test_ccore::display_has_extendsUI():
    assert hasattr(ccore::Display, "extendsUI")
    descriptor = None
    for klass in ccore::Display.__mro__:
        if "extendsUI" in klass.__dict__:
            descriptor = klass.__dict__["extendsUI"]
            break
    assert isinstance(descriptor, property)

def test_ccore::display_has_extendsMC():
    assert hasattr(ccore::Display, "extendsMC")
    descriptor = None
    for klass in ccore::Display.__mro__:
        if "extendsMC" in klass.__dict__:
            descriptor = klass.__dict__["extendsMC"]
            break
    assert isinstance(descriptor, property)



def test_ccore::exportedcontent_is_not_abstract():
    assert not inspect.isabstract(ccore::ExportedContent)


def test_ccore::exportedcontent_constructor_exists():
    assert callable(ccore::ExportedContent.__init__)


def test_ccore::exportedcontent_constructor_args():
    sig = inspect.signature(ccore::ExportedContent.__init__)
    params = list(sig.parameters.keys())



def test_bindingdesc_is_not_abstract():
    assert not inspect.isabstract(BindingDesc)


def test_bindingdesc_constructor_exists():
    assert callable(BindingDesc.__init__)


def test_bindingdesc_constructor_args():
    sig = inspect.signature(BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_ccore::bindext_is_not_abstract():
    assert not inspect.isabstract(ccore::BindExt)


def test_ccore::bindext_constructor_exists():
    assert callable(ccore::BindExt.__init__)


def test_ccore::bindext_constructor_args():
    sig = inspect.signature(ccore::BindExt.__init__)
    params = list(sig.parameters.keys())



def test_ccore::unresolvedattributetype_is_not_abstract():
    assert not inspect.isabstract(ccore::UnresolvedAttributeType)


def test_ccore::unresolvedattributetype_constructor_exists():
    assert callable(ccore::UnresolvedAttributeType.__init__)


def test_ccore::unresolvedattributetype_constructor_args():
    sig = inspect.signature(ccore::UnresolvedAttributeType.__init__)
    params = list(sig.parameters.keys())



def test_longattribute_is_not_abstract():
    assert not inspect.isabstract(LongAttribute)


def test_longattribute_constructor_exists():
    assert callable(LongAttribute.__init__)


def test_longattribute_constructor_args():
    sig = inspect.signature(LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::timeattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::TimeAttribute)


def test_ccore::timeattribute_constructor_exists():
    assert callable(ccore::TimeAttribute.__init__)


def test_ccore::timeattribute_constructor_args():
    sig = inspect.signature(ccore::TimeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "initWithTheCurrentTime" in params, "Missing parameter 'initWithTheCurrentTime'"

def test_ccore::timeattribute_has_initWithTheCurrentTime():
    assert hasattr(ccore::TimeAttribute, "initWithTheCurrentTime")
    descriptor = None
    for klass in ccore::TimeAttribute.__mro__:
        if "initWithTheCurrentTime" in klass.__dict__:
            descriptor = klass.__dict__["initWithTheCurrentTime"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::dateattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::DateAttribute)


def test_ccore::dateattribute_constructor_exists():
    assert callable(ccore::DateAttribute.__init__)


def test_ccore::dateattribute_constructor_args():
    sig = inspect.signature(ccore::DateAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::enum_is_not_abstract():
    assert not inspect.isabstract(ccore::Enum)


def test_ccore::enum_constructor_exists():
    assert callable(ccore::Enum.__init__)


def test_ccore::enum_constructor_args():
    sig = inspect.signature(ccore::Enum.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "enumClazz" in params, "Missing parameter 'enumClazz'"

def test_ccore::enum_has_values():
    assert hasattr(ccore::Enum, "values")
    descriptor = None
    for klass in ccore::Enum.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_ccore::enum_has_enumClazz():
    assert hasattr(ccore::Enum, "enumClazz")
    descriptor = None
    for klass in ccore::Enum.__mro__:
        if "enumClazz" in klass.__dict__:
            descriptor = klass.__dict__["enumClazz"]
            break
    assert isinstance(descriptor, property)



def test_ccore::linktype_is_not_abstract():
    assert not inspect.isabstract(ccore::LinkType)


def test_ccore::linktype_constructor_exists():
    assert callable(ccore::LinkType.__init__)


def test_ccore::linktype_constructor_args():
    sig = inspect.signature(ccore::LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "composition" in params, "Missing parameter 'composition'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "twCoupled" in params, "Missing parameter 'twCoupled'"
    assert "max" in params, "Missing parameter 'max'"
    assert "mapping" in params, "Missing parameter 'mapping'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "linkManager" in params, "Missing parameter 'linkManager'"
    assert "min" in params, "Missing parameter 'min'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "annotation" in params, "Missing parameter 'annotation'"
    assert "group" in params, "Missing parameter 'group'"
    assert "twDestEvol" in params, "Missing parameter 'twDestEvol'"

def test_ccore::linktype_has_aggregation():
    assert hasattr(ccore::LinkType, "aggregation")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_composition():
    assert hasattr(ccore::LinkType, "composition")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "composition" in klass.__dict__:
            descriptor = klass.__dict__["composition"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_kind():
    assert hasattr(ccore::LinkType, "kind")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_twCoupled():
    assert hasattr(ccore::LinkType, "twCoupled")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "twCoupled" in klass.__dict__:
            descriptor = klass.__dict__["twCoupled"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_max():
    assert hasattr(ccore::LinkType, "max")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_mapping():
    assert hasattr(ccore::LinkType, "mapping")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "mapping" in klass.__dict__:
            descriptor = klass.__dict__["mapping"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_hidden():
    assert hasattr(ccore::LinkType, "hidden")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_linkManager():
    assert hasattr(ccore::LinkType, "linkManager")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "linkManager" in klass.__dict__:
            descriptor = klass.__dict__["linkManager"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_min():
    assert hasattr(ccore::LinkType, "min")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_selection():
    assert hasattr(ccore::LinkType, "selection")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_annotation():
    assert hasattr(ccore::LinkType, "annotation")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_group():
    assert hasattr(ccore::LinkType, "group")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_ccore::linktype_has_twDestEvol():
    assert hasattr(ccore::LinkType, "twDestEvol")
    descriptor = None
    for klass in ccore::LinkType.__mro__:
        if "twDestEvol" in klass.__dict__:
            descriptor = klass.__dict__["twDestEvol"]
            break
    assert isinstance(descriptor, property)



def test_ccore::doubleattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::DoubleAttribute)


def test_ccore::doubleattribute_constructor_exists():
    assert callable(ccore::DoubleAttribute.__init__)


def test_ccore::doubleattribute_constructor_args():
    sig = inspect.signature(ccore::DoubleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::longattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::LongAttribute)


def test_ccore::longattribute_constructor_exists():
    assert callable(ccore::LongAttribute.__init__)


def test_ccore::longattribute_constructor_args():
    sig = inspect.signature(ccore::LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::uuidattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::UUIDAttribute)


def test_ccore::uuidattribute_constructor_exists():
    assert callable(ccore::UUIDAttribute.__init__)


def test_ccore::uuidattribute_constructor_args():
    sig = inspect.signature(ccore::UUIDAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::integerattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::IntegerAttribute)


def test_ccore::integerattribute_constructor_exists():
    assert callable(ccore::IntegerAttribute.__init__)


def test_ccore::integerattribute_constructor_args():
    sig = inspect.signature(ccore::IntegerAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::booleanattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::BooleanAttribute)


def test_ccore::booleanattribute_constructor_exists():
    assert callable(ccore::BooleanAttribute.__init__)


def test_ccore::booleanattribute_constructor_args():
    sig = inspect.signature(ccore::BooleanAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::stringattribute_is_not_abstract():
    assert not inspect.isabstract(ccore::StringAttribute)


def test_ccore::stringattribute_constructor_exists():
    assert callable(ccore::StringAttribute.__init__)


def test_ccore::stringattribute_constructor_args():
    sig = inspect.signature(ccore::StringAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "notEmpty" in params, "Missing parameter 'notEmpty'"

def test_ccore::stringattribute_has_notEmpty():
    assert hasattr(ccore::StringAttribute, "notEmpty")
    descriptor = None
    for klass in ccore::StringAttribute.__mro__:
        if "notEmpty" in klass.__dict__:
            descriptor = klass.__dict__["notEmpty"]
            break
    assert isinstance(descriptor, property)



def test_ccore::viewdescription_is_not_abstract():
    assert not inspect.isabstract(ccore::ViewDescription)


def test_ccore::viewdescription_constructor_exists():
    assert callable(ccore::ViewDescription.__init__)


def test_ccore::viewdescription_constructor_args():
    sig = inspect.signature(ccore::ViewDescription.__init__)
    params = list(sig.parameters.keys())



def test_ccore::viewlinktype_is_not_abstract():
    assert not inspect.isabstract(ccore::ViewLinkType)


def test_ccore::viewlinktype_constructor_exists():
    assert callable(ccore::ViewLinkType.__init__)


def test_ccore::viewlinktype_constructor_args():
    sig = inspect.signature(ccore::ViewLinkType.__init__)
    params = list(sig.parameters.keys())
    assert "displayCreate" in params, "Missing parameter 'displayCreate'"
    assert "canCreateLink" in params, "Missing parameter 'canCreateLink'"
    assert "canCreateItem" in params, "Missing parameter 'canCreateItem'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_ccore::viewlinktype_has_displayCreate():
    assert hasattr(ccore::ViewLinkType, "displayCreate")
    descriptor = None
    for klass in ccore::ViewLinkType.__mro__:
        if "displayCreate" in klass.__dict__:
            descriptor = klass.__dict__["displayCreate"]
            break
    assert isinstance(descriptor, property)

def test_ccore::viewlinktype_has_canCreateLink():
    assert hasattr(ccore::ViewLinkType, "canCreateLink")
    descriptor = None
    for klass in ccore::ViewLinkType.__mro__:
        if "canCreateLink" in klass.__dict__:
            descriptor = klass.__dict__["canCreateLink"]
            break
    assert isinstance(descriptor, property)

def test_ccore::viewlinktype_has_canCreateItem():
    assert hasattr(ccore::ViewLinkType, "canCreateItem")
    descriptor = None
    for klass in ccore::ViewLinkType.__mro__:
        if "canCreateItem" in klass.__dict__:
            descriptor = klass.__dict__["canCreateItem"]
            break
    assert isinstance(descriptor, property)

def test_ccore::viewlinktype_has_aggregation():
    assert hasattr(ccore::ViewLinkType, "aggregation")
    descriptor = None
    for klass in ccore::ViewLinkType.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



def test_ccore::viewitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore::ViewItemType)


def test_ccore::viewitemtype_constructor_exists():
    assert callable(ccore::ViewItemType.__init__)


def test_ccore::viewitemtype_constructor_args():
    sig = inspect.signature(ccore::ViewItemType.__init__)
    params = list(sig.parameters.keys())
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_ccore::viewitemtype_has_isRootElement():
    assert hasattr(ccore::ViewItemType, "isRootElement")
    descriptor = None
    for klass in ccore::ViewItemType.__mro__:
        if "isRootElement" in klass.__dict__:
            descriptor = klass.__dict__["isRootElement"]
            break
    assert isinstance(descriptor, property)

def test_ccore::viewitemtype_has_ref():
    assert hasattr(ccore::ViewItemType, "ref")
    descriptor = None
    for klass in ccore::ViewItemType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_ccore::geninformation_is_not_abstract():
    assert not inspect.isabstract(ccore::GenInformation)


def test_ccore::geninformation_constructor_exists():
    assert callable(ccore::GenInformation.__init__)


def test_ccore::geninformation_constructor_args():
    sig = inspect.signature(ccore::GenInformation.__init__)
    params = list(sig.parameters.keys())
    assert "cSTName" in params, "Missing parameter 'cSTName'"

def test_ccore::geninformation_has_cSTName():
    assert hasattr(ccore::GenInformation, "cSTName")
    descriptor = None
    for klass in ccore::GenInformation.__mro__:
        if "cSTName" in klass.__dict__:
            descriptor = klass.__dict__["cSTName"]
            break
    assert isinstance(descriptor, property)



def test_itemtype_is_not_abstract():
    assert not inspect.isabstract(ItemType)


def test_itemtype_constructor_exists():
    assert callable(ItemType.__init__)


def test_itemtype_constructor_args():
    sig = inspect.signature(ItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore::RuntimeItemType)


def test_ccore::runtimeitemtype_constructor_exists():
    assert callable(ccore::RuntimeItemType.__init__)


def test_ccore::runtimeitemtype_constructor_args():
    sig = inspect.signature(ccore::RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::menuabstract_is_not_abstract():
    assert not inspect.isabstract(ccore::MenuAbstract)


def test_ccore::menuabstract_constructor_exists():
    assert callable(ccore::MenuAbstract.__init__)


def test_ccore::menuabstract_constructor_args():
    sig = inspect.signature(ccore::MenuAbstract.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "path" in params, "Missing parameter 'path'"
    assert "icon" in params, "Missing parameter 'icon'"

def test_ccore::menuabstract_has_label():
    assert hasattr(ccore::MenuAbstract, "label")
    descriptor = None
    for klass in ccore::MenuAbstract.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ccore::menuabstract_has_path():
    assert hasattr(ccore::MenuAbstract, "path")
    descriptor = None
    for klass in ccore::MenuAbstract.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_ccore::menuabstract_has_icon():
    assert hasattr(ccore::MenuAbstract, "icon")
    descriptor = None
    for klass in ccore::MenuAbstract.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_ccore::menu_is_not_abstract():
    assert not inspect.isabstract(ccore::Menu)


def test_ccore::menu_constructor_exists():
    assert callable(ccore::Menu.__init__)


def test_ccore::menu_constructor_args():
    sig = inspect.signature(ccore::Menu.__init__)
    params = list(sig.parameters.keys())



def test_ccore::actionextitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore::ActionExtItemType)


def test_ccore::actionextitemtype_constructor_exists():
    assert callable(ccore::ActionExtItemType.__init__)


def test_ccore::actionextitemtype_constructor_args():
    sig = inspect.signature(ccore::ActionExtItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::dynamicactions_is_not_abstract():
    assert not inspect.isabstract(ccore::DynamicActions)


def test_ccore::dynamicactions_constructor_exists():
    assert callable(ccore::DynamicActions.__init__)


def test_ccore::dynamicactions_constructor_args():
    sig = inspect.signature(ccore::DynamicActions.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore::composer_is_not_abstract():
    assert not inspect.isabstract(ccore::Composer)


def test_ccore::composer_constructor_exists():
    assert callable(ccore::Composer.__init__)


def test_ccore::composer_constructor_args():
    sig = inspect.signature(ccore::Composer.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"

def test_ccore::composer_has_types():
    assert hasattr(ccore::Composer, "types")
    descriptor = None
    for klass in ccore::Composer.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_ccore::exporter_is_not_abstract():
    assert not inspect.isabstract(ccore::Exporter)


def test_ccore::exporter_constructor_exists():
    assert callable(ccore::Exporter.__init__)


def test_ccore::exporter_constructor_args():
    sig = inspect.signature(ccore::Exporter.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"

def test_ccore::exporter_has_types():
    assert hasattr(ccore::Exporter, "types")
    descriptor = None
    for klass in ccore::Exporter.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_ccore::contentitem_is_not_abstract():
    assert not inspect.isabstract(ccore::ContentItem)


def test_ccore::contentitem_constructor_exists():
    assert callable(ccore::ContentItem.__init__)


def test_ccore::contentitem_constructor_args():
    sig = inspect.signature(ccore::ContentItem.__init__)
    params = list(sig.parameters.keys())



def test_ccore::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ccore::EStructuralFeature)


def test_ccore::estructuralfeature_constructor_exists():
    assert callable(ccore::EStructuralFeature.__init__)


def test_ccore::estructuralfeature_constructor_args():
    sig = inspect.signature(ccore::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ccore::composertype_is_not_abstract():
    assert not inspect.isabstract(ccore::ComposerType)


def test_ccore::composertype_constructor_exists():
    assert callable(ccore::ComposerType.__init__)


def test_ccore::composertype_constructor_args():
    sig = inspect.signature(ccore::ComposerType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::exportertype_is_not_abstract():
    assert not inspect.isabstract(ccore::ExporterType)


def test_ccore::exportertype_constructor_exists():
    assert callable(ccore::ExporterType.__init__)


def test_ccore::exportertype_constructor_args():
    sig = inspect.signature(ccore::ExporterType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::contentitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore::ContentItemType)


def test_ccore::contentitemtype_constructor_exists():
    assert callable(ccore::ContentItemType.__init__)


def test_ccore::contentitemtype_constructor_args():
    sig = inspect.signature(ccore::ContentItemType.__init__)
    params = list(sig.parameters.keys())
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"

def test_ccore::contentitemtype_has_extendsClass():
    assert hasattr(ccore::ContentItemType, "extendsClass")
    descriptor = None
    for klass in ccore::ContentItemType.__mro__:
        if "extendsClass" in klass.__dict__:
            descriptor = klass.__dict__["extendsClass"]
            break
    assert isinstance(descriptor, property)



def test_dbobject_is_not_abstract():
    assert not inspect.isabstract(DBObject)


def test_dbobject_constructor_exists():
    assert callable(DBObject.__init__)


def test_dbobject_constructor_args():
    sig = inspect.signature(DBObject.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ccore::item_is_not_abstract():
    assert not inspect.isabstract(ccore::Item)


def test_ccore::item_constructor_exists():
    assert callable(ccore::Item.__init__)


def test_ccore::item_constructor_args():
    sig = inspect.signature(ccore::Item.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "twVersion" in params, "Missing parameter 'twVersion'"
    assert "committedBy" in params, "Missing parameter 'committedBy'"
    assert "itemHidden" in params, "Missing parameter 'itemHidden'"
    assert "twCommittedDate" in params, "Missing parameter 'twCommittedDate'"
    assert "twRequireNewRev" in params, "Missing parameter 'twRequireNewRev'"
    assert "itemReadonly" in params, "Missing parameter 'itemReadonly'"
    assert "twRevModified" in params, "Missing parameter 'twRevModified'"
    assert "isvalid" in params, "Missing parameter 'isvalid'"

def test_ccore::item_has_displayName():
    assert hasattr(ccore::Item, "displayName")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_qualifiedName():
    assert hasattr(ccore::Item, "qualifiedName")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_twVersion():
    assert hasattr(ccore::Item, "twVersion")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "twVersion" in klass.__dict__:
            descriptor = klass.__dict__["twVersion"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_committedBy():
    assert hasattr(ccore::Item, "committedBy")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "committedBy" in klass.__dict__:
            descriptor = klass.__dict__["committedBy"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_itemHidden():
    assert hasattr(ccore::Item, "itemHidden")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "itemHidden" in klass.__dict__:
            descriptor = klass.__dict__["itemHidden"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_twCommittedDate():
    assert hasattr(ccore::Item, "twCommittedDate")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "twCommittedDate" in klass.__dict__:
            descriptor = klass.__dict__["twCommittedDate"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_twRequireNewRev():
    assert hasattr(ccore::Item, "twRequireNewRev")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "twRequireNewRev" in klass.__dict__:
            descriptor = klass.__dict__["twRequireNewRev"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_itemReadonly():
    assert hasattr(ccore::Item, "itemReadonly")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "itemReadonly" in klass.__dict__:
            descriptor = klass.__dict__["itemReadonly"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_twRevModified():
    assert hasattr(ccore::Item, "twRevModified")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "twRevModified" in klass.__dict__:
            descriptor = klass.__dict__["twRevModified"]
            break
    assert isinstance(descriptor, property)

def test_ccore::item_has_isvalid():
    assert hasattr(ccore::Item, "isvalid")
    descriptor = None
    for klass in ccore::Item.__mro__:
        if "isvalid" in klass.__dict__:
            descriptor = klass.__dict__["isvalid"]
            break
    assert isinstance(descriptor, property)



def test_ccore::bindingdesc_is_not_abstract():
    assert not inspect.isabstract(ccore::BindingDesc)


def test_ccore::bindingdesc_constructor_exists():
    assert callable(ccore::BindingDesc.__init__)


def test_ccore::bindingdesc_constructor_args():
    sig = inspect.signature(ccore::BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_ccore::epackage_is_not_abstract():
    assert not inspect.isabstract(ccore::EPackage)


def test_ccore::epackage_constructor_exists():
    assert callable(ccore::EPackage.__init__)


def test_ccore::epackage_constructor_args():
    sig = inspect.signature(ccore::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ccore::wclistener_is_not_abstract():
    assert not inspect.isabstract(ccore::WCListener)


def test_ccore::wclistener_constructor_exists():
    assert callable(ccore::WCListener.__init__)


def test_ccore::wclistener_constructor_args():
    sig = inspect.signature(ccore::WCListener.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ccore::itemtype_is_not_abstract():
    assert not inspect.isabstract(ccore::ItemType)


def test_ccore::itemtype_constructor_exists():
    assert callable(ccore::ItemType.__init__)


def test_ccore::itemtype_constructor_args():
    sig = inspect.signature(ccore::ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "managerClass" in params, "Missing parameter 'managerClass'"
    assert "messageErrorId" in params, "Missing parameter 'messageErrorId'"
    assert "humanName" in params, "Missing parameter 'humanName'"
    assert "overwriteDefaultPages" in params, "Missing parameter 'overwriteDefaultPages'"
    assert "itemManagerClass" in params, "Missing parameter 'itemManagerClass'"
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "validateNameRe" in params, "Missing parameter 'validateNameRe'"
    assert "qualifiedNameTemplate" in params, "Missing parameter 'qualifiedNameTemplate'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "hasShortName" in params, "Missing parameter 'hasShortName'"
    assert "isMetaItemType" in params, "Missing parameter 'isMetaItemType'"
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"
    assert "hasContent" in params, "Missing parameter 'hasContent'"
    assert "itemFactoryClass" in params, "Missing parameter 'itemFactoryClass'"
    assert "displayNameTemplate" in params, "Missing parameter 'displayNameTemplate'"
    assert "hasUniqueName" in params, "Missing parameter 'hasUniqueName'"
    assert "isInstanceHidden" in params, "Missing parameter 'isInstanceHidden'"
    assert "isInstanceAbstract" in params, "Missing parameter 'isInstanceAbstract'"
    assert "customManager" in params, "Missing parameter 'customManager'"

def test_ccore::itemtype_has_managerClass():
    assert hasattr(ccore::ItemType, "managerClass")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "managerClass" in klass.__dict__:
            descriptor = klass.__dict__["managerClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_messageErrorId():
    assert hasattr(ccore::ItemType, "messageErrorId")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "messageErrorId" in klass.__dict__:
            descriptor = klass.__dict__["messageErrorId"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_humanName():
    assert hasattr(ccore::ItemType, "humanName")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "humanName" in klass.__dict__:
            descriptor = klass.__dict__["humanName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_overwriteDefaultPages():
    assert hasattr(ccore::ItemType, "overwriteDefaultPages")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "overwriteDefaultPages" in klass.__dict__:
            descriptor = klass.__dict__["overwriteDefaultPages"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_itemManagerClass():
    assert hasattr(ccore::ItemType, "itemManagerClass")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "itemManagerClass" in klass.__dict__:
            descriptor = klass.__dict__["itemManagerClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_packageName():
    assert hasattr(ccore::ItemType, "packageName")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_validateNameRe():
    assert hasattr(ccore::ItemType, "validateNameRe")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "validateNameRe" in klass.__dict__:
            descriptor = klass.__dict__["validateNameRe"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_qualifiedNameTemplate():
    assert hasattr(ccore::ItemType, "qualifiedNameTemplate")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "qualifiedNameTemplate" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedNameTemplate"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_icon():
    assert hasattr(ccore::ItemType, "icon")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_hasShortName():
    assert hasattr(ccore::ItemType, "hasShortName")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "hasShortName" in klass.__dict__:
            descriptor = klass.__dict__["hasShortName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_isMetaItemType():
    assert hasattr(ccore::ItemType, "isMetaItemType")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "isMetaItemType" in klass.__dict__:
            descriptor = klass.__dict__["isMetaItemType"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_isRootElement():
    assert hasattr(ccore::ItemType, "isRootElement")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "isRootElement" in klass.__dict__:
            descriptor = klass.__dict__["isRootElement"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_hasContent():
    assert hasattr(ccore::ItemType, "hasContent")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "hasContent" in klass.__dict__:
            descriptor = klass.__dict__["hasContent"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_itemFactoryClass():
    assert hasattr(ccore::ItemType, "itemFactoryClass")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "itemFactoryClass" in klass.__dict__:
            descriptor = klass.__dict__["itemFactoryClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_displayNameTemplate():
    assert hasattr(ccore::ItemType, "displayNameTemplate")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "displayNameTemplate" in klass.__dict__:
            descriptor = klass.__dict__["displayNameTemplate"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_hasUniqueName():
    assert hasattr(ccore::ItemType, "hasUniqueName")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "hasUniqueName" in klass.__dict__:
            descriptor = klass.__dict__["hasUniqueName"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_isInstanceHidden():
    assert hasattr(ccore::ItemType, "isInstanceHidden")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "isInstanceHidden" in klass.__dict__:
            descriptor = klass.__dict__["isInstanceHidden"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_isInstanceAbstract():
    assert hasattr(ccore::ItemType, "isInstanceAbstract")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "isInstanceAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isInstanceAbstract"]
            break
    assert isinstance(descriptor, property)

def test_ccore::itemtype_has_customManager():
    assert hasattr(ccore::ItemType, "customManager")
    descriptor = None
    for klass in ccore::ItemType.__mro__:
        if "customManager" in klass.__dict__:
            descriptor = klass.__dict__["customManager"]
            break
    assert isinstance(descriptor, property)



def test_ccore::extentedtype_is_not_abstract():
    assert not inspect.isabstract(ccore::ExtentedType)


def test_ccore::extentedtype_constructor_exists():
    assert callable(ccore::ExtentedType.__init__)


def test_ccore::extentedtype_constructor_args():
    sig = inspect.signature(ccore::ExtentedType.__init__)
    params = list(sig.parameters.keys())



def test_ccore::eclass_is_not_abstract():
    assert not inspect.isabstract(ccore::EClass)


def test_ccore::eclass_constructor_exists():
    assert callable(ccore::EClass.__init__)


def test_ccore::eclass_constructor_args():
    sig = inspect.signature(ccore::EClass.__init__)
    params = list(sig.parameters.keys())



def test_ccore::groupofattributes_is_not_abstract():
    assert not inspect.isabstract(ccore::GroupOfAttributes)


def test_ccore::groupofattributes_constructor_exists():
    assert callable(ccore::GroupOfAttributes.__init__)


def test_ccore::groupofattributes_constructor_args():
    sig = inspect.signature(ccore::GroupOfAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_ccore::groupofattributes_has_column():
    assert hasattr(ccore::GroupOfAttributes, "column")
    descriptor = None
    for klass in ccore::GroupOfAttributes.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_ccore::uivalidator_is_not_abstract():
    assert not inspect.isabstract(ccore::UIValidator)


def test_ccore::uivalidator_constructor_exists():
    assert callable(ccore::UIValidator.__init__)


def test_ccore::uivalidator_constructor_args():
    sig = inspect.signature(ccore::UIValidator.__init__)
    params = list(sig.parameters.keys())



def test_ccore::page_is_not_abstract():
    assert not inspect.isabstract(ccore::Page)


def test_ccore::page_constructor_exists():
    assert callable(ccore::Page.__init__)


def test_ccore::page_constructor_args():
    sig = inspect.signature(ccore::Page.__init__)
    params = list(sig.parameters.keys())
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "label" in params, "Missing parameter 'label'"

def test_ccore::page_has_idRuntime():
    assert hasattr(ccore::Page, "idRuntime")
    descriptor = None
    for klass in ccore::Page.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)

def test_ccore::page_has_description():
    assert hasattr(ccore::Page, "description")
    descriptor = None
    for klass in ccore::Page.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ccore::page_has_title():
    assert hasattr(ccore::Page, "title")
    descriptor = None
    for klass in ccore::Page.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_ccore::page_has_label():
    assert hasattr(ccore::Page, "label")
    descriptor = None
    for klass in ccore::Page.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_ccore::runtimeitem_is_not_abstract():
    assert not inspect.isabstract(ccore::RuntimeItem)


def test_ccore::runtimeitem_constructor_exists():
    assert callable(ccore::RuntimeItem.__init__)


def test_ccore::runtimeitem_constructor_args():
    sig = inspect.signature(ccore::RuntimeItem.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"

def test_ccore::runtimeitem_has_className():
    assert hasattr(ccore::RuntimeItem, "className")
    descriptor = None
    for klass in ccore::RuntimeItem.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_ccore::runtimeitem_has_extendsClass():
    assert hasattr(ccore::RuntimeItem, "extendsClass")
    descriptor = None
    for klass in ccore::RuntimeItem.__mro__:
        if "extendsClass" in klass.__dict__:
            descriptor = klass.__dict__["extendsClass"]
            break
    assert isinstance(descriptor, property)



def test_ccore::attribute_is_not_abstract():
    assert not inspect.isabstract(ccore::Attribute)


def test_ccore::attribute_constructor_exists():
    assert callable(ccore::Attribute.__init__)


def test_ccore::attribute_constructor_args():
    sig = inspect.signature(ccore::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "tWRevSpecific" in params, "Missing parameter 'tWRevSpecific'"
    assert "isList" in params, "Missing parameter 'isList'"
    assert "tWCommitKind" in params, "Missing parameter 'tWCommitKind'"
    assert "devGenerated" in params, "Missing parameter 'devGenerated'"
    assert "mustBeInitialized" in params, "Missing parameter 'mustBeInitialized'"
    assert "cannotBeUndefined" in params, "Missing parameter 'cannotBeUndefined'"
    assert "hiddenInComputedPages" in params, "Missing parameter 'hiddenInComputedPages'"
    assert "tWUpdateKind" in params, "Missing parameter 'tWUpdateKind'"
    assert "_final" in params, "Missing parameter '_final'"
    assert "require" in params, "Missing parameter 'require'"
    assert "natif" in params, "Missing parameter 'natif'"
    assert "tWEvol" in params, "Missing parameter 'tWEvol'"
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"

def test_ccore::attribute_has_tWRevSpecific():
    assert hasattr(ccore::Attribute, "tWRevSpecific")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "tWRevSpecific" in klass.__dict__:
            descriptor = klass.__dict__["tWRevSpecific"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_isList():
    assert hasattr(ccore::Attribute, "isList")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_tWCommitKind():
    assert hasattr(ccore::Attribute, "tWCommitKind")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "tWCommitKind" in klass.__dict__:
            descriptor = klass.__dict__["tWCommitKind"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_devGenerated():
    assert hasattr(ccore::Attribute, "devGenerated")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "devGenerated" in klass.__dict__:
            descriptor = klass.__dict__["devGenerated"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_mustBeInitialized():
    assert hasattr(ccore::Attribute, "mustBeInitialized")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "mustBeInitialized" in klass.__dict__:
            descriptor = klass.__dict__["mustBeInitialized"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_cannotBeUndefined():
    assert hasattr(ccore::Attribute, "cannotBeUndefined")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "cannotBeUndefined" in klass.__dict__:
            descriptor = klass.__dict__["cannotBeUndefined"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_hiddenInComputedPages():
    assert hasattr(ccore::Attribute, "hiddenInComputedPages")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "hiddenInComputedPages" in klass.__dict__:
            descriptor = klass.__dict__["hiddenInComputedPages"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_tWUpdateKind():
    assert hasattr(ccore::Attribute, "tWUpdateKind")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "tWUpdateKind" in klass.__dict__:
            descriptor = klass.__dict__["tWUpdateKind"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has__final():
    assert hasattr(ccore::Attribute, "_final")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "_final" in klass.__dict__:
            descriptor = klass.__dict__["_final"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_require():
    assert hasattr(ccore::Attribute, "require")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "require" in klass.__dict__:
            descriptor = klass.__dict__["require"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_natif():
    assert hasattr(ccore::Attribute, "natif")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "natif" in klass.__dict__:
            descriptor = klass.__dict__["natif"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_tWEvol():
    assert hasattr(ccore::Attribute, "tWEvol")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "tWEvol" in klass.__dict__:
            descriptor = klass.__dict__["tWEvol"]
            break
    assert isinstance(descriptor, property)

def test_ccore::attribute_has_idRuntime():
    assert hasattr(ccore::Attribute, "idRuntime")
    descriptor = None
    for klass in ccore::Attribute.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)



def test_ccore::keydefinition_is_not_abstract():
    assert not inspect.isabstract(ccore::KeyDefinition)


def test_ccore::keydefinition_constructor_exists():
    assert callable(ccore::KeyDefinition.__init__)


def test_ccore::keydefinition_constructor_args():
    sig = inspect.signature(ccore::KeyDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ccore::field_is_not_abstract():
    assert not inspect.isabstract(ccore::Field)


def test_ccore::field_constructor_exists():
    assert callable(ccore::Field.__init__)


def test_ccore::field_constructor_args():
    sig = inspect.signature(ccore::Field.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "label" in params, "Missing parameter 'label'"
    assert "editable" in params, "Missing parameter 'editable'"

def test_ccore::field_has_position():
    assert hasattr(ccore::Field, "position")
    descriptor = None
    for klass in ccore::Field.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_ccore::field_has_label():
    assert hasattr(ccore::Field, "label")
    descriptor = None
    for klass in ccore::Field.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ccore::field_has_editable():
    assert hasattr(ccore::Field, "editable")
    descriptor = None
    for klass in ccore::Field.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)



def test_ccore::cadse_is_not_abstract():
    assert not inspect.isabstract(ccore::Cadse)


def test_ccore::cadse_constructor_exists():
    assert callable(ccore::Cadse.__init__)


def test_ccore::cadse_constructor_args():
    sig = inspect.signature(ccore::Cadse.__init__)
    params = list(sig.parameters.keys())
    assert "itemRepoURL" in params, "Missing parameter 'itemRepoURL'"
    assert "description" in params, "Missing parameter 'description'"
    assert "defaultContentRepoURL" in params, "Missing parameter 'defaultContentRepoURL'"
    assert "itemRepoPasswd" in params, "Missing parameter 'itemRepoPasswd'"
    assert "itemRepoLogin" in params, "Missing parameter 'itemRepoLogin'"
    assert "executed" in params, "Missing parameter 'executed'"
    assert "idDefinition" in params, "Missing parameter 'idDefinition'"

def test_ccore::cadse_has_itemRepoURL():
    assert hasattr(ccore::Cadse, "itemRepoURL")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "itemRepoURL" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoURL"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_description():
    assert hasattr(ccore::Cadse, "description")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_defaultContentRepoURL():
    assert hasattr(ccore::Cadse, "defaultContentRepoURL")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "defaultContentRepoURL" in klass.__dict__:
            descriptor = klass.__dict__["defaultContentRepoURL"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_itemRepoPasswd():
    assert hasattr(ccore::Cadse, "itemRepoPasswd")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "itemRepoPasswd" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoPasswd"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_itemRepoLogin():
    assert hasattr(ccore::Cadse, "itemRepoLogin")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "itemRepoLogin" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoLogin"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_executed():
    assert hasattr(ccore::Cadse, "executed")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "executed" in klass.__dict__:
            descriptor = klass.__dict__["executed"]
            break
    assert isinstance(descriptor, property)

def test_ccore::cadse_has_idDefinition():
    assert hasattr(ccore::Cadse, "idDefinition")
    descriptor = None
    for klass in ccore::Cadse.__mro__:
        if "idDefinition" in klass.__dict__:
            descriptor = klass.__dict__["idDefinition"]
            break
    assert isinstance(descriptor, property)



def test_ccore::typedefinition_is_not_abstract():
    assert not inspect.isabstract(ccore::TypeDefinition)


def test_ccore::typedefinition_constructor_exists():
    assert callable(ccore::TypeDefinition.__init__)


def test_ccore::typedefinition_constructor_args():
    sig = inspect.signature(ccore::TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"

def test_ccore::typedefinition_has_idRuntime():
    assert hasattr(ccore::TypeDefinition, "idRuntime")
    descriptor = None
    for klass in ccore::TypeDefinition.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)

def test_twcommitkind_exists():
    # Check that the Enumeration exists
    assert TWCommitKind is not None

def test_twcommitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWCommitKind]
    expected_literals = [
        "reconcile",
        "none",
        "conflict",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWCommitKind"

def test_twevol_exists():
    # Check that the Enumeration exists
    assert TWEvol is not None

def test_twevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWEvol]
    expected_literals = [
        "twMutable",
        "twTransient",
        "twFinal",
        "twImmutable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWEvol"

def test_twdestevol_exists():
    # Check that the Enumeration exists
    assert TWDestEvol is not None

def test_twdestevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWDestEvol]
    expected_literals = [
        "effective",
        "immutable",
        "mutable",
        "branch",
        "finalDest",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWDestEvol"

def test_twupdatekind_exists():
    # Check that the Enumeration exists
    assert TWUpdateKind is not None

def test_twupdatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWUpdateKind]
    expected_literals = [
        "merge",
        "none",
        "compute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWUpdateKind"

def test_positionenum_exists():
    # Check that the Enumeration exists
    assert PositionEnum is not None

def test_positionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionEnum]
    expected_literals = [
        "group",
        "none",
        "right",
        "defaultpos",
        "left",
        "top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionEnum"


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
RuntimeItemType_strategy = st.builds(
    RuntimeItemType,
)
ccore::DBObject_strategy = st.builds(
    ccore::DBObject,
    uuid_lsb=
        safe_text,
    objectId=
        st.integers(),
    uuid_msb=
        safe_text
)
ccore::View_strategy = st.builds(
    ccore::View,
    icon=
        safe_text
)
ccore::ComposerLink_strategy = st.builds(
    ccore::ComposerLink,
)
ccore::MenuGroup_strategy = st.builds(
    ccore::MenuGroup,
)
ccore::MenuAction_strategy = st.builds(
    ccore::MenuAction,
)
ccore::ViewModel_strategy = st.builds(
    ccore::ViewModel,
)
ccore::ExtItem_strategy = st.builds(
    ccore::ExtItem,
)
ccore::ComputedString_strategy = st.builds(
    ccore::ComputedString,
    expression=
        safe_text
)
ccore::EEnum_strategy = st.builds(
    ccore::EEnum,
)
EEnum_strategy = st.builds(
    EEnum,
)
ccore::GroupExtItem_strategy = st.builds(
    ccore::GroupExtItem,
)
EReference_strategy = st.builds(
    EReference,
)
ccore::EnumType_strategy = st.builds(
    ccore::EnumType,
    values=
        safe_text,
    javaClass=
        safe_text,
    mustBeGenerated=
        st.booleans()
)
RuntimeItem_strategy = st.builds(
    RuntimeItem,
)
ccore::ModelController_strategy = st.builds(
    ccore::ModelController,
)
ccore::InteractionController_strategy = st.builds(
    ccore::InteractionController,
)
ccore::Display_strategy = st.builds(
    ccore::Display,
    extendsIC=
        st.booleans(),
    extendsUI=
        st.booleans(),
    extendsMC=
        st.booleans()
)
ccore::ExportedContent_strategy = st.builds(
    ccore::ExportedContent,
)
BindingDesc_strategy = st.builds(
    BindingDesc,
)
ccore::BindExt_strategy = st.builds(
    ccore::BindExt,
)
ccore::UnresolvedAttributeType_strategy = st.builds(
    ccore::UnresolvedAttributeType,
)
LongAttribute_strategy = st.builds(
    LongAttribute,
)
ccore::TimeAttribute_strategy = st.builds(
    ccore::TimeAttribute,
    initWithTheCurrentTime=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
ccore::DateAttribute_strategy = st.builds(
    ccore::DateAttribute,
)
ccore::Enum_strategy = st.builds(
    ccore::Enum,
    values=
        safe_text,
    enumClazz=
        safe_text
)
ccore::LinkType_strategy = st.builds(
    ccore::LinkType,
    aggregation=
        st.booleans(),
    composition=
        st.booleans(),
    kind=
        st.integers(),
    twCoupled=
        st.booleans(),
    max=
        st.integers(),
    mapping=
        st.booleans(),
    hidden=
        st.booleans(),
    linkManager=
        safe_text,
    min=
        st.integers(),
    selection=
        safe_text,
    annotation=
        st.booleans(),
    group=
        st.booleans(),
    twDestEvol=
        safe_text
)
ccore::DoubleAttribute_strategy = st.builds(
    ccore::DoubleAttribute,
)
ccore::LongAttribute_strategy = st.builds(
    ccore::LongAttribute,
)
ccore::UUIDAttribute_strategy = st.builds(
    ccore::UUIDAttribute,
)
ccore::IntegerAttribute_strategy = st.builds(
    ccore::IntegerAttribute,
)
ccore::BooleanAttribute_strategy = st.builds(
    ccore::BooleanAttribute,
)
ccore::StringAttribute_strategy = st.builds(
    ccore::StringAttribute,
    notEmpty=
        st.booleans()
)
ccore::ViewDescription_strategy = st.builds(
    ccore::ViewDescription,
)
ccore::ViewLinkType_strategy = st.builds(
    ccore::ViewLinkType,
    displayCreate=
        safe_text,
    canCreateLink=
        st.booleans(),
    canCreateItem=
        st.booleans(),
    aggregation=
        st.booleans()
)
ccore::ViewItemType_strategy = st.builds(
    ccore::ViewItemType,
    isRootElement=
        st.booleans(),
    ref=
        st.booleans()
)
ccore::GenInformation_strategy = st.builds(
    ccore::GenInformation,
    cSTName=
        safe_text
)
ItemType_strategy = st.builds(
    ItemType,
)
ccore::RuntimeItemType_strategy = st.builds(
    ccore::RuntimeItemType,
)
ccore::MenuAbstract_strategy = st.builds(
    ccore::MenuAbstract,
    label=
        safe_text,
    path=
        safe_text,
    icon=
        safe_text
)
ccore::Menu_strategy = st.builds(
    ccore::Menu,
)
ccore::ActionExtItemType_strategy = st.builds(
    ccore::ActionExtItemType,
)
ccore::DynamicActions_strategy = st.builds(
    ccore::DynamicActions,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
ccore::Composer_strategy = st.builds(
    ccore::Composer,
    types=
        safe_text
)
ccore::Exporter_strategy = st.builds(
    ccore::Exporter,
    types=
        safe_text
)
ccore::ContentItem_strategy = st.builds(
    ccore::ContentItem,
)
ccore::EStructuralFeature_strategy = st.builds(
    ccore::EStructuralFeature,
)
EPackage_strategy = st.builds(
    EPackage,
)
ccore::ComposerType_strategy = st.builds(
    ccore::ComposerType,
)
ccore::ExporterType_strategy = st.builds(
    ccore::ExporterType,
)
ccore::ContentItemType_strategy = st.builds(
    ccore::ContentItemType,
    extendsClass=
        st.booleans()
)
DBObject_strategy = st.builds(
    DBObject,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ccore::Item_strategy = st.builds(
    ccore::Item,
    displayName=
        safe_text,
    qualifiedName=
        safe_text,
    twVersion=
        st.integers(),
    committedBy=
        safe_text,
    itemHidden=
        st.booleans(),
    twCommittedDate=
        safe_text,
    twRequireNewRev=
        st.booleans(),
    itemReadonly=
        st.booleans(),
    twRevModified=
        st.booleans(),
    isvalid=
        st.booleans()
)
ccore::BindingDesc_strategy = st.builds(
    ccore::BindingDesc,
)
ccore::EPackage_strategy = st.builds(
    ccore::EPackage,
)
ccore::WCListener_strategy = st.builds(
    ccore::WCListener,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
ccore::ItemType_strategy = st.builds(
    ccore::ItemType,
    managerClass=
        safe_text,
    messageErrorId=
        safe_text,
    humanName=
        safe_text,
    overwriteDefaultPages=
        st.booleans(),
    itemManagerClass=
        safe_text,
    packageName=
        safe_text,
    validateNameRe=
        safe_text,
    qualifiedNameTemplate=
        safe_text,
    icon=
        safe_text,
    hasShortName=
        st.booleans(),
    isMetaItemType=
        st.booleans(),
    isRootElement=
        st.booleans(),
    hasContent=
        st.booleans(),
    itemFactoryClass=
        safe_text,
    displayNameTemplate=
        safe_text,
    hasUniqueName=
        st.booleans(),
    isInstanceHidden=
        st.booleans(),
    isInstanceAbstract=
        st.booleans(),
    customManager=
        st.booleans()
)
ccore::ExtentedType_strategy = st.builds(
    ccore::ExtentedType,
)
ccore::EClass_strategy = st.builds(
    ccore::EClass,
)
ccore::GroupOfAttributes_strategy = st.builds(
    ccore::GroupOfAttributes,
    column=
        st.integers()
)
ccore::UIValidator_strategy = st.builds(
    ccore::UIValidator,
)
ccore::Page_strategy = st.builds(
    ccore::Page,
    idRuntime=
        safe_text,
    description=
        safe_text,
    title=
        safe_text,
    label=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
Item_strategy = st.builds(
    Item,
)
ccore::RuntimeItem_strategy = st.builds(
    ccore::RuntimeItem,
    className=
        safe_text,
    extendsClass=
        st.booleans()
)
ccore::Attribute_strategy = st.builds(
    ccore::Attribute,
    tWRevSpecific=
        st.booleans(),
    isList=
        st.booleans(),
    tWCommitKind=
        safe_text,
    devGenerated=
        st.booleans(),
    mustBeInitialized=
        st.booleans(),
    cannotBeUndefined=
        st.booleans(),
    hiddenInComputedPages=
        st.booleans(),
    tWUpdateKind=
        safe_text,
    _final=
        st.booleans(),
    require=
        st.booleans(),
    natif=
        st.booleans(),
    tWEvol=
        safe_text,
    idRuntime=
        safe_text
)
ccore::KeyDefinition_strategy = st.builds(
    ccore::KeyDefinition,
)
ccore::Field_strategy = st.builds(
    ccore::Field,
    position=
        safe_text,
    label=
        safe_text,
    editable=
        st.booleans()
)
ccore::Cadse_strategy = st.builds(
    ccore::Cadse,
    itemRepoURL=
        safe_text,
    description=
        safe_text,
    defaultContentRepoURL=
        safe_text,
    itemRepoPasswd=
        safe_text,
    itemRepoLogin=
        safe_text,
    executed=
        st.booleans(),
    idDefinition=
        safe_text
)
ccore::TypeDefinition_strategy = st.builds(
    ccore::TypeDefinition,
    idRuntime=
        safe_text
)

@given(instance=RuntimeItemType_strategy)
@settings(max_examples=50)
def test_runtimeitemtype_instantiation(instance):
    assert isinstance(instance, RuntimeItemType)

@given(instance=ccore::DBObject_strategy)
@settings(max_examples=50)
def test_ccore::dbobject_instantiation(instance):
    assert isinstance(instance, ccore::DBObject)

@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_uuid_lsb_type(instance):
    assert isinstance(instance.uuid_lsb, str)


@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_uuid_lsb_setter(instance):
    original = instance.uuid_lsb
    instance.uuid_lsb = original
    assert instance.uuid_lsb == original

@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_objectId_type(instance):
    assert isinstance(instance.objectId, int)


@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_uuid_msb_type(instance):
    assert isinstance(instance.uuid_msb, str)


@given(instance=ccore::DBObject_strategy)
def test_ccore::dbobject_uuid_msb_setter(instance):
    original = instance.uuid_msb
    instance.uuid_msb = original
    assert instance.uuid_msb == original

@given(instance=ccore::View_strategy)
@settings(max_examples=50)
def test_ccore::view_instantiation(instance):
    assert isinstance(instance, ccore::View)

@given(instance=ccore::View_strategy)
def test_ccore::view_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=ccore::View_strategy)
def test_ccore::view_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=ccore::ComposerLink_strategy)
@settings(max_examples=50)
def test_ccore::composerlink_instantiation(instance):
    assert isinstance(instance, ccore::ComposerLink)

@given(instance=ccore::MenuGroup_strategy)
@settings(max_examples=50)
def test_ccore::menugroup_instantiation(instance):
    assert isinstance(instance, ccore::MenuGroup)

@given(instance=ccore::MenuAction_strategy)
@settings(max_examples=50)
def test_ccore::menuaction_instantiation(instance):
    assert isinstance(instance, ccore::MenuAction)

@given(instance=ccore::ViewModel_strategy)
@settings(max_examples=50)
def test_ccore::viewmodel_instantiation(instance):
    assert isinstance(instance, ccore::ViewModel)

@given(instance=ccore::ExtItem_strategy)
@settings(max_examples=50)
def test_ccore::extitem_instantiation(instance):
    assert isinstance(instance, ccore::ExtItem)

@given(instance=ccore::ComputedString_strategy)
@settings(max_examples=50)
def test_ccore::computedstring_instantiation(instance):
    assert isinstance(instance, ccore::ComputedString)

@given(instance=ccore::ComputedString_strategy)
def test_ccore::computedstring_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=ccore::ComputedString_strategy)
def test_ccore::computedstring_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=ccore::EEnum_strategy)
@settings(max_examples=50)
def test_ccore::eenum_instantiation(instance):
    assert isinstance(instance, ccore::EEnum)

@given(instance=EEnum_strategy)
@settings(max_examples=50)
def test_eenum_instantiation(instance):
    assert isinstance(instance, EEnum)

@given(instance=ccore::GroupExtItem_strategy)
@settings(max_examples=50)
def test_ccore::groupextitem_instantiation(instance):
    assert isinstance(instance, ccore::GroupExtItem)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=ccore::EnumType_strategy)
@settings(max_examples=50)
def test_ccore::enumtype_instantiation(instance):
    assert isinstance(instance, ccore::EnumType)

@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_javaClass_type(instance):
    assert isinstance(instance.javaClass, str)


@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original

@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_mustBeGenerated_type(instance):
    assert isinstance(instance.mustBeGenerated, bool)


@given(instance=ccore::EnumType_strategy)
def test_ccore::enumtype_mustBeGenerated_setter(instance):
    original = instance.mustBeGenerated
    instance.mustBeGenerated = original
    assert instance.mustBeGenerated == original

@given(instance=RuntimeItem_strategy)
@settings(max_examples=50)
def test_runtimeitem_instantiation(instance):
    assert isinstance(instance, RuntimeItem)

@given(instance=ccore::ModelController_strategy)
@settings(max_examples=50)
def test_ccore::modelcontroller_instantiation(instance):
    assert isinstance(instance, ccore::ModelController)

@given(instance=ccore::InteractionController_strategy)
@settings(max_examples=50)
def test_ccore::interactioncontroller_instantiation(instance):
    assert isinstance(instance, ccore::InteractionController)

@given(instance=ccore::Display_strategy)
@settings(max_examples=50)
def test_ccore::display_instantiation(instance):
    assert isinstance(instance, ccore::Display)

@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsIC_type(instance):
    assert isinstance(instance.extendsIC, bool)


@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsIC_setter(instance):
    original = instance.extendsIC
    instance.extendsIC = original
    assert instance.extendsIC == original

@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsUI_type(instance):
    assert isinstance(instance.extendsUI, bool)


@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsUI_setter(instance):
    original = instance.extendsUI
    instance.extendsUI = original
    assert instance.extendsUI == original

@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsMC_type(instance):
    assert isinstance(instance.extendsMC, bool)


@given(instance=ccore::Display_strategy)
def test_ccore::display_extendsMC_setter(instance):
    original = instance.extendsMC
    instance.extendsMC = original
    assert instance.extendsMC == original

@given(instance=ccore::ExportedContent_strategy)
@settings(max_examples=50)
def test_ccore::exportedcontent_instantiation(instance):
    assert isinstance(instance, ccore::ExportedContent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ccore::ExportedContent_strategy)
@settings(max_examples=30)
def test_ccore::exportedcontent_haschildren_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasChildren()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasChildren).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasChildren' in ccore::ExportedContent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasChildren' in ccore::ExportedContent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasChildren' in ccore::ExportedContent is not implemented or raised an error")

@given(instance=BindingDesc_strategy)
@settings(max_examples=50)
def test_bindingdesc_instantiation(instance):
    assert isinstance(instance, BindingDesc)

@given(instance=ccore::BindExt_strategy)
@settings(max_examples=50)
def test_ccore::bindext_instantiation(instance):
    assert isinstance(instance, ccore::BindExt)

@given(instance=ccore::UnresolvedAttributeType_strategy)
@settings(max_examples=50)
def test_ccore::unresolvedattributetype_instantiation(instance):
    assert isinstance(instance, ccore::UnresolvedAttributeType)

@given(instance=LongAttribute_strategy)
@settings(max_examples=50)
def test_longattribute_instantiation(instance):
    assert isinstance(instance, LongAttribute)

@given(instance=ccore::TimeAttribute_strategy)
@settings(max_examples=50)
def test_ccore::timeattribute_instantiation(instance):
    assert isinstance(instance, ccore::TimeAttribute)

@given(instance=ccore::TimeAttribute_strategy)
def test_ccore::timeattribute_initWithTheCurrentTime_type(instance):
    assert isinstance(instance.initWithTheCurrentTime, bool)


@given(instance=ccore::TimeAttribute_strategy)
def test_ccore::timeattribute_initWithTheCurrentTime_setter(instance):
    original = instance.initWithTheCurrentTime
    instance.initWithTheCurrentTime = original
    assert instance.initWithTheCurrentTime == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=ccore::DateAttribute_strategy)
@settings(max_examples=50)
def test_ccore::dateattribute_instantiation(instance):
    assert isinstance(instance, ccore::DateAttribute)

@given(instance=ccore::Enum_strategy)
@settings(max_examples=50)
def test_ccore::enum_instantiation(instance):
    assert isinstance(instance, ccore::Enum)

@given(instance=ccore::Enum_strategy)
def test_ccore::enum_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=ccore::Enum_strategy)
def test_ccore::enum_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ccore::Enum_strategy)
def test_ccore::enum_enumClazz_type(instance):
    assert isinstance(instance.enumClazz, str)


@given(instance=ccore::Enum_strategy)
def test_ccore::enum_enumClazz_setter(instance):
    original = instance.enumClazz
    instance.enumClazz = original
    assert instance.enumClazz == original

@given(instance=ccore::LinkType_strategy)
@settings(max_examples=50)
def test_ccore::linktype_instantiation(instance):
    assert isinstance(instance, ccore::LinkType)

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_aggregation_type(instance):
    assert isinstance(instance.aggregation, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_composition_type(instance):
    assert isinstance(instance.composition, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_kind_type(instance):
    assert isinstance(instance.kind, int)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_twCoupled_type(instance):
    assert isinstance(instance.twCoupled, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_twCoupled_setter(instance):
    original = instance.twCoupled
    instance.twCoupled = original
    assert instance.twCoupled == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_mapping_type(instance):
    assert isinstance(instance.mapping, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_mapping_setter(instance):
    original = instance.mapping
    instance.mapping = original
    assert instance.mapping == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_hidden_type(instance):
    assert isinstance(instance.hidden, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_linkManager_type(instance):
    assert isinstance(instance.linkManager, str)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_linkManager_setter(instance):
    original = instance.linkManager
    instance.linkManager = original
    assert instance.linkManager == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_annotation_type(instance):
    assert isinstance(instance.annotation, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_group_type(instance):
    assert isinstance(instance.group, bool)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_twDestEvol_type(instance):
    assert isinstance(instance.twDestEvol, str)


@given(instance=ccore::LinkType_strategy)
def test_ccore::linktype_twDestEvol_setter(instance):
    original = instance.twDestEvol
    instance.twDestEvol = original
    assert instance.twDestEvol == original

@given(instance=ccore::DoubleAttribute_strategy)
@settings(max_examples=50)
def test_ccore::doubleattribute_instantiation(instance):
    assert isinstance(instance, ccore::DoubleAttribute)

@given(instance=ccore::LongAttribute_strategy)
@settings(max_examples=50)
def test_ccore::longattribute_instantiation(instance):
    assert isinstance(instance, ccore::LongAttribute)

@given(instance=ccore::UUIDAttribute_strategy)
@settings(max_examples=50)
def test_ccore::uuidattribute_instantiation(instance):
    assert isinstance(instance, ccore::UUIDAttribute)

@given(instance=ccore::IntegerAttribute_strategy)
@settings(max_examples=50)
def test_ccore::integerattribute_instantiation(instance):
    assert isinstance(instance, ccore::IntegerAttribute)

@given(instance=ccore::BooleanAttribute_strategy)
@settings(max_examples=50)
def test_ccore::booleanattribute_instantiation(instance):
    assert isinstance(instance, ccore::BooleanAttribute)

@given(instance=ccore::StringAttribute_strategy)
@settings(max_examples=50)
def test_ccore::stringattribute_instantiation(instance):
    assert isinstance(instance, ccore::StringAttribute)

@given(instance=ccore::StringAttribute_strategy)
def test_ccore::stringattribute_notEmpty_type(instance):
    assert isinstance(instance.notEmpty, bool)


@given(instance=ccore::StringAttribute_strategy)
def test_ccore::stringattribute_notEmpty_setter(instance):
    original = instance.notEmpty
    instance.notEmpty = original
    assert instance.notEmpty == original

@given(instance=ccore::ViewDescription_strategy)
@settings(max_examples=50)
def test_ccore::viewdescription_instantiation(instance):
    assert isinstance(instance, ccore::ViewDescription)

@given(instance=ccore::ViewLinkType_strategy)
@settings(max_examples=50)
def test_ccore::viewlinktype_instantiation(instance):
    assert isinstance(instance, ccore::ViewLinkType)

@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_displayCreate_type(instance):
    assert isinstance(instance.displayCreate, str)


@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_displayCreate_setter(instance):
    original = instance.displayCreate
    instance.displayCreate = original
    assert instance.displayCreate == original

@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_canCreateLink_type(instance):
    assert isinstance(instance.canCreateLink, bool)


@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_canCreateLink_setter(instance):
    original = instance.canCreateLink
    instance.canCreateLink = original
    assert instance.canCreateLink == original

@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_canCreateItem_type(instance):
    assert isinstance(instance.canCreateItem, bool)


@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_canCreateItem_setter(instance):
    original = instance.canCreateItem
    instance.canCreateItem = original
    assert instance.canCreateItem == original

@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_aggregation_type(instance):
    assert isinstance(instance.aggregation, bool)


@given(instance=ccore::ViewLinkType_strategy)
def test_ccore::viewlinktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=ccore::ViewItemType_strategy)
@settings(max_examples=50)
def test_ccore::viewitemtype_instantiation(instance):
    assert isinstance(instance, ccore::ViewItemType)

@given(instance=ccore::ViewItemType_strategy)
def test_ccore::viewitemtype_isRootElement_type(instance):
    assert isinstance(instance.isRootElement, bool)


@given(instance=ccore::ViewItemType_strategy)
def test_ccore::viewitemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original

@given(instance=ccore::ViewItemType_strategy)
def test_ccore::viewitemtype_ref_type(instance):
    assert isinstance(instance.ref, bool)


@given(instance=ccore::ViewItemType_strategy)
def test_ccore::viewitemtype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=ccore::GenInformation_strategy)
@settings(max_examples=50)
def test_ccore::geninformation_instantiation(instance):
    assert isinstance(instance, ccore::GenInformation)

@given(instance=ccore::GenInformation_strategy)
def test_ccore::geninformation_cSTName_type(instance):
    assert isinstance(instance.cSTName, str)


@given(instance=ccore::GenInformation_strategy)
def test_ccore::geninformation_cSTName_setter(instance):
    original = instance.cSTName
    instance.cSTName = original
    assert instance.cSTName == original

@given(instance=ItemType_strategy)
@settings(max_examples=50)
def test_itemtype_instantiation(instance):
    assert isinstance(instance, ItemType)

@given(instance=ccore::RuntimeItemType_strategy)
@settings(max_examples=50)
def test_ccore::runtimeitemtype_instantiation(instance):
    assert isinstance(instance, ccore::RuntimeItemType)

@given(instance=ccore::MenuAbstract_strategy)
@settings(max_examples=50)
def test_ccore::menuabstract_instantiation(instance):
    assert isinstance(instance, ccore::MenuAbstract)

@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=ccore::MenuAbstract_strategy)
def test_ccore::menuabstract_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=ccore::Menu_strategy)
@settings(max_examples=50)
def test_ccore::menu_instantiation(instance):
    assert isinstance(instance, ccore::Menu)

@given(instance=ccore::ActionExtItemType_strategy)
@settings(max_examples=50)
def test_ccore::actionextitemtype_instantiation(instance):
    assert isinstance(instance, ccore::ActionExtItemType)

@given(instance=ccore::DynamicActions_strategy)
@settings(max_examples=50)
def test_ccore::dynamicactions_instantiation(instance):
    assert isinstance(instance, ccore::DynamicActions)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=ccore::Composer_strategy)
@settings(max_examples=50)
def test_ccore::composer_instantiation(instance):
    assert isinstance(instance, ccore::Composer)

@given(instance=ccore::Composer_strategy)
def test_ccore::composer_types_type(instance):
    assert isinstance(instance.types, str)


@given(instance=ccore::Composer_strategy)
def test_ccore::composer_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=ccore::Exporter_strategy)
@settings(max_examples=50)
def test_ccore::exporter_instantiation(instance):
    assert isinstance(instance, ccore::Exporter)

@given(instance=ccore::Exporter_strategy)
def test_ccore::exporter_types_type(instance):
    assert isinstance(instance.types, str)


@given(instance=ccore::Exporter_strategy)
def test_ccore::exporter_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=ccore::ContentItem_strategy)
@settings(max_examples=50)
def test_ccore::contentitem_instantiation(instance):
    assert isinstance(instance, ccore::ContentItem)

@given(instance=ccore::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ccore::estructuralfeature_instantiation(instance):
    assert isinstance(instance, ccore::EStructuralFeature)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=ccore::ComposerType_strategy)
@settings(max_examples=50)
def test_ccore::composertype_instantiation(instance):
    assert isinstance(instance, ccore::ComposerType)

@given(instance=ccore::ExporterType_strategy)
@settings(max_examples=50)
def test_ccore::exportertype_instantiation(instance):
    assert isinstance(instance, ccore::ExporterType)

@given(instance=ccore::ContentItemType_strategy)
@settings(max_examples=50)
def test_ccore::contentitemtype_instantiation(instance):
    assert isinstance(instance, ccore::ContentItemType)

@given(instance=ccore::ContentItemType_strategy)
def test_ccore::contentitemtype_extendsClass_type(instance):
    assert isinstance(instance.extendsClass, bool)


@given(instance=ccore::ContentItemType_strategy)
def test_ccore::contentitemtype_extendsClass_setter(instance):
    original = instance.extendsClass
    instance.extendsClass = original
    assert instance.extendsClass == original

@given(instance=DBObject_strategy)
@settings(max_examples=50)
def test_dbobject_instantiation(instance):
    assert isinstance(instance, DBObject)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ccore::Item_strategy)
@settings(max_examples=50)
def test_ccore::item_instantiation(instance):
    assert isinstance(instance, ccore::Item)

@given(instance=ccore::Item_strategy)
def test_ccore::item_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=ccore::Item_strategy)
def test_ccore::item_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=ccore::Item_strategy)
def test_ccore::item_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_twVersion_type(instance):
    assert isinstance(instance.twVersion, int)


@given(instance=ccore::Item_strategy)
def test_ccore::item_twVersion_setter(instance):
    original = instance.twVersion
    instance.twVersion = original
    assert instance.twVersion == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_committedBy_type(instance):
    assert isinstance(instance.committedBy, str)


@given(instance=ccore::Item_strategy)
def test_ccore::item_committedBy_setter(instance):
    original = instance.committedBy
    instance.committedBy = original
    assert instance.committedBy == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_itemHidden_type(instance):
    assert isinstance(instance.itemHidden, bool)


@given(instance=ccore::Item_strategy)
def test_ccore::item_itemHidden_setter(instance):
    original = instance.itemHidden
    instance.itemHidden = original
    assert instance.itemHidden == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_twCommittedDate_type(instance):
    assert isinstance(instance.twCommittedDate, str)


@given(instance=ccore::Item_strategy)
def test_ccore::item_twCommittedDate_setter(instance):
    original = instance.twCommittedDate
    instance.twCommittedDate = original
    assert instance.twCommittedDate == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_twRequireNewRev_type(instance):
    assert isinstance(instance.twRequireNewRev, bool)


@given(instance=ccore::Item_strategy)
def test_ccore::item_twRequireNewRev_setter(instance):
    original = instance.twRequireNewRev
    instance.twRequireNewRev = original
    assert instance.twRequireNewRev == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_itemReadonly_type(instance):
    assert isinstance(instance.itemReadonly, bool)


@given(instance=ccore::Item_strategy)
def test_ccore::item_itemReadonly_setter(instance):
    original = instance.itemReadonly
    instance.itemReadonly = original
    assert instance.itemReadonly == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_twRevModified_type(instance):
    assert isinstance(instance.twRevModified, bool)


@given(instance=ccore::Item_strategy)
def test_ccore::item_twRevModified_setter(instance):
    original = instance.twRevModified
    instance.twRevModified = original
    assert instance.twRevModified == original

@given(instance=ccore::Item_strategy)
def test_ccore::item_isvalid_type(instance):
    assert isinstance(instance.isvalid, bool)


@given(instance=ccore::Item_strategy)
def test_ccore::item_isvalid_setter(instance):
    original = instance.isvalid
    instance.isvalid = original
    assert instance.isvalid == original

@given(instance=ccore::BindingDesc_strategy)
@settings(max_examples=50)
def test_ccore::bindingdesc_instantiation(instance):
    assert isinstance(instance, ccore::BindingDesc)

@given(instance=ccore::EPackage_strategy)
@settings(max_examples=50)
def test_ccore::epackage_instantiation(instance):
    assert isinstance(instance, ccore::EPackage)

@given(instance=ccore::WCListener_strategy)
@settings(max_examples=50)
def test_ccore::wclistener_instantiation(instance):
    assert isinstance(instance, ccore::WCListener)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=ccore::ItemType_strategy)
@settings(max_examples=50)
def test_ccore::itemtype_instantiation(instance):
    assert isinstance(instance, ccore::ItemType)

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_managerClass_type(instance):
    assert isinstance(instance.managerClass, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_managerClass_setter(instance):
    original = instance.managerClass
    instance.managerClass = original
    assert instance.managerClass == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_messageErrorId_type(instance):
    assert isinstance(instance.messageErrorId, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_messageErrorId_setter(instance):
    original = instance.messageErrorId
    instance.messageErrorId = original
    assert instance.messageErrorId == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_humanName_type(instance):
    assert isinstance(instance.humanName, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_humanName_setter(instance):
    original = instance.humanName
    instance.humanName = original
    assert instance.humanName == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_overwriteDefaultPages_type(instance):
    assert isinstance(instance.overwriteDefaultPages, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_overwriteDefaultPages_setter(instance):
    original = instance.overwriteDefaultPages
    instance.overwriteDefaultPages = original
    assert instance.overwriteDefaultPages == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_itemManagerClass_type(instance):
    assert isinstance(instance.itemManagerClass, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_itemManagerClass_setter(instance):
    original = instance.itemManagerClass
    instance.itemManagerClass = original
    assert instance.itemManagerClass == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_validateNameRe_type(instance):
    assert isinstance(instance.validateNameRe, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_validateNameRe_setter(instance):
    original = instance.validateNameRe
    instance.validateNameRe = original
    assert instance.validateNameRe == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_qualifiedNameTemplate_type(instance):
    assert isinstance(instance.qualifiedNameTemplate, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_qualifiedNameTemplate_setter(instance):
    original = instance.qualifiedNameTemplate
    instance.qualifiedNameTemplate = original
    assert instance.qualifiedNameTemplate == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasShortName_type(instance):
    assert isinstance(instance.hasShortName, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasShortName_setter(instance):
    original = instance.hasShortName
    instance.hasShortName = original
    assert instance.hasShortName == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isMetaItemType_type(instance):
    assert isinstance(instance.isMetaItemType, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isMetaItemType_setter(instance):
    original = instance.isMetaItemType
    instance.isMetaItemType = original
    assert instance.isMetaItemType == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isRootElement_type(instance):
    assert isinstance(instance.isRootElement, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasContent_type(instance):
    assert isinstance(instance.hasContent, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasContent_setter(instance):
    original = instance.hasContent
    instance.hasContent = original
    assert instance.hasContent == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_itemFactoryClass_type(instance):
    assert isinstance(instance.itemFactoryClass, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_itemFactoryClass_setter(instance):
    original = instance.itemFactoryClass
    instance.itemFactoryClass = original
    assert instance.itemFactoryClass == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_displayNameTemplate_type(instance):
    assert isinstance(instance.displayNameTemplate, str)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_displayNameTemplate_setter(instance):
    original = instance.displayNameTemplate
    instance.displayNameTemplate = original
    assert instance.displayNameTemplate == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasUniqueName_type(instance):
    assert isinstance(instance.hasUniqueName, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_hasUniqueName_setter(instance):
    original = instance.hasUniqueName
    instance.hasUniqueName = original
    assert instance.hasUniqueName == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isInstanceHidden_type(instance):
    assert isinstance(instance.isInstanceHidden, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isInstanceHidden_setter(instance):
    original = instance.isInstanceHidden
    instance.isInstanceHidden = original
    assert instance.isInstanceHidden == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isInstanceAbstract_type(instance):
    assert isinstance(instance.isInstanceAbstract, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_isInstanceAbstract_setter(instance):
    original = instance.isInstanceAbstract
    instance.isInstanceAbstract = original
    assert instance.isInstanceAbstract == original

@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_customManager_type(instance):
    assert isinstance(instance.customManager, bool)


@given(instance=ccore::ItemType_strategy)
def test_ccore::itemtype_customManager_setter(instance):
    original = instance.customManager
    instance.customManager = original
    assert instance.customManager == original

@given(instance=ccore::ExtentedType_strategy)
@settings(max_examples=50)
def test_ccore::extentedtype_instantiation(instance):
    assert isinstance(instance, ccore::ExtentedType)

@given(instance=ccore::EClass_strategy)
@settings(max_examples=50)
def test_ccore::eclass_instantiation(instance):
    assert isinstance(instance, ccore::EClass)

@given(instance=ccore::GroupOfAttributes_strategy)
@settings(max_examples=50)
def test_ccore::groupofattributes_instantiation(instance):
    assert isinstance(instance, ccore::GroupOfAttributes)

@given(instance=ccore::GroupOfAttributes_strategy)
def test_ccore::groupofattributes_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=ccore::GroupOfAttributes_strategy)
def test_ccore::groupofattributes_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=ccore::UIValidator_strategy)
@settings(max_examples=50)
def test_ccore::uivalidator_instantiation(instance):
    assert isinstance(instance, ccore::UIValidator)

@given(instance=ccore::Page_strategy)
@settings(max_examples=50)
def test_ccore::page_instantiation(instance):
    assert isinstance(instance, ccore::Page)

@given(instance=ccore::Page_strategy)
def test_ccore::page_idRuntime_type(instance):
    assert isinstance(instance.idRuntime, str)


@given(instance=ccore::Page_strategy)
def test_ccore::page_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original

@given(instance=ccore::Page_strategy)
def test_ccore::page_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ccore::Page_strategy)
def test_ccore::page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ccore::Page_strategy)
def test_ccore::page_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ccore::Page_strategy)
def test_ccore::page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ccore::Page_strategy)
def test_ccore::page_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ccore::Page_strategy)
def test_ccore::page_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=ccore::RuntimeItem_strategy)
@settings(max_examples=50)
def test_ccore::runtimeitem_instantiation(instance):
    assert isinstance(instance, ccore::RuntimeItem)

@given(instance=ccore::RuntimeItem_strategy)
def test_ccore::runtimeitem_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=ccore::RuntimeItem_strategy)
def test_ccore::runtimeitem_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=ccore::RuntimeItem_strategy)
def test_ccore::runtimeitem_extendsClass_type(instance):
    assert isinstance(instance.extendsClass, bool)


@given(instance=ccore::RuntimeItem_strategy)
def test_ccore::runtimeitem_extendsClass_setter(instance):
    original = instance.extendsClass
    instance.extendsClass = original
    assert instance.extendsClass == original

@given(instance=ccore::Attribute_strategy)
@settings(max_examples=50)
def test_ccore::attribute_instantiation(instance):
    assert isinstance(instance, ccore::Attribute)

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWRevSpecific_type(instance):
    assert isinstance(instance.tWRevSpecific, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWRevSpecific_setter(instance):
    original = instance.tWRevSpecific
    instance.tWRevSpecific = original
    assert instance.tWRevSpecific == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_isList_type(instance):
    assert isinstance(instance.isList, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWCommitKind_type(instance):
    assert isinstance(instance.tWCommitKind, str)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWCommitKind_setter(instance):
    original = instance.tWCommitKind
    instance.tWCommitKind = original
    assert instance.tWCommitKind == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_devGenerated_type(instance):
    assert isinstance(instance.devGenerated, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_devGenerated_setter(instance):
    original = instance.devGenerated
    instance.devGenerated = original
    assert instance.devGenerated == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_mustBeInitialized_type(instance):
    assert isinstance(instance.mustBeInitialized, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_mustBeInitialized_setter(instance):
    original = instance.mustBeInitialized
    instance.mustBeInitialized = original
    assert instance.mustBeInitialized == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_cannotBeUndefined_type(instance):
    assert isinstance(instance.cannotBeUndefined, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_cannotBeUndefined_setter(instance):
    original = instance.cannotBeUndefined
    instance.cannotBeUndefined = original
    assert instance.cannotBeUndefined == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_hiddenInComputedPages_type(instance):
    assert isinstance(instance.hiddenInComputedPages, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_hiddenInComputedPages_setter(instance):
    original = instance.hiddenInComputedPages
    instance.hiddenInComputedPages = original
    assert instance.hiddenInComputedPages == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWUpdateKind_type(instance):
    assert isinstance(instance.tWUpdateKind, str)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWUpdateKind_setter(instance):
    original = instance.tWUpdateKind
    instance.tWUpdateKind = original
    assert instance.tWUpdateKind == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute__final_type(instance):
    assert isinstance(instance._final, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute__final_setter(instance):
    original = instance._final
    instance._final = original
    assert instance._final == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_require_type(instance):
    assert isinstance(instance.require, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_require_setter(instance):
    original = instance.require
    instance.require = original
    assert instance.require == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_natif_type(instance):
    assert isinstance(instance.natif, bool)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_natif_setter(instance):
    original = instance.natif
    instance.natif = original
    assert instance.natif == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWEvol_type(instance):
    assert isinstance(instance.tWEvol, str)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_tWEvol_setter(instance):
    original = instance.tWEvol
    instance.tWEvol = original
    assert instance.tWEvol == original

@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_idRuntime_type(instance):
    assert isinstance(instance.idRuntime, str)


@given(instance=ccore::Attribute_strategy)
def test_ccore::attribute_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original

@given(instance=ccore::KeyDefinition_strategy)
@settings(max_examples=50)
def test_ccore::keydefinition_instantiation(instance):
    assert isinstance(instance, ccore::KeyDefinition)

@given(instance=ccore::Field_strategy)
@settings(max_examples=50)
def test_ccore::field_instantiation(instance):
    assert isinstance(instance, ccore::Field)

@given(instance=ccore::Field_strategy)
def test_ccore::field_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=ccore::Field_strategy)
def test_ccore::field_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=ccore::Field_strategy)
def test_ccore::field_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ccore::Field_strategy)
def test_ccore::field_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ccore::Field_strategy)
def test_ccore::field_editable_type(instance):
    assert isinstance(instance.editable, bool)


@given(instance=ccore::Field_strategy)
def test_ccore::field_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original

@given(instance=ccore::Cadse_strategy)
@settings(max_examples=50)
def test_ccore::cadse_instantiation(instance):
    assert isinstance(instance, ccore::Cadse)

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoURL_type(instance):
    assert isinstance(instance.itemRepoURL, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoURL_setter(instance):
    original = instance.itemRepoURL
    instance.itemRepoURL = original
    assert instance.itemRepoURL == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_defaultContentRepoURL_type(instance):
    assert isinstance(instance.defaultContentRepoURL, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_defaultContentRepoURL_setter(instance):
    original = instance.defaultContentRepoURL
    instance.defaultContentRepoURL = original
    assert instance.defaultContentRepoURL == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoPasswd_type(instance):
    assert isinstance(instance.itemRepoPasswd, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoPasswd_setter(instance):
    original = instance.itemRepoPasswd
    instance.itemRepoPasswd = original
    assert instance.itemRepoPasswd == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoLogin_type(instance):
    assert isinstance(instance.itemRepoLogin, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_itemRepoLogin_setter(instance):
    original = instance.itemRepoLogin
    instance.itemRepoLogin = original
    assert instance.itemRepoLogin == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_executed_type(instance):
    assert isinstance(instance.executed, bool)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_executed_setter(instance):
    original = instance.executed
    instance.executed = original
    assert instance.executed == original

@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_idDefinition_type(instance):
    assert isinstance(instance.idDefinition, str)


@given(instance=ccore::Cadse_strategy)
def test_ccore::cadse_idDefinition_setter(instance):
    original = instance.idDefinition
    instance.idDefinition = original
    assert instance.idDefinition == original

@given(instance=ccore::TypeDefinition_strategy)
@settings(max_examples=50)
def test_ccore::typedefinition_instantiation(instance):
    assert isinstance(instance, ccore::TypeDefinition)

@given(instance=ccore::TypeDefinition_strategy)
def test_ccore::typedefinition_idRuntime_type(instance):
    assert isinstance(instance.idRuntime, str)


@given(instance=ccore::TypeDefinition_strategy)
def test_ccore::typedefinition_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original
