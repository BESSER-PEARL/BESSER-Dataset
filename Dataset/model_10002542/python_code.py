from __future__ import annotations
from datetime import datetime, date, time
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



class LeaveStatusQuery:

    pass


class CancelLeaveRequest:

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

    def __init__(self, applicationId: str, fromDate: date, toDate: date, reason: str, studentId: str, status: str, approverComments: str):
        self.applicationId = applicationId
        self.fromDate = fromDate
        self.toDate = toDate
        self.reason = reason
        self.studentId = studentId
        self.status = status
        self.approverComments = approverComments
        
        pass
    @property
    def toDate(self):
        return self.__toDate
    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate

    @property
    def reason(self):
        return self.__reason
    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def fromDate(self):
        return self.__fromDate
    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate

    @property
    def studentId(self):
        return self.__studentId
    @studentId.setter
    def studentId(self, studentId: str):
        self.__studentId = studentId

    @property
    def approverComments(self):
        return self.__approverComments
    @approverComments.setter
    def approverComments(self, approverComments: str):
        self.__approverComments = approverComments

    @property
    def applicationId(self):
        return self.__applicationId
    @applicationId.setter
    def applicationId(self, applicationId: str):
        self.__applicationId = applicationId



class LeaveHistoryQuery:

    def __init__(self, fromDate: date, toDate: date):
        self.fromDate = fromDate
        self.toDate = toDate
        
        pass
    @property
    def toDate(self):
        return self.__toDate
    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate

    @property
    def fromDate(self):
        return self.__fromDate
    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate



class LeaveBalanceQuery:

    pass


class EligibilityQuery:

    pass


class Query:

    def __init__(self, requestId: str, user: Student):
        self.requestId = requestId
        self.user = user
        
        pass
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: Student):
        self.__user = user

    @property
    def requestId(self):
        return self.__requestId
    @requestId.setter
    def requestId(self, requestId: str):
        self.__requestId = requestId



class Student:

    def __init__(self, branch: str, year: int, password: str, leavesTaken: str, studentId: str, studentName: str):
        self.branch = branch
        self.year = year
        self.password = password
        self.leavesTaken = leavesTaken
        self.studentId = studentId
        self.studentName = studentName
        
        pass
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def leavesTaken(self):
        return self.__leavesTaken
    @leavesTaken.setter
    def leavesTaken(self, leavesTaken: str):
        self.__leavesTaken = leavesTaken

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def studentName(self):
        return self.__studentName
    @studentName.setter
    def studentName(self, studentName: str):
        self.__studentName = studentName

    @property
    def studentId(self):
        return self.__studentId
    @studentId.setter
    def studentId(self, studentId: str):
        self.__studentId = studentId

