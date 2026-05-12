from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class WS(Enum):
    cocoa = "cocoa"
    motif = "motif"
    win32 = "win32"
    gtk = "gtk"
    carbon = "carbon"
class BuildType(Enum):
    Continuous = "Continuous"
    Nightly = "Nightly"
    Integration = "Integration"
    Stable = "Stable"
    Release = "Release"
    Maintenance = "Maintenance"
class ArchiveFormat(Enum):
    zip = "zip"
    tar = "tar"
class ARCH(Enum):
    x86 = "x86"
    ppc = "ppc"
    x86_64 = "x86_64"
    ppc64 = "ppc64"
    sparc = "sparc"
    ia64_32 = "ia64_32"
    s390 = "s390"
    s390x = "s390x"
class OS(Enum):
    win32 = "win32"
    linux = "linux"
    macosx = "macosx"
    solaris = "solaris"
    hpux = "hpux"
    aix = "aix"


############################################
# Definition of Classes
############################################

class build_InstallationUnit(ABC):

    def __init__(self, id: str, version: str, build_InstallationUnit: "build_Repository" = None):
        self.id = id
        self.version = version
        self.build_InstallationUnit = build_InstallationUnit
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def build_InstallationUnit(self):
        return self.__build_InstallationUnit

    @build_InstallationUnit.setter
    def build_InstallationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_InstallationUnit__build_InstallationUnit", None)
        self.__build_InstallationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Repository44"):
                opp_val = getattr(old_value, "build_Repository44", None)
                if opp_val == self:
                    setattr(old_value, "build_Repository44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Repository44"):
                opp_val = getattr(value, "build_Repository44", None)
                setattr(value, "build_Repository44", self)

class build_Repository:

    def __init__(self, location: str, label: str, build_Repository: "build_Contribution" = None, build_Repository44: "build_InstallationUnit" = None):
        self.location = location
        self.label = label
        self.build_Repository = build_Repository
        self.build_Repository44 = build_Repository44
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def build_Repository44(self):
        return self.__build_Repository44

    @build_Repository44.setter
    def build_Repository44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository44", None)
        self.__build_Repository44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_InstallationUnit"):
                opp_val = getattr(old_value, "build_InstallationUnit", None)
                if opp_val == self:
                    setattr(old_value, "build_InstallationUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_InstallationUnit"):
                opp_val = getattr(value, "build_InstallationUnit", None)
                setattr(value, "build_InstallationUnit", self)

    @property
    def build_Repository(self):
        return self.__build_Repository

    @build_Repository.setter
    def build_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository", None)
        self.__build_Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Contribution36"):
                opp_val = getattr(old_value, "build_Contribution36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Contribution36"):
                opp_val = getattr(value, "build_Contribution36", None)
                if opp_val is None:
                    setattr(value, "build_Contribution36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class InstallationUnit:

    pass
class build_Bundle(InstallationUnit):

    pass
class build_Feature(InstallationUnit):

    def __init__(self, inProduct: bool, Feature: "build_Category" = None, build_Feature: "build_Contribution" = None, features: set["build_Category"] = None):
        self.inProduct = inProduct
        self.Feature = Feature
        self.build_Feature = build_Feature
        self.features = features if features is not None else set()
        
        pass
    @property
    def inProduct(self):
        return self.__inProduct

    @inProduct.setter
    def inProduct(self, inProduct: bool):
        self.__inProduct = inProduct


    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Feature__features", None)
        self.__features = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    if opp_val == self:
                        setattr(item, "Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    setattr(item, "Category", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Feature(self):
        return self.__build_Feature

    @build_Feature.setter
    def build_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Feature__build_Feature", None)
        self.__build_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Contribution34"):
                opp_val = getattr(old_value, "build_Contribution34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Contribution34"):
                opp_val = getattr(value, "build_Contribution34", None)
                if opp_val is None:
                    setattr(value, "build_Contribution34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class build_Build:

    def __init__(self, buildRoot: str, fetchTag: str, label: str, date: str, time: str, launchVM: str, builderURL: str, sendmail: bool, type: str, build_Build8: set["build_Contribution"] = None, build_Build10: "build_Product" = None, build_Build12: "build_Platform" = None, build_Build15: "build_Platform" = None, build_Build18: "build_Compiler" = None, build_Build20: "build_Promotion" = None, build_Build22: "build_Contact" = None, build_Build24: set["build_Contact"] = None, build_Build: set["build_Platform"] = None, build_Build2: set["build_Config"] = None, build_Build4: "build_Map" = None, build_Build6: set["build_Category"] = None):
        self.buildRoot = buildRoot
        self.fetchTag = fetchTag
        self.label = label
        self.date = date
        self.time = time
        self.launchVM = launchVM
        self.builderURL = builderURL
        self.sendmail = sendmail
        self.type = type
        self.build_Build8 = build_Build8 if build_Build8 is not None else set()
        self.build_Build10 = build_Build10
        self.build_Build12 = build_Build12
        self.build_Build15 = build_Build15
        self.build_Build18 = build_Build18
        self.build_Build20 = build_Build20
        self.build_Build22 = build_Build22
        self.build_Build24 = build_Build24 if build_Build24 is not None else set()
        self.build_Build = build_Build if build_Build is not None else set()
        self.build_Build2 = build_Build2 if build_Build2 is not None else set()
        self.build_Build4 = build_Build4
        self.build_Build6 = build_Build6 if build_Build6 is not None else set()
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def buildRoot(self):
        return self.__buildRoot

    @buildRoot.setter
    def buildRoot(self, buildRoot: str):
        self.__buildRoot = buildRoot


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def builderURL(self):
        return self.__builderURL

    @builderURL.setter
    def builderURL(self, builderURL: str):
        self.__builderURL = builderURL


    @property
    def launchVM(self):
        return self.__launchVM

    @launchVM.setter
    def launchVM(self, launchVM: str):
        self.__launchVM = launchVM


    @property
    def fetchTag(self):
        return self.__fetchTag

    @fetchTag.setter
    def fetchTag(self, fetchTag: str):
        self.__fetchTag = fetchTag


    @property
    def sendmail(self):
        return self.__sendmail

    @sendmail.setter
    def sendmail(self, sendmail: bool):
        self.__sendmail = sendmail


    @property
    def build_Build22(self):
        return self.__build_Build22

    @build_Build22.setter
    def build_Build22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build22", None)
        self.__build_Build22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Contact"):
                opp_val = getattr(old_value, "build_Contact", None)
                if opp_val == self:
                    setattr(old_value, "build_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Contact"):
                opp_val = getattr(value, "build_Contact", None)
                setattr(value, "build_Contact", self)

    @property
    def build_Build10(self):
        return self.__build_Build10

    @build_Build10.setter
    def build_Build10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build10", None)
        self.__build_Build10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Product"):
                opp_val = getattr(old_value, "build_Product", None)
                if opp_val == self:
                    setattr(old_value, "build_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Product"):
                opp_val = getattr(value, "build_Product", None)
                setattr(value, "build_Product", self)

    @property
    def build_Build4(self):
        return self.__build_Build4

    @build_Build4.setter
    def build_Build4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build4", None)
        self.__build_Build4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Map"):
                opp_val = getattr(old_value, "build_Map", None)
                if opp_val == self:
                    setattr(old_value, "build_Map", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Map"):
                opp_val = getattr(value, "build_Map", None)
                setattr(value, "build_Map", self)

    @property
    def build_Build2(self):
        return self.__build_Build2

    @build_Build2.setter
    def build_Build2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build2", None)
        self.__build_Build2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Config"):
                    opp_val = getattr(item, "build_Config", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Config", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Config"):
                    opp_val = getattr(item, "build_Config", None)
                    
                    setattr(item, "build_Config", self)
                    

    @property
    def build_Build18(self):
        return self.__build_Build18

    @build_Build18.setter
    def build_Build18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build18", None)
        self.__build_Build18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Compiler"):
                opp_val = getattr(old_value, "build_Compiler", None)
                if opp_val == self:
                    setattr(old_value, "build_Compiler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Compiler"):
                opp_val = getattr(value, "build_Compiler", None)
                setattr(value, "build_Compiler", self)

    @property
    def build_Build6(self):
        return self.__build_Build6

    @build_Build6.setter
    def build_Build6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build6", None)
        self.__build_Build6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Category"):
                    opp_val = getattr(item, "build_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Category"):
                    opp_val = getattr(item, "build_Category", None)
                    
                    setattr(item, "build_Category", self)
                    

    @property
    def build_Build20(self):
        return self.__build_Build20

    @build_Build20.setter
    def build_Build20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build20", None)
        self.__build_Build20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Promotion"):
                opp_val = getattr(old_value, "build_Promotion", None)
                if opp_val == self:
                    setattr(old_value, "build_Promotion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Promotion"):
                opp_val = getattr(value, "build_Promotion", None)
                setattr(value, "build_Promotion", self)

    @property
    def build_Build15(self):
        return self.__build_Build15

    @build_Build15.setter
    def build_Build15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build15", None)
        self.__build_Build15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Platform16"):
                opp_val = getattr(old_value, "build_Platform16", None)
                if opp_val == self:
                    setattr(old_value, "build_Platform16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Platform16"):
                opp_val = getattr(value, "build_Platform16", None)
                setattr(value, "build_Platform16", self)

    @property
    def build_Build12(self):
        return self.__build_Build12

    @build_Build12.setter
    def build_Build12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build12", None)
        self.__build_Build12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Platform13"):
                opp_val = getattr(old_value, "build_Platform13", None)
                if opp_val == self:
                    setattr(old_value, "build_Platform13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Platform13"):
                opp_val = getattr(value, "build_Platform13", None)
                setattr(value, "build_Platform13", self)

    @property
    def build_Build(self):
        return self.__build_Build

    @build_Build.setter
    def build_Build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build", None)
        self.__build_Build = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Platform"):
                    opp_val = getattr(item, "build_Platform", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Platform", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Platform"):
                    opp_val = getattr(item, "build_Platform", None)
                    
                    setattr(item, "build_Platform", self)
                    

    @property
    def build_Build24(self):
        return self.__build_Build24

    @build_Build24.setter
    def build_Build24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build24", None)
        self.__build_Build24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Contact25"):
                    opp_val = getattr(item, "build_Contact25", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Contact25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Contact25"):
                    opp_val = getattr(item, "build_Contact25", None)
                    
                    setattr(item, "build_Contact25", self)
                    

    @property
    def build_Build8(self):
        return self.__build_Build8

    @build_Build8.setter
    def build_Build8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Build__build_Build8", None)
        self.__build_Build8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Contribution"):
                    opp_val = getattr(item, "build_Contribution", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Contribution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Contribution"):
                    opp_val = getattr(item, "build_Contribution", None)
                    
                    setattr(item, "build_Contribution", self)
                    

class build_Contact:

    def __init__(self, name: str, email: str, build_Contact: "build_Build" = None, build_Contact25: "build_Build" = None, build_Contact32: "build_Contribution" = None):
        self.name = name
        self.email = email
        self.build_Contact = build_Contact
        self.build_Contact25 = build_Contact25
        self.build_Contact32 = build_Contact32
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def build_Contact32(self):
        return self.__build_Contact32

    @build_Contact32.setter
    def build_Contact32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contact__build_Contact32", None)
        self.__build_Contact32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Contribution31"):
                opp_val = getattr(old_value, "build_Contribution31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Contribution31"):
                opp_val = getattr(value, "build_Contribution31", None)
                if opp_val is None:
                    setattr(value, "build_Contribution31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Contact25(self):
        return self.__build_Contact25

    @build_Contact25.setter
    def build_Contact25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contact__build_Contact25", None)
        self.__build_Contact25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build24"):
                opp_val = getattr(old_value, "build_Build24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build24"):
                opp_val = getattr(value, "build_Build24", None)
                if opp_val is None:
                    setattr(value, "build_Build24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Contact(self):
        return self.__build_Contact

    @build_Contact.setter
    def build_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contact__build_Contact", None)
        self.__build_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build22"):
                opp_val = getattr(old_value, "build_Build22", None)
                if opp_val == self:
                    setattr(old_value, "build_Build22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build22"):
                opp_val = getattr(value, "build_Build22", None)
                setattr(value, "build_Build22", self)

class build_Promotion:

    def __init__(self, uploadDirectory: str, downloadDirectory: str, incubating: bool, baseURL: str, buildAlias: str, build_Promotion: "build_Build" = None):
        self.uploadDirectory = uploadDirectory
        self.downloadDirectory = downloadDirectory
        self.incubating = incubating
        self.baseURL = baseURL
        self.buildAlias = buildAlias
        self.build_Promotion = build_Promotion
        
        pass
    @property
    def buildAlias(self):
        return self.__buildAlias

    @buildAlias.setter
    def buildAlias(self, buildAlias: str):
        self.__buildAlias = buildAlias


    @property
    def incubating(self):
        return self.__incubating

    @incubating.setter
    def incubating(self, incubating: bool):
        self.__incubating = incubating


    @property
    def downloadDirectory(self):
        return self.__downloadDirectory

    @downloadDirectory.setter
    def downloadDirectory(self, downloadDirectory: str):
        self.__downloadDirectory = downloadDirectory


    @property
    def baseURL(self):
        return self.__baseURL

    @baseURL.setter
    def baseURL(self, baseURL: str):
        self.__baseURL = baseURL


    @property
    def uploadDirectory(self):
        return self.__uploadDirectory

    @uploadDirectory.setter
    def uploadDirectory(self, uploadDirectory: str):
        self.__uploadDirectory = uploadDirectory


    @property
    def build_Promotion(self):
        return self.__build_Promotion

    @build_Promotion.setter
    def build_Promotion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Promotion__build_Promotion", None)
        self.__build_Promotion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build20"):
                opp_val = getattr(old_value, "build_Build20", None)
                if opp_val == self:
                    setattr(old_value, "build_Build20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build20"):
                opp_val = getattr(value, "build_Build20", None)
                setattr(value, "build_Build20", self)

class build_Compiler:

    def __init__(self, args: str, sourceVersion: str, targetVersion: str, verbose: bool, failOnError: bool, debugInfo: bool, build_Compiler: "build_Build" = None):
        self.args = args
        self.sourceVersion = sourceVersion
        self.targetVersion = targetVersion
        self.verbose = verbose
        self.failOnError = failOnError
        self.debugInfo = debugInfo
        self.build_Compiler = build_Compiler
        
        pass
    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: bool):
        self.__verbose = verbose


    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args


    @property
    def debugInfo(self):
        return self.__debugInfo

    @debugInfo.setter
    def debugInfo(self, debugInfo: bool):
        self.__debugInfo = debugInfo


    @property
    def sourceVersion(self):
        return self.__sourceVersion

    @sourceVersion.setter
    def sourceVersion(self, sourceVersion: str):
        self.__sourceVersion = sourceVersion


    @property
    def failOnError(self):
        return self.__failOnError

    @failOnError.setter
    def failOnError(self, failOnError: bool):
        self.__failOnError = failOnError


    @property
    def targetVersion(self):
        return self.__targetVersion

    @targetVersion.setter
    def targetVersion(self, targetVersion: str):
        self.__targetVersion = targetVersion


    @property
    def build_Compiler(self):
        return self.__build_Compiler

    @build_Compiler.setter
    def build_Compiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Compiler__build_Compiler", None)
        self.__build_Compiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build18"):
                opp_val = getattr(old_value, "build_Build18", None)
                if opp_val == self:
                    setattr(old_value, "build_Build18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build18"):
                opp_val = getattr(value, "build_Build18", None)
                setattr(value, "build_Build18", self)

class build_Product(InstallationUnit):

    pass
class build_Contribution:

    def __init__(self, label: str, build_Contribution: "build_Build" = None, build_Contribution31: set["build_Contact"] = None, build_Contribution34: set["build_Feature"] = None, build_Contribution36: set["build_Repository"] = None, build_Contribution38: set["build_Bundle"] = None, build_Contribution40: set["build_Product"] = None):
        self.label = label
        self.build_Contribution = build_Contribution
        self.build_Contribution31 = build_Contribution31 if build_Contribution31 is not None else set()
        self.build_Contribution34 = build_Contribution34 if build_Contribution34 is not None else set()
        self.build_Contribution36 = build_Contribution36 if build_Contribution36 is not None else set()
        self.build_Contribution38 = build_Contribution38 if build_Contribution38 is not None else set()
        self.build_Contribution40 = build_Contribution40 if build_Contribution40 is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def build_Contribution36(self):
        return self.__build_Contribution36

    @build_Contribution36.setter
    def build_Contribution36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution36", None)
        self.__build_Contribution36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Repository"):
                    opp_val = getattr(item, "build_Repository", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Repository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Repository"):
                    opp_val = getattr(item, "build_Repository", None)
                    
                    setattr(item, "build_Repository", self)
                    

    @property
    def build_Contribution38(self):
        return self.__build_Contribution38

    @build_Contribution38.setter
    def build_Contribution38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution38", None)
        self.__build_Contribution38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Bundle"):
                    opp_val = getattr(item, "build_Bundle", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Bundle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Bundle"):
                    opp_val = getattr(item, "build_Bundle", None)
                    
                    setattr(item, "build_Bundle", self)
                    

    @property
    def build_Contribution40(self):
        return self.__build_Contribution40

    @build_Contribution40.setter
    def build_Contribution40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution40", None)
        self.__build_Contribution40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Product41"):
                    opp_val = getattr(item, "build_Product41", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Product41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Product41"):
                    opp_val = getattr(item, "build_Product41", None)
                    
                    setattr(item, "build_Product41", self)
                    

    @property
    def build_Contribution(self):
        return self.__build_Contribution

    @build_Contribution.setter
    def build_Contribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution", None)
        self.__build_Contribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build8"):
                opp_val = getattr(old_value, "build_Build8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build8"):
                opp_val = getattr(value, "build_Build8", None)
                if opp_val is None:
                    setattr(value, "build_Build8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Contribution31(self):
        return self.__build_Contribution31

    @build_Contribution31.setter
    def build_Contribution31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution31", None)
        self.__build_Contribution31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Contact32"):
                    opp_val = getattr(item, "build_Contact32", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Contact32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Contact32"):
                    opp_val = getattr(item, "build_Contact32", None)
                    
                    setattr(item, "build_Contact32", self)
                    

    @property
    def build_Contribution34(self):
        return self.__build_Contribution34

    @build_Contribution34.setter
    def build_Contribution34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Contribution__build_Contribution34", None)
        self.__build_Contribution34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Feature"):
                    opp_val = getattr(item, "build_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Feature"):
                    opp_val = getattr(item, "build_Feature", None)
                    
                    setattr(item, "build_Feature", self)
                    

class build_Category:

    def __init__(self, name: str, label: str, description: str, category: set["build_Feature"] = None, Category: "build_Feature" = None, build_Category: "build_Build" = None):
        self.name = name
        self.label = label
        self.description = description
        self.category = category if category is not None else set()
        self.Category = Category
        self.build_Category = build_Category
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Category__Category", None)
        self.__Category = value
        
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
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Category__category", None)
        self.__category = value if value is not None else set()
        
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
    def build_Category(self):
        return self.__build_Category

    @build_Category.setter
    def build_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Category__build_Category", None)
        self.__build_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build6"):
                opp_val = getattr(old_value, "build_Build6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build6"):
                opp_val = getattr(value, "build_Build6", None)
                if opp_val is None:
                    setattr(value, "build_Build6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class build_Map:

    def __init__(self, root: str, repo: str, tag: str, build_Map: "build_Build" = None):
        self.root = root
        self.repo = repo
        self.tag = tag
        self.build_Map = build_Map
        
        pass
    @property
    def repo(self):
        return self.__repo

    @repo.setter
    def repo(self, repo: str):
        self.__repo = repo


    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root: str):
        self.__root = root


    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag


    @property
    def build_Map(self):
        return self.__build_Map

    @build_Map.setter
    def build_Map(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Map__build_Map", None)
        self.__build_Map = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build4"):
                opp_val = getattr(old_value, "build_Build4", None)
                if opp_val == self:
                    setattr(old_value, "build_Build4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build4"):
                opp_val = getattr(value, "build_Build4", None)
                setattr(value, "build_Build4", self)

class build_Config:

    def __init__(self, os: str, ws: str, arch: str, archiveFormat: str, build_Config28: "build_Platform" = None, build_Config: "build_Build" = None):
        self.os = os
        self.ws = ws
        self.arch = arch
        self.archiveFormat = archiveFormat
        self.build_Config28 = build_Config28
        self.build_Config = build_Config
        
        pass
    @property
    def archiveFormat(self):
        return self.__archiveFormat

    @archiveFormat.setter
    def archiveFormat(self, archiveFormat: str):
        self.__archiveFormat = archiveFormat


    @property
    def ws(self):
        return self.__ws

    @ws.setter
    def ws(self, ws: str):
        self.__ws = ws


    @property
    def arch(self):
        return self.__arch

    @arch.setter
    def arch(self, arch: str):
        self.__arch = arch


    @property
    def os(self):
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os


    @property
    def build_Config28(self):
        return self.__build_Config28

    @build_Config28.setter
    def build_Config28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Config__build_Config28", None)
        self.__build_Config28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Platform27"):
                opp_val = getattr(old_value, "build_Platform27", None)
                if opp_val == self:
                    setattr(old_value, "build_Platform27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Platform27"):
                opp_val = getattr(value, "build_Platform27", None)
                setattr(value, "build_Platform27", self)

    @property
    def build_Config(self):
        return self.__build_Config

    @build_Config.setter
    def build_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Config__build_Config", None)
        self.__build_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build2"):
                opp_val = getattr(old_value, "build_Build2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build2"):
                opp_val = getattr(value, "build_Build2", None)
                if opp_val is None:
                    setattr(value, "build_Build2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class build_Platform:

    def __init__(self, file: str, location: str, deltapack: str, build_Platform13: "build_Build" = None, build_Platform16: "build_Build" = None, build_Platform27: "build_Config" = None, build_Platform: "build_Build" = None):
        self.file = file
        self.location = location
        self.deltapack = deltapack
        self.build_Platform13 = build_Platform13
        self.build_Platform16 = build_Platform16
        self.build_Platform27 = build_Platform27
        self.build_Platform = build_Platform
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def deltapack(self):
        return self.__deltapack

    @deltapack.setter
    def deltapack(self, deltapack: str):
        self.__deltapack = deltapack


    @property
    def build_Platform(self):
        return self.__build_Platform

    @build_Platform.setter
    def build_Platform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Platform__build_Platform", None)
        self.__build_Platform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build"):
                opp_val = getattr(old_value, "build_Build", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build"):
                opp_val = getattr(value, "build_Build", None)
                if opp_val is None:
                    setattr(value, "build_Build", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Platform13(self):
        return self.__build_Platform13

    @build_Platform13.setter
    def build_Platform13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Platform__build_Platform13", None)
        self.__build_Platform13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build12"):
                opp_val = getattr(old_value, "build_Build12", None)
                if opp_val == self:
                    setattr(old_value, "build_Build12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build12"):
                opp_val = getattr(value, "build_Build12", None)
                setattr(value, "build_Build12", self)

    @property
    def build_Platform27(self):
        return self.__build_Platform27

    @build_Platform27.setter
    def build_Platform27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Platform__build_Platform27", None)
        self.__build_Platform27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Config28"):
                opp_val = getattr(old_value, "build_Config28", None)
                if opp_val == self:
                    setattr(old_value, "build_Config28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Config28"):
                opp_val = getattr(value, "build_Config28", None)
                setattr(value, "build_Config28", self)

    @property
    def build_Platform16(self):
        return self.__build_Platform16

    @build_Platform16.setter
    def build_Platform16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Platform__build_Platform16", None)
        self.__build_Platform16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Build15"):
                opp_val = getattr(old_value, "build_Build15", None)
                if opp_val == self:
                    setattr(old_value, "build_Build15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Build15"):
                opp_val = getattr(value, "build_Build15", None)
                setattr(value, "build_Build15", self)
