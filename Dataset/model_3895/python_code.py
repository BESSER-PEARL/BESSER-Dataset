from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Language(Enum):
    Python = "Python"
    Java = "Java"
class TaskStatus(Enum):
    FINISHED = "FINISHED"
    PREPARED = "PREPARED"
    NOT_PREPARED = "NOT_PREPARED"
    PROCESSING = "PROCESSING"


############################################
# Definition of Classes
############################################

class TaskInput:

    pass
class workflow_Connection(TaskInput):

    pass
class SimpleTask:

    pass
class workflow_LibraryTask(SimpleTask):

    pass
class TypedElement:

    pass
class workflow_Setter(TypedElement, TaskInput):

    pass
class IsInitSetter:

    pass
class workflow_IsNotInitSetter(IsInitSetter):

    pass
class Nsetter:

    pass
class workflow_IsInitSetter(Nsetter):

    pass
class Setter:

    pass
class workflow_Nsetter(Setter):

    pass
class workflow_CustomTask(SimpleTask):

    def __init__(self, runner: str):
        self.runner = runner
        
    @property
    def runner(self) -> str:
        return self.__runner

    @runner.setter
    def runner(self, runner: str):
        self.__runner = runner

class NamedElement:

    pass
class workflow_Workflow(NamedElement):

    def __init__(self, language: str, workflow_Workflow: "workflow_BaseTask" = None, workflow_Workflow13: set["workflow_LibraryFunction"] = None):
        self.language = language
        self.workflow_Workflow = workflow_Workflow
        self.workflow_Workflow13 = workflow_Workflow13 if workflow_Workflow13 is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def workflow_Workflow13(self):
        return self.__workflow_Workflow13

    @workflow_Workflow13.setter
    def workflow_Workflow13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Workflow__workflow_Workflow13", None)
        self.__workflow_Workflow13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_LibraryFunction14"):
                    opp_val = getattr(item, "workflow_LibraryFunction14", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_LibraryFunction14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_LibraryFunction14"):
                    opp_val = getattr(item, "workflow_LibraryFunction14", None)
                    
                    setattr(item, "workflow_LibraryFunction14", self)
                    

    @property
    def workflow_Workflow(self):
        return self.__workflow_Workflow

    @workflow_Workflow.setter
    def workflow_Workflow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Workflow__workflow_Workflow", None)
        self.__workflow_Workflow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_BaseTask11"):
                opp_val = getattr(old_value, "workflow_BaseTask11", None)
                if opp_val == self:
                    setattr(old_value, "workflow_BaseTask11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_BaseTask11"):
                opp_val = getattr(value, "workflow_BaseTask11", None)
                setattr(value, "workflow_BaseTask11", self)

class workflow_Output(TypedElement, NamedElement):

    pass
class workflow_LibraryFunction(NamedElement):

    def __init__(self, function: str, workflow_LibraryFunction: set["workflow_Output"] = None, workflow_LibraryFunction7: set["workflow_Input"] = None, workflow_LibraryFunction9: "workflow_LibraryTask" = None, workflow_LibraryFunction14: "workflow_Workflow" = None):
        self.function = function
        self.workflow_LibraryFunction = workflow_LibraryFunction if workflow_LibraryFunction is not None else set()
        self.workflow_LibraryFunction7 = workflow_LibraryFunction7 if workflow_LibraryFunction7 is not None else set()
        self.workflow_LibraryFunction9 = workflow_LibraryFunction9
        self.workflow_LibraryFunction14 = workflow_LibraryFunction14
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def workflow_LibraryFunction14(self):
        return self.__workflow_LibraryFunction14

    @workflow_LibraryFunction14.setter
    def workflow_LibraryFunction14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_LibraryFunction__workflow_LibraryFunction14", None)
        self.__workflow_LibraryFunction14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Workflow13"):
                opp_val = getattr(old_value, "workflow_Workflow13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Workflow13"):
                opp_val = getattr(value, "workflow_Workflow13", None)
                if opp_val is None:
                    setattr(value, "workflow_Workflow13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_LibraryFunction7(self):
        return self.__workflow_LibraryFunction7

    @workflow_LibraryFunction7.setter
    def workflow_LibraryFunction7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_LibraryFunction__workflow_LibraryFunction7", None)
        self.__workflow_LibraryFunction7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Input"):
                    opp_val = getattr(item, "workflow_Input", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Input"):
                    opp_val = getattr(item, "workflow_Input", None)
                    
                    setattr(item, "workflow_Input", self)
                    

    @property
    def workflow_LibraryFunction(self):
        return self.__workflow_LibraryFunction

    @workflow_LibraryFunction.setter
    def workflow_LibraryFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_LibraryFunction__workflow_LibraryFunction", None)
        self.__workflow_LibraryFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Output"):
                    opp_val = getattr(item, "workflow_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Output"):
                    opp_val = getattr(item, "workflow_Output", None)
                    
                    setattr(item, "workflow_Output", self)
                    

    @property
    def workflow_LibraryFunction9(self):
        return self.__workflow_LibraryFunction9

    @workflow_LibraryFunction9.setter
    def workflow_LibraryFunction9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_LibraryFunction__workflow_LibraryFunction9", None)
        self.__workflow_LibraryFunction9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_LibraryTask"):
                opp_val = getattr(old_value, "workflow_LibraryTask", None)
                if opp_val == self:
                    setattr(old_value, "workflow_LibraryTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_LibraryTask"):
                opp_val = getattr(value, "workflow_LibraryTask", None)
                setattr(value, "workflow_LibraryTask", self)

class workflow_TaskOutput(TypedElement, NamedElement):

    pass
class workflow_Input(TypedElement, NamedElement):

    pass
class workflow_TaskInput(NamedElement):

    pass
class workflow_AbstractTask(NamedElement):

    def __init__(self, status: str, workflow_AbstractTask: set["workflow_TaskInput"] = None, workflow_AbstractTask2: set["workflow_TaskOutput"] = None, workflow_AbstractTask4: "workflow_BaseTask" = None):
        self.status = status
        self.workflow_AbstractTask = workflow_AbstractTask if workflow_AbstractTask is not None else set()
        self.workflow_AbstractTask2 = workflow_AbstractTask2 if workflow_AbstractTask2 is not None else set()
        self.workflow_AbstractTask4 = workflow_AbstractTask4
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def workflow_AbstractTask(self):
        return self.__workflow_AbstractTask

    @workflow_AbstractTask.setter
    def workflow_AbstractTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_AbstractTask__workflow_AbstractTask", None)
        self.__workflow_AbstractTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_TaskInput"):
                    opp_val = getattr(item, "workflow_TaskInput", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_TaskInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_TaskInput"):
                    opp_val = getattr(item, "workflow_TaskInput", None)
                    
                    setattr(item, "workflow_TaskInput", self)
                    

    @property
    def workflow_AbstractTask2(self):
        return self.__workflow_AbstractTask2

    @workflow_AbstractTask2.setter
    def workflow_AbstractTask2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_AbstractTask__workflow_AbstractTask2", None)
        self.__workflow_AbstractTask2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_TaskOutput"):
                    opp_val = getattr(item, "workflow_TaskOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_TaskOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_TaskOutput"):
                    opp_val = getattr(item, "workflow_TaskOutput", None)
                    
                    setattr(item, "workflow_TaskOutput", self)
                    

    @property
    def workflow_AbstractTask4(self):
        return self.__workflow_AbstractTask4

    @workflow_AbstractTask4.setter
    def workflow_AbstractTask4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_AbstractTask__workflow_AbstractTask4", None)
        self.__workflow_AbstractTask4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_BaseTask"):
                opp_val = getattr(old_value, "workflow_BaseTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_BaseTask"):
                opp_val = getattr(value, "workflow_BaseTask", None)
                if opp_val is None:
                    setattr(value, "workflow_BaseTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractTask:

    pass
class workflow_BaseTask(AbstractTask):

    pass
class workflow_SimpleTask(AbstractTask):

    pass
class workflow_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class workflow_TypedElement:

    def __init__(self, typeAsString: str, valueAsString: str):
        self.typeAsString = typeAsString
        self.valueAsString = valueAsString
        
    @property
    def typeAsString(self) -> str:
        return self.__typeAsString

    @typeAsString.setter
    def typeAsString(self, typeAsString: str):
        self.__typeAsString = typeAsString

    @property
    def valueAsString(self) -> str:
        return self.__valueAsString

    @valueAsString.setter
    def valueAsString(self, valueAsString: str):
        self.__valueAsString = valueAsString
