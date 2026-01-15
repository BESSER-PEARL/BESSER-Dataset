from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Reponse:

    pass
class myDsl_ReponseF(Reponse):

    pass
class myDsl_ReponseT(Reponse):

    pass
class myDsl_Reponse:

    def __init__(self, name: str, myDsl_Reponse: "myDsl_Greeting" = None):
        self.name = name
        self.myDsl_Reponse = myDsl_Reponse
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Reponse(self):
        return self.__myDsl_Reponse

    @myDsl_Reponse.setter
    def myDsl_Reponse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Reponse__myDsl_Reponse", None)
        self.__myDsl_Reponse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting2"):
                opp_val = getattr(old_value, "myDsl_Greeting2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting2"):
                opp_val = getattr(value, "myDsl_Greeting2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Greeting2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Greeting:

    def __init__(self, question: str, myDsl_Greeting: "myDsl_Model" = None, myDsl_Greeting2: set["myDsl_Reponse"] = None):
        self.question = question
        self.myDsl_Greeting = myDsl_Greeting
        self.myDsl_Greeting2 = myDsl_Greeting2 if myDsl_Greeting2 is not None else set()
        
    @property
    def question(self) -> str:
        return self.__question

    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def myDsl_Greeting2(self):
        return self.__myDsl_Greeting2

    @myDsl_Greeting2.setter
    def myDsl_Greeting2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting2", None)
        self.__myDsl_Greeting2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Reponse"):
                    opp_val = getattr(item, "myDsl_Reponse", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Reponse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Reponse"):
                    opp_val = getattr(item, "myDsl_Reponse", None)
                    
                    setattr(item, "myDsl_Reponse", self)
                    

    @property
    def myDsl_Greeting(self):
        return self.__myDsl_Greeting

    @myDsl_Greeting.setter
    def myDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting", None)
        self.__myDsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Model:

    pass