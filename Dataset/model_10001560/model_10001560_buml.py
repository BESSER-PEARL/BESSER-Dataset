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
Customer_Actor = Class(name="Customer_Actor")
Search_the_route_UseCase = Class(name="Search_the_route_UseCase")
Book_ticket_UseCase = Class(name="Book_ticket_UseCase")
Use_Actor = Class(name="Use_Actor")
customer_management_UseCase = Class(name="customer_management_UseCase")
account_management_UseCase = Class(name="account_management_UseCase")
vehicle_management_UseCase = Class(name="vehicle_management_UseCase")
statistical_reporting_UseCase = Class(name="statistical_reporting_UseCase")
Manager_Actor = Class(name="Manager_Actor")
Customer_Actor1 = Class(name="Customer_Actor1")
book_ticket_UseCase = Class(name="book_ticket_UseCase")
choose_vehicle_UseCase = Class(name="choose_vehicle_UseCase")
choose_seats_UseCase = Class(name="choose_seats_UseCase")
confirm_information_UseCase = Class(name="confirm_information_UseCase")
search_UseCase = Class(name="search_UseCase")
Manager_Actor1 = Class(name="Manager_Actor1")
account_management_UseCase1 = Class(name="account_management_UseCase1")
Login_UseCase = Class(name="Login_UseCase")
Account_settings_UseCase = Class(name="Account_settings_UseCase")
View_account_information_UseCase = Class(name="View_account_information_UseCase")
make_payment_UseCase = Class(name="make_payment_UseCase")
Manager_Actor2 = Class(name="Manager_Actor2")
customer_management_UseCase1 = Class(name="customer_management_UseCase1")
search_customers_UseCase = Class(name="search_customers_UseCase")
confirm_booking_UseCase = Class(name="confirm_booking_UseCase")
cancel_booking_UseCase = Class(name="cancel_booking_UseCase")
View_customers_information_UseCase = Class(name="View_customers_information_UseCase")
Login_UseCase1 = Class(name="Login_UseCase1")
call_for_customers_UseCase = Class(name="call_for_customers_UseCase")
Manager_Actor3 = Class(name="Manager_Actor3")
vehicle_management_UseCase1 = Class(name="vehicle_management_UseCase1")
View_vehicles_information_UseCase = Class(name="View_vehicles_information_UseCase")
Update_vehicles_information_UseCase = Class(name="Update_vehicles_information_UseCase")
Delete_vehicles_UseCase = Class(name="Delete_vehicles_UseCase")
Login_UseCase2 = Class(name="Login_UseCase2")
Manager_Actor4 = Class(name="Manager_Actor4")
statistical_reporting_UseCase1 = Class(name="statistical_reporting_UseCase1")
Report_by_revenue_UseCase = Class(name="Report_by_revenue_UseCase")
Report_by_ticket_amount_UseCase = Class(name="Report_by_ticket_amount_UseCase")
Login_UseCase3 = Class(name="Login_UseCase3")
Car = Class(name="Car")
mapCarExchange = Class(name="mapCarExchange")
infoCompany = Class(name="infoCompany")
Customer = Class(name="Customer")
Ticket = Class(name="Ticket")
accoutUser = Class(name="accoutUser")

# Customer_Actor class attributes and methods

# Search_the_route_UseCase class attributes and methods

# Book_ticket_UseCase class attributes and methods

# Use_Actor class attributes and methods

# customer_management_UseCase class attributes and methods

# account_management_UseCase class attributes and methods

# vehicle_management_UseCase class attributes and methods

# statistical_reporting_UseCase class attributes and methods

# Manager_Actor class attributes and methods

# Customer_Actor1 class attributes and methods

# book_ticket_UseCase class attributes and methods

# choose_vehicle_UseCase class attributes and methods

# choose_seats_UseCase class attributes and methods

# confirm_information_UseCase class attributes and methods

# search_UseCase class attributes and methods

# Manager_Actor1 class attributes and methods

# account_management_UseCase1 class attributes and methods

# Login_UseCase class attributes and methods

# Account_settings_UseCase class attributes and methods

# View_account_information_UseCase class attributes and methods

# make_payment_UseCase class attributes and methods

# Manager_Actor2 class attributes and methods

# customer_management_UseCase1 class attributes and methods

# search_customers_UseCase class attributes and methods

# confirm_booking_UseCase class attributes and methods

# cancel_booking_UseCase class attributes and methods

# View_customers_information_UseCase class attributes and methods

# Login_UseCase1 class attributes and methods

# call_for_customers_UseCase class attributes and methods

# Manager_Actor3 class attributes and methods

# vehicle_management_UseCase1 class attributes and methods

# View_vehicles_information_UseCase class attributes and methods

# Update_vehicles_information_UseCase class attributes and methods

# Delete_vehicles_UseCase class attributes and methods

# Login_UseCase2 class attributes and methods

# Manager_Actor4 class attributes and methods

# statistical_reporting_UseCase1 class attributes and methods

# Report_by_revenue_UseCase class attributes and methods

# Report_by_ticket_amount_UseCase class attributes and methods

# Login_UseCase3 class attributes and methods

# Car class attributes and methods
Car_idCar: Property = Property(name="idCar", type=IntegerType)
Car_idUser: Property = Property(name="idUser", type=IntegerType)
Car_nameCar: Property = Property(name="nameCar", type=StringType)
Car_classifyCar: Property = Property(name="classifyCar", type=IntegerType)
Car_statusCar: Property = Property(name="statusCar", type=IntegerType)
Car_phoneCar: Property = Property(name="phoneCar", type=StringType)
Car_positionStartCar: Property = Property(name="positionStartCar", type=StringType)
Car_positionEndCar: Property = Property(name="positionEndCar", type=StringType)
Car_timeStartCar: Property = Property(name="timeStartCar", type=StringType)
Car_numberPlatesCar: Property = Property(name="numberPlatesCar", type=StringType)
Car_mapOnCar: Property = Property(name="mapOnCar", type=StringType)
Car_mapBelowCar: Property = Property(name="mapBelowCar", type=StringType)
Car_fareCar: Property = Property(name="fareCar", type=StringType)
Car_imageLinkCar: Property = Property(name="imageLinkCar", type=StringType)
Car.attributes={Car_nameCar, Car_classifyCar, Car_mapBelowCar, Car_fareCar, Car_phoneCar, Car_numberPlatesCar, Car_positionEndCar, Car_statusCar, Car_positionStartCar, Car_idUser, Car_mapOnCar, Car_timeStartCar, Car_idCar, Car_imageLinkCar}

# mapCarExchange class attributes and methods
mapCarExchange_mapOnCar: Property = Property(name="mapOnCar", type=StringType)
mapCarExchange_mapBelowCar: Property = Property(name="mapBelowCar", type=StringType)
mapCarExchange_timeExchange: Property = Property(name="timeExchange", type=StringType)
mapCarExchange_idMap: Property = Property(name="idMap", type=IntegerType)
mapCarExchange_idCar: Property = Property(name="idCar", type=IntegerType)
mapCarExchange.attributes={mapCarExchange_mapOnCar, mapCarExchange_timeExchange, mapCarExchange_idMap, mapCarExchange_idCar, mapCarExchange_mapBelowCar}

# infoCompany class attributes and methods
infoCompany_idCompany: Property = Property(name="idCompany", type=IntegerType)
infoCompany_nameCompany: Property = Property(name="nameCompany", type=StringType)
infoCompany_dateEstablish: Property = Property(name="dateEstablish", type=StringType)
infoCompany_phoneCompany: Property = Property(name="phoneCompany", type=StringType)
infoCompany_addressCompany: Property = Property(name="addressCompany", type=StringType)
infoCompany_describeCompany: Property = Property(name="describeCompany", type=StringType)
infoCompany_showSafe: Property = Property(name="showSafe", type=StringType)
infoCompany_dateRegister: Property = Property(name="dateRegister", type=StringType)
infoCompany_dateUpdate: Property = Property(name="dateUpdate", type=StringType)
infoCompany.attributes={infoCompany_addressCompany, infoCompany_idCompany, infoCompany_dateEstablish, infoCompany_phoneCompany, infoCompany_dateRegister, infoCompany_showSafe, infoCompany_nameCompany, infoCompany_describeCompany, infoCompany_dateUpdate}

# Customer class attributes and methods
Customer_idCustomer: Property = Property(name="idCustomer", type=IntegerType)
Customer_nameCustomer: Property = Property(name="nameCustomer", type=StringType)
Customer_phoneCustomer: Property = Property(name="phoneCustomer", type=StringType)
Customer_emailCustomer: Property = Property(name="emailCustomer", type=StringType)
Customer.attributes={Customer_nameCustomer, Customer_phoneCustomer, Customer_idCustomer, Customer_emailCustomer}

# Ticket class attributes and methods
Ticket_idTicket: Property = Property(name="idTicket", type=IntegerType)
Ticket_idCustomer: Property = Property(name="idCustomer", type=IntegerType)
Ticket_idCar: Property = Property(name="idCar", type=IntegerType)
Ticket_numberSeat: Property = Property(name="numberSeat", type=IntegerType)
Ticket_positionSeat: Property = Property(name="positionSeat", type=StringType)
Ticket_positionSeatBelow: Property = Property(name="positionSeatBelow", type=StringType)
Ticket_statusSeat: Property = Property(name="statusSeat", type=IntegerType)
Ticket_timeExchange: Property = Property(name="timeExchange", type=StringType)
Ticket_code: Property = Property(name="code", type=StringType)
Ticket.attributes={Ticket_idCar, Ticket_code, Ticket_numberSeat, Ticket_idCustomer, Ticket_statusSeat, Ticket_idTicket, Ticket_positionSeat, Ticket_timeExchange, Ticket_positionSeatBelow}

# accoutUser class attributes and methods
accoutUser_idUser: Property = Property(name="idUser", type=IntegerType)
accoutUser_emailUser: Property = Property(name="emailUser", type=StringType)
accoutUser_passwordUser: Property = Property(name="passwordUser", type=StringType)
accoutUser_codeConfirm: Property = Property(name="codeConfirm", type=StringType)
accoutUser_dateRegister: Property = Property(name="dateRegister", type=StringType)
accoutUser_idCompany: Property = Property(name="idCompany", type=IntegerType)
accoutUser.attributes={accoutUser_emailUser, accoutUser_idCompany, accoutUser_codeConfirm, accoutUser_passwordUser, accoutUser_idUser, accoutUser_dateRegister}

# Relationships
Use_search: BinaryAssociation = BinaryAssociation(
    name="Use_search",
    ends={
        Property(name="search0", type=Search_the_route_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="use1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Use_UseCase: BinaryAssociation = BinaryAssociation(
    name="Use_UseCase",
    ends={
        Property(name="useCase2", type=Book_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="use3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_customer_management: BinaryAssociation = BinaryAssociation(
    name="Manager_customer_management",
    ends={
        Property(name="customer_management4", type=customer_management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager5", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_account_management: BinaryAssociation = BinaryAssociation(
    name="Manager_account_management",
    ends={
        Property(name="account_management6", type=account_management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager7", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_vehicle_management: BinaryAssociation = BinaryAssociation(
    name="Manager_vehicle_management",
    ends={
        Property(name="vehicle_management8", type=vehicle_management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager9", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_statistical_reporting: BinaryAssociation = BinaryAssociation(
    name="Manager_statistical_reporting",
    ends={
        Property(name="statistical_reporting10", type=statistical_reporting_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager11", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_booking_tickets: BinaryAssociation = BinaryAssociation(
    name="Customer_booking_tickets",
    ends={
        Property(name="booking_tickets12", type=book_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Manager_account_management2: BinaryAssociation = BinaryAssociation(
    name="Manager_account_management2",
    ends={
        Property(name="account_management14", type=account_management_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="manager15", type=Manager_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Manager_customer_management2: BinaryAssociation = BinaryAssociation(
    name="Manager_customer_management2",
    ends={
        Property(name="customer_management16", type=customer_management_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="manager17", type=Manager_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Manager_vehicle_management2: BinaryAssociation = BinaryAssociation(
    name="Manager_vehicle_management2",
    ends={
        Property(name="vehicle_management18", type=vehicle_management_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="manager19", type=Manager_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Manager_statistical_reporting2: BinaryAssociation = BinaryAssociation(
    name="Manager_statistical_reporting2",
    ends={
        Property(name="statistical_reporting20", type=statistical_reporting_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="manager21", type=Manager_Actor4, multiplicity=Multiplicity(0, 1))
    }
)
Car_Car: BinaryAssociation = BinaryAssociation(
    name="Car_Car",
    ends={
        Property(name="Car_Car_022", type=Car, multiplicity=Multiplicity(1, 1)),
        Property(name="Car_Car_123", type=mapCarExchange, multiplicity=Multiplicity(1, 9999))
    }
)
accoutUser_accoutUser: BinaryAssociation = BinaryAssociation(
    name="accoutUser_accoutUser",
    ends={
        Property(name="accoutUser_accoutUser_024", type=accoutUser, multiplicity=Multiplicity(1, 1)),
        Property(name="accoutUser_accoutUser_125", type=Car, multiplicity=Multiplicity(1, 9999))
    }
)
Car_Car2: BinaryAssociation = BinaryAssociation(
    name="Car_Car2",
    ends={
        Property(name="Car_Car2_026", type=Car, multiplicity=Multiplicity(1, 1)),
        Property(name="Car_Car2_127", type=Ticket, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer",
    ends={
        Property(name="Customer_Customer_028", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_Customer_129", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)
infoCompany_infoCompany: BinaryAssociation = BinaryAssociation(
    name="infoCompany_infoCompany",
    ends={
        Property(name="infoCompany_infoCompany_030", type=infoCompany, multiplicity=Multiplicity(1, 1)),
        Property(name="infoCompany_infoCompany_131", type=accoutUser, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_FkGQYI_XEemqpd237shV0A",
    types={Customer_Actor, Search_the_route_UseCase, Book_ticket_UseCase, Use_Actor, customer_management_UseCase, account_management_UseCase, vehicle_management_UseCase, statistical_reporting_UseCase, Manager_Actor, Customer_Actor1, book_ticket_UseCase, choose_vehicle_UseCase, choose_seats_UseCase, confirm_information_UseCase, search_UseCase, Manager_Actor1, account_management_UseCase1, Login_UseCase, Account_settings_UseCase, View_account_information_UseCase, make_payment_UseCase, Manager_Actor2, customer_management_UseCase1, search_customers_UseCase, confirm_booking_UseCase, cancel_booking_UseCase, View_customers_information_UseCase, Login_UseCase1, call_for_customers_UseCase, Manager_Actor3, vehicle_management_UseCase1, View_vehicles_information_UseCase, Update_vehicles_information_UseCase, Delete_vehicles_UseCase, Login_UseCase2, Manager_Actor4, statistical_reporting_UseCase1, Report_by_revenue_UseCase, Report_by_ticket_amount_UseCase, Login_UseCase3, Car, mapCarExchange, infoCompany, Customer, Ticket, accoutUser},
    associations={Use_search, Use_UseCase, Manager_customer_management, Manager_account_management, Manager_vehicle_management, Manager_statistical_reporting, Customer_booking_tickets, Manager_account_management2, Manager_customer_management2, Manager_vehicle_management2, Manager_statistical_reporting2, Car_Car, accoutUser_accoutUser, Car_Car2, Customer_Customer, infoCompany_infoCompany},
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