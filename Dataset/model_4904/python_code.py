from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Service_Tool:

    def __init__(self, name: str, Service_Tool: set["Service_JavaService"] = None):
        self.name = name
        self.Service_Tool = Service_Tool if Service_Tool is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Service_Tool(self):
        return self.__Service_Tool

    @Service_Tool.setter
    def Service_Tool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service_Tool__Service_Tool", None)
        self.__Service_Tool = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service_JavaService"):
                    opp_val = getattr(item, "Service_JavaService", None)
                    
                    if opp_val == self:
                        setattr(item, "Service_JavaService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service_JavaService"):
                    opp_val = getattr(item, "Service_JavaService", None)
                    
                    setattr(item, "Service_JavaService", self)
                    

class Service_JavaService:

    def __init__(self, name: str, option: str, Service_JavaService: "Service_Tool" = None):
        self.name = name
        self.option = option
        self.Service_JavaService = Service_JavaService
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def option(self) -> str:
        return self.__option

    @option.setter
    def option(self, option: str):
        self.__option = option

    @property
    def Service_JavaService(self):
        return self.__Service_JavaService

    @Service_JavaService.setter
    def Service_JavaService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service_JavaService__Service_JavaService", None)
        self.__Service_JavaService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service_Tool"):
                opp_val = getattr(old_value, "Service_Tool", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service_Tool"):
                opp_val = getattr(value, "Service_Tool", None)
                if opp_val is None:
                    setattr(value, "Service_Tool", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
