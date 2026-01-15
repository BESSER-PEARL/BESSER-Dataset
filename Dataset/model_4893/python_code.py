from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatingSystem(Enum):
    Win32 = "Win32"
    Linux = "Linux"
    MacOSX = "MacOSX"
class PackedStrategy(Enum):
    Copy = "Copy"
    Verify = "Verify"
    UnpackAsSibling = "UnpackAsSibling"
    Unpack = "Unpack"
    Skip = "Skip"
class Architecture(Enum):
    X86 = "X86"
    PPC = "PPC"
    X86_64 = "X86_64"
class AggregationType(Enum):
    Stable = "Stable"
    Integration = "Integration"
    Nightly = "Nightly"
    Maintenance = "Maintenance"
    Continuous = "Continuous"
    Release = "Release"
class StatusCode(Enum):
    OK = "OK"
    BROKEN = "BROKEN"
    WAITING = "WAITING"
class WindowSystem(Enum):
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


############################################
# Definition of Classes
############################################

class p2_IProvidedCapability:

    pass
class LabelProvider:

    pass
class aggregator_p2view_ProvidedCapabilityWrapper(p2_IProvidedCapability, LabelProvider):

    pass
class p2_IRequiredCapability:

    pass
class aggregator_p2view_RequiredCapabilityWrapper(p2_IRequiredCapability, LabelProvider):

    pass
class Touchpoints:

    pass
class ProvidedCapabilities:

    pass
class RequiredCapabilities:

    pass
class aggregator_p2view_IUDetails:

    pass
class aggregator_p2view_Touchpoints:

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
class IUPresentationWithDetails:

    pass
class aggregator_p2view_Bundle(IUPresentationWithDetails):

    pass
class aggregator_p2view_Product(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Product: "Features" = None, aggregator_p2view_Product124: "Bundles" = None, aggregator_p2view_Product127: "Fragments" = None):
        self.aggregator_p2view_Product = aggregator_p2view_Product
        self.aggregator_p2view_Product124 = aggregator_p2view_Product124
        self.aggregator_p2view_Product127 = aggregator_p2view_Product127
        
    @property
    def aggregator_p2view_Product127(self):
        return self.__aggregator_p2view_Product127

    @aggregator_p2view_Product127.setter
    def aggregator_p2view_Product127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product127", None)
        self.__aggregator_p2view_Product127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments128"):
                opp_val = getattr(old_value, "Fragments128", None)
                if opp_val == self:
                    setattr(old_value, "Fragments128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments128"):
                opp_val = getattr(value, "Fragments128", None)
                setattr(value, "Fragments128", self)

    @property
    def aggregator_p2view_Product124(self):
        return self.__aggregator_p2view_Product124

    @aggregator_p2view_Product124.setter
    def aggregator_p2view_Product124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Product__aggregator_p2view_Product124", None)
        self.__aggregator_p2view_Product124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles125"):
                opp_val = getattr(old_value, "Bundles125", None)
                if opp_val == self:
                    setattr(old_value, "Bundles125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles125"):
                opp_val = getattr(value, "Bundles125", None)
                setattr(value, "Bundles125", self)

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
            if hasattr(old_value, "Features122"):
                opp_val = getattr(old_value, "Features122", None)
                if opp_val == self:
                    setattr(old_value, "Features122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features122"):
                opp_val = getattr(value, "Features122", None)
                setattr(value, "Features122", self)

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

class aggregator_p2view_OtherIU(IUPresentationWithDetails):

    pass
class aggregator_p2view_Feature(IUPresentationWithDetails):

    def __init__(self, aggregator_p2view_Feature: "Features" = None, aggregator_p2view_Feature116: "Bundles" = None, aggregator_p2view_Feature119: "Fragments" = None):
        self.aggregator_p2view_Feature = aggregator_p2view_Feature
        self.aggregator_p2view_Feature116 = aggregator_p2view_Feature116
        self.aggregator_p2view_Feature119 = aggregator_p2view_Feature119
        
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
            if hasattr(old_value, "Features114"):
                opp_val = getattr(old_value, "Features114", None)
                if opp_val == self:
                    setattr(old_value, "Features114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features114"):
                opp_val = getattr(value, "Features114", None)
                setattr(value, "Features114", self)

    @property
    def aggregator_p2view_Feature119(self):
        return self.__aggregator_p2view_Feature119

    @aggregator_p2view_Feature119.setter
    def aggregator_p2view_Feature119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature119", None)
        self.__aggregator_p2view_Feature119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments120"):
                opp_val = getattr(old_value, "Fragments120", None)
                if opp_val == self:
                    setattr(old_value, "Fragments120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments120"):
                opp_val = getattr(value, "Fragments120", None)
                setattr(value, "Fragments120", self)

    @property
    def aggregator_p2view_Feature116(self):
        return self.__aggregator_p2view_Feature116

    @aggregator_p2view_Feature116.setter
    def aggregator_p2view_Feature116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Feature__aggregator_p2view_Feature116", None)
        self.__aggregator_p2view_Feature116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles117"):
                opp_val = getattr(old_value, "Bundles117", None)
                if opp_val == self:
                    setattr(old_value, "Bundles117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles117"):
                opp_val = getattr(value, "Bundles117", None)
                setattr(value, "Bundles117", self)

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

class IUDetails:

    pass
class IUPresentation:

    pass
class aggregator_p2view_Category(IUPresentation):

    def __init__(self, aggregator_p2view_Category: "Categories" = None, aggregator_p2view_Category100: "Features" = None, aggregator_p2view_Category103: "Products" = None, aggregator_p2view_Category106: "Bundles" = None, aggregator_p2view_Category109: "Fragments" = None, aggregator_p2view_Category112: "IUDetails" = None):
        self.aggregator_p2view_Category = aggregator_p2view_Category
        self.aggregator_p2view_Category100 = aggregator_p2view_Category100
        self.aggregator_p2view_Category103 = aggregator_p2view_Category103
        self.aggregator_p2view_Category106 = aggregator_p2view_Category106
        self.aggregator_p2view_Category109 = aggregator_p2view_Category109
        self.aggregator_p2view_Category112 = aggregator_p2view_Category112
        
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
            if hasattr(old_value, "Categories98"):
                opp_val = getattr(old_value, "Categories98", None)
                if opp_val == self:
                    setattr(old_value, "Categories98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Categories98"):
                opp_val = getattr(value, "Categories98", None)
                setattr(value, "Categories98", self)

    @property
    def aggregator_p2view_Category106(self):
        return self.__aggregator_p2view_Category106

    @aggregator_p2view_Category106.setter
    def aggregator_p2view_Category106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category106", None)
        self.__aggregator_p2view_Category106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundles107"):
                opp_val = getattr(old_value, "Bundles107", None)
                if opp_val == self:
                    setattr(old_value, "Bundles107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundles107"):
                opp_val = getattr(value, "Bundles107", None)
                setattr(value, "Bundles107", self)

    @property
    def aggregator_p2view_Category103(self):
        return self.__aggregator_p2view_Category103

    @aggregator_p2view_Category103.setter
    def aggregator_p2view_Category103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category103", None)
        self.__aggregator_p2view_Category103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Products104"):
                opp_val = getattr(old_value, "Products104", None)
                if opp_val == self:
                    setattr(old_value, "Products104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products104"):
                opp_val = getattr(value, "Products104", None)
                setattr(value, "Products104", self)

    @property
    def aggregator_p2view_Category109(self):
        return self.__aggregator_p2view_Category109

    @aggregator_p2view_Category109.setter
    def aggregator_p2view_Category109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category109", None)
        self.__aggregator_p2view_Category109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragments110"):
                opp_val = getattr(old_value, "Fragments110", None)
                if opp_val == self:
                    setattr(old_value, "Fragments110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragments110"):
                opp_val = getattr(value, "Fragments110", None)
                setattr(value, "Fragments110", self)

    @property
    def aggregator_p2view_Category100(self):
        return self.__aggregator_p2view_Category100

    @aggregator_p2view_Category100.setter
    def aggregator_p2view_Category100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category100", None)
        self.__aggregator_p2view_Category100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Features101"):
                opp_val = getattr(old_value, "Features101", None)
                if opp_val == self:
                    setattr(old_value, "Features101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Features101"):
                opp_val = getattr(value, "Features101", None)
                setattr(value, "Features101", self)

    @property
    def aggregator_p2view_Category112(self):
        return self.__aggregator_p2view_Category112

    @aggregator_p2view_Category112.setter
    def aggregator_p2view_Category112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_Category__aggregator_p2view_Category112", None)
        self.__aggregator_p2view_Category112 = value
        
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

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def isNested(self) -> bool:
        # TODO: Implement isNested method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

class p2view_IUDetails:

    pass
class p2view_IUPresentation:

    pass
class aggregator_p2view_IUPresentationWithDetails(p2view_IUPresentation, p2view_IUDetails):

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
            if hasattr(old_value, "InstallableUnit96"):
                opp_val = getattr(old_value, "InstallableUnit96", None)
                if opp_val == self:
                    setattr(old_value, "InstallableUnit96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InstallableUnit96"):
                opp_val = getattr(value, "InstallableUnit96", None)
                setattr(value, "InstallableUnit96", self)

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
class aggregator_p2view_Bundles:

    pass
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

    def __init__(self, aggregator_p2view_InstallableUnits85: "Fragments" = None, aggregator_p2view_InstallableUnits87: "Miscellaneous" = None, aggregator_p2view_InstallableUnits: "Categories" = None, aggregator_p2view_InstallableUnits79: "Features" = None, aggregator_p2view_InstallableUnits81: "Products" = None, aggregator_p2view_InstallableUnits83: "Bundles" = None):
        self.aggregator_p2view_InstallableUnits85 = aggregator_p2view_InstallableUnits85
        self.aggregator_p2view_InstallableUnits87 = aggregator_p2view_InstallableUnits87
        self.aggregator_p2view_InstallableUnits = aggregator_p2view_InstallableUnits
        self.aggregator_p2view_InstallableUnits79 = aggregator_p2view_InstallableUnits79
        self.aggregator_p2view_InstallableUnits81 = aggregator_p2view_InstallableUnits81
        self.aggregator_p2view_InstallableUnits83 = aggregator_p2view_InstallableUnits83
        
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
    def aggregator_p2view_InstallableUnits81(self):
        return self.__aggregator_p2view_InstallableUnits81

    @aggregator_p2view_InstallableUnits81.setter
    def aggregator_p2view_InstallableUnits81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits81", None)
        self.__aggregator_p2view_InstallableUnits81 = value
        
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
    def aggregator_p2view_InstallableUnits85(self):
        return self.__aggregator_p2view_InstallableUnits85

    @aggregator_p2view_InstallableUnits85.setter
    def aggregator_p2view_InstallableUnits85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits85", None)
        self.__aggregator_p2view_InstallableUnits85 = value
        
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
    def aggregator_p2view_InstallableUnits79(self):
        return self.__aggregator_p2view_InstallableUnits79

    @aggregator_p2view_InstallableUnits79.setter
    def aggregator_p2view_InstallableUnits79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits79", None)
        self.__aggregator_p2view_InstallableUnits79 = value
        
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
    def aggregator_p2view_InstallableUnits87(self):
        return self.__aggregator_p2view_InstallableUnits87

    @aggregator_p2view_InstallableUnits87.setter
    def aggregator_p2view_InstallableUnits87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_InstallableUnits__aggregator_p2view_InstallableUnits87", None)
        self.__aggregator_p2view_InstallableUnits87 = value
        
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

    def getNotNullBundleContainer(self) -> str:
        # TODO: Implement getNotNullBundleContainer method
        pass

    def getNotNullFragmentContainer(self) -> str:
        # TODO: Implement getNotNullFragmentContainer method
        pass

    def getNotNullFeatureContainer(self) -> str:
        # TODO: Implement getNotNullFeatureContainer method
        pass

    def getNotNullCategoryContainer(self) -> str:
        # TODO: Implement getNotNullCategoryContainer method
        pass

    def getNotNullProductContainer(self) -> str:
        # TODO: Implement getNotNullProductContainer method
        pass

    def getNotNullMiscellaneousContainer(self) -> str:
        # TODO: Implement getNotNullMiscellaneousContainer method
        pass

class Properties:

    pass
class InstallableUnits:

    pass
class aggregator_p2view_MetadataRepositoryStructuredView:

    def __init__(self, name: str, loaded: bool, aggregator_p2view_MetadataRepositoryStructuredView: "InstallableUnits" = None, aggregator_p2view_MetadataRepositoryStructuredView73: "Properties" = None, aggregator_p2view_MetadataRepositoryStructuredView75: "MetadataRepository" = None):
        self.name = name
        self.loaded = loaded
        self.aggregator_p2view_MetadataRepositoryStructuredView = aggregator_p2view_MetadataRepositoryStructuredView
        self.aggregator_p2view_MetadataRepositoryStructuredView73 = aggregator_p2view_MetadataRepositoryStructuredView73
        self.aggregator_p2view_MetadataRepositoryStructuredView75 = aggregator_p2view_MetadataRepositoryStructuredView75
        
    @property
    def loaded(self) -> bool:
        return self.__loaded

    @loaded.setter
    def loaded(self, loaded: bool):
        self.__loaded = loaded

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def aggregator_p2view_MetadataRepositoryStructuredView75(self):
        return self.__aggregator_p2view_MetadataRepositoryStructuredView75

    @aggregator_p2view_MetadataRepositoryStructuredView75.setter
    def aggregator_p2view_MetadataRepositoryStructuredView75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2view_MetadataRepositoryStructuredView__aggregator_p2view_MetadataRepositoryStructuredView75", None)
        self.__aggregator_p2view_MetadataRepositoryStructuredView75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetadataRepository76"):
                opp_val = getattr(old_value, "MetadataRepository76", None)
                if opp_val == self:
                    setattr(old_value, "MetadataRepository76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetadataRepository76"):
                opp_val = getattr(value, "MetadataRepository76", None)
                setattr(value, "MetadataRepository76", self)

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
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

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
    def modifiable(self) -> bool:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: bool):
        self.__modifiable = modifiable

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

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    def getProperties(self) -> str:
        # TODO: Implement getProperties method
        pass

    def setProperty(self, value: str, key: str) -> str:
        # TODO: Implement setProperty method
        pass

class Miscellaneous:

    pass
class p2_IRepository:

    pass
class p2_IQueryable:

    pass
class aggregator_p2_IMetadataRepository(p2_IRepository, p2_IQueryable):

    def __init__(self):
        
    def addInstallableUnits(self, installableUnits: str):
        # TODO: Implement addInstallableUnits method
        pass

    def removeAll(self):
        # TODO: Implement removeAll method
        pass

    def removeInstallableUnits(self, query: str, monitor: str) -> bool:
        # TODO: Implement removeInstallableUnits method
        pass

    def addReference(self, type: int, options: int, location: str, nickname: str):
        # TODO: Implement addReference method
        pass

class aggregator_p2_IQueryable(ABC):

    def __init__(self):
        
    def query(self, progress: str, collector: str, query: str) -> str:
        # TODO: Implement query method
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
class aggregator_p2_InstallableUnitFragment(p2_IInstallableUnitFragment, p2_InstallableUnit):

    pass
class TouchpointData:

    pass
class RequiredCapability:

    pass
class ArtifactKey:

    pass
class ProvidedCapability:

    pass
class Property:

    pass
class RepositoryReference:

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

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    def isUpdateOf(self, iu: str) -> bool:
        # TODO: Implement isUpdateOf method
        pass

class aggregator_p2_ITouchpointType(ABC):

    def __init__(self, id: str, version: str):
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
        
    def getInstructions(self) -> str:
        # TODO: Implement getInstructions method
        pass

    def getInstruction(self, instructionKey: str) -> str:
        # TODO: Implement getInstruction method
        pass

class aggregator_p2_IRequiredCapability(ABC):

    def __init__(self, filter: str, name: str, namespace: str, range: str, negation: bool, selectorList: str, multiple: bool, optional: bool, greedy: bool):
        self.filter = filter
        self.name = name
        self.namespace = namespace
        self.range = range
        self.negation = negation
        self.selectorList = selectorList
        self.multiple = multiple
        self.optional = optional
        self.greedy = greedy
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def selectorList(self) -> str:
        return self.__selectorList

    @selectorList.setter
    def selectorList(self, selectorList: str):
        self.__selectorList = selectorList

    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

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
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def setSelectors(self, selectors: str):
        # TODO: Implement setSelectors method
        pass

    def getSelectors(self) -> str:
        # TODO: Implement getSelectors method
        pass

    def satisfiedBy(self, capability: str) -> bool:
        # TODO: Implement satisfiedBy method
        pass

class aggregator_p2_IProvidedCapability(ABC):

    def __init__(self, name: str, namespace: str, version: str):
        self.name = name
        self.namespace = namespace
        self.version = version
        
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
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    def satisfies(self, requirement: str) -> bool:
        # TODO: Implement satisfies method
        pass

class aggregator_p2_ILicense(ABC):

    def __init__(self, location: str, body: str, digest: str):
        self.location = location
        self.body = body
        self.digest = digest
        
    @property
    def digest(self) -> str:
        return self.__digest

    @digest.setter
    def digest(self, digest: str):
        self.__digest = digest

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

class IInstallableUnit:

    pass
class aggregator_p2_InstallableUnit(IInstallableUnit):

    def __init__(self, aggregator_p2_InstallableUnit56: set["ProvidedCapability"] = None, aggregator_p2_InstallableUnit: set["ArtifactKey"] = None, aggregator_p2_InstallableUnit58: set["RequiredCapability"] = None, aggregator_p2_InstallableUnit60: set["RequiredCapability"] = None, aggregator_p2_InstallableUnit63: set["Property"] = None, aggregator_p2_InstallableUnit66: set["TouchpointData"] = None):
        self.aggregator_p2_InstallableUnit56 = aggregator_p2_InstallableUnit56 if aggregator_p2_InstallableUnit56 is not None else set()
        self.aggregator_p2_InstallableUnit = aggregator_p2_InstallableUnit if aggregator_p2_InstallableUnit is not None else set()
        self.aggregator_p2_InstallableUnit58 = aggregator_p2_InstallableUnit58 if aggregator_p2_InstallableUnit58 is not None else set()
        self.aggregator_p2_InstallableUnit60 = aggregator_p2_InstallableUnit60 if aggregator_p2_InstallableUnit60 is not None else set()
        self.aggregator_p2_InstallableUnit63 = aggregator_p2_InstallableUnit63 if aggregator_p2_InstallableUnit63 is not None else set()
        self.aggregator_p2_InstallableUnit66 = aggregator_p2_InstallableUnit66 if aggregator_p2_InstallableUnit66 is not None else set()
        
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
    def aggregator_p2_InstallableUnit60(self):
        return self.__aggregator_p2_InstallableUnit60

    @aggregator_p2_InstallableUnit60.setter
    def aggregator_p2_InstallableUnit60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit60", None)
        self.__aggregator_p2_InstallableUnit60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredCapability61"):
                    opp_val = getattr(item, "RequiredCapability61", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredCapability61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredCapability61"):
                    opp_val = getattr(item, "RequiredCapability61", None)
                    
                    setattr(item, "RequiredCapability61", self)
                    

    @property
    def aggregator_p2_InstallableUnit63(self):
        return self.__aggregator_p2_InstallableUnit63

    @aggregator_p2_InstallableUnit63.setter
    def aggregator_p2_InstallableUnit63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit63", None)
        self.__aggregator_p2_InstallableUnit63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property64"):
                    opp_val = getattr(item, "Property64", None)
                    
                    if opp_val == self:
                        setattr(item, "Property64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property64"):
                    opp_val = getattr(item, "Property64", None)
                    
                    setattr(item, "Property64", self)
                    

    @property
    def aggregator_p2_InstallableUnit66(self):
        return self.__aggregator_p2_InstallableUnit66

    @aggregator_p2_InstallableUnit66.setter
    def aggregator_p2_InstallableUnit66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_InstallableUnit__aggregator_p2_InstallableUnit66", None)
        self.__aggregator_p2_InstallableUnit66 = value if value is not None else set()
        
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
class aggregator_p2_IInstallableUnit(ABC):

    def __init__(self, filter: str, id: str, version: str, resolved: bool, singleton: bool, aggregator_p2_IInstallableUnit: "ITouchpointType" = None, aggregator_p2_IInstallableUnit43: "IUpdateDescriptor" = None, aggregator_p2_IInstallableUnit45: "ILicense" = None, aggregator_p2_IInstallableUnit47: "ICopyright" = None):
        self.filter = filter
        self.id = id
        self.version = version
        self.resolved = resolved
        self.singleton = singleton
        self.aggregator_p2_IInstallableUnit = aggregator_p2_IInstallableUnit
        self.aggregator_p2_IInstallableUnit43 = aggregator_p2_IInstallableUnit43
        self.aggregator_p2_IInstallableUnit45 = aggregator_p2_IInstallableUnit45
        self.aggregator_p2_IInstallableUnit47 = aggregator_p2_IInstallableUnit47
        
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
    def aggregator_p2_IInstallableUnit43(self):
        return self.__aggregator_p2_IInstallableUnit43

    @aggregator_p2_IInstallableUnit43.setter
    def aggregator_p2_IInstallableUnit43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit43", None)
        self.__aggregator_p2_IInstallableUnit43 = value
        
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
    def aggregator_p2_IInstallableUnit45(self):
        return self.__aggregator_p2_IInstallableUnit45

    @aggregator_p2_IInstallableUnit45.setter
    def aggregator_p2_IInstallableUnit45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit45", None)
        self.__aggregator_p2_IInstallableUnit45 = value
        
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

    @property
    def aggregator_p2_IInstallableUnit47(self):
        return self.__aggregator_p2_IInstallableUnit47

    @aggregator_p2_IInstallableUnit47.setter
    def aggregator_p2_IInstallableUnit47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_p2_IInstallableUnit__aggregator_p2_IInstallableUnit47", None)
        self.__aggregator_p2_IInstallableUnit47 = value
        
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

    def unresolved(self) -> str:
        # TODO: Implement unresolved method
        pass

    def getTouchpointData(self) -> str:
        # TODO: Implement getTouchpointData method
        pass

    def getArtifacts(self) -> str:
        # TODO: Implement getArtifacts method
        pass

    def isFragment(self) -> bool:
        # TODO: Implement isFragment method
        pass

    def satisfies(self, candidate: str) -> bool:
        # TODO: Implement satisfies method
        pass

    def getMetaRequiredCapabilities(self) -> str:
        # TODO: Implement getMetaRequiredCapabilities method
        pass

    def getProperties(self) -> str:
        # TODO: Implement getProperties method
        pass

    def getFragments(self) -> str:
        # TODO: Implement getFragments method
        pass

    def getRequiredCapabilities(self) -> str:
        # TODO: Implement getRequiredCapabilities method
        pass

    def getProvidedCapabilities(self) -> str:
        # TODO: Implement getProvidedCapabilities method
        pass

    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

class aggregator_p2_ICopyright(ABC):

    def __init__(self, location: str, body: str):
        self.location = location
        self.body = body
        
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
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

class aggregator_Status:

    def __init__(self, message: str, code: str, aggregator_Status: "aggregator_StatusProvider" = None):
        self.message = message
        self.code = code
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
class aggregator_StatusProvider(ABC):

    pass
class InstallableUnit:

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

class InstallableUnitReference:

    pass
class MapRule:

    pass
class aggregator_ValidConfigurationsRule(MapRule):

    pass
class aggregator_ExclusionRule(MapRule):

    pass
class MappedUnit:

    pass
class EnabledStatusProvider:

    pass
class aggregator_MappedUnit(InstallableUnitReference, EnabledStatusProvider):

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
class aggregator_Contact:

    def __init__(self, name: str, email: str, aggregator_Contact: "aggregator_Aggregator" = None, Contact: "aggregator_Aggregator" = None, aggregator_Contact26: "aggregator_Contribution" = None, contacts: "aggregator_Aggregator" = None):
        self.name = name
        self.email = email
        self.aggregator_Contact = aggregator_Contact
        self.Contact = Contact
        self.aggregator_Contact26 = aggregator_Contact26
        self.contacts = contacts
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

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

    def __init__(self, operatingSystem: str, windowSystem: str, architecture: str, aggregator_Configuration: "aggregator_Aggregator" = None, aggregator_Configuration37: "aggregator_ValidConfigurationsRule" = None, aggregator_Configuration33: "aggregator_MappedUnit" = None):
        self.operatingSystem = operatingSystem
        self.windowSystem = windowSystem
        self.architecture = architecture
        self.aggregator_Configuration = aggregator_Configuration
        self.aggregator_Configuration37 = aggregator_Configuration37
        self.aggregator_Configuration33 = aggregator_Configuration33
        
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

    @property
    def aggregator_Configuration37(self):
        return self.__aggregator_Configuration37

    @aggregator_Configuration37.setter
    def aggregator_Configuration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_Configuration__aggregator_Configuration37", None)
        self.__aggregator_Configuration37 = value
        
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

    def getOSGiEnvironmentString(self) -> str:
        # TODO: Implement getOSGiEnvironmentString method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class InfosProvider:

    pass
class StatusProvider:

    pass
class aggregator_MetadataRepositoryReference(StatusProvider, InfosProvider, EnabledStatusProvider):

    def __init__(self, location: str, nature: str, aggregator_MetadataRepositoryReference: "aggregator_Aggregator" = None, aggregator_MetadataRepositoryReference39: "MetadataRepository" = None):
        self.location = location
        self.nature = nature
        self.aggregator_MetadataRepositoryReference = aggregator_MetadataRepositoryReference
        self.aggregator_MetadataRepositoryReference39 = aggregator_MetadataRepositoryReference39
        
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
    def aggregator_MetadataRepositoryReference39(self):
        return self.__aggregator_MetadataRepositoryReference39

    @aggregator_MetadataRepositoryReference39.setter
    def aggregator_MetadataRepositoryReference39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_MetadataRepositoryReference__aggregator_MetadataRepositoryReference39", None)
        self.__aggregator_MetadataRepositoryReference39 = value
        
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

    def onRepositoryLoad(self):
        # TODO: Implement onRepositoryLoad method
        pass

    def startRepositoryLoad(self, forceReload: bool):
        # TODO: Implement startRepositoryLoad method
        pass

    def cancelRepositoryLoad(self):
        # TODO: Implement cancelRepositoryLoad method
        pass

    def getMetadataRepository(self, forceResolve: bool) -> str:
        # TODO: Implement getMetadataRepository method
        pass

    def getResolvedLocation(self) -> str:
        # TODO: Implement getResolvedLocation method
        pass

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def getAggregator(self) -> str:
        # TODO: Implement getAggregator method
        pass

class aggregator_InstallableUnitReference(StatusProvider, InfosProvider):

    def __init__(self, aggregator_InstallableUnitReference: "InstallableUnit" = None):
        self.aggregator_InstallableUnitReference = aggregator_InstallableUnitReference
        
    @property
    def aggregator_InstallableUnitReference(self):
        return self.__aggregator_InstallableUnitReference

    @aggregator_InstallableUnitReference.setter
    def aggregator_InstallableUnitReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aggregator_InstallableUnitReference__aggregator_InstallableUnitReference", None)
        self.__aggregator_InstallableUnitReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InstallableUnit"):
                opp_val = getattr(old_value, "InstallableUnit", None)
                if opp_val == self:
                    setattr(old_value, "InstallableUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InstallableUnit"):
                opp_val = getattr(value, "InstallableUnit", None)
                setattr(value, "InstallableUnit", self)

    def getInstallableUnit(self, forceResolve: bool) -> str:
        # TODO: Implement getInstallableUnit method
        pass

    def isBranchEnabled(self) -> bool:
        # TODO: Implement isBranchEnabled method
        pass

    def isMappedRepositoryBroken(self) -> bool:
        # TODO: Implement isMappedRepositoryBroken method
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

class DescriptionProvider:

    pass
class aggregator_MapRule(DescriptionProvider, InstallableUnitReference):

    pass
class aggregator_Contribution(DescriptionProvider, InfosProvider, EnabledStatusProvider, StatusProvider):

    def __init__(self, label: str, aggregator_Contribution: "aggregator_Aggregator" = None, aggregator_Contribution22: set["aggregator_MappedRepository"] = None, aggregator_Contribution25: set["aggregator_Contact"] = None, aggregator_Contribution28: set["aggregator_MavenMapping"] = None):
        self.label = label
        self.aggregator_Contribution = aggregator_Contribution
        self.aggregator_Contribution22 = aggregator_Contribution22 if aggregator_Contribution22 is not None else set()
        self.aggregator_Contribution25 = aggregator_Contribution25 if aggregator_Contribution25 is not None else set()
        self.aggregator_Contribution28 = aggregator_Contribution28 if aggregator_Contribution28 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

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

    def getAllMavenMappings(self) -> str:
        # TODO: Implement getAllMavenMappings method
        pass

    def getRepositories(self, enabledOnly: bool) -> str:
        # TODO: Implement getRepositories method
        pass

class aggregator_Aggregator(StatusProvider, InfosProvider, DescriptionProvider):

    def __init__(self, label: str, buildRoot: str, packedStrategy: str, sendmail: bool, type: str, mavenResult: bool, aggregator_Aggregator11: set["aggregator_MavenMapping"] = None, aggregator_Aggregator: set["aggregator_Configuration"] = None, aggregator_Aggregator2: set["aggregator_Contribution"] = None, aggregator_Aggregator4: "aggregator_Contact" = None, aggregator: set["aggregator_Contact"] = None, aggregator_Aggregator7: set["aggregator_CustomCategory"] = None, aggregator_Aggregator9: set["aggregator_MetadataRepositoryReference"] = None, Aggregator: "aggregator_Contact" = None):
        self.label = label
        self.buildRoot = buildRoot
        self.packedStrategy = packedStrategy
        self.sendmail = sendmail
        self.type = type
        self.mavenResult = mavenResult
        self.aggregator_Aggregator11 = aggregator_Aggregator11 if aggregator_Aggregator11 is not None else set()
        self.aggregator_Aggregator = aggregator_Aggregator if aggregator_Aggregator is not None else set()
        self.aggregator_Aggregator2 = aggregator_Aggregator2 if aggregator_Aggregator2 is not None else set()
        self.aggregator_Aggregator4 = aggregator_Aggregator4
        self.aggregator = aggregator if aggregator is not None else set()
        self.aggregator_Aggregator7 = aggregator_Aggregator7 if aggregator_Aggregator7 is not None else set()
        self.aggregator_Aggregator9 = aggregator_Aggregator9 if aggregator_Aggregator9 is not None else set()
        self.Aggregator = Aggregator
        
    @property
    def packedStrategy(self) -> str:
        return self.__packedStrategy

    @packedStrategy.setter
    def packedStrategy(self, packedStrategy: str):
        self.__packedStrategy = packedStrategy

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
    def buildRoot(self) -> str:
        return self.__buildRoot

    @buildRoot.setter
    def buildRoot(self, buildRoot: str):
        self.__buildRoot = buildRoot

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
                    

    def getContributions(self, enabledOnly: bool) -> str:
        # TODO: Implement getContributions method
        pass

    def getValidationRepositories(self, enabledOnly: bool) -> str:
        # TODO: Implement getValidationRepositories method
        pass

    def getAllMetadataRepositoryReferences(self, enabledOnly: bool) -> str:
        # TODO: Implement getAllMetadataRepositoryReferences method
        pass

class MetadataRepositoryReference:

    pass
class aggregator_MappedRepository(DescriptionProvider, MetadataRepositoryReference):

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
    def mirrorArtifacts(self) -> bool:
        return self.__mirrorArtifacts

    @mirrorArtifacts.setter
    def mirrorArtifacts(self, mirrorArtifacts: bool):
        self.__mirrorArtifacts = mirrorArtifacts

    @property
    def categoryPrefix(self) -> str:
        return self.__categoryPrefix

    @categoryPrefix.setter
    def categoryPrefix(self, categoryPrefix: str):
        self.__categoryPrefix = categoryPrefix

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
                    

    def getUnits(self, enabledOnly: bool) -> str:
        # TODO: Implement getUnits method
        pass

    def isMapExclusive(self) -> bool:
        # TODO: Implement isMapExclusive method
        pass

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
