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

# Enumerations
ot_Type: Enumeration = Enumeration(
    name="ot_Type",
    literals={
            
    }
)

date: Enumeration = Enumeration(
    name="date",
    literals={
            
    }
)

# Classes
Employee_Actor = Class(name="Employee_Actor")
Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase")
Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase")
Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase")
Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase")
Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase")
Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase")
Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase")
Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase")
Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase")
Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase")
Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1 = Class(name="Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1")
Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase")
Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase")
Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase")
Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase")
Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase")
Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase = Class(name="Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Clark_Actor = Class(name="Clark_Actor")
Interface_Interface = Class(name="Interface_Interface")
Package_Allowance = Class(name="Package_Allowance")
Package_Attendance = Class(name="Package_Attendance")
Package_DeuctionTypes = Class(name="Package_DeuctionTypes")
Package_AllowanceTypes = Class(name="Package_AllowanceTypes")
Package_Deductions = Class(name="Package_Deductions")
Package_Departments = Class(name="Package_Departments")
Package_Shifts = Class(name="Package_Shifts")
Package_Posts = Class(name="Package_Posts")
Package_Employee = Class(name="Package_Employee")
Package_EmployeeParoll = Class(name="Package_EmployeeParoll")
Package_EmployeeSalary = Class(name="Package_EmployeeSalary")
Package_EPF = Class(name="Package_EPF")
Package_Event = Class(name="Package_Event")
Package_Leave_Taken = Class(name="Package_Leave_Taken")
Package_LeaveProfiles = Class(name="Package_LeaveProfiles")
Package_OT_Requests = Class(name="Package_OT_Requests")
Package_User_groups = Class(name="Package_User_groups")
Package_Users = Class(name="Package_Users")
Package_UserUpdates = Class(name="Package_UserUpdates")
Package_Advances = Class(name="Package_Advances")
Package_Messages = Class(name="Package_Messages")
Package_User_Permissions = Class(name="Package_User_Permissions")
Package_ETF = Class(name="Package_ETF")
Class_Diagram_for_Propsed_System_Allowance = Class(name="Class_Diagram_for_Propsed_System_Allowance")
Class_Diagram_for_Propsed_System_Attendance = Class(name="Class_Diagram_for_Propsed_System_Attendance")
Class_Diagram_for_Propsed_System_DeuctionTypes = Class(name="Class_Diagram_for_Propsed_System_DeuctionTypes")
Class_Diagram_for_Propsed_System_AllowanceTypes = Class(name="Class_Diagram_for_Propsed_System_AllowanceTypes")
Class_Diagram_for_Propsed_System_Deductions = Class(name="Class_Diagram_for_Propsed_System_Deductions")
Class_Diagram_for_Propsed_System_Departments = Class(name="Class_Diagram_for_Propsed_System_Departments")
Class_Diagram_for_Propsed_System_Shifts = Class(name="Class_Diagram_for_Propsed_System_Shifts")
Class_Diagram_for_Propsed_System_Posts = Class(name="Class_Diagram_for_Propsed_System_Posts")
Class_Diagram_for_Propsed_System_Employee = Class(name="Class_Diagram_for_Propsed_System_Employee")
Class_Diagram_for_Propsed_System_EmployeeParoll = Class(name="Class_Diagram_for_Propsed_System_EmployeeParoll")
Class_Diagram_for_Propsed_System_EmployeeSalary = Class(name="Class_Diagram_for_Propsed_System_EmployeeSalary")
Class_Diagram_for_Propsed_System_EPF = Class(name="Class_Diagram_for_Propsed_System_EPF")
Class_Diagram_for_Propsed_System_Event = Class(name="Class_Diagram_for_Propsed_System_Event")
Class_Diagram_for_Propsed_System_Leave_Taken = Class(name="Class_Diagram_for_Propsed_System_Leave_Taken")
Class_Diagram_for_Propsed_System_LeaveProfiles = Class(name="Class_Diagram_for_Propsed_System_LeaveProfiles")
Class_Diagram_for_Propsed_System_OT_Requests = Class(name="Class_Diagram_for_Propsed_System_OT_Requests")
Class_Diagram_for_Propsed_System_User_groups = Class(name="Class_Diagram_for_Propsed_System_User_groups")
Class_Diagram_for_Propsed_System_Users = Class(name="Class_Diagram_for_Propsed_System_Users")
Class_Diagram_for_Propsed_System_UserUpdates = Class(name="Class_Diagram_for_Propsed_System_UserUpdates")
Class_Diagram_for_Propsed_System_Advances = Class(name="Class_Diagram_for_Propsed_System_Advances")
Class_Diagram_for_Propsed_System_Messages = Class(name="Class_Diagram_for_Propsed_System_Messages")
Class_Diagram_for_Propsed_System_User_Permissions = Class(name="Class_Diagram_for_Propsed_System_User_Permissions")
Class_Diagram_for_Propsed_System_ETF = Class(name="Class_Diagram_for_Propsed_System_ETF")

# Employee_Actor class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1 class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase class attributes and methods

# Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Clark_Actor class attributes and methods

# Interface_Interface class attributes and methods

# Package_Allowance class attributes and methods
Package_Allowance_id: Property = Property(name="id", type=IntegerType)
Package_Allowance_emp_id: Property = Property(name="emp_id", type=StringType)
Package_Allowance_Effectivedate: Property = Property(name="Effectivedate", type=StringType)
Package_Allowance.attributes={Package_Allowance_id, Package_Allowance_emp_id, Package_Allowance_Effectivedate}

# Package_Attendance class attributes and methods
Package_Attendance_id: Property = Property(name="id", type=IntegerType)
Package_Attendance_timein: Property = Property(name="timein", type=StringType)
Package_Attendance_timeout: Property = Property(name="timeout", type=StringType)
Package_Attendance_empid: Property = Property(name="empid", type=IntegerType)
Package_Attendance.attributes={Package_Attendance_id, Package_Attendance_timein, Package_Attendance_empid, Package_Attendance_timeout}

# Package_DeuctionTypes class attributes and methods

# Package_AllowanceTypes class attributes and methods

# Package_Deductions class attributes and methods
Package_Deductions_attribute: Property = Property(name="attribute", type=StringType)
Package_Deductions_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Deductions.attributes={Package_Deductions_attribute2, Package_Deductions_attribute}

# Package_Departments class attributes and methods
Package_Departments_id: Property = Property(name="id", type=IntegerType)
Package_Departments.attributes={Package_Departments_id}

# Package_Shifts class attributes and methods
Package_Shifts_attribute: Property = Property(name="attribute", type=StringType)
Package_Shifts_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Shifts.attributes={Package_Shifts_attribute2, Package_Shifts_attribute}

# Package_Posts class attributes and methods
Package_Posts_attribute: Property = Property(name="attribute", type=StringType)
Package_Posts_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Posts.attributes={Package_Posts_attribute2, Package_Posts_attribute}

# Package_Employee class attributes and methods
Package_Employee_id: Property = Property(name="id", type=StringType)
Package_Employee_empid: Property = Property(name="empid", type=StringType)
Package_Employee_depid: Property = Property(name="depid", type=IntegerType)
Package_Employee_post: Property = Property(name="post", type=StringType)
Package_Employee_shift: Property = Property(name="shift", type=StringType)
Package_Employee_usergroup: Property = Property(name="usergroup", type=IntegerType)
Package_Employee_leavegroup: Property = Property(name="leavegroup", type=IntegerType)
Package_Employee.attributes={Package_Employee_id, Package_Employee_depid, Package_Employee_shift, Package_Employee_leavegroup, Package_Employee_empid, Package_Employee_post, Package_Employee_usergroup}

# Package_EmployeeParoll class attributes and methods
Package_EmployeeParoll_attribute: Property = Property(name="attribute", type=StringType)
Package_EmployeeParoll_attribute2: Property = Property(name="attribute2", type=StringType)
Package_EmployeeParoll.attributes={Package_EmployeeParoll_attribute2, Package_EmployeeParoll_attribute}

# Package_EmployeeSalary class attributes and methods
Package_EmployeeSalary_attribute: Property = Property(name="attribute", type=StringType)
Package_EmployeeSalary_attribute2: Property = Property(name="attribute2", type=StringType)
Package_EmployeeSalary.attributes={Package_EmployeeSalary_attribute2, Package_EmployeeSalary_attribute}

# Package_EPF class attributes and methods
Package_EPF_id: Property = Property(name="id", type=IntegerType)
Package_EPF_effectve_date: Property = Property(name="effectve_date", type=Package_UserUpdates)
Package_EPF_precentage: Property = Property(name="precentage", type=IntegerType)
Package_EPF.attributes={Package_EPF_precentage, Package_EPF_effectve_date, Package_EPF_id}

# Package_Event class attributes and methods

# Package_Leave_Taken class attributes and methods
Package_Leave_Taken_attribute: Property = Property(name="attribute", type=StringType)
Package_Leave_Taken_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Leave_Taken.attributes={Package_Leave_Taken_attribute2, Package_Leave_Taken_attribute}

# Package_LeaveProfiles class attributes and methods
Package_LeaveProfiles_attribute: Property = Property(name="attribute", type=StringType)
Package_LeaveProfiles_attribute2: Property = Property(name="attribute2", type=StringType)
Package_LeaveProfiles.attributes={Package_LeaveProfiles_attribute, Package_LeaveProfiles_attribute2}

# Package_OT_Requests class attributes and methods
Package_OT_Requests_id: Property = Property(name="id", type=IntegerType)
Package_OT_Requests_OtDay: Property = Property(name="OtDay", type=DateType)
Package_OT_Requests_OTType: Property = Property(name="OTType", type=IntegerType)
Package_OT_Requests_EmpID: Property = Property(name="EmpID", type=IntegerType)
Package_OT_Requests.attributes={Package_OT_Requests_id, Package_OT_Requests_OTType, Package_OT_Requests_OtDay, Package_OT_Requests_EmpID}

# Package_User_groups class attributes and methods
Package_User_groups_attribute: Property = Property(name="attribute", type=StringType)
Package_User_groups_attribute2: Property = Property(name="attribute2", type=StringType)
Package_User_groups_attribute3: Property = Property(name="attribute3", type=StringType)
Package_User_groups.attributes={Package_User_groups_attribute2, Package_User_groups_attribute3, Package_User_groups_attribute}

# Package_Users class attributes and methods
Package_Users_id: Property = Property(name="id", type=IntegerType)
Package_Users_firstname: Property = Property(name="firstname", type=IntegerType)
Package_Users_lastname: Property = Property(name="lastname", type=IntegerType)
Package_Users_email: Property = Property(name="email", type=IntegerType)
Package_Users_password: Property = Property(name="password", type=IntegerType)
Package_Users.attributes={Package_Users_id, Package_Users_password, Package_Users_email, Package_Users_firstname, Package_Users_lastname}

# Package_UserUpdates class attributes and methods

# Package_Advances class attributes and methods

# Package_Messages class attributes and methods

# Package_User_Permissions class attributes and methods
Package_User_Permissions_attribute: Property = Property(name="attribute", type=StringType)
Package_User_Permissions_attribute2: Property = Property(name="attribute2", type=StringType)
Package_User_Permissions.attributes={Package_User_Permissions_attribute2, Package_User_Permissions_attribute}

# Package_ETF class attributes and methods

# Class_Diagram_for_Propsed_System_Allowance class attributes and methods
Class_Diagram_for_Propsed_System_Allowance_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Allowance_emp_id: Property = Property(name="emp_id", type=IntegerType)
Class_Diagram_for_Propsed_System_Allowance_effectivedate: Property = Property(name="effectivedate", type=StringType)
Class_Diagram_for_Propsed_System_Allowance_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Propsed_System_Allowance.attributes={Class_Diagram_for_Propsed_System_Allowance_id, Class_Diagram_for_Propsed_System_Allowance_amount, Class_Diagram_for_Propsed_System_Allowance_emp_id, Class_Diagram_for_Propsed_System_Allowance_effectivedate}

# Class_Diagram_for_Propsed_System_Attendance class attributes and methods
Class_Diagram_for_Propsed_System_Attendance_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Attendance_timein: Property = Property(name="timein", type=StringType)
Class_Diagram_for_Propsed_System_Attendance_timeout: Property = Property(name="timeout", type=StringType)
Class_Diagram_for_Propsed_System_Attendance_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_Attendance.attributes={Class_Diagram_for_Propsed_System_Attendance_timein, Class_Diagram_for_Propsed_System_Attendance_id, Class_Diagram_for_Propsed_System_Attendance_timeout, Class_Diagram_for_Propsed_System_Attendance_empid}

# Class_Diagram_for_Propsed_System_DeuctionTypes class attributes and methods
Class_Diagram_for_Propsed_System_DeuctionTypes_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_DeuctionTypes_type: Property = Property(name="type", type=StringType)
Class_Diagram_for_Propsed_System_DeuctionTypes.attributes={Class_Diagram_for_Propsed_System_DeuctionTypes_type, Class_Diagram_for_Propsed_System_DeuctionTypes_id}

# Class_Diagram_for_Propsed_System_AllowanceTypes class attributes and methods
Class_Diagram_for_Propsed_System_AllowanceTypes_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_AllowanceTypes_type: Property = Property(name="type", type=IntegerType)
Class_Diagram_for_Propsed_System_AllowanceTypes_date_added: Property = Property(name="date_added", type=StringType)
Class_Diagram_for_Propsed_System_AllowanceTypes.attributes={Class_Diagram_for_Propsed_System_AllowanceTypes_type, Class_Diagram_for_Propsed_System_AllowanceTypes_date_added, Class_Diagram_for_Propsed_System_AllowanceTypes_id}

# Class_Diagram_for_Propsed_System_Deductions class attributes and methods
Class_Diagram_for_Propsed_System_Deductions_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Deductions_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Propsed_System_Deductions_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_Deductions.attributes={Class_Diagram_for_Propsed_System_Deductions_id, Class_Diagram_for_Propsed_System_Deductions_empid, Class_Diagram_for_Propsed_System_Deductions_amount}

# Class_Diagram_for_Propsed_System_Departments class attributes and methods
Class_Diagram_for_Propsed_System_Departments_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Departments_depname: Property = Property(name="depname", type=StringType)
Class_Diagram_for_Propsed_System_Departments.attributes={Class_Diagram_for_Propsed_System_Departments_id, Class_Diagram_for_Propsed_System_Departments_depname}

# Class_Diagram_for_Propsed_System_Shifts class attributes and methods
Class_Diagram_for_Propsed_System_Shifts_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Shifts_shiftaname: Property = Property(name="shiftaname", type=StringType)
Class_Diagram_for_Propsed_System_Shifts_starttime: Property = Property(name="starttime", type=StringType)
Class_Diagram_for_Propsed_System_Shifts_endtime: Property = Property(name="endtime", type=StringType)
Class_Diagram_for_Propsed_System_Shifts.attributes={Class_Diagram_for_Propsed_System_Shifts_shiftaname, Class_Diagram_for_Propsed_System_Shifts_starttime, Class_Diagram_for_Propsed_System_Shifts_id, Class_Diagram_for_Propsed_System_Shifts_endtime}

# Class_Diagram_for_Propsed_System_Posts class attributes and methods
Class_Diagram_for_Propsed_System_Posts_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Posts_name: Property = Property(name="name", type=StringType)
Class_Diagram_for_Propsed_System_Posts_department_id: Property = Property(name="department_id", type=IntegerType)
Class_Diagram_for_Propsed_System_Posts.attributes={Class_Diagram_for_Propsed_System_Posts_department_id, Class_Diagram_for_Propsed_System_Posts_id, Class_Diagram_for_Propsed_System_Posts_name}

# Class_Diagram_for_Propsed_System_Employee class attributes and methods
Class_Diagram_for_Propsed_System_Employee_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Propsed_System_Employee_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_depid: Property = Property(name="depid", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_post: Property = Property(name="post", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_shift: Property = Property(name="shift", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_usergroup: Property = Property(name="usergroup", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_leavegroup: Property = Property(name="leavegroup", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_mobile: Property = Property(name="mobile", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee_user_id: Property = Property(name="user_id", type=IntegerType)
Class_Diagram_for_Propsed_System_Employee.attributes={Class_Diagram_for_Propsed_System_Employee_id, Class_Diagram_for_Propsed_System_Employee_leavegroup, Class_Diagram_for_Propsed_System_Employee_empid, Class_Diagram_for_Propsed_System_Employee_depid, Class_Diagram_for_Propsed_System_Employee_usergroup, Class_Diagram_for_Propsed_System_Employee_shift, Class_Diagram_for_Propsed_System_Employee_post, Class_Diagram_for_Propsed_System_Employee_user_id, Class_Diagram_for_Propsed_System_Employee_mobile}

# Class_Diagram_for_Propsed_System_EmployeeParoll class attributes and methods
Class_Diagram_for_Propsed_System_EmployeeParoll_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_EmployeeParoll_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_EmployeeParoll_basicslaray: Property = Property(name="basicslaray", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll_lateamount: Property = Property(name="lateamount", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll_otamount: Property = Property(name="otamount", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll_dotamount: Property = Property(name="dotamount", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll_epf: Property = Property(name="epf", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll_etf: Property = Property(name="etf", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeParoll.attributes={Class_Diagram_for_Propsed_System_EmployeeParoll_dotamount, Class_Diagram_for_Propsed_System_EmployeeParoll_otamount, Class_Diagram_for_Propsed_System_EmployeeParoll_basicslaray, Class_Diagram_for_Propsed_System_EmployeeParoll_lateamount, Class_Diagram_for_Propsed_System_EmployeeParoll_id, Class_Diagram_for_Propsed_System_EmployeeParoll_epf, Class_Diagram_for_Propsed_System_EmployeeParoll_empid, Class_Diagram_for_Propsed_System_EmployeeParoll_etf}

# Class_Diagram_for_Propsed_System_EmployeeSalary class attributes and methods
Class_Diagram_for_Propsed_System_EmployeeSalary_id: Property = Property(name="id", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeSalary_emp_id: Property = Property(name="emp_id", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeSalary_basic_salary: Property = Property(name="basic_salary", type=StringType)
Class_Diagram_for_Propsed_System_EmployeeSalary_allowances: Property = Property(name="allowances", type=BooleanType)
Class_Diagram_for_Propsed_System_EmployeeSalary_deductions: Property = Property(name="deductions", type=BooleanType)
Class_Diagram_for_Propsed_System_EmployeeSalary.attributes={Class_Diagram_for_Propsed_System_EmployeeSalary_id, Class_Diagram_for_Propsed_System_EmployeeSalary_deductions, Class_Diagram_for_Propsed_System_EmployeeSalary_allowances, Class_Diagram_for_Propsed_System_EmployeeSalary_basic_salary, Class_Diagram_for_Propsed_System_EmployeeSalary_emp_id}

# Class_Diagram_for_Propsed_System_EPF class attributes and methods
Class_Diagram_for_Propsed_System_EPF_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_EPF_precentage: Property = Property(name="precentage", type=IntegerType)
Class_Diagram_for_Propsed_System_EPF_effectve_date: Property = Property(name="effectve_date", type=StringType)
Class_Diagram_for_Propsed_System_EPF.attributes={Class_Diagram_for_Propsed_System_EPF_id, Class_Diagram_for_Propsed_System_EPF_effectve_date, Class_Diagram_for_Propsed_System_EPF_precentage}

# Class_Diagram_for_Propsed_System_Event class attributes and methods
Class_Diagram_for_Propsed_System_Event_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Event_eventname: Property = Property(name="eventname", type=StringType)
Class_Diagram_for_Propsed_System_Event_type: Property = Property(name="type", type=IntegerType)
Class_Diagram_for_Propsed_System_Event_date: Property = Property(name="date", type=StringType)
Class_Diagram_for_Propsed_System_Event.attributes={Class_Diagram_for_Propsed_System_Event_date, Class_Diagram_for_Propsed_System_Event_type, Class_Diagram_for_Propsed_System_Event_id, Class_Diagram_for_Propsed_System_Event_eventname}

# Class_Diagram_for_Propsed_System_Leave_Taken class attributes and methods
Class_Diagram_for_Propsed_System_Leave_Taken_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Leave_Taken_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_Leave_Taken_leavetype: Property = Property(name="leavetype", type=IntegerType)
Class_Diagram_for_Propsed_System_Leave_Taken_start_date: Property = Property(name="start_date", type=StringType)
Class_Diagram_for_Propsed_System_Leave_Taken_enddate: Property = Property(name="enddate", type=StringType)
Class_Diagram_for_Propsed_System_Leave_Taken_status: Property = Property(name="status", type=IntegerType)
Class_Diagram_for_Propsed_System_Leave_Taken.attributes={Class_Diagram_for_Propsed_System_Leave_Taken_status, Class_Diagram_for_Propsed_System_Leave_Taken_leavetype, Class_Diagram_for_Propsed_System_Leave_Taken_start_date, Class_Diagram_for_Propsed_System_Leave_Taken_enddate, Class_Diagram_for_Propsed_System_Leave_Taken_empid, Class_Diagram_for_Propsed_System_Leave_Taken_id}

# Class_Diagram_for_Propsed_System_LeaveProfiles class attributes and methods
Class_Diagram_for_Propsed_System_LeaveProfiles_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_LeaveProfiles_name: Property = Property(name="name", type=StringType)
Class_Diagram_for_Propsed_System_LeaveProfiles_casual: Property = Property(name="casual", type=IntegerType)
Class_Diagram_for_Propsed_System_LeaveProfiles_anual: Property = Property(name="anual", type=IntegerType)
Class_Diagram_for_Propsed_System_LeaveProfiles.attributes={Class_Diagram_for_Propsed_System_LeaveProfiles_name, Class_Diagram_for_Propsed_System_LeaveProfiles_id, Class_Diagram_for_Propsed_System_LeaveProfiles_casual, Class_Diagram_for_Propsed_System_LeaveProfiles_anual}

# Class_Diagram_for_Propsed_System_OT_Requests class attributes and methods
Class_Diagram_for_Propsed_System_OT_Requests_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_OT_Requests_OtDay: Property = Property(name="OtDay", type=DateType)
Class_Diagram_for_Propsed_System_OT_Requests_OTType: Property = Property(name="OTType", type=IntegerType)
Class_Diagram_for_Propsed_System_OT_Requests_EmpID: Property = Property(name="EmpID", type=IntegerType)
Class_Diagram_for_Propsed_System_OT_Requests.attributes={Class_Diagram_for_Propsed_System_OT_Requests_OTType, Class_Diagram_for_Propsed_System_OT_Requests_id, Class_Diagram_for_Propsed_System_OT_Requests_OtDay, Class_Diagram_for_Propsed_System_OT_Requests_EmpID}

# Class_Diagram_for_Propsed_System_User_groups class attributes and methods
Class_Diagram_for_Propsed_System_User_groups_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_User_groups_user_group: Property = Property(name="user_group", type=StringType)
Class_Diagram_for_Propsed_System_User_groups.attributes={Class_Diagram_for_Propsed_System_User_groups_user_group, Class_Diagram_for_Propsed_System_User_groups_id}

# Class_Diagram_for_Propsed_System_Users class attributes and methods
Class_Diagram_for_Propsed_System_Users_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Users_firstname: Property = Property(name="firstname", type=StringType)
Class_Diagram_for_Propsed_System_Users_lastname: Property = Property(name="lastname", type=StringType)
Class_Diagram_for_Propsed_System_Users_email: Property = Property(name="email", type=StringType)
Class_Diagram_for_Propsed_System_Users_password: Property = Property(name="password", type=StringType)
Class_Diagram_for_Propsed_System_Users.attributes={Class_Diagram_for_Propsed_System_Users_id, Class_Diagram_for_Propsed_System_Users_lastname, Class_Diagram_for_Propsed_System_Users_email, Class_Diagram_for_Propsed_System_Users_firstname, Class_Diagram_for_Propsed_System_Users_password}

# Class_Diagram_for_Propsed_System_UserUpdates class attributes and methods
Class_Diagram_for_Propsed_System_UserUpdates_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_UserUpdates_user_id: Property = Property(name="user_id", type=IntegerType)
Class_Diagram_for_Propsed_System_UserUpdates.attributes={Class_Diagram_for_Propsed_System_UserUpdates_id, Class_Diagram_for_Propsed_System_UserUpdates_user_id}

# Class_Diagram_for_Propsed_System_Advances class attributes and methods
Class_Diagram_for_Propsed_System_Advances_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Advances_empid: Property = Property(name="empid", type=IntegerType)
Class_Diagram_for_Propsed_System_Advances_amount: Property = Property(name="amount", type=StringType)
Class_Diagram_for_Propsed_System_Advances_installments: Property = Property(name="installments", type=IntegerType)
Class_Diagram_for_Propsed_System_Advances_remain: Property = Property(name="remain", type=IntegerType)
Class_Diagram_for_Propsed_System_Advances.attributes={Class_Diagram_for_Propsed_System_Advances_remain, Class_Diagram_for_Propsed_System_Advances_empid, Class_Diagram_for_Propsed_System_Advances_id, Class_Diagram_for_Propsed_System_Advances_amount, Class_Diagram_for_Propsed_System_Advances_installments}

# Class_Diagram_for_Propsed_System_Messages class attributes and methods
Class_Diagram_for_Propsed_System_Messages_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_Messages_reciever: Property = Property(name="reciever", type=IntegerType)
Class_Diagram_for_Propsed_System_Messages_sender: Property = Property(name="sender", type=IntegerType)
Class_Diagram_for_Propsed_System_Messages_message: Property = Property(name="message", type=StringType)
Class_Diagram_for_Propsed_System_Messages_read_recipt: Property = Property(name="read_recipt", type=StringType)
Class_Diagram_for_Propsed_System_Messages.attributes={Class_Diagram_for_Propsed_System_Messages_read_recipt, Class_Diagram_for_Propsed_System_Messages_reciever, Class_Diagram_for_Propsed_System_Messages_id, Class_Diagram_for_Propsed_System_Messages_sender, Class_Diagram_for_Propsed_System_Messages_message}

# Class_Diagram_for_Propsed_System_User_Permissions class attributes and methods
Class_Diagram_for_Propsed_System_User_Permissions_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_User_Permissions_module: Property = Property(name="module", type=IntegerType)
Class_Diagram_for_Propsed_System_User_Permissions_permissions: Property = Property(name="permissions", type=StringType)
Class_Diagram_for_Propsed_System_User_Permissions.attributes={Class_Diagram_for_Propsed_System_User_Permissions_id, Class_Diagram_for_Propsed_System_User_Permissions_permissions, Class_Diagram_for_Propsed_System_User_Permissions_module}

# Class_Diagram_for_Propsed_System_ETF class attributes and methods
Class_Diagram_for_Propsed_System_ETF_id: Property = Property(name="id", type=IntegerType)
Class_Diagram_for_Propsed_System_ETF_precentage: Property = Property(name="precentage", type=StringType)
Class_Diagram_for_Propsed_System_ETF_effectivedate: Property = Property(name="effectivedate", type=DateType)
Class_Diagram_for_Propsed_System_ETF.attributes={Class_Diagram_for_Propsed_System_ETF_effectivedate, Class_Diagram_for_Propsed_System_ETF_precentage, Class_Diagram_for_Propsed_System_ETF_id}

# Relationships
Clark_Add_new_company_Events: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_new_company_Events",
    ends={
        Property(name="add_new_company_Events38", type=Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark39", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
View_personal_detais_Actor: BinaryAssociation = BinaryAssociation(
    name="View_personal_detais_Actor",
    ends={
        Property(name="actor0", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_personal_detais1", type=Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Request_Loan_and_advances_Actor: BinaryAssociation = BinaryAssociation(
    name="Request_Loan_and_advances_Actor",
    ends={
        Property(name="actor2", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="request_Loan_and_advances3", type=Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_Reports_Admin: BinaryAssociation = BinaryAssociation(
    name="View_Reports_Admin",
    ends={
        Property(name="admin4", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_Reports5", type=Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="View_Personal_Salary_history6", type=Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase28", type=Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor9", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase3",
    ends={
        Property(name="useCase310", type=Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor11", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase4: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase4",
    ends={
        Property(name="useCase412", type=Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor13", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase5",
    ends={
        Property(name="useCase514", type=Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Set_advances_status: BinaryAssociation = BinaryAssociation(
    name="Admin_Set_advances_status",
    ends={
        Property(name="set_advances_status16", type=Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_View_leave_Rquest: BinaryAssociation = BinaryAssociation(
    name="Admin_View_leave_Rquest",
    ends={
        Property(name="view_leave_Rquest18", type=Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_View_Employee_Time_Records: BinaryAssociation = BinaryAssociation(
    name="Admin_View_Employee_Time_Records",
    ends={
        Property(name="view_Employee_Time_Records20", type=Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Issue_and_Check_Appraislas: BinaryAssociation = BinaryAssociation(
    name="Admin_Issue_and_Check_Appraislas",
    ends={
        Property(name="issue_and_Check_Appraislas22", type=Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin23", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_View_Pay_Sheet_History: BinaryAssociation = BinaryAssociation(
    name="Admin_View_Pay_Sheet_History",
    ends={
        Property(name="view_Pay_Sheet_History24", type=Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin25", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Approve_Employee_Pay_sheets: BinaryAssociation = BinaryAssociation(
    name="Admin_Approve_Employee_Pay_sheets",
    ends={
        Property(name="approve_Employee_Pay_sheets26", type=Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Set_Leave_status: BinaryAssociation = BinaryAssociation(
    name="Admin_Set_Leave_status",
    ends={
        Property(name="set_Leave_status28", type=Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin29", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_Add_Employee_profile: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_Employee_profile",
    ends={
        Property(name="add_Employee_profile30", type=Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark31", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_Add_New_department: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_New_department",
    ends={
        Property(name="add_New_department32", type=Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark33", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_View_Reports: BinaryAssociation = BinaryAssociation(
    name="Clark_View_Reports",
    ends={
        Property(name="view_Reports34", type=Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="clark35", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_View_Employee_profiles: BinaryAssociation = BinaryAssociation(
    name="Clark_View_Employee_profiles",
    ends={
        Property(name="view_Employee_profiles36", type=Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark37", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_Generate_Paysheet: BinaryAssociation = BinaryAssociation(
    name="Clark_Generate_Paysheet",
    ends={
        Property(name="generate_Paysheet40", type=Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark41", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clark_Add_Employee_Time_Records: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_Employee_Time_Records",
    ends={
        Property(name="add_Employee_Time_Records42", type=Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark43", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Users_Employee: BinaryAssociation = BinaryAssociation(
    name="Users_Employee",
    ends={
        Property(name="Users_Employee_044", type=Package_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Users_Employee_145", type=Package_Users, multiplicity=Multiplicity(1, 1))
    }
)
Attendance_Employee: BinaryAssociation = BinaryAssociation(
    name="Attendance_Employee",
    ends={
        Property(name="Attendance_Employee_046", type=Package_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Attendance_Employee_147", type=Package_Attendance, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_OT_Requests: BinaryAssociation = BinaryAssociation(
    name="Employee_OT_Requests",
    ends={
        Property(name="Employee_OT_Requests_048", type=Package_OT_Requests, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_OT_Requests_149", type=Package_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Shifts: BinaryAssociation = BinaryAssociation(
    name="Employee_Shifts",
    ends={
        Property(name="Employee_Shifts_050", type=Package_Shifts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Shifts_151", type=Package_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Leave_Taken: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave_Taken",
    ends={
        Property(name="Employee_Leave_Taken_052", type=Package_Leave_Taken, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_Leave_Taken_153", type=Package_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_EmployeeSalary: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeSalary",
    ends={
        Property(name="Employee_EmployeeSalary_054", type=Package_EmployeeSalary, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_EmployeeSalary_155", type=Package_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Allowance_Employee: BinaryAssociation = BinaryAssociation(
    name="Allowance_Employee",
    ends={
        Property(name="Allowance_Employee_056", type=Package_Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="Allowance_Employee_157", type=Package_Allowance, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Messages: BinaryAssociation = BinaryAssociation(
    name="Employee_Messages",
    ends={
        Property(name="Employee_Messages_058", type=Package_Messages, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Messages_159", type=Package_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_LeaveProfiles: BinaryAssociation = BinaryAssociation(
    name="Employee_LeaveProfiles",
    ends={
        Property(name="Employee_LeaveProfiles_060", type=Package_LeaveProfiles, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_LeaveProfiles_161", type=Package_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Posts: BinaryAssociation = BinaryAssociation(
    name="Employee_Posts",
    ends={
        Property(name="Employee_Posts_062", type=Package_Posts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Posts_163", type=Package_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Departments_Employee: BinaryAssociation = BinaryAssociation(
    name="Departments_Employee",
    ends={
        Property(name="Departments_Employee_064", type=Package_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Departments_Employee_165", type=Package_Departments, multiplicity=Multiplicity(1, 1))
    }
)
Employee_EmployeeParoll: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeParoll",
    ends={
        Property(name="Employee_EmployeeParoll_066", type=Package_EmployeeParoll, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_EmployeeParoll_167", type=Package_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_User_groups: BinaryAssociation = BinaryAssociation(
    name="Employee_User_groups",
    ends={
        Property(name="Employee_User_groups_068", type=Package_User_groups, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_User_groups_169", type=Package_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
User_groups_User_Permissions: BinaryAssociation = BinaryAssociation(
    name="User_groups_User_Permissions",
    ends={
        Property(name="User_groups_User_Permissions_070", type=Package_User_Permissions, multiplicity=Multiplicity(1, 1)),
        Property(name="User_groups_User_Permissions_171", type=Package_User_groups, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Advances: BinaryAssociation = BinaryAssociation(
    name="Employee_Advances",
    ends={
        Property(name="advances72", type=Package_Advances, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Advances_173", type=Package_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Users_Employee1: BinaryAssociation = BinaryAssociation(
    name="Users_Employee1",
    ends={
        Property(name="Users_Employee_074", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Users_Employee_175", type=Class_Diagram_for_Propsed_System_Users, multiplicity=Multiplicity(1, 1))
    }
)
Attendance_Employee1: BinaryAssociation = BinaryAssociation(
    name="Attendance_Employee1",
    ends={
        Property(name="Attendance_Employee_076", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Attendance_Employee_177", type=Class_Diagram_for_Propsed_System_Attendance, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_OT_Requests1: BinaryAssociation = BinaryAssociation(
    name="Employee_OT_Requests1",
    ends={
        Property(name="Employee_OT_Requests_078", type=Class_Diagram_for_Propsed_System_OT_Requests, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_OT_Requests_179", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Shifts1: BinaryAssociation = BinaryAssociation(
    name="Employee_Shifts1",
    ends={
        Property(name="Employee_Shifts_080", type=Class_Diagram_for_Propsed_System_Shifts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Shifts_181", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Leave_Taken1: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave_Taken1",
    ends={
        Property(name="Employee_Leave_Taken_082", type=Class_Diagram_for_Propsed_System_Leave_Taken, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_Leave_Taken_183", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_EmployeeSalary1: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeSalary1",
    ends={
        Property(name="Employee_EmployeeSalary_084", type=Class_Diagram_for_Propsed_System_EmployeeSalary, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_EmployeeSalary_185", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Allowance_Employee1: BinaryAssociation = BinaryAssociation(
    name="Allowance_Employee1",
    ends={
        Property(name="Allowance_Employee_086", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="Allowance_Employee_187", type=Class_Diagram_for_Propsed_System_Allowance, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Messages1: BinaryAssociation = BinaryAssociation(
    name="Employee_Messages1",
    ends={
        Property(name="Employee_Messages_088", type=Class_Diagram_for_Propsed_System_Messages, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Messages_189", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_LeaveProfiles1: BinaryAssociation = BinaryAssociation(
    name="Employee_LeaveProfiles1",
    ends={
        Property(name="Employee_LeaveProfiles_090", type=Class_Diagram_for_Propsed_System_LeaveProfiles, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_LeaveProfiles_191", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Posts1: BinaryAssociation = BinaryAssociation(
    name="Employee_Posts1",
    ends={
        Property(name="Employee_Posts_092", type=Class_Diagram_for_Propsed_System_Posts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Posts_193", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Departments_Employee1: BinaryAssociation = BinaryAssociation(
    name="Departments_Employee1",
    ends={
        Property(name="Departments_Employee_094", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Departments_Employee_195", type=Class_Diagram_for_Propsed_System_Departments, multiplicity=Multiplicity(1, 1))
    }
)
Employee_EmployeeParoll1: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeParoll1",
    ends={
        Property(name="Employee_EmployeeParoll_096", type=Class_Diagram_for_Propsed_System_EmployeeParoll, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_EmployeeParoll_197", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_User_groups1: BinaryAssociation = BinaryAssociation(
    name="Employee_User_groups1",
    ends={
        Property(name="Employee_User_groups_098", type=Class_Diagram_for_Propsed_System_User_groups, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_User_groups_199", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
User_groups_User_Permissions1: BinaryAssociation = BinaryAssociation(
    name="User_groups_User_Permissions1",
    ends={
        Property(name="User_groups_User_Permissions_0100", type=Class_Diagram_for_Propsed_System_User_Permissions, multiplicity=Multiplicity(1, 1)),
        Property(name="User_groups_User_Permissions_1101", type=Class_Diagram_for_Propsed_System_User_groups, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Advances1: BinaryAssociation = BinaryAssociation(
    name="Employee_Advances1",
    ends={
        Property(name="Employee_Advances_0102", type=Class_Diagram_for_Propsed_System_Advances, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Advances_1103", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Deductions: BinaryAssociation = BinaryAssociation(
    name="Employee_Deductions",
    ends={
        Property(name="Employee_Deductions_0104", type=Class_Diagram_for_Propsed_System_Deductions, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Deductions_1105", type=Class_Diagram_for_Propsed_System_Employee, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jmSOYF1rEeqK2M3E1LfZ7Q",
    types={Employee_Actor, Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase, Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase, Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase, Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase, Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase, Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase, Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase, Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase, Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase, Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase, Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase, Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase, Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase, Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase, Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1, Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase, Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase, Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase, Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase, Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase, Admin_Actor, Clark_Actor, Interface_Interface, Package_Allowance, Package_Attendance, Package_DeuctionTypes, Package_AllowanceTypes, Package_Deductions, Package_Departments, Package_Shifts, Package_Posts, Package_Employee, Package_EmployeeParoll, Package_EmployeeSalary, Package_EPF, Package_Event, Package_Leave_Taken, Package_LeaveProfiles, Package_OT_Requests, Package_User_groups, Package_Users, Package_UserUpdates, Package_Advances, Package_Messages, Package_User_Permissions, Package_ETF, Class_Diagram_for_Propsed_System_Allowance, Class_Diagram_for_Propsed_System_Attendance, Class_Diagram_for_Propsed_System_DeuctionTypes, Class_Diagram_for_Propsed_System_AllowanceTypes, Class_Diagram_for_Propsed_System_Deductions, Class_Diagram_for_Propsed_System_Departments, Class_Diagram_for_Propsed_System_Shifts, Class_Diagram_for_Propsed_System_Posts, Class_Diagram_for_Propsed_System_Employee, Class_Diagram_for_Propsed_System_EmployeeParoll, Class_Diagram_for_Propsed_System_EmployeeSalary, Class_Diagram_for_Propsed_System_EPF, Class_Diagram_for_Propsed_System_Event, Class_Diagram_for_Propsed_System_Leave_Taken, Class_Diagram_for_Propsed_System_LeaveProfiles, Class_Diagram_for_Propsed_System_OT_Requests, Class_Diagram_for_Propsed_System_User_groups, Class_Diagram_for_Propsed_System_Users, Class_Diagram_for_Propsed_System_UserUpdates, Class_Diagram_for_Propsed_System_Advances, Class_Diagram_for_Propsed_System_Messages, Class_Diagram_for_Propsed_System_User_Permissions, Class_Diagram_for_Propsed_System_ETF, ot_Type, date},
    associations={Clark_Add_new_company_Events, View_personal_detais_Actor, Request_Loan_and_advances_Actor, View_Reports_Admin, Actor_UseCase, Actor_UseCase2, Actor_UseCase3, Actor_UseCase4, Actor_UseCase5, Admin_Set_advances_status, Admin_View_leave_Rquest, Admin_View_Employee_Time_Records, Admin_Issue_and_Check_Appraislas, Admin_View_Pay_Sheet_History, Admin_Approve_Employee_Pay_sheets, Admin_Set_Leave_status, Clark_Add_Employee_profile, Clark_Add_New_department, Clark_View_Reports, Clark_View_Employee_profiles, Clark_Generate_Paysheet, Clark_Add_Employee_Time_Records, Users_Employee, Attendance_Employee, Employee_OT_Requests, Employee_Shifts, Employee_Leave_Taken, Employee_EmployeeSalary, Allowance_Employee, Employee_Messages, Employee_LeaveProfiles, Employee_Posts, Departments_Employee, Employee_EmployeeParoll, Employee_User_groups, User_groups_User_Permissions, Employee_Advances, Users_Employee1, Attendance_Employee1, Employee_OT_Requests1, Employee_Shifts1, Employee_Leave_Taken1, Employee_EmployeeSalary1, Allowance_Employee1, Employee_Messages1, Employee_LeaveProfiles1, Employee_Posts1, Departments_Employee1, Employee_EmployeeParoll1, Employee_User_groups1, User_groups_User_Permissions1, Employee_Advances1, Employee_Deductions},
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