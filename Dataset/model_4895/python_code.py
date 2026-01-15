from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AvailableFrom(Enum):
    REPOSITORY = "REPOSITORY"
    CONTRIBUTION = "CONTRIBUTION"
    VALIDATION_SET = "VALIDATION_SET"
    AGGREGATION = "AGGREGATION"
class InstallableUnitType(Enum):
    BUNDLE = "BUNDLE"
    FEATURE = "FEATURE"
    PRODUCT = "PRODUCT"
    CATEGORY = "CATEGORY"
    FRAGMENT = "FRAGMENT"
    OTHER = "OTHER"
class OperatingSystem(Enum):
    Win32 = "Win32"
    Linux = "Linux"
    MacOSX = "MacOSX"
    AIX = "AIX"
    HPUX = "HPUX"
    Solaris = "Solaris"
    QNX = "QNX"
class VersionMatch(Enum):
    BELOW = "BELOW"
    MATCHES = "MATCHES"
    ABOVE = "ABOVE"
class Architecture(Enum):
    X86 = "X86"
    PPC = "PPC"
    X86_64 = "X86_64"
    IA64 = "IA64"
    IA64_32 = "IA64_32"
    Sparc = "Sparc"
    PPC64 = "PPC64"
    S390 = "S390"
    S390X = "S390X"
class PackedStrategy(Enum):
    Copy = "Copy"
    Verify = "Verify"
    UnpackAsSibling = "UnpackAsSibling"
    Unpack = "Unpack"
    Skip = "Skip"
class StatusCode(Enum):
    OK = "OK"
    BROKEN = "BROKEN"
    WAITING = "WAITING"
class WindowSystem(Enum):
    Win32 = "Win32"
    GTK = "GTK"
    Carbon = "Carbon"
    Cocoa = "Cocoa"
    Motif = "Motif"
    Photon = "Photon"
class AggregationType(Enum):
    Stable = "Stable"
    Integration = "Integration"
    Nightly = "Nightly"
    Maintenance = "Maintenance"
    Continuous = "Continuous"
    Release = "Release"


############################################
# Definition of Classes
############################################

class p2view_aggregator_ITouchpointData:

    pass
class p2view_aggregator_ITouchpointType:

    pass
class aggregator_p2view_Touchpoints:

    pass
class p2view_aggregator_IRequirement:

    pass
class p2view_aggregator_IRepositoryReference:

    pass
class aggregator_p2view_RepositoryReferences:

    pass
class p2view_aggregator_IProvidedCapability:

    pass
class LabelProvider:

    pass
class IProvidedCapability:

    pass
class aggregator_p2view_ProvidedCapabilityWrapper(IProvidedCapability, LabelProvider):

    pass
class ProvidedCapabilityWrapper:

    pass
class aggregator_p2view_ProvidedCapabilities:

    pass
class p2view_aggregator_Property:

    pass
class aggregator_p2view_Properties:

    pass
class Product:

    pass
class aggregator_p2view_Products:

    pass
class OtherIU:

    pass
class aggregator_p2view_Miscellaneous:

    pass
class RepositoryReferences:

    pass
class p2view_aggregator_MetadataRepository:

    pass
class InstallableUnits:

    pass
class IRequirement:

    pass
class aggregator_p2view_RequirementWrapper(IRequirement, LabelProvider):

    pass
class aggregator_p2view_MetadataRepositoryStructuredView:

    def __init__(self, name: str, loaded: bool, location: str, aggregator_p2view_MetadataRepositoryStructuredView: "InstallableUnits" = None, aggregator_p2view_MetadataRepositoryStructuredView110: "Properties" = None, aggregator_p2view_MetadataRepositoryStructuredView113: "p2view_aggregator_MetadataRepository" = None, aggregator_p2view_MetadataRepositoryStructuredView115: "RepositoryReferences" = None):
        self.name = name
        self.loaded = loaded
        self.location = location
        self.aggregator_p2view_MetadataRepositoryStructuredView = aggregator_p2view_MetadataRepositoryStructuredView
        self.aggregator_p2view_MetadataRepositoryStructuredView110 = aggregator_p2view_MetadataRepositoryStructuredView110
        self.aggregator_p2view_MetadataRepositoryStructuredView113 = aggregator_p2view_MetadataRepositoryStructuredView113
        self.aggregator_p2view_MetadataRepositoryStructuredView115 = aggregator_p2view_MetadataRepositoryStructuredView115
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def loaded(self) -> bool:
        return self.__loaded

    @loaded.setter
    def loaded(self, loaded: bool):
        self.__loaded = loaded

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView115(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView115

    @aggregator_p2view_MetadataRepositoryStructuredView115.setter
    def aggregator_p2view_MetadataRepositoryStructuredView115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView115", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepositoryReferences"):
                opp_val = getattr(old_value, "RepositoryReferences", None)
                if opp_val == self:
                    setattr(old_value, "RepositoryReferences", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepositoryReferences"):
                opp_val = getattr(value, "RepositoryReferences", None)
                setattr(value, "RepositoryReferences", self)

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView113(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView113

    @aggregator_p2view_MetadataRepositoryStructuredView113.setter
    def aggregator_p2view_MetadataRepositoryStructuredView113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView113", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2view_aggregator_MetadataRepository"):
                opp_val = getattr(old_value, "p2view_aggregator_MetadataRepository", None)
                if opp_val == self:
                    setattr(old_value, "p2view_aggregator_MetadataRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2view_aggregator_MetadataRepository"):
                opp_val = getattr(value, "p2view_aggregator_MetadataRepository", None)
                setattr(value, "p2view_aggregator_MetadataRepository", self)

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView110(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView110

    @aggregator_p2view_MetadataRepositoryStructuredView110.setter
    def aggregator_p2view_MetadataRepositoryStructuredView110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView110", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Properties111"):
                opp_val = getattr(old_value, "Properties111", None)
                if opp_val == self:
                    setattr(old_value, "Properties111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Properties111"):
                opp_val = getattr(value, "Properties111", None)
                setattr(value, "Properties111", self)

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView

    @aggregator_p2view_MetadataRepositoryStructuredView.setter
    def aggregator_p2view_MetadataRepositoryStructuredView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InstallableUnits"):
                opp_val = getattr(old_value, "InstallableUnits", None)
                if opp_val == self:
                    setattr(old_value, "InstallableUnits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InstallableUnits"):
                opp_val = getattr(value, "InstallableUnits", None)
                setattr(value, "InstallableUnits", self)

class MetadataRepositoryStructuredView:

    pass
class RequirementWrapper:

    pass
class aggregator_p2view_RepositoryBrowser:

    def __init__(self, loading: bool, aggregator_p2view_RepositoryBrowser: set["MetadataRepositoryStructuredView"] = None):
        self.loading = loading
        self.aggregator_p2view_RepositoryBrowser = aggregator_p2view_RepositoryBrowser if aggregator_p2view_RepositoryBrowser is not None else set()
        
    @property
    def loading(self) -> bool:
        return self.__loading

    @loading.setter
    def loading(self, loading: bool):
        self.__loading = loading

    @property
    def aggregator_p2view_RepositoryBrowser(self):
        return self.__aggregator_p2view_RepositoryBrowser

    @aggregator_p2view_RepositoryBrowser.setter
    def aggregator_p2view_RepositoryBrowser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_RepositoryBrowser__aggregator_p2view_RepositoryBrowser", None)
        self.__aggregator_p2view_RepositoryBrowser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetadataRepositoryStructuredView"):
                    opp_val = getattr(item, "MetadataRepositoryStructuredView", None)
                    
                    if opp_val == self:
                        setattr(item, "MetadataRepositoryStructuredView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetadataRepositoryStructuredView"):
                    opp_val = getattr(item, "MetadataRepositoryStructuredView", None)
                    
                    setattr(item, "MetadataRepositoryStructuredView", self)
                    

class aggregator_p2view_Requirements:

    pass
class p2view_aggregator_ILicense:

    pass
class aggregator_p2view_Licenses:

    pass
class p2view_IUDetails:

    pass
class p2view_IUPresentation:

    pass
class aggregator_p2view_IUPresentationWithDetails(p2view_IUDetails, p2view_IUPresentation):

    def __init__(self, detailsResolved: str):
        self.detailsResolved = detailsResolved
        
    @property
    def detailsResolved(self) -> str:
        return self.__detailsResolved

    @detailsResolved.setter
    def detailsResolved(self, detailsResolved: str):
        self.__detailsResolved = detailsResolved

class p2view_aggregator_IInstallableUnit:

    pass
class aggregator_p2view_IUPresentation(ABC):

    def __init__(self, id: str, version: str, name: str, label: str, description: str, type: str, filter: str, aggregator_p2view_IUPresentation: "p2view_aggregator_IInstallableUnit" = None):
        self.id = id
        self.version = version
        self.name = name
        self.label = label
        self.description = description
        self.type = type
        self.filter = filter
        self.aggregator_p2view_IUPresentation = aggregator_p2view_IUPresentation
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def aggregator_p2view_IUPresentation(self):
        return self.__aggregator_p2view_IUPresentation

    @aggregator_p2view_IUPresentation.setter
    def aggregator_p2view_IUPresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_IUPresentation__aggregator_p2view_IUPresentation", None)
        self.__aggregator_p2view_IUPresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2view_aggregator_IInstallableUnit"):
                opp_val = getattr(old_value, "p2view_aggregator_IInstallableUnit", None)
                if opp_val == self:
                    setattr(old_value, "p2view_aggregator_IInstallableUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2view_aggregator_IInstallableUnit"):
                opp_val = getattr(value, "p2view_aggregator_IInstallableUnit", None)
                setattr(value, "p2view_aggregator_IInstallableUnit", self)

class Licenses:

    pass
class p2view_aggregator_ICopyright:

    pass
class p2view_aggregator_IUpdateDescriptor:

    pass
class Touchpoints:

    pass
class Properties:

    pass
class ProvidedCapabilities:

    pass
class Miscellaneous:

    pass
class aggregator_p2view_InstallableUnits:

    def __init__(self, aggregator_p2view_InstallableUnits91: "Miscellaneous" = None, aggregator_p2view_InstallableUnits: set["IUPresentation"] = None, aggregator_p2view_InstallableUnits76: "Categories" = None, aggregator_p2view_InstallableUnits79: "Features" = None, aggregator_p2view_InstallableUnits82: "Products" = None, aggregator_p2view_InstallableUnits85: "Bundles" = None, aggregator_p2view_InstallableUnits88: "Fragments" = None):
        self.aggregator_p2view_InstallableUnits91 = aggregator_p2view_InstallableUnits91
        self.aggregator_p2view_InstallableUnits = aggregator_p2view_InstallableUnits if aggregator_p2view_InstallableUnits is not None else set()
        self.aggregator_p2view_InstallableUnits76 = aggregator_p2view_InstallableUnits76
        self.aggregator_p2view_InstallableUnits79 = aggregator_p2view_InstallableUnits79
        self.aggregator_p2view_InstallableUnits82 = aggregator_p2view_InstallableUnits82
        self.aggregator_p2view_InstallableUnits85 = aggregator_p2view_InstallableUnits85
        self.aggregator_p2view_InstallableUnits88 = aggregator_p2view_InstallableUnits88
        
    @property
    def aggregator_p2view_InstallableUnits79(self):
        return self.__aggregator_p2view_InstallableUnits79

    @aggregator_p2view_InstallableUnits79.setter
    def aggregator_p2view_InstallableUnits79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits79", None)
        self.__aggregator_p2view_InstallableUnits79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features80"):
                opp_val = getattr(old_value, "Features80", None)
                if opp_val == self:
                    setattr(old_value, "Features80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features80"):
                opp_val = getattr(value, "Features80", None)
                setattr(value, "Features80", self)

    @property
    def aggregator_p2view_InstallableUnits88(self):
        return self.__aggregator_p2view_InstallableUnits88

    @aggregator_p2view_InstallableUnits88.setter
    def aggregator_p2view_InstallableUnits88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits88", None)
        self.__aggregator_p2view_InstallableUnits88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments89"):
                opp_val = getattr(old_value, "Fragments89", None)
                if opp_val == self:
                    setattr(old_value, "Fragments89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments89"):
                opp_val = getattr(value, "Fragments89", None)
                setattr(value, "Fragments89", self)

    @property
    def aggregator_p2view_InstallableUnits85(self):
        return self.__aggregator_p2view_InstallableUnits85

    @aggregator_p2view_InstallableUnits85.setter
    def aggregator_p2view_InstallableUnits85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits85", None)
        self.__aggregator_p2view_InstallableUnits85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles86"):
                opp_val = getattr(old_value, "Bundles86", None)
                if opp_val == self:
                    setattr(old_value, "Bundles86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles86"):
                opp_val = getattr(value, "Bundles86", None)
                setattr(value, "Bundles86", self)

    @property
    def aggregator_p2view_InstallableUnits(self):
        return self.__aggregator_p2view_InstallableUnits

    @aggregator_p2view_InstallableUnits.setter
    def aggregator_p2view_InstallableUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits", None)
        self.__aggregator_p2view_InstallableUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IUPresentation"):
                    opp_val = getattr(item, "IUPresentation", None)
                    
                    if opp_val == self:
                        setattr(item, "IUPresentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IUPresentation"):
                    opp_val = getattr(item, "IUPresentation", None)
                    
                    setattr(item, "IUPresentation", self)
                    

    @property
    def aggregator_p2view_InstallableUnits76(self):
        return self.__aggregator_p2view_InstallableUnits76

    @aggregator_p2view_InstallableUnits76.setter
    def aggregator_p2view_InstallableUnits76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits76", None)
        self.__aggregator_p2view_InstallableUnits76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Categories77"):
                opp_val = getattr(old_value, "Categories77", None)
                if opp_val == self:
                    setattr(old_value, "Categories77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Categories77"):
                opp_val = getattr(value, "Categories77", None)
                setattr(value, "Categories77", self)

    @property
    def aggregator_p2view_InstallableUnits82(self):
        return self.__aggregator_p2view_InstallableUnits82

    @aggregator_p2view_InstallableUnits82.setter
    def aggregator_p2view_InstallableUnits82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits82", None)
        self.__aggregator_p2view_InstallableUnits82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Products83"):
                opp_val = getattr(old_value, "Products83", None)
                if opp_val == self:
                    setattr(old_value, "Products83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products83"):
                opp_val = getattr(value, "Products83", None)
                setattr(value, "Products83", self)

    @property
    def aggregator_p2view_InstallableUnits91(self):
        return self.__aggregator_p2view_InstallableUnits91

    @aggregator_p2view_InstallableUnits91.setter
    def aggregator_p2view_InstallableUnits91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits91", None)
        self.__aggregator_p2view_InstallableUnits91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Miscellaneous"):
                opp_val = getattr(old_value, "Miscellaneous", None)
                if opp_val == self:
                    setattr(old_value, "Miscellaneous", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Miscellaneous"):
                opp_val = getattr(value, "Miscellaneous", None)
                setattr(value, "Miscellaneous", self)

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullMiscellaneousContainer(self) -> str:
        # TODO: Implement getNotNullMiscellaneousContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

class Fragment:

    pass
class aggregator_p2view_Fragments:

    pass
class Feature:

    pass
class aggregator_p2view_Features:

    pass
class Category:

    pass
class aggregator_p2view_Categories:

    pass
class Requirements:

    pass
class aggregator_p2view_IUDetails:

    pass
class Fragments:

    pass
class Bundles:

    pass
class Products:

    pass
class Features:

    pass
class Categories:

    pass
class IUPresentation:

    pass
class aggregator_p2view_Category(IUPresentation):

    def __init__(self, aggregator_p2view_Category59: "Fragments" = None, aggregator_p2view_Category61: "IUDetails" = None, aggregator_p2view_Category: "Categories" = None, aggregator_p2view_Category53: "Features" = None, aggregator_p2view_Category55: "Products" = None, aggregator_p2view_Category57: "Bundles" = None, IUPresentation: "aggregator_p2view_InstallableUnits"):
        self.aggregator_p2view_Category59 = aggregator_p2view_Category59
        self.aggregator_p2view_Category61 = aggregator_p2view_Category61
        self.aggregator_p2view_Category = aggregator_p2view_Category
        self.aggregator_p2view_Category53 = aggregator_p2view_Category53
        self.aggregator_p2view_Category55 = aggregator_p2view_Category55
        self.aggregator_p2view_Category57 = aggregator_p2view_Category57
        
    @property
    def aggregator_p2view_Category53(self):
        return self.__aggregator_p2view_Category53

    @aggregator_p2view_Category53.setter
    def aggregator_p2view_Category53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category53", None)
        self.__aggregator_p2view_Category53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features"):
                opp_val = getattr(old_value, "Features", None)
                if opp_val == self:
                    setattr(old_value, "Features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features"):
                opp_val = getattr(value, "Features", None)
                setattr(value, "Features", self)

    @property
    def aggregator_p2view_Category59(self):
        return self.__aggregator_p2view_Category59

    @aggregator_p2view_Category59.setter
    def aggregator_p2view_Category59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category59", None)
        self.__aggregator_p2view_Category59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments"):
                opp_val = getattr(old_value, "Fragments", None)
                if opp_val == self:
                    setattr(old_value, "Fragments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments"):
                opp_val = getattr(value, "Fragments", None)
                setattr(value, "Fragments", self)

    @property
    def aggregator_p2view_Category61(self):
        return self.__aggregator_p2view_Category61

    @aggregator_p2view_Category61.setter
    def aggregator_p2view_Category61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category61", None)
        self.__aggregator_p2view_Category61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IUDetails"):
                opp_val = getattr(old_value, "IUDetails", None)
                if opp_val == self:
                    setattr(old_value, "IUDetails", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IUDetails"):
                opp_val = getattr(value, "IUDetails", None)
                setattr(value, "IUDetails", self)

    @property
    def aggregator_p2view_Category57(self):
        return self.__aggregator_p2view_Category57

    @aggregator_p2view_Category57.setter
    def aggregator_p2view_Category57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category57", None)
        self.__aggregator_p2view_Category57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles"):
                opp_val = getattr(old_value, "Bundles", None)
                if opp_val == self:
                    setattr(old_value, "Bundles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles"):
                opp_val = getattr(value, "Bundles", None)
                setattr(value, "Bundles", self)

    @property
    def aggregator_p2view_Category(self):
        return self.__aggregator_p2view_Category

    @aggregator_p2view_Category.setter
    def aggregator_p2view_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category", None)
        self.__aggregator_p2view_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Categories"):
                opp_val = getattr(old_value, "Categories", None)
                if opp_val == self:
                    setattr(old_value, "Categories", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Categories"):
                opp_val = getattr(value, "Categories", None)
                setattr(value, "Categories", self)

    @property
    def aggregator_p2view_Category55(self):
        return self.__aggregator_p2view_Category55

    @aggregator_p2view_Category55.setter
    def aggregator_p2view_Category55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category55", None)
        self.__aggregator_p2view_Category55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Products"):
                opp_val = getattr(old_value, "Products", None)
                if opp_val == self:
                    setattr(old_value, "Products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products"):
                opp_val = getattr(value, "Products", None)
                setattr(value, "Products", self)

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def isNested(self) -> bool:
        # TODO: Implement isNested method
        pass

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

class Bundle:

    pass
class aggregator_p2view_Fragment(Bundle):

    pass
class aggregator_p2view_Bundles:

    pass
class IUPresentationWithDetails:

    pass
class aggregator_p2view_Feature(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Feature: "Features" = None, aggregator_p2view_Feature66: "Bundles" = None, aggregator_p2view_Feature69: "Fragments" = None):
        self.aggregator_p2view_Feature = aggregator_p2view_Feature
        self.aggregator_p2view_Feature66 = aggregator_p2view_Feature66
        self.aggregator_p2view_Feature69 = aggregator_p2view_Feature69
        
    @property
    def aggregator_p2view_Feature(self):
        return self.__aggregator_p2view_Feature

    @aggregator_p2view_Feature.setter
    def aggregator_p2view_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature", None)
        self.__aggregator_p2view_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features64"):
                opp_val = getattr(old_value, "Features64", None)
                if opp_val == self:
                    setattr(old_value, "Features64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features64"):
                opp_val = getattr(value, "Features64", None)
                setattr(value, "Features64", self)

    @property
    def aggregator_p2view_Feature69(self):
        return self.__aggregator_p2view_Feature69

    @aggregator_p2view_Feature69.setter
    def aggregator_p2view_Feature69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature69", None)
        self.__aggregator_p2view_Feature69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments70"):
                opp_val = getattr(old_value, "Fragments70", None)
                if opp_val == self:
                    setattr(old_value, "Fragments70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments70"):
                opp_val = getattr(value, "Fragments70", None)
                setattr(value, "Fragments70", self)

    @property
    def aggregator_p2view_Feature66(self):
        return self.__aggregator_p2view_Feature66

    @aggregator_p2view_Feature66.setter
    def aggregator_p2view_Feature66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature66", None)
        self.__aggregator_p2view_Feature66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles67"):
                opp_val = getattr(old_value, "Bundles67", None)
                if opp_val == self:
                    setattr(old_value, "Bundles67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles67"):
                opp_val = getattr(value, "Bundles67", None)
                setattr(value, "Bundles67", self)

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

class aggregator_p2view_Product(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Product: "Features" = None, aggregator_p2view_Product120: "Bundles" = None, aggregator_p2view_Product123: "Fragments" = None):
        self.aggregator_p2view_Product = aggregator_p2view_Product
        self.aggregator_p2view_Product120 = aggregator_p2view_Product120
        self.aggregator_p2view_Product123 = aggregator_p2view_Product123
        
    @property
    def aggregator_p2view_Product123(self):
        return self.__aggregator_p2view_Product123

    @aggregator_p2view_Product123.setter
    def aggregator_p2view_Product123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product123", None)
        self.__aggregator_p2view_Product123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments124"):
                opp_val = getattr(old_value, "Fragments124", None)
                if opp_val == self:
                    setattr(old_value, "Fragments124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments124"):
                opp_val = getattr(value, "Fragments124", None)
                setattr(value, "Fragments124", self)

    @property
    def aggregator_p2view_Product120(self):
        return self.__aggregator_p2view_Product120

    @aggregator_p2view_Product120.setter
    def aggregator_p2view_Product120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product120", None)
        self.__aggregator_p2view_Product120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles121"):
                opp_val = getattr(old_value, "Bundles121", None)
                if opp_val == self:
                    setattr(old_value, "Bundles121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles121"):
                opp_val = getattr(value, "Bundles121", None)
                setattr(value, "Bundles121", self)

    @property
    def aggregator_p2view_Product(self):
        return self.__aggregator_p2view_Product

    @aggregator_p2view_Product.setter
    def aggregator_p2view_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product", None)
        self.__aggregator_p2view_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features118"):
                opp_val = getattr(old_value, "Features118", None)
                if opp_val == self:
                    setattr(old_value, "Features118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features118"):
                opp_val = getattr(value, "Features118", None)
                setattr(value, "Features118", self)

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

class aggregator_p2view_OtherIU(IUPresentationWithDetails):

    pass
class aggregator_p2view_Bundle(IUPresentationWithDetails):

    pass
class IUDetails:

    pass
class aggregator_Status:

    def __init__(self, code: str, message: str, aggregator_Status: "aggregator_StatusProvider" = None):
        self.code = code
        self.message = message
        self.aggregator_Status = aggregator_Status
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def aggregator_Status(self):
        return self.__aggregator_Status

    @aggregator_Status.setter
    def aggregator_Status(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Status__aggregator_Status", None)
        self.__aggregator_Status = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_StatusProvider"):
                opp_val = getattr(old_value, "aggregator_StatusProvider", None)
                if opp_val == self:
                    setattr(old_value, "aggregator_StatusProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_StatusProvider"):
                opp_val = getattr(value, "aggregator_StatusProvider", None)
                setattr(value, "aggregator_StatusProvider", self)

class aggregator_Property:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class aggregator_MetadataRepository:

    pass
class aggregator_MavenItem:

    def __init__(self, groupId: str, artifactId: str):
        self.groupId = groupId
        self.artifactId = artifactId
        
    @property
    def artifactId(self) -> str:
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId

    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

class InstallableUnitRequest:

    pass
class aggregator_StatusProvider(ABC):

    pass
class MetadataRepositoryReference:

    pass
class aggregator_LabelProvider(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class aggregator_InfosProvider:

    def __init__(self, errors: str, warnings: str, infos: str):
        self.errors = errors
        self.warnings = warnings
        self.infos = infos
        
    @property
    def warnings(self) -> str:
        return self.__warnings

    @warnings.setter
    def warnings(self, warnings: str):
        self.__warnings = warnings

    @property
    def errors(self) -> str:
        return self.__errors

    @errors.setter
    def errors(self, errors: str):
        self.__errors = errors

    @property
    def infos(self) -> str:
        return self.__infos

    @infos.setter
    def infos(self, infos: str):
        self.__infos = infos

class aggregator_IdentificationProvider(ABC):

    def __init__(self):
        
    def getIdentification(self) -> str:
        # TODO: Implement getIdentification method
        pass

class MapRule:

    pass
class aggregator_ValidConfigurationsRule(MapRule):

    pass
class aggregator_ExclusionRule(MapRule):

    pass
class aggregator_EnabledStatusProvider(ABC):

    def __init__(self, branchEnabled: bool, enabled: bool):
        self.branchEnabled = branchEnabled
        self.enabled = enabled
        
    @property
    def branchEnabled(self) -> bool:
        return self.__branchEnabled

    @branchEnabled.setter
    def branchEnabled(self, branchEnabled: bool):
        self.__branchEnabled = branchEnabled

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

class aggregator_DescriptionProvider:

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class IdentificationProvider:

    pass
class EnabledStatusProvider:

    pass
class aggregator_MappedUnit(InstallableUnitRequest, IdentificationProvider, EnabledStatusProvider):

    def __init__(self, aggregator_MappedUnit: set["aggregator_Configuration"] = None):
        self.aggregator_MappedUnit = aggregator_MappedUnit if aggregator_MappedUnit is not None else set()
        
    @property
    def aggregator_MappedUnit(self):
        return self.__aggregator_MappedUnit

    @aggregator_MappedUnit.setter
    def aggregator_MappedUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedUnit__aggregator_MappedUnit", None)
        self.__aggregator_MappedUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Configuration36"):
                    opp_val = getattr(item, "aggregator_Configuration36", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Configuration36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Configuration36"):
                    opp_val = getattr(item, "aggregator_Configuration36", None)
                    
                    setattr(item, "aggregator_Configuration36", self)
                    

    def getRequirement(self) -> str:
        # TODO: Implement getRequirement method
        pass

    def getFilter(self):
        # TODO: Implement getFilter method
        pass

class aggregator_ChildrenProvider(ABC):

    pass
class MappedUnit:

    pass
class aggregator_Category(MappedUnit):

    def __init__(self, labelOverride: str, aggregator_Category: "aggregator_MappedRepository" = None):
        self.labelOverride = labelOverride
        self.aggregator_Category = aggregator_Category
        
    @property
    def labelOverride(self) -> str:
        return self.__labelOverride

    @labelOverride.setter
    def labelOverride(self, labelOverride: str):
        self.__labelOverride = labelOverride

    @property
    def aggregator_Category(self):
        return self.__aggregator_Category

    @aggregator_Category.setter
    def aggregator_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Category__aggregator_Category", None)
        self.__aggregator_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_MappedRepository32"):
                opp_val = getattr(old_value, "aggregator_MappedRepository32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_MappedRepository32"):
                opp_val = getattr(value, "aggregator_MappedRepository32", None)
                if opp_val is None:
                    setattr(value, "aggregator_MappedRepository32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aggregator_Product(MappedUnit):

    pass
class aggregator_Feature(MappedUnit):

    pass
class aggregator_Bundle(MappedUnit):

    pass
class aggregator_AvailableVersionsHeader:

    pass
class aggregator_Contact:

    def __init__(self, name: str, email: str, Contact: "aggregator_Aggregation" = None, aggregator_Contact: "aggregator_Aggregation" = None, contacts: "aggregator_Aggregation" = None, aggregator_Contact16: "aggregator_Contribution" = None):
        self.name = name
        self.email = email
        self.Contact = Contact
        self.aggregator_Contact = aggregator_Contact
        self.contacts = contacts
        self.aggregator_Contact16 = aggregator_Contact16
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aggregator_Contact(self):
        return self.__aggregator_Contact

    @aggregator_Contact.setter
    def aggregator_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__aggregator_Contact", None)
        self.__aggregator_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregation7"):
                opp_val = getattr(old_value, "aggregator_Aggregation7", None)
                if opp_val == self:
                    setattr(old_value, "aggregator_Aggregation7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregation7"):
                opp_val = getattr(value, "aggregator_Aggregation7", None)
                setattr(value, "aggregator_Aggregation7", self)

    @property
    def Contact(self):
        return self.__Contact

    @Contact.setter
    def Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__Contact", None)
        self.__Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregation"):
                opp_val = getattr(old_value, "aggregation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregation"):
                opp_val = getattr(value, "aggregation", None)
                if opp_val is None:
                    setattr(value, "aggregation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Contact16(self):
        return self.__aggregator_Contact16

    @aggregator_Contact16.setter
    def aggregator_Contact16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__aggregator_Contact16", None)
        self.__aggregator_Contact16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution15"):
                opp_val = getattr(old_value, "aggregator_Contribution15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution15"):
                opp_val = getattr(value, "aggregator_Contribution15", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__contacts", None)
        self.__contacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Aggregation"):
                opp_val = getattr(old_value, "Aggregation", None)
                if opp_val == self:
                    setattr(old_value, "Aggregation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Aggregation"):
                opp_val = getattr(value, "Aggregation", None)
                setattr(value, "Aggregation", self)

class aggregator_Configuration(EnabledStatusProvider):

    def __init__(self, operatingSystem: str, windowSystem: str, architecture: str, aggregator_Configuration: "aggregator_Aggregation" = None, aggregator_Configuration36: "aggregator_MappedUnit" = None, aggregator_Configuration49: "aggregator_ValidConfigurationsRule" = None):
        self.operatingSystem = operatingSystem
        self.windowSystem = windowSystem
        self.architecture = architecture
        self.aggregator_Configuration = aggregator_Configuration
        self.aggregator_Configuration36 = aggregator_Configuration36
        self.aggregator_Configuration49 = aggregator_Configuration49
        
    @property
    def architecture(self) -> str:
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture

    @property
    def operatingSystem(self) -> str:
        return self.__operatingSystem

    @operatingSystem.setter
    def operatingSystem(self, operatingSystem: str):
        self.__operatingSystem = operatingSystem

    @property
    def windowSystem(self) -> str:
        return self.__windowSystem

    @windowSystem.setter
    def windowSystem(self, windowSystem: str):
        self.__windowSystem = windowSystem

    @property
    def aggregator_Configuration(self):
        return self.__aggregator_Configuration

    @aggregator_Configuration.setter
    def aggregator_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration", None)
        self.__aggregator_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregation2"):
                opp_val = getattr(old_value, "aggregator_Aggregation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregation2"):
                opp_val = getattr(value, "aggregator_Aggregation2", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Configuration36(self):
        return self.__aggregator_Configuration36

    @aggregator_Configuration36.setter
    def aggregator_Configuration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration36", None)
        self.__aggregator_Configuration36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_MappedUnit"):
                opp_val = getattr(old_value, "aggregator_MappedUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_MappedUnit"):
                opp_val = getattr(value, "aggregator_MappedUnit", None)
                if opp_val is None:
                    setattr(value, "aggregator_MappedUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Configuration49(self):
        return self.__aggregator_Configuration49

    @aggregator_Configuration49.setter
    def aggregator_Configuration49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration49", None)
        self.__aggregator_Configuration49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_ValidConfigurationsRule"):
                opp_val = getattr(old_value, "aggregator_ValidConfigurationsRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_ValidConfigurationsRule"):
                opp_val = getattr(value, "aggregator_ValidConfigurationsRule", None)
                if opp_val is None:
                    setattr(value, "aggregator_ValidConfigurationsRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getOSGiEnvironmentString(self) -> str:
        # TODO: Implement getOSGiEnvironmentString method
        pass

class InfosProvider:

    pass
class StatusProvider:

    pass
class aggregator_MavenMapping(InfosProvider, StatusProvider):

    def __init__(self, namePattern: str, groupId: str, artifactId: str, aggregator_MavenMapping: "aggregator_Aggregation" = None, aggregator_MavenMapping19: "aggregator_Contribution" = None):
        self.namePattern = namePattern
        self.groupId = groupId
        self.artifactId = artifactId
        self.aggregator_MavenMapping = aggregator_MavenMapping
        self.aggregator_MavenMapping19 = aggregator_MavenMapping19
        
    @property
    def namePattern(self) -> str:
        return self.__namePattern

    @namePattern.setter
    def namePattern(self, namePattern: str):
        self.__namePattern = namePattern

    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def artifactId(self) -> str:
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId

    @property
    def aggregator_MavenMapping(self):
        return self.__aggregator_MavenMapping

    @aggregator_MavenMapping.setter
    def aggregator_MavenMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MavenMapping__aggregator_MavenMapping", None)
        self.__aggregator_MavenMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregation9"):
                opp_val = getattr(old_value, "aggregator_Aggregation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregation9"):
                opp_val = getattr(value, "aggregator_Aggregation9", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_MavenMapping19(self):
        return self.__aggregator_MavenMapping19

    @aggregator_MavenMapping19.setter
    def aggregator_MavenMapping19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MavenMapping__aggregator_MavenMapping19", None)
        self.__aggregator_MavenMapping19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution18"):
                opp_val = getattr(old_value, "aggregator_Contribution18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution18"):
                opp_val = getattr(value, "aggregator_Contribution18", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def map(self, installableUnitID: str) -> str:
        # TODO: Implement map method
        pass

class aggregator_MetadataRepositoryReference(InfosProvider, StatusProvider, EnabledStatusProvider):

    def __init__(self, location: str, nature: str, aggregator_MetadataRepositoryReference: "aggregator_MetadataRepository" = None, aggregator_MetadataRepositoryReference44: "aggregator_ValidationSet" = None):
        self.location = location
        self.nature = nature
        self.aggregator_MetadataRepositoryReference = aggregator_MetadataRepositoryReference
        self.aggregator_MetadataRepositoryReference44 = aggregator_MetadataRepositoryReference44
        
    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def aggregator_MetadataRepositoryReference44(self):
        return self.__aggregator_MetadataRepositoryReference44

    @aggregator_MetadataRepositoryReference44.setter
    def aggregator_MetadataRepositoryReference44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MetadataRepositoryReference__aggregator_MetadataRepositoryReference44", None)
        self.__aggregator_MetadataRepositoryReference44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_ValidationSet43"):
                opp_val = getattr(old_value, "aggregator_ValidationSet43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_ValidationSet43"):
                opp_val = getattr(value, "aggregator_ValidationSet43", None)
                if opp_val is None:
                    setattr(value, "aggregator_ValidationSet43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_MetadataRepositoryReference(self):
        return self.__aggregator_MetadataRepositoryReference

    @aggregator_MetadataRepositoryReference.setter
    def aggregator_MetadataRepositoryReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MetadataRepositoryReference__aggregator_MetadataRepositoryReference", None)
        self.__aggregator_MetadataRepositoryReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_MetadataRepository"):
                opp_val = getattr(old_value, "aggregator_MetadataRepository", None)
                if opp_val == self:
                    setattr(old_value, "aggregator_MetadataRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_MetadataRepository"):
                opp_val = getattr(value, "aggregator_MetadataRepository", None)
                setattr(value, "aggregator_MetadataRepository", self)

    def onRepositoryLoad(self):
        # TODO: Implement onRepositoryLoad method
        pass

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def startRepositoryLoad(self, forceReload: bool):
        # TODO: Implement startRepositoryLoad method
        pass

    def getResolvedLocation(self) -> str:
        # TODO: Implement getResolvedLocation method
        pass

    def getAggregation(self) -> str:
        # TODO: Implement getAggregation method
        pass

    def cancelRepositoryLoad(self):
        # TODO: Implement cancelRepositoryLoad method
        pass

class aggregator_CustomCategory(InfosProvider, StatusProvider):

    def __init__(self, identifier: str, label: str, description: str, aggregator_CustomCategory: "aggregator_Aggregation" = None, categories: set["aggregator_Feature"] = None, CustomCategory: "aggregator_Feature" = None):
        self.identifier = identifier
        self.label = label
        self.description = description
        self.aggregator_CustomCategory = aggregator_CustomCategory
        self.categories = categories if categories is not None else set()
        self.CustomCategory = CustomCategory
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aggregator_CustomCategory(self):
        return self.__aggregator_CustomCategory

    @aggregator_CustomCategory.setter
    def aggregator_CustomCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_CustomCategory__aggregator_CustomCategory", None)
        self.__aggregator_CustomCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregation4"):
                opp_val = getattr(old_value, "aggregator_Aggregation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregation4"):
                opp_val = getattr(value, "aggregator_Aggregation4", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_CustomCategory__categories", None)
        self.__categories = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def CustomCategory(self):
        return self.__CustomCategory

    @CustomCategory.setter
    def CustomCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_CustomCategory__CustomCategory", None)
        self.__CustomCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                if opp_val is None:
                    setattr(value, "features", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DescriptionProvider:

    pass
class aggregator_MapRule(InstallableUnitRequest, DescriptionProvider, EnabledStatusProvider):

    pass
class aggregator_Contribution(DescriptionProvider, StatusProvider, EnabledStatusProvider, InfosProvider, IdentificationProvider):

    def __init__(self, label: str, aggregator_Contribution: set["aggregator_MappedRepository"] = None, aggregator_Contribution15: set["aggregator_Contact"] = None, aggregator_Contribution18: set["aggregator_MavenMapping"] = None, aggregator_Contribution41: "aggregator_ValidationSet" = None):
        self.label = label
        self.aggregator_Contribution = aggregator_Contribution if aggregator_Contribution is not None else set()
        self.aggregator_Contribution15 = aggregator_Contribution15 if aggregator_Contribution15 is not None else set()
        self.aggregator_Contribution18 = aggregator_Contribution18 if aggregator_Contribution18 is not None else set()
        self.aggregator_Contribution41 = aggregator_Contribution41
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aggregator_Contribution15(self):
        return self.__aggregator_Contribution15

    @aggregator_Contribution15.setter
    def aggregator_Contribution15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution15", None)
        self.__aggregator_Contribution15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Contact16"):
                    opp_val = getattr(item, "aggregator_Contact16", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Contact16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Contact16"):
                    opp_val = getattr(item, "aggregator_Contact16", None)
                    
                    setattr(item, "aggregator_Contact16", self)
                    

    @property
    def aggregator_Contribution(self):
        return self.__aggregator_Contribution

    @aggregator_Contribution.setter
    def aggregator_Contribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution", None)
        self.__aggregator_Contribution = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MappedRepository"):
                    opp_val = getattr(item, "aggregator_MappedRepository", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MappedRepository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MappedRepository"):
                    opp_val = getattr(item, "aggregator_MappedRepository", None)
                    
                    setattr(item, "aggregator_MappedRepository", self)
                    

    @property
    def aggregator_Contribution41(self):
        return self.__aggregator_Contribution41

    @aggregator_Contribution41.setter
    def aggregator_Contribution41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution41", None)
        self.__aggregator_Contribution41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_ValidationSet40"):
                opp_val = getattr(old_value, "aggregator_ValidationSet40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_ValidationSet40"):
                opp_val = getattr(value, "aggregator_ValidationSet40", None)
                if opp_val is None:
                    setattr(value, "aggregator_ValidationSet40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Contribution18(self):
        return self.__aggregator_Contribution18

    @aggregator_Contribution18.setter
    def aggregator_Contribution18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution18", None)
        self.__aggregator_Contribution18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MavenMapping19"):
                    opp_val = getattr(item, "aggregator_MavenMapping19", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MavenMapping19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MavenMapping19"):
                    opp_val = getattr(item, "aggregator_MavenMapping19", None)
                    
                    setattr(item, "aggregator_MavenMapping19", self)
                    

    def getAllMavenMappings(self) -> str:
        # TODO: Implement getAllMavenMappings method
        pass

    def getRepositories(self, enabledOnly: bool) -> str:
        # TODO: Implement getRepositories method
        pass

class aggregator_MappedRepository(IdentificationProvider, DescriptionProvider, MetadataRepositoryReference):

    def __init__(self, mirrorArtifacts: bool, categoryPrefix: str, aggregator_MappedRepository: "aggregator_Contribution" = None, aggregator_MappedRepository26: set["aggregator_Product"] = None, aggregator_MappedRepository28: set["aggregator_Bundle"] = None, aggregator_MappedRepository30: set["aggregator_Feature"] = None, aggregator_MappedRepository32: set["aggregator_Category"] = None, aggregator_MappedRepository34: set["aggregator_MapRule"] = None):
        self.mirrorArtifacts = mirrorArtifacts
        self.categoryPrefix = categoryPrefix
        self.aggregator_MappedRepository = aggregator_MappedRepository
        self.aggregator_MappedRepository26 = aggregator_MappedRepository26 if aggregator_MappedRepository26 is not None else set()
        self.aggregator_MappedRepository28 = aggregator_MappedRepository28 if aggregator_MappedRepository28 is not None else set()
        self.aggregator_MappedRepository30 = aggregator_MappedRepository30 if aggregator_MappedRepository30 is not None else set()
        self.aggregator_MappedRepository32 = aggregator_MappedRepository32 if aggregator_MappedRepository32 is not None else set()
        self.aggregator_MappedRepository34 = aggregator_MappedRepository34 if aggregator_MappedRepository34 is not None else set()
        
    @property
    def categoryPrefix(self) -> str:
        return self.__categoryPrefix

    @categoryPrefix.setter
    def categoryPrefix(self, categoryPrefix: str):
        self.__categoryPrefix = categoryPrefix

    @property
    def mirrorArtifacts(self) -> bool:
        return self.__mirrorArtifacts

    @mirrorArtifacts.setter
    def mirrorArtifacts(self, mirrorArtifacts: bool):
        self.__mirrorArtifacts = mirrorArtifacts

    @property
    def aggregator_MappedRepository(self):
        return self.__aggregator_MappedRepository

    @aggregator_MappedRepository.setter
    def aggregator_MappedRepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository", None)
        self.__aggregator_MappedRepository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution"):
                opp_val = getattr(old_value, "aggregator_Contribution", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution"):
                opp_val = getattr(value, "aggregator_Contribution", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_MappedRepository32(self):
        return self.__aggregator_MappedRepository32

    @aggregator_MappedRepository32.setter
    def aggregator_MappedRepository32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository32", None)
        self.__aggregator_MappedRepository32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Category"):
                    opp_val = getattr(item, "aggregator_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Category"):
                    opp_val = getattr(item, "aggregator_Category", None)
                    
                    setattr(item, "aggregator_Category", self)
                    

    @property
    def aggregator_MappedRepository30(self):
        return self.__aggregator_MappedRepository30

    @aggregator_MappedRepository30.setter
    def aggregator_MappedRepository30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository30", None)
        self.__aggregator_MappedRepository30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Feature"):
                    opp_val = getattr(item, "aggregator_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Feature"):
                    opp_val = getattr(item, "aggregator_Feature", None)
                    
                    setattr(item, "aggregator_Feature", self)
                    

    @property
    def aggregator_MappedRepository28(self):
        return self.__aggregator_MappedRepository28

    @aggregator_MappedRepository28.setter
    def aggregator_MappedRepository28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository28", None)
        self.__aggregator_MappedRepository28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Bundle"):
                    opp_val = getattr(item, "aggregator_Bundle", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Bundle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Bundle"):
                    opp_val = getattr(item, "aggregator_Bundle", None)
                    
                    setattr(item, "aggregator_Bundle", self)
                    

    @property
    def aggregator_MappedRepository26(self):
        return self.__aggregator_MappedRepository26

    @aggregator_MappedRepository26.setter
    def aggregator_MappedRepository26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository26", None)
        self.__aggregator_MappedRepository26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Product"):
                    opp_val = getattr(item, "aggregator_Product", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Product"):
                    opp_val = getattr(item, "aggregator_Product", None)
                    
                    setattr(item, "aggregator_Product", self)
                    

    @property
    def aggregator_MappedRepository34(self):
        return self.__aggregator_MappedRepository34

    @aggregator_MappedRepository34.setter
    def aggregator_MappedRepository34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository34", None)
        self.__aggregator_MappedRepository34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MapRule"):
                    opp_val = getattr(item, "aggregator_MapRule", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MapRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MapRule"):
                    opp_val = getattr(item, "aggregator_MapRule", None)
                    
                    setattr(item, "aggregator_MapRule", self)
                    

    def getMapRules(self, enabledOnly: bool) -> MapRule:
        # TODO: Implement getMapRules method
        pass

    def isMapExclusive(self) -> bool:
        # TODO: Implement isMapExclusive method
        pass

    def getUnits(self, enabledOnly: bool) -> MappedUnit:
        # TODO: Implement getUnits method
        pass

class aggregator_ValidationSet(DescriptionProvider, StatusProvider, EnabledStatusProvider, InfosProvider, IdentificationProvider):

    def __init__(self, abstract: bool, extension: bool, label: str, aggregator_ValidationSet: "aggregator_Aggregation" = None, aggregator_ValidationSet40: set["aggregator_Contribution"] = None, aggregator_ValidationSet43: set["aggregator_MetadataRepositoryReference"] = None, aggregator_ValidationSet47: "aggregator_ValidationSet" = None, aggregator_ValidationSet45: set["aggregator_ValidationSet"] = None):
        self.abstract = abstract
        self.extension = extension
        self.label = label
        self.aggregator_ValidationSet = aggregator_ValidationSet
        self.aggregator_ValidationSet40 = aggregator_ValidationSet40 if aggregator_ValidationSet40 is not None else set()
        self.aggregator_ValidationSet43 = aggregator_ValidationSet43 if aggregator_ValidationSet43 is not None else set()
        self.aggregator_ValidationSet47 = aggregator_ValidationSet47
        self.aggregator_ValidationSet45 = aggregator_ValidationSet45 if aggregator_ValidationSet45 is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def extension(self) -> bool:
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension

    @property
    def aggregator_ValidationSet40(self):
        return self.__aggregator_ValidationSet40

    @aggregator_ValidationSet40.setter
    def aggregator_ValidationSet40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_ValidationSet__aggregator_ValidationSet40", None)
        self.__aggregator_ValidationSet40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Contribution41"):
                    opp_val = getattr(item, "aggregator_Contribution41", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Contribution41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Contribution41"):
                    opp_val = getattr(item, "aggregator_Contribution41", None)
                    
                    setattr(item, "aggregator_Contribution41", self)
                    

    @property
    def aggregator_ValidationSet43(self):
        return self.__aggregator_ValidationSet43

    @aggregator_ValidationSet43.setter
    def aggregator_ValidationSet43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_ValidationSet__aggregator_ValidationSet43", None)
        self.__aggregator_ValidationSet43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MetadataRepositoryReference44"):
                    opp_val = getattr(item, "aggregator_MetadataRepositoryReference44", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MetadataRepositoryReference44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MetadataRepositoryReference44"):
                    opp_val = getattr(item, "aggregator_MetadataRepositoryReference44", None)
                    
                    setattr(item, "aggregator_MetadataRepositoryReference44", self)
                    

    @property
    def aggregator_ValidationSet47(self):
        return self.__aggregator_ValidationSet47

    @aggregator_ValidationSet47.setter
    def aggregator_ValidationSet47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_ValidationSet__aggregator_ValidationSet47", None)
        self.__aggregator_ValidationSet47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_ValidationSet45"):
                opp_val = getattr(old_value, "aggregator_ValidationSet45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_ValidationSet45"):
                opp_val = getattr(value, "aggregator_ValidationSet45", None)
                if opp_val is None:
                    setattr(value, "aggregator_ValidationSet45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_ValidationSet(self):
        return self.__aggregator_ValidationSet

    @aggregator_ValidationSet.setter
    def aggregator_ValidationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_ValidationSet__aggregator_ValidationSet", None)
        self.__aggregator_ValidationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregation"):
                opp_val = getattr(old_value, "aggregator_Aggregation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregation"):
                opp_val = getattr(value, "aggregator_Aggregation", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_ValidationSet45(self):
        return self.__aggregator_ValidationSet45

    @aggregator_ValidationSet45.setter
    def aggregator_ValidationSet45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_ValidationSet__aggregator_ValidationSet45", None)
        self.__aggregator_ValidationSet45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_ValidationSet47"):
                    opp_val = getattr(item, "aggregator_ValidationSet47", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_ValidationSet47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_ValidationSet47"):
                    opp_val = getattr(item, "aggregator_ValidationSet47", None)
                    
                    setattr(item, "aggregator_ValidationSet47", self)
                    

    def getDeclaredValidationRepositories(self) -> MetadataRepositoryReference:
        # TODO: Implement getDeclaredValidationRepositories method
        pass

    def isExtensionOf(self, validationSet: str) -> bool:
        # TODO: Implement isExtensionOf method
        pass

    def getAllValidationRepositories(self) -> MetadataRepositoryReference:
        # TODO: Implement getAllValidationRepositories method
        pass

    def getAllContributions(self) -> str:
        # TODO: Implement getAllContributions method
        pass

    def getDeclaredContributions(self) -> str:
        # TODO: Implement getDeclaredContributions method
        pass

class aggregator_Aggregation(InfosProvider, StatusProvider, DescriptionProvider):

    def __init__(self, label: str, buildRoot: str, packedStrategy: str, sendmail: bool, type: str, mavenResult: bool, aggregator_Aggregation: set["aggregator_ValidationSet"] = None, aggregator_Aggregation2: set["aggregator_Configuration"] = None, aggregator_Aggregation4: set["aggregator_CustomCategory"] = None, aggregation: set["aggregator_Contact"] = None, aggregator_Aggregation7: "aggregator_Contact" = None, aggregator_Aggregation9: set["aggregator_MavenMapping"] = None, Aggregation: "aggregator_Contact" = None):
        self.label = label
        self.buildRoot = buildRoot
        self.packedStrategy = packedStrategy
        self.sendmail = sendmail
        self.type = type
        self.mavenResult = mavenResult
        self.aggregator_Aggregation = aggregator_Aggregation if aggregator_Aggregation is not None else set()
        self.aggregator_Aggregation2 = aggregator_Aggregation2 if aggregator_Aggregation2 is not None else set()
        self.aggregator_Aggregation4 = aggregator_Aggregation4 if aggregator_Aggregation4 is not None else set()
        self.aggregation = aggregation if aggregation is not None else set()
        self.aggregator_Aggregation7 = aggregator_Aggregation7
        self.aggregator_Aggregation9 = aggregator_Aggregation9 if aggregator_Aggregation9 is not None else set()
        self.Aggregation = Aggregation
        
    @property
    def sendmail(self) -> bool:
        return self.__sendmail

    @sendmail.setter
    def sendmail(self, sendmail: bool):
        self.__sendmail = sendmail

    @property
    def mavenResult(self) -> bool:
        return self.__mavenResult

    @mavenResult.setter
    def mavenResult(self, mavenResult: bool):
        self.__mavenResult = mavenResult

    @property
    def packedStrategy(self) -> str:
        return self.__packedStrategy

    @packedStrategy.setter
    def packedStrategy(self, packedStrategy: str):
        self.__packedStrategy = packedStrategy

    @property
    def buildRoot(self) -> str:
        return self.__buildRoot

    @buildRoot.setter
    def buildRoot(self, buildRoot: str):
        self.__buildRoot = buildRoot

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aggregator_Aggregation9(self):
        return self.__aggregator_Aggregation9

    @aggregator_Aggregation9.setter
    def aggregator_Aggregation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregator_Aggregation9", None)
        self.__aggregator_Aggregation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MavenMapping"):
                    opp_val = getattr(item, "aggregator_MavenMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MavenMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MavenMapping"):
                    opp_val = getattr(item, "aggregator_MavenMapping", None)
                    
                    setattr(item, "aggregator_MavenMapping", self)
                    

    @property
    def aggregator_Aggregation4(self):
        return self.__aggregator_Aggregation4

    @aggregator_Aggregation4.setter
    def aggregator_Aggregation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregator_Aggregation4", None)
        self.__aggregator_Aggregation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_CustomCategory"):
                    opp_val = getattr(item, "aggregator_CustomCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_CustomCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_CustomCategory"):
                    opp_val = getattr(item, "aggregator_CustomCategory", None)
                    
                    setattr(item, "aggregator_CustomCategory", self)
                    

    @property
    def aggregator_Aggregation7(self):
        return self.__aggregator_Aggregation7

    @aggregator_Aggregation7.setter
    def aggregator_Aggregation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregator_Aggregation7", None)
        self.__aggregator_Aggregation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contact"):
                opp_val = getattr(old_value, "aggregator_Contact", None)
                if opp_val == self:
                    setattr(old_value, "aggregator_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contact"):
                opp_val = getattr(value, "aggregator_Contact", None)
                setattr(value, "aggregator_Contact", self)

    @property
    def aggregator_Aggregation2(self):
        return self.__aggregator_Aggregation2

    @aggregator_Aggregation2.setter
    def aggregator_Aggregation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregator_Aggregation2", None)
        self.__aggregator_Aggregation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Configuration"):
                    opp_val = getattr(item, "aggregator_Configuration", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Configuration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Configuration"):
                    opp_val = getattr(item, "aggregator_Configuration", None)
                    
                    setattr(item, "aggregator_Configuration", self)
                    

    @property
    def Aggregation(self):
        return self.__Aggregation

    @Aggregation.setter
    def Aggregation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__Aggregation", None)
        self.__Aggregation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts"):
                opp_val = getattr(old_value, "contacts", None)
                if opp_val == self:
                    setattr(old_value, "contacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts"):
                opp_val = getattr(value, "contacts", None)
                setattr(value, "contacts", self)

    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregation", None)
        self.__aggregation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Contact"):
                    opp_val = getattr(item, "Contact", None)
                    
                    if opp_val == self:
                        setattr(item, "Contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Contact"):
                    opp_val = getattr(item, "Contact", None)
                    
                    setattr(item, "Contact", self)
                    

    @property
    def aggregator_Aggregation(self):
        return self.__aggregator_Aggregation

    @aggregator_Aggregation.setter
    def aggregator_Aggregation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregation__aggregator_Aggregation", None)
        self.__aggregator_Aggregation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_ValidationSet"):
                    opp_val = getattr(item, "aggregator_ValidationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_ValidationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_ValidationSet"):
                    opp_val = getattr(item, "aggregator_ValidationSet", None)
                    
                    setattr(item, "aggregator_ValidationSet", self)
                    

    def getAllContributions(self, enabledOnly: bool) -> str:
        # TODO: Implement getAllContributions method
        pass

    def getAllMetadataRepositoryReferences(self, enabledOnly: bool) -> str:
        # TODO: Implement getAllMetadataRepositoryReferences method
        pass

    def getValidationSets(self, enabledOnly: bool) -> str:
        # TODO: Implement getValidationSets method
        pass

class aggregator_InstallableUnitRequest(InfosProvider, StatusProvider, DescriptionProvider):

    def __init__(self, name: str, versionRange: str, InstallableUnitRequest: "aggregator_AvailableVersionsHeader" = None, installableUnitRequest: "aggregator_AvailableVersionsHeader" = None, aggregator_InstallableUnitRequest: set["aggregator_AvailableVersion"] = None):
        self.name = name
        self.versionRange = versionRange
        self.InstallableUnitRequest = InstallableUnitRequest
        self.installableUnitRequest = installableUnitRequest
        self.aggregator_InstallableUnitRequest = aggregator_InstallableUnitRequest if aggregator_InstallableUnitRequest is not None else set()
        
    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aggregator_InstallableUnitRequest(self):
        return self.__aggregator_InstallableUnitRequest

    @aggregator_InstallableUnitRequest.setter
    def aggregator_InstallableUnitRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_InstallableUnitRequest__aggregator_InstallableUnitRequest", None)
        self.__aggregator_InstallableUnitRequest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_AvailableVersion24"):
                    opp_val = getattr(item, "aggregator_AvailableVersion24", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_AvailableVersion24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_AvailableVersion24"):
                    opp_val = getattr(item, "aggregator_AvailableVersion24", None)
                    
                    setattr(item, "aggregator_AvailableVersion24", self)
                    

    @property
    def installableUnitRequest(self):
        return self.__installableUnitRequest

    @installableUnitRequest.setter
    def installableUnitRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_InstallableUnitRequest__installableUnitRequest", None)
        self.__installableUnitRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AvailableVersionsHeader"):
                opp_val = getattr(old_value, "AvailableVersionsHeader", None)
                if opp_val == self:
                    setattr(old_value, "AvailableVersionsHeader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AvailableVersionsHeader"):
                opp_val = getattr(value, "AvailableVersionsHeader", None)
                setattr(value, "AvailableVersionsHeader", self)

    @property
    def InstallableUnitRequest(self):
        return self.__InstallableUnitRequest

    @InstallableUnitRequest.setter
    def InstallableUnitRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_InstallableUnitRequest__InstallableUnitRequest", None)
        self.__InstallableUnitRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "availableVersionsHeader"):
                opp_val = getattr(old_value, "availableVersionsHeader", None)
                if opp_val == self:
                    setattr(old_value, "availableVersionsHeader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "availableVersionsHeader"):
                opp_val = getattr(value, "availableVersionsHeader", None)
                setattr(value, "availableVersionsHeader", self)

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def resolveAsSingleton(self) -> str:
        # TODO: Implement resolveAsSingleton method
        pass

    def resolveAvailableVersions(self, updateOnly: str):
        # TODO: Implement resolveAvailableVersions method
        pass

    def resolveAsSingleton(self, forceResolve: bool) -> str:
        # TODO: Implement resolveAsSingleton method
        pass

    def isMappedRepositoryBroken(self) -> bool:
        # TODO: Implement isMappedRepositoryBroken method
        pass

class aggregator_AvailableVersion:

    def __init__(self, versionMatch: str, version: str, filter: str, availableFrom: str, aggregator_AvailableVersion: "aggregator_AvailableVersionsHeader" = None, aggregator_AvailableVersion24: "aggregator_InstallableUnitRequest" = None):
        self.versionMatch = versionMatch
        self.version = version
        self.filter = filter
        self.availableFrom = availableFrom
        self.aggregator_AvailableVersion = aggregator_AvailableVersion
        self.aggregator_AvailableVersion24 = aggregator_AvailableVersion24
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def versionMatch(self) -> str:
        return self.__versionMatch

    @versionMatch.setter
    def versionMatch(self, versionMatch: str):
        self.__versionMatch = versionMatch

    @property
    def availableFrom(self) -> str:
        return self.__availableFrom

    @availableFrom.setter
    def availableFrom(self, availableFrom: str):
        self.__availableFrom = availableFrom

    @property
    def aggregator_AvailableVersion24(self):
        return self.__aggregator_AvailableVersion24

    @aggregator_AvailableVersion24.setter
    def aggregator_AvailableVersion24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_AvailableVersion__aggregator_AvailableVersion24", None)
        self.__aggregator_AvailableVersion24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_InstallableUnitRequest"):
                opp_val = getattr(old_value, "aggregator_InstallableUnitRequest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_InstallableUnitRequest"):
                opp_val = getattr(value, "aggregator_InstallableUnitRequest", None)
                if opp_val is None:
                    setattr(value, "aggregator_InstallableUnitRequest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_AvailableVersion(self):
        return self.__aggregator_AvailableVersion

    @aggregator_AvailableVersion.setter
    def aggregator_AvailableVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_AvailableVersion__aggregator_AvailableVersion", None)
        self.__aggregator_AvailableVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_AvailableVersionsHeader"):
                opp_val = getattr(old_value, "aggregator_AvailableVersionsHeader", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_AvailableVersionsHeader"):
                opp_val = getattr(value, "aggregator_AvailableVersionsHeader", None)
                if opp_val is None:
                    setattr(value, "aggregator_AvailableVersionsHeader", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
