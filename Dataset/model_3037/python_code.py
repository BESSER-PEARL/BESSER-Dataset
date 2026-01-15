from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateMachineType(Enum):
    infinite = "infinite"
    stateless = "stateless"
    finite = "finite"
class ConnectionType(Enum):
    independent = "independent"
    dependent = "dependent"


############################################
# Definition of Classes
############################################

class conversation_Junction:

    pass
class conversation_Import:

    def __init__(self, alias: str):
        self.alias = alias
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

class Import:

    pass
class PubliclySubscribable:

    pass
class PubliclyPublishable:

    pass
class conversation_PublicPubSub(PubliclyPublishable, PubliclySubscribable):

    pass
class SubscribableByOthers:

    pass
class PublishableByMe:

    pass
class PublicEvent:

    pass
class PublishableByOthers:

    pass
class SubscribableByMe:

    pass
class conversation_PubliclyPublishable(PublishableByOthers, SubscribableByMe, PublicEvent):

    pass
class conversation_ProjectionField:

    pass
class conversation_PrivatePubSub(SubscribableByMe, PublishableByMe):

    pass
class State:

    pass
class conversation_Join(State):

    pass
class conversation_Decision(State):

    pass
class Event:

    pass
class conversation_PublicEvent(Event):

    pass
class conversation_SubscribableByMe(Event):

    pass
class conversation_PublishableByOthers(Event):

    pass
class conversation_SubscribableByOthers(Event):

    pass
class conversation_PublishableByMe(Event):

    pass
class conversation_Event(ABC):

    def __init__(self, name: str, conversation_Event: "conversation_Projection" = None):
        self.name = name
        self.conversation_Event = conversation_Event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def conversation_Event(self):
        return self.__conversation_Event

    @conversation_Event.setter
    def conversation_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Event__conversation_Event", None)
        self.__conversation_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_Projection30"):
                opp_val = getattr(old_value, "conversation_Projection30", None)
                if opp_val == self:
                    setattr(old_value, "conversation_Projection30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_Projection30"):
                opp_val = getattr(value, "conversation_Projection30", None)
                setattr(value, "conversation_Projection30", self)

class conversation_Transition:

    def __init__(self, requiresExecution: bool, conversation_Transition: "conversation_StateMachine" = None, conversation_Transition33: "conversation_State" = None, conversation_Transition37: "conversation_State" = None, conversation_Transition40: "conversation_SubscribableByOthers" = None, transition: "conversation_PrivatePubSub" = None, conversation_Transition43: "conversation_PublishableByOthers" = None, conversation_Transition45: "conversation_PublishableByMe" = None, conversation_Transition47: "conversation_ProjectionField" = None, Transition: "conversation_PrivatePubSub" = None):
        self.requiresExecution = requiresExecution
        self.conversation_Transition = conversation_Transition
        self.conversation_Transition33 = conversation_Transition33
        self.conversation_Transition37 = conversation_Transition37
        self.conversation_Transition40 = conversation_Transition40
        self.transition = transition
        self.conversation_Transition43 = conversation_Transition43
        self.conversation_Transition45 = conversation_Transition45
        self.conversation_Transition47 = conversation_Transition47
        self.Transition = Transition
        
    @property
    def requiresExecution(self) -> bool:
        return self.__requiresExecution

    @requiresExecution.setter
    def requiresExecution(self, requiresExecution: bool):
        self.__requiresExecution = requiresExecution

    @property
    def conversation_Transition37(self):
        return self.__conversation_Transition37

    @conversation_Transition37.setter
    def conversation_Transition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition37", None)
        self.__conversation_Transition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_State38"):
                opp_val = getattr(old_value, "conversation_State38", None)
                if opp_val == self:
                    setattr(old_value, "conversation_State38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_State38"):
                opp_val = getattr(value, "conversation_State38", None)
                setattr(value, "conversation_State38", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "causedBy"):
                opp_val = getattr(old_value, "causedBy", None)
                if opp_val == self:
                    setattr(old_value, "causedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "causedBy"):
                opp_val = getattr(value, "causedBy", None)
                setattr(value, "causedBy", self)

    @property
    def conversation_Transition(self):
        return self.__conversation_Transition

    @conversation_Transition.setter
    def conversation_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition", None)
        self.__conversation_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_StateMachine28"):
                opp_val = getattr(old_value, "conversation_StateMachine28", None)
                if opp_val == self:
                    setattr(old_value, "conversation_StateMachine28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_StateMachine28"):
                opp_val = getattr(value, "conversation_StateMachine28", None)
                setattr(value, "conversation_StateMachine28", self)

    @property
    def conversation_Transition47(self):
        return self.__conversation_Transition47

    @conversation_Transition47.setter
    def conversation_Transition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition47", None)
        self.__conversation_Transition47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_ProjectionField"):
                opp_val = getattr(old_value, "conversation_ProjectionField", None)
                if opp_val == self:
                    setattr(old_value, "conversation_ProjectionField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_ProjectionField"):
                opp_val = getattr(value, "conversation_ProjectionField", None)
                setattr(value, "conversation_ProjectionField", self)

    @property
    def conversation_Transition43(self):
        return self.__conversation_Transition43

    @conversation_Transition43.setter
    def conversation_Transition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition43", None)
        self.__conversation_Transition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_PublishableByOthers"):
                opp_val = getattr(old_value, "conversation_PublishableByOthers", None)
                if opp_val == self:
                    setattr(old_value, "conversation_PublishableByOthers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_PublishableByOthers"):
                opp_val = getattr(value, "conversation_PublishableByOthers", None)
                setattr(value, "conversation_PublishableByOthers", self)

    @property
    def conversation_Transition33(self):
        return self.__conversation_Transition33

    @conversation_Transition33.setter
    def conversation_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition33", None)
        self.__conversation_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_State32"):
                opp_val = getattr(old_value, "conversation_State32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_State32"):
                opp_val = getattr(value, "conversation_State32", None)
                if opp_val is None:
                    setattr(value, "conversation_State32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conversation_Transition45(self):
        return self.__conversation_Transition45

    @conversation_Transition45.setter
    def conversation_Transition45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition45", None)
        self.__conversation_Transition45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_PublishableByMe"):
                opp_val = getattr(old_value, "conversation_PublishableByMe", None)
                if opp_val == self:
                    setattr(old_value, "conversation_PublishableByMe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_PublishableByMe"):
                opp_val = getattr(value, "conversation_PublishableByMe", None)
                setattr(value, "conversation_PublishableByMe", self)

    @property
    def conversation_Transition40(self):
        return self.__conversation_Transition40

    @conversation_Transition40.setter
    def conversation_Transition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__conversation_Transition40", None)
        self.__conversation_Transition40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_SubscribableByOthers"):
                opp_val = getattr(old_value, "conversation_SubscribableByOthers", None)
                if opp_val == self:
                    setattr(old_value, "conversation_SubscribableByOthers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_SubscribableByOthers"):
                opp_val = getattr(value, "conversation_SubscribableByOthers", None)
                setattr(value, "conversation_SubscribableByOthers", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrivatePubSub"):
                opp_val = getattr(old_value, "PrivatePubSub", None)
                if opp_val == self:
                    setattr(old_value, "PrivatePubSub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrivatePubSub"):
                opp_val = getattr(value, "PrivatePubSub", None)
                setattr(value, "PrivatePubSub", self)

class conversation_PubliclySubscribable(SubscribableByOthers, PublishableByMe, PublicEvent):

    pass
class conversation_StateMachine:

    pass
class conversation_State:

    def __init__(self, requiresExecution: bool, join: bool, name: str, conversation_State: "conversation_StateMachine" = None, State: "conversation_StateMachine" = None, states: "conversation_StateMachine" = None, conversation_State32: set["conversation_Transition"] = None, conversation_State38: "conversation_Transition" = None):
        self.requiresExecution = requiresExecution
        self.join = join
        self.name = name
        self.conversation_State = conversation_State
        self.State = State
        self.states = states
        self.conversation_State32 = conversation_State32 if conversation_State32 is not None else set()
        self.conversation_State38 = conversation_State38
        
    @property
    def requiresExecution(self) -> bool:
        return self.__requiresExecution

    @requiresExecution.setter
    def requiresExecution(self, requiresExecution: bool):
        self.__requiresExecution = requiresExecution

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def join(self) -> bool:
        return self.__join

    @join.setter
    def join(self, join: bool):
        self.__join = join

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine35"):
                opp_val = getattr(old_value, "StateMachine35", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine35"):
                opp_val = getattr(value, "StateMachine35", None)
                setattr(value, "StateMachine35", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent24"):
                opp_val = getattr(old_value, "parent24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent24"):
                opp_val = getattr(value, "parent24", None)
                if opp_val is None:
                    setattr(value, "parent24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conversation_State32(self):
        return self.__conversation_State32

    @conversation_State32.setter
    def conversation_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_State__conversation_State32", None)
        self.__conversation_State32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_Transition33"):
                    opp_val = getattr(item, "conversation_Transition33", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_Transition33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_Transition33"):
                    opp_val = getattr(item, "conversation_Transition33", None)
                    
                    setattr(item, "conversation_Transition33", self)
                    

    @property
    def conversation_State38(self):
        return self.__conversation_State38

    @conversation_State38.setter
    def conversation_State38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_State__conversation_State38", None)
        self.__conversation_State38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_Transition37"):
                opp_val = getattr(old_value, "conversation_Transition37", None)
                if opp_val == self:
                    setattr(old_value, "conversation_Transition37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_Transition37"):
                opp_val = getattr(value, "conversation_Transition37", None)
                setattr(value, "conversation_Transition37", self)

    @property
    def conversation_State(self):
        return self.__conversation_State

    @conversation_State.setter
    def conversation_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_State__conversation_State", None)
        self.__conversation_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_StateMachine"):
                opp_val = getattr(old_value, "conversation_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "conversation_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_StateMachine"):
                opp_val = getattr(value, "conversation_StateMachine", None)
                setattr(value, "conversation_StateMachine", self)

class conversation_View:

    pass
class conversation_AgentImport(Import):

    pass
class conversation_TypeImport(Import):

    pass
class conversation_Service:

    pass
class conversation_Agent:

    def __init__(self, name: str, stateMachineType: str, connectionType: str, accessRequirement: str, Agent: "conversation_Conversation" = None, conversation_Agent: set["conversation_Projection"] = None, parent15: "conversation_StateMachine" = None, parent17: set["conversation_PubliclySubscribable"] = None, agents: "conversation_Conversation" = None, conversation_Agent20: "conversation_Projection" = None, Agent26: "conversation_StateMachine" = None, Agent49: "conversation_PubliclySubscribable" = None, conversation_Agent53: "conversation_AgentImport" = None):
        self.name = name
        self.stateMachineType = stateMachineType
        self.connectionType = connectionType
        self.accessRequirement = accessRequirement
        self.Agent = Agent
        self.conversation_Agent = conversation_Agent if conversation_Agent is not None else set()
        self.parent15 = parent15
        self.parent17 = parent17 if parent17 is not None else set()
        self.agents = agents
        self.conversation_Agent20 = conversation_Agent20
        self.Agent26 = Agent26
        self.Agent49 = Agent49
        self.conversation_Agent53 = conversation_Agent53
        
    @property
    def stateMachineType(self) -> str:
        return self.__stateMachineType

    @stateMachineType.setter
    def stateMachineType(self, stateMachineType: str):
        self.__stateMachineType = stateMachineType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accessRequirement(self) -> str:
        return self.__accessRequirement

    @accessRequirement.setter
    def accessRequirement(self, accessRequirement: str):
        self.__accessRequirement = accessRequirement

    @property
    def connectionType(self) -> str:
        return self.__connectionType

    @connectionType.setter
    def connectionType(self, connectionType: str):
        self.__connectionType = connectionType

    @property
    def Agent49(self):
        return self.__Agent49

    @Agent49.setter
    def Agent49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__Agent49", None)
        self.__Agent49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sendables"):
                opp_val = getattr(old_value, "sendables", None)
                if opp_val == self:
                    setattr(old_value, "sendables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sendables"):
                opp_val = getattr(value, "sendables", None)
                setattr(value, "sendables", self)

    @property
    def conversation_Agent(self):
        return self.__conversation_Agent

    @conversation_Agent.setter
    def conversation_Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__conversation_Agent", None)
        self.__conversation_Agent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_Projection13"):
                    opp_val = getattr(item, "conversation_Projection13", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_Projection13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_Projection13"):
                    opp_val = getattr(item, "conversation_Projection13", None)
                    
                    setattr(item, "conversation_Projection13", self)
                    

    @property
    def Agent26(self):
        return self.__Agent26

    @Agent26.setter
    def Agent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__Agent26", None)
        self.__Agent26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine"):
                opp_val = getattr(old_value, "stateMachine", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine"):
                opp_val = getattr(value, "stateMachine", None)
                setattr(value, "stateMachine", self)

    @property
    def conversation_Agent53(self):
        return self.__conversation_Agent53

    @conversation_Agent53.setter
    def conversation_Agent53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__conversation_Agent53", None)
        self.__conversation_Agent53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_AgentImport52"):
                opp_val = getattr(old_value, "conversation_AgentImport52", None)
                if opp_val == self:
                    setattr(old_value, "conversation_AgentImport52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_AgentImport52"):
                opp_val = getattr(value, "conversation_AgentImport52", None)
                setattr(value, "conversation_AgentImport52", self)

    @property
    def parent15(self):
        return self.__parent15

    @parent15.setter
    def parent15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__parent15", None)
        self.__parent15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def parent17(self):
        return self.__parent17

    @parent17.setter
    def parent17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__parent17", None)
        self.__parent17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PubliclySubscribable"):
                    opp_val = getattr(item, "PubliclySubscribable", None)
                    
                    if opp_val == self:
                        setattr(item, "PubliclySubscribable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PubliclySubscribable"):
                    opp_val = getattr(item, "PubliclySubscribable", None)
                    
                    setattr(item, "PubliclySubscribable", self)
                    

    @property
    def agents(self):
        return self.__agents

    @agents.setter
    def agents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__agents", None)
        self.__agents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conversation"):
                opp_val = getattr(old_value, "Conversation", None)
                if opp_val == self:
                    setattr(old_value, "Conversation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conversation"):
                opp_val = getattr(value, "Conversation", None)
                setattr(value, "Conversation", self)

    @property
    def conversation_Agent20(self):
        return self.__conversation_Agent20

    @conversation_Agent20.setter
    def conversation_Agent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__conversation_Agent20", None)
        self.__conversation_Agent20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conversation_Projection21"):
                opp_val = getattr(old_value, "conversation_Projection21", None)
                if opp_val == self:
                    setattr(old_value, "conversation_Projection21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conversation_Projection21"):
                opp_val = getattr(value, "conversation_Projection21", None)
                setattr(value, "conversation_Projection21", self)

    @property
    def Agent(self):
        return self.__Agent

    @Agent.setter
    def Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Agent__Agent", None)
        self.__Agent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class conversation_Conversation:

    def __init__(self, name: str, conversation_Conversation: set["conversation_Projection"] = None, parent: set["conversation_Agent"] = None, conversation_Conversation3: set["conversation_RestService"] = None, conversation_Conversation5: set["conversation_Service"] = None, conversation_Conversation7: set["conversation_TypeImport"] = None, conversation_Conversation9: set["conversation_AgentImport"] = None, conversation_Conversation11: set["conversation_View"] = None, Conversation: "conversation_Agent" = None):
        self.name = name
        self.conversation_Conversation = conversation_Conversation if conversation_Conversation is not None else set()
        self.parent = parent if parent is not None else set()
        self.conversation_Conversation3 = conversation_Conversation3 if conversation_Conversation3 is not None else set()
        self.conversation_Conversation5 = conversation_Conversation5 if conversation_Conversation5 is not None else set()
        self.conversation_Conversation7 = conversation_Conversation7 if conversation_Conversation7 is not None else set()
        self.conversation_Conversation9 = conversation_Conversation9 if conversation_Conversation9 is not None else set()
        self.conversation_Conversation11 = conversation_Conversation11 if conversation_Conversation11 is not None else set()
        self.Conversation = Conversation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def conversation_Conversation5(self):
        return self.__conversation_Conversation5

    @conversation_Conversation5.setter
    def conversation_Conversation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation5", None)
        self.__conversation_Conversation5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_Service"):
                    opp_val = getattr(item, "conversation_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_Service"):
                    opp_val = getattr(item, "conversation_Service", None)
                    
                    setattr(item, "conversation_Service", self)
                    

    @property
    def conversation_Conversation11(self):
        return self.__conversation_Conversation11

    @conversation_Conversation11.setter
    def conversation_Conversation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation11", None)
        self.__conversation_Conversation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_View"):
                    opp_val = getattr(item, "conversation_View", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_View"):
                    opp_val = getattr(item, "conversation_View", None)
                    
                    setattr(item, "conversation_View", self)
                    

    @property
    def conversation_Conversation9(self):
        return self.__conversation_Conversation9

    @conversation_Conversation9.setter
    def conversation_Conversation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation9", None)
        self.__conversation_Conversation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_AgentImport"):
                    opp_val = getattr(item, "conversation_AgentImport", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_AgentImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_AgentImport"):
                    opp_val = getattr(item, "conversation_AgentImport", None)
                    
                    setattr(item, "conversation_AgentImport", self)
                    

    @property
    def conversation_Conversation3(self):
        return self.__conversation_Conversation3

    @conversation_Conversation3.setter
    def conversation_Conversation3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation3", None)
        self.__conversation_Conversation3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_RestService"):
                    opp_val = getattr(item, "conversation_RestService", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_RestService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_RestService"):
                    opp_val = getattr(item, "conversation_RestService", None)
                    
                    setattr(item, "conversation_RestService", self)
                    

    @property
    def Conversation(self):
        return self.__Conversation

    @Conversation.setter
    def Conversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__Conversation", None)
        self.__Conversation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agents"):
                opp_val = getattr(old_value, "agents", None)
                if opp_val == self:
                    setattr(old_value, "agents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agents"):
                opp_val = getattr(value, "agents", None)
                setattr(value, "agents", self)

    @property
    def conversation_Conversation7(self):
        return self.__conversation_Conversation7

    @conversation_Conversation7.setter
    def conversation_Conversation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation7", None)
        self.__conversation_Conversation7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_TypeImport"):
                    opp_val = getattr(item, "conversation_TypeImport", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_TypeImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_TypeImport"):
                    opp_val = getattr(item, "conversation_TypeImport", None)
                    
                    setattr(item, "conversation_TypeImport", self)
                    

    @property
    def conversation_Conversation(self):
        return self.__conversation_Conversation

    @conversation_Conversation.setter
    def conversation_Conversation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__conversation_Conversation", None)
        self.__conversation_Conversation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conversation_Projection"):
                    opp_val = getattr(item, "conversation_Projection", None)
                    
                    if opp_val == self:
                        setattr(item, "conversation_Projection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conversation_Projection"):
                    opp_val = getattr(item, "conversation_Projection", None)
                    
                    setattr(item, "conversation_Projection", self)
                    

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conversation_Conversation__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Agent"):
                    opp_val = getattr(item, "Agent", None)
                    
                    if opp_val == self:
                        setattr(item, "Agent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Agent"):
                    opp_val = getattr(item, "Agent", None)
                    
                    setattr(item, "Agent", self)
                    

class conversation_RestService:

    pass
class conversation_Projection:

    pass