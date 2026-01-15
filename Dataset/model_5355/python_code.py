from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LocatedElement:

    pass
class p2_FeatureMetadata(LocatedElement):

    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Bundle:

    pass
class FeatureMetadata:

    pass
class p2_Plugin(Bundle):

    pass
class Tool:

    pass
class p2_Feature(Tool):

    def __init__(self, application: str, p2_Feature: "p2_Copyright" = None, p2_Feature2: "p2_Description" = None, p2_Feature4: set["p2_DiscoverySite"] = None, p2_Feature6: "p2_License" = None, p2_Feature8: "p2_Vendor" = None, p2_Feature10: set["p2_Plugin"] = None):
        self.application = application
        self.p2_Feature = p2_Feature
        self.p2_Feature2 = p2_Feature2
        self.p2_Feature4 = p2_Feature4 if p2_Feature4 is not None else set()
        self.p2_Feature6 = p2_Feature6
        self.p2_Feature8 = p2_Feature8
        self.p2_Feature10 = p2_Feature10 if p2_Feature10 is not None else set()
        
    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def p2_Feature2(self):
        return self.__p2_Feature2

    @p2_Feature2.setter
    def p2_Feature2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature2", None)
        self.__p2_Feature2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_Description"):
                opp_val = getattr(old_value, "p2_Description", None)
                if opp_val == self:
                    setattr(old_value, "p2_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_Description"):
                opp_val = getattr(value, "p2_Description", None)
                setattr(value, "p2_Description", self)

    @property
    def p2_Feature8(self):
        return self.__p2_Feature8

    @p2_Feature8.setter
    def p2_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature8", None)
        self.__p2_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_Vendor"):
                opp_val = getattr(old_value, "p2_Vendor", None)
                if opp_val == self:
                    setattr(old_value, "p2_Vendor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_Vendor"):
                opp_val = getattr(value, "p2_Vendor", None)
                setattr(value, "p2_Vendor", self)

    @property
    def p2_Feature4(self):
        return self.__p2_Feature4

    @p2_Feature4.setter
    def p2_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature4", None)
        self.__p2_Feature4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_DiscoverySite"):
                    opp_val = getattr(item, "p2_DiscoverySite", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_DiscoverySite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_DiscoverySite"):
                    opp_val = getattr(item, "p2_DiscoverySite", None)
                    
                    setattr(item, "p2_DiscoverySite", self)
                    

    @property
    def p2_Feature10(self):
        return self.__p2_Feature10

    @p2_Feature10.setter
    def p2_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature10", None)
        self.__p2_Feature10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_Plugin"):
                    opp_val = getattr(item, "p2_Plugin", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_Plugin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_Plugin"):
                    opp_val = getattr(item, "p2_Plugin", None)
                    
                    setattr(item, "p2_Plugin", self)
                    

    @property
    def p2_Feature6(self):
        return self.__p2_Feature6

    @p2_Feature6.setter
    def p2_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature6", None)
        self.__p2_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_License"):
                opp_val = getattr(old_value, "p2_License", None)
                if opp_val == self:
                    setattr(old_value, "p2_License", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_License"):
                opp_val = getattr(value, "p2_License", None)
                setattr(value, "p2_License", self)

    @property
    def p2_Feature(self):
        return self.__p2_Feature

    @p2_Feature.setter
    def p2_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Feature__p2_Feature", None)
        self.__p2_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_Copyright"):
                opp_val = getattr(old_value, "p2_Copyright", None)
                if opp_val == self:
                    setattr(old_value, "p2_Copyright", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_Copyright"):
                opp_val = getattr(value, "p2_Copyright", None)
                setattr(value, "p2_Copyright", self)

class p2_Vendor:

    pass
class p2_License(FeatureMetadata):

    pass
class p2_DiscoverySite(FeatureMetadata):

    pass
class p2_Description(FeatureMetadata):

    pass
class p2_Copyright(FeatureMetadata):

    pass