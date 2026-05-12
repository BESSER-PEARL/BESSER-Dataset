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
UseCase_UseCase = Class(name="UseCase_UseCase")
Reservation_System_Actor1 = Class(name="Reservation_System_Actor1")
round_trip_or_one_way__UseCase = Class(name="round_trip_or_one_way__UseCase")
enter_airport_UseCase1 = Class(name="enter_airport_UseCase1")
enter_date_UseCase = Class(name="enter_date_UseCase")
enter_no__of_tickets_UseCase = Class(name="enter_no__of_tickets_UseCase")
search_flights_UseCase = Class(name="search_flights_UseCase")
select_flight_UseCase = Class(name="select_flight_UseCase")
confirm_purchase_UseCase = Class(name="confirm_purchase_UseCase")
make_payment_UseCase = Class(name="make_payment_UseCase")
reserve_seats_UseCase = Class(name="reserve_seats_UseCase")
print_ticket_UseCase = Class(name="print_ticket_UseCase")
customer_Actor = Class(name="customer_Actor")
Common_fuctions = Class(name="Common_fuctions")
Customer = Class(name="Customer")
Agent = Class(name="Agent")
Booking_counter = Class(name="Booking_counter")
Ticket = Class(name="Ticket")
Reservation_System_Actor = Class(name="Reservation_System_Actor")
round_trip_or_one_way_UseCase = Class(name="round_trip_or_one_way_UseCase")
enter_airport_UseCase = Class(name="enter_airport_UseCase")

# UseCase_UseCase class attributes and methods

# Reservation_System_Actor1 class attributes and methods

# round_trip_or_one_way__UseCase class attributes and methods

# enter_airport_UseCase1 class attributes and methods

# enter_date_UseCase class attributes and methods

# enter_no__of_tickets_UseCase class attributes and methods

# search_flights_UseCase class attributes and methods

# select_flight_UseCase class attributes and methods

# confirm_purchase_UseCase class attributes and methods

# make_payment_UseCase class attributes and methods

# reserve_seats_UseCase class attributes and methods

# print_ticket_UseCase class attributes and methods

# customer_Actor class attributes and methods

# Common_fuctions class attributes and methods

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_ph_no: Property = Property(name="ph_no", type=IntegerType)
Customer.attributes={Customer_ph_no, Customer_name, Customer_address}

# Agent class attributes and methods
Agent_name: Property = Property(name="name", type=StringType)
Agent.attributes={Agent_name}

# Booking_counter class attributes and methods

# Ticket class attributes and methods
Ticket_source: Property = Property(name="source", type=StringType)
Ticket_destination: Property = Property(name="destination", type=StringType)
Ticket_dateofjourney: Property = Property(name="dateofjourney", type=DateType)
Ticket_time: Property = Property(name="time", type=IntegerType)
Ticket_flight_No: Property = Property(name="flight_No", type=StringType)
Ticket_flight_name: Property = Property(name="flight_name", type=StringType)
Ticket.attributes={Ticket_source, Ticket_dateofjourney, Ticket_flight_No, Ticket_time, Ticket_destination, Ticket_flight_name}

# Reservation_System_Actor class attributes and methods

# round_trip_or_one_way_UseCase class attributes and methods

# enter_airport_UseCase class attributes and methods

# Relationships
Reservation_System_search_flights: BinaryAssociation = BinaryAssociation(
    name="Reservation_System_search_flights",
    ends={
        Property(name="search_flights0", type=search_flights_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation_System1", type=Reservation_System_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Reservation_System_make_payment: BinaryAssociation = BinaryAssociation(
    name="Reservation_System_make_payment",
    ends={
        Property(name="make_payment2", type=make_payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation_System3", type=Reservation_System_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Reservation_System_reserve_seats: BinaryAssociation = BinaryAssociation(
    name="Reservation_System_reserve_seats",
    ends={
        Property(name="reserve_seats4", type=reserve_seats_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation_System5", type=Reservation_System_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
customer_round_trip_or_one_way: BinaryAssociation = BinaryAssociation(
    name="customer_round_trip_or_one_way",
    ends={
        Property(name="round_trip_or_one_way6", type=round_trip_or_one_way__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_enter_airport: BinaryAssociation = BinaryAssociation(
    name="customer_enter_airport",
    ends={
        Property(name="enter_airport8", type=enter_airport_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_enter_date: BinaryAssociation = BinaryAssociation(
    name="customer_enter_date",
    ends={
        Property(name="enter_date10", type=enter_date_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_enter_no__of_tickets: BinaryAssociation = BinaryAssociation(
    name="customer_enter_no__of_tickets",
    ends={
        Property(name="enter_no__of_tickets12", type=enter_no__of_tickets_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_search_flights: BinaryAssociation = BinaryAssociation(
    name="customer_search_flights",
    ends={
        Property(name="search_flights14", type=search_flights_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_select_flight: BinaryAssociation = BinaryAssociation(
    name="customer_select_flight",
    ends={
        Property(name="select_flight16", type=select_flight_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer17", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_confirm_purchase: BinaryAssociation = BinaryAssociation(
    name="customer_confirm_purchase",
    ends={
        Property(name="confirm_purchase18", type=confirm_purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer19", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_make_payment: BinaryAssociation = BinaryAssociation(
    name="customer_make_payment",
    ends={
        Property(name="make_payment20", type=make_payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer21", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_print_ticket: BinaryAssociation = BinaryAssociation(
    name="customer_print_ticket",
    ends={
        Property(name="print_ticket22", type=print_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer23", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Booking_counter: BinaryAssociation = BinaryAssociation(
    name="Customer_Booking_counter",
    ends={
        Property(name="booking_counter24", type=Booking_counter, multiplicity=Multiplicity(0, 1)),
        Property(name="customer25", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Ticket: BinaryAssociation = BinaryAssociation(
    name="Customer_Ticket",
    ends={
        Property(name="ticket26", type=Ticket, multiplicity=Multiplicity(0, 1)),
        Property(name="customer27", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Ticket_Booking_counter: BinaryAssociation = BinaryAssociation(
    name="Ticket_Booking_counter",
    ends={
        Property(name="booking_counter28", type=Booking_counter, multiplicity=Multiplicity(0, 1)),
        Property(name="ticket29", type=Ticket, multiplicity=Multiplicity(0, 1))
    }
)
Ticket_Agent: BinaryAssociation = BinaryAssociation(
    name="Ticket_Agent",
    ends={
        Property(name="agent30", type=Agent, multiplicity=Multiplicity(0, 1)),
        Property(name="ticket31", type=Ticket, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_14ff9bc7_2935_4413_89d8_8d680c8f21b9",
    types={UseCase_UseCase, Reservation_System_Actor1, round_trip_or_one_way__UseCase, enter_airport_UseCase1, enter_date_UseCase, enter_no__of_tickets_UseCase, search_flights_UseCase, select_flight_UseCase, confirm_purchase_UseCase, make_payment_UseCase, reserve_seats_UseCase, print_ticket_UseCase, customer_Actor, Common_fuctions, Customer, Agent, Booking_counter, Ticket, Reservation_System_Actor, round_trip_or_one_way_UseCase, enter_airport_UseCase},
    associations={Reservation_System_search_flights, Reservation_System_make_payment, Reservation_System_reserve_seats, customer_round_trip_or_one_way, customer_enter_airport, customer_enter_date, customer_enter_no__of_tickets, customer_search_flights, customer_select_flight, customer_confirm_purchase, customer_make_payment, customer_print_ticket, Customer_Booking_counter, Customer_Ticket, Ticket_Booking_counter, Ticket_Agent},
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