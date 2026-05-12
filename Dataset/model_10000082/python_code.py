from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class LeaveStatus(Enum):
    pass

############################################
# Definition of Classes
############################################







class GenerateSummary_UseCase:

    pass


class AutoApproval_UseCase:

    pass


class Credit_Leaves_UseCase:

    pass


class SendNotification_UseCase:

    pass


class Application_Actor:

    pass


class Update_Calendar_UseCase:

    pass


class CreateUser_UseCase:

    pass


class Admin_Actor:

    pass


class Cancel_Leaves_UseCase:

    pass


class Approve_RejectRequests_UseCase:

    pass


class Approver_Jobs_UseCase:

    pass


class Withdraw_Application_UseCase:

    pass


class Leave_Request_Status_UseCase:

    pass


class Apply_Leave_UseCase:

    pass


class Query_Leave_History_UseCase:

    pass


class Query_Leave_Balance_UseCase:

    pass


class Query_Eligibility_UseCase:

    pass


class Change_Password_UseCase:

    pass


class Employee_Actor:

    pass


class Login_UseCase:

    pass





class ApplicationUtils:

    pass


class UpdateCalendar:

    pass


class CreateUserAction:

    def __init__(self, employee: Employee_Actor):
        self.employee = employee
        
        pass
    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self, employee: Employee_Actor):
        self.__employee = employee



class LoginAction:

    def __init__(self, employee: Employee_Actor):
        self.employee = employee
        
        pass
    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self, employee: Employee_Actor):
        self.__employee = employee



class ApproveOrRejectStatus:

    pass


class LeaveStatusQuery:

    pass


class CancelLeaveRequest:

    pass


class WithdrawLeaveRequest:

    pass


class ApplyLeaveRequest:

    pass


class Request:

    def __init__(self, requestId: str, leaveApplication: LeaveApplication):
        self.requestId = requestId
        self.leaveApplication = leaveApplication
        
        pass
    @property
    def requestId(self):
        return self.__requestId
    @requestId.setter
    def requestId(self, requestId: str):
        self.__requestId = requestId

    @property
    def leaveApplication(self):
        return self.__leaveApplication
    @leaveApplication.setter
    def leaveApplication(self, leaveApplication: LeaveApplication):
        self.__leaveApplication = leaveApplication



class LeaveApplication:

    def __init__(self, applicationId: str, fromDate: date, toDate: date, reason: str, employeeId: str, status: str, approverComments: str):
        self.applicationId = applicationId
        self.fromDate = fromDate
        self.toDate = toDate
        self.reason = reason
        self.employeeId = employeeId
        self.status = status
        self.approverComments = approverComments
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def applicationId(self):
        return self.__applicationId
    @applicationId.setter
    def applicationId(self, applicationId: str):
        self.__applicationId = applicationId

    @property
    def reason(self):
        return self.__reason
    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

    @property
    def employeeId(self):
        return self.__employeeId
    @employeeId.setter
    def employeeId(self, employeeId: str):
        self.__employeeId = employeeId

    @property
    def fromDate(self):
        return self.__fromDate
    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate

    @property
    def toDate(self):
        return self.__toDate
    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate

    @property
    def approverComments(self):
        return self.__approverComments
    @approverComments.setter
    def approverComments(self, approverComments: str):
        self.__approverComments = approverComments



class LeaveHistoryQuery:

    def __init__(self, fromDate: date, toDate: date):
        self.fromDate = fromDate
        self.toDate = toDate
        
        pass
    @property
    def fromDate(self):
        return self.__fromDate
    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate

    @property
    def toDate(self):
        return self.__toDate
    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate



class LeaveBalanceQuery:

    pass


class EligibilityQuery:

    pass


class Query:

    def __init__(self, requestId: str, user: Employee_Actor):
        self.requestId = requestId
        self.user = user
        
        pass
    @property
    def requestId(self):
        return self.__requestId
    @requestId.setter
    def requestId(self, requestId: str):
        self.__requestId = requestId

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: Employee_Actor):
        self.__user = user



class Employee:

    def __init__(self, employeeId: str, employeeName: str, jobLevel: int, password: str, managerId: str, noOfLeaves: int, leavesTaken: str):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.jobLevel = jobLevel
        self.password = password
        self.managerId = managerId
        self.noOfLeaves = noOfLeaves
        self.leavesTaken = leavesTaken
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def employeeName(self):
        return self.__employeeName
    @employeeName.setter
    def employeeName(self, employeeName: str):
        self.__employeeName = employeeName

    @property
    def noOfLeaves(self):
        return self.__noOfLeaves
    @noOfLeaves.setter
    def noOfLeaves(self, noOfLeaves: int):
        self.__noOfLeaves = noOfLeaves

    @property
    def jobLevel(self):
        return self.__jobLevel
    @jobLevel.setter
    def jobLevel(self, jobLevel: int):
        self.__jobLevel = jobLevel

    @property
    def managerId(self):
        return self.__managerId
    @managerId.setter
    def managerId(self, managerId: str):
        self.__managerId = managerId

    @property
    def employeeId(self):
        return self.__employeeId
    @employeeId.setter
    def employeeId(self, employeeId: str):
        self.__employeeId = employeeId

    @property
    def leavesTaken(self):
        return self.__leavesTaken
    @leavesTaken.setter
    def leavesTaken(self, leavesTaken: str):
        self.__leavesTaken = leavesTaken

