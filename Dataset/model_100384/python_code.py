from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rfsm_Event:

    def __init__(self, eventliteral: str, events: "rfsm_Transition" = None, Event: "rfsm_Transition" = None):
        self.eventliteral = eventliteral
        self.events = events
        self.Event = Event
        
        pass
    @property
    def eventliteral(self):
        return self.__eventliteral

    @eventliteral.setter
    def eventliteral(self, eventliteral: str):
        self.__eventliteral = eventliteral


    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Event__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition26"):
                opp_val = getattr(old_value, "Transition26", None)
                if opp_val == self:
                    setattr(old_value, "Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition26"):
                opp_val = getattr(value, "Transition26", None)
                setattr(value, "Transition26", self)

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner18"):
                opp_val = getattr(old_value, "owner18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner18"):
                opp_val = getattr(value, "owner18", None)
                if opp_val is None:
                    setattr(value, "owner18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rfsm_Function:

    def __init__(self, sourcecode: str, rfsm_Function9: "rfsm_State" = None, rfsm_Function: "rfsm_State" = None, rfsm_Function6: "rfsm_State" = None, rfsm_Function21: "rfsm_Transition" = None, rfsm_Function24: "rfsm_Transition" = None):
        self.sourcecode = sourcecode
        self.rfsm_Function9 = rfsm_Function9
        self.rfsm_Function = rfsm_Function
        self.rfsm_Function6 = rfsm_Function6
        self.rfsm_Function21 = rfsm_Function21
        self.rfsm_Function24 = rfsm_Function24
        
        pass
    @property
    def sourcecode(self):
        return self.__sourcecode

    @sourcecode.setter
    def sourcecode(self, sourcecode: str):
        self.__sourcecode = sourcecode


    @property
    def rfsm_Function21(self):
        return self.__rfsm_Function21

    @rfsm_Function21.setter
    def rfsm_Function21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Function__rfsm_Function21", None)
        self.__rfsm_Function21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Transition20"):
                opp_val = getattr(old_value, "rfsm_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Transition20"):
                opp_val = getattr(value, "rfsm_Transition20", None)
                setattr(value, "rfsm_Transition20", self)

    @property
    def rfsm_Function6(self):
        return self.__rfsm_Function6

    @rfsm_Function6.setter
    def rfsm_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Function__rfsm_Function6", None)
        self.__rfsm_Function6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_State5"):
                opp_val = getattr(old_value, "rfsm_State5", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_State5"):
                opp_val = getattr(value, "rfsm_State5", None)
                setattr(value, "rfsm_State5", self)

    @property
    def rfsm_Function(self):
        return self.__rfsm_Function

    @rfsm_Function.setter
    def rfsm_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Function__rfsm_Function", None)
        self.__rfsm_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_State"):
                opp_val = getattr(old_value, "rfsm_State", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_State"):
                opp_val = getattr(value, "rfsm_State", None)
                setattr(value, "rfsm_State", self)

    @property
    def rfsm_Function9(self):
        return self.__rfsm_Function9

    @rfsm_Function9.setter
    def rfsm_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Function__rfsm_Function9", None)
        self.__rfsm_Function9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_State8"):
                opp_val = getattr(old_value, "rfsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_State8"):
                opp_val = getattr(value, "rfsm_State8", None)
                setattr(value, "rfsm_State8", self)

    @property
    def rfsm_Function24(self):
        return self.__rfsm_Function24

    @rfsm_Function24.setter
    def rfsm_Function24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Function__rfsm_Function24", None)
        self.__rfsm_Function24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Transition23"):
                opp_val = getattr(old_value, "rfsm_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Transition23"):
                opp_val = getattr(value, "rfsm_Transition23", None)
                setattr(value, "rfsm_Transition23", self)

class rfsm_Transition:

    def __init__(self, priority_number: int, Transition: "rfsm_State" = None, transitions: "rfsm_State" = None, rfsm_Transition: "rfsm_Node" = None, Transition26: "rfsm_Event" = None, rfsm_Transition15: "rfsm_Node" = None, owner18: set["rfsm_Event"] = None, rfsm_Transition20: "rfsm_Function" = None, rfsm_Transition23: "rfsm_Function" = None):
        self.priority_number = priority_number
        self.Transition = Transition
        self.transitions = transitions
        self.rfsm_Transition = rfsm_Transition
        self.Transition26 = Transition26
        self.rfsm_Transition15 = rfsm_Transition15
        self.owner18 = owner18 if owner18 is not None else set()
        self.rfsm_Transition20 = rfsm_Transition20
        self.rfsm_Transition23 = rfsm_Transition23
        
        pass
    @property
    def priority_number(self):
        return self.__priority_number

    @priority_number.setter
    def priority_number(self, priority_number: int):
        self.__priority_number = priority_number


    @property
    def rfsm_Transition15(self):
        return self.__rfsm_Transition15

    @rfsm_Transition15.setter
    def rfsm_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__rfsm_Transition15", None)
        self.__rfsm_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Node16"):
                opp_val = getattr(old_value, "rfsm_Node16", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Node16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Node16"):
                opp_val = getattr(value, "rfsm_Node16", None)
                setattr(value, "rfsm_Node16", self)

    @property
    def Transition26(self):
        return self.__Transition26

    @Transition26.setter
    def Transition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__Transition26", None)
        self.__Transition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if opp_val == self:
                    setattr(old_value, "events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                setattr(value, "events", self)

    @property
    def rfsm_Transition20(self):
        return self.__rfsm_Transition20

    @rfsm_Transition20.setter
    def rfsm_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__rfsm_Transition20", None)
        self.__rfsm_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Function21"):
                opp_val = getattr(old_value, "rfsm_Function21", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Function21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Function21"):
                opp_val = getattr(value, "rfsm_Function21", None)
                setattr(value, "rfsm_Function21", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State12"):
                opp_val = getattr(old_value, "State12", None)
                if opp_val == self:
                    setattr(old_value, "State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State12"):
                opp_val = getattr(value, "State12", None)
                setattr(value, "State12", self)

    @property
    def rfsm_Transition(self):
        return self.__rfsm_Transition

    @rfsm_Transition.setter
    def rfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__rfsm_Transition", None)
        self.__rfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Node"):
                opp_val = getattr(old_value, "rfsm_Node", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Node"):
                opp_val = getattr(value, "rfsm_Node", None)
                setattr(value, "rfsm_Node", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner18(self):
        return self.__owner18

    @owner18.setter
    def owner18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__owner18", None)
        self.__owner18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def rfsm_Transition23(self):
        return self.__rfsm_Transition23

    @rfsm_Transition23.setter
    def rfsm_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Transition__rfsm_Transition23", None)
        self.__rfsm_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Function24"):
                opp_val = getattr(old_value, "rfsm_Function24", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Function24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Function24"):
                opp_val = getattr(value, "rfsm_Function24", None)
                setattr(value, "rfsm_Function24", self)

    def isAncestor(self, rfsm_one, rfsm_two) :
        # TODO: Implement isAncestor method
        pass

    def LCA(self, rfsm_two, rfsm_one) :
        # TODO: Implement LCA method
        pass

class rfsm_History:

    def __init__(self, depth: int, hot: bool, rfsm_History: "rfsm_Connector" = None):
        self.depth = depth
        self.hot = hot
        self.rfsm_History = rfsm_History
        
        pass
    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth: int):
        self.__depth = depth


    @property
    def hot(self):
        return self.__hot

    @hot.setter
    def hot(self, hot: bool):
        self.__hot = hot


    @property
    def rfsm_History(self):
        return self.__rfsm_History

    @rfsm_History.setter
    def rfsm_History(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_History__rfsm_History", None)
        self.__rfsm_History = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Connector"):
                opp_val = getattr(old_value, "rfsm_Connector", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Connector"):
                opp_val = getattr(value, "rfsm_Connector", None)
                setattr(value, "rfsm_Connector", self)

class rfsm_Node:

    def __init__(self, name: str, subnodes: "rfsm_State" = None, Node: "rfsm_State" = None, rfsm_Node: "rfsm_Transition" = None, rfsm_Node16: "rfsm_Transition" = None):
        self.name = name
        self.subnodes = subnodes
        self.Node = Node
        self.rfsm_Node = rfsm_Node
        self.rfsm_Node16 = rfsm_Node16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rfsm_Node16(self):
        return self.__rfsm_Node16

    @rfsm_Node16.setter
    def rfsm_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Node__rfsm_Node16", None)
        self.__rfsm_Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Transition15"):
                opp_val = getattr(old_value, "rfsm_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Transition15"):
                opp_val = getattr(value, "rfsm_Transition15", None)
                setattr(value, "rfsm_Transition15", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Node__Node", None)
        self.__Node = value
        
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

    @property
    def rfsm_Node(self):
        return self.__rfsm_Node

    @rfsm_Node.setter
    def rfsm_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Node__rfsm_Node", None)
        self.__rfsm_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_Transition"):
                opp_val = getattr(old_value, "rfsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_Transition"):
                opp_val = getattr(value, "rfsm_Transition", None)
                setattr(value, "rfsm_Transition", self)

    @property
    def subnodes(self):
        return self.__subnodes

    @subnodes.setter
    def subnodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Node__subnodes", None)
        self.__subnodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

class Node:

    pass
class rfsm_Connector(Node):

    def __init__(self, public: bool, rfsm_Connector: "rfsm_History" = None):
        self.public = public
        self.rfsm_Connector = rfsm_Connector
        
        pass
    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, public: bool):
        self.__public = public


    @property
    def rfsm_Connector(self):
        return self.__rfsm_Connector

    @rfsm_Connector.setter
    def rfsm_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rfsm_Connector__rfsm_Connector", None)
        self.__rfsm_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rfsm_History"):
                opp_val = getattr(old_value, "rfsm_History", None)
                if opp_val == self:
                    setattr(old_value, "rfsm_History", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rfsm_History"):
                opp_val = getattr(value, "rfsm_History", None)
                setattr(value, "rfsm_History", self)

class rfsm_State(Node):

    pass