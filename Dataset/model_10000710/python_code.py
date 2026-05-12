from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TicketBuyType(Enum):
    pass
class ProviderType(Enum):
    pass
class FlightType(Enum):
    pass
class TicketPayment(Enum):
    pass
class GenderType(Enum):
    pass
class EmployeeType(Enum):
    pass
class ReportType(Enum):
    pass
class PlaneState(Enum):
    pass

############################################
# Definition of Classes
############################################







class Send_Luggage_To_Loading_UseCase:

    pass


class Print_Luggage_Ticket_UseCase:

    pass


class Add_A_Luggage_UseCase:

    pass


class Consult_Luggage_Ticket_Infos_UseCase:

    pass


class Luggage_Checkin_UseCase:

    pass


class AsksForFreeFlight_UseCase:

    pass


class CheckEligibility__FreeMiles__UseCase:

    pass


class Surbooking_UseCase:

    pass


class TicketsAveragePrice_UseCase:

    pass


class TicketsPrice_UseCase:

    pass


class Customers_UseCase:

    pass


class Charges_UseCase:

    pass


class Flights_UseCase:

    pass


class Resources_UseCase:

    pass


class CheckReportInFolder_UseCase:

    pass


class GenerateReport_UseCase:

    pass


class Promotion_UseCase:

    pass


class Company_Actor:

    pass


class Consomation_UseCase:

    pass


class Reparation_UseCase:

    pass


class Service_UseCase:

    pass


class Fuel_UseCase:

    pass


class ChooseProvider_UseCase:

    pass


class FillConsomationStock_UseCase:

    pass


class AirportAdministration_Actor:

    pass


class CleaningService_UseCase:

    pass


class Immobilisation_UseCase:

    pass


class Refuel_UseCase:

    pass


class Revision_UseCase:

    pass


class Intervention_UseCase:

    pass


class Plane_Actor:

    pass


class CheckConsomationStock_UseCase:

    pass


class SellConsomation_UseCase:

    pass


class Steward_Actor:

    pass


class CheckConsomationCatalogue_UseCase:

    pass


class BuyConsomation_UseCase:

    pass


class StartBoarding_UseCase:

    pass


class PrintLuggageBadge_UseCase:

    pass


class AddABagage_UseCase:

    pass


class LuggageCheckIn_UseCase:

    pass


class ProcessWaitingList_UseCase:

    pass


class CloseCheckIn_UseCase:

    pass


class RegisterToWaitingList_UseCase:

    pass


class CheckAvailability_UseCase:

    pass


class AddASurbooking_UseCase:

    pass


class WaitingList_UseCase:

    pass


class ChangeSeat_UseCase:

    pass


class CheckSeat_UseCase:

    pass


class CheckInformations_UseCase:

    pass


class CheckInForFlight_UseCase:

    pass


class ByBookingNumber_UseCase:

    pass


class ByName_UseCase:

    pass


class PassengerIdentification_UseCase:

    pass


class PassengerCheckIn_UseCase:

    pass


class Distribute_UseCase:

    pass


class Seller_Actor:

    pass


class OnlineBuy_UseCase:

    pass


class Customer_Actor:

    pass


class Employee_Actor:

    pass


class Admin_Actor:

    pass


class User_Actor:

    pass





class EditPlanning_external:

    pass


class Advertising_external:

    pass


class Promotion_System_external:

    pass


class SetTaxes_external:

    pass


class SetDestinationPrice_external:

    pass


class SearchEmployee_external:

    pass


class PlanningCheck_external:

    pass


class DeleteEmployee_external:

    pass


class EditEmployee_external:

    pass


class AddEmployee_external:

    pass


class CheckPlanning_external:

    pass


class CancelFlight_external:

    pass


class EditFlight_external:

    pass


class CreateFlight_external:

    pass


class ProviderSystem_ConsomationStock:

    def __init__(self, _capacity: int, consomation86: set["ProviderSystem_Consomation"] = None, plane23: "FlightSystem_Plane" = None):
        self._capacity = _capacity
        self.consomation86 = consomation86 if consomation86 is not None else set()
        self.plane23 = plane23
        
        pass
    @property
    def _capacity(self):
        return self.___capacity
    @_capacity.setter
    def _capacity(self, _capacity: int):
        self.___capacity = _capacity

    @property
    def consomation86(self):
        return self.__consomation86
    @consomation86.setter
    def consomation86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_ConsomationStock__consomation86", None)
        self.__consomation86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consomationStock87"):
                    opp_val = getattr(item, "consomationStock87", None)
                    
                    if opp_val == self:
                        setattr(item, "consomationStock87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consomationStock87"):
                    opp_val = getattr(item, "consomationStock87", None)
                    
                    setattr(item, "consomationStock87", self)
                    

    @property
    def plane23(self):
        return self.__plane23
    @plane23.setter
    def plane23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_ConsomationStock__plane23", None)
        self.__plane23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consomationStock22"):
                opp_val = getattr(old_value, "consomationStock22", None)
                if opp_val == self:
                    setattr(old_value, "consomationStock22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consomationStock22"):
                opp_val = getattr(value, "consomationStock22", None)
                setattr(value, "consomationStock22", self)



class ProviderSystem_Provider:

    def __init__(self, pricePerUnit: int, name: str, consomation88: set["ProviderSystem_Consomation"] = None, fuel12: set["ProviderSystem_Fuel"] = None, airport21: set["Company_Airport"] = None):
        self.pricePerUnit = pricePerUnit
        self.name = name
        self.consomation88 = consomation88 if consomation88 is not None else set()
        self.fuel12 = fuel12 if fuel12 is not None else set()
        self.airport21 = airport21 if airport21 is not None else set()
        
        pass
    @property
    def pricePerUnit(self):
        return self.__pricePerUnit
    @pricePerUnit.setter
    def pricePerUnit(self, pricePerUnit: int):
        self.__pricePerUnit = pricePerUnit

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuel12(self):
        return self.__fuel12
    @fuel12.setter
    def fuel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Provider__fuel12", None)
        self.__fuel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuelProvider13"):
                    opp_val = getattr(item, "fuelProvider13", None)
                    
                    if opp_val == self:
                        setattr(item, "fuelProvider13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuelProvider13"):
                    opp_val = getattr(item, "fuelProvider13", None)
                    
                    setattr(item, "fuelProvider13", self)
                    

    @property
    def airport21(self):
        return self.__airport21
    @airport21.setter
    def airport21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Provider__airport21", None)
        self.__airport21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "provider20"):
                    opp_val = getattr(item, "provider20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "provider20"):
                    opp_val = getattr(item, "provider20", None)
                    
                    if opp_val is None:
                        setattr(item, "provider20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def consomation88(self):
        return self.__consomation88
    @consomation88.setter
    def consomation88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Provider__consomation88", None)
        self.__consomation88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consomationProvider89"):
                    opp_val = getattr(item, "consomationProvider89", None)
                    
                    if opp_val == self:
                        setattr(item, "consomationProvider89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consomationProvider89"):
                    opp_val = getattr(item, "consomationProvider89", None)
                    
                    setattr(item, "consomationProvider89", self)
                    



class ProviderSystem_Consomation:

    def __init__(self, name: str, pricePerUnit: int, consomationStock87: "ProviderSystem_ConsomationStock" = None, consomationProvider89: "ProviderSystem_Provider" = None):
        self.name = name
        self.pricePerUnit = pricePerUnit
        self.consomationStock87 = consomationStock87
        self.consomationProvider89 = consomationProvider89
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pricePerUnit(self):
        return self.__pricePerUnit
    @pricePerUnit.setter
    def pricePerUnit(self, pricePerUnit: int):
        self.__pricePerUnit = pricePerUnit

    @property
    def consomationProvider89(self):
        return self.__consomationProvider89
    @consomationProvider89.setter
    def consomationProvider89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Consomation__consomationProvider89", None)
        self.__consomationProvider89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consomation88"):
                opp_val = getattr(old_value, "consomation88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consomation88"):
                opp_val = getattr(value, "consomation88", None)
                if opp_val is None:
                    setattr(value, "consomation88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consomationStock87(self):
        return self.__consomationStock87
    @consomationStock87.setter
    def consomationStock87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Consomation__consomationStock87", None)
        self.__consomationStock87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consomation86"):
                opp_val = getattr(old_value, "consomation86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consomation86"):
                opp_val = getattr(value, "consomation86", None)
                if opp_val is None:
                    setattr(value, "consomation86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ProviderSystem_Fuel:

    def __init__(self, date: date, _price: int, volme: int, plane: FlightSystem_Plane, fuelProvider13: "ProviderSystem_Provider" = None):
        self.date = date
        self._price = _price
        self.volme = volme
        self.plane = plane
        self.fuelProvider13 = fuelProvider13
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def plane(self):
        return self.__plane
    @plane.setter
    def plane(self, plane: FlightSystem_Plane):
        self.__plane = plane

    @property
    def volme(self):
        return self.__volme
    @volme.setter
    def volme(self, volme: int):
        self.__volme = volme

    @property
    def _price(self):
        return self.___price
    @_price.setter
    def _price(self, _price: int):
        self.___price = _price

    @property
    def fuelProvider13(self):
        return self.__fuelProvider13
    @fuelProvider13.setter
    def fuelProvider13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProviderSystem_Fuel__fuelProvider13", None)
        self.__fuelProvider13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuel12"):
                opp_val = getattr(old_value, "fuel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuel12"):
                opp_val = getattr(value, "fuel12", None)
                if opp_val is None:
                    setattr(value, "fuel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Employee_Actor2:

    pass


class Distribute_UseCase1:

    pass


class Customer_Actor2:

    pass


class AirportAdministration_Actor2:

    pass


class Taxes_Component:

    pass


class Marketting_Component:

    pass


class Company_Actor1:

    pass


class AirportAdministration_Actor1:

    pass


class Customer_Actor1:

    pass


class Employee_Actor1:

    pass


class User_Actor1:

    pass


class UI_FlightPlanning_Component:

    pass


class UI_FlightManager_Component:

    pass


class UI_EmployeePlanning_Component:

    pass


class UI_EmployeeManager_Component:

    pass


class Admin_Actor1:

    pass


class DistributionSystem_TicketDistributor:

    def __init__(self, from1: TicketBuyType, payment: TicketPayment, company19: "Company_Company" = None):
        self.from1 = from1
        self.payment = payment
        self.company19 = company19
        
        pass
    @property
    def from1(self):
        return self.__from1
    @from1.setter
    def from1(self, from1: TicketBuyType):
        self.__from1 = from1

    @property
    def payment(self):
        return self.__payment
    @payment.setter
    def payment(self, payment: TicketPayment):
        self.__payment = payment

    @property
    def company19(self):
        return self.__company19
    @company19.setter
    def company19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_TicketDistributor__company19", None)
        self.__company19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticketDistributor18"):
                opp_val = getattr(old_value, "ticketDistributor18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticketDistributor18"):
                opp_val = getattr(value, "ticketDistributor18", None)
                if opp_val is None:
                    setattr(value, "ticketDistributor18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class DistributionSystem_Customer:

    def __init__(self, _milesFlyed: int, Luggage: str, name: str, boardingPass8: set["DistributionSystem_BoardingPass"] = None):
        self._milesFlyed = _milesFlyed
        self.Luggage = Luggage
        self.name = name
        self.boardingPass8 = boardingPass8 if boardingPass8 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Luggage(self):
        return self.__Luggage
    @Luggage.setter
    def Luggage(self, Luggage: str):
        self.__Luggage = Luggage

    @property
    def _milesFlyed(self):
        return self.___milesFlyed
    @_milesFlyed.setter
    def _milesFlyed(self, _milesFlyed: int):
        self.___milesFlyed = _milesFlyed

    @property
    def boardingPass8(self):
        return self.__boardingPass8
    @boardingPass8.setter
    def boardingPass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_Customer__boardingPass8", None)
        self.__boardingPass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    if opp_val == self:
                        setattr(item, "customer9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    setattr(item, "customer9", self)
                    



class DistributionSystem_BoardingPass:

    def __init__(self, price: int, row: int, seat: int, isValidated: bool, dateOfPurchase: date, flight: str, customer9: "DistributionSystem_Customer" = None, ticket11: "DistributionSystem_Ticket" = None):
        self.price = price
        self.row = row
        self.seat = seat
        self.isValidated = isValidated
        self.dateOfPurchase = dateOfPurchase
        self.flight = flight
        self.customer9 = customer9
        self.ticket11 = ticket11
        
        pass
    @property
    def row(self):
        return self.__row
    @row.setter
    def row(self, row: int):
        self.__row = row

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def flight(self):
        return self.__flight
    @flight.setter
    def flight(self, flight: str):
        self.__flight = flight

    @property
    def seat(self):
        return self.__seat
    @seat.setter
    def seat(self, seat: int):
        self.__seat = seat

    @property
    def dateOfPurchase(self):
        return self.__dateOfPurchase
    @dateOfPurchase.setter
    def dateOfPurchase(self, dateOfPurchase: date):
        self.__dateOfPurchase = dateOfPurchase

    @property
    def isValidated(self):
        return self.__isValidated
    @isValidated.setter
    def isValidated(self, isValidated: bool):
        self.__isValidated = isValidated

    @property
    def ticket11(self):
        return self.__ticket11
    @ticket11.setter
    def ticket11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_BoardingPass__ticket11", None)
        self.__ticket11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boardingPass10"):
                opp_val = getattr(old_value, "boardingPass10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boardingPass10"):
                opp_val = getattr(value, "boardingPass10", None)
                if opp_val is None:
                    setattr(value, "boardingPass10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_BoardingPass__customer9", None)
        self.__customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boardingPass8"):
                opp_val = getattr(old_value, "boardingPass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boardingPass8"):
                opp_val = getattr(value, "boardingPass8", None)
                if opp_val is None:
                    setattr(value, "boardingPass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class DistributionSystem_Ticket:

    def __init__(self, from1: TicketBuyType, payment: TicketPayment, _price: int, isRegistered: bool, _numberPlace: int, boardingPass10: set["DistributionSystem_BoardingPass"] = None, flight16: "FlightSystem_Flight" = None):
        self.from1 = from1
        self.payment = payment
        self._price = _price
        self.isRegistered = isRegistered
        self._numberPlace = _numberPlace
        self.boardingPass10 = boardingPass10 if boardingPass10 is not None else set()
        self.flight16 = flight16
        
        pass
    @property
    def isRegistered(self):
        return self.__isRegistered
    @isRegistered.setter
    def isRegistered(self, isRegistered: bool):
        self.__isRegistered = isRegistered

    @property
    def _numberPlace(self):
        return self.___numberPlace
    @_numberPlace.setter
    def _numberPlace(self, _numberPlace: int):
        self.___numberPlace = _numberPlace

    @property
    def _price(self):
        return self.___price
    @_price.setter
    def _price(self, _price: int):
        self.___price = _price

    @property
    def payment(self):
        return self.__payment
    @payment.setter
    def payment(self, payment: TicketPayment):
        self.__payment = payment

    @property
    def from1(self):
        return self.__from1
    @from1.setter
    def from1(self, from1: TicketBuyType):
        self.__from = from1

    @property
    def boardingPass10(self):
        return self.__boardingPass10
    @boardingPass10.setter
    def boardingPass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_Ticket__boardingPass10", None)
        self.__boardingPass10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ticket11"):
                    opp_val = getattr(item, "ticket11", None)
                    
                    if opp_val == self:
                        setattr(item, "ticket11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ticket11"):
                    opp_val = getattr(item, "ticket11", None)
                    
                    setattr(item, "ticket11", self)
                    

    @property
    def flight16(self):
        return self.__flight16
    @flight16.setter
    def flight16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DistributionSystem_Ticket__flight16", None)
        self.__flight16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket17"):
                opp_val = getattr(old_value, "ticket17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket17"):
                opp_val = getattr(value, "ticket17", None)
                if opp_val is None:
                    setattr(value, "ticket17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FlightSystem_Plane:

    def __init__(self, row: int, seatPerRow: int, _seat: int, nbPilote: int, nbSteward: int, _crew: Employee_IEmployee_Interface, _millesFlyed: int, _flySinceRefuel: int, _state: PlaneState, _location: Company_Airport, _millesSinceRevisionned: int, flight0: set["FlightSystem_Flight"] = None, company3: "Company_Company" = None, consomationStock22: "ProviderSystem_ConsomationStock" = None):
        self.row = row
        self.seatPerRow = seatPerRow
        self._seat = _seat
        self.nbPilote = nbPilote
        self.nbSteward = nbSteward
        self._crew = _crew
        self._millesFlyed = _millesFlyed
        self._flySinceRefuel = _flySinceRefuel
        self._state = _state
        self._location = _location
        self._millesSinceRevisionned = _millesSinceRevisionned
        self.flight0 = flight0 if flight0 is not None else set()
        self.company3 = company3
        self.consomationStock22 = consomationStock22
        
        pass
    @property
    def _flySinceRefuel(self):
        return self.___flySinceRefuel
    @_flySinceRefuel.setter
    def _flySinceRefuel(self, _flySinceRefuel: int):
        self.___flySinceRefuel = _flySinceRefuel

    @property
    def _location(self):
        return self.___location
    @_location.setter
    def _location(self, _location: Company_Airport):
        self.___location = _location

    @property
    def _seat(self):
        return self.___seat
    @_seat.setter
    def _seat(self, _seat: int):
        self.___seat = _seat

    @property
    def nbSteward(self):
        return self.__nbSteward
    @nbSteward.setter
    def nbSteward(self, nbSteward: int):
        self.__nbSteward = nbSteward

    @property
    def nbPilote(self):
        return self.__nbPilote
    @nbPilote.setter
    def nbPilote(self, nbPilote: int):
        self.__nbPilote = nbPilote

    @property
    def _millesSinceRevisionned(self):
        return self.___millesSinceRevisionned
    @_millesSinceRevisionned.setter
    def _millesSinceRevisionned(self, _millesSinceRevisionned: int):
        self.___millesSinceRevisionned = _millesSinceRevisionned

    @property
    def seatPerRow(self):
        return self.__seatPerRow
    @seatPerRow.setter
    def seatPerRow(self, seatPerRow: int):
        self.__seatPerRow = seatPerRow

    @property
    def _millesFlyed(self):
        return self.___millesFlyed
    @_millesFlyed.setter
    def _millesFlyed(self, _millesFlyed: int):
        self.___millesFlyed = _millesFlyed

    @property
    def _state(self):
        return self.___state
    @_state.setter
    def _state(self, _state: PlaneState):
        self.___state = _state

    @property
    def row(self):
        return self.__row
    @row.setter
    def row(self, row: int):
        self.__row = row

    @property
    def _crew(self):
        return self.___crew
    @_crew.setter
    def _crew(self, _crew: Employee_IEmployee_Interface):
        self.___crew = _crew

    @property
    def flight0(self):
        return self.__flight0
    @flight0.setter
    def flight0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Plane__flight0", None)
        self.__flight0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plane1"):
                    opp_val = getattr(item, "plane1", None)
                    
                    if opp_val == self:
                        setattr(item, "plane1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plane1"):
                    opp_val = getattr(item, "plane1", None)
                    
                    setattr(item, "plane1", self)
                    

    @property
    def company3(self):
        return self.__company3
    @company3.setter
    def company3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Plane__company3", None)
        self.__company3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plane2"):
                opp_val = getattr(old_value, "plane2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plane2"):
                opp_val = getattr(value, "plane2", None)
                if opp_val is None:
                    setattr(value, "plane2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consomationStock22(self):
        return self.__consomationStock22
    @consomationStock22.setter
    def consomationStock22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Plane__consomationStock22", None)
        self.__consomationStock22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plane23"):
                opp_val = getattr(old_value, "plane23", None)
                if opp_val == self:
                    setattr(old_value, "plane23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plane23"):
                opp_val = getattr(value, "plane23", None)
                setattr(value, "plane23", self)



class FlightSystem_Flight:

    def __init__(self, airportFrom: Company_Airport, airportTo: Company_Airport, _duration: int, flightType: FlightType, schedule: date, _miles: int, plane1: "FlightSystem_Plane" = None, company7: "Company_Company" = None, ticket17: set["DistributionSystem_Ticket"] = None):
        self.airportFrom = airportFrom
        self.airportTo = airportTo
        self._duration = _duration
        self.flightType = flightType
        self.schedule = schedule
        self._miles = _miles
        self.plane1 = plane1
        self.company7 = company7
        self.ticket17 = ticket17 if ticket17 is not None else set()
        
        pass
    @property
    def schedule(self):
        return self.__schedule
    @schedule.setter
    def schedule(self, schedule: date):
        self.__schedule = schedule

    @property
    def airportFrom(self):
        return self.__airportFrom
    @airportFrom.setter
    def airportFrom(self, airportFrom: Company_Airport):
        self.__airportFrom = airportFrom

    @property
    def flightType(self):
        return self.__flightType
    @flightType.setter
    def flightType(self, flightType: FlightType):
        self.__flightType = flightType

    @property
    def _miles(self):
        return self.___miles
    @_miles.setter
    def _miles(self, _miles: int):
        self.___miles = _miles

    @property
    def airportTo(self):
        return self.__airportTo
    @airportTo.setter
    def airportTo(self, airportTo: Company_Airport):
        self.__airportTo = airportTo

    @property
    def _duration(self):
        return self.___duration
    @_duration.setter
    def _duration(self, _duration: int):
        self.___duration = _duration

    @property
    def plane1(self):
        return self.__plane1
    @plane1.setter
    def plane1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Flight__plane1", None)
        self.__plane1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight0"):
                opp_val = getattr(old_value, "flight0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight0"):
                opp_val = getattr(value, "flight0", None)
                if opp_val is None:
                    setattr(value, "flight0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ticket17(self):
        return self.__ticket17
    @ticket17.setter
    def ticket17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Flight__ticket17", None)
        self.__ticket17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight16"):
                    opp_val = getattr(item, "flight16", None)
                    
                    if opp_val == self:
                        setattr(item, "flight16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight16"):
                    opp_val = getattr(item, "flight16", None)
                    
                    setattr(item, "flight16", self)
                    

    @property
    def company7(self):
        return self.__company7
    @company7.setter
    def company7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlightSystem_Flight__company7", None)
        self.__company7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight6"):
                opp_val = getattr(old_value, "flight6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight6"):
                opp_val = getattr(value, "flight6", None)
                if opp_val is None:
                    setattr(value, "flight6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Company_Airport:

    def __init__(self, city: str, ticketPrice: int, ticketCharges: int, beginSchedule: int, endSchedule: int, company14: "Company_Company" = None, provider20: set["ProviderSystem_Provider"] = None):
        self.city = city
        self.ticketPrice = ticketPrice
        self.ticketCharges = ticketCharges
        self.beginSchedule = beginSchedule
        self.endSchedule = endSchedule
        self.company14 = company14
        self.provider20 = provider20 if provider20 is not None else set()
        
        pass
    @property
    def endSchedule(self):
        return self.__endSchedule
    @endSchedule.setter
    def endSchedule(self, endSchedule: int):
        self.__endSchedule = endSchedule

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def ticketPrice(self):
        return self.__ticketPrice
    @ticketPrice.setter
    def ticketPrice(self, ticketPrice: int):
        self.__ticketPrice = ticketPrice

    @property
    def beginSchedule(self):
        return self.__beginSchedule
    @beginSchedule.setter
    def beginSchedule(self, beginSchedule: int):
        self.__beginSchedule = beginSchedule

    @property
    def ticketCharges(self):
        return self.__ticketCharges
    @ticketCharges.setter
    def ticketCharges(self, ticketCharges: int):
        self.__ticketCharges = ticketCharges

    @property
    def provider20(self):
        return self.__provider20
    @provider20.setter
    def provider20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Airport__provider20", None)
        self.__provider20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "airport21"):
                    opp_val = getattr(item, "airport21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "airport21"):
                    opp_val = getattr(item, "airport21", None)
                    
                    if opp_val is None:
                        setattr(item, "airport21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def company14(self):
        return self.__company14
    @company14.setter
    def company14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Airport__company14", None)
        self.__company14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "airport15"):
                opp_val = getattr(old_value, "airport15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "airport15"):
                opp_val = getattr(value, "airport15", None)
                if opp_val is None:
                    setattr(value, "airport15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Company_Company:

    def __init__(self, name: str, stewards: Employee_Steward, pilots: Employee_Pilot, airportEmployees: Employee_AirportEmployee, plane2: set["FlightSystem_Plane"] = None, IEmployee4: set["Employee_IEmployee_Interface"] = None, flight6: set["FlightSystem_Flight"] = None, airport15: set["Company_Airport"] = None, ticketDistributor18: set["DistributionSystem_TicketDistributor"] = None):
        self.name = name
        self.stewards = stewards
        self.pilots = pilots
        self.airportEmployees = airportEmployees
        self.plane2 = plane2 if plane2 is not None else set()
        self.IEmployee4 = IEmployee4 if IEmployee4 is not None else set()
        self.flight6 = flight6 if flight6 is not None else set()
        self.airport15 = airport15 if airport15 is not None else set()
        self.ticketDistributor18 = ticketDistributor18 if ticketDistributor18 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pilots(self):
        return self.__pilots
    @pilots.setter
    def pilots(self, pilots: Employee_Pilot):
        self.__pilots = pilots

    @property
    def stewards(self):
        return self.__stewards
    @stewards.setter
    def stewards(self, stewards: Employee_Steward):
        self.__stewards = stewards

    @property
    def airportEmployees(self):
        return self.__airportEmployees
    @airportEmployees.setter
    def airportEmployees(self, airportEmployees: Employee_AirportEmployee):
        self.__airportEmployees = airportEmployees

    @property
    def airport15(self):
        return self.__airport15
    @airport15.setter
    def airport15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Company__airport15", None)
        self.__airport15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company14"):
                    opp_val = getattr(item, "company14", None)
                    
                    if opp_val == self:
                        setattr(item, "company14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company14"):
                    opp_val = getattr(item, "company14", None)
                    
                    setattr(item, "company14", self)
                    

    @property
    def IEmployee4(self):
        return self.__IEmployee4
    @IEmployee4.setter
    def IEmployee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Company__IEmployee4", None)
        self.__IEmployee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company5"):
                    opp_val = getattr(item, "company5", None)
                    
                    if opp_val == self:
                        setattr(item, "company5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company5"):
                    opp_val = getattr(item, "company5", None)
                    
                    setattr(item, "company5", self)
                    

    @property
    def plane2(self):
        return self.__plane2
    @plane2.setter
    def plane2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Company__plane2", None)
        self.__plane2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company3"):
                    opp_val = getattr(item, "company3", None)
                    
                    if opp_val == self:
                        setattr(item, "company3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company3"):
                    opp_val = getattr(item, "company3", None)
                    
                    setattr(item, "company3", self)
                    

    @property
    def flight6(self):
        return self.__flight6
    @flight6.setter
    def flight6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Company__flight6", None)
        self.__flight6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company7"):
                    opp_val = getattr(item, "company7", None)
                    
                    if opp_val == self:
                        setattr(item, "company7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company7"):
                    opp_val = getattr(item, "company7", None)
                    
                    setattr(item, "company7", self)
                    

    @property
    def ticketDistributor18(self):
        return self.__ticketDistributor18
    @ticketDistributor18.setter
    def ticketDistributor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Company__ticketDistributor18", None)
        self.__ticketDistributor18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company19"):
                    opp_val = getattr(item, "company19", None)
                    
                    if opp_val == self:
                        setattr(item, "company19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company19"):
                    opp_val = getattr(item, "company19", None)
                    
                    setattr(item, "company19", self)
                    



class Employee_Employee:

    def __init__(self, dayByWeek: int, name: str, gender: GenderType, JobType: EmployeeType, isSuperUser: bool):
        self.dayByWeek = dayByWeek
        self.name = name
        self.gender = gender
        self.JobType = JobType
        self.isSuperUser = isSuperUser
        
        pass
    @property
    def isSuperUser(self):
        return self.__isSuperUser
    @isSuperUser.setter
    def isSuperUser(self, isSuperUser: bool):
        self.__isSuperUser = isSuperUser

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: GenderType):
        self.__gender = gender

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JobType(self):
        return self.__JobType
    @JobType.setter
    def JobType(self, JobType: EmployeeType):
        self.__JobType = JobType

    @property
    def dayByWeek(self):
        return self.__dayByWeek
    @dayByWeek.setter
    def dayByWeek(self, dayByWeek: int):
        self.__dayByWeek = dayByWeek



class Employee_AirportEmployee:

    def __init__(self, airport: Company_Airport):
        self.airport = airport
        
        pass
    @property
    def airport(self):
        return self.__airport
    @airport.setter
    def airport(self, airport: Company_Airport):
        self.__airport = airport



class Employee_Pilot:

    def __init__(self, plane: FlightSystem_Plane, airport: Company_Airport):
        self.plane = plane
        self.airport = airport
        
        pass
    @property
    def plane(self):
        return self.__plane
    @plane.setter
    def plane(self, plane: FlightSystem_Plane):
        self.__plane = plane

    @property
    def airport(self):
        return self.__airport
    @airport.setter
    def airport(self, airport: Company_Airport):
        self.__airport = airport



class Employee_Steward:

    def __init__(self, plane: FlightSystem_Plane, airport: Company_Airport):
        self.plane = plane
        self.airport = airport
        
        pass
    @property
    def plane(self):
        return self.__plane
    @plane.setter
    def plane(self, plane: FlightSystem_Plane):
        self.__plane = plane

    @property
    def airport(self):
        return self.__airport
    @airport.setter
    def airport(self, airport: Company_Airport):
        self.__airport = airport



class Employee_IEmployee_Interface:

    pass


class Controller_FlightEvent:

    def __init__(self, _dateBegin: date, _dateEnd: date, _title: str, flight: FlightSystem_Flight):
        self._dateBegin = _dateBegin
        self._dateEnd = _dateEnd
        self._title = _title
        self.flight = flight
        
        pass
    @property
    def _dateEnd(self):
        return self.___dateEnd
    @_dateEnd.setter
    def _dateEnd(self, _dateEnd: date):
        self.___dateEnd = _dateEnd

    @property
    def _dateBegin(self):
        return self.___dateBegin
    @_dateBegin.setter
    def _dateBegin(self, _dateBegin: date):
        self.___dateBegin = _dateBegin

    @property
    def _title(self):
        return self.___title
    @_title.setter
    def _title(self, _title: str):
        self.___title = _title

    @property
    def flight(self):
        return self.__flight
    @flight.setter
    def flight(self, flight: FlightSystem_Flight):
        self.__flight = flight

