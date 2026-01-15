from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rsgf_vm_VM:

    def __init__(self, ID: str, protocol: str):
        self.ID = ID
        self.protocol = protocol
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

class VM:

    pass
class rsgf_mw_Middleware:

    def __init__(self, rsgf_mw_Middleware: set["Process"] = None, rsgf_mw_Middleware21: "VM" = None):
        self.rsgf_mw_Middleware = rsgf_mw_Middleware if rsgf_mw_Middleware is not None else set()
        self.rsgf_mw_Middleware21 = rsgf_mw_Middleware21
        
    @property
    def rsgf_mw_Middleware21(self):
        return self.__rsgf_mw_Middleware21

    @rsgf_mw_Middleware21.setter
    def rsgf_mw_Middleware21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_mw_Middleware__rsgf_mw_Middleware21", None)
        self.__rsgf_mw_Middleware21 = value
        
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

    @property
    def rsgf_mw_Middleware(self):
        return self.__rsgf_mw_Middleware

    @rsgf_mw_Middleware.setter
    def rsgf_mw_Middleware(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_mw_Middleware__rsgf_mw_Middleware", None)
        self.__rsgf_mw_Middleware = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process19"):
                    opp_val = getattr(item, "Process19", None)
                    
                    if opp_val == self:
                        setattr(item, "Process19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process19"):
                    opp_val = getattr(item, "Process19", None)
                    
                    setattr(item, "Process19", self)
                    

    def send(self):
        # TODO: Implement send method
        pass

    def bind(self):
        # TODO: Implement bind method
        pass

    def establish(self):
        # TODO: Implement establish method
        pass

class rsgf_bundle_Bundle:

    def __init__(self, ID: str, rsgf_bundle_Bundle: "Skeleton" = None, rsgf_bundle_Bundle14: set["Process"] = None):
        self.ID = ID
        self.rsgf_bundle_Bundle = rsgf_bundle_Bundle
        self.rsgf_bundle_Bundle14 = rsgf_bundle_Bundle14 if rsgf_bundle_Bundle14 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def rsgf_bundle_Bundle(self):
        return self.__rsgf_bundle_Bundle

    @rsgf_bundle_Bundle.setter
    def rsgf_bundle_Bundle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_bundle_Bundle__rsgf_bundle_Bundle", None)
        self.__rsgf_bundle_Bundle = value
        
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

    @property
    def rsgf_bundle_Bundle14(self):
        return self.__rsgf_bundle_Bundle14

    @rsgf_bundle_Bundle14.setter
    def rsgf_bundle_Bundle14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_bundle_Bundle__rsgf_bundle_Bundle14", None)
        self.__rsgf_bundle_Bundle14 = value if value is not None else set()
        
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
                    

class Middleware:

    pass
class rsgf_bundle_Process:

    def __init__(self, ID: str, rsgf_bundle_Process: set["Node"] = None, rsgf_bundle_Process17: "Middleware" = None):
        self.ID = ID
        self.rsgf_bundle_Process = rsgf_bundle_Process if rsgf_bundle_Process is not None else set()
        self.rsgf_bundle_Process17 = rsgf_bundle_Process17
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def rsgf_bundle_Process(self):
        return self.__rsgf_bundle_Process

    @rsgf_bundle_Process.setter
    def rsgf_bundle_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_bundle_Process__rsgf_bundle_Process", None)
        self.__rsgf_bundle_Process = value if value is not None else set()
        
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
                    

    @property
    def rsgf_bundle_Process17(self):
        return self.__rsgf_bundle_Process17

    @rsgf_bundle_Process17.setter
    def rsgf_bundle_Process17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_bundle_Process__rsgf_bundle_Process17", None)
        self.__rsgf_bundle_Process17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Middleware"):
                opp_val = getattr(old_value, "Middleware", None)
                if opp_val == self:
                    setattr(old_value, "Middleware", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Middleware"):
                opp_val = getattr(value, "Middleware", None)
                setattr(value, "Middleware", self)

class Process:

    pass
class Skeleton:

    pass
class Tree:

    pass
class rsgf_skeleton_Skeleton:

    def __init__(self, ID: str, rsgf_skeleton_Skeleton: "Tree" = None, rsgf_skeleton_Skeleton10: set["Root"] = None):
        self.ID = ID
        self.rsgf_skeleton_Skeleton = rsgf_skeleton_Skeleton
        self.rsgf_skeleton_Skeleton10 = rsgf_skeleton_Skeleton10 if rsgf_skeleton_Skeleton10 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def rsgf_skeleton_Skeleton10(self):
        return self.__rsgf_skeleton_Skeleton10

    @rsgf_skeleton_Skeleton10.setter
    def rsgf_skeleton_Skeleton10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_skeleton_Skeleton__rsgf_skeleton_Skeleton10", None)
        self.__rsgf_skeleton_Skeleton10 = value if value is not None else set()
        
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
    def rsgf_skeleton_Skeleton(self):
        return self.__rsgf_skeleton_Skeleton

    @rsgf_skeleton_Skeleton.setter
    def rsgf_skeleton_Skeleton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_skeleton_Skeleton__rsgf_skeleton_Skeleton", None)
        self.__rsgf_skeleton_Skeleton = value
        
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

class rsgf_tree_Node(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class Simulator:

    pass
class rsgf_tree_CDEVSSimulator(Simulator):

    pass
class rsgf_tree_PDEVSSimulator(Simulator):

    pass
class rsgf_tree_P_Simulator(Simulator):

    pass
class Coordinator:

    pass
class rsgf_tree_NodeCoordinator(Coordinator):

    pass
class rsgf_tree_PDEVSCoordinator(Coordinator):

    pass
class rsgf_tree_FlatCoordinator(Coordinator):

    pass
class rsgf_tree_P_Coordinator(Coordinator):

    pass
class rsgf_tree_CDEVSCoordinator(Coordinator):

    pass
class BasicNode:

    pass
class rsgf_tree_Simulator(BasicNode):

    pass
class rsgf_tree_Coordinator(BasicNode):

    pass
class Node:

    pass
class rsgf_tree_BasicNode(Node):

    def __init__(self, modelName: str, Node: "rsgf_bundle_Process"):
        self.modelName = modelName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class rsgf_tree_Root(Node):

    pass
class Root:

    pass
class rsgf_tree_Tree:

    def __init__(self, ID: str, rsgf_tree_Tree: "Root" = None, rsgf_tree_Tree2: set["Coordinator"] = None, rsgf_tree_Tree4: set["Simulator"] = None):
        self.ID = ID
        self.rsgf_tree_Tree = rsgf_tree_Tree
        self.rsgf_tree_Tree2 = rsgf_tree_Tree2 if rsgf_tree_Tree2 is not None else set()
        self.rsgf_tree_Tree4 = rsgf_tree_Tree4 if rsgf_tree_Tree4 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def rsgf_tree_Tree4(self):
        return self.__rsgf_tree_Tree4

    @rsgf_tree_Tree4.setter
    def rsgf_tree_Tree4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_tree_Tree__rsgf_tree_Tree4", None)
        self.__rsgf_tree_Tree4 = value if value is not None else set()
        
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
    def rsgf_tree_Tree2(self):
        return self.__rsgf_tree_Tree2

    @rsgf_tree_Tree2.setter
    def rsgf_tree_Tree2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_tree_Tree__rsgf_tree_Tree2", None)
        self.__rsgf_tree_Tree2 = value if value is not None else set()
        
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
    def rsgf_tree_Tree(self):
        return self.__rsgf_tree_Tree

    @rsgf_tree_Tree.setter
    def rsgf_tree_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rsgf_tree_Tree__rsgf_tree_Tree", None)
        self.__rsgf_tree_Tree = value
        
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
