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
Package2_Allowance = Class(name="Package2_Allowance")
Package2_Attendance = Class(name="Package2_Attendance")
Package2_DeuctionTypes = Class(name="Package2_DeuctionTypes")
Package2_AllowanceTypes = Class(name="Package2_AllowanceTypes")
Package2_Deductions = Class(name="Package2_Deductions")
Package2_Departments = Class(name="Package2_Departments")
Package2_Shifts = Class(name="Package2_Shifts")
Package2_Posts = Class(name="Package2_Posts")
Package2_Employee = Class(name="Package2_Employee")
Package2_EmployeeParoll = Class(name="Package2_EmployeeParoll")
Package2_EmployeeSalary = Class(name="Package2_EmployeeSalary")
Package2_EPF = Class(name="Package2_EPF")
Package2_Event = Class(name="Package2_Event")
Package2_Leave_Taken = Class(name="Package2_Leave_Taken")
Package2_LeaveProfiles = Class(name="Package2_LeaveProfiles")
Package2_OT_Requests = Class(name="Package2_OT_Requests")
Package2_User_groups = Class(name="Package2_User_groups")
Package2_Users = Class(name="Package2_Users")
Package2_UserUpdates = Class(name="Package2_UserUpdates")
Package2_Advances = Class(name="Package2_Advances")
Package2_Messages = Class(name="Package2_Messages")
Package2_User_Permissions = Class(name="Package2_User_Permissions")
Package2_ETF = Class(name="Package2_ETF")
Presentation_StaffUI = Class(name="Presentation_StaffUI")

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
Package_Allowance.attributes={Package_Allowance_id, Package_Allowance_Effectivedate, Package_Allowance_emp_id}

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
Package_Deductions.attributes={Package_Deductions_attribute, Package_Deductions_attribute2}

# Package_Departments class attributes and methods
Package_Departments_id: Property = Property(name="id", type=IntegerType)
Package_Departments.attributes={Package_Departments_id}

# Package_Shifts class attributes and methods
Package_Shifts_attribute: Property = Property(name="attribute", type=StringType)
Package_Shifts_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Shifts.attributes={Package_Shifts_attribute, Package_Shifts_attribute2}

# Package_Posts class attributes and methods
Package_Posts_attribute: Property = Property(name="attribute", type=StringType)
Package_Posts_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Posts.attributes={Package_Posts_attribute, Package_Posts_attribute2}

# Package_Employee class attributes and methods
Package_Employee_id: Property = Property(name="id", type=StringType)
Package_Employee_empid: Property = Property(name="empid", type=StringType)
Package_Employee_depid: Property = Property(name="depid", type=IntegerType)
Package_Employee_post: Property = Property(name="post", type=StringType)
Package_Employee_shift: Property = Property(name="shift", type=StringType)
Package_Employee_usergroup: Property = Property(name="usergroup", type=IntegerType)
Package_Employee_leavegroup: Property = Property(name="leavegroup", type=IntegerType)
Package_Employee.attributes={Package_Employee_post, Package_Employee_empid, Package_Employee_depid, Package_Employee_shift, Package_Employee_usergroup, Package_Employee_id, Package_Employee_leavegroup}

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
Package_EPF_precentage: Property = Property(name="precentage", type=IntegerType)
Package_EPF_effectve_date: Property = Property(name="effectve_date", type=Package_UserUpdates)
Package_EPF.attributes={Package_EPF_effectve_date, Package_EPF_precentage, Package_EPF_id}

# Package_Event class attributes and methods

# Package_Leave_Taken class attributes and methods
Package_Leave_Taken_attribute: Property = Property(name="attribute", type=StringType)
Package_Leave_Taken_attribute2: Property = Property(name="attribute2", type=StringType)
Package_Leave_Taken.attributes={Package_Leave_Taken_attribute, Package_Leave_Taken_attribute2}

# Package_LeaveProfiles class attributes and methods
Package_LeaveProfiles_attribute: Property = Property(name="attribute", type=StringType)
Package_LeaveProfiles_attribute2: Property = Property(name="attribute2", type=StringType)
Package_LeaveProfiles.attributes={Package_LeaveProfiles_attribute, Package_LeaveProfiles_attribute2}

# Package_OT_Requests class attributes and methods
Package_OT_Requests_id: Property = Property(name="id", type=IntegerType)
Package_OT_Requests_OtDay: Property = Property(name="OtDay", type=DateType)
Package_OT_Requests_OTType: Property = Property(name="OTType", type=IntegerType)
Package_OT_Requests_EmpID: Property = Property(name="EmpID", type=IntegerType)
Package_OT_Requests.attributes={Package_OT_Requests_EmpID, Package_OT_Requests_id, Package_OT_Requests_OtDay, Package_OT_Requests_OTType}

# Package_User_groups class attributes and methods
Package_User_groups_attribute: Property = Property(name="attribute", type=StringType)
Package_User_groups_attribute2: Property = Property(name="attribute2", type=StringType)
Package_User_groups_attribute3: Property = Property(name="attribute3", type=StringType)
Package_User_groups.attributes={Package_User_groups_attribute, Package_User_groups_attribute3, Package_User_groups_attribute2}

# Package_Users class attributes and methods
Package_Users_id: Property = Property(name="id", type=IntegerType)
Package_Users_firstname: Property = Property(name="firstname", type=IntegerType)
Package_Users_lastname: Property = Property(name="lastname", type=IntegerType)
Package_Users_email: Property = Property(name="email", type=IntegerType)
Package_Users_password: Property = Property(name="password", type=IntegerType)
Package_Users.attributes={Package_Users_firstname, Package_Users_password, Package_Users_lastname, Package_Users_id, Package_Users_email}

# Package_UserUpdates class attributes and methods

# Package_Advances class attributes and methods

# Package_Messages class attributes and methods

# Package_User_Permissions class attributes and methods
Package_User_Permissions_attribute: Property = Property(name="attribute", type=StringType)
Package_User_Permissions_attribute2: Property = Property(name="attribute2", type=StringType)
Package_User_Permissions.attributes={Package_User_Permissions_attribute, Package_User_Permissions_attribute2}

# Package_ETF class attributes and methods

# Package2_Allowance class attributes and methods
Package2_Allowance_id: Property = Property(name="id", type=IntegerType)
Package2_Allowance_emp_id: Property = Property(name="emp_id", type=StringType)
Package2_Allowance_Effectivedate: Property = Property(name="Effectivedate", type=StringType)
Package2_Allowance.attributes={Package2_Allowance_Effectivedate, Package2_Allowance_id, Package2_Allowance_emp_id}

# Package2_Attendance class attributes and methods
Package2_Attendance_id: Property = Property(name="id", type=IntegerType)
Package2_Attendance_timein: Property = Property(name="timein", type=StringType)
Package2_Attendance_timeout: Property = Property(name="timeout", type=StringType)
Package2_Attendance_empid: Property = Property(name="empid", type=IntegerType)
Package2_Attendance.attributes={Package2_Attendance_timein, Package2_Attendance_id, Package2_Attendance_timeout, Package2_Attendance_empid}

# Package2_DeuctionTypes class attributes and methods

# Package2_AllowanceTypes class attributes and methods

# Package2_Deductions class attributes and methods
Package2_Deductions_attribute: Property = Property(name="attribute", type=StringType)
Package2_Deductions_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_Deductions.attributes={Package2_Deductions_attribute2, Package2_Deductions_attribute}

# Package2_Departments class attributes and methods
Package2_Departments_id: Property = Property(name="id", type=IntegerType)
Package2_Departments_depname: Property = Property(name="depname", type=StringType)
Package2_Departments.attributes={Package2_Departments_id, Package2_Departments_depname}

# Package2_Shifts class attributes and methods
Package2_Shifts_id: Property = Property(name="id", type=StringType)
Package2_Shifts_shiftaname: Property = Property(name="shiftaname", type=StringType)
Package2_Shifts_starttime: Property = Property(name="starttime", type=StringType)
Package2_Shifts_endtime: Property = Property(name="endtime", type=StringType)
Package2_Shifts.attributes={Package2_Shifts_shiftaname, Package2_Shifts_id, Package2_Shifts_starttime, Package2_Shifts_endtime}

# Package2_Posts class attributes and methods
Package2_Posts_id: Property = Property(name="id", type=IntegerType)
Package2_Posts_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_Posts.attributes={Package2_Posts_id, Package2_Posts_attribute2}

# Package2_Employee class attributes and methods
Package2_Employee_id: Property = Property(name="id", type=StringType)
Package2_Employee_empid: Property = Property(name="empid", type=StringType)
Package2_Employee_depid: Property = Property(name="depid", type=IntegerType)
Package2_Employee_post: Property = Property(name="post", type=StringType)
Package2_Employee_shift: Property = Property(name="shift", type=StringType)
Package2_Employee_usergroup: Property = Property(name="usergroup", type=IntegerType)
Package2_Employee_leavegroup: Property = Property(name="leavegroup", type=IntegerType)
Package2_Employee.attributes={Package2_Employee_id, Package2_Employee_empid, Package2_Employee_leavegroup, Package2_Employee_post, Package2_Employee_shift, Package2_Employee_depid, Package2_Employee_usergroup}

# Package2_EmployeeParoll class attributes and methods
Package2_EmployeeParoll_id: Property = Property(name="id", type=IntegerType)
Package2_EmployeeParoll_empid: Property = Property(name="empid", type=IntegerType)
Package2_EmployeeParoll_basicslaray: Property = Property(name="basicslaray", type=IntegerType)
Package2_EmployeeParoll_empid3: Property = Property(name="empid3", type=IntegerType)
Package2_EmployeeParoll_otamount: Property = Property(name="otamount", type=IntegerType)
Package2_EmployeeParoll_doyamount: Property = Property(name="doyamount", type=IntegerType)
Package2_EmployeeParoll_epf: Property = Property(name="epf", type=IntegerType)
Package2_EmployeeParoll_etf: Property = Property(name="etf", type=StringType)
Package2_EmployeeParoll.attributes={Package2_EmployeeParoll_empid3, Package2_EmployeeParoll_basicslaray, Package2_EmployeeParoll_epf, Package2_EmployeeParoll_doyamount, Package2_EmployeeParoll_etf, Package2_EmployeeParoll_id, Package2_EmployeeParoll_otamount, Package2_EmployeeParoll_empid}

# Package2_EmployeeSalary class attributes and methods
Package2_EmployeeSalary_attribute: Property = Property(name="attribute", type=StringType)
Package2_EmployeeSalary_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_EmployeeSalary.attributes={Package2_EmployeeSalary_attribute2, Package2_EmployeeSalary_attribute}

# Package2_EPF class attributes and methods
Package2_EPF_id: Property = Property(name="id", type=IntegerType)
Package2_EPF_precentage: Property = Property(name="precentage", type=IntegerType)
Package2_EPF_effectve_date: Property = Property(name="effectve_date", type=Package2_UserUpdates)
Package2_EPF.attributes={Package2_EPF_precentage, Package2_EPF_effectve_date, Package2_EPF_id}

# Package2_Event class attributes and methods

# Package2_Leave_Taken class attributes and methods
Package2_Leave_Taken_attribute: Property = Property(name="attribute", type=StringType)
Package2_Leave_Taken_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_Leave_Taken.attributes={Package2_Leave_Taken_attribute, Package2_Leave_Taken_attribute2}

# Package2_LeaveProfiles class attributes and methods
Package2_LeaveProfiles_id: Property = Property(name="id", type=IntegerType)
Package2_LeaveProfiles_name: Property = Property(name="name", type=StringType)
Package2_LeaveProfiles_casual: Property = Property(name="casual", type=IntegerType)
Package2_LeaveProfiles_anual: Property = Property(name="anual", type=IntegerType)
Package2_LeaveProfiles.attributes={Package2_LeaveProfiles_id, Package2_LeaveProfiles_casual, Package2_LeaveProfiles_name, Package2_LeaveProfiles_anual}

# Package2_OT_Requests class attributes and methods
Package2_OT_Requests_id: Property = Property(name="id", type=IntegerType)
Package2_OT_Requests_OtDay: Property = Property(name="OtDay", type=DateType)
Package2_OT_Requests_OTType: Property = Property(name="OTType", type=IntegerType)
Package2_OT_Requests_EmpID: Property = Property(name="EmpID", type=IntegerType)
Package2_OT_Requests.attributes={Package2_OT_Requests_OTType, Package2_OT_Requests_EmpID, Package2_OT_Requests_OtDay, Package2_OT_Requests_id}

# Package2_User_groups class attributes and methods
Package2_User_groups_attribute: Property = Property(name="attribute", type=StringType)
Package2_User_groups_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_User_groups_attribute3: Property = Property(name="attribute3", type=StringType)
Package2_User_groups.attributes={Package2_User_groups_attribute, Package2_User_groups_attribute3, Package2_User_groups_attribute2}

# Package2_Users class attributes and methods
Package2_Users_id: Property = Property(name="id", type=IntegerType)
Package2_Users_firstname: Property = Property(name="firstname", type=IntegerType)
Package2_Users_lastname: Property = Property(name="lastname", type=IntegerType)
Package2_Users_email: Property = Property(name="email", type=IntegerType)
Package2_Users_password: Property = Property(name="password", type=IntegerType)
Package2_Users.attributes={Package2_Users_lastname, Package2_Users_firstname, Package2_Users_password, Package2_Users_email, Package2_Users_id}

# Package2_UserUpdates class attributes and methods

# Package2_Advances class attributes and methods

# Package2_Messages class attributes and methods

# Package2_User_Permissions class attributes and methods
Package2_User_Permissions_attribute: Property = Property(name="attribute", type=StringType)
Package2_User_Permissions_attribute2: Property = Property(name="attribute2", type=StringType)
Package2_User_Permissions.attributes={Package2_User_Permissions_attribute, Package2_User_Permissions_attribute2}

# Package2_ETF class attributes and methods

# Presentation_StaffUI class attributes and methods

# Relationships
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="actor9", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase28", type=Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase, multiplicity=Multiplicity(0, 1))
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
Users_Employee1: BinaryAssociation = BinaryAssociation(
    name="Users_Employee1",
    ends={
        Property(name="Users_Employee_074", type=Package2_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Users_Employee_175", type=Package2_Users, multiplicity=Multiplicity(1, 1))
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
Clark_Add_new_company_Events: BinaryAssociation = BinaryAssociation(
    name="Clark_Add_new_company_Events",
    ends={
        Property(name="add_new_company_Events38", type=Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clark39", type=Clark_Actor, multiplicity=Multiplicity(0, 1))
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
Attendance_Employee1: BinaryAssociation = BinaryAssociation(
    name="Attendance_Employee1",
    ends={
        Property(name="Attendance_Employee_076", type=Package2_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Attendance_Employee_177", type=Package2_Attendance, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_OT_Requests1: BinaryAssociation = BinaryAssociation(
    name="Employee_OT_Requests1",
    ends={
        Property(name="Employee_OT_Requests_078", type=Package2_OT_Requests, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_OT_Requests_179", type=Package2_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Shifts1: BinaryAssociation = BinaryAssociation(
    name="Employee_Shifts1",
    ends={
        Property(name="Employee_Shifts_080", type=Package2_Shifts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Shifts_181", type=Package2_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Leave_Taken1: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave_Taken1",
    ends={
        Property(name="Employee_Leave_Taken_082", type=Package2_Leave_Taken, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_Leave_Taken_183", type=Package2_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_EmployeeSalary1: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeSalary1",
    ends={
        Property(name="Employee_EmployeeSalary_084", type=Package2_EmployeeSalary, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_EmployeeSalary_185", type=Package2_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Allowance_Employee1: BinaryAssociation = BinaryAssociation(
    name="Allowance_Employee1",
    ends={
        Property(name="Allowance_Employee_086", type=Package2_Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="Allowance_Employee_187", type=Package2_Allowance, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Messages1: BinaryAssociation = BinaryAssociation(
    name="Employee_Messages1",
    ends={
        Property(name="Employee_Messages_088", type=Package2_Messages, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Messages_189", type=Package2_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_LeaveProfiles1: BinaryAssociation = BinaryAssociation(
    name="Employee_LeaveProfiles1",
    ends={
        Property(name="Employee_LeaveProfiles_090", type=Package2_LeaveProfiles, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_LeaveProfiles_191", type=Package2_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Posts1: BinaryAssociation = BinaryAssociation(
    name="Employee_Posts1",
    ends={
        Property(name="Employee_Posts_092", type=Package2_Posts, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_Posts_193", type=Package2_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Departments_Employee1: BinaryAssociation = BinaryAssociation(
    name="Departments_Employee1",
    ends={
        Property(name="Departments_Employee_094", type=Package2_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Departments_Employee_195", type=Package2_Departments, multiplicity=Multiplicity(1, 1))
    }
)
Employee_EmployeeParoll1: BinaryAssociation = BinaryAssociation(
    name="Employee_EmployeeParoll1",
    ends={
        Property(name="Employee_EmployeeParoll_096", type=Package2_EmployeeParoll, multiplicity=Multiplicity(1, 9999)),
        Property(name="Employee_EmployeeParoll_197", type=Package2_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
Employee_User_groups1: BinaryAssociation = BinaryAssociation(
    name="Employee_User_groups1",
    ends={
        Property(name="Employee_User_groups_098", type=Package2_User_groups, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee_User_groups_199", type=Package2_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
User_groups_User_Permissions1: BinaryAssociation = BinaryAssociation(
    name="User_groups_User_Permissions1",
    ends={
        Property(name="User_groups_User_Permissions_0100", type=Package2_User_Permissions, multiplicity=Multiplicity(1, 1)),
        Property(name="User_groups_User_Permissions_1101", type=Package2_User_groups, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Advances1: BinaryAssociation = BinaryAssociation(
    name="Employee_Advances1",
    ends={
        Property(name="advances102", type=Package2_Advances, multiplicity=Multiplicity(0, 9999)),
        Property(name="Employee_Advances_1103", type=Package2_Employee, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Kqi2YBTZEeqDmNBP3mfLQg",
    types={Employee_Actor, Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase, Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase, Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase, Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase, Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase, Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase, Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase, Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase, Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase, Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase, Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase, Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase, Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase, Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase, Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1, Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase, Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase, Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase, Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase, Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase, Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase, Admin_Actor, Clark_Actor, Interface_Interface, Package_Allowance, Package_Attendance, Package_DeuctionTypes, Package_AllowanceTypes, Package_Deductions, Package_Departments, Package_Shifts, Package_Posts, Package_Employee, Package_EmployeeParoll, Package_EmployeeSalary, Package_EPF, Package_Event, Package_Leave_Taken, Package_LeaveProfiles, Package_OT_Requests, Package_User_groups, Package_Users, Package_UserUpdates, Package_Advances, Package_Messages, Package_User_Permissions, Package_ETF, Package2_Allowance, Package2_Attendance, Package2_DeuctionTypes, Package2_AllowanceTypes, Package2_Deductions, Package2_Departments, Package2_Shifts, Package2_Posts, Package2_Employee, Package2_EmployeeParoll, Package2_EmployeeSalary, Package2_EPF, Package2_Event, Package2_Leave_Taken, Package2_LeaveProfiles, Package2_OT_Requests, Package2_User_groups, Package2_Users, Package2_UserUpdates, Package2_Advances, Package2_Messages, Package2_User_Permissions, Package2_ETF, Presentation_StaffUI, ot_Type, date},
    associations={Actor_UseCase2, View_personal_detais_Actor, Request_Loan_and_advances_Actor, View_Reports_Admin, Actor_UseCase, Users_Employee1, Actor_UseCase3, Actor_UseCase4, Actor_UseCase5, Admin_Set_advances_status, Admin_View_leave_Rquest, Admin_View_Employee_Time_Records, Admin_Issue_and_Check_Appraislas, Admin_View_Pay_Sheet_History, Admin_Approve_Employee_Pay_sheets, Admin_Set_Leave_status, Clark_Add_Employee_profile, Clark_Add_New_department, Clark_View_Reports, Clark_View_Employee_profiles, Clark_Add_new_company_Events, Clark_Generate_Paysheet, Clark_Add_Employee_Time_Records, Users_Employee, Attendance_Employee, Employee_OT_Requests, Employee_Shifts, Employee_Leave_Taken, Employee_EmployeeSalary, Allowance_Employee, Employee_Messages, Employee_LeaveProfiles, Employee_Posts, Departments_Employee, Employee_EmployeeParoll, Employee_User_groups, User_groups_User_Permissions, Employee_Advances, Attendance_Employee1, Employee_OT_Requests1, Employee_Shifts1, Employee_Leave_Taken1, Employee_EmployeeSalary1, Allowance_Employee1, Employee_Messages1, Employee_LeaveProfiles1, Employee_Posts1, Departments_Employee1, Employee_EmployeeParoll1, Employee_User_groups1, User_groups_User_Permissions1, Employee_Advances1},
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