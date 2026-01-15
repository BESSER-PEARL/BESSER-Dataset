from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class remember_Years:

    pass
class remember_Year:

    def __init__(self, year: int, year: set["remember_InvoiceSpecification"] = None, year33: "remember_Years" = None, Year: "remember_InvoiceSpecification" = None, Year38: "remember_Years" = None):
        self.year = year
        self.year = year if year is not None else set()
        self.year33 = year33
        self.Year = Year
        self.Year38 = Year38
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Year__Year", None)
        self.__Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoiceSpecifications"):
                opp_val = getattr(old_value, "invoiceSpecifications", None)
                if opp_val == self:
                    setattr(old_value, "invoiceSpecifications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoiceSpecifications"):
                opp_val = getattr(value, "invoiceSpecifications", None)
                setattr(value, "invoiceSpecifications", self)

    @property
    def Year38(self):
        return self.__Year38

    @Year38.setter
    def Year38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Year__Year38", None)
        self.__Year38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "years"):
                opp_val = getattr(old_value, "years", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "years"):
                opp_val = getattr(value, "years", None)
                if opp_val is None:
                    setattr(value, "years", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def year33(self):
        return self.__year33

    @year33.setter
    def year33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Year__year33", None)
        self.__year33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Years"):
                opp_val = getattr(old_value, "Years", None)
                if opp_val == self:
                    setattr(old_value, "Years", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Years"):
                opp_val = getattr(value, "Years", None)
                setattr(value, "Years", self)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Year__year", None)
        self.__year = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvoiceSpecification31"):
                    opp_val = getattr(item, "InvoiceSpecification31", None)
                    
                    if opp_val == self:
                        setattr(item, "InvoiceSpecification31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvoiceSpecification31"):
                    opp_val = getattr(item, "InvoiceSpecification31", None)
                    
                    setattr(item, "InvoiceSpecification31", self)
                    

class remember_InvoiceSpecification:

    def __init__(self, month: int, InvoiceSpecification: "remember_TimeSpent" = None, InvoiceSpecification31: "remember_Year" = None, invoiceSpecification: set["remember_TimeSpent"] = None, invoiceSpecifications: "remember_Year" = None):
        self.month = month
        self.InvoiceSpecification = InvoiceSpecification
        self.InvoiceSpecification31 = InvoiceSpecification31
        self.invoiceSpecification = invoiceSpecification if invoiceSpecification is not None else set()
        self.invoiceSpecifications = invoiceSpecifications
        
    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month

    @property
    def InvoiceSpecification31(self):
        return self.__InvoiceSpecification31

    @InvoiceSpecification31.setter
    def InvoiceSpecification31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_InvoiceSpecification__InvoiceSpecification31", None)
        self.__InvoiceSpecification31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "year"):
                opp_val = getattr(old_value, "year", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "year"):
                opp_val = getattr(value, "year", None)
                if opp_val is None:
                    setattr(value, "year", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invoiceSpecification(self):
        return self.__invoiceSpecification

    @invoiceSpecification.setter
    def invoiceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_InvoiceSpecification__invoiceSpecification", None)
        self.__invoiceSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TimeSpent35"):
                    opp_val = getattr(item, "TimeSpent35", None)
                    
                    if opp_val == self:
                        setattr(item, "TimeSpent35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TimeSpent35"):
                    opp_val = getattr(item, "TimeSpent35", None)
                    
                    setattr(item, "TimeSpent35", self)
                    

    @property
    def invoiceSpecifications(self):
        return self.__invoiceSpecifications

    @invoiceSpecifications.setter
    def invoiceSpecifications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_InvoiceSpecification__invoiceSpecifications", None)
        self.__invoiceSpecifications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Year"):
                opp_val = getattr(old_value, "Year", None)
                if opp_val == self:
                    setattr(old_value, "Year", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Year"):
                opp_val = getattr(value, "Year", None)
                setattr(value, "Year", self)

    @property
    def InvoiceSpecification(self):
        return self.__InvoiceSpecification

    @InvoiceSpecification.setter
    def InvoiceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_InvoiceSpecification__InvoiceSpecification", None)
        self.__InvoiceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeSpent29"):
                opp_val = getattr(old_value, "timeSpent29", None)
                if opp_val == self:
                    setattr(old_value, "timeSpent29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeSpent29"):
                opp_val = getattr(value, "timeSpent29", None)
                setattr(value, "timeSpent29", self)

class remember_KeyIdPair:

    def __init__(self, key: str, id: str, remember_KeyIdPair: "remember_KeyManager" = None):
        self.key = key
        self.id = id
        self.remember_KeyIdPair = remember_KeyIdPair
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def remember_KeyIdPair(self):
        return self.__remember_KeyIdPair

    @remember_KeyIdPair.setter
    def remember_KeyIdPair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_KeyIdPair__remember_KeyIdPair", None)
        self.__remember_KeyIdPair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remember_KeyManager"):
                opp_val = getattr(old_value, "remember_KeyManager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remember_KeyManager"):
                opp_val = getattr(value, "remember_KeyManager", None)
                if opp_val is None:
                    setattr(value, "remember_KeyManager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remember_KeyManager:

    pass
class remember_Node(ABC):

    def __init__(self, nodeId: str, nodeType: str, parentNodeId: str, parentNodeType: str, sequence: int, name: str, description: str, dateCreated: date, dateModified: date, markedForDeletion: bool, nodes: "remember_Customer" = None, nodes13: "remember_Project" = None, Node: "remember_Customer" = None, Node22: "remember_Project" = None):
        self.nodeId = nodeId
        self.nodeType = nodeType
        self.parentNodeId = parentNodeId
        self.parentNodeType = parentNodeType
        self.sequence = sequence
        self.name = name
        self.description = description
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.markedForDeletion = markedForDeletion
        self.nodes = nodes
        self.nodes13 = nodes13
        self.Node = Node
        self.Node22 = Node22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def dateCreated(self) -> date:
        return self.__dateCreated

    @dateCreated.setter
    def dateCreated(self, dateCreated: date):
        self.__dateCreated = dateCreated

    @property
    def nodeType(self) -> str:
        return self.__nodeType

    @nodeType.setter
    def nodeType(self, nodeType: str):
        self.__nodeType = nodeType

    @property
    def parentNodeId(self) -> str:
        return self.__parentNodeId

    @parentNodeId.setter
    def parentNodeId(self, parentNodeId: str):
        self.__parentNodeId = parentNodeId

    @property
    def parentNodeType(self) -> str:
        return self.__parentNodeType

    @parentNodeType.setter
    def parentNodeType(self, parentNodeType: str):
        self.__parentNodeType = parentNodeType

    @property
    def nodeId(self) -> str:
        return self.__nodeId

    @nodeId.setter
    def nodeId(self, nodeId: str):
        self.__nodeId = nodeId

    @property
    def dateModified(self) -> date:
        return self.__dateModified

    @dateModified.setter
    def dateModified(self, dateModified: date):
        self.__dateModified = dateModified

    @property
    def sequence(self) -> int:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence

    @property
    def markedForDeletion(self) -> bool:
        return self.__markedForDeletion

    @markedForDeletion.setter
    def markedForDeletion(self, markedForDeletion: bool):
        self.__markedForDeletion = markedForDeletion

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer18"):
                opp_val = getattr(old_value, "customer18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer18"):
                opp_val = getattr(value, "customer18", None)
                if opp_val is None:
                    setattr(value, "customer18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nodes13(self):
        return self.__nodes13

    @nodes13.setter
    def nodes13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Node__nodes13", None)
        self.__nodes13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project"):
                opp_val = getattr(old_value, "Project", None)
                if opp_val == self:
                    setattr(old_value, "Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project"):
                opp_val = getattr(value, "Project", None)
                setattr(value, "Project", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def Node22(self):
        return self.__Node22

    @Node22.setter
    def Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Node__Node22", None)
        self.__Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project"):
                opp_val = getattr(old_value, "project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project"):
                opp_val = getattr(value, "project", None)
                if opp_val is None:
                    setattr(value, "project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remember_TimeSpent:

    def __init__(self, invoiced: bool, timeSpentId: str, date: date, minutes: int, comment: str, TimeSpent: "remember_Task" = None, remember_TimeSpent: "remember_Project" = None, timeSpent: "remember_Task" = None, timeSpent29: "remember_InvoiceSpecification" = None, TimeSpent35: "remember_InvoiceSpecification" = None):
        self.invoiced = invoiced
        self.timeSpentId = timeSpentId
        self.date = date
        self.minutes = minutes
        self.comment = comment
        self.TimeSpent = TimeSpent
        self.remember_TimeSpent = remember_TimeSpent
        self.timeSpent = timeSpent
        self.timeSpent29 = timeSpent29
        self.TimeSpent35 = TimeSpent35
        
    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def invoiced(self) -> bool:
        return self.__invoiced

    @invoiced.setter
    def invoiced(self, invoiced: bool):
        self.__invoiced = invoiced

    @property
    def timeSpentId(self) -> str:
        return self.__timeSpentId

    @timeSpentId.setter
    def timeSpentId(self, timeSpentId: str):
        self.__timeSpentId = timeSpentId

    @property
    def timeSpent29(self):
        return self.__timeSpent29

    @timeSpent29.setter
    def timeSpent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_TimeSpent__timeSpent29", None)
        self.__timeSpent29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InvoiceSpecification"):
                opp_val = getattr(old_value, "InvoiceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "InvoiceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InvoiceSpecification"):
                opp_val = getattr(value, "InvoiceSpecification", None)
                setattr(value, "InvoiceSpecification", self)

    @property
    def timeSpent(self):
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_TimeSpent__timeSpent", None)
        self.__timeSpent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Task27"):
                opp_val = getattr(old_value, "Task27", None)
                if opp_val == self:
                    setattr(old_value, "Task27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Task27"):
                opp_val = getattr(value, "Task27", None)
                setattr(value, "Task27", self)

    @property
    def remember_TimeSpent(self):
        return self.__remember_TimeSpent

    @remember_TimeSpent.setter
    def remember_TimeSpent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_TimeSpent__remember_TimeSpent", None)
        self.__remember_TimeSpent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remember_Project"):
                opp_val = getattr(old_value, "remember_Project", None)
                if opp_val == self:
                    setattr(old_value, "remember_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remember_Project"):
                opp_val = getattr(value, "remember_Project", None)
                setattr(value, "remember_Project", self)

    @property
    def TimeSpent35(self):
        return self.__TimeSpent35

    @TimeSpent35.setter
    def TimeSpent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_TimeSpent__TimeSpent35", None)
        self.__TimeSpent35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoiceSpecification"):
                opp_val = getattr(old_value, "invoiceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoiceSpecification"):
                opp_val = getattr(value, "invoiceSpecification", None)
                if opp_val is None:
                    setattr(value, "invoiceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TimeSpent(self):
        return self.__TimeSpent

    @TimeSpent.setter
    def TimeSpent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_TimeSpent__TimeSpent", None)
        self.__TimeSpent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task"):
                opp_val = getattr(old_value, "task", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task"):
                opp_val = getattr(value, "task", None)
                if opp_val is None:
                    setattr(value, "task", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remember_Project:

    def __init__(self, projectId: str, projectNumber: str, description: str, Project: "remember_Node" = None, projects: "remember_Customer" = None, project: set["remember_Node"] = None, Project16: "remember_Customer" = None, remember_Project: "remember_TimeSpent" = None):
        self.projectId = projectId
        self.projectNumber = projectNumber
        self.description = description
        self.Project = Project
        self.projects = projects
        self.project = project if project is not None else set()
        self.Project16 = Project16
        self.remember_Project = remember_Project
        
    @property
    def projectId(self) -> str:
        return self.__projectId

    @projectId.setter
    def projectId(self, projectId: str):
        self.__projectId = projectId

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def projectNumber(self) -> str:
        return self.__projectNumber

    @projectNumber.setter
    def projectNumber(self, projectNumber: str):
        self.__projectNumber = projectNumber

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Project__projects", None)
        self.__projects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer20"):
                opp_val = getattr(old_value, "Customer20", None)
                if opp_val == self:
                    setattr(old_value, "Customer20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer20"):
                opp_val = getattr(value, "Customer20", None)
                setattr(value, "Customer20", self)

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node22"):
                    opp_val = getattr(item, "Node22", None)
                    
                    if opp_val == self:
                        setattr(item, "Node22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node22"):
                    opp_val = getattr(item, "Node22", None)
                    
                    setattr(item, "Node22", self)
                    

    @property
    def remember_Project(self):
        return self.__remember_Project

    @remember_Project.setter
    def remember_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Project__remember_Project", None)
        self.__remember_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remember_TimeSpent"):
                opp_val = getattr(old_value, "remember_TimeSpent", None)
                if opp_val == self:
                    setattr(old_value, "remember_TimeSpent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remember_TimeSpent"):
                opp_val = getattr(value, "remember_TimeSpent", None)
                setattr(value, "remember_TimeSpent", self)

    @property
    def Project16(self):
        return self.__Project16

    @Project16.setter
    def Project16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Project__Project16", None)
        self.__Project16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes13"):
                opp_val = getattr(old_value, "nodes13", None)
                if opp_val == self:
                    setattr(old_value, "nodes13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes13"):
                opp_val = getattr(value, "nodes13", None)
                setattr(value, "nodes13", self)

class remember_Customer:

    def __init__(self, customerId: str, name: str, Customer: "remember_Node" = None, customer18: set["remember_Node"] = None, Customer20: "remember_Project" = None, remember_Customer: "remember_Customers" = None, customer: set["remember_Project"] = None):
        self.customerId = customerId
        self.name = name
        self.Customer = Customer
        self.customer18 = customer18 if customer18 is not None else set()
        self.Customer20 = Customer20
        self.remember_Customer = remember_Customer
        self.customer = customer if customer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerId(self) -> str:
        return self.__customerId

    @customerId.setter
    def customerId(self, customerId: str):
        self.__customerId = customerId

    @property
    def customer18(self):
        return self.__customer18

    @customer18.setter
    def customer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Customer__customer18", None)
        self.__customer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project16"):
                    opp_val = getattr(item, "Project16", None)
                    
                    if opp_val == self:
                        setattr(item, "Project16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project16"):
                    opp_val = getattr(item, "Project16", None)
                    
                    setattr(item, "Project16", self)
                    

    @property
    def remember_Customer(self):
        return self.__remember_Customer

    @remember_Customer.setter
    def remember_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Customer__remember_Customer", None)
        self.__remember_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remember_Customers24"):
                opp_val = getattr(old_value, "remember_Customers24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remember_Customers24"):
                opp_val = getattr(value, "remember_Customers24", None)
                if opp_val is None:
                    setattr(value, "remember_Customers24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def Customer20(self):
        return self.__Customer20

    @Customer20.setter
    def Customer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Customer__Customer20", None)
        self.__Customer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects"):
                opp_val = getattr(old_value, "projects", None)
                if opp_val == self:
                    setattr(old_value, "projects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects"):
                opp_val = getattr(value, "projects", None)
                setattr(value, "projects", self)

class Node:

    pass
class remember_Task(Node):

    def __init__(self, taskId: int, priority: str, status: str, budget: str, text: str, done: bool, Task: "remember_Folder" = None, Tasks: "remember_Folder" = None, task: set["remember_TimeSpent"] = None, Task27: "remember_TimeSpent" = None):
        self.taskId = taskId
        self.priority = priority
        self.status = status
        self.budget = budget
        self.text = text
        self.done = done
        self.Task = Task
        self.Tasks = Tasks
        self.task = task if task is not None else set()
        self.Task27 = Task27
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def taskId(self) -> int:
        return self.__taskId

    @taskId.setter
    def taskId(self, taskId: int):
        self.__taskId = taskId

    @property
    def done(self) -> bool:
        return self.__done

    @done.setter
    def done(self, done: bool):
        self.__done = done

    @property
    def budget(self) -> str:
        return self.__budget

    @budget.setter
    def budget(self, budget: str):
        self.__budget = budget

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Task__task", None)
        self.__task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TimeSpent"):
                    opp_val = getattr(item, "TimeSpent", None)
                    
                    if opp_val == self:
                        setattr(item, "TimeSpent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TimeSpent"):
                    opp_val = getattr(item, "TimeSpent", None)
                    
                    setattr(item, "TimeSpent", self)
                    

    @property
    def Task(self):
        return self.__Task

    @Task.setter
    def Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Task__Task", None)
        self.__Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tasks(self):
        return self.__Tasks

    @Tasks.setter
    def Tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Task__Tasks", None)
        self.__Tasks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Folder9"):
                opp_val = getattr(old_value, "Folder9", None)
                if opp_val == self:
                    setattr(old_value, "Folder9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Folder9"):
                opp_val = getattr(value, "Folder9", None)
                setattr(value, "Folder9", self)

    @property
    def Task27(self):
        return self.__Task27

    @Task27.setter
    def Task27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remember_Task__Task27", None)
        self.__Task27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeSpent"):
                opp_val = getattr(old_value, "timeSpent", None)
                if opp_val == self:
                    setattr(old_value, "timeSpent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeSpent"):
                opp_val = getattr(value, "timeSpent", None)
                setattr(value, "timeSpent", self)

class remember_Folder(Node):

    pass
class remember_Customers:

    pass