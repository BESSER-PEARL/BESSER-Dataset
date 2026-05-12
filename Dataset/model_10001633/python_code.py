from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class date(Enum):
    pass
class ot_Type(Enum):
    pass

############################################
# Definition of Classes
############################################







class Clark_Actor:

    pass


class Admin_Actor:

    pass


class Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase:

    pass


class Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase:

    pass


class Employee_Actor:

    pass





class Presentation_StaffUI:

    pass


class Package2_ETF:

    pass


class Package2_User_Permissions:

    def __init__(self, attribute: str, attribute2: str, User_groups_User_Permissions_1101: "Package2_User_groups" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.User_groups_User_Permissions_1101 = User_groups_User_Permissions_1101
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def User_groups_User_Permissions_1101(self):
        return self.__User_groups_User_Permissions_1101
    @User_groups_User_Permissions_1101.setter
    def User_groups_User_Permissions_1101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_User_Permissions__User_groups_User_Permissions_1101", None)
        self.__User_groups_User_Permissions_1101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_groups_User_Permissions_0100"):
                opp_val = getattr(old_value, "User_groups_User_Permissions_0100", None)
                if opp_val == self:
                    setattr(old_value, "User_groups_User_Permissions_0100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_groups_User_Permissions_0100"):
                opp_val = getattr(value, "User_groups_User_Permissions_0100", None)
                setattr(value, "User_groups_User_Permissions_0100", self)



class Package2_Messages:

    pass


class Package2_Advances:

    pass


class Package2_UserUpdates:

    pass


class Package2_Users:

    def __init__(self, id: int, firstname: int, lastname: int, email: int, password: int, Users_Employee_074: "Package2_Employee" = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.Users_Employee_074 = Users_Employee_074
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: int):
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: int):
        self.__email = email

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: int):
        self.__firstname = firstname

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Users_Employee_074(self):
        return self.__Users_Employee_074
    @Users_Employee_074.setter
    def Users_Employee_074(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Users__Users_Employee_074", None)
        self.__Users_Employee_074 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Users_Employee_175"):
                opp_val = getattr(old_value, "Users_Employee_175", None)
                if opp_val == self:
                    setattr(old_value, "Users_Employee_175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Users_Employee_175"):
                opp_val = getattr(value, "Users_Employee_175", None)
                setattr(value, "Users_Employee_175", self)



class Package2_User_groups:

    def __init__(self, attribute: str, attribute2: str, attribute3: str, Employee_User_groups_199: set["Package2_Employee"] = None, User_groups_User_Permissions_0100: "Package2_User_Permissions" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.Employee_User_groups_199 = Employee_User_groups_199 if Employee_User_groups_199 is not None else set()
        self.User_groups_User_Permissions_0100 = User_groups_User_Permissions_0100
        
        pass
    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Employee_User_groups_199(self):
        return self.__Employee_User_groups_199
    @Employee_User_groups_199.setter
    def Employee_User_groups_199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_User_groups__Employee_User_groups_199", None)
        self.__Employee_User_groups_199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_User_groups_098"):
                    opp_val = getattr(item, "Employee_User_groups_098", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_User_groups_098", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_User_groups_098"):
                    opp_val = getattr(item, "Employee_User_groups_098", None)
                    
                    setattr(item, "Employee_User_groups_098", self)
                    

    @property
    def User_groups_User_Permissions_0100(self):
        return self.__User_groups_User_Permissions_0100
    @User_groups_User_Permissions_0100.setter
    def User_groups_User_Permissions_0100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_User_groups__User_groups_User_Permissions_0100", None)
        self.__User_groups_User_Permissions_0100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_groups_User_Permissions_1101"):
                opp_val = getattr(old_value, "User_groups_User_Permissions_1101", None)
                if opp_val == self:
                    setattr(old_value, "User_groups_User_Permissions_1101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_groups_User_Permissions_1101"):
                opp_val = getattr(value, "User_groups_User_Permissions_1101", None)
                setattr(value, "User_groups_User_Permissions_1101", self)



class Package2_OT_Requests:

    def __init__(self, id: int, OtDay: date, OTType: int, EmpID: int, Employee_OT_Requests_179: "Package2_Employee" = None):
        self.id = id
        self.OtDay = OtDay
        self.OTType = OTType
        self.EmpID = EmpID
        self.Employee_OT_Requests_179 = Employee_OT_Requests_179
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def EmpID(self):
        return self.__EmpID
    @EmpID.setter
    def EmpID(self, EmpID: int):
        self.__EmpID = EmpID

    @property
    def OtDay(self):
        return self.__OtDay
    @OtDay.setter
    def OtDay(self, OtDay: date):
        self.__OtDay = OtDay

    @property
    def OTType(self):
        return self.__OTType
    @OTType.setter
    def OTType(self, OTType: int):
        self.__OTType = OTType

    @property
    def Employee_OT_Requests_179(self):
        return self.__Employee_OT_Requests_179
    @Employee_OT_Requests_179.setter
    def Employee_OT_Requests_179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_OT_Requests__Employee_OT_Requests_179", None)
        self.__Employee_OT_Requests_179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_OT_Requests_078"):
                opp_val = getattr(old_value, "Employee_OT_Requests_078", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_OT_Requests_078"):
                opp_val = getattr(value, "Employee_OT_Requests_078", None)
                if opp_val is None:
                    setattr(value, "Employee_OT_Requests_078", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package2_LeaveProfiles:

    def __init__(self, id: int, name: str, casual: int, anual: int, Employee_LeaveProfiles_191: "Package2_Employee" = None):
        self.id = id
        self.name = name
        self.casual = casual
        self.anual = anual
        self.Employee_LeaveProfiles_191 = Employee_LeaveProfiles_191
        
        pass
    @property
    def casual(self):
        return self.__casual
    @casual.setter
    def casual(self, casual: int):
        self.__casual = casual

    @property
    def anual(self):
        return self.__anual
    @anual.setter
    def anual(self, anual: int):
        self.__anual = anual

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Employee_LeaveProfiles_191(self):
        return self.__Employee_LeaveProfiles_191
    @Employee_LeaveProfiles_191.setter
    def Employee_LeaveProfiles_191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_LeaveProfiles__Employee_LeaveProfiles_191", None)
        self.__Employee_LeaveProfiles_191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_LeaveProfiles_090"):
                opp_val = getattr(old_value, "Employee_LeaveProfiles_090", None)
                if opp_val == self:
                    setattr(old_value, "Employee_LeaveProfiles_090", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_LeaveProfiles_090"):
                opp_val = getattr(value, "Employee_LeaveProfiles_090", None)
                setattr(value, "Employee_LeaveProfiles_090", self)



class Package2_Leave_Taken:

    def __init__(self, attribute: str, attribute2: str, Employee_Leave_Taken_183: "Package2_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_Leave_Taken_183 = Employee_Leave_Taken_183
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Employee_Leave_Taken_183(self):
        return self.__Employee_Leave_Taken_183
    @Employee_Leave_Taken_183.setter
    def Employee_Leave_Taken_183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Leave_Taken__Employee_Leave_Taken_183", None)
        self.__Employee_Leave_Taken_183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Leave_Taken_082"):
                opp_val = getattr(old_value, "Employee_Leave_Taken_082", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Leave_Taken_082"):
                opp_val = getattr(value, "Employee_Leave_Taken_082", None)
                if opp_val is None:
                    setattr(value, "Employee_Leave_Taken_082", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package2_Event:

    pass


class Package2_EPF:

    def __init__(self, id: int, precentage: int, effectve_date: Package2_UserUpdates):
        self.id = id
        self.precentage = precentage
        self.effectve_date = effectve_date
        
        pass
    @property
    def effectve_date(self):
        return self.__effectve_date
    @effectve_date.setter
    def effectve_date(self, effectve_date: Package2_UserUpdates):
        self.__effectve_date = effectve_date

    @property
    def precentage(self):
        return self.__precentage
    @precentage.setter
    def precentage(self, precentage: int):
        self.__precentage = precentage

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Package2_EmployeeSalary:

    def __init__(self, attribute: str, attribute2: str, Employee_EmployeeSalary_185: "Package2_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_EmployeeSalary_185 = Employee_EmployeeSalary_185
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Employee_EmployeeSalary_185(self):
        return self.__Employee_EmployeeSalary_185
    @Employee_EmployeeSalary_185.setter
    def Employee_EmployeeSalary_185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_EmployeeSalary__Employee_EmployeeSalary_185", None)
        self.__Employee_EmployeeSalary_185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_EmployeeSalary_084"):
                opp_val = getattr(old_value, "Employee_EmployeeSalary_084", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_EmployeeSalary_084"):
                opp_val = getattr(value, "Employee_EmployeeSalary_084", None)
                if opp_val is None:
                    setattr(value, "Employee_EmployeeSalary_084", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package2_EmployeeParoll:

    def __init__(self, id: int, empid: int, basicslaray: int, empid3: int, otamount: int, doyamount: int, epf: int, etf: str, Employee_EmployeeParoll_197: set["Package2_Employee"] = None):
        self.id = id
        self.empid = empid
        self.basicslaray = basicslaray
        self.empid3 = empid3
        self.otamount = otamount
        self.doyamount = doyamount
        self.epf = epf
        self.etf = etf
        self.Employee_EmployeeParoll_197 = Employee_EmployeeParoll_197 if Employee_EmployeeParoll_197 is not None else set()
        
        pass
    @property
    def etf(self):
        return self.__etf
    @etf.setter
    def etf(self, etf: str):
        self.__etf = etf

    @property
    def doyamount(self):
        return self.__doyamount
    @doyamount.setter
    def doyamount(self, doyamount: int):
        self.__doyamount = doyamount

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def otamount(self):
        return self.__otamount
    @otamount.setter
    def otamount(self, otamount: int):
        self.__otamount = otamount

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: int):
        self.__empid = empid

    @property
    def epf(self):
        return self.__epf
    @epf.setter
    def epf(self, epf: int):
        self.__epf = epf

    @property
    def basicslaray(self):
        return self.__basicslaray
    @basicslaray.setter
    def basicslaray(self, basicslaray: int):
        self.__basicslaray = basicslaray

    @property
    def empid3(self):
        return self.__empid3
    @empid3.setter
    def empid3(self, empid3: int):
        self.__empid3 = empid3

    @property
    def Employee_EmployeeParoll_197(self):
        return self.__Employee_EmployeeParoll_197
    @Employee_EmployeeParoll_197.setter
    def Employee_EmployeeParoll_197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_EmployeeParoll__Employee_EmployeeParoll_197", None)
        self.__Employee_EmployeeParoll_197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeParoll_096"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_096", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeParoll_096"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_096", None)
                    
                    if opp_val is None:
                        setattr(item, "Employee_EmployeeParoll_096", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Package2_Employee:

    def __init__(self, id: str, empid: str, depid: int, post: str, shift: str, usergroup: int, leavegroup: int, Users_Employee_175: "Package2_Users" = None, Employee_Shifts_080: "Package2_Shifts" = None, Employee_Leave_Taken_082: set["Package2_Leave_Taken"] = None, Employee_EmployeeSalary_084: set["Package2_EmployeeSalary"] = None, Allowance_Employee_187: "Package2_Allowance" = None, Employee_Messages_088: set["Package2_Messages"] = None, Employee_LeaveProfiles_090: "Package2_LeaveProfiles" = None, Employee_Posts_092: "Package2_Posts" = None, Departments_Employee_195: "Package2_Departments" = None, Employee_EmployeeParoll_096: set["Package2_EmployeeParoll"] = None, Employee_User_groups_098: "Package2_User_groups" = None, advances102: set["Package2_Advances"] = None, Attendance_Employee_177: set["Package2_Attendance"] = None, Employee_OT_Requests_078: set["Package2_OT_Requests"] = None):
        self.id = id
        self.empid = empid
        self.depid = depid
        self.post = post
        self.shift = shift
        self.usergroup = usergroup
        self.leavegroup = leavegroup
        self.Users_Employee_175 = Users_Employee_175
        self.Employee_Shifts_080 = Employee_Shifts_080
        self.Employee_Leave_Taken_082 = Employee_Leave_Taken_082 if Employee_Leave_Taken_082 is not None else set()
        self.Employee_EmployeeSalary_084 = Employee_EmployeeSalary_084 if Employee_EmployeeSalary_084 is not None else set()
        self.Allowance_Employee_187 = Allowance_Employee_187
        self.Employee_Messages_088 = Employee_Messages_088 if Employee_Messages_088 is not None else set()
        self.Employee_LeaveProfiles_090 = Employee_LeaveProfiles_090
        self.Employee_Posts_092 = Employee_Posts_092
        self.Departments_Employee_195 = Departments_Employee_195
        self.Employee_EmployeeParoll_096 = Employee_EmployeeParoll_096 if Employee_EmployeeParoll_096 is not None else set()
        self.Employee_User_groups_098 = Employee_User_groups_098
        self.advances102 = advances102 if advances102 is not None else set()
        self.Attendance_Employee_177 = Attendance_Employee_177 if Attendance_Employee_177 is not None else set()
        self.Employee_OT_Requests_078 = Employee_OT_Requests_078 if Employee_OT_Requests_078 is not None else set()
        
        pass
    @property
    def leavegroup(self):
        return self.__leavegroup
    @leavegroup.setter
    def leavegroup(self, leavegroup: int):
        self.__leavegroup = leavegroup

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: str):
        self.__empid = empid

    @property
    def post(self):
        return self.__post
    @post.setter
    def post(self, post: str):
        self.__post = post

    @property
    def usergroup(self):
        return self.__usergroup
    @usergroup.setter
    def usergroup(self, usergroup: int):
        self.__usergroup = usergroup

    @property
    def shift(self):
        return self.__shift
    @shift.setter
    def shift(self, shift: str):
        self.__shift = shift

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def depid(self):
        return self.__depid
    @depid.setter
    def depid(self, depid: int):
        self.__depid = depid

    @property
    def Departments_Employee_195(self):
        return self.__Departments_Employee_195
    @Departments_Employee_195.setter
    def Departments_Employee_195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Departments_Employee_195", None)
        self.__Departments_Employee_195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Departments_Employee_094"):
                opp_val = getattr(old_value, "Departments_Employee_094", None)
                if opp_val == self:
                    setattr(old_value, "Departments_Employee_094", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Departments_Employee_094"):
                opp_val = getattr(value, "Departments_Employee_094", None)
                setattr(value, "Departments_Employee_094", self)

    @property
    def Employee_Posts_092(self):
        return self.__Employee_Posts_092
    @Employee_Posts_092.setter
    def Employee_Posts_092(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_Posts_092", None)
        self.__Employee_Posts_092 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Posts_193"):
                opp_val = getattr(old_value, "Employee_Posts_193", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Posts_193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Posts_193"):
                opp_val = getattr(value, "Employee_Posts_193", None)
                setattr(value, "Employee_Posts_193", self)

    @property
    def Employee_EmployeeParoll_096(self):
        return self.__Employee_EmployeeParoll_096
    @Employee_EmployeeParoll_096.setter
    def Employee_EmployeeParoll_096(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_EmployeeParoll_096", None)
        self.__Employee_EmployeeParoll_096 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeParoll_197"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_197", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeParoll_197"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_197", None)
                    
                    if opp_val is None:
                        setattr(item, "Employee_EmployeeParoll_197", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Employee_User_groups_098(self):
        return self.__Employee_User_groups_098
    @Employee_User_groups_098.setter
    def Employee_User_groups_098(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_User_groups_098", None)
        self.__Employee_User_groups_098 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_User_groups_199"):
                opp_val = getattr(old_value, "Employee_User_groups_199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_User_groups_199"):
                opp_val = getattr(value, "Employee_User_groups_199", None)
                if opp_val is None:
                    setattr(value, "Employee_User_groups_199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee_LeaveProfiles_090(self):
        return self.__Employee_LeaveProfiles_090
    @Employee_LeaveProfiles_090.setter
    def Employee_LeaveProfiles_090(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_LeaveProfiles_090", None)
        self.__Employee_LeaveProfiles_090 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_LeaveProfiles_191"):
                opp_val = getattr(old_value, "Employee_LeaveProfiles_191", None)
                if opp_val == self:
                    setattr(old_value, "Employee_LeaveProfiles_191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_LeaveProfiles_191"):
                opp_val = getattr(value, "Employee_LeaveProfiles_191", None)
                setattr(value, "Employee_LeaveProfiles_191", self)

    @property
    def Allowance_Employee_187(self):
        return self.__Allowance_Employee_187
    @Allowance_Employee_187.setter
    def Allowance_Employee_187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Allowance_Employee_187", None)
        self.__Allowance_Employee_187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Allowance_Employee_086"):
                opp_val = getattr(old_value, "Allowance_Employee_086", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Allowance_Employee_086"):
                opp_val = getattr(value, "Allowance_Employee_086", None)
                if opp_val is None:
                    setattr(value, "Allowance_Employee_086", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee_EmployeeSalary_084(self):
        return self.__Employee_EmployeeSalary_084
    @Employee_EmployeeSalary_084.setter
    def Employee_EmployeeSalary_084(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_EmployeeSalary_084", None)
        self.__Employee_EmployeeSalary_084 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeSalary_185"):
                    opp_val = getattr(item, "Employee_EmployeeSalary_185", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_EmployeeSalary_185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeSalary_185"):
                    opp_val = getattr(item, "Employee_EmployeeSalary_185", None)
                    
                    setattr(item, "Employee_EmployeeSalary_185", self)
                    

    @property
    def Users_Employee_175(self):
        return self.__Users_Employee_175
    @Users_Employee_175.setter
    def Users_Employee_175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Users_Employee_175", None)
        self.__Users_Employee_175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Users_Employee_074"):
                opp_val = getattr(old_value, "Users_Employee_074", None)
                if opp_val == self:
                    setattr(old_value, "Users_Employee_074", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Users_Employee_074"):
                opp_val = getattr(value, "Users_Employee_074", None)
                setattr(value, "Users_Employee_074", self)

    @property
    def advances102(self):
        return self.__advances102
    @advances102.setter
    def advances102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__advances102", None)
        self.__advances102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Advances_1103"):
                    opp_val = getattr(item, "Employee_Advances_1103", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Advances_1103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Advances_1103"):
                    opp_val = getattr(item, "Employee_Advances_1103", None)
                    
                    setattr(item, "Employee_Advances_1103", self)
                    

    @property
    def Employee_OT_Requests_078(self):
        return self.__Employee_OT_Requests_078
    @Employee_OT_Requests_078.setter
    def Employee_OT_Requests_078(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_OT_Requests_078", None)
        self.__Employee_OT_Requests_078 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_OT_Requests_179"):
                    opp_val = getattr(item, "Employee_OT_Requests_179", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_OT_Requests_179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_OT_Requests_179"):
                    opp_val = getattr(item, "Employee_OT_Requests_179", None)
                    
                    setattr(item, "Employee_OT_Requests_179", self)
                    

    @property
    def Employee_Shifts_080(self):
        return self.__Employee_Shifts_080
    @Employee_Shifts_080.setter
    def Employee_Shifts_080(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_Shifts_080", None)
        self.__Employee_Shifts_080 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Shifts_181"):
                opp_val = getattr(old_value, "Employee_Shifts_181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Shifts_181"):
                opp_val = getattr(value, "Employee_Shifts_181", None)
                if opp_val is None:
                    setattr(value, "Employee_Shifts_181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attendance_Employee_177(self):
        return self.__Attendance_Employee_177
    @Attendance_Employee_177.setter
    def Attendance_Employee_177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Attendance_Employee_177", None)
        self.__Attendance_Employee_177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attendance_Employee_076"):
                    opp_val = getattr(item, "Attendance_Employee_076", None)
                    
                    if opp_val == self:
                        setattr(item, "Attendance_Employee_076", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attendance_Employee_076"):
                    opp_val = getattr(item, "Attendance_Employee_076", None)
                    
                    setattr(item, "Attendance_Employee_076", self)
                    

    @property
    def Employee_Messages_088(self):
        return self.__Employee_Messages_088
    @Employee_Messages_088.setter
    def Employee_Messages_088(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_Messages_088", None)
        self.__Employee_Messages_088 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Messages_189"):
                    opp_val = getattr(item, "Employee_Messages_189", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Messages_189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Messages_189"):
                    opp_val = getattr(item, "Employee_Messages_189", None)
                    
                    setattr(item, "Employee_Messages_189", self)
                    

    @property
    def Employee_Leave_Taken_082(self):
        return self.__Employee_Leave_Taken_082
    @Employee_Leave_Taken_082.setter
    def Employee_Leave_Taken_082(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Employee__Employee_Leave_Taken_082", None)
        self.__Employee_Leave_Taken_082 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Leave_Taken_183"):
                    opp_val = getattr(item, "Employee_Leave_Taken_183", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Leave_Taken_183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Leave_Taken_183"):
                    opp_val = getattr(item, "Employee_Leave_Taken_183", None)
                    
                    setattr(item, "Employee_Leave_Taken_183", self)
                    



class Package2_Posts:

    def __init__(self, id: int, attribute2: str, Employee_Posts_193: "Package2_Employee" = None):
        self.id = id
        self.attribute2 = attribute2
        self.Employee_Posts_193 = Employee_Posts_193
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Employee_Posts_193(self):
        return self.__Employee_Posts_193
    @Employee_Posts_193.setter
    def Employee_Posts_193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Posts__Employee_Posts_193", None)
        self.__Employee_Posts_193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Posts_092"):
                opp_val = getattr(old_value, "Employee_Posts_092", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Posts_092", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Posts_092"):
                opp_val = getattr(value, "Employee_Posts_092", None)
                setattr(value, "Employee_Posts_092", self)



class Package2_Shifts:

    def __init__(self, id: str, shiftaname: str, starttime: str, endtime: str, Employee_Shifts_181: set["Package2_Employee"] = None):
        self.id = id
        self.shiftaname = shiftaname
        self.starttime = starttime
        self.endtime = endtime
        self.Employee_Shifts_181 = Employee_Shifts_181 if Employee_Shifts_181 is not None else set()
        
        pass
    @property
    def starttime(self):
        return self.__starttime
    @starttime.setter
    def starttime(self, starttime: str):
        self.__starttime = starttime

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def shiftaname(self):
        return self.__shiftaname
    @shiftaname.setter
    def shiftaname(self, shiftaname: str):
        self.__shiftaname = shiftaname

    @property
    def endtime(self):
        return self.__endtime
    @endtime.setter
    def endtime(self, endtime: str):
        self.__endtime = endtime

    @property
    def Employee_Shifts_181(self):
        return self.__Employee_Shifts_181
    @Employee_Shifts_181.setter
    def Employee_Shifts_181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Shifts__Employee_Shifts_181", None)
        self.__Employee_Shifts_181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Shifts_080"):
                    opp_val = getattr(item, "Employee_Shifts_080", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Shifts_080", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Shifts_080"):
                    opp_val = getattr(item, "Employee_Shifts_080", None)
                    
                    setattr(item, "Employee_Shifts_080", self)
                    



class Package2_Departments:

    def __init__(self, id: int, depname: str, Departments_Employee_094: "Package2_Employee" = None):
        self.id = id
        self.depname = depname
        self.Departments_Employee_094 = Departments_Employee_094
        
        pass
    @property
    def depname(self):
        return self.__depname
    @depname.setter
    def depname(self, depname: str):
        self.__depname = depname

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Departments_Employee_094(self):
        return self.__Departments_Employee_094
    @Departments_Employee_094.setter
    def Departments_Employee_094(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Departments__Departments_Employee_094", None)
        self.__Departments_Employee_094 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Departments_Employee_195"):
                opp_val = getattr(old_value, "Departments_Employee_195", None)
                if opp_val == self:
                    setattr(old_value, "Departments_Employee_195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Departments_Employee_195"):
                opp_val = getattr(value, "Departments_Employee_195", None)
                setattr(value, "Departments_Employee_195", self)



class Package2_Deductions:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Package2_AllowanceTypes:

    pass


class Package2_DeuctionTypes:

    pass


class Package2_Attendance:

    def __init__(self, id: int, timein: str, timeout: str, empid: int, Attendance_Employee_076: "Package2_Employee" = None):
        self.id = id
        self.timein = timein
        self.timeout = timeout
        self.empid = empid
        self.Attendance_Employee_076 = Attendance_Employee_076
        
        pass
    @property
    def timeout(self):
        return self.__timeout
    @timeout.setter
    def timeout(self, timeout: str):
        self.__timeout = timeout

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def timein(self):
        return self.__timein
    @timein.setter
    def timein(self, timein: str):
        self.__timein = timein

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: int):
        self.__empid = empid

    @property
    def Attendance_Employee_076(self):
        return self.__Attendance_Employee_076
    @Attendance_Employee_076.setter
    def Attendance_Employee_076(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Attendance__Attendance_Employee_076", None)
        self.__Attendance_Employee_076 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attendance_Employee_177"):
                opp_val = getattr(old_value, "Attendance_Employee_177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attendance_Employee_177"):
                opp_val = getattr(value, "Attendance_Employee_177", None)
                if opp_val is None:
                    setattr(value, "Attendance_Employee_177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package2_Allowance:

    def __init__(self, id: int, emp_id: str, Effectivedate: str, Allowance_Employee_086: set["Package2_Employee"] = None):
        self.id = id
        self.emp_id = emp_id
        self.Effectivedate = Effectivedate
        self.Allowance_Employee_086 = Allowance_Employee_086 if Allowance_Employee_086 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Effectivedate(self):
        return self.__Effectivedate
    @Effectivedate.setter
    def Effectivedate(self, Effectivedate: str):
        self.__Effectivedate = Effectivedate

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: str):
        self.__emp_id = emp_id

    @property
    def Allowance_Employee_086(self):
        return self.__Allowance_Employee_086
    @Allowance_Employee_086.setter
    def Allowance_Employee_086(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package2_Allowance__Allowance_Employee_086", None)
        self.__Allowance_Employee_086 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Allowance_Employee_187"):
                    opp_val = getattr(item, "Allowance_Employee_187", None)
                    
                    if opp_val == self:
                        setattr(item, "Allowance_Employee_187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Allowance_Employee_187"):
                    opp_val = getattr(item, "Allowance_Employee_187", None)
                    
                    setattr(item, "Allowance_Employee_187", self)
                    



class Package_ETF:

    pass


class Package_User_Permissions:

    def __init__(self, attribute: str, attribute2: str, User_groups_User_Permissions_171: "Package_User_groups" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.User_groups_User_Permissions_171 = User_groups_User_Permissions_171
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def User_groups_User_Permissions_171(self):
        return self.__User_groups_User_Permissions_171
    @User_groups_User_Permissions_171.setter
    def User_groups_User_Permissions_171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_User_Permissions__User_groups_User_Permissions_171", None)
        self.__User_groups_User_Permissions_171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_groups_User_Permissions_070"):
                opp_val = getattr(old_value, "User_groups_User_Permissions_070", None)
                if opp_val == self:
                    setattr(old_value, "User_groups_User_Permissions_070", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_groups_User_Permissions_070"):
                opp_val = getattr(value, "User_groups_User_Permissions_070", None)
                setattr(value, "User_groups_User_Permissions_070", self)



class Package_Messages:

    pass


class Package_Advances:

    pass


class Package_UserUpdates:

    pass


class Package_Users:

    def __init__(self, id: int, firstname: int, lastname: int, email: int, password: int, Users_Employee_044: "Package_Employee" = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.Users_Employee_044 = Users_Employee_044
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: int):
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: int):
        self.__email = email

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: int):
        self.__firstname = firstname

    @property
    def Users_Employee_044(self):
        return self.__Users_Employee_044
    @Users_Employee_044.setter
    def Users_Employee_044(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Users__Users_Employee_044", None)
        self.__Users_Employee_044 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Users_Employee_145"):
                opp_val = getattr(old_value, "Users_Employee_145", None)
                if opp_val == self:
                    setattr(old_value, "Users_Employee_145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Users_Employee_145"):
                opp_val = getattr(value, "Users_Employee_145", None)
                setattr(value, "Users_Employee_145", self)



class Package_User_groups:

    def __init__(self, attribute: str, attribute2: str, attribute3: str, Employee_User_groups_169: set["Package_Employee"] = None, User_groups_User_Permissions_070: "Package_User_Permissions" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.Employee_User_groups_169 = Employee_User_groups_169 if Employee_User_groups_169 is not None else set()
        self.User_groups_User_Permissions_070 = User_groups_User_Permissions_070
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def User_groups_User_Permissions_070(self):
        return self.__User_groups_User_Permissions_070
    @User_groups_User_Permissions_070.setter
    def User_groups_User_Permissions_070(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_User_groups__User_groups_User_Permissions_070", None)
        self.__User_groups_User_Permissions_070 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_groups_User_Permissions_171"):
                opp_val = getattr(old_value, "User_groups_User_Permissions_171", None)
                if opp_val == self:
                    setattr(old_value, "User_groups_User_Permissions_171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_groups_User_Permissions_171"):
                opp_val = getattr(value, "User_groups_User_Permissions_171", None)
                setattr(value, "User_groups_User_Permissions_171", self)

    @property
    def Employee_User_groups_169(self):
        return self.__Employee_User_groups_169
    @Employee_User_groups_169.setter
    def Employee_User_groups_169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_User_groups__Employee_User_groups_169", None)
        self.__Employee_User_groups_169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_User_groups_068"):
                    opp_val = getattr(item, "Employee_User_groups_068", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_User_groups_068", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_User_groups_068"):
                    opp_val = getattr(item, "Employee_User_groups_068", None)
                    
                    setattr(item, "Employee_User_groups_068", self)
                    



class Package_OT_Requests:

    def __init__(self, id: int, OtDay: date, OTType: int, EmpID: int, Employee_OT_Requests_149: "Package_Employee" = None):
        self.id = id
        self.OtDay = OtDay
        self.OTType = OTType
        self.EmpID = EmpID
        self.Employee_OT_Requests_149 = Employee_OT_Requests_149
        
        pass
    @property
    def OtDay(self):
        return self.__OtDay
    @OtDay.setter
    def OtDay(self, OtDay: date):
        self.__OtDay = OtDay

    @property
    def EmpID(self):
        return self.__EmpID
    @EmpID.setter
    def EmpID(self, EmpID: int):
        self.__EmpID = EmpID

    @property
    def OTType(self):
        return self.__OTType
    @OTType.setter
    def OTType(self, OTType: int):
        self.__OTType = OTType

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Employee_OT_Requests_149(self):
        return self.__Employee_OT_Requests_149
    @Employee_OT_Requests_149.setter
    def Employee_OT_Requests_149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_OT_Requests__Employee_OT_Requests_149", None)
        self.__Employee_OT_Requests_149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_OT_Requests_048"):
                opp_val = getattr(old_value, "Employee_OT_Requests_048", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_OT_Requests_048"):
                opp_val = getattr(value, "Employee_OT_Requests_048", None)
                if opp_val is None:
                    setattr(value, "Employee_OT_Requests_048", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package_LeaveProfiles:

    def __init__(self, attribute: str, attribute2: str, Employee_LeaveProfiles_161: "Package_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_LeaveProfiles_161 = Employee_LeaveProfiles_161
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Employee_LeaveProfiles_161(self):
        return self.__Employee_LeaveProfiles_161
    @Employee_LeaveProfiles_161.setter
    def Employee_LeaveProfiles_161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_LeaveProfiles__Employee_LeaveProfiles_161", None)
        self.__Employee_LeaveProfiles_161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_LeaveProfiles_060"):
                opp_val = getattr(old_value, "Employee_LeaveProfiles_060", None)
                if opp_val == self:
                    setattr(old_value, "Employee_LeaveProfiles_060", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_LeaveProfiles_060"):
                opp_val = getattr(value, "Employee_LeaveProfiles_060", None)
                setattr(value, "Employee_LeaveProfiles_060", self)



class Package_Leave_Taken:

    def __init__(self, attribute: str, attribute2: str, Employee_Leave_Taken_153: "Package_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_Leave_Taken_153 = Employee_Leave_Taken_153
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Employee_Leave_Taken_153(self):
        return self.__Employee_Leave_Taken_153
    @Employee_Leave_Taken_153.setter
    def Employee_Leave_Taken_153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Leave_Taken__Employee_Leave_Taken_153", None)
        self.__Employee_Leave_Taken_153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Leave_Taken_052"):
                opp_val = getattr(old_value, "Employee_Leave_Taken_052", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Leave_Taken_052"):
                opp_val = getattr(value, "Employee_Leave_Taken_052", None)
                if opp_val is None:
                    setattr(value, "Employee_Leave_Taken_052", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package_Event:

    pass


class Package_EPF:

    def __init__(self, id: int, precentage: int, effectve_date: Package_UserUpdates):
        self.id = id
        self.precentage = precentage
        self.effectve_date = effectve_date
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def precentage(self):
        return self.__precentage
    @precentage.setter
    def precentage(self, precentage: int):
        self.__precentage = precentage

    @property
    def effectve_date(self):
        return self.__effectve_date
    @effectve_date.setter
    def effectve_date(self, effectve_date: Package_UserUpdates):
        self.__effectve_date = effectve_date



class Package_EmployeeSalary:

    def __init__(self, attribute: str, attribute2: str, Employee_EmployeeSalary_155: "Package_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_EmployeeSalary_155 = Employee_EmployeeSalary_155
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Employee_EmployeeSalary_155(self):
        return self.__Employee_EmployeeSalary_155
    @Employee_EmployeeSalary_155.setter
    def Employee_EmployeeSalary_155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_EmployeeSalary__Employee_EmployeeSalary_155", None)
        self.__Employee_EmployeeSalary_155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_EmployeeSalary_054"):
                opp_val = getattr(old_value, "Employee_EmployeeSalary_054", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_EmployeeSalary_054"):
                opp_val = getattr(value, "Employee_EmployeeSalary_054", None)
                if opp_val is None:
                    setattr(value, "Employee_EmployeeSalary_054", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package_EmployeeParoll:

    def __init__(self, attribute: str, attribute2: str, Employee_EmployeeParoll_167: set["Package_Employee"] = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_EmployeeParoll_167 = Employee_EmployeeParoll_167 if Employee_EmployeeParoll_167 is not None else set()
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Employee_EmployeeParoll_167(self):
        return self.__Employee_EmployeeParoll_167
    @Employee_EmployeeParoll_167.setter
    def Employee_EmployeeParoll_167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_EmployeeParoll__Employee_EmployeeParoll_167", None)
        self.__Employee_EmployeeParoll_167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeParoll_066"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_066", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeParoll_066"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_066", None)
                    
                    if opp_val is None:
                        setattr(item, "Employee_EmployeeParoll_066", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Package_Employee:

    def __init__(self, id: str, empid: str, depid: int, post: str, shift: str, usergroup: int, leavegroup: int, Users_Employee_145: "Package_Users" = None, Attendance_Employee_147: set["Package_Attendance"] = None, Employee_OT_Requests_048: set["Package_OT_Requests"] = None, Employee_Shifts_050: "Package_Shifts" = None, Employee_Leave_Taken_052: set["Package_Leave_Taken"] = None, Employee_EmployeeSalary_054: set["Package_EmployeeSalary"] = None, Allowance_Employee_157: "Package_Allowance" = None, Employee_Messages_058: set["Package_Messages"] = None, Employee_LeaveProfiles_060: "Package_LeaveProfiles" = None, Employee_Posts_062: "Package_Posts" = None, Departments_Employee_165: "Package_Departments" = None, Employee_EmployeeParoll_066: set["Package_EmployeeParoll"] = None, Employee_User_groups_068: "Package_User_groups" = None, advances72: set["Package_Advances"] = None):
        self.id = id
        self.empid = empid
        self.depid = depid
        self.post = post
        self.shift = shift
        self.usergroup = usergroup
        self.leavegroup = leavegroup
        self.Users_Employee_145 = Users_Employee_145
        self.Attendance_Employee_147 = Attendance_Employee_147 if Attendance_Employee_147 is not None else set()
        self.Employee_OT_Requests_048 = Employee_OT_Requests_048 if Employee_OT_Requests_048 is not None else set()
        self.Employee_Shifts_050 = Employee_Shifts_050
        self.Employee_Leave_Taken_052 = Employee_Leave_Taken_052 if Employee_Leave_Taken_052 is not None else set()
        self.Employee_EmployeeSalary_054 = Employee_EmployeeSalary_054 if Employee_EmployeeSalary_054 is not None else set()
        self.Allowance_Employee_157 = Allowance_Employee_157
        self.Employee_Messages_058 = Employee_Messages_058 if Employee_Messages_058 is not None else set()
        self.Employee_LeaveProfiles_060 = Employee_LeaveProfiles_060
        self.Employee_Posts_062 = Employee_Posts_062
        self.Departments_Employee_165 = Departments_Employee_165
        self.Employee_EmployeeParoll_066 = Employee_EmployeeParoll_066 if Employee_EmployeeParoll_066 is not None else set()
        self.Employee_User_groups_068 = Employee_User_groups_068
        self.advances72 = advances72 if advances72 is not None else set()
        
        pass
    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: str):
        self.__empid = empid

    @property
    def usergroup(self):
        return self.__usergroup
    @usergroup.setter
    def usergroup(self, usergroup: int):
        self.__usergroup = usergroup

    @property
    def post(self):
        return self.__post
    @post.setter
    def post(self, post: str):
        self.__post = post

    @property
    def depid(self):
        return self.__depid
    @depid.setter
    def depid(self, depid: int):
        self.__depid = depid

    @property
    def shift(self):
        return self.__shift
    @shift.setter
    def shift(self, shift: str):
        self.__shift = shift

    @property
    def leavegroup(self):
        return self.__leavegroup
    @leavegroup.setter
    def leavegroup(self, leavegroup: int):
        self.__leavegroup = leavegroup

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Employee_Posts_062(self):
        return self.__Employee_Posts_062
    @Employee_Posts_062.setter
    def Employee_Posts_062(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_Posts_062", None)
        self.__Employee_Posts_062 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Posts_163"):
                opp_val = getattr(old_value, "Employee_Posts_163", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Posts_163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Posts_163"):
                opp_val = getattr(value, "Employee_Posts_163", None)
                setattr(value, "Employee_Posts_163", self)

    @property
    def Users_Employee_145(self):
        return self.__Users_Employee_145
    @Users_Employee_145.setter
    def Users_Employee_145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Users_Employee_145", None)
        self.__Users_Employee_145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Users_Employee_044"):
                opp_val = getattr(old_value, "Users_Employee_044", None)
                if opp_val == self:
                    setattr(old_value, "Users_Employee_044", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Users_Employee_044"):
                opp_val = getattr(value, "Users_Employee_044", None)
                setattr(value, "Users_Employee_044", self)

    @property
    def Employee_LeaveProfiles_060(self):
        return self.__Employee_LeaveProfiles_060
    @Employee_LeaveProfiles_060.setter
    def Employee_LeaveProfiles_060(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_LeaveProfiles_060", None)
        self.__Employee_LeaveProfiles_060 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_LeaveProfiles_161"):
                opp_val = getattr(old_value, "Employee_LeaveProfiles_161", None)
                if opp_val == self:
                    setattr(old_value, "Employee_LeaveProfiles_161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_LeaveProfiles_161"):
                opp_val = getattr(value, "Employee_LeaveProfiles_161", None)
                setattr(value, "Employee_LeaveProfiles_161", self)

    @property
    def Employee_EmployeeSalary_054(self):
        return self.__Employee_EmployeeSalary_054
    @Employee_EmployeeSalary_054.setter
    def Employee_EmployeeSalary_054(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_EmployeeSalary_054", None)
        self.__Employee_EmployeeSalary_054 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeSalary_155"):
                    opp_val = getattr(item, "Employee_EmployeeSalary_155", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_EmployeeSalary_155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeSalary_155"):
                    opp_val = getattr(item, "Employee_EmployeeSalary_155", None)
                    
                    setattr(item, "Employee_EmployeeSalary_155", self)
                    

    @property
    def Employee_Messages_058(self):
        return self.__Employee_Messages_058
    @Employee_Messages_058.setter
    def Employee_Messages_058(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_Messages_058", None)
        self.__Employee_Messages_058 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Messages_159"):
                    opp_val = getattr(item, "Employee_Messages_159", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Messages_159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Messages_159"):
                    opp_val = getattr(item, "Employee_Messages_159", None)
                    
                    setattr(item, "Employee_Messages_159", self)
                    

    @property
    def Employee_OT_Requests_048(self):
        return self.__Employee_OT_Requests_048
    @Employee_OT_Requests_048.setter
    def Employee_OT_Requests_048(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_OT_Requests_048", None)
        self.__Employee_OT_Requests_048 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_OT_Requests_149"):
                    opp_val = getattr(item, "Employee_OT_Requests_149", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_OT_Requests_149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_OT_Requests_149"):
                    opp_val = getattr(item, "Employee_OT_Requests_149", None)
                    
                    setattr(item, "Employee_OT_Requests_149", self)
                    

    @property
    def advances72(self):
        return self.__advances72
    @advances72.setter
    def advances72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__advances72", None)
        self.__advances72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Advances_173"):
                    opp_val = getattr(item, "Employee_Advances_173", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Advances_173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Advances_173"):
                    opp_val = getattr(item, "Employee_Advances_173", None)
                    
                    setattr(item, "Employee_Advances_173", self)
                    

    @property
    def Employee_Shifts_050(self):
        return self.__Employee_Shifts_050
    @Employee_Shifts_050.setter
    def Employee_Shifts_050(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_Shifts_050", None)
        self.__Employee_Shifts_050 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Shifts_151"):
                opp_val = getattr(old_value, "Employee_Shifts_151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Shifts_151"):
                opp_val = getattr(value, "Employee_Shifts_151", None)
                if opp_val is None:
                    setattr(value, "Employee_Shifts_151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Departments_Employee_165(self):
        return self.__Departments_Employee_165
    @Departments_Employee_165.setter
    def Departments_Employee_165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Departments_Employee_165", None)
        self.__Departments_Employee_165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Departments_Employee_064"):
                opp_val = getattr(old_value, "Departments_Employee_064", None)
                if opp_val == self:
                    setattr(old_value, "Departments_Employee_064", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Departments_Employee_064"):
                opp_val = getattr(value, "Departments_Employee_064", None)
                setattr(value, "Departments_Employee_064", self)

    @property
    def Employee_EmployeeParoll_066(self):
        return self.__Employee_EmployeeParoll_066
    @Employee_EmployeeParoll_066.setter
    def Employee_EmployeeParoll_066(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_EmployeeParoll_066", None)
        self.__Employee_EmployeeParoll_066 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_EmployeeParoll_167"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_167", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_EmployeeParoll_167"):
                    opp_val = getattr(item, "Employee_EmployeeParoll_167", None)
                    
                    if opp_val is None:
                        setattr(item, "Employee_EmployeeParoll_167", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Attendance_Employee_147(self):
        return self.__Attendance_Employee_147
    @Attendance_Employee_147.setter
    def Attendance_Employee_147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Attendance_Employee_147", None)
        self.__Attendance_Employee_147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attendance_Employee_046"):
                    opp_val = getattr(item, "Attendance_Employee_046", None)
                    
                    if opp_val == self:
                        setattr(item, "Attendance_Employee_046", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attendance_Employee_046"):
                    opp_val = getattr(item, "Attendance_Employee_046", None)
                    
                    setattr(item, "Attendance_Employee_046", self)
                    

    @property
    def Allowance_Employee_157(self):
        return self.__Allowance_Employee_157
    @Allowance_Employee_157.setter
    def Allowance_Employee_157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Allowance_Employee_157", None)
        self.__Allowance_Employee_157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Allowance_Employee_056"):
                opp_val = getattr(old_value, "Allowance_Employee_056", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Allowance_Employee_056"):
                opp_val = getattr(value, "Allowance_Employee_056", None)
                if opp_val is None:
                    setattr(value, "Allowance_Employee_056", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee_User_groups_068(self):
        return self.__Employee_User_groups_068
    @Employee_User_groups_068.setter
    def Employee_User_groups_068(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_User_groups_068", None)
        self.__Employee_User_groups_068 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_User_groups_169"):
                opp_val = getattr(old_value, "Employee_User_groups_169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_User_groups_169"):
                opp_val = getattr(value, "Employee_User_groups_169", None)
                if opp_val is None:
                    setattr(value, "Employee_User_groups_169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee_Leave_Taken_052(self):
        return self.__Employee_Leave_Taken_052
    @Employee_Leave_Taken_052.setter
    def Employee_Leave_Taken_052(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Employee__Employee_Leave_Taken_052", None)
        self.__Employee_Leave_Taken_052 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Leave_Taken_153"):
                    opp_val = getattr(item, "Employee_Leave_Taken_153", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Leave_Taken_153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Leave_Taken_153"):
                    opp_val = getattr(item, "Employee_Leave_Taken_153", None)
                    
                    setattr(item, "Employee_Leave_Taken_153", self)
                    



class Package_Posts:

    def __init__(self, attribute: str, attribute2: str, Employee_Posts_163: "Package_Employee" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_Posts_163 = Employee_Posts_163
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Employee_Posts_163(self):
        return self.__Employee_Posts_163
    @Employee_Posts_163.setter
    def Employee_Posts_163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Posts__Employee_Posts_163", None)
        self.__Employee_Posts_163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Posts_062"):
                opp_val = getattr(old_value, "Employee_Posts_062", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Posts_062", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Posts_062"):
                opp_val = getattr(value, "Employee_Posts_062", None)
                setattr(value, "Employee_Posts_062", self)



class Package_Shifts:

    def __init__(self, attribute: str, attribute2: str, Employee_Shifts_151: set["Package_Employee"] = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.Employee_Shifts_151 = Employee_Shifts_151 if Employee_Shifts_151 is not None else set()
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Employee_Shifts_151(self):
        return self.__Employee_Shifts_151
    @Employee_Shifts_151.setter
    def Employee_Shifts_151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Shifts__Employee_Shifts_151", None)
        self.__Employee_Shifts_151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee_Shifts_050"):
                    opp_val = getattr(item, "Employee_Shifts_050", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee_Shifts_050", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee_Shifts_050"):
                    opp_val = getattr(item, "Employee_Shifts_050", None)
                    
                    setattr(item, "Employee_Shifts_050", self)
                    



class Package_Departments:

    def __init__(self, id: int, Departments_Employee_064: "Package_Employee" = None):
        self.id = id
        self.Departments_Employee_064 = Departments_Employee_064
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Departments_Employee_064(self):
        return self.__Departments_Employee_064
    @Departments_Employee_064.setter
    def Departments_Employee_064(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Departments__Departments_Employee_064", None)
        self.__Departments_Employee_064 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Departments_Employee_165"):
                opp_val = getattr(old_value, "Departments_Employee_165", None)
                if opp_val == self:
                    setattr(old_value, "Departments_Employee_165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Departments_Employee_165"):
                opp_val = getattr(value, "Departments_Employee_165", None)
                setattr(value, "Departments_Employee_165", self)



class Package_Deductions:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Package_AllowanceTypes:

    pass


class Package_DeuctionTypes:

    pass


class Package_Attendance:

    def __init__(self, id: int, timein: str, timeout: str, empid: int, Attendance_Employee_046: "Package_Employee" = None):
        self.id = id
        self.timein = timein
        self.timeout = timeout
        self.empid = empid
        self.Attendance_Employee_046 = Attendance_Employee_046
        
        pass
    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: int):
        self.__empid = empid

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def timein(self):
        return self.__timein
    @timein.setter
    def timein(self, timein: str):
        self.__timein = timein

    @property
    def timeout(self):
        return self.__timeout
    @timeout.setter
    def timeout(self, timeout: str):
        self.__timeout = timeout

    @property
    def Attendance_Employee_046(self):
        return self.__Attendance_Employee_046
    @Attendance_Employee_046.setter
    def Attendance_Employee_046(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Attendance__Attendance_Employee_046", None)
        self.__Attendance_Employee_046 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attendance_Employee_147"):
                opp_val = getattr(old_value, "Attendance_Employee_147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attendance_Employee_147"):
                opp_val = getattr(value, "Attendance_Employee_147", None)
                if opp_val is None:
                    setattr(value, "Attendance_Employee_147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Package_Allowance:

    def __init__(self, id: int, emp_id: str, Effectivedate: str, Allowance_Employee_056: set["Package_Employee"] = None):
        self.id = id
        self.emp_id = emp_id
        self.Effectivedate = Effectivedate
        self.Allowance_Employee_056 = Allowance_Employee_056 if Allowance_Employee_056 is not None else set()
        
        pass
    @property
    def Effectivedate(self):
        return self.__Effectivedate
    @Effectivedate.setter
    def Effectivedate(self, Effectivedate: str):
        self.__Effectivedate = Effectivedate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: str):
        self.__emp_id = emp_id

    @property
    def Allowance_Employee_056(self):
        return self.__Allowance_Employee_056
    @Allowance_Employee_056.setter
    def Allowance_Employee_056(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Package_Allowance__Allowance_Employee_056", None)
        self.__Allowance_Employee_056 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Allowance_Employee_157"):
                    opp_val = getattr(item, "Allowance_Employee_157", None)
                    
                    if opp_val == self:
                        setattr(item, "Allowance_Employee_157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Allowance_Employee_157"):
                    opp_val = getattr(item, "Allowance_Employee_157", None)
                    
                    setattr(item, "Allowance_Employee_157", self)
                    



class Interface_Interface:

    pass


class Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1:

    pass
