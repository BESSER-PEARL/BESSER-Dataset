from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Manager_Actor:

    pass


class Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase:

    pass


class Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase:

    pass


class Clark1_Actor:

    pass





class Class_Diagram_for_Proposed_system_overtimeRequests:

    def __init__(self, id: str, date: str, start_time: str, nd_time: str, employee51: "Class_Diagram_for_Proposed_system_Employee" = None):
        self.id = id
        self.date = date
        self.start_time = start_time
        self.nd_time = nd_time
        self.employee51 = employee51
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def nd_time(self):
        return self.__nd_time
    @nd_time.setter
    def nd_time(self, nd_time: str):
        self.__nd_time = nd_time

    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self, start_time: str):
        self.__start_time = start_time

    @property
    def employee51(self):
        return self.__employee51
    @employee51.setter
    def employee51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_overtimeRequests__employee51", None)
        self.__employee51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "overtimeRequests50"):
                opp_val = getattr(old_value, "overtimeRequests50", None)
                if opp_val == self:
                    setattr(old_value, "overtimeRequests50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "overtimeRequests50"):
                opp_val = getattr(value, "overtimeRequests50", None)
                setattr(value, "overtimeRequests50", self)



class Class_Diagram_for_Proposed_system_Calender:

    def __init__(self, author_id: str, depid: str, id: str, eventType: str, events48: "Class_Diagram_for_Proposed_system_Events" = None):
        self.author_id = author_id
        self.depid = depid
        self.id = id
        self.eventType = eventType
        self.events48 = events48
        
        pass
    @property
    def eventType(self):
        return self.__eventType
    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def depid(self):
        return self.__depid
    @depid.setter
    def depid(self, depid: str):
        self.__depid = depid

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def author_id(self):
        return self.__author_id
    @author_id.setter
    def author_id(self, author_id: str):
        self.__author_id = author_id

    @property
    def events48(self):
        return self.__events48
    @events48.setter
    def events48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Calender__events48", None)
        self.__events48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calender49"):
                opp_val = getattr(old_value, "calender49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calender49"):
                opp_val = getattr(value, "calender49", None)
                if opp_val is None:
                    setattr(value, "calender49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class_Diagram_for_Proposed_system_ETF:

    def __init__(self, id: str, precentage: str, leavesAllocated47: "Class_Diagram_for_Proposed_system_LeavesAllocated" = None):
        self.id = id
        self.precentage = precentage
        self.leavesAllocated47 = leavesAllocated47
        
        pass
    @property
    def precentage(self):
        return self.__precentage
    @precentage.setter
    def precentage(self, precentage: str):
        self.__precentage = precentage

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def leavesAllocated47(self):
        return self.__leavesAllocated47
    @leavesAllocated47.setter
    def leavesAllocated47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_ETF__leavesAllocated47", None)
        self.__leavesAllocated47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTF46"):
                opp_val = getattr(old_value, "eTF46", None)
                if opp_val == self:
                    setattr(old_value, "eTF46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTF46"):
                opp_val = getattr(value, "eTF46", None)
                setattr(value, "eTF46", self)



class Class_Diagram_for_Proposed_system_EPF:

    def __init__(self, id: str, precentage: str, leavesAllocated45: "Class_Diagram_for_Proposed_system_LeavesAllocated" = None):
        self.id = id
        self.precentage = precentage
        self.leavesAllocated45 = leavesAllocated45
        
        pass
    @property
    def precentage(self):
        return self.__precentage
    @precentage.setter
    def precentage(self, precentage: str):
        self.__precentage = precentage

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def leavesAllocated45(self):
        return self.__leavesAllocated45
    @leavesAllocated45.setter
    def leavesAllocated45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_EPF__leavesAllocated45", None)
        self.__leavesAllocated45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePF44"):
                opp_val = getattr(old_value, "ePF44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePF44"):
                opp_val = getattr(value, "ePF44", None)
                if opp_val is None:
                    setattr(value, "ePF44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class_Diagram_for_Proposed_system_Events:

    def __init__(self, id: str, type: str, calender49: set["Class_Diagram_for_Proposed_system_Calender"] = None):
        self.id = id
        self.type = type
        self.calender49 = calender49 if calender49 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def calender49(self):
        return self.__calender49
    @calender49.setter
    def calender49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Events__calender49", None)
        self.__calender49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events48"):
                    opp_val = getattr(item, "events48", None)
                    
                    if opp_val == self:
                        setattr(item, "events48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events48"):
                    opp_val = getattr(item, "events48", None)
                    
                    setattr(item, "events48", self)
                    



class Class_Diagram_for_Proposed_system_LeavesAllocated:

    def __init__(self, id: str, empId: str, leaveType: str, noOfLeaves: str, employee39: "Class_Diagram_for_Proposed_system_Employee" = None, ePF44: set["Class_Diagram_for_Proposed_system_EPF"] = None, eTF46: "Class_Diagram_for_Proposed_system_ETF" = None):
        self.id = id
        self.empId = empId
        self.leaveType = leaveType
        self.noOfLeaves = noOfLeaves
        self.employee39 = employee39
        self.ePF44 = ePF44 if ePF44 is not None else set()
        self.eTF46 = eTF46
        
        pass
    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def leaveType(self):
        return self.__leaveType
    @leaveType.setter
    def leaveType(self, leaveType: str):
        self.__leaveType = leaveType

    @property
    def noOfLeaves(self):
        return self.__noOfLeaves
    @noOfLeaves.setter
    def noOfLeaves(self, noOfLeaves: str):
        self.__noOfLeaves = noOfLeaves

    @property
    def eTF46(self):
        return self.__eTF46
    @eTF46.setter
    def eTF46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_LeavesAllocated__eTF46", None)
        self.__eTF46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leavesAllocated47"):
                opp_val = getattr(old_value, "leavesAllocated47", None)
                if opp_val == self:
                    setattr(old_value, "leavesAllocated47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leavesAllocated47"):
                opp_val = getattr(value, "leavesAllocated47", None)
                setattr(value, "leavesAllocated47", self)

    @property
    def ePF44(self):
        return self.__ePF44
    @ePF44.setter
    def ePF44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_LeavesAllocated__ePF44", None)
        self.__ePF44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "leavesAllocated45"):
                    opp_val = getattr(item, "leavesAllocated45", None)
                    
                    if opp_val == self:
                        setattr(item, "leavesAllocated45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "leavesAllocated45"):
                    opp_val = getattr(item, "leavesAllocated45", None)
                    
                    setattr(item, "leavesAllocated45", self)
                    

    @property
    def employee39(self):
        return self.__employee39
    @employee39.setter
    def employee39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_LeavesAllocated__employee39", None)
        self.__employee39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leavesAllocated38"):
                opp_val = getattr(old_value, "leavesAllocated38", None)
                if opp_val == self:
                    setattr(old_value, "leavesAllocated38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leavesAllocated38"):
                opp_val = getattr(value, "leavesAllocated38", None)
                setattr(value, "leavesAllocated38", self)



class Class_Diagram_for_Proposed_system_Attendance:

    def __init__(self, id: str, empId: str, clock_in: str, clock_out: str, date: str, attribute: str, employee36: "Class_Diagram_for_Proposed_system_Employee" = None):
        self.id = id
        self.empId = empId
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.date = date
        self.attribute = attribute
        self.employee36 = employee36
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

    @property
    def clock_out(self):
        return self.__clock_out
    @clock_out.setter
    def clock_out(self, clock_out: str):
        self.__clock_out = clock_out

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def clock_in(self):
        return self.__clock_in
    @clock_in.setter
    def clock_in(self, clock_in: str):
        self.__clock_in = clock_in

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def employee36(self):
        return self.__employee36
    @employee36.setter
    def employee36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Attendance__employee36", None)
        self.__employee36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance37"):
                opp_val = getattr(old_value, "attendance37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance37"):
                opp_val = getattr(value, "attendance37", None)
                if opp_val is None:
                    setattr(value, "attendance37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class_Diagram_for_Proposed_system_Post:

    def __init__(self, id: str, name: str, deptId: str, leavesEntitled: str, attribute: str, department33: "Class_Diagram_for_Proposed_system_Department" = None, employee35: "Class_Diagram_for_Proposed_system_Employee" = None):
        self.id = id
        self.name = name
        self.deptId = deptId
        self.leavesEntitled = leavesEntitled
        self.attribute = attribute
        self.department33 = department33
        self.employee35 = employee35
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

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
    def leavesEntitled(self):
        return self.__leavesEntitled
    @leavesEntitled.setter
    def leavesEntitled(self, leavesEntitled: str):
        self.__leavesEntitled = leavesEntitled

    @property
    def deptId(self):
        return self.__deptId
    @deptId.setter
    def deptId(self, deptId: str):
        self.__deptId = deptId

    @property
    def department33(self):
        return self.__department33
    @department33.setter
    def department33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Post__department33", None)
        self.__department33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post32"):
                opp_val = getattr(old_value, "post32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post32"):
                opp_val = getattr(value, "post32", None)
                if opp_val is None:
                    setattr(value, "post32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee35(self):
        return self.__employee35
    @employee35.setter
    def employee35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Post__employee35", None)
        self.__employee35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post34"):
                opp_val = getattr(old_value, "post34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post34"):
                opp_val = getattr(value, "post34", None)
                if opp_val is None:
                    setattr(value, "post34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class_Diagram_for_Proposed_system_Advances:

    def __init__(self, id: str, amount: str, issueDate: str, installments: str, salaryId: str, salary28: set["Class_Diagram_for_Proposed_system_Salary"] = None):
        self.id = id
        self.amount = amount
        self.issueDate = issueDate
        self.installments = installments
        self.salaryId = salaryId
        self.salary28 = salary28 if salary28 is not None else set()
        
        pass
    @property
    def installments(self):
        return self.__installments
    @installments.setter
    def installments(self, installments: str):
        self.__installments = installments

    @property
    def issueDate(self):
        return self.__issueDate
    @issueDate.setter
    def issueDate(self, issueDate: str):
        self.__issueDate = issueDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def salaryId(self):
        return self.__salaryId
    @salaryId.setter
    def salaryId(self, salaryId: str):
        self.__salaryId = salaryId

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def salary28(self):
        return self.__salary28
    @salary28.setter
    def salary28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Advances__salary28", None)
        self.__salary28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "advances229"):
                    opp_val = getattr(item, "advances229", None)
                    
                    if opp_val == self:
                        setattr(item, "advances229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "advances229"):
                    opp_val = getattr(item, "advances229", None)
                    
                    setattr(item, "advances229", self)
                    



class Class_Diagram_for_Proposed_system_Deductions:

    def __init__(self, id: str, amount: str, deductDate: str, deducType: str, salaryId: str, salary26: "Class_Diagram_for_Proposed_system_Salary" = None):
        self.id = id
        self.amount = amount
        self.deductDate = deductDate
        self.deducType = deducType
        self.salaryId = salaryId
        self.salary26 = salary26
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def salaryId(self):
        return self.__salaryId
    @salaryId.setter
    def salaryId(self, salaryId: str):
        self.__salaryId = salaryId

    @property
    def deductDate(self):
        return self.__deductDate
    @deductDate.setter
    def deductDate(self, deductDate: str):
        self.__deductDate = deductDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def deducType(self):
        return self.__deducType
    @deducType.setter
    def deducType(self, deducType: str):
        self.__deducType = deducType

    @property
    def salary26(self):
        return self.__salary26
    @salary26.setter
    def salary26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Deductions__salary26", None)
        self.__salary26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deductions227"):
                opp_val = getattr(old_value, "deductions227", None)
                if opp_val == self:
                    setattr(old_value, "deductions227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deductions227"):
                opp_val = getattr(value, "deductions227", None)
                setattr(value, "deductions227", self)



class Class_Diagram_for_Proposed_system_Allowances:

    def __init__(self, id: str, amount: str, allowanceType: str, issueDate: str, salaryId: str, salary24: "Class_Diagram_for_Proposed_system_Salary" = None):
        self.id = id
        self.amount = amount
        self.allowanceType = allowanceType
        self.issueDate = issueDate
        self.salaryId = salaryId
        self.salary24 = salary24
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def issueDate(self):
        return self.__issueDate
    @issueDate.setter
    def issueDate(self, issueDate: str):
        self.__issueDate = issueDate

    @property
    def salaryId(self):
        return self.__salaryId
    @salaryId.setter
    def salaryId(self, salaryId: str):
        self.__salaryId = salaryId

    @property
    def allowanceType(self):
        return self.__allowanceType
    @allowanceType.setter
    def allowanceType(self, allowanceType: str):
        self.__allowanceType = allowanceType

    @property
    def salary24(self):
        return self.__salary24
    @salary24.setter
    def salary24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Allowances__salary24", None)
        self.__salary24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allowances225"):
                opp_val = getattr(old_value, "allowances225", None)
                if opp_val == self:
                    setattr(old_value, "allowances225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allowances225"):
                opp_val = getattr(value, "allowances225", None)
                setattr(value, "allowances225", self)



class Class_Diagram_for_Proposed_system_Salary:

    def __init__(self, id: str, payDate: str, basicPay: str, allowances: str, deductions: str, advances: str, empId: str, overtimes: str, EPF: str, ETF: str, allowances225: "Class_Diagram_for_Proposed_system_Allowances" = None, deductions227: "Class_Diagram_for_Proposed_system_Deductions" = None, advances229: "Class_Diagram_for_Proposed_system_Advances" = None):
        self.id = id
        self.payDate = payDate
        self.basicPay = basicPay
        self.allowances = allowances
        self.deductions = deductions
        self.advances = advances
        self.empId = empId
        self.overtimes = overtimes
        self.EPF = EPF
        self.ETF = ETF
        self.allowances225 = allowances225
        self.deductions227 = deductions227
        self.advances229 = advances229
        
        pass
    @property
    def allowances(self):
        return self.__allowances
    @allowances.setter
    def allowances(self, allowances: str):
        self.__allowances = allowances

    @property
    def overtimes(self):
        return self.__overtimes
    @overtimes.setter
    def overtimes(self, overtimes: str):
        self.__overtimes = overtimes

    @property
    def basicPay(self):
        return self.__basicPay
    @basicPay.setter
    def basicPay(self, basicPay: str):
        self.__basicPay = basicPay

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

    @property
    def deductions(self):
        return self.__deductions
    @deductions.setter
    def deductions(self, deductions: str):
        self.__deductions = deductions

    @property
    def advances(self):
        return self.__advances
    @advances.setter
    def advances(self, advances: str):
        self.__advances = advances

    @property
    def EPF(self):
        return self.__EPF
    @EPF.setter
    def EPF(self, EPF: str):
        self.__EPF = EPF

    @property
    def payDate(self):
        return self.__payDate
    @payDate.setter
    def payDate(self, payDate: str):
        self.__payDate = payDate

    @property
    def ETF(self):
        return self.__ETF
    @ETF.setter
    def ETF(self, ETF: str):
        self.__ETF = ETF

    @property
    def advances229(self):
        return self.__advances229
    @advances229.setter
    def advances229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Salary__advances229", None)
        self.__advances229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary28"):
                opp_val = getattr(old_value, "salary28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary28"):
                opp_val = getattr(value, "salary28", None)
                if opp_val is None:
                    setattr(value, "salary28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def allowances225(self):
        return self.__allowances225
    @allowances225.setter
    def allowances225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Salary__allowances225", None)
        self.__allowances225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary24"):
                opp_val = getattr(old_value, "salary24", None)
                if opp_val == self:
                    setattr(old_value, "salary24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary24"):
                opp_val = getattr(value, "salary24", None)
                setattr(value, "salary24", self)

    @property
    def deductions227(self):
        return self.__deductions227
    @deductions227.setter
    def deductions227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Salary__deductions227", None)
        self.__deductions227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary26"):
                opp_val = getattr(old_value, "salary26", None)
                if opp_val == self:
                    setattr(old_value, "salary26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary26"):
                opp_val = getattr(value, "salary26", None)
                setattr(value, "salary26", self)



class Class_Diagram_for_Proposed_system_Department:

    def __init__(self, id: str, name: str, empId: str, employee23: set["Class_Diagram_for_Proposed_system_Employee"] = None, post32: set["Class_Diagram_for_Proposed_system_Post"] = None):
        self.id = id
        self.name = name
        self.empId = empId
        self.employee23 = employee23 if employee23 is not None else set()
        self.post32 = post32 if post32 is not None else set()
        
        pass
    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

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
    def employee23(self):
        return self.__employee23
    @employee23.setter
    def employee23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Department__employee23", None)
        self.__employee23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department22"):
                    opp_val = getattr(item, "department22", None)
                    
                    if opp_val == self:
                        setattr(item, "department22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department22"):
                    opp_val = getattr(item, "department22", None)
                    
                    setattr(item, "department22", self)
                    

    @property
    def post32(self):
        return self.__post32
    @post32.setter
    def post32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Department__post32", None)
        self.__post32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department33"):
                    opp_val = getattr(item, "department33", None)
                    
                    if opp_val == self:
                        setattr(item, "department33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department33"):
                    opp_val = getattr(item, "department33", None)
                    
                    setattr(item, "department33", self)
                    



class Class_Diagram_for_Proposed_system_LeaveTaken:

    def __init__(self, id: str, empId: str, leaveType: str, leaveDate: str, attribute5: str, employee31: set["Class_Diagram_for_Proposed_system_Employee"] = None):
        self.id = id
        self.empId = empId
        self.leaveType = leaveType
        self.leaveDate = leaveDate
        self.attribute5 = attribute5
        self.employee31 = employee31 if employee31 is not None else set()
        
        pass
    @property
    def attribute5(self):
        return self.__attribute5
    @attribute5.setter
    def attribute5(self, attribute5: str):
        self.__attribute5 = attribute5

    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

    @property
    def leaveType(self):
        return self.__leaveType
    @leaveType.setter
    def leaveType(self, leaveType: str):
        self.__leaveType = leaveType

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def leaveDate(self):
        return self.__leaveDate
    @leaveDate.setter
    def leaveDate(self, leaveDate: str):
        self.__leaveDate = leaveDate

    @property
    def employee31(self):
        return self.__employee31
    @employee31.setter
    def employee31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_LeaveTaken__employee31", None)
        self.__employee31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "leaveTaken30"):
                    opp_val = getattr(item, "leaveTaken30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "leaveTaken30"):
                    opp_val = getattr(item, "leaveTaken30", None)
                    
                    if opp_val is None:
                        setattr(item, "leaveTaken30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Class_Diagram_for_Proposed_system_WorkingShifts:

    def __init__(self, id: str, startingTime: str, endingTime: str, empId: str, employee20: "Class_Diagram_for_Proposed_system_Employee" = None):
        self.id = id
        self.startingTime = startingTime
        self.endingTime = endingTime
        self.empId = empId
        self.employee20 = employee20
        
        pass
    @property
    def endingTime(self):
        return self.__endingTime
    @endingTime.setter
    def endingTime(self, endingTime: str):
        self.__endingTime = endingTime

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def empId(self):
        return self.__empId
    @empId.setter
    def empId(self, empId: str):
        self.__empId = empId

    @property
    def startingTime(self):
        return self.__startingTime
    @startingTime.setter
    def startingTime(self, startingTime: str):
        self.__startingTime = startingTime

    @property
    def employee20(self):
        return self.__employee20
    @employee20.setter
    def employee20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_WorkingShifts__employee20", None)
        self.__employee20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workingShifts21"):
                opp_val = getattr(old_value, "workingShifts21", None)
                if opp_val == self:
                    setattr(old_value, "workingShifts21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workingShifts21"):
                opp_val = getattr(value, "workingShifts21", None)
                setattr(value, "workingShifts21", self)



class Class_Diagram_for_Proposed_system_Role:

    def __init__(self, id: str, roleName: str, description: str, user43: "Class_Diagram_for_Proposed_system_User" = None):
        self.id = id
        self.roleName = roleName
        self.description = description
        self.user43 = user43
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def roleName(self):
        return self.__roleName
    @roleName.setter
    def roleName(self, roleName: str):
        self.__roleName = roleName

    @property
    def user43(self):
        return self.__user43
    @user43.setter
    def user43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Role__user43", None)
        self.__user43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role42"):
                opp_val = getattr(old_value, "role42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role42"):
                opp_val = getattr(value, "role42", None)
                if opp_val is None:
                    setattr(value, "role42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Class_Diagram_for_Proposed_system_User:

    def __init__(self, id: str, firstNAme: str, LastName: str, roleId: int, employee41: "Class_Diagram_for_Proposed_system_Employee" = None, role42: set["Class_Diagram_for_Proposed_system_Role"] = None):
        self.id = id
        self.firstNAme = firstNAme
        self.LastName = LastName
        self.roleId = roleId
        self.employee41 = employee41
        self.role42 = role42 if role42 is not None else set()
        
        pass
    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def roleId(self):
        return self.__roleId
    @roleId.setter
    def roleId(self, roleId: int):
        self.__roleId = roleId

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def firstNAme(self):
        return self.__firstNAme
    @firstNAme.setter
    def firstNAme(self, firstNAme: str):
        self.__firstNAme = firstNAme

    @property
    def role42(self):
        return self.__role42
    @role42.setter
    def role42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_User__role42", None)
        self.__role42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user43"):
                    opp_val = getattr(item, "user43", None)
                    
                    if opp_val == self:
                        setattr(item, "user43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user43"):
                    opp_val = getattr(item, "user43", None)
                    
                    setattr(item, "user43", self)
                    

    @property
    def employee41(self):
        return self.__employee41
    @employee41.setter
    def employee41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_User__employee41", None)
        self.__employee41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user40"):
                opp_val = getattr(old_value, "user40", None)
                if opp_val == self:
                    setattr(old_value, "user40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user40"):
                opp_val = getattr(value, "user40", None)
                setattr(value, "user40", self)



class Class_Diagram_for_Proposed_system_Employee:

    def __init__(self, id: int, gender: str, NIC: str, address: str, deptId: int, postID: int, shiftId: int, userId: int, mobile: str, phone: str, workingShifts21: "Class_Diagram_for_Proposed_system_WorkingShifts" = None, department22: "Class_Diagram_for_Proposed_system_Department" = None, leaveTaken30: set["Class_Diagram_for_Proposed_system_LeaveTaken"] = None, post34: set["Class_Diagram_for_Proposed_system_Post"] = None, attendance37: set["Class_Diagram_for_Proposed_system_Attendance"] = None, leavesAllocated38: "Class_Diagram_for_Proposed_system_LeavesAllocated" = None, user40: "Class_Diagram_for_Proposed_system_User" = None, overtimeRequests50: "Class_Diagram_for_Proposed_system_overtimeRequests" = None):
        self.id = id
        self.gender = gender
        self.NIC = NIC
        self.address = address
        self.deptId = deptId
        self.postID = postID
        self.shiftId = shiftId
        self.userId = userId
        self.mobile = mobile
        self.phone = phone
        self.workingShifts21 = workingShifts21
        self.department22 = department22
        self.leaveTaken30 = leaveTaken30 if leaveTaken30 is not None else set()
        self.post34 = post34 if post34 is not None else set()
        self.attendance37 = attendance37 if attendance37 is not None else set()
        self.leavesAllocated38 = leavesAllocated38
        self.user40 = user40
        self.overtimeRequests50 = overtimeRequests50
        
        pass
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def mobile(self):
        return self.__mobile
    @mobile.setter
    def mobile(self, mobile: str):
        self.__mobile = mobile

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def shiftId(self):
        return self.__shiftId
    @shiftId.setter
    def shiftId(self, shiftId: int):
        self.__shiftId = shiftId

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def deptId(self):
        return self.__deptId
    @deptId.setter
    def deptId(self, deptId: int):
        self.__deptId = deptId

    @property
    def postID(self):
        return self.__postID
    @postID.setter
    def postID(self, postID: int):
        self.__postID = postID

    @property
    def NIC(self):
        return self.__NIC
    @NIC.setter
    def NIC(self, NIC: str):
        self.__NIC = NIC

    @property
    def workingShifts21(self):
        return self.__workingShifts21
    @workingShifts21.setter
    def workingShifts21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__workingShifts21", None)
        self.__workingShifts21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee20"):
                opp_val = getattr(old_value, "employee20", None)
                if opp_val == self:
                    setattr(old_value, "employee20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee20"):
                opp_val = getattr(value, "employee20", None)
                setattr(value, "employee20", self)

    @property
    def user40(self):
        return self.__user40
    @user40.setter
    def user40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__user40", None)
        self.__user40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee41"):
                opp_val = getattr(old_value, "employee41", None)
                if opp_val == self:
                    setattr(old_value, "employee41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee41"):
                opp_val = getattr(value, "employee41", None)
                setattr(value, "employee41", self)

    @property
    def attendance37(self):
        return self.__attendance37
    @attendance37.setter
    def attendance37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__attendance37", None)
        self.__attendance37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee36"):
                    opp_val = getattr(item, "employee36", None)
                    
                    if opp_val == self:
                        setattr(item, "employee36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee36"):
                    opp_val = getattr(item, "employee36", None)
                    
                    setattr(item, "employee36", self)
                    

    @property
    def post34(self):
        return self.__post34
    @post34.setter
    def post34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__post34", None)
        self.__post34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee35"):
                    opp_val = getattr(item, "employee35", None)
                    
                    if opp_val == self:
                        setattr(item, "employee35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee35"):
                    opp_val = getattr(item, "employee35", None)
                    
                    setattr(item, "employee35", self)
                    

    @property
    def leaveTaken30(self):
        return self.__leaveTaken30
    @leaveTaken30.setter
    def leaveTaken30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__leaveTaken30", None)
        self.__leaveTaken30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee31"):
                    opp_val = getattr(item, "employee31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee31"):
                    opp_val = getattr(item, "employee31", None)
                    
                    if opp_val is None:
                        setattr(item, "employee31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def overtimeRequests50(self):
        return self.__overtimeRequests50
    @overtimeRequests50.setter
    def overtimeRequests50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__overtimeRequests50", None)
        self.__overtimeRequests50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee51"):
                opp_val = getattr(old_value, "employee51", None)
                if opp_val == self:
                    setattr(old_value, "employee51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee51"):
                opp_val = getattr(value, "employee51", None)
                setattr(value, "employee51", self)

    @property
    def leavesAllocated38(self):
        return self.__leavesAllocated38
    @leavesAllocated38.setter
    def leavesAllocated38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__leavesAllocated38", None)
        self.__leavesAllocated38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee39"):
                opp_val = getattr(old_value, "employee39", None)
                if opp_val == self:
                    setattr(old_value, "employee39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee39"):
                opp_val = getattr(value, "employee39", None)
                setattr(value, "employee39", self)

    @property
    def department22(self):
        return self.__department22
    @department22.setter
    def department22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class_Diagram_for_Proposed_system_Employee__department22", None)
        self.__department22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee23"):
                opp_val = getattr(old_value, "employee23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee23"):
                opp_val = getattr(value, "employee23", None)
                if opp_val is None:
                    setattr(value, "employee23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Clark1_Actor1:

    pass
