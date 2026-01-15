from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    IMPLIES = "IMPLIES"
class Quantifier(Enum):
    EXISTS = "EXISTS"
    FORALL = "FORALL"


############################################
# Definition of Classes
############################################

class GraphConstraint_EDataType:

    pass
class GraphConstraint_Variable:

    def __init__(self, name: str, GraphConstraint_Variable: "GraphConstraint_EDataType" = None, GraphConstraint_Variable57: "GraphConstraint_NestedGraphCondition" = None):
        self.name = name
        self.GraphConstraint_Variable = GraphConstraint_Variable
        self.GraphConstraint_Variable57 = GraphConstraint_Variable57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GraphConstraint_Variable57(self):
        return self.__GraphConstraint_Variable57

    @GraphConstraint_Variable57.setter
    def GraphConstraint_Variable57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Variable__GraphConstraint_Variable57", None)
        self.__GraphConstraint_Variable57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_NestedGraphCondition56"):
                opp_val = getattr(old_value, "GraphConstraint_NestedGraphCondition56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_NestedGraphCondition56"):
                opp_val = getattr(value, "GraphConstraint_NestedGraphCondition56", None)
                if opp_val is None:
                    setattr(value, "GraphConstraint_NestedGraphCondition56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphConstraint_Variable(self):
        return self.__GraphConstraint_Variable

    @GraphConstraint_Variable.setter
    def GraphConstraint_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Variable__GraphConstraint_Variable", None)
        self.__GraphConstraint_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_EDataType"):
                opp_val = getattr(old_value, "GraphConstraint_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_EDataType"):
                opp_val = getattr(value, "GraphConstraint_EDataType", None)
                setattr(value, "GraphConstraint_EDataType", self)

class NestedGraphCondition:

    pass
class GraphConstraint_True(NestedGraphCondition):

    pass
class GraphConstraint_Formula(NestedGraphCondition):

    def __init__(self, op: str, Formula: "GraphConstraint_NestedGraphCondition" = None, formula: set["GraphConstraint_NestedGraphCondition"] = None):
        self.op = op
        self.Formula = Formula
        self.formula = formula if formula is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Formula__formula", None)
        self.__formula = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NestedGraphCondition48"):
                    opp_val = getattr(item, "NestedGraphCondition48", None)
                    
                    if opp_val == self:
                        setattr(item, "NestedGraphCondition48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NestedGraphCondition48"):
                    opp_val = getattr(item, "NestedGraphCondition48", None)
                    
                    setattr(item, "NestedGraphCondition48", self)
                    

    @property
    def Formula(self):
        return self.__Formula

    @Formula.setter
    def Formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Formula__Formula", None)
        self.__Formula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "args"):
                opp_val = getattr(old_value, "args", None)
                if opp_val == self:
                    setattr(old_value, "args", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "args"):
                opp_val = getattr(value, "args", None)
                setattr(value, "args", self)

class GraphConstraint_QuantifiedGraphCondition(NestedGraphCondition):

    def __init__(self, quantifier: str, GraphConstraint_QuantifiedGraphCondition: "GraphConstraint_Graph" = None, GraphConstraint_QuantifiedGraphCondition37: "GraphConstraint_Graph" = None, GraphConstraint_QuantifiedGraphCondition40: "GraphConstraint_Mapping" = None, QuantifiedGraphCondition: "GraphConstraint_NestedGraphCondition" = None, GraphConstraint_QuantifiedGraphCondition43: "GraphConstraint_Mapping" = None, qgc: "GraphConstraint_NestedGraphCondition" = None):
        self.quantifier = quantifier
        self.GraphConstraint_QuantifiedGraphCondition = GraphConstraint_QuantifiedGraphCondition
        self.GraphConstraint_QuantifiedGraphCondition37 = GraphConstraint_QuantifiedGraphCondition37
        self.GraphConstraint_QuantifiedGraphCondition40 = GraphConstraint_QuantifiedGraphCondition40
        self.QuantifiedGraphCondition = QuantifiedGraphCondition
        self.GraphConstraint_QuantifiedGraphCondition43 = GraphConstraint_QuantifiedGraphCondition43
        self.qgc = qgc
        
    @property
    def quantifier(self) -> str:
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier

    @property
    def QuantifiedGraphCondition(self):
        return self.__QuantifiedGraphCondition

    @QuantifiedGraphCondition.setter
    def QuantifiedGraphCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__QuantifiedGraphCondition", None)
        self.__QuantifiedGraphCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested"):
                opp_val = getattr(old_value, "nested", None)
                if opp_val == self:
                    setattr(old_value, "nested", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested"):
                opp_val = getattr(value, "nested", None)
                setattr(value, "nested", self)

    @property
    def GraphConstraint_QuantifiedGraphCondition(self):
        return self.__GraphConstraint_QuantifiedGraphCondition

    @GraphConstraint_QuantifiedGraphCondition.setter
    def GraphConstraint_QuantifiedGraphCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__GraphConstraint_QuantifiedGraphCondition", None)
        self.__GraphConstraint_QuantifiedGraphCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Graph35"):
                opp_val = getattr(old_value, "GraphConstraint_Graph35", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_Graph35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Graph35"):
                opp_val = getattr(value, "GraphConstraint_Graph35", None)
                setattr(value, "GraphConstraint_Graph35", self)

    @property
    def GraphConstraint_QuantifiedGraphCondition40(self):
        return self.__GraphConstraint_QuantifiedGraphCondition40

    @GraphConstraint_QuantifiedGraphCondition40.setter
    def GraphConstraint_QuantifiedGraphCondition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__GraphConstraint_QuantifiedGraphCondition40", None)
        self.__GraphConstraint_QuantifiedGraphCondition40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Mapping41"):
                opp_val = getattr(old_value, "GraphConstraint_Mapping41", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_Mapping41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Mapping41"):
                opp_val = getattr(value, "GraphConstraint_Mapping41", None)
                setattr(value, "GraphConstraint_Mapping41", self)

    @property
    def GraphConstraint_QuantifiedGraphCondition43(self):
        return self.__GraphConstraint_QuantifiedGraphCondition43

    @GraphConstraint_QuantifiedGraphCondition43.setter
    def GraphConstraint_QuantifiedGraphCondition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__GraphConstraint_QuantifiedGraphCondition43", None)
        self.__GraphConstraint_QuantifiedGraphCondition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Mapping44"):
                opp_val = getattr(old_value, "GraphConstraint_Mapping44", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_Mapping44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Mapping44"):
                opp_val = getattr(value, "GraphConstraint_Mapping44", None)
                setattr(value, "GraphConstraint_Mapping44", self)

    @property
    def qgc(self):
        return self.__qgc

    @qgc.setter
    def qgc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__qgc", None)
        self.__qgc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NestedGraphCondition46"):
                opp_val = getattr(old_value, "NestedGraphCondition46", None)
                if opp_val == self:
                    setattr(old_value, "NestedGraphCondition46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NestedGraphCondition46"):
                opp_val = getattr(value, "NestedGraphCondition46", None)
                setattr(value, "NestedGraphCondition46", self)

    @property
    def GraphConstraint_QuantifiedGraphCondition37(self):
        return self.__GraphConstraint_QuantifiedGraphCondition37

    @GraphConstraint_QuantifiedGraphCondition37.setter
    def GraphConstraint_QuantifiedGraphCondition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_QuantifiedGraphCondition__GraphConstraint_QuantifiedGraphCondition37", None)
        self.__GraphConstraint_QuantifiedGraphCondition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Graph38"):
                opp_val = getattr(old_value, "GraphConstraint_Graph38", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_Graph38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Graph38"):
                opp_val = getattr(value, "GraphConstraint_Graph38", None)
                setattr(value, "GraphConstraint_Graph38", self)

class GraphConstraint_ElementMapping:

    pass
class GraphConstraint_EReference:

    pass
class GraphConstraint_EClass:

    pass
class GraphElement:

    pass
class GraphConstraint_Attribute(GraphElement):

    def __init__(self, op: str, value: str, GraphConstraint_Attribute21: "GraphConstraint_EAttribute" = None, GraphConstraint_Attribute: "GraphConstraint_Node" = None):
        self.op = op
        self.value = value
        self.GraphConstraint_Attribute21 = GraphConstraint_Attribute21
        self.GraphConstraint_Attribute = GraphConstraint_Attribute
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def GraphConstraint_Attribute(self):
        return self.__GraphConstraint_Attribute

    @GraphConstraint_Attribute.setter
    def GraphConstraint_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Attribute__GraphConstraint_Attribute", None)
        self.__GraphConstraint_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Node9"):
                opp_val = getattr(old_value, "GraphConstraint_Node9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Node9"):
                opp_val = getattr(value, "GraphConstraint_Node9", None)
                if opp_val is None:
                    setattr(value, "GraphConstraint_Node9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphConstraint_Attribute21(self):
        return self.__GraphConstraint_Attribute21

    @GraphConstraint_Attribute21.setter
    def GraphConstraint_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_Attribute__GraphConstraint_Attribute21", None)
        self.__GraphConstraint_Attribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_EAttribute"):
                opp_val = getattr(old_value, "GraphConstraint_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_EAttribute"):
                opp_val = getattr(value, "GraphConstraint_EAttribute", None)
                setattr(value, "GraphConstraint_EAttribute", self)

class GraphConstraint_Mapping:

    pass
class GraphConstraint_EAttribute:

    pass
class GraphConstraint_EPackage:

    pass
class GraphConstraint_NestedGraphConstraint:

    def __init__(self, name: str, gc: "GraphConstraint_NestedGraphCondition" = None, GraphConstraint_NestedGraphConstraint6: "GraphConstraint_Graph" = None, GraphConstraint_NestedGraphConstraint: "GraphConstraint_EPackage" = None, NestedGraphConstraint: "GraphConstraint_NestedGraphCondition" = None):
        self.name = name
        self.gc = gc
        self.GraphConstraint_NestedGraphConstraint6 = GraphConstraint_NestedGraphConstraint6
        self.GraphConstraint_NestedGraphConstraint = GraphConstraint_NestedGraphConstraint
        self.NestedGraphConstraint = NestedGraphConstraint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GraphConstraint_NestedGraphConstraint(self):
        return self.__GraphConstraint_NestedGraphConstraint

    @GraphConstraint_NestedGraphConstraint.setter
    def GraphConstraint_NestedGraphConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_NestedGraphConstraint__GraphConstraint_NestedGraphConstraint", None)
        self.__GraphConstraint_NestedGraphConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_EPackage"):
                opp_val = getattr(old_value, "GraphConstraint_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_EPackage"):
                opp_val = getattr(value, "GraphConstraint_EPackage", None)
                setattr(value, "GraphConstraint_EPackage", self)

    @property
    def GraphConstraint_NestedGraphConstraint6(self):
        return self.__GraphConstraint_NestedGraphConstraint6

    @GraphConstraint_NestedGraphConstraint6.setter
    def GraphConstraint_NestedGraphConstraint6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_NestedGraphConstraint__GraphConstraint_NestedGraphConstraint6", None)
        self.__GraphConstraint_NestedGraphConstraint6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_Graph7"):
                opp_val = getattr(old_value, "GraphConstraint_Graph7", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_Graph7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_Graph7"):
                opp_val = getattr(value, "GraphConstraint_Graph7", None)
                setattr(value, "GraphConstraint_Graph7", self)

    @property
    def NestedGraphConstraint(self):
        return self.__NestedGraphConstraint

    @NestedGraphConstraint.setter
    def NestedGraphConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_NestedGraphConstraint__NestedGraphConstraint", None)
        self.__NestedGraphConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "condition"):
                opp_val = getattr(old_value, "condition", None)
                if opp_val == self:
                    setattr(old_value, "condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "condition"):
                opp_val = getattr(value, "condition", None)
                setattr(value, "condition", self)

    @property
    def gc(self):
        return self.__gc

    @gc.setter
    def gc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_NestedGraphConstraint__gc", None)
        self.__gc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NestedGraphCondition"):
                opp_val = getattr(old_value, "NestedGraphCondition", None)
                if opp_val == self:
                    setattr(old_value, "NestedGraphCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NestedGraphCondition"):
                opp_val = getattr(value, "NestedGraphCondition", None)
                setattr(value, "NestedGraphCondition", self)

class GraphConstraint_GraphElement(ABC):

    def __init__(self, name: str, GraphConstraint_GraphElement: "GraphConstraint_ElementMapping" = None, GraphConstraint_GraphElement33: "GraphConstraint_ElementMapping" = None):
        self.name = name
        self.GraphConstraint_GraphElement = GraphConstraint_GraphElement
        self.GraphConstraint_GraphElement33 = GraphConstraint_GraphElement33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GraphConstraint_GraphElement(self):
        return self.__GraphConstraint_GraphElement

    @GraphConstraint_GraphElement.setter
    def GraphConstraint_GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_GraphElement__GraphConstraint_GraphElement", None)
        self.__GraphConstraint_GraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_ElementMapping30"):
                opp_val = getattr(old_value, "GraphConstraint_ElementMapping30", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_ElementMapping30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_ElementMapping30"):
                opp_val = getattr(value, "GraphConstraint_ElementMapping30", None)
                setattr(value, "GraphConstraint_ElementMapping30", self)

    @property
    def GraphConstraint_GraphElement33(self):
        return self.__GraphConstraint_GraphElement33

    @GraphConstraint_GraphElement33.setter
    def GraphConstraint_GraphElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphConstraint_GraphElement__GraphConstraint_GraphElement33", None)
        self.__GraphConstraint_GraphElement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConstraint_ElementMapping32"):
                opp_val = getattr(old_value, "GraphConstraint_ElementMapping32", None)
                if opp_val == self:
                    setattr(old_value, "GraphConstraint_ElementMapping32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConstraint_ElementMapping32"):
                opp_val = getattr(value, "GraphConstraint_ElementMapping32", None)
                setattr(value, "GraphConstraint_ElementMapping32", self)

class GraphConstraint_Node(GraphElement):

    pass
class GraphConstraint_Edge(GraphElement):

    pass
class GraphConstraint_Graph:

    pass
class GraphConstraint_NestedGraphCondition(ABC):

    pass