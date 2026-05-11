from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NLUService(Enum):
    WIT = "WIT"
    OTHER = "OTHER"
class Mensageiro(Enum):
    TELEGRAM = "TELEGRAM"
    WEB = "WEB"


############################################
# Definition of Classes
############################################

class StationaryState:

    pass
class mdc_StationaryStateImpl(StationaryState):

    pass
class TransactionalState:

    pass
class mdc_TransactionalStateImpl(TransactionalState):

    pass
class mdc_State(ABC):

    def __init__(self, name: str, messages: str, input: str, mdc_State5: "mdc_StationaryState" = None, mdc_State: "mdc_Chatbot" = None):
        self.name = name
        self.messages = messages
        self.input = input
        self.mdc_State5 = mdc_State5
        self.mdc_State = mdc_State
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def messages(self):
        return self.__messages

    @messages.setter
    def messages(self, messages: str):
        self.__messages = messages


    @property
    def mdc_State(self):
        return self.__mdc_State

    @mdc_State.setter
    def mdc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_State__mdc_State", None)
        self.__mdc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mdc_Chatbot"):
                opp_val = getattr(old_value, "mdc_Chatbot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mdc_Chatbot"):
                opp_val = getattr(value, "mdc_Chatbot", None)
                if opp_val is None:
                    setattr(value, "mdc_Chatbot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mdc_State5(self):
        return self.__mdc_State5

    @mdc_State5.setter
    def mdc_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_State__mdc_State5", None)
        self.__mdc_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mdc_StationaryState4"):
                opp_val = getattr(old_value, "mdc_StationaryState4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mdc_StationaryState4"):
                opp_val = getattr(value, "mdc_StationaryState4", None)
                if opp_val is None:
                    setattr(value, "mdc_StationaryState4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def sincMessages(self):
        # TODO: Implement sincMessages method
        pass

    def entryPoint(self) :
        # TODO: Implement entryPoint method
        pass

class mdc_Chatbot:

    def __init__(self, tokenNluService: str, nluService: str, mensageiro: str, name: str, token: str, mdc_Chatbot2: "mdc_StationaryState" = None, mdc_Chatbot: set["mdc_State"] = None):
        self.tokenNluService = tokenNluService
        self.nluService = nluService
        self.mensageiro = mensageiro
        self.name = name
        self.token = token
        self.mdc_Chatbot2 = mdc_Chatbot2
        self.mdc_Chatbot = mdc_Chatbot if mdc_Chatbot is not None else set()
        
        pass
    @property
    def tokenNluService(self):
        return self.__tokenNluService

    @tokenNluService.setter
    def tokenNluService(self, tokenNluService: str):
        self.__tokenNluService = tokenNluService


    @property
    def nluService(self):
        return self.__nluService

    @nluService.setter
    def nluService(self, nluService: str):
        self.__nluService = nluService


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mensageiro(self):
        return self.__mensageiro

    @mensageiro.setter
    def mensageiro(self, mensageiro: str):
        self.__mensageiro = mensageiro


    @property
    def mdc_Chatbot2(self):
        return self.__mdc_Chatbot2

    @mdc_Chatbot2.setter
    def mdc_Chatbot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_Chatbot__mdc_Chatbot2", None)
        self.__mdc_Chatbot2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mdc_StationaryState"):
                opp_val = getattr(old_value, "mdc_StationaryState", None)
                if opp_val == self:
                    setattr(old_value, "mdc_StationaryState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mdc_StationaryState"):
                opp_val = getattr(value, "mdc_StationaryState", None)
                setattr(value, "mdc_StationaryState", self)

    @property
    def mdc_Chatbot(self):
        return self.__mdc_Chatbot

    @mdc_Chatbot.setter
    def mdc_Chatbot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_Chatbot__mdc_Chatbot", None)
        self.__mdc_Chatbot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mdc_State"):
                    opp_val = getattr(item, "mdc_State", None)
                    
                    if opp_val == self:
                        setattr(item, "mdc_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mdc_State"):
                    opp_val = getattr(item, "mdc_State", None)
                    
                    setattr(item, "mdc_State", self)
                    

class State:

    pass
class mdc_TransactionalState(State):

    pass
class mdc_StationaryState(State):

    def __init__(self, mdc_StationaryState: "mdc_Chatbot" = None, mdc_StationaryState4: set["mdc_State"] = None, mdc_StationaryState7: "mdc_TransactionalState" = None):
        self.mdc_StationaryState = mdc_StationaryState
        self.mdc_StationaryState4 = mdc_StationaryState4 if mdc_StationaryState4 is not None else set()
        self.mdc_StationaryState7 = mdc_StationaryState7
        
        pass
    @property
    def mdc_StationaryState4(self):
        return self.__mdc_StationaryState4

    @mdc_StationaryState4.setter
    def mdc_StationaryState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_StationaryState__mdc_StationaryState4", None)
        self.__mdc_StationaryState4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mdc_State5"):
                    opp_val = getattr(item, "mdc_State5", None)
                    
                    if opp_val == self:
                        setattr(item, "mdc_State5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mdc_State5"):
                    opp_val = getattr(item, "mdc_State5", None)
                    
                    setattr(item, "mdc_State5", self)
                    

    @property
    def mdc_StationaryState(self):
        return self.__mdc_StationaryState

    @mdc_StationaryState.setter
    def mdc_StationaryState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_StationaryState__mdc_StationaryState", None)
        self.__mdc_StationaryState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mdc_Chatbot2"):
                opp_val = getattr(old_value, "mdc_Chatbot2", None)
                if opp_val == self:
                    setattr(old_value, "mdc_Chatbot2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mdc_Chatbot2"):
                opp_val = getattr(value, "mdc_Chatbot2", None)
                setattr(value, "mdc_Chatbot2", self)

    @property
    def mdc_StationaryState7(self):
        return self.__mdc_StationaryState7

    @mdc_StationaryState7.setter
    def mdc_StationaryState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mdc_StationaryState__mdc_StationaryState7", None)
        self.__mdc_StationaryState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mdc_TransactionalState"):
                opp_val = getattr(old_value, "mdc_TransactionalState", None)
                if opp_val == self:
                    setattr(old_value, "mdc_TransactionalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mdc_TransactionalState"):
                opp_val = getattr(value, "mdc_TransactionalState", None)
                setattr(value, "mdc_TransactionalState", self)

    def handler(self) :
        # TODO: Implement handler method
        pass

    def sincTransitions(self):
        # TODO: Implement sincTransitions method
        pass
