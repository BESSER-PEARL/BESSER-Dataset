import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UsingMappers,
    domain_DeploymentStarStep,
    domain_DeploymentComponent,
    domain_DeploymentComponents,
    domain_ConfigExtension,
    domain_DeploymentSequence,
    domain_Infrastructure,
    domain_Configuration,
    domain_Recipe,
    domain_UsingMappers,
    TypeMapper,
    domain_JavaScriptMapper,
    domain_JavaMapper,
    Mapper,
    domain_CSSMapper,
    domain_RoleMapper,
    domain_Mapper,
    domain_StyleLibrary,
    domain_Group,
    domain_StyleSet,
    domain_Translation,
    domain_Message,
    domain_LanguageRef,
    Categorized,
    domain_Language,
    domain_MessageLibrary,
    TypePointer,
    domain_TypeMapper,
    domain_MethodPointer,
    domain_Mappers,
    domain_ApplicationMapper,
    domain_Recipes,
    domain_ApplicationRecipe,
    domain_UIPackage,
    domain_ApplicationUIPackage,
    domain_Styles,
    domain_Roles,
    domain_Messages,
    domain_ApplicationMessages,
    domain_ApplicationRole,
    domain_ApplicationInfrastructureLayer,
    domain_StylesPackage,
    domain_Option,
    domain_QueryParameter,
    domain_Specifier,
    domain_ModelQuery,
    domain_ConfigHash,
    domain_ConfigVariable,
    domain_Artifact,
    DomainArtifact,
    domain_JPAService,
    domain_EJBService,
    domain_ContinuousIintegration,
    domain_ORMEntity,
    domain_Artifacts,
    domain_Application,
    domain_DomainArtifact,
    HTMLLayerHolder,
    domain_Component,
    domain_ApplicationStyle,
    domain_ApplicationMappers,
    domain_Ingredient,
    domain_ApplicationRecipes,
    domain_ApplicationUILayer,
    domain_Role,
    domain_DomainApplication,
    domain_GrantAccess,
    domain_Secured,
    domain_GenerationHint,
    domain_Classifier,
    domain_Categorized,
    domain_HTMLLayerHolder,
    domain_EObject,
    domain_DomainApplications,
    domain_DomainTypes,
    domain_DomainArtifacts,
    domain_Domain,
    domain_TypesRepository,
    MenuExtensionRef,
    MenuElement,
    domain_MenuExtensionPoint,
    domain_MenuSeparator,
    domain_MenuExtensionRef,
    domain_MenuHolder,
    domain_InfrastructureComponent,
    domain_InfrastructureLayer,
    domain_Subsystem,
    InfrastructureComponent,
    domain_ServerClaster,
    domain_Storage,
    domain_Router,
    domain_Hub,
    domain_Server,
    domain_EnterpriseInfrastructure,
    domain_InfrastructureConnection,
    domain_Datacenter,
    domain_OrderBy,
    domain_Orders,
    domain_ArtificialField,
    domain_FormVariable,
    ProxiesList,
    domain_ProxiesList,
    MethodPointer,
    domain_Dependency,
    domain_Root,
    ItemIcon,
    domain_SubMenu,
    domain_Relation,
    OptionSelection,
    domain_DropDownSelection,
    Formatable,
    ChildrenHolder,
    SourcesPointer,
    domain_DataControl,
    Uielement,
    domain_Menu,
    domain_SourcesPointer,
    domain_Formatable,
    domain_ItemIcon,
    domain_AreaRef,
    MenuHolder,
    EnabledUIItem,
    domain_EnabledUIItem,
    Context,
    domain_FlexField,
    domain_FlexFields,
    domain_NickNamed,
    InputElement,
    domain_Image,
    domain_Password,
    domain_OutputText,
    domain_Date,
    domain_InputText,
    domain_CheckBox,
    domain_OptionSelection,
    domain_StyleElement,
    ContextParameters,
    domain_Trigger,
    ContextValue,
    domain_StyleClass,
    domain_ContextParameters,
    domain_ExpressionPart,
    domain_ContextValue,
    domain_ContextParameter,
    domain_ChildrenHolder,
    domain_InputElement,
    domain_LinkToMessage,
    domain_LinkToLabel,
    domain_LayerHolder,
    domain_Controls,
    Trigger,
    domain_UpdateTrigger,
    domain_PREFormTrigger,
    domain_InsertTrigger,
    domain_POSTQueryTrigger,
    domain_PREInsertTrigger,
    domain_PREQueryTrigger,
    domain_DeleteTrigger,
    domain_CreateTrigger,
    domain_POSTCreateTrigger,
    domain_SearchTrigger,
    domain_PREUpdateTrigger,
    domain_PREDeleteTrigger,
    domain_CanvasView,
    domain_ViewPortTrigger,
    ViewElement,
    Orderable,
    domain_ViewPort,
    domain_ViewArea,
    domain_MenuView,
    FlexFields,
    domain_MenuItem,
    MultiLangLabel,
    domain_Tree,
    domain_MessageElement,
    domain_Table,
    domain_Button,
    domain_Label,
    DefaultCavas,
    ViewPortHolder,
    CanvasFrame,
    domain_Canvas,
    domain_TabPage,
    domain_TabCanvas,
    domain_PopupCanvas,
    NickNamed,
    domain_DefaultCavas,
    domain_ViewPortHolder,
    StyleElement,
    domain_Uielement,
    domain_Selection,
    domain_Column,
    domain_MenuFolder,
    domain_ViewElement,
    domain_MenuElement,
    domain_Context,
    domain_MultiLangLabel,
    domain_Orderable,
    domain_MenuDefinition,
    domain_TabPagesInheritance,
    domain_ViewInheritance,
    domain_CanvasFrame,
    domain_Views,
    domain_FormParameter,
    domain_FormDataControls,
    domain_FormView,
    domain_Form,
    domain_Types,
    domain_EnumAttribute,
    domain_ReturnValue,
    domain_Parameter,
    Secured,
    domain_Window,
    domain_Operation,
    TypeElement,
    domain_Type,
    domain_TypeReference,
    domain_Enumarator,
    domain_Primitive,
    domain_Attribute,
    domain_Link,
    RelationShip,
    domain_Generalization,
    domain_Assosiation,
    domain_References,
    domain_RelationShip,
    domain_TypeElement,
    domain_Package,
    domain_TypePointer,
    domain_ArtifactRef,
    domain_QueryVariable,
    domain_KeyValuePair,
    domain_TypeDefinition,
    domain_Query,
    domain_MappingSpecifier,
    ArtifactRef,
    domain_ModelMapper,
    domain_HashProperty,
    domain_Property,
    Component,
    domain_JavaComponent,
    PlatformLayers,
    Order,
    RelationType,
    Comparator,
    Orientation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usingmappers_is_not_abstract():
    assert not inspect.isabstract(UsingMappers)


def test_usingmappers_constructor_exists():
    assert callable(UsingMappers.__init__)


def test_usingmappers_constructor_args():
    sig = inspect.signature(UsingMappers.__init__)
    params = list(sig.parameters.keys())



def test_domain_deploymentstarstep_is_not_abstract():
    assert not inspect.isabstract(domain_DeploymentStarStep)


def test_domain_deploymentstarstep_constructor_exists():
    assert callable(domain_DeploymentStarStep.__init__)


def test_domain_deploymentstarstep_constructor_args():
    sig = inspect.signature(domain_DeploymentStarStep.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_deploymentstarstep_has_uid():
    assert hasattr(domain_DeploymentStarStep, "uid")
    descriptor = None
    for klass in domain_DeploymentStarStep.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_deploymentstarstep_has_name():
    assert hasattr(domain_DeploymentStarStep, "name")
    descriptor = None
    for klass in domain_DeploymentStarStep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_deploymentcomponent_is_not_abstract():
    assert not inspect.isabstract(domain_DeploymentComponent)


def test_domain_deploymentcomponent_constructor_exists():
    assert callable(domain_DeploymentComponent.__init__)


def test_domain_deploymentcomponent_constructor_args():
    sig = inspect.signature(domain_DeploymentComponent.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_deploymentcomponent_has_uid():
    assert hasattr(domain_DeploymentComponent, "uid")
    descriptor = None
    for klass in domain_DeploymentComponent.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_deploymentcomponent_has_name():
    assert hasattr(domain_DeploymentComponent, "name")
    descriptor = None
    for klass in domain_DeploymentComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_deploymentcomponents_is_not_abstract():
    assert not inspect.isabstract(domain_DeploymentComponents)


def test_domain_deploymentcomponents_constructor_exists():
    assert callable(domain_DeploymentComponents.__init__)


def test_domain_deploymentcomponents_constructor_args():
    sig = inspect.signature(domain_DeploymentComponents.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_deploymentcomponents_has_uid():
    assert hasattr(domain_DeploymentComponents, "uid")
    descriptor = None
    for klass in domain_DeploymentComponents.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_configextension_is_not_abstract():
    assert not inspect.isabstract(domain_ConfigExtension)


def test_domain_configextension_constructor_exists():
    assert callable(domain_ConfigExtension.__init__)


def test_domain_configextension_constructor_args():
    sig = inspect.signature(domain_ConfigExtension.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_configextension_has_uid():
    assert hasattr(domain_ConfigExtension, "uid")
    descriptor = None
    for klass in domain_ConfigExtension.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_deploymentsequence_is_not_abstract():
    assert not inspect.isabstract(domain_DeploymentSequence)


def test_domain_deploymentsequence_constructor_exists():
    assert callable(domain_DeploymentSequence.__init__)


def test_domain_deploymentsequence_constructor_args():
    sig = inspect.signature(domain_DeploymentSequence.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_deploymentsequence_has_uid():
    assert hasattr(domain_DeploymentSequence, "uid")
    descriptor = None
    for klass in domain_DeploymentSequence.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_deploymentsequence_has_name():
    assert hasattr(domain_DeploymentSequence, "name")
    descriptor = None
    for klass in domain_DeploymentSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_infrastructure_is_not_abstract():
    assert not inspect.isabstract(domain_Infrastructure)


def test_domain_infrastructure_constructor_exists():
    assert callable(domain_Infrastructure.__init__)


def test_domain_infrastructure_constructor_args():
    sig = inspect.signature(domain_Infrastructure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_infrastructure_has_name():
    assert hasattr(domain_Infrastructure, "name")
    descriptor = None
    for klass in domain_Infrastructure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_infrastructure_has_uid():
    assert hasattr(domain_Infrastructure, "uid")
    descriptor = None
    for klass in domain_Infrastructure.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_configuration_is_not_abstract():
    assert not inspect.isabstract(domain_Configuration)


def test_domain_configuration_constructor_exists():
    assert callable(domain_Configuration.__init__)


def test_domain_configuration_constructor_args():
    sig = inspect.signature(domain_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_configuration_has_name():
    assert hasattr(domain_Configuration, "name")
    descriptor = None
    for klass in domain_Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_configuration_has_uid():
    assert hasattr(domain_Configuration, "uid")
    descriptor = None
    for klass in domain_Configuration.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_recipe_is_not_abstract():
    assert not inspect.isabstract(domain_Recipe)


def test_domain_recipe_constructor_exists():
    assert callable(domain_Recipe.__init__)


def test_domain_recipe_constructor_args():
    sig = inspect.signature(domain_Recipe.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_recipe_has_uid():
    assert hasattr(domain_Recipe, "uid")
    descriptor = None
    for klass in domain_Recipe.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_recipe_has_name():
    assert hasattr(domain_Recipe, "name")
    descriptor = None
    for klass in domain_Recipe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_usingmappers_is_not_abstract():
    assert not inspect.isabstract(domain_UsingMappers)


def test_domain_usingmappers_constructor_exists():
    assert callable(domain_UsingMappers.__init__)


def test_domain_usingmappers_constructor_args():
    sig = inspect.signature(domain_UsingMappers.__init__)
    params = list(sig.parameters.keys())



def test_typemapper_is_not_abstract():
    assert not inspect.isabstract(TypeMapper)


def test_typemapper_constructor_exists():
    assert callable(TypeMapper.__init__)


def test_typemapper_constructor_args():
    sig = inspect.signature(TypeMapper.__init__)
    params = list(sig.parameters.keys())



def test_domain_javascriptmapper_is_not_abstract():
    assert not inspect.isabstract(domain_JavaScriptMapper)


def test_domain_javascriptmapper_constructor_exists():
    assert callable(domain_JavaScriptMapper.__init__)


def test_domain_javascriptmapper_constructor_args():
    sig = inspect.signature(domain_JavaScriptMapper.__init__)
    params = list(sig.parameters.keys())
    assert "libraryUrl" in params, "Missing parameter 'libraryUrl'"

def test_domain_javascriptmapper_has_libraryUrl():
    assert hasattr(domain_JavaScriptMapper, "libraryUrl")
    descriptor = None
    for klass in domain_JavaScriptMapper.__mro__:
        if "libraryUrl" in klass.__dict__:
            descriptor = klass.__dict__["libraryUrl"]
            break
    assert isinstance(descriptor, property)



def test_domain_javamapper_is_not_abstract():
    assert not inspect.isabstract(domain_JavaMapper)


def test_domain_javamapper_constructor_exists():
    assert callable(domain_JavaMapper.__init__)


def test_domain_javamapper_constructor_args():
    sig = inspect.signature(domain_JavaMapper.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "artifactType" in params, "Missing parameter 'artifactType'"
    assert "mappedToClassName" in params, "Missing parameter 'mappedToClassName'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "mappedToPackageName" in params, "Missing parameter 'mappedToPackageName'"

def test_domain_javamapper_has_version():
    assert hasattr(domain_JavaMapper, "version")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_artifactType():
    assert hasattr(domain_JavaMapper, "artifactType")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "artifactType" in klass.__dict__:
            descriptor = klass.__dict__["artifactType"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_mappedToClassName():
    assert hasattr(domain_JavaMapper, "mappedToClassName")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "mappedToClassName" in klass.__dict__:
            descriptor = klass.__dict__["mappedToClassName"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_groupId():
    assert hasattr(domain_JavaMapper, "groupId")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_libraryName():
    assert hasattr(domain_JavaMapper, "libraryName")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_artifactId():
    assert hasattr(domain_JavaMapper, "artifactId")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_domain_javamapper_has_mappedToPackageName():
    assert hasattr(domain_JavaMapper, "mappedToPackageName")
    descriptor = None
    for klass in domain_JavaMapper.__mro__:
        if "mappedToPackageName" in klass.__dict__:
            descriptor = klass.__dict__["mappedToPackageName"]
            break
    assert isinstance(descriptor, property)



def test_mapper_is_not_abstract():
    assert not inspect.isabstract(Mapper)


def test_mapper_constructor_exists():
    assert callable(Mapper.__init__)


def test_mapper_constructor_args():
    sig = inspect.signature(Mapper.__init__)
    params = list(sig.parameters.keys())



def test_domain_cssmapper_is_not_abstract():
    assert not inspect.isabstract(domain_CSSMapper)


def test_domain_cssmapper_constructor_exists():
    assert callable(domain_CSSMapper.__init__)


def test_domain_cssmapper_constructor_args():
    sig = inspect.signature(domain_CSSMapper.__init__)
    params = list(sig.parameters.keys())
    assert "libraryUrl" in params, "Missing parameter 'libraryUrl'"
    assert "fakeTypeName" in params, "Missing parameter 'fakeTypeName'"
    assert "fakePackageName" in params, "Missing parameter 'fakePackageName'"

def test_domain_cssmapper_has_libraryUrl():
    assert hasattr(domain_CSSMapper, "libraryUrl")
    descriptor = None
    for klass in domain_CSSMapper.__mro__:
        if "libraryUrl" in klass.__dict__:
            descriptor = klass.__dict__["libraryUrl"]
            break
    assert isinstance(descriptor, property)

def test_domain_cssmapper_has_fakeTypeName():
    assert hasattr(domain_CSSMapper, "fakeTypeName")
    descriptor = None
    for klass in domain_CSSMapper.__mro__:
        if "fakeTypeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeTypeName"]
            break
    assert isinstance(descriptor, property)

def test_domain_cssmapper_has_fakePackageName():
    assert hasattr(domain_CSSMapper, "fakePackageName")
    descriptor = None
    for klass in domain_CSSMapper.__mro__:
        if "fakePackageName" in klass.__dict__:
            descriptor = klass.__dict__["fakePackageName"]
            break
    assert isinstance(descriptor, property)



def test_domain_rolemapper_is_not_abstract():
    assert not inspect.isabstract(domain_RoleMapper)


def test_domain_rolemapper_constructor_exists():
    assert callable(domain_RoleMapper.__init__)


def test_domain_rolemapper_constructor_args():
    sig = inspect.signature(domain_RoleMapper.__init__)
    params = list(sig.parameters.keys())
    assert "globalRoleName" in params, "Missing parameter 'globalRoleName'"
    assert "localRoleName" in params, "Missing parameter 'localRoleName'"
    assert "fakeRoleName" in params, "Missing parameter 'fakeRoleName'"

def test_domain_rolemapper_has_globalRoleName():
    assert hasattr(domain_RoleMapper, "globalRoleName")
    descriptor = None
    for klass in domain_RoleMapper.__mro__:
        if "globalRoleName" in klass.__dict__:
            descriptor = klass.__dict__["globalRoleName"]
            break
    assert isinstance(descriptor, property)

def test_domain_rolemapper_has_localRoleName():
    assert hasattr(domain_RoleMapper, "localRoleName")
    descriptor = None
    for klass in domain_RoleMapper.__mro__:
        if "localRoleName" in klass.__dict__:
            descriptor = klass.__dict__["localRoleName"]
            break
    assert isinstance(descriptor, property)

def test_domain_rolemapper_has_fakeRoleName():
    assert hasattr(domain_RoleMapper, "fakeRoleName")
    descriptor = None
    for klass in domain_RoleMapper.__mro__:
        if "fakeRoleName" in klass.__dict__:
            descriptor = klass.__dict__["fakeRoleName"]
            break
    assert isinstance(descriptor, property)



def test_domain_mapper_is_not_abstract():
    assert not inspect.isabstract(domain_Mapper)


def test_domain_mapper_constructor_exists():
    assert callable(domain_Mapper.__init__)


def test_domain_mapper_constructor_args():
    sig = inspect.signature(domain_Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "uiLayer" in params, "Missing parameter 'uiLayer'"
    assert "serviceLayer" in params, "Missing parameter 'serviceLayer'"

def test_domain_mapper_has_uid():
    assert hasattr(domain_Mapper, "uid")
    descriptor = None
    for klass in domain_Mapper.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_mapper_has_uiLayer():
    assert hasattr(domain_Mapper, "uiLayer")
    descriptor = None
    for klass in domain_Mapper.__mro__:
        if "uiLayer" in klass.__dict__:
            descriptor = klass.__dict__["uiLayer"]
            break
    assert isinstance(descriptor, property)

def test_domain_mapper_has_serviceLayer():
    assert hasattr(domain_Mapper, "serviceLayer")
    descriptor = None
    for klass in domain_Mapper.__mro__:
        if "serviceLayer" in klass.__dict__:
            descriptor = klass.__dict__["serviceLayer"]
            break
    assert isinstance(descriptor, property)



def test_domain_stylelibrary_is_not_abstract():
    assert not inspect.isabstract(domain_StyleLibrary)


def test_domain_stylelibrary_constructor_exists():
    assert callable(domain_StyleLibrary.__init__)


def test_domain_stylelibrary_constructor_args():
    sig = inspect.signature(domain_StyleLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_stylelibrary_has_uid():
    assert hasattr(domain_StyleLibrary, "uid")
    descriptor = None
    for klass in domain_StyleLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_stylelibrary_has_name():
    assert hasattr(domain_StyleLibrary, "name")
    descriptor = None
    for klass in domain_StyleLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_group_is_not_abstract():
    assert not inspect.isabstract(domain_Group)


def test_domain_group_constructor_exists():
    assert callable(domain_Group.__init__)


def test_domain_group_constructor_args():
    sig = inspect.signature(domain_Group.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_group_has_uid():
    assert hasattr(domain_Group, "uid")
    descriptor = None
    for klass in domain_Group.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_group_has_name():
    assert hasattr(domain_Group, "name")
    descriptor = None
    for klass in domain_Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_styleset_is_not_abstract():
    assert not inspect.isabstract(domain_StyleSet)


def test_domain_styleset_constructor_exists():
    assert callable(domain_StyleSet.__init__)


def test_domain_styleset_constructor_args():
    sig = inspect.signature(domain_StyleSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_styleset_has_name():
    assert hasattr(domain_StyleSet, "name")
    descriptor = None
    for klass in domain_StyleSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_styleset_has_uid():
    assert hasattr(domain_StyleSet, "uid")
    descriptor = None
    for klass in domain_StyleSet.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_translation_is_not_abstract():
    assert not inspect.isabstract(domain_Translation)


def test_domain_translation_constructor_exists():
    assert callable(domain_Translation.__init__)


def test_domain_translation_constructor_args():
    sig = inspect.signature(domain_Translation.__init__)
    params = list(sig.parameters.keys())
    assert "translation" in params, "Missing parameter 'translation'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_translation_has_translation():
    assert hasattr(domain_Translation, "translation")
    descriptor = None
    for klass in domain_Translation.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)

def test_domain_translation_has_uid():
    assert hasattr(domain_Translation, "uid")
    descriptor = None
    for klass in domain_Translation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_message_is_not_abstract():
    assert not inspect.isabstract(domain_Message)


def test_domain_message_constructor_exists():
    assert callable(domain_Message.__init__)


def test_domain_message_constructor_args():
    sig = inspect.signature(domain_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_message_has_name():
    assert hasattr(domain_Message, "name")
    descriptor = None
    for klass in domain_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_message_has_uid():
    assert hasattr(domain_Message, "uid")
    descriptor = None
    for klass in domain_Message.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_languageref_is_not_abstract():
    assert not inspect.isabstract(domain_LanguageRef)


def test_domain_languageref_constructor_exists():
    assert callable(domain_LanguageRef.__init__)


def test_domain_languageref_constructor_args():
    sig = inspect.signature(domain_LanguageRef.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_languageref_has_uid():
    assert hasattr(domain_LanguageRef, "uid")
    descriptor = None
    for klass in domain_LanguageRef.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_categorized_is_not_abstract():
    assert not inspect.isabstract(Categorized)


def test_categorized_constructor_exists():
    assert callable(Categorized.__init__)


def test_categorized_constructor_args():
    sig = inspect.signature(Categorized.__init__)
    params = list(sig.parameters.keys())



def test_domain_language_is_not_abstract():
    assert not inspect.isabstract(domain_Language)


def test_domain_language_constructor_exists():
    assert callable(domain_Language.__init__)


def test_domain_language_constructor_args():
    sig = inspect.signature(domain_Language.__init__)
    params = list(sig.parameters.keys())
    assert "defaultLang" in params, "Missing parameter 'defaultLang'"
    assert "code" in params, "Missing parameter 'code'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "lang" in params, "Missing parameter 'lang'"

def test_domain_language_has_defaultLang():
    assert hasattr(domain_Language, "defaultLang")
    descriptor = None
    for klass in domain_Language.__mro__:
        if "defaultLang" in klass.__dict__:
            descriptor = klass.__dict__["defaultLang"]
            break
    assert isinstance(descriptor, property)

def test_domain_language_has_code():
    assert hasattr(domain_Language, "code")
    descriptor = None
    for klass in domain_Language.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_domain_language_has_uid():
    assert hasattr(domain_Language, "uid")
    descriptor = None
    for klass in domain_Language.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_language_has_lang():
    assert hasattr(domain_Language, "lang")
    descriptor = None
    for klass in domain_Language.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_domain_messagelibrary_is_not_abstract():
    assert not inspect.isabstract(domain_MessageLibrary)


def test_domain_messagelibrary_constructor_exists():
    assert callable(domain_MessageLibrary.__init__)


def test_domain_messagelibrary_constructor_args():
    sig = inspect.signature(domain_MessageLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_messagelibrary_has_name():
    assert hasattr(domain_MessageLibrary, "name")
    descriptor = None
    for klass in domain_MessageLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_messagelibrary_has_uid():
    assert hasattr(domain_MessageLibrary, "uid")
    descriptor = None
    for klass in domain_MessageLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_typepointer_is_not_abstract():
    assert not inspect.isabstract(TypePointer)


def test_typepointer_constructor_exists():
    assert callable(TypePointer.__init__)


def test_typepointer_constructor_args():
    sig = inspect.signature(TypePointer.__init__)
    params = list(sig.parameters.keys())



def test_domain_typemapper_is_not_abstract():
    assert not inspect.isabstract(domain_TypeMapper)


def test_domain_typemapper_constructor_exists():
    assert callable(domain_TypeMapper.__init__)


def test_domain_typemapper_constructor_args():
    sig = inspect.signature(domain_TypeMapper.__init__)
    params = list(sig.parameters.keys())



def test_domain_methodpointer_is_not_abstract():
    assert not inspect.isabstract(domain_MethodPointer)


def test_domain_methodpointer_constructor_exists():
    assert callable(domain_MethodPointer.__init__)


def test_domain_methodpointer_constructor_args():
    sig = inspect.signature(domain_MethodPointer.__init__)
    params = list(sig.parameters.keys())
    assert "fakeMethod" in params, "Missing parameter 'fakeMethod'"

def test_domain_methodpointer_has_fakeMethod():
    assert hasattr(domain_MethodPointer, "fakeMethod")
    descriptor = None
    for klass in domain_MethodPointer.__mro__:
        if "fakeMethod" in klass.__dict__:
            descriptor = klass.__dict__["fakeMethod"]
            break
    assert isinstance(descriptor, property)



def test_domain_mappers_is_not_abstract():
    assert not inspect.isabstract(domain_Mappers)


def test_domain_mappers_constructor_exists():
    assert callable(domain_Mappers.__init__)


def test_domain_mappers_constructor_args():
    sig = inspect.signature(domain_Mappers.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_mappers_has_uid():
    assert hasattr(domain_Mappers, "uid")
    descriptor = None
    for klass in domain_Mappers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationmapper_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationMapper)


def test_domain_applicationmapper_constructor_exists():
    assert callable(domain_ApplicationMapper.__init__)


def test_domain_applicationmapper_constructor_args():
    sig = inspect.signature(domain_ApplicationMapper.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationmapper_has_name():
    assert hasattr(domain_ApplicationMapper, "name")
    descriptor = None
    for klass in domain_ApplicationMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationmapper_has_uid():
    assert hasattr(domain_ApplicationMapper, "uid")
    descriptor = None
    for klass in domain_ApplicationMapper.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_recipes_is_not_abstract():
    assert not inspect.isabstract(domain_Recipes)


def test_domain_recipes_constructor_exists():
    assert callable(domain_Recipes.__init__)


def test_domain_recipes_constructor_args():
    sig = inspect.signature(domain_Recipes.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_recipes_has_uid():
    assert hasattr(domain_Recipes, "uid")
    descriptor = None
    for klass in domain_Recipes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationrecipe_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationRecipe)


def test_domain_applicationrecipe_constructor_exists():
    assert callable(domain_ApplicationRecipe.__init__)


def test_domain_applicationrecipe_constructor_args():
    sig = inspect.signature(domain_ApplicationRecipe.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationrecipe_has_name():
    assert hasattr(domain_ApplicationRecipe, "name")
    descriptor = None
    for klass in domain_ApplicationRecipe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationrecipe_has_uid():
    assert hasattr(domain_ApplicationRecipe, "uid")
    descriptor = None
    for klass in domain_ApplicationRecipe.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_uipackage_is_not_abstract():
    assert not inspect.isabstract(domain_UIPackage)


def test_domain_uipackage_constructor_exists():
    assert callable(domain_UIPackage.__init__)


def test_domain_uipackage_constructor_args():
    sig = inspect.signature(domain_UIPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_uipackage_has_uid():
    assert hasattr(domain_UIPackage, "uid")
    descriptor = None
    for klass in domain_UIPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationuipackage_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationUIPackage)


def test_domain_applicationuipackage_constructor_exists():
    assert callable(domain_ApplicationUIPackage.__init__)


def test_domain_applicationuipackage_constructor_args():
    sig = inspect.signature(domain_ApplicationUIPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationuipackage_has_name():
    assert hasattr(domain_ApplicationUIPackage, "name")
    descriptor = None
    for klass in domain_ApplicationUIPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationuipackage_has_uid():
    assert hasattr(domain_ApplicationUIPackage, "uid")
    descriptor = None
    for klass in domain_ApplicationUIPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_styles_is_not_abstract():
    assert not inspect.isabstract(domain_Styles)


def test_domain_styles_constructor_exists():
    assert callable(domain_Styles.__init__)


def test_domain_styles_constructor_args():
    sig = inspect.signature(domain_Styles.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_styles_has_uid():
    assert hasattr(domain_Styles, "uid")
    descriptor = None
    for klass in domain_Styles.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_roles_is_not_abstract():
    assert not inspect.isabstract(domain_Roles)


def test_domain_roles_constructor_exists():
    assert callable(domain_Roles.__init__)


def test_domain_roles_constructor_args():
    sig = inspect.signature(domain_Roles.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_roles_has_uid():
    assert hasattr(domain_Roles, "uid")
    descriptor = None
    for klass in domain_Roles.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_messages_is_not_abstract():
    assert not inspect.isabstract(domain_Messages)


def test_domain_messages_constructor_exists():
    assert callable(domain_Messages.__init__)


def test_domain_messages_constructor_args():
    sig = inspect.signature(domain_Messages.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_messages_has_uid():
    assert hasattr(domain_Messages, "uid")
    descriptor = None
    for klass in domain_Messages.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationmessages_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationMessages)


def test_domain_applicationmessages_constructor_exists():
    assert callable(domain_ApplicationMessages.__init__)


def test_domain_applicationmessages_constructor_args():
    sig = inspect.signature(domain_ApplicationMessages.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationmessages_has_name():
    assert hasattr(domain_ApplicationMessages, "name")
    descriptor = None
    for klass in domain_ApplicationMessages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationmessages_has_uid():
    assert hasattr(domain_ApplicationMessages, "uid")
    descriptor = None
    for klass in domain_ApplicationMessages.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationrole_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationRole)


def test_domain_applicationrole_constructor_exists():
    assert callable(domain_ApplicationRole.__init__)


def test_domain_applicationrole_constructor_args():
    sig = inspect.signature(domain_ApplicationRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationrole_has_name():
    assert hasattr(domain_ApplicationRole, "name")
    descriptor = None
    for klass in domain_ApplicationRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationrole_has_uid():
    assert hasattr(domain_ApplicationRole, "uid")
    descriptor = None
    for klass in domain_ApplicationRole.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationinfrastructurelayer_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationInfrastructureLayer)


def test_domain_applicationinfrastructurelayer_constructor_exists():
    assert callable(domain_ApplicationInfrastructureLayer.__init__)


def test_domain_applicationinfrastructurelayer_constructor_args():
    sig = inspect.signature(domain_ApplicationInfrastructureLayer.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_applicationinfrastructurelayer_has_uid():
    assert hasattr(domain_ApplicationInfrastructureLayer, "uid")
    descriptor = None
    for klass in domain_ApplicationInfrastructureLayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationinfrastructurelayer_has_name():
    assert hasattr(domain_ApplicationInfrastructureLayer, "name")
    descriptor = None
    for klass in domain_ApplicationInfrastructureLayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_stylespackage_is_not_abstract():
    assert not inspect.isabstract(domain_StylesPackage)


def test_domain_stylespackage_constructor_exists():
    assert callable(domain_StylesPackage.__init__)


def test_domain_stylespackage_constructor_args():
    sig = inspect.signature(domain_StylesPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_stylespackage_has_name():
    assert hasattr(domain_StylesPackage, "name")
    descriptor = None
    for klass in domain_StylesPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_stylespackage_has_uid():
    assert hasattr(domain_StylesPackage, "uid")
    descriptor = None
    for klass in domain_StylesPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_option_is_not_abstract():
    assert not inspect.isabstract(domain_Option)


def test_domain_option_constructor_exists():
    assert callable(domain_Option.__init__)


def test_domain_option_constructor_args():
    sig = inspect.signature(domain_Option.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "value" in params, "Missing parameter 'value'"

def test_domain_option_has_uid():
    assert hasattr(domain_Option, "uid")
    descriptor = None
    for klass in domain_Option.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_option_has_value():
    assert hasattr(domain_Option, "value")
    descriptor = None
    for klass in domain_Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_domain_queryparameter_is_not_abstract():
    assert not inspect.isabstract(domain_QueryParameter)


def test_domain_queryparameter_constructor_exists():
    assert callable(domain_QueryParameter.__init__)


def test_domain_queryparameter_constructor_args():
    sig = inspect.signature(domain_QueryParameter.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_queryparameter_has_uid():
    assert hasattr(domain_QueryParameter, "uid")
    descriptor = None
    for klass in domain_QueryParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_queryparameter_has_name():
    assert hasattr(domain_QueryParameter, "name")
    descriptor = None
    for klass in domain_QueryParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_specifier_is_not_abstract():
    assert not inspect.isabstract(domain_Specifier)


def test_domain_specifier_constructor_exists():
    assert callable(domain_Specifier.__init__)


def test_domain_specifier_constructor_args():
    sig = inspect.signature(domain_Specifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_specifier_has_name():
    assert hasattr(domain_Specifier, "name")
    descriptor = None
    for klass in domain_Specifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_specifier_has_uid():
    assert hasattr(domain_Specifier, "uid")
    descriptor = None
    for klass in domain_Specifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_modelquery_is_not_abstract():
    assert not inspect.isabstract(domain_ModelQuery)


def test_domain_modelquery_constructor_exists():
    assert callable(domain_ModelQuery.__init__)


def test_domain_modelquery_constructor_args():
    sig = inspect.signature(domain_ModelQuery.__init__)
    params = list(sig.parameters.keys())
    assert "query" in params, "Missing parameter 'query'"
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_modelquery_has_query():
    assert hasattr(domain_ModelQuery, "query")
    descriptor = None
    for klass in domain_ModelQuery.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_domain_modelquery_has_name():
    assert hasattr(domain_ModelQuery, "name")
    descriptor = None
    for klass in domain_ModelQuery.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_modelquery_has_uid():
    assert hasattr(domain_ModelQuery, "uid")
    descriptor = None
    for klass in domain_ModelQuery.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_confighash_is_not_abstract():
    assert not inspect.isabstract(domain_ConfigHash)


def test_domain_confighash_constructor_exists():
    assert callable(domain_ConfigHash.__init__)


def test_domain_confighash_constructor_args():
    sig = inspect.signature(domain_ConfigHash.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_confighash_has_uid():
    assert hasattr(domain_ConfigHash, "uid")
    descriptor = None
    for klass in domain_ConfigHash.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_confighash_has_name():
    assert hasattr(domain_ConfigHash, "name")
    descriptor = None
    for klass in domain_ConfigHash.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_configvariable_is_not_abstract():
    assert not inspect.isabstract(domain_ConfigVariable)


def test_domain_configvariable_constructor_exists():
    assert callable(domain_ConfigVariable.__init__)


def test_domain_configvariable_constructor_args():
    sig = inspect.signature(domain_ConfigVariable.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_configvariable_has_uid():
    assert hasattr(domain_ConfigVariable, "uid")
    descriptor = None
    for klass in domain_ConfigVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_configvariable_has_name():
    assert hasattr(domain_ConfigVariable, "name")
    descriptor = None
    for klass in domain_ConfigVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_artifact_is_not_abstract():
    assert not inspect.isabstract(domain_Artifact)


def test_domain_artifact_constructor_exists():
    assert callable(domain_Artifact.__init__)


def test_domain_artifact_constructor_args():
    sig = inspect.signature(domain_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "template" in params, "Missing parameter 'template'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_artifact_has_description():
    assert hasattr(domain_Artifact, "description")
    descriptor = None
    for klass in domain_Artifact.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_domain_artifact_has_template():
    assert hasattr(domain_Artifact, "template")
    descriptor = None
    for klass in domain_Artifact.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_domain_artifact_has_uid():
    assert hasattr(domain_Artifact, "uid")
    descriptor = None
    for klass in domain_Artifact.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_artifact_has_name():
    assert hasattr(domain_Artifact, "name")
    descriptor = None
    for klass in domain_Artifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainartifact_is_not_abstract():
    assert not inspect.isabstract(DomainArtifact)


def test_domainartifact_constructor_exists():
    assert callable(DomainArtifact.__init__)


def test_domainartifact_constructor_args():
    sig = inspect.signature(DomainArtifact.__init__)
    params = list(sig.parameters.keys())



def test_domain_jpaservice_is_not_abstract():
    assert not inspect.isabstract(domain_JPAService)


def test_domain_jpaservice_constructor_exists():
    assert callable(domain_JPAService.__init__)


def test_domain_jpaservice_constructor_args():
    sig = inspect.signature(domain_JPAService.__init__)
    params = list(sig.parameters.keys())



def test_domain_ejbservice_is_not_abstract():
    assert not inspect.isabstract(domain_EJBService)


def test_domain_ejbservice_constructor_exists():
    assert callable(domain_EJBService.__init__)


def test_domain_ejbservice_constructor_args():
    sig = inspect.signature(domain_EJBService.__init__)
    params = list(sig.parameters.keys())



def test_domain_continuousiintegration_is_not_abstract():
    assert not inspect.isabstract(domain_ContinuousIintegration)


def test_domain_continuousiintegration_constructor_exists():
    assert callable(domain_ContinuousIintegration.__init__)


def test_domain_continuousiintegration_constructor_args():
    sig = inspect.signature(domain_ContinuousIintegration.__init__)
    params = list(sig.parameters.keys())



def test_domain_ormentity_is_not_abstract():
    assert not inspect.isabstract(domain_ORMEntity)


def test_domain_ormentity_constructor_exists():
    assert callable(domain_ORMEntity.__init__)


def test_domain_ormentity_constructor_args():
    sig = inspect.signature(domain_ORMEntity.__init__)
    params = list(sig.parameters.keys())



def test_domain_artifacts_is_not_abstract():
    assert not inspect.isabstract(domain_Artifacts)


def test_domain_artifacts_constructor_exists():
    assert callable(domain_Artifacts.__init__)


def test_domain_artifacts_constructor_args():
    sig = inspect.signature(domain_Artifacts.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_artifacts_has_uid():
    assert hasattr(domain_Artifacts, "uid")
    descriptor = None
    for klass in domain_Artifacts.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_application_is_not_abstract():
    assert not inspect.isabstract(domain_Application)


def test_domain_application_constructor_exists():
    assert callable(domain_Application.__init__)


def test_domain_application_constructor_args():
    sig = inspect.signature(domain_Application.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_application_has_uid():
    assert hasattr(domain_Application, "uid")
    descriptor = None
    for klass in domain_Application.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_domainartifact_is_not_abstract():
    assert not inspect.isabstract(domain_DomainArtifact)


def test_domain_domainartifact_constructor_exists():
    assert callable(domain_DomainArtifact.__init__)


def test_domain_domainartifact_constructor_args():
    sig = inspect.signature(domain_DomainArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_domainartifact_has_uid():
    assert hasattr(domain_DomainArtifact, "uid")
    descriptor = None
    for klass in domain_DomainArtifact.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_domainartifact_has_name():
    assert hasattr(domain_DomainArtifact, "name")
    descriptor = None
    for klass in domain_DomainArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_htmllayerholder_is_not_abstract():
    assert not inspect.isabstract(HTMLLayerHolder)


def test_htmllayerholder_constructor_exists():
    assert callable(HTMLLayerHolder.__init__)


def test_htmllayerholder_constructor_args():
    sig = inspect.signature(HTMLLayerHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain_component_is_not_abstract():
    assert not inspect.isabstract(domain_Component)


def test_domain_component_constructor_exists():
    assert callable(domain_Component.__init__)


def test_domain_component_constructor_args():
    sig = inspect.signature(domain_Component.__init__)
    params = list(sig.parameters.keys())
    assert "componentRoot" in params, "Missing parameter 'componentRoot'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_component_has_componentRoot():
    assert hasattr(domain_Component, "componentRoot")
    descriptor = None
    for klass in domain_Component.__mro__:
        if "componentRoot" in klass.__dict__:
            descriptor = klass.__dict__["componentRoot"]
            break
    assert isinstance(descriptor, property)

def test_domain_component_has_uid():
    assert hasattr(domain_Component, "uid")
    descriptor = None
    for klass in domain_Component.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_component_has_name():
    assert hasattr(domain_Component, "name")
    descriptor = None
    for klass in domain_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationstyle_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationStyle)


def test_domain_applicationstyle_constructor_exists():
    assert callable(domain_ApplicationStyle.__init__)


def test_domain_applicationstyle_constructor_args():
    sig = inspect.signature(domain_ApplicationStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationstyle_has_name():
    assert hasattr(domain_ApplicationStyle, "name")
    descriptor = None
    for klass in domain_ApplicationStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationstyle_has_uid():
    assert hasattr(domain_ApplicationStyle, "uid")
    descriptor = None
    for klass in domain_ApplicationStyle.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationmappers_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationMappers)


def test_domain_applicationmappers_constructor_exists():
    assert callable(domain_ApplicationMappers.__init__)


def test_domain_applicationmappers_constructor_args():
    sig = inspect.signature(domain_ApplicationMappers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationmappers_has_name():
    assert hasattr(domain_ApplicationMappers, "name")
    descriptor = None
    for klass in domain_ApplicationMappers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationmappers_has_uid():
    assert hasattr(domain_ApplicationMappers, "uid")
    descriptor = None
    for klass in domain_ApplicationMappers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_ingredient_is_not_abstract():
    assert not inspect.isabstract(domain_Ingredient)


def test_domain_ingredient_constructor_exists():
    assert callable(domain_Ingredient.__init__)


def test_domain_ingredient_constructor_args():
    sig = inspect.signature(domain_Ingredient.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "layer" in params, "Missing parameter 'layer'"

def test_domain_ingredient_has_uid():
    assert hasattr(domain_Ingredient, "uid")
    descriptor = None
    for klass in domain_Ingredient.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_ingredient_has_name():
    assert hasattr(domain_Ingredient, "name")
    descriptor = None
    for klass in domain_Ingredient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_ingredient_has_layer():
    assert hasattr(domain_Ingredient, "layer")
    descriptor = None
    for klass in domain_Ingredient.__mro__:
        if "layer" in klass.__dict__:
            descriptor = klass.__dict__["layer"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationrecipes_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationRecipes)


def test_domain_applicationrecipes_constructor_exists():
    assert callable(domain_ApplicationRecipes.__init__)


def test_domain_applicationrecipes_constructor_args():
    sig = inspect.signature(domain_ApplicationRecipes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_applicationrecipes_has_name():
    assert hasattr(domain_ApplicationRecipes, "name")
    descriptor = None
    for klass in domain_ApplicationRecipes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationrecipes_has_uid():
    assert hasattr(domain_ApplicationRecipes, "uid")
    descriptor = None
    for klass in domain_ApplicationRecipes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_applicationuilayer_is_not_abstract():
    assert not inspect.isabstract(domain_ApplicationUILayer)


def test_domain_applicationuilayer_constructor_exists():
    assert callable(domain_ApplicationUILayer.__init__)


def test_domain_applicationuilayer_constructor_args():
    sig = inspect.signature(domain_ApplicationUILayer.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_applicationuilayer_has_uid():
    assert hasattr(domain_ApplicationUILayer, "uid")
    descriptor = None
    for klass in domain_ApplicationUILayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_applicationuilayer_has_name():
    assert hasattr(domain_ApplicationUILayer, "name")
    descriptor = None
    for klass in domain_ApplicationUILayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_role_is_not_abstract():
    assert not inspect.isabstract(domain_Role)


def test_domain_role_constructor_exists():
    assert callable(domain_Role.__init__)


def test_domain_role_constructor_args():
    sig = inspect.signature(domain_Role.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_role_has_uid():
    assert hasattr(domain_Role, "uid")
    descriptor = None
    for klass in domain_Role.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_role_has_name():
    assert hasattr(domain_Role, "name")
    descriptor = None
    for klass in domain_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_domainapplication_is_not_abstract():
    assert not inspect.isabstract(domain_DomainApplication)


def test_domain_domainapplication_constructor_exists():
    assert callable(domain_DomainApplication.__init__)


def test_domain_domainapplication_constructor_args():
    sig = inspect.signature(domain_DomainApplication.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_domainapplication_has_uid():
    assert hasattr(domain_DomainApplication, "uid")
    descriptor = None
    for klass in domain_DomainApplication.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_domainapplication_has_name():
    assert hasattr(domain_DomainApplication, "name")
    descriptor = None
    for klass in domain_DomainApplication.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_grantaccess_is_not_abstract():
    assert not inspect.isabstract(domain_GrantAccess)


def test_domain_grantaccess_constructor_exists():
    assert callable(domain_GrantAccess.__init__)


def test_domain_grantaccess_constructor_args():
    sig = inspect.signature(domain_GrantAccess.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_grantaccess_has_uid():
    assert hasattr(domain_GrantAccess, "uid")
    descriptor = None
    for klass in domain_GrantAccess.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_secured_is_not_abstract():
    assert not inspect.isabstract(domain_Secured)


def test_domain_secured_constructor_exists():
    assert callable(domain_Secured.__init__)


def test_domain_secured_constructor_args():
    sig = inspect.signature(domain_Secured.__init__)
    params = list(sig.parameters.keys())



def test_domain_generationhint_is_not_abstract():
    assert not inspect.isabstract(domain_GenerationHint)


def test_domain_generationhint_constructor_exists():
    assert callable(domain_GenerationHint.__init__)


def test_domain_generationhint_constructor_args():
    sig = inspect.signature(domain_GenerationHint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "applyedClass" in params, "Missing parameter 'applyedClass'"

def test_domain_generationhint_has_name():
    assert hasattr(domain_GenerationHint, "name")
    descriptor = None
    for klass in domain_GenerationHint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_generationhint_has_uid():
    assert hasattr(domain_GenerationHint, "uid")
    descriptor = None
    for klass in domain_GenerationHint.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_generationhint_has_applyedClass():
    assert hasattr(domain_GenerationHint, "applyedClass")
    descriptor = None
    for klass in domain_GenerationHint.__mro__:
        if "applyedClass" in klass.__dict__:
            descriptor = klass.__dict__["applyedClass"]
            break
    assert isinstance(descriptor, property)



def test_domain_classifier_is_not_abstract():
    assert not inspect.isabstract(domain_Classifier)


def test_domain_classifier_constructor_exists():
    assert callable(domain_Classifier.__init__)


def test_domain_classifier_constructor_args():
    sig = inspect.signature(domain_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_classifier_has_details():
    assert hasattr(domain_Classifier, "details")
    descriptor = None
    for klass in domain_Classifier.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_domain_classifier_has_uid():
    assert hasattr(domain_Classifier, "uid")
    descriptor = None
    for klass in domain_Classifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_categorized_is_not_abstract():
    assert not inspect.isabstract(domain_Categorized)


def test_domain_categorized_constructor_exists():
    assert callable(domain_Categorized.__init__)


def test_domain_categorized_constructor_args():
    sig = inspect.signature(domain_Categorized.__init__)
    params = list(sig.parameters.keys())



def test_domain_htmllayerholder_is_not_abstract():
    assert not inspect.isabstract(domain_HTMLLayerHolder)


def test_domain_htmllayerholder_constructor_exists():
    assert callable(domain_HTMLLayerHolder.__init__)


def test_domain_htmllayerholder_constructor_args():
    sig = inspect.signature(domain_HTMLLayerHolder.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"

def test_domain_htmllayerholder_has_columns():
    assert hasattr(domain_HTMLLayerHolder, "columns")
    descriptor = None
    for klass in domain_HTMLLayerHolder.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_domain_eobject_is_not_abstract():
    assert not inspect.isabstract(domain_EObject)


def test_domain_eobject_constructor_exists():
    assert callable(domain_EObject.__init__)


def test_domain_eobject_constructor_args():
    sig = inspect.signature(domain_EObject.__init__)
    params = list(sig.parameters.keys())



def test_domain_domainapplications_is_not_abstract():
    assert not inspect.isabstract(domain_DomainApplications)


def test_domain_domainapplications_constructor_exists():
    assert callable(domain_DomainApplications.__init__)


def test_domain_domainapplications_constructor_args():
    sig = inspect.signature(domain_DomainApplications.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_domainapplications_has_name():
    assert hasattr(domain_DomainApplications, "name")
    descriptor = None
    for klass in domain_DomainApplications.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_domainapplications_has_uid():
    assert hasattr(domain_DomainApplications, "uid")
    descriptor = None
    for klass in domain_DomainApplications.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_domaintypes_is_not_abstract():
    assert not inspect.isabstract(domain_DomainTypes)


def test_domain_domaintypes_constructor_exists():
    assert callable(domain_DomainTypes.__init__)


def test_domain_domaintypes_constructor_args():
    sig = inspect.signature(domain_DomainTypes.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_domaintypes_has_uid():
    assert hasattr(domain_DomainTypes, "uid")
    descriptor = None
    for klass in domain_DomainTypes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_domaintypes_has_name():
    assert hasattr(domain_DomainTypes, "name")
    descriptor = None
    for klass in domain_DomainTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_domainartifacts_is_not_abstract():
    assert not inspect.isabstract(domain_DomainArtifacts)


def test_domain_domainartifacts_constructor_exists():
    assert callable(domain_DomainArtifacts.__init__)


def test_domain_domainartifacts_constructor_args():
    sig = inspect.signature(domain_DomainArtifacts.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_domainartifacts_has_uid():
    assert hasattr(domain_DomainArtifacts, "uid")
    descriptor = None
    for klass in domain_DomainArtifacts.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_domainartifacts_has_name():
    assert hasattr(domain_DomainArtifacts, "name")
    descriptor = None
    for klass in domain_DomainArtifacts.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_domain_is_not_abstract():
    assert not inspect.isabstract(domain_Domain)


def test_domain_domain_constructor_exists():
    assert callable(domain_Domain.__init__)


def test_domain_domain_constructor_args():
    sig = inspect.signature(domain_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_domain_has_uid():
    assert hasattr(domain_Domain, "uid")
    descriptor = None
    for klass in domain_Domain.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_typesrepository_is_not_abstract():
    assert not inspect.isabstract(domain_TypesRepository)


def test_domain_typesrepository_constructor_exists():
    assert callable(domain_TypesRepository.__init__)


def test_domain_typesrepository_constructor_args():
    sig = inspect.signature(domain_TypesRepository.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_typesrepository_has_uid():
    assert hasattr(domain_TypesRepository, "uid")
    descriptor = None
    for klass in domain_TypesRepository.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_menuextensionref_is_not_abstract():
    assert not inspect.isabstract(MenuExtensionRef)


def test_menuextensionref_constructor_exists():
    assert callable(MenuExtensionRef.__init__)


def test_menuextensionref_constructor_args():
    sig = inspect.signature(MenuExtensionRef.__init__)
    params = list(sig.parameters.keys())



def test_menuelement_is_not_abstract():
    assert not inspect.isabstract(MenuElement)


def test_menuelement_constructor_exists():
    assert callable(MenuElement.__init__)


def test_menuelement_constructor_args():
    sig = inspect.signature(MenuElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuextensionpoint_is_not_abstract():
    assert not inspect.isabstract(domain_MenuExtensionPoint)


def test_domain_menuextensionpoint_constructor_exists():
    assert callable(domain_MenuExtensionPoint.__init__)


def test_domain_menuextensionpoint_constructor_args():
    sig = inspect.signature(domain_MenuExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuseparator_is_not_abstract():
    assert not inspect.isabstract(domain_MenuSeparator)


def test_domain_menuseparator_constructor_exists():
    assert callable(domain_MenuSeparator.__init__)


def test_domain_menuseparator_constructor_args():
    sig = inspect.signature(domain_MenuSeparator.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuextensionref_is_not_abstract():
    assert not inspect.isabstract(domain_MenuExtensionRef)


def test_domain_menuextensionref_constructor_exists():
    assert callable(domain_MenuExtensionRef.__init__)


def test_domain_menuextensionref_constructor_args():
    sig = inspect.signature(domain_MenuExtensionRef.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuholder_is_not_abstract():
    assert not inspect.isabstract(domain_MenuHolder)


def test_domain_menuholder_constructor_exists():
    assert callable(domain_MenuHolder.__init__)


def test_domain_menuholder_constructor_args():
    sig = inspect.signature(domain_MenuHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain_infrastructurecomponent_is_not_abstract():
    assert not inspect.isabstract(domain_InfrastructureComponent)


def test_domain_infrastructurecomponent_constructor_exists():
    assert callable(domain_InfrastructureComponent.__init__)


def test_domain_infrastructurecomponent_constructor_args():
    sig = inspect.signature(domain_InfrastructureComponent.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_infrastructurecomponent_has_uid():
    assert hasattr(domain_InfrastructureComponent, "uid")
    descriptor = None
    for klass in domain_InfrastructureComponent.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_infrastructurecomponent_has_name():
    assert hasattr(domain_InfrastructureComponent, "name")
    descriptor = None
    for klass in domain_InfrastructureComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_infrastructurelayer_is_not_abstract():
    assert not inspect.isabstract(domain_InfrastructureLayer)


def test_domain_infrastructurelayer_constructor_exists():
    assert callable(domain_InfrastructureLayer.__init__)


def test_domain_infrastructurelayer_constructor_args():
    sig = inspect.signature(domain_InfrastructureLayer.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_infrastructurelayer_has_uid():
    assert hasattr(domain_InfrastructureLayer, "uid")
    descriptor = None
    for klass in domain_InfrastructureLayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_infrastructurelayer_has_name():
    assert hasattr(domain_InfrastructureLayer, "name")
    descriptor = None
    for klass in domain_InfrastructureLayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_subsystem_is_not_abstract():
    assert not inspect.isabstract(domain_Subsystem)


def test_domain_subsystem_constructor_exists():
    assert callable(domain_Subsystem.__init__)


def test_domain_subsystem_constructor_args():
    sig = inspect.signature(domain_Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_subsystem_has_uid():
    assert hasattr(domain_Subsystem, "uid")
    descriptor = None
    for klass in domain_Subsystem.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_subsystem_has_name():
    assert hasattr(domain_Subsystem, "name")
    descriptor = None
    for klass in domain_Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_infrastructurecomponent_is_not_abstract():
    assert not inspect.isabstract(InfrastructureComponent)


def test_infrastructurecomponent_constructor_exists():
    assert callable(InfrastructureComponent.__init__)


def test_infrastructurecomponent_constructor_args():
    sig = inspect.signature(InfrastructureComponent.__init__)
    params = list(sig.parameters.keys())



def test_domain_serverclaster_is_not_abstract():
    assert not inspect.isabstract(domain_ServerClaster)


def test_domain_serverclaster_constructor_exists():
    assert callable(domain_ServerClaster.__init__)


def test_domain_serverclaster_constructor_args():
    sig = inspect.signature(domain_ServerClaster.__init__)
    params = list(sig.parameters.keys())



def test_domain_storage_is_not_abstract():
    assert not inspect.isabstract(domain_Storage)


def test_domain_storage_constructor_exists():
    assert callable(domain_Storage.__init__)


def test_domain_storage_constructor_args():
    sig = inspect.signature(domain_Storage.__init__)
    params = list(sig.parameters.keys())



def test_domain_router_is_not_abstract():
    assert not inspect.isabstract(domain_Router)


def test_domain_router_constructor_exists():
    assert callable(domain_Router.__init__)


def test_domain_router_constructor_args():
    sig = inspect.signature(domain_Router.__init__)
    params = list(sig.parameters.keys())



def test_domain_hub_is_not_abstract():
    assert not inspect.isabstract(domain_Hub)


def test_domain_hub_constructor_exists():
    assert callable(domain_Hub.__init__)


def test_domain_hub_constructor_args():
    sig = inspect.signature(domain_Hub.__init__)
    params = list(sig.parameters.keys())



def test_domain_server_is_not_abstract():
    assert not inspect.isabstract(domain_Server)


def test_domain_server_constructor_exists():
    assert callable(domain_Server.__init__)


def test_domain_server_constructor_args():
    sig = inspect.signature(domain_Server.__init__)
    params = list(sig.parameters.keys())



def test_domain_enterpriseinfrastructure_is_not_abstract():
    assert not inspect.isabstract(domain_EnterpriseInfrastructure)


def test_domain_enterpriseinfrastructure_constructor_exists():
    assert callable(domain_EnterpriseInfrastructure.__init__)


def test_domain_enterpriseinfrastructure_constructor_args():
    sig = inspect.signature(domain_EnterpriseInfrastructure.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_enterpriseinfrastructure_has_uid():
    assert hasattr(domain_EnterpriseInfrastructure, "uid")
    descriptor = None
    for klass in domain_EnterpriseInfrastructure.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_infrastructureconnection_is_not_abstract():
    assert not inspect.isabstract(domain_InfrastructureConnection)


def test_domain_infrastructureconnection_constructor_exists():
    assert callable(domain_InfrastructureConnection.__init__)


def test_domain_infrastructureconnection_constructor_args():
    sig = inspect.signature(domain_InfrastructureConnection.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_infrastructureconnection_has_uid():
    assert hasattr(domain_InfrastructureConnection, "uid")
    descriptor = None
    for klass in domain_InfrastructureConnection.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_datacenter_is_not_abstract():
    assert not inspect.isabstract(domain_Datacenter)


def test_domain_datacenter_constructor_exists():
    assert callable(domain_Datacenter.__init__)


def test_domain_datacenter_constructor_args():
    sig = inspect.signature(domain_Datacenter.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_datacenter_has_uid():
    assert hasattr(domain_Datacenter, "uid")
    descriptor = None
    for klass in domain_Datacenter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_datacenter_has_name():
    assert hasattr(domain_Datacenter, "name")
    descriptor = None
    for klass in domain_Datacenter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_orderby_is_not_abstract():
    assert not inspect.isabstract(domain_OrderBy)


def test_domain_orderby_constructor_exists():
    assert callable(domain_OrderBy.__init__)


def test_domain_orderby_constructor_args():
    sig = inspect.signature(domain_OrderBy.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_orderby_has_order():
    assert hasattr(domain_OrderBy, "order")
    descriptor = None
    for klass in domain_OrderBy.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_domain_orderby_has_uid():
    assert hasattr(domain_OrderBy, "uid")
    descriptor = None
    for klass in domain_OrderBy.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_orders_is_not_abstract():
    assert not inspect.isabstract(domain_Orders)


def test_domain_orders_constructor_exists():
    assert callable(domain_Orders.__init__)


def test_domain_orders_constructor_args():
    sig = inspect.signature(domain_Orders.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_orders_has_uid():
    assert hasattr(domain_Orders, "uid")
    descriptor = None
    for klass in domain_Orders.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_artificialfield_is_not_abstract():
    assert not inspect.isabstract(domain_ArtificialField)


def test_domain_artificialfield_constructor_exists():
    assert callable(domain_ArtificialField.__init__)


def test_domain_artificialfield_constructor_args():
    sig = inspect.signature(domain_ArtificialField.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_artificialfield_has_uid():
    assert hasattr(domain_ArtificialField, "uid")
    descriptor = None
    for klass in domain_ArtificialField.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_artificialfield_has_name():
    assert hasattr(domain_ArtificialField, "name")
    descriptor = None
    for klass in domain_ArtificialField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_formvariable_is_not_abstract():
    assert not inspect.isabstract(domain_FormVariable)


def test_domain_formvariable_constructor_exists():
    assert callable(domain_FormVariable.__init__)


def test_domain_formvariable_constructor_args():
    sig = inspect.signature(domain_FormVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_formvariable_has_name():
    assert hasattr(domain_FormVariable, "name")
    descriptor = None
    for klass in domain_FormVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_formvariable_has_uid():
    assert hasattr(domain_FormVariable, "uid")
    descriptor = None
    for klass in domain_FormVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_proxieslist_is_not_abstract():
    assert not inspect.isabstract(ProxiesList)


def test_proxieslist_constructor_exists():
    assert callable(ProxiesList.__init__)


def test_proxieslist_constructor_args():
    sig = inspect.signature(ProxiesList.__init__)
    params = list(sig.parameters.keys())



def test_domain_proxieslist_is_not_abstract():
    assert not inspect.isabstract(domain_ProxiesList)


def test_domain_proxieslist_constructor_exists():
    assert callable(domain_ProxiesList.__init__)


def test_domain_proxieslist_constructor_args():
    sig = inspect.signature(domain_ProxiesList.__init__)
    params = list(sig.parameters.keys())



def test_methodpointer_is_not_abstract():
    assert not inspect.isabstract(MethodPointer)


def test_methodpointer_constructor_exists():
    assert callable(MethodPointer.__init__)


def test_methodpointer_constructor_args():
    sig = inspect.signature(MethodPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain_dependency_is_not_abstract():
    assert not inspect.isabstract(domain_Dependency)


def test_domain_dependency_constructor_exists():
    assert callable(domain_Dependency.__init__)


def test_domain_dependency_constructor_args():
    sig = inspect.signature(domain_Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_dependency_has_uid():
    assert hasattr(domain_Dependency, "uid")
    descriptor = None
    for klass in domain_Dependency.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_dependency_has_name():
    assert hasattr(domain_Dependency, "name")
    descriptor = None
    for klass in domain_Dependency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_root_is_not_abstract():
    assert not inspect.isabstract(domain_Root)


def test_domain_root_constructor_exists():
    assert callable(domain_Root.__init__)


def test_domain_root_constructor_args():
    sig = inspect.signature(domain_Root.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_root_has_uid():
    assert hasattr(domain_Root, "uid")
    descriptor = None
    for klass in domain_Root.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_root_has_name():
    assert hasattr(domain_Root, "name")
    descriptor = None
    for klass in domain_Root.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_itemicon_is_not_abstract():
    assert not inspect.isabstract(ItemIcon)


def test_itemicon_constructor_exists():
    assert callable(ItemIcon.__init__)


def test_itemicon_constructor_args():
    sig = inspect.signature(ItemIcon.__init__)
    params = list(sig.parameters.keys())



def test_domain_submenu_is_not_abstract():
    assert not inspect.isabstract(domain_SubMenu)


def test_domain_submenu_constructor_exists():
    assert callable(domain_SubMenu.__init__)


def test_domain_submenu_constructor_args():
    sig = inspect.signature(domain_SubMenu.__init__)
    params = list(sig.parameters.keys())



def test_domain_relation_is_not_abstract():
    assert not inspect.isabstract(domain_Relation)


def test_domain_relation_constructor_exists():
    assert callable(domain_Relation.__init__)


def test_domain_relation_constructor_args():
    sig = inspect.signature(domain_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isTree" in params, "Missing parameter 'isTree'"

def test_domain_relation_has_uid():
    assert hasattr(domain_Relation, "uid")
    descriptor = None
    for klass in domain_Relation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_relation_has_name():
    assert hasattr(domain_Relation, "name")
    descriptor = None
    for klass in domain_Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_relation_has_isTree():
    assert hasattr(domain_Relation, "isTree")
    descriptor = None
    for klass in domain_Relation.__mro__:
        if "isTree" in klass.__dict__:
            descriptor = klass.__dict__["isTree"]
            break
    assert isinstance(descriptor, property)



def test_optionselection_is_not_abstract():
    assert not inspect.isabstract(OptionSelection)


def test_optionselection_constructor_exists():
    assert callable(OptionSelection.__init__)


def test_optionselection_constructor_args():
    sig = inspect.signature(OptionSelection.__init__)
    params = list(sig.parameters.keys())



def test_domain_dropdownselection_is_not_abstract():
    assert not inspect.isabstract(domain_DropDownSelection)


def test_domain_dropdownselection_constructor_exists():
    assert callable(domain_DropDownSelection.__init__)


def test_domain_dropdownselection_constructor_args():
    sig = inspect.signature(domain_DropDownSelection.__init__)
    params = list(sig.parameters.keys())
    assert "initialOptionValue" in params, "Missing parameter 'initialOptionValue'"

def test_domain_dropdownselection_has_initialOptionValue():
    assert hasattr(domain_DropDownSelection, "initialOptionValue")
    descriptor = None
    for klass in domain_DropDownSelection.__mro__:
        if "initialOptionValue" in klass.__dict__:
            descriptor = klass.__dict__["initialOptionValue"]
            break
    assert isinstance(descriptor, property)



def test_formatable_is_not_abstract():
    assert not inspect.isabstract(Formatable)


def test_formatable_constructor_exists():
    assert callable(Formatable.__init__)


def test_formatable_constructor_args():
    sig = inspect.signature(Formatable.__init__)
    params = list(sig.parameters.keys())



def test_childrenholder_is_not_abstract():
    assert not inspect.isabstract(ChildrenHolder)


def test_childrenholder_constructor_exists():
    assert callable(ChildrenHolder.__init__)


def test_childrenholder_constructor_args():
    sig = inspect.signature(ChildrenHolder.__init__)
    params = list(sig.parameters.keys())



def test_sourcespointer_is_not_abstract():
    assert not inspect.isabstract(SourcesPointer)


def test_sourcespointer_constructor_exists():
    assert callable(SourcesPointer.__init__)


def test_sourcespointer_constructor_args():
    sig = inspect.signature(SourcesPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain_datacontrol_is_not_abstract():
    assert not inspect.isabstract(domain_DataControl)


def test_domain_datacontrol_constructor_exists():
    assert callable(domain_DataControl.__init__)


def test_domain_datacontrol_constructor_args():
    sig = inspect.signature(domain_DataControl.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_datacontrol_has_uid():
    assert hasattr(domain_DataControl, "uid")
    descriptor = None
    for klass in domain_DataControl.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_datacontrol_has_name():
    assert hasattr(domain_DataControl, "name")
    descriptor = None
    for klass in domain_DataControl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uielement_is_not_abstract():
    assert not inspect.isabstract(Uielement)


def test_uielement_constructor_exists():
    assert callable(Uielement.__init__)


def test_uielement_constructor_args():
    sig = inspect.signature(Uielement.__init__)
    params = list(sig.parameters.keys())



def test_domain_menu_is_not_abstract():
    assert not inspect.isabstract(domain_Menu)


def test_domain_menu_constructor_exists():
    assert callable(domain_Menu.__init__)


def test_domain_menu_constructor_args():
    sig = inspect.signature(domain_Menu.__init__)
    params = list(sig.parameters.keys())
    assert "fakeName" in params, "Missing parameter 'fakeName'"

def test_domain_menu_has_fakeName():
    assert hasattr(domain_Menu, "fakeName")
    descriptor = None
    for klass in domain_Menu.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)



def test_domain_sourcespointer_is_not_abstract():
    assert not inspect.isabstract(domain_SourcesPointer)


def test_domain_sourcespointer_constructor_exists():
    assert callable(domain_SourcesPointer.__init__)


def test_domain_sourcespointer_constructor_args():
    sig = inspect.signature(domain_SourcesPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain_formatable_is_not_abstract():
    assert not inspect.isabstract(domain_Formatable)


def test_domain_formatable_constructor_exists():
    assert callable(domain_Formatable.__init__)


def test_domain_formatable_constructor_args():
    sig = inspect.signature(domain_Formatable.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_domain_formatable_has_format():
    assert hasattr(domain_Formatable, "format")
    descriptor = None
    for klass in domain_Formatable.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_domain_itemicon_is_not_abstract():
    assert not inspect.isabstract(domain_ItemIcon)


def test_domain_itemicon_constructor_exists():
    assert callable(domain_ItemIcon.__init__)


def test_domain_itemicon_constructor_args():
    sig = inspect.signature(domain_ItemIcon.__init__)
    params = list(sig.parameters.keys())



def test_domain_arearef_is_not_abstract():
    assert not inspect.isabstract(domain_AreaRef)


def test_domain_arearef_constructor_exists():
    assert callable(domain_AreaRef.__init__)


def test_domain_arearef_constructor_args():
    sig = inspect.signature(domain_AreaRef.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_domain_arearef_has_group():
    assert hasattr(domain_AreaRef, "group")
    descriptor = None
    for klass in domain_AreaRef.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_menuholder_is_not_abstract():
    assert not inspect.isabstract(MenuHolder)


def test_menuholder_constructor_exists():
    assert callable(MenuHolder.__init__)


def test_menuholder_constructor_args():
    sig = inspect.signature(MenuHolder.__init__)
    params = list(sig.parameters.keys())



def test_enableduiitem_is_not_abstract():
    assert not inspect.isabstract(EnabledUIItem)


def test_enableduiitem_constructor_exists():
    assert callable(EnabledUIItem.__init__)


def test_enableduiitem_constructor_args():
    sig = inspect.signature(EnabledUIItem.__init__)
    params = list(sig.parameters.keys())



def test_domain_enableduiitem_is_not_abstract():
    assert not inspect.isabstract(domain_EnabledUIItem)


def test_domain_enableduiitem_constructor_exists():
    assert callable(domain_EnabledUIItem.__init__)


def test_domain_enableduiitem_constructor_args():
    sig = inspect.signature(domain_EnabledUIItem.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_domain_flexfield_is_not_abstract():
    assert not inspect.isabstract(domain_FlexField)


def test_domain_flexfield_constructor_exists():
    assert callable(domain_FlexField.__init__)


def test_domain_flexfield_constructor_args():
    sig = inspect.signature(domain_FlexField.__init__)
    params = list(sig.parameters.keys())



def test_domain_flexfields_is_not_abstract():
    assert not inspect.isabstract(domain_FlexFields)


def test_domain_flexfields_constructor_exists():
    assert callable(domain_FlexFields.__init__)


def test_domain_flexfields_constructor_args():
    sig = inspect.signature(domain_FlexFields.__init__)
    params = list(sig.parameters.keys())



def test_domain_nicknamed_is_not_abstract():
    assert not inspect.isabstract(domain_NickNamed)


def test_domain_nicknamed_constructor_exists():
    assert callable(domain_NickNamed.__init__)


def test_domain_nicknamed_constructor_args():
    sig = inspect.signature(domain_NickNamed.__init__)
    params = list(sig.parameters.keys())
    assert "nickname" in params, "Missing parameter 'nickname'"

def test_domain_nicknamed_has_nickname():
    assert hasattr(domain_NickNamed, "nickname")
    descriptor = None
    for klass in domain_NickNamed.__mro__:
        if "nickname" in klass.__dict__:
            descriptor = klass.__dict__["nickname"]
            break
    assert isinstance(descriptor, property)



def test_inputelement_is_not_abstract():
    assert not inspect.isabstract(InputElement)


def test_inputelement_constructor_exists():
    assert callable(InputElement.__init__)


def test_inputelement_constructor_args():
    sig = inspect.signature(InputElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_image_is_not_abstract():
    assert not inspect.isabstract(domain_Image)


def test_domain_image_constructor_exists():
    assert callable(domain_Image.__init__)


def test_domain_image_constructor_args():
    sig = inspect.signature(domain_Image.__init__)
    params = list(sig.parameters.keys())



def test_domain_password_is_not_abstract():
    assert not inspect.isabstract(domain_Password)


def test_domain_password_constructor_exists():
    assert callable(domain_Password.__init__)


def test_domain_password_constructor_args():
    sig = inspect.signature(domain_Password.__init__)
    params = list(sig.parameters.keys())



def test_domain_outputtext_is_not_abstract():
    assert not inspect.isabstract(domain_OutputText)


def test_domain_outputtext_constructor_exists():
    assert callable(domain_OutputText.__init__)


def test_domain_outputtext_constructor_args():
    sig = inspect.signature(domain_OutputText.__init__)
    params = list(sig.parameters.keys())



def test_domain_date_is_not_abstract():
    assert not inspect.isabstract(domain_Date)


def test_domain_date_constructor_exists():
    assert callable(domain_Date.__init__)


def test_domain_date_constructor_args():
    sig = inspect.signature(domain_Date.__init__)
    params = list(sig.parameters.keys())



def test_domain_inputtext_is_not_abstract():
    assert not inspect.isabstract(domain_InputText)


def test_domain_inputtext_constructor_exists():
    assert callable(domain_InputText.__init__)


def test_domain_inputtext_constructor_args():
    sig = inspect.signature(domain_InputText.__init__)
    params = list(sig.parameters.keys())



def test_domain_checkbox_is_not_abstract():
    assert not inspect.isabstract(domain_CheckBox)


def test_domain_checkbox_constructor_exists():
    assert callable(domain_CheckBox.__init__)


def test_domain_checkbox_constructor_args():
    sig = inspect.signature(domain_CheckBox.__init__)
    params = list(sig.parameters.keys())



def test_domain_optionselection_is_not_abstract():
    assert not inspect.isabstract(domain_OptionSelection)


def test_domain_optionselection_constructor_exists():
    assert callable(domain_OptionSelection.__init__)


def test_domain_optionselection_constructor_args():
    sig = inspect.signature(domain_OptionSelection.__init__)
    params = list(sig.parameters.keys())



def test_domain_styleelement_is_not_abstract():
    assert not inspect.isabstract(domain_StyleElement)


def test_domain_styleelement_constructor_exists():
    assert callable(domain_StyleElement.__init__)


def test_domain_styleelement_constructor_args():
    sig = inspect.signature(domain_StyleElement.__init__)
    params = list(sig.parameters.keys())



def test_contextparameters_is_not_abstract():
    assert not inspect.isabstract(ContextParameters)


def test_contextparameters_constructor_exists():
    assert callable(ContextParameters.__init__)


def test_contextparameters_constructor_args():
    sig = inspect.signature(ContextParameters.__init__)
    params = list(sig.parameters.keys())



def test_domain_trigger_is_not_abstract():
    assert not inspect.isabstract(domain_Trigger)


def test_domain_trigger_constructor_exists():
    assert callable(domain_Trigger.__init__)


def test_domain_trigger_constructor_args():
    sig = inspect.signature(domain_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_contextvalue_is_not_abstract():
    assert not inspect.isabstract(ContextValue)


def test_contextvalue_constructor_exists():
    assert callable(ContextValue.__init__)


def test_contextvalue_constructor_args():
    sig = inspect.signature(ContextValue.__init__)
    params = list(sig.parameters.keys())



def test_domain_styleclass_is_not_abstract():
    assert not inspect.isabstract(domain_StyleClass)


def test_domain_styleclass_constructor_exists():
    assert callable(domain_StyleClass.__init__)


def test_domain_styleclass_constructor_args():
    sig = inspect.signature(domain_StyleClass.__init__)
    params = list(sig.parameters.keys())



def test_domain_contextparameters_is_not_abstract():
    assert not inspect.isabstract(domain_ContextParameters)


def test_domain_contextparameters_constructor_exists():
    assert callable(domain_ContextParameters.__init__)


def test_domain_contextparameters_constructor_args():
    sig = inspect.signature(domain_ContextParameters.__init__)
    params = list(sig.parameters.keys())



def test_domain_expressionpart_is_not_abstract():
    assert not inspect.isabstract(domain_ExpressionPart)


def test_domain_expressionpart_constructor_exists():
    assert callable(domain_ExpressionPart.__init__)


def test_domain_expressionpart_constructor_args():
    sig = inspect.signature(domain_ExpressionPart.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "expressionType" in params, "Missing parameter 'expressionType'"

def test_domain_expressionpart_has_order():
    assert hasattr(domain_ExpressionPart, "order")
    descriptor = None
    for klass in domain_ExpressionPart.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_domain_expressionpart_has_uid():
    assert hasattr(domain_ExpressionPart, "uid")
    descriptor = None
    for klass in domain_ExpressionPart.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_expressionpart_has_expressionType():
    assert hasattr(domain_ExpressionPart, "expressionType")
    descriptor = None
    for klass in domain_ExpressionPart.__mro__:
        if "expressionType" in klass.__dict__:
            descriptor = klass.__dict__["expressionType"]
            break
    assert isinstance(descriptor, property)



def test_domain_contextvalue_is_not_abstract():
    assert not inspect.isabstract(domain_ContextValue)


def test_domain_contextvalue_constructor_exists():
    assert callable(domain_ContextValue.__init__)


def test_domain_contextvalue_constructor_args():
    sig = inspect.signature(domain_ContextValue.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "value" in params, "Missing parameter 'value'"

def test_domain_contextvalue_has_constant():
    assert hasattr(domain_ContextValue, "constant")
    descriptor = None
    for klass in domain_ContextValue.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_domain_contextvalue_has_uid():
    assert hasattr(domain_ContextValue, "uid")
    descriptor = None
    for klass in domain_ContextValue.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_contextvalue_has_value():
    assert hasattr(domain_ContextValue, "value")
    descriptor = None
    for klass in domain_ContextValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_domain_contextparameter_is_not_abstract():
    assert not inspect.isabstract(domain_ContextParameter)


def test_domain_contextparameter_constructor_exists():
    assert callable(domain_ContextParameter.__init__)


def test_domain_contextparameter_constructor_args():
    sig = inspect.signature(domain_ContextParameter.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "operation" in params, "Missing parameter 'operation'"

def test_domain_contextparameter_has_uid():
    assert hasattr(domain_ContextParameter, "uid")
    descriptor = None
    for klass in domain_ContextParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_contextparameter_has_operation():
    assert hasattr(domain_ContextParameter, "operation")
    descriptor = None
    for klass in domain_ContextParameter.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_domain_childrenholder_is_not_abstract():
    assert not inspect.isabstract(domain_ChildrenHolder)


def test_domain_childrenholder_constructor_exists():
    assert callable(domain_ChildrenHolder.__init__)


def test_domain_childrenholder_constructor_args():
    sig = inspect.signature(domain_ChildrenHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain_inputelement_is_not_abstract():
    assert not inspect.isabstract(domain_InputElement)


def test_domain_inputelement_constructor_exists():
    assert callable(domain_InputElement.__init__)


def test_domain_inputelement_constructor_args():
    sig = inspect.signature(domain_InputElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_linktomessage_is_not_abstract():
    assert not inspect.isabstract(domain_LinkToMessage)


def test_domain_linktomessage_constructor_exists():
    assert callable(domain_LinkToMessage.__init__)


def test_domain_linktomessage_constructor_args():
    sig = inspect.signature(domain_LinkToMessage.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_linktomessage_has_uid():
    assert hasattr(domain_LinkToMessage, "uid")
    descriptor = None
    for klass in domain_LinkToMessage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_linktolabel_is_not_abstract():
    assert not inspect.isabstract(domain_LinkToLabel)


def test_domain_linktolabel_constructor_exists():
    assert callable(domain_LinkToLabel.__init__)


def test_domain_linktolabel_constructor_args():
    sig = inspect.signature(domain_LinkToLabel.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_linktolabel_has_uid():
    assert hasattr(domain_LinkToLabel, "uid")
    descriptor = None
    for klass in domain_LinkToLabel.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_layerholder_is_not_abstract():
    assert not inspect.isabstract(domain_LayerHolder)


def test_domain_layerholder_constructor_exists():
    assert callable(domain_LayerHolder.__init__)


def test_domain_layerholder_constructor_args():
    sig = inspect.signature(domain_LayerHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain_controls_is_not_abstract():
    assert not inspect.isabstract(domain_Controls)


def test_domain_controls_constructor_exists():
    assert callable(domain_Controls.__init__)


def test_domain_controls_constructor_args():
    sig = inspect.signature(domain_Controls.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_controls_has_uid():
    assert hasattr(domain_Controls, "uid")
    descriptor = None
    for klass in domain_Controls.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_domain_updatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain_UpdateTrigger)


def test_domain_updatetrigger_constructor_exists():
    assert callable(domain_UpdateTrigger.__init__)


def test_domain_updatetrigger_constructor_args():
    sig = inspect.signature(domain_UpdateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_updatetrigger_has_uid():
    assert hasattr(domain_UpdateTrigger, "uid")
    descriptor = None
    for klass in domain_UpdateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_preformtrigger_is_not_abstract():
    assert not inspect.isabstract(domain_PREFormTrigger)


def test_domain_preformtrigger_constructor_exists():
    assert callable(domain_PREFormTrigger.__init__)


def test_domain_preformtrigger_constructor_args():
    sig = inspect.signature(domain_PREFormTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_preformtrigger_has_uid():
    assert hasattr(domain_PREFormTrigger, "uid")
    descriptor = None
    for klass in domain_PREFormTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_inserttrigger_is_not_abstract():
    assert not inspect.isabstract(domain_InsertTrigger)


def test_domain_inserttrigger_constructor_exists():
    assert callable(domain_InsertTrigger.__init__)


def test_domain_inserttrigger_constructor_args():
    sig = inspect.signature(domain_InsertTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_inserttrigger_has_uid():
    assert hasattr(domain_InsertTrigger, "uid")
    descriptor = None
    for klass in domain_InsertTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_postquerytrigger_is_not_abstract():
    assert not inspect.isabstract(domain_POSTQueryTrigger)


def test_domain_postquerytrigger_constructor_exists():
    assert callable(domain_POSTQueryTrigger.__init__)


def test_domain_postquerytrigger_constructor_args():
    sig = inspect.signature(domain_POSTQueryTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_postquerytrigger_has_uid():
    assert hasattr(domain_POSTQueryTrigger, "uid")
    descriptor = None
    for klass in domain_POSTQueryTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_preinserttrigger_is_not_abstract():
    assert not inspect.isabstract(domain_PREInsertTrigger)


def test_domain_preinserttrigger_constructor_exists():
    assert callable(domain_PREInsertTrigger.__init__)


def test_domain_preinserttrigger_constructor_args():
    sig = inspect.signature(domain_PREInsertTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_preinserttrigger_has_uid():
    assert hasattr(domain_PREInsertTrigger, "uid")
    descriptor = None
    for klass in domain_PREInsertTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_prequerytrigger_is_not_abstract():
    assert not inspect.isabstract(domain_PREQueryTrigger)


def test_domain_prequerytrigger_constructor_exists():
    assert callable(domain_PREQueryTrigger.__init__)


def test_domain_prequerytrigger_constructor_args():
    sig = inspect.signature(domain_PREQueryTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_prequerytrigger_has_uid():
    assert hasattr(domain_PREQueryTrigger, "uid")
    descriptor = None
    for klass in domain_PREQueryTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_deletetrigger_is_not_abstract():
    assert not inspect.isabstract(domain_DeleteTrigger)


def test_domain_deletetrigger_constructor_exists():
    assert callable(domain_DeleteTrigger.__init__)


def test_domain_deletetrigger_constructor_args():
    sig = inspect.signature(domain_DeleteTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_deletetrigger_has_uid():
    assert hasattr(domain_DeleteTrigger, "uid")
    descriptor = None
    for klass in domain_DeleteTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_createtrigger_is_not_abstract():
    assert not inspect.isabstract(domain_CreateTrigger)


def test_domain_createtrigger_constructor_exists():
    assert callable(domain_CreateTrigger.__init__)


def test_domain_createtrigger_constructor_args():
    sig = inspect.signature(domain_CreateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_createtrigger_has_uid():
    assert hasattr(domain_CreateTrigger, "uid")
    descriptor = None
    for klass in domain_CreateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_postcreatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain_POSTCreateTrigger)


def test_domain_postcreatetrigger_constructor_exists():
    assert callable(domain_POSTCreateTrigger.__init__)


def test_domain_postcreatetrigger_constructor_args():
    sig = inspect.signature(domain_POSTCreateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_postcreatetrigger_has_uid():
    assert hasattr(domain_POSTCreateTrigger, "uid")
    descriptor = None
    for klass in domain_POSTCreateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_searchtrigger_is_not_abstract():
    assert not inspect.isabstract(domain_SearchTrigger)


def test_domain_searchtrigger_constructor_exists():
    assert callable(domain_SearchTrigger.__init__)


def test_domain_searchtrigger_constructor_args():
    sig = inspect.signature(domain_SearchTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_searchtrigger_has_uid():
    assert hasattr(domain_SearchTrigger, "uid")
    descriptor = None
    for klass in domain_SearchTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_preupdatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain_PREUpdateTrigger)


def test_domain_preupdatetrigger_constructor_exists():
    assert callable(domain_PREUpdateTrigger.__init__)


def test_domain_preupdatetrigger_constructor_args():
    sig = inspect.signature(domain_PREUpdateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_preupdatetrigger_has_uid():
    assert hasattr(domain_PREUpdateTrigger, "uid")
    descriptor = None
    for klass in domain_PREUpdateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_predeletetrigger_is_not_abstract():
    assert not inspect.isabstract(domain_PREDeleteTrigger)


def test_domain_predeletetrigger_constructor_exists():
    assert callable(domain_PREDeleteTrigger.__init__)


def test_domain_predeletetrigger_constructor_args():
    sig = inspect.signature(domain_PREDeleteTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_predeletetrigger_has_uid():
    assert hasattr(domain_PREDeleteTrigger, "uid")
    descriptor = None
    for klass in domain_PREDeleteTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_canvasview_is_not_abstract():
    assert not inspect.isabstract(domain_CanvasView)


def test_domain_canvasview_constructor_exists():
    assert callable(domain_CanvasView.__init__)


def test_domain_canvasview_constructor_args():
    sig = inspect.signature(domain_CanvasView.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_canvasview_has_uid():
    assert hasattr(domain_CanvasView, "uid")
    descriptor = None
    for klass in domain_CanvasView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_viewporttrigger_is_not_abstract():
    assert not inspect.isabstract(domain_ViewPortTrigger)


def test_domain_viewporttrigger_constructor_exists():
    assert callable(domain_ViewPortTrigger.__init__)


def test_domain_viewporttrigger_constructor_args():
    sig = inspect.signature(domain_ViewPortTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_viewporttrigger_has_uid():
    assert hasattr(domain_ViewPortTrigger, "uid")
    descriptor = None
    for klass in domain_ViewPortTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_viewelement_is_not_abstract():
    assert not inspect.isabstract(ViewElement)


def test_viewelement_constructor_exists():
    assert callable(ViewElement.__init__)


def test_viewelement_constructor_args():
    sig = inspect.signature(ViewElement.__init__)
    params = list(sig.parameters.keys())



def test_orderable_is_not_abstract():
    assert not inspect.isabstract(Orderable)


def test_orderable_constructor_exists():
    assert callable(Orderable.__init__)


def test_orderable_constructor_args():
    sig = inspect.signature(Orderable.__init__)
    params = list(sig.parameters.keys())



def test_domain_viewport_is_not_abstract():
    assert not inspect.isabstract(domain_ViewPort)


def test_domain_viewport_constructor_exists():
    assert callable(domain_ViewPort.__init__)


def test_domain_viewport_constructor_args():
    sig = inspect.signature(domain_ViewPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_viewport_has_name():
    assert hasattr(domain_ViewPort, "name")
    descriptor = None
    for klass in domain_ViewPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_viewport_has_uid():
    assert hasattr(domain_ViewPort, "uid")
    descriptor = None
    for klass in domain_ViewPort.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_viewarea_is_not_abstract():
    assert not inspect.isabstract(domain_ViewArea)


def test_domain_viewarea_constructor_exists():
    assert callable(domain_ViewArea.__init__)


def test_domain_viewarea_constructor_args():
    sig = inspect.signature(domain_ViewArea.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_viewarea_has_name():
    assert hasattr(domain_ViewArea, "name")
    descriptor = None
    for klass in domain_ViewArea.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_viewarea_has_uid():
    assert hasattr(domain_ViewArea, "uid")
    descriptor = None
    for klass in domain_ViewArea.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_menuview_is_not_abstract():
    assert not inspect.isabstract(domain_MenuView)


def test_domain_menuview_constructor_exists():
    assert callable(domain_MenuView.__init__)


def test_domain_menuview_constructor_args():
    sig = inspect.signature(domain_MenuView.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_menuview_has_uid():
    assert hasattr(domain_MenuView, "uid")
    descriptor = None
    for klass in domain_MenuView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_flexfields_is_not_abstract():
    assert not inspect.isabstract(FlexFields)


def test_flexfields_constructor_exists():
    assert callable(FlexFields.__init__)


def test_flexfields_constructor_args():
    sig = inspect.signature(FlexFields.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuitem_is_not_abstract():
    assert not inspect.isabstract(domain_MenuItem)


def test_domain_menuitem_constructor_exists():
    assert callable(domain_MenuItem.__init__)


def test_domain_menuitem_constructor_args():
    sig = inspect.signature(domain_MenuItem.__init__)
    params = list(sig.parameters.keys())



def test_multilanglabel_is_not_abstract():
    assert not inspect.isabstract(MultiLangLabel)


def test_multilanglabel_constructor_exists():
    assert callable(MultiLangLabel.__init__)


def test_multilanglabel_constructor_args():
    sig = inspect.signature(MultiLangLabel.__init__)
    params = list(sig.parameters.keys())



def test_domain_tree_is_not_abstract():
    assert not inspect.isabstract(domain_Tree)


def test_domain_tree_constructor_exists():
    assert callable(domain_Tree.__init__)


def test_domain_tree_constructor_args():
    sig = inspect.signature(domain_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain_tree_has_label():
    assert hasattr(domain_Tree, "label")
    descriptor = None
    for klass in domain_Tree.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain_messageelement_is_not_abstract():
    assert not inspect.isabstract(domain_MessageElement)


def test_domain_messageelement_constructor_exists():
    assert callable(domain_MessageElement.__init__)


def test_domain_messageelement_constructor_args():
    sig = inspect.signature(domain_MessageElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain_messageelement_has_label():
    assert hasattr(domain_MessageElement, "label")
    descriptor = None
    for klass in domain_MessageElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain_table_is_not_abstract():
    assert not inspect.isabstract(domain_Table)


def test_domain_table_constructor_exists():
    assert callable(domain_Table.__init__)


def test_domain_table_constructor_args():
    sig = inspect.signature(domain_Table.__init__)
    params = list(sig.parameters.keys())
    assert "rowNumber" in params, "Missing parameter 'rowNumber'"
    assert "label" in params, "Missing parameter 'label'"

def test_domain_table_has_rowNumber():
    assert hasattr(domain_Table, "rowNumber")
    descriptor = None
    for klass in domain_Table.__mro__:
        if "rowNumber" in klass.__dict__:
            descriptor = klass.__dict__["rowNumber"]
            break
    assert isinstance(descriptor, property)

def test_domain_table_has_label():
    assert hasattr(domain_Table, "label")
    descriptor = None
    for klass in domain_Table.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain_button_is_not_abstract():
    assert not inspect.isabstract(domain_Button)


def test_domain_button_constructor_exists():
    assert callable(domain_Button.__init__)


def test_domain_button_constructor_args():
    sig = inspect.signature(domain_Button.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain_button_has_label():
    assert hasattr(domain_Button, "label")
    descriptor = None
    for klass in domain_Button.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain_label_is_not_abstract():
    assert not inspect.isabstract(domain_Label)


def test_domain_label_constructor_exists():
    assert callable(domain_Label.__init__)


def test_domain_label_constructor_args():
    sig = inspect.signature(domain_Label.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain_label_has_label():
    assert hasattr(domain_Label, "label")
    descriptor = None
    for klass in domain_Label.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_defaultcavas_is_not_abstract():
    assert not inspect.isabstract(DefaultCavas)


def test_defaultcavas_constructor_exists():
    assert callable(DefaultCavas.__init__)


def test_defaultcavas_constructor_args():
    sig = inspect.signature(DefaultCavas.__init__)
    params = list(sig.parameters.keys())



def test_viewportholder_is_not_abstract():
    assert not inspect.isabstract(ViewPortHolder)


def test_viewportholder_constructor_exists():
    assert callable(ViewPortHolder.__init__)


def test_viewportholder_constructor_args():
    sig = inspect.signature(ViewPortHolder.__init__)
    params = list(sig.parameters.keys())



def test_canvasframe_is_not_abstract():
    assert not inspect.isabstract(CanvasFrame)


def test_canvasframe_constructor_exists():
    assert callable(CanvasFrame.__init__)


def test_canvasframe_constructor_args():
    sig = inspect.signature(CanvasFrame.__init__)
    params = list(sig.parameters.keys())



def test_domain_canvas_is_not_abstract():
    assert not inspect.isabstract(domain_Canvas)


def test_domain_canvas_constructor_exists():
    assert callable(domain_Canvas.__init__)


def test_domain_canvas_constructor_args():
    sig = inspect.signature(domain_Canvas.__init__)
    params = list(sig.parameters.keys())



def test_domain_tabpage_is_not_abstract():
    assert not inspect.isabstract(domain_TabPage)


def test_domain_tabpage_constructor_exists():
    assert callable(domain_TabPage.__init__)


def test_domain_tabpage_constructor_args():
    sig = inspect.signature(domain_TabPage.__init__)
    params = list(sig.parameters.keys())



def test_domain_tabcanvas_is_not_abstract():
    assert not inspect.isabstract(domain_TabCanvas)


def test_domain_tabcanvas_constructor_exists():
    assert callable(domain_TabCanvas.__init__)


def test_domain_tabcanvas_constructor_args():
    sig = inspect.signature(domain_TabCanvas.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_domain_tabcanvas_has_orientation():
    assert hasattr(domain_TabCanvas, "orientation")
    descriptor = None
    for klass in domain_TabCanvas.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_domain_popupcanvas_is_not_abstract():
    assert not inspect.isabstract(domain_PopupCanvas)


def test_domain_popupcanvas_constructor_exists():
    assert callable(domain_PopupCanvas.__init__)


def test_domain_popupcanvas_constructor_args():
    sig = inspect.signature(domain_PopupCanvas.__init__)
    params = list(sig.parameters.keys())
    assert "modal" in params, "Missing parameter 'modal'"

def test_domain_popupcanvas_has_modal():
    assert hasattr(domain_PopupCanvas, "modal")
    descriptor = None
    for klass in domain_PopupCanvas.__mro__:
        if "modal" in klass.__dict__:
            descriptor = klass.__dict__["modal"]
            break
    assert isinstance(descriptor, property)



def test_nicknamed_is_not_abstract():
    assert not inspect.isabstract(NickNamed)


def test_nicknamed_constructor_exists():
    assert callable(NickNamed.__init__)


def test_nicknamed_constructor_args():
    sig = inspect.signature(NickNamed.__init__)
    params = list(sig.parameters.keys())



def test_domain_defaultcavas_is_not_abstract():
    assert not inspect.isabstract(domain_DefaultCavas)


def test_domain_defaultcavas_constructor_exists():
    assert callable(domain_DefaultCavas.__init__)


def test_domain_defaultcavas_constructor_args():
    sig = inspect.signature(domain_DefaultCavas.__init__)
    params = list(sig.parameters.keys())
    assert "defaultCanvas" in params, "Missing parameter 'defaultCanvas'"

def test_domain_defaultcavas_has_defaultCanvas():
    assert hasattr(domain_DefaultCavas, "defaultCanvas")
    descriptor = None
    for klass in domain_DefaultCavas.__mro__:
        if "defaultCanvas" in klass.__dict__:
            descriptor = klass.__dict__["defaultCanvas"]
            break
    assert isinstance(descriptor, property)



def test_domain_viewportholder_is_not_abstract():
    assert not inspect.isabstract(domain_ViewPortHolder)


def test_domain_viewportholder_constructor_exists():
    assert callable(domain_ViewPortHolder.__init__)


def test_domain_viewportholder_constructor_args():
    sig = inspect.signature(domain_ViewPortHolder.__init__)
    params = list(sig.parameters.keys())



def test_styleelement_is_not_abstract():
    assert not inspect.isabstract(StyleElement)


def test_styleelement_constructor_exists():
    assert callable(StyleElement.__init__)


def test_styleelement_constructor_args():
    sig = inspect.signature(StyleElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_uielement_is_not_abstract():
    assert not inspect.isabstract(domain_Uielement)


def test_domain_uielement_constructor_exists():
    assert callable(domain_Uielement.__init__)


def test_domain_uielement_constructor_args():
    sig = inspect.signature(domain_Uielement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_uielement_has_uid():
    assert hasattr(domain_Uielement, "uid")
    descriptor = None
    for klass in domain_Uielement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_selection_is_not_abstract():
    assert not inspect.isabstract(domain_Selection)


def test_domain_selection_constructor_exists():
    assert callable(domain_Selection.__init__)


def test_domain_selection_constructor_args():
    sig = inspect.signature(domain_Selection.__init__)
    params = list(sig.parameters.keys())



def test_domain_column_is_not_abstract():
    assert not inspect.isabstract(domain_Column)


def test_domain_column_constructor_exists():
    assert callable(domain_Column.__init__)


def test_domain_column_constructor_args():
    sig = inspect.signature(domain_Column.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_column_has_label():
    assert hasattr(domain_Column, "label")
    descriptor = None
    for klass in domain_Column.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_domain_column_has_uid():
    assert hasattr(domain_Column, "uid")
    descriptor = None
    for klass in domain_Column.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_menufolder_is_not_abstract():
    assert not inspect.isabstract(domain_MenuFolder)


def test_domain_menufolder_constructor_exists():
    assert callable(domain_MenuFolder.__init__)


def test_domain_menufolder_constructor_args():
    sig = inspect.signature(domain_MenuFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "extensionPoint" in params, "Missing parameter 'extensionPoint'"

def test_domain_menufolder_has_name():
    assert hasattr(domain_MenuFolder, "name")
    descriptor = None
    for klass in domain_MenuFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_menufolder_has_uid():
    assert hasattr(domain_MenuFolder, "uid")
    descriptor = None
    for klass in domain_MenuFolder.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_menufolder_has_extensionPoint():
    assert hasattr(domain_MenuFolder, "extensionPoint")
    descriptor = None
    for klass in domain_MenuFolder.__mro__:
        if "extensionPoint" in klass.__dict__:
            descriptor = klass.__dict__["extensionPoint"]
            break
    assert isinstance(descriptor, property)



def test_domain_viewelement_is_not_abstract():
    assert not inspect.isabstract(domain_ViewElement)


def test_domain_viewelement_constructor_exists():
    assert callable(domain_ViewElement.__init__)


def test_domain_viewelement_constructor_args():
    sig = inspect.signature(domain_ViewElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_menuelement_is_not_abstract():
    assert not inspect.isabstract(domain_MenuElement)


def test_domain_menuelement_constructor_exists():
    assert callable(domain_MenuElement.__init__)


def test_domain_menuelement_constructor_args():
    sig = inspect.signature(domain_MenuElement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_menuelement_has_uid():
    assert hasattr(domain_MenuElement, "uid")
    descriptor = None
    for klass in domain_MenuElement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_menuelement_has_name():
    assert hasattr(domain_MenuElement, "name")
    descriptor = None
    for klass in domain_MenuElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_context_is_not_abstract():
    assert not inspect.isabstract(domain_Context)


def test_domain_context_constructor_exists():
    assert callable(domain_Context.__init__)


def test_domain_context_constructor_args():
    sig = inspect.signature(domain_Context.__init__)
    params = list(sig.parameters.keys())



def test_domain_multilanglabel_is_not_abstract():
    assert not inspect.isabstract(domain_MultiLangLabel)


def test_domain_multilanglabel_constructor_exists():
    assert callable(domain_MultiLangLabel.__init__)


def test_domain_multilanglabel_constructor_args():
    sig = inspect.signature(domain_MultiLangLabel.__init__)
    params = list(sig.parameters.keys())



def test_domain_orderable_is_not_abstract():
    assert not inspect.isabstract(domain_Orderable)


def test_domain_orderable_constructor_exists():
    assert callable(domain_Orderable.__init__)


def test_domain_orderable_constructor_args():
    sig = inspect.signature(domain_Orderable.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_domain_orderable_has_order():
    assert hasattr(domain_Orderable, "order")
    descriptor = None
    for klass in domain_Orderable.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_domain_menudefinition_is_not_abstract():
    assert not inspect.isabstract(domain_MenuDefinition)


def test_domain_menudefinition_constructor_exists():
    assert callable(domain_MenuDefinition.__init__)


def test_domain_menudefinition_constructor_args():
    sig = inspect.signature(domain_MenuDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_menudefinition_has_name():
    assert hasattr(domain_MenuDefinition, "name")
    descriptor = None
    for klass in domain_MenuDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_menudefinition_has_uid():
    assert hasattr(domain_MenuDefinition, "uid")
    descriptor = None
    for klass in domain_MenuDefinition.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_tabpagesinheritance_is_not_abstract():
    assert not inspect.isabstract(domain_TabPagesInheritance)


def test_domain_tabpagesinheritance_constructor_exists():
    assert callable(domain_TabPagesInheritance.__init__)


def test_domain_tabpagesinheritance_constructor_args():
    sig = inspect.signature(domain_TabPagesInheritance.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_tabpagesinheritance_has_uid():
    assert hasattr(domain_TabPagesInheritance, "uid")
    descriptor = None
    for klass in domain_TabPagesInheritance.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_viewinheritance_is_not_abstract():
    assert not inspect.isabstract(domain_ViewInheritance)


def test_domain_viewinheritance_constructor_exists():
    assert callable(domain_ViewInheritance.__init__)


def test_domain_viewinheritance_constructor_args():
    sig = inspect.signature(domain_ViewInheritance.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_viewinheritance_has_uid():
    assert hasattr(domain_ViewInheritance, "uid")
    descriptor = None
    for klass in domain_ViewInheritance.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_canvasframe_is_not_abstract():
    assert not inspect.isabstract(domain_CanvasFrame)


def test_domain_canvasframe_constructor_exists():
    assert callable(domain_CanvasFrame.__init__)


def test_domain_canvasframe_constructor_args():
    sig = inspect.signature(domain_CanvasFrame.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_canvasframe_has_name():
    assert hasattr(domain_CanvasFrame, "name")
    descriptor = None
    for klass in domain_CanvasFrame.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_canvasframe_has_uid():
    assert hasattr(domain_CanvasFrame, "uid")
    descriptor = None
    for klass in domain_CanvasFrame.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_views_is_not_abstract():
    assert not inspect.isabstract(domain_Views)


def test_domain_views_constructor_exists():
    assert callable(domain_Views.__init__)


def test_domain_views_constructor_args():
    sig = inspect.signature(domain_Views.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_views_has_uid():
    assert hasattr(domain_Views, "uid")
    descriptor = None
    for klass in domain_Views.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_formparameter_is_not_abstract():
    assert not inspect.isabstract(domain_FormParameter)


def test_domain_formparameter_constructor_exists():
    assert callable(domain_FormParameter.__init__)


def test_domain_formparameter_constructor_args():
    sig = inspect.signature(domain_FormParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_formparameter_has_name():
    assert hasattr(domain_FormParameter, "name")
    descriptor = None
    for klass in domain_FormParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_formparameter_has_uid():
    assert hasattr(domain_FormParameter, "uid")
    descriptor = None
    for klass in domain_FormParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_formdatacontrols_is_not_abstract():
    assert not inspect.isabstract(domain_FormDataControls)


def test_domain_formdatacontrols_constructor_exists():
    assert callable(domain_FormDataControls.__init__)


def test_domain_formdatacontrols_constructor_args():
    sig = inspect.signature(domain_FormDataControls.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_formdatacontrols_has_uid():
    assert hasattr(domain_FormDataControls, "uid")
    descriptor = None
    for klass in domain_FormDataControls.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_formdatacontrols_has_name():
    assert hasattr(domain_FormDataControls, "name")
    descriptor = None
    for klass in domain_FormDataControls.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_formview_is_not_abstract():
    assert not inspect.isabstract(domain_FormView)


def test_domain_formview_constructor_exists():
    assert callable(domain_FormView.__init__)


def test_domain_formview_constructor_args():
    sig = inspect.signature(domain_FormView.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_formview_has_uid():
    assert hasattr(domain_FormView, "uid")
    descriptor = None
    for klass in domain_FormView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_formview_has_name():
    assert hasattr(domain_FormView, "name")
    descriptor = None
    for klass in domain_FormView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_form_is_not_abstract():
    assert not inspect.isabstract(domain_Form)


def test_domain_form_constructor_exists():
    assert callable(domain_Form.__init__)


def test_domain_form_constructor_args():
    sig = inspect.signature(domain_Form.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_form_has_uid():
    assert hasattr(domain_Form, "uid")
    descriptor = None
    for klass in domain_Form.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_form_has_name():
    assert hasattr(domain_Form, "name")
    descriptor = None
    for klass in domain_Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_types_is_not_abstract():
    assert not inspect.isabstract(domain_Types)


def test_domain_types_constructor_exists():
    assert callable(domain_Types.__init__)


def test_domain_types_constructor_args():
    sig = inspect.signature(domain_Types.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_types_has_name():
    assert hasattr(domain_Types, "name")
    descriptor = None
    for klass in domain_Types.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_types_has_uid():
    assert hasattr(domain_Types, "uid")
    descriptor = None
    for klass in domain_Types.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_enumattribute_is_not_abstract():
    assert not inspect.isabstract(domain_EnumAttribute)


def test_domain_enumattribute_constructor_exists():
    assert callable(domain_EnumAttribute.__init__)


def test_domain_enumattribute_constructor_args():
    sig = inspect.signature(domain_EnumAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_enumattribute_has_uid():
    assert hasattr(domain_EnumAttribute, "uid")
    descriptor = None
    for klass in domain_EnumAttribute.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_enumattribute_has_value():
    assert hasattr(domain_EnumAttribute, "value")
    descriptor = None
    for klass in domain_EnumAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain_enumattribute_has_name():
    assert hasattr(domain_EnumAttribute, "name")
    descriptor = None
    for klass in domain_EnumAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_returnvalue_is_not_abstract():
    assert not inspect.isabstract(domain_ReturnValue)


def test_domain_returnvalue_constructor_exists():
    assert callable(domain_ReturnValue.__init__)


def test_domain_returnvalue_constructor_args():
    sig = inspect.signature(domain_ReturnValue.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_returnvalue_has_uid():
    assert hasattr(domain_ReturnValue, "uid")
    descriptor = None
    for klass in domain_ReturnValue.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_parameter_is_not_abstract():
    assert not inspect.isabstract(domain_Parameter)


def test_domain_parameter_constructor_exists():
    assert callable(domain_Parameter.__init__)


def test_domain_parameter_constructor_args():
    sig = inspect.signature(domain_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "order" in params, "Missing parameter 'order'"

def test_domain_parameter_has_uid():
    assert hasattr(domain_Parameter, "uid")
    descriptor = None
    for klass in domain_Parameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_parameter_has_name():
    assert hasattr(domain_Parameter, "name")
    descriptor = None
    for klass in domain_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_parameter_has_order():
    assert hasattr(domain_Parameter, "order")
    descriptor = None
    for klass in domain_Parameter.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_secured_is_not_abstract():
    assert not inspect.isabstract(Secured)


def test_secured_constructor_exists():
    assert callable(Secured.__init__)


def test_secured_constructor_args():
    sig = inspect.signature(Secured.__init__)
    params = list(sig.parameters.keys())



def test_domain_window_is_not_abstract():
    assert not inspect.isabstract(domain_Window)


def test_domain_window_constructor_exists():
    assert callable(domain_Window.__init__)


def test_domain_window_constructor_args():
    sig = inspect.signature(domain_Window.__init__)
    params = list(sig.parameters.keys())



def test_domain_operation_is_not_abstract():
    assert not inspect.isabstract(domain_Operation)


def test_domain_operation_constructor_exists():
    assert callable(domain_Operation.__init__)


def test_domain_operation_constructor_args():
    sig = inspect.signature(domain_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_operation_has_name():
    assert hasattr(domain_Operation, "name")
    descriptor = None
    for klass in domain_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_operation_has_uid():
    assert hasattr(domain_Operation, "uid")
    descriptor = None
    for klass in domain_Operation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_typeelement_is_not_abstract():
    assert not inspect.isabstract(TypeElement)


def test_typeelement_constructor_exists():
    assert callable(TypeElement.__init__)


def test_typeelement_constructor_args():
    sig = inspect.signature(TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_domain_type_is_not_abstract():
    assert not inspect.isabstract(domain_Type)


def test_domain_type_constructor_exists():
    assert callable(domain_Type.__init__)


def test_domain_type_constructor_args():
    sig = inspect.signature(domain_Type.__init__)
    params = list(sig.parameters.keys())



def test_domain_typereference_is_not_abstract():
    assert not inspect.isabstract(domain_TypeReference)


def test_domain_typereference_constructor_exists():
    assert callable(domain_TypeReference.__init__)


def test_domain_typereference_constructor_args():
    sig = inspect.signature(domain_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_domain_enumarator_is_not_abstract():
    assert not inspect.isabstract(domain_Enumarator)


def test_domain_enumarator_constructor_exists():
    assert callable(domain_Enumarator.__init__)


def test_domain_enumarator_constructor_args():
    sig = inspect.signature(domain_Enumarator.__init__)
    params = list(sig.parameters.keys())



def test_domain_primitive_is_not_abstract():
    assert not inspect.isabstract(domain_Primitive)


def test_domain_primitive_constructor_exists():
    assert callable(domain_Primitive.__init__)


def test_domain_primitive_constructor_args():
    sig = inspect.signature(domain_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_domain_attribute_is_not_abstract():
    assert not inspect.isabstract(domain_Attribute)


def test_domain_attribute_constructor_exists():
    assert callable(domain_Attribute.__init__)


def test_domain_attribute_constructor_args():
    sig = inspect.signature(domain_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "pk" in params, "Missing parameter 'pk'"

def test_domain_attribute_has_name():
    assert hasattr(domain_Attribute, "name")
    descriptor = None
    for klass in domain_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_attribute_has_uid():
    assert hasattr(domain_Attribute, "uid")
    descriptor = None
    for klass in domain_Attribute.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_attribute_has_pk():
    assert hasattr(domain_Attribute, "pk")
    descriptor = None
    for klass in domain_Attribute.__mro__:
        if "pk" in klass.__dict__:
            descriptor = klass.__dict__["pk"]
            break
    assert isinstance(descriptor, property)



def test_domain_link_is_not_abstract():
    assert not inspect.isabstract(domain_Link)


def test_domain_link_constructor_exists():
    assert callable(domain_Link.__init__)


def test_domain_link_constructor_args():
    sig = inspect.signature(domain_Link.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_link_has_uid():
    assert hasattr(domain_Link, "uid")
    descriptor = None
    for klass in domain_Link.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(RelationShip)


def test_relationship_constructor_exists():
    assert callable(RelationShip.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(RelationShip.__init__)
    params = list(sig.parameters.keys())



def test_domain_generalization_is_not_abstract():
    assert not inspect.isabstract(domain_Generalization)


def test_domain_generalization_constructor_exists():
    assert callable(domain_Generalization.__init__)


def test_domain_generalization_constructor_args():
    sig = inspect.signature(domain_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_domain_assosiation_is_not_abstract():
    assert not inspect.isabstract(domain_Assosiation)


def test_domain_assosiation_constructor_exists():
    assert callable(domain_Assosiation.__init__)


def test_domain_assosiation_constructor_args():
    sig = inspect.signature(domain_Assosiation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_domain_assosiation_has_type():
    assert hasattr(domain_Assosiation, "type")
    descriptor = None
    for klass in domain_Assosiation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_domain_references_is_not_abstract():
    assert not inspect.isabstract(domain_References)


def test_domain_references_constructor_exists():
    assert callable(domain_References.__init__)


def test_domain_references_constructor_args():
    sig = inspect.signature(domain_References.__init__)
    params = list(sig.parameters.keys())



def test_domain_relationship_is_not_abstract():
    assert not inspect.isabstract(domain_RelationShip)


def test_domain_relationship_constructor_exists():
    assert callable(domain_RelationShip.__init__)


def test_domain_relationship_constructor_args():
    sig = inspect.signature(domain_RelationShip.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_relationship_has_uid():
    assert hasattr(domain_RelationShip, "uid")
    descriptor = None
    for klass in domain_RelationShip.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_typeelement_is_not_abstract():
    assert not inspect.isabstract(domain_TypeElement)


def test_domain_typeelement_constructor_exists():
    assert callable(domain_TypeElement.__init__)


def test_domain_typeelement_constructor_args():
    sig = inspect.signature(domain_TypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_typeelement_has_name():
    assert hasattr(domain_TypeElement, "name")
    descriptor = None
    for klass in domain_TypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_typeelement_has_uid():
    assert hasattr(domain_TypeElement, "uid")
    descriptor = None
    for klass in domain_TypeElement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_package_is_not_abstract():
    assert not inspect.isabstract(domain_Package)


def test_domain_package_constructor_exists():
    assert callable(domain_Package.__init__)


def test_domain_package_constructor_args():
    sig = inspect.signature(domain_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_package_has_uid():
    assert hasattr(domain_Package, "uid")
    descriptor = None
    for klass in domain_Package.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_package_has_name():
    assert hasattr(domain_Package, "name")
    descriptor = None
    for klass in domain_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_typepointer_is_not_abstract():
    assert not inspect.isabstract(domain_TypePointer)


def test_domain_typepointer_constructor_exists():
    assert callable(domain_TypePointer.__init__)


def test_domain_typepointer_constructor_args():
    sig = inspect.signature(domain_TypePointer.__init__)
    params = list(sig.parameters.keys())
    assert "fakeTypeName" in params, "Missing parameter 'fakeTypeName'"
    assert "fakePackageName" in params, "Missing parameter 'fakePackageName'"

def test_domain_typepointer_has_fakeTypeName():
    assert hasattr(domain_TypePointer, "fakeTypeName")
    descriptor = None
    for klass in domain_TypePointer.__mro__:
        if "fakeTypeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeTypeName"]
            break
    assert isinstance(descriptor, property)

def test_domain_typepointer_has_fakePackageName():
    assert hasattr(domain_TypePointer, "fakePackageName")
    descriptor = None
    for klass in domain_TypePointer.__mro__:
        if "fakePackageName" in klass.__dict__:
            descriptor = klass.__dict__["fakePackageName"]
            break
    assert isinstance(descriptor, property)



def test_domain_artifactref_is_not_abstract():
    assert not inspect.isabstract(domain_ArtifactRef)


def test_domain_artifactref_constructor_exists():
    assert callable(domain_ArtifactRef.__init__)


def test_domain_artifactref_constructor_args():
    sig = inspect.signature(domain_ArtifactRef.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_artifactref_has_uid():
    assert hasattr(domain_ArtifactRef, "uid")
    descriptor = None
    for klass in domain_ArtifactRef.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_queryvariable_is_not_abstract():
    assert not inspect.isabstract(domain_QueryVariable)


def test_domain_queryvariable_constructor_exists():
    assert callable(domain_QueryVariable.__init__)


def test_domain_queryvariable_constructor_args():
    sig = inspect.signature(domain_QueryVariable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_queryvariable_has_value():
    assert hasattr(domain_QueryVariable, "value")
    descriptor = None
    for klass in domain_QueryVariable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain_queryvariable_has_uid():
    assert hasattr(domain_QueryVariable, "uid")
    descriptor = None
    for klass in domain_QueryVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(domain_KeyValuePair)


def test_domain_keyvaluepair_constructor_exists():
    assert callable(domain_KeyValuePair.__init__)


def test_domain_keyvaluepair_constructor_args():
    sig = inspect.signature(domain_KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_keyvaluepair_has_key():
    assert hasattr(domain_KeyValuePair, "key")
    descriptor = None
    for klass in domain_KeyValuePair.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_domain_keyvaluepair_has_value():
    assert hasattr(domain_KeyValuePair, "value")
    descriptor = None
    for klass in domain_KeyValuePair.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain_keyvaluepair_has_uid():
    assert hasattr(domain_KeyValuePair, "uid")
    descriptor = None
    for klass in domain_KeyValuePair.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_typedefinition_is_not_abstract():
    assert not inspect.isabstract(domain_TypeDefinition)


def test_domain_typedefinition_constructor_exists():
    assert callable(domain_TypeDefinition.__init__)


def test_domain_typedefinition_constructor_args():
    sig = inspect.signature(domain_TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_typedefinition_has_uid():
    assert hasattr(domain_TypeDefinition, "uid")
    descriptor = None
    for klass in domain_TypeDefinition.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_query_is_not_abstract():
    assert not inspect.isabstract(domain_Query)


def test_domain_query_constructor_exists():
    assert callable(domain_Query.__init__)


def test_domain_query_constructor_args():
    sig = inspect.signature(domain_Query.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain_query_has_uid():
    assert hasattr(domain_Query, "uid")
    descriptor = None
    for klass in domain_Query.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_query_has_name():
    assert hasattr(domain_Query, "name")
    descriptor = None
    for klass in domain_Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_mappingspecifier_is_not_abstract():
    assert not inspect.isabstract(domain_MappingSpecifier)


def test_domain_mappingspecifier_constructor_exists():
    assert callable(domain_MappingSpecifier.__init__)


def test_domain_mappingspecifier_constructor_args():
    sig = inspect.signature(domain_MappingSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_mappingspecifier_has_uid():
    assert hasattr(domain_MappingSpecifier, "uid")
    descriptor = None
    for klass in domain_MappingSpecifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_artifactref_is_not_abstract():
    assert not inspect.isabstract(ArtifactRef)


def test_artifactref_constructor_exists():
    assert callable(ArtifactRef.__init__)


def test_artifactref_constructor_args():
    sig = inspect.signature(ArtifactRef.__init__)
    params = list(sig.parameters.keys())



def test_domain_modelmapper_is_not_abstract():
    assert not inspect.isabstract(domain_ModelMapper)


def test_domain_modelmapper_constructor_exists():
    assert callable(domain_ModelMapper.__init__)


def test_domain_modelmapper_constructor_args():
    sig = inspect.signature(domain_ModelMapper.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "artifactRoot" in params, "Missing parameter 'artifactRoot'"
    assert "artifactExecutionString" in params, "Missing parameter 'artifactExecutionString'"

def test_domain_modelmapper_has_name():
    assert hasattr(domain_ModelMapper, "name")
    descriptor = None
    for klass in domain_ModelMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain_modelmapper_has_artifactRoot():
    assert hasattr(domain_ModelMapper, "artifactRoot")
    descriptor = None
    for klass in domain_ModelMapper.__mro__:
        if "artifactRoot" in klass.__dict__:
            descriptor = klass.__dict__["artifactRoot"]
            break
    assert isinstance(descriptor, property)

def test_domain_modelmapper_has_artifactExecutionString():
    assert hasattr(domain_ModelMapper, "artifactExecutionString")
    descriptor = None
    for klass in domain_ModelMapper.__mro__:
        if "artifactExecutionString" in klass.__dict__:
            descriptor = klass.__dict__["artifactExecutionString"]
            break
    assert isinstance(descriptor, property)



def test_domain_hashproperty_is_not_abstract():
    assert not inspect.isabstract(domain_HashProperty)


def test_domain_hashproperty_constructor_exists():
    assert callable(domain_HashProperty.__init__)


def test_domain_hashproperty_constructor_args():
    sig = inspect.signature(domain_HashProperty.__init__)
    params = list(sig.parameters.keys())
    assert "fakeName" in params, "Missing parameter 'fakeName'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain_hashproperty_has_fakeName():
    assert hasattr(domain_HashProperty, "fakeName")
    descriptor = None
    for klass in domain_HashProperty.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)

def test_domain_hashproperty_has_uid():
    assert hasattr(domain_HashProperty, "uid")
    descriptor = None
    for klass in domain_HashProperty.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain_property_is_not_abstract():
    assert not inspect.isabstract(domain_Property)


def test_domain_property_constructor_exists():
    assert callable(domain_Property.__init__)


def test_domain_property_constructor_args():
    sig = inspect.signature(domain_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "fakeName" in params, "Missing parameter 'fakeName'"

def test_domain_property_has_value():
    assert hasattr(domain_Property, "value")
    descriptor = None
    for klass in domain_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain_property_has_uid():
    assert hasattr(domain_Property, "uid")
    descriptor = None
    for klass in domain_Property.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain_property_has_fakeName():
    assert hasattr(domain_Property, "fakeName")
    descriptor = None
    for klass in domain_Property.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_domain_javacomponent_is_not_abstract():
    assert not inspect.isabstract(domain_JavaComponent)


def test_domain_javacomponent_constructor_exists():
    assert callable(domain_JavaComponent.__init__)


def test_domain_javacomponent_constructor_args():
    sig = inspect.signature(domain_JavaComponent.__init__)
    params = list(sig.parameters.keys())
    assert "basePackage" in params, "Missing parameter 'basePackage'"
    assert "version" in params, "Missing parameter 'version'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"

def test_domain_javacomponent_has_basePackage():
    assert hasattr(domain_JavaComponent, "basePackage")
    descriptor = None
    for klass in domain_JavaComponent.__mro__:
        if "basePackage" in klass.__dict__:
            descriptor = klass.__dict__["basePackage"]
            break
    assert isinstance(descriptor, property)

def test_domain_javacomponent_has_version():
    assert hasattr(domain_JavaComponent, "version")
    descriptor = None
    for klass in domain_JavaComponent.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_domain_javacomponent_has_groupId():
    assert hasattr(domain_JavaComponent, "groupId")
    descriptor = None
    for klass in domain_JavaComponent.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_domain_javacomponent_has_artifactId():
    assert hasattr(domain_JavaComponent, "artifactId")
    descriptor = None
    for klass in domain_JavaComponent.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_platformlayers_exists():
    # Check that the Enumeration exists
    assert PlatformLayers is not None

def test_platformlayers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PlatformLayers]
    expected_literals = [
        "UILayer",
        "ServiceLayer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PlatformLayers"

def test_order_exists():
    # Check that the Enumeration exists
    assert Order is not None

def test_order_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Order]
    expected_literals = [
        "ASC",
        "DESC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Order"

def test_relationtype_exists():
    # Check that the Enumeration exists
    assert RelationType is not None

def test_relationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationType]
    expected_literals = [
        "One2Many",
        "Many2Many",
        "One2One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationType"

def test_comparator_exists():
    # Check that the Enumeration exists
    assert Comparator is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Comparator]
    expected_literals = [
        "EQ",
        "GT",
        "GEQ",
        "NEQ",
        "LT",
        "LEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Comparator"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "Left",
        "Right",
        "Bottom",
        "Top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"


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
UsingMappers_strategy = st.builds(
    UsingMappers,
)
domain_DeploymentStarStep_strategy = st.builds(
    domain_DeploymentStarStep,
    uid=
        safe_text,
    name=
        safe_text
)
domain_DeploymentComponent_strategy = st.builds(
    domain_DeploymentComponent,
    uid=
        safe_text,
    name=
        safe_text
)
domain_DeploymentComponents_strategy = st.builds(
    domain_DeploymentComponents,
    uid=
        safe_text
)
domain_ConfigExtension_strategy = st.builds(
    domain_ConfigExtension,
    uid=
        safe_text
)
domain_DeploymentSequence_strategy = st.builds(
    domain_DeploymentSequence,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Infrastructure_strategy = st.builds(
    domain_Infrastructure,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Configuration_strategy = st.builds(
    domain_Configuration,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Recipe_strategy = st.builds(
    domain_Recipe,
    uid=
        safe_text,
    name=
        safe_text
)
domain_UsingMappers_strategy = st.builds(
    domain_UsingMappers,
)
TypeMapper_strategy = st.builds(
    TypeMapper,
)
domain_JavaScriptMapper_strategy = st.builds(
    domain_JavaScriptMapper,
    libraryUrl=
        safe_text
)
domain_JavaMapper_strategy = st.builds(
    domain_JavaMapper,
    version=
        safe_text,
    artifactType=
        safe_text,
    mappedToClassName=
        safe_text,
    groupId=
        safe_text,
    libraryName=
        safe_text,
    artifactId=
        safe_text,
    mappedToPackageName=
        safe_text
)
Mapper_strategy = st.builds(
    Mapper,
)
domain_CSSMapper_strategy = st.builds(
    domain_CSSMapper,
    libraryUrl=
        safe_text,
    fakeTypeName=
        safe_text,
    fakePackageName=
        safe_text
)
domain_RoleMapper_strategy = st.builds(
    domain_RoleMapper,
    globalRoleName=
        safe_text,
    localRoleName=
        safe_text,
    fakeRoleName=
        safe_text
)
domain_Mapper_strategy = st.builds(
    domain_Mapper,
    uid=
        safe_text,
    uiLayer=
        st.booleans(),
    serviceLayer=
        st.booleans()
)
domain_StyleLibrary_strategy = st.builds(
    domain_StyleLibrary,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Group_strategy = st.builds(
    domain_Group,
    uid=
        safe_text,
    name=
        safe_text
)
domain_StyleSet_strategy = st.builds(
    domain_StyleSet,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Translation_strategy = st.builds(
    domain_Translation,
    translation=
        safe_text,
    uid=
        safe_text
)
domain_Message_strategy = st.builds(
    domain_Message,
    name=
        safe_text,
    uid=
        safe_text
)
domain_LanguageRef_strategy = st.builds(
    domain_LanguageRef,
    uid=
        safe_text
)
Categorized_strategy = st.builds(
    Categorized,
)
domain_Language_strategy = st.builds(
    domain_Language,
    defaultLang=
        st.booleans(),
    code=
        safe_text,
    uid=
        safe_text,
    lang=
        safe_text
)
domain_MessageLibrary_strategy = st.builds(
    domain_MessageLibrary,
    name=
        safe_text,
    uid=
        safe_text
)
TypePointer_strategy = st.builds(
    TypePointer,
)
domain_TypeMapper_strategy = st.builds(
    domain_TypeMapper,
)
domain_MethodPointer_strategy = st.builds(
    domain_MethodPointer,
    fakeMethod=
        safe_text
)
domain_Mappers_strategy = st.builds(
    domain_Mappers,
    uid=
        safe_text
)
domain_ApplicationMapper_strategy = st.builds(
    domain_ApplicationMapper,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Recipes_strategy = st.builds(
    domain_Recipes,
    uid=
        safe_text
)
domain_ApplicationRecipe_strategy = st.builds(
    domain_ApplicationRecipe,
    name=
        safe_text,
    uid=
        safe_text
)
domain_UIPackage_strategy = st.builds(
    domain_UIPackage,
    uid=
        safe_text
)
domain_ApplicationUIPackage_strategy = st.builds(
    domain_ApplicationUIPackage,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Styles_strategy = st.builds(
    domain_Styles,
    uid=
        safe_text
)
domain_Roles_strategy = st.builds(
    domain_Roles,
    uid=
        safe_text
)
domain_Messages_strategy = st.builds(
    domain_Messages,
    uid=
        safe_text
)
domain_ApplicationMessages_strategy = st.builds(
    domain_ApplicationMessages,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ApplicationRole_strategy = st.builds(
    domain_ApplicationRole,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ApplicationInfrastructureLayer_strategy = st.builds(
    domain_ApplicationInfrastructureLayer,
    uid=
        safe_text,
    name=
        safe_text
)
domain_StylesPackage_strategy = st.builds(
    domain_StylesPackage,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Option_strategy = st.builds(
    domain_Option,
    uid=
        safe_text,
    value=
        safe_text
)
domain_QueryParameter_strategy = st.builds(
    domain_QueryParameter,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Specifier_strategy = st.builds(
    domain_Specifier,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ModelQuery_strategy = st.builds(
    domain_ModelQuery,
    query=
        safe_text,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ConfigHash_strategy = st.builds(
    domain_ConfigHash,
    uid=
        safe_text,
    name=
        safe_text
)
domain_ConfigVariable_strategy = st.builds(
    domain_ConfigVariable,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Artifact_strategy = st.builds(
    domain_Artifact,
    description=
        safe_text,
    template=
        safe_text,
    uid=
        safe_text,
    name=
        safe_text
)
DomainArtifact_strategy = st.builds(
    DomainArtifact,
)
domain_JPAService_strategy = st.builds(
    domain_JPAService,
)
domain_EJBService_strategy = st.builds(
    domain_EJBService,
)
domain_ContinuousIintegration_strategy = st.builds(
    domain_ContinuousIintegration,
)
domain_ORMEntity_strategy = st.builds(
    domain_ORMEntity,
)
domain_Artifacts_strategy = st.builds(
    domain_Artifacts,
    uid=
        safe_text
)
domain_Application_strategy = st.builds(
    domain_Application,
    uid=
        safe_text
)
domain_DomainArtifact_strategy = st.builds(
    domain_DomainArtifact,
    uid=
        safe_text,
    name=
        safe_text
)
HTMLLayerHolder_strategy = st.builds(
    HTMLLayerHolder,
)
domain_Component_strategy = st.builds(
    domain_Component,
    componentRoot=
        safe_text,
    uid=
        safe_text,
    name=
        safe_text
)
domain_ApplicationStyle_strategy = st.builds(
    domain_ApplicationStyle,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ApplicationMappers_strategy = st.builds(
    domain_ApplicationMappers,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Ingredient_strategy = st.builds(
    domain_Ingredient,
    uid=
        safe_text,
    name=
        safe_text,
    layer=
        safe_text
)
domain_ApplicationRecipes_strategy = st.builds(
    domain_ApplicationRecipes,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ApplicationUILayer_strategy = st.builds(
    domain_ApplicationUILayer,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Role_strategy = st.builds(
    domain_Role,
    uid=
        safe_text,
    name=
        safe_text
)
domain_DomainApplication_strategy = st.builds(
    domain_DomainApplication,
    uid=
        safe_text,
    name=
        safe_text
)
domain_GrantAccess_strategy = st.builds(
    domain_GrantAccess,
    uid=
        safe_text
)
domain_Secured_strategy = st.builds(
    domain_Secured,
)
domain_GenerationHint_strategy = st.builds(
    domain_GenerationHint,
    name=
        safe_text,
    uid=
        safe_text,
    applyedClass=
        safe_text
)
domain_Classifier_strategy = st.builds(
    domain_Classifier,
    details=
        safe_text,
    uid=
        safe_text
)
domain_Categorized_strategy = st.builds(
    domain_Categorized,
)
domain_HTMLLayerHolder_strategy = st.builds(
    domain_HTMLLayerHolder,
    columns=
        st.integers()
)
domain_EObject_strategy = st.builds(
    domain_EObject,
)
domain_DomainApplications_strategy = st.builds(
    domain_DomainApplications,
    name=
        safe_text,
    uid=
        safe_text
)
domain_DomainTypes_strategy = st.builds(
    domain_DomainTypes,
    uid=
        safe_text,
    name=
        safe_text
)
domain_DomainArtifacts_strategy = st.builds(
    domain_DomainArtifacts,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Domain_strategy = st.builds(
    domain_Domain,
    uid=
        safe_text
)
domain_TypesRepository_strategy = st.builds(
    domain_TypesRepository,
    uid=
        safe_text
)
MenuExtensionRef_strategy = st.builds(
    MenuExtensionRef,
)
MenuElement_strategy = st.builds(
    MenuElement,
)
domain_MenuExtensionPoint_strategy = st.builds(
    domain_MenuExtensionPoint,
)
domain_MenuSeparator_strategy = st.builds(
    domain_MenuSeparator,
)
domain_MenuExtensionRef_strategy = st.builds(
    domain_MenuExtensionRef,
)
domain_MenuHolder_strategy = st.builds(
    domain_MenuHolder,
)
domain_InfrastructureComponent_strategy = st.builds(
    domain_InfrastructureComponent,
    uid=
        safe_text,
    name=
        safe_text
)
domain_InfrastructureLayer_strategy = st.builds(
    domain_InfrastructureLayer,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Subsystem_strategy = st.builds(
    domain_Subsystem,
    uid=
        safe_text,
    name=
        safe_text
)
InfrastructureComponent_strategy = st.builds(
    InfrastructureComponent,
)
domain_ServerClaster_strategy = st.builds(
    domain_ServerClaster,
)
domain_Storage_strategy = st.builds(
    domain_Storage,
)
domain_Router_strategy = st.builds(
    domain_Router,
)
domain_Hub_strategy = st.builds(
    domain_Hub,
)
domain_Server_strategy = st.builds(
    domain_Server,
)
domain_EnterpriseInfrastructure_strategy = st.builds(
    domain_EnterpriseInfrastructure,
    uid=
        safe_text
)
domain_InfrastructureConnection_strategy = st.builds(
    domain_InfrastructureConnection,
    uid=
        safe_text
)
domain_Datacenter_strategy = st.builds(
    domain_Datacenter,
    uid=
        safe_text,
    name=
        safe_text
)
domain_OrderBy_strategy = st.builds(
    domain_OrderBy,
    order=
        safe_text,
    uid=
        safe_text
)
domain_Orders_strategy = st.builds(
    domain_Orders,
    uid=
        safe_text
)
domain_ArtificialField_strategy = st.builds(
    domain_ArtificialField,
    uid=
        safe_text,
    name=
        safe_text
)
domain_FormVariable_strategy = st.builds(
    domain_FormVariable,
    name=
        safe_text,
    uid=
        safe_text
)
ProxiesList_strategy = st.builds(
    ProxiesList,
)
domain_ProxiesList_strategy = st.builds(
    domain_ProxiesList,
)
MethodPointer_strategy = st.builds(
    MethodPointer,
)
domain_Dependency_strategy = st.builds(
    domain_Dependency,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Root_strategy = st.builds(
    domain_Root,
    uid=
        safe_text,
    name=
        safe_text
)
ItemIcon_strategy = st.builds(
    ItemIcon,
)
domain_SubMenu_strategy = st.builds(
    domain_SubMenu,
)
domain_Relation_strategy = st.builds(
    domain_Relation,
    uid=
        safe_text,
    name=
        safe_text,
    isTree=
        st.booleans()
)
OptionSelection_strategy = st.builds(
    OptionSelection,
)
domain_DropDownSelection_strategy = st.builds(
    domain_DropDownSelection,
    initialOptionValue=
        safe_text
)
Formatable_strategy = st.builds(
    Formatable,
)
ChildrenHolder_strategy = st.builds(
    ChildrenHolder,
)
SourcesPointer_strategy = st.builds(
    SourcesPointer,
)
domain_DataControl_strategy = st.builds(
    domain_DataControl,
    uid=
        safe_text,
    name=
        safe_text
)
Uielement_strategy = st.builds(
    Uielement,
)
domain_Menu_strategy = st.builds(
    domain_Menu,
    fakeName=
        safe_text
)
domain_SourcesPointer_strategy = st.builds(
    domain_SourcesPointer,
)
domain_Formatable_strategy = st.builds(
    domain_Formatable,
    format=
        safe_text
)
domain_ItemIcon_strategy = st.builds(
    domain_ItemIcon,
)
domain_AreaRef_strategy = st.builds(
    domain_AreaRef,
    group=
        st.integers()
)
MenuHolder_strategy = st.builds(
    MenuHolder,
)
EnabledUIItem_strategy = st.builds(
    EnabledUIItem,
)
domain_EnabledUIItem_strategy = st.builds(
    domain_EnabledUIItem,
)
Context_strategy = st.builds(
    Context,
)
domain_FlexField_strategy = st.builds(
    domain_FlexField,
)
domain_FlexFields_strategy = st.builds(
    domain_FlexFields,
)
domain_NickNamed_strategy = st.builds(
    domain_NickNamed,
    nickname=
        safe_text
)
InputElement_strategy = st.builds(
    InputElement,
)
domain_Image_strategy = st.builds(
    domain_Image,
)
domain_Password_strategy = st.builds(
    domain_Password,
)
domain_OutputText_strategy = st.builds(
    domain_OutputText,
)
domain_Date_strategy = st.builds(
    domain_Date,
)
domain_InputText_strategy = st.builds(
    domain_InputText,
)
domain_CheckBox_strategy = st.builds(
    domain_CheckBox,
)
domain_OptionSelection_strategy = st.builds(
    domain_OptionSelection,
)
domain_StyleElement_strategy = st.builds(
    domain_StyleElement,
)
ContextParameters_strategy = st.builds(
    ContextParameters,
)
domain_Trigger_strategy = st.builds(
    domain_Trigger,
)
ContextValue_strategy = st.builds(
    ContextValue,
)
domain_StyleClass_strategy = st.builds(
    domain_StyleClass,
)
domain_ContextParameters_strategy = st.builds(
    domain_ContextParameters,
)
domain_ExpressionPart_strategy = st.builds(
    domain_ExpressionPart,
    order=
        st.integers(),
    uid=
        safe_text,
    expressionType=
        safe_text
)
domain_ContextValue_strategy = st.builds(
    domain_ContextValue,
    constant=
        st.booleans(),
    uid=
        safe_text,
    value=
        safe_text
)
domain_ContextParameter_strategy = st.builds(
    domain_ContextParameter,
    uid=
        safe_text,
    operation=
        safe_text
)
domain_ChildrenHolder_strategy = st.builds(
    domain_ChildrenHolder,
)
domain_InputElement_strategy = st.builds(
    domain_InputElement,
)
domain_LinkToMessage_strategy = st.builds(
    domain_LinkToMessage,
    uid=
        safe_text
)
domain_LinkToLabel_strategy = st.builds(
    domain_LinkToLabel,
    uid=
        safe_text
)
domain_LayerHolder_strategy = st.builds(
    domain_LayerHolder,
)
domain_Controls_strategy = st.builds(
    domain_Controls,
    uid=
        safe_text
)
Trigger_strategy = st.builds(
    Trigger,
)
domain_UpdateTrigger_strategy = st.builds(
    domain_UpdateTrigger,
    uid=
        safe_text
)
domain_PREFormTrigger_strategy = st.builds(
    domain_PREFormTrigger,
    uid=
        safe_text
)
domain_InsertTrigger_strategy = st.builds(
    domain_InsertTrigger,
    uid=
        safe_text
)
domain_POSTQueryTrigger_strategy = st.builds(
    domain_POSTQueryTrigger,
    uid=
        safe_text
)
domain_PREInsertTrigger_strategy = st.builds(
    domain_PREInsertTrigger,
    uid=
        safe_text
)
domain_PREQueryTrigger_strategy = st.builds(
    domain_PREQueryTrigger,
    uid=
        safe_text
)
domain_DeleteTrigger_strategy = st.builds(
    domain_DeleteTrigger,
    uid=
        safe_text
)
domain_CreateTrigger_strategy = st.builds(
    domain_CreateTrigger,
    uid=
        safe_text
)
domain_POSTCreateTrigger_strategy = st.builds(
    domain_POSTCreateTrigger,
    uid=
        safe_text
)
domain_SearchTrigger_strategy = st.builds(
    domain_SearchTrigger,
    uid=
        safe_text
)
domain_PREUpdateTrigger_strategy = st.builds(
    domain_PREUpdateTrigger,
    uid=
        safe_text
)
domain_PREDeleteTrigger_strategy = st.builds(
    domain_PREDeleteTrigger,
    uid=
        safe_text
)
domain_CanvasView_strategy = st.builds(
    domain_CanvasView,
    uid=
        safe_text
)
domain_ViewPortTrigger_strategy = st.builds(
    domain_ViewPortTrigger,
    uid=
        safe_text
)
ViewElement_strategy = st.builds(
    ViewElement,
)
Orderable_strategy = st.builds(
    Orderable,
)
domain_ViewPort_strategy = st.builds(
    domain_ViewPort,
    name=
        safe_text,
    uid=
        safe_text
)
domain_ViewArea_strategy = st.builds(
    domain_ViewArea,
    name=
        safe_text,
    uid=
        safe_text
)
domain_MenuView_strategy = st.builds(
    domain_MenuView,
    uid=
        safe_text
)
FlexFields_strategy = st.builds(
    FlexFields,
)
domain_MenuItem_strategy = st.builds(
    domain_MenuItem,
)
MultiLangLabel_strategy = st.builds(
    MultiLangLabel,
)
domain_Tree_strategy = st.builds(
    domain_Tree,
    label=
        safe_text
)
domain_MessageElement_strategy = st.builds(
    domain_MessageElement,
    label=
        safe_text
)
domain_Table_strategy = st.builds(
    domain_Table,
    rowNumber=
        st.integers(),
    label=
        safe_text
)
domain_Button_strategy = st.builds(
    domain_Button,
    label=
        safe_text
)
domain_Label_strategy = st.builds(
    domain_Label,
    label=
        safe_text
)
DefaultCavas_strategy = st.builds(
    DefaultCavas,
)
ViewPortHolder_strategy = st.builds(
    ViewPortHolder,
)
CanvasFrame_strategy = st.builds(
    CanvasFrame,
)
domain_Canvas_strategy = st.builds(
    domain_Canvas,
)
domain_TabPage_strategy = st.builds(
    domain_TabPage,
)
domain_TabCanvas_strategy = st.builds(
    domain_TabCanvas,
    orientation=
        safe_text
)
domain_PopupCanvas_strategy = st.builds(
    domain_PopupCanvas,
    modal=
        st.booleans()
)
NickNamed_strategy = st.builds(
    NickNamed,
)
domain_DefaultCavas_strategy = st.builds(
    domain_DefaultCavas,
    defaultCanvas=
        st.booleans()
)
domain_ViewPortHolder_strategy = st.builds(
    domain_ViewPortHolder,
)
StyleElement_strategy = st.builds(
    StyleElement,
)
domain_Uielement_strategy = st.builds(
    domain_Uielement,
    uid=
        safe_text
)
domain_Selection_strategy = st.builds(
    domain_Selection,
)
domain_Column_strategy = st.builds(
    domain_Column,
    label=
        safe_text,
    uid=
        safe_text
)
domain_MenuFolder_strategy = st.builds(
    domain_MenuFolder,
    name=
        safe_text,
    uid=
        safe_text,
    extensionPoint=
        st.booleans()
)
domain_ViewElement_strategy = st.builds(
    domain_ViewElement,
)
domain_MenuElement_strategy = st.builds(
    domain_MenuElement,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Context_strategy = st.builds(
    domain_Context,
)
domain_MultiLangLabel_strategy = st.builds(
    domain_MultiLangLabel,
)
domain_Orderable_strategy = st.builds(
    domain_Orderable,
    order=
        st.integers()
)
domain_MenuDefinition_strategy = st.builds(
    domain_MenuDefinition,
    name=
        safe_text,
    uid=
        safe_text
)
domain_TabPagesInheritance_strategy = st.builds(
    domain_TabPagesInheritance,
    uid=
        safe_text
)
domain_ViewInheritance_strategy = st.builds(
    domain_ViewInheritance,
    uid=
        safe_text
)
domain_CanvasFrame_strategy = st.builds(
    domain_CanvasFrame,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Views_strategy = st.builds(
    domain_Views,
    uid=
        safe_text
)
domain_FormParameter_strategy = st.builds(
    domain_FormParameter,
    name=
        safe_text,
    uid=
        safe_text
)
domain_FormDataControls_strategy = st.builds(
    domain_FormDataControls,
    uid=
        safe_text,
    name=
        safe_text
)
domain_FormView_strategy = st.builds(
    domain_FormView,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Form_strategy = st.builds(
    domain_Form,
    uid=
        safe_text,
    name=
        safe_text
)
domain_Types_strategy = st.builds(
    domain_Types,
    name=
        safe_text,
    uid=
        safe_text
)
domain_EnumAttribute_strategy = st.builds(
    domain_EnumAttribute,
    uid=
        safe_text,
    value=
        safe_text,
    name=
        safe_text
)
domain_ReturnValue_strategy = st.builds(
    domain_ReturnValue,
    uid=
        safe_text
)
domain_Parameter_strategy = st.builds(
    domain_Parameter,
    uid=
        safe_text,
    name=
        safe_text,
    order=
        st.integers()
)
Secured_strategy = st.builds(
    Secured,
)
domain_Window_strategy = st.builds(
    domain_Window,
)
domain_Operation_strategy = st.builds(
    domain_Operation,
    name=
        safe_text,
    uid=
        safe_text
)
TypeElement_strategy = st.builds(
    TypeElement,
)
domain_Type_strategy = st.builds(
    domain_Type,
)
domain_TypeReference_strategy = st.builds(
    domain_TypeReference,
)
domain_Enumarator_strategy = st.builds(
    domain_Enumarator,
)
domain_Primitive_strategy = st.builds(
    domain_Primitive,
)
domain_Attribute_strategy = st.builds(
    domain_Attribute,
    name=
        safe_text,
    uid=
        safe_text,
    pk=
        st.booleans()
)
domain_Link_strategy = st.builds(
    domain_Link,
    uid=
        safe_text
)
RelationShip_strategy = st.builds(
    RelationShip,
)
domain_Generalization_strategy = st.builds(
    domain_Generalization,
)
domain_Assosiation_strategy = st.builds(
    domain_Assosiation,
    type=
        safe_text
)
domain_References_strategy = st.builds(
    domain_References,
)
domain_RelationShip_strategy = st.builds(
    domain_RelationShip,
    uid=
        safe_text
)
domain_TypeElement_strategy = st.builds(
    domain_TypeElement,
    name=
        safe_text,
    uid=
        safe_text
)
domain_Package_strategy = st.builds(
    domain_Package,
    uid=
        safe_text,
    name=
        safe_text
)
domain_TypePointer_strategy = st.builds(
    domain_TypePointer,
    fakeTypeName=
        safe_text,
    fakePackageName=
        safe_text
)
domain_ArtifactRef_strategy = st.builds(
    domain_ArtifactRef,
    uid=
        safe_text
)
domain_QueryVariable_strategy = st.builds(
    domain_QueryVariable,
    value=
        safe_text,
    uid=
        safe_text
)
domain_KeyValuePair_strategy = st.builds(
    domain_KeyValuePair,
    key=
        safe_text,
    value=
        safe_text,
    uid=
        safe_text
)
domain_TypeDefinition_strategy = st.builds(
    domain_TypeDefinition,
    uid=
        safe_text
)
domain_Query_strategy = st.builds(
    domain_Query,
    uid=
        safe_text,
    name=
        safe_text
)
domain_MappingSpecifier_strategy = st.builds(
    domain_MappingSpecifier,
    uid=
        safe_text
)
ArtifactRef_strategy = st.builds(
    ArtifactRef,
)
domain_ModelMapper_strategy = st.builds(
    domain_ModelMapper,
    name=
        safe_text,
    artifactRoot=
        safe_text,
    artifactExecutionString=
        safe_text
)
domain_HashProperty_strategy = st.builds(
    domain_HashProperty,
    fakeName=
        safe_text,
    uid=
        safe_text
)
domain_Property_strategy = st.builds(
    domain_Property,
    value=
        safe_text,
    uid=
        safe_text,
    fakeName=
        safe_text
)
Component_strategy = st.builds(
    Component,
)
domain_JavaComponent_strategy = st.builds(
    domain_JavaComponent,
    basePackage=
        safe_text,
    version=
        safe_text,
    groupId=
        safe_text,
    artifactId=
        safe_text
)

@given(instance=UsingMappers_strategy)
@settings(max_examples=50)
def test_usingmappers_instantiation(instance):
    assert isinstance(instance, UsingMappers)

@given(instance=domain_DeploymentStarStep_strategy)
@settings(max_examples=50)
def test_domain_deploymentstarstep_instantiation(instance):
    assert isinstance(instance, domain_DeploymentStarStep)



@given(instance=domain_DeploymentStarStep_strategy)
def test_domain_deploymentstarstep_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DeploymentStarStep_strategy)
def test_domain_deploymentstarstep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_DeploymentComponent_strategy)
@settings(max_examples=50)
def test_domain_deploymentcomponent_instantiation(instance):
    assert isinstance(instance, domain_DeploymentComponent)



@given(instance=domain_DeploymentComponent_strategy)
def test_domain_deploymentcomponent_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DeploymentComponent_strategy)
def test_domain_deploymentcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_DeploymentComponents_strategy)
@settings(max_examples=50)
def test_domain_deploymentcomponents_instantiation(instance):
    assert isinstance(instance, domain_DeploymentComponents)



@given(instance=domain_DeploymentComponents_strategy)
def test_domain_deploymentcomponents_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ConfigExtension_strategy)
@settings(max_examples=50)
def test_domain_configextension_instantiation(instance):
    assert isinstance(instance, domain_ConfigExtension)



@given(instance=domain_ConfigExtension_strategy)
def test_domain_configextension_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_DeploymentSequence_strategy)
@settings(max_examples=50)
def test_domain_deploymentsequence_instantiation(instance):
    assert isinstance(instance, domain_DeploymentSequence)



@given(instance=domain_DeploymentSequence_strategy)
def test_domain_deploymentsequence_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DeploymentSequence_strategy)
def test_domain_deploymentsequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Infrastructure_strategy)
@settings(max_examples=50)
def test_domain_infrastructure_instantiation(instance):
    assert isinstance(instance, domain_Infrastructure)



@given(instance=domain_Infrastructure_strategy)
def test_domain_infrastructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Infrastructure_strategy)
def test_domain_infrastructure_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Configuration_strategy)
@settings(max_examples=50)
def test_domain_configuration_instantiation(instance):
    assert isinstance(instance, domain_Configuration)



@given(instance=domain_Configuration_strategy)
def test_domain_configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Configuration_strategy)
def test_domain_configuration_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Recipe_strategy)
@settings(max_examples=50)
def test_domain_recipe_instantiation(instance):
    assert isinstance(instance, domain_Recipe)



@given(instance=domain_Recipe_strategy)
def test_domain_recipe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Recipe_strategy)
def test_domain_recipe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_UsingMappers_strategy)
@settings(max_examples=50)
def test_domain_usingmappers_instantiation(instance):
    assert isinstance(instance, domain_UsingMappers)

@given(instance=TypeMapper_strategy)
@settings(max_examples=50)
def test_typemapper_instantiation(instance):
    assert isinstance(instance, TypeMapper)

@given(instance=domain_JavaScriptMapper_strategy)
@settings(max_examples=50)
def test_domain_javascriptmapper_instantiation(instance):
    assert isinstance(instance, domain_JavaScriptMapper)



@given(instance=domain_JavaScriptMapper_strategy)
def test_domain_javascriptmapper_libraryUrl_setter(instance):
    original = instance.libraryUrl
    instance.libraryUrl = original
    assert instance.libraryUrl == original

@given(instance=domain_JavaMapper_strategy)
@settings(max_examples=50)
def test_domain_javamapper_instantiation(instance):
    assert isinstance(instance, domain_JavaMapper)



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_artifactType_setter(instance):
    original = instance.artifactType
    instance.artifactType = original
    assert instance.artifactType == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_mappedToClassName_setter(instance):
    original = instance.mappedToClassName
    instance.mappedToClassName = original
    assert instance.mappedToClassName == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original



@given(instance=domain_JavaMapper_strategy)
def test_domain_javamapper_mappedToPackageName_setter(instance):
    original = instance.mappedToPackageName
    instance.mappedToPackageName = original
    assert instance.mappedToPackageName == original

@given(instance=Mapper_strategy)
@settings(max_examples=50)
def test_mapper_instantiation(instance):
    assert isinstance(instance, Mapper)

@given(instance=domain_CSSMapper_strategy)
@settings(max_examples=50)
def test_domain_cssmapper_instantiation(instance):
    assert isinstance(instance, domain_CSSMapper)



@given(instance=domain_CSSMapper_strategy)
def test_domain_cssmapper_libraryUrl_setter(instance):
    original = instance.libraryUrl
    instance.libraryUrl = original
    assert instance.libraryUrl == original



@given(instance=domain_CSSMapper_strategy)
def test_domain_cssmapper_fakeTypeName_setter(instance):
    original = instance.fakeTypeName
    instance.fakeTypeName = original
    assert instance.fakeTypeName == original



@given(instance=domain_CSSMapper_strategy)
def test_domain_cssmapper_fakePackageName_setter(instance):
    original = instance.fakePackageName
    instance.fakePackageName = original
    assert instance.fakePackageName == original

@given(instance=domain_RoleMapper_strategy)
@settings(max_examples=50)
def test_domain_rolemapper_instantiation(instance):
    assert isinstance(instance, domain_RoleMapper)



@given(instance=domain_RoleMapper_strategy)
def test_domain_rolemapper_globalRoleName_setter(instance):
    original = instance.globalRoleName
    instance.globalRoleName = original
    assert instance.globalRoleName == original



@given(instance=domain_RoleMapper_strategy)
def test_domain_rolemapper_localRoleName_setter(instance):
    original = instance.localRoleName
    instance.localRoleName = original
    assert instance.localRoleName == original



@given(instance=domain_RoleMapper_strategy)
def test_domain_rolemapper_fakeRoleName_setter(instance):
    original = instance.fakeRoleName
    instance.fakeRoleName = original
    assert instance.fakeRoleName == original

@given(instance=domain_Mapper_strategy)
@settings(max_examples=50)
def test_domain_mapper_instantiation(instance):
    assert isinstance(instance, domain_Mapper)



@given(instance=domain_Mapper_strategy)
def test_domain_mapper_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Mapper_strategy)
def test_domain_mapper_uiLayer_setter(instance):
    original = instance.uiLayer
    instance.uiLayer = original
    assert instance.uiLayer == original



@given(instance=domain_Mapper_strategy)
def test_domain_mapper_serviceLayer_setter(instance):
    original = instance.serviceLayer
    instance.serviceLayer = original
    assert instance.serviceLayer == original

@given(instance=domain_StyleLibrary_strategy)
@settings(max_examples=50)
def test_domain_stylelibrary_instantiation(instance):
    assert isinstance(instance, domain_StyleLibrary)



@given(instance=domain_StyleLibrary_strategy)
def test_domain_stylelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_StyleLibrary_strategy)
def test_domain_stylelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Group_strategy)
@settings(max_examples=50)
def test_domain_group_instantiation(instance):
    assert isinstance(instance, domain_Group)



@given(instance=domain_Group_strategy)
def test_domain_group_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Group_strategy)
def test_domain_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_StyleSet_strategy)
@settings(max_examples=50)
def test_domain_styleset_instantiation(instance):
    assert isinstance(instance, domain_StyleSet)



@given(instance=domain_StyleSet_strategy)
def test_domain_styleset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_StyleSet_strategy)
def test_domain_styleset_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Translation_strategy)
@settings(max_examples=50)
def test_domain_translation_instantiation(instance):
    assert isinstance(instance, domain_Translation)



@given(instance=domain_Translation_strategy)
def test_domain_translation_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original



@given(instance=domain_Translation_strategy)
def test_domain_translation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Message_strategy)
@settings(max_examples=50)
def test_domain_message_instantiation(instance):
    assert isinstance(instance, domain_Message)



@given(instance=domain_Message_strategy)
def test_domain_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Message_strategy)
def test_domain_message_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_LanguageRef_strategy)
@settings(max_examples=50)
def test_domain_languageref_instantiation(instance):
    assert isinstance(instance, domain_LanguageRef)



@given(instance=domain_LanguageRef_strategy)
def test_domain_languageref_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Categorized_strategy)
@settings(max_examples=50)
def test_categorized_instantiation(instance):
    assert isinstance(instance, Categorized)

@given(instance=domain_Language_strategy)
@settings(max_examples=50)
def test_domain_language_instantiation(instance):
    assert isinstance(instance, domain_Language)



@given(instance=domain_Language_strategy)
def test_domain_language_defaultLang_setter(instance):
    original = instance.defaultLang
    instance.defaultLang = original
    assert instance.defaultLang == original



@given(instance=domain_Language_strategy)
def test_domain_language_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=domain_Language_strategy)
def test_domain_language_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Language_strategy)
def test_domain_language_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=domain_MessageLibrary_strategy)
@settings(max_examples=50)
def test_domain_messagelibrary_instantiation(instance):
    assert isinstance(instance, domain_MessageLibrary)



@given(instance=domain_MessageLibrary_strategy)
def test_domain_messagelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_MessageLibrary_strategy)
def test_domain_messagelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=TypePointer_strategy)
@settings(max_examples=50)
def test_typepointer_instantiation(instance):
    assert isinstance(instance, TypePointer)

@given(instance=domain_TypeMapper_strategy)
@settings(max_examples=50)
def test_domain_typemapper_instantiation(instance):
    assert isinstance(instance, domain_TypeMapper)

@given(instance=domain_MethodPointer_strategy)
@settings(max_examples=50)
def test_domain_methodpointer_instantiation(instance):
    assert isinstance(instance, domain_MethodPointer)



@given(instance=domain_MethodPointer_strategy)
def test_domain_methodpointer_fakeMethod_setter(instance):
    original = instance.fakeMethod
    instance.fakeMethod = original
    assert instance.fakeMethod == original

@given(instance=domain_Mappers_strategy)
@settings(max_examples=50)
def test_domain_mappers_instantiation(instance):
    assert isinstance(instance, domain_Mappers)



@given(instance=domain_Mappers_strategy)
def test_domain_mappers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationMapper_strategy)
@settings(max_examples=50)
def test_domain_applicationmapper_instantiation(instance):
    assert isinstance(instance, domain_ApplicationMapper)



@given(instance=domain_ApplicationMapper_strategy)
def test_domain_applicationmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationMapper_strategy)
def test_domain_applicationmapper_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Recipes_strategy)
@settings(max_examples=50)
def test_domain_recipes_instantiation(instance):
    assert isinstance(instance, domain_Recipes)



@given(instance=domain_Recipes_strategy)
def test_domain_recipes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationRecipe_strategy)
@settings(max_examples=50)
def test_domain_applicationrecipe_instantiation(instance):
    assert isinstance(instance, domain_ApplicationRecipe)



@given(instance=domain_ApplicationRecipe_strategy)
def test_domain_applicationrecipe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationRecipe_strategy)
def test_domain_applicationrecipe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_UIPackage_strategy)
@settings(max_examples=50)
def test_domain_uipackage_instantiation(instance):
    assert isinstance(instance, domain_UIPackage)



@given(instance=domain_UIPackage_strategy)
def test_domain_uipackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationUIPackage_strategy)
@settings(max_examples=50)
def test_domain_applicationuipackage_instantiation(instance):
    assert isinstance(instance, domain_ApplicationUIPackage)



@given(instance=domain_ApplicationUIPackage_strategy)
def test_domain_applicationuipackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationUIPackage_strategy)
def test_domain_applicationuipackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Styles_strategy)
@settings(max_examples=50)
def test_domain_styles_instantiation(instance):
    assert isinstance(instance, domain_Styles)



@given(instance=domain_Styles_strategy)
def test_domain_styles_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Roles_strategy)
@settings(max_examples=50)
def test_domain_roles_instantiation(instance):
    assert isinstance(instance, domain_Roles)



@given(instance=domain_Roles_strategy)
def test_domain_roles_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Messages_strategy)
@settings(max_examples=50)
def test_domain_messages_instantiation(instance):
    assert isinstance(instance, domain_Messages)



@given(instance=domain_Messages_strategy)
def test_domain_messages_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationMessages_strategy)
@settings(max_examples=50)
def test_domain_applicationmessages_instantiation(instance):
    assert isinstance(instance, domain_ApplicationMessages)



@given(instance=domain_ApplicationMessages_strategy)
def test_domain_applicationmessages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationMessages_strategy)
def test_domain_applicationmessages_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationRole_strategy)
@settings(max_examples=50)
def test_domain_applicationrole_instantiation(instance):
    assert isinstance(instance, domain_ApplicationRole)



@given(instance=domain_ApplicationRole_strategy)
def test_domain_applicationrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationRole_strategy)
def test_domain_applicationrole_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationInfrastructureLayer_strategy)
@settings(max_examples=50)
def test_domain_applicationinfrastructurelayer_instantiation(instance):
    assert isinstance(instance, domain_ApplicationInfrastructureLayer)



@given(instance=domain_ApplicationInfrastructureLayer_strategy)
def test_domain_applicationinfrastructurelayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ApplicationInfrastructureLayer_strategy)
def test_domain_applicationinfrastructurelayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_StylesPackage_strategy)
@settings(max_examples=50)
def test_domain_stylespackage_instantiation(instance):
    assert isinstance(instance, domain_StylesPackage)



@given(instance=domain_StylesPackage_strategy)
def test_domain_stylespackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_StylesPackage_strategy)
def test_domain_stylespackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Option_strategy)
@settings(max_examples=50)
def test_domain_option_instantiation(instance):
    assert isinstance(instance, domain_Option)



@given(instance=domain_Option_strategy)
def test_domain_option_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Option_strategy)
def test_domain_option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain_QueryParameter_strategy)
@settings(max_examples=50)
def test_domain_queryparameter_instantiation(instance):
    assert isinstance(instance, domain_QueryParameter)



@given(instance=domain_QueryParameter_strategy)
def test_domain_queryparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_QueryParameter_strategy)
def test_domain_queryparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Specifier_strategy)
@settings(max_examples=50)
def test_domain_specifier_instantiation(instance):
    assert isinstance(instance, domain_Specifier)



@given(instance=domain_Specifier_strategy)
def test_domain_specifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Specifier_strategy)
def test_domain_specifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ModelQuery_strategy)
@settings(max_examples=50)
def test_domain_modelquery_instantiation(instance):
    assert isinstance(instance, domain_ModelQuery)



@given(instance=domain_ModelQuery_strategy)
def test_domain_modelquery_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=domain_ModelQuery_strategy)
def test_domain_modelquery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ModelQuery_strategy)
def test_domain_modelquery_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ConfigHash_strategy)
@settings(max_examples=50)
def test_domain_confighash_instantiation(instance):
    assert isinstance(instance, domain_ConfigHash)



@given(instance=domain_ConfigHash_strategy)
def test_domain_confighash_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ConfigHash_strategy)
def test_domain_confighash_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_ConfigVariable_strategy)
@settings(max_examples=50)
def test_domain_configvariable_instantiation(instance):
    assert isinstance(instance, domain_ConfigVariable)



@given(instance=domain_ConfigVariable_strategy)
def test_domain_configvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ConfigVariable_strategy)
def test_domain_configvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Artifact_strategy)
@settings(max_examples=50)
def test_domain_artifact_instantiation(instance):
    assert isinstance(instance, domain_Artifact)



@given(instance=domain_Artifact_strategy)
def test_domain_artifact_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=domain_Artifact_strategy)
def test_domain_artifact_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=domain_Artifact_strategy)
def test_domain_artifact_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Artifact_strategy)
def test_domain_artifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomainArtifact_strategy)
@settings(max_examples=50)
def test_domainartifact_instantiation(instance):
    assert isinstance(instance, DomainArtifact)

@given(instance=domain_JPAService_strategy)
@settings(max_examples=50)
def test_domain_jpaservice_instantiation(instance):
    assert isinstance(instance, domain_JPAService)

@given(instance=domain_EJBService_strategy)
@settings(max_examples=50)
def test_domain_ejbservice_instantiation(instance):
    assert isinstance(instance, domain_EJBService)

@given(instance=domain_ContinuousIintegration_strategy)
@settings(max_examples=50)
def test_domain_continuousiintegration_instantiation(instance):
    assert isinstance(instance, domain_ContinuousIintegration)

@given(instance=domain_ORMEntity_strategy)
@settings(max_examples=50)
def test_domain_ormentity_instantiation(instance):
    assert isinstance(instance, domain_ORMEntity)

@given(instance=domain_Artifacts_strategy)
@settings(max_examples=50)
def test_domain_artifacts_instantiation(instance):
    assert isinstance(instance, domain_Artifacts)



@given(instance=domain_Artifacts_strategy)
def test_domain_artifacts_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Application_strategy)
@settings(max_examples=50)
def test_domain_application_instantiation(instance):
    assert isinstance(instance, domain_Application)



@given(instance=domain_Application_strategy)
def test_domain_application_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_DomainArtifact_strategy)
@settings(max_examples=50)
def test_domain_domainartifact_instantiation(instance):
    assert isinstance(instance, domain_DomainArtifact)



@given(instance=domain_DomainArtifact_strategy)
def test_domain_domainartifact_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DomainArtifact_strategy)
def test_domain_domainartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HTMLLayerHolder_strategy)
@settings(max_examples=50)
def test_htmllayerholder_instantiation(instance):
    assert isinstance(instance, HTMLLayerHolder)

@given(instance=domain_Component_strategy)
@settings(max_examples=50)
def test_domain_component_instantiation(instance):
    assert isinstance(instance, domain_Component)



@given(instance=domain_Component_strategy)
def test_domain_component_componentRoot_setter(instance):
    original = instance.componentRoot
    instance.componentRoot = original
    assert instance.componentRoot == original



@given(instance=domain_Component_strategy)
def test_domain_component_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Component_strategy)
def test_domain_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_ApplicationStyle_strategy)
@settings(max_examples=50)
def test_domain_applicationstyle_instantiation(instance):
    assert isinstance(instance, domain_ApplicationStyle)



@given(instance=domain_ApplicationStyle_strategy)
def test_domain_applicationstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationStyle_strategy)
def test_domain_applicationstyle_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationMappers_strategy)
@settings(max_examples=50)
def test_domain_applicationmappers_instantiation(instance):
    assert isinstance(instance, domain_ApplicationMappers)



@given(instance=domain_ApplicationMappers_strategy)
def test_domain_applicationmappers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationMappers_strategy)
def test_domain_applicationmappers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Ingredient_strategy)
@settings(max_examples=50)
def test_domain_ingredient_instantiation(instance):
    assert isinstance(instance, domain_Ingredient)



@given(instance=domain_Ingredient_strategy)
def test_domain_ingredient_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Ingredient_strategy)
def test_domain_ingredient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Ingredient_strategy)
def test_domain_ingredient_layer_setter(instance):
    original = instance.layer
    instance.layer = original
    assert instance.layer == original

@given(instance=domain_ApplicationRecipes_strategy)
@settings(max_examples=50)
def test_domain_applicationrecipes_instantiation(instance):
    assert isinstance(instance, domain_ApplicationRecipes)



@given(instance=domain_ApplicationRecipes_strategy)
def test_domain_applicationrecipes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ApplicationRecipes_strategy)
def test_domain_applicationrecipes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ApplicationUILayer_strategy)
@settings(max_examples=50)
def test_domain_applicationuilayer_instantiation(instance):
    assert isinstance(instance, domain_ApplicationUILayer)



@given(instance=domain_ApplicationUILayer_strategy)
def test_domain_applicationuilayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ApplicationUILayer_strategy)
def test_domain_applicationuilayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Role_strategy)
@settings(max_examples=50)
def test_domain_role_instantiation(instance):
    assert isinstance(instance, domain_Role)



@given(instance=domain_Role_strategy)
def test_domain_role_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Role_strategy)
def test_domain_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_DomainApplication_strategy)
@settings(max_examples=50)
def test_domain_domainapplication_instantiation(instance):
    assert isinstance(instance, domain_DomainApplication)



@given(instance=domain_DomainApplication_strategy)
def test_domain_domainapplication_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DomainApplication_strategy)
def test_domain_domainapplication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_GrantAccess_strategy)
@settings(max_examples=50)
def test_domain_grantaccess_instantiation(instance):
    assert isinstance(instance, domain_GrantAccess)



@given(instance=domain_GrantAccess_strategy)
def test_domain_grantaccess_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Secured_strategy)
@settings(max_examples=50)
def test_domain_secured_instantiation(instance):
    assert isinstance(instance, domain_Secured)

@given(instance=domain_GenerationHint_strategy)
@settings(max_examples=50)
def test_domain_generationhint_instantiation(instance):
    assert isinstance(instance, domain_GenerationHint)



@given(instance=domain_GenerationHint_strategy)
def test_domain_generationhint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_GenerationHint_strategy)
def test_domain_generationhint_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_GenerationHint_strategy)
def test_domain_generationhint_applyedClass_setter(instance):
    original = instance.applyedClass
    instance.applyedClass = original
    assert instance.applyedClass == original

@given(instance=domain_Classifier_strategy)
@settings(max_examples=50)
def test_domain_classifier_instantiation(instance):
    assert isinstance(instance, domain_Classifier)



@given(instance=domain_Classifier_strategy)
def test_domain_classifier_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=domain_Classifier_strategy)
def test_domain_classifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Categorized_strategy)
@settings(max_examples=50)
def test_domain_categorized_instantiation(instance):
    assert isinstance(instance, domain_Categorized)

@given(instance=domain_HTMLLayerHolder_strategy)
@settings(max_examples=50)
def test_domain_htmllayerholder_instantiation(instance):
    assert isinstance(instance, domain_HTMLLayerHolder)



@given(instance=domain_HTMLLayerHolder_strategy)
def test_domain_htmllayerholder_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=domain_EObject_strategy)
@settings(max_examples=50)
def test_domain_eobject_instantiation(instance):
    assert isinstance(instance, domain_EObject)

@given(instance=domain_DomainApplications_strategy)
@settings(max_examples=50)
def test_domain_domainapplications_instantiation(instance):
    assert isinstance(instance, domain_DomainApplications)



@given(instance=domain_DomainApplications_strategy)
def test_domain_domainapplications_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_DomainApplications_strategy)
def test_domain_domainapplications_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_DomainTypes_strategy)
@settings(max_examples=50)
def test_domain_domaintypes_instantiation(instance):
    assert isinstance(instance, domain_DomainTypes)



@given(instance=domain_DomainTypes_strategy)
def test_domain_domaintypes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DomainTypes_strategy)
def test_domain_domaintypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_DomainArtifacts_strategy)
@settings(max_examples=50)
def test_domain_domainartifacts_instantiation(instance):
    assert isinstance(instance, domain_DomainArtifacts)



@given(instance=domain_DomainArtifacts_strategy)
def test_domain_domainartifacts_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DomainArtifacts_strategy)
def test_domain_domainartifacts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Domain_strategy)
@settings(max_examples=50)
def test_domain_domain_instantiation(instance):
    assert isinstance(instance, domain_Domain)



@given(instance=domain_Domain_strategy)
def test_domain_domain_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_TypesRepository_strategy)
@settings(max_examples=50)
def test_domain_typesrepository_instantiation(instance):
    assert isinstance(instance, domain_TypesRepository)



@given(instance=domain_TypesRepository_strategy)
def test_domain_typesrepository_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=MenuExtensionRef_strategy)
@settings(max_examples=50)
def test_menuextensionref_instantiation(instance):
    assert isinstance(instance, MenuExtensionRef)

@given(instance=MenuElement_strategy)
@settings(max_examples=50)
def test_menuelement_instantiation(instance):
    assert isinstance(instance, MenuElement)

@given(instance=domain_MenuExtensionPoint_strategy)
@settings(max_examples=50)
def test_domain_menuextensionpoint_instantiation(instance):
    assert isinstance(instance, domain_MenuExtensionPoint)

@given(instance=domain_MenuSeparator_strategy)
@settings(max_examples=50)
def test_domain_menuseparator_instantiation(instance):
    assert isinstance(instance, domain_MenuSeparator)

@given(instance=domain_MenuExtensionRef_strategy)
@settings(max_examples=50)
def test_domain_menuextensionref_instantiation(instance):
    assert isinstance(instance, domain_MenuExtensionRef)

@given(instance=domain_MenuHolder_strategy)
@settings(max_examples=50)
def test_domain_menuholder_instantiation(instance):
    assert isinstance(instance, domain_MenuHolder)

@given(instance=domain_InfrastructureComponent_strategy)
@settings(max_examples=50)
def test_domain_infrastructurecomponent_instantiation(instance):
    assert isinstance(instance, domain_InfrastructureComponent)



@given(instance=domain_InfrastructureComponent_strategy)
def test_domain_infrastructurecomponent_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_InfrastructureComponent_strategy)
def test_domain_infrastructurecomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_InfrastructureLayer_strategy)
@settings(max_examples=50)
def test_domain_infrastructurelayer_instantiation(instance):
    assert isinstance(instance, domain_InfrastructureLayer)



@given(instance=domain_InfrastructureLayer_strategy)
def test_domain_infrastructurelayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_InfrastructureLayer_strategy)
def test_domain_infrastructurelayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Subsystem_strategy)
@settings(max_examples=50)
def test_domain_subsystem_instantiation(instance):
    assert isinstance(instance, domain_Subsystem)



@given(instance=domain_Subsystem_strategy)
def test_domain_subsystem_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Subsystem_strategy)
def test_domain_subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InfrastructureComponent_strategy)
@settings(max_examples=50)
def test_infrastructurecomponent_instantiation(instance):
    assert isinstance(instance, InfrastructureComponent)

@given(instance=domain_ServerClaster_strategy)
@settings(max_examples=50)
def test_domain_serverclaster_instantiation(instance):
    assert isinstance(instance, domain_ServerClaster)

@given(instance=domain_Storage_strategy)
@settings(max_examples=50)
def test_domain_storage_instantiation(instance):
    assert isinstance(instance, domain_Storage)

@given(instance=domain_Router_strategy)
@settings(max_examples=50)
def test_domain_router_instantiation(instance):
    assert isinstance(instance, domain_Router)

@given(instance=domain_Hub_strategy)
@settings(max_examples=50)
def test_domain_hub_instantiation(instance):
    assert isinstance(instance, domain_Hub)

@given(instance=domain_Server_strategy)
@settings(max_examples=50)
def test_domain_server_instantiation(instance):
    assert isinstance(instance, domain_Server)

@given(instance=domain_EnterpriseInfrastructure_strategy)
@settings(max_examples=50)
def test_domain_enterpriseinfrastructure_instantiation(instance):
    assert isinstance(instance, domain_EnterpriseInfrastructure)



@given(instance=domain_EnterpriseInfrastructure_strategy)
def test_domain_enterpriseinfrastructure_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_InfrastructureConnection_strategy)
@settings(max_examples=50)
def test_domain_infrastructureconnection_instantiation(instance):
    assert isinstance(instance, domain_InfrastructureConnection)



@given(instance=domain_InfrastructureConnection_strategy)
def test_domain_infrastructureconnection_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Datacenter_strategy)
@settings(max_examples=50)
def test_domain_datacenter_instantiation(instance):
    assert isinstance(instance, domain_Datacenter)



@given(instance=domain_Datacenter_strategy)
def test_domain_datacenter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Datacenter_strategy)
def test_domain_datacenter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_OrderBy_strategy)
@settings(max_examples=50)
def test_domain_orderby_instantiation(instance):
    assert isinstance(instance, domain_OrderBy)



@given(instance=domain_OrderBy_strategy)
def test_domain_orderby_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=domain_OrderBy_strategy)
def test_domain_orderby_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Orders_strategy)
@settings(max_examples=50)
def test_domain_orders_instantiation(instance):
    assert isinstance(instance, domain_Orders)



@given(instance=domain_Orders_strategy)
def test_domain_orders_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ArtificialField_strategy)
@settings(max_examples=50)
def test_domain_artificialfield_instantiation(instance):
    assert isinstance(instance, domain_ArtificialField)



@given(instance=domain_ArtificialField_strategy)
def test_domain_artificialfield_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ArtificialField_strategy)
def test_domain_artificialfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_FormVariable_strategy)
@settings(max_examples=50)
def test_domain_formvariable_instantiation(instance):
    assert isinstance(instance, domain_FormVariable)



@given(instance=domain_FormVariable_strategy)
def test_domain_formvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_FormVariable_strategy)
def test_domain_formvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ProxiesList_strategy)
@settings(max_examples=50)
def test_proxieslist_instantiation(instance):
    assert isinstance(instance, ProxiesList)

@given(instance=domain_ProxiesList_strategy)
@settings(max_examples=50)
def test_domain_proxieslist_instantiation(instance):
    assert isinstance(instance, domain_ProxiesList)

@given(instance=MethodPointer_strategy)
@settings(max_examples=50)
def test_methodpointer_instantiation(instance):
    assert isinstance(instance, MethodPointer)

@given(instance=domain_Dependency_strategy)
@settings(max_examples=50)
def test_domain_dependency_instantiation(instance):
    assert isinstance(instance, domain_Dependency)



@given(instance=domain_Dependency_strategy)
def test_domain_dependency_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Dependency_strategy)
def test_domain_dependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Root_strategy)
@settings(max_examples=50)
def test_domain_root_instantiation(instance):
    assert isinstance(instance, domain_Root)



@given(instance=domain_Root_strategy)
def test_domain_root_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Root_strategy)
def test_domain_root_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ItemIcon_strategy)
@settings(max_examples=50)
def test_itemicon_instantiation(instance):
    assert isinstance(instance, ItemIcon)

@given(instance=domain_SubMenu_strategy)
@settings(max_examples=50)
def test_domain_submenu_instantiation(instance):
    assert isinstance(instance, domain_SubMenu)

@given(instance=domain_Relation_strategy)
@settings(max_examples=50)
def test_domain_relation_instantiation(instance):
    assert isinstance(instance, domain_Relation)



@given(instance=domain_Relation_strategy)
def test_domain_relation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Relation_strategy)
def test_domain_relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Relation_strategy)
def test_domain_relation_isTree_setter(instance):
    original = instance.isTree
    instance.isTree = original
    assert instance.isTree == original

@given(instance=OptionSelection_strategy)
@settings(max_examples=50)
def test_optionselection_instantiation(instance):
    assert isinstance(instance, OptionSelection)

@given(instance=domain_DropDownSelection_strategy)
@settings(max_examples=50)
def test_domain_dropdownselection_instantiation(instance):
    assert isinstance(instance, domain_DropDownSelection)



@given(instance=domain_DropDownSelection_strategy)
def test_domain_dropdownselection_initialOptionValue_setter(instance):
    original = instance.initialOptionValue
    instance.initialOptionValue = original
    assert instance.initialOptionValue == original

@given(instance=Formatable_strategy)
@settings(max_examples=50)
def test_formatable_instantiation(instance):
    assert isinstance(instance, Formatable)

@given(instance=ChildrenHolder_strategy)
@settings(max_examples=50)
def test_childrenholder_instantiation(instance):
    assert isinstance(instance, ChildrenHolder)

@given(instance=SourcesPointer_strategy)
@settings(max_examples=50)
def test_sourcespointer_instantiation(instance):
    assert isinstance(instance, SourcesPointer)

@given(instance=domain_DataControl_strategy)
@settings(max_examples=50)
def test_domain_datacontrol_instantiation(instance):
    assert isinstance(instance, domain_DataControl)



@given(instance=domain_DataControl_strategy)
def test_domain_datacontrol_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_DataControl_strategy)
def test_domain_datacontrol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Uielement_strategy)
@settings(max_examples=50)
def test_uielement_instantiation(instance):
    assert isinstance(instance, Uielement)

@given(instance=domain_Menu_strategy)
@settings(max_examples=50)
def test_domain_menu_instantiation(instance):
    assert isinstance(instance, domain_Menu)



@given(instance=domain_Menu_strategy)
def test_domain_menu_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original

@given(instance=domain_SourcesPointer_strategy)
@settings(max_examples=50)
def test_domain_sourcespointer_instantiation(instance):
    assert isinstance(instance, domain_SourcesPointer)

@given(instance=domain_Formatable_strategy)
@settings(max_examples=50)
def test_domain_formatable_instantiation(instance):
    assert isinstance(instance, domain_Formatable)



@given(instance=domain_Formatable_strategy)
def test_domain_formatable_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=domain_ItemIcon_strategy)
@settings(max_examples=50)
def test_domain_itemicon_instantiation(instance):
    assert isinstance(instance, domain_ItemIcon)

@given(instance=domain_AreaRef_strategy)
@settings(max_examples=50)
def test_domain_arearef_instantiation(instance):
    assert isinstance(instance, domain_AreaRef)



@given(instance=domain_AreaRef_strategy)
def test_domain_arearef_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=MenuHolder_strategy)
@settings(max_examples=50)
def test_menuholder_instantiation(instance):
    assert isinstance(instance, MenuHolder)

@given(instance=EnabledUIItem_strategy)
@settings(max_examples=50)
def test_enableduiitem_instantiation(instance):
    assert isinstance(instance, EnabledUIItem)

@given(instance=domain_EnabledUIItem_strategy)
@settings(max_examples=50)
def test_domain_enableduiitem_instantiation(instance):
    assert isinstance(instance, domain_EnabledUIItem)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=domain_FlexField_strategy)
@settings(max_examples=50)
def test_domain_flexfield_instantiation(instance):
    assert isinstance(instance, domain_FlexField)

@given(instance=domain_FlexFields_strategy)
@settings(max_examples=50)
def test_domain_flexfields_instantiation(instance):
    assert isinstance(instance, domain_FlexFields)

@given(instance=domain_NickNamed_strategy)
@settings(max_examples=50)
def test_domain_nicknamed_instantiation(instance):
    assert isinstance(instance, domain_NickNamed)



@given(instance=domain_NickNamed_strategy)
def test_domain_nicknamed_nickname_setter(instance):
    original = instance.nickname
    instance.nickname = original
    assert instance.nickname == original

@given(instance=InputElement_strategy)
@settings(max_examples=50)
def test_inputelement_instantiation(instance):
    assert isinstance(instance, InputElement)

@given(instance=domain_Image_strategy)
@settings(max_examples=50)
def test_domain_image_instantiation(instance):
    assert isinstance(instance, domain_Image)

@given(instance=domain_Password_strategy)
@settings(max_examples=50)
def test_domain_password_instantiation(instance):
    assert isinstance(instance, domain_Password)

@given(instance=domain_OutputText_strategy)
@settings(max_examples=50)
def test_domain_outputtext_instantiation(instance):
    assert isinstance(instance, domain_OutputText)

@given(instance=domain_Date_strategy)
@settings(max_examples=50)
def test_domain_date_instantiation(instance):
    assert isinstance(instance, domain_Date)

@given(instance=domain_InputText_strategy)
@settings(max_examples=50)
def test_domain_inputtext_instantiation(instance):
    assert isinstance(instance, domain_InputText)

@given(instance=domain_CheckBox_strategy)
@settings(max_examples=50)
def test_domain_checkbox_instantiation(instance):
    assert isinstance(instance, domain_CheckBox)

@given(instance=domain_OptionSelection_strategy)
@settings(max_examples=50)
def test_domain_optionselection_instantiation(instance):
    assert isinstance(instance, domain_OptionSelection)

@given(instance=domain_StyleElement_strategy)
@settings(max_examples=50)
def test_domain_styleelement_instantiation(instance):
    assert isinstance(instance, domain_StyleElement)

@given(instance=ContextParameters_strategy)
@settings(max_examples=50)
def test_contextparameters_instantiation(instance):
    assert isinstance(instance, ContextParameters)

@given(instance=domain_Trigger_strategy)
@settings(max_examples=50)
def test_domain_trigger_instantiation(instance):
    assert isinstance(instance, domain_Trigger)

@given(instance=ContextValue_strategy)
@settings(max_examples=50)
def test_contextvalue_instantiation(instance):
    assert isinstance(instance, ContextValue)

@given(instance=domain_StyleClass_strategy)
@settings(max_examples=50)
def test_domain_styleclass_instantiation(instance):
    assert isinstance(instance, domain_StyleClass)

@given(instance=domain_ContextParameters_strategy)
@settings(max_examples=50)
def test_domain_contextparameters_instantiation(instance):
    assert isinstance(instance, domain_ContextParameters)

@given(instance=domain_ExpressionPart_strategy)
@settings(max_examples=50)
def test_domain_expressionpart_instantiation(instance):
    assert isinstance(instance, domain_ExpressionPart)



@given(instance=domain_ExpressionPart_strategy)
def test_domain_expressionpart_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=domain_ExpressionPart_strategy)
def test_domain_expressionpart_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ExpressionPart_strategy)
def test_domain_expressionpart_expressionType_setter(instance):
    original = instance.expressionType
    instance.expressionType = original
    assert instance.expressionType == original

@given(instance=domain_ContextValue_strategy)
@settings(max_examples=50)
def test_domain_contextvalue_instantiation(instance):
    assert isinstance(instance, domain_ContextValue)



@given(instance=domain_ContextValue_strategy)
def test_domain_contextvalue_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=domain_ContextValue_strategy)
def test_domain_contextvalue_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ContextValue_strategy)
def test_domain_contextvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain_ContextParameter_strategy)
@settings(max_examples=50)
def test_domain_contextparameter_instantiation(instance):
    assert isinstance(instance, domain_ContextParameter)



@given(instance=domain_ContextParameter_strategy)
def test_domain_contextparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_ContextParameter_strategy)
def test_domain_contextparameter_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=domain_ChildrenHolder_strategy)
@settings(max_examples=50)
def test_domain_childrenholder_instantiation(instance):
    assert isinstance(instance, domain_ChildrenHolder)

@given(instance=domain_InputElement_strategy)
@settings(max_examples=50)
def test_domain_inputelement_instantiation(instance):
    assert isinstance(instance, domain_InputElement)

@given(instance=domain_LinkToMessage_strategy)
@settings(max_examples=50)
def test_domain_linktomessage_instantiation(instance):
    assert isinstance(instance, domain_LinkToMessage)



@given(instance=domain_LinkToMessage_strategy)
def test_domain_linktomessage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_LinkToLabel_strategy)
@settings(max_examples=50)
def test_domain_linktolabel_instantiation(instance):
    assert isinstance(instance, domain_LinkToLabel)



@given(instance=domain_LinkToLabel_strategy)
def test_domain_linktolabel_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_LayerHolder_strategy)
@settings(max_examples=50)
def test_domain_layerholder_instantiation(instance):
    assert isinstance(instance, domain_LayerHolder)

@given(instance=domain_Controls_strategy)
@settings(max_examples=50)
def test_domain_controls_instantiation(instance):
    assert isinstance(instance, domain_Controls)



@given(instance=domain_Controls_strategy)
def test_domain_controls_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=domain_UpdateTrigger_strategy)
@settings(max_examples=50)
def test_domain_updatetrigger_instantiation(instance):
    assert isinstance(instance, domain_UpdateTrigger)



@given(instance=domain_UpdateTrigger_strategy)
def test_domain_updatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_PREFormTrigger_strategy)
@settings(max_examples=50)
def test_domain_preformtrigger_instantiation(instance):
    assert isinstance(instance, domain_PREFormTrigger)



@given(instance=domain_PREFormTrigger_strategy)
def test_domain_preformtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_InsertTrigger_strategy)
@settings(max_examples=50)
def test_domain_inserttrigger_instantiation(instance):
    assert isinstance(instance, domain_InsertTrigger)



@given(instance=domain_InsertTrigger_strategy)
def test_domain_inserttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_POSTQueryTrigger_strategy)
@settings(max_examples=50)
def test_domain_postquerytrigger_instantiation(instance):
    assert isinstance(instance, domain_POSTQueryTrigger)



@given(instance=domain_POSTQueryTrigger_strategy)
def test_domain_postquerytrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_PREInsertTrigger_strategy)
@settings(max_examples=50)
def test_domain_preinserttrigger_instantiation(instance):
    assert isinstance(instance, domain_PREInsertTrigger)



@given(instance=domain_PREInsertTrigger_strategy)
def test_domain_preinserttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_PREQueryTrigger_strategy)
@settings(max_examples=50)
def test_domain_prequerytrigger_instantiation(instance):
    assert isinstance(instance, domain_PREQueryTrigger)



@given(instance=domain_PREQueryTrigger_strategy)
def test_domain_prequerytrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_DeleteTrigger_strategy)
@settings(max_examples=50)
def test_domain_deletetrigger_instantiation(instance):
    assert isinstance(instance, domain_DeleteTrigger)



@given(instance=domain_DeleteTrigger_strategy)
def test_domain_deletetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_CreateTrigger_strategy)
@settings(max_examples=50)
def test_domain_createtrigger_instantiation(instance):
    assert isinstance(instance, domain_CreateTrigger)



@given(instance=domain_CreateTrigger_strategy)
def test_domain_createtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_POSTCreateTrigger_strategy)
@settings(max_examples=50)
def test_domain_postcreatetrigger_instantiation(instance):
    assert isinstance(instance, domain_POSTCreateTrigger)



@given(instance=domain_POSTCreateTrigger_strategy)
def test_domain_postcreatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_SearchTrigger_strategy)
@settings(max_examples=50)
def test_domain_searchtrigger_instantiation(instance):
    assert isinstance(instance, domain_SearchTrigger)



@given(instance=domain_SearchTrigger_strategy)
def test_domain_searchtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_PREUpdateTrigger_strategy)
@settings(max_examples=50)
def test_domain_preupdatetrigger_instantiation(instance):
    assert isinstance(instance, domain_PREUpdateTrigger)



@given(instance=domain_PREUpdateTrigger_strategy)
def test_domain_preupdatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_PREDeleteTrigger_strategy)
@settings(max_examples=50)
def test_domain_predeletetrigger_instantiation(instance):
    assert isinstance(instance, domain_PREDeleteTrigger)



@given(instance=domain_PREDeleteTrigger_strategy)
def test_domain_predeletetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_CanvasView_strategy)
@settings(max_examples=50)
def test_domain_canvasview_instantiation(instance):
    assert isinstance(instance, domain_CanvasView)



@given(instance=domain_CanvasView_strategy)
def test_domain_canvasview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ViewPortTrigger_strategy)
@settings(max_examples=50)
def test_domain_viewporttrigger_instantiation(instance):
    assert isinstance(instance, domain_ViewPortTrigger)



@given(instance=domain_ViewPortTrigger_strategy)
def test_domain_viewporttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ViewElement_strategy)
@settings(max_examples=50)
def test_viewelement_instantiation(instance):
    assert isinstance(instance, ViewElement)

@given(instance=Orderable_strategy)
@settings(max_examples=50)
def test_orderable_instantiation(instance):
    assert isinstance(instance, Orderable)

@given(instance=domain_ViewPort_strategy)
@settings(max_examples=50)
def test_domain_viewport_instantiation(instance):
    assert isinstance(instance, domain_ViewPort)



@given(instance=domain_ViewPort_strategy)
def test_domain_viewport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ViewPort_strategy)
def test_domain_viewport_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ViewArea_strategy)
@settings(max_examples=50)
def test_domain_viewarea_instantiation(instance):
    assert isinstance(instance, domain_ViewArea)



@given(instance=domain_ViewArea_strategy)
def test_domain_viewarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ViewArea_strategy)
def test_domain_viewarea_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_MenuView_strategy)
@settings(max_examples=50)
def test_domain_menuview_instantiation(instance):
    assert isinstance(instance, domain_MenuView)



@given(instance=domain_MenuView_strategy)
def test_domain_menuview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=FlexFields_strategy)
@settings(max_examples=50)
def test_flexfields_instantiation(instance):
    assert isinstance(instance, FlexFields)

@given(instance=domain_MenuItem_strategy)
@settings(max_examples=50)
def test_domain_menuitem_instantiation(instance):
    assert isinstance(instance, domain_MenuItem)

@given(instance=MultiLangLabel_strategy)
@settings(max_examples=50)
def test_multilanglabel_instantiation(instance):
    assert isinstance(instance, MultiLangLabel)

@given(instance=domain_Tree_strategy)
@settings(max_examples=50)
def test_domain_tree_instantiation(instance):
    assert isinstance(instance, domain_Tree)



@given(instance=domain_Tree_strategy)
def test_domain_tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain_MessageElement_strategy)
@settings(max_examples=50)
def test_domain_messageelement_instantiation(instance):
    assert isinstance(instance, domain_MessageElement)



@given(instance=domain_MessageElement_strategy)
def test_domain_messageelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain_Table_strategy)
@settings(max_examples=50)
def test_domain_table_instantiation(instance):
    assert isinstance(instance, domain_Table)



@given(instance=domain_Table_strategy)
def test_domain_table_rowNumber_setter(instance):
    original = instance.rowNumber
    instance.rowNumber = original
    assert instance.rowNumber == original



@given(instance=domain_Table_strategy)
def test_domain_table_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain_Button_strategy)
@settings(max_examples=50)
def test_domain_button_instantiation(instance):
    assert isinstance(instance, domain_Button)



@given(instance=domain_Button_strategy)
def test_domain_button_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain_Label_strategy)
@settings(max_examples=50)
def test_domain_label_instantiation(instance):
    assert isinstance(instance, domain_Label)



@given(instance=domain_Label_strategy)
def test_domain_label_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=DefaultCavas_strategy)
@settings(max_examples=50)
def test_defaultcavas_instantiation(instance):
    assert isinstance(instance, DefaultCavas)

@given(instance=ViewPortHolder_strategy)
@settings(max_examples=50)
def test_viewportholder_instantiation(instance):
    assert isinstance(instance, ViewPortHolder)

@given(instance=CanvasFrame_strategy)
@settings(max_examples=50)
def test_canvasframe_instantiation(instance):
    assert isinstance(instance, CanvasFrame)

@given(instance=domain_Canvas_strategy)
@settings(max_examples=50)
def test_domain_canvas_instantiation(instance):
    assert isinstance(instance, domain_Canvas)

@given(instance=domain_TabPage_strategy)
@settings(max_examples=50)
def test_domain_tabpage_instantiation(instance):
    assert isinstance(instance, domain_TabPage)

@given(instance=domain_TabCanvas_strategy)
@settings(max_examples=50)
def test_domain_tabcanvas_instantiation(instance):
    assert isinstance(instance, domain_TabCanvas)



@given(instance=domain_TabCanvas_strategy)
def test_domain_tabcanvas_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=domain_PopupCanvas_strategy)
@settings(max_examples=50)
def test_domain_popupcanvas_instantiation(instance):
    assert isinstance(instance, domain_PopupCanvas)



@given(instance=domain_PopupCanvas_strategy)
def test_domain_popupcanvas_modal_setter(instance):
    original = instance.modal
    instance.modal = original
    assert instance.modal == original

@given(instance=NickNamed_strategy)
@settings(max_examples=50)
def test_nicknamed_instantiation(instance):
    assert isinstance(instance, NickNamed)

@given(instance=domain_DefaultCavas_strategy)
@settings(max_examples=50)
def test_domain_defaultcavas_instantiation(instance):
    assert isinstance(instance, domain_DefaultCavas)



@given(instance=domain_DefaultCavas_strategy)
def test_domain_defaultcavas_defaultCanvas_setter(instance):
    original = instance.defaultCanvas
    instance.defaultCanvas = original
    assert instance.defaultCanvas == original

@given(instance=domain_ViewPortHolder_strategy)
@settings(max_examples=50)
def test_domain_viewportholder_instantiation(instance):
    assert isinstance(instance, domain_ViewPortHolder)

@given(instance=StyleElement_strategy)
@settings(max_examples=50)
def test_styleelement_instantiation(instance):
    assert isinstance(instance, StyleElement)

@given(instance=domain_Uielement_strategy)
@settings(max_examples=50)
def test_domain_uielement_instantiation(instance):
    assert isinstance(instance, domain_Uielement)



@given(instance=domain_Uielement_strategy)
def test_domain_uielement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Selection_strategy)
@settings(max_examples=50)
def test_domain_selection_instantiation(instance):
    assert isinstance(instance, domain_Selection)

@given(instance=domain_Column_strategy)
@settings(max_examples=50)
def test_domain_column_instantiation(instance):
    assert isinstance(instance, domain_Column)



@given(instance=domain_Column_strategy)
def test_domain_column_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=domain_Column_strategy)
def test_domain_column_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_MenuFolder_strategy)
@settings(max_examples=50)
def test_domain_menufolder_instantiation(instance):
    assert isinstance(instance, domain_MenuFolder)



@given(instance=domain_MenuFolder_strategy)
def test_domain_menufolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_MenuFolder_strategy)
def test_domain_menufolder_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_MenuFolder_strategy)
def test_domain_menufolder_extensionPoint_setter(instance):
    original = instance.extensionPoint
    instance.extensionPoint = original
    assert instance.extensionPoint == original

@given(instance=domain_ViewElement_strategy)
@settings(max_examples=50)
def test_domain_viewelement_instantiation(instance):
    assert isinstance(instance, domain_ViewElement)

@given(instance=domain_MenuElement_strategy)
@settings(max_examples=50)
def test_domain_menuelement_instantiation(instance):
    assert isinstance(instance, domain_MenuElement)



@given(instance=domain_MenuElement_strategy)
def test_domain_menuelement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_MenuElement_strategy)
def test_domain_menuelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Context_strategy)
@settings(max_examples=50)
def test_domain_context_instantiation(instance):
    assert isinstance(instance, domain_Context)

@given(instance=domain_MultiLangLabel_strategy)
@settings(max_examples=50)
def test_domain_multilanglabel_instantiation(instance):
    assert isinstance(instance, domain_MultiLangLabel)

@given(instance=domain_Orderable_strategy)
@settings(max_examples=50)
def test_domain_orderable_instantiation(instance):
    assert isinstance(instance, domain_Orderable)



@given(instance=domain_Orderable_strategy)
def test_domain_orderable_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=domain_MenuDefinition_strategy)
@settings(max_examples=50)
def test_domain_menudefinition_instantiation(instance):
    assert isinstance(instance, domain_MenuDefinition)



@given(instance=domain_MenuDefinition_strategy)
def test_domain_menudefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_MenuDefinition_strategy)
def test_domain_menudefinition_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_TabPagesInheritance_strategy)
@settings(max_examples=50)
def test_domain_tabpagesinheritance_instantiation(instance):
    assert isinstance(instance, domain_TabPagesInheritance)



@given(instance=domain_TabPagesInheritance_strategy)
def test_domain_tabpagesinheritance_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_ViewInheritance_strategy)
@settings(max_examples=50)
def test_domain_viewinheritance_instantiation(instance):
    assert isinstance(instance, domain_ViewInheritance)



@given(instance=domain_ViewInheritance_strategy)
def test_domain_viewinheritance_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_CanvasFrame_strategy)
@settings(max_examples=50)
def test_domain_canvasframe_instantiation(instance):
    assert isinstance(instance, domain_CanvasFrame)



@given(instance=domain_CanvasFrame_strategy)
def test_domain_canvasframe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_CanvasFrame_strategy)
def test_domain_canvasframe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Views_strategy)
@settings(max_examples=50)
def test_domain_views_instantiation(instance):
    assert isinstance(instance, domain_Views)



@given(instance=domain_Views_strategy)
def test_domain_views_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_FormParameter_strategy)
@settings(max_examples=50)
def test_domain_formparameter_instantiation(instance):
    assert isinstance(instance, domain_FormParameter)



@given(instance=domain_FormParameter_strategy)
def test_domain_formparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_FormParameter_strategy)
def test_domain_formparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_FormDataControls_strategy)
@settings(max_examples=50)
def test_domain_formdatacontrols_instantiation(instance):
    assert isinstance(instance, domain_FormDataControls)



@given(instance=domain_FormDataControls_strategy)
def test_domain_formdatacontrols_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_FormDataControls_strategy)
def test_domain_formdatacontrols_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_FormView_strategy)
@settings(max_examples=50)
def test_domain_formview_instantiation(instance):
    assert isinstance(instance, domain_FormView)



@given(instance=domain_FormView_strategy)
def test_domain_formview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_FormView_strategy)
def test_domain_formview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Form_strategy)
@settings(max_examples=50)
def test_domain_form_instantiation(instance):
    assert isinstance(instance, domain_Form)



@given(instance=domain_Form_strategy)
def test_domain_form_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Form_strategy)
def test_domain_form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_Types_strategy)
@settings(max_examples=50)
def test_domain_types_instantiation(instance):
    assert isinstance(instance, domain_Types)



@given(instance=domain_Types_strategy)
def test_domain_types_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Types_strategy)
def test_domain_types_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_EnumAttribute_strategy)
@settings(max_examples=50)
def test_domain_enumattribute_instantiation(instance):
    assert isinstance(instance, domain_EnumAttribute)



@given(instance=domain_EnumAttribute_strategy)
def test_domain_enumattribute_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_EnumAttribute_strategy)
def test_domain_enumattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=domain_EnumAttribute_strategy)
def test_domain_enumattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_ReturnValue_strategy)
@settings(max_examples=50)
def test_domain_returnvalue_instantiation(instance):
    assert isinstance(instance, domain_ReturnValue)



@given(instance=domain_ReturnValue_strategy)
def test_domain_returnvalue_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Parameter_strategy)
@settings(max_examples=50)
def test_domain_parameter_instantiation(instance):
    assert isinstance(instance, domain_Parameter)



@given(instance=domain_Parameter_strategy)
def test_domain_parameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Parameter_strategy)
def test_domain_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Parameter_strategy)
def test_domain_parameter_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=Secured_strategy)
@settings(max_examples=50)
def test_secured_instantiation(instance):
    assert isinstance(instance, Secured)

@given(instance=domain_Window_strategy)
@settings(max_examples=50)
def test_domain_window_instantiation(instance):
    assert isinstance(instance, domain_Window)

@given(instance=domain_Operation_strategy)
@settings(max_examples=50)
def test_domain_operation_instantiation(instance):
    assert isinstance(instance, domain_Operation)



@given(instance=domain_Operation_strategy)
def test_domain_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Operation_strategy)
def test_domain_operation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=TypeElement_strategy)
@settings(max_examples=50)
def test_typeelement_instantiation(instance):
    assert isinstance(instance, TypeElement)

@given(instance=domain_Type_strategy)
@settings(max_examples=50)
def test_domain_type_instantiation(instance):
    assert isinstance(instance, domain_Type)

@given(instance=domain_TypeReference_strategy)
@settings(max_examples=50)
def test_domain_typereference_instantiation(instance):
    assert isinstance(instance, domain_TypeReference)

@given(instance=domain_Enumarator_strategy)
@settings(max_examples=50)
def test_domain_enumarator_instantiation(instance):
    assert isinstance(instance, domain_Enumarator)

@given(instance=domain_Primitive_strategy)
@settings(max_examples=50)
def test_domain_primitive_instantiation(instance):
    assert isinstance(instance, domain_Primitive)

@given(instance=domain_Attribute_strategy)
@settings(max_examples=50)
def test_domain_attribute_instantiation(instance):
    assert isinstance(instance, domain_Attribute)



@given(instance=domain_Attribute_strategy)
def test_domain_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_Attribute_strategy)
def test_domain_attribute_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Attribute_strategy)
def test_domain_attribute_pk_setter(instance):
    original = instance.pk
    instance.pk = original
    assert instance.pk == original

@given(instance=domain_Link_strategy)
@settings(max_examples=50)
def test_domain_link_instantiation(instance):
    assert isinstance(instance, domain_Link)



@given(instance=domain_Link_strategy)
def test_domain_link_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=RelationShip_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, RelationShip)

@given(instance=domain_Generalization_strategy)
@settings(max_examples=50)
def test_domain_generalization_instantiation(instance):
    assert isinstance(instance, domain_Generalization)

@given(instance=domain_Assosiation_strategy)
@settings(max_examples=50)
def test_domain_assosiation_instantiation(instance):
    assert isinstance(instance, domain_Assosiation)



@given(instance=domain_Assosiation_strategy)
def test_domain_assosiation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=domain_References_strategy)
@settings(max_examples=50)
def test_domain_references_instantiation(instance):
    assert isinstance(instance, domain_References)

@given(instance=domain_RelationShip_strategy)
@settings(max_examples=50)
def test_domain_relationship_instantiation(instance):
    assert isinstance(instance, domain_RelationShip)



@given(instance=domain_RelationShip_strategy)
def test_domain_relationship_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_TypeElement_strategy)
@settings(max_examples=50)
def test_domain_typeelement_instantiation(instance):
    assert isinstance(instance, domain_TypeElement)



@given(instance=domain_TypeElement_strategy)
def test_domain_typeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_TypeElement_strategy)
def test_domain_typeelement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Package_strategy)
@settings(max_examples=50)
def test_domain_package_instantiation(instance):
    assert isinstance(instance, domain_Package)



@given(instance=domain_Package_strategy)
def test_domain_package_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Package_strategy)
def test_domain_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_TypePointer_strategy)
@settings(max_examples=50)
def test_domain_typepointer_instantiation(instance):
    assert isinstance(instance, domain_TypePointer)



@given(instance=domain_TypePointer_strategy)
def test_domain_typepointer_fakeTypeName_setter(instance):
    original = instance.fakeTypeName
    instance.fakeTypeName = original
    assert instance.fakeTypeName == original



@given(instance=domain_TypePointer_strategy)
def test_domain_typepointer_fakePackageName_setter(instance):
    original = instance.fakePackageName
    instance.fakePackageName = original
    assert instance.fakePackageName == original

@given(instance=domain_ArtifactRef_strategy)
@settings(max_examples=50)
def test_domain_artifactref_instantiation(instance):
    assert isinstance(instance, domain_ArtifactRef)



@given(instance=domain_ArtifactRef_strategy)
def test_domain_artifactref_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_QueryVariable_strategy)
@settings(max_examples=50)
def test_domain_queryvariable_instantiation(instance):
    assert isinstance(instance, domain_QueryVariable)



@given(instance=domain_QueryVariable_strategy)
def test_domain_queryvariable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=domain_QueryVariable_strategy)
def test_domain_queryvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_KeyValuePair_strategy)
@settings(max_examples=50)
def test_domain_keyvaluepair_instantiation(instance):
    assert isinstance(instance, domain_KeyValuePair)



@given(instance=domain_KeyValuePair_strategy)
def test_domain_keyvaluepair_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=domain_KeyValuePair_strategy)
def test_domain_keyvaluepair_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=domain_KeyValuePair_strategy)
def test_domain_keyvaluepair_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_TypeDefinition_strategy)
@settings(max_examples=50)
def test_domain_typedefinition_instantiation(instance):
    assert isinstance(instance, domain_TypeDefinition)



@given(instance=domain_TypeDefinition_strategy)
def test_domain_typedefinition_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Query_strategy)
@settings(max_examples=50)
def test_domain_query_instantiation(instance):
    assert isinstance(instance, domain_Query)



@given(instance=domain_Query_strategy)
def test_domain_query_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Query_strategy)
def test_domain_query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain_MappingSpecifier_strategy)
@settings(max_examples=50)
def test_domain_mappingspecifier_instantiation(instance):
    assert isinstance(instance, domain_MappingSpecifier)



@given(instance=domain_MappingSpecifier_strategy)
def test_domain_mappingspecifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ArtifactRef_strategy)
@settings(max_examples=50)
def test_artifactref_instantiation(instance):
    assert isinstance(instance, ArtifactRef)

@given(instance=domain_ModelMapper_strategy)
@settings(max_examples=50)
def test_domain_modelmapper_instantiation(instance):
    assert isinstance(instance, domain_ModelMapper)



@given(instance=domain_ModelMapper_strategy)
def test_domain_modelmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domain_ModelMapper_strategy)
def test_domain_modelmapper_artifactRoot_setter(instance):
    original = instance.artifactRoot
    instance.artifactRoot = original
    assert instance.artifactRoot == original



@given(instance=domain_ModelMapper_strategy)
def test_domain_modelmapper_artifactExecutionString_setter(instance):
    original = instance.artifactExecutionString
    instance.artifactExecutionString = original
    assert instance.artifactExecutionString == original

@given(instance=domain_HashProperty_strategy)
@settings(max_examples=50)
def test_domain_hashproperty_instantiation(instance):
    assert isinstance(instance, domain_HashProperty)



@given(instance=domain_HashProperty_strategy)
def test_domain_hashproperty_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original



@given(instance=domain_HashProperty_strategy)
def test_domain_hashproperty_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain_Property_strategy)
@settings(max_examples=50)
def test_domain_property_instantiation(instance):
    assert isinstance(instance, domain_Property)



@given(instance=domain_Property_strategy)
def test_domain_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=domain_Property_strategy)
def test_domain_property_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=domain_Property_strategy)
def test_domain_property_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=domain_JavaComponent_strategy)
@settings(max_examples=50)
def test_domain_javacomponent_instantiation(instance):
    assert isinstance(instance, domain_JavaComponent)



@given(instance=domain_JavaComponent_strategy)
def test_domain_javacomponent_basePackage_setter(instance):
    original = instance.basePackage
    instance.basePackage = original
    assert instance.basePackage == original



@given(instance=domain_JavaComponent_strategy)
def test_domain_javacomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=domain_JavaComponent_strategy)
def test_domain_javacomponent_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=domain_JavaComponent_strategy)
def test_domain_javacomponent_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original
