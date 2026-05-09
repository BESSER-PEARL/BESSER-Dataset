import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JavaUserDefinedType,
    PSM::JavaInterfaceType,
    PSM::JavaClassType,
    JavaDataField,
    PSM::JavaMethodParameter,
    SpringWebApplicationLayer,
    PSM::SpringBootApplicationLayer,
    JavaDataType,
    PSM::JavaUserDefinedType,
    JavaElement,
    PSM::JavaDataField,
    PSM::JavaMethod,
    PSM::JavaDataType,
    PSM::SpringModelPojoLayer,
    PSM::SpringDomainLayer,
    PSM::SpringRepositoryLayer,
    PSM::SpringComponentLayer,
    PSM::SpringFeignClientLayer,
    PSM::SpringConfigurationLayer,
    PSM::SpringServiceLayer,
    PSM::SpringControllerLayer,
    ArtifactElement,
    PSM::JavaAnnotation,
    PSM::JavaElement,
    PSM::JavaAnnotationParameter,
    JavaSpringWebApplicationProject,
    PSM::JavaSpringMVCApplicationProject,
    PSM::JavaSpringWebFluxApplicationProject,
    PSM::SpringWebApplicationLayer,
    PSM::ConfigurationProperty,
    MicroserviceProject,
    PSM::JavaSpringWebApplicationProject,
    PSM::DependencyLibrary,
    PSM::MicroserviceProject,
    PSM::DockerContainerPort,
    PSM::DockerContainerLink,
    PSM::ApplicationProject,
    PSM::DockerContainerDefinition,
    PSM::DistributedApplicationProject,
    PSM::RootPSM,
    PSM::ArtifactElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javauserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(JavaUserDefinedType)


def test_javauserdefinedtype_constructor_exists():
    assert callable(JavaUserDefinedType.__init__)


def test_javauserdefinedtype_constructor_args():
    sig = inspect.signature(JavaUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_psm::javainterfacetype_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaInterfaceType)


def test_psm::javainterfacetype_constructor_exists():
    assert callable(PSM::JavaInterfaceType.__init__)


def test_psm::javainterfacetype_constructor_args():
    sig = inspect.signature(PSM::JavaInterfaceType.__init__)
    params = list(sig.parameters.keys())



def test_psm::javaclasstype_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaClassType)


def test_psm::javaclasstype_constructor_exists():
    assert callable(PSM::JavaClassType.__init__)


def test_psm::javaclasstype_constructor_args():
    sig = inspect.signature(PSM::JavaClassType.__init__)
    params = list(sig.parameters.keys())



def test_javadatafield_is_not_abstract():
    assert not inspect.isabstract(JavaDataField)


def test_javadatafield_constructor_exists():
    assert callable(JavaDataField.__init__)


def test_javadatafield_constructor_args():
    sig = inspect.signature(JavaDataField.__init__)
    params = list(sig.parameters.keys())



def test_psm::javamethodparameter_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaMethodParameter)


def test_psm::javamethodparameter_constructor_exists():
    assert callable(PSM::JavaMethodParameter.__init__)


def test_psm::javamethodparameter_constructor_args():
    sig = inspect.signature(PSM::JavaMethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterOrder" in params, "Missing parameter 'ParameterOrder'"

def test_psm::javamethodparameter_has_ParameterOrder():
    assert hasattr(PSM::JavaMethodParameter, "ParameterOrder")
    descriptor = None
    for klass in PSM::JavaMethodParameter.__mro__:
        if "ParameterOrder" in klass.__dict__:
            descriptor = klass.__dict__["ParameterOrder"]
            break
    assert isinstance(descriptor, property)



def test_springwebapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(SpringWebApplicationLayer)


def test_springwebapplicationlayer_constructor_exists():
    assert callable(SpringWebApplicationLayer.__init__)


def test_springwebapplicationlayer_constructor_args():
    sig = inspect.signature(SpringWebApplicationLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springbootapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringBootApplicationLayer)


def test_psm::springbootapplicationlayer_constructor_exists():
    assert callable(PSM::SpringBootApplicationLayer.__init__)


def test_psm::springbootapplicationlayer_constructor_args():
    sig = inspect.signature(PSM::SpringBootApplicationLayer.__init__)
    params = list(sig.parameters.keys())



def test_javadatatype_is_not_abstract():
    assert not inspect.isabstract(JavaDataType)


def test_javadatatype_constructor_exists():
    assert callable(JavaDataType.__init__)


def test_javadatatype_constructor_args():
    sig = inspect.signature(JavaDataType.__init__)
    params = list(sig.parameters.keys())



def test_psm::javauserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaUserDefinedType)


def test_psm::javauserdefinedtype_constructor_exists():
    assert callable(PSM::JavaUserDefinedType.__init__)


def test_psm::javauserdefinedtype_constructor_args():
    sig = inspect.signature(PSM::JavaUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_javaelement_is_not_abstract():
    assert not inspect.isabstract(JavaElement)


def test_javaelement_constructor_exists():
    assert callable(JavaElement.__init__)


def test_javaelement_constructor_args():
    sig = inspect.signature(JavaElement.__init__)
    params = list(sig.parameters.keys())



def test_psm::javadatafield_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaDataField)


def test_psm::javadatafield_constructor_exists():
    assert callable(PSM::JavaDataField.__init__)


def test_psm::javadatafield_constructor_args():
    sig = inspect.signature(PSM::JavaDataField.__init__)
    params = list(sig.parameters.keys())
    assert "FieldValue" in params, "Missing parameter 'FieldValue'"

def test_psm::javadatafield_has_FieldValue():
    assert hasattr(PSM::JavaDataField, "FieldValue")
    descriptor = None
    for klass in PSM::JavaDataField.__mro__:
        if "FieldValue" in klass.__dict__:
            descriptor = klass.__dict__["FieldValue"]
            break
    assert isinstance(descriptor, property)



def test_psm::javamethod_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaMethod)


def test_psm::javamethod_constructor_exists():
    assert callable(PSM::JavaMethod.__init__)


def test_psm::javamethod_constructor_args():
    sig = inspect.signature(PSM::JavaMethod.__init__)
    params = list(sig.parameters.keys())
    assert "RootCallingMethod" in params, "Missing parameter 'RootCallingMethod'"

def test_psm::javamethod_has_RootCallingMethod():
    assert hasattr(PSM::JavaMethod, "RootCallingMethod")
    descriptor = None
    for klass in PSM::JavaMethod.__mro__:
        if "RootCallingMethod" in klass.__dict__:
            descriptor = klass.__dict__["RootCallingMethod"]
            break
    assert isinstance(descriptor, property)



def test_psm::javadatatype_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaDataType)


def test_psm::javadatatype_constructor_exists():
    assert callable(PSM::JavaDataType.__init__)


def test_psm::javadatatype_constructor_args():
    sig = inspect.signature(PSM::JavaDataType.__init__)
    params = list(sig.parameters.keys())
    assert "IsPrimitive" in params, "Missing parameter 'IsPrimitive'"
    assert "PackageName" in params, "Missing parameter 'PackageName'"
    assert "JsonSchema" in params, "Missing parameter 'JsonSchema'"

def test_psm::javadatatype_has_IsPrimitive():
    assert hasattr(PSM::JavaDataType, "IsPrimitive")
    descriptor = None
    for klass in PSM::JavaDataType.__mro__:
        if "IsPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["IsPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_psm::javadatatype_has_PackageName():
    assert hasattr(PSM::JavaDataType, "PackageName")
    descriptor = None
    for klass in PSM::JavaDataType.__mro__:
        if "PackageName" in klass.__dict__:
            descriptor = klass.__dict__["PackageName"]
            break
    assert isinstance(descriptor, property)

def test_psm::javadatatype_has_JsonSchema():
    assert hasattr(PSM::JavaDataType, "JsonSchema")
    descriptor = None
    for klass in PSM::JavaDataType.__mro__:
        if "JsonSchema" in klass.__dict__:
            descriptor = klass.__dict__["JsonSchema"]
            break
    assert isinstance(descriptor, property)



def test_psm::springmodelpojolayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringModelPojoLayer)


def test_psm::springmodelpojolayer_constructor_exists():
    assert callable(PSM::SpringModelPojoLayer.__init__)


def test_psm::springmodelpojolayer_constructor_args():
    sig = inspect.signature(PSM::SpringModelPojoLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springdomainlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringDomainLayer)


def test_psm::springdomainlayer_constructor_exists():
    assert callable(PSM::SpringDomainLayer.__init__)


def test_psm::springdomainlayer_constructor_args():
    sig = inspect.signature(PSM::SpringDomainLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springrepositorylayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringRepositoryLayer)


def test_psm::springrepositorylayer_constructor_exists():
    assert callable(PSM::SpringRepositoryLayer.__init__)


def test_psm::springrepositorylayer_constructor_args():
    sig = inspect.signature(PSM::SpringRepositoryLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springcomponentlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringComponentLayer)


def test_psm::springcomponentlayer_constructor_exists():
    assert callable(PSM::SpringComponentLayer.__init__)


def test_psm::springcomponentlayer_constructor_args():
    sig = inspect.signature(PSM::SpringComponentLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springfeignclientlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringFeignClientLayer)


def test_psm::springfeignclientlayer_constructor_exists():
    assert callable(PSM::SpringFeignClientLayer.__init__)


def test_psm::springfeignclientlayer_constructor_args():
    sig = inspect.signature(PSM::SpringFeignClientLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springconfigurationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringConfigurationLayer)


def test_psm::springconfigurationlayer_constructor_exists():
    assert callable(PSM::SpringConfigurationLayer.__init__)


def test_psm::springconfigurationlayer_constructor_args():
    sig = inspect.signature(PSM::SpringConfigurationLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springservicelayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringServiceLayer)


def test_psm::springservicelayer_constructor_exists():
    assert callable(PSM::SpringServiceLayer.__init__)


def test_psm::springservicelayer_constructor_args():
    sig = inspect.signature(PSM::SpringServiceLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm::springcontrollerlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringControllerLayer)


def test_psm::springcontrollerlayer_constructor_exists():
    assert callable(PSM::SpringControllerLayer.__init__)


def test_psm::springcontrollerlayer_constructor_args():
    sig = inspect.signature(PSM::SpringControllerLayer.__init__)
    params = list(sig.parameters.keys())



def test_artifactelement_is_not_abstract():
    assert not inspect.isabstract(ArtifactElement)


def test_artifactelement_constructor_exists():
    assert callable(ArtifactElement.__init__)


def test_artifactelement_constructor_args():
    sig = inspect.signature(ArtifactElement.__init__)
    params = list(sig.parameters.keys())



def test_psm::javaannotation_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaAnnotation)


def test_psm::javaannotation_constructor_exists():
    assert callable(PSM::JavaAnnotation.__init__)


def test_psm::javaannotation_constructor_args():
    sig = inspect.signature(PSM::JavaAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "AnnotationName" in params, "Missing parameter 'AnnotationName'"

def test_psm::javaannotation_has_AnnotationName():
    assert hasattr(PSM::JavaAnnotation, "AnnotationName")
    descriptor = None
    for klass in PSM::JavaAnnotation.__mro__:
        if "AnnotationName" in klass.__dict__:
            descriptor = klass.__dict__["AnnotationName"]
            break
    assert isinstance(descriptor, property)



def test_psm::javaelement_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaElement)


def test_psm::javaelement_constructor_exists():
    assert callable(PSM::JavaElement.__init__)


def test_psm::javaelement_constructor_args():
    sig = inspect.signature(PSM::JavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "ElementIdentifier" in params, "Missing parameter 'ElementIdentifier'"
    assert "ElementProfile" in params, "Missing parameter 'ElementProfile'"

def test_psm::javaelement_has_ElementIdentifier():
    assert hasattr(PSM::JavaElement, "ElementIdentifier")
    descriptor = None
    for klass in PSM::JavaElement.__mro__:
        if "ElementIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["ElementIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_psm::javaelement_has_ElementProfile():
    assert hasattr(PSM::JavaElement, "ElementProfile")
    descriptor = None
    for klass in PSM::JavaElement.__mro__:
        if "ElementProfile" in klass.__dict__:
            descriptor = klass.__dict__["ElementProfile"]
            break
    assert isinstance(descriptor, property)



def test_psm::javaannotationparameter_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaAnnotationParameter)


def test_psm::javaannotationparameter_constructor_exists():
    assert callable(PSM::JavaAnnotationParameter.__init__)


def test_psm::javaannotationparameter_constructor_args():
    sig = inspect.signature(PSM::JavaAnnotationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterName" in params, "Missing parameter 'ParameterName'"
    assert "ParameterValue" in params, "Missing parameter 'ParameterValue'"

def test_psm::javaannotationparameter_has_ParameterName():
    assert hasattr(PSM::JavaAnnotationParameter, "ParameterName")
    descriptor = None
    for klass in PSM::JavaAnnotationParameter.__mro__:
        if "ParameterName" in klass.__dict__:
            descriptor = klass.__dict__["ParameterName"]
            break
    assert isinstance(descriptor, property)

def test_psm::javaannotationparameter_has_ParameterValue():
    assert hasattr(PSM::JavaAnnotationParameter, "ParameterValue")
    descriptor = None
    for klass in PSM::JavaAnnotationParameter.__mro__:
        if "ParameterValue" in klass.__dict__:
            descriptor = klass.__dict__["ParameterValue"]
            break
    assert isinstance(descriptor, property)



def test_javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(JavaSpringWebApplicationProject)


def test_javaspringwebapplicationproject_constructor_exists():
    assert callable(JavaSpringWebApplicationProject.__init__)


def test_javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm::javaspringmvcapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaSpringMVCApplicationProject)


def test_psm::javaspringmvcapplicationproject_constructor_exists():
    assert callable(PSM::JavaSpringMVCApplicationProject.__init__)


def test_psm::javaspringmvcapplicationproject_constructor_args():
    sig = inspect.signature(PSM::JavaSpringMVCApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm::javaspringwebfluxapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaSpringWebFluxApplicationProject)


def test_psm::javaspringwebfluxapplicationproject_constructor_exists():
    assert callable(PSM::JavaSpringWebFluxApplicationProject.__init__)


def test_psm::javaspringwebfluxapplicationproject_constructor_args():
    sig = inspect.signature(PSM::JavaSpringWebFluxApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm::springwebapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM::SpringWebApplicationLayer)


def test_psm::springwebapplicationlayer_constructor_exists():
    assert callable(PSM::SpringWebApplicationLayer.__init__)


def test_psm::springwebapplicationlayer_constructor_args():
    sig = inspect.signature(PSM::SpringWebApplicationLayer.__init__)
    params = list(sig.parameters.keys())
    assert "LayerName" in params, "Missing parameter 'LayerName'"

def test_psm::springwebapplicationlayer_has_LayerName():
    assert hasattr(PSM::SpringWebApplicationLayer, "LayerName")
    descriptor = None
    for klass in PSM::SpringWebApplicationLayer.__mro__:
        if "LayerName" in klass.__dict__:
            descriptor = klass.__dict__["LayerName"]
            break
    assert isinstance(descriptor, property)



def test_psm::configurationproperty_is_not_abstract():
    assert not inspect.isabstract(PSM::ConfigurationProperty)


def test_psm::configurationproperty_constructor_exists():
    assert callable(PSM::ConfigurationProperty.__init__)


def test_psm::configurationproperty_constructor_args():
    sig = inspect.signature(PSM::ConfigurationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "PropertyValue" in params, "Missing parameter 'PropertyValue'"
    assert "FullyQualifiedPropertyName" in params, "Missing parameter 'FullyQualifiedPropertyName'"
    assert "ConfigurationProfile" in params, "Missing parameter 'ConfigurationProfile'"

def test_psm::configurationproperty_has_PropertyValue():
    assert hasattr(PSM::ConfigurationProperty, "PropertyValue")
    descriptor = None
    for klass in PSM::ConfigurationProperty.__mro__:
        if "PropertyValue" in klass.__dict__:
            descriptor = klass.__dict__["PropertyValue"]
            break
    assert isinstance(descriptor, property)

def test_psm::configurationproperty_has_FullyQualifiedPropertyName():
    assert hasattr(PSM::ConfigurationProperty, "FullyQualifiedPropertyName")
    descriptor = None
    for klass in PSM::ConfigurationProperty.__mro__:
        if "FullyQualifiedPropertyName" in klass.__dict__:
            descriptor = klass.__dict__["FullyQualifiedPropertyName"]
            break
    assert isinstance(descriptor, property)

def test_psm::configurationproperty_has_ConfigurationProfile():
    assert hasattr(PSM::ConfigurationProperty, "ConfigurationProfile")
    descriptor = None
    for klass in PSM::ConfigurationProperty.__mro__:
        if "ConfigurationProfile" in klass.__dict__:
            descriptor = klass.__dict__["ConfigurationProfile"]
            break
    assert isinstance(descriptor, property)



def test_microserviceproject_is_not_abstract():
    assert not inspect.isabstract(MicroserviceProject)


def test_microserviceproject_constructor_exists():
    assert callable(MicroserviceProject.__init__)


def test_microserviceproject_constructor_args():
    sig = inspect.signature(MicroserviceProject.__init__)
    params = list(sig.parameters.keys())



def test_psm::javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM::JavaSpringWebApplicationProject)


def test_psm::javaspringwebapplicationproject_constructor_exists():
    assert callable(PSM::JavaSpringWebApplicationProject.__init__)


def test_psm::javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(PSM::JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm::dependencylibrary_is_not_abstract():
    assert not inspect.isabstract(PSM::DependencyLibrary)


def test_psm::dependencylibrary_constructor_exists():
    assert callable(PSM::DependencyLibrary.__init__)


def test_psm::dependencylibrary_constructor_args():
    sig = inspect.signature(PSM::DependencyLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "LibraryName" in params, "Missing parameter 'LibraryName'"
    assert "LibraryScope" in params, "Missing parameter 'LibraryScope'"
    assert "LibraryGroupName" in params, "Missing parameter 'LibraryGroupName'"

def test_psm::dependencylibrary_has_LibraryName():
    assert hasattr(PSM::DependencyLibrary, "LibraryName")
    descriptor = None
    for klass in PSM::DependencyLibrary.__mro__:
        if "LibraryName" in klass.__dict__:
            descriptor = klass.__dict__["LibraryName"]
            break
    assert isinstance(descriptor, property)

def test_psm::dependencylibrary_has_LibraryScope():
    assert hasattr(PSM::DependencyLibrary, "LibraryScope")
    descriptor = None
    for klass in PSM::DependencyLibrary.__mro__:
        if "LibraryScope" in klass.__dict__:
            descriptor = klass.__dict__["LibraryScope"]
            break
    assert isinstance(descriptor, property)

def test_psm::dependencylibrary_has_LibraryGroupName():
    assert hasattr(PSM::DependencyLibrary, "LibraryGroupName")
    descriptor = None
    for klass in PSM::DependencyLibrary.__mro__:
        if "LibraryGroupName" in klass.__dict__:
            descriptor = klass.__dict__["LibraryGroupName"]
            break
    assert isinstance(descriptor, property)



def test_psm::microserviceproject_is_not_abstract():
    assert not inspect.isabstract(PSM::MicroserviceProject)


def test_psm::microserviceproject_constructor_exists():
    assert callable(PSM::MicroserviceProject.__init__)


def test_psm::microserviceproject_constructor_args():
    sig = inspect.signature(PSM::MicroserviceProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"

def test_psm::microserviceproject_has_ProjectArtifactId():
    assert hasattr(PSM::MicroserviceProject, "ProjectArtifactId")
    descriptor = None
    for klass in PSM::MicroserviceProject.__mro__:
        if "ProjectArtifactId" in klass.__dict__:
            descriptor = klass.__dict__["ProjectArtifactId"]
            break
    assert isinstance(descriptor, property)



def test_psm::dockercontainerport_is_not_abstract():
    assert not inspect.isabstract(PSM::DockerContainerPort)


def test_psm::dockercontainerport_constructor_exists():
    assert callable(PSM::DockerContainerPort.__init__)


def test_psm::dockercontainerport_constructor_args():
    sig = inspect.signature(PSM::DockerContainerPort.__init__)
    params = list(sig.parameters.keys())
    assert "ExposesPortsField" in params, "Missing parameter 'ExposesPortsField'"

def test_psm::dockercontainerport_has_ExposesPortsField():
    assert hasattr(PSM::DockerContainerPort, "ExposesPortsField")
    descriptor = None
    for klass in PSM::DockerContainerPort.__mro__:
        if "ExposesPortsField" in klass.__dict__:
            descriptor = klass.__dict__["ExposesPortsField"]
            break
    assert isinstance(descriptor, property)



def test_psm::dockercontainerlink_is_not_abstract():
    assert not inspect.isabstract(PSM::DockerContainerLink)


def test_psm::dockercontainerlink_constructor_exists():
    assert callable(PSM::DockerContainerLink.__init__)


def test_psm::dockercontainerlink_constructor_args():
    sig = inspect.signature(PSM::DockerContainerLink.__init__)
    params = list(sig.parameters.keys())
    assert "LinksDependsOnField" in params, "Missing parameter 'LinksDependsOnField'"
    assert "DependencyOrder" in params, "Missing parameter 'DependencyOrder'"

def test_psm::dockercontainerlink_has_LinksDependsOnField():
    assert hasattr(PSM::DockerContainerLink, "LinksDependsOnField")
    descriptor = None
    for klass in PSM::DockerContainerLink.__mro__:
        if "LinksDependsOnField" in klass.__dict__:
            descriptor = klass.__dict__["LinksDependsOnField"]
            break
    assert isinstance(descriptor, property)

def test_psm::dockercontainerlink_has_DependencyOrder():
    assert hasattr(PSM::DockerContainerLink, "DependencyOrder")
    descriptor = None
    for klass in PSM::DockerContainerLink.__mro__:
        if "DependencyOrder" in klass.__dict__:
            descriptor = klass.__dict__["DependencyOrder"]
            break
    assert isinstance(descriptor, property)



def test_psm::applicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM::ApplicationProject)


def test_psm::applicationproject_constructor_exists():
    assert callable(PSM::ApplicationProject.__init__)


def test_psm::applicationproject_constructor_args():
    sig = inspect.signature(PSM::ApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"

def test_psm::applicationproject_has_ProjectArtifactId():
    assert hasattr(PSM::ApplicationProject, "ProjectArtifactId")
    descriptor = None
    for klass in PSM::ApplicationProject.__mro__:
        if "ProjectArtifactId" in klass.__dict__:
            descriptor = klass.__dict__["ProjectArtifactId"]
            break
    assert isinstance(descriptor, property)



def test_psm::dockercontainerdefinition_is_not_abstract():
    assert not inspect.isabstract(PSM::DockerContainerDefinition)


def test_psm::dockercontainerdefinition_constructor_exists():
    assert callable(PSM::DockerContainerDefinition.__init__)


def test_psm::dockercontainerdefinition_constructor_args():
    sig = inspect.signature(PSM::DockerContainerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "GeneratesLogs" in params, "Missing parameter 'GeneratesLogs'"
    assert "BuildField" in params, "Missing parameter 'BuildField'"
    assert "ImageField" in params, "Missing parameter 'ImageField'"
    assert "ContainerName" in params, "Missing parameter 'ContainerName'"

def test_psm::dockercontainerdefinition_has_GeneratesLogs():
    assert hasattr(PSM::DockerContainerDefinition, "GeneratesLogs")
    descriptor = None
    for klass in PSM::DockerContainerDefinition.__mro__:
        if "GeneratesLogs" in klass.__dict__:
            descriptor = klass.__dict__["GeneratesLogs"]
            break
    assert isinstance(descriptor, property)

def test_psm::dockercontainerdefinition_has_BuildField():
    assert hasattr(PSM::DockerContainerDefinition, "BuildField")
    descriptor = None
    for klass in PSM::DockerContainerDefinition.__mro__:
        if "BuildField" in klass.__dict__:
            descriptor = klass.__dict__["BuildField"]
            break
    assert isinstance(descriptor, property)

def test_psm::dockercontainerdefinition_has_ImageField():
    assert hasattr(PSM::DockerContainerDefinition, "ImageField")
    descriptor = None
    for klass in PSM::DockerContainerDefinition.__mro__:
        if "ImageField" in klass.__dict__:
            descriptor = klass.__dict__["ImageField"]
            break
    assert isinstance(descriptor, property)

def test_psm::dockercontainerdefinition_has_ContainerName():
    assert hasattr(PSM::DockerContainerDefinition, "ContainerName")
    descriptor = None
    for klass in PSM::DockerContainerDefinition.__mro__:
        if "ContainerName" in klass.__dict__:
            descriptor = klass.__dict__["ContainerName"]
            break
    assert isinstance(descriptor, property)



def test_psm::distributedapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM::DistributedApplicationProject)


def test_psm::distributedapplicationproject_constructor_exists():
    assert callable(PSM::DistributedApplicationProject.__init__)


def test_psm::distributedapplicationproject_constructor_args():
    sig = inspect.signature(PSM::DistributedApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectPackageURL" in params, "Missing parameter 'ProjectPackageURL'"
    assert "ApplicationName" in params, "Missing parameter 'ApplicationName'"

def test_psm::distributedapplicationproject_has_ProjectPackageURL():
    assert hasattr(PSM::DistributedApplicationProject, "ProjectPackageURL")
    descriptor = None
    for klass in PSM::DistributedApplicationProject.__mro__:
        if "ProjectPackageURL" in klass.__dict__:
            descriptor = klass.__dict__["ProjectPackageURL"]
            break
    assert isinstance(descriptor, property)

def test_psm::distributedapplicationproject_has_ApplicationName():
    assert hasattr(PSM::DistributedApplicationProject, "ApplicationName")
    descriptor = None
    for klass in PSM::DistributedApplicationProject.__mro__:
        if "ApplicationName" in klass.__dict__:
            descriptor = klass.__dict__["ApplicationName"]
            break
    assert isinstance(descriptor, property)



def test_psm::rootpsm_is_not_abstract():
    assert not inspect.isabstract(PSM::RootPSM)


def test_psm::rootpsm_constructor_exists():
    assert callable(PSM::RootPSM.__init__)


def test_psm::rootpsm_constructor_args():
    sig = inspect.signature(PSM::RootPSM.__init__)
    params = list(sig.parameters.keys())



def test_psm::artifactelement_is_not_abstract():
    assert not inspect.isabstract(PSM::ArtifactElement)


def test_psm::artifactelement_constructor_exists():
    assert callable(PSM::ArtifactElement.__init__)


def test_psm::artifactelement_constructor_args():
    sig = inspect.signature(PSM::ArtifactElement.__init__)
    params = list(sig.parameters.keys())
    assert "ArtifactFileName" in params, "Missing parameter 'ArtifactFileName'"
    assert "GeneratingLinesOfCode" in params, "Missing parameter 'GeneratingLinesOfCode'"
    assert "ParentProjectName" in params, "Missing parameter 'ParentProjectName'"

def test_psm::artifactelement_has_ArtifactFileName():
    assert hasattr(PSM::ArtifactElement, "ArtifactFileName")
    descriptor = None
    for klass in PSM::ArtifactElement.__mro__:
        if "ArtifactFileName" in klass.__dict__:
            descriptor = klass.__dict__["ArtifactFileName"]
            break
    assert isinstance(descriptor, property)

def test_psm::artifactelement_has_GeneratingLinesOfCode():
    assert hasattr(PSM::ArtifactElement, "GeneratingLinesOfCode")
    descriptor = None
    for klass in PSM::ArtifactElement.__mro__:
        if "GeneratingLinesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["GeneratingLinesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_psm::artifactelement_has_ParentProjectName():
    assert hasattr(PSM::ArtifactElement, "ParentProjectName")
    descriptor = None
    for klass in PSM::ArtifactElement.__mro__:
        if "ParentProjectName" in klass.__dict__:
            descriptor = klass.__dict__["ParentProjectName"]
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
JavaUserDefinedType_strategy = st.builds(
    JavaUserDefinedType,
)
PSM::JavaInterfaceType_strategy = st.builds(
    PSM::JavaInterfaceType,
)
PSM::JavaClassType_strategy = st.builds(
    PSM::JavaClassType,
)
JavaDataField_strategy = st.builds(
    JavaDataField,
)
PSM::JavaMethodParameter_strategy = st.builds(
    PSM::JavaMethodParameter,
    ParameterOrder=
        st.integers()
)
SpringWebApplicationLayer_strategy = st.builds(
    SpringWebApplicationLayer,
)
PSM::SpringBootApplicationLayer_strategy = st.builds(
    PSM::SpringBootApplicationLayer,
)
JavaDataType_strategy = st.builds(
    JavaDataType,
)
PSM::JavaUserDefinedType_strategy = st.builds(
    PSM::JavaUserDefinedType,
)
JavaElement_strategy = st.builds(
    JavaElement,
)
PSM::JavaDataField_strategy = st.builds(
    PSM::JavaDataField,
    FieldValue=
        safe_text
)
PSM::JavaMethod_strategy = st.builds(
    PSM::JavaMethod,
    RootCallingMethod=
        safe_text
)
PSM::JavaDataType_strategy = st.builds(
    PSM::JavaDataType,
    IsPrimitive=
        st.booleans(),
    PackageName=
        safe_text,
    JsonSchema=
        safe_text
)
PSM::SpringModelPojoLayer_strategy = st.builds(
    PSM::SpringModelPojoLayer,
)
PSM::SpringDomainLayer_strategy = st.builds(
    PSM::SpringDomainLayer,
)
PSM::SpringRepositoryLayer_strategy = st.builds(
    PSM::SpringRepositoryLayer,
)
PSM::SpringComponentLayer_strategy = st.builds(
    PSM::SpringComponentLayer,
)
PSM::SpringFeignClientLayer_strategy = st.builds(
    PSM::SpringFeignClientLayer,
)
PSM::SpringConfigurationLayer_strategy = st.builds(
    PSM::SpringConfigurationLayer,
)
PSM::SpringServiceLayer_strategy = st.builds(
    PSM::SpringServiceLayer,
)
PSM::SpringControllerLayer_strategy = st.builds(
    PSM::SpringControllerLayer,
)
ArtifactElement_strategy = st.builds(
    ArtifactElement,
)
PSM::JavaAnnotation_strategy = st.builds(
    PSM::JavaAnnotation,
    AnnotationName=
        safe_text
)
PSM::JavaElement_strategy = st.builds(
    PSM::JavaElement,
    ElementIdentifier=
        safe_text,
    ElementProfile=
        safe_text
)
PSM::JavaAnnotationParameter_strategy = st.builds(
    PSM::JavaAnnotationParameter,
    ParameterName=
        safe_text,
    ParameterValue=
        safe_text
)
JavaSpringWebApplicationProject_strategy = st.builds(
    JavaSpringWebApplicationProject,
)
PSM::JavaSpringMVCApplicationProject_strategy = st.builds(
    PSM::JavaSpringMVCApplicationProject,
)
PSM::JavaSpringWebFluxApplicationProject_strategy = st.builds(
    PSM::JavaSpringWebFluxApplicationProject,
)
PSM::SpringWebApplicationLayer_strategy = st.builds(
    PSM::SpringWebApplicationLayer,
    LayerName=
        safe_text
)
PSM::ConfigurationProperty_strategy = st.builds(
    PSM::ConfigurationProperty,
    PropertyValue=
        safe_text,
    FullyQualifiedPropertyName=
        safe_text,
    ConfigurationProfile=
        safe_text
)
MicroserviceProject_strategy = st.builds(
    MicroserviceProject,
)
PSM::JavaSpringWebApplicationProject_strategy = st.builds(
    PSM::JavaSpringWebApplicationProject,
)
PSM::DependencyLibrary_strategy = st.builds(
    PSM::DependencyLibrary,
    LibraryName=
        safe_text,
    LibraryScope=
        safe_text,
    LibraryGroupName=
        safe_text
)
PSM::MicroserviceProject_strategy = st.builds(
    PSM::MicroserviceProject,
    ProjectArtifactId=
        safe_text
)
PSM::DockerContainerPort_strategy = st.builds(
    PSM::DockerContainerPort,
    ExposesPortsField=
        safe_text
)
PSM::DockerContainerLink_strategy = st.builds(
    PSM::DockerContainerLink,
    LinksDependsOnField=
        safe_text,
    DependencyOrder=
        st.integers()
)
PSM::ApplicationProject_strategy = st.builds(
    PSM::ApplicationProject,
    ProjectArtifactId=
        safe_text
)
PSM::DockerContainerDefinition_strategy = st.builds(
    PSM::DockerContainerDefinition,
    GeneratesLogs=
        st.booleans(),
    BuildField=
        safe_text,
    ImageField=
        safe_text,
    ContainerName=
        safe_text
)
PSM::DistributedApplicationProject_strategy = st.builds(
    PSM::DistributedApplicationProject,
    ProjectPackageURL=
        safe_text,
    ApplicationName=
        safe_text
)
PSM::RootPSM_strategy = st.builds(
    PSM::RootPSM,
)
PSM::ArtifactElement_strategy = st.builds(
    PSM::ArtifactElement,
    ArtifactFileName=
        safe_text,
    GeneratingLinesOfCode=
        safe_text,
    ParentProjectName=
        safe_text
)

@given(instance=JavaUserDefinedType_strategy)
@settings(max_examples=50)
def test_javauserdefinedtype_instantiation(instance):
    assert isinstance(instance, JavaUserDefinedType)

@given(instance=PSM::JavaInterfaceType_strategy)
@settings(max_examples=50)
def test_psm::javainterfacetype_instantiation(instance):
    assert isinstance(instance, PSM::JavaInterfaceType)

@given(instance=PSM::JavaClassType_strategy)
@settings(max_examples=50)
def test_psm::javaclasstype_instantiation(instance):
    assert isinstance(instance, PSM::JavaClassType)

@given(instance=JavaDataField_strategy)
@settings(max_examples=50)
def test_javadatafield_instantiation(instance):
    assert isinstance(instance, JavaDataField)

@given(instance=PSM::JavaMethodParameter_strategy)
@settings(max_examples=50)
def test_psm::javamethodparameter_instantiation(instance):
    assert isinstance(instance, PSM::JavaMethodParameter)

@given(instance=PSM::JavaMethodParameter_strategy)
def test_psm::javamethodparameter_ParameterOrder_type(instance):
    assert isinstance(instance.ParameterOrder, int)


@given(instance=PSM::JavaMethodParameter_strategy)
def test_psm::javamethodparameter_ParameterOrder_setter(instance):
    original = instance.ParameterOrder
    instance.ParameterOrder = original
    assert instance.ParameterOrder == original

@given(instance=SpringWebApplicationLayer_strategy)
@settings(max_examples=50)
def test_springwebapplicationlayer_instantiation(instance):
    assert isinstance(instance, SpringWebApplicationLayer)

@given(instance=PSM::SpringBootApplicationLayer_strategy)
@settings(max_examples=50)
def test_psm::springbootapplicationlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringBootApplicationLayer)

@given(instance=JavaDataType_strategy)
@settings(max_examples=50)
def test_javadatatype_instantiation(instance):
    assert isinstance(instance, JavaDataType)

@given(instance=PSM::JavaUserDefinedType_strategy)
@settings(max_examples=50)
def test_psm::javauserdefinedtype_instantiation(instance):
    assert isinstance(instance, PSM::JavaUserDefinedType)

@given(instance=JavaElement_strategy)
@settings(max_examples=50)
def test_javaelement_instantiation(instance):
    assert isinstance(instance, JavaElement)

@given(instance=PSM::JavaDataField_strategy)
@settings(max_examples=50)
def test_psm::javadatafield_instantiation(instance):
    assert isinstance(instance, PSM::JavaDataField)

@given(instance=PSM::JavaDataField_strategy)
def test_psm::javadatafield_FieldValue_type(instance):
    assert isinstance(instance.FieldValue, str)


@given(instance=PSM::JavaDataField_strategy)
def test_psm::javadatafield_FieldValue_setter(instance):
    original = instance.FieldValue
    instance.FieldValue = original
    assert instance.FieldValue == original

@given(instance=PSM::JavaMethod_strategy)
@settings(max_examples=50)
def test_psm::javamethod_instantiation(instance):
    assert isinstance(instance, PSM::JavaMethod)

@given(instance=PSM::JavaMethod_strategy)
def test_psm::javamethod_RootCallingMethod_type(instance):
    assert isinstance(instance.RootCallingMethod, str)


@given(instance=PSM::JavaMethod_strategy)
def test_psm::javamethod_RootCallingMethod_setter(instance):
    original = instance.RootCallingMethod
    instance.RootCallingMethod = original
    assert instance.RootCallingMethod == original

@given(instance=PSM::JavaDataType_strategy)
@settings(max_examples=50)
def test_psm::javadatatype_instantiation(instance):
    assert isinstance(instance, PSM::JavaDataType)

@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_IsPrimitive_type(instance):
    assert isinstance(instance.IsPrimitive, bool)


@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_IsPrimitive_setter(instance):
    original = instance.IsPrimitive
    instance.IsPrimitive = original
    assert instance.IsPrimitive == original

@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_PackageName_type(instance):
    assert isinstance(instance.PackageName, str)


@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_PackageName_setter(instance):
    original = instance.PackageName
    instance.PackageName = original
    assert instance.PackageName == original

@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_JsonSchema_type(instance):
    assert isinstance(instance.JsonSchema, str)


@given(instance=PSM::JavaDataType_strategy)
def test_psm::javadatatype_JsonSchema_setter(instance):
    original = instance.JsonSchema
    instance.JsonSchema = original
    assert instance.JsonSchema == original

@given(instance=PSM::SpringModelPojoLayer_strategy)
@settings(max_examples=50)
def test_psm::springmodelpojolayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringModelPojoLayer)

@given(instance=PSM::SpringDomainLayer_strategy)
@settings(max_examples=50)
def test_psm::springdomainlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringDomainLayer)

@given(instance=PSM::SpringRepositoryLayer_strategy)
@settings(max_examples=50)
def test_psm::springrepositorylayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringRepositoryLayer)

@given(instance=PSM::SpringComponentLayer_strategy)
@settings(max_examples=50)
def test_psm::springcomponentlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringComponentLayer)

@given(instance=PSM::SpringFeignClientLayer_strategy)
@settings(max_examples=50)
def test_psm::springfeignclientlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringFeignClientLayer)

@given(instance=PSM::SpringConfigurationLayer_strategy)
@settings(max_examples=50)
def test_psm::springconfigurationlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringConfigurationLayer)

@given(instance=PSM::SpringServiceLayer_strategy)
@settings(max_examples=50)
def test_psm::springservicelayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringServiceLayer)

@given(instance=PSM::SpringControllerLayer_strategy)
@settings(max_examples=50)
def test_psm::springcontrollerlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringControllerLayer)

@given(instance=ArtifactElement_strategy)
@settings(max_examples=50)
def test_artifactelement_instantiation(instance):
    assert isinstance(instance, ArtifactElement)

@given(instance=PSM::JavaAnnotation_strategy)
@settings(max_examples=50)
def test_psm::javaannotation_instantiation(instance):
    assert isinstance(instance, PSM::JavaAnnotation)

@given(instance=PSM::JavaAnnotation_strategy)
def test_psm::javaannotation_AnnotationName_type(instance):
    assert isinstance(instance.AnnotationName, str)


@given(instance=PSM::JavaAnnotation_strategy)
def test_psm::javaannotation_AnnotationName_setter(instance):
    original = instance.AnnotationName
    instance.AnnotationName = original
    assert instance.AnnotationName == original

@given(instance=PSM::JavaElement_strategy)
@settings(max_examples=50)
def test_psm::javaelement_instantiation(instance):
    assert isinstance(instance, PSM::JavaElement)

@given(instance=PSM::JavaElement_strategy)
def test_psm::javaelement_ElementIdentifier_type(instance):
    assert isinstance(instance.ElementIdentifier, str)


@given(instance=PSM::JavaElement_strategy)
def test_psm::javaelement_ElementIdentifier_setter(instance):
    original = instance.ElementIdentifier
    instance.ElementIdentifier = original
    assert instance.ElementIdentifier == original

@given(instance=PSM::JavaElement_strategy)
def test_psm::javaelement_ElementProfile_type(instance):
    assert isinstance(instance.ElementProfile, str)


@given(instance=PSM::JavaElement_strategy)
def test_psm::javaelement_ElementProfile_setter(instance):
    original = instance.ElementProfile
    instance.ElementProfile = original
    assert instance.ElementProfile == original

@given(instance=PSM::JavaAnnotationParameter_strategy)
@settings(max_examples=50)
def test_psm::javaannotationparameter_instantiation(instance):
    assert isinstance(instance, PSM::JavaAnnotationParameter)

@given(instance=PSM::JavaAnnotationParameter_strategy)
def test_psm::javaannotationparameter_ParameterName_type(instance):
    assert isinstance(instance.ParameterName, str)


@given(instance=PSM::JavaAnnotationParameter_strategy)
def test_psm::javaannotationparameter_ParameterName_setter(instance):
    original = instance.ParameterName
    instance.ParameterName = original
    assert instance.ParameterName == original

@given(instance=PSM::JavaAnnotationParameter_strategy)
def test_psm::javaannotationparameter_ParameterValue_type(instance):
    assert isinstance(instance.ParameterValue, str)


@given(instance=PSM::JavaAnnotationParameter_strategy)
def test_psm::javaannotationparameter_ParameterValue_setter(instance):
    original = instance.ParameterValue
    instance.ParameterValue = original
    assert instance.ParameterValue == original

@given(instance=JavaSpringWebApplicationProject_strategy)
@settings(max_examples=50)
def test_javaspringwebapplicationproject_instantiation(instance):
    assert isinstance(instance, JavaSpringWebApplicationProject)

@given(instance=PSM::JavaSpringMVCApplicationProject_strategy)
@settings(max_examples=50)
def test_psm::javaspringmvcapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM::JavaSpringMVCApplicationProject)

@given(instance=PSM::JavaSpringWebFluxApplicationProject_strategy)
@settings(max_examples=50)
def test_psm::javaspringwebfluxapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM::JavaSpringWebFluxApplicationProject)

@given(instance=PSM::SpringWebApplicationLayer_strategy)
@settings(max_examples=50)
def test_psm::springwebapplicationlayer_instantiation(instance):
    assert isinstance(instance, PSM::SpringWebApplicationLayer)

@given(instance=PSM::SpringWebApplicationLayer_strategy)
def test_psm::springwebapplicationlayer_LayerName_type(instance):
    assert isinstance(instance.LayerName, str)


@given(instance=PSM::SpringWebApplicationLayer_strategy)
def test_psm::springwebapplicationlayer_LayerName_setter(instance):
    original = instance.LayerName
    instance.LayerName = original
    assert instance.LayerName == original

@given(instance=PSM::ConfigurationProperty_strategy)
@settings(max_examples=50)
def test_psm::configurationproperty_instantiation(instance):
    assert isinstance(instance, PSM::ConfigurationProperty)

@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_PropertyValue_type(instance):
    assert isinstance(instance.PropertyValue, str)


@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_PropertyValue_setter(instance):
    original = instance.PropertyValue
    instance.PropertyValue = original
    assert instance.PropertyValue == original

@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_FullyQualifiedPropertyName_type(instance):
    assert isinstance(instance.FullyQualifiedPropertyName, str)


@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_FullyQualifiedPropertyName_setter(instance):
    original = instance.FullyQualifiedPropertyName
    instance.FullyQualifiedPropertyName = original
    assert instance.FullyQualifiedPropertyName == original

@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_ConfigurationProfile_type(instance):
    assert isinstance(instance.ConfigurationProfile, str)


@given(instance=PSM::ConfigurationProperty_strategy)
def test_psm::configurationproperty_ConfigurationProfile_setter(instance):
    original = instance.ConfigurationProfile
    instance.ConfigurationProfile = original
    assert instance.ConfigurationProfile == original

@given(instance=MicroserviceProject_strategy)
@settings(max_examples=50)
def test_microserviceproject_instantiation(instance):
    assert isinstance(instance, MicroserviceProject)

@given(instance=PSM::JavaSpringWebApplicationProject_strategy)
@settings(max_examples=50)
def test_psm::javaspringwebapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM::JavaSpringWebApplicationProject)

@given(instance=PSM::DependencyLibrary_strategy)
@settings(max_examples=50)
def test_psm::dependencylibrary_instantiation(instance):
    assert isinstance(instance, PSM::DependencyLibrary)

@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryName_type(instance):
    assert isinstance(instance.LibraryName, str)


@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryName_setter(instance):
    original = instance.LibraryName
    instance.LibraryName = original
    assert instance.LibraryName == original

@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryScope_type(instance):
    assert isinstance(instance.LibraryScope, str)


@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryScope_setter(instance):
    original = instance.LibraryScope
    instance.LibraryScope = original
    assert instance.LibraryScope == original

@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryGroupName_type(instance):
    assert isinstance(instance.LibraryGroupName, str)


@given(instance=PSM::DependencyLibrary_strategy)
def test_psm::dependencylibrary_LibraryGroupName_setter(instance):
    original = instance.LibraryGroupName
    instance.LibraryGroupName = original
    assert instance.LibraryGroupName == original

@given(instance=PSM::MicroserviceProject_strategy)
@settings(max_examples=50)
def test_psm::microserviceproject_instantiation(instance):
    assert isinstance(instance, PSM::MicroserviceProject)

@given(instance=PSM::MicroserviceProject_strategy)
def test_psm::microserviceproject_ProjectArtifactId_type(instance):
    assert isinstance(instance.ProjectArtifactId, str)


@given(instance=PSM::MicroserviceProject_strategy)
def test_psm::microserviceproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original

@given(instance=PSM::DockerContainerPort_strategy)
@settings(max_examples=50)
def test_psm::dockercontainerport_instantiation(instance):
    assert isinstance(instance, PSM::DockerContainerPort)

@given(instance=PSM::DockerContainerPort_strategy)
def test_psm::dockercontainerport_ExposesPortsField_type(instance):
    assert isinstance(instance.ExposesPortsField, str)


@given(instance=PSM::DockerContainerPort_strategy)
def test_psm::dockercontainerport_ExposesPortsField_setter(instance):
    original = instance.ExposesPortsField
    instance.ExposesPortsField = original
    assert instance.ExposesPortsField == original

@given(instance=PSM::DockerContainerLink_strategy)
@settings(max_examples=50)
def test_psm::dockercontainerlink_instantiation(instance):
    assert isinstance(instance, PSM::DockerContainerLink)

@given(instance=PSM::DockerContainerLink_strategy)
def test_psm::dockercontainerlink_LinksDependsOnField_type(instance):
    assert isinstance(instance.LinksDependsOnField, str)


@given(instance=PSM::DockerContainerLink_strategy)
def test_psm::dockercontainerlink_LinksDependsOnField_setter(instance):
    original = instance.LinksDependsOnField
    instance.LinksDependsOnField = original
    assert instance.LinksDependsOnField == original

@given(instance=PSM::DockerContainerLink_strategy)
def test_psm::dockercontainerlink_DependencyOrder_type(instance):
    assert isinstance(instance.DependencyOrder, int)


@given(instance=PSM::DockerContainerLink_strategy)
def test_psm::dockercontainerlink_DependencyOrder_setter(instance):
    original = instance.DependencyOrder
    instance.DependencyOrder = original
    assert instance.DependencyOrder == original

@given(instance=PSM::ApplicationProject_strategy)
@settings(max_examples=50)
def test_psm::applicationproject_instantiation(instance):
    assert isinstance(instance, PSM::ApplicationProject)

@given(instance=PSM::ApplicationProject_strategy)
def test_psm::applicationproject_ProjectArtifactId_type(instance):
    assert isinstance(instance.ProjectArtifactId, str)


@given(instance=PSM::ApplicationProject_strategy)
def test_psm::applicationproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original

@given(instance=PSM::DockerContainerDefinition_strategy)
@settings(max_examples=50)
def test_psm::dockercontainerdefinition_instantiation(instance):
    assert isinstance(instance, PSM::DockerContainerDefinition)

@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_GeneratesLogs_type(instance):
    assert isinstance(instance.GeneratesLogs, bool)


@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_GeneratesLogs_setter(instance):
    original = instance.GeneratesLogs
    instance.GeneratesLogs = original
    assert instance.GeneratesLogs == original

@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_BuildField_type(instance):
    assert isinstance(instance.BuildField, str)


@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_BuildField_setter(instance):
    original = instance.BuildField
    instance.BuildField = original
    assert instance.BuildField == original

@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_ImageField_type(instance):
    assert isinstance(instance.ImageField, str)


@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_ImageField_setter(instance):
    original = instance.ImageField
    instance.ImageField = original
    assert instance.ImageField == original

@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_ContainerName_type(instance):
    assert isinstance(instance.ContainerName, str)


@given(instance=PSM::DockerContainerDefinition_strategy)
def test_psm::dockercontainerdefinition_ContainerName_setter(instance):
    original = instance.ContainerName
    instance.ContainerName = original
    assert instance.ContainerName == original

@given(instance=PSM::DistributedApplicationProject_strategy)
@settings(max_examples=50)
def test_psm::distributedapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM::DistributedApplicationProject)

@given(instance=PSM::DistributedApplicationProject_strategy)
def test_psm::distributedapplicationproject_ProjectPackageURL_type(instance):
    assert isinstance(instance.ProjectPackageURL, str)


@given(instance=PSM::DistributedApplicationProject_strategy)
def test_psm::distributedapplicationproject_ProjectPackageURL_setter(instance):
    original = instance.ProjectPackageURL
    instance.ProjectPackageURL = original
    assert instance.ProjectPackageURL == original

@given(instance=PSM::DistributedApplicationProject_strategy)
def test_psm::distributedapplicationproject_ApplicationName_type(instance):
    assert isinstance(instance.ApplicationName, str)


@given(instance=PSM::DistributedApplicationProject_strategy)
def test_psm::distributedapplicationproject_ApplicationName_setter(instance):
    original = instance.ApplicationName
    instance.ApplicationName = original
    assert instance.ApplicationName == original

@given(instance=PSM::RootPSM_strategy)
@settings(max_examples=50)
def test_psm::rootpsm_instantiation(instance):
    assert isinstance(instance, PSM::RootPSM)

@given(instance=PSM::ArtifactElement_strategy)
@settings(max_examples=50)
def test_psm::artifactelement_instantiation(instance):
    assert isinstance(instance, PSM::ArtifactElement)

@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_ArtifactFileName_type(instance):
    assert isinstance(instance.ArtifactFileName, str)


@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_ArtifactFileName_setter(instance):
    original = instance.ArtifactFileName
    instance.ArtifactFileName = original
    assert instance.ArtifactFileName == original

@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_GeneratingLinesOfCode_type(instance):
    assert isinstance(instance.GeneratingLinesOfCode, str)


@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_GeneratingLinesOfCode_setter(instance):
    original = instance.GeneratingLinesOfCode
    instance.GeneratingLinesOfCode = original
    assert instance.GeneratingLinesOfCode == original

@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_ParentProjectName_type(instance):
    assert isinstance(instance.ParentProjectName, str)


@given(instance=PSM::ArtifactElement_strategy)
def test_psm::artifactelement_ParentProjectName_setter(instance):
    original = instance.ParentProjectName
    instance.ParentProjectName = original
    assert instance.ParentProjectName == original
