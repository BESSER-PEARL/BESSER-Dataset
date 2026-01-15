from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TaskStatus(Enum):
    todo = "todo"
    in_progress = "in_progress"
    skipped = "skipped"
    done = "done"
class UrlPattern(Enum):
    ANT = "ANT"
class Language(Enum):
    C_Sharp = "C_Sharp"
    Scala = "Scala"
    PHP = "PHP"
    C_Cpp = "C_Cpp"
    Ruby = "Ruby"
    Other = "Other"
    Java = "Java"
    Python = "Python"
class HttpMethod(Enum):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    CONNECT = "CONNECT"
    PATCH = "PATCH"


############################################
# Definition of Classes
############################################

class assessment_Notes(ABC):

    def __init__(self, notes: str):
        self.notes = notes
        
    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

class assessment_Contents(ABC):

    def __init__(self, contents: str):
        self.contents = contents
        
    @property
    def contents(self) -> str:
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

class assessment_Label(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class assessment_Graph(ABC):

    pass
class Contents:

    pass
class assessment_Url:

    def __init__(self, pattern: str, patternType: str):
        self.pattern = pattern
        self.patternType = patternType
        
    @property
    def patternType(self) -> str:
        return self.__patternType

    @patternType.setter
    def patternType(self, patternType: str):
        self.__patternType = patternType

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class Node:

    pass
class assessment_View(Node):

    pass
class assessment_Account(Node):

    def __init__(self, password: str, email: str, Account: "assessment_Entitlement" = None, accounts: "assessment_Accounts" = None, accounts47: set["assessment_Entitlement"] = None, Account77: "assessment_Accounts" = None):
        self.password = password
        self.email = email
        self.Account = Account
        self.accounts = accounts
        self.accounts47 = accounts47 if accounts47 is not None else set()
        self.Account77 = Account77
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Account__accounts", None)
        self.__accounts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Accounts"):
                opp_val = getattr(old_value, "Accounts", None)
                if opp_val == self:
                    setattr(old_value, "Accounts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Accounts"):
                opp_val = getattr(value, "Accounts", None)
                setattr(value, "Accounts", self)

    @property
    def accounts47(self):
        return self.__accounts47

    @accounts47.setter
    def accounts47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Account__accounts47", None)
        self.__accounts47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entitlement"):
                    opp_val = getattr(item, "Entitlement", None)
                    
                    if opp_val == self:
                        setattr(item, "Entitlement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entitlement"):
                    opp_val = getattr(item, "Entitlement", None)
                    
                    setattr(item, "Entitlement", self)
                    

    @property
    def Account77(self):
        return self.__Account77

    @Account77.setter
    def Account77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Account__Account77", None)
        self.__Account77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts76"):
                opp_val = getattr(old_value, "accounts76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts76"):
                opp_val = getattr(value, "accounts76", None)
                if opp_val is None:
                    setattr(value, "accounts76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Account(self):
        return self.__Account

    @Account.setter
    def Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Account__Account", None)
        self.__Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitlements"):
                opp_val = getattr(old_value, "entitlements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitlements"):
                opp_val = getattr(value, "entitlements", None)
                if opp_val is None:
                    setattr(value, "entitlements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class assessment_Entitlement(Node):

    pass
class assessment_Controller(Node):

    pass
class assessment_Sink(Node):

    def __init__(self, cwes: int, sinks: "assessment_Sinks" = None, Sink: "assessment_Sinks" = None):
        self.cwes = cwes
        self.sinks = sinks
        self.Sink = Sink
        
    @property
    def cwes(self) -> int:
        return self.__cwes

    @cwes.setter
    def cwes(self, cwes: int):
        self.__cwes = cwes

    @property
    def sinks(self):
        return self.__sinks

    @sinks.setter
    def sinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Sink__sinks", None)
        self.__sinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sinks"):
                opp_val = getattr(old_value, "Sinks", None)
                if opp_val == self:
                    setattr(old_value, "Sinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sinks"):
                opp_val = getattr(value, "Sinks", None)
                setattr(value, "Sinks", self)

    @property
    def Sink(self):
        return self.__Sink

    @Sink.setter
    def Sink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Sink__Sink", None)
        self.__Sink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sinks103"):
                opp_val = getattr(old_value, "sinks103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sinks103"):
                opp_val = getattr(value, "sinks103", None)
                if opp_val is None:
                    setattr(value, "sinks103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class assessment_Model(Node):

    pass
class assessment_Scm:

    def __init__(self, repository: str, branchTag: str, Scm: "assessment_Application" = None, scm: "assessment_Application" = None):
        self.repository = repository
        self.branchTag = branchTag
        self.Scm = Scm
        self.scm = scm
        
    @property
    def branchTag(self) -> str:
        return self.__branchTag

    @branchTag.setter
    def branchTag(self, branchTag: str):
        self.__branchTag = branchTag

    @property
    def repository(self) -> str:
        return self.__repository

    @repository.setter
    def repository(self, repository: str):
        self.__repository = repository

    @property
    def Scm(self):
        return self.__Scm

    @Scm.setter
    def Scm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Scm__Scm", None)
        self.__Scm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application24"):
                opp_val = getattr(old_value, "application24", None)
                if opp_val == self:
                    setattr(old_value, "application24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application24"):
                opp_val = getattr(value, "application24", None)
                setattr(value, "application24", self)

    @property
    def scm(self):
        return self.__scm

    @scm.setter
    def scm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Scm__scm", None)
        self.__scm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application"):
                opp_val = getattr(old_value, "Application", None)
                if opp_val == self:
                    setattr(old_value, "Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application"):
                opp_val = getattr(value, "Application", None)
                setattr(value, "Application", self)

class assessment_Models:

    pass
class assessment_Controllers:

    pass
class assessment_Entitlements:

    pass
class assessment_Accounts:

    pass
class assessment_Resources:

    pass
class assessment_Sinks:

    pass
class assessment_Views:

    pass
class assessment_Tasks:

    pass
class assessment_Findings:

    pass
class assessment_Applications:

    pass
class GraphNode:

    pass
class assessment_Snippet(Contents, GraphNode):

    def __init__(self, lineEnd: int, columnStart: int, columnEnd: int, lineStart: int, snippets: "assessment_Resource" = None, Snippet: "assessment_Resource" = None):
        self.lineEnd = lineEnd
        self.columnStart = columnStart
        self.columnEnd = columnEnd
        self.lineStart = lineStart
        self.snippets = snippets
        self.Snippet = Snippet
        
    @property
    def columnEnd(self) -> int:
        return self.__columnEnd

    @columnEnd.setter
    def columnEnd(self, columnEnd: int):
        self.__columnEnd = columnEnd

    @property
    def lineStart(self) -> int:
        return self.__lineStart

    @lineStart.setter
    def lineStart(self, lineStart: int):
        self.__lineStart = lineStart

    @property
    def columnStart(self) -> int:
        return self.__columnStart

    @columnStart.setter
    def columnStart(self, columnStart: int):
        self.__columnStart = columnStart

    @property
    def lineEnd(self) -> int:
        return self.__lineEnd

    @lineEnd.setter
    def lineEnd(self, lineEnd: int):
        self.__lineEnd = lineEnd

    @property
    def Snippet(self):
        return self.__Snippet

    @Snippet.setter
    def Snippet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Snippet__Snippet", None)
        self.__Snippet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resource"):
                opp_val = getattr(old_value, "resource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resource"):
                opp_val = getattr(value, "resource", None)
                if opp_val is None:
                    setattr(value, "resource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def snippets(self):
        return self.__snippets

    @snippets.setter
    def snippets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Snippet__snippets", None)
        self.__snippets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Resource"):
                opp_val = getattr(old_value, "Resource", None)
                if opp_val == self:
                    setattr(old_value, "Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Resource"):
                opp_val = getattr(value, "Resource", None)
                setattr(value, "Resource", self)

class assessment_Generic(GraphNode):

    pass
class assessment_Control(GraphNode):

    pass
class assessment_Http(GraphNode):

    def __init__(self, response: str, request: str):
        self.response = response
        self.request = request
        
    @property
    def response(self) -> str:
        return self.__response

    @response.setter
    def response(self, response: str):
        self.__response = response

    @property
    def request(self) -> str:
        return self.__request

    @request.setter
    def request(self, request: str):
        self.__request = request

class assessment_GraphNode(Node):

    pass
class Notes:

    pass
class Label:

    pass
class assessment_Task(Notes, Label):

    def __init__(self, status: str, Task: "assessment_Node" = None, tasks: "assessment_Tasks" = None, tasks54: set["assessment_Node"] = None, Task115: "assessment_Tasks" = None):
        self.status = status
        self.Task = Task
        self.tasks = tasks
        self.tasks54 = tasks54 if tasks54 is not None else set()
        self.Task115 = Task115
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def Task115(self):
        return self.__Task115

    @Task115.setter
    def Task115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Task__Task115", None)
        self.__Task115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks114"):
                opp_val = getattr(old_value, "tasks114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks114"):
                opp_val = getattr(value, "tasks114", None)
                if opp_val is None:
                    setattr(value, "tasks114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Task__tasks", None)
        self.__tasks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tasks52"):
                opp_val = getattr(old_value, "Tasks52", None)
                if opp_val == self:
                    setattr(old_value, "Tasks52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tasks52"):
                opp_val = getattr(value, "Tasks52", None)
                setattr(value, "Tasks52", self)

    @property
    def Task(self):
        return self.__Task

    @Task.setter
    def Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Task__Task", None)
        self.__Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "affects"):
                opp_val = getattr(old_value, "affects", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "affects"):
                opp_val = getattr(value, "affects", None)
                if opp_val is None:
                    setattr(value, "affects", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tasks54(self):
        return self.__tasks54

    @tasks54.setter
    def tasks54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Task__tasks54", None)
        self.__tasks54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node55"):
                    opp_val = getattr(item, "Node55", None)
                    
                    if opp_val == self:
                        setattr(item, "Node55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node55"):
                    opp_val = getattr(item, "Node55", None)
                    
                    setattr(item, "Node55", self)
                    

class assessment_Application(Notes, Label):

    def __init__(self, internalURL: str, externalURL: str, application26: "assessment_Views" = None, assessment_Application28: "assessment_Sinks" = None, application30: "assessment_Resources" = None, applications: "assessment_Applications" = None, assessment_Application: "assessment_Accounts" = None, assessment_Application19: "assessment_Entitlements" = None, application: "assessment_Controllers" = None, application22: "assessment_Models" = None, application24: "assessment_Scm" = None, Application: "assessment_Scm" = None, Application63: "assessment_Applications" = None, assessment_Application85: "assessment_Entitlements" = None, Application91: "assessment_Models" = None, assessment_Application74: "assessment_Accounts" = None, Application80: "assessment_Controllers" = None, Application106: "assessment_Resources" = None, Application96: "assessment_Views" = None, assessment_Application101: "assessment_Sinks" = None):
        self.internalURL = internalURL
        self.externalURL = externalURL
        self.application26 = application26
        self.assessment_Application28 = assessment_Application28
        self.application30 = application30
        self.applications = applications
        self.assessment_Application = assessment_Application
        self.assessment_Application19 = assessment_Application19
        self.application = application
        self.application22 = application22
        self.application24 = application24
        self.Application = Application
        self.Application63 = Application63
        self.assessment_Application85 = assessment_Application85
        self.Application91 = Application91
        self.assessment_Application74 = assessment_Application74
        self.Application80 = Application80
        self.Application106 = Application106
        self.Application96 = Application96
        self.assessment_Application101 = assessment_Application101
        
    @property
    def internalURL(self) -> str:
        return self.__internalURL

    @internalURL.setter
    def internalURL(self, internalURL: str):
        self.__internalURL = internalURL

    @property
    def externalURL(self) -> str:
        return self.__externalURL

    @externalURL.setter
    def externalURL(self, externalURL: str):
        self.__externalURL = externalURL

    @property
    def application26(self):
        return self.__application26

    @application26.setter
    def application26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__application26", None)
        self.__application26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Views"):
                opp_val = getattr(old_value, "Views", None)
                if opp_val == self:
                    setattr(old_value, "Views", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Views"):
                opp_val = getattr(value, "Views", None)
                setattr(value, "Views", self)

    @property
    def assessment_Application74(self):
        return self.__assessment_Application74

    @assessment_Application74.setter
    def assessment_Application74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application74", None)
        self.__assessment_Application74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Accounts73"):
                opp_val = getattr(old_value, "assessment_Accounts73", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Accounts73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Accounts73"):
                opp_val = getattr(value, "assessment_Accounts73", None)
                setattr(value, "assessment_Accounts73", self)

    @property
    def assessment_Application(self):
        return self.__assessment_Application

    @assessment_Application.setter
    def assessment_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application", None)
        self.__assessment_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Accounts"):
                opp_val = getattr(old_value, "assessment_Accounts", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Accounts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Accounts"):
                opp_val = getattr(value, "assessment_Accounts", None)
                setattr(value, "assessment_Accounts", self)

    @property
    def Application91(self):
        return self.__Application91

    @Application91.setter
    def Application91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application91", None)
        self.__Application91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "models90"):
                opp_val = getattr(old_value, "models90", None)
                if opp_val == self:
                    setattr(old_value, "models90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "models90"):
                opp_val = getattr(value, "models90", None)
                setattr(value, "models90", self)

    @property
    def application24(self):
        return self.__application24

    @application24.setter
    def application24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__application24", None)
        self.__application24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scm"):
                opp_val = getattr(old_value, "Scm", None)
                if opp_val == self:
                    setattr(old_value, "Scm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scm"):
                opp_val = getattr(value, "Scm", None)
                setattr(value, "Scm", self)

    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__application", None)
        self.__application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controllers"):
                opp_val = getattr(old_value, "Controllers", None)
                if opp_val == self:
                    setattr(old_value, "Controllers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controllers"):
                opp_val = getattr(value, "Controllers", None)
                setattr(value, "Controllers", self)

    @property
    def Application106(self):
        return self.__Application106

    @Application106.setter
    def Application106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application106", None)
        self.__Application106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources105"):
                opp_val = getattr(old_value, "resources105", None)
                if opp_val == self:
                    setattr(old_value, "resources105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources105"):
                opp_val = getattr(value, "resources105", None)
                setattr(value, "resources105", self)

    @property
    def assessment_Application101(self):
        return self.__assessment_Application101

    @assessment_Application101.setter
    def assessment_Application101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application101", None)
        self.__assessment_Application101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Sinks100"):
                opp_val = getattr(old_value, "assessment_Sinks100", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Sinks100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Sinks100"):
                opp_val = getattr(value, "assessment_Sinks100", None)
                setattr(value, "assessment_Sinks100", self)

    @property
    def Application96(self):
        return self.__Application96

    @Application96.setter
    def Application96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application96", None)
        self.__Application96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "views95"):
                opp_val = getattr(old_value, "views95", None)
                if opp_val == self:
                    setattr(old_value, "views95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "views95"):
                opp_val = getattr(value, "views95", None)
                setattr(value, "views95", self)

    @property
    def assessment_Application28(self):
        return self.__assessment_Application28

    @assessment_Application28.setter
    def assessment_Application28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application28", None)
        self.__assessment_Application28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Sinks"):
                opp_val = getattr(old_value, "assessment_Sinks", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Sinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Sinks"):
                opp_val = getattr(value, "assessment_Sinks", None)
                setattr(value, "assessment_Sinks", self)

    @property
    def application30(self):
        return self.__application30

    @application30.setter
    def application30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__application30", None)
        self.__application30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Resources"):
                opp_val = getattr(old_value, "Resources", None)
                if opp_val == self:
                    setattr(old_value, "Resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Resources"):
                opp_val = getattr(value, "Resources", None)
                setattr(value, "Resources", self)

    @property
    def assessment_Application85(self):
        return self.__assessment_Application85

    @assessment_Application85.setter
    def assessment_Application85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application85", None)
        self.__assessment_Application85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Entitlements84"):
                opp_val = getattr(old_value, "assessment_Entitlements84", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Entitlements84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Entitlements84"):
                opp_val = getattr(value, "assessment_Entitlements84", None)
                setattr(value, "assessment_Entitlements84", self)

    @property
    def Application63(self):
        return self.__Application63

    @Application63.setter
    def Application63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application63", None)
        self.__Application63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applications62"):
                opp_val = getattr(old_value, "applications62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applications62"):
                opp_val = getattr(value, "applications62", None)
                if opp_val is None:
                    setattr(value, "applications62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Application80(self):
        return self.__Application80

    @Application80.setter
    def Application80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application80", None)
        self.__Application80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controllers79"):
                opp_val = getattr(old_value, "controllers79", None)
                if opp_val == self:
                    setattr(old_value, "controllers79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controllers79"):
                opp_val = getattr(value, "controllers79", None)
                setattr(value, "controllers79", self)

    @property
    def applications(self):
        return self.__applications

    @applications.setter
    def applications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__applications", None)
        self.__applications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Applications32"):
                opp_val = getattr(old_value, "Applications32", None)
                if opp_val == self:
                    setattr(old_value, "Applications32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Applications32"):
                opp_val = getattr(value, "Applications32", None)
                setattr(value, "Applications32", self)

    @property
    def application22(self):
        return self.__application22

    @application22.setter
    def application22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__application22", None)
        self.__application22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Models"):
                opp_val = getattr(old_value, "Models", None)
                if opp_val == self:
                    setattr(old_value, "Models", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Models"):
                opp_val = getattr(value, "Models", None)
                setattr(value, "Models", self)

    @property
    def Application(self):
        return self.__Application

    @Application.setter
    def Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__Application", None)
        self.__Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scm"):
                opp_val = getattr(old_value, "scm", None)
                if opp_val == self:
                    setattr(old_value, "scm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scm"):
                opp_val = getattr(value, "scm", None)
                setattr(value, "scm", self)

    @property
    def assessment_Application19(self):
        return self.__assessment_Application19

    @assessment_Application19.setter
    def assessment_Application19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Application__assessment_Application19", None)
        self.__assessment_Application19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment_Entitlements"):
                opp_val = getattr(old_value, "assessment_Entitlements", None)
                if opp_val == self:
                    setattr(old_value, "assessment_Entitlements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment_Entitlements"):
                opp_val = getattr(value, "assessment_Entitlements", None)
                setattr(value, "assessment_Entitlements", self)

class assessment_Assessment(Notes, Label):

    pass
class assessment_Resource(Contents, Notes, Label):

    pass
class assessment_Finding(Notes, Label):

    def __init__(self, reproducer: str, remediation: str, references: str, Finding: "assessment_Node" = None, findings: "assessment_Findings" = None, findings43: set["assessment_Node"] = None, Finding68: "assessment_Findings" = None):
        self.reproducer = reproducer
        self.remediation = remediation
        self.references = references
        self.Finding = Finding
        self.findings = findings
        self.findings43 = findings43 if findings43 is not None else set()
        self.Finding68 = Finding68
        
    @property
    def references(self) -> str:
        return self.__references

    @references.setter
    def references(self, references: str):
        self.__references = references

    @property
    def remediation(self) -> str:
        return self.__remediation

    @remediation.setter
    def remediation(self, remediation: str):
        self.__remediation = remediation

    @property
    def reproducer(self) -> str:
        return self.__reproducer

    @reproducer.setter
    def reproducer(self, reproducer: str):
        self.__reproducer = reproducer

    @property
    def Finding68(self):
        return self.__Finding68

    @Finding68.setter
    def Finding68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Finding__Finding68", None)
        self.__Finding68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "findings67"):
                opp_val = getattr(old_value, "findings67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "findings67"):
                opp_val = getattr(value, "findings67", None)
                if opp_val is None:
                    setattr(value, "findings67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def findings(self):
        return self.__findings

    @findings.setter
    def findings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Finding__findings", None)
        self.__findings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Findings41"):
                opp_val = getattr(old_value, "Findings41", None)
                if opp_val == self:
                    setattr(old_value, "Findings41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Findings41"):
                opp_val = getattr(value, "Findings41", None)
                setattr(value, "Findings41", self)

    @property
    def Finding(self):
        return self.__Finding

    @Finding.setter
    def Finding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Finding__Finding", None)
        self.__Finding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "affects11"):
                opp_val = getattr(old_value, "affects11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "affects11"):
                opp_val = getattr(value, "affects11", None)
                if opp_val is None:
                    setattr(value, "affects11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def findings43(self):
        return self.__findings43

    @findings43.setter
    def findings43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assessment_Finding__findings43", None)
        self.__findings43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node44"):
                    opp_val = getattr(item, "Node44", None)
                    
                    if opp_val == self:
                        setattr(item, "Node44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node44"):
                    opp_val = getattr(item, "Node44", None)
                    
                    setattr(item, "Node44", self)
                    

class assessment_Node(Notes, Label):

    pass