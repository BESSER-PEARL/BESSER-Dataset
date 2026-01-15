from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class egraphs_EHyperEdge:

    def __init__(self, label: str, EHyperEdge: "egraphs_ENode" = None, EHyperEdge3: "egraphs_ENode" = None, outgoing: "egraphs_ENode" = None, incoming: set["egraphs_ENode"] = None):
        self.label = label
        self.EHyperEdge = EHyperEdge
        self.EHyperEdge3 = EHyperEdge3
        self.outgoing = outgoing
        self.incoming = incoming if incoming is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def EHyperEdge(self):
        return self.__EHyperEdge

    @EHyperEdge.setter
    def EHyperEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_EHyperEdge__EHyperEdge", None)
        self.__EHyperEdge = value
        
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
        old_value = getattr(self, f"_egraphs_EHyperEdge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ENode"):
                opp_val = getattr(old_value, "ENode", None)
                if opp_val == self:
                    setattr(old_value, "ENode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ENode"):
                opp_val = getattr(value, "ENode", None)
                setattr(value, "ENode", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_EHyperEdge__incoming", None)
        self.__incoming = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ENode6"):
                    opp_val = getattr(item, "ENode6", None)
                    
                    if opp_val == self:
                        setattr(item, "ENode6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ENode6"):
                    opp_val = getattr(item, "ENode6", None)
                    
                    setattr(item, "ENode6", self)
                    

    @property
    def EHyperEdge3(self):
        return self.__EHyperEdge3

    @EHyperEdge3.setter
    def EHyperEdge3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_EHyperEdge__EHyperEdge3", None)
        self.__EHyperEdge3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targets"):
                opp_val = getattr(old_value, "targets", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targets"):
                opp_val = getattr(value, "targets", None)
                if opp_val is None:
                    setattr(value, "targets", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class egraphs_ENode:

    def __init__(self, element: str, egraphs_ENode: "egraphs_EGraph" = None, source: set["egraphs_EHyperEdge"] = None, targets: set["egraphs_EHyperEdge"] = None, ENode: "egraphs_EHyperEdge" = None, ENode6: "egraphs_EHyperEdge" = None):
        self.element = element
        self.egraphs_ENode = egraphs_ENode
        self.source = source if source is not None else set()
        self.targets = targets if targets is not None else set()
        self.ENode = ENode
        self.ENode6 = ENode6
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def egraphs_ENode(self):
        return self.__egraphs_ENode

    @egraphs_ENode.setter
    def egraphs_ENode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_ENode__egraphs_ENode", None)
        self.__egraphs_ENode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egraphs_EGraph"):
                opp_val = getattr(old_value, "egraphs_EGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egraphs_EGraph"):
                opp_val = getattr(value, "egraphs_EGraph", None)
                if opp_val is None:
                    setattr(value, "egraphs_EGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ENode(self):
        return self.__ENode

    @ENode.setter
    def ENode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_ENode__ENode", None)
        self.__ENode = value
        
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

    @property
    def ENode6(self):
        return self.__ENode6

    @ENode6.setter
    def ENode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_ENode__ENode6", None)
        self.__ENode6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                if opp_val is None:
                    setattr(value, "incoming", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_ENode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EHyperEdge"):
                    opp_val = getattr(item, "EHyperEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "EHyperEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EHyperEdge"):
                    opp_val = getattr(item, "EHyperEdge", None)
                    
                    setattr(item, "EHyperEdge", self)
                    

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egraphs_ENode__targets", None)
        self.__targets = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EHyperEdge3"):
                    opp_val = getattr(item, "EHyperEdge3", None)
                    
                    if opp_val == self:
                        setattr(item, "EHyperEdge3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EHyperEdge3"):
                    opp_val = getattr(item, "EHyperEdge3", None)
                    
                    setattr(item, "EHyperEdge3", self)
                    

class egraphs_EGraph:

    pass