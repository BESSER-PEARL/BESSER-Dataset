import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    softGalleryLanguage::RequestMappingProduces,
    softGalleryLanguage::RequestMappingMethod,
    softGalleryLanguage::RequestMappingValue,
    MappingType,
    softGalleryLanguage::GetMapping,
    softGalleryLanguage::PutMapping,
    softGalleryLanguage::DeleteMapping,
    softGalleryLanguage::PostMapping,
    softGalleryLanguage::RequestMapping,
    softGalleryLanguage::SpringEntity,
    softGalleryLanguage::ResponseParameter,
    softGalleryLanguage::MappingType,
    softGalleryLanguage::ResponseEntity,
    softGalleryLanguage::Autowired,
    softGalleryLanguage::SearchCriteria,
    softGalleryLanguage::Predicate,
    softGalleryLanguage::Specification,
    softGalleryLanguage::RestController,
    softGalleryLanguage::SpringRepositoryAnnotation,
    softGalleryLanguage::SpringRepositories,
    softGalleryLanguage::SpringRepository,
    softGalleryLanguage::OrderSpring,
    softGalleryLanguage::SpringComponent,
    softGalleryLanguage::EnableWebSecurity,
    softGalleryLanguage::EnableResourceServer,
    softGalleryLanguage::EnableAuthorizationServer,
    softGalleryLanguage::EnableGlobalMethodSecurity,
    softGalleryLanguage::Configuration,
    softGalleryLanguage::SpringBootApplication,
    softGalleryLanguage::AmazonWebServices,
    softGalleryLanguage::PostgreSQL,
    softGalleryLanguage::React,
    softGalleryLanguage::Spring,
    softGalleryLanguage::Technologies,
    softGalleryLanguage::NTiersRelations,
    softGalleryLanguage::NTierTarget,
    softGalleryLanguage::NTierSource,
    softGalleryLanguage::NTierConnectionContent,
    softGalleryLanguage::NTiersConnections,
    softGalleryLanguage::PersistenceDataComponent,
    softGalleryLanguage::BackEnd,
    softGalleryLanguage::FrontEnd,
    softGalleryLanguage::ArchitectureComponents,
    softGalleryLanguage::LayerTarget,
    softGalleryLanguage::LayerSource,
    softGalleryLanguage::Technology,
    softGalleryLanguage::SingleFile,
    softGalleryLanguage::MultipleFile,
    softGalleryLanguage::Directories,
    softGalleryLanguage::DirectoryContent,
    softGalleryLanguage::SegmentStructureContent,
    softGalleryLanguage::SegmentStructure,
    softGalleryLanguage::DataPersistenceSegments,
    softGalleryLanguage::DataPersistenceContent,
    softGalleryLanguage::DataPersistenceLayer,
    softGalleryLanguage::CriteriaAttributeType,
    softGalleryLanguage::SpecificationSegmentElement,
    softGalleryLanguage::ControllerSegmentElement,
    softGalleryLanguage::LayerRelations,
    softGalleryLanguage::BusinessLogicSegments,
    softGalleryLanguage::BusinessLogicContent,
    softGalleryLanguage::BusinessLogicLayer,
    softGalleryLanguage::PresentationSegments,
    softGalleryLanguage::PresentationContent,
    softGalleryLanguage::PresentationLayer,
    softGalleryLanguage::Layer,
    softGalleryLanguage::NTiers,
    softGalleryLanguage::Architecture,
    softGalleryLanguage::UserException,
    softGalleryLanguage::AlbumException,
    softGalleryLanguage::PhotoException,
    softGalleryLanguage::LandingFunctions,
    softGalleryLanguage::PhotoActionsFunctions,
    softGalleryLanguage::AlbumManagementFunctions,
    softGalleryLanguage::ExceptionsType,
    softGalleryLanguage::AppAccessFunctions,
    softGalleryLanguage::ProfileManagementFunctions,
    softGalleryLanguage::LandingActions,
    softGalleryLanguage::PhotoActions,
    softGalleryLanguage::AlbumManagement,
    softGalleryLanguage::AmazonElasticComputeCloud,
    softGalleryLanguage::Metadata,
    softGalleryLanguage::AmazonFile,
    softGalleryLanguage::AmazonFolder,
    softGalleryLanguage::OnlyAuthorized,
    softGalleryLanguage::BucketObjectsNotPublic,
    softGalleryLanguage::ObjectsPublic,
    softGalleryLanguage::BucketAccess,
    softGalleryLanguage::Bucket,
    softGalleryLanguage::BatchOperation,
    softGalleryLanguage::AmazonSimpleStorageService,
    softGalleryLanguage::Clause,
    softGalleryLanguage::Query,
    softGalleryLanguage::Privilege,
    softGalleryLanguage::PostgresUser,
    softGalleryLanguage::Function,
    softGalleryLanguage::Trigger,
    softGalleryLanguage::Policy,
    softGalleryLanguage::PublicAccess,
    softGalleryLanguage::Constraint,
    softGalleryLanguage::DatatypeDB,
    softGalleryLanguage::ColumnP,
    softGalleryLanguage::RefTable::p,
    softGalleryLanguage::ForeignKeyRef,
    softGalleryLanguage::ForeignKey::n,
    softGalleryLanguage::ForeignKey,
    softGalleryLanguage::Table::p,
    softGalleryLanguage::ViewSchema,
    softGalleryLanguage::Index::p,
    softGalleryLanguage::Schema,
    softGalleryLanguage::Database,
    softGalleryLanguage::Cluster,
    softGalleryLanguage::Row,
    softGalleryLanguage::ReactInformation,
    softGalleryLanguage::ReactLibrary,
    softGalleryLanguage::ReactsRelationServ,
    softGalleryLanguage::ReactServiceRequestProps,
    softGalleryLanguage::ReactServiceContRequest,
    softGalleryLanguage::ReactServiceContent,
    softGalleryLanguage::ReactServicesType,
    softGalleryLanguage::ReactServicesRelation,
    softGalleryLanguage::ReactActionsContent,
    softGalleryLanguage::StylePropertiesContent,
    softGalleryLanguage::ComponentsStylesContent,
    softGalleryLanguage::PropsType,
    softGalleryLanguage::StateContent,
    softGalleryLanguage::CoreFunctionsDeclaration,
    softGalleryLanguage::State,
    softGalleryLanguage::ReactCoreFunctions,
    softGalleryLanguage::ReactConstructor,
    softGalleryLanguage::ReactImportContent,
    softGalleryLanguage::StyleProperties,
    softGalleryLanguage::Props,
    softGalleryLanguage::ReactFunctions,
    softGalleryLanguage::ReactImports,
    softGalleryLanguage::SubcomponentCont,
    softGalleryLanguage::ViewComponentCont,
    softGalleryLanguage::UIContent,
    softGalleryLanguage::ComponentClass,
    softGalleryLanguage::LogicStructure,
    softGalleryLanguage::LogicContent,
    softGalleryLanguage::ComponentsStyles,
    softGalleryLanguage::ComponentsLogic,
    softGalleryLanguage::DOMConfigurations,
    softGalleryLanguage::PackageVersion,
    softGalleryLanguage::PackageName,
    softGalleryLanguage::SingleDependencies,
    softGalleryLanguage::ReactDependenciesSubRules,
    softGalleryLanguage::ReactDependenciesRules,
    softGalleryLanguage::ReactConfigurations,
    softGalleryLanguage::ReactDependencies,
    softGalleryLanguage::ReactInfo,
    softGalleryLanguage::ReactLibraries,
    softGalleryLanguage::ReactActions,
    softGalleryLanguage::ComponentsUI,
    softGalleryLanguage::ReactConfiguration,
    softGalleryLanguage::ReactSubModules,
    softGalleryLanguage::ReactModules,
    softGalleryLanguage::StorageActionMemberName,
    softGalleryLanguage::StorageActionMemberType,
    softGalleryLanguage::StorageActionMember,
    softGalleryLanguage::StorageActionReturn,
    softGalleryLanguage::StorageActionAnnotation,
    softGalleryLanguage::StorageAction,
    softGalleryLanguage::StorageMemberAnnotation,
    softGalleryLanguage::StorageMemberType,
    softGalleryLanguage::StorageMember,
    softGalleryLanguage::StorageClient,
    softGalleryLanguage::SpringEntityAnnotationTypes,
    softGalleryLanguage::ReactComponents,
    softGalleryLanguage::ExceptionProcess,
    softGalleryLanguage::ExceptionHandler,
    softGalleryLanguage::ResponseParameterName,
    softGalleryLanguage::ResponseParameterType,
    softGalleryLanguage::ResponseParameterAnnotation,
    softGalleryLanguage::AppAccess,
    softGalleryLanguage::ProfileManagement,
    softGalleryLanguage::Functionalities,
    softGalleryLanguage::AtributeUserDomain,
    softGalleryLanguage::AtributeAlbum,
    softGalleryLanguage::AtributePhoto,
    softGalleryLanguage::Entities,
    softGalleryLanguage::ExceptionsDomain,
    softGalleryLanguage::Functionality,
    softGalleryLanguage::Entity,
    softGalleryLanguage::Domain,
    softGalleryLanguage::EObject,
    softGalleryLanguage::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_softgallerylanguage::requestmappingproduces_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RequestMappingProduces)


def test_softgallerylanguage::requestmappingproduces_constructor_exists():
    assert callable(softGalleryLanguage::RequestMappingProduces.__init__)


def test_softgallerylanguage::requestmappingproduces_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RequestMappingProduces.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::requestmappingproduces_has_name():
    assert hasattr(softGalleryLanguage::RequestMappingProduces, "name")
    descriptor = None
    for klass in softGalleryLanguage::RequestMappingProduces.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::requestmappingmethod_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RequestMappingMethod)


def test_softgallerylanguage::requestmappingmethod_constructor_exists():
    assert callable(softGalleryLanguage::RequestMappingMethod.__init__)


def test_softgallerylanguage::requestmappingmethod_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RequestMappingMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::requestmappingmethod_has_name():
    assert hasattr(softGalleryLanguage::RequestMappingMethod, "name")
    descriptor = None
    for klass in softGalleryLanguage::RequestMappingMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::requestmappingvalue_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RequestMappingValue)


def test_softgallerylanguage::requestmappingvalue_constructor_exists():
    assert callable(softGalleryLanguage::RequestMappingValue.__init__)


def test_softgallerylanguage::requestmappingvalue_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RequestMappingValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::requestmappingvalue_has_name():
    assert hasattr(softGalleryLanguage::RequestMappingValue, "name")
    descriptor = None
    for klass in softGalleryLanguage::RequestMappingValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mappingtype_is_not_abstract():
    assert not inspect.isabstract(MappingType)


def test_mappingtype_constructor_exists():
    assert callable(MappingType.__init__)


def test_mappingtype_constructor_args():
    sig = inspect.signature(MappingType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::getmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::GetMapping)


def test_softgallerylanguage::getmapping_constructor_exists():
    assert callable(softGalleryLanguage::GetMapping.__init__)


def test_softgallerylanguage::getmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage::GetMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::getmapping_has_name():
    assert hasattr(softGalleryLanguage::GetMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage::GetMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::putmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PutMapping)


def test_softgallerylanguage::putmapping_constructor_exists():
    assert callable(softGalleryLanguage::PutMapping.__init__)


def test_softgallerylanguage::putmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PutMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::putmapping_has_name():
    assert hasattr(softGalleryLanguage::PutMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage::PutMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::deletemapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DeleteMapping)


def test_softgallerylanguage::deletemapping_constructor_exists():
    assert callable(softGalleryLanguage::DeleteMapping.__init__)


def test_softgallerylanguage::deletemapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DeleteMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::deletemapping_has_name():
    assert hasattr(softGalleryLanguage::DeleteMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage::DeleteMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::postmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PostMapping)


def test_softgallerylanguage::postmapping_constructor_exists():
    assert callable(softGalleryLanguage::PostMapping.__init__)


def test_softgallerylanguage::postmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PostMapping.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::postmapping_has_name():
    assert hasattr(softGalleryLanguage::PostMapping, "name")
    descriptor = None
    for klass in softGalleryLanguage::PostMapping.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::requestmapping_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RequestMapping)


def test_softgallerylanguage::requestmapping_constructor_exists():
    assert callable(softGalleryLanguage::RequestMapping.__init__)


def test_softgallerylanguage::requestmapping_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RequestMapping.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::springentity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringEntity)


def test_softgallerylanguage::springentity_constructor_exists():
    assert callable(softGalleryLanguage::SpringEntity.__init__)


def test_softgallerylanguage::springentity_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringEntity.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::responseparameter_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ResponseParameter)


def test_softgallerylanguage::responseparameter_constructor_exists():
    assert callable(softGalleryLanguage::ResponseParameter.__init__)


def test_softgallerylanguage::responseparameter_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ResponseParameter.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::mappingtype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::MappingType)


def test_softgallerylanguage::mappingtype_constructor_exists():
    assert callable(softGalleryLanguage::MappingType.__init__)


def test_softgallerylanguage::mappingtype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::MappingType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::responseentity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ResponseEntity)


def test_softgallerylanguage::responseentity_constructor_exists():
    assert callable(softGalleryLanguage::ResponseEntity.__init__)


def test_softgallerylanguage::responseentity_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ResponseEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::responseentity_has_name():
    assert hasattr(softGalleryLanguage::ResponseEntity, "name")
    descriptor = None
    for klass in softGalleryLanguage::ResponseEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::autowired_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Autowired)


def test_softgallerylanguage::autowired_constructor_exists():
    assert callable(softGalleryLanguage::Autowired.__init__)


def test_softgallerylanguage::autowired_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Autowired.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::autowired_has_name():
    assert hasattr(softGalleryLanguage::Autowired, "name")
    descriptor = None
    for klass in softGalleryLanguage::Autowired.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::searchcriteria_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SearchCriteria)


def test_softgallerylanguage::searchcriteria_constructor_exists():
    assert callable(softGalleryLanguage::SearchCriteria.__init__)


def test_softgallerylanguage::searchcriteria_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SearchCriteria.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::searchcriteria_has_name():
    assert hasattr(softGalleryLanguage::SearchCriteria, "name")
    descriptor = None
    for klass in softGalleryLanguage::SearchCriteria.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::predicate_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Predicate)


def test_softgallerylanguage::predicate_constructor_exists():
    assert callable(softGalleryLanguage::Predicate.__init__)


def test_softgallerylanguage::predicate_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Predicate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::predicate_has_name():
    assert hasattr(softGalleryLanguage::Predicate, "name")
    descriptor = None
    for klass in softGalleryLanguage::Predicate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::specification_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Specification)


def test_softgallerylanguage::specification_constructor_exists():
    assert callable(softGalleryLanguage::Specification.__init__)


def test_softgallerylanguage::specification_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Specification.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::restcontroller_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RestController)


def test_softgallerylanguage::restcontroller_constructor_exists():
    assert callable(softGalleryLanguage::RestController.__init__)


def test_softgallerylanguage::restcontroller_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RestController.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::restcontroller_has_name():
    assert hasattr(softGalleryLanguage::RestController, "name")
    descriptor = None
    for klass in softGalleryLanguage::RestController.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::springrepositoryannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringRepositoryAnnotation)


def test_softgallerylanguage::springrepositoryannotation_constructor_exists():
    assert callable(softGalleryLanguage::SpringRepositoryAnnotation.__init__)


def test_softgallerylanguage::springrepositoryannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringRepositoryAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::springrepositoryannotation_has_name():
    assert hasattr(softGalleryLanguage::SpringRepositoryAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage::SpringRepositoryAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::springrepositories_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringRepositories)


def test_softgallerylanguage::springrepositories_constructor_exists():
    assert callable(softGalleryLanguage::SpringRepositories.__init__)


def test_softgallerylanguage::springrepositories_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringRepositories.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::springrepositories_has_name():
    assert hasattr(softGalleryLanguage::SpringRepositories, "name")
    descriptor = None
    for klass in softGalleryLanguage::SpringRepositories.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::springrepository_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringRepository)


def test_softgallerylanguage::springrepository_constructor_exists():
    assert callable(softGalleryLanguage::SpringRepository.__init__)


def test_softgallerylanguage::springrepository_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringRepository.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::orderspring_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::OrderSpring)


def test_softgallerylanguage::orderspring_constructor_exists():
    assert callable(softGalleryLanguage::OrderSpring.__init__)


def test_softgallerylanguage::orderspring_constructor_args():
    sig = inspect.signature(softGalleryLanguage::OrderSpring.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::orderspring_has_name():
    assert hasattr(softGalleryLanguage::OrderSpring, "name")
    descriptor = None
    for klass in softGalleryLanguage::OrderSpring.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::springcomponent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringComponent)


def test_softgallerylanguage::springcomponent_constructor_exists():
    assert callable(softGalleryLanguage::SpringComponent.__init__)


def test_softgallerylanguage::springcomponent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringComponent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::enablewebsecurity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::EnableWebSecurity)


def test_softgallerylanguage::enablewebsecurity_constructor_exists():
    assert callable(softGalleryLanguage::EnableWebSecurity.__init__)


def test_softgallerylanguage::enablewebsecurity_constructor_args():
    sig = inspect.signature(softGalleryLanguage::EnableWebSecurity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::enablewebsecurity_has_name():
    assert hasattr(softGalleryLanguage::EnableWebSecurity, "name")
    descriptor = None
    for klass in softGalleryLanguage::EnableWebSecurity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::enableresourceserver_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::EnableResourceServer)


def test_softgallerylanguage::enableresourceserver_constructor_exists():
    assert callable(softGalleryLanguage::EnableResourceServer.__init__)


def test_softgallerylanguage::enableresourceserver_constructor_args():
    sig = inspect.signature(softGalleryLanguage::EnableResourceServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::enableresourceserver_has_name():
    assert hasattr(softGalleryLanguage::EnableResourceServer, "name")
    descriptor = None
    for klass in softGalleryLanguage::EnableResourceServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::enableauthorizationserver_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::EnableAuthorizationServer)


def test_softgallerylanguage::enableauthorizationserver_constructor_exists():
    assert callable(softGalleryLanguage::EnableAuthorizationServer.__init__)


def test_softgallerylanguage::enableauthorizationserver_constructor_args():
    sig = inspect.signature(softGalleryLanguage::EnableAuthorizationServer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::enableauthorizationserver_has_name():
    assert hasattr(softGalleryLanguage::EnableAuthorizationServer, "name")
    descriptor = None
    for klass in softGalleryLanguage::EnableAuthorizationServer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::enableglobalmethodsecurity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::EnableGlobalMethodSecurity)


def test_softgallerylanguage::enableglobalmethodsecurity_constructor_exists():
    assert callable(softGalleryLanguage::EnableGlobalMethodSecurity.__init__)


def test_softgallerylanguage::enableglobalmethodsecurity_constructor_args():
    sig = inspect.signature(softGalleryLanguage::EnableGlobalMethodSecurity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::enableglobalmethodsecurity_has_name():
    assert hasattr(softGalleryLanguage::EnableGlobalMethodSecurity, "name")
    descriptor = None
    for klass in softGalleryLanguage::EnableGlobalMethodSecurity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::configuration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Configuration)


def test_softgallerylanguage::configuration_constructor_exists():
    assert callable(softGalleryLanguage::Configuration.__init__)


def test_softgallerylanguage::configuration_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::springbootapplication_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringBootApplication)


def test_softgallerylanguage::springbootapplication_constructor_exists():
    assert callable(softGalleryLanguage::SpringBootApplication.__init__)


def test_softgallerylanguage::springbootapplication_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringBootApplication.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::amazonwebservices_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AmazonWebServices)


def test_softgallerylanguage::amazonwebservices_constructor_exists():
    assert callable(softGalleryLanguage::AmazonWebServices.__init__)


def test_softgallerylanguage::amazonwebservices_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AmazonWebServices.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::amazonwebservices_has_name():
    assert hasattr(softGalleryLanguage::AmazonWebServices, "name")
    descriptor = None
    for klass in softGalleryLanguage::AmazonWebServices.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::postgresql_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PostgreSQL)


def test_softgallerylanguage::postgresql_constructor_exists():
    assert callable(softGalleryLanguage::PostgreSQL.__init__)


def test_softgallerylanguage::postgresql_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PostgreSQL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::postgresql_has_name():
    assert hasattr(softGalleryLanguage::PostgreSQL, "name")
    descriptor = None
    for klass in softGalleryLanguage::PostgreSQL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::react_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::React)


def test_softgallerylanguage::react_constructor_exists():
    assert callable(softGalleryLanguage::React.__init__)


def test_softgallerylanguage::react_constructor_args():
    sig = inspect.signature(softGalleryLanguage::React.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::react_has_name():
    assert hasattr(softGalleryLanguage::React, "name")
    descriptor = None
    for klass in softGalleryLanguage::React.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::spring_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Spring)


def test_softgallerylanguage::spring_constructor_exists():
    assert callable(softGalleryLanguage::Spring.__init__)


def test_softgallerylanguage::spring_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Spring.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::spring_has_name():
    assert hasattr(softGalleryLanguage::Spring, "name")
    descriptor = None
    for klass in softGalleryLanguage::Spring.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::technologies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Technologies)


def test_softgallerylanguage::technologies_constructor_exists():
    assert callable(softGalleryLanguage::Technologies.__init__)


def test_softgallerylanguage::technologies_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Technologies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::ntiersrelations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTiersRelations)


def test_softgallerylanguage::ntiersrelations_constructor_exists():
    assert callable(softGalleryLanguage::NTiersRelations.__init__)


def test_softgallerylanguage::ntiersrelations_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTiersRelations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::ntiersrelations_has_name():
    assert hasattr(softGalleryLanguage::NTiersRelations, "name")
    descriptor = None
    for klass in softGalleryLanguage::NTiersRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::ntiertarget_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTierTarget)


def test_softgallerylanguage::ntiertarget_constructor_exists():
    assert callable(softGalleryLanguage::NTierTarget.__init__)


def test_softgallerylanguage::ntiertarget_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTierTarget.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::ntiersource_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTierSource)


def test_softgallerylanguage::ntiersource_constructor_exists():
    assert callable(softGalleryLanguage::NTierSource.__init__)


def test_softgallerylanguage::ntiersource_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTierSource.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::ntierconnectioncontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTierConnectionContent)


def test_softgallerylanguage::ntierconnectioncontent_constructor_exists():
    assert callable(softGalleryLanguage::NTierConnectionContent.__init__)


def test_softgallerylanguage::ntierconnectioncontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTierConnectionContent.__init__)
    params = list(sig.parameters.keys())
    assert "nTierName" in params, "Missing parameter 'nTierName'"
    assert "ntierconnection" in params, "Missing parameter 'ntierconnection'"

def test_softgallerylanguage::ntierconnectioncontent_has_nTierName():
    assert hasattr(softGalleryLanguage::NTierConnectionContent, "nTierName")
    descriptor = None
    for klass in softGalleryLanguage::NTierConnectionContent.__mro__:
        if "nTierName" in klass.__dict__:
            descriptor = klass.__dict__["nTierName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::ntierconnectioncontent_has_ntierconnection():
    assert hasattr(softGalleryLanguage::NTierConnectionContent, "ntierconnection")
    descriptor = None
    for klass in softGalleryLanguage::NTierConnectionContent.__mro__:
        if "ntierconnection" in klass.__dict__:
            descriptor = klass.__dict__["ntierconnection"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::ntiersconnections_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTiersConnections)


def test_softgallerylanguage::ntiersconnections_constructor_exists():
    assert callable(softGalleryLanguage::NTiersConnections.__init__)


def test_softgallerylanguage::ntiersconnections_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTiersConnections.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::persistencedatacomponent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PersistenceDataComponent)


def test_softgallerylanguage::persistencedatacomponent_constructor_exists():
    assert callable(softGalleryLanguage::PersistenceDataComponent.__init__)


def test_softgallerylanguage::persistencedatacomponent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PersistenceDataComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::persistencedatacomponent_has_name():
    assert hasattr(softGalleryLanguage::PersistenceDataComponent, "name")
    descriptor = None
    for klass in softGalleryLanguage::PersistenceDataComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::backend_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BackEnd)


def test_softgallerylanguage::backend_constructor_exists():
    assert callable(softGalleryLanguage::BackEnd.__init__)


def test_softgallerylanguage::backend_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BackEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::backend_has_name():
    assert hasattr(softGalleryLanguage::BackEnd, "name")
    descriptor = None
    for klass in softGalleryLanguage::BackEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::frontend_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::FrontEnd)


def test_softgallerylanguage::frontend_constructor_exists():
    assert callable(softGalleryLanguage::FrontEnd.__init__)


def test_softgallerylanguage::frontend_constructor_args():
    sig = inspect.signature(softGalleryLanguage::FrontEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::frontend_has_name():
    assert hasattr(softGalleryLanguage::FrontEnd, "name")
    descriptor = None
    for klass in softGalleryLanguage::FrontEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::architecturecomponents_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ArchitectureComponents)


def test_softgallerylanguage::architecturecomponents_constructor_exists():
    assert callable(softGalleryLanguage::ArchitectureComponents.__init__)


def test_softgallerylanguage::architecturecomponents_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ArchitectureComponents.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::layertarget_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LayerTarget)


def test_softgallerylanguage::layertarget_constructor_exists():
    assert callable(softGalleryLanguage::LayerTarget.__init__)


def test_softgallerylanguage::layertarget_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LayerTarget.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_softgallerylanguage::layertarget_has_layerelations():
    assert hasattr(softGalleryLanguage::LayerTarget, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage::LayerTarget.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::layersource_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LayerSource)


def test_softgallerylanguage::layersource_constructor_exists():
    assert callable(softGalleryLanguage::LayerSource.__init__)


def test_softgallerylanguage::layersource_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LayerSource.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_softgallerylanguage::layersource_has_layerelations():
    assert hasattr(softGalleryLanguage::LayerSource, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage::LayerSource.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::technology_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Technology)


def test_softgallerylanguage::technology_constructor_exists():
    assert callable(softGalleryLanguage::Technology.__init__)


def test_softgallerylanguage::technology_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Technology.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::technology_has_name():
    assert hasattr(softGalleryLanguage::Technology, "name")
    descriptor = None
    for klass in softGalleryLanguage::Technology.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::singlefile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SingleFile)


def test_softgallerylanguage::singlefile_constructor_exists():
    assert callable(softGalleryLanguage::SingleFile.__init__)


def test_softgallerylanguage::singlefile_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SingleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::singlefile_has_name():
    assert hasattr(softGalleryLanguage::SingleFile, "name")
    descriptor = None
    for klass in softGalleryLanguage::SingleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::multiplefile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::MultipleFile)


def test_softgallerylanguage::multiplefile_constructor_exists():
    assert callable(softGalleryLanguage::MultipleFile.__init__)


def test_softgallerylanguage::multiplefile_constructor_args():
    sig = inspect.signature(softGalleryLanguage::MultipleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::multiplefile_has_name():
    assert hasattr(softGalleryLanguage::MultipleFile, "name")
    descriptor = None
    for klass in softGalleryLanguage::MultipleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::directories_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Directories)


def test_softgallerylanguage::directories_constructor_exists():
    assert callable(softGalleryLanguage::Directories.__init__)


def test_softgallerylanguage::directories_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Directories.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::directorycontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DirectoryContent)


def test_softgallerylanguage::directorycontent_constructor_exists():
    assert callable(softGalleryLanguage::DirectoryContent.__init__)


def test_softgallerylanguage::directorycontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DirectoryContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::directorycontent_has_name():
    assert hasattr(softGalleryLanguage::DirectoryContent, "name")
    descriptor = None
    for klass in softGalleryLanguage::DirectoryContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::segmentstructurecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SegmentStructureContent)


def test_softgallerylanguage::segmentstructurecontent_constructor_exists():
    assert callable(softGalleryLanguage::SegmentStructureContent.__init__)


def test_softgallerylanguage::segmentstructurecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SegmentStructureContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::segmentstructurecontent_has_name():
    assert hasattr(softGalleryLanguage::SegmentStructureContent, "name")
    descriptor = None
    for klass in softGalleryLanguage::SegmentStructureContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::segmentstructure_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SegmentStructure)


def test_softgallerylanguage::segmentstructure_constructor_exists():
    assert callable(softGalleryLanguage::SegmentStructure.__init__)


def test_softgallerylanguage::segmentstructure_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SegmentStructure.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::datapersistencesegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DataPersistenceSegments)


def test_softgallerylanguage::datapersistencesegments_constructor_exists():
    assert callable(softGalleryLanguage::DataPersistenceSegments.__init__)


def test_softgallerylanguage::datapersistencesegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DataPersistenceSegments.__init__)
    params = list(sig.parameters.keys())
    assert "amazonSName" in params, "Missing parameter 'amazonSName'"
    assert "postSName" in params, "Missing parameter 'postSName'"

def test_softgallerylanguage::datapersistencesegments_has_amazonSName():
    assert hasattr(softGalleryLanguage::DataPersistenceSegments, "amazonSName")
    descriptor = None
    for klass in softGalleryLanguage::DataPersistenceSegments.__mro__:
        if "amazonSName" in klass.__dict__:
            descriptor = klass.__dict__["amazonSName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::datapersistencesegments_has_postSName():
    assert hasattr(softGalleryLanguage::DataPersistenceSegments, "postSName")
    descriptor = None
    for klass in softGalleryLanguage::DataPersistenceSegments.__mro__:
        if "postSName" in klass.__dict__:
            descriptor = klass.__dict__["postSName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::datapersistencecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DataPersistenceContent)


def test_softgallerylanguage::datapersistencecontent_constructor_exists():
    assert callable(softGalleryLanguage::DataPersistenceContent.__init__)


def test_softgallerylanguage::datapersistencecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DataPersistenceContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::datapersistencelayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DataPersistenceLayer)


def test_softgallerylanguage::datapersistencelayer_constructor_exists():
    assert callable(softGalleryLanguage::DataPersistenceLayer.__init__)


def test_softgallerylanguage::datapersistencelayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DataPersistenceLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::criteriaattributetype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::CriteriaAttributeType)


def test_softgallerylanguage::criteriaattributetype_constructor_exists():
    assert callable(softGalleryLanguage::CriteriaAttributeType.__init__)


def test_softgallerylanguage::criteriaattributetype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::CriteriaAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::criteriaattributetype_has_name():
    assert hasattr(softGalleryLanguage::CriteriaAttributeType, "name")
    descriptor = None
    for klass in softGalleryLanguage::CriteriaAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::specificationsegmentelement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpecificationSegmentElement)


def test_softgallerylanguage::specificationsegmentelement_constructor_exists():
    assert callable(softGalleryLanguage::SpecificationSegmentElement.__init__)


def test_softgallerylanguage::specificationsegmentelement_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpecificationSegmentElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::specificationsegmentelement_has_name():
    assert hasattr(softGalleryLanguage::SpecificationSegmentElement, "name")
    descriptor = None
    for klass in softGalleryLanguage::SpecificationSegmentElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::controllersegmentelement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ControllerSegmentElement)


def test_softgallerylanguage::controllersegmentelement_constructor_exists():
    assert callable(softGalleryLanguage::ControllerSegmentElement.__init__)


def test_softgallerylanguage::controllersegmentelement_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ControllerSegmentElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::controllersegmentelement_has_name():
    assert hasattr(softGalleryLanguage::ControllerSegmentElement, "name")
    descriptor = None
    for klass in softGalleryLanguage::ControllerSegmentElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::layerrelations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LayerRelations)


def test_softgallerylanguage::layerrelations_constructor_exists():
    assert callable(softGalleryLanguage::LayerRelations.__init__)


def test_softgallerylanguage::layerrelations_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LayerRelations.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::layerrelations_has_layerelations():
    assert hasattr(softGalleryLanguage::LayerRelations, "layerelations")
    descriptor = None
    for klass in softGalleryLanguage::LayerRelations.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::layerrelations_has_name():
    assert hasattr(softGalleryLanguage::LayerRelations, "name")
    descriptor = None
    for klass in softGalleryLanguage::LayerRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::businesslogicsegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BusinessLogicSegments)


def test_softgallerylanguage::businesslogicsegments_constructor_exists():
    assert callable(softGalleryLanguage::BusinessLogicSegments.__init__)


def test_softgallerylanguage::businesslogicsegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BusinessLogicSegments.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::businesslogicsegments_has_name():
    assert hasattr(softGalleryLanguage::BusinessLogicSegments, "name")
    descriptor = None
    for klass in softGalleryLanguage::BusinessLogicSegments.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::businesslogiccontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BusinessLogicContent)


def test_softgallerylanguage::businesslogiccontent_constructor_exists():
    assert callable(softGalleryLanguage::BusinessLogicContent.__init__)


def test_softgallerylanguage::businesslogiccontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BusinessLogicContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::businesslogiclayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BusinessLogicLayer)


def test_softgallerylanguage::businesslogiclayer_constructor_exists():
    assert callable(softGalleryLanguage::BusinessLogicLayer.__init__)


def test_softgallerylanguage::businesslogiclayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BusinessLogicLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::presentationsegments_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PresentationSegments)


def test_softgallerylanguage::presentationsegments_constructor_exists():
    assert callable(softGalleryLanguage::PresentationSegments.__init__)


def test_softgallerylanguage::presentationsegments_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PresentationSegments.__init__)
    params = list(sig.parameters.keys())
    assert "presentationSName" in params, "Missing parameter 'presentationSName'"
    assert "presentationAName" in params, "Missing parameter 'presentationAName'"
    assert "presentationCName" in params, "Missing parameter 'presentationCName'"

def test_softgallerylanguage::presentationsegments_has_presentationSName():
    assert hasattr(softGalleryLanguage::PresentationSegments, "presentationSName")
    descriptor = None
    for klass in softGalleryLanguage::PresentationSegments.__mro__:
        if "presentationSName" in klass.__dict__:
            descriptor = klass.__dict__["presentationSName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::presentationsegments_has_presentationAName():
    assert hasattr(softGalleryLanguage::PresentationSegments, "presentationAName")
    descriptor = None
    for klass in softGalleryLanguage::PresentationSegments.__mro__:
        if "presentationAName" in klass.__dict__:
            descriptor = klass.__dict__["presentationAName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::presentationsegments_has_presentationCName():
    assert hasattr(softGalleryLanguage::PresentationSegments, "presentationCName")
    descriptor = None
    for klass in softGalleryLanguage::PresentationSegments.__mro__:
        if "presentationCName" in klass.__dict__:
            descriptor = klass.__dict__["presentationCName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::presentationcontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PresentationContent)


def test_softgallerylanguage::presentationcontent_constructor_exists():
    assert callable(softGalleryLanguage::PresentationContent.__init__)


def test_softgallerylanguage::presentationcontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PresentationContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::presentationlayer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PresentationLayer)


def test_softgallerylanguage::presentationlayer_constructor_exists():
    assert callable(softGalleryLanguage::PresentationLayer.__init__)


def test_softgallerylanguage::presentationlayer_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PresentationLayer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::layer_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Layer)


def test_softgallerylanguage::layer_constructor_exists():
    assert callable(softGalleryLanguage::Layer.__init__)


def test_softgallerylanguage::layer_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Layer.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::ntiers_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::NTiers)


def test_softgallerylanguage::ntiers_constructor_exists():
    assert callable(softGalleryLanguage::NTiers.__init__)


def test_softgallerylanguage::ntiers_constructor_args():
    sig = inspect.signature(softGalleryLanguage::NTiers.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::architecture_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Architecture)


def test_softgallerylanguage::architecture_constructor_exists():
    assert callable(softGalleryLanguage::Architecture.__init__)


def test_softgallerylanguage::architecture_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::userexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::UserException)


def test_softgallerylanguage::userexception_constructor_exists():
    assert callable(softGalleryLanguage::UserException.__init__)


def test_softgallerylanguage::userexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage::UserException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::userexception_has_name():
    assert hasattr(softGalleryLanguage::UserException, "name")
    descriptor = None
    for klass in softGalleryLanguage::UserException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::albumexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AlbumException)


def test_softgallerylanguage::albumexception_constructor_exists():
    assert callable(softGalleryLanguage::AlbumException.__init__)


def test_softgallerylanguage::albumexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AlbumException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::albumexception_has_name():
    assert hasattr(softGalleryLanguage::AlbumException, "name")
    descriptor = None
    for klass in softGalleryLanguage::AlbumException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::photoexception_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PhotoException)


def test_softgallerylanguage::photoexception_constructor_exists():
    assert callable(softGalleryLanguage::PhotoException.__init__)


def test_softgallerylanguage::photoexception_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PhotoException.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::photoexception_has_name():
    assert hasattr(softGalleryLanguage::PhotoException, "name")
    descriptor = None
    for klass in softGalleryLanguage::PhotoException.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::landingfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LandingFunctions)


def test_softgallerylanguage::landingfunctions_constructor_exists():
    assert callable(softGalleryLanguage::LandingFunctions.__init__)


def test_softgallerylanguage::landingfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LandingFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "nameCarouselName" in params, "Missing parameter 'nameCarouselName'"
    assert "passPhotoName" in params, "Missing parameter 'passPhotoName'"

def test_softgallerylanguage::landingfunctions_has_nameCarouselName():
    assert hasattr(softGalleryLanguage::LandingFunctions, "nameCarouselName")
    descriptor = None
    for klass in softGalleryLanguage::LandingFunctions.__mro__:
        if "nameCarouselName" in klass.__dict__:
            descriptor = klass.__dict__["nameCarouselName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::landingfunctions_has_passPhotoName():
    assert hasattr(softGalleryLanguage::LandingFunctions, "passPhotoName")
    descriptor = None
    for klass in softGalleryLanguage::LandingFunctions.__mro__:
        if "passPhotoName" in klass.__dict__:
            descriptor = klass.__dict__["passPhotoName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::photoactionsfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PhotoActionsFunctions)


def test_softgallerylanguage::photoactionsfunctions_constructor_exists():
    assert callable(softGalleryLanguage::PhotoActionsFunctions.__init__)


def test_softgallerylanguage::photoactionsfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PhotoActionsFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "nameLoad" in params, "Missing parameter 'nameLoad'"
    assert "namePhoto" in params, "Missing parameter 'namePhoto'"
    assert "nameGenerico" in params, "Missing parameter 'nameGenerico'"

def test_softgallerylanguage::photoactionsfunctions_has_nameLoad():
    assert hasattr(softGalleryLanguage::PhotoActionsFunctions, "nameLoad")
    descriptor = None
    for klass in softGalleryLanguage::PhotoActionsFunctions.__mro__:
        if "nameLoad" in klass.__dict__:
            descriptor = klass.__dict__["nameLoad"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::photoactionsfunctions_has_namePhoto():
    assert hasattr(softGalleryLanguage::PhotoActionsFunctions, "namePhoto")
    descriptor = None
    for klass in softGalleryLanguage::PhotoActionsFunctions.__mro__:
        if "namePhoto" in klass.__dict__:
            descriptor = klass.__dict__["namePhoto"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::photoactionsfunctions_has_nameGenerico():
    assert hasattr(softGalleryLanguage::PhotoActionsFunctions, "nameGenerico")
    descriptor = None
    for klass in softGalleryLanguage::PhotoActionsFunctions.__mro__:
        if "nameGenerico" in klass.__dict__:
            descriptor = klass.__dict__["nameGenerico"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::albummanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AlbumManagementFunctions)


def test_softgallerylanguage::albummanagementfunctions_constructor_exists():
    assert callable(softGalleryLanguage::AlbumManagementFunctions.__init__)


def test_softgallerylanguage::albummanagementfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AlbumManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "createdAlbName" in params, "Missing parameter 'createdAlbName'"
    assert "selectAlbName" in params, "Missing parameter 'selectAlbName'"

def test_softgallerylanguage::albummanagementfunctions_has_createdAlbName():
    assert hasattr(softGalleryLanguage::AlbumManagementFunctions, "createdAlbName")
    descriptor = None
    for klass in softGalleryLanguage::AlbumManagementFunctions.__mro__:
        if "createdAlbName" in klass.__dict__:
            descriptor = klass.__dict__["createdAlbName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::albummanagementfunctions_has_selectAlbName():
    assert hasattr(softGalleryLanguage::AlbumManagementFunctions, "selectAlbName")
    descriptor = None
    for klass in softGalleryLanguage::AlbumManagementFunctions.__mro__:
        if "selectAlbName" in klass.__dict__:
            descriptor = klass.__dict__["selectAlbName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::exceptionstype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ExceptionsType)


def test_softgallerylanguage::exceptionstype_constructor_exists():
    assert callable(softGalleryLanguage::ExceptionsType.__init__)


def test_softgallerylanguage::exceptionstype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ExceptionsType.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::appaccessfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AppAccessFunctions)


def test_softgallerylanguage::appaccessfunctions_constructor_exists():
    assert callable(softGalleryLanguage::AppAccessFunctions.__init__)


def test_softgallerylanguage::appaccessfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AppAccessFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "registerName" in params, "Missing parameter 'registerName'"
    assert "loginName" in params, "Missing parameter 'loginName'"

def test_softgallerylanguage::appaccessfunctions_has_registerName():
    assert hasattr(softGalleryLanguage::AppAccessFunctions, "registerName")
    descriptor = None
    for klass in softGalleryLanguage::AppAccessFunctions.__mro__:
        if "registerName" in klass.__dict__:
            descriptor = klass.__dict__["registerName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::appaccessfunctions_has_loginName():
    assert hasattr(softGalleryLanguage::AppAccessFunctions, "loginName")
    descriptor = None
    for klass in softGalleryLanguage::AppAccessFunctions.__mro__:
        if "loginName" in klass.__dict__:
            descriptor = klass.__dict__["loginName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::profilemanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ProfileManagementFunctions)


def test_softgallerylanguage::profilemanagementfunctions_constructor_exists():
    assert callable(softGalleryLanguage::ProfileManagementFunctions.__init__)


def test_softgallerylanguage::profilemanagementfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ProfileManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "viewprofileName" in params, "Missing parameter 'viewprofileName'"
    assert "editProfileName" in params, "Missing parameter 'editProfileName'"

def test_softgallerylanguage::profilemanagementfunctions_has_viewprofileName():
    assert hasattr(softGalleryLanguage::ProfileManagementFunctions, "viewprofileName")
    descriptor = None
    for klass in softGalleryLanguage::ProfileManagementFunctions.__mro__:
        if "viewprofileName" in klass.__dict__:
            descriptor = klass.__dict__["viewprofileName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::profilemanagementfunctions_has_editProfileName():
    assert hasattr(softGalleryLanguage::ProfileManagementFunctions, "editProfileName")
    descriptor = None
    for klass in softGalleryLanguage::ProfileManagementFunctions.__mro__:
        if "editProfileName" in klass.__dict__:
            descriptor = klass.__dict__["editProfileName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::landingactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LandingActions)


def test_softgallerylanguage::landingactions_constructor_exists():
    assert callable(softGalleryLanguage::LandingActions.__init__)


def test_softgallerylanguage::landingactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LandingActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::photoactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PhotoActions)


def test_softgallerylanguage::photoactions_constructor_exists():
    assert callable(softGalleryLanguage::PhotoActions.__init__)


def test_softgallerylanguage::photoactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PhotoActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::albummanagement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AlbumManagement)


def test_softgallerylanguage::albummanagement_constructor_exists():
    assert callable(softGalleryLanguage::AlbumManagement.__init__)


def test_softgallerylanguage::albummanagement_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AlbumManagement.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::amazonelasticcomputecloud_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AmazonElasticComputeCloud)


def test_softgallerylanguage::amazonelasticcomputecloud_constructor_exists():
    assert callable(softGalleryLanguage::AmazonElasticComputeCloud.__init__)


def test_softgallerylanguage::amazonelasticcomputecloud_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AmazonElasticComputeCloud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::amazonelasticcomputecloud_has_name():
    assert hasattr(softGalleryLanguage::AmazonElasticComputeCloud, "name")
    descriptor = None
    for klass in softGalleryLanguage::AmazonElasticComputeCloud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::metadata_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Metadata)


def test_softgallerylanguage::metadata_constructor_exists():
    assert callable(softGalleryLanguage::Metadata.__init__)


def test_softgallerylanguage::metadata_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Metadata.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::metadata_has_name():
    assert hasattr(softGalleryLanguage::Metadata, "name")
    descriptor = None
    for klass in softGalleryLanguage::Metadata.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::amazonfile_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AmazonFile)


def test_softgallerylanguage::amazonfile_constructor_exists():
    assert callable(softGalleryLanguage::AmazonFile.__init__)


def test_softgallerylanguage::amazonfile_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AmazonFile.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::amazonfolder_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AmazonFolder)


def test_softgallerylanguage::amazonfolder_constructor_exists():
    assert callable(softGalleryLanguage::AmazonFolder.__init__)


def test_softgallerylanguage::amazonfolder_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AmazonFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::amazonfolder_has_name():
    assert hasattr(softGalleryLanguage::AmazonFolder, "name")
    descriptor = None
    for klass in softGalleryLanguage::AmazonFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::onlyauthorized_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::OnlyAuthorized)


def test_softgallerylanguage::onlyauthorized_constructor_exists():
    assert callable(softGalleryLanguage::OnlyAuthorized.__init__)


def test_softgallerylanguage::onlyauthorized_constructor_args():
    sig = inspect.signature(softGalleryLanguage::OnlyAuthorized.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::onlyauthorized_has_name():
    assert hasattr(softGalleryLanguage::OnlyAuthorized, "name")
    descriptor = None
    for klass in softGalleryLanguage::OnlyAuthorized.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::bucketobjectsnotpublic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BucketObjectsNotPublic)


def test_softgallerylanguage::bucketobjectsnotpublic_constructor_exists():
    assert callable(softGalleryLanguage::BucketObjectsNotPublic.__init__)


def test_softgallerylanguage::bucketobjectsnotpublic_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BucketObjectsNotPublic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::bucketobjectsnotpublic_has_name():
    assert hasattr(softGalleryLanguage::BucketObjectsNotPublic, "name")
    descriptor = None
    for klass in softGalleryLanguage::BucketObjectsNotPublic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::objectspublic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ObjectsPublic)


def test_softgallerylanguage::objectspublic_constructor_exists():
    assert callable(softGalleryLanguage::ObjectsPublic.__init__)


def test_softgallerylanguage::objectspublic_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ObjectsPublic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::objectspublic_has_name():
    assert hasattr(softGalleryLanguage::ObjectsPublic, "name")
    descriptor = None
    for klass in softGalleryLanguage::ObjectsPublic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::bucketaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BucketAccess)


def test_softgallerylanguage::bucketaccess_constructor_exists():
    assert callable(softGalleryLanguage::BucketAccess.__init__)


def test_softgallerylanguage::bucketaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BucketAccess.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::bucket_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Bucket)


def test_softgallerylanguage::bucket_constructor_exists():
    assert callable(softGalleryLanguage::Bucket.__init__)


def test_softgallerylanguage::bucket_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Bucket.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::bucket_has_name():
    assert hasattr(softGalleryLanguage::Bucket, "name")
    descriptor = None
    for klass in softGalleryLanguage::Bucket.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::batchoperation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::BatchOperation)


def test_softgallerylanguage::batchoperation_constructor_exists():
    assert callable(softGalleryLanguage::BatchOperation.__init__)


def test_softgallerylanguage::batchoperation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::BatchOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::batchoperation_has_name():
    assert hasattr(softGalleryLanguage::BatchOperation, "name")
    descriptor = None
    for klass in softGalleryLanguage::BatchOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::amazonsimplestorageservice_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AmazonSimpleStorageService)


def test_softgallerylanguage::amazonsimplestorageservice_constructor_exists():
    assert callable(softGalleryLanguage::AmazonSimpleStorageService.__init__)


def test_softgallerylanguage::amazonsimplestorageservice_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AmazonSimpleStorageService.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::clause_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Clause)


def test_softgallerylanguage::clause_constructor_exists():
    assert callable(softGalleryLanguage::Clause.__init__)


def test_softgallerylanguage::clause_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Clause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::clause_has_name():
    assert hasattr(softGalleryLanguage::Clause, "name")
    descriptor = None
    for klass in softGalleryLanguage::Clause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::query_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Query)


def test_softgallerylanguage::query_constructor_exists():
    assert callable(softGalleryLanguage::Query.__init__)


def test_softgallerylanguage::query_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Query.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::privilege_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Privilege)


def test_softgallerylanguage::privilege_constructor_exists():
    assert callable(softGalleryLanguage::Privilege.__init__)


def test_softgallerylanguage::privilege_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Privilege.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::privilege_has_name():
    assert hasattr(softGalleryLanguage::Privilege, "name")
    descriptor = None
    for klass in softGalleryLanguage::Privilege.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::postgresuser_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PostgresUser)


def test_softgallerylanguage::postgresuser_constructor_exists():
    assert callable(softGalleryLanguage::PostgresUser.__init__)


def test_softgallerylanguage::postgresuser_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PostgresUser.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::postgresuser_has_name():
    assert hasattr(softGalleryLanguage::PostgresUser, "name")
    descriptor = None
    for klass in softGalleryLanguage::PostgresUser.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::function_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Function)


def test_softgallerylanguage::function_constructor_exists():
    assert callable(softGalleryLanguage::Function.__init__)


def test_softgallerylanguage::function_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::function_has_name():
    assert hasattr(softGalleryLanguage::Function, "name")
    descriptor = None
    for klass in softGalleryLanguage::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::trigger_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Trigger)


def test_softgallerylanguage::trigger_constructor_exists():
    assert callable(softGalleryLanguage::Trigger.__init__)


def test_softgallerylanguage::trigger_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::trigger_has_name():
    assert hasattr(softGalleryLanguage::Trigger, "name")
    descriptor = None
    for klass in softGalleryLanguage::Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::policy_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Policy)


def test_softgallerylanguage::policy_constructor_exists():
    assert callable(softGalleryLanguage::Policy.__init__)


def test_softgallerylanguage::policy_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Policy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::policy_has_name():
    assert hasattr(softGalleryLanguage::Policy, "name")
    descriptor = None
    for klass in softGalleryLanguage::Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::publicaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PublicAccess)


def test_softgallerylanguage::publicaccess_constructor_exists():
    assert callable(softGalleryLanguage::PublicAccess.__init__)


def test_softgallerylanguage::publicaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PublicAccess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::publicaccess_has_name():
    assert hasattr(softGalleryLanguage::PublicAccess, "name")
    descriptor = None
    for klass in softGalleryLanguage::PublicAccess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::constraint_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Constraint)


def test_softgallerylanguage::constraint_constructor_exists():
    assert callable(softGalleryLanguage::Constraint.__init__)


def test_softgallerylanguage::constraint_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::constraint_has_name():
    assert hasattr(softGalleryLanguage::Constraint, "name")
    descriptor = None
    for klass in softGalleryLanguage::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::datatypedb_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DatatypeDB)


def test_softgallerylanguage::datatypedb_constructor_exists():
    assert callable(softGalleryLanguage::DatatypeDB.__init__)


def test_softgallerylanguage::datatypedb_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DatatypeDB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::datatypedb_has_name():
    assert hasattr(softGalleryLanguage::DatatypeDB, "name")
    descriptor = None
    for klass in softGalleryLanguage::DatatypeDB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::columnp_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ColumnP)


def test_softgallerylanguage::columnp_constructor_exists():
    assert callable(softGalleryLanguage::ColumnP.__init__)


def test_softgallerylanguage::columnp_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ColumnP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::columnp_has_name():
    assert hasattr(softGalleryLanguage::ColumnP, "name")
    descriptor = None
    for klass in softGalleryLanguage::ColumnP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reftable::p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::RefTable::p)


def test_softgallerylanguage::reftable::p_constructor_exists():
    assert callable(softGalleryLanguage::RefTable::p.__init__)


def test_softgallerylanguage::reftable::p_constructor_args():
    sig = inspect.signature(softGalleryLanguage::RefTable::p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reftable::p_has_name():
    assert hasattr(softGalleryLanguage::RefTable::p, "name")
    descriptor = None
    for klass in softGalleryLanguage::RefTable::p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::foreignkeyref_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ForeignKeyRef)


def test_softgallerylanguage::foreignkeyref_constructor_exists():
    assert callable(softGalleryLanguage::ForeignKeyRef.__init__)


def test_softgallerylanguage::foreignkeyref_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ForeignKeyRef.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::foreignkey::n_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ForeignKey::n)


def test_softgallerylanguage::foreignkey::n_constructor_exists():
    assert callable(softGalleryLanguage::ForeignKey::n.__init__)


def test_softgallerylanguage::foreignkey::n_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ForeignKey::n.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::foreignkey::n_has_name():
    assert hasattr(softGalleryLanguage::ForeignKey::n, "name")
    descriptor = None
    for klass in softGalleryLanguage::ForeignKey::n.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::foreignkey_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ForeignKey)


def test_softgallerylanguage::foreignkey_constructor_exists():
    assert callable(softGalleryLanguage::ForeignKey.__init__)


def test_softgallerylanguage::foreignkey_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::table::p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Table::p)


def test_softgallerylanguage::table::p_constructor_exists():
    assert callable(softGalleryLanguage::Table::p.__init__)


def test_softgallerylanguage::table::p_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Table::p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::table::p_has_name():
    assert hasattr(softGalleryLanguage::Table::p, "name")
    descriptor = None
    for klass in softGalleryLanguage::Table::p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::viewschema_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ViewSchema)


def test_softgallerylanguage::viewschema_constructor_exists():
    assert callable(softGalleryLanguage::ViewSchema.__init__)


def test_softgallerylanguage::viewschema_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ViewSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::viewschema_has_name():
    assert hasattr(softGalleryLanguage::ViewSchema, "name")
    descriptor = None
    for klass in softGalleryLanguage::ViewSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::index::p_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Index::p)


def test_softgallerylanguage::index::p_constructor_exists():
    assert callable(softGalleryLanguage::Index::p.__init__)


def test_softgallerylanguage::index::p_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Index::p.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::index::p_has_name():
    assert hasattr(softGalleryLanguage::Index::p, "name")
    descriptor = None
    for klass in softGalleryLanguage::Index::p.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::schema_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Schema)


def test_softgallerylanguage::schema_constructor_exists():
    assert callable(softGalleryLanguage::Schema.__init__)


def test_softgallerylanguage::schema_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Schema.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::database_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Database)


def test_softgallerylanguage::database_constructor_exists():
    assert callable(softGalleryLanguage::Database.__init__)


def test_softgallerylanguage::database_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::database_has_name():
    assert hasattr(softGalleryLanguage::Database, "name")
    descriptor = None
    for klass in softGalleryLanguage::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::cluster_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Cluster)


def test_softgallerylanguage::cluster_constructor_exists():
    assert callable(softGalleryLanguage::Cluster.__init__)


def test_softgallerylanguage::cluster_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Cluster.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::row_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Row)


def test_softgallerylanguage::row_constructor_exists():
    assert callable(softGalleryLanguage::Row.__init__)


def test_softgallerylanguage::row_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Row.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::row_has_name():
    assert hasattr(softGalleryLanguage::Row, "name")
    descriptor = None
    for klass in softGalleryLanguage::Row.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactinformation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactInformation)


def test_softgallerylanguage::reactinformation_constructor_exists():
    assert callable(softGalleryLanguage::ReactInformation.__init__)


def test_softgallerylanguage::reactinformation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactInformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactinformation_has_name():
    assert hasattr(softGalleryLanguage::ReactInformation, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactInformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactlibrary_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactLibrary)


def test_softgallerylanguage::reactlibrary_constructor_exists():
    assert callable(softGalleryLanguage::ReactLibrary.__init__)


def test_softgallerylanguage::reactlibrary_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactlibrary_has_name():
    assert hasattr(softGalleryLanguage::ReactLibrary, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactsrelationserv_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactsRelationServ)


def test_softgallerylanguage::reactsrelationserv_constructor_exists():
    assert callable(softGalleryLanguage::ReactsRelationServ.__init__)


def test_softgallerylanguage::reactsrelationserv_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactsRelationServ.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactsrelationserv_has_name():
    assert hasattr(softGalleryLanguage::ReactsRelationServ, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactsRelationServ.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactservicerequestprops_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactServiceRequestProps)


def test_softgallerylanguage::reactservicerequestprops_constructor_exists():
    assert callable(softGalleryLanguage::ReactServiceRequestProps.__init__)


def test_softgallerylanguage::reactservicerequestprops_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactServiceRequestProps.__init__)
    params = list(sig.parameters.keys())
    assert "reqPropName" in params, "Missing parameter 'reqPropName'"
    assert "reqPropDescription" in params, "Missing parameter 'reqPropDescription'"

def test_softgallerylanguage::reactservicerequestprops_has_reqPropName():
    assert hasattr(softGalleryLanguage::ReactServiceRequestProps, "reqPropName")
    descriptor = None
    for klass in softGalleryLanguage::ReactServiceRequestProps.__mro__:
        if "reqPropName" in klass.__dict__:
            descriptor = klass.__dict__["reqPropName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::reactservicerequestprops_has_reqPropDescription():
    assert hasattr(softGalleryLanguage::ReactServiceRequestProps, "reqPropDescription")
    descriptor = None
    for klass in softGalleryLanguage::ReactServiceRequestProps.__mro__:
        if "reqPropDescription" in klass.__dict__:
            descriptor = klass.__dict__["reqPropDescription"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactservicecontrequest_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactServiceContRequest)


def test_softgallerylanguage::reactservicecontrequest_constructor_exists():
    assert callable(softGalleryLanguage::ReactServiceContRequest.__init__)


def test_softgallerylanguage::reactservicecontrequest_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactServiceContRequest.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactservicecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactServiceContent)


def test_softgallerylanguage::reactservicecontent_constructor_exists():
    assert callable(softGalleryLanguage::ReactServiceContent.__init__)


def test_softgallerylanguage::reactservicecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactServiceContent.__init__)
    params = list(sig.parameters.keys())
    assert "functName" in params, "Missing parameter 'functName'"

def test_softgallerylanguage::reactservicecontent_has_functName():
    assert hasattr(softGalleryLanguage::ReactServiceContent, "functName")
    descriptor = None
    for klass in softGalleryLanguage::ReactServiceContent.__mro__:
        if "functName" in klass.__dict__:
            descriptor = klass.__dict__["functName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactservicestype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactServicesType)


def test_softgallerylanguage::reactservicestype_constructor_exists():
    assert callable(softGalleryLanguage::ReactServicesType.__init__)


def test_softgallerylanguage::reactservicestype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactServicesType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactservicestype_has_name():
    assert hasattr(softGalleryLanguage::ReactServicesType, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactServicesType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactservicesrelation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactServicesRelation)


def test_softgallerylanguage::reactservicesrelation_constructor_exists():
    assert callable(softGalleryLanguage::ReactServicesRelation.__init__)


def test_softgallerylanguage::reactservicesrelation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactServicesRelation.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactactionscontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactActionsContent)


def test_softgallerylanguage::reactactionscontent_constructor_exists():
    assert callable(softGalleryLanguage::ReactActionsContent.__init__)


def test_softgallerylanguage::reactactionscontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactActionsContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::stylepropertiescontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StylePropertiesContent)


def test_softgallerylanguage::stylepropertiescontent_constructor_exists():
    assert callable(softGalleryLanguage::StylePropertiesContent.__init__)


def test_softgallerylanguage::stylepropertiescontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StylePropertiesContent.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_softgallerylanguage::stylepropertiescontent_has_propName():
    assert hasattr(softGalleryLanguage::StylePropertiesContent, "propName")
    descriptor = None
    for klass in softGalleryLanguage::StylePropertiesContent.__mro__:
        if "propName" in klass.__dict__:
            descriptor = klass.__dict__["propName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::componentsstylescontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ComponentsStylesContent)


def test_softgallerylanguage::componentsstylescontent_constructor_exists():
    assert callable(softGalleryLanguage::ComponentsStylesContent.__init__)


def test_softgallerylanguage::componentsstylescontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ComponentsStylesContent.__init__)
    params = list(sig.parameters.keys())
    assert "nameStyle" in params, "Missing parameter 'nameStyle'"

def test_softgallerylanguage::componentsstylescontent_has_nameStyle():
    assert hasattr(softGalleryLanguage::ComponentsStylesContent, "nameStyle")
    descriptor = None
    for klass in softGalleryLanguage::ComponentsStylesContent.__mro__:
        if "nameStyle" in klass.__dict__:
            descriptor = klass.__dict__["nameStyle"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::propstype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PropsType)


def test_softgallerylanguage::propstype_constructor_exists():
    assert callable(softGalleryLanguage::PropsType.__init__)


def test_softgallerylanguage::propstype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PropsType.__init__)
    params = list(sig.parameters.keys())
    assert "propsdatas" in params, "Missing parameter 'propsdatas'"
    assert "nameProps" in params, "Missing parameter 'nameProps'"

def test_softgallerylanguage::propstype_has_propsdatas():
    assert hasattr(softGalleryLanguage::PropsType, "propsdatas")
    descriptor = None
    for klass in softGalleryLanguage::PropsType.__mro__:
        if "propsdatas" in klass.__dict__:
            descriptor = klass.__dict__["propsdatas"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::propstype_has_nameProps():
    assert hasattr(softGalleryLanguage::PropsType, "nameProps")
    descriptor = None
    for klass in softGalleryLanguage::PropsType.__mro__:
        if "nameProps" in klass.__dict__:
            descriptor = klass.__dict__["nameProps"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::statecontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StateContent)


def test_softgallerylanguage::statecontent_constructor_exists():
    assert callable(softGalleryLanguage::StateContent.__init__)


def test_softgallerylanguage::statecontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StateContent.__init__)
    params = list(sig.parameters.keys())
    assert "stateName" in params, "Missing parameter 'stateName'"
    assert "componentdatatyp" in params, "Missing parameter 'componentdatatyp'"

def test_softgallerylanguage::statecontent_has_stateName():
    assert hasattr(softGalleryLanguage::StateContent, "stateName")
    descriptor = None
    for klass in softGalleryLanguage::StateContent.__mro__:
        if "stateName" in klass.__dict__:
            descriptor = klass.__dict__["stateName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::statecontent_has_componentdatatyp():
    assert hasattr(softGalleryLanguage::StateContent, "componentdatatyp")
    descriptor = None
    for klass in softGalleryLanguage::StateContent.__mro__:
        if "componentdatatyp" in klass.__dict__:
            descriptor = klass.__dict__["componentdatatyp"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::corefunctionsdeclaration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::CoreFunctionsDeclaration)


def test_softgallerylanguage::corefunctionsdeclaration_constructor_exists():
    assert callable(softGalleryLanguage::CoreFunctionsDeclaration.__init__)


def test_softgallerylanguage::corefunctionsdeclaration_constructor_args():
    sig = inspect.signature(softGalleryLanguage::CoreFunctionsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::corefunctionsdeclaration_has_name():
    assert hasattr(softGalleryLanguage::CoreFunctionsDeclaration, "name")
    descriptor = None
    for klass in softGalleryLanguage::CoreFunctionsDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::state_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::State)


def test_softgallerylanguage::state_constructor_exists():
    assert callable(softGalleryLanguage::State.__init__)


def test_softgallerylanguage::state_constructor_args():
    sig = inspect.signature(softGalleryLanguage::State.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactcorefunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactCoreFunctions)


def test_softgallerylanguage::reactcorefunctions_constructor_exists():
    assert callable(softGalleryLanguage::ReactCoreFunctions.__init__)


def test_softgallerylanguage::reactcorefunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactCoreFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactcorefunctions_has_name():
    assert hasattr(softGalleryLanguage::ReactCoreFunctions, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactCoreFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactconstructor_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactConstructor)


def test_softgallerylanguage::reactconstructor_constructor_exists():
    assert callable(softGalleryLanguage::ReactConstructor.__init__)


def test_softgallerylanguage::reactconstructor_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactConstructor.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactimportcontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactImportContent)


def test_softgallerylanguage::reactimportcontent_constructor_exists():
    assert callable(softGalleryLanguage::ReactImportContent.__init__)


def test_softgallerylanguage::reactimportcontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactImportContent.__init__)
    params = list(sig.parameters.keys())
    assert "impName" in params, "Missing parameter 'impName'"

def test_softgallerylanguage::reactimportcontent_has_impName():
    assert hasattr(softGalleryLanguage::ReactImportContent, "impName")
    descriptor = None
    for klass in softGalleryLanguage::ReactImportContent.__mro__:
        if "impName" in klass.__dict__:
            descriptor = klass.__dict__["impName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::styleproperties_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StyleProperties)


def test_softgallerylanguage::styleproperties_constructor_exists():
    assert callable(softGalleryLanguage::StyleProperties.__init__)


def test_softgallerylanguage::styleproperties_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StyleProperties.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::props_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Props)


def test_softgallerylanguage::props_constructor_exists():
    assert callable(softGalleryLanguage::Props.__init__)


def test_softgallerylanguage::props_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Props.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactfunctions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactFunctions)


def test_softgallerylanguage::reactfunctions_constructor_exists():
    assert callable(softGalleryLanguage::ReactFunctions.__init__)


def test_softgallerylanguage::reactfunctions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "lifecycleclass" in params, "Missing parameter 'lifecycleclass'"
    assert "renderclass" in params, "Missing parameter 'renderclass'"

def test_softgallerylanguage::reactfunctions_has_lifecycleclass():
    assert hasattr(softGalleryLanguage::ReactFunctions, "lifecycleclass")
    descriptor = None
    for klass in softGalleryLanguage::ReactFunctions.__mro__:
        if "lifecycleclass" in klass.__dict__:
            descriptor = klass.__dict__["lifecycleclass"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::reactfunctions_has_renderclass():
    assert hasattr(softGalleryLanguage::ReactFunctions, "renderclass")
    descriptor = None
    for klass in softGalleryLanguage::ReactFunctions.__mro__:
        if "renderclass" in klass.__dict__:
            descriptor = klass.__dict__["renderclass"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactimports_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactImports)


def test_softgallerylanguage::reactimports_constructor_exists():
    assert callable(softGalleryLanguage::ReactImports.__init__)


def test_softgallerylanguage::reactimports_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactImports.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::subcomponentcont_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SubcomponentCont)


def test_softgallerylanguage::subcomponentcont_constructor_exists():
    assert callable(softGalleryLanguage::SubcomponentCont.__init__)


def test_softgallerylanguage::subcomponentcont_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SubcomponentCont.__init__)
    params = list(sig.parameters.keys())
    assert "nameSubComp" in params, "Missing parameter 'nameSubComp'"

def test_softgallerylanguage::subcomponentcont_has_nameSubComp():
    assert hasattr(softGalleryLanguage::SubcomponentCont, "nameSubComp")
    descriptor = None
    for klass in softGalleryLanguage::SubcomponentCont.__mro__:
        if "nameSubComp" in klass.__dict__:
            descriptor = klass.__dict__["nameSubComp"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::viewcomponentcont_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ViewComponentCont)


def test_softgallerylanguage::viewcomponentcont_constructor_exists():
    assert callable(softGalleryLanguage::ViewComponentCont.__init__)


def test_softgallerylanguage::viewcomponentcont_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ViewComponentCont.__init__)
    params = list(sig.parameters.keys())
    assert "nameView" in params, "Missing parameter 'nameView'"

def test_softgallerylanguage::viewcomponentcont_has_nameView():
    assert hasattr(softGalleryLanguage::ViewComponentCont, "nameView")
    descriptor = None
    for klass in softGalleryLanguage::ViewComponentCont.__mro__:
        if "nameView" in klass.__dict__:
            descriptor = klass.__dict__["nameView"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::uicontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::UIContent)


def test_softgallerylanguage::uicontent_constructor_exists():
    assert callable(softGalleryLanguage::UIContent.__init__)


def test_softgallerylanguage::uicontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::UIContent.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::componentclass_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ComponentClass)


def test_softgallerylanguage::componentclass_constructor_exists():
    assert callable(softGalleryLanguage::ComponentClass.__init__)


def test_softgallerylanguage::componentclass_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ComponentClass.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::logicstructure_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LogicStructure)


def test_softgallerylanguage::logicstructure_constructor_exists():
    assert callable(softGalleryLanguage::LogicStructure.__init__)


def test_softgallerylanguage::logicstructure_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LogicStructure.__init__)
    params = list(sig.parameters.keys())
    assert "indexCompName" in params, "Missing parameter 'indexCompName'"
    assert "appComName" in params, "Missing parameter 'appComName'"

def test_softgallerylanguage::logicstructure_has_indexCompName():
    assert hasattr(softGalleryLanguage::LogicStructure, "indexCompName")
    descriptor = None
    for klass in softGalleryLanguage::LogicStructure.__mro__:
        if "indexCompName" in klass.__dict__:
            descriptor = klass.__dict__["indexCompName"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::logicstructure_has_appComName():
    assert hasattr(softGalleryLanguage::LogicStructure, "appComName")
    descriptor = None
    for klass in softGalleryLanguage::LogicStructure.__mro__:
        if "appComName" in klass.__dict__:
            descriptor = klass.__dict__["appComName"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::logiccontent_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::LogicContent)


def test_softgallerylanguage::logiccontent_constructor_exists():
    assert callable(softGalleryLanguage::LogicContent.__init__)


def test_softgallerylanguage::logiccontent_constructor_args():
    sig = inspect.signature(softGalleryLanguage::LogicContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::logiccontent_has_name():
    assert hasattr(softGalleryLanguage::LogicContent, "name")
    descriptor = None
    for klass in softGalleryLanguage::LogicContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::componentsstyles_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ComponentsStyles)


def test_softgallerylanguage::componentsstyles_constructor_exists():
    assert callable(softGalleryLanguage::ComponentsStyles.__init__)


def test_softgallerylanguage::componentsstyles_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ComponentsStyles.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::componentslogic_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ComponentsLogic)


def test_softgallerylanguage::componentslogic_constructor_exists():
    assert callable(softGalleryLanguage::ComponentsLogic.__init__)


def test_softgallerylanguage::componentslogic_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ComponentsLogic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::componentslogic_has_name():
    assert hasattr(softGalleryLanguage::ComponentsLogic, "name")
    descriptor = None
    for klass in softGalleryLanguage::ComponentsLogic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::domconfigurations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::DOMConfigurations)


def test_softgallerylanguage::domconfigurations_constructor_exists():
    assert callable(softGalleryLanguage::DOMConfigurations.__init__)


def test_softgallerylanguage::domconfigurations_constructor_args():
    sig = inspect.signature(softGalleryLanguage::DOMConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::domconfigurations_has_elements():
    assert hasattr(softGalleryLanguage::DOMConfigurations, "elements")
    descriptor = None
    for klass in softGalleryLanguage::DOMConfigurations.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_softgallerylanguage::domconfigurations_has_name():
    assert hasattr(softGalleryLanguage::DOMConfigurations, "name")
    descriptor = None
    for klass in softGalleryLanguage::DOMConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::packageversion_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PackageVersion)


def test_softgallerylanguage::packageversion_constructor_exists():
    assert callable(softGalleryLanguage::PackageVersion.__init__)


def test_softgallerylanguage::packageversion_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PackageVersion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::packageversion_has_name():
    assert hasattr(softGalleryLanguage::PackageVersion, "name")
    descriptor = None
    for klass in softGalleryLanguage::PackageVersion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::packagename_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::PackageName)


def test_softgallerylanguage::packagename_constructor_exists():
    assert callable(softGalleryLanguage::PackageName.__init__)


def test_softgallerylanguage::packagename_constructor_args():
    sig = inspect.signature(softGalleryLanguage::PackageName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::packagename_has_name():
    assert hasattr(softGalleryLanguage::PackageName, "name")
    descriptor = None
    for klass in softGalleryLanguage::PackageName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::singledependencies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SingleDependencies)


def test_softgallerylanguage::singledependencies_constructor_exists():
    assert callable(softGalleryLanguage::SingleDependencies.__init__)


def test_softgallerylanguage::singledependencies_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SingleDependencies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactdependenciessubrules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactDependenciesSubRules)


def test_softgallerylanguage::reactdependenciessubrules_constructor_exists():
    assert callable(softGalleryLanguage::ReactDependenciesSubRules.__init__)


def test_softgallerylanguage::reactdependenciessubrules_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactDependenciesSubRules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactdependenciesrules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactDependenciesRules)


def test_softgallerylanguage::reactdependenciesrules_constructor_exists():
    assert callable(softGalleryLanguage::ReactDependenciesRules.__init__)


def test_softgallerylanguage::reactdependenciesrules_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactDependenciesRules.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactdependenciesrules_has_name():
    assert hasattr(softGalleryLanguage::ReactDependenciesRules, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactDependenciesRules.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactconfigurations_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactConfigurations)


def test_softgallerylanguage::reactconfigurations_constructor_exists():
    assert callable(softGalleryLanguage::ReactConfigurations.__init__)


def test_softgallerylanguage::reactconfigurations_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::reactconfigurations_has_name():
    assert hasattr(softGalleryLanguage::ReactConfigurations, "name")
    descriptor = None
    for klass in softGalleryLanguage::ReactConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactdependencies_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactDependencies)


def test_softgallerylanguage::reactdependencies_constructor_exists():
    assert callable(softGalleryLanguage::ReactDependencies.__init__)


def test_softgallerylanguage::reactdependencies_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactDependencies.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactinfo_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactInfo)


def test_softgallerylanguage::reactinfo_constructor_exists():
    assert callable(softGalleryLanguage::ReactInfo.__init__)


def test_softgallerylanguage::reactinfo_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactInfo.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactlibraries_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactLibraries)


def test_softgallerylanguage::reactlibraries_constructor_exists():
    assert callable(softGalleryLanguage::ReactLibraries.__init__)


def test_softgallerylanguage::reactlibraries_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactLibraries.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactactions_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactActions)


def test_softgallerylanguage::reactactions_constructor_exists():
    assert callable(softGalleryLanguage::ReactActions.__init__)


def test_softgallerylanguage::reactactions_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactActions.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::componentsui_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ComponentsUI)


def test_softgallerylanguage::componentsui_constructor_exists():
    assert callable(softGalleryLanguage::ComponentsUI.__init__)


def test_softgallerylanguage::componentsui_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ComponentsUI.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::componentsui_has_name():
    assert hasattr(softGalleryLanguage::ComponentsUI, "name")
    descriptor = None
    for klass in softGalleryLanguage::ComponentsUI.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactconfiguration_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactConfiguration)


def test_softgallerylanguage::reactconfiguration_constructor_exists():
    assert callable(softGalleryLanguage::ReactConfiguration.__init__)


def test_softgallerylanguage::reactconfiguration_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactsubmodules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactSubModules)


def test_softgallerylanguage::reactsubmodules_constructor_exists():
    assert callable(softGalleryLanguage::ReactSubModules.__init__)


def test_softgallerylanguage::reactsubmodules_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactSubModules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::reactmodules_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactModules)


def test_softgallerylanguage::reactmodules_constructor_exists():
    assert callable(softGalleryLanguage::ReactModules.__init__)


def test_softgallerylanguage::reactmodules_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactModules.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::storageactionmembername_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageActionMemberName)


def test_softgallerylanguage::storageactionmembername_constructor_exists():
    assert callable(softGalleryLanguage::StorageActionMemberName.__init__)


def test_softgallerylanguage::storageactionmembername_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageActionMemberName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageactionmembername_has_name():
    assert hasattr(softGalleryLanguage::StorageActionMemberName, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageActionMemberName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storageactionmembertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageActionMemberType)


def test_softgallerylanguage::storageactionmembertype_constructor_exists():
    assert callable(softGalleryLanguage::StorageActionMemberType.__init__)


def test_softgallerylanguage::storageactionmembertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageActionMemberType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageactionmembertype_has_name():
    assert hasattr(softGalleryLanguage::StorageActionMemberType, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageActionMemberType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storageactionmember_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageActionMember)


def test_softgallerylanguage::storageactionmember_constructor_exists():
    assert callable(softGalleryLanguage::StorageActionMember.__init__)


def test_softgallerylanguage::storageactionmember_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageActionMember.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::storageactionreturn_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageActionReturn)


def test_softgallerylanguage::storageactionreturn_constructor_exists():
    assert callable(softGalleryLanguage::StorageActionReturn.__init__)


def test_softgallerylanguage::storageactionreturn_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageActionReturn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageactionreturn_has_name():
    assert hasattr(softGalleryLanguage::StorageActionReturn, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageActionReturn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storageactionannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageActionAnnotation)


def test_softgallerylanguage::storageactionannotation_constructor_exists():
    assert callable(softGalleryLanguage::StorageActionAnnotation.__init__)


def test_softgallerylanguage::storageactionannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageActionAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageactionannotation_has_name():
    assert hasattr(softGalleryLanguage::StorageActionAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageActionAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storageaction_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageAction)


def test_softgallerylanguage::storageaction_constructor_exists():
    assert callable(softGalleryLanguage::StorageAction.__init__)


def test_softgallerylanguage::storageaction_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageaction_has_name():
    assert hasattr(softGalleryLanguage::StorageAction, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storagememberannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageMemberAnnotation)


def test_softgallerylanguage::storagememberannotation_constructor_exists():
    assert callable(softGalleryLanguage::StorageMemberAnnotation.__init__)


def test_softgallerylanguage::storagememberannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageMemberAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storagememberannotation_has_name():
    assert hasattr(softGalleryLanguage::StorageMemberAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageMemberAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storagemembertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageMemberType)


def test_softgallerylanguage::storagemembertype_constructor_exists():
    assert callable(softGalleryLanguage::StorageMemberType.__init__)


def test_softgallerylanguage::storagemembertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageMemberType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storagemembertype_has_name():
    assert hasattr(softGalleryLanguage::StorageMemberType, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageMemberType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storagemember_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageMember)


def test_softgallerylanguage::storagemember_constructor_exists():
    assert callable(softGalleryLanguage::StorageMember.__init__)


def test_softgallerylanguage::storagemember_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storagemember_has_name():
    assert hasattr(softGalleryLanguage::StorageMember, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::storageclient_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::StorageClient)


def test_softgallerylanguage::storageclient_constructor_exists():
    assert callable(softGalleryLanguage::StorageClient.__init__)


def test_softgallerylanguage::storageclient_constructor_args():
    sig = inspect.signature(softGalleryLanguage::StorageClient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::storageclient_has_name():
    assert hasattr(softGalleryLanguage::StorageClient, "name")
    descriptor = None
    for klass in softGalleryLanguage::StorageClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::springentityannotationtypes_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::SpringEntityAnnotationTypes)


def test_softgallerylanguage::springentityannotationtypes_constructor_exists():
    assert callable(softGalleryLanguage::SpringEntityAnnotationTypes.__init__)


def test_softgallerylanguage::springentityannotationtypes_constructor_args():
    sig = inspect.signature(softGalleryLanguage::SpringEntityAnnotationTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::springentityannotationtypes_has_name():
    assert hasattr(softGalleryLanguage::SpringEntityAnnotationTypes, "name")
    descriptor = None
    for klass in softGalleryLanguage::SpringEntityAnnotationTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::reactcomponents_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ReactComponents)


def test_softgallerylanguage::reactcomponents_constructor_exists():
    assert callable(softGalleryLanguage::ReactComponents.__init__)


def test_softgallerylanguage::reactcomponents_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ReactComponents.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::exceptionprocess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ExceptionProcess)


def test_softgallerylanguage::exceptionprocess_constructor_exists():
    assert callable(softGalleryLanguage::ExceptionProcess.__init__)


def test_softgallerylanguage::exceptionprocess_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ExceptionProcess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::exceptionprocess_has_name():
    assert hasattr(softGalleryLanguage::ExceptionProcess, "name")
    descriptor = None
    for klass in softGalleryLanguage::ExceptionProcess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ExceptionHandler)


def test_softgallerylanguage::exceptionhandler_constructor_exists():
    assert callable(softGalleryLanguage::ExceptionHandler.__init__)


def test_softgallerylanguage::exceptionhandler_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::exceptionhandler_has_name():
    assert hasattr(softGalleryLanguage::ExceptionHandler, "name")
    descriptor = None
    for klass in softGalleryLanguage::ExceptionHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::responseparametername_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ResponseParameterName)


def test_softgallerylanguage::responseparametername_constructor_exists():
    assert callable(softGalleryLanguage::ResponseParameterName.__init__)


def test_softgallerylanguage::responseparametername_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ResponseParameterName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::responseparametername_has_name():
    assert hasattr(softGalleryLanguage::ResponseParameterName, "name")
    descriptor = None
    for klass in softGalleryLanguage::ResponseParameterName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::responseparametertype_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ResponseParameterType)


def test_softgallerylanguage::responseparametertype_constructor_exists():
    assert callable(softGalleryLanguage::ResponseParameterType.__init__)


def test_softgallerylanguage::responseparametertype_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ResponseParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::responseparametertype_has_name():
    assert hasattr(softGalleryLanguage::ResponseParameterType, "name")
    descriptor = None
    for klass in softGalleryLanguage::ResponseParameterType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::responseparameterannotation_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ResponseParameterAnnotation)


def test_softgallerylanguage::responseparameterannotation_constructor_exists():
    assert callable(softGalleryLanguage::ResponseParameterAnnotation.__init__)


def test_softgallerylanguage::responseparameterannotation_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ResponseParameterAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::responseparameterannotation_has_name():
    assert hasattr(softGalleryLanguage::ResponseParameterAnnotation, "name")
    descriptor = None
    for klass in softGalleryLanguage::ResponseParameterAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::appaccess_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AppAccess)


def test_softgallerylanguage::appaccess_constructor_exists():
    assert callable(softGalleryLanguage::AppAccess.__init__)


def test_softgallerylanguage::appaccess_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AppAccess.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::profilemanagement_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ProfileManagement)


def test_softgallerylanguage::profilemanagement_constructor_exists():
    assert callable(softGalleryLanguage::ProfileManagement.__init__)


def test_softgallerylanguage::profilemanagement_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ProfileManagement.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::functionalities_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Functionalities)


def test_softgallerylanguage::functionalities_constructor_exists():
    assert callable(softGalleryLanguage::Functionalities.__init__)


def test_softgallerylanguage::functionalities_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Functionalities.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::atributeuserdomain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AtributeUserDomain)


def test_softgallerylanguage::atributeuserdomain_constructor_exists():
    assert callable(softGalleryLanguage::AtributeUserDomain.__init__)


def test_softgallerylanguage::atributeuserdomain_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AtributeUserDomain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::atributeuserdomain_has_name():
    assert hasattr(softGalleryLanguage::AtributeUserDomain, "name")
    descriptor = None
    for klass in softGalleryLanguage::AtributeUserDomain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::atributealbum_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AtributeAlbum)


def test_softgallerylanguage::atributealbum_constructor_exists():
    assert callable(softGalleryLanguage::AtributeAlbum.__init__)


def test_softgallerylanguage::atributealbum_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AtributeAlbum.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::atributealbum_has_name():
    assert hasattr(softGalleryLanguage::AtributeAlbum, "name")
    descriptor = None
    for klass in softGalleryLanguage::AtributeAlbum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::atributephoto_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::AtributePhoto)


def test_softgallerylanguage::atributephoto_constructor_exists():
    assert callable(softGalleryLanguage::AtributePhoto.__init__)


def test_softgallerylanguage::atributephoto_constructor_args():
    sig = inspect.signature(softGalleryLanguage::AtributePhoto.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::atributephoto_has_name():
    assert hasattr(softGalleryLanguage::AtributePhoto, "name")
    descriptor = None
    for klass in softGalleryLanguage::AtributePhoto.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::entities_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Entities)


def test_softgallerylanguage::entities_constructor_exists():
    assert callable(softGalleryLanguage::Entities.__init__)


def test_softgallerylanguage::entities_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Entities.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::entities_has_name():
    assert hasattr(softGalleryLanguage::Entities, "name")
    descriptor = None
    for klass in softGalleryLanguage::Entities.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::exceptionsdomain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::ExceptionsDomain)


def test_softgallerylanguage::exceptionsdomain_constructor_exists():
    assert callable(softGalleryLanguage::ExceptionsDomain.__init__)


def test_softgallerylanguage::exceptionsdomain_constructor_args():
    sig = inspect.signature(softGalleryLanguage::ExceptionsDomain.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::functionality_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Functionality)


def test_softgallerylanguage::functionality_constructor_exists():
    assert callable(softGalleryLanguage::Functionality.__init__)


def test_softgallerylanguage::functionality_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Functionality.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::entity_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Entity)


def test_softgallerylanguage::entity_constructor_exists():
    assert callable(softGalleryLanguage::Entity.__init__)


def test_softgallerylanguage::entity_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Entity.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::domain_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Domain)


def test_softgallerylanguage::domain_constructor_exists():
    assert callable(softGalleryLanguage::Domain.__init__)


def test_softgallerylanguage::domain_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_softgallerylanguage::domain_has_name():
    assert hasattr(softGalleryLanguage::Domain, "name")
    descriptor = None
    for klass in softGalleryLanguage::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_softgallerylanguage::eobject_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::EObject)


def test_softgallerylanguage::eobject_constructor_exists():
    assert callable(softGalleryLanguage::EObject.__init__)


def test_softgallerylanguage::eobject_constructor_args():
    sig = inspect.signature(softGalleryLanguage::EObject.__init__)
    params = list(sig.parameters.keys())



def test_softgallerylanguage::model_is_not_abstract():
    assert not inspect.isabstract(softGalleryLanguage::Model)


def test_softgallerylanguage::model_constructor_exists():
    assert callable(softGalleryLanguage::Model.__init__)


def test_softgallerylanguage::model_constructor_args():
    sig = inspect.signature(softGalleryLanguage::Model.__init__)
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
softGalleryLanguage::RequestMappingProduces_strategy = st.builds(
    softGalleryLanguage::RequestMappingProduces,
    name=
        safe_text
)
softGalleryLanguage::RequestMappingMethod_strategy = st.builds(
    softGalleryLanguage::RequestMappingMethod,
    name=
        safe_text
)
softGalleryLanguage::RequestMappingValue_strategy = st.builds(
    softGalleryLanguage::RequestMappingValue,
    name=
        safe_text
)
MappingType_strategy = st.builds(
    MappingType,
)
softGalleryLanguage::GetMapping_strategy = st.builds(
    softGalleryLanguage::GetMapping,
    name=
        safe_text
)
softGalleryLanguage::PutMapping_strategy = st.builds(
    softGalleryLanguage::PutMapping,
    name=
        safe_text
)
softGalleryLanguage::DeleteMapping_strategy = st.builds(
    softGalleryLanguage::DeleteMapping,
    name=
        safe_text
)
softGalleryLanguage::PostMapping_strategy = st.builds(
    softGalleryLanguage::PostMapping,
    name=
        safe_text
)
softGalleryLanguage::RequestMapping_strategy = st.builds(
    softGalleryLanguage::RequestMapping,
)
softGalleryLanguage::SpringEntity_strategy = st.builds(
    softGalleryLanguage::SpringEntity,
)
softGalleryLanguage::ResponseParameter_strategy = st.builds(
    softGalleryLanguage::ResponseParameter,
)
softGalleryLanguage::MappingType_strategy = st.builds(
    softGalleryLanguage::MappingType,
)
softGalleryLanguage::ResponseEntity_strategy = st.builds(
    softGalleryLanguage::ResponseEntity,
    name=
        safe_text
)
softGalleryLanguage::Autowired_strategy = st.builds(
    softGalleryLanguage::Autowired,
    name=
        safe_text
)
softGalleryLanguage::SearchCriteria_strategy = st.builds(
    softGalleryLanguage::SearchCriteria,
    name=
        safe_text
)
softGalleryLanguage::Predicate_strategy = st.builds(
    softGalleryLanguage::Predicate,
    name=
        safe_text
)
softGalleryLanguage::Specification_strategy = st.builds(
    softGalleryLanguage::Specification,
)
softGalleryLanguage::RestController_strategy = st.builds(
    softGalleryLanguage::RestController,
    name=
        safe_text
)
softGalleryLanguage::SpringRepositoryAnnotation_strategy = st.builds(
    softGalleryLanguage::SpringRepositoryAnnotation,
    name=
        safe_text
)
softGalleryLanguage::SpringRepositories_strategy = st.builds(
    softGalleryLanguage::SpringRepositories,
    name=
        safe_text
)
softGalleryLanguage::SpringRepository_strategy = st.builds(
    softGalleryLanguage::SpringRepository,
)
softGalleryLanguage::OrderSpring_strategy = st.builds(
    softGalleryLanguage::OrderSpring,
    name=
        safe_text
)
softGalleryLanguage::SpringComponent_strategy = st.builds(
    softGalleryLanguage::SpringComponent,
)
softGalleryLanguage::EnableWebSecurity_strategy = st.builds(
    softGalleryLanguage::EnableWebSecurity,
    name=
        safe_text
)
softGalleryLanguage::EnableResourceServer_strategy = st.builds(
    softGalleryLanguage::EnableResourceServer,
    name=
        safe_text
)
softGalleryLanguage::EnableAuthorizationServer_strategy = st.builds(
    softGalleryLanguage::EnableAuthorizationServer,
    name=
        safe_text
)
softGalleryLanguage::EnableGlobalMethodSecurity_strategy = st.builds(
    softGalleryLanguage::EnableGlobalMethodSecurity,
    name=
        safe_text
)
softGalleryLanguage::Configuration_strategy = st.builds(
    softGalleryLanguage::Configuration,
)
softGalleryLanguage::SpringBootApplication_strategy = st.builds(
    softGalleryLanguage::SpringBootApplication,
)
softGalleryLanguage::AmazonWebServices_strategy = st.builds(
    softGalleryLanguage::AmazonWebServices,
    name=
        safe_text
)
softGalleryLanguage::PostgreSQL_strategy = st.builds(
    softGalleryLanguage::PostgreSQL,
    name=
        safe_text
)
softGalleryLanguage::React_strategy = st.builds(
    softGalleryLanguage::React,
    name=
        safe_text
)
softGalleryLanguage::Spring_strategy = st.builds(
    softGalleryLanguage::Spring,
    name=
        safe_text
)
softGalleryLanguage::Technologies_strategy = st.builds(
    softGalleryLanguage::Technologies,
)
softGalleryLanguage::NTiersRelations_strategy = st.builds(
    softGalleryLanguage::NTiersRelations,
    name=
        safe_text
)
softGalleryLanguage::NTierTarget_strategy = st.builds(
    softGalleryLanguage::NTierTarget,
)
softGalleryLanguage::NTierSource_strategy = st.builds(
    softGalleryLanguage::NTierSource,
)
softGalleryLanguage::NTierConnectionContent_strategy = st.builds(
    softGalleryLanguage::NTierConnectionContent,
    nTierName=
        safe_text,
    ntierconnection=
        safe_text
)
softGalleryLanguage::NTiersConnections_strategy = st.builds(
    softGalleryLanguage::NTiersConnections,
)
softGalleryLanguage::PersistenceDataComponent_strategy = st.builds(
    softGalleryLanguage::PersistenceDataComponent,
    name=
        safe_text
)
softGalleryLanguage::BackEnd_strategy = st.builds(
    softGalleryLanguage::BackEnd,
    name=
        safe_text
)
softGalleryLanguage::FrontEnd_strategy = st.builds(
    softGalleryLanguage::FrontEnd,
    name=
        safe_text
)
softGalleryLanguage::ArchitectureComponents_strategy = st.builds(
    softGalleryLanguage::ArchitectureComponents,
)
softGalleryLanguage::LayerTarget_strategy = st.builds(
    softGalleryLanguage::LayerTarget,
    layerelations=
        safe_text
)
softGalleryLanguage::LayerSource_strategy = st.builds(
    softGalleryLanguage::LayerSource,
    layerelations=
        safe_text
)
softGalleryLanguage::Technology_strategy = st.builds(
    softGalleryLanguage::Technology,
    name=
        safe_text
)
softGalleryLanguage::SingleFile_strategy = st.builds(
    softGalleryLanguage::SingleFile,
    name=
        safe_text
)
softGalleryLanguage::MultipleFile_strategy = st.builds(
    softGalleryLanguage::MultipleFile,
    name=
        safe_text
)
softGalleryLanguage::Directories_strategy = st.builds(
    softGalleryLanguage::Directories,
)
softGalleryLanguage::DirectoryContent_strategy = st.builds(
    softGalleryLanguage::DirectoryContent,
    name=
        safe_text
)
softGalleryLanguage::SegmentStructureContent_strategy = st.builds(
    softGalleryLanguage::SegmentStructureContent,
    name=
        safe_text
)
softGalleryLanguage::SegmentStructure_strategy = st.builds(
    softGalleryLanguage::SegmentStructure,
)
softGalleryLanguage::DataPersistenceSegments_strategy = st.builds(
    softGalleryLanguage::DataPersistenceSegments,
    amazonSName=
        safe_text,
    postSName=
        safe_text
)
softGalleryLanguage::DataPersistenceContent_strategy = st.builds(
    softGalleryLanguage::DataPersistenceContent,
)
softGalleryLanguage::DataPersistenceLayer_strategy = st.builds(
    softGalleryLanguage::DataPersistenceLayer,
)
softGalleryLanguage::CriteriaAttributeType_strategy = st.builds(
    softGalleryLanguage::CriteriaAttributeType,
    name=
        safe_text
)
softGalleryLanguage::SpecificationSegmentElement_strategy = st.builds(
    softGalleryLanguage::SpecificationSegmentElement,
    name=
        safe_text
)
softGalleryLanguage::ControllerSegmentElement_strategy = st.builds(
    softGalleryLanguage::ControllerSegmentElement,
    name=
        safe_text
)
softGalleryLanguage::LayerRelations_strategy = st.builds(
    softGalleryLanguage::LayerRelations,
    layerelations=
        safe_text,
    name=
        safe_text
)
softGalleryLanguage::BusinessLogicSegments_strategy = st.builds(
    softGalleryLanguage::BusinessLogicSegments,
    name=
        safe_text
)
softGalleryLanguage::BusinessLogicContent_strategy = st.builds(
    softGalleryLanguage::BusinessLogicContent,
)
softGalleryLanguage::BusinessLogicLayer_strategy = st.builds(
    softGalleryLanguage::BusinessLogicLayer,
)
softGalleryLanguage::PresentationSegments_strategy = st.builds(
    softGalleryLanguage::PresentationSegments,
    presentationSName=
        safe_text,
    presentationAName=
        safe_text,
    presentationCName=
        safe_text
)
softGalleryLanguage::PresentationContent_strategy = st.builds(
    softGalleryLanguage::PresentationContent,
)
softGalleryLanguage::PresentationLayer_strategy = st.builds(
    softGalleryLanguage::PresentationLayer,
)
softGalleryLanguage::Layer_strategy = st.builds(
    softGalleryLanguage::Layer,
)
softGalleryLanguage::NTiers_strategy = st.builds(
    softGalleryLanguage::NTiers,
)
softGalleryLanguage::Architecture_strategy = st.builds(
    softGalleryLanguage::Architecture,
)
softGalleryLanguage::UserException_strategy = st.builds(
    softGalleryLanguage::UserException,
    name=
        safe_text
)
softGalleryLanguage::AlbumException_strategy = st.builds(
    softGalleryLanguage::AlbumException,
    name=
        safe_text
)
softGalleryLanguage::PhotoException_strategy = st.builds(
    softGalleryLanguage::PhotoException,
    name=
        safe_text
)
softGalleryLanguage::LandingFunctions_strategy = st.builds(
    softGalleryLanguage::LandingFunctions,
    nameCarouselName=
        safe_text,
    passPhotoName=
        safe_text
)
softGalleryLanguage::PhotoActionsFunctions_strategy = st.builds(
    softGalleryLanguage::PhotoActionsFunctions,
    nameLoad=
        safe_text,
    namePhoto=
        safe_text,
    nameGenerico=
        safe_text
)
softGalleryLanguage::AlbumManagementFunctions_strategy = st.builds(
    softGalleryLanguage::AlbumManagementFunctions,
    createdAlbName=
        safe_text,
    selectAlbName=
        safe_text
)
softGalleryLanguage::ExceptionsType_strategy = st.builds(
    softGalleryLanguage::ExceptionsType,
)
softGalleryLanguage::AppAccessFunctions_strategy = st.builds(
    softGalleryLanguage::AppAccessFunctions,
    registerName=
        safe_text,
    loginName=
        safe_text
)
softGalleryLanguage::ProfileManagementFunctions_strategy = st.builds(
    softGalleryLanguage::ProfileManagementFunctions,
    viewprofileName=
        safe_text,
    editProfileName=
        safe_text
)
softGalleryLanguage::LandingActions_strategy = st.builds(
    softGalleryLanguage::LandingActions,
)
softGalleryLanguage::PhotoActions_strategy = st.builds(
    softGalleryLanguage::PhotoActions,
)
softGalleryLanguage::AlbumManagement_strategy = st.builds(
    softGalleryLanguage::AlbumManagement,
)
softGalleryLanguage::AmazonElasticComputeCloud_strategy = st.builds(
    softGalleryLanguage::AmazonElasticComputeCloud,
    name=
        safe_text
)
softGalleryLanguage::Metadata_strategy = st.builds(
    softGalleryLanguage::Metadata,
    name=
        safe_text
)
softGalleryLanguage::AmazonFile_strategy = st.builds(
    softGalleryLanguage::AmazonFile,
)
softGalleryLanguage::AmazonFolder_strategy = st.builds(
    softGalleryLanguage::AmazonFolder,
    name=
        safe_text
)
softGalleryLanguage::OnlyAuthorized_strategy = st.builds(
    softGalleryLanguage::OnlyAuthorized,
    name=
        safe_text
)
softGalleryLanguage::BucketObjectsNotPublic_strategy = st.builds(
    softGalleryLanguage::BucketObjectsNotPublic,
    name=
        safe_text
)
softGalleryLanguage::ObjectsPublic_strategy = st.builds(
    softGalleryLanguage::ObjectsPublic,
    name=
        safe_text
)
softGalleryLanguage::BucketAccess_strategy = st.builds(
    softGalleryLanguage::BucketAccess,
)
softGalleryLanguage::Bucket_strategy = st.builds(
    softGalleryLanguage::Bucket,
    name=
        safe_text
)
softGalleryLanguage::BatchOperation_strategy = st.builds(
    softGalleryLanguage::BatchOperation,
    name=
        safe_text
)
softGalleryLanguage::AmazonSimpleStorageService_strategy = st.builds(
    softGalleryLanguage::AmazonSimpleStorageService,
)
softGalleryLanguage::Clause_strategy = st.builds(
    softGalleryLanguage::Clause,
    name=
        safe_text
)
softGalleryLanguage::Query_strategy = st.builds(
    softGalleryLanguage::Query,
)
softGalleryLanguage::Privilege_strategy = st.builds(
    softGalleryLanguage::Privilege,
    name=
        safe_text
)
softGalleryLanguage::PostgresUser_strategy = st.builds(
    softGalleryLanguage::PostgresUser,
    name=
        safe_text
)
softGalleryLanguage::Function_strategy = st.builds(
    softGalleryLanguage::Function,
    name=
        safe_text
)
softGalleryLanguage::Trigger_strategy = st.builds(
    softGalleryLanguage::Trigger,
    name=
        safe_text
)
softGalleryLanguage::Policy_strategy = st.builds(
    softGalleryLanguage::Policy,
    name=
        safe_text
)
softGalleryLanguage::PublicAccess_strategy = st.builds(
    softGalleryLanguage::PublicAccess,
    name=
        safe_text
)
softGalleryLanguage::Constraint_strategy = st.builds(
    softGalleryLanguage::Constraint,
    name=
        safe_text
)
softGalleryLanguage::DatatypeDB_strategy = st.builds(
    softGalleryLanguage::DatatypeDB,
    name=
        safe_text
)
softGalleryLanguage::ColumnP_strategy = st.builds(
    softGalleryLanguage::ColumnP,
    name=
        safe_text
)
softGalleryLanguage::RefTable::p_strategy = st.builds(
    softGalleryLanguage::RefTable::p,
    name=
        safe_text
)
softGalleryLanguage::ForeignKeyRef_strategy = st.builds(
    softGalleryLanguage::ForeignKeyRef,
)
softGalleryLanguage::ForeignKey::n_strategy = st.builds(
    softGalleryLanguage::ForeignKey::n,
    name=
        safe_text
)
softGalleryLanguage::ForeignKey_strategy = st.builds(
    softGalleryLanguage::ForeignKey,
)
softGalleryLanguage::Table::p_strategy = st.builds(
    softGalleryLanguage::Table::p,
    name=
        safe_text
)
softGalleryLanguage::ViewSchema_strategy = st.builds(
    softGalleryLanguage::ViewSchema,
    name=
        safe_text
)
softGalleryLanguage::Index::p_strategy = st.builds(
    softGalleryLanguage::Index::p,
    name=
        safe_text
)
softGalleryLanguage::Schema_strategy = st.builds(
    softGalleryLanguage::Schema,
)
softGalleryLanguage::Database_strategy = st.builds(
    softGalleryLanguage::Database,
    name=
        safe_text
)
softGalleryLanguage::Cluster_strategy = st.builds(
    softGalleryLanguage::Cluster,
)
softGalleryLanguage::Row_strategy = st.builds(
    softGalleryLanguage::Row,
    name=
        safe_text
)
softGalleryLanguage::ReactInformation_strategy = st.builds(
    softGalleryLanguage::ReactInformation,
    name=
        safe_text
)
softGalleryLanguage::ReactLibrary_strategy = st.builds(
    softGalleryLanguage::ReactLibrary,
    name=
        safe_text
)
softGalleryLanguage::ReactsRelationServ_strategy = st.builds(
    softGalleryLanguage::ReactsRelationServ,
    name=
        safe_text
)
softGalleryLanguage::ReactServiceRequestProps_strategy = st.builds(
    softGalleryLanguage::ReactServiceRequestProps,
    reqPropName=
        safe_text,
    reqPropDescription=
        safe_text
)
softGalleryLanguage::ReactServiceContRequest_strategy = st.builds(
    softGalleryLanguage::ReactServiceContRequest,
)
softGalleryLanguage::ReactServiceContent_strategy = st.builds(
    softGalleryLanguage::ReactServiceContent,
    functName=
        safe_text
)
softGalleryLanguage::ReactServicesType_strategy = st.builds(
    softGalleryLanguage::ReactServicesType,
    name=
        safe_text
)
softGalleryLanguage::ReactServicesRelation_strategy = st.builds(
    softGalleryLanguage::ReactServicesRelation,
)
softGalleryLanguage::ReactActionsContent_strategy = st.builds(
    softGalleryLanguage::ReactActionsContent,
)
softGalleryLanguage::StylePropertiesContent_strategy = st.builds(
    softGalleryLanguage::StylePropertiesContent,
    propName=
        safe_text
)
softGalleryLanguage::ComponentsStylesContent_strategy = st.builds(
    softGalleryLanguage::ComponentsStylesContent,
    nameStyle=
        safe_text
)
softGalleryLanguage::PropsType_strategy = st.builds(
    softGalleryLanguage::PropsType,
    propsdatas=
        safe_text,
    nameProps=
        safe_text
)
softGalleryLanguage::StateContent_strategy = st.builds(
    softGalleryLanguage::StateContent,
    stateName=
        safe_text,
    componentdatatyp=
        safe_text
)
softGalleryLanguage::CoreFunctionsDeclaration_strategy = st.builds(
    softGalleryLanguage::CoreFunctionsDeclaration,
    name=
        safe_text
)
softGalleryLanguage::State_strategy = st.builds(
    softGalleryLanguage::State,
)
softGalleryLanguage::ReactCoreFunctions_strategy = st.builds(
    softGalleryLanguage::ReactCoreFunctions,
    name=
        safe_text
)
softGalleryLanguage::ReactConstructor_strategy = st.builds(
    softGalleryLanguage::ReactConstructor,
)
softGalleryLanguage::ReactImportContent_strategy = st.builds(
    softGalleryLanguage::ReactImportContent,
    impName=
        safe_text
)
softGalleryLanguage::StyleProperties_strategy = st.builds(
    softGalleryLanguage::StyleProperties,
)
softGalleryLanguage::Props_strategy = st.builds(
    softGalleryLanguage::Props,
)
softGalleryLanguage::ReactFunctions_strategy = st.builds(
    softGalleryLanguage::ReactFunctions,
    lifecycleclass=
        safe_text,
    renderclass=
        safe_text
)
softGalleryLanguage::ReactImports_strategy = st.builds(
    softGalleryLanguage::ReactImports,
)
softGalleryLanguage::SubcomponentCont_strategy = st.builds(
    softGalleryLanguage::SubcomponentCont,
    nameSubComp=
        safe_text
)
softGalleryLanguage::ViewComponentCont_strategy = st.builds(
    softGalleryLanguage::ViewComponentCont,
    nameView=
        safe_text
)
softGalleryLanguage::UIContent_strategy = st.builds(
    softGalleryLanguage::UIContent,
)
softGalleryLanguage::ComponentClass_strategy = st.builds(
    softGalleryLanguage::ComponentClass,
)
softGalleryLanguage::LogicStructure_strategy = st.builds(
    softGalleryLanguage::LogicStructure,
    indexCompName=
        safe_text,
    appComName=
        safe_text
)
softGalleryLanguage::LogicContent_strategy = st.builds(
    softGalleryLanguage::LogicContent,
    name=
        safe_text
)
softGalleryLanguage::ComponentsStyles_strategy = st.builds(
    softGalleryLanguage::ComponentsStyles,
)
softGalleryLanguage::ComponentsLogic_strategy = st.builds(
    softGalleryLanguage::ComponentsLogic,
    name=
        safe_text
)
softGalleryLanguage::DOMConfigurations_strategy = st.builds(
    softGalleryLanguage::DOMConfigurations,
    elements=
        safe_text,
    name=
        safe_text
)
softGalleryLanguage::PackageVersion_strategy = st.builds(
    softGalleryLanguage::PackageVersion,
    name=
        safe_text
)
softGalleryLanguage::PackageName_strategy = st.builds(
    softGalleryLanguage::PackageName,
    name=
        safe_text
)
softGalleryLanguage::SingleDependencies_strategy = st.builds(
    softGalleryLanguage::SingleDependencies,
)
softGalleryLanguage::ReactDependenciesSubRules_strategy = st.builds(
    softGalleryLanguage::ReactDependenciesSubRules,
)
softGalleryLanguage::ReactDependenciesRules_strategy = st.builds(
    softGalleryLanguage::ReactDependenciesRules,
    name=
        safe_text
)
softGalleryLanguage::ReactConfigurations_strategy = st.builds(
    softGalleryLanguage::ReactConfigurations,
    name=
        safe_text
)
softGalleryLanguage::ReactDependencies_strategy = st.builds(
    softGalleryLanguage::ReactDependencies,
)
softGalleryLanguage::ReactInfo_strategy = st.builds(
    softGalleryLanguage::ReactInfo,
)
softGalleryLanguage::ReactLibraries_strategy = st.builds(
    softGalleryLanguage::ReactLibraries,
)
softGalleryLanguage::ReactActions_strategy = st.builds(
    softGalleryLanguage::ReactActions,
)
softGalleryLanguage::ComponentsUI_strategy = st.builds(
    softGalleryLanguage::ComponentsUI,
    name=
        safe_text
)
softGalleryLanguage::ReactConfiguration_strategy = st.builds(
    softGalleryLanguage::ReactConfiguration,
)
softGalleryLanguage::ReactSubModules_strategy = st.builds(
    softGalleryLanguage::ReactSubModules,
)
softGalleryLanguage::ReactModules_strategy = st.builds(
    softGalleryLanguage::ReactModules,
)
softGalleryLanguage::StorageActionMemberName_strategy = st.builds(
    softGalleryLanguage::StorageActionMemberName,
    name=
        safe_text
)
softGalleryLanguage::StorageActionMemberType_strategy = st.builds(
    softGalleryLanguage::StorageActionMemberType,
    name=
        safe_text
)
softGalleryLanguage::StorageActionMember_strategy = st.builds(
    softGalleryLanguage::StorageActionMember,
)
softGalleryLanguage::StorageActionReturn_strategy = st.builds(
    softGalleryLanguage::StorageActionReturn,
    name=
        safe_text
)
softGalleryLanguage::StorageActionAnnotation_strategy = st.builds(
    softGalleryLanguage::StorageActionAnnotation,
    name=
        safe_text
)
softGalleryLanguage::StorageAction_strategy = st.builds(
    softGalleryLanguage::StorageAction,
    name=
        safe_text
)
softGalleryLanguage::StorageMemberAnnotation_strategy = st.builds(
    softGalleryLanguage::StorageMemberAnnotation,
    name=
        safe_text
)
softGalleryLanguage::StorageMemberType_strategy = st.builds(
    softGalleryLanguage::StorageMemberType,
    name=
        safe_text
)
softGalleryLanguage::StorageMember_strategy = st.builds(
    softGalleryLanguage::StorageMember,
    name=
        safe_text
)
softGalleryLanguage::StorageClient_strategy = st.builds(
    softGalleryLanguage::StorageClient,
    name=
        safe_text
)
softGalleryLanguage::SpringEntityAnnotationTypes_strategy = st.builds(
    softGalleryLanguage::SpringEntityAnnotationTypes,
    name=
        safe_text
)
softGalleryLanguage::ReactComponents_strategy = st.builds(
    softGalleryLanguage::ReactComponents,
)
softGalleryLanguage::ExceptionProcess_strategy = st.builds(
    softGalleryLanguage::ExceptionProcess,
    name=
        safe_text
)
softGalleryLanguage::ExceptionHandler_strategy = st.builds(
    softGalleryLanguage::ExceptionHandler,
    name=
        safe_text
)
softGalleryLanguage::ResponseParameterName_strategy = st.builds(
    softGalleryLanguage::ResponseParameterName,
    name=
        safe_text
)
softGalleryLanguage::ResponseParameterType_strategy = st.builds(
    softGalleryLanguage::ResponseParameterType,
    name=
        safe_text
)
softGalleryLanguage::ResponseParameterAnnotation_strategy = st.builds(
    softGalleryLanguage::ResponseParameterAnnotation,
    name=
        safe_text
)
softGalleryLanguage::AppAccess_strategy = st.builds(
    softGalleryLanguage::AppAccess,
)
softGalleryLanguage::ProfileManagement_strategy = st.builds(
    softGalleryLanguage::ProfileManagement,
)
softGalleryLanguage::Functionalities_strategy = st.builds(
    softGalleryLanguage::Functionalities,
)
softGalleryLanguage::AtributeUserDomain_strategy = st.builds(
    softGalleryLanguage::AtributeUserDomain,
    name=
        safe_text
)
softGalleryLanguage::AtributeAlbum_strategy = st.builds(
    softGalleryLanguage::AtributeAlbum,
    name=
        safe_text
)
softGalleryLanguage::AtributePhoto_strategy = st.builds(
    softGalleryLanguage::AtributePhoto,
    name=
        safe_text
)
softGalleryLanguage::Entities_strategy = st.builds(
    softGalleryLanguage::Entities,
    name=
        safe_text
)
softGalleryLanguage::ExceptionsDomain_strategy = st.builds(
    softGalleryLanguage::ExceptionsDomain,
)
softGalleryLanguage::Functionality_strategy = st.builds(
    softGalleryLanguage::Functionality,
)
softGalleryLanguage::Entity_strategy = st.builds(
    softGalleryLanguage::Entity,
)
softGalleryLanguage::Domain_strategy = st.builds(
    softGalleryLanguage::Domain,
    name=
        safe_text
)
softGalleryLanguage::EObject_strategy = st.builds(
    softGalleryLanguage::EObject,
)
softGalleryLanguage::Model_strategy = st.builds(
    softGalleryLanguage::Model,
)

@given(instance=softGalleryLanguage::RequestMappingProduces_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::requestmappingproduces_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RequestMappingProduces)

@given(instance=softGalleryLanguage::RequestMappingProduces_strategy)
def test_softgallerylanguage::requestmappingproduces_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::RequestMappingProduces_strategy)
def test_softgallerylanguage::requestmappingproduces_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::RequestMappingMethod_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::requestmappingmethod_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RequestMappingMethod)

@given(instance=softGalleryLanguage::RequestMappingMethod_strategy)
def test_softgallerylanguage::requestmappingmethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::RequestMappingMethod_strategy)
def test_softgallerylanguage::requestmappingmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::RequestMappingValue_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::requestmappingvalue_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RequestMappingValue)

@given(instance=softGalleryLanguage::RequestMappingValue_strategy)
def test_softgallerylanguage::requestmappingvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::RequestMappingValue_strategy)
def test_softgallerylanguage::requestmappingvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MappingType_strategy)
@settings(max_examples=50)
def test_mappingtype_instantiation(instance):
    assert isinstance(instance, MappingType)

@given(instance=softGalleryLanguage::GetMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::getmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::GetMapping)

@given(instance=softGalleryLanguage::GetMapping_strategy)
def test_softgallerylanguage::getmapping_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::GetMapping_strategy)
def test_softgallerylanguage::getmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PutMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::putmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PutMapping)

@given(instance=softGalleryLanguage::PutMapping_strategy)
def test_softgallerylanguage::putmapping_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PutMapping_strategy)
def test_softgallerylanguage::putmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::DeleteMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::deletemapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DeleteMapping)

@given(instance=softGalleryLanguage::DeleteMapping_strategy)
def test_softgallerylanguage::deletemapping_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::DeleteMapping_strategy)
def test_softgallerylanguage::deletemapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PostMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::postmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PostMapping)

@given(instance=softGalleryLanguage::PostMapping_strategy)
def test_softgallerylanguage::postmapping_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PostMapping_strategy)
def test_softgallerylanguage::postmapping_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::RequestMapping_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::requestmapping_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RequestMapping)

@given(instance=softGalleryLanguage::SpringEntity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springentity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringEntity)

@given(instance=softGalleryLanguage::ResponseParameter_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::responseparameter_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ResponseParameter)

@given(instance=softGalleryLanguage::MappingType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::mappingtype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::MappingType)

@given(instance=softGalleryLanguage::ResponseEntity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::responseentity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ResponseEntity)

@given(instance=softGalleryLanguage::ResponseEntity_strategy)
def test_softgallerylanguage::responseentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ResponseEntity_strategy)
def test_softgallerylanguage::responseentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Autowired_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::autowired_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Autowired)

@given(instance=softGalleryLanguage::Autowired_strategy)
def test_softgallerylanguage::autowired_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Autowired_strategy)
def test_softgallerylanguage::autowired_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SearchCriteria_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::searchcriteria_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SearchCriteria)

@given(instance=softGalleryLanguage::SearchCriteria_strategy)
def test_softgallerylanguage::searchcriteria_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SearchCriteria_strategy)
def test_softgallerylanguage::searchcriteria_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Predicate_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::predicate_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Predicate)

@given(instance=softGalleryLanguage::Predicate_strategy)
def test_softgallerylanguage::predicate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Predicate_strategy)
def test_softgallerylanguage::predicate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Specification_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::specification_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Specification)

@given(instance=softGalleryLanguage::RestController_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::restcontroller_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RestController)

@given(instance=softGalleryLanguage::RestController_strategy)
def test_softgallerylanguage::restcontroller_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::RestController_strategy)
def test_softgallerylanguage::restcontroller_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpringRepositoryAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springrepositoryannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringRepositoryAnnotation)

@given(instance=softGalleryLanguage::SpringRepositoryAnnotation_strategy)
def test_softgallerylanguage::springrepositoryannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SpringRepositoryAnnotation_strategy)
def test_softgallerylanguage::springrepositoryannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpringRepositories_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springrepositories_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringRepositories)

@given(instance=softGalleryLanguage::SpringRepositories_strategy)
def test_softgallerylanguage::springrepositories_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SpringRepositories_strategy)
def test_softgallerylanguage::springrepositories_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpringRepository_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springrepository_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringRepository)

@given(instance=softGalleryLanguage::OrderSpring_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::orderspring_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::OrderSpring)

@given(instance=softGalleryLanguage::OrderSpring_strategy)
def test_softgallerylanguage::orderspring_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::OrderSpring_strategy)
def test_softgallerylanguage::orderspring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpringComponent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springcomponent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringComponent)

@given(instance=softGalleryLanguage::EnableWebSecurity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::enablewebsecurity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::EnableWebSecurity)

@given(instance=softGalleryLanguage::EnableWebSecurity_strategy)
def test_softgallerylanguage::enablewebsecurity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::EnableWebSecurity_strategy)
def test_softgallerylanguage::enablewebsecurity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::EnableResourceServer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::enableresourceserver_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::EnableResourceServer)

@given(instance=softGalleryLanguage::EnableResourceServer_strategy)
def test_softgallerylanguage::enableresourceserver_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::EnableResourceServer_strategy)
def test_softgallerylanguage::enableresourceserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::EnableAuthorizationServer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::enableauthorizationserver_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::EnableAuthorizationServer)

@given(instance=softGalleryLanguage::EnableAuthorizationServer_strategy)
def test_softgallerylanguage::enableauthorizationserver_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::EnableAuthorizationServer_strategy)
def test_softgallerylanguage::enableauthorizationserver_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::EnableGlobalMethodSecurity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::enableglobalmethodsecurity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::EnableGlobalMethodSecurity)

@given(instance=softGalleryLanguage::EnableGlobalMethodSecurity_strategy)
def test_softgallerylanguage::enableglobalmethodsecurity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::EnableGlobalMethodSecurity_strategy)
def test_softgallerylanguage::enableglobalmethodsecurity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Configuration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::configuration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Configuration)

@given(instance=softGalleryLanguage::SpringBootApplication_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springbootapplication_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringBootApplication)

@given(instance=softGalleryLanguage::AmazonWebServices_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::amazonwebservices_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AmazonWebServices)

@given(instance=softGalleryLanguage::AmazonWebServices_strategy)
def test_softgallerylanguage::amazonwebservices_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AmazonWebServices_strategy)
def test_softgallerylanguage::amazonwebservices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PostgreSQL_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::postgresql_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PostgreSQL)

@given(instance=softGalleryLanguage::PostgreSQL_strategy)
def test_softgallerylanguage::postgresql_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PostgreSQL_strategy)
def test_softgallerylanguage::postgresql_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::React_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::react_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::React)

@given(instance=softGalleryLanguage::React_strategy)
def test_softgallerylanguage::react_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::React_strategy)
def test_softgallerylanguage::react_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Spring_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::spring_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Spring)

@given(instance=softGalleryLanguage::Spring_strategy)
def test_softgallerylanguage::spring_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Spring_strategy)
def test_softgallerylanguage::spring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Technologies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::technologies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Technologies)

@given(instance=softGalleryLanguage::NTiersRelations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntiersrelations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTiersRelations)

@given(instance=softGalleryLanguage::NTiersRelations_strategy)
def test_softgallerylanguage::ntiersrelations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::NTiersRelations_strategy)
def test_softgallerylanguage::ntiersrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::NTierTarget_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntiertarget_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTierTarget)

@given(instance=softGalleryLanguage::NTierSource_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntiersource_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTierSource)

@given(instance=softGalleryLanguage::NTierConnectionContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntierconnectioncontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTierConnectionContent)

@given(instance=softGalleryLanguage::NTierConnectionContent_strategy)
def test_softgallerylanguage::ntierconnectioncontent_nTierName_type(instance):
    assert isinstance(instance.nTierName, str)


@given(instance=softGalleryLanguage::NTierConnectionContent_strategy)
def test_softgallerylanguage::ntierconnectioncontent_nTierName_setter(instance):
    original = instance.nTierName
    instance.nTierName = original
    assert instance.nTierName == original

@given(instance=softGalleryLanguage::NTierConnectionContent_strategy)
def test_softgallerylanguage::ntierconnectioncontent_ntierconnection_type(instance):
    assert isinstance(instance.ntierconnection, str)


@given(instance=softGalleryLanguage::NTierConnectionContent_strategy)
def test_softgallerylanguage::ntierconnectioncontent_ntierconnection_setter(instance):
    original = instance.ntierconnection
    instance.ntierconnection = original
    assert instance.ntierconnection == original

@given(instance=softGalleryLanguage::NTiersConnections_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntiersconnections_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTiersConnections)

@given(instance=softGalleryLanguage::PersistenceDataComponent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::persistencedatacomponent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PersistenceDataComponent)

@given(instance=softGalleryLanguage::PersistenceDataComponent_strategy)
def test_softgallerylanguage::persistencedatacomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PersistenceDataComponent_strategy)
def test_softgallerylanguage::persistencedatacomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BackEnd_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::backend_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BackEnd)

@given(instance=softGalleryLanguage::BackEnd_strategy)
def test_softgallerylanguage::backend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::BackEnd_strategy)
def test_softgallerylanguage::backend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::FrontEnd_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::frontend_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::FrontEnd)

@given(instance=softGalleryLanguage::FrontEnd_strategy)
def test_softgallerylanguage::frontend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::FrontEnd_strategy)
def test_softgallerylanguage::frontend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ArchitectureComponents_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::architecturecomponents_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ArchitectureComponents)

@given(instance=softGalleryLanguage::LayerTarget_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::layertarget_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LayerTarget)

@given(instance=softGalleryLanguage::LayerTarget_strategy)
def test_softgallerylanguage::layertarget_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=softGalleryLanguage::LayerTarget_strategy)
def test_softgallerylanguage::layertarget_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage::LayerSource_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::layersource_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LayerSource)

@given(instance=softGalleryLanguage::LayerSource_strategy)
def test_softgallerylanguage::layersource_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=softGalleryLanguage::LayerSource_strategy)
def test_softgallerylanguage::layersource_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage::Technology_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::technology_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Technology)

@given(instance=softGalleryLanguage::Technology_strategy)
def test_softgallerylanguage::technology_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Technology_strategy)
def test_softgallerylanguage::technology_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SingleFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::singlefile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SingleFile)

@given(instance=softGalleryLanguage::SingleFile_strategy)
def test_softgallerylanguage::singlefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SingleFile_strategy)
def test_softgallerylanguage::singlefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::MultipleFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::multiplefile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::MultipleFile)

@given(instance=softGalleryLanguage::MultipleFile_strategy)
def test_softgallerylanguage::multiplefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::MultipleFile_strategy)
def test_softgallerylanguage::multiplefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Directories_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::directories_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Directories)

@given(instance=softGalleryLanguage::DirectoryContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::directorycontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DirectoryContent)

@given(instance=softGalleryLanguage::DirectoryContent_strategy)
def test_softgallerylanguage::directorycontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::DirectoryContent_strategy)
def test_softgallerylanguage::directorycontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SegmentStructureContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::segmentstructurecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SegmentStructureContent)

@given(instance=softGalleryLanguage::SegmentStructureContent_strategy)
def test_softgallerylanguage::segmentstructurecontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SegmentStructureContent_strategy)
def test_softgallerylanguage::segmentstructurecontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SegmentStructure_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::segmentstructure_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SegmentStructure)

@given(instance=softGalleryLanguage::DataPersistenceSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::datapersistencesegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DataPersistenceSegments)

@given(instance=softGalleryLanguage::DataPersistenceSegments_strategy)
def test_softgallerylanguage::datapersistencesegments_amazonSName_type(instance):
    assert isinstance(instance.amazonSName, str)


@given(instance=softGalleryLanguage::DataPersistenceSegments_strategy)
def test_softgallerylanguage::datapersistencesegments_amazonSName_setter(instance):
    original = instance.amazonSName
    instance.amazonSName = original
    assert instance.amazonSName == original

@given(instance=softGalleryLanguage::DataPersistenceSegments_strategy)
def test_softgallerylanguage::datapersistencesegments_postSName_type(instance):
    assert isinstance(instance.postSName, str)


@given(instance=softGalleryLanguage::DataPersistenceSegments_strategy)
def test_softgallerylanguage::datapersistencesegments_postSName_setter(instance):
    original = instance.postSName
    instance.postSName = original
    assert instance.postSName == original

@given(instance=softGalleryLanguage::DataPersistenceContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::datapersistencecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DataPersistenceContent)

@given(instance=softGalleryLanguage::DataPersistenceLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::datapersistencelayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DataPersistenceLayer)

@given(instance=softGalleryLanguage::CriteriaAttributeType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::criteriaattributetype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::CriteriaAttributeType)

@given(instance=softGalleryLanguage::CriteriaAttributeType_strategy)
def test_softgallerylanguage::criteriaattributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::CriteriaAttributeType_strategy)
def test_softgallerylanguage::criteriaattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpecificationSegmentElement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::specificationsegmentelement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpecificationSegmentElement)

@given(instance=softGalleryLanguage::SpecificationSegmentElement_strategy)
def test_softgallerylanguage::specificationsegmentelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SpecificationSegmentElement_strategy)
def test_softgallerylanguage::specificationsegmentelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ControllerSegmentElement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::controllersegmentelement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ControllerSegmentElement)

@given(instance=softGalleryLanguage::ControllerSegmentElement_strategy)
def test_softgallerylanguage::controllersegmentelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ControllerSegmentElement_strategy)
def test_softgallerylanguage::controllersegmentelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::LayerRelations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::layerrelations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LayerRelations)

@given(instance=softGalleryLanguage::LayerRelations_strategy)
def test_softgallerylanguage::layerrelations_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=softGalleryLanguage::LayerRelations_strategy)
def test_softgallerylanguage::layerrelations_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=softGalleryLanguage::LayerRelations_strategy)
def test_softgallerylanguage::layerrelations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::LayerRelations_strategy)
def test_softgallerylanguage::layerrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BusinessLogicSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::businesslogicsegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BusinessLogicSegments)

@given(instance=softGalleryLanguage::BusinessLogicSegments_strategy)
def test_softgallerylanguage::businesslogicsegments_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::BusinessLogicSegments_strategy)
def test_softgallerylanguage::businesslogicsegments_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BusinessLogicContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::businesslogiccontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BusinessLogicContent)

@given(instance=softGalleryLanguage::BusinessLogicLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::businesslogiclayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BusinessLogicLayer)

@given(instance=softGalleryLanguage::PresentationSegments_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::presentationsegments_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PresentationSegments)

@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationSName_type(instance):
    assert isinstance(instance.presentationSName, str)


@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationSName_setter(instance):
    original = instance.presentationSName
    instance.presentationSName = original
    assert instance.presentationSName == original

@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationAName_type(instance):
    assert isinstance(instance.presentationAName, str)


@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationAName_setter(instance):
    original = instance.presentationAName
    instance.presentationAName = original
    assert instance.presentationAName == original

@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationCName_type(instance):
    assert isinstance(instance.presentationCName, str)


@given(instance=softGalleryLanguage::PresentationSegments_strategy)
def test_softgallerylanguage::presentationsegments_presentationCName_setter(instance):
    original = instance.presentationCName
    instance.presentationCName = original
    assert instance.presentationCName == original

@given(instance=softGalleryLanguage::PresentationContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::presentationcontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PresentationContent)

@given(instance=softGalleryLanguage::PresentationLayer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::presentationlayer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PresentationLayer)

@given(instance=softGalleryLanguage::Layer_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::layer_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Layer)

@given(instance=softGalleryLanguage::NTiers_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::ntiers_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::NTiers)

@given(instance=softGalleryLanguage::Architecture_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::architecture_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Architecture)

@given(instance=softGalleryLanguage::UserException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::userexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::UserException)

@given(instance=softGalleryLanguage::UserException_strategy)
def test_softgallerylanguage::userexception_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::UserException_strategy)
def test_softgallerylanguage::userexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AlbumException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::albumexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AlbumException)

@given(instance=softGalleryLanguage::AlbumException_strategy)
def test_softgallerylanguage::albumexception_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AlbumException_strategy)
def test_softgallerylanguage::albumexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PhotoException_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::photoexception_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PhotoException)

@given(instance=softGalleryLanguage::PhotoException_strategy)
def test_softgallerylanguage::photoexception_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PhotoException_strategy)
def test_softgallerylanguage::photoexception_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::LandingFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::landingfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LandingFunctions)

@given(instance=softGalleryLanguage::LandingFunctions_strategy)
def test_softgallerylanguage::landingfunctions_nameCarouselName_type(instance):
    assert isinstance(instance.nameCarouselName, str)


@given(instance=softGalleryLanguage::LandingFunctions_strategy)
def test_softgallerylanguage::landingfunctions_nameCarouselName_setter(instance):
    original = instance.nameCarouselName
    instance.nameCarouselName = original
    assert instance.nameCarouselName == original

@given(instance=softGalleryLanguage::LandingFunctions_strategy)
def test_softgallerylanguage::landingfunctions_passPhotoName_type(instance):
    assert isinstance(instance.passPhotoName, str)


@given(instance=softGalleryLanguage::LandingFunctions_strategy)
def test_softgallerylanguage::landingfunctions_passPhotoName_setter(instance):
    original = instance.passPhotoName
    instance.passPhotoName = original
    assert instance.passPhotoName == original

@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::photoactionsfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PhotoActionsFunctions)

@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_nameLoad_type(instance):
    assert isinstance(instance.nameLoad, str)


@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_nameLoad_setter(instance):
    original = instance.nameLoad
    instance.nameLoad = original
    assert instance.nameLoad == original

@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_namePhoto_type(instance):
    assert isinstance(instance.namePhoto, str)


@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_namePhoto_setter(instance):
    original = instance.namePhoto
    instance.namePhoto = original
    assert instance.namePhoto == original

@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_nameGenerico_type(instance):
    assert isinstance(instance.nameGenerico, str)


@given(instance=softGalleryLanguage::PhotoActionsFunctions_strategy)
def test_softgallerylanguage::photoactionsfunctions_nameGenerico_setter(instance):
    original = instance.nameGenerico
    instance.nameGenerico = original
    assert instance.nameGenerico == original

@given(instance=softGalleryLanguage::AlbumManagementFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::albummanagementfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AlbumManagementFunctions)

@given(instance=softGalleryLanguage::AlbumManagementFunctions_strategy)
def test_softgallerylanguage::albummanagementfunctions_createdAlbName_type(instance):
    assert isinstance(instance.createdAlbName, str)


@given(instance=softGalleryLanguage::AlbumManagementFunctions_strategy)
def test_softgallerylanguage::albummanagementfunctions_createdAlbName_setter(instance):
    original = instance.createdAlbName
    instance.createdAlbName = original
    assert instance.createdAlbName == original

@given(instance=softGalleryLanguage::AlbumManagementFunctions_strategy)
def test_softgallerylanguage::albummanagementfunctions_selectAlbName_type(instance):
    assert isinstance(instance.selectAlbName, str)


@given(instance=softGalleryLanguage::AlbumManagementFunctions_strategy)
def test_softgallerylanguage::albummanagementfunctions_selectAlbName_setter(instance):
    original = instance.selectAlbName
    instance.selectAlbName = original
    assert instance.selectAlbName == original

@given(instance=softGalleryLanguage::ExceptionsType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::exceptionstype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ExceptionsType)

@given(instance=softGalleryLanguage::AppAccessFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::appaccessfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AppAccessFunctions)

@given(instance=softGalleryLanguage::AppAccessFunctions_strategy)
def test_softgallerylanguage::appaccessfunctions_registerName_type(instance):
    assert isinstance(instance.registerName, str)


@given(instance=softGalleryLanguage::AppAccessFunctions_strategy)
def test_softgallerylanguage::appaccessfunctions_registerName_setter(instance):
    original = instance.registerName
    instance.registerName = original
    assert instance.registerName == original

@given(instance=softGalleryLanguage::AppAccessFunctions_strategy)
def test_softgallerylanguage::appaccessfunctions_loginName_type(instance):
    assert isinstance(instance.loginName, str)


@given(instance=softGalleryLanguage::AppAccessFunctions_strategy)
def test_softgallerylanguage::appaccessfunctions_loginName_setter(instance):
    original = instance.loginName
    instance.loginName = original
    assert instance.loginName == original

@given(instance=softGalleryLanguage::ProfileManagementFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::profilemanagementfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ProfileManagementFunctions)

@given(instance=softGalleryLanguage::ProfileManagementFunctions_strategy)
def test_softgallerylanguage::profilemanagementfunctions_viewprofileName_type(instance):
    assert isinstance(instance.viewprofileName, str)


@given(instance=softGalleryLanguage::ProfileManagementFunctions_strategy)
def test_softgallerylanguage::profilemanagementfunctions_viewprofileName_setter(instance):
    original = instance.viewprofileName
    instance.viewprofileName = original
    assert instance.viewprofileName == original

@given(instance=softGalleryLanguage::ProfileManagementFunctions_strategy)
def test_softgallerylanguage::profilemanagementfunctions_editProfileName_type(instance):
    assert isinstance(instance.editProfileName, str)


@given(instance=softGalleryLanguage::ProfileManagementFunctions_strategy)
def test_softgallerylanguage::profilemanagementfunctions_editProfileName_setter(instance):
    original = instance.editProfileName
    instance.editProfileName = original
    assert instance.editProfileName == original

@given(instance=softGalleryLanguage::LandingActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::landingactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LandingActions)

@given(instance=softGalleryLanguage::PhotoActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::photoactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PhotoActions)

@given(instance=softGalleryLanguage::AlbumManagement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::albummanagement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AlbumManagement)

@given(instance=softGalleryLanguage::AmazonElasticComputeCloud_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::amazonelasticcomputecloud_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AmazonElasticComputeCloud)

@given(instance=softGalleryLanguage::AmazonElasticComputeCloud_strategy)
def test_softgallerylanguage::amazonelasticcomputecloud_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AmazonElasticComputeCloud_strategy)
def test_softgallerylanguage::amazonelasticcomputecloud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Metadata_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::metadata_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Metadata)

@given(instance=softGalleryLanguage::Metadata_strategy)
def test_softgallerylanguage::metadata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Metadata_strategy)
def test_softgallerylanguage::metadata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AmazonFile_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::amazonfile_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AmazonFile)

@given(instance=softGalleryLanguage::AmazonFolder_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::amazonfolder_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AmazonFolder)

@given(instance=softGalleryLanguage::AmazonFolder_strategy)
def test_softgallerylanguage::amazonfolder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AmazonFolder_strategy)
def test_softgallerylanguage::amazonfolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::OnlyAuthorized_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::onlyauthorized_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::OnlyAuthorized)

@given(instance=softGalleryLanguage::OnlyAuthorized_strategy)
def test_softgallerylanguage::onlyauthorized_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::OnlyAuthorized_strategy)
def test_softgallerylanguage::onlyauthorized_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BucketObjectsNotPublic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::bucketobjectsnotpublic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BucketObjectsNotPublic)

@given(instance=softGalleryLanguage::BucketObjectsNotPublic_strategy)
def test_softgallerylanguage::bucketobjectsnotpublic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::BucketObjectsNotPublic_strategy)
def test_softgallerylanguage::bucketobjectsnotpublic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ObjectsPublic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::objectspublic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ObjectsPublic)

@given(instance=softGalleryLanguage::ObjectsPublic_strategy)
def test_softgallerylanguage::objectspublic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ObjectsPublic_strategy)
def test_softgallerylanguage::objectspublic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BucketAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::bucketaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BucketAccess)

@given(instance=softGalleryLanguage::Bucket_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::bucket_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Bucket)

@given(instance=softGalleryLanguage::Bucket_strategy)
def test_softgallerylanguage::bucket_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Bucket_strategy)
def test_softgallerylanguage::bucket_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::BatchOperation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::batchoperation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::BatchOperation)

@given(instance=softGalleryLanguage::BatchOperation_strategy)
def test_softgallerylanguage::batchoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::BatchOperation_strategy)
def test_softgallerylanguage::batchoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AmazonSimpleStorageService_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::amazonsimplestorageservice_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AmazonSimpleStorageService)

@given(instance=softGalleryLanguage::Clause_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::clause_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Clause)

@given(instance=softGalleryLanguage::Clause_strategy)
def test_softgallerylanguage::clause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Clause_strategy)
def test_softgallerylanguage::clause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Query_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::query_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Query)

@given(instance=softGalleryLanguage::Privilege_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::privilege_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Privilege)

@given(instance=softGalleryLanguage::Privilege_strategy)
def test_softgallerylanguage::privilege_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Privilege_strategy)
def test_softgallerylanguage::privilege_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PostgresUser_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::postgresuser_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PostgresUser)

@given(instance=softGalleryLanguage::PostgresUser_strategy)
def test_softgallerylanguage::postgresuser_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PostgresUser_strategy)
def test_softgallerylanguage::postgresuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Function_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::function_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Function)

@given(instance=softGalleryLanguage::Function_strategy)
def test_softgallerylanguage::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Function_strategy)
def test_softgallerylanguage::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Trigger_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::trigger_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Trigger)

@given(instance=softGalleryLanguage::Trigger_strategy)
def test_softgallerylanguage::trigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Trigger_strategy)
def test_softgallerylanguage::trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Policy_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::policy_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Policy)

@given(instance=softGalleryLanguage::Policy_strategy)
def test_softgallerylanguage::policy_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Policy_strategy)
def test_softgallerylanguage::policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PublicAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::publicaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PublicAccess)

@given(instance=softGalleryLanguage::PublicAccess_strategy)
def test_softgallerylanguage::publicaccess_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PublicAccess_strategy)
def test_softgallerylanguage::publicaccess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Constraint_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::constraint_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Constraint)

@given(instance=softGalleryLanguage::Constraint_strategy)
def test_softgallerylanguage::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Constraint_strategy)
def test_softgallerylanguage::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::DatatypeDB_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::datatypedb_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DatatypeDB)

@given(instance=softGalleryLanguage::DatatypeDB_strategy)
def test_softgallerylanguage::datatypedb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::DatatypeDB_strategy)
def test_softgallerylanguage::datatypedb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ColumnP_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::columnp_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ColumnP)

@given(instance=softGalleryLanguage::ColumnP_strategy)
def test_softgallerylanguage::columnp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ColumnP_strategy)
def test_softgallerylanguage::columnp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::RefTable::p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reftable::p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::RefTable::p)

@given(instance=softGalleryLanguage::RefTable::p_strategy)
def test_softgallerylanguage::reftable::p_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::RefTable::p_strategy)
def test_softgallerylanguage::reftable::p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ForeignKeyRef_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::foreignkeyref_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ForeignKeyRef)

@given(instance=softGalleryLanguage::ForeignKey::n_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::foreignkey::n_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ForeignKey::n)

@given(instance=softGalleryLanguage::ForeignKey::n_strategy)
def test_softgallerylanguage::foreignkey::n_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ForeignKey::n_strategy)
def test_softgallerylanguage::foreignkey::n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ForeignKey_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::foreignkey_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ForeignKey)

@given(instance=softGalleryLanguage::Table::p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::table::p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Table::p)

@given(instance=softGalleryLanguage::Table::p_strategy)
def test_softgallerylanguage::table::p_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Table::p_strategy)
def test_softgallerylanguage::table::p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ViewSchema_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::viewschema_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ViewSchema)

@given(instance=softGalleryLanguage::ViewSchema_strategy)
def test_softgallerylanguage::viewschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ViewSchema_strategy)
def test_softgallerylanguage::viewschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Index::p_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::index::p_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Index::p)

@given(instance=softGalleryLanguage::Index::p_strategy)
def test_softgallerylanguage::index::p_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Index::p_strategy)
def test_softgallerylanguage::index::p_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Schema_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::schema_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Schema)

@given(instance=softGalleryLanguage::Database_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::database_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Database)

@given(instance=softGalleryLanguage::Database_strategy)
def test_softgallerylanguage::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Database_strategy)
def test_softgallerylanguage::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Cluster_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::cluster_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Cluster)

@given(instance=softGalleryLanguage::Row_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::row_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Row)

@given(instance=softGalleryLanguage::Row_strategy)
def test_softgallerylanguage::row_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Row_strategy)
def test_softgallerylanguage::row_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactInformation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactinformation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactInformation)

@given(instance=softGalleryLanguage::ReactInformation_strategy)
def test_softgallerylanguage::reactinformation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactInformation_strategy)
def test_softgallerylanguage::reactinformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactLibrary_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactlibrary_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactLibrary)

@given(instance=softGalleryLanguage::ReactLibrary_strategy)
def test_softgallerylanguage::reactlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactLibrary_strategy)
def test_softgallerylanguage::reactlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactsRelationServ_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactsrelationserv_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactsRelationServ)

@given(instance=softGalleryLanguage::ReactsRelationServ_strategy)
def test_softgallerylanguage::reactsrelationserv_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactsRelationServ_strategy)
def test_softgallerylanguage::reactsrelationserv_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactServiceRequestProps_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactservicerequestprops_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactServiceRequestProps)

@given(instance=softGalleryLanguage::ReactServiceRequestProps_strategy)
def test_softgallerylanguage::reactservicerequestprops_reqPropName_type(instance):
    assert isinstance(instance.reqPropName, str)


@given(instance=softGalleryLanguage::ReactServiceRequestProps_strategy)
def test_softgallerylanguage::reactservicerequestprops_reqPropName_setter(instance):
    original = instance.reqPropName
    instance.reqPropName = original
    assert instance.reqPropName == original

@given(instance=softGalleryLanguage::ReactServiceRequestProps_strategy)
def test_softgallerylanguage::reactservicerequestprops_reqPropDescription_type(instance):
    assert isinstance(instance.reqPropDescription, str)


@given(instance=softGalleryLanguage::ReactServiceRequestProps_strategy)
def test_softgallerylanguage::reactservicerequestprops_reqPropDescription_setter(instance):
    original = instance.reqPropDescription
    instance.reqPropDescription = original
    assert instance.reqPropDescription == original

@given(instance=softGalleryLanguage::ReactServiceContRequest_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactservicecontrequest_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactServiceContRequest)

@given(instance=softGalleryLanguage::ReactServiceContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactservicecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactServiceContent)

@given(instance=softGalleryLanguage::ReactServiceContent_strategy)
def test_softgallerylanguage::reactservicecontent_functName_type(instance):
    assert isinstance(instance.functName, str)


@given(instance=softGalleryLanguage::ReactServiceContent_strategy)
def test_softgallerylanguage::reactservicecontent_functName_setter(instance):
    original = instance.functName
    instance.functName = original
    assert instance.functName == original

@given(instance=softGalleryLanguage::ReactServicesType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactservicestype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactServicesType)

@given(instance=softGalleryLanguage::ReactServicesType_strategy)
def test_softgallerylanguage::reactservicestype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactServicesType_strategy)
def test_softgallerylanguage::reactservicestype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactServicesRelation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactservicesrelation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactServicesRelation)

@given(instance=softGalleryLanguage::ReactActionsContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactactionscontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactActionsContent)

@given(instance=softGalleryLanguage::StylePropertiesContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::stylepropertiescontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StylePropertiesContent)

@given(instance=softGalleryLanguage::StylePropertiesContent_strategy)
def test_softgallerylanguage::stylepropertiescontent_propName_type(instance):
    assert isinstance(instance.propName, str)


@given(instance=softGalleryLanguage::StylePropertiesContent_strategy)
def test_softgallerylanguage::stylepropertiescontent_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=softGalleryLanguage::ComponentsStylesContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::componentsstylescontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ComponentsStylesContent)

@given(instance=softGalleryLanguage::ComponentsStylesContent_strategy)
def test_softgallerylanguage::componentsstylescontent_nameStyle_type(instance):
    assert isinstance(instance.nameStyle, str)


@given(instance=softGalleryLanguage::ComponentsStylesContent_strategy)
def test_softgallerylanguage::componentsstylescontent_nameStyle_setter(instance):
    original = instance.nameStyle
    instance.nameStyle = original
    assert instance.nameStyle == original

@given(instance=softGalleryLanguage::PropsType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::propstype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PropsType)

@given(instance=softGalleryLanguage::PropsType_strategy)
def test_softgallerylanguage::propstype_propsdatas_type(instance):
    assert isinstance(instance.propsdatas, str)


@given(instance=softGalleryLanguage::PropsType_strategy)
def test_softgallerylanguage::propstype_propsdatas_setter(instance):
    original = instance.propsdatas
    instance.propsdatas = original
    assert instance.propsdatas == original

@given(instance=softGalleryLanguage::PropsType_strategy)
def test_softgallerylanguage::propstype_nameProps_type(instance):
    assert isinstance(instance.nameProps, str)


@given(instance=softGalleryLanguage::PropsType_strategy)
def test_softgallerylanguage::propstype_nameProps_setter(instance):
    original = instance.nameProps
    instance.nameProps = original
    assert instance.nameProps == original

@given(instance=softGalleryLanguage::StateContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::statecontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StateContent)

@given(instance=softGalleryLanguage::StateContent_strategy)
def test_softgallerylanguage::statecontent_stateName_type(instance):
    assert isinstance(instance.stateName, str)


@given(instance=softGalleryLanguage::StateContent_strategy)
def test_softgallerylanguage::statecontent_stateName_setter(instance):
    original = instance.stateName
    instance.stateName = original
    assert instance.stateName == original

@given(instance=softGalleryLanguage::StateContent_strategy)
def test_softgallerylanguage::statecontent_componentdatatyp_type(instance):
    assert isinstance(instance.componentdatatyp, str)


@given(instance=softGalleryLanguage::StateContent_strategy)
def test_softgallerylanguage::statecontent_componentdatatyp_setter(instance):
    original = instance.componentdatatyp
    instance.componentdatatyp = original
    assert instance.componentdatatyp == original

@given(instance=softGalleryLanguage::CoreFunctionsDeclaration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::corefunctionsdeclaration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::CoreFunctionsDeclaration)

@given(instance=softGalleryLanguage::CoreFunctionsDeclaration_strategy)
def test_softgallerylanguage::corefunctionsdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::CoreFunctionsDeclaration_strategy)
def test_softgallerylanguage::corefunctionsdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::State_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::state_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::State)

@given(instance=softGalleryLanguage::ReactCoreFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactcorefunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactCoreFunctions)

@given(instance=softGalleryLanguage::ReactCoreFunctions_strategy)
def test_softgallerylanguage::reactcorefunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactCoreFunctions_strategy)
def test_softgallerylanguage::reactcorefunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactConstructor_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactconstructor_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactConstructor)

@given(instance=softGalleryLanguage::ReactImportContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactimportcontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactImportContent)

@given(instance=softGalleryLanguage::ReactImportContent_strategy)
def test_softgallerylanguage::reactimportcontent_impName_type(instance):
    assert isinstance(instance.impName, str)


@given(instance=softGalleryLanguage::ReactImportContent_strategy)
def test_softgallerylanguage::reactimportcontent_impName_setter(instance):
    original = instance.impName
    instance.impName = original
    assert instance.impName == original

@given(instance=softGalleryLanguage::StyleProperties_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::styleproperties_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StyleProperties)

@given(instance=softGalleryLanguage::Props_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::props_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Props)

@given(instance=softGalleryLanguage::ReactFunctions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactfunctions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactFunctions)

@given(instance=softGalleryLanguage::ReactFunctions_strategy)
def test_softgallerylanguage::reactfunctions_lifecycleclass_type(instance):
    assert isinstance(instance.lifecycleclass, str)


@given(instance=softGalleryLanguage::ReactFunctions_strategy)
def test_softgallerylanguage::reactfunctions_lifecycleclass_setter(instance):
    original = instance.lifecycleclass
    instance.lifecycleclass = original
    assert instance.lifecycleclass == original

@given(instance=softGalleryLanguage::ReactFunctions_strategy)
def test_softgallerylanguage::reactfunctions_renderclass_type(instance):
    assert isinstance(instance.renderclass, str)


@given(instance=softGalleryLanguage::ReactFunctions_strategy)
def test_softgallerylanguage::reactfunctions_renderclass_setter(instance):
    original = instance.renderclass
    instance.renderclass = original
    assert instance.renderclass == original

@given(instance=softGalleryLanguage::ReactImports_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactimports_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactImports)

@given(instance=softGalleryLanguage::SubcomponentCont_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::subcomponentcont_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SubcomponentCont)

@given(instance=softGalleryLanguage::SubcomponentCont_strategy)
def test_softgallerylanguage::subcomponentcont_nameSubComp_type(instance):
    assert isinstance(instance.nameSubComp, str)


@given(instance=softGalleryLanguage::SubcomponentCont_strategy)
def test_softgallerylanguage::subcomponentcont_nameSubComp_setter(instance):
    original = instance.nameSubComp
    instance.nameSubComp = original
    assert instance.nameSubComp == original

@given(instance=softGalleryLanguage::ViewComponentCont_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::viewcomponentcont_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ViewComponentCont)

@given(instance=softGalleryLanguage::ViewComponentCont_strategy)
def test_softgallerylanguage::viewcomponentcont_nameView_type(instance):
    assert isinstance(instance.nameView, str)


@given(instance=softGalleryLanguage::ViewComponentCont_strategy)
def test_softgallerylanguage::viewcomponentcont_nameView_setter(instance):
    original = instance.nameView
    instance.nameView = original
    assert instance.nameView == original

@given(instance=softGalleryLanguage::UIContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::uicontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::UIContent)

@given(instance=softGalleryLanguage::ComponentClass_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::componentclass_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ComponentClass)

@given(instance=softGalleryLanguage::LogicStructure_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::logicstructure_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LogicStructure)

@given(instance=softGalleryLanguage::LogicStructure_strategy)
def test_softgallerylanguage::logicstructure_indexCompName_type(instance):
    assert isinstance(instance.indexCompName, str)


@given(instance=softGalleryLanguage::LogicStructure_strategy)
def test_softgallerylanguage::logicstructure_indexCompName_setter(instance):
    original = instance.indexCompName
    instance.indexCompName = original
    assert instance.indexCompName == original

@given(instance=softGalleryLanguage::LogicStructure_strategy)
def test_softgallerylanguage::logicstructure_appComName_type(instance):
    assert isinstance(instance.appComName, str)


@given(instance=softGalleryLanguage::LogicStructure_strategy)
def test_softgallerylanguage::logicstructure_appComName_setter(instance):
    original = instance.appComName
    instance.appComName = original
    assert instance.appComName == original

@given(instance=softGalleryLanguage::LogicContent_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::logiccontent_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::LogicContent)

@given(instance=softGalleryLanguage::LogicContent_strategy)
def test_softgallerylanguage::logiccontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::LogicContent_strategy)
def test_softgallerylanguage::logiccontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ComponentsStyles_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::componentsstyles_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ComponentsStyles)

@given(instance=softGalleryLanguage::ComponentsLogic_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::componentslogic_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ComponentsLogic)

@given(instance=softGalleryLanguage::ComponentsLogic_strategy)
def test_softgallerylanguage::componentslogic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ComponentsLogic_strategy)
def test_softgallerylanguage::componentslogic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::DOMConfigurations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::domconfigurations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::DOMConfigurations)

@given(instance=softGalleryLanguage::DOMConfigurations_strategy)
def test_softgallerylanguage::domconfigurations_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=softGalleryLanguage::DOMConfigurations_strategy)
def test_softgallerylanguage::domconfigurations_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=softGalleryLanguage::DOMConfigurations_strategy)
def test_softgallerylanguage::domconfigurations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::DOMConfigurations_strategy)
def test_softgallerylanguage::domconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PackageVersion_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::packageversion_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PackageVersion)

@given(instance=softGalleryLanguage::PackageVersion_strategy)
def test_softgallerylanguage::packageversion_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PackageVersion_strategy)
def test_softgallerylanguage::packageversion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::PackageName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::packagename_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::PackageName)

@given(instance=softGalleryLanguage::PackageName_strategy)
def test_softgallerylanguage::packagename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::PackageName_strategy)
def test_softgallerylanguage::packagename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SingleDependencies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::singledependencies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SingleDependencies)

@given(instance=softGalleryLanguage::ReactDependenciesSubRules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactdependenciessubrules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactDependenciesSubRules)

@given(instance=softGalleryLanguage::ReactDependenciesRules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactdependenciesrules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactDependenciesRules)

@given(instance=softGalleryLanguage::ReactDependenciesRules_strategy)
def test_softgallerylanguage::reactdependenciesrules_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactDependenciesRules_strategy)
def test_softgallerylanguage::reactdependenciesrules_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactConfigurations_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactconfigurations_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactConfigurations)

@given(instance=softGalleryLanguage::ReactConfigurations_strategy)
def test_softgallerylanguage::reactconfigurations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ReactConfigurations_strategy)
def test_softgallerylanguage::reactconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactDependencies_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactdependencies_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactDependencies)

@given(instance=softGalleryLanguage::ReactInfo_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactinfo_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactInfo)

@given(instance=softGalleryLanguage::ReactLibraries_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactlibraries_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactLibraries)

@given(instance=softGalleryLanguage::ReactActions_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactactions_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactActions)

@given(instance=softGalleryLanguage::ComponentsUI_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::componentsui_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ComponentsUI)

@given(instance=softGalleryLanguage::ComponentsUI_strategy)
def test_softgallerylanguage::componentsui_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ComponentsUI_strategy)
def test_softgallerylanguage::componentsui_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactConfiguration_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactconfiguration_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactConfiguration)

@given(instance=softGalleryLanguage::ReactSubModules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactsubmodules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactSubModules)

@given(instance=softGalleryLanguage::ReactModules_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactmodules_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactModules)

@given(instance=softGalleryLanguage::StorageActionMemberName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageactionmembername_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageActionMemberName)

@given(instance=softGalleryLanguage::StorageActionMemberName_strategy)
def test_softgallerylanguage::storageactionmembername_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageActionMemberName_strategy)
def test_softgallerylanguage::storageactionmembername_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageActionMemberType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageactionmembertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageActionMemberType)

@given(instance=softGalleryLanguage::StorageActionMemberType_strategy)
def test_softgallerylanguage::storageactionmembertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageActionMemberType_strategy)
def test_softgallerylanguage::storageactionmembertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageActionMember_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageactionmember_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageActionMember)

@given(instance=softGalleryLanguage::StorageActionReturn_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageactionreturn_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageActionReturn)

@given(instance=softGalleryLanguage::StorageActionReturn_strategy)
def test_softgallerylanguage::storageactionreturn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageActionReturn_strategy)
def test_softgallerylanguage::storageactionreturn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageActionAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageactionannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageActionAnnotation)

@given(instance=softGalleryLanguage::StorageActionAnnotation_strategy)
def test_softgallerylanguage::storageactionannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageActionAnnotation_strategy)
def test_softgallerylanguage::storageactionannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageAction_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageaction_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageAction)

@given(instance=softGalleryLanguage::StorageAction_strategy)
def test_softgallerylanguage::storageaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageAction_strategy)
def test_softgallerylanguage::storageaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageMemberAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storagememberannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageMemberAnnotation)

@given(instance=softGalleryLanguage::StorageMemberAnnotation_strategy)
def test_softgallerylanguage::storagememberannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageMemberAnnotation_strategy)
def test_softgallerylanguage::storagememberannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageMemberType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storagemembertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageMemberType)

@given(instance=softGalleryLanguage::StorageMemberType_strategy)
def test_softgallerylanguage::storagemembertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageMemberType_strategy)
def test_softgallerylanguage::storagemembertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageMember_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storagemember_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageMember)

@given(instance=softGalleryLanguage::StorageMember_strategy)
def test_softgallerylanguage::storagemember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageMember_strategy)
def test_softgallerylanguage::storagemember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::StorageClient_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::storageclient_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::StorageClient)

@given(instance=softGalleryLanguage::StorageClient_strategy)
def test_softgallerylanguage::storageclient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::StorageClient_strategy)
def test_softgallerylanguage::storageclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::SpringEntityAnnotationTypes_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::springentityannotationtypes_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::SpringEntityAnnotationTypes)

@given(instance=softGalleryLanguage::SpringEntityAnnotationTypes_strategy)
def test_softgallerylanguage::springentityannotationtypes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::SpringEntityAnnotationTypes_strategy)
def test_softgallerylanguage::springentityannotationtypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ReactComponents_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::reactcomponents_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ReactComponents)

@given(instance=softGalleryLanguage::ExceptionProcess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::exceptionprocess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ExceptionProcess)

@given(instance=softGalleryLanguage::ExceptionProcess_strategy)
def test_softgallerylanguage::exceptionprocess_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ExceptionProcess_strategy)
def test_softgallerylanguage::exceptionprocess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::exceptionhandler_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ExceptionHandler)

@given(instance=softGalleryLanguage::ExceptionHandler_strategy)
def test_softgallerylanguage::exceptionhandler_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ExceptionHandler_strategy)
def test_softgallerylanguage::exceptionhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ResponseParameterName_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::responseparametername_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ResponseParameterName)

@given(instance=softGalleryLanguage::ResponseParameterName_strategy)
def test_softgallerylanguage::responseparametername_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ResponseParameterName_strategy)
def test_softgallerylanguage::responseparametername_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ResponseParameterType_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::responseparametertype_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ResponseParameterType)

@given(instance=softGalleryLanguage::ResponseParameterType_strategy)
def test_softgallerylanguage::responseparametertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ResponseParameterType_strategy)
def test_softgallerylanguage::responseparametertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ResponseParameterAnnotation_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::responseparameterannotation_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ResponseParameterAnnotation)

@given(instance=softGalleryLanguage::ResponseParameterAnnotation_strategy)
def test_softgallerylanguage::responseparameterannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::ResponseParameterAnnotation_strategy)
def test_softgallerylanguage::responseparameterannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AppAccess_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::appaccess_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AppAccess)

@given(instance=softGalleryLanguage::ProfileManagement_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::profilemanagement_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ProfileManagement)

@given(instance=softGalleryLanguage::Functionalities_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::functionalities_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Functionalities)

@given(instance=softGalleryLanguage::AtributeUserDomain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::atributeuserdomain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AtributeUserDomain)

@given(instance=softGalleryLanguage::AtributeUserDomain_strategy)
def test_softgallerylanguage::atributeuserdomain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AtributeUserDomain_strategy)
def test_softgallerylanguage::atributeuserdomain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AtributeAlbum_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::atributealbum_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AtributeAlbum)

@given(instance=softGalleryLanguage::AtributeAlbum_strategy)
def test_softgallerylanguage::atributealbum_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AtributeAlbum_strategy)
def test_softgallerylanguage::atributealbum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::AtributePhoto_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::atributephoto_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::AtributePhoto)

@given(instance=softGalleryLanguage::AtributePhoto_strategy)
def test_softgallerylanguage::atributephoto_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::AtributePhoto_strategy)
def test_softgallerylanguage::atributephoto_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::Entities_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::entities_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Entities)

@given(instance=softGalleryLanguage::Entities_strategy)
def test_softgallerylanguage::entities_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Entities_strategy)
def test_softgallerylanguage::entities_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::ExceptionsDomain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::exceptionsdomain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::ExceptionsDomain)

@given(instance=softGalleryLanguage::Functionality_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::functionality_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Functionality)

@given(instance=softGalleryLanguage::Entity_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::entity_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Entity)

@given(instance=softGalleryLanguage::Domain_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::domain_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Domain)

@given(instance=softGalleryLanguage::Domain_strategy)
def test_softgallerylanguage::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=softGalleryLanguage::Domain_strategy)
def test_softgallerylanguage::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=softGalleryLanguage::EObject_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::eobject_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::EObject)

@given(instance=softGalleryLanguage::Model_strategy)
@settings(max_examples=50)
def test_softgallerylanguage::model_instantiation(instance):
    assert isinstance(instance, softGalleryLanguage::Model)
