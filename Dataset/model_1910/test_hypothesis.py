import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::AmazonWebServices,
    myDsl::PostgreSQL,
    myDsl::Spring,
    myDsl::ReactInformation,
    myDsl::ReactInfo,
    myDsl::ReactLibrary,
    myDsl::ReactLibraries,
    myDsl::ReactServicesType,
    myDsl::ReactServicesRelation,
    myDsl::ReactActionsContent,
    myDsl::ReactActions,
    myDsl::ReactCoreFunctions,
    myDsl::Props,
    myDsl::CoreFunctionsDeclaration,
    myDsl::State,
    myDsl::ReactConstructor,
    myDsl::UIContent,
    myDsl::ComponentClass,
    myDsl::LogicStructure,
    myDsl::LogicContent,
    myDsl::ComponentsUI,
    myDsl::ComponentsLogic,
    myDsl::ReactComponents,
    myDsl::DOMConfigurations,
    myDsl::PackageVersion,
    myDsl::PackageName,
    myDsl::ReactFunctions,
    myDsl::ReactDependenciesSubRules,
    myDsl::ReactDependenciesRules,
    myDsl::ReactConfigurations,
    myDsl::ReactDependencies,
    myDsl::ReactConfiguration,
    myDsl::ReactSubModules,
    myDsl::ReactModules,
    myDsl::React,
    myDsl::Technologies,
    myDsl::Technology,
    myDsl::NTiersRelations,
    myDsl::NTierSource,
    myDsl::NTierTarget,
    myDsl::SingleDependencies,
    myDsl::NTiersConnections,
    myDsl::PersistenceDataComponent,
    myDsl::BackEnd,
    myDsl::FrontEnd,
    myDsl::ArchitectureComponents,
    myDsl::LayerTarget,
    myDsl::LayerSource,
    myDsl::LayerRelations,
    myDsl::SingleFile,
    myDsl::MultipleFile,
    myDsl::Directories,
    myDsl::DirectoryContent,
    myDsl::DataPersistenceContent,
    myDsl::DataPersistenceLayer,
    myDsl::BusinessLogicSegments,
    myDsl::BusinessLogicContent,
    myDsl::BusinessLogicLayer,
    myDsl::PresentationSegments,
    myDsl::PresentationContent,
    myDsl::PresentationLayer,
    myDsl::Layer,
    myDsl::NTiers,
    myDsl::Architecture,
    myDsl::DomainRelations,
    myDsl::DomainConnection,
    myDsl::LandingFunctions,
    myDsl::PhotoActionsFunctions,
    myDsl::AlbumManagementFunctions,
    myDsl::SegmentStructureContent,
    myDsl::SegmentStructure,
    myDsl::DataPersistenceSegments,
    myDsl::ProfileManagementFunctions,
    myDsl::LandingActions,
    myDsl::PhotoActions,
    myDsl::AlbumManagement,
    myDsl::AppAccess,
    myDsl::ProfileManagement,
    myDsl::Functionalities,
    myDsl::Functionality,
    myDsl::UserDomain,
    myDsl::Album,
    myDsl::Photo,
    myDsl::Entities,
    myDsl::Entity,
    myDsl::Domain,
    myDsl::EObject,
    myDsl::Model,
    myDsl::AppAccessFunctions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::amazonwebservices_is_not_abstract():
    assert not inspect.isabstract(myDsl::AmazonWebServices)


def test_mydsl::amazonwebservices_constructor_exists():
    assert callable(myDsl::AmazonWebServices.__init__)


def test_mydsl::amazonwebservices_constructor_args():
    sig = inspect.signature(myDsl::AmazonWebServices.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::amazonwebservices_has_name():
    assert hasattr(myDsl::AmazonWebServices, "name")
    descriptor = None
    for klass in myDsl::AmazonWebServices.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::postgresql_is_not_abstract():
    assert not inspect.isabstract(myDsl::PostgreSQL)


def test_mydsl::postgresql_constructor_exists():
    assert callable(myDsl::PostgreSQL.__init__)


def test_mydsl::postgresql_constructor_args():
    sig = inspect.signature(myDsl::PostgreSQL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::postgresql_has_name():
    assert hasattr(myDsl::PostgreSQL, "name")
    descriptor = None
    for klass in myDsl::PostgreSQL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::spring_is_not_abstract():
    assert not inspect.isabstract(myDsl::Spring)


def test_mydsl::spring_constructor_exists():
    assert callable(myDsl::Spring.__init__)


def test_mydsl::spring_constructor_args():
    sig = inspect.signature(myDsl::Spring.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::spring_has_name():
    assert hasattr(myDsl::Spring, "name")
    descriptor = None
    for klass in myDsl::Spring.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactinformation_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactInformation)


def test_mydsl::reactinformation_constructor_exists():
    assert callable(myDsl::ReactInformation.__init__)


def test_mydsl::reactinformation_constructor_args():
    sig = inspect.signature(myDsl::ReactInformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactinformation_has_name():
    assert hasattr(myDsl::ReactInformation, "name")
    descriptor = None
    for klass in myDsl::ReactInformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactinfo_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactInfo)


def test_mydsl::reactinfo_constructor_exists():
    assert callable(myDsl::ReactInfo.__init__)


def test_mydsl::reactinfo_constructor_args():
    sig = inspect.signature(myDsl::ReactInfo.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactlibrary_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactLibrary)


def test_mydsl::reactlibrary_constructor_exists():
    assert callable(myDsl::ReactLibrary.__init__)


def test_mydsl::reactlibrary_constructor_args():
    sig = inspect.signature(myDsl::ReactLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactlibrary_has_name():
    assert hasattr(myDsl::ReactLibrary, "name")
    descriptor = None
    for klass in myDsl::ReactLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactlibraries_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactLibraries)


def test_mydsl::reactlibraries_constructor_exists():
    assert callable(myDsl::ReactLibraries.__init__)


def test_mydsl::reactlibraries_constructor_args():
    sig = inspect.signature(myDsl::ReactLibraries.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactservicestype_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactServicesType)


def test_mydsl::reactservicestype_constructor_exists():
    assert callable(myDsl::ReactServicesType.__init__)


def test_mydsl::reactservicestype_constructor_args():
    sig = inspect.signature(myDsl::ReactServicesType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactservicestype_has_name():
    assert hasattr(myDsl::ReactServicesType, "name")
    descriptor = None
    for klass in myDsl::ReactServicesType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactservicesrelation_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactServicesRelation)


def test_mydsl::reactservicesrelation_constructor_exists():
    assert callable(myDsl::ReactServicesRelation.__init__)


def test_mydsl::reactservicesrelation_constructor_args():
    sig = inspect.signature(myDsl::ReactServicesRelation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactservicesrelation_has_name():
    assert hasattr(myDsl::ReactServicesRelation, "name")
    descriptor = None
    for klass in myDsl::ReactServicesRelation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactactionscontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactActionsContent)


def test_mydsl::reactactionscontent_constructor_exists():
    assert callable(myDsl::ReactActionsContent.__init__)


def test_mydsl::reactactionscontent_constructor_args():
    sig = inspect.signature(myDsl::ReactActionsContent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactactions_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactActions)


def test_mydsl::reactactions_constructor_exists():
    assert callable(myDsl::ReactActions.__init__)


def test_mydsl::reactactions_constructor_args():
    sig = inspect.signature(myDsl::ReactActions.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactcorefunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactCoreFunctions)


def test_mydsl::reactcorefunctions_constructor_exists():
    assert callable(myDsl::ReactCoreFunctions.__init__)


def test_mydsl::reactcorefunctions_constructor_args():
    sig = inspect.signature(myDsl::ReactCoreFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactcorefunctions_has_name():
    assert hasattr(myDsl::ReactCoreFunctions, "name")
    descriptor = None
    for klass in myDsl::ReactCoreFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::props_is_not_abstract():
    assert not inspect.isabstract(myDsl::Props)


def test_mydsl::props_constructor_exists():
    assert callable(myDsl::Props.__init__)


def test_mydsl::props_constructor_args():
    sig = inspect.signature(myDsl::Props.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "componentclass" in params, "Missing parameter 'componentclass'"

def test_mydsl::props_has_name():
    assert hasattr(myDsl::Props, "name")
    descriptor = None
    for klass in myDsl::Props.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::props_has_componentclass():
    assert hasattr(myDsl::Props, "componentclass")
    descriptor = None
    for klass in myDsl::Props.__mro__:
        if "componentclass" in klass.__dict__:
            descriptor = klass.__dict__["componentclass"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::corefunctionsdeclaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::CoreFunctionsDeclaration)


def test_mydsl::corefunctionsdeclaration_constructor_exists():
    assert callable(myDsl::CoreFunctionsDeclaration.__init__)


def test_mydsl::corefunctionsdeclaration_constructor_args():
    sig = inspect.signature(myDsl::CoreFunctionsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::corefunctionsdeclaration_has_name():
    assert hasattr(myDsl::CoreFunctionsDeclaration, "name")
    descriptor = None
    for klass in myDsl::CoreFunctionsDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::state_is_not_abstract():
    assert not inspect.isabstract(myDsl::State)


def test_mydsl::state_constructor_exists():
    assert callable(myDsl::State.__init__)


def test_mydsl::state_constructor_args():
    sig = inspect.signature(myDsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "componentclass" in params, "Missing parameter 'componentclass'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::state_has_componentclass():
    assert hasattr(myDsl::State, "componentclass")
    descriptor = None
    for klass in myDsl::State.__mro__:
        if "componentclass" in klass.__dict__:
            descriptor = klass.__dict__["componentclass"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::state_has_name():
    assert hasattr(myDsl::State, "name")
    descriptor = None
    for klass in myDsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactconstructor_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactConstructor)


def test_mydsl::reactconstructor_constructor_exists():
    assert callable(myDsl::ReactConstructor.__init__)


def test_mydsl::reactconstructor_constructor_args():
    sig = inspect.signature(myDsl::ReactConstructor.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::uicontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::UIContent)


def test_mydsl::uicontent_constructor_exists():
    assert callable(myDsl::UIContent.__init__)


def test_mydsl::uicontent_constructor_args():
    sig = inspect.signature(myDsl::UIContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::uicontent_has_name():
    assert hasattr(myDsl::UIContent, "name")
    descriptor = None
    for klass in myDsl::UIContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::componentclass_is_not_abstract():
    assert not inspect.isabstract(myDsl::ComponentClass)


def test_mydsl::componentclass_constructor_exists():
    assert callable(myDsl::ComponentClass.__init__)


def test_mydsl::componentclass_constructor_args():
    sig = inspect.signature(myDsl::ComponentClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logicstructure_is_not_abstract():
    assert not inspect.isabstract(myDsl::LogicStructure)


def test_mydsl::logicstructure_constructor_exists():
    assert callable(myDsl::LogicStructure.__init__)


def test_mydsl::logicstructure_constructor_args():
    sig = inspect.signature(myDsl::LogicStructure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::logicstructure_has_name():
    assert hasattr(myDsl::LogicStructure, "name")
    descriptor = None
    for klass in myDsl::LogicStructure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::logiccontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::LogicContent)


def test_mydsl::logiccontent_constructor_exists():
    assert callable(myDsl::LogicContent.__init__)


def test_mydsl::logiccontent_constructor_args():
    sig = inspect.signature(myDsl::LogicContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::logiccontent_has_name():
    assert hasattr(myDsl::LogicContent, "name")
    descriptor = None
    for klass in myDsl::LogicContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::componentsui_is_not_abstract():
    assert not inspect.isabstract(myDsl::ComponentsUI)


def test_mydsl::componentsui_constructor_exists():
    assert callable(myDsl::ComponentsUI.__init__)


def test_mydsl::componentsui_constructor_args():
    sig = inspect.signature(myDsl::ComponentsUI.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::componentsui_has_name():
    assert hasattr(myDsl::ComponentsUI, "name")
    descriptor = None
    for klass in myDsl::ComponentsUI.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::componentslogic_is_not_abstract():
    assert not inspect.isabstract(myDsl::ComponentsLogic)


def test_mydsl::componentslogic_constructor_exists():
    assert callable(myDsl::ComponentsLogic.__init__)


def test_mydsl::componentslogic_constructor_args():
    sig = inspect.signature(myDsl::ComponentsLogic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::componentslogic_has_name():
    assert hasattr(myDsl::ComponentsLogic, "name")
    descriptor = None
    for klass in myDsl::ComponentsLogic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactcomponents_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactComponents)


def test_mydsl::reactcomponents_constructor_exists():
    assert callable(myDsl::ReactComponents.__init__)


def test_mydsl::reactcomponents_constructor_args():
    sig = inspect.signature(myDsl::ReactComponents.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::domconfigurations_is_not_abstract():
    assert not inspect.isabstract(myDsl::DOMConfigurations)


def test_mydsl::domconfigurations_constructor_exists():
    assert callable(myDsl::DOMConfigurations.__init__)


def test_mydsl::domconfigurations_constructor_args():
    sig = inspect.signature(myDsl::DOMConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::domconfigurations_has_elements():
    assert hasattr(myDsl::DOMConfigurations, "elements")
    descriptor = None
    for klass in myDsl::DOMConfigurations.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::domconfigurations_has_name():
    assert hasattr(myDsl::DOMConfigurations, "name")
    descriptor = None
    for klass in myDsl::DOMConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::packageversion_is_not_abstract():
    assert not inspect.isabstract(myDsl::PackageVersion)


def test_mydsl::packageversion_constructor_exists():
    assert callable(myDsl::PackageVersion.__init__)


def test_mydsl::packageversion_constructor_args():
    sig = inspect.signature(myDsl::PackageVersion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::packageversion_has_name():
    assert hasattr(myDsl::PackageVersion, "name")
    descriptor = None
    for klass in myDsl::PackageVersion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::packagename_is_not_abstract():
    assert not inspect.isabstract(myDsl::PackageName)


def test_mydsl::packagename_constructor_exists():
    assert callable(myDsl::PackageName.__init__)


def test_mydsl::packagename_constructor_args():
    sig = inspect.signature(myDsl::PackageName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::packagename_has_name():
    assert hasattr(myDsl::PackageName, "name")
    descriptor = None
    for klass in myDsl::PackageName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactFunctions)


def test_mydsl::reactfunctions_constructor_exists():
    assert callable(myDsl::ReactFunctions.__init__)


def test_mydsl::reactfunctions_constructor_args():
    sig = inspect.signature(myDsl::ReactFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "lifecycleclass" in params, "Missing parameter 'lifecycleclass'"
    assert "renderclass" in params, "Missing parameter 'renderclass'"

def test_mydsl::reactfunctions_has_lifecycleclass():
    assert hasattr(myDsl::ReactFunctions, "lifecycleclass")
    descriptor = None
    for klass in myDsl::ReactFunctions.__mro__:
        if "lifecycleclass" in klass.__dict__:
            descriptor = klass.__dict__["lifecycleclass"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::reactfunctions_has_renderclass():
    assert hasattr(myDsl::ReactFunctions, "renderclass")
    descriptor = None
    for klass in myDsl::ReactFunctions.__mro__:
        if "renderclass" in klass.__dict__:
            descriptor = klass.__dict__["renderclass"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactdependenciessubrules_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactDependenciesSubRules)


def test_mydsl::reactdependenciessubrules_constructor_exists():
    assert callable(myDsl::ReactDependenciesSubRules.__init__)


def test_mydsl::reactdependenciessubrules_constructor_args():
    sig = inspect.signature(myDsl::ReactDependenciesSubRules.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactdependenciesrules_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactDependenciesRules)


def test_mydsl::reactdependenciesrules_constructor_exists():
    assert callable(myDsl::ReactDependenciesRules.__init__)


def test_mydsl::reactdependenciesrules_constructor_args():
    sig = inspect.signature(myDsl::ReactDependenciesRules.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactdependenciesrules_has_name():
    assert hasattr(myDsl::ReactDependenciesRules, "name")
    descriptor = None
    for klass in myDsl::ReactDependenciesRules.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactconfigurations_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactConfigurations)


def test_mydsl::reactconfigurations_constructor_exists():
    assert callable(myDsl::ReactConfigurations.__init__)


def test_mydsl::reactconfigurations_constructor_args():
    sig = inspect.signature(myDsl::ReactConfigurations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reactconfigurations_has_name():
    assert hasattr(myDsl::ReactConfigurations, "name")
    descriptor = None
    for klass in myDsl::ReactConfigurations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactdependencies_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactDependencies)


def test_mydsl::reactdependencies_constructor_exists():
    assert callable(myDsl::ReactDependencies.__init__)


def test_mydsl::reactdependencies_constructor_args():
    sig = inspect.signature(myDsl::ReactDependencies.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactconfiguration_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactConfiguration)


def test_mydsl::reactconfiguration_constructor_exists():
    assert callable(myDsl::ReactConfiguration.__init__)


def test_mydsl::reactconfiguration_constructor_args():
    sig = inspect.signature(myDsl::ReactConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactsubmodules_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactSubModules)


def test_mydsl::reactsubmodules_constructor_exists():
    assert callable(myDsl::ReactSubModules.__init__)


def test_mydsl::reactsubmodules_constructor_args():
    sig = inspect.signature(myDsl::ReactSubModules.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::reactmodules_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactModules)


def test_mydsl::reactmodules_constructor_exists():
    assert callable(myDsl::ReactModules.__init__)


def test_mydsl::reactmodules_constructor_args():
    sig = inspect.signature(myDsl::ReactModules.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::react_is_not_abstract():
    assert not inspect.isabstract(myDsl::React)


def test_mydsl::react_constructor_exists():
    assert callable(myDsl::React.__init__)


def test_mydsl::react_constructor_args():
    sig = inspect.signature(myDsl::React.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::react_has_name():
    assert hasattr(myDsl::React, "name")
    descriptor = None
    for klass in myDsl::React.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::technologies_is_not_abstract():
    assert not inspect.isabstract(myDsl::Technologies)


def test_mydsl::technologies_constructor_exists():
    assert callable(myDsl::Technologies.__init__)


def test_mydsl::technologies_constructor_args():
    sig = inspect.signature(myDsl::Technologies.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::technology_is_not_abstract():
    assert not inspect.isabstract(myDsl::Technology)


def test_mydsl::technology_constructor_exists():
    assert callable(myDsl::Technology.__init__)


def test_mydsl::technology_constructor_args():
    sig = inspect.signature(myDsl::Technology.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::technology_has_name():
    assert hasattr(myDsl::Technology, "name")
    descriptor = None
    for klass in myDsl::Technology.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::ntiersrelations_is_not_abstract():
    assert not inspect.isabstract(myDsl::NTiersRelations)


def test_mydsl::ntiersrelations_constructor_exists():
    assert callable(myDsl::NTiersRelations.__init__)


def test_mydsl::ntiersrelations_constructor_args():
    sig = inspect.signature(myDsl::NTiersRelations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::ntiersrelations_has_name():
    assert hasattr(myDsl::NTiersRelations, "name")
    descriptor = None
    for klass in myDsl::NTiersRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::ntiersource_is_not_abstract():
    assert not inspect.isabstract(myDsl::NTierSource)


def test_mydsl::ntiersource_constructor_exists():
    assert callable(myDsl::NTierSource.__init__)


def test_mydsl::ntiersource_constructor_args():
    sig = inspect.signature(myDsl::NTierSource.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::ntiertarget_is_not_abstract():
    assert not inspect.isabstract(myDsl::NTierTarget)


def test_mydsl::ntiertarget_constructor_exists():
    assert callable(myDsl::NTierTarget.__init__)


def test_mydsl::ntiertarget_constructor_args():
    sig = inspect.signature(myDsl::NTierTarget.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::singledependencies_is_not_abstract():
    assert not inspect.isabstract(myDsl::SingleDependencies)


def test_mydsl::singledependencies_constructor_exists():
    assert callable(myDsl::SingleDependencies.__init__)


def test_mydsl::singledependencies_constructor_args():
    sig = inspect.signature(myDsl::SingleDependencies.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::ntiersconnections_is_not_abstract():
    assert not inspect.isabstract(myDsl::NTiersConnections)


def test_mydsl::ntiersconnections_constructor_exists():
    assert callable(myDsl::NTiersConnections.__init__)


def test_mydsl::ntiersconnections_constructor_args():
    sig = inspect.signature(myDsl::NTiersConnections.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ntierconnection" in params, "Missing parameter 'ntierconnection'"

def test_mydsl::ntiersconnections_has_name():
    assert hasattr(myDsl::NTiersConnections, "name")
    descriptor = None
    for klass in myDsl::NTiersConnections.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::ntiersconnections_has_ntierconnection():
    assert hasattr(myDsl::NTiersConnections, "ntierconnection")
    descriptor = None
    for klass in myDsl::NTiersConnections.__mro__:
        if "ntierconnection" in klass.__dict__:
            descriptor = klass.__dict__["ntierconnection"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::persistencedatacomponent_is_not_abstract():
    assert not inspect.isabstract(myDsl::PersistenceDataComponent)


def test_mydsl::persistencedatacomponent_constructor_exists():
    assert callable(myDsl::PersistenceDataComponent.__init__)


def test_mydsl::persistencedatacomponent_constructor_args():
    sig = inspect.signature(myDsl::PersistenceDataComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::persistencedatacomponent_has_name():
    assert hasattr(myDsl::PersistenceDataComponent, "name")
    descriptor = None
    for klass in myDsl::PersistenceDataComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::backend_is_not_abstract():
    assert not inspect.isabstract(myDsl::BackEnd)


def test_mydsl::backend_constructor_exists():
    assert callable(myDsl::BackEnd.__init__)


def test_mydsl::backend_constructor_args():
    sig = inspect.signature(myDsl::BackEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::backend_has_name():
    assert hasattr(myDsl::BackEnd, "name")
    descriptor = None
    for klass in myDsl::BackEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::frontend_is_not_abstract():
    assert not inspect.isabstract(myDsl::FrontEnd)


def test_mydsl::frontend_constructor_exists():
    assert callable(myDsl::FrontEnd.__init__)


def test_mydsl::frontend_constructor_args():
    sig = inspect.signature(myDsl::FrontEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::frontend_has_name():
    assert hasattr(myDsl::FrontEnd, "name")
    descriptor = None
    for klass in myDsl::FrontEnd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::architecturecomponents_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArchitectureComponents)


def test_mydsl::architecturecomponents_constructor_exists():
    assert callable(myDsl::ArchitectureComponents.__init__)


def test_mydsl::architecturecomponents_constructor_args():
    sig = inspect.signature(myDsl::ArchitectureComponents.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::layertarget_is_not_abstract():
    assert not inspect.isabstract(myDsl::LayerTarget)


def test_mydsl::layertarget_constructor_exists():
    assert callable(myDsl::LayerTarget.__init__)


def test_mydsl::layertarget_constructor_args():
    sig = inspect.signature(myDsl::LayerTarget.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_mydsl::layertarget_has_layerelations():
    assert hasattr(myDsl::LayerTarget, "layerelations")
    descriptor = None
    for klass in myDsl::LayerTarget.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::layersource_is_not_abstract():
    assert not inspect.isabstract(myDsl::LayerSource)


def test_mydsl::layersource_constructor_exists():
    assert callable(myDsl::LayerSource.__init__)


def test_mydsl::layersource_constructor_args():
    sig = inspect.signature(myDsl::LayerSource.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"

def test_mydsl::layersource_has_layerelations():
    assert hasattr(myDsl::LayerSource, "layerelations")
    descriptor = None
    for klass in myDsl::LayerSource.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::layerrelations_is_not_abstract():
    assert not inspect.isabstract(myDsl::LayerRelations)


def test_mydsl::layerrelations_constructor_exists():
    assert callable(myDsl::LayerRelations.__init__)


def test_mydsl::layerrelations_constructor_args():
    sig = inspect.signature(myDsl::LayerRelations.__init__)
    params = list(sig.parameters.keys())
    assert "layerelations" in params, "Missing parameter 'layerelations'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::layerrelations_has_layerelations():
    assert hasattr(myDsl::LayerRelations, "layerelations")
    descriptor = None
    for klass in myDsl::LayerRelations.__mro__:
        if "layerelations" in klass.__dict__:
            descriptor = klass.__dict__["layerelations"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::layerrelations_has_name():
    assert hasattr(myDsl::LayerRelations, "name")
    descriptor = None
    for klass in myDsl::LayerRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::singlefile_is_not_abstract():
    assert not inspect.isabstract(myDsl::SingleFile)


def test_mydsl::singlefile_constructor_exists():
    assert callable(myDsl::SingleFile.__init__)


def test_mydsl::singlefile_constructor_args():
    sig = inspect.signature(myDsl::SingleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::singlefile_has_name():
    assert hasattr(myDsl::SingleFile, "name")
    descriptor = None
    for klass in myDsl::SingleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::multiplefile_is_not_abstract():
    assert not inspect.isabstract(myDsl::MultipleFile)


def test_mydsl::multiplefile_constructor_exists():
    assert callable(myDsl::MultipleFile.__init__)


def test_mydsl::multiplefile_constructor_args():
    sig = inspect.signature(myDsl::MultipleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::multiplefile_has_name():
    assert hasattr(myDsl::MultipleFile, "name")
    descriptor = None
    for klass in myDsl::MultipleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::directories_is_not_abstract():
    assert not inspect.isabstract(myDsl::Directories)


def test_mydsl::directories_constructor_exists():
    assert callable(myDsl::Directories.__init__)


def test_mydsl::directories_constructor_args():
    sig = inspect.signature(myDsl::Directories.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::directorycontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::DirectoryContent)


def test_mydsl::directorycontent_constructor_exists():
    assert callable(myDsl::DirectoryContent.__init__)


def test_mydsl::directorycontent_constructor_args():
    sig = inspect.signature(myDsl::DirectoryContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::directorycontent_has_name():
    assert hasattr(myDsl::DirectoryContent, "name")
    descriptor = None
    for klass in myDsl::DirectoryContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::datapersistencecontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataPersistenceContent)


def test_mydsl::datapersistencecontent_constructor_exists():
    assert callable(myDsl::DataPersistenceContent.__init__)


def test_mydsl::datapersistencecontent_constructor_args():
    sig = inspect.signature(myDsl::DataPersistenceContent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datapersistencelayer_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataPersistenceLayer)


def test_mydsl::datapersistencelayer_constructor_exists():
    assert callable(myDsl::DataPersistenceLayer.__init__)


def test_mydsl::datapersistencelayer_constructor_args():
    sig = inspect.signature(myDsl::DataPersistenceLayer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::businesslogicsegments_is_not_abstract():
    assert not inspect.isabstract(myDsl::BusinessLogicSegments)


def test_mydsl::businesslogicsegments_constructor_exists():
    assert callable(myDsl::BusinessLogicSegments.__init__)


def test_mydsl::businesslogicsegments_constructor_args():
    sig = inspect.signature(myDsl::BusinessLogicSegments.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::businesslogicsegments_has_name():
    assert hasattr(myDsl::BusinessLogicSegments, "name")
    descriptor = None
    for klass in myDsl::BusinessLogicSegments.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::businesslogiccontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::BusinessLogicContent)


def test_mydsl::businesslogiccontent_constructor_exists():
    assert callable(myDsl::BusinessLogicContent.__init__)


def test_mydsl::businesslogiccontent_constructor_args():
    sig = inspect.signature(myDsl::BusinessLogicContent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::businesslogiclayer_is_not_abstract():
    assert not inspect.isabstract(myDsl::BusinessLogicLayer)


def test_mydsl::businesslogiclayer_constructor_exists():
    assert callable(myDsl::BusinessLogicLayer.__init__)


def test_mydsl::businesslogiclayer_constructor_args():
    sig = inspect.signature(myDsl::BusinessLogicLayer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::presentationsegments_is_not_abstract():
    assert not inspect.isabstract(myDsl::PresentationSegments)


def test_mydsl::presentationsegments_constructor_exists():
    assert callable(myDsl::PresentationSegments.__init__)


def test_mydsl::presentationsegments_constructor_args():
    sig = inspect.signature(myDsl::PresentationSegments.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::presentationsegments_has_name():
    assert hasattr(myDsl::PresentationSegments, "name")
    descriptor = None
    for klass in myDsl::PresentationSegments.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::presentationcontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::PresentationContent)


def test_mydsl::presentationcontent_constructor_exists():
    assert callable(myDsl::PresentationContent.__init__)


def test_mydsl::presentationcontent_constructor_args():
    sig = inspect.signature(myDsl::PresentationContent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::presentationlayer_is_not_abstract():
    assert not inspect.isabstract(myDsl::PresentationLayer)


def test_mydsl::presentationlayer_constructor_exists():
    assert callable(myDsl::PresentationLayer.__init__)


def test_mydsl::presentationlayer_constructor_args():
    sig = inspect.signature(myDsl::PresentationLayer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::layer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Layer)


def test_mydsl::layer_constructor_exists():
    assert callable(myDsl::Layer.__init__)


def test_mydsl::layer_constructor_args():
    sig = inspect.signature(myDsl::Layer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::ntiers_is_not_abstract():
    assert not inspect.isabstract(myDsl::NTiers)


def test_mydsl::ntiers_constructor_exists():
    assert callable(myDsl::NTiers.__init__)


def test_mydsl::ntiers_constructor_args():
    sig = inspect.signature(myDsl::NTiers.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::architecture_is_not_abstract():
    assert not inspect.isabstract(myDsl::Architecture)


def test_mydsl::architecture_constructor_exists():
    assert callable(myDsl::Architecture.__init__)


def test_mydsl::architecture_constructor_args():
    sig = inspect.signature(myDsl::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::domainrelations_is_not_abstract():
    assert not inspect.isabstract(myDsl::DomainRelations)


def test_mydsl::domainrelations_constructor_exists():
    assert callable(myDsl::DomainRelations.__init__)


def test_mydsl::domainrelations_constructor_args():
    sig = inspect.signature(myDsl::DomainRelations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::domainrelations_has_name():
    assert hasattr(myDsl::DomainRelations, "name")
    descriptor = None
    for klass in myDsl::DomainRelations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::domainconnection_is_not_abstract():
    assert not inspect.isabstract(myDsl::DomainConnection)


def test_mydsl::domainconnection_constructor_exists():
    assert callable(myDsl::DomainConnection.__init__)


def test_mydsl::domainconnection_constructor_args():
    sig = inspect.signature(myDsl::DomainConnection.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::landingfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::LandingFunctions)


def test_mydsl::landingfunctions_constructor_exists():
    assert callable(myDsl::LandingFunctions.__init__)


def test_mydsl::landingfunctions_constructor_args():
    sig = inspect.signature(myDsl::LandingFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::landingfunctions_has_name():
    assert hasattr(myDsl::LandingFunctions, "name")
    descriptor = None
    for klass in myDsl::LandingFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::photoactionsfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::PhotoActionsFunctions)


def test_mydsl::photoactionsfunctions_constructor_exists():
    assert callable(myDsl::PhotoActionsFunctions.__init__)


def test_mydsl::photoactionsfunctions_constructor_args():
    sig = inspect.signature(myDsl::PhotoActionsFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::photoactionsfunctions_has_name():
    assert hasattr(myDsl::PhotoActionsFunctions, "name")
    descriptor = None
    for klass in myDsl::PhotoActionsFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::albummanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::AlbumManagementFunctions)


def test_mydsl::albummanagementfunctions_constructor_exists():
    assert callable(myDsl::AlbumManagementFunctions.__init__)


def test_mydsl::albummanagementfunctions_constructor_args():
    sig = inspect.signature(myDsl::AlbumManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::albummanagementfunctions_has_name():
    assert hasattr(myDsl::AlbumManagementFunctions, "name")
    descriptor = None
    for klass in myDsl::AlbumManagementFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::segmentstructurecontent_is_not_abstract():
    assert not inspect.isabstract(myDsl::SegmentStructureContent)


def test_mydsl::segmentstructurecontent_constructor_exists():
    assert callable(myDsl::SegmentStructureContent.__init__)


def test_mydsl::segmentstructurecontent_constructor_args():
    sig = inspect.signature(myDsl::SegmentStructureContent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::segmentstructurecontent_has_name():
    assert hasattr(myDsl::SegmentStructureContent, "name")
    descriptor = None
    for klass in myDsl::SegmentStructureContent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::segmentstructure_is_not_abstract():
    assert not inspect.isabstract(myDsl::SegmentStructure)


def test_mydsl::segmentstructure_constructor_exists():
    assert callable(myDsl::SegmentStructure.__init__)


def test_mydsl::segmentstructure_constructor_args():
    sig = inspect.signature(myDsl::SegmentStructure.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datapersistencesegments_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataPersistenceSegments)


def test_mydsl::datapersistencesegments_constructor_exists():
    assert callable(myDsl::DataPersistenceSegments.__init__)


def test_mydsl::datapersistencesegments_constructor_args():
    sig = inspect.signature(myDsl::DataPersistenceSegments.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::datapersistencesegments_has_name():
    assert hasattr(myDsl::DataPersistenceSegments, "name")
    descriptor = None
    for klass in myDsl::DataPersistenceSegments.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::profilemanagementfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::ProfileManagementFunctions)


def test_mydsl::profilemanagementfunctions_constructor_exists():
    assert callable(myDsl::ProfileManagementFunctions.__init__)


def test_mydsl::profilemanagementfunctions_constructor_args():
    sig = inspect.signature(myDsl::ProfileManagementFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::profilemanagementfunctions_has_name():
    assert hasattr(myDsl::ProfileManagementFunctions, "name")
    descriptor = None
    for klass in myDsl::ProfileManagementFunctions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::landingactions_is_not_abstract():
    assert not inspect.isabstract(myDsl::LandingActions)


def test_mydsl::landingactions_constructor_exists():
    assert callable(myDsl::LandingActions.__init__)


def test_mydsl::landingactions_constructor_args():
    sig = inspect.signature(myDsl::LandingActions.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::photoactions_is_not_abstract():
    assert not inspect.isabstract(myDsl::PhotoActions)


def test_mydsl::photoactions_constructor_exists():
    assert callable(myDsl::PhotoActions.__init__)


def test_mydsl::photoactions_constructor_args():
    sig = inspect.signature(myDsl::PhotoActions.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::albummanagement_is_not_abstract():
    assert not inspect.isabstract(myDsl::AlbumManagement)


def test_mydsl::albummanagement_constructor_exists():
    assert callable(myDsl::AlbumManagement.__init__)


def test_mydsl::albummanagement_constructor_args():
    sig = inspect.signature(myDsl::AlbumManagement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::appaccess_is_not_abstract():
    assert not inspect.isabstract(myDsl::AppAccess)


def test_mydsl::appaccess_constructor_exists():
    assert callable(myDsl::AppAccess.__init__)


def test_mydsl::appaccess_constructor_args():
    sig = inspect.signature(myDsl::AppAccess.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::profilemanagement_is_not_abstract():
    assert not inspect.isabstract(myDsl::ProfileManagement)


def test_mydsl::profilemanagement_constructor_exists():
    assert callable(myDsl::ProfileManagement.__init__)


def test_mydsl::profilemanagement_constructor_args():
    sig = inspect.signature(myDsl::ProfileManagement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functionalities_is_not_abstract():
    assert not inspect.isabstract(myDsl::Functionalities)


def test_mydsl::functionalities_constructor_exists():
    assert callable(myDsl::Functionalities.__init__)


def test_mydsl::functionalities_constructor_args():
    sig = inspect.signature(myDsl::Functionalities.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functionality_is_not_abstract():
    assert not inspect.isabstract(myDsl::Functionality)


def test_mydsl::functionality_constructor_exists():
    assert callable(myDsl::Functionality.__init__)


def test_mydsl::functionality_constructor_args():
    sig = inspect.signature(myDsl::Functionality.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::userdomain_is_not_abstract():
    assert not inspect.isabstract(myDsl::UserDomain)


def test_mydsl::userdomain_constructor_exists():
    assert callable(myDsl::UserDomain.__init__)


def test_mydsl::userdomain_constructor_args():
    sig = inspect.signature(myDsl::UserDomain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::userdomain_has_name():
    assert hasattr(myDsl::UserDomain, "name")
    descriptor = None
    for klass in myDsl::UserDomain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::album_is_not_abstract():
    assert not inspect.isabstract(myDsl::Album)


def test_mydsl::album_constructor_exists():
    assert callable(myDsl::Album.__init__)


def test_mydsl::album_constructor_args():
    sig = inspect.signature(myDsl::Album.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::album_has_name():
    assert hasattr(myDsl::Album, "name")
    descriptor = None
    for klass in myDsl::Album.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::photo_is_not_abstract():
    assert not inspect.isabstract(myDsl::Photo)


def test_mydsl::photo_constructor_exists():
    assert callable(myDsl::Photo.__init__)


def test_mydsl::photo_constructor_args():
    sig = inspect.signature(myDsl::Photo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::photo_has_name():
    assert hasattr(myDsl::Photo, "name")
    descriptor = None
    for klass in myDsl::Photo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::entities_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entities)


def test_mydsl::entities_constructor_exists():
    assert callable(myDsl::Entities.__init__)


def test_mydsl::entities_constructor_args():
    sig = inspect.signature(myDsl::Entities.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::domain_is_not_abstract():
    assert not inspect.isabstract(myDsl::Domain)


def test_mydsl::domain_constructor_exists():
    assert callable(myDsl::Domain.__init__)


def test_mydsl::domain_constructor_args():
    sig = inspect.signature(myDsl::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::domain_has_name():
    assert hasattr(myDsl::Domain, "name")
    descriptor = None
    for klass in myDsl::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::appaccessfunctions_is_not_abstract():
    assert not inspect.isabstract(myDsl::AppAccessFunctions)


def test_mydsl::appaccessfunctions_constructor_exists():
    assert callable(myDsl::AppAccessFunctions.__init__)


def test_mydsl::appaccessfunctions_constructor_args():
    sig = inspect.signature(myDsl::AppAccessFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::appaccessfunctions_has_name():
    assert hasattr(myDsl::AppAccessFunctions, "name")
    descriptor = None
    for klass in myDsl::AppAccessFunctions.__mro__:
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
myDsl::AmazonWebServices_strategy = st.builds(
    myDsl::AmazonWebServices,
    name=
        safe_text
)
myDsl::PostgreSQL_strategy = st.builds(
    myDsl::PostgreSQL,
    name=
        safe_text
)
myDsl::Spring_strategy = st.builds(
    myDsl::Spring,
    name=
        safe_text
)
myDsl::ReactInformation_strategy = st.builds(
    myDsl::ReactInformation,
    name=
        safe_text
)
myDsl::ReactInfo_strategy = st.builds(
    myDsl::ReactInfo,
)
myDsl::ReactLibrary_strategy = st.builds(
    myDsl::ReactLibrary,
    name=
        safe_text
)
myDsl::ReactLibraries_strategy = st.builds(
    myDsl::ReactLibraries,
)
myDsl::ReactServicesType_strategy = st.builds(
    myDsl::ReactServicesType,
    name=
        safe_text
)
myDsl::ReactServicesRelation_strategy = st.builds(
    myDsl::ReactServicesRelation,
    name=
        safe_text
)
myDsl::ReactActionsContent_strategy = st.builds(
    myDsl::ReactActionsContent,
)
myDsl::ReactActions_strategy = st.builds(
    myDsl::ReactActions,
)
myDsl::ReactCoreFunctions_strategy = st.builds(
    myDsl::ReactCoreFunctions,
    name=
        safe_text
)
myDsl::Props_strategy = st.builds(
    myDsl::Props,
    name=
        safe_text,
    componentclass=
        safe_text
)
myDsl::CoreFunctionsDeclaration_strategy = st.builds(
    myDsl::CoreFunctionsDeclaration,
    name=
        safe_text
)
myDsl::State_strategy = st.builds(
    myDsl::State,
    componentclass=
        safe_text,
    name=
        safe_text
)
myDsl::ReactConstructor_strategy = st.builds(
    myDsl::ReactConstructor,
)
myDsl::UIContent_strategy = st.builds(
    myDsl::UIContent,
    name=
        safe_text
)
myDsl::ComponentClass_strategy = st.builds(
    myDsl::ComponentClass,
)
myDsl::LogicStructure_strategy = st.builds(
    myDsl::LogicStructure,
    name=
        safe_text
)
myDsl::LogicContent_strategy = st.builds(
    myDsl::LogicContent,
    name=
        safe_text
)
myDsl::ComponentsUI_strategy = st.builds(
    myDsl::ComponentsUI,
    name=
        safe_text
)
myDsl::ComponentsLogic_strategy = st.builds(
    myDsl::ComponentsLogic,
    name=
        safe_text
)
myDsl::ReactComponents_strategy = st.builds(
    myDsl::ReactComponents,
)
myDsl::DOMConfigurations_strategy = st.builds(
    myDsl::DOMConfigurations,
    elements=
        safe_text,
    name=
        safe_text
)
myDsl::PackageVersion_strategy = st.builds(
    myDsl::PackageVersion,
    name=
        safe_text
)
myDsl::PackageName_strategy = st.builds(
    myDsl::PackageName,
    name=
        safe_text
)
myDsl::ReactFunctions_strategy = st.builds(
    myDsl::ReactFunctions,
    lifecycleclass=
        safe_text,
    renderclass=
        safe_text
)
myDsl::ReactDependenciesSubRules_strategy = st.builds(
    myDsl::ReactDependenciesSubRules,
)
myDsl::ReactDependenciesRules_strategy = st.builds(
    myDsl::ReactDependenciesRules,
    name=
        safe_text
)
myDsl::ReactConfigurations_strategy = st.builds(
    myDsl::ReactConfigurations,
    name=
        safe_text
)
myDsl::ReactDependencies_strategy = st.builds(
    myDsl::ReactDependencies,
)
myDsl::ReactConfiguration_strategy = st.builds(
    myDsl::ReactConfiguration,
)
myDsl::ReactSubModules_strategy = st.builds(
    myDsl::ReactSubModules,
)
myDsl::ReactModules_strategy = st.builds(
    myDsl::ReactModules,
)
myDsl::React_strategy = st.builds(
    myDsl::React,
    name=
        safe_text
)
myDsl::Technologies_strategy = st.builds(
    myDsl::Technologies,
)
myDsl::Technology_strategy = st.builds(
    myDsl::Technology,
    name=
        safe_text
)
myDsl::NTiersRelations_strategy = st.builds(
    myDsl::NTiersRelations,
    name=
        safe_text
)
myDsl::NTierSource_strategy = st.builds(
    myDsl::NTierSource,
)
myDsl::NTierTarget_strategy = st.builds(
    myDsl::NTierTarget,
)
myDsl::SingleDependencies_strategy = st.builds(
    myDsl::SingleDependencies,
)
myDsl::NTiersConnections_strategy = st.builds(
    myDsl::NTiersConnections,
    name=
        safe_text,
    ntierconnection=
        safe_text
)
myDsl::PersistenceDataComponent_strategy = st.builds(
    myDsl::PersistenceDataComponent,
    name=
        safe_text
)
myDsl::BackEnd_strategy = st.builds(
    myDsl::BackEnd,
    name=
        safe_text
)
myDsl::FrontEnd_strategy = st.builds(
    myDsl::FrontEnd,
    name=
        safe_text
)
myDsl::ArchitectureComponents_strategy = st.builds(
    myDsl::ArchitectureComponents,
)
myDsl::LayerTarget_strategy = st.builds(
    myDsl::LayerTarget,
    layerelations=
        safe_text
)
myDsl::LayerSource_strategy = st.builds(
    myDsl::LayerSource,
    layerelations=
        safe_text
)
myDsl::LayerRelations_strategy = st.builds(
    myDsl::LayerRelations,
    layerelations=
        safe_text,
    name=
        safe_text
)
myDsl::SingleFile_strategy = st.builds(
    myDsl::SingleFile,
    name=
        safe_text
)
myDsl::MultipleFile_strategy = st.builds(
    myDsl::MultipleFile,
    name=
        safe_text
)
myDsl::Directories_strategy = st.builds(
    myDsl::Directories,
)
myDsl::DirectoryContent_strategy = st.builds(
    myDsl::DirectoryContent,
    name=
        safe_text
)
myDsl::DataPersistenceContent_strategy = st.builds(
    myDsl::DataPersistenceContent,
)
myDsl::DataPersistenceLayer_strategy = st.builds(
    myDsl::DataPersistenceLayer,
)
myDsl::BusinessLogicSegments_strategy = st.builds(
    myDsl::BusinessLogicSegments,
    name=
        safe_text
)
myDsl::BusinessLogicContent_strategy = st.builds(
    myDsl::BusinessLogicContent,
)
myDsl::BusinessLogicLayer_strategy = st.builds(
    myDsl::BusinessLogicLayer,
)
myDsl::PresentationSegments_strategy = st.builds(
    myDsl::PresentationSegments,
    name=
        safe_text
)
myDsl::PresentationContent_strategy = st.builds(
    myDsl::PresentationContent,
)
myDsl::PresentationLayer_strategy = st.builds(
    myDsl::PresentationLayer,
)
myDsl::Layer_strategy = st.builds(
    myDsl::Layer,
)
myDsl::NTiers_strategy = st.builds(
    myDsl::NTiers,
)
myDsl::Architecture_strategy = st.builds(
    myDsl::Architecture,
)
myDsl::DomainRelations_strategy = st.builds(
    myDsl::DomainRelations,
    name=
        safe_text
)
myDsl::DomainConnection_strategy = st.builds(
    myDsl::DomainConnection,
)
myDsl::LandingFunctions_strategy = st.builds(
    myDsl::LandingFunctions,
    name=
        safe_text
)
myDsl::PhotoActionsFunctions_strategy = st.builds(
    myDsl::PhotoActionsFunctions,
    name=
        safe_text
)
myDsl::AlbumManagementFunctions_strategy = st.builds(
    myDsl::AlbumManagementFunctions,
    name=
        safe_text
)
myDsl::SegmentStructureContent_strategy = st.builds(
    myDsl::SegmentStructureContent,
    name=
        safe_text
)
myDsl::SegmentStructure_strategy = st.builds(
    myDsl::SegmentStructure,
)
myDsl::DataPersistenceSegments_strategy = st.builds(
    myDsl::DataPersistenceSegments,
    name=
        safe_text
)
myDsl::ProfileManagementFunctions_strategy = st.builds(
    myDsl::ProfileManagementFunctions,
    name=
        safe_text
)
myDsl::LandingActions_strategy = st.builds(
    myDsl::LandingActions,
)
myDsl::PhotoActions_strategy = st.builds(
    myDsl::PhotoActions,
)
myDsl::AlbumManagement_strategy = st.builds(
    myDsl::AlbumManagement,
)
myDsl::AppAccess_strategy = st.builds(
    myDsl::AppAccess,
)
myDsl::ProfileManagement_strategy = st.builds(
    myDsl::ProfileManagement,
)
myDsl::Functionalities_strategy = st.builds(
    myDsl::Functionalities,
)
myDsl::Functionality_strategy = st.builds(
    myDsl::Functionality,
)
myDsl::UserDomain_strategy = st.builds(
    myDsl::UserDomain,
    name=
        safe_text
)
myDsl::Album_strategy = st.builds(
    myDsl::Album,
    name=
        safe_text
)
myDsl::Photo_strategy = st.builds(
    myDsl::Photo,
    name=
        safe_text
)
myDsl::Entities_strategy = st.builds(
    myDsl::Entities,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
myDsl::Domain_strategy = st.builds(
    myDsl::Domain,
    name=
        safe_text
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)
myDsl::AppAccessFunctions_strategy = st.builds(
    myDsl::AppAccessFunctions,
    name=
        safe_text
)

@given(instance=myDsl::AmazonWebServices_strategy)
@settings(max_examples=50)
def test_mydsl::amazonwebservices_instantiation(instance):
    assert isinstance(instance, myDsl::AmazonWebServices)

@given(instance=myDsl::AmazonWebServices_strategy)
def test_mydsl::amazonwebservices_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AmazonWebServices_strategy)
def test_mydsl::amazonwebservices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::PostgreSQL_strategy)
@settings(max_examples=50)
def test_mydsl::postgresql_instantiation(instance):
    assert isinstance(instance, myDsl::PostgreSQL)

@given(instance=myDsl::PostgreSQL_strategy)
def test_mydsl::postgresql_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PostgreSQL_strategy)
def test_mydsl::postgresql_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Spring_strategy)
@settings(max_examples=50)
def test_mydsl::spring_instantiation(instance):
    assert isinstance(instance, myDsl::Spring)

@given(instance=myDsl::Spring_strategy)
def test_mydsl::spring_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Spring_strategy)
def test_mydsl::spring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactInformation_strategy)
@settings(max_examples=50)
def test_mydsl::reactinformation_instantiation(instance):
    assert isinstance(instance, myDsl::ReactInformation)

@given(instance=myDsl::ReactInformation_strategy)
def test_mydsl::reactinformation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactInformation_strategy)
def test_mydsl::reactinformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactInfo_strategy)
@settings(max_examples=50)
def test_mydsl::reactinfo_instantiation(instance):
    assert isinstance(instance, myDsl::ReactInfo)

@given(instance=myDsl::ReactLibrary_strategy)
@settings(max_examples=50)
def test_mydsl::reactlibrary_instantiation(instance):
    assert isinstance(instance, myDsl::ReactLibrary)

@given(instance=myDsl::ReactLibrary_strategy)
def test_mydsl::reactlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactLibrary_strategy)
def test_mydsl::reactlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactLibraries_strategy)
@settings(max_examples=50)
def test_mydsl::reactlibraries_instantiation(instance):
    assert isinstance(instance, myDsl::ReactLibraries)

@given(instance=myDsl::ReactServicesType_strategy)
@settings(max_examples=50)
def test_mydsl::reactservicestype_instantiation(instance):
    assert isinstance(instance, myDsl::ReactServicesType)

@given(instance=myDsl::ReactServicesType_strategy)
def test_mydsl::reactservicestype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactServicesType_strategy)
def test_mydsl::reactservicestype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactServicesRelation_strategy)
@settings(max_examples=50)
def test_mydsl::reactservicesrelation_instantiation(instance):
    assert isinstance(instance, myDsl::ReactServicesRelation)

@given(instance=myDsl::ReactServicesRelation_strategy)
def test_mydsl::reactservicesrelation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactServicesRelation_strategy)
def test_mydsl::reactservicesrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactActionsContent_strategy)
@settings(max_examples=50)
def test_mydsl::reactactionscontent_instantiation(instance):
    assert isinstance(instance, myDsl::ReactActionsContent)

@given(instance=myDsl::ReactActions_strategy)
@settings(max_examples=50)
def test_mydsl::reactactions_instantiation(instance):
    assert isinstance(instance, myDsl::ReactActions)

@given(instance=myDsl::ReactCoreFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::reactcorefunctions_instantiation(instance):
    assert isinstance(instance, myDsl::ReactCoreFunctions)

@given(instance=myDsl::ReactCoreFunctions_strategy)
def test_mydsl::reactcorefunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactCoreFunctions_strategy)
def test_mydsl::reactcorefunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Props_strategy)
@settings(max_examples=50)
def test_mydsl::props_instantiation(instance):
    assert isinstance(instance, myDsl::Props)

@given(instance=myDsl::Props_strategy)
def test_mydsl::props_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Props_strategy)
def test_mydsl::props_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Props_strategy)
def test_mydsl::props_componentclass_type(instance):
    assert isinstance(instance.componentclass, str)


@given(instance=myDsl::Props_strategy)
def test_mydsl::props_componentclass_setter(instance):
    original = instance.componentclass
    instance.componentclass = original
    assert instance.componentclass == original

@given(instance=myDsl::CoreFunctionsDeclaration_strategy)
@settings(max_examples=50)
def test_mydsl::corefunctionsdeclaration_instantiation(instance):
    assert isinstance(instance, myDsl::CoreFunctionsDeclaration)

@given(instance=myDsl::CoreFunctionsDeclaration_strategy)
def test_mydsl::corefunctionsdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::CoreFunctionsDeclaration_strategy)
def test_mydsl::corefunctionsdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::State_strategy)
@settings(max_examples=50)
def test_mydsl::state_instantiation(instance):
    assert isinstance(instance, myDsl::State)

@given(instance=myDsl::State_strategy)
def test_mydsl::state_componentclass_type(instance):
    assert isinstance(instance.componentclass, str)


@given(instance=myDsl::State_strategy)
def test_mydsl::state_componentclass_setter(instance):
    original = instance.componentclass
    instance.componentclass = original
    assert instance.componentclass == original

@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactConstructor_strategy)
@settings(max_examples=50)
def test_mydsl::reactconstructor_instantiation(instance):
    assert isinstance(instance, myDsl::ReactConstructor)

@given(instance=myDsl::UIContent_strategy)
@settings(max_examples=50)
def test_mydsl::uicontent_instantiation(instance):
    assert isinstance(instance, myDsl::UIContent)

@given(instance=myDsl::UIContent_strategy)
def test_mydsl::uicontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::UIContent_strategy)
def test_mydsl::uicontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ComponentClass_strategy)
@settings(max_examples=50)
def test_mydsl::componentclass_instantiation(instance):
    assert isinstance(instance, myDsl::ComponentClass)

@given(instance=myDsl::LogicStructure_strategy)
@settings(max_examples=50)
def test_mydsl::logicstructure_instantiation(instance):
    assert isinstance(instance, myDsl::LogicStructure)

@given(instance=myDsl::LogicStructure_strategy)
def test_mydsl::logicstructure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::LogicStructure_strategy)
def test_mydsl::logicstructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::LogicContent_strategy)
@settings(max_examples=50)
def test_mydsl::logiccontent_instantiation(instance):
    assert isinstance(instance, myDsl::LogicContent)

@given(instance=myDsl::LogicContent_strategy)
def test_mydsl::logiccontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::LogicContent_strategy)
def test_mydsl::logiccontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ComponentsUI_strategy)
@settings(max_examples=50)
def test_mydsl::componentsui_instantiation(instance):
    assert isinstance(instance, myDsl::ComponentsUI)

@given(instance=myDsl::ComponentsUI_strategy)
def test_mydsl::componentsui_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ComponentsUI_strategy)
def test_mydsl::componentsui_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ComponentsLogic_strategy)
@settings(max_examples=50)
def test_mydsl::componentslogic_instantiation(instance):
    assert isinstance(instance, myDsl::ComponentsLogic)

@given(instance=myDsl::ComponentsLogic_strategy)
def test_mydsl::componentslogic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ComponentsLogic_strategy)
def test_mydsl::componentslogic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactComponents_strategy)
@settings(max_examples=50)
def test_mydsl::reactcomponents_instantiation(instance):
    assert isinstance(instance, myDsl::ReactComponents)

@given(instance=myDsl::DOMConfigurations_strategy)
@settings(max_examples=50)
def test_mydsl::domconfigurations_instantiation(instance):
    assert isinstance(instance, myDsl::DOMConfigurations)

@given(instance=myDsl::DOMConfigurations_strategy)
def test_mydsl::domconfigurations_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=myDsl::DOMConfigurations_strategy)
def test_mydsl::domconfigurations_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=myDsl::DOMConfigurations_strategy)
def test_mydsl::domconfigurations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::DOMConfigurations_strategy)
def test_mydsl::domconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::PackageVersion_strategy)
@settings(max_examples=50)
def test_mydsl::packageversion_instantiation(instance):
    assert isinstance(instance, myDsl::PackageVersion)

@given(instance=myDsl::PackageVersion_strategy)
def test_mydsl::packageversion_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PackageVersion_strategy)
def test_mydsl::packageversion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::PackageName_strategy)
@settings(max_examples=50)
def test_mydsl::packagename_instantiation(instance):
    assert isinstance(instance, myDsl::PackageName)

@given(instance=myDsl::PackageName_strategy)
def test_mydsl::packagename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PackageName_strategy)
def test_mydsl::packagename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::reactfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::ReactFunctions)

@given(instance=myDsl::ReactFunctions_strategy)
def test_mydsl::reactfunctions_lifecycleclass_type(instance):
    assert isinstance(instance.lifecycleclass, str)


@given(instance=myDsl::ReactFunctions_strategy)
def test_mydsl::reactfunctions_lifecycleclass_setter(instance):
    original = instance.lifecycleclass
    instance.lifecycleclass = original
    assert instance.lifecycleclass == original

@given(instance=myDsl::ReactFunctions_strategy)
def test_mydsl::reactfunctions_renderclass_type(instance):
    assert isinstance(instance.renderclass, str)


@given(instance=myDsl::ReactFunctions_strategy)
def test_mydsl::reactfunctions_renderclass_setter(instance):
    original = instance.renderclass
    instance.renderclass = original
    assert instance.renderclass == original

@given(instance=myDsl::ReactDependenciesSubRules_strategy)
@settings(max_examples=50)
def test_mydsl::reactdependenciessubrules_instantiation(instance):
    assert isinstance(instance, myDsl::ReactDependenciesSubRules)

@given(instance=myDsl::ReactDependenciesRules_strategy)
@settings(max_examples=50)
def test_mydsl::reactdependenciesrules_instantiation(instance):
    assert isinstance(instance, myDsl::ReactDependenciesRules)

@given(instance=myDsl::ReactDependenciesRules_strategy)
def test_mydsl::reactdependenciesrules_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactDependenciesRules_strategy)
def test_mydsl::reactdependenciesrules_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactConfigurations_strategy)
@settings(max_examples=50)
def test_mydsl::reactconfigurations_instantiation(instance):
    assert isinstance(instance, myDsl::ReactConfigurations)

@given(instance=myDsl::ReactConfigurations_strategy)
def test_mydsl::reactconfigurations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ReactConfigurations_strategy)
def test_mydsl::reactconfigurations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactDependencies_strategy)
@settings(max_examples=50)
def test_mydsl::reactdependencies_instantiation(instance):
    assert isinstance(instance, myDsl::ReactDependencies)

@given(instance=myDsl::ReactConfiguration_strategy)
@settings(max_examples=50)
def test_mydsl::reactconfiguration_instantiation(instance):
    assert isinstance(instance, myDsl::ReactConfiguration)

@given(instance=myDsl::ReactSubModules_strategy)
@settings(max_examples=50)
def test_mydsl::reactsubmodules_instantiation(instance):
    assert isinstance(instance, myDsl::ReactSubModules)

@given(instance=myDsl::ReactModules_strategy)
@settings(max_examples=50)
def test_mydsl::reactmodules_instantiation(instance):
    assert isinstance(instance, myDsl::ReactModules)

@given(instance=myDsl::React_strategy)
@settings(max_examples=50)
def test_mydsl::react_instantiation(instance):
    assert isinstance(instance, myDsl::React)

@given(instance=myDsl::React_strategy)
def test_mydsl::react_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::React_strategy)
def test_mydsl::react_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Technologies_strategy)
@settings(max_examples=50)
def test_mydsl::technologies_instantiation(instance):
    assert isinstance(instance, myDsl::Technologies)

@given(instance=myDsl::Technology_strategy)
@settings(max_examples=50)
def test_mydsl::technology_instantiation(instance):
    assert isinstance(instance, myDsl::Technology)

@given(instance=myDsl::Technology_strategy)
def test_mydsl::technology_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Technology_strategy)
def test_mydsl::technology_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::NTiersRelations_strategy)
@settings(max_examples=50)
def test_mydsl::ntiersrelations_instantiation(instance):
    assert isinstance(instance, myDsl::NTiersRelations)

@given(instance=myDsl::NTiersRelations_strategy)
def test_mydsl::ntiersrelations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::NTiersRelations_strategy)
def test_mydsl::ntiersrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::NTierSource_strategy)
@settings(max_examples=50)
def test_mydsl::ntiersource_instantiation(instance):
    assert isinstance(instance, myDsl::NTierSource)

@given(instance=myDsl::NTierTarget_strategy)
@settings(max_examples=50)
def test_mydsl::ntiertarget_instantiation(instance):
    assert isinstance(instance, myDsl::NTierTarget)

@given(instance=myDsl::SingleDependencies_strategy)
@settings(max_examples=50)
def test_mydsl::singledependencies_instantiation(instance):
    assert isinstance(instance, myDsl::SingleDependencies)

@given(instance=myDsl::NTiersConnections_strategy)
@settings(max_examples=50)
def test_mydsl::ntiersconnections_instantiation(instance):
    assert isinstance(instance, myDsl::NTiersConnections)

@given(instance=myDsl::NTiersConnections_strategy)
def test_mydsl::ntiersconnections_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::NTiersConnections_strategy)
def test_mydsl::ntiersconnections_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::NTiersConnections_strategy)
def test_mydsl::ntiersconnections_ntierconnection_type(instance):
    assert isinstance(instance.ntierconnection, str)


@given(instance=myDsl::NTiersConnections_strategy)
def test_mydsl::ntiersconnections_ntierconnection_setter(instance):
    original = instance.ntierconnection
    instance.ntierconnection = original
    assert instance.ntierconnection == original

@given(instance=myDsl::PersistenceDataComponent_strategy)
@settings(max_examples=50)
def test_mydsl::persistencedatacomponent_instantiation(instance):
    assert isinstance(instance, myDsl::PersistenceDataComponent)

@given(instance=myDsl::PersistenceDataComponent_strategy)
def test_mydsl::persistencedatacomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PersistenceDataComponent_strategy)
def test_mydsl::persistencedatacomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::BackEnd_strategy)
@settings(max_examples=50)
def test_mydsl::backend_instantiation(instance):
    assert isinstance(instance, myDsl::BackEnd)

@given(instance=myDsl::BackEnd_strategy)
def test_mydsl::backend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::BackEnd_strategy)
def test_mydsl::backend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::FrontEnd_strategy)
@settings(max_examples=50)
def test_mydsl::frontend_instantiation(instance):
    assert isinstance(instance, myDsl::FrontEnd)

@given(instance=myDsl::FrontEnd_strategy)
def test_mydsl::frontend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::FrontEnd_strategy)
def test_mydsl::frontend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ArchitectureComponents_strategy)
@settings(max_examples=50)
def test_mydsl::architecturecomponents_instantiation(instance):
    assert isinstance(instance, myDsl::ArchitectureComponents)

@given(instance=myDsl::LayerTarget_strategy)
@settings(max_examples=50)
def test_mydsl::layertarget_instantiation(instance):
    assert isinstance(instance, myDsl::LayerTarget)

@given(instance=myDsl::LayerTarget_strategy)
def test_mydsl::layertarget_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=myDsl::LayerTarget_strategy)
def test_mydsl::layertarget_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=myDsl::LayerSource_strategy)
@settings(max_examples=50)
def test_mydsl::layersource_instantiation(instance):
    assert isinstance(instance, myDsl::LayerSource)

@given(instance=myDsl::LayerSource_strategy)
def test_mydsl::layersource_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=myDsl::LayerSource_strategy)
def test_mydsl::layersource_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=myDsl::LayerRelations_strategy)
@settings(max_examples=50)
def test_mydsl::layerrelations_instantiation(instance):
    assert isinstance(instance, myDsl::LayerRelations)

@given(instance=myDsl::LayerRelations_strategy)
def test_mydsl::layerrelations_layerelations_type(instance):
    assert isinstance(instance.layerelations, str)


@given(instance=myDsl::LayerRelations_strategy)
def test_mydsl::layerrelations_layerelations_setter(instance):
    original = instance.layerelations
    instance.layerelations = original
    assert instance.layerelations == original

@given(instance=myDsl::LayerRelations_strategy)
def test_mydsl::layerrelations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::LayerRelations_strategy)
def test_mydsl::layerrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::SingleFile_strategy)
@settings(max_examples=50)
def test_mydsl::singlefile_instantiation(instance):
    assert isinstance(instance, myDsl::SingleFile)

@given(instance=myDsl::SingleFile_strategy)
def test_mydsl::singlefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::SingleFile_strategy)
def test_mydsl::singlefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::MultipleFile_strategy)
@settings(max_examples=50)
def test_mydsl::multiplefile_instantiation(instance):
    assert isinstance(instance, myDsl::MultipleFile)

@given(instance=myDsl::MultipleFile_strategy)
def test_mydsl::multiplefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::MultipleFile_strategy)
def test_mydsl::multiplefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Directories_strategy)
@settings(max_examples=50)
def test_mydsl::directories_instantiation(instance):
    assert isinstance(instance, myDsl::Directories)

@given(instance=myDsl::DirectoryContent_strategy)
@settings(max_examples=50)
def test_mydsl::directorycontent_instantiation(instance):
    assert isinstance(instance, myDsl::DirectoryContent)

@given(instance=myDsl::DirectoryContent_strategy)
def test_mydsl::directorycontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::DirectoryContent_strategy)
def test_mydsl::directorycontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DataPersistenceContent_strategy)
@settings(max_examples=50)
def test_mydsl::datapersistencecontent_instantiation(instance):
    assert isinstance(instance, myDsl::DataPersistenceContent)

@given(instance=myDsl::DataPersistenceLayer_strategy)
@settings(max_examples=50)
def test_mydsl::datapersistencelayer_instantiation(instance):
    assert isinstance(instance, myDsl::DataPersistenceLayer)

@given(instance=myDsl::BusinessLogicSegments_strategy)
@settings(max_examples=50)
def test_mydsl::businesslogicsegments_instantiation(instance):
    assert isinstance(instance, myDsl::BusinessLogicSegments)

@given(instance=myDsl::BusinessLogicSegments_strategy)
def test_mydsl::businesslogicsegments_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::BusinessLogicSegments_strategy)
def test_mydsl::businesslogicsegments_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::BusinessLogicContent_strategy)
@settings(max_examples=50)
def test_mydsl::businesslogiccontent_instantiation(instance):
    assert isinstance(instance, myDsl::BusinessLogicContent)

@given(instance=myDsl::BusinessLogicLayer_strategy)
@settings(max_examples=50)
def test_mydsl::businesslogiclayer_instantiation(instance):
    assert isinstance(instance, myDsl::BusinessLogicLayer)

@given(instance=myDsl::PresentationSegments_strategy)
@settings(max_examples=50)
def test_mydsl::presentationsegments_instantiation(instance):
    assert isinstance(instance, myDsl::PresentationSegments)

@given(instance=myDsl::PresentationSegments_strategy)
def test_mydsl::presentationsegments_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PresentationSegments_strategy)
def test_mydsl::presentationsegments_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::PresentationContent_strategy)
@settings(max_examples=50)
def test_mydsl::presentationcontent_instantiation(instance):
    assert isinstance(instance, myDsl::PresentationContent)

@given(instance=myDsl::PresentationLayer_strategy)
@settings(max_examples=50)
def test_mydsl::presentationlayer_instantiation(instance):
    assert isinstance(instance, myDsl::PresentationLayer)

@given(instance=myDsl::Layer_strategy)
@settings(max_examples=50)
def test_mydsl::layer_instantiation(instance):
    assert isinstance(instance, myDsl::Layer)

@given(instance=myDsl::NTiers_strategy)
@settings(max_examples=50)
def test_mydsl::ntiers_instantiation(instance):
    assert isinstance(instance, myDsl::NTiers)

@given(instance=myDsl::Architecture_strategy)
@settings(max_examples=50)
def test_mydsl::architecture_instantiation(instance):
    assert isinstance(instance, myDsl::Architecture)

@given(instance=myDsl::DomainRelations_strategy)
@settings(max_examples=50)
def test_mydsl::domainrelations_instantiation(instance):
    assert isinstance(instance, myDsl::DomainRelations)

@given(instance=myDsl::DomainRelations_strategy)
def test_mydsl::domainrelations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::DomainRelations_strategy)
def test_mydsl::domainrelations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DomainConnection_strategy)
@settings(max_examples=50)
def test_mydsl::domainconnection_instantiation(instance):
    assert isinstance(instance, myDsl::DomainConnection)

@given(instance=myDsl::LandingFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::landingfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::LandingFunctions)

@given(instance=myDsl::LandingFunctions_strategy)
def test_mydsl::landingfunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::LandingFunctions_strategy)
def test_mydsl::landingfunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::PhotoActionsFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::photoactionsfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::PhotoActionsFunctions)

@given(instance=myDsl::PhotoActionsFunctions_strategy)
def test_mydsl::photoactionsfunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::PhotoActionsFunctions_strategy)
def test_mydsl::photoactionsfunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::AlbumManagementFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::albummanagementfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::AlbumManagementFunctions)

@given(instance=myDsl::AlbumManagementFunctions_strategy)
def test_mydsl::albummanagementfunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AlbumManagementFunctions_strategy)
def test_mydsl::albummanagementfunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::SegmentStructureContent_strategy)
@settings(max_examples=50)
def test_mydsl::segmentstructurecontent_instantiation(instance):
    assert isinstance(instance, myDsl::SegmentStructureContent)

@given(instance=myDsl::SegmentStructureContent_strategy)
def test_mydsl::segmentstructurecontent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::SegmentStructureContent_strategy)
def test_mydsl::segmentstructurecontent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::SegmentStructure_strategy)
@settings(max_examples=50)
def test_mydsl::segmentstructure_instantiation(instance):
    assert isinstance(instance, myDsl::SegmentStructure)

@given(instance=myDsl::DataPersistenceSegments_strategy)
@settings(max_examples=50)
def test_mydsl::datapersistencesegments_instantiation(instance):
    assert isinstance(instance, myDsl::DataPersistenceSegments)

@given(instance=myDsl::DataPersistenceSegments_strategy)
def test_mydsl::datapersistencesegments_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::DataPersistenceSegments_strategy)
def test_mydsl::datapersistencesegments_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ProfileManagementFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::profilemanagementfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::ProfileManagementFunctions)

@given(instance=myDsl::ProfileManagementFunctions_strategy)
def test_mydsl::profilemanagementfunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ProfileManagementFunctions_strategy)
def test_mydsl::profilemanagementfunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::LandingActions_strategy)
@settings(max_examples=50)
def test_mydsl::landingactions_instantiation(instance):
    assert isinstance(instance, myDsl::LandingActions)

@given(instance=myDsl::PhotoActions_strategy)
@settings(max_examples=50)
def test_mydsl::photoactions_instantiation(instance):
    assert isinstance(instance, myDsl::PhotoActions)

@given(instance=myDsl::AlbumManagement_strategy)
@settings(max_examples=50)
def test_mydsl::albummanagement_instantiation(instance):
    assert isinstance(instance, myDsl::AlbumManagement)

@given(instance=myDsl::AppAccess_strategy)
@settings(max_examples=50)
def test_mydsl::appaccess_instantiation(instance):
    assert isinstance(instance, myDsl::AppAccess)

@given(instance=myDsl::ProfileManagement_strategy)
@settings(max_examples=50)
def test_mydsl::profilemanagement_instantiation(instance):
    assert isinstance(instance, myDsl::ProfileManagement)

@given(instance=myDsl::Functionalities_strategy)
@settings(max_examples=50)
def test_mydsl::functionalities_instantiation(instance):
    assert isinstance(instance, myDsl::Functionalities)

@given(instance=myDsl::Functionality_strategy)
@settings(max_examples=50)
def test_mydsl::functionality_instantiation(instance):
    assert isinstance(instance, myDsl::Functionality)

@given(instance=myDsl::UserDomain_strategy)
@settings(max_examples=50)
def test_mydsl::userdomain_instantiation(instance):
    assert isinstance(instance, myDsl::UserDomain)

@given(instance=myDsl::UserDomain_strategy)
def test_mydsl::userdomain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::UserDomain_strategy)
def test_mydsl::userdomain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Album_strategy)
@settings(max_examples=50)
def test_mydsl::album_instantiation(instance):
    assert isinstance(instance, myDsl::Album)

@given(instance=myDsl::Album_strategy)
def test_mydsl::album_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Album_strategy)
def test_mydsl::album_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Photo_strategy)
@settings(max_examples=50)
def test_mydsl::photo_instantiation(instance):
    assert isinstance(instance, myDsl::Photo)

@given(instance=myDsl::Photo_strategy)
def test_mydsl::photo_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Photo_strategy)
def test_mydsl::photo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Entities_strategy)
@settings(max_examples=50)
def test_mydsl::entities_instantiation(instance):
    assert isinstance(instance, myDsl::Entities)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::Domain_strategy)
@settings(max_examples=50)
def test_mydsl::domain_instantiation(instance):
    assert isinstance(instance, myDsl::Domain)

@given(instance=myDsl::Domain_strategy)
def test_mydsl::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Domain_strategy)
def test_mydsl::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

@given(instance=myDsl::AppAccessFunctions_strategy)
@settings(max_examples=50)
def test_mydsl::appaccessfunctions_instantiation(instance):
    assert isinstance(instance, myDsl::AppAccessFunctions)

@given(instance=myDsl::AppAccessFunctions_strategy)
def test_mydsl::appaccessfunctions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AppAccessFunctions_strategy)
def test_mydsl::appaccessfunctions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
