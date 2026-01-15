from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class node:

    pass
class cfg_endnode(node):

    pass
class cfg_startnode(node):

    pass
class cfg_edge:

    pass
class cfg_node:

    def __init__(self, name: str, cfg_node4: "cfg_edge" = None, cfg_node: "cfg_cfg" = None, target: set["cfg_edge"] = None, source: set["cfg_edge"] = None, node: "cfg_edge" = None, cfg_node12: "cfg_edge" = None, node14: "cfg_edge" = None):
        self.name = name
        self.cfg_node4 = cfg_node4
        self.cfg_node = cfg_node
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.node = node
        self.cfg_node12 = cfg_node12
        self.node14 = node14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def node14(self):
        return self.__node14

    @node14.setter
    def node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__node14", None)
        self.__node14 = value
        
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
    def cfg_node12(self):
        return self.__cfg_node12

    @cfg_node12.setter
    def cfg_node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__cfg_node12", None)
        self.__cfg_node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfg_edge11"):
                opp_val = getattr(old_value, "cfg_edge11", None)
                if opp_val == self:
                    setattr(old_value, "cfg_edge11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfg_edge11"):
                opp_val = getattr(value, "cfg_edge11", None)
                setattr(value, "cfg_edge11", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__node", None)
        self.__node = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edge8"):
                    opp_val = getattr(item, "edge8", None)
                    
                    if opp_val == self:
                        setattr(item, "edge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edge8"):
                    opp_val = getattr(item, "edge8", None)
                    
                    setattr(item, "edge8", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edge"):
                    opp_val = getattr(item, "edge", None)
                    
                    if opp_val == self:
                        setattr(item, "edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edge"):
                    opp_val = getattr(item, "edge", None)
                    
                    setattr(item, "edge", self)
                    

    @property
    def cfg_node(self):
        return self.__cfg_node

    @cfg_node.setter
    def cfg_node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__cfg_node", None)
        self.__cfg_node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfg_cfg"):
                opp_val = getattr(old_value, "cfg_cfg", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfg_cfg"):
                opp_val = getattr(value, "cfg_cfg", None)
                if opp_val is None:
                    setattr(value, "cfg_cfg", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cfg_node4(self):
        return self.__cfg_node4

    @cfg_node4.setter
    def cfg_node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfg_node__cfg_node4", None)
        self.__cfg_node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfg_edge5"):
                opp_val = getattr(old_value, "cfg_edge5", None)
                if opp_val == self:
                    setattr(old_value, "cfg_edge5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfg_edge5"):
                opp_val = getattr(value, "cfg_edge5", None)
                setattr(value, "cfg_edge5", self)

class cfg_cfg:

    pass