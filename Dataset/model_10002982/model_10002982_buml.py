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
Login_UseCase = Class(name="Login_UseCase")
Employee_Actor = Class(name="Employee_Actor")
Change_Password_UseCase = Class(name="Change_Password_UseCase")
Query_Eligibility_UseCase = Class(name="Query_Eligibility_UseCase")
Query_Leave_Balance_UseCase = Class(name="Query_Leave_Balance_UseCase")
Query_Leave_History_UseCase = Class(name="Query_Leave_History_UseCase")
Apply_Leave_UseCase = Class(name="Apply_Leave_UseCase")
Leave_Request_Status_UseCase = Class(name="Leave_Request_Status_UseCase")
Withdraw_Application_UseCase = Class(name="Withdraw_Application_UseCase")
Approver_Jobs_UseCase = Class(name="Approver_Jobs_UseCase")
Approve_RejectRequests_UseCase = Class(name="Approve_RejectRequests_UseCase")
Cancel_Leaves_UseCase = Class(name="Cancel_Leaves_UseCase")
Admin_Actor = Class(name="Admin_Actor")
CreateUser_UseCase = Class(name="CreateUser_UseCase")
Update_Calendar_UseCase = Class(name="Update_Calendar_UseCase")
Application_Actor = Class(name="Application_Actor")
SendNotification_UseCase = Class(name="SendNotification_UseCase")
Credit_Leaves_UseCase = Class(name="Credit_Leaves_UseCase")
AutoApproval_UseCase = Class(name="AutoApproval_UseCase")
GenerateSummary_UseCase = Class(name="GenerateSummary_UseCase")
Student = Class(name="Student")
Query = Class(name="Query")
LeaveBalanceQuery = Class(name="LeaveBalanceQuery")
LeaveHistoryQuery = Class(name="LeaveHistoryQuery")
LeaveApplication = Class(name="LeaveApplication")
Request = Class(name="Request")
ApplyLeaveRequest = Class(name="ApplyLeaveRequest")
CancelLeaveRequest = Class(name="CancelLeaveRequest")
LeaveStatusQuery = Class(name="LeaveStatusQuery")
LoginAction = Class(name="LoginAction")
CreateUserAction = Class(name="CreateUserAction")
UpdateCalendar = Class(name="UpdateCalendar")
ApplicationUtils = Class(name="ApplicationUtils")

# Login_UseCase class attributes and methods

# Employee_Actor class attributes and methods

# Change_Password_UseCase class attributes and methods

# Query_Eligibility_UseCase class attributes and methods

# Query_Leave_Balance_UseCase class attributes and methods

# Query_Leave_History_UseCase class attributes and methods

# Apply_Leave_UseCase class attributes and methods

# Leave_Request_Status_UseCase class attributes and methods

# Withdraw_Application_UseCase class attributes and methods

# Approver_Jobs_UseCase class attributes and methods

# Approve_RejectRequests_UseCase class attributes and methods

# Cancel_Leaves_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# CreateUser_UseCase class attributes and methods

# Update_Calendar_UseCase class attributes and methods

# Application_Actor class attributes and methods

# SendNotification_UseCase class attributes and methods

# Credit_Leaves_UseCase class attributes and methods

# AutoApproval_UseCase class attributes and methods

# GenerateSummary_UseCase class attributes and methods

# Student class attributes and methods
Student_studentId: Property = Property(name="studentId", type=StringType)
Student_studentName: Property = Property(name="studentName", type=StringType)
Student_year: Property = Property(name="year", type=IntegerType)
Student_branch: Property = Property(name="branch", type=StringType)
Student_password: Property = Property(name="password", type=StringType)
Student_leavesTaken: Property = Property(name="leavesTaken", type=StringType)
Student.attributes={Student_branch, Student_password, Student_year, Student_leavesTaken, Student_studentId, Student_studentName}

# Query class attributes and methods
Query_requestId: Property = Property(name="requestId", type=StringType)
Query_user: Property = Property(name="user", type=Student)
Query.attributes={Query_requestId, Query_user}

# LeaveBalanceQuery class attributes and methods

# LeaveHistoryQuery class attributes and methods
LeaveHistoryQuery_fromDate: Property = Property(name="fromDate", type=DateType)
LeaveHistoryQuery_toDate: Property = Property(name="toDate", type=DateType)
LeaveHistoryQuery.attributes={LeaveHistoryQuery_toDate, LeaveHistoryQuery_fromDate}

# LeaveApplication class attributes and methods
LeaveApplication_applicationId: Property = Property(name="applicationId", type=StringType)
LeaveApplication_fromDate: Property = Property(name="fromDate", type=DateType)
LeaveApplication_toDate: Property = Property(name="toDate", type=DateType)
LeaveApplication_reason: Property = Property(name="reason", type=StringType)
LeaveApplication_studentId: Property = Property(name="studentId", type=StringType)
LeaveApplication_status: Property = Property(name="status", type=StringType)
LeaveApplication_approverComments: Property = Property(name="approverComments", type=StringType)
LeaveApplication.attributes={LeaveApplication_studentId, LeaveApplication_toDate, LeaveApplication_status, LeaveApplication_approverComments, LeaveApplication_fromDate, LeaveApplication_applicationId, LeaveApplication_reason}

# Request class attributes and methods
Request_requestId: Property = Property(name="requestId", type=StringType)
Request_leaveApplication: Property = Property(name="leaveApplication", type=LeaveApplication)
Request.attributes={Request_leaveApplication, Request_requestId}

# ApplyLeaveRequest class attributes and methods

# CancelLeaveRequest class attributes and methods

# LeaveStatusQuery class attributes and methods

# LoginAction class attributes and methods
LoginAction_student: Property = Property(name="student", type=Student)
LoginAction.attributes={LoginAction_student}

# CreateUserAction class attributes and methods
CreateUserAction_employee: Property = Property(name="employee", type=Employee_Actor)
CreateUserAction.attributes={CreateUserAction_employee}

# UpdateCalendar class attributes and methods

# ApplicationUtils class attributes and methods

# Relationships
Employee_Apply_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Apply_Leave",
    ends={
        Property(name="apply_Leave8", type=Apply_Leave_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee9", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Leave_Request_Status: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave_Request_Status",
    ends={
        Property(name="leave_Request_Status10", type=Leave_Request_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee11", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Approver_Jobs: BinaryAssociation = BinaryAssociation(
    name="Employee_Approver_Jobs",
    ends={
        Property(name="approver_Jobs12", type=Approver_Jobs_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee13", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_CreateUser: BinaryAssociation = BinaryAssociation(
    name="Admin_CreateUser",
    ends={
        Property(name="createUser14", type=CreateUser_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Update_Calendar: BinaryAssociation = BinaryAssociation(
    name="Admin_Update_Calendar",
    ends={
        Property(name="update_Calendar16", type=Update_Calendar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login0", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Query_Eligibility: BinaryAssociation = BinaryAssociation(
    name="User_Query_Eligibility",
    ends={
        Property(name="query_Eligibility2", type=Query_Eligibility_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Query_Leave_Balance: BinaryAssociation = BinaryAssociation(
    name="User_Query_Leave_Balance",
    ends={
        Property(name="query_Leave_Balance4", type=Query_Leave_Balance_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Query_Leave_History: BinaryAssociation = BinaryAssociation(
    name="User_Query_Leave_History",
    ends={
        Property(name="query_Leave_History6", type=Query_Leave_History_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Application_SendNotification: BinaryAssociation = BinaryAssociation(
    name="Application_SendNotification",
    ends={
        Property(name="sendNotification18", type=SendNotification_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="application19", type=Application_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Credit_Leaves_Application: BinaryAssociation = BinaryAssociation(
    name="Credit_Leaves_Application",
    ends={
        Property(name="application20", type=Application_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="credit_Leaves21", type=Credit_Leaves_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Application_AutoApproval: BinaryAssociation = BinaryAssociation(
    name="Application_AutoApproval",
    ends={
        Property(name="autoApproval22", type=AutoApproval_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="application23", type=Application_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Application_GenerateSummary: BinaryAssociation = BinaryAssociation(
    name="Application_GenerateSummary",
    ends={
        Property(name="generateSummary24", type=GenerateSummary_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="application25", type=Application_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f1ad1903_73e5_43c1_8e2c_7b66bbde119d",
    types={Login_UseCase, Employee_Actor, Change_Password_UseCase, Query_Eligibility_UseCase, Query_Leave_Balance_UseCase, Query_Leave_History_UseCase, Apply_Leave_UseCase, Leave_Request_Status_UseCase, Withdraw_Application_UseCase, Approver_Jobs_UseCase, Approve_RejectRequests_UseCase, Cancel_Leaves_UseCase, Admin_Actor, CreateUser_UseCase, Update_Calendar_UseCase, Application_Actor, SendNotification_UseCase, Credit_Leaves_UseCase, AutoApproval_UseCase, GenerateSummary_UseCase, Student, Query, LeaveBalanceQuery, LeaveHistoryQuery, LeaveApplication, Request, ApplyLeaveRequest, CancelLeaveRequest, LeaveStatusQuery, LoginAction, CreateUserAction, UpdateCalendar, ApplicationUtils},
    associations={Employee_Apply_Leave, Employee_Leave_Request_Status, Employee_Approver_Jobs, Admin_CreateUser, Admin_Update_Calendar, User_Login, User_Query_Eligibility, User_Query_Leave_Balance, User_Query_Leave_History, Application_SendNotification, Credit_Leaves_Application, Application_AutoApproval, Application_GenerateSummary},
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