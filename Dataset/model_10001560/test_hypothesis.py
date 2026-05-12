import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    book_ticket_UseCase,
    Customer_Actor1,
    Manager_Actor,
    statistical_reporting_UseCase,
    vehicle_management_UseCase,
    account_management_UseCase,
    customer_management_UseCase,
    Use_Actor,
    Book_ticket_UseCase,
    Search_the_route_UseCase,
    Customer_Actor,
    accoutUser,
    Ticket,
    Customer,
    infoCompany,
    mapCarExchange,
    Car,
    Login_UseCase3,
    Report_by_ticket_amount_UseCase,
    Report_by_revenue_UseCase,
    statistical_reporting_UseCase1,
    Manager_Actor4,
    Login_UseCase2,
    Delete_vehicles_UseCase,
    Update_vehicles_information_UseCase,
    View_vehicles_information_UseCase,
    vehicle_management_UseCase1,
    Manager_Actor3,
    call_for_customers_UseCase,
    Login_UseCase1,
    View_customers_information_UseCase,
    cancel_booking_UseCase,
    confirm_booking_UseCase,
    search_customers_UseCase,
    customer_management_UseCase1,
    Manager_Actor2,
    make_payment_UseCase,
    View_account_information_UseCase,
    Account_settings_UseCase,
    Login_UseCase,
    account_management_UseCase1,
    Manager_Actor1,
    search_UseCase,
    confirm_information_UseCase,
    choose_seats_UseCase,
    choose_vehicle_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_book_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(book_ticket_UseCase)


def test_book_ticket_usecase_constructor_exists():
    assert callable(book_ticket_UseCase.__init__)


def test_book_ticket_usecase_constructor_args():
    sig = inspect.signature(book_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor1_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor1)


def test_customer_actor1_constructor_exists():
    assert callable(Customer_Actor1.__init__)


def test_customer_actor1_constructor_args():
    sig = inspect.signature(Customer_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_statistical_reporting_usecase_is_not_abstract():
    assert not inspect.isabstract(statistical_reporting_UseCase)


def test_statistical_reporting_usecase_constructor_exists():
    assert callable(statistical_reporting_UseCase.__init__)


def test_statistical_reporting_usecase_constructor_args():
    sig = inspect.signature(statistical_reporting_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_management_usecase_is_not_abstract():
    assert not inspect.isabstract(vehicle_management_UseCase)


def test_vehicle_management_usecase_constructor_exists():
    assert callable(vehicle_management_UseCase.__init__)


def test_vehicle_management_usecase_constructor_args():
    sig = inspect.signature(vehicle_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_account_management_usecase_is_not_abstract():
    assert not inspect.isabstract(account_management_UseCase)


def test_account_management_usecase_constructor_exists():
    assert callable(account_management_UseCase.__init__)


def test_account_management_usecase_constructor_args():
    sig = inspect.signature(account_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_management_usecase_is_not_abstract():
    assert not inspect.isabstract(customer_management_UseCase)


def test_customer_management_usecase_constructor_exists():
    assert callable(customer_management_UseCase.__init__)


def test_customer_management_usecase_constructor_args():
    sig = inspect.signature(customer_management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_use_actor_is_not_abstract():
    assert not inspect.isabstract(Use_Actor)


def test_use_actor_constructor_exists():
    assert callable(Use_Actor.__init__)


def test_use_actor_constructor_args():
    sig = inspect.signature(Use_Actor.__init__)
    params = list(sig.parameters.keys())



def test_book_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(Book_ticket_UseCase)


def test_book_ticket_usecase_constructor_exists():
    assert callable(Book_ticket_UseCase.__init__)


def test_book_ticket_usecase_constructor_args():
    sig = inspect.signature(Book_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_the_route_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_the_route_UseCase)


def test_search_the_route_usecase_constructor_exists():
    assert callable(Search_the_route_UseCase.__init__)


def test_search_the_route_usecase_constructor_args():
    sig = inspect.signature(Search_the_route_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_accoutuser_is_not_abstract():
    assert not inspect.isabstract(accoutUser)


def test_accoutuser_constructor_exists():
    assert callable(accoutUser.__init__)


def test_accoutuser_constructor_args():
    sig = inspect.signature(accoutUser.__init__)
    params = list(sig.parameters.keys())
    assert "codeConfirm" in params, "Missing parameter 'codeConfirm'"
    assert "idCompany" in params, "Missing parameter 'idCompany'"
    assert "emailUser" in params, "Missing parameter 'emailUser'"
    assert "dateRegister" in params, "Missing parameter 'dateRegister'"
    assert "idUser" in params, "Missing parameter 'idUser'"
    assert "passwordUser" in params, "Missing parameter 'passwordUser'"

def test_accoutuser_has_codeConfirm():
    assert hasattr(accoutUser, "codeConfirm")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "codeConfirm" in klass.__dict__:
            descriptor = klass.__dict__["codeConfirm"]
            break
    assert isinstance(descriptor, property)

def test_accoutuser_has_idCompany():
    assert hasattr(accoutUser, "idCompany")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "idCompany" in klass.__dict__:
            descriptor = klass.__dict__["idCompany"]
            break
    assert isinstance(descriptor, property)

def test_accoutuser_has_emailUser():
    assert hasattr(accoutUser, "emailUser")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "emailUser" in klass.__dict__:
            descriptor = klass.__dict__["emailUser"]
            break
    assert isinstance(descriptor, property)

def test_accoutuser_has_dateRegister():
    assert hasattr(accoutUser, "dateRegister")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "dateRegister" in klass.__dict__:
            descriptor = klass.__dict__["dateRegister"]
            break
    assert isinstance(descriptor, property)

def test_accoutuser_has_idUser():
    assert hasattr(accoutUser, "idUser")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "idUser" in klass.__dict__:
            descriptor = klass.__dict__["idUser"]
            break
    assert isinstance(descriptor, property)

def test_accoutuser_has_passwordUser():
    assert hasattr(accoutUser, "passwordUser")
    descriptor = None
    for klass in accoutUser.__mro__:
        if "passwordUser" in klass.__dict__:
            descriptor = klass.__dict__["passwordUser"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "idCustomer" in params, "Missing parameter 'idCustomer'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "idTicket" in params, "Missing parameter 'idTicket'"
    assert "code" in params, "Missing parameter 'code'"
    assert "timeExchange" in params, "Missing parameter 'timeExchange'"
    assert "statusSeat" in params, "Missing parameter 'statusSeat'"
    assert "positionSeat" in params, "Missing parameter 'positionSeat'"
    assert "numberSeat" in params, "Missing parameter 'numberSeat'"
    assert "positionSeatBelow" in params, "Missing parameter 'positionSeatBelow'"

def test_ticket_has_idCustomer():
    assert hasattr(Ticket, "idCustomer")
    descriptor = None
    for klass in Ticket.__mro__:
        if "idCustomer" in klass.__dict__:
            descriptor = klass.__dict__["idCustomer"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_idCar():
    assert hasattr(Ticket, "idCar")
    descriptor = None
    for klass in Ticket.__mro__:
        if "idCar" in klass.__dict__:
            descriptor = klass.__dict__["idCar"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_idTicket():
    assert hasattr(Ticket, "idTicket")
    descriptor = None
    for klass in Ticket.__mro__:
        if "idTicket" in klass.__dict__:
            descriptor = klass.__dict__["idTicket"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_code():
    assert hasattr(Ticket, "code")
    descriptor = None
    for klass in Ticket.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_timeExchange():
    assert hasattr(Ticket, "timeExchange")
    descriptor = None
    for klass in Ticket.__mro__:
        if "timeExchange" in klass.__dict__:
            descriptor = klass.__dict__["timeExchange"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_statusSeat():
    assert hasattr(Ticket, "statusSeat")
    descriptor = None
    for klass in Ticket.__mro__:
        if "statusSeat" in klass.__dict__:
            descriptor = klass.__dict__["statusSeat"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_positionSeat():
    assert hasattr(Ticket, "positionSeat")
    descriptor = None
    for klass in Ticket.__mro__:
        if "positionSeat" in klass.__dict__:
            descriptor = klass.__dict__["positionSeat"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_numberSeat():
    assert hasattr(Ticket, "numberSeat")
    descriptor = None
    for klass in Ticket.__mro__:
        if "numberSeat" in klass.__dict__:
            descriptor = klass.__dict__["numberSeat"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_positionSeatBelow():
    assert hasattr(Ticket, "positionSeatBelow")
    descriptor = None
    for klass in Ticket.__mro__:
        if "positionSeatBelow" in klass.__dict__:
            descriptor = klass.__dict__["positionSeatBelow"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "emailCustomer" in params, "Missing parameter 'emailCustomer'"
    assert "phoneCustomer" in params, "Missing parameter 'phoneCustomer'"
    assert "idCustomer" in params, "Missing parameter 'idCustomer'"
    assert "nameCustomer" in params, "Missing parameter 'nameCustomer'"

def test_customer_has_emailCustomer():
    assert hasattr(Customer, "emailCustomer")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailCustomer" in klass.__dict__:
            descriptor = klass.__dict__["emailCustomer"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phoneCustomer():
    assert hasattr(Customer, "phoneCustomer")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneCustomer" in klass.__dict__:
            descriptor = klass.__dict__["phoneCustomer"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_idCustomer():
    assert hasattr(Customer, "idCustomer")
    descriptor = None
    for klass in Customer.__mro__:
        if "idCustomer" in klass.__dict__:
            descriptor = klass.__dict__["idCustomer"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_nameCustomer():
    assert hasattr(Customer, "nameCustomer")
    descriptor = None
    for klass in Customer.__mro__:
        if "nameCustomer" in klass.__dict__:
            descriptor = klass.__dict__["nameCustomer"]
            break
    assert isinstance(descriptor, property)



def test_infocompany_is_not_abstract():
    assert not inspect.isabstract(infoCompany)


def test_infocompany_constructor_exists():
    assert callable(infoCompany.__init__)


def test_infocompany_constructor_args():
    sig = inspect.signature(infoCompany.__init__)
    params = list(sig.parameters.keys())
    assert "idCompany" in params, "Missing parameter 'idCompany'"
    assert "nameCompany" in params, "Missing parameter 'nameCompany'"
    assert "dateEstablish" in params, "Missing parameter 'dateEstablish'"
    assert "describeCompany" in params, "Missing parameter 'describeCompany'"
    assert "addressCompany" in params, "Missing parameter 'addressCompany'"
    assert "showSafe" in params, "Missing parameter 'showSafe'"
    assert "dateUpdate" in params, "Missing parameter 'dateUpdate'"
    assert "dateRegister" in params, "Missing parameter 'dateRegister'"
    assert "phoneCompany" in params, "Missing parameter 'phoneCompany'"

def test_infocompany_has_idCompany():
    assert hasattr(infoCompany, "idCompany")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "idCompany" in klass.__dict__:
            descriptor = klass.__dict__["idCompany"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_nameCompany():
    assert hasattr(infoCompany, "nameCompany")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "nameCompany" in klass.__dict__:
            descriptor = klass.__dict__["nameCompany"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_dateEstablish():
    assert hasattr(infoCompany, "dateEstablish")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "dateEstablish" in klass.__dict__:
            descriptor = klass.__dict__["dateEstablish"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_describeCompany():
    assert hasattr(infoCompany, "describeCompany")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "describeCompany" in klass.__dict__:
            descriptor = klass.__dict__["describeCompany"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_addressCompany():
    assert hasattr(infoCompany, "addressCompany")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "addressCompany" in klass.__dict__:
            descriptor = klass.__dict__["addressCompany"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_showSafe():
    assert hasattr(infoCompany, "showSafe")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "showSafe" in klass.__dict__:
            descriptor = klass.__dict__["showSafe"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_dateUpdate():
    assert hasattr(infoCompany, "dateUpdate")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "dateUpdate" in klass.__dict__:
            descriptor = klass.__dict__["dateUpdate"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_dateRegister():
    assert hasattr(infoCompany, "dateRegister")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "dateRegister" in klass.__dict__:
            descriptor = klass.__dict__["dateRegister"]
            break
    assert isinstance(descriptor, property)

def test_infocompany_has_phoneCompany():
    assert hasattr(infoCompany, "phoneCompany")
    descriptor = None
    for klass in infoCompany.__mro__:
        if "phoneCompany" in klass.__dict__:
            descriptor = klass.__dict__["phoneCompany"]
            break
    assert isinstance(descriptor, property)



def test_mapcarexchange_is_not_abstract():
    assert not inspect.isabstract(mapCarExchange)


def test_mapcarexchange_constructor_exists():
    assert callable(mapCarExchange.__init__)


def test_mapcarexchange_constructor_args():
    sig = inspect.signature(mapCarExchange.__init__)
    params = list(sig.parameters.keys())
    assert "mapOnCar" in params, "Missing parameter 'mapOnCar'"
    assert "idMap" in params, "Missing parameter 'idMap'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "timeExchange" in params, "Missing parameter 'timeExchange'"
    assert "mapBelowCar" in params, "Missing parameter 'mapBelowCar'"

def test_mapcarexchange_has_mapOnCar():
    assert hasattr(mapCarExchange, "mapOnCar")
    descriptor = None
    for klass in mapCarExchange.__mro__:
        if "mapOnCar" in klass.__dict__:
            descriptor = klass.__dict__["mapOnCar"]
            break
    assert isinstance(descriptor, property)

def test_mapcarexchange_has_idMap():
    assert hasattr(mapCarExchange, "idMap")
    descriptor = None
    for klass in mapCarExchange.__mro__:
        if "idMap" in klass.__dict__:
            descriptor = klass.__dict__["idMap"]
            break
    assert isinstance(descriptor, property)

def test_mapcarexchange_has_idCar():
    assert hasattr(mapCarExchange, "idCar")
    descriptor = None
    for klass in mapCarExchange.__mro__:
        if "idCar" in klass.__dict__:
            descriptor = klass.__dict__["idCar"]
            break
    assert isinstance(descriptor, property)

def test_mapcarexchange_has_timeExchange():
    assert hasattr(mapCarExchange, "timeExchange")
    descriptor = None
    for klass in mapCarExchange.__mro__:
        if "timeExchange" in klass.__dict__:
            descriptor = klass.__dict__["timeExchange"]
            break
    assert isinstance(descriptor, property)

def test_mapcarexchange_has_mapBelowCar():
    assert hasattr(mapCarExchange, "mapBelowCar")
    descriptor = None
    for klass in mapCarExchange.__mro__:
        if "mapBelowCar" in klass.__dict__:
            descriptor = klass.__dict__["mapBelowCar"]
            break
    assert isinstance(descriptor, property)



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "idUser" in params, "Missing parameter 'idUser'"
    assert "statusCar" in params, "Missing parameter 'statusCar'"
    assert "timeStartCar" in params, "Missing parameter 'timeStartCar'"
    assert "fareCar" in params, "Missing parameter 'fareCar'"
    assert "positionEndCar" in params, "Missing parameter 'positionEndCar'"
    assert "idCar" in params, "Missing parameter 'idCar'"
    assert "classifyCar" in params, "Missing parameter 'classifyCar'"
    assert "positionStartCar" in params, "Missing parameter 'positionStartCar'"
    assert "mapOnCar" in params, "Missing parameter 'mapOnCar'"
    assert "mapBelowCar" in params, "Missing parameter 'mapBelowCar'"
    assert "numberPlatesCar" in params, "Missing parameter 'numberPlatesCar'"
    assert "phoneCar" in params, "Missing parameter 'phoneCar'"
    assert "imageLinkCar" in params, "Missing parameter 'imageLinkCar'"
    assert "nameCar" in params, "Missing parameter 'nameCar'"

def test_car_has_idUser():
    assert hasattr(Car, "idUser")
    descriptor = None
    for klass in Car.__mro__:
        if "idUser" in klass.__dict__:
            descriptor = klass.__dict__["idUser"]
            break
    assert isinstance(descriptor, property)

def test_car_has_statusCar():
    assert hasattr(Car, "statusCar")
    descriptor = None
    for klass in Car.__mro__:
        if "statusCar" in klass.__dict__:
            descriptor = klass.__dict__["statusCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_timeStartCar():
    assert hasattr(Car, "timeStartCar")
    descriptor = None
    for klass in Car.__mro__:
        if "timeStartCar" in klass.__dict__:
            descriptor = klass.__dict__["timeStartCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_fareCar():
    assert hasattr(Car, "fareCar")
    descriptor = None
    for klass in Car.__mro__:
        if "fareCar" in klass.__dict__:
            descriptor = klass.__dict__["fareCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_positionEndCar():
    assert hasattr(Car, "positionEndCar")
    descriptor = None
    for klass in Car.__mro__:
        if "positionEndCar" in klass.__dict__:
            descriptor = klass.__dict__["positionEndCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_idCar():
    assert hasattr(Car, "idCar")
    descriptor = None
    for klass in Car.__mro__:
        if "idCar" in klass.__dict__:
            descriptor = klass.__dict__["idCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_classifyCar():
    assert hasattr(Car, "classifyCar")
    descriptor = None
    for klass in Car.__mro__:
        if "classifyCar" in klass.__dict__:
            descriptor = klass.__dict__["classifyCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_positionStartCar():
    assert hasattr(Car, "positionStartCar")
    descriptor = None
    for klass in Car.__mro__:
        if "positionStartCar" in klass.__dict__:
            descriptor = klass.__dict__["positionStartCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_mapOnCar():
    assert hasattr(Car, "mapOnCar")
    descriptor = None
    for klass in Car.__mro__:
        if "mapOnCar" in klass.__dict__:
            descriptor = klass.__dict__["mapOnCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_mapBelowCar():
    assert hasattr(Car, "mapBelowCar")
    descriptor = None
    for klass in Car.__mro__:
        if "mapBelowCar" in klass.__dict__:
            descriptor = klass.__dict__["mapBelowCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_numberPlatesCar():
    assert hasattr(Car, "numberPlatesCar")
    descriptor = None
    for klass in Car.__mro__:
        if "numberPlatesCar" in klass.__dict__:
            descriptor = klass.__dict__["numberPlatesCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_phoneCar():
    assert hasattr(Car, "phoneCar")
    descriptor = None
    for klass in Car.__mro__:
        if "phoneCar" in klass.__dict__:
            descriptor = klass.__dict__["phoneCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_imageLinkCar():
    assert hasattr(Car, "imageLinkCar")
    descriptor = None
    for klass in Car.__mro__:
        if "imageLinkCar" in klass.__dict__:
            descriptor = klass.__dict__["imageLinkCar"]
            break
    assert isinstance(descriptor, property)

def test_car_has_nameCar():
    assert hasattr(Car, "nameCar")
    descriptor = None
    for klass in Car.__mro__:
        if "nameCar" in klass.__dict__:
            descriptor = klass.__dict__["nameCar"]
            break
    assert isinstance(descriptor, property)



def test_login_usecase3_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase3)


def test_login_usecase3_constructor_exists():
    assert callable(Login_UseCase3.__init__)


def test_login_usecase3_constructor_args():
    sig = inspect.signature(Login_UseCase3.__init__)
    params = list(sig.parameters.keys())



def test_report_by_ticket_amount_usecase_is_not_abstract():
    assert not inspect.isabstract(Report_by_ticket_amount_UseCase)


def test_report_by_ticket_amount_usecase_constructor_exists():
    assert callable(Report_by_ticket_amount_UseCase.__init__)


def test_report_by_ticket_amount_usecase_constructor_args():
    sig = inspect.signature(Report_by_ticket_amount_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_report_by_revenue_usecase_is_not_abstract():
    assert not inspect.isabstract(Report_by_revenue_UseCase)


def test_report_by_revenue_usecase_constructor_exists():
    assert callable(Report_by_revenue_UseCase.__init__)


def test_report_by_revenue_usecase_constructor_args():
    sig = inspect.signature(Report_by_revenue_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_statistical_reporting_usecase1_is_not_abstract():
    assert not inspect.isabstract(statistical_reporting_UseCase1)


def test_statistical_reporting_usecase1_constructor_exists():
    assert callable(statistical_reporting_UseCase1.__init__)


def test_statistical_reporting_usecase1_constructor_args():
    sig = inspect.signature(statistical_reporting_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor4_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor4)


def test_manager_actor4_constructor_exists():
    assert callable(Manager_Actor4.__init__)


def test_manager_actor4_constructor_args():
    sig = inspect.signature(Manager_Actor4.__init__)
    params = list(sig.parameters.keys())



def test_login_usecase2_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase2)


def test_login_usecase2_constructor_exists():
    assert callable(Login_UseCase2.__init__)


def test_login_usecase2_constructor_args():
    sig = inspect.signature(Login_UseCase2.__init__)
    params = list(sig.parameters.keys())



def test_delete_vehicles_usecase_is_not_abstract():
    assert not inspect.isabstract(Delete_vehicles_UseCase)


def test_delete_vehicles_usecase_constructor_exists():
    assert callable(Delete_vehicles_UseCase.__init__)


def test_delete_vehicles_usecase_constructor_args():
    sig = inspect.signature(Delete_vehicles_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_update_vehicles_information_usecase_is_not_abstract():
    assert not inspect.isabstract(Update_vehicles_information_UseCase)


def test_update_vehicles_information_usecase_constructor_exists():
    assert callable(Update_vehicles_information_UseCase.__init__)


def test_update_vehicles_information_usecase_constructor_args():
    sig = inspect.signature(Update_vehicles_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view_vehicles_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_vehicles_information_UseCase)


def test_view_vehicles_information_usecase_constructor_exists():
    assert callable(View_vehicles_information_UseCase.__init__)


def test_view_vehicles_information_usecase_constructor_args():
    sig = inspect.signature(View_vehicles_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(vehicle_management_UseCase1)


def test_vehicle_management_usecase1_constructor_exists():
    assert callable(vehicle_management_UseCase1.__init__)


def test_vehicle_management_usecase1_constructor_args():
    sig = inspect.signature(vehicle_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor3_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor3)


def test_manager_actor3_constructor_exists():
    assert callable(Manager_Actor3.__init__)


def test_manager_actor3_constructor_args():
    sig = inspect.signature(Manager_Actor3.__init__)
    params = list(sig.parameters.keys())



def test_call_for_customers_usecase_is_not_abstract():
    assert not inspect.isabstract(call_for_customers_UseCase)


def test_call_for_customers_usecase_constructor_exists():
    assert callable(call_for_customers_UseCase.__init__)


def test_call_for_customers_usecase_constructor_args():
    sig = inspect.signature(call_for_customers_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_login_usecase1_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase1)


def test_login_usecase1_constructor_exists():
    assert callable(Login_UseCase1.__init__)


def test_login_usecase1_constructor_args():
    sig = inspect.signature(Login_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_view_customers_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_customers_information_UseCase)


def test_view_customers_information_usecase_constructor_exists():
    assert callable(View_customers_information_UseCase.__init__)


def test_view_customers_information_usecase_constructor_args():
    sig = inspect.signature(View_customers_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cancel_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(cancel_booking_UseCase)


def test_cancel_booking_usecase_constructor_exists():
    assert callable(cancel_booking_UseCase.__init__)


def test_cancel_booking_usecase_constructor_args():
    sig = inspect.signature(cancel_booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_confirm_booking_usecase_is_not_abstract():
    assert not inspect.isabstract(confirm_booking_UseCase)


def test_confirm_booking_usecase_constructor_exists():
    assert callable(confirm_booking_UseCase.__init__)


def test_confirm_booking_usecase_constructor_args():
    sig = inspect.signature(confirm_booking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_customers_usecase_is_not_abstract():
    assert not inspect.isabstract(search_customers_UseCase)


def test_search_customers_usecase_constructor_exists():
    assert callable(search_customers_UseCase.__init__)


def test_search_customers_usecase_constructor_args():
    sig = inspect.signature(search_customers_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(customer_management_UseCase1)


def test_customer_management_usecase1_constructor_exists():
    assert callable(customer_management_UseCase1.__init__)


def test_customer_management_usecase1_constructor_args():
    sig = inspect.signature(customer_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor2_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor2)


def test_manager_actor2_constructor_exists():
    assert callable(Manager_Actor2.__init__)


def test_manager_actor2_constructor_args():
    sig = inspect.signature(Manager_Actor2.__init__)
    params = list(sig.parameters.keys())



def test_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(make_payment_UseCase)


def test_make_payment_usecase_constructor_exists():
    assert callable(make_payment_UseCase.__init__)


def test_make_payment_usecase_constructor_args():
    sig = inspect.signature(make_payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view_account_information_usecase_is_not_abstract():
    assert not inspect.isabstract(View_account_information_UseCase)


def test_view_account_information_usecase_constructor_exists():
    assert callable(View_account_information_UseCase.__init__)


def test_view_account_information_usecase_constructor_args():
    sig = inspect.signature(View_account_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_account_settings_usecase_is_not_abstract():
    assert not inspect.isabstract(Account_settings_UseCase)


def test_account_settings_usecase_constructor_exists():
    assert callable(Account_settings_UseCase.__init__)


def test_account_settings_usecase_constructor_args():
    sig = inspect.signature(Account_settings_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_account_management_usecase1_is_not_abstract():
    assert not inspect.isabstract(account_management_UseCase1)


def test_account_management_usecase1_constructor_exists():
    assert callable(account_management_UseCase1.__init__)


def test_account_management_usecase1_constructor_args():
    sig = inspect.signature(account_management_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor1_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor1)


def test_manager_actor1_constructor_exists():
    assert callable(Manager_Actor1.__init__)


def test_manager_actor1_constructor_args():
    sig = inspect.signature(Manager_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_search_usecase_is_not_abstract():
    assert not inspect.isabstract(search_UseCase)


def test_search_usecase_constructor_exists():
    assert callable(search_UseCase.__init__)


def test_search_usecase_constructor_args():
    sig = inspect.signature(search_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_confirm_information_usecase_is_not_abstract():
    assert not inspect.isabstract(confirm_information_UseCase)


def test_confirm_information_usecase_constructor_exists():
    assert callable(confirm_information_UseCase.__init__)


def test_confirm_information_usecase_constructor_args():
    sig = inspect.signature(confirm_information_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_choose_seats_usecase_is_not_abstract():
    assert not inspect.isabstract(choose_seats_UseCase)


def test_choose_seats_usecase_constructor_exists():
    assert callable(choose_seats_UseCase.__init__)


def test_choose_seats_usecase_constructor_args():
    sig = inspect.signature(choose_seats_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_choose_vehicle_usecase_is_not_abstract():
    assert not inspect.isabstract(choose_vehicle_UseCase)


def test_choose_vehicle_usecase_constructor_exists():
    assert callable(choose_vehicle_UseCase.__init__)


def test_choose_vehicle_usecase_constructor_args():
    sig = inspect.signature(choose_vehicle_UseCase.__init__)
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
book_ticket_UseCase_strategy = st.builds(
    book_ticket_UseCase,
)
Customer_Actor1_strategy = st.builds(
    Customer_Actor1,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
statistical_reporting_UseCase_strategy = st.builds(
    statistical_reporting_UseCase,
)
vehicle_management_UseCase_strategy = st.builds(
    vehicle_management_UseCase,
)
account_management_UseCase_strategy = st.builds(
    account_management_UseCase,
)
customer_management_UseCase_strategy = st.builds(
    customer_management_UseCase,
)
Use_Actor_strategy = st.builds(
    Use_Actor,
)
Book_ticket_UseCase_strategy = st.builds(
    Book_ticket_UseCase,
)
Search_the_route_UseCase_strategy = st.builds(
    Search_the_route_UseCase,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)
accoutUser_strategy = st.builds(
    accoutUser,
    codeConfirm=
        safe_text,
    idCompany=
        st.integers(),
    emailUser=
        safe_text,
    dateRegister=
        safe_text,
    idUser=
        st.integers(),
    passwordUser=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    idCustomer=
        st.integers(),
    idCar=
        st.integers(),
    idTicket=
        st.integers(),
    code=
        safe_text,
    timeExchange=
        safe_text,
    statusSeat=
        st.integers(),
    positionSeat=
        safe_text,
    numberSeat=
        st.integers(),
    positionSeatBelow=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    emailCustomer=
        safe_text,
    phoneCustomer=
        safe_text,
    idCustomer=
        st.integers(),
    nameCustomer=
        safe_text
)
infoCompany_strategy = st.builds(
    infoCompany,
    idCompany=
        st.integers(),
    nameCompany=
        safe_text,
    dateEstablish=
        safe_text,
    describeCompany=
        safe_text,
    addressCompany=
        safe_text,
    showSafe=
        safe_text,
    dateUpdate=
        safe_text,
    dateRegister=
        safe_text,
    phoneCompany=
        safe_text
)
mapCarExchange_strategy = st.builds(
    mapCarExchange,
    mapOnCar=
        safe_text,
    idMap=
        st.integers(),
    idCar=
        st.integers(),
    timeExchange=
        safe_text,
    mapBelowCar=
        safe_text
)
Car_strategy = st.builds(
    Car,
    idUser=
        st.integers(),
    statusCar=
        st.integers(),
    timeStartCar=
        safe_text,
    fareCar=
        safe_text,
    positionEndCar=
        safe_text,
    idCar=
        st.integers(),
    classifyCar=
        st.integers(),
    positionStartCar=
        safe_text,
    mapOnCar=
        safe_text,
    mapBelowCar=
        safe_text,
    numberPlatesCar=
        safe_text,
    phoneCar=
        safe_text,
    imageLinkCar=
        safe_text,
    nameCar=
        safe_text
)
Login_UseCase3_strategy = st.builds(
    Login_UseCase3,
)
Report_by_ticket_amount_UseCase_strategy = st.builds(
    Report_by_ticket_amount_UseCase,
)
Report_by_revenue_UseCase_strategy = st.builds(
    Report_by_revenue_UseCase,
)
statistical_reporting_UseCase1_strategy = st.builds(
    statistical_reporting_UseCase1,
)
Manager_Actor4_strategy = st.builds(
    Manager_Actor4,
)
Login_UseCase2_strategy = st.builds(
    Login_UseCase2,
)
Delete_vehicles_UseCase_strategy = st.builds(
    Delete_vehicles_UseCase,
)
Update_vehicles_information_UseCase_strategy = st.builds(
    Update_vehicles_information_UseCase,
)
View_vehicles_information_UseCase_strategy = st.builds(
    View_vehicles_information_UseCase,
)
vehicle_management_UseCase1_strategy = st.builds(
    vehicle_management_UseCase1,
)
Manager_Actor3_strategy = st.builds(
    Manager_Actor3,
)
call_for_customers_UseCase_strategy = st.builds(
    call_for_customers_UseCase,
)
Login_UseCase1_strategy = st.builds(
    Login_UseCase1,
)
View_customers_information_UseCase_strategy = st.builds(
    View_customers_information_UseCase,
)
cancel_booking_UseCase_strategy = st.builds(
    cancel_booking_UseCase,
)
confirm_booking_UseCase_strategy = st.builds(
    confirm_booking_UseCase,
)
search_customers_UseCase_strategy = st.builds(
    search_customers_UseCase,
)
customer_management_UseCase1_strategy = st.builds(
    customer_management_UseCase1,
)
Manager_Actor2_strategy = st.builds(
    Manager_Actor2,
)
make_payment_UseCase_strategy = st.builds(
    make_payment_UseCase,
)
View_account_information_UseCase_strategy = st.builds(
    View_account_information_UseCase,
)
Account_settings_UseCase_strategy = st.builds(
    Account_settings_UseCase,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)
account_management_UseCase1_strategy = st.builds(
    account_management_UseCase1,
)
Manager_Actor1_strategy = st.builds(
    Manager_Actor1,
)
search_UseCase_strategy = st.builds(
    search_UseCase,
)
confirm_information_UseCase_strategy = st.builds(
    confirm_information_UseCase,
)
choose_seats_UseCase_strategy = st.builds(
    choose_seats_UseCase,
)
choose_vehicle_UseCase_strategy = st.builds(
    choose_vehicle_UseCase,
)

@given(instance=book_ticket_UseCase_strategy)
@settings(max_examples=50)
def test_book_ticket_usecase_instantiation(instance):
    assert isinstance(instance, book_ticket_UseCase)

@given(instance=Customer_Actor1_strategy)
@settings(max_examples=50)
def test_customer_actor1_instantiation(instance):
    assert isinstance(instance, Customer_Actor1)

@given(instance=Manager_Actor_strategy)
@settings(max_examples=50)
def test_manager_actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)

@given(instance=statistical_reporting_UseCase_strategy)
@settings(max_examples=50)
def test_statistical_reporting_usecase_instantiation(instance):
    assert isinstance(instance, statistical_reporting_UseCase)

@given(instance=vehicle_management_UseCase_strategy)
@settings(max_examples=50)
def test_vehicle_management_usecase_instantiation(instance):
    assert isinstance(instance, vehicle_management_UseCase)

@given(instance=account_management_UseCase_strategy)
@settings(max_examples=50)
def test_account_management_usecase_instantiation(instance):
    assert isinstance(instance, account_management_UseCase)

@given(instance=customer_management_UseCase_strategy)
@settings(max_examples=50)
def test_customer_management_usecase_instantiation(instance):
    assert isinstance(instance, customer_management_UseCase)

@given(instance=Use_Actor_strategy)
@settings(max_examples=50)
def test_use_actor_instantiation(instance):
    assert isinstance(instance, Use_Actor)

@given(instance=Book_ticket_UseCase_strategy)
@settings(max_examples=50)
def test_book_ticket_usecase_instantiation(instance):
    assert isinstance(instance, Book_ticket_UseCase)

@given(instance=Search_the_route_UseCase_strategy)
@settings(max_examples=50)
def test_search_the_route_usecase_instantiation(instance):
    assert isinstance(instance, Search_the_route_UseCase)

@given(instance=Customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)

@given(instance=accoutUser_strategy)
@settings(max_examples=50)
def test_accoutuser_instantiation(instance):
    assert isinstance(instance, accoutUser)



@given(instance=accoutUser_strategy)
def test_accoutuser_codeConfirm_setter(instance):
    original = instance.codeConfirm
    instance.codeConfirm = original
    assert instance.codeConfirm == original



@given(instance=accoutUser_strategy)
def test_accoutuser_idCompany_setter(instance):
    original = instance.idCompany
    instance.idCompany = original
    assert instance.idCompany == original



@given(instance=accoutUser_strategy)
def test_accoutuser_emailUser_setter(instance):
    original = instance.emailUser
    instance.emailUser = original
    assert instance.emailUser == original



@given(instance=accoutUser_strategy)
def test_accoutuser_dateRegister_setter(instance):
    original = instance.dateRegister
    instance.dateRegister = original
    assert instance.dateRegister == original



@given(instance=accoutUser_strategy)
def test_accoutuser_idUser_setter(instance):
    original = instance.idUser
    instance.idUser = original
    assert instance.idUser == original



@given(instance=accoutUser_strategy)
def test_accoutuser_passwordUser_setter(instance):
    original = instance.passwordUser
    instance.passwordUser = original
    assert instance.passwordUser == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_idCustomer_setter(instance):
    original = instance.idCustomer
    instance.idCustomer = original
    assert instance.idCustomer == original



@given(instance=Ticket_strategy)
def test_ticket_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=Ticket_strategy)
def test_ticket_idTicket_setter(instance):
    original = instance.idTicket
    instance.idTicket = original
    assert instance.idTicket == original



@given(instance=Ticket_strategy)
def test_ticket_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Ticket_strategy)
def test_ticket_timeExchange_setter(instance):
    original = instance.timeExchange
    instance.timeExchange = original
    assert instance.timeExchange == original



@given(instance=Ticket_strategy)
def test_ticket_statusSeat_setter(instance):
    original = instance.statusSeat
    instance.statusSeat = original
    assert instance.statusSeat == original



@given(instance=Ticket_strategy)
def test_ticket_positionSeat_setter(instance):
    original = instance.positionSeat
    instance.positionSeat = original
    assert instance.positionSeat == original



@given(instance=Ticket_strategy)
def test_ticket_numberSeat_setter(instance):
    original = instance.numberSeat
    instance.numberSeat = original
    assert instance.numberSeat == original



@given(instance=Ticket_strategy)
def test_ticket_positionSeatBelow_setter(instance):
    original = instance.positionSeatBelow
    instance.positionSeatBelow = original
    assert instance.positionSeatBelow == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_emailCustomer_setter(instance):
    original = instance.emailCustomer
    instance.emailCustomer = original
    assert instance.emailCustomer == original



@given(instance=Customer_strategy)
def test_customer_phoneCustomer_setter(instance):
    original = instance.phoneCustomer
    instance.phoneCustomer = original
    assert instance.phoneCustomer == original



@given(instance=Customer_strategy)
def test_customer_idCustomer_setter(instance):
    original = instance.idCustomer
    instance.idCustomer = original
    assert instance.idCustomer == original



@given(instance=Customer_strategy)
def test_customer_nameCustomer_setter(instance):
    original = instance.nameCustomer
    instance.nameCustomer = original
    assert instance.nameCustomer == original

@given(instance=infoCompany_strategy)
@settings(max_examples=50)
def test_infocompany_instantiation(instance):
    assert isinstance(instance, infoCompany)



@given(instance=infoCompany_strategy)
def test_infocompany_idCompany_setter(instance):
    original = instance.idCompany
    instance.idCompany = original
    assert instance.idCompany == original



@given(instance=infoCompany_strategy)
def test_infocompany_nameCompany_setter(instance):
    original = instance.nameCompany
    instance.nameCompany = original
    assert instance.nameCompany == original



@given(instance=infoCompany_strategy)
def test_infocompany_dateEstablish_setter(instance):
    original = instance.dateEstablish
    instance.dateEstablish = original
    assert instance.dateEstablish == original



@given(instance=infoCompany_strategy)
def test_infocompany_describeCompany_setter(instance):
    original = instance.describeCompany
    instance.describeCompany = original
    assert instance.describeCompany == original



@given(instance=infoCompany_strategy)
def test_infocompany_addressCompany_setter(instance):
    original = instance.addressCompany
    instance.addressCompany = original
    assert instance.addressCompany == original



@given(instance=infoCompany_strategy)
def test_infocompany_showSafe_setter(instance):
    original = instance.showSafe
    instance.showSafe = original
    assert instance.showSafe == original



@given(instance=infoCompany_strategy)
def test_infocompany_dateUpdate_setter(instance):
    original = instance.dateUpdate
    instance.dateUpdate = original
    assert instance.dateUpdate == original



@given(instance=infoCompany_strategy)
def test_infocompany_dateRegister_setter(instance):
    original = instance.dateRegister
    instance.dateRegister = original
    assert instance.dateRegister == original



@given(instance=infoCompany_strategy)
def test_infocompany_phoneCompany_setter(instance):
    original = instance.phoneCompany
    instance.phoneCompany = original
    assert instance.phoneCompany == original

@given(instance=mapCarExchange_strategy)
@settings(max_examples=50)
def test_mapcarexchange_instantiation(instance):
    assert isinstance(instance, mapCarExchange)



@given(instance=mapCarExchange_strategy)
def test_mapcarexchange_mapOnCar_setter(instance):
    original = instance.mapOnCar
    instance.mapOnCar = original
    assert instance.mapOnCar == original



@given(instance=mapCarExchange_strategy)
def test_mapcarexchange_idMap_setter(instance):
    original = instance.idMap
    instance.idMap = original
    assert instance.idMap == original



@given(instance=mapCarExchange_strategy)
def test_mapcarexchange_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=mapCarExchange_strategy)
def test_mapcarexchange_timeExchange_setter(instance):
    original = instance.timeExchange
    instance.timeExchange = original
    assert instance.timeExchange == original



@given(instance=mapCarExchange_strategy)
def test_mapcarexchange_mapBelowCar_setter(instance):
    original = instance.mapBelowCar
    instance.mapBelowCar = original
    assert instance.mapBelowCar == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)



@given(instance=Car_strategy)
def test_car_idUser_setter(instance):
    original = instance.idUser
    instance.idUser = original
    assert instance.idUser == original



@given(instance=Car_strategy)
def test_car_statusCar_setter(instance):
    original = instance.statusCar
    instance.statusCar = original
    assert instance.statusCar == original



@given(instance=Car_strategy)
def test_car_timeStartCar_setter(instance):
    original = instance.timeStartCar
    instance.timeStartCar = original
    assert instance.timeStartCar == original



@given(instance=Car_strategy)
def test_car_fareCar_setter(instance):
    original = instance.fareCar
    instance.fareCar = original
    assert instance.fareCar == original



@given(instance=Car_strategy)
def test_car_positionEndCar_setter(instance):
    original = instance.positionEndCar
    instance.positionEndCar = original
    assert instance.positionEndCar == original



@given(instance=Car_strategy)
def test_car_idCar_setter(instance):
    original = instance.idCar
    instance.idCar = original
    assert instance.idCar == original



@given(instance=Car_strategy)
def test_car_classifyCar_setter(instance):
    original = instance.classifyCar
    instance.classifyCar = original
    assert instance.classifyCar == original



@given(instance=Car_strategy)
def test_car_positionStartCar_setter(instance):
    original = instance.positionStartCar
    instance.positionStartCar = original
    assert instance.positionStartCar == original



@given(instance=Car_strategy)
def test_car_mapOnCar_setter(instance):
    original = instance.mapOnCar
    instance.mapOnCar = original
    assert instance.mapOnCar == original



@given(instance=Car_strategy)
def test_car_mapBelowCar_setter(instance):
    original = instance.mapBelowCar
    instance.mapBelowCar = original
    assert instance.mapBelowCar == original



@given(instance=Car_strategy)
def test_car_numberPlatesCar_setter(instance):
    original = instance.numberPlatesCar
    instance.numberPlatesCar = original
    assert instance.numberPlatesCar == original



@given(instance=Car_strategy)
def test_car_phoneCar_setter(instance):
    original = instance.phoneCar
    instance.phoneCar = original
    assert instance.phoneCar == original



@given(instance=Car_strategy)
def test_car_imageLinkCar_setter(instance):
    original = instance.imageLinkCar
    instance.imageLinkCar = original
    assert instance.imageLinkCar == original



@given(instance=Car_strategy)
def test_car_nameCar_setter(instance):
    original = instance.nameCar
    instance.nameCar = original
    assert instance.nameCar == original

@given(instance=Login_UseCase3_strategy)
@settings(max_examples=50)
def test_login_usecase3_instantiation(instance):
    assert isinstance(instance, Login_UseCase3)

@given(instance=Report_by_ticket_amount_UseCase_strategy)
@settings(max_examples=50)
def test_report_by_ticket_amount_usecase_instantiation(instance):
    assert isinstance(instance, Report_by_ticket_amount_UseCase)

@given(instance=Report_by_revenue_UseCase_strategy)
@settings(max_examples=50)
def test_report_by_revenue_usecase_instantiation(instance):
    assert isinstance(instance, Report_by_revenue_UseCase)

@given(instance=statistical_reporting_UseCase1_strategy)
@settings(max_examples=50)
def test_statistical_reporting_usecase1_instantiation(instance):
    assert isinstance(instance, statistical_reporting_UseCase1)

@given(instance=Manager_Actor4_strategy)
@settings(max_examples=50)
def test_manager_actor4_instantiation(instance):
    assert isinstance(instance, Manager_Actor4)

@given(instance=Login_UseCase2_strategy)
@settings(max_examples=50)
def test_login_usecase2_instantiation(instance):
    assert isinstance(instance, Login_UseCase2)

@given(instance=Delete_vehicles_UseCase_strategy)
@settings(max_examples=50)
def test_delete_vehicles_usecase_instantiation(instance):
    assert isinstance(instance, Delete_vehicles_UseCase)

@given(instance=Update_vehicles_information_UseCase_strategy)
@settings(max_examples=50)
def test_update_vehicles_information_usecase_instantiation(instance):
    assert isinstance(instance, Update_vehicles_information_UseCase)

@given(instance=View_vehicles_information_UseCase_strategy)
@settings(max_examples=50)
def test_view_vehicles_information_usecase_instantiation(instance):
    assert isinstance(instance, View_vehicles_information_UseCase)

@given(instance=vehicle_management_UseCase1_strategy)
@settings(max_examples=50)
def test_vehicle_management_usecase1_instantiation(instance):
    assert isinstance(instance, vehicle_management_UseCase1)

@given(instance=Manager_Actor3_strategy)
@settings(max_examples=50)
def test_manager_actor3_instantiation(instance):
    assert isinstance(instance, Manager_Actor3)

@given(instance=call_for_customers_UseCase_strategy)
@settings(max_examples=50)
def test_call_for_customers_usecase_instantiation(instance):
    assert isinstance(instance, call_for_customers_UseCase)

@given(instance=Login_UseCase1_strategy)
@settings(max_examples=50)
def test_login_usecase1_instantiation(instance):
    assert isinstance(instance, Login_UseCase1)

@given(instance=View_customers_information_UseCase_strategy)
@settings(max_examples=50)
def test_view_customers_information_usecase_instantiation(instance):
    assert isinstance(instance, View_customers_information_UseCase)

@given(instance=cancel_booking_UseCase_strategy)
@settings(max_examples=50)
def test_cancel_booking_usecase_instantiation(instance):
    assert isinstance(instance, cancel_booking_UseCase)

@given(instance=confirm_booking_UseCase_strategy)
@settings(max_examples=50)
def test_confirm_booking_usecase_instantiation(instance):
    assert isinstance(instance, confirm_booking_UseCase)

@given(instance=search_customers_UseCase_strategy)
@settings(max_examples=50)
def test_search_customers_usecase_instantiation(instance):
    assert isinstance(instance, search_customers_UseCase)

@given(instance=customer_management_UseCase1_strategy)
@settings(max_examples=50)
def test_customer_management_usecase1_instantiation(instance):
    assert isinstance(instance, customer_management_UseCase1)

@given(instance=Manager_Actor2_strategy)
@settings(max_examples=50)
def test_manager_actor2_instantiation(instance):
    assert isinstance(instance, Manager_Actor2)

@given(instance=make_payment_UseCase_strategy)
@settings(max_examples=50)
def test_make_payment_usecase_instantiation(instance):
    assert isinstance(instance, make_payment_UseCase)

@given(instance=View_account_information_UseCase_strategy)
@settings(max_examples=50)
def test_view_account_information_usecase_instantiation(instance):
    assert isinstance(instance, View_account_information_UseCase)

@given(instance=Account_settings_UseCase_strategy)
@settings(max_examples=50)
def test_account_settings_usecase_instantiation(instance):
    assert isinstance(instance, Account_settings_UseCase)

@given(instance=Login_UseCase_strategy)
@settings(max_examples=50)
def test_login_usecase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)

@given(instance=account_management_UseCase1_strategy)
@settings(max_examples=50)
def test_account_management_usecase1_instantiation(instance):
    assert isinstance(instance, account_management_UseCase1)

@given(instance=Manager_Actor1_strategy)
@settings(max_examples=50)
def test_manager_actor1_instantiation(instance):
    assert isinstance(instance, Manager_Actor1)

@given(instance=search_UseCase_strategy)
@settings(max_examples=50)
def test_search_usecase_instantiation(instance):
    assert isinstance(instance, search_UseCase)

@given(instance=confirm_information_UseCase_strategy)
@settings(max_examples=50)
def test_confirm_information_usecase_instantiation(instance):
    assert isinstance(instance, confirm_information_UseCase)

@given(instance=choose_seats_UseCase_strategy)
@settings(max_examples=50)
def test_choose_seats_usecase_instantiation(instance):
    assert isinstance(instance, choose_seats_UseCase)

@given(instance=choose_vehicle_UseCase_strategy)
@settings(max_examples=50)
def test_choose_vehicle_usecase_instantiation(instance):
    assert isinstance(instance, choose_vehicle_UseCase)
