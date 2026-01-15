from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mydsl_Node:

    def __init__(self, content: str, name: str, isInvisible: bool, mydsl_Node: "mydsl_Graph" = None, mydsl_Node8: "mydsl_Edge" = None, mydsl_Node11: "mydsl_Edge" = None):
        self.content = content
        self.name = name
        self.isInvisible = isInvisible
        self.mydsl_Node = mydsl_Node
        self.mydsl_Node8 = mydsl_Node8
        self.mydsl_Node11 = mydsl_Node11
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isInvisible(self) -> bool:
        return self.__isInvisible

    @isInvisible.setter
    def isInvisible(self, isInvisible: bool):
        self.__isInvisible = isInvisible

    @property
    def mydsl_Node8(self):
        return self.__mydsl_Node8

    @mydsl_Node8.setter
    def mydsl_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Node__mydsl_Node8", None)
        self.__mydsl_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Edge7"):
                opp_val = getattr(old_value, "mydsl_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Edge7"):
                opp_val = getattr(value, "mydsl_Edge7", None)
                setattr(value, "mydsl_Edge7", self)

    @property
    def mydsl_Node11(self):
        return self.__mydsl_Node11

    @mydsl_Node11.setter
    def mydsl_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Node__mydsl_Node11", None)
        self.__mydsl_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Edge10"):
                opp_val = getattr(old_value, "mydsl_Edge10", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Edge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Edge10"):
                opp_val = getattr(value, "mydsl_Edge10", None)
                setattr(value, "mydsl_Edge10", self)

    @property
    def mydsl_Node(self):
        return self.__mydsl_Node

    @mydsl_Node.setter
    def mydsl_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Node__mydsl_Node", None)
        self.__mydsl_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Graph2"):
                opp_val = getattr(old_value, "mydsl_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Graph2"):
                opp_val = getattr(value, "mydsl_Graph2", None)
                if opp_val is None:
                    setattr(value, "mydsl_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mydsl_Edge:

    def __init__(self, label: str, parsed_target: str, parsed_source: str, mydsl_Edge: "mydsl_Graph" = None, mydsl_Edge7: "mydsl_Node" = None, mydsl_Edge10: "mydsl_Node" = None):
        self.label = label
        self.parsed_target = parsed_target
        self.parsed_source = parsed_source
        self.mydsl_Edge = mydsl_Edge
        self.mydsl_Edge7 = mydsl_Edge7
        self.mydsl_Edge10 = mydsl_Edge10
        
    @property
    def parsed_source(self) -> str:
        return self.__parsed_source

    @parsed_source.setter
    def parsed_source(self, parsed_source: str):
        self.__parsed_source = parsed_source

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def parsed_target(self) -> str:
        return self.__parsed_target

    @parsed_target.setter
    def parsed_target(self, parsed_target: str):
        self.__parsed_target = parsed_target

    @property
    def mydsl_Edge7(self):
        return self.__mydsl_Edge7

    @mydsl_Edge7.setter
    def mydsl_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Edge__mydsl_Edge7", None)
        self.__mydsl_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Node8"):
                opp_val = getattr(old_value, "mydsl_Node8", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Node8"):
                opp_val = getattr(value, "mydsl_Node8", None)
                setattr(value, "mydsl_Node8", self)

    @property
    def mydsl_Edge10(self):
        return self.__mydsl_Edge10

    @mydsl_Edge10.setter
    def mydsl_Edge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Edge__mydsl_Edge10", None)
        self.__mydsl_Edge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Node11"):
                opp_val = getattr(old_value, "mydsl_Node11", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Node11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Node11"):
                opp_val = getattr(value, "mydsl_Node11", None)
                setattr(value, "mydsl_Node11", self)

    @property
    def mydsl_Edge(self):
        return self.__mydsl_Edge

    @mydsl_Edge.setter
    def mydsl_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Edge__mydsl_Edge", None)
        self.__mydsl_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Graph"):
                opp_val = getattr(old_value, "mydsl_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Graph"):
                opp_val = getattr(value, "mydsl_Graph", None)
                if opp_val is None:
                    setattr(value, "mydsl_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mydsl_Graph:

    def __init__(self, name: str, mydsl_Graph: set["mydsl_Edge"] = None, mydsl_Graph2: set["mydsl_Node"] = None, mydsl_Graph5: "mydsl_Graph" = None, mydsl_Graph3: set["mydsl_Graph"] = None):
        self.name = name
        self.mydsl_Graph = mydsl_Graph if mydsl_Graph is not None else set()
        self.mydsl_Graph2 = mydsl_Graph2 if mydsl_Graph2 is not None else set()
        self.mydsl_Graph5 = mydsl_Graph5
        self.mydsl_Graph3 = mydsl_Graph3 if mydsl_Graph3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_Graph(self):
        return self.__mydsl_Graph

    @mydsl_Graph.setter
    def mydsl_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Graph__mydsl_Graph", None)
        self.__mydsl_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_Edge"):
                    opp_val = getattr(item, "mydsl_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_Edge"):
                    opp_val = getattr(item, "mydsl_Edge", None)
                    
                    setattr(item, "mydsl_Edge", self)
                    

    @property
    def mydsl_Graph2(self):
        return self.__mydsl_Graph2

    @mydsl_Graph2.setter
    def mydsl_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Graph__mydsl_Graph2", None)
        self.__mydsl_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_Node"):
                    opp_val = getattr(item, "mydsl_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_Node"):
                    opp_val = getattr(item, "mydsl_Node", None)
                    
                    setattr(item, "mydsl_Node", self)
                    

    @property
    def mydsl_Graph5(self):
        return self.__mydsl_Graph5

    @mydsl_Graph5.setter
    def mydsl_Graph5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Graph__mydsl_Graph5", None)
        self.__mydsl_Graph5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Graph3"):
                opp_val = getattr(old_value, "mydsl_Graph3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Graph3"):
                opp_val = getattr(value, "mydsl_Graph3", None)
                if opp_val is None:
                    setattr(value, "mydsl_Graph3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mydsl_Graph3(self):
        return self.__mydsl_Graph3

    @mydsl_Graph3.setter
    def mydsl_Graph3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Graph__mydsl_Graph3", None)
        self.__mydsl_Graph3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_Graph5"):
                    opp_val = getattr(item, "mydsl_Graph5", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_Graph5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_Graph5"):
                    opp_val = getattr(item, "mydsl_Graph5", None)
                    
                    setattr(item, "mydsl_Graph5", self)
                    
