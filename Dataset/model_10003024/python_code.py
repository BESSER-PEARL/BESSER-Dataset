from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Currency(Enum):
    pass
class Package_ExpenseStatus(Enum):
    pass
class Package_PaymentMethod(Enum):
    pass

############################################
# Definition of Classes
############################################







class Authenticate_UseCase:

    pass


class Sales_Agent_Actor:

    pass


class Download_an_attached_file_UseCase:

    pass


class Consult_an_attched_file_UseCase:

    pass


class Delete_an_attached_file_UseCase:

    pass


class Upload_a_file_UseCase:

    pass


class Manage_attached_files_UseCase:

    pass


class Super_Administrator_Actor:

    pass


class Sales_agent_Actor:

    pass


class Administrator_Actor:

    pass


class Office_Manager_Actor:

    pass


class Manager_Actor:

    pass


class Collaborator_Actor:

    pass





class Delete_an_Expense_external:

    pass


class Send_an_Expenses_to_verification_external:

    pass


class Update_an_Expense_external:

    pass


class Create_an_Expense_external:

    pass


class Verify_collaborators__Expenses_external:

    pass


class Manage_Expenses__settings_external:

    pass


class Refund_Expenses_external:

    pass


class Review_collaborators__Expense_refunds_external:

    pass


class Consult_collaborators__Expenses_external:

    pass


class Manage_Expenses_external:

    pass


class Manage_Expense_currency_external:

    pass


class Manage_Expense_types_external:

    pass


class Refuse_collaborators__Expense_refunds_external:

    pass


class Validate_collaborators__Expense_refunds_external:

    pass


class Filter_Expenses_external:

    pass


class Search_Expenses_external:

    pass


class Consult_Expenses_external:

    pass


class Package_ExpenseType:

    def __init__(self, id: str, name: str, price: str, ExpenseType_Bill_042: "Package_Bill" = None):
        self.id = id
        self.name = name
        self.price = price
        self.ExpenseType_Bill_042 = ExpenseType_Bill_042
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def ExpenseType_Bill_042(self):
        return self.__ExpenseType_Bill_042
    @ExpenseType_Bill_042.setter
    def ExpenseType_Bill_042(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_ExpenseType__ExpenseType_Bill_042", None)
        self.__ExpenseType_Bill_042 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExpenseType_Bill_143"):
                opp_val = getattr(old_value, "ExpenseType_Bill_143", None)
                if opp_val == self:
                    setattr(old_value, "ExpenseType_Bill_143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExpenseType_Bill_143"):
                opp_val = getattr(value, "ExpenseType_Bill_143", None)
                setattr(value, "ExpenseType_Bill_143", self)



class Package_Currency:

    def __init__(self, id: str, name: str, abr: str, Currency_Expense_040: "Package_Bill" = None):
        self.id = id
        self.name = name
        self.abr = abr
        self.Currency_Expense_040 = Currency_Expense_040
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def abr(self):
        return self.__abr
    @abr.setter
    def abr(self, abr: str):
        self.__abr = abr

    @property
    def Currency_Expense_040(self):
        return self.__Currency_Expense_040
    @Currency_Expense_040.setter
    def Currency_Expense_040(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Currency__Currency_Expense_040", None)
        self.__Currency_Expense_040 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Currency_Expense_141"):
                opp_val = getattr(old_value, "Currency_Expense_141", None)
                if opp_val == self:
                    setattr(old_value, "Currency_Expense_141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Currency_Expense_141"):
                opp_val = getattr(value, "Currency_Expense_141", None)
                setattr(value, "Currency_Expense_141", self)



class Package_Comment:

    def __init__(self, id: str, user_id: str, text: str, Expense_Comment_137: "Package_Bill" = None):
        self.id = id
        self.user_id = user_id
        self.text = text
        self.Expense_Comment_137 = Expense_Comment_137
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Expense_Comment_137(self):
        return self.__Expense_Comment_137
    @Expense_Comment_137.setter
    def Expense_Comment_137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Comment__Expense_Comment_137", None)
        self.__Expense_Comment_137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expense_Comment_036"):
                opp_val = getattr(old_value, "Expense_Comment_036", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expense_Comment_036"):
                opp_val = getattr(value, "Expense_Comment_036", None)
                if opp_val is None:
                    setattr(value, "Expense_Comment_036", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package_Bill:

    def __init__(self, id: str, date: str, payment_method: Package_PaymentMethod, attachment_id: str, sum: str, status: Package_ExpenseStatus, distance: str, Expense_Comment_036: set["Package_Comment"] = None, Expense_Bill_139: "Package_Expense" = None, Currency_Expense_141: "Package_Currency" = None, ExpenseType_Bill_143: "Package_ExpenseType" = None):
        self.id = id
        self.date = date
        self.payment_method = payment_method
        self.attachment_id = attachment_id
        self.sum = sum
        self.status = status
        self.distance = distance
        self.Expense_Comment_036 = Expense_Comment_036 if Expense_Comment_036 is not None else set()
        self.Expense_Bill_139 = Expense_Bill_139
        self.Currency_Expense_141 = Currency_Expense_141
        self.ExpenseType_Bill_143 = ExpenseType_Bill_143
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: Package_ExpenseStatus):
        self.__status = status

    @property
    def sum(self):
        return self.__sum
    @sum.setter
    def sum(self, sum: str):
        self.__sum = sum

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def payment_method(self):
        return self.__payment_method
    @payment_method.setter
    def payment_method(self, payment_method: Package_PaymentMethod):
        self.__payment_method = payment_method

    @property
    def attachment_id(self):
        return self.__attachment_id
    @attachment_id.setter
    def attachment_id(self, attachment_id: str):
        self.__attachment_id = attachment_id

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

    @property
    def Expense_Comment_036(self):
        return self.__Expense_Comment_036
    @Expense_Comment_036.setter
    def Expense_Comment_036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Bill__Expense_Comment_036", None)
        self.__Expense_Comment_036 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expense_Comment_137"):
                    opp_val = getattr(item, "Expense_Comment_137", None)
                    
                    if opp_val == self:
                        setattr(item, "Expense_Comment_137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expense_Comment_137"):
                    opp_val = getattr(item, "Expense_Comment_137", None)
                    
                    setattr(item, "Expense_Comment_137", self)
                    

    @property
    def Expense_Bill_139(self):
        return self.__Expense_Bill_139
    @Expense_Bill_139.setter
    def Expense_Bill_139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Bill__Expense_Bill_139", None)
        self.__Expense_Bill_139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expense_Bill_038"):
                opp_val = getattr(old_value, "Expense_Bill_038", None)
                if opp_val == self:
                    setattr(old_value, "Expense_Bill_038", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expense_Bill_038"):
                opp_val = getattr(value, "Expense_Bill_038", None)
                setattr(value, "Expense_Bill_038", self)

    @property
    def Currency_Expense_141(self):
        return self.__Currency_Expense_141
    @Currency_Expense_141.setter
    def Currency_Expense_141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Bill__Currency_Expense_141", None)
        self.__Currency_Expense_141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Currency_Expense_040"):
                opp_val = getattr(old_value, "Currency_Expense_040", None)
                if opp_val == self:
                    setattr(old_value, "Currency_Expense_040", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Currency_Expense_040"):
                opp_val = getattr(value, "Currency_Expense_040", None)
                setattr(value, "Currency_Expense_040", self)

    @property
    def ExpenseType_Bill_143(self):
        return self.__ExpenseType_Bill_143
    @ExpenseType_Bill_143.setter
    def ExpenseType_Bill_143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Bill__ExpenseType_Bill_143", None)
        self.__ExpenseType_Bill_143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExpenseType_Bill_042"):
                opp_val = getattr(old_value, "ExpenseType_Bill_042", None)
                if opp_val == self:
                    setattr(old_value, "ExpenseType_Bill_042", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExpenseType_Bill_042"):
                opp_val = getattr(value, "ExpenseType_Bill_042", None)
                setattr(value, "ExpenseType_Bill_042", self)



class Package_Expense:

    def __init__(self, project_id: str, id: str, user_id: str, manager_id: str, mission_id: str, Expense_Bill_038: "Package_Bill" = None):
        self.project_id = project_id
        self.id = id
        self.user_id = user_id
        self.manager_id = manager_id
        self.mission_id = mission_id
        self.Expense_Bill_038 = Expense_Bill_038
        
        pass
    @property
    def mission_id(self):
        return self.__mission_id
    @mission_id.setter
    def mission_id(self, mission_id: str):
        self.__mission_id = mission_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def manager_id(self):
        return self.__manager_id
    @manager_id.setter
    def manager_id(self, manager_id: str):
        self.__manager_id = manager_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_id(self):
        return self.__project_id
    @project_id.setter
    def project_id(self, project_id: str):
        self.__project_id = project_id

    @property
    def Expense_Bill_038(self):
        return self.__Expense_Bill_038
    @Expense_Bill_038.setter
    def Expense_Bill_038(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Expense__Expense_Bill_038", None)
        self.__Expense_Bill_038 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expense_Bill_139"):
                opp_val = getattr(old_value, "Expense_Bill_139", None)
                if opp_val == self:
                    setattr(old_value, "Expense_Bill_139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expense_Bill_139"):
                opp_val = getattr(value, "Expense_Bill_139", None)
                setattr(value, "Expense_Bill_139", self)



class Manage_Expenses__settings_Component:

    pass


class Manager_Actor3:

    pass


class Manager_Actor2:

    pass


class Review_collaborators__Expense_refunds_Component:

    pass


class Manager_Actor1:

    pass


class Office_Manager_Actor1:

    pass


class Consult_collaborators__Expenses_Component:

    pass


class Collaborator_Actor1:

    pass


class Manage_Expenses_Component:

    pass


class My_Expenses_general_use_case_diagram_Component:

    pass
