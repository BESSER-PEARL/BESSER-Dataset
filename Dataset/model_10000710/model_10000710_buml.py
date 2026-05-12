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
GenderType: Enumeration = Enumeration(
    name="GenderType",
    literals={
            
    }
)

EmployeeType: Enumeration = Enumeration(
    name="EmployeeType",
    literals={
            
    }
)

ReportType: Enumeration = Enumeration(
    name="ReportType",
    literals={
            
    }
)

ProviderType: Enumeration = Enumeration(
    name="ProviderType",
    literals={
            
    }
)

TicketBuyType: Enumeration = Enumeration(
    name="TicketBuyType",
    literals={
            
    }
)

TicketPayment: Enumeration = Enumeration(
    name="TicketPayment",
    literals={
            
    }
)

FlightType: Enumeration = Enumeration(
    name="FlightType",
    literals={
            
    }
)

PlaneState: Enumeration = Enumeration(
    name="PlaneState",
    literals={
            
    }
)

# Classes
Controller_FlightEvent = Class(name="Controller_FlightEvent")
Employee_IEmployee_Interface = Class(name="Employee_IEmployee_Interface")
Employee_Steward = Class(name="Employee_Steward")
Employee_Pilot = Class(name="Employee_Pilot")
Employee_AirportEmployee = Class(name="Employee_AirportEmployee")
Employee_Employee = Class(name="Employee_Employee")
Company_Company = Class(name="Company_Company")
Company_Airport = Class(name="Company_Airport")
FlightSystem_Flight = Class(name="FlightSystem_Flight")
FlightSystem_Plane = Class(name="FlightSystem_Plane")
DistributionSystem_Ticket = Class(name="DistributionSystem_Ticket")
DistributionSystem_BoardingPass = Class(name="DistributionSystem_BoardingPass")
DistributionSystem_Customer = Class(name="DistributionSystem_Customer")
DistributionSystem_TicketDistributor = Class(name="DistributionSystem_TicketDistributor")
User_Actor = Class(name="User_Actor")
Admin_Actor = Class(name="Admin_Actor")
Admin_Actor1 = Class(name="Admin_Actor1")
UI_EmployeeManager_Component = Class(name="UI_EmployeeManager_Component")
UI_EmployeePlanning_Component = Class(name="UI_EmployeePlanning_Component")
Employee_Actor = Class(name="Employee_Actor")
UI_FlightManager_Component = Class(name="UI_FlightManager_Component")
UI_FlightPlanning_Component = Class(name="UI_FlightPlanning_Component")
User_Actor1 = Class(name="User_Actor1")
Customer_Actor = Class(name="Customer_Actor")
OnlineBuy_UseCase = Class(name="OnlineBuy_UseCase")
Seller_Actor = Class(name="Seller_Actor")
Distribute_UseCase = Class(name="Distribute_UseCase")
Employee_Actor1 = Class(name="Employee_Actor1")
PassengerCheckIn_UseCase = Class(name="PassengerCheckIn_UseCase")
PassengerIdentification_UseCase = Class(name="PassengerIdentification_UseCase")
ByName_UseCase = Class(name="ByName_UseCase")
ByBookingNumber_UseCase = Class(name="ByBookingNumber_UseCase")
CheckInForFlight_UseCase = Class(name="CheckInForFlight_UseCase")
CheckInformations_UseCase = Class(name="CheckInformations_UseCase")
CheckSeat_UseCase = Class(name="CheckSeat_UseCase")
ChangeSeat_UseCase = Class(name="ChangeSeat_UseCase")
WaitingList_UseCase = Class(name="WaitingList_UseCase")
AddASurbooking_UseCase = Class(name="AddASurbooking_UseCase")
CheckAvailability_UseCase = Class(name="CheckAvailability_UseCase")
RegisterToWaitingList_UseCase = Class(name="RegisterToWaitingList_UseCase")
CloseCheckIn_UseCase = Class(name="CloseCheckIn_UseCase")
ProcessWaitingList_UseCase = Class(name="ProcessWaitingList_UseCase")
LuggageCheckIn_UseCase = Class(name="LuggageCheckIn_UseCase")
AddABagage_UseCase = Class(name="AddABagage_UseCase")
PrintLuggageBadge_UseCase = Class(name="PrintLuggageBadge_UseCase")
StartBoarding_UseCase = Class(name="StartBoarding_UseCase")
Customer_Actor1 = Class(name="Customer_Actor1")
BuyConsomation_UseCase = Class(name="BuyConsomation_UseCase")
CheckConsomationCatalogue_UseCase = Class(name="CheckConsomationCatalogue_UseCase")
Steward_Actor = Class(name="Steward_Actor")
SellConsomation_UseCase = Class(name="SellConsomation_UseCase")
CheckConsomationStock_UseCase = Class(name="CheckConsomationStock_UseCase")
Plane_Actor = Class(name="Plane_Actor")
Intervention_UseCase = Class(name="Intervention_UseCase")
Revision_UseCase = Class(name="Revision_UseCase")
Refuel_UseCase = Class(name="Refuel_UseCase")
Immobilisation_UseCase = Class(name="Immobilisation_UseCase")
CleaningService_UseCase = Class(name="CleaningService_UseCase")
AirportAdministration_Actor = Class(name="AirportAdministration_Actor")
FillConsomationStock_UseCase = Class(name="FillConsomationStock_UseCase")
ChooseProvider_UseCase = Class(name="ChooseProvider_UseCase")
Fuel_UseCase = Class(name="Fuel_UseCase")
Service_UseCase = Class(name="Service_UseCase")
Reparation_UseCase = Class(name="Reparation_UseCase")
Consomation_UseCase = Class(name="Consomation_UseCase")
AirportAdministration_Actor1 = Class(name="AirportAdministration_Actor1")
Company_Actor = Class(name="Company_Actor")
Company_Actor1 = Class(name="Company_Actor1")
Promotion_UseCase = Class(name="Promotion_UseCase")
Marketting_Component = Class(name="Marketting_Component")
Taxes_Component = Class(name="Taxes_Component")
AirportAdministration_Actor2 = Class(name="AirportAdministration_Actor2")
GenerateReport_UseCase = Class(name="GenerateReport_UseCase")
CheckReportInFolder_UseCase = Class(name="CheckReportInFolder_UseCase")
Resources_UseCase = Class(name="Resources_UseCase")
Flights_UseCase = Class(name="Flights_UseCase")
Charges_UseCase = Class(name="Charges_UseCase")
Customers_UseCase = Class(name="Customers_UseCase")
TicketsPrice_UseCase = Class(name="TicketsPrice_UseCase")
TicketsAveragePrice_UseCase = Class(name="TicketsAveragePrice_UseCase")
Surbooking_UseCase = Class(name="Surbooking_UseCase")
Customer_Actor2 = Class(name="Customer_Actor2")
Distribute_UseCase1 = Class(name="Distribute_UseCase1")
CheckEligibility__FreeMiles__UseCase = Class(name="CheckEligibility__FreeMiles__UseCase")
AsksForFreeFlight_UseCase = Class(name="AsksForFreeFlight_UseCase")
Employee_Actor2 = Class(name="Employee_Actor2")
Luggage_Checkin_UseCase = Class(name="Luggage_Checkin_UseCase")
Consult_Luggage_Ticket_Infos_UseCase = Class(name="Consult_Luggage_Ticket_Infos_UseCase")
Add_A_Luggage_UseCase = Class(name="Add_A_Luggage_UseCase")
Print_Luggage_Ticket_UseCase = Class(name="Print_Luggage_Ticket_UseCase")
Send_Luggage_To_Loading_UseCase = Class(name="Send_Luggage_To_Loading_UseCase")
ProviderSystem_Fuel = Class(name="ProviderSystem_Fuel")
ProviderSystem_Consomation = Class(name="ProviderSystem_Consomation")
ProviderSystem_Provider = Class(name="ProviderSystem_Provider")
ProviderSystem_ConsomationStock = Class(name="ProviderSystem_ConsomationStock")
CreateFlight_external = Class(name="CreateFlight_external")
EditFlight_external = Class(name="EditFlight_external")
CancelFlight_external = Class(name="CancelFlight_external")
CheckPlanning_external = Class(name="CheckPlanning_external")
AddEmployee_external = Class(name="AddEmployee_external")
EditEmployee_external = Class(name="EditEmployee_external")
DeleteEmployee_external = Class(name="DeleteEmployee_external")
PlanningCheck_external = Class(name="PlanningCheck_external")
SearchEmployee_external = Class(name="SearchEmployee_external")
SetDestinationPrice_external = Class(name="SetDestinationPrice_external")
SetTaxes_external = Class(name="SetTaxes_external")
Promotion_System_external = Class(name="Promotion_System_external")
Advertising_external = Class(name="Advertising_external")
EditPlanning_external = Class(name="EditPlanning_external")

# Controller_FlightEvent class attributes and methods
Controller_FlightEvent__dateBegin: Property = Property(name="_dateBegin", type=DateType)
Controller_FlightEvent__dateEnd: Property = Property(name="_dateEnd", type=DateType)
Controller_FlightEvent__title: Property = Property(name="_title", type=StringType)
Controller_FlightEvent_flight: Property = Property(name="flight", type=FlightSystem_Flight)
Controller_FlightEvent.attributes={Controller_FlightEvent__title, Controller_FlightEvent__dateBegin, Controller_FlightEvent__dateEnd, Controller_FlightEvent_flight}

# Employee_IEmployee_Interface class attributes and methods

# Employee_Steward class attributes and methods
Employee_Steward_plane: Property = Property(name="plane", type=FlightSystem_Plane)
Employee_Steward_airport: Property = Property(name="airport", type=Company_Airport)
Employee_Steward.attributes={Employee_Steward_plane, Employee_Steward_airport}

# Employee_Pilot class attributes and methods
Employee_Pilot_plane: Property = Property(name="plane", type=FlightSystem_Plane)
Employee_Pilot_airport: Property = Property(name="airport", type=Company_Airport)
Employee_Pilot.attributes={Employee_Pilot_plane, Employee_Pilot_airport}

# Employee_AirportEmployee class attributes and methods
Employee_AirportEmployee_airport: Property = Property(name="airport", type=Company_Airport)
Employee_AirportEmployee.attributes={Employee_AirportEmployee_airport}

# Employee_Employee class attributes and methods
Employee_Employee_dayByWeek: Property = Property(name="dayByWeek", type=IntegerType)
Employee_Employee_name: Property = Property(name="name", type=StringType)
Employee_Employee_gender: Property = Property(name="gender", type=GenderType)
Employee_Employee_JobType: Property = Property(name="JobType", type=EmployeeType)
Employee_Employee_isSuperUser: Property = Property(name="isSuperUser", type=BooleanType)
Employee_Employee.attributes={Employee_Employee_gender, Employee_Employee_JobType, Employee_Employee_dayByWeek, Employee_Employee_name, Employee_Employee_isSuperUser}

# Company_Company class attributes and methods
Company_Company_name: Property = Property(name="name", type=StringType)
Company_Company_stewards: Property = Property(name="stewards", type=Employee_Steward)
Company_Company_pilots: Property = Property(name="pilots", type=Employee_Pilot)
Company_Company_airportEmployees: Property = Property(name="airportEmployees", type=Employee_AirportEmployee)
Company_Company.attributes={Company_Company_stewards, Company_Company_airportEmployees, Company_Company_pilots, Company_Company_name}

# Company_Airport class attributes and methods
Company_Airport_city: Property = Property(name="city", type=StringType)
Company_Airport_ticketPrice: Property = Property(name="ticketPrice", type=IntegerType)
Company_Airport_ticketCharges: Property = Property(name="ticketCharges", type=IntegerType)
Company_Airport_beginSchedule: Property = Property(name="beginSchedule", type=IntegerType)
Company_Airport_endSchedule: Property = Property(name="endSchedule", type=IntegerType)
Company_Airport.attributes={Company_Airport_endSchedule, Company_Airport_beginSchedule, Company_Airport_ticketCharges, Company_Airport_ticketPrice, Company_Airport_city}

# FlightSystem_Flight class attributes and methods
FlightSystem_Flight_airportFrom: Property = Property(name="airportFrom", type=Company_Airport)
FlightSystem_Flight_airportTo: Property = Property(name="airportTo", type=Company_Airport)
FlightSystem_Flight__duration: Property = Property(name="_duration", type=IntegerType)
FlightSystem_Flight_flightType: Property = Property(name="flightType", type=FlightType)
FlightSystem_Flight_schedule: Property = Property(name="schedule", type=DateType)
FlightSystem_Flight__miles: Property = Property(name="_miles", type=IntegerType)
FlightSystem_Flight.attributes={FlightSystem_Flight__miles, FlightSystem_Flight_airportTo, FlightSystem_Flight_flightType, FlightSystem_Flight_airportFrom, FlightSystem_Flight_schedule, FlightSystem_Flight__duration}

# FlightSystem_Plane class attributes and methods
FlightSystem_Plane_row: Property = Property(name="row", type=IntegerType)
FlightSystem_Plane_seatPerRow: Property = Property(name="seatPerRow", type=IntegerType)
FlightSystem_Plane__seat: Property = Property(name="_seat", type=IntegerType)
FlightSystem_Plane_nbPilote: Property = Property(name="nbPilote", type=IntegerType)
FlightSystem_Plane_nbSteward: Property = Property(name="nbSteward", type=IntegerType)
FlightSystem_Plane__crew: Property = Property(name="_crew", type=Employee_IEmployee_Interface)
FlightSystem_Plane__millesFlyed: Property = Property(name="_millesFlyed", type=IntegerType)
FlightSystem_Plane__flySinceRefuel: Property = Property(name="_flySinceRefuel", type=IntegerType)
FlightSystem_Plane__state: Property = Property(name="_state", type=PlaneState)
FlightSystem_Plane__location: Property = Property(name="_location", type=Company_Airport)
FlightSystem_Plane__millesSinceRevisionned: Property = Property(name="_millesSinceRevisionned", type=IntegerType)
FlightSystem_Plane.attributes={FlightSystem_Plane__millesSinceRevisionned, FlightSystem_Plane_nbSteward, FlightSystem_Plane_row, FlightSystem_Plane__seat, FlightSystem_Plane_nbPilote, FlightSystem_Plane_seatPerRow, FlightSystem_Plane__crew, FlightSystem_Plane__millesFlyed, FlightSystem_Plane__state, FlightSystem_Plane__flySinceRefuel, FlightSystem_Plane__location}

# DistributionSystem_Ticket class attributes and methods
DistributionSystem_Ticket_from: Property = Property(name="from", type=TicketBuyType)
DistributionSystem_Ticket_payment: Property = Property(name="payment", type=TicketPayment)
DistributionSystem_Ticket__price: Property = Property(name="_price", type=IntegerType)
DistributionSystem_Ticket_isRegistered: Property = Property(name="isRegistered", type=BooleanType)
DistributionSystem_Ticket__numberPlace: Property = Property(name="_numberPlace", type=IntegerType)
DistributionSystem_Ticket.attributes={DistributionSystem_Ticket_isRegistered, DistributionSystem_Ticket_payment, DistributionSystem_Ticket__price, DistributionSystem_Ticket__numberPlace, DistributionSystem_Ticket_from}

# DistributionSystem_BoardingPass class attributes and methods
DistributionSystem_BoardingPass_price: Property = Property(name="price", type=IntegerType)
DistributionSystem_BoardingPass_row: Property = Property(name="row", type=IntegerType)
DistributionSystem_BoardingPass_seat: Property = Property(name="seat", type=IntegerType)
DistributionSystem_BoardingPass_isValidated: Property = Property(name="isValidated", type=BooleanType)
DistributionSystem_BoardingPass_dateOfPurchase: Property = Property(name="dateOfPurchase", type=DateType)
DistributionSystem_BoardingPass_flight: Property = Property(name="flight", type=StringType)
DistributionSystem_BoardingPass.attributes={DistributionSystem_BoardingPass_row, DistributionSystem_BoardingPass_isValidated, DistributionSystem_BoardingPass_price, DistributionSystem_BoardingPass_seat, DistributionSystem_BoardingPass_flight, DistributionSystem_BoardingPass_dateOfPurchase}

# DistributionSystem_Customer class attributes and methods
DistributionSystem_Customer__milesFlyed: Property = Property(name="_milesFlyed", type=IntegerType)
DistributionSystem_Customer_Luggage: Property = Property(name="Luggage", type=StringType)
DistributionSystem_Customer_name: Property = Property(name="name", type=StringType)
DistributionSystem_Customer.attributes={DistributionSystem_Customer_Luggage, DistributionSystem_Customer__milesFlyed, DistributionSystem_Customer_name}

# DistributionSystem_TicketDistributor class attributes and methods
DistributionSystem_TicketDistributor_from: Property = Property(name="from", type=TicketBuyType)
DistributionSystem_TicketDistributor_payment: Property = Property(name="payment", type=TicketPayment)
DistributionSystem_TicketDistributor.attributes={DistributionSystem_TicketDistributor_payment, DistributionSystem_TicketDistributor_from}

# User_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Admin_Actor1 class attributes and methods

# UI_EmployeeManager_Component class attributes and methods

# UI_EmployeePlanning_Component class attributes and methods

# Employee_Actor class attributes and methods

# UI_FlightManager_Component class attributes and methods

# UI_FlightPlanning_Component class attributes and methods

# User_Actor1 class attributes and methods

# Customer_Actor class attributes and methods

# OnlineBuy_UseCase class attributes and methods

# Seller_Actor class attributes and methods

# Distribute_UseCase class attributes and methods

# Employee_Actor1 class attributes and methods

# PassengerCheckIn_UseCase class attributes and methods

# PassengerIdentification_UseCase class attributes and methods

# ByName_UseCase class attributes and methods

# ByBookingNumber_UseCase class attributes and methods

# CheckInForFlight_UseCase class attributes and methods

# CheckInformations_UseCase class attributes and methods

# CheckSeat_UseCase class attributes and methods

# ChangeSeat_UseCase class attributes and methods

# WaitingList_UseCase class attributes and methods

# AddASurbooking_UseCase class attributes and methods

# CheckAvailability_UseCase class attributes and methods

# RegisterToWaitingList_UseCase class attributes and methods

# CloseCheckIn_UseCase class attributes and methods

# ProcessWaitingList_UseCase class attributes and methods

# LuggageCheckIn_UseCase class attributes and methods

# AddABagage_UseCase class attributes and methods

# PrintLuggageBadge_UseCase class attributes and methods

# StartBoarding_UseCase class attributes and methods

# Customer_Actor1 class attributes and methods

# BuyConsomation_UseCase class attributes and methods

# CheckConsomationCatalogue_UseCase class attributes and methods

# Steward_Actor class attributes and methods

# SellConsomation_UseCase class attributes and methods

# CheckConsomationStock_UseCase class attributes and methods

# Plane_Actor class attributes and methods

# Intervention_UseCase class attributes and methods

# Revision_UseCase class attributes and methods

# Refuel_UseCase class attributes and methods

# Immobilisation_UseCase class attributes and methods

# CleaningService_UseCase class attributes and methods

# AirportAdministration_Actor class attributes and methods

# FillConsomationStock_UseCase class attributes and methods

# ChooseProvider_UseCase class attributes and methods

# Fuel_UseCase class attributes and methods

# Service_UseCase class attributes and methods

# Reparation_UseCase class attributes and methods

# Consomation_UseCase class attributes and methods

# AirportAdministration_Actor1 class attributes and methods

# Company_Actor class attributes and methods

# Company_Actor1 class attributes and methods

# Promotion_UseCase class attributes and methods

# Marketting_Component class attributes and methods

# Taxes_Component class attributes and methods

# AirportAdministration_Actor2 class attributes and methods

# GenerateReport_UseCase class attributes and methods

# CheckReportInFolder_UseCase class attributes and methods

# Resources_UseCase class attributes and methods

# Flights_UseCase class attributes and methods

# Charges_UseCase class attributes and methods

# Customers_UseCase class attributes and methods

# TicketsPrice_UseCase class attributes and methods

# TicketsAveragePrice_UseCase class attributes and methods

# Surbooking_UseCase class attributes and methods

# Customer_Actor2 class attributes and methods

# Distribute_UseCase1 class attributes and methods

# CheckEligibility__FreeMiles__UseCase class attributes and methods

# AsksForFreeFlight_UseCase class attributes and methods

# Employee_Actor2 class attributes and methods

# Luggage_Checkin_UseCase class attributes and methods

# Consult_Luggage_Ticket_Infos_UseCase class attributes and methods

# Add_A_Luggage_UseCase class attributes and methods

# Print_Luggage_Ticket_UseCase class attributes and methods

# Send_Luggage_To_Loading_UseCase class attributes and methods

# ProviderSystem_Fuel class attributes and methods
ProviderSystem_Fuel_date: Property = Property(name="date", type=DateType)
ProviderSystem_Fuel__price: Property = Property(name="_price", type=IntegerType)
ProviderSystem_Fuel_volme: Property = Property(name="volme", type=IntegerType)
ProviderSystem_Fuel_plane: Property = Property(name="plane", type=FlightSystem_Plane)
ProviderSystem_Fuel.attributes={ProviderSystem_Fuel_volme, ProviderSystem_Fuel_plane, ProviderSystem_Fuel__price, ProviderSystem_Fuel_date}

# ProviderSystem_Consomation class attributes and methods
ProviderSystem_Consomation_name: Property = Property(name="name", type=StringType)
ProviderSystem_Consomation_pricePerUnit: Property = Property(name="pricePerUnit", type=IntegerType)
ProviderSystem_Consomation.attributes={ProviderSystem_Consomation_pricePerUnit, ProviderSystem_Consomation_name}

# ProviderSystem_Provider class attributes and methods
ProviderSystem_Provider_pricePerUnit: Property = Property(name="pricePerUnit", type=IntegerType)
ProviderSystem_Provider_name: Property = Property(name="name", type=StringType)
ProviderSystem_Provider.attributes={ProviderSystem_Provider_name, ProviderSystem_Provider_pricePerUnit}

# ProviderSystem_ConsomationStock class attributes and methods
ProviderSystem_ConsomationStock__capacity: Property = Property(name="_capacity", type=IntegerType)
ProviderSystem_ConsomationStock.attributes={ProviderSystem_ConsomationStock__capacity}

# CreateFlight_external class attributes and methods

# EditFlight_external class attributes and methods

# CancelFlight_external class attributes and methods

# CheckPlanning_external class attributes and methods

# AddEmployee_external class attributes and methods

# EditEmployee_external class attributes and methods

# DeleteEmployee_external class attributes and methods

# PlanningCheck_external class attributes and methods

# SearchEmployee_external class attributes and methods

# SetDestinationPrice_external class attributes and methods

# SetTaxes_external class attributes and methods

# Promotion_System_external class attributes and methods

# Advertising_external class attributes and methods

# EditPlanning_external class attributes and methods

# Relationships
Plane_Fly: BinaryAssociation = BinaryAssociation(
    name="Plane_Fly",
    ends={
        Property(name="flight0", type=FlightSystem_Flight, multiplicity=Multiplicity(0, 9999)),
        Property(name="plane1", type=FlightSystem_Plane, multiplicity=Multiplicity(1, 1))
    }
)
Company_Plane: BinaryAssociation = BinaryAssociation(
    name="Company_Plane",
    ends={
        Property(name="plane2", type=FlightSystem_Plane, multiplicity=Multiplicity(1, 9999)),
        Property(name="company3", type=Company_Company, multiplicity=Multiplicity(1, 1))
    }
)
Company_IPersonnel: BinaryAssociation = BinaryAssociation(
    name="Company_IPersonnel",
    ends={
        Property(name="IEmployee4", type=Employee_IEmployee_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="company5", type=Company_Company, multiplicity=Multiplicity(1, 1))
    }
)
Company_Fly: BinaryAssociation = BinaryAssociation(
    name="Company_Fly",
    ends={
        Property(name="flight6", type=FlightSystem_Flight, multiplicity=Multiplicity(0, 9999)),
        Property(name="company7", type=Company_Company, multiplicity=Multiplicity(1, 1))
    }
)
Customer_BoardingPass: BinaryAssociation = BinaryAssociation(
    name="Customer_BoardingPass",
    ends={
        Property(name="boardingPass8", type=DistributionSystem_BoardingPass, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer9", type=DistributionSystem_Customer, multiplicity=Multiplicity(1, 1))
    }
)
Ticket_BoardingPass: BinaryAssociation = BinaryAssociation(
    name="Ticket_BoardingPass",
    ends={
        Property(name="boardingPass10", type=DistributionSystem_BoardingPass, multiplicity=Multiplicity(0, 9999)),
        Property(name="ticket11", type=DistributionSystem_Ticket, multiplicity=Multiplicity(1, 1))
    }
)
FuelProvider_Fuel: BinaryAssociation = BinaryAssociation(
    name="FuelProvider_Fuel",
    ends={
        Property(name="fuel12", type=ProviderSystem_Fuel, multiplicity=Multiplicity(0, 9999)),
        Property(name="fuelProvider13", type=ProviderSystem_Provider, multiplicity=Multiplicity(1, 1))
    }
)
Airport_Company: BinaryAssociation = BinaryAssociation(
    name="Airport_Company",
    ends={
        Property(name="company14", type=Company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="airport15", type=Company_Airport, multiplicity=Multiplicity(0, 9999))
    }
)
Ticket_Flight: BinaryAssociation = BinaryAssociation(
    name="Ticket_Flight",
    ends={
        Property(name="flight16", type=FlightSystem_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="ticket17", type=DistributionSystem_Ticket, multiplicity=Multiplicity(1, 9999))
    }
)
Company_TicketDistributor: BinaryAssociation = BinaryAssociation(
    name="Company_TicketDistributor",
    ends={
        Property(name="ticketDistributor18", type=DistributionSystem_TicketDistributor, multiplicity=Multiplicity(1, 9999)),
        Property(name="company19", type=Company_Company, multiplicity=Multiplicity(1, 1))
    }
)
Airport_Provider: BinaryAssociation = BinaryAssociation(
    name="Airport_Provider",
    ends={
        Property(name="provider20", type=ProviderSystem_Provider, multiplicity=Multiplicity(0, 9999)),
        Property(name="airport21", type=Company_Airport, multiplicity=Multiplicity(0, 9999))
    }
)
Plane_ConsomationStock: BinaryAssociation = BinaryAssociation(
    name="Plane_ConsomationStock",
    ends={
        Property(name="consomationStock22", type=ProviderSystem_ConsomationStock, multiplicity=Multiplicity(1, 1)),
        Property(name="plane23", type=FlightSystem_Plane, multiplicity=Multiplicity(1, 1))
    }
)
Bob_CreateFlight: BinaryAssociation = BinaryAssociation(
    name="Bob_CreateFlight",
    ends={
        Property(name="createFlight24", type=CreateFlight_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob25", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bob_EditFlight: BinaryAssociation = BinaryAssociation(
    name="Bob_EditFlight",
    ends={
        Property(name="editFlight26", type=EditFlight_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob27", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bob_CancelFlight: BinaryAssociation = BinaryAssociation(
    name="Bob_CancelFlight",
    ends={
        Property(name="cancelFlight28", type=CancelFlight_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob29", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_CheckPlanning: BinaryAssociation = BinaryAssociation(
    name="User_CheckPlanning",
    ends={
        Property(name="checkPlanning30", type=CheckPlanning_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user31", type=User_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Bob_AddEmployee: BinaryAssociation = BinaryAssociation(
    name="Bob_AddEmployee",
    ends={
        Property(name="addEmployee32", type=AddEmployee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob33", type=Admin_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Bob_EditEmployee: BinaryAssociation = BinaryAssociation(
    name="Bob_EditEmployee",
    ends={
        Property(name="editEmployee34", type=EditEmployee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob35", type=Admin_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Bob_DeleteEmployee: BinaryAssociation = BinaryAssociation(
    name="Bob_DeleteEmployee",
    ends={
        Property(name="deleteEmployee36", type=DeleteEmployee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob37", type=Admin_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
User_PlanningCheck: BinaryAssociation = BinaryAssociation(
    name="User_PlanningCheck",
    ends={
        Property(name="planningCheck38", type=PlanningCheck_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user39", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_SearchEmployee: BinaryAssociation = BinaryAssociation(
    name="User_SearchEmployee",
    ends={
        Property(name="searchEmployee40", type=SearchEmployee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user41", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Seller: BinaryAssociation = BinaryAssociation(
    name="Customer_Seller",
    ends={
        Property(name="seller42", type=Seller_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="customer43", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_OnlineBuy: BinaryAssociation = BinaryAssociation(
    name="Customer_OnlineBuy",
    ends={
        Property(name="onlineBuy44", type=OnlineBuy_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer45", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Seller_BuyThing: BinaryAssociation = BinaryAssociation(
    name="Seller_BuyThing",
    ends={
        Property(name="buyThing46", type=Distribute_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="seller47", type=Seller_Actor, multiplicity=Multiplicity(0, 1))
    }
)
OnlineBuy_BuyThing: BinaryAssociation = BinaryAssociation(
    name="OnlineBuy_BuyThing",
    ends={
        Property(name="buyThing48", type=Distribute_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineBuy49", type=OnlineBuy_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_BuyConsomation: BinaryAssociation = BinaryAssociation(
    name="Customer_BuyConsomation",
    ends={
        Property(name="buyConsomation54", type=BuyConsomation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer55", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Customer_CheckConsomationCatalogue: BinaryAssociation = BinaryAssociation(
    name="Customer_CheckConsomationCatalogue",
    ends={
        Property(name="checkConsomationCatalogue56", type=CheckConsomationCatalogue_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer57", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Steward_SellConsomation: BinaryAssociation = BinaryAssociation(
    name="Steward_SellConsomation",
    ends={
        Property(name="sellConsomation58", type=SellConsomation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="steward59", type=Steward_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Steward_CheckConsomationStock: BinaryAssociation = BinaryAssociation(
    name="Steward_CheckConsomationStock",
    ends={
        Property(name="checkConsomationStock60", type=CheckConsomationStock_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="steward61", type=Steward_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Plane_Intervention: BinaryAssociation = BinaryAssociation(
    name="Plane_Intervention",
    ends={
        Property(name="intervention62", type=Intervention_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="plane63", type=Plane_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Plane_Cleaning___services: BinaryAssociation = BinaryAssociation(
    name="Plane_Cleaning___services",
    ends={
        Property(name="cleaning___services64", type=CleaningService_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="plane65", type=Plane_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airport_ChooseProvider: BinaryAssociation = BinaryAssociation(
    name="Airport_ChooseProvider",
    ends={
        Property(name="chooseProvider66", type=ChooseProvider_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airport67", type=AirportAdministration_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airport_FillConsomationStock: BinaryAssociation = BinaryAssociation(
    name="Airport_FillConsomationStock",
    ends={
        Property(name="fillConsomationStock68", type=FillConsomationStock_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airport69", type=AirportAdministration_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Company_SetDestinationPrice: BinaryAssociation = BinaryAssociation(
    name="Company_SetDestinationPrice",
    ends={
        Property(name="setDestinationPrice70", type=SetDestinationPrice_external, multiplicity=Multiplicity(0, 1)),
        Property(name="company71", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airport_SetTaxes: BinaryAssociation = BinaryAssociation(
    name="Airport_SetTaxes",
    ends={
        Property(name="setTaxes72", type=SetTaxes_external, multiplicity=Multiplicity(0, 1)),
        Property(name="airport73", type=AirportAdministration_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Company_Promotion_System: BinaryAssociation = BinaryAssociation(
    name="Company_Promotion_System",
    ends={
        Property(name="promotion_System74", type=Promotion_System_external, multiplicity=Multiplicity(0, 1)),
        Property(name="company75", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Company_Advertising: BinaryAssociation = BinaryAssociation(
    name="Company_Advertising",
    ends={
        Property(name="advertising76", type=Advertising_external, multiplicity=Multiplicity(0, 1)),
        Property(name="company77", type=Company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airport_CheckReportInFolder: BinaryAssociation = BinaryAssociation(
    name="Airport_CheckReportInFolder",
    ends={
        Property(name="checkReportInFolder78", type=CheckReportInFolder_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airport79", type=AirportAdministration_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Airport_GenerateReport: BinaryAssociation = BinaryAssociation(
    name="Airport_GenerateReport",
    ends={
        Property(name="generateReport80", type=GenerateReport_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airport81", type=AirportAdministration_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Customer_AsksForFreeFlight: BinaryAssociation = BinaryAssociation(
    name="Customer_AsksForFreeFlight",
    ends={
        Property(name="asksForFreeFlight82", type=AsksForFreeFlight_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer83", type=Customer_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Luggage_Checkin_Employee: BinaryAssociation = BinaryAssociation(
    name="Luggage_Checkin_Employee",
    ends={
        Property(name="employee84", type=Employee_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="luggage_Checkin85", type=Luggage_Checkin_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ConsomationStock_Consomation: BinaryAssociation = BinaryAssociation(
    name="ConsomationStock_Consomation",
    ends={
        Property(name="consomation86", type=ProviderSystem_Consomation, multiplicity=Multiplicity(0, 9999)),
        Property(name="consomationStock87", type=ProviderSystem_ConsomationStock, multiplicity=Multiplicity(1, 1))
    }
)
ConsomationProvider_Consomation: BinaryAssociation = BinaryAssociation(
    name="ConsomationProvider_Consomation",
    ends={
        Property(name="consomation88", type=ProviderSystem_Consomation, multiplicity=Multiplicity(0, 9999)),
        Property(name="consomationProvider89", type=ProviderSystem_Provider, multiplicity=Multiplicity(1, 1))
    }
)
Bob_EditPlanning: BinaryAssociation = BinaryAssociation(
    name="Bob_EditPlanning",
    ends={
        Property(name="editPlanning50", type=EditPlanning_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bob51", type=Admin_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Employee_PassengerCheckIn: BinaryAssociation = BinaryAssociation(
    name="Employee_PassengerCheckIn",
    ends={
        Property(name="passengerCheckIn52", type=PassengerCheckIn_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee53", type=Employee_Actor1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_57db9265_afee_41c2_92cb_44b23b9a5c39",
    types={Controller_FlightEvent, Employee_IEmployee_Interface, Employee_Steward, Employee_Pilot, Employee_AirportEmployee, Employee_Employee, Company_Company, Company_Airport, FlightSystem_Flight, FlightSystem_Plane, DistributionSystem_Ticket, DistributionSystem_BoardingPass, DistributionSystem_Customer, DistributionSystem_TicketDistributor, User_Actor, Admin_Actor, Admin_Actor1, UI_EmployeeManager_Component, UI_EmployeePlanning_Component, Employee_Actor, UI_FlightManager_Component, UI_FlightPlanning_Component, User_Actor1, Customer_Actor, OnlineBuy_UseCase, Seller_Actor, Distribute_UseCase, Employee_Actor1, PassengerCheckIn_UseCase, PassengerIdentification_UseCase, ByName_UseCase, ByBookingNumber_UseCase, CheckInForFlight_UseCase, CheckInformations_UseCase, CheckSeat_UseCase, ChangeSeat_UseCase, WaitingList_UseCase, AddASurbooking_UseCase, CheckAvailability_UseCase, RegisterToWaitingList_UseCase, CloseCheckIn_UseCase, ProcessWaitingList_UseCase, LuggageCheckIn_UseCase, AddABagage_UseCase, PrintLuggageBadge_UseCase, StartBoarding_UseCase, Customer_Actor1, BuyConsomation_UseCase, CheckConsomationCatalogue_UseCase, Steward_Actor, SellConsomation_UseCase, CheckConsomationStock_UseCase, Plane_Actor, Intervention_UseCase, Revision_UseCase, Refuel_UseCase, Immobilisation_UseCase, CleaningService_UseCase, AirportAdministration_Actor, FillConsomationStock_UseCase, ChooseProvider_UseCase, Fuel_UseCase, Service_UseCase, Reparation_UseCase, Consomation_UseCase, AirportAdministration_Actor1, Company_Actor, Company_Actor1, Promotion_UseCase, Marketting_Component, Taxes_Component, AirportAdministration_Actor2, GenerateReport_UseCase, CheckReportInFolder_UseCase, Resources_UseCase, Flights_UseCase, Charges_UseCase, Customers_UseCase, TicketsPrice_UseCase, TicketsAveragePrice_UseCase, Surbooking_UseCase, Customer_Actor2, Distribute_UseCase1, CheckEligibility__FreeMiles__UseCase, AsksForFreeFlight_UseCase, Employee_Actor2, Luggage_Checkin_UseCase, Consult_Luggage_Ticket_Infos_UseCase, Add_A_Luggage_UseCase, Print_Luggage_Ticket_UseCase, Send_Luggage_To_Loading_UseCase, ProviderSystem_Fuel, ProviderSystem_Consomation, ProviderSystem_Provider, ProviderSystem_ConsomationStock, CreateFlight_external, EditFlight_external, CancelFlight_external, CheckPlanning_external, AddEmployee_external, EditEmployee_external, DeleteEmployee_external, PlanningCheck_external, SearchEmployee_external, SetDestinationPrice_external, SetTaxes_external, Promotion_System_external, Advertising_external, EditPlanning_external, GenderType, EmployeeType, ReportType, ProviderType, TicketBuyType, TicketPayment, FlightType, PlaneState},
    associations={Plane_Fly, Company_Plane, Company_IPersonnel, Company_Fly, Customer_BoardingPass, Ticket_BoardingPass, FuelProvider_Fuel, Airport_Company, Ticket_Flight, Company_TicketDistributor, Airport_Provider, Plane_ConsomationStock, Bob_CreateFlight, Bob_EditFlight, Bob_CancelFlight, User_CheckPlanning, Bob_AddEmployee, Bob_EditEmployee, Bob_DeleteEmployee, User_PlanningCheck, User_SearchEmployee, Customer_Seller, Customer_OnlineBuy, Seller_BuyThing, OnlineBuy_BuyThing, Customer_BuyConsomation, Customer_CheckConsomationCatalogue, Steward_SellConsomation, Steward_CheckConsomationStock, Plane_Intervention, Plane_Cleaning___services, Airport_ChooseProvider, Airport_FillConsomationStock, Company_SetDestinationPrice, Airport_SetTaxes, Company_Promotion_System, Company_Advertising, Airport_CheckReportInFolder, Airport_GenerateReport, Customer_AsksForFreeFlight, Luggage_Checkin_Employee, ConsomationStock_Consomation, ConsomationProvider_Consomation, Bob_EditPlanning, Employee_PassengerCheckIn},
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