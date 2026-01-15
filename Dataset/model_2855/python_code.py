from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ir_AnnotationArgument:

    def __init__(self, id: str, value: str, ir_AnnotationArgument: "ir_Annotation" = None):
        self.id = id
        self.value = value
        self.ir_AnnotationArgument = ir_AnnotationArgument
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ir_AnnotationArgument(self):
        return self.__ir_AnnotationArgument

    @ir_AnnotationArgument.setter
    def ir_AnnotationArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_AnnotationArgument__ir_AnnotationArgument", None)
        self.__ir_AnnotationArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Annotation256"):
                opp_val = getattr(old_value, "ir_Annotation256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Annotation256"):
                opp_val = getattr(value, "ir_Annotation256", None)
                if opp_val is None:
                    setattr(value, "ir_Annotation256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_State:

    def __init__(self, PriorityGraph: str, Action2TargetMap: str, name: str, ir_State: "ir_Schedule" = None, ir_State254: "ir_Schedule" = None):
        self.PriorityGraph = PriorityGraph
        self.Action2TargetMap = Action2TargetMap
        self.name = name
        self.ir_State = ir_State
        self.ir_State254 = ir_State254
        
    @property
    def PriorityGraph(self) -> str:
        return self.__PriorityGraph

    @PriorityGraph.setter
    def PriorityGraph(self, PriorityGraph: str):
        self.__PriorityGraph = PriorityGraph

    @property
    def Action2TargetMap(self) -> str:
        return self.__Action2TargetMap

    @Action2TargetMap.setter
    def Action2TargetMap(self, Action2TargetMap: str):
        self.__Action2TargetMap = Action2TargetMap

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_State(self):
        return self.__ir_State

    @ir_State.setter
    def ir_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_State__ir_State", None)
        self.__ir_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Schedule248"):
                opp_val = getattr(old_value, "ir_Schedule248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Schedule248"):
                opp_val = getattr(value, "ir_Schedule248", None)
                if opp_val is None:
                    setattr(value, "ir_Schedule248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_State254(self):
        return self.__ir_State254

    @ir_State254.setter
    def ir_State254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_State__ir_State254", None)
        self.__ir_State254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Schedule253"):
                opp_val = getattr(old_value, "ir_Schedule253", None)
                if opp_val == self:
                    setattr(old_value, "ir_Schedule253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Schedule253"):
                opp_val = getattr(value, "ir_Schedule253", None)
                setattr(value, "ir_Schedule253", self)

class Type:

    pass
class ir_TypeInt(Type):

    pass
class ir_TypeUser(Type):

    pass
class ir_TypeFloat(Type):

    pass
class ir_TypeList(Type):

    pass
class ir_TypeUndef(Type):

    pass
class ir_TypeExternal(Type):

    def __init__(self, name: str, scopeName: str, ir_TypeExternal: set["ir_TaggedExpression"] = None):
        self.name = name
        self.scopeName = scopeName
        self.ir_TypeExternal = ir_TypeExternal if ir_TypeExternal is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scopeName(self) -> str:
        return self.__scopeName

    @scopeName.setter
    def scopeName(self, scopeName: str):
        self.__scopeName = scopeName

    @property
    def ir_TypeExternal(self):
        return self.__ir_TypeExternal

    @ir_TypeExternal.setter
    def ir_TypeExternal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TypeExternal__ir_TypeExternal", None)
        self.__ir_TypeExternal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_TaggedExpression213"):
                    opp_val = getattr(item, "ir_TaggedExpression213", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_TaggedExpression213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_TaggedExpression213"):
                    opp_val = getattr(item, "ir_TaggedExpression213", None)
                    
                    setattr(item, "ir_TaggedExpression213", self)
                    

class ir_TypeString(Type):

    pass
class ir_TypeUint(Type):

    pass
class ir_TypeLambda(Type):

    pass
class ir_TypeProc(Type):

    pass
class ir_TypeBool(Type):

    pass
class LambdaExpression:

    pass
class PortAccess:

    pass
class ir_PortPeek(PortAccess):

    def __init__(self, position: int, ir_PortPeek: "ir_VariableReference" = None, ir_PortPeek211: "ir_Guard" = None):
        self.position = position
        self.ir_PortPeek = ir_PortPeek
        self.ir_PortPeek211 = ir_PortPeek211
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def ir_PortPeek211(self):
        return self.__ir_PortPeek211

    @ir_PortPeek211.setter
    def ir_PortPeek211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortPeek__ir_PortPeek211", None)
        self.__ir_PortPeek211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Guard210"):
                opp_val = getattr(old_value, "ir_Guard210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Guard210"):
                opp_val = getattr(value, "ir_Guard210", None)
                if opp_val is None:
                    setattr(value, "ir_Guard210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_PortPeek(self):
        return self.__ir_PortPeek

    @ir_PortPeek.setter
    def ir_PortPeek(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortPeek__ir_PortPeek", None)
        self.__ir_PortPeek = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableReference170"):
                opp_val = getattr(old_value, "ir_VariableReference170", None)
                if opp_val == self:
                    setattr(old_value, "ir_VariableReference170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableReference170"):
                opp_val = getattr(value, "ir_VariableReference170", None)
                setattr(value, "ir_VariableReference170", self)

class Block:

    pass
class Statement:

    pass
class ir_ReturnValue(Statement):

    pass
class ir_IfStatement(Statement):

    pass
class ir_ForEach(Statement):

    pass
class ir_ProcCall(Statement):

    pass
class ir_WhileLoop(Statement):

    pass
class ir_Assign(Statement):

    pass
class Connection:

    pass
class ir_FromSource(Connection):

    pass
class ir_ToSink(Connection):

    pass
class ir_Point2PointConnection(Connection):

    pass
class ExpressionCall:

    pass
class ir_TypeConstructorCall(ExpressionCall):

    def __init__(self, name: str, ir_TypeConstructorCall: set["ir_Expression"] = None, ir_TypeConstructorCall92: "ir_Declaration" = None):
        self.name = name
        self.ir_TypeConstructorCall = ir_TypeConstructorCall if ir_TypeConstructorCall is not None else set()
        self.ir_TypeConstructorCall92 = ir_TypeConstructorCall92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_TypeConstructorCall(self):
        return self.__ir_TypeConstructorCall

    @ir_TypeConstructorCall.setter
    def ir_TypeConstructorCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TypeConstructorCall__ir_TypeConstructorCall", None)
        self.__ir_TypeConstructorCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Expression90"):
                    opp_val = getattr(item, "ir_Expression90", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Expression90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Expression90"):
                    opp_val = getattr(item, "ir_Expression90", None)
                    
                    setattr(item, "ir_Expression90", self)
                    

    @property
    def ir_TypeConstructorCall92(self):
        return self.__ir_TypeConstructorCall92

    @ir_TypeConstructorCall92.setter
    def ir_TypeConstructorCall92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TypeConstructorCall__ir_TypeConstructorCall92", None)
        self.__ir_TypeConstructorCall92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Declaration93"):
                opp_val = getattr(old_value, "ir_Declaration93", None)
                if opp_val == self:
                    setattr(old_value, "ir_Declaration93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Declaration93"):
                opp_val = getattr(value, "ir_Declaration93", None)
                setattr(value, "ir_Declaration93", self)

class ir_FunctionCall(ExpressionCall):

    pass
class LiteralExpression:

    pass
class ir_StringLiteral(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ir_BooleanLiteral(LiteralExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ir_FloatLiteral(LiteralExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class ir_IntegerLiteral(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Expression:

    pass
class ir_IfExpression(Expression):

    pass
class ir_BinaryExpression(Expression):

    def __init__(self, operator: str, ir_BinaryExpression: "ir_Expression" = None, ir_BinaryExpression80: "ir_Expression" = None):
        self.operator = operator
        self.ir_BinaryExpression = ir_BinaryExpression
        self.ir_BinaryExpression80 = ir_BinaryExpression80
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ir_BinaryExpression(self):
        return self.__ir_BinaryExpression

    @ir_BinaryExpression.setter
    def ir_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BinaryExpression__ir_BinaryExpression", None)
        self.__ir_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression78"):
                opp_val = getattr(old_value, "ir_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression78"):
                opp_val = getattr(value, "ir_Expression78", None)
                setattr(value, "ir_Expression78", self)

    @property
    def ir_BinaryExpression80(self):
        return self.__ir_BinaryExpression80

    @ir_BinaryExpression80.setter
    def ir_BinaryExpression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BinaryExpression__ir_BinaryExpression80", None)
        self.__ir_BinaryExpression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression81"):
                opp_val = getattr(old_value, "ir_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression81"):
                opp_val = getattr(value, "ir_Expression81", None)
                setattr(value, "ir_Expression81", self)

class ir_ListExpression(Expression):

    pass
class ir_ExpressionCall(Expression):

    pass
class ir_VariableExpression(Expression):

    pass
class ir_UnaryExpression(Expression):

    def __init__(self, operator: str, ir_UnaryExpression: "ir_Expression" = None):
        self.operator = operator
        self.ir_UnaryExpression = ir_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ir_UnaryExpression(self):
        return self.__ir_UnaryExpression

    @ir_UnaryExpression.setter
    def ir_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_UnaryExpression__ir_UnaryExpression", None)
        self.__ir_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression83"):
                opp_val = getattr(old_value, "ir_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression83"):
                opp_val = getattr(value, "ir_Expression83", None)
                setattr(value, "ir_Expression83", self)

class ir_LiteralExpression(Expression):

    pass
class ir_TaggedExpression:

    def __init__(self, tag: str, ir_TaggedExpression: "ir_ActorInstance" = None, ir_TaggedExpression55: "ir_Expression" = None, ir_TaggedExpression96: "ir_Connection" = None, ir_TaggedExpression176: "ir_Declaration" = None, ir_TaggedExpression213: "ir_TypeExternal" = None):
        self.tag = tag
        self.ir_TaggedExpression = ir_TaggedExpression
        self.ir_TaggedExpression55 = ir_TaggedExpression55
        self.ir_TaggedExpression96 = ir_TaggedExpression96
        self.ir_TaggedExpression176 = ir_TaggedExpression176
        self.ir_TaggedExpression213 = ir_TaggedExpression213
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def ir_TaggedExpression213(self):
        return self.__ir_TaggedExpression213

    @ir_TaggedExpression213.setter
    def ir_TaggedExpression213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TaggedExpression__ir_TaggedExpression213", None)
        self.__ir_TaggedExpression213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeExternal"):
                opp_val = getattr(old_value, "ir_TypeExternal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeExternal"):
                opp_val = getattr(value, "ir_TypeExternal", None)
                if opp_val is None:
                    setattr(value, "ir_TypeExternal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_TaggedExpression96(self):
        return self.__ir_TaggedExpression96

    @ir_TaggedExpression96.setter
    def ir_TaggedExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TaggedExpression__ir_TaggedExpression96", None)
        self.__ir_TaggedExpression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Connection95"):
                opp_val = getattr(old_value, "ir_Connection95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Connection95"):
                opp_val = getattr(value, "ir_Connection95", None)
                if opp_val is None:
                    setattr(value, "ir_Connection95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_TaggedExpression176(self):
        return self.__ir_TaggedExpression176

    @ir_TaggedExpression176.setter
    def ir_TaggedExpression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TaggedExpression__ir_TaggedExpression176", None)
        self.__ir_TaggedExpression176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Declaration175"):
                opp_val = getattr(old_value, "ir_Declaration175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Declaration175"):
                opp_val = getattr(value, "ir_Declaration175", None)
                if opp_val is None:
                    setattr(value, "ir_Declaration175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_TaggedExpression55(self):
        return self.__ir_TaggedExpression55

    @ir_TaggedExpression55.setter
    def ir_TaggedExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TaggedExpression__ir_TaggedExpression55", None)
        self.__ir_TaggedExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression56"):
                opp_val = getattr(old_value, "ir_Expression56", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression56"):
                opp_val = getattr(value, "ir_Expression56", None)
                setattr(value, "ir_Expression56", self)

    @property
    def ir_TaggedExpression(self):
        return self.__ir_TaggedExpression

    @ir_TaggedExpression.setter
    def ir_TaggedExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TaggedExpression__ir_TaggedExpression", None)
        self.__ir_TaggedExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ActorInstance42"):
                opp_val = getattr(old_value, "ir_ActorInstance42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ActorInstance42"):
                opp_val = getattr(value, "ir_ActorInstance42", None)
                if opp_val is None:
                    setattr(value, "ir_ActorInstance42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Variable:

    pass
class ir_PortRead(PortAccess):

    pass
class ir_PortWrite(PortAccess, Block):

    pass
class ir_Guard(LambdaExpression):

    pass
class ir_ActorInstance(Variable):

    pass
class ir_Schedule:

    def __init__(self, PriorityGraph: str, ir_Schedule: "ir_Actor" = None, ir_Schedule248: set["ir_State"] = None, ir_Schedule250: set["ir_Action"] = None, ir_Schedule253: "ir_State" = None):
        self.PriorityGraph = PriorityGraph
        self.ir_Schedule = ir_Schedule
        self.ir_Schedule248 = ir_Schedule248 if ir_Schedule248 is not None else set()
        self.ir_Schedule250 = ir_Schedule250 if ir_Schedule250 is not None else set()
        self.ir_Schedule253 = ir_Schedule253
        
    @property
    def PriorityGraph(self) -> str:
        return self.__PriorityGraph

    @PriorityGraph.setter
    def PriorityGraph(self, PriorityGraph: str):
        self.__PriorityGraph = PriorityGraph

    @property
    def ir_Schedule250(self):
        return self.__ir_Schedule250

    @ir_Schedule250.setter
    def ir_Schedule250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Schedule__ir_Schedule250", None)
        self.__ir_Schedule250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Action251"):
                    opp_val = getattr(item, "ir_Action251", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Action251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Action251"):
                    opp_val = getattr(item, "ir_Action251", None)
                    
                    setattr(item, "ir_Action251", self)
                    

    @property
    def ir_Schedule(self):
        return self.__ir_Schedule

    @ir_Schedule.setter
    def ir_Schedule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Schedule__ir_Schedule", None)
        self.__ir_Schedule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Actor21"):
                opp_val = getattr(old_value, "ir_Actor21", None)
                if opp_val == self:
                    setattr(old_value, "ir_Actor21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Actor21"):
                opp_val = getattr(value, "ir_Actor21", None)
                setattr(value, "ir_Actor21", self)

    @property
    def ir_Schedule248(self):
        return self.__ir_Schedule248

    @ir_Schedule248.setter
    def ir_Schedule248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Schedule__ir_Schedule248", None)
        self.__ir_Schedule248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_State"):
                    opp_val = getattr(item, "ir_State", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_State"):
                    opp_val = getattr(item, "ir_State", None)
                    
                    setattr(item, "ir_State", self)
                    

    @property
    def ir_Schedule253(self):
        return self.__ir_Schedule253

    @ir_Schedule253.setter
    def ir_Schedule253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Schedule__ir_Schedule253", None)
        self.__ir_Schedule253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_State254"):
                opp_val = getattr(old_value, "ir_State254", None)
                if opp_val == self:
                    setattr(old_value, "ir_State254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_State254"):
                opp_val = getattr(value, "ir_State254", None)
                setattr(value, "ir_State254", self)

class AbstractActor:

    pass
class ir_Actor(AbstractActor):

    pass
class ir_Network(AbstractActor):

    pass
class ir_ExternalActor(AbstractActor):

    pass
class ir_TypeActor(Type):

    def __init__(self, namespace: str, name: str, ir_TypeActor: "ir_AbstractActor" = None):
        self.namespace = namespace
        self.name = name
        self.ir_TypeActor = ir_TypeActor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def ir_TypeActor(self):
        return self.__ir_TypeActor

    @ir_TypeActor.setter
    def ir_TypeActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TypeActor__ir_TypeActor", None)
        self.__ir_TypeActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_AbstractActor8"):
                opp_val = getattr(old_value, "ir_AbstractActor8", None)
                if opp_val == self:
                    setattr(old_value, "ir_AbstractActor8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_AbstractActor8"):
                opp_val = getattr(value, "ir_AbstractActor8", None)
                setattr(value, "ir_AbstractActor8", self)

class Scope:

    pass
class ir_Block(Statement, Scope):

    pass
class ir_LambdaExpression(Expression, Scope):

    pass
class ir_AbstractActor(Scope):

    pass
class ir_Action(Scope):

    def __init__(self, tag: str, ir_Action19: "ir_Actor" = None, ir_Action26: set["ir_Guard"] = None, ir_Action28: set["ir_PortWrite"] = None, ir_Action30: set["ir_PortRead"] = None, ir_Action32: set["ir_Statement"] = None, ir_Action: "ir_Actor" = None, ir_Action251: "ir_Schedule" = None):
        self.tag = tag
        self.ir_Action19 = ir_Action19
        self.ir_Action26 = ir_Action26 if ir_Action26 is not None else set()
        self.ir_Action28 = ir_Action28 if ir_Action28 is not None else set()
        self.ir_Action30 = ir_Action30 if ir_Action30 is not None else set()
        self.ir_Action32 = ir_Action32 if ir_Action32 is not None else set()
        self.ir_Action = ir_Action
        self.ir_Action251 = ir_Action251
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def ir_Action251(self):
        return self.__ir_Action251

    @ir_Action251.setter
    def ir_Action251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action251", None)
        self.__ir_Action251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Schedule250"):
                opp_val = getattr(old_value, "ir_Schedule250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Schedule250"):
                opp_val = getattr(value, "ir_Schedule250", None)
                if opp_val is None:
                    setattr(value, "ir_Schedule250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Action28(self):
        return self.__ir_Action28

    @ir_Action28.setter
    def ir_Action28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action28", None)
        self.__ir_Action28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_PortWrite"):
                    opp_val = getattr(item, "ir_PortWrite", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_PortWrite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_PortWrite"):
                    opp_val = getattr(item, "ir_PortWrite", None)
                    
                    setattr(item, "ir_PortWrite", self)
                    

    @property
    def ir_Action(self):
        return self.__ir_Action

    @ir_Action.setter
    def ir_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action", None)
        self.__ir_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Actor"):
                opp_val = getattr(old_value, "ir_Actor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Actor"):
                opp_val = getattr(value, "ir_Actor", None)
                if opp_val is None:
                    setattr(value, "ir_Actor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Action32(self):
        return self.__ir_Action32

    @ir_Action32.setter
    def ir_Action32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action32", None)
        self.__ir_Action32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Statement"):
                    opp_val = getattr(item, "ir_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Statement"):
                    opp_val = getattr(item, "ir_Statement", None)
                    
                    setattr(item, "ir_Statement", self)
                    

    @property
    def ir_Action26(self):
        return self.__ir_Action26

    @ir_Action26.setter
    def ir_Action26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action26", None)
        self.__ir_Action26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Guard"):
                    opp_val = getattr(item, "ir_Guard", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Guard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Guard"):
                    opp_val = getattr(item, "ir_Guard", None)
                    
                    setattr(item, "ir_Guard", self)
                    

    @property
    def ir_Action19(self):
        return self.__ir_Action19

    @ir_Action19.setter
    def ir_Action19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action19", None)
        self.__ir_Action19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Actor18"):
                opp_val = getattr(old_value, "ir_Actor18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Actor18"):
                opp_val = getattr(value, "ir_Actor18", None)
                if opp_val is None:
                    setattr(value, "ir_Actor18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Action30(self):
        return self.__ir_Action30

    @ir_Action30.setter
    def ir_Action30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Action__ir_Action30", None)
        self.__ir_Action30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_PortRead"):
                    opp_val = getattr(item, "ir_PortRead", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_PortRead", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_PortRead"):
                    opp_val = getattr(item, "ir_PortRead", None)
                    
                    setattr(item, "ir_PortRead", self)
                    

class ir_Generator(Scope):

    pass
class ir_ProcExpression(Expression, Scope):

    pass
class ir_Namespace(Scope):

    def __init__(self, name: str, ir_Namespace: set["ir_AbstractActor"] = None):
        self.name = name
        self.ir_Namespace = ir_Namespace if ir_Namespace is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Namespace(self):
        return self.__ir_Namespace

    @ir_Namespace.setter
    def ir_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Namespace__ir_Namespace", None)
        self.__ir_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_AbstractActor"):
                    opp_val = getattr(item, "ir_AbstractActor", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_AbstractActor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_AbstractActor"):
                    opp_val = getattr(item, "ir_AbstractActor", None)
                    
                    setattr(item, "ir_AbstractActor", self)
                    

class ir_Type:

    pass
class Declaration:

    pass
class ir_TypeDeclarationImport(Declaration):

    def __init__(self, namespace: str):
        self.namespace = namespace
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

class ir_ForwardDeclaration(Declaration):

    pass
class ir_TypeDeclaration(Declaration):

    pass
class ir_TypeConstructor(Declaration):

    pass
class ir_VariableExternal(Declaration):

    pass
class ir_Variable(Declaration):

    def __init__(self, constant: bool, parameter: bool, ir_Variable: "ir_AbstractActor" = None, ir_Variable113: "ir_VariableReference" = None, ir_Variable183: "ir_Expression" = None, ir_Variable186: "ir_Type" = None, ir_Variable189: "ir_LambdaExpression" = None, ir_Variable194: "ir_ProcExpression" = None, ir_Variable197: "ir_ProcExpression" = None, ir_Variable224: "ir_TypeRecord" = None, ir_Variable240: "ir_TypeConstructor" = None):
        self.constant = constant
        self.parameter = parameter
        self.ir_Variable = ir_Variable
        self.ir_Variable113 = ir_Variable113
        self.ir_Variable183 = ir_Variable183
        self.ir_Variable186 = ir_Variable186
        self.ir_Variable189 = ir_Variable189
        self.ir_Variable194 = ir_Variable194
        self.ir_Variable197 = ir_Variable197
        self.ir_Variable224 = ir_Variable224
        self.ir_Variable240 = ir_Variable240
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def parameter(self) -> bool:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: bool):
        self.__parameter = parameter

    @property
    def ir_Variable224(self):
        return self.__ir_Variable224

    @ir_Variable224.setter
    def ir_Variable224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable224", None)
        self.__ir_Variable224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeRecord"):
                opp_val = getattr(old_value, "ir_TypeRecord", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeRecord"):
                opp_val = getattr(value, "ir_TypeRecord", None)
                if opp_val is None:
                    setattr(value, "ir_TypeRecord", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable183(self):
        return self.__ir_Variable183

    @ir_Variable183.setter
    def ir_Variable183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable183", None)
        self.__ir_Variable183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression184"):
                opp_val = getattr(old_value, "ir_Expression184", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression184"):
                opp_val = getattr(value, "ir_Expression184", None)
                setattr(value, "ir_Expression184", self)

    @property
    def ir_Variable(self):
        return self.__ir_Variable

    @ir_Variable.setter
    def ir_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable", None)
        self.__ir_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_AbstractActor15"):
                opp_val = getattr(old_value, "ir_AbstractActor15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_AbstractActor15"):
                opp_val = getattr(value, "ir_AbstractActor15", None)
                if opp_val is None:
                    setattr(value, "ir_AbstractActor15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable189(self):
        return self.__ir_Variable189

    @ir_Variable189.setter
    def ir_Variable189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable189", None)
        self.__ir_Variable189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_LambdaExpression"):
                opp_val = getattr(old_value, "ir_LambdaExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_LambdaExpression"):
                opp_val = getattr(value, "ir_LambdaExpression", None)
                if opp_val is None:
                    setattr(value, "ir_LambdaExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable240(self):
        return self.__ir_Variable240

    @ir_Variable240.setter
    def ir_Variable240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable240", None)
        self.__ir_Variable240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeConstructor239"):
                opp_val = getattr(old_value, "ir_TypeConstructor239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeConstructor239"):
                opp_val = getattr(value, "ir_TypeConstructor239", None)
                if opp_val is None:
                    setattr(value, "ir_TypeConstructor239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable113(self):
        return self.__ir_Variable113

    @ir_Variable113.setter
    def ir_Variable113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable113", None)
        self.__ir_Variable113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableReference"):
                opp_val = getattr(old_value, "ir_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "ir_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableReference"):
                opp_val = getattr(value, "ir_VariableReference", None)
                setattr(value, "ir_VariableReference", self)

    @property
    def ir_Variable194(self):
        return self.__ir_Variable194

    @ir_Variable194.setter
    def ir_Variable194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable194", None)
        self.__ir_Variable194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ProcExpression"):
                opp_val = getattr(old_value, "ir_ProcExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ProcExpression"):
                opp_val = getattr(value, "ir_ProcExpression", None)
                if opp_val is None:
                    setattr(value, "ir_ProcExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable186(self):
        return self.__ir_Variable186

    @ir_Variable186.setter
    def ir_Variable186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable186", None)
        self.__ir_Variable186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Type187"):
                opp_val = getattr(old_value, "ir_Type187", None)
                if opp_val == self:
                    setattr(old_value, "ir_Type187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Type187"):
                opp_val = getattr(value, "ir_Type187", None)
                setattr(value, "ir_Type187", self)

    @property
    def ir_Variable197(self):
        return self.__ir_Variable197

    @ir_Variable197.setter
    def ir_Variable197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable197", None)
        self.__ir_Variable197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ProcExpression196"):
                opp_val = getattr(old_value, "ir_ProcExpression196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ProcExpression196"):
                opp_val = getattr(value, "ir_ProcExpression196", None)
                if opp_val is None:
                    setattr(value, "ir_ProcExpression196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_VariableImport(Declaration):

    def __init__(self, namespace: str):
        self.namespace = namespace
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

class ir_Annotation:

    def __init__(self, name: str, ir_Annotation: "ir_Node" = None, ir_Annotation256: set["ir_AnnotationArgument"] = None):
        self.name = name
        self.ir_Annotation = ir_Annotation
        self.ir_Annotation256 = ir_Annotation256 if ir_Annotation256 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Annotation256(self):
        return self.__ir_Annotation256

    @ir_Annotation256.setter
    def ir_Annotation256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Annotation__ir_Annotation256", None)
        self.__ir_Annotation256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_AnnotationArgument"):
                    opp_val = getattr(item, "ir_AnnotationArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_AnnotationArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_AnnotationArgument"):
                    opp_val = getattr(item, "ir_AnnotationArgument", None)
                    
                    setattr(item, "ir_AnnotationArgument", self)
                    

    @property
    def ir_Annotation(self):
        return self.__ir_Annotation

    @ir_Annotation.setter
    def ir_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Annotation__ir_Annotation", None)
        self.__ir_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Node"):
                opp_val = getattr(old_value, "ir_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Node"):
                opp_val = getattr(value, "ir_Node", None)
                if opp_val is None:
                    setattr(value, "ir_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_Node:

    def __init__(self, id: str, ir_Node: set["ir_Annotation"] = None):
        self.id = id
        self.ir_Node = ir_Node if ir_Node is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ir_Node(self):
        return self.__ir_Node

    @ir_Node.setter
    def ir_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Node__ir_Node", None)
        self.__ir_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Annotation"):
                    opp_val = getattr(item, "ir_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Annotation"):
                    opp_val = getattr(item, "ir_Annotation", None)
                    
                    setattr(item, "ir_Annotation", self)
                    

class Node:

    pass
class ir_PortInstance(Node):

    def __init__(self, name: str, ir_PortInstance: "ir_ActorInstance" = None, ir_PortInstance40: "ir_ActorInstance" = None, ir_PortInstance44: set["ir_Connection"] = None, ir_PortInstance47: "ir_ActorInstance" = None, ir_PortInstance98: "ir_Point2PointConnection" = None, ir_PortInstance101: "ir_Point2PointConnection" = None, ir_PortInstance103: "ir_FromSource" = None, ir_PortInstance108: "ir_ToSink" = None):
        self.name = name
        self.ir_PortInstance = ir_PortInstance
        self.ir_PortInstance40 = ir_PortInstance40
        self.ir_PortInstance44 = ir_PortInstance44 if ir_PortInstance44 is not None else set()
        self.ir_PortInstance47 = ir_PortInstance47
        self.ir_PortInstance98 = ir_PortInstance98
        self.ir_PortInstance101 = ir_PortInstance101
        self.ir_PortInstance103 = ir_PortInstance103
        self.ir_PortInstance108 = ir_PortInstance108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_PortInstance98(self):
        return self.__ir_PortInstance98

    @ir_PortInstance98.setter
    def ir_PortInstance98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance98", None)
        self.__ir_PortInstance98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Point2PointConnection"):
                opp_val = getattr(old_value, "ir_Point2PointConnection", None)
                if opp_val == self:
                    setattr(old_value, "ir_Point2PointConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Point2PointConnection"):
                opp_val = getattr(value, "ir_Point2PointConnection", None)
                setattr(value, "ir_Point2PointConnection", self)

    @property
    def ir_PortInstance40(self):
        return self.__ir_PortInstance40

    @ir_PortInstance40.setter
    def ir_PortInstance40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance40", None)
        self.__ir_PortInstance40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ActorInstance39"):
                opp_val = getattr(old_value, "ir_ActorInstance39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ActorInstance39"):
                opp_val = getattr(value, "ir_ActorInstance39", None)
                if opp_val is None:
                    setattr(value, "ir_ActorInstance39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_PortInstance44(self):
        return self.__ir_PortInstance44

    @ir_PortInstance44.setter
    def ir_PortInstance44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance44", None)
        self.__ir_PortInstance44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Connection45"):
                    opp_val = getattr(item, "ir_Connection45", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Connection45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Connection45"):
                    opp_val = getattr(item, "ir_Connection45", None)
                    
                    setattr(item, "ir_Connection45", self)
                    

    @property
    def ir_PortInstance101(self):
        return self.__ir_PortInstance101

    @ir_PortInstance101.setter
    def ir_PortInstance101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance101", None)
        self.__ir_PortInstance101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Point2PointConnection100"):
                opp_val = getattr(old_value, "ir_Point2PointConnection100", None)
                if opp_val == self:
                    setattr(old_value, "ir_Point2PointConnection100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Point2PointConnection100"):
                opp_val = getattr(value, "ir_Point2PointConnection100", None)
                setattr(value, "ir_Point2PointConnection100", self)

    @property
    def ir_PortInstance47(self):
        return self.__ir_PortInstance47

    @ir_PortInstance47.setter
    def ir_PortInstance47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance47", None)
        self.__ir_PortInstance47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ActorInstance48"):
                opp_val = getattr(old_value, "ir_ActorInstance48", None)
                if opp_val == self:
                    setattr(old_value, "ir_ActorInstance48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ActorInstance48"):
                opp_val = getattr(value, "ir_ActorInstance48", None)
                setattr(value, "ir_ActorInstance48", self)

    @property
    def ir_PortInstance(self):
        return self.__ir_PortInstance

    @ir_PortInstance.setter
    def ir_PortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance", None)
        self.__ir_PortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ActorInstance37"):
                opp_val = getattr(old_value, "ir_ActorInstance37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ActorInstance37"):
                opp_val = getattr(value, "ir_ActorInstance37", None)
                if opp_val is None:
                    setattr(value, "ir_ActorInstance37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_PortInstance103(self):
        return self.__ir_PortInstance103

    @ir_PortInstance103.setter
    def ir_PortInstance103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance103", None)
        self.__ir_PortInstance103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_FromSource"):
                opp_val = getattr(old_value, "ir_FromSource", None)
                if opp_val == self:
                    setattr(old_value, "ir_FromSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_FromSource"):
                opp_val = getattr(value, "ir_FromSource", None)
                setattr(value, "ir_FromSource", self)

    @property
    def ir_PortInstance108(self):
        return self.__ir_PortInstance108

    @ir_PortInstance108.setter
    def ir_PortInstance108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PortInstance__ir_PortInstance108", None)
        self.__ir_PortInstance108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ToSink"):
                opp_val = getattr(old_value, "ir_ToSink", None)
                if opp_val == self:
                    setattr(old_value, "ir_ToSink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ToSink"):
                opp_val = getattr(value, "ir_ToSink", None)
                setattr(value, "ir_ToSink", self)

class ir_VariableReference(Node):

    pass
class ir_Member(Node):

    def __init__(self, name: str, ir_Member: "ir_VariableExpression" = None, ir_Member72: set["ir_Expression"] = None, ir_Member75: "ir_Type" = None, ir_Member119: "ir_VariableReference" = None):
        self.name = name
        self.ir_Member = ir_Member
        self.ir_Member72 = ir_Member72 if ir_Member72 is not None else set()
        self.ir_Member75 = ir_Member75
        self.ir_Member119 = ir_Member119
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Member(self):
        return self.__ir_Member

    @ir_Member.setter
    def ir_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Member__ir_Member", None)
        self.__ir_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableExpression63"):
                opp_val = getattr(old_value, "ir_VariableExpression63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableExpression63"):
                opp_val = getattr(value, "ir_VariableExpression63", None)
                if opp_val is None:
                    setattr(value, "ir_VariableExpression63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Member75(self):
        return self.__ir_Member75

    @ir_Member75.setter
    def ir_Member75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Member__ir_Member75", None)
        self.__ir_Member75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Type76"):
                opp_val = getattr(old_value, "ir_Type76", None)
                if opp_val == self:
                    setattr(old_value, "ir_Type76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Type76"):
                opp_val = getattr(value, "ir_Type76", None)
                setattr(value, "ir_Type76", self)

    @property
    def ir_Member119(self):
        return self.__ir_Member119

    @ir_Member119.setter
    def ir_Member119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Member__ir_Member119", None)
        self.__ir_Member119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableReference118"):
                opp_val = getattr(old_value, "ir_VariableReference118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableReference118"):
                opp_val = getattr(value, "ir_VariableReference118", None)
                if opp_val is None:
                    setattr(value, "ir_VariableReference118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Member72(self):
        return self.__ir_Member72

    @ir_Member72.setter
    def ir_Member72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Member__ir_Member72", None)
        self.__ir_Member72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Expression73"):
                    opp_val = getattr(item, "ir_Expression73", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Expression73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Expression73"):
                    opp_val = getattr(item, "ir_Expression73", None)
                    
                    setattr(item, "ir_Expression73", self)
                    

class ir_PortAccess(Node):

    pass
class ir_Expression(Node):

    pass
class ir_Declaration(Node):

    def __init__(self, name: str, ir_Declaration: "ir_Scope" = None, ir_Declaration58: "ir_VariableExpression" = None, ir_Declaration93: "ir_TypeConstructorCall" = None, ir_Declaration137: "ir_ProcCall" = None, ir_Declaration172: "ir_Scope" = None, ir_Declaration175: set["ir_TaggedExpression"] = None, ir_Declaration178: "ir_ForwardDeclaration" = None, ir_Declaration226: "ir_TypeUser" = None):
        self.name = name
        self.ir_Declaration = ir_Declaration
        self.ir_Declaration58 = ir_Declaration58
        self.ir_Declaration93 = ir_Declaration93
        self.ir_Declaration137 = ir_Declaration137
        self.ir_Declaration172 = ir_Declaration172
        self.ir_Declaration175 = ir_Declaration175 if ir_Declaration175 is not None else set()
        self.ir_Declaration178 = ir_Declaration178
        self.ir_Declaration226 = ir_Declaration226
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Declaration(self):
        return self.__ir_Declaration

    @ir_Declaration.setter
    def ir_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration", None)
        self.__ir_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Scope"):
                opp_val = getattr(old_value, "ir_Scope", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Scope"):
                opp_val = getattr(value, "ir_Scope", None)
                if opp_val is None:
                    setattr(value, "ir_Scope", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Declaration226(self):
        return self.__ir_Declaration226

    @ir_Declaration226.setter
    def ir_Declaration226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration226", None)
        self.__ir_Declaration226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeUser"):
                opp_val = getattr(old_value, "ir_TypeUser", None)
                if opp_val == self:
                    setattr(old_value, "ir_TypeUser", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeUser"):
                opp_val = getattr(value, "ir_TypeUser", None)
                setattr(value, "ir_TypeUser", self)

    @property
    def ir_Declaration93(self):
        return self.__ir_Declaration93

    @ir_Declaration93.setter
    def ir_Declaration93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration93", None)
        self.__ir_Declaration93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeConstructorCall92"):
                opp_val = getattr(old_value, "ir_TypeConstructorCall92", None)
                if opp_val == self:
                    setattr(old_value, "ir_TypeConstructorCall92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeConstructorCall92"):
                opp_val = getattr(value, "ir_TypeConstructorCall92", None)
                setattr(value, "ir_TypeConstructorCall92", self)

    @property
    def ir_Declaration175(self):
        return self.__ir_Declaration175

    @ir_Declaration175.setter
    def ir_Declaration175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration175", None)
        self.__ir_Declaration175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_TaggedExpression176"):
                    opp_val = getattr(item, "ir_TaggedExpression176", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_TaggedExpression176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_TaggedExpression176"):
                    opp_val = getattr(item, "ir_TaggedExpression176", None)
                    
                    setattr(item, "ir_TaggedExpression176", self)
                    

    @property
    def ir_Declaration172(self):
        return self.__ir_Declaration172

    @ir_Declaration172.setter
    def ir_Declaration172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration172", None)
        self.__ir_Declaration172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Scope173"):
                opp_val = getattr(old_value, "ir_Scope173", None)
                if opp_val == self:
                    setattr(old_value, "ir_Scope173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Scope173"):
                opp_val = getattr(value, "ir_Scope173", None)
                setattr(value, "ir_Scope173", self)

    @property
    def ir_Declaration137(self):
        return self.__ir_Declaration137

    @ir_Declaration137.setter
    def ir_Declaration137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration137", None)
        self.__ir_Declaration137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ProcCall136"):
                opp_val = getattr(old_value, "ir_ProcCall136", None)
                if opp_val == self:
                    setattr(old_value, "ir_ProcCall136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ProcCall136"):
                opp_val = getattr(value, "ir_ProcCall136", None)
                setattr(value, "ir_ProcCall136", self)

    @property
    def ir_Declaration178(self):
        return self.__ir_Declaration178

    @ir_Declaration178.setter
    def ir_Declaration178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration178", None)
        self.__ir_Declaration178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ForwardDeclaration"):
                opp_val = getattr(old_value, "ir_ForwardDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "ir_ForwardDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ForwardDeclaration"):
                opp_val = getattr(value, "ir_ForwardDeclaration", None)
                setattr(value, "ir_ForwardDeclaration", self)

    @property
    def ir_Declaration58(self):
        return self.__ir_Declaration58

    @ir_Declaration58.setter
    def ir_Declaration58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Declaration__ir_Declaration58", None)
        self.__ir_Declaration58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableExpression"):
                opp_val = getattr(old_value, "ir_VariableExpression", None)
                if opp_val == self:
                    setattr(old_value, "ir_VariableExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableExpression"):
                opp_val = getattr(value, "ir_VariableExpression", None)
                setattr(value, "ir_VariableExpression", self)

class ir_TypeRecord(Type, Node):

    pass
class ir_Statement(Node):

    pass
class ir_Connection(Node):

    pass
class ir_Port(Node):

    def __init__(self, name: str, ir_Port: "ir_AbstractActor" = None, ir_Port13: "ir_AbstractActor" = None, ir_Port34: "ir_Type" = None, ir_Port106: "ir_FromSource" = None, ir_Port111: "ir_ToSink" = None, ir_Port159: "ir_PortAccess" = None):
        self.name = name
        self.ir_Port = ir_Port
        self.ir_Port13 = ir_Port13
        self.ir_Port34 = ir_Port34
        self.ir_Port106 = ir_Port106
        self.ir_Port111 = ir_Port111
        self.ir_Port159 = ir_Port159
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Port111(self):
        return self.__ir_Port111

    @ir_Port111.setter
    def ir_Port111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port111", None)
        self.__ir_Port111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ToSink110"):
                opp_val = getattr(old_value, "ir_ToSink110", None)
                if opp_val == self:
                    setattr(old_value, "ir_ToSink110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ToSink110"):
                opp_val = getattr(value, "ir_ToSink110", None)
                setattr(value, "ir_ToSink110", self)

    @property
    def ir_Port(self):
        return self.__ir_Port

    @ir_Port.setter
    def ir_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port", None)
        self.__ir_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_AbstractActor10"):
                opp_val = getattr(old_value, "ir_AbstractActor10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_AbstractActor10"):
                opp_val = getattr(value, "ir_AbstractActor10", None)
                if opp_val is None:
                    setattr(value, "ir_AbstractActor10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Port13(self):
        return self.__ir_Port13

    @ir_Port13.setter
    def ir_Port13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port13", None)
        self.__ir_Port13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_AbstractActor12"):
                opp_val = getattr(old_value, "ir_AbstractActor12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_AbstractActor12"):
                opp_val = getattr(value, "ir_AbstractActor12", None)
                if opp_val is None:
                    setattr(value, "ir_AbstractActor12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Port106(self):
        return self.__ir_Port106

    @ir_Port106.setter
    def ir_Port106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port106", None)
        self.__ir_Port106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_FromSource105"):
                opp_val = getattr(old_value, "ir_FromSource105", None)
                if opp_val == self:
                    setattr(old_value, "ir_FromSource105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_FromSource105"):
                opp_val = getattr(value, "ir_FromSource105", None)
                setattr(value, "ir_FromSource105", self)

    @property
    def ir_Port34(self):
        return self.__ir_Port34

    @ir_Port34.setter
    def ir_Port34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port34", None)
        self.__ir_Port34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Type35"):
                opp_val = getattr(old_value, "ir_Type35", None)
                if opp_val == self:
                    setattr(old_value, "ir_Type35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Type35"):
                opp_val = getattr(value, "ir_Type35", None)
                setattr(value, "ir_Type35", self)

    @property
    def ir_Port159(self):
        return self.__ir_Port159

    @ir_Port159.setter
    def ir_Port159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Port__ir_Port159", None)
        self.__ir_Port159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_PortAccess"):
                opp_val = getattr(old_value, "ir_PortAccess", None)
                if opp_val == self:
                    setattr(old_value, "ir_PortAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_PortAccess"):
                opp_val = getattr(value, "ir_PortAccess", None)
                setattr(value, "ir_PortAccess", self)

class ir_Scope(Node):

    pass