from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Graph:

    pass
class graph_Identifiable(ABC):

    def __init__(self, ID: str, number: int):
        self.ID = ID
        self.number = number
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

class Identifiable:

    pass
class graph_Node(Identifiable):

    def __init__(self, name: str, AttackerObservation: int, visited: bool, Attacker: bool, graph_Node8: "graph_GraphAsset" = None, graph_Node11: "graph_GraphAsset" = None, graph_Node: "graph_Edge" = None, graph_Node3: "graph_Edge" = None, graph_Node13: set["graph_Edge"] = None, graph_Node16: set["graph_NodeResponsibility"] = None, graph_Node18: set["graph_Edge"] = None, graph_Node21: "graph_Subgraphs" = None):
        self.name = name
        self.AttackerObservation = AttackerObservation
        self.visited = visited
        self.Attacker = Attacker
        self.graph_Node8 = graph_Node8
        self.graph_Node11 = graph_Node11
        self.graph_Node = graph_Node
        self.graph_Node3 = graph_Node3
        self.graph_Node13 = graph_Node13 if graph_Node13 is not None else set()
        self.graph_Node16 = graph_Node16 if graph_Node16 is not None else set()
        self.graph_Node18 = graph_Node18 if graph_Node18 is not None else set()
        self.graph_Node21 = graph_Node21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attacker(self) -> bool:
        return self.__Attacker

    @Attacker.setter
    def Attacker(self, Attacker: bool):
        self.__Attacker = Attacker

    @property
    def AttackerObservation(self) -> int:
        return self.__AttackerObservation

    @AttackerObservation.setter
    def AttackerObservation(self, AttackerObservation: int):
        self.__AttackerObservation = AttackerObservation

    @property
    def visited(self) -> bool:
        return self.__visited

    @visited.setter
    def visited(self, visited: bool):
        self.__visited = visited

    @property
    def graph_Node21(self):
        return self.__graph_Node21

    @graph_Node21.setter
    def graph_Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node21", None)
        self.__graph_Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Subgraphs"):
                opp_val = getattr(old_value, "graph_Subgraphs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Subgraphs"):
                opp_val = getattr(value, "graph_Subgraphs", None)
                if opp_val is None:
                    setattr(value, "graph_Subgraphs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node8(self):
        return self.__graph_Node8

    @graph_Node8.setter
    def graph_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node8", None)
        self.__graph_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GraphAsset7"):
                opp_val = getattr(old_value, "graph_GraphAsset7", None)
                if opp_val == self:
                    setattr(old_value, "graph_GraphAsset7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GraphAsset7"):
                opp_val = getattr(value, "graph_GraphAsset7", None)
                setattr(value, "graph_GraphAsset7", self)

    @property
    def graph_Node16(self):
        return self.__graph_Node16

    @graph_Node16.setter
    def graph_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node16", None)
        self.__graph_Node16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_NodeResponsibility"):
                    opp_val = getattr(item, "graph_NodeResponsibility", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_NodeResponsibility", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_NodeResponsibility"):
                    opp_val = getattr(item, "graph_NodeResponsibility", None)
                    
                    setattr(item, "graph_NodeResponsibility", self)
                    

    @property
    def graph_Node13(self):
        return self.__graph_Node13

    @graph_Node13.setter
    def graph_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node13", None)
        self.__graph_Node13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge14"):
                    opp_val = getattr(item, "graph_Edge14", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge14"):
                    opp_val = getattr(item, "graph_Edge14", None)
                    
                    setattr(item, "graph_Edge14", self)
                    

    @property
    def graph_Node18(self):
        return self.__graph_Node18

    @graph_Node18.setter
    def graph_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node18", None)
        self.__graph_Node18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge19"):
                    opp_val = getattr(item, "graph_Edge19", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge19"):
                    opp_val = getattr(item, "graph_Edge19", None)
                    
                    setattr(item, "graph_Edge19", self)
                    

    @property
    def graph_Node(self):
        return self.__graph_Node

    @graph_Node.setter
    def graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node", None)
        self.__graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge"):
                opp_val = getattr(old_value, "graph_Edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge"):
                opp_val = getattr(value, "graph_Edge", None)
                if opp_val is None:
                    setattr(value, "graph_Edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node11(self):
        return self.__graph_Node11

    @graph_Node11.setter
    def graph_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node11", None)
        self.__graph_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GraphAsset10"):
                opp_val = getattr(old_value, "graph_GraphAsset10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GraphAsset10"):
                opp_val = getattr(value, "graph_GraphAsset10", None)
                if opp_val is None:
                    setattr(value, "graph_GraphAsset10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node3(self):
        return self.__graph_Node3

    @graph_Node3.setter
    def graph_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node3", None)
        self.__graph_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge2"):
                opp_val = getattr(old_value, "graph_Edge2", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge2"):
                opp_val = getattr(value, "graph_Edge2", None)
                setattr(value, "graph_Edge2", self)

class graph_GraphAsset(Identifiable):

    def __init__(self, Encrypted: bool, Label: int, graph_GraphAsset7: "graph_Node" = None, graph_GraphAsset10: set["graph_Node"] = None, graph_GraphAsset: "graph_Edge" = None, graph_GraphAsset27: "graph_NodeResponsibility" = None, graph_GraphAsset30: "graph_NodeResponsibility" = None, graph_GraphAsset24: "graph_Subgraphs" = None):
        self.Encrypted = Encrypted
        self.Label = Label
        self.graph_GraphAsset7 = graph_GraphAsset7
        self.graph_GraphAsset10 = graph_GraphAsset10 if graph_GraphAsset10 is not None else set()
        self.graph_GraphAsset = graph_GraphAsset
        self.graph_GraphAsset27 = graph_GraphAsset27
        self.graph_GraphAsset30 = graph_GraphAsset30
        self.graph_GraphAsset24 = graph_GraphAsset24
        
    @property
    def Encrypted(self) -> bool:
        return self.__Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted: bool):
        self.__Encrypted = Encrypted

    @property
    def Label(self) -> int:
        return self.__Label

    @Label.setter
    def Label(self, Label: int):
        self.__Label = Label

    @property
    def graph_GraphAsset30(self):
        return self.__graph_GraphAsset30

    @graph_GraphAsset30.setter
    def graph_GraphAsset30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset30", None)
        self.__graph_GraphAsset30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_NodeResponsibility29"):
                opp_val = getattr(old_value, "graph_NodeResponsibility29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_NodeResponsibility29"):
                opp_val = getattr(value, "graph_NodeResponsibility29", None)
                if opp_val is None:
                    setattr(value, "graph_NodeResponsibility29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_GraphAsset(self):
        return self.__graph_GraphAsset

    @graph_GraphAsset.setter
    def graph_GraphAsset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset", None)
        self.__graph_GraphAsset = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge5"):
                opp_val = getattr(old_value, "graph_Edge5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge5"):
                opp_val = getattr(value, "graph_Edge5", None)
                if opp_val is None:
                    setattr(value, "graph_Edge5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_GraphAsset27(self):
        return self.__graph_GraphAsset27

    @graph_GraphAsset27.setter
    def graph_GraphAsset27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset27", None)
        self.__graph_GraphAsset27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_NodeResponsibility26"):
                opp_val = getattr(old_value, "graph_NodeResponsibility26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_NodeResponsibility26"):
                opp_val = getattr(value, "graph_NodeResponsibility26", None)
                if opp_val is None:
                    setattr(value, "graph_NodeResponsibility26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_GraphAsset24(self):
        return self.__graph_GraphAsset24

    @graph_GraphAsset24.setter
    def graph_GraphAsset24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset24", None)
        self.__graph_GraphAsset24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Subgraphs23"):
                opp_val = getattr(old_value, "graph_Subgraphs23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Subgraphs23"):
                opp_val = getattr(value, "graph_Subgraphs23", None)
                if opp_val is None:
                    setattr(value, "graph_Subgraphs23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_GraphAsset7(self):
        return self.__graph_GraphAsset7

    @graph_GraphAsset7.setter
    def graph_GraphAsset7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset7", None)
        self.__graph_GraphAsset7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node8"):
                opp_val = getattr(old_value, "graph_Node8", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node8"):
                opp_val = getattr(value, "graph_Node8", None)
                setattr(value, "graph_Node8", self)

    @property
    def graph_GraphAsset10(self):
        return self.__graph_GraphAsset10

    @graph_GraphAsset10.setter
    def graph_GraphAsset10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GraphAsset__graph_GraphAsset10", None)
        self.__graph_GraphAsset10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node11"):
                    opp_val = getattr(item, "graph_Node11", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node11"):
                    opp_val = getattr(item, "graph_Node11", None)
                    
                    setattr(item, "graph_Node11", self)
                    

class graph_NodeResponsibility(Identifiable):

    def __init__(self, operation: str, graph_NodeResponsibility26: set["graph_GraphAsset"] = None, graph_NodeResponsibility29: set["graph_GraphAsset"] = None, graph_NodeResponsibility: "graph_Node" = None):
        self.operation = operation
        self.graph_NodeResponsibility26 = graph_NodeResponsibility26 if graph_NodeResponsibility26 is not None else set()
        self.graph_NodeResponsibility29 = graph_NodeResponsibility29 if graph_NodeResponsibility29 is not None else set()
        self.graph_NodeResponsibility = graph_NodeResponsibility
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def graph_NodeResponsibility29(self):
        return self.__graph_NodeResponsibility29

    @graph_NodeResponsibility29.setter
    def graph_NodeResponsibility29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_NodeResponsibility__graph_NodeResponsibility29", None)
        self.__graph_NodeResponsibility29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_GraphAsset30"):
                    opp_val = getattr(item, "graph_GraphAsset30", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_GraphAsset30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_GraphAsset30"):
                    opp_val = getattr(item, "graph_GraphAsset30", None)
                    
                    setattr(item, "graph_GraphAsset30", self)
                    

    @property
    def graph_NodeResponsibility(self):
        return self.__graph_NodeResponsibility

    @graph_NodeResponsibility.setter
    def graph_NodeResponsibility(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_NodeResponsibility__graph_NodeResponsibility", None)
        self.__graph_NodeResponsibility = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node16"):
                opp_val = getattr(old_value, "graph_Node16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node16"):
                opp_val = getattr(value, "graph_Node16", None)
                if opp_val is None:
                    setattr(value, "graph_Node16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_NodeResponsibility26(self):
        return self.__graph_NodeResponsibility26

    @graph_NodeResponsibility26.setter
    def graph_NodeResponsibility26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_NodeResponsibility__graph_NodeResponsibility26", None)
        self.__graph_NodeResponsibility26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_GraphAsset27"):
                    opp_val = getattr(item, "graph_GraphAsset27", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_GraphAsset27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_GraphAsset27"):
                    opp_val = getattr(item, "graph_GraphAsset27", None)
                    
                    setattr(item, "graph_GraphAsset27", self)
                    

    def findLeastRestrictiveLabel(self) -> str:
        # TODO: Implement findLeastRestrictiveLabel method
        pass

    def findMostRestrictiveLabel(self) -> str:
        # TODO: Implement findMostRestrictiveLabel method
        pass

class graph_Subgraphs(Identifiable):

    pass
class graph_Edge(Identifiable):

    def __init__(self, EdgeLabel: int, visited: bool, graph_Edge: set["graph_Node"] = None, graph_Edge2: "graph_Node" = None, graph_Edge5: set["graph_GraphAsset"] = None, graph_Edge14: "graph_Node" = None, graph_Edge19: "graph_Node" = None):
        self.EdgeLabel = EdgeLabel
        self.visited = visited
        self.graph_Edge = graph_Edge if graph_Edge is not None else set()
        self.graph_Edge2 = graph_Edge2
        self.graph_Edge5 = graph_Edge5 if graph_Edge5 is not None else set()
        self.graph_Edge14 = graph_Edge14
        self.graph_Edge19 = graph_Edge19
        
    @property
    def visited(self) -> bool:
        return self.__visited

    @visited.setter
    def visited(self, visited: bool):
        self.__visited = visited

    @property
    def EdgeLabel(self) -> int:
        return self.__EdgeLabel

    @EdgeLabel.setter
    def EdgeLabel(self, EdgeLabel: int):
        self.__EdgeLabel = EdgeLabel

    @property
    def graph_Edge14(self):
        return self.__graph_Edge14

    @graph_Edge14.setter
    def graph_Edge14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge14", None)
        self.__graph_Edge14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node13"):
                opp_val = getattr(old_value, "graph_Node13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node13"):
                opp_val = getattr(value, "graph_Node13", None)
                if opp_val is None:
                    setattr(value, "graph_Node13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Edge(self):
        return self.__graph_Edge

    @graph_Edge.setter
    def graph_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge", None)
        self.__graph_Edge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    setattr(item, "graph_Node", self)
                    

    @property
    def graph_Edge5(self):
        return self.__graph_Edge5

    @graph_Edge5.setter
    def graph_Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge5", None)
        self.__graph_Edge5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_GraphAsset"):
                    opp_val = getattr(item, "graph_GraphAsset", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_GraphAsset", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_GraphAsset"):
                    opp_val = getattr(item, "graph_GraphAsset", None)
                    
                    setattr(item, "graph_GraphAsset", self)
                    

    @property
    def graph_Edge19(self):
        return self.__graph_Edge19

    @graph_Edge19.setter
    def graph_Edge19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge19", None)
        self.__graph_Edge19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node18"):
                opp_val = getattr(old_value, "graph_Node18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node18"):
                opp_val = getattr(value, "graph_Node18", None)
                if opp_val is None:
                    setattr(value, "graph_Node18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Edge2(self):
        return self.__graph_Edge2

    @graph_Edge2.setter
    def graph_Edge2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge2", None)
        self.__graph_Edge2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node3"):
                opp_val = getattr(old_value, "graph_Node3", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node3"):
                opp_val = getattr(value, "graph_Node3", None)
                setattr(value, "graph_Node3", self)
