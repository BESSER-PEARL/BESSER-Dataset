from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class flowchart_Flowchart:

    pass
class flowchart_Decision:

    def __init__(self, isDecision: bool, condition: str, flowchart_Decision: "flowchart_Node" = None):
        self.isDecision = isDecision
        self.condition = condition
        self.flowchart_Decision = flowchart_Decision
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def isDecision(self) -> bool:
        return self.__isDecision

    @isDecision.setter
    def isDecision(self, isDecision: bool):
        self.__isDecision = isDecision

    @property
    def flowchart_Decision(self):
        return self.__flowchart_Decision

    @flowchart_Decision.setter
    def flowchart_Decision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Decision__flowchart_Decision", None)
        self.__flowchart_Decision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Node9"):
                opp_val = getattr(old_value, "flowchart_Node9", None)
                if opp_val == self:
                    setattr(old_value, "flowchart_Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Node9"):
                opp_val = getattr(value, "flowchart_Node9", None)
                setattr(value, "flowchart_Node9", self)

class flowchart_Action:

    def __init__(self, isAction: bool, flowchart_Action: "flowchart_Node" = None):
        self.isAction = isAction
        self.flowchart_Action = flowchart_Action
        
    @property
    def isAction(self) -> bool:
        return self.__isAction

    @isAction.setter
    def isAction(self, isAction: bool):
        self.__isAction = isAction

    @property
    def flowchart_Action(self):
        return self.__flowchart_Action

    @flowchart_Action.setter
    def flowchart_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Action__flowchart_Action", None)
        self.__flowchart_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Node7"):
                opp_val = getattr(old_value, "flowchart_Node7", None)
                if opp_val == self:
                    setattr(old_value, "flowchart_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Node7"):
                opp_val = getattr(value, "flowchart_Node7", None)
                setattr(value, "flowchart_Node7", self)

class flowchart_Transition:

    def __init__(self, label: str, flowchart_Transition: "flowchart_Flowchart" = None, Transition: "flowchart_Node" = None, Transition5: "flowchart_Node" = None, outgoing: "flowchart_Node" = None, incoming: "flowchart_Node" = None):
        self.label = label
        self.flowchart_Transition = flowchart_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flowchart_Transition(self):
        return self.__flowchart_Transition

    @flowchart_Transition.setter
    def flowchart_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Transition__flowchart_Transition", None)
        self.__flowchart_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Flowchart2"):
                opp_val = getattr(old_value, "flowchart_Flowchart2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Flowchart2"):
                opp_val = getattr(value, "flowchart_Flowchart2", None)
                if opp_val is None:
                    setattr(value, "flowchart_Flowchart2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node12"):
                opp_val = getattr(old_value, "Node12", None)
                if opp_val == self:
                    setattr(old_value, "Node12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node12"):
                opp_val = getattr(value, "Node12", None)
                setattr(value, "Node12", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

class flowchart_Node:

    def __init__(self, name: str, flowchart_Node: "flowchart_Flowchart" = None, target: set["flowchart_Transition"] = None, source: set["flowchart_Transition"] = None, flowchart_Node7: "flowchart_Action" = None, flowchart_Node9: "flowchart_Decision" = None, Node: "flowchart_Transition" = None, Node12: "flowchart_Transition" = None):
        self.name = name
        self.flowchart_Node = flowchart_Node
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.flowchart_Node7 = flowchart_Node7
        self.flowchart_Node9 = flowchart_Node9
        self.Node = Node
        self.Node12 = Node12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def flowchart_Node7(self):
        return self.__flowchart_Node7

    @flowchart_Node7.setter
    def flowchart_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__flowchart_Node7", None)
        self.__flowchart_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Action"):
                opp_val = getattr(old_value, "flowchart_Action", None)
                if opp_val == self:
                    setattr(old_value, "flowchart_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Action"):
                opp_val = getattr(value, "flowchart_Action", None)
                setattr(value, "flowchart_Action", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def flowchart_Node9(self):
        return self.__flowchart_Node9

    @flowchart_Node9.setter
    def flowchart_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__flowchart_Node9", None)
        self.__flowchart_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Decision"):
                opp_val = getattr(old_value, "flowchart_Decision", None)
                if opp_val == self:
                    setattr(old_value, "flowchart_Decision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Decision"):
                opp_val = getattr(value, "flowchart_Decision", None)
                setattr(value, "flowchart_Decision", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def Node12(self):
        return self.__Node12

    @Node12.setter
    def Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__Node12", None)
        self.__Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def flowchart_Node(self):
        return self.__flowchart_Node

    @flowchart_Node.setter
    def flowchart_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__flowchart_Node", None)
        self.__flowchart_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchart_Flowchart"):
                opp_val = getattr(old_value, "flowchart_Flowchart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchart_Flowchart"):
                opp_val = getattr(value, "flowchart_Flowchart", None)
                if opp_val is None:
                    setattr(value, "flowchart_Flowchart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchart_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)
