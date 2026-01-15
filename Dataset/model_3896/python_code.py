from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Parameter:

    pass
class workflow_InputParameter(Parameter):

    pass
class workflow_OutputParameter(Parameter):

    pass
class workflow_Program:

    def __init__(self, name_exec: str, description: str, exec_order: int, workflow_Program: set["workflow_Parameter"] = None, workflow_Program10: "workflow_SimpleCommand" = None):
        self.name_exec = name_exec
        self.description = description
        self.exec_order = exec_order
        self.workflow_Program = workflow_Program if workflow_Program is not None else set()
        self.workflow_Program10 = workflow_Program10
        
    @property
    def exec_order(self) -> int:
        return self.__exec_order

    @exec_order.setter
    def exec_order(self, exec_order: int):
        self.__exec_order = exec_order

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name_exec(self) -> str:
        return self.__name_exec

    @name_exec.setter
    def name_exec(self, name_exec: str):
        self.__name_exec = name_exec

    @property
    def workflow_Program(self):
        return self.__workflow_Program

    @workflow_Program.setter
    def workflow_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Program__workflow_Program", None)
        self.__workflow_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Parameter"):
                    opp_val = getattr(item, "workflow_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Parameter"):
                    opp_val = getattr(item, "workflow_Parameter", None)
                    
                    setattr(item, "workflow_Parameter", self)
                    

    @property
    def workflow_Program10(self):
        return self.__workflow_Program10

    @workflow_Program10.setter
    def workflow_Program10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Program__workflow_Program10", None)
        self.__workflow_Program10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_SimpleCommand"):
                opp_val = getattr(old_value, "workflow_SimpleCommand", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_SimpleCommand"):
                opp_val = getattr(value, "workflow_SimpleCommand", None)
                if opp_val is None:
                    setattr(value, "workflow_SimpleCommand", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Statement:

    pass
class workflow_ForEach(Statement):

    def __init__(self, element: str, sequence: str, workflow_ForEach: set["workflow_Statement"] = None):
        self.element = element
        self.sequence = sequence
        self.workflow_ForEach = workflow_ForEach if workflow_ForEach is not None else set()
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def sequence(self) -> str:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: str):
        self.__sequence = sequence

    @property
    def workflow_ForEach(self):
        return self.__workflow_ForEach

    @workflow_ForEach.setter
    def workflow_ForEach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ForEach__workflow_ForEach", None)
        self.__workflow_ForEach = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Statement16"):
                    opp_val = getattr(item, "workflow_Statement16", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Statement16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Statement16"):
                    opp_val = getattr(item, "workflow_Statement16", None)
                    
                    setattr(item, "workflow_Statement16", self)
                    

class workflow_SimpleCommand(Statement):

    def __init__(self, description: str, workflow_SimpleCommand: set["workflow_Program"] = None):
        self.description = description
        self.workflow_SimpleCommand = workflow_SimpleCommand if workflow_SimpleCommand is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def workflow_SimpleCommand(self):
        return self.__workflow_SimpleCommand

    @workflow_SimpleCommand.setter
    def workflow_SimpleCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_SimpleCommand__workflow_SimpleCommand", None)
        self.__workflow_SimpleCommand = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Program10"):
                    opp_val = getattr(item, "workflow_Program10", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Program10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Program10"):
                    opp_val = getattr(item, "workflow_Program10", None)
                    
                    setattr(item, "workflow_Program10", self)
                    

class workflow_Condition(Statement):

    def __init__(self, description: str, expression: str, workflow_Condition: "workflow_Statement" = None, workflow_Condition6: "workflow_Statement" = None):
        self.description = description
        self.expression = expression
        self.workflow_Condition = workflow_Condition
        self.workflow_Condition6 = workflow_Condition6
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def workflow_Condition6(self):
        return self.__workflow_Condition6

    @workflow_Condition6.setter
    def workflow_Condition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Condition__workflow_Condition6", None)
        self.__workflow_Condition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Statement7"):
                opp_val = getattr(old_value, "workflow_Statement7", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Statement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Statement7"):
                opp_val = getattr(value, "workflow_Statement7", None)
                setattr(value, "workflow_Statement7", self)

    @property
    def workflow_Condition(self):
        return self.__workflow_Condition

    @workflow_Condition.setter
    def workflow_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Condition__workflow_Condition", None)
        self.__workflow_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Statement4"):
                opp_val = getattr(old_value, "workflow_Statement4", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Statement4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Statement4"):
                opp_val = getattr(value, "workflow_Statement4", None)
                setattr(value, "workflow_Statement4", self)

class workflow_Parameter(ABC):

    def __init__(self, option: str, data: str, workflow_Parameter: "workflow_Program" = None):
        self.option = option
        self.data = data
        self.workflow_Parameter = workflow_Parameter
        
    @property
    def option(self) -> str:
        return self.__option

    @option.setter
    def option(self, option: str):
        self.__option = option

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def workflow_Parameter(self):
        return self.__workflow_Parameter

    @workflow_Parameter.setter
    def workflow_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Parameter__workflow_Parameter", None)
        self.__workflow_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Program"):
                opp_val = getattr(old_value, "workflow_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Program"):
                opp_val = getattr(value, "workflow_Program", None)
                if opp_val is None:
                    setattr(value, "workflow_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_Statement(ABC):

    def __init__(self, exec_order: int, workflow_Statement: "workflow_Recipe" = None, workflow_Statement4: "workflow_Condition" = None, workflow_Statement7: "workflow_Condition" = None, workflow_Statement16: "workflow_ForEach" = None):
        self.exec_order = exec_order
        self.workflow_Statement = workflow_Statement
        self.workflow_Statement4 = workflow_Statement4
        self.workflow_Statement7 = workflow_Statement7
        self.workflow_Statement16 = workflow_Statement16
        
    @property
    def exec_order(self) -> int:
        return self.__exec_order

    @exec_order.setter
    def exec_order(self, exec_order: int):
        self.__exec_order = exec_order

    @property
    def workflow_Statement(self):
        return self.__workflow_Statement

    @workflow_Statement.setter
    def workflow_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Statement__workflow_Statement", None)
        self.__workflow_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Recipe2"):
                opp_val = getattr(old_value, "workflow_Recipe2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Recipe2"):
                opp_val = getattr(value, "workflow_Recipe2", None)
                if opp_val is None:
                    setattr(value, "workflow_Recipe2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Statement7(self):
        return self.__workflow_Statement7

    @workflow_Statement7.setter
    def workflow_Statement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Statement__workflow_Statement7", None)
        self.__workflow_Statement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Condition6"):
                opp_val = getattr(old_value, "workflow_Condition6", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Condition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Condition6"):
                opp_val = getattr(value, "workflow_Condition6", None)
                setattr(value, "workflow_Condition6", self)

    @property
    def workflow_Statement16(self):
        return self.__workflow_Statement16

    @workflow_Statement16.setter
    def workflow_Statement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Statement__workflow_Statement16", None)
        self.__workflow_Statement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ForEach"):
                opp_val = getattr(old_value, "workflow_ForEach", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ForEach"):
                opp_val = getattr(value, "workflow_ForEach", None)
                if opp_val is None:
                    setattr(value, "workflow_ForEach", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_Statement4(self):
        return self.__workflow_Statement4

    @workflow_Statement4.setter
    def workflow_Statement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Statement__workflow_Statement4", None)
        self.__workflow_Statement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Condition"):
                opp_val = getattr(old_value, "workflow_Condition", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Condition"):
                opp_val = getattr(value, "workflow_Condition", None)
                setattr(value, "workflow_Condition", self)

class workflow_Recipe:

    def __init__(self, name: str, workflow_Recipe: "workflow_Workflow" = None, workflow_Recipe2: set["workflow_Statement"] = None):
        self.name = name
        self.workflow_Recipe = workflow_Recipe
        self.workflow_Recipe2 = workflow_Recipe2 if workflow_Recipe2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Recipe2(self):
        return self.__workflow_Recipe2

    @workflow_Recipe2.setter
    def workflow_Recipe2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Recipe__workflow_Recipe2", None)
        self.__workflow_Recipe2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Statement"):
                    opp_val = getattr(item, "workflow_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Statement"):
                    opp_val = getattr(item, "workflow_Statement", None)
                    
                    setattr(item, "workflow_Statement", self)
                    

    @property
    def workflow_Recipe(self):
        return self.__workflow_Recipe

    @workflow_Recipe.setter
    def workflow_Recipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Recipe__workflow_Recipe", None)
        self.__workflow_Recipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Workflow"):
                opp_val = getattr(old_value, "workflow_Workflow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Workflow"):
                opp_val = getattr(value, "workflow_Workflow", None)
                if opp_val is None:
                    setattr(value, "workflow_Workflow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_Workflow:

    def __init__(self, name: str, workflow_Workflow: set["workflow_Recipe"] = None):
        self.name = name
        self.workflow_Workflow = workflow_Workflow if workflow_Workflow is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Workflow(self):
        return self.__workflow_Workflow

    @workflow_Workflow.setter
    def workflow_Workflow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Workflow__workflow_Workflow", None)
        self.__workflow_Workflow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Recipe"):
                    opp_val = getattr(item, "workflow_Recipe", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Recipe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Recipe"):
                    opp_val = getattr(item, "workflow_Recipe", None)
                    
                    setattr(item, "workflow_Recipe", self)
                    
