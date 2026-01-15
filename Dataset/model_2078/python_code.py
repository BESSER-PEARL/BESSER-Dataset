from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class goatInfrastructure_TreeNode:

    def __init__(self, address: str, goatInfrastructure_TreeNode: "goatInfrastructure_Tree" = None, goatInfrastructure_TreeNode3: "goatInfrastructure_TreeNode" = None, goatInfrastructure_TreeNode1: set["goatInfrastructure_TreeNode"] = None):
        self.address = address
        self.goatInfrastructure_TreeNode = goatInfrastructure_TreeNode
        self.goatInfrastructure_TreeNode3 = goatInfrastructure_TreeNode3
        self.goatInfrastructure_TreeNode1 = goatInfrastructure_TreeNode1 if goatInfrastructure_TreeNode1 is not None else set()
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def goatInfrastructure_TreeNode3(self):
        return self.__goatInfrastructure_TreeNode3

    @goatInfrastructure_TreeNode3.setter
    def goatInfrastructure_TreeNode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_goatInfrastructure_TreeNode__goatInfrastructure_TreeNode3", None)
        self.__goatInfrastructure_TreeNode3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goatInfrastructure_TreeNode1"):
                opp_val = getattr(old_value, "goatInfrastructure_TreeNode1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goatInfrastructure_TreeNode1"):
                opp_val = getattr(value, "goatInfrastructure_TreeNode1", None)
                if opp_val is None:
                    setattr(value, "goatInfrastructure_TreeNode1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goatInfrastructure_TreeNode(self):
        return self.__goatInfrastructure_TreeNode

    @goatInfrastructure_TreeNode.setter
    def goatInfrastructure_TreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_goatInfrastructure_TreeNode__goatInfrastructure_TreeNode", None)
        self.__goatInfrastructure_TreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goatInfrastructure_Tree"):
                opp_val = getattr(old_value, "goatInfrastructure_Tree", None)
                if opp_val == self:
                    setattr(old_value, "goatInfrastructure_Tree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goatInfrastructure_Tree"):
                opp_val = getattr(value, "goatInfrastructure_Tree", None)
                setattr(value, "goatInfrastructure_Tree", self)

    @property
    def goatInfrastructure_TreeNode1(self):
        return self.__goatInfrastructure_TreeNode1

    @goatInfrastructure_TreeNode1.setter
    def goatInfrastructure_TreeNode1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_goatInfrastructure_TreeNode__goatInfrastructure_TreeNode1", None)
        self.__goatInfrastructure_TreeNode1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "goatInfrastructure_TreeNode3"):
                    opp_val = getattr(item, "goatInfrastructure_TreeNode3", None)
                    
                    if opp_val == self:
                        setattr(item, "goatInfrastructure_TreeNode3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "goatInfrastructure_TreeNode3"):
                    opp_val = getattr(item, "goatInfrastructure_TreeNode3", None)
                    
                    setattr(item, "goatInfrastructure_TreeNode3", self)
                    

class Infrastructure:

    pass
class goatInfrastructure_Ring(Infrastructure):

    def __init__(self, registration: str, mid_assigner: str, nodes: str):
        self.registration = registration
        self.mid_assigner = mid_assigner
        self.nodes = nodes
        
    @property
    def mid_assigner(self) -> str:
        return self.__mid_assigner

    @mid_assigner.setter
    def mid_assigner(self, mid_assigner: str):
        self.__mid_assigner = mid_assigner

    @property
    def registration(self) -> str:
        return self.__registration

    @registration.setter
    def registration(self, registration: str):
        self.__registration = registration

    @property
    def nodes(self) -> str:
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes: str):
        self.__nodes = nodes

class goatInfrastructure_Tree(Infrastructure):

    def __init__(self, registration: str, goatInfrastructure_Tree: "goatInfrastructure_TreeNode" = None):
        self.registration = registration
        self.goatInfrastructure_Tree = goatInfrastructure_Tree
        
    @property
    def registration(self) -> str:
        return self.__registration

    @registration.setter
    def registration(self, registration: str):
        self.__registration = registration

    @property
    def goatInfrastructure_Tree(self):
        return self.__goatInfrastructure_Tree

    @goatInfrastructure_Tree.setter
    def goatInfrastructure_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_goatInfrastructure_Tree__goatInfrastructure_Tree", None)
        self.__goatInfrastructure_Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goatInfrastructure_TreeNode"):
                opp_val = getattr(old_value, "goatInfrastructure_TreeNode", None)
                if opp_val == self:
                    setattr(old_value, "goatInfrastructure_TreeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goatInfrastructure_TreeNode"):
                opp_val = getattr(value, "goatInfrastructure_TreeNode", None)
                setattr(value, "goatInfrastructure_TreeNode", self)

class goatInfrastructure_Cluster(Infrastructure):

    def __init__(self, message_queue: str, registration: str, mid_assigner: str, nodes: str):
        self.message_queue = message_queue
        self.registration = registration
        self.mid_assigner = mid_assigner
        self.nodes = nodes
        
    @property
    def mid_assigner(self) -> str:
        return self.__mid_assigner

    @mid_assigner.setter
    def mid_assigner(self, mid_assigner: str):
        self.__mid_assigner = mid_assigner

    @property
    def registration(self) -> str:
        return self.__registration

    @registration.setter
    def registration(self, registration: str):
        self.__registration = registration

    @property
    def message_queue(self) -> str:
        return self.__message_queue

    @message_queue.setter
    def message_queue(self, message_queue: str):
        self.__message_queue = message_queue

    @property
    def nodes(self) -> str:
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes: str):
        self.__nodes = nodes

class goatInfrastructure_SingleServer(Infrastructure):

    def __init__(self, server: str, timeout: int):
        self.server = server
        self.timeout = timeout
        
    @property
    def server(self) -> str:
        return self.__server

    @server.setter
    def server(self, server: str):
        self.__server = server

    @property
    def timeout(self) -> int:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: int):
        self.__timeout = timeout

class goatInfrastructure_Infrastructure:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
