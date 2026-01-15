from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InvoiceState(Enum):
    New = "New"
    Invoiced = "Invoiced"
    Paid = "Paid"


############################################
# Definition of Classes
############################################

class accounting_Invoice:

    def __init__(self, id: str, unitAmount: float, invoiceDate: date, dueDate: date, state: str, accounting_Invoice: "accounting_Employee" = None, invoices: "accounting_Order" = None, Invoice: "accounting_Order" = None):
        self.id = id
        self.unitAmount = unitAmount
        self.invoiceDate = invoiceDate
        self.dueDate = dueDate
        self.state = state
        self.accounting_Invoice = accounting_Invoice
        self.invoices = invoices
        self.Invoice = Invoice
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def dueDate(self) -> date:
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate

    @property
    def unitAmount(self) -> float:
        return self.__unitAmount

    @unitAmount.setter
    def unitAmount(self, unitAmount: float):
        self.__unitAmount = unitAmount

    @property
    def invoiceDate(self) -> date:
        return self.__invoiceDate

    @invoiceDate.setter
    def invoiceDate(self, invoiceDate: date):
        self.__invoiceDate = invoiceDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def accounting_Invoice(self):
        return self.__accounting_Invoice

    @accounting_Invoice.setter
    def accounting_Invoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Invoice__accounting_Invoice", None)
        self.__accounting_Invoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Employee"):
                opp_val = getattr(old_value, "accounting_Employee", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Employee"):
                opp_val = getattr(value, "accounting_Employee", None)
                setattr(value, "accounting_Employee", self)

    @property
    def Invoice(self):
        return self.__Invoice

    @Invoice.setter
    def Invoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Invoice__Invoice", None)
        self.__Invoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order7"):
                opp_val = getattr(old_value, "order7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order7"):
                opp_val = getattr(value, "order7", None)
                if opp_val is None:
                    setattr(value, "order7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invoices(self):
        return self.__invoices

    @invoices.setter
    def invoices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Invoice__invoices", None)
        self.__invoices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order12"):
                opp_val = getattr(old_value, "Order12", None)
                if opp_val == self:
                    setattr(old_value, "Order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order12"):
                opp_val = getattr(value, "Order12", None)
                setattr(value, "Order12", self)

class accounting_Deliverable:

    def __init__(self, dueDate: date, unitAmount: float, deliverables: "accounting_Order" = None, Deliverable: "accounting_Order" = None):
        self.dueDate = dueDate
        self.unitAmount = unitAmount
        self.deliverables = deliverables
        self.Deliverable = Deliverable
        
    @property
    def unitAmount(self) -> float:
        return self.__unitAmount

    @unitAmount.setter
    def unitAmount(self, unitAmount: float):
        self.__unitAmount = unitAmount

    @property
    def dueDate(self) -> date:
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate

    @property
    def deliverables(self):
        return self.__deliverables

    @deliverables.setter
    def deliverables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Deliverable__deliverables", None)
        self.__deliverables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order9"):
                opp_val = getattr(old_value, "Order9", None)
                if opp_val == self:
                    setattr(old_value, "Order9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order9"):
                opp_val = getattr(value, "Order9", None)
                setattr(value, "Order9", self)

    @property
    def Deliverable(self):
        return self.__Deliverable

    @Deliverable.setter
    def Deliverable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Deliverable__Deliverable", None)
        self.__Deliverable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order"):
                opp_val = getattr(old_value, "order", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order"):
                opp_val = getattr(value, "order", None)
                if opp_val is None:
                    setattr(value, "order", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class accounting_Employees:

    pass
class accounting_Clients:

    pass
class accounting_WorkPackage:

    def __init__(self, date: date, hours: float, task: str, comment: str, accounting_WorkPackage: "accounting_Employee" = None, accounting_WorkPackage16: "accounting_Project" = None):
        self.date = date
        self.hours = hours
        self.task = task
        self.comment = comment
        self.accounting_WorkPackage = accounting_WorkPackage
        self.accounting_WorkPackage16 = accounting_WorkPackage16
        
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
    def hours(self) -> float:
        return self.__hours

    @hours.setter
    def hours(self, hours: float):
        self.__hours = hours

    @property
    def task(self) -> str:
        return self.__task

    @task.setter
    def task(self, task: str):
        self.__task = task

    @property
    def accounting_WorkPackage16(self):
        return self.__accounting_WorkPackage16

    @accounting_WorkPackage16.setter
    def accounting_WorkPackage16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_WorkPackage__accounting_WorkPackage16", None)
        self.__accounting_WorkPackage16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Project"):
                opp_val = getattr(old_value, "accounting_Project", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Project"):
                opp_val = getattr(value, "accounting_Project", None)
                setattr(value, "accounting_Project", self)

    @property
    def accounting_WorkPackage(self):
        return self.__accounting_WorkPackage

    @accounting_WorkPackage.setter
    def accounting_WorkPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_WorkPackage__accounting_WorkPackage", None)
        self.__accounting_WorkPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Employee14"):
                opp_val = getattr(old_value, "accounting_Employee14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Employee14"):
                opp_val = getattr(value, "accounting_Employee14", None)
                if opp_val is None:
                    setattr(value, "accounting_Employee14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class accounting_Order:

    def __init__(self, id: str, paymentOffset: int, pricePerUnit: float, Order: "accounting_Project" = None, Order9: "accounting_Deliverable" = None, Order12: "accounting_Invoice" = None, orders: "accounting_Project" = None, order: set["accounting_Deliverable"] = None, order7: set["accounting_Invoice"] = None):
        self.id = id
        self.paymentOffset = paymentOffset
        self.pricePerUnit = pricePerUnit
        self.Order = Order
        self.Order9 = Order9
        self.Order12 = Order12
        self.orders = orders
        self.order = order if order is not None else set()
        self.order7 = order7 if order7 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def paymentOffset(self) -> int:
        return self.__paymentOffset

    @paymentOffset.setter
    def paymentOffset(self, paymentOffset: int):
        self.__paymentOffset = paymentOffset

    @property
    def pricePerUnit(self) -> float:
        return self.__pricePerUnit

    @pricePerUnit.setter
    def pricePerUnit(self, pricePerUnit: float):
        self.__pricePerUnit = pricePerUnit

    @property
    def Order9(self):
        return self.__Order9

    @Order9.setter
    def Order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__Order9", None)
        self.__Order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deliverables"):
                opp_val = getattr(old_value, "deliverables", None)
                if opp_val == self:
                    setattr(old_value, "deliverables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deliverables"):
                opp_val = getattr(value, "deliverables", None)
                setattr(value, "deliverables", self)

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__orders", None)
        self.__orders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project4"):
                opp_val = getattr(old_value, "Project4", None)
                if opp_val == self:
                    setattr(old_value, "Project4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project4"):
                opp_val = getattr(value, "Project4", None)
                setattr(value, "Project4", self)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__order", None)
        self.__order = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Deliverable"):
                    opp_val = getattr(item, "Deliverable", None)
                    
                    if opp_val == self:
                        setattr(item, "Deliverable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Deliverable"):
                    opp_val = getattr(item, "Deliverable", None)
                    
                    setattr(item, "Deliverable", self)
                    

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__Order", None)
        self.__Order = value
        
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

    @property
    def Order12(self):
        return self.__Order12

    @Order12.setter
    def Order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__Order12", None)
        self.__Order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoices"):
                opp_val = getattr(old_value, "invoices", None)
                if opp_val == self:
                    setattr(old_value, "invoices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoices"):
                opp_val = getattr(value, "invoices", None)
                setattr(value, "invoices", self)

    @property
    def order7(self):
        return self.__order7

    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Order__order7", None)
        self.__order7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invoice"):
                    opp_val = getattr(item, "Invoice", None)
                    
                    if opp_val == self:
                        setattr(item, "Invoice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invoice"):
                    opp_val = getattr(item, "Invoice", None)
                    
                    setattr(item, "Invoice", self)
                    

    def validateUnitAmount(self, diagnosticChain: str, context: str) -> bool:
        # TODO: Implement validateUnitAmount method
        pass

class NamedElement:

    pass
class accounting_Employee(NamedElement):

    def __init__(self, emails: str, accounting_Employee: "accounting_Invoice" = None, accounting_Employee14: set["accounting_WorkPackage"] = None, accounting_Employee19: "accounting_Employees" = None):
        self.emails = emails
        self.accounting_Employee = accounting_Employee
        self.accounting_Employee14 = accounting_Employee14 if accounting_Employee14 is not None else set()
        self.accounting_Employee19 = accounting_Employee19
        
    @property
    def emails(self) -> str:
        return self.__emails

    @emails.setter
    def emails(self, emails: str):
        self.__emails = emails

    @property
    def accounting_Employee19(self):
        return self.__accounting_Employee19

    @accounting_Employee19.setter
    def accounting_Employee19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Employee__accounting_Employee19", None)
        self.__accounting_Employee19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Employees"):
                opp_val = getattr(old_value, "accounting_Employees", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Employees"):
                opp_val = getattr(value, "accounting_Employees", None)
                if opp_val is None:
                    setattr(value, "accounting_Employees", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_Employee14(self):
        return self.__accounting_Employee14

    @accounting_Employee14.setter
    def accounting_Employee14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Employee__accounting_Employee14", None)
        self.__accounting_Employee14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_WorkPackage"):
                    opp_val = getattr(item, "accounting_WorkPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_WorkPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_WorkPackage"):
                    opp_val = getattr(item, "accounting_WorkPackage", None)
                    
                    setattr(item, "accounting_WorkPackage", self)
                    

    @property
    def accounting_Employee(self):
        return self.__accounting_Employee

    @accounting_Employee.setter
    def accounting_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Employee__accounting_Employee", None)
        self.__accounting_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Invoice"):
                opp_val = getattr(old_value, "accounting_Invoice", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Invoice"):
                opp_val = getattr(value, "accounting_Invoice", None)
                setattr(value, "accounting_Invoice", self)

class accounting_Project(NamedElement):

    pass
class accounting_Client(NamedElement):

    pass
class accounting_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
