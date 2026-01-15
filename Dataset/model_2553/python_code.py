from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testmodel_Val:

    def __init__(self, intvl: int, valname: str, intlist: int, testmodel_Val: "testmodel_cont" = None, testmodel_Val5: "testmodel_Node" = None):
        self.intvl = intvl
        self.valname = valname
        self.intlist = intlist
        self.testmodel_Val = testmodel_Val
        self.testmodel_Val5 = testmodel_Val5
        
    @property
    def valname(self) -> str:
        return self.__valname

    @valname.setter
    def valname(self, valname: str):
        self.__valname = valname

    @property
    def intlist(self) -> int:
        return self.__intlist

    @intlist.setter
    def intlist(self, intlist: int):
        self.__intlist = intlist

    @property
    def intvl(self) -> int:
        return self.__intvl

    @intvl.setter
    def intvl(self, intvl: int):
        self.__intvl = intvl

    @property
    def testmodel_Val(self):
        return self.__testmodel_Val

    @testmodel_Val.setter
    def testmodel_Val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Val__testmodel_Val", None)
        self.__testmodel_Val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_cont2"):
                opp_val = getattr(old_value, "testmodel_cont2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_cont2"):
                opp_val = getattr(value, "testmodel_cont2", None)
                if opp_val is None:
                    setattr(value, "testmodel_cont2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_Val5(self):
        return self.__testmodel_Val5

    @testmodel_Val5.setter
    def testmodel_Val5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Val__testmodel_Val5", None)
        self.__testmodel_Val5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_Node4"):
                opp_val = getattr(old_value, "testmodel_Node4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_Node4"):
                opp_val = getattr(value, "testmodel_Node4", None)
                if opp_val is None:
                    setattr(value, "testmodel_Node4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testmodel_Node:

    def __init__(self, nodename: str, testmodel_Node: "testmodel_cont" = None, Node10: "testmodel_Node" = None, parentNode: set["testmodel_Node"] = None, testmodel_Node4: set["testmodel_Val"] = None, Node: "testmodel_Node" = None, childNodes: "testmodel_Node" = None):
        self.nodename = nodename
        self.testmodel_Node = testmodel_Node
        self.Node10 = Node10
        self.parentNode = parentNode if parentNode is not None else set()
        self.testmodel_Node4 = testmodel_Node4 if testmodel_Node4 is not None else set()
        self.Node = Node
        self.childNodes = childNodes
        
    @property
    def nodename(self) -> str:
        return self.__nodename

    @nodename.setter
    def nodename(self, nodename: str):
        self.__nodename = nodename

    @property
    def childNodes(self):
        return self.__childNodes

    @childNodes.setter
    def childNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__childNodes", None)
        self.__childNodes = value
        
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
    def Node10(self):
        return self.__Node10

    @Node10.setter
    def Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__Node10", None)
        self.__Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentNode"):
                opp_val = getattr(old_value, "parentNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentNode"):
                opp_val = getattr(value, "parentNode", None)
                if opp_val is None:
                    setattr(value, "parentNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_Node(self):
        return self.__testmodel_Node

    @testmodel_Node.setter
    def testmodel_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__testmodel_Node", None)
        self.__testmodel_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_cont"):
                opp_val = getattr(old_value, "testmodel_cont", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_cont"):
                opp_val = getattr(value, "testmodel_cont", None)
                if opp_val is None:
                    setattr(value, "testmodel_cont", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_Node4(self):
        return self.__testmodel_Node4

    @testmodel_Node4.setter
    def testmodel_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__testmodel_Node4", None)
        self.__testmodel_Node4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_Val5"):
                    opp_val = getattr(item, "testmodel_Val5", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_Val5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_Val5"):
                    opp_val = getattr(item, "testmodel_Val5", None)
                    
                    setattr(item, "testmodel_Val5", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childNodes"):
                opp_val = getattr(old_value, "childNodes", None)
                if opp_val == self:
                    setattr(old_value, "childNodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childNodes"):
                opp_val = getattr(value, "childNodes", None)
                setattr(value, "childNodes", self)

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Node__parentNode", None)
        self.__parentNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    if opp_val == self:
                        setattr(item, "Node10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    setattr(item, "Node10", self)
                    

class testmodel_cont:

    pass