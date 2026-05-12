import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JavaUserDefinedType,
    PSM_JavaInterfaceType,
    PSM_JavaClassType,
    JavaDataField,
    PSM_JavaMethodParameter,
    SpringWebApplicationLayer,
    PSM_SpringBootApplicationLayer,
    JavaDataType,
    PSM_JavaUserDefinedType,
    JavaElement,
    PSM_JavaDataField,
    PSM_JavaMethod,
    PSM_JavaDataType,
    PSM_SpringModelPojoLayer,
    PSM_SpringDomainLayer,
    PSM_SpringRepositoryLayer,
    PSM_SpringComponentLayer,
    PSM_SpringFeignClientLayer,
    PSM_SpringConfigurationLayer,
    PSM_SpringServiceLayer,
    PSM_SpringControllerLayer,
    ArtifactElement,
    PSM_JavaElement,
    PSM_JavaAnnotationParameter,
    PSM_JavaAnnotation,
    JavaSpringWebApplicationProject,
    PSM_JavaSpringMVCApplicationProject,
    PSM_JavaSpringWebFluxApplicationProject,
    PSM_SpringWebApplicationLayer,
    PSM_ConfigurationProperty,
    MicroserviceProject,
    PSM_JavaSpringWebApplicationProject,
    PSM_DependencyLibrary,
    PSM_MicroserviceProject,
    PSM_DockerContainerPort,
    PSM_DockerContainerLink,
    PSM_ApplicationProject,
    PSM_DockerContainerDefinition,
    PSM_DistributedApplicationProject,
    PSM_RootPSM,
    PSM_ArtifactElement,
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



def test_psm_javainterfacetype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaInterfaceType)


def test_psm_javainterfacetype_constructor_exists():
    assert callable(PSM_JavaInterfaceType.__init__)


def test_psm_javainterfacetype_constructor_args():
    sig = inspect.signature(PSM_JavaInterfaceType.__init__)
    params = list(sig.parameters.keys())



def test_psm_javaclasstype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaClassType)


def test_psm_javaclasstype_constructor_exists():
    assert callable(PSM_JavaClassType.__init__)


def test_psm_javaclasstype_constructor_args():
    sig = inspect.signature(PSM_JavaClassType.__init__)
    params = list(sig.parameters.keys())



def test_javadatafield_is_not_abstract():
    assert not inspect.isabstract(JavaDataField)


def test_javadatafield_constructor_exists():
    assert callable(JavaDataField.__init__)


def test_javadatafield_constructor_args():
    sig = inspect.signature(JavaDataField.__init__)
    params = list(sig.parameters.keys())



def test_psm_javamethodparameter_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaMethodParameter)


def test_psm_javamethodparameter_constructor_exists():
    assert callable(PSM_JavaMethodParameter.__init__)


def test_psm_javamethodparameter_constructor_args():
    sig = inspect.signature(PSM_JavaMethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterOrder" in params, "Missing parameter 'ParameterOrder'"

def test_psm_javamethodparameter_has_ParameterOrder():
    assert hasattr(PSM_JavaMethodParameter, "ParameterOrder")
    descriptor = None
    for klass in PSM_JavaMethodParameter.__mro__:
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



def test_psm_springbootapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringBootApplicationLayer)


def test_psm_springbootapplicationlayer_constructor_exists():
    assert callable(PSM_SpringBootApplicationLayer.__init__)


def test_psm_springbootapplicationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringBootApplicationLayer.__init__)
    params = list(sig.parameters.keys())



def test_javadatatype_is_not_abstract():
    assert not inspect.isabstract(JavaDataType)


def test_javadatatype_constructor_exists():
    assert callable(JavaDataType.__init__)


def test_javadatatype_constructor_args():
    sig = inspect.signature(JavaDataType.__init__)
    params = list(sig.parameters.keys())



def test_psm_javauserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaUserDefinedType)


def test_psm_javauserdefinedtype_constructor_exists():
    assert callable(PSM_JavaUserDefinedType.__init__)


def test_psm_javauserdefinedtype_constructor_args():
    sig = inspect.signature(PSM_JavaUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_javaelement_is_not_abstract():
    assert not inspect.isabstract(JavaElement)


def test_javaelement_constructor_exists():
    assert callable(JavaElement.__init__)


def test_javaelement_constructor_args():
    sig = inspect.signature(JavaElement.__init__)
    params = list(sig.parameters.keys())



def test_psm_javadatafield_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaDataField)


def test_psm_javadatafield_constructor_exists():
    assert callable(PSM_JavaDataField.__init__)


def test_psm_javadatafield_constructor_args():
    sig = inspect.signature(PSM_JavaDataField.__init__)
    params = list(sig.parameters.keys())
    assert "FieldValue" in params, "Missing parameter 'FieldValue'"

def test_psm_javadatafield_has_FieldValue():
    assert hasattr(PSM_JavaDataField, "FieldValue")
    descriptor = None
    for klass in PSM_JavaDataField.__mro__:
        if "FieldValue" in klass.__dict__:
            descriptor = klass.__dict__["FieldValue"]
            break
    assert isinstance(descriptor, property)



def test_psm_javamethod_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaMethod)


def test_psm_javamethod_constructor_exists():
    assert callable(PSM_JavaMethod.__init__)


def test_psm_javamethod_constructor_args():
    sig = inspect.signature(PSM_JavaMethod.__init__)
    params = list(sig.parameters.keys())
    assert "RootCallingMethod" in params, "Missing parameter 'RootCallingMethod'"

def test_psm_javamethod_has_RootCallingMethod():
    assert hasattr(PSM_JavaMethod, "RootCallingMethod")
    descriptor = None
    for klass in PSM_JavaMethod.__mro__:
        if "RootCallingMethod" in klass.__dict__:
            descriptor = klass.__dict__["RootCallingMethod"]
            break
    assert isinstance(descriptor, property)



def test_psm_javadatatype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaDataType)


def test_psm_javadatatype_constructor_exists():
    assert callable(PSM_JavaDataType.__init__)


def test_psm_javadatatype_constructor_args():
    sig = inspect.signature(PSM_JavaDataType.__init__)
    params = list(sig.parameters.keys())
    assert "PackageName" in params, "Missing parameter 'PackageName'"
    assert "IsPrimitive" in params, "Missing parameter 'IsPrimitive'"
    assert "JsonSchema" in params, "Missing parameter 'JsonSchema'"

def test_psm_javadatatype_has_PackageName():
    assert hasattr(PSM_JavaDataType, "PackageName")
    descriptor = None
    for klass in PSM_JavaDataType.__mro__:
        if "PackageName" in klass.__dict__:
            descriptor = klass.__dict__["PackageName"]
            break
    assert isinstance(descriptor, property)

def test_psm_javadatatype_has_IsPrimitive():
    assert hasattr(PSM_JavaDataType, "IsPrimitive")
    descriptor = None
    for klass in PSM_JavaDataType.__mro__:
        if "IsPrimitive" in klass.__dict__:
            descriptor = klass.__dict__["IsPrimitive"]
            break
    assert isinstance(descriptor, property)

def test_psm_javadatatype_has_JsonSchema():
    assert hasattr(PSM_JavaDataType, "JsonSchema")
    descriptor = None
    for klass in PSM_JavaDataType.__mro__:
        if "JsonSchema" in klass.__dict__:
            descriptor = klass.__dict__["JsonSchema"]
            break
    assert isinstance(descriptor, property)



def test_psm_springmodelpojolayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringModelPojoLayer)


def test_psm_springmodelpojolayer_constructor_exists():
    assert callable(PSM_SpringModelPojoLayer.__init__)


def test_psm_springmodelpojolayer_constructor_args():
    sig = inspect.signature(PSM_SpringModelPojoLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springdomainlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringDomainLayer)


def test_psm_springdomainlayer_constructor_exists():
    assert callable(PSM_SpringDomainLayer.__init__)


def test_psm_springdomainlayer_constructor_args():
    sig = inspect.signature(PSM_SpringDomainLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springrepositorylayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringRepositoryLayer)


def test_psm_springrepositorylayer_constructor_exists():
    assert callable(PSM_SpringRepositoryLayer.__init__)


def test_psm_springrepositorylayer_constructor_args():
    sig = inspect.signature(PSM_SpringRepositoryLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springcomponentlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringComponentLayer)


def test_psm_springcomponentlayer_constructor_exists():
    assert callable(PSM_SpringComponentLayer.__init__)


def test_psm_springcomponentlayer_constructor_args():
    sig = inspect.signature(PSM_SpringComponentLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springfeignclientlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringFeignClientLayer)


def test_psm_springfeignclientlayer_constructor_exists():
    assert callable(PSM_SpringFeignClientLayer.__init__)


def test_psm_springfeignclientlayer_constructor_args():
    sig = inspect.signature(PSM_SpringFeignClientLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springconfigurationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringConfigurationLayer)


def test_psm_springconfigurationlayer_constructor_exists():
    assert callable(PSM_SpringConfigurationLayer.__init__)


def test_psm_springconfigurationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringConfigurationLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springservicelayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringServiceLayer)


def test_psm_springservicelayer_constructor_exists():
    assert callable(PSM_SpringServiceLayer.__init__)


def test_psm_springservicelayer_constructor_args():
    sig = inspect.signature(PSM_SpringServiceLayer.__init__)
    params = list(sig.parameters.keys())



def test_psm_springcontrollerlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringControllerLayer)


def test_psm_springcontrollerlayer_constructor_exists():
    assert callable(PSM_SpringControllerLayer.__init__)


def test_psm_springcontrollerlayer_constructor_args():
    sig = inspect.signature(PSM_SpringControllerLayer.__init__)
    params = list(sig.parameters.keys())



def test_artifactelement_is_not_abstract():
    assert not inspect.isabstract(ArtifactElement)


def test_artifactelement_constructor_exists():
    assert callable(ArtifactElement.__init__)


def test_artifactelement_constructor_args():
    sig = inspect.signature(ArtifactElement.__init__)
    params = list(sig.parameters.keys())



def test_psm_javaelement_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaElement)


def test_psm_javaelement_constructor_exists():
    assert callable(PSM_JavaElement.__init__)


def test_psm_javaelement_constructor_args():
    sig = inspect.signature(PSM_JavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "ElementIdentifier" in params, "Missing parameter 'ElementIdentifier'"
    assert "ElementProfile" in params, "Missing parameter 'ElementProfile'"

def test_psm_javaelement_has_ElementIdentifier():
    assert hasattr(PSM_JavaElement, "ElementIdentifier")
    descriptor = None
    for klass in PSM_JavaElement.__mro__:
        if "ElementIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["ElementIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_psm_javaelement_has_ElementProfile():
    assert hasattr(PSM_JavaElement, "ElementProfile")
    descriptor = None
    for klass in PSM_JavaElement.__mro__:
        if "ElementProfile" in klass.__dict__:
            descriptor = klass.__dict__["ElementProfile"]
            break
    assert isinstance(descriptor, property)



def test_psm_javaannotationparameter_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaAnnotationParameter)


def test_psm_javaannotationparameter_constructor_exists():
    assert callable(PSM_JavaAnnotationParameter.__init__)


def test_psm_javaannotationparameter_constructor_args():
    sig = inspect.signature(PSM_JavaAnnotationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterName" in params, "Missing parameter 'ParameterName'"
    assert "ParameterValue" in params, "Missing parameter 'ParameterValue'"

def test_psm_javaannotationparameter_has_ParameterName():
    assert hasattr(PSM_JavaAnnotationParameter, "ParameterName")
    descriptor = None
    for klass in PSM_JavaAnnotationParameter.__mro__:
        if "ParameterName" in klass.__dict__:
            descriptor = klass.__dict__["ParameterName"]
            break
    assert isinstance(descriptor, property)

def test_psm_javaannotationparameter_has_ParameterValue():
    assert hasattr(PSM_JavaAnnotationParameter, "ParameterValue")
    descriptor = None
    for klass in PSM_JavaAnnotationParameter.__mro__:
        if "ParameterValue" in klass.__dict__:
            descriptor = klass.__dict__["ParameterValue"]
            break
    assert isinstance(descriptor, property)



def test_psm_javaannotation_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaAnnotation)


def test_psm_javaannotation_constructor_exists():
    assert callable(PSM_JavaAnnotation.__init__)


def test_psm_javaannotation_constructor_args():
    sig = inspect.signature(PSM_JavaAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "AnnotationName" in params, "Missing parameter 'AnnotationName'"

def test_psm_javaannotation_has_AnnotationName():
    assert hasattr(PSM_JavaAnnotation, "AnnotationName")
    descriptor = None
    for klass in PSM_JavaAnnotation.__mro__:
        if "AnnotationName" in klass.__dict__:
            descriptor = klass.__dict__["AnnotationName"]
            break
    assert isinstance(descriptor, property)



def test_javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(JavaSpringWebApplicationProject)


def test_javaspringwebapplicationproject_constructor_exists():
    assert callable(JavaSpringWebApplicationProject.__init__)


def test_javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm_javaspringmvcapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringMVCApplicationProject)


def test_psm_javaspringmvcapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringMVCApplicationProject.__init__)


def test_psm_javaspringmvcapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringMVCApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm_javaspringwebfluxapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringWebFluxApplicationProject)


def test_psm_javaspringwebfluxapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringWebFluxApplicationProject.__init__)


def test_psm_javaspringwebfluxapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringWebFluxApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm_springwebapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringWebApplicationLayer)


def test_psm_springwebapplicationlayer_constructor_exists():
    assert callable(PSM_SpringWebApplicationLayer.__init__)


def test_psm_springwebapplicationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringWebApplicationLayer.__init__)
    params = list(sig.parameters.keys())
    assert "LayerName" in params, "Missing parameter 'LayerName'"

def test_psm_springwebapplicationlayer_has_LayerName():
    assert hasattr(PSM_SpringWebApplicationLayer, "LayerName")
    descriptor = None
    for klass in PSM_SpringWebApplicationLayer.__mro__:
        if "LayerName" in klass.__dict__:
            descriptor = klass.__dict__["LayerName"]
            break
    assert isinstance(descriptor, property)



def test_psm_configurationproperty_is_not_abstract():
    assert not inspect.isabstract(PSM_ConfigurationProperty)


def test_psm_configurationproperty_constructor_exists():
    assert callable(PSM_ConfigurationProperty.__init__)


def test_psm_configurationproperty_constructor_args():
    sig = inspect.signature(PSM_ConfigurationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "PropertyValue" in params, "Missing parameter 'PropertyValue'"
    assert "ConfigurationProfile" in params, "Missing parameter 'ConfigurationProfile'"
    assert "FullyQualifiedPropertyName" in params, "Missing parameter 'FullyQualifiedPropertyName'"

def test_psm_configurationproperty_has_PropertyValue():
    assert hasattr(PSM_ConfigurationProperty, "PropertyValue")
    descriptor = None
    for klass in PSM_ConfigurationProperty.__mro__:
        if "PropertyValue" in klass.__dict__:
            descriptor = klass.__dict__["PropertyValue"]
            break
    assert isinstance(descriptor, property)

def test_psm_configurationproperty_has_ConfigurationProfile():
    assert hasattr(PSM_ConfigurationProperty, "ConfigurationProfile")
    descriptor = None
    for klass in PSM_ConfigurationProperty.__mro__:
        if "ConfigurationProfile" in klass.__dict__:
            descriptor = klass.__dict__["ConfigurationProfile"]
            break
    assert isinstance(descriptor, property)

def test_psm_configurationproperty_has_FullyQualifiedPropertyName():
    assert hasattr(PSM_ConfigurationProperty, "FullyQualifiedPropertyName")
    descriptor = None
    for klass in PSM_ConfigurationProperty.__mro__:
        if "FullyQualifiedPropertyName" in klass.__dict__:
            descriptor = klass.__dict__["FullyQualifiedPropertyName"]
            break
    assert isinstance(descriptor, property)



def test_microserviceproject_is_not_abstract():
    assert not inspect.isabstract(MicroserviceProject)


def test_microserviceproject_constructor_exists():
    assert callable(MicroserviceProject.__init__)


def test_microserviceproject_constructor_args():
    sig = inspect.signature(MicroserviceProject.__init__)
    params = list(sig.parameters.keys())



def test_psm_javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringWebApplicationProject)


def test_psm_javaspringwebapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringWebApplicationProject.__init__)


def test_psm_javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_psm_dependencylibrary_is_not_abstract():
    assert not inspect.isabstract(PSM_DependencyLibrary)


def test_psm_dependencylibrary_constructor_exists():
    assert callable(PSM_DependencyLibrary.__init__)


def test_psm_dependencylibrary_constructor_args():
    sig = inspect.signature(PSM_DependencyLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "LibraryName" in params, "Missing parameter 'LibraryName'"
    assert "LibraryScope" in params, "Missing parameter 'LibraryScope'"
    assert "LibraryGroupName" in params, "Missing parameter 'LibraryGroupName'"

def test_psm_dependencylibrary_has_LibraryName():
    assert hasattr(PSM_DependencyLibrary, "LibraryName")
    descriptor = None
    for klass in PSM_DependencyLibrary.__mro__:
        if "LibraryName" in klass.__dict__:
            descriptor = klass.__dict__["LibraryName"]
            break
    assert isinstance(descriptor, property)

def test_psm_dependencylibrary_has_LibraryScope():
    assert hasattr(PSM_DependencyLibrary, "LibraryScope")
    descriptor = None
    for klass in PSM_DependencyLibrary.__mro__:
        if "LibraryScope" in klass.__dict__:
            descriptor = klass.__dict__["LibraryScope"]
            break
    assert isinstance(descriptor, property)

def test_psm_dependencylibrary_has_LibraryGroupName():
    assert hasattr(PSM_DependencyLibrary, "LibraryGroupName")
    descriptor = None
    for klass in PSM_DependencyLibrary.__mro__:
        if "LibraryGroupName" in klass.__dict__:
            descriptor = klass.__dict__["LibraryGroupName"]
            break
    assert isinstance(descriptor, property)



def test_psm_microserviceproject_is_not_abstract():
    assert not inspect.isabstract(PSM_MicroserviceProject)


def test_psm_microserviceproject_constructor_exists():
    assert callable(PSM_MicroserviceProject.__init__)


def test_psm_microserviceproject_constructor_args():
    sig = inspect.signature(PSM_MicroserviceProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"

def test_psm_microserviceproject_has_ProjectArtifactId():
    assert hasattr(PSM_MicroserviceProject, "ProjectArtifactId")
    descriptor = None
    for klass in PSM_MicroserviceProject.__mro__:
        if "ProjectArtifactId" in klass.__dict__:
            descriptor = klass.__dict__["ProjectArtifactId"]
            break
    assert isinstance(descriptor, property)



def test_psm_dockercontainerport_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerPort)


def test_psm_dockercontainerport_constructor_exists():
    assert callable(PSM_DockerContainerPort.__init__)


def test_psm_dockercontainerport_constructor_args():
    sig = inspect.signature(PSM_DockerContainerPort.__init__)
    params = list(sig.parameters.keys())
    assert "ExposesPortsField" in params, "Missing parameter 'ExposesPortsField'"

def test_psm_dockercontainerport_has_ExposesPortsField():
    assert hasattr(PSM_DockerContainerPort, "ExposesPortsField")
    descriptor = None
    for klass in PSM_DockerContainerPort.__mro__:
        if "ExposesPortsField" in klass.__dict__:
            descriptor = klass.__dict__["ExposesPortsField"]
            break
    assert isinstance(descriptor, property)



def test_psm_dockercontainerlink_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerLink)


def test_psm_dockercontainerlink_constructor_exists():
    assert callable(PSM_DockerContainerLink.__init__)


def test_psm_dockercontainerlink_constructor_args():
    sig = inspect.signature(PSM_DockerContainerLink.__init__)
    params = list(sig.parameters.keys())
    assert "DependencyOrder" in params, "Missing parameter 'DependencyOrder'"
    assert "LinksDependsOnField" in params, "Missing parameter 'LinksDependsOnField'"

def test_psm_dockercontainerlink_has_DependencyOrder():
    assert hasattr(PSM_DockerContainerLink, "DependencyOrder")
    descriptor = None
    for klass in PSM_DockerContainerLink.__mro__:
        if "DependencyOrder" in klass.__dict__:
            descriptor = klass.__dict__["DependencyOrder"]
            break
    assert isinstance(descriptor, property)

def test_psm_dockercontainerlink_has_LinksDependsOnField():
    assert hasattr(PSM_DockerContainerLink, "LinksDependsOnField")
    descriptor = None
    for klass in PSM_DockerContainerLink.__mro__:
        if "LinksDependsOnField" in klass.__dict__:
            descriptor = klass.__dict__["LinksDependsOnField"]
            break
    assert isinstance(descriptor, property)



def test_psm_applicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_ApplicationProject)


def test_psm_applicationproject_constructor_exists():
    assert callable(PSM_ApplicationProject.__init__)


def test_psm_applicationproject_constructor_args():
    sig = inspect.signature(PSM_ApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"

def test_psm_applicationproject_has_ProjectArtifactId():
    assert hasattr(PSM_ApplicationProject, "ProjectArtifactId")
    descriptor = None
    for klass in PSM_ApplicationProject.__mro__:
        if "ProjectArtifactId" in klass.__dict__:
            descriptor = klass.__dict__["ProjectArtifactId"]
            break
    assert isinstance(descriptor, property)



def test_psm_dockercontainerdefinition_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerDefinition)


def test_psm_dockercontainerdefinition_constructor_exists():
    assert callable(PSM_DockerContainerDefinition.__init__)


def test_psm_dockercontainerdefinition_constructor_args():
    sig = inspect.signature(PSM_DockerContainerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "ImageField" in params, "Missing parameter 'ImageField'"
    assert "GeneratesLogs" in params, "Missing parameter 'GeneratesLogs'"
    assert "ContainerName" in params, "Missing parameter 'ContainerName'"
    assert "BuildField" in params, "Missing parameter 'BuildField'"

def test_psm_dockercontainerdefinition_has_ImageField():
    assert hasattr(PSM_DockerContainerDefinition, "ImageField")
    descriptor = None
    for klass in PSM_DockerContainerDefinition.__mro__:
        if "ImageField" in klass.__dict__:
            descriptor = klass.__dict__["ImageField"]
            break
    assert isinstance(descriptor, property)

def test_psm_dockercontainerdefinition_has_GeneratesLogs():
    assert hasattr(PSM_DockerContainerDefinition, "GeneratesLogs")
    descriptor = None
    for klass in PSM_DockerContainerDefinition.__mro__:
        if "GeneratesLogs" in klass.__dict__:
            descriptor = klass.__dict__["GeneratesLogs"]
            break
    assert isinstance(descriptor, property)

def test_psm_dockercontainerdefinition_has_ContainerName():
    assert hasattr(PSM_DockerContainerDefinition, "ContainerName")
    descriptor = None
    for klass in PSM_DockerContainerDefinition.__mro__:
        if "ContainerName" in klass.__dict__:
            descriptor = klass.__dict__["ContainerName"]
            break
    assert isinstance(descriptor, property)

def test_psm_dockercontainerdefinition_has_BuildField():
    assert hasattr(PSM_DockerContainerDefinition, "BuildField")
    descriptor = None
    for klass in PSM_DockerContainerDefinition.__mro__:
        if "BuildField" in klass.__dict__:
            descriptor = klass.__dict__["BuildField"]
            break
    assert isinstance(descriptor, property)



def test_psm_distributedapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_DistributedApplicationProject)


def test_psm_distributedapplicationproject_constructor_exists():
    assert callable(PSM_DistributedApplicationProject.__init__)


def test_psm_distributedapplicationproject_constructor_args():
    sig = inspect.signature(PSM_DistributedApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ApplicationName" in params, "Missing parameter 'ApplicationName'"
    assert "ProjectPackageURL" in params, "Missing parameter 'ProjectPackageURL'"

def test_psm_distributedapplicationproject_has_ApplicationName():
    assert hasattr(PSM_DistributedApplicationProject, "ApplicationName")
    descriptor = None
    for klass in PSM_DistributedApplicationProject.__mro__:
        if "ApplicationName" in klass.__dict__:
            descriptor = klass.__dict__["ApplicationName"]
            break
    assert isinstance(descriptor, property)

def test_psm_distributedapplicationproject_has_ProjectPackageURL():
    assert hasattr(PSM_DistributedApplicationProject, "ProjectPackageURL")
    descriptor = None
    for klass in PSM_DistributedApplicationProject.__mro__:
        if "ProjectPackageURL" in klass.__dict__:
            descriptor = klass.__dict__["ProjectPackageURL"]
            break
    assert isinstance(descriptor, property)



def test_psm_rootpsm_is_not_abstract():
    assert not inspect.isabstract(PSM_RootPSM)


def test_psm_rootpsm_constructor_exists():
    assert callable(PSM_RootPSM.__init__)


def test_psm_rootpsm_constructor_args():
    sig = inspect.signature(PSM_RootPSM.__init__)
    params = list(sig.parameters.keys())



def test_psm_artifactelement_is_not_abstract():
    assert not inspect.isabstract(PSM_ArtifactElement)


def test_psm_artifactelement_constructor_exists():
    assert callable(PSM_ArtifactElement.__init__)


def test_psm_artifactelement_constructor_args():
    sig = inspect.signature(PSM_ArtifactElement.__init__)
    params = list(sig.parameters.keys())
    assert "GeneratingLinesOfCode" in params, "Missing parameter 'GeneratingLinesOfCode'"
    assert "ParentProjectName" in params, "Missing parameter 'ParentProjectName'"
    assert "ArtifactFileName" in params, "Missing parameter 'ArtifactFileName'"

def test_psm_artifactelement_has_GeneratingLinesOfCode():
    assert hasattr(PSM_ArtifactElement, "GeneratingLinesOfCode")
    descriptor = None
    for klass in PSM_ArtifactElement.__mro__:
        if "GeneratingLinesOfCode" in klass.__dict__:
            descriptor = klass.__dict__["GeneratingLinesOfCode"]
            break
    assert isinstance(descriptor, property)

def test_psm_artifactelement_has_ParentProjectName():
    assert hasattr(PSM_ArtifactElement, "ParentProjectName")
    descriptor = None
    for klass in PSM_ArtifactElement.__mro__:
        if "ParentProjectName" in klass.__dict__:
            descriptor = klass.__dict__["ParentProjectName"]
            break
    assert isinstance(descriptor, property)

def test_psm_artifactelement_has_ArtifactFileName():
    assert hasattr(PSM_ArtifactElement, "ArtifactFileName")
    descriptor = None
    for klass in PSM_ArtifactElement.__mro__:
        if "ArtifactFileName" in klass.__dict__:
            descriptor = klass.__dict__["ArtifactFileName"]
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
PSM_JavaInterfaceType_strategy = st.builds(
    PSM_JavaInterfaceType,
)
PSM_JavaClassType_strategy = st.builds(
    PSM_JavaClassType,
)
JavaDataField_strategy = st.builds(
    JavaDataField,
)
PSM_JavaMethodParameter_strategy = st.builds(
    PSM_JavaMethodParameter,
    ParameterOrder=
        st.integers()
)
SpringWebApplicationLayer_strategy = st.builds(
    SpringWebApplicationLayer,
)
PSM_SpringBootApplicationLayer_strategy = st.builds(
    PSM_SpringBootApplicationLayer,
)
JavaDataType_strategy = st.builds(
    JavaDataType,
)
PSM_JavaUserDefinedType_strategy = st.builds(
    PSM_JavaUserDefinedType,
)
JavaElement_strategy = st.builds(
    JavaElement,
)
PSM_JavaDataField_strategy = st.builds(
    PSM_JavaDataField,
    FieldValue=
        safe_text
)
PSM_JavaMethod_strategy = st.builds(
    PSM_JavaMethod,
    RootCallingMethod=
        safe_text
)
PSM_JavaDataType_strategy = st.builds(
    PSM_JavaDataType,
    PackageName=
        safe_text,
    IsPrimitive=
        st.booleans(),
    JsonSchema=
        safe_text
)
PSM_SpringModelPojoLayer_strategy = st.builds(
    PSM_SpringModelPojoLayer,
)
PSM_SpringDomainLayer_strategy = st.builds(
    PSM_SpringDomainLayer,
)
PSM_SpringRepositoryLayer_strategy = st.builds(
    PSM_SpringRepositoryLayer,
)
PSM_SpringComponentLayer_strategy = st.builds(
    PSM_SpringComponentLayer,
)
PSM_SpringFeignClientLayer_strategy = st.builds(
    PSM_SpringFeignClientLayer,
)
PSM_SpringConfigurationLayer_strategy = st.builds(
    PSM_SpringConfigurationLayer,
)
PSM_SpringServiceLayer_strategy = st.builds(
    PSM_SpringServiceLayer,
)
PSM_SpringControllerLayer_strategy = st.builds(
    PSM_SpringControllerLayer,
)
ArtifactElement_strategy = st.builds(
    ArtifactElement,
)
PSM_JavaElement_strategy = st.builds(
    PSM_JavaElement,
    ElementIdentifier=
        safe_text,
    ElementProfile=
        safe_text
)
PSM_JavaAnnotationParameter_strategy = st.builds(
    PSM_JavaAnnotationParameter,
    ParameterName=
        safe_text,
    ParameterValue=
        safe_text
)
PSM_JavaAnnotation_strategy = st.builds(
    PSM_JavaAnnotation,
    AnnotationName=
        safe_text
)
JavaSpringWebApplicationProject_strategy = st.builds(
    JavaSpringWebApplicationProject,
)
PSM_JavaSpringMVCApplicationProject_strategy = st.builds(
    PSM_JavaSpringMVCApplicationProject,
)
PSM_JavaSpringWebFluxApplicationProject_strategy = st.builds(
    PSM_JavaSpringWebFluxApplicationProject,
)
PSM_SpringWebApplicationLayer_strategy = st.builds(
    PSM_SpringWebApplicationLayer,
    LayerName=
        safe_text
)
PSM_ConfigurationProperty_strategy = st.builds(
    PSM_ConfigurationProperty,
    PropertyValue=
        safe_text,
    ConfigurationProfile=
        safe_text,
    FullyQualifiedPropertyName=
        safe_text
)
MicroserviceProject_strategy = st.builds(
    MicroserviceProject,
)
PSM_JavaSpringWebApplicationProject_strategy = st.builds(
    PSM_JavaSpringWebApplicationProject,
)
PSM_DependencyLibrary_strategy = st.builds(
    PSM_DependencyLibrary,
    LibraryName=
        safe_text,
    LibraryScope=
        safe_text,
    LibraryGroupName=
        safe_text
)
PSM_MicroserviceProject_strategy = st.builds(
    PSM_MicroserviceProject,
    ProjectArtifactId=
        safe_text
)
PSM_DockerContainerPort_strategy = st.builds(
    PSM_DockerContainerPort,
    ExposesPortsField=
        safe_text
)
PSM_DockerContainerLink_strategy = st.builds(
    PSM_DockerContainerLink,
    DependencyOrder=
        st.integers(),
    LinksDependsOnField=
        safe_text
)
PSM_ApplicationProject_strategy = st.builds(
    PSM_ApplicationProject,
    ProjectArtifactId=
        safe_text
)
PSM_DockerContainerDefinition_strategy = st.builds(
    PSM_DockerContainerDefinition,
    ImageField=
        safe_text,
    GeneratesLogs=
        st.booleans(),
    ContainerName=
        safe_text,
    BuildField=
        safe_text
)
PSM_DistributedApplicationProject_strategy = st.builds(
    PSM_DistributedApplicationProject,
    ApplicationName=
        safe_text,
    ProjectPackageURL=
        safe_text
)
PSM_RootPSM_strategy = st.builds(
    PSM_RootPSM,
)
PSM_ArtifactElement_strategy = st.builds(
    PSM_ArtifactElement,
    GeneratingLinesOfCode=
        safe_text,
    ParentProjectName=
        safe_text,
    ArtifactFileName=
        safe_text
)

@given(instance=JavaUserDefinedType_strategy)
@settings(max_examples=50)
def test_javauserdefinedtype_instantiation(instance):
    assert isinstance(instance, JavaUserDefinedType)

@given(instance=PSM_JavaInterfaceType_strategy)
@settings(max_examples=50)
def test_psm_javainterfacetype_instantiation(instance):
    assert isinstance(instance, PSM_JavaInterfaceType)

@given(instance=PSM_JavaClassType_strategy)
@settings(max_examples=50)
def test_psm_javaclasstype_instantiation(instance):
    assert isinstance(instance, PSM_JavaClassType)

@given(instance=JavaDataField_strategy)
@settings(max_examples=50)
def test_javadatafield_instantiation(instance):
    assert isinstance(instance, JavaDataField)

@given(instance=PSM_JavaMethodParameter_strategy)
@settings(max_examples=50)
def test_psm_javamethodparameter_instantiation(instance):
    assert isinstance(instance, PSM_JavaMethodParameter)



@given(instance=PSM_JavaMethodParameter_strategy)
def test_psm_javamethodparameter_ParameterOrder_setter(instance):
    original = instance.ParameterOrder
    instance.ParameterOrder = original
    assert instance.ParameterOrder == original

@given(instance=SpringWebApplicationLayer_strategy)
@settings(max_examples=50)
def test_springwebapplicationlayer_instantiation(instance):
    assert isinstance(instance, SpringWebApplicationLayer)

@given(instance=PSM_SpringBootApplicationLayer_strategy)
@settings(max_examples=50)
def test_psm_springbootapplicationlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringBootApplicationLayer)

@given(instance=JavaDataType_strategy)
@settings(max_examples=50)
def test_javadatatype_instantiation(instance):
    assert isinstance(instance, JavaDataType)

@given(instance=PSM_JavaUserDefinedType_strategy)
@settings(max_examples=50)
def test_psm_javauserdefinedtype_instantiation(instance):
    assert isinstance(instance, PSM_JavaUserDefinedType)

@given(instance=JavaElement_strategy)
@settings(max_examples=50)
def test_javaelement_instantiation(instance):
    assert isinstance(instance, JavaElement)

@given(instance=PSM_JavaDataField_strategy)
@settings(max_examples=50)
def test_psm_javadatafield_instantiation(instance):
    assert isinstance(instance, PSM_JavaDataField)



@given(instance=PSM_JavaDataField_strategy)
def test_psm_javadatafield_FieldValue_setter(instance):
    original = instance.FieldValue
    instance.FieldValue = original
    assert instance.FieldValue == original

@given(instance=PSM_JavaMethod_strategy)
@settings(max_examples=50)
def test_psm_javamethod_instantiation(instance):
    assert isinstance(instance, PSM_JavaMethod)



@given(instance=PSM_JavaMethod_strategy)
def test_psm_javamethod_RootCallingMethod_setter(instance):
    original = instance.RootCallingMethod
    instance.RootCallingMethod = original
    assert instance.RootCallingMethod == original

@given(instance=PSM_JavaDataType_strategy)
@settings(max_examples=50)
def test_psm_javadatatype_instantiation(instance):
    assert isinstance(instance, PSM_JavaDataType)



@given(instance=PSM_JavaDataType_strategy)
def test_psm_javadatatype_PackageName_setter(instance):
    original = instance.PackageName
    instance.PackageName = original
    assert instance.PackageName == original



@given(instance=PSM_JavaDataType_strategy)
def test_psm_javadatatype_IsPrimitive_setter(instance):
    original = instance.IsPrimitive
    instance.IsPrimitive = original
    assert instance.IsPrimitive == original



@given(instance=PSM_JavaDataType_strategy)
def test_psm_javadatatype_JsonSchema_setter(instance):
    original = instance.JsonSchema
    instance.JsonSchema = original
    assert instance.JsonSchema == original

@given(instance=PSM_SpringModelPojoLayer_strategy)
@settings(max_examples=50)
def test_psm_springmodelpojolayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringModelPojoLayer)

@given(instance=PSM_SpringDomainLayer_strategy)
@settings(max_examples=50)
def test_psm_springdomainlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringDomainLayer)

@given(instance=PSM_SpringRepositoryLayer_strategy)
@settings(max_examples=50)
def test_psm_springrepositorylayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringRepositoryLayer)

@given(instance=PSM_SpringComponentLayer_strategy)
@settings(max_examples=50)
def test_psm_springcomponentlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringComponentLayer)

@given(instance=PSM_SpringFeignClientLayer_strategy)
@settings(max_examples=50)
def test_psm_springfeignclientlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringFeignClientLayer)

@given(instance=PSM_SpringConfigurationLayer_strategy)
@settings(max_examples=50)
def test_psm_springconfigurationlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringConfigurationLayer)

@given(instance=PSM_SpringServiceLayer_strategy)
@settings(max_examples=50)
def test_psm_springservicelayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringServiceLayer)

@given(instance=PSM_SpringControllerLayer_strategy)
@settings(max_examples=50)
def test_psm_springcontrollerlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringControllerLayer)

@given(instance=ArtifactElement_strategy)
@settings(max_examples=50)
def test_artifactelement_instantiation(instance):
    assert isinstance(instance, ArtifactElement)

@given(instance=PSM_JavaElement_strategy)
@settings(max_examples=50)
def test_psm_javaelement_instantiation(instance):
    assert isinstance(instance, PSM_JavaElement)



@given(instance=PSM_JavaElement_strategy)
def test_psm_javaelement_ElementIdentifier_setter(instance):
    original = instance.ElementIdentifier
    instance.ElementIdentifier = original
    assert instance.ElementIdentifier == original



@given(instance=PSM_JavaElement_strategy)
def test_psm_javaelement_ElementProfile_setter(instance):
    original = instance.ElementProfile
    instance.ElementProfile = original
    assert instance.ElementProfile == original

@given(instance=PSM_JavaAnnotationParameter_strategy)
@settings(max_examples=50)
def test_psm_javaannotationparameter_instantiation(instance):
    assert isinstance(instance, PSM_JavaAnnotationParameter)



@given(instance=PSM_JavaAnnotationParameter_strategy)
def test_psm_javaannotationparameter_ParameterName_setter(instance):
    original = instance.ParameterName
    instance.ParameterName = original
    assert instance.ParameterName == original



@given(instance=PSM_JavaAnnotationParameter_strategy)
def test_psm_javaannotationparameter_ParameterValue_setter(instance):
    original = instance.ParameterValue
    instance.ParameterValue = original
    assert instance.ParameterValue == original

@given(instance=PSM_JavaAnnotation_strategy)
@settings(max_examples=50)
def test_psm_javaannotation_instantiation(instance):
    assert isinstance(instance, PSM_JavaAnnotation)



@given(instance=PSM_JavaAnnotation_strategy)
def test_psm_javaannotation_AnnotationName_setter(instance):
    original = instance.AnnotationName
    instance.AnnotationName = original
    assert instance.AnnotationName == original

@given(instance=JavaSpringWebApplicationProject_strategy)
@settings(max_examples=50)
def test_javaspringwebapplicationproject_instantiation(instance):
    assert isinstance(instance, JavaSpringWebApplicationProject)

@given(instance=PSM_JavaSpringMVCApplicationProject_strategy)
@settings(max_examples=50)
def test_psm_javaspringmvcapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringMVCApplicationProject)

@given(instance=PSM_JavaSpringWebFluxApplicationProject_strategy)
@settings(max_examples=50)
def test_psm_javaspringwebfluxapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringWebFluxApplicationProject)

@given(instance=PSM_SpringWebApplicationLayer_strategy)
@settings(max_examples=50)
def test_psm_springwebapplicationlayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringWebApplicationLayer)



@given(instance=PSM_SpringWebApplicationLayer_strategy)
def test_psm_springwebapplicationlayer_LayerName_setter(instance):
    original = instance.LayerName
    instance.LayerName = original
    assert instance.LayerName == original

@given(instance=PSM_ConfigurationProperty_strategy)
@settings(max_examples=50)
def test_psm_configurationproperty_instantiation(instance):
    assert isinstance(instance, PSM_ConfigurationProperty)



@given(instance=PSM_ConfigurationProperty_strategy)
def test_psm_configurationproperty_PropertyValue_setter(instance):
    original = instance.PropertyValue
    instance.PropertyValue = original
    assert instance.PropertyValue == original



@given(instance=PSM_ConfigurationProperty_strategy)
def test_psm_configurationproperty_ConfigurationProfile_setter(instance):
    original = instance.ConfigurationProfile
    instance.ConfigurationProfile = original
    assert instance.ConfigurationProfile == original



@given(instance=PSM_ConfigurationProperty_strategy)
def test_psm_configurationproperty_FullyQualifiedPropertyName_setter(instance):
    original = instance.FullyQualifiedPropertyName
    instance.FullyQualifiedPropertyName = original
    assert instance.FullyQualifiedPropertyName == original

@given(instance=MicroserviceProject_strategy)
@settings(max_examples=50)
def test_microserviceproject_instantiation(instance):
    assert isinstance(instance, MicroserviceProject)

@given(instance=PSM_JavaSpringWebApplicationProject_strategy)
@settings(max_examples=50)
def test_psm_javaspringwebapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringWebApplicationProject)

@given(instance=PSM_DependencyLibrary_strategy)
@settings(max_examples=50)
def test_psm_dependencylibrary_instantiation(instance):
    assert isinstance(instance, PSM_DependencyLibrary)



@given(instance=PSM_DependencyLibrary_strategy)
def test_psm_dependencylibrary_LibraryName_setter(instance):
    original = instance.LibraryName
    instance.LibraryName = original
    assert instance.LibraryName == original



@given(instance=PSM_DependencyLibrary_strategy)
def test_psm_dependencylibrary_LibraryScope_setter(instance):
    original = instance.LibraryScope
    instance.LibraryScope = original
    assert instance.LibraryScope == original



@given(instance=PSM_DependencyLibrary_strategy)
def test_psm_dependencylibrary_LibraryGroupName_setter(instance):
    original = instance.LibraryGroupName
    instance.LibraryGroupName = original
    assert instance.LibraryGroupName == original

@given(instance=PSM_MicroserviceProject_strategy)
@settings(max_examples=50)
def test_psm_microserviceproject_instantiation(instance):
    assert isinstance(instance, PSM_MicroserviceProject)



@given(instance=PSM_MicroserviceProject_strategy)
def test_psm_microserviceproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original

@given(instance=PSM_DockerContainerPort_strategy)
@settings(max_examples=50)
def test_psm_dockercontainerport_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerPort)



@given(instance=PSM_DockerContainerPort_strategy)
def test_psm_dockercontainerport_ExposesPortsField_setter(instance):
    original = instance.ExposesPortsField
    instance.ExposesPortsField = original
    assert instance.ExposesPortsField == original

@given(instance=PSM_DockerContainerLink_strategy)
@settings(max_examples=50)
def test_psm_dockercontainerlink_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerLink)



@given(instance=PSM_DockerContainerLink_strategy)
def test_psm_dockercontainerlink_DependencyOrder_setter(instance):
    original = instance.DependencyOrder
    instance.DependencyOrder = original
    assert instance.DependencyOrder == original



@given(instance=PSM_DockerContainerLink_strategy)
def test_psm_dockercontainerlink_LinksDependsOnField_setter(instance):
    original = instance.LinksDependsOnField
    instance.LinksDependsOnField = original
    assert instance.LinksDependsOnField == original

@given(instance=PSM_ApplicationProject_strategy)
@settings(max_examples=50)
def test_psm_applicationproject_instantiation(instance):
    assert isinstance(instance, PSM_ApplicationProject)



@given(instance=PSM_ApplicationProject_strategy)
def test_psm_applicationproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original

@given(instance=PSM_DockerContainerDefinition_strategy)
@settings(max_examples=50)
def test_psm_dockercontainerdefinition_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerDefinition)



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_psm_dockercontainerdefinition_ImageField_setter(instance):
    original = instance.ImageField
    instance.ImageField = original
    assert instance.ImageField == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_psm_dockercontainerdefinition_GeneratesLogs_setter(instance):
    original = instance.GeneratesLogs
    instance.GeneratesLogs = original
    assert instance.GeneratesLogs == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_psm_dockercontainerdefinition_ContainerName_setter(instance):
    original = instance.ContainerName
    instance.ContainerName = original
    assert instance.ContainerName == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_psm_dockercontainerdefinition_BuildField_setter(instance):
    original = instance.BuildField
    instance.BuildField = original
    assert instance.BuildField == original

@given(instance=PSM_DistributedApplicationProject_strategy)
@settings(max_examples=50)
def test_psm_distributedapplicationproject_instantiation(instance):
    assert isinstance(instance, PSM_DistributedApplicationProject)



@given(instance=PSM_DistributedApplicationProject_strategy)
def test_psm_distributedapplicationproject_ApplicationName_setter(instance):
    original = instance.ApplicationName
    instance.ApplicationName = original
    assert instance.ApplicationName == original



@given(instance=PSM_DistributedApplicationProject_strategy)
def test_psm_distributedapplicationproject_ProjectPackageURL_setter(instance):
    original = instance.ProjectPackageURL
    instance.ProjectPackageURL = original
    assert instance.ProjectPackageURL == original

@given(instance=PSM_RootPSM_strategy)
@settings(max_examples=50)
def test_psm_rootpsm_instantiation(instance):
    assert isinstance(instance, PSM_RootPSM)

@given(instance=PSM_ArtifactElement_strategy)
@settings(max_examples=50)
def test_psm_artifactelement_instantiation(instance):
    assert isinstance(instance, PSM_ArtifactElement)



@given(instance=PSM_ArtifactElement_strategy)
def test_psm_artifactelement_GeneratingLinesOfCode_setter(instance):
    original = instance.GeneratingLinesOfCode
    instance.GeneratingLinesOfCode = original
    assert instance.GeneratingLinesOfCode == original



@given(instance=PSM_ArtifactElement_strategy)
def test_psm_artifactelement_ParentProjectName_setter(instance):
    original = instance.ParentProjectName
    instance.ParentProjectName = original
    assert instance.ParentProjectName == original



@given(instance=PSM_ArtifactElement_strategy)
def test_psm_artifactelement_ArtifactFileName_setter(instance):
    original = instance.ArtifactFileName
    instance.ArtifactFileName = original
    assert instance.ArtifactFileName == original
