import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    becontent_ViewItem,
    TypedSystemAttribute,
    becontent_SystemAttributePassword,
    becontent_SystemAttributePosition,
    becontent_SystemAttributeText,
    becontent_SystemAttributeLongDate,
    becontent_SystemAttributeDate,
    becontent_SystemAttributeColor,
    SystemEntityField,
    becontent_TypedSystemAttribute,
    becontent_SystemReference,
    becontent_SystemAttributeFileToFolder,
    becontent_SystemAttributeFile,
    becontent_SystemAttributeVarchar,
    becontent_SystemAttributeInteger,
    becontent_SystemAttributeImage,
    TypedAttribute,
    becontent_AttributeFileToFolder,
    becontent_AttributeColor,
    EntityField,
    becontent_TypedAttribute,
    becontent_Reference,
    becontent_AttributeFile,
    becontent_AttributeVarchar,
    becontent_AttributeInteger,
    becontent_AttributeImage,
    becontent_AttributePosition,
    becontent_AttributePassword,
    becontent_AttributeText,
    becontent_AttributeLongDate,
    becontent_AttributeDate,
    becontent_EntityField,
    DefinitionItem,
    becontent_Entity,
    BeContentElement,
    becontent_FileToFolderExtension,
    becontent_DefinitionItem,
    becontent_BeContentElement,
    becontent_BeContentModel,
    Relation,
    becontent_SystemRelation,
    becontent_CustomRelation,
    becontent_Relation,
    becontent_SystemEntityField,
    Entity,
    becontent_SystemEntity,
    becontent_CustomEntity,
    becontent_Handler,
    becontent_Channel,
    NotStructuredElement,
    becontent_FileToFolder,
    becontent_Password,
    becontent_LongDate,
    becontent_Editor,
    becontent_RadioFromReference,
    becontent_SelectFromReference,
    becontent_Image,
    becontent_File,
    becontent_Textarea,
    becontent_HierarchicalPosition,
    becontent_Hidden,
    becontent_Position,
    becontent_Year,
    becontent_Date,
    becontent_RelationManager,
    becontent_Link,
    becontent_Color,
    becontent_Select,
    becontent_Section,
    Form,
    becontent_ExtendedForm,
    becontent_Checkbox,
    becontent_RadioButton,
    becontent_Text,
    becontent_Validation,
    becontent_CustomPager,
    becontent_EntityManagerPage,
    ApplyCommand,
    becontent_ApplyItem,
    becontent_ApplyIndexed,
    becontent_Apply,
    FormElement,
    becontent_Form,
    becontent_NotStructuredElement,
    becontent_FormElement,
    becontent_ConditionalTemplate,
    becontent_ContentCommand,
    becontent_JoinEntity,
    ContentCommand,
    becontent_UnsetParameter,
    becontent_ApplyCommand,
    becontent_Copy,
    becontent_Trigger,
    becontent_Propagate,
    becontent_Parameter,
    ViewItem,
    becontent_Skinlet,
    becontent_Content,
    becontent_Template,
    becontent_Skin,
    OrientationType,
    ContentStyle,
    ConditionalTemplateExpType,
    ConditionType,
    FormMethodType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_becontent_viewitem_is_not_abstract():
    assert not inspect.isabstract(becontent_ViewItem)


def test_becontent_viewitem_constructor_exists():
    assert callable(becontent_ViewItem.__init__)


def test_becontent_viewitem_constructor_args():
    sig = inspect.signature(becontent_ViewItem.__init__)
    params = list(sig.parameters.keys())



def test_typedsystemattribute_is_not_abstract():
    assert not inspect.isabstract(TypedSystemAttribute)


def test_typedsystemattribute_constructor_exists():
    assert callable(TypedSystemAttribute.__init__)


def test_typedsystemattribute_constructor_args():
    sig = inspect.signature(TypedSystemAttribute.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributepassword_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributePassword)


def test_becontent_systemattributepassword_constructor_exists():
    assert callable(becontent_SystemAttributePassword.__init__)


def test_becontent_systemattributepassword_constructor_args():
    sig = inspect.signature(becontent_SystemAttributePassword.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributeposition_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributePosition)


def test_becontent_systemattributeposition_constructor_exists():
    assert callable(becontent_SystemAttributePosition.__init__)


def test_becontent_systemattributeposition_constructor_args():
    sig = inspect.signature(becontent_SystemAttributePosition.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributetext_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeText)


def test_becontent_systemattributetext_constructor_exists():
    assert callable(becontent_SystemAttributeText.__init__)


def test_becontent_systemattributetext_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeText.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributelongdate_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeLongDate)


def test_becontent_systemattributelongdate_constructor_exists():
    assert callable(becontent_SystemAttributeLongDate.__init__)


def test_becontent_systemattributelongdate_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeLongDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributedate_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeDate)


def test_becontent_systemattributedate_constructor_exists():
    assert callable(becontent_SystemAttributeDate.__init__)


def test_becontent_systemattributedate_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributecolor_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeColor)


def test_becontent_systemattributecolor_constructor_exists():
    assert callable(becontent_SystemAttributeColor.__init__)


def test_becontent_systemattributecolor_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeColor.__init__)
    params = list(sig.parameters.keys())



def test_systementityfield_is_not_abstract():
    assert not inspect.isabstract(SystemEntityField)


def test_systementityfield_constructor_exists():
    assert callable(SystemEntityField.__init__)


def test_systementityfield_constructor_args():
    sig = inspect.signature(SystemEntityField.__init__)
    params = list(sig.parameters.keys())



def test_becontent_typedsystemattribute_is_not_abstract():
    assert not inspect.isabstract(becontent_TypedSystemAttribute)


def test_becontent_typedsystemattribute_constructor_exists():
    assert callable(becontent_TypedSystemAttribute.__init__)


def test_becontent_typedsystemattribute_constructor_args():
    sig = inspect.signature(becontent_TypedSystemAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_typedsystemattribute_has_name():
    assert hasattr(becontent_TypedSystemAttribute, "name")
    descriptor = None
    for klass in becontent_TypedSystemAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_typedsystemattribute_has_isMandatory():
    assert hasattr(becontent_TypedSystemAttribute, "isMandatory")
    descriptor = None
    for klass in becontent_TypedSystemAttribute.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_systemreference_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemReference)


def test_becontent_systemreference_constructor_exists():
    assert callable(becontent_SystemReference.__init__)


def test_becontent_systemreference_constructor_args():
    sig = inspect.signature(becontent_SystemReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_systemreference_has_name():
    assert hasattr(becontent_SystemReference, "name")
    descriptor = None
    for klass in becontent_SystemReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_systemattributefiletofolder_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeFileToFolder)


def test_becontent_systemattributefiletofolder_constructor_exists():
    assert callable(becontent_SystemAttributeFileToFolder.__init__)


def test_becontent_systemattributefiletofolder_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeFileToFolder.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributefile_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeFile)


def test_becontent_systemattributefile_constructor_exists():
    assert callable(becontent_SystemAttributeFile.__init__)


def test_becontent_systemattributefile_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeFile.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemattributevarchar_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeVarchar)


def test_becontent_systemattributevarchar_constructor_exists():
    assert callable(becontent_SystemAttributeVarchar.__init__)


def test_becontent_systemattributevarchar_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeVarchar.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"
    assert "length" in params, "Missing parameter 'length'"

def test_becontent_systemattributevarchar_has_isPrimaryKey():
    assert hasattr(becontent_SystemAttributeVarchar, "isPrimaryKey")
    descriptor = None
    for klass in becontent_SystemAttributeVarchar.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_becontent_systemattributevarchar_has_length():
    assert hasattr(becontent_SystemAttributeVarchar, "length")
    descriptor = None
    for klass in becontent_SystemAttributeVarchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_becontent_systemattributeinteger_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeInteger)


def test_becontent_systemattributeinteger_constructor_exists():
    assert callable(becontent_SystemAttributeInteger.__init__)


def test_becontent_systemattributeinteger_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent_systemattributeinteger_has_isPrimaryKey():
    assert hasattr(becontent_SystemAttributeInteger, "isPrimaryKey")
    descriptor = None
    for klass in becontent_SystemAttributeInteger.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent_systemattributeimage_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemAttributeImage)


def test_becontent_systemattributeimage_constructor_exists():
    assert callable(becontent_SystemAttributeImage.__init__)


def test_becontent_systemattributeimage_constructor_args():
    sig = inspect.signature(becontent_SystemAttributeImage.__init__)
    params = list(sig.parameters.keys())



def test_typedattribute_is_not_abstract():
    assert not inspect.isabstract(TypedAttribute)


def test_typedattribute_constructor_exists():
    assert callable(TypedAttribute.__init__)


def test_typedattribute_constructor_args():
    sig = inspect.signature(TypedAttribute.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributefiletofolder_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeFileToFolder)


def test_becontent_attributefiletofolder_constructor_exists():
    assert callable(becontent_AttributeFileToFolder.__init__)


def test_becontent_attributefiletofolder_constructor_args():
    sig = inspect.signature(becontent_AttributeFileToFolder.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributecolor_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeColor)


def test_becontent_attributecolor_constructor_exists():
    assert callable(becontent_AttributeColor.__init__)


def test_becontent_attributecolor_constructor_args():
    sig = inspect.signature(becontent_AttributeColor.__init__)
    params = list(sig.parameters.keys())



def test_entityfield_is_not_abstract():
    assert not inspect.isabstract(EntityField)


def test_entityfield_constructor_exists():
    assert callable(EntityField.__init__)


def test_entityfield_constructor_args():
    sig = inspect.signature(EntityField.__init__)
    params = list(sig.parameters.keys())



def test_becontent_typedattribute_is_not_abstract():
    assert not inspect.isabstract(becontent_TypedAttribute)


def test_becontent_typedattribute_constructor_exists():
    assert callable(becontent_TypedAttribute.__init__)


def test_becontent_typedattribute_constructor_args():
    sig = inspect.signature(becontent_TypedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_typedattribute_has_name():
    assert hasattr(becontent_TypedAttribute, "name")
    descriptor = None
    for klass in becontent_TypedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_typedattribute_has_isMandatory():
    assert hasattr(becontent_TypedAttribute, "isMandatory")
    descriptor = None
    for klass in becontent_TypedAttribute.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_reference_is_not_abstract():
    assert not inspect.isabstract(becontent_Reference)


def test_becontent_reference_constructor_exists():
    assert callable(becontent_Reference.__init__)


def test_becontent_reference_constructor_args():
    sig = inspect.signature(becontent_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_reference_has_name():
    assert hasattr(becontent_Reference, "name")
    descriptor = None
    for klass in becontent_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_attributefile_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeFile)


def test_becontent_attributefile_constructor_exists():
    assert callable(becontent_AttributeFile.__init__)


def test_becontent_attributefile_constructor_args():
    sig = inspect.signature(becontent_AttributeFile.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributevarchar_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeVarchar)


def test_becontent_attributevarchar_constructor_exists():
    assert callable(becontent_AttributeVarchar.__init__)


def test_becontent_attributevarchar_constructor_args():
    sig = inspect.signature(becontent_AttributeVarchar.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent_attributevarchar_has_length():
    assert hasattr(becontent_AttributeVarchar, "length")
    descriptor = None
    for klass in becontent_AttributeVarchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_becontent_attributevarchar_has_isPrimaryKey():
    assert hasattr(becontent_AttributeVarchar, "isPrimaryKey")
    descriptor = None
    for klass in becontent_AttributeVarchar.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent_attributeinteger_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeInteger)


def test_becontent_attributeinteger_constructor_exists():
    assert callable(becontent_AttributeInteger.__init__)


def test_becontent_attributeinteger_constructor_args():
    sig = inspect.signature(becontent_AttributeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryKey" in params, "Missing parameter 'isPrimaryKey'"

def test_becontent_attributeinteger_has_isPrimaryKey():
    assert hasattr(becontent_AttributeInteger, "isPrimaryKey")
    descriptor = None
    for klass in becontent_AttributeInteger.__mro__:
        if "isPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent_attributeimage_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeImage)


def test_becontent_attributeimage_constructor_exists():
    assert callable(becontent_AttributeImage.__init__)


def test_becontent_attributeimage_constructor_args():
    sig = inspect.signature(becontent_AttributeImage.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributeposition_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributePosition)


def test_becontent_attributeposition_constructor_exists():
    assert callable(becontent_AttributePosition.__init__)


def test_becontent_attributeposition_constructor_args():
    sig = inspect.signature(becontent_AttributePosition.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributepassword_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributePassword)


def test_becontent_attributepassword_constructor_exists():
    assert callable(becontent_AttributePassword.__init__)


def test_becontent_attributepassword_constructor_args():
    sig = inspect.signature(becontent_AttributePassword.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributetext_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeText)


def test_becontent_attributetext_constructor_exists():
    assert callable(becontent_AttributeText.__init__)


def test_becontent_attributetext_constructor_args():
    sig = inspect.signature(becontent_AttributeText.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributelongdate_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeLongDate)


def test_becontent_attributelongdate_constructor_exists():
    assert callable(becontent_AttributeLongDate.__init__)


def test_becontent_attributelongdate_constructor_args():
    sig = inspect.signature(becontent_AttributeLongDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent_attributedate_is_not_abstract():
    assert not inspect.isabstract(becontent_AttributeDate)


def test_becontent_attributedate_constructor_exists():
    assert callable(becontent_AttributeDate.__init__)


def test_becontent_attributedate_constructor_args():
    sig = inspect.signature(becontent_AttributeDate.__init__)
    params = list(sig.parameters.keys())



def test_becontent_entityfield_is_not_abstract():
    assert not inspect.isabstract(becontent_EntityField)


def test_becontent_entityfield_constructor_exists():
    assert callable(becontent_EntityField.__init__)


def test_becontent_entityfield_constructor_args():
    sig = inspect.signature(becontent_EntityField.__init__)
    params = list(sig.parameters.keys())
    assert "isTextSearch" in params, "Missing parameter 'isTextSearch'"
    assert "isSearchPresentationHead" in params, "Missing parameter 'isSearchPresentationHead'"
    assert "isPresented" in params, "Missing parameter 'isPresented'"
    assert "isSearchPresentationBody" in params, "Missing parameter 'isSearchPresentationBody'"

def test_becontent_entityfield_has_isTextSearch():
    assert hasattr(becontent_EntityField, "isTextSearch")
    descriptor = None
    for klass in becontent_EntityField.__mro__:
        if "isTextSearch" in klass.__dict__:
            descriptor = klass.__dict__["isTextSearch"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entityfield_has_isSearchPresentationHead():
    assert hasattr(becontent_EntityField, "isSearchPresentationHead")
    descriptor = None
    for klass in becontent_EntityField.__mro__:
        if "isSearchPresentationHead" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationHead"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entityfield_has_isPresented():
    assert hasattr(becontent_EntityField, "isPresented")
    descriptor = None
    for klass in becontent_EntityField.__mro__:
        if "isPresented" in klass.__dict__:
            descriptor = klass.__dict__["isPresented"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entityfield_has_isSearchPresentationBody():
    assert hasattr(becontent_EntityField, "isSearchPresentationBody")
    descriptor = None
    for klass in becontent_EntityField.__mro__:
        if "isSearchPresentationBody" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationBody"]
            break
    assert isinstance(descriptor, property)



def test_definitionitem_is_not_abstract():
    assert not inspect.isabstract(DefinitionItem)


def test_definitionitem_constructor_exists():
    assert callable(DefinitionItem.__init__)


def test_definitionitem_constructor_args():
    sig = inspect.signature(DefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent_entity_is_not_abstract():
    assert not inspect.isabstract(becontent_Entity)


def test_becontent_entity_constructor_exists():
    assert callable(becontent_Entity.__init__)


def test_becontent_entity_constructor_args():
    sig = inspect.signature(becontent_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "rssFilter" in params, "Missing parameter 'rssFilter'"
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "presentationString" in params, "Missing parameter 'presentationString'"
    assert "isOwned" in params, "Missing parameter 'isOwned'"

def test_becontent_entity_has_rssFilter():
    assert hasattr(becontent_Entity, "rssFilter")
    descriptor = None
    for klass in becontent_Entity.__mro__:
        if "rssFilter" in klass.__dict__:
            descriptor = klass.__dict__["rssFilter"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entity_has_variableName():
    assert hasattr(becontent_Entity, "variableName")
    descriptor = None
    for klass in becontent_Entity.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entity_has_name():
    assert hasattr(becontent_Entity, "name")
    descriptor = None
    for klass in becontent_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entity_has_presentationString():
    assert hasattr(becontent_Entity, "presentationString")
    descriptor = None
    for klass in becontent_Entity.__mro__:
        if "presentationString" in klass.__dict__:
            descriptor = klass.__dict__["presentationString"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entity_has_isOwned():
    assert hasattr(becontent_Entity, "isOwned")
    descriptor = None
    for klass in becontent_Entity.__mro__:
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



def test_becontent_filetofolderextension_is_not_abstract():
    assert not inspect.isabstract(becontent_FileToFolderExtension)


def test_becontent_filetofolderextension_constructor_exists():
    assert callable(becontent_FileToFolderExtension.__init__)


def test_becontent_filetofolderextension_constructor_args():
    sig = inspect.signature(becontent_FileToFolderExtension.__init__)
    params = list(sig.parameters.keys())
    assert "extensionValue" in params, "Missing parameter 'extensionValue'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "extensionKey" in params, "Missing parameter 'extensionKey'"

def test_becontent_filetofolderextension_has_extensionValue():
    assert hasattr(becontent_FileToFolderExtension, "extensionValue")
    descriptor = None
    for klass in becontent_FileToFolderExtension.__mro__:
        if "extensionValue" in klass.__dict__:
            descriptor = klass.__dict__["extensionValue"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolderextension_has__id_model():
    assert hasattr(becontent_FileToFolderExtension, "_id_model")
    descriptor = None
    for klass in becontent_FileToFolderExtension.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolderextension_has_extensionKey():
    assert hasattr(becontent_FileToFolderExtension, "extensionKey")
    descriptor = None
    for klass in becontent_FileToFolderExtension.__mro__:
        if "extensionKey" in klass.__dict__:
            descriptor = klass.__dict__["extensionKey"]
            break
    assert isinstance(descriptor, property)



def test_becontent_definitionitem_is_not_abstract():
    assert not inspect.isabstract(becontent_DefinitionItem)


def test_becontent_definitionitem_constructor_exists():
    assert callable(becontent_DefinitionItem.__init__)


def test_becontent_definitionitem_constructor_args():
    sig = inspect.signature(becontent_DefinitionItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent_becontentelement_is_not_abstract():
    assert not inspect.isabstract(becontent_BeContentElement)


def test_becontent_becontentelement_constructor_exists():
    assert callable(becontent_BeContentElement.__init__)


def test_becontent_becontentelement_constructor_args():
    sig = inspect.signature(becontent_BeContentElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent_becontentmodel_is_not_abstract():
    assert not inspect.isabstract(becontent_BeContentModel)


def test_becontent_becontentmodel_constructor_exists():
    assert callable(becontent_BeContentModel.__init__)


def test_becontent_becontentmodel_constructor_args():
    sig = inspect.signature(becontent_BeContentModel.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systemrelation_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemRelation)


def test_becontent_systemrelation_constructor_exists():
    assert callable(becontent_SystemRelation.__init__)


def test_becontent_systemrelation_constructor_args():
    sig = inspect.signature(becontent_SystemRelation.__init__)
    params = list(sig.parameters.keys())



def test_becontent_customrelation_is_not_abstract():
    assert not inspect.isabstract(becontent_CustomRelation)


def test_becontent_customrelation_constructor_exists():
    assert callable(becontent_CustomRelation.__init__)


def test_becontent_customrelation_constructor_args():
    sig = inspect.signature(becontent_CustomRelation.__init__)
    params = list(sig.parameters.keys())



def test_becontent_relation_is_not_abstract():
    assert not inspect.isabstract(becontent_Relation)


def test_becontent_relation_constructor_exists():
    assert callable(becontent_Relation.__init__)


def test_becontent_relation_constructor_args():
    sig = inspect.signature(becontent_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_becontent_relation_has_name():
    assert hasattr(becontent_Relation, "name")
    descriptor = None
    for klass in becontent_Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_relation_has_variableName():
    assert hasattr(becontent_Relation, "variableName")
    descriptor = None
    for klass in becontent_Relation.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_becontent_systementityfield_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemEntityField)


def test_becontent_systementityfield_constructor_exists():
    assert callable(becontent_SystemEntityField.__init__)


def test_becontent_systementityfield_constructor_args():
    sig = inspect.signature(becontent_SystemEntityField.__init__)
    params = list(sig.parameters.keys())
    assert "isTextSearch" in params, "Missing parameter 'isTextSearch'"
    assert "isSearchPresentationHead" in params, "Missing parameter 'isSearchPresentationHead'"
    assert "isSearchPresentationBody" in params, "Missing parameter 'isSearchPresentationBody'"
    assert "isPresented" in params, "Missing parameter 'isPresented'"

def test_becontent_systementityfield_has_isTextSearch():
    assert hasattr(becontent_SystemEntityField, "isTextSearch")
    descriptor = None
    for klass in becontent_SystemEntityField.__mro__:
        if "isTextSearch" in klass.__dict__:
            descriptor = klass.__dict__["isTextSearch"]
            break
    assert isinstance(descriptor, property)

def test_becontent_systementityfield_has_isSearchPresentationHead():
    assert hasattr(becontent_SystemEntityField, "isSearchPresentationHead")
    descriptor = None
    for klass in becontent_SystemEntityField.__mro__:
        if "isSearchPresentationHead" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationHead"]
            break
    assert isinstance(descriptor, property)

def test_becontent_systementityfield_has_isSearchPresentationBody():
    assert hasattr(becontent_SystemEntityField, "isSearchPresentationBody")
    descriptor = None
    for klass in becontent_SystemEntityField.__mro__:
        if "isSearchPresentationBody" in klass.__dict__:
            descriptor = klass.__dict__["isSearchPresentationBody"]
            break
    assert isinstance(descriptor, property)

def test_becontent_systementityfield_has_isPresented():
    assert hasattr(becontent_SystemEntityField, "isPresented")
    descriptor = None
    for klass in becontent_SystemEntityField.__mro__:
        if "isPresented" in klass.__dict__:
            descriptor = klass.__dict__["isPresented"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_becontent_systementity_is_not_abstract():
    assert not inspect.isabstract(becontent_SystemEntity)


def test_becontent_systementity_constructor_exists():
    assert callable(becontent_SystemEntity.__init__)


def test_becontent_systementity_constructor_args():
    sig = inspect.signature(becontent_SystemEntity.__init__)
    params = list(sig.parameters.keys())



def test_becontent_customentity_is_not_abstract():
    assert not inspect.isabstract(becontent_CustomEntity)


def test_becontent_customentity_constructor_exists():
    assert callable(becontent_CustomEntity.__init__)


def test_becontent_customentity_constructor_args():
    sig = inspect.signature(becontent_CustomEntity.__init__)
    params = list(sig.parameters.keys())



def test_becontent_handler_is_not_abstract():
    assert not inspect.isabstract(becontent_Handler)


def test_becontent_handler_constructor_exists():
    assert callable(becontent_Handler.__init__)


def test_becontent_handler_constructor_args():
    sig = inspect.signature(becontent_Handler.__init__)
    params = list(sig.parameters.keys())
    assert "mainSkinPagerLength" in params, "Missing parameter 'mainSkinPagerLength'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "mainSkinWithPager" in params, "Missing parameter 'mainSkinWithPager'"
    assert "mainSkinPlaceholder" in params, "Missing parameter 'mainSkinPlaceholder'"

def test_becontent_handler_has_mainSkinPagerLength():
    assert hasattr(becontent_Handler, "mainSkinPagerLength")
    descriptor = None
    for klass in becontent_Handler.__mro__:
        if "mainSkinPagerLength" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinPagerLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent_handler_has_fileName():
    assert hasattr(becontent_Handler, "fileName")
    descriptor = None
    for klass in becontent_Handler.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_becontent_handler_has_mainSkinWithPager():
    assert hasattr(becontent_Handler, "mainSkinWithPager")
    descriptor = None
    for klass in becontent_Handler.__mro__:
        if "mainSkinWithPager" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinWithPager"]
            break
    assert isinstance(descriptor, property)

def test_becontent_handler_has_mainSkinPlaceholder():
    assert hasattr(becontent_Handler, "mainSkinPlaceholder")
    descriptor = None
    for klass in becontent_Handler.__mro__:
        if "mainSkinPlaceholder" in klass.__dict__:
            descriptor = klass.__dict__["mainSkinPlaceholder"]
            break
    assert isinstance(descriptor, property)



def test_becontent_channel_is_not_abstract():
    assert not inspect.isabstract(becontent_Channel)


def test_becontent_channel_constructor_exists():
    assert callable(becontent_Channel.__init__)


def test_becontent_channel_constructor_args():
    sig = inspect.signature(becontent_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_becontent_channel_has__id_model():
    assert hasattr(becontent_Channel, "_id_model")
    descriptor = None
    for klass in becontent_Channel.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_channel_has_parameters():
    assert hasattr(becontent_Channel, "parameters")
    descriptor = None
    for klass in becontent_Channel.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_notstructuredelement_is_not_abstract():
    assert not inspect.isabstract(NotStructuredElement)


def test_notstructuredelement_constructor_exists():
    assert callable(NotStructuredElement.__init__)


def test_notstructuredelement_constructor_args():
    sig = inspect.signature(NotStructuredElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent_filetofolder_is_not_abstract():
    assert not inspect.isabstract(becontent_FileToFolder)


def test_becontent_filetofolder_constructor_exists():
    assert callable(becontent_FileToFolder.__init__)


def test_becontent_filetofolder_constructor_args():
    sig = inspect.signature(becontent_FileToFolder.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "label" in params, "Missing parameter 'label'"
    assert "extensionMessage" in params, "Missing parameter 'extensionMessage'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_filetofolder_has_extension():
    assert hasattr(becontent_FileToFolder, "extension")
    descriptor = None
    for klass in becontent_FileToFolder.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolder_has_label():
    assert hasattr(becontent_FileToFolder, "label")
    descriptor = None
    for klass in becontent_FileToFolder.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolder_has_extensionMessage():
    assert hasattr(becontent_FileToFolder, "extensionMessage")
    descriptor = None
    for klass in becontent_FileToFolder.__mro__:
        if "extensionMessage" in klass.__dict__:
            descriptor = klass.__dict__["extensionMessage"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolder_has_name():
    assert hasattr(becontent_FileToFolder, "name")
    descriptor = None
    for klass in becontent_FileToFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_filetofolder_has_isMandatory():
    assert hasattr(becontent_FileToFolder, "isMandatory")
    descriptor = None
    for klass in becontent_FileToFolder.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_password_is_not_abstract():
    assert not inspect.isabstract(becontent_Password)


def test_becontent_password_constructor_exists():
    assert callable(becontent_Password.__init__)


def test_becontent_password_constructor_args():
    sig = inspect.signature(becontent_Password.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "size" in params, "Missing parameter 'size'"
    assert "label" in params, "Missing parameter 'label'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_password_has_isMandatory():
    assert hasattr(becontent_Password, "isMandatory")
    descriptor = None
    for klass in becontent_Password.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_password_has_size():
    assert hasattr(becontent_Password, "size")
    descriptor = None
    for klass in becontent_Password.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent_password_has_label():
    assert hasattr(becontent_Password, "label")
    descriptor = None
    for klass in becontent_Password.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_password_has_maxLength():
    assert hasattr(becontent_Password, "maxLength")
    descriptor = None
    for klass in becontent_Password.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent_password_has_name():
    assert hasattr(becontent_Password, "name")
    descriptor = None
    for klass in becontent_Password.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_longdate_is_not_abstract():
    assert not inspect.isabstract(becontent_LongDate)


def test_becontent_longdate_constructor_exists():
    assert callable(becontent_LongDate.__init__)


def test_becontent_longdate_constructor_args():
    sig = inspect.signature(becontent_LongDate.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent_longdate_has_isMandatory():
    assert hasattr(becontent_LongDate, "isMandatory")
    descriptor = None
    for klass in becontent_LongDate.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_longdate_has_name():
    assert hasattr(becontent_LongDate, "name")
    descriptor = None
    for klass in becontent_LongDate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_longdate_has_label():
    assert hasattr(becontent_LongDate, "label")
    descriptor = None
    for klass in becontent_LongDate.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent_editor_is_not_abstract():
    assert not inspect.isabstract(becontent_Editor)


def test_becontent_editor_constructor_exists():
    assert callable(becontent_Editor.__init__)


def test_becontent_editor_constructor_args():
    sig = inspect.signature(becontent_Editor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "rows" in params, "Missing parameter 'rows'"
    assert "columns" in params, "Missing parameter 'columns'"

def test_becontent_editor_has_name():
    assert hasattr(becontent_Editor, "name")
    descriptor = None
    for klass in becontent_Editor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_editor_has_isMandatory():
    assert hasattr(becontent_Editor, "isMandatory")
    descriptor = None
    for klass in becontent_Editor.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_editor_has_label():
    assert hasattr(becontent_Editor, "label")
    descriptor = None
    for klass in becontent_Editor.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_editor_has_rows():
    assert hasattr(becontent_Editor, "rows")
    descriptor = None
    for klass in becontent_Editor.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_becontent_editor_has_columns():
    assert hasattr(becontent_Editor, "columns")
    descriptor = None
    for klass in becontent_Editor.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_becontent_radiofromreference_is_not_abstract():
    assert not inspect.isabstract(becontent_RadioFromReference)


def test_becontent_radiofromreference_constructor_exists():
    assert callable(becontent_RadioFromReference.__init__)


def test_becontent_radiofromreference_constructor_args():
    sig = inspect.signature(becontent_RadioFromReference.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_radiofromreference_has_isMandatory():
    assert hasattr(becontent_RadioFromReference, "isMandatory")
    descriptor = None
    for klass in becontent_RadioFromReference.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_radiofromreference_has_restrictCondition():
    assert hasattr(becontent_RadioFromReference, "restrictCondition")
    descriptor = None
    for klass in becontent_RadioFromReference.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent_radiofromreference_has_label():
    assert hasattr(becontent_RadioFromReference, "label")
    descriptor = None
    for klass in becontent_RadioFromReference.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_radiofromreference_has_name():
    assert hasattr(becontent_RadioFromReference, "name")
    descriptor = None
    for klass in becontent_RadioFromReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_selectfromreference_is_not_abstract():
    assert not inspect.isabstract(becontent_SelectFromReference)


def test_becontent_selectfromreference_constructor_exists():
    assert callable(becontent_SelectFromReference.__init__)


def test_becontent_selectfromreference_constructor_args():
    sig = inspect.signature(becontent_SelectFromReference.__init__)
    params = list(sig.parameters.keys())
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_selectfromreference_has_restrictCondition():
    assert hasattr(becontent_SelectFromReference, "restrictCondition")
    descriptor = None
    for klass in becontent_SelectFromReference.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent_selectfromreference_has_isMandatory():
    assert hasattr(becontent_SelectFromReference, "isMandatory")
    descriptor = None
    for klass in becontent_SelectFromReference.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_selectfromreference_has_label():
    assert hasattr(becontent_SelectFromReference, "label")
    descriptor = None
    for klass in becontent_SelectFromReference.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_selectfromreference_has_name():
    assert hasattr(becontent_SelectFromReference, "name")
    descriptor = None
    for klass in becontent_SelectFromReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_image_is_not_abstract():
    assert not inspect.isabstract(becontent_Image)


def test_becontent_image_constructor_exists():
    assert callable(becontent_Image.__init__)


def test_becontent_image_constructor_args():
    sig = inspect.signature(becontent_Image.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_image_has_label():
    assert hasattr(becontent_Image, "label")
    descriptor = None
    for klass in becontent_Image.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_image_has_isMandatory():
    assert hasattr(becontent_Image, "isMandatory")
    descriptor = None
    for klass in becontent_Image.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_image_has_name():
    assert hasattr(becontent_Image, "name")
    descriptor = None
    for klass in becontent_Image.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_file_is_not_abstract():
    assert not inspect.isabstract(becontent_File)


def test_becontent_file_constructor_exists():
    assert callable(becontent_File.__init__)


def test_becontent_file_constructor_args():
    sig = inspect.signature(becontent_File.__init__)
    params = list(sig.parameters.keys())
    assert "extensionMessage" in params, "Missing parameter 'extensionMessage'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_file_has_extensionMessage():
    assert hasattr(becontent_File, "extensionMessage")
    descriptor = None
    for klass in becontent_File.__mro__:
        if "extensionMessage" in klass.__dict__:
            descriptor = klass.__dict__["extensionMessage"]
            break
    assert isinstance(descriptor, property)

def test_becontent_file_has_isMandatory():
    assert hasattr(becontent_File, "isMandatory")
    descriptor = None
    for klass in becontent_File.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_file_has_label():
    assert hasattr(becontent_File, "label")
    descriptor = None
    for klass in becontent_File.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_file_has_extension():
    assert hasattr(becontent_File, "extension")
    descriptor = None
    for klass in becontent_File.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_becontent_file_has_name():
    assert hasattr(becontent_File, "name")
    descriptor = None
    for klass in becontent_File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_textarea_is_not_abstract():
    assert not inspect.isabstract(becontent_Textarea)


def test_becontent_textarea_constructor_exists():
    assert callable(becontent_Textarea.__init__)


def test_becontent_textarea_constructor_args():
    sig = inspect.signature(becontent_Textarea.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "rows" in params, "Missing parameter 'rows'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_textarea_has_label():
    assert hasattr(becontent_Textarea, "label")
    descriptor = None
    for klass in becontent_Textarea.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_textarea_has_columns():
    assert hasattr(becontent_Textarea, "columns")
    descriptor = None
    for klass in becontent_Textarea.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_becontent_textarea_has_rows():
    assert hasattr(becontent_Textarea, "rows")
    descriptor = None
    for klass in becontent_Textarea.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_becontent_textarea_has_name():
    assert hasattr(becontent_Textarea, "name")
    descriptor = None
    for klass in becontent_Textarea.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_textarea_has_isMandatory():
    assert hasattr(becontent_Textarea, "isMandatory")
    descriptor = None
    for klass in becontent_Textarea.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_hierarchicalposition_is_not_abstract():
    assert not inspect.isabstract(becontent_HierarchicalPosition)


def test_becontent_hierarchicalposition_constructor_exists():
    assert callable(becontent_HierarchicalPosition.__init__)


def test_becontent_hierarchicalposition_constructor_args():
    sig = inspect.signature(becontent_HierarchicalPosition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "referenceField" in params, "Missing parameter 'referenceField'"
    assert "controlledField" in params, "Missing parameter 'controlledField'"

def test_becontent_hierarchicalposition_has_label():
    assert hasattr(becontent_HierarchicalPosition, "label")
    descriptor = None
    for klass in becontent_HierarchicalPosition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_hierarchicalposition_has_size():
    assert hasattr(becontent_HierarchicalPosition, "size")
    descriptor = None
    for klass in becontent_HierarchicalPosition.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent_hierarchicalposition_has_name():
    assert hasattr(becontent_HierarchicalPosition, "name")
    descriptor = None
    for klass in becontent_HierarchicalPosition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_hierarchicalposition_has_referenceField():
    assert hasattr(becontent_HierarchicalPosition, "referenceField")
    descriptor = None
    for klass in becontent_HierarchicalPosition.__mro__:
        if "referenceField" in klass.__dict__:
            descriptor = klass.__dict__["referenceField"]
            break
    assert isinstance(descriptor, property)

def test_becontent_hierarchicalposition_has_controlledField():
    assert hasattr(becontent_HierarchicalPosition, "controlledField")
    descriptor = None
    for klass in becontent_HierarchicalPosition.__mro__:
        if "controlledField" in klass.__dict__:
            descriptor = klass.__dict__["controlledField"]
            break
    assert isinstance(descriptor, property)



def test_becontent_hidden_is_not_abstract():
    assert not inspect.isabstract(becontent_Hidden)


def test_becontent_hidden_constructor_exists():
    assert callable(becontent_Hidden.__init__)


def test_becontent_hidden_constructor_args():
    sig = inspect.signature(becontent_Hidden.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "values" in params, "Missing parameter 'values'"

def test_becontent_hidden_has_name():
    assert hasattr(becontent_Hidden, "name")
    descriptor = None
    for klass in becontent_Hidden.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_hidden_has_values():
    assert hasattr(becontent_Hidden, "values")
    descriptor = None
    for klass in becontent_Hidden.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_becontent_position_is_not_abstract():
    assert not inspect.isabstract(becontent_Position)


def test_becontent_position_constructor_exists():
    assert callable(becontent_Position.__init__)


def test_becontent_position_constructor_args():
    sig = inspect.signature(becontent_Position.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "controlledField" in params, "Missing parameter 'controlledField'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_position_has_size():
    assert hasattr(becontent_Position, "size")
    descriptor = None
    for klass in becontent_Position.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent_position_has_controlledField():
    assert hasattr(becontent_Position, "controlledField")
    descriptor = None
    for klass in becontent_Position.__mro__:
        if "controlledField" in klass.__dict__:
            descriptor = klass.__dict__["controlledField"]
            break
    assert isinstance(descriptor, property)

def test_becontent_position_has_isMandatory():
    assert hasattr(becontent_Position, "isMandatory")
    descriptor = None
    for klass in becontent_Position.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_position_has_label():
    assert hasattr(becontent_Position, "label")
    descriptor = None
    for klass in becontent_Position.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_position_has_name():
    assert hasattr(becontent_Position, "name")
    descriptor = None
    for klass in becontent_Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_year_is_not_abstract():
    assert not inspect.isabstract(becontent_Year)


def test_becontent_year_constructor_exists():
    assert callable(becontent_Year.__init__)


def test_becontent_year_constructor_args():
    sig = inspect.signature(becontent_Year.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_becontent_year_has_name():
    assert hasattr(becontent_Year, "name")
    descriptor = None
    for klass in becontent_Year.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_year_has_isMandatory():
    assert hasattr(becontent_Year, "isMandatory")
    descriptor = None
    for klass in becontent_Year.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_year_has_label():
    assert hasattr(becontent_Year, "label")
    descriptor = None
    for klass in becontent_Year.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_year_has_end():
    assert hasattr(becontent_Year, "end")
    descriptor = None
    for klass in becontent_Year.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_becontent_year_has_start():
    assert hasattr(becontent_Year, "start")
    descriptor = None
    for klass in becontent_Year.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_becontent_date_is_not_abstract():
    assert not inspect.isabstract(becontent_Date)


def test_becontent_date_constructor_exists():
    assert callable(becontent_Date.__init__)


def test_becontent_date_constructor_args():
    sig = inspect.signature(becontent_Date.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_date_has_name():
    assert hasattr(becontent_Date, "name")
    descriptor = None
    for klass in becontent_Date.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_date_has_label():
    assert hasattr(becontent_Date, "label")
    descriptor = None
    for klass in becontent_Date.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_date_has_isMandatory():
    assert hasattr(becontent_Date, "isMandatory")
    descriptor = None
    for klass in becontent_Date.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_relationmanager_is_not_abstract():
    assert not inspect.isabstract(becontent_RelationManager)


def test_becontent_relationmanager_constructor_exists():
    assert callable(becontent_RelationManager.__init__)


def test_becontent_relationmanager_constructor_args():
    sig = inspect.signature(becontent_RelationManager.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "restrictCondition" in params, "Missing parameter 'restrictCondition'"
    assert "label" in params, "Missing parameter 'label'"

def test_becontent_relationmanager_has_orientation():
    assert hasattr(becontent_RelationManager, "orientation")
    descriptor = None
    for klass in becontent_RelationManager.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_becontent_relationmanager_has_name():
    assert hasattr(becontent_RelationManager, "name")
    descriptor = None
    for klass in becontent_RelationManager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_relationmanager_has_restrictCondition():
    assert hasattr(becontent_RelationManager, "restrictCondition")
    descriptor = None
    for klass in becontent_RelationManager.__mro__:
        if "restrictCondition" in klass.__dict__:
            descriptor = klass.__dict__["restrictCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent_relationmanager_has_label():
    assert hasattr(becontent_RelationManager, "label")
    descriptor = None
    for klass in becontent_RelationManager.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_becontent_link_is_not_abstract():
    assert not inspect.isabstract(becontent_Link)


def test_becontent_link_constructor_exists():
    assert callable(becontent_Link.__init__)


def test_becontent_link_constructor_args():
    sig = inspect.signature(becontent_Link.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_link_has_size():
    assert hasattr(becontent_Link, "size")
    descriptor = None
    for klass in becontent_Link.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent_link_has_isMandatory():
    assert hasattr(becontent_Link, "isMandatory")
    descriptor = None
    for klass in becontent_Link.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_link_has_maxLength():
    assert hasattr(becontent_Link, "maxLength")
    descriptor = None
    for klass in becontent_Link.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent_link_has_label():
    assert hasattr(becontent_Link, "label")
    descriptor = None
    for klass in becontent_Link.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_link_has_name():
    assert hasattr(becontent_Link, "name")
    descriptor = None
    for klass in becontent_Link.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_color_is_not_abstract():
    assert not inspect.isabstract(becontent_Color)


def test_becontent_color_constructor_exists():
    assert callable(becontent_Color.__init__)


def test_becontent_color_constructor_args():
    sig = inspect.signature(becontent_Color.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultColor" in params, "Missing parameter 'defaultColor'"

def test_becontent_color_has_label():
    assert hasattr(becontent_Color, "label")
    descriptor = None
    for klass in becontent_Color.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_color_has_name():
    assert hasattr(becontent_Color, "name")
    descriptor = None
    for klass in becontent_Color.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_color_has_defaultColor():
    assert hasattr(becontent_Color, "defaultColor")
    descriptor = None
    for klass in becontent_Color.__mro__:
        if "defaultColor" in klass.__dict__:
            descriptor = klass.__dict__["defaultColor"]
            break
    assert isinstance(descriptor, property)



def test_becontent_select_is_not_abstract():
    assert not inspect.isabstract(becontent_Select)


def test_becontent_select_constructor_exists():
    assert callable(becontent_Select.__init__)


def test_becontent_select_constructor_args():
    sig = inspect.signature(becontent_Select.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "label" in params, "Missing parameter 'label'"
    assert "values" in params, "Missing parameter 'values'"

def test_becontent_select_has_name():
    assert hasattr(becontent_Select, "name")
    descriptor = None
    for klass in becontent_Select.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_select_has_isMandatory():
    assert hasattr(becontent_Select, "isMandatory")
    descriptor = None
    for klass in becontent_Select.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_becontent_select_has_label():
    assert hasattr(becontent_Select, "label")
    descriptor = None
    for klass in becontent_Select.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_select_has_values():
    assert hasattr(becontent_Select, "values")
    descriptor = None
    for klass in becontent_Select.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_becontent_section_is_not_abstract():
    assert not inspect.isabstract(becontent_Section)


def test_becontent_section_constructor_exists():
    assert callable(becontent_Section.__init__)


def test_becontent_section_constructor_args():
    sig = inspect.signature(becontent_Section.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_section_has_text():
    assert hasattr(becontent_Section, "text")
    descriptor = None
    for klass in becontent_Section.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_becontent_section_has_name():
    assert hasattr(becontent_Section, "name")
    descriptor = None
    for klass in becontent_Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_form_is_not_abstract():
    assert not inspect.isabstract(Form)


def test_form_constructor_exists():
    assert callable(Form.__init__)


def test_form_constructor_args():
    sig = inspect.signature(Form.__init__)
    params = list(sig.parameters.keys())



def test_becontent_extendedform_is_not_abstract():
    assert not inspect.isabstract(becontent_ExtendedForm)


def test_becontent_extendedform_constructor_exists():
    assert callable(becontent_ExtendedForm.__init__)


def test_becontent_extendedform_constructor_args():
    sig = inspect.signature(becontent_ExtendedForm.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_becontent_extendedform_has_className():
    assert hasattr(becontent_ExtendedForm, "className")
    descriptor = None
    for klass in becontent_ExtendedForm.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_becontent_checkbox_is_not_abstract():
    assert not inspect.isabstract(becontent_Checkbox)


def test_becontent_checkbox_constructor_exists():
    assert callable(becontent_Checkbox.__init__)


def test_becontent_checkbox_constructor_args():
    sig = inspect.signature(becontent_Checkbox.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "value" in params, "Missing parameter 'value'"
    assert "isChecked" in params, "Missing parameter 'isChecked'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_checkbox_has_label():
    assert hasattr(becontent_Checkbox, "label")
    descriptor = None
    for klass in becontent_Checkbox.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_checkbox_has_value():
    assert hasattr(becontent_Checkbox, "value")
    descriptor = None
    for klass in becontent_Checkbox.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_becontent_checkbox_has_isChecked():
    assert hasattr(becontent_Checkbox, "isChecked")
    descriptor = None
    for klass in becontent_Checkbox.__mro__:
        if "isChecked" in klass.__dict__:
            descriptor = klass.__dict__["isChecked"]
            break
    assert isinstance(descriptor, property)

def test_becontent_checkbox_has_name():
    assert hasattr(becontent_Checkbox, "name")
    descriptor = None
    for klass in becontent_Checkbox.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_radiobutton_is_not_abstract():
    assert not inspect.isabstract(becontent_RadioButton)


def test_becontent_radiobutton_constructor_exists():
    assert callable(becontent_RadioButton.__init__)


def test_becontent_radiobutton_constructor_args():
    sig = inspect.signature(becontent_RadioButton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "values" in params, "Missing parameter 'values'"

def test_becontent_radiobutton_has_name():
    assert hasattr(becontent_RadioButton, "name")
    descriptor = None
    for klass in becontent_RadioButton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_radiobutton_has_label():
    assert hasattr(becontent_RadioButton, "label")
    descriptor = None
    for klass in becontent_RadioButton.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_radiobutton_has_values():
    assert hasattr(becontent_RadioButton, "values")
    descriptor = None
    for klass in becontent_RadioButton.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_becontent_text_is_not_abstract():
    assert not inspect.isabstract(becontent_Text)


def test_becontent_text_constructor_exists():
    assert callable(becontent_Text.__init__)


def test_becontent_text_constructor_args():
    sig = inspect.signature(becontent_Text.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_becontent_text_has_size():
    assert hasattr(becontent_Text, "size")
    descriptor = None
    for klass in becontent_Text.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_becontent_text_has_maxLength():
    assert hasattr(becontent_Text, "maxLength")
    descriptor = None
    for klass in becontent_Text.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_becontent_text_has_label():
    assert hasattr(becontent_Text, "label")
    descriptor = None
    for klass in becontent_Text.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_becontent_text_has_name():
    assert hasattr(becontent_Text, "name")
    descriptor = None
    for klass in becontent_Text.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_text_has_isMandatory():
    assert hasattr(becontent_Text, "isMandatory")
    descriptor = None
    for klass in becontent_Text.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_becontent_validation_is_not_abstract():
    assert not inspect.isabstract(becontent_Validation)


def test_becontent_validation_constructor_exists():
    assert callable(becontent_Validation.__init__)


def test_becontent_validation_constructor_args():
    sig = inspect.signature(becontent_Validation.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "message" in params, "Missing parameter 'message'"

def test_becontent_validation_has_condition():
    assert hasattr(becontent_Validation, "condition")
    descriptor = None
    for klass in becontent_Validation.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_becontent_validation_has__id_model():
    assert hasattr(becontent_Validation, "_id_model")
    descriptor = None
    for klass in becontent_Validation.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_validation_has_message():
    assert hasattr(becontent_Validation, "message")
    descriptor = None
    for klass in becontent_Validation.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_becontent_custompager_is_not_abstract():
    assert not inspect.isabstract(becontent_CustomPager)


def test_becontent_custompager_constructor_exists():
    assert callable(becontent_CustomPager.__init__)


def test_becontent_custompager_constructor_args():
    sig = inspect.signature(becontent_CustomPager.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "order" in params, "Missing parameter 'order'"
    assert "className" in params, "Missing parameter 'className'"
    assert "template" in params, "Missing parameter 'template'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "length" in params, "Missing parameter 'length'"
    assert "query" in params, "Missing parameter 'query'"

def test_becontent_custompager_has__id_model():
    assert hasattr(becontent_CustomPager, "_id_model")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_order():
    assert hasattr(becontent_CustomPager, "order")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_className():
    assert hasattr(becontent_CustomPager, "className")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_template():
    assert hasattr(becontent_CustomPager, "template")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_filter():
    assert hasattr(becontent_CustomPager, "filter")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_length():
    assert hasattr(becontent_CustomPager, "length")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_becontent_custompager_has_query():
    assert hasattr(becontent_CustomPager, "query")
    descriptor = None
    for klass in becontent_CustomPager.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_becontent_entitymanagerpage_is_not_abstract():
    assert not inspect.isabstract(becontent_EntityManagerPage)


def test_becontent_entitymanagerpage_constructor_exists():
    assert callable(becontent_EntityManagerPage.__init__)


def test_becontent_entitymanagerpage_constructor_args():
    sig = inspect.signature(becontent_EntityManagerPage.__init__)
    params = list(sig.parameters.keys())
    assert "skin" in params, "Missing parameter 'skin'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_becontent_entitymanagerpage_has_skin():
    assert hasattr(becontent_EntityManagerPage, "skin")
    descriptor = None
    for klass in becontent_EntityManagerPage.__mro__:
        if "skin" in klass.__dict__:
            descriptor = klass.__dict__["skin"]
            break
    assert isinstance(descriptor, property)

def test_becontent_entitymanagerpage_has_fileName():
    assert hasattr(becontent_EntityManagerPage, "fileName")
    descriptor = None
    for klass in becontent_EntityManagerPage.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_applycommand_is_not_abstract():
    assert not inspect.isabstract(ApplyCommand)


def test_applycommand_constructor_exists():
    assert callable(ApplyCommand.__init__)


def test_applycommand_constructor_args():
    sig = inspect.signature(ApplyCommand.__init__)
    params = list(sig.parameters.keys())



def test_becontent_applyitem_is_not_abstract():
    assert not inspect.isabstract(becontent_ApplyItem)


def test_becontent_applyitem_constructor_exists():
    assert callable(becontent_ApplyItem.__init__)


def test_becontent_applyitem_constructor_args():
    sig = inspect.signature(becontent_ApplyItem.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "key" in params, "Missing parameter 'key'"

def test_becontent_applyitem_has_prefix():
    assert hasattr(becontent_ApplyItem, "prefix")
    descriptor = None
    for klass in becontent_ApplyItem.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_becontent_applyitem_has_key():
    assert hasattr(becontent_ApplyItem, "key")
    descriptor = None
    for klass in becontent_ApplyItem.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_becontent_applyindexed_is_not_abstract():
    assert not inspect.isabstract(becontent_ApplyIndexed)


def test_becontent_applyindexed_constructor_exists():
    assert callable(becontent_ApplyIndexed.__init__)


def test_becontent_applyindexed_constructor_args():
    sig = inspect.signature(becontent_ApplyIndexed.__init__)
    params = list(sig.parameters.keys())



def test_becontent_apply_is_not_abstract():
    assert not inspect.isabstract(becontent_Apply)


def test_becontent_apply_constructor_exists():
    assert callable(becontent_Apply.__init__)


def test_becontent_apply_constructor_args():
    sig = inspect.signature(becontent_Apply.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_becontent_apply_has_prefix():
    assert hasattr(becontent_Apply, "prefix")
    descriptor = None
    for klass in becontent_Apply.__mro__:
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



def test_becontent_form_is_not_abstract():
    assert not inspect.isabstract(becontent_Form)


def test_becontent_form_constructor_exists():
    assert callable(becontent_Form.__init__)


def test_becontent_form_constructor_args():
    sig = inspect.signature(becontent_Form.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"

def test_becontent_form_has_description():
    assert hasattr(becontent_Form, "description")
    descriptor = None
    for klass in becontent_Form.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_becontent_form_has_name():
    assert hasattr(becontent_Form, "name")
    descriptor = None
    for klass in becontent_Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_form_has_method():
    assert hasattr(becontent_Form, "method")
    descriptor = None
    for klass in becontent_Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_becontent_notstructuredelement_is_not_abstract():
    assert not inspect.isabstract(becontent_NotStructuredElement)


def test_becontent_notstructuredelement_constructor_exists():
    assert callable(becontent_NotStructuredElement.__init__)


def test_becontent_notstructuredelement_constructor_args():
    sig = inspect.signature(becontent_NotStructuredElement.__init__)
    params = list(sig.parameters.keys())
    assert "helper" in params, "Missing parameter 'helper'"

def test_becontent_notstructuredelement_has_helper():
    assert hasattr(becontent_NotStructuredElement, "helper")
    descriptor = None
    for klass in becontent_NotStructuredElement.__mro__:
        if "helper" in klass.__dict__:
            descriptor = klass.__dict__["helper"]
            break
    assert isinstance(descriptor, property)



def test_becontent_formelement_is_not_abstract():
    assert not inspect.isabstract(becontent_FormElement)


def test_becontent_formelement_constructor_exists():
    assert callable(becontent_FormElement.__init__)


def test_becontent_formelement_constructor_args():
    sig = inspect.signature(becontent_FormElement.__init__)
    params = list(sig.parameters.keys())



def test_becontent_conditionaltemplate_is_not_abstract():
    assert not inspect.isabstract(becontent_ConditionalTemplate)


def test_becontent_conditionaltemplate_constructor_exists():
    assert callable(becontent_ConditionalTemplate.__init__)


def test_becontent_conditionaltemplate_constructor_args():
    sig = inspect.signature(becontent_ConditionalTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "trueTemplate" in params, "Missing parameter 'trueTemplate'"
    assert "conditionExp" in params, "Missing parameter 'conditionExp'"
    assert "falseTemplate" in params, "Missing parameter 'falseTemplate'"

def test_becontent_conditionaltemplate_has_fieldName():
    assert hasattr(becontent_ConditionalTemplate, "fieldName")
    descriptor = None
    for klass in becontent_ConditionalTemplate.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_becontent_conditionaltemplate_has__id_model():
    assert hasattr(becontent_ConditionalTemplate, "_id_model")
    descriptor = None
    for klass in becontent_ConditionalTemplate.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_conditionaltemplate_has_trueTemplate():
    assert hasattr(becontent_ConditionalTemplate, "trueTemplate")
    descriptor = None
    for klass in becontent_ConditionalTemplate.__mro__:
        if "trueTemplate" in klass.__dict__:
            descriptor = klass.__dict__["trueTemplate"]
            break
    assert isinstance(descriptor, property)

def test_becontent_conditionaltemplate_has_conditionExp():
    assert hasattr(becontent_ConditionalTemplate, "conditionExp")
    descriptor = None
    for klass in becontent_ConditionalTemplate.__mro__:
        if "conditionExp" in klass.__dict__:
            descriptor = klass.__dict__["conditionExp"]
            break
    assert isinstance(descriptor, property)

def test_becontent_conditionaltemplate_has_falseTemplate():
    assert hasattr(becontent_ConditionalTemplate, "falseTemplate")
    descriptor = None
    for klass in becontent_ConditionalTemplate.__mro__:
        if "falseTemplate" in klass.__dict__:
            descriptor = klass.__dict__["falseTemplate"]
            break
    assert isinstance(descriptor, property)



def test_becontent_contentcommand_is_not_abstract():
    assert not inspect.isabstract(becontent_ContentCommand)


def test_becontent_contentcommand_constructor_exists():
    assert callable(becontent_ContentCommand.__init__)


def test_becontent_contentcommand_constructor_args():
    sig = inspect.signature(becontent_ContentCommand.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent_contentcommand_has__id_model():
    assert hasattr(becontent_ContentCommand, "_id_model")
    descriptor = None
    for klass in becontent_ContentCommand.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_becontent_joinentity_is_not_abstract():
    assert not inspect.isabstract(becontent_JoinEntity)


def test_becontent_joinentity_constructor_exists():
    assert callable(becontent_JoinEntity.__init__)


def test_becontent_joinentity_constructor_args():
    sig = inspect.signature(becontent_JoinEntity.__init__)
    params = list(sig.parameters.keys())
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent_joinentity_has__id_model():
    assert hasattr(becontent_JoinEntity, "_id_model")
    descriptor = None
    for klass in becontent_JoinEntity.__mro__:
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



def test_becontent_unsetparameter_is_not_abstract():
    assert not inspect.isabstract(becontent_UnsetParameter)


def test_becontent_unsetparameter_constructor_exists():
    assert callable(becontent_UnsetParameter.__init__)


def test_becontent_unsetparameter_constructor_args():
    sig = inspect.signature(becontent_UnsetParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_unsetparameter_has_name():
    assert hasattr(becontent_UnsetParameter, "name")
    descriptor = None
    for klass in becontent_UnsetParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_becontent_applycommand_is_not_abstract():
    assert not inspect.isabstract(becontent_ApplyCommand)


def test_becontent_applycommand_constructor_exists():
    assert callable(becontent_ApplyCommand.__init__)


def test_becontent_applycommand_constructor_args():
    sig = inspect.signature(becontent_ApplyCommand.__init__)
    params = list(sig.parameters.keys())



def test_becontent_copy_is_not_abstract():
    assert not inspect.isabstract(becontent_Copy)


def test_becontent_copy_constructor_exists():
    assert callable(becontent_Copy.__init__)


def test_becontent_copy_constructor_args():
    sig = inspect.signature(becontent_Copy.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName1" in params, "Missing parameter 'fieldName1'"
    assert "fieldName2" in params, "Missing parameter 'fieldName2'"

def test_becontent_copy_has_fieldName1():
    assert hasattr(becontent_Copy, "fieldName1")
    descriptor = None
    for klass in becontent_Copy.__mro__:
        if "fieldName1" in klass.__dict__:
            descriptor = klass.__dict__["fieldName1"]
            break
    assert isinstance(descriptor, property)

def test_becontent_copy_has_fieldName2():
    assert hasattr(becontent_Copy, "fieldName2")
    descriptor = None
    for klass in becontent_Copy.__mro__:
        if "fieldName2" in klass.__dict__:
            descriptor = klass.__dict__["fieldName2"]
            break
    assert isinstance(descriptor, property)



def test_becontent_trigger_is_not_abstract():
    assert not inspect.isabstract(becontent_Trigger)


def test_becontent_trigger_constructor_exists():
    assert callable(becontent_Trigger.__init__)


def test_becontent_trigger_constructor_args():
    sig = inspect.signature(becontent_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_becontent_trigger_has_name():
    assert hasattr(becontent_Trigger, "name")
    descriptor = None
    for klass in becontent_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_becontent_trigger_has_value():
    assert hasattr(becontent_Trigger, "value")
    descriptor = None
    for klass in becontent_Trigger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_becontent_propagate_is_not_abstract():
    assert not inspect.isabstract(becontent_Propagate)


def test_becontent_propagate_constructor_exists():
    assert callable(becontent_Propagate.__init__)


def test_becontent_propagate_constructor_args():
    sig = inspect.signature(becontent_Propagate.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName1" in params, "Missing parameter 'fieldName1'"
    assert "fieldName2" in params, "Missing parameter 'fieldName2'"

def test_becontent_propagate_has_fieldName1():
    assert hasattr(becontent_Propagate, "fieldName1")
    descriptor = None
    for klass in becontent_Propagate.__mro__:
        if "fieldName1" in klass.__dict__:
            descriptor = klass.__dict__["fieldName1"]
            break
    assert isinstance(descriptor, property)

def test_becontent_propagate_has_fieldName2():
    assert hasattr(becontent_Propagate, "fieldName2")
    descriptor = None
    for klass in becontent_Propagate.__mro__:
        if "fieldName2" in klass.__dict__:
            descriptor = klass.__dict__["fieldName2"]
            break
    assert isinstance(descriptor, property)



def test_becontent_parameter_is_not_abstract():
    assert not inspect.isabstract(becontent_Parameter)


def test_becontent_parameter_constructor_exists():
    assert callable(becontent_Parameter.__init__)


def test_becontent_parameter_constructor_args():
    sig = inspect.signature(becontent_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_parameter_has_value():
    assert hasattr(becontent_Parameter, "value")
    descriptor = None
    for klass in becontent_Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_becontent_parameter_has_name():
    assert hasattr(becontent_Parameter, "name")
    descriptor = None
    for klass in becontent_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewitem_is_not_abstract():
    assert not inspect.isabstract(ViewItem)


def test_viewitem_constructor_exists():
    assert callable(ViewItem.__init__)


def test_viewitem_constructor_args():
    sig = inspect.signature(ViewItem.__init__)
    params = list(sig.parameters.keys())



def test_becontent_skinlet_is_not_abstract():
    assert not inspect.isabstract(becontent_Skinlet)


def test_becontent_skinlet_constructor_exists():
    assert callable(becontent_Skinlet.__init__)


def test_becontent_skinlet_constructor_args():
    sig = inspect.signature(becontent_Skinlet.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent_skinlet_has_template():
    assert hasattr(becontent_Skinlet, "template")
    descriptor = None
    for klass in becontent_Skinlet.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_becontent_skinlet_has__id_model():
    assert hasattr(becontent_Skinlet, "_id_model")
    descriptor = None
    for klass in becontent_Skinlet.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_becontent_content_is_not_abstract():
    assert not inspect.isabstract(becontent_Content)


def test_becontent_content_constructor_exists():
    assert callable(becontent_Content.__init__)


def test_becontent_content_constructor_args():
    sig = inspect.signature(becontent_Content.__init__)
    params = list(sig.parameters.keys())
    assert "orderFields" in params, "Missing parameter 'orderFields'"
    assert "style" in params, "Missing parameter 'style'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "_id_model" in params, "Missing parameter '_id_model'"
    assert "joinCondition" in params, "Missing parameter 'joinCondition'"
    assert "presentationFields" in params, "Missing parameter 'presentationFields'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "template" in params, "Missing parameter 'template'"

def test_becontent_content_has_orderFields():
    assert hasattr(becontent_Content, "orderFields")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "orderFields" in klass.__dict__:
            descriptor = klass.__dict__["orderFields"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_style():
    assert hasattr(becontent_Content, "style")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_limit():
    assert hasattr(becontent_Content, "limit")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has__id_model():
    assert hasattr(becontent_Content, "_id_model")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_joinCondition():
    assert hasattr(becontent_Content, "joinCondition")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "joinCondition" in klass.__dict__:
            descriptor = klass.__dict__["joinCondition"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_presentationFields():
    assert hasattr(becontent_Content, "presentationFields")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "presentationFields" in klass.__dict__:
            descriptor = klass.__dict__["presentationFields"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_filter():
    assert hasattr(becontent_Content, "filter")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)

def test_becontent_content_has_template():
    assert hasattr(becontent_Content, "template")
    descriptor = None
    for klass in becontent_Content.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_becontent_template_is_not_abstract():
    assert not inspect.isabstract(becontent_Template)


def test_becontent_template_constructor_exists():
    assert callable(becontent_Template.__init__)


def test_becontent_template_constructor_args():
    sig = inspect.signature(becontent_Template.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "_id_model" in params, "Missing parameter '_id_model'"

def test_becontent_template_has_path():
    assert hasattr(becontent_Template, "path")
    descriptor = None
    for klass in becontent_Template.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_becontent_template_has__id_model():
    assert hasattr(becontent_Template, "_id_model")
    descriptor = None
    for klass in becontent_Template.__mro__:
        if "_id_model" in klass.__dict__:
            descriptor = klass.__dict__["_id_model"]
            break
    assert isinstance(descriptor, property)



def test_becontent_skin_is_not_abstract():
    assert not inspect.isabstract(becontent_Skin)


def test_becontent_skin_constructor_exists():
    assert callable(becontent_Skin.__init__)


def test_becontent_skin_constructor_args():
    sig = inspect.signature(becontent_Skin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_becontent_skin_has_name():
    assert hasattr(becontent_Skin, "name")
    descriptor = None
    for klass in becontent_Skin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_contentstyle_exists():
    # Check that the Enumeration exists
    assert ContentStyle is not None

def test_contentstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContentStyle]
    expected_literals = [
        "normal",
        "hierarchical",
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

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "equal",
        "dateLessEqual",
        "implies",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"

def test_formmethodtype_exists():
    # Check that the Enumeration exists
    assert FormMethodType is not None

def test_formmethodtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FormMethodType]
    expected_literals = [
        "get",
        "post",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FormMethodType"


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
becontent_ViewItem_strategy = st.builds(
    becontent_ViewItem,
)
TypedSystemAttribute_strategy = st.builds(
    TypedSystemAttribute,
)
becontent_SystemAttributePassword_strategy = st.builds(
    becontent_SystemAttributePassword,
)
becontent_SystemAttributePosition_strategy = st.builds(
    becontent_SystemAttributePosition,
)
becontent_SystemAttributeText_strategy = st.builds(
    becontent_SystemAttributeText,
)
becontent_SystemAttributeLongDate_strategy = st.builds(
    becontent_SystemAttributeLongDate,
)
becontent_SystemAttributeDate_strategy = st.builds(
    becontent_SystemAttributeDate,
)
becontent_SystemAttributeColor_strategy = st.builds(
    becontent_SystemAttributeColor,
)
SystemEntityField_strategy = st.builds(
    SystemEntityField,
)
becontent_TypedSystemAttribute_strategy = st.builds(
    becontent_TypedSystemAttribute,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_SystemReference_strategy = st.builds(
    becontent_SystemReference,
    name=
        safe_text
)
becontent_SystemAttributeFileToFolder_strategy = st.builds(
    becontent_SystemAttributeFileToFolder,
)
becontent_SystemAttributeFile_strategy = st.builds(
    becontent_SystemAttributeFile,
)
becontent_SystemAttributeVarchar_strategy = st.builds(
    becontent_SystemAttributeVarchar,
    isPrimaryKey=
        st.booleans(),
    length=
        st.integers()
)
becontent_SystemAttributeInteger_strategy = st.builds(
    becontent_SystemAttributeInteger,
    isPrimaryKey=
        st.booleans()
)
becontent_SystemAttributeImage_strategy = st.builds(
    becontent_SystemAttributeImage,
)
TypedAttribute_strategy = st.builds(
    TypedAttribute,
)
becontent_AttributeFileToFolder_strategy = st.builds(
    becontent_AttributeFileToFolder,
)
becontent_AttributeColor_strategy = st.builds(
    becontent_AttributeColor,
)
EntityField_strategy = st.builds(
    EntityField,
)
becontent_TypedAttribute_strategy = st.builds(
    becontent_TypedAttribute,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_Reference_strategy = st.builds(
    becontent_Reference,
    name=
        safe_text
)
becontent_AttributeFile_strategy = st.builds(
    becontent_AttributeFile,
)
becontent_AttributeVarchar_strategy = st.builds(
    becontent_AttributeVarchar,
    length=
        st.integers(),
    isPrimaryKey=
        st.booleans()
)
becontent_AttributeInteger_strategy = st.builds(
    becontent_AttributeInteger,
    isPrimaryKey=
        st.booleans()
)
becontent_AttributeImage_strategy = st.builds(
    becontent_AttributeImage,
)
becontent_AttributePosition_strategy = st.builds(
    becontent_AttributePosition,
)
becontent_AttributePassword_strategy = st.builds(
    becontent_AttributePassword,
)
becontent_AttributeText_strategy = st.builds(
    becontent_AttributeText,
)
becontent_AttributeLongDate_strategy = st.builds(
    becontent_AttributeLongDate,
)
becontent_AttributeDate_strategy = st.builds(
    becontent_AttributeDate,
)
becontent_EntityField_strategy = st.builds(
    becontent_EntityField,
    isTextSearch=
        st.booleans(),
    isSearchPresentationHead=
        st.booleans(),
    isPresented=
        st.booleans(),
    isSearchPresentationBody=
        st.booleans()
)
DefinitionItem_strategy = st.builds(
    DefinitionItem,
)
becontent_Entity_strategy = st.builds(
    becontent_Entity,
    rssFilter=
        safe_text,
    variableName=
        safe_text,
    name=
        safe_text,
    presentationString=
        safe_text,
    isOwned=
        st.booleans()
)
BeContentElement_strategy = st.builds(
    BeContentElement,
)
becontent_FileToFolderExtension_strategy = st.builds(
    becontent_FileToFolderExtension,
    extensionValue=
        safe_text,
    _id_model=
        safe_text,
    extensionKey=
        safe_text
)
becontent_DefinitionItem_strategy = st.builds(
    becontent_DefinitionItem,
)
becontent_BeContentElement_strategy = st.builds(
    becontent_BeContentElement,
)
becontent_BeContentModel_strategy = st.builds(
    becontent_BeContentModel,
)
Relation_strategy = st.builds(
    Relation,
)
becontent_SystemRelation_strategy = st.builds(
    becontent_SystemRelation,
)
becontent_CustomRelation_strategy = st.builds(
    becontent_CustomRelation,
)
becontent_Relation_strategy = st.builds(
    becontent_Relation,
    name=
        safe_text,
    variableName=
        safe_text
)
becontent_SystemEntityField_strategy = st.builds(
    becontent_SystemEntityField,
    isTextSearch=
        st.booleans(),
    isSearchPresentationHead=
        st.booleans(),
    isSearchPresentationBody=
        st.booleans(),
    isPresented=
        st.booleans()
)
Entity_strategy = st.builds(
    Entity,
)
becontent_SystemEntity_strategy = st.builds(
    becontent_SystemEntity,
)
becontent_CustomEntity_strategy = st.builds(
    becontent_CustomEntity,
)
becontent_Handler_strategy = st.builds(
    becontent_Handler,
    mainSkinPagerLength=
        st.integers(),
    fileName=
        safe_text,
    mainSkinWithPager=
        st.booleans(),
    mainSkinPlaceholder=
        safe_text
)
becontent_Channel_strategy = st.builds(
    becontent_Channel,
    _id_model=
        safe_text,
    parameters=
        safe_text
)
NotStructuredElement_strategy = st.builds(
    NotStructuredElement,
)
becontent_FileToFolder_strategy = st.builds(
    becontent_FileToFolder,
    extension=
        safe_text,
    label=
        safe_text,
    extensionMessage=
        safe_text,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_Password_strategy = st.builds(
    becontent_Password,
    isMandatory=
        st.booleans(),
    size=
        st.integers(),
    label=
        safe_text,
    maxLength=
        st.integers(),
    name=
        safe_text
)
becontent_LongDate_strategy = st.builds(
    becontent_LongDate,
    isMandatory=
        st.booleans(),
    name=
        safe_text,
    label=
        safe_text
)
becontent_Editor_strategy = st.builds(
    becontent_Editor,
    name=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    rows=
        st.integers(),
    columns=
        st.integers()
)
becontent_RadioFromReference_strategy = st.builds(
    becontent_RadioFromReference,
    isMandatory=
        st.booleans(),
    restrictCondition=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
becontent_SelectFromReference_strategy = st.builds(
    becontent_SelectFromReference,
    restrictCondition=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    name=
        safe_text
)
becontent_Image_strategy = st.builds(
    becontent_Image,
    label=
        safe_text,
    isMandatory=
        st.booleans(),
    name=
        safe_text
)
becontent_File_strategy = st.builds(
    becontent_File,
    extensionMessage=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    extension=
        safe_text,
    name=
        safe_text
)
becontent_Textarea_strategy = st.builds(
    becontent_Textarea,
    label=
        safe_text,
    columns=
        st.integers(),
    rows=
        st.integers(),
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_HierarchicalPosition_strategy = st.builds(
    becontent_HierarchicalPosition,
    label=
        safe_text,
    size=
        st.integers(),
    name=
        safe_text,
    referenceField=
        safe_text,
    controlledField=
        safe_text
)
becontent_Hidden_strategy = st.builds(
    becontent_Hidden,
    name=
        safe_text,
    values=
        safe_text
)
becontent_Position_strategy = st.builds(
    becontent_Position,
    size=
        st.integers(),
    controlledField=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    name=
        safe_text
)
becontent_Year_strategy = st.builds(
    becontent_Year,
    name=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    end=
        st.integers(),
    start=
        st.integers()
)
becontent_Date_strategy = st.builds(
    becontent_Date,
    name=
        safe_text,
    label=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_RelationManager_strategy = st.builds(
    becontent_RelationManager,
    orientation=
        safe_text,
    name=
        safe_text,
    restrictCondition=
        safe_text,
    label=
        safe_text
)
becontent_Link_strategy = st.builds(
    becontent_Link,
    size=
        st.integers(),
    isMandatory=
        st.booleans(),
    maxLength=
        st.integers(),
    label=
        safe_text,
    name=
        safe_text
)
becontent_Color_strategy = st.builds(
    becontent_Color,
    label=
        safe_text,
    name=
        safe_text,
    defaultColor=
        safe_text
)
becontent_Select_strategy = st.builds(
    becontent_Select,
    name=
        safe_text,
    isMandatory=
        st.booleans(),
    label=
        safe_text,
    values=
        safe_text
)
becontent_Section_strategy = st.builds(
    becontent_Section,
    text=
        safe_text,
    name=
        safe_text
)
Form_strategy = st.builds(
    Form,
)
becontent_ExtendedForm_strategy = st.builds(
    becontent_ExtendedForm,
    className=
        safe_text
)
becontent_Checkbox_strategy = st.builds(
    becontent_Checkbox,
    label=
        safe_text,
    value=
        safe_text,
    isChecked=
        st.booleans(),
    name=
        safe_text
)
becontent_RadioButton_strategy = st.builds(
    becontent_RadioButton,
    name=
        safe_text,
    label=
        safe_text,
    values=
        safe_text
)
becontent_Text_strategy = st.builds(
    becontent_Text,
    size=
        st.integers(),
    maxLength=
        st.integers(),
    label=
        safe_text,
    name=
        safe_text,
    isMandatory=
        st.booleans()
)
becontent_Validation_strategy = st.builds(
    becontent_Validation,
    condition=
        safe_text,
    _id_model=
        safe_text,
    message=
        safe_text
)
becontent_CustomPager_strategy = st.builds(
    becontent_CustomPager,
    _id_model=
        safe_text,
    order=
        safe_text,
    className=
        safe_text,
    template=
        safe_text,
    filter=
        safe_text,
    length=
        st.integers(),
    query=
        safe_text
)
becontent_EntityManagerPage_strategy = st.builds(
    becontent_EntityManagerPage,
    skin=
        safe_text,
    fileName=
        safe_text
)
ApplyCommand_strategy = st.builds(
    ApplyCommand,
)
becontent_ApplyItem_strategy = st.builds(
    becontent_ApplyItem,
    prefix=
        safe_text,
    key=
        safe_text
)
becontent_ApplyIndexed_strategy = st.builds(
    becontent_ApplyIndexed,
)
becontent_Apply_strategy = st.builds(
    becontent_Apply,
    prefix=
        safe_text
)
FormElement_strategy = st.builds(
    FormElement,
)
becontent_Form_strategy = st.builds(
    becontent_Form,
    description=
        safe_text,
    name=
        safe_text,
    method=
        safe_text
)
becontent_NotStructuredElement_strategy = st.builds(
    becontent_NotStructuredElement,
    helper=
        safe_text
)
becontent_FormElement_strategy = st.builds(
    becontent_FormElement,
)
becontent_ConditionalTemplate_strategy = st.builds(
    becontent_ConditionalTemplate,
    fieldName=
        safe_text,
    _id_model=
        safe_text,
    trueTemplate=
        safe_text,
    conditionExp=
        safe_text,
    falseTemplate=
        safe_text
)
becontent_ContentCommand_strategy = st.builds(
    becontent_ContentCommand,
    _id_model=
        safe_text
)
becontent_JoinEntity_strategy = st.builds(
    becontent_JoinEntity,
    _id_model=
        safe_text
)
ContentCommand_strategy = st.builds(
    ContentCommand,
)
becontent_UnsetParameter_strategy = st.builds(
    becontent_UnsetParameter,
    name=
        safe_text
)
becontent_ApplyCommand_strategy = st.builds(
    becontent_ApplyCommand,
)
becontent_Copy_strategy = st.builds(
    becontent_Copy,
    fieldName1=
        safe_text,
    fieldName2=
        safe_text
)
becontent_Trigger_strategy = st.builds(
    becontent_Trigger,
    name=
        safe_text,
    value=
        safe_text
)
becontent_Propagate_strategy = st.builds(
    becontent_Propagate,
    fieldName1=
        safe_text,
    fieldName2=
        safe_text
)
becontent_Parameter_strategy = st.builds(
    becontent_Parameter,
    value=
        safe_text,
    name=
        safe_text
)
ViewItem_strategy = st.builds(
    ViewItem,
)
becontent_Skinlet_strategy = st.builds(
    becontent_Skinlet,
    template=
        safe_text,
    _id_model=
        safe_text
)
becontent_Content_strategy = st.builds(
    becontent_Content,
    orderFields=
        safe_text,
    style=
        safe_text,
    limit=
        st.integers(),
    _id_model=
        safe_text,
    joinCondition=
        safe_text,
    presentationFields=
        safe_text,
    filter=
        safe_text,
    template=
        safe_text
)
becontent_Template_strategy = st.builds(
    becontent_Template,
    path=
        safe_text,
    _id_model=
        safe_text
)
becontent_Skin_strategy = st.builds(
    becontent_Skin,
    name=
        safe_text
)

@given(instance=becontent_ViewItem_strategy)
@settings(max_examples=50)
def test_becontent_viewitem_instantiation(instance):
    assert isinstance(instance, becontent_ViewItem)

@given(instance=TypedSystemAttribute_strategy)
@settings(max_examples=50)
def test_typedsystemattribute_instantiation(instance):
    assert isinstance(instance, TypedSystemAttribute)

@given(instance=becontent_SystemAttributePassword_strategy)
@settings(max_examples=50)
def test_becontent_systemattributepassword_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributePassword)

@given(instance=becontent_SystemAttributePosition_strategy)
@settings(max_examples=50)
def test_becontent_systemattributeposition_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributePosition)

@given(instance=becontent_SystemAttributeText_strategy)
@settings(max_examples=50)
def test_becontent_systemattributetext_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeText)

@given(instance=becontent_SystemAttributeLongDate_strategy)
@settings(max_examples=50)
def test_becontent_systemattributelongdate_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeLongDate)

@given(instance=becontent_SystemAttributeDate_strategy)
@settings(max_examples=50)
def test_becontent_systemattributedate_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeDate)

@given(instance=becontent_SystemAttributeColor_strategy)
@settings(max_examples=50)
def test_becontent_systemattributecolor_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeColor)

@given(instance=SystemEntityField_strategy)
@settings(max_examples=50)
def test_systementityfield_instantiation(instance):
    assert isinstance(instance, SystemEntityField)

@given(instance=becontent_TypedSystemAttribute_strategy)
@settings(max_examples=50)
def test_becontent_typedsystemattribute_instantiation(instance):
    assert isinstance(instance, becontent_TypedSystemAttribute)



@given(instance=becontent_TypedSystemAttribute_strategy)
def test_becontent_typedsystemattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_TypedSystemAttribute_strategy)
def test_becontent_typedsystemattribute_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_SystemReference_strategy)
@settings(max_examples=50)
def test_becontent_systemreference_instantiation(instance):
    assert isinstance(instance, becontent_SystemReference)



@given(instance=becontent_SystemReference_strategy)
def test_becontent_systemreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_SystemAttributeFileToFolder_strategy)
@settings(max_examples=50)
def test_becontent_systemattributefiletofolder_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeFileToFolder)

@given(instance=becontent_SystemAttributeFile_strategy)
@settings(max_examples=50)
def test_becontent_systemattributefile_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeFile)

@given(instance=becontent_SystemAttributeVarchar_strategy)
@settings(max_examples=50)
def test_becontent_systemattributevarchar_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeVarchar)



@given(instance=becontent_SystemAttributeVarchar_strategy)
def test_becontent_systemattributevarchar_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original



@given(instance=becontent_SystemAttributeVarchar_strategy)
def test_becontent_systemattributevarchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=becontent_SystemAttributeInteger_strategy)
@settings(max_examples=50)
def test_becontent_systemattributeinteger_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeInteger)



@given(instance=becontent_SystemAttributeInteger_strategy)
def test_becontent_systemattributeinteger_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent_SystemAttributeImage_strategy)
@settings(max_examples=50)
def test_becontent_systemattributeimage_instantiation(instance):
    assert isinstance(instance, becontent_SystemAttributeImage)

@given(instance=TypedAttribute_strategy)
@settings(max_examples=50)
def test_typedattribute_instantiation(instance):
    assert isinstance(instance, TypedAttribute)

@given(instance=becontent_AttributeFileToFolder_strategy)
@settings(max_examples=50)
def test_becontent_attributefiletofolder_instantiation(instance):
    assert isinstance(instance, becontent_AttributeFileToFolder)

@given(instance=becontent_AttributeColor_strategy)
@settings(max_examples=50)
def test_becontent_attributecolor_instantiation(instance):
    assert isinstance(instance, becontent_AttributeColor)

@given(instance=EntityField_strategy)
@settings(max_examples=50)
def test_entityfield_instantiation(instance):
    assert isinstance(instance, EntityField)

@given(instance=becontent_TypedAttribute_strategy)
@settings(max_examples=50)
def test_becontent_typedattribute_instantiation(instance):
    assert isinstance(instance, becontent_TypedAttribute)



@given(instance=becontent_TypedAttribute_strategy)
def test_becontent_typedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_TypedAttribute_strategy)
def test_becontent_typedattribute_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_Reference_strategy)
@settings(max_examples=50)
def test_becontent_reference_instantiation(instance):
    assert isinstance(instance, becontent_Reference)



@given(instance=becontent_Reference_strategy)
def test_becontent_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_AttributeFile_strategy)
@settings(max_examples=50)
def test_becontent_attributefile_instantiation(instance):
    assert isinstance(instance, becontent_AttributeFile)

@given(instance=becontent_AttributeVarchar_strategy)
@settings(max_examples=50)
def test_becontent_attributevarchar_instantiation(instance):
    assert isinstance(instance, becontent_AttributeVarchar)



@given(instance=becontent_AttributeVarchar_strategy)
def test_becontent_attributevarchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=becontent_AttributeVarchar_strategy)
def test_becontent_attributevarchar_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent_AttributeInteger_strategy)
@settings(max_examples=50)
def test_becontent_attributeinteger_instantiation(instance):
    assert isinstance(instance, becontent_AttributeInteger)



@given(instance=becontent_AttributeInteger_strategy)
def test_becontent_attributeinteger_isPrimaryKey_setter(instance):
    original = instance.isPrimaryKey
    instance.isPrimaryKey = original
    assert instance.isPrimaryKey == original

@given(instance=becontent_AttributeImage_strategy)
@settings(max_examples=50)
def test_becontent_attributeimage_instantiation(instance):
    assert isinstance(instance, becontent_AttributeImage)

@given(instance=becontent_AttributePosition_strategy)
@settings(max_examples=50)
def test_becontent_attributeposition_instantiation(instance):
    assert isinstance(instance, becontent_AttributePosition)

@given(instance=becontent_AttributePassword_strategy)
@settings(max_examples=50)
def test_becontent_attributepassword_instantiation(instance):
    assert isinstance(instance, becontent_AttributePassword)

@given(instance=becontent_AttributeText_strategy)
@settings(max_examples=50)
def test_becontent_attributetext_instantiation(instance):
    assert isinstance(instance, becontent_AttributeText)

@given(instance=becontent_AttributeLongDate_strategy)
@settings(max_examples=50)
def test_becontent_attributelongdate_instantiation(instance):
    assert isinstance(instance, becontent_AttributeLongDate)

@given(instance=becontent_AttributeDate_strategy)
@settings(max_examples=50)
def test_becontent_attributedate_instantiation(instance):
    assert isinstance(instance, becontent_AttributeDate)

@given(instance=becontent_EntityField_strategy)
@settings(max_examples=50)
def test_becontent_entityfield_instantiation(instance):
    assert isinstance(instance, becontent_EntityField)



@given(instance=becontent_EntityField_strategy)
def test_becontent_entityfield_isTextSearch_setter(instance):
    original = instance.isTextSearch
    instance.isTextSearch = original
    assert instance.isTextSearch == original



@given(instance=becontent_EntityField_strategy)
def test_becontent_entityfield_isSearchPresentationHead_setter(instance):
    original = instance.isSearchPresentationHead
    instance.isSearchPresentationHead = original
    assert instance.isSearchPresentationHead == original



@given(instance=becontent_EntityField_strategy)
def test_becontent_entityfield_isPresented_setter(instance):
    original = instance.isPresented
    instance.isPresented = original
    assert instance.isPresented == original



@given(instance=becontent_EntityField_strategy)
def test_becontent_entityfield_isSearchPresentationBody_setter(instance):
    original = instance.isSearchPresentationBody
    instance.isSearchPresentationBody = original
    assert instance.isSearchPresentationBody == original

@given(instance=DefinitionItem_strategy)
@settings(max_examples=50)
def test_definitionitem_instantiation(instance):
    assert isinstance(instance, DefinitionItem)

@given(instance=becontent_Entity_strategy)
@settings(max_examples=50)
def test_becontent_entity_instantiation(instance):
    assert isinstance(instance, becontent_Entity)



@given(instance=becontent_Entity_strategy)
def test_becontent_entity_rssFilter_setter(instance):
    original = instance.rssFilter
    instance.rssFilter = original
    assert instance.rssFilter == original



@given(instance=becontent_Entity_strategy)
def test_becontent_entity_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=becontent_Entity_strategy)
def test_becontent_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Entity_strategy)
def test_becontent_entity_presentationString_setter(instance):
    original = instance.presentationString
    instance.presentationString = original
    assert instance.presentationString == original



@given(instance=becontent_Entity_strategy)
def test_becontent_entity_isOwned_setter(instance):
    original = instance.isOwned
    instance.isOwned = original
    assert instance.isOwned == original

@given(instance=BeContentElement_strategy)
@settings(max_examples=50)
def test_becontentelement_instantiation(instance):
    assert isinstance(instance, BeContentElement)

@given(instance=becontent_FileToFolderExtension_strategy)
@settings(max_examples=50)
def test_becontent_filetofolderextension_instantiation(instance):
    assert isinstance(instance, becontent_FileToFolderExtension)



@given(instance=becontent_FileToFolderExtension_strategy)
def test_becontent_filetofolderextension_extensionValue_setter(instance):
    original = instance.extensionValue
    instance.extensionValue = original
    assert instance.extensionValue == original



@given(instance=becontent_FileToFolderExtension_strategy)
def test_becontent_filetofolderextension__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_FileToFolderExtension_strategy)
def test_becontent_filetofolderextension_extensionKey_setter(instance):
    original = instance.extensionKey
    instance.extensionKey = original
    assert instance.extensionKey == original

@given(instance=becontent_DefinitionItem_strategy)
@settings(max_examples=50)
def test_becontent_definitionitem_instantiation(instance):
    assert isinstance(instance, becontent_DefinitionItem)

@given(instance=becontent_BeContentElement_strategy)
@settings(max_examples=50)
def test_becontent_becontentelement_instantiation(instance):
    assert isinstance(instance, becontent_BeContentElement)

@given(instance=becontent_BeContentModel_strategy)
@settings(max_examples=50)
def test_becontent_becontentmodel_instantiation(instance):
    assert isinstance(instance, becontent_BeContentModel)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=becontent_SystemRelation_strategy)
@settings(max_examples=50)
def test_becontent_systemrelation_instantiation(instance):
    assert isinstance(instance, becontent_SystemRelation)

@given(instance=becontent_CustomRelation_strategy)
@settings(max_examples=50)
def test_becontent_customrelation_instantiation(instance):
    assert isinstance(instance, becontent_CustomRelation)

@given(instance=becontent_Relation_strategy)
@settings(max_examples=50)
def test_becontent_relation_instantiation(instance):
    assert isinstance(instance, becontent_Relation)



@given(instance=becontent_Relation_strategy)
def test_becontent_relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Relation_strategy)
def test_becontent_relation_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=becontent_SystemEntityField_strategy)
@settings(max_examples=50)
def test_becontent_systementityfield_instantiation(instance):
    assert isinstance(instance, becontent_SystemEntityField)



@given(instance=becontent_SystemEntityField_strategy)
def test_becontent_systementityfield_isTextSearch_setter(instance):
    original = instance.isTextSearch
    instance.isTextSearch = original
    assert instance.isTextSearch == original



@given(instance=becontent_SystemEntityField_strategy)
def test_becontent_systementityfield_isSearchPresentationHead_setter(instance):
    original = instance.isSearchPresentationHead
    instance.isSearchPresentationHead = original
    assert instance.isSearchPresentationHead == original



@given(instance=becontent_SystemEntityField_strategy)
def test_becontent_systementityfield_isSearchPresentationBody_setter(instance):
    original = instance.isSearchPresentationBody
    instance.isSearchPresentationBody = original
    assert instance.isSearchPresentationBody == original



@given(instance=becontent_SystemEntityField_strategy)
def test_becontent_systementityfield_isPresented_setter(instance):
    original = instance.isPresented
    instance.isPresented = original
    assert instance.isPresented == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=becontent_SystemEntity_strategy)
@settings(max_examples=50)
def test_becontent_systementity_instantiation(instance):
    assert isinstance(instance, becontent_SystemEntity)

@given(instance=becontent_CustomEntity_strategy)
@settings(max_examples=50)
def test_becontent_customentity_instantiation(instance):
    assert isinstance(instance, becontent_CustomEntity)

@given(instance=becontent_Handler_strategy)
@settings(max_examples=50)
def test_becontent_handler_instantiation(instance):
    assert isinstance(instance, becontent_Handler)



@given(instance=becontent_Handler_strategy)
def test_becontent_handler_mainSkinPagerLength_setter(instance):
    original = instance.mainSkinPagerLength
    instance.mainSkinPagerLength = original
    assert instance.mainSkinPagerLength == original



@given(instance=becontent_Handler_strategy)
def test_becontent_handler_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=becontent_Handler_strategy)
def test_becontent_handler_mainSkinWithPager_setter(instance):
    original = instance.mainSkinWithPager
    instance.mainSkinWithPager = original
    assert instance.mainSkinWithPager == original



@given(instance=becontent_Handler_strategy)
def test_becontent_handler_mainSkinPlaceholder_setter(instance):
    original = instance.mainSkinPlaceholder
    instance.mainSkinPlaceholder = original
    assert instance.mainSkinPlaceholder == original

@given(instance=becontent_Channel_strategy)
@settings(max_examples=50)
def test_becontent_channel_instantiation(instance):
    assert isinstance(instance, becontent_Channel)



@given(instance=becontent_Channel_strategy)
def test_becontent_channel__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_Channel_strategy)
def test_becontent_channel_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=NotStructuredElement_strategy)
@settings(max_examples=50)
def test_notstructuredelement_instantiation(instance):
    assert isinstance(instance, NotStructuredElement)

@given(instance=becontent_FileToFolder_strategy)
@settings(max_examples=50)
def test_becontent_filetofolder_instantiation(instance):
    assert isinstance(instance, becontent_FileToFolder)



@given(instance=becontent_FileToFolder_strategy)
def test_becontent_filetofolder_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=becontent_FileToFolder_strategy)
def test_becontent_filetofolder_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_FileToFolder_strategy)
def test_becontent_filetofolder_extensionMessage_setter(instance):
    original = instance.extensionMessage
    instance.extensionMessage = original
    assert instance.extensionMessage == original



@given(instance=becontent_FileToFolder_strategy)
def test_becontent_filetofolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_FileToFolder_strategy)
def test_becontent_filetofolder_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_Password_strategy)
@settings(max_examples=50)
def test_becontent_password_instantiation(instance):
    assert isinstance(instance, becontent_Password)



@given(instance=becontent_Password_strategy)
def test_becontent_password_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Password_strategy)
def test_becontent_password_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=becontent_Password_strategy)
def test_becontent_password_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Password_strategy)
def test_becontent_password_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=becontent_Password_strategy)
def test_becontent_password_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_LongDate_strategy)
@settings(max_examples=50)
def test_becontent_longdate_instantiation(instance):
    assert isinstance(instance, becontent_LongDate)



@given(instance=becontent_LongDate_strategy)
def test_becontent_longdate_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_LongDate_strategy)
def test_becontent_longdate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_LongDate_strategy)
def test_becontent_longdate_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent_Editor_strategy)
@settings(max_examples=50)
def test_becontent_editor_instantiation(instance):
    assert isinstance(instance, becontent_Editor)



@given(instance=becontent_Editor_strategy)
def test_becontent_editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Editor_strategy)
def test_becontent_editor_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Editor_strategy)
def test_becontent_editor_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Editor_strategy)
def test_becontent_editor_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original



@given(instance=becontent_Editor_strategy)
def test_becontent_editor_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=becontent_RadioFromReference_strategy)
@settings(max_examples=50)
def test_becontent_radiofromreference_instantiation(instance):
    assert isinstance(instance, becontent_RadioFromReference)



@given(instance=becontent_RadioFromReference_strategy)
def test_becontent_radiofromreference_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_RadioFromReference_strategy)
def test_becontent_radiofromreference_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original



@given(instance=becontent_RadioFromReference_strategy)
def test_becontent_radiofromreference_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_RadioFromReference_strategy)
def test_becontent_radiofromreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_SelectFromReference_strategy)
@settings(max_examples=50)
def test_becontent_selectfromreference_instantiation(instance):
    assert isinstance(instance, becontent_SelectFromReference)



@given(instance=becontent_SelectFromReference_strategy)
def test_becontent_selectfromreference_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original



@given(instance=becontent_SelectFromReference_strategy)
def test_becontent_selectfromreference_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_SelectFromReference_strategy)
def test_becontent_selectfromreference_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_SelectFromReference_strategy)
def test_becontent_selectfromreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_Image_strategy)
@settings(max_examples=50)
def test_becontent_image_instantiation(instance):
    assert isinstance(instance, becontent_Image)



@given(instance=becontent_Image_strategy)
def test_becontent_image_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Image_strategy)
def test_becontent_image_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Image_strategy)
def test_becontent_image_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_File_strategy)
@settings(max_examples=50)
def test_becontent_file_instantiation(instance):
    assert isinstance(instance, becontent_File)



@given(instance=becontent_File_strategy)
def test_becontent_file_extensionMessage_setter(instance):
    original = instance.extensionMessage
    instance.extensionMessage = original
    assert instance.extensionMessage == original



@given(instance=becontent_File_strategy)
def test_becontent_file_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_File_strategy)
def test_becontent_file_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_File_strategy)
def test_becontent_file_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=becontent_File_strategy)
def test_becontent_file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_Textarea_strategy)
@settings(max_examples=50)
def test_becontent_textarea_instantiation(instance):
    assert isinstance(instance, becontent_Textarea)



@given(instance=becontent_Textarea_strategy)
def test_becontent_textarea_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Textarea_strategy)
def test_becontent_textarea_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=becontent_Textarea_strategy)
def test_becontent_textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original



@given(instance=becontent_Textarea_strategy)
def test_becontent_textarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Textarea_strategy)
def test_becontent_textarea_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_HierarchicalPosition_strategy)
@settings(max_examples=50)
def test_becontent_hierarchicalposition_instantiation(instance):
    assert isinstance(instance, becontent_HierarchicalPosition)



@given(instance=becontent_HierarchicalPosition_strategy)
def test_becontent_hierarchicalposition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_HierarchicalPosition_strategy)
def test_becontent_hierarchicalposition_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=becontent_HierarchicalPosition_strategy)
def test_becontent_hierarchicalposition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_HierarchicalPosition_strategy)
def test_becontent_hierarchicalposition_referenceField_setter(instance):
    original = instance.referenceField
    instance.referenceField = original
    assert instance.referenceField == original



@given(instance=becontent_HierarchicalPosition_strategy)
def test_becontent_hierarchicalposition_controlledField_setter(instance):
    original = instance.controlledField
    instance.controlledField = original
    assert instance.controlledField == original

@given(instance=becontent_Hidden_strategy)
@settings(max_examples=50)
def test_becontent_hidden_instantiation(instance):
    assert isinstance(instance, becontent_Hidden)



@given(instance=becontent_Hidden_strategy)
def test_becontent_hidden_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Hidden_strategy)
def test_becontent_hidden_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent_Position_strategy)
@settings(max_examples=50)
def test_becontent_position_instantiation(instance):
    assert isinstance(instance, becontent_Position)



@given(instance=becontent_Position_strategy)
def test_becontent_position_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=becontent_Position_strategy)
def test_becontent_position_controlledField_setter(instance):
    original = instance.controlledField
    instance.controlledField = original
    assert instance.controlledField == original



@given(instance=becontent_Position_strategy)
def test_becontent_position_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Position_strategy)
def test_becontent_position_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Position_strategy)
def test_becontent_position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_Year_strategy)
@settings(max_examples=50)
def test_becontent_year_instantiation(instance):
    assert isinstance(instance, becontent_Year)



@given(instance=becontent_Year_strategy)
def test_becontent_year_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Year_strategy)
def test_becontent_year_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Year_strategy)
def test_becontent_year_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Year_strategy)
def test_becontent_year_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=becontent_Year_strategy)
def test_becontent_year_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=becontent_Date_strategy)
@settings(max_examples=50)
def test_becontent_date_instantiation(instance):
    assert isinstance(instance, becontent_Date)



@given(instance=becontent_Date_strategy)
def test_becontent_date_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Date_strategy)
def test_becontent_date_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Date_strategy)
def test_becontent_date_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_RelationManager_strategy)
@settings(max_examples=50)
def test_becontent_relationmanager_instantiation(instance):
    assert isinstance(instance, becontent_RelationManager)



@given(instance=becontent_RelationManager_strategy)
def test_becontent_relationmanager_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=becontent_RelationManager_strategy)
def test_becontent_relationmanager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_RelationManager_strategy)
def test_becontent_relationmanager_restrictCondition_setter(instance):
    original = instance.restrictCondition
    instance.restrictCondition = original
    assert instance.restrictCondition == original



@given(instance=becontent_RelationManager_strategy)
def test_becontent_relationmanager_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=becontent_Link_strategy)
@settings(max_examples=50)
def test_becontent_link_instantiation(instance):
    assert isinstance(instance, becontent_Link)



@given(instance=becontent_Link_strategy)
def test_becontent_link_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=becontent_Link_strategy)
def test_becontent_link_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Link_strategy)
def test_becontent_link_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=becontent_Link_strategy)
def test_becontent_link_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Link_strategy)
def test_becontent_link_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_Color_strategy)
@settings(max_examples=50)
def test_becontent_color_instantiation(instance):
    assert isinstance(instance, becontent_Color)



@given(instance=becontent_Color_strategy)
def test_becontent_color_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Color_strategy)
def test_becontent_color_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Color_strategy)
def test_becontent_color_defaultColor_setter(instance):
    original = instance.defaultColor
    instance.defaultColor = original
    assert instance.defaultColor == original

@given(instance=becontent_Select_strategy)
@settings(max_examples=50)
def test_becontent_select_instantiation(instance):
    assert isinstance(instance, becontent_Select)



@given(instance=becontent_Select_strategy)
def test_becontent_select_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Select_strategy)
def test_becontent_select_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=becontent_Select_strategy)
def test_becontent_select_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Select_strategy)
def test_becontent_select_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent_Section_strategy)
@settings(max_examples=50)
def test_becontent_section_instantiation(instance):
    assert isinstance(instance, becontent_Section)



@given(instance=becontent_Section_strategy)
def test_becontent_section_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=becontent_Section_strategy)
def test_becontent_section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Form_strategy)
@settings(max_examples=50)
def test_form_instantiation(instance):
    assert isinstance(instance, Form)

@given(instance=becontent_ExtendedForm_strategy)
@settings(max_examples=50)
def test_becontent_extendedform_instantiation(instance):
    assert isinstance(instance, becontent_ExtendedForm)



@given(instance=becontent_ExtendedForm_strategy)
def test_becontent_extendedform_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=becontent_Checkbox_strategy)
@settings(max_examples=50)
def test_becontent_checkbox_instantiation(instance):
    assert isinstance(instance, becontent_Checkbox)



@given(instance=becontent_Checkbox_strategy)
def test_becontent_checkbox_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Checkbox_strategy)
def test_becontent_checkbox_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=becontent_Checkbox_strategy)
def test_becontent_checkbox_isChecked_setter(instance):
    original = instance.isChecked
    instance.isChecked = original
    assert instance.isChecked == original



@given(instance=becontent_Checkbox_strategy)
def test_becontent_checkbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_RadioButton_strategy)
@settings(max_examples=50)
def test_becontent_radiobutton_instantiation(instance):
    assert isinstance(instance, becontent_RadioButton)



@given(instance=becontent_RadioButton_strategy)
def test_becontent_radiobutton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_RadioButton_strategy)
def test_becontent_radiobutton_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_RadioButton_strategy)
def test_becontent_radiobutton_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=becontent_Text_strategy)
@settings(max_examples=50)
def test_becontent_text_instantiation(instance):
    assert isinstance(instance, becontent_Text)



@given(instance=becontent_Text_strategy)
def test_becontent_text_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=becontent_Text_strategy)
def test_becontent_text_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=becontent_Text_strategy)
def test_becontent_text_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=becontent_Text_strategy)
def test_becontent_text_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Text_strategy)
def test_becontent_text_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=becontent_Validation_strategy)
@settings(max_examples=50)
def test_becontent_validation_instantiation(instance):
    assert isinstance(instance, becontent_Validation)



@given(instance=becontent_Validation_strategy)
def test_becontent_validation_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original



@given(instance=becontent_Validation_strategy)
def test_becontent_validation__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_Validation_strategy)
def test_becontent_validation_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=becontent_CustomPager_strategy)
@settings(max_examples=50)
def test_becontent_custompager_instantiation(instance):
    assert isinstance(instance, becontent_CustomPager)



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=becontent_CustomPager_strategy)
def test_becontent_custompager_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=becontent_EntityManagerPage_strategy)
@settings(max_examples=50)
def test_becontent_entitymanagerpage_instantiation(instance):
    assert isinstance(instance, becontent_EntityManagerPage)



@given(instance=becontent_EntityManagerPage_strategy)
def test_becontent_entitymanagerpage_skin_setter(instance):
    original = instance.skin
    instance.skin = original
    assert instance.skin == original



@given(instance=becontent_EntityManagerPage_strategy)
def test_becontent_entitymanagerpage_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=ApplyCommand_strategy)
@settings(max_examples=50)
def test_applycommand_instantiation(instance):
    assert isinstance(instance, ApplyCommand)

@given(instance=becontent_ApplyItem_strategy)
@settings(max_examples=50)
def test_becontent_applyitem_instantiation(instance):
    assert isinstance(instance, becontent_ApplyItem)



@given(instance=becontent_ApplyItem_strategy)
def test_becontent_applyitem_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=becontent_ApplyItem_strategy)
def test_becontent_applyitem_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=becontent_ApplyIndexed_strategy)
@settings(max_examples=50)
def test_becontent_applyindexed_instantiation(instance):
    assert isinstance(instance, becontent_ApplyIndexed)

@given(instance=becontent_Apply_strategy)
@settings(max_examples=50)
def test_becontent_apply_instantiation(instance):
    assert isinstance(instance, becontent_Apply)



@given(instance=becontent_Apply_strategy)
def test_becontent_apply_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=FormElement_strategy)
@settings(max_examples=50)
def test_formelement_instantiation(instance):
    assert isinstance(instance, FormElement)

@given(instance=becontent_Form_strategy)
@settings(max_examples=50)
def test_becontent_form_instantiation(instance):
    assert isinstance(instance, becontent_Form)



@given(instance=becontent_Form_strategy)
def test_becontent_form_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=becontent_Form_strategy)
def test_becontent_form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Form_strategy)
def test_becontent_form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=becontent_NotStructuredElement_strategy)
@settings(max_examples=50)
def test_becontent_notstructuredelement_instantiation(instance):
    assert isinstance(instance, becontent_NotStructuredElement)



@given(instance=becontent_NotStructuredElement_strategy)
def test_becontent_notstructuredelement_helper_setter(instance):
    original = instance.helper
    instance.helper = original
    assert instance.helper == original

@given(instance=becontent_FormElement_strategy)
@settings(max_examples=50)
def test_becontent_formelement_instantiation(instance):
    assert isinstance(instance, becontent_FormElement)

@given(instance=becontent_ConditionalTemplate_strategy)
@settings(max_examples=50)
def test_becontent_conditionaltemplate_instantiation(instance):
    assert isinstance(instance, becontent_ConditionalTemplate)



@given(instance=becontent_ConditionalTemplate_strategy)
def test_becontent_conditionaltemplate_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=becontent_ConditionalTemplate_strategy)
def test_becontent_conditionaltemplate__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_ConditionalTemplate_strategy)
def test_becontent_conditionaltemplate_trueTemplate_setter(instance):
    original = instance.trueTemplate
    instance.trueTemplate = original
    assert instance.trueTemplate == original



@given(instance=becontent_ConditionalTemplate_strategy)
def test_becontent_conditionaltemplate_conditionExp_setter(instance):
    original = instance.conditionExp
    instance.conditionExp = original
    assert instance.conditionExp == original



@given(instance=becontent_ConditionalTemplate_strategy)
def test_becontent_conditionaltemplate_falseTemplate_setter(instance):
    original = instance.falseTemplate
    instance.falseTemplate = original
    assert instance.falseTemplate == original

@given(instance=becontent_ContentCommand_strategy)
@settings(max_examples=50)
def test_becontent_contentcommand_instantiation(instance):
    assert isinstance(instance, becontent_ContentCommand)



@given(instance=becontent_ContentCommand_strategy)
def test_becontent_contentcommand__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent_JoinEntity_strategy)
@settings(max_examples=50)
def test_becontent_joinentity_instantiation(instance):
    assert isinstance(instance, becontent_JoinEntity)



@given(instance=becontent_JoinEntity_strategy)
def test_becontent_joinentity__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=ContentCommand_strategy)
@settings(max_examples=50)
def test_contentcommand_instantiation(instance):
    assert isinstance(instance, ContentCommand)

@given(instance=becontent_UnsetParameter_strategy)
@settings(max_examples=50)
def test_becontent_unsetparameter_instantiation(instance):
    assert isinstance(instance, becontent_UnsetParameter)



@given(instance=becontent_UnsetParameter_strategy)
def test_becontent_unsetparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=becontent_ApplyCommand_strategy)
@settings(max_examples=50)
def test_becontent_applycommand_instantiation(instance):
    assert isinstance(instance, becontent_ApplyCommand)

@given(instance=becontent_Copy_strategy)
@settings(max_examples=50)
def test_becontent_copy_instantiation(instance):
    assert isinstance(instance, becontent_Copy)



@given(instance=becontent_Copy_strategy)
def test_becontent_copy_fieldName1_setter(instance):
    original = instance.fieldName1
    instance.fieldName1 = original
    assert instance.fieldName1 == original



@given(instance=becontent_Copy_strategy)
def test_becontent_copy_fieldName2_setter(instance):
    original = instance.fieldName2
    instance.fieldName2 = original
    assert instance.fieldName2 == original

@given(instance=becontent_Trigger_strategy)
@settings(max_examples=50)
def test_becontent_trigger_instantiation(instance):
    assert isinstance(instance, becontent_Trigger)



@given(instance=becontent_Trigger_strategy)
def test_becontent_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=becontent_Trigger_strategy)
def test_becontent_trigger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=becontent_Propagate_strategy)
@settings(max_examples=50)
def test_becontent_propagate_instantiation(instance):
    assert isinstance(instance, becontent_Propagate)



@given(instance=becontent_Propagate_strategy)
def test_becontent_propagate_fieldName1_setter(instance):
    original = instance.fieldName1
    instance.fieldName1 = original
    assert instance.fieldName1 == original



@given(instance=becontent_Propagate_strategy)
def test_becontent_propagate_fieldName2_setter(instance):
    original = instance.fieldName2
    instance.fieldName2 = original
    assert instance.fieldName2 == original

@given(instance=becontent_Parameter_strategy)
@settings(max_examples=50)
def test_becontent_parameter_instantiation(instance):
    assert isinstance(instance, becontent_Parameter)



@given(instance=becontent_Parameter_strategy)
def test_becontent_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=becontent_Parameter_strategy)
def test_becontent_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ViewItem_strategy)
@settings(max_examples=50)
def test_viewitem_instantiation(instance):
    assert isinstance(instance, ViewItem)

@given(instance=becontent_Skinlet_strategy)
@settings(max_examples=50)
def test_becontent_skinlet_instantiation(instance):
    assert isinstance(instance, becontent_Skinlet)



@given(instance=becontent_Skinlet_strategy)
def test_becontent_skinlet_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=becontent_Skinlet_strategy)
def test_becontent_skinlet__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent_Content_strategy)
@settings(max_examples=50)
def test_becontent_content_instantiation(instance):
    assert isinstance(instance, becontent_Content)



@given(instance=becontent_Content_strategy)
def test_becontent_content_orderFields_setter(instance):
    original = instance.orderFields
    instance.orderFields = original
    assert instance.orderFields == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=becontent_Content_strategy)
def test_becontent_content__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_joinCondition_setter(instance):
    original = instance.joinCondition
    instance.joinCondition = original
    assert instance.joinCondition == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_presentationFields_setter(instance):
    original = instance.presentationFields
    instance.presentationFields = original
    assert instance.presentationFields == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original



@given(instance=becontent_Content_strategy)
def test_becontent_content_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=becontent_Template_strategy)
@settings(max_examples=50)
def test_becontent_template_instantiation(instance):
    assert isinstance(instance, becontent_Template)



@given(instance=becontent_Template_strategy)
def test_becontent_template_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=becontent_Template_strategy)
def test_becontent_template__id_model_setter(instance):
    original = instance._id_model
    instance._id_model = original
    assert instance._id_model == original

@given(instance=becontent_Skin_strategy)
@settings(max_examples=50)
def test_becontent_skin_instantiation(instance):
    assert isinstance(instance, becontent_Skin)



@given(instance=becontent_Skin_strategy)
def test_becontent_skin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
