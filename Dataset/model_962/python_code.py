from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class vml_Model:

    pass
class vml_Edge:

    def __init__(self, relation: str, vml_Edge: "vml_Graph" = None, Edge: "vml_Node" = None, Edge13: "vml_Node" = None, outgoing: "vml_Node" = None, incoming: "vml_Node" = None):
        self.relation = relation
        self.vml_Edge = vml_Edge
        self.Edge = Edge
        self.Edge13 = Edge13
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__Edge", None)
        self.__Edge = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node16"):
                opp_val = getattr(old_value, "Node16", None)
                if opp_val == self:
                    setattr(old_value, "Node16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node16"):
                opp_val = getattr(value, "Node16", None)
                setattr(value, "Node16", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__outgoing", None)
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

    @property
    def Edge13(self):
        return self.__Edge13

    @Edge13.setter
    def Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__Edge13", None)
        self.__Edge13 = value
        
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
    def vml_Edge(self):
        return self.__vml_Edge

    @vml_Edge.setter
    def vml_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__vml_Edge", None)
        self.__vml_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Graph10"):
                opp_val = getattr(old_value, "vml_Graph10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Graph10"):
                opp_val = getattr(value, "vml_Graph10", None)
                if opp_val is None:
                    setattr(value, "vml_Graph10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vml_Node:

    def __init__(self, title: str, vml_Node: "vml_Graph" = None, source: set["vml_Edge"] = None, target: set["vml_Edge"] = None, Node: "vml_Edge" = None, Node16: "vml_Edge" = None):
        self.title = title
        self.vml_Node = vml_Node
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node16 = Node16
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    setattr(item, "Edge13", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__Node", None)
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

    @property
    def vml_Node(self):
        return self.__vml_Node

    @vml_Node.setter
    def vml_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__vml_Node", None)
        self.__vml_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Graph8"):
                opp_val = getattr(old_value, "vml_Graph8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Graph8"):
                opp_val = getattr(value, "vml_Graph8", None)
                if opp_val is None:
                    setattr(value, "vml_Graph8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def Node16(self):
        return self.__Node16

    @Node16.setter
    def Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__Node16", None)
        self.__Node16 = value
        
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

class vml_Slice:

    def __init__(self, title: str, value: int, vml_Slice: "vml_Pie" = None):
        self.title = title
        self.value = value
        self.vml_Slice = vml_Slice
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def vml_Slice(self):
        return self.__vml_Slice

    @vml_Slice.setter
    def vml_Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Slice__vml_Slice", None)
        self.__vml_Slice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Pie6"):
                opp_val = getattr(old_value, "vml_Pie6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Pie6"):
                opp_val = getattr(value, "vml_Pie6", None)
                if opp_val is None:
                    setattr(value, "vml_Pie6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vml_Graph:

    def __init__(self, ID: str, title: str, vml_Graph: "vml_Diagram" = None, vml_Graph8: set["vml_Node"] = None, vml_Graph10: set["vml_Edge"] = None):
        self.ID = ID
        self.title = title
        self.vml_Graph = vml_Graph
        self.vml_Graph8 = vml_Graph8 if vml_Graph8 is not None else set()
        self.vml_Graph10 = vml_Graph10 if vml_Graph10 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Graph8(self):
        return self.__vml_Graph8

    @vml_Graph8.setter
    def vml_Graph8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph8", None)
        self.__vml_Graph8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Node"):
                    opp_val = getattr(item, "vml_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Node"):
                    opp_val = getattr(item, "vml_Node", None)
                    
                    setattr(item, "vml_Node", self)
                    

    @property
    def vml_Graph10(self):
        return self.__vml_Graph10

    @vml_Graph10.setter
    def vml_Graph10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph10", None)
        self.__vml_Graph10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Edge"):
                    opp_val = getattr(item, "vml_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Edge"):
                    opp_val = getattr(item, "vml_Edge", None)
                    
                    setattr(item, "vml_Edge", self)
                    

    @property
    def vml_Graph(self):
        return self.__vml_Graph

    @vml_Graph.setter
    def vml_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph", None)
        self.__vml_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Diagram4"):
                opp_val = getattr(old_value, "vml_Diagram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Diagram4"):
                opp_val = getattr(value, "vml_Diagram4", None)
                if opp_val is None:
                    setattr(value, "vml_Diagram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vml_Pie:

    def __init__(self, ID: str, title: str, vml_Pie: "vml_Diagram" = None, vml_Pie6: set["vml_Slice"] = None):
        self.ID = ID
        self.title = title
        self.vml_Pie = vml_Pie
        self.vml_Pie6 = vml_Pie6 if vml_Pie6 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Pie6(self):
        return self.__vml_Pie6

    @vml_Pie6.setter
    def vml_Pie6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Pie__vml_Pie6", None)
        self.__vml_Pie6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Slice"):
                    opp_val = getattr(item, "vml_Slice", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Slice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Slice"):
                    opp_val = getattr(item, "vml_Slice", None)
                    
                    setattr(item, "vml_Slice", self)
                    

    @property
    def vml_Pie(self):
        return self.__vml_Pie

    @vml_Pie.setter
    def vml_Pie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Pie__vml_Pie", None)
        self.__vml_Pie = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Diagram2"):
                opp_val = getattr(old_value, "vml_Diagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Diagram2"):
                opp_val = getattr(value, "vml_Diagram2", None)
                if opp_val is None:
                    setattr(value, "vml_Diagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vml_Diagram:

    def __init__(self, title: str, vml_Diagram: "vml_Model" = None, vml_Diagram2: set["vml_Pie"] = None, vml_Diagram4: set["vml_Graph"] = None):
        self.title = title
        self.vml_Diagram = vml_Diagram
        self.vml_Diagram2 = vml_Diagram2 if vml_Diagram2 is not None else set()
        self.vml_Diagram4 = vml_Diagram4 if vml_Diagram4 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Diagram(self):
        return self.__vml_Diagram

    @vml_Diagram.setter
    def vml_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Diagram__vml_Diagram", None)
        self.__vml_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Model"):
                opp_val = getattr(old_value, "vml_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Model"):
                opp_val = getattr(value, "vml_Model", None)
                if opp_val is None:
                    setattr(value, "vml_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Diagram2(self):
        return self.__vml_Diagram2

    @vml_Diagram2.setter
    def vml_Diagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Diagram__vml_Diagram2", None)
        self.__vml_Diagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Pie"):
                    opp_val = getattr(item, "vml_Pie", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Pie", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Pie"):
                    opp_val = getattr(item, "vml_Pie", None)
                    
                    setattr(item, "vml_Pie", self)
                    

    @property
    def vml_Diagram4(self):
        return self.__vml_Diagram4

    @vml_Diagram4.setter
    def vml_Diagram4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Diagram__vml_Diagram4", None)
        self.__vml_Diagram4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Graph"):
                    opp_val = getattr(item, "vml_Graph", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Graph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Graph"):
                    opp_val = getattr(item, "vml_Graph", None)
                    
                    setattr(item, "vml_Graph", self)
                    
