####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
PSM_ArtifactElement = Class(name="PSM::ArtifactElement")
ArtifactElement = Class(name="ArtifactElement")
PSM_DockerContainerLink = Class(name="PSM::DockerContainerLink")
PSM_RootPSM = Class(name="PSM::RootPSM")
PSM_DistributedApplicationProject = Class(name="PSM::DistributedApplicationProject")
PSM_DockerContainerDefinition = Class(name="PSM::DockerContainerDefinition")
PSM_ApplicationProject = Class(name="PSM::ApplicationProject")
PSM_MicroserviceProject = Class(name="PSM::MicroserviceProject")
PSM_DockerContainerPort = Class(name="PSM::DockerContainerPort")
PSM_JavaSpringWebApplicationProject = Class(name="PSM::JavaSpringWebApplicationProject")
MicroserviceProject = Class(name="MicroserviceProject")
PSM_ConfigurationProperty = Class(name="PSM::ConfigurationProperty")
PSM_DependencyLibrary = Class(name="PSM::DependencyLibrary")
PSM_JavaUserDefinedType = Class(name="PSM::JavaUserDefinedType")
PSM_SpringBootApplicationLayer = Class(name="PSM::SpringBootApplicationLayer")
SpringWebApplicationLayer = Class(name="SpringWebApplicationLayer")
PSM_SpringControllerLayer = Class(name="PSM::SpringControllerLayer")
PSM_SpringServiceLayer = Class(name="PSM::SpringServiceLayer")
PSM_SpringConfigurationLayer = Class(name="PSM::SpringConfigurationLayer")
PSM_SpringFeignClientLayer = Class(name="PSM::SpringFeignClientLayer")
PSM_SpringComponentLayer = Class(name="PSM::SpringComponentLayer")
PSM_SpringWebApplicationLayer = Class(name="PSM::SpringWebApplicationLayer")
PSM_JavaSpringWebFluxApplicationProject = Class(name="PSM::JavaSpringWebFluxApplicationProject")
JavaSpringWebApplicationProject = Class(name="JavaSpringWebApplicationProject")
PSM_JavaSpringMVCApplicationProject = Class(name="PSM::JavaSpringMVCApplicationProject")
PSM_JavaDataType = Class(name="PSM::JavaDataType")
JavaElement = Class(name="JavaElement")
JavaDataType = Class(name="JavaDataType")
PSM_JavaMethod = Class(name="PSM::JavaMethod")
PSM_SpringRepositoryLayer = Class(name="PSM::SpringRepositoryLayer")
PSM_SpringDomainLayer = Class(name="PSM::SpringDomainLayer")
PSM_SpringModelPojoLayer = Class(name="PSM::SpringModelPojoLayer")
PSM_JavaElement = Class(name="PSM::JavaElement")
PSM_JavaAnnotation = Class(name="PSM::JavaAnnotation")
PSM_JavaAnnotationParameter = Class(name="PSM::JavaAnnotationParameter")
PSM_JavaInterfaceType = Class(name="PSM::JavaInterfaceType")
PSM_JavaMethodParameter = Class(name="PSM::JavaMethodParameter")
PSM_JavaDataField = Class(name="PSM::JavaDataField")
PSM_JavaClassType = Class(name="PSM::JavaClassType")
JavaUserDefinedType = Class(name="JavaUserDefinedType")
JavaDataField = Class(name="JavaDataField")

# PSM_ArtifactElement class attributes and methods
PSM_ArtifactElement_ParentProjectName: Property = Property(name="ParentProjectName", type=StringType)
PSM_ArtifactElement_ArtifactFileName: Property = Property(name="ArtifactFileName", type=StringType)
PSM_ArtifactElement_GeneratingLinesOfCode: Property = Property(name="GeneratingLinesOfCode", type=StringType)
PSM_ArtifactElement.attributes={PSM_ArtifactElement_GeneratingLinesOfCode, PSM_ArtifactElement_ArtifactFileName, PSM_ArtifactElement_ParentProjectName}

# ArtifactElement class attributes and methods

# PSM_DockerContainerLink class attributes and methods
PSM_DockerContainerLink_DependencyOrder: Property = Property(name="DependencyOrder", type=IntegerType)
PSM_DockerContainerLink_LinksDependsOnField: Property = Property(name="LinksDependsOnField", type=StringType)
PSM_DockerContainerLink.attributes={PSM_DockerContainerLink_DependencyOrder, PSM_DockerContainerLink_LinksDependsOnField}

# PSM_RootPSM class attributes and methods

# PSM_DistributedApplicationProject class attributes and methods
PSM_DistributedApplicationProject_ApplicationName: Property = Property(name="ApplicationName", type=StringType)
PSM_DistributedApplicationProject_ProjectPackageURL: Property = Property(name="ProjectPackageURL", type=StringType)
PSM_DistributedApplicationProject.attributes={PSM_DistributedApplicationProject_ApplicationName, PSM_DistributedApplicationProject_ProjectPackageURL}

# PSM_DockerContainerDefinition class attributes and methods
PSM_DockerContainerDefinition_ContainerName: Property = Property(name="ContainerName", type=StringType)
PSM_DockerContainerDefinition_GeneratesLogs: Property = Property(name="GeneratesLogs", type=BooleanType)
PSM_DockerContainerDefinition_ImageField: Property = Property(name="ImageField", type=StringType)
PSM_DockerContainerDefinition_BuildField: Property = Property(name="BuildField", type=StringType)
PSM_DockerContainerDefinition.attributes={PSM_DockerContainerDefinition_GeneratesLogs, PSM_DockerContainerDefinition_BuildField, PSM_DockerContainerDefinition_ImageField, PSM_DockerContainerDefinition_ContainerName}

# PSM_ApplicationProject class attributes and methods
PSM_ApplicationProject_ProjectArtifactId: Property = Property(name="ProjectArtifactId", type=StringType)
PSM_ApplicationProject.attributes={PSM_ApplicationProject_ProjectArtifactId}

# PSM_MicroserviceProject class attributes and methods
PSM_MicroserviceProject_ProjectArtifactId: Property = Property(name="ProjectArtifactId", type=StringType)
PSM_MicroserviceProject.attributes={PSM_MicroserviceProject_ProjectArtifactId}

# PSM_DockerContainerPort class attributes and methods
PSM_DockerContainerPort_ExposesPortsField: Property = Property(name="ExposesPortsField", type=StringType)
PSM_DockerContainerPort.attributes={PSM_DockerContainerPort_ExposesPortsField}

# PSM_JavaSpringWebApplicationProject class attributes and methods

# MicroserviceProject class attributes and methods

# PSM_ConfigurationProperty class attributes and methods
PSM_ConfigurationProperty_FullyQualifiedPropertyName: Property = Property(name="FullyQualifiedPropertyName", type=StringType)
PSM_ConfigurationProperty_PropertyValue: Property = Property(name="PropertyValue", type=StringType)
PSM_ConfigurationProperty_ConfigurationProfile: Property = Property(name="ConfigurationProfile", type=StringType)
PSM_ConfigurationProperty.attributes={PSM_ConfigurationProperty_ConfigurationProfile, PSM_ConfigurationProperty_PropertyValue, PSM_ConfigurationProperty_FullyQualifiedPropertyName}

# PSM_DependencyLibrary class attributes and methods
PSM_DependencyLibrary_LibraryName: Property = Property(name="LibraryName", type=StringType)
PSM_DependencyLibrary_LibraryScope: Property = Property(name="LibraryScope", type=StringType)
PSM_DependencyLibrary_LibraryGroupName: Property = Property(name="LibraryGroupName", type=StringType)
PSM_DependencyLibrary.attributes={PSM_DependencyLibrary_LibraryScope, PSM_DependencyLibrary_LibraryGroupName, PSM_DependencyLibrary_LibraryName}

# PSM_JavaUserDefinedType class attributes and methods

# PSM_SpringBootApplicationLayer class attributes and methods

# SpringWebApplicationLayer class attributes and methods

# PSM_SpringControllerLayer class attributes and methods

# PSM_SpringServiceLayer class attributes and methods

# PSM_SpringConfigurationLayer class attributes and methods

# PSM_SpringFeignClientLayer class attributes and methods

# PSM_SpringComponentLayer class attributes and methods

# PSM_SpringWebApplicationLayer class attributes and methods
PSM_SpringWebApplicationLayer_LayerName: Property = Property(name="LayerName", type=StringType)
PSM_SpringWebApplicationLayer.attributes={PSM_SpringWebApplicationLayer_LayerName}

# PSM_JavaSpringWebFluxApplicationProject class attributes and methods

# JavaSpringWebApplicationProject class attributes and methods

# PSM_JavaSpringMVCApplicationProject class attributes and methods

# PSM_JavaDataType class attributes and methods
PSM_JavaDataType_IsPrimitive: Property = Property(name="IsPrimitive", type=BooleanType)
PSM_JavaDataType_JsonSchema: Property = Property(name="JsonSchema", type=StringType)
PSM_JavaDataType_PackageName: Property = Property(name="PackageName", type=StringType)
PSM_JavaDataType.attributes={PSM_JavaDataType_PackageName, PSM_JavaDataType_JsonSchema, PSM_JavaDataType_IsPrimitive}

# JavaElement class attributes and methods

# JavaDataType class attributes and methods

# PSM_JavaMethod class attributes and methods
PSM_JavaMethod_RootCallingMethod: Property = Property(name="RootCallingMethod", type=StringType)
PSM_JavaMethod.attributes={PSM_JavaMethod_RootCallingMethod}

# PSM_SpringRepositoryLayer class attributes and methods

# PSM_SpringDomainLayer class attributes and methods

# PSM_SpringModelPojoLayer class attributes and methods

# PSM_JavaElement class attributes and methods
PSM_JavaElement_ElementIdentifier: Property = Property(name="ElementIdentifier", type=StringType)
PSM_JavaElement_ElementProfile: Property = Property(name="ElementProfile", type=StringType)
PSM_JavaElement.attributes={PSM_JavaElement_ElementIdentifier, PSM_JavaElement_ElementProfile}

# PSM_JavaAnnotation class attributes and methods
PSM_JavaAnnotation_AnnotationName: Property = Property(name="AnnotationName", type=StringType)
PSM_JavaAnnotation.attributes={PSM_JavaAnnotation_AnnotationName}

# PSM_JavaAnnotationParameter class attributes and methods
PSM_JavaAnnotationParameter_ParameterName: Property = Property(name="ParameterName", type=StringType)
PSM_JavaAnnotationParameter_ParameterValue: Property = Property(name="ParameterValue", type=StringType)
PSM_JavaAnnotationParameter.attributes={PSM_JavaAnnotationParameter_ParameterValue, PSM_JavaAnnotationParameter_ParameterName}

# PSM_JavaInterfaceType class attributes and methods

# PSM_JavaMethodParameter class attributes and methods
PSM_JavaMethodParameter_ParameterOrder: Property = Property(name="ParameterOrder", type=IntegerType)
PSM_JavaMethodParameter.attributes={PSM_JavaMethodParameter_ParameterOrder}

# PSM_JavaDataField class attributes and methods
PSM_JavaDataField_FieldValue: Property = Property(name="FieldValue", type=StringType)
PSM_JavaDataField.attributes={PSM_JavaDataField_FieldValue}

# PSM_JavaClassType class attributes and methods

# JavaUserDefinedType class attributes and methods

# JavaDataField class attributes and methods

# Relationships
application_project3: BinaryAssociation = BinaryAssociation(
    name="application_project3",
    ends={
        Property(name="PSM_ApplicationProject", type=PSM_DistributedApplicationProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_DistributedApplicationProject4", type=PSM_ApplicationProject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
application0: BinaryAssociation = BinaryAssociation(
    name="application0",
    ends={
        Property(name="PSM_DistributedApplicationProject", type=PSM_RootPSM, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_RootPSM", type=PSM_DistributedApplicationProject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containers1: BinaryAssociation = BinaryAssociation(
    name="containers1",
    ends={
        Property(name="PSM_DockerContainerDefinition", type=PSM_DistributedApplicationProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_DistributedApplicationProject2", type=PSM_DockerContainerDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modules9: BinaryAssociation = BinaryAssociation(
    name="modules9",
    ends={
        Property(name="PSM_MicroserviceProject", type=PSM_ApplicationProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_ApplicationProject10", type=PSM_MicroserviceProject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
links5: BinaryAssociation = BinaryAssociation(
    name="links5",
    ends={
        Property(name="PSM_DockerContainerLink", type=PSM_DockerContainerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_DockerContainerDefinition6", type=PSM_DockerContainerLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports7: BinaryAssociation = BinaryAssociation(
    name="ports7",
    ends={
        Property(name="PSM_DockerContainerPort", type=PSM_DockerContainerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_DockerContainerDefinition8", type=PSM_DockerContainerPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties13: BinaryAssociation = BinaryAssociation(
    name="properties13",
    ends={
        Property(name="PSM_ConfigurationProperty", type=PSM_JavaSpringWebApplicationProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaSpringWebApplicationProject", type=PSM_ConfigurationProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
libraries11: BinaryAssociation = BinaryAssociation(
    name="libraries11",
    ends={
        Property(name="PSM_DependencyLibrary", type=PSM_MicroserviceProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_MicroserviceProject12", type=PSM_DependencyLibrary, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements16: BinaryAssociation = BinaryAssociation(
    name="elements16",
    ends={
        Property(name="PSM_JavaUserDefinedType", type=PSM_SpringWebApplicationLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_SpringWebApplicationLayer17", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
layers14: BinaryAssociation = BinaryAssociation(
    name="layers14",
    ends={
        Property(name="PSM_SpringWebApplicationLayer", type=PSM_JavaSpringWebApplicationProject, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaSpringWebApplicationProject15", type=PSM_SpringWebApplicationLayer, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
parameters19: BinaryAssociation = BinaryAssociation(
    name="parameters19",
    ends={
        Property(name="PSM_JavaAnnotationParameter", type=PSM_JavaAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaAnnotation20", type=PSM_JavaAnnotationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods21: BinaryAssociation = BinaryAssociation(
    name="methods21",
    ends={
        Property(name="PSM_JavaMethod", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaUserDefinedType22", type=PSM_JavaMethod, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
annotations18: BinaryAssociation = BinaryAssociation(
    name="annotations18",
    ends={
        Property(name="PSM_JavaAnnotation", type=PSM_JavaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaElement", type=PSM_JavaAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements34: BinaryAssociation = BinaryAssociation(
    name="implements34",
    ends={
        Property(name="PSM_JavaInterfaceType", type=PSM_JavaClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaClassType", type=PSM_JavaInterfaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent35: BinaryAssociation = BinaryAssociation(
    name="parent35",
    ends={
        Property(name="PSM_JavaUserDefinedType37", type=PSM_JavaMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaMethod36", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters38: BinaryAssociation = BinaryAssociation(
    name="parameters38",
    ends={
        Property(name="PSM_JavaMethodParameter", type=PSM_JavaMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaMethod39", type=PSM_JavaMethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returns40: BinaryAssociation = BinaryAssociation(
    name="returns40",
    ends={
        Property(name="PSM_JavaDataType", type=PSM_JavaMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaMethod41", type=PSM_JavaDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends24: BinaryAssociation = BinaryAssociation(
    name="extends24",
    ends={
        Property(name="PSM_JavaUserDefinedType25", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaUserDefinedType23", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports27: BinaryAssociation = BinaryAssociation(
    name="imports27",
    ends={
        Property(name="PSM_JavaUserDefinedType28", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaUserDefinedType26", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defines30: BinaryAssociation = BinaryAssociation(
    name="defines30",
    ends={
        Property(name="PSM_JavaUserDefinedType31", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaUserDefinedType29", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields32: BinaryAssociation = BinaryAssociation(
    name="fields32",
    ends={
        Property(name="PSM_JavaDataField", type=PSM_JavaUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaUserDefinedType33", type=PSM_JavaDataField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokes43: BinaryAssociation = BinaryAssociation(
    name="invokes43",
    ends={
        Property(name="PSM_JavaMethod44", type=PSM_JavaMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaMethod42", type=PSM_JavaMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="PSM_JavaDataType47", type=PSM_JavaDataField, multiplicity=Multiplicity(1, 1)),
        Property(name="PSM_JavaDataField46", type=PSM_JavaDataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_PSM_DockerContainerDefinition_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_DockerContainerDefinition)
gen_PSM_ApplicationProject_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_ApplicationProject)
gen_PSM_DockerContainerLink_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_DockerContainerLink)
gen_PSM_DockerContainerPort_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_DockerContainerPort)
gen_PSM_JavaSpringWebApplicationProject_MicroserviceProject = Generalization(general=MicroserviceProject, specific=PSM_JavaSpringWebApplicationProject)
gen_PSM_MicroserviceProject_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_MicroserviceProject)
gen_PSM_DependencyLibrary_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_DependencyLibrary)
gen_PSM_SpringBootApplicationLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringBootApplicationLayer)
gen_PSM_SpringControllerLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringControllerLayer)
gen_PSM_SpringServiceLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringServiceLayer)
gen_PSM_SpringConfigurationLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringConfigurationLayer)
gen_PSM_SpringFeignClientLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringFeignClientLayer)
gen_PSM_SpringComponentLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringComponentLayer)
gen_PSM_JavaSpringWebFluxApplicationProject_JavaSpringWebApplicationProject = Generalization(general=JavaSpringWebApplicationProject, specific=PSM_JavaSpringWebFluxApplicationProject)
gen_PSM_JavaSpringMVCApplicationProject_JavaSpringWebApplicationProject = Generalization(general=JavaSpringWebApplicationProject, specific=PSM_JavaSpringMVCApplicationProject)
gen_PSM_ConfigurationProperty_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_ConfigurationProperty)
gen_PSM_SpringWebApplicationLayer_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_SpringWebApplicationLayer)
gen_PSM_JavaAnnotationParameter_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_JavaAnnotationParameter)
gen_PSM_JavaDataType_JavaElement = Generalization(general=JavaElement, specific=PSM_JavaDataType)
gen_PSM_JavaUserDefinedType_JavaDataType = Generalization(general=JavaDataType, specific=PSM_JavaUserDefinedType)
gen_PSM_SpringRepositoryLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringRepositoryLayer)
gen_PSM_SpringDomainLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringDomainLayer)
gen_PSM_SpringModelPojoLayer_SpringWebApplicationLayer = Generalization(general=SpringWebApplicationLayer, specific=PSM_SpringModelPojoLayer)
gen_PSM_JavaElement_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_JavaElement)
gen_PSM_JavaAnnotation_ArtifactElement = Generalization(general=ArtifactElement, specific=PSM_JavaAnnotation)
gen_PSM_JavaInterfaceType_JavaUserDefinedType = Generalization(general=JavaUserDefinedType, specific=PSM_JavaInterfaceType)
gen_PSM_JavaMethod_JavaElement = Generalization(general=JavaElement, specific=PSM_JavaMethod)
gen_PSM_JavaClassType_JavaUserDefinedType = Generalization(general=JavaUserDefinedType, specific=PSM_JavaClassType)
gen_PSM_JavaDataField_JavaElement = Generalization(general=JavaElement, specific=PSM_JavaDataField)
gen_PSM_JavaMethodParameter_JavaDataField = Generalization(general=JavaDataField, specific=PSM_JavaMethodParameter)

# Domain Model
domain_model = DomainModel(
    name="PSM",
    types={PSM_ArtifactElement, ArtifactElement, PSM_DockerContainerLink, PSM_RootPSM, PSM_DistributedApplicationProject, PSM_DockerContainerDefinition, PSM_ApplicationProject, PSM_MicroserviceProject, PSM_DockerContainerPort, PSM_JavaSpringWebApplicationProject, MicroserviceProject, PSM_ConfigurationProperty, PSM_DependencyLibrary, PSM_JavaUserDefinedType, PSM_SpringBootApplicationLayer, SpringWebApplicationLayer, PSM_SpringControllerLayer, PSM_SpringServiceLayer, PSM_SpringConfigurationLayer, PSM_SpringFeignClientLayer, PSM_SpringComponentLayer, PSM_SpringWebApplicationLayer, PSM_JavaSpringWebFluxApplicationProject, JavaSpringWebApplicationProject, PSM_JavaSpringMVCApplicationProject, PSM_JavaDataType, JavaElement, JavaDataType, PSM_JavaMethod, PSM_SpringRepositoryLayer, PSM_SpringDomainLayer, PSM_SpringModelPojoLayer, PSM_JavaElement, PSM_JavaAnnotation, PSM_JavaAnnotationParameter, PSM_JavaInterfaceType, PSM_JavaMethodParameter, PSM_JavaDataField, PSM_JavaClassType, JavaUserDefinedType, JavaDataField},
    associations={application_project3, application0, containers1, modules9, links5, ports7, properties13, libraries11, elements16, layers14, parameters19, methods21, annotations18, implements34, parent35, parameters38, returns40, extends24, imports27, defines30, fields32, invokes43, type45},
    generalizations={gen_PSM_DockerContainerDefinition_ArtifactElement, gen_PSM_ApplicationProject_ArtifactElement, gen_PSM_DockerContainerLink_ArtifactElement, gen_PSM_DockerContainerPort_ArtifactElement, gen_PSM_JavaSpringWebApplicationProject_MicroserviceProject, gen_PSM_MicroserviceProject_ArtifactElement, gen_PSM_DependencyLibrary_ArtifactElement, gen_PSM_SpringBootApplicationLayer_SpringWebApplicationLayer, gen_PSM_SpringControllerLayer_SpringWebApplicationLayer, gen_PSM_SpringServiceLayer_SpringWebApplicationLayer, gen_PSM_SpringConfigurationLayer_SpringWebApplicationLayer, gen_PSM_SpringFeignClientLayer_SpringWebApplicationLayer, gen_PSM_SpringComponentLayer_SpringWebApplicationLayer, gen_PSM_JavaSpringWebFluxApplicationProject_JavaSpringWebApplicationProject, gen_PSM_JavaSpringMVCApplicationProject_JavaSpringWebApplicationProject, gen_PSM_ConfigurationProperty_ArtifactElement, gen_PSM_SpringWebApplicationLayer_ArtifactElement, gen_PSM_JavaAnnotationParameter_ArtifactElement, gen_PSM_JavaDataType_JavaElement, gen_PSM_JavaUserDefinedType_JavaDataType, gen_PSM_SpringRepositoryLayer_SpringWebApplicationLayer, gen_PSM_SpringDomainLayer_SpringWebApplicationLayer, gen_PSM_SpringModelPojoLayer_SpringWebApplicationLayer, gen_PSM_JavaElement_ArtifactElement, gen_PSM_JavaAnnotation_ArtifactElement, gen_PSM_JavaInterfaceType_JavaUserDefinedType, gen_PSM_JavaMethod_JavaElement, gen_PSM_JavaClassType_JavaUserDefinedType, gen_PSM_JavaDataField_JavaElement, gen_PSM_JavaMethodParameter_JavaDataField},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)