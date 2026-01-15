from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Param:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_App:

    def __init__(self, model_App: set["model_User"] = None, model_App4: set["model_Service"] = None):
        self.model_App = model_App if model_App is not None else set()
        self.model_App4 = model_App4 if model_App4 is not None else set()
        
    @property
    def model_App(self):
        return self.__model_App

    @model_App.setter
    def model_App(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_App__model_App", None)
        self.__model_App = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_User2"):
                    opp_val = getattr(item, "model_User2", None)
                    
                    if opp_val == self:
                        setattr(item, "model_User2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_User2"):
                    opp_val = getattr(item, "model_User2", None)
                    
                    setattr(item, "model_User2", self)
                    

    @property
    def model_App4(self):
        return self.__model_App4

    @model_App4.setter
    def model_App4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_App__model_App4", None)
        self.__model_App4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Service5"):
                    opp_val = getattr(item, "model_Service5", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Service5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Service5"):
                    opp_val = getattr(item, "model_Service5", None)
                    
                    setattr(item, "model_Service5", self)
                    

    def result(self, result: str):
        # TODO: Implement result method
        pass

    def service(self, params: str, token: str, service: str):
        # TODO: Implement service method
        pass

    def authSuccess(self, token: str):
        # TODO: Implement authSuccess method
        pass

    def authFailure(self):
        # TODO: Implement authFailure method
        pass

    def auth(self, login: str, password: str):
        # TODO: Implement auth method
        pass

class model_Service:

    def __init__(self, name: str, methodName: str, acceptedParams: str, model_Service: set["model_User"] = None, model_Service5: "model_App" = None):
        self.name = name
        self.methodName = methodName
        self.acceptedParams = acceptedParams
        self.model_Service = model_Service if model_Service is not None else set()
        self.model_Service5 = model_Service5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def acceptedParams(self) -> str:
        return self.__acceptedParams

    @acceptedParams.setter
    def acceptedParams(self, acceptedParams: str):
        self.__acceptedParams = acceptedParams

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def model_Service5(self):
        return self.__model_Service5

    @model_Service5.setter
    def model_Service5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Service__model_Service5", None)
        self.__model_Service5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_App4"):
                opp_val = getattr(old_value, "model_App4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_App4"):
                opp_val = getattr(value, "model_App4", None)
                if opp_val is None:
                    setattr(value, "model_App4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Service(self):
        return self.__model_Service

    @model_Service.setter
    def model_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Service__model_Service", None)
        self.__model_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    if opp_val == self:
                        setattr(item, "model_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    setattr(item, "model_User", self)
                    

class model_User:

    def __init__(self, name: str, password: str, model_User: "model_Service" = None, model_User2: "model_App" = None):
        self.name = name
        self.password = password
        self.model_User = model_User
        self.model_User2 = model_User2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def model_User2(self):
        return self.__model_User2

    @model_User2.setter
    def model_User2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User2", None)
        self.__model_User2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_App"):
                opp_val = getattr(old_value, "model_App", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_App"):
                opp_val = getattr(value, "model_App", None)
                if opp_val is None:
                    setattr(value, "model_App", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_User(self):
        return self.__model_User

    @model_User.setter
    def model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User", None)
        self.__model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Service"):
                opp_val = getattr(old_value, "model_Service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Service"):
                opp_val = getattr(value, "model_Service", None)
                if opp_val is None:
                    setattr(value, "model_Service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
