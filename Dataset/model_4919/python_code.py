from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataRecogniser:

    pass
class web_service_GenericDataRecogniser(DataRecogniser):

    pass
class FunctionProvider:

    pass
class web_service_GenericFunctionProvider(FunctionProvider):

    pass
class MessageFormatter:

    pass
class web_service_GenericMessageFormatter(MessageFormatter):

    pass
class web_service_DataRecogniser:

    def __init__(self, name: str, web_service_DataRecogniser: "web_service_Endpoint" = None):
        self.name = name
        self.web_service_DataRecogniser = web_service_DataRecogniser
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def web_service_DataRecogniser(self):
        return self.__web_service_DataRecogniser

    @web_service_DataRecogniser.setter
    def web_service_DataRecogniser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_DataRecogniser__web_service_DataRecogniser", None)
        self.__web_service_DataRecogniser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_service_Endpoint6"):
                opp_val = getattr(old_value, "web_service_Endpoint6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_service_Endpoint6"):
                opp_val = getattr(value, "web_service_Endpoint6", None)
                if opp_val is None:
                    setattr(value, "web_service_Endpoint6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_service_FunctionProvider:

    def __init__(self, name: str, web_service_FunctionProvider: "web_service_Endpoint" = None):
        self.name = name
        self.web_service_FunctionProvider = web_service_FunctionProvider
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def web_service_FunctionProvider(self):
        return self.__web_service_FunctionProvider

    @web_service_FunctionProvider.setter
    def web_service_FunctionProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_FunctionProvider__web_service_FunctionProvider", None)
        self.__web_service_FunctionProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_service_Endpoint4"):
                opp_val = getattr(old_value, "web_service_Endpoint4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_service_Endpoint4"):
                opp_val = getattr(value, "web_service_Endpoint4", None)
                if opp_val is None:
                    setattr(value, "web_service_Endpoint4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_service_MessageFormatter:

    def __init__(self, name: str, web_service_MessageFormatter: "web_service_Endpoint" = None):
        self.name = name
        self.web_service_MessageFormatter = web_service_MessageFormatter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def web_service_MessageFormatter(self):
        return self.__web_service_MessageFormatter

    @web_service_MessageFormatter.setter
    def web_service_MessageFormatter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_MessageFormatter__web_service_MessageFormatter", None)
        self.__web_service_MessageFormatter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_service_Endpoint2"):
                opp_val = getattr(old_value, "web_service_Endpoint2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_service_Endpoint2"):
                opp_val = getattr(value, "web_service_Endpoint2", None)
                if opp_val is None:
                    setattr(value, "web_service_Endpoint2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_service_Endpoint:

    def __init__(self, name: str, web_service_Endpoint: "web_service_Service" = None, web_service_Endpoint2: set["web_service_MessageFormatter"] = None, web_service_Endpoint4: set["web_service_FunctionProvider"] = None, web_service_Endpoint6: set["web_service_DataRecogniser"] = None):
        self.name = name
        self.web_service_Endpoint = web_service_Endpoint
        self.web_service_Endpoint2 = web_service_Endpoint2 if web_service_Endpoint2 is not None else set()
        self.web_service_Endpoint4 = web_service_Endpoint4 if web_service_Endpoint4 is not None else set()
        self.web_service_Endpoint6 = web_service_Endpoint6 if web_service_Endpoint6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def web_service_Endpoint2(self):
        return self.__web_service_Endpoint2

    @web_service_Endpoint2.setter
    def web_service_Endpoint2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_Endpoint__web_service_Endpoint2", None)
        self.__web_service_Endpoint2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_service_MessageFormatter"):
                    opp_val = getattr(item, "web_service_MessageFormatter", None)
                    
                    if opp_val == self:
                        setattr(item, "web_service_MessageFormatter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_service_MessageFormatter"):
                    opp_val = getattr(item, "web_service_MessageFormatter", None)
                    
                    setattr(item, "web_service_MessageFormatter", self)
                    

    @property
    def web_service_Endpoint4(self):
        return self.__web_service_Endpoint4

    @web_service_Endpoint4.setter
    def web_service_Endpoint4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_Endpoint__web_service_Endpoint4", None)
        self.__web_service_Endpoint4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_service_FunctionProvider"):
                    opp_val = getattr(item, "web_service_FunctionProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "web_service_FunctionProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_service_FunctionProvider"):
                    opp_val = getattr(item, "web_service_FunctionProvider", None)
                    
                    setattr(item, "web_service_FunctionProvider", self)
                    

    @property
    def web_service_Endpoint(self):
        return self.__web_service_Endpoint

    @web_service_Endpoint.setter
    def web_service_Endpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_Endpoint__web_service_Endpoint", None)
        self.__web_service_Endpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_service_Service"):
                opp_val = getattr(old_value, "web_service_Service", None)
                if opp_val == self:
                    setattr(old_value, "web_service_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_service_Service"):
                opp_val = getattr(value, "web_service_Service", None)
                setattr(value, "web_service_Service", self)

    @property
    def web_service_Endpoint6(self):
        return self.__web_service_Endpoint6

    @web_service_Endpoint6.setter
    def web_service_Endpoint6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_service_Endpoint__web_service_Endpoint6", None)
        self.__web_service_Endpoint6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_service_DataRecogniser"):
                    opp_val = getattr(item, "web_service_DataRecogniser", None)
                    
                    if opp_val == self:
                        setattr(item, "web_service_DataRecogniser", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_service_DataRecogniser"):
                    opp_val = getattr(item, "web_service_DataRecogniser", None)
                    
                    setattr(item, "web_service_DataRecogniser", self)
                    

class web_service_Service:

    pass