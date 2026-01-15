from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PackedStrategy(Enum):
    Copy = "Copy"
    Verify = "Verify"
    UnpackAsSibling = "UnpackAsSibling"
    Unpack = "Unpack"
    Skip = "Skip"
class OperatingSystem(Enum):
    Win32 = "Win32"
    Linux = "Linux"
    MacOSX = "MacOSX"
    AIX = "AIX"
    HPUX = "HPUX"
    Solaris = "Solaris"
    QNX = "QNX"
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
class WindowSystem(Enum):
    Motif = "Motif"
    Photon = "Photon"
    Win32 = "Win32"
    GTK = "GTK"
    Carbon = "Carbon"
    Cocoa = "Cocoa"
class InstallableUnitType(Enum):
    BUNDLE = "BUNDLE"
    FEATURE = "FEATURE"
    PRODUCT = "PRODUCT"
    CATEGORY = "CATEGORY"
    FRAGMENT = "FRAGMENT"
    OTHER = "OTHER"
class StatusCode(Enum):
    WAITING = "WAITING"
    OK = "OK"
    BROKEN = "BROKEN"
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

class aggregator_p2view_Touchpoints:

    pass
class p2_IProvidedCapability:

    pass
class LabelProvider:

    pass
class aggregator_p2view_ProvidedCapabilityWrapper(p2_IProvidedCapability, LabelProvider):

    pass
class p2_IRequiredCapability:

    pass
class aggregator_p2view_RequiredCapabilityWrapper(LabelProvider, p2_IRequiredCapability):

    pass
class Touchpoints:

    pass
class ProvidedCapabilities:

    pass
class RequiredCapabilities:

    pass
class aggregator_p2view_IUDetails:

    pass
class IUDetails:

    pass
class ProvidedCapabilityWrapper:

    pass
class aggregator_p2view_ProvidedCapabilities:

    pass
class RequiredCapabilityWrapper:

    pass
class aggregator_p2view_RequiredCapabilities:

    pass
class p2view_aggregator_Property:

    pass
class aggregator_p2view_Properties:

    pass
class aggregator_p2view_Bundles:

    pass
class IUPresentationWithDetails:

    pass
class aggregator_p2view_Product(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Product: "Features" = None, aggregator_p2view_Product122: "Bundles" = None, aggregator_p2view_Product125: "Fragments" = None):
        self.aggregator_p2view_Product = aggregator_p2view_Product
        self.aggregator_p2view_Product122 = aggregator_p2view_Product122
        self.aggregator_p2view_Product125 = aggregator_p2view_Product125
        
    @property
    def aggregator_p2view_Product125(self):
        return self.__aggregator_p2view_Product125

    @aggregator_p2view_Product125.setter
    def aggregator_p2view_Product125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product125", None)
        self.__aggregator_p2view_Product125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments126"):
                opp_val = getattr(old_value, "Fragments126", None)
                if opp_val == self:
                    setattr(old_value, "Fragments126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments126"):
                opp_val = getattr(value, "Fragments126", None)
                setattr(value, "Fragments126", self)

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
            if hasattr(old_value, "Features120"):
                opp_val = getattr(old_value, "Features120", None)
                if opp_val == self:
                    setattr(old_value, "Features120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features120"):
                opp_val = getattr(value, "Features120", None)
                setattr(value, "Features120", self)

    @property
    def aggregator_p2view_Product122(self):
        return self.__aggregator_p2view_Product122

    @aggregator_p2view_Product122.setter
    def aggregator_p2view_Product122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product122", None)
        self.__aggregator_p2view_Product122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles123"):
                opp_val = getattr(old_value, "Bundles123", None)
                if opp_val == self:
                    setattr(old_value, "Bundles123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles123"):
                opp_val = getattr(value, "Bundles123", None)
                setattr(value, "Bundles123", self)

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

class aggregator_p2view_Bundle(IUPresentationWithDetails):

    pass
class aggregator_p2view_OtherIU(IUPresentationWithDetails):

    pass
class aggregator_p2view_Feature(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Feature: "Features" = None, aggregator_p2view_Feature114: "Bundles" = None, aggregator_p2view_Feature117: "Fragments" = None):
        self.aggregator_p2view_Feature = aggregator_p2view_Feature
        self.aggregator_p2view_Feature114 = aggregator_p2view_Feature114
        self.aggregator_p2view_Feature117 = aggregator_p2view_Feature117
        
    @property
    def aggregator_p2view_Feature117(self):
        return self.__aggregator_p2view_Feature117

    @aggregator_p2view_Feature117.setter
    def aggregator_p2view_Feature117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature117", None)
        self.__aggregator_p2view_Feature117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments118"):
                opp_val = getattr(old_value, "Fragments118", None)
                if opp_val == self:
                    setattr(old_value, "Fragments118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments118"):
                opp_val = getattr(value, "Fragments118", None)
                setattr(value, "Fragments118", self)

    @property
    def aggregator_p2view_Feature114(self):
        return self.__aggregator_p2view_Feature114

    @aggregator_p2view_Feature114.setter
    def aggregator_p2view_Feature114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature114", None)
        self.__aggregator_p2view_Feature114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles115"):
                opp_val = getattr(old_value, "Bundles115", None)
                if opp_val == self:
                    setattr(old_value, "Bundles115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles115"):
                opp_val = getattr(value, "Bundles115", None)
                setattr(value, "Bundles115", self)

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
            if hasattr(old_value, "Features112"):
                opp_val = getattr(old_value, "Features112", None)
                if opp_val == self:
                    setattr(old_value, "Features112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features112"):
                opp_val = getattr(value, "Features112", None)
                setattr(value, "Features112", self)

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

class IUPresentation:

    pass
class aggregator_p2view_Category(IUPresentation):

    def __init__(self, aggregator_p2view_Category: "Categories" = None, aggregator_p2view_Category98: "Features" = None, aggregator_p2view_Category101: "Products" = None, aggregator_p2view_Category110: "IUDetails" = None, aggregator_p2view_Category104: "Bundles" = None, aggregator_p2view_Category107: "Fragments" = None):
        self.aggregator_p2view_Category = aggregator_p2view_Category
        self.aggregator_p2view_Category98 = aggregator_p2view_Category98
        self.aggregator_p2view_Category101 = aggregator_p2view_Category101
        self.aggregator_p2view_Category110 = aggregator_p2view_Category110
        self.aggregator_p2view_Category104 = aggregator_p2view_Category104
        self.aggregator_p2view_Category107 = aggregator_p2view_Category107
        
    @property
    def aggregator_p2view_Category101(self):
        return self.__aggregator_p2view_Category101

    @aggregator_p2view_Category101.setter
    def aggregator_p2view_Category101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category101", None)
        self.__aggregator_p2view_Category101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Products102"):
                opp_val = getattr(old_value, "Products102", None)
                if opp_val == self:
                    setattr(old_value, "Products102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products102"):
                opp_val = getattr(value, "Products102", None)
                setattr(value, "Products102", self)

    @property
    def aggregator_p2view_Category107(self):
        return self.__aggregator_p2view_Category107

    @aggregator_p2view_Category107.setter
    def aggregator_p2view_Category107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category107", None)
        self.__aggregator_p2view_Category107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments108"):
                opp_val = getattr(old_value, "Fragments108", None)
                if opp_val == self:
                    setattr(old_value, "Fragments108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments108"):
                opp_val = getattr(value, "Fragments108", None)
                setattr(value, "Fragments108", self)

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
            if hasattr(old_value, "Categories96"):
                opp_val = getattr(old_value, "Categories96", None)
                if opp_val == self:
                    setattr(old_value, "Categories96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Categories96"):
                opp_val = getattr(value, "Categories96", None)
                setattr(value, "Categories96", self)

    @property
    def aggregator_p2view_Category98(self):
        return self.__aggregator_p2view_Category98

    @aggregator_p2view_Category98.setter
    def aggregator_p2view_Category98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category98", None)
        self.__aggregator_p2view_Category98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features99"):
                opp_val = getattr(old_value, "Features99", None)
                if opp_val == self:
                    setattr(old_value, "Features99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features99"):
                opp_val = getattr(value, "Features99", None)
                setattr(value, "Features99", self)

    @property
    def aggregator_p2view_Category104(self):
        return self.__aggregator_p2view_Category104

    @aggregator_p2view_Category104.setter
    def aggregator_p2view_Category104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category104", None)
        self.__aggregator_p2view_Category104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles105"):
                opp_val = getattr(old_value, "Bundles105", None)
                if opp_val == self:
                    setattr(old_value, "Bundles105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles105"):
                opp_val = getattr(value, "Bundles105", None)
                setattr(value, "Bundles105", self)

    @property
    def aggregator_p2view_Category110(self):
        return self.__aggregator_p2view_Category110

    @aggregator_p2view_Category110.setter
    def aggregator_p2view_Category110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category110", None)
        self.__aggregator_p2view_Category110 = value
        
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

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def isNested(self) -> bool:
        # TODO: Implement isNested method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
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

class aggregator_p2view_IUPresentation(ABC):

    def __init__(self, id: str, version: str, name: str, label: str, description: str, type: str, aggregator_p2view_IUPresentation: "InstallableUnit" = None):
        self.id = id
        self.version = version
        self.name = name
        self.label = label
        self.description = description
        self.type = type
        self.aggregator_p2view_IUPresentation = aggregator_p2view_IUPresentation
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

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
    def aggregator_p2view_IUPresentation(self):
        return self.__aggregator_p2view_IUPresentation

    @aggregator_p2view_IUPresentation.setter
    def aggregator_p2view_IUPresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_IUPresentation__aggregator_p2view_IUPresentation", None)
        self.__aggregator_p2view_IUPresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InstallableUnit94"):
                opp_val = getattr(old_value, "InstallableUnit94", None)
                if opp_val == self:
                    setattr(old_value, "InstallableUnit94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InstallableUnit94"):
                opp_val = getattr(value, "InstallableUnit94", None)
                setattr(value, "InstallableUnit94", self)

class OtherIU:

    pass
class aggregator_p2view_Miscellaneous:

    pass
class Fragment:

    pass
class aggregator_p2view_Fragments:

    pass
class Bundle:

    pass
class aggregator_p2view_Fragment(Bundle):

    pass
class aggregator_p2view_MetadataRepositoryStructuredView:

    def __init__(self, loaded: bool, name: str, aggregator_p2view_MetadataRepositoryStructuredView: "InstallableUnits" = None, aggregator_p2view_MetadataRepositoryStructuredView71: "Properties" = None, aggregator_p2view_MetadataRepositoryStructuredView73: "MetadataRepository" = None):
        self.loaded = loaded
        self.name = name
        self.aggregator_p2view_MetadataRepositoryStructuredView = aggregator_p2view_MetadataRepositoryStructuredView
        self.aggregator_p2view_MetadataRepositoryStructuredView71 = aggregator_p2view_MetadataRepositoryStructuredView71
        self.aggregator_p2view_MetadataRepositoryStructuredView73 = aggregator_p2view_MetadataRepositoryStructuredView73
        
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
    def aggregator_p2view_MetadataRepositoryStructuredView73(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView73

    @aggregator_p2view_MetadataRepositoryStructuredView73.setter
    def aggregator_p2view_MetadataRepositoryStructuredView73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView73", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetadataRepository74"):
                opp_val = getattr(old_value, "MetadataRepository74", None)
                if opp_val == self:
                    setattr(old_value, "MetadataRepository74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetadataRepository74"):
                opp_val = getattr(value, "MetadataRepository74", None)
                setattr(value, "MetadataRepository74", self)

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView71(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView71

    @aggregator_p2view_MetadataRepositoryStructuredView71.setter
    def aggregator_p2view_MetadataRepositoryStructuredView71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView71", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Properties"):
                opp_val = getattr(old_value, "Properties", None)
                if opp_val == self:
                    setattr(old_value, "Properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Properties"):
                opp_val = getattr(value, "Properties", None)
                setattr(value, "Properties", self)

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

class Product:

    pass
class aggregator_p2view_Products:

    pass
class Feature:

    pass
class aggregator_p2view_Features:

    pass
class Category:

    pass
class aggregator_p2view_Categories:

    pass
class Miscellaneous:

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
class aggregator_p2view_InstallableUnits:

    def __init__(self, aggregator_p2view_InstallableUnits: "Categories" = None, aggregator_p2view_InstallableUnits77: "Features" = None, aggregator_p2view_InstallableUnits79: "Products" = None, aggregator_p2view_InstallableUnits81: "Bundles" = None, aggregator_p2view_InstallableUnits83: "Fragments" = None, aggregator_p2view_InstallableUnits85: "Miscellaneous" = None):
        self.aggregator_p2view_InstallableUnits = aggregator_p2view_InstallableUnits
        self.aggregator_p2view_InstallableUnits77 = aggregator_p2view_InstallableUnits77
        self.aggregator_p2view_InstallableUnits79 = aggregator_p2view_InstallableUnits79
        self.aggregator_p2view_InstallableUnits81 = aggregator_p2view_InstallableUnits81
        self.aggregator_p2view_InstallableUnits83 = aggregator_p2view_InstallableUnits83
        self.aggregator_p2view_InstallableUnits85 = aggregator_p2view_InstallableUnits85
        
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
            if hasattr(old_value, "Products"):
                opp_val = getattr(old_value, "Products", None)
                if opp_val == self:
                    setattr(old_value, "Products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products"):
                opp_val = getattr(value, "Products", None)
                setattr(value, "Products", self)

    @property
    def aggregator_p2view_InstallableUnits77(self):
        return self.__aggregator_p2view_InstallableUnits77

    @aggregator_p2view_InstallableUnits77.setter
    def aggregator_p2view_InstallableUnits77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits77", None)
        self.__aggregator_p2view_InstallableUnits77 = value
        
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
    def aggregator_p2view_InstallableUnits81(self):
        return self.__aggregator_p2view_InstallableUnits81

    @aggregator_p2view_InstallableUnits81.setter
    def aggregator_p2view_InstallableUnits81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits81", None)
        self.__aggregator_p2view_InstallableUnits81 = value
        
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
    def aggregator_p2view_InstallableUnits(self):
        return self.__aggregator_p2view_InstallableUnits

    @aggregator_p2view_InstallableUnits.setter
    def aggregator_p2view_InstallableUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits", None)
        self.__aggregator_p2view_InstallableUnits = value
        
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
    def aggregator_p2view_InstallableUnits85(self):
        return self.__aggregator_p2view_InstallableUnits85

    @aggregator_p2view_InstallableUnits85.setter
    def aggregator_p2view_InstallableUnits85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits85", None)
        self.__aggregator_p2view_InstallableUnits85 = value
        
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

    @property
    def aggregator_p2view_InstallableUnits83(self):
        return self.__aggregator_p2view_InstallableUnits83

    @aggregator_p2view_InstallableUnits83.setter
    def aggregator_p2view_InstallableUnits83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits83", None)
        self.__aggregator_p2view_InstallableUnits83 = value
        
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

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def getNotNullMiscellaneousContainer(self) -> str:
        # TODO: Implement getNotNullMiscellaneousContainer method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

class Properties:

    pass
class InstallableUnits:

    pass
class aggregator_p2_IAdaptable(ABC):

    def __init__(self):
        
    def getAdapter(self, adapter: str) -> str:
        # TODO: Implement getAdapter method
        pass

class aggregator_p2_RepositoryReference:

    def __init__(self, location: str, type: int, options: int, nickname: str):
        self.location = location
        self.type = type
        self.options = options
        self.nickname = nickname
        
    @property
    def options(self) -> int:
        return self.__options

    @options.setter
    def options(self, options: int):
        self.__options = options

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

class IAdaptable:

    pass
class aggregator_p2_IRepository(IAdaptable):

    def __init__(self, location: str, name: str, type: str, version: str, description: str, provider: str, modifiable: bool):
        self.location = location
        self.name = name
        self.type = type
        self.version = version
        self.description = description
        self.provider = provider
        self.modifiable = modifiable
        
    @property
    def modifiable(self) -> bool:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: bool):
        self.__modifiable = modifiable

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    def getProperties(self) -> str:
        # TODO: Implement getProperties method
        pass

    def setProperty(self, value: str, key: str) -> str:
        # TODO: Implement setProperty method
        pass

class p2_IRepository:

    pass
class p2_IQueryable:

    pass
class aggregator_p2_IMetadataRepository(p2_IQueryable, p2_IRepository):

    def __init__(self):
        
    def addInstallableUnits(self, installableUnits: str):
        # TODO: Implement addInstallableUnits method
        pass

    def addReference(self, options: int, location: str, type: int, nickname: str):
        # TODO: Implement addReference method
        pass

    def removeAll(self):
        # TODO: Implement removeAll method
        pass

    def removeInstallableUnits(self, query: str, monitor: str) -> bool:
        # TODO: Implement removeInstallableUnits method
        pass

class ProvidedCapability:

    pass
class aggregator_p2_IQueryable(ABC):

    def __init__(self):
        
    def query(self, query: str, collector: str, progress: str) -> str:
        # TODO: Implement query method
        pass

class ArtifactKey:

    pass
class TouchpointInstruction:

    pass
class aggregator_p2_InstructionMap:

    def __init__(self, key: str, aggregator_p2_InstructionMap: "TouchpointInstruction" = None):
        self.key = key
        self.aggregator_p2_InstructionMap = aggregator_p2_InstructionMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def aggregator_p2_InstructionMap(self):
        return self.__aggregator_p2_InstructionMap

    @aggregator_p2_InstructionMap.setter
    def aggregator_p2_InstructionMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstructionMap__aggregator_p2_InstructionMap", None)
        self.__aggregator_p2_InstructionMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TouchpointInstruction"):
                opp_val = getattr(old_value, "TouchpointInstruction", None)
                if opp_val == self:
                    setattr(old_value, "TouchpointInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TouchpointInstruction"):
                opp_val = getattr(value, "TouchpointInstruction", None)
                setattr(value, "TouchpointInstruction", self)

class aggregator_p2_Property:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ITouchpointInstruction:

    pass
class aggregator_p2_TouchpointInstruction(ITouchpointInstruction):

    pass
class InstructionMap:

    pass
class ITouchpointData:

    pass
class aggregator_p2_TouchpointData(ITouchpointData):

    pass
class IRequiredCapability:

    pass
class aggregator_p2_RequiredCapability(IRequiredCapability):

    pass
class IProvidedCapability:

    pass
class aggregator_p2_ProvidedCapability(IProvidedCapability):

    pass
class p2_IInstallableUnitFragment:

    pass
class p2_InstallableUnit:

    pass
class aggregator_p2_InstallableUnitFragment(p2_InstallableUnit, p2_IInstallableUnitFragment):

    pass
class TouchpointData:

    pass
class RequiredCapability:

    pass
class Property:

    pass
class RepositoryReference:

    pass
class InstallableUnit:

    pass
class IMetadataRepository:

    pass
class aggregator_p2_MetadataRepository(IMetadataRepository):

    pass
class IArtifactKey:

    pass
class aggregator_p2_ArtifactKey(IArtifactKey):

    pass
class aggregator_p2_IUpdateDescriptor(ABC):

    def __init__(self, id: str, range: str, description: str, severity: int):
        self.id = id
        self.range = range
        self.description = description
        self.severity = severity
        
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
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    def isUpdateOf(self, iu: str) -> bool:
        # TODO: Implement isUpdateOf method
        pass

class aggregator_p2_ITouchpointType(ABC):

    def __init__(self, id: str, version: str):
        self.id = id
        self.version = version
        
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

class aggregator_p2_ITouchpointInstruction(ABC):

    def __init__(self, body: str, importAttribute: str):
        self.body = body
        self.importAttribute = importAttribute
        
    @property
    def importAttribute(self) -> str:
        return self.__importAttribute

    @importAttribute.setter
    def importAttribute(self, importAttribute: str):
        self.__importAttribute = importAttribute

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class aggregator_p2_ITouchpointData(ABC):

    def __init__(self):
        
    def getInstruction(self, instructionKey: str) -> str:
        # TODO: Implement getInstruction method
        pass

    def getInstructions(self) -> str:
        # TODO: Implement getInstructions method
        pass

class aggregator_p2_IRequiredCapability(ABC):

    def __init__(self, filter: str, name: str, greedy: bool, namespace: str, range: str, negation: bool, selectorList: str, multiple: bool, optional: bool):
        self.filter = filter
        self.name = name
        self.greedy = greedy
        self.namespace = namespace
        self.range = range
        self.negation = negation
        self.selectorList = selectorList
        self.multiple = multiple
        self.optional = optional
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def greedy(self) -> bool:
        return self.__greedy

    @greedy.setter
    def greedy(self, greedy: bool):
        self.__greedy = greedy

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def selectorList(self) -> str:
        return self.__selectorList

    @selectorList.setter
    def selectorList(self, selectorList: str):
        self.__selectorList = selectorList

    def satisfiedBy(self, capability: str) -> bool:
        # TODO: Implement satisfiedBy method
        pass

    def setSelectors(self, selectors: str):
        # TODO: Implement setSelectors method
        pass

    def getSelectors(self) -> str:
        # TODO: Implement getSelectors method
        pass

class aggregator_p2_IProvidedCapability(ABC):

    def __init__(self, name: str, namespace: str, version: str):
        self.name = name
        self.namespace = namespace
        self.version = version
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def satisfies(self, requirement: str) -> bool:
        # TODO: Implement satisfies method
        pass

class aggregator_p2_ILicense(ABC):

    def __init__(self, location: str, body: str, digest: str):
        self.location = location
        self.body = body
        self.digest = digest
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def digest(self) -> str:
        return self.__digest

    @digest.setter
    def digest(self, digest: str):
        self.__digest = digest

class IInstallableUnit:

    pass
class aggregator_p2_InstallableUnit(IInstallableUnit):

    def __init__(self, aggregator_p2_InstallableUnit56: set["RequiredCapability"] = None, aggregator_p2_InstallableUnit58: set["RequiredCapability"] = None, aggregator_p2_InstallableUnit61: set["Property"] = None, aggregator_p2_InstallableUnit64: set["TouchpointData"] = None, aggregator_p2_InstallableUnit: set["ArtifactKey"] = None, aggregator_p2_InstallableUnit54: set["ProvidedCapability"] = None):
        self.aggregator_p2_InstallableUnit56 = aggregator_p2_InstallableUnit56 if aggregator_p2_InstallableUnit56 is not None else set()
        self.aggregator_p2_InstallableUnit58 = aggregator_p2_InstallableUnit58 if aggregator_p2_InstallableUnit58 is not None else set()
        self.aggregator_p2_InstallableUnit61 = aggregator_p2_InstallableUnit61 if aggregator_p2_InstallableUnit61 is not None else set()
        self.aggregator_p2_InstallableUnit64 = aggregator_p2_InstallableUnit64 if aggregator_p2_InstallableUnit64 is not None else set()
        self.aggregator_p2_InstallableUnit = aggregator_p2_InstallableUnit if aggregator_p2_InstallableUnit is not None else set()
        self.aggregator_p2_InstallableUnit54 = aggregator_p2_InstallableUnit54 if aggregator_p2_InstallableUnit54 is not None else set()
        
    @property
    def aggregator_p2_InstallableUnit58(self):
        return self.__aggregator_p2_InstallableUnit58

    @aggregator_p2_InstallableUnit58.setter
    def aggregator_p2_InstallableUnit58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit58", None)
        self.__aggregator_p2_InstallableUnit58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredCapability59"):
                    opp_val = getattr(item, "RequiredCapability59", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredCapability59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredCapability59"):
                    opp_val = getattr(item, "RequiredCapability59", None)
                    
                    setattr(item, "RequiredCapability59", self)
                    

    @property
    def aggregator_p2_InstallableUnit56(self):
        return self.__aggregator_p2_InstallableUnit56

    @aggregator_p2_InstallableUnit56.setter
    def aggregator_p2_InstallableUnit56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit56", None)
        self.__aggregator_p2_InstallableUnit56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredCapability"):
                    opp_val = getattr(item, "RequiredCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredCapability"):
                    opp_val = getattr(item, "RequiredCapability", None)
                    
                    setattr(item, "RequiredCapability", self)
                    

    @property
    def aggregator_p2_InstallableUnit64(self):
        return self.__aggregator_p2_InstallableUnit64

    @aggregator_p2_InstallableUnit64.setter
    def aggregator_p2_InstallableUnit64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit64", None)
        self.__aggregator_p2_InstallableUnit64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TouchpointData"):
                    opp_val = getattr(item, "TouchpointData", None)
                    
                    if opp_val == self:
                        setattr(item, "TouchpointData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TouchpointData"):
                    opp_val = getattr(item, "TouchpointData", None)
                    
                    setattr(item, "TouchpointData", self)
                    

    @property
    def aggregator_p2_InstallableUnit61(self):
        return self.__aggregator_p2_InstallableUnit61

    @aggregator_p2_InstallableUnit61.setter
    def aggregator_p2_InstallableUnit61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit61", None)
        self.__aggregator_p2_InstallableUnit61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property62"):
                    opp_val = getattr(item, "Property62", None)
                    
                    if opp_val == self:
                        setattr(item, "Property62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property62"):
                    opp_val = getattr(item, "Property62", None)
                    
                    setattr(item, "Property62", self)
                    

    @property
    def aggregator_p2_InstallableUnit54(self):
        return self.__aggregator_p2_InstallableUnit54

    @aggregator_p2_InstallableUnit54.setter
    def aggregator_p2_InstallableUnit54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit54", None)
        self.__aggregator_p2_InstallableUnit54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedCapability"):
                    opp_val = getattr(item, "ProvidedCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedCapability"):
                    opp_val = getattr(item, "ProvidedCapability", None)
                    
                    setattr(item, "ProvidedCapability", self)
                    

    @property
    def aggregator_p2_InstallableUnit(self):
        return self.__aggregator_p2_InstallableUnit

    @aggregator_p2_InstallableUnit.setter
    def aggregator_p2_InstallableUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit", None)
        self.__aggregator_p2_InstallableUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArtifactKey"):
                    opp_val = getattr(item, "ArtifactKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ArtifactKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArtifactKey"):
                    opp_val = getattr(item, "ArtifactKey", None)
                    
                    setattr(item, "ArtifactKey", self)
                    

    def compareTo(self, other: str) -> int:
        # TODO: Implement compareTo method
        pass

class aggregator_p2_IInstallableUnitFragment(IInstallableUnit):

    def __init__(self):
        
    def getHost(self) -> str:
        # TODO: Implement getHost method
        pass

class ICopyright:

    pass
class aggregator_p2_Copyright(ICopyright):

    pass
class ILicense:

    pass
class aggregator_p2_License(ILicense):

    pass
class IUpdateDescriptor:

    pass
class aggregator_p2_UpdateDescriptor(IUpdateDescriptor):

    pass
class ITouchpointType:

    pass
class aggregator_p2_TouchpointType(ITouchpointType):

    pass
class aggregator_ChildrenProvider(ABC):

    pass
class aggregator_MavenItem:

    def __init__(self, groupId: str, artifactId: str):
        self.groupId = groupId
        self.artifactId = artifactId
        
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

class aggregator_p2_IInstallableUnit(ABC):

    def __init__(self, version: str, resolved: bool, singleton: bool, filter: str, id: str, aggregator_p2_IInstallableUnit: "ITouchpointType" = None, aggregator_p2_IInstallableUnit42: "IUpdateDescriptor" = None, aggregator_p2_IInstallableUnit44: "ILicense" = None, aggregator_p2_IInstallableUnit46: "ICopyright" = None):
        self.version = version
        self.resolved = resolved
        self.singleton = singleton
        self.filter = filter
        self.id = id
        self.aggregator_p2_IInstallableUnit = aggregator_p2_IInstallableUnit
        self.aggregator_p2_IInstallableUnit42 = aggregator_p2_IInstallableUnit42
        self.aggregator_p2_IInstallableUnit44 = aggregator_p2_IInstallableUnit44
        self.aggregator_p2_IInstallableUnit46 = aggregator_p2_IInstallableUnit46
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def resolved(self) -> bool:
        return self.__resolved

    @resolved.setter
    def resolved(self, resolved: bool):
        self.__resolved = resolved

    @property
    def singleton(self) -> bool:
        return self.__singleton

    @singleton.setter
    def singleton(self, singleton: bool):
        self.__singleton = singleton

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aggregator_p2_IInstallableUnit(self):
        return self.__aggregator_p2_IInstallableUnit

    @aggregator_p2_IInstallableUnit.setter
    def aggregator_p2_IInstallableUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit", None)
        self.__aggregator_p2_IInstallableUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ITouchpointType"):
                opp_val = getattr(old_value, "ITouchpointType", None)
                if opp_val == self:
                    setattr(old_value, "ITouchpointType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ITouchpointType"):
                opp_val = getattr(value, "ITouchpointType", None)
                setattr(value, "ITouchpointType", self)

    @property
    def aggregator_p2_IInstallableUnit46(self):
        return self.__aggregator_p2_IInstallableUnit46

    @aggregator_p2_IInstallableUnit46.setter
    def aggregator_p2_IInstallableUnit46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit46", None)
        self.__aggregator_p2_IInstallableUnit46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ICopyright"):
                opp_val = getattr(old_value, "ICopyright", None)
                if opp_val == self:
                    setattr(old_value, "ICopyright", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ICopyright"):
                opp_val = getattr(value, "ICopyright", None)
                setattr(value, "ICopyright", self)

    @property
    def aggregator_p2_IInstallableUnit42(self):
        return self.__aggregator_p2_IInstallableUnit42

    @aggregator_p2_IInstallableUnit42.setter
    def aggregator_p2_IInstallableUnit42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit42", None)
        self.__aggregator_p2_IInstallableUnit42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IUpdateDescriptor"):
                opp_val = getattr(old_value, "IUpdateDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "IUpdateDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IUpdateDescriptor"):
                opp_val = getattr(value, "IUpdateDescriptor", None)
                setattr(value, "IUpdateDescriptor", self)

    @property
    def aggregator_p2_IInstallableUnit44(self):
        return self.__aggregator_p2_IInstallableUnit44

    @aggregator_p2_IInstallableUnit44.setter
    def aggregator_p2_IInstallableUnit44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit44", None)
        self.__aggregator_p2_IInstallableUnit44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ILicense"):
                opp_val = getattr(old_value, "ILicense", None)
                if opp_val == self:
                    setattr(old_value, "ILicense", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ILicense"):
                opp_val = getattr(value, "ILicense", None)
                setattr(value, "ILicense", self)

    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

    def satisfies(self, candidate: str) -> bool:
        # TODO: Implement satisfies method
        pass

    def getArtifacts(self) -> str:
        # TODO: Implement getArtifacts method
        pass

    def getProperties(self) -> str:
        # TODO: Implement getProperties method
        pass

    def getTouchpointData(self) -> str:
        # TODO: Implement getTouchpointData method
        pass

    def unresolved(self) -> str:
        # TODO: Implement unresolved method
        pass

    def isFragment(self) -> bool:
        # TODO: Implement isFragment method
        pass

    def getRequiredCapabilities(self) -> str:
        # TODO: Implement getRequiredCapabilities method
        pass

    def getMetaRequiredCapabilities(self) -> str:
        # TODO: Implement getMetaRequiredCapabilities method
        pass

    def getFragments(self) -> str:
        # TODO: Implement getFragments method
        pass

    def getProvidedCapabilities(self) -> str:
        # TODO: Implement getProvidedCapabilities method
        pass

class aggregator_p2_ICopyright(ABC):

    def __init__(self, location: str, body: str):
        self.location = location
        self.body = body
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class aggregator_p2_IArtifactKey(ABC):

    def __init__(self, classifier: str, id: str, version: str):
        self.classifier = classifier
        self.id = id
        self.version = version
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    def toExternalForm(self) -> str:
        # TODO: Implement toExternalForm method
        pass

class aggregator_InfosProvider:

    def __init__(self, errors: str, warnings: str, infos: str):
        self.errors = errors
        self.warnings = warnings
        self.infos = infos
        
    @property
    def infos(self) -> str:
        return self.__infos

    @infos.setter
    def infos(self, infos: str):
        self.__infos = infos

    @property
    def errors(self) -> str:
        return self.__errors

    @errors.setter
    def errors(self, errors: str):
        self.__errors = errors

    @property
    def warnings(self) -> str:
        return self.__warnings

    @warnings.setter
    def warnings(self, warnings: str):
        self.__warnings = warnings

class aggregator_StatusProvider(ABC):

    pass
class aggregator_Status:

    def __init__(self, code: str, message: str, aggregator_Status: "aggregator_StatusProvider" = None):
        self.code = code
        self.message = message
        self.aggregator_Status = aggregator_Status
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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

class MapRule:

    pass
class aggregator_ValidConfigurationsRule(MapRule):

    pass
class aggregator_ExclusionRule(MapRule):

    pass
class aggregator_EnabledStatusProvider(ABC):

    def __init__(self, enabled: bool):
        self.enabled = enabled
        
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

class aggregator_LabelProvider(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class aggregator_Comparable(ABC):

    pass
class MetadataRepository:

    pass
class EnabledStatusProvider:

    pass
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

class InstallableUnitRequest:

    pass
class aggregator_MappedUnit(InstallableUnitRequest, EnabledStatusProvider):

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
                if hasattr(item, "aggregator_Configuration33"):
                    opp_val = getattr(item, "aggregator_Configuration33", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Configuration33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Configuration33"):
                    opp_val = getattr(item, "aggregator_Configuration33", None)
                    
                    setattr(item, "aggregator_Configuration33", self)
                    

    def getRequiredCapability(self) -> str:
        # TODO: Implement getRequiredCapability method
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
            if hasattr(old_value, "aggregator_MappedRepository18"):
                opp_val = getattr(old_value, "aggregator_MappedRepository18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_MappedRepository18"):
                opp_val = getattr(value, "aggregator_MappedRepository18", None)
                if opp_val is None:
                    setattr(value, "aggregator_MappedRepository18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aggregator_Feature(MappedUnit):

    pass
class aggregator_Bundle(MappedUnit):

    pass
class aggregator_Product(MappedUnit):

    pass
class MetadataRepositoryReference:

    pass
class aggregator_Contact:

    def __init__(self, name: str, email: str, aggregator_Contact: "aggregator_Aggregator" = None, Contact: "aggregator_Aggregator" = None, aggregator_Contact26: "aggregator_Contribution" = None, contacts: "aggregator_Aggregator" = None):
        self.name = name
        self.email = email
        self.aggregator_Contact = aggregator_Contact
        self.Contact = Contact
        self.aggregator_Contact26 = aggregator_Contact26
        self.contacts = contacts
        
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
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__contacts", None)
        self.__contacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Aggregator"):
                opp_val = getattr(old_value, "Aggregator", None)
                if opp_val == self:
                    setattr(old_value, "Aggregator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Aggregator"):
                opp_val = getattr(value, "Aggregator", None)
                setattr(value, "Aggregator", self)

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
            if hasattr(old_value, "aggregator_Aggregator4"):
                opp_val = getattr(old_value, "aggregator_Aggregator4", None)
                if opp_val == self:
                    setattr(old_value, "aggregator_Aggregator4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator4"):
                opp_val = getattr(value, "aggregator_Aggregator4", None)
                setattr(value, "aggregator_Aggregator4", self)

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
            if hasattr(old_value, "aggregator"):
                opp_val = getattr(old_value, "aggregator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator"):
                opp_val = getattr(value, "aggregator", None)
                if opp_val is None:
                    setattr(value, "aggregator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Contact26(self):
        return self.__aggregator_Contact26

    @aggregator_Contact26.setter
    def aggregator_Contact26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contact__aggregator_Contact26", None)
        self.__aggregator_Contact26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution25"):
                opp_val = getattr(old_value, "aggregator_Contribution25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution25"):
                opp_val = getattr(value, "aggregator_Contribution25", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aggregator_Configuration(EnabledStatusProvider):

    def __init__(self, operatingSystem: str, windowSystem: str, architecture: str, aggregator_Configuration: "aggregator_Aggregator" = None, aggregator_Configuration33: "aggregator_MappedUnit" = None, aggregator_Configuration36: "aggregator_ValidConfigurationsRule" = None):
        self.operatingSystem = operatingSystem
        self.windowSystem = windowSystem
        self.architecture = architecture
        self.aggregator_Configuration = aggregator_Configuration
        self.aggregator_Configuration33 = aggregator_Configuration33
        self.aggregator_Configuration36 = aggregator_Configuration36
        
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
    def aggregator_Configuration36(self):
        return self.__aggregator_Configuration36

    @aggregator_Configuration36.setter
    def aggregator_Configuration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration36", None)
        self.__aggregator_Configuration36 = value
        
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

    @property
    def aggregator_Configuration33(self):
        return self.__aggregator_Configuration33

    @aggregator_Configuration33.setter
    def aggregator_Configuration33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration33", None)
        self.__aggregator_Configuration33 = value
        
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
    def aggregator_Configuration(self):
        return self.__aggregator_Configuration

    @aggregator_Configuration.setter
    def aggregator_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration", None)
        self.__aggregator_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregator"):
                opp_val = getattr(old_value, "aggregator_Aggregator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator"):
                opp_val = getattr(value, "aggregator_Aggregator", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregator", set([self]))
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
class aggregator_CustomCategory(StatusProvider, InfosProvider):

    def __init__(self, identifier: str, label: str, description: str, aggregator_CustomCategory: "aggregator_Aggregator" = None, CustomCategory: "aggregator_Feature" = None, categories: set["aggregator_Feature"] = None):
        self.identifier = identifier
        self.label = label
        self.description = description
        self.aggregator_CustomCategory = aggregator_CustomCategory
        self.CustomCategory = CustomCategory
        self.categories = categories if categories is not None else set()
        
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
            if hasattr(old_value, "aggregator_Aggregator7"):
                opp_val = getattr(old_value, "aggregator_Aggregator7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator7"):
                opp_val = getattr(value, "aggregator_Aggregator7", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregator7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aggregator_MavenMapping(StatusProvider, InfosProvider):

    def __init__(self, namePattern: str, groupId: str, artifactId: str, aggregator_MavenMapping: "aggregator_Aggregator" = None, aggregator_MavenMapping29: "aggregator_Contribution" = None):
        self.namePattern = namePattern
        self.groupId = groupId
        self.artifactId = artifactId
        self.aggregator_MavenMapping = aggregator_MavenMapping
        self.aggregator_MavenMapping29 = aggregator_MavenMapping29
        
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
    def aggregator_MavenMapping29(self):
        return self.__aggregator_MavenMapping29

    @aggregator_MavenMapping29.setter
    def aggregator_MavenMapping29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MavenMapping__aggregator_MavenMapping29", None)
        self.__aggregator_MavenMapping29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution28"):
                opp_val = getattr(old_value, "aggregator_Contribution28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution28"):
                opp_val = getattr(value, "aggregator_Contribution28", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "aggregator_Aggregator11"):
                opp_val = getattr(old_value, "aggregator_Aggregator11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator11"):
                opp_val = getattr(value, "aggregator_Aggregator11", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregator11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def map(self, installableUnitID: str) -> str:
        # TODO: Implement map method
        pass

class aggregator_MetadataRepositoryReference(EnabledStatusProvider, StatusProvider, InfosProvider):

    def __init__(self, location: str, nature: str, aggregator_MetadataRepositoryReference: "aggregator_Aggregator" = None, aggregator_MetadataRepositoryReference38: "MetadataRepository" = None):
        self.location = location
        self.nature = nature
        self.aggregator_MetadataRepositoryReference = aggregator_MetadataRepositoryReference
        self.aggregator_MetadataRepositoryReference38 = aggregator_MetadataRepositoryReference38
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

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
            if hasattr(old_value, "aggregator_Aggregator9"):
                opp_val = getattr(old_value, "aggregator_Aggregator9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator9"):
                opp_val = getattr(value, "aggregator_Aggregator9", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregator9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_MetadataRepositoryReference38(self):
        return self.__aggregator_MetadataRepositoryReference38

    @aggregator_MetadataRepositoryReference38.setter
    def aggregator_MetadataRepositoryReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MetadataRepositoryReference__aggregator_MetadataRepositoryReference38", None)
        self.__aggregator_MetadataRepositoryReference38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetadataRepository"):
                opp_val = getattr(old_value, "MetadataRepository", None)
                if opp_val == self:
                    setattr(old_value, "MetadataRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetadataRepository"):
                opp_val = getattr(value, "MetadataRepository", None)
                setattr(value, "MetadataRepository", self)

    def cancelRepositoryLoad(self):
        # TODO: Implement cancelRepositoryLoad method
        pass

    def getAggregator(self) -> str:
        # TODO: Implement getAggregator method
        pass

    def getResolvedLocation(self) -> str:
        # TODO: Implement getResolvedLocation method
        pass

    def onRepositoryLoad(self):
        # TODO: Implement onRepositoryLoad method
        pass

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def startRepositoryLoad(self, forceReload: bool):
        # TODO: Implement startRepositoryLoad method
        pass

class DescriptionProvider:

    pass
class aggregator_MapRule(DescriptionProvider, InstallableUnitRequest):

    pass
class aggregator_MappedRepository(MetadataRepositoryReference, DescriptionProvider):

    def __init__(self, mirrorArtifacts: bool, categoryPrefix: str, aggregator_MappedRepository: set["aggregator_Product"] = None, aggregator_MappedRepository14: set["aggregator_Bundle"] = None, aggregator_MappedRepository16: set["aggregator_Feature"] = None, aggregator_MappedRepository18: set["aggregator_Category"] = None, aggregator_MappedRepository20: set["aggregator_MapRule"] = None, aggregator_MappedRepository23: "aggregator_Contribution" = None):
        self.mirrorArtifacts = mirrorArtifacts
        self.categoryPrefix = categoryPrefix
        self.aggregator_MappedRepository = aggregator_MappedRepository if aggregator_MappedRepository is not None else set()
        self.aggregator_MappedRepository14 = aggregator_MappedRepository14 if aggregator_MappedRepository14 is not None else set()
        self.aggregator_MappedRepository16 = aggregator_MappedRepository16 if aggregator_MappedRepository16 is not None else set()
        self.aggregator_MappedRepository18 = aggregator_MappedRepository18 if aggregator_MappedRepository18 is not None else set()
        self.aggregator_MappedRepository20 = aggregator_MappedRepository20 if aggregator_MappedRepository20 is not None else set()
        self.aggregator_MappedRepository23 = aggregator_MappedRepository23
        
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
    def aggregator_MappedRepository14(self):
        return self.__aggregator_MappedRepository14

    @aggregator_MappedRepository14.setter
    def aggregator_MappedRepository14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository14", None)
        self.__aggregator_MappedRepository14 = value if value is not None else set()
        
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
    def aggregator_MappedRepository20(self):
        return self.__aggregator_MappedRepository20

    @aggregator_MappedRepository20.setter
    def aggregator_MappedRepository20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository20", None)
        self.__aggregator_MappedRepository20 = value if value is not None else set()
        
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
                    

    @property
    def aggregator_MappedRepository(self):
        return self.__aggregator_MappedRepository

    @aggregator_MappedRepository.setter
    def aggregator_MappedRepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository", None)
        self.__aggregator_MappedRepository = value if value is not None else set()
        
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
    def aggregator_MappedRepository18(self):
        return self.__aggregator_MappedRepository18

    @aggregator_MappedRepository18.setter
    def aggregator_MappedRepository18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository18", None)
        self.__aggregator_MappedRepository18 = value if value is not None else set()
        
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
    def aggregator_MappedRepository16(self):
        return self.__aggregator_MappedRepository16

    @aggregator_MappedRepository16.setter
    def aggregator_MappedRepository16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository16", None)
        self.__aggregator_MappedRepository16 = value if value is not None else set()
        
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
    def aggregator_MappedRepository23(self):
        return self.__aggregator_MappedRepository23

    @aggregator_MappedRepository23.setter
    def aggregator_MappedRepository23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MappedRepository__aggregator_MappedRepository23", None)
        self.__aggregator_MappedRepository23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Contribution22"):
                opp_val = getattr(old_value, "aggregator_Contribution22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Contribution22"):
                opp_val = getattr(value, "aggregator_Contribution22", None)
                if opp_val is None:
                    setattr(value, "aggregator_Contribution22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getUnits(self, enabledOnly: bool) -> str:
        # TODO: Implement getUnits method
        pass

    def isMapExclusive(self) -> bool:
        # TODO: Implement isMapExclusive method
        pass

class aggregator_Contribution(DescriptionProvider, EnabledStatusProvider, StatusProvider, InfosProvider):

    def __init__(self, label: str, aggregator_Contribution: "aggregator_Aggregator" = None, aggregator_Contribution25: set["aggregator_Contact"] = None, aggregator_Contribution28: set["aggregator_MavenMapping"] = None, aggregator_Contribution22: set["aggregator_MappedRepository"] = None):
        self.label = label
        self.aggregator_Contribution = aggregator_Contribution
        self.aggregator_Contribution25 = aggregator_Contribution25 if aggregator_Contribution25 is not None else set()
        self.aggregator_Contribution28 = aggregator_Contribution28 if aggregator_Contribution28 is not None else set()
        self.aggregator_Contribution22 = aggregator_Contribution22 if aggregator_Contribution22 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def aggregator_Contribution28(self):
        return self.__aggregator_Contribution28

    @aggregator_Contribution28.setter
    def aggregator_Contribution28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution28", None)
        self.__aggregator_Contribution28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MavenMapping29"):
                    opp_val = getattr(item, "aggregator_MavenMapping29", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MavenMapping29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MavenMapping29"):
                    opp_val = getattr(item, "aggregator_MavenMapping29", None)
                    
                    setattr(item, "aggregator_MavenMapping29", self)
                    

    @property
    def aggregator_Contribution(self):
        return self.__aggregator_Contribution

    @aggregator_Contribution.setter
    def aggregator_Contribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution", None)
        self.__aggregator_Contribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregator_Aggregator2"):
                opp_val = getattr(old_value, "aggregator_Aggregator2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregator_Aggregator2"):
                opp_val = getattr(value, "aggregator_Aggregator2", None)
                if opp_val is None:
                    setattr(value, "aggregator_Aggregator2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregator_Contribution25(self):
        return self.__aggregator_Contribution25

    @aggregator_Contribution25.setter
    def aggregator_Contribution25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution25", None)
        self.__aggregator_Contribution25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Contact26"):
                    opp_val = getattr(item, "aggregator_Contact26", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Contact26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Contact26"):
                    opp_val = getattr(item, "aggregator_Contact26", None)
                    
                    setattr(item, "aggregator_Contact26", self)
                    

    @property
    def aggregator_Contribution22(self):
        return self.__aggregator_Contribution22

    @aggregator_Contribution22.setter
    def aggregator_Contribution22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Contribution__aggregator_Contribution22", None)
        self.__aggregator_Contribution22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MappedRepository23"):
                    opp_val = getattr(item, "aggregator_MappedRepository23", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MappedRepository23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MappedRepository23"):
                    opp_val = getattr(item, "aggregator_MappedRepository23", None)
                    
                    setattr(item, "aggregator_MappedRepository23", self)
                    

    def getRepositories(self, enabledOnly: bool) -> str:
        # TODO: Implement getRepositories method
        pass

    def getAllMavenMappings(self) -> str:
        # TODO: Implement getAllMavenMappings method
        pass

class aggregator_InstallableUnitRequest(DescriptionProvider, StatusProvider, InfosProvider):

    def __init__(self, name: str, versionRange: str):
        self.name = name
        self.versionRange = versionRange
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

    def isMappedRepositoryBroken(self) -> bool:
        # TODO: Implement isMappedRepositoryBroken method
        pass

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def resolveAsSingleton(self) -> str:
        # TODO: Implement resolveAsSingleton method
        pass

class aggregator_Aggregator(DescriptionProvider, StatusProvider, InfosProvider):

    def __init__(self, label: str, buildRoot: str, packedStrategy: str, sendmail: bool, type: str, mavenResult: bool, aggregator_Aggregator: set["aggregator_Configuration"] = None, aggregator_Aggregator2: set["aggregator_Contribution"] = None, aggregator_Aggregator4: "aggregator_Contact" = None, aggregator_Aggregator11: set["aggregator_MavenMapping"] = None, aggregator: set["aggregator_Contact"] = None, aggregator_Aggregator7: set["aggregator_CustomCategory"] = None, aggregator_Aggregator9: set["aggregator_MetadataRepositoryReference"] = None, Aggregator: "aggregator_Contact" = None):
        self.label = label
        self.buildRoot = buildRoot
        self.packedStrategy = packedStrategy
        self.sendmail = sendmail
        self.type = type
        self.mavenResult = mavenResult
        self.aggregator_Aggregator = aggregator_Aggregator if aggregator_Aggregator is not None else set()
        self.aggregator_Aggregator2 = aggregator_Aggregator2 if aggregator_Aggregator2 is not None else set()
        self.aggregator_Aggregator4 = aggregator_Aggregator4
        self.aggregator_Aggregator11 = aggregator_Aggregator11 if aggregator_Aggregator11 is not None else set()
        self.aggregator = aggregator if aggregator is not None else set()
        self.aggregator_Aggregator7 = aggregator_Aggregator7 if aggregator_Aggregator7 is not None else set()
        self.aggregator_Aggregator9 = aggregator_Aggregator9 if aggregator_Aggregator9 is not None else set()
        self.Aggregator = Aggregator
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def packedStrategy(self) -> str:
        return self.__packedStrategy

    @packedStrategy.setter
    def packedStrategy(self, packedStrategy: str):
        self.__packedStrategy = packedStrategy

    @property
    def mavenResult(self) -> bool:
        return self.__mavenResult

    @mavenResult.setter
    def mavenResult(self, mavenResult: bool):
        self.__mavenResult = mavenResult

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sendmail(self) -> bool:
        return self.__sendmail

    @sendmail.setter
    def sendmail(self, sendmail: bool):
        self.__sendmail = sendmail

    @property
    def buildRoot(self) -> str:
        return self.__buildRoot

    @buildRoot.setter
    def buildRoot(self, buildRoot: str):
        self.__buildRoot = buildRoot

    @property
    def aggregator(self):
        return self.__aggregator

    @aggregator.setter
    def aggregator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator", None)
        self.__aggregator = value if value is not None else set()
        
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
    def Aggregator(self):
        return self.__Aggregator

    @Aggregator.setter
    def Aggregator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__Aggregator", None)
        self.__Aggregator = value
        
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
    def aggregator_Aggregator11(self):
        return self.__aggregator_Aggregator11

    @aggregator_Aggregator11.setter
    def aggregator_Aggregator11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator11", None)
        self.__aggregator_Aggregator11 = value if value is not None else set()
        
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
    def aggregator_Aggregator4(self):
        return self.__aggregator_Aggregator4

    @aggregator_Aggregator4.setter
    def aggregator_Aggregator4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator4", None)
        self.__aggregator_Aggregator4 = value
        
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
    def aggregator_Aggregator(self):
        return self.__aggregator_Aggregator

    @aggregator_Aggregator.setter
    def aggregator_Aggregator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator", None)
        self.__aggregator_Aggregator = value if value is not None else set()
        
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
    def aggregator_Aggregator7(self):
        return self.__aggregator_Aggregator7

    @aggregator_Aggregator7.setter
    def aggregator_Aggregator7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator7", None)
        self.__aggregator_Aggregator7 = value if value is not None else set()
        
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
    def aggregator_Aggregator2(self):
        return self.__aggregator_Aggregator2

    @aggregator_Aggregator2.setter
    def aggregator_Aggregator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator2", None)
        self.__aggregator_Aggregator2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_Contribution"):
                    opp_val = getattr(item, "aggregator_Contribution", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_Contribution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_Contribution"):
                    opp_val = getattr(item, "aggregator_Contribution", None)
                    
                    setattr(item, "aggregator_Contribution", self)
                    

    @property
    def aggregator_Aggregator9(self):
        return self.__aggregator_Aggregator9

    @aggregator_Aggregator9.setter
    def aggregator_Aggregator9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Aggregator__aggregator_Aggregator9", None)
        self.__aggregator_Aggregator9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aggregator_MetadataRepositoryReference"):
                    opp_val = getattr(item, "aggregator_MetadataRepositoryReference", None)
                    
                    if opp_val == self:
                        setattr(item, "aggregator_MetadataRepositoryReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aggregator_MetadataRepositoryReference"):
                    opp_val = getattr(item, "aggregator_MetadataRepositoryReference", None)
                    
                    setattr(item, "aggregator_MetadataRepositoryReference", self)
                    

    def getContributions(self, enabledOnly: bool) -> str:
        # TODO: Implement getContributions method
        pass

    def getValidationRepositories(self, enabledOnly: bool) -> str:
        # TODO: Implement getValidationRepositories method
        pass

    def getAllMetadataRepositoryReferences(self, enabledOnly: bool) -> str:
        # TODO: Implement getAllMetadataRepositoryReferences method
        pass
