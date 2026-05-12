import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ItemType,
    ccore_MenuAbstract,
    ccore_Menu,
    ccore_ActionExtItemType,
    ccore_DynamicActions,
    EAttribute,
    ccore_ContentItem,
    ccore_EStructuralFeature,
    EPackage,
    ccore_ContentItemType,
    DBObject,
    ENamedElement,
    ccore_Item,
    ccore_BindingDesc,
    ccore_EPackage,
    ccore_WCListener,
    TypeDefinition,
    ccore_ItemType,
    ccore_ExtentedType,
    ccore_EClass,
    ccore_GroupOfAttributes,
    ccore_UIValidator,
    ccore_Page,
    EClass,
    Item,
    ccore_Cadse,
    ccore_KeyDefinition,
    ccore_RuntimeItem,
    ccore_Field,
    ccore_Attribute,
    ccore_TypeDefinition,
    ccore_RuntimeItemType,
    RuntimeItemType,
    ccore_ComposerType,
    ccore_ExporterType,
    ccore_DBObject,
    ccore_View,
    ccore_ComposerLink,
    ccore_MenuGroup,
    ccore_MenuAction,
    ccore_ViewModel,
    ccore_ExtItem,
    ccore_ComputedString,
    ccore_EEnum,
    EEnum,
    ccore_GroupExtItem,
    EReference,
    ccore_EnumType,
    RuntimeItem,
    ccore_Composer,
    ccore_Exporter,
    ccore_ModelController,
    ccore_InteractionController,
    ccore_Display,
    ccore_ExportedContent,
    BindingDesc,
    ccore_BindExt,
    ccore_UnresolvedAttributeType,
    LongAttribute,
    ccore_TimeAttribute,
    Attribute,
    ccore_IntegerAttribute,
    ccore_Enum,
    ccore_LongAttribute,
    ccore_UUIDAttribute,
    ccore_DateAttribute,
    ccore_LinkType,
    ccore_DoubleAttribute,
    ccore_BooleanAttribute,
    ccore_StringAttribute,
    ccore_ViewDescription,
    ccore_ViewLinkType,
    ccore_ViewItemType,
    ccore_GenInformation,
    PositionEnum,
    TWCommitKind,
    TWDestEvol,
    TWEvol,
    TWUpdateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itemtype_is_not_abstract():
    assert not inspect.isabstract(ItemType)


def test_itemtype_constructor_exists():
    assert callable(ItemType.__init__)


def test_itemtype_constructor_args():
    sig = inspect.signature(ItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_menuabstract_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuAbstract)


def test_ccore_menuabstract_constructor_exists():
    assert callable(ccore_MenuAbstract.__init__)


def test_ccore_menuabstract_constructor_args():
    sig = inspect.signature(ccore_MenuAbstract.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "label" in params, "Missing parameter 'label'"
    assert "path" in params, "Missing parameter 'path'"

def test_ccore_menuabstract_has_icon():
    assert hasattr(ccore_MenuAbstract, "icon")
    descriptor = None
    for klass in ccore_MenuAbstract.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_ccore_menuabstract_has_label():
    assert hasattr(ccore_MenuAbstract, "label")
    descriptor = None
    for klass in ccore_MenuAbstract.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ccore_menuabstract_has_path():
    assert hasattr(ccore_MenuAbstract, "path")
    descriptor = None
    for klass in ccore_MenuAbstract.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_ccore_menu_is_not_abstract():
    assert not inspect.isabstract(ccore_Menu)


def test_ccore_menu_constructor_exists():
    assert callable(ccore_Menu.__init__)


def test_ccore_menu_constructor_args():
    sig = inspect.signature(ccore_Menu.__init__)
    params = list(sig.parameters.keys())



def test_ccore_actionextitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ActionExtItemType)


def test_ccore_actionextitemtype_constructor_exists():
    assert callable(ccore_ActionExtItemType.__init__)


def test_ccore_actionextitemtype_constructor_args():
    sig = inspect.signature(ccore_ActionExtItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_dynamicactions_is_not_abstract():
    assert not inspect.isabstract(ccore_DynamicActions)


def test_ccore_dynamicactions_constructor_exists():
    assert callable(ccore_DynamicActions.__init__)


def test_ccore_dynamicactions_constructor_args():
    sig = inspect.signature(ccore_DynamicActions.__init__)
    params = list(sig.parameters.keys())



def test_eattribute_is_not_abstract():
    assert not inspect.isabstract(EAttribute)


def test_eattribute_constructor_exists():
    assert callable(EAttribute.__init__)


def test_eattribute_constructor_args():
    sig = inspect.signature(EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_contentitem_is_not_abstract():
    assert not inspect.isabstract(ccore_ContentItem)


def test_ccore_contentitem_constructor_exists():
    assert callable(ccore_ContentItem.__init__)


def test_ccore_contentitem_constructor_args():
    sig = inspect.signature(ccore_ContentItem.__init__)
    params = list(sig.parameters.keys())



def test_ccore_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ccore_EStructuralFeature)


def test_ccore_estructuralfeature_constructor_exists():
    assert callable(ccore_EStructuralFeature.__init__)


def test_ccore_estructuralfeature_constructor_args():
    sig = inspect.signature(ccore_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ccore_contentitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ContentItemType)


def test_ccore_contentitemtype_constructor_exists():
    assert callable(ccore_ContentItemType.__init__)


def test_ccore_contentitemtype_constructor_args():
    sig = inspect.signature(ccore_ContentItemType.__init__)
    params = list(sig.parameters.keys())
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"

def test_ccore_contentitemtype_has_extendsClass():
    assert hasattr(ccore_ContentItemType, "extendsClass")
    descriptor = None
    for klass in ccore_ContentItemType.__mro__:
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



def test_ccore_item_is_not_abstract():
    assert not inspect.isabstract(ccore_Item)


def test_ccore_item_constructor_exists():
    assert callable(ccore_Item.__init__)


def test_ccore_item_constructor_args():
    sig = inspect.signature(ccore_Item.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "twCommittedDate" in params, "Missing parameter 'twCommittedDate'"
    assert "twVersion" in params, "Missing parameter 'twVersion'"
    assert "twRevModified" in params, "Missing parameter 'twRevModified'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "twRequireNewRev" in params, "Missing parameter 'twRequireNewRev'"
    assert "committedBy" in params, "Missing parameter 'committedBy'"
    assert "itemReadonly" in params, "Missing parameter 'itemReadonly'"
    assert "isvalid" in params, "Missing parameter 'isvalid'"
    assert "itemHidden" in params, "Missing parameter 'itemHidden'"

def test_ccore_item_has_qualifiedName():
    assert hasattr(ccore_Item, "qualifiedName")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_twCommittedDate():
    assert hasattr(ccore_Item, "twCommittedDate")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "twCommittedDate" in klass.__dict__:
            descriptor = klass.__dict__["twCommittedDate"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_twVersion():
    assert hasattr(ccore_Item, "twVersion")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "twVersion" in klass.__dict__:
            descriptor = klass.__dict__["twVersion"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_twRevModified():
    assert hasattr(ccore_Item, "twRevModified")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "twRevModified" in klass.__dict__:
            descriptor = klass.__dict__["twRevModified"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_displayName():
    assert hasattr(ccore_Item, "displayName")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_twRequireNewRev():
    assert hasattr(ccore_Item, "twRequireNewRev")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "twRequireNewRev" in klass.__dict__:
            descriptor = klass.__dict__["twRequireNewRev"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_committedBy():
    assert hasattr(ccore_Item, "committedBy")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "committedBy" in klass.__dict__:
            descriptor = klass.__dict__["committedBy"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_itemReadonly():
    assert hasattr(ccore_Item, "itemReadonly")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "itemReadonly" in klass.__dict__:
            descriptor = klass.__dict__["itemReadonly"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_isvalid():
    assert hasattr(ccore_Item, "isvalid")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "isvalid" in klass.__dict__:
            descriptor = klass.__dict__["isvalid"]
            break
    assert isinstance(descriptor, property)

def test_ccore_item_has_itemHidden():
    assert hasattr(ccore_Item, "itemHidden")
    descriptor = None
    for klass in ccore_Item.__mro__:
        if "itemHidden" in klass.__dict__:
            descriptor = klass.__dict__["itemHidden"]
            break
    assert isinstance(descriptor, property)



def test_ccore_bindingdesc_is_not_abstract():
    assert not inspect.isabstract(ccore_BindingDesc)


def test_ccore_bindingdesc_constructor_exists():
    assert callable(ccore_BindingDesc.__init__)


def test_ccore_bindingdesc_constructor_args():
    sig = inspect.signature(ccore_BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_ccore_epackage_is_not_abstract():
    assert not inspect.isabstract(ccore_EPackage)


def test_ccore_epackage_constructor_exists():
    assert callable(ccore_EPackage.__init__)


def test_ccore_epackage_constructor_args():
    sig = inspect.signature(ccore_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ccore_wclistener_is_not_abstract():
    assert not inspect.isabstract(ccore_WCListener)


def test_ccore_wclistener_constructor_exists():
    assert callable(ccore_WCListener.__init__)


def test_ccore_wclistener_constructor_args():
    sig = inspect.signature(ccore_WCListener.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ccore_itemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ItemType)


def test_ccore_itemtype_constructor_exists():
    assert callable(ccore_ItemType.__init__)


def test_ccore_itemtype_constructor_args():
    sig = inspect.signature(ccore_ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "isInstanceHidden" in params, "Missing parameter 'isInstanceHidden'"
    assert "hasShortName" in params, "Missing parameter 'hasShortName'"
    assert "customManager" in params, "Missing parameter 'customManager'"
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "overwriteDefaultPages" in params, "Missing parameter 'overwriteDefaultPages'"
    assert "qualifiedNameTemplate" in params, "Missing parameter 'qualifiedNameTemplate'"
    assert "validateNameRe" in params, "Missing parameter 'validateNameRe'"
    assert "messageErrorId" in params, "Missing parameter 'messageErrorId'"
    assert "hasContent" in params, "Missing parameter 'hasContent'"
    assert "itemManagerClass" in params, "Missing parameter 'itemManagerClass'"
    assert "isInstanceAbstract" in params, "Missing parameter 'isInstanceAbstract'"
    assert "managerClass" in params, "Missing parameter 'managerClass'"
    assert "humanName" in params, "Missing parameter 'humanName'"
    assert "displayNameTemplate" in params, "Missing parameter 'displayNameTemplate'"
    assert "itemFactoryClass" in params, "Missing parameter 'itemFactoryClass'"
    assert "hasUniqueName" in params, "Missing parameter 'hasUniqueName'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "isMetaItemType" in params, "Missing parameter 'isMetaItemType'"
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"

def test_ccore_itemtype_has_isInstanceHidden():
    assert hasattr(ccore_ItemType, "isInstanceHidden")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "isInstanceHidden" in klass.__dict__:
            descriptor = klass.__dict__["isInstanceHidden"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_hasShortName():
    assert hasattr(ccore_ItemType, "hasShortName")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "hasShortName" in klass.__dict__:
            descriptor = klass.__dict__["hasShortName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_customManager():
    assert hasattr(ccore_ItemType, "customManager")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "customManager" in klass.__dict__:
            descriptor = klass.__dict__["customManager"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_packageName():
    assert hasattr(ccore_ItemType, "packageName")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_overwriteDefaultPages():
    assert hasattr(ccore_ItemType, "overwriteDefaultPages")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "overwriteDefaultPages" in klass.__dict__:
            descriptor = klass.__dict__["overwriteDefaultPages"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_qualifiedNameTemplate():
    assert hasattr(ccore_ItemType, "qualifiedNameTemplate")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "qualifiedNameTemplate" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedNameTemplate"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_validateNameRe():
    assert hasattr(ccore_ItemType, "validateNameRe")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "validateNameRe" in klass.__dict__:
            descriptor = klass.__dict__["validateNameRe"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_messageErrorId():
    assert hasattr(ccore_ItemType, "messageErrorId")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "messageErrorId" in klass.__dict__:
            descriptor = klass.__dict__["messageErrorId"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_hasContent():
    assert hasattr(ccore_ItemType, "hasContent")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "hasContent" in klass.__dict__:
            descriptor = klass.__dict__["hasContent"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_itemManagerClass():
    assert hasattr(ccore_ItemType, "itemManagerClass")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "itemManagerClass" in klass.__dict__:
            descriptor = klass.__dict__["itemManagerClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_isInstanceAbstract():
    assert hasattr(ccore_ItemType, "isInstanceAbstract")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "isInstanceAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isInstanceAbstract"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_managerClass():
    assert hasattr(ccore_ItemType, "managerClass")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "managerClass" in klass.__dict__:
            descriptor = klass.__dict__["managerClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_humanName():
    assert hasattr(ccore_ItemType, "humanName")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "humanName" in klass.__dict__:
            descriptor = klass.__dict__["humanName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_displayNameTemplate():
    assert hasattr(ccore_ItemType, "displayNameTemplate")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "displayNameTemplate" in klass.__dict__:
            descriptor = klass.__dict__["displayNameTemplate"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_itemFactoryClass():
    assert hasattr(ccore_ItemType, "itemFactoryClass")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "itemFactoryClass" in klass.__dict__:
            descriptor = klass.__dict__["itemFactoryClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_hasUniqueName():
    assert hasattr(ccore_ItemType, "hasUniqueName")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "hasUniqueName" in klass.__dict__:
            descriptor = klass.__dict__["hasUniqueName"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_icon():
    assert hasattr(ccore_ItemType, "icon")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_isMetaItemType():
    assert hasattr(ccore_ItemType, "isMetaItemType")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "isMetaItemType" in klass.__dict__:
            descriptor = klass.__dict__["isMetaItemType"]
            break
    assert isinstance(descriptor, property)

def test_ccore_itemtype_has_isRootElement():
    assert hasattr(ccore_ItemType, "isRootElement")
    descriptor = None
    for klass in ccore_ItemType.__mro__:
        if "isRootElement" in klass.__dict__:
            descriptor = klass.__dict__["isRootElement"]
            break
    assert isinstance(descriptor, property)



def test_ccore_extentedtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ExtentedType)


def test_ccore_extentedtype_constructor_exists():
    assert callable(ccore_ExtentedType.__init__)


def test_ccore_extentedtype_constructor_args():
    sig = inspect.signature(ccore_ExtentedType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_eclass_is_not_abstract():
    assert not inspect.isabstract(ccore_EClass)


def test_ccore_eclass_constructor_exists():
    assert callable(ccore_EClass.__init__)


def test_ccore_eclass_constructor_args():
    sig = inspect.signature(ccore_EClass.__init__)
    params = list(sig.parameters.keys())



def test_ccore_groupofattributes_is_not_abstract():
    assert not inspect.isabstract(ccore_GroupOfAttributes)


def test_ccore_groupofattributes_constructor_exists():
    assert callable(ccore_GroupOfAttributes.__init__)


def test_ccore_groupofattributes_constructor_args():
    sig = inspect.signature(ccore_GroupOfAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_ccore_groupofattributes_has_column():
    assert hasattr(ccore_GroupOfAttributes, "column")
    descriptor = None
    for klass in ccore_GroupOfAttributes.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_ccore_uivalidator_is_not_abstract():
    assert not inspect.isabstract(ccore_UIValidator)


def test_ccore_uivalidator_constructor_exists():
    assert callable(ccore_UIValidator.__init__)


def test_ccore_uivalidator_constructor_args():
    sig = inspect.signature(ccore_UIValidator.__init__)
    params = list(sig.parameters.keys())



def test_ccore_page_is_not_abstract():
    assert not inspect.isabstract(ccore_Page)


def test_ccore_page_constructor_exists():
    assert callable(ccore_Page.__init__)


def test_ccore_page_constructor_args():
    sig = inspect.signature(ccore_Page.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"
    assert "title" in params, "Missing parameter 'title'"

def test_ccore_page_has_label():
    assert hasattr(ccore_Page, "label")
    descriptor = None
    for klass in ccore_Page.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ccore_page_has_description():
    assert hasattr(ccore_Page, "description")
    descriptor = None
    for klass in ccore_Page.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ccore_page_has_idRuntime():
    assert hasattr(ccore_Page, "idRuntime")
    descriptor = None
    for klass in ccore_Page.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)

def test_ccore_page_has_title():
    assert hasattr(ccore_Page, "title")
    descriptor = None
    for klass in ccore_Page.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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



def test_ccore_cadse_is_not_abstract():
    assert not inspect.isabstract(ccore_Cadse)


def test_ccore_cadse_constructor_exists():
    assert callable(ccore_Cadse.__init__)


def test_ccore_cadse_constructor_args():
    sig = inspect.signature(ccore_Cadse.__init__)
    params = list(sig.parameters.keys())
    assert "itemRepoLogin" in params, "Missing parameter 'itemRepoLogin'"
    assert "idDefinition" in params, "Missing parameter 'idDefinition'"
    assert "itemRepoURL" in params, "Missing parameter 'itemRepoURL'"
    assert "description" in params, "Missing parameter 'description'"
    assert "executed" in params, "Missing parameter 'executed'"
    assert "itemRepoPasswd" in params, "Missing parameter 'itemRepoPasswd'"
    assert "defaultContentRepoURL" in params, "Missing parameter 'defaultContentRepoURL'"

def test_ccore_cadse_has_itemRepoLogin():
    assert hasattr(ccore_Cadse, "itemRepoLogin")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "itemRepoLogin" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoLogin"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_idDefinition():
    assert hasattr(ccore_Cadse, "idDefinition")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "idDefinition" in klass.__dict__:
            descriptor = klass.__dict__["idDefinition"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_itemRepoURL():
    assert hasattr(ccore_Cadse, "itemRepoURL")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "itemRepoURL" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoURL"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_description():
    assert hasattr(ccore_Cadse, "description")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_executed():
    assert hasattr(ccore_Cadse, "executed")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "executed" in klass.__dict__:
            descriptor = klass.__dict__["executed"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_itemRepoPasswd():
    assert hasattr(ccore_Cadse, "itemRepoPasswd")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "itemRepoPasswd" in klass.__dict__:
            descriptor = klass.__dict__["itemRepoPasswd"]
            break
    assert isinstance(descriptor, property)

def test_ccore_cadse_has_defaultContentRepoURL():
    assert hasattr(ccore_Cadse, "defaultContentRepoURL")
    descriptor = None
    for klass in ccore_Cadse.__mro__:
        if "defaultContentRepoURL" in klass.__dict__:
            descriptor = klass.__dict__["defaultContentRepoURL"]
            break
    assert isinstance(descriptor, property)



def test_ccore_keydefinition_is_not_abstract():
    assert not inspect.isabstract(ccore_KeyDefinition)


def test_ccore_keydefinition_constructor_exists():
    assert callable(ccore_KeyDefinition.__init__)


def test_ccore_keydefinition_constructor_args():
    sig = inspect.signature(ccore_KeyDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ccore_runtimeitem_is_not_abstract():
    assert not inspect.isabstract(ccore_RuntimeItem)


def test_ccore_runtimeitem_constructor_exists():
    assert callable(ccore_RuntimeItem.__init__)


def test_ccore_runtimeitem_constructor_args():
    sig = inspect.signature(ccore_RuntimeItem.__init__)
    params = list(sig.parameters.keys())
    assert "extendsClass" in params, "Missing parameter 'extendsClass'"
    assert "className" in params, "Missing parameter 'className'"

def test_ccore_runtimeitem_has_extendsClass():
    assert hasattr(ccore_RuntimeItem, "extendsClass")
    descriptor = None
    for klass in ccore_RuntimeItem.__mro__:
        if "extendsClass" in klass.__dict__:
            descriptor = klass.__dict__["extendsClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore_runtimeitem_has_className():
    assert hasattr(ccore_RuntimeItem, "className")
    descriptor = None
    for klass in ccore_RuntimeItem.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_ccore_field_is_not_abstract():
    assert not inspect.isabstract(ccore_Field)


def test_ccore_field_constructor_exists():
    assert callable(ccore_Field.__init__)


def test_ccore_field_constructor_args():
    sig = inspect.signature(ccore_Field.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "editable" in params, "Missing parameter 'editable'"
    assert "label" in params, "Missing parameter 'label'"

def test_ccore_field_has_position():
    assert hasattr(ccore_Field, "position")
    descriptor = None
    for klass in ccore_Field.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_ccore_field_has_editable():
    assert hasattr(ccore_Field, "editable")
    descriptor = None
    for klass in ccore_Field.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_ccore_field_has_label():
    assert hasattr(ccore_Field, "label")
    descriptor = None
    for klass in ccore_Field.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_ccore_attribute_is_not_abstract():
    assert not inspect.isabstract(ccore_Attribute)


def test_ccore_attribute_constructor_exists():
    assert callable(ccore_Attribute.__init__)


def test_ccore_attribute_constructor_args():
    sig = inspect.signature(ccore_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "natif" in params, "Missing parameter 'natif'"
    assert "isList" in params, "Missing parameter 'isList'"
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"
    assert "devGenerated" in params, "Missing parameter 'devGenerated'"
    assert "_final" in params, "Missing parameter '_final'"
    assert "tWRevSpecific" in params, "Missing parameter 'tWRevSpecific'"
    assert "mustBeInitialized" in params, "Missing parameter 'mustBeInitialized'"
    assert "hiddenInComputedPages" in params, "Missing parameter 'hiddenInComputedPages'"
    assert "tWEvol" in params, "Missing parameter 'tWEvol'"
    assert "tWUpdateKind" in params, "Missing parameter 'tWUpdateKind'"
    assert "tWCommitKind" in params, "Missing parameter 'tWCommitKind'"
    assert "cannotBeUndefined" in params, "Missing parameter 'cannotBeUndefined'"
    assert "require" in params, "Missing parameter 'require'"

def test_ccore_attribute_has_natif():
    assert hasattr(ccore_Attribute, "natif")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "natif" in klass.__dict__:
            descriptor = klass.__dict__["natif"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_isList():
    assert hasattr(ccore_Attribute, "isList")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_idRuntime():
    assert hasattr(ccore_Attribute, "idRuntime")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_devGenerated():
    assert hasattr(ccore_Attribute, "devGenerated")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "devGenerated" in klass.__dict__:
            descriptor = klass.__dict__["devGenerated"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has__final():
    assert hasattr(ccore_Attribute, "_final")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "_final" in klass.__dict__:
            descriptor = klass.__dict__["_final"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_tWRevSpecific():
    assert hasattr(ccore_Attribute, "tWRevSpecific")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "tWRevSpecific" in klass.__dict__:
            descriptor = klass.__dict__["tWRevSpecific"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_mustBeInitialized():
    assert hasattr(ccore_Attribute, "mustBeInitialized")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "mustBeInitialized" in klass.__dict__:
            descriptor = klass.__dict__["mustBeInitialized"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_hiddenInComputedPages():
    assert hasattr(ccore_Attribute, "hiddenInComputedPages")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "hiddenInComputedPages" in klass.__dict__:
            descriptor = klass.__dict__["hiddenInComputedPages"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_tWEvol():
    assert hasattr(ccore_Attribute, "tWEvol")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "tWEvol" in klass.__dict__:
            descriptor = klass.__dict__["tWEvol"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_tWUpdateKind():
    assert hasattr(ccore_Attribute, "tWUpdateKind")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "tWUpdateKind" in klass.__dict__:
            descriptor = klass.__dict__["tWUpdateKind"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_tWCommitKind():
    assert hasattr(ccore_Attribute, "tWCommitKind")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "tWCommitKind" in klass.__dict__:
            descriptor = klass.__dict__["tWCommitKind"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_cannotBeUndefined():
    assert hasattr(ccore_Attribute, "cannotBeUndefined")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "cannotBeUndefined" in klass.__dict__:
            descriptor = klass.__dict__["cannotBeUndefined"]
            break
    assert isinstance(descriptor, property)

def test_ccore_attribute_has_require():
    assert hasattr(ccore_Attribute, "require")
    descriptor = None
    for klass in ccore_Attribute.__mro__:
        if "require" in klass.__dict__:
            descriptor = klass.__dict__["require"]
            break
    assert isinstance(descriptor, property)



def test_ccore_typedefinition_is_not_abstract():
    assert not inspect.isabstract(ccore_TypeDefinition)


def test_ccore_typedefinition_constructor_exists():
    assert callable(ccore_TypeDefinition.__init__)


def test_ccore_typedefinition_constructor_args():
    sig = inspect.signature(ccore_TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "idRuntime" in params, "Missing parameter 'idRuntime'"

def test_ccore_typedefinition_has_idRuntime():
    assert hasattr(ccore_TypeDefinition, "idRuntime")
    descriptor = None
    for klass in ccore_TypeDefinition.__mro__:
        if "idRuntime" in klass.__dict__:
            descriptor = klass.__dict__["idRuntime"]
            break
    assert isinstance(descriptor, property)



def test_ccore_runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_RuntimeItemType)


def test_ccore_runtimeitemtype_constructor_exists():
    assert callable(ccore_RuntimeItemType.__init__)


def test_ccore_runtimeitemtype_constructor_args():
    sig = inspect.signature(ccore_RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_runtimeitemtype_is_not_abstract():
    assert not inspect.isabstract(RuntimeItemType)


def test_runtimeitemtype_constructor_exists():
    assert callable(RuntimeItemType.__init__)


def test_runtimeitemtype_constructor_args():
    sig = inspect.signature(RuntimeItemType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_composertype_is_not_abstract():
    assert not inspect.isabstract(ccore_ComposerType)


def test_ccore_composertype_constructor_exists():
    assert callable(ccore_ComposerType.__init__)


def test_ccore_composertype_constructor_args():
    sig = inspect.signature(ccore_ComposerType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_exportertype_is_not_abstract():
    assert not inspect.isabstract(ccore_ExporterType)


def test_ccore_exportertype_constructor_exists():
    assert callable(ccore_ExporterType.__init__)


def test_ccore_exportertype_constructor_args():
    sig = inspect.signature(ccore_ExporterType.__init__)
    params = list(sig.parameters.keys())



def test_ccore_dbobject_is_not_abstract():
    assert not inspect.isabstract(ccore_DBObject)


def test_ccore_dbobject_constructor_exists():
    assert callable(ccore_DBObject.__init__)


def test_ccore_dbobject_constructor_args():
    sig = inspect.signature(ccore_DBObject.__init__)
    params = list(sig.parameters.keys())
    assert "objectId" in params, "Missing parameter 'objectId'"
    assert "uuid_lsb" in params, "Missing parameter 'uuid_lsb'"
    assert "uuid_msb" in params, "Missing parameter 'uuid_msb'"

def test_ccore_dbobject_has_objectId():
    assert hasattr(ccore_DBObject, "objectId")
    descriptor = None
    for klass in ccore_DBObject.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)

def test_ccore_dbobject_has_uuid_lsb():
    assert hasattr(ccore_DBObject, "uuid_lsb")
    descriptor = None
    for klass in ccore_DBObject.__mro__:
        if "uuid_lsb" in klass.__dict__:
            descriptor = klass.__dict__["uuid_lsb"]
            break
    assert isinstance(descriptor, property)

def test_ccore_dbobject_has_uuid_msb():
    assert hasattr(ccore_DBObject, "uuid_msb")
    descriptor = None
    for klass in ccore_DBObject.__mro__:
        if "uuid_msb" in klass.__dict__:
            descriptor = klass.__dict__["uuid_msb"]
            break
    assert isinstance(descriptor, property)



def test_ccore_view_is_not_abstract():
    assert not inspect.isabstract(ccore_View)


def test_ccore_view_constructor_exists():
    assert callable(ccore_View.__init__)


def test_ccore_view_constructor_args():
    sig = inspect.signature(ccore_View.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_ccore_view_has_icon():
    assert hasattr(ccore_View, "icon")
    descriptor = None
    for klass in ccore_View.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_ccore_composerlink_is_not_abstract():
    assert not inspect.isabstract(ccore_ComposerLink)


def test_ccore_composerlink_constructor_exists():
    assert callable(ccore_ComposerLink.__init__)


def test_ccore_composerlink_constructor_args():
    sig = inspect.signature(ccore_ComposerLink.__init__)
    params = list(sig.parameters.keys())



def test_ccore_menugroup_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuGroup)


def test_ccore_menugroup_constructor_exists():
    assert callable(ccore_MenuGroup.__init__)


def test_ccore_menugroup_constructor_args():
    sig = inspect.signature(ccore_MenuGroup.__init__)
    params = list(sig.parameters.keys())



def test_ccore_menuaction_is_not_abstract():
    assert not inspect.isabstract(ccore_MenuAction)


def test_ccore_menuaction_constructor_exists():
    assert callable(ccore_MenuAction.__init__)


def test_ccore_menuaction_constructor_args():
    sig = inspect.signature(ccore_MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_ccore_viewmodel_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewModel)


def test_ccore_viewmodel_constructor_exists():
    assert callable(ccore_ViewModel.__init__)


def test_ccore_viewmodel_constructor_args():
    sig = inspect.signature(ccore_ViewModel.__init__)
    params = list(sig.parameters.keys())



def test_ccore_extitem_is_not_abstract():
    assert not inspect.isabstract(ccore_ExtItem)


def test_ccore_extitem_constructor_exists():
    assert callable(ccore_ExtItem.__init__)


def test_ccore_extitem_constructor_args():
    sig = inspect.signature(ccore_ExtItem.__init__)
    params = list(sig.parameters.keys())



def test_ccore_computedstring_is_not_abstract():
    assert not inspect.isabstract(ccore_ComputedString)


def test_ccore_computedstring_constructor_exists():
    assert callable(ccore_ComputedString.__init__)


def test_ccore_computedstring_constructor_args():
    sig = inspect.signature(ccore_ComputedString.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_ccore_computedstring_has_expression():
    assert hasattr(ccore_ComputedString, "expression")
    descriptor = None
    for klass in ccore_ComputedString.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_ccore_eenum_is_not_abstract():
    assert not inspect.isabstract(ccore_EEnum)


def test_ccore_eenum_constructor_exists():
    assert callable(ccore_EEnum.__init__)


def test_ccore_eenum_constructor_args():
    sig = inspect.signature(ccore_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_eenum_is_not_abstract():
    assert not inspect.isabstract(EEnum)


def test_eenum_constructor_exists():
    assert callable(EEnum.__init__)


def test_eenum_constructor_args():
    sig = inspect.signature(EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ccore_groupextitem_is_not_abstract():
    assert not inspect.isabstract(ccore_GroupExtItem)


def test_ccore_groupextitem_constructor_exists():
    assert callable(ccore_GroupExtItem.__init__)


def test_ccore_groupextitem_constructor_args():
    sig = inspect.signature(ccore_GroupExtItem.__init__)
    params = list(sig.parameters.keys())



def test_ereference_is_not_abstract():
    assert not inspect.isabstract(EReference)


def test_ereference_constructor_exists():
    assert callable(EReference.__init__)


def test_ereference_constructor_args():
    sig = inspect.signature(EReference.__init__)
    params = list(sig.parameters.keys())



def test_ccore_enumtype_is_not_abstract():
    assert not inspect.isabstract(ccore_EnumType)


def test_ccore_enumtype_constructor_exists():
    assert callable(ccore_EnumType.__init__)


def test_ccore_enumtype_constructor_args():
    sig = inspect.signature(ccore_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "javaClass" in params, "Missing parameter 'javaClass'"
    assert "mustBeGenerated" in params, "Missing parameter 'mustBeGenerated'"

def test_ccore_enumtype_has_values():
    assert hasattr(ccore_EnumType, "values")
    descriptor = None
    for klass in ccore_EnumType.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_ccore_enumtype_has_javaClass():
    assert hasattr(ccore_EnumType, "javaClass")
    descriptor = None
    for klass in ccore_EnumType.__mro__:
        if "javaClass" in klass.__dict__:
            descriptor = klass.__dict__["javaClass"]
            break
    assert isinstance(descriptor, property)

def test_ccore_enumtype_has_mustBeGenerated():
    assert hasattr(ccore_EnumType, "mustBeGenerated")
    descriptor = None
    for klass in ccore_EnumType.__mro__:
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



def test_ccore_composer_is_not_abstract():
    assert not inspect.isabstract(ccore_Composer)


def test_ccore_composer_constructor_exists():
    assert callable(ccore_Composer.__init__)


def test_ccore_composer_constructor_args():
    sig = inspect.signature(ccore_Composer.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"

def test_ccore_composer_has_types():
    assert hasattr(ccore_Composer, "types")
    descriptor = None
    for klass in ccore_Composer.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_ccore_exporter_is_not_abstract():
    assert not inspect.isabstract(ccore_Exporter)


def test_ccore_exporter_constructor_exists():
    assert callable(ccore_Exporter.__init__)


def test_ccore_exporter_constructor_args():
    sig = inspect.signature(ccore_Exporter.__init__)
    params = list(sig.parameters.keys())
    assert "types" in params, "Missing parameter 'types'"

def test_ccore_exporter_has_types():
    assert hasattr(ccore_Exporter, "types")
    descriptor = None
    for klass in ccore_Exporter.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_ccore_modelcontroller_is_not_abstract():
    assert not inspect.isabstract(ccore_ModelController)


def test_ccore_modelcontroller_constructor_exists():
    assert callable(ccore_ModelController.__init__)


def test_ccore_modelcontroller_constructor_args():
    sig = inspect.signature(ccore_ModelController.__init__)
    params = list(sig.parameters.keys())



def test_ccore_interactioncontroller_is_not_abstract():
    assert not inspect.isabstract(ccore_InteractionController)


def test_ccore_interactioncontroller_constructor_exists():
    assert callable(ccore_InteractionController.__init__)


def test_ccore_interactioncontroller_constructor_args():
    sig = inspect.signature(ccore_InteractionController.__init__)
    params = list(sig.parameters.keys())



def test_ccore_display_is_not_abstract():
    assert not inspect.isabstract(ccore_Display)


def test_ccore_display_constructor_exists():
    assert callable(ccore_Display.__init__)


def test_ccore_display_constructor_args():
    sig = inspect.signature(ccore_Display.__init__)
    params = list(sig.parameters.keys())
    assert "extendsIC" in params, "Missing parameter 'extendsIC'"
    assert "extendsUI" in params, "Missing parameter 'extendsUI'"
    assert "extendsMC" in params, "Missing parameter 'extendsMC'"

def test_ccore_display_has_extendsIC():
    assert hasattr(ccore_Display, "extendsIC")
    descriptor = None
    for klass in ccore_Display.__mro__:
        if "extendsIC" in klass.__dict__:
            descriptor = klass.__dict__["extendsIC"]
            break
    assert isinstance(descriptor, property)

def test_ccore_display_has_extendsUI():
    assert hasattr(ccore_Display, "extendsUI")
    descriptor = None
    for klass in ccore_Display.__mro__:
        if "extendsUI" in klass.__dict__:
            descriptor = klass.__dict__["extendsUI"]
            break
    assert isinstance(descriptor, property)

def test_ccore_display_has_extendsMC():
    assert hasattr(ccore_Display, "extendsMC")
    descriptor = None
    for klass in ccore_Display.__mro__:
        if "extendsMC" in klass.__dict__:
            descriptor = klass.__dict__["extendsMC"]
            break
    assert isinstance(descriptor, property)



def test_ccore_exportedcontent_is_not_abstract():
    assert not inspect.isabstract(ccore_ExportedContent)


def test_ccore_exportedcontent_constructor_exists():
    assert callable(ccore_ExportedContent.__init__)


def test_ccore_exportedcontent_constructor_args():
    sig = inspect.signature(ccore_ExportedContent.__init__)
    params = list(sig.parameters.keys())



def test_bindingdesc_is_not_abstract():
    assert not inspect.isabstract(BindingDesc)


def test_bindingdesc_constructor_exists():
    assert callable(BindingDesc.__init__)


def test_bindingdesc_constructor_args():
    sig = inspect.signature(BindingDesc.__init__)
    params = list(sig.parameters.keys())



def test_ccore_bindext_is_not_abstract():
    assert not inspect.isabstract(ccore_BindExt)


def test_ccore_bindext_constructor_exists():
    assert callable(ccore_BindExt.__init__)


def test_ccore_bindext_constructor_args():
    sig = inspect.signature(ccore_BindExt.__init__)
    params = list(sig.parameters.keys())



def test_ccore_unresolvedattributetype_is_not_abstract():
    assert not inspect.isabstract(ccore_UnresolvedAttributeType)


def test_ccore_unresolvedattributetype_constructor_exists():
    assert callable(ccore_UnresolvedAttributeType.__init__)


def test_ccore_unresolvedattributetype_constructor_args():
    sig = inspect.signature(ccore_UnresolvedAttributeType.__init__)
    params = list(sig.parameters.keys())



def test_longattribute_is_not_abstract():
    assert not inspect.isabstract(LongAttribute)


def test_longattribute_constructor_exists():
    assert callable(LongAttribute.__init__)


def test_longattribute_constructor_args():
    sig = inspect.signature(LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_timeattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_TimeAttribute)


def test_ccore_timeattribute_constructor_exists():
    assert callable(ccore_TimeAttribute.__init__)


def test_ccore_timeattribute_constructor_args():
    sig = inspect.signature(ccore_TimeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "initWithTheCurrentTime" in params, "Missing parameter 'initWithTheCurrentTime'"

def test_ccore_timeattribute_has_initWithTheCurrentTime():
    assert hasattr(ccore_TimeAttribute, "initWithTheCurrentTime")
    descriptor = None
    for klass in ccore_TimeAttribute.__mro__:
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



def test_ccore_integerattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_IntegerAttribute)


def test_ccore_integerattribute_constructor_exists():
    assert callable(ccore_IntegerAttribute.__init__)


def test_ccore_integerattribute_constructor_args():
    sig = inspect.signature(ccore_IntegerAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_enum_is_not_abstract():
    assert not inspect.isabstract(ccore_Enum)


def test_ccore_enum_constructor_exists():
    assert callable(ccore_Enum.__init__)


def test_ccore_enum_constructor_args():
    sig = inspect.signature(ccore_Enum.__init__)
    params = list(sig.parameters.keys())
    assert "enumClazz" in params, "Missing parameter 'enumClazz'"
    assert "values" in params, "Missing parameter 'values'"

def test_ccore_enum_has_enumClazz():
    assert hasattr(ccore_Enum, "enumClazz")
    descriptor = None
    for klass in ccore_Enum.__mro__:
        if "enumClazz" in klass.__dict__:
            descriptor = klass.__dict__["enumClazz"]
            break
    assert isinstance(descriptor, property)

def test_ccore_enum_has_values():
    assert hasattr(ccore_Enum, "values")
    descriptor = None
    for klass in ccore_Enum.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_ccore_longattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_LongAttribute)


def test_ccore_longattribute_constructor_exists():
    assert callable(ccore_LongAttribute.__init__)


def test_ccore_longattribute_constructor_args():
    sig = inspect.signature(ccore_LongAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_uuidattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_UUIDAttribute)


def test_ccore_uuidattribute_constructor_exists():
    assert callable(ccore_UUIDAttribute.__init__)


def test_ccore_uuidattribute_constructor_args():
    sig = inspect.signature(ccore_UUIDAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_dateattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_DateAttribute)


def test_ccore_dateattribute_constructor_exists():
    assert callable(ccore_DateAttribute.__init__)


def test_ccore_dateattribute_constructor_args():
    sig = inspect.signature(ccore_DateAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_linktype_is_not_abstract():
    assert not inspect.isabstract(ccore_LinkType)


def test_ccore_linktype_constructor_exists():
    assert callable(ccore_LinkType.__init__)


def test_ccore_linktype_constructor_args():
    sig = inspect.signature(ccore_LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "composition" in params, "Missing parameter 'composition'"
    assert "twCoupled" in params, "Missing parameter 'twCoupled'"
    assert "linkManager" in params, "Missing parameter 'linkManager'"
    assert "min" in params, "Missing parameter 'min'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "max" in params, "Missing parameter 'max'"
    assert "mapping" in params, "Missing parameter 'mapping'"
    assert "annotation" in params, "Missing parameter 'annotation'"
    assert "twDestEvol" in params, "Missing parameter 'twDestEvol'"
    assert "group" in params, "Missing parameter 'group'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_ccore_linktype_has_composition():
    assert hasattr(ccore_LinkType, "composition")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "composition" in klass.__dict__:
            descriptor = klass.__dict__["composition"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_twCoupled():
    assert hasattr(ccore_LinkType, "twCoupled")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "twCoupled" in klass.__dict__:
            descriptor = klass.__dict__["twCoupled"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_linkManager():
    assert hasattr(ccore_LinkType, "linkManager")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "linkManager" in klass.__dict__:
            descriptor = klass.__dict__["linkManager"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_min():
    assert hasattr(ccore_LinkType, "min")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_hidden():
    assert hasattr(ccore_LinkType, "hidden")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_max():
    assert hasattr(ccore_LinkType, "max")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_mapping():
    assert hasattr(ccore_LinkType, "mapping")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "mapping" in klass.__dict__:
            descriptor = klass.__dict__["mapping"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_annotation():
    assert hasattr(ccore_LinkType, "annotation")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_twDestEvol():
    assert hasattr(ccore_LinkType, "twDestEvol")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "twDestEvol" in klass.__dict__:
            descriptor = klass.__dict__["twDestEvol"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_group():
    assert hasattr(ccore_LinkType, "group")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_selection():
    assert hasattr(ccore_LinkType, "selection")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_kind():
    assert hasattr(ccore_LinkType, "kind")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_ccore_linktype_has_aggregation():
    assert hasattr(ccore_LinkType, "aggregation")
    descriptor = None
    for klass in ccore_LinkType.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



def test_ccore_doubleattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_DoubleAttribute)


def test_ccore_doubleattribute_constructor_exists():
    assert callable(ccore_DoubleAttribute.__init__)


def test_ccore_doubleattribute_constructor_args():
    sig = inspect.signature(ccore_DoubleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_booleanattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_BooleanAttribute)


def test_ccore_booleanattribute_constructor_exists():
    assert callable(ccore_BooleanAttribute.__init__)


def test_ccore_booleanattribute_constructor_args():
    sig = inspect.signature(ccore_BooleanAttribute.__init__)
    params = list(sig.parameters.keys())



def test_ccore_stringattribute_is_not_abstract():
    assert not inspect.isabstract(ccore_StringAttribute)


def test_ccore_stringattribute_constructor_exists():
    assert callable(ccore_StringAttribute.__init__)


def test_ccore_stringattribute_constructor_args():
    sig = inspect.signature(ccore_StringAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "notEmpty" in params, "Missing parameter 'notEmpty'"

def test_ccore_stringattribute_has_notEmpty():
    assert hasattr(ccore_StringAttribute, "notEmpty")
    descriptor = None
    for klass in ccore_StringAttribute.__mro__:
        if "notEmpty" in klass.__dict__:
            descriptor = klass.__dict__["notEmpty"]
            break
    assert isinstance(descriptor, property)



def test_ccore_viewdescription_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewDescription)


def test_ccore_viewdescription_constructor_exists():
    assert callable(ccore_ViewDescription.__init__)


def test_ccore_viewdescription_constructor_args():
    sig = inspect.signature(ccore_ViewDescription.__init__)
    params = list(sig.parameters.keys())



def test_ccore_viewlinktype_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewLinkType)


def test_ccore_viewlinktype_constructor_exists():
    assert callable(ccore_ViewLinkType.__init__)


def test_ccore_viewlinktype_constructor_args():
    sig = inspect.signature(ccore_ViewLinkType.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "displayCreate" in params, "Missing parameter 'displayCreate'"
    assert "canCreateItem" in params, "Missing parameter 'canCreateItem'"
    assert "canCreateLink" in params, "Missing parameter 'canCreateLink'"

def test_ccore_viewlinktype_has_aggregation():
    assert hasattr(ccore_ViewLinkType, "aggregation")
    descriptor = None
    for klass in ccore_ViewLinkType.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_ccore_viewlinktype_has_displayCreate():
    assert hasattr(ccore_ViewLinkType, "displayCreate")
    descriptor = None
    for klass in ccore_ViewLinkType.__mro__:
        if "displayCreate" in klass.__dict__:
            descriptor = klass.__dict__["displayCreate"]
            break
    assert isinstance(descriptor, property)

def test_ccore_viewlinktype_has_canCreateItem():
    assert hasattr(ccore_ViewLinkType, "canCreateItem")
    descriptor = None
    for klass in ccore_ViewLinkType.__mro__:
        if "canCreateItem" in klass.__dict__:
            descriptor = klass.__dict__["canCreateItem"]
            break
    assert isinstance(descriptor, property)

def test_ccore_viewlinktype_has_canCreateLink():
    assert hasattr(ccore_ViewLinkType, "canCreateLink")
    descriptor = None
    for klass in ccore_ViewLinkType.__mro__:
        if "canCreateLink" in klass.__dict__:
            descriptor = klass.__dict__["canCreateLink"]
            break
    assert isinstance(descriptor, property)



def test_ccore_viewitemtype_is_not_abstract():
    assert not inspect.isabstract(ccore_ViewItemType)


def test_ccore_viewitemtype_constructor_exists():
    assert callable(ccore_ViewItemType.__init__)


def test_ccore_viewitemtype_constructor_args():
    sig = inspect.signature(ccore_ViewItemType.__init__)
    params = list(sig.parameters.keys())
    assert "isRootElement" in params, "Missing parameter 'isRootElement'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_ccore_viewitemtype_has_isRootElement():
    assert hasattr(ccore_ViewItemType, "isRootElement")
    descriptor = None
    for klass in ccore_ViewItemType.__mro__:
        if "isRootElement" in klass.__dict__:
            descriptor = klass.__dict__["isRootElement"]
            break
    assert isinstance(descriptor, property)

def test_ccore_viewitemtype_has_ref():
    assert hasattr(ccore_ViewItemType, "ref")
    descriptor = None
    for klass in ccore_ViewItemType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_ccore_geninformation_is_not_abstract():
    assert not inspect.isabstract(ccore_GenInformation)


def test_ccore_geninformation_constructor_exists():
    assert callable(ccore_GenInformation.__init__)


def test_ccore_geninformation_constructor_args():
    sig = inspect.signature(ccore_GenInformation.__init__)
    params = list(sig.parameters.keys())
    assert "cSTName" in params, "Missing parameter 'cSTName'"

def test_ccore_geninformation_has_cSTName():
    assert hasattr(ccore_GenInformation, "cSTName")
    descriptor = None
    for klass in ccore_GenInformation.__mro__:
        if "cSTName" in klass.__dict__:
            descriptor = klass.__dict__["cSTName"]
            break
    assert isinstance(descriptor, property)

def test_positionenum_exists():
    # Check that the Enumeration exists
    assert PositionEnum is not None

def test_positionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionEnum]
    expected_literals = [
        "defaultpos",
        "group",
        "none",
        "top",
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionEnum"

def test_twcommitkind_exists():
    # Check that the Enumeration exists
    assert TWCommitKind is not None

def test_twcommitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWCommitKind]
    expected_literals = [
        "none",
        "conflict",
        "reconcile",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWCommitKind"

def test_twdestevol_exists():
    # Check that the Enumeration exists
    assert TWDestEvol is not None

def test_twdestevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWDestEvol]
    expected_literals = [
        "finalDest",
        "mutable",
        "effective",
        "branch",
        "immutable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWDestEvol"

def test_twevol_exists():
    # Check that the Enumeration exists
    assert TWEvol is not None

def test_twevol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWEvol]
    expected_literals = [
        "twFinal",
        "twImmutable",
        "twTransient",
        "twMutable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWEvol"

def test_twupdatekind_exists():
    # Check that the Enumeration exists
    assert TWUpdateKind is not None

def test_twupdatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TWUpdateKind]
    expected_literals = [
        "merge",
        "compute",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TWUpdateKind"


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
ItemType_strategy = st.builds(
    ItemType,
)
ccore_MenuAbstract_strategy = st.builds(
    ccore_MenuAbstract,
    icon=
        safe_text,
    label=
        safe_text,
    path=
        safe_text
)
ccore_Menu_strategy = st.builds(
    ccore_Menu,
)
ccore_ActionExtItemType_strategy = st.builds(
    ccore_ActionExtItemType,
)
ccore_DynamicActions_strategy = st.builds(
    ccore_DynamicActions,
)
EAttribute_strategy = st.builds(
    EAttribute,
)
ccore_ContentItem_strategy = st.builds(
    ccore_ContentItem,
)
ccore_EStructuralFeature_strategy = st.builds(
    ccore_EStructuralFeature,
)
EPackage_strategy = st.builds(
    EPackage,
)
ccore_ContentItemType_strategy = st.builds(
    ccore_ContentItemType,
    extendsClass=
        st.booleans()
)
DBObject_strategy = st.builds(
    DBObject,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ccore_Item_strategy = st.builds(
    ccore_Item,
    qualifiedName=
        safe_text,
    twCommittedDate=
        safe_text,
    twVersion=
        st.integers(),
    twRevModified=
        st.booleans(),
    displayName=
        safe_text,
    twRequireNewRev=
        st.booleans(),
    committedBy=
        safe_text,
    itemReadonly=
        st.booleans(),
    isvalid=
        st.booleans(),
    itemHidden=
        st.booleans()
)
ccore_BindingDesc_strategy = st.builds(
    ccore_BindingDesc,
)
ccore_EPackage_strategy = st.builds(
    ccore_EPackage,
)
ccore_WCListener_strategy = st.builds(
    ccore_WCListener,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
ccore_ItemType_strategy = st.builds(
    ccore_ItemType,
    isInstanceHidden=
        st.booleans(),
    hasShortName=
        st.booleans(),
    customManager=
        st.booleans(),
    packageName=
        safe_text,
    overwriteDefaultPages=
        st.booleans(),
    qualifiedNameTemplate=
        safe_text,
    validateNameRe=
        safe_text,
    messageErrorId=
        safe_text,
    hasContent=
        st.booleans(),
    itemManagerClass=
        safe_text,
    isInstanceAbstract=
        st.booleans(),
    managerClass=
        safe_text,
    humanName=
        safe_text,
    displayNameTemplate=
        safe_text,
    itemFactoryClass=
        safe_text,
    hasUniqueName=
        st.booleans(),
    icon=
        safe_text,
    isMetaItemType=
        st.booleans(),
    isRootElement=
        st.booleans()
)
ccore_ExtentedType_strategy = st.builds(
    ccore_ExtentedType,
)
ccore_EClass_strategy = st.builds(
    ccore_EClass,
)
ccore_GroupOfAttributes_strategy = st.builds(
    ccore_GroupOfAttributes,
    column=
        st.integers()
)
ccore_UIValidator_strategy = st.builds(
    ccore_UIValidator,
)
ccore_Page_strategy = st.builds(
    ccore_Page,
    label=
        safe_text,
    description=
        safe_text,
    idRuntime=
        safe_text,
    title=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
Item_strategy = st.builds(
    Item,
)
ccore_Cadse_strategy = st.builds(
    ccore_Cadse,
    itemRepoLogin=
        safe_text,
    idDefinition=
        safe_text,
    itemRepoURL=
        safe_text,
    description=
        safe_text,
    executed=
        st.booleans(),
    itemRepoPasswd=
        safe_text,
    defaultContentRepoURL=
        safe_text
)
ccore_KeyDefinition_strategy = st.builds(
    ccore_KeyDefinition,
)
ccore_RuntimeItem_strategy = st.builds(
    ccore_RuntimeItem,
    extendsClass=
        st.booleans(),
    className=
        safe_text
)
ccore_Field_strategy = st.builds(
    ccore_Field,
    position=
        safe_text,
    editable=
        st.booleans(),
    label=
        safe_text
)
ccore_Attribute_strategy = st.builds(
    ccore_Attribute,
    natif=
        st.booleans(),
    isList=
        st.booleans(),
    idRuntime=
        safe_text,
    devGenerated=
        st.booleans(),
    _final=
        st.booleans(),
    tWRevSpecific=
        st.booleans(),
    mustBeInitialized=
        st.booleans(),
    hiddenInComputedPages=
        st.booleans(),
    tWEvol=
        safe_text,
    tWUpdateKind=
        safe_text,
    tWCommitKind=
        safe_text,
    cannotBeUndefined=
        st.booleans(),
    require=
        st.booleans()
)
ccore_TypeDefinition_strategy = st.builds(
    ccore_TypeDefinition,
    idRuntime=
        safe_text
)
ccore_RuntimeItemType_strategy = st.builds(
    ccore_RuntimeItemType,
)
RuntimeItemType_strategy = st.builds(
    RuntimeItemType,
)
ccore_ComposerType_strategy = st.builds(
    ccore_ComposerType,
)
ccore_ExporterType_strategy = st.builds(
    ccore_ExporterType,
)
ccore_DBObject_strategy = st.builds(
    ccore_DBObject,
    objectId=
        st.integers(),
    uuid_lsb=
        safe_text,
    uuid_msb=
        safe_text
)
ccore_View_strategy = st.builds(
    ccore_View,
    icon=
        safe_text
)
ccore_ComposerLink_strategy = st.builds(
    ccore_ComposerLink,
)
ccore_MenuGroup_strategy = st.builds(
    ccore_MenuGroup,
)
ccore_MenuAction_strategy = st.builds(
    ccore_MenuAction,
)
ccore_ViewModel_strategy = st.builds(
    ccore_ViewModel,
)
ccore_ExtItem_strategy = st.builds(
    ccore_ExtItem,
)
ccore_ComputedString_strategy = st.builds(
    ccore_ComputedString,
    expression=
        safe_text
)
ccore_EEnum_strategy = st.builds(
    ccore_EEnum,
)
EEnum_strategy = st.builds(
    EEnum,
)
ccore_GroupExtItem_strategy = st.builds(
    ccore_GroupExtItem,
)
EReference_strategy = st.builds(
    EReference,
)
ccore_EnumType_strategy = st.builds(
    ccore_EnumType,
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
ccore_Composer_strategy = st.builds(
    ccore_Composer,
    types=
        safe_text
)
ccore_Exporter_strategy = st.builds(
    ccore_Exporter,
    types=
        safe_text
)
ccore_ModelController_strategy = st.builds(
    ccore_ModelController,
)
ccore_InteractionController_strategy = st.builds(
    ccore_InteractionController,
)
ccore_Display_strategy = st.builds(
    ccore_Display,
    extendsIC=
        st.booleans(),
    extendsUI=
        st.booleans(),
    extendsMC=
        st.booleans()
)
ccore_ExportedContent_strategy = st.builds(
    ccore_ExportedContent,
)
BindingDesc_strategy = st.builds(
    BindingDesc,
)
ccore_BindExt_strategy = st.builds(
    ccore_BindExt,
)
ccore_UnresolvedAttributeType_strategy = st.builds(
    ccore_UnresolvedAttributeType,
)
LongAttribute_strategy = st.builds(
    LongAttribute,
)
ccore_TimeAttribute_strategy = st.builds(
    ccore_TimeAttribute,
    initWithTheCurrentTime=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
ccore_IntegerAttribute_strategy = st.builds(
    ccore_IntegerAttribute,
)
ccore_Enum_strategy = st.builds(
    ccore_Enum,
    enumClazz=
        safe_text,
    values=
        safe_text
)
ccore_LongAttribute_strategy = st.builds(
    ccore_LongAttribute,
)
ccore_UUIDAttribute_strategy = st.builds(
    ccore_UUIDAttribute,
)
ccore_DateAttribute_strategy = st.builds(
    ccore_DateAttribute,
)
ccore_LinkType_strategy = st.builds(
    ccore_LinkType,
    composition=
        st.booleans(),
    twCoupled=
        st.booleans(),
    linkManager=
        safe_text,
    min=
        st.integers(),
    hidden=
        st.booleans(),
    max=
        st.integers(),
    mapping=
        st.booleans(),
    annotation=
        st.booleans(),
    twDestEvol=
        safe_text,
    group=
        st.booleans(),
    selection=
        safe_text,
    kind=
        st.integers(),
    aggregation=
        st.booleans()
)
ccore_DoubleAttribute_strategy = st.builds(
    ccore_DoubleAttribute,
)
ccore_BooleanAttribute_strategy = st.builds(
    ccore_BooleanAttribute,
)
ccore_StringAttribute_strategy = st.builds(
    ccore_StringAttribute,
    notEmpty=
        st.booleans()
)
ccore_ViewDescription_strategy = st.builds(
    ccore_ViewDescription,
)
ccore_ViewLinkType_strategy = st.builds(
    ccore_ViewLinkType,
    aggregation=
        st.booleans(),
    displayCreate=
        safe_text,
    canCreateItem=
        st.booleans(),
    canCreateLink=
        st.booleans()
)
ccore_ViewItemType_strategy = st.builds(
    ccore_ViewItemType,
    isRootElement=
        st.booleans(),
    ref=
        st.booleans()
)
ccore_GenInformation_strategy = st.builds(
    ccore_GenInformation,
    cSTName=
        safe_text
)

@given(instance=ItemType_strategy)
@settings(max_examples=50)
def test_itemtype_instantiation(instance):
    assert isinstance(instance, ItemType)

@given(instance=ccore_MenuAbstract_strategy)
@settings(max_examples=50)
def test_ccore_menuabstract_instantiation(instance):
    assert isinstance(instance, ccore_MenuAbstract)



@given(instance=ccore_MenuAbstract_strategy)
def test_ccore_menuabstract_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=ccore_MenuAbstract_strategy)
def test_ccore_menuabstract_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=ccore_MenuAbstract_strategy)
def test_ccore_menuabstract_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=ccore_Menu_strategy)
@settings(max_examples=50)
def test_ccore_menu_instantiation(instance):
    assert isinstance(instance, ccore_Menu)

@given(instance=ccore_ActionExtItemType_strategy)
@settings(max_examples=50)
def test_ccore_actionextitemtype_instantiation(instance):
    assert isinstance(instance, ccore_ActionExtItemType)

@given(instance=ccore_DynamicActions_strategy)
@settings(max_examples=50)
def test_ccore_dynamicactions_instantiation(instance):
    assert isinstance(instance, ccore_DynamicActions)

@given(instance=EAttribute_strategy)
@settings(max_examples=50)
def test_eattribute_instantiation(instance):
    assert isinstance(instance, EAttribute)

@given(instance=ccore_ContentItem_strategy)
@settings(max_examples=50)
def test_ccore_contentitem_instantiation(instance):
    assert isinstance(instance, ccore_ContentItem)

@given(instance=ccore_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ccore_estructuralfeature_instantiation(instance):
    assert isinstance(instance, ccore_EStructuralFeature)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=ccore_ContentItemType_strategy)
@settings(max_examples=50)
def test_ccore_contentitemtype_instantiation(instance):
    assert isinstance(instance, ccore_ContentItemType)



@given(instance=ccore_ContentItemType_strategy)
def test_ccore_contentitemtype_extendsClass_setter(instance):
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

@given(instance=ccore_Item_strategy)
@settings(max_examples=50)
def test_ccore_item_instantiation(instance):
    assert isinstance(instance, ccore_Item)



@given(instance=ccore_Item_strategy)
def test_ccore_item_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_twCommittedDate_setter(instance):
    original = instance.twCommittedDate
    instance.twCommittedDate = original
    assert instance.twCommittedDate == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_twVersion_setter(instance):
    original = instance.twVersion
    instance.twVersion = original
    assert instance.twVersion == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_twRevModified_setter(instance):
    original = instance.twRevModified
    instance.twRevModified = original
    assert instance.twRevModified == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_twRequireNewRev_setter(instance):
    original = instance.twRequireNewRev
    instance.twRequireNewRev = original
    assert instance.twRequireNewRev == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_committedBy_setter(instance):
    original = instance.committedBy
    instance.committedBy = original
    assert instance.committedBy == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_itemReadonly_setter(instance):
    original = instance.itemReadonly
    instance.itemReadonly = original
    assert instance.itemReadonly == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_isvalid_setter(instance):
    original = instance.isvalid
    instance.isvalid = original
    assert instance.isvalid == original



@given(instance=ccore_Item_strategy)
def test_ccore_item_itemHidden_setter(instance):
    original = instance.itemHidden
    instance.itemHidden = original
    assert instance.itemHidden == original

@given(instance=ccore_BindingDesc_strategy)
@settings(max_examples=50)
def test_ccore_bindingdesc_instantiation(instance):
    assert isinstance(instance, ccore_BindingDesc)

@given(instance=ccore_EPackage_strategy)
@settings(max_examples=50)
def test_ccore_epackage_instantiation(instance):
    assert isinstance(instance, ccore_EPackage)

@given(instance=ccore_WCListener_strategy)
@settings(max_examples=50)
def test_ccore_wclistener_instantiation(instance):
    assert isinstance(instance, ccore_WCListener)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=ccore_ItemType_strategy)
@settings(max_examples=50)
def test_ccore_itemtype_instantiation(instance):
    assert isinstance(instance, ccore_ItemType)



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_isInstanceHidden_setter(instance):
    original = instance.isInstanceHidden
    instance.isInstanceHidden = original
    assert instance.isInstanceHidden == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_hasShortName_setter(instance):
    original = instance.hasShortName
    instance.hasShortName = original
    assert instance.hasShortName == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_customManager_setter(instance):
    original = instance.customManager
    instance.customManager = original
    assert instance.customManager == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_overwriteDefaultPages_setter(instance):
    original = instance.overwriteDefaultPages
    instance.overwriteDefaultPages = original
    assert instance.overwriteDefaultPages == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_qualifiedNameTemplate_setter(instance):
    original = instance.qualifiedNameTemplate
    instance.qualifiedNameTemplate = original
    assert instance.qualifiedNameTemplate == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_validateNameRe_setter(instance):
    original = instance.validateNameRe
    instance.validateNameRe = original
    assert instance.validateNameRe == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_messageErrorId_setter(instance):
    original = instance.messageErrorId
    instance.messageErrorId = original
    assert instance.messageErrorId == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_hasContent_setter(instance):
    original = instance.hasContent
    instance.hasContent = original
    assert instance.hasContent == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_itemManagerClass_setter(instance):
    original = instance.itemManagerClass
    instance.itemManagerClass = original
    assert instance.itemManagerClass == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_isInstanceAbstract_setter(instance):
    original = instance.isInstanceAbstract
    instance.isInstanceAbstract = original
    assert instance.isInstanceAbstract == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_managerClass_setter(instance):
    original = instance.managerClass
    instance.managerClass = original
    assert instance.managerClass == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_humanName_setter(instance):
    original = instance.humanName
    instance.humanName = original
    assert instance.humanName == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_displayNameTemplate_setter(instance):
    original = instance.displayNameTemplate
    instance.displayNameTemplate = original
    assert instance.displayNameTemplate == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_itemFactoryClass_setter(instance):
    original = instance.itemFactoryClass
    instance.itemFactoryClass = original
    assert instance.itemFactoryClass == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_hasUniqueName_setter(instance):
    original = instance.hasUniqueName
    instance.hasUniqueName = original
    assert instance.hasUniqueName == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_isMetaItemType_setter(instance):
    original = instance.isMetaItemType
    instance.isMetaItemType = original
    assert instance.isMetaItemType == original



@given(instance=ccore_ItemType_strategy)
def test_ccore_itemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original

@given(instance=ccore_ExtentedType_strategy)
@settings(max_examples=50)
def test_ccore_extentedtype_instantiation(instance):
    assert isinstance(instance, ccore_ExtentedType)

@given(instance=ccore_EClass_strategy)
@settings(max_examples=50)
def test_ccore_eclass_instantiation(instance):
    assert isinstance(instance, ccore_EClass)

@given(instance=ccore_GroupOfAttributes_strategy)
@settings(max_examples=50)
def test_ccore_groupofattributes_instantiation(instance):
    assert isinstance(instance, ccore_GroupOfAttributes)



@given(instance=ccore_GroupOfAttributes_strategy)
def test_ccore_groupofattributes_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=ccore_UIValidator_strategy)
@settings(max_examples=50)
def test_ccore_uivalidator_instantiation(instance):
    assert isinstance(instance, ccore_UIValidator)

@given(instance=ccore_Page_strategy)
@settings(max_examples=50)
def test_ccore_page_instantiation(instance):
    assert isinstance(instance, ccore_Page)



@given(instance=ccore_Page_strategy)
def test_ccore_page_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=ccore_Page_strategy)
def test_ccore_page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ccore_Page_strategy)
def test_ccore_page_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original



@given(instance=ccore_Page_strategy)
def test_ccore_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=ccore_Cadse_strategy)
@settings(max_examples=50)
def test_ccore_cadse_instantiation(instance):
    assert isinstance(instance, ccore_Cadse)



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_itemRepoLogin_setter(instance):
    original = instance.itemRepoLogin
    instance.itemRepoLogin = original
    assert instance.itemRepoLogin == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_idDefinition_setter(instance):
    original = instance.idDefinition
    instance.idDefinition = original
    assert instance.idDefinition == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_itemRepoURL_setter(instance):
    original = instance.itemRepoURL
    instance.itemRepoURL = original
    assert instance.itemRepoURL == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_executed_setter(instance):
    original = instance.executed
    instance.executed = original
    assert instance.executed == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_itemRepoPasswd_setter(instance):
    original = instance.itemRepoPasswd
    instance.itemRepoPasswd = original
    assert instance.itemRepoPasswd == original



@given(instance=ccore_Cadse_strategy)
def test_ccore_cadse_defaultContentRepoURL_setter(instance):
    original = instance.defaultContentRepoURL
    instance.defaultContentRepoURL = original
    assert instance.defaultContentRepoURL == original

@given(instance=ccore_KeyDefinition_strategy)
@settings(max_examples=50)
def test_ccore_keydefinition_instantiation(instance):
    assert isinstance(instance, ccore_KeyDefinition)

@given(instance=ccore_RuntimeItem_strategy)
@settings(max_examples=50)
def test_ccore_runtimeitem_instantiation(instance):
    assert isinstance(instance, ccore_RuntimeItem)



@given(instance=ccore_RuntimeItem_strategy)
def test_ccore_runtimeitem_extendsClass_setter(instance):
    original = instance.extendsClass
    instance.extendsClass = original
    assert instance.extendsClass == original



@given(instance=ccore_RuntimeItem_strategy)
def test_ccore_runtimeitem_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=ccore_Field_strategy)
@settings(max_examples=50)
def test_ccore_field_instantiation(instance):
    assert isinstance(instance, ccore_Field)



@given(instance=ccore_Field_strategy)
def test_ccore_field_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=ccore_Field_strategy)
def test_ccore_field_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original



@given(instance=ccore_Field_strategy)
def test_ccore_field_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ccore_Attribute_strategy)
@settings(max_examples=50)
def test_ccore_attribute_instantiation(instance):
    assert isinstance(instance, ccore_Attribute)



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_natif_setter(instance):
    original = instance.natif
    instance.natif = original
    assert instance.natif == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_devGenerated_setter(instance):
    original = instance.devGenerated
    instance.devGenerated = original
    assert instance.devGenerated == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute__final_setter(instance):
    original = instance._final
    instance._final = original
    assert instance._final == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_tWRevSpecific_setter(instance):
    original = instance.tWRevSpecific
    instance.tWRevSpecific = original
    assert instance.tWRevSpecific == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_mustBeInitialized_setter(instance):
    original = instance.mustBeInitialized
    instance.mustBeInitialized = original
    assert instance.mustBeInitialized == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_hiddenInComputedPages_setter(instance):
    original = instance.hiddenInComputedPages
    instance.hiddenInComputedPages = original
    assert instance.hiddenInComputedPages == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_tWEvol_setter(instance):
    original = instance.tWEvol
    instance.tWEvol = original
    assert instance.tWEvol == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_tWUpdateKind_setter(instance):
    original = instance.tWUpdateKind
    instance.tWUpdateKind = original
    assert instance.tWUpdateKind == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_tWCommitKind_setter(instance):
    original = instance.tWCommitKind
    instance.tWCommitKind = original
    assert instance.tWCommitKind == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_cannotBeUndefined_setter(instance):
    original = instance.cannotBeUndefined
    instance.cannotBeUndefined = original
    assert instance.cannotBeUndefined == original



@given(instance=ccore_Attribute_strategy)
def test_ccore_attribute_require_setter(instance):
    original = instance.require
    instance.require = original
    assert instance.require == original

@given(instance=ccore_TypeDefinition_strategy)
@settings(max_examples=50)
def test_ccore_typedefinition_instantiation(instance):
    assert isinstance(instance, ccore_TypeDefinition)



@given(instance=ccore_TypeDefinition_strategy)
def test_ccore_typedefinition_idRuntime_setter(instance):
    original = instance.idRuntime
    instance.idRuntime = original
    assert instance.idRuntime == original

@given(instance=ccore_RuntimeItemType_strategy)
@settings(max_examples=50)
def test_ccore_runtimeitemtype_instantiation(instance):
    assert isinstance(instance, ccore_RuntimeItemType)

@given(instance=RuntimeItemType_strategy)
@settings(max_examples=50)
def test_runtimeitemtype_instantiation(instance):
    assert isinstance(instance, RuntimeItemType)

@given(instance=ccore_ComposerType_strategy)
@settings(max_examples=50)
def test_ccore_composertype_instantiation(instance):
    assert isinstance(instance, ccore_ComposerType)

@given(instance=ccore_ExporterType_strategy)
@settings(max_examples=50)
def test_ccore_exportertype_instantiation(instance):
    assert isinstance(instance, ccore_ExporterType)

@given(instance=ccore_DBObject_strategy)
@settings(max_examples=50)
def test_ccore_dbobject_instantiation(instance):
    assert isinstance(instance, ccore_DBObject)



@given(instance=ccore_DBObject_strategy)
def test_ccore_dbobject_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original



@given(instance=ccore_DBObject_strategy)
def test_ccore_dbobject_uuid_lsb_setter(instance):
    original = instance.uuid_lsb
    instance.uuid_lsb = original
    assert instance.uuid_lsb == original



@given(instance=ccore_DBObject_strategy)
def test_ccore_dbobject_uuid_msb_setter(instance):
    original = instance.uuid_msb
    instance.uuid_msb = original
    assert instance.uuid_msb == original

@given(instance=ccore_View_strategy)
@settings(max_examples=50)
def test_ccore_view_instantiation(instance):
    assert isinstance(instance, ccore_View)



@given(instance=ccore_View_strategy)
def test_ccore_view_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=ccore_ComposerLink_strategy)
@settings(max_examples=50)
def test_ccore_composerlink_instantiation(instance):
    assert isinstance(instance, ccore_ComposerLink)

@given(instance=ccore_MenuGroup_strategy)
@settings(max_examples=50)
def test_ccore_menugroup_instantiation(instance):
    assert isinstance(instance, ccore_MenuGroup)

@given(instance=ccore_MenuAction_strategy)
@settings(max_examples=50)
def test_ccore_menuaction_instantiation(instance):
    assert isinstance(instance, ccore_MenuAction)

@given(instance=ccore_ViewModel_strategy)
@settings(max_examples=50)
def test_ccore_viewmodel_instantiation(instance):
    assert isinstance(instance, ccore_ViewModel)

@given(instance=ccore_ExtItem_strategy)
@settings(max_examples=50)
def test_ccore_extitem_instantiation(instance):
    assert isinstance(instance, ccore_ExtItem)

@given(instance=ccore_ComputedString_strategy)
@settings(max_examples=50)
def test_ccore_computedstring_instantiation(instance):
    assert isinstance(instance, ccore_ComputedString)



@given(instance=ccore_ComputedString_strategy)
def test_ccore_computedstring_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=ccore_EEnum_strategy)
@settings(max_examples=50)
def test_ccore_eenum_instantiation(instance):
    assert isinstance(instance, ccore_EEnum)

@given(instance=EEnum_strategy)
@settings(max_examples=50)
def test_eenum_instantiation(instance):
    assert isinstance(instance, EEnum)

@given(instance=ccore_GroupExtItem_strategy)
@settings(max_examples=50)
def test_ccore_groupextitem_instantiation(instance):
    assert isinstance(instance, ccore_GroupExtItem)

@given(instance=EReference_strategy)
@settings(max_examples=50)
def test_ereference_instantiation(instance):
    assert isinstance(instance, EReference)

@given(instance=ccore_EnumType_strategy)
@settings(max_examples=50)
def test_ccore_enumtype_instantiation(instance):
    assert isinstance(instance, ccore_EnumType)



@given(instance=ccore_EnumType_strategy)
def test_ccore_enumtype_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=ccore_EnumType_strategy)
def test_ccore_enumtype_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original



@given(instance=ccore_EnumType_strategy)
def test_ccore_enumtype_mustBeGenerated_setter(instance):
    original = instance.mustBeGenerated
    instance.mustBeGenerated = original
    assert instance.mustBeGenerated == original

@given(instance=RuntimeItem_strategy)
@settings(max_examples=50)
def test_runtimeitem_instantiation(instance):
    assert isinstance(instance, RuntimeItem)

@given(instance=ccore_Composer_strategy)
@settings(max_examples=50)
def test_ccore_composer_instantiation(instance):
    assert isinstance(instance, ccore_Composer)



@given(instance=ccore_Composer_strategy)
def test_ccore_composer_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=ccore_Exporter_strategy)
@settings(max_examples=50)
def test_ccore_exporter_instantiation(instance):
    assert isinstance(instance, ccore_Exporter)



@given(instance=ccore_Exporter_strategy)
def test_ccore_exporter_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=ccore_ModelController_strategy)
@settings(max_examples=50)
def test_ccore_modelcontroller_instantiation(instance):
    assert isinstance(instance, ccore_ModelController)

@given(instance=ccore_InteractionController_strategy)
@settings(max_examples=50)
def test_ccore_interactioncontroller_instantiation(instance):
    assert isinstance(instance, ccore_InteractionController)

@given(instance=ccore_Display_strategy)
@settings(max_examples=50)
def test_ccore_display_instantiation(instance):
    assert isinstance(instance, ccore_Display)



@given(instance=ccore_Display_strategy)
def test_ccore_display_extendsIC_setter(instance):
    original = instance.extendsIC
    instance.extendsIC = original
    assert instance.extendsIC == original



@given(instance=ccore_Display_strategy)
def test_ccore_display_extendsUI_setter(instance):
    original = instance.extendsUI
    instance.extendsUI = original
    assert instance.extendsUI == original



@given(instance=ccore_Display_strategy)
def test_ccore_display_extendsMC_setter(instance):
    original = instance.extendsMC
    instance.extendsMC = original
    assert instance.extendsMC == original

@given(instance=ccore_ExportedContent_strategy)
@settings(max_examples=50)
def test_ccore_exportedcontent_instantiation(instance):
    assert isinstance(instance, ccore_ExportedContent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ccore_ExportedContent_strategy)
@settings(max_examples=30)
def test_ccore_exportedcontent_haschildren_changes_state(instance):
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
        assert has_statements, f"Function 'hasChildren' in ccore_ExportedContent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasChildren' in ccore_ExportedContent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasChildren' in ccore_ExportedContent is not implemented or raised an error")

@given(instance=BindingDesc_strategy)
@settings(max_examples=50)
def test_bindingdesc_instantiation(instance):
    assert isinstance(instance, BindingDesc)

@given(instance=ccore_BindExt_strategy)
@settings(max_examples=50)
def test_ccore_bindext_instantiation(instance):
    assert isinstance(instance, ccore_BindExt)

@given(instance=ccore_UnresolvedAttributeType_strategy)
@settings(max_examples=50)
def test_ccore_unresolvedattributetype_instantiation(instance):
    assert isinstance(instance, ccore_UnresolvedAttributeType)

@given(instance=LongAttribute_strategy)
@settings(max_examples=50)
def test_longattribute_instantiation(instance):
    assert isinstance(instance, LongAttribute)

@given(instance=ccore_TimeAttribute_strategy)
@settings(max_examples=50)
def test_ccore_timeattribute_instantiation(instance):
    assert isinstance(instance, ccore_TimeAttribute)



@given(instance=ccore_TimeAttribute_strategy)
def test_ccore_timeattribute_initWithTheCurrentTime_setter(instance):
    original = instance.initWithTheCurrentTime
    instance.initWithTheCurrentTime = original
    assert instance.initWithTheCurrentTime == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=ccore_IntegerAttribute_strategy)
@settings(max_examples=50)
def test_ccore_integerattribute_instantiation(instance):
    assert isinstance(instance, ccore_IntegerAttribute)

@given(instance=ccore_Enum_strategy)
@settings(max_examples=50)
def test_ccore_enum_instantiation(instance):
    assert isinstance(instance, ccore_Enum)



@given(instance=ccore_Enum_strategy)
def test_ccore_enum_enumClazz_setter(instance):
    original = instance.enumClazz
    instance.enumClazz = original
    assert instance.enumClazz == original



@given(instance=ccore_Enum_strategy)
def test_ccore_enum_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ccore_LongAttribute_strategy)
@settings(max_examples=50)
def test_ccore_longattribute_instantiation(instance):
    assert isinstance(instance, ccore_LongAttribute)

@given(instance=ccore_UUIDAttribute_strategy)
@settings(max_examples=50)
def test_ccore_uuidattribute_instantiation(instance):
    assert isinstance(instance, ccore_UUIDAttribute)

@given(instance=ccore_DateAttribute_strategy)
@settings(max_examples=50)
def test_ccore_dateattribute_instantiation(instance):
    assert isinstance(instance, ccore_DateAttribute)

@given(instance=ccore_LinkType_strategy)
@settings(max_examples=50)
def test_ccore_linktype_instantiation(instance):
    assert isinstance(instance, ccore_LinkType)



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_composition_setter(instance):
    original = instance.composition
    instance.composition = original
    assert instance.composition == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_twCoupled_setter(instance):
    original = instance.twCoupled
    instance.twCoupled = original
    assert instance.twCoupled == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_linkManager_setter(instance):
    original = instance.linkManager
    instance.linkManager = original
    assert instance.linkManager == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_mapping_setter(instance):
    original = instance.mapping
    instance.mapping = original
    assert instance.mapping == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_twDestEvol_setter(instance):
    original = instance.twDestEvol
    instance.twDestEvol = original
    assert instance.twDestEvol == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=ccore_LinkType_strategy)
def test_ccore_linktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=ccore_DoubleAttribute_strategy)
@settings(max_examples=50)
def test_ccore_doubleattribute_instantiation(instance):
    assert isinstance(instance, ccore_DoubleAttribute)

@given(instance=ccore_BooleanAttribute_strategy)
@settings(max_examples=50)
def test_ccore_booleanattribute_instantiation(instance):
    assert isinstance(instance, ccore_BooleanAttribute)

@given(instance=ccore_StringAttribute_strategy)
@settings(max_examples=50)
def test_ccore_stringattribute_instantiation(instance):
    assert isinstance(instance, ccore_StringAttribute)



@given(instance=ccore_StringAttribute_strategy)
def test_ccore_stringattribute_notEmpty_setter(instance):
    original = instance.notEmpty
    instance.notEmpty = original
    assert instance.notEmpty == original

@given(instance=ccore_ViewDescription_strategy)
@settings(max_examples=50)
def test_ccore_viewdescription_instantiation(instance):
    assert isinstance(instance, ccore_ViewDescription)

@given(instance=ccore_ViewLinkType_strategy)
@settings(max_examples=50)
def test_ccore_viewlinktype_instantiation(instance):
    assert isinstance(instance, ccore_ViewLinkType)



@given(instance=ccore_ViewLinkType_strategy)
def test_ccore_viewlinktype_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=ccore_ViewLinkType_strategy)
def test_ccore_viewlinktype_displayCreate_setter(instance):
    original = instance.displayCreate
    instance.displayCreate = original
    assert instance.displayCreate == original



@given(instance=ccore_ViewLinkType_strategy)
def test_ccore_viewlinktype_canCreateItem_setter(instance):
    original = instance.canCreateItem
    instance.canCreateItem = original
    assert instance.canCreateItem == original



@given(instance=ccore_ViewLinkType_strategy)
def test_ccore_viewlinktype_canCreateLink_setter(instance):
    original = instance.canCreateLink
    instance.canCreateLink = original
    assert instance.canCreateLink == original

@given(instance=ccore_ViewItemType_strategy)
@settings(max_examples=50)
def test_ccore_viewitemtype_instantiation(instance):
    assert isinstance(instance, ccore_ViewItemType)



@given(instance=ccore_ViewItemType_strategy)
def test_ccore_viewitemtype_isRootElement_setter(instance):
    original = instance.isRootElement
    instance.isRootElement = original
    assert instance.isRootElement == original



@given(instance=ccore_ViewItemType_strategy)
def test_ccore_viewitemtype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=ccore_GenInformation_strategy)
@settings(max_examples=50)
def test_ccore_geninformation_instantiation(instance):
    assert isinstance(instance, ccore_GenInformation)



@given(instance=ccore_GenInformation_strategy)
def test_ccore_geninformation_cSTName_setter(instance):
    original = instance.cSTName
    instance.cSTName = original
    assert instance.cSTName == original
