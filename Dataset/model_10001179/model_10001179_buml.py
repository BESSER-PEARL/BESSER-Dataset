####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Clark1_Actor = Class(name="Clark1_Actor")
Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase")
Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase")
Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase")
Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase")
Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase")
Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase")
Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase")
Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase")
Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase")
Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase")
Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase")
Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase")
Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase")
Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase")
Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase")
Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase")
Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase")
Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase")
Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase")
Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase")
Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase")
Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase = Class(name="Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase")
Manager_Actor = Class(name="Manager_Actor")
Clark1_Actor1 = Class(name="Clark1_Actor1")
Class_Diagram_for_Proposed_system_Employee = Class(name="Class_Diagram_for_Proposed_system_Employee")
Class_Diagram_for_Proposed_system_User = Class(name="Class_Diagram_for_Proposed_system_User")
Class_Diagram_for_Proposed_system_Role = Class(name="Class_Diagram_for_Proposed_system_Role")
Class_Diagram_for_Proposed_system_WorkingShifts = Class(name="Class_Diagram_for_Proposed_system_WorkingShifts")
Class_Diagram_for_Proposed_system_LeaveTaken = Class(name="Class_Diagram_for_Proposed_system_LeaveTaken")
Class_Diagram_for_Proposed_system_Department = Class(name="Class_Diagram_for_Proposed_system_Department")
Class_Diagram_for_Proposed_system_Salary = Class(name="Class_Diagram_for_Proposed_system_Salary")
Class_Diagram_for_Proposed_system_Allowances = Class(name="Class_Diagram_for_Proposed_system_Allowances")
Class_Diagram_for_Proposed_system_Deductions = Class(name="Class_Diagram_for_Proposed_system_Deductions")
Class_Diagram_for_Proposed_system_Advances = Class(name="Class_Diagram_for_Proposed_system_Advances")
Class_Diagram_for_Proposed_system_Post = Class(name="Class_Diagram_for_Proposed_system_Post")
Class_Diagram_for_Proposed_system_Attendance = Class(name="Class_Diagram_for_Proposed_system_Attendance")
Class_Diagram_for_Proposed_system_LeavesAllocated = Class(name="Class_Diagram_for_Proposed_system_LeavesAllocated")
Class_Diagram_for_Proposed_system_Events = Class(name="Class_Diagram_for_Proposed_system_Events")
Class_Diagram_for_Proposed_system_EPF = Class(name="Class_Diagram_for_Proposed_system_EPF")
Class_Diagram_for_Proposed_system_ETF = Class(name="Class_Diagram_for_Proposed_system_ETF")
Class_Diagram_for_Proposed_system_Calender = Class(name="Class_Diagram_for_Proposed_system_Calender")
Class_Diagram_for_Proposed_system_overtimeRequests = Class(name="Class_Diagram_for_Proposed_system_overtimeRequests")

# Clark1_Actor class attributes and methods

# Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase class attributes and methods

# Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase class attributes and methods

# Manager_Actor class attributes and methods

# Clark1_Actor1 class attributes and methods

# Class_Diagram_for_Proposed_system_Employee class attributes and methods
Class_Diagram_for_Proposed_system_Employee_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Proposed_system_Employee_gender: Property = Property(name="gender", type=StringType)
Class_Diagram_for_Proposed_system_Employee_NIC: Property = Property(name="NIC", type=StringType)
Class_Diagram_for_Proposed_system_Employee_address: Property = Property(name="address", type=StringType)
Class_Diagram_for_Proposed_system_Employee_deptId: Property = Property(name="deptId", type=IntegerType)
Class_Diagram_for_Proposed_system_Employee_postID: Property = Property(name="postID", type=IntegerType)
Class_Diagram_for_Proposed_system_Employee_shiftId: Property = Property(name="shiftId", type=IntegerType)
Class_Diagram_for_Proposed_system_Employee_userId: Property = Property(name="userId", type=IntegerType)
Class_Diagram_for_Proposed_system_Employee_mobile: Property = Property(name="mobile", type=StringType)
Class_Diagram_for_Proposed_system_Employee_phone: Property = Property(name="phone", type=StringType)
Class_Diagram_for_Proposed_system_Employee.attributes={Class_Diagram_for_Proposed_system_Employee_phone, Class_Diagram_for_Proposed_system_Employee_NIC, Class_Diagram_for_Proposed_system_Employee_gender, Class_Diagram_for_Proposed_system_Employee_shiftId, Class_Diagram_for_Proposed_system_Employee_deptId, Class_Diagram_for_Proposed_system_Employee_id, Class_Diagram_for_Proposed_system_Employee_postID, Class_Diagram_for_Proposed_system_Employee_address, Class_Diagram_for_Proposed_system_Employee_userId, Class_Diagram_for_Proposed_system_Employee_mobile}

# Class_Diagram_for_Proposed_system_User class attributes and methods
Class_Diagram_for_Proposed_system_User_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_User_firstNAme: Property = Property(name="firstNAme", type=StringType)
Class_Diagram_for_Proposed_system_User_LastName: Property = Property(name="LastName", type=StringType)
Class_Diagram_for_Proposed_system_User_roleId: Property = Property(name="roleId", type=IntegerType)
Class_Diagram_for_Proposed_system_User.attributes={Class_Diagram_for_Proposed_system_User_roleId, Class_Diagram_for_Proposed_system_User_LastName, Class_Diagram_for_Proposed_system_User_firstNAme, Class_Diagram_for_Proposed_system_User_id}

# Class_Diagram_for_Proposed_system_Role class attributes and methods
Class_Diagram_for_Proposed_system_Role_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Role_roleName: Property = Property(name="roleName", type=StringType)
Class_Diagram_for_Proposed_system_Role_description: Property = Property(name="description", type=StringType)
Class_Diagram_for_Proposed_system_Role.attributes={Class_Diagram_for_Proposed_system_Role_id, Class_Diagram_for_Proposed_system_Role_description, Class_Diagram_for_Proposed_system_Role_roleName}

# Class_Diagram_for_Proposed_system_WorkingShifts class attributes and methods
Class_Diagram_for_Proposed_system_WorkingShifts_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_WorkingShifts_startingTime: Property = Property(name="startingTime", type=StringType)
Class_Diagram_for_Proposed_system_WorkingShifts_endingTime: Property = Property(name="endingTime", type=StringType)
Class_Diagram_for_Proposed_system_WorkingShifts_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_WorkingShifts.attributes={Class_Diagram_for_Proposed_system_WorkingShifts_endingTime, Class_Diagram_for_Proposed_system_WorkingShifts_startingTime, Class_Diagram_for_Proposed_system_WorkingShifts_empId, Class_Diagram_for_Proposed_system_WorkingShifts_id}

# Class_Diagram_for_Proposed_system_LeaveTaken class attributes and methods
Class_Diagram_for_Proposed_system_LeaveTaken_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_LeaveTaken_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_LeaveTaken_leaveType: Property = Property(name="leaveType", type=StringType)
Class_Diagram_for_Proposed_system_LeaveTaken_leaveDate: Property = Property(name="leaveDate", type=StringType)
Class_Diagram_for_Proposed_system_LeaveTaken_attribute5: Property = Property(name="attribute5", type=StringType)
Class_Diagram_for_Proposed_system_LeaveTaken.attributes={Class_Diagram_for_Proposed_system_LeaveTaken_id, Class_Diagram_for_Proposed_system_LeaveTaken_empId, Class_Diagram_for_Proposed_system_LeaveTaken_leaveType, Class_Diagram_for_Proposed_system_LeaveTaken_leaveDate, Class_Diagram_for_Proposed_system_LeaveTaken_attribute5}

# Class_Diagram_for_Proposed_system_Department class attributes and methods
Class_Diagram_for_Proposed_system_Department_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Department_name: Property = Property(name="name", type=StringType)
Class_Diagram_for_Proposed_system_Department_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_Department.attributes={Class_Diagram_for_Proposed_system_Department_empId, Class_Diagram_for_Proposed_system_Department_id, Class_Diagram_for_Proposed_system_Department_name}

# Class_Diagram_for_Proposed_system_Salary class attributes and methods
Class_Diagram_for_Proposed_system_Salary_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Salary_payDate: Property = Property(name="payDate", type=StringType)
Class_Diagram_for_Proposed_system_Salary_basicPay: Property = Property(name="basicPay", type=StringType)
Class_Diagram_for_Proposed_system_Salary_allowances: Property = Property(name="allowances", type=StringType)
Class_Diagram_for_Proposed_system_Salary_deductions: Property = Property(name="deductions", type=StringType)
Class_Diagram_for_Proposed_system_Salary_advances: Property = Property(name="advances", type=StringType)
Class_Diagram_for_Proposed_system_Salary_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_Salary_overtimes: Property = Property(name="overtimes", type=StringType)
Class_Diagram_for_Proposed_system_Salary_EPF: Property = Property(name="EPF", type=StringType)
Class_Diagram_for_Proposed_system_Salary_ETF: Property = Property(name="ETF", type=StringType)
Class_Diagram_for_Proposed_system_Salary.attributes={Class_Diagram_for_Proposed_system_Salary_payDate, Class_Diagram_for_Proposed_system_Salary_empId, Class_Diagram_for_Proposed_system_Salary_id, Class_Diagram_for_Proposed_system_Salary_ETF, Class_Diagram_for_Proposed_system_Salary_allowances, Class_Diagram_for_Proposed_system_Salary_basicPay, Class_Diagram_for_Proposed_system_Salary_overtimes, Class_Diagram_for_Proposed_system_Salary_advances, Class_Diagram_for_Proposed_system_Salary_EPF, Class_Diagram_for_Proposed_system_Salary_deductions}

# Class_Diagram_for_Proposed_system_Allowances class attributes and methods
Class_Diagram_for_Proposed_system_Allowances_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Allowances_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Proposed_system_Allowances_allowanceType: Property = Property(name="allowanceType", type=StringType)
Class_Diagram_for_Proposed_system_Allowances_issueDate: Property = Property(name="issueDate", type=StringType)
Class_Diagram_for_Proposed_system_Allowances_salaryId: Property = Property(name="salaryId", type=StringType)
Class_Diagram_for_Proposed_system_Allowances.attributes={Class_Diagram_for_Proposed_system_Allowances_amount, Class_Diagram_for_Proposed_system_Allowances_salaryId, Class_Diagram_for_Proposed_system_Allowances_id, Class_Diagram_for_Proposed_system_Allowances_allowanceType, Class_Diagram_for_Proposed_system_Allowances_issueDate}

# Class_Diagram_for_Proposed_system_Deductions class attributes and methods
Class_Diagram_for_Proposed_system_Deductions_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Deductions_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Proposed_system_Deductions_deductDate: Property = Property(name="deductDate", type=StringType)
Class_Diagram_for_Proposed_system_Deductions_deducType: Property = Property(name="deducType", type=StringType)
Class_Diagram_for_Proposed_system_Deductions_salaryId: Property = Property(name="salaryId", type=StringType)
Class_Diagram_for_Proposed_system_Deductions.attributes={Class_Diagram_for_Proposed_system_Deductions_deducType, Class_Diagram_for_Proposed_system_Deductions_amount, Class_Diagram_for_Proposed_system_Deductions_id, Class_Diagram_for_Proposed_system_Deductions_deductDate, Class_Diagram_for_Proposed_system_Deductions_salaryId}

# Class_Diagram_for_Proposed_system_Advances class attributes and methods
Class_Diagram_for_Proposed_system_Advances_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Advances_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Proposed_system_Advances_issueDate: Property = Property(name="issueDate", type=StringType)
Class_Diagram_for_Proposed_system_Advances_installments: Property = Property(name="installments", type=StringType)
Class_Diagram_for_Proposed_system_Advances_salaryId: Property = Property(name="salaryId", type=StringType)
Class_Diagram_for_Proposed_system_Advances.attributes={Class_Diagram_for_Proposed_system_Advances_salaryId, Class_Diagram_for_Proposed_system_Advances_amount, Class_Diagram_for_Proposed_system_Advances_installments, Class_Diagram_for_Proposed_system_Advances_issueDate, Class_Diagram_for_Proposed_system_Advances_id}

# Class_Diagram_for_Proposed_system_Post class attributes and methods
Class_Diagram_for_Proposed_system_Post_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Post_name: Property = Property(name="name", type=StringType)
Class_Diagram_for_Proposed_system_Post_deptId: Property = Property(name="deptId", type=StringType)
Class_Diagram_for_Proposed_system_Post_leavesEntitled: Property = Property(name="leavesEntitled", type=StringType)
Class_Diagram_for_Proposed_system_Post_attribute: Property = Property(name="attribute", type=StringType)
Class_Diagram_for_Proposed_system_Post.attributes={Class_Diagram_for_Proposed_system_Post_name, Class_Diagram_for_Proposed_system_Post_id, Class_Diagram_for_Proposed_system_Post_leavesEntitled, Class_Diagram_for_Proposed_system_Post_deptId, Class_Diagram_for_Proposed_system_Post_attribute}

# Class_Diagram_for_Proposed_system_Attendance class attributes and methods
Class_Diagram_for_Proposed_system_Attendance_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Attendance_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_Attendance_clock_in: Property = Property(name="clock_in", type=StringType)
Class_Diagram_for_Proposed_system_Attendance_clock_out: Property = Property(name="clock_out", type=StringType)
Class_Diagram_for_Proposed_system_Attendance_date: Property = Property(name="date", type=StringType)
Class_Diagram_for_Proposed_system_Attendance_attribute: Property = Property(name="attribute", type=StringType)
Class_Diagram_for_Proposed_system_Attendance.attributes={Class_Diagram_for_Proposed_system_Attendance_date, Class_Diagram_for_Proposed_system_Attendance_attribute, Class_Diagram_for_Proposed_system_Attendance_empId, Class_Diagram_for_Proposed_system_Attendance_id, Class_Diagram_for_Proposed_system_Attendance_clock_out, Class_Diagram_for_Proposed_system_Attendance_clock_in}

# Class_Diagram_for_Proposed_system_LeavesAllocated class attributes and methods
Class_Diagram_for_Proposed_system_LeavesAllocated_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_LeavesAllocated_empId: Property = Property(name="empId", type=StringType)
Class_Diagram_for_Proposed_system_LeavesAllocated_leaveType: Property = Property(name="leaveType", type=StringType)
Class_Diagram_for_Proposed_system_LeavesAllocated_noOfLeaves: Property = Property(name="noOfLeaves", type=StringType)
Class_Diagram_for_Proposed_system_LeavesAllocated.attributes={Class_Diagram_for_Proposed_system_LeavesAllocated_id, Class_Diagram_for_Proposed_system_LeavesAllocated_leaveType, Class_Diagram_for_Proposed_system_LeavesAllocated_empId, Class_Diagram_for_Proposed_system_LeavesAllocated_noOfLeaves}

# Class_Diagram_for_Proposed_system_Events class attributes and methods
Class_Diagram_for_Proposed_system_Events_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Events_type: Property = Property(name="type", type=StringType)
Class_Diagram_for_Proposed_system_Events.attributes={Class_Diagram_for_Proposed_system_Events_type, Class_Diagram_for_Proposed_system_Events_id}

# Class_Diagram_for_Proposed_system_EPF class attributes and methods
Class_Diagram_for_Proposed_system_EPF_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_EPF_precentage: Property = Property(name="precentage", type=StringType)
Class_Diagram_for_Proposed_system_EPF.attributes={Class_Diagram_for_Proposed_system_EPF_precentage, Class_Diagram_for_Proposed_system_EPF_id}

# Class_Diagram_for_Proposed_system_ETF class attributes and methods
Class_Diagram_for_Proposed_system_ETF_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_ETF_precentage: Property = Property(name="precentage", type=StringType)
Class_Diagram_for_Proposed_system_ETF.attributes={Class_Diagram_for_Proposed_system_ETF_id, Class_Diagram_for_Proposed_system_ETF_precentage}

# Class_Diagram_for_Proposed_system_Calender class attributes and methods
Class_Diagram_for_Proposed_system_Calender_author_id: Property = Property(name="author_id", type=StringType)
Class_Diagram_for_Proposed_system_Calender_depid: Property = Property(name="depid", type=StringType)
Class_Diagram_for_Proposed_system_Calender_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_Calender_eventType: Property = Property(name="eventType", type=StringType)
Class_Diagram_for_Proposed_system_Calender.attributes={Class_Diagram_for_Proposed_system_Calender_id, Class_Diagram_for_Proposed_system_Calender_eventType, Class_Diagram_for_Proposed_system_Calender_author_id, Class_Diagram_for_Proposed_system_Calender_depid}

# Class_Diagram_for_Proposed_system_overtimeRequests class attributes and methods
Class_Diagram_for_Proposed_system_overtimeRequests_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Proposed_system_overtimeRequests_date: Property = Property(name="date", type=StringType)
Class_Diagram_for_Proposed_system_overtimeRequests_start_time: Property = Property(name="start_time", type=StringType)
Class_Diagram_for_Proposed_system_overtimeRequests_nd_time: Property = Property(name="nd_time", type=StringType)
Class_Diagram_for_Proposed_system_overtimeRequests.attributes={Class_Diagram_for_Proposed_system_overtimeRequests_nd_time, Class_Diagram_for_Proposed_system_overtimeRequests_date, Class_Diagram_for_Proposed_system_overtimeRequests_start_time, Class_Diagram_for_Proposed_system_overtimeRequests_id}

# Relationships
Request_Loan_and_advances_Actor: BinaryAssociation = BinaryAssociation(
    name="Request_Loan_and_advances_Actor",
    ends={
        Property(name="actor0", type=Clark1_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="request_Loan_and_advances1", type=Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
generate_reports_from_excel_Admin: BinaryAssociation = BinaryAssociation(
    name="generate_reports_from_excel_Admin",
    ends={
        Property(name="admin2", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_reports_from_excel3", type=Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
put_company_notices_Manager: BinaryAssociation = BinaryAssociation(
    name="put_company_notices_Manager",
    ends={
        Property(name="manager4", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="put_company_notices5", type=Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase26", type=Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor7", type=Clark1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase5",
    ends={
        Property(name="useCase58", type=Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor9", type=Clark1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Approve_Employee_Pay_sheets: BinaryAssociation = BinaryAssociation(
    name="Admin_Approve_Employee_Pay_sheets",
    ends={
        Property(name="approve_Employee_Pay_sheets10", type=Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Set_Leave_status: BinaryAssociation = BinaryAssociation(
    name="Admin_Set_Leave_status",
    ends={
        Property(name="set_Leave_status12", type=Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_Add_Employee_profile: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_Employee_profile",
    ends={
        Property(name="add_Employee_profile14", type=Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark15", type=Clark1_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Clark_View_Employee_profiles: BinaryAssociation = BinaryAssociation(
    name="Clark_View_Employee_profiles",
    ends={
        Property(name="view_Employee_profiles16", type=Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark17", type=Clark1_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Clark1_Salary_calculation: BinaryAssociation = BinaryAssociation(
    name="Clark1_Salary_calculation",
    ends={
        Property(name="salary_calculation18", type=Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark119", type=Clark1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
WorkingShifts_Employee: BinaryAssociation = BinaryAssociation(
    name="WorkingShifts_Employee",
    ends={
        Property(name="employee20", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="workingShifts21", type=Class_Diagram_for_Proposed_system_WorkingShifts, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Department: BinaryAssociation = BinaryAssociation(
    name="Employee_Department",
    ends={
        Property(name="department22", type=Class_Diagram_for_Proposed_system_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employee23", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
Allowances_Salary: BinaryAssociation = BinaryAssociation(
    name="Allowances_Salary",
    ends={
        Property(name="salary24", type=Class_Diagram_for_Proposed_system_Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="allowances225", type=Class_Diagram_for_Proposed_system_Allowances, multiplicity=Multiplicity(0, 1))
    }
)
Deductions_Salary: BinaryAssociation = BinaryAssociation(
    name="Deductions_Salary",
    ends={
        Property(name="salary26", type=Class_Diagram_for_Proposed_system_Salary, multiplicity=Multiplicity(1, 1)),
        Property(name="deductions227", type=Class_Diagram_for_Proposed_system_Deductions, multiplicity=Multiplicity(0, 1))
    }
)
Advances_Salary: BinaryAssociation = BinaryAssociation(
    name="Advances_Salary",
    ends={
        Property(name="salary28", type=Class_Diagram_for_Proposed_system_Salary, multiplicity=Multiplicity(1, 9999)),
        Property(name="advances229", type=Class_Diagram_for_Proposed_system_Advances, multiplicity=Multiplicity(0, 1))
    }
)
Employee_LeaveTaken: BinaryAssociation = BinaryAssociation(
    name="Employee_LeaveTaken",
    ends={
        Property(name="leaveTaken30", type=Class_Diagram_for_Proposed_system_LeaveTaken, multiplicity=Multiplicity(1, 9999)),
        Property(name="employee31", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Department_Post: BinaryAssociation = BinaryAssociation(
    name="Department_Post",
    ends={
        Property(name="post32", type=Class_Diagram_for_Proposed_system_Post, multiplicity=Multiplicity(1, 9999)),
        Property(name="department33", type=Class_Diagram_for_Proposed_system_Department, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Post: BinaryAssociation = BinaryAssociation(
    name="Employee_Post",
    ends={
        Property(name="post34", type=Class_Diagram_for_Proposed_system_Post, multiplicity=Multiplicity(1, 9999)),
        Property(name="employee35", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Attendance_Employee: BinaryAssociation = BinaryAssociation(
    name="Attendance_Employee",
    ends={
        Property(name="employee36", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="attendance37", type=Class_Diagram_for_Proposed_system_Attendance, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_LeavesAllocated: BinaryAssociation = BinaryAssociation(
    name="Employee_LeavesAllocated",
    ends={
        Property(name="leavesAllocated38", type=Class_Diagram_for_Proposed_system_LeavesAllocated, multiplicity=Multiplicity(0, 1)),
        Property(name="employee39", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_User: BinaryAssociation = BinaryAssociation(
    name="Employee_User",
    ends={
        Property(name="user40", type=Class_Diagram_for_Proposed_system_User, multiplicity=Multiplicity(1, 1)),
        Property(name="employee41", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(1, 1))
    }
)
User_Role: BinaryAssociation = BinaryAssociation(
    name="User_Role",
    ends={
        Property(name="role42", type=Class_Diagram_for_Proposed_system_Role, multiplicity=Multiplicity(1, 9999)),
        Property(name="user43", type=Class_Diagram_for_Proposed_system_User, multiplicity=Multiplicity(1, 1))
    }
)
LeavesAllocated_EPF: BinaryAssociation = BinaryAssociation(
    name="LeavesAllocated_EPF",
    ends={
        Property(name="ePF44", type=Class_Diagram_for_Proposed_system_EPF, multiplicity=Multiplicity(1, 9999)),
        Property(name="leavesAllocated45", type=Class_Diagram_for_Proposed_system_LeavesAllocated, multiplicity=Multiplicity(1, 1))
    }
)
LeavesAllocated_ETF: BinaryAssociation = BinaryAssociation(
    name="LeavesAllocated_ETF",
    ends={
        Property(name="eTF46", type=Class_Diagram_for_Proposed_system_ETF, multiplicity=Multiplicity(0, 1)),
        Property(name="leavesAllocated47", type=Class_Diagram_for_Proposed_system_LeavesAllocated, multiplicity=Multiplicity(1, 1))
    }
)
Calender_Events: BinaryAssociation = BinaryAssociation(
    name="Calender_Events",
    ends={
        Property(name="events48", type=Class_Diagram_for_Proposed_system_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="calender49", type=Class_Diagram_for_Proposed_system_Calender, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_overtimeRequests: BinaryAssociation = BinaryAssociation(
    name="Employee_overtimeRequests",
    ends={
        Property(name="overtimeRequests50", type=Class_Diagram_for_Proposed_system_overtimeRequests, multiplicity=Multiplicity(0, 1)),
        Property(name="employee51", type=Class_Diagram_for_Proposed_system_Employee, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8e77e7d1_178a_48ea_974a_eb451fdc17b7",
    types={Clark1_Actor, Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase, Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase, Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase, Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase, Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase, Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase, Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase, Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase, Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase, Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase, Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase, Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase, Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase, Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase, Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase, Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase, Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase, Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase, Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase, Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase, Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase, Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase, Manager_Actor, Clark1_Actor1, Class_Diagram_for_Proposed_system_Employee, Class_Diagram_for_Proposed_system_User, Class_Diagram_for_Proposed_system_Role, Class_Diagram_for_Proposed_system_WorkingShifts, Class_Diagram_for_Proposed_system_LeaveTaken, Class_Diagram_for_Proposed_system_Department, Class_Diagram_for_Proposed_system_Salary, Class_Diagram_for_Proposed_system_Allowances, Class_Diagram_for_Proposed_system_Deductions, Class_Diagram_for_Proposed_system_Advances, Class_Diagram_for_Proposed_system_Post, Class_Diagram_for_Proposed_system_Attendance, Class_Diagram_for_Proposed_system_LeavesAllocated, Class_Diagram_for_Proposed_system_Events, Class_Diagram_for_Proposed_system_EPF, Class_Diagram_for_Proposed_system_ETF, Class_Diagram_for_Proposed_system_Calender, Class_Diagram_for_Proposed_system_overtimeRequests},
    associations={Request_Loan_and_advances_Actor, generate_reports_from_excel_Admin, put_company_notices_Manager, Actor_UseCase2, Actor_UseCase5, Admin_Approve_Employee_Pay_sheets, Admin_Set_Leave_status, Clark_Add_Employee_profile, Clark_View_Employee_profiles, Clark1_Salary_calculation, WorkingShifts_Employee, Employee_Department, Allowances_Salary, Deductions_Salary, Advances_Salary, Employee_LeaveTaken, Department_Post, Employee_Post, Attendance_Employee, Employee_LeavesAllocated, Employee_User, User_Role, LeavesAllocated_EPF, LeavesAllocated_ETF, Calender_Events, Employee_overtimeRequests},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)