from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloWorld_KeywordsExample:

    def __init__(self, option: str, helloWorld_KeywordsExample: "helloWorld_Model" = None):
        self.option = option
        self.helloWorld_KeywordsExample = helloWorld_KeywordsExample
        
    @property
    def option(self) -> str:
        return self.__option

    @option.setter
    def option(self, option: str):
        self.__option = option

    @property
    def helloWorld_KeywordsExample(self):
        return self.__helloWorld_KeywordsExample

    @helloWorld_KeywordsExample.setter
    def helloWorld_KeywordsExample(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWorld_KeywordsExample__helloWorld_KeywordsExample", None)
        self.__helloWorld_KeywordsExample = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloWorld_Model2"):
                opp_val = getattr(old_value, "helloWorld_Model2", None)
                if opp_val == self:
                    setattr(old_value, "helloWorld_Model2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloWorld_Model2"):
                opp_val = getattr(value, "helloWorld_Model2", None)
                setattr(value, "helloWorld_Model2", self)

class helloWorld_Greeting:

    def __init__(self, name: str, helloWorld_Greeting: "helloWorld_Model" = None):
        self.name = name
        self.helloWorld_Greeting = helloWorld_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloWorld_Greeting(self):
        return self.__helloWorld_Greeting

    @helloWorld_Greeting.setter
    def helloWorld_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWorld_Greeting__helloWorld_Greeting", None)
        self.__helloWorld_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloWorld_Model"):
                opp_val = getattr(old_value, "helloWorld_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloWorld_Model"):
                opp_val = getattr(value, "helloWorld_Model", None)
                if opp_val is None:
                    setattr(value, "helloWorld_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloWorld_Model:

    pass