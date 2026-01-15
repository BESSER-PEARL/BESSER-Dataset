from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    Functional_Safety_Requirement = "Functional_Safety_Requirement"
    Technical_Safety_Requirement = "Technical_Safety_Requirement"
    Technical_Requirement = "Technical_Requirement"
class Category(Enum):
    main = "main"
    observable_external_behavior = "observable_external_behavior"
    perception = "perception"
    planning = "planning"
    action = "action"
    sensor = "sensor"
    actuator = "actuator"


############################################
# Definition of Classes
############################################

class SkillGraph_Requirement:

    def __init__(self, comment: str, term: str, type: str, Requirement: "SkillGraph_Node" = None, requirements: "SkillGraph_Node" = None):
        self.comment = comment
        self.term = term
        self.type = type
        self.Requirement = Requirement
        self.requirements = requirements
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def Requirement(self):
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Requirement__Requirement", None)
        self.__Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node13"):
                opp_val = getattr(old_value, "node13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node13"):
                opp_val = getattr(value, "node13", None)
                if opp_val is None:
                    setattr(value, "node13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Requirement__requirements", None)
        self.__requirements = value
        
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

class SkillGraph_Edge:

    pass
class SkillGraph_Equation:

    def __init__(self, equation: str, Equation: "SkillGraph_Node" = None, equations: "SkillGraph_Node" = None):
        self.equation = equation
        self.Equation = Equation
        self.equations = equations
        
    @property
    def equation(self) -> str:
        return self.__equation

    @equation.setter
    def equation(self, equation: str):
        self.__equation = equation

    @property
    def equations(self):
        return self.__equations

    @equations.setter
    def equations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Equation__equations", None)
        self.__equations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node16"):
                opp_val = getattr(old_value, "Node16", None)
                if opp_val == self:
                    setattr(old_value, "Node16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node16"):
                opp_val = getattr(value, "Node16", None)
                setattr(value, "Node16", self)

    @property
    def Equation(self):
        return self.__Equation

    @Equation.setter
    def Equation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Equation__Equation", None)
        self.__Equation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SkillGraph_Node:

    def __init__(self, category: str, name: str, programPath: str, SkillGraph_Node19: "SkillGraph_Edge" = None, SkillGraph_Node22: "SkillGraph_Edge" = None, SkillGraph_Node: "SkillGraph_Graph" = None, SkillGraph_Node4: "SkillGraph_Graph" = None, node: set["SkillGraph_Equation"] = None, SkillGraph_Node8: set["SkillGraph_Edge"] = None, SkillGraph_Node11: "SkillGraph_Node" = None, SkillGraph_Node9: set["SkillGraph_Node"] = None, node13: set["SkillGraph_Requirement"] = None, Node: "SkillGraph_Requirement" = None, Node16: "SkillGraph_Equation" = None):
        self.category = category
        self.name = name
        self.programPath = programPath
        self.SkillGraph_Node19 = SkillGraph_Node19
        self.SkillGraph_Node22 = SkillGraph_Node22
        self.SkillGraph_Node = SkillGraph_Node
        self.SkillGraph_Node4 = SkillGraph_Node4
        self.node = node if node is not None else set()
        self.SkillGraph_Node8 = SkillGraph_Node8 if SkillGraph_Node8 is not None else set()
        self.SkillGraph_Node11 = SkillGraph_Node11
        self.SkillGraph_Node9 = SkillGraph_Node9 if SkillGraph_Node9 is not None else set()
        self.node13 = node13 if node13 is not None else set()
        self.Node = Node
        self.Node16 = Node16
        
    @property
    def programPath(self) -> str:
        return self.__programPath

    @programPath.setter
    def programPath(self, programPath: str):
        self.__programPath = programPath

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def SkillGraph_Node19(self):
        return self.__SkillGraph_Node19

    @SkillGraph_Node19.setter
    def SkillGraph_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node19", None)
        self.__SkillGraph_Node19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SkillGraph_Edge18"):
                opp_val = getattr(old_value, "SkillGraph_Edge18", None)
                if opp_val == self:
                    setattr(old_value, "SkillGraph_Edge18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SkillGraph_Edge18"):
                opp_val = getattr(value, "SkillGraph_Edge18", None)
                setattr(value, "SkillGraph_Edge18", self)

    @property
    def SkillGraph_Node9(self):
        return self.__SkillGraph_Node9

    @SkillGraph_Node9.setter
    def SkillGraph_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node9", None)
        self.__SkillGraph_Node9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SkillGraph_Node11"):
                    opp_val = getattr(item, "SkillGraph_Node11", None)
                    
                    if opp_val == self:
                        setattr(item, "SkillGraph_Node11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SkillGraph_Node11"):
                    opp_val = getattr(item, "SkillGraph_Node11", None)
                    
                    setattr(item, "SkillGraph_Node11", self)
                    

    @property
    def SkillGraph_Node11(self):
        return self.__SkillGraph_Node11

    @SkillGraph_Node11.setter
    def SkillGraph_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node11", None)
        self.__SkillGraph_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SkillGraph_Node9"):
                opp_val = getattr(old_value, "SkillGraph_Node9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SkillGraph_Node9"):
                opp_val = getattr(value, "SkillGraph_Node9", None)
                if opp_val is None:
                    setattr(value, "SkillGraph_Node9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node16(self):
        return self.__Node16

    @Node16.setter
    def Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__Node16", None)
        self.__Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equations"):
                opp_val = getattr(old_value, "equations", None)
                if opp_val == self:
                    setattr(old_value, "equations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equations"):
                opp_val = getattr(value, "equations", None)
                setattr(value, "equations", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Equation"):
                    opp_val = getattr(item, "Equation", None)
                    
                    if opp_val == self:
                        setattr(item, "Equation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Equation"):
                    opp_val = getattr(item, "Equation", None)
                    
                    setattr(item, "Equation", self)
                    

    @property
    def SkillGraph_Node8(self):
        return self.__SkillGraph_Node8

    @SkillGraph_Node8.setter
    def SkillGraph_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node8", None)
        self.__SkillGraph_Node8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SkillGraph_Edge"):
                    opp_val = getattr(item, "SkillGraph_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "SkillGraph_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SkillGraph_Edge"):
                    opp_val = getattr(item, "SkillGraph_Edge", None)
                    
                    setattr(item, "SkillGraph_Edge", self)
                    

    @property
    def SkillGraph_Node(self):
        return self.__SkillGraph_Node

    @SkillGraph_Node.setter
    def SkillGraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node", None)
        self.__SkillGraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SkillGraph_Graph"):
                opp_val = getattr(old_value, "SkillGraph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SkillGraph_Graph"):
                opp_val = getattr(value, "SkillGraph_Graph", None)
                if opp_val is None:
                    setattr(value, "SkillGraph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SkillGraph_Node22(self):
        return self.__SkillGraph_Node22

    @SkillGraph_Node22.setter
    def SkillGraph_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node22", None)
        self.__SkillGraph_Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SkillGraph_Edge21"):
                opp_val = getattr(old_value, "SkillGraph_Edge21", None)
                if opp_val == self:
                    setattr(old_value, "SkillGraph_Edge21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SkillGraph_Edge21"):
                opp_val = getattr(value, "SkillGraph_Edge21", None)
                setattr(value, "SkillGraph_Edge21", self)

    @property
    def SkillGraph_Node4(self):
        return self.__SkillGraph_Node4

    @SkillGraph_Node4.setter
    def SkillGraph_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__SkillGraph_Node4", None)
        self.__SkillGraph_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SkillGraph_Graph3"):
                opp_val = getattr(old_value, "SkillGraph_Graph3", None)
                if opp_val == self:
                    setattr(old_value, "SkillGraph_Graph3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SkillGraph_Graph3"):
                opp_val = getattr(value, "SkillGraph_Graph3", None)
                setattr(value, "SkillGraph_Graph3", self)

    @property
    def node13(self):
        return self.__node13

    @node13.setter
    def node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__node13", None)
        self.__node13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requirement"):
                    opp_val = getattr(item, "Requirement", None)
                    
                    setattr(item, "Requirement", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements"):
                opp_val = getattr(old_value, "requirements", None)
                if opp_val == self:
                    setattr(old_value, "requirements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements"):
                opp_val = getattr(value, "requirements", None)
                setattr(value, "requirements", self)

class SkillGraph_Graph:

    pass
class SkillGraph_Parameter:

    def __init__(self, name: str, unit: str, defaultValue: str, abbreviation: str, variable: bool, parameterList: "SkillGraph_Graph" = None, Parameter: "SkillGraph_Graph" = None):
        self.name = name
        self.unit = unit
        self.defaultValue = defaultValue
        self.abbreviation = abbreviation
        self.variable = variable
        self.parameterList = parameterList
        self.Parameter = Parameter
        
    @property
    def variable(self) -> bool:
        return self.__variable

    @variable.setter
    def variable(self, variable: bool):
        self.__variable = variable

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def abbreviation(self) -> str:
        return self.__abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: str):
        self.__abbreviation = abbreviation

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameterList(self):
        return self.__parameterList

    @parameterList.setter
    def parameterList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Parameter__parameterList", None)
        self.__parameterList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillGraph_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
