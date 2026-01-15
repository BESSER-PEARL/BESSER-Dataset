from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rpslPerceptionGraphMetaModel_OutputPort:

    pass
class rpslPerceptionGraphMetaModel_InputPort:

    pass
class rpslPerceptionGraphMetaModel_Connection:

    pass
class Element:

    pass
class rpslPerceptionGraphMetaModel_Node(Element):

    pass
class rpslPerceptionGraphMetaModel_Leaf(Element):

    pass
class rpslPerceptionGraphMetaModel_Component:

    pass
class rpslPerceptionGraphMetaModel_Prototype:

    pass
class rpslPerceptionGraphMetaModel_Element:

    def __init__(self, name: str, doc: str, rpslPerceptionGraphMetaModel_Element: "rpslPerceptionGraphMetaModel_PerceptionGraph" = None, rpslPerceptionGraphMetaModel_Element4: "rpslPerceptionGraphMetaModel_Component" = None, rpslPerceptionGraphMetaModel_Element8: "rpslPerceptionGraphMetaModel_Connection" = None):
        self.name = name
        self.doc = doc
        self.rpslPerceptionGraphMetaModel_Element = rpslPerceptionGraphMetaModel_Element
        self.rpslPerceptionGraphMetaModel_Element4 = rpslPerceptionGraphMetaModel_Element4
        self.rpslPerceptionGraphMetaModel_Element8 = rpslPerceptionGraphMetaModel_Element8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def rpslPerceptionGraphMetaModel_Element8(self):
        return self.__rpslPerceptionGraphMetaModel_Element8

    @rpslPerceptionGraphMetaModel_Element8.setter
    def rpslPerceptionGraphMetaModel_Element8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rpslPerceptionGraphMetaModel_Element__rpslPerceptionGraphMetaModel_Element8", None)
        self.__rpslPerceptionGraphMetaModel_Element8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rpslPerceptionGraphMetaModel_Connection7"):
                opp_val = getattr(old_value, "rpslPerceptionGraphMetaModel_Connection7", None)
                if opp_val == self:
                    setattr(old_value, "rpslPerceptionGraphMetaModel_Connection7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rpslPerceptionGraphMetaModel_Connection7"):
                opp_val = getattr(value, "rpslPerceptionGraphMetaModel_Connection7", None)
                setattr(value, "rpslPerceptionGraphMetaModel_Connection7", self)

    @property
    def rpslPerceptionGraphMetaModel_Element(self):
        return self.__rpslPerceptionGraphMetaModel_Element

    @rpslPerceptionGraphMetaModel_Element.setter
    def rpslPerceptionGraphMetaModel_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rpslPerceptionGraphMetaModel_Element__rpslPerceptionGraphMetaModel_Element", None)
        self.__rpslPerceptionGraphMetaModel_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rpslPerceptionGraphMetaModel_PerceptionGraph"):
                opp_val = getattr(old_value, "rpslPerceptionGraphMetaModel_PerceptionGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rpslPerceptionGraphMetaModel_PerceptionGraph"):
                opp_val = getattr(value, "rpslPerceptionGraphMetaModel_PerceptionGraph", None)
                if opp_val is None:
                    setattr(value, "rpslPerceptionGraphMetaModel_PerceptionGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rpslPerceptionGraphMetaModel_Element4(self):
        return self.__rpslPerceptionGraphMetaModel_Element4

    @rpslPerceptionGraphMetaModel_Element4.setter
    def rpslPerceptionGraphMetaModel_Element4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rpslPerceptionGraphMetaModel_Element__rpslPerceptionGraphMetaModel_Element4", None)
        self.__rpslPerceptionGraphMetaModel_Element4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rpslPerceptionGraphMetaModel_Component"):
                opp_val = getattr(old_value, "rpslPerceptionGraphMetaModel_Component", None)
                if opp_val == self:
                    setattr(old_value, "rpslPerceptionGraphMetaModel_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rpslPerceptionGraphMetaModel_Component"):
                opp_val = getattr(value, "rpslPerceptionGraphMetaModel_Component", None)
                setattr(value, "rpslPerceptionGraphMetaModel_Component", self)

class rpslPerceptionGraphMetaModel_PerceptionGraph:

    def __init__(self, name: str, uuid: str, doc: str, rpslPerceptionGraphMetaModel_PerceptionGraph: set["rpslPerceptionGraphMetaModel_Element"] = None, rpslPerceptionGraphMetaModel_PerceptionGraph2: set["rpslPerceptionGraphMetaModel_Prototype"] = None):
        self.name = name
        self.uuid = uuid
        self.doc = doc
        self.rpslPerceptionGraphMetaModel_PerceptionGraph = rpslPerceptionGraphMetaModel_PerceptionGraph if rpslPerceptionGraphMetaModel_PerceptionGraph is not None else set()
        self.rpslPerceptionGraphMetaModel_PerceptionGraph2 = rpslPerceptionGraphMetaModel_PerceptionGraph2 if rpslPerceptionGraphMetaModel_PerceptionGraph2 is not None else set()
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rpslPerceptionGraphMetaModel_PerceptionGraph2(self):
        return self.__rpslPerceptionGraphMetaModel_PerceptionGraph2

    @rpslPerceptionGraphMetaModel_PerceptionGraph2.setter
    def rpslPerceptionGraphMetaModel_PerceptionGraph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rpslPerceptionGraphMetaModel_PerceptionGraph__rpslPerceptionGraphMetaModel_PerceptionGraph2", None)
        self.__rpslPerceptionGraphMetaModel_PerceptionGraph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rpslPerceptionGraphMetaModel_Prototype"):
                    opp_val = getattr(item, "rpslPerceptionGraphMetaModel_Prototype", None)
                    
                    if opp_val == self:
                        setattr(item, "rpslPerceptionGraphMetaModel_Prototype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rpslPerceptionGraphMetaModel_Prototype"):
                    opp_val = getattr(item, "rpslPerceptionGraphMetaModel_Prototype", None)
                    
                    setattr(item, "rpslPerceptionGraphMetaModel_Prototype", self)
                    

    @property
    def rpslPerceptionGraphMetaModel_PerceptionGraph(self):
        return self.__rpslPerceptionGraphMetaModel_PerceptionGraph

    @rpslPerceptionGraphMetaModel_PerceptionGraph.setter
    def rpslPerceptionGraphMetaModel_PerceptionGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rpslPerceptionGraphMetaModel_PerceptionGraph__rpslPerceptionGraphMetaModel_PerceptionGraph", None)
        self.__rpslPerceptionGraphMetaModel_PerceptionGraph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rpslPerceptionGraphMetaModel_Element"):
                    opp_val = getattr(item, "rpslPerceptionGraphMetaModel_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "rpslPerceptionGraphMetaModel_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rpslPerceptionGraphMetaModel_Element"):
                    opp_val = getattr(item, "rpslPerceptionGraphMetaModel_Element", None)
                    
                    setattr(item, "rpslPerceptionGraphMetaModel_Element", self)
                    
