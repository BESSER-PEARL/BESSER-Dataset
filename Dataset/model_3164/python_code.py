from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class softwaretraces_MyNode(ABC):

    pass
class MyNode:

    pass
class softwaretraces_Feature(MyNode):

    def __init__(self, name: str, softwaretraces_Feature: "softwaretraces_Model" = None, softwaretraces_Feature5: "softwaretraces_Feature" = None, softwaretraces_Feature3: set["softwaretraces_Feature"] = None, softwaretraces_Feature7: set["softwaretraces_Trace"] = None):
        self.name = name
        self.softwaretraces_Feature = softwaretraces_Feature
        self.softwaretraces_Feature5 = softwaretraces_Feature5
        self.softwaretraces_Feature3 = softwaretraces_Feature3 if softwaretraces_Feature3 is not None else set()
        self.softwaretraces_Feature7 = softwaretraces_Feature7 if softwaretraces_Feature7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softwaretraces_Feature3(self):
        return self.__softwaretraces_Feature3

    @softwaretraces_Feature3.setter
    def softwaretraces_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Feature__softwaretraces_Feature3", None)
        self.__softwaretraces_Feature3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softwaretraces_Feature5"):
                    opp_val = getattr(item, "softwaretraces_Feature5", None)
                    
                    if opp_val == self:
                        setattr(item, "softwaretraces_Feature5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softwaretraces_Feature5"):
                    opp_val = getattr(item, "softwaretraces_Feature5", None)
                    
                    setattr(item, "softwaretraces_Feature5", self)
                    

    @property
    def softwaretraces_Feature(self):
        return self.__softwaretraces_Feature

    @softwaretraces_Feature.setter
    def softwaretraces_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Feature__softwaretraces_Feature", None)
        self.__softwaretraces_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softwaretraces_Model"):
                opp_val = getattr(old_value, "softwaretraces_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softwaretraces_Model"):
                opp_val = getattr(value, "softwaretraces_Model", None)
                if opp_val is None:
                    setattr(value, "softwaretraces_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softwaretraces_Feature5(self):
        return self.__softwaretraces_Feature5

    @softwaretraces_Feature5.setter
    def softwaretraces_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Feature__softwaretraces_Feature5", None)
        self.__softwaretraces_Feature5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softwaretraces_Feature3"):
                opp_val = getattr(old_value, "softwaretraces_Feature3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softwaretraces_Feature3"):
                opp_val = getattr(value, "softwaretraces_Feature3", None)
                if opp_val is None:
                    setattr(value, "softwaretraces_Feature3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softwaretraces_Feature7(self):
        return self.__softwaretraces_Feature7

    @softwaretraces_Feature7.setter
    def softwaretraces_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Feature__softwaretraces_Feature7", None)
        self.__softwaretraces_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softwaretraces_Trace8"):
                    opp_val = getattr(item, "softwaretraces_Trace8", None)
                    
                    if opp_val == self:
                        setattr(item, "softwaretraces_Trace8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softwaretraces_Trace8"):
                    opp_val = getattr(item, "softwaretraces_Trace8", None)
                    
                    setattr(item, "softwaretraces_Trace8", self)
                    

class softwaretraces_Trace(MyNode):

    def __init__(self, projectName: str, fileName: str, lineNumber: int, softwaretraces_Trace: "softwaretraces_Model" = None, softwaretraces_Trace8: "softwaretraces_Feature" = None, softwaretraces_Trace11: "softwaretraces_Trace" = None, softwaretraces_Trace9: set["softwaretraces_Trace"] = None):
        self.projectName = projectName
        self.fileName = fileName
        self.lineNumber = lineNumber
        self.softwaretraces_Trace = softwaretraces_Trace
        self.softwaretraces_Trace8 = softwaretraces_Trace8
        self.softwaretraces_Trace11 = softwaretraces_Trace11
        self.softwaretraces_Trace9 = softwaretraces_Trace9 if softwaretraces_Trace9 is not None else set()
        
    @property
    def projectName(self) -> str:
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def lineNumber(self) -> int:
        return self.__lineNumber

    @lineNumber.setter
    def lineNumber(self, lineNumber: int):
        self.__lineNumber = lineNumber

    @property
    def softwaretraces_Trace8(self):
        return self.__softwaretraces_Trace8

    @softwaretraces_Trace8.setter
    def softwaretraces_Trace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Trace__softwaretraces_Trace8", None)
        self.__softwaretraces_Trace8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softwaretraces_Feature7"):
                opp_val = getattr(old_value, "softwaretraces_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softwaretraces_Feature7"):
                opp_val = getattr(value, "softwaretraces_Feature7", None)
                if opp_val is None:
                    setattr(value, "softwaretraces_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softwaretraces_Trace9(self):
        return self.__softwaretraces_Trace9

    @softwaretraces_Trace9.setter
    def softwaretraces_Trace9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Trace__softwaretraces_Trace9", None)
        self.__softwaretraces_Trace9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softwaretraces_Trace11"):
                    opp_val = getattr(item, "softwaretraces_Trace11", None)
                    
                    if opp_val == self:
                        setattr(item, "softwaretraces_Trace11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softwaretraces_Trace11"):
                    opp_val = getattr(item, "softwaretraces_Trace11", None)
                    
                    setattr(item, "softwaretraces_Trace11", self)
                    

    @property
    def softwaretraces_Trace(self):
        return self.__softwaretraces_Trace

    @softwaretraces_Trace.setter
    def softwaretraces_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Trace__softwaretraces_Trace", None)
        self.__softwaretraces_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softwaretraces_Model2"):
                opp_val = getattr(old_value, "softwaretraces_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softwaretraces_Model2"):
                opp_val = getattr(value, "softwaretraces_Model2", None)
                if opp_val is None:
                    setattr(value, "softwaretraces_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softwaretraces_Trace11(self):
        return self.__softwaretraces_Trace11

    @softwaretraces_Trace11.setter
    def softwaretraces_Trace11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Trace__softwaretraces_Trace11", None)
        self.__softwaretraces_Trace11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softwaretraces_Trace9"):
                opp_val = getattr(old_value, "softwaretraces_Trace9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softwaretraces_Trace9"):
                opp_val = getattr(value, "softwaretraces_Trace9", None)
                if opp_val is None:
                    setattr(value, "softwaretraces_Trace9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softwaretraces_Model(MyNode):

    def __init__(self, resourceFileName: str, softwaretraces_Model: set["softwaretraces_Feature"] = None, softwaretraces_Model2: set["softwaretraces_Trace"] = None):
        self.resourceFileName = resourceFileName
        self.softwaretraces_Model = softwaretraces_Model if softwaretraces_Model is not None else set()
        self.softwaretraces_Model2 = softwaretraces_Model2 if softwaretraces_Model2 is not None else set()
        
    @property
    def resourceFileName(self) -> str:
        return self.__resourceFileName

    @resourceFileName.setter
    def resourceFileName(self, resourceFileName: str):
        self.__resourceFileName = resourceFileName

    @property
    def softwaretraces_Model2(self):
        return self.__softwaretraces_Model2

    @softwaretraces_Model2.setter
    def softwaretraces_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Model__softwaretraces_Model2", None)
        self.__softwaretraces_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softwaretraces_Trace"):
                    opp_val = getattr(item, "softwaretraces_Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "softwaretraces_Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softwaretraces_Trace"):
                    opp_val = getattr(item, "softwaretraces_Trace", None)
                    
                    setattr(item, "softwaretraces_Trace", self)
                    

    @property
    def softwaretraces_Model(self):
        return self.__softwaretraces_Model

    @softwaretraces_Model.setter
    def softwaretraces_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softwaretraces_Model__softwaretraces_Model", None)
        self.__softwaretraces_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softwaretraces_Feature"):
                    opp_val = getattr(item, "softwaretraces_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "softwaretraces_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softwaretraces_Feature"):
                    opp_val = getattr(item, "softwaretraces_Feature", None)
                    
                    setattr(item, "softwaretraces_Feature", self)
                    
