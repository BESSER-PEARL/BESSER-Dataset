import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MappingType,
    softGalleryLanguage_RequestMapping,
    softGalleryLanguage_SpringEntity,
    softGalleryLanguage_ResponseParameter,
    softGalleryLanguage_MappingType,
    softGalleryLanguage_ResponseEntity,
    softGalleryLanguage_Autowired,
    softGalleryLanguage_SearchCriteria,
    softGalleryLanguage_Predicate,
    softGalleryLanguage_Specification,
    softGalleryLanguage_RestController,
    softGalleryLanguage_SpringRepositoryAnnotation,
    softGalleryLanguage_SpringRepositories,
    softGalleryLanguage_SpringRepository,
    softGalleryLanguage_OrderSpring,
    softGalleryLanguage_SpringComponent,
    softGalleryLanguage_EnableWebSecurity,
    softGalleryLanguage_EnableResourceServer,
    softGalleryLanguage_EnableAuthorizationServer,
    softGalleryLanguage_EnableGlobalMethodSecurity,
    softGalleryLanguage_Configuration,
    softGalleryLanguage_SpringBootApplication,
    softGalleryLanguage_AmazonWebServices,
    softGalleryLanguage_PostgreSQL,
    softGalleryLanguage_React,
    softGalleryLanguage_Spring,
    softGalleryLanguage_Technologies,
    softGalleryLanguage_NTiersRelations,
    softGalleryLanguage_NTierTarget,
    softGalleryLanguage_NTierSource,
    softGalleryLanguage_NTierConnectionContent,
    softGalleryLanguage_NTiersConnections,
    softGalleryLanguage_PersistenceDataComponent,
    softGalleryLanguage_BackEnd,
    softGalleryLanguage_FrontEnd,
    softGalleryLanguage_ArchitectureComponents,
    softGalleryLanguage_LayerTarget,
    softGalleryLanguage_LayerSource,
    softGalleryLanguage_Technology,
    softGalleryLanguage_SingleFile,
    softGalleryLanguage_MultipleFile,
    softGalleryLanguage_Directories,
    softGalleryLanguage_DirectoryContent,
    softGalleryLanguage_SegmentStructureContent,
    softGalleryLanguage_SegmentStructure,
    softGalleryLanguage_DataPersistenceSegments,
    softGalleryLanguage_DataPersistenceContent,
    softGalleryLanguage_DataPersistenceLayer,
    softGalleryLanguage_CriteriaAttributeType,
    softGalleryLanguage_SpecificationSegmentElement,
    softGalleryLanguage_ControllerSegmentElement,
    softGalleryLanguage_LayerRelations,
    softGalleryLanguage_BusinessLogicSegments,
    softGalleryLanguage_BusinessLogicContent,
    softGalleryLanguage_BusinessLogicLayer,
    softGalleryLanguage_PresentationSegments,
    softGalleryLanguage_PresentationContent,
    softGalleryLanguage_PresentationLayer,
    softGalleryLanguage_Layer,
    softGalleryLanguage_NTiers,
    softGalleryLanguage_Architecture,
    softGalleryLanguage_UserException,
    softGalleryLanguage_AlbumException,
    softGalleryLanguage_PhotoException,
    softGalleryLanguage_LandingFunctions,
    softGalleryLanguage_PhotoActionsFunctions,
    softGalleryLanguage_AlbumManagementFunctions,
    softGalleryLanguage_ExceptionsType,
    softGalleryLanguage_AppAccessFunctions,
    softGalleryLanguage_ProfileManagementFunctions,
    softGalleryLanguage_LandingActions,
    softGalleryLanguage_PhotoActions,
    softGalleryLanguage_AlbumManagement,
    softGalleryLanguage_AppAccess,
    softGalleryLanguage_ProfileManagement,
    softGalleryLanguage_Functionalities,
    softGalleryLanguage_AtributeUserDomain,
    softGalleryLanguage_AtributeAlbum,
    softGalleryLanguage_AtributePhoto,
    softGalleryLanguage_Entities,
    softGalleryLanguage_ExceptionsDomain,
    softGalleryLanguage_Functionality,
    softGalleryLanguage_Entity,
    softGalleryLanguage_Domain,
    softGalleryLanguage_EObject,
    softGalleryLanguage_Model,
    softGalleryLanguage_AmazonElasticComputeCloud,
    softGalleryLanguage_Metadata,
    softGalleryLanguage_AmazonFile,
    softGalleryLanguage_AmazonFolder,
    softGalleryLanguage_OnlyAuthorized,
    softGalleryLanguage_BucketObjectsNotPublic,
    softGalleryLanguage_ObjectsPublic,
    softGalleryLanguage_BucketAccess,
    softGalleryLanguage_Bucket,
    softGalleryLanguage_BatchOperation,
    softGalleryLanguage_AmazonSimpleStorageService,
    softGalleryLanguage_Clause,
    softGalleryLanguage_Query,
    softGalleryLanguage_Privilege,
    softGalleryLanguage_PostgresUser,
    softGalleryLanguage_Function,
    softGalleryLanguage_Trigger,
    softGalleryLanguage_Policy,
    softGalleryLanguage_PublicAccess,
    softGalleryLanguage_Constraint,
    softGalleryLanguage_DatatypeDB,
    softGalleryLanguage_ColumnP,
    softGalleryLanguage_RefTable_p,
    softGalleryLanguage_ForeignKeyRef,
    softGalleryLanguage_ForeignKey_n,
    softGalleryLanguage_ForeignKey,
    softGalleryLanguage_Table_p,
    softGalleryLanguage_ViewSchema,
    softGalleryLanguage_Index_p,
    softGalleryLanguage_Schema,
    softGalleryLanguage_Database,
    softGalleryLanguage_Cluster,
    softGalleryLanguage_Row,
    softGalleryLanguage_ReactInformation,
    softGalleryLanguage_ReactLibrary,
    softGalleryLanguage_ReactsRelationServ,
    softGalleryLanguage_ReactServiceRequestProps,
    softGalleryLanguage_ReactServiceContRequest,
    softGalleryLanguage_ReactServiceContent,
    softGalleryLanguage_ReactServicesType,
    softGalleryLanguage_ReactServicesRelation,
    softGalleryLanguage_ReactActionsContent,
    softGalleryLanguage_StylePropertiesContent,
    softGalleryLanguage_ComponentsStylesContent,
    softGalleryLanguage_PropsType,
    softGalleryLanguage_StateContent,
    softGalleryLanguage_CoreFunctionsDeclaration,
    softGalleryLanguage_State,
    softGalleryLanguage_ReactCoreFunctions,
    softGalleryLanguage_ReactConstructor,
    softGalleryLanguage_ReactImportContent,
    softGalleryLanguage_StyleProperties,
    softGalleryLanguage_Props,
    softGalleryLanguage_ReactFunctions,
    softGalleryLanguage_ReactImports,
    softGalleryLanguage_SubcomponentCont,
    softGalleryLanguage_ViewComponentCont,
    softGalleryLanguage_UIContent,
    softGalleryLanguage_ComponentClass,
    softGalleryLanguage_LogicStructure,
    softGalleryLanguage_LogicContent,
    softGalleryLanguage_ComponentsStyles,
    softGalleryLanguage_ComponentsLogic,
    softGalleryLanguage_DOMConfigurations,
    softGalleryLanguage_PackageVersion,
    softGalleryLanguage_PackageName,
    softGalleryLanguage_SingleDependencies,
    softGalleryLanguage_ReactDependenciesSubRules,
    softGalleryLanguage_ReactDependenciesRules,
    softGalleryLanguage_ReactConfigurations,
    softGalleryLanguage_ReactDependencies,
    softGalleryLanguage_ReactInfo,
    softGalleryLanguage_ReactLibraries,
    softGalleryLanguage_ReactActions,
    softGalleryLanguage_ComponentsUI,
    softGalleryLanguage_ReactConfiguration,
    softGalleryLanguage_ReactSubModules,
    softGalleryLanguage_ReactModules,
    softGalleryLanguage_StorageActionMemberName,
    softGalleryLanguage_StorageActionMemberType,
    softGalleryLanguage_StorageActionMember,
    softGalleryLanguage_StorageActionReturn,
    softGalleryLanguage_StorageActionAnnotation,
    softGalleryLanguage_StorageAction,
    softGalleryLanguage_StorageMemberAnnotation,
    softGalleryLanguage_StorageMemberType,
    softGalleryLanguage_StorageMember,
    softGalleryLanguage_StorageClient,
    softGalleryLanguage_SpringEntityAnnotationTypes,
    softGalleryLanguage_ReactComponents,
    softGalleryLanguage_ExceptionProcess,
    softGalleryLanguage_ExceptionHandler,
    softGalleryLanguage_ResponseParameterName,
    softGalleryLanguage_ResponseParameterType,
    softGalleryLanguage_ResponseParameterAnnotation,
    softGalleryLanguage_DeleteMapping,
    softGalleryLanguage_PutMapping,
    softGalleryLanguage_GetMapping,
    softGalleryLanguage_PostMapping,
    softGalleryLanguage_RequestMappingProduces,
    softGalleryLanguage_RequestMappingMethod,
    softGalleryLanguage_RequestMappingValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mappingtype_is_not_abstract():
    assert not inspect.isabstract(MappingType)


def test_mappingtype_constructor_exists():
    assert callable(MappingType.__init__)


def test_mappingtype_constructor_args():
    sig = inspect.signature(MappingType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_requestmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RequestMapping)


def test_softgallerylanguage_requestmapping_constructor_exists():
    assert callable(softGalleryLanguage_RequestMapping.__init__)


def test_softgallerylanguage_requestmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RequestMapping.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_springentity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringEntity)


def test_softgallerylanguage_springentity_constructor_exists():
    assert callable(softGalleryLanguage_SpringEntity.__init__)


def test_softgallerylanguage_springentity_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringEntity.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_responseparameter_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ResponseParameter)


def test_softgallerylanguage_responseparameter_constructor_exists():
    assert callable(softGalleryLanguage_ResponseParameter.__init__)


def test_softgallerylanguage_responseparameter_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ResponseParameter.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_mappingtype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_MappingType)


def test_softgallerylanguage_mappingtype_constructor_exists():
    assert callable(softGalleryLanguage_MappingType.__init__)


def test_softgallerylanguage_mappingtype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_MappingType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_responseentity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ResponseEntity)


def test_softgallerylanguage_responseentity_constructor_exists():
    assert callable(softGalleryLanguage_ResponseEntity.__init__)


def test_softgallerylanguage_responseentity_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ResponseEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_responseentity_has_name():
    assert hasattr(softGalleryLanguage_ResponseEntity, "name")
    descriptor = None
    for klass in softGalleryLanguage_ResponseEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_autowired_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Autowired)


def test_softgallerylanguage_autowired_constructor_exists():
    assert callable(softGalleryLanguage_Autowired.__init__)


def test_softgallerylanguage_autowired_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Autowired.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_autowired_has_name():
    assert hasattr(softGalleryLanguage_Autowired, "name")
    descriptor = None
    for klass in softGalleryLanguage_Autowired.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_searchcriteria_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SearchCriteria)


def test_softgallerylanguage_searchcriteria_constructor_exists():
    assert callable(softGalleryLanguage_SearchCriteria.__init__)


def test_softgallerylanguage_searchcriteria_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SearchCriteria.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_searchcriteria_has_name():
    assert hasattr(softGalleryLanguage_SearchCriteria, "name")
    descriptor = None
    for klass in softGalleryLanguage_SearchCriteria.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_predicate_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Predicate)


def test_softgallerylanguage_predicate_constructor_exists():
    assert callable(softGalleryLanguage_Predicate.__init__)


def test_softgallerylanguage_predicate_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_predicate_has_name():
    assert hasattr(softGalleryLanguage_Predicate, "name")
    descriptor = None
    for klass in softGalleryLanguage_Predicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_specification_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Specification)


def test_softgallerylanguage_specification_constructor_exists():
    assert callable(softGalleryLanguage_Specification.__init__)


def test_softgallerylanguage_specification_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Specification.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_restcontroller_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RestController)


def test_softgallerylanguage_restcontroller_constructor_exists():
    assert callable(softGalleryLanguage_RestController.__init__)


def test_softgallerylanguage_restcontroller_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RestController.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_restcontroller_has_name():
    assert hasattr(softGalleryLanguage_RestController, "name")
    descriptor = None
    for klass in softGalleryLanguage_RestController.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_springrepositoryannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringRepositoryAnnotation)


def test_softgallerylanguage_springrepositoryannotation_constructor_exists():
    assert callable(softGalleryLanguage_SpringRepositoryAnnotation.__init__)


def test_softgallerylanguage_springrepositoryannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringRepositoryAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_springrepositoryannotation_has_name():
    assert hasattr(softGalleryLanguage_SpringRepositoryAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage_SpringRepositoryAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_springrepositories_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringRepositories)


def test_softgallerylanguage_springrepositories_constructor_exists():
    assert callable(softGalleryLanguage_SpringRepositories.__init__)


def test_softgallerylanguage_springrepositories_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringRepositories.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_springrepositories_has_name():
    assert hasattr(softGalleryLanguage_SpringRepositories, "name")
    descriptor = None
    for klass in softGalleryLanguage_SpringRepositories.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_springrepository_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringRepository)


def test_softgallerylanguage_springrepository_constructor_exists():
    assert callable(softGalleryLanguage_SpringRepository.__init__)


def test_softgallerylanguage_springrepository_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringRepository.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_orderspring_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_OrderSpring)


def test_softgallerylanguage_orderspring_constructor_exists():
    assert callable(softGalleryLanguage_OrderSpring.__init__)


def test_softgallerylanguage_orderspring_constructor_args():
    sig = inspect.signature(softGalleryLanguage_OrderSpring.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_orderspring_has_name():
    assert hasattr(softGalleryLanguage_OrderSpring, "name")
    descriptor = None
    for klass in softGalleryLanguage_OrderSpring.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_springcomponent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringComponent)


def test_softgallerylanguage_springcomponent_constructor_exists():
    assert callable(softGalleryLanguage_SpringComponent.__init__)


def test_softgallerylanguage_springcomponent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringComponent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_enablewebsecurity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_EnableWebSecurity)


def test_softgallerylanguage_enablewebsecurity_constructor_exists():
    assert callable(softGalleryLanguage_EnableWebSecurity.__init__)


def test_softgallerylanguage_enablewebsecurity_constructor_args():
    sig = inspect.signature(softGalleryLanguage_EnableWebSecurity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_enablewebsecurity_has_name():
    assert hasattr(softGalleryLanguage_EnableWebSecurity, "name")
    descriptor = None
    for klass in softGalleryLanguage_EnableWebSecurity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_enableresourceserver_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_EnableResourceServer)


def test_softgallerylanguage_enableresourceserver_constructor_exists():
    assert callable(softGalleryLanguage_EnableResourceServer.__init__)


def test_softgallerylanguage_enableresourceserver_constructor_args():
    sig = inspect.signature(softGalleryLanguage_EnableResourceServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_enableresourceserver_has_name():
    assert hasattr(softGalleryLanguage_EnableResourceServer, "name")
    descriptor = None
    for klass in softGalleryLanguage_EnableResourceServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_enableauthorizationserver_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_EnableAuthorizationServer)


def test_softgallerylanguage_enableauthorizationserver_constructor_exists():
    assert callable(softGalleryLanguage_EnableAuthorizationServer.__init__)


def test_softgallerylanguage_enableauthorizationserver_constructor_args():
    sig = inspect.signature(softGalleryLanguage_EnableAuthorizationServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_enableauthorizationserver_has_name():
    assert hasattr(softGalleryLanguage_EnableAuthorizationServer, "name")
    descriptor = None
    for klass in softGalleryLanguage_EnableAuthorizationServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_enableglobalmethodsecurity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_EnableGlobalMethodSecurity)


def test_softgallerylanguage_enableglobalmethodsecurity_constructor_exists():
    assert callable(softGalleryLanguage_EnableGlobalMethodSecurity.__init__)


def test_softgallerylanguage_enableglobalmethodsecurity_constructor_args():
    sig = inspect.signature(softGalleryLanguage_EnableGlobalMethodSecurity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_enableglobalmethodsecurity_has_name():
    assert hasattr(softGalleryLanguage_EnableGlobalMethodSecurity, "name")
    descriptor = None
    for klass in softGalleryLanguage_EnableGlobalMethodSecurity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_configuration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Configuration)


def test_softgallerylanguage_configuration_constructor_exists():
    assert callable(softGalleryLanguage_Configuration.__init__)


def test_softgallerylanguage_configuration_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_springbootapplication_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringBootApplication)


def test_softgallerylanguage_springbootapplication_constructor_exists():
    assert callable(softGalleryLanguage_SpringBootApplication.__init__)


def test_softgallerylanguage_springbootapplication_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringBootApplication.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_amazonwebservices_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AmazonWebServices)


def test_softgallerylanguage_amazonwebservices_constructor_exists():
    assert callable(softGalleryLanguage_AmazonWebServices.__init__)


def test_softgallerylanguage_amazonwebservices_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AmazonWebServices.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_amazonwebservices_has_name():
    assert hasattr(softGalleryLanguage_AmazonWebServices, "name")
    descriptor = None
    for klass in softGalleryLanguage_AmazonWebServices.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_postgresql_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PostgreSQL)


def test_softgallerylanguage_postgresql_constructor_exists():
    assert callable(softGalleryLanguage_PostgreSQL.__init__)


def test_softgallerylanguage_postgresql_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PostgreSQL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_postgresql_has_name():
    assert hasattr(softGalleryLanguage_PostgreSQL, "name")
    descriptor = None
    for klass in softGalleryLanguage_PostgreSQL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_react_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_React)


def test_softgallerylanguage_react_constructor_exists():
    assert callable(softGalleryLanguage_React.__init__)


def test_softgallerylanguage_react_constructor_args():
    sig = inspect.signature(softGalleryLanguage_React.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_react_has_name():
    assert hasattr(softGalleryLanguage_React, "name")
    descriptor = None
    for klass in softGalleryLanguage_React.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_spring_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Spring)


def test_softgallerylanguage_spring_constructor_exists():
    assert callable(softGalleryLanguage_Spring.__init__)


def test_softgallerylanguage_spring_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Spring.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_spring_has_name():
    assert hasattr(softGalleryLanguage_Spring, "name")
    descriptor = None
    for klass in softGalleryLanguage_Spring.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_technologies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Technologies)


def test_softgallerylanguage_technologies_constructor_exists():
    assert callable(softGalleryLanguage_Technologies.__init__)


def test_softgallerylanguage_technologies_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Technologies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_ntiersrelations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTiersRelations)


def test_softgallerylanguage_ntiersrelations_constructor_exists():
    assert callable(softGalleryLanguage_NTiersRelations.__init__)


def test_softgallerylanguage_ntiersrelations_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTiersRelations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_ntiersrelations_has_name():
    assert hasattr(softGalleryLanguage_NTiersRelations, "name")
    descriptor = None
    for klass in softGalleryLanguage_NTiersRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_ntiertarget_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTierTarget)


def test_softgallerylanguage_ntiertarget_constructor_exists():
    assert callable(softGalleryLanguage_NTierTarget.__init__)


def test_softgallerylanguage_ntiertarget_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTierTarget.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_ntiersource_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTierSource)


def test_softgallerylanguage_ntiersource_constructor_exists():
    assert callable(softGalleryLanguage_NTierSource.__init__)


def test_softgallerylanguage_ntiersource_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTierSource.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_ntierconnectioncontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTierConnectionContent)


def test_softgallerylanguage_ntierconnectioncontent_constructor_exists():
    assert callable(softGalleryLanguage_NTierConnectionContent.__init__)


def test_softgallerylanguage_ntierconnectioncontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTierConnectionContent.__init__)
    params = list(sig.parameters.keys())
    assert "nTierName" in params, "Missing parameter 'nTierName'"
    assert "ntierconnection" in params, "Missing parameter 'ntierconnection'"

def test_softgallerylanguage_ntierconnectioncontent_has_nTierName():
    assert hasattr(softGalleryLanguage_NTierConnectionContent, "nTierName")
    descriptor = None
    for klass in softGalleryLanguage_NTierConnectionContent.__mro__:
        if "nTierName" in klass.__dict__:
            descriptor = klass.__dict__["nTierName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_ntierconnectioncontent_has_ntierconnection():
    assert hasattr(softGalleryLanguage_NTierConnectionContent, "ntierconnection")
    descriptor = None
    for klass in softGalleryLanguage_NTierConnectionContent.__mro__:
        if "ntierconnection" in klass.__dict__:
            descriptor = klass.__dict__["ntierconnection"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_ntiersconnections_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTiersConnections)


def test_softgallerylanguage_ntiersconnections_constructor_exists():
    assert callable(softGalleryLanguage_NTiersConnections.__init__)


def test_softgallerylanguage_ntiersconnections_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTiersConnections.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_persistencedatacomponent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PersistenceDataComponent)


def test_softgallerylanguage_persistencedatacomponent_constructor_exists():
    assert callable(softGalleryLanguage_PersistenceDataComponent.__init__)


def test_softgallerylanguage_persistencedatacomponent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PersistenceDataComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_persistencedatacomponent_has_name():
    assert hasattr(softGalleryLanguage_PersistenceDataComponent, "name")
    descriptor = None
    for klass in softGalleryLanguage_PersistenceDataComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_backend_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BackEnd)


def test_softgallerylanguage_backend_constructor_exists():
    assert callable(softGalleryLanguage_BackEnd.__init__)


def test_softgallerylanguage_backend_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BackEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_backend_has_name():
    assert hasattr(softGalleryLanguage_BackEnd, "name")
    descriptor = None
    for klass in softGalleryLanguage_BackEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_frontend_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_FrontEnd)


def test_softgallerylanguage_frontend_constructor_exists():
    assert callable(softGalleryLanguage_FrontEnd.__init__)


def test_softgallerylanguage_frontend_constructor_args():
    sig = inspect.signature(softGalleryLanguage_FrontEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_frontend_has_name():
    assert hasattr(softGalleryLanguage_FrontEnd, "name")
    descriptor = None
    for klass in softGalleryLanguage_FrontEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_architecturecomponents_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ArchitectureComponents)


def test_softgallerylanguage_architecturecomponents_constructor_exists():
    assert callable(softGalleryLanguage_ArchitectureComponents.__init__)


def test_softgallerylanguage_architecturecomponents_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ArchitectureComponents.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_layertarget_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LayerTarget)


def test_softgallerylanguage_layertarget_constructor_exists():
    assert callable(softGalleryLanguage_LayerTarget.__init__)


def test_softgallerylanguage_layertarget_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LayerTarget.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_softgallerylanguage_layertarget_has_layerelations():
    assert hasattr(softGalleryLanguage_LayerTarget, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage_LayerTarget.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_layersource_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LayerSource)


def test_softgallerylanguage_layersource_constructor_exists():
    assert callable(softGalleryLanguage_LayerSource.__init__)


def test_softgallerylanguage_layersource_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LayerSource.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_softgallerylanguage_layersource_has_layerelations():
    assert hasattr(softGalleryLanguage_LayerSource, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage_LayerSource.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_technology_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Technology)


def test_softgallerylanguage_technology_constructor_exists():
    assert callable(softGalleryLanguage_Technology.__init__)


def test_softgallerylanguage_technology_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Technology.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_technology_has_name():
    assert hasattr(softGalleryLanguage_Technology, "name")
    descriptor = None
    for klass in softGalleryLanguage_Technology.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_singlefile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SingleFile)


def test_softgallerylanguage_singlefile_constructor_exists():
    assert callable(softGalleryLanguage_SingleFile.__init__)


def test_softgallerylanguage_singlefile_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SingleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_singlefile_has_name():
    assert hasattr(softGalleryLanguage_SingleFile, "name")
    descriptor = None
    for klass in softGalleryLanguage_SingleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_multiplefile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_MultipleFile)


def test_softgallerylanguage_multiplefile_constructor_exists():
    assert callable(softGalleryLanguage_MultipleFile.__init__)


def test_softgallerylanguage_multiplefile_constructor_args():
    sig = inspect.signature(softGalleryLanguage_MultipleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_multiplefile_has_name():
    assert hasattr(softGalleryLanguage_MultipleFile, "name")
    descriptor = None
    for klass in softGalleryLanguage_MultipleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_directories_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Directories)


def test_softgallerylanguage_directories_constructor_exists():
    assert callable(softGalleryLanguage_Directories.__init__)


def test_softgallerylanguage_directories_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Directories.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_directorycontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DirectoryContent)


def test_softgallerylanguage_directorycontent_constructor_exists():
    assert callable(softGalleryLanguage_DirectoryContent.__init__)


def test_softgallerylanguage_directorycontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DirectoryContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_directorycontent_has_name():
    assert hasattr(softGalleryLanguage_DirectoryContent, "name")
    descriptor = None
    for klass in softGalleryLanguage_DirectoryContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_segmentstructurecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SegmentStructureContent)


def test_softgallerylanguage_segmentstructurecontent_constructor_exists():
    assert callable(softGalleryLanguage_SegmentStructureContent.__init__)


def test_softgallerylanguage_segmentstructurecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SegmentStructureContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_segmentstructurecontent_has_name():
    assert hasattr(softGalleryLanguage_SegmentStructureContent, "name")
    descriptor = None
    for klass in softGalleryLanguage_SegmentStructureContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_segmentstructure_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SegmentStructure)


def test_softgallerylanguage_segmentstructure_constructor_exists():
    assert callable(softGalleryLanguage_SegmentStructure.__init__)


def test_softgallerylanguage_segmentstructure_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SegmentStructure.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_datapersistencesegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DataPersistenceSegments)


def test_softgallerylanguage_datapersistencesegments_constructor_exists():
    assert callable(softGalleryLanguage_DataPersistenceSegments.__init__)


def test_softgallerylanguage_datapersistencesegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DataPersistenceSegments.__init__)
    params = list(sig.parameters.keys())
    assert "postSName" in params, "Missing parameter 'postSName'"
    assert "amazonSName" in params, "Missing parameter 'amazonSName'"

def test_softgallerylanguage_datapersistencesegments_has_postSName():
    assert hasattr(softGalleryLanguage_DataPersistenceSegments, "postSName")
    descriptor = None
    for klass in softGalleryLanguage_DataPersistenceSegments.__mro__:
        if "postSName" in klass.__dict__:
            descriptor = klass.__dict__["postSName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_datapersistencesegments_has_amazonSName():
    assert hasattr(softGalleryLanguage_DataPersistenceSegments, "amazonSName")
    descriptor = None
    for klass in softGalleryLanguage_DataPersistenceSegments.__mro__:
        if "amazonSName" in klass.__dict__:
            descriptor = klass.__dict__["amazonSName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_datapersistencecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DataPersistenceContent)


def test_softgallerylanguage_datapersistencecontent_constructor_exists():
    assert callable(softGalleryLanguage_DataPersistenceContent.__init__)


def test_softgallerylanguage_datapersistencecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DataPersistenceContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_datapersistencelayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DataPersistenceLayer)


def test_softgallerylanguage_datapersistencelayer_constructor_exists():
    assert callable(softGalleryLanguage_DataPersistenceLayer.__init__)


def test_softgallerylanguage_datapersistencelayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DataPersistenceLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_criteriaattributetype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_CriteriaAttributeType)


def test_softgallerylanguage_criteriaattributetype_constructor_exists():
    assert callable(softGalleryLanguage_CriteriaAttributeType.__init__)


def test_softgallerylanguage_criteriaattributetype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_CriteriaAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_criteriaattributetype_has_name():
    assert hasattr(softGalleryLanguage_CriteriaAttributeType, "name")
    descriptor = None
    for klass in softGalleryLanguage_CriteriaAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_specificationsegmentelement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpecificationSegmentElement)


def test_softgallerylanguage_specificationsegmentelement_constructor_exists():
    assert callable(softGalleryLanguage_SpecificationSegmentElement.__init__)


def test_softgallerylanguage_specificationsegmentelement_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpecificationSegmentElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_specificationsegmentelement_has_name():
    assert hasattr(softGalleryLanguage_SpecificationSegmentElement, "name")
    descriptor = None
    for klass in softGalleryLanguage_SpecificationSegmentElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_controllersegmentelement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ControllerSegmentElement)


def test_softgallerylanguage_controllersegmentelement_constructor_exists():
    assert callable(softGalleryLanguage_ControllerSegmentElement.__init__)


def test_softgallerylanguage_controllersegmentelement_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ControllerSegmentElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_controllersegmentelement_has_name():
    assert hasattr(softGalleryLanguage_ControllerSegmentElement, "name")
    descriptor = None
    for klass in softGalleryLanguage_ControllerSegmentElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_layerrelations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LayerRelations)


def test_softgallerylanguage_layerrelations_constructor_exists():
    assert callable(softGalleryLanguage_LayerRelations.__init__)


def test_softgallerylanguage_layerrelations_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LayerRelations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_softgallerylanguage_layerrelations_has_name():
    assert hasattr(softGalleryLanguage_LayerRelations, "name")
    descriptor = None
    for klass in softGalleryLanguage_LayerRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_layerrelations_has_layerelations():
    assert hasattr(softGalleryLanguage_LayerRelations, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage_LayerRelations.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_businesslogicsegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BusinessLogicSegments)


def test_softgallerylanguage_businesslogicsegments_constructor_exists():
    assert callable(softGalleryLanguage_BusinessLogicSegments.__init__)


def test_softgallerylanguage_businesslogicsegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BusinessLogicSegments.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_businesslogicsegments_has_name():
    assert hasattr(softGalleryLanguage_BusinessLogicSegments, "name")
    descriptor = None
    for klass in softGalleryLanguage_BusinessLogicSegments.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_businesslogiccontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BusinessLogicContent)


def test_softgallerylanguage_businesslogiccontent_constructor_exists():
    assert callable(softGalleryLanguage_BusinessLogicContent.__init__)


def test_softgallerylanguage_businesslogiccontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BusinessLogicContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_businesslogiclayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BusinessLogicLayer)


def test_softgallerylanguage_businesslogiclayer_constructor_exists():
    assert callable(softGalleryLanguage_BusinessLogicLayer.__init__)


def test_softgallerylanguage_businesslogiclayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BusinessLogicLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_presentationsegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PresentationSegments)


def test_softgallerylanguage_presentationsegments_constructor_exists():
    assert callable(softGalleryLanguage_PresentationSegments.__init__)


def test_softgallerylanguage_presentationsegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PresentationSegments.__init__)
    params = list(sig.parameters.keys())
    assert "presentationCName" in params, "Missing parameter 'presentationCName'"
    assert "presentationAName" in params, "Missing parameter 'presentationAName'"
    assert "presentationSName" in params, "Missing parameter 'presentationSName'"

def test_softgallerylanguage_presentationsegments_has_presentationCName():
    assert hasattr(softGalleryLanguage_PresentationSegments, "presentationCName")
    descriptor = None
    for klass in softGalleryLanguage_PresentationSegments.__mro__:
        if "presentationCName" in klass.__dict__:
            descriptor = klass.__dict__["presentationCName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_presentationsegments_has_presentationAName():
    assert hasattr(softGalleryLanguage_PresentationSegments, "presentationAName")
    descriptor = None
    for klass in softGalleryLanguage_PresentationSegments.__mro__:
        if "presentationAName" in klass.__dict__:
            descriptor = klass.__dict__["presentationAName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_presentationsegments_has_presentationSName():
    assert hasattr(softGalleryLanguage_PresentationSegments, "presentationSName")
    descriptor = None
    for klass in softGalleryLanguage_PresentationSegments.__mro__:
        if "presentationSName" in klass.__dict__:
            descriptor = klass.__dict__["presentationSName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_presentationcontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PresentationContent)


def test_softgallerylanguage_presentationcontent_constructor_exists():
    assert callable(softGalleryLanguage_PresentationContent.__init__)


def test_softgallerylanguage_presentationcontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PresentationContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_presentationlayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PresentationLayer)


def test_softgallerylanguage_presentationlayer_constructor_exists():
    assert callable(softGalleryLanguage_PresentationLayer.__init__)


def test_softgallerylanguage_presentationlayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PresentationLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_layer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Layer)


def test_softgallerylanguage_layer_constructor_exists():
    assert callable(softGalleryLanguage_Layer.__init__)


def test_softgallerylanguage_layer_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Layer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_ntiers_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_NTiers)


def test_softgallerylanguage_ntiers_constructor_exists():
    assert callable(softGalleryLanguage_NTiers.__init__)


def test_softgallerylanguage_ntiers_constructor_args():
    sig = inspect.signature(softGalleryLanguage_NTiers.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_architecture_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Architecture)


def test_softgallerylanguage_architecture_constructor_exists():
    assert callable(softGalleryLanguage_Architecture.__init__)


def test_softgallerylanguage_architecture_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Architecture.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_userexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_UserException)


def test_softgallerylanguage_userexception_constructor_exists():
    assert callable(softGalleryLanguage_UserException.__init__)


def test_softgallerylanguage_userexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage_UserException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_userexception_has_name():
    assert hasattr(softGalleryLanguage_UserException, "name")
    descriptor = None
    for klass in softGalleryLanguage_UserException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_albumexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AlbumException)


def test_softgallerylanguage_albumexception_constructor_exists():
    assert callable(softGalleryLanguage_AlbumException.__init__)


def test_softgallerylanguage_albumexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AlbumException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_albumexception_has_name():
    assert hasattr(softGalleryLanguage_AlbumException, "name")
    descriptor = None
    for klass in softGalleryLanguage_AlbumException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_photoexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PhotoException)


def test_softgallerylanguage_photoexception_constructor_exists():
    assert callable(softGalleryLanguage_PhotoException.__init__)


def test_softgallerylanguage_photoexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PhotoException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_photoexception_has_name():
    assert hasattr(softGalleryLanguage_PhotoException, "name")
    descriptor = None
    for klass in softGalleryLanguage_PhotoException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_landingfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LandingFunctions)


def test_softgallerylanguage_landingfunctions_constructor_exists():
    assert callable(softGalleryLanguage_LandingFunctions.__init__)


def test_softgallerylanguage_landingfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LandingFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "passPhotoName" in params, "Missing parameter 'passPhotoName'"
    assert "nameCarouselName" in params, "Missing parameter 'nameCarouselName'"

def test_softgallerylanguage_landingfunctions_has_passPhotoName():
    assert hasattr(softGalleryLanguage_LandingFunctions, "passPhotoName")
    descriptor = None
    for klass in softGalleryLanguage_LandingFunctions.__mro__:
        if "passPhotoName" in klass.__dict__:
            descriptor = klass.__dict__["passPhotoName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_landingfunctions_has_nameCarouselName():
    assert hasattr(softGalleryLanguage_LandingFunctions, "nameCarouselName")
    descriptor = None
    for klass in softGalleryLanguage_LandingFunctions.__mro__:
        if "nameCarouselName" in klass.__dict__:
            descriptor = klass.__dict__["nameCarouselName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_photoactionsfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PhotoActionsFunctions)


def test_softgallerylanguage_photoactionsfunctions_constructor_exists():
    assert callable(softGalleryLanguage_PhotoActionsFunctions.__init__)


def test_softgallerylanguage_photoactionsfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PhotoActionsFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "nameLoad" in params, "Missing parameter 'nameLoad'"
    assert "nameGenerico" in params, "Missing parameter 'nameGenerico'"
    assert "namePhoto" in params, "Missing parameter 'namePhoto'"

def test_softgallerylanguage_photoactionsfunctions_has_nameLoad():
    assert hasattr(softGalleryLanguage_PhotoActionsFunctions, "nameLoad")
    descriptor = None
    for klass in softGalleryLanguage_PhotoActionsFunctions.__mro__:
        if "nameLoad" in klass.__dict__:
            descriptor = klass.__dict__["nameLoad"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_photoactionsfunctions_has_nameGenerico():
    assert hasattr(softGalleryLanguage_PhotoActionsFunctions, "nameGenerico")
    descriptor = None
    for klass in softGalleryLanguage_PhotoActionsFunctions.__mro__:
        if "nameGenerico" in klass.__dict__:
            descriptor = klass.__dict__["nameGenerico"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_photoactionsfunctions_has_namePhoto():
    assert hasattr(softGalleryLanguage_PhotoActionsFunctions, "namePhoto")
    descriptor = None
    for klass in softGalleryLanguage_PhotoActionsFunctions.__mro__:
        if "namePhoto" in klass.__dict__:
            descriptor = klass.__dict__["namePhoto"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_albummanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AlbumManagementFunctions)


def test_softgallerylanguage_albummanagementfunctions_constructor_exists():
    assert callable(softGalleryLanguage_AlbumManagementFunctions.__init__)


def test_softgallerylanguage_albummanagementfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AlbumManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "selectAlbName" in params, "Missing parameter 'selectAlbName'"
    assert "createdAlbName" in params, "Missing parameter 'createdAlbName'"

def test_softgallerylanguage_albummanagementfunctions_has_selectAlbName():
    assert hasattr(softGalleryLanguage_AlbumManagementFunctions, "selectAlbName")
    descriptor = None
    for klass in softGalleryLanguage_AlbumManagementFunctions.__mro__:
        if "selectAlbName" in klass.__dict__:
            descriptor = klass.__dict__["selectAlbName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_albummanagementfunctions_has_createdAlbName():
    assert hasattr(softGalleryLanguage_AlbumManagementFunctions, "createdAlbName")
    descriptor = None
    for klass in softGalleryLanguage_AlbumManagementFunctions.__mro__:
        if "createdAlbName" in klass.__dict__:
            descriptor = klass.__dict__["createdAlbName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_exceptionstype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ExceptionsType)


def test_softgallerylanguage_exceptionstype_constructor_exists():
    assert callable(softGalleryLanguage_ExceptionsType.__init__)


def test_softgallerylanguage_exceptionstype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ExceptionsType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_appaccessfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AppAccessFunctions)


def test_softgallerylanguage_appaccessfunctions_constructor_exists():
    assert callable(softGalleryLanguage_AppAccessFunctions.__init__)


def test_softgallerylanguage_appaccessfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AppAccessFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "loginName" in params, "Missing parameter 'loginName'"
    assert "registerName" in params, "Missing parameter 'registerName'"

def test_softgallerylanguage_appaccessfunctions_has_loginName():
    assert hasattr(softGalleryLanguage_AppAccessFunctions, "loginName")
    descriptor = None
    for klass in softGalleryLanguage_AppAccessFunctions.__mro__:
        if "loginName" in klass.__dict__:
            descriptor = klass.__dict__["loginName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_appaccessfunctions_has_registerName():
    assert hasattr(softGalleryLanguage_AppAccessFunctions, "registerName")
    descriptor = None
    for klass in softGalleryLanguage_AppAccessFunctions.__mro__:
        if "registerName" in klass.__dict__:
            descriptor = klass.__dict__["registerName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_profilemanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ProfileManagementFunctions)


def test_softgallerylanguage_profilemanagementfunctions_constructor_exists():
    assert callable(softGalleryLanguage_ProfileManagementFunctions.__init__)


def test_softgallerylanguage_profilemanagementfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ProfileManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "viewprofileName" in params, "Missing parameter 'viewprofileName'"
    assert "editProfileName" in params, "Missing parameter 'editProfileName'"

def test_softgallerylanguage_profilemanagementfunctions_has_viewprofileName():
    assert hasattr(softGalleryLanguage_ProfileManagementFunctions, "viewprofileName")
    descriptor = None
    for klass in softGalleryLanguage_ProfileManagementFunctions.__mro__:
        if "viewprofileName" in klass.__dict__:
            descriptor = klass.__dict__["viewprofileName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_profilemanagementfunctions_has_editProfileName():
    assert hasattr(softGalleryLanguage_ProfileManagementFunctions, "editProfileName")
    descriptor = None
    for klass in softGalleryLanguage_ProfileManagementFunctions.__mro__:
        if "editProfileName" in klass.__dict__:
            descriptor = klass.__dict__["editProfileName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_landingactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LandingActions)


def test_softgallerylanguage_landingactions_constructor_exists():
    assert callable(softGalleryLanguage_LandingActions.__init__)


def test_softgallerylanguage_landingactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LandingActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_photoactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PhotoActions)


def test_softgallerylanguage_photoactions_constructor_exists():
    assert callable(softGalleryLanguage_PhotoActions.__init__)


def test_softgallerylanguage_photoactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PhotoActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_albummanagement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AlbumManagement)


def test_softgallerylanguage_albummanagement_constructor_exists():
    assert callable(softGalleryLanguage_AlbumManagement.__init__)


def test_softgallerylanguage_albummanagement_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AlbumManagement.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_appaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AppAccess)


def test_softgallerylanguage_appaccess_constructor_exists():
    assert callable(softGalleryLanguage_AppAccess.__init__)


def test_softgallerylanguage_appaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AppAccess.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_profilemanagement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ProfileManagement)


def test_softgallerylanguage_profilemanagement_constructor_exists():
    assert callable(softGalleryLanguage_ProfileManagement.__init__)


def test_softgallerylanguage_profilemanagement_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ProfileManagement.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_functionalities_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Functionalities)


def test_softgallerylanguage_functionalities_constructor_exists():
    assert callable(softGalleryLanguage_Functionalities.__init__)


def test_softgallerylanguage_functionalities_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Functionalities.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_atributeuserdomain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AtributeUserDomain)


def test_softgallerylanguage_atributeuserdomain_constructor_exists():
    assert callable(softGalleryLanguage_AtributeUserDomain.__init__)


def test_softgallerylanguage_atributeuserdomain_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AtributeUserDomain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_atributeuserdomain_has_name():
    assert hasattr(softGalleryLanguage_AtributeUserDomain, "name")
    descriptor = None
    for klass in softGalleryLanguage_AtributeUserDomain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_atributealbum_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AtributeAlbum)


def test_softgallerylanguage_atributealbum_constructor_exists():
    assert callable(softGalleryLanguage_AtributeAlbum.__init__)


def test_softgallerylanguage_atributealbum_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AtributeAlbum.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_atributealbum_has_name():
    assert hasattr(softGalleryLanguage_AtributeAlbum, "name")
    descriptor = None
    for klass in softGalleryLanguage_AtributeAlbum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_atributephoto_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AtributePhoto)


def test_softgallerylanguage_atributephoto_constructor_exists():
    assert callable(softGalleryLanguage_AtributePhoto.__init__)


def test_softgallerylanguage_atributephoto_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AtributePhoto.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_atributephoto_has_name():
    assert hasattr(softGalleryLanguage_AtributePhoto, "name")
    descriptor = None
    for klass in softGalleryLanguage_AtributePhoto.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_entities_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Entities)


def test_softgallerylanguage_entities_constructor_exists():
    assert callable(softGalleryLanguage_Entities.__init__)


def test_softgallerylanguage_entities_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Entities.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_entities_has_name():
    assert hasattr(softGalleryLanguage_Entities, "name")
    descriptor = None
    for klass in softGalleryLanguage_Entities.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_exceptionsdomain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ExceptionsDomain)


def test_softgallerylanguage_exceptionsdomain_constructor_exists():
    assert callable(softGalleryLanguage_ExceptionsDomain.__init__)


def test_softgallerylanguage_exceptionsdomain_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ExceptionsDomain.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_functionality_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Functionality)


def test_softgallerylanguage_functionality_constructor_exists():
    assert callable(softGalleryLanguage_Functionality.__init__)


def test_softgallerylanguage_functionality_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Functionality.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_entity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Entity)


def test_softgallerylanguage_entity_constructor_exists():
    assert callable(softGalleryLanguage_Entity.__init__)


def test_softgallerylanguage_entity_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Entity.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_domain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Domain)


def test_softgallerylanguage_domain_constructor_exists():
    assert callable(softGalleryLanguage_Domain.__init__)


def test_softgallerylanguage_domain_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_domain_has_name():
    assert hasattr(softGalleryLanguage_Domain, "name")
    descriptor = None
    for klass in softGalleryLanguage_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_eobject_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_EObject)


def test_softgallerylanguage_eobject_constructor_exists():
    assert callable(softGalleryLanguage_EObject.__init__)


def test_softgallerylanguage_eobject_constructor_args():
    sig = inspect.signature(softGalleryLanguage_EObject.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_model_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Model)


def test_softgallerylanguage_model_constructor_exists():
    assert callable(softGalleryLanguage_Model.__init__)


def test_softgallerylanguage_model_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Model.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_amazonelasticcomputecloud_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AmazonElasticComputeCloud)


def test_softgallerylanguage_amazonelasticcomputecloud_constructor_exists():
    assert callable(softGalleryLanguage_AmazonElasticComputeCloud.__init__)


def test_softgallerylanguage_amazonelasticcomputecloud_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AmazonElasticComputeCloud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_amazonelasticcomputecloud_has_name():
    assert hasattr(softGalleryLanguage_AmazonElasticComputeCloud, "name")
    descriptor = None
    for klass in softGalleryLanguage_AmazonElasticComputeCloud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_metadata_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Metadata)


def test_softgallerylanguage_metadata_constructor_exists():
    assert callable(softGalleryLanguage_Metadata.__init__)


def test_softgallerylanguage_metadata_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_metadata_has_name():
    assert hasattr(softGalleryLanguage_Metadata, "name")
    descriptor = None
    for klass in softGalleryLanguage_Metadata.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_amazonfile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AmazonFile)


def test_softgallerylanguage_amazonfile_constructor_exists():
    assert callable(softGalleryLanguage_AmazonFile.__init__)


def test_softgallerylanguage_amazonfile_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AmazonFile.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_amazonfolder_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AmazonFolder)


def test_softgallerylanguage_amazonfolder_constructor_exists():
    assert callable(softGalleryLanguage_AmazonFolder.__init__)


def test_softgallerylanguage_amazonfolder_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AmazonFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_amazonfolder_has_name():
    assert hasattr(softGalleryLanguage_AmazonFolder, "name")
    descriptor = None
    for klass in softGalleryLanguage_AmazonFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_onlyauthorized_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_OnlyAuthorized)


def test_softgallerylanguage_onlyauthorized_constructor_exists():
    assert callable(softGalleryLanguage_OnlyAuthorized.__init__)


def test_softgallerylanguage_onlyauthorized_constructor_args():
    sig = inspect.signature(softGalleryLanguage_OnlyAuthorized.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_onlyauthorized_has_name():
    assert hasattr(softGalleryLanguage_OnlyAuthorized, "name")
    descriptor = None
    for klass in softGalleryLanguage_OnlyAuthorized.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_bucketobjectsnotpublic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BucketObjectsNotPublic)


def test_softgallerylanguage_bucketobjectsnotpublic_constructor_exists():
    assert callable(softGalleryLanguage_BucketObjectsNotPublic.__init__)


def test_softgallerylanguage_bucketobjectsnotpublic_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BucketObjectsNotPublic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_bucketobjectsnotpublic_has_name():
    assert hasattr(softGalleryLanguage_BucketObjectsNotPublic, "name")
    descriptor = None
    for klass in softGalleryLanguage_BucketObjectsNotPublic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_objectspublic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ObjectsPublic)


def test_softgallerylanguage_objectspublic_constructor_exists():
    assert callable(softGalleryLanguage_ObjectsPublic.__init__)


def test_softgallerylanguage_objectspublic_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ObjectsPublic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_objectspublic_has_name():
    assert hasattr(softGalleryLanguage_ObjectsPublic, "name")
    descriptor = None
    for klass in softGalleryLanguage_ObjectsPublic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_bucketaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BucketAccess)


def test_softgallerylanguage_bucketaccess_constructor_exists():
    assert callable(softGalleryLanguage_BucketAccess.__init__)


def test_softgallerylanguage_bucketaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BucketAccess.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_bucket_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Bucket)


def test_softgallerylanguage_bucket_constructor_exists():
    assert callable(softGalleryLanguage_Bucket.__init__)


def test_softgallerylanguage_bucket_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Bucket.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_bucket_has_name():
    assert hasattr(softGalleryLanguage_Bucket, "name")
    descriptor = None
    for klass in softGalleryLanguage_Bucket.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_batchoperation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_BatchOperation)


def test_softgallerylanguage_batchoperation_constructor_exists():
    assert callable(softGalleryLanguage_BatchOperation.__init__)


def test_softgallerylanguage_batchoperation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_BatchOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_batchoperation_has_name():
    assert hasattr(softGalleryLanguage_BatchOperation, "name")
    descriptor = None
    for klass in softGalleryLanguage_BatchOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_amazonsimplestorageservice_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_AmazonSimpleStorageService)


def test_softgallerylanguage_amazonsimplestorageservice_constructor_exists():
    assert callable(softGalleryLanguage_AmazonSimpleStorageService.__init__)


def test_softgallerylanguage_amazonsimplestorageservice_constructor_args():
    sig = inspect.signature(softGalleryLanguage_AmazonSimpleStorageService.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_clause_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Clause)


def test_softgallerylanguage_clause_constructor_exists():
    assert callable(softGalleryLanguage_Clause.__init__)


def test_softgallerylanguage_clause_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Clause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_clause_has_name():
    assert hasattr(softGalleryLanguage_Clause, "name")
    descriptor = None
    for klass in softGalleryLanguage_Clause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_query_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Query)


def test_softgallerylanguage_query_constructor_exists():
    assert callable(softGalleryLanguage_Query.__init__)


def test_softgallerylanguage_query_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Query.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_privilege_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Privilege)


def test_softgallerylanguage_privilege_constructor_exists():
    assert callable(softGalleryLanguage_Privilege.__init__)


def test_softgallerylanguage_privilege_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Privilege.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_privilege_has_name():
    assert hasattr(softGalleryLanguage_Privilege, "name")
    descriptor = None
    for klass in softGalleryLanguage_Privilege.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_postgresuser_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PostgresUser)


def test_softgallerylanguage_postgresuser_constructor_exists():
    assert callable(softGalleryLanguage_PostgresUser.__init__)


def test_softgallerylanguage_postgresuser_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PostgresUser.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_postgresuser_has_name():
    assert hasattr(softGalleryLanguage_PostgresUser, "name")
    descriptor = None
    for klass in softGalleryLanguage_PostgresUser.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_function_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Function)


def test_softgallerylanguage_function_constructor_exists():
    assert callable(softGalleryLanguage_Function.__init__)


def test_softgallerylanguage_function_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_function_has_name():
    assert hasattr(softGalleryLanguage_Function, "name")
    descriptor = None
    for klass in softGalleryLanguage_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_trigger_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Trigger)


def test_softgallerylanguage_trigger_constructor_exists():
    assert callable(softGalleryLanguage_Trigger.__init__)


def test_softgallerylanguage_trigger_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_trigger_has_name():
    assert hasattr(softGalleryLanguage_Trigger, "name")
    descriptor = None
    for klass in softGalleryLanguage_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_policy_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Policy)


def test_softgallerylanguage_policy_constructor_exists():
    assert callable(softGalleryLanguage_Policy.__init__)


def test_softgallerylanguage_policy_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Policy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_policy_has_name():
    assert hasattr(softGalleryLanguage_Policy, "name")
    descriptor = None
    for klass in softGalleryLanguage_Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_publicaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PublicAccess)


def test_softgallerylanguage_publicaccess_constructor_exists():
    assert callable(softGalleryLanguage_PublicAccess.__init__)


def test_softgallerylanguage_publicaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PublicAccess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_publicaccess_has_name():
    assert hasattr(softGalleryLanguage_PublicAccess, "name")
    descriptor = None
    for klass in softGalleryLanguage_PublicAccess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_constraint_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Constraint)


def test_softgallerylanguage_constraint_constructor_exists():
    assert callable(softGalleryLanguage_Constraint.__init__)


def test_softgallerylanguage_constraint_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_constraint_has_name():
    assert hasattr(softGalleryLanguage_Constraint, "name")
    descriptor = None
    for klass in softGalleryLanguage_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_datatypedb_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DatatypeDB)


def test_softgallerylanguage_datatypedb_constructor_exists():
    assert callable(softGalleryLanguage_DatatypeDB.__init__)


def test_softgallerylanguage_datatypedb_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DatatypeDB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_datatypedb_has_name():
    assert hasattr(softGalleryLanguage_DatatypeDB, "name")
    descriptor = None
    for klass in softGalleryLanguage_DatatypeDB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_columnp_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ColumnP)


def test_softgallerylanguage_columnp_constructor_exists():
    assert callable(softGalleryLanguage_ColumnP.__init__)


def test_softgallerylanguage_columnp_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ColumnP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_columnp_has_name():
    assert hasattr(softGalleryLanguage_ColumnP, "name")
    descriptor = None
    for klass in softGalleryLanguage_ColumnP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reftable_p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RefTable_p)


def test_softgallerylanguage_reftable_p_constructor_exists():
    assert callable(softGalleryLanguage_RefTable_p.__init__)


def test_softgallerylanguage_reftable_p_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RefTable_p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reftable_p_has_name():
    assert hasattr(softGalleryLanguage_RefTable_p, "name")
    descriptor = None
    for klass in softGalleryLanguage_RefTable_p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_foreignkeyref_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ForeignKeyRef)


def test_softgallerylanguage_foreignkeyref_constructor_exists():
    assert callable(softGalleryLanguage_ForeignKeyRef.__init__)


def test_softgallerylanguage_foreignkeyref_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ForeignKeyRef.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_foreignkey_n_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ForeignKey_n)


def test_softgallerylanguage_foreignkey_n_constructor_exists():
    assert callable(softGalleryLanguage_ForeignKey_n.__init__)


def test_softgallerylanguage_foreignkey_n_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ForeignKey_n.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_foreignkey_n_has_name():
    assert hasattr(softGalleryLanguage_ForeignKey_n, "name")
    descriptor = None
    for klass in softGalleryLanguage_ForeignKey_n.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_foreignkey_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ForeignKey)


def test_softgallerylanguage_foreignkey_constructor_exists():
    assert callable(softGalleryLanguage_ForeignKey.__init__)


def test_softgallerylanguage_foreignkey_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_table_p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Table_p)


def test_softgallerylanguage_table_p_constructor_exists():
    assert callable(softGalleryLanguage_Table_p.__init__)


def test_softgallerylanguage_table_p_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Table_p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_table_p_has_name():
    assert hasattr(softGalleryLanguage_Table_p, "name")
    descriptor = None
    for klass in softGalleryLanguage_Table_p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_viewschema_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ViewSchema)


def test_softgallerylanguage_viewschema_constructor_exists():
    assert callable(softGalleryLanguage_ViewSchema.__init__)


def test_softgallerylanguage_viewschema_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ViewSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_viewschema_has_name():
    assert hasattr(softGalleryLanguage_ViewSchema, "name")
    descriptor = None
    for klass in softGalleryLanguage_ViewSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_index_p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Index_p)


def test_softgallerylanguage_index_p_constructor_exists():
    assert callable(softGalleryLanguage_Index_p.__init__)


def test_softgallerylanguage_index_p_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Index_p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_index_p_has_name():
    assert hasattr(softGalleryLanguage_Index_p, "name")
    descriptor = None
    for klass in softGalleryLanguage_Index_p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_schema_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Schema)


def test_softgallerylanguage_schema_constructor_exists():
    assert callable(softGalleryLanguage_Schema.__init__)


def test_softgallerylanguage_schema_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Schema.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_database_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Database)


def test_softgallerylanguage_database_constructor_exists():
    assert callable(softGalleryLanguage_Database.__init__)


def test_softgallerylanguage_database_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_database_has_name():
    assert hasattr(softGalleryLanguage_Database, "name")
    descriptor = None
    for klass in softGalleryLanguage_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_cluster_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Cluster)


def test_softgallerylanguage_cluster_constructor_exists():
    assert callable(softGalleryLanguage_Cluster.__init__)


def test_softgallerylanguage_cluster_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Cluster.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_row_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Row)


def test_softgallerylanguage_row_constructor_exists():
    assert callable(softGalleryLanguage_Row.__init__)


def test_softgallerylanguage_row_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Row.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_row_has_name():
    assert hasattr(softGalleryLanguage_Row, "name")
    descriptor = None
    for klass in softGalleryLanguage_Row.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactinformation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactInformation)


def test_softgallerylanguage_reactinformation_constructor_exists():
    assert callable(softGalleryLanguage_ReactInformation.__init__)


def test_softgallerylanguage_reactinformation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactInformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactinformation_has_name():
    assert hasattr(softGalleryLanguage_ReactInformation, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactInformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactlibrary_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactLibrary)


def test_softgallerylanguage_reactlibrary_constructor_exists():
    assert callable(softGalleryLanguage_ReactLibrary.__init__)


def test_softgallerylanguage_reactlibrary_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactlibrary_has_name():
    assert hasattr(softGalleryLanguage_ReactLibrary, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactsrelationserv_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactsRelationServ)


def test_softgallerylanguage_reactsrelationserv_constructor_exists():
    assert callable(softGalleryLanguage_ReactsRelationServ.__init__)


def test_softgallerylanguage_reactsrelationserv_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactsRelationServ.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactsrelationserv_has_name():
    assert hasattr(softGalleryLanguage_ReactsRelationServ, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactsRelationServ.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactservicerequestprops_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactServiceRequestProps)


def test_softgallerylanguage_reactservicerequestprops_constructor_exists():
    assert callable(softGalleryLanguage_ReactServiceRequestProps.__init__)


def test_softgallerylanguage_reactservicerequestprops_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactServiceRequestProps.__init__)
    params = list(sig.parameters.keys())
    assert "reqPropName" in params, "Missing parameter 'reqPropName'"
    assert "reqPropDescription" in params, "Missing parameter 'reqPropDescription'"

def test_softgallerylanguage_reactservicerequestprops_has_reqPropName():
    assert hasattr(softGalleryLanguage_ReactServiceRequestProps, "reqPropName")
    descriptor = None
    for klass in softGalleryLanguage_ReactServiceRequestProps.__mro__:
        if "reqPropName" in klass.__dict__:
            descriptor = klass.__dict__["reqPropName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_reactservicerequestprops_has_reqPropDescription():
    assert hasattr(softGalleryLanguage_ReactServiceRequestProps, "reqPropDescription")
    descriptor = None
    for klass in softGalleryLanguage_ReactServiceRequestProps.__mro__:
        if "reqPropDescription" in klass.__dict__:
            descriptor = klass.__dict__["reqPropDescription"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactservicecontrequest_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactServiceContRequest)


def test_softgallerylanguage_reactservicecontrequest_constructor_exists():
    assert callable(softGalleryLanguage_ReactServiceContRequest.__init__)


def test_softgallerylanguage_reactservicecontrequest_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactServiceContRequest.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactservicecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactServiceContent)


def test_softgallerylanguage_reactservicecontent_constructor_exists():
    assert callable(softGalleryLanguage_ReactServiceContent.__init__)


def test_softgallerylanguage_reactservicecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactServiceContent.__init__)
    params = list(sig.parameters.keys())
    assert "functName" in params, "Missing parameter 'functName'"

def test_softgallerylanguage_reactservicecontent_has_functName():
    assert hasattr(softGalleryLanguage_ReactServiceContent, "functName")
    descriptor = None
    for klass in softGalleryLanguage_ReactServiceContent.__mro__:
        if "functName" in klass.__dict__:
            descriptor = klass.__dict__["functName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactservicestype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactServicesType)


def test_softgallerylanguage_reactservicestype_constructor_exists():
    assert callable(softGalleryLanguage_ReactServicesType.__init__)


def test_softgallerylanguage_reactservicestype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactServicesType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactservicestype_has_name():
    assert hasattr(softGalleryLanguage_ReactServicesType, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactServicesType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactservicesrelation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactServicesRelation)


def test_softgallerylanguage_reactservicesrelation_constructor_exists():
    assert callable(softGalleryLanguage_ReactServicesRelation.__init__)


def test_softgallerylanguage_reactservicesrelation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactServicesRelation.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactactionscontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactActionsContent)


def test_softgallerylanguage_reactactionscontent_constructor_exists():
    assert callable(softGalleryLanguage_ReactActionsContent.__init__)


def test_softgallerylanguage_reactactionscontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactActionsContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_stylepropertiescontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StylePropertiesContent)


def test_softgallerylanguage_stylepropertiescontent_constructor_exists():
    assert callable(softGalleryLanguage_StylePropertiesContent.__init__)


def test_softgallerylanguage_stylepropertiescontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StylePropertiesContent.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_softgallerylanguage_stylepropertiescontent_has_propName():
    assert hasattr(softGalleryLanguage_StylePropertiesContent, "propName")
    descriptor = None
    for klass in softGalleryLanguage_StylePropertiesContent.__mro__:
        if "propName" in klass.__dict__:
            descriptor = klass.__dict__["propName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_componentsstylescontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ComponentsStylesContent)


def test_softgallerylanguage_componentsstylescontent_constructor_exists():
    assert callable(softGalleryLanguage_ComponentsStylesContent.__init__)


def test_softgallerylanguage_componentsstylescontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ComponentsStylesContent.__init__)
    params = list(sig.parameters.keys())
    assert "nameStyle" in params, "Missing parameter 'nameStyle'"

def test_softgallerylanguage_componentsstylescontent_has_nameStyle():
    assert hasattr(softGalleryLanguage_ComponentsStylesContent, "nameStyle")
    descriptor = None
    for klass in softGalleryLanguage_ComponentsStylesContent.__mro__:
        if "nameStyle" in klass.__dict__:
            descriptor = klass.__dict__["nameStyle"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_propstype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PropsType)


def test_softgallerylanguage_propstype_constructor_exists():
    assert callable(softGalleryLanguage_PropsType.__init__)


def test_softgallerylanguage_propstype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PropsType.__init__)
    params = list(sig.parameters.keys())
    assert "nameProps" in params, "Missing parameter 'nameProps'"
    assert "propsdatas" in params, "Missing parameter 'propsdatas'"

def test_softgallerylanguage_propstype_has_nameProps():
    assert hasattr(softGalleryLanguage_PropsType, "nameProps")
    descriptor = None
    for klass in softGalleryLanguage_PropsType.__mro__:
        if "nameProps" in klass.__dict__:
            descriptor = klass.__dict__["nameProps"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_propstype_has_propsdatas():
    assert hasattr(softGalleryLanguage_PropsType, "propsdatas")
    descriptor = None
    for klass in softGalleryLanguage_PropsType.__mro__:
        if "propsdatas" in klass.__dict__:
            descriptor = klass.__dict__["propsdatas"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_statecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StateContent)


def test_softgallerylanguage_statecontent_constructor_exists():
    assert callable(softGalleryLanguage_StateContent.__init__)


def test_softgallerylanguage_statecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StateContent.__init__)
    params = list(sig.parameters.keys())
    assert "stateName" in params, "Missing parameter 'stateName'"
    assert "componentdatatyp" in params, "Missing parameter 'componentdatatyp'"

def test_softgallerylanguage_statecontent_has_stateName():
    assert hasattr(softGalleryLanguage_StateContent, "stateName")
    descriptor = None
    for klass in softGalleryLanguage_StateContent.__mro__:
        if "stateName" in klass.__dict__:
            descriptor = klass.__dict__["stateName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_statecontent_has_componentdatatyp():
    assert hasattr(softGalleryLanguage_StateContent, "componentdatatyp")
    descriptor = None
    for klass in softGalleryLanguage_StateContent.__mro__:
        if "componentdatatyp" in klass.__dict__:
            descriptor = klass.__dict__["componentdatatyp"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_corefunctionsdeclaration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_CoreFunctionsDeclaration)


def test_softgallerylanguage_corefunctionsdeclaration_constructor_exists():
    assert callable(softGalleryLanguage_CoreFunctionsDeclaration.__init__)


def test_softgallerylanguage_corefunctionsdeclaration_constructor_args():
    sig = inspect.signature(softGalleryLanguage_CoreFunctionsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_corefunctionsdeclaration_has_name():
    assert hasattr(softGalleryLanguage_CoreFunctionsDeclaration, "name")
    descriptor = None
    for klass in softGalleryLanguage_CoreFunctionsDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_state_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_State)


def test_softgallerylanguage_state_constructor_exists():
    assert callable(softGalleryLanguage_State.__init__)


def test_softgallerylanguage_state_constructor_args():
    sig = inspect.signature(softGalleryLanguage_State.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactcorefunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactCoreFunctions)


def test_softgallerylanguage_reactcorefunctions_constructor_exists():
    assert callable(softGalleryLanguage_ReactCoreFunctions.__init__)


def test_softgallerylanguage_reactcorefunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactCoreFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactcorefunctions_has_name():
    assert hasattr(softGalleryLanguage_ReactCoreFunctions, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactCoreFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactconstructor_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactConstructor)


def test_softgallerylanguage_reactconstructor_constructor_exists():
    assert callable(softGalleryLanguage_ReactConstructor.__init__)


def test_softgallerylanguage_reactconstructor_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactConstructor.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactimportcontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactImportContent)


def test_softgallerylanguage_reactimportcontent_constructor_exists():
    assert callable(softGalleryLanguage_ReactImportContent.__init__)


def test_softgallerylanguage_reactimportcontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactImportContent.__init__)
    params = list(sig.parameters.keys())
    assert "impName" in params, "Missing parameter 'impName'"

def test_softgallerylanguage_reactimportcontent_has_impName():
    assert hasattr(softGalleryLanguage_ReactImportContent, "impName")
    descriptor = None
    for klass in softGalleryLanguage_ReactImportContent.__mro__:
        if "impName" in klass.__dict__:
            descriptor = klass.__dict__["impName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_styleproperties_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StyleProperties)


def test_softgallerylanguage_styleproperties_constructor_exists():
    assert callable(softGalleryLanguage_StyleProperties.__init__)


def test_softgallerylanguage_styleproperties_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StyleProperties.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_props_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_Props)


def test_softgallerylanguage_props_constructor_exists():
    assert callable(softGalleryLanguage_Props.__init__)


def test_softgallerylanguage_props_constructor_args():
    sig = inspect.signature(softGalleryLanguage_Props.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactFunctions)


def test_softgallerylanguage_reactfunctions_constructor_exists():
    assert callable(softGalleryLanguage_ReactFunctions.__init__)


def test_softgallerylanguage_reactfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "renderclass" in params, "Missing parameter 'renderclass'"
    assert "lifecycleclass" in params, "Missing parameter 'lifecycleclass'"

def test_softgallerylanguage_reactfunctions_has_renderclass():
    assert hasattr(softGalleryLanguage_ReactFunctions, "renderclass")
    descriptor = None
    for klass in softGalleryLanguage_ReactFunctions.__mro__:
        if "renderclass" in klass.__dict__:
            descriptor = klass.__dict__["renderclass"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_reactfunctions_has_lifecycleclass():
    assert hasattr(softGalleryLanguage_ReactFunctions, "lifecycleclass")
    descriptor = None
    for klass in softGalleryLanguage_ReactFunctions.__mro__:
        if "lifecycleclass" in klass.__dict__:
            descriptor = klass.__dict__["lifecycleclass"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactimports_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactImports)


def test_softgallerylanguage_reactimports_constructor_exists():
    assert callable(softGalleryLanguage_ReactImports.__init__)


def test_softgallerylanguage_reactimports_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactImports.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_subcomponentcont_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SubcomponentCont)


def test_softgallerylanguage_subcomponentcont_constructor_exists():
    assert callable(softGalleryLanguage_SubcomponentCont.__init__)


def test_softgallerylanguage_subcomponentcont_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SubcomponentCont.__init__)
    params = list(sig.parameters.keys())
    assert "nameSubComp" in params, "Missing parameter 'nameSubComp'"

def test_softgallerylanguage_subcomponentcont_has_nameSubComp():
    assert hasattr(softGalleryLanguage_SubcomponentCont, "nameSubComp")
    descriptor = None
    for klass in softGalleryLanguage_SubcomponentCont.__mro__:
        if "nameSubComp" in klass.__dict__:
            descriptor = klass.__dict__["nameSubComp"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_viewcomponentcont_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ViewComponentCont)


def test_softgallerylanguage_viewcomponentcont_constructor_exists():
    assert callable(softGalleryLanguage_ViewComponentCont.__init__)


def test_softgallerylanguage_viewcomponentcont_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ViewComponentCont.__init__)
    params = list(sig.parameters.keys())
    assert "nameView" in params, "Missing parameter 'nameView'"

def test_softgallerylanguage_viewcomponentcont_has_nameView():
    assert hasattr(softGalleryLanguage_ViewComponentCont, "nameView")
    descriptor = None
    for klass in softGalleryLanguage_ViewComponentCont.__mro__:
        if "nameView" in klass.__dict__:
            descriptor = klass.__dict__["nameView"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_uicontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_UIContent)


def test_softgallerylanguage_uicontent_constructor_exists():
    assert callable(softGalleryLanguage_UIContent.__init__)


def test_softgallerylanguage_uicontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_UIContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_componentclass_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ComponentClass)


def test_softgallerylanguage_componentclass_constructor_exists():
    assert callable(softGalleryLanguage_ComponentClass.__init__)


def test_softgallerylanguage_componentclass_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ComponentClass.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_logicstructure_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LogicStructure)


def test_softgallerylanguage_logicstructure_constructor_exists():
    assert callable(softGalleryLanguage_LogicStructure.__init__)


def test_softgallerylanguage_logicstructure_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LogicStructure.__init__)
    params = list(sig.parameters.keys())
    assert "appComName" in params, "Missing parameter 'appComName'"
    assert "indexCompName" in params, "Missing parameter 'indexCompName'"

def test_softgallerylanguage_logicstructure_has_appComName():
    assert hasattr(softGalleryLanguage_LogicStructure, "appComName")
    descriptor = None
    for klass in softGalleryLanguage_LogicStructure.__mro__:
        if "appComName" in klass.__dict__:
            descriptor = klass.__dict__["appComName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_logicstructure_has_indexCompName():
    assert hasattr(softGalleryLanguage_LogicStructure, "indexCompName")
    descriptor = None
    for klass in softGalleryLanguage_LogicStructure.__mro__:
        if "indexCompName" in klass.__dict__:
            descriptor = klass.__dict__["indexCompName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_logiccontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_LogicContent)


def test_softgallerylanguage_logiccontent_constructor_exists():
    assert callable(softGalleryLanguage_LogicContent.__init__)


def test_softgallerylanguage_logiccontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage_LogicContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_logiccontent_has_name():
    assert hasattr(softGalleryLanguage_LogicContent, "name")
    descriptor = None
    for klass in softGalleryLanguage_LogicContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_componentsstyles_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ComponentsStyles)


def test_softgallerylanguage_componentsstyles_constructor_exists():
    assert callable(softGalleryLanguage_ComponentsStyles.__init__)


def test_softgallerylanguage_componentsstyles_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ComponentsStyles.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_componentslogic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ComponentsLogic)


def test_softgallerylanguage_componentslogic_constructor_exists():
    assert callable(softGalleryLanguage_ComponentsLogic.__init__)


def test_softgallerylanguage_componentslogic_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ComponentsLogic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_componentslogic_has_name():
    assert hasattr(softGalleryLanguage_ComponentsLogic, "name")
    descriptor = None
    for klass in softGalleryLanguage_ComponentsLogic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_domconfigurations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DOMConfigurations)


def test_softgallerylanguage_domconfigurations_constructor_exists():
    assert callable(softGalleryLanguage_DOMConfigurations.__init__)


def test_softgallerylanguage_domconfigurations_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DOMConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "elements" in params, "Missing parameter 'elements'"

def test_softgallerylanguage_domconfigurations_has_name():
    assert hasattr(softGalleryLanguage_DOMConfigurations, "name")
    descriptor = None
    for klass in softGalleryLanguage_DOMConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage_domconfigurations_has_elements():
    assert hasattr(softGalleryLanguage_DOMConfigurations, "elements")
    descriptor = None
    for klass in softGalleryLanguage_DOMConfigurations.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_packageversion_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PackageVersion)


def test_softgallerylanguage_packageversion_constructor_exists():
    assert callable(softGalleryLanguage_PackageVersion.__init__)


def test_softgallerylanguage_packageversion_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PackageVersion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_packageversion_has_name():
    assert hasattr(softGalleryLanguage_PackageVersion, "name")
    descriptor = None
    for klass in softGalleryLanguage_PackageVersion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_packagename_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PackageName)


def test_softgallerylanguage_packagename_constructor_exists():
    assert callable(softGalleryLanguage_PackageName.__init__)


def test_softgallerylanguage_packagename_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PackageName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_packagename_has_name():
    assert hasattr(softGalleryLanguage_PackageName, "name")
    descriptor = None
    for klass in softGalleryLanguage_PackageName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_singledependencies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SingleDependencies)


def test_softgallerylanguage_singledependencies_constructor_exists():
    assert callable(softGalleryLanguage_SingleDependencies.__init__)


def test_softgallerylanguage_singledependencies_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SingleDependencies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactdependenciessubrules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactDependenciesSubRules)


def test_softgallerylanguage_reactdependenciessubrules_constructor_exists():
    assert callable(softGalleryLanguage_ReactDependenciesSubRules.__init__)


def test_softgallerylanguage_reactdependenciessubrules_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactDependenciesSubRules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactdependenciesrules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactDependenciesRules)


def test_softgallerylanguage_reactdependenciesrules_constructor_exists():
    assert callable(softGalleryLanguage_ReactDependenciesRules.__init__)


def test_softgallerylanguage_reactdependenciesrules_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactDependenciesRules.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactdependenciesrules_has_name():
    assert hasattr(softGalleryLanguage_ReactDependenciesRules, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactDependenciesRules.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactconfigurations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactConfigurations)


def test_softgallerylanguage_reactconfigurations_constructor_exists():
    assert callable(softGalleryLanguage_ReactConfigurations.__init__)


def test_softgallerylanguage_reactconfigurations_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_reactconfigurations_has_name():
    assert hasattr(softGalleryLanguage_ReactConfigurations, "name")
    descriptor = None
    for klass in softGalleryLanguage_ReactConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactdependencies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactDependencies)


def test_softgallerylanguage_reactdependencies_constructor_exists():
    assert callable(softGalleryLanguage_ReactDependencies.__init__)


def test_softgallerylanguage_reactdependencies_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactDependencies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactinfo_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactInfo)


def test_softgallerylanguage_reactinfo_constructor_exists():
    assert callable(softGalleryLanguage_ReactInfo.__init__)


def test_softgallerylanguage_reactinfo_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactInfo.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactlibraries_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactLibraries)


def test_softgallerylanguage_reactlibraries_constructor_exists():
    assert callable(softGalleryLanguage_ReactLibraries.__init__)


def test_softgallerylanguage_reactlibraries_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactLibraries.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactActions)


def test_softgallerylanguage_reactactions_constructor_exists():
    assert callable(softGalleryLanguage_ReactActions.__init__)


def test_softgallerylanguage_reactactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_componentsui_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ComponentsUI)


def test_softgallerylanguage_componentsui_constructor_exists():
    assert callable(softGalleryLanguage_ComponentsUI.__init__)


def test_softgallerylanguage_componentsui_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ComponentsUI.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_componentsui_has_name():
    assert hasattr(softGalleryLanguage_ComponentsUI, "name")
    descriptor = None
    for klass in softGalleryLanguage_ComponentsUI.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactconfiguration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactConfiguration)


def test_softgallerylanguage_reactconfiguration_constructor_exists():
    assert callable(softGalleryLanguage_ReactConfiguration.__init__)


def test_softgallerylanguage_reactconfiguration_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactsubmodules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactSubModules)


def test_softgallerylanguage_reactsubmodules_constructor_exists():
    assert callable(softGalleryLanguage_ReactSubModules.__init__)


def test_softgallerylanguage_reactsubmodules_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactSubModules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_reactmodules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactModules)


def test_softgallerylanguage_reactmodules_constructor_exists():
    assert callable(softGalleryLanguage_ReactModules.__init__)


def test_softgallerylanguage_reactmodules_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactModules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_storageactionmembername_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageActionMemberName)


def test_softgallerylanguage_storageactionmembername_constructor_exists():
    assert callable(softGalleryLanguage_StorageActionMemberName.__init__)


def test_softgallerylanguage_storageactionmembername_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageActionMemberName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageactionmembername_has_name():
    assert hasattr(softGalleryLanguage_StorageActionMemberName, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageActionMemberName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storageactionmembertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageActionMemberType)


def test_softgallerylanguage_storageactionmembertype_constructor_exists():
    assert callable(softGalleryLanguage_StorageActionMemberType.__init__)


def test_softgallerylanguage_storageactionmembertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageActionMemberType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageactionmembertype_has_name():
    assert hasattr(softGalleryLanguage_StorageActionMemberType, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageActionMemberType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storageactionmember_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageActionMember)


def test_softgallerylanguage_storageactionmember_constructor_exists():
    assert callable(softGalleryLanguage_StorageActionMember.__init__)


def test_softgallerylanguage_storageactionmember_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageActionMember.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_storageactionreturn_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageActionReturn)


def test_softgallerylanguage_storageactionreturn_constructor_exists():
    assert callable(softGalleryLanguage_StorageActionReturn.__init__)


def test_softgallerylanguage_storageactionreturn_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageActionReturn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageactionreturn_has_name():
    assert hasattr(softGalleryLanguage_StorageActionReturn, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageActionReturn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storageactionannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageActionAnnotation)


def test_softgallerylanguage_storageactionannotation_constructor_exists():
    assert callable(softGalleryLanguage_StorageActionAnnotation.__init__)


def test_softgallerylanguage_storageactionannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageActionAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageactionannotation_has_name():
    assert hasattr(softGalleryLanguage_StorageActionAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageActionAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storageaction_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageAction)


def test_softgallerylanguage_storageaction_constructor_exists():
    assert callable(softGalleryLanguage_StorageAction.__init__)


def test_softgallerylanguage_storageaction_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageaction_has_name():
    assert hasattr(softGalleryLanguage_StorageAction, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storagememberannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageMemberAnnotation)


def test_softgallerylanguage_storagememberannotation_constructor_exists():
    assert callable(softGalleryLanguage_StorageMemberAnnotation.__init__)


def test_softgallerylanguage_storagememberannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageMemberAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storagememberannotation_has_name():
    assert hasattr(softGalleryLanguage_StorageMemberAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageMemberAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storagemembertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageMemberType)


def test_softgallerylanguage_storagemembertype_constructor_exists():
    assert callable(softGalleryLanguage_StorageMemberType.__init__)


def test_softgallerylanguage_storagemembertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageMemberType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storagemembertype_has_name():
    assert hasattr(softGalleryLanguage_StorageMemberType, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageMemberType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storagemember_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageMember)


def test_softgallerylanguage_storagemember_constructor_exists():
    assert callable(softGalleryLanguage_StorageMember.__init__)


def test_softgallerylanguage_storagemember_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storagemember_has_name():
    assert hasattr(softGalleryLanguage_StorageMember, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_storageclient_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_StorageClient)


def test_softgallerylanguage_storageclient_constructor_exists():
    assert callable(softGalleryLanguage_StorageClient.__init__)


def test_softgallerylanguage_storageclient_constructor_args():
    sig = inspect.signature(softGalleryLanguage_StorageClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_storageclient_has_name():
    assert hasattr(softGalleryLanguage_StorageClient, "name")
    descriptor = None
    for klass in softGalleryLanguage_StorageClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_springentityannotationtypes_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_SpringEntityAnnotationTypes)


def test_softgallerylanguage_springentityannotationtypes_constructor_exists():
    assert callable(softGalleryLanguage_SpringEntityAnnotationTypes.__init__)


def test_softgallerylanguage_springentityannotationtypes_constructor_args():
    sig = inspect.signature(softGalleryLanguage_SpringEntityAnnotationTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_springentityannotationtypes_has_name():
    assert hasattr(softGalleryLanguage_SpringEntityAnnotationTypes, "name")
    descriptor = None
    for klass in softGalleryLanguage_SpringEntityAnnotationTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_reactcomponents_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ReactComponents)


def test_softgallerylanguage_reactcomponents_constructor_exists():
    assert callable(softGalleryLanguage_ReactComponents.__init__)


def test_softgallerylanguage_reactcomponents_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ReactComponents.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage_exceptionprocess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ExceptionProcess)


def test_softgallerylanguage_exceptionprocess_constructor_exists():
    assert callable(softGalleryLanguage_ExceptionProcess.__init__)


def test_softgallerylanguage_exceptionprocess_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ExceptionProcess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_exceptionprocess_has_name():
    assert hasattr(softGalleryLanguage_ExceptionProcess, "name")
    descriptor = None
    for klass in softGalleryLanguage_ExceptionProcess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ExceptionHandler)


def test_softgallerylanguage_exceptionhandler_constructor_exists():
    assert callable(softGalleryLanguage_ExceptionHandler.__init__)


def test_softgallerylanguage_exceptionhandler_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_exceptionhandler_has_name():
    assert hasattr(softGalleryLanguage_ExceptionHandler, "name")
    descriptor = None
    for klass in softGalleryLanguage_ExceptionHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_responseparametername_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ResponseParameterName)


def test_softgallerylanguage_responseparametername_constructor_exists():
    assert callable(softGalleryLanguage_ResponseParameterName.__init__)


def test_softgallerylanguage_responseparametername_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ResponseParameterName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_responseparametername_has_name():
    assert hasattr(softGalleryLanguage_ResponseParameterName, "name")
    descriptor = None
    for klass in softGalleryLanguage_ResponseParameterName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_responseparametertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ResponseParameterType)


def test_softgallerylanguage_responseparametertype_constructor_exists():
    assert callable(softGalleryLanguage_ResponseParameterType.__init__)


def test_softgallerylanguage_responseparametertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ResponseParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_responseparametertype_has_name():
    assert hasattr(softGalleryLanguage_ResponseParameterType, "name")
    descriptor = None
    for klass in softGalleryLanguage_ResponseParameterType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_responseparameterannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_ResponseParameterAnnotation)


def test_softgallerylanguage_responseparameterannotation_constructor_exists():
    assert callable(softGalleryLanguage_ResponseParameterAnnotation.__init__)


def test_softgallerylanguage_responseparameterannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage_ResponseParameterAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_responseparameterannotation_has_name():
    assert hasattr(softGalleryLanguage_ResponseParameterAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage_ResponseParameterAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_deletemapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_DeleteMapping)


def test_softgallerylanguage_deletemapping_constructor_exists():
    assert callable(softGalleryLanguage_DeleteMapping.__init__)


def test_softgallerylanguage_deletemapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage_DeleteMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_deletemapping_has_name():
    assert hasattr(softGalleryLanguage_DeleteMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage_DeleteMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_putmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PutMapping)


def test_softgallerylanguage_putmapping_constructor_exists():
    assert callable(softGalleryLanguage_PutMapping.__init__)


def test_softgallerylanguage_putmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PutMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_putmapping_has_name():
    assert hasattr(softGalleryLanguage_PutMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage_PutMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_getmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_GetMapping)


def test_softgallerylanguage_getmapping_constructor_exists():
    assert callable(softGalleryLanguage_GetMapping.__init__)


def test_softgallerylanguage_getmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage_GetMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_getmapping_has_name():
    assert hasattr(softGalleryLanguage_GetMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage_GetMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_postmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_PostMapping)


def test_softgallerylanguage_postmapping_constructor_exists():
    assert callable(softGalleryLanguage_PostMapping.__init__)


def test_softgallerylanguage_postmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage_PostMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_postmapping_has_name():
    assert hasattr(softGalleryLanguage_PostMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage_PostMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_requestmappingproduces_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RequestMappingProduces)


def test_softgallerylanguage_requestmappingproduces_constructor_exists():
    assert callable(softGalleryLanguage_RequestMappingProduces.__init__)


def test_softgallerylanguage_requestmappingproduces_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RequestMappingProduces.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_requestmappingproduces_has_name():
    assert hasattr(softGalleryLanguage_RequestMappingProduces, "name")
    descriptor = None
    for klass in softGalleryLanguage_RequestMappingProduces.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_requestmappingmethod_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RequestMappingMethod)


def test_softgallerylanguage_requestmappingmethod_constructor_exists():
    assert callable(softGalleryLanguage_RequestMappingMethod.__init__)


def test_softgallerylanguage_requestmappingmethod_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RequestMappingMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_requestmappingmethod_has_name():
    assert hasattr(softGalleryLanguage_RequestMappingMethod, "name")
    descriptor = None
    for klass in softGalleryLanguage_RequestMappingMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage_requestmappingvalue_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage_RequestMappingValue)


def test_softgallerylanguage_requestmappingvalue_constructor_exists():
    assert callable(softGalleryLanguage_RequestMappingValue.__init__)


def test_softgallerylanguage_requestmappingvalue_constructor_args():
    sig = inspect.signature(softGalleryLanguage_RequestMappingValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage_requestmappingvalue_has_name():
    assert hasattr(softGalleryLanguage_RequestMappingValue, "name")
    descriptor = None
    for klass in softGalleryLanguage_RequestMappingValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
MappingType_strategy = st.builds(
    MappingType,
)
softGalleryLanguage_RequestMapping_strategy = st.builds(
    softGalleryLanguage_RequestMapping,
)
softGalleryLanguage_SpringEntity_strategy = st.builds(
    softGalleryLanguage_SpringEntity,
)
softGalleryLanguage_ResponseParameter_strategy = st.builds(
    softGalleryLanguage_ResponseParameter,
)
softGalleryLanguage_MappingType_strategy = st.builds(
    softGalleryLanguage_MappingType,
)
softGalleryLanguage_ResponseEntity_strategy = st.builds(
    softGalleryLanguage_ResponseEntity,
    name=
        safe_text
)
softGalleryLanguage_Autowired_strategy = st.builds(
    softGalleryLanguage_Autowired,
    name=
        safe_text
)
softGalleryLanguage_SearchCriteria_strategy = st.builds(
    softGalleryLanguage_SearchCriteria,
    name=
        safe_text
)
softGalleryLanguage_Predicate_strategy = st.builds(
    softGalleryLanguage_Predicate,
    name=
        safe_text
)
softGalleryLanguage_Specification_strategy = st.builds(
    softGalleryLanguage_Specification,
)
softGalleryLanguage_RestController_strategy = st.builds(
    softGalleryLanguage_RestController,
    name=
        safe_text
)
softGalleryLanguage_SpringRepositoryAnnotation_strategy = st.builds(
    softGalleryLanguage_SpringRepositoryAnnotation,
    name=
        safe_text
)
softGalleryLanguage_SpringRepositories_strategy = st.builds(
    softGalleryLanguage_SpringRepositories,
    name=
        safe_text
)
softGalleryLanguage_SpringRepository_strategy = st.builds(
    softGalleryLanguage_SpringRepository,
)
softGalleryLanguage_OrderSpring_strategy = st.builds(
    softGalleryLanguage_OrderSpring,
    name=
        safe_text
)
softGalleryLanguage_SpringComponent_strategy = st.builds(
    softGalleryLanguage_SpringComponent,
)
softGalleryLanguage_EnableWebSecurity_strategy = st.builds(
    softGalleryLanguage_EnableWebSecurity,
    name=
        safe_text
)
softGalleryLanguage_EnableResourceServer_strategy = st.builds(
    softGalleryLanguage_EnableResourceServer,
    name=
        safe_text
)
softGalleryLanguage_EnableAuthorizationServer_strategy = st.builds(
    softGalleryLanguage_EnableAuthorizationServer,
    name=
        safe_text
)
softGalleryLanguage_EnableGlobalMethodSecurity_strategy = st.builds(
    softGalleryLanguage_EnableGlobalMethodSecurity,
    name=
        safe_text
)
softGalleryLanguage_Configuration_strategy = st.builds(
    softGalleryLanguage_Configuration,
)
softGalleryLanguage_SpringBootApplication_strategy = st.builds(
    softGalleryLanguage_SpringBootApplication,
)
softGalleryLanguage_AmazonWebServices_strategy = st.builds(
    softGalleryLanguage_AmazonWebServices,
    name=
        safe_text
)
softGalleryLanguage_PostgreSQL_strategy = st.builds(
    softGalleryLanguage_PostgreSQL,
    name=
        safe_text
)
softGalleryLanguage_React_strategy = st.builds(
    softGalleryLanguage_React,
    name=
        safe_text
)
softGalleryLanguage_Spring_strategy = st.builds(
    softGalleryLanguage_Spring,
    name=
        safe_text
)
softGalleryLanguage_Technologies_strategy = st.builds(
    softGalleryLanguage_Technologies,
)
softGalleryLanguage_NTiersRelations_strategy = st.builds(
    softGalleryLanguage_NTiersRelations,
    name=
        safe_text
)
softGalleryLanguage_NTierTarget_strategy = st.builds(
    softGalleryLanguage_NTierTarget,
)
softGalleryLanguage_NTierSource_strategy = st.builds(
    softGalleryLanguage_NTierSource,
)
softGalleryLanguage_NTierConnectionContent_strategy = st.builds(
    softGalleryLanguage_NTierConnectionContent,
    nTierName=
        safe_text,
    ntierconnection=
        safe_text
)
softGalleryLanguage_NTiersConnections_strategy = st.builds(
    softGalleryLanguage_NTiersConnections,
)
softGalleryLanguage_PersistenceDataComponent_strategy = st.builds(
    softGalleryLanguage_PersistenceDataComponent,
    name=
        safe_text
)
softGalleryLanguage_BackEnd_strategy = st.builds(
    softGalleryLanguage_BackEnd,
    name=
        safe_text
)
softGalleryLanguage_FrontEnd_strategy = st.builds(
    softGalleryLanguage_FrontEnd,
    name=
        safe_text
)
softGalleryLanguage_ArchitectureComponents_strategy = st.builds(
    softGalleryLanguage_ArchitectureComponents,
)
softGalleryLanguage_LayerTarget_strategy = st.builds(
    softGalleryLanguage_LayerTarget,
    layerelations=
        safe_text
)
softGalleryLanguage_LayerSource_strategy = st.builds(
    softGalleryLanguage_LayerSource,
    layerelations=
        safe_text
)
softGalleryLanguage_Technology_strategy = st.builds(
    softGalleryLanguage_Technology,
    name=
        safe_text
)
softGalleryLanguage_SingleFile_strategy = st.builds(
    softGalleryLanguage_SingleFile,
    name=
        safe_text
)
softGalleryLanguage_MultipleFile_strategy = st.builds(
    softGalleryLanguage_MultipleFile,
    name=
        safe_text
)
softGalleryLanguage_Directories_strategy = st.builds(
    softGalleryLanguage_Directories,
)
softGalleryLanguage_DirectoryContent_strategy = st.builds(
    softGalleryLanguage_DirectoryContent,
    name=
        safe_text
)
softGalleryLanguage_SegmentStructureContent_strategy = st.builds(
    softGalleryLanguage_SegmentStructureContent,
    name=
        safe_text
)
softGalleryLanguage_SegmentStructure_strategy = st.builds(
    softGalleryLanguage_SegmentStructure,
)
softGalleryLanguage_DataPersistenceSegments_strategy = st.builds(
    softGalleryLanguage_DataPersistenceSegments,
    postSName=
        safe_text,
    amazonSName=
        safe_text
)
softGalleryLanguage_DataPersistenceContent_strategy = st.builds(
    softGalleryLanguage_DataPersistenceContent,
)
softGalleryLanguage_DataPersistenceLayer_strategy = st.builds(
    softGalleryLanguage_DataPersistenceLayer,
)
softGalleryLanguage_CriteriaAttributeType_strategy = st.builds(
    softGalleryLanguage_CriteriaAttributeType,
    name=
        safe_text
)
softGalleryLanguage_SpecificationSegmentElement_strategy = st.builds(
    softGalleryLanguage_SpecificationSegmentElement,
    name=
        safe_text
)
softGalleryLanguage_ControllerSegmentElement_strategy = st.builds(
    softGalleryLanguage_ControllerSegmentElement,
    name=
        safe_text
)
softGalleryLanguage_LayerRelations_strategy = st.builds(
    softGalleryLanguage_LayerRelations,
    name=
        safe_text,
    layerelations=
        safe_text
)
softGalleryLanguage_BusinessLogicSegments_strategy = st.builds(
    softGalleryLanguage_BusinessLogicSegments,
    name=
        safe_text
)
softGalleryLanguage_BusinessLogicContent_strategy = st.builds(
    softGalleryLanguage_BusinessLogicContent,
)
softGalleryLanguage_BusinessLogicLayer_strategy = st.builds(
    softGalleryLanguage_BusinessLogicLayer,
)
softGalleryLanguage_PresentationSegments_strategy = st.builds(
    softGalleryLanguage_PresentationSegments,
    presentationCName=
        safe_text,
    presentationAName=
        safe_text,
    presentationSName=
        safe_text
)
softGalleryLanguage_PresentationContent_strategy = st.builds(
    softGalleryLanguage_PresentationContent,
)
softGalleryLanguage_PresentationLayer_strategy = st.builds(
    softGalleryLanguage_PresentationLayer,
)
softGalleryLanguage_Layer_strategy = st.builds(
    softGalleryLanguage_Layer,
)
softGalleryLanguage_NTiers_strategy = st.builds(
    softGalleryLanguage_NTiers,
)
softGalleryLanguage_Architecture_strategy = st.builds(
    softGalleryLanguage_Architecture,
)
softGalleryLanguage_UserException_strategy = st.builds(
    softGalleryLanguage_UserException,
    name=
        safe_text
)
softGalleryLanguage_AlbumException_strategy = st.builds(
    softGalleryLanguage_AlbumException,
    name=
        safe_text
)
softGalleryLanguage_PhotoException_strategy = st.builds(
    softGalleryLanguage_PhotoException,
    name=
        safe_text
)
softGalleryLanguage_LandingFunctions_strategy = st.builds(
    softGalleryLanguage_LandingFunctions,
    passPhotoName=
        safe_text,
    nameCarouselName=
        safe_text
)
softGalleryLanguage_PhotoActionsFunctions_strategy = st.builds(
    softGalleryLanguage_PhotoActionsFunctions,
    nameLoad=
        safe_text,
    nameGenerico=
        safe_text,
    namePhoto=
        safe_text
)
softGalleryLanguage_AlbumManagementFunctions_strategy = st.builds(
    softGalleryLanguage_AlbumManagementFunctions,
    selectAlbName=
        safe_text,
    createdAlbName=
        safe_text
)
softGalleryLanguage_ExceptionsType_strategy = st.builds(
    softGalleryLanguage_ExceptionsType,
)
softGalleryLanguage_AppAccessFunctions_strategy = st.builds(
    softGalleryLanguage_AppAccessFunctions,
    loginName=
        safe_text,
    registerName=
        safe_text
)
softGalleryLanguage_ProfileManagementFunctions_strategy = st.builds(
    softGalleryLanguage_ProfileManagementFunctions,
    viewprofileName=
        safe_text,
    editProfileName=
        safe_text
)
softGalleryLanguage_LandingActions_strategy = st.builds(
    softGalleryLanguage_LandingActions,
)
softGalleryLanguage_PhotoActions_strategy = st.builds(
    softGalleryLanguage_PhotoActions,
)
softGalleryLanguage_AlbumManagement_strategy = st.builds(
    softGalleryLanguage_AlbumManagement,
)
softGalleryLanguage_AppAccess_strategy = st.builds(
    softGalleryLanguage_AppAccess,
)
softGalleryLanguage_ProfileManagement_strategy = st.builds(
    softGalleryLanguage_ProfileManagement,
)
softGalleryLanguage_Functionalities_strategy = st.builds(
    softGalleryLanguage_Functionalities,
)
softGalleryLanguage_AtributeUserDomain_strategy = st.builds(
    softGalleryLanguage_AtributeUserDomain,
    name=
        safe_text
)
softGalleryLanguage_AtributeAlbum_strategy = st.builds(
    softGalleryLanguage_AtributeAlbum,
    name=
        safe_text
)
softGalleryLanguage_AtributePhoto_strategy = st.builds(
    softGalleryLanguage_AtributePhoto,
    name=
        safe_text
)
softGalleryLanguage_Entities_strategy = st.builds(
    softGalleryLanguage_Entities,
    name=
        safe_text
)
softGalleryLanguage_ExceptionsDomain_strategy = st.builds(
    softGalleryLanguage_ExceptionsDomain,
)
softGalleryLanguage_Functionality_strategy = st.builds(
    softGalleryLanguage_Functionality,
)
softGalleryLanguage_Entity_strategy = st.builds(
    softGalleryLanguage_Entity,
)
softGalleryLanguage_Domain_strategy = st.builds(
    softGalleryLanguage_Domain,
    name=
        safe_text
)
softGalleryLanguage_EObject_strategy = st.builds(
    softGalleryLanguage_EObject,
)
softGalleryLanguage_Model_strategy = st.builds(
    softGalleryLanguage_Model,
)
softGalleryLanguage_AmazonElasticComputeCloud_strategy = st.builds(
    softGalleryLanguage_AmazonElasticComputeCloud,
    name=
        safe_text
)
softGalleryLanguage_Metadata_strategy = st.builds(
    softGalleryLanguage_Metadata,
    name=
        safe_text
)
softGalleryLanguage_AmazonFile_strategy = st.builds(
    softGalleryLanguage_AmazonFile,
)
softGalleryLanguage_AmazonFolder_strategy = st.builds(
    softGalleryLanguage_AmazonFolder,
    name=
        safe_text
)
softGalleryLanguage_OnlyAuthorized_strategy = st.builds(
    softGalleryLanguage_OnlyAuthorized,
    name=
        safe_text
)
softGalleryLanguage_BucketObjectsNotPublic_strategy = st.builds(
    softGalleryLanguage_BucketObjectsNotPublic,
    name=
        safe_text
)
softGalleryLanguage_ObjectsPublic_strategy = st.builds(
    softGalleryLanguage_ObjectsPublic,
    name=
        safe_text
)
softGalleryLanguage_BucketAccess_strategy = st.builds(
    softGalleryLanguage_BucketAccess,
)
softGalleryLanguage_Bucket_strategy = st.builds(
    softGalleryLanguage_Bucket,
    name=
        safe_text
)
softGalleryLanguage_BatchOperation_strategy = st.builds(
    softGalleryLanguage_BatchOperation,
    name=
        safe_text
)
softGalleryLanguage_AmazonSimpleStorageService_strategy = st.builds(
    softGalleryLanguage_AmazonSimpleStorageService,
)
softGalleryLanguage_Clause_strategy = st.builds(
    softGalleryLanguage_Clause,
    name=
        safe_text
)
softGalleryLanguage_Query_strategy = st.builds(
    softGalleryLanguage_Query,
)
softGalleryLanguage_Privilege_strategy = st.builds(
    softGalleryLanguage_Privilege,
    name=
        safe_text
)
softGalleryLanguage_PostgresUser_strategy = st.builds(
    softGalleryLanguage_PostgresUser,
    name=
        safe_text
)
softGalleryLanguage_Function_strategy = st.builds(
    softGalleryLanguage_Function,
    name=
        safe_text
)
softGalleryLanguage_Trigger_strategy = st.builds(
    softGalleryLanguage_Trigger,
    name=
        safe_text
)
softGalleryLanguage_Policy_strategy = st.builds(
    softGalleryLanguage_Policy,
    name=
        safe_text
)
softGalleryLanguage_PublicAccess_strategy = st.builds(
    softGalleryLanguage_PublicAccess,
    name=
        safe_text
)
softGalleryLanguage_Constraint_strategy = st.builds(
    softGalleryLanguage_Constraint,
    name=
        safe_text
)
softGalleryLanguage_DatatypeDB_strategy = st.builds(
    softGalleryLanguage_DatatypeDB,
    name=
        safe_text
)
softGalleryLanguage_ColumnP_strategy = st.builds(
    softGalleryLanguage_ColumnP,
    name=
        safe_text
)
softGalleryLanguage_RefTable_p_strategy = st.builds(
    softGalleryLanguage_RefTable_p,
    name=
        safe_text
)
softGalleryLanguage_ForeignKeyRef_strategy = st.builds(
    softGalleryLanguage_ForeignKeyRef,
)
softGalleryLanguage_ForeignKey_n_strategy = st.builds(
    softGalleryLanguage_ForeignKey_n,
    name=
        safe_text
)
softGalleryLanguage_ForeignKey_strategy = st.builds(
    softGalleryLanguage_ForeignKey,
)
softGalleryLanguage_Table_p_strategy = st.builds(
    softGalleryLanguage_Table_p,
    name=
        safe_text
)
softGalleryLanguage_ViewSchema_strategy = st.builds(
    softGalleryLanguage_ViewSchema,
    name=
        safe_text
)
softGalleryLanguage_Index_p_strategy = st.builds(
    softGalleryLanguage_Index_p,
    name=
        safe_text
)
softGalleryLanguage_Schema_strategy = st.builds(
    softGalleryLanguage_Schema,
)
softGalleryLanguage_Database_strategy = st.builds(
    softGalleryLanguage_Database,
    name=
        safe_text
)
softGalleryLanguage_Cluster_strategy = st.builds(
    softGalleryLanguage_Cluster,
)
softGalleryLanguage_Row_strategy = st.builds(
    softGalleryLanguage_Row,
    name=
        safe_text
)
softGalleryLanguage_ReactInformation_strategy = st.builds(
    softGalleryLanguage_ReactInformation,
    name=
        safe_text
)
softGalleryLanguage_ReactLibrary_strategy = st.builds(
    softGalleryLanguage_ReactLibrary,
    name=
        safe_text
)
softGalleryLanguage_ReactsRelationServ_strategy = st.builds(
    softGalleryLanguage_ReactsRelationServ,
    name=
        safe_text
)
softGalleryLanguage_ReactServiceRequestProps_strategy = st.builds(
    softGalleryLanguage_ReactServiceRequestProps,
    reqPropName=
        safe_text,
    reqPropDescription=
        safe_text
)
softGalleryLanguage_ReactServiceContRequest_strategy = st.builds(
    softGalleryLanguage_ReactServiceContRequest,
)
softGalleryLanguage_ReactServiceContent_strategy = st.builds(
    softGalleryLanguage_ReactServiceContent,
    functName=
        safe_text
)
softGalleryLanguage_ReactServicesType_strategy = st.builds(
    softGalleryLanguage_ReactServicesType,
    name=
        safe_text
)
softGalleryLanguage_ReactServicesRelation_strategy = st.builds(
    softGalleryLanguage_ReactServicesRelation,
)
softGalleryLanguage_ReactActionsContent_strategy = st.builds(
    softGalleryLanguage_ReactActionsContent,
)
softGalleryLanguage_StylePropertiesContent_strategy = st.builds(
    softGalleryLanguage_StylePropertiesContent,
    propName=
        safe_text
)
softGalleryLanguage_ComponentsStylesContent_strategy = st.builds(
    softGalleryLanguage_ComponentsStylesContent,
    nameStyle=
        safe_text
)
softGalleryLanguage_PropsType_strategy = st.builds(
    softGalleryLanguage_PropsType,
    nameProps=
        safe_text,
    propsdatas=
        safe_text
)
softGalleryLanguage_StateContent_strategy = st.builds(
    softGalleryLanguage_StateContent,
    stateName=
        safe_text,
    componentdatatyp=
        safe_text
)
softGalleryLanguage_CoreFunctionsDeclaration_strategy = st.builds(
    softGalleryLanguage_CoreFunctionsDeclaration,
    name=
        safe_text
)
softGalleryLanguage_State_strategy = st.builds(
    softGalleryLanguage_State,
)
softGalleryLanguage_ReactCoreFunctions_strategy = st.builds(
    softGalleryLanguage_ReactCoreFunctions,
    name=
        safe_text
)
softGalleryLanguage_ReactConstructor_strategy = st.builds(
    softGalleryLanguage_ReactConstructor,
)
softGalleryLanguage_ReactImportContent_strategy = st.builds(
    softGalleryLanguage_ReactImportContent,
    impName=
        safe_text
)
softGalleryLanguage_StyleProperties_strategy = st.builds(
    softGalleryLanguage_StyleProperties,
)
softGalleryLanguage_Props_strategy = st.builds(
    softGalleryLanguage_Props,
)
softGalleryLanguage_ReactFunctions_strategy = st.builds(
    softGalleryLanguage_ReactFunctions,
    renderclass=
        safe_text,
    lifecycleclass=
        safe_text
)
softGalleryLanguage_ReactImports_strategy = st.builds(
    softGalleryLanguage_ReactImports,
)
softGalleryLanguage_SubcomponentCont_strategy = st.builds(
    softGalleryLanguage_SubcomponentCont,
    nameSubComp=
        safe_text
)
softGalleryLanguage_ViewComponentCont_strategy = st.builds(
    softGalleryLanguage_ViewComponentCont,
    nameView=
        safe_text
)
softGalleryLanguage_UIContent_strategy = st.builds(
    softGalleryLanguage_UIContent,
)
softGalleryLanguage_ComponentClass_strategy = st.builds(
    softGalleryLanguage_ComponentClass,
)
softGalleryLanguage_LogicStructure_strategy = st.builds(
    softGalleryLanguage_LogicStructure,
    appComName=
        safe_text,
    indexCompName=
        safe_text
)
softGalleryLanguage_LogicContent_strategy = st.builds(
    softGalleryLanguage_LogicContent,
    name=
        safe_text
)
softGalleryLanguage_ComponentsStyles_strategy = st.builds(
    softGalleryLanguage_ComponentsStyles,
)
softGalleryLanguage_ComponentsLogic_strategy = st.builds(
    softGalleryLanguage_ComponentsLogic,
    name=
        safe_text
)
softGalleryLanguage_DOMConfigurations_strategy = st.builds(
    softGalleryLanguage_DOMConfigurations,
    name=
        safe_text,
    elements=
        safe_text
)
softGalleryLanguage_PackageVersion_strategy = st.builds(
    softGalleryLanguage_PackageVersion,
    name=
        safe_text
)
softGalleryLanguage_PackageName_strategy = st.builds(
    softGalleryLanguage_PackageName,
    name=
        safe_text
)
softGalleryLanguage_SingleDependencies_strategy = st.builds(
    softGalleryLanguage_SingleDependencies,
)
softGalleryLanguage_ReactDependenciesSubRules_strategy = st.builds(
    softGalleryLanguage_ReactDependenciesSubRules,
)
softGalleryLanguage_ReactDependenciesRules_strategy = st.builds(
    softGalleryLanguage_ReactDependenciesRules,
    name=
        safe_text
)
softGalleryLanguage_ReactConfigurations_strategy = st.builds(
    softGalleryLanguage_ReactConfigurations,
    name=
        safe_text
)
softGalleryLanguage_ReactDependencies_strategy = st.builds(
    softGalleryLanguage_ReactDependencies,
)
softGalleryLanguage_ReactInfo_strategy = st.builds(
    softGalleryLanguage_ReactInfo,
)
softGalleryLanguage_ReactLibraries_strategy = st.builds(
    softGalleryLanguage_ReactLibraries,
)
softGalleryLanguage_ReactActions_strategy = st.builds(
    softGalleryLanguage_ReactActions,
)
softGalleryLanguage_ComponentsUI_strategy = st.builds(
    softGalleryLanguage_ComponentsUI,
    name=
        safe_text
)
softGalleryLanguage_ReactConfiguration_strategy = st.builds(
    softGalleryLanguage_ReactConfiguration,
)
softGalleryLanguage_ReactSubModules_strategy = st.builds(
    softGalleryLanguage_ReactSubModules,
)
softGalleryLanguage_ReactModules_strategy = st.builds(
    softGalleryLanguage_ReactModules,
)
softGalleryLanguage_StorageActionMemberName_strategy = st.builds(
    softGalleryLanguage_StorageActionMemberName,
    name=
        safe_text
)
softGalleryLanguage_StorageActionMemberType_strategy = st.builds(
    softGalleryLanguage_StorageActionMemberType,
    name=
        safe_text
)
softGalleryLanguage_StorageActionMember_strategy = st.builds(
    softGalleryLanguage_StorageActionMember,
)
softGalleryLanguage_StorageActionReturn_strategy = st.builds(
    softGalleryLanguage_StorageActionReturn,
    name=
        safe_text
)
softGalleryLanguage_StorageActionAnnotation_strategy = st.builds(
    softGalleryLanguage_StorageActionAnnotation,
    name=
        safe_text
)
softGalleryLanguage_StorageAction_strategy = st.builds(
    softGalleryLanguage_StorageAction,
    name=
        safe_text
)
softGalleryLanguage_StorageMemberAnnotation_strategy = st.builds(
    softGalleryLanguage_StorageMemberAnnotation,
    name=
        safe_text
)
softGalleryLanguage_StorageMemberType_strategy = st.builds(
    softGalleryLanguage_StorageMemberType,
    name=
        safe_text
)
softGalleryLanguage_StorageMember_strategy = st.builds(
    softGalleryLanguage_StorageMember,
    name=
        safe_text
)
softGalleryLanguage_StorageClient_strategy = st.builds(
    softGalleryLanguage_StorageClient,
    name=
        safe_text
)
softGalleryLanguage_SpringEntityAnnotationTypes_strategy = st.builds(
    softGalleryLanguage_SpringEntityAnnotationTypes,
    name=
        safe_text
)
softGalleryLanguage_ReactComponents_strategy = st.builds(
    softGalleryLanguage_ReactComponents,
)
softGalleryLanguage_ExceptionProcess_strategy = st.builds(
    softGalleryLanguage_ExceptionProcess,
    name=
        safe_text
)
softGalleryLanguage_ExceptionHandler_strategy = st.builds(
    softGalleryLanguage_ExceptionHandler,
    name=
        safe_text
)
softGalleryLanguage_ResponseParameterName_strategy = st.builds(
    softGalleryLanguage_ResponseParameterName,
    name=
        safe_text
)
softGalleryLanguage_ResponseParameterType_strategy = st.builds(
    softGalleryLanguage_ResponseParameterType,
    name=
        safe_text
)
softGalleryLanguage_ResponseParameterAnnotation_strategy = st.builds(
    softGalleryLanguage_ResponseParameterAnnotation,
    name=
        safe_text
)
softGalleryLanguage_DeleteMapping_strategy = st.builds(
    softGalleryLanguage_DeleteMapping,
    name=
        safe_text
)
softGalleryLanguage_PutMapping_strategy = st.builds(
    softGalleryLanguage_PutMapping,
    name=
        safe_text
)
softGalleryLanguage_GetMapping_strategy = st.builds(
    softGalleryLanguage_GetMapping,
    name=
        safe_text
)
softGalleryLanguage_PostMapping_strategy = st.builds(
    softGalleryLanguage_PostMapping,
    name=
        safe_text
)
softGalleryLanguage_RequestMappingProduces_strategy = st.builds(
    softGalleryLanguage_RequestMappingProduces,
    name=
        safe_text
)
softGalleryLanguage_RequestMappingMethod_strategy = st.builds(
    softGalleryLanguage_RequestMappingMethod,
    name=
        safe_text
)
softGalleryLanguage_RequestMappingValue_strategy = st.builds(
    softGalleryLanguage_RequestMappingValue,
    name=
        safe_text
)

@given(instance=MappingType_strategy)
@settings(max_examples=50)
def test_mappingtype_instantiation(instance):
    assert isinstance(instance, MappingType)

@given(instance=softGalleryLanguage_RequestMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_requestmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RequestMapping)

@given(instance=softGalleryLanguage_SpringEntity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springentity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringEntity)

@given(instance=softGalleryLanguage_ResponseParameter_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_responseparameter_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ResponseParameter)

@given(instance=softGalleryLanguage_MappingType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_mappingtype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_MappingType)

@given(instance=softGalleryLanguage_ResponseEntity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_responseentity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ResponseEntity)



@given(instance=softGalleryLanguage_ResponseEntity_strategy)
def test_softgallerylanguage_responseentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Autowired_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_autowired_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Autowired)



@given(instance=softGalleryLanguage_Autowired_strategy)
def test_softgallerylanguage_autowired_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SearchCriteria_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_searchcriteria_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SearchCriteria)



@given(instance=softGalleryLanguage_SearchCriteria_strategy)
def test_softgallerylanguage_searchcriteria_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Predicate_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_predicate_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Predicate)



@given(instance=softGalleryLanguage_Predicate_strategy)
def test_softgallerylanguage_predicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Specification_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_specification_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Specification)

@given(instance=softGalleryLanguage_RestController_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_restcontroller_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RestController)



@given(instance=softGalleryLanguage_RestController_strategy)
def test_softgallerylanguage_restcontroller_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpringRepositoryAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springrepositoryannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringRepositoryAnnotation)



@given(instance=softGalleryLanguage_SpringRepositoryAnnotation_strategy)
def test_softgallerylanguage_springrepositoryannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpringRepositories_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springrepositories_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringRepositories)



@given(instance=softGalleryLanguage_SpringRepositories_strategy)
def test_softgallerylanguage_springrepositories_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpringRepository_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springrepository_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringRepository)

@given(instance=softGalleryLanguage_OrderSpring_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_orderspring_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_OrderSpring)



@given(instance=softGalleryLanguage_OrderSpring_strategy)
def test_softgallerylanguage_orderspring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpringComponent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springcomponent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringComponent)

@given(instance=softGalleryLanguage_EnableWebSecurity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_enablewebsecurity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_EnableWebSecurity)



@given(instance=softGalleryLanguage_EnableWebSecurity_strategy)
def test_softgallerylanguage_enablewebsecurity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_EnableResourceServer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_enableresourceserver_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_EnableResourceServer)



@given(instance=softGalleryLanguage_EnableResourceServer_strategy)
def test_softgallerylanguage_enableresourceserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_EnableAuthorizationServer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_enableauthorizationserver_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_EnableAuthorizationServer)



@given(instance=softGalleryLanguage_EnableAuthorizationServer_strategy)
def test_softgallerylanguage_enableauthorizationserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_EnableGlobalMethodSecurity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_enableglobalmethodsecurity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_EnableGlobalMethodSecurity)



@given(instance=softGalleryLanguage_EnableGlobalMethodSecurity_strategy)
def test_softgallerylanguage_enableglobalmethodsecurity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Configuration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_configuration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Configuration)

@given(instance=softGalleryLanguage_SpringBootApplication_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springbootapplication_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringBootApplication)

@given(instance=softGalleryLanguage_AmazonWebServices_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_amazonwebservices_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AmazonWebServices)



@given(instance=softGalleryLanguage_AmazonWebServices_strategy)
def test_softgallerylanguage_amazonwebservices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PostgreSQL_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_postgresql_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PostgreSQL)



@given(instance=softGalleryLanguage_PostgreSQL_strategy)
def test_softgallerylanguage_postgresql_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_React_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_react_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_React)



@given(instance=softGalleryLanguage_React_strategy)
def test_softgallerylanguage_react_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Spring_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_spring_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Spring)



@given(instance=softGalleryLanguage_Spring_strategy)
def test_softgallerylanguage_spring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Technologies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_technologies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Technologies)

@given(instance=softGalleryLanguage_NTiersRelations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntiersrelations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTiersRelations)



@given(instance=softGalleryLanguage_NTiersRelations_strategy)
def test_softgallerylanguage_ntiersrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_NTierTarget_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntiertarget_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTierTarget)

@given(instance=softGalleryLanguage_NTierSource_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntiersource_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTierSource)

@given(instance=softGalleryLanguage_NTierConnectionContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntierconnectioncontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTierConnectionContent)



@given(instance=softGalleryLanguage_NTierConnectionContent_strategy)
def test_softgallerylanguage_ntierconnectioncontent_nTierName_setter(instance):
    original = instance.nTierName
    instance.nTierName = original
    assert instance.nTierName == original



@given(instance=softGalleryLanguage_NTierConnectionContent_strategy)
def test_softgallerylanguage_ntierconnectioncontent_ntierconnection_setter(instance):
    original = instance.ntierconnection
    instance.ntierconnection = original
    assert instance.ntierconnection == original

@given(instance=softGalleryLanguage_NTiersConnections_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntiersconnections_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTiersConnections)

@given(instance=softGalleryLanguage_PersistenceDataComponent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_persistencedatacomponent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PersistenceDataComponent)



@given(instance=softGalleryLanguage_PersistenceDataComponent_strategy)
def test_softgallerylanguage_persistencedatacomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_BackEnd_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_backend_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BackEnd)



@given(instance=softGalleryLanguage_BackEnd_strategy)
def test_softgallerylanguage_backend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_FrontEnd_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_frontend_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_FrontEnd)



@given(instance=softGalleryLanguage_FrontEnd_strategy)
def test_softgallerylanguage_frontend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ArchitectureComponents_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_architecturecomponents_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ArchitectureComponents)

@given(instance=softGalleryLanguage_LayerTarget_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_layertarget_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LayerTarget)



@given(instance=softGalleryLanguage_LayerTarget_strategy)
def test_softgallerylanguage_layertarget_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage_LayerSource_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_layersource_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LayerSource)



@given(instance=softGalleryLanguage_LayerSource_strategy)
def test_softgallerylanguage_layersource_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage_Technology_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_technology_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Technology)



@given(instance=softGalleryLanguage_Technology_strategy)
def test_softgallerylanguage_technology_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SingleFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_singlefile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SingleFile)



@given(instance=softGalleryLanguage_SingleFile_strategy)
def test_softgallerylanguage_singlefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_MultipleFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_multiplefile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_MultipleFile)



@given(instance=softGalleryLanguage_MultipleFile_strategy)
def test_softgallerylanguage_multiplefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Directories_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_directories_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Directories)

@given(instance=softGalleryLanguage_DirectoryContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_directorycontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DirectoryContent)



@given(instance=softGalleryLanguage_DirectoryContent_strategy)
def test_softgallerylanguage_directorycontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SegmentStructureContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_segmentstructurecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SegmentStructureContent)



@given(instance=softGalleryLanguage_SegmentStructureContent_strategy)
def test_softgallerylanguage_segmentstructurecontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SegmentStructure_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_segmentstructure_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SegmentStructure)

@given(instance=softGalleryLanguage_DataPersistenceSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_datapersistencesegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DataPersistenceSegments)



@given(instance=softGalleryLanguage_DataPersistenceSegments_strategy)
def test_softgallerylanguage_datapersistencesegments_postSName_setter(instance):
    original = instance.postSName
    instance.postSName = original
    assert instance.postSName == original



@given(instance=softGalleryLanguage_DataPersistenceSegments_strategy)
def test_softgallerylanguage_datapersistencesegments_amazonSName_setter(instance):
    original = instance.amazonSName
    instance.amazonSName = original
    assert instance.amazonSName == original

@given(instance=softGalleryLanguage_DataPersistenceContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_datapersistencecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DataPersistenceContent)

@given(instance=softGalleryLanguage_DataPersistenceLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_datapersistencelayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DataPersistenceLayer)

@given(instance=softGalleryLanguage_CriteriaAttributeType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_criteriaattributetype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_CriteriaAttributeType)



@given(instance=softGalleryLanguage_CriteriaAttributeType_strategy)
def test_softgallerylanguage_criteriaattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpecificationSegmentElement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_specificationsegmentelement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpecificationSegmentElement)



@given(instance=softGalleryLanguage_SpecificationSegmentElement_strategy)
def test_softgallerylanguage_specificationsegmentelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ControllerSegmentElement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_controllersegmentelement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ControllerSegmentElement)



@given(instance=softGalleryLanguage_ControllerSegmentElement_strategy)
def test_softgallerylanguage_controllersegmentelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_LayerRelations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_layerrelations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LayerRelations)



@given(instance=softGalleryLanguage_LayerRelations_strategy)
def test_softgallerylanguage_layerrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=softGalleryLanguage_LayerRelations_strategy)
def test_softgallerylanguage_layerrelations_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage_BusinessLogicSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_businesslogicsegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BusinessLogicSegments)



@given(instance=softGalleryLanguage_BusinessLogicSegments_strategy)
def test_softgallerylanguage_businesslogicsegments_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_BusinessLogicContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_businesslogiccontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BusinessLogicContent)

@given(instance=softGalleryLanguage_BusinessLogicLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_businesslogiclayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BusinessLogicLayer)

@given(instance=softGalleryLanguage_PresentationSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_presentationsegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PresentationSegments)



@given(instance=softGalleryLanguage_PresentationSegments_strategy)
def test_softgallerylanguage_presentationsegments_presentationCName_setter(instance):
    original = instance.presentationCName
    instance.presentationCName = original
    assert instance.presentationCName == original



@given(instance=softGalleryLanguage_PresentationSegments_strategy)
def test_softgallerylanguage_presentationsegments_presentationAName_setter(instance):
    original = instance.presentationAName
    instance.presentationAName = original
    assert instance.presentationAName == original



@given(instance=softGalleryLanguage_PresentationSegments_strategy)
def test_softgallerylanguage_presentationsegments_presentationSName_setter(instance):
    original = instance.presentationSName
    instance.presentationSName = original
    assert instance.presentationSName == original

@given(instance=softGalleryLanguage_PresentationContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_presentationcontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PresentationContent)

@given(instance=softGalleryLanguage_PresentationLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_presentationlayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PresentationLayer)

@given(instance=softGalleryLanguage_Layer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_layer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Layer)

@given(instance=softGalleryLanguage_NTiers_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_ntiers_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_NTiers)

@given(instance=softGalleryLanguage_Architecture_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_architecture_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Architecture)

@given(instance=softGalleryLanguage_UserException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_userexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_UserException)



@given(instance=softGalleryLanguage_UserException_strategy)
def test_softgallerylanguage_userexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_AlbumException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_albumexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AlbumException)



@given(instance=softGalleryLanguage_AlbumException_strategy)
def test_softgallerylanguage_albumexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PhotoException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_photoexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PhotoException)



@given(instance=softGalleryLanguage_PhotoException_strategy)
def test_softgallerylanguage_photoexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_LandingFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_landingfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LandingFunctions)



@given(instance=softGalleryLanguage_LandingFunctions_strategy)
def test_softgallerylanguage_landingfunctions_passPhotoName_setter(instance):
    original = instance.passPhotoName
    instance.passPhotoName = original
    assert instance.passPhotoName == original



@given(instance=softGalleryLanguage_LandingFunctions_strategy)
def test_softgallerylanguage_landingfunctions_nameCarouselName_setter(instance):
    original = instance.nameCarouselName
    instance.nameCarouselName = original
    assert instance.nameCarouselName == original

@given(instance=softGalleryLanguage_PhotoActionsFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_photoactionsfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PhotoActionsFunctions)



@given(instance=softGalleryLanguage_PhotoActionsFunctions_strategy)
def test_softgallerylanguage_photoactionsfunctions_nameLoad_setter(instance):
    original = instance.nameLoad
    instance.nameLoad = original
    assert instance.nameLoad == original



@given(instance=softGalleryLanguage_PhotoActionsFunctions_strategy)
def test_softgallerylanguage_photoactionsfunctions_nameGenerico_setter(instance):
    original = instance.nameGenerico
    instance.nameGenerico = original
    assert instance.nameGenerico == original



@given(instance=softGalleryLanguage_PhotoActionsFunctions_strategy)
def test_softgallerylanguage_photoactionsfunctions_namePhoto_setter(instance):
    original = instance.namePhoto
    instance.namePhoto = original
    assert instance.namePhoto == original

@given(instance=softGalleryLanguage_AlbumManagementFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_albummanagementfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AlbumManagementFunctions)



@given(instance=softGalleryLanguage_AlbumManagementFunctions_strategy)
def test_softgallerylanguage_albummanagementfunctions_selectAlbName_setter(instance):
    original = instance.selectAlbName
    instance.selectAlbName = original
    assert instance.selectAlbName == original



@given(instance=softGalleryLanguage_AlbumManagementFunctions_strategy)
def test_softgallerylanguage_albummanagementfunctions_createdAlbName_setter(instance):
    original = instance.createdAlbName
    instance.createdAlbName = original
    assert instance.createdAlbName == original

@given(instance=softGalleryLanguage_ExceptionsType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_exceptionstype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ExceptionsType)

@given(instance=softGalleryLanguage_AppAccessFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_appaccessfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AppAccessFunctions)



@given(instance=softGalleryLanguage_AppAccessFunctions_strategy)
def test_softgallerylanguage_appaccessfunctions_loginName_setter(instance):
    original = instance.loginName
    instance.loginName = original
    assert instance.loginName == original



@given(instance=softGalleryLanguage_AppAccessFunctions_strategy)
def test_softgallerylanguage_appaccessfunctions_registerName_setter(instance):
    original = instance.registerName
    instance.registerName = original
    assert instance.registerName == original

@given(instance=softGalleryLanguage_ProfileManagementFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_profilemanagementfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ProfileManagementFunctions)



@given(instance=softGalleryLanguage_ProfileManagementFunctions_strategy)
def test_softgallerylanguage_profilemanagementfunctions_viewprofileName_setter(instance):
    original = instance.viewprofileName
    instance.viewprofileName = original
    assert instance.viewprofileName == original



@given(instance=softGalleryLanguage_ProfileManagementFunctions_strategy)
def test_softgallerylanguage_profilemanagementfunctions_editProfileName_setter(instance):
    original = instance.editProfileName
    instance.editProfileName = original
    assert instance.editProfileName == original

@given(instance=softGalleryLanguage_LandingActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_landingactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LandingActions)

@given(instance=softGalleryLanguage_PhotoActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_photoactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PhotoActions)

@given(instance=softGalleryLanguage_AlbumManagement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_albummanagement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AlbumManagement)

@given(instance=softGalleryLanguage_AppAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_appaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AppAccess)

@given(instance=softGalleryLanguage_ProfileManagement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_profilemanagement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ProfileManagement)

@given(instance=softGalleryLanguage_Functionalities_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_functionalities_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Functionalities)

@given(instance=softGalleryLanguage_AtributeUserDomain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_atributeuserdomain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AtributeUserDomain)



@given(instance=softGalleryLanguage_AtributeUserDomain_strategy)
def test_softgallerylanguage_atributeuserdomain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_AtributeAlbum_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_atributealbum_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AtributeAlbum)



@given(instance=softGalleryLanguage_AtributeAlbum_strategy)
def test_softgallerylanguage_atributealbum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_AtributePhoto_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_atributephoto_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AtributePhoto)



@given(instance=softGalleryLanguage_AtributePhoto_strategy)
def test_softgallerylanguage_atributephoto_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Entities_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_entities_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Entities)



@given(instance=softGalleryLanguage_Entities_strategy)
def test_softgallerylanguage_entities_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ExceptionsDomain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_exceptionsdomain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ExceptionsDomain)

@given(instance=softGalleryLanguage_Functionality_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_functionality_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Functionality)

@given(instance=softGalleryLanguage_Entity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_entity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Entity)

@given(instance=softGalleryLanguage_Domain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_domain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Domain)



@given(instance=softGalleryLanguage_Domain_strategy)
def test_softgallerylanguage_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_EObject_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_eobject_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_EObject)

@given(instance=softGalleryLanguage_Model_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_model_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Model)

@given(instance=softGalleryLanguage_AmazonElasticComputeCloud_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_amazonelasticcomputecloud_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AmazonElasticComputeCloud)



@given(instance=softGalleryLanguage_AmazonElasticComputeCloud_strategy)
def test_softgallerylanguage_amazonelasticcomputecloud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Metadata_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_metadata_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Metadata)



@given(instance=softGalleryLanguage_Metadata_strategy)
def test_softgallerylanguage_metadata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_AmazonFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_amazonfile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AmazonFile)

@given(instance=softGalleryLanguage_AmazonFolder_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_amazonfolder_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AmazonFolder)



@given(instance=softGalleryLanguage_AmazonFolder_strategy)
def test_softgallerylanguage_amazonfolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_OnlyAuthorized_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_onlyauthorized_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_OnlyAuthorized)



@given(instance=softGalleryLanguage_OnlyAuthorized_strategy)
def test_softgallerylanguage_onlyauthorized_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_BucketObjectsNotPublic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_bucketobjectsnotpublic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BucketObjectsNotPublic)



@given(instance=softGalleryLanguage_BucketObjectsNotPublic_strategy)
def test_softgallerylanguage_bucketobjectsnotpublic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ObjectsPublic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_objectspublic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ObjectsPublic)



@given(instance=softGalleryLanguage_ObjectsPublic_strategy)
def test_softgallerylanguage_objectspublic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_BucketAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_bucketaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BucketAccess)

@given(instance=softGalleryLanguage_Bucket_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_bucket_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Bucket)



@given(instance=softGalleryLanguage_Bucket_strategy)
def test_softgallerylanguage_bucket_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_BatchOperation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_batchoperation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_BatchOperation)



@given(instance=softGalleryLanguage_BatchOperation_strategy)
def test_softgallerylanguage_batchoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_AmazonSimpleStorageService_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_amazonsimplestorageservice_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_AmazonSimpleStorageService)

@given(instance=softGalleryLanguage_Clause_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_clause_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Clause)



@given(instance=softGalleryLanguage_Clause_strategy)
def test_softgallerylanguage_clause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Query_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_query_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Query)

@given(instance=softGalleryLanguage_Privilege_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_privilege_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Privilege)



@given(instance=softGalleryLanguage_Privilege_strategy)
def test_softgallerylanguage_privilege_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PostgresUser_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_postgresuser_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PostgresUser)



@given(instance=softGalleryLanguage_PostgresUser_strategy)
def test_softgallerylanguage_postgresuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Function_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_function_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Function)



@given(instance=softGalleryLanguage_Function_strategy)
def test_softgallerylanguage_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Trigger_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_trigger_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Trigger)



@given(instance=softGalleryLanguage_Trigger_strategy)
def test_softgallerylanguage_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Policy_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_policy_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Policy)



@given(instance=softGalleryLanguage_Policy_strategy)
def test_softgallerylanguage_policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PublicAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_publicaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PublicAccess)



@given(instance=softGalleryLanguage_PublicAccess_strategy)
def test_softgallerylanguage_publicaccess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Constraint_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_constraint_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Constraint)



@given(instance=softGalleryLanguage_Constraint_strategy)
def test_softgallerylanguage_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_DatatypeDB_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_datatypedb_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DatatypeDB)



@given(instance=softGalleryLanguage_DatatypeDB_strategy)
def test_softgallerylanguage_datatypedb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ColumnP_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_columnp_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ColumnP)



@given(instance=softGalleryLanguage_ColumnP_strategy)
def test_softgallerylanguage_columnp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_RefTable_p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reftable_p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RefTable_p)



@given(instance=softGalleryLanguage_RefTable_p_strategy)
def test_softgallerylanguage_reftable_p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ForeignKeyRef_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_foreignkeyref_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ForeignKeyRef)

@given(instance=softGalleryLanguage_ForeignKey_n_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_foreignkey_n_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ForeignKey_n)



@given(instance=softGalleryLanguage_ForeignKey_n_strategy)
def test_softgallerylanguage_foreignkey_n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ForeignKey_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_foreignkey_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ForeignKey)

@given(instance=softGalleryLanguage_Table_p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_table_p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Table_p)



@given(instance=softGalleryLanguage_Table_p_strategy)
def test_softgallerylanguage_table_p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ViewSchema_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_viewschema_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ViewSchema)



@given(instance=softGalleryLanguage_ViewSchema_strategy)
def test_softgallerylanguage_viewschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Index_p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_index_p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Index_p)



@given(instance=softGalleryLanguage_Index_p_strategy)
def test_softgallerylanguage_index_p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Schema_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_schema_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Schema)

@given(instance=softGalleryLanguage_Database_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_database_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Database)



@given(instance=softGalleryLanguage_Database_strategy)
def test_softgallerylanguage_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_Cluster_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_cluster_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Cluster)

@given(instance=softGalleryLanguage_Row_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_row_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Row)



@given(instance=softGalleryLanguage_Row_strategy)
def test_softgallerylanguage_row_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactInformation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactinformation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactInformation)



@given(instance=softGalleryLanguage_ReactInformation_strategy)
def test_softgallerylanguage_reactinformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactLibrary_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactlibrary_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactLibrary)



@given(instance=softGalleryLanguage_ReactLibrary_strategy)
def test_softgallerylanguage_reactlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactsRelationServ_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactsrelationserv_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactsRelationServ)



@given(instance=softGalleryLanguage_ReactsRelationServ_strategy)
def test_softgallerylanguage_reactsrelationserv_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactServiceRequestProps_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactservicerequestprops_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactServiceRequestProps)



@given(instance=softGalleryLanguage_ReactServiceRequestProps_strategy)
def test_softgallerylanguage_reactservicerequestprops_reqPropName_setter(instance):
    original = instance.reqPropName
    instance.reqPropName = original
    assert instance.reqPropName == original



@given(instance=softGalleryLanguage_ReactServiceRequestProps_strategy)
def test_softgallerylanguage_reactservicerequestprops_reqPropDescription_setter(instance):
    original = instance.reqPropDescription
    instance.reqPropDescription = original
    assert instance.reqPropDescription == original

@given(instance=softGalleryLanguage_ReactServiceContRequest_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactservicecontrequest_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactServiceContRequest)

@given(instance=softGalleryLanguage_ReactServiceContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactservicecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactServiceContent)



@given(instance=softGalleryLanguage_ReactServiceContent_strategy)
def test_softgallerylanguage_reactservicecontent_functName_setter(instance):
    original = instance.functName
    instance.functName = original
    assert instance.functName == original

@given(instance=softGalleryLanguage_ReactServicesType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactservicestype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactServicesType)



@given(instance=softGalleryLanguage_ReactServicesType_strategy)
def test_softgallerylanguage_reactservicestype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactServicesRelation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactservicesrelation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactServicesRelation)

@given(instance=softGalleryLanguage_ReactActionsContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactactionscontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactActionsContent)

@given(instance=softGalleryLanguage_StylePropertiesContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_stylepropertiescontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StylePropertiesContent)



@given(instance=softGalleryLanguage_StylePropertiesContent_strategy)
def test_softgallerylanguage_stylepropertiescontent_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=softGalleryLanguage_ComponentsStylesContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_componentsstylescontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ComponentsStylesContent)



@given(instance=softGalleryLanguage_ComponentsStylesContent_strategy)
def test_softgallerylanguage_componentsstylescontent_nameStyle_setter(instance):
    original = instance.nameStyle
    instance.nameStyle = original
    assert instance.nameStyle == original

@given(instance=softGalleryLanguage_PropsType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_propstype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PropsType)



@given(instance=softGalleryLanguage_PropsType_strategy)
def test_softgallerylanguage_propstype_nameProps_setter(instance):
    original = instance.nameProps
    instance.nameProps = original
    assert instance.nameProps == original



@given(instance=softGalleryLanguage_PropsType_strategy)
def test_softgallerylanguage_propstype_propsdatas_setter(instance):
    original = instance.propsdatas
    instance.propsdatas = original
    assert instance.propsdatas == original

@given(instance=softGalleryLanguage_StateContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_statecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StateContent)



@given(instance=softGalleryLanguage_StateContent_strategy)
def test_softgallerylanguage_statecontent_stateName_setter(instance):
    original = instance.stateName
    instance.stateName = original
    assert instance.stateName == original



@given(instance=softGalleryLanguage_StateContent_strategy)
def test_softgallerylanguage_statecontent_componentdatatyp_setter(instance):
    original = instance.componentdatatyp
    instance.componentdatatyp = original
    assert instance.componentdatatyp == original

@given(instance=softGalleryLanguage_CoreFunctionsDeclaration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_corefunctionsdeclaration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_CoreFunctionsDeclaration)



@given(instance=softGalleryLanguage_CoreFunctionsDeclaration_strategy)
def test_softgallerylanguage_corefunctionsdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_State_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_state_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_State)

@given(instance=softGalleryLanguage_ReactCoreFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactcorefunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactCoreFunctions)



@given(instance=softGalleryLanguage_ReactCoreFunctions_strategy)
def test_softgallerylanguage_reactcorefunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactConstructor_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactconstructor_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactConstructor)

@given(instance=softGalleryLanguage_ReactImportContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactimportcontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactImportContent)



@given(instance=softGalleryLanguage_ReactImportContent_strategy)
def test_softgallerylanguage_reactimportcontent_impName_setter(instance):
    original = instance.impName
    instance.impName = original
    assert instance.impName == original

@given(instance=softGalleryLanguage_StyleProperties_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_styleproperties_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StyleProperties)

@given(instance=softGalleryLanguage_Props_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_props_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_Props)

@given(instance=softGalleryLanguage_ReactFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactFunctions)



@given(instance=softGalleryLanguage_ReactFunctions_strategy)
def test_softgallerylanguage_reactfunctions_renderclass_setter(instance):
    original = instance.renderclass
    instance.renderclass = original
    assert instance.renderclass == original



@given(instance=softGalleryLanguage_ReactFunctions_strategy)
def test_softgallerylanguage_reactfunctions_lifecycleclass_setter(instance):
    original = instance.lifecycleclass
    instance.lifecycleclass = original
    assert instance.lifecycleclass == original

@given(instance=softGalleryLanguage_ReactImports_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactimports_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactImports)

@given(instance=softGalleryLanguage_SubcomponentCont_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_subcomponentcont_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SubcomponentCont)



@given(instance=softGalleryLanguage_SubcomponentCont_strategy)
def test_softgallerylanguage_subcomponentcont_nameSubComp_setter(instance):
    original = instance.nameSubComp
    instance.nameSubComp = original
    assert instance.nameSubComp == original

@given(instance=softGalleryLanguage_ViewComponentCont_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_viewcomponentcont_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ViewComponentCont)



@given(instance=softGalleryLanguage_ViewComponentCont_strategy)
def test_softgallerylanguage_viewcomponentcont_nameView_setter(instance):
    original = instance.nameView
    instance.nameView = original
    assert instance.nameView == original

@given(instance=softGalleryLanguage_UIContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_uicontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_UIContent)

@given(instance=softGalleryLanguage_ComponentClass_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_componentclass_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ComponentClass)

@given(instance=softGalleryLanguage_LogicStructure_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_logicstructure_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LogicStructure)



@given(instance=softGalleryLanguage_LogicStructure_strategy)
def test_softgallerylanguage_logicstructure_appComName_setter(instance):
    original = instance.appComName
    instance.appComName = original
    assert instance.appComName == original



@given(instance=softGalleryLanguage_LogicStructure_strategy)
def test_softgallerylanguage_logicstructure_indexCompName_setter(instance):
    original = instance.indexCompName
    instance.indexCompName = original
    assert instance.indexCompName == original

@given(instance=softGalleryLanguage_LogicContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_logiccontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_LogicContent)



@given(instance=softGalleryLanguage_LogicContent_strategy)
def test_softgallerylanguage_logiccontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ComponentsStyles_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_componentsstyles_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ComponentsStyles)

@given(instance=softGalleryLanguage_ComponentsLogic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_componentslogic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ComponentsLogic)



@given(instance=softGalleryLanguage_ComponentsLogic_strategy)
def test_softgallerylanguage_componentslogic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_DOMConfigurations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_domconfigurations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DOMConfigurations)



@given(instance=softGalleryLanguage_DOMConfigurations_strategy)
def test_softgallerylanguage_domconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=softGalleryLanguage_DOMConfigurations_strategy)
def test_softgallerylanguage_domconfigurations_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=softGalleryLanguage_PackageVersion_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_packageversion_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PackageVersion)



@given(instance=softGalleryLanguage_PackageVersion_strategy)
def test_softgallerylanguage_packageversion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PackageName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_packagename_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PackageName)



@given(instance=softGalleryLanguage_PackageName_strategy)
def test_softgallerylanguage_packagename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SingleDependencies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_singledependencies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SingleDependencies)

@given(instance=softGalleryLanguage_ReactDependenciesSubRules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactdependenciessubrules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactDependenciesSubRules)

@given(instance=softGalleryLanguage_ReactDependenciesRules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactdependenciesrules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactDependenciesRules)



@given(instance=softGalleryLanguage_ReactDependenciesRules_strategy)
def test_softgallerylanguage_reactdependenciesrules_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactConfigurations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactconfigurations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactConfigurations)



@given(instance=softGalleryLanguage_ReactConfigurations_strategy)
def test_softgallerylanguage_reactconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactDependencies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactdependencies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactDependencies)

@given(instance=softGalleryLanguage_ReactInfo_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactinfo_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactInfo)

@given(instance=softGalleryLanguage_ReactLibraries_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactlibraries_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactLibraries)

@given(instance=softGalleryLanguage_ReactActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactActions)

@given(instance=softGalleryLanguage_ComponentsUI_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_componentsui_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ComponentsUI)



@given(instance=softGalleryLanguage_ComponentsUI_strategy)
def test_softgallerylanguage_componentsui_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactConfiguration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactconfiguration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactConfiguration)

@given(instance=softGalleryLanguage_ReactSubModules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactsubmodules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactSubModules)

@given(instance=softGalleryLanguage_ReactModules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactmodules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactModules)

@given(instance=softGalleryLanguage_StorageActionMemberName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageactionmembername_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageActionMemberName)



@given(instance=softGalleryLanguage_StorageActionMemberName_strategy)
def test_softgallerylanguage_storageactionmembername_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageActionMemberType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageactionmembertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageActionMemberType)



@given(instance=softGalleryLanguage_StorageActionMemberType_strategy)
def test_softgallerylanguage_storageactionmembertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageActionMember_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageactionmember_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageActionMember)

@given(instance=softGalleryLanguage_StorageActionReturn_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageactionreturn_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageActionReturn)



@given(instance=softGalleryLanguage_StorageActionReturn_strategy)
def test_softgallerylanguage_storageactionreturn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageActionAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageactionannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageActionAnnotation)



@given(instance=softGalleryLanguage_StorageActionAnnotation_strategy)
def test_softgallerylanguage_storageactionannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageAction_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageaction_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageAction)



@given(instance=softGalleryLanguage_StorageAction_strategy)
def test_softgallerylanguage_storageaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageMemberAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storagememberannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageMemberAnnotation)



@given(instance=softGalleryLanguage_StorageMemberAnnotation_strategy)
def test_softgallerylanguage_storagememberannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageMemberType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storagemembertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageMemberType)



@given(instance=softGalleryLanguage_StorageMemberType_strategy)
def test_softgallerylanguage_storagemembertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageMember_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storagemember_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageMember)



@given(instance=softGalleryLanguage_StorageMember_strategy)
def test_softgallerylanguage_storagemember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_StorageClient_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_storageclient_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_StorageClient)



@given(instance=softGalleryLanguage_StorageClient_strategy)
def test_softgallerylanguage_storageclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_SpringEntityAnnotationTypes_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_springentityannotationtypes_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_SpringEntityAnnotationTypes)



@given(instance=softGalleryLanguage_SpringEntityAnnotationTypes_strategy)
def test_softgallerylanguage_springentityannotationtypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ReactComponents_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_reactcomponents_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ReactComponents)

@given(instance=softGalleryLanguage_ExceptionProcess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_exceptionprocess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ExceptionProcess)



@given(instance=softGalleryLanguage_ExceptionProcess_strategy)
def test_softgallerylanguage_exceptionprocess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_exceptionhandler_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ExceptionHandler)



@given(instance=softGalleryLanguage_ExceptionHandler_strategy)
def test_softgallerylanguage_exceptionhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ResponseParameterName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_responseparametername_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ResponseParameterName)



@given(instance=softGalleryLanguage_ResponseParameterName_strategy)
def test_softgallerylanguage_responseparametername_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ResponseParameterType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_responseparametertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ResponseParameterType)



@given(instance=softGalleryLanguage_ResponseParameterType_strategy)
def test_softgallerylanguage_responseparametertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_ResponseParameterAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_responseparameterannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_ResponseParameterAnnotation)



@given(instance=softGalleryLanguage_ResponseParameterAnnotation_strategy)
def test_softgallerylanguage_responseparameterannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_DeleteMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_deletemapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_DeleteMapping)



@given(instance=softGalleryLanguage_DeleteMapping_strategy)
def test_softgallerylanguage_deletemapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PutMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_putmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PutMapping)



@given(instance=softGalleryLanguage_PutMapping_strategy)
def test_softgallerylanguage_putmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_GetMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_getmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_GetMapping)



@given(instance=softGalleryLanguage_GetMapping_strategy)
def test_softgallerylanguage_getmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_PostMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_postmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_PostMapping)



@given(instance=softGalleryLanguage_PostMapping_strategy)
def test_softgallerylanguage_postmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_RequestMappingProduces_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_requestmappingproduces_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RequestMappingProduces)



@given(instance=softGalleryLanguage_RequestMappingProduces_strategy)
def test_softgallerylanguage_requestmappingproduces_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_RequestMappingMethod_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_requestmappingmethod_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RequestMappingMethod)



@given(instance=softGalleryLanguage_RequestMappingMethod_strategy)
def test_softgallerylanguage_requestmappingmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage_RequestMappingValue_strategy)
@settings(max_examples=50)
def test_softgallerylanguage_requestmappingvalue_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage_RequestMappingValue)



@given(instance=softGalleryLanguage_RequestMappingValue_strategy)
def test_softgallerylanguage_requestmappingvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
