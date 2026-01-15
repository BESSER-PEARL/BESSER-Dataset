from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IPort:

    pass
class workflow_IOutputPort(IPort):

    pass
class workflow_IWorkflowElement(ABC):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class IWorkflowNode:

    pass
class workflow_IWorkflowJob(IWorkflowNode):

    def __init__(self, jobDescription: str, jobDescriptionFileName: str):
        self.jobDescription = jobDescription
        self.jobDescriptionFileName = jobDescriptionFileName
        
    @property
    def jobDescriptionFileName(self) -> str:
        return self.__jobDescriptionFileName

    @jobDescriptionFileName.setter
    def jobDescriptionFileName(self, jobDescriptionFileName: str):
        self.__jobDescriptionFileName = jobDescriptionFileName

    @property
    def jobDescription(self) -> str:
        return self.__jobDescription

    @jobDescription.setter
    def jobDescription(self, jobDescription: str):
        self.__jobDescription = jobDescription

class workflow_IInputPort(IPort):

    pass
class IWorkflowElement:

    pass
class workflow_IWorkflowNode(IWorkflowElement):

    def __init__(self, isStart: bool, isFinish: bool, IWorkflowNode12: "workflow_IWorkflow" = None, nodes: "workflow_IWorkflow" = None, node: set["workflow_IOutputPort"] = None, node21: set["workflow_IInputPort"] = None, IWorkflowNode: "workflow_IInputPort" = None, IWorkflowNode8: "workflow_IOutputPort" = None):
        self.isStart = isStart
        self.isFinish = isFinish
        self.IWorkflowNode12 = IWorkflowNode12
        self.nodes = nodes
        self.node = node if node is not None else set()
        self.node21 = node21 if node21 is not None else set()
        self.IWorkflowNode = IWorkflowNode
        self.IWorkflowNode8 = IWorkflowNode8
        
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
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IWorkflow17"):
                opp_val = getattr(old_value, "IWorkflow17", None)
                if opp_val == self:
                    setattr(old_value, "IWorkflow17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IWorkflow17"):
                opp_val = getattr(value, "IWorkflow17", None)
                setattr(value, "IWorkflow17", self)

    @property
    def IWorkflowNode12(self):
        return self.__IWorkflowNode12

    @IWorkflowNode12.setter
    def IWorkflowNode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__IWorkflowNode12", None)
        self.__IWorkflowNode12 = value
        
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
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOutputPort19"):
                    opp_val = getattr(item, "IOutputPort19", None)
                    
                    if opp_val == self:
                        setattr(item, "IOutputPort19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOutputPort19"):
                    opp_val = getattr(item, "IOutputPort19", None)
                    
                    setattr(item, "IOutputPort19", self)
                    

    @property
    def IWorkflowNode(self):
        return self.__IWorkflowNode

    @IWorkflowNode.setter
    def IWorkflowNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__IWorkflowNode", None)
        self.__IWorkflowNode = value
        
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

    @property
    def IWorkflowNode8(self):
        return self.__IWorkflowNode8

    @IWorkflowNode8.setter
    def IWorkflowNode8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__IWorkflowNode8", None)
        self.__IWorkflowNode8 = value
        
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
    def node21(self):
        return self.__node21

    @node21.setter
    def node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_IWorkflowNode__node21", None)
        self.__node21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IInputPort22"):
                    opp_val = getattr(item, "IInputPort22", None)
                    
                    if opp_val == self:
                        setattr(item, "IInputPort22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IInputPort22"):
                    opp_val = getattr(item, "IInputPort22", None)
                    
                    setattr(item, "IInputPort22", self)
                    

class workflow_IWorkflow(IWorkflowElement):

    pass
class workflow_ILink(IWorkflowElement):

    pass
class workflow_IPort(IWorkflowElement):

    def __init__(self, fileName: str):
        self.fileName = fileName
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName
