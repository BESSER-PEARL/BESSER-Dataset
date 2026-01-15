from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class transformr_Expression:

    def __init__(self, expression: str, transformr_Expression: set["transformr_Variable"] = None):
        self.expression = expression
        self.transformr_Expression = transformr_Expression if transformr_Expression is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def transformr_Expression(self):
        return self.__transformr_Expression

    @transformr_Expression.setter
    def transformr_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Expression__transformr_Expression", None)
        self.__transformr_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformr_Variable30"):
                    opp_val = getattr(item, "transformr_Variable30", None)
                    
                    if opp_val == self:
                        setattr(item, "transformr_Variable30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformr_Variable30"):
                    opp_val = getattr(item, "transformr_Variable30", None)
                    
                    setattr(item, "transformr_Variable30", self)
                    

class transformr_TypedElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class transformr_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PatternConstraint:

    pass
class transformr_ForAll(PatternConstraint):

    pass
class transformr_Exists(PatternConstraint):

    pass
class BinaryConstraint:

    pass
class transformr_Or(BinaryConstraint):

    pass
class transformr_And(BinaryConstraint):

    pass
class Constraint:

    pass
class transformr_VariableConstraint(Expression, Constraint):

    pass
class transformr_BinaryConstraint(Constraint):

    pass
class transformr_Not(Constraint):

    pass
class transformr_PatternConstraint(Constraint):

    pass
class transformr_Constraint(ABC):

    pass
class Graph:

    pass
class transformr_Pattern(Graph):

    pass
class TypedElement:

    pass
class transformr_Assignment(Expression):

    pass
class Executable:

    pass
class transformr_Branch(Executable):

    pass
class transformr_Block(Executable):

    pass
class Pattern:

    pass
class transformr_Rule(Executable, Pattern):

    pass
class NamedElement:

    pass
class transformr_Executable(NamedElement):

    pass
class transformr_Variable(NamedElement):

    pass
class transformr_GraphElement(NamedElement, TypedElement):

    pass
class transformr_Graph(NamedElement):

    pass
class transformr_Attribute(NamedElement, TypedElement):

    def __init__(self, transformr_Attribute: "transformr_Node" = None, transformr_Attribute28: "transformr_Variable" = None):
        self.transformr_Attribute = transformr_Attribute
        self.transformr_Attribute28 = transformr_Attribute28
        
    @property
    def transformr_Attribute(self):
        return self.__transformr_Attribute

    @transformr_Attribute.setter
    def transformr_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Attribute__transformr_Attribute", None)
        self.__transformr_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Node4"):
                opp_val = getattr(old_value, "transformr_Node4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Node4"):
                opp_val = getattr(value, "transformr_Node4", None)
                if opp_val is None:
                    setattr(value, "transformr_Node4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transformr_Attribute28(self):
        return self.__transformr_Attribute28

    @transformr_Attribute28.setter
    def transformr_Attribute28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Attribute__transformr_Attribute28", None)
        self.__transformr_Attribute28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Variable27"):
                opp_val = getattr(old_value, "transformr_Variable27", None)
                if opp_val == self:
                    setattr(old_value, "transformr_Variable27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Variable27"):
                opp_val = getattr(value, "transformr_Variable27", None)
                setattr(value, "transformr_Variable27", self)

    def setEType(self, eattribute: str):
        # TODO: Implement setEType method
        pass

class GraphElement:

    pass
class transformr_Edge(GraphElement):

    def __init__(self, transformr_Edge: "transformr_Node" = None, transformr_Edge6: "transformr_Node" = None):
        self.transformr_Edge = transformr_Edge
        self.transformr_Edge6 = transformr_Edge6
        
    @property
    def transformr_Edge6(self):
        return self.__transformr_Edge6

    @transformr_Edge6.setter
    def transformr_Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Edge__transformr_Edge6", None)
        self.__transformr_Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Node7"):
                opp_val = getattr(old_value, "transformr_Node7", None)
                if opp_val == self:
                    setattr(old_value, "transformr_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Node7"):
                opp_val = getattr(value, "transformr_Node7", None)
                setattr(value, "transformr_Node7", self)

    @property
    def transformr_Edge(self):
        return self.__transformr_Edge

    @transformr_Edge.setter
    def transformr_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Edge__transformr_Edge", None)
        self.__transformr_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Node2"):
                opp_val = getattr(old_value, "transformr_Node2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Node2"):
                opp_val = getattr(value, "transformr_Node2", None)
                if opp_val is None:
                    setattr(value, "transformr_Node2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

    def setEType(self, ereference: str):
        # TODO: Implement setEType method
        pass

    def setSource(self, source: str):
        # TODO: Implement setSource method
        pass

class transformr_Node(GraphElement):

    def __init__(self, transformr_Node: "transformr_Graph" = None, transformr_Node2: set["transformr_Edge"] = None, transformr_Node4: set["transformr_Attribute"] = None, transformr_Node7: "transformr_Edge" = None):
        self.transformr_Node = transformr_Node
        self.transformr_Node2 = transformr_Node2 if transformr_Node2 is not None else set()
        self.transformr_Node4 = transformr_Node4 if transformr_Node4 is not None else set()
        self.transformr_Node7 = transformr_Node7
        
    @property
    def transformr_Node4(self):
        return self.__transformr_Node4

    @transformr_Node4.setter
    def transformr_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Node__transformr_Node4", None)
        self.__transformr_Node4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformr_Attribute"):
                    opp_val = getattr(item, "transformr_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "transformr_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformr_Attribute"):
                    opp_val = getattr(item, "transformr_Attribute", None)
                    
                    setattr(item, "transformr_Attribute", self)
                    

    @property
    def transformr_Node2(self):
        return self.__transformr_Node2

    @transformr_Node2.setter
    def transformr_Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Node__transformr_Node2", None)
        self.__transformr_Node2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformr_Edge"):
                    opp_val = getattr(item, "transformr_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "transformr_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformr_Edge"):
                    opp_val = getattr(item, "transformr_Edge", None)
                    
                    setattr(item, "transformr_Edge", self)
                    

    @property
    def transformr_Node(self):
        return self.__transformr_Node

    @transformr_Node.setter
    def transformr_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Node__transformr_Node", None)
        self.__transformr_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Graph"):
                opp_val = getattr(old_value, "transformr_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Graph"):
                opp_val = getattr(value, "transformr_Graph", None)
                if opp_val is None:
                    setattr(value, "transformr_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transformr_Node7(self):
        return self.__transformr_Node7

    @transformr_Node7.setter
    def transformr_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformr_Node__transformr_Node7", None)
        self.__transformr_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformr_Edge6"):
                opp_val = getattr(old_value, "transformr_Edge6", None)
                if opp_val == self:
                    setattr(old_value, "transformr_Edge6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformr_Edge6"):
                opp_val = getattr(value, "transformr_Edge6", None)
                setattr(value, "transformr_Edge6", self)

    def setEType(self, eclass: str):
        # TODO: Implement setEType method
        pass
