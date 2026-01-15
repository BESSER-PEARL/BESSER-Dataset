from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class JavaDataField:

    pass
class JavaUserDefinedType:

    pass
class PSM_JavaClassType(JavaUserDefinedType):

    pass
class PSM_JavaMethodParameter(JavaDataField):

    def __init__(self, ParameterOrder: int, PSM_JavaMethodParameter: "PSM_JavaMethod" = None):
        self.ParameterOrder = ParameterOrder
        self.PSM_JavaMethodParameter = PSM_JavaMethodParameter
        
    @property
    def ParameterOrder(self) -> int:
        return self.__ParameterOrder

    @ParameterOrder.setter
    def ParameterOrder(self, ParameterOrder: int):
        self.__ParameterOrder = ParameterOrder

    @property
    def PSM_JavaMethodParameter(self):
        return self.__PSM_JavaMethodParameter

    @PSM_JavaMethodParameter.setter
    def PSM_JavaMethodParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethodParameter__PSM_JavaMethodParameter", None)
        self.__PSM_JavaMethodParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaMethod39"):
                opp_val = getattr(old_value, "PSM_JavaMethod39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaMethod39"):
                opp_val = getattr(value, "PSM_JavaMethod39", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaMethod39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_JavaInterfaceType(JavaUserDefinedType):

    pass
class JavaDataType:

    pass
class JavaElement:

    pass
class PSM_JavaMethod(JavaElement):

    def __init__(self, RootCallingMethod: str, PSM_JavaMethod: "PSM_JavaUserDefinedType" = None, PSM_JavaMethod36: "PSM_JavaUserDefinedType" = None, PSM_JavaMethod39: set["PSM_JavaMethodParameter"] = None, PSM_JavaMethod41: "PSM_JavaDataType" = None, PSM_JavaMethod44: "PSM_JavaMethod" = None, PSM_JavaMethod42: set["PSM_JavaMethod"] = None):
        self.RootCallingMethod = RootCallingMethod
        self.PSM_JavaMethod = PSM_JavaMethod
        self.PSM_JavaMethod36 = PSM_JavaMethod36
        self.PSM_JavaMethod39 = PSM_JavaMethod39 if PSM_JavaMethod39 is not None else set()
        self.PSM_JavaMethod41 = PSM_JavaMethod41
        self.PSM_JavaMethod44 = PSM_JavaMethod44
        self.PSM_JavaMethod42 = PSM_JavaMethod42 if PSM_JavaMethod42 is not None else set()
        
    @property
    def RootCallingMethod(self) -> str:
        return self.__RootCallingMethod

    @RootCallingMethod.setter
    def RootCallingMethod(self, RootCallingMethod: str):
        self.__RootCallingMethod = RootCallingMethod

    @property
    def PSM_JavaMethod36(self):
        return self.__PSM_JavaMethod36

    @PSM_JavaMethod36.setter
    def PSM_JavaMethod36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod36", None)
        self.__PSM_JavaMethod36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaUserDefinedType37"):
                opp_val = getattr(old_value, "PSM_JavaUserDefinedType37", None)
                if opp_val == self:
                    setattr(old_value, "PSM_JavaUserDefinedType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaUserDefinedType37"):
                opp_val = getattr(value, "PSM_JavaUserDefinedType37", None)
                setattr(value, "PSM_JavaUserDefinedType37", self)

    @property
    def PSM_JavaMethod44(self):
        return self.__PSM_JavaMethod44

    @PSM_JavaMethod44.setter
    def PSM_JavaMethod44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod44", None)
        self.__PSM_JavaMethod44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaMethod42"):
                opp_val = getattr(old_value, "PSM_JavaMethod42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaMethod42"):
                opp_val = getattr(value, "PSM_JavaMethod42", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaMethod42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PSM_JavaMethod42(self):
        return self.__PSM_JavaMethod42

    @PSM_JavaMethod42.setter
    def PSM_JavaMethod42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod42", None)
        self.__PSM_JavaMethod42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_JavaMethod44"):
                    opp_val = getattr(item, "PSM_JavaMethod44", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_JavaMethod44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_JavaMethod44"):
                    opp_val = getattr(item, "PSM_JavaMethod44", None)
                    
                    setattr(item, "PSM_JavaMethod44", self)
                    

    @property
    def PSM_JavaMethod(self):
        return self.__PSM_JavaMethod

    @PSM_JavaMethod.setter
    def PSM_JavaMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod", None)
        self.__PSM_JavaMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaUserDefinedType22"):
                opp_val = getattr(old_value, "PSM_JavaUserDefinedType22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaUserDefinedType22"):
                opp_val = getattr(value, "PSM_JavaUserDefinedType22", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaUserDefinedType22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PSM_JavaMethod41(self):
        return self.__PSM_JavaMethod41

    @PSM_JavaMethod41.setter
    def PSM_JavaMethod41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod41", None)
        self.__PSM_JavaMethod41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaDataType"):
                opp_val = getattr(old_value, "PSM_JavaDataType", None)
                if opp_val == self:
                    setattr(old_value, "PSM_JavaDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaDataType"):
                opp_val = getattr(value, "PSM_JavaDataType", None)
                setattr(value, "PSM_JavaDataType", self)

    @property
    def PSM_JavaMethod39(self):
        return self.__PSM_JavaMethod39

    @PSM_JavaMethod39.setter
    def PSM_JavaMethod39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaMethod__PSM_JavaMethod39", None)
        self.__PSM_JavaMethod39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_JavaMethodParameter"):
                    opp_val = getattr(item, "PSM_JavaMethodParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_JavaMethodParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_JavaMethodParameter"):
                    opp_val = getattr(item, "PSM_JavaMethodParameter", None)
                    
                    setattr(item, "PSM_JavaMethodParameter", self)
                    

class PSM_JavaDataField(JavaElement):

    def __init__(self, FieldValue: str, PSM_JavaDataField: "PSM_JavaUserDefinedType" = None, PSM_JavaDataField46: "PSM_JavaDataType" = None):
        self.FieldValue = FieldValue
        self.PSM_JavaDataField = PSM_JavaDataField
        self.PSM_JavaDataField46 = PSM_JavaDataField46
        
    @property
    def FieldValue(self) -> str:
        return self.__FieldValue

    @FieldValue.setter
    def FieldValue(self, FieldValue: str):
        self.__FieldValue = FieldValue

    @property
    def PSM_JavaDataField46(self):
        return self.__PSM_JavaDataField46

    @PSM_JavaDataField46.setter
    def PSM_JavaDataField46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaDataField__PSM_JavaDataField46", None)
        self.__PSM_JavaDataField46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaDataType47"):
                opp_val = getattr(old_value, "PSM_JavaDataType47", None)
                if opp_val == self:
                    setattr(old_value, "PSM_JavaDataType47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaDataType47"):
                opp_val = getattr(value, "PSM_JavaDataType47", None)
                setattr(value, "PSM_JavaDataType47", self)

    @property
    def PSM_JavaDataField(self):
        return self.__PSM_JavaDataField

    @PSM_JavaDataField.setter
    def PSM_JavaDataField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaDataField__PSM_JavaDataField", None)
        self.__PSM_JavaDataField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaUserDefinedType33"):
                opp_val = getattr(old_value, "PSM_JavaUserDefinedType33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaUserDefinedType33"):
                opp_val = getattr(value, "PSM_JavaUserDefinedType33", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaUserDefinedType33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_JavaDataType(JavaElement):

    def __init__(self, IsPrimitive: bool, JsonSchema: str, PackageName: str, PSM_JavaDataType: "PSM_JavaMethod" = None, PSM_JavaDataType47: "PSM_JavaDataField" = None):
        self.IsPrimitive = IsPrimitive
        self.JsonSchema = JsonSchema
        self.PackageName = PackageName
        self.PSM_JavaDataType = PSM_JavaDataType
        self.PSM_JavaDataType47 = PSM_JavaDataType47
        
    @property
    def PackageName(self) -> str:
        return self.__PackageName

    @PackageName.setter
    def PackageName(self, PackageName: str):
        self.__PackageName = PackageName

    @property
    def JsonSchema(self) -> str:
        return self.__JsonSchema

    @JsonSchema.setter
    def JsonSchema(self, JsonSchema: str):
        self.__JsonSchema = JsonSchema

    @property
    def IsPrimitive(self) -> bool:
        return self.__IsPrimitive

    @IsPrimitive.setter
    def IsPrimitive(self, IsPrimitive: bool):
        self.__IsPrimitive = IsPrimitive

    @property
    def PSM_JavaDataType47(self):
        return self.__PSM_JavaDataType47

    @PSM_JavaDataType47.setter
    def PSM_JavaDataType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaDataType__PSM_JavaDataType47", None)
        self.__PSM_JavaDataType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaDataField46"):
                opp_val = getattr(old_value, "PSM_JavaDataField46", None)
                if opp_val == self:
                    setattr(old_value, "PSM_JavaDataField46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaDataField46"):
                opp_val = getattr(value, "PSM_JavaDataField46", None)
                setattr(value, "PSM_JavaDataField46", self)

    @property
    def PSM_JavaDataType(self):
        return self.__PSM_JavaDataType

    @PSM_JavaDataType.setter
    def PSM_JavaDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaDataType__PSM_JavaDataType", None)
        self.__PSM_JavaDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaMethod41"):
                opp_val = getattr(old_value, "PSM_JavaMethod41", None)
                if opp_val == self:
                    setattr(old_value, "PSM_JavaMethod41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaMethod41"):
                opp_val = getattr(value, "PSM_JavaMethod41", None)
                setattr(value, "PSM_JavaMethod41", self)

class JavaSpringWebApplicationProject:

    pass
class PSM_JavaSpringMVCApplicationProject(JavaSpringWebApplicationProject):

    pass
class PSM_JavaSpringWebFluxApplicationProject(JavaSpringWebApplicationProject):

    pass
class SpringWebApplicationLayer:

    pass
class PSM_SpringComponentLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringModelPojoLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringRepositoryLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringControllerLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringFeignClientLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringDomainLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringConfigurationLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringServiceLayer(SpringWebApplicationLayer):

    pass
class PSM_SpringBootApplicationLayer(SpringWebApplicationLayer):

    pass
class PSM_JavaUserDefinedType(JavaDataType):

    pass
class MicroserviceProject:

    pass
class PSM_JavaSpringWebApplicationProject(MicroserviceProject):

    pass
class PSM_DistributedApplicationProject:

    def __init__(self, ApplicationName: str, ProjectPackageURL: str, PSM_DistributedApplicationProject4: "PSM_ApplicationProject" = None, PSM_DistributedApplicationProject: "PSM_RootPSM" = None, PSM_DistributedApplicationProject2: set["PSM_DockerContainerDefinition"] = None):
        self.ApplicationName = ApplicationName
        self.ProjectPackageURL = ProjectPackageURL
        self.PSM_DistributedApplicationProject4 = PSM_DistributedApplicationProject4
        self.PSM_DistributedApplicationProject = PSM_DistributedApplicationProject
        self.PSM_DistributedApplicationProject2 = PSM_DistributedApplicationProject2 if PSM_DistributedApplicationProject2 is not None else set()
        
    @property
    def ApplicationName(self) -> str:
        return self.__ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName: str):
        self.__ApplicationName = ApplicationName

    @property
    def ProjectPackageURL(self) -> str:
        return self.__ProjectPackageURL

    @ProjectPackageURL.setter
    def ProjectPackageURL(self, ProjectPackageURL: str):
        self.__ProjectPackageURL = ProjectPackageURL

    @property
    def PSM_DistributedApplicationProject2(self):
        return self.__PSM_DistributedApplicationProject2

    @PSM_DistributedApplicationProject2.setter
    def PSM_DistributedApplicationProject2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DistributedApplicationProject__PSM_DistributedApplicationProject2", None)
        self.__PSM_DistributedApplicationProject2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_DockerContainerDefinition"):
                    opp_val = getattr(item, "PSM_DockerContainerDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_DockerContainerDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_DockerContainerDefinition"):
                    opp_val = getattr(item, "PSM_DockerContainerDefinition", None)
                    
                    setattr(item, "PSM_DockerContainerDefinition", self)
                    

    @property
    def PSM_DistributedApplicationProject4(self):
        return self.__PSM_DistributedApplicationProject4

    @PSM_DistributedApplicationProject4.setter
    def PSM_DistributedApplicationProject4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DistributedApplicationProject__PSM_DistributedApplicationProject4", None)
        self.__PSM_DistributedApplicationProject4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_ApplicationProject"):
                opp_val = getattr(old_value, "PSM_ApplicationProject", None)
                if opp_val == self:
                    setattr(old_value, "PSM_ApplicationProject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_ApplicationProject"):
                opp_val = getattr(value, "PSM_ApplicationProject", None)
                setattr(value, "PSM_ApplicationProject", self)

    @property
    def PSM_DistributedApplicationProject(self):
        return self.__PSM_DistributedApplicationProject

    @PSM_DistributedApplicationProject.setter
    def PSM_DistributedApplicationProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DistributedApplicationProject__PSM_DistributedApplicationProject", None)
        self.__PSM_DistributedApplicationProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_RootPSM"):
                opp_val = getattr(old_value, "PSM_RootPSM", None)
                if opp_val == self:
                    setattr(old_value, "PSM_RootPSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_RootPSM"):
                opp_val = getattr(value, "PSM_RootPSM", None)
                setattr(value, "PSM_RootPSM", self)

class PSM_RootPSM:

    pass
class ArtifactElement:

    pass
class PSM_ConfigurationProperty(ArtifactElement):

    def __init__(self, FullyQualifiedPropertyName: str, PropertyValue: str, ConfigurationProfile: str, PSM_ConfigurationProperty: "PSM_JavaSpringWebApplicationProject" = None):
        self.FullyQualifiedPropertyName = FullyQualifiedPropertyName
        self.PropertyValue = PropertyValue
        self.ConfigurationProfile = ConfigurationProfile
        self.PSM_ConfigurationProperty = PSM_ConfigurationProperty
        
    @property
    def ConfigurationProfile(self) -> str:
        return self.__ConfigurationProfile

    @ConfigurationProfile.setter
    def ConfigurationProfile(self, ConfigurationProfile: str):
        self.__ConfigurationProfile = ConfigurationProfile

    @property
    def PropertyValue(self) -> str:
        return self.__PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue: str):
        self.__PropertyValue = PropertyValue

    @property
    def FullyQualifiedPropertyName(self) -> str:
        return self.__FullyQualifiedPropertyName

    @FullyQualifiedPropertyName.setter
    def FullyQualifiedPropertyName(self, FullyQualifiedPropertyName: str):
        self.__FullyQualifiedPropertyName = FullyQualifiedPropertyName

    @property
    def PSM_ConfigurationProperty(self):
        return self.__PSM_ConfigurationProperty

    @PSM_ConfigurationProperty.setter
    def PSM_ConfigurationProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_ConfigurationProperty__PSM_ConfigurationProperty", None)
        self.__PSM_ConfigurationProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaSpringWebApplicationProject"):
                opp_val = getattr(old_value, "PSM_JavaSpringWebApplicationProject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaSpringWebApplicationProject"):
                opp_val = getattr(value, "PSM_JavaSpringWebApplicationProject", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaSpringWebApplicationProject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_DockerContainerLink(ArtifactElement):

    def __init__(self, DependencyOrder: int, LinksDependsOnField: str, PSM_DockerContainerLink: "PSM_DockerContainerDefinition" = None):
        self.DependencyOrder = DependencyOrder
        self.LinksDependsOnField = LinksDependsOnField
        self.PSM_DockerContainerLink = PSM_DockerContainerLink
        
    @property
    def DependencyOrder(self) -> int:
        return self.__DependencyOrder

    @DependencyOrder.setter
    def DependencyOrder(self, DependencyOrder: int):
        self.__DependencyOrder = DependencyOrder

    @property
    def LinksDependsOnField(self) -> str:
        return self.__LinksDependsOnField

    @LinksDependsOnField.setter
    def LinksDependsOnField(self, LinksDependsOnField: str):
        self.__LinksDependsOnField = LinksDependsOnField

    @property
    def PSM_DockerContainerLink(self):
        return self.__PSM_DockerContainerLink

    @PSM_DockerContainerLink.setter
    def PSM_DockerContainerLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DockerContainerLink__PSM_DockerContainerLink", None)
        self.__PSM_DockerContainerLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_DockerContainerDefinition6"):
                opp_val = getattr(old_value, "PSM_DockerContainerDefinition6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_DockerContainerDefinition6"):
                opp_val = getattr(value, "PSM_DockerContainerDefinition6", None)
                if opp_val is None:
                    setattr(value, "PSM_DockerContainerDefinition6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_DependencyLibrary(ArtifactElement):

    def __init__(self, LibraryName: str, LibraryScope: str, LibraryGroupName: str, PSM_DependencyLibrary: "PSM_MicroserviceProject" = None):
        self.LibraryName = LibraryName
        self.LibraryScope = LibraryScope
        self.LibraryGroupName = LibraryGroupName
        self.PSM_DependencyLibrary = PSM_DependencyLibrary
        
    @property
    def LibraryScope(self) -> str:
        return self.__LibraryScope

    @LibraryScope.setter
    def LibraryScope(self, LibraryScope: str):
        self.__LibraryScope = LibraryScope

    @property
    def LibraryGroupName(self) -> str:
        return self.__LibraryGroupName

    @LibraryGroupName.setter
    def LibraryGroupName(self, LibraryGroupName: str):
        self.__LibraryGroupName = LibraryGroupName

    @property
    def LibraryName(self) -> str:
        return self.__LibraryName

    @LibraryName.setter
    def LibraryName(self, LibraryName: str):
        self.__LibraryName = LibraryName

    @property
    def PSM_DependencyLibrary(self):
        return self.__PSM_DependencyLibrary

    @PSM_DependencyLibrary.setter
    def PSM_DependencyLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DependencyLibrary__PSM_DependencyLibrary", None)
        self.__PSM_DependencyLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_MicroserviceProject12"):
                opp_val = getattr(old_value, "PSM_MicroserviceProject12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_MicroserviceProject12"):
                opp_val = getattr(value, "PSM_MicroserviceProject12", None)
                if opp_val is None:
                    setattr(value, "PSM_MicroserviceProject12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_ApplicationProject(ArtifactElement):

    def __init__(self, ProjectArtifactId: str, PSM_ApplicationProject: "PSM_DistributedApplicationProject" = None, PSM_ApplicationProject10: set["PSM_MicroserviceProject"] = None):
        self.ProjectArtifactId = ProjectArtifactId
        self.PSM_ApplicationProject = PSM_ApplicationProject
        self.PSM_ApplicationProject10 = PSM_ApplicationProject10 if PSM_ApplicationProject10 is not None else set()
        
    @property
    def ProjectArtifactId(self) -> str:
        return self.__ProjectArtifactId

    @ProjectArtifactId.setter
    def ProjectArtifactId(self, ProjectArtifactId: str):
        self.__ProjectArtifactId = ProjectArtifactId

    @property
    def PSM_ApplicationProject(self):
        return self.__PSM_ApplicationProject

    @PSM_ApplicationProject.setter
    def PSM_ApplicationProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_ApplicationProject__PSM_ApplicationProject", None)
        self.__PSM_ApplicationProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_DistributedApplicationProject4"):
                opp_val = getattr(old_value, "PSM_DistributedApplicationProject4", None)
                if opp_val == self:
                    setattr(old_value, "PSM_DistributedApplicationProject4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_DistributedApplicationProject4"):
                opp_val = getattr(value, "PSM_DistributedApplicationProject4", None)
                setattr(value, "PSM_DistributedApplicationProject4", self)

    @property
    def PSM_ApplicationProject10(self):
        return self.__PSM_ApplicationProject10

    @PSM_ApplicationProject10.setter
    def PSM_ApplicationProject10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_ApplicationProject__PSM_ApplicationProject10", None)
        self.__PSM_ApplicationProject10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_MicroserviceProject"):
                    opp_val = getattr(item, "PSM_MicroserviceProject", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_MicroserviceProject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_MicroserviceProject"):
                    opp_val = getattr(item, "PSM_MicroserviceProject", None)
                    
                    setattr(item, "PSM_MicroserviceProject", self)
                    

class PSM_JavaElement(ArtifactElement):

    def __init__(self, ElementIdentifier: str, ElementProfile: str, PSM_JavaElement: set["PSM_JavaAnnotation"] = None):
        self.ElementIdentifier = ElementIdentifier
        self.ElementProfile = ElementProfile
        self.PSM_JavaElement = PSM_JavaElement if PSM_JavaElement is not None else set()
        
    @property
    def ElementIdentifier(self) -> str:
        return self.__ElementIdentifier

    @ElementIdentifier.setter
    def ElementIdentifier(self, ElementIdentifier: str):
        self.__ElementIdentifier = ElementIdentifier

    @property
    def ElementProfile(self) -> str:
        return self.__ElementProfile

    @ElementProfile.setter
    def ElementProfile(self, ElementProfile: str):
        self.__ElementProfile = ElementProfile

    @property
    def PSM_JavaElement(self):
        return self.__PSM_JavaElement

    @PSM_JavaElement.setter
    def PSM_JavaElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaElement__PSM_JavaElement", None)
        self.__PSM_JavaElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_JavaAnnotation"):
                    opp_val = getattr(item, "PSM_JavaAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_JavaAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_JavaAnnotation"):
                    opp_val = getattr(item, "PSM_JavaAnnotation", None)
                    
                    setattr(item, "PSM_JavaAnnotation", self)
                    

class PSM_DockerContainerPort(ArtifactElement):

    def __init__(self, ExposesPortsField: str, PSM_DockerContainerPort: "PSM_DockerContainerDefinition" = None):
        self.ExposesPortsField = ExposesPortsField
        self.PSM_DockerContainerPort = PSM_DockerContainerPort
        
    @property
    def ExposesPortsField(self) -> str:
        return self.__ExposesPortsField

    @ExposesPortsField.setter
    def ExposesPortsField(self, ExposesPortsField: str):
        self.__ExposesPortsField = ExposesPortsField

    @property
    def PSM_DockerContainerPort(self):
        return self.__PSM_DockerContainerPort

    @PSM_DockerContainerPort.setter
    def PSM_DockerContainerPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DockerContainerPort__PSM_DockerContainerPort", None)
        self.__PSM_DockerContainerPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_DockerContainerDefinition8"):
                opp_val = getattr(old_value, "PSM_DockerContainerDefinition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_DockerContainerDefinition8"):
                opp_val = getattr(value, "PSM_DockerContainerDefinition8", None)
                if opp_val is None:
                    setattr(value, "PSM_DockerContainerDefinition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_DockerContainerDefinition(ArtifactElement):

    def __init__(self, ContainerName: str, GeneratesLogs: bool, ImageField: str, BuildField: str, PSM_DockerContainerDefinition6: set["PSM_DockerContainerLink"] = None, PSM_DockerContainerDefinition: "PSM_DistributedApplicationProject" = None, PSM_DockerContainerDefinition8: set["PSM_DockerContainerPort"] = None):
        self.ContainerName = ContainerName
        self.GeneratesLogs = GeneratesLogs
        self.ImageField = ImageField
        self.BuildField = BuildField
        self.PSM_DockerContainerDefinition6 = PSM_DockerContainerDefinition6 if PSM_DockerContainerDefinition6 is not None else set()
        self.PSM_DockerContainerDefinition = PSM_DockerContainerDefinition
        self.PSM_DockerContainerDefinition8 = PSM_DockerContainerDefinition8 if PSM_DockerContainerDefinition8 is not None else set()
        
    @property
    def GeneratesLogs(self) -> bool:
        return self.__GeneratesLogs

    @GeneratesLogs.setter
    def GeneratesLogs(self, GeneratesLogs: bool):
        self.__GeneratesLogs = GeneratesLogs

    @property
    def BuildField(self) -> str:
        return self.__BuildField

    @BuildField.setter
    def BuildField(self, BuildField: str):
        self.__BuildField = BuildField

    @property
    def ImageField(self) -> str:
        return self.__ImageField

    @ImageField.setter
    def ImageField(self, ImageField: str):
        self.__ImageField = ImageField

    @property
    def ContainerName(self) -> str:
        return self.__ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName: str):
        self.__ContainerName = ContainerName

    @property
    def PSM_DockerContainerDefinition8(self):
        return self.__PSM_DockerContainerDefinition8

    @PSM_DockerContainerDefinition8.setter
    def PSM_DockerContainerDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DockerContainerDefinition__PSM_DockerContainerDefinition8", None)
        self.__PSM_DockerContainerDefinition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_DockerContainerPort"):
                    opp_val = getattr(item, "PSM_DockerContainerPort", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_DockerContainerPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_DockerContainerPort"):
                    opp_val = getattr(item, "PSM_DockerContainerPort", None)
                    
                    setattr(item, "PSM_DockerContainerPort", self)
                    

    @property
    def PSM_DockerContainerDefinition(self):
        return self.__PSM_DockerContainerDefinition

    @PSM_DockerContainerDefinition.setter
    def PSM_DockerContainerDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DockerContainerDefinition__PSM_DockerContainerDefinition", None)
        self.__PSM_DockerContainerDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_DistributedApplicationProject2"):
                opp_val = getattr(old_value, "PSM_DistributedApplicationProject2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_DistributedApplicationProject2"):
                opp_val = getattr(value, "PSM_DistributedApplicationProject2", None)
                if opp_val is None:
                    setattr(value, "PSM_DistributedApplicationProject2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PSM_DockerContainerDefinition6(self):
        return self.__PSM_DockerContainerDefinition6

    @PSM_DockerContainerDefinition6.setter
    def PSM_DockerContainerDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_DockerContainerDefinition__PSM_DockerContainerDefinition6", None)
        self.__PSM_DockerContainerDefinition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_DockerContainerLink"):
                    opp_val = getattr(item, "PSM_DockerContainerLink", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_DockerContainerLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_DockerContainerLink"):
                    opp_val = getattr(item, "PSM_DockerContainerLink", None)
                    
                    setattr(item, "PSM_DockerContainerLink", self)
                    

class PSM_SpringWebApplicationLayer(ArtifactElement):

    def __init__(self, LayerName: str, PSM_SpringWebApplicationLayer17: set["PSM_JavaUserDefinedType"] = None, PSM_SpringWebApplicationLayer: "PSM_JavaSpringWebApplicationProject" = None):
        self.LayerName = LayerName
        self.PSM_SpringWebApplicationLayer17 = PSM_SpringWebApplicationLayer17 if PSM_SpringWebApplicationLayer17 is not None else set()
        self.PSM_SpringWebApplicationLayer = PSM_SpringWebApplicationLayer
        
    @property
    def LayerName(self) -> str:
        return self.__LayerName

    @LayerName.setter
    def LayerName(self, LayerName: str):
        self.__LayerName = LayerName

    @property
    def PSM_SpringWebApplicationLayer17(self):
        return self.__PSM_SpringWebApplicationLayer17

    @PSM_SpringWebApplicationLayer17.setter
    def PSM_SpringWebApplicationLayer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_SpringWebApplicationLayer__PSM_SpringWebApplicationLayer17", None)
        self.__PSM_SpringWebApplicationLayer17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_JavaUserDefinedType"):
                    opp_val = getattr(item, "PSM_JavaUserDefinedType", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_JavaUserDefinedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_JavaUserDefinedType"):
                    opp_val = getattr(item, "PSM_JavaUserDefinedType", None)
                    
                    setattr(item, "PSM_JavaUserDefinedType", self)
                    

    @property
    def PSM_SpringWebApplicationLayer(self):
        return self.__PSM_SpringWebApplicationLayer

    @PSM_SpringWebApplicationLayer.setter
    def PSM_SpringWebApplicationLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_SpringWebApplicationLayer__PSM_SpringWebApplicationLayer", None)
        self.__PSM_SpringWebApplicationLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaSpringWebApplicationProject15"):
                opp_val = getattr(old_value, "PSM_JavaSpringWebApplicationProject15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaSpringWebApplicationProject15"):
                opp_val = getattr(value, "PSM_JavaSpringWebApplicationProject15", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaSpringWebApplicationProject15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_JavaAnnotationParameter(ArtifactElement):

    def __init__(self, ParameterName: str, ParameterValue: str, PSM_JavaAnnotationParameter: "PSM_JavaAnnotation" = None):
        self.ParameterName = ParameterName
        self.ParameterValue = ParameterValue
        self.PSM_JavaAnnotationParameter = PSM_JavaAnnotationParameter
        
    @property
    def ParameterValue(self) -> str:
        return self.__ParameterValue

    @ParameterValue.setter
    def ParameterValue(self, ParameterValue: str):
        self.__ParameterValue = ParameterValue

    @property
    def ParameterName(self) -> str:
        return self.__ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName: str):
        self.__ParameterName = ParameterName

    @property
    def PSM_JavaAnnotationParameter(self):
        return self.__PSM_JavaAnnotationParameter

    @PSM_JavaAnnotationParameter.setter
    def PSM_JavaAnnotationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaAnnotationParameter__PSM_JavaAnnotationParameter", None)
        self.__PSM_JavaAnnotationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaAnnotation20"):
                opp_val = getattr(old_value, "PSM_JavaAnnotation20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaAnnotation20"):
                opp_val = getattr(value, "PSM_JavaAnnotation20", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaAnnotation20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PSM_JavaAnnotation(ArtifactElement):

    def __init__(self, AnnotationName: str, PSM_JavaAnnotation20: set["PSM_JavaAnnotationParameter"] = None, PSM_JavaAnnotation: "PSM_JavaElement" = None):
        self.AnnotationName = AnnotationName
        self.PSM_JavaAnnotation20 = PSM_JavaAnnotation20 if PSM_JavaAnnotation20 is not None else set()
        self.PSM_JavaAnnotation = PSM_JavaAnnotation
        
    @property
    def AnnotationName(self) -> str:
        return self.__AnnotationName

    @AnnotationName.setter
    def AnnotationName(self, AnnotationName: str):
        self.__AnnotationName = AnnotationName

    @property
    def PSM_JavaAnnotation(self):
        return self.__PSM_JavaAnnotation

    @PSM_JavaAnnotation.setter
    def PSM_JavaAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaAnnotation__PSM_JavaAnnotation", None)
        self.__PSM_JavaAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_JavaElement"):
                opp_val = getattr(old_value, "PSM_JavaElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_JavaElement"):
                opp_val = getattr(value, "PSM_JavaElement", None)
                if opp_val is None:
                    setattr(value, "PSM_JavaElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PSM_JavaAnnotation20(self):
        return self.__PSM_JavaAnnotation20

    @PSM_JavaAnnotation20.setter
    def PSM_JavaAnnotation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_JavaAnnotation__PSM_JavaAnnotation20", None)
        self.__PSM_JavaAnnotation20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_JavaAnnotationParameter"):
                    opp_val = getattr(item, "PSM_JavaAnnotationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_JavaAnnotationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_JavaAnnotationParameter"):
                    opp_val = getattr(item, "PSM_JavaAnnotationParameter", None)
                    
                    setattr(item, "PSM_JavaAnnotationParameter", self)
                    

class PSM_MicroserviceProject(ArtifactElement):

    def __init__(self, ProjectArtifactId: str, PSM_MicroserviceProject: "PSM_ApplicationProject" = None, PSM_MicroserviceProject12: set["PSM_DependencyLibrary"] = None):
        self.ProjectArtifactId = ProjectArtifactId
        self.PSM_MicroserviceProject = PSM_MicroserviceProject
        self.PSM_MicroserviceProject12 = PSM_MicroserviceProject12 if PSM_MicroserviceProject12 is not None else set()
        
    @property
    def ProjectArtifactId(self) -> str:
        return self.__ProjectArtifactId

    @ProjectArtifactId.setter
    def ProjectArtifactId(self, ProjectArtifactId: str):
        self.__ProjectArtifactId = ProjectArtifactId

    @property
    def PSM_MicroserviceProject(self):
        return self.__PSM_MicroserviceProject

    @PSM_MicroserviceProject.setter
    def PSM_MicroserviceProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_MicroserviceProject__PSM_MicroserviceProject", None)
        self.__PSM_MicroserviceProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PSM_ApplicationProject10"):
                opp_val = getattr(old_value, "PSM_ApplicationProject10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PSM_ApplicationProject10"):
                opp_val = getattr(value, "PSM_ApplicationProject10", None)
                if opp_val is None:
                    setattr(value, "PSM_ApplicationProject10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PSM_MicroserviceProject12(self):
        return self.__PSM_MicroserviceProject12

    @PSM_MicroserviceProject12.setter
    def PSM_MicroserviceProject12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PSM_MicroserviceProject__PSM_MicroserviceProject12", None)
        self.__PSM_MicroserviceProject12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PSM_DependencyLibrary"):
                    opp_val = getattr(item, "PSM_DependencyLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "PSM_DependencyLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PSM_DependencyLibrary"):
                    opp_val = getattr(item, "PSM_DependencyLibrary", None)
                    
                    setattr(item, "PSM_DependencyLibrary", self)
                    

class PSM_ArtifactElement:

    def __init__(self, ParentProjectName: str, ArtifactFileName: str, GeneratingLinesOfCode: str):
        self.ParentProjectName = ParentProjectName
        self.ArtifactFileName = ArtifactFileName
        self.GeneratingLinesOfCode = GeneratingLinesOfCode
        
    @property
    def GeneratingLinesOfCode(self) -> str:
        return self.__GeneratingLinesOfCode

    @GeneratingLinesOfCode.setter
    def GeneratingLinesOfCode(self, GeneratingLinesOfCode: str):
        self.__GeneratingLinesOfCode = GeneratingLinesOfCode

    @property
    def ArtifactFileName(self) -> str:
        return self.__ArtifactFileName

    @ArtifactFileName.setter
    def ArtifactFileName(self, ArtifactFileName: str):
        self.__ArtifactFileName = ArtifactFileName

    @property
    def ParentProjectName(self) -> str:
        return self.__ParentProjectName

    @ParentProjectName.setter
    def ParentProjectName(self, ParentProjectName: str):
        self.__ParentProjectName = ParentProjectName
