from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CompoundTask:

    pass
class workflow_LoopTask(CompoundTask):

    def __init__(self, whileCondition: str):
        self.whileCondition = whileCondition
        
    @property
    def whileCondition(self) -> str:
        return self.__whileCondition

    @whileCondition.setter
    def whileCondition(self, whileCondition: str):
        self.__whileCondition = whileCondition

class WorkflowNode:

    pass
class workflow_Task(WorkflowNode):

    pass
class workflow_TransformationTask(WorkflowNode):

    def __init__(self, transformExpression: str):
        self.transformExpression = transformExpression
        
    @property
    def transformExpression(self) -> str:
        return self.__transformExpression

    @transformExpression.setter
    def transformExpression(self, transformExpression: str):
        self.__transformExpression = transformExpression

class workflow_ConditionalTask(WorkflowNode):

    pass
class workflow_CompoundTask(WorkflowNode):

    pass
class OutputPort:

    pass
class workflow_Fault(OutputPort):

    pass
class Port:

    pass
class workflow_ConditionalOutputPort(OutputPort):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class workflow_WorkflowElement(ABC):

    def __init__(self, name: str, comment: str, x: int, y: int, width: int, height: int, id: str):
        self.name = name
        self.comment = comment
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class WorkflowElement:

    pass
class workflow_Edge(WorkflowElement):

    pass
class workflow_WorkflowNode(WorkflowElement):

    def __init__(self, isStart: bool, isFinish: bool, nodes: "workflow_Workflow" = None, node: set["workflow_OutputPort"] = None, node8: set["workflow_InputPort"] = None, WorkflowNode: "workflow_Workflow" = None, WorkflowNode18: "workflow_InputPort" = None, WorkflowNode22: "workflow_OutputPort" = None):
        self.isStart = isStart
        self.isFinish = isFinish
        self.nodes = nodes
        self.node = node if node is not None else set()
        self.node8 = node8 if node8 is not None else set()
        self.WorkflowNode = WorkflowNode
        self.WorkflowNode18 = WorkflowNode18
        self.WorkflowNode22 = WorkflowNode22
        
    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

    @property
    def isFinish(self) -> bool:
        return self.__isFinish

    @isFinish.setter
    def isFinish(self, isFinish: bool):
        self.__isFinish = isFinish

    @property
    def node8(self):
        return self.__node8

    @node8.setter
    def node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__node8", None)
        self.__node8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPort"):
                    opp_val = getattr(item, "InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPort"):
                    opp_val = getattr(item, "InputPort", None)
                    
                    setattr(item, "InputPort", self)
                    

    @property
    def WorkflowNode(self):
        return self.__WorkflowNode

    @WorkflowNode.setter
    def WorkflowNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__WorkflowNode", None)
        self.__WorkflowNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow"):
                opp_val = getattr(old_value, "workflow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow"):
                opp_val = getattr(value, "workflow", None)
                if opp_val is None:
                    setattr(value, "workflow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workflow"):
                opp_val = getattr(old_value, "Workflow", None)
                if opp_val == self:
                    setattr(old_value, "Workflow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workflow"):
                opp_val = getattr(value, "Workflow", None)
                setattr(value, "Workflow", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPort"):
                    opp_val = getattr(item, "OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPort"):
                    opp_val = getattr(item, "OutputPort", None)
                    
                    setattr(item, "OutputPort", self)
                    

    @property
    def WorkflowNode22(self):
        return self.__WorkflowNode22

    @WorkflowNode22.setter
    def WorkflowNode22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__WorkflowNode22", None)
        self.__WorkflowNode22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputs"):
                opp_val = getattr(old_value, "outputs", None)
                if opp_val == self:
                    setattr(old_value, "outputs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputs"):
                opp_val = getattr(value, "outputs", None)
                setattr(value, "outputs", self)

    @property
    def WorkflowNode18(self):
        return self.__WorkflowNode18

    @WorkflowNode18.setter
    def WorkflowNode18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_WorkflowNode__WorkflowNode18", None)
        self.__WorkflowNode18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputs"):
                opp_val = getattr(old_value, "inputs", None)
                if opp_val == self:
                    setattr(old_value, "inputs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputs"):
                opp_val = getattr(value, "inputs", None)
                setattr(value, "inputs", self)

class workflow_Port(WorkflowElement):

    pass
class workflow_Workflow(WorkflowElement):

    pass
class workflow_InputPort(Port):

    pass
class workflow_OutputPort(Port):

    pass
class workflow_Comment(WorkflowElement):

    pass