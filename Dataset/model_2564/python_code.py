from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class eCoreContainemntTree_EObject:

    pass
class eCoreContainemntTree_Node:

    def __init__(self, name: str, Node: "eCoreContainemntTree_Node" = None, children: set["eCoreContainemntTree_Node"] = None, Node4: "eCoreContainemntTree_Node" = None, parent: set["eCoreContainemntTree_Node"] = None, eCoreContainemntTree_Node: "eCoreContainemntTree_EObject" = None, Node8: "eCoreContainemntTree_Node" = None, superTypes: set["eCoreContainemntTree_Node"] = None, Node11: "eCoreContainemntTree_Node" = None, subTypes: set["eCoreContainemntTree_Node"] = None):
        self.name = name
        self.Node = Node
        self.children = children if children is not None else set()
        self.Node4 = Node4
        self.parent = parent if parent is not None else set()
        self.eCoreContainemntTree_Node = eCoreContainemntTree_Node
        self.Node8 = Node8
        self.superTypes = superTypes if superTypes is not None else set()
        self.Node11 = Node11
        self.subTypes = subTypes if subTypes is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superTypes(self):
        return self.__superTypes

    @superTypes.setter
    def superTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__superTypes", None)
        self.__superTypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node8"):
                    opp_val = getattr(item, "Node8", None)
                    
                    if opp_val == self:
                        setattr(item, "Node8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node8"):
                    opp_val = getattr(item, "Node8", None)
                    
                    setattr(item, "Node8", self)
                    

    @property
    def Node4(self):
        return self.__Node4

    @Node4.setter
    def Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__Node4", None)
        self.__Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node11(self):
        return self.__Node11

    @Node11.setter
    def Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__Node11", None)
        self.__Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subTypes"):
                opp_val = getattr(old_value, "subTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subTypes"):
                opp_val = getattr(value, "subTypes", None)
                if opp_val is None:
                    setattr(value, "subTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__children", None)
        self.__children = value if value is not None else set()
        
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
    def Node8(self):
        return self.__Node8

    @Node8.setter
    def Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__Node8", None)
        self.__Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superTypes"):
                opp_val = getattr(old_value, "superTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superTypes"):
                opp_val = getattr(value, "superTypes", None)
                if opp_val is None:
                    setattr(value, "superTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eCoreContainemntTree_Node(self):
        return self.__eCoreContainemntTree_Node

    @eCoreContainemntTree_Node.setter
    def eCoreContainemntTree_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__eCoreContainemntTree_Node", None)
        self.__eCoreContainemntTree_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eCoreContainemntTree_EObject"):
                opp_val = getattr(old_value, "eCoreContainemntTree_EObject", None)
                if opp_val == self:
                    setattr(old_value, "eCoreContainemntTree_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eCoreContainemntTree_EObject"):
                opp_val = getattr(value, "eCoreContainemntTree_EObject", None)
                setattr(value, "eCoreContainemntTree_EObject", self)

    @property
    def subTypes(self):
        return self.__subTypes

    @subTypes.setter
    def subTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__subTypes", None)
        self.__subTypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node11"):
                    opp_val = getattr(item, "Node11", None)
                    
                    if opp_val == self:
                        setattr(item, "Node11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node11"):
                    opp_val = getattr(item, "Node11", None)
                    
                    setattr(item, "Node11", self)
                    

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eCoreContainemntTree_Node__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node4"):
                    opp_val = getattr(item, "Node4", None)
                    
                    if opp_val == self:
                        setattr(item, "Node4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node4"):
                    opp_val = getattr(item, "Node4", None)
                    
                    setattr(item, "Node4", self)
                    
