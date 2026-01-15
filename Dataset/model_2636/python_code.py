from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model3_Image:

    def __init__(self, width: int, height: int, data: str):
        self.width = width
        self.height = height
        self.data = data
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class subpackage_model3_Class1:

    pass
class model3_subpackage_Class2:

    pass
class model3_ClassWithIDAttribute:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class model3_File:

    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model3_NodeD:

    def __init__(self, name: str, NodeD: "model3_NodeD" = None, parent31: set["model3_NodeD"] = None, NodeD35: "model3_NodeD" = None, children34: "model3_NodeD" = None, NodeD38: "model3_NodeD" = None, oppositeNode: set["model3_NodeD"] = None, NodeD42: "model3_NodeD" = None, otherNodes41: "model3_NodeD" = None):
        self.name = name
        self.NodeD = NodeD
        self.parent31 = parent31 if parent31 is not None else set()
        self.NodeD35 = NodeD35
        self.children34 = children34
        self.NodeD38 = NodeD38
        self.oppositeNode = oppositeNode if oppositeNode is not None else set()
        self.NodeD42 = NodeD42
        self.otherNodes41 = otherNodes41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NodeD35(self):
        return self.__NodeD35

    @NodeD35.setter
    def NodeD35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__NodeD35", None)
        self.__NodeD35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children34"):
                opp_val = getattr(old_value, "children34", None)
                if opp_val == self:
                    setattr(old_value, "children34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children34"):
                opp_val = getattr(value, "children34", None)
                setattr(value, "children34", self)

    @property
    def children34(self):
        return self.__children34

    @children34.setter
    def children34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__children34", None)
        self.__children34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeD35"):
                opp_val = getattr(old_value, "NodeD35", None)
                if opp_val == self:
                    setattr(old_value, "NodeD35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeD35"):
                opp_val = getattr(value, "NodeD35", None)
                setattr(value, "NodeD35", self)

    @property
    def NodeD42(self):
        return self.__NodeD42

    @NodeD42.setter
    def NodeD42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__NodeD42", None)
        self.__NodeD42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "otherNodes41"):
                opp_val = getattr(old_value, "otherNodes41", None)
                if opp_val == self:
                    setattr(old_value, "otherNodes41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "otherNodes41"):
                opp_val = getattr(value, "otherNodes41", None)
                setattr(value, "otherNodes41", self)

    @property
    def otherNodes41(self):
        return self.__otherNodes41

    @otherNodes41.setter
    def otherNodes41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__otherNodes41", None)
        self.__otherNodes41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeD42"):
                opp_val = getattr(old_value, "NodeD42", None)
                if opp_val == self:
                    setattr(old_value, "NodeD42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeD42"):
                opp_val = getattr(value, "NodeD42", None)
                setattr(value, "NodeD42", self)

    @property
    def NodeD(self):
        return self.__NodeD

    @NodeD.setter
    def NodeD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__NodeD", None)
        self.__NodeD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent31"):
                opp_val = getattr(old_value, "parent31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent31"):
                opp_val = getattr(value, "parent31", None)
                if opp_val is None:
                    setattr(value, "parent31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NodeD38(self):
        return self.__NodeD38

    @NodeD38.setter
    def NodeD38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__NodeD38", None)
        self.__NodeD38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oppositeNode"):
                opp_val = getattr(old_value, "oppositeNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oppositeNode"):
                opp_val = getattr(value, "oppositeNode", None)
                if opp_val is None:
                    setattr(value, "oppositeNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oppositeNode(self):
        return self.__oppositeNode

    @oppositeNode.setter
    def oppositeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__oppositeNode", None)
        self.__oppositeNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeD38"):
                    opp_val = getattr(item, "NodeD38", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeD38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeD38"):
                    opp_val = getattr(item, "NodeD38", None)
                    
                    setattr(item, "NodeD38", self)
                    

    @property
    def parent31(self):
        return self.__parent31

    @parent31.setter
    def parent31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeD__parent31", None)
        self.__parent31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeD"):
                    opp_val = getattr(item, "NodeD", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeD", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeD"):
                    opp_val = getattr(item, "NodeD", None)
                    
                    setattr(item, "NodeD", self)
                    

class model3_NodeC:

    def __init__(self, name: str, NodeC: "model3_NodeC" = None, parent18: set["model3_NodeC"] = None, NodeC22: "model3_NodeC" = None, children21: "model3_NodeC" = None, NodeC25: "model3_NodeC" = None, oppositeNodes: set["model3_NodeC"] = None, NodeC28: "model3_NodeC" = None, otherNodes: set["model3_NodeC"] = None):
        self.name = name
        self.NodeC = NodeC
        self.parent18 = parent18 if parent18 is not None else set()
        self.NodeC22 = NodeC22
        self.children21 = children21
        self.NodeC25 = NodeC25
        self.oppositeNodes = oppositeNodes if oppositeNodes is not None else set()
        self.NodeC28 = NodeC28
        self.otherNodes = otherNodes if otherNodes is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NodeC(self):
        return self.__NodeC

    @NodeC.setter
    def NodeC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__NodeC", None)
        self.__NodeC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent18"):
                opp_val = getattr(old_value, "parent18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent18"):
                opp_val = getattr(value, "parent18", None)
                if opp_val is None:
                    setattr(value, "parent18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NodeC25(self):
        return self.__NodeC25

    @NodeC25.setter
    def NodeC25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__NodeC25", None)
        self.__NodeC25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oppositeNodes"):
                opp_val = getattr(old_value, "oppositeNodes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oppositeNodes"):
                opp_val = getattr(value, "oppositeNodes", None)
                if opp_val is None:
                    setattr(value, "oppositeNodes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children21(self):
        return self.__children21

    @children21.setter
    def children21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__children21", None)
        self.__children21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeC22"):
                opp_val = getattr(old_value, "NodeC22", None)
                if opp_val == self:
                    setattr(old_value, "NodeC22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeC22"):
                opp_val = getattr(value, "NodeC22", None)
                setattr(value, "NodeC22", self)

    @property
    def NodeC22(self):
        return self.__NodeC22

    @NodeC22.setter
    def NodeC22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__NodeC22", None)
        self.__NodeC22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children21"):
                opp_val = getattr(old_value, "children21", None)
                if opp_val == self:
                    setattr(old_value, "children21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children21"):
                opp_val = getattr(value, "children21", None)
                setattr(value, "children21", self)

    @property
    def otherNodes(self):
        return self.__otherNodes

    @otherNodes.setter
    def otherNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__otherNodes", None)
        self.__otherNodes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeC28"):
                    opp_val = getattr(item, "NodeC28", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeC28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeC28"):
                    opp_val = getattr(item, "NodeC28", None)
                    
                    setattr(item, "NodeC28", self)
                    

    @property
    def oppositeNodes(self):
        return self.__oppositeNodes

    @oppositeNodes.setter
    def oppositeNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__oppositeNodes", None)
        self.__oppositeNodes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeC25"):
                    opp_val = getattr(item, "NodeC25", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeC25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeC25"):
                    opp_val = getattr(item, "NodeC25", None)
                    
                    setattr(item, "NodeC25", self)
                    

    @property
    def parent18(self):
        return self.__parent18

    @parent18.setter
    def parent18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__parent18", None)
        self.__parent18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeC"):
                    opp_val = getattr(item, "NodeC", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeC", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeC"):
                    opp_val = getattr(item, "NodeC", None)
                    
                    setattr(item, "NodeC", self)
                    

    @property
    def NodeC28(self):
        return self.__NodeC28

    @NodeC28.setter
    def NodeC28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeC__NodeC28", None)
        self.__NodeC28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "otherNodes"):
                opp_val = getattr(old_value, "otherNodes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "otherNodes"):
                opp_val = getattr(value, "otherNodes", None)
                if opp_val is None:
                    setattr(value, "otherNodes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Class2:

    pass
class model3_NodeB:

    def __init__(self, name: str, NodeB: "model3_NodeB" = None, parent: set["model3_NodeB"] = None, NodeB15: "model3_NodeB" = None, children: "model3_NodeB" = None):
        self.name = name
        self.NodeB = NodeB
        self.parent = parent if parent is not None else set()
        self.NodeB15 = NodeB15
        self.children = children
        
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
        old_value = getattr(self, f"_model3_NodeB__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeB15"):
                opp_val = getattr(old_value, "NodeB15", None)
                if opp_val == self:
                    setattr(old_value, "NodeB15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeB15"):
                opp_val = getattr(value, "NodeB15", None)
                setattr(value, "NodeB15", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeB__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeB"):
                    opp_val = getattr(item, "NodeB", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeB", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeB"):
                    opp_val = getattr(item, "NodeB", None)
                    
                    setattr(item, "NodeB", self)
                    

    @property
    def NodeB(self):
        return self.__NodeB

    @NodeB.setter
    def NodeB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeB__NodeB", None)
        self.__NodeB = value
        
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
    def NodeB15(self):
        return self.__NodeB15

    @NodeB15.setter
    def NodeB15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeB__NodeB15", None)
        self.__NodeB15 = value
        
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

class model3_NodeA:

    def __init__(self, name: str, model3_NodeA: "model3_NodeA" = None, model3_NodeA6: set["model3_NodeA"] = None, model3_NodeA10: "model3_NodeA" = None, model3_NodeA8: set["model3_NodeA"] = None):
        self.name = name
        self.model3_NodeA = model3_NodeA
        self.model3_NodeA6 = model3_NodeA6 if model3_NodeA6 is not None else set()
        self.model3_NodeA10 = model3_NodeA10
        self.model3_NodeA8 = model3_NodeA8 if model3_NodeA8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model3_NodeA10(self):
        return self.__model3_NodeA10

    @model3_NodeA10.setter
    def model3_NodeA10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeA__model3_NodeA10", None)
        self.__model3_NodeA10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model3_NodeA8"):
                opp_val = getattr(old_value, "model3_NodeA8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model3_NodeA8"):
                opp_val = getattr(value, "model3_NodeA8", None)
                if opp_val is None:
                    setattr(value, "model3_NodeA8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model3_NodeA(self):
        return self.__model3_NodeA

    @model3_NodeA.setter
    def model3_NodeA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeA__model3_NodeA", None)
        self.__model3_NodeA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model3_NodeA6"):
                opp_val = getattr(old_value, "model3_NodeA6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model3_NodeA6"):
                opp_val = getattr(value, "model3_NodeA6", None)
                if opp_val is None:
                    setattr(value, "model3_NodeA6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model3_NodeA8(self):
        return self.__model3_NodeA8

    @model3_NodeA8.setter
    def model3_NodeA8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeA__model3_NodeA8", None)
        self.__model3_NodeA8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model3_NodeA10"):
                    opp_val = getattr(item, "model3_NodeA10", None)
                    
                    if opp_val == self:
                        setattr(item, "model3_NodeA10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model3_NodeA10"):
                    opp_val = getattr(item, "model3_NodeA10", None)
                    
                    setattr(item, "model3_NodeA10", self)
                    

    @property
    def model3_NodeA6(self):
        return self.__model3_NodeA6

    @model3_NodeA6.setter
    def model3_NodeA6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model3_NodeA__model3_NodeA6", None)
        self.__model3_NodeA6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model3_NodeA"):
                    opp_val = getattr(item, "model3_NodeA", None)
                    
                    if opp_val == self:
                        setattr(item, "model3_NodeA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model3_NodeA"):
                    opp_val = getattr(item, "model3_NodeA", None)
                    
                    setattr(item, "model3_NodeA", self)
                    

class model3_PolygonWithDuplicates:

    def __init__(self, points: str):
        self.points = points
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

class model3_Polygon:

    def __init__(self, points: str):
        self.points = points
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

class model3_EReference:

    pass
class model3_EClass:

    pass
class model3_EPackage:

    pass
class model3_MetaRef:

    pass
class model3_Class1:

    pass