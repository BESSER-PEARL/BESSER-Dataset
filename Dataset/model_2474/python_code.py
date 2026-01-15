from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TraceLinkEnd:

    pass
class textlink_TraceLinkEnd(ABC):

    pass
class textlink_TextLocation(TraceLinkEnd):

    def __init__(self, resource: str, textlink_TextLocation7: "textlink_Region" = None, textlink_TextLocation: "textlink_TraceLink" = None):
        self.resource = resource
        self.textlink_TextLocation7 = textlink_TextLocation7
        self.textlink_TextLocation = textlink_TextLocation
        
    @property
    def resource(self) -> str:
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource

    @property
    def textlink_TextLocation7(self):
        return self.__textlink_TextLocation7

    @textlink_TextLocation7.setter
    def textlink_TextLocation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textlink_TextLocation__textlink_TextLocation7", None)
        self.__textlink_TextLocation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textlink_Region"):
                opp_val = getattr(old_value, "textlink_Region", None)
                if opp_val == self:
                    setattr(old_value, "textlink_Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textlink_Region"):
                opp_val = getattr(value, "textlink_Region", None)
                setattr(value, "textlink_Region", self)

    @property
    def textlink_TextLocation(self):
        return self.__textlink_TextLocation

    @textlink_TextLocation.setter
    def textlink_TextLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textlink_TextLocation__textlink_TextLocation", None)
        self.__textlink_TextLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textlink_TraceLink4"):
                opp_val = getattr(old_value, "textlink_TraceLink4", None)
                if opp_val == self:
                    setattr(old_value, "textlink_TraceLink4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textlink_TraceLink4"):
                opp_val = getattr(value, "textlink_TraceLink4", None)
                setattr(value, "textlink_TraceLink4", self)

class textlink_ModelLocation(TraceLinkEnd):

    def __init__(self, propertyName: str, textlink_ModelLocation: "textlink_TraceLink" = None):
        self.propertyName = propertyName
        self.textlink_ModelLocation = textlink_ModelLocation
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def textlink_ModelLocation(self):
        return self.__textlink_ModelLocation

    @textlink_ModelLocation.setter
    def textlink_ModelLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textlink_ModelLocation__textlink_ModelLocation", None)
        self.__textlink_ModelLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textlink_TraceLink2"):
                opp_val = getattr(old_value, "textlink_TraceLink2", None)
                if opp_val == self:
                    setattr(old_value, "textlink_TraceLink2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textlink_TraceLink2"):
                opp_val = getattr(value, "textlink_TraceLink2", None)
                setattr(value, "textlink_TraceLink2", self)

class textlink_TraceLink:

    pass
class textlink_Trace:

    pass
class textlink_Region:

    def __init__(self, offset: str, length: str, textlink_Region: "textlink_TextLocation" = None):
        self.offset = offset
        self.length = length
        self.textlink_Region = textlink_Region
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def textlink_Region(self):
        return self.__textlink_Region

    @textlink_Region.setter
    def textlink_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textlink_Region__textlink_Region", None)
        self.__textlink_Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textlink_TextLocation7"):
                opp_val = getattr(old_value, "textlink_TextLocation7", None)
                if opp_val == self:
                    setattr(old_value, "textlink_TextLocation7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textlink_TextLocation7"):
                opp_val = getattr(value, "textlink_TextLocation7", None)
                setattr(value, "textlink_TextLocation7", self)

class textlink_EObject:

    pass
class ModelLocation:

    pass
class textlink_EmfModelLocation(ModelLocation):

    pass