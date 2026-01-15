from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Language(Enum):
    C = "C"
    Other = "Other"
    Java = "Java"
    Cpp = "Cpp"


############################################
# Definition of Classes
############################################

class libraryElement_Primitive:

    def __init__(self, event: str, parameters: str, libraryElement_Primitive: "libraryElement_ServiceInterface" = None):
        self.event = event
        self.parameters = parameters
        self.libraryElement_Primitive = libraryElement_Primitive
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def libraryElement_Primitive(self):
        return self.__libraryElement_Primitive

    @libraryElement_Primitive.setter
    def libraryElement_Primitive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Primitive__libraryElement_Primitive", None)
        self.__libraryElement_Primitive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ServiceInterface171"):
                opp_val = getattr(old_value, "libraryElement_ServiceInterface171", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_ServiceInterface171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ServiceInterface171"):
                opp_val = getattr(value, "libraryElement_ServiceInterface171", None)
                setattr(value, "libraryElement_ServiceInterface171", self)

class libraryElement_IVarElement(ABC):

    pass
class libraryElement_ColorizableElement:

    pass
class libraryElement_Color:

    def __init__(self, red: str, green: str, blue: str, libraryElement_Color: "libraryElement_ColorizableElement" = None):
        self.red = red
        self.green = green
        self.blue = blue
        self.libraryElement_Color = libraryElement_Color
        
    @property
    def blue(self) -> str:
        return self.__blue

    @blue.setter
    def blue(self, blue: str):
        self.__blue = blue

    @property
    def red(self) -> str:
        return self.__red

    @red.setter
    def red(self, red: str):
        self.__red = red

    @property
    def green(self) -> str:
        return self.__green

    @green.setter
    def green(self, green: str):
        self.__green = green

    @property
    def libraryElement_Color(self):
        return self.__libraryElement_Color

    @libraryElement_Color.setter
    def libraryElement_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Color__libraryElement_Color", None)
        self.__libraryElement_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ColorizableElement"):
                opp_val = getattr(old_value, "libraryElement_ColorizableElement", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_ColorizableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ColorizableElement"):
                opp_val = getattr(value, "libraryElement_ColorizableElement", None)
                setattr(value, "libraryElement_ColorizableElement", self)

class libraryElement_PositionableElement:

    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

class Event:

    pass
class libraryElement_AdapterEvent(Event):

    pass
class libraryElement_Annotation:

    def __init__(self, name: str, servity: str, libraryElement_Annotation: "libraryElement_I4DIACElement" = None):
        self.name = name
        self.servity = servity
        self.libraryElement_Annotation = libraryElement_Annotation
        
    @property
    def servity(self) -> str:
        return self.__servity

    @servity.setter
    def servity(self, servity: str):
        self.__servity = servity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryElement_Annotation(self):
        return self.__libraryElement_Annotation

    @libraryElement_Annotation.setter
    def libraryElement_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Annotation__libraryElement_Annotation", None)
        self.__libraryElement_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_I4DIACElement"):
                opp_val = getattr(old_value, "libraryElement_I4DIACElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_I4DIACElement"):
                opp_val = getattr(value, "libraryElement_I4DIACElement", None)
                if opp_val is None:
                    setattr(value, "libraryElement_I4DIACElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryElement_I4DIACElement(ABC):

    def __init__(self, libraryElement_I4DIACElement: set["libraryElement_Annotation"] = None):
        self.libraryElement_I4DIACElement = libraryElement_I4DIACElement if libraryElement_I4DIACElement is not None else set()
        
    @property
    def libraryElement_I4DIACElement(self):
        return self.__libraryElement_I4DIACElement

    @libraryElement_I4DIACElement.setter
    def libraryElement_I4DIACElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_I4DIACElement__libraryElement_I4DIACElement", None)
        self.__libraryElement_I4DIACElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Annotation"):
                    opp_val = getattr(item, "libraryElement_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Annotation"):
                    opp_val = getattr(item, "libraryElement_Annotation", None)
                    
                    setattr(item, "libraryElement_Annotation", self)
                    

    def createAnnotation(self, name: str) -> str:
        # TODO: Implement createAnnotation method
        pass

    def removeAnnotation(self, annotation: str):
        # TODO: Implement removeAnnotation method
        pass

class FB:

    pass
class libraryElement_ResourceTypeFB(FB):

    def __init__(self):
        
    def isResourceTypeFB(self) -> bool:
        # TODO: Implement isResourceTypeFB method
        pass

class I4DIACElement:

    pass
class libraryElement_INamedElement(I4DIACElement):

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class libraryElement_Value:

    def __init__(self, value: str, libraryElement_Value: "libraryElement_IInterfaceElement" = None):
        self.value = value
        self.libraryElement_Value = libraryElement_Value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def libraryElement_Value(self):
        return self.__libraryElement_Value

    @libraryElement_Value.setter
    def libraryElement_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Value__libraryElement_Value", None)
        self.__libraryElement_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_IInterfaceElement144"):
                opp_val = getattr(old_value, "libraryElement_IInterfaceElement144", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_IInterfaceElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_IInterfaceElement144"):
                opp_val = getattr(value, "libraryElement_IInterfaceElement144", None)
                setattr(value, "libraryElement_IInterfaceElement144", self)

    def getVarDeclaration(self) -> VarDeclaration:
        # TODO: Implement getVarDeclaration method
        pass

class libraryElement_DataType:

    pass
class Connection:

    pass
class Algorithm:

    pass
class libraryElement_TextAlgorithm(Algorithm):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class libraryElement_PaletteEntry:

    pass
class libraryElement_Palette:

    pass
class libraryElement_VersionInfo:

    def __init__(self, author: str, remarks: str, version: str, date: str, organization: str, libraryElement_VersionInfo: "libraryElement_LibraryElement" = None):
        self.author = author
        self.remarks = remarks
        self.version = version
        self.date = date
        self.organization = organization
        self.libraryElement_VersionInfo = libraryElement_VersionInfo
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def remarks(self) -> str:
        return self.__remarks

    @remarks.setter
    def remarks(self, remarks: str):
        self.__remarks = remarks

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def libraryElement_VersionInfo(self):
        return self.__libraryElement_VersionInfo

    @libraryElement_VersionInfo.setter
    def libraryElement_VersionInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VersionInfo__libraryElement_VersionInfo", None)
        self.__libraryElement_VersionInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_LibraryElement"):
                opp_val = getattr(old_value, "libraryElement_LibraryElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_LibraryElement"):
                opp_val = getattr(value, "libraryElement_LibraryElement", None)
                if opp_val is None:
                    setattr(value, "libraryElement_LibraryElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryElement_VarInitialization:

    pass
class libraryElement_SystemConfiguration(I4DIACElement):

    def __init__(self, libraryElement_SystemConfiguration: "libraryElement_AutomationSystem" = None, libraryElement_SystemConfiguration151: set["libraryElement_Link"] = None, libraryElement_SystemConfiguration146: set["libraryElement_Device"] = None, libraryElement_SystemConfiguration148: set["libraryElement_Segment"] = None):
        self.libraryElement_SystemConfiguration = libraryElement_SystemConfiguration
        self.libraryElement_SystemConfiguration151 = libraryElement_SystemConfiguration151 if libraryElement_SystemConfiguration151 is not None else set()
        self.libraryElement_SystemConfiguration146 = libraryElement_SystemConfiguration146 if libraryElement_SystemConfiguration146 is not None else set()
        self.libraryElement_SystemConfiguration148 = libraryElement_SystemConfiguration148 if libraryElement_SystemConfiguration148 is not None else set()
        
    @property
    def libraryElement_SystemConfiguration148(self):
        return self.__libraryElement_SystemConfiguration148

    @libraryElement_SystemConfiguration148.setter
    def libraryElement_SystemConfiguration148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration148", None)
        self.__libraryElement_SystemConfiguration148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Segment149"):
                    opp_val = getattr(item, "libraryElement_Segment149", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Segment149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Segment149"):
                    opp_val = getattr(item, "libraryElement_Segment149", None)
                    
                    setattr(item, "libraryElement_Segment149", self)
                    

    @property
    def libraryElement_SystemConfiguration(self):
        return self.__libraryElement_SystemConfiguration

    @libraryElement_SystemConfiguration.setter
    def libraryElement_SystemConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration", None)
        self.__libraryElement_SystemConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_AutomationSystem123"):
                opp_val = getattr(old_value, "libraryElement_AutomationSystem123", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_AutomationSystem123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_AutomationSystem123"):
                opp_val = getattr(value, "libraryElement_AutomationSystem123", None)
                setattr(value, "libraryElement_AutomationSystem123", self)

    @property
    def libraryElement_SystemConfiguration146(self):
        return self.__libraryElement_SystemConfiguration146

    @libraryElement_SystemConfiguration146.setter
    def libraryElement_SystemConfiguration146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration146", None)
        self.__libraryElement_SystemConfiguration146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Device"):
                    opp_val = getattr(item, "libraryElement_Device", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Device"):
                    opp_val = getattr(item, "libraryElement_Device", None)
                    
                    setattr(item, "libraryElement_Device", self)
                    

    @property
    def libraryElement_SystemConfiguration151(self):
        return self.__libraryElement_SystemConfiguration151

    @libraryElement_SystemConfiguration151.setter
    def libraryElement_SystemConfiguration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration151", None)
        self.__libraryElement_SystemConfiguration151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Link"):
                    opp_val = getattr(item, "libraryElement_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Link"):
                    opp_val = getattr(item, "libraryElement_Link", None)
                    
                    setattr(item, "libraryElement_Link", self)
                    

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

    def getSegmentNamed(self, name: str) -> str:
        # TODO: Implement getSegmentNamed method
        pass

    def getDeviceNamed(self, name: str) -> str:
        # TODO: Implement getDeviceNamed method
        pass

class libraryElement_EventConnection(Connection):

    def __init__(self, libraryElement_EventConnection: "libraryElement_FBNetwork" = None):
        self.libraryElement_EventConnection = libraryElement_EventConnection
        
    @property
    def libraryElement_EventConnection(self):
        return self.__libraryElement_EventConnection

    @libraryElement_EventConnection.setter
    def libraryElement_EventConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_EventConnection__libraryElement_EventConnection", None)
        self.__libraryElement_EventConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork113"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork113"):
                opp_val = getattr(value, "libraryElement_FBNetwork113", None)
                if opp_val is None:
                    setattr(value, "libraryElement_FBNetwork113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

    def getDestination(self) -> str:
        # TODO: Implement getDestination method
        pass

class libraryElement_DataConnection(Connection):

    def __init__(self, libraryElement_DataConnection: "libraryElement_FBNetwork" = None):
        self.libraryElement_DataConnection = libraryElement_DataConnection
        
    @property
    def libraryElement_DataConnection(self):
        return self.__libraryElement_DataConnection

    @libraryElement_DataConnection.setter
    def libraryElement_DataConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_DataConnection__libraryElement_DataConnection", None)
        self.__libraryElement_DataConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork111"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork111"):
                opp_val = getattr(value, "libraryElement_FBNetwork111", None)
                if opp_val is None:
                    setattr(value, "libraryElement_FBNetwork111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getDestination(self) -> VarDeclaration:
        # TODO: Implement getDestination method
        pass

    def getSource(self) -> VarDeclaration:
        # TODO: Implement getSource method
        pass

class LibraryElement:

    pass
class libraryElement_CompilableType(LibraryElement):

    pass
class libraryElement_AutomationSystem(LibraryElement):

    def __init__(self, project: str, libraryElement_AutomationSystem: set["libraryElement_Application"] = None, libraryElement_AutomationSystem123: "libraryElement_SystemConfiguration" = None, libraryElement_AutomationSystem119: set["libraryElement_Mapping"] = None, automationSystem: "libraryElement_Palette" = None):
        self.project = project
        self.libraryElement_AutomationSystem = libraryElement_AutomationSystem if libraryElement_AutomationSystem is not None else set()
        self.libraryElement_AutomationSystem123 = libraryElement_AutomationSystem123
        self.libraryElement_AutomationSystem119 = libraryElement_AutomationSystem119 if libraryElement_AutomationSystem119 is not None else set()
        self.automationSystem = automationSystem
        
    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def automationSystem(self):
        return self.__automationSystem

    @automationSystem.setter
    def automationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AutomationSystem__automationSystem", None)
        self.__automationSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "palette.ecorePalette"):
                opp_val = getattr(old_value, "palette.ecorePalette", None)
                if opp_val == self:
                    setattr(old_value, "palette.ecorePalette", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "palette.ecorePalette"):
                opp_val = getattr(value, "palette.ecorePalette", None)
                setattr(value, "palette.ecorePalette", self)

    @property
    def libraryElement_AutomationSystem119(self):
        return self.__libraryElement_AutomationSystem119

    @libraryElement_AutomationSystem119.setter
    def libraryElement_AutomationSystem119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AutomationSystem__libraryElement_AutomationSystem119", None)
        self.__libraryElement_AutomationSystem119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Mapping120"):
                    opp_val = getattr(item, "libraryElement_Mapping120", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Mapping120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Mapping120"):
                    opp_val = getattr(item, "libraryElement_Mapping120", None)
                    
                    setattr(item, "libraryElement_Mapping120", self)
                    

    @property
    def libraryElement_AutomationSystem(self):
        return self.__libraryElement_AutomationSystem

    @libraryElement_AutomationSystem.setter
    def libraryElement_AutomationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AutomationSystem__libraryElement_AutomationSystem", None)
        self.__libraryElement_AutomationSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Application117"):
                    opp_val = getattr(item, "libraryElement_Application117", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Application117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Application117"):
                    opp_val = getattr(item, "libraryElement_Application117", None)
                    
                    setattr(item, "libraryElement_Application117", self)
                    

    @property
    def libraryElement_AutomationSystem123(self):
        return self.__libraryElement_AutomationSystem123

    @libraryElement_AutomationSystem123.setter
    def libraryElement_AutomationSystem123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AutomationSystem__libraryElement_AutomationSystem123", None)
        self.__libraryElement_AutomationSystem123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_SystemConfiguration"):
                opp_val = getattr(old_value, "libraryElement_SystemConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_SystemConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_SystemConfiguration"):
                opp_val = getattr(value, "libraryElement_SystemConfiguration", None)
                setattr(value, "libraryElement_SystemConfiguration", self)

    def getApplicationNamed(self, name: str) -> str:
        # TODO: Implement getApplicationNamed method
        pass

    def getDeviceNamed(self, name: str) -> str:
        # TODO: Implement getDeviceNamed method
        pass

class CompositeFBType:

    pass
class libraryElement_SubAppType(CompositeFBType):

    pass
class libraryElement_AdapterConnection(Connection):

    def __init__(self, libraryElement_AdapterConnection: "libraryElement_FBNetwork" = None):
        self.libraryElement_AdapterConnection = libraryElement_AdapterConnection
        
    @property
    def libraryElement_AdapterConnection(self):
        return self.__libraryElement_AdapterConnection

    @libraryElement_AdapterConnection.setter
    def libraryElement_AdapterConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AdapterConnection__libraryElement_AdapterConnection", None)
        self.__libraryElement_AdapterConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork115"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork115"):
                opp_val = getattr(value, "libraryElement_FBNetwork115", None)
                if opp_val is None:
                    setattr(value, "libraryElement_FBNetwork115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

    def getDestination(self) -> str:
        # TODO: Implement getDestination method
        pass

class libraryElement_ServiceTransaction:

    def __init__(self, TestResult: str, libraryElement_ServiceTransaction: "libraryElement_ServiceSequence" = None, libraryElement_ServiceTransaction106: set["libraryElement_OutputPrimitive"] = None, libraryElement_ServiceTransaction104: "libraryElement_InputPrimitive" = None):
        self.TestResult = TestResult
        self.libraryElement_ServiceTransaction = libraryElement_ServiceTransaction
        self.libraryElement_ServiceTransaction106 = libraryElement_ServiceTransaction106 if libraryElement_ServiceTransaction106 is not None else set()
        self.libraryElement_ServiceTransaction104 = libraryElement_ServiceTransaction104
        
    @property
    def TestResult(self) -> str:
        return self.__TestResult

    @TestResult.setter
    def TestResult(self, TestResult: str):
        self.__TestResult = TestResult

    @property
    def libraryElement_ServiceTransaction104(self):
        return self.__libraryElement_ServiceTransaction104

    @libraryElement_ServiceTransaction104.setter
    def libraryElement_ServiceTransaction104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ServiceTransaction__libraryElement_ServiceTransaction104", None)
        self.__libraryElement_ServiceTransaction104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_InputPrimitive"):
                opp_val = getattr(old_value, "libraryElement_InputPrimitive", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_InputPrimitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_InputPrimitive"):
                opp_val = getattr(value, "libraryElement_InputPrimitive", None)
                setattr(value, "libraryElement_InputPrimitive", self)

    @property
    def libraryElement_ServiceTransaction(self):
        return self.__libraryElement_ServiceTransaction

    @libraryElement_ServiceTransaction.setter
    def libraryElement_ServiceTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ServiceTransaction__libraryElement_ServiceTransaction", None)
        self.__libraryElement_ServiceTransaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ServiceSequence"):
                opp_val = getattr(old_value, "libraryElement_ServiceSequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ServiceSequence"):
                opp_val = getattr(value, "libraryElement_ServiceSequence", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ServiceSequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_ServiceTransaction106(self):
        return self.__libraryElement_ServiceTransaction106

    @libraryElement_ServiceTransaction106.setter
    def libraryElement_ServiceTransaction106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ServiceTransaction__libraryElement_ServiceTransaction106", None)
        self.__libraryElement_ServiceTransaction106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_OutputPrimitive"):
                    opp_val = getattr(item, "libraryElement_OutputPrimitive", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_OutputPrimitive", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_OutputPrimitive"):
                    opp_val = getattr(item, "libraryElement_OutputPrimitive", None)
                    
                    setattr(item, "libraryElement_OutputPrimitive", self)
                    

class libraryElement_Parameter:

    def __init__(self, name: str, value: str, comment: str, libraryElement_Parameter: "libraryElement_ConfigurableObject" = None):
        self.name = name
        self.value = value
        self.comment = comment
        self.libraryElement_Parameter = libraryElement_Parameter
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def libraryElement_Parameter(self):
        return self.__libraryElement_Parameter

    @libraryElement_Parameter.setter
    def libraryElement_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Parameter__libraryElement_Parameter", None)
        self.__libraryElement_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ConfigurableObject"):
                opp_val = getattr(old_value, "libraryElement_ConfigurableObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ConfigurableObject"):
                opp_val = getattr(value, "libraryElement_ConfigurableObject", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ConfigurableObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TextAlgorithm:

    pass
class libraryElement_STAlgorithm(TextAlgorithm):

    pass
class libraryElement_OtherAlgorithm(TextAlgorithm):

    def __init__(self, language: str):
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

class Primitive:

    pass
class libraryElement_OutputPrimitive(Primitive):

    def __init__(self, TestResult: str, libraryElement_OutputPrimitive: "libraryElement_ServiceTransaction" = None):
        self.TestResult = TestResult
        self.libraryElement_OutputPrimitive = libraryElement_OutputPrimitive
        
    @property
    def TestResult(self) -> str:
        return self.__TestResult

    @TestResult.setter
    def TestResult(self, TestResult: str):
        self.__TestResult = TestResult

    @property
    def libraryElement_OutputPrimitive(self):
        return self.__libraryElement_OutputPrimitive

    @libraryElement_OutputPrimitive.setter
    def libraryElement_OutputPrimitive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_OutputPrimitive__libraryElement_OutputPrimitive", None)
        self.__libraryElement_OutputPrimitive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ServiceTransaction106"):
                opp_val = getattr(old_value, "libraryElement_ServiceTransaction106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ServiceTransaction106"):
                opp_val = getattr(value, "libraryElement_ServiceTransaction106", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ServiceTransaction106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryElement_InputPrimitive(Primitive):

    pass
class libraryElement_Service(I4DIACElement):

    pass
class libraryElement_Identification:

    def __init__(self, applicationDomain: str, classification: str, description: str, function: str, standard: str, type: str, libraryElement_Identification: "libraryElement_LibraryElement" = None):
        self.applicationDomain = applicationDomain
        self.classification = classification
        self.description = description
        self.function = function
        self.standard = standard
        self.type = type
        self.libraryElement_Identification = libraryElement_Identification
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def applicationDomain(self) -> str:
        return self.__applicationDomain

    @applicationDomain.setter
    def applicationDomain(self, applicationDomain: str):
        self.__applicationDomain = applicationDomain

    @property
    def standard(self) -> str:
        return self.__standard

    @standard.setter
    def standard(self, standard: str):
        self.__standard = standard

    @property
    def classification(self) -> str:
        return self.__classification

    @classification.setter
    def classification(self, classification: str):
        self.__classification = classification

    @property
    def libraryElement_Identification(self):
        return self.__libraryElement_Identification

    @libraryElement_Identification.setter
    def libraryElement_Identification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Identification__libraryElement_Identification", None)
        self.__libraryElement_Identification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_LibraryElement130"):
                opp_val = getattr(old_value, "libraryElement_LibraryElement130", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_LibraryElement130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_LibraryElement130"):
                opp_val = getattr(value, "libraryElement_LibraryElement130", None)
                setattr(value, "libraryElement_LibraryElement130", self)

class libraryElement_Mapping:

    def __init__(self, libraryElement_Mapping: "libraryElement_FBNetworkElement" = None, libraryElement_Mapping80: "libraryElement_FBNetworkElement" = None, libraryElement_Mapping83: "libraryElement_FBNetworkElement" = None, libraryElement_Mapping120: "libraryElement_AutomationSystem" = None):
        self.libraryElement_Mapping = libraryElement_Mapping
        self.libraryElement_Mapping80 = libraryElement_Mapping80
        self.libraryElement_Mapping83 = libraryElement_Mapping83
        self.libraryElement_Mapping120 = libraryElement_Mapping120
        
    @property
    def libraryElement_Mapping(self):
        return self.__libraryElement_Mapping

    @libraryElement_Mapping.setter
    def libraryElement_Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Mapping__libraryElement_Mapping", None)
        self.__libraryElement_Mapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetworkElement52"):
                opp_val = getattr(old_value, "libraryElement_FBNetworkElement52", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetworkElement52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetworkElement52"):
                opp_val = getattr(value, "libraryElement_FBNetworkElement52", None)
                setattr(value, "libraryElement_FBNetworkElement52", self)

    @property
    def libraryElement_Mapping83(self):
        return self.__libraryElement_Mapping83

    @libraryElement_Mapping83.setter
    def libraryElement_Mapping83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Mapping__libraryElement_Mapping83", None)
        self.__libraryElement_Mapping83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetworkElement84"):
                opp_val = getattr(old_value, "libraryElement_FBNetworkElement84", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetworkElement84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetworkElement84"):
                opp_val = getattr(value, "libraryElement_FBNetworkElement84", None)
                setattr(value, "libraryElement_FBNetworkElement84", self)

    @property
    def libraryElement_Mapping80(self):
        return self.__libraryElement_Mapping80

    @libraryElement_Mapping80.setter
    def libraryElement_Mapping80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Mapping__libraryElement_Mapping80", None)
        self.__libraryElement_Mapping80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetworkElement81"):
                opp_val = getattr(old_value, "libraryElement_FBNetworkElement81", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetworkElement81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetworkElement81"):
                opp_val = getattr(value, "libraryElement_FBNetworkElement81", None)
                setattr(value, "libraryElement_FBNetworkElement81", self)

    @property
    def libraryElement_Mapping120(self):
        return self.__libraryElement_Mapping120

    @libraryElement_Mapping120.setter
    def libraryElement_Mapping120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Mapping__libraryElement_Mapping120", None)
        self.__libraryElement_Mapping120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_AutomationSystem119"):
                opp_val = getattr(old_value, "libraryElement_AutomationSystem119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_AutomationSystem119"):
                opp_val = getattr(value, "libraryElement_AutomationSystem119", None)
                if opp_val is None:
                    setattr(value, "libraryElement_AutomationSystem119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

class libraryElement_InterfaceList:

    def __init__(self, libraryElement_InterfaceList: "libraryElement_FBNetworkElement" = None, libraryElement_InterfaceList56: "libraryElement_FBType" = None, libraryElement_InterfaceList60: set["libraryElement_AdapterDeclaration"] = None, libraryElement_InterfaceList66: set["libraryElement_Event"] = None, libraryElement_InterfaceList69: set["libraryElement_Event"] = None, libraryElement_InterfaceList72: set["libraryElement_VarDeclaration"] = None, libraryElement_InterfaceList75: set["libraryElement_VarDeclaration"] = None, libraryElement_InterfaceList63: set["libraryElement_AdapterDeclaration"] = None):
        self.libraryElement_InterfaceList = libraryElement_InterfaceList
        self.libraryElement_InterfaceList56 = libraryElement_InterfaceList56
        self.libraryElement_InterfaceList60 = libraryElement_InterfaceList60 if libraryElement_InterfaceList60 is not None else set()
        self.libraryElement_InterfaceList66 = libraryElement_InterfaceList66 if libraryElement_InterfaceList66 is not None else set()
        self.libraryElement_InterfaceList69 = libraryElement_InterfaceList69 if libraryElement_InterfaceList69 is not None else set()
        self.libraryElement_InterfaceList72 = libraryElement_InterfaceList72 if libraryElement_InterfaceList72 is not None else set()
        self.libraryElement_InterfaceList75 = libraryElement_InterfaceList75 if libraryElement_InterfaceList75 is not None else set()
        self.libraryElement_InterfaceList63 = libraryElement_InterfaceList63 if libraryElement_InterfaceList63 is not None else set()
        
    @property
    def libraryElement_InterfaceList72(self):
        return self.__libraryElement_InterfaceList72

    @libraryElement_InterfaceList72.setter
    def libraryElement_InterfaceList72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList72", None)
        self.__libraryElement_InterfaceList72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_VarDeclaration73"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration73", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_VarDeclaration73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_VarDeclaration73"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration73", None)
                    
                    setattr(item, "libraryElement_VarDeclaration73", self)
                    

    @property
    def libraryElement_InterfaceList66(self):
        return self.__libraryElement_InterfaceList66

    @libraryElement_InterfaceList66.setter
    def libraryElement_InterfaceList66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList66", None)
        self.__libraryElement_InterfaceList66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Event67"):
                    opp_val = getattr(item, "libraryElement_Event67", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Event67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Event67"):
                    opp_val = getattr(item, "libraryElement_Event67", None)
                    
                    setattr(item, "libraryElement_Event67", self)
                    

    @property
    def libraryElement_InterfaceList75(self):
        return self.__libraryElement_InterfaceList75

    @libraryElement_InterfaceList75.setter
    def libraryElement_InterfaceList75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList75", None)
        self.__libraryElement_InterfaceList75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_VarDeclaration76"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration76", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_VarDeclaration76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_VarDeclaration76"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration76", None)
                    
                    setattr(item, "libraryElement_VarDeclaration76", self)
                    

    @property
    def libraryElement_InterfaceList(self):
        return self.__libraryElement_InterfaceList

    @libraryElement_InterfaceList.setter
    def libraryElement_InterfaceList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList", None)
        self.__libraryElement_InterfaceList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetworkElement"):
                opp_val = getattr(old_value, "libraryElement_FBNetworkElement", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetworkElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetworkElement"):
                opp_val = getattr(value, "libraryElement_FBNetworkElement", None)
                setattr(value, "libraryElement_FBNetworkElement", self)

    @property
    def libraryElement_InterfaceList56(self):
        return self.__libraryElement_InterfaceList56

    @libraryElement_InterfaceList56.setter
    def libraryElement_InterfaceList56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList56", None)
        self.__libraryElement_InterfaceList56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBType"):
                opp_val = getattr(old_value, "libraryElement_FBType", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBType"):
                opp_val = getattr(value, "libraryElement_FBType", None)
                setattr(value, "libraryElement_FBType", self)

    @property
    def libraryElement_InterfaceList60(self):
        return self.__libraryElement_InterfaceList60

    @libraryElement_InterfaceList60.setter
    def libraryElement_InterfaceList60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList60", None)
        self.__libraryElement_InterfaceList60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_AdapterDeclaration61"):
                    opp_val = getattr(item, "libraryElement_AdapterDeclaration61", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_AdapterDeclaration61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_AdapterDeclaration61"):
                    opp_val = getattr(item, "libraryElement_AdapterDeclaration61", None)
                    
                    setattr(item, "libraryElement_AdapterDeclaration61", self)
                    

    @property
    def libraryElement_InterfaceList63(self):
        return self.__libraryElement_InterfaceList63

    @libraryElement_InterfaceList63.setter
    def libraryElement_InterfaceList63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList63", None)
        self.__libraryElement_InterfaceList63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_AdapterDeclaration64"):
                    opp_val = getattr(item, "libraryElement_AdapterDeclaration64", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_AdapterDeclaration64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_AdapterDeclaration64"):
                    opp_val = getattr(item, "libraryElement_AdapterDeclaration64", None)
                    
                    setattr(item, "libraryElement_AdapterDeclaration64", self)
                    

    @property
    def libraryElement_InterfaceList69(self):
        return self.__libraryElement_InterfaceList69

    @libraryElement_InterfaceList69.setter
    def libraryElement_InterfaceList69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_InterfaceList__libraryElement_InterfaceList69", None)
        self.__libraryElement_InterfaceList69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Event70"):
                    opp_val = getattr(item, "libraryElement_Event70", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Event70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Event70"):
                    opp_val = getattr(item, "libraryElement_Event70", None)
                    
                    setattr(item, "libraryElement_Event70", self)
                    

    def getAllInterfaceElements(self):
        # TODO: Implement getAllInterfaceElements method
        pass

    def getInterfaceElement(self, name: str) -> IInterfaceElement:
        # TODO: Implement getInterfaceElement method
        pass

    def getVariable(self, name: str) -> VarDeclaration:
        # TODO: Implement getVariable method
        pass

    def getFBNetworkElement(self) -> FBNetworkElement:
        # TODO: Implement getFBNetworkElement method
        pass

    def getEvent(self, name: str) -> str:
        # TODO: Implement getEvent method
        pass

class FBNetworkElement:

    pass
class libraryElement_SubApp(FBNetworkElement):

    def __init__(self, libraryElement_SubApp: "libraryElement_FBNetwork" = None):
        self.libraryElement_SubApp = libraryElement_SubApp
        
    @property
    def libraryElement_SubApp(self):
        return self.__libraryElement_SubApp

    @libraryElement_SubApp.setter
    def libraryElement_SubApp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_SubApp__libraryElement_SubApp", None)
        self.__libraryElement_SubApp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork54"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork54", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetwork54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork54"):
                opp_val = getattr(value, "libraryElement_FBNetwork54", None)
                setattr(value, "libraryElement_FBNetwork54", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class libraryElement_FB(FBNetworkElement):

    def __init__(self):
        
    def getType(self) -> FBType:
        # TODO: Implement getType method
        pass

    def isResourceTypeFB(self) -> bool:
        # TODO: Implement isResourceTypeFB method
        pass

    def isResourceFB(self) -> bool:
        # TODO: Implement isResourceFB method
        pass

class libraryElement_With:

    pass
class IInterfaceElement:

    pass
class libraryElement_Event(IInterfaceElement):

    pass
class libraryElement_ECAction:

    pass
class libraryElement_ResourceTypeName:

    def __init__(self, name: str, libraryElement_ResourceTypeName: "libraryElement_DeviceType" = None):
        self.name = name
        self.libraryElement_ResourceTypeName = libraryElement_ResourceTypeName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryElement_ResourceTypeName(self):
        return self.__libraryElement_ResourceTypeName

    @libraryElement_ResourceTypeName.setter
    def libraryElement_ResourceTypeName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ResourceTypeName__libraryElement_ResourceTypeName", None)
        self.__libraryElement_ResourceTypeName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_DeviceType19"):
                opp_val = getattr(old_value, "libraryElement_DeviceType19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_DeviceType19"):
                opp_val = getattr(value, "libraryElement_DeviceType19", None)
                if opp_val is None:
                    setattr(value, "libraryElement_DeviceType19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompilableType:

    pass
class libraryElement_ResourceType(CompilableType):

    pass
class libraryElement_SegmentType(CompilableType):

    pass
class libraryElement_FBType(CompilableType):

    pass
class libraryElement_DeviceType(CompilableType):

    def __init__(self, profile: str, libraryElement_DeviceType: set["libraryElement_VarDeclaration"] = None, libraryElement_DeviceType19: set["libraryElement_ResourceTypeName"] = None, libraryElement_DeviceType21: set["libraryElement_Resource"] = None, libraryElement_DeviceType23: "libraryElement_FBNetwork" = None):
        self.profile = profile
        self.libraryElement_DeviceType = libraryElement_DeviceType if libraryElement_DeviceType is not None else set()
        self.libraryElement_DeviceType19 = libraryElement_DeviceType19 if libraryElement_DeviceType19 is not None else set()
        self.libraryElement_DeviceType21 = libraryElement_DeviceType21 if libraryElement_DeviceType21 is not None else set()
        self.libraryElement_DeviceType23 = libraryElement_DeviceType23
        
    @property
    def profile(self) -> str:
        return self.__profile

    @profile.setter
    def profile(self, profile: str):
        self.__profile = profile

    @property
    def libraryElement_DeviceType(self):
        return self.__libraryElement_DeviceType

    @libraryElement_DeviceType.setter
    def libraryElement_DeviceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_DeviceType__libraryElement_DeviceType", None)
        self.__libraryElement_DeviceType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_VarDeclaration17"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration17", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_VarDeclaration17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_VarDeclaration17"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration17", None)
                    
                    setattr(item, "libraryElement_VarDeclaration17", self)
                    

    @property
    def libraryElement_DeviceType21(self):
        return self.__libraryElement_DeviceType21

    @libraryElement_DeviceType21.setter
    def libraryElement_DeviceType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_DeviceType__libraryElement_DeviceType21", None)
        self.__libraryElement_DeviceType21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Resource"):
                    opp_val = getattr(item, "libraryElement_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Resource"):
                    opp_val = getattr(item, "libraryElement_Resource", None)
                    
                    setattr(item, "libraryElement_Resource", self)
                    

    @property
    def libraryElement_DeviceType19(self):
        return self.__libraryElement_DeviceType19

    @libraryElement_DeviceType19.setter
    def libraryElement_DeviceType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_DeviceType__libraryElement_DeviceType19", None)
        self.__libraryElement_DeviceType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_ResourceTypeName"):
                    opp_val = getattr(item, "libraryElement_ResourceTypeName", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_ResourceTypeName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_ResourceTypeName"):
                    opp_val = getattr(item, "libraryElement_ResourceTypeName", None)
                    
                    setattr(item, "libraryElement_ResourceTypeName", self)
                    

    @property
    def libraryElement_DeviceType23(self):
        return self.__libraryElement_DeviceType23

    @libraryElement_DeviceType23.setter
    def libraryElement_DeviceType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_DeviceType__libraryElement_DeviceType23", None)
        self.__libraryElement_DeviceType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork24"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork24", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetwork24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork24"):
                opp_val = getattr(value, "libraryElement_FBNetwork24", None)
                setattr(value, "libraryElement_FBNetwork24", self)

class IVarElement:

    pass
class ColorizableElement:

    pass
class PositionableElement:

    pass
class libraryElement_ECTransition(PositionableElement):

    def __init__(self, comment: str, conditionExpression: str, libraryElement_ECTransition: "libraryElement_ECC" = None, outTransitions: "libraryElement_ECState" = None, inTransitions: "libraryElement_ECState" = None, libraryElement_ECTransition46: "libraryElement_Event" = None, ECTransition: "libraryElement_ECState" = None, ECTransition41: "libraryElement_ECState" = None):
        self.comment = comment
        self.conditionExpression = conditionExpression
        self.libraryElement_ECTransition = libraryElement_ECTransition
        self.outTransitions = outTransitions
        self.inTransitions = inTransitions
        self.libraryElement_ECTransition46 = libraryElement_ECTransition46
        self.ECTransition = ECTransition
        self.ECTransition41 = ECTransition41
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def conditionExpression(self) -> str:
        return self.__conditionExpression

    @conditionExpression.setter
    def conditionExpression(self, conditionExpression: str):
        self.__conditionExpression = conditionExpression

    @property
    def ECTransition(self):
        return self.__ECTransition

    @ECTransition.setter
    def ECTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__ECTransition", None)
        self.__ECTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_ECTransition(self):
        return self.__libraryElement_ECTransition

    @libraryElement_ECTransition.setter
    def libraryElement_ECTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__libraryElement_ECTransition", None)
        self.__libraryElement_ECTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ECC32"):
                opp_val = getattr(old_value, "libraryElement_ECC32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ECC32"):
                opp_val = getattr(value, "libraryElement_ECC32", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ECC32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inTransitions(self):
        return self.__inTransitions

    @inTransitions.setter
    def inTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__inTransitions", None)
        self.__inTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ECState44"):
                opp_val = getattr(old_value, "ECState44", None)
                if opp_val == self:
                    setattr(old_value, "ECState44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ECState44"):
                opp_val = getattr(value, "ECState44", None)
                setattr(value, "ECState44", self)

    @property
    def ECTransition41(self):
        return self.__ECTransition41

    @ECTransition41.setter
    def ECTransition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__ECTransition41", None)
        self.__ECTransition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destination"):
                opp_val = getattr(old_value, "destination", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destination"):
                opp_val = getattr(value, "destination", None)
                if opp_val is None:
                    setattr(value, "destination", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_ECTransition46(self):
        return self.__libraryElement_ECTransition46

    @libraryElement_ECTransition46.setter
    def libraryElement_ECTransition46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__libraryElement_ECTransition46", None)
        self.__libraryElement_ECTransition46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Event47"):
                opp_val = getattr(old_value, "libraryElement_Event47", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Event47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Event47"):
                opp_val = getattr(value, "libraryElement_Event47", None)
                setattr(value, "libraryElement_Event47", self)

    @property
    def outTransitions(self):
        return self.__outTransitions

    @outTransitions.setter
    def outTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECTransition__outTransitions", None)
        self.__outTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ECState"):
                opp_val = getattr(old_value, "ECState", None)
                if opp_val == self:
                    setattr(old_value, "ECState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ECState"):
                opp_val = getattr(value, "ECState", None)
                setattr(value, "ECState", self)

    def getConditionText(self) -> str:
        # TODO: Implement getConditionText method
        pass

class TypedConfigureableObject:

    pass
class libraryElement_Resource(TypedConfigureableObject, IVarElement):

    def __init__(self, x: str, deviceTypeResource: str, y: str, Resource: "libraryElement_Device" = None, libraryElement_Resource: "libraryElement_DeviceType" = None, libraryElement_Resource86: "libraryElement_FBNetwork" = None, resource: "libraryElement_Device" = None):
        self.x = x
        self.deviceTypeResource = deviceTypeResource
        self.y = y
        self.Resource = Resource
        self.libraryElement_Resource = libraryElement_Resource
        self.libraryElement_Resource86 = libraryElement_Resource86
        self.resource = resource
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def deviceTypeResource(self) -> str:
        return self.__deviceTypeResource

    @deviceTypeResource.setter
    def deviceTypeResource(self, deviceTypeResource: str):
        self.__deviceTypeResource = deviceTypeResource

    @property
    def libraryElement_Resource86(self):
        return self.__libraryElement_Resource86

    @libraryElement_Resource86.setter
    def libraryElement_Resource86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Resource__libraryElement_Resource86", None)
        self.__libraryElement_Resource86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork87"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork87", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetwork87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork87"):
                opp_val = getattr(value, "libraryElement_FBNetwork87", None)
                setattr(value, "libraryElement_FBNetwork87", self)

    @property
    def libraryElement_Resource(self):
        return self.__libraryElement_Resource

    @libraryElement_Resource.setter
    def libraryElement_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Resource__libraryElement_Resource", None)
        self.__libraryElement_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_DeviceType21"):
                opp_val = getattr(old_value, "libraryElement_DeviceType21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_DeviceType21"):
                opp_val = getattr(value, "libraryElement_DeviceType21", None)
                if opp_val is None:
                    setattr(value, "libraryElement_DeviceType21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Resource__Resource", None)
        self.__Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "device"):
                opp_val = getattr(old_value, "device", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "device"):
                opp_val = getattr(value, "device", None)
                if opp_val is None:
                    setattr(value, "device", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Resource__resource", None)
        self.__resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Device89"):
                opp_val = getattr(old_value, "Device89", None)
                if opp_val == self:
                    setattr(old_value, "Device89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Device89"):
                opp_val = getattr(value, "Device89", None)
                setattr(value, "Device89", self)

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

class libraryElement_Segment(TypedConfigureableObject, PositionableElement, ColorizableElement):

    def __init__(self, width: str, Segment: "libraryElement_Link" = None, libraryElement_Segment: set["libraryElement_VarDeclaration"] = None, segment: set["libraryElement_Link"] = None, libraryElement_Segment149: "libraryElement_SystemConfiguration" = None):
        self.width = width
        self.Segment = Segment
        self.libraryElement_Segment = libraryElement_Segment if libraryElement_Segment is not None else set()
        self.segment = segment if segment is not None else set()
        self.libraryElement_Segment149 = libraryElement_Segment149
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def Segment(self):
        return self.__Segment

    @Segment.setter
    def Segment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Segment__Segment", None)
        self.__Segment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outConnections"):
                opp_val = getattr(old_value, "outConnections", None)
                if opp_val == self:
                    setattr(old_value, "outConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outConnections"):
                opp_val = getattr(value, "outConnections", None)
                setattr(value, "outConnections", self)

    @property
    def libraryElement_Segment(self):
        return self.__libraryElement_Segment

    @libraryElement_Segment.setter
    def libraryElement_Segment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Segment__libraryElement_Segment", None)
        self.__libraryElement_Segment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_VarDeclaration99"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration99", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_VarDeclaration99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_VarDeclaration99"):
                    opp_val = getattr(item, "libraryElement_VarDeclaration99", None)
                    
                    setattr(item, "libraryElement_VarDeclaration99", self)
                    

    @property
    def segment(self):
        return self.__segment

    @segment.setter
    def segment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Segment__segment", None)
        self.__segment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link101"):
                    opp_val = getattr(item, "Link101", None)
                    
                    if opp_val == self:
                        setattr(item, "Link101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link101"):
                    opp_val = getattr(item, "Link101", None)
                    
                    setattr(item, "Link101", self)
                    

    @property
    def libraryElement_Segment149(self):
        return self.__libraryElement_Segment149

    @libraryElement_Segment149.setter
    def libraryElement_Segment149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Segment__libraryElement_Segment149", None)
        self.__libraryElement_Segment149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_SystemConfiguration148"):
                opp_val = getattr(old_value, "libraryElement_SystemConfiguration148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_SystemConfiguration148"):
                opp_val = getattr(value, "libraryElement_SystemConfiguration148", None)
                if opp_val is None:
                    setattr(value, "libraryElement_SystemConfiguration148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryElement_FBNetworkElement(TypedConfigureableObject, PositionableElement):

    def __init__(self, libraryElement_FBNetworkElement: "libraryElement_InterfaceList" = None, libraryElement_FBNetworkElement52: "libraryElement_Mapping" = None, libraryElement_FBNetworkElement81: "libraryElement_Mapping" = None, libraryElement_FBNetworkElement84: "libraryElement_Mapping" = None, libraryElement_FBNetworkElement109: "libraryElement_FBNetwork" = None):
        self.libraryElement_FBNetworkElement = libraryElement_FBNetworkElement
        self.libraryElement_FBNetworkElement52 = libraryElement_FBNetworkElement52
        self.libraryElement_FBNetworkElement81 = libraryElement_FBNetworkElement81
        self.libraryElement_FBNetworkElement84 = libraryElement_FBNetworkElement84
        self.libraryElement_FBNetworkElement109 = libraryElement_FBNetworkElement109
        
    @property
    def libraryElement_FBNetworkElement109(self):
        return self.__libraryElement_FBNetworkElement109

    @libraryElement_FBNetworkElement109.setter
    def libraryElement_FBNetworkElement109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetworkElement__libraryElement_FBNetworkElement109", None)
        self.__libraryElement_FBNetworkElement109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork108"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork108"):
                opp_val = getattr(value, "libraryElement_FBNetwork108", None)
                if opp_val is None:
                    setattr(value, "libraryElement_FBNetwork108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_FBNetworkElement52(self):
        return self.__libraryElement_FBNetworkElement52

    @libraryElement_FBNetworkElement52.setter
    def libraryElement_FBNetworkElement52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetworkElement__libraryElement_FBNetworkElement52", None)
        self.__libraryElement_FBNetworkElement52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Mapping"):
                opp_val = getattr(old_value, "libraryElement_Mapping", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Mapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Mapping"):
                opp_val = getattr(value, "libraryElement_Mapping", None)
                setattr(value, "libraryElement_Mapping", self)

    @property
    def libraryElement_FBNetworkElement81(self):
        return self.__libraryElement_FBNetworkElement81

    @libraryElement_FBNetworkElement81.setter
    def libraryElement_FBNetworkElement81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetworkElement__libraryElement_FBNetworkElement81", None)
        self.__libraryElement_FBNetworkElement81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Mapping80"):
                opp_val = getattr(old_value, "libraryElement_Mapping80", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Mapping80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Mapping80"):
                opp_val = getattr(value, "libraryElement_Mapping80", None)
                setattr(value, "libraryElement_Mapping80", self)

    @property
    def libraryElement_FBNetworkElement84(self):
        return self.__libraryElement_FBNetworkElement84

    @libraryElement_FBNetworkElement84.setter
    def libraryElement_FBNetworkElement84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetworkElement__libraryElement_FBNetworkElement84", None)
        self.__libraryElement_FBNetworkElement84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Mapping83"):
                opp_val = getattr(old_value, "libraryElement_Mapping83", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Mapping83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Mapping83"):
                opp_val = getattr(value, "libraryElement_Mapping83", None)
                setattr(value, "libraryElement_Mapping83", self)

    @property
    def libraryElement_FBNetworkElement(self):
        return self.__libraryElement_FBNetworkElement

    @libraryElement_FBNetworkElement.setter
    def libraryElement_FBNetworkElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetworkElement__libraryElement_FBNetworkElement", None)
        self.__libraryElement_FBNetworkElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_InterfaceList"):
                opp_val = getattr(old_value, "libraryElement_InterfaceList", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_InterfaceList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_InterfaceList"):
                opp_val = getattr(value, "libraryElement_InterfaceList", None)
                setattr(value, "libraryElement_InterfaceList", self)

    def checkConnections(self):
        # TODO: Implement checkConnections method
        pass

    def getOpposite(self) -> FBNetworkElement:
        # TODO: Implement getOpposite method
        pass

    def getInterfaceElement(self, name: str) -> IInterfaceElement:
        # TODO: Implement getInterfaceElement method
        pass

    def getResource(self) -> str:
        # TODO: Implement getResource method
        pass

    def isMapped(self) -> bool:
        # TODO: Implement isMapped method
        pass

    def getFbNetwork(self) -> str:
        # TODO: Implement getFbNetwork method
        pass

class libraryElement_Device(TypedConfigureableObject, PositionableElement, ColorizableElement, IVarElement):

    def __init__(self, profile: str, device: set["libraryElement_Resource"] = None, device15: set["libraryElement_Link"] = None, Device: "libraryElement_Link" = None, Device89: "libraryElement_Resource" = None, libraryElement_Device: "libraryElement_SystemConfiguration" = None):
        self.profile = profile
        self.device = device if device is not None else set()
        self.device15 = device15 if device15 is not None else set()
        self.Device = Device
        self.Device89 = Device89
        self.libraryElement_Device = libraryElement_Device
        
    @property
    def profile(self) -> str:
        return self.__profile

    @profile.setter
    def profile(self, profile: str):
        self.__profile = profile

    @property
    def device(self):
        return self.__device

    @device.setter
    def device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Device__device", None)
        self.__device = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    

    @property
    def libraryElement_Device(self):
        return self.__libraryElement_Device

    @libraryElement_Device.setter
    def libraryElement_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Device__libraryElement_Device", None)
        self.__libraryElement_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_SystemConfiguration146"):
                opp_val = getattr(old_value, "libraryElement_SystemConfiguration146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_SystemConfiguration146"):
                opp_val = getattr(value, "libraryElement_SystemConfiguration146", None)
                if opp_val is None:
                    setattr(value, "libraryElement_SystemConfiguration146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def device15(self):
        return self.__device15

    @device15.setter
    def device15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Device__device15", None)
        self.__device15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

    @property
    def Device(self):
        return self.__Device

    @Device.setter
    def Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Device__Device", None)
        self.__Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inConnections"):
                opp_val = getattr(old_value, "inConnections", None)
                if opp_val == self:
                    setattr(old_value, "inConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inConnections"):
                opp_val = getattr(value, "inConnections", None)
                setattr(value, "inConnections", self)

    @property
    def Device89(self):
        return self.__Device89

    @Device89.setter
    def Device89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Device__Device89", None)
        self.__Device89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resource"):
                opp_val = getattr(old_value, "resource", None)
                if opp_val == self:
                    setattr(old_value, "resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resource"):
                opp_val = getattr(value, "resource", None)
                setattr(value, "resource", self)

    def getSystemConfiguration(self) -> str:
        # TODO: Implement getSystemConfiguration method
        pass

    def getResourceNamed(self, name: str) -> str:
        # TODO: Implement getResourceNamed method
        pass

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class ConfigurableObject:

    pass
class libraryElement_Link(ConfigurableObject):

    pass
class libraryElement_TypedConfigureableObject(ConfigurableObject):

    def __init__(self, libraryElement_TypedConfigureableObject: "libraryElement_PaletteEntry" = None):
        self.libraryElement_TypedConfigureableObject = libraryElement_TypedConfigureableObject
        
    @property
    def libraryElement_TypedConfigureableObject(self):
        return self.__libraryElement_TypedConfigureableObject

    @libraryElement_TypedConfigureableObject.setter
    def libraryElement_TypedConfigureableObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_TypedConfigureableObject__libraryElement_TypedConfigureableObject", None)
        self.__libraryElement_TypedConfigureableObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_PaletteEntry"):
                opp_val = getattr(old_value, "libraryElement_PaletteEntry", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_PaletteEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_PaletteEntry"):
                opp_val = getattr(value, "libraryElement_PaletteEntry", None)
                setattr(value, "libraryElement_PaletteEntry", self)

    def getType(self) -> LibraryElement:
        # TODO: Implement getType method
        pass

    def getTypeName(self) -> str:
        # TODO: Implement getTypeName method
        pass

class libraryElement_Connection(ConfigurableObject):

    def __init__(self, dx1: str, dx2: str, dy: str, resTypeConnection: str, brokenConnection: str, inputConnections: "libraryElement_IInterfaceElement" = None, outputConnections: "libraryElement_IInterfaceElement" = None, Connection: "libraryElement_IInterfaceElement" = None, Connection141: "libraryElement_IInterfaceElement" = None):
        self.dx1 = dx1
        self.dx2 = dx2
        self.dy = dy
        self.resTypeConnection = resTypeConnection
        self.brokenConnection = brokenConnection
        self.inputConnections = inputConnections
        self.outputConnections = outputConnections
        self.Connection = Connection
        self.Connection141 = Connection141
        
    @property
    def brokenConnection(self) -> str:
        return self.__brokenConnection

    @brokenConnection.setter
    def brokenConnection(self, brokenConnection: str):
        self.__brokenConnection = brokenConnection

    @property
    def dx1(self) -> str:
        return self.__dx1

    @dx1.setter
    def dx1(self, dx1: str):
        self.__dx1 = dx1

    @property
    def resTypeConnection(self) -> str:
        return self.__resTypeConnection

    @resTypeConnection.setter
    def resTypeConnection(self, resTypeConnection: str):
        self.__resTypeConnection = resTypeConnection

    @property
    def dx2(self) -> str:
        return self.__dx2

    @dx2.setter
    def dx2(self, dx2: str):
        self.__dx2 = dx2

    @property
    def dy(self) -> str:
        return self.__dy

    @dy.setter
    def dy(self, dy: str):
        self.__dy = dy

    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Connection__Connection", None)
        self.__Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destination138"):
                opp_val = getattr(old_value, "destination138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destination138"):
                opp_val = getattr(value, "destination138", None)
                if opp_val is None:
                    setattr(value, "destination138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputConnections(self):
        return self.__inputConnections

    @inputConnections.setter
    def inputConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Connection__inputConnections", None)
        self.__inputConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IInterfaceElement12"):
                opp_val = getattr(old_value, "IInterfaceElement12", None)
                if opp_val == self:
                    setattr(old_value, "IInterfaceElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IInterfaceElement12"):
                opp_val = getattr(value, "IInterfaceElement12", None)
                setattr(value, "IInterfaceElement12", self)

    @property
    def outputConnections(self):
        return self.__outputConnections

    @outputConnections.setter
    def outputConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Connection__outputConnections", None)
        self.__outputConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IInterfaceElement"):
                opp_val = getattr(old_value, "IInterfaceElement", None)
                if opp_val == self:
                    setattr(old_value, "IInterfaceElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IInterfaceElement"):
                opp_val = getattr(value, "IInterfaceElement", None)
                setattr(value, "IInterfaceElement", self)

    @property
    def Connection141(self):
        return self.__Connection141

    @Connection141.setter
    def Connection141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Connection__Connection141", None)
        self.__Connection141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source140"):
                opp_val = getattr(old_value, "source140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source140"):
                opp_val = getattr(value, "source140", None)
                if opp_val is None:
                    setattr(value, "source140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getDestinationElement(self) -> str:
        # TODO: Implement getDestinationElement method
        pass

    def getFBNetwork(self) -> str:
        # TODO: Implement getFBNetwork method
        pass

    def isResourceConnection(self) -> bool:
        # TODO: Implement isResourceConnection method
        pass

    def getSourceElement(self) -> str:
        # TODO: Implement getSourceElement method
        pass

    def checkIfConnectionBroken(self):
        # TODO: Implement checkIfConnectionBroken method
        pass

class libraryElement_ECC:

    pass
class libraryElement_Compiler:

    def __init__(self, version: str, language: str, product: str, vendor: str, libraryElement_Compiler: "libraryElement_CompilerInfo" = None):
        self.version = version
        self.language = language
        self.product = product
        self.vendor = vendor
        self.libraryElement_Compiler = libraryElement_Compiler
        
    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def product(self) -> str:
        return self.__product

    @product.setter
    def product(self, product: str):
        self.__product = product

    @property
    def libraryElement_Compiler(self):
        return self.__libraryElement_Compiler

    @libraryElement_Compiler.setter
    def libraryElement_Compiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Compiler__libraryElement_Compiler", None)
        self.__libraryElement_Compiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_CompilerInfo"):
                opp_val = getattr(old_value, "libraryElement_CompilerInfo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_CompilerInfo"):
                opp_val = getattr(value, "libraryElement_CompilerInfo", None)
                if opp_val is None:
                    setattr(value, "libraryElement_CompilerInfo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryElement_CompilerInfo:

    def __init__(self, classdef: str, header: str, libraryElement_CompilerInfo: set["libraryElement_Compiler"] = None, libraryElement_CompilerInfo133: "libraryElement_CompilableType" = None):
        self.classdef = classdef
        self.header = header
        self.libraryElement_CompilerInfo = libraryElement_CompilerInfo if libraryElement_CompilerInfo is not None else set()
        self.libraryElement_CompilerInfo133 = libraryElement_CompilerInfo133
        
    @property
    def classdef(self) -> str:
        return self.__classdef

    @classdef.setter
    def classdef(self, classdef: str):
        self.__classdef = classdef

    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

    @property
    def libraryElement_CompilerInfo133(self):
        return self.__libraryElement_CompilerInfo133

    @libraryElement_CompilerInfo133.setter
    def libraryElement_CompilerInfo133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_CompilerInfo__libraryElement_CompilerInfo133", None)
        self.__libraryElement_CompilerInfo133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_CompilableType"):
                opp_val = getattr(old_value, "libraryElement_CompilableType", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_CompilableType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_CompilableType"):
                opp_val = getattr(value, "libraryElement_CompilableType", None)
                setattr(value, "libraryElement_CompilableType", self)

    @property
    def libraryElement_CompilerInfo(self):
        return self.__libraryElement_CompilerInfo

    @libraryElement_CompilerInfo.setter
    def libraryElement_CompilerInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_CompilerInfo__libraryElement_CompilerInfo", None)
        self.__libraryElement_CompilerInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Compiler"):
                    opp_val = getattr(item, "libraryElement_Compiler", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Compiler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Compiler"):
                    opp_val = getattr(item, "libraryElement_Compiler", None)
                    
                    setattr(item, "libraryElement_Compiler", self)
                    

class libraryElement_VarDeclaration(IInterfaceElement):

    def __init__(self, arraySize: str, libraryElement_VarDeclaration: "libraryElement_BasicFBType" = None, libraryElement_VarDeclaration17: "libraryElement_DeviceType" = None, libraryElement_VarDeclaration73: "libraryElement_InterfaceList" = None, libraryElement_VarDeclaration76: "libraryElement_InterfaceList" = None, libraryElement_VarDeclaration91: "libraryElement_ResourceType" = None, libraryElement_VarDeclaration99: "libraryElement_Segment" = None, libraryElement_VarDeclaration125: "libraryElement_VarInitialization" = None, variables: set["libraryElement_With"] = None, VarDeclaration: "libraryElement_With" = None, libraryElement_VarDeclaration154: "libraryElement_SegmentType" = None, libraryElement_VarDeclaration174: "libraryElement_IVarElement" = None):
        self.arraySize = arraySize
        self.libraryElement_VarDeclaration = libraryElement_VarDeclaration
        self.libraryElement_VarDeclaration17 = libraryElement_VarDeclaration17
        self.libraryElement_VarDeclaration73 = libraryElement_VarDeclaration73
        self.libraryElement_VarDeclaration76 = libraryElement_VarDeclaration76
        self.libraryElement_VarDeclaration91 = libraryElement_VarDeclaration91
        self.libraryElement_VarDeclaration99 = libraryElement_VarDeclaration99
        self.libraryElement_VarDeclaration125 = libraryElement_VarDeclaration125
        self.variables = variables if variables is not None else set()
        self.VarDeclaration = VarDeclaration
        self.libraryElement_VarDeclaration154 = libraryElement_VarDeclaration154
        self.libraryElement_VarDeclaration174 = libraryElement_VarDeclaration174
        
    @property
    def arraySize(self) -> str:
        return self.__arraySize

    @arraySize.setter
    def arraySize(self, arraySize: str):
        self.__arraySize = arraySize

    @property
    def libraryElement_VarDeclaration125(self):
        return self.__libraryElement_VarDeclaration125

    @libraryElement_VarDeclaration125.setter
    def libraryElement_VarDeclaration125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration125", None)
        self.__libraryElement_VarDeclaration125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_VarInitialization"):
                opp_val = getattr(old_value, "libraryElement_VarInitialization", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_VarInitialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_VarInitialization"):
                opp_val = getattr(value, "libraryElement_VarInitialization", None)
                setattr(value, "libraryElement_VarInitialization", self)

    @property
    def libraryElement_VarDeclaration99(self):
        return self.__libraryElement_VarDeclaration99

    @libraryElement_VarDeclaration99.setter
    def libraryElement_VarDeclaration99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration99", None)
        self.__libraryElement_VarDeclaration99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Segment"):
                opp_val = getattr(old_value, "libraryElement_Segment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Segment"):
                opp_val = getattr(value, "libraryElement_Segment", None)
                if opp_val is None:
                    setattr(value, "libraryElement_Segment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration174(self):
        return self.__libraryElement_VarDeclaration174

    @libraryElement_VarDeclaration174.setter
    def libraryElement_VarDeclaration174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration174", None)
        self.__libraryElement_VarDeclaration174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_IVarElement"):
                opp_val = getattr(old_value, "libraryElement_IVarElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_IVarElement"):
                opp_val = getattr(value, "libraryElement_IVarElement", None)
                if opp_val is None:
                    setattr(value, "libraryElement_IVarElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration(self):
        return self.__libraryElement_VarDeclaration

    @libraryElement_VarDeclaration.setter
    def libraryElement_VarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration", None)
        self.__libraryElement_VarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_BasicFBType8"):
                opp_val = getattr(old_value, "libraryElement_BasicFBType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_BasicFBType8"):
                opp_val = getattr(value, "libraryElement_BasicFBType8", None)
                if opp_val is None:
                    setattr(value, "libraryElement_BasicFBType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration154(self):
        return self.__libraryElement_VarDeclaration154

    @libraryElement_VarDeclaration154.setter
    def libraryElement_VarDeclaration154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration154", None)
        self.__libraryElement_VarDeclaration154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_SegmentType"):
                opp_val = getattr(old_value, "libraryElement_SegmentType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_SegmentType"):
                opp_val = getattr(value, "libraryElement_SegmentType", None)
                if opp_val is None:
                    setattr(value, "libraryElement_SegmentType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VarDeclaration(self):
        return self.__VarDeclaration

    @VarDeclaration.setter
    def VarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__VarDeclaration", None)
        self.__VarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "withs"):
                opp_val = getattr(old_value, "withs", None)
                if opp_val == self:
                    setattr(old_value, "withs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "withs"):
                opp_val = getattr(value, "withs", None)
                setattr(value, "withs", self)

    @property
    def libraryElement_VarDeclaration91(self):
        return self.__libraryElement_VarDeclaration91

    @libraryElement_VarDeclaration91.setter
    def libraryElement_VarDeclaration91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration91", None)
        self.__libraryElement_VarDeclaration91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ResourceType"):
                opp_val = getattr(old_value, "libraryElement_ResourceType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ResourceType"):
                opp_val = getattr(value, "libraryElement_ResourceType", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ResourceType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration76(self):
        return self.__libraryElement_VarDeclaration76

    @libraryElement_VarDeclaration76.setter
    def libraryElement_VarDeclaration76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration76", None)
        self.__libraryElement_VarDeclaration76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_InterfaceList75"):
                opp_val = getattr(old_value, "libraryElement_InterfaceList75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_InterfaceList75"):
                opp_val = getattr(value, "libraryElement_InterfaceList75", None)
                if opp_val is None:
                    setattr(value, "libraryElement_InterfaceList75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration17(self):
        return self.__libraryElement_VarDeclaration17

    @libraryElement_VarDeclaration17.setter
    def libraryElement_VarDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration17", None)
        self.__libraryElement_VarDeclaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_DeviceType"):
                opp_val = getattr(old_value, "libraryElement_DeviceType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_DeviceType"):
                opp_val = getattr(value, "libraryElement_DeviceType", None)
                if opp_val is None:
                    setattr(value, "libraryElement_DeviceType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_VarDeclaration73(self):
        return self.__libraryElement_VarDeclaration73

    @libraryElement_VarDeclaration73.setter
    def libraryElement_VarDeclaration73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__libraryElement_VarDeclaration73", None)
        self.__libraryElement_VarDeclaration73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_InterfaceList72"):
                opp_val = getattr(old_value, "libraryElement_InterfaceList72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_InterfaceList72"):
                opp_val = getattr(value, "libraryElement_InterfaceList72", None)
                if opp_val is None:
                    setattr(value, "libraryElement_InterfaceList72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_VarDeclaration__variables", None)
        self.__variables = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "With"):
                    opp_val = getattr(item, "With", None)
                    
                    if opp_val == self:
                        setattr(item, "With", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "With"):
                    opp_val = getattr(item, "With", None)
                    
                    setattr(item, "With", self)
                    

    def isArray(self) -> str:
        # TODO: Implement isArray method
        pass

class DataType:

    pass
class libraryElement_AdapterType(DataType):

    def __init__(self, libraryElement_AdapterType: "libraryElement_AdapterFBType" = None, libraryElement_AdapterType157: "libraryElement_AdapterFBType" = None):
        self.libraryElement_AdapterType = libraryElement_AdapterType
        self.libraryElement_AdapterType157 = libraryElement_AdapterType157
        
    @property
    def libraryElement_AdapterType157(self):
        return self.__libraryElement_AdapterType157

    @libraryElement_AdapterType157.setter
    def libraryElement_AdapterType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AdapterType__libraryElement_AdapterType157", None)
        self.__libraryElement_AdapterType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_AdapterFBType156"):
                opp_val = getattr(old_value, "libraryElement_AdapterFBType156", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_AdapterFBType156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_AdapterFBType156"):
                opp_val = getattr(value, "libraryElement_AdapterFBType156", None)
                setattr(value, "libraryElement_AdapterFBType156", self)

    @property
    def libraryElement_AdapterType(self):
        return self.__libraryElement_AdapterType

    @libraryElement_AdapterType.setter
    def libraryElement_AdapterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AdapterType__libraryElement_AdapterType", None)
        self.__libraryElement_AdapterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_AdapterFBType"):
                opp_val = getattr(old_value, "libraryElement_AdapterFBType", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_AdapterFBType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_AdapterFBType"):
                opp_val = getattr(value, "libraryElement_AdapterFBType", None)
                setattr(value, "libraryElement_AdapterFBType", self)

    def getSocketType(self) -> str:
        # TODO: Implement getSocketType method
        pass

    def getPlugType(self) -> str:
        # TODO: Implement getPlugType method
        pass

    def getInterfaceList(self) -> str:
        # TODO: Implement getInterfaceList method
        pass

class libraryElement_AdapterTypePaletteEntry:

    pass
class FBType:

    pass
class libraryElement_ServiceInterfaceFBType(FBType):

    pass
class libraryElement_CompositeFBType(FBType):

    pass
class libraryElement_BasicFBType(FBType):

    pass
class libraryElement_FBNetwork:

    def __init__(self, libraryElement_FBNetwork: "libraryElement_Application" = None, libraryElement_FBNetwork24: "libraryElement_DeviceType" = None, libraryElement_FBNetwork54: "libraryElement_SubApp" = None, libraryElement_FBNetwork87: "libraryElement_Resource" = None, libraryElement_FBNetwork94: "libraryElement_ResourceType" = None, libraryElement_FBNetwork108: set["libraryElement_FBNetworkElement"] = None, libraryElement_FBNetwork115: set["libraryElement_AdapterConnection"] = None, libraryElement_FBNetwork111: set["libraryElement_DataConnection"] = None, libraryElement_FBNetwork113: set["libraryElement_EventConnection"] = None, libraryElement_FBNetwork136: "libraryElement_CompositeFBType" = None):
        self.libraryElement_FBNetwork = libraryElement_FBNetwork
        self.libraryElement_FBNetwork24 = libraryElement_FBNetwork24
        self.libraryElement_FBNetwork54 = libraryElement_FBNetwork54
        self.libraryElement_FBNetwork87 = libraryElement_FBNetwork87
        self.libraryElement_FBNetwork94 = libraryElement_FBNetwork94
        self.libraryElement_FBNetwork108 = libraryElement_FBNetwork108 if libraryElement_FBNetwork108 is not None else set()
        self.libraryElement_FBNetwork115 = libraryElement_FBNetwork115 if libraryElement_FBNetwork115 is not None else set()
        self.libraryElement_FBNetwork111 = libraryElement_FBNetwork111 if libraryElement_FBNetwork111 is not None else set()
        self.libraryElement_FBNetwork113 = libraryElement_FBNetwork113 if libraryElement_FBNetwork113 is not None else set()
        self.libraryElement_FBNetwork136 = libraryElement_FBNetwork136
        
    @property
    def libraryElement_FBNetwork108(self):
        return self.__libraryElement_FBNetwork108

    @libraryElement_FBNetwork108.setter
    def libraryElement_FBNetwork108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork108", None)
        self.__libraryElement_FBNetwork108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_FBNetworkElement109"):
                    opp_val = getattr(item, "libraryElement_FBNetworkElement109", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_FBNetworkElement109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_FBNetworkElement109"):
                    opp_val = getattr(item, "libraryElement_FBNetworkElement109", None)
                    
                    setattr(item, "libraryElement_FBNetworkElement109", self)
                    

    @property
    def libraryElement_FBNetwork87(self):
        return self.__libraryElement_FBNetwork87

    @libraryElement_FBNetwork87.setter
    def libraryElement_FBNetwork87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork87", None)
        self.__libraryElement_FBNetwork87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Resource86"):
                opp_val = getattr(old_value, "libraryElement_Resource86", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Resource86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Resource86"):
                opp_val = getattr(value, "libraryElement_Resource86", None)
                setattr(value, "libraryElement_Resource86", self)

    @property
    def libraryElement_FBNetwork115(self):
        return self.__libraryElement_FBNetwork115

    @libraryElement_FBNetwork115.setter
    def libraryElement_FBNetwork115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork115", None)
        self.__libraryElement_FBNetwork115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_AdapterConnection"):
                    opp_val = getattr(item, "libraryElement_AdapterConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_AdapterConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_AdapterConnection"):
                    opp_val = getattr(item, "libraryElement_AdapterConnection", None)
                    
                    setattr(item, "libraryElement_AdapterConnection", self)
                    

    @property
    def libraryElement_FBNetwork94(self):
        return self.__libraryElement_FBNetwork94

    @libraryElement_FBNetwork94.setter
    def libraryElement_FBNetwork94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork94", None)
        self.__libraryElement_FBNetwork94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ResourceType93"):
                opp_val = getattr(old_value, "libraryElement_ResourceType93", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_ResourceType93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ResourceType93"):
                opp_val = getattr(value, "libraryElement_ResourceType93", None)
                setattr(value, "libraryElement_ResourceType93", self)

    @property
    def libraryElement_FBNetwork136(self):
        return self.__libraryElement_FBNetwork136

    @libraryElement_FBNetwork136.setter
    def libraryElement_FBNetwork136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork136", None)
        self.__libraryElement_FBNetwork136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_CompositeFBType"):
                opp_val = getattr(old_value, "libraryElement_CompositeFBType", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_CompositeFBType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_CompositeFBType"):
                opp_val = getattr(value, "libraryElement_CompositeFBType", None)
                setattr(value, "libraryElement_CompositeFBType", self)

    @property
    def libraryElement_FBNetwork111(self):
        return self.__libraryElement_FBNetwork111

    @libraryElement_FBNetwork111.setter
    def libraryElement_FBNetwork111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork111", None)
        self.__libraryElement_FBNetwork111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_DataConnection"):
                    opp_val = getattr(item, "libraryElement_DataConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_DataConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_DataConnection"):
                    opp_val = getattr(item, "libraryElement_DataConnection", None)
                    
                    setattr(item, "libraryElement_DataConnection", self)
                    

    @property
    def libraryElement_FBNetwork113(self):
        return self.__libraryElement_FBNetwork113

    @libraryElement_FBNetwork113.setter
    def libraryElement_FBNetwork113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork113", None)
        self.__libraryElement_FBNetwork113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_EventConnection"):
                    opp_val = getattr(item, "libraryElement_EventConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_EventConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_EventConnection"):
                    opp_val = getattr(item, "libraryElement_EventConnection", None)
                    
                    setattr(item, "libraryElement_EventConnection", self)
                    

    @property
    def libraryElement_FBNetwork54(self):
        return self.__libraryElement_FBNetwork54

    @libraryElement_FBNetwork54.setter
    def libraryElement_FBNetwork54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork54", None)
        self.__libraryElement_FBNetwork54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_SubApp"):
                opp_val = getattr(old_value, "libraryElement_SubApp", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_SubApp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_SubApp"):
                opp_val = getattr(value, "libraryElement_SubApp", None)
                setattr(value, "libraryElement_SubApp", self)

    @property
    def libraryElement_FBNetwork24(self):
        return self.__libraryElement_FBNetwork24

    @libraryElement_FBNetwork24.setter
    def libraryElement_FBNetwork24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork24", None)
        self.__libraryElement_FBNetwork24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_DeviceType23"):
                opp_val = getattr(old_value, "libraryElement_DeviceType23", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_DeviceType23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_DeviceType23"):
                opp_val = getattr(value, "libraryElement_DeviceType23", None)
                setattr(value, "libraryElement_DeviceType23", self)

    @property
    def libraryElement_FBNetwork(self):
        return self.__libraryElement_FBNetwork

    @libraryElement_FBNetwork.setter
    def libraryElement_FBNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_FBNetwork__libraryElement_FBNetwork", None)
        self.__libraryElement_FBNetwork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Application"):
                opp_val = getattr(old_value, "libraryElement_Application", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Application"):
                opp_val = getattr(value, "libraryElement_Application", None)
                setattr(value, "libraryElement_Application", self)

    def getSubAppNamed(self, name: str) -> str:
        # TODO: Implement getSubAppNamed method
        pass

    def getFBNamed(self, name: str) -> str:
        # TODO: Implement getFBNamed method
        pass

    def isSubApplicationNetwork(self) -> str:
        # TODO: Implement isSubApplicationNetwork method
        pass

    def addConnection(self, connection: str):
        # TODO: Implement addConnection method
        pass

    def removeConnection(self, connection: str):
        # TODO: Implement removeConnection method
        pass

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

    def getElementNamed(self, name: str) -> FBNetworkElement:
        # TODO: Implement getElementNamed method
        pass

    def isResourceNetwork(self) -> str:
        # TODO: Implement isResourceNetwork method
        pass

    def isCFBTypeNetwork(self) -> str:
        # TODO: Implement isCFBTypeNetwork method
        pass

    def getApplication(self) -> str:
        # TODO: Implement getApplication method
        pass

    def isApplicationNetwork(self) -> str:
        # TODO: Implement isApplicationNetwork method
        pass

class INamedElement:

    pass
class libraryElement_ServiceInterface(INamedElement):

    pass
class libraryElement_LibraryElement(INamedElement):

    pass
class libraryElement_Application(INamedElement):

    def __init__(self, libraryElement_Application: "libraryElement_FBNetwork" = None, libraryElement_Application117: "libraryElement_AutomationSystem" = None):
        self.libraryElement_Application = libraryElement_Application
        self.libraryElement_Application117 = libraryElement_Application117
        
    @property
    def libraryElement_Application(self):
        return self.__libraryElement_Application

    @libraryElement_Application.setter
    def libraryElement_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Application__libraryElement_Application", None)
        self.__libraryElement_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_FBNetwork"):
                opp_val = getattr(old_value, "libraryElement_FBNetwork", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_FBNetwork", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_FBNetwork"):
                opp_val = getattr(value, "libraryElement_FBNetwork", None)
                setattr(value, "libraryElement_FBNetwork", self)

    @property
    def libraryElement_Application117(self):
        return self.__libraryElement_Application117

    @libraryElement_Application117.setter
    def libraryElement_Application117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_Application__libraryElement_Application117", None)
        self.__libraryElement_Application117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_AutomationSystem"):
                opp_val = getattr(old_value, "libraryElement_AutomationSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_AutomationSystem"):
                opp_val = getattr(value, "libraryElement_AutomationSystem", None)
                if opp_val is None:
                    setattr(value, "libraryElement_AutomationSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getAutomationSystem(self) -> str:
        # TODO: Implement getAutomationSystem method
        pass

class libraryElement_ECState(PositionableElement, INamedElement):

    def __init__(self, libraryElement_ECState: "libraryElement_ECC" = None, libraryElement_ECState35: "libraryElement_ECC" = None, ECState: "libraryElement_ECTransition" = None, ECState44: "libraryElement_ECTransition" = None, libraryElement_ECState37: set["libraryElement_ECAction"] = None, source: set["libraryElement_ECTransition"] = None, destination: set["libraryElement_ECTransition"] = None):
        self.libraryElement_ECState = libraryElement_ECState
        self.libraryElement_ECState35 = libraryElement_ECState35
        self.ECState = ECState
        self.ECState44 = ECState44
        self.libraryElement_ECState37 = libraryElement_ECState37 if libraryElement_ECState37 is not None else set()
        self.source = source if source is not None else set()
        self.destination = destination if destination is not None else set()
        
    @property
    def libraryElement_ECState37(self):
        return self.__libraryElement_ECState37

    @libraryElement_ECState37.setter
    def libraryElement_ECState37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__libraryElement_ECState37", None)
        self.__libraryElement_ECState37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_ECAction38"):
                    opp_val = getattr(item, "libraryElement_ECAction38", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_ECAction38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_ECAction38"):
                    opp_val = getattr(item, "libraryElement_ECAction38", None)
                    
                    setattr(item, "libraryElement_ECAction38", self)
                    

    @property
    def libraryElement_ECState35(self):
        return self.__libraryElement_ECState35

    @libraryElement_ECState35.setter
    def libraryElement_ECState35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__libraryElement_ECState35", None)
        self.__libraryElement_ECState35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ECC34"):
                opp_val = getattr(old_value, "libraryElement_ECC34", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_ECC34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ECC34"):
                opp_val = getattr(value, "libraryElement_ECC34", None)
                setattr(value, "libraryElement_ECC34", self)

    @property
    def libraryElement_ECState(self):
        return self.__libraryElement_ECState

    @libraryElement_ECState.setter
    def libraryElement_ECState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__libraryElement_ECState", None)
        self.__libraryElement_ECState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_ECC30"):
                opp_val = getattr(old_value, "libraryElement_ECC30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_ECC30"):
                opp_val = getattr(value, "libraryElement_ECC30", None)
                if opp_val is None:
                    setattr(value, "libraryElement_ECC30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ECState(self):
        return self.__ECState

    @ECState.setter
    def ECState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__ECState", None)
        self.__ECState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outTransitions"):
                opp_val = getattr(old_value, "outTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outTransitions"):
                opp_val = getattr(value, "outTransitions", None)
                setattr(value, "outTransitions", self)

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__destination", None)
        self.__destination = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ECTransition41"):
                    opp_val = getattr(item, "ECTransition41", None)
                    
                    if opp_val == self:
                        setattr(item, "ECTransition41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ECTransition41"):
                    opp_val = getattr(item, "ECTransition41", None)
                    
                    setattr(item, "ECTransition41", self)
                    

    @property
    def ECState44(self):
        return self.__ECState44

    @ECState44.setter
    def ECState44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__ECState44", None)
        self.__ECState44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTransitions"):
                opp_val = getattr(old_value, "inTransitions", None)
                if opp_val == self:
                    setattr(old_value, "inTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTransitions"):
                opp_val = getattr(value, "inTransitions", None)
                setattr(value, "inTransitions", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ECState__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ECTransition"):
                    opp_val = getattr(item, "ECTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "ECTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ECTransition"):
                    opp_val = getattr(item, "ECTransition", None)
                    
                    setattr(item, "ECTransition", self)
                    

    def isStartState(self) -> str:
        # TODO: Implement isStartState method
        pass

class libraryElement_ServiceSequence(INamedElement):

    def __init__(self, TestResult: str, libraryElement_ServiceSequence: set["libraryElement_ServiceTransaction"] = None, libraryElement_ServiceSequence167: "libraryElement_Service" = None):
        self.TestResult = TestResult
        self.libraryElement_ServiceSequence = libraryElement_ServiceSequence if libraryElement_ServiceSequence is not None else set()
        self.libraryElement_ServiceSequence167 = libraryElement_ServiceSequence167
        
    @property
    def TestResult(self) -> str:
        return self.__TestResult

    @TestResult.setter
    def TestResult(self, TestResult: str):
        self.__TestResult = TestResult

    @property
    def libraryElement_ServiceSequence167(self):
        return self.__libraryElement_ServiceSequence167

    @libraryElement_ServiceSequence167.setter
    def libraryElement_ServiceSequence167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ServiceSequence__libraryElement_ServiceSequence167", None)
        self.__libraryElement_ServiceSequence167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Service166"):
                opp_val = getattr(old_value, "libraryElement_Service166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Service166"):
                opp_val = getattr(value, "libraryElement_Service166", None)
                if opp_val is None:
                    setattr(value, "libraryElement_Service166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryElement_ServiceSequence(self):
        return self.__libraryElement_ServiceSequence

    @libraryElement_ServiceSequence.setter
    def libraryElement_ServiceSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ServiceSequence__libraryElement_ServiceSequence", None)
        self.__libraryElement_ServiceSequence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_ServiceTransaction"):
                    opp_val = getattr(item, "libraryElement_ServiceTransaction", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_ServiceTransaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_ServiceTransaction"):
                    opp_val = getattr(item, "libraryElement_ServiceTransaction", None)
                    
                    setattr(item, "libraryElement_ServiceTransaction", self)
                    

class libraryElement_IInterfaceElement(INamedElement):

    def __init__(self, isInput: str, typeName: str, IInterfaceElement12: "libraryElement_Connection" = None, IInterfaceElement: "libraryElement_Connection" = None, destination138: set["libraryElement_Connection"] = None, source140: set["libraryElement_Connection"] = None, libraryElement_IInterfaceElement: "libraryElement_DataType" = None, libraryElement_IInterfaceElement144: "libraryElement_Value" = None):
        self.isInput = isInput
        self.typeName = typeName
        self.IInterfaceElement12 = IInterfaceElement12
        self.IInterfaceElement = IInterfaceElement
        self.destination138 = destination138 if destination138 is not None else set()
        self.source140 = source140 if source140 is not None else set()
        self.libraryElement_IInterfaceElement = libraryElement_IInterfaceElement
        self.libraryElement_IInterfaceElement144 = libraryElement_IInterfaceElement144
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def isInput(self) -> str:
        return self.__isInput

    @isInput.setter
    def isInput(self, isInput: str):
        self.__isInput = isInput

    @property
    def IInterfaceElement12(self):
        return self.__IInterfaceElement12

    @IInterfaceElement12.setter
    def IInterfaceElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__IInterfaceElement12", None)
        self.__IInterfaceElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputConnections"):
                opp_val = getattr(old_value, "inputConnections", None)
                if opp_val == self:
                    setattr(old_value, "inputConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputConnections"):
                opp_val = getattr(value, "inputConnections", None)
                setattr(value, "inputConnections", self)

    @property
    def source140(self):
        return self.__source140

    @source140.setter
    def source140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__source140", None)
        self.__source140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection141"):
                    opp_val = getattr(item, "Connection141", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection141"):
                    opp_val = getattr(item, "Connection141", None)
                    
                    setattr(item, "Connection141", self)
                    

    @property
    def libraryElement_IInterfaceElement144(self):
        return self.__libraryElement_IInterfaceElement144

    @libraryElement_IInterfaceElement144.setter
    def libraryElement_IInterfaceElement144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__libraryElement_IInterfaceElement144", None)
        self.__libraryElement_IInterfaceElement144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_Value"):
                opp_val = getattr(old_value, "libraryElement_Value", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_Value"):
                opp_val = getattr(value, "libraryElement_Value", None)
                setattr(value, "libraryElement_Value", self)

    @property
    def IInterfaceElement(self):
        return self.__IInterfaceElement

    @IInterfaceElement.setter
    def IInterfaceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__IInterfaceElement", None)
        self.__IInterfaceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputConnections"):
                opp_val = getattr(old_value, "outputConnections", None)
                if opp_val == self:
                    setattr(old_value, "outputConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputConnections"):
                opp_val = getattr(value, "outputConnections", None)
                setattr(value, "outputConnections", self)

    @property
    def destination138(self):
        return self.__destination138

    @destination138.setter
    def destination138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__destination138", None)
        self.__destination138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    setattr(item, "Connection", self)
                    

    @property
    def libraryElement_IInterfaceElement(self):
        return self.__libraryElement_IInterfaceElement

    @libraryElement_IInterfaceElement.setter
    def libraryElement_IInterfaceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_IInterfaceElement__libraryElement_IInterfaceElement", None)
        self.__libraryElement_IInterfaceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryElement_DataType"):
                opp_val = getattr(old_value, "libraryElement_DataType", None)
                if opp_val == self:
                    setattr(old_value, "libraryElement_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryElement_DataType"):
                opp_val = getattr(value, "libraryElement_DataType", None)
                setattr(value, "libraryElement_DataType", self)

    def getFBNetworkElement(self) -> FBNetworkElement:
        # TODO: Implement getFBNetworkElement method
        pass

class libraryElement_ConfigurableObject(INamedElement):

    def __init__(self, libraryElement_ConfigurableObject: set["libraryElement_Parameter"] = None):
        self.libraryElement_ConfigurableObject = libraryElement_ConfigurableObject if libraryElement_ConfigurableObject is not None else set()
        
    @property
    def libraryElement_ConfigurableObject(self):
        return self.__libraryElement_ConfigurableObject

    @libraryElement_ConfigurableObject.setter
    def libraryElement_ConfigurableObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_ConfigurableObject__libraryElement_ConfigurableObject", None)
        self.__libraryElement_ConfigurableObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryElement_Parameter"):
                    opp_val = getattr(item, "libraryElement_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryElement_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryElement_Parameter"):
                    opp_val = getattr(item, "libraryElement_Parameter", None)
                    
                    setattr(item, "libraryElement_Parameter", self)
                    

    def getParameter(self, parameterName: str) -> str:
        # TODO: Implement getParameter method
        pass

    def setParameter(self, parameterName: str, value: str):
        # TODO: Implement setParameter method
        pass

class libraryElement_Algorithm(INamedElement):

    pass
class libraryElement_AdapterFBType(FBType):

    pass
class libraryElement_AdapterFB(FB):

    def __init__(self, AdapterFB: "libraryElement_AdapterDeclaration" = None, adapterFB: "libraryElement_AdapterDeclaration" = None):
        self.AdapterFB = AdapterFB
        self.adapterFB = adapterFB
        
    @property
    def AdapterFB(self):
        return self.__AdapterFB

    @AdapterFB.setter
    def AdapterFB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AdapterFB__AdapterFB", None)
        self.__AdapterFB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adapterDecl"):
                opp_val = getattr(old_value, "adapterDecl", None)
                if opp_val == self:
                    setattr(old_value, "adapterDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adapterDecl"):
                opp_val = getattr(value, "adapterDecl", None)
                setattr(value, "adapterDecl", self)

    @property
    def adapterFB(self):
        return self.__adapterFB

    @adapterFB.setter
    def adapterFB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryElement_AdapterFB__adapterFB", None)
        self.__adapterFB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AdapterDeclaration"):
                opp_val = getattr(old_value, "AdapterDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "AdapterDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AdapterDeclaration"):
                opp_val = getattr(value, "AdapterDeclaration", None)
                setattr(value, "AdapterDeclaration", self)

    def isSocket(self) -> str:
        # TODO: Implement isSocket method
        pass

    def isPlug(self) -> str:
        # TODO: Implement isPlug method
        pass

    def getType(self) -> FBType:
        # TODO: Implement getType method
        pass

class VarDeclaration:

    pass
class libraryElement_AdapterDeclaration(VarDeclaration):

    pass