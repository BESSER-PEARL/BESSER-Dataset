from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class font_Greeting:

    def __init__(self, name: str, font_Greeting: "font_Model" = None):
        self.name = name
        self.font_Greeting = font_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def font_Greeting(self):
        return self.__font_Greeting

    @font_Greeting.setter
    def font_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_font_Greeting__font_Greeting", None)
        self.__font_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "font_Model"):
                opp_val = getattr(old_value, "font_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "font_Model"):
                opp_val = getattr(value, "font_Model", None)
                if opp_val is None:
                    setattr(value, "font_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class font_Model:

    pass