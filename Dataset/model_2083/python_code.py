from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ws_bundle_Process:

    def __init__(self, ID: str, ws_bundle_Process: set["Node"] = None, ws_bundle_Process27: "Middleware" = None):
        self.ID = ID
        self.ws_bundle_Process = ws_bundle_Process if ws_bundle_Process is not None else set()
        self.ws_bundle_Process27 = ws_bundle_Process27
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ws_bundle_Process(self):
        return self.__ws_bundle_Process

    @ws_bundle_Process.setter
    def ws_bundle_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_bundle_Process__ws_bundle_Process", None)
        self.__ws_bundle_Process = value if value is not None else set()
        
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
    def ws_bundle_Process27(self):
        return self.__ws_bundle_Process27

    @ws_bundle_Process27.setter
    def ws_bundle_Process27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_bundle_Process__ws_bundle_Process27", None)
        self.__ws_bundle_Process27 = value
        
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

    def receive(self):
        # TODO: Implement receive method
        pass

class Skeleton:

    pass
class ws_bundle_Bundle:

    def __init__(self, ID: str, ws_bundle_Bundle: "Skeleton" = None, ws_bundle_Bundle23: set["Process"] = None):
        self.ID = ID
        self.ws_bundle_Bundle = ws_bundle_Bundle
        self.ws_bundle_Bundle23 = ws_bundle_Bundle23 if ws_bundle_Bundle23 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ws_bundle_Bundle(self):
        return self.__ws_bundle_Bundle

    @ws_bundle_Bundle.setter
    def ws_bundle_Bundle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_bundle_Bundle__ws_bundle_Bundle", None)
        self.__ws_bundle_Bundle = value
        
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
    def ws_bundle_Bundle23(self):
        return self.__ws_bundle_Bundle23

    @ws_bundle_Bundle23.setter
    def ws_bundle_Bundle23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_bundle_Bundle__ws_bundle_Bundle23", None)
        self.__ws_bundle_Bundle23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process24"):
                    opp_val = getattr(item, "Process24", None)
                    
                    if opp_val == self:
                        setattr(item, "Process24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process24"):
                    opp_val = getattr(item, "Process24", None)
                    
                    setattr(item, "Process24", self)
                    

class Tree:

    pass
class ws_skeleton_Skeleton:

    def __init__(self, ID: str, ws_skeleton_Skeleton: "Tree" = None, ws_skeleton_Skeleton19: set["Root"] = None):
        self.ID = ID
        self.ws_skeleton_Skeleton = ws_skeleton_Skeleton
        self.ws_skeleton_Skeleton19 = ws_skeleton_Skeleton19 if ws_skeleton_Skeleton19 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ws_skeleton_Skeleton19(self):
        return self.__ws_skeleton_Skeleton19

    @ws_skeleton_Skeleton19.setter
    def ws_skeleton_Skeleton19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_skeleton_Skeleton__ws_skeleton_Skeleton19", None)
        self.__ws_skeleton_Skeleton19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Root20"):
                    opp_val = getattr(item, "Root20", None)
                    
                    if opp_val == self:
                        setattr(item, "Root20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Root20"):
                    opp_val = getattr(item, "Root20", None)
                    
                    setattr(item, "Root20", self)
                    

    @property
    def ws_skeleton_Skeleton(self):
        return self.__ws_skeleton_Skeleton

    @ws_skeleton_Skeleton.setter
    def ws_skeleton_Skeleton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_skeleton_Skeleton__ws_skeleton_Skeleton", None)
        self.__ws_skeleton_Skeleton = value
        
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

class ws_tree_Node(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class BasicNode:

    pass
class ws_tree_Coordinator(BasicNode):

    pass
class Node:

    pass
class ws_tree_BasicNode(Node):

    def __init__(self, modelName: str, Node: "ws_bundle_Process"):
        self.modelName = modelName
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class ws_tree_Root(Node):

    pass
class Simulator:

    pass
class ws_tree_PDEVSSimulator(Simulator):

    pass
class ws_tree_P_Simulator(Simulator):

    pass
class ws_tree_CDEVSSimulator(Simulator):

    pass
class ws_tree_Simulator(BasicNode):

    pass
class Root:

    pass
class ws_tree_Tree:

    def __init__(self, ID: str, ws_tree_Tree: "Root" = None, ws_tree_Tree11: set["Coordinator"] = None, ws_tree_Tree13: set["Simulator"] = None):
        self.ID = ID
        self.ws_tree_Tree = ws_tree_Tree
        self.ws_tree_Tree11 = ws_tree_Tree11 if ws_tree_Tree11 is not None else set()
        self.ws_tree_Tree13 = ws_tree_Tree13 if ws_tree_Tree13 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ws_tree_Tree13(self):
        return self.__ws_tree_Tree13

    @ws_tree_Tree13.setter
    def ws_tree_Tree13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_tree_Tree__ws_tree_Tree13", None)
        self.__ws_tree_Tree13 = value if value is not None else set()
        
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
    def ws_tree_Tree11(self):
        return self.__ws_tree_Tree11

    @ws_tree_Tree11.setter
    def ws_tree_Tree11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_tree_Tree__ws_tree_Tree11", None)
        self.__ws_tree_Tree11 = value if value is not None else set()
        
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
    def ws_tree_Tree(self):
        return self.__ws_tree_Tree

    @ws_tree_Tree.setter
    def ws_tree_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_tree_Tree__ws_tree_Tree", None)
        self.__ws_tree_Tree = value
        
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

class ws_middleware_ServiceDescription(ABC):

    pass
class ws_middleware_Repository:

    def __init__(self, ws_middleware_Repository: set["ServiceDescription"] = None):
        self.ws_middleware_Repository = ws_middleware_Repository if ws_middleware_Repository is not None else set()
        
    @property
    def ws_middleware_Repository(self):
        return self.__ws_middleware_Repository

    @ws_middleware_Repository.setter
    def ws_middleware_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_middleware_Repository__ws_middleware_Repository", None)
        self.__ws_middleware_Repository = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceDescription"):
                    opp_val = getattr(item, "ServiceDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceDescription"):
                    opp_val = getattr(item, "ServiceDescription", None)
                    
                    setattr(item, "ServiceDescription", self)
                    

    def lookup(self):
        # TODO: Implement lookup method
        pass

    def rebind(self):
        # TODO: Implement rebind method
        pass

class ServiceImpl:

    pass
class ws_middleware_Stub:

    def __init__(self, ws_middleware_Stub: "ServiceImpl" = None):
        self.ws_middleware_Stub = ws_middleware_Stub
        
    @property
    def ws_middleware_Stub(self):
        return self.__ws_middleware_Stub

    @ws_middleware_Stub.setter
    def ws_middleware_Stub(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_middleware_Stub__ws_middleware_Stub", None)
        self.__ws_middleware_Stub = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceImpl"):
                opp_val = getattr(old_value, "ServiceImpl", None)
                if opp_val == self:
                    setattr(old_value, "ServiceImpl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceImpl"):
                opp_val = getattr(value, "ServiceImpl", None)
                setattr(value, "ServiceImpl", self)

    def receive(self):
        # TODO: Implement receive method
        pass

class ServiceDescription:

    pass
class ws_middleware_ServiceImpl(ServiceDescription):

    def __init__(self, ServiceDescription: "ws_middleware_Repository"):
        
    def receive(self):
        # TODO: Implement receive method
        pass

class ws_middleware_Processor:

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

    def receive(self):
        # TODO: Implement receive method
        pass

class Coordinator:

    pass
class ws_tree_CDEVSCoordinator(Coordinator):

    pass
class ws_tree_PDEVSCoordinator(Coordinator):

    pass
class ws_tree_FlatCoordinator(Coordinator):

    pass
class ws_tree_NodeCoordinator(Coordinator):

    pass
class ws_tree_P_Coordinator(Coordinator):

    pass
class ws_middleware_VM:

    def __init__(self, ID: str, protocol: str, ws_middleware_VM: set["Processor"] = None):
        self.ID = ID
        self.protocol = protocol
        self.ws_middleware_VM = ws_middleware_VM if ws_middleware_VM is not None else set()
        
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

    @property
    def ws_middleware_VM(self):
        return self.__ws_middleware_VM

    @ws_middleware_VM.setter
    def ws_middleware_VM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_middleware_VM__ws_middleware_VM", None)
        self.__ws_middleware_VM = value if value is not None else set()
        
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
                    

class Repository:

    pass
class Stub:

    pass
class Middleware:

    pass
class ws_middleware_WebService(Middleware):

    pass
class Process:

    pass
class VM:

    pass
class ws_middleware_Middleware(ABC):

    def __init__(self, ws_middleware_Middleware: "VM" = None, ws_middleware_Middleware2: set["Process"] = None):
        self.ws_middleware_Middleware = ws_middleware_Middleware
        self.ws_middleware_Middleware2 = ws_middleware_Middleware2 if ws_middleware_Middleware2 is not None else set()
        
    @property
    def ws_middleware_Middleware2(self):
        return self.__ws_middleware_Middleware2

    @ws_middleware_Middleware2.setter
    def ws_middleware_Middleware2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_middleware_Middleware__ws_middleware_Middleware2", None)
        self.__ws_middleware_Middleware2 = value if value is not None else set()
        
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
    def ws_middleware_Middleware(self):
        return self.__ws_middleware_Middleware

    @ws_middleware_Middleware.setter
    def ws_middleware_Middleware(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ws_middleware_Middleware__ws_middleware_Middleware", None)
        self.__ws_middleware_Middleware = value
        
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

    def establish(self):
        # TODO: Implement establish method
        pass

    def bind(self):
        # TODO: Implement bind method
        pass

    def send(self):
        # TODO: Implement send method
        pass

class Processor:

    pass