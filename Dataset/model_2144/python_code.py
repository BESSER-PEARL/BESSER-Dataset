from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expr:

    pass
class graph_MulOrDiv(Expr):

    def __init__(self, op: str, graph_MulOrDiv: "graph_Expr" = None, graph_MulOrDiv56: "graph_Expr" = None):
        self.op = op
        self.graph_MulOrDiv = graph_MulOrDiv
        self.graph_MulOrDiv56 = graph_MulOrDiv56
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def graph_MulOrDiv56(self):
        return self.__graph_MulOrDiv56

    @graph_MulOrDiv56.setter
    def graph_MulOrDiv56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_MulOrDiv__graph_MulOrDiv56", None)
        self.__graph_MulOrDiv56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr57"):
                opp_val = getattr(old_value, "graph_Expr57", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr57"):
                opp_val = getattr(value, "graph_Expr57", None)
                setattr(value, "graph_Expr57", self)

    @property
    def graph_MulOrDiv(self):
        return self.__graph_MulOrDiv

    @graph_MulOrDiv.setter
    def graph_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_MulOrDiv__graph_MulOrDiv", None)
        self.__graph_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr54"):
                opp_val = getattr(old_value, "graph_Expr54", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr54"):
                opp_val = getattr(value, "graph_Expr54", None)
                setattr(value, "graph_Expr54", self)

class graph_BoolConstant(Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class graph_IntConstant(Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class graph_Not(Expr):

    pass
class graph_PlusOrMin(Expr):

    def __init__(self, op: str, graph_PlusOrMin: "graph_Expr" = None, graph_PlusOrMin51: "graph_Expr" = None):
        self.op = op
        self.graph_PlusOrMin = graph_PlusOrMin
        self.graph_PlusOrMin51 = graph_PlusOrMin51
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def graph_PlusOrMin(self):
        return self.__graph_PlusOrMin

    @graph_PlusOrMin.setter
    def graph_PlusOrMin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_PlusOrMin__graph_PlusOrMin", None)
        self.__graph_PlusOrMin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr49"):
                opp_val = getattr(old_value, "graph_Expr49", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr49"):
                opp_val = getattr(value, "graph_Expr49", None)
                setattr(value, "graph_Expr49", self)

    @property
    def graph_PlusOrMin51(self):
        return self.__graph_PlusOrMin51

    @graph_PlusOrMin51.setter
    def graph_PlusOrMin51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_PlusOrMin__graph_PlusOrMin51", None)
        self.__graph_PlusOrMin51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr52"):
                opp_val = getattr(old_value, "graph_Expr52", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr52"):
                opp_val = getattr(value, "graph_Expr52", None)
                setattr(value, "graph_Expr52", self)

class graph_GraphConstant(Expr):

    pass
class graph_StringConstant(Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class graph_PathExistence(Expr):

    pass
class graph_And(Expr):

    pass
class graph_Comparison(Expr):

    def __init__(self, op: str, graph_Comparison: "graph_Expr" = None, graph_Comparison46: "graph_Expr" = None):
        self.op = op
        self.graph_Comparison = graph_Comparison
        self.graph_Comparison46 = graph_Comparison46
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def graph_Comparison(self):
        return self.__graph_Comparison

    @graph_Comparison.setter
    def graph_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Comparison__graph_Comparison", None)
        self.__graph_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr44"):
                opp_val = getattr(old_value, "graph_Expr44", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr44"):
                opp_val = getattr(value, "graph_Expr44", None)
                setattr(value, "graph_Expr44", self)

    @property
    def graph_Comparison46(self):
        return self.__graph_Comparison46

    @graph_Comparison46.setter
    def graph_Comparison46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Comparison__graph_Comparison46", None)
        self.__graph_Comparison46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Expr47"):
                opp_val = getattr(old_value, "graph_Expr47", None)
                if opp_val == self:
                    setattr(old_value, "graph_Expr47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Expr47"):
                opp_val = getattr(value, "graph_Expr47", None)
                setattr(value, "graph_Expr47", self)

class graph_VariableRef(Expr):

    pass
class graph_ParticleConstant(Expr):

    pass
class graph_Or(Expr):

    pass
class graph_Edge:

    pass
class graph_Vertex:

    def __init__(self, name: str, graph_Vertex: "graph_Edge" = None, graph_Vertex27: "graph_Edge" = None, graph_Vertex63: "graph_GraphConstant" = None, graph_Vertex71: "graph_ParticleConstant" = None):
        self.name = name
        self.graph_Vertex = graph_Vertex
        self.graph_Vertex27 = graph_Vertex27
        self.graph_Vertex63 = graph_Vertex63
        self.graph_Vertex71 = graph_Vertex71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Vertex63(self):
        return self.__graph_Vertex63

    @graph_Vertex63.setter
    def graph_Vertex63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex63", None)
        self.__graph_Vertex63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GraphConstant"):
                opp_val = getattr(old_value, "graph_GraphConstant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GraphConstant"):
                opp_val = getattr(value, "graph_GraphConstant", None)
                if opp_val is None:
                    setattr(value, "graph_GraphConstant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Vertex71(self):
        return self.__graph_Vertex71

    @graph_Vertex71.setter
    def graph_Vertex71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex71", None)
        self.__graph_Vertex71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ParticleConstant70"):
                opp_val = getattr(old_value, "graph_ParticleConstant70", None)
                if opp_val == self:
                    setattr(old_value, "graph_ParticleConstant70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ParticleConstant70"):
                opp_val = getattr(value, "graph_ParticleConstant70", None)
                setattr(value, "graph_ParticleConstant70", self)

    @property
    def graph_Vertex27(self):
        return self.__graph_Vertex27

    @graph_Vertex27.setter
    def graph_Vertex27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex27", None)
        self.__graph_Vertex27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge26"):
                opp_val = getattr(old_value, "graph_Edge26", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge26"):
                opp_val = getattr(value, "graph_Edge26", None)
                setattr(value, "graph_Edge26", self)

    @property
    def graph_Vertex(self):
        return self.__graph_Vertex

    @graph_Vertex.setter
    def graph_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex", None)
        self.__graph_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge"):
                opp_val = getattr(old_value, "graph_Edge", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge"):
                opp_val = getattr(value, "graph_Edge", None)
                setattr(value, "graph_Edge", self)

class graph_Expr:

    pass
class Statement:

    pass
class graph_IfStmt(Statement):

    pass
class graph_PrintStmt(Statement):

    pass
class graph_WhileStmt(Statement):

    pass
class graph_MoveStmt(Statement):

    pass
class graph_AssignStmt(Statement):

    pass
class graph_Statement:

    pass
class graph_Declaration:

    def __init__(self, name: str, type: str, graph_Declaration: "graph_Program" = None, graph_Declaration4: "graph_AssignStmt" = None, graph_Declaration23: "graph_MoveStmt" = None, graph_Declaration61: "graph_VariableRef" = None):
        self.name = name
        self.type = type
        self.graph_Declaration = graph_Declaration
        self.graph_Declaration4 = graph_Declaration4
        self.graph_Declaration23 = graph_Declaration23
        self.graph_Declaration61 = graph_Declaration61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def graph_Declaration61(self):
        return self.__graph_Declaration61

    @graph_Declaration61.setter
    def graph_Declaration61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Declaration__graph_Declaration61", None)
        self.__graph_Declaration61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_VariableRef"):
                opp_val = getattr(old_value, "graph_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "graph_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_VariableRef"):
                opp_val = getattr(value, "graph_VariableRef", None)
                setattr(value, "graph_VariableRef", self)

    @property
    def graph_Declaration(self):
        return self.__graph_Declaration

    @graph_Declaration.setter
    def graph_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Declaration__graph_Declaration", None)
        self.__graph_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Program"):
                opp_val = getattr(old_value, "graph_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Program"):
                opp_val = getattr(value, "graph_Program", None)
                if opp_val is None:
                    setattr(value, "graph_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Declaration23(self):
        return self.__graph_Declaration23

    @graph_Declaration23.setter
    def graph_Declaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Declaration__graph_Declaration23", None)
        self.__graph_Declaration23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_MoveStmt"):
                opp_val = getattr(old_value, "graph_MoveStmt", None)
                if opp_val == self:
                    setattr(old_value, "graph_MoveStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_MoveStmt"):
                opp_val = getattr(value, "graph_MoveStmt", None)
                setattr(value, "graph_MoveStmt", self)

    @property
    def graph_Declaration4(self):
        return self.__graph_Declaration4

    @graph_Declaration4.setter
    def graph_Declaration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Declaration__graph_Declaration4", None)
        self.__graph_Declaration4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_AssignStmt"):
                opp_val = getattr(old_value, "graph_AssignStmt", None)
                if opp_val == self:
                    setattr(old_value, "graph_AssignStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_AssignStmt"):
                opp_val = getattr(value, "graph_AssignStmt", None)
                setattr(value, "graph_AssignStmt", self)

class graph_Program:

    pass