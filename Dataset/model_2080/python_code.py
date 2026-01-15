from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sgf_graph_Mapping:

    def __init__(self, ID: str, sgf_graph_Mapping: set["Process"] = None, sgf_graph_Mapping25: "Processor" = None):
        self.ID = ID
        self.sgf_graph_Mapping = sgf_graph_Mapping if sgf_graph_Mapping is not None else set()
        self.sgf_graph_Mapping25 = sgf_graph_Mapping25
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_graph_Mapping25(self):
        return self.__sgf_graph_Mapping25

    @sgf_graph_Mapping25.setter
    def sgf_graph_Mapping25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_graph_Mapping__sgf_graph_Mapping25", None)
        self.__sgf_graph_Mapping25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Processor26"):
                opp_val = getattr(old_value, "Processor26", None)
                if opp_val == self:
                    setattr(old_value, "Processor26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Processor26"):
                opp_val = getattr(value, "Processor26", None)
                setattr(value, "Processor26", self)

    @property
    def sgf_graph_Mapping(self):
        return self.__sgf_graph_Mapping

    @sgf_graph_Mapping.setter
    def sgf_graph_Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_graph_Mapping__sgf_graph_Mapping", None)
        self.__sgf_graph_Mapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process23"):
                    opp_val = getattr(item, "Process23", None)
                    
                    if opp_val == self:
                        setattr(item, "Process23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process23"):
                    opp_val = getattr(item, "Process23", None)
                    
                    setattr(item, "Process23", self)
                    

class sgf_graph_Graph:

    def __init__(self, ID: str, sgf_graph_Graph: "Bundle" = None, sgf_graph_Graph19: "VM" = None, sgf_graph_Graph21: set["Mapping"] = None):
        self.ID = ID
        self.sgf_graph_Graph = sgf_graph_Graph
        self.sgf_graph_Graph19 = sgf_graph_Graph19
        self.sgf_graph_Graph21 = sgf_graph_Graph21 if sgf_graph_Graph21 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_graph_Graph21(self):
        return self.__sgf_graph_Graph21

    @sgf_graph_Graph21.setter
    def sgf_graph_Graph21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_graph_Graph__sgf_graph_Graph21", None)
        self.__sgf_graph_Graph21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Mapping"):
                    opp_val = getattr(item, "Mapping", None)
                    
                    if opp_val == self:
                        setattr(item, "Mapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Mapping"):
                    opp_val = getattr(item, "Mapping", None)
                    
                    setattr(item, "Mapping", self)
                    

    @property
    def sgf_graph_Graph(self):
        return self.__sgf_graph_Graph

    @sgf_graph_Graph.setter
    def sgf_graph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_graph_Graph__sgf_graph_Graph", None)
        self.__sgf_graph_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bundle"):
                opp_val = getattr(old_value, "Bundle", None)
                if opp_val == self:
                    setattr(old_value, "Bundle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bundle"):
                opp_val = getattr(value, "Bundle", None)
                setattr(value, "Bundle", self)

    @property
    def sgf_graph_Graph19(self):
        return self.__sgf_graph_Graph19

    @sgf_graph_Graph19.setter
    def sgf_graph_Graph19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_graph_Graph__sgf_graph_Graph19", None)
        self.__sgf_graph_Graph19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VM"):
                opp_val = getattr(old_value, "VM", None)
                if opp_val == self:
                    setattr(old_value, "VM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VM"):
                opp_val = getattr(value, "VM", None)
                setattr(value, "VM", self)

class sgf_vm_Processor:

    def __init__(self, ID: str, IP: str):
        self.ID = ID
        self.IP = IP
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def IP(self) -> str:
        return self.__IP

    @IP.setter
    def IP(self, IP: str):
        self.__IP = IP

class Mapping:

    pass
class VM:

    pass
class Bundle:

    pass
class sgf_bundle_Process:

    def __init__(self, ID: str, sgf_bundle_Process: set["Node"] = None):
        self.ID = ID
        self.sgf_bundle_Process = sgf_bundle_Process if sgf_bundle_Process is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_bundle_Process(self):
        return self.__sgf_bundle_Process

    @sgf_bundle_Process.setter
    def sgf_bundle_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_bundle_Process__sgf_bundle_Process", None)
        self.__sgf_bundle_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

class Process:

    pass
class Skeleton:

    pass
class Processor:

    pass
class sgf_vm_VM:

    def __init__(self, ID: str, protocol: str, sgf_vm_VM: set["Processor"] = None):
        self.ID = ID
        self.protocol = protocol
        self.sgf_vm_VM = sgf_vm_VM if sgf_vm_VM is not None else set()
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_vm_VM(self):
        return self.__sgf_vm_VM

    @sgf_vm_VM.setter
    def sgf_vm_VM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_vm_VM__sgf_vm_VM", None)
        self.__sgf_vm_VM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Processor"):
                    opp_val = getattr(item, "Processor", None)
                    
                    if opp_val == self:
                        setattr(item, "Processor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Processor"):
                    opp_val = getattr(item, "Processor", None)
                    
                    setattr(item, "Processor", self)
                    

class sgf_skeleton_Skeleton:

    def __init__(self, ID: str, sgf_skeleton_Skeleton: "Tree" = None, sgf_skeleton_Skeleton10: set["Root"] = None):
        self.ID = ID
        self.sgf_skeleton_Skeleton = sgf_skeleton_Skeleton
        self.sgf_skeleton_Skeleton10 = sgf_skeleton_Skeleton10 if sgf_skeleton_Skeleton10 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_skeleton_Skeleton10(self):
        return self.__sgf_skeleton_Skeleton10

    @sgf_skeleton_Skeleton10.setter
    def sgf_skeleton_Skeleton10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_skeleton_Skeleton__sgf_skeleton_Skeleton10", None)
        self.__sgf_skeleton_Skeleton10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Root11"):
                    opp_val = getattr(item, "Root11", None)
                    
                    if opp_val == self:
                        setattr(item, "Root11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Root11"):
                    opp_val = getattr(item, "Root11", None)
                    
                    setattr(item, "Root11", self)
                    

    @property
    def sgf_skeleton_Skeleton(self):
        return self.__sgf_skeleton_Skeleton

    @sgf_skeleton_Skeleton.setter
    def sgf_skeleton_Skeleton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_skeleton_Skeleton__sgf_skeleton_Skeleton", None)
        self.__sgf_skeleton_Skeleton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tree"):
                opp_val = getattr(old_value, "Tree", None)
                if opp_val == self:
                    setattr(old_value, "Tree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tree"):
                opp_val = getattr(value, "Tree", None)
                setattr(value, "Tree", self)

class sgf_tree_Node(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class sgf_bundle_Bundle:

    def __init__(self, ID: str, sgf_bundle_Bundle: "Skeleton" = None, sgf_bundle_Bundle14: set["Process"] = None):
        self.ID = ID
        self.sgf_bundle_Bundle = sgf_bundle_Bundle
        self.sgf_bundle_Bundle14 = sgf_bundle_Bundle14 if sgf_bundle_Bundle14 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_bundle_Bundle14(self):
        return self.__sgf_bundle_Bundle14

    @sgf_bundle_Bundle14.setter
    def sgf_bundle_Bundle14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_bundle_Bundle__sgf_bundle_Bundle14", None)
        self.__sgf_bundle_Bundle14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    if opp_val == self:
                        setattr(item, "Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    setattr(item, "Process", self)
                    

    @property
    def sgf_bundle_Bundle(self):
        return self.__sgf_bundle_Bundle

    @sgf_bundle_Bundle.setter
    def sgf_bundle_Bundle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_bundle_Bundle__sgf_bundle_Bundle", None)
        self.__sgf_bundle_Bundle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Skeleton"):
                opp_val = getattr(old_value, "Skeleton", None)
                if opp_val == self:
                    setattr(old_value, "Skeleton", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Skeleton"):
                opp_val = getattr(value, "Skeleton", None)
                setattr(value, "Skeleton", self)

class Tree:

    pass
class sgf_tree_Tree:

    def __init__(self, ID: str, sgf_tree_Tree: "Root" = None, sgf_tree_Tree2: set["Coordinator"] = None, sgf_tree_Tree4: set["Simulator"] = None):
        self.ID = ID
        self.sgf_tree_Tree = sgf_tree_Tree
        self.sgf_tree_Tree2 = sgf_tree_Tree2 if sgf_tree_Tree2 is not None else set()
        self.sgf_tree_Tree4 = sgf_tree_Tree4 if sgf_tree_Tree4 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def sgf_tree_Tree2(self):
        return self.__sgf_tree_Tree2

    @sgf_tree_Tree2.setter
    def sgf_tree_Tree2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_tree_Tree__sgf_tree_Tree2", None)
        self.__sgf_tree_Tree2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Coordinator"):
                    opp_val = getattr(item, "Coordinator", None)
                    
                    if opp_val == self:
                        setattr(item, "Coordinator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Coordinator"):
                    opp_val = getattr(item, "Coordinator", None)
                    
                    setattr(item, "Coordinator", self)
                    

    @property
    def sgf_tree_Tree4(self):
        return self.__sgf_tree_Tree4

    @sgf_tree_Tree4.setter
    def sgf_tree_Tree4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_tree_Tree__sgf_tree_Tree4", None)
        self.__sgf_tree_Tree4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Simulator"):
                    opp_val = getattr(item, "Simulator", None)
                    
                    if opp_val == self:
                        setattr(item, "Simulator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Simulator"):
                    opp_val = getattr(item, "Simulator", None)
                    
                    setattr(item, "Simulator", self)
                    

    @property
    def sgf_tree_Tree(self):
        return self.__sgf_tree_Tree

    @sgf_tree_Tree.setter
    def sgf_tree_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgf_tree_Tree__sgf_tree_Tree", None)
        self.__sgf_tree_Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

class BasicNode:

    pass
class sgf_tree_Coordinator(BasicNode):

    pass
class sgf_tree_Simulator(BasicNode):

    pass
class Node:

    pass
class sgf_tree_BasicNode(Node):

    def __init__(self, modelName: str, Node: "sgf_bundle_Process"):
        self.modelName = modelName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class sgf_tree_Root(Node):

    pass
class Simulator:

    pass
class Coordinator:

    pass
class Root:

    pass