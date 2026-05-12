import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class_Diagram_for_Proposed_system_overtimeRequests,
    Class_Diagram_for_Proposed_system_Calender,
    Class_Diagram_for_Proposed_system_ETF,
    Class_Diagram_for_Proposed_system_EPF,
    Class_Diagram_for_Proposed_system_Events,
    Class_Diagram_for_Proposed_system_LeavesAllocated,
    Class_Diagram_for_Proposed_system_Attendance,
    Class_Diagram_for_Proposed_system_Post,
    Class_Diagram_for_Proposed_system_Advances,
    Class_Diagram_for_Proposed_system_Deductions,
    Class_Diagram_for_Proposed_system_Allowances,
    Class_Diagram_for_Proposed_system_Salary,
    Class_Diagram_for_Proposed_system_Department,
    Class_Diagram_for_Proposed_system_LeaveTaken,
    Class_Diagram_for_Proposed_system_WorkingShifts,
    Class_Diagram_for_Proposed_system_Role,
    Class_Diagram_for_Proposed_system_User,
    Class_Diagram_for_Proposed_system_Employee,
    Clark1_Actor1,
    Manager_Actor,
    Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase,
    Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase,
    Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase,
    Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase,
    Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase,
    Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase,
    Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase,
    Clark1_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_diagram_for_proposed_system_overtimerequests_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_overtimeRequests)


def test_class_diagram_for_proposed_system_overtimerequests_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_overtimeRequests.__init__)


def test_class_diagram_for_proposed_system_overtimerequests_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_overtimeRequests.__init__)
    params = list(sig.parameters.keys())
    assert "start_time" in params, "Missing parameter 'start_time'"
    assert "date" in params, "Missing parameter 'date'"
    assert "nd_time" in params, "Missing parameter 'nd_time'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_overtimerequests_has_start_time():
    assert hasattr(Class_Diagram_for_Proposed_system_overtimeRequests, "start_time")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_overtimeRequests.__mro__:
        if "start_time" in klass.__dict__:
            descriptor = klass.__dict__["start_time"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_overtimerequests_has_date():
    assert hasattr(Class_Diagram_for_Proposed_system_overtimeRequests, "date")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_overtimeRequests.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_overtimerequests_has_nd_time():
    assert hasattr(Class_Diagram_for_Proposed_system_overtimeRequests, "nd_time")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_overtimeRequests.__mro__:
        if "nd_time" in klass.__dict__:
            descriptor = klass.__dict__["nd_time"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_overtimerequests_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_overtimeRequests, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_overtimeRequests.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_calender_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Calender)


def test_class_diagram_for_proposed_system_calender_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Calender.__init__)


def test_class_diagram_for_proposed_system_calender_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Calender.__init__)
    params = list(sig.parameters.keys())
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "depid" in params, "Missing parameter 'depid'"
    assert "author_id" in params, "Missing parameter 'author_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_calender_has_eventType():
    assert hasattr(Class_Diagram_for_Proposed_system_Calender, "eventType")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Calender.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_calender_has_depid():
    assert hasattr(Class_Diagram_for_Proposed_system_Calender, "depid")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Calender.__mro__:
        if "depid" in klass.__dict__:
            descriptor = klass.__dict__["depid"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_calender_has_author_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Calender, "author_id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Calender.__mro__:
        if "author_id" in klass.__dict__:
            descriptor = klass.__dict__["author_id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_calender_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Calender, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Calender.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_etf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_ETF)


def test_class_diagram_for_proposed_system_etf_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_ETF.__init__)


def test_class_diagram_for_proposed_system_etf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_ETF.__init__)
    params = list(sig.parameters.keys())
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_etf_has_precentage():
    assert hasattr(Class_Diagram_for_Proposed_system_ETF, "precentage")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_ETF.__mro__:
        if "precentage" in klass.__dict__:
            descriptor = klass.__dict__["precentage"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_etf_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_ETF, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_ETF.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_epf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_EPF)


def test_class_diagram_for_proposed_system_epf_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_EPF.__init__)


def test_class_diagram_for_proposed_system_epf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_epf_has_precentage():
    assert hasattr(Class_Diagram_for_Proposed_system_EPF, "precentage")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_EPF.__mro__:
        if "precentage" in klass.__dict__:
            descriptor = klass.__dict__["precentage"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_epf_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_EPF, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_EPF.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_events_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Events)


def test_class_diagram_for_proposed_system_events_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Events.__init__)


def test_class_diagram_for_proposed_system_events_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Events.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_events_has_type():
    assert hasattr(Class_Diagram_for_Proposed_system_Events, "type")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Events.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_events_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Events, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Events.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_leavesallocated_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_LeavesAllocated)


def test_class_diagram_for_proposed_system_leavesallocated_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_LeavesAllocated.__init__)


def test_class_diagram_for_proposed_system_leavesallocated_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_LeavesAllocated.__init__)
    params = list(sig.parameters.keys())
    assert "leaveType" in params, "Missing parameter 'leaveType'"
    assert "noOfLeaves" in params, "Missing parameter 'noOfLeaves'"
    assert "id" in params, "Missing parameter 'id'"
    assert "empId" in params, "Missing parameter 'empId'"

def test_class_diagram_for_proposed_system_leavesallocated_has_leaveType():
    assert hasattr(Class_Diagram_for_Proposed_system_LeavesAllocated, "leaveType")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeavesAllocated.__mro__:
        if "leaveType" in klass.__dict__:
            descriptor = klass.__dict__["leaveType"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavesallocated_has_noOfLeaves():
    assert hasattr(Class_Diagram_for_Proposed_system_LeavesAllocated, "noOfLeaves")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeavesAllocated.__mro__:
        if "noOfLeaves" in klass.__dict__:
            descriptor = klass.__dict__["noOfLeaves"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavesallocated_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_LeavesAllocated, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeavesAllocated.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavesallocated_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_LeavesAllocated, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeavesAllocated.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_attendance_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Attendance)


def test_class_diagram_for_proposed_system_attendance_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Attendance.__init__)


def test_class_diagram_for_proposed_system_attendance_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "clock_in" in params, "Missing parameter 'clock_in'"
    assert "date" in params, "Missing parameter 'date'"
    assert "clock_out" in params, "Missing parameter 'clock_out'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "empId" in params, "Missing parameter 'empId'"

def test_class_diagram_for_proposed_system_attendance_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_attendance_has_clock_in():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "clock_in")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "clock_in" in klass.__dict__:
            descriptor = klass.__dict__["clock_in"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_attendance_has_date():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "date")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_attendance_has_clock_out():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "clock_out")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "clock_out" in klass.__dict__:
            descriptor = klass.__dict__["clock_out"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_attendance_has_attribute():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "attribute")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_attendance_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_Attendance, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Attendance.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_post_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Post)


def test_class_diagram_for_proposed_system_post_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Post.__init__)


def test_class_diagram_for_proposed_system_post_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Post.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "leavesEntitled" in params, "Missing parameter 'leavesEntitled'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "deptId" in params, "Missing parameter 'deptId'"
    assert "name" in params, "Missing parameter 'name'"

def test_class_diagram_for_proposed_system_post_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Post, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Post.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_post_has_leavesEntitled():
    assert hasattr(Class_Diagram_for_Proposed_system_Post, "leavesEntitled")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Post.__mro__:
        if "leavesEntitled" in klass.__dict__:
            descriptor = klass.__dict__["leavesEntitled"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_post_has_attribute():
    assert hasattr(Class_Diagram_for_Proposed_system_Post, "attribute")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Post.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_post_has_deptId():
    assert hasattr(Class_Diagram_for_Proposed_system_Post, "deptId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Post.__mro__:
        if "deptId" in klass.__dict__:
            descriptor = klass.__dict__["deptId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_post_has_name():
    assert hasattr(Class_Diagram_for_Proposed_system_Post, "name")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Post.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_advances_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Advances)


def test_class_diagram_for_proposed_system_advances_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Advances.__init__)


def test_class_diagram_for_proposed_system_advances_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Advances.__init__)
    params = list(sig.parameters.keys())
    assert "installments" in params, "Missing parameter 'installments'"
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_class_diagram_for_proposed_system_advances_has_installments():
    assert hasattr(Class_Diagram_for_Proposed_system_Advances, "installments")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Advances.__mro__:
        if "installments" in klass.__dict__:
            descriptor = klass.__dict__["installments"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_advances_has_issueDate():
    assert hasattr(Class_Diagram_for_Proposed_system_Advances, "issueDate")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Advances.__mro__:
        if "issueDate" in klass.__dict__:
            descriptor = klass.__dict__["issueDate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_advances_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Advances, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Advances.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_advances_has_salaryId():
    assert hasattr(Class_Diagram_for_Proposed_system_Advances, "salaryId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Advances.__mro__:
        if "salaryId" in klass.__dict__:
            descriptor = klass.__dict__["salaryId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_advances_has_amount():
    assert hasattr(Class_Diagram_for_Proposed_system_Advances, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Advances.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_deductions_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Deductions)


def test_class_diagram_for_proposed_system_deductions_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Deductions.__init__)


def test_class_diagram_for_proposed_system_deductions_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Deductions.__init__)
    params = list(sig.parameters.keys())
    assert "deductDate" in params, "Missing parameter 'deductDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "deducType" in params, "Missing parameter 'deducType'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_class_diagram_for_proposed_system_deductions_has_deductDate():
    assert hasattr(Class_Diagram_for_Proposed_system_Deductions, "deductDate")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Deductions.__mro__:
        if "deductDate" in klass.__dict__:
            descriptor = klass.__dict__["deductDate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_deductions_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Deductions, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Deductions.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_deductions_has_deducType():
    assert hasattr(Class_Diagram_for_Proposed_system_Deductions, "deducType")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Deductions.__mro__:
        if "deducType" in klass.__dict__:
            descriptor = klass.__dict__["deducType"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_deductions_has_salaryId():
    assert hasattr(Class_Diagram_for_Proposed_system_Deductions, "salaryId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Deductions.__mro__:
        if "salaryId" in klass.__dict__:
            descriptor = klass.__dict__["salaryId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_deductions_has_amount():
    assert hasattr(Class_Diagram_for_Proposed_system_Deductions, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Deductions.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_allowances_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Allowances)


def test_class_diagram_for_proposed_system_allowances_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Allowances.__init__)


def test_class_diagram_for_proposed_system_allowances_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Allowances.__init__)
    params = list(sig.parameters.keys())
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "allowanceType" in params, "Missing parameter 'allowanceType'"

def test_class_diagram_for_proposed_system_allowances_has_issueDate():
    assert hasattr(Class_Diagram_for_Proposed_system_Allowances, "issueDate")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Allowances.__mro__:
        if "issueDate" in klass.__dict__:
            descriptor = klass.__dict__["issueDate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_allowances_has_salaryId():
    assert hasattr(Class_Diagram_for_Proposed_system_Allowances, "salaryId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Allowances.__mro__:
        if "salaryId" in klass.__dict__:
            descriptor = klass.__dict__["salaryId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_allowances_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Allowances, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Allowances.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_allowances_has_amount():
    assert hasattr(Class_Diagram_for_Proposed_system_Allowances, "amount")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Allowances.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_allowances_has_allowanceType():
    assert hasattr(Class_Diagram_for_Proposed_system_Allowances, "allowanceType")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Allowances.__mro__:
        if "allowanceType" in klass.__dict__:
            descriptor = klass.__dict__["allowanceType"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_salary_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Salary)


def test_class_diagram_for_proposed_system_salary_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Salary.__init__)


def test_class_diagram_for_proposed_system_salary_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Salary.__init__)
    params = list(sig.parameters.keys())
    assert "empId" in params, "Missing parameter 'empId'"
    assert "EPF" in params, "Missing parameter 'EPF'"
    assert "basicPay" in params, "Missing parameter 'basicPay'"
    assert "ETF" in params, "Missing parameter 'ETF'"
    assert "deductions" in params, "Missing parameter 'deductions'"
    assert "allowances" in params, "Missing parameter 'allowances'"
    assert "payDate" in params, "Missing parameter 'payDate'"
    assert "advances" in params, "Missing parameter 'advances'"
    assert "overtimes" in params, "Missing parameter 'overtimes'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_salary_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_EPF():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "EPF")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "EPF" in klass.__dict__:
            descriptor = klass.__dict__["EPF"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_basicPay():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "basicPay")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "basicPay" in klass.__dict__:
            descriptor = klass.__dict__["basicPay"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_ETF():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "ETF")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "ETF" in klass.__dict__:
            descriptor = klass.__dict__["ETF"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_deductions():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "deductions")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "deductions" in klass.__dict__:
            descriptor = klass.__dict__["deductions"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_allowances():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "allowances")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "allowances" in klass.__dict__:
            descriptor = klass.__dict__["allowances"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_payDate():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "payDate")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "payDate" in klass.__dict__:
            descriptor = klass.__dict__["payDate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_advances():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "advances")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "advances" in klass.__dict__:
            descriptor = klass.__dict__["advances"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_overtimes():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "overtimes")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "overtimes" in klass.__dict__:
            descriptor = klass.__dict__["overtimes"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_salary_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Salary, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Salary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_department_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Department)


def test_class_diagram_for_proposed_system_department_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Department.__init__)


def test_class_diagram_for_proposed_system_department_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "empId" in params, "Missing parameter 'empId'"

def test_class_diagram_for_proposed_system_department_has_name():
    assert hasattr(Class_Diagram_for_Proposed_system_Department, "name")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_department_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Department, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Department.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_department_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_Department, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Department.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_leavetaken_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_LeaveTaken)


def test_class_diagram_for_proposed_system_leavetaken_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_LeaveTaken.__init__)


def test_class_diagram_for_proposed_system_leavetaken_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_LeaveTaken.__init__)
    params = list(sig.parameters.keys())
    assert "leaveType" in params, "Missing parameter 'leaveType'"
    assert "leaveDate" in params, "Missing parameter 'leaveDate'"
    assert "empId" in params, "Missing parameter 'empId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"

def test_class_diagram_for_proposed_system_leavetaken_has_leaveType():
    assert hasattr(Class_Diagram_for_Proposed_system_LeaveTaken, "leaveType")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeaveTaken.__mro__:
        if "leaveType" in klass.__dict__:
            descriptor = klass.__dict__["leaveType"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavetaken_has_leaveDate():
    assert hasattr(Class_Diagram_for_Proposed_system_LeaveTaken, "leaveDate")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeaveTaken.__mro__:
        if "leaveDate" in klass.__dict__:
            descriptor = klass.__dict__["leaveDate"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavetaken_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_LeaveTaken, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeaveTaken.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavetaken_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_LeaveTaken, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeaveTaken.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_leavetaken_has_attribute5():
    assert hasattr(Class_Diagram_for_Proposed_system_LeaveTaken, "attribute5")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_LeaveTaken.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_workingshifts_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_WorkingShifts)


def test_class_diagram_for_proposed_system_workingshifts_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_WorkingShifts.__init__)


def test_class_diagram_for_proposed_system_workingshifts_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_WorkingShifts.__init__)
    params = list(sig.parameters.keys())
    assert "empId" in params, "Missing parameter 'empId'"
    assert "startingTime" in params, "Missing parameter 'startingTime'"
    assert "id" in params, "Missing parameter 'id'"
    assert "endingTime" in params, "Missing parameter 'endingTime'"

def test_class_diagram_for_proposed_system_workingshifts_has_empId():
    assert hasattr(Class_Diagram_for_Proposed_system_WorkingShifts, "empId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_WorkingShifts.__mro__:
        if "empId" in klass.__dict__:
            descriptor = klass.__dict__["empId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_workingshifts_has_startingTime():
    assert hasattr(Class_Diagram_for_Proposed_system_WorkingShifts, "startingTime")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_WorkingShifts.__mro__:
        if "startingTime" in klass.__dict__:
            descriptor = klass.__dict__["startingTime"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_workingshifts_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_WorkingShifts, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_WorkingShifts.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_workingshifts_has_endingTime():
    assert hasattr(Class_Diagram_for_Proposed_system_WorkingShifts, "endingTime")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_WorkingShifts.__mro__:
        if "endingTime" in klass.__dict__:
            descriptor = klass.__dict__["endingTime"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_role_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Role)


def test_class_diagram_for_proposed_system_role_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Role.__init__)


def test_class_diagram_for_proposed_system_role_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Role.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "roleName" in params, "Missing parameter 'roleName'"
    assert "description" in params, "Missing parameter 'description'"

def test_class_diagram_for_proposed_system_role_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Role, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Role.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_role_has_roleName():
    assert hasattr(Class_Diagram_for_Proposed_system_Role, "roleName")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Role.__mro__:
        if "roleName" in klass.__dict__:
            descriptor = klass.__dict__["roleName"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_role_has_description():
    assert hasattr(Class_Diagram_for_Proposed_system_Role, "description")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Role.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_user_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_User)


def test_class_diagram_for_proposed_system_user_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_User.__init__)


def test_class_diagram_for_proposed_system_user_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_User.__init__)
    params = list(sig.parameters.keys())
    assert "roleId" in params, "Missing parameter 'roleId'"
    assert "firstNAme" in params, "Missing parameter 'firstNAme'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_diagram_for_proposed_system_user_has_roleId():
    assert hasattr(Class_Diagram_for_Proposed_system_User, "roleId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_User.__mro__:
        if "roleId" in klass.__dict__:
            descriptor = klass.__dict__["roleId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_user_has_firstNAme():
    assert hasattr(Class_Diagram_for_Proposed_system_User, "firstNAme")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_User.__mro__:
        if "firstNAme" in klass.__dict__:
            descriptor = klass.__dict__["firstNAme"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_user_has_LastName():
    assert hasattr(Class_Diagram_for_Proposed_system_User, "LastName")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_User.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_user_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_User, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_diagram_for_proposed_system_employee_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Employee)


def test_class_diagram_for_proposed_system_employee_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Employee.__init__)


def test_class_diagram_for_proposed_system_employee_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "NIC" in params, "Missing parameter 'NIC'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "deptId" in params, "Missing parameter 'deptId'"
    assert "address" in params, "Missing parameter 'address'"
    assert "postID" in params, "Missing parameter 'postID'"
    assert "id" in params, "Missing parameter 'id'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "shiftId" in params, "Missing parameter 'shiftId'"

def test_class_diagram_for_proposed_system_employee_has_gender():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "gender")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_mobile():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "mobile")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "mobile" in klass.__dict__:
            descriptor = klass.__dict__["mobile"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_NIC():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "NIC")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "NIC" in klass.__dict__:
            descriptor = klass.__dict__["NIC"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_userId():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "userId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_deptId():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "deptId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "deptId" in klass.__dict__:
            descriptor = klass.__dict__["deptId"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_address():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "address")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_postID():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "postID")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "postID" in klass.__dict__:
            descriptor = klass.__dict__["postID"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_id():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "id")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_phone():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "phone")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_class_diagram_for_proposed_system_employee_has_shiftId():
    assert hasattr(Class_Diagram_for_Proposed_system_Employee, "shiftId")
    descriptor = None
    for klass in Class_Diagram_for_Proposed_system_Employee.__mro__:
        if "shiftId" in klass.__dict__:
            descriptor = klass.__dict__["shiftId"]
            break
    assert isinstance(descriptor, property)



def test_clark1_actor1_is_not_abstract():
    assert not inspect.isabstract(Clark1_Actor1)


def test_clark1_actor1_constructor_exists():
    assert callable(Clark1_Actor1.__init__)


def test_clark1_actor1_constructor_args():
    sig = inspect.signature(Clark1_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_put_company_notices_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase)


def test_use_case_diagram_for_existing_system_put_company_notices_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase.__init__)


def test_use_case_diagram_for_existing_system_put_company_notices_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase)


def test_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase.__init__)


def test_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase)


def test_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase.__init__)


def test_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase)


def test_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase.__init__)


def test_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase)


def test_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase.__init__)


def test_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_give_message_to_employee_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase)


def test_use_case_diagram_for_existing_system_give_message_to_employee_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase.__init__)


def test_use_case_diagram_for_existing_system_give_message_to_employee_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase)


def test_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase.__init__)


def test_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase)


def test_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase.__init__)


def test_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_access_time_cards_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase)


def test_use_case_diagram_for_existing_system_access_time_cards_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase.__init__)


def test_use_case_diagram_for_existing_system_access_time_cards_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_check_leave_forms_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase)


def test_use_case_diagram_for_existing_system_check_leave_forms_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase.__init__)


def test_use_case_diagram_for_existing_system_check_leave_forms_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_salary_calculation_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase)


def test_use_case_diagram_for_existing_system_salary_calculation_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase.__init__)


def test_use_case_diagram_for_existing_system_salary_calculation_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_approve_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase)


def test_use_case_diagram_for_existing_system_approve_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase.__init__)


def test_use_case_diagram_for_existing_system_approve_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_access_leave_documents_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase)


def test_use_case_diagram_for_existing_system_access_leave_documents_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase.__init__)


def test_use_case_diagram_for_existing_system_access_leave_documents_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase)


def test_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase.__init__)


def test_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_reject_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase)


def test_use_case_diagram_for_existing_system_reject_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase.__init__)


def test_use_case_diagram_for_existing_system_reject_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase)


def test_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase.__init__)


def test_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_register_new_employee_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase)


def test_use_case_diagram_for_existing_system_register_new_employee_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase.__init__)


def test_use_case_diagram_for_existing_system_register_new_employee_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase)


def test_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase.__init__)


def test_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_calculate_late_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase)


def test_use_case_diagram_for_existing_system_calculate_late_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase.__init__)


def test_use_case_diagram_for_existing_system_calculate_late_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_request_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase)


def test_use_case_diagram_for_existing_system_request_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase.__init__)


def test_use_case_diagram_for_existing_system_request_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_calculate_overtime_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase)


def test_use_case_diagram_for_existing_system_calculate_overtime_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase.__init__)


def test_use_case_diagram_for_existing_system_calculate_overtime_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase)


def test_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase.__init__)


def test_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_clark1_actor_is_not_abstract():
    assert not inspect.isabstract(Clark1_Actor)


def test_clark1_actor_constructor_exists():
    assert callable(Clark1_Actor.__init__)


def test_clark1_actor_constructor_args():
    sig = inspect.signature(Clark1_Actor.__init__)
    params = list(sig.parameters.keys())


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
Class_Diagram_for_Proposed_system_overtimeRequests_strategy = st.builds(
    Class_Diagram_for_Proposed_system_overtimeRequests,
    start_time=
        safe_text,
    date=
        safe_text,
    nd_time=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Calender_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Calender,
    eventType=
        safe_text,
    depid=
        safe_text,
    author_id=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_ETF_strategy = st.builds(
    Class_Diagram_for_Proposed_system_ETF,
    precentage=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_EPF_strategy = st.builds(
    Class_Diagram_for_Proposed_system_EPF,
    precentage=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Events_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Events,
    type=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_LeavesAllocated_strategy = st.builds(
    Class_Diagram_for_Proposed_system_LeavesAllocated,
    leaveType=
        safe_text,
    noOfLeaves=
        safe_text,
    id=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_Attendance_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Attendance,
    id=
        safe_text,
    clock_in=
        safe_text,
    date=
        safe_text,
    clock_out=
        safe_text,
    attribute=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_Post_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Post,
    id=
        safe_text,
    leavesEntitled=
        safe_text,
    attribute=
        safe_text,
    deptId=
        safe_text,
    name=
        safe_text
)
Class_Diagram_for_Proposed_system_Advances_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Advances,
    installments=
        safe_text,
    issueDate=
        safe_text,
    id=
        safe_text,
    salaryId=
        safe_text,
    amount=
        safe_text
)
Class_Diagram_for_Proposed_system_Deductions_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Deductions,
    deductDate=
        safe_text,
    id=
        safe_text,
    deducType=
        safe_text,
    salaryId=
        safe_text,
    amount=
        safe_text
)
Class_Diagram_for_Proposed_system_Allowances_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Allowances,
    issueDate=
        safe_text,
    salaryId=
        safe_text,
    id=
        safe_text,
    amount=
        safe_text,
    allowanceType=
        safe_text
)
Class_Diagram_for_Proposed_system_Salary_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Salary,
    empId=
        safe_text,
    EPF=
        safe_text,
    basicPay=
        safe_text,
    ETF=
        safe_text,
    deductions=
        safe_text,
    allowances=
        safe_text,
    payDate=
        safe_text,
    advances=
        safe_text,
    overtimes=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Department_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Department,
    name=
        safe_text,
    id=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_LeaveTaken_strategy = st.builds(
    Class_Diagram_for_Proposed_system_LeaveTaken,
    leaveType=
        safe_text,
    leaveDate=
        safe_text,
    empId=
        safe_text,
    id=
        safe_text,
    attribute5=
        safe_text
)
Class_Diagram_for_Proposed_system_WorkingShifts_strategy = st.builds(
    Class_Diagram_for_Proposed_system_WorkingShifts,
    empId=
        safe_text,
    startingTime=
        safe_text,
    id=
        safe_text,
    endingTime=
        safe_text
)
Class_Diagram_for_Proposed_system_Role_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Role,
    id=
        safe_text,
    roleName=
        safe_text,
    description=
        safe_text
)
Class_Diagram_for_Proposed_system_User_strategy = st.builds(
    Class_Diagram_for_Proposed_system_User,
    roleId=
        st.integers(),
    firstNAme=
        safe_text,
    LastName=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Employee_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Employee,
    gender=
        safe_text,
    mobile=
        safe_text,
    NIC=
        safe_text,
    userId=
        st.integers(),
    deptId=
        st.integers(),
    address=
        safe_text,
    postID=
        st.integers(),
    id=
        st.integers(),
    phone=
        safe_text,
    shiftId=
        st.integers()
)
Clark1_Actor1_strategy = st.builds(
    Clark1_Actor1,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase,
)
Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase,
)
Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase,
)
Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase,
)
Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase,
)
Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase,
)
Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase,
)
Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase,
)
Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase,
)
Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase,
)
Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase,
)
Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase,
)
Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase,
)
Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase,
)
Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase,
)
Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase,
)
Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase,
)
Clark1_Actor_strategy = st.builds(
    Clark1_Actor,
)

@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_overtimerequests_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_overtimeRequests)



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_class_diagram_for_proposed_system_overtimerequests_start_time_setter(instance):
    original = instance.start_time
    instance.start_time = original
    assert instance.start_time == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_class_diagram_for_proposed_system_overtimerequests_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_class_diagram_for_proposed_system_overtimerequests_nd_time_setter(instance):
    original = instance.nd_time
    instance.nd_time = original
    assert instance.nd_time == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_class_diagram_for_proposed_system_overtimerequests_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_calender_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Calender)



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_class_diagram_for_proposed_system_calender_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_class_diagram_for_proposed_system_calender_depid_setter(instance):
    original = instance.depid
    instance.depid = original
    assert instance.depid == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_class_diagram_for_proposed_system_calender_author_id_setter(instance):
    original = instance.author_id
    instance.author_id = original
    assert instance.author_id == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_class_diagram_for_proposed_system_calender_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_etf_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_ETF)



@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
def test_class_diagram_for_proposed_system_etf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
def test_class_diagram_for_proposed_system_etf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_epf_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_EPF)



@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
def test_class_diagram_for_proposed_system_epf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
def test_class_diagram_for_proposed_system_epf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_events_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Events)



@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
def test_class_diagram_for_proposed_system_events_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
def test_class_diagram_for_proposed_system_events_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_leavesallocated_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_LeavesAllocated)



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_class_diagram_for_proposed_system_leavesallocated_leaveType_setter(instance):
    original = instance.leaveType
    instance.leaveType = original
    assert instance.leaveType == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_class_diagram_for_proposed_system_leavesallocated_noOfLeaves_setter(instance):
    original = instance.noOfLeaves
    instance.noOfLeaves = original
    assert instance.noOfLeaves == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_class_diagram_for_proposed_system_leavesallocated_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_class_diagram_for_proposed_system_leavesallocated_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original

@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_attendance_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Attendance)



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_clock_in_setter(instance):
    original = instance.clock_in
    instance.clock_in = original
    assert instance.clock_in == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_clock_out_setter(instance):
    original = instance.clock_out
    instance.clock_out = original
    assert instance.clock_out == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_class_diagram_for_proposed_system_attendance_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original

@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_post_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Post)



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_class_diagram_for_proposed_system_post_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_class_diagram_for_proposed_system_post_leavesEntitled_setter(instance):
    original = instance.leavesEntitled
    instance.leavesEntitled = original
    assert instance.leavesEntitled == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_class_diagram_for_proposed_system_post_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_class_diagram_for_proposed_system_post_deptId_setter(instance):
    original = instance.deptId
    instance.deptId = original
    assert instance.deptId == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_class_diagram_for_proposed_system_post_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_advances_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Advances)



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_class_diagram_for_proposed_system_advances_installments_setter(instance):
    original = instance.installments
    instance.installments = original
    assert instance.installments == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_class_diagram_for_proposed_system_advances_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_class_diagram_for_proposed_system_advances_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_class_diagram_for_proposed_system_advances_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_class_diagram_for_proposed_system_advances_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_deductions_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Deductions)



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_class_diagram_for_proposed_system_deductions_deductDate_setter(instance):
    original = instance.deductDate
    instance.deductDate = original
    assert instance.deductDate == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_class_diagram_for_proposed_system_deductions_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_class_diagram_for_proposed_system_deductions_deducType_setter(instance):
    original = instance.deducType
    instance.deducType = original
    assert instance.deducType == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_class_diagram_for_proposed_system_deductions_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_class_diagram_for_proposed_system_deductions_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_allowances_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Allowances)



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_class_diagram_for_proposed_system_allowances_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_class_diagram_for_proposed_system_allowances_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_class_diagram_for_proposed_system_allowances_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_class_diagram_for_proposed_system_allowances_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_class_diagram_for_proposed_system_allowances_allowanceType_setter(instance):
    original = instance.allowanceType
    instance.allowanceType = original
    assert instance.allowanceType == original

@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_salary_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Salary)



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_EPF_setter(instance):
    original = instance.EPF
    instance.EPF = original
    assert instance.EPF == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_basicPay_setter(instance):
    original = instance.basicPay
    instance.basicPay = original
    assert instance.basicPay == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_ETF_setter(instance):
    original = instance.ETF
    instance.ETF = original
    assert instance.ETF == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_deductions_setter(instance):
    original = instance.deductions
    instance.deductions = original
    assert instance.deductions == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_allowances_setter(instance):
    original = instance.allowances
    instance.allowances = original
    assert instance.allowances == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_payDate_setter(instance):
    original = instance.payDate
    instance.payDate = original
    assert instance.payDate == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_advances_setter(instance):
    original = instance.advances
    instance.advances = original
    assert instance.advances == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_overtimes_setter(instance):
    original = instance.overtimes
    instance.overtimes = original
    assert instance.overtimes == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_class_diagram_for_proposed_system_salary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_department_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Department)



@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_class_diagram_for_proposed_system_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_class_diagram_for_proposed_system_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_class_diagram_for_proposed_system_department_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original

@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_leavetaken_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_LeaveTaken)



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_class_diagram_for_proposed_system_leavetaken_leaveType_setter(instance):
    original = instance.leaveType
    instance.leaveType = original
    assert instance.leaveType == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_class_diagram_for_proposed_system_leavetaken_leaveDate_setter(instance):
    original = instance.leaveDate
    instance.leaveDate = original
    assert instance.leaveDate == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_class_diagram_for_proposed_system_leavetaken_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_class_diagram_for_proposed_system_leavetaken_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_class_diagram_for_proposed_system_leavetaken_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original

@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_workingshifts_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_WorkingShifts)



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_class_diagram_for_proposed_system_workingshifts_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_class_diagram_for_proposed_system_workingshifts_startingTime_setter(instance):
    original = instance.startingTime
    instance.startingTime = original
    assert instance.startingTime == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_class_diagram_for_proposed_system_workingshifts_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_class_diagram_for_proposed_system_workingshifts_endingTime_setter(instance):
    original = instance.endingTime
    instance.endingTime = original
    assert instance.endingTime == original

@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_role_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Role)



@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_class_diagram_for_proposed_system_role_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_class_diagram_for_proposed_system_role_roleName_setter(instance):
    original = instance.roleName
    instance.roleName = original
    assert instance.roleName == original



@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_class_diagram_for_proposed_system_role_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_user_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_User)



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_class_diagram_for_proposed_system_user_roleId_setter(instance):
    original = instance.roleId
    instance.roleId = original
    assert instance.roleId == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_class_diagram_for_proposed_system_user_firstNAme_setter(instance):
    original = instance.firstNAme
    instance.firstNAme = original
    assert instance.firstNAme == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_class_diagram_for_proposed_system_user_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_class_diagram_for_proposed_system_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
@settings(max_examples=50)
def test_class_diagram_for_proposed_system_employee_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Employee)



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_NIC_setter(instance):
    original = instance.NIC
    instance.NIC = original
    assert instance.NIC == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_deptId_setter(instance):
    original = instance.deptId
    instance.deptId = original
    assert instance.deptId == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_postID_setter(instance):
    original = instance.postID
    instance.postID = original
    assert instance.postID == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_class_diagram_for_proposed_system_employee_shiftId_setter(instance):
    original = instance.shiftId
    instance.shiftId = original
    assert instance.shiftId == original

@given(instance=Clark1_Actor1_strategy)
@settings(max_examples=50)
def test_clark1_actor1_instantiation(instance):
    assert isinstance(instance, Clark1_Actor1)

@given(instance=Manager_Actor_strategy)
@settings(max_examples=50)
def test_manager_actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)

@given(instance=Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_put_company_notices_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_give_message_to_employee_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_access_time_cards_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_check_leave_forms_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_salary_calculation_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_approve_leave_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_access_leave_documents_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_reject_leave_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_register_new_employee_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_calculate_late_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_request_leave_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_calculate_overtime_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase)

@given(instance=Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_strategy)
@settings(max_examples=50)
def test_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase)

@given(instance=Clark1_Actor_strategy)
@settings(max_examples=50)
def test_clark1_actor_instantiation(instance):
    assert isinstance(instance, Clark1_Actor)
