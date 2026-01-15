from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SomeKind(Enum):
    one = "one"
    Two = "Two"
    Three = "Three"


############################################
# Definition of Classes
############################################

class PhysicalNode:

    pass
class sample_LocalNode(PhysicalNode):

    pass
class sample_RemoteNode(PhysicalNode):

    pass
class Node:

    pass
class sample_VirtualNode(Node):

    pass
class sample_PhysicalNode(Node):

    pass
class sample_Comment:

    def __init__(self, content: str, sample_Comment: "sample_Tree" = None, sample_Comment66: "sample_Node" = None):
        self.content = content
        self.sample_Comment = sample_Comment
        self.sample_Comment66 = sample_Comment66
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def sample_Comment66(self):
        return self.__sample_Comment66

    @sample_Comment66.setter
    def sample_Comment66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Comment__sample_Comment66", None)
        self.__sample_Comment66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Node"):
                opp_val = getattr(old_value, "sample_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Node"):
                opp_val = getattr(value, "sample_Node", None)
                if opp_val is None:
                    setattr(value, "sample_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Comment(self):
        return self.__sample_Comment

    @sample_Comment.setter
    def sample_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Comment__sample_Comment", None)
        self.__sample_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Tree"):
                opp_val = getattr(old_value, "sample_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Tree"):
                opp_val = getattr(value, "sample_Tree", None)
                if opp_val is None:
                    setattr(value, "sample_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Node(ABC):

    def __init__(self, label: str, childrenProxies: "sample_Node" = None, nodes: "sample_Tree" = None, Node: "sample_Tree" = None, Node52: "sample_Node" = None, parent51: set["sample_Node"] = None, Node55: "sample_Node" = None, parentProxy: set["sample_Node"] = None, Node59: "sample_Node" = None, children58: "sample_Node" = None, Node62: "sample_Node" = None, sample_Node: set["sample_Comment"] = None):
        self.label = label
        self.childrenProxies = childrenProxies
        self.nodes = nodes
        self.Node = Node
        self.Node52 = Node52
        self.parent51 = parent51 if parent51 is not None else set()
        self.Node55 = Node55
        self.parentProxy = parentProxy if parentProxy is not None else set()
        self.Node59 = Node59
        self.children58 = children58
        self.Node62 = Node62
        self.sample_Node = sample_Node if sample_Node is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tree64"):
                opp_val = getattr(old_value, "Tree64", None)
                if opp_val == self:
                    setattr(old_value, "Tree64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tree64"):
                opp_val = getattr(value, "Tree64", None)
                setattr(value, "Tree64", self)

    @property
    def children58(self):
        return self.__children58

    @children58.setter
    def children58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__children58", None)
        self.__children58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node59"):
                opp_val = getattr(old_value, "Node59", None)
                if opp_val == self:
                    setattr(old_value, "Node59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node59"):
                opp_val = getattr(value, "Node59", None)
                setattr(value, "Node59", self)

    @property
    def sample_Node(self):
        return self.__sample_Node

    @sample_Node.setter
    def sample_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__sample_Node", None)
        self.__sample_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Comment66"):
                    opp_val = getattr(item, "sample_Comment66", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Comment66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Comment66"):
                    opp_val = getattr(item, "sample_Comment66", None)
                    
                    setattr(item, "sample_Comment66", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree"):
                opp_val = getattr(old_value, "tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree"):
                opp_val = getattr(value, "tree", None)
                if opp_val is None:
                    setattr(value, "tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node52(self):
        return self.__Node52

    @Node52.setter
    def Node52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__Node52", None)
        self.__Node52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent51"):
                opp_val = getattr(old_value, "parent51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent51"):
                opp_val = getattr(value, "parent51", None)
                if opp_val is None:
                    setattr(value, "parent51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node62(self):
        return self.__Node62

    @Node62.setter
    def Node62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__Node62", None)
        self.__Node62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childrenProxies"):
                opp_val = getattr(old_value, "childrenProxies", None)
                if opp_val == self:
                    setattr(old_value, "childrenProxies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childrenProxies"):
                opp_val = getattr(value, "childrenProxies", None)
                setattr(value, "childrenProxies", self)

    @property
    def Node55(self):
        return self.__Node55

    @Node55.setter
    def Node55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__Node55", None)
        self.__Node55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentProxy"):
                opp_val = getattr(old_value, "parentProxy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentProxy"):
                opp_val = getattr(value, "parentProxy", None)
                if opp_val is None:
                    setattr(value, "parentProxy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node59(self):
        return self.__Node59

    @Node59.setter
    def Node59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__Node59", None)
        self.__Node59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children58"):
                opp_val = getattr(old_value, "children58", None)
                if opp_val == self:
                    setattr(old_value, "children58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children58"):
                opp_val = getattr(value, "children58", None)
                setattr(value, "children58", self)

    @property
    def childrenProxies(self):
        return self.__childrenProxies

    @childrenProxies.setter
    def childrenProxies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__childrenProxies", None)
        self.__childrenProxies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node62"):
                opp_val = getattr(old_value, "Node62", None)
                if opp_val == self:
                    setattr(old_value, "Node62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node62"):
                opp_val = getattr(value, "Node62", None)
                setattr(value, "Node62", self)

    @property
    def parent51(self):
        return self.__parent51

    @parent51.setter
    def parent51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__parent51", None)
        self.__parent51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node52"):
                    opp_val = getattr(item, "Node52", None)
                    
                    if opp_val == self:
                        setattr(item, "Node52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node52"):
                    opp_val = getattr(item, "Node52", None)
                    
                    setattr(item, "Node52", self)
                    

    @property
    def parentProxy(self):
        return self.__parentProxy

    @parentProxy.setter
    def parentProxy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Node__parentProxy", None)
        self.__parentProxy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node55"):
                    opp_val = getattr(item, "Node55", None)
                    
                    if opp_val == self:
                        setattr(item, "Node55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node55"):
                    opp_val = getattr(item, "Node55", None)
                    
                    setattr(item, "Node55", self)
                    

class sample_Tree:

    def __init__(self, name: str, Tree64: "sample_Node" = None, tree: set["sample_Node"] = None, Tree: "sample_Tree" = None, children: "sample_Tree" = None, Tree47: "sample_Tree" = None, parent: set["sample_Tree"] = None, sample_Tree: set["sample_Comment"] = None):
        self.name = name
        self.Tree64 = Tree64
        self.tree = tree if tree is not None else set()
        self.Tree = Tree
        self.children = children
        self.Tree47 = Tree47
        self.parent = parent if parent is not None else set()
        self.sample_Tree = sample_Tree if sample_Tree is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__children", None)
        self.__children = value
        
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

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tree47"):
                    opp_val = getattr(item, "Tree47", None)
                    
                    if opp_val == self:
                        setattr(item, "Tree47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tree47"):
                    opp_val = getattr(item, "Tree47", None)
                    
                    setattr(item, "Tree47", self)
                    

    @property
    def Tree64(self):
        return self.__Tree64

    @Tree64.setter
    def Tree64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__Tree64", None)
        self.__Tree64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def Tree47(self):
        return self.__Tree47

    @Tree47.setter
    def Tree47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__Tree47", None)
        self.__Tree47 = value
        
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
    def Tree(self):
        return self.__Tree

    @Tree.setter
    def Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__Tree", None)
        self.__Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def sample_Tree(self):
        return self.__sample_Tree

    @sample_Tree.setter
    def sample_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__sample_Tree", None)
        self.__sample_Tree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Comment"):
                    opp_val = getattr(item, "sample_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Comment"):
                    opp_val = getattr(item, "sample_Comment", None)
                    
                    setattr(item, "sample_Comment", self)
                    

    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Tree__tree", None)
        self.__tree = value if value is not None else set()
        
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
                    

class sample_TargetObject:

    def __init__(self, name: str, singleAttribute: str, manyAttributes: str, sample_TargetObject: "sample_TypeMapReference" = None, sample_TargetObject35: "sample_PrimaryObject" = None, sample_TargetObject17: "sample_PrimaryObject" = None, sample_TargetObject20: "sample_PrimaryObject" = None, sample_TargetObject23: "sample_PrimaryObject" = None, sample_TargetObject26: "sample_PrimaryObject" = None, sample_TargetObject29: "sample_PrimaryObject" = None, sample_TargetObject32: "sample_PrimaryObject" = None, sample_TargetObject37: "sample_PrimaryObject" = None, sample_TargetObject40: set["sample_PrimaryObject"] = None):
        self.name = name
        self.singleAttribute = singleAttribute
        self.manyAttributes = manyAttributes
        self.sample_TargetObject = sample_TargetObject
        self.sample_TargetObject35 = sample_TargetObject35
        self.sample_TargetObject17 = sample_TargetObject17
        self.sample_TargetObject20 = sample_TargetObject20
        self.sample_TargetObject23 = sample_TargetObject23
        self.sample_TargetObject26 = sample_TargetObject26
        self.sample_TargetObject29 = sample_TargetObject29
        self.sample_TargetObject32 = sample_TargetObject32
        self.sample_TargetObject37 = sample_TargetObject37
        self.sample_TargetObject40 = sample_TargetObject40 if sample_TargetObject40 is not None else set()
        
    @property
    def manyAttributes(self) -> str:
        return self.__manyAttributes

    @manyAttributes.setter
    def manyAttributes(self, manyAttributes: str):
        self.__manyAttributes = manyAttributes

    @property
    def singleAttribute(self) -> str:
        return self.__singleAttribute

    @singleAttribute.setter
    def singleAttribute(self, singleAttribute: str):
        self.__singleAttribute = singleAttribute

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_TargetObject32(self):
        return self.__sample_TargetObject32

    @sample_TargetObject32.setter
    def sample_TargetObject32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject32", None)
        self.__sample_TargetObject32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject31"):
                opp_val = getattr(old_value, "sample_PrimaryObject31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject31"):
                opp_val = getattr(value, "sample_PrimaryObject31", None)
                if opp_val is None:
                    setattr(value, "sample_PrimaryObject31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_TargetObject17(self):
        return self.__sample_TargetObject17

    @sample_TargetObject17.setter
    def sample_TargetObject17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject17", None)
        self.__sample_TargetObject17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject16"):
                opp_val = getattr(old_value, "sample_PrimaryObject16", None)
                if opp_val == self:
                    setattr(old_value, "sample_PrimaryObject16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject16"):
                opp_val = getattr(value, "sample_PrimaryObject16", None)
                setattr(value, "sample_PrimaryObject16", self)

    @property
    def sample_TargetObject35(self):
        return self.__sample_TargetObject35

    @sample_TargetObject35.setter
    def sample_TargetObject35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject35", None)
        self.__sample_TargetObject35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject34"):
                opp_val = getattr(old_value, "sample_PrimaryObject34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject34"):
                opp_val = getattr(value, "sample_PrimaryObject34", None)
                if opp_val is None:
                    setattr(value, "sample_PrimaryObject34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_TargetObject23(self):
        return self.__sample_TargetObject23

    @sample_TargetObject23.setter
    def sample_TargetObject23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject23", None)
        self.__sample_TargetObject23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject22"):
                opp_val = getattr(old_value, "sample_PrimaryObject22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject22"):
                opp_val = getattr(value, "sample_PrimaryObject22", None)
                if opp_val is None:
                    setattr(value, "sample_PrimaryObject22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_TargetObject40(self):
        return self.__sample_TargetObject40

    @sample_TargetObject40.setter
    def sample_TargetObject40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject40", None)
        self.__sample_TargetObject40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_PrimaryObject41"):
                    opp_val = getattr(item, "sample_PrimaryObject41", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_PrimaryObject41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_PrimaryObject41"):
                    opp_val = getattr(item, "sample_PrimaryObject41", None)
                    
                    setattr(item, "sample_PrimaryObject41", self)
                    

    @property
    def sample_TargetObject20(self):
        return self.__sample_TargetObject20

    @sample_TargetObject20.setter
    def sample_TargetObject20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject20", None)
        self.__sample_TargetObject20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject19"):
                opp_val = getattr(old_value, "sample_PrimaryObject19", None)
                if opp_val == self:
                    setattr(old_value, "sample_PrimaryObject19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject19"):
                opp_val = getattr(value, "sample_PrimaryObject19", None)
                setattr(value, "sample_PrimaryObject19", self)

    @property
    def sample_TargetObject26(self):
        return self.__sample_TargetObject26

    @sample_TargetObject26.setter
    def sample_TargetObject26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject26", None)
        self.__sample_TargetObject26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject25"):
                opp_val = getattr(old_value, "sample_PrimaryObject25", None)
                if opp_val == self:
                    setattr(old_value, "sample_PrimaryObject25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject25"):
                opp_val = getattr(value, "sample_PrimaryObject25", None)
                setattr(value, "sample_PrimaryObject25", self)

    @property
    def sample_TargetObject29(self):
        return self.__sample_TargetObject29

    @sample_TargetObject29.setter
    def sample_TargetObject29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject29", None)
        self.__sample_TargetObject29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject28"):
                opp_val = getattr(old_value, "sample_PrimaryObject28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject28"):
                opp_val = getattr(value, "sample_PrimaryObject28", None)
                if opp_val is None:
                    setattr(value, "sample_PrimaryObject28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_TargetObject37(self):
        return self.__sample_TargetObject37

    @sample_TargetObject37.setter
    def sample_TargetObject37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject37", None)
        self.__sample_TargetObject37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_PrimaryObject38"):
                opp_val = getattr(old_value, "sample_PrimaryObject38", None)
                if opp_val == self:
                    setattr(old_value, "sample_PrimaryObject38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_PrimaryObject38"):
                opp_val = getattr(value, "sample_PrimaryObject38", None)
                setattr(value, "sample_PrimaryObject38", self)

    @property
    def sample_TargetObject(self):
        return self.__sample_TargetObject

    @sample_TargetObject.setter
    def sample_TargetObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_TargetObject__sample_TargetObject", None)
        self.__sample_TargetObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TypeMapReference14"):
                opp_val = getattr(old_value, "sample_TypeMapReference14", None)
                if opp_val == self:
                    setattr(old_value, "sample_TypeMapReference14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TypeMapReference14"):
                opp_val = getattr(value, "sample_TypeMapReference14", None)
                setattr(value, "sample_TypeMapReference14", self)

class sample_PrimaryObject:

    def __init__(self, name: str, kind: str, unsettableAttribute: str, id: str, unsettableAttributeWithDefault: str, featureMapReferenceCollection: str, featureMapAttributeCollection: str, featureMapAttributeType1: str, featureMapAttributeType2: str, sample_PrimaryObject: "sample_TypeMapReference" = None, sample_PrimaryObject34: set["sample_TargetObject"] = None, sample_PrimaryObject16: "sample_TargetObject" = None, sample_PrimaryObject19: "sample_TargetObject" = None, sample_PrimaryObject22: set["sample_TargetObject"] = None, sample_PrimaryObject25: "sample_TargetObject" = None, sample_PrimaryObject28: set["sample_TargetObject"] = None, sample_PrimaryObject31: set["sample_TargetObject"] = None, sample_PrimaryObject38: "sample_TargetObject" = None, sample_PrimaryObject41: "sample_TargetObject" = None):
        self.name = name
        self.kind = kind
        self.unsettableAttribute = unsettableAttribute
        self.id = id
        self.unsettableAttributeWithDefault = unsettableAttributeWithDefault
        self.featureMapReferenceCollection = featureMapReferenceCollection
        self.featureMapAttributeCollection = featureMapAttributeCollection
        self.featureMapAttributeType1 = featureMapAttributeType1
        self.featureMapAttributeType2 = featureMapAttributeType2
        self.sample_PrimaryObject = sample_PrimaryObject
        self.sample_PrimaryObject34 = sample_PrimaryObject34 if sample_PrimaryObject34 is not None else set()
        self.sample_PrimaryObject16 = sample_PrimaryObject16
        self.sample_PrimaryObject19 = sample_PrimaryObject19
        self.sample_PrimaryObject22 = sample_PrimaryObject22 if sample_PrimaryObject22 is not None else set()
        self.sample_PrimaryObject25 = sample_PrimaryObject25
        self.sample_PrimaryObject28 = sample_PrimaryObject28 if sample_PrimaryObject28 is not None else set()
        self.sample_PrimaryObject31 = sample_PrimaryObject31 if sample_PrimaryObject31 is not None else set()
        self.sample_PrimaryObject38 = sample_PrimaryObject38
        self.sample_PrimaryObject41 = sample_PrimaryObject41
        
    @property
    def featureMapReferenceCollection(self) -> str:
        return self.__featureMapReferenceCollection

    @featureMapReferenceCollection.setter
    def featureMapReferenceCollection(self, featureMapReferenceCollection: str):
        self.__featureMapReferenceCollection = featureMapReferenceCollection

    @property
    def unsettableAttributeWithDefault(self) -> str:
        return self.__unsettableAttributeWithDefault

    @unsettableAttributeWithDefault.setter
    def unsettableAttributeWithDefault(self, unsettableAttributeWithDefault: str):
        self.__unsettableAttributeWithDefault = unsettableAttributeWithDefault

    @property
    def featureMapAttributeType1(self) -> str:
        return self.__featureMapAttributeType1

    @featureMapAttributeType1.setter
    def featureMapAttributeType1(self, featureMapAttributeType1: str):
        self.__featureMapAttributeType1 = featureMapAttributeType1

    @property
    def unsettableAttribute(self) -> str:
        return self.__unsettableAttribute

    @unsettableAttribute.setter
    def unsettableAttribute(self, unsettableAttribute: str):
        self.__unsettableAttribute = unsettableAttribute

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def featureMapAttributeType2(self) -> str:
        return self.__featureMapAttributeType2

    @featureMapAttributeType2.setter
    def featureMapAttributeType2(self, featureMapAttributeType2: str):
        self.__featureMapAttributeType2 = featureMapAttributeType2

    @property
    def featureMapAttributeCollection(self) -> str:
        return self.__featureMapAttributeCollection

    @featureMapAttributeCollection.setter
    def featureMapAttributeCollection(self, featureMapAttributeCollection: str):
        self.__featureMapAttributeCollection = featureMapAttributeCollection

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_PrimaryObject41(self):
        return self.__sample_PrimaryObject41

    @sample_PrimaryObject41.setter
    def sample_PrimaryObject41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject41", None)
        self.__sample_PrimaryObject41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TargetObject40"):
                opp_val = getattr(old_value, "sample_TargetObject40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TargetObject40"):
                opp_val = getattr(value, "sample_TargetObject40", None)
                if opp_val is None:
                    setattr(value, "sample_TargetObject40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_PrimaryObject16(self):
        return self.__sample_PrimaryObject16

    @sample_PrimaryObject16.setter
    def sample_PrimaryObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject16", None)
        self.__sample_PrimaryObject16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TargetObject17"):
                opp_val = getattr(old_value, "sample_TargetObject17", None)
                if opp_val == self:
                    setattr(old_value, "sample_TargetObject17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TargetObject17"):
                opp_val = getattr(value, "sample_TargetObject17", None)
                setattr(value, "sample_TargetObject17", self)

    @property
    def sample_PrimaryObject19(self):
        return self.__sample_PrimaryObject19

    @sample_PrimaryObject19.setter
    def sample_PrimaryObject19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject19", None)
        self.__sample_PrimaryObject19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TargetObject20"):
                opp_val = getattr(old_value, "sample_TargetObject20", None)
                if opp_val == self:
                    setattr(old_value, "sample_TargetObject20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TargetObject20"):
                opp_val = getattr(value, "sample_TargetObject20", None)
                setattr(value, "sample_TargetObject20", self)

    @property
    def sample_PrimaryObject38(self):
        return self.__sample_PrimaryObject38

    @sample_PrimaryObject38.setter
    def sample_PrimaryObject38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject38", None)
        self.__sample_PrimaryObject38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TargetObject37"):
                opp_val = getattr(old_value, "sample_TargetObject37", None)
                if opp_val == self:
                    setattr(old_value, "sample_TargetObject37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TargetObject37"):
                opp_val = getattr(value, "sample_TargetObject37", None)
                setattr(value, "sample_TargetObject37", self)

    @property
    def sample_PrimaryObject(self):
        return self.__sample_PrimaryObject

    @sample_PrimaryObject.setter
    def sample_PrimaryObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject", None)
        self.__sample_PrimaryObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TypeMapReference12"):
                opp_val = getattr(old_value, "sample_TypeMapReference12", None)
                if opp_val == self:
                    setattr(old_value, "sample_TypeMapReference12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TypeMapReference12"):
                opp_val = getattr(value, "sample_TypeMapReference12", None)
                setattr(value, "sample_TypeMapReference12", self)

    @property
    def sample_PrimaryObject22(self):
        return self.__sample_PrimaryObject22

    @sample_PrimaryObject22.setter
    def sample_PrimaryObject22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject22", None)
        self.__sample_PrimaryObject22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TargetObject23"):
                    opp_val = getattr(item, "sample_TargetObject23", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TargetObject23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TargetObject23"):
                    opp_val = getattr(item, "sample_TargetObject23", None)
                    
                    setattr(item, "sample_TargetObject23", self)
                    

    @property
    def sample_PrimaryObject34(self):
        return self.__sample_PrimaryObject34

    @sample_PrimaryObject34.setter
    def sample_PrimaryObject34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject34", None)
        self.__sample_PrimaryObject34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TargetObject35"):
                    opp_val = getattr(item, "sample_TargetObject35", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TargetObject35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TargetObject35"):
                    opp_val = getattr(item, "sample_TargetObject35", None)
                    
                    setattr(item, "sample_TargetObject35", self)
                    

    @property
    def sample_PrimaryObject28(self):
        return self.__sample_PrimaryObject28

    @sample_PrimaryObject28.setter
    def sample_PrimaryObject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject28", None)
        self.__sample_PrimaryObject28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TargetObject29"):
                    opp_val = getattr(item, "sample_TargetObject29", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TargetObject29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TargetObject29"):
                    opp_val = getattr(item, "sample_TargetObject29", None)
                    
                    setattr(item, "sample_TargetObject29", self)
                    

    @property
    def sample_PrimaryObject31(self):
        return self.__sample_PrimaryObject31

    @sample_PrimaryObject31.setter
    def sample_PrimaryObject31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject31", None)
        self.__sample_PrimaryObject31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TargetObject32"):
                    opp_val = getattr(item, "sample_TargetObject32", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TargetObject32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TargetObject32"):
                    opp_val = getattr(item, "sample_TargetObject32", None)
                    
                    setattr(item, "sample_TargetObject32", self)
                    

    @property
    def sample_PrimaryObject25(self):
        return self.__sample_PrimaryObject25

    @sample_PrimaryObject25.setter
    def sample_PrimaryObject25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_PrimaryObject__sample_PrimaryObject25", None)
        self.__sample_PrimaryObject25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TargetObject26"):
                opp_val = getattr(old_value, "sample_TargetObject26", None)
                if opp_val == self:
                    setattr(old_value, "sample_TargetObject26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TargetObject26"):
                opp_val = getattr(value, "sample_TargetObject26", None)
                setattr(value, "sample_TargetObject26", self)

class sample_Value:

    def __init__(self, value: int, sample_Value: "sample_TypeMap" = None):
        self.value = value
        self.sample_Value = sample_Value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def sample_Value(self):
        return self.__sample_Value

    @sample_Value.setter
    def sample_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Value__sample_Value", None)
        self.__sample_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TypeMap10"):
                opp_val = getattr(old_value, "sample_TypeMap10", None)
                if opp_val == self:
                    setattr(old_value, "sample_TypeMap10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TypeMap10"):
                opp_val = getattr(value, "sample_TypeMap10", None)
                setattr(value, "sample_TypeMap10", self)

class sample_Type:

    def __init__(self, name: str, sample_Type: "sample_TypeMap" = None):
        self.name = name
        self.sample_Type = sample_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sample_Type(self):
        return self.__sample_Type

    @sample_Type.setter
    def sample_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Type__sample_Type", None)
        self.__sample_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_TypeMap8"):
                opp_val = getattr(old_value, "sample_TypeMap8", None)
                if opp_val == self:
                    setattr(old_value, "sample_TypeMap8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_TypeMap8"):
                opp_val = getattr(value, "sample_TypeMap8", None)
                setattr(value, "sample_TypeMap8", self)

class sample_DataTypeMap:

    def __init__(self, key: str, value: str, sample_DataTypeMap: "sample_ETypes" = None):
        self.key = key
        self.value = value
        self.sample_DataTypeMap = sample_DataTypeMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def sample_DataTypeMap(self):
        return self.__sample_DataTypeMap

    @sample_DataTypeMap.setter
    def sample_DataTypeMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_DataTypeMap__sample_DataTypeMap", None)
        self.__sample_DataTypeMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_ETypes6"):
                opp_val = getattr(old_value, "sample_ETypes6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_ETypes6"):
                opp_val = getattr(value, "sample_ETypes6", None)
                if opp_val is None:
                    setattr(value, "sample_ETypes6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_StringMap:

    def __init__(self, value: str, key: str, sample_StringMap: "sample_ETypes" = None):
        self.value = value
        self.key = key
        self.sample_StringMap = sample_StringMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def sample_StringMap(self):
        return self.__sample_StringMap

    @sample_StringMap.setter
    def sample_StringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_StringMap__sample_StringMap", None)
        self.__sample_StringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_ETypes4"):
                opp_val = getattr(old_value, "sample_ETypes4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_ETypes4"):
                opp_val = getattr(value, "sample_ETypes4", None)
                if opp_val is None:
                    setattr(value, "sample_ETypes4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_TypeMapReference:

    pass
class sample_TypeMap:

    pass
class sample_ETypes:

    def __init__(self, uris: str, sample_ETypes: set["sample_TypeMap"] = None, sample_ETypes2: set["sample_TypeMapReference"] = None, sample_ETypes4: set["sample_StringMap"] = None, sample_ETypes6: set["sample_DataTypeMap"] = None):
        self.uris = uris
        self.sample_ETypes = sample_ETypes if sample_ETypes is not None else set()
        self.sample_ETypes2 = sample_ETypes2 if sample_ETypes2 is not None else set()
        self.sample_ETypes4 = sample_ETypes4 if sample_ETypes4 is not None else set()
        self.sample_ETypes6 = sample_ETypes6 if sample_ETypes6 is not None else set()
        
    @property
    def uris(self) -> str:
        return self.__uris

    @uris.setter
    def uris(self, uris: str):
        self.__uris = uris

    @property
    def sample_ETypes4(self):
        return self.__sample_ETypes4

    @sample_ETypes4.setter
    def sample_ETypes4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_ETypes__sample_ETypes4", None)
        self.__sample_ETypes4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_StringMap"):
                    opp_val = getattr(item, "sample_StringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_StringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_StringMap"):
                    opp_val = getattr(item, "sample_StringMap", None)
                    
                    setattr(item, "sample_StringMap", self)
                    

    @property
    def sample_ETypes(self):
        return self.__sample_ETypes

    @sample_ETypes.setter
    def sample_ETypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_ETypes__sample_ETypes", None)
        self.__sample_ETypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TypeMap"):
                    opp_val = getattr(item, "sample_TypeMap", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TypeMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TypeMap"):
                    opp_val = getattr(item, "sample_TypeMap", None)
                    
                    setattr(item, "sample_TypeMap", self)
                    

    @property
    def sample_ETypes2(self):
        return self.__sample_ETypes2

    @sample_ETypes2.setter
    def sample_ETypes2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_ETypes__sample_ETypes2", None)
        self.__sample_ETypes2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_TypeMapReference"):
                    opp_val = getattr(item, "sample_TypeMapReference", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_TypeMapReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_TypeMapReference"):
                    opp_val = getattr(item, "sample_TypeMapReference", None)
                    
                    setattr(item, "sample_TypeMapReference", self)
                    

    @property
    def sample_ETypes6(self):
        return self.__sample_ETypes6

    @sample_ETypes6.setter
    def sample_ETypes6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_ETypes__sample_ETypes6", None)
        self.__sample_ETypes6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_DataTypeMap"):
                    opp_val = getattr(item, "sample_DataTypeMap", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_DataTypeMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_DataTypeMap"):
                    opp_val = getattr(item, "sample_DataTypeMap", None)
                    
                    setattr(item, "sample_DataTypeMap", self)
                    
