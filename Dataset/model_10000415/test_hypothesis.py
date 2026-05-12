import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class_Diagram_for_Propsed_System_ETF,
    Class_Diagram_for_Propsed_System_User_Permissions,
    Class_Diagram_for_Propsed_System_Messages,
    Class_Diagram_for_Propsed_System_Advances,
    Class_Diagram_for_Propsed_System_UserUpdates,
    Class_Diagram_for_Propsed_System_Users,
    Class_Diagram_for_Propsed_System_User_groups,
    Class_Diagram_for_Propsed_System_OT_Requests,
    Class_Diagram_for_Propsed_System_LeaveProfiles,
    Class_Diagram_for_Propsed_System_Leave_Taken,
    Class_Diagram_for_Propsed_System_Event,
    Class_Diagram_for_Propsed_System_EPF,
    Class_Diagram_for_Propsed_System_EmployeeSalary,
    Class_Diagram_for_Propsed_System_EmployeeParoll,
    Class_Diagram_for_Propsed_System_Employee,
    Class_Diagram_for_Propsed_System_Posts,
    Class_Diagram_for_Propsed_System_Shifts,
    Class_Diagram_for_Propsed_System_Departments,
    Class_Diagram_for_Propsed_System_Deductions,
    Class_Diagram_for_Propsed_System_AllowanceTypes,
    Class_Diagram_for_Propsed_System_DeuctionTypes,
    Class_Diagram_for_Propsed_System_Attendance,
    Class_Diagram_for_Propsed_System_Allowance,
    Package_ETF,
    Package_User_Permissions,
    Package_Messages,
    Package_Advances,
    Package_UserUpdates,
    Package_Users,
    Package_User_groups,
    Package_OT_Requests,
    Package_LeaveProfiles,
    Package_Leave_Taken,
    Package_Event,
    Package_EPF,
    Package_EmployeeSalary,
    Package_EmployeeParoll,
    Package_Employee,
    Package_Posts,
    Package_Shifts,
    Package_Departments,
    Package_Deductions,
    Package_AllowanceTypes,
    Package_DeuctionTypes,
    Package_Attendance,
    Package_Allowance,
    Interface_Interface,
    Clark_Actor,
    Admin_Actor,
    Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1,
    Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase,
    Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase,
    Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase,
    Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase,
    Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase,
    Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase,
    Employee_Actor,
    date,
    ot_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_diagram_for_propsed_system_etf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_ETF)


def test_class_diagram_for_propsed_system_etf_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_ETF.__init__)


def test_class_diagram_for_propsed_system_etf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_ETF.__init__)
    params = list(sig.parameters.keys())
    assert "effectivedate" in params, "Missing parameter 'effectivedate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "precentage" in params, "Missing parameter 'precentage'"

def test_class_diagram_for_propsed_system_etf_has_effectivedate():
    assert hasattr(Class_Diagram_for_Propsed_System_ETF, "effectivedate")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_ETF.__mro__:
        if "effectivedate" in klass.__dict__:
            descriptor = klass.__dict__["effectivedate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_etf_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_ETF, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_ETF.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_etf_has_precentage():
    assert hasattr(Class_Diagram_for_Propsed_System_ETF, "precentage")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_ETF.__mro__:
        if "precentage" in klass.__dict__:
            descriptor = klass.__dict__["precentage"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_user_permissions_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_User_Permissions)


def test_class_diagram_for_propsed_system_user_permissions_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_User_Permissions.__init__)


def test_class_diagram_for_propsed_system_user_permissions_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_User_Permissions.__init__)
    params = list(sig.parameters.keys())
    assert "module" in params, "Missing parameter 'module'"
    assert "permissions" in params, "Missing parameter 'permissions'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_user_permissions_has_module():
    assert hasattr(Class_Diagram_for_Propsed_System_User_Permissions, "module")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_User_Permissions.__mro__:
        if "module" in klass.__dict__:
            descriptor = klass.__dict__["module"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_user_permissions_has_permissions():
    assert hasattr(Class_Diagram_for_Propsed_System_User_Permissions, "permissions")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_User_Permissions.__mro__:
        if "permissions" in klass.__dict__:
            descriptor = klass.__dict__["permissions"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_user_permissions_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_User_Permissions, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_User_Permissions.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_messages_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Messages)


def test_class_diagram_for_propsed_system_messages_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Messages.__init__)


def test_class_diagram_for_propsed_system_messages_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Messages.__init__)
    params = list(sig.parameters.keys())
    assert "reciever" in params, "Missing parameter 'reciever'"
    assert "sender" in params, "Missing parameter 'sender'"
    assert "message" in params, "Missing parameter 'message'"
    assert "read_recipt" in params, "Missing parameter 'read_recipt'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_messages_has_reciever():
    assert hasattr(Class_Diagram_for_Propsed_System_Messages, "reciever")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Messages.__mro__:
        if "reciever" in klass.__dict__:
            descriptor = klass.__dict__["reciever"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_messages_has_sender():
    assert hasattr(Class_Diagram_for_Propsed_System_Messages, "sender")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Messages.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_messages_has_message():
    assert hasattr(Class_Diagram_for_Propsed_System_Messages, "message")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Messages.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_messages_has_read_recipt():
    assert hasattr(Class_Diagram_for_Propsed_System_Messages, "read_recipt")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Messages.__mro__:
        if "read_recipt" in klass.__dict__:
            descriptor = klass.__dict__["read_recipt"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_messages_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Messages, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Messages.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_advances_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Advances)


def test_class_diagram_for_propsed_system_advances_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Advances.__init__)


def test_class_diagram_for_propsed_system_advances_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Advances.__init__)
    params = list(sig.parameters.keys())
    assert "installments" in params, "Missing parameter 'installments'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "remain" in params, "Missing parameter 'remain'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_advances_has_installments():
    assert hasattr(Class_Diagram_for_Propsed_System_Advances, "installments")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Advances.__mro__:
        if "installments" in klass.__dict__:
            descriptor = klass.__dict__["installments"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_advances_has_amount():
    assert hasattr(Class_Diagram_for_Propsed_System_Advances, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Advances.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_advances_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_Advances, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Advances.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_advances_has_remain():
    assert hasattr(Class_Diagram_for_Propsed_System_Advances, "remain")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Advances.__mro__:
        if "remain" in klass.__dict__:
            descriptor = klass.__dict__["remain"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_advances_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Advances, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Advances.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_userupdates_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_UserUpdates)


def test_class_diagram_for_propsed_system_userupdates_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_UserUpdates.__init__)


def test_class_diagram_for_propsed_system_userupdates_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_UserUpdates.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_userupdates_has_user_id():
    assert hasattr(Class_Diagram_for_Propsed_System_UserUpdates, "user_id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_UserUpdates.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_userupdates_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_UserUpdates, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_UserUpdates.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_users_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Users)


def test_class_diagram_for_propsed_system_users_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Users.__init__)


def test_class_diagram_for_propsed_system_users_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Users.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "email" in params, "Missing parameter 'email'"

def test_class_diagram_for_propsed_system_users_has_firstname():
    assert hasattr(Class_Diagram_for_Propsed_System_Users, "firstname")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Users.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_users_has_password():
    assert hasattr(Class_Diagram_for_Propsed_System_Users, "password")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Users.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_users_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Users, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Users.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_users_has_lastname():
    assert hasattr(Class_Diagram_for_Propsed_System_Users, "lastname")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Users.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_users_has_email():
    assert hasattr(Class_Diagram_for_Propsed_System_Users, "email")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Users.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_user_groups_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_User_groups)


def test_class_diagram_for_propsed_system_user_groups_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_User_groups.__init__)


def test_class_diagram_for_propsed_system_user_groups_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_User_groups.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "user_group" in params, "Missing parameter 'user_group'"

def test_class_diagram_for_propsed_system_user_groups_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_User_groups, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_User_groups.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_user_groups_has_user_group():
    assert hasattr(Class_Diagram_for_Propsed_System_User_groups, "user_group")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_User_groups.__mro__:
        if "user_group" in klass.__dict__:
            descriptor = klass.__dict__["user_group"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_ot_requests_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_OT_Requests)


def test_class_diagram_for_propsed_system_ot_requests_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_OT_Requests.__init__)


def test_class_diagram_for_propsed_system_ot_requests_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_OT_Requests.__init__)
    params = list(sig.parameters.keys())
    assert "EmpID" in params, "Missing parameter 'EmpID'"
    assert "id" in params, "Missing parameter 'id'"
    assert "OtDay" in params, "Missing parameter 'OtDay'"
    assert "OTType" in params, "Missing parameter 'OTType'"

def test_class_diagram_for_propsed_system_ot_requests_has_EmpID():
    assert hasattr(Class_Diagram_for_Propsed_System_OT_Requests, "EmpID")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_OT_Requests.__mro__:
        if "EmpID" in klass.__dict__:
            descriptor = klass.__dict__["EmpID"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_ot_requests_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_OT_Requests, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_OT_Requests.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_ot_requests_has_OtDay():
    assert hasattr(Class_Diagram_for_Propsed_System_OT_Requests, "OtDay")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_OT_Requests.__mro__:
        if "OtDay" in klass.__dict__:
            descriptor = klass.__dict__["OtDay"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_ot_requests_has_OTType():
    assert hasattr(Class_Diagram_for_Propsed_System_OT_Requests, "OTType")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_OT_Requests.__mro__:
        if "OTType" in klass.__dict__:
            descriptor = klass.__dict__["OTType"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_leaveprofiles_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_LeaveProfiles)


def test_class_diagram_for_propsed_system_leaveprofiles_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_LeaveProfiles.__init__)


def test_class_diagram_for_propsed_system_leaveprofiles_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_LeaveProfiles.__init__)
    params = list(sig.parameters.keys())
    assert "casual" in params, "Missing parameter 'casual'"
    assert "anual" in params, "Missing parameter 'anual'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_leaveprofiles_has_casual():
    assert hasattr(Class_Diagram_for_Propsed_System_LeaveProfiles, "casual")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_LeaveProfiles.__mro__:
        if "casual" in klass.__dict__:
            descriptor = klass.__dict__["casual"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leaveprofiles_has_anual():
    assert hasattr(Class_Diagram_for_Propsed_System_LeaveProfiles, "anual")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_LeaveProfiles.__mro__:
        if "anual" in klass.__dict__:
            descriptor = klass.__dict__["anual"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leaveprofiles_has_name():
    assert hasattr(Class_Diagram_for_Propsed_System_LeaveProfiles, "name")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_LeaveProfiles.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leaveprofiles_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_LeaveProfiles, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_LeaveProfiles.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_leave_taken_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Leave_Taken)


def test_class_diagram_for_propsed_system_leave_taken_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Leave_Taken.__init__)


def test_class_diagram_for_propsed_system_leave_taken_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Leave_Taken.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "enddate" in params, "Missing parameter 'enddate'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "status" in params, "Missing parameter 'status'"
    assert "start_date" in params, "Missing parameter 'start_date'"
    assert "leavetype" in params, "Missing parameter 'leavetype'"

def test_class_diagram_for_propsed_system_leave_taken_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leave_taken_has_enddate():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "enddate")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "enddate" in klass.__dict__:
            descriptor = klass.__dict__["enddate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leave_taken_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leave_taken_has_status():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "status")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leave_taken_has_start_date():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "start_date")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_leave_taken_has_leavetype():
    assert hasattr(Class_Diagram_for_Propsed_System_Leave_Taken, "leavetype")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Leave_Taken.__mro__:
        if "leavetype" in klass.__dict__:
            descriptor = klass.__dict__["leavetype"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_event_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Event)


def test_class_diagram_for_propsed_system_event_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Event.__init__)


def test_class_diagram_for_propsed_system_event_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "eventname" in params, "Missing parameter 'eventname'"

def test_class_diagram_for_propsed_system_event_has_type():
    assert hasattr(Class_Diagram_for_Propsed_System_Event, "type")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_event_has_date():
    assert hasattr(Class_Diagram_for_Propsed_System_Event, "date")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_event_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Event, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_event_has_eventname():
    assert hasattr(Class_Diagram_for_Propsed_System_Event, "eventname")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Event.__mro__:
        if "eventname" in klass.__dict__:
            descriptor = klass.__dict__["eventname"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_epf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_EPF)


def test_class_diagram_for_propsed_system_epf_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_EPF.__init__)


def test_class_diagram_for_propsed_system_epf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "effectve_date" in params, "Missing parameter 'effectve_date'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_epf_has_precentage():
    assert hasattr(Class_Diagram_for_Propsed_System_EPF, "precentage")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EPF.__mro__:
        if "precentage" in klass.__dict__:
            descriptor = klass.__dict__["precentage"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_epf_has_effectve_date():
    assert hasattr(Class_Diagram_for_Propsed_System_EPF, "effectve_date")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EPF.__mro__:
        if "effectve_date" in klass.__dict__:
            descriptor = klass.__dict__["effectve_date"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_epf_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_EPF, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EPF.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_employeesalary_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_EmployeeSalary)


def test_class_diagram_for_propsed_system_employeesalary_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_EmployeeSalary.__init__)


def test_class_diagram_for_propsed_system_employeesalary_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_EmployeeSalary.__init__)
    params = list(sig.parameters.keys())
    assert "allowances" in params, "Missing parameter 'allowances'"
    assert "basic_salary" in params, "Missing parameter 'basic_salary'"
    assert "id" in params, "Missing parameter 'id'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "deductions" in params, "Missing parameter 'deductions'"

def test_class_diagram_for_propsed_system_employeesalary_has_allowances():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeSalary, "allowances")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeSalary.__mro__:
        if "allowances" in klass.__dict__:
            descriptor = klass.__dict__["allowances"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeesalary_has_basic_salary():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeSalary, "basic_salary")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeSalary.__mro__:
        if "basic_salary" in klass.__dict__:
            descriptor = klass.__dict__["basic_salary"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeesalary_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeSalary, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeSalary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeesalary_has_emp_id():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeSalary, "emp_id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeSalary.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeesalary_has_deductions():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeSalary, "deductions")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeSalary.__mro__:
        if "deductions" in klass.__dict__:
            descriptor = klass.__dict__["deductions"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_employeeparoll_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_EmployeeParoll)


def test_class_diagram_for_propsed_system_employeeparoll_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_EmployeeParoll.__init__)


def test_class_diagram_for_propsed_system_employeeparoll_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_EmployeeParoll.__init__)
    params = list(sig.parameters.keys())
    assert "etf" in params, "Missing parameter 'etf'"
    assert "otamount" in params, "Missing parameter 'otamount'"
    assert "epf" in params, "Missing parameter 'epf'"
    assert "id" in params, "Missing parameter 'id'"
    assert "dotamount" in params, "Missing parameter 'dotamount'"
    assert "lateamount" in params, "Missing parameter 'lateamount'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "basicslaray" in params, "Missing parameter 'basicslaray'"

def test_class_diagram_for_propsed_system_employeeparoll_has_etf():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "etf")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "etf" in klass.__dict__:
            descriptor = klass.__dict__["etf"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_otamount():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "otamount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "otamount" in klass.__dict__:
            descriptor = klass.__dict__["otamount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_epf():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "epf")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "epf" in klass.__dict__:
            descriptor = klass.__dict__["epf"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_dotamount():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "dotamount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "dotamount" in klass.__dict__:
            descriptor = klass.__dict__["dotamount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_lateamount():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "lateamount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "lateamount" in klass.__dict__:
            descriptor = klass.__dict__["lateamount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employeeparoll_has_basicslaray():
    assert hasattr(Class_Diagram_for_Propsed_System_EmployeeParoll, "basicslaray")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_EmployeeParoll.__mro__:
        if "basicslaray" in klass.__dict__:
            descriptor = klass.__dict__["basicslaray"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_employee_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Employee)


def test_class_diagram_for_propsed_system_employee_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Employee.__init__)


def test_class_diagram_for_propsed_system_employee_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "post" in params, "Missing parameter 'post'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "leavegroup" in params, "Missing parameter 'leavegroup'"
    assert "usergroup" in params, "Missing parameter 'usergroup'"
    assert "depid" in params, "Missing parameter 'depid'"

def test_class_diagram_for_propsed_system_employee_has_shift():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "shift")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "shift" in klass.__dict__:
            descriptor = klass.__dict__["shift"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_mobile():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "mobile")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "mobile" in klass.__dict__:
            descriptor = klass.__dict__["mobile"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_post():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "post")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "post" in klass.__dict__:
            descriptor = klass.__dict__["post"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_user_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "user_id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_leavegroup():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "leavegroup")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "leavegroup" in klass.__dict__:
            descriptor = klass.__dict__["leavegroup"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_usergroup():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "usergroup")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "usergroup" in klass.__dict__:
            descriptor = klass.__dict__["usergroup"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_employee_has_depid():
    assert hasattr(Class_Diagram_for_Propsed_System_Employee, "depid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Employee.__mro__:
        if "depid" in klass.__dict__:
            descriptor = klass.__dict__["depid"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_posts_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Posts)


def test_class_diagram_for_propsed_system_posts_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Posts.__init__)


def test_class_diagram_for_propsed_system_posts_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Posts.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "department_id" in params, "Missing parameter 'department_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_posts_has_name():
    assert hasattr(Class_Diagram_for_Propsed_System_Posts, "name")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Posts.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_posts_has_department_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Posts, "department_id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Posts.__mro__:
        if "department_id" in klass.__dict__:
            descriptor = klass.__dict__["department_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_posts_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Posts, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Posts.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_shifts_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Shifts)


def test_class_diagram_for_propsed_system_shifts_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Shifts.__init__)


def test_class_diagram_for_propsed_system_shifts_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Shifts.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "endtime" in params, "Missing parameter 'endtime'"
    assert "starttime" in params, "Missing parameter 'starttime'"
    assert "shiftaname" in params, "Missing parameter 'shiftaname'"

def test_class_diagram_for_propsed_system_shifts_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Shifts, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Shifts.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_shifts_has_endtime():
    assert hasattr(Class_Diagram_for_Propsed_System_Shifts, "endtime")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Shifts.__mro__:
        if "endtime" in klass.__dict__:
            descriptor = klass.__dict__["endtime"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_shifts_has_starttime():
    assert hasattr(Class_Diagram_for_Propsed_System_Shifts, "starttime")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Shifts.__mro__:
        if "starttime" in klass.__dict__:
            descriptor = klass.__dict__["starttime"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_shifts_has_shiftaname():
    assert hasattr(Class_Diagram_for_Propsed_System_Shifts, "shiftaname")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Shifts.__mro__:
        if "shiftaname" in klass.__dict__:
            descriptor = klass.__dict__["shiftaname"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_departments_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Departments)


def test_class_diagram_for_propsed_system_departments_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Departments.__init__)


def test_class_diagram_for_propsed_system_departments_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Departments.__init__)
    params = list(sig.parameters.keys())
    assert "depname" in params, "Missing parameter 'depname'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_propsed_system_departments_has_depname():
    assert hasattr(Class_Diagram_for_Propsed_System_Departments, "depname")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Departments.__mro__:
        if "depname" in klass.__dict__:
            descriptor = klass.__dict__["depname"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_departments_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Departments, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Departments.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_deductions_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Deductions)


def test_class_diagram_for_propsed_system_deductions_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Deductions.__init__)


def test_class_diagram_for_propsed_system_deductions_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Deductions.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_class_diagram_for_propsed_system_deductions_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Deductions, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Deductions.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_deductions_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_Deductions, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Deductions.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_deductions_has_amount():
    assert hasattr(Class_Diagram_for_Propsed_System_Deductions, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Deductions.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_allowancetypes_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_AllowanceTypes)


def test_class_diagram_for_propsed_system_allowancetypes_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_AllowanceTypes.__init__)


def test_class_diagram_for_propsed_system_allowancetypes_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_AllowanceTypes.__init__)
    params = list(sig.parameters.keys())
    assert "date_added" in params, "Missing parameter 'date_added'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_class_diagram_for_propsed_system_allowancetypes_has_date_added():
    assert hasattr(Class_Diagram_for_Propsed_System_AllowanceTypes, "date_added")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_AllowanceTypes.__mro__:
        if "date_added" in klass.__dict__:
            descriptor = klass.__dict__["date_added"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_allowancetypes_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_AllowanceTypes, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_AllowanceTypes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_allowancetypes_has_type():
    assert hasattr(Class_Diagram_for_Propsed_System_AllowanceTypes, "type")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_AllowanceTypes.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_deuctiontypes_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_DeuctionTypes)


def test_class_diagram_for_propsed_system_deuctiontypes_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_DeuctionTypes.__init__)


def test_class_diagram_for_propsed_system_deuctiontypes_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_DeuctionTypes.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_class_diagram_for_propsed_system_deuctiontypes_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_DeuctionTypes, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_DeuctionTypes.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_deuctiontypes_has_type():
    assert hasattr(Class_Diagram_for_Propsed_System_DeuctionTypes, "type")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_DeuctionTypes.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_attendance_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Attendance)


def test_class_diagram_for_propsed_system_attendance_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Attendance.__init__)


def test_class_diagram_for_propsed_system_attendance_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "timein" in params, "Missing parameter 'timein'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_class_diagram_for_propsed_system_attendance_has_timein():
    assert hasattr(Class_Diagram_for_Propsed_System_Attendance, "timein")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Attendance.__mro__:
        if "timein" in klass.__dict__:
            descriptor = klass.__dict__["timein"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_attendance_has_empid():
    assert hasattr(Class_Diagram_for_Propsed_System_Attendance, "empid")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Attendance.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_attendance_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Attendance, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Attendance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_attendance_has_timeout():
    assert hasattr(Class_Diagram_for_Propsed_System_Attendance, "timeout")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Attendance.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_propsed_system_allowance_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Propsed_System_Allowance)


def test_class_diagram_for_propsed_system_allowance_constructor_exists():
    assert callable(Class_Diagram_for_Propsed_System_Allowance.__init__)


def test_class_diagram_for_propsed_system_allowance_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Propsed_System_Allowance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "effectivedate" in params, "Missing parameter 'effectivedate'"

def test_class_diagram_for_propsed_system_allowance_has_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Allowance, "id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Allowance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_allowance_has_amount():
    assert hasattr(Class_Diagram_for_Propsed_System_Allowance, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Allowance.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_allowance_has_emp_id():
    assert hasattr(Class_Diagram_for_Propsed_System_Allowance, "emp_id")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Allowance.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_propsed_system_allowance_has_effectivedate():
    assert hasattr(Class_Diagram_for_Propsed_System_Allowance, "effectivedate")
    descriptor = None
    for klass in Class_Diagram_for_Propsed_System_Allowance.__mro__:
        if "effectivedate" in klass.__dict__:
            descriptor = klass.__dict__["effectivedate"]
            break
    assert isinstance(descriptor, property)



def test_package_etf_is_not_abstract():
    assert not inspect.isabstract(Package_ETF)


def test_package_etf_constructor_exists():
    assert callable(Package_ETF.__init__)


def test_package_etf_constructor_args():
    sig = inspect.signature(Package_ETF.__init__)
    params = list(sig.parameters.keys())



def test_package_user_permissions_is_not_abstract():
    assert not inspect.isabstract(Package_User_Permissions)


def test_package_user_permissions_constructor_exists():
    assert callable(Package_User_Permissions.__init__)


def test_package_user_permissions_constructor_args():
    sig = inspect.signature(Package_User_Permissions.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_user_permissions_has_attribute():
    assert hasattr(Package_User_Permissions, "attribute")
    descriptor = None
    for klass in Package_User_Permissions.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_user_permissions_has_attribute2():
    assert hasattr(Package_User_Permissions, "attribute2")
    descriptor = None
    for klass in Package_User_Permissions.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_messages_is_not_abstract():
    assert not inspect.isabstract(Package_Messages)


def test_package_messages_constructor_exists():
    assert callable(Package_Messages.__init__)


def test_package_messages_constructor_args():
    sig = inspect.signature(Package_Messages.__init__)
    params = list(sig.parameters.keys())



def test_package_advances_is_not_abstract():
    assert not inspect.isabstract(Package_Advances)


def test_package_advances_constructor_exists():
    assert callable(Package_Advances.__init__)


def test_package_advances_constructor_args():
    sig = inspect.signature(Package_Advances.__init__)
    params = list(sig.parameters.keys())



def test_package_userupdates_is_not_abstract():
    assert not inspect.isabstract(Package_UserUpdates)


def test_package_userupdates_constructor_exists():
    assert callable(Package_UserUpdates.__init__)


def test_package_userupdates_constructor_args():
    sig = inspect.signature(Package_UserUpdates.__init__)
    params = list(sig.parameters.keys())



def test_package_users_is_not_abstract():
    assert not inspect.isabstract(Package_Users)


def test_package_users_constructor_exists():
    assert callable(Package_Users.__init__)


def test_package_users_constructor_args():
    sig = inspect.signature(Package_Users.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_package_users_has_firstname():
    assert hasattr(Package_Users, "firstname")
    descriptor = None
    for klass in Package_Users.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_package_users_has_password():
    assert hasattr(Package_Users, "password")
    descriptor = None
    for klass in Package_Users.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_package_users_has_id():
    assert hasattr(Package_Users, "id")
    descriptor = None
    for klass in Package_Users.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_package_users_has_email():
    assert hasattr(Package_Users, "email")
    descriptor = None
    for klass in Package_Users.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_package_users_has_lastname():
    assert hasattr(Package_Users, "lastname")
    descriptor = None
    for klass in Package_Users.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_package_user_groups_is_not_abstract():
    assert not inspect.isabstract(Package_User_groups)


def test_package_user_groups_constructor_exists():
    assert callable(Package_User_groups.__init__)


def test_package_user_groups_constructor_args():
    sig = inspect.signature(Package_User_groups.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_package_user_groups_has_attribute2():
    assert hasattr(Package_User_groups, "attribute2")
    descriptor = None
    for klass in Package_User_groups.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_package_user_groups_has_attribute3():
    assert hasattr(Package_User_groups, "attribute3")
    descriptor = None
    for klass in Package_User_groups.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_package_user_groups_has_attribute():
    assert hasattr(Package_User_groups, "attribute")
    descriptor = None
    for klass in Package_User_groups.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_package_ot_requests_is_not_abstract():
    assert not inspect.isabstract(Package_OT_Requests)


def test_package_ot_requests_constructor_exists():
    assert callable(Package_OT_Requests.__init__)


def test_package_ot_requests_constructor_args():
    sig = inspect.signature(Package_OT_Requests.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "EmpID" in params, "Missing parameter 'EmpID'"
    assert "OTType" in params, "Missing parameter 'OTType'"
    assert "OtDay" in params, "Missing parameter 'OtDay'"

def test_package_ot_requests_has_id():
    assert hasattr(Package_OT_Requests, "id")
    descriptor = None
    for klass in Package_OT_Requests.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_package_ot_requests_has_EmpID():
    assert hasattr(Package_OT_Requests, "EmpID")
    descriptor = None
    for klass in Package_OT_Requests.__mro__:
        if "EmpID" in klass.__dict__:
            descriptor = klass.__dict__["EmpID"]
            break
    assert isinstance(descriptor, property)

def test_package_ot_requests_has_OTType():
    assert hasattr(Package_OT_Requests, "OTType")
    descriptor = None
    for klass in Package_OT_Requests.__mro__:
        if "OTType" in klass.__dict__:
            descriptor = klass.__dict__["OTType"]
            break
    assert isinstance(descriptor, property)

def test_package_ot_requests_has_OtDay():
    assert hasattr(Package_OT_Requests, "OtDay")
    descriptor = None
    for klass in Package_OT_Requests.__mro__:
        if "OtDay" in klass.__dict__:
            descriptor = klass.__dict__["OtDay"]
            break
    assert isinstance(descriptor, property)



def test_package_leaveprofiles_is_not_abstract():
    assert not inspect.isabstract(Package_LeaveProfiles)


def test_package_leaveprofiles_constructor_exists():
    assert callable(Package_LeaveProfiles.__init__)


def test_package_leaveprofiles_constructor_args():
    sig = inspect.signature(Package_LeaveProfiles.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_leaveprofiles_has_attribute():
    assert hasattr(Package_LeaveProfiles, "attribute")
    descriptor = None
    for klass in Package_LeaveProfiles.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_leaveprofiles_has_attribute2():
    assert hasattr(Package_LeaveProfiles, "attribute2")
    descriptor = None
    for klass in Package_LeaveProfiles.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_leave_taken_is_not_abstract():
    assert not inspect.isabstract(Package_Leave_Taken)


def test_package_leave_taken_constructor_exists():
    assert callable(Package_Leave_Taken.__init__)


def test_package_leave_taken_constructor_args():
    sig = inspect.signature(Package_Leave_Taken.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_leave_taken_has_attribute():
    assert hasattr(Package_Leave_Taken, "attribute")
    descriptor = None
    for klass in Package_Leave_Taken.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_leave_taken_has_attribute2():
    assert hasattr(Package_Leave_Taken, "attribute2")
    descriptor = None
    for klass in Package_Leave_Taken.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_event_is_not_abstract():
    assert not inspect.isabstract(Package_Event)


def test_package_event_constructor_exists():
    assert callable(Package_Event.__init__)


def test_package_event_constructor_args():
    sig = inspect.signature(Package_Event.__init__)
    params = list(sig.parameters.keys())



def test_package_epf_is_not_abstract():
    assert not inspect.isabstract(Package_EPF)


def test_package_epf_constructor_exists():
    assert callable(Package_EPF.__init__)


def test_package_epf_constructor_args():
    sig = inspect.signature(Package_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "effectve_date" in params, "Missing parameter 'effectve_date'"

def test_package_epf_has_id():
    assert hasattr(Package_EPF, "id")
    descriptor = None
    for klass in Package_EPF.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_package_epf_has_precentage():
    assert hasattr(Package_EPF, "precentage")
    descriptor = None
    for klass in Package_EPF.__mro__:
        if "precentage" in klass.__dict__:
            descriptor = klass.__dict__["precentage"]
            break
    assert isinstance(descriptor, property)

def test_package_epf_has_effectve_date():
    assert hasattr(Package_EPF, "effectve_date")
    descriptor = None
    for klass in Package_EPF.__mro__:
        if "effectve_date" in klass.__dict__:
            descriptor = klass.__dict__["effectve_date"]
            break
    assert isinstance(descriptor, property)



def test_package_employeesalary_is_not_abstract():
    assert not inspect.isabstract(Package_EmployeeSalary)


def test_package_employeesalary_constructor_exists():
    assert callable(Package_EmployeeSalary.__init__)


def test_package_employeesalary_constructor_args():
    sig = inspect.signature(Package_EmployeeSalary.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_employeesalary_has_attribute():
    assert hasattr(Package_EmployeeSalary, "attribute")
    descriptor = None
    for klass in Package_EmployeeSalary.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_employeesalary_has_attribute2():
    assert hasattr(Package_EmployeeSalary, "attribute2")
    descriptor = None
    for klass in Package_EmployeeSalary.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_employeeparoll_is_not_abstract():
    assert not inspect.isabstract(Package_EmployeeParoll)


def test_package_employeeparoll_constructor_exists():
    assert callable(Package_EmployeeParoll.__init__)


def test_package_employeeparoll_constructor_args():
    sig = inspect.signature(Package_EmployeeParoll.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_employeeparoll_has_attribute():
    assert hasattr(Package_EmployeeParoll, "attribute")
    descriptor = None
    for klass in Package_EmployeeParoll.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_employeeparoll_has_attribute2():
    assert hasattr(Package_EmployeeParoll, "attribute2")
    descriptor = None
    for klass in Package_EmployeeParoll.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_employee_is_not_abstract():
    assert not inspect.isabstract(Package_Employee)


def test_package_employee_constructor_exists():
    assert callable(Package_Employee.__init__)


def test_package_employee_constructor_args():
    sig = inspect.signature(Package_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "leavegroup" in params, "Missing parameter 'leavegroup'"
    assert "post" in params, "Missing parameter 'post'"
    assert "id" in params, "Missing parameter 'id'"
    assert "empid" in params, "Missing parameter 'empid'"
    assert "depid" in params, "Missing parameter 'depid'"
    assert "usergroup" in params, "Missing parameter 'usergroup'"
    assert "shift" in params, "Missing parameter 'shift'"

def test_package_employee_has_leavegroup():
    assert hasattr(Package_Employee, "leavegroup")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "leavegroup" in klass.__dict__:
            descriptor = klass.__dict__["leavegroup"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_post():
    assert hasattr(Package_Employee, "post")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "post" in klass.__dict__:
            descriptor = klass.__dict__["post"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_id():
    assert hasattr(Package_Employee, "id")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_empid():
    assert hasattr(Package_Employee, "empid")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_depid():
    assert hasattr(Package_Employee, "depid")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "depid" in klass.__dict__:
            descriptor = klass.__dict__["depid"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_usergroup():
    assert hasattr(Package_Employee, "usergroup")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "usergroup" in klass.__dict__:
            descriptor = klass.__dict__["usergroup"]
            break
    assert isinstance(descriptor, property)

def test_package_employee_has_shift():
    assert hasattr(Package_Employee, "shift")
    descriptor = None
    for klass in Package_Employee.__mro__:
        if "shift" in klass.__dict__:
            descriptor = klass.__dict__["shift"]
            break
    assert isinstance(descriptor, property)



def test_package_posts_is_not_abstract():
    assert not inspect.isabstract(Package_Posts)


def test_package_posts_constructor_exists():
    assert callable(Package_Posts.__init__)


def test_package_posts_constructor_args():
    sig = inspect.signature(Package_Posts.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_package_posts_has_attribute():
    assert hasattr(Package_Posts, "attribute")
    descriptor = None
    for klass in Package_Posts.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_package_posts_has_attribute2():
    assert hasattr(Package_Posts, "attribute2")
    descriptor = None
    for klass in Package_Posts.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_package_shifts_is_not_abstract():
    assert not inspect.isabstract(Package_Shifts)


def test_package_shifts_constructor_exists():
    assert callable(Package_Shifts.__init__)


def test_package_shifts_constructor_args():
    sig = inspect.signature(Package_Shifts.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_package_shifts_has_attribute2():
    assert hasattr(Package_Shifts, "attribute2")
    descriptor = None
    for klass in Package_Shifts.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_package_shifts_has_attribute():
    assert hasattr(Package_Shifts, "attribute")
    descriptor = None
    for klass in Package_Shifts.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_package_departments_is_not_abstract():
    assert not inspect.isabstract(Package_Departments)


def test_package_departments_constructor_exists():
    assert callable(Package_Departments.__init__)


def test_package_departments_constructor_args():
    sig = inspect.signature(Package_Departments.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_package_departments_has_id():
    assert hasattr(Package_Departments, "id")
    descriptor = None
    for klass in Package_Departments.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_package_deductions_is_not_abstract():
    assert not inspect.isabstract(Package_Deductions)


def test_package_deductions_constructor_exists():
    assert callable(Package_Deductions.__init__)


def test_package_deductions_constructor_args():
    sig = inspect.signature(Package_Deductions.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_package_deductions_has_attribute2():
    assert hasattr(Package_Deductions, "attribute2")
    descriptor = None
    for klass in Package_Deductions.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_package_deductions_has_attribute():
    assert hasattr(Package_Deductions, "attribute")
    descriptor = None
    for klass in Package_Deductions.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_package_allowancetypes_is_not_abstract():
    assert not inspect.isabstract(Package_AllowanceTypes)


def test_package_allowancetypes_constructor_exists():
    assert callable(Package_AllowanceTypes.__init__)


def test_package_allowancetypes_constructor_args():
    sig = inspect.signature(Package_AllowanceTypes.__init__)
    params = list(sig.parameters.keys())



def test_package_deuctiontypes_is_not_abstract():
    assert not inspect.isabstract(Package_DeuctionTypes)


def test_package_deuctiontypes_constructor_exists():
    assert callable(Package_DeuctionTypes.__init__)


def test_package_deuctiontypes_constructor_args():
    sig = inspect.signature(Package_DeuctionTypes.__init__)
    params = list(sig.parameters.keys())



def test_package_attendance_is_not_abstract():
    assert not inspect.isabstract(Package_Attendance)


def test_package_attendance_constructor_exists():
    assert callable(Package_Attendance.__init__)


def test_package_attendance_constructor_args():
    sig = inspect.signature(Package_Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "empid" in params, "Missing parameter 'empid'"
    assert "timein" in params, "Missing parameter 'timein'"
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "id" in params, "Missing parameter 'id'"

def test_package_attendance_has_empid():
    assert hasattr(Package_Attendance, "empid")
    descriptor = None
    for klass in Package_Attendance.__mro__:
        if "empid" in klass.__dict__:
            descriptor = klass.__dict__["empid"]
            break
    assert isinstance(descriptor, property)

def test_package_attendance_has_timein():
    assert hasattr(Package_Attendance, "timein")
    descriptor = None
    for klass in Package_Attendance.__mro__:
        if "timein" in klass.__dict__:
            descriptor = klass.__dict__["timein"]
            break
    assert isinstance(descriptor, property)

def test_package_attendance_has_timeout():
    assert hasattr(Package_Attendance, "timeout")
    descriptor = None
    for klass in Package_Attendance.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_package_attendance_has_id():
    assert hasattr(Package_Attendance, "id")
    descriptor = None
    for klass in Package_Attendance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_package_allowance_is_not_abstract():
    assert not inspect.isabstract(Package_Allowance)


def test_package_allowance_constructor_exists():
    assert callable(Package_Allowance.__init__)


def test_package_allowance_constructor_args():
    sig = inspect.signature(Package_Allowance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "Effectivedate" in params, "Missing parameter 'Effectivedate'"

def test_package_allowance_has_id():
    assert hasattr(Package_Allowance, "id")
    descriptor = None
    for klass in Package_Allowance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_package_allowance_has_emp_id():
    assert hasattr(Package_Allowance, "emp_id")
    descriptor = None
    for klass in Package_Allowance.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_package_allowance_has_Effectivedate():
    assert hasattr(Package_Allowance, "Effectivedate")
    descriptor = None
    for klass in Package_Allowance.__mro__:
        if "Effectivedate" in klass.__dict__:
            descriptor = klass.__dict__["Effectivedate"]
            break
    assert isinstance(descriptor, property)



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_clark_actor_is_not_abstract():
    assert not inspect.isabstract(Clark_Actor)


def test_clark_actor_constructor_exists():
    assert callable(Clark_Actor.__init__)


def test_clark_actor_constructor_args():
    sig = inspect.signature(Clark_Actor.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_add_new_company_events_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase)


def test_use_case_diagram_for_proposed_system_add_new_company_events_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_add_new_company_events_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_add_employee_time_records_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase)


def test_use_case_diagram_for_proposed_system_add_employee_time_records_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_add_employee_time_records_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_generate_paysheet_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase)


def test_use_case_diagram_for_proposed_system_generate_paysheet_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_generate_paysheet_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_employee_profiles_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase)


def test_use_case_diagram_for_proposed_system_view_employee_profiles_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_employee_profiles_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_add_new_department_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase)


def test_use_case_diagram_for_proposed_system_add_new_department_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_add_new_department_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_add_employee_profile_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase)


def test_use_case_diagram_for_proposed_system_add_employee_profile_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_add_employee_profile_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_reports_usecase1_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1)


def test_use_case_diagram_for_proposed_system_view_reports_usecase1_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1.__init__)


def test_use_case_diagram_for_proposed_system_view_reports_usecase1_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_accept_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase)


def test_use_case_diagram_for_proposed_system_accept_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_accept_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_update_leave_balance_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase)


def test_use_case_diagram_for_proposed_system_update_leave_balance_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_update_leave_balance_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_reject_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase)


def test_use_case_diagram_for_proposed_system_reject_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_reject_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_issue_and_check_appraislas_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase)


def test_use_case_diagram_for_proposed_system_issue_and_check_appraislas_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_issue_and_check_appraislas_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_approve_employee_pay_sheets_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase)


def test_use_case_diagram_for_proposed_system_approve_employee_pay_sheets_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_approve_employee_pay_sheets_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_pay_sheet_history_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase)


def test_use_case_diagram_for_proposed_system_view_pay_sheet_history_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_pay_sheet_history_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_leave_rquest_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase)


def test_use_case_diagram_for_proposed_system_view_leave_rquest_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_leave_rquest_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_employee_time_records_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase)


def test_use_case_diagram_for_proposed_system_view_employee_time_records_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_employee_time_records_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_set_leave_status_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase)


def test_use_case_diagram_for_proposed_system_set_leave_status_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_set_leave_status_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_set_advances_status_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase)


def test_use_case_diagram_for_proposed_system_set_advances_status_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_set_advances_status_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_request_loan_and_advances_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase)


def test_use_case_diagram_for_proposed_system_request_loan_and_advances_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_request_loan_and_advances_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_request_leaves_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase)


def test_use_case_diagram_for_proposed_system_request_leaves_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_request_leaves_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_reports_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase)


def test_use_case_diagram_for_proposed_system_view_reports_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_reports_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_personal_time_records_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase)


def test_use_case_diagram_for_proposed_system_view_personal_time_records_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_personal_time_records_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_leave_status_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase)


def test_use_case_diagram_for_proposed_system_view_leave_status_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_leave_status_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_personal_salary_history_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase)


def test_use_case_diagram_for_proposed_system_view_personal_salary_history_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_personal_salary_history_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_proposed_system_view_personal_detais_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase)


def test_use_case_diagram_for_proposed_system_view_personal_detais_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase.__init__)


def test_use_case_diagram_for_proposed_system_view_personal_detais_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())

def test_date_exists():
    # Check that the Enumeration exists
    assert date is not None

def test_date_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in date]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in date"

def test_ot_type_exists():
    # Check that the Enumeration exists
    assert ot_Type is not None

def test_ot_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ot_Type]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ot_Type"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Class_Diagram_for_Propsed_System_ETF_strategy = st.builds(
    Class_Diagram_for_Propsed_System_ETF,
    effectivedate=
        st.dates(),
    id=
        st.integers(),
    precentage=
        safe_text
)
Class_Diagram_for_Propsed_System_User_Permissions_strategy = st.builds(
    Class_Diagram_for_Propsed_System_User_Permissions,
    module=
        st.integers(),
    permissions=
        safe_text,
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Messages_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Messages,
    reciever=
        st.integers(),
    sender=
        st.integers(),
    message=
        safe_text,
    read_recipt=
        safe_text,
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Advances_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Advances,
    installments=
        st.integers(),
    amount=
        safe_text,
    empid=
        st.integers(),
    remain=
        st.integers(),
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_UserUpdates_strategy = st.builds(
    Class_Diagram_for_Propsed_System_UserUpdates,
    user_id=
        st.integers(),
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Users_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Users,
    firstname=
        safe_text,
    password=
        safe_text,
    id=
        st.integers(),
    lastname=
        safe_text,
    email=
        safe_text
)
Class_Diagram_for_Propsed_System_User_groups_strategy = st.builds(
    Class_Diagram_for_Propsed_System_User_groups,
    id=
        st.integers(),
    user_group=
        safe_text
)
Class_Diagram_for_Propsed_System_OT_Requests_strategy = st.builds(
    Class_Diagram_for_Propsed_System_OT_Requests,
    EmpID=
        st.integers(),
    id=
        st.integers(),
    OtDay=
        st.dates(),
    OTType=
        st.integers()
)
Class_Diagram_for_Propsed_System_LeaveProfiles_strategy = st.builds(
    Class_Diagram_for_Propsed_System_LeaveProfiles,
    casual=
        st.integers(),
    anual=
        st.integers(),
    name=
        safe_text,
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Leave_Taken_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Leave_Taken,
    id=
        st.integers(),
    enddate=
        safe_text,
    empid=
        st.integers(),
    status=
        st.integers(),
    start_date=
        safe_text,
    leavetype=
        st.integers()
)
Class_Diagram_for_Propsed_System_Event_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Event,
    type=
        st.integers(),
    date=
        safe_text,
    id=
        st.integers(),
    eventname=
        safe_text
)
Class_Diagram_for_Propsed_System_EPF_strategy = st.builds(
    Class_Diagram_for_Propsed_System_EPF,
    precentage=
        st.integers(),
    effectve_date=
        safe_text,
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_EmployeeSalary_strategy = st.builds(
    Class_Diagram_for_Propsed_System_EmployeeSalary,
    allowances=
        st.booleans(),
    basic_salary=
        safe_text,
    id=
        safe_text,
    emp_id=
        safe_text,
    deductions=
        st.booleans()
)
Class_Diagram_for_Propsed_System_EmployeeParoll_strategy = st.builds(
    Class_Diagram_for_Propsed_System_EmployeeParoll,
    etf=
        safe_text,
    otamount=
        safe_text,
    epf=
        safe_text,
    id=
        st.integers(),
    dotamount=
        safe_text,
    lateamount=
        safe_text,
    empid=
        st.integers(),
    basicslaray=
        safe_text
)
Class_Diagram_for_Propsed_System_Employee_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Employee,
    shift=
        st.integers(),
    empid=
        st.integers(),
    mobile=
        st.integers(),
    post=
        st.integers(),
    user_id=
        st.integers(),
    id=
        safe_text,
    leavegroup=
        st.integers(),
    usergroup=
        st.integers(),
    depid=
        st.integers()
)
Class_Diagram_for_Propsed_System_Posts_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Posts,
    name=
        safe_text,
    department_id=
        st.integers(),
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Shifts_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Shifts,
    id=
        st.integers(),
    endtime=
        safe_text,
    starttime=
        safe_text,
    shiftaname=
        safe_text
)
Class_Diagram_for_Propsed_System_Departments_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Departments,
    depname=
        safe_text,
    id=
        st.integers()
)
Class_Diagram_for_Propsed_System_Deductions_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Deductions,
    id=
        st.integers(),
    empid=
        st.integers(),
    amount=
        safe_text
)
Class_Diagram_for_Propsed_System_AllowanceTypes_strategy = st.builds(
    Class_Diagram_for_Propsed_System_AllowanceTypes,
    date_added=
        safe_text,
    id=
        st.integers(),
    type=
        st.integers()
)
Class_Diagram_for_Propsed_System_DeuctionTypes_strategy = st.builds(
    Class_Diagram_for_Propsed_System_DeuctionTypes,
    id=
        st.integers(),
    type=
        safe_text
)
Class_Diagram_for_Propsed_System_Attendance_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Attendance,
    timein=
        safe_text,
    empid=
        st.integers(),
    id=
        st.integers(),
    timeout=
        safe_text
)
Class_Diagram_for_Propsed_System_Allowance_strategy = st.builds(
    Class_Diagram_for_Propsed_System_Allowance,
    id=
        st.integers(),
    amount=
        safe_text,
    emp_id=
        st.integers(),
    effectivedate=
        safe_text
)
Package_ETF_strategy = st.builds(
    Package_ETF,
)
Package_User_Permissions_strategy = st.builds(
    Package_User_Permissions,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_Messages_strategy = st.builds(
    Package_Messages,
)
Package_Advances_strategy = st.builds(
    Package_Advances,
)
Package_UserUpdates_strategy = st.builds(
    Package_UserUpdates,
)
Package_Users_strategy = st.builds(
    Package_Users,
    firstname=
        st.integers(),
    password=
        st.integers(),
    id=
        st.integers(),
    email=
        st.integers(),
    lastname=
        st.integers()
)
Package_User_groups_strategy = st.builds(
    Package_User_groups,
    attribute2=
        safe_text,
    attribute3=
        safe_text,
    attribute=
        safe_text
)
Package_OT_Requests_strategy = st.builds(
    Package_OT_Requests,
    id=
        st.integers(),
    EmpID=
        st.integers(),
    OTType=
        st.integers(),
    OtDay=
        st.dates()
)
Package_LeaveProfiles_strategy = st.builds(
    Package_LeaveProfiles,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_Leave_Taken_strategy = st.builds(
    Package_Leave_Taken,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_Event_strategy = st.builds(
    Package_Event,
)
Package_EPF_strategy = st.builds(
    Package_EPF,
    id=
        st.integers(),
    precentage=
        st.integers(),
    effectve_date=
        st.none()
)
Package_EmployeeSalary_strategy = st.builds(
    Package_EmployeeSalary,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_EmployeeParoll_strategy = st.builds(
    Package_EmployeeParoll,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_Employee_strategy = st.builds(
    Package_Employee,
    leavegroup=
        st.integers(),
    post=
        safe_text,
    id=
        safe_text,
    empid=
        safe_text,
    depid=
        st.integers(),
    usergroup=
        st.integers(),
    shift=
        safe_text
)
Package_Posts_strategy = st.builds(
    Package_Posts,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
Package_Shifts_strategy = st.builds(
    Package_Shifts,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
Package_Departments_strategy = st.builds(
    Package_Departments,
    id=
        st.integers()
)
Package_Deductions_strategy = st.builds(
    Package_Deductions,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
Package_AllowanceTypes_strategy = st.builds(
    Package_AllowanceTypes,
)
Package_DeuctionTypes_strategy = st.builds(
    Package_DeuctionTypes,
)
Package_Attendance_strategy = st.builds(
    Package_Attendance,
    empid=
        st.integers(),
    timein=
        safe_text,
    timeout=
        safe_text,
    id=
        st.integers()
)
Package_Allowance_strategy = st.builds(
    Package_Allowance,
    id=
        st.integers(),
    emp_id=
        safe_text,
    Effectivedate=
        safe_text
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Clark_Actor_strategy = st.builds(
    Clark_Actor,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1,
)
Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase,
)
Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase,
)
Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)

@given(instance=Class_Diagram_for_Propsed_System_ETF_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_etf_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_ETF)



@given(instance=Class_Diagram_for_Propsed_System_ETF_strategy)
def test_class_diagram_for_propsed_system_etf_effectivedate_setter(instance):
    original = instance.effectivedate
    instance.effectivedate = original
    assert instance.effectivedate == original



@given(instance=Class_Diagram_for_Propsed_System_ETF_strategy)
def test_class_diagram_for_propsed_system_etf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_ETF_strategy)
def test_class_diagram_for_propsed_system_etf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original

@given(instance=Class_Diagram_for_Propsed_System_User_Permissions_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_user_permissions_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_User_Permissions)



@given(instance=Class_Diagram_for_Propsed_System_User_Permissions_strategy)
def test_class_diagram_for_propsed_system_user_permissions_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original



@given(instance=Class_Diagram_for_Propsed_System_User_Permissions_strategy)
def test_class_diagram_for_propsed_system_user_permissions_permissions_setter(instance):
    original = instance.permissions
    instance.permissions = original
    assert instance.permissions == original



@given(instance=Class_Diagram_for_Propsed_System_User_Permissions_strategy)
def test_class_diagram_for_propsed_system_user_permissions_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_messages_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Messages)



@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
def test_class_diagram_for_propsed_system_messages_reciever_setter(instance):
    original = instance.reciever
    instance.reciever = original
    assert instance.reciever == original



@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
def test_class_diagram_for_propsed_system_messages_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original



@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
def test_class_diagram_for_propsed_system_messages_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
def test_class_diagram_for_propsed_system_messages_read_recipt_setter(instance):
    original = instance.read_recipt
    instance.read_recipt = original
    assert instance.read_recipt == original



@given(instance=Class_Diagram_for_Propsed_System_Messages_strategy)
def test_class_diagram_for_propsed_system_messages_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_advances_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Advances)



@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
def test_class_diagram_for_propsed_system_advances_installments_setter(instance):
    original = instance.installments
    instance.installments = original
    assert instance.installments == original



@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
def test_class_diagram_for_propsed_system_advances_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
def test_class_diagram_for_propsed_system_advances_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
def test_class_diagram_for_propsed_system_advances_remain_setter(instance):
    original = instance.remain
    instance.remain = original
    assert instance.remain == original



@given(instance=Class_Diagram_for_Propsed_System_Advances_strategy)
def test_class_diagram_for_propsed_system_advances_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_UserUpdates_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_userupdates_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_UserUpdates)



@given(instance=Class_Diagram_for_Propsed_System_UserUpdates_strategy)
def test_class_diagram_for_propsed_system_userupdates_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Class_Diagram_for_Propsed_System_UserUpdates_strategy)
def test_class_diagram_for_propsed_system_userupdates_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_users_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Users)



@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
def test_class_diagram_for_propsed_system_users_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
def test_class_diagram_for_propsed_system_users_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
def test_class_diagram_for_propsed_system_users_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
def test_class_diagram_for_propsed_system_users_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Class_Diagram_for_Propsed_System_Users_strategy)
def test_class_diagram_for_propsed_system_users_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Class_Diagram_for_Propsed_System_User_groups_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_user_groups_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_User_groups)



@given(instance=Class_Diagram_for_Propsed_System_User_groups_strategy)
def test_class_diagram_for_propsed_system_user_groups_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_User_groups_strategy)
def test_class_diagram_for_propsed_system_user_groups_user_group_setter(instance):
    original = instance.user_group
    instance.user_group = original
    assert instance.user_group == original

@given(instance=Class_Diagram_for_Propsed_System_OT_Requests_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_ot_requests_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_OT_Requests)



@given(instance=Class_Diagram_for_Propsed_System_OT_Requests_strategy)
def test_class_diagram_for_propsed_system_ot_requests_EmpID_setter(instance):
    original = instance.EmpID
    instance.EmpID = original
    assert instance.EmpID == original



@given(instance=Class_Diagram_for_Propsed_System_OT_Requests_strategy)
def test_class_diagram_for_propsed_system_ot_requests_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_OT_Requests_strategy)
def test_class_diagram_for_propsed_system_ot_requests_OtDay_setter(instance):
    original = instance.OtDay
    instance.OtDay = original
    assert instance.OtDay == original



@given(instance=Class_Diagram_for_Propsed_System_OT_Requests_strategy)
def test_class_diagram_for_propsed_system_ot_requests_OTType_setter(instance):
    original = instance.OTType
    instance.OTType = original
    assert instance.OTType == original

@given(instance=Class_Diagram_for_Propsed_System_LeaveProfiles_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_leaveprofiles_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_LeaveProfiles)



@given(instance=Class_Diagram_for_Propsed_System_LeaveProfiles_strategy)
def test_class_diagram_for_propsed_system_leaveprofiles_casual_setter(instance):
    original = instance.casual
    instance.casual = original
    assert instance.casual == original



@given(instance=Class_Diagram_for_Propsed_System_LeaveProfiles_strategy)
def test_class_diagram_for_propsed_system_leaveprofiles_anual_setter(instance):
    original = instance.anual
    instance.anual = original
    assert instance.anual == original



@given(instance=Class_Diagram_for_Propsed_System_LeaveProfiles_strategy)
def test_class_diagram_for_propsed_system_leaveprofiles_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Diagram_for_Propsed_System_LeaveProfiles_strategy)
def test_class_diagram_for_propsed_system_leaveprofiles_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_leave_taken_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Leave_Taken)



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_enddate_setter(instance):
    original = instance.enddate
    instance.enddate = original
    assert instance.enddate == original



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original



@given(instance=Class_Diagram_for_Propsed_System_Leave_Taken_strategy)
def test_class_diagram_for_propsed_system_leave_taken_leavetype_setter(instance):
    original = instance.leavetype
    instance.leavetype = original
    assert instance.leavetype == original

@given(instance=Class_Diagram_for_Propsed_System_Event_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_event_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Event)



@given(instance=Class_Diagram_for_Propsed_System_Event_strategy)
def test_class_diagram_for_propsed_system_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Class_Diagram_for_Propsed_System_Event_strategy)
def test_class_diagram_for_propsed_system_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Class_Diagram_for_Propsed_System_Event_strategy)
def test_class_diagram_for_propsed_system_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Event_strategy)
def test_class_diagram_for_propsed_system_event_eventname_setter(instance):
    original = instance.eventname
    instance.eventname = original
    assert instance.eventname == original

@given(instance=Class_Diagram_for_Propsed_System_EPF_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_epf_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_EPF)



@given(instance=Class_Diagram_for_Propsed_System_EPF_strategy)
def test_class_diagram_for_propsed_system_epf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Class_Diagram_for_Propsed_System_EPF_strategy)
def test_class_diagram_for_propsed_system_epf_effectve_date_setter(instance):
    original = instance.effectve_date
    instance.effectve_date = original
    assert instance.effectve_date == original



@given(instance=Class_Diagram_for_Propsed_System_EPF_strategy)
def test_class_diagram_for_propsed_system_epf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_employeesalary_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_EmployeeSalary)



@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
def test_class_diagram_for_propsed_system_employeesalary_allowances_setter(instance):
    original = instance.allowances
    instance.allowances = original
    assert instance.allowances == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
def test_class_diagram_for_propsed_system_employeesalary_basic_salary_setter(instance):
    original = instance.basic_salary
    instance.basic_salary = original
    assert instance.basic_salary == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
def test_class_diagram_for_propsed_system_employeesalary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
def test_class_diagram_for_propsed_system_employeesalary_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeSalary_strategy)
def test_class_diagram_for_propsed_system_employeesalary_deductions_setter(instance):
    original = instance.deductions
    instance.deductions = original
    assert instance.deductions == original

@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_employeeparoll_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_EmployeeParoll)



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_etf_setter(instance):
    original = instance.etf
    instance.etf = original
    assert instance.etf == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_otamount_setter(instance):
    original = instance.otamount
    instance.otamount = original
    assert instance.otamount == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_epf_setter(instance):
    original = instance.epf
    instance.epf = original
    assert instance.epf == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_dotamount_setter(instance):
    original = instance.dotamount
    instance.dotamount = original
    assert instance.dotamount == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_lateamount_setter(instance):
    original = instance.lateamount
    instance.lateamount = original
    assert instance.lateamount == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_EmployeeParoll_strategy)
def test_class_diagram_for_propsed_system_employeeparoll_basicslaray_setter(instance):
    original = instance.basicslaray
    instance.basicslaray = original
    assert instance.basicslaray == original

@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_employee_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Employee)



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_post_setter(instance):
    original = instance.post
    instance.post = original
    assert instance.post == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_leavegroup_setter(instance):
    original = instance.leavegroup
    instance.leavegroup = original
    assert instance.leavegroup == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_usergroup_setter(instance):
    original = instance.usergroup
    instance.usergroup = original
    assert instance.usergroup == original



@given(instance=Class_Diagram_for_Propsed_System_Employee_strategy)
def test_class_diagram_for_propsed_system_employee_depid_setter(instance):
    original = instance.depid
    instance.depid = original
    assert instance.depid == original

@given(instance=Class_Diagram_for_Propsed_System_Posts_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_posts_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Posts)



@given(instance=Class_Diagram_for_Propsed_System_Posts_strategy)
def test_class_diagram_for_propsed_system_posts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Diagram_for_Propsed_System_Posts_strategy)
def test_class_diagram_for_propsed_system_posts_department_id_setter(instance):
    original = instance.department_id
    instance.department_id = original
    assert instance.department_id == original



@given(instance=Class_Diagram_for_Propsed_System_Posts_strategy)
def test_class_diagram_for_propsed_system_posts_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Shifts_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_shifts_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Shifts)



@given(instance=Class_Diagram_for_Propsed_System_Shifts_strategy)
def test_class_diagram_for_propsed_system_shifts_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Shifts_strategy)
def test_class_diagram_for_propsed_system_shifts_endtime_setter(instance):
    original = instance.endtime
    instance.endtime = original
    assert instance.endtime == original



@given(instance=Class_Diagram_for_Propsed_System_Shifts_strategy)
def test_class_diagram_for_propsed_system_shifts_starttime_setter(instance):
    original = instance.starttime
    instance.starttime = original
    assert instance.starttime == original



@given(instance=Class_Diagram_for_Propsed_System_Shifts_strategy)
def test_class_diagram_for_propsed_system_shifts_shiftaname_setter(instance):
    original = instance.shiftaname
    instance.shiftaname = original
    assert instance.shiftaname == original

@given(instance=Class_Diagram_for_Propsed_System_Departments_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_departments_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Departments)



@given(instance=Class_Diagram_for_Propsed_System_Departments_strategy)
def test_class_diagram_for_propsed_system_departments_depname_setter(instance):
    original = instance.depname
    instance.depname = original
    assert instance.depname == original



@given(instance=Class_Diagram_for_Propsed_System_Departments_strategy)
def test_class_diagram_for_propsed_system_departments_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Propsed_System_Deductions_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_deductions_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Deductions)



@given(instance=Class_Diagram_for_Propsed_System_Deductions_strategy)
def test_class_diagram_for_propsed_system_deductions_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Deductions_strategy)
def test_class_diagram_for_propsed_system_deductions_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_Deductions_strategy)
def test_class_diagram_for_propsed_system_deductions_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Class_Diagram_for_Propsed_System_AllowanceTypes_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_allowancetypes_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_AllowanceTypes)



@given(instance=Class_Diagram_for_Propsed_System_AllowanceTypes_strategy)
def test_class_diagram_for_propsed_system_allowancetypes_date_added_setter(instance):
    original = instance.date_added
    instance.date_added = original
    assert instance.date_added == original



@given(instance=Class_Diagram_for_Propsed_System_AllowanceTypes_strategy)
def test_class_diagram_for_propsed_system_allowancetypes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_AllowanceTypes_strategy)
def test_class_diagram_for_propsed_system_allowancetypes_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Class_Diagram_for_Propsed_System_DeuctionTypes_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_deuctiontypes_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_DeuctionTypes)



@given(instance=Class_Diagram_for_Propsed_System_DeuctionTypes_strategy)
def test_class_diagram_for_propsed_system_deuctiontypes_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_DeuctionTypes_strategy)
def test_class_diagram_for_propsed_system_deuctiontypes_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Class_Diagram_for_Propsed_System_Attendance_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_attendance_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Attendance)



@given(instance=Class_Diagram_for_Propsed_System_Attendance_strategy)
def test_class_diagram_for_propsed_system_attendance_timein_setter(instance):
    original = instance.timein
    instance.timein = original
    assert instance.timein == original



@given(instance=Class_Diagram_for_Propsed_System_Attendance_strategy)
def test_class_diagram_for_propsed_system_attendance_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Class_Diagram_for_Propsed_System_Attendance_strategy)
def test_class_diagram_for_propsed_system_attendance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Attendance_strategy)
def test_class_diagram_for_propsed_system_attendance_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=Class_Diagram_for_Propsed_System_Allowance_strategy)
@settings(max_examples=50)
def test_class_diagram_for_propsed_system_allowance_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Propsed_System_Allowance)



@given(instance=Class_Diagram_for_Propsed_System_Allowance_strategy)
def test_class_diagram_for_propsed_system_allowance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Propsed_System_Allowance_strategy)
def test_class_diagram_for_propsed_system_allowance_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Class_Diagram_for_Propsed_System_Allowance_strategy)
def test_class_diagram_for_propsed_system_allowance_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Class_Diagram_for_Propsed_System_Allowance_strategy)
def test_class_diagram_for_propsed_system_allowance_effectivedate_setter(instance):
    original = instance.effectivedate
    instance.effectivedate = original
    assert instance.effectivedate == original

@given(instance=Package_ETF_strategy)
@settings(max_examples=50)
def test_package_etf_instantiation(instance):
    assert isinstance(instance, Package_ETF)

@given(instance=Package_User_Permissions_strategy)
@settings(max_examples=50)
def test_package_user_permissions_instantiation(instance):
    assert isinstance(instance, Package_User_Permissions)



@given(instance=Package_User_Permissions_strategy)
def test_package_user_permissions_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_User_Permissions_strategy)
def test_package_user_permissions_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_Messages_strategy)
@settings(max_examples=50)
def test_package_messages_instantiation(instance):
    assert isinstance(instance, Package_Messages)

@given(instance=Package_Advances_strategy)
@settings(max_examples=50)
def test_package_advances_instantiation(instance):
    assert isinstance(instance, Package_Advances)

@given(instance=Package_UserUpdates_strategy)
@settings(max_examples=50)
def test_package_userupdates_instantiation(instance):
    assert isinstance(instance, Package_UserUpdates)

@given(instance=Package_Users_strategy)
@settings(max_examples=50)
def test_package_users_instantiation(instance):
    assert isinstance(instance, Package_Users)



@given(instance=Package_Users_strategy)
def test_package_users_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Package_Users_strategy)
def test_package_users_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Package_Users_strategy)
def test_package_users_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Package_Users_strategy)
def test_package_users_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Package_Users_strategy)
def test_package_users_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Package_User_groups_strategy)
@settings(max_examples=50)
def test_package_user_groups_instantiation(instance):
    assert isinstance(instance, Package_User_groups)



@given(instance=Package_User_groups_strategy)
def test_package_user_groups_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Package_User_groups_strategy)
def test_package_user_groups_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=Package_User_groups_strategy)
def test_package_user_groups_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Package_OT_Requests_strategy)
@settings(max_examples=50)
def test_package_ot_requests_instantiation(instance):
    assert isinstance(instance, Package_OT_Requests)



@given(instance=Package_OT_Requests_strategy)
def test_package_ot_requests_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Package_OT_Requests_strategy)
def test_package_ot_requests_EmpID_setter(instance):
    original = instance.EmpID
    instance.EmpID = original
    assert instance.EmpID == original



@given(instance=Package_OT_Requests_strategy)
def test_package_ot_requests_OTType_setter(instance):
    original = instance.OTType
    instance.OTType = original
    assert instance.OTType == original



@given(instance=Package_OT_Requests_strategy)
def test_package_ot_requests_OtDay_setter(instance):
    original = instance.OtDay
    instance.OtDay = original
    assert instance.OtDay == original

@given(instance=Package_LeaveProfiles_strategy)
@settings(max_examples=50)
def test_package_leaveprofiles_instantiation(instance):
    assert isinstance(instance, Package_LeaveProfiles)



@given(instance=Package_LeaveProfiles_strategy)
def test_package_leaveprofiles_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_LeaveProfiles_strategy)
def test_package_leaveprofiles_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_Leave_Taken_strategy)
@settings(max_examples=50)
def test_package_leave_taken_instantiation(instance):
    assert isinstance(instance, Package_Leave_Taken)



@given(instance=Package_Leave_Taken_strategy)
def test_package_leave_taken_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_Leave_Taken_strategy)
def test_package_leave_taken_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_Event_strategy)
@settings(max_examples=50)
def test_package_event_instantiation(instance):
    assert isinstance(instance, Package_Event)

@given(instance=Package_EPF_strategy)
@settings(max_examples=50)
def test_package_epf_instantiation(instance):
    assert isinstance(instance, Package_EPF)



@given(instance=Package_EPF_strategy)
def test_package_epf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Package_EPF_strategy)
def test_package_epf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Package_EPF_strategy)
def test_package_epf_effectve_date_setter(instance):
    original = instance.effectve_date
    instance.effectve_date = original
    assert instance.effectve_date == original

@given(instance=Package_EmployeeSalary_strategy)
@settings(max_examples=50)
def test_package_employeesalary_instantiation(instance):
    assert isinstance(instance, Package_EmployeeSalary)



@given(instance=Package_EmployeeSalary_strategy)
def test_package_employeesalary_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_EmployeeSalary_strategy)
def test_package_employeesalary_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_EmployeeParoll_strategy)
@settings(max_examples=50)
def test_package_employeeparoll_instantiation(instance):
    assert isinstance(instance, Package_EmployeeParoll)



@given(instance=Package_EmployeeParoll_strategy)
def test_package_employeeparoll_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_EmployeeParoll_strategy)
def test_package_employeeparoll_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_Employee_strategy)
@settings(max_examples=50)
def test_package_employee_instantiation(instance):
    assert isinstance(instance, Package_Employee)



@given(instance=Package_Employee_strategy)
def test_package_employee_leavegroup_setter(instance):
    original = instance.leavegroup
    instance.leavegroup = original
    assert instance.leavegroup == original



@given(instance=Package_Employee_strategy)
def test_package_employee_post_setter(instance):
    original = instance.post
    instance.post = original
    assert instance.post == original



@given(instance=Package_Employee_strategy)
def test_package_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Package_Employee_strategy)
def test_package_employee_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Package_Employee_strategy)
def test_package_employee_depid_setter(instance):
    original = instance.depid
    instance.depid = original
    assert instance.depid == original



@given(instance=Package_Employee_strategy)
def test_package_employee_usergroup_setter(instance):
    original = instance.usergroup
    instance.usergroup = original
    assert instance.usergroup == original



@given(instance=Package_Employee_strategy)
def test_package_employee_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original

@given(instance=Package_Posts_strategy)
@settings(max_examples=50)
def test_package_posts_instantiation(instance):
    assert isinstance(instance, Package_Posts)



@given(instance=Package_Posts_strategy)
def test_package_posts_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Package_Posts_strategy)
def test_package_posts_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Package_Shifts_strategy)
@settings(max_examples=50)
def test_package_shifts_instantiation(instance):
    assert isinstance(instance, Package_Shifts)



@given(instance=Package_Shifts_strategy)
def test_package_shifts_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Package_Shifts_strategy)
def test_package_shifts_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Package_Departments_strategy)
@settings(max_examples=50)
def test_package_departments_instantiation(instance):
    assert isinstance(instance, Package_Departments)



@given(instance=Package_Departments_strategy)
def test_package_departments_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Package_Deductions_strategy)
@settings(max_examples=50)
def test_package_deductions_instantiation(instance):
    assert isinstance(instance, Package_Deductions)



@given(instance=Package_Deductions_strategy)
def test_package_deductions_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Package_Deductions_strategy)
def test_package_deductions_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Package_AllowanceTypes_strategy)
@settings(max_examples=50)
def test_package_allowancetypes_instantiation(instance):
    assert isinstance(instance, Package_AllowanceTypes)

@given(instance=Package_DeuctionTypes_strategy)
@settings(max_examples=50)
def test_package_deuctiontypes_instantiation(instance):
    assert isinstance(instance, Package_DeuctionTypes)

@given(instance=Package_Attendance_strategy)
@settings(max_examples=50)
def test_package_attendance_instantiation(instance):
    assert isinstance(instance, Package_Attendance)



@given(instance=Package_Attendance_strategy)
def test_package_attendance_empid_setter(instance):
    original = instance.empid
    instance.empid = original
    assert instance.empid == original



@given(instance=Package_Attendance_strategy)
def test_package_attendance_timein_setter(instance):
    original = instance.timein
    instance.timein = original
    assert instance.timein == original



@given(instance=Package_Attendance_strategy)
def test_package_attendance_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original



@given(instance=Package_Attendance_strategy)
def test_package_attendance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Package_Allowance_strategy)
@settings(max_examples=50)
def test_package_allowance_instantiation(instance):
    assert isinstance(instance, Package_Allowance)



@given(instance=Package_Allowance_strategy)
def test_package_allowance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Package_Allowance_strategy)
def test_package_allowance_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Package_Allowance_strategy)
def test_package_allowance_Effectivedate_setter(instance):
    original = instance.Effectivedate
    instance.Effectivedate = original
    assert instance.Effectivedate == original

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Clark_Actor_strategy)
@settings(max_examples=50)
def test_clark_actor_instantiation(instance):
    assert isinstance(instance, Clark_Actor)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)

@given(instance=Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_add_new_company_events_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_add_employee_time_records_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_generate_paysheet_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_employee_profiles_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_add_new_department_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_add_employee_profile_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_reports_usecase1_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1)

@given(instance=Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_accept_leave_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_update_leave_balance_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_reject_leave_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_issue_and_check_appraislas_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_approve_employee_pay_sheets_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_pay_sheet_history_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_leave_rquest_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_employee_time_records_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_set_leave_status_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_set_advances_status_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_request_loan_and_advances_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_request_leaves_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_reports_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_personal_time_records_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_leave_status_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_personal_salary_history_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase)

@given(instance=Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_proposed_system_view_personal_detais_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase)

@given(instance=Employee_Actor_strategy)
@settings(max_examples=50)
def test_employee_actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)
